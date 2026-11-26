---
description: "Separates note functions stronger models can absorb—activation cues, weight-resident knowledge, and multi-step scaffolding—from durable functions such as commitments, local history, and preserved search work."
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, context-engineering, curation]
---

# Model upgrades obsolete notes by function rather than uniformly

Because [information value is observer-relative](./information-value-is-observer-relative.md), upgrading to a stronger model shifts which retained notes earn their maintenance and context cost. Obsolescence tracks the **function** a note performs for its reader, not whether the note looks abstract or concrete on the surface.

## What model upgrades can make obsolete

Stronger models erode at least three note functions on fixed tasks:

- **Attention cues for knowledge already in weights.** Some notes add no new substance; they exist only to bring one familiar, uncontested idea into focus at the right moment ([knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md)). When a newer model activates that knowledge unprompted in live work, pure reminder notes lose marginal value.
- **General knowledge and familiar principles absorbed into weights.** Immutable, authority-free expositions—tutorials, textbook patterns, and widely known design principles—are the genuinely absorbable class once newer models reproduce and apply them unaided ([parametric reproduction alone cannot replace an authoritative record](./parametric-reproduction-cannot-replace-an-authoritative-record.md)). Retaining a long prose restatement saves less work with each upgrade.
- **Goal-direction and step-horizon scaffolding.** Checklists, procedural breakouts, and intermediate guardrails that compensate for weak goal maintenance or short reliable step-count become unnecessary on fixed tasks once stronger models hold goals longer and complete more steps reliably in one go ([scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md)).

## What note value can survive an upgrade

Several note functions resist absorption because stronger general priors and longer reliable horizons do not replace them:

- **Preserved search work under discovery–verification asymmetry.** Even a stronger model operates inside bounded sessions over large search spaces. Retaining the hard-to-discover output of prior search—such as a minimal counterexample, boundary case, or contrast that separates competing explanations—can stay valuable because verifying a supplied case is cheap while rediscovering it unaided remains uncertain. [Discriminating examples may outlast principles across upgrades](./discriminating-examples-may-outlast-principles-across-upgrades.md) develops this thread and its consequences for note selection and authoring.
- **Authoritative commitments and governing selections.** Local decisions, contracts, permissions, and conventions bind future work by adoption rather than derivation ([commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md)). Even if a model memorizes their text, parametric reproduction does not transfer identity, integrity, contestability, or current authority ([parametric reproduction alone cannot replace an authoritative record](./parametric-reproduction-cannot-replace-an-authoritative-record.md)).
- **Unrecoverable local facts, history, and empirical episodes.** Project-specific constraints, observed failure traces, and decision rationale absent from training data cannot be derived from stronger general priors ([history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md); [a linked note's durable payload is what its consumption path cannot reliably supply](./linked-note-durable-payload-is-what-consumption-path-cannot-supply.md)).
- **Methodology selection, unknown-name routing, and shared vocabulary.** Unlike an uncontested reminder, selecting among *incompatible* competent approaches becomes more consequential as models improve because stronger models hold more competing methods in weights ([a capable agent needs methodology selection, not just relevant knowledge](./capable-agents-need-methodology-selection.md); [weight-resident methodologies provide context-efficient behavioral compression](./weight-resident-methodologies-compress-behavior-in-context.md)). Routing maps for names the reader does not yet know and cross-component syntheses also survive even when live source answers exact-fact queries ([seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md)), alongside registered terms that coordinate humans and agents and amortize recognition ([recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md)).
- **Frontier-shifted structure and open criticism.** When deployments respond to stronger models by assigning harder, longer-horizon work, external coordination and verification structure recurs at the new frontier ([scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md)). Likewise, open-ended critique questions that invite a reviewer to discover new objections can gain leverage from a stronger critic, unlike checklists that only guard against yesterday's mistakes.

## Scope

- This functional split identifies candidate obsolescence and durability mechanisms; it does not predict which specific notes a given upgrade absorbs. Parallel shifts happen when *tool or context* capabilities improve rather than model weights—for example, direct live-source access ([seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md)) or larger context budgets ([system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md)).
- Because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), a model reciting a principle when asked directly does not show that a note reminding it of that principle is obsolete in live work. Confirming absorption requires counterfactual withholding on representative tasks, as in the behavioral boundary test of [a linked note's durable payload](./linked-note-durable-payload-is-what-consumption-path-cannot-supply.md).
- Most real notes are mixed. One artifact can combine absorbable general exposition with a durable local fact, commitment, or discriminating example, so upgrade hygiene often means trimming to the durable payload rather than deleting the whole note—and diagnosing obsolescence removes clutter only when connected to an operative retirement path ([cheap adoption and weak retirement accumulate cost](./cheap-adoption-and-weak-retirement-accumulate-cost.md)).
- Current curation heuristics such as [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) model time-based recency decay (assigning zero decay to design notes), not capability-driven obsolescence across upgrades.

## Open Questions

- Across real model upgrades, how quickly do unprompted activation gaps shrink compared to raw knowledge gaps and step-horizon limits?
- What lightweight curation signal can flag newly absorbed notes for trimming or retirement without prematurely discarding compact cues that still carry activation lift?

---

Relevant Notes:

- [Discriminating examples may outlast principles across upgrades](./discriminating-examples-may-outlast-principles-across-upgrades.md) — extends: develops the discovery–verification asymmetry thread for why well-chosen examples can preserve search work across upgrades
- [Information value is observer-relative](./information-value-is-observer-relative.md) — grounds: note value depends on the gap between task demands and what the consuming model supplies unaided
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — grounds: explains why fixed-difficulty horizon and procedural scaffolding erodes while frontier structure recurs
- [Parametric reproduction alone cannot replace an authoritative record](./parametric-reproduction-cannot-replace-an-authoritative-record.md) — grounds: separates genuinely absorbable authority-free expositions from authority-bearing commitments
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — contrasts: warns that knowledge entering model weights does not automatically eliminate the need for contextual activation cues
- [A linked note's durable payload is what its consumption path cannot reliably supply](./linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — extends: supplies the behavioral ablation test for separating absorbed recap from durable payload
- [A capable agent needs methodology selection, not just relevant knowledge](./capable-agents-need-methodology-selection.md) — extends: explains why stronger models still require explicit selection among incompatible weight-resident approaches
- [Notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — contrasts: models time-based recency decay with zero decay on design notes, omitting capability-driven obsolescence
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — contrasts: draws a parallel functional split under unbounded context where scarcity-driven heuristic shortcuts melt while authority-bearing constraints and structural codifications endure
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — contrasts: supplies the scaling-obsolescence boundary for symbolic codifications, where exact-spec components endure while proxy-theory decompositions relax
- [Cheap adoption and weak retirement accumulate cost](./cheap-adoption-and-weak-retirement-accumulate-cost.md) — enables: obsolescence signals remove clutter only when connected to an operative retirement path with scoped disposition and migration
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: turns capability-relative omission into an author-time rule that leaves determinable choices to execution while fixing intent, constraints, and unrecoverable evidence
- [Seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md) — evidenced-by: bounded Commonplace sweep qualifying the same pattern under improved live-source access, which retired exact-fact prose while leaving unknown-name routing and cross-component synthesis
