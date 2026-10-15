---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Link runtime baseline: local context retrieval, admission, session delivery and maintenance at cc92f3632121b04063b24eaaf3a8c5429eaf2b57."
run-id: AAS-2026-10-14-link-595f6f9cba36-01
reviewed-boundary: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
---

# Link runtime report

## Runtime account

### Consequential work and evidence

Link supplies local retained context to an external agent; the external agent answers and performs application work. Link also provides explicit memory writes, proposal capture, source compilation procedures, project seeding and maintenance. It is not an enclosing model/tool execution loop. The boundary and its exclusions remain those in [boundary](boundary.md). All source evidence here is SRC-1 at the frozen commit. No target code, tests, examples, providers or benchmarks were executed. Implementation wiring is inspectable; invocation success, host compliance and benefits remain unobserved.

The package exposes `lnk` and `link-mcp`; its wheel includes the root CLI, viewer, `LINK.md` and ignore configuration. MCP runs over stdio with a selected slim or full tool surface. The slim surface is a smaller menu, not a reduced filesystem permission grant: `admin` still exposes maintenance and advanced mutations. CLI and core APIs are other shipped entry paths. The HTTP server has write routes despite the viewer label. LinkBar runs `lnk` subprocesses against its selected workspace, and can also run an executable command returned for runtime repair. SRC-1, `mcp_package/pyproject.toml`, `mcp_package/link_mcp/server.py`, `serve.py`, `apps/LinkBar/Sources/LinkBar/LinkCLI.swift`.

> [project.scripts]
> link-mcp = "link_mcp.server:main"
> lnk = "link_cli:main"
> --- `mcp_package/pyproject.toml`

### Ordinary invocation: a substantive question through slim MCP

An external user asks the foreground agent a question. Installed steering and MCP instructions ask that agent to recall before broad searches. That is a natural-language next-step policy, not enforced interception of every host model call. The agent decides whether and how to invoke `recall(query, budget, project, mode, limit, context_path)`. Link cleans the query, resolves project identity and selects a deterministic branch. Empty auto queries produce a startup brief; memory mode produces memory-only results; an ordinary nonempty auto query produces a combined query packet. See [RT-RTE-context-recall](#rt-rte-context-recall) and [RT-BAP-agent-steering](#rt-bap-agent-steering). SRC-1, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/agent_instructions.py`.

The server adapter builds/reuses a wiki cache and reloads memory records. The shared query function combines lexical/hybrid memory recall, wiki search and graph-neighborhood pages. Project visibility and lifecycle predicates apply to its memory branch, not its generic wiki branch. The latter enumerates all nonhidden Markdown, including memories excluded by focused recall, and can return archived, expired or another project's memory as a wiki page. It then compacts selected material, ranks the packet and builds a shorter recall capsule. Memory results carry review/lifecycle information; generic page provenance omits those fields. Budget information and follow-up tool arguments accompany the packet. This is a source-supported alternate delivery path, not an observed disclosure. See [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read). Optional numerical encoders affect memory similarity; optional reranking is a distinct explicit memory-only recall path, not a stage in this ordinary query packet. See [RT-CMP-model2vec](#rt-cmp-model2vec), [RT-CMP-fastembed](#rt-cmp-fastembed), [RT-CMP-reranker](#rt-cmp-reranker). SRC-1, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/query.py`, `mcp_package/link_core/memory.py`, `mcp_package/link_core/semantic.py`.

> This module keeps retrieval planning shared across CLI, HTTP, and MCP. It does
> not answer the user directly; it returns a compact, source-backed packet an
> agent can read before answering.
> --- `mcp_package/link_core/query.py`

The executor is the local Python process. Its immediate effect is JSON text returned through MCP; reads can also refresh derived semantic caches and retrieval accounting on selected paths. The external host adds tool results to its own model context. Neither final answer generation nor a host's shell/tool permission system is controlled by Link. The receiving agent can request larger budgets, full topic context, individual pages or direct files. Link does not remove earlier host turns or pop a separate model context. Its working-context control keeps most external content out of the first packet and restores selected additional content on demand. A capsule is an excerpt with follow-up instructions, not a reference that the model automatically dereferences. SRC-1, `mcp_package/link_core/query.py`, `LINK.md`, `mcp_package/link_mcp/server.py`.

### Material loops and forcing routes

1. **Write without a verified approval credential.** `remember` says user approval is required, but forwards caller arguments to a core write function, with caller-controlled secret/duplicate/conflict overrides. The core creates active, pending-review memory, not a reviewed-only quarantine invisible to recall. Reviewing is another callable mutation. The same principal with workspace access can use CLI, core API, HTTP mutations or direct Markdown editing. The relevant controls are code rejection of detected candidates and agent/user protocols; they do not authenticate that a human approved this exact content. See [RT-RTE-memory-admission](#rt-rte-memory-admission). SRC-1, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/memory.py`, `serve.py`, `LINK.md`.
2. **Automatic supply without an explicit recall.** Installed session-start hooks emit a brief into host context. Separately, MCP tool wrappers attach a compact brief to the first suitable JSON response of a server process, unless disabled. A pending handoff is prepended or placed prominently in that supply. Thus "retrieval happens only when the agent asks" would be false. A server-process flag is not an independently established host-session identity. See [RT-RTE-session-delivery](#rt-rte-session-delivery). SRC-1, `link.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/handoff.py`.
3. **Trace-fed capture is not the same as accepted memory.** Automatic session-end hooks extract user turns for proposal mining, use full retained notes for review context, suppress duplicates/echoes/dismissed proposals and create proposal-only captures. Manual session-end can mine its supplied text without the user-only extraction. Capture acceptance is separately callable and passes selected proposal text into the write path. See [RT-RTE-session-capture](#rt-rte-session-capture). SRC-1, `link.py`, `mcp_package/link_mcp/server.py`.
4. **Structured admission is stronger than agent-authored admission.** The structured adapter compares ownership hashes, stages pages and validates the staged wiki before copying changes. The arbitrary-source path tells an external agent to author wiki files and validate afterwards. Direct file writes bypass both procedures. This prevents assigning one global pre-write validation invariant to the wiki. See [RT-RTE-structured-ingest](#rt-rte-structured-ingest) and [RT-RTE-agent-wiki](#rt-rte-agent-wiki). SRC-1, `mcp_package/link_core/structured_ingest.py`, `LINK.md`.

These are source forcing cases, not executed attacks or experiments. Host callbacks, direct model calls, provider-native tools, sub-agents and remote application workers belong to excluded hosts; Link's handoff transfers text, not a running delegated worker. The included subprocess paths are LinkBar-to-CLI, explicit setup/repair and Git-based sync. No deployed grant set, installed hook configuration or OS isolation envelope is supplied. Workspace paths and localhost binding are code configuration, not evidence of a sandbox separating an agent from the files. SRC-1, `apps/LinkBar/Sources/LinkBar/LinkCLI.swift`, `mcp_package/link_core/agent_hooks.py`, `mcp_package/link_core/sync.py`, `serve.py`.

### Load-bearing guarantees and their actual enforcement points

| Guarantee and owner | Enforcement and strength | Covered and alternate paths; external contract | Conclusions |
|---|---|---|---|
| User-approved memory; foreground agent/user | Tool instructions, `LINK.md`, skills; **protocol** | Calls are requested to follow approval. Core API, direct Markdown, CLI and local HTTP have no independent human-content approval proof at the inspected write points. Requires host instruction adherence and honest caller inputs. | instruction conclusion status: wired; operation conclusion status: uninspected |
| Reject secret-shaped, duplicate or conflicting new memory; memory core | `write_memory_page` detection and early returns; **policy** | Shared callers using this function; explicit override arguments change rejection. Detection is heuristic, not a proof of absence of secrets or contradictions. Direct files and other admission mechanisms differ. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Local HTTP viewer/mutations; HTTP handler | Loopback bind, Host check, local-action header, browser-source checks, body limits and rate limiting; **policy** | HTTP request path only. Missing Origin/Referer is allowed; the marker header is not a user identity token. CLI/MCP/file access is outside this gate. Requires OS networking behavior; does not isolate local applications. | implementation conclusion status: wired; deployment conclusion status: uninspected |
| Offline recall model loading; semantic loader | Offline environment guard by default, download-enabled setup as exception; **policy** | Inspected built-in model loaders, not an OS network deny rule. Requires external libraries to honor their offline contracts. Explicit setup and evaluator download mode are alternate allowed network paths. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recoverable local writes; file/journal helpers | Per-file replace and locks, pre-write snapshots, exception rollback and interrupted-operation recovery; **best effort** | Journaled memory mutations. Not a serializable whole-workspace transaction or coverage of agent/Git/plain writes. Directory fsync is best effort. Recovery can report snapshot errors and needs explicit confirmation after interruption. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Project/lifecycle selection; memory core | `recall_memories` visibility and activity predicates; **policy** | Focused-memory recall and the combined packet's memory branch only; explicit archive/temporal options alter eligibility. Generic wiki search/context uses all nonhidden Markdown without these gates and can return excluded memories as pages. Requires callers to use the intended branch; not a workspace access-control or all-packet withdrawal guarantee. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Bounded context; query constructor | Item counts and excerpt sizes; **policy** | Combined packets by chosen budget. Full-page/context requests and manual reads bypass them. Token counts are estimates; no host-window cap is enforced. MCP autobrief drops trailing memories toward 4,000 characters, but does not truncate every possible non-memory field. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Safe structured update; adapter | Manifest ownership checks plus staged validation; **policy** | Adapter plan/apply path. Caller may adopt unmanaged outputs explicitly; agent edits, seed and restore have different gates. No concurrent workspace transaction is established. | implementation conclusion status: wired; operation conclusion status: uninspected |
| No secret-shaped outgoing wiki data; sync | Scan outgoing wiki file contents before push; **best effort** | `sync_workspace`, including team workspace use. Direct Git push is outside the scanner; it scans current wiki files rather than every historical blob or every tracked path. Requires remote/Git contracts and heuristic detection. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence and minimum passages for these findings are retained in the route records below. HTTP-specific support is SRC-1, `serve.py`, `mcp_package/link_core/web_http.py`:

> if path in {"/api/remember-memory", "/api/update-memory"}:
>     if not self._require_local_action_header({"saved": False}):
>         return
> --- `serve.py`

> for header_value in (origin_header, referer_header):
>     host = _browser_source_host(header_value)
>     if host is None:
>         continue
>     if host not in allowed:
>         return False, BROWSER_SOURCE_LOCAL_ONLY
> return True, None
> --- `mcp_package/link_core/web_http.py`

### Change admission, recovery and evidence coverage

Knowledge changes have several principals: a human supplies or approves memories; a host agent formulates arbitrary-source wiki content; deterministic software renders a supported export or project seed; software imports/synchronizes existing material. Human approval is required by some instructions, not by every content-producing mechanism. Source seeding deliberately differs from personal-memory approval. Raw copies, pending captures, wiki pages, handoffs, derived indexes and installed steering have different consumers and controls. [RT-RTE-project-seed](#rt-rte-project-seed), [RT-RTE-source-import](#rt-rte-source-import), [RT-RTE-workspace-sync](#rt-rte-workspace-sync), [RT-RTE-local-recovery](#rt-rte-local-recovery) preserve those distinctions. Memory revisions and detailed curation assessment are left to the memory member. SRC-1, `mcp_package/link_core/project_seed.py`, `mcp_package/link_core/obsidian.py`, `mcp_package/link_core/importers.py`, `mcp_package/link_core/sync.py`, `mcp_package/link_core/backup.py`.

Product/capability/production changes come through packaging, setup, runtime-copy repair, model provisioning and integration rewrites, not an inspected autonomous model-generated source-code improvement loop. LinkBar's explicit repair actions call init, semantic setup or an upgrade command, then inspect readiness. Installed steering can be replaced with the shipped current template. The recall evaluator compares lexical and hybrid retrieval against authored target IDs; this is an offline comparison, not a live answer oracle or automatic product-admission rule. See [RT-RTE-runtime-install](#rt-rte-runtime-install) and [RT-RTE-recall-evaluation](#rt-rte-recall-evaluation). SRC-1, `mcp_package/pyproject.toml`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`, `mcp_package/link_core/agent_instructions.py`, `scripts/eval_recall_quality.py`.

Added inspection beyond the boundary's initial bodies: implementation sections of `mcp_package/link_core/query.py`, `mcp_package/link_core/search.py`, `semantic.py`, `operations.py`, `files.py`, `web_http.py`, `handoff.py`, `project_seed.py`, `obsidian.py`, `importers.py`, `doctor.py`, `wiki.py`; extended `memory.py`, `sync.py`, MCP and CLI handlers; HTTP dispatch; LinkBar subprocess and repair bodies; recall evaluator selection/scoring. Added doctrine/design inspection: `LINK.md` operations and runtime instruction template/hook contracts. These are all SRC-1, not additional sources. Auxiliary share/snapshot/export internals, full validation internals, every installer and all evaluators/tests were not audited here. Their entry paths were located in the supplied boundary or source searches; equivalence of all their checks, security properties and evaluation outcomes is not asserted. Source availability is not an access gap. No overall effectiveness, complete security audit or all-path transaction claim follows from this runtime baseline.

## Shared records

### Components

#### RT-CMP-model2vec
Label: Model2vec static embedding provider

Source-native identity: the `model2vec.StaticModel` branch of the semantic loader. Representational form: distributed-parametric model and dense numerical output. Substrate: external local model cache and process `_MODEL_CACHE`; derived vectors use JSON under `.link-cache/semantic/`. Runtime code encodes text; no parameter-update/training step is present in this inspected loader. Exact weights/revision are not pinned: the default is a model name, overridable by environment. There is no inference-service endpoint here, but a model name/cache or subsequent setup can resolve to different weights; provider internals and weight identity remain uninspected. SRC-1, `mcp_package/link_core/semantic.py`, `mcp_package/pyproject.toml`.

> DEFAULT_SEMANTIC_MODEL = "minishlab/potion-base-8M"
> SEMANTIC_MODEL_ENV = "LINK_SEMANTIC_MODEL"
> --- `mcp_package/link_core/semantic.py`

> from model2vec import StaticModel
>
> model = StaticModel.from_pretrained(model_name)
> --- `mcp_package/link_core/semantic.py`

#### RT-CMP-fastembed
Label: Fastembed contextual embedding provider

Source-native identity: `fastembed.TextEmbedding` semantic branch, preferred automatically when installed except the CLI preference for installed model2vec. Representational form: distributed-parametric ONNX embeddings; substrate: external local model cache, in-process cache and derived JSON vectors. No inspected operation updates model parameters; embedding indexes do change. Exact weight revision is not pinned and `LINK_SEMANTIC_MODEL`/provider selection can change the model. No remote inference endpoint is wired by this branch; model-name resolution and library internals remain external. SRC-1, `mcp_package/link_core/semantic.py`.

> DEFAULT_FASTEMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
> --- `mcp_package/link_core/semantic.py`

> if provider == "fastembed":
>     from fastembed import TextEmbedding
>
>     model = TextEmbedding(model_name)
> --- `mcp_package/link_core/semantic.py`

#### RT-CMP-reranker
Label: Local cross-encoder reranker

Source-native identity: `fastembed.rerank.cross_encoder.TextCrossEncoder`, distinct from both embedding providers. Representational form: distributed-parametric model scoring query/document pairs; substrate: local model cache and process cache. No parameter training is wired in the inspected scoring path. Default model name is `Xenova/ms-marco-MiniLM-L-6-v2`, environment-overridable and not revision-pinned; there is no remote inference endpoint, but setup/cache resolution can change weights. Explicit memory recall overfetches up to at least 50 candidates and fuses retrieval/reranker ranks. Briefs/hooks and the shared combined query do not invoke that wrapper. The source comment says disabled by default, but the inspected `rerank_disabled` function disables only on explicit off-like values: absence of a switch alone does not disable an available model/provider. SRC-1, `mcp_package/link_core/semantic.py`, `link.py`, `mcp_package/link_mcp/server.py`.

> def rerank_disabled() -> bool:
>     return os.environ.get(RERANK_DISABLE_ENV, "").strip().lower() in {"off", "0", "false", "no"}
> --- `mcp_package/link_core/semantic.py`

> from fastembed.rerank.cross_encoder import TextCrossEncoder
>
> _set_offline_guard(allow_download)
> model = TextCrossEncoder(model_name)
> --- `mcp_package/link_core/semantic.py`

### Operative objects

#### RT-OBJ-link-instructions
Label: Link agent instructions

Source-native identity: `LINK.md` and the Link-owned installed steering section, with MCP instructions as another delivery surface for related policy. Representational form: natural-language procedures and templates consumed by agents/humans. Substrate: shipped Markdown, installed agent instruction files and Python string templates. Templates contain symbolic examples, but the operative instruction force described here depends on host interpretation. They say when to recall, how to approve memories, how to compile sources and how to check completion. Shipped text is static until installation/refresh or authorized human/agent editing; it is not itself read-back of use-derived memory. SRC-1, `LINK.md`, `mcp_package/link_core/agent_instructions.py`, `mcp_package/link_mcp/server.py`.

> **LINK.md** — This file. The schema that tells you how the wiki works. You and the human co-evolve this over time.
> --- `LINK.md`

#### RT-OBJ-operation-journal
Label: Operation journal and snapshots

Source-native identity: `wiki/.link-operations/` pending/failed markers and adjacent pre-write snapshot directories. Form: symbolic JSON status/path/manifest records plus file-byte snapshots. Substrate: local filesystem. Consumers: journal completion/error handling, doctor/status and explicit recovery. It records write/recovery state, not a theory or improved answer policy. Per-target locks and snapshots should not be confused with workspace-level serialization. SRC-1, `mcp_package/link_core/operations.py`, `mcp_package/link_core/files.py`.

> def operation_dir(wiki_dir: Path) -> Path:
>     return wiki_dir / OPERATION_DIR_NAME
> --- `mcp_package/link_core/operations.py`

### Routes

#### RT-RTE-context-recall
Label: Bounded context recall

Endpoints/progression: host question/tool request → MCP/CLI/HTTP adapter → shared query or focused memory/brief branch → JSON/text packet → external agent. Owner: code selects/ranks retained items; foreground agent selects tools and interprets answers. Context/state: wiki cache, memory records, project, query and selected budget; focused recall optionally uses context path, temporal date and model scores. Effects: local read, possible semantic-cache refresh and selected retrieval-ledger writes; no application action executor. Operating mode: open requests; no runtime expected-answer oracle. Providers/components are the three component records above. SRC-1, `mcp_package/link_mcp/server.py`, `link.py`, `mcp_package/link_core/query.py`, `mcp_package/link_core/memory.py`, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/semantic.py`.

- Immediate return: JSON context packet, capsule, provenance, warnings and follow-up actions; focused mode returns selected memories and abstention information.
- Later read-back: retained Markdown is reloaded at later invocations; refreshed vector caches are reused by subsequent similarity queries.
- Delegated visibility: tool results go to the calling host; any further delegation depends on that host, not Link.
- Selection predicate: focused-memory recall and the combined packet's memory branch apply project visibility and lifecycle filters, lexical plus optional semantic score and review/applicability ranking. Pending review does not itself exclude active memory; out-of-context memory is demoted and labeled, not universally omitted. The combined packet's generic wiki branch instead searches all nonhidden Markdown and selects ranked pages plus graph neighbors without memory project/lifecycle gates. It can deliver archived, expired or another project's memory as a page. Item/excerpt budgets clip combined output; generic page provenance omits memory lifecycle/review fields.
- Invalidation or expiry: Markdown/cache signatures and mtime drive rebuilds; semantic text hashes/model key invalidate vectors. Focused temporal recall determines earlier eligibility from lifecycle fields, not historical body versions. Archive/expiry/project predicates do not withdraw a still-present memory page from the generic wiki branch.
- Activation or effect: wired delivery and ranking; external answer/action dependence is uninspected without host traces.
- Evidence limits: source only; no recall success, model weight identity, host compliance or token-cost benefit measured here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> elif applicability == "out_of_context":
>     # Conditional memory outside its context: still findable,
>     # but demoted and labeled so agents do not apply it blindly.
>     rank_score = max(1, rank_score - 10)
> --- `mcp_package/link_core/memory.py`

> if index.get("model") != model:
>     items = {}
> --- `mcp_package/link_core/semantic.py`

The generic wiki branch is the material part identified by [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read); it is not another focused-memory selector. Added correction inspection covers enumeration and topic context in `mcp_package/link_core/wiki.py`, the complete `search_pages` selector in `mcp_package/link_core/search.py`, and branch assembly/page compaction in `mcp_package/link_core/query.py`, all implementation evidence from SRC-1. Their source text supports branch coverage, not actual disclosure or host reliance.

> def _markdown_page_paths(wiki_dir: Path) -> list[Path]:
>     return sorted(path for path in wiki_dir.rglob("*.md") if not path.name.startswith("."))
> --- `mcp_package/link_core/wiki.py`

> raw_search_results = search_pages(q, cache, limit=limits["search_results"] + 1)
> search_has_more = len(raw_search_results) > limits["search_results"]
> search_results = raw_search_results[: limits["search_results"]]
> context = context_for_topic(
>     wiki_dir,
>     q,
>     cache,
>     limit=limits["context_pages"] + 1,
> )
> --- `mcp_package/link_core/query.py`

> if not memory_visible_for_project(record, project_name):
>     continue
> if memory_type and str(record.get("memory_type") or "") != memory_type:
>     continue
> --- `mcp_package/link_core/memory.py`

The offline loader sets environment guards, catches failed load and falls back to lexical paths. This is not a process-level network firewall. The evaluator explicitly supports download-enabled model loading. SRC-1, `mcp_package/link_core/semantic.py`, `scripts/eval_recall_quality.py`.

> os.environ["HF_HUB_OFFLINE"] = "1"
> --- `mcp_package/link_core/semantic.py`

#### RT-RTE-memory-admission
Label: Explicit memory admission

Endpoints/progression: caller text or accepted proposal → shared memory writer → Markdown page, index, log/backlinks → result → later recall. Owner: caller proposes and chooses overrides; software infers type when omitted and rejects detected secrets/conflicts/duplicates unless permitted. Human supplies/approves under the protocol, but no independent approval artifact is checked by these functions. CLI, MCP, web and LinkBar are alternate callers; direct file authoring bypasses this mechanism. Operating mode: open durable-memory requests; answer oracle: inapplicable, no reference outcome is used. Guidance: only remember explicit/approved content and resolve conflicts with the human. Persisted result: active pending-review memory and lineage on supersession. Rejection: caller can stop; core can return `created: False`; user can decline proposals. Recovery: journal snapshots on failure, archive/restore or explicit forget later. Detailed update/review/curation belongs to the memory analyst. SRC-1, `mcp_package/link_core/memory.py`, `mcp_package/link_mcp/server.py`, `serve.py`, `LINK.md`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`.

- Immediate return: created page identity/path or refusal/candidate data; not a proof of user assent.
- Later read-back: active memory is eligible for recall with review state and warnings.
- Delegated visibility: workspace readers and connected hosts can read the plain files; visibility fields and project filtering are consumer policies, not OS access control.
- Selection predicate: explicit text or capture index; allowed type/scope/visibility and date syntax; detected secret/conflict/duplicate checks with caller overrides.
- Invalidation or expiry: archive/supersession and lifecycle dates alter focused-memory eligibility, not generic wiki delivery of a still-present page; forget removes the page. Updating resets pending review; adapter clears cache after successful write.
- Activation or effect: code writes durable context; downstream agent reliance is unobserved.
- Evidence limits: approval is a protocol; actual human control and truth of content cannot be inferred from callable mutations or `source` strings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> status: active
> date_captured: "{timestamp}"
> source: "{frontmatter_string(clean_source)}"
> review_status: pending
> --- `mcp_package/link_core/memory.py`

> allow_duplicate=allow_duplicate, allow_conflict=allow_conflict,
> allow_secret=allow_secret,
> **options,
> --- `mcp_package/link_mcp/server.py`

#### RT-RTE-session-capture
Label: Session proposal capture

Endpoints/progression: host session-end event/transcript or explicit notes/import → text extraction/mining → raw capture and proposal response → later inbox/accept-capture → memory admission. Owner: hook code selects user turns and filters proposals; deterministic miner proposes, human is asked to decide, caller executes acceptance. Automatic capture retains review context without approving durable memory. Manual `session-end` accepts supplied text and can mine it all; imported instruction/auto-memory units carry their original mixed provenance, not automatically a user's own utterances. Mode: open session/import inputs; no reference-answer oracle. Trigger/improvement intent: preserve potentially useful context for later work, not an evaluated improvement loop. User may decline/delete/redact; dismissed fingerprints suppress future automatic proposals. Acceptance can be vetoed by the memory writer's gates. SRC-1, `link.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/importers.py`, `mcp_package/link_core/capture.py`.

- Immediate return: proposal-only capture location and candidates/warnings; hook early exits if no usable/fresh proposals.
- Later read-back: capture inbox and startup review summaries reload raw captures; accepting a selected proposal creates memory later eligible for recall.
- Delegated visibility: local workspace and review callers see capture text; automatic delivery of review summaries does not establish full transcript delivery to every host.
- Selection predicate: automatic user-only head/tail mining; minimum conversation length, duplicate/echo/dismissed/pending checks; manual notes differ; acceptance selects proposal index with metadata overrides.
- Invalidation or expiry: conversation identity permits in-place refresh; deletion records dismissed proposals; redaction changes retained text; hook fingerprint suppresses repeated events.
- Activation or effect: wired raw capture and candidate retention, not automatic approval; accepted-content influence remains unobserved.
- Evidence limits: host event/transcript format and availability are external contracts; user-only provenance covers automatic extraction, not every manual or import path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> user_notes = _core_extract_transcript_text(
>     transcript_path, roles=("user",), max_chars=9000, keep_head=True
> )
> --- `link.py`

> proposal_text if proposal_text is not None else text,
> --- `link.py`

#### RT-RTE-session-delivery
Label: Session brief and handoff delivery

Endpoints/progression: installed start hook → stdout/host context; or first suitable MCP tool response → attached brief; explicit handoff → local packet → next start/brief → receiving agent. Owner: code selects and formats, host schedules hooks and receives text, model decides subsequent behavior. State: project, retained memories, pending captures, handoffs, server-process `_session_brief_sent` and optional usage ledger. Startup hooks and MCP attachment are independent delivery channels. Prompt-check hooks can also emit a saved-constraint reminder with cooldown. Handoff is a text relay, not delegated execution. Admission: caller writes supplied handoff content with redaction and TTL; human is asked to offer/approve the handoff by steering, not authenticated per-content in core. Rejection: do not call writer, clear packet or let it expire; no outcome oracle. Mode: host events and open requests. SRC-1, `link.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/agent_hooks.py`, `mcp_package/link_core/handoff.py`.

- Immediate return: bounded brief, optional top-priority handoff and review information; per-prompt guard normally emits nothing.
- Later read-back: retained handoff and memories reach later host invocation through hook or MCP response.
- Delegated visibility: receiving sessions may belong to different agents using the workspace; no automatically copied full source context or live worker identity is established.
- Selection predicate: project/lifecycle/brief ranking; newest pending handoff first; first eligible JSON dictionary response per server process; guard overlap/cooldown predicates.
- Invalidation or expiry: autobrief can be disabled; process flag prevents repeat attachment; handoff expiry suppresses surfacing without deleting history, explicit clear deletes; resumed hook contexts are intentionally not matched in the nested default config.
- Activation or effect: emitted material instructs resume/rely/verify; actual changed host behavior is uninspected.
- Evidence limits: installation and host trust/scheduling not observed; autobrief process lifetime is not proven equivalent to a user's session; 4,000-character dropping loop is not an absolute bound on every non-memory field.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if _session_brief_sent or _autobrief_disabled() or not isinstance(result, str):
>     return result
> --- `mcp_package/link_mcp/server.py`

> while memories and len(json.dumps(compact, ensure_ascii=False)) > SESSION_BRIEF_MAX_CHARS:
>     memories.pop()
>     compact["truncated"] = True
> --- `mcp_package/link_mcp/server.py`

> "Resume this task before anything else, then clear it: "
> --- `mcp_package/link_core/handoff.py`

#### RT-RTE-agent-wiki
Label: Agent-authored wiki change

Endpoints/progression: human adds raw material/asks ingest, query filing, research or lint → external agent reads source/instructions and proposes/authors wiki → rebuild/validate → later query consumption. Owner: agent interprets content and writes; human decides sources, filing and proposed lint fixes. Context: existing pages, raw sources, templates and links; executor/effect boundary: host file/shell tools, not an internal Link model call. Admission guidance requires source links, explicit contradictions, rereading coherence, and completion validation. Ordinary source ingest is authorized at workflow level, not necessarily per-claim human approval. Research selection and filing have additional human decisions. No answer oracle: confidence labels are authored assertions, not reference judgments. Operating mode: open work, including periodic lint proposals. Rollback: backup before risky edits and manual correction; validation after writing is a completion blocker, not universal pre-write prevention. SRC-1, `LINK.md`, `mcp_package/link_mcp/server.py`.

- Immediate return: external agent reports takeaways/answer/proposals and eventually changed wiki; Link status alone returns a plan, not compilation.
- Later read-back: authored source/concept/entity/comparison/exploration pages feed later search/graph query packets.
- Delegated visibility: agents/humans sharing workspace receive selected pages; external host decides any further model delegation.
- Selection predicate: significant concepts/entities/claims, existing page matching and selected raw sources; these are natural-language agent judgments.
- Invalidation or expiry: explicit updates, source staleness reports, lint and index rebuild; source instructions treat raw as immutable but manual file access is not blocked by this text.
- Activation or effect: requested authoring and future consumption; successful compilation, faithful grounding and changed answers are unobserved.
- Evidence limits: implemented status/rebuild/validation capacity does not establish model compliance with source-grounding or contradiction procedures.
- instruction conclusion status: wired
- operation conclusion status: uninspected

> Check for contradictions with existing pages — note them in both pages' Open Questions
> --- `LINK.md`

Theory account: page templates expose claims, mechanisms, open questions and sources, so an authored page could contain a formulated theory; the empty scaffold does not supply one. Guidance asks agents to criticize contradictory content but does not codify blame/test/revision decisions. `theory-builder conditions 1–4`: condition 1 conclusion status: afforded — templates permit localized theories, no actual candidate supplied; condition 2 conclusion status: uninspected — no decision trace depending on such a theory; condition 3 conclusion status: claimed — contradiction checking is requested, not observed content-directed criticism with blame; condition 4 conclusion status: uninspected — persisted pages/open questions enable later access but no traced criticism-shaped next round is supplied. Addressability: headings/claims provide coarse editable units; finer actual assumptions depend on authored content. Persistence: wiki pages across sessions, not an established iterated theory. Learning: improved future capacity unestablished. Reflection: lint represents wiki aspects and can prompt edits, but this source does not establish an exercised self-representation loop or reflective theory building. Autonomous theory builder: unestablished; human source/admission choices and opaque host interpretation remain material. These are independent limits, not a bundled absence claim. SRC-1, `LINK.md`.

#### RT-RTE-structured-ingest
Label: Structured export admission

Endpoints/progression: CLI supported raw export → adapter plan → conflicts/preview → explicit apply → staged generation/log/index/backlinks/validation → copy outputs and manifest → later wiki recall. Owner: deterministic adapter proposes generated change; caller decides apply/exclusion/adoption/pruning; code vetoes conflicts and failed staged validation. Mode: open supported export requests, not an adaptive curriculum. Answer oracle: inapplicable — shape/link validation is not a semantic expected answer. Guidance is adapter schema/rendering and validation rules. Persisted material: wiki outputs plus source/output hashes under `.link-ingest/`. Recovery: caught copy exceptions restore saved originals; no universal crash or concurrent-write isolation guarantee. SRC-1, `mcp_package/link_core/structured_ingest.py`, `link.py`, `LINK.md`.

- Immediate return: plan/conflicts by default; applied count/validation on successful apply; exception on conflict/invalid staged wiki.
- Later read-back: generated wiki knowledge reaches shared search/graph consumers; manifest hashes govern later adapter updates.
- Delegated visibility: no inner model delegation; output pages available to ordinary workspace consumers.
- Selection predicate: supported adapter, source inside raw workspace, rendered groups minus exclusions; prior hashes distinguish managed unchanged output from modified/unmanaged conflicts.
- Invalidation or expiry: source/hash change plans new outputs; prune is explicit, otherwise obsolete outputs remain; manually changed outputs block replacement.
- Activation or effect: deterministic wiki mutation after staged validation; factual benefit to later answers unobserved.
- Evidence limits: generated knowledge has no automatic truth oracle; planning and subsequent application are not established as one workspace transaction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> validation = validate_wiki(stage_wiki)
> if not validation.get("passed"):
>     raise StructuredIngestError(f"staged wiki failed validation: {validation.get('findings')}")
> --- `mcp_package/link_core/structured_ingest.py`

#### RT-RTE-project-seed
Label: Source-backed project seeding

Endpoints/progression: caller/agent requests seed after empty context → bounded project-file reader and optional Git history → raw project seed and wiki source page → rebuilt graph → retry recall. Owner: software selects/renders; caller chooses root/name/options and whether to overwrite/dry-run. Unlike memory approval, shipped steering permits this source-backed knowledge creation before broad search. Rejection: blocked secrets/read errors, existing outputs without overwrite, empty inputs or caller abstention. No answer oracle; mode: open project bootstrap. Persisted guidance/source: selected project docs/rules/history, not an approved personal preference claim. Recovery: overwrite is explicit; no operation-journal rollback is shown in this seed body. SRC-1, `mcp_package/link_core/project_seed.py`, `mcp_package/link_core/agent_instructions.py`.

- Immediate return: status/included/skipped/blocked/read-error counts, output paths and next commands.
- Later read-back: generated source-backed page becomes available to query/graph consumers; raw snapshot remains provenance.
- Delegated visibility: workspace consumers; no internal model call in the seed writer.
- Selection predicate: configured bounded project-file reader, file/byte limits and secret scan; optional Git-log inclusion.
- Invalidation or expiry: repeat seed detects existing outputs; overwrite or later ingest/update needed for refreshed sources.
- Activation or effect: wired automatic source-page generation when eligible and not dry-run; later answer dependence unobserved.
- Evidence limits: workflow invocation is not human approval of each generated passage; no deployed project state or actual seed execution supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> would_write = bool(included) and not blocked_secret and not read_errors
> --- `mcp_package/link_core/project_seed.py`

#### RT-RTE-source-import
Label: External source import

Endpoints/progression: explicit Obsidian vault import → size/secret/existing-file checks → copies Markdown under raw → caller subsequently uses agent-authored ingest. Distinct from instruction/auto-memory import, whose text units enter proposal capture through [RT-RTE-session-capture](#rt-rte-session-capture), and from project seed, which also generates a wiki source page. Owner: caller selects vault/options, software copies eligible notes; later agent/human controls wiki admission. Mode: open import; answer oracle: inapplicable. Proposal is a source copy, not a new evaluated knowledge claim. Caller can veto/dry-run; existing-file overwrite requires option. Recovery is manual source cleanup; original vault remains outside destination writes. SRC-1, `mcp_package/link_core/obsidian.py`, `mcp_package/link_core/importers.py`, `LINK.md`.

- Immediate return: import report and next ingest/status commands.
- Later read-back: copied raw notes can later be consumed by an ingesting agent; import alone does not create recalled wiki knowledge.
- Delegated visibility: raw files remain locally accessible; later delivery depends on ingest and retrieval.
- Selection predicate: discovered Markdown notes, optional limit, maximum bytes, secret scanner and existing-file/overwrite choice.
- Invalidation or expiry: existing destinations skipped unless overwrite; no continuous vault synchronization established.
- Activation or effect: eligible raw copies are written unless dry-run; downstream knowledge activation is conditional on later ingest.
- Evidence limits: no imported real corpus or semantic source-preservation test run supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not dry_run:
>     atomic_write_bytes(destination, data)
> --- `mcp_package/link_core/obsidian.py`

#### RT-RTE-workspace-sync
Label: Workspace and team sync admission

Endpoints/progression: explicit sync → local Git commit → fetch/merge/conflict resolution → outgoing wiki scan → push; team path exports active team-visible memories into a separate workspace, syncs it, then imports missing names, keeping differing local files. Owner: caller chooses remote and invokes; code resolves conflicts with fixed policies, not human review of every incoming item. New remote/imported text can enter later recall without the ordinary memory writer. Mode: open explicit synchronization; no answer oracle. Proposed change is retained workspace content; code can reject push for detected secrets or fail Git operations; human reconciliation is requested for both-version conflicts. Recovery: Git history and later edit/consolidate; no evidence of universal rollback of fetch/merge/commit on failed push. SRC-1, `mcp_package/link_core/sync.py`, `link.py`, `LINK.md`.

- Immediate return: commit/pull/push status, conflict resolutions and secret findings; a blocked push can follow already committed/merged local state.
- Later read-back: imported/merged wiki text becomes visible to later local retrieval; conflict siblings are retained for review.
- Delegated visibility: configured Git remote and other machines; team export initially filters active team visibility, not personal private/project pages.
- Selection predicate: Git workspace changes for ordinary sync; outgoing scanner restricts to wiki files; team export active/team-visible and team import filename collision policy.
- Invalidation or expiry: subsequent sync reconciles new changes; archive/visibility changes affect future export selection, but the inspected export only copies and does not establish deletion of previously exported remote files.
- Activation or effect: durable local/remote file changes; later agent dependence and correctness unobserved.
- Evidence limits: no remote trust/authentication/actual deployment evidence; secret scanning is current-file heuristic and direct Git operations bypass it; team visibility is not an access-control boundary after copies exist.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> findings = _outgoing_secret_findings(root, branch)
> pushed = False
> if findings:
> --- `mcp_package/link_core/sync.py`

> if not target.exists():
>     target.write_text(content, encoding="utf-8")
>     imported.append(path.stem)
>     continue
> --- `mcp_package/link_core/sync.py`

#### RT-RTE-local-recovery
Label: Local write and restore recovery

Endpoints/progression: journaled memory mutation → pending marker/pre-write snapshots → writes → finish or exception rollback; interrupted operation → inspect recovery preview → confirmed snapshot restore. Separate backup path creates archive, then confirmed restore stages extraction and replaces selected roots, validating afterwards. Owner: software snapshots/restores; caller selects marker/archive, confirms and can veto. Mode: bounded recovery requests; expected state is pre-write bytes or selected archive, not an answer oracle. Proposed change restores retained state; persisted markers/snapshots enable interrupted recovery. Backup defaults to wiki only, retains up to configured count; raw opt-in differs. SRC-1, `mcp_package/link_core/operations.py`, `mcp_package/link_core/files.py`, `mcp_package/link_core/backup.py`.

- Immediate return: mutation result/error; recovery/restore preview or restoration report with errors/integrity.
- Later read-back: restored wiki/raw content is consumed in later invocations; pending/failed markers are read by health/status and recovery.
- Delegated visibility: local consumers only unless other explicit sharing/sync operations follow.
- Selection predicate: journal's named touched paths or inspected safe archive roots; explicit confirm for manual recovery/restore.
- Invalidation or expiry: completed journals remove marker/snapshots; backup count prunes older archives; recovery replaces prior content and restore can supersede newer state.
- Activation or effect: byte/state restoration is wired; semantic validation after backup restore reports issues rather than preventing all replacement.
- Evidence limits: per-file locks and atomic replace do not serialize whole read-modify-write workflows; agent direct writes/Git conflicts bypass helpers; crash recovery and concurrency behavior not executed here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except BaseException as exc:
>     rollback = _rollback_snapshots(marker)
>     fail_operation(marker, exc, rollback=rollback)
>     raise
> --- `mcp_package/link_core/operations.py`

> os.replace(tmp_name, target)
> _fsync_directory(target.parent)
> --- `mcp_package/link_core/files.py`

#### RT-RTE-runtime-install
Label: Runtime and integration change admission

Endpoints/progression: install/connect/setup or LinkBar repair click → package/runtime/config changes → readiness inspection → later command/host operation. Owner: human/operator initiates; software copies shipped runtime, registers MCP, writes hook/config/steering or provisions model dependencies. Package maintainers supply code; no model-authored product successor selection is established here. Guidance is shipped setup/repair policy; generated MCP config names Python command and slim tool surface. Caller can decline/run manual commands; readiness checks can show failure but are not semantic product-approval oracles. Mode: open setup/repair, externally released package updates. Recovery: refresh/reinstall or manual correction; package rollback not inspected. SRC-1, `mcp_package/pyproject.toml`, `integrations/claude-code/install.sh`, `mcp_package/link_core/agent_hooks.py`, `mcp_package/link_core/agent_instructions.py`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`, `apps/LinkBar/Sources/LinkBar/LinkCLI.swift`.

- Immediate return: setup/repair status, next actions and readiness; LinkBar rechecks semantic/MCP readiness after attempted changes.
- Later read-back: installed steering/config/runtime and local models shape later invocations; these are deployment changes, not themselves use-derived memories.
- Delegated visibility: host instruction files/MCP registration expose tools and policy to that host; model context inheritance follows external host contracts.
- Selection predicate: selected agent/global/project mode, current shipped template, repair command or explicit setup choice; optional provider/model environment selection.
- Invalidation or expiry: current-template refresh replaces stale Link-owned instruction sections; init/upgrade refreshes runtime; installed model/cache version remains unpinned.
- Activation or effect: wired installation/remediation affordances; actual loading/host trust and subsequent behavior are unobserved.
- Evidence limits: no installed configuration or supply-chain reproduction; a smaller MCP surface does not prove narrower filesystem permission; no autonomously generated code update/effect trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _ = try? LinkCLI.runRaw(command)
> let after = try? LinkCLI.runJSON(MCPVerify.self, ["verify-mcp", LinkCLI.workspace, "--json"])
> --- `apps/LinkBar/Sources/LinkBar/LinkStore.swift`

#### RT-RTE-recall-evaluation
Label: Offline recall comparison

Endpoints/progression: maintainer invokes evaluator → authored corpus/cases → lexical or fake/real semantic retrieval → rank metrics by overlap/domain → report/comparison. Owner: code scores target rank; humans supply dataset and choose evaluation mode. Proposer/decider/veto: evaluator proposes no content/product successor; maintainer decides any later change, not wired here. Answer oracle: authored `case['target']` memory identity from `scripts/recall_dataset.py`, compared against returned names; it is not a generative answer judge. Mode: bounded offline benchmark; real mode can explicitly allow model download. Improvement trigger: regression check for hybrid versus lexical, not automatic deployment/admission. Persisted material: evaluator output if externally retained; no runtime update from this function. SRC-1, `scripts/eval_recall_quality.py`.

- Immediate return: metrics and latency report; regression comparison determines process result elsewhere in the evaluator.
- Later read-back: inapplicable — this inspected scoring function does not write a durable behavioral update for recall to load.
- Delegated visibility: inapplicable — no inner generative agent delegation in this evaluator.
- Selection predicate: authored query/target cases, measured token-overlap grouping, configured mode/suite and top-five retrieval ranks.
- Invalidation or expiry: inapplicable — a fresh invocation recomputes metrics from supplied corpus/model; no admitted checkpoint lifecycle here.
- Activation or effect: scoring capacity wired; no benchmark executed and no resulting product change/benefit observed in this run.
- Evidence limits: target-rank metrics do not establish truth or end-to-end answer quality; external reported QA adapter/judgments remain outside supplied evidence as stated in boundary.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> names = [str(item["name"]) for item in results]
> rank = names.index(case["target"]) + 1 if case["target"] in names else 0
> --- `scripts/eval_recall_quality.py`

### Claims

#### RT-CLM-approved-memory
Label: Approved memory contract

Claimed operation: agents save durable memory only when the human asks or approves. This is the shipped behavioral contract, not evidence that the writer validates a human credential. Its natural-language consumers and limits are [RT-BAP-agent-steering](#rt-bap-agent-steering) and [RT-RTE-memory-admission](#rt-rte-memory-admission). SRC-1, `LINK.md`, `mcp_package/link_mcp/server.py`.

> Only save memories the human explicitly asks to remember or confirms should be remembered.
> --- `LINK.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-steering
Label: Installed agent steering authority

Consumer: foreground external agent. Channel: installed host instruction section, `LINK.md`, MCP server instructions/resources/prompts and packet guidance. Force: natural-language request to recall, obtain approval, validate and prefer bounded context; no independently enforced host tool permission or answer constraint. Horizon: host sessions while installation/template remains loaded. Static steering is not retained experience; changing installed policy can change later requests to the host, with loading/compliance unobserved. SRC-1, `mcp_package/link_core/agent_instructions.py`, `integrations/claude-code/install.sh`, `mcp_package/link_mcp/server.py`, `LINK.md`.

> Otherwise, keep working normally after the cheap first recall; do not save durable memory unless the user asks or approves it.
> --- `mcp_package/link_core/agent_instructions.py`

#### RT-BAP-context-packet
Label: Retained context authority

Consumer: receiving agent/human after recall or startup injection. Channel: selected memory/wiki excerpts, procedure steps, warnings and pending handoff in tool JSON or hook stdout. Force: context and instructions interpreted by the host model, distinct from symbolic selection by Link code. The handoff explicitly asks priority task resumption; out-of-context/weak/review-due material asks cautious reliance. Horizon: later invocations/sessions across agents using the workspace, bounded by each consumer's selection. Memory lifecycle/project gates cover focused-memory delivery, not generic wiki delivery of still-present memory pages; generic page compaction also omits memory lifecycle/review fields. Delivery is wired; behavioral dependence and improvement are not observed. SRC-1, `mcp_package/link_core/query.py`, `mcp_package/link_core/memory.py`, `mcp_package/link_core/handoff.py`, `link.py`, `mcp_package/link_mcp/server.py`.

> "Prefer recall-ready reviewed memories for personalization and source-backed wiki pages for factual claims.",
> --- `mcp_package/link_core/query.py`

## Annotations

none
