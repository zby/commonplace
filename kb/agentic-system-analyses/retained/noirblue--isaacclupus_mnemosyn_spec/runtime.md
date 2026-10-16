---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of IsaacCLupus_mnemosyn_spec: proposed unified lifecycle and statically inspected legacy bridge at 0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92."
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
reviewed-boundary: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
---

# IsaacCLupus_mnemosyn_spec runtime report

## Runtime account

### Evidence and consequential work

Mnemosyne proposes a shared memory substrate, not an enclosing agent controller. Its claimed work is to turn sources and memory proposals into audited, approved, searchable knowledge, then answer client questions with bounded context. The canonical design, legacy implementation and implementation-study sketches are different evidence layers. No target code was executed and no execution traces or experimental comparisons were supplied. Operation, activation and benefit remain unobserved. SRC-1, `README.md`, `ARCHITECTURE.md`, `AGENTS.md`, `SPECIFICATION.md`.

> **Concept / Architecture Proposal.**
> This repository contains the specification, data models, and roadmap.
> We are seeking core contributors to begin implementation.
> --- `README.md`

The design's ordinary lifecycle is source ingestion → fast extraction → heavy compilation → structural/contradiction/adversarial audit → publication or rejection → later query. A human approval gate is configurable in the compilation study; agent-memory guidance also allows configurable auto-approval. These are declared policies, not verified enforcement in the bridge. [RT-RTE-design-lifecycle](#rt-rte-design-lifecycle) records the design loop and decision roles. SRC-1, `ARCHITECTURE.md`, `AGENTS.md`, `python_thoughts/05-heavy-llm-compilation.md`.

### Shipped invocation and effect boundaries

The installable legacy package exposes `jarvis-kb = jarvis_kb.cli:main`. The driver loads YAML selected by `--config` or `JARVIS_KB_CONFIG`, expands home-relative strings, and dispatches `init`, `publish`, `serve-proxy`, `serve-mcp` or `status`. It does not implement the proposed unified REST/CLI lifecycle. `init` creates backend directories and optionally initializes Git; it explicitly requires backend initialization by hand. The service units launch the same proxy and MCP commands and request process restart on failure. They are launch recipes, not observed deployments; the gateway unit's socket input and journal output do not establish a working bidirectional client transport. SRC-1, `prior-art/v0-glue/pyproject.toml`, `prior-art/v0-glue/jarvis_kb/cli.py`, `prior-art/v0-glue/jarvis_kb/config.py`, `prior-art/v0-glue/systemd/jarvis-kb-mcp.service`, `prior-art/v0-glue/systemd/jarvis-kb-proxy.service`.

An ordinary inspectable invocation is `serve-mcp` followed by a client's `tools/call` for `kb_ask`. The initiating principal is an external client; no authenticated per-agent identity enters the inspected dispatcher. The gateway reads one JSON line, dispatches a fixed Python handler, invokes `llm-wiki --vault <configured vault> ask <question>` as an argument-vector subprocess, waits up to 120 seconds, and returns stdout, stderr and a reported context budget inside JSON serialized as MCP text. The backend owns retrieval, synthesis, model context and any conversation persistence. The gateway then resumes reading stdin; it owns neither the client's next action nor an autonomous task loop. Exceptions inside tool dispatch become `isError` text; backend nonzero return codes alone do not become gateway errors. See [RT-RTE-client-query](#rt-rte-client-query). SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

>         # Set context budgets via CLI if supported, otherwise rely on defaults
>         r = subprocess.run(
>             ["llm-wiki", "--vault", vault, "ask", args["question"]],
>             capture_output=True, text=True, timeout=120
>         )
> --- `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`

This is not gateway budget enforcement: `context_budget` is echoed, `history_budget` is not forwarded, and no trimming, session reload or summarization occurs in this handler. Search similarly assigns `source` but does not use it to restrict either backend request. `top_k` reaches Link as `limit`, not the LLM-WIKI command. These counterexamples prevent attributing the proposed context and source controls to the shipped bridge. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `SPECIFICATION.md`.

### Material mutation and alternate routes

The gateway delegates ingestion by file extension or explicit document type, compilation to Synto, memory writes to Link HTTP with a CLI fallback, and audit to Synto evaluation, Synthadoc lint and Link validation. These are separate action paths, not stages automatically chained by gateway code. In particular, compile does not call `VaultSync`; `publish` is a separate CLI command. [RT-RTE-foundry-tools](#rt-rte-foundry-tools), [RT-RTE-link-remember](#rt-rte-link-remember) and [RT-RTE-vault-publish](#rt-rte-vault-publish) retain their admission and recovery limits. External backend callers can also act directly; their implementations, access controls and grants are outside this evidence set. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/cli.py`.

Publication is consequential because it supplies later retrieval. `publish` sequentially copies and normalizes Synto wiki files to `self/` and Synthadoc wiki files to `world/`, renames colliding world paths, calls LLM-WIKI ingestion and reindexing, requests Link snapshot/load, and optionally commits the unified vault. It is not a single transaction. Metadata normalization replaces the metadata dictionary with a small selected set, drops approval/hash/internal audit fields, and preserves the article body. Thus later consumers receive normalized pages, not a complete preservation of producer-side governance metadata. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

Four forcing cases bound the guarantees:

1. **Approval path asymmetry.** Synto `.drafts` paths are skipped; Synthadoc's recursive wiki traversal has no corresponding exclusion. Neither path checks an approval field before writing the destination. A source folder convention is not a universal approval gate.
2. **Partial publish failure.** Files are written before index/snapshot/commit calls. Those calls use `check=False`; nonzero exits can coexist with printed completion. No rollback coordinates file writes, indexes, Link and Git.
3. **Queue versus router.** Queue mode selects chat before compile before lint between jobs, but cannot preempt a running generation. Router mode sends chat to Frontline and everything else to Foundry without that queue. Direct backend calls need not traverse either proxy.
4. **Memory fallback.** Link HTTP exceptions trigger CLI `remember`; that command drops `project`, unlike the HTTP payload. An HTTP failure after an actual write can leave an ambiguous outcome before fallback; no gateway deduplication or compensating transaction is shown.

These are static path analyses, not executed fault tests. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

### Guarantees, ownership and coverage

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths / required external contract | Separate conclusions |
|---|---|---|---|---|
| Audited approval before publication | Proposed audit/publish engines; bridge has only a Synto path filter | policy; design lifecycle, narrower Synto draft exclusion | Synthadoc copy, direct backend memory writes and `--auto-approve` require backend-specific admission behavior | design conclusion status: claimed; implementation conclusion status: wired for path filter only; operation conclusion status: uninspected |
| Atomic publication and index rebuild | Proposed publish engine, not the legacy sequential copier | invariant as design claim; not established for legacy publish | All external index/load commands would require a shared transaction or coordinated recovery contract, not supplied | design conclusion status: claimed; operation conclusion status: uninspected |
| Human-edit protection | Proposed hash/write-guard policy at page writes | policy; canonical Phase 2 guards and study helper | Bridge overwrites destinations without checking guards; DDL metadata alone does not enforce identity or approval | design conclusion status: claimed; operation conclusion status: uninspected |
| Context budgets | Proposed query engine; legacy handler only reports a value | policy; proposed ask path | External LLM-WIKI must enforce its own defaults; returned budget is not proof | design conclusion status: claimed; operation conclusion status: uninspected |
| Serialized local Ollama calls | Legacy queue worker and semaphore | invariant within one queue instance's forwarding loop | Router mode, direct model clients, other processes bypass it; requires callers to use this instance | implementation conclusion status: wired; operation conclusion status: uninspected |

SRC-1, `ARCHITECTURE.md`, `SPECIFICATION.md`, `schema/001-init.sql`, `python_thoughts/05-heavy-llm-compilation.md`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`. The quotations in the linked route and claim records preserve the load-bearing contrasts.

Capability, grants and isolation must remain separate. The bridge's capability surface includes fixed tool handlers, arbitrary caller-supplied ingest paths, subprocess execution under the launch user's filesystem permissions, and HTTP calls to configured or hard-coded endpoints. Subprocesses use argument lists rather than shell interpretation; that does not sandbox the called programs or validate their options. The MCP dispatcher does not perform tool-level caller authorization. Current per-client grants and deployed OS/network isolation are uninspected. Loopback defaults reduce ordinary exposure but do not prove isolation; the proxy CLI accepts an alternate bind host. MCPX governance in `AGENTS.md` is a recommended external integration, not installed gateway enforcement. SRC-1, `AGENTS.md`, `prior-art/v0-glue/jarvis_kb/cli.py`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`.

### Model and machinery change

[RT-CMP-fast-model](#rt-cmp-fast-model), [RT-CMP-heavy-model](#rt-cmp-heavy-model) and [RT-CMP-chat-model](#rt-cmp-chat-model) distinguish configured roles from executable selection. The bridge proxy forwards caller payloads rather than forcing those model aliases. Model numerical internals, training and exact resolved versions are unavailable. Template registries, structured generation, retries, prompt experiments and later DSPy optimization are study proposals, not live production machinery. The study names labeled contradiction data as a possible oracle for later prompt optimization; no such dataset or experiment was supplied or inspected. Editing YAML or package code changes later startup behavior, but this package supplies no inspected automatic mechanism admitting product, capability or production-code revisions. This is a bounded statement about the inspected bridge, not an absence claim over every study. SRC-1, `prior-art/v0-glue/config.yaml`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`, `python_thoughts/05-heavy-llm-compilation.md`.

Additional coverage beyond the boundary's initial scope: the heavy-compilation study was read completely as doctrine/design, including its template registry, structured-output examples, staged compilation, hash helper and optimization proposals. The package metadata and both service units were reread as implementation/configuration evidence. Other Rust/Python study details, draft v0.2 integrations and external backends remain uninspected here; no exhaustive statement about their proposed routing or guarantees is made.

## Shared records

### Components

#### RT-CMP-fast-model
Label: Fast model

Configured source-native role `foundry.models.fast` is `gemma4:e4b`. Representational form: distributed-parametric model; numerical substrate is external Ollama model storage, not included weights. It is intended to extract concepts before compilation, but legacy ingestion delegates to external programs and does not itself select this role. Parameters changing during operation: uninspected — no training/model internals supplied. Exact version pinned: no digest in the inspected config. Mutable endpoint can resolve another model: yes, URL and tag configuration can change; actual resolution uninspected. The architecture mentions 4B–8B while agent guidance mentions 30B; these are not evidence of one deployed size. SRC-1, `ARCHITECTURE.md`, `AGENTS.md`, `prior-art/v0-glue/config.yaml`.

>       fast: gemma4:e4b
>       heavy: qwen2.5:14b
> --- `prior-art/v0-glue/config.yaml`

#### RT-CMP-heavy-model
Label: Heavy model

Configured source-native role `foundry.models.heavy` is `qwen2.5:14b`. Representational form: distributed-parametric; storage is external Ollama weights. The design assigns compilation and review to heavy models; the study illustrates `llama3.3:70b`, not the configured prototype model. Parameter updates during operation: uninspected — providers and backend implementations excluded. Exact version pinned: no immutable digest in config or illustrated tag. Mutable endpoint can resolve another model: yes, addresses/tags are mutable; proxy payload may select another model. Fixed numerical state, if any, would not rule out retained-page changes. SRC-1, `prior-art/v0-glue/config.yaml`, `python_thoughts/05-heavy-llm-compilation.md`; the paired config quotation above supplies the configured identity.

#### RT-CMP-chat-model
Label: Chat model

Configured source-native role `frontline.models.chat` is `qwen3:30b-a3b`. Representational form: distributed-parametric; storage is external provider model files. Proxy routing chooses a URL by request priority, not a fixed model. Parameter change during operation: uninspected — no provider internals. Exact version pinned: no immutable model digest. Mutable endpoint can resolve another model: yes, configuration and payload choose mutable addresses/tags. SRC-1, `prior-art/v0-glue/config.yaml`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`.

>       chat: qwen3:30b-a3b
> --- `prior-art/v0-glue/config.yaml`

### Operative objects

#### RT-OBJ-proxy-queues
Label: PriorityQueueProxy queues

Source-native `queues` maps `chat`, `compile`, `lint` to deques of futures and request dictionaries. Representational form: symbolic, with fixed Python selection rules. Storage: process RAM only; not the proposed SQLite `jobs` queue. It coordinates pending calls and loses its pending state on process exit. SRC-1, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`.

>         self.sem = asyncio.Semaphore(1)  # one Ollama job at a time
>         self._worker = asyncio.create_task(self._loop())
> --- `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`

#### RT-OBJ-compile-template
Label: Article compilation template

The study's Jinja2 example supplies natural-language instructions, source material and related-page summaries to a model; template control syntax is symbolic, while rendered instructions gain effects through model interpretation. Storage is a proposed vault-side template registry and files, not an installed package template. It requests citations and cross-links, not verified factual correctness. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

> You are Mnemosyne, a knowledge compilation engine.
> Generate a wiki article from the provided source material.
> Follow these rules:
> - Use markdown formatting
> - Include inline citations [[source_id]]
> - Link to related concepts [[Concept Name]]
> - Flag contradictions with {{contradiction_marker}}
> - Target audience: {{ audience | default('general') }}
> --- `python_thoughts/05-heavy-llm-compilation.md`

### Routes

#### RT-RTE-client-query
Label: MCP ask and search

Endpoints: external client → stdio gateway → LLM-WIKI CLI / Link HTTP → client. Owner: fixed gateway dispatch; backend owns retrieval and generation. Open-request mode, not a curriculum. Client chooses question/query; no gateway model decides tool choice. No answer oracle is supplied. `kb_search` always calls LLM-WIKI and tries Link; Link exceptions become per-backend error entries. `kb_ask` calls only LLM-WIKI. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP text containing serialized backend stdout/stderr or Link JSON; exceptions become tool error text.
- Later read-back: backend vaults feed later search/ask requests; backend selection and persistence internals are uninspected.
- Delegated visibility: LLM-WIKI receives question/query and configured vault; Link receives query and limit, not source restriction.
- Selection predicate: fixed tool-name dispatch; source is reported but not applied; top_k affects only Link.
- Invalidation or expiry: uninspected — backend history/index invalidation is outside the bridge.
- Activation or effect: launches backend retrieval/synthesis requests; downstream client compliance or changed behavior unobserved.
- Evidence limits: static adapter wiring only; reported context_budget is not forwarded, history_budget is unused, and subprocess nonzero exit is not itself raised.

>         return {
>             "question": args["question"],
>             "answer": r.stdout,
>             "stderr": r.stderr,
>             "context_budget": args.get("context_budget", 24000),
>         }
> --- `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`

#### RT-RTE-foundry-tools
Label: Foundry ingest compile audit

Endpoints: MCP handlers → Synto/Synthadoc subprocesses and Link validation HTTP → MCP result. Owner: gateway code routes; external backends own model calls, artifacts and evaluations. Open requests. Caller proposes path or compile intent; filename extension / doc_type selects ingestion destination. Compilation chooses configured Synto vault regardless of the advertised vault argument; truthy auto_approve appends a flag. Audit scope selects Synto eval and/or Synthadoc lint, then always tries Link validation. Human versus software caller identity unresolved. No local per-content veto; backend rejection/approval remains uninspected. No supplied reference answers; an evaluation command alone does not establish an answer oracle. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected backend outputs in MCP text, not a gateway job ID or completed publish transaction.
- Later read-back: intended compiled/ingested backend artifacts can reach publication and later retrieval; backend durable-write outcomes unobserved.
- Delegated visibility: Synthadoc receives path/type; Synto receives path/vault or run/eval command; Link receives validate request.
- Selection predicate: office/PDF extension or non-auto doc_type selects Synthadoc; other paths select Synto; compile and audit use fixed handlers.
- Invalidation or expiry: uninspected — backend artifact/index lifecycle not present here.
- Activation or effect: requests ingest, compilation or checks under launcher permissions; does not automatically invoke publication.
- Evidence limits: timeouts bound waiting, not distributed completion; backend nonzero return codes generally remain output data.

Admission: compiler/backend proposes knowledge content; backend governs approval, with caller-requested bypass flag. Gateway does not inspect proposed text. Rejection ability and content rollback are external; local exception conversion is reporting, not rollback. Proposal-shaping guidance is backend-owned and unavailable in this implementation, distinct from the proposed study template. Recovery is caller retry with uncertain external state.

>         cmd = ["synto", "run", "--vault", vault]
>         if args.get("auto_approve"):
>             cmd.append("--auto-approve")
> --- `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`

#### RT-RTE-link-remember
Label: Link remember dispatch

Endpoints: caller content → Link `/api/remember` → gateway, or exception-triggered `link remember` CLI. Owner: gateway fallback policy; Link owns admission and retained state. Open-request mode. Caller proposes content and tags; whether a human supplied/approved them is unresolved. No local answer oracle, model adjudication or per-content human veto. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Link response JSON or CLI stdout/stderr wrapped as MCP text.
- Later read-back: intended Link memory can feed later Link queries; exact memory storage and selection semantics are external.
- Delegated visibility: HTTP receives content/tags/project; CLI fallback receives content and comma-joined tags but no project.
- Selection predicate: tool-name dispatch; exceptions on HTTP call or response decoding select CLI fallback.
- Invalidation or expiry: uninspected — Link retention/deletion behavior not supplied.
- Activation or effect: requests memory admission, not a gateway inbox/audit/human approval transaction; success and later behavioral activation unobserved.
- Evidence limits: HTTP status is not checked before parsing JSON; failure may be ambiguous after a remote write; no local deduplication.

Admission/recovery: caller proposes text, Link decides admission; gateway's exception branch cannot establish whether the first request wrote. Rollback and rejection policy external. Guidance shaping content belongs to caller/backend, not an inspected gateway prompt. What persists is opaque Link-owned memory, if admitted.

>             r = subprocess.run(
>                 ["link", "remember", args["content"], "--tags", ",".join(args.get("tags", []))],
>                 capture_output=True, text=True, timeout=30
>             )
> --- `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`

#### RT-RTE-vault-publish
Label: VaultSync publication

Endpoints: Foundry wiki directories → normalized unified vault → LLM-WIKI ingest/reindex and Link snapshot/load → optional Git commit. Owner: synchronous CLI `publish` and `VaultSync.run`. Open operator/caller request; not automatic on compilation in this driver. No answer oracle. Source backend content is the candidate; fixed software copying and normalization decide local admission. Starting publish is not per-page human approval. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`, `prior-art/v0-glue/jarvis_kb/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: console progress and completion messages, or uncaught filesystem/process-launch exception.
- Later read-back: written unified pages enter requested LLM-WIKI indexing and Link reload; gateway later queries those backend stores.
- Delegated visibility: normalized markdown reaches LLM-WIKI ingest-dir; Link receives tag/vault snapshot commands, not an explicit unified-vault path.
- Selection predicate: recursive markdown under each source wiki; Synto excludes .drafts; Synthadoc does not; same-relative-path world collision causes _ext rename.
- Invalidation or expiry: no deletion reconciliation in inspected loops; source removals do not explicitly remove destination pages. Repeated publication rewrites selected destinations.
- Activation or effect: writes files and requests backend reload; no evidence establishes successful reload or answer changes.
- Evidence limits: backend command contracts unavailable; nonzero exits ignored; optional Git commit covers unified files, not a cross-backend transaction.

Admission guidance: confidence thresholds map maturity (>0.8 established, >0.5 refining, otherwise seed); contradicted status maps disputed only when numeric confidence did not already select a branch. Body stays intact; selected title/maturity/tool/time/provenance/citations metadata persists, other keys do not. No local page-specific veto, hash comparison or approval check. Recovery: source files remain, optional Git history may help manual file recovery if commits succeed; no implemented coordinated rollback across recipients. Guarantee strength: best effort for external synchronization, not the proposed atomic-publish invariant.

>         # Best-effort: Link may not have snapshot CLI; adjust to your Link version
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

>         for md in src.rglob("*.md"):
>             # Skip drafts unless explicitly approved
>             if ".drafts" in md.parts:
>                 continue
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

>         post.metadata = clean
>         dst.parent.mkdir(parents=True, exist_ok=True)
>         dst.write_text(frontmatter.dumps(post), encoding="utf-8")
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

#### RT-RTE-model-proxy
Label: Ollama proxy routing

Endpoints: HTTP `/api/generate` or `/api/chat` → in-memory queue or dual-node router → Ollama → JSONResponse. Owner: startup configuration chooses mode; header chooses priority. Caller payload supplies model/context. No compiler/agent delegation or model decision within proxy. No answer oracle; open generation requests. SRC-1, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed backend JSON as one JSON response, not token streaming; forwarding timeout is 600 seconds.
- Later read-back: inapplicable — proxy does not retain responses for later invocations; provider-side state is uninspected.
- Delegated visibility: backend receives request payload minus internal _endpoint marker; proxy performs no inspected context trimming.
- Selection predicate: queue checks chat/compile/lint in order, FIFO inside each; unknown priority queues as compile. Router sends only chat to Frontline, everything else to Foundry.
- Invalidation or expiry: queues disappear on process exit; configured per-priority timeouts are not consulted by this implementation. Explicit cancellation/retry recovery is not implemented in inspected forwarding loop.
- Activation or effect: forwards generation requests; queue serialization covers only that instance, not direct model calls or router mode.
- Evidence limits: no observed latency, deadlock prevention or priority benefit; no preemption of running work and no deployed isolation evidence.

>         target = self.frontline if priority == "chat" else self.foundry
> --- `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`

>             if self.queues["chat"]:
>                 return self.queues["chat"].popleft()
>             if self.queues["compile"]:
>                 return self.queues["compile"].popleft()
> --- `prior-art/v0-glue/jarvis_kb/ollama_proxy.py`

#### RT-RTE-design-lifecycle
Label: Proposed compilation lifecycle

Endpoints: raw sources → extracted concepts → article → audit result → published page or rejected draft → another compilation/query. Owner: proposed OS orchestration; fast/heavy/audit roles are model computations, approval may be human or configured automatic policy. Operating mode: open ingestion/compilation requests; later prompt optimization is separately proposed for metric-based experiments, not current operation. No expected-answer oracle for ordinary article admission: audit judgment and threshold are not reference truth. SRC-1, `ARCHITECTURE.md`, `AGENTS.md`, `python_thoughts/05-heavy-llm-compilation.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed typed extraction/article/audit artifacts and finalized publication or rejection feedback.
- Later read-back: proposed published pages inform query and compilation; rejection_feedback is intended as recompile input.
- Delegated visibility: proposed Python satellite receives source/concept/article files and renders templates with related-page summaries and flagged contradictions; exact complete assembled context unobserved.
- Selection predicate: stage sequencing, template variables and audit threshold; human gate if configured.
- Invalidation or expiry: proposed incremental compilation/hash guards; no inspected deployed invalidation protocol.
- Activation or effect: requests model extraction, writing, critique and knowledge admission; compliance and resulting quality unobserved.
- Evidence limits: study snippets are design examples, not a wired unified runtime; proposed policies differ in model sizes and maturity across documents.

Admission: models propose articles and audit recommendations. Threshold logic proposes publication or return to drafts; configured human approval can veto. Rejected drafts retain feedback for a new attempt. Rollback is not specified as a coordinated deployed transaction. Guidance: rendered compile template requests citations, links and contradiction flags; audit compares article against existing pages. Proposed persistent material includes articles, claims, contradiction descriptions, template versions/hashes and audit records. Product or capability revisions do not follow merely from editing knowledge pages.

>     - Score >= threshold: promote to wiki/
>     - Score < threshold: return to drafts/ with feedback
>     - Human approval gate (if configured)
> --- `python_thoughts/05-heavy-llm-compilation.md`

Theory scope: articles may contain formulated explanations, but an ArticleOutput label alone does not establish a theory. The examples request compilation and inconsistency detection rather than demonstrating theory revision. Theory-builder conditions 1–4: (1) claimed — templates solicit localized claims/explanations; actual resulting theories uninspected; (2) claimed — related pages/contradictions are intended to inform model decisions, dependence on a particular theory unobserved; (3) uninspected — contradiction reporting does not establish placement of blame plus changed reliance/revision; (4) claimed — rejection feedback is intended to shape recompilation, but retained content-directed criticism shaping another round is unobserved. Addressability: proposed page/claim/contradiction fields give some inspectable units, not established addressability of every assumption. Persistence: proposed files/SQLite across sessions; later consumption is design-level. Learning: improved future capacity and attribution uninspected. Reflection: audit represents content properties and intends to affect later content, but a live two-way self-representation of operating machinery is not established. Reflective theory builder and autonomous theory builder: uninspected — internal criticism/iteration and complete computational ownership are not established, and human gating is configurable rather than uniformly absent. No exercised self-improvement is attributed.

### Claims

#### RT-CLM-publish-atomicity
Label: Atomic publication claim

Claimed operation: unified publish engine promotes drafts and rebuilds indexes, graph and packs transactionally. This is doctrine/design, not established by the bridge's sequential filesystem and subprocess operations. Owner: proposed publish engine; guarantee strength: invariant as a design claim. Covered design route: [RT-RTE-design-lifecycle](#rt-rte-design-lifecycle). Inspected legacy contrast: [RT-RTE-vault-publish](#rt-rte-vault-publish). External transaction/recovery contract unavailable. SRC-1, `ARCHITECTURE.md`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

- design conclusion status: claimed
- operation conclusion status: uninspected

> Atomic promotion from `.drafts/` to `wiki/`.
> Rebuilds search index, graph, and agent packs in one transaction.
> --- `ARCHITECTURE.md`

#### RT-CLM-write-guards
Label: Write guard policy

Claimed operation: canonical Phase 2 policy grants open writes, conditional hash-checked writes, or human-only frozen writes. Owner: proposed page-write path. Guarantee strength: policy. No caller authentication, guard checking or approval enforcement is established by the legacy copier. Initial DDL has content_hash/approved_at but no write_guard column; a stored hash alone is not an enforcement point. SRC-1, `SPECIFICATION.md`, `schema/001-init.sql`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

- design conclusion status: claimed
- operation conclusion status: uninspected

> - `open`: any agent can write (default for new pages)
> - `protected`: agent can write only if `content_hash` matches expected (prevents overwrites of compiled content)
> - `frozen`: only human can write (hand-edit protection)
> --- `SPECIFICATION.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-compile-guidance
Label: Compilation template authority

Consumer: proposed heavy compilation model. Channel: rendered template supplied as model input with source/related pages. Force: interpretive instruction requesting article structure, citations, cross-links and contradiction markers, not a code-enforced truth guarantee. Horizon: an intended compilation invocation; registry versions are proposed to persist across invocations. Referent: [RT-OBJ-compile-template](#rt-obj-compile-template); route: [RT-RTE-design-lifecycle](#rt-rte-design-lifecycle). The source's illustrated Instructor call supplies the whole prompt as a user message, so the risk table's recommended separation of source and system instructions must not be assumed already enforced by that example. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

>         messages=[{'role': 'user', 'content': prompt}],
>         response_model=ArticleOutput,
> --- `python_thoughts/05-heavy-llm-compilation.md`

## Annotations

none
