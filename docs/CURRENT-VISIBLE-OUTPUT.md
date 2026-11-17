# Current Visible Executed Output

**Model version:** 2026-11-17  
**Price-data as-of date:** 2026-09-01  
**Decision framework:** 5% allocation grid; 5.03% net annual return hurdle; 15 bps annual trading-cost drag; 3.0% SGOV reserve floor; current portfolio = 40% SGOV / 60% RXI.

## Base case — all 60 months

| Portfolio | SGOV | RXI | PEJ | Gross return | Net return | Volatility | 95% normal VaR | Mandate result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Equal weight | 33.3% | 33.3% | 33.3% | 4.72% | 4.57% | 12.76% | -16.27% | Fails net-return hurdle |
| Inverse volatility | 95.4% | 2.4% | 2.2% | 3.84% | 3.69% | 1.07% | 2.08% | Fails net-return hurdle |
| Constrained portfolio | 50.0% | 0.0% | 50.0% | 5.31% | 5.16% | 10.65% | -12.21% | Conditional: 60.0% turnover requires sign-off |

### Rule audit — constrained portfolio

- Weights sum to 100%: pass
- Long only: pass
- Net return hurdle: pass
- Reserve floor: pass
- Five-day liquidity: pass
- Issuer limit: pass under the diversified-ETF exemption
- Turnover <=25% or committee sign-off: **fails without sign-off**
- Optional modeled 95% normal-VaR limit: **fails** if the committee adopts it

## Stress case — last 36 months

The constrained portfolio becomes **90% SGOV / 5% RXI / 5% PEJ**. The largest sleeve changes by **40 percentage points** from the base case, breaching the 25-point estimation-stability stop condition.

## Committee decision

**Conditional pilot / do not implement as-is.** The base portfolio clears the net-return and reserve tests but needs explicit turnover approval; the window-sensitivity result independently triggers the stability stop condition. No full adoption is recommended until the committee resolves the turnover and downside-risk governance rules.

## Reproduce

```powershell
python -m streamlit run app.py
python -m unittest discover -s tests -v
```

The app displays the input-data SHA-256 hash, as-of date, and an exportable decision JSON at runtime.
