---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Smriti MCP runtime baseline: caller-driven durable writes, recall, trace consolidation and maintenance at the frozen source revision."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
---

# Smriti MCP runtime report

## Runtime account

Smriti executes memory operations, not a model's next-action loop. An external agent or operator chooses the tool, supplies content and consumes the response. Inside Smriti, Python rules choose paths, matches, ranking and file effects. The [boundary](boundary.md) registers SRC-1, the sole evidence source. All findings below are implementation or declared-design findings at that revision. No target code or tests were executed; exercised operation, model compliance and downstream benefit remain unobserved.

### Entry and ordinary invocation

The installed `smriti-mcp` entry point dispatches to `smriti_mcp.cli:main`; option-only and empty invocations normalize to `server`. The server subcommand resolves `--memory-root` (environment fallback `SMRITI_MEMORY_ROOT`, then the home-directory default), creates a server and calls FastMCP with `stdio` by default or caller-selected `sse`. `create_server` captures one `MemoryStore` instance in its registered tool wrappers. The store resolves/creates its root and owns an instance-local `RLock`. These are process/store identities, not user isolation domains (SRC-1, `pyproject.toml`, `src/smriti_mcp/cli.py`, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`).

> server = create_server(Path(args.memory_root).expanduser())
> server.run(transport=args.transport)
> --- `src/smriti_mcp/cli.py`

An ordinary write proceeds from host request through the MCP `create_memory` wrapper, Pydantic metadata serialization and `MemoryStore.create_memory`: derive any missing description, clean metadata, derive or clean ID, resolve its path, reject an existing target under the lock, add timestamps, serialize YAML plus body, write a temporary file beside the destination and replace the destination. Return is the ID and absolute path. A later `get_memory` independently reloads the file and returns complete serialized Markdown. The host then owns the next step. [RT-RTE-memory-write](#rt-rte-memory-write) captures admission, direct-library alternatives and failure boundaries; [RT-CMP-memory-store](#rt-cmp-memory-store) identifies the executor.

The integration test supplies a source-level example of create → search without body → get → build index over stdio, followed by filesystem assertions. It establishes the intended protocol round trip, not a supplied successful execution (SRC-1, `tests/test_smriti_mcp_integration.py`). Packaging depends on MCP, Pydantic and PyYAML; their internal transport/security behavior is not frozen by this source. SSE serving therefore does not establish authentication, remote isolation or deployment safety.

### Material routes and forcing cases

1. **Explicit versus automatic write.** `remember` searches candidates even in explicit modes, chooses append automatically only for a sufficiently scored equal title, then writes and finally records a trace. Explicit append/update bypass the automatic match decision; lower-level create/update/append do not require traces. Thus neither semantic duplicate prevention nor universal audit logging follows. Its returned reason begins with a no-match message and is not revised for every explicit mode, so the action and actual branch are stronger evidence than that prose (SRC-1, `src/smriti_mcp/store.py`; [RT-RTE-memory-write](#rt-rte-memory-write)).
2. **Recall is bounded delivery, not host context ownership.** The caller requests retrieval; code scans current files, ranks, optionally adds one-hop wikilink/backlink neighbors, formats snippets and applies a word-count heuristic. It does not trim an existing conversation or create an isolated agent frame. `include_content=False` on search and the recall bundle can keep full bodies out of a response; full retrieval remains reachable by ID. The first recall item may exceed the budget. Archived exclusion is a recall default with explicit overrides, not universal access denial: search/list/get have materially different defaults. Expiry downranks rather than deletes (SRC-1, `src/smriti_mcp/store.py`; [RT-RTE-context-recall](#rt-rte-context-recall)).
3. **Trace review is not automatic synthesis.** Trace grouping and recommendations return raw events plus related-memory metadata. The external caller supplies consolidated prose. Consolidation append ignores the newly assembled metadata, including trace-source metadata; update/create apply it. Trace identifiers are provenance strings, not validated support. A memory write followed by a failed trace append is not rolled back (SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`; [RT-RTE-trace-consolidation](#rt-rte-trace-consolidation)).
4. **Maintenance does not share all ordinary-write guarantees.** CLI and MCP rebuild can repair metadata, rewrite wikilinks and regenerate indexes. Frontmatter repair and index writes use direct writes, unlike ordinary note replacement. Repair scanning excludes every hidden path component, whereas store scanning has different exclusions. In particular a hidden default root can suppress repair scanning without suppressing all store operations. Dry-run repair only checks title/category, so its report is not a complete preview of all real repairs (SRC-1, `src/smriti_mcp/fix_frontmatter.py`, `src/smriti_mcp/store.py`; [RT-RTE-store-maintenance](#rt-rte-store-maintenance)).

These cases were inspected in source, not experimentally exercised. They challenge the most consequential generalizations: automatic capture, strict context budgets, universal provenance and uniform durability. No autonomous summarizer or internal model invocation is required by these paths. External hosts may use distributed-parametric models, but none is an owned component of this inspected Smriti execution chain; provider versions, mutable endpoints and weight changes are outside the frozen artifact, not inferred fixed.

### Controls, authority and recovery

The capability surface includes create, replace, append, read, rank, delete, archive, supersede and batch repair/indexing. All registered tools capture the same store; caller-supplied author, source-agent, visibility and scope values serve metadata/filtering roles rather than authenticated principals. Current host grants and approval settings are not supplied. The actual filesystem permissions, process isolation and transport exposure are also unobserved. Smriti's tool declarations must not be confused with either the host's grant set or a deployed sandbox (SRC-1, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`).

The bounded file controls are recorded in [RT-CLM-file-controls](#rt-clm-file-controls). Ordinary ID-based operations resolve paths and check root containment, but `record_trace` constructs an agent-named path without that resolver; arbitrary agent strings therefore prevent a universal root-containment conclusion. The instance-local lock does not coordinate distinct processes or stores, direct file editors, or every scan/rebuild operation. Atomic replacement is per note, not a transaction across note and trace, both sides of supersession, or both generated indexes. There is no inspected automatic rollback for those composite operations; callers can receive exceptions after earlier effects persist. Permanent deletion has no target-managed undo. These limits follow from the concrete write sequences, not observed failures (SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`, `src/smriti_mcp/fix_frontmatter.py`).

Retained text receives possible downstream behavioral force only when an external consumer interprets it; Smriti delivers it without establishing compliance. Shipped tool instructions have a separate host-facing channel ([RT-BAP-tool-guidance](#rt-bap-tool-guidance)). Knowledge admission is implemented by caller-supplied writes; maintenance admits deterministic transformations after invocation. Product/package changes are not admitted by these memory tools. No runtime extension loading, shell tool, remote worker delegation, provider-native tool loop or model mutation was found in the inspected CLI/server/store paths; this is a bounded source account, not a claim about the enclosing host. Memory content, detailed revision semantics and specialist learning assessments remain for the memory member.

## Shared records

### Components

#### RT-CMP-memory-store
Label: MemoryStore executor

Source-native identity: `MemoryStore`, instantiated by `create_server` or direct Python callers. Representational form: symbolic Python rules and transient dictionaries, protected selectively by `threading.RLock`. Substrate: process memory for execution, resolved local filesystem root for its effects; implementation source at SRC-1, `src/smriti_mcp/store.py`, with wrappers at `src/smriti_mcp/server.py`. It is not a distributed-parametric component. It performs deterministic string, metadata and graph operations; no model parameters belong to this component.

> self.root = Path(root).expanduser().resolve()
> self.root.mkdir(parents=True, exist_ok=True)
> self._lock = threading.RLock()
> --- `src/smriti_mcp/store.py`

### Operative objects

#### RT-OBJ-server-instructions
Label: Server instructions and tool descriptions

Source-native identity: FastMCP `instructions` plus registered tool descriptions and parameter `Field` descriptions. Representational form: natural-language guidance interpreted by a host/model or human; registration and schemas are symbolic consumption machinery. Substrate: shipped Python string literals and runtime tool metadata, not use-updated retained memory. SRC-1, `src/smriti_mcp/server.py`.

> "Smriti gives agents durable markdown memory. Store facts, decisions, "
> "preferences, project context, and reusable notes that should survive "
> "beyond the current chat."
> --- `src/smriti_mcp/server.py`

The strings request durable storage; they do not schedule calls or prove retention judgments. [RT-BAP-tool-guidance](#rt-bap-tool-guidance) records their force and horizon.

### Routes

#### RT-RTE-memory-write
Label: Caller-supplied memory admission

Endpoints: external MCP caller or direct `MemoryStore` caller → create/append/update/archive/delete/remember/supersede → local files → returned result. Owner: caller chooses semantic content and operation; Python executes validation, matching and I/O. Pydantic governs MCP inputs, whereas store cleaning and path checks govern direct store calls. Human versus model authorship is unresolved for a generic caller; there is no per-content human approval gate in the inspected wrappers. `source_agent` and `author` are self-supplied metadata. Operating mode: open caller requests, with explicit `remember` modes and deterministic automatic successor choice. No answer oracle; matching scores are heuristics, not correctness references. Trigger/proposal: a tool/library request; admission: acceptable shape/path, available target and selected branch; veto: caller can withhold the call, code rejects invalid requests or conflicting creates. Guidance is shipped durable-memory/tool guidance, not a source-truth evaluator. Recovery: caller edits/restores files; no composite rollback. Archive preserves content; delete removes it; supersession preserves two notes but saves them sequentially. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: create returns ID/path; mutations return ID/status; remember returns action, ID, reason, candidate metadata and trace ID; supersession returns both IDs/status.
- Later read-back: saved Markdown/YAML reloads through get, scans, search and recall; remember additionally appends a remembered event for later grouping.
- Delegated visibility: inapplicable — no worker delegation is implemented; callers sharing a root can read its files subject to external filesystem controls.
- Selection predicate: explicit ID for direct edits; default ID from category/title for creation; auto remember appends only when the best candidate score is at least 6 and normalized titles equal, otherwise creates.
- Invalidation or expiry: explicit replacement/deletion/archive/supersession; expiry metadata affects ranking rather than admission or physical removal.
- Activation or effect: local file replacement/deletion is wired; later ranking can use changed metadata. External model behavior from the content is unobserved.
- Evidence limits: source implementation only; raw filesystem editors bypass these API checks and direct store callers bypass MCP input models. Trace creation is not mandatory for lower-level writes.

> if candidate.get("score", 0) < 6:
>     return False
> candidate_title = str(candidate.get("title") or "").strip().lower()
> title = str(meta.get("title") or "").strip().lower()
> if title and title == candidate_title:
>     return True
> return False
> --- `src/smriti_mcp/store.py`

#### RT-RTE-context-recall
Label: Requested recall and browsing

Endpoints: query/filters from caller → scan/reload/index/rank → recall context or search/list/get/index response. Python owns the selector and formatter; the external host owns whether that response enters a model invocation. Context/state: current files, aliases, terms, backlinks, lifecycle, confidence, salience, access counts and timestamps. Code computes lexical weights and affinity; it neither embeds nor asks a model to rank. Query strings and optional filters define requested scope; metadata values are not authenticated access controls. Operating mode: open retrieval request; code selects candidates without an answer oracle or human adjudication. Healthier matching or future usefulness is not established by the selection rule. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: recall returns query/count, selected metadata, formatted context and requested budget; search returns ranked snippets and optional full Markdown; get returns full Markdown; list returns metadata; index load returns generated Markdown.
- Later read-back: recall defaults to access reinforcement, writing last-access time, incremented count and salience (capped at 1); later ranking reads these values. Index load can reuse an existing generated file until refreshed.
- Delegated visibility: inapplicable — this route returns to its caller, with no sub-agent context or delegated execution.
- Selection predicate: exact metadata filters, weighted lexical/phrase score plus affinity, optional one-hop wikilinks/backlinks at 0.35 of seed score, top limit then approximate word budget. Default recall excludes archived/superseded unless overridden; search does not share that exclusion.
- Invalidation or expiry: scans rebuild source-derived ranking data per invocation; expired memories receive a score penalty. Existing markdown index may remain stale without refresh. File mutation/deletion changes later scans.
- Activation or effect: compact text delivery and optional access writes are implemented; actual host injection, compliance and task improvement are unobserved.
- Evidence limits: no supplied retrieval evaluation or host trace; budget is approximate and the first memory is admitted even if oversized. Snippets omit most body content; delivery does not imply complete memory use.

> if used_words + words > budget_words and memories:
>     break
> --- `src/smriti_mcp/store.py`

> expires_at = _parse_datetime(note.get("expires_at"))
> if expires_at and expires_at < datetime.now(timezone.utc):
>     score -= 4.0
> --- `src/smriti_mcp/store.py`

The second passage is the expired-memory affinity penalty, not eviction. This route controls returned working-context material, not the host's accumulated conversation. Metadata-only search and ID reload provide selective omission/re-entry; no frame popping, conversation summarization or context-tail retention is implemented here.

#### RT-RTE-trace-consolidation
Label: Trace review and consolidated admission

Endpoints: record_trace/remember events → dated agent-named NDJSON files → suggest_consolidation groups → caller judgment/content → consolidate_memory → note and consolidation event. Raw observations can originate from a human, model or external application; generic caller identity does not resolve provenance. Python groups by the first three normalized content terms, recommends updates when related memories exist, otherwise creates for repeated or high-salience groups. The caller proposes and decides final prose; software admits it by the selected write operation. No mandatory human veto or source-verification oracle. Operating mode: requested review and requested write, not a scheduler, experiment or internal model synthesis loop. Improvement trigger is caller review; recommendation heuristics do not establish improved capacity. Guidance tells callers to review traces and supply final content. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: recording returns event/ID/relative path; suggestions return grouped raw events, recommendations and related-memory metadata; consolidation returns the selected write result.
- Later read-back: suggestions reload NDJSON by optional scope/since/agent; admitted notes can enter later get/search/recall. Trace retention alone is not a behavior-changing semantic consolidation.
- Delegated visibility: inapplicable — the caller may be an agent but Smriti neither launches nor coordinates one.
- Selection predicate: trace scope/time/filename-agent filters and topic grouping; caller selects trace IDs, content and target; create is also the fallback for modes other than append/update.
- Invalidation or expiry: no automatic trace removal here; caller can edit notes, replace content or supersede. No automatic rollback joins note write with event append.
- Activation or effect: create/update admit supplied prose and source references; append admits body text but does not apply the newly prepared metadata. Later behavioral use remains unobserved.
- Evidence limits: no checked linkage from trace IDs to factual support, no supplied consolidated corpus or later-consumer run, and no automated content-directed criticism established by these grouping/write rules.

> "Suggest groups of raw traces that may deserve consolidation. "
> "Smriti does not summarize them; the agent decides the final memory content."
> --- `src/smriti_mcp/server.py`

> if mode == "append":
>     if not id:
>         raise ValueError("Append consolidation requires an existing memory id.")
>     result = self.append_memory(id, content)
> --- `src/smriti_mcp/store.py`

This route does not require formulated theories; arbitrary supplied prose can contain them, but neither that fact nor the word consolidation establishes theory-builder conditions. Content-specific theory assessments require the actual supplied material and its consumption, neither supplied here.

#### RT-RTE-store-maintenance
Label: Requested health review and rebuild

Endpoints: CLI fix-frontmatter/rebuild, MCP rebuild/index/health, or library calls → filesystem scan → diagnostic response or deterministic rewrites → caller. Code decides defaults, metadata inference, whole-phrase longest-first links and generated indexes. The caller invokes and can choose dry-run/skip options; no per-edit human approval is required after invocation. Operating mode: requested batch maintenance, not an experiment. Health compares duplicate titles, inactivity at least 180 days, bodies above 2500 words and unresolved links against code rules; these thresholds are diagnostic criteria, not an answer oracle for note truth. Trigger/proposal: caller requests inspection or repair; admission: matching file/phrase and repair rules; rejection: skip flags/dry-run or errors. Guidance: title/content/path metadata inference and title/alias matching. It changes retained metadata/text and derived navigation, not executable capabilities. SRC-1, `src/smriti_mcp/cli.py`, `src/smriti_mcp/store.py`, `src/smriti_mcp/fix_frontmatter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: health counts/details, rebuild component reports and index path/count; CLI prints summaries and can exit nonzero for reported frontmatter errors.
- Later read-back: repaired notes and links feed subsequent scans/recall; generated index.md is loadable and index.yaml is written as a derived representation. Search/recall rebuild their in-memory index from files rather than trusting saved YAML.
- Delegated visibility: inapplicable — no delegated process or agent performs review; CLI and MCP enter the same core code where applicable.
- Selection predicate: repair scans non-reserved Markdown and excludes hidden path components; store scan excludes reserved basenames and .smriti paths, skips unparseable or untitled notes. Link insertion excludes self-targets, ambiguous phrases, code spans and existing Markdown links.
- Invalidation or expiry: index refresh overwrites generated files; repairs/link normalization update notes. Recovery requires caller restoration; batch writes have no shared transaction or automatic rollback.
- Activation or effect: source-wired metadata/body/index changes alter later retrieval candidates and graph expansion; health alone reports without applying repairs.
- Evidence limits: dry-run repair checks only title/category rather than simulating all repairs; direct frontmatter/index writes do not inherit ordinary atomic replacement. No supplied maintenance run establishes correctness or retrieval benefit.

> if not dry_run:
>     result["index"] = self.build_memory_index(group_by_category=group_by_category)
> return result
> --- `src/smriti_mcp/store.py`

> md_files = [f for f in md_files if not any(p.startswith(".") for p in f.parts)]
> --- `src/smriti_mcp/fix_frontmatter.py`

### Claims

#### RT-CLM-file-controls
Label: Bounded file write controls

Claimed operation: ordinary memory writes use a checked root-relative ID, an instance lock and temporary-file replacement. Owner: `MemoryStore`; enforcement: `_path_for_id`, selected mutation lock regions and `_atomic_save`. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. These controls cover ordinary note API writes, including direct store invocation, but not arbitrary direct filesystem editing, trace agent-path construction, every maintenance/index write, or composite transactions. Required external contract: filesystem path/replace semantics and permission/isolation policy; no hostile concurrent filesystem mutation and no expectation of cross-process locking. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/fix_frontmatter.py`, `src/smriti_mcp/frontmatter.py`.

> if not self._is_relative_to(path, self.root):
>     raise ValueError(f"Memory id escapes root: {id}")
> --- `src/smriti_mcp/store.py`

> os.replace(tmp_name, doc.path)
> --- `src/smriti_mcp/store.py`

Counterpath:

> path = self.trace_root / now[:10] / f"{event['agent'] or 'shared'}.ndjson"
> --- `src/smriti_mcp/store.py`

Agent strings are stripped but not cleaned as IDs or checked for containment. Thus path separators/absolute strings can change the trace destination; no universal root sandbox is established. Atomic replace prevents an ordinary reader seeing the intermediate temporary note, subject to filesystem semantics; it does not supply crash durability, semantic validation, multi-note atomicity or lost-update prevention across independent instances. This is a bounded implementation assessment, not an exploitation or crash test.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-tool-guidance
Label: Host-facing memory guidance

Consumer: MCP host and its agent/model, when it exposes and interprets tool metadata. Channel: server instructions and tool/parameter descriptions from [RT-OBJ-server-instructions](#rt-obj-server-instructions). Force: natural-language request to preserve appropriate information and use particular APIs; schemas separately constrain accepted shape. Horizon: server session and later invocations reading the same shipped definitions, not adaptation from operation. SRC-1, `src/smriti_mcp/server.py`.

> "Agent-friendly write API that records a trace and deterministically chooses "
> "whether to create a new memory or append to a strongly matching existing memory."
> --- `src/smriti_mcp/server.py`

This channel can influence tool choice, but no supplied host/model trace shows activation. The implementation's narrower exact-title append test controls the actual branch regardless of how the host interprets “strongly matching.” It is distinct from authority of subsequently retrieved user content, which depends on external consumption.

## Annotations

none
