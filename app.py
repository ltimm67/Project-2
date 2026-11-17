"""Project 2 reproducible investment-management decision dashboard."""
import json
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st
from portfolio_engine import (ASSETS, file_sha256, load_prices, mandate_audit, metrics,
                              optimize, portfolio_return_series, realized_summary, statistics)

ROOT = Path(__file__).resolve().parent
PRICES = ROOT / "prices.csv"
st.set_page_config(page_title="Project 2 | Investment Management", page_icon="📈", layout="wide")
st.title("Investment Management Application")
st.caption("Educational decision support only — not investment advice. Inputs are local and versioned.")
rows = load_prices(PRICES)

with st.sidebar:
    st.header("Decision inputs")
    last_36 = st.radio("Estimation window", [False, True], format_func=lambda x: "Last 36 months" if x else "All 60 months")
    hurdle = st.number_input("Net annual return hurdle (%)", 3.0, 12.0, 5.03, 0.01) / 100
    reserve_min = st.number_input("Minimum SGOV reserve (%)", 1.0, 100.0, 3.0, 0.5) / 100
    cost_drag = st.slider("Annual trading-cost drag (bps)", 0, 100, 15, 5) / 10000
    enforce_var = st.checkbox("Enforce modeled 95% normal VaR loss limit")
    signoff = st.checkbox("Committee turnover sign-off obtained")
    st.caption("VaR is a modeled governance assumption; do not call it an original mandate rule without CIO approval.")

annual_returns, vols, cov, corr, returns = statistics(rows, last_36)
current = {"SGOV": 0.40, "RXI": 0.60, "PEJ": 0.0}
optimal = optimize(annual_returns, cov, hurdle, reserve_min, cost_drag, enforce_var=enforce_var)
st.subheader("1. Decision and mandate result")
if optimal is None:
    st.error("No 5%-grid portfolio satisfies net return, reserve, and selected downside constraints. Do not implement.")
    st.stop()
result = metrics(optimal, annual_returns, cov, cost_drag)
rules, turnover, liquidity = mandate_audit(optimal, result, hurdle, reserve_min, current, signoff, enforce_var)
if all(rules.values()):
    st.success("CONDITIONAL PILOT: all selected constraints pass. Monitor and retain implementation evidence.")
else:
    st.warning("DO NOT IMPLEMENT AS-IS: one or more constraints fail or committee turnover sign-off is missing.")
for col, label, value in zip(st.columns(5), ["SGOV", "RXI", "PEJ", "Net return", "Volatility"],
                             [f"{optimal['SGOV']:.0%}", f"{optimal['RXI']:.0%}", f"{optimal['PEJ']:.0%}", f"{result['net_return']:.2%}", f"{result['volatility']:.2%}"]):
    col.metric(label, value)
st.write(f"One-way turnover from the 60/40 current portfolio: **{turnover:.1%}**. Five-day liquidity: **{liquidity:.1%}**.")

st.subheader("2. Rule audit")
audit = pd.DataFrame({"Rule": rules.keys(), "Pass": rules.values()})
audit["Status"] = audit["Pass"].map({True: "PASS", False: "FAIL / SIGN-OFF REQUIRED"})
st.dataframe(audit[["Rule", "Status"]], hide_index=True, use_container_width=True)

st.subheader("3. Transparent baselines")
equal = {a: 1 / 3 for a in ASSETS}
raw_inverse = {a: 1 / vols[a] for a in ASSETS}
inverse = {a: raw_inverse[a] / sum(raw_inverse.values()) for a in ASSETS}
baseline_rows = []
for name, weights in [("Equal weight", equal), ("Inverse volatility", inverse), ("Constrained portfolio", optimal)]:
    m = metrics(weights, annual_returns, cov, cost_drag)
    baseline_rows.append({"Portfolio": name, **weights, "Gross return": m["gross_return"], "Net return": m["net_return"], "Volatility": m["volatility"], "95% normal VaR": m["normal_var_95"]})
formats = {a: "{:.1%}" for a in ASSETS} | {"Gross return": "{:.2%}", "Net return": "{:.2%}", "Volatility": "{:.2%}", "95% normal VaR": "{:.2%}"}
st.dataframe(pd.DataFrame(baseline_rows).style.format(formats), hide_index=True, use_container_width=True)

st.subheader("4. Historical behavior and stability")
summary = realized_summary(portfolio_return_series(optimal, returns))
stress_stats = statistics(rows, True)
stress_weights = optimize(stress_stats[0], stress_stats[2], hurdle, reserve_min, cost_drag, enforce_var=enforce_var)
if stress_weights:
    shift = max(abs(stress_weights[a] - optimal[a]) for a in ASSETS)
    st.write(f"36-month re-estimation largest sleeve shift: **{shift:.1%}**. Formal stop condition: **greater than 25%**.")
st.dataframe(pd.DataFrame([summary]).style.format("{:.2%}"), hide_index=True, use_container_width=True)
st.warning("Known limitations: 60 monthly observations, historical expected returns, normal-VaR approximation, and no live feed. These results are not forecasts.")

st.subheader("5. Provenance and reproducibility")
provenance = {"prices_file": PRICES.name, "rows": len(rows), "as_of_date": rows[-1]["Date"], "sha256": file_sha256(PRICES), "window": "36 months" if last_36 else "60 months", "calculation_date": str(date.today())}
st.code(json.dumps(provenance, indent=2), language="json")
st.caption("A future FRED integration must cache the raw response and its availability/vintage date before any recommendation uses it.")
report = {"provenance": provenance, "inputs": {"hurdle": hurdle, "reserve_min": reserve_min, "cost_drag": cost_drag, "enforce_var": enforce_var, "committee_signoff": signoff}, "weights": optimal, "metrics": result, "rules": rules, "turnover": turnover, "realized_summary": summary}
st.download_button("Download committee decision JSON", json.dumps(report, indent=2), "committee_decision.json", "application/json")
st.download_button("Download portfolio table CSV", pd.DataFrame(baseline_rows).to_csv(index=False), "portfolio_comparison.csv", "text/csv")
