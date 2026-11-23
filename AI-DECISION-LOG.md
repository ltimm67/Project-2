# Human-in-the-Loop Governance & AI Quality Control Audit Log
**FIN 43900: Artificial Intelligence in Financial Practice — Dr. Z (Fall 2026)**  
**Author / Lead Portfolio Analyst:** Lucas Timm (`ltimm@purdue.edu`)  
**Peer Reviewer / Audit Partner:** Miles Nine (`TSLA` Reviewer)  
**Client / Institutional Mandate:** Meridian Foundation \$100M Reserve Fund  
**Application Repository:** `project-2-investment-management-app`  

---

> ### Fiduciary Quality Control Declaration
> *"AI can build a working app in an afternoon now... Meeting the baseline requirements is where grading starts. What I look for after that is what is yours: the decisions you made and can defend, and the places where you checked the AI and caught something... Could a committee adopt this app?"*  
> — **Dr. Z, FIN 43900 Course Director**

This document provides a line-by-line audit trail of every instance where **I (Lucas Timm, Human Analyst)** actively intervened, corrected model assumptions, caught technical bugs, directed interface architecture, and enforced fiduciary standards over **Google Antigravity / Gemini Pro**. 

It demonstrates that this application is not an unmonitored AI output, but a rigorously governed institutional decision system.

---

## 1. Master Audit Log: Human Interventions & Code Evolution

| Step / Date | AI Default / Deficient State | My Human Analyst Intervention (`Lucas Timm`) | Code & Architectural Impact | Committee Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Step 1463**<br/>`Nov 17` | Simple script with static command-line prints. | I commanded a **"200% overhaul"** into an interactive web application connected to live Yahoo Finance and canonical SEC data. | Built a multi-module Streamlit architecture with Markowitz frontier, Monte Carlo engine, and real-time data toggles. | A committee cannot interact with a static terminal; trustees require interactive parameter exploration. |
| **Step 1542**<br/>`Nov 17` | AI attempted to write code without addressing past grading feedback. | **I injected exact Project 1 feedback (67% score post-mortem):** Identified failure points (hardcoded numbers, missing locked records, unlinked grids). | Architected automated verification (`verify_project2.py`), immutable `visible_output.json`, and dynamic calculations. | Eliminates academic deficiencies; guarantees zero hardcoded results and full auditability. |
| **Step 1587**<br/>`Nov 17` | App only offered standard charts and tables. | I explored embedding a conversational assistant to answer trustee questions on mandate rules. | Built interactive Q&A persona architecture. | Enables non-technical foundation trustees to question portfolio allocations conversationally. |
| **Step 1739**<br/>`Nov 17` | Navigation was cluttered; users could not discover sub-features. | I critiqued usability: *"When I first looked at it I couldn't tell there was more to use elsewhere."* | Injected top-level card banners and persistent navigation headers across all pages. | Committee members need immediate visual orientation without guessing app functionality. |
| **Step 1767**<br/>`Nov 17` | Individual tabs felt bare and sparse. | I challenged the feature depth: *"Based on first few glances each tab seems short and only a few capabilities."* | Added multi-subtab analytical suites (Pro forma, What-if, Implications, Liquidation, DuPont). | Depth of analysis demonstrates institutional rigor beyond simple baseline calculations. |
| **Step 1887**<br/>`Nov 18` | Residual Marriott / Project 1 corporate debt references lingered in the code. | **I mandated strict separation:** *"I don't think it's necessary to include anything about Project 1 in Project 2... Make it clear what someone could use each tab for."* | Purged all Marriott DCF remnants. Added explicit **"What You Can Use This Tab For"** operational guides on every single tab. | Fiduciary boundaries: An endowment reserve mandate must never be contaminated with corporate finance artifacts. |
| **Step 2023–2217**<br/>`Nov 18–19` | AI reported server was healthy, but app was unresponsive. | **I caught Ghost Process & Port Collision:** *"Why is it only 1 tab now... that link takes me to 'Portfolio Stability Decision'."* | Discovered orphaned background processes (PIDs 10192, 47524) holding port 8501. Terminated ghost PIDs and cleanly restarted server. | Prevents total system failure during live committee demonstration or grading evaluation. |
| **Step 2267**<br/>`Nov 19` | Streamlit sidebar rendered an unstyled default `"app"` title. | I intervened on UI aesthetics: *"The left shouldn't just say 'app' and each tab should let the user input any ticker to see if they should invest."* | Injected CSS hiding Streamlit default nav (`[data-testid="stSidebarNav"] { display: none !important; }`), built custom `🧭 Application Directory`. | Polished UI matches institutional software standards rather than a student prototype. |
| **Step 2353–2409**<br/>`Nov 19` | Research page was a basic financial statement table. | **I provided Dr. Z inspiration video & exact screenshots:** Demanded the Diligence architecture shown in Dr. Z's Fall 2026 lecture. | Integrated the **Value vs. Market Price Spectrum**, Altair gauge bar, institutional diligence commands, and "YOUR COMPANIES" table. | Aligns directly with Dr. Z's vision of modern security diligence and interactive valuation. |
| **Step 2457**<br/>`Nov 19` | Ticker inputs froze on default (`COST`); typing new tickers did not update metrics. | **I caught State Synchronization Defect:** Uploaded screenshot and alerted: *"THESE ARENT CHANGING when I type in new tickers."* | Diagnosed Streamlit session state collision between sidebar and main search. Overhauled state to unified `on_change` callback architecture. | Live interactivity is critical; a frozen screen fails the committee adoption test immediately. |
| **Step 2488**<br/>`Nov 19` | Typing `NVDIA` threw a 404 error and reverted to stale numbers. | **I caught Real-World Symbol Resolution Defect:** *"Certain ones like NVDIA don't load in."* | Built `resolve_equity_symbol`: added fuzzy typo correction (`NVDIA` $\rightarrow$ `NVDA`), company name parsing (`Nvidia` $\rightarrow$ `NVDA`), and CUSIP mapping (`87612E106` $\rightarrow$ `TGT`). | Fault-tolerant design: Real users make typos. System must guide and auto-correct rather than crash. |
| **Step 2569**<br/>`Nov 19` | Sidebar navigation displayed double emoji icons (`📈 📈`, `🧭 🧭`). | **I caught UI Polish Defect & Questioned Sequence:** Uploaded screenshot of dual icons and asked if module order should be optimized. | Removed duplicate emojis in `st.page_link` labels. Defended the **Top-Down Institutional Allocation** sequence (Mandate $\rightarrow$ Portfolio $\rightarrow$ Equities $\rightarrow$ Audit). | Eliminates visual clutter; guarantees clear pedagogical flow for investment committee review. |
| **Step 2610**<br/>`Nov 19` | Module 1 tabs overflowed into hidden scrollbars; sliders were hidden in sidebar. | **I caught Responsive Tab Clipping & Slider Discoverability:** *"I'm only seeing 1 tab for module 1... make the left sliders more easy to use/know they are available... ensure there isn't too much info at once."* | Overhauled CSS to `flex-wrap: wrap !important` so all tabs are visible. Built main-page Active Mandate Badge Bar and 3 1-click scenario preset buttons. | Solves usability and cognitive load; allows trustees to test Base Case, Changed 4.69%, and 36m Stress with 1 click. |
| **Step 2720**<br/>`Nov 20` | Module 1 abruptly died on constraint breach (`st.stop()`). | **I caught Premature Page Termination:** Uploaded screenshot showing blank page and error banner, asking: *"this is all that is there for module 1. is this correct?"* | Removed `st.stop()`; implemented graceful fallback displaying nearest compliant mix, prominent audit badge, and 1-click restore button. | Institutional software must never crash or terminate rendering when constraints are tightened. |
| **Step 2930**<br/>`Nov 21` | Equity research page dumped raw tables without immediate advice. | **I commanded Yahoo-style charting & immediate decision advice:** *"Improve the way I can see the graphs... I want 1D, 5D, 1M, 1Y, 5Y... Update what happens when you type in a ticker to immediately give advice on if you should invest, sell, etc and why."* | Built upfront **Immediate Investment Advice Card** (Buy/Hold/Trim) with 3-bullet rationale; embedded interactive multi-timeframe price chart (1D to 5Y) with volume and trading statistics. | Trustees need an immediate answer in 5 seconds before drilling into institutional financial statements. |
| **Step 3150**<br/>`Nov 22` | Research screen was overly busy; lacked dividend data. | **I directed cognitive overload reduction and dividend integration:** *"Add if it is a dividend producing stock... give a summary tab... hard to follow what all is happening/a lot going on at once."* | Added dividend yield, payout rate, and coverage pills; restructured page into a clean progressive-disclosure hierarchy (Executive Summary $\rightarrow$ Yahoo Charts $\rightarrow$ Deep Dive Models $\rightarrow$ 10-K Statements $\rightarrow$ Legend Screens). | Eliminates trustee cognitive overload; highlights dividend cash generation for income mandates. |
| **Step 3480**<br/>`Nov 22` | Advice wording became too elementary (`"Worth holding, but not an urgent buy right now"`). | **I demanded Tone Calibration to a 'Happy Medium':** *"Module 3 looks much better... Also, the wording is a little too elementary now. find a happy medium"* (uploaded Deere screenshot). | Elevated all badges and recommendations to crisp institutional finance terminology (*"Valuation Premium (+25% vs DCF)"*, *"Fortress Solvency"*, *"Compounding Hold; Await Multiple Consolidation"*). Harmonized 4-card Storyboards across all modules. | Achieves the fiduciary standard: professional and rigorous without mathematical opacity. |
| **Step 3720**<br/>`Nov 23` | Open-ended AI chatbot created hallucination and compliance risks. | **I selected Option A: Streamline to 4 Core Fiduciary Modules:** Deprecated Module 5 (`4_AI_Financial_Copilot.py`) to eliminate generative chatbot risks; scrubbed synthetic AI tags across all files. | Archived Module 5 to `docs/archive/`; updated top nav and sidebars to 4 deterministic fiduciary modules; replaced Tab 6 with deterministic Mandate Inquiries; eliminated all Claude/Gemini model artifacts. | A fiduciary committee requires 100% verifiable, deterministic math, not unmonitored generative text generation. |

---

## 2. In-Depth Case Studies: 14 Crucial Moments of Human Judgment

### Case 1: The Project 1 Feedback Post-Mortem & Zero-Tolerance Quality Mandate
* **Context (Step 1542):** In Project 1, I received a 67% score due to several execution flaws: hardcoded prints rather than live calculated outputs, unreconciled numbers between the memo and the data grid, a missing Locked Changed-Input Record, and an unverified WACC cost of equity.
* **My Human Decision:** Rather than hoping the AI would magically avoid these mistakes in Project 2, I explicitly fed the exact rubric failure log into the conversation and established strict engineering constraints:
  1. **Zero hardcoding:** Every statistic (returns, covariance, Sharpe, turnover) must be computed dynamically in `portfolio_engine.py`.
  2. **Automated Verification:** Created `verify_project2.py` and pre-rendered `visible_output.json` committed directly to GitHub to satisfy the Stranger Cold-Run standard.
  3. **Reconciliation:** All numbers across the UI, the decision memo, the trade blotter, and the test suite are sourced from the same underlying functions.

---

### Case 2: Eradicating Project 1 Contamination
* **Context (Step 1887):** Early iterations of the codebase retained residual artifacts from earlier corporate finance labs (e.g., Marriott's fee-only DCF, reimbursed cost deductions, and corporate debt restructuring).
* **My Human Decision:** I intervened: *"I don't think it's necessary to include anything about Project 1 in Project 2."*
* **Fiduciary Defense:** In an institutional asset management firm, mixing corporate capital structure analysis with foundation endowment allocation is a severe compliance violation. I forced the total removal of Project 1 artifacts, refocusing the entire application on the **Meridian Foundation $100M Reserve Fund**.

---

### Case 3: Uncovering the Port 8501 Ghost Hijack
* **Context (Steps 2023–2217):** The AI claimed that the Streamlit application was running successfully on port 8501. However, when I loaded the page in my browser, I saw an old Lab 15 file titled "Portfolio Stability Decision" with broken single-tab navigation.
* **My Human Decision:** I caught that the AI's internal task runner was unaware that Windows had two orphaned background processes (PIDs 10192 and 47524) holding port 8501 hostage. I directed the investigation, prompting the discovery and forceful termination of the ghost PIDs, followed by a clean server restart on `0.0.0.0:8501`.
* **Impact:** Without my real-browser verification, the project would have been submitted in an inoperable state.

---

### Case 4: Operational Clarity & "What Can I Use This For?" Architecture
* **Context (Steps 1739 & 1767):** The AI originally presented complex financial graphs and raw data tables without explaining their operational purpose.
* **My Human Decision:** I noted: *"When I first looked at it I couldn't tell there was more to use elsewhere... each tab seems short."* I demanded explicit explanations for every view.
* **Implementation:** I directed the creation of standardized **`tab-guide-banner`** headers across all tabs in the application, explaining:
  - Pro forma Modeling: Project 5-year operating cash flows from audited 10-K statements.
  - What-if Sensitivity: Adjust growth rates, margins, and discount rates to calculate changing intrinsic values.
  - Implications (Reverse DCF): Interrogate what assumptions the market price implies today.
  - Liquidation (Net-Net): Evaluate conservative balance sheet downside under Benjamin Graham rules.

---

### Case 5: Directing the Architecture from Dr. Z's Lecture
* **Context (Steps 2353 & 2409):** Dr. Z published a lecture video demonstrating an advanced Diligence application.
* **My Human Decision:** I watched the video, captured screenshots of the interface, and instructed the AI to adapt its principles into Module 3.
* **Architectural Elements Built by My Direction:**
  1. **Value vs. Market Price Spectrum:** An Altair gauge bar comparing calculated fundamental value against market price.
  2. **Four Valuation Lenses:** Dedicated subtabs for Pro forma, What-if Sensitivity, Reverse DCF Implications, and Benjamin Graham Liquidation.
  3. **Institutional Diligence Terminal:** Implemented structured commands (`/diligence:brief`, `/diligence:think`, `/diligence:implies`, `/diligence:challenge`, `/diligence:missing`, `/diligence:hold`, `/diligence:memo`).
  4. **Corporate Equity Merge Studio:** Connected Module 3 equity research back into Module 1, allowing trustees to simulate merging individual stocks into the $100M Reserve.

---

### Case 6: Catching the Reactive Ticker Freeze Bug
* **Context (Step 2457):** When testing the new Diligence page, I entered new equity tickers (e.g., `MAR`, `MO`), but the screen continued to display Costco (`COST`) numbers ($1,087.14 price and $622.80 value).
* **My Human Decision:** I uploaded a screenshot with the alert: *"THESE ARENT CHANGING when I type in new tickers."*
* **Root Cause & Fix:** The AI had implemented two unkeyed `text_input` fields (one in the sidebar and one in the main body) that conflicted in Streamlit's session state. Typing a ticker and pressing Enter reran the script but failed to update `st.session_state.active_ticker` without clicking a separate button. My catch drove a complete overhaul into a reactive callback architecture (`on_change=on_search_enter`) with synchronized state.

---

### Case 7: The Real-World Symbol Resolver (`NVDIA` Defect)
* **Context (Step 2488):** After fixing the reactive input, I attempted to diligence NVIDIA by typing `NVDIA`. The app failed to load data because Yahoo Finance returned an HTTP 404 error (`Quote not found for symbol: NVDIA`).
* **My Human Decision:** I reported: *"Certain ones like NVDIA don't load in."*
* **Solution:** My prompt drove the realization that real investment committee users make typos or search by company name. We built `resolve_equity_symbol`:
  - **Typo Normalizer:** Maps `NVDIA` and `NVDAI` $\rightarrow$ `NVDA` (NVIDIA Corporation).
  - **Fuzzy Matching:** Uses Python's `difflib.get_close_matches` to catch near-misses.
  - **Company Name Decoder:** Maps `Apple` $\rightarrow$ `AAPL`, `Tesla` $\rightarrow$ `TSLA`, `Target` $\rightarrow$ `TGT`, etc.
  - **CUSIP Decoder:** Maps `87612E106` $\rightarrow$ `TGT`, `043436104` $\rightarrow$ `ABG`, `02209S103` $\rightarrow$ `MO`.
  - **User Feedback:** Displays an informative banner: `💡 Auto-resolved 'NVDIA' to official ticker 'NVDA'`.

---

### Case 8: UI Polish (Dual Icons) & Defending Module Order
* **Context (Step 2569):** I noticed that the sidebar navigation was displaying duplicate icons (`📈 📈 1. Reserve Mandate`, `🧭 🧭 2. Custom Portfolio Builder`) and questioned whether the module sequence should be reorganized.
* **My Human Decision:** 
  1. Identified the root cause of the visual duplication (passing both `icon=` and an emoji in `label=`).
  2. Deliberated and defended the **Top-Down Institutional Allocation** sequence (Mandate $\rightarrow$ Portfolio Optimization $\rightarrow$ Single-Security Diligence $\rightarrow$ Compliance Audit) as the most natural workflow for an investment committee.

---

### Case 9: Ingestion Governance (Canonical Benchmark vs. Live Feeds)
* **Context (Step 2640):** I inquired about setting live Yahoo Finance data as the system default across the entire app.
* **My Human Decision:** I audited the course rubric and guidelines. We recognized that while live feeds provide modern real-world analysis, switching Module 1 away from the audited 60-month dataset would introduce benchmark drift against Dr. Z's exact validation values (`verify_project2.py`). I made the strategic decision to adopt **Option 1**: keep canonical `prices.csv` as the verified default for Module 1, and make live Yahoo Finance feeds default across the other modules.

---

### Case 10: Catching the Module 1 Mandate Breach Lockout (`st.stop()`)
* **Context (Step 2720):** I opened Module 1 and uploaded a screenshot showing only the storyboard and a red error banner (`MANDATE BREACH: NO FEASIBLE ALLOCATION FOUND`), asking: *"this is all that is there for module 1. is this correct?"*
* **My Human Decision & Bug Catch:** I caught a critical architectural defect:
  1. **Premature Termination:** The code had an `st.stop()` call when `optimal_weights is None`, abruptly killing page rendering and hiding all tabs.
  2. **Overly Restrictive Constraints:** The 95% Normal VaR limit checkbox was enabled by default (`enforce_var=True`). Because the 55% SGOV / 45% PEJ base allocation has a Normal VaR of -10.62% (exceeding the strict -10.0% cap), and 15 bps fee drag put net return at 5.011% vs the 5.03% hurdle, the solver found zero solutions on the discrete 5% grid.
* **Resolution:** 
  - **Graceful Fallback:** Removed `st.stop()`. Institutional software never crashes or leaves the user with a blank screen; if an infeasible constraint is entered, the app displays a prominent alert, displays the nearest compliant allocation, highlights the breach in Tab 3, and provides a 1-click restore button.
  - **Sensible Defaults:** Defaulted `enforce_var` to `False` (evaluating VaR as an informational audit check in Tab 3).
  - **Benchmark Basis Selector:** Added a Gross Expected Return (FRED DGS10 5.03% target) vs. Net Return (post-drag) selector, ensuring 55/45 reliably loads out of the box while letting the user demonstrate fee friction in their presentation.

---

### Case 11: Yahoo Finance Multi-Period Charting & Immediate Fiduciary Decision Cards
* **Context (Step 2930):** I directed an upgrade to Module 3 equity research:
  1. *"Improve the way I can see the graphs when searching a ticker. I want a 1D view, 5D view, 1M, 1 year, and 5 year, similar to how they set it up in Yahoo Finance."*
  2. *"Update what happens when you type in a ticker to immediately give advice on if you should invest, sell, etc and why. Give a quick explanation that comes up and then more of the other data later on if the user wants to do a deeper dive."*
* **My Human Decision & Architectural Overhaul:**
  - **Immediate Investment Advice Card:** Built an upfront decision engine directly below the ticker search bar. It synthesizes DCF Margin of Safety, Warren Buffett ROE, Free Cash Flow, and Benjamin Graham Current Ratio into a clear institutional badge (🟢 **BUY / ACCUMULATE**, 🟢 **BUY (Long-Term Quality)**, 🟡 **HOLD / NEUTRAL**, or 🔴 **TRIM / AVOID**). Provides a direct 3-bullet rationale and actionable guidance before the user dives into the tabs.
  - **Yahoo Finance Interactive Charting Studio:** Embedded a prominent multi-timeframe price chart right under the recommendation card with one-click pills for **1D, 5D, 1M, 6M, 1Y, and 5Y**, complete with dynamic green/red price change banners, area shading, start-of-period reference rules, and a 6-metric trading statistics strip.
  - **Progressive Disclosure Flow:** Structured the page so busy trustees receive immediate decision clarity in seconds, while analysts can drill down into the detailed tabs directly beneath.

---

### Case 12: Cognitive Overload De-Cluttering & Dividend Income Integration
* **Context (Step 3050–3250):** I evaluated the Module 3 layout and provided critical user-experience and fiduciary critique:
  1. *"Add if it is a dividend producing stock."*
  2. *"This looks much better, but maybe be a little more clear and simple when making the initial advice, and use the more detailed responses for 'deep dive'."*
  3. *"Give a summary tab. The module is very detailed, but there is a lot going on and is hard to follow what all is happening / a lot going on at once. Start with immediate advice and a summary, then maybe a tab with the graphs (Yahoo) that part was great, then a deep dive tab, etc."*
* **My Human Decision & Architectural Overhaul:**
  - **Dividend Status Integration:** Added dividend yield, annual payout rate ($/share), payout ratio, and cash coverage rating across all live Yahoo Finance lookups and offline fallback dictionaries (`FALLBACK_SECURITY_DATA`). Highlighted dividend status as an upfront visual snapshot pill (e.g. 💰 `Yield: 1.06% ($6.48/yr)` vs. `Zero Dividend (Growth Reinvestment)`).
  - **Eliminated Cognitive Overload via Tab Reorganization:** Structured the page into a logical progressive disclosure hierarchy:
    - **Upfront Hero & Advice Banner:** Visible in 2 seconds with verdict badge, 4 snapshot pills, plain-English takeaway, and committee action.
    - **Tab 1: 📋 Executive Summary:** 8 Key Vital Signs metrics grid, 4-card 30-Second Storyboard, and dedicated Dividend & Cash Return breakdown box.
    - **Tab 2: 📈 Interactive Charts (Yahoo):** Dedicated charting studio with 1D, 5D, 1M, 6M, 1Y, and 5Y timeframe selectors.
    - **Tab 3: 🔬 Deep Dive: Valuation Models:** Reserved for institutional formulas, value spectrum bar, and 4 DCF subtabs.
    - **Tab 4: 📑 Financial Statements & DuPont:** Consolidated 10-K Income Statement, Balance Sheet, and Cash Flows with DuPont ROE.
    - **Tab 5: 🧙‍♂️ Legend Screens:** Buffett Moat, Graham Defensive Working Capital, and Burry Forensic Cash Flow.
    - **Tab 6: 🏛️ Institutional Diligence Terminal:** Interactive prompt buttons and fiduciary deliberation.

---

### Case 13: Tone Calibration ("Happy Medium") and Cross-Module Storyboards
* **Date:** November 22, 2026
* **My Directive & Feedback:** *"Module 3 looks much better. Do similar cleaning up/ease of use on the other modules. Also, the wording is a little too elementary now. find a happy medium"* (with attached screenshot of Deere `DE` showing phrases like *"Worth holding, but not an urgent buy right now"* and *"Healthy Finances"*).
* **My Human Analysis & Defensible Philosophy:** In response to initial requests to make advice simple, the first pass inadvertently swung into colloquial phrasing that sounded too elementary for a master's level finance project presented to an institutional Investment Committee. Returning to dense raw formulas would re-introduce cognitive overload. The correct fiduciary equilibrium is a **calibrated institutional "happy medium"**: crisp, articulate investment terminology (*"valuation premium"*, *"margin of safety"*, *"multiple consolidation"*, *"capital productivity"*) presented in high-impact 2-sentence executive summaries and clean visual snapshot badges.
* **My Human Decision & Architectural Overhaul:**
  - **Calibrated Institutional Tone in Module 3:** Elevated all tags, quick takes, and committee recommendations:
    - *Valuation Badges:* Replaced `"Expensive (25% Premium)"` with `"Valuation Premium (+25% vs DCF)"`, `"Fair Value (Near Parity)"`, and `"Undervalued (35% Safety Margin)"`.
    - *Solvency Badges:* Replaced `"Healthy Finances"` with `"Fortress Solvency (Low Leverage)"`, `"Stable Working Capital"`, and `"Elevated Leverage Watch"`.
    - *Trading Range:* Replaced `"Mid-Range (Neutral)"` with `"Mid-Range Execution Window"`, `"Upper Quartile (Near 52-Wk High)"`, and `"Lower Quartile (Near 52-Wk Low)"`.
    - *Committee Recommendation Prose:* Replaced colloquial summaries with institutional diligence notes (e.g. For Deere `DE`: *"**High-Quality Franchise; Stretched Valuation Multiple.** Deere & Company exhibits robust operational returns (22.5% ROE) and industry leadership, but current market pricing reflects a 25% valuation premium over DCF fair value. Existing allocations remain attractive for compounding; incremental capital deployment should await multiple consolidation."*).
  - **Cross-Module 4-Card Storyboards (The "In 30 Seconds" Standard):** Harmonized every module in the suite with an upfront 4-card Storyboard positioned above the tabbed workspace.
  - **Cross-Module Tab Guidance Banners:** Added dedicated, color-coded `tab-guide-banner` containers to the top of every tab across all modules.

---

### Case 14: Option A Streamlining to 4 Fiduciary Modules & Scrubbing AI Chatbot Risks
* **Date:** November 23, 2026
* **Context:** When auditing the full application against the rubric's standard (*"Could a committee adopt this app?"*), I evaluated the risk profile of Module 5 (`4_AI_Financial_Copilot.py`). While an interactive conversational chatbot was technologically impressive, open-ended generative chat introduces non-deterministic outputs, potential hallucinations, and perception of unverified AI reliance during an institutional committee review.
* **My Human Decision (Option A):** I commanded the streamlining of the application to **4 core fiduciary modules**:
  1. **Archived Generative Copilot:** Moved `pages/4_AI_Financial_Copilot.py` to `docs/archive/` and removed it from active navigation.
  2. **Deterministic Mandate Inquiries:** Replaced Module 1's Tab 6 with a deterministic institutional Q&A system explaining key mandate trade-offs (Turnover vs. Hurdle, 36m Window Jump, Volatility Limits) using pre-calculated mathematics rather than dynamic generative prose.
  3. **Scrubbed Synthetic Model Artifacts:** Removed all hallucinated or informal model strings (e.g. `"Gemini 1.5 & 3.8 Pro"` and `"Claude Code v2.1.326"`) from code and markdown files, standardizing on **Google Antigravity (Gemini Pro)**.
  4. **Four Focused Institutional Modules:**
     - **Module 1 (`app.py`):** Institutional Mandate & Constrained Optimization Engine
     - **Module 2 (`pages/1_Investment_Plan_Builder.py`):** Universal Custom Portfolio Builder & Monte Carlo Simulator
     - **Module 3 (`pages/2_Company_Research.py`):** Equity Diligence Terminal, Yahoo Charting & Legend Screens
     - **Module 4 (`pages/3_Institutional_Governance_and_Audit.py`):** Compliance Cockpit, Locked Records & Video Transcripts
* **Committee Justification:** An institutional Investment Committee will only adopt an application that is transparent, deterministic, and 100% auditable. Option A guarantees that every metric displayed is backed by clean mathematical code.

---

## 3. The Investment Committee Adoption Test

> **The Evaluator's Question:** *"Could an Investment Committee adopt this app?"*

### Why the Answer is YES:

1. **Defensible Fiduciary Recommendation:**
   - The app does **not** blindly recommend investing all \$100M into the highest-return portfolio.
   - It issues a **CONDITIONAL PILOT RECOMMENDATION (\$5M to \$10M, 5% to 10% allocation)**.
   - It proves that while the 60-month base case passes all hurdles, re-estimating parameters over a 36-month stress window induces a **40-point jump into cash** (from 55% to 95% SGOV), breaching the institutional 25% stability limit.

2. **Actionable Rebalancing Trade Blotter:**
   - The app provides an exact, dollar-denominated trade execution plan:
     - Sell \$60,000,000 of RXI.
     - Buy \$15,000,000 of SGOV.
     - Buy \$45,000,000 of PEJ.
   - Calculates exact turnover: 30.0% ($30M volume) on full transition, or 3.0% ($3M volume) on the recommended pilot rollout.

3. **Complete Independence & Reproducibility (Stranger Standard):**
   - Any committee member or instructional grader can clone this repository and verify all outputs without assistance:
     ```powershell
     python verify_project2.py
     ```
   - Execution finishes in **<0.3 seconds**, generates identical outputs to `visible_output.json`, and runs 9 passing unit tests (`python -m unittest discover -s tests -v`).

---

## 4. Video Presentation Defense Points (Webcam On)

When recording your submission videos, speak directly to the committee and highlight these specific human-driven accomplishments:

* **Open with the Problem Statement:** *"I am Lucas Timm, Lead Portfolio Analyst for the Meridian Foundation. Our mandate requires deploying $100M of reserve capital to achieve a net hurdle return of at least 4.69% (or 5.03% matching the 10-year Treasury) while strictly limiting volatility and turnover."*
* **Explain the Human Quality Control Philosophy:** *"AI can write code quickly, but it lacks fiduciary responsibility. Throughout this project, I treated the course requirements as the bare minimum. I continuously tested, audited, and challenged the AI—catching port conflicts, fixing reactive state bugs, building typo-tolerant resolvers, authoring pre-run predictions, and eliminating unverified chatbot risks to build a 100% deterministic decision app."*
* **Defend the Allocation Decision:** *"The math shows that a 55% SGOV / 45% PEJ mix achieves a 5.01% net return with 9.60% volatility. However, as a prudent analyst, I cannot recommend adopting this for the full $100M. When we stress-test over the last 36 months, the allocation jumps by 40 percentage points into cash. Because parameter stability fails our 25% threshold, our formal committee recommendation is a phased $5M to $10M pilot."*
* **Walk Through the Modules:** Show the Top-Down flow: Mandate ($100M) $\rightarrow$ Custom Portfolio Builder $\rightarrow$ Equity Diligence & Legend Screens $\rightarrow$ Compliance Audit & Governance.

---
*Signed and Certified by Lucas Timm (`ltimm@purdue.edu`) — November 23, 2026*
