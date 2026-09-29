---
type: agentic-systems/types/generated-review.md
description: "PageIndex retains document trees and pages for model-driven retrieval, with local scope enforcement, bounded index correction and opaque cloud internals"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-28-pageindex-01
source-identity: https://github.com/VectifyAI/PageIndex
reviewed-revision: "619cbd89f6dd02681a8cfc5d00b1f9b4848e973e"
analysis-artifact: kb/reports/retained/agentic-system-analysis/AAS-2026-09-28-pageindex-01/ARTIFACT.yaml
analysis-artifact-sha256: "cbaecd4cc060bc9614a39e0e209ef072c46c063efc0130671686bb71f285006e"
---

# PageIndex

Evidence basis: source code and repository contracts inspected on 2026-09-28 at [commit 619cbd89f6dd02681a8cfc5d00b1f9b4848e973e](https://github.com/VectifyAI/PageIndex/tree/619cbd89f6dd02681a8cfc5d00b1f9b4848e973e). No live model/service run or independent benchmark reproduction. The [retained overview](../../reports/retained/agentic-system-analysis/AAS-2026-09-28-pageindex-01/overview.md) fixes the boundary and source register.

PageIndex is a document indexing and QA SDK with a built-in model/tool loop and adapters for external agents. Local submission saves extracted pages separately from a hierarchical index and document metadata. Flash starts with layout/bookmark extraction and can add model refinement and summaries; standard indexing uses models to construct and check section locations. The stored index is reusable context for later questions, rather than demonstrated learning from prior agent experience (OBJ-3, RTE-5).

Standard indexing has a bounded correction mechanism: a title/page assertion selects a source check, a negative verdict can trigger location repair, and the corrected map plus remaining errors feed another round. Under the narrow factual-map interpretation, all four theory-builder conditions and computational autonomy are wired. The loop does not revise its own method; model explanations are discarded from returned check records, and repair exhaustion can still return an index with errors. This establishes candidate correction, not improved future answer capacity (RTE-5).

A separate optimizer can refine an already saved tree. It filters proposed headings and selects structure using a fixed page-search-cost proxy, then writes an output artifact. That supports retained-index maintenance, but neither proxy improvement nor saving the file demonstrates better QA or automatic installation into the SDK store (RTE-6).

For a question, PageIndex supplies guidance and document tools to an OpenAI or Anthropic SDK runner. The model pulls requested outlines/pages; local catalog discovery is time-ordered, with the model comparing names and descriptions. Chat also automatically pushes retained metadata selected by caller document/folder IDs. Those are distinct context-selection paths. A nominal response character budget is soft for an oversized first page (RTE-1, RTE-8, RTE-9).

Local built-in chat enforces document scope through a tool-layer ID allowlist. Cloud own-model chat uses prompt targeting instead, and external hosts own their broader permissions. Reading and citation instructions are model policy, not answer-truth checks. Cloud tool schemas, instructions and native payloads come from a service whose internals are outside this analysis; source-local guarantees do not transfer to it (RTE-2, RTE-3, RTE-4, RTE-11, BAP-1, BAP-2).

Conversation continuation depends on the caller returning raw history or native transcript items. No automatic local trace-to-derived durable memory route was found in the inspected paths; hosted opacity prevents a whole-system negative. Recall dependence, semantic faithfulness, general self-improvement and the README's benchmark advantages remain unestablished by this source-only pass (RTE-10, ABS-1, ABS-2, CLM-2).

The [runtime member](../../reports/retained/agentic-system-analysis/AAS-2026-09-28-pageindex-01/runtime.md) details protocol alternatives and forcing cases; the [memory member](../../reports/retained/agentic-system-analysis/AAS-2026-09-28-pageindex-01/memory.md) carries the comparison profile; the [epistemic member](../../reports/retained/agentic-system-analysis/AAS-2026-09-28-pageindex-01/epistemic.md) separates structural checks, operational admission and claim warrant. Retention and source citations make material available and traceable; they do not by themselves establish truth or acceptance of new knowledge.
