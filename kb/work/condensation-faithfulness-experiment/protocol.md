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
- **Has a real condenser** — it distills reasoning strategies from self-judged success/failure traces.

**Seam: verified clean (2026-06-15).** The condenser is a single swappable step in `WebArena/induce_memory.py:main()` — `trajectory → one_step_chat(system_msg=SUCCESSFUL_SI|FAILED_SI) → markdown memory_items`. Retrieval (`memory_management.py`, embedding top-k) is separate and orthogonal. No deep fork needed; we replace one system prompt + post-step. Notably the native prompt *already* exhorts "say why / be concrete / when-NOT-to-use" and the paper still finds it inert — so the treatment must add structure + enforcement, not wording. See [condenser-design.md](./condenser-design.md).

## Treatment vs control

We do not yet have any trace condensation — the treatment is a **new condenser built from KB theory**, not a tuned prompt. Full design and output schema in [condenser-design.md](./condenser-design.md).

- **Control (naive baseline)** = ReasoningBank's native condenser (SUCCESSFUL_SI/FAILED_SI, unchanged) — the fair baseline the paper found inert.
- **Treatment (theory-grounded condenser)** = draft → gate-check → revise, emitting a claim/Trigger/Mechanism/Scope/Form schema (constraining + activation + grounding, enforced rather than exhorted).

**OPEN — automation depth.** Two ways to produce the treatment, tracked as build cost not method:
1. **Offline / gated-sub-agent** authored condensates for a fixed task set — cheapest path to a *signal*.
2. **In-loop condenser** that runs draft→gate-check→revise automatically each task — closer to a real system.
   Start with (1); build (2) only if (1) shows an effect. (How much gate suite runs in-loop is Fork B in the design doc.)

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
