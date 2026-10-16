---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Dense-Mem runtime baseline: authenticated Remember, session intake, bounded recall and automatic and manager-controlled maintenance at bd736450454e237f1ab6d138f4ae9755916d73f6."
run-id: AAS-2026-10-15-dense-mem-1a314bed9a5c-01
reviewed-boundary: bd736450454e237f1ab6d138f4ae9755916d73f6
---

# Dense-Mem runtime report

## Runtime account

### Responsibility and evidence

Dense-Mem is a memory service, not the enclosing agent's conversational controller. It accepts evidence and proposed relationships, performs bounded model-assisted interpretation, commits authorized knowledge and search state, and returns selected context. The host still chooses when to call it and what to do with its results. The [boundary](boundary.md#boundary-and-evidence) fixes the whole-system source boundary. This report uses SRC-1 implementation and target-authored doctrine at that revision, not supplied execution traces. No target code, example, test, provider or service was run. All operational activation and benefits remain unobserved.

Added implementation inspection beyond the boundary's initial reads covers the registry Remember binding; protected and user-portal routing; synchronous preparation, processor replay and assessment-session loops; provider repair/history and transport construction; session extraction; ontology automatic and manager services and organization context selection; conflict review service/runner; evaluation scoring dispatch; and production evaluation-tool exclusion. Paths appear beside the findings below. These are additional inspections of SRC-1, not new sources. Detailed storage/lifecycle revision semantics remain for the memory analyst; this report identifies runtime admission and alternate consumers without asserting a complete memory-policy audit.

### Ordinary shipped invocation

The production driver starts the composed server, not a free-running task agent. `cmd/server/main.go`, `cmd/internal/serverapp/bootstrap.go` and `cmd/internal/serverapp/server.go` compose PostgreSQL repositories, service applications, MCP/browser interfaces and workers (SRC-1; see boundary). The Python example supplies a concrete ordinary principal: a client configured by endpoint and token sends evidence, one proposed relationship and an idempotency key. It repeats Remember, calls recall and traces returned relationship handles. These calls are shipped usage, not an observed successful episode (SRC-1, `packages/python/examples/remember.py`).

The ordinary path is [RT-RTE-remember-intake](#rt-rte-remember-intake), then [RT-RTE-recall-context](#rt-rte-recall-context). HTTP authentication, team resolution/authorization, usage recording, rate limiting and credential activity precede `/mcp` and `/teams/:teamId/mcp`. MCP resolves an existing registry tool, checks runtime visibility and scopes, validates contract arguments, and invokes it with fixed team context. The registry reconstructs the request and maps success or typed terminal failure back to MCP text plus structured content. These are transport/application controls, not isolation of the host or proof that supplied evidence is true (SRC-1, `internal/http/router_protected.go`, `internal/mcp/server.go`, `internal/tools/registry/remember_bindings.go`).

Inside Remember, actor team/owner IDs and memory-space generation, content limits, evidence coverage and idempotency are checked. Code scans input; a security rejection must be audited and the processor rejects before semantic preparation. Code, not the model, owns progression: durable-attempt lookup; duplicate embedding planning and selection; assessment with server-owned context; bounded validation/repair; final embedding planning; fenced database commit; terminal result projection. Natural-language evidence reaches a remote model through JSON/system messages; symbolic identifiers, bounds, validation results and admission decisions constrain its response. Embeddings come from a separate numerical provider. The model proposes semantic decisions; software can reject them. No per-item human approval is required by this inspected intake path, and a generic authenticated caller does not establish human authorship or approval (SRC-1, `internal/remember/service/service.go`, `internal/remember/service/processor/remember_processor.go`, `internal/remember/service/processor/remember_preparation.go`).

The result distinguishes processing/search outcomes, evidence dispositions, relationship results and errors; successful response delivery is not proof of later host use. The example's explicit second call challenges any account that every request repeats provider work. Completed or non-retryable terminal attempts replay, a changed body under the same key conflicts, waiters load the owner's durable outcome, and a later call can retry a retryable failure. An optional application-level lock is not the final duplicate fence: the PostgreSQL commit independently locks the idempotency key and duplicate keys (SRC-1, `internal/remember/service/processor/remember_processor.go`, `internal/knowledge/postgres/remember_commit.go`).

### Four forcing cases and guarantee scope

1. **Replay/concurrency:** the processor can be constructed with a ledger lacking its optional outer lock. Consequently the outer lock cannot establish a universal single-provider-call guarantee. Production commit has transaction-level fences, but these establish accepted-write/replay control rather than exactly-once provider execution. Owner-result success can survive lock-cleanup failure. See [RT-CLM-commit-fences](#rt-clm-commit-fences).
2. **Session intake:** [RT-RTE-session-intake](#rt-rte-session-intake) stages raw sessions before extraction, unlike direct Remember's accepted-write transaction. It uses a private write scope, extraction/linking and shared semantic preparation, but its own repository commit. Thus the direct Remember comment about no pre-provider ingest/evidence/placement/attempt rows must not be generalized to all retained intake. It also has different working-context control: windowed inputs and complete regeneration without accumulating invalid assistant responses (SRC-1, `internal/session/service/service.go`, `internal/session/extraction/provider.go`).
3. **Automatic versus manager admission:** [RT-RTE-ontology-maintenance](#rt-rte-ontology-maintenance) is a background principal with leases, policy windows and attempt accounting. It can publish derived organization without a manager approving each item; some locked decisions bypass the model. [RT-RTE-manager-publication](#rt-rte-manager-publication) instead requires manager identity, grant and audit availability and exposes draft publication/discard and rollback. Manager-only checks do not protect the automatic route, which has its own admission boundary. Conflict review is another automatic change route, not a manager draft or ordinary Remember call.
4. **Recall degradation:** recall need not fail simply because some evidence vectors fail. It returns explicit degradations and distinguishes evidence, relationships and derived community discovery. Private branches do not inherit shared graph/community expansion. A portal can reach recall without going through MCP tool validation; it has its own HTTP auth/scope/team chain. See [RT-RTE-recall-context](#rt-rte-recall-context).

A load-bearing guarantee needs a narrower scope than “the system is safe”:

| Guarantee and owner | Enforcement, strength and covered paths | Alternate paths and external contract | Status |
| --- | --- | --- | --- |
| Fixed connection team for MCP; HTTP/MCP owners | Auth/team middleware and registry invocation; invariant within inspected endpoint/dispatch path | Browser recall uses its own middleware; background jobs use explicit internal team identity. Direct in-process service callers must supply trusted actor context. No deployed current credentials/grants were supplied. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Accepted Remember write is fenced; knowledge repository | Team/profile transaction, replay/duplicate locks, active embedding-contract and known-evidence authorization checks; invariant for this commit API | Session uses separate staging/commit. This is not semantic truth, global exactly-once processing or a provider-side guarantee. Requires PostgreSQL transaction/locking semantics and correct repository scope implementation. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Bounded model repair; assessment/session/ontology owners | Turn and token checks plus typed validators; protocol, not guaranteed semantic correctness | Separate provider loops have distinct histories; deterministic ontology decisions and conflict resolution can skip a model. Requires endpoint availability, compatible response protocol and usable token estimates. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Discovery must be verified before support; recall/host owners | Guidance text in returned result; policy at the host consumption boundary | Does not mechanically force a host to call trace or prevent unsupported answers. Requires host compliance. | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface includes memory submission/recall/trace and lifecycle tools, browser management, automatic ontology/conflict processing, and build-specific evaluation functions. Actual grants are actor-specific and not supplied. Shipped source wiring is not the deployed isolation envelope: no live network topology, database role configuration, provider isolation or production credential set is observed. The examined model loops use structured HTTP completions and parsed results, not an inspected model-operated shell or arbitrary extension loader; this is a bounded account of those calls, not a whole-repository absence claim. MCP/Python/proxy clients transport calls; their enclosing agent permissions are outside the service's authority (SRC-1, `internal/mcp/server.go`, `internal/http/user_portal_routes.go`, `cmd/internal/serverapp/server.go`, `internal/provider/assessor/openai.go`).

### Context, recovery and change boundaries

Assessment context is a temporary provider conversation, not the host's complete conversation. Server-selected candidate allowlists remain fixed during repairs. The adapter may replace oversized previous assistant content with a placeholder, retaining original request and error feedback; removed response content is not restored by a pointer dereference. Session extraction regenerates from original messages plus validation feedback, leaving invalid prior response text out. Ontology keeps a bounded repair dialogue. These are task frames whose parsed return escapes; diagnostic persistence is separate from provider working history. Host context compaction and reinjection after recall remain outside this inspected controller (SRC-1, `internal/provider/assessor/remember.go`, `internal/session/extraction/provider.go`, `internal/ontology/assessment/provider.go`).

Change admission is not one universal improvement loop. Direct Remember/session admission changes retained knowledge; ontology changes derived classification/equivalence; manager publication changes ontology under explicit role authorization; conflict review selects or falls back among conflicting positions. The evaluator uses deterministic qrels and explicit optional gates, but the inspected dispatch does not install a new product or tune parameters. The export prompt asks a host to produce a portable skill and user review checklist, not automatically install it. Their authority paths and evidence limits are recorded separately below. Product packaging, migration and CI/release correctness are not established by these route inspections. No inference of model training, reliable semantic correctness, exercised learning or successful self-improvement follows from retained outputs alone.

## Shared records

### Components

#### RT-CMP-openai-assessor
Label: Configured OpenAI assessor transport

Source-native identity: `OpenAIAssessor`, serving Remember assessment, session assessment and structured calls used by session extraction and ontology organization. These role invocations have distinct prompts, schemas, limits and potentially selected model names, not one undifferentiated semantic operation. Form: distributed-parametric external model, with natural-language messages and symbolic JSON request/response wrappers. Substrate: externally hosted provider parameters, inaccessible in SRC-1; per-session message state is process memory. Parameters are not updated by the inspected request/repair methods. Exact weights/version are not pinned by the configurable model string; a mutable endpoint can resolve the same name to another model. Provider training, hidden state and immutable-version guarantees are uninspected. Ontology's hash of model/prompt/schema/limits identifies local request policy, not provider weights (SRC-1, `cmd/internal/serverapp/server.go`, `internal/provider/assessor/openai.go`, `internal/session/extraction/provider.go`, `internal/ontology/assessment/provider.go`).

> model:              model,
> --- `internal/provider/assessor/openai.go`

> url := strings.TrimSuffix(v.baseURL, "/") + "/chat/completions"
> --- `internal/provider/assessor/openai.go:308-308`

#### RT-CMP-openai-embedding
Label: OpenAI embedding provider

Source-native identity: `OpenAIEmbeddingProvider`, shared through composition with retrying embedding consumers. Form: distributed-parametric model producing dense vectors; vectors are numerical representations, not symbolic truth labels. Substrate: external parameters and PostgreSQL search projections downstream. Config supplies endpoint, model and dimensions. No parameter update occurs in the inspected embedding calls. Exact parameter version is not pinned; configurable endpoint/name can change provider resolution. Active-contract and vector checks constrain returned shape/model metadata, not weight identity (SRC-1, `internal/embedding/openai_provider.go`, `internal/remember/service/processor/remember_embedding_helpers.go`, `internal/knowledge/postgres/remember_commit.go`).

> baseURL:       cfg.GetAIAPIURL(),
> --- `internal/embedding/openai_provider.go`

> model:         cfg.GetAIEmbeddingModel(),
> --- `internal/embedding/openai_provider.go`

#### RT-CMP-openai-verifier
Label: Conflict review verifier

Source-native identity: `verifierProvider` composed for conflict review with `sessionModels.conflictReview`, distinct from the Remember assessor even though a process-wide concurrency gate is shared. Form: external distributed-parametric model with symbolic dossier/decision wrappers. Substrate: remote provider parameters; durable reservation and completion belong to the conflict repository. The inspected caller requests decisions, not parameter changes. Exact parameter version is unpinned; configured endpoint/model resolution can be mutable. Verifier internal response-repair implementation and provider internals remain uninspected here, preventing a claim that its detailed repair policy equals Remember's (SRC-1, `cmd/internal/serverapp/server.go`, `internal/conflict/review/service.go`).

> response, err := s.provider.AssessRelationshipConflict(providerCtx, prepared)
> --- `internal/conflict/review/service.go`

### Operative objects

#### RT-OBJ-assessment-session
Label: Remember assessment session

Source-native identity: `openAISemanticAssessmentSession`: ID, immutable prepared request, messages, previous assistant content and turn counter. Mixed parts: natural-language prompt/evidence/feedback interpreted by a model; symbolic candidate references/schema/bounds consumed by code. Substrate: process memory for the bounded conversation, with separate database diagnostic recording through the processor. This is not an independently reloaded host conversation. Used by [RT-RTE-remember-intake](#rt-rte-remember-intake).

SRC-1, `internal/provider/assessor/remember.go`:

> The previous assessor response was omitted from repair history because its serialized form exceeded the configured input budget. Use the original request and validation_errors to return one complete replacement object.
> --- `internal/provider/assessor/remember.go`

### Routes

#### RT-RTE-remember-intake
Label: Synchronous Remember intake and replay

Endpoints: authenticated MCP `remember` through registry → application service → processor → provider/catalog/embedding → PostgreSQL → terminal MCP result. Owner: application code decides next step; model proposes semantic interpretation. State includes team/owner/space generation, hash, key, snapshot/candidates, provider turns, planned vectors, ingest ID and durable attempt. Effects are accepted retained evidence/semantic/search state or a rejected/failed attempt, not a host answer. SRC-1, `internal/tools/registry/remember_bindings.go`, `internal/remember/service/service.go`, `internal/remember/service/processor/remember_processor.go`, `internal/remember/service/processor/remember_preparation.go`, `internal/remember/service/submission_assessment_session.go`, `internal/knowledge/postgres/remember_commit.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Terminal submission result or typed error with evidence/relationship outcomes, serialized as text and structured MCP content.
- Later read-back: Durable attempt feeds replay; admitted evidence/relationships feed later recall/trace. Detailed retained revision semantics are left to memory analysis.
- Delegated visibility: Assessor receives server-prepared evidence/candidates and errors; embedder receives planned search texts, not unrestricted database or host conversation access.
- Selection predicate: Authenticated actor and bounds admit request; hash/key select replay/conflict/retry; duplicate/catalog selection shapes assessment; validators and commit fences select permissible writes.
- Invalidation or expiry: Caller deadline and phase budgets end processing; contract/hash mismatch rejects replay; stale catalogs/search contracts/known evidence can veto commit. Repair is turn bounded.
- Activation or effect: Implementation wires database changes and returns results; actual execution and later host behavior are uninspected.
- Evidence limits: Source wiring establishes neither semantic truth nor successful delivery/durability in deployment. The optional outer lock is not an exactly-once model-call guarantee.

Admission: open caller submissions, not a bounded experiment. Caller proposes evidence/relationships, model selects semantic outcomes, application validators and repository transaction can veto. No per-content human decision is required in this path; caller humanity is unresolved. Answer oracle: none supplied as expected answer; evidence/allowlists and schema validators constrain proposals, not an independent factual oracle. Trigger is a Remember call; rejected input does not advance to accepted semantic commit. Recovery replays committed outcomes or retries eligible failures with the same request; transaction failure does not constitute an accepted write. Guidance is shipped assessment policy plus validation errors, while evidence, semantic results and diagnostics—not revised model weights—persist. This describes admission, not demonstrated capacity improvement.

> // A waiter must replay the owner's durable result, including a retryable
> // failure. It may retry only after the lock owner has returned and a later
> // call acquires the key.
> --- `internal/remember/service/processor/remember_processor.go`

> if totalTurns >= SemanticMaxAssessorTurns {
> --- `internal/remember/service/submission_assessment_session.go`

#### RT-RTE-session-intake
Label: Private session extraction and admission

Endpoints: session service → private-scope selection → locked staging → extraction windows → entity linking → shared preparation → session repository commit. Owner: session service; provider proposes extracted/linked content. This separate intake is not merely another call to the direct Remember service. SRC-1, `internal/session/service/service.go`, `internal/remember/service/processor/remember_preparation.go`, `internal/session/extraction/provider.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Session submission result with accepted/duplicate event counts, per-event states, warnings, relationship results and errors.
- Later read-back: Staged submission supports retries/replay; committed extracted knowledge reaches later service consumers. Exact storage revisions remain for the memory analyst.
- Delegated visibility: Extractor receives bounded request windows; linking and assessment receive transformed selections, not automatically every raw event in one context.
- Selection predicate: Enabled dependencies, write grant and exactly one valid private space; request hash/version checks; new-event windows; extracted relationships determine whether semantic preparation is needed.
- Invalidation or expiry: Request deadline, token/turn bounds, extraction version mismatch and repository conflict checks; completed or non-retryable stored results short-circuit processing.
- Activation or effect: Can stage session intake before model work and commit prepared semantic results afterward; no observed run supplied.
- Evidence limits: Shared preparation does not prove identical staging/commit semantics to direct Remember. Window-selection and extraction grounding details are not fully audited here.

Admission: caller supplies events; model extracts/links; code validates regenerated output and repository commit can reject. No per-event human approval requirement is visible in the inspected service. Mode is open intake, not evaluation; no expected-answer oracle. Guidance is fixed extraction/linking prompts, immutable request, schema and validation feedback. Each failed turn is discarded from the next message list; only original base messages and new correction are sent. It is a bounded subcontext whose parsed result escapes. Failure recording has a separate non-cancelled persistence budget. Retryable failures can resume; exact raw-content erasure/rollback policy is uninspected.

> messages = append(append([]modelprovider.Message(nil), base...), modelprovider.Message{Role: "user", Content: string(correction)})
> --- `internal/session/extraction/provider.go`

#### RT-RTE-recall-context
Label: Bounded recall and returned discovery

Endpoints: MCP recall or browser recall handler → recall service → retrieval/search, embeddings and optional community repository → structured result. Owner: code selects context; host owns downstream judgment. Context includes query, limit, temporal filters, known IDs, expansion IDs, actor spaces, active search contract and ontology enablement. SRC-1, `internal/recall/recall.go`, `internal/recall/recall_embedding_degradation.go`, `internal/http/user_portal_routes.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evidence results, related relationships/communities, discovery paths, search states and degradations.
- Later read-back: This is the explicit requested consumption of retained evidence/semantic/organization state; it does not itself establish a new durable revision.
- Delegated visibility: Embedding provider receives query input; caller receives selected output rather than the complete store. External host context assembly remains uninspected.
- Selection predicate: Actor/space branches, query/vector, limits, valid/known times, known IDs and expansion IDs; graph/community organization is restricted to shared branches in the inspected service.
- Invalidation or expiry: Search-contract and eligibility checks occur on read; cancellation propagates. Some vector/ontology failures produce degradation rather than universal failure.
- Activation or effect: Selected context is returned; source does not show an enclosing host actually relying on it or following guidance.
- Evidence limits: Detailed retrieval ranking and all support filters are not independently audited here. Guidance delivery is not guaranteed compliance or answer improvement.

> result.DiscoveryGuidance = "Community discovery found derived relationship paths; verify details with trace_memory before using them as support."
> --- `internal/recall/recall.go`

> Message:  "Some evidence vectors are unavailable; lexical recall remains available. Check the control portal for recovery guidance.",
> --- `internal/recall/recall_embedding_degradation.go`

#### RT-RTE-ontology-maintenance
Label: Automatic ontology organization

Endpoints: server-started scheduler → maintenance policy/window/turn/batch claims → organizer → selected source/vocabulary context → deterministic or model assessment → compiled publication/repository commit → batch completion. Owner: internal maintenance code, not a manager actor. SRC-1, `cmd/internal/serverapp/server.go`, `internal/ontology/maintenance.go`, `internal/ontology/service.go`, `internal/ontology/assessment/provider.go`, `internal/ontology/postgres/organization.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Worker progress/error and organization result/receipt; this is not a conversational response.
- Later read-back: Definitions, assignments, groups, dependencies and receipts can shape later organization and recall; exact invalidation semantics are reserved for memory analysis.
- Delegated visibility: Model gets selected items, definitions and pair references under vocabulary/input/output bounds; no arbitrary memory search is granted by the inspected provider call.
- Selection predicate: Enabled policy, available model, window, leased turn/batch and sources; forced/exact/lexical vocabulary candidates. Fully locked item/pair decisions can be validated deterministically without provider calls.
- Invalidation or expiry: Leases and source/dependency context bound work; at most three provider turns with token checks; attempt reservations can reject dispatch. Failures complete/release claims and record empty publication outcomes.
- Activation or effect: Code can compile and submit derived organization changes; observed publication and retrieval effects are uninspected.
- Evidence limits: Transaction-level publication rejection rules and every scheduler scenario are not fully audited. Request semantics do not prove correct model equivalence judgments.

Admission: automatic batch trigger; model proposes classifications, definitions and equivalence for undecided cases; code validates, compiles and commits or records rejection. No per-item human approval. Guidance is fixed source-data-only organization prompt and validation feedback. No answer oracle; supplied locked definitions/required relations are code decisions, not external truth labels. Mode is recurring open maintenance, not a curriculum. It retains organization/receipt state rather than changing provider parameters. Rejection and failure recording are implemented; manager rollback is a separate route, not a demonstrated automatic rollback policy.

> if deterministic {
> err = assessment.Validate(request, response)
> } else {
> response, receipt.Result.Attempts, err = s.provider.Assess(ctx, request)
> }
> --- `internal/ontology/service.go`

> return fmt.Errorf("%w: transport omitted durable admission", contract.ErrAccounting)
> --- `internal/ontology/maintenance.go`

#### RT-RTE-manager-publication
Label: Manager ontology draft publication and rollback

Endpoints: manager application service → validated edits/draft → preview → explicit publish/discard → repository; rollback uses publication identity and revision/operation contract. Owner: manager principal plus software admission. SRC-1, `internal/ontology/management.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Draft, preview, publication or rollback result/error.
- Later read-back: Published ontology is retained and available to organization/recall; draft and publication readers expose management history.
- Delegated visibility: Manager sees repository-projected records, sources, drafts and previews; no model delegation in this service.
- Selection predicate: Actor must have team/owner, manager role and appropriate read/write grant; writes also require audit availability, valid operation and expected revisions/versions.
- Invalidation or expiry: Invalid edit/action/version/revision rejects progression; exact transactional staleness and rollback eligibility rules remain uninspected here.
- Activation or effect: Explicit publication or rollback requests can change ontology; source wiring does not prove exercised changes.
- Evidence limits: Manager role does not prove a human was the actor. No observed review quality or complete UI-to-repository transaction audit.

Admission: manager supplies edits and publication/discard/rollback decisions; code compiles against current context and repository can reject. This is deliberate content control by a role, not proof of human-in-the-loop deployment. No expected-answer oracle; mode is explicit administration. Guidance is edit/operation contract and current context. Drafts/publications and audit events persist; rollback is exposed as a separate command with operation/revision validation.

> if action != "publish" && action != "discard" {
> return contract.ManagementDraft{}, contract.ErrInvalid
> }
> --- `internal/ontology/management.go`

#### RT-RTE-conflict-review
Label: Automatic relationship conflict review

Endpoints: scheduled runner/ledger → deterministic case review → pending resolution resume or overdue reservation/dossier → verifier when required → assessment completion → resolution planning/execution. Owner: conflict review service/repository, with bounded model proposal. SRC-1, `cmd/internal/serverapp/server.go`, `internal/conflict/review/runner.go`, `internal/conflict/review/service.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Case review outcome/stage, pending/stale indicators, updated relationship identities or failure.
- Later read-back: Reservations/completions and pending resolution state support later reviews; resolved semantic state and derived evidence tasks reach later knowledge consumers.
- Delegated visibility: Verifier receives prepared bounded dossier, not unrestricted store access through this interface; semantic-write executor receives a plan and embedding provider.
- Selection predicate: Deterministic result can resolve without model; overdue cases reserve by case/run/worker/local date/model/policy. A selected position must be valid and confidence at least 0.70.
- Invalidation or expiry: Case version and stale/pending resolution outcomes constrain effect. Provider failures are recorded; failed-day threshold or abstention can lead to last-write-wins fallback.
- Activation or effect: Implemented path can select and commit conflict resolution and stage derived evidence; exercise and correctness are unobserved.
- Evidence limits: Detailed repository majority rule, fallback ordering, derived-evidence staging and verifier prompt/repair internals remain uninspected; no universal model-correctness claim.

Admission: internal review trigger, deterministic policy or model proposes preferred position, code validates and repository/executor can reject/stale it. No per-case human approval in inspected service. Mode is recurring conflict maintenance; no expected-answer oracle. Dossier and configured policy guide judgment; durable assessment outcomes/pending tasks shape recovery. An abstention is not necessarily no change: code invokes fallback. Rollback of resolved factual state is not established here.

> if response.Confidence < AssessmentConfidenceThreshold {
> return s.recordAssessmentFailure(ctx, result, input, reservation, dossier, "below_confidence_threshold")
> }
> --- `internal/conflict/review/service.go`

> s.observeConflictAssessment(input.TeamID, "abstained", "none")
> return s.applyLastWriteWins(ctx, result, input, reservation, dossier)
> --- `internal/conflict/review/service.go`

#### RT-RTE-evaluation-suite
Label: Retrieval evaluation and optional gates

Endpoints: shipped eval runner → load/validate manifest/corpus/cases/qrels/suite → import/live recall or loaded traces → deterministic scoring → artifacts/optional gates. Owner: explicit evaluator invocation, not production conversational controller. SRC-1, `internal/evalharness/runner.go`, `internal/tools/registry/evaluation_catalog_production.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary, artifacts and optional gate failure; import-only mode returns before retrieval scoring.
- Later read-back: Mapping/checkpoints can resume imports; saved traces/mapping can be loaded for scoring; run directories can be compared. Production knowledge may be produced by import calls, not by scores themselves.
- Delegated visibility: Live driver sends corpus submissions and recall cases through client; loaded-trace mode can avoid live calls. No answer-judge model in inspected dispatch.
- Selection predicate: Explicit mode/options, manifest/suite validation, qrel mapping completeness and optional gate thresholds.
- Invalidation or expiry: Invalid input/mappings reject the run; legacy Dream expectations reject live flow; configured gates can fail after scores/artifacts exist.
- Activation or effect: Measurement/import capacity wired; achieved scores, reproduction and causal benefit uninspected.
- Evidence limits: No supplied runtime artifacts or intervention evidence. The inspected evaluator does not show automatic score-driven product installation or provider training.

Answer oracle: loaded qrels supplied by evaluation inputs, applied through `ScoreTraces`; their construction and factual validity are not established by the runner. Mode is bounded benchmark, unlike ordinary intake. Operator selects inputs/options, software scores and can veto gate acceptance. No new product/capability admission is inferred from gate failure/success. Production compilation excludes evaluation tools under the non-evaluation build tag, so evaluation capability is not the current grant set of every server.

> scores, summary, err := ScoreTraces(runID, mode, manifest.SeedID, seedHash, opts.SuitePath, suite, IndexCases(cases), IndexQrels(qrels), traces, mapping)
> --- `internal/evalharness/runner.go`

> func evaluationTools(Dependencies) []Tool {
> return nil
> }
> --- `internal/tools/registry/evaluation_catalog_production.go`

#### RT-RTE-skill-export
Label: Host-mediated portable skill drafting

Endpoints: rendered export prompt → host recall/drafting → proposed skill markdown and review checklist. Owner: host for execution; Dense-Mem supplies guidance. SRC-1, `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`, `internal/mcp/server.go` (catalog construction; prompt registration described in boundary).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Prompt requests skill contents in code blocks and user review checklist, not automatic installation.
- Later read-back: inapplicable — no inspected automatic persistence or installation of generated skill; later host adoption would be a separate event.
- Delegated visibility: Host is asked to recall relevant memory and distill it; actual recalled selection and draft are not supplied.
- Selection predicate: Topic/scope and prompt rules prefer relevant durable preferences, corrections, decisions and reusable instructions while excluding unapproved/private/temporary material.
- Invalidation or expiry: uninspected — host execution and rejection of unsuitable drafts are not supplied; prompt requests review before sharing.
- Activation or effect: Supplied instruction could shape a host draft; actual compliance, adoption and sharing are unobserved.
- Evidence limits: A natural-language prohibition is not a server-enforced confidentiality or no-write guarantee over all host capabilities.

Admission: user/host request triggers proposed portable instruction content; prompt asks user review before sharing and forbids automatic memory import. No installed capability change is established. Host proposes/decides under instruction; user approval is requested, not observed. Mode is open drafting, no answer oracle. Recalled context and fixed export guidance shape the proposal; only generated output is requested, with no inspected rollback or durable installation route.

> Return the skill content as markdown code blocks. Do not import the generated skill into memory automatically.
> --- `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`

### Claims

#### RT-CLM-commit-fences
Label: Accepted Remember commit fences

Claimed operation: accepted direct Remember persists after provider work inside a team/profile transaction, with idempotency, duplicate, active embedding-contract and known-evidence fences. Owner is knowledge repository; guarantee strength: invariant for the inspected commit API under PostgreSQL transaction/locking and trusted scope contracts. Not a guarantee of truth, exactly-once model execution or identical session staging. Covered route: [RT-RTE-remember-intake](#rt-rte-remember-intake). Alternate route: [RT-RTE-session-intake](#rt-rte-session-intake). SRC-1, `internal/knowledge/postgres/remember_commit.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> // CommitRememberWithEmbeddings persists one accepted Remember after
> // provider work has completed. No knowledge-ingest, evidence, placement, or
> // attempt row exists before this transaction starts.
> --- `internal/knowledge/postgres/remember_commit.go`

> if err := validateRememberEmbeddingContractAgainstActive(embeddings, contract); err != nil {
> return err
> }
> --- `internal/knowledge/postgres/remember_commit.go`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-assessment-guidance
Label: Assessment guidance into bounded semantic decisions

Consumer: configured assessor behind [RT-CMP-openai-assessor](#rt-cmp-openai-assessor). Channel: system prompt, prepared user JSON and validation feedback in [RT-OBJ-assessment-session](#rt-obj-assessment-session). Force: natural-language instruction interpreted by model, then symbolic response validation and commit checks; instruction delivery alone does not guarantee semantic compliance. Horizon: one bounded conversation, with admitted output reaching later service calls through retained knowledge. SRC-1, `internal/provider/assessor/remember.go`, `internal/remember/service/submission_assessment_session.go`.

> {Role: "system", Content: assessor.SemanticAssessmentSystemPrompt},
> {Role: "user", Content: string(userJSON)},
> --- `internal/provider/assessor/remember.go`

#### RT-BAP-discovery-guidance
Label: Recall guidance into host support decisions

Consumer: MCP/browser client and possible enclosing host model. Channel: recall result's discovery guidance, through [RT-RTE-recall-context](#rt-rte-recall-context). Force: advisory natural language to verify with trace, not a server veto on downstream answers. Horizon: caller's current and possible later reasoning; no observed activation or retained host adoption. Evidence and exact guidance are in that route (SRC-1, `internal/recall/recall.go`).

#### RT-BAP-export-guidance
Label: Export prompt into proposed skill instructions

Consumer: host drafting agent and user reviewer. Channel: rendered catalog prompt for [RT-RTE-skill-export](#rt-rte-skill-export). Force: natural-language workflow, exclusion rules and review request; not installed code or an enforced host permission. Horizon: proposed shareable skill, with later installation/use unobserved. Evidence and exact prohibition are in that route (SRC-1, `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`).

## Annotations

none
