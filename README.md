# Project 2 — Institutional Investment Management Application

> **Mandatory AI & Responsibility Statements:**  
> 1. **AI Assistance Disclosure:** This application, statistical engine, and governance verification architecture were built with assistance from **Google Antigravity (Gemini Pro)** for mathematical optimization routines, unit testing, and interface layout.  
> 2. **Analyst Responsibility & Academic Scope:** All financial model choices, mandate parameter bounds, stress test analyses, and final portfolio recommendations were authored, reviewed, and finalized by **Lucas Timm**. This system is designed solely for educational decision support and academic evaluation, not individualized investment advice.  
> 3. **Human-in-the-Loop Quality Control Audit:** For a full audit trail chronicling every instance of human design intervention, bug catching, and fiduciary steering over the AI, see [AI-DECISION-LOG.md](AI-DECISION-LOG.md).

---

## Executive Summary & Visible Decision Output

*This table is pre-rendered and committed directly to GitHub to satisfy the Stranger Standard and ensure immediate accessibility without running code (insulating against the rubric's 50% score cap).*

| Portfolio Strategy | SGOV % | RXI % | PEJ % | Gross Return | Net Return | Volatility | Sharpe | Reserve Floor | Turnover | Mandate Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **1. Baseline: Equal Weight (1/N)** | 33.3% | 33.3% | 33.3% | 4.72% | 4.57% | 12.76% | 0.07 | 33.3% | 40.0% | **FAILS MANDATE** (Return < 5.03%) |
| **2. Baseline: Inverse Volatility** | 95.4% | 2.4% | 2.2% | 3.84% | 3.69% | 1.07% | 0.06 | 95.4% | 55.4% | **FAILS MANDATE** (Return < 5.03%) |
| **3. Constrained Optimal (Base 60m)** | **55.0%** | **0.0%** | **45.0%** | **5.16%** | **5.01%** | **9.60%** | **0.14** | **55.0%** | **30.0%** | **PASSES PRIMARY MANDATE** |
| **4. Stress Window (Last 36-Mo)** | 95.0% | 0.0% | 5.0% | 5.12% | 4.97% | 0.92% | 1.46 | 95.0% | 55.0% | **PASSES MANDATE** (Triggers Stop) |
| **5. Changed-Input Run (4.69% Hurdle)** | 70.0% | 0.0% | 30.0% | 4.70% | 4.55% | 6.43% | 0.14 | 70.0% | 30.0% | **PASSES MANDATE** |

### The Institutional Recommendation
> **RECOMMENDATION: CONDITIONAL PILOT (5% to 10% Allocation Range, \$5M to \$10M). DO NOT ADOPT FOR FULL \$100M ROLLOUT.**  
> While the constrained optimal mix clears all core mandate hurdles, re-estimating parameters over a 36-month horizon induces a **40-point allocation shift** into cash (from 55% to 95% SGOV), breaching the institutional 25% stability limit. Full capital rollout is withheld until a live pilot with volatility dampening proves parameter stability.

---

## One-Command Quickstart

To run the application locally on any machine:

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the Streamlit Web Application
streamlit run app.py
```

To run the automated verification engine and regenerate all visible outputs in <0.3s:

```powershell
python verify_project2.py
```

To run unit tests:

```powershell
python -m unittest discover -s tests -v
```

---

## Application Architecture & Multi-Page Capabilities

* **`app.py` (Main Dashboard — Institutional Mandate Engine):**
  * Real-time optimization across all valid portfolio weights.
  * Interactive **Altair Markowitz Efficient Frontier** & 600-portfolio opportunity cloud.
  * Asset allocation sleeve comparison and historical cumulative wealth curves ($10,000 growth).
  * Dual-mode data engine: Audited canonical dataset (`prices.csv`) with instant toggle to **Live Yahoo Finance** (`yfinance`).
  * Real-time mandate audit scorecard and sensitivity matrix.
* **`pages/1_Investment_Plan_Builder.py` (Universal Portfolio Builder):**
  * Allows any user to input ANY custom tickers (e.g. `SPY, BND, GLD` or `AAPL, MSFT, GOOGL`).
  * Pulls live historical prices from Yahoo Finance with auto-adjusted dividends and splits.
  * Interactive correlation matrix heatmap and 500-path Monte Carlo wealth projection simulator.
* **`pages/2_Company_Research.py` (Fundamental Equity & Legend Screener):**
  * Live SEC 10-K financial statement explorer (Income Statement, Balance Sheet, Cash Flow).
  * **Legend Investor Screener:** Integrates quantitative tests from Warren Buffett (Lab 18), Benjamin Graham (Lab 19), and Michael Burry (Lab 19).
  * Scenario valuation calculator (EV/EBITDA multiple sensitivity).
* **`pages/3_Institutional_Governance_and_Audit.py` (Compliance Cockpit):**
  * Complete Lab 20 stranger cold-run receipt (Miles Nine).
  * Locked changed-input records and pre-committed human predictions.
  * Presentation video links with full, verbatim transcripts.
  * Line-by-line mapping against the 300-point Major Project Analytic Rubric.

---

## Video Presentations & Verified Transcripts

All three required student presentations are recorded with closed captions enabled:

| Video | Title & Focus | Duration | YouTube Link | Transcript |
|---|---|:---:|:---:|:---:|
| **Video 1** | Research Evolution & Checked AI Output | 3:22 | [Watch Video 1](https://youtu.be/3y5cM4I0CYg) | [`docs/transcript-video-1.txt`](docs/transcript-video-1.txt) |
| **Video 2** | Code Walkthrough & Optimization Engine | 4:48 | [Watch Video 2](https://youtu.be/mJVCupZrEZU) | [`docs/transcript-video-2.txt`](docs/transcript-video-2.txt) |
| **Video 3** | Committee Defense (Live App Walkthrough) | 5:06 | [Watch Video 3](https://youtu.be/_aaUnLdPBl0) | [`docs/transcript-video-3.txt`](docs/transcript-video-3.txt) |

---

## Repository Map

```
project-2-investment-management-app/
├── app.py                              # Main Streamlit application (Module 1: Mandate Engine)
├── portfolio_engine.py                 # Core deterministic portfolio mathematics
├── prices.csv                          # Audited 60-month canonical price dataset
├── verify_project2.py                  # Automated verification runner (<0.3s runtime)
├── visible_output.json                 # Pre-rendered executed output JSON
├── requirements.txt                    # Project dependencies (streamlit, pandas, numpy, altair, yfinance)
├── AI-DECISION-LOG.md                  # Complete audit trail of human interventions & AI QC
├── pages/
│   ├── 1_Investment_Plan_Builder.py    # Module 2: Custom ticker portfolio builder & Monte Carlo
│   ├── 2_Company_Research.py           # Module 3: Equity fundamentals & Legend Investor screener
│   └── 3_Institutional_Governance_and_Audit.py # Module 4: Compliance audit & transcripts
├── tests/
│   └── test_portfolio_engine.py        # Automated calculation unit tests (9/9 pass)
└── docs/
    ├── decision-memo.md                # Institutional investment committee decision memo
    ├── validation-and-ai-use.md        # Data card, stress matrix & locked changed-input record
    ├── manifest.md                     # Timestamped grading navigation manifest
    └── visible_output.json             # Execution artifact copy
```

---

## Data Provenance & Point-in-Time Integrity

* **Point-in-Time Hurdle Signal:** FRED 10-Year Treasury Constant Maturity Rate (`DGS10`), **5.03% Annualized**, locked as-of September 30, 2026.
* **Canonical Price Dataset:** 60 monthly observations (2021-10-01 to 2026-09-01) for SGOV, RXI, and PEJ.
* **Cryptographic Provenance:** `prices.csv` SHA-256 Hash verified and logged in `visible_output.json`.
* **Zero Look-Ahead Bias:** All optimization estimates use strictly backward-looking monthly returns.
