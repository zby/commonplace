---
description: "PostHog's human-governed SQL semantic catalogue operationalizes authority, drift detection, and agent-uptake evaluation, but reports design rather than outcomes"
source: https://x.com/posthog/status/2090858894419693598
captured: "2026-08-22T07:54:34.187816+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: e1273f268f019ebe4144bcad54c824bab3e83dd7924dafc253c83ff95c31dc4e
status_id: 2090858894419693598
conversation_id: 2090858894419693598
post_count: 1
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, agent-memory, data-governance, lineage]
---

# Ingest: Building a semantic layer at PostHog

## Classification

A first-party account by the PostHog team members who built and launched a beta feature, centered on concrete architecture and rejected design alternatives rather than independent evaluation.
Authors: Lizzie Epton (Developer Marketer) and Thiago Rocha Salvatore (Product Engineer), published by PostHog. Their product access gives the account implementation value, while the vendor and launch context creates an incentive to foreground benefits and omit failures.

## Summary

PostHog argues that agents produce inconsistent business answers when metric meanings, canonical tables, and joins remain tribal knowledge. Its semantic layer records those commitments in a SQL-readable catalogue over existing data rather than copying the data or requiring a separate catalogue API. Agents may propose metrics, tables, and joins, but only humans can approve them; editing an approved definition revokes approval, and an insight-backed metric is marked drifted when its stored query snapshot diverges from the source insight. The catalogue therefore gives consumers a simple canonicality rule—approved and not drifted—while preserving native execution paths for SQL-, Markdown-, and insight-shaped metrics. The article closes with planned measures of answer accuracy, governed-metric uptake, and catalogue growth, but reports no results.

## Claims

No claims have been grounded yet.

## Connections Found

This source is a concrete implementation witness for [Make Authority Explicit](../notes/agent-memory-requirements/make-authority-explicit.md) and [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md): agent output remains proposed, human approval grants authority, edits revoke it, and an insight-derived definition retains enough lineage to expose divergence. Its opening case also supports the distinction in [Parametric reproduction alone cannot replace an authoritative record](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): several agents can generate plausible metric logic without any generated answer thereby becoming the operative definition.

The proposed measurements rest on [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) and [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), because PostHog separates catalogue growth, answer correctness, and whether agents actually use an approved metric. Architecturally, the source supplies a deliberately thin, prescribed counterpart to the broader ontology and trace-inference alternatives in [Palantir Ontology vs Decision Traces](./palantir-ontology-vs-decision-traces.ingest.md). Its accepted-query snapshot and live drift check also compare with Commonplace's more general [freshness architecture](../reference/freshness-architecture.md), without implying shared lineage between the systems.

## Extractable Value

1. **Preserve a governed definition in its native executable representation.** PostHog stores an insight-shaped metric as the same query shape the dashboard engine executes instead of translating it into hand-written SQL. This makes semantic equivalence a construction property rather than a claim that must be rechecked after every translation. [quick-win]

2. **Make canonicality a machine-readable conjunction of authority and freshness.** The consumer rule `status = 'approved' and is_drifted = false` turns two separate governance questions—who accepted the definition and whether its lineage still matches—into a cheap runtime check. This concretizes the KB's existing authority and compiled-view requirements. [quick-win]

3. **Expose governance through an action vocabulary agents already possess.** Storing the catalogue as ordinary SQL tables lets any agent with `execute-sql` discover definitions without learning a bespoke API. This is a context-bound but reusable integration pattern: place new semantics behind an existing, strongly typed access path when the path preserves the needed authority distinctions. [quick-win]

4. **Separate answer quality, behavioral uptake, and maintenance health in evaluation.** Golden-question accuracy asks whether answers improve; approved-metric use asks whether the intended knowledge path activated; continued catalogue growth asks whether the maintenance workflow remains alive. The separation is stronger than a single “semantic layer works” score, but it remains an evaluation plan rather than reported evidence. [experiment]

5. **Use agent generation for candidate throughput without granting it canonical authority.** Schema inspection can cheaply propose metric definitions, trusted tables, and joins, while human promotion remains a separate operation. The source adds a concrete data-governance instance to an authority pattern already present in the KB. [just-a-reference]

## Limitations (our opinion)

This is a first-party beta account with no benchmark results, adoption data, error analysis, or independent verification. The opening comparison among Claude, Cursor, and PostHog AI does not hold prompts, tool access, schema visibility, source tables, or query procedures constant. It establishes disagreement, not that missing semantic governance was the sole cause or that the proposed layer produces correct answers. A shared definition can make every agent consistently wrong when human approval, source data, or the definition itself is wrong.

The planned evaluation operates inside a fixed decomposition. Agents can condition on the catalogue, schema, and available data; they can choose whether to use an approved metric and execute the supplied SQL-, Markdown-, or insight-shaped operations. The approved metric forms, human promotion workflow, agent interfaces, golden questions, and catalogue representation remain outside the effective update space. Improvement on that test would support the compound PostHog configuration, not establish that these fixed choices are necessary or preferable to rival semantic-layer designs.

The governance account also leaves important boundaries unspecified: how approvers verify a metric, resolve conflicts, manage permissions, or keep review throughput ahead of agent proposals; whether upstream table, view, join, or business-meaning changes invalidate every affected definition; and whether agents reliably check the catalogue before answering. The stated claim that one definition yields the same number every time therefore depends on data currentness, drift coverage, execution determinism, and behavioral uptake that the article does not demonstrate.

## Recommended Next Action

Create a doc-grounded lightweight review at `kb/agent-memory-systems/lightweight/posthog-semantic-layer.md`, using this snapshot as first-party evidence and explicitly marking outcome evidence as absent; compare its SQL catalogue, pull-based read path, proposal/approval authority, lineage checks, and evaluation plan on the collection's standard context-engineering axes.
