---
description: "Proposal: decide what a failed agent-memory review replacement owes the incumbent it already archived, once the run has passed the point where it can still decline to start"
type: ../types/design-proposal.md
tags: [architecture, lifecycle-management]
---

# Recoverable replacement of an incumbent review

A workflow that replaces an artifact in place has to decide when the incumbent stops being the live one, and what happens if the replacement never arrives. `write-agent-memory-system-review` now refuses to start when it can see in advance that drafting is impossible. It still has no answer for the failures it cannot see in advance: a worker that launches and then fails, and a draft that quality assurance rejects. In both cases the incumbent has already been archived, and nothing restores it.

This proposal parks the remaining question: what restore obligation a replacement workflow owes the artifact it is replacing. It does not select an option.

## Current state (as of 2026-08-29)

- [`write-agent-memory-system-review`](../../instructions/write-agent-memory-system-review/SKILL.md) is a fourteen-step procedure. Steps 1–6 are read-only setup.
- **Adopted 2026-08-29:** step 7 now confirms that drafting is possible before anything mutates. If the harness cannot launch a worker and no local fallback is authorized, the run stops with the incumbent untouched at `note_path`. This was option 1 of this proposal's original option space; it shipped, so it is recorded here rather than proposed below.
- Step 8 archives the incumbent, and the rename is not the whole edit: it also clears `tags` (including `trace-learning`), inserts a banner pointing at the not-yet-written replacement, and removes `user-verified` if present.
- Step 9 delegates drafting. Steps 12 and 13 run taxonomy and semantic quality assurance, either of which can reject the draft. All three sit after the archive.
- No step restores the incumbent. The skill has no inverse for the rename or for the three content edits that accompany it.
- A same-day rerun is handled — the archive target takes a numeric suffix rather than overwriting — so repeated failures accumulate archived copies rather than destroying earlier ones.
- The [commissioning-surface audit](../../reports/retained/planning-delegation-theory/shared-doctrine-operationalization/commissioning-surface-audit.md) recorded this cohort as *defer*, stating that the fix needs a checked candidate/promotion or exact-restore protocol including staged rename recovery, and that removing duplicated packet text would not address it.
- [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) already runs the opposite ordering for a comparable job: workers write isolated candidate files, acceptance binds an exact digest, the parent alone mutates the live target, promotion stops when the live target has drifted, and the run is retained for recovery rather than discarded.

## Problem

The adopted check closes the failures the run can predict. It cannot close the failures that only appear once work is under way, and those are the ordinary ones: a worker that dies mid-draft, a draft that quality assurance rejects. In each case the workflow has already spent an irreversible action, and the collection is left with no active review for that system.

Three properties of the incumbent make the loss asymmetric:

- It is the collection's only active review for that system. While the run is stopped, navigation and comparison surfaces point at nothing.
- Its archived form has been edited to describe a state that did not come about. A reader who finds it is told a current review exists elsewhere.
- `user-verified` records a human attestation. An agent can strip it and cannot regenerate it; only the person who verified the content can restore it truthfully.

So "restore the incumbent" is not a rename in reverse. It is a rename plus an undo of edits, one of which crosses the boundary between what an agent may assert and what a human must.

## Forces

- **Ordering alone cannot finish the job.** The cheap fix is spent. What remains are failures discoverable only after the mutating phase begins, so any further improvement has to add a recovery path or move the mutation later.
- **Incumbent-blindness must survive the change.** The drafting worker must not read the incumbent. An option that keeps the incumbent at its canonical path has to prevent the worker from reading it by instruction or by scope, and that instruction is weaker than a file that is not there.
- **One active review per system.** Any transient state where two candidate reviews sit in the collection needs a rule saying which is live, or a location outside the collection for the one that is not.
- **Attestation cannot be forged.** If a restore path must return `user-verified`, only an exact byte restore of the pre-run file is honest. A reconstructed file is not the attested one.
- **The archived record is wanted even on success.** Superseded reviews are deliberately retained with a banner. A fix must not make ordinary successful replacement stop producing that record.
- **A versioned protocol is not free to change.** This workflow's controls — anti-recursion, sole write, read-only checkout, pinned citations — are load-bearing. A restructure has to preserve them, which is why the audit called for a focused failure-path design rather than an edit.

## Option space

1. **Exact-restore obligation.** Give the run an inverse: on any stop before a promoted replacement, restore the incumbent's exact pre-run bytes at its canonical path and delete the archive stub. Closes every remaining failure at the cost of a recovery path that must itself be exercised, and it is the only option that can honestly return `user-verified`.
2. **Candidate and promotion.** Adopt the multistage shape: the incumbent stays live, the worker writes a candidate outside the collection's live path, and the parent archives and promotes in one guarded step after quality assurance. Closes the window structurally, matches machinery the repository already operates, and moves the incumbent-blindness guarantee from "the file is gone" to an explicit scope rule.
3. **Accept the residue.** Treat the adopted precondition as sufficient in practice and record the remaining failures as known, on the grounds that a same-day rerun already recovers the common case by drafting a fresh replacement. Cheapest, and honest only if someone checks how often a run dies mid-draft.

Options 1 and 2 are not exclusive: a promotion-shaped workflow still needs a stated behavior when promotion is abandoned, even if that behavior becomes trivial.

## Operativity path

The consumer is the skill file itself, read by the parent agent that runs the workflow; the channel is instruction text, and its force is whatever the parent's runtime supplies. That is the same force the adopted precondition has, so option 3 needs no new mechanism. Options 1 and 2 add states a parent can get wrong silently — a restore that half-completes, a promotion that leaves a candidate behind — and the adoption decision should say whether those states get a deterministic check or stay under instruction alone. No validator sees this today.

## What the adoption decision needs

- Whether restoring `user-verified` is required. If it is, the design needs exact bytes, which rules out any option that reconstructs the incumbent.
- Whether the transient candidate lives inside the collection, and if so what marks it as not yet live.
- How incumbent-blindness is guaranteed once the incumbent is no longer removed from its path.
- Whether the failure path gets an exercised test, given that the audit's stated reason for deferral was that these states have never been run.
- For option 3, what evidence would show the residue is rare enough to accept.
