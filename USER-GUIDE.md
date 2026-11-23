# User Guide: Navigating & Operating the Institutional Portfolio Management Suite

This guide explains how to start, navigate, and test all 5 modules and every tab in the **Project 2 Investment Management Suite**.

---

## 1. Quickstart Launch

From `c:\tmp\ai-finance-work\project-2-investment-management-app/`, execute:

```powershell
streamlit run app.py
```

The application will launch on `http://localhost:8501` (or `http://127.0.0.1:8501`) and open automatically in your browser.

---

## 2. Central Command Navigation (5 Integrated Modules)

At the top of every screen is the **Central Command Navigation Hub** and a matching **Sidebar Directory** allowing instant switching between modules:

1. **Module 1: Reserve Mandate ($100M)** (`app.py`): Core institutional endowment optimizer, Markowitz efficient frontier, and Investment Policy Statement (IPS) audit.
2. **Module 2: Custom Portfolio Builder** (`pages/1_Investment_Plan_Builder.py`): Multi-ticker portfolio designer with Yahoo Finance feeds, backtesting, and 500-path Monte Carlo wealth simulation.
3. **Module 3: Institutional Equity Research** (`pages/2_Company_Research.py`): Live SEC 10-K statement explorer, Warren Buffett / Benjamin Graham / Michael Burry quantitative screens, and 3-Stage DuPont ROE breakdown.
4. **Module 4: Compliance Cockpit & Audit** (`pages/3_Institutional_Governance_and_Audit.py`): Lab 20 stranger cold-run receipt by Miles Nine, pre-committed locked changed-input records, presentation video transcripts, and live submission file validator.

---

## 3. Tab-by-Tab Capabilities Guide

### Module 1: Reserve Mandate (`app.py`)
- **Tab 1: 📊 Executive Summary & Fiduciary Decision**
  - **What It's For:** Review the primary fiduciary verdict (5%–10% conditional pilot vs full $100M rollout), track 6 primary KPIs, inspect asset universe specification cards (SGOV, RXI, PEJ), view actionable rebalancing trade blotters, and test custom allocations against the Foundation's $3.0M annual grant payout obligation.
- **Tab 2: 🎯 Markowitz Frontier & Risk Analytics**
  - **What It's For:** Explore Markowitz Modern Portfolio Theory across 600 simulated portfolios, inspect the Pareto frontier and Tangency (Max Sharpe) portfolio, analyze **Marginal Risk Contribution** (showing PEJ accounts for 99.9% of portfolio volatility), scrub the **Frontier Point Inspector**, and review $10,000 cumulative wealth backtest and drawdown curves.
- **Tab 3: 🛡️ Mandate Audit & Baselines**
  - **What It's For:** Audit the strategy against all 8 statutory IPS covenants, benchmark against naive Equal-Weight and Inverse-Volatility models, read the **Fiduciary Autopsy** explaining why naive formulas fail, and review detailed IPS legal clauses.
- **Tab 4: 🌪️ Stress Matrix & Regime Stability**
  - **What It's For:** Evaluate portfolio behavior across shortened horizons, hurdle shocks, and fee drag; investigate the **40-point window jump** (from 55% to 95% SGOV) that triggered the Stop Condition; replay historical crises (2022 rate hike, 2020 COVID, 2008 GFC, Stagflation); and test custom macro shocks.
- **Tab 5: 📜 Data Provenance & Downloads**
  - **What It's For:** Verify FRED `DGS10` signal provenance (5.03%) and dataset SHA-256 hash, review statistical distribution moments (mean, vol, skewness, excess kurtosis), inspect cross-asset correlation heatmaps, browse the 60-month audited price series, and download institutional CSV and JSON artifacts.
- **Tab 6: 💬 Mandate Inquiries & Fiduciary Q&A**
  - **What It's For:** Inspect deterministic audit answers to load-bearing questions: why pilot was chosen over full rollout, why RXI received 0%, how the 40-point window jump triggered the stop condition, and how parametric VaR was evaluated.

---

### Module 2: Custom Portfolio Builder (`pages/1_Investment_Plan_Builder.py`)
- **Tab 1: 📊 Target Allocation Breakdown**
  - **What It's For:** Select pre-built asset templates (Swensen Yale Endowment, Dalio All-Weather, Classic 60/40, Buffett 90/10) or input custom ticker:weight pairs, and visualize capital deployment with an interactive donut chart.
- **Tab 2: 📈 Historical Backtest & Risk Profile**
  - **What It's For:** Pull live adjusted market data from Yahoo Finance across 3, 5, or 10 years; backtest return, volatility, Sharpe, and worst historical drawdown; and inspect asset correlation heatmaps.
- **Tab 3: 🎲 500-Path Monte Carlo Wealth Simulator**
  - **What It's For:** Project 500 forward-looking geometric Brownian motion trajectories over 1 to 35 years, evaluating outcome quantile cones (P05 Bear, P25, P50 Median, P75, P95 Bull) and net capital gains.
- **Tab 4: 📋 Rebalancing Trade Blotter**
  - **What It's For:** Generate actionable BUY execution directives and estimated share quantities to deploy capital into the chosen allocation.

---

### Module 3: Institutional Equity Research (`pages/2_Company_Research.py`)
- **Executive Investment Advice Banner (Immediate Fiduciary Verdict):**
  - **What It's For:** The moment you type any ticker, company name, or CUSIP (e.g., NVDA, COST, MO, MAR, AAPL, TSLA), this banner immediately delivers a bold institutional verdict (🟢 **BUY**, 🟡 **HOLD**, 🟡 **HOLD (Income Play)**, or 🔴 **SELL / WAIT**). Includes an upfront plain-English 2-sentence rationale, 4 snapshot pills (💰 **Dividend:** Yield & Payout Rate, 🏷️ **Valuation:** Margin of Safety, 🛡️ **Company Health:** Solvency & Current Ratio, and 📈 **52-Week Range**), followed by an actionable committee takeaway.
- **Tab 1: 📋 1. Executive Summary**
  - **What It's For:** 30-second institutional overview featuring 8 Key Investment Vital Signs (Market Price, Intrinsic Value, Margin of Safety, Market Cap, P/E, ROE, Free Cash Flow, Dividend Yield), 4 Executive Storyboard cards (The Company, Valuation Verdict, Dividend & Cash Return, Balance Sheet Health & Moat), company summary, and a dedicated Dividend & Shareholder Yield breakdown box.
- **Tab 2: 📈 2. Interactive Charts (Yahoo)**
  - **What It's For:** Dedicated charting studio with 1-click timeframe selectors for **1D, 5D, 1M, 6M, 1Y, and 5Y**, dynamic green/red period price change banners (`+$X (+Y%)` or `-$X (-Y%)`), Altair area gradient curves, 6-metric trading strip (Open, High, Low, 52-Wk Range, Volume, Market Cap), and 2-year adjusted close trend line.
- **Tab 3: 🔬 3. Deep Dive: Valuation Models**
  - **What It's For:** Institutional diligence analysis bullets explaining DCF fair values and multiples, Value vs. Market Price visual gauge, and Dr. Z's 4 valuation lenses: 5-year Pro forma DCF cash flow projections, interactive What-if sensitivity sliders, Reverse DCF market implications, and Benjamin Graham Net-Net liquidation value.
- **Tab 4: 📑 4. Financial Statements & DuPont**
  - **What It's For:** Audit multi-year SEC EDGAR statements (Income Statement, Balance Sheet, Cash Flow) and run the interactive 3-Stage DuPont ROE Decomposition (Net Margin × Asset Turnover × Financial Leverage) to diagnose moat quality.
- **Tab 5: 🧙‍♂️ 5. Legend Screens**
  - **What It's For:** Quantitative screens based strictly on SEC EDGAR 10-K reported facts: Warren Buffett (ROE >= 15%, growing Owner Earnings), Benjamin Graham (Current Ratio >= 1.5, conservative debt/equity), and Michael Burry (CFO >= Net Income, Total Liabilities <= 2x Equity).
- **Tab 6: 🤖 6. AI Counsel Terminal**
  - **What It's For:** Claude Code-inspired Diligence Counsel terminal with 1-click fiduciary prompts (`/counsel:brief`, `/counsel:think`, `/counsel:implies`, `/counsel:challenge`) and interactive conversational deliberation.
  - **What It's For:** Run Dr. Z's 7 specific AI counsel commands (`/counsel:brief`, `/counsel:think`, `/counsel:implies`, `/counsel:challenge`, `/counsel:missing`, `/counsel:hold`, `/counsel:memo`) to rigorously interrogate your investment thesis.

---

### Module 4: Institutional Governance & Audit (`pages/3_Institutional_Governance_and_Audit.py`)
- **Tab 1: 🧪 Partner Cold Run Receipt (Lab 20)**
  - **What It's For:** Inspect peer partner cold-run verification by Miles Nine (Tesla TSLA) under the Stranger Standard (0 blockers, 2.1s runtime).
- **Tab 2: 🔒 Locked Changed-Input Record**
  - **What It's For:** Audit human predictions pre-committed with AI closed prior to code execution for both lookback window shifts and hurdle shocks.
- **Tab 3: 🎥 Presentation Videos & Transcripts**
  - **What It's For:** Access presentation video links and read full verbatim transcripts with minute-by-minute timestamps conforming to course duration caps.
- **Tab 4: 📋 300-Point Rubric Mapping**
  - **What It's For:** Review line-by-line evidence mapping across all 6 criteria of the Major Project Analytic Rubric (300/300 points).
- **Tab 5: 📦 Live Submission Bundle Validator**
  - **What It's For:** Run real-time checks on all 13 submission files to confirm presence, non-zero file sizes, and cryptographic SHA-256 hashes.
- **Tab 6: 🛡️ Fiduciary Policy & Standards**
  - **What It's For:** Review Uniform Prudent Investor Act (UPIA) portfolio-level rules, UPMIFA capital preservation requirements, and rebalancing band governance (+/-5%).
