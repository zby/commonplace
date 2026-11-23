---
description: "Curated head for the prompt-semantics tag — what fixes the meaning of a prompt (an English requirement or an adopted model package) and how accurately that meaning can be predicted or inspected"
type: types/tag-readme.md
---

# prompt-semantics

What fixes the meaning of a prompt, and how accurately that meaning can be predicted or inspected. Assign this tag to artifacts that substantively address one of three questions: which reference governs a prompt (an English requirement or an adopted model package), how an English reading relates to the behavior the package defines, or what evidence a claim about a prompt's behavior needs. Writing a prompt, or reporting what one produced, is insufficient. The defining note is [Prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md).

This is a child of [computational-model](./computational-model-README.md); members keep that tag. [LLM reliability](./llm-reliability-README.md) covers detecting and correcting deviations once the governing reference is named; this tag covers naming it and predicting against it. The general accounts of semantic reference and inspection cost apply to code and weights as well as prompts. They stay under [artifact-analysis](./artifact-analysis-README.md) and are linked below as neighbours, not members.

## Which reference governs

- [Prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — the same prompt can be read as a program in a model-defined language or as English executed by a fallible interpreter; the choice changes what counts as a failure, not the cost of prediction
- [Traditional software can bracket executor conformance; LLM systems cannot](../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) — why executing English leaves interpreter conformance as an open question that classical stacks set aside

## English as the working approximation

- [English can approximate a model-defined prompt language](../theory/english-can-approximate-a-model-defined-prompt-language.md) — the package's semantics can be precise yet too costly to inspect; clause meanings give a coarse account whose fidelity is empirical
- [Natural-language meaning is coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) — untested hypothesis that the English reference itself has no fixed target, only readings aligned where something checks them

## Requirements and evidence

- [Clear instructions can compose into an unsettled contract](../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) — scope, precedence and exceptions can leave combined English requirements unsettled before any interpreter runs
- [Programming practices for prompts need evidence matched to the question](../theory/programming-practices-for-prompts-need-question-specific-evidence.md) — matches typing, testing and versioning to requirement adequacy, conformance, predictive fidelity and execution variation

## Neighbouring accounts

These are not members. They supply the general mechanisms the members apply to prompts.

- [Symbolic form holds consumers to a semantic reference](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) — what adopting a reference fixes, and why adopting a pinned model does not formalize English
- [Implementations do not establish shared semantics](../theory/implementations-do-not-establish-shared-semantics.md) — a formal model of one consumer does not settle a language's meaning
- [Opacity depends on the inspection question and budget](../theory/opacity-depends-on-the-inspection-question-and-budget.md) — why a precise semantics can still be unusable for a given question
- [Near-decomposability may make local inspection affordable](../theory/near-decomposability-may-make-local-inspection-affordable.md) — the proposed condition under which reasoning clause by clause works
- [LLM output deviation requires three-way diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md) — the diagnostic questions that follow once a reference is named

## Related Tags

- [computational-model](./computational-model-README.md) — parent: how instruction execution and orchestration work
- [llm-reliability](./llm-reliability-README.md) — neighbour: deviation, detection and correction against a named reference
- [artifact-analysis](./artifact-analysis-README.md) — neighbour: representational form, semantic reference and opacity for all retained artifacts
- [constraining](./constraining-README.md) — neighbour: narrowing the readings an instruction permits
