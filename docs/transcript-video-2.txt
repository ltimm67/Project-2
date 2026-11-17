# Video 2 Transcript: Code Walkthrough & Optimization Engine

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Video Length:** ~3–4 Minutes  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video2-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script

> "Hello again. This is Video 2, our code walkthrough for Project 2. My name is Lucas Timm. In this video, I will share my screen, open our Python codebase in `app.py`, and walk through the quantitative modeling stack line by line.
> 
> Let's start with our data ingestion and mathematical foundation. 
> 
> In lines 38 through 78 of `app.py`, we define `compute_statistics_from_prices`. This function takes our raw `prices.csv` file—which contains 60 monthly observations of adjusted close prices for `SGOV`, `RXI`, and `PEJ` from October 2021 to September 2026. 
> 
> For each asset, it computes simple monthly returns: $R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$. It annualizes the mean return by multiplying the monthly average by 12, and calculates annualized sample volatility using Bessel's correction—dividing by $m - 1$—and multiplying by the square root of 12. 
> 
> Notice how we construct the covariance matrix: each cell is computed as $\text{Cov}_{i,j} = \text{Corr}_{i,j} \times \sigma_i \times \sigma_j$. We enforce mathematical symmetry across all pairs, ensuring that $\text{Cov}(\text{RXI}, \text{PEJ})$ equals $\text{Cov}(\text{PEJ}, \text{RXI})$.
> 
> Moving to lines 80 through 96, `portfolio_metrics` calculates portfolio return as the inner product of weights and mean returns, and portfolio variance using the double summation: $\sigma_p^2 = \sum_i \sum_j w_i w_j \text{Cov}_{i,j}$. We take the square root of variance to get portfolio volatility, and calculate the Sharpe ratio using SGOV's 3.78% yield as the institutional risk-free rate.
> 
> Now let's examine the core optimization engine in lines 98 through 135: `find_lowest_risk_mix`. 
> 
> Instead of using an opaque black-box solver, we implement a transparent grid search over 5 percentage-point weight steps. The nested loops test every possible combination of $w_1$, $w_2$, and $w_3$ such that weights sum exactly to 1.0 and all weights are non-negative.
> 
> For every candidate mix, the function enforces two hard mathematical constraints:
> First: `p_ret >= obj_ret - 1e-5`, checking that expected return meets or exceeds our 5.03% hurdle.
> Second: `weights['SGOV'] >= reserve_min - 1e-5`, ensuring that cash Treasuries meet our 3.0% distribution liquidity covenant.
> If both hurdles are cleared, it calculates portfolio volatility, and keeps the mix that achieves the absolute global minimum volatility across the grid.
> 
> Next, in lines 137 through 172, `evaluate_mandate_rules` audits any portfolio against the Meridian Foundation's IPS:
> It verifies that weights sum to 100%, confirms long-only compliance, checks the 3.0% reserve floor, tests the return hurdle, validates 5-day liquidity (which is 100% for ETFs), verifies single-issuer limits, and evaluates downside risk via a 95% one-year Value at Risk formula: $\text{Return} - 1.645 \times \text{Volatility}$. If any rule is breached, the function loudly outputs a `FAILS MANDATE` verdict and identifies the exact rule that failed.
> 
> Finally, in our Streamlit UI architecture, we connect this engine to our interactive dashboard. In Section 3, we implement our Point-in-Time macro rates gate, allowing committee members to select an as-of vintage date, and in Section 4, we run a full multi-scenario stress test showing how allocations change under return shocks, cost drag, and window adjustments.
> 
> When I run `streamlit run app.py` in the terminal, the app launches instantly in under two seconds with zero errors, rendering the complete committee dashboard.
> 
> In Video 3, I will present our findings to the investment committee and defend our recommendation. Thank you."
