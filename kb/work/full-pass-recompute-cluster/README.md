# Full improvement pass over the recoverability/economics cluster

## Goal

Run [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md)
over the six notes this cluster produced or altered on 2026-08-22/23. Not yet
started.

The notes were written fast, in one conversation, several of them revised or
retitled hours after landing. None has been through a full pass. They validate
clean and are densely linked, which is exactly the state where an unexamined
claim survives on structural plausibility.

## Batches

Two batches of four and two, ordered by dependency rather than by topic. A pass
can reframe a note's title and thesis, which invalidates citers — so the
most-depended-on notes go first, and the second batch runs against a settled
first batch.

**Batch 1 — most-depended-on.**

1. `kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`
2. `kb/notes/documentation-generates-the-system-rather-than-describing-it.md`
3. `kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md`
4. `kb/notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md`

**Batch 2 — dependents.**

5. `kb/notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md`
6. `kb/notes/addressability-grain-not-compression-ratio-decides-whether-a.md`

Batch 2 cites batch 1 four ways: `addressability-grain` extends
`documentation-generates`, contrasts `human-recompute`, and grounds on
`llm-recompute`; `a-theory-may-name` contrasts `superseded-choices`. If batch 1
reframes any of those, batch 2's premises move before its own pass reads them.

Excluded: `artifact-analysis-README.md`, `document-system-README.md`,
`context-engineering-README.md`. They are type `tag-readme`, weight-gated, and
carry index entries rather than claims; the pass targets notes.

## What this pass is likely to find, and should not be shielded from

Recorded so a later session does not mistake a known weakness for a surprise,
and does not pre-empt the pass's own judgment either. These are expectations,
not instructions to the pass.

- **`human-recompute` carries a claim that may not be its own.** Four
  consecutive "Consequence:" sections, one of which — segmentation strips the
  drift detector from the low-traffic layer — is a maintenance claim on an
  economics note, and more general than its host. A split candidate. Deciding
  it before the pass would also be legitimate; deciding it *during* is what the
  pass is for.
- **Two notes cite Commonplace as an existential witness.** The collection-fit
  check should confirm that reads as witness rather than subject. Both were
  written under the bound-variable requirement, so this is a live test of
  whether the requirement was met, not a formality.
- **`llm-recompute` received a scope paragraph on 2026-08-23** naming the
  volume condition under which its default flips back. It is the oldest note
  here and the least examined against its new neighbours.
- **`a-theory-may-name` was revised by a second agent** after its initial write,
  including a replaced section. Two authors, one pass.

## Operating constraints

From the instruction, not restated in full — read it before starting.

- **One note at a time per pass.** The concurrency precondition forbids any
  other actor editing `{note-path}` from step 1 until the pass stops or
  completes. Two passes over two different notes may overlap; two passes over
  one note may not.
- **Steps 8, 9, 10 are a strict pipeline**, not a parallel batch. Closing jobs
  snapshot the note at pair-create, so a closing job queued while the copyedit
  runs pins freshness to pre-copyedit text.
- **Re-entrancy preflight first.** A prior `pending` report for the same
  historical path blocks a new pass until resolved.
- **Cost is real.** Six method families per note, each in a fresh single-use
  sub-agent, plus a closing cycle that reruns all of them. Budget per note, not
  per batch.
- **A reframe leaves the KB asserting the old claim.** The required follow-up —
  rename via `commonplace-relocate-note`, then fix inbound link text, summaries,
  and any citer that used the old title as a premise — runs after the pass, not
  inside it. Within this cluster the citers are mostly each other, so a batch-1
  reframe creates batch-2 work.

## What closes this workshop

Every note has a retained packet. `keep` packets are applied and closed;
`delete`, `merge`, and `rehome` packets are handed back with their dispositions
unresolved, since executing those is the reader's call. Any reframe's follow-up
operation is either executed or recorded as a named open item with concrete
scope. Findings that generalize beyond these six notes are promoted; the rest is
consumed and the workshop deleted.
