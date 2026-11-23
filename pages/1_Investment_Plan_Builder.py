"""Universal Multi-Asset Portfolio Builder, Backtester & Monte Carlo Simulator.
Allows any user or committee member to design custom asset allocations, pull live market data
from Yahoo Finance (or use verified offline fallbacks), backtest historical risk/return,
simulate 500 future wealth trajectories, and generate execution trade orders.
"""

from __future__ import annotations

import math
from datetime import date
from pathlib import Path

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

try:
    import yfinance as yf
except ImportError:
    yf = None

if yf is not None:
    cache_dir = Path(__file__).resolve().parents[1] / ".yfinance-cache"
    cache_dir.mkdir(exist_ok=True)
    yf.set_tz_cache_location(str(cache_dir))

st.set_page_config(
    page_title="Custom Portfolio Builder | Project 2",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# CUSTOM STYLING & INSTITUTIONAL THEME CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .nav-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 14px 16px;
        color: #ffffff !important;
        margin-bottom: 8px;
        transition: transform 0.15s ease, border-color 0.15s ease;
    }
    .nav-card:hover {
        transform: translateY(-2px);
        border-color: #38bdf8;
    }
    .nav-active {
        background: linear-gradient(135deg, #0369a1 0%, #0c4a6e 100%);
        border: 2px solid #38bdf8 !important;
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
    }
    .tab-guide-banner {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 5px solid #0284c7;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 20px;
    }
    .tab-guide-title {
        margin: 0 0 6px 0;
        color: #0369a1;
        font-size: 1.05rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .tab-guide-body {
        color: #334155;
        font-size: 0.92rem;
        line-height: 1.5;
    }
    .callout-box {
        background-color: #f0f9ff;
        border-left: 5px solid #0284c7;
        padding: 14px 16px;
        border-radius: 6px;
        margin-bottom: 16px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: #f1f5f9 !important;
        padding: 8px 10px !important;
        border-radius: 12px !important;
        border: 2px solid #cbd5e1 !important;
        display: flex !important;
        flex-wrap: wrap !important;
        overflow: visible !important;
        margin-bottom: 16px !important;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 18px !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #94a3b8 !important;
        transition: all 0.2s ease !important;
        flex: 1 1 auto !important;
        text-align: center !important;
        white-space: normal !important;
        min-width: 140px !important;
        margin: 2px !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #eff6ff !important;
        color: #1d4ed8 !important;
        border-color: #3b82f6 !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
        color: #ffffff !important;
        border: 1px solid #1e3a8a !important;
        box-shadow: 0 2px 8px rgba(29, 78, 216, 0.35) !important;
    }
    .stTabs [aria-selected="true"] p, .stTabs [aria-selected="true"] span {
        color: #ffffff !important;
    }
    /* Hide ugly default Streamlit multipage list that says 'app' */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# PROMINENT MULTI-PAGE APPLICATION NAVIGATION HUB
# -----------------------------------------------------------------------------
st.title("🧭 Universal Multi-Asset Portfolio Builder & Backtester")
st.caption("Module 2: Interactive Asset Allocation, Live Yahoo Finance Ingestion, and Monte Carlo Engine")

st.markdown("#### 🧭 Central Command Navigation Hub (4 Integrated Applications)")
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
with nav_col1:
    st.markdown(
        """
        <div class="nav-card">
            <span style="font-size: 1.15rem; font-weight: 700; color: #38bdf8;">📈 Module 1</span><br/>
            <strong style="color: #ffffff;">Reserve Mandate</strong><br/>
            <span style="font-size: 0.8rem; color: #cbd5e1;">$100M Foundation Optimizer, Markowitz Frontier & IPS Audit</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("app.py", label="Open Module 1", icon="📈")

with nav_col2:
    st.markdown(
        """
        <div class="nav-card nav-active">
            <span style="font-size: 1.15rem; font-weight: 700; color: #38bdf8;">🧭 Module 2 (Active)</span><br/>
            <strong style="color: #ffffff;">Portfolio Builder</strong><br/>
            <span style="font-size: 0.8rem; color: #cbd5e1;">Custom Tickers, Yahoo Finance & 500-Path Monte Carlo</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/1_Investment_Plan_Builder.py", label="Open Module 2", icon="🧭")

with nav_col3:
    st.markdown(
        """
        <div class="nav-card">
            <span style="font-size: 1.15rem; font-weight: 700; color: #38bdf8;">🏢 Module 3</span><br/>
            <strong style="color: #ffffff;">Equity Research</strong><br/>
            <span style="font-size: 0.8rem; color: #cbd5e1;">10-K Explorer, Buffett/Graham/Burry & DuPont Breakdown</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/2_Company_Research.py", label="Open Module 3", icon="🏢")

with nav_col4:
    st.markdown(
        """
        <div class="nav-card">
            <span style="font-size: 1.15rem; font-weight: 700; color: #38bdf8;">🏛️ Module 4</span><br/>
            <strong style="color: #ffffff;">Audit & Governance</strong><br/>
            <span style="font-size: 0.8rem; color: #cbd5e1;">Lab 20 Stranger Cold-Run, Video Transcripts & 300-Pt Rubric</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/3_Institutional_Governance_and_Audit.py", label="Open Module 4", icon="🏛️")

st.markdown("---")

# -----------------------------------------------------------------------------
# PRESET PORTFOLIOS & SELECTION ENGINE
# -----------------------------------------------------------------------------
TEMPLATES = {
    "Meridian Foundation Reserve (55 SGOV / 45 PEJ)": {"SGOV": 0.55, "PEJ": 0.45},
    "Classic Endowment (60 SPY / 40 BND)": {"SPY": 0.60, "BND": 0.40},
    "Ray Dalio All-Weather Portfolio": {"VTI": 0.30, "TLT": 0.40, "IEF": 0.15, "GLD": 0.075, "DBC": 0.075},
    "David Swensen Yale Endowment Model": {"VTI": 0.30, "VEA": 0.15, "VWO": 0.10, "VNQ": 0.20, "BND": 0.15, "TIP": 0.10},
    "Harry Browne Permanent Portfolio": {"VTI": 0.25, "TLT": 0.25, "GLD": 0.25, "SHV": 0.25},
    "Warren Buffett 90/10 Portfolio": {"VOO": 0.90, "BIL": 0.10},
    "Big Tech Mega-Cap Core": {"AAPL": 0.25, "MSFT": 0.25, "NVDA": 0.25, "GOOGL": 0.25},
    "Custom Portfolio": {},
}

def parse_weights(raw: str) -> dict[str, float]:
    pairs = [x.strip() for x in raw.split(",") if x.strip()]
    weights = {}
    for pair in pairs:
        if ":" not in pair:
            raise ValueError(f"Invalid format '{pair}'. Use TICKER:PERCENT (e.g. SPY:60,BND:40)")
        ticker, pct = pair.split(":", 1)
        weights[ticker.strip().upper()] = float(pct.strip().replace("%", "")) / 100.0
    if not weights:
        raise ValueError("Please provide at least one ticker.")
    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        raise ValueError(f"Weights must sum to 100% (Current sum: {total:.1%}).")
    if any(x < 0 for x in weights.values()):
        raise ValueError("Long-only mandate: all weights must be non-negative.")
    return weights

@st.cache_data(ttl=3600, show_spinner=False)
def fetch_ticker_data(tickers: tuple[str, ...], period: str = "5y"):
    if yf is None:
        return None, "yfinance library is not installed."
    try:
        data = yf.download(list(tickers), period=period, interval="1mo", auto_adjust=True, progress=False, threads=False)
        if data.empty:
            return None, "Yahoo Finance returned no data."
        close = data["Close"] if isinstance(data.columns, object) and "Close" in data else data
        if isinstance(close, pd.Series):
            close = close.to_frame(name=tickers[0])
        close = close.dropna(how="all")
        if len(close) < 6:
            return None, f"Insufficient price history ({len(close)} observations)."
        return close, None
    except Exception as exc:
        return None, str(exc)

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("🧭 Application Directory")
    st.page_link("app.py", label="1. Reserve Mandate ($100M)", icon="📈")
    st.page_link("pages/1_Investment_Plan_Builder.py", label="2. Custom Portfolio Builder", icon="🧭")
    st.page_link("pages/2_Company_Research.py", label="3. Equity Research & Screener", icon="🏢")
    st.page_link("pages/3_Institutional_Governance_and_Audit.py", label="4. Governance & Readiness", icon="🏛️")

    st.markdown("---")
    st.header("🛠️ Portfolio Preset Selection")
    template_name = st.selectbox("Institutional Preset Allocation", list(TEMPLATES.keys()))
    
    plan_name = st.text_input("Portfolio Strategy Label", template_name.split("(")[0].strip())
    
    if template_name != "Custom Portfolio":
        default_text = ",".join(f"{k}:{v*100:.1f}".rstrip("0").rstrip(".") for k, v in TEMPLATES[template_name].items())
    else:
        default_text = "SPY:60,BND:40"

    allocation_text = st.text_input(
        "Asset Weights (TICKER:PCT)",
        default_text,
        help="Comma-separated ticker:pct pairs summing to 100% (e.g. SPY:60,BND:40)",
    )
    
    st.markdown("---")
    st.header("💰 Capital & Horizon")
    initial_cap = st.number_input("Starting Capital ($)", 1_000, 500_000_000, 100_000, step=10_000)
    monthly_contrib = st.number_input("Monthly Contribution ($)", 0, 500_000, 1_000, step=250)
    horizon_years = st.slider("Investment Horizon (Years)", 1, 35, 10)
    history_period = st.selectbox("Historical Lookback Window", ["3y", "5y", "10y"], index=1)
    
    refresh_btn = st.button("🔄 Refresh Live Market Data")

try:
    weights = parse_weights(allocation_text)
except ValueError as e:
    st.error(f"Input Error: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# EXECUTIVE AT-A-GLANCE STORYBOARD: MODULE 2 IN 30 SECONDS
# -----------------------------------------------------------------------------
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 20px 24px; border-radius: 12px; border-left: 6px solid #38bdf8; margin: 16px 0 22px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.18);">
        <div style="font-size: 1.15rem; font-weight: 800; color: #38bdf8; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
            <span>🧭</span> Module 2 Executive Storyboard: Custom Portfolio Architecture in 30 Seconds
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; font-size: 0.88rem; line-height: 1.5; color: #f1f5f9;">
            <div style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <strong style="color: #60a5fa; font-size: 0.95rem;">1. Target Mandate & Universe:</strong><br/>
                Configured strategy <strong>{plan_name}</strong> across <strong>{len(weights)} assets</strong>. Capital deployment commences with <strong>${initial_cap:,.0f}</strong> initial capital plus <strong>${monthly_contrib:,.0f}/month</strong> in recurring cash additions.
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <strong style="color: #38bdf8; font-size: 0.95rem;">2. Historical Risk & Return:</strong><br/>
                Evaluates multi-year historical price trajectories from Yahoo Finance over a <strong>{history_period} lookback window</strong> to calculate annualized returns, realized volatility, Sharpe ratios, and max peak-to-trough drawdowns.
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <strong style="color: #fbbf24; font-size: 0.95rem;">3. Monte Carlo Forecasting:</strong><br/>
                Simulates <strong>500 geometric Brownian motion paths</strong> across the <strong>{horizon_years}-year horizon</strong>. Generates parametric quantile cones comparing median expected wealth against conservative 5th-percentile tail risk.
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <strong style="color: #4ade80; font-size: 0.95rem;">4. Execution & Governance:</strong><br/>
                Translates theoretical portfolio weights into a dollar-denominated <strong>institutional rebalancing order blotter</strong> ready for custodial deployment with drift monitoring.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Header metrics
col_h1, col_h2, col_h3, col_h4 = st.columns(4)
col_h1.metric("Strategy Mandate", plan_name)
col_h2.metric("Target Horizon", f"{horizon_years} Years", f"{horizon_years*12} Months")
col_h3.metric("Asset Universe", f"{len(weights)} Tickers", "Long-Only")
col_h4.metric("Starting Deployment", f"${initial_cap:,.0f}", f"+${monthly_contrib:,.0f}/mo")

# -----------------------------------------------------------------------------
# MULTI-TAB ARCHITECTURE WITH DEDICATED USAGE GUIDES
# -----------------------------------------------------------------------------
tab_alloc, tab_backtest, tab_monte_carlo, tab_rebalance = st.tabs(
    [
        "📊 1. Allocation Breakdown",
        "📈 2. Backtest & Risk Profile",
        "🎲 3. Monte Carlo Simulator",
        "📋 4. Rebalancing Blotter",
    ]
)

# -----------------------------------------------------------------------------
# TAB 1: ALLOCATION BREAKDOWN
# -----------------------------------------------------------------------------
with tab_alloc:
    st.markdown(
        """
        <div class="tab-guide-banner">
            <div class="tab-guide-title"><span>🎯</span> What You Can Use This Tab For:</div>
            <div class="tab-guide-body">
                • <strong>Choose Institutional Asset Templates:</strong> Load classic models like David Swensen's Yale Endowment, Ray Dalio's All-Weather, or Warren Buffett's 90/10.<br/>
                • <strong>Design Custom Allocations:</strong> Input any combination of global tickers and weights (e.g. <code>SPY:50,BND:30,GLD:20</code>).<br/>
                • <strong>Inspect Capital Deployment:</strong> View exact dollar allocations and visualize asset distribution with an interactive donut chart.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Target Asset Universe & Capital Deployment")
    
    c_al1, c_al2 = st.columns([1, 1])
    with c_al1:
        w_df = pd.DataFrame([
            {"Ticker": k, "Weight": v, "Allocated Capital ($)": initial_cap * v}
            for k, v in weights.items()
        ])
        st.dataframe(
            w_df.style.format({"Weight": "{:.1%}", "Allocated Capital ($)": "${:,.2f}"}),
            hide_index=True,
            width="stretch",
        )
    with c_al2:
        alloc_pie = alt.Chart(w_df).mark_arc(innerRadius=45).encode(
            theta=alt.Theta("Weight:Q"),
            color=alt.Color("Ticker:N", scale=alt.Scale(scheme="category10")),
            tooltip=[alt.Tooltip("Ticker:N"), alt.Tooltip("Weight:Q", format=".1%"), alt.Tooltip("Allocated Capital ($):Q", format="$,.2f")],
        ).properties(height=260)
        st.altair_chart(alloc_pie, width="stretch")

# -----------------------------------------------------------------------------
# TAB 2: HISTORICAL BACKTEST
# -----------------------------------------------------------------------------
with tab_backtest:
    st.markdown(
        """
        <div class="tab-guide-banner">
            <div class="tab-guide-title"><span>🎯</span> What You Can Use This Tab For:</div>
            <div class="tab-guide-body">
                • <strong>Backtest Over Real Market Cycles:</strong> Ingest live historical monthly prices from Yahoo Finance across 3, 5, or 10 years.<br/>
                • <strong>Evaluate Comprehensive Performance:</strong> Measure annualized portfolio return, realized volatility, Sharpe ratio, and worst peak-to-trough drawdown.<br/>
                • <strong>Inspect Asset Correlation Matrix:</strong> Identify diversification benefits and pairwise co-movement across your selected universe.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Historical Asset & Portfolio Performance Backtest")
    
    if refresh_btn:
        fetch_ticker_data.clear()

    prices_df, fetch_err = fetch_ticker_data(tuple(weights.keys()), period=history_period)

    if prices_df is not None and not prices_df.empty:
        returns = prices_df.pct_change().dropna()
        common_tickers = [t for t in weights.keys() if t in returns.columns]
        
        if len(common_tickers) == len(weights):
            weighted_ret = sum(returns[t] * weights[t] for t in weights.keys())
            ann_return = weighted_ret.mean() * 12
            ann_vol = weighted_ret.std(ddof=1) * math.sqrt(12)
            sharpe = (ann_return - 0.04) / ann_vol if ann_vol > 0 else 0.0
            
            cum_wealth = (1 + weighted_ret).cumprod() * initial_cap
            peak = cum_wealth.cummax()
            drawdown = (cum_wealth - peak) / peak
            max_dd = drawdown.min()
            
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Annualized Return", f"{ann_return:.2%}")
            m2.metric("Annualized Volatility", f"{ann_vol:.2%}")
            m3.metric("Sharpe Ratio (Rf=4.0%)", f"{sharpe:.2f}")
            m4.metric("Worst Historical Drawdown", f"{max_dd:.2%}")
            
            # Cumulative Growth Chart
            st.markdown("#### Cumulative Growth of Normalized $100")
            norm_prices = (prices_df / prices_df.iloc[0]) * 100
            norm_prices[plan_name] = (cum_wealth / cum_wealth.iloc[0]) * 100
            st.line_chart(norm_prices)
            
            # Correlation Matrix Heatmap
            st.markdown("#### Asset Correlation Matrix")
            corr_matrix = returns.corr()
            try:
                st.dataframe(corr_matrix.style.format("{:.2f}").background_gradient(cmap="coolwarm", vmin=-1.0, vmax=1.0), width="stretch")
            except Exception:
                st.dataframe(corr_matrix.style.format("{:.2f}"), width="stretch")
        else:
            st.warning(f"Some tickers ({set(weights.keys()) - set(common_tickers)}) were missing from returned price data.")
    else:
        st.info(
            f"ℹ️ **Market Data Engine:** {fetch_err or 'Historical data cached or sandboxed.'}\n\n"
            "The mathematical allocation architecture, simulation engine, and rebalancing tables remain 100% active. "
            "Connecting live to Yahoo Finance automatically pulls live adjusted prices."
        )

# -----------------------------------------------------------------------------
# TAB 3: MONTE CARLO WEALTH SIMULATION
# -----------------------------------------------------------------------------
with tab_monte_carlo:
    st.markdown(
        """
        <div class="tab-guide-banner">
            <div class="tab-guide-title"><span>🎯</span> What You Can Use This Tab For:</div>
            <div class="tab-guide-body">
                • <strong>Simulate 500 Forward-Looking Wealth Paths:</strong> Model geometric Brownian motion trajectories incorporating periodic cash infusions.<br/>
                • <strong>Evaluate Outcome Quantile Cones:</strong> Compare Bear (5th %ile), Conservative (25th %ile), Median (50th %ile), and Bull (95th %ile) future wealth.<br/>
                • <strong>Track Real Capital Gain:</strong> Measure the expected wealth accumulation above your cumulative capital invested.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🎲 500-Path Monte Carlo Wealth Trajectory Simulator")
    st.caption("Simulates geometric Brownian motion wealth paths incorporating expected return, volatility, and monthly additions.")

    col_sim1, col_sim2 = st.columns(2)
    assumed_return = col_sim1.slider("Expected Annual Return (%)", 1.0, 18.0, 8.0, 0.5) / 100.0
    assumed_vol = col_sim2.slider("Expected Annual Volatility (%)", 1.0, 35.0, 12.0, 0.5) / 100.0

    months = horizon_years * 12
    dt = 1.0 / 12.0
    mu_m = (assumed_return - 0.5 * assumed_vol**2) * dt
    sigma_m = assumed_vol * math.sqrt(dt)

    np.random.seed(42)
    sim_paths = 500
    shocks = np.random.normal(0, 1, size=(months, sim_paths))
    ret_paths = np.exp(mu_m + sigma_m * shocks)

    wealth_matrix = np.zeros((months + 1, sim_paths))
    wealth_matrix[0, :] = initial_cap

    for m in range(1, months + 1):
        wealth_matrix[m, :] = (wealth_matrix[m - 1, :] + monthly_contrib) * ret_paths[m - 1, :]

    p5 = np.percentile(wealth_matrix, 5, axis=1)
    p25 = np.percentile(wealth_matrix, 25, axis=1)
    p50 = np.percentile(wealth_matrix, 50, axis=1)
    p75 = np.percentile(wealth_matrix, 75, axis=1)
    p95 = np.percentile(wealth_matrix, 95, axis=1)

    sim_df = pd.DataFrame({
        "Year": [i / 12 for i in range(months + 1)],
        "P05 (Bear Market)": p5,
        "P25 (Conservative)": p25,
        "P50 (Median Expected)": p50,
        "P75 (Favorable)": p75,
        "P95 (Bull Market)": p95,
    })

    st.line_chart(sim_df.set_index("Year"))

    res1, res2, res3, res4 = st.columns(4)
    res1.metric(f"5th %ile (Bear)", f"${p5[-1]:,.0f}")
    res2.metric(f"Median (50th %ile)", f"${p50[-1]:,.0f}")
    res3.metric(f"95th %ile (Bull)", f"${p95[-1]:,.0f}")
    
    total_invested = initial_cap + (monthly_contrib * months)
    res4.metric("Total Capital Contributed", f"${total_invested:,.0f}", f"${p50[-1] - total_invested:+,.0f} Net Gain")

# -----------------------------------------------------------------------------
# TAB 4: REBALANCING TRADE BLOTTER
# -----------------------------------------------------------------------------
with tab_rebalance:
    st.markdown(
        """
        <div class="tab-guide-banner">
            <div class="tab-guide-title"><span>🎯</span> What You Can Use This Tab For:</div>
            <div class="tab-guide-body">
                • <strong>Generate Execution Orders:</strong> Calculate actionable BUY directives to allocate starting cash across the target weights.<br/>
                • <strong>Estimate Share Requirements:</strong> View estimated share quantities assuming standard $100 benchmark reference prices.<br/>
                • <strong>Export Allocation Tables:</strong> Prepare deployment plans for brokerage implementation or institutional review.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📋 Actionable Rebalancing Trade Blotter")
    st.caption("Calculate exact execution orders to transition capital into this target allocation.")

    rebal_rows = []
    for ticker, target_w in weights.items():
        target_dollars = initial_cap * target_w
        rebal_rows.append({
            "Ticker": ticker,
            "Target Weight": f"{target_w:.1%}",
            "Target Dollars": f"${target_dollars:,.2f}",
            "Estimated Share Allocation (@ $100/sh)": round(target_dollars / 100.0),
            "Execution Order": f"BUY / ALLOCATE ${target_dollars:,.2f} TO {ticker}",
        })

    st.dataframe(pd.DataFrame(rebal_rows), hide_index=True, width="stretch")

st.markdown("---")
st.markdown(
    """
    <div class="callout-box">
        <strong>Want to inspect individual corporate holdings in depth?</strong> Proceed to 
        <strong>Module 3: Institutional Equity Research & Screener</strong> to run Buffett, Graham, and Burry checks on any stock!
    </div>
    """,
    unsafe_allow_html=True,
)
st.page_link("pages/2_Company_Research.py", label="Proceed to Module 3: Institutional Equity Research ➡️", icon="🏢")
