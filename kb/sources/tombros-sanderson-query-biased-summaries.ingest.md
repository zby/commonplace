---
description: "A controlled human study finds query-biased result summaries improve relevance judgments and reduce full-text consultation, supporting query-specific pointer design while limiting the speed claim."
source: https://ciir.cs.umass.edu/pubfiles/ir-130.pdf
captured: "2026-08-26"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: 19c22c213a4c44e8bb75f12811624b08425398fa9de577e05ef341818cd16e65
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [information-retrieval, context-engineering, evaluation]
---

# Ingest: Advantages of Query Biased Summaries in Information Retrieval

## Classification

This is a scientific paper reporting a controlled, task-based evaluation of an extractive summarization system. Authors Anastasios Tombros of the University of Glasgow and Mark Sanderson of the UMass Center for Intelligent Information Retrieval supply relevant academic information-retrieval expertise; their affiliations are expertise signals rather than independent confirmation of the results.

## Summary

The paper compares query-biased extractive summaries with static title-and-leading-sentence surrogates in a timed relevance-judgment task using Wall Street Journal documents and TREC queries. Two independently assigned groups of ten participants each judged retrieved documents under one condition. The query-biased group achieved higher mean recall (65.6% versus 49.76%) and precision (55.32% versus 44.29%), examined 22.62 rather than 20 documents per query, and opened full text for 1.32% rather than 23.7% of examined documents. An appendix reports a same-length rerun of the static condition: the accuracy and full-text-access differences remained, but that group examined 23.24 documents per query, removing the claimed speed advantage. For Commonplace, the durable result is bounded human-task evidence that a query-conditioned result pointer can improve selection accuracy and reduce source-opening demand; it is not evidence that the same effect transfers unchanged to LLM agents.

## Quotes

- **Source extract (verbatim):** Experimental conditions. We are interested in two levels of
  an independent variable in our experimental design: the use of
  query-biased summaries in a ranked list of retrieved
  documents; and the use of static pre-defined summaries (the
  title and first few lines of a document) in such a list. In this
  way, the design comprises two tasks that a group of subjects
  will have to perform: to judge the relevance of the documents
  in a ranked list, with either query biased or predefined
  summaries.
  - **Source location:** Section 3.1, “Design considerations,” paper p. 4 (PDF p. 4)
- **Source extract (verbatim):** Therefore, we conclude that subjects using query biased
  summaries in a retrieved document list, performed their
  relevance judgements significantly better than those using the
  classic IR standard: the title and first few lines of a document.
  In essence this means that query biased summaries allow
  users to identify more relevant documents, and identify them
  more accurately.
  - **Source location:** Section 4.1, “Recall and Precision,” paper p. 7 (PDF p. 6)
- **Source extract (verbatim):** The new results show that the accuracy of the judgements
  and the opinion of the users about the system were not
  significantly affected by the amount of text shown. The
  number of times that users had to refer to the full text of the
  documents was decreased (by approximately 8%), but it still
  remained significantly higher than the other group’s figure
  (14.42% higher). Finally, users examined more documents per
  query with the new settings (3.24 more documents on
  average), but just 0.62 documents more than the group using
  the summaries.
  Based on the new results, we can conclude that the amount
  of text shown was not a significant factor, and that the
  difference in performance in the two experimental groups can
  be attributed to the presence of the query biased summaries in
  the retrieved document list.
  - **Source location:** Appendix, paper p. 10 (PDF p. 9)

## Connections Found

The paper is a technical basis for the query-specificity branch of [pointer design tradeoffs in progressive disclosure](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md): it directly compares a query-conditioned surrogate with a fixed one and measures downstream human choices. It is also bounded evidence for [link-following and search imposing different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md), because decision-relevant context on a long-range result surface reduced mistaken selections and full-document consultation. Compared with [The Perfect Search Engine Is Not Enough](./teevan-perfect-search-engine-orienteering.ingest.md), this study isolates pointer presentation after direct retrieval rather than the choice between direct jumps and local navigation; it therefore informs pointer quality, not route preference.

## Extractable Value

1. **Query specificity has controlled human-task support.** The measured contrast provides bounded evidence that tailoring a result surrogate to the active query can improve relevance-judgment recall and precision relative to a fixed title-and-lead surrogate. [quick-win]
2. **Summary quality can be evaluated through the decision it is meant to support.** The study measures judgment accuracy, documents examined, full-text openings, and user ratings instead of relying only on similarity to a human-written summary; this supplies a reusable evaluation pattern for KB pointer experiments. [experiment]
3. **Full-source consultation is a useful pointer-cost signal.** The large difference in full-text opening rates operationalizes whether a surrogate carries enough context for a preliminary selection decision, while leaving final-answer reliability untested. [experiment]
4. **The matched-length rerun narrows the headline claim.** Accuracy and reduced full-text consultation persisted when display length was equalized, but the original speed advantage did not, so the paper should support selection quality and access reduction rather than a general speed claim. [quick-win]
5. **The intervention leaves its decomposition fixed.** The system can condition sentence scores on query terms, document structure, term clusters, and document length, and can respond only by selecting source sentences under a fixed scoring and length rule. It has no run-time learner or history-dependent update, and the experiment does not compare alternative representations, response bases, or mappings. [deep-dive]

## Limitations (our opinion)

The evidence comes from twenty mainly postgraduate conversion-course students, one 1990s news collection, TREC relevance assessments, and a five-minute screening task. That narrow population and task do not establish effects for other genres, open-ended synthesis, modern retrieval interfaces, or LLM agents. The paper reports significance at an error probability of 0.05 but does not provide the variance, test statistics, confidence intervals, or per-query distribution needed to assess robustness from this snapshot.

The intervention is also a compound fixed design. Available signals are query-term occurrence, titles, headings, sentence position, term-frequency clusters, and document length; the only output operation is extractive sentence selection under a fixed additive scoring procedure and length cap. There is no learner improving within an update space. The main contrast therefore supports the complete query-biased surrogate against the chosen static baseline, not the necessity or relative contribution of any component. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains, success within fixed representational and operational choices does not validate alternatives excluded by those choices. The appendix varies display length only; it addresses that confound but does not isolate query bias from the other differences between the two surrogate generators.

## Recommended Next Action

Update [pointer design tradeoffs in progressive disclosure](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) to cite this ingest as bounded human-task evidence for query-specific pointers, preserving the same-length rerun's limit on the speed claim and explicitly withholding transfer to LLM-agent behavior.
