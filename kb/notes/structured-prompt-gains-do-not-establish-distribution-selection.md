---
description: Formatting compliance, extra computation, and task decomposition can mimic distribution-selection gains, so prompt performance alone cannot identify the mechanism
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [type-system]
---

# Structured-prompt gains do not establish training-distribution selection

Structured prompts can change model outputs and sometimes improve task accuracy. Those effects alone do not identify why they occur. In particular, they do not show that headings such as `Evidence` and `Reasoning` cue patterns from a higher-quality subset of the model's training data.

## What distribution selection would have to mean

Distribution selection is the hypothesis that structural cues improve output by evoking patterns learned from training examples whose reasoning quality is systematically higher than that of the relevant alternatives. Surface resemblance to scientific papers or legal analyses is not enough. The improvement must come from those learned patterns, not from formatting compliance, extra generated tokens, task decomposition, or a reasoning procedure that the prompt explicitly requires.

These rival mechanisms predict many of the same observations. A heading can constrain an answer's format without changing its reasoning. A template can improve accuracy by requiring useful intermediate checks. A genre cue can change style without selecting training examples associated with better task performance.

A discriminating test would hold task information and token budget constant while comparing matched heading-only, process-only, heading-plus-process, and unstructured prompts. It would measure task accuracy separately from format compliance. The distribution-selection hypothesis would gain distinctive support only if the structural or genre cue improved task quality beyond what the process and format controls explain. Until such a comparison exists, a performance gain does not identify the mechanism.

## What the current evidence establishes

Ugare and Chandra report gains of 5–12 percentage points from semi-formal reasoning templates on code-verification tasks. Yet the same study reports no improvement for the Claude Sonnet model on code QA: 84.8% with the template versus 85.3% without it. These mixed results show that template effects vary across the tested task and model conditions. They establish neither a general performance tendency nor training-distribution selection as the cause of the favorable results.

Lampinen et al. report that chain-of-thought prompting partly reduces content bias in abstract or unfamiliar reasoning conditions without degrading performance in familiar ones. This result shows that a structural intervention can change reasoning behavior, but it does not directly observe activation of a higher-quality training subset or rule out the rival mechanisms. Likewise, the persistence of content effects shows only that scaling and tuning did not eliminate the effect in the tested conditions; it does not establish that structural prompting is permanently necessary.

## Epiplexity supplies an analogy, not a causal identification

Finzi et al.'s epiplexity framework shows that data arrangement can change what a computationally bounded learner extracts. This result makes the distribution-selection hypothesis plausible: reorganizing a task may change which learned structure a bounded model can use. But the formal result concerns learning from ordered data, not inference-time prompting or selection among pretraining subsets. It motivates a test of the proposed prompting mechanism; it does not formalize that mechanism.

## Design consequence

A prompt or KB template should be justified by the work its structure requires or exposes: separating evidence from inference, requiring intermediate checks, enforcing an output contract, or making review easier. Training-distribution selection may explain an additional benefit, but it should not be a premise for adopting the structure until evidence distinguishes it from the rival mechanisms.

The arguments from [shared failure modes](./human-writing-structures-transfer-to-llms-because-failure-modes.md) and [human reviewability](./structured-output-is-easier-for-humans-to-review.md) do not depend on this hypothesis. The distinction between [process structure and output structure](./process-structure-and-output-structure-are-independent-levers.md) helps expose two of the causal rivals that a useful test must separate.

---

Sources:

- [Ingest: From Entropy to Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) — evidenced-by: preserves the bounded-extractability result and the caveat about transferring it to inference-time prompts.
- [Ingest: Agentic Code Reasoning](../sources/agentic-code-reasoning.ingest.md) — evidenced-by: records the code-verification gains and the Claude Sonnet null in a caveated local analysis.
- [Ingest: Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) — evidenced-by: records the content-effect results while noting that they do not identify a causal training-data property.

Relevant Notes:

- [Epiplexity by example: what entropy and complexity miss](./epiplexity-by-example-what-entropy-and-complexity-miss.md) — grounds: makes the arrangement-sensitive bounded-observer mechanism concrete.
- [Human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — contrasts: supplies an independent justification for structure based on failure-mode transfer.
- [Structured output is easier for humans to review](./structured-output-is-easier-for-humans-to-review.md) — contrasts: supplies an independent justification based on reviewability.
- [Process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md) — mechanism: distinguishes two effects that the distribution-selection hypothesis must not conflate.
