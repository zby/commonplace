---
description: "Frozen-model game agents improve through inherited artifacts; held-out learning curves separate acquisition cost, artifact reuse, and task benefit."
source: https://arxiv.org/abs/2610.08902
captured: "2026-10-18"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 2810c7794bf46a449e09d4e11a9911e9ffca1aa193c6ea0086dae1221a608f65
ingested: "2026-10-18"
type: types/ingest-report.md
learning_claims: true
domains: [agent-learning, persistent-artifacts, behavioral-evaluation]
---

# Ingest: Agent Plasticity: Measuring Self-Improvement Through Experience

## Classification

An empirical preprint proposing an evaluation protocol and acquisition-efficiency measure, with experiments in Chess, Go, Hex, and NetHack, diagnostic annotations, and qualitative repair examples.
Author: Harman Singh and ten coauthors, affiliated with UC Berkeley, Meta Superintelligence Labs, the University of Washington, and Princeton University. These affiliations are an author signal, not independent verification of the results.

## Summary

The paper measures whether fixed-weight agents become better through experience when fresh acting contexts inherit only self-constructed tools, skills, strategies, and memory. Under its board-game protocol, the same model acts and reflects on training feedback; structurally and executably valid inventory revisions persist, while held-out trajectories and scores remain unavailable to reflection. Some lineages improve substantially on held-out games, others stagnate or regress, and transfer to stronger opponents is uneven. The proposed agent plasticity measure divides held-out score gain by learning cost, including rejected reflection attempts; endpoint capability and acquisition efficiency produce different rankings within this protocol. Observational diagnostics distinguish missing covering artifacts, available but unused artifacts, and failures despite use: high reuse is not sufficient for high task performance. NetHack extends the setting to native coding-agent harnesses but changes games across checkpoints, so its trajectories also reflect game difficulty. The results evaluate adaptation within these fixed interfaces and feedback regimes, not the superiority of this decomposition over alternatives.

## Contribution assessment (our opinion)

The measurement problem matters: endpoint scores hide both regressions and the expense of acquiring capability. The useful contribution appears to be the combination of fresh-context artifact inheritance, held-out trajectories, cost accounting, and separate reuse diagnostics, rather than a demonstrated new improvement algorithm. The controlled board-game results make persistent improvement testable and expose candidate bottlenecks; they do not establish that experience itself adds value beyond budget-matched artifact development without feedback. That missing comparison narrows the causal explanation more than it undermines the evaluation framework. The framework could enable stronger interventions, but its significance beyond these tasks remains prospective, and the captured comparisons do not establish literature-wide priority.

## Quotes

No source quotes have been retained yet.

## Connections Found

This source is a bounded empirical case for [Evaluate Memory By Effects, Not By Existence](../theory/agent-memory-requirements/evaluate-memory-by-effects.md): within fixed-weight, fresh-context game lineages, the paper measures future task scores and acquisition costs separately from artifact availability and invocation. Strong reuse alongside different game scores supports keeping those measurement levels separate, not treating invocation as causal benefit. Relative to the note's existing routing-versus-outcome distinction, the paper adds full checkpoint trajectories, acquisition-cost accounting, and failure-coverage diagnostics. Its results do not test Commonplace's own memory architecture or compare alternative artifact representations.

## Learning Claims (our opinion)

On the source's terms, learning occurs through inventory revisions, not weight updates or continued conversational history. Training trajectories, outcomes, traces, and game-specific feedback reach reflection; the model may compose Python tools and revise textual rules and strategies. Chess supplies expert move-quality feedback, whereas Go and Hex supply lighter learning-time diagnostics. Stronger offline annotations used for failure analysis are not learner feedback.

Against Commonplace's [theory-builder conditions](../theory/definitions/theory-builder.md), the evidence differs by condition:

- **Localized content:** tools, rules, and named failure-mode records are inspectable units. The source's stable artifact IDs and editable guard clauses offer relatively fine [addressability](../theory/definitions/addressable-theory.md), though fine localization does not establish correct blame.
- **Consumption:** execution traces show invocation, which is weaker than content-directed influence. The paper's exact-position chess guard removal changes the chosen move in a replay, providing stronger local evidence of consumption. This does not establish causal uptake for every annotated reuse event. These are author-reported replays; no code was inspected or executed for this ingest.
- **Content-directed criticism:** the reported repair examples connect identified failures to particular commitments, such as draw valuation near the move cap and risky prayer bypasses. This supports the condition in those examples. Structural acceptance and generic reflection opportunities alone do not show that every lineage criticizes what its artifacts say.
- **Iteration:** accepted repairs enter later inventories and some are visibly used in later games. This supports iteration across checkpoints and fresh episodes within a lineage; the paper does not establish transfer of those artifacts across independently trained lineages or different problems.

The concrete repair sequences therefore support theory-builder behavior in parts of the evaluated systems, not a uniform classification inferred from their architecture. Learning remains a separate outcome: positive held-out board-game trajectories support improved future capacity in some model–task combinations, while flat and negative trajectories show that revision need not help. The exact-position guard also shows that a narrow remembered correction can affect later action without establishing broad generalization.

The effective update space is broad enough to construct search engines and replace local strategies. It still fixes model weights, the acting/reflection interface, game APIs, feedback availability, budgets, and the inventory-admission protocol. Following [the fixed-decomposition boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement inside that space does not establish that these external choices are preferable or that they exclude no useful corrections. The paper adds measurement detail to Commonplace's account; it does not require equating artifact reuse with learning, nor does it demonstrate that earlier gains improve the productivity of later improvement.

## Extractable Value

1. **Evaluate a retained-artifact lineage, not just its final inventory.** Fresh contexts, feedback-isolated held-out board games, and checkpoint curves expose persistence, regressions, and acquisition expense under the tested interface. This extends the existing effects requirement with a reusable evaluation design; it is not evidence that the particular interface is optimal. [experiment]
2. **Separate diagnostic denominators.** Decision-level reuse includes successful decisions; failure-composition shares condition on identified failures. Distinguishing absent coverage, non-use, and failure despite use helps choose an intervention without mistaking a changing failure mix for progress. The paper's annotations nominate causes rather than establish them. [quick-win]
3. **Keep acquisition efficiency distinct from capability.** Held-out gain per learning dollar can distinguish lineages with different starting scores and learning trajectories. Retain full curves beside the scalar: prices, score headroom, horizon, and saturation fitting affect it. The measure is protocol-relative, not evidence of target-sample efficiency or total lifecycle economy. [just-a-reference]

## Limitations (our opinion)

The central causal gap is the lack of a budget-matched reflection-without-feedback comparison: extra computation for building artifacts could account for part of the improvement attributed to experience. Using the same model for acting and reflection also couples artifact production with artifact use. Whole-lineage gains do not identify individual artifacts' effects; the local guard-removal replay varies one guard and establishes a move change, not the guard's aggregate contribution to winning.

Reuse attribution combines Gemini 3.1 Pro semantic judgments with execution evidence. That improves inspectability but does not turn correlation into intervention evidence or distinguish defective content from defective application. Broad relevance is also not coverage of a particular failure. High artifact-conditioned success can coexist with rare reuse or poor game outcomes.

Board-game OOD evaluation means stronger opponents, not new tasks. Separately trained game lineages do not establish cross-task transfer. NetHack has one lineage per model, changing seeds across checkpoints, different native agent harnesses, and reported harness-version differences; its model comparisons and longitudinal gains are consequently less controlled. Finite checkpoint evaluations introduce noise. The monotone saturation fit suppresses regressions, uses a minimum-rise criterion and sometimes extrapolates; price-normalized estimates are not measurements of physical compute. Structural admission does not test behavioral effectiveness, and no alternative decomposition of feedback, artifact storage, or acting/reflection boundaries is compared. These conditions bound transfer to agent-operated KB work.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../theory/agent-memory-requirements/evaluate-memory-by-effects.md) with a bounded evaluation example that separates checkpoint task outcomes, acquisition cost, decision-level reuse, and failure-conditioned coverage diagnostics.
