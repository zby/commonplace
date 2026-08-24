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

Cohorts 01–07 cover 29 notes. The remainder sits in one connected component of
36 notes and 62 ingests that cannot be parallelized on both conflict axes — see
Concurrency.

## Concurrency

Two conflict axes, and both bind. Concurrent agents must not append to the same
ingest's `Claims` section — V1 ships no locking, deliberately — and must not edit
the same note during repair. So the safe unit is a connected component of the
note-to-ingest graph.

Cohorts 02–07 are mutually disjoint on both axes by construction. Six agents can
run with no coordination scheme. Do not hand-assemble a cohort without rechecking
disjointness against every cohort running at the same time.

The 36-note giant component is the open scaling problem. Splitting it needs
either serialized repair or a scheme separating grounding from repair so only the
ingest axis binds. **Do not build that scheme until the procedure has been
exercised on cohorts that do not need one.**

## What closes this workshop

1. Every cohort has a completion record where each claim use carries a terminal
   disposition or a named blocker.
2. The giant component is either worked or has a recorded decision not to work
   it, with the reason.
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
