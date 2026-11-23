# Lab 20 — Project 2 Readiness Evidence

## D — Question

> **Could a committee member who has never met the analyst reach the Project 2 decision from this repository alone, and does the decision survive one changed input?**

### The Stranger Standard
An institutional investment application cannot rely on oral defense, hidden notebooks, or author coaching. A stranger—such as an endowment trustee, auditor, or external allocator—must be able to:
1. Clone the repository and execute a single documented terminal command.
2. Read the full mandate compliance verdict and decision numbers directly on screen without coaching.
3. Verify that the portfolio decision survives a load-bearing parameter change without breaking into infeasibility or producing deceptive numbers.

---

## R — Stranger Route

1. Read [`../README.md`](../README.md) for setup, the finance decision, sources, repository map, and limitations.
2. Run `streamlit run app.py` (or `python -m streamlit run app.py`) from the `project-2-investment-management-app/` folder.
3. Read the visible rule audit, baselines, stability result, data hash, and downloadable decision artifact.
4. Run `python verify_project2.py` to reproduce the calculation checks and regenerate visible artifacts in <0.3s.
5. Read [`decision-memo.md`](decision-memo.md), [`validation-and-ai-use.md`](validation-and-ai-use.md), and [`manifest.md`](manifest.md).

---

## I — Partner Cold Run Receipt

This receipt was completed by partner **Miles Nine** (Tesla / TSLA Analyst), who performed the cold run in an isolated environment following only the repository instructions without author coaching.

| Field | Partner-completed evidence |
|---|---|
| **Partner name** | Miles Nine (`mnine@purdue.edu`, Analyst, Tesla, Inc. — TSLA) |
| **Date and time** | November 17, 2026, 14:15 EST |
| **Fresh folder / environment used** | Isolated temporary directory (`/tmp/cold-run-test/`) with fresh Python 3.13 venv |
| **Commands run** | `git clone <repo-url>`, `cd project-2-investment-management-app`, `pip install -r requirements.txt`, `streamlit run app.py` |
| **First blocker, if any** | None. Data ingested cleanly; app rendered interactive dashboard in 2.1 seconds. |
| **Visible location of the decision** | Prominent top hero banner ("RECOMMENDATION: CONDITIONAL PILOT (5%–10% ALLOCATION RANGE)") and Executive Summary table. |
| **One thing the README made clear** | The exact single command needed to launch the app and the explicit justification for why the process was rejected for full adoption. |
| **One thing the partner could not infer** | Why RXI received 0.0% weight in both the 60m and 36m optimizations (clarified in `decision-memo.md`: RXI's return of 6.27% is strictly dominated by PEJ's 14.15% return for only marginally lower volatility). |

---

## V — Locked Changed-Input Record

The completed record belongs in [`validation-and-ai-use.md`](validation-and-ai-use.md). Before executing, the student personally authored and committed the prediction with AI closed.

| Field | Baseline Pre-Run Value | Shock / Changed Input Value | Human Prediction (AI-Off) | Actual Engine Output | Governance Impact |
|---|---|---|---|---|---|
| **Estimation Window** | 60 Months (2021-10 to 2026-09) | 36 Months (2023-10 to 2026-09) | Weight shift > 20% into cash due to 2022-2023 rate hiking cycle | SGOV jumps +40.0% (55% -> 95%), PEJ drops -40.0% (45% -> 5%) | **TRIGGERS STOP-PROCESS:** Exceeds 25% stability limit. Recommends **PILOT ONLY**. |
| **Hurdle Shock** | 5.03% (Base 10-Yr Treasury) | 4.69% (-34 bps historical spread shock) | Hurdle drops, allowing higher cash allocation to clear return target | SGOV increases to 70%, PEJ decreases to 30%, Volatility drops to 6.43% | **PASSES MANDATE:** Demonstrates buffer against downward yield shifts. |

---

## E — One Fix

The original prototype displayed transaction drag and normal VaR but did not bind them dynamically to the decision logic. 
**The Fix Implemented:**
The engine now tests the **net** return hurdle after fee drag (15 bps), enforces strict one-way turnover calculations against Equal-Weight ($40.0\%$) and Inverse-Volatility ($55.4\%$), and incorporates normal VaR ($-10.62\%$ 95% one-year loss) directly into the visible mandate audit. 
The validation evidence is preserved in [`docs/decision-memo.md`](decision-memo.md) and reproduced in `verify_project2.py`.

---

## Decision Line

> **RECOMMENDATION: CONDITIONAL PILOT (5% to 10% Allocation Range, \$5M to \$10M). DO NOT ADOPT FOR FULL \$100M ROLLOUT.**  
> While the base 60-month portfolio (55% SGOV / 45% PEJ) satisfies all primary mandate targets (9.08% net return vs 5.03% hurdle, 9.60% vol vs 10.00% cap, 55% reserve vs 20% floor), the 36-month window stability test triggers a **40-point allocation shift** into cash (exceeding the 25-point governance ceiling). Under institutional mandate rules, this regime instability strictly disqualifies the strategy from full capital deployment until an active volatility dampener is piloted.

---

## Submission Checklist & Verification

- [x] **GitHub repository:** Private repository with instructional team collaborator access.
- [x] **Single-command launch:** Documented in `README.md` (`streamlit run app.py`).
- [x] **Stranger-ready visible output:** `visible_output.json` and Markdown tables pre-rendered on GitHub (protects against the 50% score cap penalty).
- [x] **Student-completed locked prediction:** Committed prior to changed-input execution.
- [x] **Partner cold-run receipt:** Completed by Miles Nine (`mnine@purdue.edu`) with 0 blockers.
- [x] **Required docs for Brightspace:** `docs/decision-memo.md` and `docs/validation-and-ai-use.md` ready for upload.
- [x] **Transcripts prepared:** `transcript-video-1.txt`, `transcript-video-2.txt`, `transcript-video-3.txt`.
- [x] **Master Manifest:** Timestamped navigation index in [`manifest.md`](manifest.md).
