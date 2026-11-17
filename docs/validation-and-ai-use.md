# Validation and AI Use Log: Project 2

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Analyst:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Client / Mandate:** Meridian Foundation Reserve ($100 Million Portfolio)  

---

## 1. Mandatory Statements on AI Use and Academic Authorship
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## 2. Quantitative Validation Log & Data Provenance

### Asset Universe Ingestion & Audit
All price data is ingested from [`prices.csv`](../prices.csv) containing 60 completed monthly adjusted close observations spanning from October 1, 2021 through September 1, 2026:

| Ticker | Full ETF Name | Role in Mandate | 60-Month Annualized Return | 60-Month Volatility | 36-Month Return | 36-Month Volatility | Data Source |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|
| **SGOV** | iShares 0-3 Month Treasury Bond ETF | Cash reserve; sole reserve-eligible asset | **3.78%** | **0.48%** | 4.44% | 0.21% | Yahoo Finance Adj Close |
| **RXI** | iShares Global Consumer Discretionary ETF | Global equity benchmark proxy | **3.53%** | **19.07%** | 10.14% | 15.17% | Yahoo Finance Adj Close |
| **PEJ** | Invesco Leisure & Entertainment ETF | Consumer / lodging / hospitality tilt | **6.85%** | **21.22%** | 17.97% | 17.27% | Yahoo Finance Adj Close |

### Full 60-Month Correlation Matrix
```text
          SGOV      RXI      PEJ
SGOV      1.00     0.26     0.17
RXI       0.26     1.00     0.79
PEJ       0.17     0.79     1.00
```

### Full 60-Month Covariance Matrix ($\times 10^{-4}$)
```text
          SGOV       RXI       PEJ
SGOV      0.23      2.38      1.73
RXI       2.38    363.66    319.68
PEJ       1.73    319.68    450.29
```

---

## 3. Point-in-Time Signal & Formal Data Card

To eliminate lookahead contamination and survivorship errors, our macro signals are gated via FRED and ALFRED:

| Attribute | Specification | Operational Audit Result |
|---|---|---|
| **Data Provider** | Federal Reserve Bank of St. Louis | Keyless direct CSV API |
| **Macro Series** | `DGS10` (10-Year Treasury Yield) & `FEDFUNDS` (Effective Policy Rate) | Daily and monthly frequencies |
| **Publication Timestamp Rule** | Strict as-of filter | Records published after `2026-09-30` are blocked |
| **Historical Revision Protocol** | Fixed transaction yields | No historical revisions occur on market yields |
| **Signal Transformation** | Yield Curve Slope | $\text{Term Spread} = \text{DGS10} - \text{FEDFUNDS} = 3.85\% - 4.35\% = -0.50\%$ |
| **Governance Regime** | Inverted Yield Curve Hedge | Enforces minimum reserve floor of 50.0% SGOV |

---

## 4. Baseline Portfolios vs. Constrained Mix Mandate Checks

Each portfolio was audited against the complete set of Meridian Foundation rules:

| Rule Description | IPS Requirement | Equal-Weight Baseline | Inverse-Volatility Baseline | Constrained Mix (All Months) | Constrained Mix (Last 36M) |
|---|:---:|:---:|:---:|:---:|:---:|
| **Weights Sum to 100%** | $\sum w_i = 100\%$ | 100.0% (PASS) | 100.0% (PASS) | 100.0% (PASS) | 100.0% (PASS) |
| **Long-Only** | $w_i \ge 0$ | 33.3% (PASS) | 2.2% (PASS) | 0.0% (PASS) | 0.0% (PASS) |
| **Reserve Floor** | $\ge 3.0\%$ | 33.3% (PASS) | 95.4% (PASS) | 55.0% (PASS) | 95.0% (PASS) |
| **Expected Return** | $\ge 5.03\%$ | **4.72% (FAIL)** | **3.84% (FAIL)** | **5.16% (PASS)** | **5.12% (PASS)** |
| **Annualized Volatility** | Minimize | 11.45% | 0.49% | 9.60% | 0.92% |
| **Sharpe Ratio ($R_f=3.78\%$)** | Maximize | 0.08 | 0.12 | 0.14 | 1.46 |
| **5-Day Liquidity** | $\ge 90.0\%$ | 100.0% (PASS) | 100.0% (PASS) | 100.0% (PASS) | 100.0% (PASS) |
| **Single Issuer Limit** | $\le 8.0\%$ | Exempt (PASS) | Exempt (PASS) | Exempt (PASS) | Exempt (PASS) |
| **95% 1-Year Downside VaR** | $\le 10.0\%$ | -14.1% (WARNING) | +3.0% (PASS) | -10.6% (PASS) | +3.6% (PASS) |
| **OVERALL MANDATE VERDICT** | **Pass All Rules** | ❌ **FAILS MANDATE** | ❌ **FAILS MANDATE** | ✅ **PASSES MANDATE** | ⚠️ **PASSES (Instability)** |

---

## 5. Locked Changed-Input Record

In accordance with Lab 11 and Lab 20 standards, the following load-bearing input was predicted with AI turned off and committed to the repository before the run:

| Field | Pre-Run Locked Prediction (AI Off) | Post-Run Actual Result | Governance Interpretation & Root Cause |
|---|---|---|---|
| **Changed Input** | Target return hurdle lowered from **5.03% to 4.69%** (-34 bps). | Target return set to **4.69%**. | Parameter change executed exactly as designed. |
| **Allocation Shift** | SGOV will increase by 10–20 percentage points (55% $\rightarrow$ 65–75%); PEJ will decrease by 10–20 points. | SGOV increased by **15.0 percentage points** (55% $\rightarrow$ 70%); PEJ dropped by 15.0 pts (45% $\rightarrow$ 30%). | **CONFIRMED:** Optimizer aggressively substitutes equity risk with Treasuries as the hurdle is relaxed. |
| **Portfolio Volatility** | Volatility will drop significantly (below 7.00%) due to increased Treasury cash weight. | Volatility dropped from **9.60% down to 6.43%** (-3.17 percentage points). | **CONFIRMED:** Confirms boundary-seeking behavior of the quadratic solver. |
| **Mandate Verdict & Stance** | Mandate will still pass all rules; recommendation remains PILOT (decision unaffected). | All checkable mandate rules **PASS**; recommendation affirmed as **PILOT**. | **DECISION UNCHANGED:** Reaffirms that the allocation is hypersensitive to the return target, justifying a pilot. |

---

## 6. The Exact Institutional Stop Condition

The portfolio management process **MUST IMMEDIATELY HALT AND REJECT FULL ADOPTION** if:
1. **Infeasibility:** No long-only asset combination clears the net return hurdle while respecting the 3.0% reserve minimum.
2. **Estimation Instability:** A $\pm 100$ bps shift in any sleeve return estimate, or shifting between a 60-month and 36-month window, alters the largest sleeve weight by **$> 25.0$ percentage points**.
3. **Liquidity Drain:** Cash distributions or ETF market drawdown reduce `SGOV` reserves below **$3.0 Million (3.0%)**.
