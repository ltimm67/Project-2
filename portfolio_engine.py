"""Deterministic portfolio calculations used by the Streamlit app and tests."""

from __future__ import annotations

import csv
import hashlib
import math
from pathlib import Path

ASSETS = ("SGOV", "RXI", "PEJ")
ASSET_METADATA = {
    "SGOV": {"liquidity_days": 1, "issuer_exempt": True},
    "RXI": {"liquidity_days": 2, "issuer_exempt": True},
    "PEJ": {"liquidity_days": 2, "issuer_exempt": True},
}


def load_prices(path: str | Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))
    if len(rows) < 37:
        raise ValueError("At least 37 monthly observations are required.")
    return rows


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def monthly_returns(rows: list[dict[str, str]], last_36: bool = False) -> dict[str, list[float]]:
    data = rows[-37:] if last_36 else rows
    return {
        asset: [float(data[i][asset]) / float(data[i - 1][asset]) - 1 for i in range(1, len(data))]
        for asset in ASSETS
    }


def statistics(rows: list[dict[str, str]], last_36: bool = False):
    returns = monthly_returns(rows, last_36)
    count = len(next(iter(returns.values())))
    means = {a: sum(returns[a]) / count for a in ASSETS}
    annual_returns = {a: means[a] * 12 for a in ASSETS}
    vols = {
        a: math.sqrt(sum((x - means[a]) ** 2 for x in returns[a]) / (count - 1)) * math.sqrt(12)
        for a in ASSETS
    }
    cov = {
        a: {
            b: sum((returns[a][i] - means[a]) * (returns[b][i] - means[b]) for i in range(count))
            / (count - 1)
            * 12
            for b in ASSETS
        }
        for a in ASSETS
    }
    corr = {a: {b: cov[a][b] / (vols[a] * vols[b]) for b in ASSETS} for a in ASSETS}
    return annual_returns, vols, cov, corr, returns


def metrics(weights, annual_returns, cov, cost_drag=0.0, risk_free=0.0378):
    gross = sum(weights[a] * annual_returns[a] for a in ASSETS)
    variance = sum(weights[a] * cov[a][b] * weights[b] for a in ASSETS for b in ASSETS)
    vol = math.sqrt(max(variance, 0.0))
    return {
        "gross_return": gross,
        "net_return": gross - cost_drag,
        "volatility": vol,
        "sharpe": (gross - risk_free) / vol if vol else 0.0,
        "normal_var_95": gross - 1.645 * vol,
        "reserve": weights["SGOV"],
    }


def one_way_turnover(current, target):
    return 0.5 * sum(abs(target[a] - current[a]) for a in ASSETS)


def optimize(annual_returns, cov, hurdle, reserve_min, cost_drag, step=0.05, enforce_var=False):
    best, best_vol = None, float("inf")
    steps = round(1 / step)
    for i in range(steps + 1):
        for j in range(steps + 1 - i):
            weights = {"SGOV": round(i * step, 4), "RXI": round(j * step, 4), "PEJ": round(1 - i * step - j * step, 4)}
            result = metrics(weights, annual_returns, cov, cost_drag)
            if result["net_return"] < hurdle - 1e-9 or weights["SGOV"] < reserve_min - 1e-9:
                continue
            if enforce_var and result["normal_var_95"] < -0.10:
                continue
            if result["volatility"] < best_vol:
                best, best_vol = weights, result["volatility"]
    return best


def mandate_audit(weights, result, hurdle, reserve_min, current, committee_signoff, enforce_var):
    turnover = one_way_turnover(current, weights)
    liquidity = sum(weights[a] for a in ASSETS if ASSET_METADATA[a]["liquidity_days"] <= 5)
    rules = {
        "Weights sum to 100%": abs(sum(weights.values()) - 1) < 1e-6,
        "Long only": min(weights.values()) >= 0,
        "Net return hurdle": result["net_return"] >= hurdle - 1e-9,
        "Reserve floor": result["reserve"] >= reserve_min - 1e-9,
        "Five-day liquidity": liquidity >= 0.90,
        "Issuer limit": all(ASSET_METADATA[a]["issuer_exempt"] or weights[a] <= 0.08 for a in ASSETS),
        "Turnover <= 25% or signoff": turnover <= 0.25 or committee_signoff,
    }
    if enforce_var:
        rules["95% normal VaR loss <= 10%"] = result["normal_var_95"] >= -0.10
    return rules, turnover, liquidity


def portfolio_return_series(weights, returns):
    return [sum(weights[a] * returns[a][i] for a in ASSETS) for i in range(len(returns["SGOV"]))]


def realized_summary(series):
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
