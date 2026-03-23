=== PROSE REVIEW: deploy-time-learning-the-missing-middle.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "Deployed AI systems adapt at three timescales, each with a different substrate" presents the note's own proposed taxonomy as established fact. The three-timescale framing is the note's primary intellectual contribution — a way of carving the space — not a consensus classification. The closing paragraph partly acknowledges this ("a synthesis of established practices into a concrete model"), but the opening assertion reads as if the taxonomy is given rather than proposed.
  Recommendation: Hedge the opening to signal that this is the note's proposed framing: "A useful way to think about adaptation in deployed AI systems is across three timescales..." or add a brief acknowledgment that the taxonomy is the note's construction. The closing paragraph's self-awareness about this could be moved earlier or echoed in the opening.

- [Unbridged cross-domain evidence] "Deploy-time learning is double-loop learning for agent systems — constraining revises the rules, not just the outputs" and "Constraining and distillation map to externalization and combination phases" assert structural equivalences between organizational learning theory and agent-system engineering without explaining the shared mechanism that makes the transfer valid. Argyris & Schon studied human organizations with politics, incentive structures, and tacit coordination — why does double-loop learning transfer to an agent revising a prompt file? The SECI spiral involves tacit knowledge embodied in human practice — what is the analogue of "tacit" for an LLM system?
  Recommendation: Add one bridge sentence per analogy stating the shared mechanism: e.g., "Both cases involve a system that can modify its own operating rules rather than just adjusting behavior within fixed rules." If the mapping is looser than equivalence, weaken to analogy ("By analogy with...").

INFO:
- [Proportion mismatch] The Concrete Examples section (~400 words) is the longest section in the note, while the Verifiability Gradient section (~250 words) — which carries the note's core analytical contribution — is shorter. The examples are well-constructed and serve the note, but the gradient concept itself gets relatively thin treatment. The description of what makes each grade *different in kind* (not just in degree) from the one above it could be developed further.

- [Orphan references] "Argyris & Schon, 1978" and "Nonaka & Takeuchi, 1995" appear without source links. The note's own TODO (line 92) flags this: "The organizational learning and knowledge creation citations are from the agent's training data, not systematic." This is a known gap, not an oversight — noting it here for completeness.

CLEAN:
- [Source residue] The note claims generality across deployed AI systems. Domain-specific terms (Commonplace, repo-hosted artifacts, the examples directory) are explicitly framed as instances of the general pattern, not leaked assumptions. The LLMOps vocabulary (prompts, evals, CI) matches the note's domain.

- [Pseudo-formalism] The note uses tables to organize distinctions (timescales, verifiability grades). Both tables carry information not present in the surrounding prose — removing them would lose the structured comparison. No decorative notation.

- [Redundant restatement] Each section opens with new content. The Verifiability Gradient section starts with the Karpathy quote (new framing), not a recap of Three Timescales. The Concrete Examples section points directly to the examples directory. No restating paragraphs detected.

- [Anthropomorphic framing] "the LLM stays focused on what requires judgment" is mildly agentive but contextually clear and consistent with the note's framing of LLMs as components in a system. No instances of "possesses," "understands," or "believes."

Overall: 2 warnings, 2 info
===
