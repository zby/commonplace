# Soar: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

Soar is a general symbolic cognitive architecture organized around working memory, production memory, operators, and a decision cycle. Productions elaborate the current state, propose and evaluate operators, and apply the selected operator. When knowledge is insufficient to choose or apply an operator, an impasse creates a substate in which further problem solving occurs. Chunking can compile the result of that substate into a production whose conditions capture the relevant prior context, allowing similar future impasses to be resolved directly. Later Soar includes semantic and episodic memory, reinforcement learning, and other subsystems.

The strong transferable pattern is **impasse-driven learning**: inability to proceed creates a scoped problem-solving context, and a successful resolution becomes a candidate fast path for the conditions that caused the impasse.

## Provisional ontology

- **Working-memory element:** symbolic current-state structure.
- **Production:** condition-triggered elaboration or action knowledge.
- **Operator:** a proposed transformation of the current state.
- **Preference:** information used to compare or select operators.
- **Decision cycle:** elaboration, proposal/evaluation, selection, and application dynamics.
- **Impasse:** failure of available knowledge to determine the next operation.
- **Substate:** a new problem context created to resolve an impasse.
- **Result:** information returned from substate reasoning to the parent state.
- **Chunk:** a learned production summarizing the dependencies of the result.

This ontology distinguishes uncertainty about **what to do** from failure while doing it. Different impasses—no candidate, tie, conflict, or inability to apply—should generate different learning opportunities.

## Transfer candidates

- **`SOAR-1` — type agent impasses.** Record whether a loop lacks a procedure, has conflicting procedures, cannot evaluate options, lacks information, or cannot execute the chosen action. "Got stuck" is too coarse for improvement.
- **`SOAR-2` — open a scoped work surface at the impasse.** A workshop or investigation should preserve the parent goal and the exact unresolved condition so that its resolution can return as a usable result rather than an unrelated essay.
- **`SOAR-3` — compile the dependency, not the whole trace.** Promotion should capture the minimal conditions that made the resolution valid. Copying every intermediate step creates brittle and overspecific fast paths.
- **`SOAR-4` — require a verified result before chunking.** A completed subproblem can still be wrong. The proposed production, skill, or rule should pass the appropriate deterministic or semantic check before becoming operative.
- **`SOAR-5` — keep fallback and explainability after compilation.** A fast path needs scope conditions and a route back to general reasoning when conditions fail, reinforcing the existing [two-layer execution-system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md).
- **`SOAR-6` — separate operator proposal, evaluation, and application.** This maps cleanly onto the [proposal-selection improvement loop](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and prevents generation from grading itself implicitly.

## Method worth borrowing

Build an **impasse corpus** from real agent traces. Label the state, available operators, missing decision knowledge, subproblem, resolution, verification, and later recurrence. Evaluate whether learned fast paths fire on genuine repeats, abstain on near-neighbors, reduce cost, and preserve correctness after source changes.

## Non-transfer and failure modes

- Chunking can learn overly general rules from incomplete dependency analysis.
- Symbolic working memory may not capture decisive latent or textual context without lossy extraction.
- Turning every hesitation into a persistent artifact creates noise; recurrence or consequence must justify promotion.
- A uniform operator ontology can force unlike activities into one control scheme.
- Later Soar's many subsystems should not be imported merely to complete an architecture diagram.

## Grounding questions

1. What impasse types and substate semantics are canonical in current Soar?
2. How does chunking determine the conditions on a learned production?
3. What mechanisms prevent overgeneralized or incorrect chunks?
4. How do semantic, episodic, and reinforcement learning interact with the decision cycle?
