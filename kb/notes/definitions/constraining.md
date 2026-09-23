---
description: Definition — constraining commits choices in a retained artifact so its consumer treats fewer readings or behaviors as valid; natural-language constraining biases the interpreter, codification excludes readings
type: kb/types/definition.md
tags: [learning-theory, constraining]
---

# Constraining

Constraining is committing choices in a retained artifact so that its consumer treats fewer readings or behaviors as valid. This KB calls the set of valid readings the artifact's **interpretation space**; constraining narrows it. When a retained constraint improves the system's capacity to act, constraining is learning in [Simon's sense](../learning-is-not-only-about-generality.md): one of the main ways a deployed system learns without weight updates. A change that only makes an artifact easier to find, shorter, or more useful is not constraining unless some reading that was valid before is now invalid or dispreferred.

Interpretation space depends on the consumer. Natural language [admits several valid readings](../agentic-systems-interpret-underspecified-instructions.md), and a model or human picks one on each use, so the same convention leaves a different interpretation space for a weaker model, a stronger model, and a human reader. How constrained an artifact is should be stated for a named consumer. Reliability, speed, cost control, and reviewability may follow from constraining, but they are consequences rather than the definition.

## Scope

Use the term when an artifact, convention, type, validation rule, or implementation narrows a named consumer's interpretation space. The test is semantic: some reading that was plausible before the change is now invalid or dispreferred.

Constraining can narrow three things, and one artifact can narrow more than one:

- **content** — what the artifact means: which reading of a term, rule, or instruction is valid;
- **activation** — when a requirement applies: which events or situations invoke it;
- **response** — what counts as satisfying it: which outputs or actions are accepted.

[Methodology enforcement](../methodology-enforcement-is-constraining.md) treats activation and response as independent axes. The narrowing need not happen inside the original artifact: when a spec's common interpretation is extracted into a function, the spec admits the same readings as before, but the function has replaced it for that operation.

Common KB instances:

- definition notes that replace vague terms with operational meanings;
- title conventions that require a note to state a claim rather than name a topic;
- structured sections that assign meaning to positions in a document, such as scope, exclusions, and misuse cases;
- schemas, validators, and scripts that give one reading formal consequences;
- hooks and required gates that fix when a rule applies.

## Two regions: biasing and excluding

The [representational form](./representational-form.md) of the committed choice determines how strongly it constrains.

**Natural-language constraining** — definitions, title conventions, structured sections, worked examples, review criteria — biases the interpreter. The consumer is still a model or human who can find another reasonable reading, so disfavored readings become less likely but remain possible.

**[Codification](./codification.md)** — schemas, validators, route tables, deterministic code — excludes readings. The artifact has a unique operational semantics, so readings outside the committed one are rejected rather than disfavored. Codification is constraining that crosses from natural-language into symbolic form, not a separate mechanism.

Many constraints never need to cross. A definition note narrows a term's meaning and stays natural language.

## Exclusions

Constraining is not lineage. Whether an artifact was adapted from recorded source material is carried by the [lineage](./lineage.md) labels (`adapted-from`, `operationalized-from`, `derived-from`, `abstracted-from`). The two vary independently: a route table can be frozen with no source behind it, and a skill can be derived from methodology notes while staying as underspecified as they were.

Constraining is not retrieval or navigation. A description field, index entry, or backlink may help an agent find the right artifact, but it is constraining only when it also narrows what the artifact means.

Constraining is not always enforcement. A convention, example, or inline gloss can constrain interpretation without any runtime enforcing it.

Constraining is not automatically an improvement. A constraint can freeze the wrong proxy theory, overfit a narrow case, or block useful generality.

Constraining is not result selection. [Retaining one LLM output](../selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) fixes which result exists, not how later consumers read it.

## Misuse Cases

- Calling every improvement constraining. A change that adds information or makes an operation easier is not constraining unless some reading becomes invalid or dispreferred.
- Treating constraining as synonymous with codification. Codification is only the region where the artifact has a unique operational semantics.
- Treating a natural-language constraint as an exclusion. "The convention forbids X" does not mean X cannot happen; only codification rules readings out.
- Stating how constrained an artifact is without naming the consumer.

## Trade-off and relaxing

Constraining [trades generality for reliability](../constraining-and-extraction-both-trade-generality-for-reliability.md): a committed reading is more predictable, but it handles poorly the cases the commitment did not anticipate. That trade makes the direction of change a design decision.

**Relaxing** is the reverse: replacing a constrained component with a more general one so interpretation space reopens. It is warranted when the committed reading turns out to be a wrong proxy, or when a more capable consumer handles the general case well enough. See [codification and relaxing navigate the bitter-lesson boundary](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and [operational signals that a component is a relaxing candidate](../operational-signals-that-a-component-is-a-relaxing-candidate.md).

## Prior analogues

Gradual typing, formal specification, and ontology engineering each narrow interpretation in their own medium. Carnap's explication narrows a concept's meaning; the [definition type](../../types/definition.md) follows it, so every definition note is an instance of natural-language constraining.

---

Relevant Notes:

- [codification](./codification.md) — defined-in: the symbolic region of constraining, where the artifact has a unique operational semantics
- [representational form](./representational-form.md) — defined-in: the natural-language/symbolic split behind biasing versus excluding
- [lineage](./lineage.md) — contrasts: source derivation, independent of how constrained an artifact is
- [agentic systems interpret underspecified instructions](../agentic-systems-interpret-underspecified-instructions.md) — grounds: why natural-language artifacts leave an interpretation space to narrow
- [learning is not only about generality](../learning-is-not-only-about-generality.md) — grounds: Simon's criterion under which an improving constraint counts as learning
- [methodology enforcement is constraining](../methodology-enforcement-is-constraining.md) — extends: activation and response as independent axes of enforcement strength
- [progressive constraining commits only after patterns stabilize](../progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: when to commit, and why one-shot commitment freezes an arbitrary reading
- [constraining and extraction both trade generality for reliability](../constraining-and-extraction-both-trade-generality-for-reliability.md) — extends: the trade that makes constraining a design decision
- [codification and relaxing navigate the bitter-lesson boundary](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to relax
- [fixed artifacts split into exact specs and proxy theories](../exact-implementation-does-not-validate-a-requirement.md) — extends: when a constraint can be hardened confidently and when relaxing may be needed
- [the verifiability gradient](../verifiability-gradient.md) — extends: the checks that decide how far a constraint can be hardened with confidence
- [error messages that teach are a constraining technique](../error-messages-that-teach-are-a-constraining-technique.md) — extends: a technique that blocks wrong outputs while demonstrating correct ones
- [selecting an LLM output fixes a result, not its interpretation](../selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) — contrasts: result selection fixes which result exists without narrowing its interpretation
