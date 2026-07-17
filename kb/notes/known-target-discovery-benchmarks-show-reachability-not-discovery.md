---
description: "Distinguishes backcast and reinvention benchmarks from autonomous discovery: they show that target insights are reachable from supplied ingredients, not that a system can select and verify new discoveries prospectively."
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, discovery]
---

# Known-target discovery benchmarks show reachability, not discovery closure

Known-target discovery benchmarks make novelty testable by replacing an open-ended objective with a hidden historical or authored target. They do not show that a system can do autonomous discovery. They show something narrower and still important: a later-recognized insight is **reachable** from supplied ingredients by an LLM plus a symbolic scaffold, search process, or training loop.

That reachability claim sits between a weaker claim and a stronger one. It is stronger than "the model can write plausible novelty," because the generated candidate is compared to a target whose value was established outside the current generation. It is weaker than practical discovery automation, because the benchmark already knows what counts as success.

## Two target constructions

**Backcast benchmarks** use temporal provenance as the leakage control. [GIANTS](../sources/giants-generative-insight-anticipation-scientific-literature.md), a benchmark for reconstructing downstream scientific insights from parent-paper summaries, is the example here. A model receives summaries of earlier parent papers and tries to reconstruct the core insight of a later downstream paper. The later paper supplies the target, so the authors do not need the same fixed-input neutrality controls as an authored experiment. The earlier papers were not written with knowledge of the future target; historical ordering does the control work.

**Reinvention benchmarks** need authored-input controls because the experimenter already knows the target. If prompts, concept pools, or rubrics are written after the target is known, the benchmark must prevent target leakage through canonical phrases, narrow micro-concepts, or suggestive scaffolding. The target can still be a useful oracle, but only if fixed inputs remain neutral enough that success means reconstruction from ingredients rather than prompt completion.

Both variants manufacture an oracle for a task that otherwise lacks one. The oracle is not "is this new idea valuable in the world?" but "does this candidate recover the target insight?" The benchmark has not solved open-ended discovery; it has converted discovery into target reconstruction or target reinvention.

## What reachability proves

Reachability means the insight is not inaccessible to the model-scaffold system. Given a constrained input set, generation procedure, and evaluation target, the system can traverse a path from precursor material to the later idea. This matters because it separates **idea synthesis capacity** from other hard parts of research. If a system cannot reconstruct known later insights from their ingredients, then stronger claims about prospective discovery are premature.

But reachability does not prove that the system can choose which problems to pursue, which lineages to combine, or which generated candidates deserve action. GIANTS deliberately isolates conditional synthesis: given a selected lineage, generate a target-like insight. That slice is useful, but it leaves parent selection, problem selection, and candidate triage outside the test.

The same boundary appears in [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md): generation is cheap, but evaluating whether a synthesis is genuine insight remains expensive. Known-target benchmarks temporarily supply that missing evaluator by importing a target from history or an authored benchmark.

## The missing practical loop

A practical discovery system needs more than a generator that can reach known targets. It needs a forward-looking verifier that can judge unknown candidates before the future reveals which ones mattered. Retrospective target comparison can train and test conditional synthesis, but it cannot close that loop by itself.

This is why known-target discovery benchmarks belong in the [oracle strength spectrum](./oracle-strength-spectrum.md) as soft-oracle manufacturing. They move a no-oracle task toward a usable proxy oracle. GIANTS hardens that proxy with human correlation, held-out splits, separate reward and evaluation judges, and independent preference checks. Those moves make the benchmark stronger, but they do not turn target similarity into prospective scientific validity.

So the automation boundary moves only partway. Known-target benchmarks show that an LLM plus symbolic system can reach some novel insights under controlled conditions. They do not remove the need for a verifier that can select valuable unknowns, so [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) still holds.

## Consequence

The right interpretation is:

> Known-target discovery benchmarks are reachability tests for insight synthesis, not end-to-end demonstrations of autonomous discovery.

That framing preserves their value without overstating them. They are useful because they create a measurable intermediate objective where open-ended discovery has no cheap ground truth. Their limitation is the same source of their power: the target is already known.

---

Relevant Notes:

- [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — grounds: known-target discovery benchmarks are one way to supply the missing synthesis oracle retrospectively
- [oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: target reconstruction is a soft-oracle manufacturing move, not a hard verifier for prospective discovery
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — extends: reachability moves the generation side of discovery but leaves the verifier boundary in place
- [conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — connects: known-target benchmarks test whether a system can reconstruct a general insight from supplied particulars
- [GIANTS: Generative Insight Anticipation from Scientific Literature](../sources/giants-generative-insight-anticipation-scientific-literature.md) — evidence: backcasts downstream scientific insights from earlier parent-paper summaries
