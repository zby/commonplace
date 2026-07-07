# Compression Bundle Review: Full identity keys decouple a batch protocol from its packing axis

**Target:** `kb/notes/full-identity-keys-decouple-a-batch-protocol-from-its-packing-axis.md`
**Bundle:** `kb/work/agent-note-improvement/compression/`

## Overall Result

WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS | The claim ("full-identity keying decouples the wire protocol from the packing axis") is stated in the title and made explicit and prominent by the second paragraph's opening sentence; the first paragraph is minimal necessary setup (the problem the claim answers), and later sections (why-it-matters, scope, open question) stay subordinate to it. |
| compression/branch-bloat | PASS | The "Why this matters more" section is a bounded contrast (old wisdom in deterministic batch APIs vs. probabilistic LLM parsing) that strengthens rather than dilutes the claim; the Scope section is a necessary boundary, not a tangent; the one Open Question is already correctly rehomed rather than argued in the body. No branch needs removal or relocation. |
| compression/detail-overhang | PASS | The three-system list (JSON-RPC, GraphQL, map-reduce) is compressed into a single clause rather than expanded per-example; the mechanism explanation (coverage checking, ordering, failure attribution) is proportionate to the work of making an abstract claim concrete. Nothing has outgrown its role. |
| compression/marginal-value-redundancy | WARN | The final sentence of paragraph 2 restates the immediately preceding sentence rather than adding new content; see finding below. |

## Findings

### compression/marginal-value-redundancy

- WARN: In paragraph 2, the sentence "Batching becomes a **policy** choice made by the caller — which axis, how many units per call, whether axes mix — instead of a **protocol** choice baked into the wire format." already establishes that grouping strategy (including mixing axes) is now a free caller choice unconstrained by the protocol. The following sentence, "A new axis, or an arbitrary mix of axes, becomes expressible for free once the grammar already carries full identity; no format change is needed to add it," restates the same policy-vs-protocol point in different words without adding a new premise, boundary, or example — "no format change is needed" is simply the entailment of "instead of a protocol choice baked into the wire format" from the sentence just before it. Recommend folding: cut the second sentence, or compress it to a short clause appended to the first (e.g., "...instead of a protocol choice baked into the wire format — so a new axis, or a mix of axes, needs no format change to add.").

## Suggested Revision

Keep the note's structure and all four sections as-is — the title-claim placement, the LLM-specific "why it matters more" contrast, and the Scope/Open-Questions material are all earning their space. The only edit needed is in paragraph 2: merge or cut the closing sentence ("A new axis, or an arbitrary mix of axes, becomes expressible for free...") since it restates the policy-vs-protocol distinction already made in the sentence immediately before it. This is a one-sentence trim, not a structural change.

## Disposition

Applied directly: folded the redundant closing sentence of paragraph 2 into the preceding sentence as a short trailing clause, per the suggested revision. Re-ran `commonplace-validate` after the edit.
