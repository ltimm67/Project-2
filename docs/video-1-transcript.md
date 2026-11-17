# Video 1 Transcript: Research Evolution & System Design

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Video Length:** ~3–4 Minutes  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video1-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script

> "Hello, everyone. My name is Lucas Timm, and this is Video 1 for Project 2 in FIN 43900. I am presenting our investment management application and portfolio process developed for the Meridian Foundation's \$100 Million Reserve Mandate. 
> 
> In this video, I want to walk through how my thinking and our quantitative system evolved over the semester, and specifically discuss one AI output that I had to audit, challenge, and correct.
> 
> When we started in Lab 13 with the Meridian mandate, my initial assumption was that portfolio management was essentially an engineering optimization problem: take the client's return hurdle—which was CPI plus 4%, or about 5.03% annually—plug in historical returns and volatilities for our universe of Treasuries (`SGOV`), global consumer discretionary (`RXI`), and leisure (`PEJ`), and let a mean-variance optimizer find the lowest-risk combination.
> 
> But as we moved into Lab 14 and Lab 15, my entire mental model shifted. I realized what Richard Michaud famously called the 'Markowitz optimization enigma': optimizers are error maximizers. They latch onto small differences in historical returns and push capital aggressively to boundary solutions. 
> 
> When I looked at our full 60-month dataset, the optimizer selected 55% SGOV, 0% RXI, and 45% PEJ. It completely eliminated global equities because PEJ had a higher historical return (6.85% vs 3.53%), even though PEJ had higher volatility and a 0.79 correlation to RXI. But when we tested our first stress scenario—shortening the estimation window to the latest 36 months—the allocation experienced a violent 40 percentage point shift, jumping to 95% SGOV and only 5% PEJ. 
> 
> That was an eye-opening moment for me as an analyst. An institutional foundation cannot deploy \$100 million of real endowment capital to a mathematical model that moves 40% based purely on whether you look at three years versus five years of data. That realization changed our entire thesis: instead of recommending full adoption, we realized the only fiduciary recommendation is a bounded PILOT of 5% to 10%, while keeping the core capital in the strategic 60/40 benchmark.
> 
> Now, turning to the AI output I checked: During development, the AI assistant suggested using a continuous SciPy quadratic optimizer with floating-point weights, which generated an unconstrained mix of 54.68% SGOV and 45.32% PEJ. 
> 
> I rejected and corrected this AI recommendation for two fundamental institutional reasons. First, in institutional asset management, trading to two decimal places of a percent creates false precision and excessive trading friction. Real committees operate on discrete rebalancing steps. I rewrote the engine in Python to use a transparent 5-point discrete grid, which guarantees that every mix can be audited and tested by hand. 
> 
> Second, I audited the AI's calculation of the covariance matrix. The AI initially assumed zero correlation between SGOV and equity sleeves. I manually inspected `prices.csv` and confirmed that SGOV has a positive 0.26 correlation with RXI and 0.17 with PEJ due to the Federal Reserve's rate-hiking cycle in 2022 and 2023. Correcting this correlation in the code prevented the optimizer from artificially understating portfolio risk.
> 
> In Video 2, I will walk you through the code line by line to show exactly how our app executes these rules. Thank you."
