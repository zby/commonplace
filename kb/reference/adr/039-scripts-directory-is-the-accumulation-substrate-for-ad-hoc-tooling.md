---
description: "scripts/ is named the committed home for reusable ad hoc tooling, distinct from throwaway python3 heredocs and the installed package, with a cleanup norm and a promotion signal"
type: ../types/adr.md
tags: []
status: accepted
---

# 039-`scripts/` is the accumulation substrate for ad hoc tooling

**Status:** accepted
**Date:** 2026-07-07

## Context

`AGENTS.md`'s Development section named two tiers of code: `python3` for stdlib-only throwaway tooling, and the installed `commonplace` package for shipped `commonplace-*` commands. A third tier already existed in practice and had existed since the repository's first commit — the git-tracked `scripts/` directory, holding ad hoc tooling that is committed (not thrown away) but hasn't earned a `commonplace-*` entry point. [ADR-014](./014-scripts-as-python-package-one-tree-model.md) documents the one precedent for a promotion out of `scripts/`, at subsystem scale, but nothing named the tier itself, its lifecycle, or when an individual script should graduate.

The gap showed up concretely: `scripts/move-reviews-to-subdir.py`, self-described as "one-off" and last touched in April, sat unused and undeleted for months — the only genuine evidence of drift, but real.

## Decision

Name `scripts/` explicitly as the destination for ad hoc tooling expected to be reused (by the same agent later in a session, or by a future one), distinct from both heredoc-and-discard and the installed package. Adopt two lightweight norms alongside it:

- **Cleanup norm.** A script whose docstring says "one-off" or "temporary" is deleted by whoever finishes using it, in the same session or commit series, rather than left for someone else to notice later.
- **Promotion signal.** A script graduates to a `commonplace-*` command when it has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes — repetition with a stable interface, the same signal spec mining uses generally ([spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md)) and consistent with committing only after patterns stabilize ([progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md)). A script whose interface is still changing hasn't stabilized enough to promote, no matter how many times it's been touched. This is a judgment call exercised periodically (e.g., at monthly triage), not a mechanical trigger.

The rule lives in two places: a one-line pointer in `AGENTS.md` (visible to every agent immediately) and the fuller norm/signal detail in `scripts/README.md` (visible to an agent that opens the directory). No scheduled sweep or expiry-timestamp machinery is adopted — one stale file in six, over 15 months, is thin evidence for anything heavier than an informal norm.

## Consequences

Easier:

- An agent deciding between a heredoc and a saved file has a documented decision point instead of guessing.
- Stale one-off scripts have a stated exit path, so `scripts/` stays a substrate rather than a junk drawer.
- A future triage pass reviewing `scripts/` contents has a named promotion signal instead of re-deriving one from ADR-014.

Harder / accepted costs:

- The cleanup norm is informal and relies on the finishing agent remembering; if drift turns out to be worse than the one observed instance, a scheduled sweep is the escalation path, not adopted now.
- The promotion signal is a judgment call, not a mechanical trigger, so it depends on someone noticing recurrence rather than firing automatically.

---

Relevant Notes:

- [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — motivation: names the fork this substrate resolves in the accumulating direction, and the costs (no learning, no testing, no review, no reuse) `scripts/` avoids by existing
- [Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) — mechanism: the promotion signal adopted here is spec mining's general trigger applied to individual scripts rather than system behavior
- [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — rationale: why the promotion signal is stabilization-across-uses rather than a first-use or fixed-count trigger
- [014-scripts as Python package, one-tree model](./014-scripts-as-python-package-one-tree-model.md) — precedent: the one documented promotion event from `scripts/` to the installed package, at the subsystem scale
