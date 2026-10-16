---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Decapod runtime baseline: ephemeral CLI/RPC governance, agent-owned work, context delivery, custody and exact-candidate publication at the frozen repository revision."
run-id: AAS-2026-10-14-decapod-c44705119841-01
reviewed-boundary: "067b8f55071e13dd103779998168b4c9ffd31a79"
---

# Decapod runtime report

## Runtime account

### Work and ordinary invocation

Decapod supplies a control plane to a coding agent, not the agent's inference/tool loop. The human supplies intent; the host agent interprets it, edits code and authored specifications, and chooses the next invocation. Decapod returns context, coordination state, prescribed next actions, blockers and validation/publication results. It owns the implemented checks on its surfaces, not arbitrary commands issued by the host. This distinction bounds every guarantee below (SRC-1, `AGENTS.md`, `docs/architecture/governed-execution.md`, `src/decapod/lib.rs`).

> Agents act. Decapod governs accepted work. One task may span many ephemeral Decapod invocations; durable state lives in the repository.
> --- `AGENTS.md`

The ordinary source-prescribed task begins with prompt evaluation and orientation, acquires a session, initializes the agent, creates/claims a todo, obtains task orientation, ensures an isolated workspace, changes directory to that workspace, and resolves constitution/context. The agent then implements the change, updates authored living specs and governance evidence, checkpoints and commits it, validates, repairs failures, revalidates and publishes. These are multiple independent processes owned by the host, not an internal scheduler advancing an autonomous graph. The ordinary single invocation traced here is `decapod rpc --op context.resolve`: CLI parse → project/governance-root resolution → applicable bootstrap/storage handling → RPC request construction → route-specific session/worktree/awareness checks → bindings and scoped selection → local specs and authority loading → JSON capsule and allowed-operation suggestions → best-effort trace append → process return. The returned suggestions do not execute the next step (SRC-1, `AGENTS.md`, `src/decapod/lib.rs`, `src/decapod/core/docs.rs`; [RT-RTE-context-resolve](#rt-rte-context-resolve)).

The principal is the calling host process. `DECAPOD_AGENT_ID`, falling back to `unknown`, identifies the agent; request IDs correlate RPC and trace events; session tokens identify a local custody epoch; todo IDs and branch names bind work; commit/base IDs bind readiness and publication. They serve different purposes. A local agent identifier is not demonstrated human authentication. Repository discovery also distinguishes workspace code/specs from shared governance data. Session records prefer machine-local storage, with legacy/workspace fallback; project data uses the governance root's `.decapod/data` (SRC-1, `src/decapod/lib.rs`).

### Shipped routes and material control differences

The executable enters the library `run`, whose Clap dispatch includes CLI groups and structured RPC. Help/bootstrap paths are deliberately usable without project storage. RPC reads one JSON request from stdin or constructs one from flags and returns an envelope. The opt-in HTTP handler spawns the same executable with `rpc --stdin`, preserving that semantic path; it is not an independent model/tool executor. The boundary already retains the source's explicit distinction from MCP. Same-repository drivers and library publication calls remain included (SRC-1, `src/main.rs`, `src/decapod/lib.rs`; [boundary](boundary.md#boundary-and-evidence)).

Three forcing comparisons change the strongest plausible reading of the governance claim:

1. **CLI versus RPC mutation/session paths.** Local CLI operations generally call `ensure_session_valid`, but that function auto-acquires on missing, expired, wrong-backend, unknown-agent, missing-password or wrong-password cases. RPC explicitly exempts `store.upsert`, `workspace.ensure`, `context.resolve` and others from its session check; `store.upsert` instead requires recorded constitutional awareness. Cloud todo commands bypass the local SQLite agent-session path and rely on Propodus/JWT authentication. Thus the normative “mutations require active session” is not a uniform external approval barrier (SRC-1, `src/decapod/lib.rs`; [RT-RTE-session-custody](#rt-rte-session-custody), [RT-CLM-session-auth](#rt-clm-session-auth)).
2. **Preparation versus readiness versus publication.** Local prerequisite success is not permission to publish. `validate` can heal generated surfaces and retry prerequisite validation twice; full workbranch scope subsequently runs current-candidate readiness. CI-local scope explicitly reports `publication_ready=false` without nested remote preflight. Publication rechecks the committed bundle, current governance, exact target and remote head/base, rather than trusting a push exit or earlier green receipt. Non-GitHub remotes can produce verified branch publication without a verified PR (SRC-1, `src/decapod/lib.rs`, `src/decapod/core/workspace.rs`, `src/decapod/core/workspace_publication.rs`; [RT-RTE-validate-candidate](#rt-rte-validate-candidate), [RT-RTE-workspace-publish](#rt-rte-workspace-publish)).
3. **Governed work versus direct host access.** Worktree checks have operation allowlists and an explicit `DECAPOD_VALIDATE_SKIP_GIT_GATES` escape. Workspace creation defaults to no container; optional containers prepare a filesystem/data-store execution environment, not a fresh model context. Direct shell/Git commands, host callbacks, provider-native tools and arbitrary host extensions do not pass through Decapod merely because an entrypoint asks the agent to obey it. This source expressly disclaims control of direct Git commands. The inspected publication function itself uses bounded `Command::new("git")`; external-action authorization is not a universal interception layer (SRC-1, `src/decapod/lib.rs`, `src/decapod/core/workspace.rs`, `src/decapod/core/external_action.rs`, `docs/architecture/governed-execution.md`; [RT-BAP-readiness-gates](#rt-bap-readiness-gates)).

> Decapod can return that instruction, but it cannot
> control Git commands issued directly by an agent or its harness.
> --- `docs/architecture/governed-execution.md`

These are static forcing cases, not observed adversarial runs. No supplied target execution, service trace or experiment establishes activation, success rates or benefit. Library calls can bypass CLI-only checks; the inspected library publication function still performs its own publication checks. Group-broker routing coordinates selected local mutators, can finish todo claim responses and can require routing in strict mode; cloud todo is a separate branch. Full broker internals, every plugin mutation, direct library consumer and cloud backend are not exhaustively traced, so no system-wide collision-proof or authentication claim follows (SRC-1, `src/decapod/lib.rs`, `src/decapod/core/workspace.rs`).

### Guarantee owners, coverage and strength

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths/external contract | Separate conclusions |
| --- | --- | --- | --- | --- |
| Stop on unsafe prompt markers | `agent_eval` evaluates supplied text and returns block/error; host must invoke it and stop | Policy for host compliance; invariant for matched-marker classification in the evaluator | Other commands do not automatically evaluate the original host prompt; substring detection is not general prompt-safety proof | implementation conclusion status: wired; operation conclusion status: uninspected |
| Isolated governed execution | CLI/RPC worktree guards; workspace ensures claimed work and rejects protected branches | Policy on covered calls; Git worktree isolation is not host sandboxing | Exempt operations, gate-skip environment, direct shell and optional container; filesystem/Git/container behavior external | implementation conclusion status: wired; operation conclusion status: uninspected |
| Bounded validation body | Parent spawns, supervises and reaps/kills project-check child; readiness has budgets and cancellation | Invariant of inspected supervised path, not demonstrated wall-clock reliability of every command | Standalone tools, update installer and arbitrary host subprocesses have different supervision; OS process/cancellation contract required | implementation conclusion status: wired; operation conclusion status: uninspected |
| Exact-candidate readiness | Validation controller binds clean tracked inputs, accepted base ancestry, profile, source inventory and executor closure | Protocol for supported profiles; unsupported controller contracts remain blockers | Remote Buildkite/snapshot alternatives need provider proof; CI-local/project-check outputs cannot substitute | implementation conclusion status: wired; operation conclusion status: uninspected |
| Verified publication rather than inferred success | Workspace publisher plus remote/PR verification module | Protocol for Decapod publication; normal push, immutable IDs, remote re-read and PR verification | Direct Git/gh outside path; network/backend correctness, authorization and Git object identity required; non-GitHub PR unavailable | implementation conclusion status: wired; operation conclusion status: uninspected |

The evidence and qualifications for these rows are retained in [RT-RTE-prompt-eval](#rt-rte-prompt-eval), [RT-RTE-workspace-ensure](#rt-rte-workspace-ensure), [RT-RTE-validate-candidate](#rt-rte-validate-candidate) and [RT-RTE-workspace-publish](#rt-rte-workspace-publish). None establishes a deployment guarantee for an unspecified host.

Capability surface, grants and deployment isolation must be separated. `ExternalCapability` names VCS read/write, proof and verification execution, inspection and sealed preflight actions. Its default proof-exec binary list includes cargo, decapod, Git, bash and sh; project `EXTERNAL_ACTIONS.json` can replace rules, and failed/missing configuration falls back to defaults. Ordinary write-like VCS authorization can require policy approval, with scoped exceptions; current readiness passes an authorization callback for probes, target reads and source checks. The actual deployed grant set, host shell privileges and container settings are unobserved. A binary allowlist containing shells is not a command-content sandbox, and this helper covers only callers using it (SRC-1, `src/decapod/core/external_action.rs`, `src/decapod/lib.rs`).

> // Only write-like external capabilities require approval.
> if capability != ExternalCapability::VcsWrite {
>     return Ok(());
> }
> --- `src/decapod/core/external_action.rs`

### Context, model use and change admission

Context resolution is a working-context supply mechanism: the host asks; code selects embedded/merged doctrine and authored specs; the host receives by-value text in JSON. It neither removes old conversation turns nor isolates model inference into sub-agent frames. Operation/path/tag boosts and lexical matching rank scoped fragments, but the RPC handler merges explicit and scoped fragments, sorts by reference, deduplicates and truncates the final `fragments` list. A separate `scoped_fragments` result retains the ranked scoped selection. Local specs and resolved authority travel in additional fields, so the fragment limit is not a total context-token bound. The host still decides what to insert into its model window. Workspace isolation concerns files and custody, not conversation reset; source doctrine says the agent's request context remains authoritative across it (SRC-1, `src/decapod/core/docs.rs`, `src/decapod/lib.rs`, `AGENTS.md`; [RT-BAP-context-delivery](#rt-bap-context-delivery)).

Decapod's optional Jev adapter submits a narrowed governance/trajectory context for a probabilistic alignment observation. Its configured model alias is `jev-latest`; the response reports a model string. It does not execute tools or decide policy. The adapter checks response type and finite probability in [0,1], and failures become explicit no-observation results. Parameter updating and service internals are inaccessible; no training operation is present in the inspected adapter, and the mutable alias is not an immutable model pin ([RT-CMP-jev](#rt-cmp-jev), [RT-RTE-assurance-observe](#rt-rte-assurance-observe)). External host model versions and context policies are not frozen by this repository. Consequently no account of the host's distributed parameters or learning follows from the CLI.

Authored code/spec changes are proposed by the host agent under human intent; Decapod requires visible semantic specs, governance/checkpoints, configured proof and supported controller contracts before its publication route accepts them. Generated entrypoint/Docker/spec projections can be refreshed or healed by software; they are not agent-authored semantic understanding. Production-machinery changes are themselves candidates: the readiness implementation captures the accepted target's executor, checks its compiled closure, and treats reviewed carriers as controller authority. Candidate source helpers changing does not license arbitrary new workflow/carrier bytes. The narrower inspection here establishes those admission checks, not every build/release effect or remote driver's correctness (SRC-1, `src/decapod/core/readiness_profile.rs`, `src/decapod/core/validation_runtime.rs`, `src/decapod/lib.rs`; [RT-RTE-validate-candidate](#rt-rte-validate-candidate)).

A distinct route can replace the installed CLI on explicit session acquire: check crates.io version, best-effort backup, run `cargo install decapod`, request a restart. That is version-driven product admission, not an evidence-directed self-improvement result. It does not use the repository's exact-candidate readiness as the install gate ([RT-RTE-release-update](#rt-rte-release-update)). Knowledge admission, revision and expiry are left to the memory analyst. No theory-builder, learning or exercised self-improvement conclusion is inferred from preserving trajectories or requiring prose updates.

### Added source coverage and remaining limits

All added inspection belongs to SRC-1 at the frozen commit and supplies implementation or doctrine/design, never observed-run evidence. Beyond boundary excerpts, this member inspected `src/decapod/lib.rs` bootstrap, dispatch, session/worktree/awareness guards, orientation gates, context resolution, RPC/HTTP return, supervised validation, readiness dispatch and installer paths; `src/decapod/core/docs.rs` scoped selection; `src/decapod/core/workspace.rs` custody/creation and publication; `src/decapod/core/workspace_publication.rs` immutable remote verification; `src/decapod/core/agent_eval.rs` prompt evaluator; `src/decapod/core/assurance.rs` provider caller; `src/decapod/core/decision_provider.rs` full adapter; `src/decapod/core/external_action.rs` default permissions/authorization; and bounded accepted-executor/input-discovery passages in `src/decapod/core/readiness_profile.rs` and `src/decapod/core/validation_runtime.rs`. `AGENTS.md` and `docs/architecture/governed-execution.md` were read as source doctrine, not analyst instructions.

Unresolved included material comprises complete broker arbitration, policy configuration/approval provenance, every library/plugin mutator, full HTTP transport authentication, complete remote/snapshot recovery state machines, container mount/privilege envelope, all CI/release drivers and dependency internals. These are available-but-not-exhaustively-inspected paths or external dependencies, not evidenced absences. They prevent universal enforcement, remote reliability, deployment-isolation and exhaustive production-machinery conclusions, without negating the inspected wiring. No target tests were run.

## Shared records

### Components

#### RT-CMP-jev
Label: Jev decision provider

Source-native identity: optional `DecisionProviderKind::Jev`, `JevDecisionProvider` and remote `jev-latest`. Adapter/control structures are symbolic Rust/JSON; the external probabilistic model is distributed-parametric. Adapter lives in the shipped binary; parameters reside at the external service, not in the checkout. No parameter-write interface is implemented in this adapter; actual service-side parameter changes during operation are uninspected. Exact parameter version is not pinned. A mutable alias can resolve to another model; the response's model string is recorded but is not a weights digest. Evidence: SRC-1, `src/decapod/core/decision_provider.rs`; consumer in `src/decapod/core/assurance.rs`.

> const JEV_API_URL: &str = "https://api.typesafe.ai/v1/systemone";
> const JEV_MODEL: &str = "jev-latest";
> --- `src/decapod/core/decision_provider.rs`

### Operative objects

#### RT-OBJ-agent-session
Label: Agent session record

Source-native identity: `AgentSessionRecord`, with agent ID, token, password hash and issued/expiry epochs. Symbolic JSON on filesystem, preferred machine-local session directories and legacy project fallback. It supplies custody/check state, not a natural-language behavioral instruction. Backend-prefixed tokens and configurable bounded TTL distinguish local/cloud session epochs. Evidence: SRC-1, `src/decapod/lib.rs`.

> struct AgentSessionRecord {
>     agent_id: String,
>     token: String,
>     password_hash: String,
>     issued_at_epoch_secs: u64,
>     expires_at_epoch_secs: u64,
> }
> --- `src/decapod/lib.rs`

#### RT-OBJ-accepted-executor
Label: Accepted executor

Source-native identity: `AcceptedExecutor`, captured from accepted-base Git objects. Symbolic revision/tree/profile-digest/source-inventory structure, in controller memory and serialized evidence; its backing authority is immutable Git objects plus compiled expected bytes. It is not deserializable as candidate-supplied authority. Different from the changed project source and any externally executed proof. Evidence: SRC-1, `src/decapod/core/readiness_profile.rs`, `src/decapod/core/validation_runtime.rs`.

> /// Captured only from the accepted target's immutable Git objects. This type is
> /// deliberately not Deserialize: a candidate or receipt cannot select authority.
> --- `src/decapod/core/readiness_profile.rs`

> if files.files != expected {
>     return Err(PlanningFailure::ControllerContractUnsupported(
>         "accepted executor closure".into(),
>     ));
> }
> --- `src/decapod/core/readiness_profile.rs`

### Routes

#### RT-RTE-prompt-eval
Label: Incoming prompt evaluation

Endpoints/progression: host supplies complete prompt through flag/stdin → whitespace normalization and lowercase substring-marker scan → SHA-256, findings, allow/block and prescribed action → CLI JSON/text or error. Owner: evaluator code classifies; host chooses whether to call it and honor the answer. Natural-language prompt/action and symbolic result remain distinct. No model is invoked. Operating mode: open incoming prompts, fixed marker policy, no expected-answer oracle. Doctrine requires human review on block, but the evaluator cannot veto later host tool use. Evidence: SRC-1, `AGENTS.md`, `src/decapod/core/agent_eval.rs`, bootstrap dispatch in `src/decapod/lib.rs`.

- Immediate return: Status, prompt digest/byte count, marker findings and action; blocked CLI returns an error.
- Later read-back: inapplicable — this inspected evaluator path does not persist the result for another invocation.
- Delegated visibility: Host receives the result; no spawned reasoning worker.
- Selection predicate: Any configured marker needle contained in normalized prompt yields a finding and block.
- Invalidation or expiry: Each new prompt requires reevaluation under source doctrine; a prior allow is not a universal safety verdict.
- Activation or effect: Evaluator returns a block error; actual host stopping remains unobserved.
- Evidence limits: Fixed-marker implementation does not prove general injection detection or automatic invocation by hosts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let status = if findings.is_empty() {
>     EvalStatus::Allow
> } else {
>     EvalStatus::Block
> };
> --- `src/decapod/core/agent_eval.rs`

#### RT-RTE-session-custody
Label: Session validation and reacquisition

Endpoints/progression: applicable CLI/RPC call → agent ID/session/backend/expiry/password checks → retain session or auto-acquire → dispatch. Owner: local code; no per-call human approval is established. Symbolic session writes are software-admitted coordination state, not revised knowledge. Missing/bad credentials generally trigger reacquisition rather than permanent denial. Cloud todo uses a different authenticated transport. Evidence: SRC-1, `src/decapod/lib.rs`; [RT-OBJ-agent-session](#rt-obj-agent-session).

- Immediate return: Continue dispatch, or filesystem/credential-generation error; auto-acquire logs a notice.
- Later read-back: Subsequent commands reload the session record for the agent/project and inspect expiry/backend/password state.
- Delegated visibility: Process-local password cache is not a model-context handoff; session files are accessible to the owning environment.
- Selection predicate: Current project, `DECAPOD_AGENT_ID` or `unknown`, configured backend and TTL.
- Invalidation or expiry: Expiry/backend mismatch removes records; stale assignments are cleaned; missing/invalid password can reacquire.
- Activation or effect: Session files and process-local password are written; this does not authenticate human consent.
- Evidence limits: RPC bypass list and cloud path prevent a universal active-local-session gate; deployed storage access controls remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Password invalid - auto-acquire new session (entrypoint funnel)
> return auto_acquire_session(&project_root, &agent_id);
> --- `src/decapod/lib.rs`

#### RT-RTE-workspace-ensure
Label: Claimed workspace preparation

Endpoints/progression: host calls ensure → find main repository and storage preflight/schema reconciliation → ensure assigned open tasks → reject scope/custody conflicts → reuse valid worktree or create task-scoped branch/worktree → initialize governance and release surfaces → optionally build container and return launch guidance. Code owns admission of custody/workspace changes; host owns intent, subsequent directory/container entry and work. Existing external-task integration may create/claim a coordination todo; branching is not always a manually preclaimed sequence. Computational admission can reject conflicting ownership; no per-content human approval is shown. Recovery is actionable same-task retry, not deleting task history. Evidence: SRC-1, `src/decapod/core/workspace.rs`, `src/decapod/lib.rs`.

- Immediate return: Workspace status/path, blockers/allowed actions and optional container launch guidance.
- Later read-back: Task assignments, registered workspaces and governance survive processes and are consulted on later ensure/status/readiness calls.
- Delegated visibility: Filesystem workspace/container receives prepared state; host conversation is not copied into a separate model frame by this mechanism.
- Selection predicate: Agent assignments, task IDs/hashes, requested branch/base and current workspace status; ambiguity and conflicting claim block.
- Invalidation or expiry: Session expiry can release stale assignments; workspace reuse requires valid state; full lifecycle cleanup/recovery is not exhaustively inspected.
- Activation or effect: Git branch/worktree and governance/projections are created or refreshed; container preparation does not itself prove the agent entered it.
- Evidence limits: Optional container privilege/mount policy and every custody path remain uninspected; worktree existence is not host sandbox enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> WorkspaceConfig {
>     branch: Some(format!(
>         "agent/{}/{}-{}",
>         sanitize_agent_id(agent_id),
>         generated_branch_scope,
>         ts
>     )),
>     use_container: false,
>     base_image: None,
>     base_branch: None,
> }
> --- `src/decapod/core/workspace.rs`

#### RT-RTE-context-resolve
Label: Scoped context resolution

Endpoints/progression: RPC request → operation/path/tag bindings → scoped lexical ranking of embedded/merged docs → merged reference sorting/dedup/truncation → load local specs/authority → mark awareness and return JSON/context capsule. Owner: code selects text; host selects next step and actual inference context. Natural-language doctrine/spec text is packaged in symbolic references, hashes and structured fields. Working-context control is on-demand supply, not eviction or sub-agent isolation. Evidence: SRC-1, `src/decapod/lib.rs`, `src/decapod/core/docs.rs`.

- Immediate return: Fragments, separately scoped fragments, authored local-spec fields, resolved authority, mandates and allowed-operation suggestions.
- Later read-back: Authored specs and project authority can be reloaded in later calls; retained knowledge query is a separately suggested operation, not automatically performed here.
- Delegated visibility: Calling host receives JSON; insertion into its own or delegated model context is uninspected.
- Selection predicate: Caller query/op/touched paths/intent tags; deterministic boosts and lexical matches, then final reference ordering/dedup and configurable limit.
- Invalidation or expiry: Recomputed from current repository state per request; awareness is session-sensitive; no TTL for delivered host text is established.
- Activation or effect: Awareness receipt is marked; text delivery is implemented, behavioral compliance is not observed.
- Evidence limits: Fragment truncation is not total context bounding; separate specs and scoped list can contain additional material; host context management is external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fragments.extend(scoped_fragments.clone());
> fragments.sort_by(|a, b| a.r#ref.cmp(&b.r#ref));
> fragments.dedup_by(|a, b| a.r#ref == b.r#ref);
> fragments.truncate(limit.max(1));
> --- `src/decapod/lib.rs`

#### RT-RTE-validate-candidate
Label: Current candidate validation and readiness

Endpoints/progression: CLI/RPC validation or publication readiness → scope/config/workspace checks → heal supported generated surfaces → supervised project-check child and bounded retries → full-scope exact-candidate readiness or explicit partial-scope result → blockers/report. Candidate changes to code, authored specs and production machinery originate with host agents/humans; generated projection changes can originate with code. Controller owns check graph/admission; user intent and semantic review remain external judgment. A required profile, clean tracked input inventory, current accepted-base ancestry and supported executor contract constrain readiness. Runtime chooses native versus configured Buildkite/snapshot proof rather than letting another provider's green result substitute. [RT-OBJ-accepted-executor](#rt-obj-accepted-executor) supplies distinct trusted executor identity. Evidence: SRC-1, `src/decapod/lib.rs`, `src/decapod/core/validation_runtime.rs`, `src/decapod/core/readiness_profile.rs`.

Admission account: trigger is requested validation/publication of a changed candidate; proposed change is repository code/spec/config/workflow/toolchain content. Host proposes and repairs; code vetoes incomplete prerequisites/proof or unsupported contracts. Human meaningful-outcome judgment is prescribed, not demonstrated per-content approval. Guidance is constitution/plan/proof obligations plus failure/root-cause instructions. Supported healing updates generated projections, not semantic living-spec authorship. Git history, authored specs, governance and eligible validation receipts persist. Recovery is repair/checkpoint/commit/revalidate the exact candidate, or preserve access/unsupported-contract blockers; no automatic semantic rollback is established.

Operating mode: open development requests evaluated against a bounded configured proof graph. Answer-oracle role: configured test assertions and expected check/protocol outcomes, not Jev alignment probability. This inspection does not establish correctness/completeness of all project tests or a held-out task oracle. Content-directed theory criticism and improved future capacity are not established by a failing check alone.

- Immediate return: JSON/text validation scope, publication-ready flag, report, healing actions, readiness blockers and guidance; failures return nonzero.
- Later read-back: Successful prerequisite validation can record governance proof/receipt; later publication verifies current artifact/revision binding and still evaluates full readiness.
- Delegated visibility: Supervised subprocess receives explicit roots/store/environment; configured remote proof has its own provider handoff, not a delegated model reasoning frame.
- Selection predicate: Validation scope, required profile, current HEAD/accepted base, complete changed-path/source inventory, configured provider and applicability facts.
- Invalidation or expiry: Material/history/spec/evaluator/accepted-target changes require fresh readiness; current input binding and ancestry checks prevent relying solely on stale receipt labels.
- Activation or effect: Generated surfaces may heal; controller executes or requests configured checks and blocks readiness when proof is incomplete; exercised production benefit remains unobserved.
- Evidence limits: Full provider state machines and remote execution internals are not traced; static wiring does not establish termination reliability or test adequacy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> /// the process alive (#1280, #1281). The parent owns the timeout and always
> /// reaps or kills the child before returning.
> --- `src/decapod/lib.rs`

> Validation scope: ci_local; publication_ready=false. Remote preflight is not run inside CI.
> --- `src/decapod/lib.rs`

> .map_err(|_| {
>     invalid("ACCEPTED_BASE_NOT_ANCESTOR: incorporate the current accepted base before proof")
> })?;
> --- `src/decapod/core/validation_runtime.rs`

#### RT-RTE-workspace-publish
Label: Verified workspace publication

Endpoints/progression: CLI/RPC or library publisher → unprotected worktree and governance/eval binding checks → resolve actual remote → optionally stage/commit with checkpoint check → required artifacts/material specs/reviews → committed bundle and merge checks → exact current readiness → normal push → read exact remote immutable head/base and recheck bundle/specs/checkpoints → create/reuse/verify GitHub PR → recheck remote unchanged → result. Owner: software vetoes its publication transition; host supplies candidate/title/description and remediation; Git/remote/gh execute external effects. Direct host push/PR commands remain alternate ungoverned routes. Evidence: SRC-1, `src/decapod/core/workspace.rs`, `src/decapod/core/workspace_publication.rs`.

Admission account: trigger is publish request; admitted change is the current repository candidate and governed publication state. Agent/human proposes semantic content; software checks proof/material requirements, not semantic truth. Human per-content approval is not universally demonstrated. Rejection leaves actionable blockers; a failed acknowledgement may leave the branch already pushed. Recovery preserves branch, reads remote, reconciles divergence, revalidates and retries; it reuses matching PRs and never force-pushes on this route. Git history, committed governance/specs and remote branch/PR persist. Operating mode: open workbranch delivery through exact-candidate proof. Answer oracle: expected remote IDs, verified PR metadata and configured readiness checks, not agent completion assertion.

- Immediate return: Branch, commit hash, redacted remote, remote-verified and PR-verified flags, optional PR URL and warnings; explicit incomplete-publication errors after push.
- Later read-back: Remote head/base and PR are read back during verification and retries; future consumers see published Git/spec/governance state.
- Delegated visibility: Git network endpoint and GitHub CLI/API receive publication inputs; no spawned model worker.
- Selection predicate: Current branch/HEAD, resolved network push destination, accepted base and matching PR head/base/repository.
- Invalidation or expiry: Changed worktree/index or remote head/base races block; historical proof cannot replace current exact-candidate requirements.
- Activation or effect: Normal push changes remote branch and optional PR; non-GitHub branch success is explicitly not verified PR readiness.
- Evidence limits: No network execution supplied; protocol relies on Git/server/GitHub identity and access contracts; cannot control host-issued alternative publication commands.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Read the exact push destination, not a possibly different fetch URL or
> // stale remote-tracking ref. A successful push alone is not publication proof.
> --- `src/decapod/core/workspace.rs`

#### RT-RTE-assurance-observe
Label: Optional intent alignment observation

Endpoints/progression: assurance request → plan/obligations/workspace and selected durable governance assembled → configured provider → Jev HTTP request → response validation → observation or no-observation → append Jev history and return advisory. Owner: assurance code constructs context; [RT-CMP-jev](#rt-cmp-jev) proposes a probability; Decapod retains policy/interlock authority. Provider receives state-labelled strings and explicit untrusted-evidence instructions, not raw operation parameters. Natural-language criteria and numerical result are distinct. Evidence: SRC-1, `src/decapod/core/assurance.rs`, `src/decapod/core/decision_provider.rs`.

Operating mode: open task alignment assessment, not bounded training/curriculum. No answer oracle is supplied: true/false criteria tell the provider what to assess, without an independently known answer. Model observation cannot approve work or resolve an interlock. Missing intent/config/trajectory, malformed response, unavailable transport and persistence failure remain explicit no-observation reasons. Host/human can choose subsequent action; the inspected caller does not admit product changes based on probability alone.

- Immediate return: Advisory contains typed probability/model/usage or no-observation; attestation is returned by assurance.
- Later read-back: Jev result is appended under trajectory/run identity; its complete downstream memory use is left to the memory analyst.
- Delegated visibility: Remote provider receives narrowed intent/trajectory/governance; internal provider context and retention are opaque.
- Selection predicate: Configured Jev versus default none, usable intent/API key/trajectory and expected answer type/probability range.
- Invalidation or expiry: Fresh assurance call creates a new assessment; immutable model pin/remote retention policy is not established.
- Activation or effect: Advisory/history are produced, not policy approval or proof; behavioral adoption by host is unobserved.
- Evidence limits: Instructions to treat repository strings as untrusted do not prove model compliance; remote internals and parameter mutation are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> //! A decision provider may inform Decapod's governance context, but it never
> //! owns policy. In particular, an observation is not an approval, an
> //! interlock resolution, or proof of completion.
> --- `src/decapod/core/decision_provider.rs`

#### RT-RTE-release-update
Label: Session-triggered CLI release update

Endpoints/progression: explicit session acquire → check curl availability/crates.io version → numerical version comparison → best-effort state backup/cargo availability → cargo install → restart/config-field notice. Owner: software selects newer release; registry/package maintainer supplies artifact; operator/host starts acquisition, not per-release content approval. Symbolic version metadata selects executable replacement. Evidence: SRC-1, `src/decapod/lib.rs`.

Admission account: trigger is acquire plus reported newer version; proposed change is installed Decapod executable. Install exit gates success; missing tools/network/errors generally skip update. No reviewed-candidate readiness or semantic comparison is wired at this installer seam. Backup is best effort; exact restore/rollback success is uninspected. Guidance is update/restart and check new config fields. Operating mode: version-driven maintenance, no answer oracle or task-outcome experiment. Installed artifact persists for subsequent processes; this does not demonstrate evidence-responsive self-improvement or beneficial release effects.

- Immediate return: Update/skipped status and notice to restart acquire; session command can continue.
- Later read-back: Future process invocation can load the installed newer binary; actual restart/version change is unobserved.
- Delegated visibility: Curl reads registry metadata and Cargo installs package; dependency/build behavior is external.
- Selection predicate: Reported version numerically greater than compiled version, required tools available, install success.
- Invalidation or expiry: Next explicit acquire can check again; no immutable artifact digest is established in this seam.
- Activation or effect: Cargo installation can replace executable; current process continues its loaded code.
- Evidence limits: Registry/Cargo trust, rollback and installation are not executed; this installer uses ordinary process output rather than the bounded validation child contract.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let output = std::process::Command::new("cargo")
>     .args(["install", "decapod"])
>     .output()
> --- `src/decapod/lib.rs`

### Claims

#### RT-CLM-session-auth
Label: Normative mutation session requirement

Claimed operation: shipped universal agent contract names an active session as a mutation invariant. Source: SRC-1, `AGENTS.md`. Implementation scope is qualified by auto-acquisition, RPC bypass and cloud authentication in [RT-RTE-session-custody](#rt-rte-session-custody); the claim is not evidence of a universal permission gate or human approval.

> - **INV-SESSION-AUTH**: Mutations require active session.
> --- `AGENTS.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-delivery
Label: Context delivery to host agent

Consumer: external coding agent/model. Channel: RPC JSON capsule, constitution/docs output, generated host entrypoint and source-prescribed early consultation. Force: natural-language guidance requiring interpretation and host compliance; symbolic awareness checks record selected resolution events, not semantic obedience. Horizon: current invocation and later repeated retrieval from repository/embedded state. Evidence: SRC-1, `AGENTS.md`, `src/decapod/lib.rs`; [RT-RTE-context-resolve](#rt-rte-context-resolve). No observed activation supplied.

> - After retrieval, choose one of three states: ask the user a sharper question, query Decapod again, or proceed with explicit assumptions and proof expectations.
> --- `AGENTS.md`

#### RT-BAP-readiness-gates
Label: Readiness control of governed publication

Consumer: Decapod publisher and validation controller. Channel: symbolic candidate/config/Git/proof inputs and control-flow checks. Force: executable rejection of the covered transition; agent/human interprets remediation text. Horizon: current candidate plus retained commits/governance and subsequent retries. Not authority over arbitrary host commands. Evidence: SRC-1, `src/decapod/core/workspace.rs`, `src/decapod/core/validation_runtime.rs`; [RT-RTE-validate-candidate](#rt-rte-validate-candidate), [RT-RTE-workspace-publish](#rt-rte-workspace-publish).

> let snapshot_handoff =
>     crate::enforce_workbranch_readiness_before_push(repo_root, readiness_invocation)?;
> --- `src/decapod/core/workspace.rs`

## Annotations

none
