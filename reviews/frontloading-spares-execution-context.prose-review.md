=== PROSE REVIEW: frontloading-spares-execution-context.md ===

Checks applied: 8

WARN:
- [Pseudo-formalism] The PE notation block `[[Ps]](d) = [[P]](s, d)` and the six-row mapping table claim formal grounding, but the note immediately concedes the analogy breaks on all three premises (no exact denotational semantics, only approximate equivalence, different optimisation target). Deleting the equation and reading the surrounding prose: the argument is equally clear — "pre-compute known inputs, insert the result, leave the rest for the LLM." The notation cannot be used to derive a non-obvious consequence or make a quantitative prediction; it is decorative.
  Recommendation: Remove the equation. The mapping table is useful as a conceptual vocabulary bridge — keep it, but drop the formal notation line above it. If the PE framing is to be kept as more than analogy, state the assumptions under which equivalence holds.

- [Proportion mismatch] The core claim is in the title: frontloading spares execution context. The section that carries most weight for that claim — "The context saving" — is a single paragraph (~100 words). The PE mechanism section ("The mechanism: partial evaluation or divide-and-conquer?") including its subsection runs to roughly 350 words plus the table plus the equation. The theoretical framing receives about three times the space of the practical payoff the note is named for.
  Recommendation: Develop "The context saving" with a concrete worked example showing the before/after context cost (the single-line search instruction is gestured at but not fully worked out). Alternatively, consider whether the PE mechanism section belongs in a separate note (e.g., "frontloading-is-partial-evaluation-over-underspecified-instructions") linked from here — that would restore proportions and improve composability.

INFO:
- [Confidence miscalibration] The section "Where the PE analogy stretches" honestly flags the limits, which is good. However, the preceding table and prose present the PE mapping with assertive framing ("That's partial evaluation, not just preprocessing"; "Template variable expansion is textbook PE") before the caveats arrive. A reader scanning the table alone gets unhedged confidence. The hedging is present but structurally late.

- [Source residue] The examples used — "search for X in `kb/notes/`", file listings, CLAUDE.md, skill templates — are all specific to the commonplace/agent-KB domain. The title and opening paragraph claim general applicability to "LLM-based systems," but every concrete illustration is from this specific knowledge-base tooling context. This is mild: the note's tags and context make the domain clear, and the examples are illustrative rather than misleading. Still, a reader arriving from outside the KB methodology might find the generality claim unsupported by the examples.

CLEAN:
- [Source residue] No leaked vocabulary from a prior domain-specific source that contradicts the note's claimed scope. The KB-tooling examples are the note's own domain, not residue from an unrelated source.
- [Orphan references] No unsourced specific numbers, percentages, or named studies. Empirical claims are structural ("execution generates artifacts that persist") rather than quantitative.
- [Unbridged cross-domain evidence] The note's evidence comes from the same domain it targets (LLM instruction systems). The PE analogy is from programming language theory, but the note explicitly bridges it via the homoiconicity argument and then flags where the bridge weakens.
- [Redundant restatement] Sections open with new content. The "Frontloading vs codification" section does revisit the indirection/build-time cases, but to draw a new distinction (determinism is not required), not to restate a prior conclusion.
- [Anthropomorphic framing] The note uses "LLM's judgment," which is borderline, but is used deliberately to distinguish judgment-requiring tasks from pre-computable ones — a functional distinction, not a cognitive claim. No other anthropomorphic language detected.

Overall: 2 warnings, 2 info
===
