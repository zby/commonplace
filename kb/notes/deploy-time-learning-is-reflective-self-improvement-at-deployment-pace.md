---
description: "Reconciles the deploy-time-learning and self-improving-systems clusters — orthogonal axes (timing×medium vs retention-form) whose intersection is one region, reached by two justifications"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [learning-theory, deploy-time-learning, self-improving-systems]
---

# Deploy-time learning is reflective self-improvement at deployment pace

Two clusters in this KB describe systems that get better by revising durable readable artifacts, and it is easy to read them as rival framings of one idea. [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) champions durable, inspectable [system-definition artifacts](./definitions/system-definition-artifact.md) updated across sessions. The [self-improving-systems](./definitions/self-improving-system.md) vocabulary prizes **addressable** retention — the top of its retention-form grading, [since reflection buys addressability](./reflection-buys-addressability.md) — which is retention a loop can read, criticize, and selectively revise. Both point at the same artifact class. Neither redundant nor one subsuming the other: they **cross-classify the same region on orthogonal axes**, and the region their axes intersect is precisely deploy-time learning.

## The two axes are orthogonal

The clusters organize by different primary questions:

- Deploy-time learning classifies by **timing × medium**: *when* adaptation lands (training, in-context, across-session deployment) and *in what medium* (distributed-parametric, prose, symbolic). Its "missing middle" is the durable-symbolic, deployment-paced cell.
- Self-improvement classifies by **retention form and reflectivity**: *how the change is held* (operative, cumulative, addressable) and *whether the pathway routes through a readable self-representation*. Membership is cheap; the information is in [where the system sits along three independent gradings](./three-independent-gradings-place-a-self-improving-system.md).

A reading on one axis does not fix a reading on the other. [OpenClaw-RL](https://arxiv.org/html/2603.10165v1) runs live RL from user interactions — deployment-paced but non-reflective, because the retention lands in opaque weights. It is a self-improving system that is *not* deploy-time learning, which is the clean witness that timing and reflectivity are independent coordinates rather than one axis restated.

## The intersection is exactly deploy-time learning

Line the coordinates up and the identity is tight. A durable prose-or-symbolic artifact the system reads as its own behavior spec *is* a causally connected self-representation, so revising it in response to deployment evidence is reflective self-improvement by the definition's own test. Doing it across sessions during deployment is the deploy-time timescale. The medium choice is not incidental: choosing prose+symbolic over parametric is exactly what lifts a self-improving system out of the [dominant cumulative-but-opaque grade](./reflection-buys-addressability.md) into the addressable one. So:

> Deploy-time learning ⟺ reflective self-improvement that is durable and deployment-paced.

The biconditional runs both ways. Every deploy-time-learning system is reflective (readable artifacts, read by the system); every reflective self-improver that retains across sessions is doing deploy-time learning. The two clusters are two names for one region.

## What each cluster's axis sees that the other's cannot

Because the axes are orthogonal, each supplies coordinates the other is blind to — which is why keeping both is not redundant.

The self-improvement axis places the region against neighbors deploy-time learning has no vocabulary for: the non-reflective floor where nothing accumulates (Ashby's Homeostat), and the cumulative-but-opaque paradigm of parametric self-improvers. Those neighbors are what "addressable" is being contrasted against; they keep the region honest. It also carries the **coverage**, **closure**, and **warranted-autonomy** gradings, and the stake — [reflection may improve sample efficiency under structured shifts](./reflection-buys-addressability.md) — that says *why the region is worth occupying* as a learning-theoretic bet.

The deploy-time axis adds two things the self-improvement gradings do not carry. First, **timescale**: self-improvement is timescale-agnostic, so it cannot distinguish a parametric learner trained slowly offline from one updated at deployment pace, whereas deploy-time learning's whole argument turns on the across-session, during-deployment slot. Second, the **operators that move an artifact within the addressable region**: constraining, [codification](./definitions/codification.md), and relaxing along [the verifiability gradient](./verifiability-gradient.md). Self-improvement grades *whether* retention is addressable; deploy-time learning describes how a given artifact tightens toward code or loosens back to prose as understanding accumulates.

## Two justifications converging on one bet

The reconciliation's payoff is that the clusters are complementary *arguments* for building the same artifact class, not competing claims about it. Deploy-time learning argues from engineering: durable readable artifacts are inspectable, tool-compatible, reversible, and buildable now — the agile lineage where prose and code co-evolve, and [the readable pair is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). Self-improvement argues from learning theory: addressability enables second-order revision and may cut target data under structured shifts. Holding both lets you predict *when* the bet pays (structured shift, need for per-change revision, deployment-pace feedback) and *how* to construct it (constraining and distillation along the verifiability gradient), where either framing alone gives only half the picture.

## Scope

- The identity requires the durability qualifier. In-context reflective adaptation — an agent revising a scratchpad it re-reads within one session — sits in the same medium but evaporates at session end, so it is reflective self-improvement without being deploy-time learning. Timing, not reflectivity, excludes it.
- "Reflective at deployment pace" excludes deployment-paced parametric updates (OpenClaw-RL) by the reflectivity condition, matching deploy-time learning's own exclusion of the parametric cell. The two exclusions coincide, which is what makes the biconditional clean rather than approximate.

## Open Questions

- Whether a deployment-paced parametric loop made addressable by interpretability tooling inside its boundary would migrate into the region — the same open question [reflection buys addressability](./reflection-buys-addressability.md) raises, here reached from the timing axis.

---

Relevant Notes:

- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — grounds: the timing×medium axis and the durable-symbolic cell this note identifies with the addressable region
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the category and the reflective/non-reflective distinction the intersection is stated against
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: the retention-form grading whose addressable top is the region's other coordinate
- [Three independent gradings place a self-improving system](./three-independent-gradings-place-a-self-improving-system.md) — extends: the placement scheme this note adds a timing coordinate to
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: how the parametric and readable loops relate once both are seen as self-improvement pathways
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — see-also: the engineering-side argument for building in this region
- [The verifiability gradient](./verifiability-gradient.md) — mechanism: the ladder the region's addressable artifacts move along, which self-improvement's gradings do not track
