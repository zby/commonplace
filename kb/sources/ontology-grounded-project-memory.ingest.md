---
description: MOOSEDev reports strong complete-set and lifecycle answers from typed project memory, with relevance parity and unresolved capture and architecture costs.
source: https://arxiv.org/abs/2608.13662v1
captured: "2026-10-30"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d8cb18d5b3961976a89845634a2836864eec8c61441b829d830c254f8c0dc252
ingested: "2026-10-30"
type: types/ingest-report.md
domains: [ontology-grounded memory, coding-agent project memory, structural queries, supersession]
---

# Ingest: Ontology-Grounded Project Memory for Coding Agents

## Classification

A short scientific system paper combining an implemented design, comparative memory benchmarks, deployment observations, and a prospective live-trial protocol. Author: James Adam, affiliated with Trivyn, which supplies the ontology workbench and proprietary MOOSE engine underlying the evaluated system. This is an author evaluation of that system, not an independent replication.

## Summary

MOOSEDev stores decisions, lessons, constraints, rationales, and anti-patterns as typed project records with provenance, lifecycle status, and supersession links. Two small OWL ontologies and SHACL validation support symbolic traversal, filtering, and evidence ranking; models interpret questions and synthesize answers through an MCP interface. On a public CodeGraph documentation corpus captured as 835 graph records versus 553 native Mem0 memories, the paper reports answer scores of 0.98–1.00 for completeness, absence, and supersession tasks, versus 0.06–0.27 for the tested Mem0 configuration. This compares a structured capture-and-query pipeline with ranked retrieval, not ontology representation alone. Simple relevance retrieval is broadly comparable, while complete enumeration can consume substantially more tokens. The paper also reports commit-history bootstrap, benchmark failures caught through audit, and an ongoing trial; reduction of long-term comprehension debt remains unestablished.

## Contribution assessment (our opinion)

The useful contribution appears to be a workload-specific demonstration that finding relevant memories and answering complete relational questions are different capabilities. Content-flattened BM25 comparisons strengthen the case that content availability alone does not explain the reported advantage, and the disclosed grading and tool-path failures make the evaluation more criticizable. The evidence supports the implemented pipeline's usefulness on these tasks more strongly than the claim that formal ontologies justify their complexity: capture, representation, query operators, and lifecycle handling change together. Broader significance depends on whether comparable results require this machinery rather than simpler typed records with explicit queries, and whether capture costs are repaid in sustained use. Originality beyond the paper's comparisons is uncertain.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source supplies a bounded empirical case for [access burden and transformation burden as distinct query dimensions](../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): comparable relevance coverage coexists with sharply different complete-set and relational answers. The case concerns available operators over captured records, not proof that graph storage or OWL reasoning uniquely reduces either burden. Its concrete contribution is to make answer semantics—ranked relevance versus complete enumeration, absence, or traversal—part of architecture comparison.

Separately, it illustrates [why final task success does not establish intended-path health](../theory/final-task-success-does-not-establish-intended-path-health.md). A failed memory server led agents to grep raw storage, initially masquerading as a relevance loss. That reported incident supports verifying which tool path ran; it is not evidence about the prevalence of silent fallback. These are distinct contributions: benchmark observability should not be treated as a premise establishing graph superiority.

## Extractable Value

1. **Compare answer operators, not just memory substrates.** Test top-k retrieval against explicit filtering, enumeration, and traversal over the same typed records and lifecycle state. The reported structured-pipeline advantage motivates this comparison but does not isolate ontology reasoning from capture and query access. This could sharpen the existing access/transformation distinction without adding a generic graph-memory claim. [experiment]
2. **Verify the evaluated tool path.** The server-outage/raw-grep incident provides a concrete example for the intended-path-health note. Immutable transcripts, re-grading, and evidence that the memory tool actually fired are reusable safeguards against attributing fallback behavior to the named system. [quick-win]
3. **Keep historical capture separate from rationale truth.** Commit-by-commit bootstrap reportedly recovered seven supersession chains, but a misleading commit message contaminated both a bootstrapped rationale and a gold answer. History can supply candidate relationships without independently validating the reasons assigned to them. This is a context-bound capture warning, not a measured bootstrap error rate. [just-a-reference]

## Limitations (our opinion)

The central comparison bundles typed capture, validation, lifecycle metadata, symbolic queries, and retrieval policy. Flattening graph content into BM25 helps test a content-only explanation, but does not compare OWL against otherwise equivalent relational tables or typed Markdown with exhaustive query operators. The paper therefore does not establish that a formal ontology or graph database is necessary, nor that every Mem0 configuration lacks structural query capabilities.

The corpus representations differ in record count and native extraction method. The author reports faithful ingestion, but this ingest has not inspected the benchmark repository, proprietary engine, per-item ground truth, or transcripts, and has executed no implementation or benchmark code. Ground truth partly derived from SPARQL sets and an LLM judge make answer-set construction and grading consequential; repeated judging and released artifacts enable scrutiny but do not substitute for independent checking. Generality is limited by the selected corpora and one coding-agent model family.

Absence means absence of a recorded relation in the captured corpus, not proof that a real-world rationale or constraint never existed. Current-guidance filtering works only when lifecycle capture is correct. Mem0 tied the graph on the tested reversal, so currency results do not establish a universal graph advantage. Completeness also has an output cost: the paper reports 78k–167k agent tokens for a 122-item SPARQL answer versus roughly 35k for targeted retrieval. Similar relevance costs should not be generalized to enumeration.

The live trial's early 71 assists and 38 misses are author-reported process observations, not the registered monthly trend or a demonstration of reduced comprehension debt. Capture friction, thin historical records, and host discretion over passive MCP calls remain adoption constraints. Benefits for small local models, automatic code-touch injection, and edit gating are proposed directions, not tested outcomes.

## Recommended Next Action

Design a focused comparison for the existing access/transformation note using one lifecycle-annotated corpus and matched answer semantics to compare top-k retrieval with explicit enumeration and traversal, without changing the captured records between conditions.
