---
description: "Compounding evidence must come from later improvement episodes through displaced productivity measures and causal traces, not from the metric that accepted the earlier change"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Compounding is tested in later improvement, not by the accepting metric

A system that keeps revising its own instructions, indexes, and checks produces a record compatible with two hypotheses. Earlier accepted changes may be helping to produce later improvements, so [the pathway compounds](./improvements-can-accumulate-without-compounding.md). Or the record may be repeated maintenance: real improvements, really retained, while each new revision remains just as difficult. The acceptance record cannot separate them because every accepted change passed its own check under both hypotheses.

The measurement must therefore be displaced twice: to a *later improvement episode*, and to a quantity *other than* the one that accepted the earlier change.

## The accepting metric tests the change, not compounding

A change is accepted because it achieves something specific: a coverage validator passes, or a corrected search recipe finds a note the old recipe missed. That check evaluates the change against its immediate target. The compounding claim is different: the retained benefit helped produce a later improvement by making that work cheaper, broader, more reliable, or less dependent on human judgment.

This has the shape of [a proximate target's linking claim](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md). A recipe can be measurably better at finding notes while the next diagnosis costs exactly what the last one did. A benchmark increase is evidence about the accepted change, not yet evidence about the productivity of the improvement pathway.

## A later episode also needs a causal trace

A cheaper next episode is compatible with a stronger model, an easier problem, or a maintainer who has simply gained experience. Attribution requires a trace from the earlier retained change to the later improvement.

The trace may be direct: the later episode reads the revised theory, invokes the validator, follows the changed procedure, or costs less because an earlier improvement now performs part of the work. An indirect trace has three links. An earlier gain frees time, compute, or judgment, or preserves capacity that would otherwise be spent restoring lost performance. An allocator or reinvestment path makes that capacity available to improvement work. Later search then consumes it while finding, testing, or refining another change. This mechanism assumes that such a path exists and that another bottleneck does not fix improvement throughput. A fixed budget or an unspent saving can satisfy the first link while leaving the other two absent. The [substitution test for cumulativity](./accumulation-counts-dependence-through-the-retained-result.md) handles direct consumption; indirect reinvestment additionally needs the resource path to be observed rather than assumed.

The protocol therefore combines a displaced measure with an uptake or reinvestment trace. A changed artifact that later work never uses contributes nothing through the direct path. A cost curve without either kind of trace supports correlation, not the claimed feedback.

## HyperAgents shows a cross-domain contribution to compounding

The [HyperAgents transfer experiment](../sources/hyperagents.md#52-improving-the-ability-to-improve), summarized in the [ingest](../sources/hyperagents.ingest.md), comes close to this protocol. The authors transferred whole hyperagent implementations from joint paper-review and robotics runs into unseen math grading, held each transferred meta-agent component fixed, and used it for 50 later agent-generation steps. Across five runs, median Improvement@50 reached 0.630 (95% bootstrap CI 0.540–0.630), significantly above the initial hyperagent.

The uptake is direct: the transferred improvement procedure generates the later agents, and the measure is displaced to a new domain rather than reusing the source-run score. This establishes one cross-domain link in which an earlier retained improver helps produce later improvements. It does not isolate which bundled task- and meta-agent changes caused the gain. Continued evolution from transferred rather than fresh hyperagents reached 0.640 versus 0.610, but the difference was not statistically significant, so sustained compounding remains unestablished.

## Agent Optimizers tests a different compounding property

The [two-phase Agent Optimizers study](../sources/agent-optimizers-compound-terminal-bench.ingest.md) uses *compounding* for a related but different property. A first optimization round must produce gains that transfer to new tasks. A second, equal-budget round must then improve the retained agent on the expanded task set without erasing earlier successes. RELAI-VCL is the only tested method that shows both: its pass rate is 79.2% after Phase 1, 72.7% on the expanded set before further optimization, and 77.3% after Phase 2. This protocol usefully separates static gain, transfer, and later re-optimization.

Under this note's causal definition, that sequence establishes retained, transferable gains followed by another successful update. It does not yet show that the Phase-1 gain helped produce the Phase-2 improvement. Every Phase-2 run starts from its method's Phase-1 agent, and there is no equally budgeted fresh-start run on the combined task set. The later result could therefore come from the optimizer's independent strength rather than from productivity supplied by the earlier gain.

The two meanings become compatible if an indirect mechanism is added and measured. Retained competence or in-loop regression control could spare Phase-2 search from reacquiring old capabilities or repairing regressions. An allocator would then have to make the saved rollout budget, compute, or evaluation effort available for new improvement, and the later search would have to consume it. This assumes that the saved resource is usable and that progress is not capped by another bottleneck. The study fixes each phase at 200 rollouts and reports no reinvestment trace, so it leaves this mechanism possible rather than established.

## Harness benefit reaches task gain, not causal uptake or feedback

The [Harness Updating Is Not Harness Benefit study](../sources/harness-updating-is-not-harness-benefit.ingest.md) separates producing a persistent update from a task-solving agent benefiting from it. This supplies a useful measurement ladder: update production → persistent retention → artifact loading → judged procedural match → task benefit. A missing earlier stage can explain a missing benefit. Observing a later stage does not by itself show that the loaded artifact caused the behavior or gain.

Compounding adds a distinct final edge: task benefit → causal contribution to a later improvement episode. Harness benefit is therefore necessary for compounding through a task-side gain, but it is not sufficient. The final edge can close when the later improver directly takes up the benefit, or when an observed allocator makes resources freed or preserved by the benefit available to improvement work and later search consumes them.

The study supports the outcome comparison through controlled evolver-agent cross-pairing and, on SkillsBench, reports skill loading separately from adherence. Its harness-following rate is assigned by a Sonnet 4.6 judge using a generated rubric, without a matched condition that withholds or replaces the target skill. It therefore measures judged procedural match, not the causal effect of the skill's content. The update and benefit metrics remain relative to the tested pairings, while prompts, editable surfaces, task streams, and anchor sets stay fixed. The measurements localize shortfalls within that decomposition; they do not observe the final feedback edge.

## What to measure in the later episode

| Direction | Measure in the later episode |
|---|---|
| Cheaper | Episode cost to completion: tokens, agent turns, wall-clock time, or compute for a comparable episode |
| Less dependent on human judgment | Human decisions per completed episode, classified by noticing, diagnosis, choice, or acceptance |
| More reliable | Share of episodes completing without later retraction or repair of what they accepted |
| Broader | Classes of artifact an episode can change without bespoke human instruction |
| Reinvestment | Saved time, compute, or judgment that is subsequently spent on improvement work |
| Maintenance debit | Work performed only to keep the retained artifact layer current |

Human decisions are the load-bearing denominator in a human-inclusive loop because [automation changes what a fixed amount of judgment buys](./increasing-computational-autonomy-relocates-human-effort.md). Maintenance is easily omitted because it belongs to no single episode; an artifact layer whose upkeep consumes the effort it saves may show a gross gain and no net gain.

## Three baselines remove different explanations

- **Frozen-artifact variant.** Replay the later episode with the artifact layer pinned at the earlier snapshot. This tests whether the retained change contributed anything.
- **Stronger base model with a thin or absent artifact layer.** This tests whether a newer model would have supplied the same capability unprompted. Because public artifacts may enter later training data, the design needs post-cutoff tasks, checks for layer-specific reproduction, or a private-corpus arm.
- **Simpler memory system.** Compare against an append-only log with no types, gates, or review to distinguish structured retention from bare persistence.

The comparisons must include evaluation, maintenance, and human judgment on the cost side. They should also be repeated across corpus sizes and model strengths: an advantage observed at one point may disappear as either grows.

## Noticing resists paired replay

A frozen-artifact replay works only after an improvement episode exists. A change that improves noticing—for example, a status command that surfaces stale artifacts—changes which episodes are initiated. In the frozen variant the later episode may never start, leaving no matched pair.

Its contribution is therefore read through rates such as relevant episodes initiated per window, plus a trace showing what surfaced them. Such rates are especially confounded by fluctuating maintainer attention. This is a structural boundary of paired replay, not a reason to assume the contribution.

## Scope

- One later episode can provide local evidence of compounding; several successive episodes show whether it is sustained over time.
- A null result still leaves real accumulated improvement. The protocol distinguishes retained gains from gains that help produce further ones.
- Human-inclusive samples are small and heterogeneous, so matched episodes are usually stronger than a fitted aggregate trend.
- A measured contribution can still be bad policy if pathway investment displaces more valuable task improvement.
- Nothing here decides whether the earlier change should have been accepted. Acceptance remains bounded by its own warrant; this note constrains what the acceptance record can later support.

## Open Questions

- Whether displaced measures and reinvestment traces can be recovered retroactively from repository and session history.
- How many matched episodes are needed before heterogeneity stops dominating the effect.
- Whether frozen-artifact replay is affordable often enough, or must be approximated between occasional audits.

---

Relevant Notes:

- [Improvements can accumulate without compounding](./improvements-can-accumulate-without-compounding.md) — grounds: supplies the feedback claim this protocol tests
- [A proximate target is checked for achievement, not for warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — grounds: explains why the accepting metric cannot test the later linking claim
- [Accumulation counts dependence through the retained result, not through the evidence it caused](./accumulation-counts-dependence-through-the-retained-result.md) — grounds: supplies the substitution test for direct uptake
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — grounds: explains the human-decision denominator
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: supplies the commensurability obstacle this protocol works around with matched episodes
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — grounds: motivates the stronger-model baseline
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: explains why an instruction-present adherence judgment is not a causal uptake effect and why bundle comparisons cannot isolate a component
- [Ingest: HyperAgents](../sources/hyperagents.ingest.md) — evidenced-by: freezes transferred improvement machinery in a new domain and measures its later agent-generation productivity
- [Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../sources/agent-optimizers-compound-terminal-bench.ingest.md) — evidenced-by: separates transfer and later re-optimization while leaving the earlier gain's causal contribution untested
- [Ingest: Harness Updating Is Not Harness Benefit](../sources/harness-updating-is-not-harness-benefit.ingest.md) — evidenced-by: separates update production, artifact loading, judged procedural match, and task benefit while leaving causal uptake and benefit-to-later-improvement feedback untested
- [Ingest: A Poetiq Perspective on Recursive Self-Improvement](../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) — evidenced-by: reports sequential benchmark wins and retained cross-task strategies as compounding without a removal, fresh-start, or displaced later-episode comparison
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: bounds what may run unattended rather than what later evidence establishes
- [Commonplace as a reflective self-improving system](../reference/commonplace-as-a-reflective-system.md) — evidenced-by: supplies human-inclusive candidate episodes whose compounding contribution remains unmeasured
- [Ablation baselines for the declared objective](../reference/proposals/ablation-baselines-for-the-declared-objective.md) — see-also: supplies objective-level ablation designs complementary to these later-episode comparisons
