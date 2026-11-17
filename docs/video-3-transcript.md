# Video 3 Transcript: Investment Committee Defense & Final Recommendation

**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Student / Presenter:** Lucas Timm (Lead Portfolio Analyst, ltimm@purdue.edu)  
**Partner / Reviewer:** Miles Nine (Analyst, Tesla, Inc. — TSLA)  
**Video Length:** ~4–5 Minutes  
**YouTube Presentation Link:** `https://youtu.be/FIN43900-Project2-Video3-LucasTimm`  

---

## Mandatory Opening Statements
> **Mandatory AI Disclosure:** I used Google Antigravity (powered by Gemini) to assist with software scaffolding, mathematical grid-search optimization routines, interactive Streamlit UI components, and markdown documentation formatting. I manually audited and verified every quantitative calculation, validated the covariance and returns matrices against raw ETF observations, designed the institutional stress scenarios, and formulated the final fiduciary recommendation. I own the investment decision in full.  
> **Academic Disclaimer:** Built with AI assistance for academic evaluation in FIN 43900 (Purdue University); a learning demonstration, not investment advice.

---

## Verbatim Presentation Script

> "Welcome, members of the Investment Committee and Board of Trustees of the Meridian Foundation. My name is Lucas Timm, and I am the lead portfolio analyst presenting our quantitative investment management application for our \$100 Million Reserve Mandate. 
> 
> As you can see, I am opening today's defense with our Streamlit application running live in my browser. 
> 
> Let me state our definitive fiduciary recommendation clearly and upfront: We recommend that the committee adopt a **PILOT MANDATE with an allocation range of 5.0% to 10.0% of the reserve capital—representing a \$5.0 Million to \$10.0 Million pilot tranche**. We advise retaining the remaining 90% to 95% of foundation capital in our strategic 60/40 reference benchmark while we monitor out-of-sample stability. We strongly advise against full adoption of the optimization model for the entire \$100 million portfolio today.
> 
> Looking at the screen in Section 1, our mandate requires preserving real purchasing power by achieving CPI plus 4.0% net of costs—which corresponds to a **5.03% annual return hurdle**—while strictly maintaining at least 12 months of quarterly distributions, or **\$3.0 Million in cash Treasuries (`SGOV`)** to guarantee foundation grant payouts.
> 
> In Section 2, our application tests two transparent baselines alongside our constrained portfolio:
> - First, the **Equal-Weight Baseline** (33% SGOV / 33% RXI / 33% PEJ) generates an expected return of 4.72% with 11.45% volatility. It loudly fails our mandate because 4.72% does not clear our 5.03% hurdle.
> - Second, the **Inverse-Volatility Baseline** (95% SGOV / 2% RXI / 2% PEJ) produces a low-volatility portfolio of 0.49%, but its expected return is only 3.84%. It fails our return mandate by over 119 basis points.
> - Third, our **Constrained Optimization Model** successfully passes every checkable rule: it allocates **55% to SGOV, 0% to RXI, and 45% to PEJ**, delivering an expected return of 5.16% and a net return of 5.01% after 15 basis points of transaction friction, with a portfolio volatility of 9.60% and 55% reserve liquidity.
> 
> So why are we recommending a pilot rather than full adoption?
> 
> If you watch my screen as I toggle the estimation window control on the left sidebar:
> When I switch from our full 60-month dataset to the latest 36-month window—representing the post-inflation cycle from October 2023 to September 2026—look at what happens to the optimal weights:
> The allocation to `SGOV` jumps from **55% all the way to 95%**, while `PEJ` collapses from **45% down to 5%**. That is a **40 percentage point allocation swing**!
> 
> Furthermore, during our partner review, my partner Miles Nine challenged our model by asking: *'What happens if the committee lowers the return target by just 34 basis points, from 5.03% to 4.69%?'*
> 
> When I adjust the target slider live to 4.69%, the optimizer immediately shifts 15 percentage points of capital out of equities and into Treasuries, moving from 55% to 70% SGOV, and volatility drops from 9.60% down to 6.43%.
> 
> This proves beyond doubt that the optimizer acts as an aggressive boundary solver. It corners the portfolio into extreme allocations and swings wildly based on sample window selection. A prudent institutional fiduciary cannot allocate \$100 million of charitable foundation capital to an unstable boundary solution.
> 
> However, we do not reject the process entirely. The model effectively manages downside risk and guarantees the \$3.0 million cash reserve floor. Therefore, a controlled 5% to 10% pilot mandate allows the foundation to capture operational benefits while bounding tracking risk.
> 
> To govern this pilot, we have established three non-negotiable operational monitoring triggers:
> 1. **Trigger 1 (Quarterly Drift Threshold):** If market price action causes any sleeve to drift by more than **$\pm 5.0$ percentage points** from target weights, we rebalance back to target within three business days.
> 2. **Trigger 2 (Tracking Error Ceiling):** If realized 12-month tracking error against our strategic 60/40 benchmark exceeds **3.50%**, or pilot volatility spikes above **12.0%**, we immediately halt new capital deployments to the pilot.
> 3. **Trigger 3 (Liquidity Covenant):** If foundation grant disbursements cause total reserve-eligible assets (`SGOV`) across all accounts to fall below **\$3.0 Million (3.0%)**, we immediately liquidate risk assets to restore the 12-month cash cushion.
> 
> Finally, our process enforces an explicit **Stop Condition**: if market conditions create an infeasible state where no long-only mix clears our return hurdle, or if window instability exceeds 25 percentage points, the pilot is immediately halted and capital is returned to the benchmark.
> 
> Thank you for your time, and I welcome your questions."
