---
description: Definition — constraining narrows the space of valid interpretations a text or symbolic artifact admits, from partial semantic focusing to full commitment in a symbolic artifact with formal semantics
type: kb/types/definition.md
tags: [learning-theory, constraining]
---

# Constraining

Constraining is making semantics more focused: narrowing the space of valid interpretations a text or symbolic artifact admits. In this KB, it names one of two co-equal deploy-time learning mechanisms, alongside [distillation](./distillation.md). A constrained artifact is not merely easier to find, shorter, clearer, or more useful; it leaves future consumers with fewer legitimate ways to read it.

At the light end, a definition, convention, or structured section rules out some readings while leaving several valid ones. At the heavy end, commitment collapses the space to one interpretation: a stored output, schema, validator, route table, or deterministic function. These cases use different media and different levels of force, but they count as constraining for the same reason: they reduce semantic latitude. Reliability, speed, cost control, and reviewability may follow, but they are consequences rather than the definition.

## Scope

Use the term constraining when an artifact, convention, type, validation rule, or implementation reduces the range of interpretations a future agent, human, interpreter, runtime, or other formal consumer can reasonably apply. The test is semantic: are there readings that were previously plausible but are now invalid or dispreferred?

Common KB instances:

- definition notes that replace vague terms with operational meanings;
- title conventions that force a note to state a claim rather than merely name a topic;
- structured sections that assign meaning to positions in a document, such as scope, exclusions, and misuse cases;
- field schemas that define what each value means and which readings are invalid;
- validators, tests, schemas, or scripts that give one interpretation formal consequences.

## The constraining spectrum

Constraining is a gradient, not a single operation. Each step removes some interpretive freedom:

| Constraining | What changes | Semantic effect |
|--------------|-------------|-----------------|
| Define a term | Replace loose usage with an operational boundary | Some ordinary readings no longer count |
| Store an LLM output | Commit to one interpretation of a prompt | Alternative possible completions no longer matter |
| Create a title convention | Require a title to assert a claim or signal a role | Ambiguous topic labels become invalid |
| Add structured sections | Assign meaning to document positions | Readers know how each part should be interpreted |
| Add a schema or validator | Make field meanings and invalid values explicit | Unsupported interpretations are rejected |
| Extract a deterministic function | Move from natural language to executable code, the main practical KB case | One operational interpretation is selected |
| Create a formal schema, grammar, or route table | Move from prose to a symbolic artifact with assigned consequences | One symbolic interpretation is selected |

The last step — [codification](./codification.md) — is the far end of the spectrum where the medium itself changes from natural language to a symbolic artifact with formal semantics. Executable code is the main practical KB case, but codification also includes schemas, grammars, route tables, and other symbolic artifacts when a formal consumer assigns their consequences. It is not a separate mechanism; it is constraining that has crossed a medium boundary and selected an operational interpretation.

Many constraints never need to codify. A definition note can focus a term's meaning without becoming code. A naming convention can constrain how a note title is interpreted without any phase transition.

## Exclusions

Constraining is not [distillation](./distillation.md). Distillation asks whether an artifact was transformed from recorded source material for a bounded consumer; constraining asks how much interpretation space the artifact leaves open.

Constraining is not retrieval or navigation. A description field, index entry, or backlink may help an agent find the right artifact, but it is constraining only when it also narrows what the artifact means.

Constraining is not always enforcement. A convention, example, or inline gloss can constrain interpretation without any runtime enforcing it.

Constraining is not automatically an improvement. A constraint can freeze the wrong proxy theory, overfit a narrow case, or block useful generality.

## Misuse Cases

- Calling every improvement constraining. If the change adds information without narrowing future interpretation, it may be accumulation, retrieval support, or distillation instead.
- Treating constraining as synonymous with codification. Codification is only the far end where interpretation moves to a symbolic artifact with formal semantics or assigned consequences.
- Counting workflow affordances as constraints because they make an operation easier. Ease is not enough; the change must rule out interpretations.

## Relaxing

Relaxing is the reverse term: replacing a constrained component with a more general-purpose one so interpretation space reopens. The pair names direction of semantic change: constraining narrows valid readings, relaxing admits more readings again.

## Relationship to distillation

Constraining and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Use-shaped but still semantically loose (draft skill, rough note) |
| **Constrained** | Committed but not transformed from a source (stored output, frozen config) | Use-shaped and semantically focused (validated skill, codified script) |

You can constrain without distilling (store an LLM output — commit to one interpretation without transforming recorded source material). You can distil without constraining (write a task-shaped skill that remains natural language and underspecified). Strong artifacts often combine both operations.

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact transformed from recorded source material for a particular consumer?*

## Prior Analogues

Several fields have nearby ideas: gradual typing narrows program meanings, formal specification narrows admissible system interpretations, Carnap's explication narrows concept meaning, and ontology engineering narrows category and relationship usage. The KB-specific use applies the same direction of change to agent-operated artifacts whose default substrate is underspecified natural language.

---

Relevant Notes:

- [codification](./codification.md) — the far end of the constraining spectrum: constraining that crosses a medium boundary
- [distillation](./distillation.md) — co-equal mechanism: targeted transformation shaped by consumer and use; orthogonal to constraining
- [agentic systems interpret underspecified instructions](../agentic-systems-interpret-underspecified-instructions.md) — foundation: the underspecification framework that constraining operates on
- [storing LLM outputs is constraining](../storing-llm-outputs-is-constraining.md) — the simplest instance: committing to one interpretation by keeping a specific output
- [methodology enforcement is constraining](../methodology-enforcement-is-constraining.md) — applies: the instruction → skill → hook → script gradient is constraining applied to methodology
- [error messages that teach are a constraining technique](../error-messages-that-teach-are-a-constraining-technique.md) — instance: teaching error messages constrain interpretation space by simultaneously blocking wrong outputs and demonstrating correct ones
- [the verifiability gradient](../verifiability-gradient.md) — the ladder across which constraining operates
- [fixed artifacts split into exact specs and proxy theories](../fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — determines when constraining can be hardened confidently vs when relaxing may be needed
- [ABC: Agent Behavioral Contracts](https://arxiv.org/html/2602.22302v1) — grounds: probabilistic compliance model (p,δ,k) and Drift Bounds Theorem quantify how much drift each enforcement layer permits — formal statement of the constraining trade-off
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: "encode standards directly into the repository" is constraining in practitioner language at production scale
