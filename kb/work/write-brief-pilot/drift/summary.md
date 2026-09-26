# Drift study — summary

Observational trace of each commission item (`rubric/<n>.md`) from the commissioned version (`incumbents/<n>.md`) to the target at HEAD `6d6bf90e` (2026-09-26). Per-item evidence is in `drift/<n>.md`. Traced by one fresh Opus agent; counts retallied from the per-item lines.

Status meanings: *realized* = the commissioned version realizes the item; of those, *survived*, *weakened* (partly kept), or *removed* at HEAD. *Recorded* = a commit body, ADR, or workshop record states the change or its reason; *unrecorded* = none found.

| # | Items | Not realized | Realized | Survived | Weakened rec. | Weakened unrec. | Removed rec. | Removed unrec. | Unplaced |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 46 | 1 | 45 | 45 | 0 | 0 | 0 | 0 | 0 |
| 2 | 32 | 0 | 32 | 32 | 0 | 0 | 0 | 0 | 0 |
| 3 | 41 | 0 | 41 | 41 | 0 | 0 | 0 | 0 | 0 |
| 4 | 27 | 7 | 20 | 8 | 4 | 0 | 8 | 0 | 0 |
| 5 | 24 | 0 | 24 | 7 | 0 | 13 | 0 | 4 | 0 |
| 6 | 61 | 9 | 52 | 49 | 0 | 1 | 2 | 0 | 0 |
| 7 | 48 | 1 | 47 | 47 | 0 | 0 | 0 | 0 | 0 |
| 8 | 28 | 5 | 23 | 13 | 2 | 2 | 4 | 2 | 0 |
| 9 | 23 | 1 | 22 | 14 | 5 | 1 | 2 | 0 | 0 |
| 10 | 48 | 4 | 44 | 11 | 13 | 5 | 7 | 8 | 0 |
| **Total** | **378** | **28** | **350** | **267** | **24** | **22** | **23** | **14** | **0** |

Of 350 realized items, 83 (24%) were lost in whole or part: 47 by a recorded change and 36 without a record. Without target 5, where every loss comes from one unrecorded non-promotion event rather than from edits, the figures are 59 lost, 47 recorded and 19 unrecorded.

The "not realized" counts here (28) differ from the `(absent)` labels in `recoverability/` (19) because the two passes applied the realization test independently; the experiment uses the `recoverability/` labels.

## Reading

- **Losses are concentrated.** Five targets (1, 2, 3, 6, 7) lost at most three items between them: their bodies are unchanged or changed only by additions and fixes. All losses on targets 4, 5, 8, 9, and 10 come from one or two whole-document events: a PR that reframed the portfolio (4, `2b406eea`), non-promotion of the accepted candidate (5, `c7484bea`), replacement of the lead article (8, `9670ede7`), a compact-rewrite plan and its execution (9, `21dd6f0a`/`ee1b6481`), and a rewrite around needs followed by a split into child notes (10, `5ec49c50`/`1f17e1e6`).
- **Recorded changes lose more than they state.** Where a loss is recorded, the record usually names the overall change (retire the portfolio, rewrite to about 1,200 words, split into notes) rather than the individual items. Unrecorded losses are mostly items dropped along with a recorded one: the same rewrite drops more than its stated reason covers (8: the "no run exists" statement; 9: the mention of Commonplace; 10: the session-log/ADR complementarity).
- **Target 5 is a different kind of loss.** Nothing was edited out. The accepted candidate was never promoted, and the closing commit does not record the decision that the workshop's closure contract required.

## Most informative individual losses

1. **Target 8, item 12, removed, unrecorded (`9670ede7`).** The article said "No test has been run"; after the lead article was replaced, it ends on "We think the answer is yes." The commit's list of dropped sections does not mention this.
2. **Target 10, items 27–29, removed, unrecorded (`5ec49c50`, no commit body).** The session-log/ADR pairing and the bridge between them went in the rewrite around needs. A critique committed the day before gives a reason for dropping the four layers, but nothing covers these items.
3. **Target 4, item 6, removed, recorded (`2b406eea`).** The commissioned row was dropped when the portfolio framing was retired as a whole. This is the clearest case where a retained brief would have gone stale rather than caught silent drift.

## Adjudication flags for the operator

- **Target 4, what counts as recorded.** The record names retiring the portfolio, not the row the commission added. Counted as recorded.
- **Target 10, two recording rules.** (a) Items counted as recorded when a critique committed before the change proposed it (`b0e5d3f5`), although the critique asked to weaken the layers and the rewrite removed them. (b) Items counted as recorded when `1f17e1e6` relocated them into child notes, with only the subject line "Split agent memory requirements into notes" as the record.
- **Target 8, item 13.** Close call, marked weakened and recorded (`43ea2b36`).
- **Target 6, a reversed silent drift.** `6b550e26` briefly broke item 56 and `281532ed` restored it with a record. Counts as survived.
- **Target 8, blinding.** The tracing agent saw line 1 of `briefs/8.md` by accident while grepping and reports it did not use it. The drift study is not an experimental arm, so this does not affect the runs.
