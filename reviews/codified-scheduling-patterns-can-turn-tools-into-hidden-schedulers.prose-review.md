=== PROSE REVIEW: codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim — that embedding scheduling patterns in tools creates hidden schedulers and that this is architecturally wrong — receives its full argument in a single dense final paragraph ("This works, but it is not where codified scheduling wants to live. Once next-step policy has stabilized enough to become code..."). The setup distinguishing ordinary tools from scheduling patterns (three paragraphs plus a four-item bullet list) is substantially longer than the payoff explaining *why* the disguise is harmful and *what* the alternative is. The consequence paragraph does a lot of work in a small space: it names the problem (masquerading control logic), identifies the missing primitive (explicit control logic / progression), and attributes the cause (framework that offers tools but not progression). Any one of those deserves development.
  Recommendation: Expand the consequence section. The note currently tells the reader that tools-as-schedulers are wrong but compresses the reasoning into one paragraph. Developing the "why" — what breaks when scheduling hides inside a tool (observability, composability, override) — would bring proportions in line with the claim's weight.

INFO:
- [Confidence miscalibration] The note proposes its own distinction (capability-internal steps vs. next-step policy) and presents it with assertive framing: "Scheduling patterns are different," "it is not where codified scheduling wants to live," "the application needs to replace model-chosen transitions with explicit control logic." These read as established design principles rather than a proposed framework from a seedling note. The assertive voice is common and arguably appropriate for architectural argument, but a reader could mistake the note's own taxonomy for an inherited one.
- [Anthropomorphic framing] Two phrases attribute intention or agency to abstractions: "codified scheduling wants to live" and "forces that control logic to masquerade as tool implementation." These are stylistic rather than substantive — no reader will think the code literally wants something — but they introduce mild imprecision where the note is otherwise technically careful. "Masquerade" in particular implies intentional deception rather than structural misfit.

CLEAN:
- [Source residue] The note's claimed domain is agent frameworks and tool-loop architecture (tags: computational-model, context-engineering, tool-loop). All examples — editing/testing workflows, feature decomposition, retry-with-narrower-context, `run_feature_workflow` — belong to that domain. No vocabulary from a narrower source domain leaks through.
- [Pseudo-formalism] No formal notation, equations, or variable definitions present. The argument is carried entirely by prose and concrete examples.
- [Orphan references] No specific figures, percentages, named studies, or empirical claims appear. All claims are architectural arguments from the note's own reasoning.
- [Unbridged cross-domain evidence] No cross-domain citations. All evidence is drawn from agent/tool design, which is the note's own domain.
- [Redundant restatement] The note has no section headings, but each paragraph advances the argument: codification intro, ordinary tools, boundary clarification, scheduling patterns (with examples), hidden scheduler mechanism, architectural consequence. No paragraph restates a prior paragraph's conclusion as setup.

Overall: 1 warning, 2 info
===
