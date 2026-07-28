---
description: "Proposal: promote bidirectional codification from design guidance to a comparative conjecture, tested by evolving the same task stream under natural-language-only, symbolic-only, one-way promotion, and bidirectional codify-and-relax regimes"
type: ../types/design-proposal.md
tags: [constraining]
---

# Bidirectional codification as a comparative test

[Codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) currently reads as design guidance: codify what stabilizes, relax what proves brittle. The guidance embeds a comparative claim nobody has tested — that the *bidirectionality* is load-bearing, not just prudent. The conjecture, stated so it can lose:

> For task families containing both underspecified judgment and recurring exact regularities, a system that can move behavior from natural-language into symbolic form as it stabilizes — and relax it back when the codification proves brittle — achieves a better reliability–generality–cost frontier than a system with a fixed boundary between learned and codified behavior, and than a system that promotes one way only.

This explains why the two readable forms are needed *together*: natural language as the provisional hypothesis surface, symbolic form as the compiled and checked surface, relaxation as the operation that keeps obsolete proxy theories from accumulating as permanent machinery. It is the mechanism-level companion to [ablation baselines for the declared objective](./ablation-baselines-for-the-declared-objective.md): that proposal compares having the framework against not having it; this one compares boundary-management regimes inside the artifact layer.

## Current state (as of 2026-07-28)

- The codification/relaxing note supplies the operators and [operational relaxing signals](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) the detection side; [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) asserts the reversibility claim in passing ("a system that can only tighten ratchets itself into brittleness") without comparative evidence.
- The [scheduler note](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) now names codification as the write path into a learnable symbolic layer, and [oracle accumulation](../../notes/oracle-accumulation-improves-the-selection-environment.md) gives retained checks their compounding role — both presuppose the promotion direction works; neither tests relaxation.
- No system in the KB's coverage demonstrates automated relaxation; one-way promotion is the observed norm in surveyed loops.
- Originates from the mixed-form-learning workshop's disposition of an external-review conjecture (2026-07-28).

## Problem

Design a comparison that could show a fixed or one-way boundary outperforming the bidirectional regime. Four arms evolve the same system against the same task stream:

1. **Natural-language only** — all learned behavior stays in prose artifacts; nothing is codified.
2. **Symbolic only** — every retained lesson must be expressed as code, schema, or test at capture time.
3. **One-way promotion** — natural-language first, codified when stable, never relaxed.
4. **Bidirectional** — codified when stable, relaxed back on brittleness signals.

The task stream is the load-bearing design element: it must contain regularities that genuinely stabilize (giving codification something to earn) *and* later shifts that invalidate some of them (giving relaxation something to do). A stream without invalidating shifts cannot distinguish arms 3 and 4 and would spuriously favor one-way promotion.

## Design space

- **Stream substrate.** A synthetic task family with scripted distribution shifts (controllable, low external validity); a replayed slice of a real repository's history where conventions demonstrably changed (real, confounded); or a harness-search benchmark where the arms are operator sets available to an automated improver (closest to the loops the conjecture is about).
- **Who runs the operators.** Hand-operated arms measure the regimes; automated arms measure regimes plus the operators' current automatability. These answer different questions and should not be mixed in one run.
- **Outcome surface.** Reliability (error rates on stabilized regularities), generality (performance across the shift), and cost (authoring, maintenance, and context spend per arm) — the conjecture claims a frontier, so single-metric wins are not confirmation.

Free choices, marked as such: shift count and spacing in the stream; the brittleness-signal set that triggers relaxation in arm 4 (the relaxing-signals note is the candidate inventory, but which signals fire automatically is a protocol choice).

## Forces

- **Relaxation events are rare by construction** — the bidirectional advantage appears only after invalidating shifts, so short streams systematically favor arms 2 and 3; stream length must be justified by expected shift count before any run is priced.
- **Oracle-quality confound.** Codification quality depends on what the objective's oracle can check; an arm's failure may indict the oracle, not the regime. The protocol must hold the oracle surface constant across arms.
- **Asymmetric operator maturity.** Promotion has worked instances; automated relaxation has none, so arm 4 run automatically measures today's relaxation tooling as much as the regime. The hand-operated variant isolates the regime claim.
- **Cost accounting is the honest metric.** A fixed boundary is cheap to operate; bidirectionality buys adaptability with machinery. If the frontier claim only holds when maintenance cost is ignored, the guidance should be weakened, not defended.

## Operativity and warrant

Adoption produces a protocol document and, once run, a results report consumed as evidence in `kb/reference/` — no behavior-determining organization changes until the codification/relaxing note is revised against the results. Arms 3 and 4 require a promotion operator, and arm 4 a relaxation operator wired to brittleness signals: "no consumer yet; the operators must be built or hand-executed" is the current operativity answer. Any automated brittleness detector's oracle warrant must be stated per signal and is part of the reviewable protocol surface.

## Adoption criteria

- A named decision the result would change: whether relaxing signals graduate from advisory note content to enforced monitors, and whether the codification guidance keeps its bidirectional form.
- A priced first run — arms bought, stream length with its shift-count justification, operator mode (hand or automated) — small enough to happen.
- The oracle surface held constant across arms, stated in the protocol.
- Pre-commitment to report the fixed-boundary or one-way arm winning, which would demote the KB's own guidance from mechanism to preference.
