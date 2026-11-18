# Concrete cases for abstract notes

Posed 2026-11-18 by the operator, as direction: abstract notes need concrete
examples, asked for systematically and with a limit. The two gate drafts here
are an agent's proposal, awaiting the operator's reading. Neither is live:
the review catalog reads gates only from `kb/instructions/review-gates/`.

## Goal

A note whose contribution is a distinction or an abstract mechanism shows
concrete cases, and the review tests the distinction on concrete cases.

The operator's reason: such notes are hard to grasp, and a mistake in a
distinction often shows only when a concrete case is put through it. So an
example has two uses. It helps the reader, and it tests the note.

## Limits the operator and the agent agreed

- Not everywhere. Only notes whose central contribution is a distinction or
  an abstract mechanism, where a reader cannot name a case from the wording.
- Only the central contribution, not every assertion.
- A distinction gets a case on each side and what differs between them.
- A constructed case is allowed when it is marked as an illustration. Its
  job is to test the distinction, not to be evidence for the claim.
- Not for instructions (an executor copies an example), ADRs, reference
  documents, indexes, logs or reports.

## Drafts

- [abstract-claim-without-case](./abstract-claim-without-case.md): the note
  shows no case. Lens `accessibility`, depth 3.
- [distinction-case-test](./distinction-case-test.md): the reviewer builds
  cases and runs the distinction on them. Lens `semantic`, depth 2.

## What exists already

Read on 2026-11-18. None of these asks whether the note shows a case, and
none tests a two-sided distinction by sorting cases.

- `semantic/completeness-boundary-cases` generates boundary cases, but for
  an enumeration or taxonomy that claims to cover a space.
- `semantic/unearned-generality` tests whether abstract wording is earned.
- Premise decomposition hunts a counterexample for each premise; for a
  definition it looks for a mis-sorted case. It is a depth 1 report with no
  verdict, and it covers every premise, not the central distinction.
- Composition friction tests whether the central claim survives being made
  concrete.
- `compression-bundle/detail-overhang` limits examples that outgrow their
  role. The new gates must not push notes into that failure.

The second draft overlaps premise decomposition most. It is worth keeping
apart only if it finds defects in distinctions that the report misses, or
finds them at lower cost. That is the first thing to check.

## Not drafted: the rewrite procedure

`rewrite-a-note/write-a-rewrite-candidate.md` says to write the shortest note
that makes the contribution clear, and nothing asks the writer for a case.
The rewrite procedure is being changed in another session, so this workshop
proposes and does not edit it:

- the stage that accounts for the note's claims also collects, from the
  sources, a case for each side of the central distinction;
- the candidate writer uses them, and a case the reader needs in order to
  apply the claim counts as part of making the contribution clear;
- the candidate's review runs the distinction case test before acceptance.

## What closes this workshop

1. The operator has accepted, changed or rejected each draft.
2. Each accepted draft was run on at least five existing theory notes, among
   them the three that had full passes on 2026-11-18, and its findings were
   read: how many were real defects, and how many repeated a finding of
   premise decomposition or composition friction on the same note.
3. Accepted gates are in `kb/instructions/review-gates/` with the depth
   table in the review system README updated, and the rewrite proposal is
   handed to whoever owns that procedure.
