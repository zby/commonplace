---
description: "Semiont review: event-sourced semantic KB with W3C annotations, graph/vector projections, gather/match read-back, and agent skills"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Semiont

Semiont, from The AI Alliance, is an open source semantic knowledge platform for shared human/agent annotation work over source documents. At the reviewed commit, it provides a browser, backend, TypeScript SDK, CLI, local/desktop packaging, protocol docs, and agent skills around eight flows: frame, yield, mark, match, bind, gather, browse, and beckon. The memory-relevant core is a project knowledge base where resources and W3C annotations are persisted as domain events, projected into views, graph state, and embeddings, then read back through context assembly and reference-resolution workflows.

**Repository:** https://github.com/The-AI-Alliance/semiont

**Reviewed commit:** [7e3f183b0b7619ce6be964d2e30c8e5eb6f207df](https://github.com/The-AI-Alliance/semiont/commit/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df)

**Last checked:** 2026-06-02

## Core Ideas

**The retained unit is source-grounded annotation work, not chat memory.** The README frames Semiont as a semantic knowledge platform for annotating, connecting, enriching, and governing domain knowledge; the protocol docs make W3C annotations the portable substrate for marks, links, comments, assessments, and tags ([README.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/README.md), [docs/protocol/W3C-WEB-ANNOTATION.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/docs/protocol/W3C-WEB-ANNOTATION.md)). AI-generated annotations can carry generator metadata, but the artifact is still an anchored annotation over a resource passage, not an unanchored recollection.

**The knowledge base is intentionally inert.** The system docs say the KB does not initiate events; five reactive actors mediate access: Stower for writes, Gatherer for context, Matcher for search, Browser for deterministic reads, and Smelter for vector projection ([docs/system/KNOWLEDGE-SYSTEM.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/docs/system/KNOWLEDGE-SYSTEM.md), [packages/make-meaning/docs/architecture.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/docs/architecture.md)). That makes memory a durable record of participant decisions and derived projections, not an autonomous agent with goals.

**Writes pass through an event-sourced gateway.** `Stower` subscribes to command events such as `yield:create`, `mark:create`, `mark:update-body`, frame changes, and job lifecycle events, then appends persisted events through the event store and content store ([packages/make-meaning/src/stower.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/stower.ts)). `EventStore.appendEvent()` persists to the log, materializes views, optionally enriches, then publishes typed domain events globally and per resource ([packages/event-sourcing/src/event-store.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/event-sourcing/src/event-store.ts)). This gives Semiont a strong lineage surface: later graph and vector state can be regenerated from logged work.

**Graph and vector stores are projections, not the source of truth.** `GraphDBConsumer` subscribes to graph-relevant persisted events and projects resources, annotations, links, entity tags, and frame vocabulary into a graph database with per-resource ordering and burst batching ([packages/make-meaning/src/graph/consumer.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/graph/consumer.ts)). `Smelter` subscribes to resource and annotation events, chunks resource text, embeds resources and annotation exact text, writes durable embedding files, and upserts Qdrant or memory vectors ([packages/make-meaning/src/smelter.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/smelter.ts), [packages/make-meaning/src/embedding-store.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/embedding-store.ts)). The graph and vectors can shape retrieval, but the event log/content store remain authoritative.

**Context efficiency is workflow-scoped.** Gatherer does not load an entire corpus into an agent prompt. `AnnotationContext.buildLLMContext()` validates the annotation, slices selected/before/after source text with a bounded `contextWindow`, collects graph connections, cited-by data, sibling entity types, optional LLM relationship summary, and optional vector-similar annotations ([packages/make-meaning/src/annotation-context.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/annotation-context.ts)). Matcher then retrieves candidates from name, entity-type, graph-neighborhood, and vector channels, scores structural signals, and optionally LLM-reranks the top candidates ([packages/make-meaning/src/matcher.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/make-meaning/src/matcher.ts)). The complexity risk is not raw volume alone; the returned object mixes passage context, graph neighborhood, semantic recall, and generated summaries.

**The integration surface is deliberately multi-participant.** The SDK gives agents and humans the same verb namespaces, with Promise-like Observables for bounded flows and fire-and-forget collaboration signals such as beckon, bind-initiate, and browse-click ([packages/sdk/README.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/sdk/README.md), [packages/sdk/src/namespaces/gather.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/sdk/src/namespaces/gather.ts), [packages/sdk/src/namespaces/match.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/sdk/src/namespaces/match.ts)). The CLI exposes the same knowledge-work verbs, and the bundled skills document agent workflows such as detect references, gather context, match, bind, and generate ([apps/cli/README.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/apps/cli/README.md), [docs/protocol/skills/semiont-wiki/SKILL.md](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/docs/protocol/skills/semiont-wiki/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `files` — Project-local event log, content store, and generated state directories described in the system docs and implemented through `EventStore` plus Stower
- **Representational form:** `mixed` — Symbolic event payloads plus source files/documents; annotations are W3C-shaped JSON with prose bodies and selectors

**Persisted domain events and content files.** Storage substrate: project-local event log, content store, and generated state directories described in the system docs and implemented through `EventStore` plus Stower. Representational form: symbolic event payloads plus source files/documents; annotations are W3C-shaped JSON with prose bodies and selectors. Lineage: authored, imported, or agent-generated commands become persisted domain events with user/generator attribution where available; content checksums and storage URIs connect resources to bytes. Behavioral authority: source events are system-definition artifacts for reconstruction, validation of current state, graph/vector projection, and live domain-event broadcast; retained resources and annotations are knowledge artifacts when later read as evidence or context.

**Materialized views.** Storage substrate: filesystem view storage updated by `EventStore.appendEvent()`. Representational form: symbolic resource/annotation views derived from the event log. Lineage: deterministic projection from persisted events; event changes or replay invalidate and regenerate views. Behavioral authority: system-definition artifact for fast reads, browsing, annotation lookup, and downstream context assembly.

**Graph projection.** Storage substrate: graph database behind the `GraphDatabase` interface. Representational form: symbolic graph vertices and edges for resources, annotations, entity tags, references, and frame vocabulary. Lineage: trace-derived projection from a filtered set of persisted events, applied by `GraphDBConsumer`. Behavioral authority: system-definition artifact for traversal, candidate retrieval, bidirectionality/citation scoring, and graph context; knowledge artifact when returned as related resources or citations.

**Embedding store and vector index.** Storage substrate: durable `.semiont/embeddings/` files plus Qdrant or memory vector store. Representational form: mixed prose chunks, exact annotation text, symbolic metadata, and distributed-parametric embeddings. Lineage: derived from resource content and annotation selectors after `yield:*` and `mark:*` events; model mismatch or resource update regenerates embeddings. Behavioral authority: ranking and retrieval authority for semantic context and candidate search; effective precision is not verified from code.

**GatheredContext and match results.** Storage substrate: transient bus responses and SDK Observables, not durable memory by default. Representational form: mixed passage prose, annotation/resource metadata, graph summaries, vector matches, optional LLM summary, and scored candidates. Lineage: assembled from views, content, graph, vectors, user hints, and optional inference calls. Behavioral authority: advisory context for generation, binding, compose workflows, and agent skills; Matcher scores can route a bind/generate decision but do not themselves persist unless a participant writes the chosen bind.

**Agent skills and protocol docs.** Storage substrate: repository Markdown skill files and protocol documentation. Representational form: prose instructions plus code snippets and thresholds. Lineage: authored system-definition artifacts. Behavioral authority: instruction for external coding agents and operators; they can drive Semiont's flow sequence but still rely on the live KB and bus for actual state.

The main promotion path is trace event -> projected view/graph/vector state -> gathered context -> human or agent decision -> new mark/bind/yield event. Semiont can turn a source passage into an annotation, a reference candidate, a generated resource, and a graph edge, but code-level governance still depends on the workflow actor or reviewer deciding when the result deserves durable authority.

## Comparison with Our System

| Dimension | Semiont | Commonplace |
|---|---|---|
| Primary purpose | Collaborative semantic KB platform for source-grounded documents and agents | Git-native methodology KB for agent-operated knowledge systems |
| Canonical retained artifact | Resources, W3C annotations, persisted events, projections, embeddings | Typed Markdown artifacts, source snapshots, generated indexes, review reports |
| Write path | EventBus command -> Stower -> event log/content store -> projections | Author/edit artifact -> validation/review/index workflows |
| Retrieval/read-back | Gatherer, Matcher, Browser, vectors, graph traversal, SDK/CLI/skills | `rg`, indexes, links, collection contracts, skills, validation/review gates |
| Behavioral authority | Protocol flows, actors, event store, graph/vector rankings, workflow skills | Collection contracts, type specs, instructions, validators, review gates |
| Governance style | Source grounding plus participant/reviewer workflow; projections are rebuildable | Explicit artifact typing, citations, deterministic validation, archive/replacement discipline |

Semiont and Commonplace share the central assumption that memory should be source-grounded and inspectable. Semiont is stronger as an application substrate for collaborative annotation over documents: it has a browser, API, event bus, graph, vectors, SDK, CLI, agent skills, and coordination signals. Commonplace is stronger as a small, text-native governance layer: artifacts are directly readable in git, typed by collection contracts, cited to sources, and checked by deterministic validators and review gates.

The major design divergence is where semantics live. Commonplace makes the durable artifact itself carry much of the meaning: frontmatter, type, prose, links, and validation rules are in the file. Semiont makes meaning emerge from event-sourced annotations, graph projection, vector projection, and protocol flows. That is more operational and collaborative, but it means a reviewer often has to inspect several surfaces to know why a candidate appeared: the annotation, graph neighbors, vector result, scoring rules, user hint, and optional LLM score.

**Read-back:** `both` — Explicit pull via SDK/CLI/browser calls, and engineered push in the reference-resolution UI where `bind:initiate` opens the wizard and emits `gather:requested`, causing bounded context to arrive before the user chooses bind/generate/compose ([packages/react-ui/src/features/resource-viewer/state/resource-viewer-page-state-unit.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/react-ui/src/features/resource-viewer/state/resource-viewer-page-state-unit.ts), [packages/sdk/src/state/flows/gather-state-unit.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/sdk/src/state/flows/gather-state-unit.ts))

### Borrowable Ideas

**Treat event traces as first-class lineage for derived search layers.** Ready conceptually. Commonplace already has generated indexes and review reports; Semiont's event log -> views/graph/vectors split is a useful reminder that derived search state should remain rebuildable from retained source events rather than becoming opaque memory.

**Separate deterministic browse from recommendation search.** Ready now as a design rule. Semiont's docs distinguish Browser queries from Matcher recommendations: one signal and one ordering belong in Browse, multi-source fusion and scoring belong in Matcher. Commonplace can use the same boundary for future search layers: lexical/index lookup is browse; blended relevance ranking is recommendation.

**Make attention and coordination signals part of the protocol, but keep them ephemeral.** Needs a concrete Commonplace workflow. Beckon-style focus events could help agents and humans coordinate review attention, but the borrowed version should avoid turning hover/click presence into durable knowledge unless a separate artifact intentionally captures it.

**Use gathered context as a typed intermediate, not just a prompt string.** Ready for agent workflows. Commonplace could expose a structured context object containing source span, linked notes, candidate references, validation state, and reviewer notes before generation. That would make review of context assembly easier than auditing a final prompt.

**Do not borrow automatic projection as authority promotion.** Semiont's graph and vector projections are useful because they shape retrieval, not because they make claims true. Commonplace should preserve the distinction: generated candidates and rankings can advise, but only reviewed artifacts should become instructions, definitions, or validators.

## Trace-derived learning placement

**Trace source.** Semiont qualifies under the current rule because durable projections are derived from event streams. The raw trace is not a free-form chat transcript; it is a persisted stream of semantic domain events such as `yield:created`, `mark:added`, `mark:body-updated`, entity-tag events, frame events, and job lifecycle events ([packages/core/src/persisted-events.ts](https://github.com/The-AI-Alliance/semiont/blob/7e3f183b0b7619ce6be964d2e30c8e5eb6f207df/packages/core/src/persisted-events.ts)). Those events may come from humans, AI workers, scripts, or skills.

**Extraction.** The extraction path is mixed. Some outputs are deterministic projections: views and graph updates are derived from event payloads. Some outputs are distributed-parametric: Smelter embeds resource chunks and annotation exact text after resource/annotation events. Some outputs are LLM-assisted before persistence: agent skills and job workers can produce annotations or generated resources, which then enter the same event stream.

**Four fields.** The raw stage is the event log and content store: file-backed symbolic/prose retained artifacts, lineage from participant commands and content checksums, and system-definition authority for replay/projection. The distilled stage is materialized views, graph state, embedding files, vector index, and gathered context: mixed symbolic/prose/distributed-parametric forms, lineage from specific event types and source text, and ranking/routing/advisory authority during read-back.

**Scope and timing.** Scope is mostly per project and per resource. `GraphDBConsumer`, Smelter, Gatherer, and view materialization all preserve per-resource ordering; graph/vector projection is online and eventually consistent, while rebuild paths can regenerate derived state.

**Survey placement.** Semiont belongs in the trace-to-projection family: structured interaction events become durable views, graph relationships, embeddings, and context assembly inputs. It strengthens the survey axis for rebuildable, source-grounded derived state. It does not, by itself, prove that trace-derived outputs should become high-authority instructions without review.

## Read-back placement

**Direction.** Both. Agents and scripts can explicitly pull memory with `browse`, `gather`, `match`, and `listen`. The resource viewer also has an engineered push path: `bind:initiate` updates wizard state and emits `gather:requested`; the gather state unit turns that local event into `client.gather.annotation(...)`, so context is prepared for the resolution workflow before the user explicitly runs search or generation.

**Trigger and relevance signal.** The push trigger is typed and workflow-specific: an unresolved reference-resolution event carrying annotation id, resource id, default title, and entity types. Relevance is then assembled from the selected annotation span, bounded surrounding text, graph neighborhood, entity-type statistics, optional vector-similar annotations, user hint, and optional inference summary. Precision and recall are not verified from code.

**Timing relative to action.** The pushed gather happens before the bind/generate/compose decision in the wizard. Matcher search runs after the user chooses the Bind path, with explicit limit and semantic-scoring options.

**Selection, scope, and complexity.** The default gather context window is 2000 characters in the SDK/state-unit path, with code validation allowing 100 to 5000. Graph context and semantic context are separately bounded by implementation limits such as top connection names, vector annotation limit 10, Matcher resource vector limit 40, and Matcher final limit 10 unless overridden. The result can still be complex because it mixes span text, metadata, graph relations, semantic matches, and LLM summaries.

**Authority at consumption.** Read-back is advisory context for humans and agents until a participant writes a mark, bind, yield, or frame event. Matcher scores can route the agent-skill choice between binding and generation, but the durable authority comes from the subsequent write event.

**Faithfulness.** I did not find a built-in WITH/WITHOUT ablation or post-action audit proving that gathered context changed agent behavior. The code can show activation and selection mechanics, not effective use.

**Other consumers.** The same memory surfaces are consumed by humans in the browser, scripts through the SDK/CLI, agent skills, workers, and observability/listen subscribers. Beckon attention signals can direct users and agents, but they are ephemeral coordination rather than durable read-back of knowledge.

## Curiosity Pass

**The platform is closer to a collaborative annotation operating system than a memory store.** Its durable state is not just "memories"; it is resources, annotations, events, projections, credentials, jobs, skills, and live coordination flows.

**The graph is explicitly derivative.** That is a useful discipline. Semiont does not make the graph the authoritative record, which avoids the common problem where a graph memory becomes impossible to audit back to source events.

**The strongest push mechanism is UI/workflow push, not autonomous pre-action agent memory.** `bind:initiate` prepares context for a resolution decision, but I did not find a deployed agent loop that automatically injects memories before arbitrary actions.

**Context assembly can become semantically dense.** The bounded context window helps volume, but graph neighborhoods, semantic matches, user hints, and LLM summaries can create a high-complexity object that still needs careful presentation and scoring explanations.

**Agent skills are system-definition artifacts outside the runtime.** They are valuable because they codify workflows, but they are not enforced by the platform unless an agent chooses to load and follow them.

**Generated resource auto-bind is a sharp authority transition.** Stower can auto-add a `SpecificResource` body when a generated resource has `generatedFrom` metadata. That is practical, but it means generation and binding can become one workflow-level authority step.

## What to Watch

- Whether Semiont adds source-span, prompt/model, and reviewer/audit metadata for every LLM-generated annotation, summary, match score, and generated resource.
- Whether the reference-resolution push path expands into a deployed agent pre-action hook, and whether it measures context faithfulness rather than assuming delivered context is used.
- Whether graph/vector projection rebuilds remain clearly subordinate to the event log as more providers and search recipes appear.
- Whether agent skills gain a review/promotion lifecycle, so skill instructions can move from examples into governed system-definition artifacts.
- Whether Matcher explanations become durable or inspectable enough for low-confidence bind decisions.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Semiont derives views, graph state, embeddings, and context inputs from persisted domain-event streams.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Semiont requires separating event logs, source files, W3C annotations, views, graph state, embeddings, gathered context, and skills by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: resources, annotations, gathered context, graph neighbors, and match results mostly advise future behavior as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: protocol flows, event schemas, actors, projections, scoring code, SDK methods, and agent skills constrain or route behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Semiont stores rich knowledge, but activation still depends on gather/match/browse calls or workflow-triggered push.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Semiont shows a structured event-to-projection path, while preserving the need for review before high-authority promotion.
