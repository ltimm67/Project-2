# Video 1: Research Evolution & System Design (Corrected Transcript)
**Course:** FIN 43900 — Advanced Financial Modeling / AI in Finance (Fall 2026)  
**Presenter:** Lucas Timm (ltimm@purdue.edu) — Lead Portfolio Analyst  
**Recording Date:** November 23, 2026  
**Duration:** 3m 22s  
**YouTube Link:** https://youtu.be/3y5cM4I0CYg  

---

### Verbatim Transcript

Meeting with Lucas Anthony Timm-20261123_122956-Meeting Recording
November 23, 2026, 5:29PM
Duration: 3m 22s

Lucas Anthony Timm started transcription

[00:04]
"All right, hello, hello. My name is Lucas Timm. I am the lead analyst here for the $100 million reserve mandate Lab 13 that we worked on. And I'm going to go through how my viewpoint changed and I'm going from that to now. 

I'll start off by saying this is not investment advice, this is educational purposes only, and I will go into my AI statement:

I used Google Antigravity and Gemini Pro to come up with, you know, the scaffolding, the mathematical grid searches, the analysis, the stress testing, and the Streamlit components to build the app, but you know, the model choices, all of this was reviewed, authorized, and finalized by me. But once again, this is not investment advice, so take it with a grain of salt.

So, in this video, Video 1, I'm documenting our research evolution, you know, our thought process from Lab 13 to now on Meridian Foundation's $100 million reserve mandate, as well as one AI output that I ultimately thought we should audit and correct.

So when I began Lab 13, you know, I thought this was a simple engineering optimization problem. Straightforward, you know, take the 5%, plug in some historical data, and then ultimately find the lowest volatility, you know, combination.

But I was soon incorrect, so I'll jump over here and get into a little bit of why, you know, what changed with me and my partner, Miles, as we went on.

So, we realized the model was, you know, an unconstrained statistical optimizer that was very naive in recommending the immediate 100% deployment into the highest historical return assets. So with AI, we, you know, created some baselines—Equal Weight, Inverse Volatility—and ultimately conducted the stress testing, which was the pivotal point for us. 

So we realized that full adoption was rejected with the discovery that shortening the sample window to 36 months caused the optimal SGOV allocation to jump by 40 percentage points. And this was huge for us in, you know, figuring out what happened there.

And then one thing, you know, that I changed ultimately, with the help of AI, of course, but the AI assistant suggested using a continuous quadratic solver with floating weighting points and ultimately assumed 0 correlation between cash and equities.

So I flagged this, audited it, and corrected the output for basically 2 reasons: 
First, committees operate on discrete 5% rebalancing steps rather than this decimal point false precision. So I rewrote that. 
And then also, the AI initially assumed 0 correlation between SGOV and equities, which could be manually audited in the prices.csv, and ultimately proved that it had a positive correlation with both RXI and PEJ due to some 2022 and 2023 rate hike data. 

And you know, this ensured our risk measures reflected true market behavior rather than making assumptions.

So I'll be back in Video 2 to go through some code line by line and share the rest of the project. Thanks."

Lucas Anthony Timm stopped transcription
