---
description: "When an artifact carries a copy of information recomputable from a ground-truth source, the copy must be machine-checked against that source or not exist — hand-maintained-and-trusted is forbidden"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, kb-maintenance]
---

# A derived copy of recomputable truth must be checked or absent

Some artifacts carry a copy of information that is mechanically recomputable from a ground-truth source elsewhere in the system: a completeness [mark](../types/tag-readme.md) (a frontmatter field caching a recomputable index property), a compiled cue (a memory system's derived retrieval hint), a hardcoded contract list inlined in a hot-path instruction, a duplicated file. Such a copy has exactly two valid states. Either it is **checked** — a validator re-derives it from the source and fails on mismatch — or it is **absent**: deleted, or replaced by reading the source live. There is no safe middle where the copy is maintained by hand and trusted by consumers.

## The asymmetry that forces the rule

The two failure modes are not symmetric, and the rule rides entirely on that. An *absent* copy costs the consumer one bounded recomputation: run the query, read the source, do the work the copy would have saved. A *false* copy costs silent, unbounded wrongness — it tells consumers to stop looking, or to follow a snapshot of a world that has since moved, with no signal that anything is wrong. This is the [stale-indexes failure](./stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: a trusted-but-stale claim suppresses exactly the fallback that would have recovered the truth.

A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky. An unenforced copy is always one missed edit away from the catastrophic state, with nothing watching.

## Where the rule applies: the deterministic end of derived knowledge

Any use-shaped artifact depends on its sources — whether its content is worked out from them (a derived copy) or generalizes beyond them (an abstracted rule, answerable to its sources as evidence). For dependent knowledge in general the KB runs *managed staleness*: [tracked lineage](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) names the downstream artifacts when a source changes, [make-like timestamp comparison](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) detects when review is due, and [holistic rework rather than patching](./evolving-understanding-needs-holistic-rewrite-not-composition.md) is the fix. The repair follows the regime: re-derive and compare where the content is recoverable from the source, re-examine the support where it exceeds it. That machinery stops at *review* because verification there is judgment. Deciding whether a revised source invalidates a downstream instruction is a Level B check in the [text testing pyramid](./text-testing-framework.md) — an LLM reading both and judging fidelity or support — too costly to run always and too noisy to block on. In that regime the hand-maintained dependent artifact is not forbidden; it is unavoidable, and the design effort goes into placing the lineage record so the staleness signal interrupts the editor at edit time.

What flips the regime is the check price: mechanical derivation makes verification Level A — deterministic, near-zero cost, binary, runnable on every pass. Detection and verification then collapse into one free step, instead of needing a cheap detector plus an expensive judge. Two things change. Enforce-or-omit stops being aspirational and becomes the rule, since trusting an unchecked copy now saves nothing. And the interrupt-placement problem dissolves, since the validator *is* the edit-time surface — lineage only needs to sit where a machine can follow it, not where a human will see it.

## What enforcement buys

[Frontloading spares execution context](./frontloading-spares-execution-context.md) wants a recomputable value inlined, since re-deriving it on every call is a hot-path cost; [an author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) wants the same value left out, since anything the situation determines goes stale by drift or ignorance. Enforcement is the third class that lets both stand: between *arbitrary* (safe to pin) and *situational* (brittle to pin) sits **recomputable-and-checked**. Here a machine watches the situation on the author's behalf, converting staleness into a validation failure at check time instead of a silently wrong snapshot discovered mid-task.

## What "checked" requires — and its limits

Enforcement is available only when four preconditions hold:

1. **A derivation rule.** The copy must be mechanically re-derivable from the source. Extractable lists, set memberships, and file identity qualify; prose summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted.
2. **Machine-locatability.** The copy must occupy a marked region that names its source — the [lineage](./definitions/lineage.md) the validator follows to find the ground truth and re-derive it. Machine-followable suffices; human visibility is not required once the validator carries the interrupt.
3. **Ground truth that exists at validation time.** Enforcement cannot help where execution itself produces the evidence: a plan's executor learns things no validator could pre-check, because the run generates them. When this precondition fails, the value was never a recomputable copy in the first place — that territory stays with the executor.
4. **A validator expected to bottom out, not recurse.** The validator is itself a hand-authored artifact making an unchecked claim — that it correctly re-derives the copy. This looks like it reopens the regress, but it doesn't: a validator is centralized, versioned, reviewed on every change, and amortized across every copy it protects, so its unit cost of correctness-assurance is far lower than N independently hand-maintained instances would be. A derivation rule that is itself a judgment call rather than a strict mechanical extraction does not meet this precondition — it is the forbidden state, just relocated one layer down, with a stronger trust signal attached.

## Consequences

- **Checked copies degrade gracefully.** Dropping one costs consumers a recomputation, never correctness, so lifecycle exits stay cheap: a copy that outgrows its purpose is deleted and readers fall back to the source.
- **Never write the unenforced prose version of a checkable claim.** "This list is complete" with no validator behind it is exactly the hand-maintained-and-trusted state the rule forbids. A checkable claim is enforced as a check or not asserted at all.
- **When a copy can't be checked, the resolution is omission.** Either delete the copy ([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) deleted committed generated indexes) or read the source live (the 2026-06-10 skill edits — logged in `kb/log.md` — chose read-the-contract per invocation). Both are correct; both pay a build-time or hot-path cost that enforcement would have avoided. Omission is the fallback, not the optimum.

## Instances across four surfaces

Four surfaces in the system instantiate the rule, each in a different state of application — already enforced, stated but unenforced, resolved by omission, and not yet applied. The spread is what shows it generalizes:

- **`complete`/`covered_by` marks on tag-READMEs** (the curated per-tag index files) — enforced and shipped. A validator re-derives membership from the scoped `rg` sweep and fails on mismatch (the mark contract is in the [`tag-readme` type spec](../types/tag-readme.md)). The sweep pattern is hand-authored, but it executes as a strict mechanical extraction — and precondition 4's amortization argument is what keeps the pattern's authorship acceptable instead of a quiet regress.
- **Compiled memory views and cues** — the general source-of-truth requirement, stated for memory systems in [keep-compiled-views-aligned](./agent-memory-requirements/keep-compiled-views-aligned.md): a derived surface needs provenance, regeneration rules, and staleness detection so it does not become an independent authority.
- **Hardcoded contract values in hot-path skills** — currently resolved by omission (read the contract live). Enforcement — a marked frontloaded region whose extractable list a validator re-derives — would dominate, recovering the context economy without the drift.
- **Duplicated build artifacts** — the two tracked `AGENTS.md.template` copies (root feeds wheel builds via `pyproject` `force-include`; `src/commonplace/_data` serves editable installs) must be byte-identical (the two-copy layout is designed in [ADR 027](../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md)). This is the trivially checkable case: file identity, one comparison.

It is the general form of "a cache must never be the only copy" — applied not only to caches but to every derived copy of recomputable truth.

## Open Questions

- Where else does an unenforced prose claim quietly stand in for a checkable one (the `status:` maturity field is a candidate trust mark with no validator)?
- What is the cheapest general mechanism for marked, locatable, checkable frontloaded regions in instruction text?

---

Relevant Notes:

- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — grounds: the absence-degrades-to-search vs presence-suppresses-search asymmetry that makes false copies catastrophic
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the "checked" branch exists only where a cheap deterministic oracle can re-derive and compare; where verification is unavailable, omission is the only safe state
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — extends: enforcement is the move that secures frontloading's validity window for recomputable inserted values
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: adds recomputable-and-checked as a third class between arbitrary and situational on its fix-or-leave axis
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — extends: generalizes its compiled-view source-of-truth rules beyond memory systems to any derived copy of recomputable truth
- [Artifacts produced from sources need lineage recorded at the source](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — extends: the general managed-staleness rule this note specializes; there verification is judgment, lineage placement carries the interrupt, and the rule tops out at review
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — contrasts: the general case splits cheap detection from expensive judgment-rebuild; in the deterministic case both collapse into one free validator step
- [Text testing framework](./text-testing-framework.md) — grounds: the Level A/B check-cost gradient is what names the boundary — the rule flips from managed staleness to enforce-or-omit exactly where the check drops to Level A
- [tag-readme type spec](../types/tag-readme.md) — evidence: the `complete`/`covered_by` marks are the shipped, validator-enforced instance of the rule; the mark contract lives here
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: the value half — recompute being dear to a model is what makes a checked derived copy worth keeping in the first place
- [ADR 027 — Package scaffold assets without source-tree symlinks](../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — evidence: source-of-truth for the byte-identical `AGENTS.md.template` duplication cited as the fourth instance
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — contrasts: the non-recomputable complement of preconditions 1 and 3 — history must be recorded at production time because there is no later ground truth left to re-derive it from
- [An enforced tag-README is a MOC with a machine-checked contract](./an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — extends: develops this note's instance 1 (the tag-README marks) into the fuller MOC-plus-contract argument
- [Prose has no reliable dereference, so a declared fact must be reinforced where it applies](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — extends: the worked prose-regime case for this note's first open question, with `status:` as the candidate unenforced trust mark
