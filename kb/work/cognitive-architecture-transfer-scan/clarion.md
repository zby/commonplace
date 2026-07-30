# CLARION: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

CLARION is a hybrid architecture organized around an explicit/implicit distinction. I remember a symbolic top level containing rules and chunks and a subsymbolic bottom level containing distributed action values or associations. Both levels can contribute to action. Learning can move bottom-up by extracting explicit rules from effective implicit behavior and top-down by training or shaping implicit competence from explicit knowledge. Broader presentations also distinguish action-centered, non-action-centered, motivational, and metacognitive subsystems.

The main transferable idea is not simply "hybrid is good." It is that explicit and implicit competence have different strengths, can disagree, and require an arbitration and translation account.

## Provisional ontology

- **Explicit representation:** inspectable rule or chunk that can be deliberately applied and reported.
- **Implicit representation:** distributed competence expressed through graded behavior without a complete verbal rule.
- **Action-centered knowledge:** state-to-action competence.
- **Non-action-centered knowledge:** general factual or associative knowledge.
- **Motivational state:** goals or drives that alter what is valuable.
- **Metacognitive control:** processes that regulate learning, selection, or reasoning.
- **Bottom-up extraction:** formation of an explicit approximation from implicit success.
- **Top-down assimilation:** influence of explicit rules on implicit behavior.

For Commonplace, natural-language knowledge, symbolic enforcement, and distributed-parametric model behavior do not map one-to-one onto these levels, but CLARION warns against treating their outputs as interchangeable merely because they concern the same task.

## Transfer candidates

- **`CLARION-1` — govern translations between representational forms.** When repeated LLM behavior becomes a written instruction or validator, record what evidence was compressed, what exceptions were lost, and how the artifact will be tested. Rule extraction is a lossy model-building act.
- **`CLARION-2` — retain parallel paths during incomplete codification.** An explicit fast path and a general model fallback can co-execute while coverage remains incomplete, matching the current [two-layer execution-system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) account.
- **`CLARION-3` — test agreement and complementarity separately.** A written rule and model judgment may agree because both are right, because one dominates the other, or because they share the same blind spot. Evaluation should include disagreement cases and unique wins.
- **`CLARION-4` — separate competence from control.** Knowing how to perform an operation is distinct from deciding when to invoke it, how much effort to spend, and whether to learn from the result. Skills, routing, and improvement policy should remain separately inspectable.
- **`CLARION-5` — allow relaxation as well as codification.** If an explicit rule becomes brittle, evidence can justify returning some decisions to judgment rather than only accumulating more rules. This fits [codification and relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md).

## Method worth borrowing

A useful evaluation crosses representation and learning direction: implicit-only, explicit-only, both, explicit extracted after experience, and explicit supplied before experience. Measuring where each condition helps would reveal whether a new instruction actually transfers competence, merely restates behavior, or interferes with the model's stronger path.

## Non-transfer and failure modes

- Equating an LLM's weights with CLARION's bottom level is only a rough analogy.
- Explicit artifacts are not necessarily more correct, and implicit behavior is not necessarily less explainable.
- A two-level story can hide important differences among prose advice, binding instructions, code, schemas, and tests; [representational form](../../notes/definitions/representational-form.md) remains finer-grained.
- Bidirectional learning can create circular confirmation unless evidence and evaluation remain external to both paths.

## Grounding questions

1. What are the precise top-level and bottom-level representations in CLARION?
2. How does the architecture combine their action recommendations?
3. Under what conditions are rules extracted, refined, or deleted?
4. What roles do the motivational and metacognitive subsystems play in learning control?
