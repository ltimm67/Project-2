# Lab 20 — Project 2 Readiness Evidence

## D — question

Could a committee member who has never met the analyst reach the Project 2 decision from this repository alone, and does the decision survive one changed input?

## R — stranger route

1. Read [`../README.md`](../README.md) for setup, the finance decision, sources, repository map, and limitations.
2. Run `python -m streamlit run app.py` from the project folder.
3. Read the visible rule audit, baselines, stability result, data hash, and downloadable decision artifact.
4. Run `python -m unittest discover -s tests -v` to reproduce the calculation checks.
5. Read [`MODEL-UPDATE.md`](MODEL-UPDATE.md), [`decision-memo.md`](decision-memo.md), and [`validation-and-ai-use.md`](validation-and-ai-use.md).

## I — partner cold run receipt

This receipt must be completed by the partner who performs the run, without coaching.

| Field | Partner-completed evidence |
|---|---|
| Partner name | `[fill in]` |
| Date and time | `[fill in]` |
| Fresh folder / environment used | `[fill in]` |
| Commands run | `[fill in]` |
| First blocker, if any | `[fill in]` |
| Visible location of the decision | `[fill in]` |
| One thing the README made clear | `[fill in]` |
| One thing the partner could not infer | `[fill in]` |

## V — locked changed-input record

The completed record belongs in [`validation-and-ai-use.md`](validation-and-ai-use.md). Before executing, the student must personally write the prediction with AI closed, then commit it. Use [`LOCKED-CHANGED-INPUT-TEMPLATE.md`](LOCKED-CHANGED-INPUT-TEMPLATE.md); do not replace the bracketed fields with AI-written content.

## E — one fix

The original prototype displayed transaction drag and normal VaR but did not bind them to the decision logic. The current engine now tests the **net** return hurdle, calculates one-way turnover, and makes normal VaR an explicit optional governance constraint. The validation evidence is in [`MODEL-UPDATE.md`](MODEL-UPDATE.md) and `tests/test_portfolio_engine.py`.

## Decision line

The current model result is **conditional pilot / do not implement as-is**: the base 50% SGOV / 50% PEJ mix clears the net-return and reserve tests, but requires turnover sign-off; the 36-month estimate produces a 40-point allocation shift, exceeding the 25-point stability stop condition.

## Submission checklist

- [ ] GitHub repository is private and instructional-team access is confirmed.
- [ ] README, decision memo, validation record, and manifest link to the final commit.
- [ ] Student-completed locked prediction was committed before the changed-input run.
- [ ] Partner cold-run receipt above is completed truthfully.
- [ ] `docs/decision-memo.md` and `docs/validation-and-ai-use.md` are attached to Brightspace.
- [ ] Video 1, Video 2, and Video 3 are uploaded as unlisted/public YouTube links with captions.
- [ ] Corrected transcript files are attached or linked: `transcript-video-1.txt`, `transcript-video-2.txt`, `transcript-video-3.txt`.
- [ ] Manifest contains every GitHub location and each video URL.
