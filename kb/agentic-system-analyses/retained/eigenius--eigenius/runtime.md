---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Eigenius runtime baseline: asynchronous prose formalization, separate knowledge admission, and effectful program execution at the frozen revision."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
---

# Eigenius runtime report

## Runtime account

Eigenius supplies a typed knowledge platform, not the external agent's reasoning loop. The consequential shipped work selected here is prose-to-artifact formalization, admission of resources into a serving branch, and execution of resource-encoded programs. The frozen [boundary](boundary.md) remains a complete artifact with a partial operational loop. All findings below use SRC-1 at its registered revision. They are implementation or attributed design findings; no supplied run, test outcome, provider transcript or intervention establishes activation, successful operation, speed, scientific correctness or benefit.

### Entry and ordinary invocation

The CLI's `serve` path opens RocksDB when `--db` is supplied, constructs the Morphy-backed parser configuration, injects `EncodingFormalizer`, and links Lean and Statistics institutions. Omitting `--db` is a material alternative: the formalization RPC rejects a server without a persistent backend/task store even though other server functions can exist without one. Configured embedders are another optional startup seam, not a necessary part of this formalization trace (SRC-1, `cli/src/main.rs`, `kernel/src/server/formalize.rs`).

An ordinary notebook formalization begins when a caller runs a cell containing prose. The notebook chooses `doc_id` or the cell ID, requests ESL, and passes a lexicon profile. The MCP alternative exposes prose, document ID, branch/layer, ordered scope/profile, model choices, strictness and encoding options. Both reach the kernel formalization seam. The initiating principal is a client; whether that client is a human or an automated agent is not established by an RPC. The external agent's task selection and tool permissions are outside the inspected target-side loop (SRC-1, `notebooks/src/runtime/notebookStore.ts`, `orchestration/src/mcp/server.ts`).

The kernel checks required inputs, resolves the read layer and ordered lexicon scope, constructs per-request model configurations, chooses inline/live/branch recordings, and persists a UUID task naming the document, source hash and layer. It returns the task ID and document-branch name immediately. A blocking worker, not an enclosing chat loop, owns the next step. The formalizer reloads previous draws before rebuilding its document glossary branch, runs parsing and discourse resolution with configured decision arms, emits the artifact, and commits newly recorded live draws. The result is stored as a CBOR metadata blob rather than loaded into the serving chain. See [RT-RTE-document-formalize](#rt-rte-document-formalize) and the separate selection route [RT-RTE-reading-selection](#rt-rte-reading-selection).

The notebook polls every three seconds with a thirty-minute client deadline, fetches the artifact, surfaces a missing/error result, and returns artifact, structure IRI, counts and working-branch identity. Its deadline does not terminate server execution. Optional `land` immediately calls Load after generation. Thus generation/admission separation is implemented, but mandatory human inspection is not. An automated MCP client can likewise fetch then load. The emitted claims identify an unattributed agent on the served path rather than silently attributing responsibility to the parser (SRC-1, `kernel/src/server/formalize.rs`, `crates/eigenius-encoding/src/formalize.rs`, `notebooks/src/runtime/notebookStore.ts`).

### Forcing cases and guarantee boundaries

Four forcing cases bound this account rather than treating tool descriptions as universal guarantees.

1. **Existing recordings versus live inference.** A repeated document ID can supply recorded answers, but exact selection questions include document hash, prior choices and candidates. Changed questions can miss and abstain. Missing recordings can invoke live models, and feature/key availability changes behavior by seam. A replay run is not automatically a complete or successful reproduction. Inline recordings and explicit live mode exist at the RPC even though the inspected MCP tool does not expose those switches. [RT-RTE-document-formalize](#rt-rte-document-formalize) records the implemented alternatives.
2. **Typed candidate versus faithful interpretation.** The reading ranker chooses among candidates, first by grammatical analysis and then by senses. Selection validates answer membership and the caller refuses indistinguishable presentations; neither establishes that the chosen reading means what the author intended. Some structures are omitted before the model sees them. The inspected source explicitly distinguishes this decision from a kernel semantic veto. See [RT-RTE-reading-selection](#rt-rte-reading-selection) and [RT-CLM-formalize-claims](#rt-clm-formalize-claims).
3. **Load versus other persistence paths.** Load with auto-commit uses structural, retroactive and institution phases. Program-run output uses `WithRetroactive`, document glossary persistence uses a direct persister, and kernel follow-up emissions use build/persist without structural validation. AutoOnLoad classes newly declared in a Load batch take effect on later loads. Therefore no single universal 'all retained content passes every gate' guarantee follows. See [RT-RTE-resource-admission](#rt-rte-resource-admission).
4. **Validation versus effectful execution.** ValidateProgram reports parsing/template/schema checks, not an EigenTT proof of program well-typedness. Inline and IRI-based execution share an IO evaluator and can dispatch registered components. CompleteText performs another model call path; runtime components can reach subprocess/container workers. A post-execution chain rejection is not a pre-execution effect authorization gate. See [RT-RTE-program-execution](#rt-rte-program-execution) and [RT-RTE-runtime-registration](#rt-rte-runtime-registration).

Load-bearing controls have different owners and scopes:

| Control | Owner and enforcement point | Strength and covered paths | Alternate path / external contract | Status |
|---|---|---|---|---|
| Refuse selecting indistinguishable candidates; reject out-of-range selection | Parser's `select_reading`, before and after ranker invocation | invariant for this selection entry; fidelity itself has no claimed guarantee here | A sole survivor does not require this selection; provider must answer the intended question, which structural checks cannot establish | implementation conclusion status: wired; operation conclusion status: uninspected |
| Preserve failures as cuts or abort under strict mode | Shared artifact emitter, `partial: !req.strict` | protocol for served artifact emission | Non-strict mode intentionally returns a partial artifact; successful generation is not complete encoding | implementation conclusion status: wired; operation conclusion status: uninspected |
| Validate and conditionally admit a Load batch | Load handler and selected commit pipeline, before persist | protocol for auto-committing Load | Other pipeline kinds and direct document persistence differ; institution meaning depends on registered implementations, and durable CAS depends on the backend | implementation conclusion status: wired; operation conclusion status: uninspected |
| Retain task/result state | Formalization handler and metadata backend | best effort for terminal state/result writes | Initial task persistence errors return an error; completion writes discard errors, so a finished computation need not become a retrievable completed task | implementation conclusion status: wired; operation conclusion status: uninspected |
| Isolate worker effects | Selected spawner, not the type system | no claimed guarantee of adversarial containment | LocalSpawner is a host subprocess; Docker configuration supplies particular controls, not a verified deployment envelope | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence for these scopes is retained in the route records. Reliability is not inferred from the existence of task status, traces or exception capture. In particular, formalization's result serialization, result write and final task write use ignored results. Program evaluation catches unwinds and returns execution errors, but this is not rollback of external effects (SRC-1, `kernel/src/server/formalize.rs`, `kernel/src/program/eval_io.rs`). Crash/restart recovery for formalization and all durable-worker variants remains uninspected; source comments about recoverable tasks are not an executed recovery demonstration.

### Capability, grants and change admission

The capability surface includes resource loading/tombstones, inline or retained program execution, direct formalization decisions, completion components and optionally registered runtime languages. This is not evidence that every installation grants all of them. Startup configuration determines component availability; credentials determine provider availability. A deployed per-principal grant set, authentication policy and host isolation envelope were not supplied and are not inferred from tool registration. No universal approval or sandbox claim is made (SRC-1, `orchestration/src/main.ts`, `orchestration/src/mcp/server.ts`, `crates/runtime-substrate/src/spawner/local.rs`, `crates/runtime-substrate/src/spawner/docker/container.rs`).

Knowledge and executable-resource changes enter through [RT-RTE-resource-admission](#rt-rte-resource-admission); recorded decisions enter the document branch through [RT-RTE-document-formalize](#rt-rte-document-formalize). Model changes can be requested per invocation without invalidating old recordings merely because the answerer changed. Runtime capabilities enter through host registration/configuration, not arbitrary prose acquiring code privileges. The inspected routes do not establish self-modification of binaries, model training, or an automatic source-code improvement/adoption loop. Such production/release mechanisms, broader institution semantics, vector retrieval, GC/consolidation and notebook publication remain available but uninspected, not evidenced absences.

### Added source coverage

Beyond boundary inspection, this member inspected implementation in `kernel/src/dcg/pipeline.rs`, `kernel/src/dcg/parse/resolve.rs`, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/dcg/model_config.rs`, `kernel/src/commit/pipeline.rs`, `kernel/src/commit/phases.rs`, `kernel/src/server/programs.rs`, `kernel/src/program/eval_io.rs`, `orchestration/src/components/complete_text.ts`, and the local/Docker spawner paths cited above, plus additional ranges of boundary-listed entry points. All are SRC-1 implementation; comments are attributed design explanations where used. This is bounded loop coverage, not inspection of every top-level responsibility in the boundary.

## Shared records

### Components

#### RT-CMP-proposer-model
Label: Formalization proposer model

The non-reading decision arms use the requested `ModelConfig`; the default is `claude-sonnet-4-6`. This is distributed-parametric content accessed through an external service, not weights stored in Eigenius. The inspected client requests structured output and deserializes replies. Parameter changes during operation are uninspected provider internals; these callers expose inference, not parameter updates. An exact immutable parameter version is not established by the model string. Endpoint resolution to changed provider implementations remains possible/uninspected. SRC-1, `kernel/src/dcg/model_config.rs`, `kernel/src/dcg/anthropic_client.rs`, `crates/eigenius-encoding/src/formalize.rs`.

> pub const DEFAULT_MODEL: &str = "claude-sonnet-4-6";
> --- `kernel/src/dcg/model_config.rs`

The forced `emit` tool is a structured-response channel, not evidence of a provider-native shell or general tool executor:

> body["tool_choice"] = json!({ "type": "tool", "name": TOOL_NAME });
> --- `kernel/src/dcg/anthropic_client.rs`

#### RT-CMP-reading-model
Label: Reading selection model

The reading seam separately defaults to `jev-latest`; `jev-` selects TypeSafe and other configured IDs select Anthropic. Distributed-parametric content remains at the provider. Eigenius stores model names and answers, not inspected weights. No operation-side weight mutation is established; provider-side updates are uninspected. The default is explicitly a mutable alias, not an exact version pin. Caller replacement of `reading_model` is supported independently of the other proposer model. SRC-1, `kernel/src/dcg/model_config.rs`, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/server/formalize.rs`.

> pub const DEFAULT_READING_MODEL: &str = "jev-latest";
> --- `kernel/src/dcg/model_config.rs`

#### RT-CMP-completion-model
Label: CompleteText provider model

CompleteText uses Anthropic through the AI SDK with model and generation parameters read from the component argument. The default model is the same named family as the proposer default, but the invocation/control path is distinct. Its distributed-parametric substrate is provider-hosted; parameters changing during operation are uninspected, exact weight pinning is not established, and the named endpoint may resolve to another provider revision. The inspected handler performs inference and has no inspected parameter-write operation. CompleteJson is separately registered but its full handler contract is uninspected here. SRC-1, `orchestration/src/components/complete_text.ts`, `orchestration/src/main.ts`.

> model: anthropic(model),
> system: systemPrompt,
> prompt,
> temperature,
> maxOutputTokens: maxTokens,
> --- `orchestration/src/components/complete_text.ts`

### Operative objects

#### RT-OBJ-formalization-artifact
Label: Emitted formalization artifact

A generated resource document is symbolic content serialized as CBOR, Eigon-JSON or ESL. Its immediate durable substrate is the result metadata blob keyed by task UUID, not a serving-chain layer. The contained source prose is interpreted through the earlier model/parser path; this record concerns the emitted resource structure and its load consumer. Counts distinguish encoded units and cuts. An artifact can be fetched and inspected without being loaded. SRC-1, `kernel/src/server/formalize.rs`, `crates/eigenius-encoding/src/formalize.rs`.

> fn result_key(task_id: &uuid::Uuid) -> String {
>     format!("formalize:result:{task_id}")
> }
> --- `kernel/src/server/formalize.rs`

#### RT-OBJ-program-resource
Label: Executable program resource

A program resource has an embedded symbolic body parsed into an EigenTT expression and evaluated with an `input` binding. It may arrive inline or be resolved from a retained layer by IRI. In the retained case the substrate is the layer/backend, not model weights. Program data may contain natural-language completion templates; those receive authority through the separate model prompt consumer, not through symbolic evaluation of their linguistic meaning. SRC-1, `kernel/src/program/eval_io.rs`, `kernel/src/server/programs.rs`, `orchestration/src/components/complete_text.ts`.

> let body_exp =
>         crate::program::expr::parse_expression(body, &layer).map_err(ProgramError::Parse)?;
> --- `kernel/src/program/eval_io.rs`

### Routes

#### RT-RTE-document-formalize
Label: Document formalization task

Endpoints: notebook/SDK or MCP request → kernel task → injected formalizer → result fetch. Code owns progression after the request; task UUID, document ID, namespace, source hash and pinned read layer distinguish identities. Scope/profile ordering, sense cap, beam, model choices and strictness are client controls. The formalizer reads previous branch/inline draws, chooses replay or live arms, builds glossary state, parses and resolves discourse, emits the artifact and commits live recordings. The serving branch is not automatically loaded. SRC-1, `kernel/src/server/formalize.rs`, `crates/eigenius-encoding/src/formalize.rs`, `kernel/src/dcg/pipeline.rs`, `notebooks/src/runtime/notebookStore.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: task UUID and doc-branch name; later result fetch returns artifact bytes, encoding, structure IRI, counts and error.
- Later read-back: a later request with branch draws can consume recorded answers from the previous doc branch; the read happens before that branch is rebuilt. Detailed memory revision semantics are left to the memory analyst.
- Delegated visibility: the blocking formalizer receives resolved layer, persistent backend and request; models receive seam-specific prompts, not the caller's whole chat history.
- Selection predicate: inline draws take priority over live flag; otherwise explicit live bypasses recordings and default branch mode loads them. Each seam selects its own replay/live arm.
- Invalidation or expiry: replay selection requires the same keyed question; changed context/candidates can miss. The doc glossary branch is deleted/repointed before persistence; artifact/task expiry and concurrent same-doc coordination are uninspected.
- Activation or effect: implemented path writes glossary/draw state and result metadata; actual execution and behavioral effects are unobserved.
- Evidence limits: terminal result/task writes ignore errors; no crash-recovery or cancellation result was supplied. Same doc ID alone does not guarantee replay hits, no provider calls, or full encoding.

Admission: caller supplies prose and controls; model arms propose decisions; parser/emitter determine accepted encoding or cuts. No per-content human approval is required to retain draws. Existing recordings guide decisions and live responses persist; there is no runtime answer oracle in this inspected route. Mode is an open document request, not a bounded improvement experiment. Strict mode rejects at first non-encoding unit; partial mode retains explicit cuts. No content-directed criticism/revision of formulated theories is established by this route; claim generation and replay are not by themselves such a loop. Theory-builder conditions 1–4 and learning outcomes are not assessed from encoding alone; theory content and criticism mechanisms require the epistemic account.

> let branch = doc_branch_head(&backend, &req.doc_id)?;
> --- `crates/eigenius-encoding/src/formalize.rs`

> let _ = result_backend.put_meta(&result_key(&task_id), &buf);
> --- `kernel/src/server/formalize.rs`

> partial: !req.strict,
> --- `crates/eigenius-encoding/src/formalize.rs`

Countercase to an undifferentiated fail-closed claim: missing sense recording without live support errors, while without `use-llm` the selection/anaphora arms can be absent, and a missing kind classifier can leave no in-loop lander. Successful strict emission is a distinct control from every optional seam being present.

> None // no ranker: ambiguous units stay ambiguous and are recorded as cuts
> --- `crates/eigenius-encoding/src/formalize.rs`

#### RT-RTE-reading-selection
Label: Reading candidate selection

Endpoints: parser's closed candidate pool → ranker/provider or replay → selected candidate and discourse context. The parser constructs skeletons, glosses, constituent/grammatical links and concept definitions. The decision ranker asks for structure and then senses where needed, limits shown structure groups, and returns an index/rationale/runners-up. Symbolic membership checks delimit the model's choice; natural-language context and questions guide the judgment. SRC-1, `kernel/src/dcg/parse/resolve.rs`, `kernel/src/dcg/reading_ranker.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: chosen candidate plus rationale/runners-up, or abstention; caller resolves the index through the ordered pool.
- Later read-back: recorded questions/answers can be replayed by a later formalization; current-document prior glosses are working state, not by themselves cross-invocation memory.
- Delegated visibility: document, current sentence and prior selected glosses enter the decision context. The parser builds a candidate concept legend; the decision surface receives a bounded presentation, not every raw parse structure.
- Selection predicate: fewer than two candidates needs no disambiguation; indistinguishable rendered candidates cause caller abstention; one shown analysis skips the structure call; alternatives not shown cannot be chosen.
- Invalidation or expiry: selection replay misses when its document/prior/candidate key differs; recorded abstentions replay as abstentions. No time expiry was inspected.
- Activation or effect: a selected reading supplies semantic structure and a surface gloss for subsequent discourse consumers; changed scientific or interpretive accuracy is unobserved.
- Evidence limits: candidate membership and distinguishability do not certify faithfulness to prose. Provider inference is opaque, and the full TypeSafe transport was not inspected.

Decision roles: model proposes the structure/sense choice; code limits presentation, validates membership and can abstain. No mandatory human selector or runtime reference answer is present in this inspected route. PinReadingRanker is a separate human-pin/gate implementation, not the served path's default oracle. Operating mode here is open-request disambiguation, not online improvement. Full document and selected prior glosses cross this decision frame; no accumulated assistant/tool conversation is passed. Code deliberately omits groups beyond `MAX_STRUCTURES_SHOWN`, keeps the original pool outside the prompt and can reconstruct questions later. This resembles a bounded call frame, but the model receives values, not dereferenceable pointers, and the whole document remains supplied; it is not a claim of chat compaction.

> groups.truncate(MAX_STRUCTURES_SHOWN);
> --- `kernel/src/dcg/reading_ranker.rs`

> let sel = ranker.select(&ctx, &cands)?;
> let chosen = *order.get(sel.chosen)?;
> --- `kernel/src/dcg/parse/resolve.rs`

The source's own design qualification is load-bearing, not a promise of semantic reliability:

> //! candidate here already type-checks — there is no kernel veto on selection.** The controls are
> --- `kernel/src/dcg/reading_ranker.rs`

#### RT-RTE-resource-admission
Label: Resource load admission

Endpoints: caller-supplied resources/tombstones → branch working builder → optional commit orchestrator → layer outcomes. The handler locks the branch context, parses/stages resources and validates tombstone IRIs. Auto-commit selects `WithInstitutions`; institution index/runtime are snapshots taken before the drain. The root pipeline runs build, structural validation, retroactive validation/cascade, AutoOnLoad and persistence; per-layer outcomes distinguish branch advancement from merely obtaining an ID. SRC-1, `kernel/src/server/load.rs`, `kernel/src/commit/pipeline.rs`, `kernel/src/commit/phases.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/errors, resource count, branch, layer ID, advancement/merge information and ordered layer outcomes.
- Later read-back: admitted resources can enter subsequent branch reads, parses, program resolution and institution selection; no observed downstream activation is supplied.
- Delegated visibility: institution dispatch receives a read-only context over the unpersisted candidate chain; new QueryClasses from the current batch do not govern that same batch's dispatch.
- Selection predicate: auto-commit must be true for the commit block. Reject policy refuses retroactive violations; cascade policy tombstones offending lower-layer IRIs. Structural failure refuses new content under either policy.
- Invalidation or expiry: explicit/cascade tombstones can invalidate chain resources; pipeline failure can prevent user-layer persistence while audit siblings survive. Branch restoration/CAS recovery exists at the orchestrator seam, but full storage crash consistency is uninspected.
- Activation or effect: implemented admission can advance a branch and refresh its institution index; post-persist hook errors need not undo commits.
- Evidence limits: Load response success is not a scientific truth certificate. Auto-commit false stages resources and skips the commit block; it is not evidence that the full validation pipeline ran.

Admission roles: caller proposes content and policy; code and applicable institutions can reject it. Human authorship/approval is unresolved for generic callers. Optional notebook land and MCP default auto-commit permit software admission without a human reviewing each artifact. Guidance consists of active schemas/institution declarations and selected commit policy; resources, tombstones and audit outcomes can persist. Rejection is distinct from compensating external effects. This is an open mutation request, not an improvement curriculum. An institution verdict is a computed result; no general expected-answer oracle is established.

Coverage counterexamples are executable phase choices, not inferred absences:

> static STRUCTURAL_FOLLOWUP_PHASES: &[Phase] = &[build, persist];
> --- `kernel/src/commit/pipeline.rs`

> if state.persist.already_validated(layer) {
> --- `kernel/src/commit/phases.rs`

The latter is an anchored revalidation skip, dependent on the persister's validated-cache contract. Program outputs select another pipeline, and glossary persistence bypasses this Load handler. Those are not silently covered by the Load guarantee.

#### RT-RTE-program-execution
Label: Program IO execution

Endpoints: inline program/input or IRI-resolved retained resources → shared `execute_program` → IO evaluator/component or institution dispatch → output/trace commit. Request branch identifies the execution context; IRI reads can name a layer snapshot. A persistent task records session, UUID, program/input IRIs and head. The evaluator binds input, evaluates with institution hooks, catches panics and collects output/produced resources/traces. SRC-1, `kernel/src/server/programs.rs`, `kernel/src/program/eval_io.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/errors, encoded output, trace/task identities, output resource IRIs and branch merge information; MCP decodes successful CBOR output for its consumer.
- Later read-back: retained programs can be resolved by IRI on a later request; committed outputs and traces remain chain resources. Trace storage alone does not establish later behavior-shaping learning.
- Delegated visibility: component/institution engine receives the read layer, registry, trace store and optional task context; CompleteText interpolates the input into its component-defined prompt, not an external agent's whole conversation.
- Selection predicate: caller chooses inline versus IRI path; both reach shared execution. Expression form and registered capability determine dispatch, not an inferred model permission.
- Invalidation or expiry: retained resources may be replaced/tombstoned through chain mutation; current registry/head are snapshotted for evaluation. Full task resumption/expiry semantics remain uninspected.
- Activation or effect: evaluation may invoke external computation before produced resources and traces are admitted through `WithRetroactive`; no execution or external effect was observed.
- Evidence limits: static validation is not type checking; output commitment is not universal AutoOnLoad admission or reversal of external effects. Provider-native tools beyond structured emission and the full remote dispatch/retry machinery are not established here.

Admission: caller proposes executable content or names a retained program; evaluator interprets its symbolic body. No human per-step approval is established. CompleteText's caller-supplied user/system templates guide an external model and its output is returned, not a new learned parameter set. Program output admission uses the default commit policy and no institution context. This route is an open execution request, not a bounded evaluator experiment; a reference answer oracle is unestablished. Recovery includes returned execution errors and task failure updates; successful external work followed by a failed commit is not claimed transactional.

> crate::commit::PipelineKind::WithRetroactive,
> --- `kernel/src/server/programs.rs`

> let eval_result = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
>         eval_traced(&body_exp, &rho, &ctx)
>     }));
> --- `kernel/src/program/eval_io.rs`

#### RT-RTE-runtime-registration
Label: Host runtime capability registration

Endpoints: Deno startup environment and native-addon availability → component/language registries → later runtime dispatch. Startup code registers real or mock completion handlers and conditionally registers test, Julia, Lean, R and OCI runtimes. This is admission of available capabilities by host configuration, not a model dynamically installing arbitrary code. SRC-1, `orchestration/src/main.ts`, `crates/runtime-substrate/src/spawner/local.rs`, `crates/runtime-substrate/src/spawner/docker/container.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registration success logs or caught registration-failure warnings; startup continues past caught language registration failures.
- Later read-back: in-process registries determine availability on subsequent requests during that process; no automatic durable capability-learning mechanism was inspected.
- Delegated visibility: registered native runtimes receive their configured worker/image/depot inputs; worker calls cross a process or container boundary rather than a model sub-agent conversation.
- Selection predicate: addon must load and each language's required environment values must be present; mock mode separately selects completion implementations.
- Invalidation or expiry: process/configuration replacement changes registry contents; runtime unregistration and hot-reload behavior are uninspected.
- Activation or effect: later runtime components can execute host/container workers; actual grants and deployed worker choice are unobserved.
- Evidence limits: registration is not proof of isolation, successful worker boot, arbitrary-code containment or a deployed privilege policy; complete image/cross-check/worker protocol semantics remain uninspected.

Admission roles: host configuration supplies capability implementations; code can refuse registration or dispatch. Human involvement in preparing that configuration is not established. Recovery is typed missing-capability behavior and logged startup failures at the inspected seam; rollback of changed images/configuration is operationally uninspected. Mode is host startup plus open dispatch requests, with no answer oracle or improvement-trigger mechanism established.

Local spawning explicitly launches a host command with a cleared environment and per-invocation working directory:

> let mut cmd = Command::new(&spec.command[0]);
> cmd.args(&spec.command[1..])
>             .current_dir(&spec.tempdir_host_path)
>             .env_clear()
>             .envs(&spec.env);
> --- `crates/runtime-substrate/src/spawner/local.rs`

Docker construction instead uses the requested digest, configured network mode, read-write tempdir/read-only depot mounts, optional memory bound and `no-new-privileges`. It deliberately does not drop capabilities. These concrete controls do not prove an adversarial sandbox:

> let mut opts = vec!["no-new-privileges:true".to_string()];
> --- `crates/runtime-substrate/src/spawner/docker/container.rs`

### Claims

#### RT-CLM-formalize-claims
Label: Typed kernel-checked formalization claim

MCP describes document formalization as typed, kernel-checked claims. SRC-1, `orchestration/src/mcp/server.ts`:

> "Formalize prose into typed, kernel-checked claims (D71). Returns a " +
> --- `orchestration/src/mcp/server.ts`

- Claim conclusion status: claimed

The inspected implementation wires parsing, bounded selection, cuts and separate commitment; it does not establish faithful interpretation, completeness for arbitrary prose, scientific warrant or universal validation across alternate persistence paths. [RT-RTE-reading-selection](#rt-rte-reading-selection) and [RT-RTE-resource-admission](#rt-rte-resource-admission) retain the decisive scope qualifications. The claim is not interpreted as an enclosing runtime's general correctness guarantee.

### Evidenced absences

#### RT-ABS-program-typecheck
Label: ValidateProgram EigenTT check absence

- conclusion status: absent

At the frozen SRC-1 revision, inspected `kernel/src/server/programs.rs` ValidateProgram handling parses the program, checks component templates and output schemas, and returns a declared type. Searching that file for `type_check`, `check::check`, and handler/check labels and inspecting the complete handler supports the narrow absence of an EigenTT type-check invocation in that handler. `kernel/src/program/eval_io.rs` additionally shows body parsing followed by IO evaluation, not an automatic call to this validation RPC. This does not assert absence of type checking elsewhere in Eigenius, nor absence of all execution-time checks. It prevents treating ValidateProgram's `valid` field as a well-typedness certificate.

> "program static checks passed; no EigenTT type-check ran (#143)"
> --- `kernel/src/server/programs.rs`

### Behavioral-authority paths

#### RT-BAP-retained-program
Label: Retained program execution authority

Consumer: shared IO evaluator. Channel: IRI resolution of a chain-resident program into its symbolic expression body. Force: executable control over supported evaluation/dispatch operations, within the active registry; not merely information delivered to a chat model. Horizon: subsequent invocations while the resource remains resolvable. [RT-OBJ-program-resource](#rt-obj-program-resource) and [RT-RTE-program-execution](#rt-rte-program-execution) give identity and enforcement limits. SRC-1, `kernel/src/server/programs.rs`, `kernel/src/program/eval_io.rs`.

> self.execute_program(&branch, program, input).await
> --- `kernel/src/server/programs.rs:768-806`

#### RT-BAP-completion-prompt
Label: Component prompt interpretation authority

Consumer: CompleteText's Anthropic model. Channel: component user/system prompt strings with input-resource interpolation. Force: requested natural-language guidance, not guaranteed compliance or authority to alter registry grants. Horizon: the current call, or later calls if a containing program/template remains retained and is invoked again. [RT-CMP-completion-model](#rt-cmp-completion-model) and [RT-RTE-program-execution](#rt-rte-program-execution) distinguish this from symbolic execution and formalization's separate decision model path. SRC-1, `orchestration/src/components/complete_text.ts`.

> const prompt = formatPrompt(userPrompt, req.input);
> --- `orchestration/src/components/complete_text.ts`

## Annotations

none
