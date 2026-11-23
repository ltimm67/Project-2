"""Deterministic portfolio calculations used by the Streamlit app, tests, and CLI verification.
Supports canonical 3-asset mandate as well as dynamic multi-asset universes.
"""

from __future__ import annotations

import csv
import hashlib
import math
from pathlib import Path
import random

ASSETS = ("SGOV", "RXI", "PEJ")
ASSET_METADATA = {
    "SGOV": {"liquidity_days": 1, "issuer_exempt": True, "name": "iShares 0-3 Month Treasury Bond ETF", "asset_class": "Cash / Ultra-Short Treasury"},
    "RXI": {"liquidity_days": 2, "issuer_exempt": True, "name": "iShares Global Consumer Discretionary ETF", "asset_class": "Global Discretionary Equity"},
    "PEJ": {"liquidity_days": 2, "issuer_exempt": True, "name": "Invesco Dynamic Leisure and Entertainment ETF", "asset_class": "U.S. Thematic Leisure Equity"},
}


def load_prices(path: str | Path) -> list[dict[str, str]]:
    """Ingest canonical monthly price rows from CSV."""
    with open(path, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))
    if len(rows) < 37:
        raise ValueError("At least 37 monthly observations are required.")
    return rows


def file_sha256(path: str | Path) -> str:
    """Calculate cryptographic SHA-256 hash for dataset provenance."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def monthly_returns(rows: list[dict[str, str]], last_36: bool = False, asset_list: tuple[str, ...] | None = None) -> dict[str, list[float]]:
    """Compute period-by-period monthly percentage returns."""
    assets = asset_list or ASSETS
    data = rows[-37:] if last_36 else rows
    return {
        asset: [float(data[i][asset]) / float(data[i - 1][asset]) - 1 for i in range(1, len(data))]
        for asset in assets
    }


def statistics(rows: list[dict[str, str]], last_36: bool = False, asset_list: tuple[str, ...] | None = None):
    """Compute annualized expected returns, volatilities, covariance, correlation, and return series."""
    assets = asset_list or ASSETS
    returns = monthly_returns(rows, last_36, assets)
    count = len(next(iter(returns.values())))
    means = {a: sum(returns[a]) / count for a in assets}
    annual_returns = {a: means[a] * 12 for a in assets}
    vols = {
        a: math.sqrt(sum((x - means[a]) ** 2 for x in returns[a]) / (count - 1)) * math.sqrt(12)
        for a in assets
    }
    cov = {
        a: {
            b: sum((returns[a][i] - means[a]) * (returns[b][i] - means[b]) for i in range(count))
            / (count - 1)
            * 12
            for b in assets
        }
        for a in assets
    }
    corr = {
        a: {b: cov[a][b] / (vols[a] * vols[b]) if vols[a] * vols[b] > 0 else 0.0 for b in assets}
        for a in assets
    }
    return annual_returns, vols, cov, corr, returns


def metrics(weights: dict[str, float], annual_returns: dict[str, float], cov: dict[str, dict[str, float]], cost_drag: float = 0.0, risk_free: float = 0.0378):
    """Calculate institutional portfolio performance and risk metrics."""
    assets = list(weights.keys())
    gross = sum(weights[a] * annual_returns[a] for a in assets)
    variance = sum(weights[a] * cov[a][b] * weights[b] for a in assets for b in assets)
    vol = math.sqrt(max(variance, 0.0))
    return {
        "gross_return": gross,
        "net_return": gross - cost_drag,
        "volatility": vol,
        "sharpe": (gross - risk_free) / vol if vol else 0.0,
        "normal_var_95": gross - 1.645 * vol,
        "reserve": weights.get("SGOV", 0.0),
    }


def one_way_turnover(current: dict[str, float], target: dict[str, float]) -> float:
    """Calculate one-way turnover: 0.5 * sum(|w_target - w_current|)."""
    all_assets = set(current.keys()) | set(target.keys())
    return 0.5 * sum(abs(target.get(a, 0.0) - current.get(a, 0.0)) for a in all_assets)


def optimize(annual_returns: dict[str, float], cov: dict[str, dict[str, float]], hurdle: float, reserve_min: float, cost_drag: float = 0.0, step: float = 0.05, enforce_var: bool = False, gross_hurdle: bool = False):
    """Exhaustive 5% grid search optimizer for minimum volatility under return hurdle and reserve constraints."""
    best, best_vol = None, float("inf")
    steps = round(1 / step)
    for i in range(steps + 1):
        for j in range(steps + 1 - i):
            weights = {"SGOV": round(i * step, 4), "RXI": round(j * step, 4), "PEJ": round(1 - i * step - j * step, 4)}
            result = metrics(weights, annual_returns, cov, cost_drag)
            ret_check = result["gross_return"] if gross_hurdle else result["net_return"]
            if ret_check < hurdle - 1e-9 or weights["SGOV"] < reserve_min - 1e-9:
                continue
            if enforce_var and result["normal_var_95"] < -0.10:
                continue
            if result["volatility"] < best_vol:
                best, best_vol = weights, result["volatility"]
    return best


def mandate_audit(weights: dict[str, float], result: dict[str, float], hurdle: float, reserve_min: float, current: dict[str, float], committee_signoff: bool = False, enforce_var: bool = False, gross_hurdle: bool = False):
    """Institutional audit of mandate constraints."""
    turnover = one_way_turnover(current, weights)
    liquidity = sum(weights.get(a, 0.0) for a in ASSETS if ASSET_METADATA.get(a, {}).get("liquidity_days", 99) <= 5)
    hurdle_pass = (result["gross_return"] >= hurdle - 1e-9) if gross_hurdle else (result["net_return"] >= hurdle - 1e-9)
    rules = {
        "Weights sum to 100%": abs(sum(weights.values()) - 1) < 1e-6,
        "Long only": min(weights.values()) >= -1e-6,
        "Target return hurdle cleared": hurdle_pass,
        "Net return hurdle": hurdle_pass,
        "Reserve floor": result["reserve"] >= reserve_min - 1e-9,
        "Volatility limit (<= 10%)": result["volatility"] <= 0.1001,
        "Five-day liquidity (>= 90%)": liquidity >= 0.90,
        "Issuer limit (<= 8% unless exempt)": all(ASSET_METADATA.get(a, {}).get("issuer_exempt", False) or weights.get(a, 0.0) <= 0.08 for a in weights),
        "Turnover <= 25% or signoff": turnover <= 0.2501 or committee_signoff,
    }
    if enforce_var:
        rules["95% normal VaR loss <= 10%"] = result["normal_var_95"] >= -0.10
    return rules, turnover, liquidity


def portfolio_return_series(weights: dict[str, float], returns: dict[str, list[float]]) -> list[float]:
    """Compute period-by-period portfolio return series."""
    assets = list(weights.keys())
    n = len(returns[assets[0]])
    return [sum(weights[a] * returns[a][i] for a in assets) for i in range(n)]


def realized_summary(series: list[float]) -> dict[str, float]:
    """Calculate compound annualized return, realized volatility, and maximum drawdown."""
    wealth, peak, max_drawdown = 1.0, 1.0, 0.0
    for value in series:
        wealth *= 1 + value
        peak = max(peak, wealth)
        max_drawdown = min(max_drawdown, wealth / peak - 1)
    years = len(series) / 12
    annualized = wealth ** (1 / years) - 1 if years else 0.0
    mean = sum(series) / len(series)
    vol = math.sqrt(sum((x - mean) ** 2 for x in series) / (len(series) - 1)) * math.sqrt(12)
    return {"annualized_return": annualized, "annualized_volatility": vol, "max_drawdown": max_drawdown}


def simulate_random_portfolios(annual_returns: dict[str, float], cov: dict[str, dict[str, float]], cost_drag: float = 0.0, n_samples: int = 600, seed: int = 42) -> list[dict]:
    """Generate random long-only portfolios to visualize the investment opportunity cloud."""
    rng = random.Random(seed)
    assets = list(annual_returns.keys())
    samples = []
    for _ in range(n_samples):
        raw = [rng.expovariate(1.0) for _ in assets]
        total = sum(raw)
        w = {assets[i]: raw[i] / total for i in range(len(assets))}
        m = metrics(w, annual_returns, cov, cost_drag)
        samples.append({
            "volatility": m["volatility"],
            "net_return": m["net_return"],
            "sharpe": m["sharpe"],
            "weights_str": ", ".join(f"{a}: {w[a]:.1%}" for a in assets),
            **w
        })
    return samples


def generate_efficient_frontier(annual_returns: dict[str, float], cov: dict[str, dict[str, float]], cost_drag: float = 0.0, step: float = 0.02) -> list[dict]:
    """Generate the discrete Markowitz efficient frontier curve via fine-grid search."""
    steps = round(1 / step)
    grid = []
    for i in range(steps + 1):
        for j in range(steps + 1 - i):
            w = {"SGOV": round(i * step, 4), "RXI": round(j * step, 4), "PEJ": round(1 - i * step - j * step, 4)}
            m = metrics(w, annual_returns, cov, cost_drag)
            grid.append({
                "volatility": m["volatility"],
                "net_return": m["net_return"],
                "sharpe": m["sharpe"],
                **w
            })
    # Filter for non-dominated pareto-optimal frontier points
    grid.sort(key=lambda x: x["volatility"])
    frontier = []
    max_return_so_far = -1e9
    for p in grid:
        if p["net_return"] > max_return_so_far:
            frontier.append(p)
            max_return_so_far = p["net_return"]
    return frontier


def calculate_cumulative_wealth(rows: list[dict[str, str]], portfolios: dict[str, dict[str, float]]) -> list[dict]:
    """Generate date-by-date cumulative wealth ($10,000 base) for multiple portfolios."""
    returns = monthly_returns(rows, last_36=False)
    dates = [rows[i]["Date"] for i in range(1, len(rows))]
    
    wealth_track = {name: 10000.0 for name in portfolios}
    history = []
    
    # Initial point
    initial_row = {"Date": rows[0]["Date"]}
    for name in portfolios:
        initial_row[name] = 10000.0
    history.append(initial_row)
    
    for i in range(len(dates)):
        row = {"Date": dates[i]}
        for name, weights in portfolios.items():
            period_ret = sum(weights.get(a, 0.0) * returns[a][i] for a in ASSETS)
            wealth_track[name] *= (1 + period_ret)
            row[name] = round(wealth_track[name], 2)
        history.append(row)
        
    return history


def fetch_yahoo_prices(tickers: list[str], period: str = "5y") -> tuple[list[dict[str, str]] | None, str | None]:
    """Fetch live monthly prices from Yahoo Finance with graceful fallback."""
    try:
        import yfinance as yf
        data = yf.download(tickers, period=period, interval="1mo", auto_adjust=True, progress=False, threads=False)
        if data.empty:
            return None, "Yahoo Finance returned empty data for tickers."
        close = data["Close"] if isinstance(data.columns, object) and "Close" in data else data
        if close.empty:
            return None, "No Close price column found."
        
        # Format as rows of dict with Date and ticker columns
        close = close.dropna()
        rows = []
        for dt, row_data in close.iterrows():
            d_str = dt.strftime("%Y-%m-%d") if hasattr(dt, "strftime") else str(dt)[:10]
            item = {"Date": d_str}
            for t in tickers:
                item[t] = str(round(float(row_data[t]), 4))
            rows.append(item)
        if len(rows) < 12:
            return None, f"Insufficient observations returned ({len(rows)} months)."
        return rows, None
    except Exception as exc:
        return None, str(exc)


def downside_deviation(series: list[float], mar: float = 0.0) -> float:
    """Calculate annualized semi-deviation (downside risk) below minimum acceptable return (MAR)."""
    downside_diffs = [min(x - mar / 12.0, 0.0) ** 2 for x in series]
    n = len(series)
    if n <= 1:
        return 0.0
    return math.sqrt(sum(downside_diffs) / n) * math.sqrt(12)


def sortino_ratio(series: list[float], risk_free: float = 0.0378, mar: float = 0.0) -> float:
    """Calculate annualized Sortino ratio: (Annualized Return - Rf) / Downside Deviation."""
    dd = downside_deviation(series, mar)
    if dd <= 1e-9:
        return 0.0
    mean_ret = sum(series) / len(series) * 12.0
    return (mean_ret - risk_free) / dd


def rebalancing_trade_blotter(current_weights: dict[str, float], target_weights: dict[str, float], total_capital: float, current_prices: dict[str, float] | None = None) -> list[dict]:
    """Generate institutional trade order blotter with dollar trade sizes and share estimates."""
    assets = sorted(list(set(current_weights.keys()) | set(target_weights.keys())))
    blotter = []
    for a in assets:
        curr_w = current_weights.get(a, 0.0)
        targ_w = target_weights.get(a, 0.0)
        curr_dollars = round(curr_w * total_capital, 2)
        targ_dollars = round(targ_w * total_capital, 2)
        trade_dollars = round(targ_dollars - curr_dollars, 2)
        action = "BUY" if trade_dollars > 1.0 else ("SELL" if trade_dollars < -1.0 else "HOLD")
        
        px = current_prices.get(a, 100.0) if current_prices else None
        shares = round(abs(trade_dollars) / px) if px and px > 0 else 0
        
        blotter.append({
            "Asset": a,
            "Current Weight": curr_w,
            "Current Dollars": curr_dollars,
            "Target Weight": targ_w,
            "Target Dollars": targ_dollars,
            "Net Trade ($)": trade_dollars,
            "Action": action,
            "Estimated Price": px,
            "Estimated Shares": shares,
        })
    return blotter


def marginal_risk_contributions(weights: dict[str, float], cov: dict[str, dict[str, float]]) -> dict[str, float]:
    """Calculate institutional percentage contribution of each asset to total portfolio variance.
    RC_i = w_i * (cov @ w)_i / sigma_p^2, summing exactly to 100%.
    """
    assets = list(weights.keys())
    # Compute sigma_p^2
    var_p = sum(weights[a] * cov[a][b] * weights[b] for a in assets for b in assets)
    if var_p <= 1e-12:
        return {a: 0.0 for a in assets}
    
    rc = {}
    for a in assets:
        # marginal covariance
        cov_w_a = sum(cov[a][b] * weights[b] for b in assets)
        rc[a] = round((weights[a] * cov_w_a) / var_p, 4)
    return rc


def tangency_portfolio(annual_returns: dict[str, float], cov: dict[str, dict[str, float]], risk_free: float = 0.0378, cost_drag: float = 0.0, step: float = 0.02) -> dict:
    """Identify the unconstrained Maximum Sharpe Ratio (Tangency) portfolio on the long-only simplex."""
    steps = round(1 / step)
    best_sharpe = -1e9
    best_tangency = None
    for i in range(steps + 1):
        for j in range(steps + 1 - i):
            w = {"SGOV": round(i * step, 4), "RXI": round(j * step, 4), "PEJ": round(1 - i * step - j * step, 4)}
            m = metrics(w, annual_returns, cov, cost_drag, risk_free=risk_free)
            if m["volatility"] > 0 and m["sharpe"] > best_sharpe:
                best_sharpe = m["sharpe"]
                best_tangency = {**w, **m}
    return best_tangency or {}


def historical_crisis_simulations(weights: dict[str, float]) -> list[dict]:
    """Simulate institutional portfolio shock impacts across canonical market crises."""
    crises = [
        {
            "name": "2022 Fed Tightening / Rate Spike",
            "narrative": "Fed hikes rates by 425 bps; long bonds and growth equities tumble while cash preserves nominal value.",
            "shocks": {"SGOV": 0.015, "RXI": -0.220, "PEJ": -0.150},
            "benchmark_60_40_loss": -0.132,
        },
        {
            "name": "2020 COVID Liquidity Freeze (Q1 2020)",
            "narrative": "Global lockdowns trigger panic selloffs in leisure, travel, and retail; Treasuries rally.",
            "shocks": {"SGOV": 0.005, "RXI": -0.280, "PEJ": -0.380},
            "benchmark_60_40_loss": -0.168,
        },
        {
            "name": "2008 Global Financial Crisis (GFC)",
            "narrative": "Systemic credit crisis with severe equity drawdowns; flight to ultra-short government paper.",
            "shocks": {"SGOV": 0.020, "RXI": -0.390, "PEJ": -0.440},
            "benchmark_60_40_loss": -0.234,
        },
        {
            "name": "Stagflationary Energy Shock",
            "narrative": "Persistent inflation curbs consumer discretionary spending while short rates stay pinned near 5%.",
            "shocks": {"SGOV": 0.045, "RXI": -0.120, "PEJ": -0.090},
            "benchmark_60_40_loss": -0.072,
        },
    ]
    results = []
    for c in crises:
        impact = sum(weights.get(a, 0.0) * c["shocks"].get(a, 0.0) for a in weights)
        diff_vs_bench = impact - c["benchmark_60_40_loss"]
        results.append({
            "Crisis Scenario": c["name"],
            "Historical Context": c["narrative"],
            "Estimated Strategy Return": round(impact, 4),
            "Benchmark 60/40 Return": round(c["benchmark_60_40_loss"], 4),
            "Net Fiduciary Protection": round(diff_vs_bench, 4),
        })
    return results


