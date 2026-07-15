---
description: "Definition — operative, evidence-responsive change to a system's own behavior-determining organization; the central distinction is reflective versus non-reflective self-improvement, pathway-relative"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** makes operative changes to its own behavior-determining organization, where those changes are causally responsive to evidence bearing on an **improvement objective**.

*Its own* means the object of change is the system's behavior-determining structure — its organization, its artifacts, its rules — not an external work product. A compiler that optimizes programs is not self-improving; a compiler pipeline that rewrites its own optimizer is. This is Ashby's two-loop distinction: operating a system is one loop, modifying the system that operates is another.

*Operative* means the change persists and acquires a consumer, a channel, and a force, in [behavioral authority](./behavioral-authority.md) terms — a transient compensation, or a change nothing ever acts on, does not qualify.

*Responsive to evidence* can be realized in two ways, and the definition requires either, not both:

- **Direct determination.** Evidence determines the update itself, as in gradient-, reward-, error-, or viability-driven adaptation: the update rule computes the change from the evidence, and every update is adopted.
- **Evaluation and selection.** Evidence is used to evaluate candidate changes and select among them, with the possibility that a candidate is not adopted.

A separately represented candidate, evaluator, rejection decision, or acceptance gate is therefore **not** required by the base definition. What is required is the objective:

> An improvement criterion is required semantically; an explicit evaluator is not required architecturally.

There must be something the evidence *bears on* — a loss function, a reward channel, viability bounds, a test suite, a rubric, a maintainer's standard — or the changes are merely caused, not improvement-directed. But that criterion need not be implemented as a component that judges candidates. [Ashby's Homeostat](../../sources/ashby-design-for-a-brain-ultrastability.md) has no evaluator anywhere in its mechanism: its criterion — keeping the essential variables within viable bounds — is what the physical dynamics respond to, and the surviving configuration is retained by equilibrium, not by anything's endorsement.

Online gradient methods are the canonical formal case of the direct arm. In [Zinkevich's online convex programming](https://dl.acm.org/doi/10.5555/3041838.3041955) (ICML 2003), each round's just-revealed cost function yields a gradient that directly moves the operative point; every step is adopted, and the method still carries a no-regret guarantee — objective-derived improvement with provable outcomes and no accept/reject gate anywhere. A policy improved by self-play is the same shape at scale. All of these are self-improving systems, and none contains a part whose job is to reject.

## The central distinction: reflective versus non-reflective

Self-improvement divides by *how the change reaches the operative substrate*, and this is the distinction the vocabulary is organized around:

- **Reflective self-improvement** — the relevant change is mediated through a writable, causally connected self-representation of the aspect being changed. The machinery is [reflection plus intercession](./reflective-system.md), grounded in [Maes's account](../../sources/maes-concepts-and-experiments-computational-reflection-1987.ingest.md) of causal connection — operations on the representation affect the system it represents. The change lands in an artifact the system also reads as a representation of itself, so what was retained is available to later work as knowledge rather than only as a setting.
- **Non-reflective self-improvement** — the operative substrate changes without the change being routed through such a self-representation. Weight updates, retained parameter settings, and equilibrium configurations are the common cases: the change steers later behavior, and nothing inside the system can read it as a claim.

The distinction is **pathway- and aspect-relative, not a partition of systems**. One system may improve some aspects reflectively and others non-reflectively: an agent platform that fine-tunes its model on its own trajectories (non-reflective) while also revising its own skill files and routing rules (reflective) is doing both at once, and a placement that assigns the whole system one label loses exactly the information that matters. Attribute the property to a named improvement pathway or aspect; a system-level attribution is shorthand for the pathways under discussion.

Neither side is a membership test. A weight-level learner is fully a self-improving system; so is a maintained codebase whose changes all pass through prose and code the team reads. What the reflective side buys is not membership and not even compounding — parametric loops compound — but *addressability*: retention that later rounds can inspect, criticize, selectively revise, and transfer. That thesis has content and stays contestable rather than definitional; it lives in [reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md). And the machinery alone delivers nothing: a Smalltalk image has reflection maximally — the compiler editable with the compiler — and left alone it improves nothing for a decade, because nothing in it responds to evidence about an objective. Put the programmer inside the declared boundary and the pathway closes, reflectively.

## The proposal-selection improvement loop

One architecture for evidence-responsiveness is important enough to carry a reserved name. In a **proposal-selection improvement loop**, candidate changes are generated, evaluated with a possibility of non-adoption, and selectively made operative. [Such a loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md): something brings a candidate into consideration, something can *reject* it against the improvement objective, and the accepted change acquires behavioral authority.

This is a subtype, not the definition — but it is where a distinctive body of machinery and risk lives, because it is the architecture in which the improvement criterion *is* implemented as an evaluator:

- **Oracle** is the shorthand for whatever supplies the evaluator's evidence or judgment — proof, test, validator, measurement, rubric, model judge, human review — and [oracles are graded by what their acceptance can establish](../oracle-strength-spectrum.md).
- Rejection is what makes the gate a gate: an unconditional trigger is not an evaluator, and search and evaluation fail asymmetrically, [since false-positive generation is filtered while false-positive acceptance becomes operative](../false-positive-generation-is-filtered-before-retention.md).
- The gate is also where unattended operation is bounded: [the boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md), and [warranted autonomy is bounded by oracle reach](../warranted-autonomy-is-bounded-by-oracle-reach.md).

The [Gödel machine](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) is a proposal-selection loop under the strongest available oracle; [Commonplace](../../reference/commonplace-as-a-reflective-system.md) is one with humans at search and the judgment-heavy evaluation. Direct-determination self-improvers stand outside the subtype: a gradient step is never rejected, so the subtype's gate vocabulary does not describe them — which is a reason to name the subtype, not a reason to read them out of the category.

## What responsiveness establishes

Aiming at the objective is all that membership requires, and aiming establishes less than it seems to:

> Evidence-responsiveness makes a system improvement-directed; only outcomes make it improving.

In a proposal-selection loop this takes the familiar form — evaluator acceptance is an *improvement claim*, not evidence that improvement occurred, because the criterion the oracle applied may be wrong, partial, or measuring the wrong thing. The direct-determination form is the same point without the gate: a learner faithfully descending a mis-specified loss is exactly as improvement-directed and exactly as capable of getting worse. A self-improving system is one that *aims* at improvement and can be wrong about it.

## Autonomous self-improving system

Autonomy asks a different question: how much of the improvement pathway runs without a person? It is assessed pathway by pathway against a declared boundary, and it grades a self-improving system without deciding whether it is one. The declared boundary may contain humans: a maintained codebase with its dev team is genuinely a self-improving system, human-inclusive and fully un-autonomous — [which is cheap to satisfy, and why bare classification discriminates little](../human-inclusive-boundaries-make-reflection-cheap.md).

**Autonomous self-improving system** is reserved for the case where the declared boundary contains no human component. Moving the boundary moves the reading, which is why the boundary must be declared before the grading means anything. Bare autonomy is cheap at the floor — the Homeostat runs unattended — so the attribution that discriminates is not autonomy but *warranted* autonomy, and the interesting occupants are composites: the Gödel machine's improvement pathway is reflective and autonomous under the strongest available oracle; Commonplace's is reflective and human-inclusive.

In a proposal-selection loop, autonomy has a trap worth naming, because two ways of automating the gate look alike and are not. *Remove* the evaluator — replace it with an unconditional accept — and the selection architecture is gone; whether the system is still self-improving then depends on whether evidence-responsiveness survives elsewhere in the pathway (an evidence-driven generator can carry it), and if nothing responds to evidence the system drops to plain self-modification. *Weaken* the evaluator — a soft rubric, a model judge, a shallow test — and the loop closes exactly as before: a fallible evaluator still rejects some candidates, so the system stays fully self-improving. It is simply wrong more often, and its errors are the ones that survive, [since false-positive acceptance becomes operative](../false-positive-generation-is-filtered-before-retention.md). The first is an architecture change; the second is a quality failure that leaves the system inside the category, degrading. Unwarranted autonomy is always available and always cheap.

## Exclusions

**Self-improving is not self-modifying.** A blind, accidental, or unconditional rewrite changes later behavior without being responsive to any evidence bearing on an objective. It is self-modification with no direction.

**Self-improving is not regulation.** A thermostat changes its environment, not its organization: the setpoint, hysteresis band, and switching rule never change, so there is no retained change to the system for evidence to have shaped. Switching the heater on is transient control output. This is Ashby's own line, drawn with this example — the thermostat is his canonical regulator, and ultrastability, the second loop that rewires the machine's own parameters when regulation fails, is exactly what he added to get adaptation. The contrast that earns membership: a *learning* thermostat that revises its own setpoint schedule from occupancy feedback is inside the category — its organization changes, and the change is driven by evidence bearing on an objective. It is autonomous either way; whether its self-improvement is *reflective* depends on where the learning lands. A legible setpoint schedule the controller consults is a readable artifact — a reflectively improved aspect. In the dominant implementation the learning lands in opaque weights, and the pathway is then non-reflective: [compounding without addressability](../reflection-buys-addressability-not-compounding.md), the household instance of the dominant paradigm of learning. The plain thermostat and the learning thermostat sit on opposite sides of the membership line — and the reflective distinction cuts *across* the learning thermostat, by representational form.

**Self-improving does not require a gate.** Refusing the name to a gradient learner, or to the Homeostat, because nothing in it represents candidates or performs rejection demands the proposal-selection architecture, which is a subtype. The base definition asks for evidence-responsiveness, which direct determination satisfies.

**Non-reflective is not non-member.** A pathway that retains improvement in an opaque substrate is inside the category; the reflective/non-reflective distinction classifies pathways, not membership.

**Self-improving is not autonomous.** The two are independent. A human-inclusive pathway is self-improving; only a boundary with no human in it is autonomously so.

**Self-improving names the direction, not the outcome.** Membership is earned by how the system is built — operative change, responsive to evidence, aimed at an objective. Nothing in that guarantees the objective was the right one, or that the evidence could tell. A system can respond to its evidence faithfully for years and decline.

**A weak oracle is not a broken loop.** Within the proposal-selection subtype, an inadequate evaluator still rejects things, so the loop still closes. What it costs is trust, not membership.

## Misuse Cases

- Calling a system self-improving because it can modify itself, without identifying the evidence channel and the objective the evidence bears on.
- Calling a system self-improving because it "adapts" in the everyday sense — responds, compensates, regulates. First-order control changes the environment, not the system; membership needs a retained change to the system's own organization.
- Refusing the name because the system has no explicit evaluator, candidate representation, or acceptance gate — that demands the proposal-selection subtype's architecture, not the definition.
- Refusing the name because a human performs part of the pathway — that is an autonomy reading, not a category one.
- Refusing the name because what is retained is opaque — that is a reflective/non-reflective reading of one pathway, not a category one.
- Assigning a whole system a single reflective or non-reflective label when its improvement pathways differ — the distinction is pathway-relative.
- Treating the proposal-selection improvement loop as the definition rather than a named subtype, which re-smuggles an architecture into semantics.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Treating evidence-responsiveness — or, in the subtype, an evaluator's acceptance — as evidence that the change improved the system.
- Treating reflection or intercession as the property, rather than as the machinery the reflective pathway runs through.

## Provenance and departures

Two narrowings have been retired from this definition, both on explication grounds.

The first revision built the self-representation requirement into membership — "runs an adaptation loop on itself, *through its own writable, causally connected self-representation*." That failed the similarity criterion (the literature's central cases — parametric self-improvers — fell outside it by construction) and immunized a substantive thesis by making it definitional. The thesis survives as a claim, where it can be argued with: [reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md).

The second revision retired the search–evaluation–retention loop from membership. The earlier definition required an evaluation that could *reject*, which admitted direct evidence-driven adapters — gradient learners, the Homeostat — only by stretching "evaluation" over mechanisms that contain no evaluator, and it read an architecture (the gate) into the semantics of the term (the criterion). Membership now asks for evidence-responsive operative change; the gate architecture is preserved intact as the [proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) subtype, where the search, evaluation, oracle, and rejectability material applies with full force; and the first revision's reserved term lands on one side of the central reflective/non-reflective distinction rather than at a boundary case.

The literature supports the retreat without dictating a replacement. The algorithms field already applies the term to gateless self-tuning: [Ailon et al.'s "self-improving algorithms"](https://arxiv.org/abs/0907.0884) (SICOMP 2011) retune themselves to an unknown input distribution and converge to optimal expected running time with neither a self-model nor an acceptance step. The self-adaptive-systems field treats its feedback-loop reference models as engineering models for building adaptation, not as its definition ([Weyns's organized tour](https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf) presents MAPE-K this way), and [a systematic review of that literature](https://arxiv.org/abs/2505.17798) (Petrovska, Erjiage, and Kugele 2025) finds no settled field-wide definition at all. So no consensus exists from which a universal loop requirement — or any alternative — would follow, and this definition is offered as Commonplace's architecture-neutral explication, chosen so that the reflective/non-reflective distinction, not the update architecture, carries the vocabulary's main weight.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: the named subtype where the improvement criterion is implemented as an evaluator, and the three functions that architecture requires
- [Reflection buys addressability, not compounding](../reflection-buys-addressability-not-compounding.md) — extends: the thesis behind the central distinction — what routing a change through a readable self-representation adds, and what compounds without it
- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that reflective self-improvement routes through
- [Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](../human-inclusive-boundaries-make-reflection-cheap.md) — grounds: why the machinery is nearly free, and why bare classification discriminates little
- [False-positive generation is filtered; false-positive acceptance becomes operative](../false-positive-generation-is-filtered-before-retention.md) — extends: the subtype's asymmetry — why false-positive acceptance is the dangerous evaluation failure
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: the ceiling on autonomous evaluation in the subtype
- [Warranted autonomy is bounded by oracle reach](../warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: the oracle limit on unattended evaluation that remains trustworthy
- [Oracle strength spectrum](../oracle-strength-spectrum.md) — grounds: what an evaluator's acceptance can and cannot establish, which is why acceptance is only an improvement claim
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative change requires
- [Gödel machines are a proof-governed case of reflective self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: a reflective, autonomous proposal-selection loop under the strongest available oracle
- [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — evidence: a reflective, human-inclusive proposal-selection loop, with humans at search and the judgment-heavy evaluation
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — exemplifies: the floor of the category — viability-driven, non-reflective self-improvement with no evaluator anywhere in the mechanism
- [Maes, Concepts and Experiments in Computational Reflection](../../sources/maes-concepts-and-experiments-computational-reflection-1987.ingest.md) — derived-from: the causally connected self-representation criterion the reflective side of the central distinction rests on
