---
description: "Proposal: determine when validation needs general change-driven target selection rather than explicit selectors, with old/new state and conservative fallback as adoption conditions."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Generalized validation invalidation

This proposal asks when Commonplace should generalize the selection of artifacts
that need revalidation after a change. It does not decide how checks execute.
[Type-selected Python validation checks](./type-selected-python-validation-checks.md)
addresses executable extensions; [document validation in working-set context](./type-declared-cross-checks-and-one-validation-surface.md)
separates the document being checked from the related artifacts used as context.

## Current state (as of 2026-10-06)

- [ADR 050](../adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md)
  established a shared validation context and explicit impacted-tag-head
  selection, without a general inverse dependency graph.
- In `src/commonplace/lib/validation.py`,
  `ValidationRun.impacted_marked_tag_readmes()` selects marked heads from the
  current tags of supplied participating artifacts. `evaluate()` adds those
  heads to its targets. The selector does not reconstruct removed tags or the
  contents of deleted artifacts.
- [Directory validation](../validation-contract.md#directory-artifacts) checks
  a manifest and its direct Markdown members together. Explicit member-file
  validation does not automatically validate the containing directory. This is
  an evaluation boundary, not change-triggered invalidation.
- `ValidationRun` caches bytes, parsed artifacts and results within one run.
  These evaluation caches do not supply a persistent old/new dependency model.

## Problem

An explicit validation target can pass while a related artifact now needs
rechecking. A changed member can invalidate a containing set; a changed type or
schema can affect many instances. Selecting those targets is separate from
checking them once selected.

The files a check reads do not necessarily identify the smallest change that
can alter its result. A tag-head check may read a whole collection index while
only membership changes matter. Conversely, inspecting only current state can
miss a removed tag, deleted target or previous referent.

The question is whether recurring selection needs justify shared machinery,
not whether the validator has cross-artifact dependencies at all.

## Options

### A. Add explicit selectors where concrete consumers need them

Keep each impact rule specific to its relation, following the existing
marked-tag-head selector. A member-to-container selector or a type-to-instance
selector could join the same target expansion path without a general language.

The validation target resolver or run would consume the selector's output and
validate the added artifacts through the ordinary pipeline. Its selection
oracle would be the relevant manifest, type identity or membership relation.
It would establish candidate impact, not that an artifact is invalid.

This keeps individual rules inspectable. Overlapping selectors may eventually
repeat change handling, especially deletion and previous-state recovery.

### B. Generalize impact selection after unlike selectors expose shared needs

Introduce a shared model of dependency identity and change, including previous
state where a current graph loses the affected relation. The implementation
could be Python APIs rather than a KB-authored declaration language; the
representation remains open.

The validation target resolver would consume change information and dependency
relations to produce the revalidation set. Adoption would need a reliable
source for those relations and for the old state, or a declared conservative
fallback when either is unavailable. A selected dependency is grounds to rerun
a check, not grounds to reuse a verdict or infer semantic support.

This could unify repeated selection work. It also introduces persistence or
reconstruction costs, versioning questions and missing-history behavior.

### C. Prefer conservative broader validation

When precise impact is expensive or uncertain, validate the enclosing artifact,
collection or other explicitly bounded scope instead of constructing an inverse
graph. Existing validation callers can choose wider targets; a proposed
change-driven caller would map uncertain impact to that fallback scope.

The oracle is the known scope's membership and the checks performed over it.
The claim stops at that scope: a collection sweep does not establish that no
external consumer was affected. This option trades extra work for simpler
selection and may remain cheaper at the KB's actual scale.

## Forces and boundaries

- Selection must account for removed as well as added relations. Current-state
  inspection alone cannot establish complete impact after deletion.
- False-positive selection costs work; false-negative selection can leave a
  stale result appearing current. Conservative fallback is preferable to a
  false completeness claim.
- Check execution, target selection and semantic review freshness are distinct
  mechanisms. Adding Python checkers does not require generic invalidation,
  and generic invalidation does not automatically solve review freshness.
- Declared input reads may support conservative selection without supporting
  precise inverse selection. No precision claim should exceed the recorded
  dependency and change information.

## Free choices

The representation of dependencies, the source of previous state, persistence
versus reconstruction, and the granularity of fallback remain open. The choice
between an explicit selector and shared machinery should follow measured work
and missed-impact cases, not the availability of a graph abstraction.

## Adoption criteria

Adopt a new explicit selector when a concrete consumer repeatedly misses or
manually supplies the same affected targets, and the relation has an inspectable
oracle. Keep broader validation when its measured cost is acceptable.

Consider generalization only after at least two unlike selectors demonstrate
shared change-handling needs. A candidate must handle old/new state, deletions,
path-existence changes and type/schema dependencies, or explicitly fall back to
a bounded broader check. Compare total work and missed impacts against the
explicit-selector and broad-validation alternatives before choosing it.

No general invalidation engine is adopted by this proposal.
