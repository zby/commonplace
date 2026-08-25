---
description: "Explicit-premise reasoning templates with execution traces and formal conclusions improve code verification by 5–12 points, supporting structure as interpretation control at 2.8× step cost"
source: https://arxiv.org/html/2603.01896v2
captured: "2026-03-07"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: acd2639d1e6041491cf9130a7d308cd5d69b8b735011991594f9d5f7d0a1a7ad
ingested: "2026-03-09"
type: kb/sources/types/ingest-report.md
domains: [execution-free-verification, structured-reasoning, agentic-code-analysis, oracle-approximation]
---

# Ingest: Agentic Code Reasoning

## Classification
ArXiv preprint with explicit methodology, controlled ablations across three evaluation tasks, multiple baselines, error analyses, and quantitative results on established benchmarks (SWE-bench, Defects4J, RubberDuckBench).
Author: Shubham Ugare and Satish Chandra (Meta). Industry researchers reporting ablations on practical SWE-agent workflows with access to frontier models (Opus-4.5, Sonnet). Moderate-to-strong credibility for empirical claims.

## Summary

The paper introduces "semi-formal reasoning" — structured prompting templates that require LLM agents to construct explicit premises, trace execution paths, and derive formal conclusions when analysing code without executing it. The templates are task-specific but share a common principle: force the agent to document verifiable evidence before reaching a conclusion. Across three tasks (patch equivalence verification, fault localization on Defects4J, code question answering on RubberDuckBench), semi-formal reasoning consistently improves accuracy over unstructured baselines by 5-12 percentage points. The headline result is 93% verification accuracy on real-world agent-generated patches using Opus-4.5, approaching the reliability needed for execution-free RL reward signals. The paper's motivating application is replacing test execution with LLM-based verification in training pipelines, though the cost argument for this substitution is asserted rather than demonstrated.

## Quotes

No source quotes have been retained yet.

## Connections Found

The `/connect` discovery identified 7 note connections and 2 source connections, with 9 candidates rejected after evaluation.

**Strongest connections:**

1. **[Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md)** (evidenced-by): The paper supplies the note's central contrast: semi-formal templates improve code-verification accuracy by 5–12 percentage points, yet the bundled intervention does not isolate format, process, extra computation, or a training-distribution mechanism. Claude Sonnet's code-QA result (84.8% with the template versus 85.3% without it) also shows that the measured effect is condition-dependent.

2. **[human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md)** (exemplifies): The paper documents specific human-like failure modes that structured templates correct: guessing function behavior from names, skipping case enumeration, dismissing subtle differences as irrelevant. The semi-formal template corrects these by forcing explicit evidence at each step.

3. **[agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)** (extends): Semi-formal templates are a concrete, measured interpretation-narrowing mechanism. "Standard reasoning" (minimal prompt, no constraints) is maximally underspecified; the template constrains the interpretation space. The 10pp accuracy gain measures the value of that narrowing.

4. **[oracle-strength-spectrum](../notes/oracle-strength-spectrum.md)** (grounds): The paper works in a domain with hard oracles (test execution) but positions LLM verification as a cheaper substitute. Semi-formal reasoning at 93% accuracy is a soft oracle approximating the hard oracle. The error analysis characterises the remaining 7% gap (incomplete tracing, third-party semantics, dismissing subtle differences).

5. **[error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)** (enables): The paper establishes that semi-formal verification has strong discriminative power (93% vs 50% random baseline), satisfying TPR > FPR for error-correction amplification. The three identified failure modes suggest decorrelation strategies (varying trace order, varying detail level) that the paper does not explore.

6. **[structured-output-is-easier-for-humans-to-review](../notes/structured-output-is-easier-for-humans-to-review.md)** (exemplifies): The paper explicitly describes semi-formal certificates as designed to be "easier to manually validate than examining full agent trajectories."

7. **[methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md)** (exemplifies): Templates constrain how the agent reasons (must state premises, must trace paths, must derive conclusions) — methodology enforcement at the skill level with underspecified response, matching the note's enforcement gradient.

**Source connections:** Synthesises with [ConvexBench ingest](./convexbench-can-llms-recognize-convex-functions.ingest.md) (both show structured process > free-form reasoning across different domains) and connects to [Towards a Science of AI Agent Reliability](https://arxiv.org/pdf/2602.16666) (reliability framework applicable to the verification approach).

## Extractable Value

1. **Semi-formal templates as a causal-identification case.** The paper provides a quantified gain and a null, but its bundled templates do not reveal which component caused either result. This now grounds [Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md). [quick-win]

2. **Failure-mode taxonomy for verification agents.** Three specific failure classes — incomplete execution tracing, third-party library semantic guessing, and dismissal of subtle differences — are reusable for designing eval harnesses or decorrelation strategies. Not currently captured in any KB note. [quick-win]

3. **Process structure vs output structure as separate design dimensions.** Existing KB notes mostly discuss output schema constraints; this paper shows process-schema constraints (what reasoning steps must occur) as an independent lever. The distinction is not articulated in the KB. [deep-dive]

4. **Decorrelation strategy design for soft-oracle amplification.** The three failure modes map to natural decorrelation axes: vary which code paths to trace first, vary the level of detail required, vary whether to start from tests or from patches. Combining this with the error-correction note could yield a concrete amplification protocol. [experiment]

5. **93% as a calibration point on the oracle-strength spectrum.** A concrete data point for what "soft oracle replacing hard oracle" looks like in practice — useful for the oracle-strength-spectrum note's maturation path, specifically the question of when substitution is economically justified. [just-a-reference]

6. **Model capability as boundary condition for structured reasoning gains.** Semi-formal reasoning helps Opus but not Sonnet on code QA. This suggests a threshold: weaker models may need the scaffolding more, while stronger models have already internalised equivalent reasoning patterns. Relevant to the structure-activates note's cautionary status. [experiment]

## Limitations (our opinion)

**What was not tested:**

- **Cost comparison is entirely absent.** The paper asserts execution-free verification is cheaper than running tests, but provides no cost analysis. Semi-formal mode uses 2.8x more agent steps than standard; Opus-4.5 inference at 100 steps per verification is expensive. Whether this is cheaper than sandbox/CI depends on scale, repo diversity, and infrastructure — none measured. The [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) note predicts this tension: soft oracles substitute for hard oracles only when the cost differential justifies the accuracy gap.

- **No evaluation of amplification through repetition.** The paper establishes that semi-formal verification has discriminative power (93% accuracy), satisfying the conditions the [error-correction note](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) identifies for amplification. But voting, ensemble, or decorrelated-prompt strategies were not tested. This is a significant omission given that the motivating application (RL reward signals) would benefit most from pushing accuracy above 93%.

- **Single model family on a single benchmark ecosystem.** All results use Claude models (Opus-4.5, Sonnet) on SWE-bench-derived tasks, Defects4J (Java only), and RubberDuckBench (15 questions). Generalization to other model families, programming languages, and repository structures is untested. The Sonnet non-improvement on code QA hints that the gains may be model-specific.

- **Accuracy ceiling may be insufficient for the stated application.** 93% on a balanced dataset means ~7% false reward signals in RL training. The paper does not evaluate whether this error rate is tolerable downstream — whether RL training with 7% noisy rewards converges to similar policies as training with test execution. The gap between "feasibility result" and "deployment result" is unaddressed.

- **No comparison with formal or semi-automated verification.** The paper positions semi-formal reasoning between unstructured CoT and full formal verification (Lean, Coq, Datalog). But no hybrid approaches were tested — combining LLM reasoning with lightweight symbolic checks, type-system verification, or property-based testing. The [codification](../notes/definitions/codification.md) framework predicts that hybrid approaches (hard checks where possible, soft elsewhere) would outperform purely soft verification.

- **Template design is not ablated.** The templates differ by task but the paper does not ablate which components matter. Is the premises section critical? The per-test traces? The formal conclusion format? Without this, it's unclear whether the gains come from forcing evidence collection (process structure) or from the specific output format (output structure) — a distinction the KB notes would care about.

## Recommended Next Action

The completed update to [Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) uses the 5–12-point gain and the Claude Sonnet null as evidence that prompt performance alone does not identify which bundled component caused the result.
