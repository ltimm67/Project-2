# Video 1 Transcript: Research Evolution & System Design

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Exact Duration:** 2:48 (Course Requirement: <= 3:00)  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video1-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script with Timestamps

[00:00] "Hello everyone. My name is Lucas Timm, Lead Portfolio Analyst for Project 2 in FIN 43900. In this video, I am documenting our research evolution and how our quantitative system and thinking changed for the Meridian Foundation's $100 Million Reserve Mandate, as well as one AI output I audited and corrected.

[00:25] When we began in Lab 13 with the Meridian mandate, my initial assumption was that portfolio construction was a straightforward engineering optimization problem: take the foundation's 5.03% return hurdle (CPI + 4.0%), plug in historical returns and volatilities for Treasuries (SGOV), global discretionary (RXI), and leisure (PEJ), and let a mean-variance optimizer find the lowest-volatility combination.

[00:55] But through our research progression from Edition A to Edition B, my entire mental model shifted. Optimizers are notorious error maximizers. Over our full 60-month dataset, the optimizer selected 55% SGOV, 0% RXI, and 45% PEJ. It completely eliminated global equities because PEJ had a higher historical return (6.85% vs 3.53%), even though PEJ carried 21.22% volatility.

[01:25] The turning point came when we executed our 36-month lookback stress test. Shifting the window caused an extreme 40 percentage point reallocation into cash, jumping from 55% to 95% SGOV. That single test revealed severe estimation fragility. An institutional committee cannot deploy $100 million of charitable capital to a mathematical boundary that swings 40 points based on lookback window selection. This drove our final decision to reject full adoption and recommend a bounded 5% to 10% pilot.

[01:58] Now, regarding the AI output I checked: During development, the AI assistant suggested using a continuous SciPy quadratic solver with floating-point weights, generating an unconstrained mix of 54.68% SGOV and 45.32% PEJ.

[02:18] I audited and corrected this for two reasons: First, institutional committees operate on discrete 5% rebalancing steps rather than decimal-point false precision. I rewrote the engine to use a discrete 5% grid search. Second, the AI initially assumed zero correlation between SGOV and equities. I manually audited prices.csv and proved that SGOV had a positive 0.26 correlation with RXI and 0.17 with PEJ due to the 2022-2023 rate hikes. Correcting this correlation in code ensured our risk metrics reflected true market behavior.

[02:40] In Video 2, I will walk through the codebase line by line. Thank you."
