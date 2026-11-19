---
description: High-level operator overview of the review and editing system — authority split, freshness, improvement modes, publication boundaries, order of concerns, and limits
type: types/note.md
tags: []
---

# Review and editing system

An overview for human operators deciding when to review or edit notes. You do not need to memorize commands, flags, or current gate lists: ask your agent in ordinary language, and it retrieves live details through `cp-skill-review`, `cp-skill-revise`, and `--help`.

## Two halves, split by authority over the note

Two commands separate judging a note from changing it ([ADR 139](./adr/139-only-commonplace-revise-writes-a-note.md)):

- **Review (`commonplace-review`)** asks headless workers to judge notes against criteria — closed-ended catalog gates, type/collection conformance, compression checks, or open-ended reports — and stores one result per `(note, criterion)` pair. **It never writes a note.**
- **Editing (`commonplace-revise`)** is the only review/editing command that writes a note. It runs simplification passes, finding fixes, or full source-grounded rewrites.

## Core properties

- **Opt-in and paid.** Review is not part of ordinary writing and nothing runs it automatically. Every launch is a paid worker call; fixed prompt context dominates cost, so bundle grouping can share context across a bundle's gates (pair grouping stays the default because verdict quality has not been compared).
- **Freshness is hash-based and independent of Git.** A result stays fresh while the hashes of the note's watched parts and the criterion match. Result files are gitignored and stay on the machine that ran the review.

| Do not conflate | Distinction |
|---|---|
| `fresh` and approved | Fresh means the inputs have not changed since the review ran. It does not approve the note or resolve findings. |
| `report` and a verdict | `report` means an open-ended report criterion completed; it is not a fifth verdict. |
| `pass` and absence of problems | A `pass` means one gate found nothing to flag. |

## Ways to improve a note

Simplification procedures edit a note whose claims already stand; rewrite rebuilds a note whose claims or synthesis are unsettled.

| Mode | What chooses the work | New review launches | May write the note |
|---|---|---|---|
| **Focused** | You pick one finding, one pass, or a fixed plan | none | yes |
| **Triage** | You decide each fresh stored warning or failure first | none | no (writes pending answers) |
| **Quick** | An assessor picks passes from the note and fresh stored findings | none | yes |
| **Full** | Runs reviews, open-ended reports, and an inbound-link role report, then assesses | yes (all depth-declaring criteria, conformance, role) | yes |
| **Rewrite** | Rebuilds from grounded sources under a commission you agree on | rewrite review | no (always holds candidate) |

**Publication and reversal.** Direct edits (`commonplace-revise` note-first and `apply`) write changes to your working tree without asking for whole-text approval and without committing (`git diff` shows them; git reverses them). Two cases **hold** the candidate instead of writing the note: a revise candidate that adds a new validation warning, and every accepted rewrite candidate. Held candidates wait for your explicit approval of that exact text (or your revision of it).

**Stops, carry-over, and write briefs.** Per-item wording passes, triage findings, and depth-1 plan stops pause for your decision in an [answers](../types/answers.md) file; rejected and deferred decisions carry over to later runs on the same note so you are not asked the same question repeatedly. A note's sibling [write brief](../types/write-brief.md) holds its lasting "must keep / must exclude" boundaries; no code edits a brief without your word.

## Order of concerns

Review criteria and edit operations share one optional `depth` scale (an integer from 1; lower depth runs first so higher-order claim and scope issues settle before wording polish):

| Depth | Concern | Review layer | Editing layer |
|---:|---|---|---|
| 1 | whether the note's claim and scope should stand | critique, friction, premises, role report | split out a treatment |
| 2 | what the note asserts and on what grounds | semantic gates, type and collection conformance | narrow overclaims |
| 3 | terms and what a reader needs to know | accessibility gates | abstractions |
| 4 | structure and proportion | complexity and compression checks | readability and flow |
| 5 | wording | sentence gates | plain wording |
| 6 | title, description, and opening | frontmatter gates | opening and title |

Each criterion or edit-operation file declares its own `depth:` value and governs its exact placement; ask your agent to list current assignments if you need them.

## Safety and limits

- **Checkout guard.** Every run records `git status` and file digests before and after and reports any changed paths (including concurrent edits from other sessions). Nothing is reverted automatically; inspect actual diffs rather than relying on a worker's summary.
- **No automatic verification of fixes.** Editing procedures do not re-review the note to prove a finding is resolved; run a fresh review afterward when you want updated verdicts.
- **Worker sandboxing.** Profile write restrictions are best-effort (Claude Code's Bash denial has not been observed to refuse a write, and Codex/Pi workers can write the workspace); the checkout guard is the verified control.

## Where current details live

- **Running reviews or revisions:** ask your agent — it uses `cp-skill-review`, `cp-skill-revise`, and `--help` (see [commands](./commands.md)).
- **Pi reviewer setup:** [run a review from Pi](../instructions/run-review-from-pi.md).
- **Implementation and state boundaries:** [review architecture](./review-architecture.md) and [ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) through [ADR 139](./adr/139-only-commonplace-revise-writes-a-note.md).
