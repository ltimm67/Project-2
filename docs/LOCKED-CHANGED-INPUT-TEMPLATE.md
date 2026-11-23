# Locked Changed-Input Record — Student Record

> Completed with AI closed, committed to repository history **before** the execution run.

## Before execution — student authored (AI Closed)

- Date/time: November 17, 2026, 13:45 EST
- Commit hash before run: `c8f1e09a3d4e`
- Changed input and units: Net Annual Return Hurdle Rate (% annual)
- Old value: 5.03% (FRED DGS10 10-Yr Treasury Yield)
- New value: 4.69% (-34 bps yield spread compression shock)
- Expected direction and approximate size of allocation/metric change: I think lowering net return hurdle by 34 bps will relax the required equity risk budget. This is because the optimizer seeks minimum variance on a 5% grid, it will substitute volatile PEJ equity with low-volatility SGOV Treasuries. I predict SGOV weight will expand by +10 ish percentage points (from 55% to 65%), PEJ will drop to 25%–35%, RXI will remain 0.0%, and portfolio volatility will fall below 7.00%.
- Expected effect on the committee decision: I think the committee recommendation will remain PILOT because the allocation remains hypersensitive to inputs.
- Finance reasoning for the prediction: Lower return requirements reduce the required equity beta needed to satisfy the mandate, enabling the minimum-variance quadratic solver to allocate more capital to risk-free cash.

## After execution

- Commands or app controls used: Slider adjustment in `app.py` or 1-click preset "⚡ Changed (4.69%)"; verified via `python verify_project2.py`
- Actual allocation and metrics before/after: 
  - Before (5.03%): SGOV 55.0% | RXI 0.0% | PEJ 45.0% | Exp Ret: 5.16% (Net: 5.01%) | Vol: 9.60%
  - After (4.69%): SGOV 70.0% | RXI 0.0% | PEJ 30.0% | Exp Ret: 4.70% (Net: 4.55%) | Vol: 6.43%
  - Net Change: SGOV +15.0 pts | PEJ -15.0 pts | Volatility -3.17 pts
- Actual decision effect: PASSES MANDATE. Recommendation confirmed as CONDITIONAL PILOT.
- Did the result match the prediction? Why or why not? Yes. SGOV expanded by +15.0 percentage points, aligning with the predicted +10 ish point expansion into cash, and volatility fell below 7.00% to 6.43%.
- Failure diagnosis or limitation revealed: Confirms the quadratic optimizer acts as a boundary-seeking cornering solver, validating our rejection of full capital adoption.
- Commit hash containing the observed output: `c8f1e09`
