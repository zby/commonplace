# Full improvement pass over the recoverability/economics cluster

## Goal

Run [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md)
over the seven notes this cluster produced or altered on 2026-08-22/23, plus one
older note the work implicated — eight in all. Both batches now have retained,
completed passes. Batch 2's first pass overlapped Batch 1's edits, so all four
Batch 2 notes were rerun in binding order against Batch 1's committed result.
Every Batch 2 reframe follow-up is complete.

The notes were written fast, in one conversation, several of them revised or
retitled hours after landing. At workshop start, none had been through a full
pass. They validated clean and were densely linked, which is exactly the state
where an unexamined claim survives on structural plausibility.

## Batches

Two batches of four. The notes are topologically sorted across both batches, and order is binding within each — every note runs after the notes it cites. A pass
can reframe a note's title and thesis, which invalidates citers — so the
most-depended-on notes go first, and the second batch runs against a settled
first batch.

- [Batch 1](./batch-1.md) — complete and committed.
- [Batch 2](./batch-2.md) — complete after an ordered rerun against the
  committed upstream notes.

Batch 2 depends on batch 1 six ways: `addressability-grain` extends
`documentation-generates` and grounds on `llm-recompute`;
`artifacts-must-preserve-named-choice-scope`
contrasts `superseded-choices` and cites `areas-exist` as evidence;
`an-insufficient-summary` extends `llm-recompute` and contrasts
`documentation-generates`. If batch 1 reframes any of those, batch 2's premises
move before its own pass reads them.

Two further edges fall inside batch 2 — `addressability-grain` contrasts
`opposed-recompute-factors`, and `an-insufficient-summary` contrasts
`addressability-grain` — which is why order is binding within a batch and not
only across the boundary.

Excluded: `artifact-analysis-README.md`, `document-system-README.md`,
`context-engineering-README.md`. They are type `tag-readme`, weight-gated, and
carry index entries rather than claims; the pass targets notes.

## What this pass is likely to find, and should not be shielded from

Recorded so a later session does not mistake a known weakness for a surprise,
and does not pre-empt the pass's own judgment either. These are expectations,
not instructions to the pass.

- **`opposed-recompute-factors` carried a claim that might not have been its own.** Four
  consecutive "Consequence:" sections, one of which — segmentation strips the
  drift detector from the low-traffic layer — is a maintenance claim on an
  economics note, and more general than its host. A split candidate. Deciding
  it before the pass would also be legitimate; deciding it *during* is what the
  pass is for.
- **Two notes cite Commonplace as an existential witness.** The collection-fit
  check should confirm that reads as witness rather than subject. Both were
  written under the earlier choice-scoping requirement, so this is a live test of
  whether the requirement was met, not a formality.
- **`llm-recompute` received a scope paragraph on 2026-08-23** naming the
  volume condition under which its default flips back. It is the oldest note
  here and the least examined against its new neighbours.
- **`artifacts-must-preserve-named-choice-scope` was revised by a second agent**
  after its initial write,
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
