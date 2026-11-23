# Project 2 Master Deliverables Manifest

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Lead Analyst:** Lucas Timm (ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Mandate:** Meridian Foundation Reserve ($100 Million Portfolio)  

---

## 1. Mandatory Statements on AI Use and Academic Authorship
> **Mandatory AI Disclosure:** I used **Google Antigravity (Gemini Pro)** to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## 2. Primary Deliverables Directory

| Deliverable | Location in Repository | Status | Verification Summary |
|---|---|:---:|---|
| **App Source Code** | [`app.py`](../app.py) | **Complete** | Full interactive Streamlit app with mandate validator, baselines, stress engine, and FRED signal. |
| **App README** | [`README.md`](../README.md) | **Complete** | Contains mandatory statements, single-command run instructions, visible decision numbers, and stop condition. |
| **Historical Price Data** | [`prices.csv`](../prices.csv) | **Complete** | 60 monthly observations (2021-10 to 2026-09) for SGOV, RXI, and PEJ. |
| **Dependencies** | [`requirements.txt`](../requirements.txt) | **Complete** | Clean, minimal dependencies (`streamlit`, `pandas`). |
| **Decision Memo** | [`docs/decision-memo.md`](./decision-memo.md) | **Complete** | 8-section institutional memo defending the PILOT stance, 5-10% allocation range, and monitoring triggers. |
| **Validation & AI Use** | [`docs/validation-and-ai-use.md`](./validation-and-ai-use.md) | **Complete** | Validation audit log, FRED data card, baseline verdicts, and Locked Changed-Input Record. |

---

## 3. Video Submissions & Transcripts

All three required student presentations are recorded with closed captions / transcripts enabled:

### Video 1: Research Evolution & System Design
- **Duration:** 3:22 (Requirement: ~3:00)
- **YouTube Link:** `https://youtu.be/3y5cM4I0CYg` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-1-transcript.md`](./video-1-transcript.md) & [`docs/transcript-video-1.txt`](./transcript-video-1.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:25`: Mandatory Opening Statements (AI usage disclosure & educational disclaimer).
  - `0:25 - 1:15`: Research Evolution (Transition from static optimization to Markowitz "error maximization").
  - `1:15 - 1:55`: Estimation Risk Demonstration (40-point allocation jump from 55% to 95% SGOV).
  - `1:55 - 2:40`: Checked AI Output (Auditing & correcting continuous SciPy optimizer to 5% discrete grid; correcting correlation).
  - `2:40 - 3:22`: Authorship attribution & transition to codebase walkthrough.

### Video 2: Code Walkthrough & Optimization Engine
- **Duration:** 4:48 (Requirement: $\le 5:00$)
- **YouTube Link:** `https://youtu.be/mJVCupZrEZU` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-2-transcript.md`](./video-2-transcript.md) & [`docs/transcript-video-2.txt`](./transcript-video-2.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:20`: Mandatory Opening Statements & repository architecture.
  - `0:20 - 1:15`: Mathematical Foundation (`load_prices`, monthly returns, annualized returns, Bessel volatility, covariance).
  - `1:15 - 2:20`: Optimization Engine (`optimize` 5% grid search logic, return hurdle, reserve floor, and normal VaR loss metric).
  - `2:20 - 3:15`: Institutional Mandate Rule Compliance Engine (`mandate_audit`, testing all 8 IPS rules).
  - `3:15 - 4:10`: Live execution in terminal with `verify_project2.py` showing baseline comparison and trade blotter.
  - `4:10 - 4:48`: Unit test suite verification: all 9 tests passing in 0.011s.

### Video 3: Investment Committee Defense & Final Recommendation
- **Duration:** 5:06 (Requirement: $\approx 5:00$)
- **YouTube Link:** `https://youtu.be/_aaUnLdPBl0` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-3-transcript.md`](./video-3-transcript.md) & [`docs/transcript-video-3.txt`](./transcript-video-3.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:30`: Live Running Streamlit App Opening & Committee Introduction.
  - `0:30 - 1:20`: Mandate review & Executive Storyboard defending the 5% to 10% pilot recommendation.
  - `1:20 - 2:15`: Live demonstration of 40-point window jump (toggling 36-Month stress test on screen).
  - `2:15 - 3:00`: Tab 3 Mandate Audit & baseline comparison (proving why Equal Weight & Inverse Volatility FAIL).
  - `3:00 - 3:55`: Live Locked Changed-Input Test (moving return hurdle to 4.69%, showing +15 pt SGOV shift).
  - `3:55 - 4:35`: Three enforceable operational monitoring triggers & Stop Condition.
  - `4:35 - 5:06`: Walkthrough of broader capabilities (Module 2 Custom Builder, Module 3 Equity Diligence, Module 4 Audit Cockpit).

---

## 4. Student Checklist Compliance

- [x] App runs cleanly from a single terminal command (`streamlit run app.py`).
- [x] Includes complete Lab 13 mandate: objective, universe, benchmark, risk measures, and limits.
- [x] Two transparent baselines (Equal Weight & Inverse Volatility) displayed beside the constrained portfolio with explicit mandate verdicts.
- [x] One point-in-time macro rate signal (`DGS10` vs `FEDFUNDS`) with a comprehensive institutional Data Card.
- [x] Multi-scenario stress testing on estimates, estimation window, costs, and constraints.
- [x] Explicit mathematical Stop Condition that halts adoption.
- [x] Locked Changed-Input Record with AI-off pre-run prediction committed before execution.
- [x] Final recommendation with bounded allocation range (5%–10% pilot tranche) and three operational triggers.
- [x] Two mandatory statements open the README, Decision Memo, Validation log, and all three video transcripts.
