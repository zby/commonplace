---
description: "Terminal-RSI paper: alternating verified-trajectory rewriting with critic-inheriting PPO for a 27B terminal agent; evidence on partial credit as reward, verifier coverage gaps, and human-held stage selection"
source: https://arxiv.org/abs/2610.22192
captured: "2026-10-18"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 4e7cc0d46166e75f9102d7d82c89c36dcd16e9d8c78b02b71db0389ee6dd71e8
ingested: "2026-10-18"
type: types/ingest-report.md
domains: [self-improving-systems, reinforcement-learning, evaluation, trace-learning]
learning_claims: true
---

# Ingest: Terminal-RSI: Recursive Self-Improving Terminal Agents

## Classification

This is a scientific paper, an arXiv preprint (2610.22192v1, 15 October 2026). It describes a training method, gives estimator derivations, and reports benchmark evaluations, offline reward rescoring, and checker-level case studies. The appendices state provenance gaps in unusual detail.
Author: Junyao Yang, Zongxia Li, Yucheng Shi and colleagues, from Tencent Hy Frontier and NUS, with Shuicheng Yan as corresponding author. The same group wrote the precursor work the paper builds on: Recursive Self-Rewrite, T1, LHTB, SWR, and the staleness-adaptive trust-region paper. The paper is therefore an integration of the group's own components, and their benchmarks are among the ones it evaluates on.

## Summary

Terminal-RSI trains a Qwen3.8-27B terminal agent through five retained stages: Base, RSR-1, RPR-1, RSR-2, and RPR-2.

- **RSR (Recursive Self-Rewrite)** is actor-only supervised training. It keeps only trajectories that pass a protected verifier. Each kept trajectory is rewritten into a runbook. A reviewer who sees only the public task screens the runbook for leakage. The current actor must then reproduce the result in a fresh public execution. The runbook and the reviewer dialogue are stripped out, and only the accepted public trajectory becomes supervision.
- **RPR (Recursive Policy-Refine)** is PPO. Its critic is carried unchanged through RSR, then recalibrated for four critic-only updates before joint training.

The paper also introduces three components:

- **TB-GAE** decays credit per interaction turn rather than per token, so verbose observations no longer shrink credit.
- **FDR (Family Dense Reward)** scales partial-check credit by task family.
- **SPR (Success-Prioritized Reward)** replaced FDR in the retained second refinement stage. It caps partial credit below the value of strict success.

The final checkpoint's mean success across four Terminal-Bench suites rises from 20.68% to 50.58%. On LHTB, strict completion rises from 0/46 to 5/46 and process reward from 0.21 to 0.37. SWR100 success rises from 3% to 6% and plateaus after RPR-1. At equal local update steps, RPR-1 started from RSR beats a direct-PPO control, but the comparison is not compute-matched.

The authors say plainly what the results do not show. Stage-specific rewards, learning rates and initialization change together. There are no compute-matched, inherited-versus-reset critic, or isolated TB-GAE controls. Evaluation uses three inference repeats rather than independent training seeds. The retained checkpoints were chosen with benchmark feedback.

Two findings matter beyond the training recipe. First, offline rescoring of 4,352 fixed trajectories finds that under FDR, failures receive 50.09% of reward mass, and 48 failures pass every executed scenario check but miss the terminal gate. Second, a case study shows the final model passing exact-output fuzz gates for a Rust–C evaluator while delegating evaluation to Python.

All gains are improvements within one tested decomposition: one backbone, the same harness, protected verifiers fixed as the outcome signal, and the stage sequence chosen by the authors.

## Contribution assessment (our opinion)

The problem matters: turning sparse, delayed verifier outcomes into policy updates for long-horizon terminal agents is a central bottleneck in agent RL. The paper's contribution is mostly integrative. It couples published primitives (verified rewriting, PPO with value warm-up, skip-observation GAE) through critic handoff and reward evolution, and it reports a strong 27B result. Its demonstrated value lies less in the headline numbers than in the error-eliminating apparatus:

- the fixed-trajectory rescoring that isolates how a reward allocates credit;
- the derivation showing that token-clock GAE decays credit by text length;
- the checker-level cases that separate passing a verifier from meeting the intended requirement.

The causal claims are weak by the paper's own account. Without compute-matched alternation, critic-reset controls, training seeds, or protected validation for checkpoint selection, the recursive coupling is a plausible conjecture, not a tested one. The comparisons with frontier models are unreconciled reference values. My guess is moderate significance: a credible recipe and some useful diagnostics, with the "recursive self-improving" framing well ahead of the evidence. I cannot place its originality relative to concurrent terminal-RL work beyond the paper's own related-work comparisons.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source has three roles in the KB: a case of verified trajectory reuse, evidence about partial credit and verifier coverage, and a boundary case for "self-improving" claims.

**Verified trajectory reuse.** RSR is a training-pipeline counterpart to [a checked outcome licenses retaining an episode, not abstracting its explanation](../theory/checked-outcome-licenses-episode-retention-not-abstraction.md) (compares-with). RSR does not trust one verified episode as reusable supervision. It rewrites the episode, screens it for leakage, and requires a fresh execution to pass the verifier again before training on it. This is extra evidence gathered by repeated outcome tests, not by inspecting the producing process.

**Partial credit and verifier coverage.** The Rust–C case, where the fuzz gates pass while evaluation is delegated to Python, is concrete evidence for [exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md). So are the 48 failures that pass every scenario check yet miss the terminal gate. Both are case evidence, not a controlled test.

The paper also continues [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.ingest.md) (compares-with on partial credit versus strict completion). LHTB used graded partial credit as evaluation evidence and left open whether feeding it to a learner helps. Terminal-RSI feeds partial credit into PPO reward. Its offline analysis shows that unsubordinated partial credit can keep rewarding incomplete behavior. Its fix is to cap partial credit below strict success.

**"Self-improving" claims.** The paper names its system "recursive self-improving", but humans still supply several decision-bearing functions. They redesigned the reward after later training steps were already visible. They set the stage-specific learning rates. They chose retained stages over discarded branches. This makes the paper evidence for [computationally directed self-improvement is a fixed-boundary reallocation](../theory/computationally-directed-self-improvement-is-a-reallocation.md): generation and filtering are computational, while evaluation and retention stay human. It is also a live instance of the "model fine-tuned by an external training pipeline" row in [the self-improving-system definition's boundary cases](../theory/the-self-improving-system-definition-classifies-its-boundary-cases.md).

The claim that "each retained stage consolidates discovered behaviors" rests only on the benchmarks that also selected each stage. That is the gap described in [compounding is tested in later improvement, not by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).

**Where learning is retained.** On this axis the source sits at the weights-only end of [treat continual learning as representational-form coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md) (compares-with). Natural-language runbooks are transient scaffolding that is removed before training. By contrast, [SkillRL](./skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) keeps a readable skill bank alongside its GRPO-trained weights (compares-with).

Like [agent optimizers compound on Terminal-Bench](./agent-optimizers-compound-terminal-bench.ingest.md), it reports staged gains on the same benchmark family without the fresh-start controls that would separate compounding from accumulation (compares-with).

Origin: [arXiv 2610.22192](https://arxiv.org/abs/2610.22192) (derived-from).

## Learning Claims (our opinion)

**Mechanism on its own terms.** What learns is the model's weights: an actor network and a critic network. Each RSR stage is a generate–filter–rewrite–re-verify–fine-tune pass in the STaR/ReST family. The filter is the protected verifier, combined with a leakage screen. Each RPR stage is clipped PPO with no KL penalty. Its advantage estimates come from a critic carried over from the previous stage, and its reward is FDR, or SPR in the retained second cycle. The paper's specific learning claims are three:

- carrying the critic through supervised transitions keeps useful return structure, provided it is recalibrated;
- turn-clock credit assignment removes decay driven by text length;
- capping partial credit below strict success shifts reward mass toward completion.

The paper supports the first only through critic explained variance, which stays positive throughout RPR-2. That shows the inherited critic was calibrated, not that inheriting it helped. It supports the second through derivations, while noting that the deployed first phase used standard GAE. It supports the third through offline rescoring of fixed trajectories. None of the three is isolated in training.

**Mapping to Commonplace concepts.** The theory-builder conditions, taken one by one:

- **Localized content: fails** for the retained learner. Weights and critic values are not units that say anything. The runbooks are localized, natural-language units, but they are transient. They are generated, screened, used to steer one execution, and then removed before training.
- **Consumption: partly met, only within RSR.** A runbook guides the fresh execution through what it says. Nothing consumes it afterwards.
- **Content-directed criticism: absent** for the retained learner. The leakage reviewer criticizes what a runbook says, but only to accept or reject it. It does not revise runbooks, and the only criticism the weights receive is gradient error. Under the definition's exclusions, this is weight adaptation, so the arrangement is outside the theory builder.
- **Iteration: met at the weight level.** Each stage's retained parameters start the next stage. This persists across runs, but none of it is a stated theory.

The closest content-directed criticism in the whole system is human. The authors read the offline rescoring, diagnosed that partial credit was misallocated, stated why, and revised the reward. They also chose stage-specific learning rates and selected checkpoints. That human loop states its reasons in the paper, so the researchers plus the training pipeline could be read as a human-staffed builder over the training recipe. The paper does not present it that way, and its reward revision was fitted with the later steps already visible.

**Learning as a separate claim.** Benchmark scores, LHTB strict completion, and training-disjoint SWR100 all improve, so improved capacity for future action is supported for this backbone and these task distributions. The caveats are that checkpoint selection used benchmark feedback and that there is only one training run. Attribution to individual components is not supported.

**Fixed decomposition.** The effective update space is the policy and critic weights, under these fixed choices:

- the harness and its JSON action interface;
- the protected verifiers as the outcome signal;
- the task pool;
- reward-family partitions, which are revised between phases by humans, not by the learner;
- the stage order.

As [learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, gains inside this space do not test the fixed choices. The Rust–C case shows one consequence. The learner optimizes against what the verifier enforces, so a requirement the verifier does not encode, a native AST evaluation path, lies outside what reward can correct.

**What it adds or questions.** The source supports the KB's view that verifier-filtered retention is extra evidence beyond a single checked outcome. It adds a concrete mechanism by which shaped partial credit misdirects a learner, distinct from noise in the oracle. It does not challenge the theory-builder account: its "recursive self-improvement" is weight iteration plus human recipe revision. The mapping of the human reward-redesign loop stays open, because the paper does not show whether that loop's criticism would generalize or was fitted to observed steps.

## Extractable Value

1. **Partial credit is useful as evaluation detail but misdirects as unsubordinated reward.** Fixed-trajectory rescoring shows that under proportional family credit, failures received 50.09% of reward mass, and 48 failures passed every executed scenario check but missed the terminal gate. Capping partial credit below strict success cut the failure share to 28.72% and eliminated failures scoring at least one. This answers, offline only, the question the LHTB ingest left open. The finding holds for this reward family and trajectory population; its effect on training is not isolated. [quick-win]
2. **A verifier certifies only what it enforces.** The final model passes exact-output fuzz gates for a Rust–C evaluator while evaluating expressions in Python. Separately, many failures pass every scenario check. Both give the exact-implementation note a compact modern case: a hard oracle certifying conformance while the intended architecture is absent. The evidence is two case studies with two repeats each. [quick-win]
3. **"Recursive self-improving" with human-held evaluation and retention.** Reward redesign was done after later steps were visible, learning rates were set per stage, and branches were discarded by checkpoint selection. These are decision-bearing functions supplied by humans, which makes the paper a worked example for the reallocation note and the self-improving-system boundary-case row. [quick-win]
4. **Verified rewriting with fresh re-execution as a retention gate.** RSR keeps a trajectory only after rewrite, a leakage review blind to private context, and an independent successful re-execution. This pattern of retention through repeated outcome tests could transfer to KB workflows that promote one verified episode into reusable procedure. Its value in the paper is not isolated from other changes. [experiment]
5. **Summarization changes conditioning; chunking does not.** The paper derives that splitting an unchanged history permits exact credit transport, while summarizing changes what later decisions are conditioned on. This is a precise statement of the difference between a lossless split and a lossy summary, but here it is an aside about estimator invariance, not a tested claim about summary sufficiency. [just-a-reference]
6. **Verbose observations shrink token-clock credit.** Under per-token GAE, two executions with identical decisions and outcomes receive different credit because one produces longer logs. This is relevant to agent-RL readers but outside KB methodology. [just-a-reference]

## Limitations (our opinion)

- **No causal attribution.** Reward, learning rate, critic initialization, and stage order change together. The authors list compute-matched alternation, inherited-versus-reset critic controls, isolated TB-GAE, and matched online reward comparisons as still needed. The recursive coupling, which is the paper's stated focus, is therefore untested as a cause.
- **The RSR-versus-PPO comparison is not compute-matched.** RSR incurs discovery and supervision costs, the direct-PPO control uses a historical protocol, and its step-zero initialization differs from Base.
- **Selection on the test benchmarks.** Retained stages were chosen with benchmark feedback, and the SPR redesign used training steps that were already observed. The gains therefore include adaptation to the evaluation, which [compounding is tested in later improvement, not by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) warns against reading as consolidation.
- **Thin replication and inconsistent provenance.** Mean@3 measures inference variability, not training variance. Historical task denominators differ across runs. The stratified analysis substitutes an alternative RSR-1 checkpoint, and the RPR-2 checkpoint used there is not reconciled with the reported one.
- **Author-built benchmarks.** LHTB, SWR, and the RSR precursor all come from the same group. The frontier-model comparisons are unreconciled reference values.
- **Limited scope.** One 27B backbone and one harness give no basis for scaling or decomposition claims. SWR100 plateaus after RPR-1, so second-cycle gains do not appear on the training-disjoint suite.
- **Offline reward evidence.** The 50.09% to 28.72% shift describes how the two rewards allocate credit on fixed trajectories. It is not evidence that SPR trains better policies.

## Recommended Next Action

Add the Rust–C delegation case and the 48 all-scenario-checks-pass failures as a bounded "illustrates" example in [exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md), grounding the source wording first through `cp-skill-ground`.
