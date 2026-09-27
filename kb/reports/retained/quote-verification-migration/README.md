# Quote verification migration acceptance record

Dated observation: 2026-09-27. Retained for auditing the corpus conversion and
citation repairs implementing [ADR 094](../../../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md).
The report records this migration's acceptance evidence; it is not a live
validation dashboard. GPT-6 inspected ambiguous occurrences under the operator's
approved quote-migration plan and the repository's collection contracts.

## Result and scope

The migration converted 158 ingests from 822 list items to 820 attributed
blocks. Every surviving extract retained its quoted bytes, including multiline
passages. Two exact duplicate extracts were removed under explicit operator
authorization; distinct locator information was preserved. Six repeated source
passages received ranges selected from their section or table context.

All 806 checkable retained extracts match their pinned snapshots. Fourteen
extracts in three ingests remain explicitly unverified because their local
snapshots were already missing: AlphaDev, automated refinement of Horn-clause
domain theories, and explanation-based generalization. This was an approved
exception. The ten emphasis-dependent matches were paper prose; all repository
extracts passed whitespace-only matching.

The citing-artifact comparison covers 291 files. All 52 real prose quotations
match after migration. Two citations needed longer excerpts to distinguish
overlapping retained passages; their claims did not change. Two raw-parser
mismatches in the graph-loader workshop and an unresolved inline example in the
articles contract are explanatory examples outside standing quote validation.

The analysis sweep checked 159 retained and local artifacts. All 3,613 quotes
in its 120 current-run artifacts pass. A separate sweep of all 40 current
review projections passes; 8 of these contain 13 quoted passages. The migration
corrected 163 result/specialist citations and two review citations across 15
current runs. Selection reasons and citation-only dispositions are recorded
per edit. One JSONL excerpt includes more surrounding text because two copies
occur on the same source line. No analysed-system claim changed.

The operator authorized synchronizing current-run local copies and dependent
hashes. Retained/local results now agree for all 15 affected runs; specialist
report pins, generated-review pins, run-state receipts, and affected live
comparison-table hashes agree. Two original paper captures were recovered
exactly by reversing an earlier type-path change in separate current-run
copies; their recorded checksums and source identities are unchanged. The
current ingest snapshots were not edited.

Superseded and unreferenced runs remain unchanged: 15 of 39 audited artifacts
have 40 quote diagnostics. Frozen comparison exports remain historical
observations. The collection `kb/agent-memory-systems/` was excluded because
the operator plans to decommission it; this migration did not edit its quotes.

## Checks and practical limits

The full Python suite passes: 899 tests. The publication trial rejects a
specialist quotation whose valid, in-bounds range points elsewhere, then
publishes after returning to the original unranged citations. This is a
controlled fixture, not a new external-system analysis.

Validation of the initial 167 edited KB documents reported zero failures and
nine pre-existing warnings. The installation probe confirmed that fresh
projects receive the new quote contract, existing ingests remain untouched by
initialization, converted ingests validate, and a second initialization is
byte-idempotent. Redirect validation passes after proposal archival.

Broader validation of the affected completed analysis runs still reports
pre-existing comparison-schema errors in 13 runs and missing links to the
retired conjectural-learning definition in some reviews. Their comparison
content and these links were not changed by citation repair. They are outside
this quote migration; the exact diagnostics are retained below. No remaining
current-run diagnostic concerns quote matching or affected byte identities.

Matching establishes occurrence under the selected normalization, not source
truth or semantic support. Repeating the source checks requires the original
Git objects or local captures; the records below remain readable without them.

## Evidence

- [Ingest and citing-artifact comparison](./ingest-comparison.json): before/after outcomes, removed duplicates, selected ranges, and citation-only edits.
- [Emphasis cases](./emphasis-cases.json): the ten inspected paper extracts.
- [Initial analysis sweep](./analysis-sweep.json) and [final sweep](./analysis-sweep-final.json): all retained/local results and specialist reports, including the excluded superseded cases.
- [Citation repairs and hashes](./analysis-repairs.json): original and replacement citations, selected occurrences, reasons, recovered captures, and final dependent hashes.
- [Review-projection sweep](./review-sweep.json): current generated reviews after repair.
- [Completed-run validation](./analysis-integrity.json): identity-check passes and the broader pre-existing schema/link diagnostics.
- [Acceptance summary](./acceptance.json) and [initial document validation](./document-validation.json): test counts and exact validator diagnostics.
- [Installation probe](./install-probe.json): fresh and existing project observations.
- [Contract consumer inventory](./contract-change-packet.md): the consumers checked during implementation.

## Cleanup

The adopted proposal is archived, its public URL redirects to ADR 094, and
historical ADRs point to the amended contract. The output-document redesign
workshop records that it must preserve the corrected citations. Temporary
migration tooling and the completed quote-migration workshop were removed;
current-run state, source captures, and unrelated checkout changes were kept.
