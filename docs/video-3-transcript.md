# Video 3 Transcript: Investment Committee Defense & Final Recommendation

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Exact Duration:** 4:38 (Course Requirement: <= 5:00)  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video3-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script with Timestamps

[00:00] "Welcome, members of the Investment Committee and Board of Trustees of the Meridian Foundation. My name is Lucas Timm, Lead Portfolio Analyst for your $100 Million Reserve Portfolio. 

[00:15] As required by our governance standards, I am opening today's defense with our interactive Streamlit application running live on screen at localhost port 8501.

[00:32] Let me state our definitive fiduciary recommendation upfront: We recommend that the committee authorize a **CONDITIONAL PILOT MANDATE with an allocation range of 5.0% to 10.0% of reserve capital ($5.0 Million to $10.0 Million pilot tranche)**. We advise retaining the remaining 90% to 95% in our strategic 60/40 benchmark (60% RXI / 40% SGOV) while tracking live out-of-sample stability. We formally advise against full adoption of the optimizer for the entire $100 million reserve today.

[01:05] Looking at the dashboard on screen, the Meridian mandate requires achieving CPI plus 4.0% net—translating to a 5.03% annual return hurdle from FRED series DGS10—while preserving a minimum 20.0% liquid cash reserve in SGOV for quarterly grant disbursements.

[01:30] In Section 4 of the app, we test two transparent baselines beside our constrained portfolio:
- The **Equal-Weight Baseline** (33.3% SGOV / 33.3% RXI / 33.3% PEJ) delivers an expected return of 4.72% with 12.76% volatility. It fails our mandate because 4.72% lags our 5.03% hurdle.
- The **Inverse-Volatility Baseline** (95.4% SGOV / 2.4% RXI / 2.2% PEJ) produces a low volatility of 1.07%, but return collapses to 3.84%, failing the hurdle by 119 basis points.
- Our **Constrained Optimal Portfolio** passes all primary mandate rules: it allocates **55.0% to SGOV, 0.0% to RXI, and 45.0% to PEJ**, generating a 5.16% gross return, 5.01% net return after 15 bps fee friction, 9.60% volatility, and 55.0% reserve liquidity.

[02:18] So why are we recommending a pilot rather than full adoption?
Watch my screen as I toggle the estimation window control on the sidebar:
When we switch from the full 60-month dataset to the post-inflation 36-month window, look at the allocation shift:
The allocation to SGOV jumps from **55% to 95%**, while PEJ drops from **45% down to 5%**. That is a **40.0 percentage point allocation swing**! Under our investment policy statement, any window shift greater than 25.0 percentage points triggers a formal Stop Condition.

[03:00] Next, look at our Locked Changed-Input Record: Before running the model, I predicted with AI turned off that lowering the net return hurdle by 34 basis points to 4.69% would relax the equity risk budget, expanding SGOV by roughly 10 percentage points from 55% to 65%, dropping PEJ to 25%–35%, and lowering volatility below 7.00%. As I move the slider to 4.69%, SGOV shifts by +15.0 percentage points to 70%, and volatility drops to 6.43%, confirming our directional prediction on the 5% grid.

[03:40] To govern our recommended 5% to 10% pilot tranche, we establish three strict operational monitoring triggers:
1. **Rebalancing Drift Trigger:** Rebalance within 3 business days if any sleeve drifts by more than +/- 5.0 percentage points from target weights.
2. **Tracking Error & Volatility Trigger:** Halt additional capital deployments if 12-month realized tracking error against the 60/40 benchmark exceeds 3.50% or pilot volatility spikes above 12.0%.
3. **Liquidity Covenant Floor:** If quarterly grant distributions pull total SGOV cash below $3.0 Million (3.0%), immediately rebalance risk assets to restore the liquid buffer.

[04:20] In summary, our process provides an auditable, transparent decision engine that protects foundation purchasing power while acknowledging real-world estimation risk. Thank you, and I look forward to your questions."
