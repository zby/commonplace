# Evidence label migration retrospective

Status: complete

Fill this during the migration, not from memory afterward. The purpose is to improve the next directional-label migration rather than narrate routine execution.

## Baseline

- Starting revision: `37676a521b422c366a428ca707f223a77dd648a2`
- Active registered `evidence` edges: **207** across 102 mutable authored files. The source→destination inventory was: notes→agent-memory 17, notes→agentic 10, notes→external 23, notes→notes 8, notes→reference 30, notes→sources 71, notes→types 2; reference→reference 8, reference→sources 3; agent-memory→notes 2, agent-memory→sources 1; sources→notes 24; current workshop→agent-memory 1, →agentic 1, →notes 2, →sources 1, and →local workshop sources/artifacts 3.
- Expected `evidenced-by`: **181**. This is every active edge except the established source/review→claim inverse cohort.
- Expected `is-evidence-for`: **26**: 24 source ingest/review→note edges plus 2 Fintool review→note edges. Live bytes agree with the earlier inverse-cohort review.
- Ambiguous before editing: **0 semantic cases**. Forty-one library edges were semantically clear but absent from their collection's destination table (notes→external 23, notes→notes 8, notes→types 2, reference→reference 8), and the two dialectical-sample citations had a clear claim→source meaning but no declared footer-label grammar. These are authorization gaps, not reasons to force a different relation.
- Intentionally excluded surfaces and why: **488 exact old-label footers** — 429 in generated/ignored `kb/reports/`; 24 frozen candidate/history artifacts under the auditable-editing experiment; 31 frozen calibration items under `kb/work/error-catching/run-01/`; and 4 in an unindexed dated agent-memory workshop draft retained as historical work. Immutable source snapshots contributed no matching authored footer edges. Archived proposals, historical ADR wording, quotations, and ordinary prose uses of “evidence” are also excluded from rewriting, but were searched for false current guidance.

The inventory counted only footer edges matching a Markdown link followed by `— evidence:` or legacy `-- evidence:`. Reconciliation uses the same query and exclusion set, so every baseline row retains its source file, line-local target, and source→destination class without treating ordinary prose as an edge.

## Surprises

For each surprise, record:

### Live authorization lag was much larger than the inverse cohort

- **Expected:** The principal semantic split would be the already-reviewed 26 inverse edges, with existing collection tables otherwise covering the forward cohort.
- **Observed:** Forty-one live library edges used the label on source→destination pairs omitted from their collection tables; the dialectical sample also used footer syntax without declaring it.
- **Why it mattered:** Renaming only the listed contract pairs would leave the migrated corpus off-authorization and would make a passing lexical migration look complete when writers still lacked a rule for those edges.
- **Local resolution:** Treat source-as-subject meaning as the semantic classifier, record the gaps separately from ambiguity, and extend only the affected evidence-pair destinations while leaving neighboring labels and general collection grammar alone.
- **Reusable lesson:** Baseline by actual source→resolved-target pairs before editing contracts; authorization matrices are hypotheses about the corpus, not inventories of it.
- **Deferred owner, if any:** The broader enforcement gap remains owned by this workshop's validator-boundary thread; this migration only reconciles the concrete pair it changes.

### Recommendation prose was a migration surface

- **Expected:** Contracts, the catalogue, authoring examples, and registered footers would contain the current guidance that could recreate the retired label.
- **Observed:** Thirty-two active source ingests also named `evidence` in recommendations for future edges. They were not registered edges, but leaving them unchanged would instruct a later writer to restore the old identifier.
- **Why it mattered:** Edge conservation alone could pass while the KB's queued work still targeted the retired vocabulary.
- **Local resolution:** Re-read each recommendation from its stated authoring direction: note→snapshot recommendations became `evidenced-by`; source-analysis→claim recommendations became `is-evidence-for`.
- **Reusable lesson:** Search imperative and recommendation prose for literal identifiers after the structural inventory; treat it as a separate guidance surface, not as an edge count.
- **Deferred owner, if any:** None.

### Excluded history dominated the raw lexical count

- **Expected:** Exclusions would be a small tail around the active authored corpus.
- **Observed:** The raw query found 695 exact old-label footers, of which 488 were generated reports, frozen experiment/calibration artifacts, or historical workshop work; only 207 were active migration targets.
- **Why it mattered:** A repository-wide replacement would have rewritten evidence and made old assay/experiment outputs cease to represent what was actually reviewed.
- **Local resolution:** Define path-level exclusion predicates before editing, report both raw and active counts, and prove that every surviving old footer falls in exactly one recorded exclusion bucket.
- **Reusable lesson:** Every label migration needs a positive mutable-surface definition and a mutually exclusive exclusion reconciliation, not only ignored globs in the rewrite command.
- **Deferred owner, if any:** None.

## Edge reconciliation

| disposition | count | notes |
|---|---:|---|
| migrated to `evidenced-by` | 181 | Same source, target, title, context phrase, and edge presence as baseline. |
| migrated to `is-evidence-for` | 26 | The 24 source ingest/review→note and 2 Fintool review→note edges from the established inverse cohort. |
| reclassified to another label | 0 | Every active edge honestly fit one assertion in the pair. |
| removed after semantic review | 0 | No edge failed both assertion templates. |
| intentionally excluded | 488 | 429 generated reports, 24 frozen editing candidates/history, 31 frozen calibration items, and 4 historical draft footers. |

The 207-edge active baseline equals 181 + 26 exactly. The 488 excluded footers are reported separately and are not part of that active baseline. A conservation comparison against `HEAD` found zero missing and zero unexpected source/title/target/context tuples, so reciprocal edge presence is unchanged.

## Verification friction

- Checks that caught a real issue: resolving actual target paths by source collection exposed 41 live library authorization gaps and the dialectical sample's undeclared footer grammar; a post-edit phrase scan caught grammatically awkward prose produced by identifier substitution.
- Checks that produced noise: repository-wide old-footer search returned 488 intentionally immutable/frozen/generated hits; useful for reconciliation, unsafe as a rewrite set. Collection-wide validation was verbose but clean.
- Missing check or unsafe manual step: `commonplace-validate` checks link resolution but does not enforce source→destination label authorization or source-as-subject semantics. This remains the [validator-boundary question](./README.md#deterministic-validation-checks-link-existence-not-link-contracts). Prose recommendation direction still required judgment.
- Reusable query or automation worth retaining: parse only Markdown links followed by `— <label>:` or legacy `-- <label>:`, resolve each local target, emit source/destination pairs plus exclusion reason, and compare normalized `(source file, link title, target, context phrase)` tuples before/after. The migration's one-shot check proved 207/207 conservation, zero wrong dispositions, zero broken targets, and zero active old footers.

## Amend the next label plan

Write executable changes, not general advice.

- **Add:** Require the next plan to declare positive mutable surfaces and named exclusion buckets; inventory actual resolved source→destination pairs; diff those pairs against collection authorization; and scan active recommendation/procedure prose for the literal identifier after edge inventory.
- **Remove:** Do not use collection matrices or prior review counts as the baseline, and do not treat a repository-wide lexical replacement set as the authored corpus.
- **Reorder:** Resolve and classify live edges first; record authorization deltas and exclusions in the retrospective; adopt the ADR/catalogue/contracts; reconcile prose guidance; migrate edges; then run tuple-conservation, old-label-exclusion, authorization, link, and validation checks in that order.
- **Automate:** For the next run, generate a temporary TSV with source path, target, resolved destination, proposed disposition, and exclusion reason, then make the post-run checker fail on a missing/unexpected tuple, an active old label, or a surviving old label outside exactly one exclusion bucket. Do not promote it to a reusable command until a second migration confirms the shape.
- **Keep label-specific:** Semantic assertion templates, inverse-journey review, neighboring-label boundaries, and evidence's target-uptake distinction remain label-specific judgment rather than generic migration mechanics.

The next label plan must explicitly accept or reject each item above.

The authorization/exclusion/recommendation findings generalize to other directional labels. The need for a separate `is-evidence-for` relation that does not assert target-side uptake, and the exact boundary around corroborating, qualifying, and boundary evidence, are evidence-specific.

## Completion

- Final validation/tests: `commonplace-validate` passed the `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems` scopes; the changed instruction and workshop files passed individually. One unchanged overlong-description warning remains on the chatbot-goal-state workshop note. No migration code or test fixture changed; the full integration suite nevertheless passed (`487 passed`). `git diff --check`, tuple conservation, old-label exclusion reconciliation, and local-target resolution passed.
- Migration commit: this migration's `Migrate directional evidence labels` commit.
- Deferred follow-ups: migrate the other source-as-subject failures listed in [directional label grammar](./directional-label-grammar.md); decide enforcement in the [validator-boundary thread](./README.md#deterministic-validation-checks-link-existence-not-link-contracts). Neither was expanded here.
- Candidate reusable procedure after another run: baseline/exclusion TSV → semantic disposition → coordinated ADR/catalogue/contracts → guidance scan → corpus rewrite → tuple/exclusion/authorization/validation reconciliation.
