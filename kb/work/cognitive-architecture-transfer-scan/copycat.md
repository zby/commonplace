# Copycat: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

Copycat constructs analogies in small letter-string puzzles. Rather than receiving one fixed representation and searching it, many small stochastic processes—codelets—build and challenge structures in a workspace. A Slipnet of concepts changes activation as the problem develops. Candidate groups, correspondences, and rules compete for support. A temperature-like measure links emerging coherence to randomness: weak organization permits exploration; strong organization increasingly stabilizes a solution.

Copycat's deepest transferable idea is that representation and solution are co-constructed. Which objects correspond, which differences matter, and what rule describes the change cannot always be fixed before reasoning begins.

## Provisional ontology

- **Workspace object/structure:** a provisional representation of the current problem.
- **Codelet:** a small process that notices, proposes, strengthens, weakens, or tests a structure.
- **Slipnet node/link:** a concept and its context-sensitive associative relation to other concepts.
- **Activation:** temporary conceptual relevance that changes which codelets run.
- **Correspondence:** a proposed mapping between objects across situations.
- **Slippage:** a context-supported substitution of one conceptual relation for another.
- **Temperature:** a control signal coupling global coherence to exploratory randomness.
- **Answer:** the result of a mutually supporting interpretation, not merely a retrieved rule.

## Transfer candidates

- **`COPY-1` — let connection discovery build several interpretations.** When relating two notes or systems, propose multiple mappings, each with explicit correspondences and mismatches, before choosing a link or synthesis.
- **`COPY-2` — represent analogy slippage.** A transfer should state which source relation changes meaning in the target. Calling both things "memory," "attention," or "compilation" without a slippage account invites decorative analogy.
- **`COPY-3` — use heterogeneous micro-critics.** Small checks for scope, mechanism, counterexample, provenance, and vocabulary collision can compete and reinforce one another around a draft rather than relying on one monolithic review judgment.
- **`COPY-4` — couple exploration to coherence.** Early discovery should preserve diverse hypotheses; as independent constraints converge, effort should shift toward testing and consolidation. A fixed creativity setting across the whole workflow wastes either breadth or rigor.
- **`COPY-5` — preserve defeated mappings long enough to diagnose ambiguity.** Rival interpretations are evidence about unstable representation even when one ultimately wins.

This architecture is especially relevant to the boundary between lexical connection search and explanatory synthesis: links become useful when a coherent relation is constructed, not when two artifacts share a term.

## Method worth borrowing

Copycat makes intermediate structures observable. For Commonplace, a connection or synthesis process could emit a trace of candidate mappings, supporting relations, counterevidence, confidence changes, and the final selection. Such a trace would let evaluation ask whether the system found the right answer for the right structural reason.

## Non-transfer and failure modes

- Coherence is not truth. A mutually supporting interpretation can be elegant and wrong without external evidence.
- Large numbers of codelet-like calls may be expensive and difficult to reproduce.
- Global temperature can be too coarse; different subproblems may warrant different exploration levels.
- Copycat's carefully designed microworld does not demonstrate that its mechanisms scale to open-ended repositories.

## Grounding questions

1. Which mechanisms are properly Copycat's and which belong to the broader parallel-terraced-scan tradition?
2. How are strength, activation, urgency, and temperature computed and kept distinct?
3. What ablations show that co-construction or slippage is necessary?
4. How does Copycat avoid premature coherent but incorrect interpretations in its task domain?
