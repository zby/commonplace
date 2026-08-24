# Claim-grounding rollout

## What this is

Retrospective application of [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
across the existing corpus. The prospective rule ships — a note that newly leans
on a named source cannot be saved until the claim is grounded in that source's
ingest — but every note written before it is unaffected. This workshop grounds
those.

Split out of [literature-disposition](../literature-disposition/README.md) on
2026-08-24, where it had been placed by momentum. The populations barely touch:
of 29 notes in the rollout cohorts, **one** is in that workshop's diagnosed
cohort. The rollout's population is selected by citation graph — every note that
links an ingest — not by any suspicion that a note restates outside literature.

## Governing question

For each claim a note draws from a source it cites: does the source actually
support it, and at what scope?

That is claim-level and evidential. What should then *happen to the note* — retire,
thin, rewrite around its delta, leave — is
[literature-disposition](../literature-disposition/README.md)'s question, and
this workshop feeds it rather than answering it. A `literature handoff`
disposition is the seam.

## Scale

68 notes cite an ingest; 94 distinct ingests are cited; 192 of 286 ingests are
cited by nobody and **are not a queue**. Claims are pulled on demand, so an
uncited ingest needs none.

Cohort 01 covers two notes; cohorts 02–07 cover another 29. After excluding
those assigned targets and recomputing the graph, 37 notes remain in four
components: 18 notes / 36 ingests, 15 / 20, 2 / 1, and 2 / 1. Cohort 08 combines
the two disconnected two-note components; cohorts 09 and 10 own the 15- and
18-note components respectively.

## Concurrency

Two conflict axes, and both bind. Concurrent agents must not append to the same
ingest's `Claims` section — V1 ships no locking, deliberately — and must not edit
the same note during repair. So the safe unit is a connected component of the
note-to-ingest graph.

Cohorts 02–07 were mutually disjoint on both axes by construction. Cohorts
08–10 are likewise mutually disjoint on both axes and can run concurrently with
one mutation owner per cohort. Do not hand-assemble a cohort without rechecking
disjointness against every cohort running at the same time.

The original 36-note component is no longer the execution unit. Three of its
notes were worked in cohort 02; removing already assigned targets fractures the
residual graph. The new cohorts preserve connected-component ownership instead
of adding locks, claim IDs, or concurrent ingest mutation. Each large-cohort
prompt imposes a complete source-blind inventory barrier before grounding and a
grounding barrier before target repair.

## Snapshot-pair repair — 2026-08-24

All seven cited ingests that lacked an exact name-paired snapshot at the corpus
freeze now have one in the working snapshot cache. Cohort 02 repaired the first
two pairs. The remaining five expected byte streams were already present under
adapter-derived names; each matched its ingest's recorded SHA-256 and canonical
source. They were moved to the ingest-derived Markdown path without changing
their bytes, and the two X capture companions were moved with them. All five
affected ingests validate; two retain only their pre-existing missing-
`distillation.md` link warnings.

This removes the snapshot-identity blocker. It does not ground the two Palantir
claim uses left by cohort 06 or any claims in the unworked corpus.

## What closes this workshop

1. Every cohort has a completion record where each claim use carries a terminal
   disposition or a named blocker.
2. Cohorts 08–10 are worked or have a recorded decision not to work them, with
   the reason.
3. The design evidence is reported: whether whole-section reading held without
   claim IDs, whether duplicate or disputed entries accumulated, and whether any
   cohort produced pressure for reconciliation. ADR 073 shipped no identity
   machinery on the strength of a two-entry run; these cohorts are its first real
   test, and a finding that the decision needs revisiting is a result, not a
   failure.
4. Blocked ingests are re-ingested or recorded as unavailable.

## Files

- [Procedure](./procedure.md) — the six steps, the corpus state at freeze, and
  the shared execution routes every cohort inherits
- [Cohort 01](./cohort-01.md) — the claim-pull rollout's own run, reconstructed
  after being deleted with its completion table unfilled. Six narrowed, two
  contradicted, **zero grounded as written**
- Cohorts [02](./cohort-02.md) · [03](./cohort-03.md) · [04](./cohort-04.md) ·
  [05](./cohort-05.md) · [06](./cohort-06.md) · [07](./cohort-07.md) — frozen
  manifests, with a dispatch prompt beside each
- [Cohort 08](./cohort-08.md) ([prompt](./cohort-08-prompt.md)) — four notes
  across the two smallest residual components; two already-populated ingests
- Cohort 09, the 15-note residual component, split into a sequential pair:
  [09a](./cohort-09a.md) ([prompt](./cohort-09a-prompt.md)), 7 targets / 0.96 MB,
  and [09b](./cohort-09b.md) ([prompt](./cohort-09b-prompt.md)), 8 targets /
  0.30 MB. Two bridge ingests
- Cohort 10, the 18-note residual component, likewise:
  [10a](./cohort-10a.md) ([prompt](./cohort-10a-prompt.md)), 9 targets / 0.80 MB,
  and [10b](./cohort-10b.md) ([prompt](./cohort-10b-prompt.md)), 9 targets /
  1.41 MB. Two bridge ingests
- [Cohort 02 prediction](./cohort-02-prediction.md) — **sealed**; open when
  judging that run, never while executing it

## What a later session should not assume

**That a clean grounding is the expected outcome.** Cohort 01 returned zero
grounded-as-written across eight claim uses. Every case examined during the
design work returned a defect rather than a confirmation. An executor expecting
to confirm citations will confirm them.

**That the cohorts are a sweep.** They ground claims notes already make. They do
not search for prior art a note failed to cite — that blind spot is stated in ADR
073 and belongs to a write-time literature check that does not exist.

### Sequential pairs

Cohorts 09 and 10 were each a single connected component: every target shared an
ingest with another, so neither admitted a parallel split. Each was cut into a
sequential pair — `09a`/`09b` and `10a`/`10b` — bounding one agent's context
while keeping the halves off each other. **A pair's halves must not run
concurrently**; the cut leaves 2 bridge ingests each, and V1 ships no locking, so
a concurrent append could lose an entry. Either pair may run alongside any other
cohort.
