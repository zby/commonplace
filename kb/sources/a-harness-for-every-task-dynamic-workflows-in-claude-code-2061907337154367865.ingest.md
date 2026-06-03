---
description: "Anthropic practitioner account of dynamic workflows in Claude Code: model-authored ephemeral JS orchestrators that spawn and coordinate sub-agents"
source_snapshot: "a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md"
ingested: "2026-06-03"
type: kb/sources/types/ingest-report.md
source_type: practitioner-report
domains: [agent-orchestration, sub-agent-coordination, context-engineering, verification]
---

# Ingest: A harness for every task: dynamic workflows in Claude Code

Source: a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md
Captured: 2026-06-03
From: https://x.com/trq212/status/2061907337154367865

## Classification

Type: practitioner-report -- a first-party account by the engineers who shipped the feature (Thariq Shihipar and Sid Bidasaria, technical staff at Anthropic working on Claude Code), describing what dynamic workflows are, why they help, and the patterns they observed in use. It announces a product but reads as a build-and-learnings report rather than a marketing announcement, with explicit "best practices are still developing" and "when not to use" caveats.
Domains: agent-orchestration, sub-agent-coordination, context-engineering, verification
Author: high credibility on the *what* (insider, ships the system), but vendor-positioned and anecdotal on the *how well* -- no measurements, no comparisons against alternatives.

## Summary

Anthropic shipped "dynamic workflows" in Claude Code: instead of planning and executing in a single context window, Claude writes a custom JavaScript harness on the fly with special functions to spawn and coordinate sub-agents, choosing each agent's model and whether it runs in an isolated worktree, and resuming from interruption. The article motivates this by three failure modes that grow with single-context length -- agentic laziness (declaring partial work done), self-preferential bias (preferring one's own output when judging), and goal drift (lossy compaction dropping "don't do X" constraints) -- and argues separate Claudes with isolated, focused goals combat all three. It catalogues six composable patterns (classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done), a long list of use cases (migrations, deep research, deep verification, qualitative sorting, rule adherence, root-cause investigation, scaled triage, evals, model routing), and operational tips: token budgets, pairing with /goal and /loop, a "quarantine" privilege-separation pattern for untrusted content, and a save/share path (press "s", check into `~/.claude/workflows`, distribute via a skill as a template). It contrasts dynamic with static (SDK / `claude -p`) workflows: static must cover all edge cases so it stays generic; a sufficiently capable model can instead author a tailor-made harness per task.

## Connections Found

The companion connect report frames this snapshot as the **shipped, first-party instance** of the KB's orchestration/scheduler theory cluster, and -- because snapshots are immutable and carry no outbound links and this one has no prior `.ingest.md` -- identifies the primary deliverable as **reverse-edge `evidence` candidates** (library notes that should cite this source). The strongest are:

- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -- dynamic workflows *are* "the model writes the orchestrator rather than being it," now on an exact JS substrate with interrupt-and-resume.
- [Orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) -- the save/check-in/distribute-via-skill path is the promote-the-recurring-strategy mechanism this note argues for (against RLM's discard-both default).
- [Synthesis is not error correction](./synthesis-is-not-error-correction.md) -- the source keeps fan-out-and-synthesize (a merging barrier) distinct from tournament/adversarial verification (selection), confirming that design distinction.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- the source motivates workflows by exactly the failure modes the chain addresses and prescribes decomposition + isolated contexts + adversarial verifiers.
- [Decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) and [Agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- the six-pattern catalogue and the model-authored/promotable/model-routed combination are concrete data points for both.
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) -- the Sorting use-case independently asserts "comparative judgment is more reliable than absolute scoring" and runs a pairwise pipeline.

Connect also flags a **synthesis opportunity** (one note could state that a production harness now supplies topology + isolation + verification plus a promotion path in one shipped system) and three maintenance observations: no note names the three failure modes with shared vocabulary, no security-of-orchestration ("quarantine") home note exists, and authoring this ingest consolidates the otherwise note-side-only outbound surface. These are non-actionable context here.

## Extractable Value

1. **A named failure-mode triad for single-context degradation: agentic laziness, self-preferential bias, goal drift.** The connect report confirms no KB note names these three crisply, though several circle them. This is a vocabulary/framing gain that improves retrieval and gives the orchestration cluster a shared diagnosis-of-need language; goal drift's "lossy compaction drops 'don't do X' constraints" is an especially sharp, citable formulation. [quick-win]

2. **First-party corroboration that a production system implements model-authored ephemeral-but-promotable orchestrators.** Until now `rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents` and `orchestration-strategies-and-run-state-have-opposite-persistence` rest largely on the RLM/REPL example; this is an independent, shipped instance on an exact JS substrate, with an explicit promotion path (save to `~/.claude/workflows`, distribute via skill-as-template) that the run-state-persistence note predicts is needed. High reach -- it generalizes the "model writes the orchestrator" move beyond one research artifact. [quick-win]

3. **The dynamic-vs-static framing: static harnesses stay generic because they must cover all edge cases; a capable model authors a tailor-made one per task.** This is a clean articulation of *why* model-authored orchestration earns its keep -- it relocates edge-case handling from author-time genericity to run-time specificity. Directly operationalizes the design-space note's "model-authored scheduler" axis. [quick-win]

4. **A six-pattern decomposition/aggregation catalogue (classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done).** A practitioner vocabulary for `decomposition-heuristics-for-bounded-context-scheduling`; "the synthesize step is a barrier" and "loop until a stop condition (no new findings)" sharpen the aggregation/termination side the KB treats more abstractly. [just-a-reference]

5. **The "quarantine" privilege-separation pattern.** Agents that read untrusted public content are barred from high-privilege actions, which are delegated to acting agents. Connect flags this as a genuine collection-content gap sitting between context-engineering and the four-field security axis -- a candidate operational pattern with no current home note. [experiment]

6. **Pairwise/comparative judgment over absolute scoring as a deployed sorting technique.** "Comparative judgment is more reliable than absolute scoring," implemented as a pairwise-comparison pipeline where "the deterministic loop holds the bracket and only the running order stays in context." Corroborates `brainstorming-how-to-test-whether-pairwise-comparison-can-harden` from production -- but as testimony, not a controlled test. The context-management detail (deterministic host holds the bracket, agents see only the running order) is a reusable scheduling insight. [just-a-reference]

7. **Operational levers: token budgets, /goal hard-completion, /loop for recurring workflows, and model/worktree routing per sub-agent.** Concrete knobs that make the abstract "coordination guarantees" and "bounded-context scheduling" discussions tangible -- e.g. /goal as a guard against agentic laziness, per-agent model choice as intelligence routing. [just-a-reference]

## Limitations (our opinion)

This is editorial opinion. As a **practitioner report** the dominant risks are survivorship and vendor framing:

- **No measurement, no baseline.** Every claim of improvement ("combats these failure modes," "comparative judgment is more reliable") is asserted, not shown. There are no token-cost numbers despite the explicit warning that workflows "often use more tokens," no success-rate comparison against single-context Claude, and no failed-workflow examples. The reach of each pattern beyond the author's own runs is unestablished.
- **Survivorship bias.** The use cases are the ones that worked. We do not see where dynamic workflows underperformed a simple prompt, where the model authored a bad harness, or where coordination overhead swamped the gain. The "when not to use" section gestures at this but stays qualitative.
- **Naming is not explaining.** The three failure modes (laziness, self-preferential bias, goal drift) are vivid and useful as vocabulary, but the article asserts that context isolation fixes them without isolating the mechanism -- a simpler account (more total compute, fresh attention budget per sub-task) could explain much of the benefit without the specific "separate context windows" story. Treat the triad as a sharable diagnosis, not a validated causal model. This matters because `topology-isolation-and-verification-form-a-causal-chain` is itself `status: speculative`; this source illustrates the chain, it does not resolve chain-vs-simpler-account.
- **Vendor bias toward its own model.** The framing ("With Claude Opus 4.8, Claude is now intelligent enough to write a custom harness") ties the capability to a specific Anthropic release; whether model-authored orchestration is broadly reliable or contingent on a particular model is not addressed.

For the KB, the safe stance is to cite this as **corroborating practitioner testimony** on seedling/speculative notes -- additive `evidence` that strengthens existence claims ("a production system does this") without validating effectiveness claims.

## Recommended Next Action

**Author the `evidence` reverse-edges from the two strongest, lowest-risk notes first**, then decide on the failure-mode note. Specifically: add an `evidence` link to this snapshot from [rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) (shipped instance of model-authored ephemeral orchestrators) and from [orchestration-strategies-and-run-state-have-opposite-persistence.md](./orchestration-strategies-and-run-state-have-opposite-persistence.md) (the save/share promotion path it predicts), framed as corroborating practitioner testimony. As a follow-on, evaluate writing a new note in `kb/notes/` that names the **single-context failure-mode triad** (agentic laziness, self-preferential bias, goal drift) and sources it here -- this fills the vocabulary gap connect identified and would anchor several of the orchestration-cluster edges. Promotion is out of scope for this ingest; these are advisory.
