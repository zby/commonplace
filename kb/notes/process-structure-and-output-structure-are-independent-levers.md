---
description: Constraining what reasoning steps must occur (process structure) is an independent lever from constraining what the result looks like (output structure) — the KB's structured-reasoning cluster conflates the two, but the agentic-code-reasoning evidence shows process constraints driving accuracy gains where output format alone would not
type: note
traits: [has-external-sources]
tags: [type-system]
status: seedling
---

# Process structure and output structure are independent levers

Structured templates constrain LLM generation in two distinct ways that the KB has been treating as one:

**Output structure** constrains the shape of the result — JSON schemas, Toulmin sections (Evidence/Reasoning/Caveats), required frontmatter fields, section headings. The constraint operates on what appears in the final artifact.

**Process structure** constrains what reasoning steps must occur before a conclusion is reached — state your premises, trace each execution path, enumerate all cases, derive the conclusion from stated evidence. The constraint operates on how the agent arrives at the result.

The two dimensions are independent: you can have output structure without process structure (a JSON schema that says nothing about how to fill it), and process structure without output structure (a prompt that forces step-by-step reasoning but leaves the answer format unconstrained). Human methodology reflects the same split. Peer review checklists are pure process structure — "did the authors address confounds?" constrains the reasoning without constraining the format. Style guides are pure output structure — "use APA citations" constrains format without constraining reasoning. Scientific paper structure imposes both: the Methods section is a process constraint (you must describe what you did) and an output constraint (it must appear in a section called Methods).

## Empirical support

[Ugare & Chandra (2026)](../sources/agentic-code-reasoning.ingest.md) provide the strongest available evidence. Their semi-formal reasoning templates require agents to construct explicit premises, trace execution paths, and derive formal conclusions — all process constraints. The templates yield 5-12pp accuracy gains on code verification. The paper does not ablate individual template components, so it cannot isolate how much of the gain comes from process constraints versus the incidental output formatting the templates also impose. But the templates' design makes the locus of effect visible: instructions like "must state premises" and "must trace paths" force specific reasoning work that a heading-only constraint would not.

## Two mechanisms, split two ways

The distinction matters because the KB's two main explanatory mechanisms — distribution selection and interpretation narrowing — apply differently to each type of structure.

**Distribution selection** ([structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md)). Output structure activates training data that shares the same format (scientific papers, legal briefs) — this is the distribution-selection effect proper. Process structure activates training data where rigorous reasoning was being performed, regardless of output format. A "state your premises before concluding" instruction may activate the same reasoning quality found in scientific papers without activating the scientific paper format. The two activations draw from overlapping but distinct subsets of the training distribution.

**Interpretation narrowing** ([agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md)). Output constraints narrow the interpretation space of what a valid result looks like. Process constraints narrow the interpretation space of how to get there. Both reduce underspecification, but they address different sources of it — and combining them is not redundant, because eliminating ambiguity about format still leaves ambiguity about reasoning strategy, and vice versa.

The [methodology-enforcement note](./methodology-enforcement-is-constraining.md) already captures the process side under "methodology enforcement at the skill level" — templates that constrain how the agent reasons. Recognising this as a distinct lever connects that observation to the distribution-selection and interpretation-narrowing mechanisms rather than leaving it as an isolated instance.

## Open questions

- **Scaling properties.** Do process constraints and output constraints scale differently with model capability? The Sonnet non-improvement on code QA ([Ugare & Chandra, 2026](../sources/agentic-code-reasoning.ingest.md)) is consistent with process constraints helping less when a model has already internalised the reasoning patterns they enforce. Whether output constraints (distribution selection) are more robust to model scaling is untested.
- **Error decorrelation.** If each process step probes a different aspect of the problem, the steps function as structurally decorrelated checks — connecting process structure to [error-correction amplification](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). This would give process constraints a role that output constraints cannot play: not just improving single-pass accuracy, but enabling multi-pass verification.

---

Relevant Notes:

- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — refines: the distribution-selection argument applies differently to process and output structure; this note separates what that note currently treats as one mechanism
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — extends: process constraints and output constraints narrow different parts of the interpretation space (how vs what)
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — connects: methodology enforcement is primarily process structure (constraining how the agent reasons), not output structure
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — context: human writing genres bundle both process and output structure; the per-convention transfer evaluation should assess each dimension separately
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — speculative: process steps as structurally decorrelated checks could connect process structure to error-correction amplification
- [Agentic Code Reasoning](../sources/agentic-code-reasoning.ingest.md) — grounds: semi-formal templates with process constraints (state premises, trace paths, derive conclusions) yield 5-12pp accuracy gains; template components not individually ablated
