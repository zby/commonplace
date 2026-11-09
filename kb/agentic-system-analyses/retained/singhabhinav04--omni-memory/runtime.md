---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Omni-Memory runtime baseline: CLI, host hooks, extraction, context delivery and alternate admission paths at the frozen revision."
run-id: AAS-2026-11-08-omni-memory-09378abbfe6b-01
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
---

# Omni-Memory runtime report

## Runtime account

### Work and evidence basis

Omni-Memory returns memory context and maintains project knowledge; it is not the coding agent that acts on that context. Its packaged skill claims that it “enforces” use of verified memory. Implementation supports storage, retrieval, instructions to the consuming agent and source-change checks, not compulsory compliance or semantic truth. The ordinary installed loop is host event → CLI → SQLite/Git refresh → rendered context → host model; at compaction or session end a transcript feeds admission back into SQLite. No execution trace or experiment is registered in [the boundary](boundary.md). All operation and benefit conclusions below remain uninspected. SRC-1 supplies implementation and doctrine/design, not observed execution.

> git provenance, and **enforces** that you use verified memory rather than
> hallucinating architecture.
> --- `omni_memory/skills/omni-memory/SKILL.md`

The shipped console entry, module driver, hooks and generated IDE plugin belong to the same system, not excluded callers. This report adds detailed SRC-1 implementation coverage of `omni_memory/llm.py`, `omni_memory/context.py`, `omni_memory/artifacts.py`, `omni_memory/inject.py`, `omni_memory/agentsmd.py`, `omni_memory/branch.py`, `omni_memory/witness.py`, `omni_memory/team.py`, the CLI lifecycle/option paths, dashboard handler and selected store methods. These are files at the boundary revision, not additional sources. Graph extraction, ranking mathematics, eviction thresholds, static browser internals and full staleness logic are not exhaustively audited here. Their existence and driver connections are not claims of correctness.

### Ordinary invocation end to end

1. A host delivers SessionStart to `hook start`. The event payload is JSON; malformed input becomes an empty object. `_store` resolves the project store. The enabled flag gates the hook. Start clears read-observation and use-witness state, imports eligible shared state, refreshes against repository changes and rewrites the managed AGENTS.md block. Default `session` mode prints recent events and one ranked seed; `manual` suppresses that seed but still updates AGENTS.md. These symbolic decisions belong to Python, not a model. See [RT-RTE-context-delivery](#rt-rte-context-delivery).
2. The foreground coding agent receives host-delivered text and decides its own next actions. The skill asks it to run `inject "<what you need>"` before architectural assumptions. That CLI path checks enabled state, refreshes if needed, ranks branch/base memory with query/files/graph context, optionally appends global and linked memories, clips text, marks provenance/staleness/conflicts and prints a block. Selection is code; interpretation and use are the host agent's. SQLite rows retain full text, while the emitted projection is narrower. There is no tool-call authorization gate between that text and the external host's actions. [RT-BAP-agent-context](#rt-bap-agent-context)
3. Host PostToolUse events for Read/Edit/Write/MultiEdit can record current in-repository file digests, bounded to files at most 2 MB. Capture later prefers those observations over capture-time hashes. This depends on the host delivering the relevant event; the CLI hashes files, not the exact bytes of a supplied tool-result body. Injection also pins emitted memories' current file digests. `used <id>` compares pins to current sources and prints warnings; later citation scanning provides retrospective checks. Neither check blocks a coding action. [RT-RTE-use-check](#rt-rte-use-check)
4. PreCompact or SessionEnd sends a transcript path. `_read_transcript` streams JSONL forward from a persisted per-path cursor, keeps text blocks rather than arbitrary tool payloads, and hands flattened role/text to extraction. Valid structured JSON bypasses model extraction; otherwise allowed unattended model extraction or a heuristic proposes candidates. Cleanup and source-sensitive trust handling precede storage. Capture writes digest/context projections, citation feedback and, when sharing is enabled, the author's shard. Cursor state survives into another hook invocation. [RT-RTE-capture-admission](#rt-rte-capture-admission)
5. Terminal products are stdout context or status, SQLite records, managed AGENTS.md, MEMORY.md and optional shared/generated artifacts. The external coding agent's final answer is not Omni-Memory's terminal result. Hooks catch exceptions and return zero: continuation of the host session is favored over proof that memory maintenance succeeded. Explicit capture reports malformed JSON as failure instead. SRC-1: `omni_memory/cli.py`, `omni_memory/session_memory.py`, `omni_memory/inject.py`.

### Alternate routes and forcing cases

Three forcing cases bound consequential controls; these are source traces, not executed tests.

**Unattended versus direct extraction.** Valid JSON arrays or supported object envelopes go straight to `remember_many`; there is no model call in that branch. Raw prose consults `autocapture_ok`: provider `agent` is excluded unless the environment opt-in is nonempty, while API providers are permitted. Despite the name/documentation `OMNI_HEADLESS_LLM=1`, the implementation tests truthiness, so any nonempty value permits the provider. A configured API plus a discoverable agent CLI still selects `agent` first unless explicitly overridden. Direct `build` and generated artifacts use `available`/`complete`, not the unattended predicate. Thus “never spawn a headless agent” covers only the default raw-transcript extraction branch, not all shipped model callers. [RT-RTE-build-artifacts](#rt-rte-build-artifacts), [RT-CMP-agent-cli](#rt-cmp-agent-cli), [RT-RTE-capture-admission](#rt-rte-capture-admission).

**`build --no-ai` does not prohibit all model calls.** Argparse accepts `--no-ai` independently of `--no-docs-gen`. The former disables the facts pass; with a provider available, document generation still runs unless the latter is set. Generated documents call `llm.complete` and can spawn the agent CLI. `--no-docs` independently controls the Markdown scan. This is a reachable supported CLI shape, not a type-only hypothetical. Failure of the facts pass does not prevent a later artifact attempt. [RT-RTE-build-artifacts](#rt-rte-build-artifacts)

**Trust enforcement is path-specific.** Autonomous capture clamps evidence upstream; the low-level store accepts trusted callers. The supported CLI `remember --verified` labels its caller `manual` even when a coding agent invokes it; the skill expressly asks agents to use `remember`. Dashboard writes also accept an evidence field. Explicit `snapshot --in --trust` preserves recognized incoming tiers while automatic shared import clamps them. This is source-label authority, not authenticated human per-item approval. Moreover, ranked injection emits warnings, but AGENTS.md uses a different rendering path: it selects active rows without branch arguments and does not reproduce per-row external/stale/evidence markers. Neither the “verified” heading nor the inline snapshot is a universal evidence filter. [RT-RTE-local-edits](#rt-rte-local-edits), [RT-RTE-shared-import](#rt-rte-shared-import), [RT-RTE-context-delivery](#rt-rte-context-delivery)

Other material routes are the dashboard's background refresh and editing, global-store reads, on-demand recall, team synchronization, and OpenCode compaction injection. OpenCode runs `hook start` at both session creation and idle, discards its quiet command output, and explicitly pushes `inject` output into compaction context. It therefore shares the CLI state transitions but not all Claude hook delivery semantics. Other named IDE bindings supply AGENTS.md. None establishes actual host loading or compliance. SRC-1: `omni_memory/install.py`, `omni_memory/cli.py`.

### Enforcement, effects and coordination

| Load-bearing control | Owner, point and strength | Covered paths, alternates and external contract | Conclusions |
|---|---|---|---|
| Ask agent to trust/cite/reverify | Injector/AGENTS writer; natural-language instructions; policy | Ranked block and managed file. Host must load and interpret text; neither controls shell/tool execution. Recall and external host behavior are alternatives. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Avoid default unattended agent invocation | Model adapter predicate at raw capture; policy | JSON bypasses extraction; prose checks provider/opt-in. Build/artifacts do not use this predicate. Environment and subprocess behavior are external. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Evidence ceiling for machine capture/import | `remember`/import; invariant within guarded branches | Source labels determine ceiling; manual/dashboard and explicit trusted import differ. Caller identity is not authenticated as human. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Keep hooks from propagating ordinary exceptions | `cmd_hook` blanket exception handler; best effort | Hook dispatcher only, not every CLI command; errors can silently lose maintenance. Process termination and host deadlines are outside the catch. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Dashboard write origin checks | HTTP handler, Host/Origin/Referer plus JSON content type; policy | Default nonzero launch (port 7777) enables these checks and binds loopback. The shipped CLI also accepts `ui --port 0` and forwards zero unchanged to `run_ui` and `_handler`, disabling both origin/host checks and the JSON content-type requirement. CLI memory writes bypass HTTP entirely. Browser/header semantics and same-user process trust remain external; exploitation is unobserved. | implementation conclusion status: wired; operation conclusion status: uninspected |

Guarantee strength describes scope, not an end-to-end security certification. Minimum supporting passages appear in the route records below. SQLite WAL, busy timeout and one request connection per dashboard request coordinate concurrent readers/writers. Atomic file replacement protects individual generated context files from partial contents; it does not serialize a multi-file snapshot or guarantee latest-writer semantic freshness. Refresh catches graph failures to permit file-level fallback. Reconciliation failure rolls back pending updates and avoids recording a successful refresh signature; AGENTS writing failure also withholds that signature. The outer hook catch can still hide the failure. SRC-1: `omni_memory/store.py`, `omni_memory/branch.py`, `omni_memory/serve.py`, `omni_memory/cli.py`.

The capability surface includes local file reads/writes, Git subprocesses, optional network completion and an optional agent subprocess. Current grants are whatever credentials, environment, host hooks and OS permissions the installation supplies; this source does not reveal a deployed grant set. No isolation envelope for the invoked agent CLI is established by the bare subprocess call. Provider-native tools, remote workers and downstream shell actions are not controlled by the completion adapter inspected here. There is no basis to attribute the enclosing agent's sandbox or approvals to Omni-Memory.

Changes to retained knowledge and generated documents are admitted through the records below, not necessarily human approval. Product-source and packaging changes remain ordinary developer/release changes; this report establishes no runtime route that patches the package or retrains a model. Memory revisions themselves, graduation/eviction semantics and epistemic warrant are left to the specialist members rather than inferred from the context heading.

## Shared records

### Components

#### RT-CMP-agent-cli
Label: Agent CLI completion backend

SRC-1: `omni_memory/llm.py`. External distributed-parametric model reached through a subprocess; command tokens are symbolic configuration, prompts/answers are natural language, parameter storage is external and uninspected. `OMNI_AGENT_CMD` is split into tokens, otherwise discoverable Claude uses `claude -p`. Completion concatenates system and user content, captures stdout, checks process status and has a 300-second timeout. No model version is pinned here. The selected command or its mutable service endpoint can resolve to another model. Parameter change during operation is uninspected; no parameter-update call is wired in this adapter. Subprocess permissions and agent-internal tools remain external.

> r = subprocess.run(cmd, input=system + "\n\n" + user,
>                            capture_output=True, text=True, timeout=300,
>                            encoding="utf-8", errors="replace")
> --- `omni_memory/llm.py`

#### RT-CMP-gemini
Label: Gemini completion backend

SRC-1: `omni_memory/llm.py`. External distributed-parametric model; weights/storage and changes during operation are uninspected. The adapter requests text over HTTPS with temperature 0.2. Default model name `gemini-2.5-flash-lite` is an environment-overridable selector, not an immutable parameter/version pin. Remote resolution can change. No training operation is wired here.

> model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-lite")
> --- `omni_memory/llm.py`

#### RT-CMP-openai
Label: OpenAI-compatible completion backend

SRC-1: `omni_memory/llm.py`. External distributed-parametric model; remote parameter substrate/change during operation uninspected. Base URL and model are mutable configuration, exact version unpinned; another endpoint/model can resolve. Symbolic JSON messages separate system and user roles; the first returned message content supplies extraction/document text. No training call is wired.

> base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
>         model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
> --- `omni_memory/llm.py`

#### RT-CMP-anthropic
Label: Anthropic completion backend

SRC-1: `omni_memory/llm.py`. External distributed-parametric model. The dated default is still environment-overridable, not a frozen weights identity; remote endpoint resolution is mutable. Parameter storage and change during operation remain uninspected. Adapter sends system/user text and takes the first content block's text; no parameter update is wired.

> model = os.environ.get("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")
> --- `omni_memory/llm.py`

### Operative objects

#### RT-OBJ-inject-cache
Label: Injection de-duplication state

SRC-1: `omni_memory/cli.py`. Symbolic SHA-1 block digest and prompt counter stored in `.omni-memory/.inject_cache`. Auto mode compares block identity and increments a counter; changed blocks or the twentieth prompt re-emit. This persistent state controls delivery, not memory truth. Session seeds mark the cache too; write failures are swallowed. It is project-file state, not demonstrated per-conversation isolation.

> if h != last_h or count + 1 >= _INJECT_REFRESH_EVERY:
>         _write_inject_state(p, h, 0)
>         return True
> --- `omni_memory/cli.py`

### Routes

#### RT-RTE-context-delivery
Label: Host and pull context delivery

Owner: host triggers events, CLI/code selects content, foreground agent owns subsequent action. Endpoints: SQLite/project state → `hook start`, auto prompt hook or explicit `inject` → stdout; managed-file writer → AGENTS.md → host loading. Symbolic scope/ranking/budget rules select natural-language memory; prompt is the consumption path, not a fourth representational form. SRC-1: `omni_memory/cli.py`, `omni_memory/inject.py`, `omni_memory/agentsmd.py`, `omni_memory/store.py`, `omni_memory/install.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked block or empty output; session start can also print recent activity. OpenCode's refresh discards stdout and its compaction hook pushes explicit injection output instead.
- Later read-back: Durable rows and managed AGENTS.md reach later calls/sessions; injection-cache state regulates repeated auto delivery.
- Delegated visibility: External host receives selected text, not the full database. Optional extraction subprocess is a different route; ordinary injection performs no model call itself.
- Selection predicate: Current/base scope unless branch awareness is off; query/files/graph context; fallback top memories; optional existing global store and co-anchored siblings; near-duplicate suppression and clipping. AGENTS.md instead reads up to 2000 active rows without branch filtering and inlines configured kinds/counts.
- Invalidation or expiry: Explicit pull/session start refresh state; auto prompt injection does not itself refresh. Identical blocks are suppressed until the refresh counter permits re-emission. Host window eviction/compaction is external.
- Activation or effect: Output includes rules to cite and trust, not an execution gate. Host compliance is unobserved. At least the first rendered memory is retained even if its line exceeds the remaining budget; headers/legends are outside that accounting.
- Evidence limits: Marker rendering and source pinning establish delivery/check wiring, not semantic correctness, complete causal chains or downstream action. Global text is delivered through a separate store; no deployed content supplied.

> if used and budget - len(line) < 0:   # keep at least one; then honor budget
>             break
> --- `omni_memory/inject.py`

> mems = store.memories(status="active", limit=2000)
> --- `omni_memory/agentsmd.py`

> "Rules: trust these; cite [id]s used; not here or in the code → say "
>     "\"not in memory\"; re-verify ⚠STALE."
> --- `omni_memory/inject.py`

Working-context control is code-controlled selection, truncation and duplicate suppression before delivery. Full retained rows remain reachable through later retrieval; omitted text is not necessarily lost. PreCompact captures material before the host summarizes; Omni-Memory does not decide the host's summary contents or retain a verbatim tail in its window. OpenCode adds memory back to compaction context. This resembles bringing external state back on demand, not an addressable heap inside the model window. No isolated subagent task frame is implemented by ordinary retrieval; the optional model subprocess receives selected input and returns text, but its internal context lifecycle is opaque.

#### RT-RTE-capture-admission
Label: Transcript and JSON admission

Owner: CLI/hook accepts host/agent input; code selects extraction branch; optional model proposes JSON; cleanup/store admit. Endpoints: stdin JSON or flattened transcript → candidates → `remember_many`/`remember` → SQLite, digest and hook-side managed context. SRC-1: `omni_memory/session_memory.py`, `omni_memory/cli.py`, `omni_memory/llm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Explicit capture prints accepted/dropped counts or malformed-JSON failure; hooks report counts to stderr or silently return zero on exception.
- Later read-back: Stored candidates feed later retrieval; per-transcript offsets in metadata resume extraction; hook citation feedback changes retained use counts and can add events.
- Delegated visibility: Optional backend sees extraction instructions plus at most the first 30000 transcript characters passed to extraction; JSON ingestion does not invoke it. Heuristic fallback stays local.
- Selection predicate: JSON parses as list or supported object envelope; JSON-looking malformed text rejects. Raw prose consults unattended provider policy, then model extraction or heuristic fallback; cleanup filters candidates before writing.
- Invalidation or expiry: Transcript cursor advances after hook processing; later maintenance can archive/quarantine memories. No guaranteed retry-to-completion after the last hook is established.
- Activation or effect: New rows are eligible for future context. Returned candidates are not proof of changed foreground behavior.
- Evidence limits: Host must provide transcript and read events; only text content blocks are flattened. Direct raw capture may exceed the model window; no automatic drain loop is established. Provider failure falls back, while empty parsed model output can admit nothing without retry.

Admission: open-ended session capture, not a bounded experiment or curriculum. Proposals come from the foreground agent, heuristic scanner or selected model. Software cleanup, evidence ceilings and store rules decide admission without per-content human approval. Human veto is operationally available through editing/forgetting/turning off hooks, not a required approval stage. Guidance is EXTRACTION_PROMPT (durable concise claims, files/symbols, evidence labels); it stays static while accepted memories persist. Retained objects are claims and anchors, not the model's hidden reasoning. There is no answer oracle: file-digest checks concern provenance/change, not a reference answer for the memory's meaning. Recovery includes fallback extraction and reversible memory maintenance; blanket hook catches can also hide incomplete work.

> if os.environ.get("OMNI_HEADLESS_LLM"):
>         return p is not None
>     return p is not None and p != "agent"
> --- `omni_memory/llm.py`

> if raw.lstrip()[:1] in "[{":
>             raise ValueError(
>                 f"input starts like JSON but failed to parse: {parse_err}") from parse_err
> --- `omni_memory/session_memory.py`

> evidence = clamp_evidence(evidence, source)
> --- `omni_memory/session_memory.py`

#### RT-RTE-build-artifacts
Label: Bootstrap facts and documents

Owner: CLI orchestrates local graph/context gathering and optional completion backends. Endpoints: repository files → context snapshot → model facts/documents → SQLite and `.omni-memory/api-map.md`/`linkup.md`; Markdown ingestion and digest generation are additional branches. SRC-1: `omni_memory/cli.py`, `omni_memory/context.py`, `omni_memory/artifacts.py`, `omni_memory/llm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Progress/errors and output locations; generated files or partial successful products can remain when later work fails.
- Later read-back: Facts enter retrieval and MEMORY.md; artifact files are exposed by the dashboard. The Markdown ingestion path excludes `.omni-memory`, so these generated files do not automatically feed that scan. Exact later activation is unobserved.
- Delegated visibility: Model receives ranked repository text, not necessarily the whole codebase: gather defaults to 140000 characters, 6000 per file, and a first-1000-file tree. Agent CLI may have capabilities beyond this supplied input; its internals are outside the boundary.
- Selection predicate: Facts require available provider and not `--no-ai`; documents require available provider and not `--no-docs-gen`; document scan requires not `--no-docs`. Context favors manifests/docs/architectural path hints.
- Invalidation or expiry: Re-running replaces generated artifact files after a minimum-length check; facts undergo normal admission. No artifact version rollback is implemented by the inspected writer.
- Activation or effect: Emits model-derived memory and documentation. Text-length rejection protects against very short responses, not hallucinated content.
- Evidence limits: Requests for code-grounded facts do not establish compliance; source context is truncated and provider behavior opaque. No run or quality comparison supplied.

Admission: operator/agent launches an open bootstrap; model proposes content under BUILD/APIMAP/LINKUP prompts. Code parses facts and uses memory admission; artifact admission rejects text under 40 characters then writes atomically. There is no semantic answer oracle or mandatory human review. Independent file generation means no all-or-nothing two-document transaction. Failed facts completion falls back toward docs; a failed artifact keeps its previous file when rejection occurs before writing. These are knowledge/document changes, not package-code changes.

> use_ai = llm.available() and not args.no_ai
> --- `omni_memory/cli.py`

> if not args.no_docs_gen and llm.available():
> --- `omni_memory/cli.py`

> if len(text) < _MIN_ARTIFACT_CHARS:
> --- `omni_memory/artifacts.py`

#### RT-RTE-local-edits
Label: Explicit CLI and dashboard changes

Owner: local caller invokes commands or HTTP endpoints; store admits fields. Endpoints: `remember`, editing/delete/reanchor/resolve dashboard requests, or maintenance CLI → SQLite → regenerated projections. Dashboard has no per-user authentication; loopback binding applies to its server, while origin and JSON content-type checks protect its browser-facing write channel only when the supplied port is nonzero. The default is 7777, but the shipped CLI accepts `ui --port 0`, reaching the disabled-control branch. SRC-1: `omni_memory/cli.py`, `omni_memory/serve.py`, `omni_memory/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Memory ID/count/status or HTTP response; doc synchronization errors may be swallowed.
- Later read-back: Updated rows and managed context influence subsequent retrieval; global remember writes a separate user-level store for cross-project delivery.
- Delegated visibility: Local caller sees CLI/HTTP output; dashboard requests use fresh SQLite connections. No model delegation occurs in these editing handlers.
- Selection predicate: Caller supplies content, ID or scope. `remember --global` rejects repository file/symbol anchors. HTTP mutations must pass configured Host/Origin/Referer and JSON checks when launched with a nonzero port; `ui --port 0` disables both checks.
- Invalidation or expiry: Forget archives; gc exposes reversible quarantine/restore and optional permanent purge; flush deletes selected store categories. CLI flush requests confirmation unless `--yes`, whereas the dashboard flush endpoint directly invokes store flush after HTTP checks.
- Activation or effect: Writes affect future reads; same-user or agent CLI callers can assert `verified` through manual-source paths. These are not authenticated human-only grants.
- Evidence limits: No deployed permissions or genuine HTTP requests supplied. Argparse accepts any integer for `--port`; `cmd_ui` forwards it unchanged, and `run_ui` passes it to both server binding and `_handler`. Thus the CLI-supported `ui --port 0` reaches the branch disabling origin/host and JSON content-type checks; the default nonzero launch does not. This is source-established reachability, not observed exploitation.

Admission: caller proposes and decides explicit edits; software validates the selected path, not the truth of each claim. No answer oracle or experiment mode. Caller can reject by not submitting, archive/delete later, or restore quarantined state; flush is documented irreversible. Dashboard document save rejects generated MEMORY.md and only allows api-map/linkup names. Regenerated digest/AGENTS.md reflect accepted row changes; there is no required human veto between an agent's CLI action and storage.

> m = sm.remember(s, root, " ".join(args.text), kind=args.kind, source="manual",
>                     evidence=evidence, files=files or None, symbols=symbols or None)
> --- `omni_memory/cli.py`

> if not _ALLOWED_HOSTS:        # port unknown (embedded/test use) → skip
>                 return True
> --- `omni_memory/serve.py`

> srv = ThreadingHTTPServer(("127.0.0.1", port), _handler(root, port))
> --- `omni_memory/serve.py`

> def cmd_ui(args):
>     from . import serve
>     return serve.run_ui(port=args.port)
> --- `omni_memory/cli.py`

> ui = sub.add_parser("ui", help="local dashboard")
>     ui.add_argument("--port", type=int, default=7777)
> --- `omni_memory/cli.py`

> if _ALLOWED_HOSTS and ctype.lower() != "application/json":
> --- `omni_memory/serve.py`

#### RT-RTE-shared-import
Label: Team and snapshot admission

Owner: sharing CLI or capture writes an author's shard; start hook/team sync/import code admits external rows. Endpoints: SQLite → JSON shard/snapshot → Git/file transport → local SQLite → later context. Source identity and branch are retained fields, not authenticated authorship. SRC-1: `omni_memory/team.py`, `omni_memory/cli.py`, `omni_memory/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/status; malformed individual team shards are skipped so other shards can continue.
- Later read-back: Imported active rows reach retrieval and managed context; shared/imported provenance is marked by ranked injection, but not by every projection.
- Delegated visibility: Teammates receive the exported text/fields once files are committed and transferred externally; no model delegation in import itself.
- Selection predicate: Shard writer exports current Git author's active default-branch rows. Sync scans other slug-named JSON shards. Fresh empty store may bootstrap root snapshot under auto-import flag and 2 MB cap; explicit snapshot import is separate.
- Invalidation or expiry: Existing IDs skip reimport, so editing content in a shard under an already-imported ID does not replace it through this path. Local maintenance can later change/archive rows.
- Activation or effect: Outside content becomes eligible local memory. Automatic import clamps evidence; explicit `snapshot --in --trust` preserves recognized tiers.
- Evidence limits: Git identity/author slug is routing, not cryptographic attribution. No actual cross-clone run is supplied. Fresh-snapshot size cap does not establish an identical cap on all imports.

Admission: contributors propose shared content; code performs shape/ID/noise checks and skips existing IDs. No per-item human approval is required for session-start synchronization. Explicit trust is a caller choice, not proof of human authorship or earned warrant. No answer oracle. Rejection ability comes from input checks, auto-import configuration and later local maintenance; imported rows persist, while external Git transport/rollback is outside the importer. The retained result is content plus provenance fields, not verified truth.

> if not trust_evidence:
>                 evidence = clamp_evidence(evidence, source)
> --- `omni_memory/store.py`

#### RT-RTE-use-check
Label: Retrieval pins and citation checks

Owner: injector pins emitted memory sources; caller `used` or capture citation scan requests verification; code compares digests. Endpoints: emitted memory/file list → witness rows → current file hashes → diagnostic text/event. SRC-1: `omni_memory/inject.py`, `omni_memory/witness.py`, `omni_memory/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Coverage and changed/missing-source warnings; zero bound sources is explicitly not a clean verification.
- Later read-back: Moved/vanished-source findings can become cross-session events; witness rows survive calls until start clears them, and citations increment uses.
- Delegated visibility: Caller sees diagnostic output; retrospective hook warnings go to stderr and events. External agent behavior after warnings is unobserved.
- Selection predicate: Only requested/cited valid IDs, their declared files and available pins. Binding kind distinguishes a matching read ledger from hashing at pin time.
- Invalidation or expiry: Session start clears witnesses/read ledger; changed or missing current digests produce findings. Pin failure does not prevent injection.
- Activation or effect: Diagnoses source movement and feeds use counts/events, not a mandatory before-action lock or a semantic truth check.
- Evidence limits: Observation-bound means recorded file digest matched, not that claim content follows from those bytes. Pin-time binding explicitly makes the weaker source-movement claim. No observed use/change trace supplied.

Decision roles: caller selects IDs; code decides hash comparison; foreground agent must decide revalidation or re-sourcing. No answer oracle for memory content and no bounded improvement experiment. This diagnostic is not itself an admission of a revised theory or a successful correction.

> valid = bound > 0
> --- `omni_memory/witness.py`

> if not r["valid"] or not (r["stale_at_use"] or r["orphaned_at_use"]):
>         return None
> --- `omni_memory/witness.py`

### Claims

#### RT-CLM-verified-context
Label: Verified-memory usage claim

The packaged skill claims enforcement of verified-memory use; implementation supplies natural-language rules, source checks and retained feedback rather than compulsory host behavior. The claim's scope is coding-agent context and architectural assertions. SRC-1: `omni_memory/skills/omni-memory/SKILL.md`, `omni_memory/inject.py`, `omni_memory/agentsmd.py`. The minimum claim passage is retained in Runtime account; supporting routes are [RT-RTE-context-delivery](#rt-rte-context-delivery) and [RT-RTE-use-check](#rt-rte-use-check). Truth of emitted content, actual compliance and effectiveness are not established by the word “verified.”

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-context
Label: Context text to foreground behavior

Consumer: external coding agent/model. Channel: hook stdout, explicit injection tool output, managed root AGENTS.md and OpenCode compaction context. Force: natural-language instructions and factual context, not a software denial of prohibited actions. Horizon: current invocation and later sessions that reload retained rows/files. SRC-1: `omni_memory/inject.py`, `omni_memory/agentsmd.py`, `omni_memory/install.py`, `omni_memory/skills/omni-memory/SKILL.md`. The instructions retained in [RT-RTE-context-delivery](#rt-rte-context-delivery) ask the agent to trust/cite memory. Delivery is wired; actual behavior changes and benefit remain unobserved. Updating these rows can change later model-visible content, but storage/loading alone does not establish exercised self-improvement.

## Annotations

none
