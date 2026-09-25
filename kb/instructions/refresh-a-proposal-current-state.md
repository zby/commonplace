---
description: Use when a live design proposal's current-state anchor may be stale — re-checks its system facts against later ADRs, code, and reference docs, and routes shipped or foreclosed content to the right procedure
type: instruction
---

# Refresh a proposal's current state

**Target: $PROPOSAL_PATH**

Makes a live proposal's `## Current state (as of YYYY-MM-DD)` section true on today's date, so an adoption decision can rely on it, and hands off any part the system has already decided.

## When this does not apply

- **The proposal is archived.** Archived proposals are frozen; do not refresh them. If something current was left behind in one, promote it into the frontier as a new or existing live proposal.
- **You intend to change the proposal's options or forces for design reasons.** That is an ordinary revision under the [design-proposal type](../reference/types/design-proposal.md); refresh the anchor as part of it.

## Steps

1. **Collect what changed since the anchor date.** List ADRs dated after it (`ls kb/reference/adr/`; each carries a `**Date:**`), and read every one whose title or description touches the proposal's subject. Run `git log --since=<anchor date> -- <paths the proposal names>` for the code and contracts it cites. If the clone is shallow, run `git fetch --unshallow` first.

2. **Check each current-state fact.** For every bullet in the anchor, and for every factual claim about the system in the problem and options, find the live evidence — code, schema, command `--help`, reference doc, or ADR — and read it. Classify the fact as still true, false, or no longer relevant. Also note any new system fact the design now depends on, such as a later ADR that changes a force.

3. **Route decided content before editing.**
   - Part of the proposal has shipped → [extract the adopted part of a proposal](./extract-adopted-part-of-a-proposal.md), then continue here.
   - All of it has shipped, or a later decision forecloses all of it → [retire an artifact](./retire-artifact.md) and stop.
   - A later decision forecloses one option but the question stays open → remove that option, and name the foreclosing ADR in the anchor.
   - No decision forecloses it, but its problem no longer exists in the system or its adoption trigger has plainly lapsed → stop and report this to the operator with the evidence. Withdrawal is the operator's decision; if they withdraw it, use [retire an artifact](./retire-artifact.md), whose destination for a withdrawn proposal is delete.

4. **Rewrite the anchor.** Correct false facts, remove irrelevant ones, add new ones with their evidence (ADR link, file path, or command), and set the anchor date to today. Keep the anchor to facts the proposal rests on; the change history stays in git.

5. **Re-check the rest against the corrected facts.** Where a corrected fact changes a force, an option's operativity path, or an adoption criterion, revise it. If an adoption criterion is now met, say so in the anchor; deciding is the operator's call, not the refresh's.

6. **Commit** the refresh alone, with a body that lists what was false and what the new evidence is.

## Verify

- `commonplace-validate` on the proposal: no failures, no link warnings.
- Every anchor bullet cites evidence you read in step 2.
- The description and opening still describe the proposal's open question.

---

Relevant Notes:

- [Design proposal](../reference/types/design-proposal.md) — operates-on: the type whose current-state anchor this procedure maintains
- [Extract the adopted part of a proposal](./extract-adopted-part-of-a-proposal.md) — see-also: the procedure a refresh hands off to when part of the design has shipped
