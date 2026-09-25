# Phase 5 — Keep metadata cleanup independent

**State:** open; not part of the core semantic/resolver adoption patch. If
Phase 2 reduces tags to search keywords, this cleanup still applies.

## Trace-learning and source-family cleanup

Retain `trace-learning` as a substantive navigation facet and the source for
the systems-matrix Boolean. Keep the review schema, type, template, writing
skill, and tests in parity with the `### Trace-learning` subsection. Correct
the stale `trace-derived` conditional spelling when that packet runs.

Separately remove redundant `x-*`, `github-issue`, and `github-pr` source-family
tags and stop snapshot producers from emitting them. Their platform/container
classification already belongs to source metadata. Derive current inventories
at execution time.

These changes are useful but do not prove tag-scope consistency. Review and
commit them independently from Phases 1–4. Before workshop closure, complete
them or transfer them to a named migration owner.

## Deferred maintenance options

The navigation comparison and the Gwern-style browsing trial moved into the
[Phase 2 finding trial](./02-finding-trial.md). The proposal's maintenance
options (suggested additions, removals, splits, and merges; a record of
rejected suggestions; aliases) stay deferred. They address the cost of
assigning tags, which the operator did not report as the problem. Reconsider
them only if Phase 2 keeps tags and maintaining them then becomes the
bottleneck.
