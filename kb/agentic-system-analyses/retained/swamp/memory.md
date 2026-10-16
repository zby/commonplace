---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Swamp memory: versioned automation data, retained plans and reviews, execution continuation, report retrieval and external-agent context limits."
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
source-identity: "https://github.com/swamp-club/swamp"
reviewed-boundary: "380e3c307164501c7d705f7707a864f4612b2785"
---

# Swamp memory report

## Boundary and evidence

Swamp retains automation definitions, typed outputs, run state and issue-lifecycle resources. Later consumers include deterministic executors, querying clients and external agents following skills. This is not an inspected implementation of an agent's conversation memory. The source and functional boundary remain those of [boundary](boundary.md#boundary-and-evidence): SRC-1 at commit `380e3c307164501c7d705f7707a864f4612b2785`. No external source, target execution, service call, evaluator result or causal experiment is added.

The runtime's launch, extension, workflow, approval and review accounts are supplied findings, not direct reads performed by this analyst. Direct inspection adds the following memory seams within SRC-1. Paths in the table are commit-relative anchors; references identify declarations or the supplied records carrying the related findings. Uninspected available code is not an access gap or evidence of absence.

| Entry point or operation | Source path and evidence basis | Coverage and limit |
| --- | --- | --- |
| CLI dispatch and data operations | Direct implementation: `src/cli/mod.ts`, `src/cli/commands/data.ts` | Data get/list/search/query/versions/gc/prune/rename/delete registered. [MEM-RTE-data-query](#mem-rte-data-query), [MEM-RTE-data-cleanup](#mem-rte-data-cleanup). Individual search/ranking and rename implementations not traced; no semantic-retrieval or exhaustive invalidation claim. |
| Resource/file write and method-local read | Direct implementation: `src/domain/models/in_process_executor.ts`, `src/domain/models/data_writer.ts`, `src/infrastructure/persistence/unified_data_repository.ts`, `src/domain/data/composite_data_repository.ts` | [MEM-RTE-resource-storage](#mem-rte-resource-storage). File payloads may be opaque bytes; schema warning is not rejection. Backend adapters and remote durability remain uninspected. |
| CEL query, projection, alternate read APIs | Direct implementation: `src/libswamp/data/query.ts`, `src/domain/data/data_query_service.ts`, `src/serve/handlers/data_handlers.ts`, `src/domain/models/in_process_executor.ts` | [MEM-RTE-data-query](#mem-rte-data-query). Method context exposes readResource, readModelData and queryData; detailed cross-model access and all server authorization branches uninspected. No universal access guarantee. |
| Issue acquisition, plan, iteration, findings and phases | Direct implementation/design: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/SKILL.md`, `.claude/skills/issue-lifecycle/references/planning.md`, `.claude/skills/issue-lifecycle/references/adversarial-review.md`, `.claude/skills/issue-lifecycle/references/implementation.md` | [MEM-RTE-plan-iteration](#mem-rte-plan-iteration), [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks). Detailed initial acquisition, classification, duplicate/linked-issue, notify, summary and remote lifecycle-post branches remain uninspected; these cannot be classified as automatic summarization or comprehensive knowledge revision. |
| Persistent checks and rejection | Direct implementation: `extensions/models/issue_lifecycle.ts` | Approval checks consume plan/review versions and unresolved severity; PR-link check consumes verification flags. [MEM-OBJ-review-findings](#mem-obj-review-findings), [MEM-OBJ-lifecycle-state](#mem-obj-lifecycle-state). Execution/skip policy beyond supplied runtime controls not exhaustively audited. |
| Trace-derived reports and later retrieval | Direct implementation: `src/domain/reports/report_execution_service.ts`, `src/domain/reports/builtin/method_summary_report.ts`, `src/libswamp/reports/get.ts` | [MEM-RTE-report-retrieval](#mem-rte-report-retrieval). Built-in method summary inspected; workflow/verification/custom report internals remain available but uninspected. No uniform semantic-content claim for all reports. |
| Activity summary command | Direct implementation: `src/cli/commands/summarise.ts`, `src/domain/summary/summary_service.ts`, `src/libswamp/summary/summarise.ts` | [MEM-RTE-activity-summary](#mem-rte-activity-summary). Computed display over retained history, not inspected conversation compaction. |
| Hooks and audit timeline | Direct implementation: `src/domain/repo/repo_service.ts`, `src/cli/commands/audit.ts`, `src/domain/audit/audit_service.ts`, `src/infrastructure/persistence/jsonl_audit_repository.ts`, `src/libswamp/audit/timeline.ts`; direct config: `.claude/settings.json` | [MEM-RTE-audit-timeline](#mem-rte-audit-timeline). Managed audit-hook template and later timeline traced, not every harness adapter or serve-audit sink. No complete tool transcript or trace-to-policy inference. |
| GC and ephemeral data | Direct implementation: `src/libswamp/models/run.ts`, `src/libswamp/data/gc.ts`, `src/domain/data/data_lifecycle_service.ts`, `src/libswamp/data/prune.ts`, `src/domain/data/data_delete_service.ts`, `src/domain/data/composite_data_repository.ts` | [MEM-RTE-data-cleanup](#mem-rte-data-cleanup). Run-artifact GC, datastore-wide GC and replication/tombstone convergence not fully inspected; remote erasure and universal retention guarantees prevented. |
| Evaluated workflow cache and replay | Direct implementation searches in `src/libswamp/workflows/evaluate.ts`, `src/libswamp/workflows/run.ts`; supplied [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run) | Expanded workflow is saved for last-evaluated replay; run plan, evaluated cache and authored workflow must remain distinct. Full cache invalidation and provenance validation not traced. |
| Launch briefs, skill maintenance, continuation | Supplied [RT-OBJ-task-brief](runtime.md#rt-obj-task-brief), [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions); direct hook-related `src/domain/repo/repo_service.ts` excerpts | Brief/session reload is established; external conversation selection/compaction remains opaque. Full instruction installation/upgrade conflict handling not independently re-inspected. |
| Registered executable capabilities | Supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), [RT-RTE-worker-dispatch](runtime.md#rt-rte-worker-dispatch), [RT-BAP-workflow-execution](runtime.md#rt-bap-workflow-execution) | Code/source, bundles and registry are not natural-language memories. Registry resolution supplies later executable authority; remote storage and all admission alternatives remain limited as in runtime. |
| Review/evaluation improvement consumers, dashboard/client | Supplied [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) and boundary coverage | Review return retained as shell/run output. Skill-eval generators, attestation posting, dashboard views and client presentation not independently traced end to end; cannot infer automated skill adoption or learning from scores. |

No material included responsibility is deliberately excluded from the memory inventory. Legal/branding exclusions remain unchanged. Host conversation storage, model weights, external vault/datastore internals and hosted Swamp Club implementation are outside frozen evidence. Their behavior is not supplied by local labels or adapters.

## Core ideas

1. **Data is versioned by behavior identity and data name.** Content bytes, ownership/tags/version metadata and query access are distinct. Later method code can consume JSON; later agents get only the command/display result selected for them. A stored plan is not automatically a prompt. [MEM-OBJ-data-content](#mem-obj-data-content), [MEM-RTE-data-query](#mem-rte-data-query).
2. **Issue progress survives through explicit resources and instructed reload.** Plans, feedback, findings and phase markers are saved by method calls. The skill asks later sessions to query the phase and follow the corresponding procedure. Swamp does not inspect the external agent's compliance. Plan review is a lossy display, and iteration's “all prior feedback” label exceeds its inspected repository enumeration. [MEM-RTE-plan-iteration](#mem-rte-plan-iteration), [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks).
3. **Some retained material has deterministic authority rather than advisory force.** A review's version and unresolved severity can reject approval; verification flags can reject PR linking. Those facts do not certify that the underlying prose or evaluation is correct, or that a human approved it. [MEM-BAP-retained-checks](#mem-bap-retained-checks).
4. **Trace-derived summaries are retrievable, but need not change future policy.** Built-in reports transform execution context into Markdown/JSON with data pointers. Activity summaries and audit timelines select prior records on request. None of these inspected chains establishes an automatic model-context push, a model-weight change or improved future capacity. [MEM-RTE-report-retrieval](#mem-rte-report-retrieval), [MEM-RTE-activity-summary](#mem-rte-activity-summary), [MEM-RTE-audit-timeline](#mem-rte-audit-timeline).
5. **Retention is conditional.** Infinite lifetime is distinct from unlimited version history. Resource policies, optional post-run GC, deletion and ephemeral routing can remove access to older content. Execution checkpoints support continuation, not necessarily semantic learning. [MEM-RTE-data-cleanup](#mem-rte-data-cleanup), [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-data-content
Label: Versioned resource and file content

Content bytes written through resource/file writers. Resources serialize JSON; files can contain text or opaque binary data. At deterministic JSON consumers the encoding is symbolic. Prose carried within a resource receives different authority when interpreted by an agent. The generic payload is not assigned a single semantic ontology. Local persistence uses version directories under `.swamp/data/{normalized-type}/{model-id}/{data-name}/`; metadata is YAML, with distinct content files, checksums and a latest marker. Metadata is access/provenance information, not the content itself. The composite repository routes ephemeral lifetime to an in-memory repository. SRC-1 implementation: `src/domain/models/data_writer.ts`, `src/infrastructure/persistence/unified_data_repository.ts`, `src/domain/data/composite_data_repository.ts`.

> return data.lifetime === "ephemeral" ? this.ephemeral : this.persistent;
> --- `src/domain/data/composite_data_repository.ts`

> const metadataContent = stringifyYaml(cleanData as Record<string, unknown>);
> await atomicWriteTextFile(metadataPath, metadataContent);
> --- `src/infrastructure/persistence/unified_data_repository.ts:1057-1058`

> await atomicWriteFile(contentPath, content);
> --- `src/infrastructure/persistence/unified_data_repository.ts:1068-1068`

Lineage depends on the producing method: externally acquired content, caller-authored material and execution traces are all possible; a generic writer does not establish source trust or trace origin. Supplied [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run) returns handles to these objects but does not declare the generic data substrate; [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run) instead denotes scheduler state. No counterpart after that comparison. The specialized issue/report objects below identify content with materially different consumers, not substitute names for all data.

#### MEM-OBJ-plan-main
Label: Issue implementation plan content

An issue-specific resource with version, summary, DDD analysis, ordered steps/file references, testing strategy, challenges, feedback strings and generation time. JSON fields provide symbolic addressing; descriptions and reasons are natural-language guidance for a human/agent. The resource persists through [MEM-OBJ-data-content](#mem-obj-data-content). Plan creation and iteration accept content from the caller; code does not generate or prove the plan. Lifetime is infinite but the declared version-count GC policy is 20. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`.

> feedbackIncorporated: allFeedback,
> --- `extensions/models/issue_lifecycle.ts`

The later `review` method logs version, summary, step descriptions and testing strategy, omitting DDD analysis, challenges, file lists, risks and feedback. Full JSON remains separately queryable. Thus retained rationale and displayed rationale differ. Plan-version numbers also feed deterministic review freshness checks. [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) is an approval route, not this object; this is distinct content used by it.

#### MEM-OBJ-feedback-main
Label: Issue feedback resource

Versioned JSON containing round, caller-supplied feedback text, reviewed plan version and timestamp, stored through [MEM-OBJ-data-content](#mem-obj-data-content). Feedback text is natural language at the agent's revision consumer; round and reviewed-version references are symbolic metadata. Origin is described as human by the argument schema, but the implementation authenticates neither author nor consent. The skill also permits adversarial findings as feedback, so mixed human/model origin is possible. Declared lifetime is infinite, version GC 20. SRC-1 implementation/design: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/references/adversarial-review.md`.

> --input feedback="<human's feedback or adversarial findings>" \
> --- `.claude/skills/issue-lifecycle/references/adversarial-review.md`

No supplied object counterpart: [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) concerns later approval. Feedback is neither the plan nor a successful revision certificate. Its downstream incorporation limit is in [MEM-RTE-plan-iteration](#mem-rte-plan-iteration).

#### MEM-OBJ-review-findings
Label: Adversarial and code conformance findings

Issue resources retain descriptions, severity/categories or deviations, identifiers, resolution notes and plan/version associations. Their prose is natural-language criticism at an agent/human consumer; unresolved flags, severity and version are symbolic at configured checks. Storage is versioned JSON through [MEM-OBJ-data-content](#mem-obj-data-content), with infinite lifetime and bounded version policies: adversarial review 20, code conformance 10. Both are caller-recorded findings, not direct code-computed proof. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`.

> return { ...f, resolved: true, resolutionNote: note };
> --- `extensions/models/issue_lifecycle.ts`

Resolution preserves descriptions and attaches a caller's explanation; it does not independently verify the plan was fixed. This material is distinct from external code-review shell output in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) and from the approval route [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission). Adversarial and conformance resources share caller-recording control but have different check targets; detailed conformance transformation remains less inspected than the adversarial path.

#### MEM-OBJ-lifecycle-state
Label: Issue phase and verification state

Symbolic JSON resources include `state-main` phase/issue/timestamp and `verificationResult-main` checklist results used by PR-link checks. They are not plan rationale. Storage uses [MEM-OBJ-data-content](#mem-obj-data-content); state has infinite lifetime/10-version policy, verification has infinite lifetime/5-version policy. They are distinct from generic workflow runs in [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run). The phase records progression; the skill's interpretation selects a later procedure. Verification flags enter a separate deterministic preflight check. SRC-1 implementation/design: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/SKILL.md`.

> if (!result.allPassed) {
> --- `extensions/models/issue_lifecycle.ts`

Checklist outcome origin depends on the caller; inspecting this consumer does not authenticate a corresponding executed test suite. Broader remote attestation validation is uninspected.

#### MEM-OBJ-method-report
Label: Method summary report representations

Derived method-execution account, persisted in separate Markdown and JSON file artifacts through the data repository. Markdown contains a narrative, error when present, argument names and output retrieval pointers. JSON additionally carries output specifications and structured data identities. These are distinct operative representations: readable display versus machine-addressable record; neither embeds the full output payload. They derive from execution status, definition, method, argument-key sets and handles, not model summarization of a conversation. SRC-1 implementation: `src/domain/reports/builtin/method_summary_report.ts`, `src/domain/reports/report_execution_service.ts`.

> // Build markdown — compact for human terminal display.
> // Schema lives in the JSON for agent retrieval.
> --- `src/domain/reports/builtin/method_summary_report.ts`

> // Arguments section — names only, never values (swamp-club#1746).
> --- `src/domain/reports/builtin/method_summary_report.ts`

The Markdown's prose receives authority only through interpretation; names, schema fields and retrieval pointers have symbolic consumers. Reports carry report-name/scope/owner tags; both artifacts have lifetime `30d` and GC count 5. A derived report does not inherit the complete information in original arguments or files. Closest supplied [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run) mentions report results but declares no report object; [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run) is not this report. No counterpart after comparison.

#### MEM-OBJ-command-audit
Label: Hook-captured command audit

Symbolic command-event records with command text, timestamp and available session/failure information, stored as date-partitioned JSONL at `.swamp/audit/commands-{YYYY-MM-DD}.jsonl`. These are selected raw command traces, not complete conversations or derived agent rules. The managed Pi template captures Bash tool command text and session/cwd, then calls audit recording after the tool result; it does not forward the whole tool result. Other harness normalization details are not exhaustively traced. Append failures are swallowed. SRC-1 implementation: `src/domain/repo/repo_service.ts`, `src/infrastructure/persistence/jsonl_audit_repository.ts`, `src/cli/commands/audit.ts`.

> const payload = JSON.stringify({
>   tool_name: "bash",
>   tool_input: { command },
>   cwd: ctx.cwd || ".",
>   session_id: ctx.sessionId,
> });
> --- `src/domain/repo/repo_service.ts`

This is not the task brief or workflow run already supplied by runtime. No supplied counterpart after comparison. Trace presence does not establish learning; [MEM-RTE-audit-timeline](#mem-rte-audit-timeline) establishes only later display.

### Routes

#### MEM-RTE-resource-storage
Label: Resource admission and method read-back

Method execution injects writers and readers; authored method calls select the resource name and body. The resource writer serializes data, applies declared policies/sensitive handling and delegates persistence. A later method invocation can call the injected reader with an instance name and optional version. SRC-1 implementation: `src/domain/models/in_process_executor.ts`, `src/domain/models/data_writer.ts`, `src/infrastructure/persistence/unified_data_repository.ts`. This is the storage/read capability underlying, not a replacement for, [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run). Concrete issue consumers are separately traced below; unspecified arbitrary callers do not establish additional consumer routes.

- Immediate return: Data handles with resource identity/version, or reader JSON object/null/error; file writer APIs return file handles rather than an inferred readable semantic summary.
- Later read-back: Known later method consumers include plan review, iteration, approval/checks and finding resolution. Generic readResource alone establishes a capability; these named consumers establish actual source wiring.
- Delegated visibility: Method receives data services; injected queryData/readModelData provide alternate access. External agent sees returned command output, not every field merely because a handle exists.
- Selection predicate: Resource spec must exist; instance name must be nonempty. Read selects current behavior/type/name and optional version; metadata resolution fixes the version used for content retrieval.
- Invalidation or expiry: Malformed stored JSON or a non-object JSON value throws; absent/empty content returns null. Version policies, deletion and ephemeral lifetime limit later availability.
- Activation or effect: Saves resource content and returns data to method code. This is implemented persistence/consumption, not observed model obedience.
- Evidence limits: Storage and remote-backend contracts, all file readers and all cross-model authorization branches are not audited; no run is observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Authorship belongs to method/caller; physical I/O belongs to writers/repository. Software admission rejects undeclared spec or invalid name, checks ownership in repository saves, and requires configured vault handling for sensitive fields. Resource schema failure emits a warning rather than rejecting content; this differs from runtime's method-argument `safeParse` gate. Human per-content approval is not generic writer behavior. This route stores open automation products, not a bounded learning curriculum, and supplies no answer oracle. Recovery depends on deferred writes for methods declaring rollback and on caller repair/retry; this is not rollback of arbitrary external effects. SRC-1: `src/domain/models/data_writer.ts`, `src/domain/models/in_process_executor.ts`, `src/infrastructure/persistence/unified_data_repository.ts`.

> // Validate data against schema (warn on failure, don't throw)
> const validationResult = spec.schema.safeParse(data);
> --- `src/domain/models/data_writer.ts`

> const resolvedVersion = dataRecord?.version;
> --- `src/domain/models/data_writer.ts`

Sensitive fields can be replaced by vault expressions on write and resolved only at tagged/schema-sensitive paths on method read; the reader also registers resolved secrets for redaction. Stored references and actual secret bytes are not the same object. A plain data display must not be assumed to reconstruct the method reader's secret-bearing object. SRC-1: `src/domain/models/data_writer.ts`.

#### MEM-RTE-data-query
Label: Requested data query and projection

Caller requests a CEL predicate with optional select/limit; libswamp invokes the query service, which uses catalog metadata and content as needed, applies filters/projection and returns matching records/values. Server handler invokes the same generator with caller visibility filtering. This is independent read-back of retained data, not automatic context supply. SRC-1 implementation: `src/libswamp/data/query.ts`, `src/domain/data/data_query_service.ts`, `src/serve/handlers/data_handlers.ts`, `src/cli/commands/data.ts`. Closest supplied [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run) produces data; this route requests it later rather than executing a behavior.

- Immediate return: Match/projected-match events and completed counts/shape; single-result requests error if zero or multiple results.
- Later read-back: CLI/server clients, including agents invoking the issue skill's state query, receive selected retained fields. The consumer role is explicit; actual agent use remains unobserved.
- Delegated visibility: Query returns records or projected values, not the whole repository. Server include filtering precedes projection and result budgeting in the inspected handler.
- Selection predicate: CEL metadata/content predicate, namespace/owner context and optional select expression; default latest-only filter unless history is opened. Optional latest-per-step behavior belongs to CEL collection helper paths, not every CLI query.
- Invalidation or expiry: Missing/stale rows, deletion, rename forwarding and removed versions affect availability. Full replication and rename alternatives remain uninspected.
- Activation or effect: Delivers requested data for caller interpretation or computation; it does not grant retrieved text instruction priority.
- Evidence limits: No observed query, no universal token budget, and no exhaustive authorization or search-ranking assessment. Unlimited result count can exceed an external host's window.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Unlimited by default — callers pass an explicit limit when they
> // need a cap.
> --- `src/libswamp/data/query.ts`

> if (!opensHistory) {
>   whereClauses.push(latestPerStep ? "is_step_latest = ?" : "is_latest = ?");
>   whereParams.push(1);
> }
> --- `src/domain/data/data_query_service.ts`

The displayed projection can omit provenance/reasons even when retained content contains them. JSON `content` is aliased to attributes; binary content has a distinct encoding/error path, not an automatic natural-language summary. Metadata predicates and count caps are selection, not evidence of semantic similarity retrieval. SRC-1: `src/domain/data/data_query_service.ts`.

#### MEM-RTE-plan-iteration
Label: Issue plan revision and feedback retention

Agent/caller submits a plan or revised plan plus feedback through a behavior method. Code loads the current plan, gathers feedback entries, stores feedback and a new plan, and resets phase to plan_generated; remote lifecycle posting is attempted separately. Later review/iteration methods reload resources. The skill asks the agent to re-read, criticize, revise and present changes. SRC-1 implementation/design: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/references/adversarial-review.md`. This revises content; [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) instead admits implementation by approval. Neither replaces the other.

- Immediate return: Data handles/logged version and lifecycle-post outcome, or error. `review` returns no data handles and logs a selected display.
- Later read-back: Next iterate reads plan version and feedback; review reads a requested/current plan. Agent-followed implementation is instructed to follow the approved plan, but source wiring does not prove model use.
- Delegated visibility: Caller authors revised substantive fields. Review display retains summary, step descriptions and testing strategy but omits other plan fields; query can retrieve full content.
- Selection predicate: Named issue behavior, plan-main with optional review version, feedback-main entries found through findAllForModel. Skill selects codebase files and issue-scoped temporary inputs; there is no inspected token-level context scheduler.
- Invalidation or expiry: New plan version makes prior review stale at the configured approval check. Version GC may remove older resources. Recalling start is explicitly warned against because it resets phase.
- Activation or effect: Persists caller revisions and feedback for later reads; does not compute semantic incorporation or verify the caller's criticism.
- Evidence limits: Full feedback history is not reconstructed by the inspected enumeration; no actual criticism/revision episode or beneficial learning is supplied. Remote posting is not a transaction guarantee.
- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected

The method says “incorporating all prior feedback”, but its loop uses `findAllForModel`, filters by one name, and reads only each returned entry.version. The persistent implementation returns latest data per name, not all versions. Therefore the next `feedbackIncorporated` array receives the latest feedback entry plus the new string, not necessarily every previous round; with one existing feedback name, `feedbackRound = feedbackEntries.length + 1` does not count historical versions. This is a source-supported counterexample to complete history accumulation, even though old versions can remain physically retained. SRC-1: `extensions/models/issue_lifecycle.ts`, `src/infrastructure/persistence/unified_data_repository.ts`.

> const feedbackEntries = allData.filter((d) =>
>   d.name === "feedback-main"
> );
> const feedbackRound = feedbackEntries.length + 1;
> --- `extensions/models/issue_lifecycle.ts`

> /**
>  * The latest data of each name under a model, following rename forwards.
>  * Each rename marker followed is pushed to `renames` when given.
>  */
> --- `src/infrastructure/persistence/unified_data_repository.ts`

Proposal/guidance: caller supplies summary, analysis, steps, testing and challenges under planning conventions; the skill supplies criticism dimensions and a human feedback loop. Computational admission checks argument structure and configured preflight rules; the storage layer itself does not establish plan truth. Human presentation, editing and explicit approval are instructed, not authenticated by iterate. Rejection can occur at execution checks/errors and later approval; rollbackOnFailure is declared for the local method, with runtime's remote limitation. Operating mode is open issue work; no expected-answer oracle is supplied.

This is a route for explicit plan/criticism retention, not evidence that every plan is a formulated explanatory theory. Localized inspectable fields and caller revision are supported. Consumption by the deterministic version check is established separately; content-directed model criticism, repeated content-dependent action and improved capacity require an episode or narrower warranted assessment, not the method name. Retained feedback/reasons can guide a later caller, but the implementation does not perform the critique or substantive revision itself.

#### MEM-RTE-lifecycle-checks
Label: Retained lifecycle checks and session reload

Two consumer paths use retained issue state: code preflight checks approval/linking, and the skill instructs later agents to query phase and select a procedure. Criticism is recorded by adversarial_review; resolve_findings reads the stored review and annotates matching finding IDs with caller notes. SRC-1 implementation/design: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/SKILL.md`, `.claude/skills/issue-lifecycle/references/adversarial-review.md`. This adds retained-input detail to, but does not redeclare, [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission); its checks are a distinct preflight consumer, while approval's external-consent limit remains.

- Immediate return: Check pass/failure with reasons; finding/revision handles; requested phase JSON and a prescribed next procedure.
- Later read-back: Approval check loads plan-main and adversarialReview-main; PR-link check loads verificationResult-main. Later-session skill reads state-main phase. These consumers are code-wired or instructed separately.
- Delegated visibility: Check reads version, severity/resolution or verification flags; agent receives queried phase and routed instructions. Neither receives proof of conversation consent from these fields.
- Selection predicate: Target method's appliesTo check, exact resource names, matching plan/review versions, critical/high unresolved findings and allPassed verification flag. Session route uses issue behavior identity and latest state.
- Invalidation or expiry: Missing review/plan or stale review version fails configured approval preflight; unresolved critical/high findings fail; no or failed verification fails PR-link check. New stored flags can change the next result.
- Activation or effect: Code can reject the configured operation based on retained state; natural-language phase routing asks the external agent to change procedure. Source proves control capacity, not its exercise in a run.
- Evidence limits: Check bypass/selection controls and remote execution differences remain as in runtime; caller-supplied flags/notes do not validate real-world remediation or executed verification.
- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected

> if (review.planVersion !== plan.version) {
> --- `extensions/models/issue_lifecycle.ts:906-906`

> const unresolved = review.findings.filter(
>   (f) =>
>     !f.resolved &&
>     (f.severity === "critical" || f.severity === "high"),
> );
> --- `extensions/models/issue_lifecycle.ts`

> **Persist everything through the model.** Don't just have a conversation —
> call the model methods so state survives context compression and sessions.
> --- `.claude/skills/issue-lifecycle/SKILL.md`

Proposer is the caller recording findings/results; software decides schema/preflight admissibility, intended human decides plan consent, and an external agent chooses whether to follow the skill. Resolution/replacement is explicitly available; caller notes can revise reliance without deleting criticism text. Recovery is revision/re-review/re-verification and retry, not proof of actual correction. The reference procedure supplies architecture/scope/risk/testing/complexity/correctness/documentation guidance. Operating mode is open issue progression; no independent reference-answer oracle for plan correctness is established. This is structured state-dependent admission, not automatic truth maintenance.

#### MEM-RTE-report-retrieval
Label: Execution report derivation and later retrieval

Report selection chooses registered reports for scope/method; report code receives execution context and returns Markdown/JSON. The service persists both and later report get selects stored Markdown by tags, owner/workflow, version and variant; JSON and underlying outputs remain data-queryable. SRC-1 implementation: `src/domain/reports/report_execution_service.ts`, `src/domain/reports/builtin/method_summary_report.ts`, `src/libswamp/reports/get.ts`. This is distinct from [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict), whose reviewer prose is a shell output, and from [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run), whose execution context supplies these reports.

- Immediate return: Report events, Markdown/JSON, handles or failures; empty Markdown announces completion without saving a new version.
- Later read-back: reportGet is a shipped CLI/library consumer of saved report content; agents may query JSON via retained data pointers. Built-in output pointers identify later retrieval commands, not inline payload copies.
- Delegated visibility: Human display is compact Markdown; JSON includes schema/data pointers. No full execution conversation is sent to a model by this report code.
- Selection predicate: Scope/report selection and method/type filters at derivation; report-name tags, owner/workflow, variant/version and optional caller include at retrieval.
- Invalidation or expiry: Both report artifacts declare 30d lifetime and five-version GC. Empty/nonapplicable report preserves previous real latest version; failure-report paths do not certify prior success is current.
- Activation or effect: Persists derived summaries and delivers selected stored content. No automatic future policy update or verified downstream model use is established.
- Evidence limits: All custom/workflow report semantics, full report-get ambiguity handling and remote consumer authorization are not exhaustively inspected; no run or benefit evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Empty markdown means the report is not applicable to this method.
> // Skip persistence so the previous real version stays latest, but still
> // announce completion so renderers can show it in verbose mode.
> --- `src/domain/reports/report_execution_service.ts`

> name: baseName,
> specName: "report",
> kind: "file",
> contentType: "text/markdown",
> lifetime: "30d",
> garbageCollection: 5,
> tags: { ...tags },
> --- `src/domain/reports/report_execution_service.ts`

The raw-to-derived chain is execution context/handles → deterministic built-in narrative and pointers → stored Markdown/JSON → requested report/data consumer. Automatic authorship and persistence are software-controlled; starting the method is not per-report human approval. Registered report code shapes the derivation, and software can skip persistence or record failures. Correctness of narrative content is not checked by a known-answer oracle. No separate human curation or trace-fed behavioral improvement is demonstrated; loss of argument values is deliberate, not a conversation summary retaining all reasons.

#### MEM-RTE-data-cleanup
Label: Data lifecycle and history removal

Explicit data GC/prune/delete operations and optional post-method autoGc remove expired entries, older versions or orphaned data. Lifetime policies, owning run existence and version policies determine software selection; caller controls invocation/dry run, not necessarily every deleted byte. SRC-1 implementation: `src/domain/data/data_lifecycle_service.ts`, `src/libswamp/data/gc.ts`, `src/libswamp/data/prune.ts`, `src/domain/data/data_delete_service.ts`, `src/libswamp/models/run.ts`. This is distinct from execution recovery in [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run).

- Immediate return: Counts/previews/deletion results; autoGc failures are caught and do not fail the method run.
- Later read-back: Later resource/query/report consumers depend on surviving versions; deleted data is not a semantic rejection notice automatically delivered to an agent.
- Delegated visibility: CLI reports removal statistics; no inspected model compaction summary replaces removed content.
- Selection predicate: Duration expiry, missing owning workflow run for workflow/job lifetime, version-count policy, explicit deletion target or orphaned definition lookup. AutoGc is guarded by input.autoGc after completed output.
- Invalidation or expiry: Infinite duration never expires by time, but version GC can still prune history. Missing workflow/run identifiers cause a warning and non-expiry in the inspected lifetime check. Ephemeral data uses separate memory storage.
- Activation or effect: Removes data/versions through repositories, altering future availability. This is mechanical retention, not truth evaluation or content-directed forgetting.
- Evidence limits: Full run/data-artifact GC interactions, synchronization/tombstone durability and recoverability after deletion are uninspected; no secure remote-erasure claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (input.autoGc) {
>   yield { kind: "auto_gc_started" };
> --- `src/libswamp/models/run.ts`

> return workflowRun === null; // Expired if workflow run is deleted
> --- `src/domain/data/data_lifecycle_service.ts`

Admission is software policy/caller deletion selection. Human per-content adjudication is unresolved, not inferred from a command being run. Explicit commands expose dry runs/previews; runtime rollback of deferred writes is a different mechanism from history GC. The inspected cleanup produces no derived guidance, contradiction record or learning product. Deleting a failed result can reduce later evidence even if it changes no claim.

#### MEM-RTE-audit-timeline
Label: Hook command capture and requested audit timeline

Installed audit adapters send selected tool events to audit record; normalized command entries append to local JSONL. Timeline requests read a time range, filter session/diagnostics/noise, categorize Swamp versus direct commands and return chronological entries. SRC-1 implementation: `src/domain/repo/repo_service.ts`, `src/cli/commands/audit.ts`, `src/infrastructure/persistence/jsonl_audit_repository.ts`, `src/domain/audit/audit_service.ts`, `src/libswamp/audit/timeline.ts`. No supplied route counterpart; [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch) starts an agent, whereas this records selected later tool activity.

- Immediate return: Silent/best-effort recording; later timeline command returns timeline/no-data/tool-not-supported.
- Later read-back: auditTimeline and AuditService are concrete later consumers of command logs. No inspected route automatically transforms their result into an agent rule or skill.
- Delegated visibility: Timeline display contains selected command events, not complete tool payloads or conversation reasoning. Pi managed template passes command/cwd/session only; other adapter detail remains less inspected.
- Selection predicate: Initialized-repository resolution on append; requested hour window/session, includeDiagnostic and showAll/noise prefix filtering on read; chronological sorting.
- Invalidation or expiry: Default audit retention constant is seven days, with old-data cleanup requested after append. Malformed JSONL lines are skipped; append errors can silently lose rows. Codex timeline returns tool_not_supported in this path.
- Activation or effect: Persists selected raw traces and produces an on-demand categorized view; no exercised future behavioral update is established.
- Evidence limits: Every harness hook, complete failure metadata and server audit sink retention are not traced; no operational completeness or causal learning evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!options.showAll && isNoiseCommand(trimmedCommand)) {
>   continue;
> }
> --- `src/domain/audit/audit_service.ts`

> const DEFAULT_RETENTION_DAYS = 7;
> --- `src/domain/audit/audit_service.ts`

The selector changes access/display, not the meaning of retained commands. Software admits normalized events automatically; human editing or approving individual records is not established. Audit metadata does not prove real-world success of commands or source credibility. This route cannot be classified as trace-fed improvement merely because its inputs are traces.

#### MEM-RTE-activity-summary
Label: Requested activity summary

CLI summarise resolves a time window and calls SummaryService over persisted method outputs, workflow runs and data metadata; the service groups and counts these records and returns an activity overview. SRC-1 implementation: `src/cli/commands/summarise.ts`, `src/domain/summary/summary_service.ts`, `src/libswamp/summary/summarise.ts`. Unlike [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run), this later consumer reports on retained history instead of scheduling work.

- Immediate return: Activity summary/no-activity result rendered for caller; no inspected write of a replacement conversation summary.
- Later read-back: Source history is read at each requested summary invocation. No inspected later consumer reloads a persisted version of this computed display.
- Delegated visibility: Grouped method/workflow run detail and data counts, not full outputs or reasoning traces.
- Selection predicate: CLI since defaults to 7d; explicit positive integer limit caps per-group most-recent run details, while counts reflect all matching runs in the time window.
- Invalidation or expiry: Future requests see surviving history and current cutoff. Detail truncation is marked, not equivalent to data deletion.
- Activation or effect: Returns a compact display; subsequent model action depends on an external caller choosing to use it.
- Evidence limits: No model-generated compaction, automatic context push or durable policy update follows from this route. No observed use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> *   ALL matching runs in the window — `limit` only bounds the detail
> *   array. When truncation occurs, the group's optional `truncated` flag
> *   is set to `true`.
> --- `src/domain/summary/summary_service.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-checks
Label: Retained finding and verification authority

Consumer: configured issue preflight checks. Channel: plan/review JSON version references, finding severity/resolution flags and verification allPassed state. Force: code rejects approval or PR linking when its predicates fail. Horizon: later method invocation while retained resource remains current/available. This is not general authority of the review prose over all host actions, and it does not establish human authorization. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`; supporting passages in [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks). Closest supplied [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions) is natural-language authority; [RT-BAP-workflow-execution](runtime.md#rt-bap-workflow-execution) is generic authored execution, not this retained-check input path.

## Annotations

#### On [RT-OBJ-task-brief](runtime.md#rt-obj-task-brief)

Memory consumers: initial external agent is asked to read the named Markdown; later task resume reloads task/session state, while brief remains unchanged. The task-to-conversation association is not a proven Swamp-managed semantic selector. Full conversation read-back, token budget and summary are external. Storage and source passage are supplied by the cited record and [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch); no new object is declared for the same brief.

#### On [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run)

Memory consumer: scheduler continuation reads saved symbolic progress and plan/checkpoint state on a later invocation. This is durable execution memory rather than transformed agent instructions. Run, captured evaluated plan, authored workflow and last-evaluated cache are distinct. The latter cache is explicitly saved for replay after expression/forEach expansion; complete invalidation logic is uninspected. SRC-1 implementation: `src/libswamp/workflows/evaluate.ts`, `src/libswamp/workflows/run.ts`; execution/reload passages are supplied in [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run).

> // Save the expanded workflow (forEach resolved, expressions evaluated)
> // so --last-evaluated can run without inputs or further expansion
> --- `src/libswamp/workflows/evaluate.ts`

This creates an alternate retained input form; it is not a summary of the external agent's working window. No claim that replay always re-derives current source is warranted.

#### On [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict)

Working-context control: deterministic driver starts a separate review process with prompt/diff pointer and selected read tools, keeping the caller's full conversation out of that task frame. What crosses back is reviewer prose in shell output and parsed verdict; temporary files are removed while outputs/run records persist. This resembles an isolated task frame returning a result, but no Swamp-managed token window, discarded-turn summary or model-context liveness mechanism is established. Host compaction and provider persistence remain external, as the supplied route and [RT-CMP-agent-models](runtime.md#rt-cmp-agent-models) state. Persistence of reviewer prose is not a source-code update or an automatic adoption of revised skills.

## Write side

**Acquisition and authored material.** Generic methods may write arbitrary declared resources or file content. Issue methods specialize this into context, plans, feedback, findings and phase/result resources. Authorship is caller/agent/human-dependent; code performs serialization, version allocation and physical I/O. Generic caller identity leaves per-content human control unresolved. Schema-shaped arguments do not make recorded conclusions true; resource schemas warn rather than reject. Sensitive field vault replacement is a separate transformation with a later method-reader reconstruction path. [MEM-RTE-resource-storage](#mem-rte-resource-storage).

**Revision and reasons.** Issue plan revision accepts already revised fields and feedback; it does not use a model internally to infer a better plan. Criticism and resolution notes can persist, while the ordinary review display omits several rationale-bearing fields. The inspected iteration's newest-feedback enumeration does not reconstruct all historical feedback. Re-reading full resource JSON, not merely display logs, is necessary to receive those retained parts. The skill asks agents to inspect code and conventions, re-run adversarial review and obtain human feedback. These are design instructions with an implemented recording surface, not observed revisions. [MEM-RTE-plan-iteration](#mem-rte-plan-iteration), [MEM-OBJ-review-findings](#mem-obj-review-findings).

**Automatic trace transformations.** Method reports derive from execution context and handles into persisted summaries/pointers, then report/data-get routes expose them later. Audit logs retain selected command events; timeline categorization and activity aggregation are requested views, not retained behavioral rules. Raw logging alone is insufficient for a trace-fed capacity-improvement claim. Report Markdown/JSON have known field losses, and opaque file bytes are not interchangeable with either. [MEM-RTE-report-retrieval](#mem-rte-report-retrieval), [MEM-RTE-audit-timeline](#mem-rte-audit-timeline), [MEM-RTE-activity-summary](#mem-rte-activity-summary).

**Rejection and withdrawal.** Configured lifecycle checks can reject stale/unresolved review or failed verification state. resolve_findings adds resolution flags/notes; new plan versions stale old reviews. Data deletion, duration/version GC and orphan pruning withdraw availability mechanically, without evaluating truth or recording a semantic retraction. A failed/empty report is not necessarily a replacement for the previous latest meaningful report. Explicit human consent remains policy at the external-agent conversation boundary, not an invariant of stored flags. [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks), [MEM-RTE-data-cleanup](#mem-rte-data-cleanup), [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission).

**Executable updates.** Authored definitions, evaluated plans and extension code are behavior-shaping retained material with symbolic execution consumers. Extension bundling/import/registration and local refresh are capability admission, separate from plan feedback and raw traces; structural validation is not universal safety review. Runtime establishes source refresh and later type resolution but not automatic trace-driven code adoption. [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), [RT-BAP-workflow-execution](runtime.md#rt-bap-workflow-execution).

## Read-back

Requests dominate the inspected memory paths: query/get by predicate or identity, method reads of exact resource names, explicit resume and report/timeline/activity requests. No report-wide unsolicited memory-injection mechanism is inferred. Selectors are concrete: issue and data names, version/latest markers, CEL fields/projections, method check targets, report tags and time windows. Resource display pointers can make more content reachable, but a pointer is not the content in the current model window. [MEM-RTE-data-query](#mem-rte-data-query), [MEM-RTE-report-retrieval](#mem-rte-report-retrieval).

The issue-session reload is explicitly instructed, not automatically pushed: query state-main, inspect phase, follow a linked procedure. Full plan guidance reaches a later agent only if it reads the relevant retained parts. The implementation reference says “Follow the approved plan step by step”; it does not itself embed all plan content into a launch prompt. SRC-1 design: `.claude/skills/issue-lifecycle/SKILL.md`, `.claude/skills/issue-lifecycle/references/implementation.md`; [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks).

> Follow the approved plan step by step.
> --- `.claude/skills/issue-lifecycle/references/implementation.md`

Budgets are result/detail counts, not inspected model-token budgets. Data query is unlimited by default; optional projection can narrow fields. Activity summary caps run details without changing counts. Method reports deliberately omit argument values and point to data. Nothing here proves host context fit or sufficient recall. [MEM-RTE-data-query](#mem-rte-data-query), [MEM-OBJ-method-report](#mem-obj-method-report), [MEM-RTE-activity-summary](#mem-rte-activity-summary).

Working-context control has three bounded surfaces: a named task brief instead of all tasks, separate review-process inputs/output, and instruction-driven state reload after sessions. Swamp's audit hooks record tool activity; their presence does not establish a compaction hook. The skill's reference to surviving context compression describes why to persist state, not an implementation of compression. External harnesses own their actual trimming, summary, window, continuation and tool-result inclusion. Supplied [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict); direct SRC-1: `src/domain/repo/repo_service.ts`, `.claude/skills/issue-lifecycle/SKILL.md`.

## Integration issues

1. **Supplied approval account needs a narrower reading.** [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) correctly says the approve method takes empty arguments and cannot authenticate conversational consent. It does not mention the separate configured adversarial-review preflight, which rejects missing/stale reviews and unresolved critical/high findings. Add [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks) and [MEM-BAP-retained-checks](#mem-bap-retained-checks) when reconciling; do not replace the consent limitation with a claim of verified human approval. SRC-1: `extensions/models/issue_lifecycle.ts`.
2. **All-prior-feedback claim does not hold for the inspected repository route.** [MEM-RTE-plan-iteration](#mem-rte-plan-iteration) compares the extension's enumeration with latest-per-name findAllForModel. Consequently retained old versions do not imply all their text reaches feedbackIncorporated, and feedback round can cease counting actual iterations. This qualifies source-native naming rather than correcting a supplied assertion. Alternative backend enumeration semantics are uninspected; no universal deployed failure is claimed. SRC-1: `extensions/models/issue_lifecycle.ts`, `src/infrastructure/persistence/unified_data_repository.ts`.
3. **Content display is not complete read-back.** [MEM-OBJ-plan-main](#mem-obj-plan-main) and [MEM-RTE-plan-iteration](#mem-rte-plan-iteration) distinguish full stored plan from review's selected log fields. [MEM-OBJ-method-report](#mem-obj-method-report) distinguishes compact Markdown, structured JSON and underlying opaque outputs. Reconciliation should not infer rationale delivery from retention or from a report label. SRC-1: `extensions/models/issue_lifecycle.ts`, `src/domain/reports/builtin/method_summary_report.ts`.
4. **Potential cross-member overlaps.** No new record duplicates a supplied referent after comparison: issue object records are content consumed by the supplied approval route, generic data storage underlies behavior outputs, report derivation differs from execution/reviewer verdict, and lifecycle checks differ from approve's state mutation. [MEM-RTE-lifecycle-checks](#mem-rte-lifecycle-checks) overlaps the broader approval narrative but is not a replacement route. Epistemic/workflow records are not supplied; those specialists may independently declare plans, findings, checks or report routes. Preserve material content/check distinctions rather than merging by label. Closest supplied links are retained in each declaration.
5. **Unresolved feedback source and actual criticism.** Feedback schema says human; reference instructions permit adversarial findings. Caller authorship and semantic incorporation are not authenticated. No inspected episode closes content-directed criticism, retained revision and later model dependence. This prevents bundling persistence, learning, reflection, autonomy or self-improvement into one conclusion. [MEM-OBJ-feedback-main](#mem-obj-feedback-main), [MEM-RTE-plan-iteration](#mem-rte-plan-iteration).
6. **Remaining included parts and prevented conclusions.** Full cache invalidation/provenance, cross-model authorization, every report implementation, run-artifact/datastore GC, replicated deletion, all hook adapters/serve audit sinks, full acquisition/classification/notification/summary consumers, evaluation-to-attestation-to-adoption, and dashboard/client displays remain uninspected at the paths named in the coverage table. They prevent exhaustive memory coverage, universal lifecycle/erasure guarantees, uniform source-trust classifications and an automatic improvement claim. They are available detail, not evidence of absence or inaccessible source. Known resource, report and check positives remain valid beside these limits.

## Limitations and checks

Source identity was rechecked with Git: HEAD equals the boundary revision and status was clean before direct inspection. Direct reads/searches stayed within SRC-1; supplied runtime findings were kept separate. Invocation/type/worker/records contracts were read completely; target programs, tests, providers and evaluators were not run. No additional source register entry is needed. The deterministic output validator checks structure, references and quotation occurrence, not semantic support or observed operation.

No source text establishes recall quality, actual human attention, semantic correctness of plan/review flags, remote durability or beneficial learning. No general absence of memory, criticism or model learning is asserted. The inspected routes support persistent content, selective read-back and configured symbolic authority; stronger outcomes remain unobserved.

Validation: the invocation-specific validate-output check passed after writing this report.
