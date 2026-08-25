---
description: "Primary cross-pairing evidence separates harness-edit production, artifact loading, judged procedural match, and downstream benefit while stopping short of causal uptake and compounding"
source: https://arxiv.org/abs/2605.30621
captured: "2026-08-04"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 453897c0e4c13dd6cb076cb2d33fc83fcd3d8bd4348633f4f0d554beb0dbe4cd
ingested: "2026-08-04"
type: kb/sources/types/ingest-report.md
domains: [self-improvement, harness-evolution, agent-capability, evaluation]
---

# Ingest: Harness Updating Is Not Harness Benefit

## Classification

An arXiv v1 preprint that formalizes two harness-evolution capabilities and reports controlled agent-evolver cross-pairings across three benchmarks.
Author: Minhua Lin and a multi-institution research team from Penn State, UC Santa Cruz, Amazon, Emory, UIUC, and Northeastern; the paper releases code, but remains a new preprint rather than peer-reviewed evidence.

## Summary

The paper separates an evolver's ability to produce useful persistent harness changes from a task-solving agent's ability to benefit from them. It pairs seven model backbones as evolvers and six as agents across SWE-bench Verified, MCP-Atlas, and SkillsBench while holding the solve-evolve loop, prompts, task stream, budget, and writable harness surfaces fixed. Harness-updating gain varies by at most 3.1 percentage points between evolvers on each benchmark, and the smallest evolver can match frontier-model update gains in one case. Harness-benefit is non-monotonic: middle-tier agents often gain most, strong agents have less headroom, and weak agents gain little. On SkillsBench, weak agents also show lower skill loading and lower judge-rated procedural match after loading.

## Quotes

- **Source extract (verbatim):** We analyze two harness self-evolution capabilities: (i) *harness-updating*, the capability to produce useful persistent harness updates from execution evidence; (ii) *harness-benefit*, the capability to benefit from updated harnesses during task solving.
  - **Source location:** Abstract.
- **Source extract (verbatim):** The evolver produces the updated harness $H_{t}$ from $H_{t-1}$ and $\mathcal{D}_{t}$ as in Eq. [2](https://arxiv.org/html/2605.30621#S3.E2), yielding the next agent $A_{t}=(f,H_{t})$. This loop repeats for $T$ steps, producing the final harness $H_{T}$.
  - **Source location:** Section 3.2, Evolution Protocol.
- **Source extract (verbatim):** To quantify this on SkillsBench, we report each agent’s *skill-load rate (SLR)*, the fraction of its trajectories in which it actively loads at least one skill into its context.
  - **Source location:** Section 4.3, Agent-side Analysis.
- **Source extract (verbatim):** Tab. [2](https://arxiv.org/html/2605.30621#S4.T2) reports HFR together with two complementary metrics: *SLR*, which measures harness activation, and *pass-when-loaded (LPR)*, which measures the pass rate among that model’s skill-loaded trajectories.
  - **Source location:** Section 4.3, Agent-side Analysis.
- **Source extract (verbatim):** We use an LLM judge to measure whether an agent follows a loaded harness artifact during task solving. All judged trajectories are blinded by replacing model identifiers with the placeholder <MODEL>. Claude Sonnet 4.6 is used as the judge model.
  - **Source location:** Appendix D.3, Judge Details for Harness-Following Rate.
- **Source extract (verbatim):** For each SkillsBench trajectory in which at least one skill is loaded, the judge receives the loaded skill body and the agent trajectory. The judge first converts the skill body into a locked rubric of atomic procedural instructions, and then checks whether the trajectory follows that rubric.
  - **Source location:** Appendix D.3, Judge Details for Harness-Following Rate.

## Connections Found

This paper is the primary empirical anchor behind the update-versus-benefit distinction reported in [Harness Engineering for Self-Improvement](harness-engineering-for-self-improvement.ingest.md). Its skill-load and harness-following measurements separate read-back from judged procedural match, but [an experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): without a matched withheld- or replaced-skill condition, the latter does not identify causal uptake of the skill content. For the KB's account of [compounding](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), harness benefit is an intermediate causal stage: an accepted update must become available and improve task outcomes before its benefit could feed into further improvement, but task benefit alone does not establish that final feedback step. The experimental claims remain bounded by the [fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) of editable substrates, interfaces, prompts, tasks, scoring, and anchor sets.

## Extractable Value

1. **Separate improvement production from improvement uptake** -- `harness-updating` asks whether an evolver can write changes that yield downstream gains; `harness-benefit` asks whether a target agent can realize gains under changed harnesses. This blocks a good edit or strong proposer from being counted as an effective system improvement before a consumer uses it successfully. [quick-win]

2. **Place harness benefit between retention and compounding** -- the paper measures applied updates, loading, judged procedural match, and task gain separately. These measurements can localize where benefit fails, but they do not form a fully identified causal chain. The paper also does not test whether a task benefit helps produce a later retained improvement. This sharpens the KB's compounding boundary without redefining task benefit as compounding. [quick-win]

3. **Measure loading and judged adherence separately** -- on SkillsBench, skill-load rate falls from about 0.96 for Opus 4.6 and Qwen3-235B to 0.25 for Qwen3-32B, while harness-following rate separates agents that load equally often: 0.76 for Opus 4.6 versus 0.35 for Qwen3-235B. The phase analysis distinguishes initial procedure matching from long-horizon drift, but neither measure identifies the skill content's causal effect. [experiment]

4. **Treat capability placement as conditional on the interface** -- under the tested prompts and edit surfaces, evolver identity changes results much less than task-solving-agent identity, so spending a stronger model on the consumer may outperform spending it on the updater. This is useful allocation evidence for these benchmarks, not a general claim that update production is easy. [just-a-reference]

5. **Map the effective update space before crediting model capability** -- evolvers can condition on the current harness and task trajectories, outputs, scores, and feedback; they can compose skill edits, plus prompt and memory edits on MCP-Atlas. Task agents can load skills and compose runner actions. The LLM backbones map those inputs to edits or actions. Tool interfaces, execution policies, solver and evolver prompts, trajectory windows, initial harnesses, task streams, budgets, permissions, benchmark objectives, scoring rules, anchor sets, and model weights remain fixed. The comparison shows improvement within this decomposition; it does not validate the decomposition or excluded alternatives. [deep-dive]

6. **Read the capability metrics as pairing-relative proxies** -- `Δupdate` is downstream gain averaged over three anchor agents, so it remains mediated by those agents' ability to use an update. `Δbenefit` is the maximum gain over three anchor evolvers, so it describes best observed pairing rather than an updater-independent property of the target model. [experiment]

## Limitations (our opinion)

The model-by-role comparison is controlled, but the capability names are stronger than the measurements. Harness-updating is inferred from gains obtained by a small fixed anchor-agent set, not from an updater quality measure independent of consumers. Harness-benefit takes a maximum over three evolvers. The paper reports no uncertainty for the headline model ordering, and SkillsBench already gives a noisier pattern than SWE or MCP.

The activation diagnosis is limited to SkillsBench. Skill-load rate directly observes whether a skill enters context, but harness-following rate is assigned by a Sonnet 4.6 judge from a generated rubric. The trajectory cases make the two failure modes plausible, yet no intervention repairs the loader protocol or adherence and then tests whether weak-agent gains recover. Base task capability could partly explain both low adherence and low success.

The in-situ stream prevents a task's own evidence from improving its scored attempt, but it remains one fixed stream per benchmark rather than a held-out distribution or repeated deployment history. The editable components are skills on SWE and SkillsBench, and skills, prompts, and append-only memory on MCP. Other representations, retrieval policies, tools, execution policies, hybrid weight updates, objectives, and evaluator designs remain outside the update space. The results therefore support role separation and two concrete uptake failures under the tested harnesses; they do not establish universal model capability rankings or a complete decomposition of self-improvement.

For compounding specifically, the paper measures retained changes affecting later task performance. It does not measure a later improvement episode becoming cheaper, broader, or more reliable because of that task benefit, nor an allocator that reinvests saved resources into improvement. Its repeated solve-evolve loop can alter later evidence, but that evidence-channel dependence is not the retained-benefit-to-improvement trace required by the KB's causal definition.

## Recommended Next Action

Completed in [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md): the paper now supplies a measurement ladder from applied change through loading and judged procedural match to task gain, while the note states both the missing causal-uptake contrast and the additional feedback edge required for compounding.
