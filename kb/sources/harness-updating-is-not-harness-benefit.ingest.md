---
description: "Primary cross-pairing evidence separates harness-edit production from artifact loading, faithful use, and downstream benefit, stopping short of compounding"
source_snapshot: "harness-updating-is-not-harness-benefit.md"
ingested: "2026-08-04"
type: kb/sources/types/ingest-report.md
domains: [self-improvement, harness-evolution, agent-capability, evaluation]
---

# Ingest: Harness Updating Is Not Harness Benefit

Source: [harness-updating-is-not-harness-benefit.md](harness-updating-is-not-harness-benefit.md)
Captured: 2026-08-04
From: https://arxiv.org/abs/2605.30621

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that formalizes two harness-evolution capabilities and reports controlled agent-evolver cross-pairings across three benchmarks.
Domains: self-improvement, harness-evolution, agent-capability, evaluation
Author: Minhua Lin and a multi-institution research team from Penn State, UC Santa Cruz, Amazon, Emory, UIUC, and Northeastern; the paper releases code, but remains a new preprint rather than peer-reviewed evidence.

## Summary

The paper separates an evolver's ability to produce useful persistent harness changes from a task-solving agent's ability to benefit from them. It pairs seven model backbones as evolvers and six as agents across SWE-bench Verified, MCP-Atlas, and SkillsBench while holding the solve-evolve loop, prompts, task stream, budget, and writable harness surfaces fixed. Harness-updating gain varies by at most 3.1 percentage points between evolvers on each benchmark, and the smallest evolver can match frontier-model update gains in one case. Harness-benefit is non-monotonic: middle-tier agents often gain most, strong agents have less headroom, and weak agents gain little. SkillsBench traces the weak-agent gap to failures to load relevant skills and to follow their procedures after loading.

## Connections Found

This paper is the primary empirical anchor behind the update-versus-benefit distinction reported in [Harness Engineering for Self-Improvement](harness-engineering-for-self-improvement.ingest.md). Its skill-load and harness-following measurements support the separation between read-back and behavioral [activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). For the KB's account of [compounding](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), harness benefit is an intermediate causal stage: an accepted update must become available and change task behavior before its benefit could feed into further improvement, but task benefit alone does not establish that final feedback step. The experimental claims remain bounded by the [fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) of editable substrates, interfaces, prompts, tasks, scoring, and anchor sets.

## Extractable Value

1. **Separate improvement production from improvement uptake** -- `harness-updating` asks whether an evolver can write changes that yield downstream gains; `harness-benefit` asks whether a target agent can realize gains under changed harnesses. This blocks a good edit or strong proposer from being counted as an effective system improvement before a consumer uses it successfully. [quick-win]

2. **Place harness benefit between retention and compounding** -- the paper supplies measurable transitions from an applied update to loading, faithful execution, and task gain. These transitions are necessary for an operational benefit, but the paper does not test whether that benefit helps produce a later retained improvement. This sharpens the KB's compounding boundary without redefining task benefit as compounding. [quick-win]

3. **Measure activation and adherence separately** -- on SkillsBench, skill-load rate falls from about 0.96 for Opus 4.6 and Qwen3-235B to 0.25 for Qwen3-32B, while harness-following rate separates agents that load equally often: 0.76 for Opus 4.6 versus 0.35 for Qwen3-235B. The phase analysis further distinguishes initial uptake from long-horizon drift. [experiment]

4. **Treat capability placement as conditional on the interface** -- under the tested prompts and edit surfaces, evolver identity changes results much less than task-solving-agent identity, so spending a stronger model on the consumer may outperform spending it on the updater. This is useful allocation evidence for these benchmarks, not a general claim that update production is easy. [just-a-reference]

5. **Map the effective update space before crediting model capability** -- evolvers can condition on the current harness and task trajectories, outputs, scores, and feedback; they can compose skill edits, plus prompt and memory edits on MCP-Atlas. Task agents can load skills and compose runner actions. The LLM backbones map those inputs to edits or actions. Tool interfaces, execution policies, solver and evolver prompts, trajectory windows, initial harnesses, task streams, budgets, permissions, benchmark objectives, scoring rules, anchor sets, and model weights remain fixed. The comparison shows improvement within this decomposition; it does not validate the decomposition or excluded alternatives. [deep-dive]

6. **Read the capability metrics as pairing-relative proxies** -- `Δupdate` is downstream gain averaged over three anchor agents, so it remains mediated by those agents' ability to use an update. `Δbenefit` is the maximum gain over three anchor evolvers, so it describes best observed pairing rather than an updater-independent property of the target model. [experiment]

## Limitations (our opinion)

The model-by-role comparison is controlled, but the capability names are stronger than the measurements. Harness-updating is inferred from gains obtained by a small fixed anchor-agent set, not from an updater quality measure independent of consumers. Harness-benefit takes a maximum over three evolvers. The paper reports no uncertainty for the headline model ordering, and SkillsBench already gives a noisier pattern than SWE or MCP.

The activation diagnosis is limited to SkillsBench. Skill-load rate directly observes whether a skill enters context, but harness-following rate is assigned by a Sonnet 4.6 judge from a generated rubric. The trajectory cases make the two failure modes plausible, yet no intervention repairs the loader protocol or adherence and then tests whether weak-agent gains recover. Base task capability could partly explain both low adherence and low success.

The in-situ stream prevents a task's own evidence from improving its scored attempt, but it remains one fixed stream per benchmark rather than a held-out distribution or repeated deployment history. The editable components are skills on SWE and SkillsBench, and skills, prompts, and append-only memory on MCP. Other representations, retrieval policies, tools, execution policies, hybrid weight updates, objectives, and evaluator designs remain outside the update space. The results therefore support role separation and two concrete uptake failures under the tested harnesses; they do not establish universal model capability rankings or a complete decomposition of self-improvement.

For compounding specifically, the paper measures retained changes affecting later task performance. It does not measure a later improvement episode becoming cheaper, broader, or more reliable because of that task benefit, nor an allocator that reinvests saved resources into improvement. Its repeated solve-evolve loop can alter later evidence, but that evidence-channel dependence is not the retained-benefit-to-improvement trace required by the KB's causal definition.

## Recommended Next Action

Update [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) with this paper as an `evidenced-by` boundary case: add harness benefit as the measured bridge from an applied change through loading and faithful use to task gain, then state that compounding requires this benefit to contribute causally to a later improvement episode.
