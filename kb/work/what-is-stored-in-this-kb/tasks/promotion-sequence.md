# Promote the choice-binding notes/reference boundary into binding artifacts

## Status

Open. Steps 1 and 2 are complete; step 3 is next. Five steps, ordered. Each
step's gate is the reason it sits where it does — the ordering is the part
worth following, not the step list.

The boundary now has a reader: agents writing notes or reference artifacts load
the collection's `COLLECTION.md`, not this workshop. The remaining steps apply
that accepted rule.

## Gate before step 2 — cleared

The [bound-variable sweep](./bound-variable-sweep.md) reported on 2026-08-23:
0/27 failures. The clause is stated flatly, with no transition provision and
no grandfathering, and its wording has already been corrected in the
[applied edits](../draft-collection-contract-edits.md). This cleared step 2.

The sweep left one targeted cleanup rather than a migration:
`areas-exist-because-useful-operations-require-reading-notes-together.md`
carries choice-dependent propositions after its opening — a threshold
presented as generally determined, a selected membership policy, and
assertions about the retired `areas:` machinery. Handle it as its own small
piece of work; it is not a gate on anything here. Check first whether the note
should be retired rather than repaired, since areas were replaced by tags.

## 1. Promote the two belief drafts — done 2026-08-23

[Superseded choices are retained](../draft-superseded-choices-are-retained-superseded-beliefs-are-not.md)
and [a theory may name a choice only as a bound variable](../draft-a-theory-may-name-a-choice-only-as-a-bound-variable.md).
Both are bare bones and need full note treatment through `cp-skill-write`.

Each draft carries a "Not already covered" section naming the incumbent it was
scoped against. Verify that scoping still holds before writing — if an
incumbent moved, the draft's contribution may have evaporated.

First, because the draft ADR's footer rests on both. Promoting the ADR first
leaves dangling links.

**Done.** Both live and validating clean:
[superseded-choices-are-retained-superseded-beliefs-are-not.md](../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md)
and [a-theory-may-name-a-choice-only-as-a-bound-variable.md](../../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md).
Step 2 must cite them by their live paths, not the workshop drafts.

Two things surfaced during promotion that step 2 should carry. The retention
note's real neighbour was `commitment-not-derivation-creates-new-ground-truth.md`,
not the artifact-classification note the draft scoped against; the commitment
boundary settles which artifact is authoritative, content kind settles whether
the displaced version survives. And the bound-variable note could not cite the
sweep findings, because the notes contract forbids outbound links into
`kb/work/` — the evidence is restated in prose so the note survives this
workshop's deletion. Apply the same constraint to anything else promoted from
here.

Watch for a tag-README carrying `complete: true` that must gain an entry, or
validation hard-fails. `artifact-analysis-README.md` needed exactly this for
the last note in this thread.

## 2. Promote the ADR and apply the contract edits — done 2026-08-23

The [draft ADR](../draft-adr-collection-placement-follows-content-kind.md) and
the [applied edits](../draft-collection-contract-edits.md) supplied the starting
text. ADR 070 was free at execution. Final review expanded the five drafted
changes to six by making the evidence/work/log lifecycle explicit and added the
missing `kb/agentic-systems/` route. A particular observation stays in notes
only when the artifact states its bounded theoretical inference and limit;
current or historical Commonplace state remains reference.

**Done.** [ADR 070](../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md)
records the accepted decision, and both collection contracts carry the binding
placement rule. Final review also fixed the observation boundary: unresolved
theory-facing evidence remains in `kb/work/`; first occurrences and pure pattern
records without explanation belong in `kb/log.md`; `kb/notes/evidence/` requires
a bounded inference and its limit even when the larger theory is incomplete.

This step gave the boundary a reader. Everything after it is an application of
a stated rule rather than an argument.

## 3. Decide the text-contract home

[The existing task](./text-contract-and-profiles.md) has options A, B, and C
with decision tests and a post-ADR-069 backlink recount already done. It was
stopped pending a general placement rule; ADR 070 now supplies it.

## 4. Act on the relocation candidates

Three reference artifacts the ADR names as candidates and does not authorize:
`tag-readme-trace-observed-causal-connection.md`,
`harness-sub-agent-model-selection-regression.md`, and
`commonplace-as-a-reflective-system.md`.

Judge each against the binding rule rather than moving all three. A move needs a
substantive theoretical contribution after Commonplace's choices are bound. The
harness regression is the doubtful one — it is primarily an operational incident
about an external tool and may remain reference or move with its external-system
evidence.

Present the candidate list and wait for maintainer approval before moving
anything. Use `commonplace-relocate-note`, never `git mv` — it rewrites
consumers and adds the redirect.

ADR 070 now lets a move apply a stated rule instead of a reviewer's opinion.

## 5. Disposition the remaining definitions

The [definition audit](../definition-audit.md) left machinery-first candidates
(`answerability`, `text-contract`) and mixed candidates (`discovery-lifecycle`,
`directed-reading`) undecided, plus a set flagged "keep provisionally" pending
the content model. The model has since settled.

The audit's own disposition test is the boundary applied to vocabulary, so
ADR 070 supplies the rule. The hard case is stipulated vocabulary: replace the
local term with its general description and ask whether a substantive,
contestable distinction remains.

## Deliberately not in this sequence

The maintenance-form audit of current-state reference artifacts —
`architecture.md`, `lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture halves of
`review-architecture.md` and `freshness-architecture.md`. Their placement is
settled: current and historical Commonplace state belongs in reference. The
remaining per-artifact choice—generate, register for staleness, author only the
irrecoverable part, or minimize—depends on the recovery test and can run in
parallel with this sequence.

## Completion condition

The boundary binds in both collection contracts, an ADR records it, the two
supporting notes are live and validated, the text-contract term has one
canonical owner, and every definition in the audit has a disposition. Any
per-artifact maintenance-form audit for current-state reference documentation
may continue as a separate handoff; its placement no longer blocks this
workshop.
