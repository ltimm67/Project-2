# Project 2 — Investment Management Application

An auditable Streamlit decision tool for a Meridian Foundation reserve-pilot decision. It compares transparent baselines with a 5%-grid constrained portfolio and makes the model's assumptions, limits, and implementation gates visible.

The GitHub-readable canonical output is [`docs/CURRENT-VISIBLE-OUTPUT.md`](docs/CURRENT-VISIBLE-OUTPUT.md).

## Decision

The tool is designed to support a **conditional pilot / do-not-implement-as-is** decision. It never treats a model output as an unconditional investment recommendation: the result must clear net return, liquidity, reserve, turnover, and any explicitly selected downside constraints.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

Run the tests before relying on the result:

```powershell
.venv\Scripts\python -m unittest discover -s tests -v
```

## Repository map

- `app.py` — Streamlit user interface and downloadable decision artifacts.
- `pages/1_Investment_Plan_Builder.py` — general educational plan builder with optional on-demand Yahoo Finance history.
- `pages/2_Company_Research.py` — synchronized Business, Financials, and Valuation tabs for a user-entered ticker.
- `portfolio_engine.py` — deterministic portfolio statistics, optimizer, mandate audit, turnover, and realized-return logic.
- `prices.csv` — versioned monthly prices for SGOV, RXI, and PEJ.
- `tests/` — repeatable calculation tests.
- `docs/` — decision memo, validation record, manifests, and corrected transcripts.

## Model controls

- Net annual return hurdle; annual trading-cost drag is subtracted before the hurdle is tested.
- Minimum SGOV reserve eligible weight.
- 60-month or 36-month estimation window.
- Explicit committee sign-off for turnover above 25%.
- Optional 95% normal-VaR loss limit. This is a governance modeling assumption, not an original mandate rule unless the CIO adopts it.

## Data, reproducibility, and limits

The app uses local versioned price data and displays its SHA-256 hash, observation count, and as-of date. It does not make a live FRED or Yahoo request. This prevents undocumented revisions but means the input data must be refreshed deliberately and documented before a new recommendation.

The model is limited by a small historical sample, historical-return estimates, normal-VaR approximation, annual cost assumption, ETF-level issuer exemptions, and no tax or market-impact model. These outputs are educational decision support, not investment advice or an execution instruction.
