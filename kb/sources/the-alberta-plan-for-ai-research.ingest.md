---
description: "A continual-learning agent architecture and research roadmap that separates per-step adaptation, model-based planning, and progressively learned abstractions."
source: https://arxiv.org/abs/2208.11173
captured: "2026-08-26"
capture: pdftotext
genre: design-proposal
snapshot_sha256: c4953ac382343dc7e9f2e880a868c4d46817c2f4645504964a8da61360d1001f
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [continual-learning, reinforcement-learning, agent-architecture, planning]
---

# Ingest: The Alberta Plan for AI Research

## Classification

This is an architecture and research-roadmap proposal rather than an empirical study. It fixes a vision of continually learning, reward-maximizing agents and proposes a provisional twelve-step program for building them.
Author: Richard S. Sutton, Michael Bowling, and Patrick M. Pilarski present the agenda as researchers affiliated with the University of Alberta, Alberta Machine Intelligence Institute, and DeepMind Alberta; the source is a first-party account of their research program.

## Summary

The Alberta Plan frames intelligence as online reward maximization through continual sensing, acting, learning, and model-based planning under finite computation. Its base agent combines learned perception, reactive policies, value functions, and a transition model whose predictions affect behavior through planning, while a foreground/background split protects time-critical interaction. A twelve-step roadmap moves from adaptation with fixed linear features through feature discovery, prediction, control, average-reward planning, temporal abstraction, and Oak's utility-based replacement of features, subtasks, options, and option models. Read it for a precise research decomposition and set of design commitments, not for evidence that the resulting architecture works.

## Quotes

No source quotes have been retained yet.

## Connections Found

The Plan is a technical architecture anchor for [An action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md): its learned transition model becomes behaviorally consequential only when continual planning uses predicted successor states and rewards to update values and policies. It also gives [Human analogies can motivate functions without determining component boundaries](../notes/human-analogies-suggest-functions-not-component-boundaries.md) a concrete supporting case, because finite compute, fixed-duration time steps, and latency obligations motivate the foreground/background split before the paper compares that split with Kahneman.

Oak is a design-space counterpoint to [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): it progressively moves features, subtasks, options, and option models into a utility-assessed replacement loop while leaving the reward objective, signal interface, and temporal discipline outside that effective update space. Compared with [Ashby's violation-triggered reorganization](ashby-design-for-a-brain-1960.ingest.md) and [GBrain's scheduled dream cycle](../agentic-systems/gbrain.md), the Plan's per-step discipline helps separate the choice to adapt continually from the choice of when adaptation runs.

## Extractable Value

1. **Instrumental and epistemic abstractions require different promotion gates.** Oak retains features, subtasks, options, and models for utility in prediction and planning; Commonplace separately asks whether explicit claims are valid, have explanatory-reach, and are worth maintaining. Neither gate subsumes the other. [deep-dive]
2. **Continual adaptation and temporal uniformity are separate design axes.** The contrast among per-step learning, violation-triggered reorganization, and scheduled consolidation exposes different latency, coordination, and credit-assignment costs that the current KB does not yet isolate in one claim. [quick-win]
3. **A learned model needs an explicit consumption path.** The Plan supplies a worked planner-to-value-to-policy path that sharpens the existing action-model note without requiring a stronger claim about the model's explanatory reach. [quick-win]
4. **Effective update spaces can widen in stages.** The roadmap moves from tuning weights over fixed features to generating and replacing features, subtasks, options, and option models, while showing that a more adaptive component stack can still inherit fixed choices about reward, signals, and cadence. [deep-dive]
5. **Resource constraints can justify architectural boundaries directly.** The foreground/background split follows from reaction-time and per-step compute obligations, making the later fast/slow human analogy illustrative rather than load-bearing. [quick-win]
6. **The source supports only the production-method axis of the Bitter Lesson.** Its preference for scalable learning and search over human-supplied domain insight bears on production method, but does not establish conclusions about representational form. [just-a-reference]

## Limitations (our opinion)

The proposal does not test whether temporal uniformity, average-reward optimization, the base-agent decomposition, or Oak's replacement loop produces capable or scalable agents. Its later prototype steps are progressively less specified, and the roadmap provides neither comparative baselines nor completed-system outcomes. Improvement inside the proposed learning machinery therefore would not validate the choices fixed outside it, including the observation-action-reward interface, scalar objective, component boundaries, and per-step temporal discipline.

The deepest theoretical difference from Commonplace is the criterion by which an abstraction earns retention. The Plan ranks features, subtasks, options, and option models by their contribution to learning and planning under reward. Commonplace instead separates [validity from learning value](../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) and asks theoretical claims to earn [explanatory-reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md). These tests are not substitutes: instrumental usefulness does not establish why an abstraction works or where it stops, while an epistemically warranted theory changes behavior only when a [consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md) uses it.

The paper also leaves reward misspecification, safety, governance, and coordination between foreground learning and asynchronous background planning largely outside the plan. Its architecture concerns numerical reinforcement-learning agents, so its timing and update-space distinctions can inform agent-operated KB design, but its particular signals, objectives, and learned representations should not be transferred to language-model agents without independent argument.

## Recommended Next Action

Write a structured-claim note titled “Continual adaptation and temporal uniformity are separate design axes” that compares per-step, violation-triggered, and scheduled update cadences by their latency, coordination, and credit-assignment costs.
