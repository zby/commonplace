---
description: "When an artifact carries a copy of information recomputable from a ground-truth source, the copy must be machine-checked against that source or not exist — hand-maintained-and-trusted is forbidden"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, kb-maintenance]
status: seedling
---

# A derived copy of recomputable truth must be checked or absent

Some artifacts carry a copy of information that is mechanically recomputable from a ground-truth source elsewhere in the system: a completeness mark, a compiled cue, a hardcoded contract list inlined in a hot-path instruction, a duplicated file. Such a copy has exactly two valid states. Either it is **checked** — a validator re-derives it from the source and fails on mismatch — or it is **absent**: deleted, or replaced by reading the source live. There is no safe middle where the copy is maintained by hand and trusted by consumers.

## The asymmetry that forces the rule

The two failure modes are not symmetric, and the rule rides entirely on that. An *absent* copy costs the consumer one bounded recomputation: run the query, read the source, do the work the copy would have saved. A *false* copy costs silent, unbounded wrongness — it tells consumers to stop looking, or to follow a snapshot of a world that has since moved, with no signal that anything is wrong. This is the [stale-indexes failure](./stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: a trusted-but-stale claim suppresses exactly the fallback that would have recovered the truth.

A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky. An unenforced copy is always one missed edit away from the catastrophic state, with nothing watching.

## Where the rule applies: the deterministic end of derived knowledge

Every distilled artifact is a derived copy of its sources, and for derived knowledge in general the KB runs *managed staleness*: [tracked lineage](./distilled-artifacts-need-source-tracking.md) so a source change names its downstream distillates, [make-like timestamp comparison](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) to detect when review is due, and [re-distillation rather than patching](./evolving-understanding-needs-re-distillation-not-composition.md) as the fix. That machinery stops at *review* because verification there is judgment: deciding whether a revised source invalidates a distilled instruction is a Level B check in the [text testing pyramid](./text-testing-framework.md) — an LLM reading both and judging fidelity — too costly to run always and too noisy to block on. In that regime the hand-maintained derived artifact is not forbidden; it is unavoidable, and the design effort goes into placing the lineage record so the staleness signal interrupts the editor at edit time.

What flips the regime is the check price. Mechanical derivation makes verification Level A: deterministic, near-zero cost, binary, runnable on every validation pass — detection and verification collapse into one free step, where the general case needs a cheap detector and an expensive judge. Two things change at that price. The economics that excused the unchecked copy disappear — trusting it saves nothing — so enforce-or-omit stops being aspirational and becomes the rule, and findings stop advising and start blocking. And the interrupt-placement problem the general note solves by design dissolves: the validator *is* the edit-time surface, firing wherever the record lives, so lineage no longer needs to sit where a human will see it — only where a machine can follow it. Same structure throughout — derived copy, moving source, staleness risk — at a different check price; the price is what changes the balance.

## What enforcement buys

Two established principles pull in opposite directions on recomputable values, and enforcement is what dissolves the collision.

[Frontloading spares execution context](./frontloading-spares-execution-context.md) wants the value inlined: pre-compute what is known before the call and insert the result, because re-deriving it — reading the contract on every skill invocation — is a recurring hot-path context cost. [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) wants the same value left out: anything the executor can determine from the live situation goes stale by ignorance, drift, or the run itself, so pin only goals, constraints, done-criteria, and genuinely arbitrary choices. The type spec can change; the inlined list is a situational snapshot.

Both are right, and enforcement creates the third class that lets them coexist. Between *arbitrary* (safe to pin, because the situation never determines it) and *situational* (brittle to pin, because the situation determines it and then moves) sits **recomputable-and-checked**: the situation determines the value, but a machine watches the situation on the author's behalf. The check converts staleness-by-drift and staleness-by-ignorance into a validation failure caught at check time, not a silently wrong snapshot discovered by the executor mid-task. The author keeps frontloading's context economy *and* the executor principle's freshness guarantee — enforcement is the move that secures frontloading's validity window.

## What "checked" requires — and its limits

Enforcement is available only when three preconditions hold:

1. **A derivation rule.** The copy must be mechanically re-derivable from the source. Extractable lists, set memberships, and file identity qualify; prose summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted.
2. **Machine-locatability.** The copy must occupy a marked region that names its source — the [lineage](./definitions/lineage.md) the validator follows to find the ground truth and re-derive. Machine-followable suffices; human visibility is not required once the validator carries the interrupt.
3. **Ground truth that exists at validation time.** Enforcement cannot help where execution itself produces the evidence: a plan's executor learns things no validator could pre-check, because the run generates them. When this precondition fails, the value was never a recomputable copy in the first place — that territory stays with the executor.

## Consequences

- **Checked copies degrade gracefully.** Dropping one costs consumers a recomputation, never correctness, so lifecycle exits stay cheap: a copy that outgrows its purpose is deleted and readers fall back to the source.
- **Never write the unenforced prose version of a checkable claim.** "This list is complete" with no validator behind it is exactly the hand-maintained-and-trusted state the rule forbids. A checkable claim is enforced as a check or not asserted at all.
- **When a copy can't be checked, the resolution is omission.** Either delete the copy ([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) deleted committed generated indexes) or read the source live (the 2026-06-10 skill edits chose read-the-contract per invocation). Both are correct; both pay a build-time or hot-path cost that enforcement would have avoided. Omission is the fallback, not the optimum.

## Instances across four surfaces

Four surfaces in the system instantiate the rule, each in a different state of application — already enforced, stated but unenforced, resolved by omission, and not yet applied. The spread is what shows it generalizes:

- **`complete`/`covered_by` marks on tag-READMEs** — enforced and shipped. A validator re-derives membership from the scoped `rg` sweep and fails on mismatch (see [mark-semantics.md](../reference/mark-semantics.md)).
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
- [Distilled artifacts need source tracking](./distilled-artifacts-need-source-tracking.md) — extends: the general managed-staleness rule this note specializes; there verification is judgment, lineage placement carries the interrupt, and the rule tops out at review
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — contrasts: the general case splits cheap detection from expensive judgment-rebuild; in the deterministic case both collapse into one free validator step
- [Text testing framework](./text-testing-framework.md) — grounds: the Level A/B check-cost gradient is what names the boundary — the rule flips from managed staleness to enforce-or-omit exactly where the check drops to Level A
- [Mark semantics](../reference/mark-semantics.md) — evidence: the shipped, validator-enforced instance of the rule
- [ADR 027 — Package scaffold assets without source-tree symlinks](../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — evidence: source-of-truth for the byte-identical `AGENTS.md.template` duplication cited as the fourth instance
