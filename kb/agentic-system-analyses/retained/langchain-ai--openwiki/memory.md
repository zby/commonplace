---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenWiki memory: generated Markdown, Claims freshness, resumable plans, chat checkpoints and trace-fed updates."
run-id: AAS-2026-10-14-openwiki-8f502f680f75-01
source-identity: "https://github.com/langchain-ai/openwiki"
reviewed-boundary: "7c469e59584bfac3f97f5c32a67604de46805999"
---

# OpenWiki memory report

## Boundary and evidence

This report covers OpenWiki's retained knowledge and context-control surfaces at the frozen commit in [boundary](boundary.md). It includes repository and personal wiki production, Claim sidecars and projections, resumable assignments, raw connector evidence, trace-derived documentation, chat checkpoints, filesystem conversation-history offload, requested retrieval, human visualization and shipped evaluation consumers. External host memory, provider parameters, dependency-owned summarization and live connector services are not inspected implementations. Their absence from the capture prevents conclusions about their exact state formats, compaction algorithms, compliance or outcomes, not conclusions about inspected OpenWiki wiring.

The runtime input is provisional. Its records supply source passages for native/host generation, personal ingestion, translation, setup and retrieval. Direct reads added Claims schemas/session/preflight/runtime, page-manifest code, retrieval ranking and extraction, connector I/O/raw read tools, LangSmith sampling/compaction, code-mode connector injection, graph checkpoints/pruning, interactive thread reuse, visualization graph construction and evaluator artifact transfer. Correction-round direct reads added the shared agent backend, OpenWiki home-directory resolution, planner/page and chat backend construction, and the complete source-native conversation-history offload test. These tests were read, not run; they establish an intended dependency contract, not observed offload. All added evidence is SRC-1 implementation or source-native doctrine/design. No target execution, test, supplied trace or experiment establishes exercised memory, semantic accuracy or benefit.

### Coverage

| Entry point or operation | SRC-1 source paths | Coverage and limits |
| --- | --- | --- |
| CLI repository init/update; host begin/plan/next/submit/finish | `src/agent/index.ts`, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`, `src/integrations/core/session-manager.ts` | Supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation), [RT-RTE-host-generation](runtime.md#rt-rte-host-generation); direct next/inspect/snapshot reads; annotations below. Native isolated attempts and host-managed contexts differ. |
| Persisted plan and semantic assignments | `src/generation/run-state.ts`, `src/agent/repository-prompts.ts` | Supplied [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state), [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance); annotations distinguish code state from model guidance. |
| Claims acquisition, reconciliation, reload, stale checks, deletion and verification projection | `src/claims/core/types.ts`, `src/claims/core/mutations.ts`, `src/claims/brains/code/store.ts`, `src/claims/brains/code/session.ts`, `src/claims/brains/code/preflight.ts`, `src/claims/brains/code/runtime.ts` | Direct schemas, working state, persistence and model-display reads; [MEM-OBJ-claim](#mem-obj-claim), [MEM-OBJ-evidence](#mem-obj-evidence), [MEM-OBJ-page-claims](#mem-obj-page-claims), [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation). Resolver internals remain uninspected here: no semantic entailment claim. |
| Per-page source coverage and finalization | `src/generation/page-manifest.ts`, `src/generation/repository-run.ts`, `src/agent/okf-middleware.ts` | Direct manifest schema/I/O and middleware; supplied durability/finalization in [RT-CLM-page-durability](runtime.md#rt-clm-page-durability). [MEM-OBJ-page-manifest](#mem-obj-page-manifest). Detailed index/link/provenance algorithms remain supplied runtime findings, not independently certified. |
| Personal init/update/chat and deterministic pulls | `src/ingestion/ingestion.ts`, `src/agent/prompts/personal.ts`, `src/connectors/io.ts`, `src/connectors/tools.ts`, `src/agent/index.ts` | Direct prompt/search, raw storage/read and graph wiring; [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion) annotation; [MEM-OBJ-connector-data](#mem-obj-connector-data). Individual Gmail/Slack/X/Notion/etc. transforms and deletion/cursor policies uninspected; prevents uniform lineage, expiry or synchronization claims. |
| Configured MCP admission/read paths | `src/connectors/mcp-runtime.ts`, `src/connectors/mcp-client.ts` | Supplied [RT-RTE-mcp-connector](runtime.md#rt-rte-mcp-connector), [RT-CLM-mcp-policy](runtime.md#rt-clm-mcp-policy); raw read inspected. External payload meaning and server effects unresolved. |
| Code-mode LangSmith pull and synthesis | `src/ingestion/code-mode.ts`, `src/ingestion/ingestion.ts`, `src/connectors/sources/langsmith/index.ts`, `src/connectors/sources/langsmith/runs.ts` | Direct sampling, compact persisted trace and guidance; [MEM-OBJ-trace](#mem-obj-trace), [MEM-RTE-trace-documentation](#mem-rte-trace-documentation). API internals uninspected; privacy guidance is not semantic enforcement. |
| Native history offload and backend reload | `src/agent/agent-backend.ts`, `src/config/openwiki-home.ts`, `src/agent/repository-runner.ts`, `src/agent/index.ts`, `test/agent/conversation-history-offload.test.ts` | Direct mount, home-directory, worker/chat construction and complete offload-test reads; [MEM-OBJ-conversation-history](#mem-obj-conversation-history), [MEM-RTE-history-offload](#mem-rte-history-offload). Home filesystem retention is separate from SQLite and queue state. Dependency trigger, payload, automatic reload, expiry and cross-worker use remain unresolved; no executed test or actual offload is claimed. |
| Chat persistence and cleanup | `src/agent/index.ts`, `src/cli/app/app.tsx` | Direct checkpointer configuration, finally-hook pruning and same-session thread use; [MEM-OBJ-chat-checkpoint](#mem-obj-chat-checkpoint), [MEM-RTE-chat-continuation](#mem-rte-chat-continuation). Dependency serialized state and any summary/eviction alternatives uninspected. |
| Search and section read through host tools | `src/retrieval/wiki.ts`, `src/integrations/core/retrieval-tools.ts`, `integrations/openwiki/SKILL.md` | Direct ranking/extraction, supplied exposed-tool route [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval), annotation below. Search and direct section reads have different withdrawal filters. |
| Translation middleware | `src/agent/translation-middleware.ts`, `src/agent/index.ts` | Supplied [RT-RTE-page-translation](runtime.md#rt-rte-page-translation), direct graph placement. Semantic preservation and retry-marker details remain supplied source findings, not observed fidelity. |
| Managed instructions, bundled skills, CI publication and scheduling | `src/ingestion/code-mode.ts`, `src/agent/skills.ts`, `.github/workflows/openwiki-update.yml`, `skills/write-connector/SKILL.md` | Supplied [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance). Platform scheduler implementations and other CI examples uninspected: prevents universal publication/recovery claims. Static skills are context supply, not use-derived memory. |
| Visualizer and static export | `src/visualize/graph.ts`, `src/visualize/server.ts`, `src/visualize/static-export.ts` | Graph construction directly read, server searched; [MEM-RTE-visualizer-delivery](#mem-rte-visualizer-delivery). Browser rendering, static-export packaging and update watcher details uninspected; prevents complete UI fidelity/freshness claims. |
| LEDGER capture/evaluate/next checkpoint | `evals/ledger/run/runner.ts`, `evals/ledger/run/evaluate-checkpoint.ts`, `evals/ledger/system/openwiki-system.ts` | Direct runner sequence plus boundary's adapter coverage; [MEM-RTE-ledger-evaluation](#mem-rte-ledger-evaluation). Detailed evaluator scoring/oracle/retention internals uninspected; no measured accuracy or evaluator feedback admission claim. |
| DeepSWE generate/cache/copy/host consumer | `evals/deepswe/openwiki_codex.py` | Direct transfer and cache-related source reads/searches; [MEM-RTE-evaluation-transfer](#mem-rte-evaluation-transfer). External Codex/Harbor execution uninspected; actual uptake and treatment effect prevented. |
| Shipped self-wiki, tests and documentation | `openwiki/INSTRUCTIONS.md`, `openwiki/.claims`, `test`, `README.md`, `AGENTS.md`, `CLAUDE.md` | Boundary/runtime coverage only except supplied passages. Generated self-wiki sidecars and tests are not independently observed results. Individual test bodies and root CLAUDE content uninspected here. |

The inventory names unresolved included alternatives rather than treating them as absent. No source access gap was encountered. Available but unread algorithms remain inspection limits.

## Core ideas

1. **Knowledge and control are separate retained parts.** Markdown and Claim statements are interpreted language; Claim IDs, versions, hashes, queue statuses and manifest entries have fixed code consumers. A JSON file can contain both forms. The page is the downstream knowledge surface; its sidecar primarily supports the next maintenance decision, not the section reader. See [MEM-OBJ-wiki-page](#mem-obj-wiki-page) and [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation).
2. **Selective maintenance avoids transferring all previous research.** Native planner/page attempts are fresh contexts. The next assignment supplies issue-bearing Claims and a count, with the full compact set available on demand. Persisted page guidance and artifacts cross stages; fresh graphs do not restore predecessor conversations through a repository-generation checkpointer. However, every native planner/page backend also mounts durable home-directory conversation history, with direct middleware writes and backend read-back afforded separately from model-facing write grants. This prevents treating worker exit as erasure of all conversation-derived material. Payload semantics and cross-worker selection/use remain unresolved. This is frame-like initial isolation, not shared pointers or exclusive artifact retention: returned text enters a new context by value. See [MEM-OBJ-conversation-history](#mem-obj-conversation-history) and [MEM-RTE-history-offload](#mem-rte-history-offload). Supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation), direct `src/generation/repository-run.ts` (SRC-1).
3. **Retrieval progressively exposes retained prose.** Search rebuilds a lexical index from current Markdown, emits compact references, and a later explicit read supplies entire selected sections. This is not summary storage, learned embeddings or automatic startup preload. Bounds constrain query/results/excerpts, not the total size of complete section reads. See annotation on [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval).
4. **Trace-fed documentation is a separate transformation, not chat compaction.** Code selects anomalous operational traces, persists reduced structure/metrics/errors, and asks a model to turn them into source-linked runtime findings. Those pages may later enter coding-host context. This is implemented evidence-fed document maintenance, not demonstrated improved capacity. See [MEM-RTE-trace-documentation](#mem-rte-trace-documentation).
5. **Withdrawal is consumer-relative.** Retracting a Claim removes current Claim state. A deprecated page is excluded from search, but direct section reads do not repeat that status filter. Checkpoint pruning removes old database snapshots, not necessarily old turns inside the surviving state. These countercases prevent global claims of semantic withdrawal or context compression. SRC-1, `src/claims/core/mutations.ts`, `src/retrieval/wiki.ts`, `src/agent/index.ts`.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki-page
Label: Generated wiki page

Source-native identity: repository `openwiki/` Markdown pages and personal local-wiki pages. Representational form: natural-language body, titles and descriptions; substrate: filesystem Markdown. Model/host authoring derives prose from repository files, connector evidence and existing pages. Deterministic metadata/index/provenance transformations also change bytes. The prose is distinct from the plan in [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance) and the run checkpoint in [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state); neither supplied object is this retained output. SRC-1, `src/agent/okf-middleware.ts`, `src/retrieval/wiki.ts`, `src/agent/prompts/personal.ts`; supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

Consumers: future authoring agents, requesting retrieval hosts, personal chat, human visualizer and evaluation drivers. At downstream model consumers prose is context/evidence under shipped guidance, not executable policy. Files may nevertheless influence interpreted decisions; delivery establishes no activation. At future authors, existing text supplies material to preserve, revise or supersede. Horizon: filesystem persistence across sessions until changed/deleted. Reasons and source links can survive in prose, but no inspected admission check requires a complete argument or revision history.

> stamps final code-owned `generated` provenance on every new or changed page.
> --- `src/agent/okf-middleware.ts`

#### MEM-OBJ-claim
Label: Claim statement

Source-native identity: `Claim.statement` keyed by a stable ID. Representational form: natural-language factual proposition; substrate: current page JSON sidecar and process-local ClaimSession. Lineage: model/host add/update, later confirm/retract. The closest supplied durability record [RT-CLM-page-durability](runtime.md#rt-clm-page-durability) is a guarantee about persistence order, not this object; no supplied object counterpart. SRC-1, `src/claims/core/types.ts`, `src/claims/brains/code/store.ts`, `src/claims/brains/code/session.ts`.

The maintenance model/host can inspect the statement and associated resource identities to decide sparse operations. Lifecycle code validates nonempty canonical text, not whether its proposition follows from evidence. Downstream section retrieval does not load statements from sidecars. The persisted schema holds current statements, evidence and verification, not a structured criticism/retraction-reason history. Prose can separately retain reasons; that possibility prevents equating absent sidecar rationale fields with universally absent reasons.

> statement: CanonicalNonEmptyStringSchema,
>     evidence: z.array(EvidenceSchema).min(1),
> --- `src/claims/brains/code/store.ts`

#### MEM-OBJ-evidence
Label: Claim evidence identity and version

Source-native identity: `Evidence.resource` and resolver-owned `Evidence.version`. Representational form: symbolic; substrate: page sidecar JSON. Lineage: submitted resource identities are resolved by code, not model-supplied versions. Fixed code uses current resolution versus saved tokens to classify stale/unresolved evidence and reject invalid mutation batches. Semantic adequacy of a cited resource remains outside these comparisons. Distinct from [MEM-OBJ-claim](#mem-obj-claim) by form, consumer and invalidation. No supplied object counterpart; related [RT-CLM-page-durability](runtime.md#rt-clm-page-durability) concerns retention of the containing page Claims. SRC-1, `src/claims/core/types.ts`, `src/claims/core/mutations.ts`, `src/claims/brains/code/preflight.ts`.

Opaque version tokens are durable equality inputs, not model-readable reasons. The compact model display intentionally omits versions and supplies resource IDs plus issues. Source content is resolved separately; the persisted sidecar is not a verbatim evidence archive.

> evidence: claim.evidence.map(({ resource }) => resource),
> --- `src/claims/brains/code/session.ts`

#### MEM-OBJ-page-claims
Label: PageClaims persistence envelope

Source-native identity: `PageClaims` containing schema discriminator, Markdown hash, Claims and optional verification event. Representational form: symbolic envelope; substrate: repository `.claims` JSON sidecars. Semantic Claim statements and evidence parts are separately declared above, not merged into a uniformly symbolic object. Lineage: strict finalize persists only rechecked dirty state; refresh synchronizes hashes after deterministic metadata edits. Consumer: ClaimsStore/session/lifecycle, with verification projected into Markdown for display. Distinct from transient [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state); related durability claim is not an object duplicate. SRC-1, `src/claims/brains/code/store.ts`, `src/claims/brains/code/runtime.ts`.

> schemaVersion: z.literal(CODE_CLAIMS_SCHEMA_VERSION),
>     pageVersion: z.string().regex(/^sha256:[a-f0-9]{64}$/u),
>     claims: z.array(ClaimSchema),
>     verification: VerificationSchema.optional(),
> --- `src/claims/brains/code/store.ts`

The `by`/`at` verification event and page hash support attribution/version association, not independent semantic truth. Failed version refresh can roll back projected verification stamps. The schema is strict; unrecognized rationale or history fields are not part of this persistence contract.

#### MEM-OBJ-page-manifest
Label: RepositoryPageManifest

Source-native identity: committed `.page-manifest.json` page coverage ledger. Representational form: symbolic; substrate: local JSON file, optionally retained in Git. Each page entry records Markdown hash and optional source HEAD/fingerprint, producer and completing run. Lifecycle code reloads this to reconstruct/advance coverage. It is distinct from transient [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state); a durable page ledger survives finish while `.run.json` is deleted. SRC-1, `src/generation/page-manifest.ts`, `src/generation/repository-run.ts`.

> * Hash of the exact Markdown bytes whose Claims were verified.
> --- `src/generation/page-manifest.ts`

The source-native label “correctness ledger” denotes protocol-proven durable coverage, not measured page correctness. Code validates the schema and atomically replaces the manifest; legacy entries can lack source fingerprints/provenance. Admission is deterministic after page durability, not a human statement approval. See supplied [RT-CLM-page-durability](runtime.md#rt-clm-page-durability).

#### MEM-OBJ-connector-data
Label: Connector raw data and state

Source-native identity: connector run directories/raw JSON and `state.json`. Substrate: private local filesystem JSON. Form: mixed source text interpreted by the model and symbolic run/access metadata interpreted by connector tools. Payload provenance and meaning differ by source; opaque MCP results are not established knowledge merely because they are serialized. Raw content and metadata are kept distinct analytically. No supplied object counterpart; closest supplied [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion) is the consuming route. SRC-1, `src/connectors/io.ts`, `src/connectors/tools.ts`, `src/agent/prompts/personal.ts`.

Connector I/O writes fetched payloads; the model reads selected files to synthesize pages. The shared state helper retains the latest 20 run records; that truncation is not evidence of deleting raw files. Source-specific cursor, expiry and payload-replacement behavior remains uninspected. Raw read returns a prefix with a truncation flag; despite the `maxBytes` name, the inspected implementation slices JavaScript string length rather than encoded byte count.

> runs: [run, ...(state.runs ?? [])].slice(0, 20),
> --- `src/connectors/io.ts`

> content: content.slice(0, limit),
>       filePath,
>       truncated: content.length > limit,
> --- `src/connectors/tools.ts`

#### MEM-OBJ-trace
Label: Compacted LangSmith Trace

Source-native identity: `Trace`, persisted in `langsmith-results.json`. Representational form: symbolic execution structure, IDs, metrics and bucket tags plus natural-language names/errors; substrate: raw connector JSON. Lineage: selected external runtime runs → ordered compact trace → persisted project results. These are derived operational records, not full raw conversations. The original served runs are not a supplied observed-run source of this analysis. Distinct specialization of connector payloads with its own traced transformation; no supplied object counterpart, closest [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion) does not identify this code-mode trace object. SRC-1, `src/connectors/sources/langsmith/index.ts`, `src/connectors/sources/langsmith/runs.ts`.

> Inputs/outputs
>  * are never fetched (they are enormous for coding-agent traces and never reach
>  * the committed page), so a compacted run is structure, timings, tokens, and the
>  * truncated error text.
> --- `src/connectors/sources/langsmith/runs.ts`

The model consumes these records as evidence for documentation, not as instructions. Trace URLs preserve a route to external provenance, not frozen source text. Error fields are bounded and interrupted roots do not count as failures. Exact source-system provenance and trust remain external; subsequent derived prose is separately [MEM-OBJ-wiki-page](#mem-obj-wiki-page).

#### MEM-OBJ-chat-checkpoint
Label: SQLite graph checkpoint

Source-native identity: graph checkpoints/writes keyed by thread and namespace. Substrate: `openwiki.sqlite` for chat; `:memory:` SQLite for nonchat graph invocations. Representational form of opaque serialized graph payload: uninspected; known thread/namespace/checkpoint keys and pruning rules are symbolic. Message text, tool results and any dependency-derived summaries cannot be equated without reading dependency state. No supplied object counterpart: [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state) is an explicit repository lifecycle plan, not a graph conversation checkpoint. SRC-1, `src/agent/index.ts`.

> if (command === "chat") {
>     return {
>       connString: checkpointPath,
>       persistent: true,
>     };
>   }
> --- `src/agent/index.ts`

Chat graph calls can reuse a thread and hence latest persisted state; the native repository generation branch instead uses fresh uncheckpointed worker contexts. Both independently mount the filesystem history surface in [MEM-OBJ-conversation-history](#mem-obj-conversation-history); that surface is not an opaque SQLite payload. Dependency-owned compaction and exact raw-to-summary-to-later-model lineage remain unresolved, but known offload storage, direct-write/read capability and tool-write denial are retained separately in [MEM-RTE-history-offload](#mem-rte-history-offload).

#### MEM-OBJ-conversation-history
Label: Conversation history offload files

Source-native identity: `/conversation_history/` virtual mount backed by `openWikiConversationHistoryDir`, defaulting to `~/.openwiki/conversation_history`, under the configurable OpenWiki home. Substrate: durable home-directory filesystem, outside the documented repository and SQLite checkpoint database. Representational form of actual offloaded payload: uninspected; the source-native test uses readable Markdown text and the backend accepts text, but this does not establish whether deployed payloads are raw messages, derived summaries or mixed material. Lineage: DeepAgents summarization middleware can write directly through the backend; OpenWiki constructs the mount and passes it to native planner/page and personal/chat agents. SRC-1, `src/agent/agent-backend.ts`, `src/config/openwiki-home.ts`, `src/agent/repository-runner.ts`, `src/agent/index.ts`, `test/agent/conversation-history-offload.test.ts`.

The closest supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) describes this channel within generation; it is a route, not an object counterpart. This surface is distinct from [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state), wiki output and [MEM-OBJ-chat-checkpoint](#mem-obj-chat-checkpoint): it has different storage, producer and access controls. Native agents have backend reads of this mount; model-facing filesystem writes are denied, while direct middleware backend writes are not governed by that denial. At a possible model reader, text is interpreted conversation context, not code-enforced wiki policy. Exact selected material, instruction force and exercised consumption remain unresolved. Persistence extends beyond a worker graph's lifetime at the filesystem level; no offload expiry or cross-worker reuse is established.

> [CONVERSATION_HISTORY_MOUNT]: new FilesystemBackend({
>       rootDir: historyDir,
>       virtualMode: true,
>     }),
> --- `src/agent/agent-backend.ts`

> // The summarization middleware writes through the backend directly and
>     // is unaffected by agent-layer permissions (covered by the offload tests
>     // above).
> --- `test/agent/conversation-history-offload.test.ts`

These passages establish the mount implementation and intended distinction between backend and tool grants. The test is source-native contract evidence, not a supplied observed run.

### Routes

#### MEM-RTE-claims-reconciliation
Label: Claims reconciliation and reload

Endpoints: begin/preflight reload → current or issue-bearing Claims → assigned worker/host inspection → sparse operations → resolved current Claim state → strict sidecar persistence/verification → later begin/inspection. Owners: model/host proposes factual edits; core resolves versions, validates IDs/operations, can reject, and performs persistence. This maintenance subflow spans supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) and [RT-RTE-host-generation](runtime.md#rt-rte-host-generation); it is not a duplicate of either complete generation invocation. Context/effects reach Claims, page hashes and verification, not model weights. SRC-1, `src/claims/core/mutations.ts`, `src/claims/brains/code/session.ts`, `src/claims/brains/code/preflight.ts`, `src/claims/brains/code/runtime.ts`, `src/generation/repository-run.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Mutation results with allocated/stable IDs or rejection; inspect returns compact statements/resources/issues; finalization returns durable verification or fails on warnings.
- Later read-back: Next process rebuilds session from sidecars; stale/unresolved issues enter planning and assignments; full compact Claim sets are available through pending-job inspect.
- Delegated visibility: Assigned worker gets issue-bearing Claims and total count, not every current Claim by default; inspect omits opaque versions.
- Selection predicate: Page/job identity plus issue status; preflight checks saved resources against current resolver versions. Explicit inspect selects the full current set for that page.
- Invalidation or expiry: Confirm/update refresh versions; retract removes a stable Claim; deleted/missing/orphan page sidecars are removed on finalization. Source changes yield stale/unresolved issues.
- Activation or effect: Code modifies current Claim state and verification eligibility; subsequent model treatment of statements/issues is requested, not observed.
- Evidence limits: Resource resolution/version identity is not entailment. No supplied run proves criticism quality or successful revision; sidecar rationale history is not present in the inspected strict schema.

Admission is software/model controlled under open init/update requests, not a bounded answer-graded experiment. Starting the run is not per-Claim human approval; generic host authorship leaves human involvement unresolved. There is no predetermined correct proposition supplied by this mechanism. Sparse operations and shared guidance permit add/confirm/update/retract; core rejects invalid IDs/evidence/debt. Native failed attempts can restore page/Claims snapshots under supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation); host edits outside protocol require external recovery. Retraction removes current state, not every prior Git revision or copied page.

> Every dirty page is rechecked against current evidence and its Markdown is
>    * hashed before any sidecar is changed. Unrelated claim state remains intact.
> --- `src/claims/brains/code/session.ts`

> Normal focused updates do not need this payload: current issue-free Claims
>  * are retained deterministically.
> --- `src/generation/repository-run.ts`

#### MEM-RTE-trace-documentation
Label: Trace-fed runtime documentation

Endpoints: code-mode connector pull → anomaly-selected external roots/trees → compact JSON → appended synthesis guidance → planner/page research → retained runtime documentation → later requested wiki context. Code owns sampling/I/O/message injection; model/host owns semantic interpretation/proposal; ordinary repository lifecycle admits pages. Distinct from personal ingestion [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion): LangSmith is registered as code-mode and enriches the repository request. It overlaps native/host generation downstream without duplicating those routes. SRC-1, `src/connectors/sources/langsmith/index.ts`, `src/connectors/sources/langsmith/runs.ts`, `src/ingestion/code-mode.ts`, `src/ingestion/ingestion.ts`; supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pull status/raw file metadata/warnings; successful configured pulls append synthesis guidance to the base request.
- Later read-back: Compact operational evidence can shape retained wiki findings, which later generation/section retrieval can supply to coding agents. Actual findings and their use are unobserved.
- Delegated visibility: Planner gets connector guidance; page guidance is meant to copy only relevant constraints. Raw trace inspection and resulting prose remain model work, not automatic full-trace prompt injection.
- Selection predicate: Window since last documented update; latest 50 roots per project, up to 20 traces prioritizing up to 10 errors and up to 5 nonerror latency outliers with a quarter-pool cap, then recent baseline. Model selects supported findings.
- Invalidation or expiry: Subsequent pulls provide fresh samples; guidance requests incremental/additive refinement and scopes volatile metrics. Connector failure skips enrichment; raw-run retention expiry is uninspected.
- Activation or effect: Automatic selection and persistence are wired; runtime prose is requested through the generation route. Delivered findings' effect on later coding decisions is unobserved.
- Evidence limits: Anomaly composition is not fleet frequency; selected external traces are not OpenWiki execution evidence supplied to this analysis. Semantic criticism, privacy adherence and improvement are not established by guidance.

This is a trace-fed write capacity: external operation → derived operational records → model-curated behavior-relevant documents → later context. It is not a raw-log-only store and not proven learning. The source asks for source-linked checks and implications, but does not supply a reference-answer oracle. Operating mode: recurring open repository updates. Code admits successful pulls; model proposes findings; normal lifecycle can reject malformed/durability-defective pages, not necessarily unsupported semantic implications. Human per-finding approval is not wired before local retention; PR merging is a separate possible gate. Recovery follows normal page snapshots and later source updates. Reasons may survive as trace/code citations and explicit implications in prose; no mandatory structured criticism lineage or observed later reader of those reasons is established.

> - Separate durable from volatile. Structural and behavioral patterns (run shape, tool set, recurring sequences, systemic hotspots) are durable prose; sample-specific metrics (this pull's latency/token figures) are volatile, so scope them clearly as this pull's numbers and keep them where a refresh will not churn the page.
> --- `src/ingestion/ingestion.ts`

#### MEM-RTE-chat-continuation
Label: Chat checkpoint continuation

Endpoints: chat invocation/thread ID → graph checkpointer → persisted latest namespace states → subsequent same-thread invocation; finally-hook prunes old database checkpoints/writes. Owners: OpenWiki selects persistence and thread, dependency graph stores/loads state, OpenWiki code prunes. No supplied route counterpart; repository generation's queue persistence in [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) is a different state/consumer. SRC-1, `src/agent/index.ts`, `src/cli/app/app.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ordinary streamed chat/tool events; pruning emits success/failure debug events.
- Later read-back: Interactive caller reuses sessionThreadId across calls; graph receives that identifier and persistent checkpointer. Exact model-visible restored payload is dependency-owned and uninspected.
- Delegated visibility: Graph streams subgraphs; dependency subagent/checkpoint sharing and any summary contents remain uninspected.
- Selection predicate: command equals chat selects disk persistence; supplied/session thread ID selects namespace history. SQL keeps rank-one latest checkpoint in each namespace.
- Invalidation or expiry: Finally-hook deletes older checkpoint rows and orphaned writes, retaining writes referenced by latest checkpoints or their parents; failures are caught. Nonchat graph storage is in-memory.
- Activation or effect: Persistence/reuse/pruning wiring is inspected; no continuation trace shows a particular remembered fact changing an answer.
- Evidence limits: Database cleanup is not context-window compression. A surviving checkpoint can still hold accumulated turns or dependency-derived material; payload schema and compaction alternatives are uninspected. The independently mounted filesystem history channel is known infrastructure, not merely a possible database payload; SQL pruning does not establish its deletion. See [MEM-RTE-history-offload](#mem-rte-history-offload).

> ROW_NUMBER() OVER (
>                         PARTITION BY checkpoint_ns ORDER BY checkpoint_id DESC
> --- `src/agent/index.ts`

The cleanup is deterministic storage maintenance, not semantic knowledge admission. Model turns/tool results become graph state under dependency control; no additional content approval or answer oracle is supplied by this checkpoint hook. This mechanism retains latest state but deletes history; it cannot prove omission of old content inside that state. Cross-process automatic resumption of a previous UI session is not established merely from disk persistence.

#### MEM-RTE-history-offload
Label: Native history offload and reload

Endpoints: native agent construction → shared home-backed history mount → dependency summarization middleware's direct backend write/edit → durable offload file → possible backend read in a later invocation. OpenWiki owns mount construction/home location and model-facing filesystem grants; dependency middleware owns summarization/offload policy. Included native planner/page agents use the mount without a generation checkpointer; personal/chat agents also use it. This is a distinct cross-cutting storage/access subflow overlapping [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) and [MEM-RTE-chat-continuation](#mem-rte-chat-continuation), not a duplicate of either invocation. SRC-1, `src/agent/agent-backend.ts`, `src/config/openwiki-home.ts`, `src/agent/repository-runner.ts`, `src/agent/index.ts`, `test/agent/conversation-history-offload.test.ts`.

- infrastructure conclusion status: wired
- consumer conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Backend write/edit/read results; source-native tests assert successful offload writes, append-like edits and text read-back, without executing those tests in this analysis.
- Later read-back: The same virtual mount exposes persisted files through backend reads. This is a storage/read capability and intended later summarization/agent access contract, not an established automatic selection/delivery chain or observed cross-worker consumer.
- Delegated visibility: Fresh native worker graphs share the configured history directory, despite separate initial prompts and no generation checkpointer. Which predecessor material a worker could discover/select, and whether any is used, remain unresolved.
- Selection predicate: OpenWiki code maps the fixed history prefix to its configured home directory. Dependency summarization trigger, production retention budget, selected turns/results and automatic reload selector are uninspected; the test's synthetic message threshold is not a production budget.
- Invalidation or expiry: uninspected — the inspected mount/home/worker/test paths do not establish an expiry, rollback or deletion policy for offloaded files; database pruning governs a different substrate.
- Activation or effect: Direct history backend access and model-tool write denial are implemented. Actual offload, compaction of a model window and changed later model behavior are unobserved.
- Evidence limits: Source and unexecuted tests establish known infrastructure and intended direct-write/read-back contract. Dependency payload semantics, raw-to-derived transformation, surviving window tail/pointers, retained reasons, automatic replay and cross-worker reuse remain unresolved.

Admission: this is middleware/dependency state persistence, not repository submit_page or per-content human approval. The model-facing tools cannot author history through the denied write path, but middleware can use direct backend I/O. OpenWiki's source-native test identifies summarization as the intended producer; semantic curation, rejection and recovery within that dependency are uninspected. Operating mode: native working-context management during open generation/chat/update requests, not answer-graded improvement. No reference-answer oracle or per-offload human decision is supplied by mount construction. No automatic trace-fed behavior-shaping summary chain is claimed from an unexecuted contract test alone.

> const read = await backend.read(offloadPath);
>     expect(read.error).toBeUndefined();
>     expect(read.content).toContain("## Summarized at t1");
> --- `test/agent/conversation-history-offload.test.ts`

#### MEM-RTE-visualizer-delivery
Label: Visualizer page delivery

Endpoints: retained wiki directory → collect Markdown → parse metadata/body → graph nodes/edges → visualization consumer. Code constructs graph; human browsing is the intended consumer. Distinct from supplied [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval): it reads page bodies and links rather than query-ranked section refs. SRC-1, `src/visualize/graph.ts`, `src/visualize/server.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Graph object with page metadata, full stripped bodies, links/backlinks and generation time.
- Later read-back: Previously retained Markdown is rebuilt as a graph for a later visualization request; served/browser display specifics remain uninspected.
- Delegated visibility: inapplicable — inspected route has no agent delegation.
- Selection predicate: Real Markdown files under wiki root, excluding named reserved files; links produce edges only to existing nodes, without self-links or duplicates.
- Invalidation or expiry: Deleted/changed files alter the next build; graph build time is not source semantic freshness. Watcher and static-export expiry details remain uninspected.
- Activation or effect: Read-only graph projection; human understanding/decisions are unobserved.
- Evidence limits: Graph construction does not establish browser rendering safety, complete navigation fidelity or semantic validity of pages.

> const nodes = await Promise.all(
>     files.map((file) => readNode(file, wikiRoot)),
>   );
> --- `src/visualize/graph.ts`

#### MEM-RTE-ledger-evaluation
Label: LEDGER checkpoint evaluation

Endpoints: ordered Git source checkpoints → system init/update in continuing worktree → captured wiki artifact/current-plus-historical evidence → evaluation → result/history/carry → next source checkpoint. Runner owns calls/capture/carry; evaluator is a separate consumer. Distinct from native generation [RT-RTE-native-generation](runtime.md#rt-rte-native-generation): this is its shipped evaluator caller, not the same invocation. SRC-1, `evals/ledger/run/runner.ts`; boundary adapter coverage at `evals/ledger/system/openwiki-system.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Checkpoint evaluation results, histories and aggregate score; initial empty wiki is rejected.
- Later read-back: Continuing wiki worktree feeds next update; historical evidence and evaluation carry feed later evaluation calls. Detailed artifact persistence and downstream report consumers remain uninspected.
- Delegated visibility: Evaluator receives captured artifact, evidence corpus, map, checkpoint and carry, not the generation worker's conversation.
- Selection predicate: Benchmark checkpoint order; source evidence records are marked current versus historical. Detailed candidate/watch selection within evaluateCheckpoint is uninspected.
- Invalidation or expiry: Each source checkout replaces source evidence but retained wiki persists; evaluator carry advances independently. Detailed forgotten-version retirement policy is not verified here.
- Activation or effect: Evaluation/carry wiring exists; inspected runner does not pass scores/carry as input to the next system.update call. No measured benefit is established.
- Evidence limits: Evaluator internals/reference-oracle use uninspected; code is not an observed evaluation or causal experiment.

> checkpointResults.push(checkpointResult);
>       history.push(historyEntry);
>       carry = nextCarry;
> --- `evals/ledger/run/runner.ts`

The evaluator diagnoses/checks the artifact under a bounded benchmark sequence. Reference data include evidenceMap and collected current/history records; exactly how these function as answer oracles remains uninspected. Generation proposals/admission remain the normal system route. Evaluation does not become a demonstrated production revision gate merely because it scores artifacts: no score-driven admission or rollback is wired in the inspected runner call sequence. Human benchmark/config authorship and per-result judgment remain unresolved.

#### MEM-RTE-evaluation-transfer
Label: DeepSWE wiki transfer

Endpoints: task base/source workspace → generated or restored cached wiki → managed setup → wiki/AGENTS copy into task workspace → downstream Codex run. Driver owns preparation/transfer; external host owns consumption. Distinct from [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) and [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval): benchmark preparation copies state before a separate consumer run. SRC-1, `evals/deepswe/openwiki_codex.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Preparation/cache/status metadata followed by super().run of the task instruction.
- Later read-back: Generated/cached wiki and managed AGENTS guidance are copied to downstream task workspace; retrieval MCP is configured for that wiki. Subsequent host use is unobserved.
- Delegated visibility: Downstream host receives task workspace/guidance and retrieval access, not generator conversation. Its context loading/compaction is external.
- Selection predicate: Task base commit, normalized package digest and model form cache key; compatible older package caches may be selected by metadata when enabled. The task host selects requested sections later.
- Invalidation or expiry: Driver validates cache archive containment/type/size and required wiki/update metadata; cache replacement and workspace overwrite are code-owned. Compatible-cache reuse prevents claiming exact current-package regeneration on every run.
- Activation or effect: Wiki/instruction delivery is wired; no supplied host trace shows reliance or changed solution behavior.
- Evidence limits: Cache validation is not semantic correctness; external evaluator/host operation and causal treatment effect are uninspected.

> f"cp {shlex.quote((_OPENWIKI_SOURCE_DIR / 'AGENTS.md').as_posix())} "
>                     f"{shlex.quote((_APP_DIR / 'AGENTS.md').as_posix())} && "
> --- `evals/deepswe/openwiki_codex.py`

Preparation admits generated or cached artifacts through code checks, not per-page human approval. Generation follows ordinary page gates; failure can stop preparation. Cache/filesystem replacement supplies operational recovery, not semantic rollback. Benchmark task success is an external evaluation outcome, not a page-admission oracle wired into this preparation. Operating mode: bounded downstream task evaluation. Managed guidance persists as a host instruction surface; wiki prose remains repository context. Source-native `super().run` establishes the later caller, not a hypothetical API consumer.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-claims-maintenance
Label: Claims guide maintenance

Consumer: later repository planner/page model or host. Channel: preflight issues, issue-bearing assignment Claims and optional complete compact inspect result. Force: semantic evidence/maintenance guidance; code separately uses versions/statuses to reject invalid state. Horizon: across update runs while sidecars/pages survive. Distinct from [RT-BAP-page-instructions](runtime.md#rt-bap-page-instructions): that supplies planner-authored objectives, whereas this supplies retained propositions and evidence problems. Delivery is wired; reliable criticism and behavioral activation remain unobserved. SRC-1, `src/claims/brains/code/preflight.ts`, `src/claims/brains/code/session.ts`, `src/generation/repository-run.ts`.

## Annotations

#### On [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state)

Storage/lineage: `.run.json` retains proposed/admitted plan, progress and recovery inputs across interrupted invocations. Symbolic queue state has code authority; natural-language assignment material has the separate consumer declared in [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance). Worker frame isolation does not erase resumable assignments. Complete finish deletes transient run state; committed manifest and pages remain. SRC-1, `src/generation/repository-run.ts`, `src/generation/page-manifest.ts`; supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

#### On [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance)

Planner-authored language is retained inside symbolic plan storage and later projected into fresh worker prompts or resumed host assignments. It therefore crosses invocations without retaining full research dialogue. Static planner instruction to copy relevant constraints is curation guidance, not proof of selective compliance. The retained instructions can preserve task rationale if written there; no required complete reasoning history is established. SRC-1, `src/agent/repository-prompts.ts`, `src/generation/run-state.ts`; supplied [RT-BAP-page-instructions](runtime.md#rt-bap-page-instructions).

#### On [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Working-context control: code creates fresh planner and page attempts; task filtering keeps model delegation out. Initial prompts do not transfer other workers' conversation/research; returned progress goes to CLI, while pages, accepted sparse Claims and plan state survive. Separately, the shared home-directory history mount affords conversation-derived retention through direct middleware writes and later backend reads, including for these uncheckpointed workers. Later attempts read files/Claims/history by value, not dereference pointers to abandoned model windows. This fits selected-input initial frame isolation; the stack analogy stops at persistent external artifacts, the durable shared history surface and parallel process-local bookkeeping. No production per-page compaction budget, actual discarded/retained conversation content or cross-worker history selector is established. Source reload remains distinct from conversation compaction. [MEM-OBJ-conversation-history](#mem-obj-conversation-history) and [MEM-RTE-history-offload](#mem-rte-history-offload) preserve the known channel and limits. SRC-1, `src/agent/agent-backend.ts`, `src/config/openwiki-home.ts`, `test/agent/conversation-history-offload.test.ts`. SRC-1, `src/agent/repository-runner.ts`; supplied runtime passages.

Read-back selection added by direct inspection: nextRepositoryPage supplies only issue-bearing Claims plus count. Complete current Claims require inspectRepositoryPageClaims; issue-free Claims otherwise survive deterministically. Snapshot captures Markdown and sidecar before model-owned work, making recovery material different from synthesized knowledge. SRC-1, `src/generation/repository-run.ts`.

> claimsRequiringAttention: existingClaims.filter(({ issue }) => issue),
> --- `src/generation/repository-run.ts`

#### On [RT-RTE-host-generation](runtime.md#rt-rte-host-generation)

Same retained assignments/Claims/pages support resume, but host conversation memory, compaction, isolation and manual edits are not controlled by the native worker builder. Skill asks sequential assigned-page work; compliance is unobserved. OpenWiki's own protocol selects assignments rather than installing a shared host-context memory manager. SRC-1, `src/integrations/core/session-manager.ts`, `integrations/openwiki/SKILL.md`; supplied runtime.

#### On [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion)

Write lineage: deterministic connector payloads → narrow raw-item model reads → natural-language local-wiki synthesis → deterministic frontmatter/index/provenance finalization. Model filesystem edits are the content admission, unlike strict repository submit_page. Physical connector I/O and user trigger do not establish human per-content approval. Deletion/correction of prose is model/host work; source-specific raw expiry/cursors remain unresolved. SRC-1, `src/ingestion/ingestion.ts`, `src/agent/okf-middleware.ts`, `src/connectors/io.ts`, `src/connectors/tools.ts`.

Read-back: later personal chat is instructed to inspect wiki first, with raw evidence only for missing/stale/ambiguous/contradicted detail or explicit source/latest-data requests. The foreground model selects files through filesystem/raw tools; this is requested tool supply rather than unsolicited whole-wiki push. Source-specific ingestion creates a fresh thread; no automatic cross-source conversation carry is established. Dependency subagent isolation/summary alternatives remain uninspected. SRC-1, `src/agent/prompts/personal.ts`, `src/ingestion/ingestion.ts`.

> - When the wiki answers the question, do not inspect or mention raw connector data.
> --- `src/agent/prompts/personal.ts:49-56`

#### On [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval)

Selector detail: per-call in-memory SQLite FTS5 over title/description/heading/prose/identifiers; path matches first, term coverage second, weighted BM25 third. Source-path hints can boost only lexically matching candidates. Each candidate's excerpt comes from its best term-matching block, stripped/compacted and shortened to 600 characters. Default 5 results, maximum 20; query at most 2,000 characters; at most 20 path hints. Full read allows at most 20 anchors and returns complete sections in requested order, without an inspected total response-token limit. This controls progressive disclosure but cannot guarantee a small final model window. SRC-1, `src/retrieval/wiki.ts`.

> "SELECT rowid, bm25(units, 8, 4, 6, 1, 3) AS score FROM units WHERE units MATCH ? ORDER BY score, rowid",
> --- `src/retrieval/wiki.ts`

Content versus metadata: search parses title/description/tags/source resources from Markdown frontmatter; it does not load sidecar Claims or evidence versions. Read strips frontmatter and supplies raw selected section content, not the search display summary and not a proof package. Rank index is discarded after each call; files persist, snippets do not become separate memory. Host policy supplies behavioral authority; actual use is unobserved. SRC-1, `src/retrieval/wiki.ts`; [RT-BAP-retrieved-sections](runtime.md#rt-bap-retrieved-sections).

Withdrawal countercase: search skips `status: deprecated`, but readWikiSections validates page/anchor and reads current Markdown without the same status gate. A stale stored reference/direct caller can still read a deprecated page. Search skips navigation-like H2 sections; read parses available headings independently. Missing sections fail; Markdown reload proves current bytes, not valid Claims or semantic freshness. This qualifies withdrawal and exhaustive selection claims, without correcting runtime's narrower retrieval description.

> if (fields.status === "deprecated") return [];
> --- `src/retrieval/wiki.ts`

#### On [RT-RTE-page-translation](runtime.md#rt-rte-page-translation)

Transformation lineage is page text → direct model translation → backend rewrite. Derived translated prose replaces the previous language; pending markers supply later retry selection. Structural nonempty/truncation checks are software admission, not fidelity proof. Original identifiers/paths are to be preserved by guidance; historical reasons can remain in translated prose but are not independently verified. This is curation distinct from trace-fed update or graph compaction. SRC-1, `src/agent/translation-middleware.ts`; supplied runtime passages.

#### On [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

Retention/adoption distinction: setup writes static host policy before generation, while CI proposes retained wiki/manifest changes through a PR. PR merge/rejection is a separate possible human/repository-policy gate; local generation has already admitted pages. Removing `.run.json` can withdraw queue-resume capability without withdrawing completed pages or their manifest coverage. Later merged-baseline consumption is afforded by driver wiring, not observed. SRC-1, `.github/workflows/openwiki-update.yml`, `src/ingestion/code-mode.ts`; supplied runtime.

## Write side

Repository authors propose prose and sparse Claims; core owns acceptance, fixed-rule metadata and persistence. The complete queue/protocol route is supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) or [RT-RTE-host-generation](runtime.md#rt-rte-host-generation); [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation) traces the retained propositions separately. Strict schemas, resolver availability, freshness checks, unresolved debt and durability are distinct from semantic truth. Claims confirmation can refresh evidence without changing statement text; retraction deletes current Claim state. Page deletion/orphan cleanup removes sidecars; it is not a semantic rewrite of every downstream copy. Initial repository init can begin with empty Claim state whereas resumed init reloads it. SRC-1, `src/claims/brains/code/runtime.ts`.

Personal writes use model filesystem curation, not the repository submission gate. Raw tool reads are bounded prefixes; raw source text remains untrusted under prompts. Deterministic migration, repair, index synchronization and provenance stamping run around authoring and on writes, but do not establish source-derived semantic changes. Human edits outside protocol are physically possible, but their authorship/approval and re-admission cannot be inferred from generic host identity. SRC-1, `src/agent/okf-middleware.ts`, `src/agent/prompts/personal.ts`; [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion).

Code-mode trace curation has two derived stages: compacted operational records remove inputs/outputs and retain structure/errors/metrics; model instructions then request supported code-linked implications in pages. The retained artifact can shape later agents, but no observed trace proves the requested criticism occurred. Reasons can be retained as code/trace links and prose implications; neither complete argument retention nor later use of the reasons is enforced. [MEM-RTE-trace-documentation](#mem-rte-trace-documentation) establishes the chain and limits. Direct translation is another curation surface with its own output/retry checks, not an evidence-learning synonym.

Chat checkpoint writes are another admission mechanism: graph/dependency state persistence, followed by code-owned database-checkpoint deletion. They must not be conflated with documentation learning or with summarizing a window. Separately, OpenWiki mounts durable home-directory conversation history for native agents, including uncheckpointed workers. Direct middleware writes can bypass model-facing history-write denial; backend reads afford reload. The intended summarization producer is named by source-native tests, but actual payload provenance, raw/derived form, retained reasons, production compaction/reload policy and exercised later readers remain unresolved. SQL cleanup and failed page snapshots do not establish history-file deletion. [MEM-RTE-chat-continuation](#mem-rte-chat-continuation), [MEM-RTE-history-offload](#mem-rte-history-offload).

CI, caches and evaluators introduce additional retention/adoption surfaces. A PR can preserve partial completed progress for later merge; a benchmark driver can restore a compatible cache then supply it to a host; LEDGER captures and scores continuing artifacts without an inspected score-feedback gate into production generation. These are different owners/checks, not a single system-wide human approval policy. See [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [MEM-RTE-evaluation-transfer](#mem-rte-evaluation-transfer), [MEM-RTE-ledger-evaluation](#mem-rte-ledger-evaluation).

## Read-back

There are several actual or instructed later consumers, not just storage APIs:

- Future repository updates reload sidecars, manifest and resumable plan; code consumes hashes/statuses, while model/host consumes selected Claims and page guidance. The full Claim state is optional inspect supply. [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation), [RT-BAP-page-instructions](runtime.md#rt-bap-page-instructions).
- Coding hosts request lexical search then select full sections. Selector inputs/bounds and status-filter asymmetry are in the retrieval annotation. This is a request-selection-delivery chain, not unsolicited injection; no repeated-use effect is observed. [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval).
- Personal chat has an explicit wiki-first consumption role and narrow raw-data fallback. This is prompt policy plus filesystem/tool capability; compliance and task benefit remain unobserved. [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion) annotation.
- Same-session chat calls pass the retained thread to the graph/checkpointer. Exact serialized summaries or original-turn fragments reaching the next model remain dependency uncertainty. [MEM-RTE-chat-continuation](#mem-rte-chat-continuation).
- Native agents also expose the shared filesystem history mount through backend reads, independent of SQLite/thread restoration. This establishes reload capability and an intended middleware/agent consumer role, not a traced automatic read-back route or cross-worker use. Production selector inputs, retained parts, budget and model delivery are unresolved. [MEM-RTE-history-offload](#mem-rte-history-offload).
- Humans receive a graph projection, and shipped evaluators capture or copy retained pages into later evaluation/host invocations. These callers establish consumer wiring, not empirical improvement. [MEM-RTE-visualizer-delivery](#mem-rte-visualizer-delivery), [MEM-RTE-ledger-evaluation](#mem-rte-ledger-evaluation), [MEM-RTE-evaluation-transfer](#mem-rte-evaluation-transfer).

Static setup guidance and shipped skills are context engineering, but are not read-back by the contract's use-derived criterion. They govern whether/how later hosts request retained knowledge. Their binding force depends on the external host; the retrieved content is explicitly context, not instructions. [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance), [RT-BAP-retrieved-sections](runtime.md#rt-bap-retrieved-sections).

## Integration issues

- **Supplied corrections:** none required. The direct reads refine runtime without contradicting its scoped claims. Its “lexical section ranking” includes per-call SQLite FTS5 BM25, path and term-coverage ordering; it is not embedding retrieval. Its source reload claim does not imply freshness or total withdrawal.
- **Overlap, not duplicates:** [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation) and [MEM-RTE-trace-documentation](#mem-rte-trace-documentation) span portions of native/host generation, not one complete supplied route. Claims and manifest objects are distinct from [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state); chat checkpoints also have a different producer/state/consumer. [MEM-BAP-claims-maintenance](#mem-bap-claims-maintenance) supplies retained propositions/issues, not planner objectives. No candidate replacement of a supplied referent is asserted.
- **Semantic grounding limit:** resolver internals and model support judgments are not assessed here. [MEM-OBJ-evidence](#mem-obj-evidence), [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation) prove versioned evidence maintenance, not entailment. Epistemic integration must not upgrade machine verification to proposition truth or observed criticism.
- **Consumer-specific withdrawal:** search's deprecated filter does not cover direct section reads. Claim retraction does not erase page prose automatically in the inspected mutation boundary or copies/Git history. [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval), [MEM-RTE-claims-reconciliation](#mem-rte-claims-reconciliation). Prevents universal withdrawal claims.
- **Context correction and remaining opacity:** the previous memory account incorrectly treated offload entirely as an opaque dependency alternative and excluded surviving worker conversations. [MEM-OBJ-conversation-history](#mem-obj-conversation-history) and [MEM-RTE-history-offload](#mem-rte-history-offload) now retain the known home-filesystem surface, direct middleware producer, backend read affordance and tool-write denial. It overlaps the revised supplied [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) account without duplicating its referent. [MEM-OBJ-chat-checkpoint](#mem-obj-chat-checkpoint) and [MEM-RTE-chat-continuation](#mem-rte-chat-continuation) still leave database payload, exact compaction/summary content and host compaction unresolved. SQL pruning and fresh initial native frames remain supported; neither establishes history-file erasure, absence of conversation-derived retention or exercised cross-worker use.
- **Trace outcome limit:** [MEM-RTE-trace-documentation](#mem-rte-trace-documentation) wires biased operational evidence into document authoring and potential later knowledge consumption; no supplied record demonstrates formulated criticism, improved capacity or causal behavioral activation. Trace origin is external source-runtime operation, not automatically OpenWiki's own operation.
- **Residual coverage limits:** individual connector transforms/cursors, scheduler/platform equivalents, browser/static-export details, detailed LEDGER evaluator/oracle and cache trust semantics remain uninspected. The corresponding coverage rows state prevented conclusions. [MEM-OBJ-connector-data](#mem-obj-connector-data), [MEM-RTE-visualizer-delivery](#mem-rte-visualizer-delivery), [MEM-RTE-ledger-evaluation](#mem-rte-ledger-evaluation), [MEM-RTE-evaluation-transfer](#mem-rte-evaluation-transfer). No missing execution is treated as an absence.

## Limitations and checks

HEAD was rechecked directly as `7c469e59584bfac3f97f5c32a67604de46805999`; source identity, run ID and reviewed boundary match the supplied boundary/invocation. Source inspection stayed read-only within SRC-1; only assigned outputs and identity were written. The supplied collection, member types, worker rules and record contract were read completely before authorship. No prior analysis or target execution was used.

This is a source-level capacity account. It does not establish semantic correctness, deployed host trust/compliance, dependency/provider behavior, source-specific synchronization completeness, exercised learning, causal benefit or successful self-improvement. Directly inspected schema, selector and cleanup countercases constrain stronger labels. Uninspected implementation alternatives remain named beside their parts rather than erased.

Validation: the required `commonplace-run validate-output` command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Deterministic form and quotation occurrence do not establish semantic support or job acceptance.
