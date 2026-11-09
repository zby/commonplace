---
description: Resolve, reject, or supersede a pending full-pass packet — a revise, delete, merge, rehome, undetermined or hand-back result of commonplace-review run full-pass
type: types/instruction.md
---

# Resolve a full-pass disposition

Use this procedure when a note's current packet under `kb/reports/state/review/packets/` has `resolution: pending`. The [full improvement pass](./run-full-improvement-pass-on-note.md) writes it, one current packet per note, at `kb/reports/state/review/packets/<note-path>`. A pending packet blocks a new pass over the same note text until it is resolved or the note changes.

Inputs:

- `{packet-path}` — the packet, or `{note-path}`, whose packet path follows from it.
- explicit user decision when accepting, rejecting, or applying an alternative. Agents may mark `superseded` only from a changed-input result of the check below.

## Inspect and check

1. Read the full packet: its `note`, `disposition`, `update`, `merge-target`, `closing-status`, the body's rationale, and the current `resolution`. Stop if it is not `pending`.
2. Run `commonplace-validate {packet-path}`. A validation failure blocks resolution.
3. Run `commonplace-review packet {packet-path}` immediately before recording a rejection or beginning any filesystem mutation. It compares the note with `final-sha256` (the text the pass left: the start text for every pending packet) and a merge target with `merge-target-sha256`.
4. Interpret the JSON and exit status:
   - Exit 0, every input `matching`: the decision may proceed.
   - Exit 1 with any `missing` input: leave `resolution: pending` and reconcile, whatever the other inputs report. Absence cannot prove a delete, merge, or rehome succeeded.
   - Exit 1 with `changed` inputs and no missing input: preserve every live artifact and resolve the packet to `superseded` with `resolution-authority: version-guard`. State which paths changed. Do not accept, reject, or apply an alternative.
   - Exit 2: leave the packet unchanged and repair the invocation or the packet.

## Resolve a matching recommendation

Proceed only with an explicit user decision:

- **Accept revise.** The packet's Revision brief names the objection, candidate replacement claims with their mode guards, and the citer scope. The author revises the note under the notes contract — retitling, renaming with `commonplace-relocate-note`, and reconciling inbound citers' link text and summaries as the brief's scope requires — or writes a different repair that meets the objection. The candidate claims are suggestions; adopting one is not required. Run `commonplace-validate` on every touched artifact. Record `accepted` with the note's surviving path (and any relocated path) in `resulting-paths`. A new full pass on the revised note starts from its new text.
- **Accept delete.** Delete only `note`. Verify it is absent and that no unintended path changed. Then record `accepted`; `resulting-paths` is empty.
- **Accept merge.** Reconcile the note into the live `merge-target` as a semantic edit, update affected backlinks as needed, remove invalid `user-verified` attestation from the edited target, and delete the note only after the target contains the accepted result. Verify the note is absent, the target exists at the recorded path, and validation succeeds. Record `accepted` with the target in `resulting-paths`. Do not substitute `commonplace-relocate-note` for semantic reconciliation.
- **Accept rehome.** The packet's Disposition names the target collection and whether the remedy is a whole move or a split. For a **whole rehome**, move the note to the target collection with `commonplace-relocate-note` (which rewrites inbound link paths and the redirect map), retype the note's `type:` frontmatter to the target collection's type, and revise it to fit the target's text contract. For a **split**, first author the extracted transferable claim as a new note in the origin collection, then rehome the operational remainder as above. In both cases update inbound citers' visible link text and summaries, remove invalid `user-verified` attestation from any edited artifact, and run `commonplace-validate` on every touched artifact. Record `accepted` with every surviving path in `resulting-paths`.
- **Answer an undetermined update.** A `keep` packet with `update: undetermined` asks one focused question in its Open items. Do not resolve it here: resume its run with `commonplace-review run full-pass {note-path} --resume <run> --direction "<the user's answer>"`, which decides the packet again and replaces it.
- **Accept a hand-back.** A packet with `closing-status: hand-back` restored the start text. The author decides what the closing record asks for and edits the note, or records why not. Record `accepted` with the note's path in `resulting-paths`.
- **Reject.** Leave the note and target byte-identical. Record `rejected` with every checked live path in `resulting-paths` and explain why the recommendation was declined.
- **Apply an alternative.** Perform only the user-authorized alternative, verify every resulting path and validate each edited artifact, then record `alternative-applied` with all surviving result paths. An opposite-direction merge is an alternative, not acceptance of the original merge.

Never record a terminal state before its filesystem postconditions succeed. If mutation succeeds only partly, leave the packet pending and reconcile the ambiguous state.

## Record the resolution

Change only the resolution fields of the packet's frontmatter:

```yaml
resolution: accepted | rejected | alternative-applied | superseded
resolved-at: "<UTC ISO-8601 timestamp>"
resolution-authority: user | version-guard
resolution-summary: <what happened>
resolution-rationale: <why>
resulting-paths: [<every surviving path left by the resolution>]
```

Use `user` only for accepted, rejected, or alternative decisions. Use `version-guard` only for supersession caused by a changed input. Run `commonplace-validate {packet-path}` after recording. Keep the packet while a rejection or alternative remains load-bearing; never delete a pending packet. A later pass over the note replaces its current packet; the earlier one stays in its run directory.
