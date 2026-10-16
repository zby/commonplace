---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Echel runtime baseline: canonical initialization, legacy work/context execution, verification and scoped change admission at aee36de4d2d1c404fb36e9ad68cc0a920784ee61."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
---

# Echel runtime report

## Runtime account

### Responsibility and evidence

Echel selects product context, invokes a separate agent runtime, and retains run and verification records. It does not implement the model/tool loop. Its shipped CLI also initializes canonical idea records and exposes an older workflow/store family. These are materially different paths, not a demonstrated continuous journey. The frozen boundary and SRC-1 identity are in [boundary](boundary.md#boundary-and-evidence). All source findings below concern that registered commit. No target code, tests or examples were executed. Implementation wiring is distinguishable from actual activation, runtime compliance and benefit, which remain unobserved.

The consequential division of responsibility is stated directly in SRC-1, `src/echel/runtimes/hermes.py`:

> """Thin adapter: Hermes owns the agent loop; Echel owns product truth."""
> --- `src/echel/runtimes/hermes.py`

The executable entry point is `echel.cli.main:main` (SRC-1, `pyproject.toml`). `init` and `clarify` take separate canonical-service branches before the CLI constructs `FileStore` and `WorkflowService` for status, add, advance, work, context, run and verify (SRC-1, `src/echel/cli/main.py`). No autonomous scheduler connects these commands. Each next CLI step belongs to the caller. Hermes owns subsequent agent steps only after explicit execution.

### Ordinary invocation and end-to-end boundary

The ordinary shipped execution path is an invocation of `run` with a previously persisted legacy work ID. Its prerequisite is important: `FileStore` work and knowledge must already exist; current canonical `init` alone does not provide that legacy state. The actual compiled-context path is [RT-RTE-compile-run](#rt-rte-compile-run), backed by [RT-OBJ-compiled-context](#rt-obj-compiled-context), and its legacy state-producing precursor is [RT-RTE-file-workflow](#rt-rte-file-workflow).

The caller supplies project root, work ID, optional model name and whether to execute. Code resolves the root, loads the work item, rejects a non-work record, and selects knowledge by explicit `relates_to` membership. It selects open findings whose `affects` overlap that same set. Text rendering supplies objective, acceptance, verification commands, knowledge statements with IDs/kinds/status/confidence, and open finding statements. It does not render the complete work dictionary or knowledge provenance. Knowledge is not filtered to accepted status. Hence the compiler's word “authoritative” is not a guarantee of accepted-only delivery (SRC-1, `src/echel/context/compiler.py`).

Echel converts that text into a runtime request, builds a Hermes command, allocates an uppercase `RUN` ID and hashes the text. The default is a preview: a run record with status `created` and a command, not an agent invocation. With `--execute`, a synchronous child process runs at the project workspace. The CLI maps zero process exit to `completed`, nonzero to `failed`, and keeps the last 4,000 characters of stdout as the summary. It does not persist the adapter's stderr or mark `completed_at`; it emits the resulting run record. It does not turn the summary into a knowledge proposal or automatically invoke verification (SRC-1, `src/echel/cli/main.py`, `src/echel/model/records.py`).

The runtime client names terminal and file toolsets by default; a direct `RunRequest` caller can specify another tuple. That is a requested grant set, not a deployed sandbox. Echel supplies a working directory, not an isolated worktree or filesystem jail. Its code does not authenticate the Hermes binary, pin its version, wrap each tool use in approval, or prevent the terminal tool from invoking other programs. Actual tool grants, provider tools, callbacks, remote workers, Hermes subagents, model context management and provider behavior remain outside inspected implementation. The adapter has a single blocking subprocess boundary, without an implemented timeout, cancellation, resumption or event-normalization loop (SRC-1, `src/echel/runtimes/base.py`, `src/echel/runtimes/hermes.py`; future integration scope is declared in `docs/hermes.md`). The external model component's version and mutability limits are [RT-CMP-runtime-model](#rt-cmp-runtime-model).

Working-context control here is deterministic pre-invocation selection, not observed compaction. Unrelated knowledge and findings are kept out of the supplied text, but remain reachable on disk and through runtime tools. The selector is code acting on caller-maintained relationships, not model relevance judgment. No Echel token budget, trimming policy or recursive dependency expansion appears in the inspected compiler. Each invocation recompiles from current files. Whether Hermes further transforms, isolates, summarizes or reloads the prompt is uninspected. The shipped implementation skill is additional natural-language guidance, not a body automatically included by this compiler; [RT-BAP-implementation-skill](#rt-bap-implementation-skill) distinguishes requested procedure from verified delivery.

### Three forcing cases

1. **Fresh canonical initialization versus legacy execution.** [RT-RTE-idea-init](#rt-rte-idea-init) writes `.echel/project.json` with a schema envelope and `.echel/records/claims/...`, using colon-namespaced identities. Legacy `FileStore` reads `.echel/knowledge` and `.echel/work` with uppercase IDs, and its `Project(**payload)` expects the old dataclass shape. Thus a fresh CLI init does not establish a usable init-to-work-to-run pipeline. This is an inspected composition mismatch, not a claim that either subsystem cannot function under its own callers. Unit source initializes `FileStore` directly; the integration test checks canonical init's two records, not the combined journey (SRC-1, `src/echel/storage/files.py`, `src/echel/model/records.py`, `src/echel/initialization.py`, `tests/unit/test_core.py`, `tests/integration/test_cli.py`).
2. **Human authority versus alternate writes.** [RT-RTE-knowledge-decide](#rt-rte-knowledge-decide) checks caller-supplied principal kind/capability and records rationale for canonical protected-knowledge decisions. In contrast, legacy `add --status accepted` directly persists caller-selected status; direct `FileStore.put` has no per-content approval check. Canonical schema validation constrains authority fields, but a schema-valid caller-supplied human label is not authentication. Direct canonical writes and workspace file writes are additional paths not mediated by the authority service. This defeats a system-wide interpretation of “only human-approved truth can reach execution” while preserving the service's narrower protocol (SRC-1, `src/echel/authority.py`, `src/echel/schemas/v1/record.schema.json`, `src/echel/storage/records.py`, `src/echel/workflow.py`).
3. **Preview and toolsets versus verification execution.** [RT-RTE-verify-work](#rt-rte-verify-work) invokes stored verification commands directly, outside Hermes. It does not require `run --execute`, apply Hermes toolsets or use the knowledge authority service. Argument splitting avoids implicit shell interpretation, but the executable can itself be a shell or another effectful program. A command can therefore alter the project independently of agent execution. Neither process exit nor a recorded checksum is a semantic answer oracle (SRC-1, `src/echel/verification/runner.py`).

These cases inspect the two in-repository subprocess sites, the direct adapter API, CLI preview/execute branches, legacy writes and the canonical write/authority boundary. They do not reconstruct provider-native tools, host callbacks or remote execution inside Hermes. No source or trace here permits a guarantee about those alternate paths.

### Change admission and guarantees

Product code effects are delegated to Hermes terminal/file tools or verification executables. Their results are not automatically reviewed or rolled back by Echel. Knowledge admission differs by storage family; capability and production-machinery changes instead have a contributor/maintainer path, [RT-RTE-source-admission](#rt-rte-source-admission). The CI definition is a proposed-change check, not evidence that a protected branch, release approval or deployment isolation is configured.

Canonical service entry points also include profile selection, maturity advance, finding creation/decision and backward staleness. Inspected service bodies record human-labelled decisions for profile/maturity/finding state, assess required accepted claims and blocking findings, and stage staleness changes through a transaction journal. They are not wired to the legacy CLI commands, whose `advance --force` has a different gate. These are available canonical API responsibilities, not evidence of exercised repair or theory revision (SRC-1, `src/echel/profiles.py`, `src/echel/lifecycle.py`, `src/echel/findings.py`, `src/echel/cli/main.py`). Detailed memory transformation, transaction, migration, import, query and index findings are left to the memory analysis; their enumerated presence is not a claim of universal authority coverage.

| Guarantee and owner | Enforcement point and strength | Covered paths, alternatives and external contract | Separate conclusions |
|---|---|---|---|
| Caller must opt into Hermes execution; CLI owns branch | `if args.execute` in CLI; invariant of that branch | Covers `run` preview versus execute, not direct adapter execution or `verify`; persistence of preview still requires writable legacy store | implementation conclusion status: wired; operation conclusion status: uninspected |
| Related context only; compiler owns membership | Explicit knowledge-ID and open-finding predicates; invariant of text construction | Covers supplied Echel text, not Hermes context or file reads; no accepted-status or transitive-closure guarantee | implementation conclusion status: wired; operation conclusion status: uninspected |
| Canonical protected decisions require human-labelled capability; authority service owns protocol | Preview authorization, transition consistency check, schema/write preconditions; protocol | Covers service calls under honest caller identity; excludes legacy writes, fabricated authority metadata and arbitrary workspace writes; needs trusted principal provisioning and OS permissions | implementation conclusion status: wired; operation conclusion status: uninspected |
| Canonical single-record conflict handling; store owns installation | Schema validation, expectation check, exclusive write lock, temp file and replace; protocol | Covers cooperating `CanonicalRecordStore.write` callers; not legacy writes or arbitrary file I/O. Identical bytes return unchanged before revision-conflict checks. Requires filesystem atomic replace and cooperative writers; not a multi-record transaction guarantee | implementation conclusion status: wired; operation conclusion status: uninspected |
| Bounded agent objective and no silent truth rewrite; skill author owns instruction | Natural-language skill, not an adapter enforcement point; policy | Requires skill delivery and runtime compliance; terminal/file capability and direct verification are not constrained by this text alone | instruction conclusion status: claimed; operation conclusion status: uninspected |

The guarantee table is supported by the corresponding route records, and by SRC-1, `src/echel/storage/records.py` for the canonical storage scope. Stale-lock inspection/retry and reload/merge/retry on revision conflicts are named recoveries; there is no proof of deployed fault tolerance. The legacy store uses a per-file temporary replacement but allocates IDs by scanning current records and has no shared locking in the inspected class. Concurrent legacy run creation is not covered by the canonical store's protocol (SRC-1, `src/echel/storage/files.py`).

### Added source coverage

Beyond the boundary's initial inspection, this member inspected runtime protocol and complete adapter/compiler/legacy store/workflow/verification/model/CLI bodies; canonical layout and single-record store; initialization; authority; relevant profile, lifecycle and finding service bodies; unit and integration consumer tests; contributor guidance; package metadata; Makefile and CI. All supply SRC-1 implementation or doctrine/design evidence, not new sources. The runtime-model internals, deployed runtime controls and an end-to-end agent trace remain uninspected. Test source establishes intended checks only; no passing result or performance gain is inferred.

## Shared records

### Components

#### RT-CMP-runtime-model
Label: Runtime-selected model

Source-native identity: `RunRequest.model`, passed as Hermes `--model`, or the external runtime's default when unset. Representational form: distributed-parametric model behind the external executable; actual architecture and weights uninspected. Storage substrate: external runtime/provider infrastructure, not Echel's JSON store. Echel stores a model label in `Run`, not weights (SRC-1, `src/echel/runtimes/base.py`, `src/echel/runtimes/hermes.py`, `src/echel/model/records.py`).

Parameters changing during operation: uninspected; Echel's adapter exposes no parameter-update operation. Exact version pinned: no exact model artifact pin is imposed by the inspected adapter. Mutable endpoint resolving to another model: uninspected at the provider, and not prevented by passing a caller-supplied name or default. Provider internals and parameter provenance remain uninspected. This is not evidence that all learning is absent.

> if request.model:
>     command[2:2] = ["--model", request.model]
> --- `src/echel/runtimes/hermes.py`

### Operative objects

#### RT-OBJ-compiled-context
Label: CompiledContext text

Source-native identity: `CompiledContext.as_text()` result. Representational form: natural-language task/knowledge/findings interpreted by the agent; JSON fields, relationship membership and digest computation have symbolic consumers in Echel. Storage substrate: in-process text, then command arguments; the CLI stores the complete command and text digest in legacy run JSON. The JSON output alternative contains full work/knowledge/finding dictionaries, but `run` sends the narrower text rendering (SRC-1, `src/echel/context/compiler.py`, `src/echel/cli/main.py`).

> return CompiledContext(work, tuple(knowledge), tuple(findings))
> --- `src/echel/context/compiler.py`

The text is newly derived from files each time. Sources, tags, most work metadata and most finding metadata are not rendered. Its ID/status annotations describe records but do not make the agent obey them. Selection and downstream authority are recorded in [RT-RTE-compile-run](#rt-rte-compile-run) and [RT-BAP-context-prompt](#rt-bap-context-prompt).

### Routes

#### RT-RTE-idea-init
Label: Canonical idea initialization

Endpoints/progression: CLI caller supplies root/name/idea/owner/profile/config; `IdeaInitializationService.preview` validates and constructs project plus proposed raw-idea claim; optional `apply` stages a temporary repository and renames it to `.echel`. Owner/next step: caller chooses preview versus apply and must subsequently review/clarify. Policy and form: symbolic input/schema/secret-pattern checks over human-supplied natural-language idea and owner metadata. Admission: caller supplies the content and the apply choice; no model authorship or authenticated human identity is established. Rejection occurs for existing state, bad root, invalid identifiers/profile/config, recognized secret patterns or changed plan digest. These patterns do not promise complete secret detection. Recovery removes staged state on handled apply failure; there is no overwrite-style reinitialization or automatic content correction (SRC-1, `src/echel/initialization.py`, `src/echel/cli/main.py`).

> store.write(plan.project, RecordExpectation.absent())
> store.write(plan.idea, RecordExpectation.absent())
> os.replace(temporary, destination)
> --- `src/echel/initialization.py`

- Immediate return: Preview plan or applied two-record summary, digest and next action; CLI returns error code 2 for InitializationError.
- Later read-back: Canonical project/claim can be loaded by canonical services; legacy work/context consumers use a different layout.
- Delegated visibility: inapplicable — initialization does not delegate to an agent.
- Selection predicate: Caller selects one root and idea; profile must be registered; owner must have user namespace.
- Invalidation or expiry: No expiry; existing `.echel` blocks initialization; preview digest detects changed staged content.
- Activation or effect: Apply publishes canonical project and proposed claim, not accepted truth or a demonstrated agent result.
- Evidence limits: SRC-1 implementation and integration-test source only; no observed atomicity under faults or complete CLI journey.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open user-supplied idea capture. Proposer and deciding caller are not authenticated by identifier syntax; software can veto structural violations. Answer oracle: no reference answer to the idea; schema and secret patterns are validation predicates, not product correctness oracles. Guidance is the minimal-idea contract encoded in preview; project/claim/provenance persist, not a derived implementation plan.

#### RT-RTE-file-workflow
Label: Legacy work and knowledge writes

Endpoints/progression: `WorkflowService` loads the legacy project, adds caller-supplied knowledge or work, and persists via `FileStore.put`; status/advance uses accepted/validated kinds at the current stage. Owner: caller supplies statements, statuses, relationships, acceptance and verification; code assigns IDs and next stage. Form: natural-language content plus symbolic IDs/status/stage fields in JSON on the local filesystem. This is distinct from canonical protected-knowledge decisions, not a duplicate of [RT-RTE-knowledge-decide](#rt-rte-knowledge-decide) (SRC-1, `src/echel/workflow.py`, `src/echel/storage/files.py`).

> if state["missing"] and not force:
>     raise LifecycleBlocked(
>         f"{project.current_stage} is not usable; missing accepted knowledge: "
>         + ", ".join(state["missing"])
>     )
> --- `src/echel/workflow.py`

- Immediate return: New knowledge/work record, status report or advanced stage; malformed references/store state can reject the call.
- Later read-back: Knowledge/work JSON is loaded by compiler, workflow status and verifier on later invocations.
- Delegated visibility: Selected knowledge/work content reaches Hermes only through the separate compile/run route.
- Selection predicate: Explicit IDs for work relationships; status checks knowledge type, stage and accepted/validated status; `force` bypasses missing-kind rejection.
- Invalidation or expiry: No automatic expiry in these bodies; caller can supply statuses or replace files; current stage changes on advance.
- Activation or effect: Direct retained writes and stage changes; no mandatory separate approval before caller-selected accepted status.
- Evidence limits: Inspected legacy bodies and test source; canonical init compatibility and concurrent ID safety are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: CLI permits caller-selected accepted/validated knowledge; `FileStore.put` checks collection and ID shape, not a Principal. Work creation verifies referenced IDs exist but does not require accepted knowledge. The knowledge-write policy string emitted by legacy initialization is not consulted by these writes. Software can veto bad references or non-forced missing requirements; a separate human veto is not implemented here. Operating mode: open caller-driven workflow. Answer oracle: kind-presence checks, not expected semantic outcomes. Proposed changes persist as knowledge/work/project JSON. Per-file replacement is not history or semantic rollback; restoration/revision is caller-managed (SRC-1, `src/echel/cli/main.py`, `src/echel/workflow.py`, `src/echel/storage/files.py`).

#### RT-RTE-compile-run
Label: Compile work and invoke Hermes

Endpoints/progression: caller work ID → `ContextCompiler.compile` → text/digest → `RunRequest` → preview command or Hermes subprocess → `RuntimeResult` → legacy run JSON and CLI output. Decision owner: code selects context and branch; Hermes owns model/tool next steps after launch. Context object and model: [RT-OBJ-compiled-context](#rt-obj-compiled-context), [RT-CMP-runtime-model](#rt-cmp-runtime-model). Executor/effect boundary: child process with inherited host privileges at workspace cwd, requested terminal/file tools; no Echel per-tool approval gate (SRC-1, `src/echel/cli/main.py`, `src/echel/context/compiler.py`, `src/echel/runtimes/base.py`, `src/echel/runtimes/hermes.py`).

> related = set(work.get("relates_to", []))
> knowledge = []
> for record in self.store.records("knowledge"):
>     if record.get("id") in related:
>         knowledge.append(record)
> --- `src/echel/context/compiler.py`

> allowed_toolsets: tuple[str, ...] = ("terminal", "file")
> --- `src/echel/runtimes/base.py`

- Immediate return: Context command prints text/JSON; run command emits persisted preview/completed/failed Run; direct adapter returns command, exit code, stdout and stderr.
- Later read-back: Persisted Run includes digest, command and bounded stdout summary; the inspected compiler does not read runs as knowledge. Related knowledge/findings are reloaded for a later compile.
- Delegated visibility: Hermes receives rendered text and requested model/toolsets; runtime-internal subagent visibility is uninspected.
- Selection predicate: Work type check; explicit related knowledge IDs; only open findings intersecting those related IDs. Knowledge status does not exclude delivery.
- Invalidation or expiry: Recompile reads current files; no cache expiry or revocation of already delivered text is implemented here.
- Activation or effect: With execute, launches external runtime; model compliance, actual tool effects and benefit are unobserved. Preview only records a requested command.
- Evidence limits: Adapter/CLI implementation, command-construction test source and integration doctrine; no Hermes/provider trace or deployed isolation evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision policy: deterministic Echel membership/formatting and caller execute flag; external runtime policy opaque. Operating mode: open bounded task request, not a curriculum or comparative experiment. Answer oracle: acceptance/verification text is supplied as guidance; model judgment is not an oracle, and process zero exit is only a process result. Admission: caller grants execution, not per-change acceptance. Runtime may propose/perform code edits through granted tools; Echel's inspected postprocessing neither parses proposals nor admits them into canonical knowledge. Rejection/recovery: missing executable raises RuntimeError; nonzero exit yields failed Run; no adapter retries or undo. If execution raises before `store.put`, no Run is saved by that branch. After a subprocess return, the CLI itself returns 0 even when the recorded run is failed (SRC-1, `src/echel/cli/main.py`, `src/echel/runtimes/hermes.py`).

#### RT-RTE-verify-work
Label: Execute work verification

Endpoints/progression: caller work ID → loaded `verification` strings → `shlex.split` → synchronous subprocess at workspace cwd → Evidence per command → legacy evidence JSON. Owner: caller/record author supplies executable checks; code executes all listed commands and maps exit status to passed/failed summary. Form: command strings parsed symbolically into argv; natural-language summaries and symbolic checksums/exit codes persisted (SRC-1, `src/echel/verification/runner.py`).

> for raw_command in work.get("verification", []):
>     command = shlex.split(raw_command)
>     completed = subprocess.run(
>         command,
>         cwd=self.store.workspace,
>         text=True,
>         capture_output=True,
>         check=False,
>     )
> --- `src/echel/verification/runner.py`

- Immediate return: List of Evidence records with command, subject, exit code, passed/failed summary and hash of combined output.
- Later read-back: Evidence files persist for later callers; no automatic knowledge promotion or compiler consumption is wired in this runner.
- Delegated visibility: Direct child executable receives argv and project cwd, not the compiled agent context or Hermes toolsets.
- Selection predicate: Every verification string in the loaded record; this runner does not check `record_type` before reading that field.
- Invalidation or expiry: No expiry or automatic rerun; repeated invocations append new IDs by store scan.
- Activation or effect: Executes host programs and records outcomes; arbitrary executable effects are possible, not sandboxed by argv splitting.
- Evidence limits: Source only; command correctness, safety, observed execution and causal benefit are unestablished. Output bytes are hashed, not retained by this body.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: caller-authored checks on a work packet. Proposer: work author; decision rule: executable return code; veto: failure is recorded, not a rollback or knowledge rejection. Answer oracle: any reference expected answer belongs inside the caller-supplied executable and is uninspected here. Admission of project effects is simply authority to run the command; no separate human per-effect approval. Recovery: nonzero exit continues to subsequent commands; launch/splitting failures can interrupt after earlier evidence/effects. No timeout, cancellation, compensating action or automatic evidence-to-knowledge update is present in this runner.

#### RT-RTE-knowledge-decide
Label: Canonical protected knowledge decision

Endpoints/progression: caller provides proposed claim/decision/learning identity, accepted/rejected action, Principal, rationale/time → service preview checks and loads record → authority-stamped revision → apply consistency checks → canonical write. Owner: caller-supplied authorized-human principal decides content acceptance/rejection; software validates allowable state and evidence structure. Natural-language statement/outcome/rationale is retained in schema-governed symbolic JSON. Storage/effect: canonical single-record file, not legacy knowledge collection (SRC-1, `src/echel/authority.py`, `src/echel/storage/records.py`).

> if principal.kind != "human" or AUTHORITY_CAPABILITY not in principal.capabilities:
>     raise AuthorityError(
>         "ECHEL-AUTHORITY-DENIED",
>         "principal",
>         "an authorized human with knowledge:decide capability must make this decision",
>     )
> --- `src/echel/authority.py`

- Immediate return: Preview AuthorityTransition or applied RecordWritePlan; unauthorized/invalid/state-conflicting requests raise errors.
- Later read-back: Canonical load/scan can consume status, rationale, actor and revision; legacy compiler does not read this canonical collection.
- Delegated visibility: inapplicable — this service does not invoke or deliver content to a model.
- Selection predicate: Only protected record types and only proposed current status; action accepted or rejected; human-labelled principal with knowledge:decide.
- Invalidation or expiry: Expected revision/digest guards changed writes; accepted/rejected records cannot be decided again by this preview route. No time expiry.
- Activation or effect: Installs accepted/rejected status and authority metadata; this is not authenticated human identity or demonstrated downstream model reliance.
- Evidence limits: Service/schema/store implementation only; caller identity trust, external filesystem permissions and actual review quality unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission mechanism: content is proposed before this service; it does not author the proposal. Human contribution is represented by Principal and rationale, but the API caller can construct them. Software can reject unsupported types, unauthorized labels, empty rationale, invalid time, non-proposed state or a write conflict. Apply checks metadata consistency rather than re-authenticating a person. Direct canonical-store writes still require schema-valid authority structure for accepted protected records, but not a call through this service. Required external contract: trusted identity provisioning and restricted write access. Guarantee strength: protocol, not isolation invariant. Rollback/recovery: conflict requests reload/merge/retry; no generic reversal of accepted decisions is supplied by this service. Guidance encoded here is explicit attributable human decision; persisted output is record revision plus rationale, not proof the rationale is sound. Operating mode: open caller-driven review. Answer oracle: human content judgment; no executable reference outcome.

#### RT-RTE-source-admission
Label: Contributor and maintainer change admission

Endpoints/progression: contributor selects approved task/ownership → edits code/contracts/tests → task checks and baseline → patch/PR evidence → maintainer accept/request changes/reject/split. This is the route for Echel capability, adapter or production-machinery changes as repository artifacts. Owner: contributor proposes, maintainers decide merge/release/deployment and durable knowledge acceptance. Representational forms: natural-language task and review guidance; symbolic source, CI YAML and test exit checks. Storage: repository patch/history and external collaboration channel; no external collaboration trace is supplied (SRC-1, `CONTRIBUTING.md`, `.github/workflows/quality.yml`, `Makefile`, `pyproject.toml`).

> Maintainers may accept, request changes, reject, or split the contribution. Merge, release, deployment, and durable knowledge acceptance remain explicit human decisions.
> --- `CONTRIBUTING.md`

- Immediate return: Proposed patch/PR and verification report under contribution doctrine; CI is wired to push, PR and manual events.
- Later read-back: Accepted source changes can affect subsequent installations/runs; no supplied acceptance, release or deployment event establishes that horizon was attained.
- Delegated visibility: Contributor agents receive task instructions through an external collaboration process, not the runtime compiler by default.
- Selection predicate: Ready approved task and ownership by doctrine; CI baseline requires named core jobs to succeed, not proof of semantic task completion.
- Invalidation or expiry: Changes may be rejected or revised; rollback impact must be reported. Automatic deployed rollback is uninspected.
- Activation or effect: CI defines test/type/lint/package/security checks; actual merge, installation and production activation remain unobserved.
- Evidence limits: Shipped contribution procedure and CI source, not branch-protection settings, reviewer identity, CI results or a release trace.
- instruction conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: maintainer human decision, with software check results as evidence and possible rejection inputs. Contributor guidance requires exact verification results, focused scope, authority preservation and rollback impact; accepted code/contracts persist in repository history. Answer oracle: test assertions and tool checks are bounded reference predicates; the CI baseline requires success from core jobs but is not an oracle for product truth. Operating mode: open task/PR workflow, not automatic self-modification. Improvement trigger is a demonstrated workflow task; proposal and acceptance do not establish improved capacity, exercised self-improvement or a theory-building loop. Recovery is revision/rejection/maintainer-directed rollback; no autonomous production admission is evidenced.

### Claims

#### RT-CLM-runtime-boundary
Label: Runtime and product truth separation

Claimed operation: Hermes supplies runtime execution and Echel owns product truth/context. Source: SRC-1, `src/echel/runtimes/hermes.py`, `docs/hermes.md`. The adapter quotation in the runtime account is the minimum statement. Wiring supports delegation, not universal protection of truth. Alternate legacy writes, external tool effects and caller-supplied authority prevent interpreting this division as a system-wide security invariant. See [RT-RTE-compile-run](#rt-rte-compile-run), [RT-RTE-file-workflow](#rt-rte-file-workflow) and [RT-RTE-knowledge-decide](#rt-rte-knowledge-decide).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-prompt
Label: Product context to runtime prompt

Consumer: Hermes and its selected model. Channel: `-q` command argument from compiled text. Force: supplied task objective, acceptance, verification and knowledge/findings for natural-language interpretation, not an enforced tool policy. Horizon: current runtime request; retained files allow recompilation across invocations, but actual repeated reliance is unobserved. Symbolic IDs select delivery before model consumption; status annotations do not enforce truth acceptance. Evidence: SRC-1, `src/echel/context/compiler.py`, `src/echel/runtimes/hermes.py`, through [RT-RTE-compile-run](#rt-rte-compile-run).

#### RT-BAP-implementation-skill
Label: Implementation skill guidance

Consumer: an implementation agent when this shipped skill is loaded. Channel: repository skill Markdown, outside the inspected compiler's text construction. Force: procedural instruction to respect objective/permissions, inspect code, verify and separate knowledge proposals; no adapter-side enforcement. Horizon: the loaded skill invocation; recurring loading and compliance remain uninspected. Evidence: SRC-1, `skills/implementation/SKILL.md`:

> Work only within the supplied objective and permissions. Inspect relevant code before editing. Run the declared verification. Return code changes, evidence, unresolved findings, and proposed knowledge updates separately. Never silently rewrite accepted product truth.
> --- `skills/implementation/SKILL.md`

This is static shipped guidance, not a demonstrated retained revision or a theory-builder cycle. It is distinct from compiler-delivered product statements in [RT-BAP-context-prompt](#rt-bap-context-prompt).

## Annotations

none
