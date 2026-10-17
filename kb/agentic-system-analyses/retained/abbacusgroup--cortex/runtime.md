---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Cortex runtime baseline: shipped capture, pipeline, retrieval, alternate admission paths and transport controls at a51c2209eb6d26812c19c97aaade3cb64ccfc23c."
run-id: AAS-2026-10-17-cortex-3da14ce55a2b-01
reviewed-boundary: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
---

# Cortex runtime report

## Runtime account

### Evidence and consequential work

Cortex is a knowledge service, not the foreground agent's task scheduler. It accepts knowledge objects, applies classification and graph processing, persists them, and serves selected content to later callers. The caller chooses whether to invoke capture, context, full read or feedback. Internal Python code owns stage order; optional model calls supply proposed classifications, relationships and synthesis prose. No inspected path requires a conversational model to select successive tools inside Cortex. The external agent's planning, approval policy and use of returned knowledge remain outside this boundary. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/orchestrator.py`, `src/cortex/services/llm.py`; [boundary](boundary.md#boundary-and-evidence).

All findings below concern SRC-1 at the frozen revision. Added detailed inspection covers the MCP registration and HTTP launch controls, CLI routing and capture, model adapters, retrieval/presenters, importer admission branches, pipeline stages, temporal snapshot implementation, restore, systemd installation and release workflow. These supply **implementation** evidence; source comments, tool descriptions and agent guidance supply **doctrine/design**. No execution trace or experiment was supplied. Operation, model compliance, isolation in an actual installation, latency, retrieval benefit and successful recovery remain unobserved. No target code was executed.

### Ordinary invocation: CLI capture through MCP, then later context

A human or process invokes `cortex capture` with a title and content, either as an option or stdin. The CLI lowercases and validates the type, maps `capture` to `idea`, and rejects empty content. Unless `--direct` is selected, it probes the configured MCP server and calls the shipped asynchronous MCP client. Failure is reported rather than silently opening another local graph writer. [RT-RTE-capture-pipeline](#rt-rte-capture-pipeline) records admission and decision roles; [RT-RTE-direct-import](#rt-rte-direct-import) records the alternate writer. SRC-1, `src/cortex/cli/main.py`, `src/cortex/transport/mcp/client.py`.

The client opens a fresh HTTP transport and MCP session, initializes it and calls `cortex_capture`. Server construction loads configuration, opens Oxigraph and SQLite through `Store`, attempts ontology initialization, and constructs the pipeline, retrieval engine and access learner. Each handler shares those service objects. IDs identify retained knowledge objects, not agents or delegated tasks. The tool passes caller data into `PipelineOrchestrator.capture`, tagging origin as `mcp`. That string records an entry channel; it does not authenticate the original author or identify a human approver. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/transport/mcp/client.py`.

The pipeline applies any selected template, with template properties winning conflicts, and creates the object **before** optional processing. Graph creation generates the object ID; SQLite insertion follows. SQLite insertion failure attempts graph deletion and raises `SyncError`. The stores are separate effect boundaries, not one inspected cross-store transaction. With the default pipeline enabled, Python runs normalize, link, enrich and reason in that order. Normalization calls the configured classifier unless a stored summary already exists; it generates an embedding only when a provider was supplied. Linking resolves entities and can admit model-proposed relationships after code checks. Enrichment writes tier metadata. Reasoning adds graph triples under fixed rules. SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/db/store.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/enrich.py`, `src/cortex/pipeline/reason.py`.

The server returns an ID, type, overall status and per-stage results. The ordinary CLI prints the ID and original requested type/title, not the full stage result. A printed capture confirmation therefore does not establish that every processing stage succeeded or that the final classification equals the printed type. A later `cortex_context(topic)` searches retained data and returns a summary projection, whereas `cortex_read(id)` returns content, metadata, relationships and entity mentions and records access. The host owns any subsequent context injection or action. [RT-RTE-retrieve-context](#rt-rte-retrieve-context) establishes the selection and context boundary; [RT-BAP-knowledge-delivery](#rt-bap-knowledge-delivery) limits its authority. SRC-1, `src/cortex/cli/main.py`, `src/cortex/transport/mcp/server.py`, `src/cortex/retrieval/presenters.py`.

### Four forcing cases and what they overturn

1. **A caller supplies a summary or disables processing.** A non-empty summary skips internal classification; `run_pipeline=False` returns after ingestion. Thus neither internal LLM review nor the full pipeline is a universal admission gate. The MCP tool explicitly asks its external model caller to classify. Its supplied confidence is a channel convention, not a measured correctness probability. [RT-RTE-capture-pipeline](#rt-rte-capture-pipeline). SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`.
2. **A stage fails, or handles its own error.** Orchestrator-level failures are recorded and later stages continue; the result becomes `partial`. But normalizer graph-update exceptions and embedding failures are logged locally, and enrichment catches write failures while still returning `enriched`. Consequently even `complete` is not a storage-consistency or semantic-quality invariant. [RT-CLM-stage-resilience](#rt-clm-stage-resilience), [RT-CLM-store-consistency](#rt-clm-store-consistency). SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/enrich.py`.
3. **The operator selects direct CLI mode or an importer.** These paths open stores without the HTTP server; direct CLI pipeline construction does not pass an embedding provider. Bootstrap imports also bypass normal CLI routing. Importers can create objects without pipeline processing. Single-writer deployment is a usage arrangement, not a guarantee across all shipped paths. [RT-RTE-direct-import](#rt-rte-direct-import). SRC-1, `src/cortex/cli/main.py`, `src/cortex/pipeline/importer.py`.
4. **HTTP binds beyond loopback, or a caller omits safety review.** Non-loopback MCP omits admin registration, but public capture, classify, link, feedback and pipeline handlers remain mutating. REST's key check is not a gate on direct MCP calls. `cortex_safety_check` returns a warning; delete does not consume an approval token. These controls cannot establish global read-only remote access or mandatory approval. [RT-RTE-transport-control](#rt-rte-transport-control). SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/transport/api/server.py`.

These are source-supported branch traces, not runtime tests. They cover ordinary service calls, direct persistence and administrative bypass boundaries. Provider-native execution, dependency-level cancellation/durability, external-host shell permissions and an actual deployed reverse proxy are not established by these files. The inspected internal completion call sends one user message and no tool schema; it is a returning computation, not an internal delegated worker. External hosts may have more capabilities, but those grants are not Cortex grants. SRC-1, `src/cortex/services/llm.py`.

### Controls, persistence and change planes

The capability surface comprises registered MCP tools, HTTP facades and direct operator commands. The configured grant set is principally determined by MCP registration mode, REST keys and dashboard password/session checks. The isolation envelope depends on the process user, network binding, dependency behavior and deployment. Reference systemd units run user services on loopback and restart them; this supplies neither evidence of deployment nor a sandbox around file/database access. Dashboard requests forward through its MCP client; absent a configured dashboard password, its password helper allows open access. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/transport/api/server.py`, `src/cortex/dashboard/server.py`, `deploy/cortex-mcp.service`.

Knowledge changes are admitted by caller input, optional model proposals and fixed code rules, with path-specific checks rather than per-content human approval. The public classify handler updates component stores directly; the admin update handler uses `Store.update` and thereby snapshots the old SQLite row. These are materially different recovery paths. Temporal history is not a universal journal of every mutation. Detailed memory revision assessment is left to the memory member. [RT-RTE-maintain-knowledge](#rt-rte-maintain-knowledge), [RT-OBJ-store](#rt-obj-store). SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/db/store.py`, `src/cortex/pipeline/temporal.py`.

Product and production changes have a separate operator/developer plane: tagged releases test, build and publish packages; service installation writes launch definitions and invokes OS managers; model names and credentials come from configuration. No inference from knowledge capture to automatic software or model-weight replacement is warranted. [RT-RTE-install-release](#rt-rte-install-release) describes inspected admission points without claiming an exhaustive extension audit. [RT-CMP-llm-client](#rt-cmp-llm-client), [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer) and [RT-CMP-litellm-provider](#rt-cmp-litellm-provider) distinguish mutable model resolution from parameter updates. SRC-1, `.github/workflows/release.yml`, `src/cortex/cli/install.py`, `src/cortex/core/config.py`.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LLMClient

Source-native `LLMClient` wraps LiteLLM completion for classification, relationship discovery and general prose. Its Python prompts are natural-language guidance; the called model is distributed-parametric content residing in an external/local provider, not in Cortex's SQLite database. Configuration and returned JSON are symbolic interfaces. SRC-1, `src/cortex/services/llm.py`, `src/cortex/core/config.py`.

Cortex's inspected wrapper requests inference, not parameter training or mutation. Exact model version is not pinned by the wrapper: configuration supplies a model string, and the dependency/provider resolves it. A mutable provider endpoint or alias can resolve to another model; provider-internal parameter changes remain uninspected. Availability depends on model, credentials where required, and LiteLLM import. Calls request a 30-second timeout and temperature 0.1; classification errors fall back to title-as-summary with confidence zero. There is no answer oracle in this wrapper.

> response = litellm.completion(
>     model=self._model,
>     messages=[{"role": "user", "content": prompt}],
>     api_key=self.config.llm_api_key,
>     timeout=30,
>     temperature=0.1,
> )
> --- `src/cortex/services/llm.py`

#### RT-CMP-sentence-transformer
Label: SentenceTransformerProvider

The local optional embedding component loads a sentence-transformers model by name and encodes text to normalized numerical vectors. Model weights are distributed-parametric and loaded through the dependency; resulting vectors are dense distributed representations stored separately as SQLite embedding bytes. No inspected call updates weights during operation. `all-mpnet-base-v2` is the default model name, not an exact artifact revision. The loader supplies no revision pin; model resolution can change between loads. There is no configured remote inference endpoint in this branch, but repository/cache resolution and dependency internals remain uninspected. SRC-1, `src/cortex/services/embeddings.py`, `src/cortex/core/config.py`.

> self._embedder = SentenceTransformer(self._model_name)
> --- `src/cortex/services/embeddings.py`

#### RT-CMP-litellm-provider
Label: LiteLLMProvider

The alternative embedding component calls `litellm.embedding` with a model string, input text and timeout. Numerical provider parameters are distributed-parametric and outside Cortex storage; returned vectors become SQLite bytes through normalization. The inspected adapter does not train or update parameters. Its exact model revision is not pinned; a mutable endpoint/model alias can resolve differently. Provider-internal state, revisions and updates are uninspected. Missing dependencies or embedding errors can disable semantic processing rather than reject ingestion. SRC-1, `src/cortex/services/embeddings.py`, `src/cortex/pipeline/normalize.py`.

> response = litellm.embedding(**kwargs)
> --- `src/cortex/services/embeddings.py`

### Operative objects

#### RT-OBJ-store
Label: Store

The source-native unified `Store` coordinates SQLite content/metadata and Oxigraph objects, relationships and ontology. Natural-language title/content/summary fields are interpreted by humans/models; symbolic IDs, types, tiers and graph predicates receive fixed code/query interpretation. Dense embedding bytes reside in SQLite but are produced by the separately declared embedding components. These parts do not share identical mutation or recovery coverage. This record establishes the runtime container, not a substitute for part-specific memory findings. SRC-1, `src/cortex/db/store.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/temporal.py`.

`Store.read` treats SQLite content as authoritative and augments it with graph relationships. `Store.create` writes graph then SQLite with attempted compensating deletion on SQLite failure. `Store.update` snapshots SQLite first, then updates SQLite and string-valued graph properties; a graph failure can leave SQLite changed. Direct component-store writes bypass that snapshot. Temporal versions are JSON snapshots in SQLite's `document_versions`, not model parameters or a cross-store transaction log.

> """Read from SQLite (content-authoritative) enriched with graph relationships."""
> --- `src/cortex/db/store.py`

#### RT-OBJ-inference-rules
Label: INFERENCE_RULES

The shipped list in Python holds named symbolic SPARQL CONSTRUCT queries and natural-language descriptions. It covers symmetric `contradicts`, inverse `causedBy`/`ledTo`, and transitive `supersedes`. `ReasonStage` consumes the formal query bodies and adds graph triples. The rules reside in source/package files; inferred triples persist in Oxigraph. Rule descriptions are inspectable statements, not proof that their assumptions hold for user data. SRC-1, `src/cortex/pipeline/reason.py`.

> "description": "If A supersedes B and B supersedes C, then A supersedes C",
> --- `src/cortex/pipeline/reason.py`

### Routes

#### RT-RTE-capture-pipeline
Label: Capture and pipeline admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP returns the retained object ID and ingestion/processing result; CLI displays ID and requested type/title rather than full stage detail.
- Later read-back: Admitted content, classification, graph links and embeddings can reach later search/context/read calls from the stores.
- Delegated visibility: No internal agent delegation is established; optional classifier sees title and up to 8000 content characters, relationship completion sees bounded content and candidate metadata, and the external caller receives the tool result.
- Selection predicate: Explicit capture request; templates can set object type/properties; existing summary skips classification, and run_pipeline controls whether stages execute.
- Invalidation or expiry: No automatic capture expiry is specified here; later edits/deletes and maintenance can change the retained object. Processing failure does not roll back the initial ingestion.
- Activation or effect: Code writes knowledge state and can add graph edges; a future agent acting differently because of that knowledge remains unobserved.
- Evidence limits: Static wiring, not an observed capture; model correctness, cross-store atomicity and human approval are not established.

Trigger/principal: caller invocation through MCP or the CLI facade. Next-step owner: fixed Python stage order, not a runtime model planner. Admission mode is open caller-supplied content, not a bounded experiment. Caller or template proposes content/type; internal model optionally proposes metadata and links. Software decides acceptance through parsing, normalization and relationship checks. A generic MCP caller is not evidence of a human approving each object. No independent expected-answer oracle is used. Internal model proposals can be discarded on parse failure, unknown relationship type, missing endpoints or self-link; malformed caller JSON is ignored at the tool boundary. Model relationship confidence must exceed 0.5 before LinkStage checks it. These are structural gates, not truth tests. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py`.

What persists: raw content is admitted first; summaries, types, entity links and graph relationships may then be added. Guidance comprises templates, the classification/relationship prompts and tool instructions asking the external model caller to classify. A caller-provided summary causes the normalizer to reuse stored data, and MCP assigns confidence 0.9 when such a summary is supplied. Recovery consists of compensating create cleanup, per-stage continuation and explicit reprocessing/edit/delete, not automatic rejection of the whole capture. SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/db/store.py`.

> if not run_pipeline:
>     return result
> --- `src/cortex/pipeline/orchestrator.py`

> # Step 1: Classification — skip LLM if pre-classified at capture time
> if existing_summary:
> --- `src/cortex/pipeline/normalize.py`

#### RT-RTE-retrieve-context
Label: Retrieval and context projection

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search returns ranked document dictionaries; context projects them to ID, title, type, tags, project, summary/title fallback, tier and score; read returns full document details or not-found.
- Later read-back: Reads persisted knowledge created or maintained earlier; full reads and positive feedback also persist access counts for subsequent learner operations.
- Delegated visibility: The requesting host receives only the selected projection. Context omits full content and graph relationships; explicit ID read reloads richer retained material.
- Selection predicate: Topic/query drives FTS and optional embedding candidates, then graph connectivity and created-at recency contribute weighted scores; filters and result limit apply before presentation.
- Invalidation or expiry: Current rows are read per request; recency decays scores rather than deleting content. This route does not establish embedding refresh on every later content update.
- Activation or effect: Code determines delivered context and logs non-empty search queries; MCP read/positive feedback calls record_access. Host compliance and changed task behavior are unobserved.
- Evidence limits: No live corpus, retrieval outcome or benefit measurement. Model-version compatibility and provider quality are not established.

The engine takes keyword candidates up to three times the requested limit, optional semantic candidates from at most 10000 stored embeddings, and scores the merged set with default keyword/semantic/graph/recency weights 0.4/0.3/0.2/0.1. The constructor uses passed weights or defaults; it does not itself fetch persisted learner weights. Context projection is a code-selected working-context control: the host asks for compact summaries, full bodies stay outside that response, and IDs remain available for later explicit reads. This is not trimming an agent's existing conversation, popping a sub-agent frame or forcing anything out of the host's window. SRC-1, `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/transport/mcp/server.py`.

Dossier is a material alternative: exact entity-name matching selects mentioning objects, otherwise FTS supplies related objects; output includes at most ten object summaries, contradiction relationships, related entities and a timeline. Synthesis instead selects recent/project objects from a bounded listing and can request prose via the LLM. These are different selectors, not proof that every presentation uses the hybrid engine. SRC-1, `src/cortex/retrieval/presenters.py`.

> "summary": doc.get("summary", "") or doc.get("title", ""),
> --- `src/cortex/retrieval/presenters.py`

> if relevant:
>     learner.record_access(obj_id)
> --- `src/cortex/transport/mcp/server.py`

Feedback mode is an open relevance signal, not a reference-answer experiment. A caller decides relevance; positive feedback/read events increment counters and can promote tier at ten accesses. No human veto, answer oracle or measured retrieval improvement is established. Detailed revision/learning assessment belongs to the memory member. SRC-1, `src/cortex/retrieval/learner.py`.

#### RT-RTE-direct-import
Label: Direct CLI and import admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Direct CLI capture prints an ID; importers return imported/skipped/failed counts, with Obsidian also reporting wiki-link relationships.
- Later read-back: Imported/directly captured objects become available to the same retained-store retrieval consumers.
- Delegated visibility: Importers receive filesystem/database content in the local process; optional pipeline calls expose bounded content to the configured model. No remote worker delegation is established.
- Selection predicate: --direct bypasses MCP for ordinary commands; bootstrap import commands directly obtain a store. Obsidian recursively selects Markdown, skips selected frontmatter/index cases and applies dedup; v1 maps database rows/types.
- Invalidation or expiry: Imports have hash/title dedup rather than automatic source synchronization; later edits/deletes/restore can change admitted state.
- Activation or effect: Direct local store creation bypasses HTTP tool-registration controls; pipeline-present Obsidian import also normalizes/enriches, while pipeline-absent and v1 branches create directly and derive entities from tags.
- Evidence limits: No import was run; dedup success and concurrent-writer safety are not established. This does not imply deployed simultaneous writers.

Trigger/principal is an operator/process choosing direct capture or an import path; author identity and human per-content control remain unresolved for imported files/rows. Importers propose retained objects from input content and metadata; fixed mapping, skip rules, hash/title checks and exceptions decide admission. No independent answer oracle or per-object human approval appears in these inspected branches. Obsidian guidance includes frontmatter type/project/tags/summary and inferred path conventions; v1 uses a fixed type map. Persistence includes objects, tag entities, wiki-link relationships and dedup markers. Failures are counted per item; already admitted items are not rolled back as one batch. Dedup markers can be set before later creation, so retryability is not equivalent to a successful-import journal. SRC-1, `src/cortex/pipeline/importer.py`.

Direct CLI pipeline construction omits the embedding provider supplied by MCP server construction. This qualifies any assertion of equivalent semantic indexing across entry points. Operator recovery may use explicit reprocessing or the separate restore path; no universal transactional import rollback is established. SRC-1, `src/cortex/cli/main.py`.

> if _direct_mode:
>     return False
> --- `src/cortex/cli/main.py`

> content_hash = hashlib.sha256(content.encode()).hexdigest()
> existing = self.store.content.get_config(f"import_hash:{content_hash}", "")
> if existing:
>     return True
> --- `src/cortex/pipeline/importer.py`

#### RT-RTE-maintain-knowledge
Label: Knowledge maintenance and recovery

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Classify/update/delete and pipeline tools return status or processing results; advanced reason returns findings; restore reports replacement state and old-store location.
- Later read-back: Changed content, metadata and graph triples feed later retrieval; Store.update preserves old SQLite rows as temporal versions, but component-store writes do not share that automatic snapshot.
- Delegated visibility: Classify consumes caller-supplied fields/entities; advanced reasoning inspects retained objects/relationships locally. Provider visibility follows optional pipeline model calls, not an autonomous maintenance agent.
- Selection predicate: Caller-selected ID or maintenance invocation; fixed inference rules select matching graph patterns, and advanced checks use bounded object lists and relationship patterns.
- Invalidation or expiry: Explicit edits/deletion/restore change state; inference adds missing triples up to fixpoint or iteration limit, without establishing automatic truth retraction when premises later change.
- Activation or effect: Public classify changes stores, ordinary pipeline reason adds triples, and admin advanced reason returns structural findings. Findings alone are not automatic revisions of the challenged content.
- Evidence limits: Recovery paths are inspected source, not exercised recovery; no demonstrated semantic contradiction resolution, model quality or future-capacity improvement.

Admission is path-specific. Caller supplies reclassification or update fields; classify writes SQLite directly and suppresses some graph failures, whereas admin update calls Store.update. Relationship creation validates predicate and non-self-link at graph API level; LinkStage additionally checks endpoints. Ordinary ReasonStage writes inferred triples directly into the backing graph, so typed API validation is not a universal inference gate. Software decides these changes; there is no per-content human acceptance step inside these handlers and no independent answer oracle. Operating mode is open maintenance on existing knowledge. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/db/graph_store.py`, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/reason.py`.

Guidance and theory: [RT-OBJ-inference-rules](#rt-obj-inference-rules) contains explicit formal relationship assumptions. ReasonStage consumes unchanged rule bodies to derive triples; advanced reason's structural contradiction check reports superseded objects with active dependents, and its pattern detector reports repeated fixes mentioning an entity. This does not establish criticism revising the rule set itself. In particular, the advanced contradiction docstring mentions semantic LLM checks, but the inspected detect_contradictions body only invokes structural checks. SRC-1, `src/cortex/pipeline/advanced_reason.py`.

- theory-builder conditions 1–4: Condition 1 conclusion status: wired — whole named formal rules state their content. Condition 2 conclusion status: wired — query results determine graph additions. Condition 3 conclusion status: uninspected — inspected inference/advanced checks do not establish content-directed blame and revision of those rules; broader external criticism is not available. Condition 4 conclusion status: uninspected — fixpoint iteration retains derivations, not an evidenced retained criticism shaping rule revision.
- Addressability: Individual rule names, descriptions and query bodies are inspectable/revisable in source; no runtime rule-editing protocol is established here.
- Persistence: Rules persist across installations/runs as shipped code; derived triples persist in the graph for later queries. No persisted criticism-to-successor-rule chain is established.
- learning: Future improved capacity and attribution are unestablished; formal derivation and persistence alone do not demonstrate improvement.
- Reflection: These checks represent selected knowledge-state relations, not an established two-way representation of Cortex's own method changing its operation.
- Reflective theory builder: uninspected — no method-criticism loop is established by these paths.
- Autonomous theory builder: uninspected — computational derivation alone does not establish every internal operation of theory criticism/revision.

Recovery differs from admission. Store.update snapshots old content, but does not roll back SQLite if graph update fails. Restore validates required archive members and rejects unsafe paths or a detected running server, moves old stores to .pre-restore, extracts with the data filter and attempts rollback on extraction failure. This is operator-triggered store replacement, not per-object semantic rejection. It requires filesystem permissions and accurate process/dependency behavior; successful recovery is unobserved. SRC-1, `src/cortex/db/store.py`, `src/cortex/pipeline/temporal.py`, `src/cortex/cli/backup.py`.

> if self.temporal is not None:
>     self.temporal.snapshot_before_update(obj_id)
> --- `src/cortex/db/store.py`

> findings.extend(self._structural_contradictions())
> return findings
> --- `src/cortex/pipeline/advanced_reason.py`

#### RT-RTE-transport-control
Label: Transport registration and approval scope

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Server registration exposes a mode-dependent tool set; REST authenticates/rejects requests and translates typed MCP failures; safety_check returns a warning and confirmed false.
- Later read-back: Transport controls are configured anew on startup; mutation tools they expose write retained knowledge. No retained approval artifact is consumed by delete.
- Delegated visibility: CLI, dashboard and REST forward to MCP; the receiving server runs tools under its own OS process authority rather than a per-tool sandbox established here.
- Selection predicate: Stdio enables admin tools; HTTP enables admin only for exact loopback host strings. REST keys and dashboard sessions apply to their respective facade routes.
- Invalidation or expiry: MCP exposure changes with server construction/bind mode; facade credentials/configuration follow their own checks. There is no inspected expiring delete-approval token.
- Activation or effect: Registration prevents omitted admin tools from that MCP server's tool surface; it does not prevent public mutations, direct CLI writes or access through another local facade.
- Evidence limits: This is not a deployed network/isolation audit. Dependency transport security, proxy exposure and actual caller grants remain uninspected.

Owner/enforcement: Cortex's run_http computes include_admin; create_mcp_server conditionally registers admin handlers. **Guarantee strength: invariant** for that registration decision on this launcher path, not for authorization of all effects. Covered path: HTTP server created by run_http. Alternates: stdio, direct factory calls with include_admin=True, direct CLI/importers and facades reaching a loopback MCP instance. External contract: the selected bind and network topology must match the operator's trust boundary. Public capture/classify/link/pipeline remain available even with admin disabled. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/cli/main.py`.

REST's owner is verify_api_key: configured keys require a constant-time match, but empty configuration permits any non-empty key. That policy does not secure the separate MCP listener. Dashboard uses configured password hash and session checks, with no password meaning open access in its helper. Neither facade proves a per-object authorization boundary. SRC-1, `src/cortex/transport/api/server.py`, `src/cortex/dashboard/server.py`.

The safety tool is **policy**, not an enforced approval handshake. Its warning asks the caller to confirm; cortex_delete directly calls store.delete without checking that tool or a confirmation field. Human approval can be provided by an external host, but is not established by Cortex's handler. No answer oracle applies; caller/host decides whether to heed the warning. SRC-1, `src/cortex/transport/mcp/server.py`.

> is_local = host in _LOCALHOST_HOSTS
> mcp = create_mcp_server(include_admin=is_local)
> --- `src/cortex/transport/mcp/server.py`

> "warning": f"This will {action} '{target}'. Confirm before proceeding.",
> "confirmed": False,
> --- `src/cortex/transport/mcp/server.py`

> deleted = store.delete(obj_id)
> --- `src/cortex/transport/mcp/server.py`

#### RT-RTE-install-release
Label: Product and production admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Release workflow builds/publishes distribution artifacts after its test dependency; install commands write service definitions and report activation; uninstall removes/disables definitions.
- Later read-back: OS service managers consume persisted launch definitions; package consumers load shipped source, prompts and ontology in later processes. Configuration selects model/provider for new service objects.
- Delegated visibility: GitHub jobs and OS service managers are executors for defined commands, not agent subcontexts; their actual execution evidence is not supplied.
- Selection predicate: Version-tag push triggers release; operator-selected install service/platform chooses rendering and manager calls; configuration values choose model endpoints.
- Invalidation or expiry: New package/configuration or service install can replace prior definitions; uninstall disables/removes services. No universal automatic package rollback is established.
- Activation or effect: Source wires package publication and persistent service registration, including systemctl enable --now; actual successful installation/release or use of a replacement model is unobserved.
- Evidence limits: Repository definitions do not expose GitHub environment protection rules, deployed OS permissions, model artifact identity or successful manager operations.

Trigger/proposal/admission: developers supply tagged source; the workflow's build job needs the reusable test job, then release/PyPI jobs need build. Tests can reject a build progression, but source alone does not establish semantic approval of every product change or externally configured human protection of the pypi environment. Expected test outcomes are evaluation references, not an answer oracle used by runtime knowledge admission. Mode is versioned software delivery, not autonomous runtime improvement. SRC-1, `.github/workflows/release.yml`, `.github/workflows/test.yml`.

Operators select installation and configuration. Templates plus selected binary/data path guide service proposals; Linux installation stops an existing unit, writes new text, reloads the manager and enables/starts it. Failure from checked manager commands can reject completion, but an earlier file write is not automatically undone. Uninstall supplies a disable/remove path rather than demonstrated transactional rollback. Shipped systemd defaults bind MCP to loopback and specify restart behavior. No inference from those declarations to a deployed isolation guarantee is warranted. SRC-1, `src/cortex/cli/install.py`, `deploy/cortex-mcp.service`, `src/cortex/core/config.py`.

> unit_path.write_text(content)
> subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
> subprocess.run(["systemctl", "--user", "enable", "--now", unit_name], check=True)
> --- `src/cortex/cli/install.py`

> needs: test
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-stage-resilience
Label: Pipeline stage resilience

Claimed operation: one stage's failure does not block subsequent stages. Owner: PipelineOrchestrator.run_pipeline; enforcement: separate exception handlers around each stage. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. Covered paths are capture with run_pipeline enabled and explicit run_pipeline calls. Alternates include ingestion-only capture, direct import and local errors suppressed within a stage. Required external contract: stage calls must return or raise; provider/dependency hangs or process failure are not covered by these handlers. This supports continuation and partial-result reporting, not all-or-nothing admission or semantic completion. SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/enrich.py`.

> Each stage is resilient — failure in one doesn't block the others.
> --- `src/cortex/pipeline/orchestrator.py`

#### RT-CLM-store-consistency
Label: Unified mutation consistency claim

Claimed operation in the Store module is that all mutations use the unified layer. The inspected implementation qualifies that declaration: normalizer, enrich, classify, learner and rule inference access backing stores directly. Owner: Store for its own methods only. Enforcement: sequential writes and compensating create deletion, with snapshot-before-update for Store.update. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. Covered path: Store methods; alternate paths are component-store updates and direct graph inference. Required external contract: backing-store calls and cleanup must succeed. Even Store.update reports a SyncError after SQLite has changed if a graph update fails. Universal synchronized writes and universal temporal history are not established. SRC-1, `src/cortex/db/store.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/enrich.py`, `src/cortex/transport/mcp/server.py`, `src/cortex/retrieval/learner.py`, `src/cortex/pipeline/reason.py`.

> All mutations go through this layer to keep both stores in sync.
> --- `src/cortex/db/store.py`

> self.store.content.update(obj_id, **updates)
> --- `src/cortex/pipeline/normalize.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-knowledge-delivery
Label: Knowledge delivery to requesting host

Consumer: external agent or human requesting search/context/read. Channel: MCP result or facade response carrying selected natural-language knowledge plus symbolic metadata. Force: informational/tool-result content, not a Cortex-enforced instruction priority or evidence of caller compliance. Horizon: immediate response and potentially later tasks through persistent object read-back. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/retrieval/presenters.py`, `llms.txt`.

The agent guidance recommends compact context injection, but the server controls only retrieval and projection. It does not establish that the host places the result into a model invocation or follows its claims. [RT-RTE-retrieve-context](#rt-rte-retrieve-context) identifies what crosses this boundary.

> Token-efficient briefing (summaries only). Use this for context injection.
> --- `llms.txt`

#### RT-BAP-rule-execution
Label: Inference rule authority

Consumer: ReasonStage._apply_rule. Channel: shipped SPARQL query strings executed on the current graph. Force: fixed executable query semantics capable of adding retained triples without a per-triple human decision. Horizon: current pipeline execution and later graph consumers across invocations. This is symbolic code authority, unlike informational knowledge delivery. Rule content and derivation are established; automatic rule criticism or replacement is not. SRC-1, `src/cortex/pipeline/reason.py`; [RT-OBJ-inference-rules](#rt-obj-inference-rules), [RT-RTE-maintain-knowledge](#rt-rte-maintain-knowledge).

> self.graph._store.add(quad)
> --- `src/cortex/pipeline/reason.py`

## Annotations

none
