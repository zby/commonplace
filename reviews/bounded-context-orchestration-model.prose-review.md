=== PROSE REVIEW: bounded-context-orchestration-model.md ===

Checks applied: 8

WARN:
- [Pseudo-formalism] The formal notation in "The select/call loop" section (`K`, `t`, `M`, `||P||_t`) introduces variable names and a cost measure `||·||` that cannot support quantitative prediction or derivation. The pseudocode `while not satisfied(K): P = select(K); r = call(P); K = K + r` is clear, but the surrounding notation — particularly the norm `||P||_t <= M` with "normalized effective-cost units" — dresses up a qualitative argument (prompts should fit in context and be tuned to task difficulty) in formal clothing. Deleting the notation and keeping only the pseudocode and prose leaves the argument equally precise. The two-paragraph explanation of what `K` "can be read as" (minimal vs. materialized) is itself evidence that the formalism is not pinning anything down — it accommodates both readings, which means it constrains neither.
  Recommendation: Keep the pseudocode loop (it is genuinely useful as a reference structure). Remove or drastically simplify the `||P||_t <= M` apparatus. The prose sentence "select must build a prompt that fits the context budget and is framed for the task type" says the same thing. If the norm notation is retained for the paper outline, flag it here as forward reference rather than presenting it as load-bearing within this note.

- [Confidence miscalibration] The note presents its own proposed framework — the two-component architecture and the select/call loop — using assertive language throughout. "Together these imply a natural architecture" (line 13), "The model has two components" (line 17), "This is where the scheduling difficulty lives" (line 41). The note's status is `seedling`, and the model is the note's own construction (not cited from a source). Despite this, no section flags it as a proposed decomposition. The "Scope and open questions" section at the end acknowledges limits but frames them as open problems within the model, not as uncertainty about the model itself.
  Recommendation: Add a brief epistemic-status marker early — something like "This note proposes a model..." or "One way to formalise this separation is..." — so the assertive language in subsequent sections reads as development of a proposal rather than reporting of established architecture. The seedling status in frontmatter does not substitute for in-prose hedging because readers encounter the prose first.

INFO:
- [Source residue] The "canonical note-selection example" (line 67) uses the specific scenario of analysing a set of notes that exceed a context window. This is close to the note's own domain (knowledge-base orchestration), so it is not cross-domain residue in the usual sense. However, the example's specificity — "notes," "relevance labels," "cluster summaries" — means a reader working on a different orchestration task (e.g., multi-step code generation, dialogue management) has to do the mapping themselves. This is borderline; the example is explicitly labelled as an example, which is the right framing.

- [Proportion mismatch] The section "Realising the model with SDKs and tool calling" (lines 105-122) is roughly 18 lines of body text. The section "What makes selection hard" (lines 57-64), which is arguably more central to the note's title claim about why bounded-context orchestration is a meaningful model, is only 8 lines of body text. The SDK/tool-calling section develops a secondary implication (compatibility with existing tooling) at greater length than the section that carries the core intellectual contribution (why selection is hard). The tool-calling discussion also overlaps substantially with the linked tool-loop-index note.
  Recommendation: Consider whether the SDK/tool-calling section could be shortened to a paragraph with a forward link to the tool-loop-index note, freeing space to develop "What makes selection hard" further — particularly the MDP analogy, which is asserted but not developed.

CLEAN:
- [Anthropomorphic framing] The note consistently uses precise language for LLM behavior: "LLM calls handle only the semantic judgments," "the model can return a request," "the sub-agent's stochastic interpretation." No instances of "understands," "knows," "believes," or similar anthropomorphic verbs applied to the model. The term "sub-agent" is used as a role label for the bounded call, not as an attribution of agency.

- [Orphan references] No unsourced empirical claims, specific numbers, percentages, or named studies appear without citation. The three sources listed at the end are referenced in context. The note avoids making empirical claims that would require grounding.

- [Unbridged cross-domain evidence] The note does not import evidence from outside its own domain. The cited sources (ConvexBench, MAKER, Anatomy of an Agent Harness) are all from the LLM/agent-systems domain, matching the note's domain. No cross-domain transfer claims are made.

- [Redundant restatement] Section openings introduce new material. "The select/call loop" opens with notation, not a recap of the model section. "What makes selection hard" opens with a new framing (optimisation lives in select), not a restatement. "Realising the model with SDKs and tool calling" opens with a new claim (compatibility with SDKs), not a recap. No redundant restatement detected.

Overall: 2 warnings, 2 info
===
