---
source_snapshot: towards-a-science-of-ai-agent-reliability.md
ingested: 2026-02-25
type: scientific-paper
domains: [agent-reliability, evaluation-methodology, safety-engineering, deployment-governance]
---

# Ingest: Towards a Science of AI Agent Reliability

Source: towards-a-science-of-ai-agent-reliability.md
Captured: 2026-02-25
From: https://arxiv.org/pdf/2602.16666

## Classification

Type: **scientific-paper** -- Princeton preprint with formal metric definitions, cross-domain survey of safety-critical engineering, systematic evaluation of 14 models across two benchmarks (GAIA, tau-bench), multi-run protocols with fault injection and prompt perturbation. Structured as a proper empirical study with methodology, experimental results, and stated limitations.

Domains: agent-reliability, evaluation-methodology, safety-engineering, deployment-governance

Author: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan (Princeton University). Narayanan is a well-known voice on AI accountability and measurement methodology; Kapoor co-authored influential work on AI evaluation pitfalls. This team has credibility on "how we measure AI systems" questions.

## Summary

The paper argues that mean task success rate is an inadequate measure for deployed AI agents and proposes a four-dimensional reliability framework borrowed from safety-critical engineering: consistency (repeatable outcomes across runs), robustness (stability under perturbations), predictability (calibrated confidence), and safety (bounded harm severity). Evaluating 14 models from OpenAI, Google, and Anthropic over 18 months of releases, they find that capability gains (accuracy) have far outpaced reliability gains. Key empirical findings: outcome consistency is low across all models; prompt robustness is the weakest robustness dimension (models handle real infrastructure faults better than paraphrased instructions); calibration has improved but discrimination has not; and larger models are sometimes less consistent than smaller ones because they have more solution strategies. Safety is deliberately excluded from the aggregate reliability score and reported as a hard constraint.

## Connections Found

/connect discovered 8 connections to existing notes, with several being substantive rather than surface-level:

1. **oracle-strength-spectrum** (strong): The paper's core principle -- reliability is independent of capability -- is direct empirical evidence for the oracle-strength claim. The four reliability dimensions operationalise different kinds of oracle strength for agent evaluation. The bottleneck is guidance quality (can you verify correctness?), not raw compute.

2. **bitter-lesson-boundary** (strong): The finding that 18 months of scaling produced only modest reliability improvement confirms the boundary exists. Reliability properties sit closer to the calculator regime (they have definite specifications), yet model scaling alone does not satisfy them.

3. **softening-signals** (strong): Prompt robustness (R_prompt) directly operationalises brittleness-under-paraphrase as a quantitative metric. The counterintuitive finding -- models handle real faults but break under rephrasings -- is the softening signal pattern measured at scale across 14 models.

4. **storing-llm-outputs-is-stabilization** (moderate): The consistency dimension quantifies the cost of un-collapsed distributions. The 50x cost swings and outcome inconsistency on identical inputs are exactly what output stabilization prevents.

5. **approvals-guard-against-llm-mistakes-not-active-attacks** (moderate): Recommendation 4's augmentation/automation distinction maps directly to llm-do's approval system. Human-in-the-loop as reliability backstop (augmentation) versus security boundary.

6. **stabilisation-is-learning** (moderate): Recommendation 2 supports crystallisation's argument that deploy-time artifact improvements (evals, deterministic modules, prompt versioning) can address reliability gaps that model training leaves open.

7. **spec-mining-as-crystallisation** (moderate): Table 3's mapping of real-world failures to reliability metrics is spec mining applied to evaluation -- extracting deterministic checks from observed failure patterns.

8. **adaptation-agentic-ai-analysis** (light): The predictability dimension overlaps with the adaptation paper's confidence signaling; both identify uncertainty estimation as a key gap.

Two synthesis opportunities were flagged: (a) reliability metrics as oracle hardening (connecting oracle-strength-spectrum, this paper, and spec-mining), and (b) augmentation as a deliberate reliability architecture (connecting approvals-guard, this paper, and professional-developers-ai-agents).

## Extractable Value

1. **The four-dimension reliability decomposition (consistency, robustness, predictability, safety) as an evaluation vocabulary.** We already talk about some of these dimensions informally; this paper gives them formal definitions and metrics. Directly applicable to how we think about llm-do agent evaluation. [quick-win]

2. **"Reliability is independent of capability" as an empirically validated principle.** Strengthens oracle-strength-spectrum and bitter-lesson-boundary with concrete data: 18 months of model releases, 14 models, two benchmarks. Useful citation when arguing that eval investment matters independently of model upgrades. [just-a-reference]

3. **Prompt robustness as the weakest link.** The counterintuitive finding that models handle real infrastructure faults better than paraphrased instructions is a concrete design implication: invest in prompt robustness testing before worrying about fault tolerance. Could inform how we think about instruction design in llm-do agents. [experiment]

4. **Larger models are less consistent than smaller ones.** Because they have more solution strategies, run-to-run variability increases with capability. This has direct implications for model selection in llm-do: if consistency matters for a task, a smaller model may be preferable. Connects to storing-llm-outputs-is-stabilization. [experiment]

5. **Safety as hard constraint, not continuous trade-off.** The design choice to exclude safety from the aggregate score and report it separately -- because averaging would obscure tail risks -- is a transferable architectural principle for any evaluation system. [quick-win]

6. **The augmentation/automation reliability threshold.** An agent that succeeds 90% but fails unpredictably may be fine as an assistant but unacceptable as an autonomous system. This quantifies the approval system's value proposition: the human review step converts an unreliable automation into a reliable augmentation. [quick-win]

7. **Calibration improves with training but discrimination does not.** Models are getting better at saying "I'm 80% confident" and being right 80% of the time, but not better at assigning higher confidence to correct answers than incorrect ones. This means confidence scores are improving in aggregate but not becoming more useful for individual decision-making. [deep-dive]

## Recommended Next Action

Write a note titled "reliability-dimensions-as-oracle-hardening" connecting to oracle-strength-spectrum.md, this source, and spec-mining-as-crystallisation.md -- it would argue that the four reliability dimensions map onto systematically converting soft oracles into hard oracles: consistency hardens "does this work?", robustness hardens "does this still work?", predictability hardens "will this work next time?", and safety bounds "what happens when it doesn't work?" This synthesis would unify the oracle-strength framework with empirical reliability measurement and connect it to the spec-mining practice of extracting deterministic checks from observed failures.
