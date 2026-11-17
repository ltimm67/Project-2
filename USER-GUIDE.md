# User Guide: Opening and Operating the Project 2 Application

This guide explains how to start, navigate, and test the **Project 2 Investment Management App**.

---

## 1. How to Launch the Application

In your terminal (from `c:\tmp\ai-finance-work\` or inside `project-2-investment-management-app/`), run:

```powershell
python -m streamlit run app.py
```
*Or, from the workspace root:*
```powershell
python -m streamlit run project-2-investment-management-app/app.py
```

The app will start on local port `8501` or `8502` and open directly in your web browser.

---

## 2. Using the Sidebar Controls

- **Historical Estimation Window:** Toggle between `All 60 Months` and `Last 36 Months`. Switching to 36 months causes the optimal Treasury weight (`SGOV`) to jump by **40 percentage points** (from 55% to 95%), proving estimation instability.
- **Objective Expected Annual Return (%):** Adjust the hurdle slider. The baseline is **5.03%**. In Lab 20, lowering this to **4.69%** shifts 15 points into SGOV (55% $\rightarrow$ 70%) and lowers volatility from 9.60% to 6.43%.
- **Minimum Reserve-Eligible Weight (%):** Controls the mandatory payout liquidity floor (default is **3.0%**, or \$3.0M).
- **Transaction Drag (bps):** Adjusts annual execution friction (default is **15 bps**).
- **As-Of Publication Vintage Gate:** Enforces point-in-time isolation on FRED macro interest rate series (`DGS10` vs `FEDFUNDS`).

---

## 3. Interpreting the Dashboard Output

- **Section 1 (Mandate):** Displays the Meridian Foundation \$100M reserve parameters and IPS rules.
- **Section 2 (Baselines vs Portfolio):** Evaluates Equal Weight, Inverse Volatility, and the Constrained Portfolio against all mandate rules. Shows why the baselines FAIL the return hurdle while the constrained mix PASSES.
- **Section 3 (Macro Signal & Data Card):** Illustrates the inverted yield curve signal (-50 bps) and formal data provenance.
- **Section 4 (Stress Testing & Stop Condition):** Tests return shocks and window sensitivity, stating the exact Stop Condition.
- **Section 5 (Locked Changed-Input Record):** Compares the pre-run AI-off prediction against post-run actuals.
- **Section 6 (Committee Recommendation):** Outlines why the committee recommends **PILOT (5% to 10% allocation range)** and establishes three operational monitoring triggers.

---

## 4. Stopping and Restarting

- **To Stop:** In your terminal, press `Ctrl + C`.
- **To Restart:** Run `streamlit run app.py` again.
