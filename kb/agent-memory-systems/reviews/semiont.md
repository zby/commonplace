---
description: "Semiont review: event-sourced W3C annotation KB with human/AI peer workflows, graph/vector projections, context gathering, and pull-based agent access"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# Semiont

Semiont, from The AI Alliance, is a source-grounded semantic knowledge platform for shared human/AI annotation work. At the reviewed commit, its durable memory model is not a chat transcript or private agent note store: it is a project knowledge base of resources, W3C Web Annotations, event-sourced history, materialized views, graph projections, and vector indexes, exposed through browser, SDK, CLI, and MCP surfaces.

**Repository:** https://github.com/The-AI-Alliance/semiont

**Reviewed commit:** [e44737844808ab209effa26978cf412957e50ea3](https://github.com/The-AI-Alliance/semiont/commit/e44737844808ab209effa26978cf412957e50ea3)

**Last checked:** 2026-06-05

## Core Ideas

**Annotations are the central behavior-shaping memory.** Semiont stores source resources plus W3C annotations whose targets carry selectors and whose bodies carry tags, comments, assessments, or links to other resources. The protocol docs frame Mark as the flow that creates those annotations manually or through AI-assisted detection, and the code persists them through `mark:create` / `mark:update-body` events handled by Stower ([docs/protocol/flows/MARK.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/docs/protocol/flows/MARK.md), [packages/make-meaning/src/stower.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/stower.ts), [packages/make-meaning/src/annotation-operations.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/annotation-operations.ts)). The memory unit is source-anchored interpretation, not free-floating prose.

**The event log is canonical; graph, views, and vectors are projections.** The storage docs make `.semiont/events/` the durable, repo-committed source of truth, while materialized views are rebuildable state. The code follows that split: `EventStore.appendEvent` persists, materializes, and publishes; `GraphDBConsumer` consumes persisted events into a graph; `Smelter` consumes resource and annotation events into embedding files and a vector store ([packages/event-sourcing/docs/STORAGE-LAYOUT.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/event-sourcing/docs/STORAGE-LAYOUT.md), [packages/event-sourcing/src/event-store.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/event-sourcing/src/event-store.ts), [packages/make-meaning/src/graph/consumer.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/graph/consumer.ts), [packages/make-meaning/src/smelter.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/smelter.ts)).

**Humans, agents, workers, scripts, and UI share the same verbs.** The protocol is organized around frame, yield, mark, match, bind, gather, browse, and beckon; the README says GUI operations are available through SDK, CLI, and agent skills. The MCP handler exposes the same browse/mark/bind/gather/yield operations to MCP clients rather than a separate agent-only memory API ([README.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/README.md), [docs/protocol/README.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/docs/protocol/README.md), [packages/mcp-server/src/handlers.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/mcp-server/src/handlers.ts)).

**AI assistance is acquisition and annotation, not autonomous memory consolidation.** `mark.assist` creates jobs for highlighting, assessing, commenting, tagging, or reference detection; worker processors call LLM detection/extraction, reconcile anchors against source content, deduplicate identical annotations, and return W3C annotation objects for persistence ([packages/sdk/src/namespaces/mark.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/sdk/src/namespaces/mark.ts), [packages/jobs/src/workers/annotation-detection.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/jobs/src/workers/annotation-detection.ts), [packages/jobs/src/processors.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/jobs/src/processors.ts), [packages/jobs/src/workers/detection/entity-extractor.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/jobs/src/workers/detection/entity-extractor.ts)). The inspected path does not learn new rules from agent traces or summarize old memories into stronger artifacts.

**Context efficiency is selective, but not globally budgeted.** Gather extracts the selected passage plus bounded surrounding text, graph neighborhood, optional relationship summary, and optional vector-similar annotations; Matcher searches names, entity types, graph neighbors, vectors, and optional LLM re-ranking over top candidates ([packages/make-meaning/src/annotation-context.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/annotation-context.ts), [packages/make-meaning/src/matcher.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/make-meaning/src/matcher.ts), [docs/protocol/flows/GATHER.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/docs/protocol/flows/GATHER.md), [docs/protocol/flows/MATCHER.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/docs/protocol/flows/MATCHER.md)). This controls scope and complexity better than loading whole corpora, but there is no single token budgeter or prompt-packing policy across all read paths.

**Trust comes from anchoring, provenance, and replayability.** Detected annotations carry dual selectors, generator metadata, creator attribution, and source text reconciliation; events carry sequence/hash metadata; projections can be rebuilt from the event log ([docs/protocol/W3C-WEB-ANNOTATION.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/docs/protocol/W3C-WEB-ANNOTATION.md), [packages/jobs/src/processors.ts](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/jobs/src/processors.ts), [packages/event-sourcing/docs/STORAGE-LAYOUT.md](https://github.com/The-AI-Alliance/semiont/blob/e44737844808ab209effa26978cf412957e50ea3/packages/event-sourcing/docs/STORAGE-LAYOUT.md)). That is strong source-grounding, but the code does not prove that later agents faithfully use retrieved context.

## Artifact analysis

- **Storage substrate:** `files` `repo` `graph` `vector` — Canonical domain events live as JSONL files under `.semiont/events/` and are intended to be committed with the project; content and embedding caches are file-backed; graph databases and vector stores are derived read models for traversal and similarity search.
- **Representational form:** `prose` `symbolic` `parametric` — Source resources and generated/comment bodies are prose or media content; annotations, selectors, event records, body operations, schema/tag projections, graph nodes/edges, and SDK/MCP contracts are symbolic; embeddings over resources and annotation spans are parametric access structures.
- **Lineage:** `authored` `imported` — Humans, agents, scripts, and workers author resources and annotations through the same flows; documents and generated resources enter through Yield; AI-assisted annotations are derived from source resource content, not from agent session/tool traces. Graph, view, and vector artifacts are derived projections over those authored/imported canonical events.
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` — Annotations and gathered context serve as evidence and reference; entity types, links, graph connections, storage URI indexes, and flow verbs route attention and binding; selector reconciliation, projection validators, event hash chains, and W3C shape constraints validate writes; graph/vector/name/entity/LLM scoring ranks candidates for binding and context assembly.

**Resource and annotation events.** `yield:created`, `mark:added`, `mark:body-updated`, archive, frame, and job lifecycle events are the canonical retained history. Their authority comes from replay: materialized views, graph state, directory metadata, vector indexes, and browser/API responses can be reconstructed from the log.

**W3C annotations.** A single annotation can carry several operative parts: the target selector anchors a source span; the motivation names why the mark exists; textual bodies classify, comment, or assess; `SpecificResource` bodies bind a mention to another resource. This makes an annotation both a knowledge artifact and a routing surface for later gather/match/bind workflows.

**Graph projection.** The graph stores resources, annotations, references, entity-type statistics, connections, reverse references, and paths. It has strong read-time authority for navigation and candidate retrieval, but it is not the source of truth; `GraphDBConsumer` updates it from persisted events and logs failures rather than changing canonical state.

**Vector projection.** `Smelter` chunks resource text, embeds resource chunks and annotation exact text, writes embedding files under `.semiont/embeddings/`, and indexes Qdrant or an in-memory vector store. The embedding text and payload metadata are retained for rebuilds, but the behavior-shaping force is ranking, not canonical knowledge.

**AI worker outputs.** Detection workers are an acquisition path from resource content to annotations. They reconcile LLM spans against source text and drop hallucinated or unreconcilable selections before persistence. Deduplication happens before storage, so it prevents duplicate acquisition rather than curating existing memory.

**Promotion path.** The strongest promotion path is unresolved reference -> matched candidate -> bound annotation: a `TextualBody` entity-type tag can later receive a `SpecificResource` body that turns a source span into a resolved graph edge. A generated resource can also auto-bind back to its source annotation when `generatedFrom` is present. The path strengthens routing authority, but it does not make the annotation an enforced instruction.

## Comparison with Our System

Semiont and Commonplace share a repository-first instinct: durable knowledge should be inspectable, replayable, and usable by tools instead of locked inside a chat transcript. Semiont is more operationally interactive: it is a multi-participant annotation platform with browser UX, event bus, SDK, CLI, MCP, graph, and vector projections. Commonplace is more methodology-centric: it uses Markdown artifacts, collection contracts, type specs, validation, and review workflows to shape how agents write and navigate the KB.

The biggest design difference is the unit of knowledge. Commonplace usually promotes claims, reviews, instructions, definitions, and indexes as human-readable Markdown artifacts. Semiont promotes source-anchored annotations and resource links. That gives Semiont better fine-grained source grounding and collaborative review affordances, but weaker narrative synthesis unless a downstream Yield/generation workflow creates a new resource from gathered context.

The second difference is read-back posture. Commonplace agents mostly navigate with `rg`, links, indexes, and explicit instructions in the repo. Semiont provides explicit read actors: Browse for views, Gather for annotation context, Matcher for candidate ranking, and MCP/SDK/CLI wrappers. The inspected code still looks pull-oriented for agents: a caller asks for context or search results; Semiont does not automatically inject project memory into arbitrary future model calls.

Semiont's event-sourced rebuild story is stronger than Commonplace's current generated-index convention. It can rebuild views, graph, and vectors from event logs. Commonplace has validation and generated indexes, but most curation remains direct artifact editing rather than replayable domain events.

### Borrowable Ideas

**Source-span annotations as first-class KB artifacts.** Commonplace could use W3C-style selectors for source snapshots and reviews where exact evidence spans matter. Ready for source reviews and quote-grounding; broader use needs editor/tooling support.

**Event log plus rebuildable projections.** Commonplace could keep canonical Markdown while logging important semantic mutations and regenerating indexes/reports from that log. Needs a concrete workflow where replay beats direct Git diff review.

**Unresolved reference to bound edge workflow.** Semiont's stub/reference/bind model could map to unresolved backlinks or candidate connections in Commonplace, with a review step before committing graph edges. Ready as a connect-report improvement.

**Projection validators as pure functions.** The tag/entity validation pattern would fit Commonplace type checks: read a projection, run a pure validator, then let the command layer handle I/O. Ready for validation code that currently mixes filesystem reads and rule logic.

**Graph/vector as derived, not canonical.** Semiont keeps embeddings and graph traversal useful without making them the authority. Commonplace should keep the same boundary if it adds semantic search: the source artifact remains authoritative; indexes are rebuildable.

## Write side

**Write agency:** `manual` `automatic` — Humans, agents, scripts, CLI, SDK, UI, and MCP tools can create/update resources and annotations; AI workers automatically create annotations from resource content; Stower automatically appends domain events; projection actors automatically update views, graph, embeddings, and vector indexes.

**Curation operations:** `evolve` — When a generated resource carries `generatedFrom`, Stower automatically emits a `mark:update-body` that adds the new resource as a `SpecificResource` body on the source annotation. That evolves an existing annotation in light of a newly created resource. Other automatic work found in the code is acquisition or access-structure maintenance: AI detection creates new annotations from source content, Smelter rebuilds embeddings, and GraphDBConsumer updates derived graph state.

Semiont does not qualify as trace-derived learning under the Commonplace review rule. It stores events about knowledge work and lets AI workers create annotations, but the inspected durable artifacts are derived from source documents and user/agent commands, not from session logs, tool traces, or trajectories distilled into new rules or learned policies.

## Read-back

**Read-back:** `pull` — Stored memory re-enters work through explicit browse, gather, match, bind, yield, SDK, CLI, browser, and MCP calls. The system supports live event subscriptions and collaboration signals, but the inspected code does not automatically push retained project memory into an agent's next model invocation without a caller requesting a read.

Gather read-back loads one focal annotation, its selected source span, bounded before/after context, target resource context when linked, graph neighborhood, sibling entity types, cited-by resources, optional LLM relationship summary, and optional vector-similar annotation spans. Matcher read-back searches names, entity types, graph neighbors, vector results, and optional LLM-scored candidates, then returns ranked resources. Browser read-back serves resources, annotations, histories, reverse references, entity types, tag schemas, and directory views. Effective precision, context dilution, and whether a downstream model obeys the returned context are not verified from code.

The MCP server exposes these reads as ordinary tool handlers. `gatherAnnotation` returns a JSON context package; `browseResource`, `browseResources`, `browseHighlights`, and `browseReferences` return resource/annotation views; `markAssist`, `bindBody`, `yieldResource`, and `yieldFromAnnotation` modify the store. That is an agent-friendly access surface, but still a pull surface.

## Curiosity Pass

Semiont's own framing as a semantic knowledge platform can make the graph sound canonical. The implementation is more careful: the event log is the canonical record, while graph and vector stores are projections. That separation is a major trust affordance.

The AI-assisted annotation path is powerful but narrower than "memory learning." It extracts marks from source content under a user-requested job, validates anchors, and persists annotations. It does not consolidate old memories, infer project rules from repeated agent behavior, or self-promote lessons into instructions.

The concurrency model is deliberately append/replay oriented. Concurrent annotation creation does not merge; body operations apply in event order without an `If-Match` check. That is simple and replayable, but workflows needing exclusive review have to enforce it at the application layer.

The strongest Commonplace-relevant idea is not vectors; it is the unresolved-reference lifecycle. A source span can be marked before the correct target is known, reviewed, then bound into a graph edge. That is a practical middle ground between ad hoc links and over-eager automated graph construction.

## What to Watch

- Whether Semiont adds agent hooks that automatically gather or inject KB context before arbitrary model calls; that would change read-back from pull to both.
- Whether AI workers begin learning from collaboration/event traces rather than only source documents; that would require a trace-derived learning reclassification.
- Whether generated resources and bindings become autonomous multi-step curation loops; that would expand write-side operations beyond the current narrow auto-bind evolution.
- Whether graph/vector projections gain independent durable authority; that would weaken the current clean event-log source-of-truth story.
- Whether evaluations add per-decision read-back ablations or post-action audits; that would strengthen faithfulness claims for gathered and matched context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - supports classifying Semiont's store as pull read-back despite strong browse/gather/match access surfaces.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating events, annotations, graph projections, vector indexes, and MCP/SDK surfaces by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - frames source resources, annotations, gathered context, and candidate lists as evidence/reference for later work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes Semiont's flow contracts, validators, projections, and ranking paths from ordinary remembered content.
- [Lineage](../../notes/definitions/lineage.md) - applies to Semiont's event replay, generated resources, W3C generator metadata, and projection invalidation boundaries.
