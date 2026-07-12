---
description: "Jaya Gupta frames Palantir-style top-down ontology and workflow-first decision traces as two ways to build LLM-facing world models"
source_snapshot: "palantir-competed-with-snowflake-before-llms.md"
ingested: "2026-07-06"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, trace-derived-learning, ontology, context-engineering]
---

# Ingest: Palantir Ontology vs Decision Traces

Source: [palantir-competed-with-snowflake-before-llms.md](./palantir-competed-with-snowflake-before-llms.md)
Captured: 2026-07-06T18:28:32.161674+00:00
From: https://x.com/JayaGup10/status/2006384049485484145

## Classification

Type: conceptual-essay -- a single-author X post advancing an architectural framing, not an implementation report or evaluated system design.
Domains: agent-memory, trace-derived-learning, ontology, context-engineering
Author: @JayaGup10 — Jaya Gupta, investor at Foundation Capital and co-author of the firm's ["context graphs" thesis](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) that the post extends. The useful signal is the framing of ontology-first versus trace-first memory architecture; the post itself supplies no implementation evidence or evaluation, and the author has an investment thesis riding on the workflow-first side of the comparison.

## Summary

The post argues that pre-LLM enterprise data platforms optimized different surfaces: Snowflake and Databricks around SQL/query throughput, Palantir around an ontology or world model of objects, relationships, properties, and interactions. LLMs make the latter look attractive because models need structured, language-shaped context they can traverse and linearize, not just raw rows. The author then reframes "decision traces" as a workflow-first alternative to Palantir-style platform-first ontology: capture inputs, policies, exception paths, approvals, actions, and outcomes at decision surfaces, then infer the minimal entities and relations from those trajectories over time. The important claim for this KB is that bottom-up decision traces are still an ontology strategy; the ontology is derived from use rather than prescribed upfront.

## Connections Found

Connection discovery found a tight trace-derived memory cluster. The source corroborates [Use Trace-Derived Extraction As Meta-Learning](../notes/agent-memory-requirements/use-trace-derived-extraction.md) because it treats ordinary decision activity as material from which reusable entities and relationships can later be learned. It also supports [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md): the post's distinction between state and legible "why" is exactly the ingress problem of adding handles, provenance, relationships, and scope. [Memory design adds operational axes to artifact analysis](../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) is the best router for the full mechanism because the post touches capture, derivation, activation, and authority at once.

The ontology side connects to [Symbolic context engineering is bounded by symbol availability](../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md): named entities, typed relationships, constraints, and interaction edges are the symbols that make traversal and prompt assembly cheap enough to rely on. The source's "write-time provenance" also belongs under [Lineage](../notes/definitions/lineage.md), while [Trace-derived memory earns authority per operation, not at capture](../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) is a useful caution: captured decision receipts are records, not trusted knowledge, until later verification, distillation, and activation operations earn that authority.

For system comparisons, [Graphiti](../agent-memory-systems/reviews/graphiti.md) is the closest concrete temporal context-graph implementation: it turns episodes into entities, edges, provenance, validity windows, and retrieval surfaces. [Memory Scaling for AI Agents](databricks-memory-scaling-ai-agents.ingest.md) complicates the post's product framing by showing Databricks itself arguing for trace and organizational-memory scaling, so the useful comparison is architectural rather than competitive.

## Extractable Value

1. **Trace-first ontology is still ontology.** The source gives a compact name for a useful distinction: the choice is not ontology versus no ontology, but whether the world model is declared before work starts or inferred from decision trajectories. This can sharpen memory-system discussions that otherwise equate ontology with upfront schema design. [quick-win]

2. **Decision receipts are ingress units.** Inputs referenced, policies, exceptions, approvals, actions, and outcomes are not just audit metadata; they are the handles from which later memory can recover why a state changed. This concretizes the ingress work described by raw-accumulation and lineage notes. [quick-win]

3. **LLM-facing data needs symbols, not only storage.** The post's "language-shaped substrate" maps cleanly onto the KB's symbol-availability claim: entities and typed relationships make context construction cheaper because they expose handles the selector can match, traverse, and linearize. [quick-win]

4. **Write-time provenance can become a world-model construction path.** Capturing traces at commit surfaces is a plausible low-friction alternative to designing the whole ontology first, especially for startups without months of embedded workflow discovery. The risk is that the derived ontology will be only as good as the trace schema, extraction oracle, and review loop. [experiment]

5. **Platform-first coherence tax versus trace-first derivation risk.** The source names a real tradeoff: a prescribed ontology buys coherence and shared semantics after heavy integration work, while a trace-first ontology lowers initial cost but pushes difficulty into noise, conflict resolution, privacy, governance, and evaluation of inferred entities and relations. [deep-dive]

## Claim reliability (fact-check, 2026-07-06)

The post mixes an architectural argument with background claims about the three companies. Web verification of the background claims:

- **"They do not believe they have any competitors" — accurate as a report of Palantir's own rhetoric.** CEO Alex Karp on the Q1 2024 earnings call: "I don't believe we have competitors. So, I don't believe in the U.S. commercial market we have competition. I don't believe in the U.S. government market we have competition," attributing the edge to the ontology, Foundry, and Apollo ([Benzinga](https://www.benzinga.com/news/earnings/24/05/38659067/palantir-ceo-alex-karp-dismisses-rivals-we-have-no-competitors-in-us-commercial-and-government-mark)). Note this is the company's own promotional claim, which the post relays without attribution or skepticism.
- **"Palantir was competing with Snowflake and Databricks" — overstated, and the competitive framing is outdated.** The platforms overlap but sit at different layers, and since March 2025 Palantir and Databricks are strategic product partners: Unity Catalog and Palantir Virtual Tables give zero-copy bidirectional access, with 150+ joint customers including the US DoD, BP, and United Airlines ([Databricks press release](https://www.databricks.com/company/newsroom/press-releases/palantir-and-databricks-announce-strategic-product-partnership), [Palantir partnership page](https://www.palantir.com/partnerships/databricks/)). The companies now position themselves as complementary layers, not rivals.
- **"Snowflake/Databricks optimized for SQL and query throughput" — a dated simplification.** Both now ship semantic layers explicitly aimed at AI agents: Snowflake Semantic Views (entities, metrics, relationships as schema objects powering Cortex Analyst) and Databricks Unity Catalog metric views / business semantics consumed by Genie and agents ([comparison](https://medium.com/@data-guy/the-rise-of-the-semantic-layer-snowflake-semantic-views-vs-databricks-metric-views-ff22f397b12a)). These are thinner than a Foundry-style ontology — metrics and dimensions rather than typed relationships with actions — so the post's contrast survives as a difference in degree, but it presents it as a difference in kind.
- **"Months of use case discovery / embedded-team tax" — describes the classic forward-deployed-engineer model, not Palantir's current pitch.** Since 2023 Palantir's AIP Bootcamps advertise "zero to use case" in one to five days on customer data, with claimed ~75% conversion ([Palantir](https://www.palantir.com/platforms/aip/bootcamp/), [Palantir blog](https://blog.palantir.com/deploying-full-spectrum-ai-in-days-how-aip-bootcamps-work-21829ec8d560)). Full ontology build-out presumably still takes longer, but both of the post's poles now claim fast starts, which weakens the cost asymmetry the post leans on.
- **The ontology characterization itself — accurate.** Foundry's Ontology (objects, typed relationships, actions) is real, central to AIP, and cited by Palantir itself as the moat.

Net: the architectural distinction (prescribed-upfront vs. trace-derived world model) is sound and matches Palantir's actual design. The competitive and cost claims are a mix of relayed company rhetoric and thesis-serving simplification — do not cite this post for Palantir's market position, Snowflake/Databricks capabilities, or integration-cost comparisons.

## Limitations (our opinion)

This is a single X post, so the product claims should not be treated as evidence that Palantir has no competitors or that Snowflake and Databricks lack LLM-facing ontology strategies. The post gives no implementation path, benchmark, customer evidence, or extraction method for learning entities and relationships from decision traces.

The decision-trace framing is promising but under-specified. It does not explain how to prevent noisy traces from becoming false structure, how to handle conflicting decisions, how access controls and deletion propagate into derived memory, or what oracle verifies that the inferred ontology improves action. Those gaps matter because trace-derived memory can look authoritative before it has earned authority.

## Recommended Next Action

Write a note titled "Trace-first ontologies are derived views, not starting schemas" connecting trace-derived extraction, lineage, raw accumulation, symbolic context engineering, and Graphiti. The note should argue that workflow-first decision traces are an ontology strategy whose authority depends on capture quality, derivation policy, review, and activation rather than on upfront schema design alone.
