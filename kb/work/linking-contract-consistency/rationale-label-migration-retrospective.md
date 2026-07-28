# Rationale label migration retrospective

Status: complete

Capture surprises when discovered. This is the second directional-label run and must test whether the evidence migration's procedure generalizes.

## Decision gate

- Live source→destination inventory: implementation-time rebaseline found 134 active `rationale` edges and 314 active `grounds` edges. `rationale` pairs remained reference→notes 95, reference→reference 16, agentic-systems→notes 9, agent-memory-systems→notes 5, instructions→notes 5, notes→reference 2, sources→notes 1, and types→notes 1. `grounds` had 276 note→note edges and the same 38 off-pattern edges; four canonical rows landed after the 310-edge semantic review.
- Neighboring-label findings: the rationale corpus splits into 114 rationale dependencies, 2 evidence edges, and 18 navigation/architecture edges. The grounds cohort has 38 off-pattern edges and only two files author both labels.
- Adopted identifier and assertion template: ADR 060 adopts `source rests-on target` for the 114 rationale-dependency edges and 8 off-pattern grounds edges. The other 50 boundary rows became `evidenced-by` (35), `is-evidence-for` (12), `implements` (2), or `compares-with` (1), with no removals. The 276 note→note `grounds` rows remain a distinct deferred cohort.

## Baseline and exclusions

- Positive mutable surface: active registered footer edges in non-generated Markdown under notes, reference (excluding proposal archive), instructions, agent-memory-systems, agentic-systems, sources analyses/ingests, and types; both ordinary and bold footer forms were parsed.
- Exclusion buckets and counts at implementation rebaseline: 1,674 generated-report rows, 181 inactive-workshop-history rows, and 10 archived-proposal rows across the two old labels. No active row came from an immutable snapshot; ordinary prose and historical quotations were not registered edges. After migration, the 57 surviving `rationale` rows are generated reports 45, archived proposals 9, and workshop history 3; all surviving `grounds` rows are the 276 active canonical cohort or an unchanged exclusion.
- Authorization gaps: the migration replaces `rationale` with `rests-on` in each affected source collection, adds `is-evidence-for` for agentic-systems→notes and sources→agent-memory, and gives `kb/types/` its own `COLLECTION.md`. No contract is widened to authorize off-pattern `grounds`.
- Guidance-only occurrences: ADRs 019/020/058, the catalogue, collection contracts, proposal guidance, current theory vocabulary, and the write/connect consumption path were reconciled. Historical ADR discussion retains the retired identifier explicitly as history.

## Surprises

- **Expected: one coherent renameable rationale relation.** **Observed:** 114 R edges, 2 E edges, and 18 N edges. **Why it mattered:** a lexical rename would convert evidence and architecture/history into false design dependencies. **Local resolution:** classify before naming; defer migration of E/N rows. **Reusable lesson:** tuple inventory and semantic disposition must precede any directional-label edit. **Deferred owner:** maintainer in the migration run.
- **Expected: the current label boundary would be visible in authorization.** **Observed:** 38 active `grounds` edges are outside note→note, including 15 external citations, 9 source→note evidence mappings, and 6 reference→note cross-register cases. **Why it mattered:** authorized labels are hypotheses, not semantic evidence, and off-contract rows carry the highest information about drift. **Local resolution:** record authorization gaps separately and do not widen contracts during evaluation. **Reusable lesson:** compare every disposition against both resolved destination and source collection. **Deferred owner:** vocabulary/contract migration maintainer.
- **Expected: same-file use of both labels would reveal a stable distinction.** **Observed:** only `kb/reference/tag-readme-trace-as-self-improving-loop.md` and `kb/types/type-spec.md` use both, and their local contexts mostly restate “why/basis.” **Why it mattered:** the cases expose uncontrolled synonymy at the cross-register boundary without invalidating the larger note→note grounds cohort. **Local resolution:** treat the two files as reclassification cases. **Reusable lesson:** same-file co-occurrence is a high-information drift test, not a reason to merge by count. **Deferred owner:** migration maintainer.
- **Expected: the N and off-pattern buckets would require removals or new vocabulary.** **Observed:** all 58 boundary edges retain an articulated reader need and fit five existing or already-selected relations; the real residue is three authorization-surface decisions. **Why it mattered:** semantic cleanup can remain conservative without preserving overloaded labels or inventing synonyms. **Local resolution:** record exact successor dispositions and authorization deltas in the boundary adjudication. **Reusable lesson:** after coarse classification, run a second pass that must choose an existing assertion or removal for every tuple before contracts change. **Deferred owner:** migration maintainer.
- **Expected: the reviewed 310-edge grounds baseline would still be current.** **Observed:** four new canonical note→note `grounds` edges landed before implementation, raising the active cohort to 314 without changing the 38-edge off-pattern boundary. **Why it mattered:** blindly conserving 272 deferred tuples would have omitted live edges even though the adjudicated edits were still correct. **Local resolution:** rebuild the baseline, classify the four rows as canonical, and defer 276 tuples. **Reusable lesson:** rebaseline after concurrent sessions and immediately before mutation; review-time counts are evidence, not an execution lock. **Deferred owner:** none.
- **Expected: the global type surface could receive three migrated links without changing collection topology.** **Observed:** `kb/types/` authored real links but had no `COLLECTION.md`, so any label remained outside collection-owned authorization. **Why it mattered:** borrowing the reference contract or self-authorizing through the root type would preserve a structural exception. **Local resolution:** ADR 060 makes `kb/types/` a collection with a minimal text/link contract while keeping type semantics type-owned. **Reusable lesson:** when a positive mutable surface lies outside the authorization topology, resolve the ownership gap rather than treating it as a label exception. **Deferred owner:** none.
- **Expected: the batch edit's final count check would confirm its own writes.** **Observed:** all 172 edits applied, then a typo in the script's expected-count expression produced a failure after mutation. **Why it mattered:** retrying the mutator would have been unsafe and its failure could not attest rollback. **Local resolution:** stop, report the partial state, and run a separate read-only reconciliation that found the exact expected distribution. **Reusable lesson:** mutation and verification must be separate phases; a post-write failure always triggers independent state inspection before any rerun. **Deferred owner:** the promoted procedure records this rule.

## Edge reconciliation

- Migrated old `rationale`: 114 → `rests-on`; 15 → `evidenced-by`; 2 → `is-evidence-for`; 2 → `implements`; 1 → `compares-with`; 0 removed. Total 134.
- Reclassified off-pattern `grounds`: 8 → `rests-on`; 20 → `evidenced-by`; 10 → `is-evidence-for`; 0 removed. Total 38.
- Deferred active `grounds`: 276 note→note tuples, unchanged.
- Final active old labels: `rationale` 0; `grounds` 276, all notes→notes.
- Final active `rests-on`: 123 — 122 conserved migrated tuples plus one new edge authored by ADR 060 and accounted separately.
- Excluded old labels remain untouched in generated reports, archived proposals, and workshop history. Reciprocal edges were not part of the mutation set.

## Verification friction

- Checks that caught a real issue: the bold-footer-aware temporary TSV exposed six active source-analysis edges omitted by the first parser; resolved-target classification exposed all 38 off-pattern grounds rows and the 19 rationale authorization gaps.
- Checks that produced noise: generated reports and workshop histories dominated raw lexical counts, confirming that repository-wide replacement sets are not a usable baseline.
- Unsafe manual step or missing check: the temporary parser still needs fixtures for nested Markdown targets and link-like prose before it could become a reusable command. The batch mutator combined writing with a final assertion, so its assertion typo surfaced only after files changed.
- Automation worth retaining: a temporary disposition-bearing TSV, mutually exclusive exclusion buckets, and an independent read-only post-migration reconciliation. The label-specific semantic classifier and one-off corpus parser remain review-owned rather than promoted as code.

## Procedure promotion decision

**Accept promotion.** Both evidence and rationale runs repeated the same stable core: fresh positive-surface inventory, exclusive exclusions, resolved source/destination authorization comparison, complete semantic disposition before edits, coordinated decision/catalogue/contract/guidance changes, exact tuple mutation, independent old-label and tuple reconciliation, validation, and surprise capture. The promoted [directional-label migration instruction](../../instructions/migrate-directional-link-label.md) records that core.

The successor assertion, neighboring-label comparisons, corpus classification, and authorization decisions remained label-specific and are deliberately excluded. Parser code also remains unpromoted until real fixtures establish one stable registered-edge grammar.

## Completion

- Validation and tests: affected library collections and each changed workshop artifact validated with no failures. The sources collection retained its unrelated pre-existing missing-distillation-link warnings. `pytest`: 486 passed, 1 unrelated pre-existing redirect-map target failure (`a-decomposition-earns-explanatory-reach-by-derivation-or-inheritance.md`). Independent tuple, exclusion, deferred-cohort, authorization-pair, and `git diff --check` checks passed.
- Migration commits: pending maintainer request.
- Deferred follow-ups: evaluate and migrate the 276 canonical note→note `grounds` edges; add parser fixtures before promoting a reusable corpus command; repair the unrelated redirect target under its owning work.
