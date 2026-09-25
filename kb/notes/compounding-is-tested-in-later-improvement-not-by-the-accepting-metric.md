---
description: "Compounding evidence must come from later improvement episodes through displaced productivity measures and causal traces, not from the metric that accepted the earlier change"
type: note
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Compounding is tested in later improvement, not by the accepting metric

A self-improving system keeps revising its own instructions, indexes, and checks. To say its improvements [compound](./improvements-can-accumulate-without-compounding.md) is to say more than that they add up. It says that earlier improvements make later improvements easier to produce.

This note states what evidence can support that claim. The short answer has three parts. The evidence must come from a *later improvement episode*. It must be measured on a quantity *other than the check that accepted the earlier change*. And it must connect the later episode to the earlier change through a *causal trace*. The sections below add these requirements one at a time using a single illustrative example, and then use them to read three published studies.

## A running example

The example is hypothetical and deliberately small.

**Episode 1 (week 1).** An agent maintaining a KB notices that its standard search recipe misses notes whose tags are written as a YAML list. It fixes the recipe. The fix is accepted because the new recipe finds a note the old recipe missed. "Finds the missed note" is the **accepting metric**: the check that decided this change should be kept.

**Episode 2 (week 5).** The agent gets a different improvement task: diagnose why two closely related notes were never linked, and repair the cause.

The compounding question is whether the week-1 fix made episode 2 easier.

## The acceptance record cannot answer the question

Two accounts fit week 1 equally well:

- **Compounding.** The fix keeps paying off. Diagnoses like episode 2 become cheaper because search is now better.
- **Repeated maintenance.** The fix is real and is retained, but episode 2 costs what it would have cost anyway. Each new revision is as difficult as the last.

Under both accounts the fix passed its accepting metric, and so does every later accepted change. So the record of accepted changes looks the same under both accounts, however long it grows.

The reason is that the accepting metric and the compounding claim test different things. The accepting metric checks whether the change achieved its immediate target. The compounding claim says that the retained benefit helped produce a later improvement by making that work cheaper, broader, more reliable, or less dependent on human judgment. This has the shape of [a proximate target's linking claim](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md). The recipe can be measurably better at finding notes while the next diagnosis costs exactly what the last one did. A benchmark increase is evidence about the accepted change, not yet evidence about the productivity of later improvement work.

## Requirement 1: look at a later improvement episode

The evidence has to come from episode 2, not from episode 1. Episode 2 must itself be improvement work, such as a diagnosis that ends in a retained change. Ordinary task use of the better recipe shows that the change is useful. It does not show that improvement became easier.

## Requirement 2: measure something other than the accepting metric

Re-running "does the recipe find the missed note" in week 5 only re-confirms episode 1. Episode 2 has to be measured on its own productivity. The measurement is therefore **displaced** twice: in time, to a later episode, and in quantity, away from the accepting metric.

| Direction | Measure in the later episode |
|---|---|
| Cheaper | Episode cost to completion: tokens, agent turns, wall-clock time, or compute for a comparable episode |
| Less dependent on human judgment | Human decisions per completed episode, classified by noticing, diagnosis, choice, or acceptance |
| More reliable | Share of episodes completing without later retraction or repair of what they accepted |
| Broader | Classes of artifact an episode can change without bespoke human instruction |
| Reinvestment | Saved time, compute, or judgment that is subsequently spent on improvement work |
| Maintenance debit | Work performed only to keep the retained artifacts current |

In the example, the natural measures are the turns episode 2 needed and the number of times a human had to point the agent to a note.

Human decisions are the load-bearing denominator in a human-inclusive loop because [automation changes what a fixed amount of judgment buys](./increasing-computational-autonomy-relocates-human-effort.md).

Maintenance is easily omitted because it belongs to no single episode. A set of retained artifacts whose upkeep consumes the effort it saves may show a gross gain and no net gain.

## Requirement 3: connect the two with a causal trace

Suppose episode 2 took 12 turns, while comparable diagnoses used to take 30. That number alone fits several explanations. The model may have been upgraded. The problem may have been easier. The maintainer may simply have gained experience. Crediting the gain to the fix needs two kinds of evidence: a trace showing that episode 2 used the fix, and a baseline showing how much the gain depends on it. This section covers the trace; the baselines come next.

### Direct trace

The trace is direct when the later episode uses the retained change itself. It reads the revised theory, invokes the validator, follows the changed procedure, or costs less because an earlier improvement now performs part of the work. In the example, episode 2's transcript would show the agent running the new recipe, and the note it found would be the one that resolved the diagnosis. The [substitution test for cumulativity](./accumulation-counts-dependence-through-the-retained-result.md) handles this direct consumption.

### Indirect trace

The trace is indirect when the earlier change helps by freeing resources that improvement work later spends. Suppose that before the fix, the maintainer spent about an hour each week searching by hand for notes the recipe missed. The indirect trace then has three links:

1. **Freed capacity.** An earlier gain frees time, compute, or judgment, or preserves capacity that would otherwise be spent restoring lost performance. In the example, the weekly hour is freed.
2. **Reinvestment path.** An allocator or reinvestment path makes that capacity available to improvement work. In the example, the maintainer puts the hour into the improvement queue rather than into another project.
3. **Consumption.** Later search consumes it while finding, testing, or refining another change. In the example, the hour is spent on episode 2 or on another change.

This mechanism assumes that such a path exists and that no other bottleneck caps improvement throughput. A fixed budget or an unspent saving can satisfy the first link while leaving the other two absent. If the hour goes to another project, or if review bandwidth caps how many improvements land regardless, the fix saved time but did not feed later improvement. Indirect reinvestment therefore needs the resource path to be observed rather than assumed.

### What the test combines

The test combines a displaced measure with a direct or indirect trace. A changed artifact that later work never uses contributes nothing through the direct path. A cost curve without either kind of trace supports correlation, not the claimed feedback.

## Three baselines remove different explanations

A trace shows that the later episode used the earlier change. A baseline shows how much that use mattered. Each baseline removes a different alternative explanation for the 12-versus-30 difference.

- **Frozen-artifact variant.** Replay the later episode with the retained artifacts pinned at the earlier snapshot. In the example, rerun episode 2 with the old recipe. This tests whether the retained change contributed anything.
- **Stronger base model with few or no retained artifacts.** This tests whether a newer model would have supplied the same capability unprompted, for example by searching list-form tags without being told to. Because public artifacts may enter later training data, the design needs post-cutoff tasks, checks for reproduction specific to the retained artifacts, or a private-corpus arm.
- **Simpler memory system.** Compare against an append-only log with no types, gates, or review to distinguish structured retention from bare persistence.

The comparisons must include evaluation, maintenance, and human judgment on the cost side. They should also be repeated across corpus sizes and model strengths: an advantage observed at one point may disappear as either grows.

## Noticing resists paired replay

A frozen-artifact replay works only after an improvement episode exists. Some changes improve noticing instead. Suppose the week-1 change had been a status command that surfaces stale artifacts. Such a change alters which episodes are initiated. In the frozen variant, episode 2 might never start, which leaves no matched pair to compare.

The contribution of such a change is therefore read through rates, such as relevant episodes initiated per window, plus a trace showing what surfaced them. Fluctuating maintainer attention confounds such rates especially strongly. That paired replay cannot test noticing is a structural boundary of the method, not a reason to assume the contribution.

## Reading published studies against the requirements

The requirements give a checklist. A study can satisfy some items and miss others:

- **Accepted.** The change passes its own check.
- **Retained.** The change is still present when later work happens.
- **Taken up.** A later improvement episode uses it directly or consumes resources it freed.
- **Displaced gain.** That later episode does better on a measure other than the accepting metric.
- **Attributed.** A baseline shows the gain shrinks or disappears without the earlier change.
- **Sustained.** The previous three items hold across successive episodes.

Uptake, displaced gain, and attribution are joint requirements, not steps taken in order. One later episode that meets all three is local evidence of compounding. Only a sequence of such episodes is evidence that compounding is sustained.

### HyperAgents shows one bundled cross-domain contribution

The [HyperAgents transfer experiment](https://ar5iv.labs.arxiv.org/html/2603.19461#52-improving-the-ability-to-improve), summarized in the [ingest](../sources/hyperagents.ingest.md), comes close to this test. The authors selected one transfer hyperagent from each of five joint paper-review and robotics runs, moved them into unseen math grading, and ran 50 later agent-generation steps with DGM-H without self-improvement. In that baseline the meta agent that modifies hyperagents is held fixed for the entire run. Median Improvement@50 reached 0.630 (95% bootstrap CI 0.540–0.630), significantly above the initial hyperagent.

The uptake is direct: the transferred improvement procedure generates the later agents. The measure is displaced to a new domain rather than reusing the source-run score. This establishes one cross-domain link in which an earlier retained improvement procedure helps produce later improvements. It does not isolate which bundled task- and meta-agent changes caused the gain. Continued evolution from transferred rather than fresh hyperagents reached 0.640 versus 0.610. The difference was not statistically significant, so sustained compounding remains unestablished ([HyperAgents experiment (snapshot required)](../sources/hyperagents.ingest.md)).

### Agent Optimizers stops before attribution

The [two-phase Agent Optimizers study](../sources/agent-optimizers-compound-terminal-bench.ingest.md) uses *compounding* for a related but different property. A first optimization round must produce gains that transfer to new tasks. A second, equal-budget round must then improve the retained agent on the expanded task set without erasing earlier successes. RELAI-VCL is the only tested method that shows both: its pass rate is 79.2% after Phase 1, 72.7% on the expanded set before further optimization, and 77.3% after Phase 2. This protocol usefully separates static gain, transfer, and later re-optimization.

Under this note's causal definition, that sequence establishes retained, transferable gains followed by another successful update. It does not yet show that the Phase-1 gain helped produce the Phase-2 improvement. Every Phase-2 run starts from its method's Phase-1 agent, and there is no equally budgeted fresh-start run on the combined task set ([Agent Optimizers protocol (snapshot required)](../sources/agent-optimizers-compound-terminal-bench.ingest.md)). The later result could therefore come from the optimizer's independent strength rather than from productivity supplied by the earlier gain.

The two meanings become compatible if the indirect mechanism is added and measured. Retained competence, or regression control inside the optimization loop, could spare Phase-2 search from reacquiring old capabilities or repairing regressions. That would save rollout budget, compute, or evaluation effort. For the saving to count, an allocator would have to make it available to later improvement search, and that search would have to consume it. The saved resource must be usable, and no other bottleneck may cap progress. The study gives each phase a fixed budget of 200 rollouts and reports no reinvestment trace. It therefore leaves this mechanism possible but not established.

### Harness Benefit stops at task gain

The [Harness Updating Is Not Harness Benefit study](../sources/harness-updating-is-not-harness-benefit.ingest.md) separates producing a persistent update from a task-solving agent benefiting from it. This supplies a useful measurement ladder: update production → persistent retention → artifact loading → judged procedural match → task benefit. Its loading and benefit stages happen in ordinary task-solving, not in a later improvement episode. They are therefore not the uptake this note requires. A missing earlier stage can explain a missing benefit. Observing a later stage does not by itself show that the loaded artifact caused the behavior or gain.

The study supports its outcome comparison by cross-pairing evolvers with task-solving agents under controlled conditions. Its update and benefit metrics hold for the tested pairings, with prompts, editable surfaces, task streams, and anchor sets held fixed. Under those conditions, the measurements locate which stage of the ladder falls short.

On SkillsBench, the study reports skill loading separately from adherence. Its harness-following rate is assigned by a Sonnet 4.6 judge using a generated rubric, without a matched condition that withholds or replaces the target skill ([Harness Updating experiment (snapshot required)](../sources/harness-updating-is-not-harness-benefit.ingest.md)). It therefore measures judged procedural match, not the causal effect of the skill's content.

Compounding adds a distinct final step: task benefit → causal contribution to a later improvement episode. Harness benefit is therefore necessary for compounding through a task-side gain, but it is not sufficient. The final step can close in two ways. The later improvement episode can take up the benefit directly. Or an observed allocator can make resources that the benefit freed or preserved available to improvement work, and later search can consume them. The study does not observe this final feedback step.

## Scope

- A null result still leaves real accumulated improvement. The test distinguishes retained gains from gains that help produce further ones.
- Human-inclusive samples are small and heterogeneous, so matched episodes are usually stronger than a fitted aggregate trend.
- A measured contribution can still be bad policy if investment in improvement displaces more valuable task improvement.
- Nothing here decides whether the earlier change should have been accepted. Acceptance remains bounded by its own warrant. This note constrains what the acceptance record can later support.

## Open Questions

- Whether displaced measures and reinvestment traces can be recovered retroactively from repository and session history.
- How many matched episodes are needed before heterogeneity stops dominating the effect.
- Whether frozen-artifact replay is affordable often enough, or must be approximated between occasional audits.

---

Relevant Notes:

- [Improvements can accumulate without compounding](./improvements-can-accumulate-without-compounding.md) — grounds: supplies the feedback claim this test checks
- [A proximate target is checked for achievement, not for warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — grounds: explains why the accepting metric cannot test the later linking claim
- [Accumulation counts dependence through the retained result, not through the evidence it caused](./accumulation-counts-dependence-through-the-retained-result.md) — grounds: supplies the substitution test for direct uptake
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — grounds: explains the human-decision denominator
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: supplies the commensurability obstacle this test works around with matched episodes
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — grounds: motivates the stronger-model baseline
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: explains why an instruction-present adherence judgment is not a causal uptake effect and why bundle comparisons cannot isolate a component
- [Ingest: HyperAgents](../sources/hyperagents.ingest.md) — evidenced-by: freezes transferred improvement machinery in a new domain and measures its later agent-generation productivity
- [Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../sources/agent-optimizers-compound-terminal-bench.ingest.md) — evidenced-by: separates transfer and later re-optimization while leaving the earlier gain's causal contribution untested
- [Ingest: Harness Updating Is Not Harness Benefit](../sources/harness-updating-is-not-harness-benefit.ingest.md) — evidenced-by: separates update production, artifact loading, judged procedural match, and task benefit while leaving causal uptake and benefit-to-later-improvement feedback untested
- [Ingest: A Poetiq Perspective on Recursive Self-Improvement (snapshot required)](../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) — evidenced-by: reports sequential benchmark wins and retained cross-task strategies as compounding without a removal, fresh-start, or displaced later-episode comparison
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: bounds what may run unattended rather than what later evidence establishes
- [Commonplace as a reflective self-improving system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: supplies human-inclusive candidate episodes whose compounding contribution remains unmeasured
- [Ablation baselines for the declared objective](../reference/proposals/ablation-baselines-for-the-declared-objective.md) — see-also: supplies objective-level ablation designs complementary to these later-episode comparisons
- [Citing retained theory at the decision point is a mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — extends: the cheap uptake side of the causal trace this test requires, and what a citation alone leaves open
