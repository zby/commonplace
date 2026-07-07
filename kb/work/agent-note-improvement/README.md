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

## Combined instruction

- [run-full-improvement-pass-on-note](./run-full-improvement-pass-on-note.md) — sequences the compression bundle, `critique-note`, the optional production `semantic` bundle, and `cp-skill-connect` over one note, then reconciles their findings into a single editorial packet. Drafted from the interim comparisons below (case 01's table, case 02's `critique-note` vs. prune-weak-expansions split, case 03's compression-bundle-beats-single-gate result). Run end-to-end for the first time in case 04.

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

## Fourth case

Case 04 uses `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` — the first live run of [run-full-improvement-pass-on-note](./run-full-improvement-pass-on-note.md), applied directly to a current library note rather than a frozen baseline/accepted-delta pair, so there is no separate "accepted delta" to compare against; the edit was made in place.

- Reports: [compression-bundle-review](./full-pass-a-derived-copy-of-recomputable-truth/compression-bundle-review.md); `critique-note` report at `kb/reports/critique/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.critique.md`; connect report at `kb/reports/connect/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.connect.md` (semantic bundle skipped — exploratory pass, not a promotion decision).
- Synthesis packet: [full-pass-report](./full-pass-a-derived-copy-of-recomputable-truth/full-pass-report.md).

Result: clean end-to-end run, no reconciliation failures.

- Compression and critique-note found genuinely different things, matching the instruction's ordering rationale: compression flagged two passages that had outgrown their argumentative job ("What enforcement buys," half of "Where the rule applies"), while critique-note surfaced a real unaddressed gap — the validator-correctness regress (a validator is itself a hand-maintained artifact making an unchecked claim). Reconciliation kept both: cut the compression-flagged passages and added a fourth precondition addressing the critique, netting out close to length-neutral.
- Connect added three missing reciprocal links and caught one unauthorized footer label (`complements`, not in `kb/notes/COLLECTION.md`'s label set) — a small maintenance find none of the other three methods could have caught.
- The step 8 flow/coherence pass made only two small wording fixes and reintroduced nothing, confirming the "copyedit only, do not reopen content decisions" boundary held in practice, not just on paper.

Takeaway: this is the first case where all four methods' outputs were genuinely complementary rather than overlapping or conflicting — plausibly because this note (dense, many links, single-thesis) sits squarely in compression's and critique-note's separate strike zones rather than needing one to arbitrate the other. A future case should stress-test the reconciliation rules on a note where compression and critique actually disagree about the same passage, which did not happen here.

## Experiment pattern

For each instruction under test:

1. Freeze the weak baseline and later accepted version.
2. Run the instruction against the baseline in a fresh agent.
3. Compare the output against the accepted delta.
4. Record whether the instruction found the weakness, proposed a direction compatible with the accepted revision, or missed the target.

## What would close this workshop

The workshop closes when it produces one of:

- a reusable note-improvement instruction — [run-full-improvement-pass-on-note](./run-full-improvement-pass-on-note.md) is the current candidate; case 04 was a clean run, but promotion should wait for a case where compression and critique-note actually disagree on the same passage;
- a critique or review-gate revision that reliably catches weak speculative expansions;
- a negative result explaining why the tested instruction family does not recover the accepted edits;
- a methodology note about when agent note-improvement should be subtractive rather than additive.

## Relevant local context

- [critique-note](../../instructions/critique-note.md) — first instruction under test.
- [auditable-llm-editing](../auditable-llm-editing/README.md) — neighboring workshop on stateful LLM editing and claim preservation.
- [review-revise-gated](../review-revise-gated/README.md) — prior workshop on review/revise arrangements that approximate manual edit quality.
