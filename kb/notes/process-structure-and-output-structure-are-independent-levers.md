---
description: "Distinguishes constraints on reasoning steps from constraints on result shape and identifies the evidence needed to separate their effects"
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [type-system]
---

# Process structure and output structure are independent levers

Structured templates constrain LLM generation in two distinct ways that the KB has been treating as one:

**Output structure** constrains the shape of the result — JSON schemas, Toulmin sections (Evidence/Reasoning/Caveats), required frontmatter fields, section headings. The constraint operates on what appears in the final artifact.

**Process structure** constrains what reasoning steps must occur before a conclusion is reached — state your premises, trace each execution path, enumerate all cases, derive the conclusion from stated evidence. The constraint operates on how the agent arrives at the result.

The two dimensions are independent: you can have output structure without process structure (a JSON schema that says nothing about how to fill it), and process structure without output structure (a prompt that forces step-by-step reasoning but leaves the answer format unconstrained). Human methodology reflects the same split. Peer review checklists are pure process structure — "did the authors address confounds?" constrains the reasoning without constraining the format. Style guides are pure output structure — "use APA citations" constrains format without constraining reasoning. Scientific paper structure imposes both: the Methods section is a process constraint (you must describe what you did) and an output constraint (it must appear in a section called Methods).

## Empirical support

[Ugare & Chandra (2026)](https://arxiv.org/html/2603.01896v2) provide evidence from a bundled structured intervention intended to elicit explicit intermediate work. Their semi-formal templates require outputs that state premises, trace execution paths, and derive formal conclusions, and they yield 5-12pp accuracy gains on code verification. The paper does not ablate individual template components, so it cannot isolate process-directed requirements from the extra visible content and formatting. Nor does it establish that the emitted trace faithfully reports the model's internal reasoning. The bounded result is that this bundled process-directed prescription improved final-answer accuracy under its accompanying output form.

[GSM-DC](../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) separates two failures inside a shared chain-of-thought format. Path Accuracy (PAcc) checks whether the model used the required reasoning dependencies without using distractors; Step Accuracy (SAcc) also requires correct arithmetic execution. The reported SAcc/PAcc gap shows that arithmetic can fail even when path selection succeeds. It does not vary a process instruction against an output-form constraint, so it bounds rather than tests this note's two-lever claim.

[CEDAR-GRPO](../sources/cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md) supplies bounded evidence that process-directed optimization can matter under a shared output prescription. CEDAR-GRPO and its correctness-only Cor-GRPO comparator generate the same structured reasoning-and-answer form after training on the 1,920-example training split of the paper's 2,400-example abductive dataset. CEDAR adds evidence-coverage and evidence-to-explanation-directionality rewards and averages 2.7 percentage points higher than Cor-GRPO across four backbones and eleven held-out tasks. The shared form means the reported difference is not a difference between prescribed result formats, but the experiment does not ablate output shape independently and therefore does not estimate a pure process-structure effect. Separately, for DeepSeek-R1-Distill-Qwen-7B, Cor-GRPO's measured directionality falls from the base model's 0.21 to 0.16, branchiness from 1.22 to 1.16, and prior invocation from 0.59 to 0.53. Those process metrics are LLM-as-judge measurements; they do not establish emitted-trace faithfulness or validate directionality as a construct.

## Two mechanisms, split two ways

The distinction matters because two proposed explanatory mechanisms — distribution selection and interpretation narrowing — apply differently to each type of structure.

**Distribution selection** is a hypothesis, not an identified effect ([structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md)). Output structure could cue patterns associated with a shared format, while process structure could cue learned reasoning procedures regardless of output format. But a measured gain does not show that either activation occurred: the constraints also change format compliance and required reasoning work directly. Process-only and output-only interventions therefore define experimental contrasts rather than two established training subsets.

**Interpretation narrowing** ([agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md)). Output constraints narrow the interpretation space of what a valid result looks like. Process constraints narrow the interpretation space of how to get there. Both reduce underspecification, but they address different sources of it — and combining them is not redundant, because eliminating ambiguity about format still leaves ambiguity about reasoning strategy, and vice versa.

The [methodology-enforcement note](./methodology-enforcement-is-constraining.md) already captures the process side under "methodology enforcement at the skill level" — templates that constrain how the agent reasons. Recognising this as a distinct lever connects that observation to the distribution-selection and interpretation-narrowing mechanisms rather than leaving it as an isolated instance.

## Open questions

- **Scaling properties.** Do process constraints and output constraints scale differently with model capability? The Sonnet non-improvement on code QA ([Ugare & Chandra, 2026](https://arxiv.org/html/2603.01896v2)) is consistent with process constraints helping less when a model has already internalised the reasoning patterns they enforce. Whether output constraints (distribution selection) are more robust to model scaling is untested.
- **Error decorrelation.** If each process step probes a different aspect of the problem, the steps function as structurally decorrelated checks — connecting process structure to [error-correction amplification](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). This would give process constraints a role that output constraints cannot play: not just improving single-pass accuracy, but enabling multi-pass verification.

---

Relevant Notes:

- [Structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md) — grounds: explains why process and output interventions must be tested separately rather than inferred from one bundled prompt gain
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — extends: process constraints and output constraints narrow different parts of the interpretation space (how vs what)
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — connects: methodology enforcement is primarily process structure (constraining how the agent reasons), not output structure
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — context: human writing genres bundle both process and output structure; the per-convention transfer evaluation should assess each dimension separately
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — speculative: process steps as structurally decorrelated checks could connect process structure to error-correction amplification
- [Agentic Code Reasoning](https://arxiv.org/html/2603.01896v2) — evidenced-by: semi-formal templates with process constraints (state premises, trace paths, derive conclusions) yield 5-12pp accuracy gains; template components not individually ablated
- [GSM-DC](../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — bounds: PAcc and SAcc separate path selection from arithmetic execution inside one shared trace format, but the study does not vary process instructions against output-form constraints
- [Verbalizable Representations Form a Global Workspace in Language Models](../sources/verbalizable-representations-global-workspace-llms.ingest.md) — evidenced-by: explicit chain-of-thought makes the same GSM8K problems more robust to J-space ablation than direct answering, which the authors interpret as externalizing intermediate computation; because chain-of-thought also changes visible output content and length, the comparison does not isolate process from output structure
