# Implementation and cutover status

The operator authorized implementation on 2026-11-15 with “ok - commit - then go on”. The contract clarification was committed as `aee17025e`. The implementation includes fixtures, not a smaller result-only slice. The operator subsequently authorized the bounded live check recorded below; broader paid calibration remains separately authorized.

## Implemented boundary

Gates, type/collection conformance and critique share the declared [review-result](../../types/review-result.md) contract. Workers supply assessment content; code supplies provenance and validates the completed artifact. Exact target and raw-output hashes are distinct from normalized freshness hashes. Current views can be replaced without losing run-owned observations, inputs, completed results or rejection evidence.

The existing review CLI now exposes draft criteria, explicit self-contained operational inputs, observation inspection and single-assessment fixtures. There is no second execution route or legacy-result adapter. Full-pass consumes structured findings as well as report prose. Its approval and publication protections remain; no new procedure combinations are designed here.

Fixtures retain the committed tree, recoverable dirty content, selected inputs, library and executable source. Missing dirty bytes require an exact-hash repair. Creation explicitly selects the current executable as a substitute baseline; source and package-version changes then block trial execution. Independent trials have independent files and Git state, bypass freshness skips and do not publish live results. Resume belongs to the same trial and rejects a changed trial tree.

The initial production adapter is Claude Code, pair grouping and one worker. The fake-harness tests also exercise an installed-project library layout. Dependency artifacts, user-level harness configuration, automatically loaded context and effective tool availability remain declared gaps. Retained content and version checks do not establish environment equivalence or calibrated judgments. Ignored source snapshots enter only through explicitly supplied inputs; there is no recursive operational dependency capture.

## Verification

- Final affected-consumer verification passed **754 tests, with one skipped**, in 210.11 seconds: `general`, `validation`, `sources`, `installation`, `review_workflows`, `relocation`, `headless` and `docs`, with `-m ''` to include slow tests.
- The full suite, including slow tests (`uv run pytest -m ''`), returned 1,505 passed, one skipped and one failure in the tooling SIGINT process-reaping test. Rerunning the complete tooling suite in the foreground passed all 67 tests. The failed full run had been launched as a background shell job; launch context is a possible cause, not an established diagnosis. No review test failed in that invocation, but the full invocation was not green.
- `uv run ruff check .` passed. All 11 edited/new Markdown artifacts passed `commonplace-validate` with zero failures and warnings. `git diff --check` passed. Bare-command help checks exposed the new selectors and fixture interface.
- Implementation changes remain uncommitted. The full-suite log is `/tmp/commonplace-review-unification-tests.log`; the final selected-suite log is `/tmp/commonplace-review-unification-final-tests.log`. No claim of paid judgment calibration follows from these tests.
- No paid model calls or live result regeneration occurred during implementation and cutover. The later operator-authorized live check is recorded below. Authorized archival completed as recorded below.

## Quote matching changed after review

A second session reviewed the uncommitted implementation on 2026-11-15 and changed one rule at the operator's instruction. Passage quotes were matched byte for byte, which rejects a quote written on one line when the target wraps the sentence; roughly 245 of 814 notes in theory, reference and instructions are hard-wrapped. The rule now uses the shared `match_quote` with prose normalization, as the ordinary verbatim-quote check does. A quote identifies a passage and is no longer a byte-exact copy of it; the captured target holds the bytes. After the change, `general`, `review_workflows`, `validation` and `relocation` passed 442 tests and `ruff` passed. The wider selection above was not rerun.

## Live check: acceptance defect remains

After cutover, the operator requested the currently executable review kinds on a long-unchanged note, with one easy catalog gate. Ran `sentence/stock-phrases`, type conformance, collection conformance and critique independently on `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`, using the default Opus profile. Git history shows an October 23 relocation preceded by September 26 edits; the working file was unchanged.

Run: `kb/reports/state/review/runs/v2/20261115T123635Z`. The checkout guard was clean. Collection conformance completed with WARN: the note presents illustrative origin cases as support for generality, and two `evidenced-by` phrases do not state a risky test or qualifying/bounding role. These are review findings, not accepted edits.

The other three assessments delivered output but exhausted validation attempts with `[base] missing pinned criterion: /home/zby/llm/commonplace/kb/reports/COLLECTION.md`. Their outputs are retained but are not accepted review results. This exposes a controller-side captured-validation dependency defect missed by fake-harness coverage; the exact cause and repair remain open. No further calls were made after the sweep returned. Seven actual model launches reported a total cost of $2.584259, all using `claude-opus-5-5`; replayed rejections were not extra launches. Do not treat deterministic test success above as live acceptance of all four review kinds. Repair and exercise the retained outputs without new model calls before another live trial.

## Completed cutover

The preflight receipt is `kb/reports/state/review/cutover/20261115-preflight/inventory.json`. The completed cutover receipt is `kb/reports/state/review/cutover/20261115-v2/receipt.json`. Immediately before archival, all 4,725 historical file hashes still matched preflight, no review controller or recorded worker remained live, and all 153 run locks were acquired and held through the move and integrity check.

| Check | Finding |
|---|---|
| Active current results | 132 Markdown files; the earlier 136 count included four directories ending in `.md` |
| Historical runs | 150 gate sweeps, two revisions, one full pass |
| Recorded requests | 613 request versions with attempts; all eventually delivered; one earlier incomplete attempt was retried successfully |
| Process/lock check | 153 locks checked and none held; no recorded worker PID or review controller remained live |
| Revisions | Both publication manifests have exact captured approvals, and both live artifacts match their final hashes |
| Full pass | Current packet is `alternative-applied`; deletion was already authorized and resolved |
| Gate sweeps | No record of the complete requested selection or whole-sweep completion; delivered calls cannot establish that no unstarted work remained |

The operator authorized cleanup with “yes - do the cleanup”, abandoning any unfinished remainder of the 150 historical gate sweeps. This is abandonment, not an inference that every sweep completed.

Archived all 132 old current results and the one current packet under `kb/reports/state/review/archive/20261115-v1/`. Historical runs remain at their original paths, outside active discovery and resume. All 4,725 inventoried files passed the post-move byte-hash check. The active results and packets trees are empty, and new runs use `kb/reports/state/review/runs/v2/`. No historical answer or approval carries into new work; results regenerate only on demand.
