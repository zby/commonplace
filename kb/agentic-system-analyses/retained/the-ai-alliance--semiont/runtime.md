---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Semiont runtime baseline tracing gathered-context generation, queued annotation work, direct admission and compiler repair at the frozen repository revision."
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
---

# Semiont runtime report

## Runtime account

Semiont's inspected work is a service-mediated knowledge workflow, not a foreground assistant with an unrestricted tool loop. A client can gather retained knowledge, delegate generation or annotation work to configured model agents, and admit the resulting bytes and annotations to the record. The Worker owns processor execution; the Dispatcher owns job selection and lifecycle; the Archivist owns resource/event admission. The client, not the generating model, selects which of these workflows to invoke. This is an implementation account under SRC-1, not a supplied execution trace. Operation, activation and benefit remain unobserved throughout.

### Ordinary invocation: annotation to generated resource

The shipped MCP `yield_from_annotation` handler is a concrete client path. An external MCP caller supplies resource/annotation identifiers and generation options. The handler gathers around that annotation with a 2,000-character context-window option, then delegates the gathered context with title, storage URI, optional instruction and languages. It follows progress and returns a completion message or an error. It does not return the generated document or resource ID in its success message. The handler also does not set `cite`; the existence of a citation-capable Worker does not establish citations on this ordinary MCP route. SRC-1, `packages/mcp-server/src/handlers.ts`; [RT-RTE-yield-generation](#rt-rte-yield-generation), [RT-RTE-annotation-gather](#rt-rte-annotation-gather).

The Librarian resolves the annotation against the source resource's current view, optionally reads source and linked-target text, builds graph context and requests similar annotations. Separate model calls may summarize linked content and describe relationships. Some supplementary failures degrade the answer instead of failing the gather. The Worker does not blindly deliver every returned field to its model: prompt code selects the annotation's first textual comment/assessment body, hint and selected surrounding text, graph-derived connections, relationship sentence and at most three high-scoring similar passages of 240 code points each. In particular, the gathered linked-target content/summary is not separately rendered by `_annotation_sections`. This is a material producer/consumer distinction, not a claim that all gathered content reaches generation. SRC-1, `apps/librarian/src/semiont_librarian/annotation_gather.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`.

Delegation crosses the authenticated gateway bus to `job:create`. Gateway code validates a named channel/schema, applies emit limits and replaces caller-supplied identity/roles with the verified principal. Dispatcher admission deserializes the request, derives the source resource from the context focus, checks named entity types where present, rejects unsupported yield parameters, and stores the job in its queue. It does not establish that a client-supplied context truthfully represents the current KB. The Python SDK exposes the equivalent `yield_.delegate(params)` path, deriving the resource from context and following completion. SRC-1, `apps/gateway/src/routes/bus.rs`, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/handlers/src/handlers.rs`, `packages/sdk-python/src/semiont/namespaces/yield_.py`.

Each configured Worker agent signs in under a gateway-issued DID for its provider/model, opens an SDK stream naming the channels it consumes, and claims matching jobs one at a time. Other configured agents can run independently. A successful claim requires a worker role and causes the Dispatcher to emit a source-resource assignment naming holder and requester. The Worker starts the job, checks its own accepted filters again, validates generation parameters, assembles a fresh prompt and invokes its configured inference client. The decision policy is split: symbolic code routes and validates; natural-language instructions and retrieved text influence model generation; distributed parameters produce the answer. Neither a general conversation history nor an autonomous choice of arbitrary next tools appears in this inspected generation path. SRC-1, `apps/worker/src/semiont_worker/agent.py`, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`; [RT-CMP-worker-inference](#rt-cmp-worker-inference).

The result is transformed into a bounded artifact, uploaded over the content path and admitted as a resource. Annotation-focused creation attempts source-annotation binding; resource-focused generation commits a link on the source resource. Generated citations are a separate batch on the new resource. The job assignment is on the original focus resource, but Archivist checks the commit target's log for that assignment, so this caller's nonempty generated-citation batch is refused before recording any citations. Token resolution and citation construction do not establish durable citation admission. The gateway forwards uploader identity/roles to the Archivist. The Archivist stores bytes, then invokes resource admission, records a `YieldCreated` event, updates local views/staging and queues a fact. The Worker reaches completion with new resource ID/name and truncation flag only after upload and successful commits, or an empty citation batch that the SDK skips. Nonempty generated-citation batches instead enter failure handling after upload and any source linkage. See the implementation mismatch evidence in [RT-RTE-yield-generation](#rt-rte-yield-generation), SRC-1, `packages/sdk-python/src/semiont/claims.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`. These are separate effects, not one distributed transaction. A resource can exist before citation work or completion; automatic linking from an annotation can warn and fail after resource creation without withdrawing that resource. SRC-1, `apps/gateway/src/routes/content.rs`, `apps/archivist/src/surface.rs`, `apps/archivist/src/commands.rs`, `apps/archivist/src/archivist.rs`, `apps/worker/src/semiont_worker/held_job.py`.

### Three forcing cases and guarantee boundaries

1. **Direct content admission bypasses model generation.** MCP `yield_resource` and SDK uploads submit caller-authored bytes directly. A non-worker writer need not cite a job; a worker-role writer must cite one, and the recorded assignment must name that writer as holder. This tests and rejects any inference that all resource creation passes through generation, per-content human approval, or a model-quality gate. The upload surface stores bytes before command admission, so a refused command does not imply no filesystem effect. See [RT-RTE-resource-admission](#rt-rte-resource-admission).
2. **Annotation jobs commit incrementally.** A mark job reloads its resource, prepares text and dispatches by motivation. It commits each chunk before advancing its checkpoint. Cancellation can leave already committed annotations; retry state can resume work. This rejects a universal all-or-nothing interpretation of job cancellation or failure. See [RT-RTE-mark-detection](#rt-rte-mark-detection).
3. **PDF output executes a compiler and can re-enter the model.** A yield job requesting PDF generates Typst, invokes a local binary and feeds compile diagnostics back for up to two whole-document repairs. This is a distinct effect boundary from a plain provider call. Cancellation is checked after model responses; it is not an immediate stop of the provider request. There is no subprocess timeout argument in the inspected compiler call, so the model timeout cannot be generalized to compilation. See [RT-RTE-pdf-repair](#rt-rte-pdf-repair).

The load-bearing guarantees are local:

| Owner and enforcement point | Strength and covered paths | Alternate paths, dependencies and limit | Separate conclusion statuses |
|---|---|---|---|
| Gateway `emit`, identity replacement | invariant within this handler: caller JSON cannot choose its effective `_userId`/`_roles` | Content upload has a separate authenticated forwarding path. Archivist's internal HTTP surface accepts service-role tokens and forwarded principal headers; trusted services/issuer and network configuration remain external contracts. Not a global hostile-service isolation proof. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Dispatcher claim handler, worker-role check | policy: only a worker-role claim passes this check | Direct content writes are not claims. Actual issued roles/grants and deployed isolation are not supplied. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Archivist `requester_of` and `yield_create` | protocol: job-citing resource creation must match a recorded source assignment and holder; worker-role resource creation must cite a job | Non-worker creation without a job is allowed. Checks are provenance/admission checks, not truth verification. The assignment must have reached the record before creation is checked. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Worker `commit_chunk` | protocol: checkpoint follows successful annotation commit in this caller | Does not prove an atomic transaction across record and queue. Direct annotations and a crash between commit/checkpoint are different cases. Requires SDK/transport commit acknowledgment. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Worker `_bounded` | best effort: async inference waits have a ten-minute bound | Depends on coroutine cancellation and provider-driver behavior; no claim of provider-side billing cancellation. Typst compilation is outside this bound. | implementation conclusion status: wired; operation conclusion status: uninspected |

SRC-1, `apps/gateway/src/routes/bus.rs`, `apps/gateway/src/routes/content.rs`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`, `apps/archivist/src/surface.rs`, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/inference_call.py`, `apps/worker/src/semiont_worker/generation/typst.py`. Supporting passages are retained in the route records below.

Capability surface, grant set and isolation are different. The inspected clients expose read, gather, annotation, bind, direct upload and delegated generation operations. Dispatcher claims need worker roles; internal Archivist HTTP needs a service-role token; configured agents have provider credentials and job filters. No deployed token roster, filesystem permissions, container/network policy or live service configuration was supplied. The compiler runs model-produced Typst through a fixed argv, not through a model-selected shell command. Its actual effective filesystem/network isolation depends on the binary and deployment; it is not established by using a temporary directory. The inspected OpenAI request sends a prompt and generation controls, with no tools argument; this does not establish the same capability boundary for every provider, Browser/desktop extension, host callback or external assistant. SRC-1, `packages/mcp-server/src/handlers.ts`, `apps/worker/src/semiont_worker/service.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/surface.rs`, `packages/inference-python/src/semiont_inference/openai.py`, `apps/worker/src/semiont_worker/generation/typst.py`.

### Recovery, change and coverage limits

Worker progress delivery is best effort. Job exceptions become classified failure reports where possible; a failure report that cannot be delivered leaves recovery to Dispatcher sweeping. A worker stall exits the process for its supervisor to restart. Queue code recovers stale running jobs from progress age and prunes terminal job records after configured retention. Admission initializes mark jobs with one retry and yield jobs with zero; this is not an exactly-once generation guarantee. Resource bytes and record events outlive a returned job status through separate storage paths; complete Git durability, projection replay and repair semantics are left to further analysis. SRC-1, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/agent.py`, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/jetstream/src/lib.rs`, `apps/archivist/src/archivist.rs`.

The material implemented change admission here is knowledge-content admission: software can generate and commit without a per-item human approval step in these routes; clients can also supply content directly. Caller identity alone does not tell whether a human or external computation authored those direct inputs. Separate commands update annotation bodies and register entity types/tag schemas; the latter affect admission vocabulary. Worker providers/models, endpoints and filters come from operator-supplied configuration read at boot. That establishes configuration-directed capability selection, not runtime self-modification. No product-code, prompt-file or production-machinery self-update is inferred from generated resources. Memory revisions and durable knowledge transformations receive their own specialist account. SRC-1, `apps/archivist/src/commands.rs`, `apps/worker/src/semiont_worker/service.py`, `packages/inference-python/src/semiont_inference/factory.py`.

Added implementation inspection under SRC-1 includes MCP handlers; Python SDK job/yield namespaces and held-job commit refusal/acknowledgment handling in `packages/sdk-python/src/semiont/claims.py`; gateway bus/content handlers; Dispatcher admission/handlers and bounded JetStream recovery/checkpoint sections; Archivist upload authentication/storage/admission and append paths; Worker agent/service/job/processors, prompt, inference bound and Typst implementation; Librarian annotation gather; inference factory/OpenAI request; vector embedding interface/factory. These extend the boundary's initial inspection, not its source identity. Browser/desktop-specific admission/review, full launcher policy, all provider-native alternatives, complete graph/vector maintenance, conformance harness assertions and production deployment remain uninspected here. No repository access gap or execution evidence was supplied. The boundary remains a complete artifact with a partial-loop account, not an exhaustive control audit.

## Shared records

### Components

#### RT-CMP-worker-inference
Label: Worker inference client

Source-native identity: the `InferenceClient` constructed for each Worker configuration agent. Representational form: distributed-parametric model behavior consumed through text/structured inference, with symbolic provider/model/base-URL configuration. Storage substrate: externally served model parameters; local client object/configuration holds access details, not weights. SRC-1, `apps/worker/src/semiont_worker/service.py`, `packages/inference-python/src/semiont_inference/factory.py`, `packages/inference-python/src/semiont_inference/openai.py`.

Parameter changes during operation: the inspected caller submits inference, not parameter updates; provider-internal parameter changes are uninspected. Exact version pinning: the mechanism accepts a configured model string, not a required immutable weights digest; no particular deployed model/version is supplied. Mutable endpoint: configurable `base_url` and model names can resolve to a different backing model; whether a deployment does so is unobserved. Fixed client configuration does not establish fixed remote weights or absence of retained-knowledge adaptation.

> return create_inference_client(
>             provider=entry.agent.provider,
>             model=entry.agent.model,
>             base_url=entry.base_url,
>             api_key=api_key_of(config, index, environment),
>             catalogue=Path(config.model_catalogue),
>         )
> --- `apps/worker/src/semiont_worker/service.py`

The factory supports Anthropic, Google, llama.cpp, Ollama, OpenAI, Together and vLLM; only the OpenAI request body was inspected beyond factory selection. It passes `store=False`, no conversation/previous-response identifier and no tools argument. Provider retention beyond the requested setting, internal reasoning and actual parameter identity remain external.

> model=self.model_id,
>                 input=prompt,
>                 max_output_tokens=max_tokens,
>                 store=False,
> --- `packages/inference-python/src/semiont_inference/openai.py`

#### RT-CMP-gatherer
Label: Librarian gatherer inference

Source-native identity: Librarian gatherer's configured `InferenceClient`, passed into annotation gathering. Representational form: distributed-parametric generation of summaries and relationship sentences; symbolic configuration and natural-language prompts are distinct inputs. Storage substrate: external provider weights and local client configuration. SRC-1, `apps/librarian/src/semiont_librarian/service.py`, `apps/librarian/src/semiont_librarian/annotation_gather.py`, `packages/inference-python/src/semiont_inference/factory.py`.

Parameters during operation: no update requested by the inspected gather calls; provider internals uninspected. Exact version: configured model identifier, no universal immutable-revision requirement established by factory. Mutable endpoint: the configured provider URL/model may resolve to another model. This is a distinct operational client from the Worker, even if a deployment happens to give both the same model.

> summary = await ask(inference, summarizing)
> --- `apps/librarian/src/semiont_librarian/annotation_gather.py`

#### RT-CMP-embedding-provider
Label: EmbeddingProvider

Source-native identity: Librarian `EmbeddingProvider` created from embedding configuration. Representational form: distributed-parametric embedding transformation producing dense numerical query vectors; storage substrate: external model parameters, then transient query vectors and a separately maintained vector index. SRC-1, `packages/vectors-python/src/semiont_vectors/embedding.py`, `packages/vectors-python/src/semiont_vectors/factory.py`, `apps/librarian/src/semiont_librarian/annotation_gather.py`.

Parameters during operation: inspected interface offers embeddings/dimensions, not training; remote updates uninspected. Exact version pinning: factory takes `config.model`, without establishing immutable model revision. Mutable endpoint: Ollama base URL or Voyage endpoint is configurable, and the provider may resolve a model name differently later. Embedding provenance and index/model compatibility require the memory analysis; successful search is not assumed.

> return OllamaEmbeddingProvider(model=config.model, base_url=config.base_url)
> --- `packages/vectors-python/src/semiont_vectors/factory.py`

### Operative objects

#### RT-OBJ-job-params
Label: JobParams

Source-native identity: Dispatcher `JobParams` and metadata for admitted jobs. Representational form: symbolic JSON fields consumed by fixed admission/filter/routing rules; the embedded instruction and gathered prose are natural-language inputs when the Worker builds its model prompt. Storage substrate: job queue records backed by JetStream, with per-attempt in-process held-job state. Not a trained model or a claim of a permanent experience store. SRC-1, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/src/main.rs`, `apps/dispatcher/jetstream/src/lib.rs`.

The queue retains context as job input, while announcements omit generation context; the claiming worker receives the job input. Terminal queue records are subject to retention pruning. This separates delegated visibility from public announcement visibility.

> params: JobParams {
>             resource_id,
>             schema,
>             rest: params,
>         },
> --- `apps/dispatcher/handlers/src/admission.rs`

> /// description less its input. A `mark` job's parameters are announced whole;
> /// a `yield` job's are the ones its request names, which its context is not.
> --- `apps/dispatcher/handlers/src/admission.rs`

### Routes

#### RT-RTE-annotation-gather
Label: Annotation context gathering

Endpoints/progression: client `gather.annotation` request → Librarian view/text/graph reads → optional inference and vector retrieval → structured `GatheredContext` returned to client. Owner: Librarian code controls progression and selected context; models propose optional summaries/relationship sentences, not the next service action. Context/state/effects: a fresh per-request assembly around resource/annotation identifiers, not a shared conversation frame. SRC-1, `packages/mcp-server/src/handlers.ts`, `apps/librarian/src/semiont_librarian/annotation_gather.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: gathered context envelope; MCP gather tool serializes its response as JSON text.
- Later read-back: retained resource views/content, graph and similar annotations are read by a later gather invocation; this route itself does not persist a revised summary or resource.
- Delegated visibility: client receives gathered fields; generation receives the fields its prompt builder selects, not necessarily the entire context.
- Selection predicate: requested resource/annotation, optional source/target inclusion and window; one-link graph neighborhood; selected text embedded for up to ten similar annotations with score threshold 0.5 and source-resource exclusion; matches without readable named resource views are omitted.
- Invalidation or expiry: fresh reads at request time; returned context is a snapshot, with no subsequent automatic refresh of a submitted job's copy established here.
- Activation or effect: code wires context into later generation; actual model reliance or improved answers is unobserved.
- Evidence limits: graph/vector population and full consistency/repair paths are not traced here; some supplementary failures omit fields, so an answered gather need not be complete.

Working-context controls: caller sets inclusion/window; code rejects out-of-bounds windows before reading. Request-local model calls receive selected prompts, not the originating external assistant's full context. Gather output escapes to client; request-local working state is not a retained conversational summary. Later retrieval is a new explicit request. Components: [RT-CMP-gatherer](#rt-cmp-gatherer), [RT-CMP-embedding-provider](#rt-cmp-embedding-provider).

> found = await vectors.search_annotations(
>                 await embedding.embed_query(selection.selected),
>                 SearchOptions(limit=_SIMILAR, score_threshold=LIKE_ENOUGH, filter=SearchFilter(exclude_resource_id=resource_id)),
>             )
> --- `apps/librarian/src/semiont_librarian/annotation_gather.py`

> degraded.note("relationship")
> --- `apps/librarian/src/semiont_librarian/annotation_gather.py`

#### RT-RTE-yield-generation
Label: Delegated resource generation

Endpoints/progression: SDK/MCP generation request → gateway emit → Dispatcher admission/queue/claim → Worker model call → artifact upload → source binding/link → attempted new-resource citation commit → completion for an empty batch, or refusal/failure for a nonempty batch without an assignment on the new resource. Owners: caller chooses task/context/options; Dispatcher decides admission and matches worker filters; Worker code chooses processor and transformations; [RT-CMP-worker-inference](#rt-cmp-worker-inference) proposes document text. State: [RT-OBJ-job-params](#rt-obj-job-params), assignment, progress and held-job state. Effects: resource bytes/record and annotations through [RT-RTE-resource-admission](#rt-rte-resource-admission). SRC-1, `packages/mcp-server/src/handlers.ts`, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: job creation yields an ID; followers receive progress and terminal completion/error. Worker completion includes resource ID/name/truncation; MCP wrapper returns only a completion message and collected progress strings.
- Later read-back: created resource and successfully recorded source links become eligible for later browse/gather. This caller's nonempty generated-citation batch is refused, so it does not establish later-readable citation annotations. Job records support status/recovery until pruned, not permanent learning by themselves.
- Delegated visibility: assigned worker receives the submitted job input; queue announcement omits yield context. Configured streams name consumed channels; this is not a proof of tenant isolation.
- Selection predicate: valid typed yield parameters and registered requested entity types; claim filters choose eligible jobs and Worker rechecks its configured filters. Prompt code sorts semantic matches descending, takes three, clips each to 240 code points; resource-focused main/related contents are clipped individually to 4,000.
- Invalidation or expiry: job context is submitted by value; cancellation is checked after generation calls; terminal queue retention is configured. No automatic proof of freshness or truth for submitted context.
- Activation or effect: ordinary code can automatically upload model output and bind/link it to the source without an inspected per-document human gate. Nonempty generated citations are constructed but refused at commit because the assignment is on the source, not the new resource. Empty batches make no commit request and can reach completion; exercise and downstream behavior change are unobserved.
- Evidence limits: no supplied run; source grounding is an instruction plus token processing and attempted attribution, not a factual entailment or successful citation-admission guarantee. Citations are optional, and the inspected MCP delegate does not request them. No alternative shipped assignment transfer or commit resolution is established in the inspected Dispatcher claim, Archivist creation/commit and Worker/SDK chain.

Admission/change fields: trigger is an open client request, not a bounded improvement experiment. Proposed change is a generated knowledge resource. Software admits based on schema, supported format/output budget and record provenance checks; the model proposes content. Caller can request cancellation, Worker can fail, compiler can reject PDF, Archivist can refuse admission. Initiating a job is not per-content approval; actual human authorship/control remains unresolved from a generic caller principal. No expected-answer oracle is used for factual correctness in this route. Guidance consists of job instruction, static prompt requirements and selected retained context; the uploaded artifact, generation-prompt field where present and record lineage persist, not a demonstrated method revision. Rollback is not atomic: cancellation before upload avoids resource creation in that branch, while failures after upload may leave content/record effects; other commands can archive/delete annotations but no universal job rollback is established. In particular, the new-resource citation refusal propagates through the SDK into Worker failure handling after resource creation and any source linkage. Upload admission checks the source assignment through `generatedFrom.resourceId`, whereas annotation commit checks its target resource; upload success does not satisfy that later check.

> made = await process_generation_job(inference, params, on_progress=reports.say, cancelled=job.cancelled)
> --- `apps/worker/src/semiont_worker/held_job.py`

The assignment/commit mismatch is implementation evidence under SRC-1, not merely an operational uncertainty:

> resource_id: job.params.resource_id.clone(),
>             holder,
>             requester: job.metadata.user_id.clone(),
> --- `apps/dispatcher/handlers/src/handlers.rs`

> await job.commit(new_resource_id, await _citations(job, client, made, new_resource_id, generator, reports))
> --- `apps/worker/src/semiont_worker/held_job.py`

> if not annotations:
>             # A batch of no annotations is no commit: there is nothing to establish.
>             return
> --- `packages/sdk-python/src/semiont/claims.py`

> await self._answered(MARK_COMMIT, MarkCommitCommand(resource_id=resource_id, annotations=list(annotations), job_id=self.job_id))
> --- `packages/sdk-python/src/semiont/claims.py`

> Some(job_id) => requester_of(archivist, resource_id, job_id, user)?,
> --- `apps/archivist/src/commands.rs`

> "refused: cites job {job_id}, but this resource's log holds no assignment for it"
> --- `apps/archivist/src/commands.rs`

The SDK rethrows non-timeout refusals; the Worker catches failures and attempts `job.fail`. This prevents the later completion call but does not reverse already admitted bytes/events. SRC-1, `packages/sdk-python/src/semiont/claims.py`, `apps/worker/src/semiont_worker/held_job.py`. The route's wired status describes these implemented branches, not successful durable citations.

> best = sorted(similar, key=lambda match: match.score, reverse=True)[:SEMANTIC_MATCH_LIMIT]
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

> "\n- Ground every claim in the provided context. Immediately after each claim, cite its source by emitting [[<id>]], "
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

Worker async inference timeout owner is `_bounded`, with best-effort ten-minute cancellation of the awaiting coroutine. Its required external contract is a cancellation-cooperative driver/provider; source alone does not show server-side cancellation. Runtime-client controls include accepted job filters, provider/model configuration, token/temperature/output settings, caller cancellation and progress/follower stall deadlines. They do not establish arbitrary tool access by the model.

> async with bound:
>                 return await ask()
> --- `apps/worker/src/semiont_worker/inference_call.py`

#### RT-RTE-resource-admission
Label: Resource upload and record admission

Endpoints/progression: MCP/SDK direct bytes or Worker artifact → authenticated gateway content upload → service-authenticated Archivist HTTP → file store → `yield_create` → event append/views/staging/fact → resource ID. Owner: gateway supplies principal, Archivist decides command acceptance and executes effects. This route admits knowledge changes, including caller-supplied content that did not pass through generation. SRC-1, `packages/mcp-server/src/handlers.ts`, `packages/sdk-python/src/semiont/namespaces/yield_.py`, `apps/gateway/src/routes/content.rs`, `apps/archivist/src/surface.rs`, `apps/archivist/src/content.rs`, `apps/archivist/src/commands.rs`, `apps/archivist/src/archivist.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: gateway upload answers HTTP 202 with the recorded resource ID, not a model-quality verdict.
- Later read-back: bytes at a storage URI and resource views/events can be consumed by browse/gather; detailed storage revisions and Git synchronization are left to memory analysis.
- Delegated visibility: gateway forwards principal and roles; internal upload requires issuer-verified service role. Other trusted service callers are therefore a different trust path from public client JSON.
- Selection predicate: required name/format/storage URI/file, supported media type, storage-URI syntax and command attribution; worker-role creators must cite a source job assigned to them.
- Invalidation or expiry: newly minted resource identity and content checksum recorded; no universal expiry or automatic rollback inferred. Storage writes occur before command acceptance and can overwrite a requested location.
- Activation or effect: files, resource creation event, views/staging and queued fact; later consumer activation remains unobserved.
- Evidence limits: syntax-based path checks are not a complete filesystem isolation audit; service credentials, symlinks and deployed grants are not assessed. Record creation, source linking and queue completion are separate effects.

Admission/change fields: trigger is upload or a generation's artifact; proposal author can be human, software or model. Archivist code decides, with format/provenance/checksum refusal; no inspected per-content human acceptance or answer oracle. Mode is open requests. Guidance comes from supplied bytes/metadata or generation guidance; stored content and provenance persist. Cancellation of an upstream job does not reverse an already accepted resource. `yield_create` attempts annotation linkage after recording creation and only warns on linkage failure. Direct non-worker uploads without job ID remain valid; therefore the assignment protocol covers job-citing and worker-role admission, not all creation.

> if holds_worker_role(command) && job_id.is_none() {
>         return Err(
>             "yield:create refused: a worker-role emitter must cite the job it fulfils in `jobId`"
>                 .into(),
>         );
>     }
> --- `apps/archivist/src/commands.rs`

> if holder != writer {
>         return Err(format!(
>             "refused: job {job_id}'s recorded holder is {holder}, not the writer {writer}"
>         )
>         .into());
>     }
> --- `apps/archivist/src/commands.rs`

> let held = archivist
>             .content
>             .store(&fields["storageUri"], &file)
>             .await?;
> --- `apps/archivist/src/surface.rs`

> .is_ok_and(|claims| has_role(&claims, SERVICE_ROLE)),
> --- `apps/archivist/src/surface.rs`

> payload.remove("_roles");
>     payload.insert("_userId".to_owned(), json!(principal.did));
> --- `apps/gateway/src/routes/bus.rs`

#### RT-RTE-mark-detection
Label: Delegated annotation detection

Endpoints/progression: mark job admission → filtered worker claim → fresh resource descriptor/text preparation → motivation-specific model processor → chunk annotation commits/checkpoints → counts or decline/cancel/failure. Owner: client selects job/motivation; Dispatcher checks vocabulary/schema; Worker code selects processor and commits model proposals after transformation. Context: request-local source pieces and relevant schema, not a retained conversation. Effects: annotations on an existing source and checkpoint state for recovery. SRC-1, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/processors.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: completion counts or readable decline; otherwise cancellation/failure with available unit/checkpoint data.
- Later read-back: annotations are later browsable/gatherable; cursors/completed units are handed into later attempts. Recovery metadata is not itself demonstrated experience-based learning.
- Delegated visibility: worker receives source resource ID, job parameters and any attached tag schema; source text is loaded by worker; public announcement rules differ from yield jobs.
- Selection predicate: job filters, motivation, registered entity types/tag schema and media-dependent readable text; processor units differ for motivation/entity type/tag category.
- Invalidation or expiry: cancellation stops at processor stopping places, not before every already committed piece. Terminal queue state is eventually pruned; detailed annotation revision semantics are deferred.
- Activation or effect: annotation chunks are committed before checkpoints advance, and can survive later failure/cancellation; actual usefulness and model precision are unobserved.
- Evidence limits: detection parsers, anchor auditing and every motivation's prompt/validation were not exhaustively traced; do not infer correct tagging, assessment or factual criticism from route names.

Admission/change fields: model proposes annotations, software transforms/commits; no per-annotation human approval appears in this worker loop. Human versus automated source job request is unresolved. Code may decline unreadable inputs or reject unsupported configurations; caller cancellation can stop later work, not undo committed pieces. Operating mode is open requests with limited failure retry, not a curriculum. No independent expected-answer oracle established. Guidance consists of motivation, job parameters, schema and static prompts; committed annotations persist. This establishes a knowledge-writing mechanism, not a theory-builder assessment: an `assessing` motivation alone supplies no evidence of localized theory, blame assignment or iterated theory revision.

> await job.commit(job.resource_id, annotations)
>         unit_cursors[checkpoint.unit] = checkpoint.cursor
>         stood.unit_cursors = dict(unit_cursors)
>         await job.checkpoint(list(stood.completed_units), dict(unit_cursors))
> --- `apps/worker/src/semiont_worker/held_job.py`

> max_retries: match job_type {
>                 JobType::Mark => 1,
>                 JobType::Yield => 0,
>             },
> --- `apps/dispatcher/handlers/src/admission.rs`

> "job:claim refused: the caller is not a worker for this knowledge base".to_owned(),
> --- `apps/dispatcher/handlers/src/handlers.rs`

#### RT-RTE-pdf-repair
Label: Typst compile repair

Endpoints/progression: generation requests PDF → model Typst response → citation-token transformation → local Typst compile → on compile error, bounded regeneration with source/diagnostics → PDF or failure. Owner: Worker code decides whether another repair is allowed; model proposes whole replacement; compiler supplies acceptance/rejection for syntactic/rendering success. Executor/effect boundary: Python subprocess with fixed argv and temporary files, then artifact upload via the parent generation route. SRC-1, `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/worker/src/semiont_worker/generation/typst.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: compiled PDF bytes or raised failure after bounded repair/truncation failure; parent route returns job result only after upload/commit.
- Later read-back: successful artifact is stored through resource admission; failed source and diagnostics are current-job repair input, not an established durable repair-knowledge store.
- Delegated visibility: repair model receives original generation framing plus failed source and compiler diagnostic; no external assistant conversation is implicitly copied.
- Selection predicate: PDF format and failed compilation; at most two repairs, with early failure if generated source was truncated. Successful compilation ends repair.
- Invalidation or expiry: each replacement supersedes current source in local state; temporary compile directory is removed on exit; parent job can fail without admitting a resource.
- Activation or effect: code wires compiler feedback into a new model invocation and executes successful replacement through compiler; successful execution and improvement are unobserved.
- Evidence limits: compilation success checks format, not truth, citation entailment or safety. No subprocess timeout/root confinement argument in the inspected call; deployed Typst behavior and isolation are external contracts.

Admission/change fields: trigger is a compile failure; proposed change is whole Typst replacement. Software decides repair count; compiler vetoes invalid output; human supplies original job but no intermediate approval. Answer oracle: actual local compiler result/diagnostics provide reference success for compilation only, not an expected semantic answer. Mode is a bounded repair loop inside an open-request workflow. Guidance explicitly asks to fix the compiler error and return the full source; what persists is successful PDF via the parent route, not a generalized repair policy. This is program-artifact repair, with no formulated explanatory theory established, so no theory-builder conditions are inferred from repetition. Rollback/recovery: failures discard temporary compilation files and fail job before upload; a process wedged in compilation needs external process supervision rather than the async inference bound.

> MAX_COMPILE_REPAIRS: Final = 2
> --- `apps/worker/src/semiont_worker/generation/typst.py`

> generated = await generate_resource_from_topic(params, output_media_type, client, Repair(source=source, error=compiled.error))
> --- `apps/worker/src/semiont_worker/processors.py`

> ran = subprocess.run(
>             ["typst", "compile", "--creation-timestamp", str(PINNED_CREATION_TIMESTAMP), str(in_file), str(out_file)],
>             stdin=subprocess.DEVNULL,
>             capture_output=True,
>             check=False,
>         )
> --- `apps/worker/src/semiont_worker/generation/typst.py`

### Claims

#### RT-CLM-source-grounding
Label: Context grounding instruction

Claimed operation: generation requests context-grounded claims and source-ID tokens when `cite` is enabled. Source: SRC-1, `apps/worker/src/semiont_worker/generation/resource_generation.py`, with minimum passage in [RT-RTE-yield-generation](#rt-rte-yield-generation). The processor resolves tokens against citable IDs and constructs citation data; the Worker constructs annotations and attempts their commit on the new resource. The SDK supplies the held job ID, but Archivist requires its assignment in that new resource's log, while Dispatcher assigned it on the original focus resource. Nonempty batches from this chain are therefore refused, not durably admitted attribution. Empty batches are skipped and can permit completion; source binding/linking and resource upload remain independently supported. This is a grounding instruction and token-processing mechanism, not an answer oracle proving entailment or a successful citation-admission progression. PDF citation anchoring may drop a claim not found in rendered text, or all claims when text cannot be obtained. The uploaded resource remains even if the remaining nonempty batch is refused. SRC-1, `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/held_job.py`, `packages/sdk-python/src/semiont/claims.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`; mismatch passages are retained in [RT-RTE-yield-generation](#rt-rte-yield-generation). The implementation status below covers instruction, token processing and attempted commit, not successful new-resource citation admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> "PDF citations dropped \N{EM DASH} the generated artifact's text is not to be had",
> --- `apps/worker/src/semiont_worker/held_job.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-generation-prompt
Label: Generation prompt authority

Consumer: configured Worker inference model. Channel: fresh natural-language prompt assembled from job instruction, source context, graph/relationship prose and selected semantic matches. Force: requested model behavior, not guaranteed obedience; symbolic code determines what is sent and whether the result is compiled/admitted. Horizon: one generation invocation, plus failed-source/compiler feedback across PDF repair calls; later knowledge influence requires storing and retrieving the admitted resource. SRC-1, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/worker/src/semiont_worker/processors.py`; [RT-RTE-yield-generation](#rt-rte-yield-generation), [RT-RTE-pdf-repair](#rt-rte-pdf-repair).

> instruction = f"Instruction: {params.prompt}" if params.prompt else ""
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### RT-BAP-worker-config
Label: Worker configuration authority

Consumer: Worker service boot and inference factory. Channel: operator-supplied configuration document and named environment credentials, symbolically selecting model/provider/base URL and accepted jobs. Force: code-enforced configuration of clients and claims, with model behavior still opaque. Horizon: service process lifetime; rereading/restarting under changed configuration can change later work. No autonomous edit of that configuration is established by generated knowledge. SRC-1, `apps/worker/src/semiont_worker/service.py`, `apps/worker/src/semiont_worker/agent.py`; [RT-CMP-worker-inference](#rt-cmp-worker-inference).

> clients = [_client_of(config, index, environment) for index in range(len(config.agents))]
> --- `apps/worker/src/semiont_worker/service.py`

## Annotations

none
