# Phase 4 — Keep cleanup and empirical follow-up independent

**State:** open; not part of the core semantic/resolver adoption patch.

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
commit them independently from Phases 1–3. Before workshop closure, complete
them or transfer them to a named migration owner.

## Agent navigation follow-up

After exact resolution and canonical heads exist, compare:

- deterministic exact membership records;
- the curated canonical head;
- query-conditioned result pointers or summaries.

Measure exact membership recovery separately from task-relevant discovery.
Record wrong opens, full-artifact reads, tool calls or context cost, task
outcome, and false stopping. Human search and information-foraging literature
motivates this comparison but does not predict its result for LLM agents.

## Gwern-style browsing and maintenance trial

The [tag maintenance and derived browsing
proposal](../../../reference/proposals/tag-maintenance-and-derived-browsing.md)
records the Gwern-derived options: temporary topic groups within one large tag,
suggested additions, removals, splits, and merges for maintainer review, a
record of rejected suggestions, aliases, and tag listings generated inside
other pages. Its first candidate is a bounded comparison on one tag: the
curated head and exact listing against a temporary grouped view, on real
finding, reading, and split tasks, with canonical membership held fixed.

Run it with or after the navigation comparison, since both need the resolver
and canonical heads, and they can share tasks and measurements. The resolver
supplies the exact input set that a grouped view must preserve. Two proposal
constraints carry over: a generated group gains no `complete` promise, and
Gwern's rule that drops a parent tag when a child is present conflicts with
Commonplace's split rule. Letting tag heads carry tags as related-topic links
is not part of this trial. Adopting that would change membership, so it
belongs in the ADR drafted in Phase 1.

Neither trial is a structural closure requirement unless the adopted ADR makes
a retrieval-performance claim. A trial that shows benefit leads to a design
proposal or ADR amendment for the specific surface it supports.
