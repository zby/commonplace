---
type: types/note.md
description: "Compare how Hermes, A-MEM, Hindsight and Basic Memory select retained material and deliver it to a later consumer, without equating delivery with use."
traits: [has-comparison, synthesis]
---

# How memory reaches the next decision

## Research question and scope

A memory store can contain the right information without supplying it to the process that needs it. This comparison asks: **what selects retained material, which representation crosses into a later consumer's context, and what evidence connects that delivery to a decision?** The important unit is a read-back route, not a database or a product's memory label. Four implementations expose different answers: whole-file prompt loading, caller-requested similarity or identifier lookup, an internal answering loop, and host-triggered checkpoint recall.

This is a qualitative comparison of four complete accepted analysis sets, selected for contrasting mechanisms rather than representativeness. The [memory landscape](agent-memory-landscape.md) supplies the broader framing; its population counts are not recomputed or used here. The evidence is inspected code and shipped instructions, not execution of the systems. “Wired” below means connected in inspected code, not observed in operation. The retained records are those at repository commit `99a6997705964e29dc38c3ef285045223b171485`. The full source boundaries are:

| System | Reviewed source revision | Applicability cutoff | Inspected boundary |
|---|---|---|---|
| [Hermes Agent](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/boundary.md#boundary-and-evidence) | `0e427d788d253630d38a3a51cd76849e73cd6925` | 2026-10-14 | Complete artifact, partial loop; enclosing runtime. |
| [A-MEM](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/boundary.md#boundary-and-evidence) | `f303dfc71e07bdc787f4bc135d4cea328ae30e99` | 2026-10-16 | Whole system relative to the synchronous memory library, not a task-solving agent; separate paper reproduction excluded. |
| [Hindsight](../../../agentic-system-analyses/retained/vectorize-io--hindsight/boundary.md#boundary-and-evidence) | `610c135b6f2d0d8b972da94146ae635943f36271` | 2026-10-14 | Complete artifact, partial loop; service and shipped callers, not complete external host orchestration. |
| [Basic Memory](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/boundary.md#boundary-and-evidence) | `a72751c5d626380dedeed30f55f7a80ba3dc710d` | 2026-10-16 | Complete artifact, partial loop; knowledge engine and shipped integrations, not the enclosing assistant. |

These cutoffs delimit the analyses, not deployment dates. Each linked boundary includes a source register. Accepted analysis completeness does not imply exhaustive route coverage. None of these sets supplies observed runs, measured continuation benefit or a causal experiment for the routes compared below.

## Architectural distinctions

Read-back has at least four separable steps: selecting an item, rendering some of it, placing that rendering in a consumer's input, and the consumer relying on it. An API result establishes a different endpoint from a model prompt. Even prompt inclusion does not show that a later answer depended on the included content.

**Pull** means a consumer requests retained material. **Push** means surrounding machinery supplies it without a request for those items. Both can occur in one chain. A lifecycle callback can request a search from a service, then automatically push the returned excerpts into an assistant's context. The service response is pull; the downstream host injection is push. This distinction is explicit in the accepted [Basic Memory direction assessment](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/memory-profile.md#comparison-rationale).

Selection must also be described separately. Loading an enabled file is coarse selection. Looking up a known identifier selects an address. Similarity search ranks candidates using a query representation. A model choosing which page to open is another decision. A catalog containing identifiers is not evidence of identifier-matched automatic delivery. Nor does a query string alone identify the search algorithm.

Finally, the consumer matters. A model updating memory is not necessarily the model answering the user. A-MEM's evolution model consumes old notes while admitting a new one. Hindsight has maintenance models and an internal reflection answering model. Basic Memory's Tau integration feeds an earlier handoff into a later summarization model as well as making saved handoffs available to the host. These are different uses of retained text, not interchangeable evidence that an answering agent remembered something.

## Concrete implementations

### Hermes: whole notes, advertised skills and requested session search

Hermes makes a useful contrast within one runtime. Its built-in notes and user profile enter the system prompt as whole enabled prompt projections at load time, with load-time threat replacement rather than necessarily byte-identical file contents. There is no query-specific ranking of those blocks. This removes a retrieval decision for those stores, but spends prompt space on the selected files regardless of the current question. Accepting a write involves configurable capacity and admission checks; external file edits can exceed capacity, and loading warns rather than truncates. Ordinary cached requests keep their prior snapshot until a refresh boundary. A successful mutation therefore need not change the very next request ([notes cycle](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/memory.md#mem-rte-notes-cycle)).

Skills use a different division of labor. Eligible names and descriptions are advertised in a prompt index; the foreground model can request a skill body or support file by name or path. Catalog visibility is not body visibility, and viewing a support script is not execution. Some preload and automatic-load alternatives exist, but their complete rendering is not traced. The supported contrast is ordinary catalog advertising versus selective body loading, not a universal rule that all skill bodies require explicit retrieval ([skill cycle](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/memory.md#mem-rte-skill-cycle)).

Hermes also wires model-requested session recall through SQLite full-text search
(FTS). It filters by lineage and other controls, returns bounded snippets and
hydrates the highest-ranked result fully in adaptive mode; explicit session IDs
or message anchors support read/scroll. This is lexical access to archived
messages, not embedding similarity or automatic whole-history injection
([session recall](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/memory.md#mem-rte-session-recall)).

This architecture trades one possible omission for another. Whole-note loading avoids failing to formulate a query, while the catalog lets bodies remain outside the prompt until selected. The catalog route can fail before a relevant procedure is opened; whole-file loading can carry stale or irrelevant material. These are architectural consequences, not measured error rates. Hermes also has session recall, local compaction and optional providers, so the built-in notes path must not stand for its entire memory system.

### Basic Memory: automatic checkpoint excerpts

Basic Memory's direct Pi integration automates a narrower checkpoint route. After the assistant settles, enabled and trusted integration code extracts user/assistant text into a durable thread note. It does not capture every tool-role or nontext block. On the first eligible later agent start, it searches checkpoints using the prompt or fallback query, constrained by project and timeframe. It supplies the first five returned rows, with each matched excerpt flattened and clipped to 500 characters, to the foreground host. This is neither whole-thread replay nor a new reasoning agent ([Pi route](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/runtime.md#rt-rte-pi-checkpoint)).

The host receives references and excerpts. Further reads remain possible, but are not guaranteed by that injection. A reference-data warning describes intended treatment; it does not enforce the model's separation of data from instructions. Search-ranking internals and actual host incorporation remain unresolved in this selected workflow ([delivery account](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/workflow.md#verification-rejection-recovery-and-delivery)).

### A-MEM: caller results and maintenance-model inputs

A-MEM stops at a sharply different boundary. A Python caller constructs a synchronous memory library and supplies note operations. Exact-ID `read` returns a live object. Embedding-based similarity `search` uses IDs selected by Chroma, a vector retrieval store, but returns live fields. `search_agentic` begins with Chroma metadata and can append linked live objects before truncating the total to `k`. If direct hits already fill that budget, every appended neighbor can disappear. A stored link is therefore not proof of linked content reaching the caller ([retrieval route](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/runtime.md#rt-rte-memory-retrieval), [read representations](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/memory.md#read-back)).

A-MEM does have an internal model consumer. During admission, missing semantic metadata can be generated; the enhanced content, context, keywords and tags shape the embedded representation. Subsequent evolution receives related-note text from Chroma metadata. Immediate neighbor edits change live objects without necessarily refreshing those snapshots. Thus exact reads, similarity results and the maintenance model can receive different versions of nominally the same note. The inspected consolidation path does not establish guaranteed replacement of existing collection records ([snapshot object](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/memory.md#mem-obj-chroma-snapshot), [evolution route](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/runtime.md#rt-rte-neighbor-evolution)).

That is a concrete maintenance feedback route, but not a shipped task-answering loop. Returning text to example callers or tests does not establish a downstream answering model using it. The library affords that integration; the accepted boundary does not supply it.

### Hindsight: internal reflection and external host injection

Hindsight goes further inside its own service. A reflection caller supplies a bank, query and controls. The service authorizes the request, loads applicable directives, binds retrieval tools and runs an internal answering model. Tool results supply selected retained prose to subsequent model invocations before an HTTP answer returns. That model is distinct in role from the external host assistant and from models extracting facts, consolidating observations or refreshing pages ([reflection route](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-reflect-request)).

Its page route mixes discovery and address-based recovery. Page search uses embeddings; the reflection model can choose subsequent queries and page IDs, distinct from code-requested initial retrieval. Search can inline a fitting top page and show other hits as 280-character snippets; explicit ID reads retrieve page content. The read budget has a consequential exception: the first available page can exceed it. A later non-fitting page is skipped and its identifier reported for retry. These controls are not an unconditional hard ceiling or a stop-at-first-oversize rule ([page delivery](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-rte-page-delivery)).

Ranking and model judgment are separate from asking an LLM to choose a tool.
Hindsight's inspected recall path supports configured fusion/ranking and a
cross-encoder that scores query/candidate pairs. This learned relevance judgment
is distinct from embedding similarity and from the reflection model deciding
which page IDs to read. Reciprocal rank fusion (RRF) and interleave alternatives bypass the cross-encoder;
the analyses do not inspect every retrieval arm or failover, so they do not
establish one universal ranking pipeline
([reranker](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-cmp-cross-encoder),
[recall selection](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-rte-recall-selection)).

The shipped Claude hooks create another chain: Stop-time transcript retention and prompt-time recall, filtering and formatting into additional host context. The internal reflection answer path and the external hook injection path must not be conflated. Both are wired; neither demonstrates actual external host reliance ([hook route](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-claude-hooks)).

## Comparison and consequences

These alternatives move both control and cost. Whole-file loading pays context
cost on every enabled load but avoids a query/ranking call for those files.
Lexical search depends on matching terms; embedding search depends on numerical
representations; a cross-encoder adds learned pair scoring. Model-directed
tool use introduces a further decision and potentially another round trip.
These are differences in computational work, not measured latency rankings.
Automatic hooks remove a foreground retrieval decision but let integration
configuration select context on its behalf.

Observability should follow each crossing. A tool result or hook payload makes
delivery inspectable; it does not show attention or reliance. IDs can support
source recovery only if the next consumer receives them and follows them.
Hindsight independently budgets fact text, chunks and source facts: a lineage
pointer can survive without its readable justification. Thus provenance stored
at rest is not provenance delivered to the decision
([recall budgets](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-rte-recall-selection)).

Across these examples, retention and delivery are not one availability bit. A-MEM separates live notes from retrieval snapshots. Basic Memory separates database acceptance from deferred Markdown and index publication; structured reload and graph-context retrieval also have different sources and shapes. Compact graph returns can omit source prose that explicit note reads can recover ([publication](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/runtime.md#rt-rte-note-materialization), [context building](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/runtime.md#rt-rte-context-build), [note reload](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/memory.md#mem-rte-note-reload)).

Even a user-visible success signal can stop short of the intended guarantee. Basic Memory's Pi subprocess helper checks exit status and JSON syntax, not an explicit write-success field or read-after-write confirmation. Its recall flag is consumed before search; a failed search can exhaust that session's automatic attempt. A capture notification and a recall callback are weaker evidence than confirmed durable publication and a captured later consumer ([workflow checks](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/workflow.md#verification-rejection-recovery-and-delivery)).

Compression creates further boundaries. Basic Memory's Tau route passes prior handoffs into subsequent synthesis and uses orientation to read saved bodies; those are maintenance and later-host consumers respectively. Confirmed branch receipts select a particular checkpoint for orientation, unlike Pi's search-selected excerpts. This is fixed-rule checkpoint selection, not proof that an identifier alone establishes relevance. Requested rationale preservation is not demonstrated fidelity. Its model summarization must not be generalized to Pi's fixed extraction ([Tau handoff](../../../agentic-system-analyses/retained/basicmachines-co--basic-memory/memory.md#mem-rte-tau-handoff)). Hindsight's within-request context synthesis, meanwhile, blanks older tool bodies while retaining current-run backing history. It is not evidence of durable cross-invocation memory restoration ([context synthesis](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-context-synthesis)).

## Evidence limitations

The common consequence is conditional: relevant stored material helps only if the selection and rendering preserve what the particular consumer needs. None of these records measures that preservation or the benefit of these alternatives. Partial route inventories also prevent exhaustive counts or conclusions that uninspected consumers are absent.

## Open questions and experiments

The next evidence should distinguish activation from benefit. A useful trace would identify the retained item's version, selection trigger, returned representation, exact consumer input and subsequent action. It should distinguish an unavailable item, a missed selection, clipped evidence and delivered-but-unused material. This would test whether a wired route actually operates without yet claiming it improves decisions.

Three controlled comparisons could then test different mechanisms:

- **Whole blocks versus selective access.** Hold the original note corpus and answering model constant. Compare whole-note loading with catalog-plus-body retrieval, counting catalog, tool-output and whole-block tokens against the same context budget. Measure relevant-evidence delivery, unnecessary context, retrieval calls, latency and task outcomes. Include tasks requiring exceptions buried in bodies, not just catalog-recognizable topics.
- **Versions and truncation.** After a known A-MEM neighbor edit, compare exact reads, map-backed search, metadata-backed search and evolution inputs. Vary direct-hit occupancy to test whether links survive. For Hindsight pages, vary first-page size and later-page fit, recording omission IDs and actual retries. These test representation and budget behavior before answer quality.
- **Checkpoint continuation.** For Basic Memory, verify successful admission and later read-back, then compare otherwise matched continuations with recall enabled and disabled. Separately vary excerpt length or permit full-body reads. Score factual continuity and next-action correctness against retained evidence, including capture omissions and failed-search sessions rather than only successful recalls.

These are proposed experiments, not results. Observed prompt inclusion would establish activation; measured outcome differences would establish performance under the tested conditions. Causal attribution to selection, compression or retention would require varying that component while holding the others fixed. The strongest conclusion supported now is narrower: these systems wire materially different paths from retained state to later inputs. Which path improves the next decision remains an empirical question.

[Agent Memory topic](../../topics/memory.md) · [Memory comparisons and data](./README.md) ·
[Correction propagation](./correction-propagation.md) · [Methods & Data](../../methods.md)
