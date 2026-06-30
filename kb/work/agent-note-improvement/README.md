# Workshop: agent-note-improvement

Goal: find instructions that help agents improve existing notes, either by moving a weak version toward a later accepted version or by accurately marking why the weak version should not stand as-is.

## Starting question

Can an agent, given an existing note that has already passed through automatic improvement mechanisms, identify the parts that still make it weak?

The target behavior is not generic polishing. A useful instruction should do one or more of:

- find the note's strongest load-bearing point;
- identify speculative or low-yield expansions that make that point weaker;
- distinguish weak-but-plausible material from material that is simply false;
- recommend removal, compression, or isolation without erasing the central claim;
- explain what evidence or argument would be needed before a speculative section deserves to stay.

## Draft review bundles

- [compression](./compression/README.md) — workshop-local gates for true, defensible material that should still be compressed, folded, deleted, split, or rehomed because it does not earn its context cost.

## First case

Case 01 uses `kb/notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`.

- [baseline-e242c975](./case-01-llm-generation-relaxes-goals/baseline-e242c975.md) — historical version from `e242c975a2542b88d43b5d609ebbca27fd3bf3cd`, after substantial automatic improvement but still weak.
- [current-2026-06-16](./case-01-llm-generation-relaxes-goals/current-2026-06-16.md) — current accepted version, copied on 2026-06-16.
- [case notes](./case-01-llm-generation-relaxes-goals/README.md) — target delta and experiment log.

## Second case

Case 02 uses `kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md`.

- [baseline-working-tree](./case-02-prose-dereference/baseline-working-tree.md) — current working-tree text copied on 2026-06-16.
- [revised-split-rehome](./case-02-prose-dereference/revised-split-rehome.md) — local copy revised after running the split/rehome critique.
- [case notes](./case-02-prose-dereference/README.md) — critique result and applied-edit summary.

## Third case

Case 03 uses `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md`.

- [baseline-working-tree](./case-03-adversarial-loop-writing-filter/baseline-working-tree.md) — current working-tree text copied on 2026-06-16.
- [revised-from-prune-and-gate](./case-03-adversarial-loop-writing-filter/revised-from-prune-and-gate.md) — local copy revised from the prune, split/rehome, and marginal-value redundancy findings.
- [case notes](./case-03-adversarial-loop-writing-filter/README.md) — critique result and applied-edit summary.

## Experiment pattern

For each instruction under test:

1. Freeze the weak baseline and later accepted version.
2. Run the instruction against the baseline in a fresh agent.
3. Compare the output against the accepted delta.
4. Record whether the instruction found the weakness, proposed a direction compatible with the accepted revision, or missed the target.

## What would close this workshop

The workshop closes when it produces one of:

- a reusable note-improvement instruction;
- a critique or review-gate revision that reliably catches weak speculative expansions;
- a negative result explaining why the tested instruction family does not recover the accepted edits;
- a methodology note about when agent note-improvement should be subtractive rather than additive.

## Relevant local context

- [critique-note](../../instructions/critique-note.md) — first instruction under test.
- [auditable-llm-editing](../auditable-llm-editing/README.md) — neighboring workshop on stateful LLM editing and claim preservation.
- [review-revise-gated](../review-revise-gated/README.md) — prior workshop on review/revise arrangements that approximate manual edit quality.
