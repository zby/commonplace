---
gate_id: semantic/load-bearing-qualifiers
name: Load-bearing qualifiers
description: 'A claim is narrower than its argument requires because a qualifier, precondition, or scope restriction appears in the title, description, or proof without doing work in the reasoning.'
type: kb/types/review-gate.md
lens: semantic
watches: [title, description, body]
staleness: changed
requires_trait: title-as-claim
---

## Failure mode

A claim is narrower than its argument requires because a qualifier, precondition, or scope restriction appears in the title, description, opening claim, or proof without doing work in the reasoning. The note may still be true, but its reach is artificially limited: readers inherit an unnecessary assumption, downstream notes cite the narrower form, and later cleanup has to rename or rewrite the claim.

One common version is **usage-fit narrowing**: the note states a claim in the exact shape needed by one downstream use even though the reasoning proves a broader claim. A broader theorem can serve a special case; the special-case condition should become a corollary, consequence, scope note, or application paragraph, not an unnecessary assumption in the central claim.

Common signals include adjectives such as "finite", "deterministic", "symbolic", "external", "complete", "stable", or "typed" in a claim statement when the proof never uses the corresponding property.

Special case: LLM-specific wording may be intentional domain scoping. Report INFO, not WARN, when the proof could generalize beyond LLM calls but the note is plainly scoped to LLM orchestration. Report WARN only when the note's central purpose is to establish the broader execution-class theorem and the LLM wording obscures that broader claim.

## Test

For each central claim:

1. Extract the qualifiers, preconditions, and scope restrictions from the title, description, opening claim, and main proof.
2. For each one, ask where the central reasoning uses it. Look for a proof step, example boundary, counterexample, or explicit dependence inside the argument for the main claim.
3. Distinguish theorem support from application support. If the qualifier is needed only to make a consequence, downstream use, target model, or linked application fit, it is not load-bearing for the central claim.
4. Try the deletion test: remove the qualifier and restate the claim. If the argument for the central claim still goes through unchanged, the qualifier is not load-bearing even if a later special-case consequence needs it.
5. Check placement. If the qualifier is needed only for one downstream application, move it to a corollary, consequence, scope note, or linked application note rather than keeping it in the general claim.
6. Preserve true boundaries. If removing the qualifier creates a false central claim or loses an important counterexample boundary, the qualifier is load-bearing and should stay.

WARN when a non-load-bearing qualifier narrows the central claim or filename-level title. INFO when the qualifier is probably unnecessary but the reviewer cannot determine whether a hidden boundary case depends on it, or when the specific qualifier is intentional LLM-domain scoping.
