---
description: "APEX-MEM preserves temporal conversational facts and resolves them at retrieval time; tool ablations support hybrid access, not append-only superiority."
source: https://arxiv.org/abs/2604.14362
captured: "2026-10-18"
capture: pdftotext
capture_scope: full-source
doi: "10.48550/arXiv.2604.14362"
genre: scientific-paper
snapshot_sha256: e7797566f6eabfca88cdc2b51def7351ba824b6718044a51cc86328c03dab317
ingested: "2026-10-18"
type: types/ingest-report.md
learning_claims: true
domains: [agent-memory, temporal-reasoning, context-engineering, evaluation]
---

# Ingest: APEX-MEM — Temporal Graph Memory and Retrieval-Time Resolution

## Classification

A scientific preprint presenting a conversational-memory architecture, benchmark comparisons, tool ablations, and qualitative cases. Author signal: Pratyay Banerjee, Masud Moshtaghi, Shivashankar Subramanian, Amita Misra, and Ankit Chadha list Amazon AGI affiliations. Institutional affiliation does not independently validate the results; the retained source is arXiv v1.

## Summary

APEX-MEM converts conversations into a property graph of canonical entities, events, typed facts, validity intervals, and utterance evidence. It appends evolving assertions rather than selecting a single current value during storage, then uses a ReAct agent with schema guidance, entity lookup, read-only SQLite queries, and hybrid search to select and interpret relevant history. The paper reports 88.88% LOCOMO accuracy with GPT5, though Table 1 identifies that figure as excluding adversarial questions, and 86.2% on LongMemEval with Claude 4.5 Sonnet. LOCOMO graphs cover all conversation sessions; LongMemEval and SealQA graphs are constructed from question-relevant documents. Within the fixed graph/extraction architecture, the Haiku tool ablation raises overall accuracy from 79.45% to 87.00% when Search is added to schema inspection, entity lookup, and GraphSQL, but lowers temporal accuracy from 82.29% to 79.17%. These results support complementary retrieval tools in this configuration; they do not isolate append-only storage or establish the graph decomposition's superiority over matched alternatives.

## Contribution assessment (our opinion)

Reliable reasoning over changing conversational facts is an important problem, and the combination of evidence-linked temporal assertions with flexible retrieval offers a credible engineering contribution. The most informative test is the within-system tool comparison: it exposes both an overall gain and a temporal trade-off rather than merely reporting a winning aggregate score. The broader benchmark results suggest usefulness of the compound system, but mixed baseline provenance and internal reporting inconsistencies weaken precise ranking and efficiency claims. Without a matched storage-policy intervention, the central explanation that postponing resolution prevents harmful information loss remains plausible rather than causally established. Originality relative to the full temporal-memory literature is unresolved by this reading; the demonstrated contribution is integration and evaluation, not proof that temporal history preservation is new.

## Quotes

No source quotes have been retained yet.

## Connections Found

APEX-MEM is a concrete design case for [preserving evidence without making history the next context](../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md): event/fact history and supporting utterances remain stored while the reader selects query-relevant context. This supports the feasibility of separating retention from activation, not exhaustive capture fidelity or a causal benefit from append-only storage.

Its strongest empirical connection is to [access burden and transformation burden](../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md). Entity lookup and hybrid search locate useful evidence; SQL can join relations, aggregate values, and calculate durations. Within the same graph and extraction pipeline, adding GraphSQL to schema inspection and entity lookup raises Haiku temporal accuracy from 72.92% to 82.29%; adding Search then raises overall accuracy from 79.45% to 87.00% while temporal accuracy falls to 79.17%. The tools overlap in function, so this is a bounded illustration of the distinction, not an experiment isolating the two abstract burdens.

## Learning Claims (our opinion)

The adaptation mechanism is external-memory accumulation and query-conditioned interpretation, not reported weight training. New turns are extracted into evidence-linked assertions; the reader can compare earlier and later statements to answer about changing preferences or historical state. Online construction additionally selects documents using the current question. Learned retrieval policies and automated ontology refinement are proposed future work, not evaluated mechanisms.

Against the [theory-builder](../theory/definitions/theory-builder.md) conditions, **localized content** is strongly supported at the design-description level: facts have identifiable subjects, properties, values, dates, and evidence. These give fine-grained targets resembling the structural property of an [addressable theory](../theory/definitions/addressable-theory.md), but identifying an assertion does not establish that the system repairs it. **Consumption** is supported by the described query path and reported QA outcomes: fact content and temporal ordering guide answers. **Content-directed criticism** is only partly supported: the reader resolves evolving claims, and the appendix describes SQL-error diagnosis, but a later preference is not a refutation of an earlier time-indexed preference. The paper does not demonstrate systematic criticism of stored factual errors. **Iteration** is supported within a query by tool outputs and SQL-failure recovery informing subsequent calls; it is not established as a continuing cycle of retained factual criticism and revision across queries.

The graph persists conversational evidence across sessions, but persistence of a learned testing record or improved policy is not shown. Aggregate QA advantages over baselines demonstrate useful memory-assisted performance, not longitudinal improvement from the system's own criticism. The ontology, extraction schema, canonicalization pipeline, and tool interfaces remain externally supplied. As in [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improved behavior within those boundaries does not validate the boundaries themselves. The missing restaurant-to-location relation in the failure case illustrates dependence on extraction and linking; it does not prove an irrecoverable information omission, because evidence and source turns may still permit recovery. The source therefore supports a storage-and-consumption mechanism more strongly than a persistent theory-revision or autonomous learning claim.

## Extractable Value

1. **Hybrid access can trade aggregate gains against specialized reasoning.** Under the fixed graph/extraction pipeline and Haiku reader, adding Search improves overall LOCOMO accuracy by 7.55 percentage points while reducing temporal accuracy by 3.12 points. This supplies a concrete, non-monotonic case for the access/transformation note; retain the tested tool bundles rather than a general claim that more tools improve every capability. [quick-win]
2. **Keep historical evidence separate from current-answer selection.** Event-linked assertions and utterance evidence provide a reusable implementation pattern for the existing preservation requirement. The broad design insight is retention without default loading; the source does not establish that preserving all extracted assertions is always preferable to ingestion-time lifecycle decisions. [just-a-reference]
3. **Test storage policy with acquisition and retrieval held constant.** Appendix F compares different systems rather than intervening on append-only versus eager updates within APEX-MEM. A matched test should include lasting changes, temporary exceptions, historical queries, and retractions of false claims; otherwise a gain in current-state selection can conceal loss of historical or epistemic distinctions. This is a proposed test, not a paper result. [experiment]

## Limitations (our opinion)

**Storage-policy causality is untested.** Appendix F explicitly supplies indirect cross-system comparisons. Models, extraction, representations, and readers differ, so temporal-score gaps cannot be assigned to append-only storage. The tool ablation varies access to tools while retaining the graph architecture; it does not compare alternative ontologies or establish that deferred resolution is preferable to explicit ingestion-time invalidation with retained history.

**The reported evaluation boundaries differ.** Question-conditioned online construction for LongMemEval and SealQA combines relevance filtering, extraction, and answering. Its score is not evidence for a single complete question-independent memory store. Reported baseline numbers and reimplementations also have different provenance. LLM-as-judge means over three trials do not establish robustness to extraction errors, production workloads, or alternative judging criteria. No implementation was inspected or executed for this ingest, and none of the outcomes were independently reproduced.

**Several numerical claims need reconciliation.** LOCOMO prose calls 88.88% overall although Table 1 labels it as excluding adversarial questions. SealQA prose presents O3 at 34.6% as the strongest baseline, while Table 5 includes GPT5 at 38.6% against APEX-MEM's approximately 40.1%; the claimed 5.55-point margin is therefore not the margin against the strongest listed baseline. Table 9 gives approximately 30,000 tokens per query, while Table 10 totals 81,604 with the same 13,557-token amortized construction entry. Estimated competitor costs and unreconciled denominators prevent a reliable efficiency ranking. Some Table 11 execution, success, and error totals also fail to reconcile, limiting quantitative reuse of the recovery analysis.

**Preservation does not settle interpretation.** Canonicalization, inferred properties, validity intervals, and query-time selections can be wrong. The restaurant/location failure case shows that retaining assertions does not ensure that a required relationship was extracted. A change in a person's preference, a temporary exception, and withdrawal of a false claim require different reasoning; selecting the latest timestamp is not a general truth-maintenance rule. Current evidence concerns text QA, not durable revision of KB methodology, deletion/redaction governance, or non-QA behavioral improvement.

## Recommended Next Action

Update [Access burden and transformation burden are distinct query dimensions](../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) with one bounded APEX-MEM tool-ablation case, keeping the fixed graph/extraction setup, opposing overall and temporal effects, and an ingest citation marked `(snapshot required)` for verification.
