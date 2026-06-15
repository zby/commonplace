# Experiment protocol (sketch)

Working draft. Records the code-availability finding and a first protocol. Open decisions are marked **OPEN**.

## Code availability (checked 2026-06-15)

- **The paper's own code is not released.** No repo linked from [arXiv abs](https://arxiv.org/abs/2601.22436) (comment field is just "ICML 2026"), and the first author's GitHub ([circle-hit](https://github.com/circle-hit)) has no matching repo. So we **reimplement the interventions ourselves** — they are trivial string ops on a memory slot — and build the harness on the published frameworks the paper benchmarked.
- Reusable framework repos:
  - **ReasoningBank** — [google-research/reasoning-bank](https://github.com/google-research/reasoning-bank) (confirmed). Condensed-only memory.
  - **Dynamic Cheatsheet** — public (`suzgunmirac/dynamic-cheatsheet`, **verify URL**).
  - **ExpeL** — public (original ExpeL repo, **verify URL**).
  - **G-Memory** — public (multi-agent, **verify URL**).

## Core design decision

We are **not** reproducing the paper. The paper asked "do existing frameworks use condensed memory faithfully?" Our question is narrower: **does swapping the condenser for Commonplace's condensation pipeline raise faithfulness, holding everything else fixed?**

So the design is a **condenser swap inside one fixed framework**:

- Hold constant: framework, benchmark, backbone, retrieval, prompt scaffold, perturbation set.
- Vary only: **how the condensed-memory artifact is produced** — the independent variable.

This isolates the methodology from the framework, which is the whole point.

## Why ReasoningBank as the base

- **Condensed-only.** It carries no raw trajectories, so there is no raw-experience channel to confound the measurement — this is exactly the paper's clean §4.2 setting where condensed memory is the *only* guidance. Faithfulness of condensed memory is measured without subtracting a raw-experience effect.
- **Public code** (the only confirmed repo of the four).
- **Has a real condenser** — it distills reasoning strategies from self-judged success/failure traces. That distillation step is precisely what we replace.

**OPEN:** confirm ReasoningBank's condenser output has a clean, swappable seam (a function that turns a trace into the stored memory string). If it's deeply entangled with retrieval, a thin reimplementation of just the condense→store→inject loop may be cheaper than forking.

## Treatment vs control

Same trace input, two condensers:

- **Control (naive baseline)** = ReasoningBank's native condenser — the brevity-oriented auto-summary the paper found inert.
- **Treatment (Commonplace pipeline)** = the trace condensed under our authoring conventions + passed through the relevant review gates (`explanatory-reach`, `claim-strength`, `explication-quality`, `grounding-alignment`, `load-bearing-qualifiers`, etc.), producing a constrained, claim-shaped, actionable artifact in the same slot.

**OPEN — the hard part.** The Commonplace pipeline is currently human/agent-in-the-loop with gates that emit warnings, not an automatic condenser. Options:
1. **Offline hand-built treatment** — author the treatment condensates by hand (or via a gated sub-agent) for a fixed task set. Cheapest path to a *signal*; not yet an automatic loop. Good enough to answer "does gated condensate help at all?"
2. **Gate-in-the-loop condenser** — wrap the native condenser with a gate pass + revise step. Closer to a real system; more build cost.
   Start with (1). Only build (2) if (1) shows a positive effect worth productizing.

## Interventions (reimplement)

Apply to the condensed-memory slot, per the paper:

- **Empty** — keep formatting cue, drop content.
- **Corrupt** — alter key components (distort action references), break coherence.
- **Irrelevant** — replace with an unrelated, generic condensate.
- **Filler** — replace content with semantically empty tokens (`%$#&`).
- Plus **w/o Condensed** (full ablation) and **unperturbed** baseline.

## Metric

**Faithfulness = behavioral sensitivity to perturbation.** Run each condition; measure task performance (the benchmark's native metric, e.g. success rate / exact match).

- **Faithfulness score** = drop from unperturbed → perturbed (Corrupt/Irrelevant/Filler). Large drop = the agent actually depended on the content. ≈0 drop = inert (the paper's finding for naive condensate).
- **Hypothesis:** treatment shows a *larger* faithfulness drop than control — i.e., our condensate is causally load-bearing where the naive one is decorative.
- Also report **utility** (unperturbed-with vs `w/o Condensed`): is the condensate even helping before we ask whether it's faithful? Utility and faithfulness are separate axes (the paper's central distinction).

## Fairness controls (from the caveats — do not skip)

- **Fair control, not a strawman.** The naive baseline must be ReasoningBank's *actual* condenser, not a deliberately bad summary. Otherwise we prove nothing.
- **Insensitivity ≠ ignored.** A flat perturbation curve can mean "agent ignored it" *or* "it carried no signal." Pair every faithfulness number with the utility number to disambiguate.
- **Label the artifact honestly.** Our treatment is closer to an authored *instruction* than to auto-distilled *experience*; state that, since the paper's thesis is specifically about auto-condensed experience.
- **Used ≠ correct.** This measures causal uptake, not whether the memory's advice is right.

## Tiers (cost control)

1. **Minimal viable signal** — ReasoningBank, one benchmark, one backbone, hand-built treatment condensates (option 1), ~N tasks. Answers: does gated condensate move the faithfulness curve at all? **OPEN:** pick benchmark + backbone + N. Prefer the cheapest env that still shows a raw-vs-condensed gap in the paper (WebArena sub-tasks are the paper's setting but heavy; a cheaper substitute may suffice for a first signal).
2. **Full** — multiple backbones, second framework (e.g. ExpeL for the joint raw+condensed setting), gate-in-the-loop condenser. Only if tier 1 is positive.

## Open decisions (consolidated)

- ReasoningBank condenser seam: forkable vs reimplement?
- Treatment production: hand-built (start) vs gate-in-the-loop?
- Benchmark + backbone + task count for tier 1?
- Cheapest environment that preserves the effect?
- Compute/API budget and where it runs?
