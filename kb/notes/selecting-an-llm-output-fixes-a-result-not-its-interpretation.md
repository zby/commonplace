---
description: "Selecting one LLM output for operative reuse creates a stable artifact-testing target without resolving ambiguity inside the text, so generator and artifact tests answer different questions"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining]
---

# Selecting an LLM output fixes a result, not its interpretation

*Conceptual claim. The distinction between testing the generator and testing the selected artifact follows from the selection boundary. Whether exploiting that distinction improves outcomes is empirical.*

LLM output can vary for two distinct reasons. A natural-language prompt may admit several valid interpretations, and one inference configuration may produce different renderings across runs. [Semantic underspecification belongs to the instruction, while execution indeterminism belongs to the sampling process](./agentic-systems-interpret-underspecified-instructions.md).

Selecting one output for reuse directly settles result identity. Alternative completions cease to be candidates for that consumption path; persisting and versioning the selected output fixes the bytes that later consumers receive. This is a [commitment](./commitment-not-derivation-creates-new-ground-truth.md) to a result, not proof that the text expresses a unique interpretation. The selected artifact may still admit several legitimate readings.

For this distinction to matter operationally, selection must be connected to reuse. An audit log may preserve every completion without preferring one. A selected artifact becomes consequential only when a [behavioral-authority path](./definitions/behavioral-authority.md) gives it a consumer, a channel, and force. For example, generating several configuration patches, accepting one after evaluation, and making later runs load that version fixes a result for those runs. Archiving every candidate preserves records but selects nothing.

Selection participates in [constraining](./definitions/constraining.md) when adoption excludes interpretations carried only by rejected candidates or gives one resolution downstream force. It does not remove ambiguity that remains inside the selected text; fixed bytes alone do not meet that semantic test.

## Two testing targets

Once a result is selected and made operative, it becomes a stable testing target distinct from the process that generated it:

1. **Generator testing:** Across repeated runs and representative inputs, does the prompt and inference setup produce an acceptable distribution of outputs? This tests the generator's range of interpretations, renderings, and failures.
2. **Artifact testing:** Does this selected output satisfy its structural, semantic, and corpus-level contract? This tests the stable product that later consumers will receive.

Neither test substitutes for the other. A generally reliable generator can still produce a bad sample, while a good artifact says nothing about what another run will produce. Artifact checks can also serve as a selection gate when they are sufficiently discriminative, timely, and economical. Weak or delayed [oracles](./oracle-strength-spectrum.md) cannot support the same candidate-filtering strategy.

## Boundary

- Persistence preserves a result; it does not choose among candidates.
- Selection chooses the result for a consumption path; it does not remove ambiguity inside that result.
- Behavioral authority makes the choice affect later behavior.
- Selection counts as learning only when evidence bearing on an improvement objective drives the choice and operative retention carries it into later behavior, as in a [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: separates persistence from the read-back and activation needed for a selected result to affect later action
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: explains why the accepted result, rather than its prompt, becomes the maintained record for choices the prompt did not determine
- [Automated tests for text](./automated-tests-for-text.md) — extends: supplies a concrete deterministic, rubric, and corpus testing pyramid for selected text artifacts
- [A retained instruction preserves what testing selected](./a-retained-instruction-preserves-what-testing-selected.md) — extends: develops the claim for a procedure selected under a criterion and retained for reuse
