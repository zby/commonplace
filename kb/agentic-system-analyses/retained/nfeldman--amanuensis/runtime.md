---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Amanuensis runtime baseline: host-directed surveys, bound MCP state access, publication and change admission at the frozen revision."
run-id: AAS-2026-11-08-amanuensis-b3a8e3e53488-01
reviewed-boundary: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
---

# Amanuensis runtime report

## Runtime account

### What runs, and who owns the next step

Amanuensis combines a portable agent method with a deterministic state service. The host's model is the coordinator: it chooses scope, reads source, interprets evidence, invokes tools and continues phases. The MCP server validates requests and changes or queries the conspectus; it does not run the model's survey reasoning. Python projects retained records into documentation. Thus the consequential work is not merely an API return: it is a survey whose findings, explanations, evidence and prose survive for later agents and human readers. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `mcp-server/src/index.ts`, `materializer/materialize.py`. See [RT-RTE-survey-cycle](#rt-rte-survey-cycle), [RT-RTE-tool-dispatch](#rt-rte-tool-dispatch), [RT-RTE-locus-read](#rt-rte-locus-read) and [RT-RTE-docs-publication](#rt-rte-docs-publication).

The shipped entry points are `amanuensis-memory` → `dist/index.js`, `amanuensis` → `dist/cli.js`, and the historical evaluator script. The package describes itself as evidence-backed codebase memory and ships the skill, MCP service, adapters and materializer. Installation supports Claude, Codex, VS Code and a generic portable-skill path. The optional project agent-instructions paragraph is opt-in; user-scoped Codex installation does not write a repository paragraph. These are delivery mechanisms, not evidence that a deployed host loaded or obeyed them. SRC-1: `mcp-server/package.json`, `mcp-server/src/cli.ts`.

> "amanuensis-memory": "dist/index.js",
> "amanuensis": "dist/cli.js",
> "amanuensis-evaluate-history": "scripts/historical-evaluation.mjs"
> --- `mcp-server/package.json`

An ordinary requested subsystem survey proceeds as follows, at the implementation/doctrine boundary rather than as an observed run:

1. The installed skill instructs the coordinator to discover and call MCP tools, handshake with the chat's absolute project root, reject a mismatch, distinguish a cold store from a warm one and check autoprogress. Warm state supplies dashboard, subsystem priorities and active-session dispatch history; changed HEAD routes through change detection. The user supplies the problem and can redirect, but is not asked to approve each survey phase. SRC-1: `.claude/skills/amanuensis/SKILL.md`.
2. The stdio server selects a workspace from explicit arguments, environment, Codex launch discovery or cwd rules, or stays unbound. It creates a context with `sessionId: null`. The first state access lazily initializes storage and opens SQLite with WAL, foreign keys, migrations and schema. `start_session` inserts a session and sets the connection context's session ID; this is bookkeeping identity, not authenticated human identity. SRC-1: `mcp-server/src/index.ts`, `mcp-server/src/db.ts`, `mcp-server/src/session.ts`.
3. The coordinator scopes files, records structural claims and explanations, evaluates concerns, and seeks disproof in adversarial review. Phases 1–4 can run in host Task-tool subagents with the phase instructions, subsystem ID, session ID and survey SHA, or inline when subagents are unavailable. The generic subagent/inline language in the skill is qualified by the specialized survey and packaging references: Phase 5 runs in the coordinator, not a separate phase agent. That coordinator settles explanations against earlier criticisms and owns publication. For delegated phases, only the summary is prescribed to return; host context isolation and exact model input assembly are not implemented by this server. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/subsystem-survey.md`, `.claude/skills/amanuensis/references/phase-4-adversarial.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md`.
4. Typed tool handlers validate and retain records, while the coordinator asks for status advances. Both ordinary status writers invoke forward prerequisite checks and separately check explanation discharge into `mapped`. The gates inspect records, not whether the model actually read carefully or whether its interpretations are true. SRC-1: `mcp-server/src/tools/subsystems.ts`, `mcp-server/src/invariants.ts`.
5. Packaging updates registered prose, settles explanations, materializes views, closes the session, advances status and checkpoints. This prescribed order has a recovery caveat: `end_session` clears the context's session ID, whereas `commit_phase_gate` requires an active session. Following the reference literally through its final checkpoint therefore requires reopening a session or correcting the order. `end_session` itself attempts a storage commit when Git is available. SRC-1: `.claude/skills/amanuensis/references/phase-5-packaging.md`, `mcp-server/src/tools/project.ts`, `mcp-server/src/tools/storage-history.ts`.
6. The terminal products are tool responses, an asynchronous counts/questions summary and the exact returned HTML entrypoint. Later agents can query the same database through the locus reader rather than reconstructing knowledge from the old chat. Crashes are addressed by durable store state, session/dispatch history and Git checkpoints; these do not guarantee resumption from the exact interrupted reasoning step. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `mcp-server/src/tools/storage-history.ts`, `mcp-server/src/tools/locus.ts`.

### Four forcing cases and the guarantees they delimit

**Workspace identity.** Owner: MCP server and project-binding module. Enforcement: request handler before tool execution, plus immutable receipt checks and storage path containment. Strength: invariant within this service path, not a host sandbox. A differing explicit handshake is refused before its requested database is opened; unbound project tools fail. Startup also rejects conflicting Git roots selected by arguments/environment unless the explicit workspace-pin override is enabled. Non-Git cwd fallback remains supported outside the Codex/root-launch cases. An omitted handshake on an already bound connection still uses that binding: code cannot verify the caller's intended chat workspace without the caller supplying it. Required external contract: correct workspace supplied by the host/coordinator. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `mcp-server/src/index.ts`, `mcp-server/src/project.ts`. See [RT-RTE-tool-dispatch](#rt-rte-tool-dispatch).

**Status admission through the second writer and deferred state.** Owner: subsystem handlers/invariants. Strength: invariant for the checks actually reached, not universal completion certification. Fresh late-status `upsert_subsystem` and ordinary forward `update_subsystem_status` both walk intermediate prerequisites. However `deferred` is outside the ordered status list: a transition from it returns before the walk. The public update schema accepts deferred and mapped, and its handler calls the same early-return function. Explanation discharge into mapped is separately enforced even from deferred; challenge, structural and reconciliation checks in the forward walk are not. Thus a deferred-to-mapped request with dischargeable purpose/account is not subjected to that walk. This is a source-reachable conditional path, not a demonstrated corrupt deployed store. Reset is another explicitly destructive status writer that transactionally removes dependent survey records and withdraws explanations; it is not an ordinary monotonic advance. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: honest workflow use, including a resurvey rather than treating deferred as completion. SRC-1: `mcp-server/src/tools/subsystems.ts`, `mcp-server/src/invariants.ts`.

> if (currentRank < 0 || targetRank <= currentRank) return [];
> --- `mcp-server/src/invariants.ts`

> if (targetStatus !== "mapped" || currentStatus === "mapped") return [];
> --- `mcp-server/src/invariants.ts`

**Publication options through the emitted result.** Owner: MCP materialization wrapper and Python materializer. Strength: protocol for verified clean publication, not an unconditional publication invariant. MCP always preflights complete HEAD reconciliation before rendering. But `clean_publish` defaults false; normal rendering writes output before verification and does not promise to preserve the previous view on red. Even with clean mode, the advertised `verify_readback=false` option is converted to `--no-verify-readback`. Python passes it to the staged materializer, which can return `ok=true` without running the verifier; clean mode promotes on that `ok` value. The absence of a readback also means no projection verification run is recorded by `recordReadback`. The options are accepted by the public MCP schema, so this is not merely an internal uncallable branch. The narrower guarantee is preservation on failed *verified clean* rendering, subject to filesystem rename/recovery behavior. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: choose clean mode with verification enabled and use the intended Python executable/script. SRC-1: `mcp-server/src/tools/materialize.ts`, `materializer/materialize.py`, `materializer/amanuensis_materializer/core.py`.

> if (!verifyReadback) cliArgs.push("--no-verify-readback");
> --- `mcp-server/src/tools/materialize.ts`

> if self.verify_readback:
>     self.summary.readback = ProjectionVerifier(
>         self.storage, self.output, expected_paths
>     ).verify()
>     if not self.summary.readback["ok"]:
>         self.summary.ok = False
> --- `materializer/amanuensis_materializer/core.py`

**Alternate executors.** The shipped standalone Python entry accepts explicit storage/workspace/output paths and invokes `Materializer` directly; its main path does not invoke the MCP reconciliation preflight or storage output containment. It still checks storage/database existence, required views and renderer/readback conditions. The Chorusmith adapter executes catalogued domain handlers directly, inside its own transaction, rather than reentering the outer MCP Ajv dispatcher; it adds frozen-plan custody, ordinal and hash checks. Handler-level checks therefore matter independently of transport schema checks. The skill also permits direct prose/storage writes by the host agent, whose shell and filesystem grants are not established here. No claim that MCP validation governs every way of changing files or consuming the database follows. SRC-1: `materializer/materialize.py`, `materializer/amanuensis_materializer/core.py`, `mcp-server/src/tools/chorusmith-adapter.ts`, `.claude/skills/amanuensis/SKILL.md`.

> const result = tool.handler(toolArgs, ctx);
> --- `mcp-server/src/tools/chorusmith-adapter.ts`

These cases challenge universal readings of workspace, completion and publication promises without asserting that they were exercised. The current grant set and deployed isolation envelope are uninspected: the service's tool annotations explicitly do not authorize operations; host permissions govern shell, Task agents and source writes. The skill's “Never modify source code” is a model-facing policy, not OS isolation. Materialization can select a script with `AMANUENSIS_MATERIALIZER` and Python with `AMANUENSIS_PYTHON`, so the checked-in renderer's behavior additionally depends on operator configuration. SRC-1: `mcp-server/src/index.ts`, `mcp-server/src/tools/materialize.ts`, `.claude/skills/amanuensis/SKILL.md`.

### Changes to retained knowledge and operating machinery

The ordinary survey admits model-authored claims using session/evidence/revision checks rather than per-content human approval. Its criticism is code-directed, and the server rejects malformed or unsupported record shapes, not false prose as such. Detailed revisions belong to the memory/epistemic analyses. Separate decision tools distinguish a draft from accepted authority, while learning tools qualify and activate policy representations. Neither storing an architectural decision nor returning an active policy proves implementation of a code change or actual later-run benefit. See [RT-RTE-decision-admission](#rt-rte-decision-admission) and [RT-RTE-policy-admission](#rt-rte-policy-admission). SRC-1: `mcp-server/src/tools/claims.ts`, `mcp-server/src/tools/decisions.ts`, `mcp-server/src/tools/learning.ts`.

Method qualification adds another admission boundary: crosswalk scoring combines predicted effect, controls, red gates, custody and readback; `activate_qualified_method` inserts an unattended registry row, whose SQLite trigger requires a matching passed plan and passed/read-back score. This is not a model-weight update. Generic learning-policy verification subsequently compares serialized state, coverage and content and transactionally switches the active successor. These checks support admission wiring, not independent authentication of caller-supplied outcomes. SRC-1: `mcp-server/src/tools/crosswalk.ts`, `mcp-server/src/schema.sql`, `mcp-server/src/tools/learning.ts`.

> BEGIN SELECT RAISE(ABORT, 'unattended method policy requires passed qualification and read-back'); END;
> --- `mcp-server/src/schema.sql`

No target execution, trial or receipt is used in this runtime report. All positive implementation findings below are source wiring, and workflow instructions are doctrine/design. Operation, model compliance, activation in a user's host and causal benefit remain unobserved. Added SRC-1 inspection beyond the boundary's initial scope includes bounded passages of `mcp-server/src/invariants.ts`, `session.ts`, `storage-git.ts`, `project.ts`, `schema.sql`, tools `subsystems.ts`, `project.ts`, `locks.ts`, `logging.ts`, `dispatch.ts`, `learning.ts`, `crosswalk.ts`, `decisions.ts`, `design-session.ts`, `chorusmith-adapter.ts`, and `materializer/amanuensis_materializer/core.py`, plus adversarial, packaging and subsystem-survey references. Design/review/evaluation declarations identify additional controlled-packet and scoring surfaces; their full handler chains, historical evaluator operation, rebuild receipts, and all host-specific scheduling remain uninspected here. They are included available paths, not evidenced absences or inaccessible sources. This prevents a system-wide claim about isolation, evaluation effectiveness or automatic downstream use of every admitted policy.

## Shared records

### Components

#### RT-CMP-host-model
Label: Host coordinator model

The skill addresses the host model as coordinator; optional Task-tool agents perform survey Phases 1–4, while Phase 5 packaging is reserved for the coordinator by the specialized references. Representational form: distributed-parametric, with natural-language task inputs. Storage substrate: external host/provider, not Amanuensis SQLite. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md`. Parameters changing during operation: uninspected, because provider execution is outside this source. Exact model version pinned: not specified by this skill. Mutable endpoint resolving to another model: uninspected; host selection and endpoint mapping are not supplied. This component performs scope inference, evidence interpretation and proposal authoring, not the server's deterministic queries.

> **As a Task-tool subagent** (preferred when available). Spawn with the
> relevant reference file's instructions, plus subsystem id, session id,
> and the survey-session SHA. Keeps Phase 2's structural read out of
> Phase 3's concern-reasoning context.
> --- `.claude/skills/amanuensis/SKILL.md`

### Operative objects

#### RT-OBJ-amanuensis-skill
Label: Amanuensis skill and phase references

Source-native identity: portable `amanuensis` skill. Representational form: natural-language instructions interpreted by host agents; the frontmatter also supplies symbolic skill-discovery metadata. Storage substrate: shipped Markdown files copied into client skill directories. It specifies start routing, phase order, evidence discipline, checkpointing and later reading. Static instructions are not retained experience merely because installed on disk. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `mcp-server/src/cli.ts`.

> Read the reference for the phase you're about to run; don't preload
> everything.
> --- `.claude/skills/amanuensis/SKILL.md`

### Routes

#### RT-RTE-survey-cycle
Label: Host-directed survey cycle

Trigger/principal: user survey, onboarding or resume request. Owner of next steps: coordinator model, with optional host agents for Phases 1–4 and inline fallback when subagents are unavailable; Phase 5 packaging remains coordinator-only. Progression: orientation → scoping → structural → concerns → adversarial → packaging. Phase IDs, session ID and revision tie work to persistent state. The phase model chooses evidence and proposes conclusions; the coordinator integrates criticisms, settles explanations and revises packaging; deterministic tools admit records and gate some transitions. No expected-answer oracle is supplied for ordinary surveys: source code and evidence are the objects of examination, not a supplied reference answer. Operating mode: open user requests with phased scope and event-driven refresh, not a fixed experimental curriculum. The user may redirect or stop; destructive unauthorized operations require stopping after a snapshot. Admission/rejection: tools can refuse missing prerequisites; the coordinator diagnoses, retries once, then defers independent work if necessary. Recovery: durable checkpoints and dispatch history; reset is an explicit destructive alternative. Guidance and what persists: shipped evidence/adversarial instructions shape proposals; database records and registered prose persist, not necessarily full agent context. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/phase-4-adversarial.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md`, `mcp-server/src/tools/subsystems.ts`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Phase summaries, counts, open questions and final HTML entrypoint are prescribed for the user/coordinator.
- Later read-back: Subsequent sessions query stored survey state and resume from active-session dispatch history; this record does not reclassify the individual memory stores.
- Delegated visibility: For Phases 1–4, phase instructions, subsystem/session IDs and survey SHA are prescribed inputs; one-line phase summary returns. Inline mode isolates nothing. Phase 5 is not a separate delegated context: the coordinator reads retained results, settles explanations and publishes.
- Selection predicate: Explicit user scope controls; otherwise cold/warm start, priority and stale backlog determine work.
- Invalidation or expiry: Changed HEAD triggers change detection; adversarial evidence can overturn findings or replace claims; pause stops at a phase boundary.
- Activation or effect: Instructions ask models to survey and retain state; actual host compliance is unobserved.
- Evidence limits: Doctrine establishes requested reasoning and separation, not a host-enforced context frame, successful criticism or improved capacity. Generic phase-delegation wording does not override the specialized coordinator-only packaging requirement.

> Phase 5 of a per-subsystem survey runs in the **coordinator** — not as
> a separate phase agent.
> --- `.claude/skills/amanuensis/references/phase-5-packaging.md`

The skill's generic subagent/inline options below apply subject to that specific ownership rule. The survey reference independently labels packaging as direct coordinator work. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/subsystem-survey.md`.

> **Inline** (fallback). Read the reference yourself, do the work, then
> continue coordinating.
> --- `.claude/skills/amanuensis/SKILL.md`

#### RT-RTE-tool-dispatch
Label: Bound MCP request dispatch

Endpoints: stdio MCP request → named handler → JSON result. Owner: server code; caller supplies name and arguments. Code compiles advertised schemas with Ajv, checks binding, lazily opens the database and invokes a synchronous handler. The process context holds one session ID; this is not a distinct session per delegated agent. Evidence: SRC-1, `mcp-server/src/index.ts`, `mcp-server/src/session.ts`, `mcp-server/src/project.ts`, `mcp-server/src/db.ts`. Guarantees and alternate executors are delimited in the runtime account. Transport errors become `ok:false` responses; unexpected tool errors also go to stderr. SQLite transactions provide atomicity only where handlers actually use them. Write locks provide holder/TTL bookkeeping for artifact coordination, not established OS exclusion over every file writer. SRC-1: `mcp-server/src/tools/locks.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `jsonResult` emits the handler result, using compact serialization when declared.
- Later read-back: Mutating handlers can commit state to SQLite/files for later reader tools; dispatch alone does not choose a retained semantic object.
- Delegated visibility: A host agent with access can call tools; the service does not prove a host's per-agent tool grant or context isolation.
- Selection predicate: Exact registered tool name, schema-valid arguments and a usable bound workspace.
- Invalidation or expiry: Connection binding is not rebindable; changed repository/storage identity is rejected by receipt checks. Process session context ends or changes independently of stored session rows.
- Activation or effect: Calls execute selected handlers under the server process's OS permissions; annotations are hints, not authorization.
- Evidence limits: Direct domain-handler adapters bypass this outer schema dispatch, and shell/storage writes are not covered by its guarantees.

> // MCP annotations are hints, not authorization. Keep the read-only set
> // intentionally narrow: every get/list/lookup tool is contractually a
> // query, while tools such as verify_* may also record custody evidence.
> --- `mcp-server/src/index.ts`

#### RT-RTE-locus-read
Label: Deterministic locus account delivery

Endpoints: `describe_locus` arguments → standing/scope and account builders → bounded JSON → host agent. Owner: code determines record selection and omission; the receiving model decides how to answer. Model-visible context is controlled by section selection, retention order, omission bookkeeping and response-byte budgets, not by summarizing the accumulated chat. Full stored records remain reachable by other reader calls; server-side delivery does not remove earlier host turns. SRC-1: `mcp-server/src/tools/locus.ts`, `mcp-server/src/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Standing, requested account sections, census, omissions and trace; no model call in this handler.
- Later read-back: Reads prior stored survey content on each invocation; the read itself does not author a new explanation.
- Delegated visibility: Same tool payload can reach any permitted host caller; no distinct delegated window is created here.
- Selection predicate: Locus kind/value, optional sections and supported revision filtering; builders use recorded scope and authorization, then deterministic retention.
- Invalidation or expiry: Standing marks unchecked revision drift; over-ceiling payloads fail rather than silently truncating immutable counts.
- Activation or effect: Delivers recorded context; obeying standing in an answer remains model-mediated.
- Evidence limits: Intended byte budget can be exceeded by the untruncatable floor and is explicitly flagged; hard ceiling rejection is a different control. No proof of downstream answer accuracy.

> trace.within_budget = false;
> trace.over_budget_reason = OVER_BUDGET_REASON;
> --- `mcp-server/src/tools/locus.ts`

#### RT-RTE-docs-publication
Label: Conspectus projection and publication

Endpoints: MCP tool or standalone Python arguments → materializer → HTML/Markdown and optional readback → caller. Owner: deterministic wrapper/renderer. State: retained SQLite and prose, output manifest, projection contract and optional verification rows. Executor/effect boundary: child Python with inherited environment and filesystem access; MCP resolves output under bound storage. Admission: code promotes a clean stage on `ok`; it refuses unmanaged output replacement. Rejection/recovery: verified red stage is discarded; exception after backup can restore the prior output. Ordinary non-clean mode is not that rollback protocol. Operating mode: requested publication, with optional diagnostic verification escape; no model answer oracle. Verification compares projection to durable source truth, not correctness of that truth. SRC-1: `mcp-server/src/tools/materialize.ts`, `materializer/materialize.py`, `materializer/amanuensis_materializer/core.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed last-line JSON, exit status, stderr when present, HTML entrypoint and optional projection-run ID.
- Later read-back: Documentation files are available to humans/later agents; verify-only mode checks existing views without rerendering.
- Delegated visibility: Python receives bound storage/workspace/output and flags, not a model transcript; caller receives summary, not renderer internal context.
- Selection predicate: Page plan and source hashes determine incremental regeneration; clean mode forces full staging.
- Invalidation or expiry: Changed inputs/version trigger rendering; readback mismatches mark failure when verification is enabled.
- Activation or effect: Writes generated views; clean stage promotion is conditional on `ok`, which is not invariably a completed readback.
- Evidence limits: Default non-clean rendering and no-verification options narrow preservation/verification claims; standalone entry is outside MCP preflight.

> if summary.get("ok", False):
>     if output.exists():
>         backup = output.with_name(
>             f".{output.name}.amanuensis-backup-{uuid.uuid4().hex}"
>         )
>         output.rename(backup)
>     stage.rename(output)
>     summary["published"] = True
> --- `materializer/materialize.py`

#### RT-RTE-decision-admission
Label: Recorded decision authority admission

Endpoints: drafted decision revision → accept/reject/invalidate tools → durable revision/events/current pointer and reader projection. Owner: caller proposes and identifies authority; code records acceptance and switches current authority transactionally. Computational/human contributions: advertised actor kind is human or owning-system; scope/source/actor/reason are caller-supplied, so this is not evidence of authenticated human approval. Accepted predecessors become superseded; rejected proposals remain in history; invalidation is a separate tool requiring evidence or impact input. Rollback/reconsideration uses successor/invalidation rather than editing accepted premises. Guidance: candidate premises, alternatives and authority event; persistent result is decision history, not modified application code. Mode: open scoped decisions; no expected-answer oracle established. SRC-1: `mcp-server/src/tools/decisions.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted/rejected revision payload.
- Later read-back: Decision and projection readers expose immutable history and current authority pointer.
- Delegated visibility: Portable projection exports decision custody; it does not independently transfer or authenticate decision authority.
- Selection predicate: Draft revision; acceptance scope must match the decision or exact revision identifier.
- Invalidation or expiry: Successor acceptance supersedes predecessor; invalidate tool can remove accepted authority and create review obligation.
- Activation or effect: Changes recorded decision authority, not by itself deployed product machinery.
- Evidence limits: Inspection establishes handler admission checks, not human identity, subsequent implementation or decision correctness.

> if (
>   auth.authorityScope !== revision.decision_id &&
>   auth.authorityScope !== `${revision.decision_id}:${revision.revision_id}`
> ) {
>   throw new ToolError("acceptance authority_scope does not cover this decision revision");
> }
> --- `mcp-server/src/tools/decisions.ts`

#### RT-RTE-policy-admission
Label: Qualified learning policy admission

Endpoints: completed-outcome extraction → immutable lesson proposal → qualification → staged version → verify/activate → active-policy reader. Owner: caller authors extraction, proposition, scope, configuration, metrics and evidence IDs; code computes directional minimum effect and admission checks. Channels separate corpus, retrieval, method, research and user preference. Preferences require the named human source's confirmation fields; this does not authenticate that person. Method staging additionally requires matching unattended-method qualification activation. Failed numerical score leaves the lesson a candidate; mismatched configuration/predecessor refuses staging; failed postactivation comparison throws inside a transaction. Rollback intent is retained in the proposed plan and successor lineage, not proof of an exercised rollback. Guidance and persisted result: typed lesson, evidence ledger, configuration, affected-future-run selector, events and readbacks. Mode: bounded qualification comparisons; metrics and reference values are supplied inputs, not independent answer-oracle execution. SRC-1: `mcp-server/src/tools/learning.ts`, `mcp-server/src/tools/crosswalk.ts`, `mcp-server/src/schema.sql`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Qualification report, staged version or active/readback result.
- Later read-back: `get_learning_policy` returns an active runtime representation only with successful postactivation readback; actual consumption by future agents is unobserved.
- Delegated visibility: Callers can fetch configuration and affected-future-run selector; no host scheduling or prompt injection is established by this reader.
- Selection predicate: Policy key, qualified candidate, matching configuration and active predecessor; method channel adds registry prerequisite.
- Invalidation or expiry: Successor activation supersedes prior lesson/policy; auditing appends mismatch evidence without itself replacing policy.
- Activation or effect: Transactionally changes the active database policy representation and checks it through the reader; no model parameters change in this code.
- Evidence limits: Self-improvement and improved capacity are not established: policy persistence/admission do not show later behavior causally depending on the change. Full crosswalk qualification and downstream consumers remain outside this bounded trace.

> const effect = expectedDirection === "increase" ? observed - baseline : baseline - observed;
> const passed = effect >= minimumEffect;
> --- `mcp-server/src/tools/learning.ts`

> post = readbackReport(expected, activePolicy(ctx, row.policy_key, false));
> if (!post.ok) throw new ToolError("activated learning policy failed next-run read-back");
> insertReadback(ctx, row.policy_version_id, "postactivation", post, actor);
> --- `mcp-server/src/tools/learning.ts`

### Claims

#### RT-CLM-autonomous-survey
Label: Autonomous phased survey claim

Claimed operation: coordinator runs inferred scope without per-phase human review gates, logs assumptions and surfaces checkpoints. This is a model-facing policy; deterministic tools enforce narrower record prerequisites. SRC-1: `.claude/skills/amanuensis/SKILL.md`.

> You **run autonomously by default.** Infer the narrowest complete scope from
> the user's request, then walk it end-to-end without review gates.
> --- `.claude/skills/amanuensis/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-phase-instructions
Label: Skill to host action

Consumer: coordinator and optional agents for survey Phases 1–4; the specialized packaging instructions address the coordinator alone. Channel: installed skill and selectively loaded reference Markdown. Force: interpreted instructions for routing, evidence and continuation; hard constraints in prose are policy, not a runtime sandbox. Horizon: session and repeated installed-skill invocations. SRC-1: `.claude/skills/amanuensis/SKILL.md`. Uses [RT-OBJ-amanuensis-skill](#rt-obj-amanuensis-skill) in [RT-RTE-survey-cycle](#rt-rte-survey-cycle).

#### RT-BAP-server-opening
Label: MCP opening to reader behavior

Consumer: connecting host model. Channel: server initialization instructions telling it to call `describe_locus` first, respect standing and bind the chat workspace. Force: model-interpreted guidance; tool binding is enforced separately by code. Horizon: host connection/session, with host injection behavior externally controlled. SRC-1: `mcp-server/src/index.ts`. Supports [RT-RTE-locus-read](#rt-rte-locus-read), not proof of answering compliance.

> "To learn what is recorded about a file, symbol, subsystem, or term, call describe_locus first."
> --- `mcp-server/src/index.ts`

## Annotations

none
