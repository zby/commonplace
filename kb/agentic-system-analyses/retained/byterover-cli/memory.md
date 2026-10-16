---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ByteRover CLI memory: topic guidance, access-signal feedback, alternate read-back and internal context replacement within the frozen repository."
run-id: AAS-2026-10-15-byterover-cli-71610aaf716b-01
source-identity: https://github.com/campfirein/byterover-cli
reviewed-boundary: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
---

# ByteRover CLI memory report

## Boundary and evidence

The memory boundary includes project topics, their rendering and retrieval, access-signal feedback, derived context artifacts, maintenance/recovery material and internal conversation reduction. It follows the complete artifact, partial loop boundary in [boundary](boundary.md). SRC-1 is the sole source. Git HEAD was checked against the frozen revision; the source checkout was clean. No target code, tests, examples, model calls or services were executed.

The supplied runtime is evidence for its quoted implementation paths, not a coverage ceiling. Direct reads added the paths below, including contrary cases to claims about universal admission, archive formats and freshness. All new evidence is implementation, except generated-prompt text, which establishes requested behavior rather than model compliance. External agent implementations, provider internals, Cloud, the transport dependency and shared UI implementation remain excluded. No observed-run or causal-experiment evidence is available. File retention, delivery, actual reliance and benefit are separate conclusions.

### Coverage inventory

“Supplied” identifies findings inherited from runtime; “direct” identifies source inspection in this job. Paths are SRC-1 commit-relative anchors. Available but uninspected branches remain in scope and limit conclusions rather than becoming absences.

| Entry point / memory operation | Source path and inspection | Covering records / limits |
|---|---|---|
| CLI/MCP curate; internal curate | Supplied `src/oclif/lib/curate-session.ts`, `src/server/infra/mcp/tools/brv-curate-tool.ts`, `src/server/infra/executor/curate-executor.ts` | [RT-RTE-curate-session](runtime.md#rt-rte-curate-session), [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation); caller authorship differs from software admission. |
| Topic semantic bodies and metadata | Direct `src/server/infra/render/reader/html-renderer.ts`; supplied writer | [MEM-OBJ-bv-rule](#mem-obj-bv-rule), [MEM-OBJ-bv-reason](#mem-obj-bv-reason), [MEM-OBJ-bv-topic](#mem-obj-bv-topic). |
| Public query and MCP delivery | Supplied query route; direct `src/server/infra/executor/query-executor.ts`, `src/server/infra/mcp/tools/brv-query-tool.ts` | [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval), [MEM-OBJ-query-cache](#mem-obj-query-cache); no internal synthesis on tool-mode path. |
| Alternative search and focused read | Direct `src/oclif/commands/search.ts`, `src/oclif/commands/read.ts`, `src/oclif/lib/read-topic.ts`, `src/agent/infra/tools/implementations/search-knowledge-service.ts` | [MEM-RTE-search-recall](#mem-rte-search-recall), [MEM-RTE-topic-read](#mem-rte-topic-read); focused read also supplies update authors. |
| Access history and automatic ranking updates | Direct `src/server/infra/context-tree/runtime-signal-store.ts`, `src/server/infra/context-tree/tool-mode-sidecar-updaters.ts`, search service, daemon construction | [MEM-OBJ-runtime-signals](#mem-obj-runtime-signals), [MEM-RTE-signal-feedback](#mem-rte-signal-feedback). |
| Internal query broad-context injection | Direct query executor, `src/server/infra/context-tree/file-context-tree-manifest-service.ts`, `src/server/core/domain/knowledge/summary-types.ts` | [MEM-OBJ-context-manifest](#mem-obj-context-manifest), [MEM-RTE-manifest-injection](#mem-rte-manifest-injection); not public query wiring. |
| Hierarchical and sibling summaries | Direct `src/server/infra/context-tree/file-context-tree-summary-service.ts`, `src/agent/infra/map/abstract-generator.ts`; queue write sites searched in `src/agent/infra/map/abstract-queue.ts` | [MEM-OBJ-summary-index](#mem-obj-summary-index), [MEM-OBJ-file-abstract](#mem-obj-file-abstract), [MEM-OBJ-file-overview](#mem-obj-file-overview). Generation coverage and HTML compatibility remain bounded below. |
| Dream structural candidates and removal | Supplied dream route; direct `src/server/infra/dream/tool-mode/topic-loader.ts`, `src/server/infra/dream/tool-mode/prune-candidates.ts`, finalize portion of `src/server/infra/dream/tool-mode/dream-session.ts` | [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance), [MEM-OBJ-dream-archive](#mem-obj-dream-archive); full link/merge/synthesis algorithms uninspected here, preventing complete candidate-quality assessment. |
| Alternative archive and reload | Direct `src/server/infra/context-tree/file-context-tree-archive-service.ts`, `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`, tool registry | [MEM-OBJ-archive-stub](#mem-obj-archive-stub), [MEM-OBJ-full-archive](#mem-obj-full-archive), [MEM-RTE-archive-expansion](#mem-rte-archive-expansion); archive service capacity is not proof of a deployed automatic archive writer. |
| Review rejection and undo | Supplied review writer/handler; direct initial undo control flow in `src/server/infra/dream/dream-undo.ts` | [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), [MEM-OBJ-dream-archive](#mem-obj-dream-archive); per-operation undo branches and CLI log assembly not fully traced, preventing an end-to-end restoration guarantee. |
| Internal full compaction, pruning, rolling checkpoint | Direct `src/agent/infra/llm/context/compaction/compaction-service.ts`, selected LLM service, context manager and message-storage ranges | [RT-RTE-context-control](runtime.md#rt-rte-context-control), [MEM-OBJ-compaction-boundary](#mem-obj-compaction-boundary), [MEM-OBJ-checkpoint-progress](#mem-obj-checkpoint-progress). Alternative reactive/enhanced compression implementations enumerated, not traced; no universal reduction-policy conclusion. |
| Direct editor, hub, Cloud | Supplied `src/server/infra/transport/handlers/context-tree-handler.ts`, `src/server/infra/hub/hub-install-service.ts`, pull/push handlers | [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit), [RT-RTE-hub-install](runtime.md#rt-rte-hub-install), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync); distinct admissions, not universal HTML validation or pre-read approval. |
| Dispatch, hooks and registered library/tools | Direct command-file inventory, `package.json` hook declarations, `src/oclif/commands/hook-prompt-submit.ts`, tool registry and command-filter method | Static hook instructions are not experiential read-back. Registered search/expand/read/write/curate/ingest/map/swarm surfaces prevent equating public tool-mode with all library behavior. Detailed ingest/map/swarm persistence, connector loading, migration, Git VC/worktree replacement and update admission remain uninspected; no completeness, common rollback or freshness guarantee across them. |
| Raw operational logs / evaluator claims | Supplied curate logging; direct search of `src/server/infra/usecase/query-log-summary-use-case.ts` | Query-log summary lists operational counts, timing, matched paths and gaps; no inspected automatic semantic revision consumer established from this summary command. Full log storage and downstream manual use remain uninspected. Benchmark benefit remains attributed reporting under [RT-CLM-project-memory](runtime.md#rt-clm-project-memory). |

## Core ideas

1. **The public memory loop separates authoring from admission and use.** The caller supplies HTML, the daemon checks structure and writes, and a later caller receives rendered content. The same topic can guide an update author through focused read or guide work through query. These are different consumer roles; neither establishes factual verification or actual obedience. See [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), [MEM-RTE-topic-read](#mem-rte-topic-read) and [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance).
2. **Access metadata has a separate feedback loop.** Returned search hits become retained importance/access/maturity signals, which later alter ranking and maintenance candidates. This is automatic trace-fed selection adjustment, not automatic rewriting of what a topic says, and not evidence that frequently retrieved material is correct. See [MEM-RTE-signal-feedback](#mem-rte-signal-feedback).
3. **There are several lossy context representations, not one memory format.** HTML-to-markdown rendering, query caches, per-file abstracts, hierarchical summaries, archive cues, full compaction and rolling checkpoints have different producers, consumers and invalidation. The rolling checkpoint is a deterministic account of tool names and short assistant snippets, not a model-written explanation of the task. See the operative objects below.
4. **Withdrawal is path-specific.** Review rejection can restore/delete a live topic; tool-mode dream moves it outside the active tree; the separate archive service leaves a searchable cue and full-content reload capability. A cached rendered answer can still precede a fresh disk read. Universal immediate removal from all consumers is not established. See [MEM-OBJ-query-cache](#mem-obj-query-cache), [MEM-OBJ-dream-archive](#mem-obj-dream-archive) and [MEM-RTE-archive-expansion](#mem-rte-archive-expansion).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-bv-rule
Label: Topic rule and decision bodies

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

Source-native units are `bv-rule` and `bv-decision` bodies in local topic HTML. Natural-language content is stored on the filesystem; tag, ID and severity are symbolic annotations. The renderer supplies readable labels, not executable rule enforcement. Lineage is caller/model-authored content admitted through the applicable writer, or replacement bytes through alternate admissions. Later query/read consumers receive rendered text; only external interpretation gives it behavioral force. This part differs from the topic container and from its rationale and selection metadata. SRC-1, `src/server/infra/render/reader/html-renderer.ts`; the rule passage is supplied by [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval).

> case 'bv-decision': {
>   const id = attributes.id ? ` (${attributes.id})` : ''
>   return `- **Decision**${id}: ${text}`
> }
> --- `src/server/infra/render/reader/html-renderer.ts`

No actual theory content or observed consumption episode is supplied; the schema's ability to carry rules does not establish a theory-building process.

#### MEM-OBJ-bv-reason
Label: Topic reason body

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

`bv-reason` stores natural-language rationale in the topic file. Its authoring/admission lineage follows the topic, not a mandatory derivation from raw execution traces. The renderer preserves it for query and focused-read consumers. Thus rationale can survive and reach a later agent; the implementation does not prove each rule has a reason, that the reason is sound, or that the reader uses it. Distinct from reviewer `meta.reason`, which belongs to the change/review record rather than necessarily the topic. SRC-1, `src/server/infra/render/reader/html-renderer.ts`, `src/server/core/domain/render/curate-prompt-builder.ts`.

> case 'bv-reason': {
>   return `**Reason:** ${text}`
> }
> --- `src/server/infra/render/reader/html-renderer.ts`

#### MEM-OBJ-bv-topic
Label: Topic selection attributes

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

The `bv-topic` path, title, summary and related attributes are persisted markup. Path and relations have symbolic lookup/candidate consumers; title and summary also contain readable natural language. The dream loader combines these attributes with full HTML, file mtime and separate signals. This is a selection/preview part, not the whole body and not an independent factual source. Rendering can lift topic metadata into the readable result; maintenance can inspect raw HTML. Initial truth/provenance remains supplied by the writer's caller. SRC-1, `src/server/infra/dream/tool-mode/topic-loader.ts`, `src/server/infra/render/reader/html-renderer.ts`.

> return {
>   html,
>   mtimeMs,
>   path: relPath,
>   related: parseRelated(attrs.related ?? ''),
>   signals,
>   summary: attrs.summary ?? '',
>   title: attrs.title ?? '',
> }
> --- `src/server/infra/dream/tool-mode/topic-loader.ts`

#### MEM-OBJ-runtime-signals
Label: Runtime signal sidecar

The source-native `RuntimeSignals` records use composite `signals` keys in `IKeyStorage`; daemon construction supplies `FileKeyStorage` at `configResult.storagePath`. They are symbolic numerical/access metadata, not embeddings or model parameters and not topic prose. Defaults seed new topics; successful rewrites and accumulated retrieval hits update them. Search scoring and prune candidate selection consume them. See [MEM-RTE-signal-feedback](#mem-rte-signal-feedback). This is distinct from [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree): the sidecar can fail independently and is deleted/reset separately on archival/restoration. SRC-1, `src/server/infra/context-tree/runtime-signal-store.ts`, `src/server/infra/context-tree/tool-mode-sidecar-updaters.ts`, `src/server/infra/daemon/agent-process.ts`.

> const daemonKeyStorage = new FileKeyStorage({
>   storageDir: configResult.storagePath,
> })
> --- `src/server/infra/daemon/agent-process.ts`

Corrupt/missing entries fall back to defaults. Per-key update locking within a process does not establish cross-process serializability. These are relevance/activity signals; the label `validated` is not factual validation.

#### MEM-OBJ-query-cache
Label: Query result caches

Two process-local `QueryResultCache` instances retain strings: internal response text versus JSON-serialized tool-mode envelopes. Natural-language answers/rendered bodies are wrapped in symbolic query tokens, fingerprint and timestamp metadata. This is a derived result store, distinct from persistent source topics and from [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval), the route that reads one instance. Exact normalized-query and fuzzy token-set matching can deliver earlier selected content to later requests without rereading the source. Defaults are 50 entries and 60 seconds; daemon enables caching. SRC-1, `src/server/infra/executor/query-result-cache.ts`, `src/server/infra/executor/query-executor.ts`, `src/server/infra/daemon/agent-process.ts`.

> this.maxSize = options.maxSize ?? 50
> this.ttlMs = options.ttlMs ?? 60_000
> --- `src/server/infra/executor/query-result-cache.ts`

Freshness is narrower than the comment “if any file ... changes.” The fingerprint glob uses the `.md` constant, with a 30-second fingerprint fast path; it does not directly enumerate HTML topics. Therefore an HTML-only overwrite/reject/archive need not invalidate that fingerprint even after its fast path expires. Cache TTL still bounds reuse; this is not indefinite retention. No experiment establishes an exercised stale result. SRC-1, `src/server/constants.ts`, `src/server/infra/executor/query-executor.ts`.

> const globResult = await this.fileSystem!.globFiles(`**/*${CONTEXT_FILE_EXTENSION}`, {
>   cwd: contextTreePath,
>   includeMetadata: true,
>   maxResults: 10_000,
>   respectGitignore: false,
> })
> --- `src/server/infra/executor/query-executor.ts`

#### MEM-OBJ-context-manifest
Label: Active context manifest

`_manifest.json` is a filesystem-persisted symbolic selection artifact, not another semantic summary. It records selected paths/types, estimated tokens and a source fingerprint. Lane allocation chooses summaries by condensation order, contexts by importance, and stubs within separate budgets. The later consumer is the internal query prompt builder through [MEM-RTE-manifest-injection](#mem-rte-manifest-injection). It is distinct from the topic container, query search envelope and supplied context-control route. SRC-1, `src/server/infra/context-tree/file-context-tree-manifest-service.ts`, `src/server/core/domain/knowledge/summary-types.ts`.

> export const DEFAULT_LANE_BUDGETS: LaneTokens = {contexts: 4000, stubs: 500, summaries: 2000}
> --- `src/server/core/domain/knowledge/summary-types.ts`

The manifest service can consume a sidecar, but the inspected internal query constructor supplies only baseDirectory. That call's rebuild therefore uses default importance, not necessarily the ranking signals used by search. Estimated lane allocation is not a hard token cap over the final assembled prompt.

#### MEM-OBJ-summary-index
Label: Hierarchical summary files

`_index.md` stores derived natural-language directory summaries plus symbolic frontmatter: children hash, covered paths, condensation order and token/compression metadata. Filesystem content derives from direct markdown leaves and immediate child summaries, skipping derived artifacts/archive stubs. Generation can use an agent or deterministic fallback. Consumers include manifest injection and search summary propagation. This is a part of the retained tree with distinct derivation and stale-child checks, not a copy of the whole topic container.

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

SRC-1, `src/server/infra/context-tree/file-context-tree-summary-service.ts`, `src/server/core/domain/knowledge/summary-types.ts`, `src/agent/infra/tools/implementations/search-knowledge-service.ts`.

> if (entry.isFile() && entryName.endsWith(CONTEXT_FILE_EXTENSION)) {
>   // Skip _index.md itself and derived artifacts
>   if (entryName === SUMMARY_INDEX_FILE) continue
>   if (isDerivedArtifact(relativePath) || isArchiveStub(relativePath)) continue
> --- `src/server/infra/context-tree/file-context-tree-summary-service.ts`

The markdown extension condition prevents treating this collector as a demonstrated summary path for newly authored HTML. Curation's deferred work and folder-pack summary propagation were located, but all queue execution and recovery paths were not traced. Prompting a summary to preserve facts does not establish fidelity or rationale preservation.

#### MEM-OBJ-file-abstract
Label: Per-file abstract

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

`.abstract.md` siblings are filesystem-derived natural-language one-line summaries. `generateFileAbstracts`/batch generation ask a configured content generator to summarize bounded source text; the abstract queue writes sibling bytes. Manifest resolution can prefer the abstract over full markdown content. This part differs from the source topic and from the overview consumed by expansion. SRC-1, `src/agent/infra/map/abstract-generator.ts`, `src/agent/infra/map/abstract-queue.ts`, `src/server/infra/context-tree/file-context-tree-manifest-service.ts`.

> const abstractPath = r.contextPath.replace(/\.md$/, '.abstract.md')
> const overviewPath = r.contextPath.replace(/\.md$/, '.overview.md')
> --- `src/agent/infra/map/abstract-queue.ts`

The generation prompt requests at most 80 tokens for the one-line form; input truncation is 20,000 characters per file. These are generation requests, not a semantic guarantee. The inspected sibling naming uses markdown replacement; no claim is made that tool-mode HTML writes universally generate valid sibling abstracts.

#### MEM-OBJ-file-overview
Label: Per-file overview

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

`.overview.md` siblings are a separate derived natural-language filesystem form. They share the abstract generator/queue lineage but not its size or direct consumer: `expand_knowledge` can return an overview when passed its path. A request asks for key points, structure and entities/decisions under 1500 tokens; it does not require all reasons or evidence to survive. This is not a full source-byte reload. SRC-1, `src/agent/infra/map/abstract-generator.ts`, `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`.

> const overviewContent = await readFile(fullPath, 'utf8')
> const originalPath = parsed.overviewPath.replace(/\.overview\.md$/, '.md')
> return {
>   originalPath,
>   overviewContent,
>   tokenCount: estimateTokens(overviewContent),
> }
> --- `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`

#### MEM-OBJ-archive-stub
Label: Archive ghost cue

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

The archive service's `_archived/...stub.md` is a mixed object: natural-language ghost cue plus symbolic `points_to`, original path, timestamp, importance and token metadata. It derives from original content through an LLM cue with deterministic truncation fallback. Search can expose archive-stub results; [MEM-RTE-archive-expansion](#mem-rte-archive-expansion) uses the pointer, not the cue's completeness, to reload full bytes. This is not the tool-mode dream archive, which lives outside the tree and does not create this stub format. SRC-1, `src/server/infra/context-tree/file-context-tree-archive-service.ts`, `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`.

> points_to: toUnixPath(fullRelPath),
> type: 'archive_stub',
> --- `src/server/infra/context-tree/file-context-tree-archive-service.ts`

#### MEM-OBJ-full-archive
Label: Full archive payload

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

`_archived/...full.md` stores verbatim former source bytes, unlike the readable cue. Its representational form follows its source content; wrapper/pointer interpretation is symbolic, while topic prose remains natural language. It is retained for explicit drill-down and restore, not established as automatic in-window knowledge. Restoring writes the original path, deletes stub and full files and seeds default runtime signals; it does not reconstruct prior access history. SRC-1, `src/server/infra/context-tree/file-context-tree-archive-service.ts`; distinct from [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance).

> // Write .full.md — verbatim original content (lossless)
> await writeFile(fullFullPath, content, 'utf8')
> --- `src/server/infra/context-tree/file-context-tree-archive-service.ts`

#### MEM-OBJ-dream-archive
Label: Tool-mode dream archive and recovery metadata

Tool-mode finalize moves selected topic files to `.brv/archive/<path>`, preserving bytes outside the active context tree. It captures previous text, mtime and sidecar signals before rename and returns them for recovery/log consumers. These are natural-language source bytes plus symbolic recovery metadata, not a generated semantic memory. This retained result belongs to [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance), but is distinct from the active tree and stub/full service representation. SRC-1, `src/server/infra/dream/tool-mode/dream-session.ts`.

> return {archived, previousMtimes, previousSignals, previousTexts, skipped}
> --- `src/server/infra/dream/tool-mode/dream-session.ts`

The undo service reads the last completed/partial dream log, reverses operations, rebuilds the manifest best effort and marks the log undone. Full operation-specific restoration/log wiring remains uninspected here; returned metadata alone is not a guarantee of durable log retention or successful undo. SRC-1, `src/server/infra/dream/dream-undo.ts`.

#### MEM-OBJ-compaction-boundary
Label: Compaction summary boundary

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

This object is the retained product of the parent route, not an identity-equivalent route. `StoredMessage` holds natural-language summary text and symbolic boundary/link/session fields in message key storage. The storage loader includes the boundary then stops traversal into older history; context reload supplies that result to subsequent model calls. Summary generation receives at most first five plus last 35 messages, with an omission marker when needed, and a 4096-output-token request. Thus even the summarizer need not see the full raw trace. SRC-1, `src/agent/infra/llm/context/compaction/compaction-service.ts`, `src/agent/infra/storage/message-storage-service.ts`, `src/agent/infra/llm/context/context-manager.ts`.

> compactionBoundary: true,
> compactionSummary: summary,
> content: summary,
> --- `src/agent/infra/storage/message-storage-service.ts`

The boundary is stored as a user-role message; this is a model-input channel assignment, not evidence of human authorship. Summary instructions request decisions and why; successful preservation is unobserved. Error fallback strings can also be returned by the generator helper, so a retained boundary is not proof of a meaningful summary.

#### MEM-OBJ-checkpoint-progress
Label: Rolling checkpoint progress

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

This is the parent's alternative retained product, not its full-summary form. `__checkpoint_progress` holds JSON in the task sandbox: symbolic message count, unique tool names and call count, plus natural-language prefixes of the last three nonempty assistant contents, each sliced to 300 characters. It derives automatically from the current trace. After history clear the continuation contains current time, a 200-character original-task prefix and instructions to read the variable through code execution. Later task model calls are the consumer; actual reload is model-directed and unobserved. SRC-1, `src/agent/infra/llm/agent-llm-service.ts`.

> return JSON.stringify({
>   assistantSummaries: assistantMessages.slice(-3),
>   messageCount: messages.length,
>   toolsUsed: [...new Set(toolCalls)],
>   totalToolCalls: toolCalls.length,
> })
> --- `src/agent/infra/llm/agent-llm-service.ts`

Persistence is across history clears within the task sandbox, not established across task deletion or process restart. This compact trace can omit reasons, tool outcomes and earlier assistant decisions. It is not equivalent to storing the original conversation or to semantically evaluating it.

### Routes

#### MEM-RTE-topic-read
Label: Focused topic read

The CLI read command resolves project root and calls `readTopic` on a caller-supplied relative path. It reads disk directly, returning rendered HTML or unchanged non-HTML bytes; `--raw` bypasses rendering. The documented consumer is the curate skill's update author. This is a distinct alternative to ranked query, not a duplicate of [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval). SRC-1, `src/oclif/commands/read.ts`, `src/oclif/lib/read-topic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Topic content/format/path or structured unsafe-path, not-found or read-failed error.
- Later read-back: Previously retained topic content reaches a later CLI caller, including an update author before merged replacement.
- Delegated visibility: Rendered markdown by default for HTML, or original source bytes on explicit raw request.
- Selection predicate: Explicit caller path, not relevance ranking or automatic discovery; lexical path checks precede I/O.
- Invalidation or expiry: Each call reads current disk bytes; replacement/removal affects subsequent calls, subject to filesystem behavior.
- Activation or effect: Supplies prior content; no evidence that a caller merges accurately or changes reliance.
- Evidence limits: No caller transcript; path checks are not proof of symlink containment or human identity.

> const format = relPath.toLowerCase().endsWith('.html') ? 'html' : 'markdown'
> const content = format === 'html' && !options.raw ? renderHtmlTopicForLlm(raw) : raw
> --- `src/oclif/lib/read-topic.ts`

#### MEM-RTE-search-recall
Label: Search recall alternatives

CLI search dispatches a daemon search task; registered `search_knowledge` invokes the service with query and options. The service supports text ranking and symbolic path navigation, summary propagation, scope and kind/maturity filters. These return excerpts/paths for a caller to choose further reads. Distinct from the public query route, which additionally filters local origin and loads/renders full matches. SRC-1, `src/oclif/commands/search.ts`, `src/agent/infra/tools/implementations/search-knowledge-tool.ts`, `src/agent/infra/tools/implementations/search-knowledge-service.ts`; closest supplied record is [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked search result envelope with paths, scores, excerpts and totalFound, or overview/navigation result according to options.
- Later read-back: Retained topic/summary/cue content is recalled as search metadata and readable excerpts for later callers.
- Delegated visibility: Search results are not a byte-complete source read; the service directs callers to read_file for full content.
- Selection predicate: Query terms or symbolic paths, requested limit/scope/filters; BM25-derived score blended with decayed sidecar signals and local-origin preference, plus summary propagation.
- Invalidation or expiry: Search index has a TTL/rebuild/invalidation lifecycle; access-hit flush can occur at index acquisition. No immediate all-write freshness guarantee.
- Activation or effect: Supplies candidate memory and records returned-hit activity; caller choice and factual usefulness remain unobserved.
- Evidence limits: Not every symbolic selector branch or shared-source failure path was traced; registration and handler code do not prove deployed grants or exercised use.

> message:
>   results.length > 0
>     ? `Found ${searchResults.length} result(s). Use read_file to view full content.`
>     : 'No matching knowledge found. Try different search terms or check available topics with /query.',
> --- `src/agent/infra/tools/implementations/search-knowledge-service.ts`

#### MEM-RTE-signal-feedback
Label: Access signal feedback

Search service accumulates returned-result hits, later flushes them into the sidecar, and loads sidecar state for subsequent scoring. Maintenance also reads it. This route is distinct from [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval): its retained output is access metadata rather than delivered topic prose. SRC-1, `src/agent/infra/tools/implementations/search-knowledge-service.ts`, `src/server/infra/context-tree/runtime-signal-store.ts`, `src/server/infra/dream/tool-mode/prune-candidates.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search returns results; a later flush snapshots and clears pending hits and attempts batch updates.
- Later read-back: Retained importance/accessCount/maturity affect later compound scoring and prune eligibility; this closes a trace-to-derived-metadata-to-later-selector chain.
- Delegated visibility: The caller receives results, not a guarantee that every delivered hit's metadata is durable; selectors consume numerical signals rather than reasons for use.
- Selection predicate: Returned result paths, mapping synthetic summaries to their actual summary file; count drives importance/accessCount bumps and maturity recalculation.
- Invalidation or expiry: Archive can delete signals; archive-service restore seeds defaults; missing/corrupt reads default. Pending in-memory hits and best-effort failures can lose updates.
- Activation or effect: Code applies activity-derived ranking/maintenance inputs. Changed ranking in a run and improved future performance are unobserved.
- Evidence limits: Hits measure selection, not confirmed reading, approval or successful task outcomes; query-cache reuse need not traverse the search-hit path.

> const bumped = recordAccessHits(current, count)
> return {
>   ...current,
>   accessCount: bumped.accessCount,
>   importance: bumped.importance,
>   maturity: determineTier(bumped.importance, current.maturity),
> }
> --- `src/agent/infra/tools/implementations/search-knowledge-service.ts`

Admission is automatic software computation over usage traces, not per-content human approval or model semantic revision. Store schema validation can veto invalid updated records; persistence failure is fail-open for search. There is no factual answer oracle or outcome-based score in these inspected updates. An open search request triggers activity; numeric tier promotion does not establish validated knowledge. The prune generator skips core maturity, then checks importance and mtime; a calling agent still decides whether to archive. These fields have direct selection authority without acquiring semantic truth authority.

#### MEM-RTE-manifest-injection
Label: Internal manifest injection

Internal `executeWithAgent` obtains/builds a fresh manifest and resolves its selected entries into broad structural context, then places that context in the task prompt. This adds a read-back route to the internal query family discussed in [RT-RTE-context-control](runtime.md#rt-rte-context-control); it is not the same referent as public tool-mode retrieval. SRC-1, `src/server/infra/executor/query-executor.ts`, `src/server/infra/context-tree/file-context-tree-manifest-service.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Internal execution eventually returns an answer; manifest acquisition failures are swallowed and execution continues without this context.
- Later read-back: Persisted summary/context/stub content reaches a later internal model invocation as prompt text.
- Delegated visibility: Selected entries only; resolver prefers abstract siblings, skips unreadable entries and orders summaries, contexts, then stubs.
- Selection predicate: Internal query branch triggers code selection; manifest lanes use order/importance/budget, not query relevance. Resolver's _query argument is unused.
- Invalidation or expiry: Freshness check may rebuild the manifest; summary/fingerprint compatibility and alternate writes prevent a universal freshness conclusion.
- Activation or effect: Automatic context supply within the requested internal query; actual model reliance is unobserved.
- Evidence limits: Not unsolicited knowledge delivery independent of a request; tool-mode query bypasses this branch, and markdown-derived manifest coverage does not establish HTML coverage.

> const resolved = await manifestService.resolveForInjection(manifest, query, this.baseDirectory)
> if (resolved.length > 0) {
>   manifestContext = resolved.map((e) => `[${e.type} ${e.path}]\n${e.content}`).join('\n\n---\n\n')
> }
> --- `src/server/infra/executor/query-executor.ts`

#### MEM-RTE-archive-expansion
Label: Archive and overview expansion

Registered `expand_knowledge` parses exactly one stubPath or overviewPath; the latter reads an overview, the former calls archiveService.drillDown and returns full bytes. This is an exposed, source-wired tool operation, not evidence a particular query task has been granted or invoked it. It is distinct from [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance), which does not produce this stub format. SRC-1, `src/agent/infra/tools/tool-registry.ts`, `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`, `src/server/infra/context-tree/file-context-tree-archive-service.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Overview content or full archive content, original path and estimated token count; parse/read errors can fail the call.
- Later read-back: Previously retained derived overview or archived source material can re-enter an agent's context through a tool result.
- Delegated visibility: Overview is lossy; fullContent follows the stub's points_to reference and is the retained original payload.
- Selection predicate: Caller explicitly supplies a path; stub parser resolves points_to. No independent relevance selector is established in the expansion call itself.
- Invalidation or expiry: Restore deletes the stub/full pair; later replacement/removal can make expansion fail. No enforced content-size budget appears in this operation.
- Activation or effect: Exposes reload of out-of-window material; actual invocation, reliance and benefit are unobserved.
- Evidence limits: Tool availability depends on grants/command filtering; archive writer API alone does not establish who populated each archive or a mandatory automatic withdrawal cycle.

> const result = await archiveService.drillDown(parsed.stubPath, config.baseDirectory)
> return {
>   fullContent: result.fullContent,
>   originalPath: result.originalPath,
>   tokenCount: result.tokenCount,
> }
> --- `src/agent/infra/tools/implementations/expand-knowledge-tool.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission)

The retained semantic result and access metadata must be separated. Successful new writes seed default signals; rewrites bump importance/recency/updateCount and recompute maturity best effort. These are automatic write-history transformations, not criticism of the stored claim. The log's human-readable reason/summary and review status are a separate recovery/approval surface; the readable topic can already reach local consumers while review is pending. Supplied backup/reject passages establish restoration dependence and failure limits. SRC-1, `src/server/infra/context-tree/tool-mode-sidecar-updaters.ts`, `src/server/infra/process/curate-html-log.ts`; see [MEM-OBJ-runtime-signals](#mem-obj-runtime-signals) and [MEM-OBJ-bv-reason](#mem-obj-bv-reason).

#### On [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval)

MCP provides another delivery adapter to the same deterministic daemon route: it renders each envelope match as a title and rendered_md body into text tool content. It does not establish model synthesis within ByteRover. SRC-1, `src/server/infra/mcp/tools/brv-query-tool.ts`.

> const heading = doc.title.trim().length > 0 ? doc.title : doc.path
> return `## ${heading}\n\n${doc.rendered_md}`
> --- `src/server/infra/mcp/tools/brv-query-tool.ts`

Selection is request-led, with code ranking/filtering. The ordinary limit is document count, not a universal token budget; the default is ten and the maximum fifty. Cache storage and invalidation are qualified in [MEM-OBJ-query-cache](#mem-obj-query-cache). Shared hits may contribute upstream search activity yet be filtered before public query delivery; returned-hit metadata is therefore not proof of downstream reading.

#### On [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Direct inspection resolves part of the supplied compaction-service uncertainty. Overflow defaults to 85%; beyond 95% it recommends full compaction rather than pruning. Pruning budgets retain 20% of the model window in tool outputs, require at least 10% recoverable savings, and protect two recent user turns by default. Message reconstruction substitutes a compacted-output placeholder. Full-summary input itself is bounded to forty history messages; the stored boundary is included during subsequent reload. SRC-1, `src/agent/infra/llm/context/compaction/compaction-service.ts`, `src/agent/infra/storage/message-storage-service.ts`, `src/agent/infra/llm/context/context-manager.ts`.

> if (stopAtCompaction && storedMsg.compactionBoundary) {
>   orderedMessages.unshift(storedMsg)
>   hitCompactionBoundary = true
>
>   break
> }
> --- `src/agent/infra/storage/message-storage-service.ts`

The parent phrase “only post-boundary messages” should not imply that the summary boundary is discarded. Its own content survives with later turns. The separate rolling checkpoint retains sandbox progress and replaces history with a pointer-like instruction, not an automatically dereferenced memory. [MEM-OBJ-compaction-boundary](#mem-obj-compaction-boundary) and [MEM-OBJ-checkpoint-progress](#mem-obj-checkpoint-progress) distinguish those products. Session framing resembles selected-input/return-value isolation, but writes can escape into persistent topics, and a sandbox variable name is not an automatically followed reference. Task/session cleanup does not prove cross-run durability.

#### On [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance)

Direct loader inspection narrows the candidate inventory: this route loads `.html` files with a bv-topic root and title, not every retained markdown/summary/stub format. Prune excludes core topics, defaults to importance below 35 or stale draft/validated mtimes of 60/120 days, sorts stalest first and defaults to twenty candidates. These are activity/age proxies for agent review, not proof of obsolescence. SRC-1, `src/server/infra/dream/tool-mode/topic-loader.ts`, `src/server/infra/dream/tool-mode/prune-candidates.ts`.

> if (t.signals.maturity === 'core') continue
> --- `src/server/infra/dream/tool-mode/prune-candidates.ts`

The source-supported retained removal result is [MEM-OBJ-dream-archive](#mem-obj-dream-archive), not a generated summary or the stub/full archive service. Semantic survivor edits still depend on the caller and their separate admission. Preserved previousTexts/mtimes/signals support recovery and next scan state; complete CLI undo persistence and execution remain unestablished.

## Write side

**Acquisition and authorship.** Public CLI/MCP input and internal model-generated topics have different authors but can share the HTML writer's structural admission. Neither generic caller identity nor an initiating human command proves per-content human editing or approval. Overwrite flags are caller policy, not authenticated human authorization. Internal generation uses a task frame and enables overwrite. Direct editing, hub bundles and Cloud pull have separate admissions and provenance: client bytes, publisher artifacts and remote snapshot content respectively. The supplied [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit), [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) and [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) supply the contrary cases to universal writer validation. Their semantic content is not made trustworthy by local persistence.

**Transformation.** Rendering preserves selected rule/decision/reason semantics but omits unsupported markup. It changes delivery form, not the stored assertion's warrant. Abstracts, overviews and hierarchical summaries are requested condensations with partial source coverage and possible truncation/fallback; no mandatory complete reasons trail is established. The full source can remain separately available through direct read or archive drill-down. See [MEM-OBJ-file-abstract](#mem-obj-file-abstract), [MEM-OBJ-file-overview](#mem-obj-file-overview) and [MEM-OBJ-summary-index](#mem-obj-summary-index). Generation APIs and queue write sites establish capacity and partial wiring, not that all current tool-mode writes generate these artifacts.

**Automatic trace-fed retention.** [MEM-RTE-signal-feedback](#mem-rte-signal-feedback) traces returned hits to persisted metadata to later ranking/maintenance. Curate rewrites separately bump write-history metadata. Neither writes a semantic revision justified by outcome evaluation. Full compaction and rolling checkpoints do create derived behavior-shaping content from conversation traces for later invocations: raw messages → selected summary/snippets → boundary or sandbox variable → subsequent model context/reload. Rationale is requested in full-summary guidance but not guaranteed; rolling snippets do not preserve a complete reason chain. These are distinct from raw query/curate logs, whose retention alone establishes no such semantic update. The internal generator's model mutability and opaque weights remain as specified in [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator), not inferred from the sidecar's numerical fields.

**Maintenance, rejection and withdrawal.** Dream's structural candidates are software proposals, not final semantic verdicts. The caller selects merge/link/prune/synthesis changes and survivor writes; finalize checks paths and moves selected losers. Archive retains bytes outside the active tree. The separate archive service can preserve searchable cues and reloadable full payloads, so withdrawal from the active tree need not mean irrecoverable deletion. Review is conditional and post-write: reject restores backup or deletes an addition; backup failure can destroy the expected restoration path. Cloud push review filtering is not local-read gating. Undo has explicit retained prior-state consumers but remains bounded by supplied logs and partial failures. These mechanisms offer recovery, not one transaction across content, logs, sidecars, derived index and cache.

## Read-back

The public chain is **caller request → deterministic selection → local-file load/render → CLI envelope or MCP text → external caller synthesis**. Rule severity remains prose at that consumer. Focused read is an independent path: it uses the caller's exact path, bypasses ranked selection and cache, and can return raw bytes. Its update-author consumer can then propose replacement material; reading is not itself admission. The search command/tool returns narrower excerpts and navigation aids; full material requires another operation. These distinctions are supported by [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval), [MEM-RTE-topic-read](#mem-rte-topic-read) and [MEM-RTE-search-recall](#mem-rte-search-recall).

Internal query's manifest supply is automatic **inside a requested execution**, not evidence of unsolicited content push. Its selector uses retained structure and lane budgets, not the query text passed to the unused resolver argument. Different code controls the public document-count limit, manifest token estimates, full-summary message/output bounds and rolling checkpoint trigger. No single context-budget number describes all routes. The pre-prompt hook loads shipped `brv-instructions` and writes them to stdout; this is static workflow supply, not dynamic retrieval of accumulated knowledge (SRC-1, `src/oclif/commands/hook-prompt-submit.ts`).

Re-entry of removed context has two explicit forms: a summary boundary arrives in later model input automatically; a rolling checkpoint or archive pointer requires an explicit access operation. The former is implemented message loading; the latter still requires a model/caller to use the afforded reload. [MEM-RTE-archive-expansion](#mem-rte-archive-expansion) exposes overview or full archived content but does not establish command grants. All consumer authority conclusions stop short of observed reliance or improved performance.

## Integration issues

1. **Summary-boundary precision.** [RT-RTE-context-control](runtime.md#rt-rte-context-control) says reload contains only post-boundary messages, but `loadMessages` includes the boundary before stopping. [MEM-OBJ-compaction-boundary](#mem-obj-compaction-boundary) establishes that the retained summary itself survives. Interpret the parent phrase as dropping pre-boundary history, not the summary. No other generic route progression is changed.
2. **HTML freshness.** [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) already disclaims immediate freshness; [MEM-OBJ-query-cache](#mem-obj-query-cache) adds a stronger implementation-specific limit: the fingerprint scans markdown, so HTML-only changes need not change it. TTL, not a demonstrated HTML-aware invalidation edge, bounds reuse. This prevents treating reject/archive as immediate withdrawal from cached delivery. An exercised stale answer remains unobserved.
3. **Format-divergent memory planes.** [MEM-OBJ-summary-index](#mem-obj-summary-index), [MEM-OBJ-file-abstract](#mem-obj-file-abstract) and [MEM-OBJ-context-manifest](#mem-obj-context-manifest) expose markdown-oriented derivation/naming, while [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) loads HTML. Exact coverage of migrated mixed-format projects and all generation callers is unresolved; neither plane may silently stand for every topic.
4. **Archive identities.** [MEM-OBJ-dream-archive](#mem-obj-dream-archive) is the retained result of the supplied dream route, not a duplicate of it. [MEM-OBJ-archive-stub](#mem-obj-archive-stub) and [MEM-OBJ-full-archive](#mem-obj-full-archive) describe a separate service format. Their write API is inspected, but ordinary automatic archiveEntry caller wiring was not established. Expansion registration establishes exposed reload capacity, not a deployed write/read cycle. Full undo log construction and per-operation branches remain unresolved.
5. **Sidecar injection difference.** [MEM-RTE-signal-feedback](#mem-rte-signal-feedback) reads live sidecar inputs for search, but the internal query manifest constructor supplies no signal store. [MEM-RTE-manifest-injection](#mem-rte-manifest-injection) must not inherit search's activity-based prioritization without that dependency. This is not an inconsistency in the supplied public-query record.
6. **Coverage left open.** Detailed ingest/map/swarm write provenance, Git VC/worktree/migration replacements, connector host loading, alternate compression branches and evaluator-to-write consumers remain uninspected. Their named inventory prevents whole-system uniform-admission, complete-reload and freshness conclusions. Excluded dependency/provider/host internals separately prevent deployed-loop conclusions. These are limits, not absence records or evidence of defective behavior.

All new declarations identify parts or distinct stores/routes relative to their closest supplied records. No identity-equivalent duplicate is intentionally declared; reconciliation should retain the topic container alongside its semantic/metadata parts and the context-control route alongside its two retained products.

## Limitations and checks

The source identity, commit and clean checkout were rechecked before inspection. Only the supplied method/type/collection contracts and SRC-1 source text were used; no prior analyses or other run state were consulted. The current method contract is the supplied invocation, not an inferred version from target documentation. The coverage table separates direct reads, inherited evidence and named uninspected responsibilities.

Source supports retention, selection and transformation wiring, not exercised compliance, factual correctness, safe deployment, measured improvement or causal benefit. Human semantic control is unresolved wherever a generic caller supplies bytes. Physical I/O success does not establish multi-artifact consistency, and a tool's registration does not establish every runtime grant. No theory-builder, learning-benefit or self-improvement conclusion is inferred from persistence or revision labels.

Validation: the supplied validate-output command reported “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The initial drafting placeholder was removed; no finding was narrowed or withdrawn to pass the check.
