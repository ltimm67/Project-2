"""Educational, client-side investment-plan builder using optional Yahoo Finance data."""
from __future__ import annotations

import math
from datetime import date

import pandas as pd
import streamlit as st

try:
    import yfinance as yf
except ImportError:
    yf = None


st.set_page_config(page_title="Investment Plan Builder", page_icon="🧭", layout="wide")
st.title("Investment Plan Builder")
st.warning("Educational planning tool only — not individualized financial, tax, or investment advice. It does not trade, connect to accounts, or store personal information.")

TEMPLATES = {
    "Conservative example (40/60)": {"VT": 0.40, "BND": 0.60},
    "Balanced example (60/40)": {"VT": 0.60, "BND": 0.40},
    "Growth example (80/20)": {"VT": 0.80, "BND": 0.20},
    "Custom": {},
}


def parse_weights(raw: str) -> dict[str, float]:
    pairs = [x.strip() for x in raw.split(",") if x.strip()]
    weights = {}
    for pair in pairs:
        ticker, pct = pair.split(":", 1)
        weights[ticker.strip().upper()] = float(pct.strip().replace("%", "")) / 100
    if not weights or abs(sum(weights.values()) - 1) > 0.001 or any(x < 0 for x in weights.values()):
        raise ValueError("Use ticker:percent pairs that add to 100%, for example VT:60,BND:40.")
    return weights


@st.cache_data(ttl=3600, show_spinner=False)
def prices_for(tickers: tuple[str, ...]):
    if yf is None:
        raise RuntimeError("yfinance is not installed. Run pip install -r requirements.txt.")
    data = yf.download(list(tickers), period="5y", interval="1mo", auto_adjust=True, progress=False, threads=False)
    if data.empty:
        raise RuntimeError("No market data returned. Check symbols or try again later.")
    close = data["Close"] if isinstance(data.columns, pd.MultiIndex) else data[["Close"]].rename(columns={"Close": tickers[0]})
    if isinstance(close, pd.Series):
        close = close.to_frame(name=tickers[0])
    return close.dropna(how="all")


with st.sidebar:
    st.header("Plan inputs")
    plan_name = st.text_input("Plan label", "My diversified plan")
    years = st.slider("Investment horizon (years)", 1, 40, 15)
    risk = st.selectbox("Comfort with volatility", ["Lower", "Moderate", "Higher"])
    initial = st.number_input("Starting amount ($)", 0, 10_000_000, 10_000, 500)
    monthly = st.number_input("Monthly contribution ($)", 0, 100_000, 500, 50)
    template_name = st.selectbox("Allocation template", list(TEMPLATES))
    default = ",".join(f"{k}:{v:.0%}" for k, v in TEMPLATES[template_name].items()) or "VT:60,BND:40"
    allocation_text = st.text_input("Ticker allocation (ticker:percent)", default)
    refresh = st.button("Refresh market data")
    st.caption("Templates are broad-asset-class examples, not recommendations. Edit or replace all tickers yourself.")

try:
    weights = parse_weights(allocation_text)
except (ValueError, TypeError) as exc:
    st.error(str(exc))
    st.stop()

st.subheader("1. Your written plan")
st.write(f"**{plan_name}** | Horizon: **{years} years** | Volatility preference: **{risk}** | Contributions: **${monthly:,.0f}/month**")
allocation = pd.DataFrame({"Ticker": weights.keys(), "Weight": weights.values()})
st.dataframe(allocation.style.format({"Weight": "{:.1%}"}), hide_index=True, use_container_width=True)

st.subheader("2. Market-data check")
st.caption("Data source: Yahoo Finance through the open-source `yfinance` package. It is intended for personal/research use; verify data and licensing before any other use.")
try:
    if refresh:
        prices_for.clear()
    prices = prices_for(tuple(weights))
    returns = prices.pct_change().dropna()
    weighted = returns.mul(pd.Series(weights), axis=1).sum(axis=1)
    annual_return = weighted.mean() * 12
    annual_vol = weighted.std(ddof=1) * math.sqrt(12)
    wealth = (1 + weighted).cumprod()
    drawdown = wealth / wealth.cummax() - 1
    c1, c2, c3 = st.columns(3)
    c1.metric("Historical annualized return", f"{annual_return:.2%}")
    c2.metric("Historical annualized volatility", f"{annual_vol:.2%}")
    c3.metric("Largest monthly-series drawdown", f"{drawdown.min():.2%}")
    st.line_chart(prices / prices.iloc[0] * 100)
except Exception as exc:
    st.info(f"Live data is unavailable: {exc}. The allocation and planning sections still work, but no historical metrics are shown.")
    annual_return, annual_vol = 0.06, 0.12

st.subheader("3. Goal projection — assumptions, not a forecast")
expected_return = st.slider("Illustrative annual return assumption (%)", -5.0, 15.0, float(round(annual_return * 100, 1)), 0.1) / 100
monthly_rate = expected_return / 12
months = years * 12
future_value = initial * (1 + monthly_rate) ** months
if monthly_rate:
    future_value += monthly * (((1 + monthly_rate) ** months - 1) / monthly_rate)
else:
    future_value += monthly * months
contributed = initial + monthly * months
st.metric("Illustrative end value", f"${future_value:,.0f}", f"Contributed: ${contributed:,.0f}")
projection = pd.DataFrame({"Year": range(years + 1)})
projection["Illustrative value"] = [initial * (1 + expected_return) ** y + monthly * 12 * (((1 + expected_return) ** y - 1) / expected_return if expected_return else y) for y in projection["Year"]]
st.line_chart(projection.set_index("Year"))

st.subheader("4. Implementation and review checklist")
st.markdown("""
- Keep an emergency fund and address high-interest debt before investing.
- Confirm fund fees, taxes, account type, liquidity, and concentration before acting.
- Rebalance on a documented schedule or when weights drift materially; avoid reacting to short-term performance.
- Review the plan after a goal, income, tax, or risk-capacity change.
- Consult a qualified fiduciary professional for individualized advice.
""")

report = {"created_on": str(date.today()), "plan_label": plan_name, "horizon_years": years, "risk_preference": risk, "allocation": weights, "initial_amount": initial, "monthly_contribution": monthly, "illustrative_return_assumption": expected_return, "illustrative_end_value": future_value}
st.download_button("Download plan JSON", pd.Series(report).to_json(indent=2), "investment_plan.json", "application/json")
