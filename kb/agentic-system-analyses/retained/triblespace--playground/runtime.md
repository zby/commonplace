---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Playground runtime baseline: tenant sandbox execution, bounded jobs, file exchange and the optional native-worker gateway."
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
---

# Playground runtime report

## Runtime account

Playground transports caller-selected work; it does not select an agent's next reasoning step. The enclosing MCP client supplies commands and consumes results. The shipped executable selects stdio, authenticated HTTP, operator account/lifecycle commands, or cleanup. HTTP selects either the sandbox catalogue or the native-worker catalogue, never their union. These are inspected implementation paths, not observed successful executions. SRC-1: `src/main.rs`, `src/mcp.rs`, `src/mcp_http.rs`, `src/mcp_http/workers.rs`. No run trace, model invocation or experiment was supplied or performed.

### Ordinary invocation and ownership

An operator first provisions a tenant and credentials through [RT-RTE-tenant-provision](#rt-rte-tenant-provision). The HTTP sandbox startup builds the configured backend and calls `reattach_all`; stdio builds a backend but has no equivalent startup sweep in its entry function. An HTTP client authenticates, initializes a transport session, calls `open_session`, submits `exec`, receives a terminal result, and releases its sandbox handle. The transport session, persistent sandbox identity and job identity are separate. `open_session` names an existing tenant, not caller-selected host storage. The HTTP layer fills the tenant from the authenticated account and checks sandbox/job ownership before dispatch. SRC-1: `src/main.rs`, `src/mcp_http.rs`, `src/mcp.rs`; [RT-RTE-sandbox-exec](#rt-rte-sandbox-exec).

The provider maintains tenant/session reference counts and lifecycle locks. Same-tenant handles share a backend sandbox; last-handle close detaches it without deleting persistent storage. Locks serialize same-tenant open, start and close within the provider process, not across a separate operator CLI process. Each command becomes a symbolic `ExecRequest`: shell text, shell mode, optional cwd/stdin and timeout. A fresh shell executes that request; login profiles supply defaults. Persistent filesystem/process state does not mean one continuously running shell preserves each preceding command's `cd` or shell-local assignments. SRC-1: `src/mcp.rs`, `src/sandbox/mod.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

The job manager admits bounded work, owns the next backend step and starts a host thread. Jail uses privileged `timeout ... jexec ... /bin/sh`; Lima invokes `limactl shell`. Output drains into bounded state; synchronous execution waits, renders the terminal result and forgets the hidden handle. Tool failures become MCP `isError` content rather than JSON-RPC protocol failures. The client, not this provider, decides whether and how to continue. SRC-1: `src/jobs.rs`, `src/mcp.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

### Selected forcing routes and guarantee coverage

Four forcing cases qualify the ordinary account: unauthenticated stdio/direct dispatch versus HTTP admission; retained jobs versus synchronous execution on different backends; clean-shell file exchange versus login-shell commands; and the native-worker gateway versus sandbox dispatch. Their records below preserve effects, returns and limits. No exhaustive security audit or deployment isolation proof is claimed.

**Tenant authorization** is owned by the HTTP transport. Enforcement occurs in `authenticate`, `validate_session` and `enforce_tenant_scope` before sandbox dispatch. Guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. It covers authenticated sandbox HTTP and tenant-owned transport sessions; native workers instead use an authenticated fixed tenant mapping plus wrapped upstream session. It does not cover stdio or direct `McpServer::handle_request` calls, nor the content of commands executed within an authorized tenant. The external contract is operator-local trust for stdio, private credential files, correct account/backend configuration, and TLS/reverse-proxy deployment for public HTTP. Revocation is checked on subsequent requests, not a promise to undo already accepted effects. SRC-1: `src/mcp.rs`, `src/mcp_http.rs`, `src/mcp_http/workers.rs`; [RT-RTE-sandbox-exec](#rt-rte-sandbox-exec), [RT-RTE-worker-forward](#rt-rte-worker-forward).

**Execution bounds** are owned by `JobManager`, with active and retention checks under one mutex. Guarantee strength: invariant within this execution kernel. Implementation conclusion status: wired. Operation conclusion status: uninspected. Both synchronous execution and retained jobs use it; file tools also use synchronous execution. The sandbox kernel permits eight active jobs per tenant and 32 globally, eight retained handles per tenant and 64 globally; each ring retains at most 4 MiB and 1024 chunks. It refuses submissions when unread/running handles cannot yield capacity; terminal TTL is a separate exception that can discard unread results. These are not limits on worker-native allocation or arbitrary background processes started by shell commands. Callers own ordering between concurrent mutations. External contracts include backend execution termination and host resource controls. SRC-1: `src/jobs.rs`, `src/mcp.rs`; [RT-RTE-retained-jobs](#rt-rte-retained-jobs).

**Cancellation/descendant cleanup** is owned by the root-local FreeBSD runner and backend, with job-manager fail-stop and transport fatal handling. Guarantee strength: deployment guarantee. Implementation conclusion status: wired. Operation conclusion status: uninspected. Background jobs are admitted only when the backend advertises proof-capable cancellation; production `LocalRunner` requires FreeBSD and root. Jail clamps timeout and wraps command execution in the server's reaper. Loss of cleanup proof marks the capable provider fatal rather than resetting the tenant sandbox. Remote SSH and Lima do not admit retained background jobs. Killing a local wrapper does not prove guest/remote work stopped; worker gateway timeout likewise leaves an unknown execution outcome. Required contracts are the FreeBSD reaper semantics, privileges and host setup, not merely a caller timeout field. SRC-1: `src/sandbox/runner.rs`, `src/sandbox/jail.rs`, `src/jobs.rs`, `src/mcp_http/workers.rs`.

**Append-only storage is backend-dependent**, not a universal provider guarantee. Jail provisioning sets host `sappnd` flags and installs fixed pile mounts, but actual enforcement requires the host/kernel and privilege envelope. Lima's guest setup explicitly tolerates `chattr` failure on virtiofs. Therefore the README's blanket append-only phrasing cannot establish Lima truncation prevention. File `write` uses truncating redirection; unrestricted shell commands offer another path. This report does not establish the semantics of entries appended by external faculty binaries. SRC-1: `src/sandbox/jail.rs`, `src/sandbox/lima.rs`, `src/mcp.rs`, `README.md`.

> /// Until one lands, a Lima session is trusted not to truncate its own pile, not
> /// prevented.
> --- `src/sandbox/lima.rs`

### Capability, grants and change admission

The sandbox capability surface is arbitrary shell execution and file exchange inside an already-provisioned environment. HTTP's current grant is tenant/backend identity, not a command allowlist or per-command human approval. Operator provisioning determines mounts, credentials, profiles and available faculty binaries. Native mode forwards the worker's catalogue without sandbox-tool-specific authorization; configured worker capabilities and downstream execution belong to the external implementation. Actual grants, egress and isolation on a deployed host were not supplied. The worker service's explicit environment and root/securelevel/RACCT checks establish launch conditions, not successful deployment. SRC-1: `src/mcp.rs`, `src/mcp_http.rs`, `src/mcp_http/workers.rs`, `deploy/freebsd/playground_faculties`.

Admission mechanisms include operator provisioning, source-fingerprint-based faculty bundle construction, operator-owned worker manifests/tokens and ordinary tenant shell/file mutations. These change available capabilities, production routing or workspace content without implying autonomous improvement. The provider supplies no inspected model-dependent proposer or evaluator; external callers could run such code inside the sandbox, but that is not evidence of a shipped Playground model loop. [RT-RTE-bundle-build](#rt-rte-bundle-build) and [RT-RTE-worker-forward](#rt-rte-worker-forward) describe installation and routing admission; memory revisions remain for the memory analyst. SRC-1: `src/main.rs`, `src/sandbox/faculties.rs`, `src/mcp_http/workers.rs`.

Added inspection under SRC-1 includes the HTTP authentication/dispatch and tenant-scope functions; provider open/start/close and file-tool implementations; job bounds, output paging, admission and shutdown; both backend execution functions; runner background capability checks; faculty fingerprint/cache/build code; gateway manifest, session and forwarding code; and the full native-worker rc service. All supply implementation evidence except attributed explanatory comments. The distributed-parametric implementation of any enclosing model or native worker remains outside the frozen source. No weight update, model pinning or mutable endpoint conclusion can be established for those external components. No distributed-parametric component was identified in the inspected provider paths.

## Shared records

### Components

#### RT-CMP-sandbox-provider
Label: SandboxProvider

Source-native provider registry and its backend/job references. Representational form: symbolic Rust structures and fixed dispatch rules. Storage substrate: process memory; backend persistent resources remain separate. It owns handle sharing, session lookup and lifecycle locking, not model reasoning. SRC-1: `src/mcp.rs`.

> pub struct SandboxProvider {
>     backend: Arc<dyn SandboxBackend>,
>     sessions: Mutex<HashMap<SessionId, SessionEntry>>,
> --- `src/mcp.rs`

#### RT-CMP-job-manager
Label: JobManager

Symbolic job state machine in Rust; process-memory maps, counters, mutexes and condition variables, with byte output rings. No disk job ledger is implemented by this component. SRC-1: `src/jobs.rs`.

> //! for its terminal state, then forgets it. The manager is in-memory because a
> //! daemon restart already loses the process handles required for cancellation;
> //! persistence and audit receipts are separate concerns.
> --- `src/jobs.rs`

### Operative objects

#### RT-OBJ-worker-manifest
Label: Worker manifest

Symbolic JSON consumed by fixed tenant/address/token rules, stored in an operator-supplied file and loaded into a process-memory mapping at startup. Token bytes come from separate files. Addresses must be distinct literal loopback sockets with nonzero ports; the mapping selects destinations, not a caller URL. SRC-1: `src/mcp_http/workers.rs`.

> struct WorkerSpec {
>     tenant: String,
>     address: SocketAddr,
>     token_file: PathBuf,
> }
> --- `src/mcp_http/workers.rs`

### Routes

#### RT-RTE-sandbox-exec
Label: Sandbox invocation and synchronous execution

Endpoints: caller → transport → McpServer → SandboxProvider → JobManager → backend shell → caller. Owner: HTTP code owns authentication/session admission; provider owns sandbox handles; job/backend code owns execution; caller owns the next requested action. Context is symbolic JSON/ExecRequest and tenant registry state. HTTP initialization and sandbox opening are distinct; stdio directly dispatches newline JSON without account authentication. Shell text is consumed as code, not interpreted by a model inside Playground. Effects reach sandbox files/processes and provisioned mounts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: synchronous exec waits for terminal state and returns rendered stdout/stderr, exit/error information as MCP content; opening returns a stable backend session ID.
- Later read-back: later calls can reach files/process state in the persistent sandbox; hidden synchronous job handles are forgotten after return.
- Delegated visibility: shell subprocesses receive the request and provisioning/login-profile environment; model-visible interpretation belongs to the external client.
- Selection predicate: HTTP bearer resolves tenant/backend, transport session must belong to tenant, named sandbox session must be registered and owned by it; stdio trusts operator-local callers.
- Invalidation or expiry: transport idle expiry requires reinitialization; close decrements provider refs and last close detaches; process restart loses registry/job state, not persistent sandbox storage.
- Activation or effect: dispatch invokes the backend shell; actual command execution and client response consumption remain unobserved.
- Evidence limits: source-level wiring, not an isolation proof or an observed successful invocation; direct dispatch and stdio bypass HTTP authority.

SRC-1: `src/main.rs`, `src/mcp_http.rs`, `src/mcp.rs`, `src/jobs.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

> pub fn exec(&self, params: ExecParams) -> Result<ExecResult> {
>     let id = self.start_job(&params)?;
>     self.jobs.wait_result_and_forget(&id)
> }
> --- `src/mcp.rs`

> if method == "tools/call" {
>     if let Err(response) = enforce_tenant_scope(&state, &token, &mut request) {
>         return response;
>     }
> }
> --- `src/mcp_http.rs`

#### RT-RTE-retained-jobs
Label: Retained job start poll and cancel

Endpoints: `job_exec` → shared execution kernel → backend, with `job_poll`/`job_cancel` returning to that same manager. Owner: manager admits and retains, backend observes cancellation, caller chooses poll/cancel and orders concurrent mutations. Job IDs and sequence cursors are symbolic; output bytes are retained separately and polling converts them with lossy UTF-8. A cancelling state is not terminal until backend return. Ordinary backend failure releases active capacity; loss of control on a capable backend shuts admission and notifies the transport fatal handler. SRC-1: `src/mcp.rs`, `src/jobs.rs`, `src/sandbox/runner.rs`, `src/sandbox/jail.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: start returns job ID/running/cursor; polls return bounded chunks, cursor, gap/dropped-byte metadata and optional terminal result; cancel requests cooperative cancellation.
- Later read-back: reconnecting clients poll accumulated output by retained job ID in the same daemon, including after terminal completion.
- Delegated visibility: backend output sink feeds the ring; HTTP authorizes job ownership before returning pages; no separate agent context is launched by the provider.
- Selection predicate: job ID and sequence cursor select retained chunks; retained start requires backend background support and active/retention capacity.
- Invalidation or expiry: 4 MiB/1024-chunk ring evicts oldest chunks; capacity eviction requires observed terminal final page; one-hour terminal TTL also expires unread outcomes; daemon restart loses all handles.
- Activation or effect: shell work and cancellation control are wired; returned output's influence on client behavior is unobserved.
- Evidence limits: root-local FreeBSD cancellation contract does not extend to Lima/SSH or worker-native work; cursor retries are safe read retries, not evidence that repeating a command is safe.

> pub fn job_exec(&self, params: ExecParams) -> Result<String> {
>     if !self.backend.supports_background_jobs() {
>         return Err(anyhow!(
>             "backend '{}' does not provide proven background-job cancellation; use synchronous exec",
>             self.backend.name()
>         ));
>     }
>     self.start_job(&params)
> }
> --- `src/mcp.rs`

> text: String::from_utf8_lossy(&chunk.bytes).into_owned(),
> --- `src/jobs.rs`

Working-context control is transport-side paging/output retention, not removal of turns from an enclosing model's window. Code bounds and drops tool output before later delivery; cursors can reload only surviving chunks. It does not isolate a model sub-agent frame or compact the host conversation. SRC-1: `src/jobs.rs`.

#### RT-RTE-file-exchange
Label: Clean-shell file read and replacement

Endpoints: MCP read/write arguments → quoted path/decoded payload → synchronous kernel → absolute guest utility → MIME-aware result. Owner: client proposes target/content, parser validates format/size, backend filesystem decides permission. Symbolic payload encoding carries arbitrary bytes; textual returned content may later be interpreted by the client model. No per-content human approval is imposed. Admission operates in open-request mode with no answer oracle. A write proposes replacement, is admitted on valid bounded payload and successful execution, and has no transaction or automatic rollback; callers must recover partial writes. Guidance is parser rules and clean-shell protocol construction, not a learned revision method. SRC-1: `src/mcp.rs`, `README.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: read returns text, image or MIME-labelled resource after bounded capture; write returns size/MIME/path metadata or tool error.
- Later read-back: written file bytes remain at the target for future read or exec calls, subject to filesystem lifetime and subsequent mutation.
- Delegated visibility: payload bytes reach cat stdin; file reads reach MCP client content, without login-profile stdout/stdin interference.
- Selection predicate: caller supplies open session, path and optional cwd; quoted path is a filesystem target, not a semantic retrieval query; payload must be one valid text/base64 value within 3 MiB.
- Invalidation or expiry: subsequent writes replace file content; failures can leave partial files; HTTP's default 1 MiB body limit may reject requests below the decoded tool ceiling.
- Activation or effect: write uses truncating redirection; read bypasses profile code and refuses oversized input rather than returning truncated success.
- Evidence limits: no transactional guarantee, semantic content check or client compliance evidence; arbitrary exec remains an alternate file mutation path.

> command: format!("file={quoted_path}; {SANDBOX_CAT} > \"$file\""),
> shell_mode: ExecShellMode::Clean,
> cwd: target.cwd,
> stdin: Some(bytes),
> --- `src/mcp.rs`

#### RT-RTE-tenant-provision
Label: Operator tenant provisioning and lifecycle

Endpoints: operator CLI → ProvisionSpec/backend provisioning → token-store mint/save → later transport admission. Operator supplies tenant, backend/topology and Lima host pile identity; software validates and performs mutations. Jail refuses caller-selected pile paths. The capability/environment proposal is admitted by backend checks, with failure able to reject; credential mint follows successful provisioning. A credential save failure need not undo an already-created sandbox. `user attach` only opens existing state. Destruction and token reset remain operator CLI operations, not model-facing tools. SRC-1: `src/main.rs`, `src/sandbox/mod.rs`, `README.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: create prints minted token once; attach prints session/persona; lifecycle commands return success or errors.
- Later read-back: persisted backend state and credential files support subsequent opens/authentication; pile/key identity is fixed by provisioning rather than reconnect arguments.
- Delegated visibility: shell environment exposes configured tenant persona and fixed guest pile/key destinations; operator state determines grants.
- Selection predicate: operator CLI arguments and backend-specific storage validation; later transport account resolves tenant/backend.
- Invalidation or expiry: explicit destruction removes sandbox resources and credentials according to the lifecycle API; token reset revokes/remints; optional OAuth-state revocation requires that configured path.
- Activation or effect: resource provisioning and credential admission are wired, not observed deployed authority.
- Evidence limits: actual human versus scripted operator invocation is unresolved; host privilege/isolation and external pile semantics are not proven.

Admission roles: operator proposes and can decline before invocation; software validates, rejects and executes. Mode: open administrative request, not an experiment or improvement curriculum. Answer oracle: inapplicable — no expected-answer evaluator participates. Guidance consists of CLI/backend topology and storage contracts; provisioned resources, profiles, signer/pile identity and credentials persist. Recovery includes explicit attach/retry or operator lifecycle operations; there is no general atomic transaction across provisioning and credential save. SRC-1: `src/main.rs`, `src/sandbox/mod.rs`.

> backend
>     .provision_sandbox(&spec)
>     .with_context(|| format!("provision sandbox for tenant '{}'", args.name))?;
>
> let mut store = mcp_http::TokenStore::load(&args.tokens)?;
> let token = store.mint(&args.name, backend_name);
> store.save(&args.tokens)?;
> --- `src/main.rs`

#### RT-RTE-bundle-build
Label: Faculty source bundle admission

Endpoints: configured faculty source tree → content fingerprint → cached cohort or throwaway Lima builder → host cache → later guest capability installation. Owner: operator chooses sources, code selects cache/build based on fingerprint and completion stamp. External source edits propose changed executables; compilation/staging success admits a bundle, not an empirical quality judgment. The fixed `SESSION_FACULTIES` list and lean features shape the proposal. There is no per-binary human review gate in this path. Failure rejects completion; stale revisions remain cached for operator recovery but automatic semantic rollback was not established. SRC-1: `src/sandbox/faculties.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bundle directory path or build error, with diagnostics.
- Later read-back: completion-stamped source-fingerprint cache is reused on subsequent preparation; binaries become guest shell capabilities.
- Delegated visibility: builder sees a read-only sibling workspace and writable scratch target; guest sessions receive the staged executable cohort, not a model-agent return summary.
- Selection predicate: current source/dependency fingerprint and existence of `.complete` select reuse versus build; explicit binary allowlist limits staged cohort.
- Invalidation or expiry: source fingerprint changes select another cache directory; stale bundles remain; no runtime model revision selector is involved.
- Activation or effect: capability installation is supported by source glue; actual installed versions and successful use remain unobserved.
- Evidence limits: external faculty contents/build dependencies are not frozen here; a completion stamp is not an answer oracle or benefit measurement.

Admission roles: operator/source maintainer proposes source edits; builder code decides successful completion; failures veto. Mode: source-driven build request. Answer oracle: inapplicable — compile/stage checks do not supply an expected behavior answer. Trigger is preparation against a missing fingerprint cache. What persists is executable bytes and completion stamp, not criticism of a formulated theory. SRC-1: `src/sandbox/faculties.rs`.

> build_bundle_in_lima(faculties_src, &bundle, builder_instance)
>     .with_context(|| format!("build faculties bundle into {}", bundle.display()))?;
> std::fs::write(&stamp, fingerprint.as_bytes()).context("write bundle completion stamp")?;
> Ok(bundle)
> --- `src/sandbox/faculties.rs`

#### RT-RTE-worker-forward
Label: Authenticated native-worker routing and supervision

Endpoints: authenticated HTTP → fixed worker mapping → upstream MCP process → byte-preserved JSON response → public caller. Native mode skips SandboxProvider/backend construction. Gateway owns routing, bounded exchange admission and public/upstream session translation; worker owns protocol/tool execution. The shipped FreeBSD rc service is a separate operator-controlled supervisor: it validates private config, reattaches the tenant jail, stages only its internal token and launches a fixed binary/environment under daemon with restart delay. SRC-1: `src/main.rs`, `src/mcp_http/workers.rs`, `deploy/freebsd/playground_faculties`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: worker JSON/status or accepted notification; failures report unavailable/configuration error or unknown execution outcome without retry.
- Later read-back: public session wrapper reaches the corresponding upstream session on later requests; native retained-state read-back semantics are uninspected because the worker implementation is external.
- Delegated visibility: worker receives original JSON body, selected media/protocol headers, translated upstream session and internal bearer, not public token/cookie or caller environment.
- Selection predicate: exact authenticated tenant selects operator mapping; non-initialize requests require its live wrapper; initialize reserves bounded session capacity; no missing-tenant fallback.
- Invalidation or expiry: DELETE closes upstream/public sessions; upstream 404 drops public wrapper; both sides' idle expiry matters; restart reloads manifest/tokens and loses wrappers; abandoned upstream work/session cleanup belongs to worker.
- Activation or effect: forwarding can invoke native side effects; terminating the HTTP exchange cannot promise cancellation of accepted native execution.
- Evidence limits: native tool catalogue, model versions/weight mutability, memory semantics and isolation internals are external; loopback alone is not tenant isolation; no hosted rollout was observed.

Routing admission: operator proposes manifest/bearer/binary configuration; load validation rejects duplicate or non-loopback mappings, and the service can reject unsafe configuration/host conditions. Restart admits changed gateway mappings/internal tokens; restart/reconfiguration is operator recovery, not automatic rollback of tool effects. Mode: open client requests under fixed provisioning. Answer oracle: inapplicable — gateway does not assess native answers. Supervision restarts machinery after exit, without evidence-based revision of its implementation. SRC-1: `src/mcp_http/workers.rs`, `deploy/freebsd/playground_faculties`.

> .header(header::AUTHORIZATION, self.authorization.clone())
> .header(header::CONNECTION, "close");
> --- `src/mcp_http/workers.rs`

> "worker response timed out; execution outcome is unknown; request was not retried",
> --- `src/mcp_http/workers.rs`

> PILE=/pile/self.pile TRIBLESPACE_KEY=/pile/self.key PERSONA="$worker_persona" \
> /opt/faculties/faculties mcp --pile /pile/self.pile --key /pile/self.key \
> --http-listen "$worker_address" --http-token-file /var/run/faculties-mcp/token
> --- `deploy/freebsd/playground_faculties`

### Claims

#### RT-CLM-persistent-sandbox
Label: Persistent sandbox contract

Claimed operation: releasing an MCP handle preserves the tenant workspace; permanent destruction is operator-only. Source claim agrees with inspected detach functions but is not an observed persistence test. The broader lifecycle comment in `run_mcp` saying a disconnect cannot leak a VM/jail must be read as releasing provider-owned handles, not deleting persistent sandboxes or guaranteeing every host cleanup succeeded. SRC-1: `README.md`, `src/main.rs`, `src/mcp.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

> - `close_session` — release this handle; the persistent sandbox remains.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-shell-command
Label: Caller shell command authority

Consumer: backend-selected `/bin/sh` in tenant sandbox. Channel: symbolic command string plus stdin/cwd and login profile. Force: executable instruction under guest privileges, not advisory prose; profile code can modify ordinary command environment but file tools use clean mode. Horizon: current command and any persistent filesystem/process effects later calls reach. Current HTTP grant is tenant identity; it imposes no semantic command approval. SRC-1: `src/mcp.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

> let argv = [
>     "sudo", "-n", "timeout", "-k", "5", &secs, "jexec", jail, "/bin/sh", shell_flag,
>     &script,
> ];
> --- `src/sandbox/jail.rs`

#### RT-BAP-worker-mapping
Label: Operator mapping authority over destination

Consumer: gateway worker lookup/forwarder. Channel: loaded symbolic manifest and private internal bearer. Force: fixed destination and authentication for every admitted public request; no client-selected URL or fallback. Horizon: gateway process lifetime until restart; downstream native effects have separate external lifetimes. SRC-1: `src/mcp_http/workers.rs`.

> self.workers.get(&token.tenant).ok_or_else(|| {
> --- `src/mcp_http/workers.rs`

## Annotations

none
