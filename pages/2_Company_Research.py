"""Ticker-driven business, financials, and valuation research page."""
from pathlib import Path
import pandas as pd
import streamlit as st

try:
    import yfinance as yf
except ImportError:
    yf = None

st.set_page_config(page_title="Company Research", page_icon="🏢", layout="wide")
st.title("Company Research")
st.warning("Educational research only — not individualized investment advice. Verify primary filings before making a decision.")

if yf is not None:
    cache_dir = Path(__file__).resolve().parents[1] / ".yfinance-cache"
    cache_dir.mkdir(exist_ok=True)
    yf.set_tz_cache_location(str(cache_dir))

def money(value):
    if value is None or pd.isna(value): return "Not available"
    for suffix, divisor in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if abs(float(value)) >= divisor: return f"${float(value)/divisor:,.2f}{suffix}"
    return f"${float(value):,.0f}"

def multiple(value):
    return "Not available" if value is None or pd.isna(value) else f"{float(value):,.2f}x"

@st.cache_data(ttl=3600, show_spinner=False)
def company_data(ticker):
    if yf is None: raise RuntimeError("Install requirements.txt to use market data.")
    company = yf.Ticker(ticker)
    info, history = company.info or {}, company.history(period="1y", auto_adjust=True)
    if not info and history.empty: raise RuntimeError("No data returned. Check the ticker or try again later.")
    return info, company.income_stmt, company.balance_sheet, company.cashflow, history

with st.sidebar:
    st.header("Company input")
    ticker = st.text_input("Ticker", "AAPL").strip().upper()
    refresh = st.button("Refresh company data")
    st.caption("One ticker updates every tab. Results are cached for one hour.")

try:
    if refresh: company_data.clear()
    info, income, balance, cashflow, history = company_data(ticker)
except Exception as exc:
    st.error(f"Could not retrieve {ticker}: {exc}")
    st.stop()

st.subheader(f"{info.get('longName', ticker)} ({ticker})")
business_tab, financials_tab, valuation_tab = st.tabs(["Business", "Financials", "Valuation"])

with business_tab:
    left, right = st.columns([2, 1])
    with left:
        st.markdown("### Business overview")
        st.write(info.get("longBusinessSummary", "Business description unavailable."))
    with right:
        st.markdown("### Profile")
        for label, key in [("Sector", "sector"), ("Industry", "industry"), ("Country", "country"), ("Employees", "fullTimeEmployees")]:
            st.write(f"**{label}:** {info.get(key, 'Not available')}")
        if info.get("website"): st.link_button("Company website", info["website"])
    st.dataframe(pd.DataFrame({"Value": [money(info.get("marketCap")), money(info.get("enterpriseValue")), info.get("fiftyTwoWeekHigh"), info.get("fiftyTwoWeekLow"), info.get("dividendYield")]}, index=["Market capitalization", "Enterprise value", "52-week high", "52-week low", "Dividend yield"]), use_container_width=True)
    if not history.empty: st.line_chart(history["Close"], y_label="Adjusted close")

with financials_tab:
    for label, statement in [("Income statement", income), ("Balance sheet", balance), ("Cash-flow statement", cashflow)]:
        st.markdown(f"### {label}")
        st.dataframe(statement if statement is not None and not statement.empty else pd.DataFrame({"Status": ["Not available"]}), use_container_width=True)

with valuation_tab:
    valuation = pd.DataFrame({"Value": [money(info.get("marketCap")), money(info.get("enterpriseValue")), multiple(info.get("trailingPE")), multiple(info.get("forwardPE")), multiple(info.get("priceToBook")), multiple(info.get("enterpriseToEbitda")), multiple(info.get("priceToSalesTrailing12Months")), multiple(info.get("beta"))]}, index=["Market capitalization", "Enterprise value", "Trailing P/E", "Forward P/E", "Price / book", "EV / EBITDA", "Price / sales", "Beta (5Y monthly)"])
    st.markdown("### Market-based valuation context")
    st.dataframe(valuation, use_container_width=True)
    st.markdown("### Scenario valuation calculator")
    c1, c2, c3 = st.columns(3)
    earnings = c1.number_input("Normalized earnings / EBITDA ($M)", 0.0, value=100.0, step=10.0)
    chosen_multiple = c2.number_input("Valuation multiple (x)", 0.0, value=15.0, step=0.5)
    net_debt = c3.number_input("Net debt ($M; negative = net cash)", value=0.0, step=10.0)
    st.metric("Illustrative equity value", money(earnings * chosen_multiple * 1_000_000 - net_debt * 1_000_000), "User-input scenario, not a price target")
    st.info("Use audited filings and a documented peer set to support your assumptions. This is a sensitivity calculator, not a recommendation.")

st.caption("Source: Yahoo Finance data through open-source yfinance. It is not affiliated with Yahoo; independently verify figures and review Yahoo's terms before relying on data.")
