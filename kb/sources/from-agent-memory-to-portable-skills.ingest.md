---
description: "Neo4j presents NAMS as a provenance-linked trace-to-skill pipeline; it supports lifecycle design comparisons but not independent outcome evidence."
source: https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills/
captured: "2026-08-29"
capture: trafilatura
capture_scope: full-source
genre: tool-announcement
snapshot_sha256: 59aafb3089f5472138b3eb4ca4b326450b3be79fc81503ffdcf3ba36923585fa
ingested: "2026-08-29"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, skill-distillation, provenance, lifecycle-governance]
---

# Ingest: From Agent Memory to Portable Skills

## Classification

This is a vendor tool announcement with a detailed account of the announced architecture and lifecycle, not an independent evaluation or an inspected implementation. Author: Jocelyn Hoppa is identified as a Senior Product Manager, which signals access to product design intentions alongside a vendor interest in the framing.

## Summary

Neo4j presents NAMS as a pipeline that turns a scoped slice of messages, ontology-backed knowledge, reasoning traces, and tool-call outcomes into a portable skill graph. It says topology is derived deterministically, an LLM writes only source-linked claims and annotations, automated gates can withhold the artifact, and a human must approve it before publication. The same graph lineage is then used to detect status drift and re-ground one affected step or demand full re-distillation. The account is useful for comparing trace promotion and maintenance designs, but its performance figures come from the separate AIP work and do not independently validate the NAMS implementation.

## Quotes

No source quotes have been retained yet.

## Connections Found

The article's strongest role is a vendor-described implementation example for [trace-extracted memory earning authority after capture](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md), [retaining episodes so distilled rules remain re-derivable](../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md), and [keeping compiled views aligned with their sources](../notes/agent-memory-requirements/keep-compiled-views-aligned.md). Its evidence edges, pending-review state, source-status checks, bounded repair, superseding version, and full-re-distillation fallback make capture, promotion, and maintenance distinct. Step-level re-grounding is also a concrete case of [localized retention paying when change is sparse](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), conditional on the unchanged dependency closure remaining valid.

As a comparison, [Memento-Skills](./memento-skills-let-agents-design-agents.ingest.md) gates skill changes with generated behavioral tests, while [Reason Wide](./reason-wide-not-deep-distilled-skills.ingest.md) reports held-out task effects for distilled skills. NAMS instead foregrounds provenance and source currency. Together they sharpen [effect-based memory evaluation](../notes/agent-memory-requirements/evaluate-memory-by-effects.md): a skill can be grounded and current without evidence that it still improves behavior.

## Extractable Value

1. **Separate provenance, currency, and behavioral-effect checks.** NAMS's grounding edges and promotion gates address where a step came from; status checks and re-grounding address whether its support has changed; the account supplies no NAMS-specific downstream outcome revalidation. This distinction connects three mechanisms that the current KB treats across separate artifacts. [quick-win]
2. **Use episode-backed step granularity as a localized-repair case.** Addressable steps preserve their evidence lineage, and repair escalates to full re-distillation when no support survives. This gives the localized-retention claim a concrete applicability boundary rather than a generic preference for small patches. [just-a-reference]
3. **Treat trace-to-skill generation as staged promotion rather than recall.** Scope resolution, settled-memory snapshotting, pattern consolidation, source-bound synthesis, automated gates, and human approval illustrate how accumulated experience can become behavior-facing authority without making raw capture authoritative. [quick-win]
4. **Audit the effective update space before transferring the reported benchmark result.** The distiller can condition on scoped conversation history, ontology entities, reasoning steps, tool calls, outcomes, observations, and reflections; its LLM can map selected snippets into claims and step annotations. The ontology, scope, extraction process, graph schema, branch vocabulary, deterministic topology rule, thresholds, and review protocol remain fixed outside that update space. The AIP comparison as summarized here varies structured skills against prose, not those fixed choices or the end-to-end NAMS pipeline. [deep-dive]
5. **Seed a lightweight NAMS system review with explicit evidence classes.** The source supports a document-grounded account of the claimed trace-to-skill lifecycle, but implementation behavior and AIP benchmark evidence would need separate treatment. That boundary would make NAMS comparable with existing trace-learning systems without upgrading vendor claims into verified mechanics. [deep-dive]

## Limitations (our opinion)

This is Neo4j's product-side account of NAMS. It supplies no inspected code, independent deployment evidence, failure-rate data, scaling results, or examples that let a reader test whether its grounding, coverage, coherence, privacy, and human-review gates reject the right artifacts. Its reported 53.3% to 67.4% pass-rate change and runtime reduction are attributed to the [AIP paper](https://arxiv.org/abs/2606.04781), so they are evidence about the paper's structured-versus-prose comparison as summarized by Neo4j, not an evaluation of NAMS distillation, provenance, drift detection, or repair.

The fixed decomposition also limits what the claimed improvement can establish. NAMS fixes its ontology, scope boundary, available trace records, script-backed-versus-judgment distinction, graph schema, dependency types, gate thresholds, and fallback rules outside the synthesis model's effective update space. Neither the announcement nor its inherited benchmark comparison tests whether alternatives to those choices would preserve more relevant distinctions, express better procedures, or produce better behavior. The drift example checks a recorded tool-call status; the article does not establish semantic policy-drift detection, downstream behavioral revalidation after repair, retirement behavior, replay, or the long-run validity of unchanged steps.

## Recommended Next Action

Create a lightweight NAMS review under `kb/agent-memory-systems/lightweight/` that separates the vendor-described trace-to-skill lifecycle from AIP benchmark claims and evaluates provenance, source currency, and behavioral-effect checks independently.
