---
description: "Brainstorm on learning reusable review gates from accepted note edits: mine candidate gates from before/after diffs, store them atomically, and load a bounded subset into future reviews"
type: note
traits: []
tags: [kb-maintenance, learning-theory, context-engineering]
status: speculative
---

# Selector-loaded review gates could let review-revise learn from accepted edits

The review-revise experiments suggest a promising learning loop. We already have the hard part that most automatic writing systems lack: explicit human-accepted before/after pairs, named changes, and review outputs that can be scored against those changes. That makes review methodology a candidate for [spec mining](./spec-mining-as-codification.md): instead of only improving one note, the system can try to extract reusable gates from accepted edits.

The key architectural move is to stop treating a review lens as one large prompt bundle. A better substrate is a **registry of atomic gates** plus a selector that loads only the gates most relevant to the note under review. Storage can be flat; loading should be selective.

## What the workshop already shows

The workshop isolates a useful pattern:

- A manual edit session produced a concrete [change catalogue](../work/review-revise-gated/change-catalogue.md) with named failures and desired directions.
- A five-review battery produced stable hits for some categories, especially accessibility and sentence-level issues.
- Revision from review findings was useful but imperfect: some findings translated cleanly into edits, while others produced misses, wrong-direction changes, or hallucinated details.

This is already enough to distinguish three things that are currently conflated inside the review instructions:

1. **The review harness** — how to read, report, and score findings
2. **The lens** — accessibility, sentence-level, semantic, complexity
3. **The gate** — a single reusable check like "define opaque internal terms inline" or "remove stock 'not just X - it is Y' rhetoric"

The current instructions bundle all three. That makes them hard to grow, hard to prune, and expensive to load.

## Proposed architecture

Use a two-layer design:

- **Canonical storage:** a flat registry of atomic gates
- **Execution:** slim review harnesses that ask the selector for a bounded gate set

The flat registry is the right canonical form because the learned unit is not "the accessibility review" but "this specific check proved useful across accepted edits." Bundles can still exist, but as derived views rather than the storage primitive.

Each gate would be a small artifact with fields like:

- `gate_id`
- `lens`
- `problem-pattern`
- `test`
- `recommended-action`
- `anti-goal` or failure mode
- `examples`
- `provenance` — which note edits produced it
- `precision` / `recall` history
- `status` — candidate, active, quarantined, retired

That turns review methodology into inspectable substrate rather than prompt folklore.

## How gates would be learned

The learning loop could run on accepted human edits rather than on free-floating critique:

1. Capture the pre-edit note, post-edit note, and accepted diff.
2. Ask the agent to segment the diff into edit intentions, not just line changes.
3. Compare those intentions against gates that were already loaded.
4. For uncovered edits, propose candidate new gates.
5. For covered edits, update evidence that an existing gate still matters.
6. Let a human accept, merge, rewrite, or reject the candidate gate.

This keeps the oracle where it is strongest: not "was the critique clever?" but "did a human actually accept this change?"

The workshop's change catalogue is the seed format for this. It already separates baseline text, problem, and desired direction. A learned gate is basically a generalized version of one catalogue item.

## How gates would be loaded

A fixed number of gates is better than the current unbounded bundling, but a **fixed token budget** is better than a fixed count. Some gates are one line; others need a counterexample. The selector should load until the review budget is full, not until an arbitrary count is reached.

A good loading policy would combine:

- **Always-on base gates** — universally cheap, high-precision checks
- **Lens-specific gates** — only when running that lens
- **Retrieved gates** — selected for this note by title, tags, vocabulary, type, and prior similar failures
- **Diversity pressure** — avoid spending the whole budget on five near-duplicate clarity gates

This matches the repo's broader [loading-frequency discipline](./instruction-specificity-should-match-loading-frequency.md): keep always-loaded review instructions slim, push specificity into on-demand gate loading.

## Why this is better than just extending the review prompts

Monolithic review instructions have four failure modes:

- They accumulate checks without any retrieval discipline, so every run pays for every old lesson.
- They hide which finding came from which gate, so precision and recall cannot be measured per unit.
- They make pruning socially hard: removing one paragraph feels like changing the whole review.
- They encourage lens-level thinking when the real reusable unit is smaller.

An atomic registry fixes all four. If a gate starts producing noise, it can be quarantined without rewriting the rest of the review method. If a gate is consistently useful, it can be promoted toward stronger enforcement.

## The maturation path

Not every good gate should remain an LLM review check forever. The natural path is:

1. **Workshop candidate gate** — extracted from one accepted edit
2. **Active review gate** — loaded selectively into future reviews
3. **Distilled instruction** — folded into a lens harness once it is stable and general
4. **Deterministic check** — promoted into `/validate` or another script if the oracle becomes hard enough

This is exactly the [methodology enforcement gradient](./methodology-enforcement-is-constraining.md). The point of the registry is not just to store gates; it is to let them mature at different rates.

## Where the hard problems still are

The proposal does not remove the oracle problem. It only narrows it.

- A human-accepted edit is a strong oracle for "this change was wanted here," but only a weak oracle for "this should generalize."
- Some edits are coupled. A structural rewrite may also fix local clarity issues, making gate attribution ambiguous.
- A gate can overfit one author's style or one note family.
- Revision can satisfy the gate while making the note worse in another way.

The workshop already shows this danger. The same review battery that caught many accessibility and sentence-level issues also missed several structural changes and once induced a factual error about Slate's attribution. A learned-gate system therefore needs promotion and rollback, not just accumulation.

## A better storage split than "flat space only"

The user's flat-space intuition is right for canonical storage, but I would not make flatness the whole design. A better split is:

- **Flat gate registry** for atomic storage and learning
- **Derived lens packs** for maintenance and human inspection
- **Selector-loaded runtime slices** for actual review execution

That preserves the benefits of flat storage without forcing the runtime to behave like a flat memory system. The runtime should see a small, task-shaped slice, not the whole registry.

## Open questions

- What is the minimal gate schema that still supports pruning and promotion?
- Should candidate gates live in a workshop area while active gates live in `kb/instructions/`?
- What metric should promotion use: precision only, stable recurrence, or measured contribution to accepted revisions?
- Should revision see the raw gate text, or only the findings emitted from those gates?
- Can we mine negative gates too — patterns that looked useful once but later caused mistakes?

The main claim is narrower than "automatic writing improvement." It is that the review-revise workflow has already produced the right raw material for a **selector-driven gate learning loop**. If we keep storing lessons only as bigger review prompts, we throw that structure away.

---

Relevant Notes:

- [spec-mining-as-codification](./spec-mining-as-codification.md) — foundation: accepted edits can be mined into reusable review gates the same way repeated behavior can be mined into deterministic checks
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — enables: candidate gates can mature from workshop artifacts into instructions and, for hard-oracle cases, scripts
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: a gate registry should be selectively loaded under a bounded budget rather than bundled into always-growing review prompts
- [automated-tests-for-text](./automated-tests-for-text.md) — adjacent mechanism: learned gates are one path to defining text contracts from real failures rather than from an abstract checklist
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — extends: promotion and retirement of gates need weak composite signals, not just accumulation
- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — scope condition: this proposal narrows the automation target to review gates, where accepted edits provide a stronger oracle than open-ended KB mutation
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: review-revise is a workshop process whose durable output would be reusable gates in the library layer
- [context-engineering](./definitions/context-engineering.md) — frame: selector-loaded gates are a routing and loading design for bounded review contexts, not just a writing trick
