# Video 2 Transcript: Code Walkthrough & Optimization Engine

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Exact Duration:** 4:25 (Course Requirement: <= 5:00)  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video2-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script with Timestamps

[00:00] "Hello again. This is Video 2, our code walkthrough for Project 2. My name is Lucas Timm. In this video, I will share my screen and walk through our Python mathematical engine in `portfolio_engine.py` and our interactive dashboard in `app.py`.

[00:25] Looking at `portfolio_engine.py`, lines 18 through 27 implement `load_prices` and `file_sha256`. The function ingests our 60 monthly observations for SGOV, RXI, and PEJ, requiring at least 37 observations for statistical degrees of freedom, and computes the cryptographic SHA-256 hash to guarantee data provenance without look-ahead revisions.

[00:58] In lines 38 through 58, `statistics` calculates period-by-period percentage returns, annualizes the mean returns by multiplying by 12, and calculates sample volatilities using Bessel's correction with $m-1$ degrees of freedom. SGOV annualized return is 3.78% at 0.48% volatility; RXI is 3.53% return at 19.07% volatility; and PEJ is 6.85% return at 21.22% volatility.

[01:35] Lines 60 through 72 define `metrics`. We compute gross return as the inner product of weights and mean returns, net return by subtracting trading drag (15 bps), and portfolio variance through the double summation $w^T \Sigma w$. We also calculate the 95% one-year Value-at-Risk using the normal parametric formula: Return minus 1.645 times Volatility.

[02:10] In lines 78 through 92, `optimize` implements our exhaustive 5% discrete grid search solver. It evaluates all valid non-negative weight combinations summing to 1.0, enforces the net return hurdle (5.03%) and minimum SGOV reserve floor (20.0%), and isolates the global minimum-variance allocation.

[02:45] Lines 94 through 108 implement `mandate_audit`. This function formally audits 8 institutional rules from the Meridian IPS: weights sum to 100%, long-only compliance, net return hurdle, reserve floor, 10% volatility ceiling, 5-day liquidity (which is 100% for ETFs), single-issuer limits, and one-way turnover against the current 60/40 benchmark.

[03:25] Turning to `app.py`, we construct the Streamlit UI. Section 1 renders the executive decision banner and KPI cards. Section 2 uses Altair to build an interactive Markowitz Efficient Frontier with 600 simulated portfolios, asset allocation sleeve bar charts, and a backtested $10,000 equity curve. Section 3 and 4 render the dynamic mandate audit and transparent baseline comparisons.

[04:00] Finally, in `verify_project2.py`, we provide a standalone verification runner that executes in under 0.3 seconds and automatically exports `visible_output.json`, ensuring the Stranger Standard is completely satisfied.

[04:18] In Video 3, I will present our live app and defend our committee recommendation. Thank you."
