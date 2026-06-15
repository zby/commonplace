# Condensation-faithfulness experiment

Exploring **how we could run an experiment** to test whether Commonplace's condensation methodology produces memory that is more *behaviorally faithful* than naive auto-summarization — using the perturbation protocol from [Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md).

This workshop designs the experiment. It does not run it, and does not (yet) build any review gate.

## Goal

The paper found that auto-distilled "condensed experience" is behaviorally inert: perturbing it (Corrupt / Irrelevant / Filler / Empty) barely changes downstream agent behavior, while perturbing raw trajectories degrades it sharply. Our methodology *claims* to produce condensate that avoids this — constrained, actionable, activated. We have never tested that claim against a behavioral-faithfulness metric.

Produce a **runnable experiment design**: treatment, control, protocol, metric, and the smallest setup that would give a real signal — enough that someone could execute it (or decide it isn't worth executing) without re-deriving the framing.

## What would close it

One of:

- A promotable experiment design → a proposal in `kb/reference/proposals/` (see its README for the contract).
- A reasoned decision that the experiment is not worth running, with the disqualifying constraint recorded as a note or log entry.

Either way: extract the durable conclusion, delete this directory, remove the README entry.

## Scope / evaluation boundary

In scope:
- How to operationalize "behavioral faithfulness" for a Commonplace condensate.
- What the treatment (methodology-produced condensate) and control (naive summary) actually are, and what makes the comparison fair.
- The minimum viable harness — does this need a full self-evolving-agent loop, or can a thinner setup isolate the effect?

Out of scope (decided by user, 2026-06-15):
- **A behavioral-faithfulness review gate.** We currently do no distillation from logs, so there is nothing for such a gate to guard. Revisit only if a log→artifact condensation loop is built.
- Running the experiment itself.
- Reproducing the paper's exact frameworks/backbones unless the design genuinely needs them.

## Context so far (leads, not commitments)

Established in the conversation that opened this workshop. Treat as starting material the live work may revise.

The paper's three causes of unfaithfulness map onto our two-axis model (distillation × constraining) plus activation — and the *enforcement arm* (the `kb/instructions/` gate suite) already targets cause #1:

- **Cause #1 — semantic vagueness of condensate.** Our review-gates are an anti-vagueness filter: `explanatory-reach`, `claim-strength`, `explication-quality`, `framework-decoration`, `could-be-a-paragraph`, `pseudo-formalism`, plus the overclaim guards (`grounding-alignment`, `load-bearing-qualifiers`, `source-residue`). The prescriptive register's quality goal ("executability + precision") is an operational definition of the paper's own unmet phrase, "cognitively actionable."
- **Cause #2 — internal bias / static-prepend underweighting.** Our answer is activation: on-situation typed cues, [frontloading](../../notes/frontloading-spares-execution-context.md), and moving lessons toward enforcement (a validator isn't underweighted by later layers). "Instruction-duality" = activation by construction.
- **Cause #3 — pretrained priors suffice.** Our answer is routing/budget: [evaluate by effects](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), don't inject memory where priors already win.

Candidate experiment shape (open):
- **Treatment** = condensate that passed the Commonplace pipeline (write conventions + gate suite). **Control** = a naive auto-summary of the same source. The gate suite is the independent variable.
- **Protocol** = the paper's interventions (Empty / Corrupt / Irrelevant / Filler), measure behavioral delta. Higher faithfulness = bigger degradation under perturbation.
- **Open tension:** our gates check *prose properties*, the paper measures *causal uptake in an agent loop*. A gate-passed note could read well and still fail the perturbation test. That gap is the whole reason to run it rather than assert it.

Honest caveats to preserve (from the ingest report's "Limitations"):
- Perturbation-insensitivity conflates "agent ignores it" with "it carried no signal" — the control must be a *fair* naive summary, not a strawman.
- "Condensed experience" (auto-distilled, descriptive) ≠ instructions (authored, prescriptive, authoritative). Be explicit about which our treatment is.
- The test measures whether memory is *used*, not whether it is *correct*.

## Related

- [Faithful Self-Evolvers — snapshot](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md) and [ingest report](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — the source and our scoped reading.
- [distillation](../../notes/definitions/distillation.md), [constraining](../../notes/definitions/constraining.md) — the two-axis model.
- [evaluate memory by effects](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), [activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md), [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — the faithfulness/activation cluster.
- Sibling llm-wiki (inquiringlines.com) ingested this paper's thesis unscoped — a live example of recall without a scoping gate; relevant if the design wants a contrast baseline for "condensate quality."

## Bookkeeping

Plain markdown, no frontmatter required. Add working files as the design develops (e.g. `protocol.md`, `harness-options.md`). Keep this README the entry point: what the work is and what would close it.
