# Model Update and Validation Addendum

## Why this addendum exists

The original Project 2 prototype displayed transaction drag and a normal-VaR estimate but did not bind both to its decision logic. The current model corrects that gap. This addendum is the authoritative record for the current code in `app.py` and `portfolio_engine.py`; older static tables are retained as historical project artifacts and should not be treated as current output.

## Corrected base case

Using all 60 monthly observations through 2026-09-01, a 5.03% **net** hurdle, 15 bps annual trading-cost drag, 3.0% SGOV reserve floor, and the 5% allocation grid:

| Item | Result |
|---|---:|
| Constrained weights | 50% SGOV / 0% RXI / 50% PEJ |
| Gross expected return | 5.31% |
| Net expected return | 5.16% |
| Annualized volatility | 10.65% |
| Modeled 95% normal VaR | -12.21% |
| One-way turnover from 60/40 | 60.0% |

The portfolio clears the net-return and liquidity constraints, but exceeds the 25% turnover cap without committee approval. It also fails the optional modeled normal-VaR limit if that governance model is adopted. Therefore the appropriate output is **conditional pilot / do not implement as-is**, not an unconditional pass.

## Corrected stress case

On the last 36 months under the same inputs, the lowest-risk mix is 90% SGOV / 5% RXI / 5% PEJ. The largest sleeve moves 40 percentage points from the base case, exceeding the 25-point stability stop condition.

## Reproducibility checks

- The app displays a SHA-256 hash of the exact `prices.csv` file used.
- `tests/test_portfolio_engine.py` verifies statistics, net-cost treatment, turnover, and optimizer constraints.
- GitHub Actions runs that test suite on each push and pull request.

## AI disclosure

AI assisted with code structuring and documentation. The numerical logic is executed by deterministic Python code and should be independently reviewed before any real-world use.
