---
description: "Ten boundary cases run against the self-improving-system definition — each classifies by the stated criteria alone; the stress they apply falls on boundary declaration, not on the membership clauses"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, self-improving-systems]
---

# The self-improving-system definition classifies its boundary cases without ad hoc exceptions

An explication earns its keep by classifying the cases that motivated it *and* the cases built to break it. This note runs ten boundary cases against the [self-improving system](./definitions/self-improving-system.md) definition — operative change to the system's own [behavior-determining organization](./definitions/behavior-determining-organization.md), causally responsive to [evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — asking six questions of each: is there [operative](./definitions/operative-change.md) self-change; what is the objective; what evidence affects the change; is the pathway reflective; is it direct-update or proposal-selection; and is it improvement-directed or demonstrably improving.

## The cases

| Case | Operative self-change? | Objective | Evidence | Reflective? | Mechanism | Directed or effective? |
|---|---|---|---|---|---|---|
| Gradient-based learning (model fine-tuned on its own deployment data) | Yes — weights persist and govern inference | Loss function | Gradients of the loss | No | Direct update | Directed; effectiveness rests on a stated outcome measure, e.g. held-out generalization |
| Adaptive control (self-tuning regulator, model-reference adaptive control) | Yes — controller gains persist and govern subsequent control | Tracking / reference-model error | Error signal | No | Direct update | Directed; effectiveness depends on achieved control performance under the relevant operating conditions |
| Evolutionary adaptation (a lineage under variation and selection; evolutionary strategies over parameters) | Yes — genomes / parameter vectors persist across generations | Viability and reproductive success (implicit); fitness function (explicit in ES) | Differential survival; measured fitness | No | Proposal-selection | Directed; selection pressure is part of the mechanism, not evidence that improvement occurred |
| Code-generating, test-running agent patching **its own** harness, skills, or tools | Yes — the patched code is the system's own substrate | Test suite plus review criteria | Test results, trace evidence | Yes | Proposal-selection | Directed; passing the oracle establishes what it warrants, not net improvement beyond its coverage |
| The same agent writing code for an **external** product | No — the diff is a work product | (Product quality — not a self-objective) | Test results | — | — | Out of category: nothing lands in the system's own organization |
| System that only improves the current answer (self-refine, best-of-n) | No — the answer is a work product; nothing survives the episode as organization | Answer quality | Critique, scores | — | — | Out of category, despite running a full generate–evaluate–select loop |
| System that updates persistent memory (lessons, notes loaded by later runs) | Yes — memory is retained organization, if later runs load it | The distillation criterion (what is worth keeping) | Traces, failures, outcomes | Yes — the memory is read as guidance | Direct (unconditional append) or proposal-selection (curated), both occur | Directed; effective only if retrieval and consumption actually happen |
| Ordinary software maintained by humans | Yes — the codebase is the organization, humans inside the declared boundary | Maintainer standards, tests, review criteria | Bug reports, tests, judgment | Yes | Proposal-selection | Directed; human-inclusive and fully un-autonomous |
| Accidental self-modification (bit flip, config corruption that happens to help) | Change, yes — but responsive to no evidence | None | None | — | — | Out of category, even when the outcome is an improvement |
| Change responsive to a bad or misaligned objective | Yes | The wrong criterion, faithfully applied | Whatever that criterion emits | Either | Either | Fully directed, demonstrably not improving — the separation absorbs it |

## What the cases stress

**The membership clauses hold without exceptions.** Every exclusion above falls out of a stated clause — work products and episode state fail the organization test; accident fails evidence-responsiveness — and every inclusion needs no stretching: the gateless cases (gradient, adaptive control) enter through direct determination, exactly what the second revision of the definition was for.

**The stress falls on boundary declaration.** Two cases classify differently depending on where the boundary is drawn. A model fine-tuned by an external training pipeline is being improved, not self-improving; declare the pipeline inside the boundary and the composite self-improves. Evolutionary adaptation is self-improvement of a *lineage or population*, not of any individual organism. Neither needs a new clause — but both show that membership, like the autonomy grading, is read against a declared boundary, and the definition should say so once rather than leave it implicit.

**Directed and effective come apart in every row.** No entry in the last column follows from membership: evidence-responsiveness makes a case improvement-directed, and effectiveness is a separate reading under a stated measure and conditions — established, not established, local only, or failed. The bad-objective row is the limiting demonstration, but the softer inclusions carry the same structure.

**Architecture without self-directedness is the instructive exclusion.** The answer-refinement case runs a complete generate–evaluate–select loop — candidates, an evaluator, selective retention — and is still not a self-improving system, because everything it improves is a work product. The subtype machinery detects the *mechanism*; only the organization clause decides *membership*. This is the cleanest demonstration that the two questions are independent.

**Memory systems fill the rare cell.** The unconditional-append memory agent is reflective *and* direct-update — evidence writes straight into the most readable substrate there is — occupying the corner of the [two-dimensions crossing](./definitions/self-improving-system.md) that neither the parametric nor the gated tradition covers. Its known failure mode is not the write but the read: memory that nothing loads is not operative, [and retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md).

## Open Questions

- Whether the lineage-boundary reading of evolutionary adaptation is worth developing, or whether population-level improvement should stay a marked analogy at the category's edge.
- Whether "improves the current answer" and "updates persistent memory" have a principled midpoint — episode-scoped organization (a revised plan governing the rest of a long deployment) that the declared-horizon reading of [operative change](./definitions/operative-change.md) admits.

---

Relevant Notes:

- [Self-improving system](./definitions/self-improving-system.md) — grounds: the definition under test, whose clauses each exclusion and inclusion traces to
- [Behavior-determining organization](./definitions/behavior-determining-organization.md) — grounds: the clause doing most of the excluding — work products and episode state fall here
- [Operative change](./definitions/operative-change.md) — grounds: the horizon-relative persistence-plus-authority clause
- [Evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — grounds: the clause that excludes accident and admits gateless adaptation
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — contrasts: the mechanism the answer-refinement case has and membership ignores
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — extends: why the memory-updating case's weak point is consumption, not capture
