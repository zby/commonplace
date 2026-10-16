---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenClerk runtime baseline tracing agent context, session planning, document admission, semantic modules and evaluation callers at the frozen commit."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
---

# OpenClerk runtime report

## Runtime account

### Boundary and ordinary invocation

OpenClerk supplies a knowledge interface to an external coding agent, not the agent's enclosing model/tool scheduler. The [boundary](boundary.md) freezes SRC-1. This account uses implementation and doctrine/design evidence from that repository only. No target commands, tests, model calls or experiments were run. All operation and behavioral-benefit conclusions below remain uninspected; implementation wiring is not evidence of compliance.

The intended ordinary loop is: inspect readiness, request task context, read cited knowledge, do application work, submit an explicit session artifact for planning, and apply approved document changes. The CLI dispatches document, retrieval, clerk and module families (SRC-1, `cmd/openclerk/main.go`). The external user supplies a task; the coding agent chooses tools under shipped natural-language instructions. Go code owns each individual CLI action and returns JSON. The external agent owns the next model invocation and whether to act on the result. The distinction is material: OpenClerk does not acquire control of the host merely by returning an `agent_handoff`.

> 4. Do the work outside OpenClerk.
> 5. After work, pass an explicit session note, handoff, or inbox artifact to the
>    read-only `openclerk clerk` planning surface.
> 6. Apply durable writes only through approved `openclerk document` lifecycle
>    APIs.
> --- `docs/agent-contract.md`

For a concrete ordinary invocation, `clerk context_pack` receives task/query, path prefix and limit. Chronicler prefers an explicit query over task text, checks existing storage, then calls search and decision lookup. It constructs must-read entries from ranked hits, including snippets and citations, and decision entries from report summaries; a requested path prefix also filters decision citations. It deduplicates citations, flags no search hits and missing decision evidence, and returns a read-only envelope. This is selected evidence, not a full vault or a verification of the answer. [RT-RTE-context-pack](#rt-rte-context-pack) records the route. The external agent must request full documents if needed; what it actually keeps in its context is outside the inspected core (SRC-1, `internal/chronicler/chronicler.go`).

After work, `clerk session_record_report` or `run` takes explicitly named inbox files. It invokes document artifact planning for each and returns candidates, pending review and duplicate warnings, rather than applying changes. There is no model call in this inspected planning chain. Proposed paths and recommended actions cross back as data to the host, not executable callbacks. [RT-RTE-session-plan](#rt-rte-session-plan) identifies this handoff; document writes are a separate admission boundary, [RT-RTE-document-write](#rt-rte-document-write) (SRC-1, `internal/chronicler/chronicler.go`, `internal/runner/document.go`).

### Three forcing cases and their limits

**1. A write request without a separate human approval event.** The contract requires approval of proposed content, but normalization defaults an omitted approval mode to `approve_write`. The runner rejects `propose_only` for the checked mutating actions; it does not authenticate a human approval in that check. Creation reaches `CreateDocument` after normalization and the runner write lock. Therefore explicit human consent is a host/agent policy, not a universal technical gate. A caller controlling JSON can select a permissive mode. Persisted profiles can change defaults, and request fields override them; this is not proof of a deployment's current grants (SRC-1, `internal/runner/autonomy.go`, `internal/runner/document.go`, `skills/openclerk/SKILL.md`). [RT-CLM-approval-boundary](#rt-clm-approval-boundary) keeps the distinction.

**2. A semantic request beyond the default read path.** Default context packs call lexical search, not semantic search. Explicit `semantic_search` checks installation, enabled state and provider configuration, invokes a local adapter subprocess and validates its response. Installed module hashes bind local manifest/executable identity, not remote model weights. The adapter can write its embedding cache even though it opens canonical storage read-only. Direct adapter requests also expose an explicit fallback-provider field; the runner's constructed request does not expose that field. Thus neither “all reads are physically side-effect free” nor “the adapter can never use fallback” follows from the routine skill's local/no-fallback policy. See [RT-RTE-semantic-search](#rt-rte-semantic-search) and [RT-RTE-module-install](#rt-rte-module-install) (SRC-1, `internal/runner/semantic_search.go`, `internal/runclient/modules.go`, `modules/semantic-retrieval-adapter/main.go`).

**3. A shipped model-driven caller with durable session continuity.** The evaluation driver invokes Codex, carries a returned session ID across turns and verifies results. Single-turn jobs instead use `--ephemeral`. These are shipped paths, not core inference machinery. They show that external model/tool access and resumed host context can coexist with the CLI contract. The script supplies writable roots and `--full-auto`; actual sandbox enforcement and model internals remain external. [RT-RTE-eval-turn](#rt-rte-eval-turn) records the deterministic orchestration and answer oracle, without adopting any evaluation score as an observed result (SRC-1, `scripts/agent-eval/ockp/codex_runner.go`).

### Enforcement and alternate-path coverage

| Load-bearing guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths and required external contract | Conclusion statuses |
|---|---|---|---|---|
| Chronicler plans rather than applies durable document changes | Chronicler `runPlan`, `addInboxScan`, `buildContextPack`; read-only runner operations | invariant within this inspected planning call chain; result reports candidates and blockers | A subsequent document action is separate. Host tools, raw file edits and direct client calls are not constrained by the returned envelope. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Proposed content needs approval | Agent contract and skill; runner rejects an explicit `propose_only` mode | policy for human approval; narrower symbolic mode check in runner | Permissive/default modes, direct store calls, host shell/file tools, demo/evaluation seeding and module subprocesses cannot be covered by this prose approval rule. Host must enforce human decisions if required. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Writes through the runner are sequenced | `WithWriteLock` around selected mutating document branches | protocol among cooperating processes using the same resolved database path | Raw vault editors, other database paths and direct APIs are not locked by this wrapper. Requires cooperating writers and a working local filesystem/process-liveness contract. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Optional module execution uses an installed, enabled, verified binding | Module configuration read/verification and runner dispatch | protocol on installed runner semantic path | Direct adapter execution has its own validation; a hash is not isolation of executable behavior. Requires local binary/file integrity and OS permissions; provider service remains external. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence for these rows is in the routes and claim records below. The write lock retries every 25 ms, gives up after five seconds or context cancellation, and attempts stale-lock removal. It is not a file-plus-database transaction. Creation writes the canonical file before synchronizing derived state; an error at synchronization can therefore follow a successful file write. Replacement receipts include a preimage hash and rollback request; rollback requires another explicit action, not an automatic reversal. These facts prevent stronger all-or-nothing or universal writer-isolation claims (SRC-1, `internal/runclient/local.go`, `internal/infra/sqlite/documents.go`, `internal/runner/document.go`).

Capability surface is not current grant set: code includes document mutation, source ingestion, module configuration and subprocess execution. Current grants depend on profiles, installed modules, OS access and host tools, none supplied as deployment evidence. The deployed isolation envelope is unobserved. Direct model calls, provider-native tools, host callbacks, remote workers and manual host graph control are not governed by a core OpenClerk scheduler in these traced paths. That is a boundary limit, not a global absence finding. Module subprocesses and the evaluation's Codex subprocess are positively wired alternatives. OCR is another advertised module path in the skill, but its executor was not traced here; no OCR isolation or correctness conclusion is made (SRC-1, `skills/openclerk/SKILL.md`).

### Evidence coverage added

Beyond initial boundary inspection, this member inspected the relevant bodies of `internal/runner/autonomy.go`, `internal/runner/document.go` (normalization gate, mutation dispatch and replacement receipts), `internal/runner/semantic_search.go` (dispatch/request/subprocess), `internal/runclient/modules.go` (install/configure), `internal/runclient/local.go` (write lock), `internal/chronicler/chronicler.go` (planning and context conversion), `modules/semantic-retrieval-adapter/main.go` (search, normalization and cache/provider branches), `scripts/agent-eval/ockp/codex_runner.go` (turn invocation), and `scripts/agent-eval/ockp/verify_helpers.go` (document oracle). All are SRC-1 implementation evidence. Full `skills/openclerk/SKILL.md` and `docs/agent-contract.md` supply doctrine/design. Constant searches in `scripts/agent-eval/ockp/constants.go` identify the evaluation model label. These are added coverage, not additional sources or execution traces. Source-fetch internals, OCR execution, synthesis/graph maintenance internals and release delivery remain outside this runtime trace's detailed inspection; this report makes no exhaustive control-equivalence or performance claim for them. Retained-memory revision details belong to the memory member.

## Shared records

### Components

#### RT-CMP-embedding-provider
Label: Embedding provider

Source-native identity: Ollama or Gemini embedding model selected by semantic adapter request/config. Representational form: distributed-parametric model parameters; returned dense vectors are separately derived numerical representations. Storage substrate: external provider runtime, inaccessible here. SRC-1, `modules/semantic-retrieval-adapter/main.go`, implements embedding inference, model-name selection and ranking, not a parameter-update protocol. Parameters changing during operation: uninspected — provider internals are outside the frozen source. Exact parameter version pinned: not established by a model name. A mutable service/model endpoint can resolve to different weights; local executable SHA verification does not pin those weights. This component is used by [RT-RTE-semantic-search](#rt-rte-semantic-search).

> request.EmbeddingModel = defaultModel(request.Provider, strings.TrimSpace(request.EmbeddingModel))
> --- `modules/semantic-retrieval-adapter/main.go`

#### RT-CMP-codex-model
Label: Codex evaluation model

Source-native identity: evaluation constant `modelName = "gpt-5.4-mini"`, with medium reasoning effort. Representational form: distributed-parametric provider model; storage substrate: external Codex/provider service. The driver supplies a model label, not an immutable weight digest. Parameters changing during operation: uninspected — no access to provider internals. Exact version pinned: not established; the endpoint can resolve the label to another model version. The inspected driver requests inference, not training. Used by [RT-RTE-eval-turn](#rt-rte-eval-turn). SRC-1, `scripts/agent-eval/ockp/constants.go`, `scripts/agent-eval/ockp/codex_runner.go`.

> "-m", modelName,
> --- `scripts/agent-eval/ockp/codex_runner.go`

### Operative objects

#### RT-OBJ-agent-contract
Label: OpenClerk agent contract

Source-native identity: shipped `skills/openclerk/SKILL.md` router and compact `docs/agent-contract.md`. Representational form: natural-language behavioral instructions, with symbolic command examples. Storage substrate: versioned Markdown files; loaded by an external skill-capable host. Their advice concerns runner use, approval, evidence authority and answering from handoffs, not modifications to model weights. [RT-BAP-skill-routing](#rt-bap-skill-routing) identifies the consumer and force. SRC-1, `skills/openclerk/SKILL.md`, `docs/agent-contract.md`.

> Answer routine OpenClerk requests only from runner JSON results.
> --- `skills/openclerk/SKILL.md`

### Routes

#### RT-RTE-context-pack
Label: Task context pack

Endpoints/progression: user/agent task or query → Chronicler `RunContextPack` → existing-storage check → retrieval search and decision lookup → converted JSON context pack → external agent. Owner: deterministic Go rules choose hits/fields; host owns subsequent reasoning. Context/state: task, query, path prefix, limit and existing derived storage. Representational form: symbolic selection/JSON wrapper carrying natural-language titles, snippets and decision summaries. No autonomous provider invocation is needed for this route. SRC-1, `internal/chronicler/chronicler.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: must-read hit snippets/citations, decision summaries, open questions, warnings and read-only envelope.
- Later read-back: existing retained vault/index material is selected into a later task invocation; this route does not itself revise it.
- Delegated visibility: host receives only converted report fields; no isolated subagent frame is implemented by this function.
- Selection predicate: explicit query takes precedence over task text; search receives prefix/limit, decisions are also filtered by prefix before delivery.
- Invalidation or expiry: no host-window eviction or TTL in this route; storage freshness is separate evidence, not automatically repaired here.
- Activation or effect: delivers a bounded context pack; whether the model reads full documents or changes behavior remains unobserved.
- Evidence limits: source wiring only; selected snippets and report summaries do not establish complete or correct context.

Working-context control: code decides a bounded external-material selection, not trimming of an accumulated host window. Selected values cross the CLI boundary by value. The remaining vault is reachable through later runner requests; a citation is not a live pointer automatically dereferenced by a model. Host compaction/isolation remains uninspected. Decision policy is code-defined retrieval, not a model answer oracle. Operating mode: open task requests, not a curriculum.

> MustRead:              []ContextDocument{},
> RelevantDecisions:     []ContextDecision{},
> --- `internal/chronicler/chronicler.go`

#### RT-RTE-session-plan
Label: Explicit session planning

Endpoints/progression: external caller's explicit inbox paths → `RunSessionRecordReport`/`RunOnce` → `addInboxScan` → runner artifact plan → candidates, duplicate risks and pending review. Owner: Chronicler's code orchestrates deterministic planning; external agent/user owns acceptance. State: explicit files and existing knowledge storage. Symbolic reports carry natural-language proposed content and source references. SRC-1, `internal/chronicler/chronicler.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposed paths/actions, pending review, duplicate warnings and blockers; zero applied document writes in this planning chain.
- Later read-back: uninspected — returned plans have no persistence route in this function; any later retention requires another caller/action.
- Delegated visibility: named session artifact reaches artifact planning; selected candidate metadata reaches the caller, not a remote worker.
- Selection predicate: explicit inbox file list; each supported plan receives a bounded limit; no implicit whole-session transcript ingestion is established.
- Invalidation or expiry: plans are snapshots without a persisted approval queue; later vault changes require rechecking relevant evidence.
- Activation or effect: returns recommendations only; a separate document lifecycle call produces a durable effect.
- Evidence limits: candidate policy internals were not exhaustively traced; returned recommendation is not evidence of approval or application.

Admission account: trigger is an explicit session request; proposal is a candidate document/update recommendation. Code proposes; user/agent decides whether to submit a subsequent write and can reject by not doing so. Human content approval is requested by doctrine but not observed. No answer oracle in this planning route; duplicate evidence is not a reference correct answer. Operating mode: open session intake. Guidance is the shipped agent contract's plan-before-approved-write policy; this function retains no durable revision or criticism. Recovery is correction/replanning of a rejected or blocked request, not automatic replay of a write.

> PlannedNoWrite:   true,
> WritesPerformed:  0,
> --- `internal/chronicler/chronicler.go`

#### RT-RTE-document-write
Label: Document lifecycle admission

Endpoints/progression: caller JSON → normalization/profile/defaults → checked autonomy/write-target restrictions → runner write lock → write client → store lifecycle → canonical Markdown then derived synchronization → document/result JSON. Source-native targets include create, append, replace, move/promote, ingestion and synthesis branches; replacement has a dry-run alternative. The creation/replacement paths are the detailed witnesses here, not proof that every branch has identical checks. Owner: caller determines proposed content; code validates and executes. SRC-1, `internal/runner/document.go`, `internal/runner/autonomy.go`, `internal/infra/sqlite/documents.go`, `internal/runclient/local.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: document or rejection; replacement also returns compact diff, preimage hash, handoff and, when applied, a rollback request.
- Later read-back: created/replaced canonical material and synchronized derived storage can feed future retrieval/document requests.
- Delegated visibility: runner and local store see supplied content; downstream host gets result JSON, not a newly delegated model context.
- Selection predicate: explicit target/body or normalized proposal; action, dry-run and autonomy mode determine admission; existing-only mode rejects checked create-shaped actions.
- Invalidation or expiry: durable content has no route-local TTL; downstream derived freshness must be assessed separately.
- Activation or effect: direct filesystem document write and synchronization; semantic influence on a future agent remains unobserved.
- Evidence limits: no deployed approval evidence; synchronization after filesystem write does not establish transactional rollback; lower-level writers need not acquire this runner lock.

Admission: caller proposes, runner makes syntactic/mode/path decisions and can reject. Human approval is a natural-language requirement, not authenticated here. In the inspected default path an omitted mode becomes `approve_write`; explicit `propose_only` is vetoed. Operating modes include open requests and explicitly trusted/disposable modes, not a single universal human gate. No reference-answer oracle governs ordinary writes. Guidance shapes proposed content through the skill; persisted output is Markdown plus derived state, not a guaranteed improvement. For replacement, caller can preview and then apply; applied receipts supply a compensating request, which must itself be run. Creation errors after the canonical write can require resynchronization rather than assuming nothing happened.

> if normalized.ApprovalMode == "" {
>     normalized.ApprovalMode = ApprovalModeApproveWrite
> }
> --- `internal/runner/autonomy.go`

> if normalized.Autonomy.ApprovalMode == ApprovalModeProposeOnly {
>     return "autonomy.approval_mode propose_only does not allow mutating document actions"
> }
> --- `internal/runner/document.go`

> if err := s.syncDocumentFromDisk(ctx, relPath, input.Title); err != nil {
>     return domain.Document{}, err
> }
> return s.getDocumentByPath(ctx, relPath)
> --- `internal/infra/sqlite/documents.go`

> if writeStatus == "applied" {
>     result.NextWriteRequest = ""
>     result.RollbackRequest = rollbackReplaceDocumentRequest(after.DocID, after.Path, before.Body)
> }
> --- `internal/runner/document.go`

#### RT-RTE-semantic-search
Label: Explicit semantic search

Endpoints/progression: explicit retrieval request → installed/enabled module config → constructed adapter request → local subprocess → provider embedding/cache/ranking → validated response → caller. Owner: deterministic runner/adapter code; embedding computation belongs to [RT-CMP-embedding-provider](#rt-cmp-embedding-provider). Canonical storage is opened read-only by adapter; derived embedding cache is writable. SRC-1, `internal/runner/semantic_search.go`, `modules/semantic-retrieval-adapter/main.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked citation-bearing semantic hits/handoff or explicit blocked/invalid-contract status.
- Later read-back: adapter cache may reuse document vectors on a subsequent query; model weight learning is not established.
- Delegated visibility: local adapter receives query, filters, database path and configured provider settings; embedding provider receives embedding text, not the entire agent session by this route.
- Selection predicate: explicit semantic action/provider, filtered document chunks, embedding similarity/ranking and limit; default context search is not replaced.
- Invalidation or expiry: cache identity uses request/corpus data and validates cache reads; mutable provider weights under an unchanged name remain an unresolved freshness risk.
- Activation or effect: numerical ranking and optional derived-cache writes are wired; host behavior change and retrieval-quality benefit unobserved.
- Evidence limits: local subprocess has OS-process authority, not a demonstrated sandbox; external provider handling and exact weights are uninspected.

Control variants matter. Runner requests use configured provider endpoints and a fixed cache location. Direct adapter requests can specify a fallback provider, and the adapter retries embedding with it after an error; the runner request builder does not forward a fallback field. Provider failure produces `provider_blocked`, not success-shaped canonical evidence. The subprocess decoder limits decoded output to 4 MiB, but stdout/stderr are collected in buffers before decoding; this is not a demonstrated whole-process memory bound. Cache-write errors are ignored in the inspected rebuild branch, so a successful search does not guarantee durable cache admission. These are implementation distinctions, not measured latency/reliability conclusions.

> command := exec.CommandContext(ctx, moduleConfig.Command, args...)
> command.Stdin = bytes.NewReader(payload)
> --- `internal/runner/semantic_search.go`

> if err != nil && request.FallbackProvider != "" && request.FallbackProvider != request.Provider {
> --- `modules/semantic-retrieval-adapter/main.go`

> _ = writeCache(cachePath, cache)
> --- `modules/semantic-retrieval-adapter/main.go`

#### RT-RTE-module-install
Label: Optional module admission

Endpoints/progression: explicit install/configure request → provider/manifest/config validation → bound executable path/hash → runtime configuration persistence → subsequent semantic dispatch. Owner: local client code; caller chooses enabled state and configuration. Representational form: symbolic manifest/config and hash binding, stored in local runtime configuration. SRC-1, `internal/runclient/modules.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: verified/redacted module configuration or error.
- Later read-back: later semantic requests read installed module configuration and require enabled state.
- Delegated visibility: selected executable receives the adapter request at invocation; no automatic model-generated extension installation is established.
- Selection predicate: supported provider, required manifest, no arbitrary semantic command arguments, resolved executable allowed by manifest and configuration validation.
- Invalidation or expiry: stored manifest/executable SHA binding is verified on configured use; disabling/removing configuration can withdraw future runner use.
- Activation or effect: persists capability configuration; execution occurs on a later explicit request, not merely on install.
- Evidence limits: binding identifies local executable bytes; it proves neither safe executable behavior nor immutable provider semantics.

Admission account: explicit caller triggers a capability change, supplying manifest, executable and provider configuration. Code rejects invalid bindings/configuration; enabled defaults to true on successful install. Human approval is requested by the agent contract but no per-content human authenticator was inspected in this client install function. Operating mode: explicit administration, no discovered autonomous capability-upgrade loop. No answer oracle. Removal/disable can roll back configuration availability; it does not undo provider disclosure or arbitrary prior subprocess effects. Guidance is the contract's install/enable/verify rule; durable configuration, not a new theory or model weights, persists.

> CommandSHA256:        commandSHA,
> ManifestPath:         manifestPath,
> ManifestSHA256:       manifestSHA,
> --- `internal/runclient/modules.go:116-118`

#### RT-RTE-eval-turn
Label: Evaluation agent turn

Endpoints/progression: scenario/variant setup → prompt and writable roots → timed Codex subprocess → JSONL/stdout and stderr files → parse final message/session/metrics → scenario verification → possible next turn with session ID. Owner: deterministic evaluation driver schedules; external Codex model chooses tools/actions within supplied host configuration. SRC-1, `scripts/agent-eval/ockp/codex_runner.go`, `scripts/agent-eval/ockp/verify_helpers.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: turn result, exit code, parsed message/session ID, timings/metrics and verification result at the driver level.
- Later read-back: multi-turn jobs resume the returned Codex session ID and consume the scenario's previously changed local state; single-turn jobs request ephemeral context.
- Delegated visibility: scenario prompt and installed variant/environment go to an external Codex process; driver receives output artifacts, not hidden provider reasoning.
- Selection predicate: scenario/variant and turn index determine prompt/config; single versus multi-turn selects ephemeral versus resumable host context.
- Invalidation or expiry: each turn has a seven-minute context deadline; host session expiration/compaction is uninspected.
- Activation or effect: driver can run an agent against seeded local knowledge and collect result/state checks; no actual execution or benefit is established by this inspection.
- Evidence limits: host flags are requested controls, not proof of deployed sandbox behavior; bundled source code alone is not an observed run.

Operating mode: bounded scenarios, not ordinary open production requests. Scenario authors supply expected outcomes; verification code is an answer oracle for bounded assertions, not a model judge. For example, `verifyDocumentContains` reads a document body and checks required/forbidden strings. Code decides pass/fail; the external agent proposes/executes work. Human design of scenarios does not equal per-write approval. Results may inform product maintenance, but no automatic product-successor admission route is established by these turn/verify functions. Changes to released code or instruction texts require a development/release path not traced here. Working-context control: single-turn `--ephemeral` versus ID-based resume changes context lifetime; internal host trimming, isolation and summaries are not visible. No claim of a target-owned subagent stack is warranted.

> cmdCtx, cancel := context.WithTimeout(ctx, 7*time.Minute)
> --- `scripts/agent-eval/ockp/codex_runner.go`

> args = append(args, "resume", "--json", "--full-auto", "--skip-git-repo-check", "--ignore-user-config")
> --- `scripts/agent-eval/ockp/codex_runner.go`

> failures := missingRequired(body, required)
> failures = append(failures, presentForbidden(body, forbidden)...)
> --- `scripts/agent-eval/ockp/verify_helpers.go`

### Claims

#### RT-CLM-approval-boundary
Label: Approval before durable writes

Claimed operation: explicit approval precedes durable local changes. SRC-1, `docs/agent-contract.md`, `skills/openclerk/SKILL.md`. Guarantee owner: external agent/user contract. Enforcement: natural-language policy, supplemented by checked runner mode restrictions in [RT-RTE-document-write](#rt-rte-document-write). Guarantee strength: policy. Policy conclusion status: claimed. Implementation conclusion status: wired for the narrower mode veto, not human-authenticated consent. Operation conclusion status: uninspected. Alternate direct caller/store/file/module paths prevent extending the policy to universal access control. Required external contract: host follows the skill and withholds write actions until appropriate approval.

> Approval is required before creating, appending, replacing, moving, renaming,
> promoting, fetching into, or configuring durable local state. Read, fetch,
> inspect, and plan permission is not durable-write approval.
> --- `docs/agent-contract.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-routing
Label: Skill routed runner behavior

Consumer: external coding agent. Channel: loaded OpenClerk skill and compact agent contract, followed by runner JSON `agent_handoff` instructions. Force: natural-language policy/request; delivery does not prove compliance and gives no OS capability restriction. Horizon: shipped instruction version across tasks, plus current-request handoff within a task. The contract tells the model to prefer workflow actions and answer from selected returned evidence. This is a live intended authority path, not evidence that instructions or retained knowledge actually changed an observed answer. SRC-1, `skills/openclerk/SKILL.md`, `docs/agent-contract.md`; operative text is [RT-OBJ-agent-contract](#rt-obj-agent-contract).

> For promoted workflow actions, answer from the first
> successful returned handoff; do not repeat the same action or inspect
> follow-up primitives unless the result rejects or the user asks for more.
> --- `skills/openclerk/SKILL.md`

## Annotations

none
