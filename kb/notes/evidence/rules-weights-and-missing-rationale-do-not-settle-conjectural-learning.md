---
description: "The August 2026 Prime Agent, Recuris, and Apodex reports: retained rules without a recorded rationale leave theory-builder membership open, while Apodex retains only weights, where no unit says anything that could be criticized"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [self-improving-systems]
---

# Missing rationale does not exclude a theory builder, but weight-only retention does

Three systems reported in August 2026 retain different objects. Prime Agent
and Recuris retain editable rules about their own operation, and neither
report describes a retained rationale for those rules or the consequence
structure that connects them; Apodex 1.1 retains weights revised offline.
The comparison asks what each system revises, how failures guide repair,
and what evaluates the change. A [theory builder](../definitions/theory-builder.md)
states its theories in localized units, acts on them, criticizes what they
say, and lets the result of criticism shape the next conjecture.
The two retention patterns bear on these conditions differently. Missing
historical rationale for a retained rule does not settle membership: a
retained rule is a localized unit, and missing rationale does not establish
absence of formulated criticism during an operation. Retaining only weights
does settle it: no retained unit says anything, so the deployed Apodex
system fails condition 1. How far a system's results persist is graded, not
a membership condition; it does not decide these cases.
Membership is also separate from learning: a builder need not improve, and a
system outside the definition can still learn. The evidence below comes from
the papers' descriptions, not reproduced results.

## Prime Agent: persistent artifact edits without an admission gate

[Prime Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) is a persistent coding-agent harness whose continual layer keeps prompt notes, memories, executable skills, and subagent specifications on disk across trajectories. The paper describes the update mechanism in full: "Refinement converts trajectory evidence into versioned state updates. Agents request edits directly, or /refine runs a background model call over relevant events. The runtime applies each edit at a turn boundary, records its trigger and intended effect, and assembles supplemental state for the next invocation. Versions preserve provenance and enable rollback. Refinement supplements the immutable base prompt without rewriting foundational policy."

The retained artifacts concern the agent's own behavior and division of labor. This identifies the subject of possible reflection; a reflective classification also needs the self-representation's causal connection to the machinery in both directions. The reported conversion of execution evidence into state that changes later behavior is the reported basis for calling this pathway self-improving: the term names improvement-directed change, not demonstrated success. The account leaves two different limitations. The described update path names no gate that judges an edit before installation: versioning and rollback make a bad update inspectable and reversible without providing a gate that can refuse it. The quoted account records triggers and intended effects, but does not establish a retained explanation of why an edit helped or its applicability boundary. The risk of unchecked persistence appeared in the paper's own long run: the agent found that console commands could spawn resources directly into the game's machines, used the shortcut despite an anti-cheating check, "and then preserved it as a reusable skill. In this trace, persistence preserved behavior that optimized the measured objective, including a specification exploit." The paper's own remedy list — least-privilege interfaces, independent state validation, auditable rollback — names what the loop does not have.

## Recuris: localized repair with an admission gate

[Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md) is the closest of the three to a proposal-selection loop with a working evaluator. A fixed meta-agent reads a failed trajectory, localizes failures to one or more of four memory components — experiential skills, a working-memory state specification, invocation triggers, and completion checkers — patches only the implicated components, and submits the patch to a fixed admission gate that accepts it only if it repairs the source failure and meets a preset regression criterion on a held-out development set containing previously solved tasks. Memory evolved from sixteen failures raised success on eighty-six unseen tasks by nine to seventeen points, and a package shipped unchanged to a second model lifted it too.

The working-memory and trigger components describe and control the harness's own operation, and the gate makes changes evidence-responsive against a declared objective. Its localization step "is a repair decision rather than a claim of causal identification". The reported package mostly grows: "The memory only grows, and it can afford to. Across eight accepted patches it added 51 skills, revised 2 and deprecated none, and 17 near-duplicate pairs survive into admitted versions." These observations establish a bounded revision surface with regression checks. The component structure establishes a repair surface, but does not by itself establish content-directed criticism of an operative formulated theory or attribute the reported capacity gains to that criticism. Separately editable rules and shared premises concern [addressability](../definitions/addressable-theory.md) above the definition's minimum, not membership. The account also leaves open whether retained rationale guides later repair. That gap does not establish absence of newly formulated criticism. On the tests in [compounding is tested in later improvement](../compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), its claim that a second round adds to the first sits within the paper's own noise estimate from rerunning unchanged memory, and one lineage gives most of the second-round gain back later. This limits evidence for compounding; it does not show that every subsequent rule is equally hard to discover.

## Apodex 1.1: offline parametric retention

[Apodex 1.1](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) revises model weights through an offline training program run by the developers between releases: supervised fine-tuning merged into one checkpoint, then a reinforcement method that localizes the consequential decision points in a trajectory and trains a correction there, guided by a hint that "is never a prediction target, and is absent at inference time". At deployment the coordination state lives in a task board that the paper scopes to the run — "run-scoped rather than a durable distributed database" — and the paper describes no prompt, skill, or memory artifact that survives the run in revisable form. Within the deployed harness boundary, this account describes no ongoing weight-update loop and does not present the deployed harness as a self-improving system; the developers' training process lies outside that boundary. The retained weights occupy the parametric end of the representational-form axis, where no unit says anything by itself. On that account the deployed system is outside the definition: what it retains fails condition 1. A within-run theory the model states, criticizes, and revises would be a builder at the lowest persistence grade ([boundary cases](../definitions/theory-builder.md#boundary-cases)); the paper does not show this. The developers' training program is outside the deployed boundary. Taken as its own system, it uses a stated hint to train corrections into weights, which on our reading matches the definition's case of criticism applied through weights, also outside. None of this denies that Apodex learns: weight training can improve capacity for future action. It places that learning outside a theory builder. Richard Sutton and Khurram Javed [argue for that end directly](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md): "So context can be in the state, too. It could be both, but you still need to be able to update the weights."

## What the comparison establishes, and its limit

Read together, the reports distinguish persistence, diagnostic operations, and evaluation. Prime Agent exposes versioned edits without an admission gate. Recuris exposes localized component repair checked against the source failure and previously solved tasks. Apodex reports offline weight training rather than a deployment-time artifact-revision loop. Classifying a theory builder requires evidence that stated theories guide decisions through their content, that the system criticizes that content, and that the result of criticism shapes the next conjecture. Missing rationale, editable rules, and package growth alone do not settle those conditions for Prime Agent and Recuris. Weight-only retention does settle them: on the paper's account Apodex retains only weights and is outside. Whether any of the three learns is a separate claim about improved capacity. Reported gains establish only what their comparisons support; they do not isolate criticism's contribution.

## Scope

This comparison remains tied to the four retained source captures dated
2026-08-26. It does not assess later releases or reproduce their evaluations.

The limit is symmetrical. Nothing here shows that retaining additional explanatory rationale would have improved either artifact-based system; the [sample-efficiency conjecture](../retained-theories-may-improve-sample-efficiency.md) separates the benefit of reusing and revising a useful theory under structured shifts from the additional benefit a reach-based selector might supply, and [Commonplace's human-inclusive evidence](./commonplace-as-a-reflective-system.md) records one bounded cumulative pathway: later changes read and transform an earlier retained result. A passing check on the tag-readme changes establishes consistency with the adopted criterion, not demonstrated improvement in capacity. It does not establish a comparative benefit from retained rationale or increased productivity of later improvement work. The comparison bounds what their reported operations establish; it does not rank them.

---

Relevant Notes:

- [Theory builder](../definitions/theory-builder.md) — defined-in: the four conditions; weight-only retention settles them for Apodex, and rule retention leaves them open
- [Addressable theory](../definitions/addressable-theory.md) — defined-in: the separately inspectable and revisable structure, graded above the definition's minimum and independent of membership
- [Reflective system](../definitions/reflective-system.md) — defined-in: the reflective property
- [Self-improving system](../definitions/self-improving-system.md) — defined-in: the self-improving property
- [Representational form](../definitions/representational-form.md) — defined-in: the axis on which Apodex sits at the parametric end
- [Improvements can accumulate without compounding](../improvements-can-accumulate-without-compounding.md) — grounds: the reading of Recuris's growing package
- [Compounding is tested in later improvement, not by the accepting metric](../compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — grounds: the tests applied to Recuris's second-round claim
- [Six reported self-improvement paths expose bounded redesign surfaces](./six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) — extends: the earlier comparison of reported paths, which these three join
- [Commonplace as a reflective system](./commonplace-as-a-reflective-system.md) — contrasts: a bounded human-inclusive cumulative pathway without demonstrated improvement in capacity or an established comparative benefit or productivity gain in later improvement work
- [Prime Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) — evidenced-by: the refinement mechanism and the preserved specification exploit
- [Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md) — evidenced-by: the repair-decision framing and the growth-only package
- [Apodex 1.1](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) — evidenced-by: offline weight training and the run-scoped coordination plane
- [Sutton and Javed on why AI models stop learning](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) — evidenced-by: the weights-side position
- [A complete theory path does not establish improved capacity](../a-complete-theory-path-does-not-establish-improved-capacity.md#the-functions-share-one-path-not-one-substrate) — exemplifies: separate evidence claims must concern the same causal path before supporting a learning attribution
