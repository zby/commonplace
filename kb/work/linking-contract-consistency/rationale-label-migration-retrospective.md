# Rationale label migration retrospective

Status: pending

Capture surprises when discovered. This is the second directional-label run and must test whether the evidence migration's procedure generalizes.

## Decision gate

- Live source→destination inventory: 134 active `rationale` edges and 310 active `grounds` edges. `rationale` pairs are reference→notes 95, reference→reference 16, agentic-systems→notes 9, agent-memory-systems→notes 5, instructions→notes 5, notes→reference 2, sources→notes 1, and types→notes 1. `grounds` has 272 note→note edges and 38 off-pattern edges.
- Neighboring-label findings: the rationale corpus splits into 114 rationale dependencies, 2 evidence edges, and 18 navigation/architecture edges. The grounds cohort has 38 off-pattern edges and only two files author both labels.
- Adopted identifier and assertion template, or reason migration stopped: `source rests-on target` is accepted for the 114 rationale-dependency edges and 8 off-pattern grounds edges. The boundary adjudication assigns the other 50 boundary rows to `evidenced-by` (35), `is-evidence-for` (12), `implements` (2), or `compares-with` (1), with no removals. The 272 note→note `grounds` rows remain a distinct deferred cohort.

## Baseline and exclusions

- Positive mutable surface: active registered footer edges in non-generated Markdown under notes, reference (excluding proposal archive), instructions, agent-memory-systems, agentic-systems, sources analyses/ingests, and types; both ordinary and bold footer forms were parsed.
- Exclusion buckets and counts: 1,660 generated-report rows, 181 inactive-workshop-history rows, and 10 archived-proposal rows. No active row came from an immutable snapshot or separately classified frozen experiment/calibration artifact; ordinary prose and historical quotations were not registered edges.
- Authorization gaps: 19 rationale rows are outside an authorized collection pairing or have no collection contract; 38 grounds rows are off the intended note→note pairing or unregistered on the type surface.
- Guidance-only occurrences: ADR 020, ADR 058, ADR 019, the shared catalogue, collection contracts, and `cp-skill-write`/`cp-skill-connect` were read as guidance. No guidance or corpus surface was edited.

## Surprises

- **Expected: one coherent renameable rationale relation.** **Observed:** 114 R edges, 2 E edges, and 18 N edges. **Why it mattered:** a lexical rename would convert evidence and architecture/history into false design dependencies. **Local resolution:** classify before naming; defer migration of E/N rows. **Reusable lesson:** tuple inventory and semantic disposition must precede any directional-label edit. **Deferred owner:** maintainer in the migration run.
- **Expected: the current label boundary would be visible in authorization.** **Observed:** 38 active `grounds` edges are outside note→note, including 15 external citations, 9 source→note evidence mappings, and 6 reference→note cross-register cases. **Why it mattered:** authorized labels are hypotheses, not semantic evidence, and off-contract rows carry the highest information about drift. **Local resolution:** record authorization gaps separately and do not widen contracts during evaluation. **Reusable lesson:** compare every disposition against both resolved destination and source collection. **Deferred owner:** vocabulary/contract migration maintainer.
- **Expected: same-file use of both labels would reveal a stable distinction.** **Observed:** only `kb/reference/tag-readme-trace-as-self-improving-loop.md` and `kb/types/type-spec.md` use both, and their local contexts mostly restate “why/basis.” **Why it mattered:** the cases expose uncontrolled synonymy at the cross-register boundary without invalidating the larger note→note grounds cohort. **Local resolution:** treat the two files as reclassification cases. **Reusable lesson:** same-file co-occurrence is a high-information drift test, not a reason to merge by count. **Deferred owner:** migration maintainer.
- **Expected: the N and off-pattern buckets would require removals or new vocabulary.** **Observed:** all 58 boundary edges retain an articulated reader need and fit five existing or already-selected relations; the real residue is three authorization-surface decisions. **Why it mattered:** semantic cleanup can remain conservative without preserving overloaded labels or inventing synonyms. **Local resolution:** record exact successor dispositions and authorization deltas in the boundary adjudication. **Reusable lesson:** after coarse classification, run a second pass that must choose an existing assertion or removal for every tuple before contracts change. **Deferred owner:** migration maintainer.

## Edge reconciliation

Record migrated, reclassified, removed, and intentionally excluded counts. Reconcile normalized source/title/target/context tuples against the baseline.

## Verification friction

- Checks that caught a real issue: the bold-footer-aware temporary TSV exposed six active source-analysis edges omitted by the first parser; resolved-target classification exposed all 38 off-pattern grounds rows and the 19 rationale authorization gaps.
- Checks that produced noise: generated reports and workshop histories dominated raw lexical counts, confirming that repository-wide replacement sets are not a usable baseline.
- Unsafe manual step or missing check: the temporary parser still needs a shared fixture for nested Markdown link syntax before becoming reusable; no migration was attempted here.
- Automation worth retaining: the evidence-run pattern of a temporary, disposition-bearing TSV plus tuple reconciliation is reusable; the label-specific semantic classifier should remain review-owned.

## Procedure promotion decision

Compare this run with the evidence retrospective. State which steps repeated, which remained label-specific, and explicitly accept or reject extracting the stable core into a reusable instruction.

## Completion

- Validation and tests:
- Migration commits:
- Deferred follow-ups:
