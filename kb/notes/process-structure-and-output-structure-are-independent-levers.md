---
description: "Distinguishes constraints on reasoning steps from constraints on result shape, using code-reasoning and GSM-DC evidence where process structure changes outcomes beyond formatting"
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

[Ugare & Chandra (2026)](https://arxiv.org/html/2603.01896v2) provide the strongest available evidence. Their semi-formal reasoning templates require agents to construct explicit premises, trace execution paths, and derive formal conclusions — all process constraints. The templates yield 5-12pp accuracy gains on code verification. The paper does not ablate individual template components, so it cannot isolate how much of the gain comes from process constraints versus the incidental output formatting the templates also impose. But the templates' design makes the locus of effect visible: instructions like "must state premises" and "must trace paths" force specific reasoning work that a heading-only constraint would not.

GSM-DC ([Yang et al., 2025](https://arxiv.org/html/2505.18761v2)) supplies a complementary metric split. Its Path Accuracy (PAcc) checks whether the model selected the right reasoning dependencies; Step Accuracy (SAcc) checks whether the arithmetic execution along those steps is correct. Irrelevant context degrades both, and the SAcc/PAcc gap shows execution errors can increase even when the reasoning path is selected correctly. That operationalizes the distinction this note needs: process quality and output/execution quality can degrade independently under the same noise.

[CEDAR-GRPO](../sources/cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md) supplies evidence that process-directed optimization can matter while output shape stays fixed. CEDAR and correctness-only GRPO retain the same `<think>/<answer>` contract and training mixture, but the composite reward improves held-out final-answer accuracy by 2.7 percentage points on average across four backbones. On DeepSeek-R1-Distill-Qwen-7B, correctness-only GRPO improves answer accuracy over the base model even as measured directionality falls from 0.21 to 0.16, branchiness from 1.22 to 1.16, and prior invocation from 0.59 to 0.53. Process-directed optimization can therefore improve behavior beyond a fixed output shape, while outcome gains need not imply gains in the named trace qualities. This supports behavioral efficacy, not emitted-trace faithfulness or validation of the directionality construct.

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
- [GSM-DC](https://arxiv.org/html/2505.18761v2) — evidenced-by: PAcc and SAcc separate path selection from step execution, showing irrelevant context can degrade both independently
- [Verbalizable Representations Form a Global Workspace in Language Models](../sources/verbalizable-representations-global-workspace-llms.ingest.md) — evidenced-by: explicit chain-of-thought makes GSM8K more robust to J-space ablation than direct answering, isolating externalized reasoning process from final-answer shape
