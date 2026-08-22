---
description: "Memento-Skills supplies empirical evidence for frozen-LLM deploy-time learning through routed, rewritten executable skill memory, with transfer bounded by domain alignment"
source: https://arxiv.org/pdf/2603.18743
captured: "2026-07-28"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: b075afb1048ca61ba269c4fc2e8a53295b6e5b364e831d55c74814102b5abaf2
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [deploy-time-learning, agent-memory, skill-routing, self-improving-systems]
---

# Ingest: Memento-Skills: Let Agents Design Agents

## Classification

An arXiv preprint presenting a formal framing, implemented system, controlled ablation, router evaluation, and held-out benchmark results.
Author: A 17-person academic and engineering team led by Huichi Zhou, with affiliations including University College London, Jilin University, HKUST (Guangzhou), and the Yangtze River Delta AI Lab; the paper links public code, but this ingest evaluates the paper rather than independently auditing the implementation.

## Summary

Memento-Skills treats a folder containing a declarative `SKILL.md`, prompts, and executable code as mutable external memory for a frozen LLM. Its read-write loop routes a task to a skill, executes it, judges the result, records utility, attributes a failure to one skill, and either rewrites that skill or creates a new one; a generated unit test gates mutations. A separately trained contrastive router targets execution usefulness rather than semantic similarity. Against a read-write ablation that disables skill optimization, the full system gains 13.7 percentage points on GAIA test accuracy (66.0% versus 52.3%) and 20.8 points on HLE (38.7% versus 17.9%). The paper's most useful boundary is as important as its headline: transfer is limited on heterogeneous GAIA tasks and much stronger within HLE's recurring subject domains, so accumulating skills helps when future tasks actually revisit the library's behavioral structure.

## Connections Found

This paper is a strong empirical anchor for [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md): the retained policy is a mutable natural-language-plus-symbolic artifact around a frozen model, rather than merely a log or prompt. It also bears directly on [retrieval misses breaking local reflective paths](../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md), because behavior-trained routing improves route hits and final execution over lexical and generic embedding retrieval, and on [evaluating memory by effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md), because the paper distinguishes retrieval quality from end-to-end task success. Its closest comparisons are [SkillOpt](skillopt-executive-strategy-self-evolving-agent-skills.ingest.md), which validation-selects edits to one natural-language skill; [SkillRL](skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md), which co-trains model weights with a natural-language skill bank; [Trajectory-Informed Memory Generation](trajectory-informed-memory-generation-self-improving-agents.ingest.md), which retrieves distilled tips rather than executable folders; and [Voyager](../agent-memory-systems/reviews/voyager.md), which promotes successful code but lacks Memento-Skills' failure-driven rewriting and behavior-trained router. The [self-evolver faithfulness study](llm-agents-are-not-always-faithful-self-evolvers.ingest.md) supplies the key counterweight: selecting and injecting condensed experience does not by itself prove that the agent causally uses it.

## Extractable Value

1. **Executable multi-file skills are a concrete mixed-form memory unit** -- The learned object bundles declarative scope, prompts, and code, so one retained unit can carry instruction, context, and executable behavior while remaining inspectable and rewritable. This extends the KB beyond natural-language-only skill optimization and code-only promotion cases. [quick-win]
2. **Skill routing should optimize behavioral utility, not semantic resemblance** -- On 140 synthetic queries, behavior-trained retrieval raises Recall@1 from 0.54 for the generic embedding baseline to 0.60; on real trajectories it raises route-hit rate from 0.53 to 0.58 and judge success from 0.79 to 0.80. The modest end-to-end delta over dense retrieval is the more honest result, but the paired measurements operationalize two different breaks in the retrieval wire. [experiment]
3. **Domain alignment bounds the return from skill accumulation** -- Learned GAIA skills often did not fire on held-out questions because the task structures were too heterogeneous, whereas HLE's recurring subject domains supported reuse and much larger gains. Library growth is therefore not itself coverage; the future task distribution must revisit behaviorally similar regions. [quick-win]
4. **Failure attribution makes the mutation unit selectively addressable** -- The system does not rewrite the whole agent after every miss. It selects one responsible skill, patches that folder while trying to preserve generality, and escalates to restructuring or new-skill discovery only after sufficient low utility. This is a reusable proposal-selection shape for mixed-form artifact loops. [experiment]
5. **Routing quality and causal uptake require different tests** -- Route-hit and trajectory-success measurements establish that selection quality matters, but they do not show whether a selected skill's content caused a particular action. Combining this paper's router ablations with memory-perturbation faithfulness tests would close a missing evaluation layer. [deep-dive]
6. **The fast loop can include a small parametric component without updating the LLM** -- The agent's large language model stays frozen, but the retrieval policy is trained as a contrastive embedding model. This is a useful boundary case for the KB's representational-form account: readable skill mutation and parametric routing can coevolve while remaining distinct adaptation surfaces. [just-a-reference]

## Limitations (our opinion)

The evidence is narrower than the paper's "agent-designing agent" framing. Both benchmarks provide clear answers and repeated evaluation, all reported agent experiments use Gemini-3.1-Flash, and the main baseline retains the same read-write loop while disabling skill optimization; the paper does not compare against the strongest neighboring self-evolving-skill methods or isolate every component of failure attribution, rewriting, discovery, and unit-test rollback. HLE's within-subject reuse may reflect benchmark taxonomy and repeated solution motifs rather than general cross-task abstraction, while GAIA already shows how quickly transfer weakens when those motifs do not recur.

The claim of continual learning "without parameter updates" applies to the underlying LLM, not to the whole system: the behavior-aligned router is itself trained parametrically on synthetic query-skill pairs drawn from a curated public skill catalog. The formal convergence result is inherited from Memento 2 for KL-regularized retrieval policy iteration under bounded rewards and discounting; it does not by itself prove convergence, safety, or non-regression of the paper's practical file-rewriting and library-expansion operations. A generated unit test for the observed failure has a small validation radius but can overfit the triggering example, and the paper does not evaluate cross-skill regressions, adversarial skill mutation, provenance, contradiction handling, retirement, or million-skill routing. Finally, aggregate accuracy and route-hit metrics show useful effects but not causal faithfulness to individual retrieved skills, the distinction emphasized by [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md).

## Recommended Next Action

Update [A retrieval miss is a local reflective-path failure](../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) with Memento-Skills as `evidenced-by`: add the router's generic-embedding versus behavior-trained route-hit and end-to-end results, then state the boundary that route selection tests the discovery wire while a separate perturbation test is still needed to establish causal uptake after retrieval.

---

Relevant Notes:

- [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — abstracted-from: the Read-Write ablation identifies the jointly varied skill-optimization bundle, not any one operation or selected skill
