---
description: Use when part of a live design proposal has shipped while the rest is still undecided — moves the shipped part out and narrows the proposal to its open remainder
type: kb/types/instruction.md
---

# Extract the adopted part of a proposal

**Target: $PROPOSAL_PATH**

Makes a partially adopted proposal true again: after this, the proposal holds only undecided design, and the shipped part is described where readers of the shipped system look.

## When this does not apply

- **Everything in the proposal has shipped, or a decision foreclosed all of it.** Use [retire an artifact](./retire-artifact.md); its extraction step covers the whole proposal.
- **Nothing has shipped, but the current-state anchor is stale.** Use [refresh the proposal's current state](./refresh-a-proposal-current-state.md).
- **The shipped behavior differs from every option the proposal holds.** The proposal was not adopted; the system moved elsewhere. Record the new fact in the current-state anchor through a refresh, and judge whether the open question still exists.

## Steps

1. **Identify the shipped part and its record.** For each option, choice, or clause you believe shipped, find the code, command, or contract that implements it and the decision that carries it: an ADR, or the implementing commit when the change needed no ADR (`git log -S'<identifier>'`; its `Decision:` trailer names the ADR it implements). If the clone is shallow, run `git fetch --unshallow` first. A claim that something shipped with no implementation you can point to is not an adoption; stop and report it.

2. **Make sure the shipped behavior is described outside the proposal.** Search `kb/reference/` for the reference doc that owns the component. If it already describes the behavior, read that text and confirm it matches the implementation. If it does not, add the description there first, in its own commit, following `kb/reference/COLLECTION.md`. Do not describe shipped behavior only in the proposal.

3. **Move decision-relevant reasoning.** If the proposal weighed alternatives to the shipped choice that the carrying ADR does not record, and that ADR is dated 2026-07-25 or later, add them to its `## Considered alternatives` section, compressed to a paragraph per option. Read `git log --grep='ADR 0NN'` before editing the ADR. If the choice shipped without an ADR, name the implementing commit in step 4 instead.

4. **Narrow the proposal.**
   - Remove the shipped option, its forces, free choices, and adoption criteria.
   - Add a bullet to the current-state anchor: "**Adopted:** {what shipped}, under {ADR or commit}; recorded here rather than proposed below." Update the anchor date to today.
   - Correct any other current-state fact that the adoption made false.
   - Rewrite the description and opening so they name only the open remainder.

5. **Fix inbound references whose context describes the removed part.** Search `rg -n '<proposal-slug>' -g '*.md' kb/` and read each hit. Where a link's context says the shipped part is still open in the proposal, rewrite that context. Leave `kb/work/` and `kb/sources/*.ingest.md` narratives alone; they are dated records.

6. **If nothing undecided remains, stop and switch to [retire an artifact](./retire-artifact.md).**

7. **Commit.** One commit for the proposal edit and the inbound fixes, with a `Decision:` trailer naming the ADR that carries the shipped part.

## Verify

- `commonplace-validate` on the proposal and every edited file: no failures, no link warnings.
- The proposal's description, opening, and adoption criteria mention nothing that `rg` finds implemented.
- The reference doc from step 2 states the shipped behavior without depending on the proposal.

---

Relevant Notes:

- [Design proposal](../reference/types/design-proposal.md) — operates-on: the type whose partially-adopted state this procedure establishes
- [Retire an artifact](./retire-artifact.md) — see-also: the procedure for a proposal with nothing undecided left
