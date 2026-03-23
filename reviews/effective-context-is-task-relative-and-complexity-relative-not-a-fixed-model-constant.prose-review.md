=== PROSE REVIEW: effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md ===

Checks applied: 8

WARN:
- [Pseudo-formalism] The notation `||P||_t ≤ M` appears twice (body and open questions as `||·||_t`) but does no formal work. The variables are not defined (what is P? what is M? what does the subscript t range over?), no assumptions are stated, and no quantitative prediction or derivation follows from the expression. The surrounding prose — "the cost norm depends on what you're asking the model to do" — carries the full argument without the notation. Deleting the formula and writing "the effective cost of a prompt depends on the task" would lose nothing.
  Recommendation: Remove the notation and let the prose carry the claim. If the formalism is meant to connect to the bounded-context orchestration model's own notation, add a sentence stating that and defining the terms here, or link to where they are defined.

- [Confidence miscalibration] The phrase "In the interpretation developed here, they are two dimensions along which prompts consume bounded effective budget" presents the note's own synthesis as a discovered fact rather than a proposed framing. The note's caveats section correctly hedges ("The claim should stay qualitative"), but the main body uses unhedged language for what is the note's own interpretive construction, not a finding from either source.
  Recommendation: Flag the synthesis as proposed in the body where it first appears. A phrase like "On this interpretation" or "A natural reading is that" would match the epistemic status the caveats section already acknowledges.

INFO:
- [Source residue] The note is pitched at a general level (effective context as a property of model-task pairs), and most of its language stays there. However, the phrase "recursive steps get focused local frames" in the ConvexBench paragraph is fairly domain-specific to symbolic/mathematical reasoning without being flagged as such. A reader unfamiliar with ConvexBench may not know what "recursive steps" or "focused local frames" mean concretely. This is mild — the note does name ConvexBench — but the phrasing reads more like a summary of the paper's mechanism than like a claim at the note's generality level.
  Recommendation: Either briefly gloss the mechanism ("when recursive sub-problems are isolated into separate prompts") or frame it as domain-specific ("in ConvexBench's symbolic tasks, performance recovered when...").

- [Proportion mismatch] The core synthesis — that effective context is relational and should be treated as a task-shaped cost measure — is compressed into a single paragraph (the one beginning "The synthesis is"). The two source summaries each get their own paragraph of comparable length. The most original contribution of the note (the relational framing and its connection to the bounded-context orchestration model) is thinner than the setup. This is not severe because the note is concise overall, but the balance slightly underweights the note's own contribution.
  Recommendation: Consider expanding the synthesis paragraph by one or two sentences to develop why the relational framing is preferable to parameterized-scalar alternatives, beyond "weaker and cleaner."

CLEAN:
- [Orphan references] All specific claims are attributed. The "5,331 tokens" figure is traced to ConvexBench with a citation. The "11 frontier models" figure is traced to Paulsen. No floating numbers or uncited empirical claims.
- [Unbridged cross-domain evidence] Both sources are from the LLM evaluation domain, and the note's claims are about LLMs. No cross-domain transfer is attempted. The evidence and the claims live in the same domain.
- [Redundant restatement] The note is compact (four substantive paragraphs plus caveats and open questions). No section reopens by restating a prior section's conclusion. Each paragraph advances a distinct point.
- [Anthropomorphic framing] The note uses "handle," "fail," and "use" for model behavior, which are standard operational language. No verbs implying mental states ("understands," "believes," "knows") appear.

Overall: 2 warnings, 2 info
===
