---
description: "The improvement claim's relata are predecessor and operative-successor states and its relation is declared before the development it judges; evaluator location is a separate declaration from the learner boundary"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, learning-theory, self-improving-systems]
---

# A better-factory claim compares operative states under an antecedent assessment relation

A [software factory](./definitions/software-factory.md) undergoes experience-responsive retention when production experience causes a retained change to its reusable machinery that later work depends on, and [learns when such retention improves it](./factory-learning-is-experience-responsive-retention-that-improves.md). Retention has no quality requirement: a factory whose retained judgements are poor retains, depends, and degenerates rather than learns. Whether it got *better* is therefore its own claim with different relata and its own declarations. The claim holds between two operative states of the factory, under an assessment relation fixed before the development it judges, and its evaluator sits at a declared location that is not settled by the learner boundary.

Four declarations make a better-factory claim determinate: which states are compared, what relation they are compared under, how a state becomes the successor, and where the evaluator sits. Getting any of them from the record after the fact is where the claim goes soft.

## The relata are operative states, not the change that produced them

Three terms keep the comparison's endpoints straight.

- The **predecessor** is the factory state current when the comparison is declared.
- A **candidate** is a constructed or proposed factory that has not yet been installed. It is not a term in the comparison.
- The **operative successor** is the state that is installed and that later production and factory development depend on — [operative in the behavioral-authority sense](./definitions/operative-change.md), not merely stored.

A candidate that is generated and discarded never enters the comparison, so a better-factory claim cannot be read off a construction event. Two routes produce a successor, and they differ in where the evaluation sits relative to the causal path.

**Measurement over snapshots.** In an interleaved process — a failed task causes a note, a test, a revised rule, and a retried task, all under the running factory — there is no phase in which an unchanged factory merely accumulates experience. The successor is then a measurement boundary drawn on a continuous process, not the product of a discrete construction step. It may be the state after a period of development or after a single retained change; either way it is already operative when measured, and the measurement judges a realized trajectory rather than performing adoption.

**Candidate admission.** A factory constructed and evaluated before installation is a candidate, and the evaluation decides whether it becomes the successor. Here the assessment is an admission decision inside the causal path that determines what the factory retains.

Both routes yield the same kind of claim about the same kind of relata. They differ in whether the evaluation determined the successor or only described it, which is what the fourth declaration below turns on.

## The assessment relation is antecedent and scope-indexed

The relation has two components. The successor must meet **non-regression thresholds** on the predecessor's prior scope, and must **exceed a specified target** on at least one named production dimension.

Both are declared while only the predecessor exists. Antecedence here is the pairwise-comparison form of the condition that makes [an improvement objective a declared parameter rather than a reading taken off the result](./self-improvement-is-relative-to-a-declared-objective.md): an objective whose only available specification refers to the change it licenses is not antecedent, however intact the causal history. Without antecedence the claim is close to unfalsifiable, because a successor that differs at all differs favourably on some dimension available to be named after the fact. Fixing the dimensions and thresholds in advance is what makes the comparison capable of failing.

Scope indexing does the complementary work. Non-regression runs over the predecessor's prior scope — what that state could already do — rather than over everything the successor might be asked to do. Without the index, the requirement is either unmeetable or vacuous depending on how generously the reader reads "no worse".

The compared states span the whole production environment. Because [the deployed system rather than the model alone is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md), the successor may improve through changes to any operative part of its machinery — prompts, natural-language artifacts, code, tools, workflows, tests, evaluators — and holding model weights fixed does not put the comparison out of reach.

## Preserving a repeatable factory-development path falls out of scope indexing

When the predecessor's prior capability set includes an operative path for [factory development](./definitions/factory-development.md), non-regression over that set requires the successor to keep such a path. This is not an extra virtue bolted onto the comparison; it is what scope-indexed non-regression already says once the factory-development path is part of what the predecessor could do.

What it rules out is a one-off gain that consumes the capacity for further improvement: a successor that scores better on the target dimension while closing the route by which any later successor could be produced. Checking it means checking that [the revision path remains applicable after the transition](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) for the factory-development redesign class, not merely that the successor is editable.

This preservation requirement is weaker than compounding and is checked at a different time. Preservation is a property of the successor state, assessed at the comparison. Whether retained changes actually help produce later improvements is [tested in later episodes rather than by the metric that accepted the earlier change](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). A successor can preserve the path and still never compound.

## Evaluator location and learner boundary are separate declarations

The learner boundary declares whose causal contributions count as the factory's own learning. The evaluator location declares who or what performs the comparison. The two come apart, and the route that produced the successor is what separates them.

Measuring whether a realized change helped does not by itself place a person on the causal update path: the measurement follows the update and does not determine it. Judgment that controls installation does, because an admission decision determines what the factory retains. The same human activity — reading results and forming a verdict — falls on opposite sides depending on whether it gated the successor. So evaluator location is not recoverable from who was in the room; it has to be declared alongside the boundary.

This is also why the oracle problem for better-factory claims is sharp rather than incidental. Judging a factory's capability over its declared family is expensive; an acceptance test the constructing factory can inspect can be gamed; and if people supply the decisive acceptance judgments, the human-inclusive boundary re-enters at the headline result rather than at a labelled input.

## Neither claim entails the other

Passing the comparison establishes improvement between the two states; the open part is attribution — who or what learned. At a learner boundary that includes the operator, a passing successor is cheap: the operator can be the learner, and people improving a system from experience is ordinary engineering. A successor can even pass with no experience link at any boundary: a capable builder can produce a better factory from supplied specifications, with people holding the production knowledge that matters. Learning by the factory at the declared boundary needs retained experience from the predecessor's own production to causally enter the changes the improvement depends on, and because [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md), that link is established by manipulating it — supplying versus withholding the predecessor's retained state — not by observing that the successor scored higher.

Retention does not establish passing either: the occurrence condition is silent about quality, and even a change that improved the factory against some objective need not pass the declared comparison. Internal controls a factory places on what it retains — heuristic self-evaluation, preregistered internal comparisons, up to a proof gate — are design choices of the factory that it can choose badly, and they do not supply the improvement claim. They govern the pathway; the comparison judges the states.

## Scope

- The framework indexes and disciplines the comparison; it does not supply an oracle for it. What makes a successor genuinely better over an open family remains unresolved here.
- Antecedence blocks post-hoc dimension selection. It does not make the declared dimensions the right ones: a comparison can be properly declared in advance and still measure something that does not matter.
- The two successor routes are a declaration about how a given episode is being read, not a partition of physical processes. A real episode can be described either way, and the description determines where the evaluator sits.
- The structure — operative states as relata, an antecedent scope-indexed relation, admission distinguished from measurement, evaluator location declared apart from the learner boundary — is stated for factories because the preserved-scope clause draws on factory development being in scope. The first three parts carry to any improvement claim about a system that revises its own reusable machinery.

## Open Questions

- Whether the predecessor's prior scope can be specified precisely enough for non-regression to be checkable when the declared family is open-ended.
- Whether an evaluator can be located outside the learner boundary while still gating admission, or whether gating always places it inside.

---

Relevant Notes:

- [Factory learning is experience-responsive retention that improves the factory](./factory-learning-is-experience-responsive-retention-that-improves.md) — grounds: the retention layer whose silence about quality makes the improvement comparison a separate claim
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the indexed and antecedent conditions this applies to a pairwise state comparison
- [A repeatable operative path keeps a redesign class open to revision](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — grounds: what preserving a factory-development path requires beyond editability
- [Compounding is tested in later improvement, not by the accepting metric](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — contrasts: preservation is checked at the comparison, compounding only in later episodes
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: why a passed comparison does not identify the experience link
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places all operative production machinery inside the compared states
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — extends: what happens when the declared comparison is itself what changes
- [Operative change](./definitions/operative-change.md) — defined-in: the installed-and-depended-on condition that separates a candidate from the successor
- [Software factory](./definitions/software-factory.md) — defined-in: the compared object
- [Factory development](./definitions/factory-development.md) — defined-in: the scope element that carries the preserved-path requirement
