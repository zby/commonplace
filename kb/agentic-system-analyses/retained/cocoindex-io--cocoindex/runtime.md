---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "CocoIndex runtime baseline: incremental indexing, live maintenance, preview, model extraction and shipped retrieval at the frozen revision."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
---

# CocoIndex runtime report

## Runtime account

CocoIndex executes caller-authored processing functions and reconciles their declared target states. It is not, on these inspected paths, an autonomous agent selecting its own tasks. The ordinary shipped text example supplies the consequential loop: Markdown files become chunks, vectors and PostgreSQL rows; a separate query invocation retrieves and displays retained text. The broader maintenance claim is declared in SRC-1, `pyproject.toml`, as quoted in [the boundary](boundary.md#boundary-and-evidence). This report establishes wiring, not successful execution or benefit.

### Ordinary invocation and control ownership

The example documents `cocoindex update main`. The CLI loads an application and starts `app.update`; the Python API creates a root processor at `StablePath()` with application arguments, environment context and deadline. The Rust core spawns a Tokio operation, runs that processor, reports readiness and termination, and returns a handle's result. Async Python, blocking Python and the Rust SDK are material alternate entry paths into the same core engine. The Rust SDK constructs a processor around the supplied closure and forwards full-reprocess, live, deadline and preview options. CLI-only checks do not govern those API callers. SRC-1: `examples/text_embedding/main.py`, `python/cocoindex/cli.py`, `python/cocoindex/_internal/app.py`, `rust/core/src/engine/app.rs`, `rust/sdk/cocoindex/src/app.rs`.

[RT-RTE-index-update](#rt-rte-index-update) records the production path. The application author decides the source root, file filter, splitter, model and schema in symbolic Python code. The operator triggers an update; the engine owns scheduling and reconciliation, not semantic truth. Files are mounted by source key, chunks receive generated IDs, and declared rows contain filename, offsets, original text and an embedding. The process-file function is memoized. The embedding call is separately memoized and batched on a GPU runner. Resource contexts provide a database pool and change-detected embedder. The return is application completion (`None` in this example), not the retrieved answer. Later queries are separate consumers.

The claim that unchanged work is skipped is conditional. Component-memo restoration checks processor fingerprints, logic dependencies and target-provider dependencies; the component path can also revalidate memo states. Failure to restore logs an error and proceeds without the memo. This is dependency-tracked reuse, not proof that every external change, such as replacement weights behind an unchanged model name, is detected. SRC-1: `rust/core/src/engine/execution.rs`, `rust/core/src/engine/component.rs`; [RT-OBJ-component-memoization](#rt-obj-component-memoization), [RT-CMP-sentence-transformer-embedder](#rt-cmp-sentence-transformer-embedder).

### Forcing cases and guarantee coverage

Three maintenance forcing cases test overbroad readings of the ordinary path.

1. **Live rather than finite catch-up.** A source's `live=True` capability does not itself select a continuously running app. The example explicitly separates it from the CLI `-L` grant. LocalFS starts the watcher before its initial scan, signals ready, dispatches path updates/deletes and periodically recreates the watcher and rescans when configured. Core live mode waits for descendants after initial readiness. Thus ready does not mean terminal completion. [RT-RTE-live-maintenance](#rt-rte-live-maintenance).
2. **Preview rather than apply.** CLI rejects preview combined with reset or live. Both SDKs nevertheless expose their own options. The core preview branch plans target actions, contributes no tracking writes through its precommit callback, collects actions and returns before normal submit. This is a target-reconciliation guarantee, not an execution sandbox: arbitrary application functions, document conversion, embeddings, direct model calls and direct database calls can still run before declarations reach that branch. [RT-RTE-preview-update](#rt-rte-preview-update).
3. **Explicit drop rather than ordinary orphan cleanup.** Drop cancels the app and snapshots live components under a registry lock, drains them, deletes the root and clears per-app storage. It installs an error handler that propagates deletion failures; ordinary update's root orphan cleanup may log and swallow errors while retaining tombstones for retry. Drain timeouts limit quiescence assurance. [RT-RTE-drop-app](#rt-rte-drop-app).

The principal guarantees have different owners and strengths:

| Guarantee | Owner and enforcement | Strength and covered paths | External contract / limit | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| Preview does not apply planned target actions | Core submit preview branch | invariant within that branch; Python and Rust preview feed it | Custom code or reconciliation callbacks can have their own effects; not a no-I/O promise | wired | uninspected |
| Memo reuse is dependency-conditioned | Core component restore and memo validation | protocol for tracked processor, logic, state and provider dependencies | External dependencies must expose meaningful change information; alias identity alone is insufficient | wired | uninspected |
| Component concurrency can be bounded without blocking all descendants | Core admission pool and parent-to-child token loans | protocol for admitted component runs; not a hard total-process memory or provider-request cap | `None` creates an unbounded pool; user code and provider batching have separate controls | wired | uninspected |
| Explicit drop surfaces target-deletion failures | Core drop installs raising handler before delete | protocol for this drop path, not ordinary root orphan cleanup | Connector deletion and external stores must succeed; timed-out live drains can outlast the wait | wired | uninspected |

The admission mechanism is load-bearing for scheduling, not knowledge admission:

> pub fn new(max_inflight_components: Option<usize>) -> Self {
>     Self {
>         semaphore: max_inflight_components.map(|n| Arc::new(Semaphore::new(n))),
>     }
> }
> --- `rust/core/src/engine/admission.rs`

That implementation qualifies any universal resource-bound claim. The same module describes parent-token loans: nested work can run even when pool tokens are exhausted, so active runs can exceed the pool count along a component chain. It does not prove a deployed memory bound or measured performance. SRC-1: `rust/core/src/engine/admission.rs`.

### Model work, capability grants and effects

The embedding component is distributed-parametric; the inspected wrapper calls encode, not a training operation. Its model name is not an exact weights revision. The GPU runner defaults to in-process execution and can pickle functions/arguments to a subprocess. That is a process-placement choice, not a demonstrated privilege boundary. The subprocess executes the deserialized callable and returns a pickled result; broken pools are restarted. The current grant set in the text example is a source directory, database pool and embedder. The capability surface is broader because caller-authored Python/Rust functions can perform direct effects. No deployment configuration or OS-level isolation evidence is supplied. SRC-1: `python/cocoindex/_internal/runner.py`, `examples/text_embedding/main.py`.

A materially different shipped model route is [RT-RTE-manual-extraction](#rt-rte-manual-extraction). It invokes Instructor over `litellm.acompletion` directly, not the CocoIndex LiteLLM embedding/transcription wrapper. PDF-derived Markdown is placed in a user message alongside a system extraction instruction; a typed result is validated and declared as a PostgreSQL record. The model proposes extracted content; schema validation checks shape rather than entailment by the manual. There is no per-result human gate in this inspected route. That positive witness prevents treating all target work as deterministic embedding, or treating one adapter's controls as universal provider mediation. [RT-CMP-llm-model](#rt-cmp-llm-model) records endpoint uncertainty.

[RT-RTE-query-index](#rt-rte-query-index) separately shows retained content reaching a consumer: query embedding, SQL distance ordering, top-k rows, then printed text. This establishes a delivered search result, not use by an answering agent or correctness of an answer. The example's stale comments say “no vector index,” but executable production code declares a vector index. The route therefore relies on executable SQL ordering rather than the comment for selection semantics. SRC-1: `examples/text_embedding/main.py`.

### Evidence and remaining coverage

All findings use SRC-1 at the boundary's commit, with implementation evidence from the paths cited here. Added inspection beyond the boundary's initial inventory covers the sentence-transformers wrapper, the manuals extraction example, core memo dependency checks and preview submit branch, LocalFS watcher body, GPU runner execution, PostgreSQL row-action body and Rust SDK option forwarding. Source passages are implementation evidence; examples' instructions and prompts also expose declared intent. No target program, test, model or provider was executed. No supplied trace or experiment establishes activation, reliability, latency, retrieval quality or improvement.

The selected cases are not an exhaustive connector audit. Other graph, image, session-search and extraction examples remain included but their detailed runtime behavior is uninspected here. The same holds for other model wrappers, provider-native tools, custom extension effects and remote execution arrangements not traced above. They cannot inherit preview safety, memo freshness or approval conclusions merely by belonging to this repository. Detailed persistence revision mechanisms are left to the memory member. No source-wide absence of autonomous loops, learning or theory construction is asserted from this bounded runtime inspection.

## Shared records

### Components

#### RT-CMP-sentence-transformer-embedder
Label: SentenceTransformerEmbedder

Source-native Python wrapper around a lazily loaded SentenceTransformer. Its model weights are distributed-parametric, held in dependency-managed model memory/cache; wrapper configuration is symbolic Python state. SRC-1: `python/cocoindex/ops/sentence_transformers.py`, `examples/text_embedding/main.py`.

Parameters change during operation: the inspected route calls `model.encode` and exposes no training update; dependency internals are uninspected. Exact version pinned: no; the example supplies `sentence-transformers/all-MiniLM-L6-v2`, not a revision or weights digest. Mutable endpoint resolution: a name or local model path can resolve to different material outside this repository pin; actual resolution is unobserved. The wrapper memo key contains model name/path, device and trust-remote-code flag, not a resolved weights digest. `trust_remote_code` defaults false but is configurable. These limits apply independently of persistent embedding memoization.

> def __coco_memo_key__(self) -> object:
>     return (self._model_name_or_path, self._device, self._trust_remote_code)
> --- `python/cocoindex/ops/sentence_transformers.py`

OOM handling requests smaller batches; other exceptions propagate. This supports an implemented retry affordance, not observed recovery.

#### RT-CMP-llm-model
Label: LLM_MODEL in manuals extraction

Source-native context key supplying a provider model string, consumed by Instructor/LiteLLM completion. The configuration is symbolic; the invoked model is distributed-parametric and provider-hosted. Parameters changing during operation: uninspected provider internals; the shipped caller requests inference and performs no weight update. Exact version pinned: no; environment overrides the default `openai/gpt-4o`. Mutable endpoint can resolve to another model: yes as an exposed configuration/alias possibility, with actual provider resolution uninspected. SRC-1: `examples/manuals_llm_extraction/main.py`.

> builder.provide(LLM_MODEL, os.environ.get("LLM_MODEL", "openai/gpt-4o"))
> --- `examples/manuals_llm_extraction/main.py`

### Operative objects

#### RT-OBJ-component-memoization
Label: ComponentMemoizationInfo

Symbolic serialized return value, processor fingerprint, logic dependencies, provider dependencies and memo states. Storage is the per-app internal state store, identified as LMDB in the boundary's storage account. It is not the PostgreSQL content index. The engine reads it at the stable component path and may reuse the return with retained dependency information. This declares the runtime reuse object, not a finding that it is always fresh. SRC-1: `rust/core/src/engine/execution.rs`, `rust/core/src/engine/component.rs`; [boundary](boundary.md#boundary-and-evidence).

> if memo_info.processor_fp == processor_fp
>     && logic_registry::all_contained_with_env(
>         &memo_info.logic_deps,
>         comp_ctx.app_ctx().env(),
>     )
>     && target_provider_deps_still_valid(
>         memo_info.target_provider_deps.iter().map(|(p, g)| (p, g)),
>         &comp_ctx.target_states_providers()?,
>     )
> --- `rust/core/src/engine/execution.rs`

### Routes

#### RT-RTE-index-update
Label: Text embedding index update

Endpoints: operator CLI or SDK call to application processor, file/chunk processing and PostgreSQL target reconciliation. The application author supplies symbolic processing policy; the engine controls component scheduling and target submission. Natural-language chunks go to [RT-CMP-sentence-transformer-embedder](#rt-cmp-sentence-transformer-embedder); vectors and row keys have numerical and symbolic consumption respectively. A database pool is the executor's external effect capability. SRC-1: `examples/text_embedding/main.py`, `python/cocoindex/_internal/app.py`, `rust/core/src/engine/app.rs`, `python/cocoindex/connectors/postgres/_target.py`.

- Immediate return: UpdateHandle; awaited completion returns app result, `None` for this example, or raises an error.
- Later read-back: Internal component/function memoization is available to later updates; PostgreSQL rows are read by the separate query route.
- Delegated visibility: Chunk processing receives chunk, filename, ID generator and table target; the embedder receives chunk text, not the whole directory or a chat history.
- Selection predicate: Recursive `**/*.md` filter; splitter uses chunk size 2000, overlap 500 and Markdown language; memo reuse is dependency-conditioned.
- Invalidation or expiry: Tracked input/logic/context/provider changes and explicit full reprocess affect reuse; external alias changes without tracked identity changes are not established as detected.
- Activation or effect: Wired row declarations become target actions with upsert/delete dispatch; successful external writes and later behavioral activation are unobserved.
- Evidence limits: Source-only path; neither database semantics nor model correctness independently verified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open operator-triggered indexing, not a bounded improvement experiment. Code proposes rows and the engine/connector admits target changes; the operator can edit source or code, preview, rerun, full-reprocess or drop, but starting an update is not per-content approval. No expected-answer oracle is supplied. Recovery includes reprocessing and explicit drop rather than a demonstrated atomic rollback spanning internal storage and PostgreSQL. Guidance is the fixed pipeline and schema; retained products are rows and memo state, not a revised runtime program.

> embedding=await coco.use_context(EMBEDDER).embed(chunk.text),
> --- `examples/text_embedding/main.py`

> for action in actions:
>     if action.value is None:
>         deletes.append(action)
>     else:
>         upserts.append(action.value)
> --- `python/cocoindex/connectors/postgres/_target.py`

#### RT-RTE-live-maintenance
Label: Live directory maintenance

Endpoints: LocalFS watcher to live subscriber update/delete and the mounted processing loop. Principal is the caller selecting live mode; next-step owner is watcher/subscriber code, not a model. Relative paths identify changed items. SRC-1: `python/cocoindex/connectors/localfs/_source.py`, `examples/text_embedding/main.py`, `rust/core/src/engine/app.rs`.

- Immediate return: Readiness after initial scan; the live update stays active while descendants run.
- Later read-back: Updated index rows and memo state feed later query/update invocations through the ordinary routes.
- Delegated visibility: Subscriber receives matched relative keys and file objects; directory deletion can trigger a complete rescan.
- Selection predicate: Created/modified/deleted/moved file events under the configured root, filtered by matcher; moves become delete plus create.
- Invalidation or expiry: Events update/delete mounted items; configured periodic rescan recreates watcher and reconciles full source state.
- Activation or effect: Wired continued target maintenance, not observed live freshness.
- Evidence limits: Watchdog/OS delivery and external-store completion unobserved; periodic rescan is a defense, not proof of zero missed changes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles and lack of per-row approval match [RT-RTE-index-update](#rt-rte-index-update). Operating mode is continuous maintenance; source events, not a quality score, trigger proposals. Caller can stop/drop or change the source. This revises indexed content, not the application policy; no answer oracle is present.

> observer = _start_observer()
> try:
>     await subscriber.update_all()
>     await subscriber.mark_ready()
> --- `python/cocoindex/connectors/localfs/_source.py`

#### RT-RTE-preview-update
Label: Preview target actions

Endpoints: CLI/SDK preview option to core target planning and action collector. Core owns the target-action non-application guarantee; caller code still executes. Both Python and Rust SDKs supply the collector. SRC-1: `python/cocoindex/cli.py`, `python/cocoindex/_internal/app.py`, `rust/sdk/cocoindex/src/app.rs`, `rust/core/src/engine/execution.rs`.

- Immediate return: Planned raw action list, printed by CLI; not an applied-index result.
- Later read-back: inapplicable — planned target actions are returned rather than installed for later target consumption by this branch.
- Delegated visibility: Application processors still receive their usual arguments/context and can call providers or other host APIs.
- Selection predicate: Explicit preview flag; CLI rejects live/reset combinations, without establishing an equivalent SDK prohibition.
- Invalidation or expiry: inapplicable — collector is scoped to this operation; this is not a retention-expiry mechanism.
- Activation or effect: Target actions are collected instead of applied; arbitrary direct side effects are outside that guarantee.
- Evidence limits: No observed preview; not a universal read-only execution promise or a claim that every internal cache path is write-free.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision role: code computes proposals; caller receives them and can decline a later real update. Preview is not an automatic approval workflow and supplies no answer oracle. Operating mode is explicit planning. No target rollback is required for the un-applied actions; direct effects require their own recovery.

> *preview_output_capture.lock().unwrap() = output;
> Ok(None::<(PrecommitWritePlan, ())>)
> --- `rust/core/src/engine/execution.rs`

#### RT-RTE-manual-extraction
Label: Typed manual extraction

Endpoints: PDF files to Docling Markdown, Instructor/LiteLLM completion, Pydantic validation and PostgreSQL `ModuleRecord`. Symbolic code fixes progression; model proposes content under a natural-language extraction instruction. The process-file function retains the original filename and derived title/description/counts plus full JSON. SRC-1: `examples/manuals_llm_extraction/main.py`.

- Immediate return: Extraction returns ModuleInfo internally; app completes after declared target reconciliation.
- Later read-back: Memoized extraction/file work can be reused; declared records persist in PostgreSQL. A downstream retrieval consumer for this example is uninspected.
- Delegated visibility: Provider request contains system extraction prompt and converted manual as user content; it does not receive the database pool.
- Selection predicate: Recursive PDF matcher; every selected file goes through the fixed conversion/extraction route unless reused.
- Invalidation or expiry: Memoized functions and change-detected LLM_MODEL context participate in tracked reuse; an unchanged provider alias does not pin model behavior.
- Activation or effect: Schema-valid returned content is declared as indexed records; source support of each assertion and actual writes remain unobserved.
- Evidence limits: Docling, Instructor, LiteLLM and provider internals are outside the frozen implementation; typed validation is not factual validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes structured content; Pydantic validates shape, then application code declares the row. No per-content human approval occurs in this inspected function. Caller can edit prompt/model/source or rerun/drop; provider failure or validation failure can prevent completion. This is open extraction, not candidate competition; the manual is evidence input, not an independently supplied expected-answer oracle. Recovery relies on rerun/reprocess and target reconciliation, not a demonstrated semantic rollback. Guidance asks for supported extraction; stored JSON is derived content, not a retained criticism or revised method. No formulated-theory revision is established by this route.

> "module-level functions (with their arguments). Use only what the text supports."
> --- `examples/manuals_llm_extraction/main.py`

> return ModuleInfo.model_validate(result.model_dump())
> --- `examples/manuals_llm_extraction/main.py`

#### RT-RTE-query-index
Label: Text index query

Endpoints: user query string to embedder, SQL fetch and printed retained text. Query code, not an agent model, owns next-step selection. It uses a fresh embedder instance with the shared model name and an asyncpg pool. SRC-1: `examples/text_embedding/main.py`.

- Immediate return: Printed filename, score and text for selected rows; no generated answer.
- Later read-back: PostgreSQL chunk text/vectors written by indexing reach a separate query invocation.
- Delegated visibility: Embedder gets query text; SQL receives vector/top-k; human-facing output gets filename, score and chunk text, not every indexed row.
- Selection predicate: Ascending `embedding <=> $1` distance and SQL `LIMIT $2`, default top-k five.
- Invalidation or expiry: inapplicable — query does not maintain index freshness; updates and deletes belong to maintenance routes.
- Activation or effect: Delivery to printed search output is wired; downstream agent use or answer influence is unobserved.
- Evidence limits: No query trace, quality evaluation or evidence that retrieved text was used in a later answer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ORDER BY distance ASC
> LIMIT $2
> --- `examples/text_embedding/main.py`

#### RT-RTE-drop-app
Label: Explicit app drop

Endpoints: CLI reset/drop or SDK drop to cancellation, live drain, root delete and per-app state-store clearing. Core owns progression; connector providers execute target retirement. SRC-1: `python/cocoindex/cli.py`, `python/cocoindex/_internal/app.py`, `rust/core/src/engine/app.rs`.

- Immediate return: Awaited drop completion or propagated error.
- Later read-back: Successfully removed app state is unavailable for subsequent reuse; failure/timed-out drains can leave incomplete retirement.
- Delegated visibility: Delete context contains provider registry, host context and raising error handler.
- Selection predicate: Explicit application identity; CLI reset confirms unless forced, while SDK drop is directly callable.
- Invalidation or expiry: Root deletion followed by per-app storage drop; connector ownership determines target retirement semantics.
- Activation or effect: Wired deletion/retirement; user-managed containers are documented as abandoned rather than universally erased.
- Evidence limits: No observed deletion; live drain timeout is ignored by the drain helper, so process-wide quiescence is not unconditional.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: operator/caller proposes removal, CLI may require confirmation, SDK does not inherit it. Core raises delete failures. Recovery after partial external failure is not a verified rollback; ordinary update may retry orphan tombstones. Operating mode is explicit destructive maintenance, not improvement selection; answer oracle is inapplicable. Persisted state is removed, not a new program revision.

> let raise_on_error: crate::engine::component::OnError =
>     Arc::new(|err| Box::pin(async move { Err(err) }));
> --- `rust/core/src/engine/app.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-extraction-prompt
Label: Manual extraction instruction path

Consumer: Instructor/LiteLLM provider completion. Channel: system message containing EXTRACT_PROMPT, beside user-message Markdown. Force: requested interpretation, not an invariant that the model obeys or that text is true. Horizon: current extraction request; returned content can persist as rows/memos but is not shown becoming a future system instruction. SRC-1: `examples/manuals_llm_extraction/main.py`; [RT-RTE-manual-extraction](#rt-rte-manual-extraction).

> messages=[
>     {"role": "system", "content": EXTRACT_PROMPT},
>     {"role": "user", "content": markdown},
> ],
> --- `examples/manuals_llm_extraction/main.py`

## Annotations

none
