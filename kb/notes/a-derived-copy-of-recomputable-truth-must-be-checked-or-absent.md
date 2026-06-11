---
description: "When an artifact carries a copy of information recomputable from a ground-truth source, the copy must be machine-checked against that source or not exist — hand-maintained-and-trusted is forbidden"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, kb-maintenance]
status: seedling
---

# A derived copy of recomputable truth must be checked or absent

Some artifacts carry a copy of information that is mechanically recomputable from a ground-truth source elsewhere in the system: a completeness mark, a compiled cue, a hardcoded contract list inlined in a hot-path instruction, a duplicated file. Such a copy has exactly two valid states. Either it is machine-checked against its source — a validator re-derives and compares, failing on mismatch — or it does not exist: delete it, or read the source live. There is no safe middle where the copy is maintained by hand and trusted by consumers.

## The asymmetry that forces the rule

The two failure modes are not symmetric, and the rule rides entirely on that. An *absent* copy costs the consumer one bounded recomputation: run the query, read the source, do the work the copy would have saved. A *false* copy costs silent, unbounded wrongness — it tells consumers to stop looking, or to follow a snapshot of a world that has since moved, and they have no signal that anything is wrong. This is the [stale-indexes failure](./stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: a trusted-but-stale claim suppresses the fallback that would have recovered the truth, so the gap becomes invisible rather than merely costly.

That asymmetry is why hand-maintained-and-trusted is *forbidden* rather than merely risky. The downside of absence is bounded and recoverable; the downside of a false copy is neither — and an unenforced copy is always one missed edit away from it, with nothing watching.

## Reconciling two pulls

Two established principles pull in opposite directions on recomputable values, and enforcement is what dissolves the collision.

[Frontloading spares execution context](./frontloading-spares-execution-context.md) says: pre-compute values known before a call and insert the result, sparing the hot path the cost of deriving them. It already demands a *validity window* — lineage or regeneration rules — for any inserted value that can change. So frontloading wants the contract list inlined in the write skill, because reading the contract on every invocation is a recurring hot-path context cost.

[An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) says the opposite for this same value: anything the executor can determine from the live situation goes stale by ignorance, drift, or the run itself, so pin only goals, constraints, done-criteria, and genuinely arbitrary choices. A type spec can change; the inlined copy is a situational snapshot; leave it to the executor to read live.

Both are right, and they point opposite directions on the same value. Enforcement creates a third class on the fix-or-leave axis. Between *arbitrary* (safe to pin, because the situation never determines it) and *situational* (brittle to pin, because the situation determines it and then moves) sits **recomputable-and-checked**: the situation determines the value, but a machine watches the situation on the author's behalf. A validator that re-derives the copy from its source and fails on mismatch converts staleness-by-drift and staleness-by-ignorance into a visible validation failure — caught at check time, not discovered by the executor mid-task as a silently wrong snapshot. The author keeps frontloading's context economy *and* the executor principle's freshness guarantee. Enforcement is precisely the move that secures frontloading's validity window.

## What "checked" requires — and its limits

Enforcement is only available when three preconditions hold:

1. **A derivation rule.** The copy must be mechanically re-derivable from the source. Extractable lists, set memberships, and file identity are checkable: a validator can re-extract and compare. Prose summaries and judgments are not — there is no comparison a machine can run, so they stay as live reads or are omitted.
2. **Machine-locatability.** The copy must occupy a marked region that names its source — the [lineage](./definitions/lineage.md) the validator follows to find the ground truth and re-derive.
3. **Ground truth that exists at validation time.** Enforcement cannot help where execution itself produces the evidence: a plan's executor learns things no validator could pre-check, because the run generates them. That part of the fix-what-the-executor territory is untouched by this rule — when the precondition fails, the value was never a recomputable copy in the first place.

## Consequences

- **Checked copies degrade gracefully.** Dropping one costs consumers a recomputation, never correctness, so lifecycle exits stay cheap: a copy that outgrows its purpose is deleted and readers fall back to the source.
- **Never write the unenforced prose version of a checkable claim.** "This list is complete" with no validator behind it is exactly the hand-maintained-and-trusted state the rule forbids. A checkable claim is enforced as a check or not asserted at all.
- **When a copy can't be checked, the resolution is omission.** Either delete the copy ([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) deleted committed generated indexes) or read the source live (the 2026-06-10 skill edits chose read-the-contract per invocation). Both are correct; both pay a build-time or hot-path cost that enforcement would have avoided. Omission is the fallback, not the optimum.

## Instances across four surfaces

Four surfaces in the system instantiate the rule, each in a different state of application — already enforced, stated but unenforced, resolved by omission, and not yet applied. The spread is what shows it generalizes:

- **`complete`/`covered_by` marks on tag-READMEs** — enforced and shipped. A validator re-derives membership from the scoped `rg` sweep and fails on mismatch (see [mark-semantics.md](../reference/mark-semantics.md)).
- **Compiled memory views and cues** — the general source-of-truth requirement, stated for memory systems in [keep-compiled-views-aligned](./agent-memory-requirements/keep-compiled-views-aligned.md): a derived surface needs provenance, regeneration rules, and staleness detection so it does not become an independent authority.
- **Hardcoded contract values in hot-path skills** — currently resolved by omission (read the contract live). Enforcement — a marked frontloaded region whose extractable list a validator re-derives — would dominate, recovering the context economy without the drift.
- **Duplicated build artifacts** — the two tracked `AGENTS.md.template` copies (root feeds wheel builds via `pyproject` `force-include`; `src/commonplace/_data` serves editable installs) must be byte-identical. This is the trivially checkable case: file identity, one comparison.

It is the general form of "a cache must never be the only copy" — applied not only to caches but to every derived copy of recomputable truth.

## Open Questions

- Where else does an unenforced prose claim quietly stand in for a checkable one (the `status:` maturity field is a candidate trust mark with no validator)?
- What is the cheapest general mechanism for marked, locatable, checkable frontloaded regions in instruction text?

---

Relevant Notes:

- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — grounds: the absence-degrades-to-search vs presence-suppresses-search asymmetry that makes false copies catastrophic
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — extends: enforcement is the move that secures frontloading's validity window for recomputable inserted values
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: adds recomputable-and-checked as a third class between arbitrary and situational on its fix-or-leave axis
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — extends: generalizes its compiled-view source-of-truth rules beyond memory systems to any derived copy of recomputable truth
- [Mark semantics](../reference/mark-semantics.md) — evidence: the shipped, validator-enforced instance of the rule
