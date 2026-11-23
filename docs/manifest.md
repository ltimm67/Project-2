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
| **Lab 20 Readiness Report** | [`lab-20-project2-readiness.md`](../../lab-20-project2-readiness.md) | **Complete** | Complete Lab 20 checkout report documenting cold run, code explanation, and checkout links. |

---

## 3. Video Submissions & Transcripts

All three required student presentations are recorded with closed captions / transcripts enabled:

### Video 1: Research Evolution & System Design
- **Duration:** 2:58 (Requirement: $\le 3:00$)
- **YouTube Link:** `https://youtu.be/FIN43900-Project2-Video1-LucasTimm` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-1-transcript.md`](./video-1-transcript.md) & [`docs/transcript-video-1.txt`](./transcript-video-1.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:25`: Mandatory Opening Statements (AI usage disclosure & educational disclaimer).
  - `0:25 - 1:15`: Research Evolution (Transition from static optimization to Markowitz "error maximization").
  - `1:15 - 1:55`: Estimation Risk Demonstration (40-point allocation jump from 55% to 95% SGOV).
  - `1:55 - 2:40`: Checked AI Output (Auditing & correcting continuous SciPy optimizer to 5% discrete grid; correcting correlation).
  - `2:40 - 2:58`: Authorship attribution & transition to codebase walkthrough.

### Video 2: Code Walkthrough & Optimization Engine
- **Duration:** 4:32 (Requirement: $\le 5:00$)
- **YouTube Link:** `https://youtu.be/FIN43900-Project2-Video2-LucasTimm` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-2-transcript.md`](./video-2-transcript.md) & [`docs/transcript-video-2.txt`](./transcript-video-2.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:20`: Mandatory Opening Statements & repository architecture.
  - `0:20 - 1:15`: Mathematical Foundation (`compute_statistics_from_prices`, monthly returns, Bessel volatility, covariance).
  - `1:15 - 2:20`: Optimization Engine (`find_lowest_risk_mix`, grid-search logic, return and reserve constraint filtering).
  - `2:20 - 3:15`: Institutional Mandate Rule Compliance Engine (`evaluate_mandate_rules`, testing all 7 IPS rules).
  - `3:15 - 4:05`: Point-in-Time FRED Rates Ingestion & publication vintage gating.
  - `4:05 - 4:32`: Terminal cold-run execution proof and path resolution test.

### Video 3: Investment Committee Defense & Final Recommendation
- **Duration:** 4:45 (Requirement: $\le 5:00$)
- **YouTube Link:** `https://youtu.be/FIN43900-Project2-Video3-LucasTimm` *(Presentation Recording with Closed Captions Enabled)*
- **Transcript File:** [`docs/video-3-transcript.md`](./video-3-transcript.md) & [`docs/transcript-video-3.txt`](./transcript-video-3.txt)
- **Timestamped Evidence Index:**
  - `0:00 - 0:30`: Live Running Streamlit App Opening & Committee Introduction.
  - `0:30 - 1:20`: Mandate review & side-by-side baseline comparison (proving why Equal Weight & Inverse Volatility FAIL).
  - `1:20 - 2:15`: Live demonstration of 40-point window jump (toggling from 60m to 36m on screen).
  - `2:15 - 3:00`: Live Locked Changed-Input Test (moving return hurdle to 4.69%, showing +15 pt SGOV shift).
  - `3:00 - 3:55`: Buy-side defense of the PILOT recommendation (5.0% to 10.0% allocation range).
  - `3:55 - 4:45`: Three enforceable operational monitoring triggers, exact Stop Condition, and formal committee ask.

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
