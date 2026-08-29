---
description: "Proposal: stop destroying the only live agent-memory review before a replacement is known to be achievable, and decide what a failed replacement run must restore"
type: ../types/design-proposal.md
tags: [architecture, lifecycle-management]
---

# Recoverable replacement of an incumbent review

A workflow that replaces an artifact in place has to decide when the incumbent stops being the live one. `write-agent-memory-system-review` currently decides that first, before it knows whether a replacement can be produced at all. If the run then stops, the collection is left with no active review for that system and an archived file that announces a successor which does not exist.

This proposal parks the design question that failure exposes: what ordering and what restore obligation a replacement workflow owes the artifact it is replacing. It does not select an option.

## Current state (as of 2026-08-29)

- [`write-agent-memory-system-review`](../../instructions/write-agent-memory-system-review/SKILL.md) archives the incumbent at step 7 and delegates drafting at step 8. Step 7 renames `note_path` to a dated `.replaced.` sibling, and the rename is not the whole edit: it also clears `tags` (including `trace-learning`), inserts a banner pointing at the not-yet-written replacement, and removes `user-verified` if present.
- Step 8 begins by checking whether the harness can launch a worker, and stops the run if it cannot. That check runs *after* the archive. Drafting can also fail later, or return a draft the parent's taxonomy or semantic QA rejects.
- No step restores the incumbent. The skill has no inverse for the rename or for the three content edits that accompany it.
- A same-day rerun is handled — the archive target takes a numeric suffix rather than overwriting — so repeated failures accumulate archived copies rather than destroying earlier ones.
- The [commissioning-surface audit](../../reports/retained/planning-delegation-theory/shared-doctrine-operationalization/commissioning-surface-audit.md) recorded this cohort as *defer*, stating that the fix needs a checked candidate/promotion or exact-restore protocol including staged rename recovery, and that removing duplicated packet text would not address it. That deferral names no owner and no trigger.
- [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) already runs the opposite ordering for a comparable job: workers write isolated candidate files, acceptance binds an exact digest, the parent alone mutates the live target, promotion stops when the live target has drifted, and the run is retained for recovery rather than discarded.

## Problem

The workflow spends an irreversible action to buy an ordering convenience. Freeing `note_path` before drafting means the worker can write to the canonical location, and it supports the rule that the drafting worker must not read the incumbent. Both are real, but neither requires that the incumbent stop being live before a replacement exists.

Three properties of the incumbent make the loss asymmetric:

- It is the collection's only active review for that system. While the run is stopped, navigation and comparison surfaces point at nothing.
- Its archived form has been edited to describe a state that did not come about. A reader who finds it is told a current review exists elsewhere.
- `user-verified` records a human attestation. An agent can strip it and cannot regenerate it; only the person who verified the content can restore it truthfully.

So "restore the incumbent" is not a rename in reverse. It is a rename plus an undo of edits, one of which crosses the boundary between what an agent may assert and what a human must.

## Forces

- **Worker availability is knowable before the destructive step.** The skill already performs that check; it is only sequenced late. This makes the cheapest option unusually cheap, and it should not be allowed to disguise the harder failures behind it.
- **Late failures remain.** Drafting can fail after a worker launches, and QA can reject a draft. An ordering fix alone leaves those cases holding a live path that is either empty or occupied by a rejected draft.
- **Incumbent-blindness must survive the change.** Whatever ordering is chosen, the drafting worker must not read the incumbent. An option that keeps the incumbent at its canonical path has to prevent the worker from reading it by instruction or by scope, and that instruction is weaker than a file that is not there.
- **One active review per system.** Any transient state where two candidate reviews sit in the collection needs a rule saying which is live, or a location outside the collection for the one that is not.
- **Attestation cannot be forged.** If a restore path must return `user-verified`, only an exact byte restore of the pre-run file is honest. A reconstructed file is not the attested one.
- **The archived record is wanted even on success.** Superseded reviews are deliberately retained with a banner. A fix must not make ordinary successful replacement stop producing that record.
- **A versioned protocol is not free to change.** This workflow's controls — anti-recursion, sole write, read-only checkout, pinned citations — are load-bearing. A restructure has to preserve them, which is why the audit called for a focused failure-path design rather than an edit.

## Option space

1. **Check first, archive later.** Move the worker-availability check ahead of the archive. Cheapest, and it removes the specific failure observed. It does nothing for drafting failure or QA rejection, so it narrows the window rather than closing it.
2. **Exact-restore obligation.** Keep the ordering and give the run an inverse: on any stop before a promoted replacement, restore the incumbent's exact pre-run bytes at its canonical path and delete the archive stub. Closes every failure at the cost of a recovery path that must itself be exercised, and it is the only option that can honestly return `user-verified`.
3. **Candidate and promotion.** Adopt the multistage shape: the incumbent stays live, the worker writes a candidate outside the collection's live path, and the parent archives and promotes in one guarded step after QA. Closes the window structurally, matches machinery the repository already operates, and moves the incumbent-blindness guarantee from "the file is gone" to an explicit scope rule.
4. **Refuse to start.** Make the run establish every precondition it needs — worker availability, checkout freshness, write scope — before any mutation, and abort otherwise. A discipline rather than a mechanism; it composes with 2 or 3 rather than competing.

Options 2 and 3 are not exclusive: a promotion-shaped workflow still needs a stated behavior when promotion is abandoned, even if that behavior becomes trivial.

## Operativity path

The consumer is the skill file itself, read by the parent agent that runs the workflow; the channel is instruction text, and its force is whatever the parent's runtime supplies. That is the same force the current broken ordering has, so no new enforcement mechanism is required for options 1 or 4. Options 2 and 3 add states a parent can get wrong silently — a restore that half-completes, a promotion that leaves a candidate behind — and the adoption decision should say whether those states get a deterministic check or stay under instruction alone. No validator sees this today.

## What the adoption decision needs

- Which failures are in scope: the observed pre-drafting stop only, or drafting failure and QA rejection as well.
- Whether restoring `user-verified` is required. If it is, the design needs exact bytes, which rules out any option that reconstructs the incumbent.
- Whether the transient candidate lives inside the collection, and if so what marks it as not yet live.
- How incumbent-blindness is guaranteed once the incumbent is no longer removed from its path.
- Whether the failure path gets an exercised test, given that the audit's stated reason for deferral was that these states have never been run.
