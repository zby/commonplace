---
description: "The measurement protocol that separates a leveraged improvement loop from repeated manual maintenance: displaced measures, uptake traces, and three ablation baselines swept across corpus size and model strength"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Reflective leverage is tested in the next episode, not in the metric that accepted the change

A system that keeps revising its own instructions, indexes, and checks produces a record that looks identical under two very different hypotheses. Under the first, earlier accepted changes are making later improvement episodes cheaper — [reflective leverage](./compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md), the multiplier that turns a growing stock of retained changes into compounding. Under the second, the record is repeated manual maintenance: real work, really retained, at a per-episode cost that has not moved. The acceptance record cannot separate them, because under both hypotheses every accepted change passed its own check. Separating them requires a measurement displaced from acceptance twice over — to a *later* episode, and to a quantity *other than* the one the change was accepted against.

## The accepting metric cannot carry the leverage claim

A change is accepted because it achieves something specific: the coverage validator passes, the corrected search recipe finds the note the old recipe missed. That check evaluates the change against its own target. The leverage claim is a different proposition — that improving this machinery makes later improvement episodes cheaper, broader, more reliable, or less dependent on human judgment. It has the shape of [a proximate target's linking claim, checked for achievement rather than warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md), and it fails in the corresponding way: a recipe can be measurably better at finding notes while the next diagnosis costs exactly what the last one did.

The displacement is therefore forced, not stylistic. A reading taken on the accepting metric succeeds by construction for every correctly accepted change, so it carries zero information about leverage — the two hypotheses predict the same value. Only a quantity the change was *not* selected on can discriminate, and the earliest place such a quantity exists is the next episode that consumes the change. This is why a self-improvement result reported as "the gate now passes" or "the benchmark rose" is not yet evidence about the loop: it is evidence about the change.

## Uptake is what turns a later reading into a leverage reading

A cheaper next episode is compatible with a stronger model, an easier problem, or a maintainer who has simply done this before. What makes the drop attributable is that the later episode actually passed through the changed artifact — [the substitution test for cumulativity](./accumulation-counts-dependence-through-the-retained-result.md), narrowed to a pathway function. The protocol therefore has two parts, not one: a displaced measure, and a trace establishing consumption. A retrieval fix that later episodes never invoke has no leverage regardless of what the cost curve does, and a cost curve without an uptake trace supports a correlation and nothing stronger.

Uptake is also the cheapest half to instrument, because consumption is usually loggable — which command ran, which file entered context, which gate fired — where cost attribution is not.

## What to measure in the later episode

Each of the four improvement directions names a distinct measure, and the fifth entry is the debit that the other four omit.

| Direction | Measure in the later episode |
|---|---|
| Cheaper | Episode cost to completion — tokens, agent turns, wall-clock — for an episode of comparable class |
| Less dependent on human judgment | Count of human decisions per completed episode, and which pathway function each falls on (noticing, diagnosis, choice, acceptance) |
| More reliable | Share of episodes completing without a later retraction or repair of what they accepted |
| Broader | Classes of artifact an episode can change without bespoke human instruction |
| — (debit) | Maintenance cost: work that exists only to keep the artifact layer current, which appears in no individual episode's accounting |

Human decisions are the load-bearing denominator in a human-inclusive loop, [since what a fixed amount of human judgment buys is the quantity that actually moves as automation advances](./increasing-computational-autonomy-relocates-human-effort.md) — total hours confound allocation with ambition. Maintenance is the entry most easily lost, precisely because it is charged to no episode: an artifact layer whose upkeep consumes the judgment it saves has a flat net effect that per-episode measures alone will report as a gain.

## Three baselines, each removing a different explanation

A displaced measure with an uptake trace still needs something to be measured against, and the three plausible alternative explanations need three different comparisons.

- **Frozen-artifact variant.** Replay the later episode with the artifact layer pinned at the earlier snapshot. This is the direct ablation of the change under test, and it removes the explanation that the corpus contributed nothing to the observed drop.
- **Stronger base model, thin or absent artifact layer.** Removes the explanation that a newer model would have supplied the same content unprompted — the bitter-lesson-shaped alternative, sharpened by the observation that [scaling absorbs scaffolding at fixed difficulty rather than at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).
- **Simpler memory system.** An append-only log with no types, gates, or review. Removes the explanation that any retention at all would have done, isolating what the governance machinery buys over bare persistence.

Two conditions make the comparison fair rather than flattering. First, it must be run at **more than one point on both the corpus-size and model-strength axes**: an advantage measured once establishes an advantage at that point, and the interesting failure mode is an advantage that shrinks as either axis grows. Second, **evaluation, maintenance, and human judgment all belong on the cost side** of every arm. Omitting them compares the artifact layer's benefits against the baseline's total, which is not a comparison.

## The noticing function resists this protocol

The frozen-artifact ablation works for every pathway function downstream of episode selection — search within an episode, evaluation, retention. It does not work for noticing. A change that improved noticing, such as a status command that surfaces stale artifacts, has no counterfactual episode to replay: in the frozen variant the episode is never started, so there is no later cost to compare. Leverage on noticing is readable only as a rate — episodes initiated per window — and that rate is the measure most confounded by the maintainer's fluctuating attention.

This is a structural boundary of the protocol, not a gap in its current form. Ablation compares two executions of the same episode; a function whose output is *which episodes exist* has no such pair.

## Scope

- The protocol reads leverage over named episodes under a declared [boundary, horizon, and objective](./definitions/self-improving-system.md), and inherits the [commensurability problem that unsettles cross-time comparison](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md): the pathway's function list itself changes across the measurement window, so a matched pair of episodes is a stronger unit than an aggregate trend.
- A null result is not a failure result. Repeated manual maintenance retains real improvements and grows a real stock; the protocol distinguishes accumulation from compounding, and finding the former is a finding.
- In a human-inclusive loop the sample is small and the episodes are heterogeneous, so the design is matched pairs of comparable episodes rather than a fitted curve. The window is also long enough for a model upgrade to land inside it — a confound that mimics leverage exactly, which is what makes the stronger-model baseline mandatory rather than optional.
- The protocol tests whether leverage is present, not whether it was worth its opportunity cost. Pathway investment that displaces task improvement can be genuinely leveraged and still bad policy over a bounded horizon.
- Nothing here bears on whether an accepted change should have been accepted. Acceptance remains governed by its own check, [whose reliability bounds what may run unattended](./warranted-autonomy-is-bounded-by-oracle-domain.md); this note constrains only what the acceptance record can subsequently be read as evidence for.

## Open Questions

- Whether the displaced measures can be recovered retroactively from repository and session history, giving the protocol a cheap first run before any prospective instrumentation exists.
- How many matched episode pairs a human-inclusive loop needs before a cost difference is readable at all, given that episode heterogeneity is likely to dominate the effect being sought.
- Whether frozen-artifact replay is affordable at the frequency the protocol wants, or whether it is a rare audit that a cheaper uptake-plus-cost proxy has to stand in for between runs.

---

Relevant Notes:

- [Compounding self-improvement needs leverage to multiply and autonomy to scale](./compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md) — enables: supplies the leverage concept and the three-regime signature this note gives a measurement procedure for
- [A proximate target is checked for achievement, not for warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — grounds: the linking-claim structure that makes the accepting metric structurally unable to test leverage
- [Accumulation counts dependence through the retained result, not through the evidence it caused](./accumulation-counts-dependence-through-the-retained-result.md) — grounds: the substitution test the uptake requirement narrows to pathway functions
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — grounds: why human decisions per completed improvement, not human hours, is the denominator these measures use
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: the commensurability obstacle this protocol works around with matched episode pairs instead of solving
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — grounds: why the stronger-base-model baseline must be swept across model strength rather than measured once
- [The Meta-Harness ablation does not identify episode-backed theory formation](./the-meta-harness-ablation-bounds-summarization-not-theory-formation.md) — evidenced-by: a worked case of an ablation whose arms do not isolate the intervention claimed, showing what baseline design has to get right
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: bounds what an acceptance check licenses; this note bounds what the acceptance record evidences afterwards
- [Commonplace as a reflective self-improving system](../reference/commonplace-as-a-reflective-system.md) — evidenced-by: the human-inclusive loop whose tag-readme episode predicted leverage on retrieval and evaluation without measuring whether the next episode ran cheaper
