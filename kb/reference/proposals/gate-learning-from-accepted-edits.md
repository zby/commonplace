---
description: "Proposal: learn review gates from accepted note edits, with candidate mining, usefulness tracking, lifecycle promotion, and budgeted loading. Atomic gates shipped; learning has not"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Gate learning from accepted edits

The review system could learn new gates from human-accepted edits instead of accumulating lessons as ever-larger prompts. The central constraint rests on [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md): accepted edits are the strongest available seed, but candidates mined from them are instance-verified, not rules — so the design must carry a promotion-and-rollback lifecycle, not just accumulation. This proposal holds the learning loop, the gate-lifecycle additions, and the loading policy.

## Current state (as of 2026-06-12)

Shipped — proposed alongside this loop and since adopted:

- Atomic gates as single files with a type contract: `kb/instructions/review-gates/{lens}/{name}.md`, type `review-gate`.
- Per-gate provenance, acceptance, and staleness: `gate_sha`, per-gate acceptance rows and current-acceptance views in the review SQLite store.
- Selector machinery: `resolve_gates`, `review_target_selector`, `warn_selector`. [ADR 031](../adr/031-review-state-uses-run-owned-review-pairs.md) records the move from monolithic review bundles to gate-native, run-owned review pairs.

Not shipped:

- Any learning path from accepted edits to new gates.
- Per-gate precision/recall history; gate lifecycle states beyond existence.
- Retrieval- or budget-based gate loading beyond static gate resolution.

Raw material exists: review-revise experiments produced human-accepted before/after pairs with named changes (change catalogues in workshop runs) — exactly the capture format a mined candidate generalizes from.

## The learning loop

1. Capture the pre-edit note, post-edit note, and accepted diff.
2. Segment the diff into edit intentions, not line changes.
3. Compare intentions against the gates that were loaded for the originating review.
4. For uncovered intentions, propose candidate gates.
5. For covered intentions, update evidence that the existing gate still earns its place.
6. A human accepts, merges, rewrites, or rejects each candidate.

The oracle stays where it is strongest: "did a human accept this change," not "was the critique clever." Step 6 is the promotion gate the oracle asymmetry requires.

## Gate lifecycle additions

Each gate gains: `status` (candidate / active / quarantined / retired), `provenance` (which accepted edits produced or confirmed it), and a precision/recall history per run. A noisy gate is quarantined without rewriting the rest of the review method; a consistently useful one can mature toward a deterministic check — the methodology enforcement gradient. The registry stays inspectable substrate rather than prompt folklore.

## Loading policy

A fixed token budget beats a fixed gate count — some gates are one line, others need a counterexample. The selector fills the budget from: always-on base gates (cheap, high-precision), lens-specific gates, retrieved gates (matched to the note by tags, vocabulary, type, prior similar failures), with diversity pressure against spending the budget on near-duplicates. Rests on [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md): always-loaded review instructions stay slim, specificity moves into on-demand gate loading.

## Alternative stance: open-ended, opportunistic, budget-bounded

This proposal assumes a *maintained-converging* registry: mine gates, promote useful ones, prune weak ones, and improve coverage over time. The opposing stance treats the catalogue as irreducibly open-ended. Review then optimizes for **marginal value, not coverage**: run a focused pass while expected accepted-edit yield beats token cost, and allow ad-hoc lenses aimed at one note's specific risk without forcing them into the registry.

The hybrid is plausible: keep a small always-on base set, load registry gates under budget, and spend remaining budget on opportunistic lenses. The disagreement is what review converges toward: a growing maintained registry, or no closed catalogue by design. The case for opportunism rests on focused-pass behavior: a diffuse reviewer can read past weak joints, while a separate single-aspect lens can force the issue that an all-purpose critique smooths over.

## Risks

- Attribution ambiguity in coupled edits (a structural rewrite also fixes clarity — which gate earned the acceptance?).
- Candidate gates overfitting one author's style or one note family.
- Revisions that satisfy a gate while worsening the note elsewhere.
- Observed in the seed experiments: review batteries missed structural changes and once induced a factual error — rollback is load-bearing, not optional.

## Open questions

- The minimal gate schema that still supports pruning and promotion.
- Where candidates live (a workshop area?) versus active gates (`kb/instructions/review-gates/`).
- The promotion metric: precision alone, stable recurrence, or measured contribution to accepted revisions — composite weak signals are a candidate ([quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md)).
- Whether revision should see raw gate text or only the findings emitted from gates.
- Negative gates: mining patterns that looked useful once but later caused mistakes.
- Maintained-converging vs opportunistic: should review grow a maintained registry, or stay open-ended with ad-hoc lenses governed by marginal value?

---

Relevant Notes:

- [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — rationale: the oracle asymmetry that dictates candidate status, promotion, and rollback
- [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — rationale: mining reusable checks from observed accepted behavior is the general move this design instantiates
- [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — rationale: budget-bounded selective loading instead of always-growing review prompts
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — rationale: the maturation gradient gates climb from candidate toward deterministic check
- [review architecture](../review-architecture.md) — part-of: the shipped review subsystem this loop would extend
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — rationale: focused review passes can recover weak joints that diffuse all-purpose review reads past
