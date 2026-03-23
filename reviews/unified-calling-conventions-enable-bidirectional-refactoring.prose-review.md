=== PROSE REVIEW: unified-calling-conventions-enable-bidirectional-refactoring.md ===

Checks applied: 8

WARN:
- [Source residue] The note claims to be about a general architectural principle — "unified calling conventions enable bidirectional refactoring between neural and symbolic" — but the body is tightly coupled to one implementation. Phrases like "`.agent` files," "YAML frontmatter (type signature) plus system prompt (implementation)," "Python functions with type annotations," and the `ticket_classifier` example are all llm-do specifics. The title promises an architectural insight; the body reads closer to an llm-do design document. The "mechanism" section especially has no separation between the general principle and the llm-do instance.
  Recommendation: Restructure so the general mechanism (name-based dispatch, implementation-agnostic interfaces, local refactoring) is stated independently, then llm-do is introduced as "one implementation that demonstrates this" in a clearly scoped section. Alternatively, retitle to make the llm-do scope explicit.

- [Proportion mismatch] The core claim is that unified calling conventions enable bidirectional refactoring. The section that most directly argues this — "Why this matters for constraining" — is roughly equal in length to "The scheduler layer," which addresses an orthogonal concern (imperative vs. declarative orchestration). The scheduler comparison is interesting but doesn't advance the title claim; it's about control-flow style, not calling conventions. It occupies roughly a quarter of the body and dilutes the focus.
  Recommendation: Either trim the scheduler section to a brief remark ("llm-do also uses an imperative scheduler, which means refactoring uses standard code patterns — see [link]") or split it into its own note. The space recovered could develop the bidirectional refactoring argument — particularly the "relaxing" direction, which gets only one sentence in step 4 of the progression.

INFO:
- [Confidence miscalibration] The four-step progression (start neural, observe patterns, codify, extend via relaxing) is presented as a definitive lifecycle: "With unified calling, the progression is smooth: 1. Start neural... 2. Observe patterns... 3. Codify... 4. Extend via relaxing." This reads as an established pattern, but it appears to be the note's own construction synthesized from the constraining and spec-mining notes. It could benefit from a light hedge — "a typical progression" or "one natural path" — to signal it's a proposed model rather than an empirically validated lifecycle.

- [Source residue] The `sanitize_filename()` example in the constraining section ("the agent consistently lowercases and replaces spaces with underscores") is a very specific implementation detail that assumes the reader is working in file-management tooling. It works as an illustration but is presented inline rather than framed as an example. A brief "For instance," before it would make the generality level explicit.

CLEAN:
- [Pseudo-formalism] The only visual formalism is the ASCII diagram (`Agent --calls--> Tool --calls--> Agent --calls--> Tool`) and the comparison table. The diagram clarifies the alternating neural-symbolic chain concisely; the table organizes a genuine four-axis comparison. Neither is decorative — both do structural work that prose alone would handle less clearly.

- [Orphan references] No unsourced numbers, percentages, or empirical claims. All specific references point to other notes in the KB or to the llm-do repository.

- [Unbridged cross-domain evidence] The note stays within the software-engineering and agent-architecture domain throughout. It does not import findings from an unrelated domain without bridging.

- [Redundant restatement] Each section opens with new content. The "Why this matters for constraining" section references the prior mechanism section but does so to extend the argument (friction without unified calling), not to restate it. The "Connection to typed callables" section likewise adds a new dimension (type-theoretic grounding) rather than repeating what came before.

- [Anthropomorphic framing] The note uses "the LLM sees both as callable functions" and "the LLM outputs a string." These are borderline but defensible — "sees" here means "has in its context" and "outputs" is literal. No language attributes beliefs, understanding, or knowledge possession to the model.

Overall: 2 warnings, 2 info
===
