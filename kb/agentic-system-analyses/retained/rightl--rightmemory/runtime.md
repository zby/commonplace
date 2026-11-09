---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "RightMemory runtime: model-backed retrieval, isolated semantic writes, native-assistant execution and alternate state-admission paths."
run-id: AAS-2026-11-08-rightmemory-cbec05309c2b-01
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
---

# RightMemory runtime report

## Runtime account

RightMemory supplies context to a coding agent and reconciles submitted evidence into a Git-backed memory root. It does not run the enclosing coding task. The [boundary](boundary.md) includes two distinct execution organizations: an internal runtime that calls models itself, and a model-free assistant service that asks the current host to supply native Retrieve and Update children. This report establishes source-level wiring, not exercised behavior or benefit. SRC-1 supplies implementation and doctrine/design; no observed-run or causal-experiment source is registered.

### Ordinary internal invocation

A shipped `rightmemory retrieve --session <session-id> <need>` goes through `entrypoint.main`, profile/root resolution in `cli.main`, role configuration and `RightMemoryRuntime`. `_session_turn` ultimately calls `run_session_turn`; the MCP backend loads the same role configuration and calls that same session method. The caller chooses a stable conversation identity; role-specific stores separate runtime history. Empty messages and the reserved internal no-session ID are rejected by the public session path. Chat, daemon and no-session calls are additional shipped entry shapes, not separate safety boundaries. SRC-1: `rightmemory/entrypoint.py`, `rightmemory/cli.py`, `rightmemory/mcp.py`, `rightmemory/runtime.py`.

In agent retrieval, the program supplies a daily snapshot for a new conversation, subsequent memory differences, pending submissions, changed-delivery notices and optionally current versions of previously delivered material. The model chooses graph IDs, source selections and recent candidate references. Program code resolves those selections against actual sources, checks the output size, returns source-derived text and records delivery coverage and history for the next call. The model's free-form account is not the terminal result. Standalone Pydantic AI uses a typed selector and output validator; provider CLI execution parses JSON and retries selection failures. Decision and oracle details are in [RT-RTE-agent-retrieval](#rt-rte-agent-retrieval); model fixity is in [RT-CMP-role-model](#rt-cmp-role-model). SRC-1: `rightmemory/runtime.py`, `rightmemory/retrieve_selection.py`.

The host then owns application of the returned material. The automatic and approval-gated orchestrator skills both direct it to reconcile memory with the current conversation, apply relevant guidance and submit evidence of stale or wrong memory. Those are natural-language obligations, not proof that the host follows them. The approval-gated skill requires approval for ordinary evidence submission, with an explicit exception for bad retrieved state; the automatic skill does not impose that approval step. Neither mode makes the user approve Update's final wording. SRC-1: `skills/rightmemory-auto-orchestrator-cli/SKILL.md`, `skills/rightmemory-orchestrator-cli/SKILL.md`; [RT-BAP-host-context](#rt-bap-host-context).

An ordinary update submission is durable evidence first, not an immediate memory edit. The async batch driver reloads configuration for each batch, creates an operation-specific session, and passes both the batch operation ID and retained candidates into the runtime. Update makes semantic keep/merge/skip/edit judgments under package prompts, inspects edit feedback, edits and commits in an isolated worktree. The supervisor checks candidate commits before publication, then local operation effects promote state and attempt publication/pressure bookkeeping. [RT-RTE-isolated-update](#rt-rte-isolated-update) separates model admission from deterministic publication. SRC-1: `rightmemory/cli.py`, `rightmemory/runtime.py`, `rightmemory/isolated_write.py`, `rightmemory/prompts/update.md`.

### Material alternate routes and forcing cases

1. **Invalid or oversized retrieval selection.** A string terminal answer is rejected in standalone mode. CLI JSON/renderer failures trigger bounded retries, then propagate. Both use the renderer rather than forwarding raw prose. Its output-size check rejects rather than silently truncates. This is a result-format/source-resolution guarantee, not a guarantee of relevant selection or complete retrieval. SRC-1: `rightmemory/runtime.py`, `rightmemory/retrieve_selection.py`; [RT-RTE-agent-retrieval](#rt-rte-agent-retrieval).
2. **Embedding retrieval and fallback.** This backend builds a corpus under the memory lock, releases it for model-service work, ranks source entries by embedding similarity and reranker order, then checks the corpus fingerprint under lock before rendering. A changed corpus retries once. Every query may return previously returned entries: agent delivery-history semantics do not carry across. Only `EmbeddingServiceError` triggers configured agent fallback; an oversized rendered result raises `ValueError` and is not caught by that fallback. The no-fallback configuration is explicitly supported. SRC-1: `rightmemory/runtime.py`, `rightmemory/config.py`, `rightmemory/embedding_retrieval.py`; [RT-RTE-embedding-retrieval](#rt-rte-embedding-retrieval).
3. **Isolation condition and alternate executors.** `_should_isolate_write_turn` requires an automatic-write role and equal memory/state roots. The ordinary configuration loaders set those roots equal. A nested runtime deliberately separates them because its memory root is already the supervisor's worktree; it also disables sync. Therefore the direct branch exists and is reached by shipped code, but this is not evidence of an ordinary CLI flag bypassing publication controls. Direct API construction can select different roots; its deployment use is unobserved. Codex write roles receive `full-access`, while Claude write roles receive `auto`; worktree publication checks are not an operating-system sandbox for those executors. SRC-1: `rightmemory/config.py`, `rightmemory/runtime.py`, `rightmemory/agent_cli.py`.
4. **Native assistant completion versus prepared work.** Assistant context preparation leaves live sources accessible and materializes pending evidence and instructions without creating model history. A host child, not the internal runtime, reads and judges those sources. Native Update prepares a persistent worktree; completion imports its commits through the supervisor, retains candidate evidence and either publishes locally or asks the Git queue coordinator to finalize, then records completion. A prepared candidate is not a receipt of publication. This path has its own task/claim identities and recovery behavior; it does not inherit the agent retriever's selector, size limit or delivery ledger. SRC-1: `rightmemory/assistant_context.py`, `rightmemory/assistant.py`, `rightmemory/assistant_write.py`, `skills/rightmemory-assistant/SKILL.md`; [RT-RTE-native-assistant](#rt-rte-native-assistant).

These are inspected source branches, not executed adversarial tests. The external host/provider implementations, actual filesystem permissions and deployments are outside observation. Remote queue-finalizer internals, every shared-view source subtype and all platform failure combinations are not exhaustively audited here. The accounts below identify additional admission surfaces rather than treating the ordinary Update supervisor as universal.

### Scope of load-bearing controls

| Control | Owner and enforcement point | Strength and covered paths | Alternate paths and external contract | Conclusion statuses |
| --- | --- | --- | --- | --- |
| Agent retrieval returns resolved selections, not model prose | Runtime coercion/parser and `RetrieveSelectionRenderer.render` | invariant for successful terminal results through the inspected internal agent retrieval paths | Embedding has a separate renderer; native assistant returns host-authored context. Depends on source/parser implementations and readable current files, not semantic model accuracy. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Automatic write publication checks role-owned committed state | `IsolatedWriteSupervisor._run_claimed`, `_validate_commits`, `_validate_candidate`; runtime root-equality routing | invariant at this publication boundary: rejects uncommitted candidates and forbidden commit paths, checks regular-file modes and applicable validation, fences active semantic changes | Provider-native tools execute before admission and can have broader capabilities; manual maintenance uses a skill protocol, Pursuit editor and sync have distinct gates. Git, locks and filesystem behavior are required external contracts. No universal no-side-effect claim. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Native completion is distinct from preparation | Assistant writer/service and queue finalization before `_finish` receipt | protocol with code checks for the inspected task-completion path | Caller/host must use the supplied root and completion commands; a host claiming success without a receipt is not prevented by natural-language instructions. Prepared publication can be retried. | implementation conclusion status: wired; operation conclusion status: uninspected |

A validation pass establishes structural admissibility, not the truth, relevance or usefulness of a proposed memory change. In particular, the supervisor deliberately disables correction-capacity enforcement for its whole-memory validation, and Insight returns before that graph-validation step. Per-role file and commit-tree checks still apply. SRC-1: `rightmemory/isolated_write.py`.

> if self.role == "insight":
>     return
> validation = MemoryTools(worktree, role=self.role).validate_memory(
>     # A pre-existing sync union must not block an unrelated semantic update.
>     enforce_correction_capacity=False
> )
> --- `rightmemory/isolated_write.py`

### Capability, grant and context boundaries

Standalone execution supplies role-selected Python tools: Retrieve gets four read tools, Historian gets history-aware reads, other applicable roles get file/Git writes, and Sync Reconciler additionally gets discard. This is the program's current tool grant, not the complete capability surface of a provider CLI. CLI adaptation expressly substitutes provider-native file tools; Codex SDK calls receive a role sandbox mapping and Claude subprocesses receive a permission-mode mapping. Provider implementation and enforcement are not frozen here. Model-request limits and tool retries constrain the standalone loop; CLI subprocess/provider termination and reliability remain external contracts. Debug tracing is optional and records starts, failures, outputs and instrumented tool calls; presence of trace code is not supplied execution evidence. SRC-1: `rightmemory/runtime.py`, `rightmemory/agent_cli.py`, `rightmemory/prompt.py`.

> if role in READ_ROLES:
>     return "read-only"
> if role in WRITE_ROLES:
>     return "full-access"
> --- `rightmemory/agent_cli.py`

> if role in READ_ROLES:
>     return "plan"
> if role in WRITE_ROLES:
>     return "auto"
> --- `rightmemory/agent_cli.py`

Working context is controlled differently across routes. Agent retrieval supplies snapshot/diff/pending/delivery context and keeps session history; `--include-returned` adds currently resolved prior material rather than merely reusing old output. Embedding uses independent queries with separate bookkeeping. Internal CLI write turns use one-shot sessions; nested operation state is staged separately from active state. Native Retrieve and Update use host-native child contexts with selected inputs and a returned result: this resembles a separate call frame, but RightMemory does not own the host's window, compaction or enforcement of that separation. Files remain accessible by tool reads, not pointers automatically followed by a model window. No claim of general trimming or token-budget management follows from this wiring. SRC-1: `rightmemory/runtime.py`, `rightmemory/assistant_context.py`, `skills/rightmemory-assistant/SKILL.md`.

### Change admission beyond ordinary Update

Pruner uses a deterministic generation-due check before invoking semantic judgment; Insight watch claims pressure-triggered operations and produces logs or no-ops; Historian returns historical context without write tools. Explicit maintenance instructions instead authorize host edits through temporary worktrees and validation/fast-forward procedures. The human Pursuit editor journals allowed operations, validates candidates and later checkpoints them. Sync admits validated incoming state through a separate candidate/repair pipeline; shared-file imports validate and promote downloaded packages, retaining a stale valid import when refresh fails. These mechanisms can change what later retrieval consumes without being an Update proposal. Their records below keep admission authority separate. SRC-1: `rightmemory/runtime.py`, `rightmemory/prune.py`, `rightmemory/cli.py`, `skills/maintain-rightmemory/SKILL.md`, `rightmemory/pursuit_store.py`, `rightmemory/sync.py`, `rightmemory/shared_view_files.py`.

Package-owned prompts/references and role configuration determine the shipped runtime's policy and executor choice. The inspected operational routes write memory, correction collections, logs, editor state or shared state; this report does not establish an operational route that revises RightMemory's own package implementation or model weights. That is a bounded observation about these routes, not a repository-wide evidenced absence. Memory content revision and any theory-builder/self-improvement attribution remain separate analytical questions, not inferred from publication or persistence.

Added inspection within SRC-1 includes `rightmemory/retrieve_selection.py`, `rightmemory/embedding_models.py`, `rightmemory/embedding_service.py`, `rightmemory/pursuit_store.py`, role-specific prompt passages, MCP backend methods and the alternate executor/control branches cited above. All are implementation or doctrine/design at the boundary's same frozen commit, not new registered sources.

## Shared records

### Components

#### RT-CMP-role-model
Label: Role inference model

The runtime's configured generative model supplies tool-use and terminal-selection/edit judgments. Representational form: distributed-parametric weights in an external provider/service; prompt/history text is a separate input, not model weights. Storage substrate: provider-owned model deployment, with local configuration selecting model ID, endpoint or CLI provider/model. Standalone routes construct Anthropic or OpenAI-compatible models; CLI routes call Codex SDK or Claude. SRC-1: `rightmemory/runtime.py`, `rightmemory/agent_cli.py`, `rightmemory/config.py`.

Parameters are not changed by the inspected RightMemory invocation code. Provider-side parameter changes remain uninspected. An exact immutable model version is not pinned by this source: model IDs and endpoint/model configuration are caller/deployment supplied, and CLI model selection may be omitted. A mutable endpoint or provider alias can resolve differently; no weight-identity check is shown in these constructors. This prevents reproducibility or fixed-model guarantees across deployments, not source-level analysis of the caller.

> if config.api_base is not None:
>     provider_kwargs["base_url"] = config.api_base
> --- `rightmemory/runtime.py:2178-2200`

#### RT-CMP-embedding-model
Label: Embedding model adapters

Source-native adapters `Nemotron3Embedding` and `JinaV5NanoEmbedding` convert query/passage text into normalized dense vectors. Representational form: distributed-parametric weights and numerical embeddings. Substrate: local downloaded model snapshot on the service host, tensors during inference, derived vectors cached as JSON by the client. The shipped adapters load local safetensors, use evaluation/inference mode and compute an identity from snapshot files, adapter revision/settings and library versions. No training/update step is present in the inspected encode methods; arbitrary remote-service internals remain uninspected. SRC-1: `rightmemory/embedding_models.py`, `rightmemory/embedding_retrieval.py`.

Exact deployed snapshot is not supplied or pinned by this analysis. The shipped service reports content-derived identity; a mutable service can change models between queries. Client requests require matching identity within a query and cache entries are keyed by model/root/text. This checks metadata consistency, not independent authenticity of remote weights.

> payload = {"weights": model_fingerprint(path), "adapter": name, "revision": revision, "settings": settings}
> --- `rightmemory/embedding_models.py`

#### RT-CMP-reranker-model
Label: Jina35Reranker

The `Jina35Reranker` adapter ranks candidate passages under a query. Form: distributed-parametric weights; substrate: local service-host snapshot/tensors, transient ranking indices returned as JSON. It loads a local safetensors snapshot with custom code enabled and uses inference mode. Parameters do not change in the inspected rerank method. Exact deployed version is not supplied; identity is snapshot/adapter-derived, while a mutable endpoint may resolve to another model between queries. Request identity checks reject an in-query mismatch under the shipped service contract. Custom model internals and actual weights are outside the frozen repository. SRC-1: `rightmemory/embedding_models.py`, `rightmemory/embedding_service.py`, `rightmemory/embedding_retrieval.py`.

> with self.torch.inference_mode():
>     results = self.model.rerank(query, documents)
> --- `rightmemory/embedding_models.py`

### Operative objects

#### RT-OBJ-role-instructions
Label: Package role instructions

Natural-language instructions assembled from package schema, role references and `prompts/<role>.md`, stored as package files and delivered as model instructions or CLI prompt text. Consumer interpretation supplies semantic judgment; tool grants and publication validators are separate symbolic controls. Native assistant preparation materializes corresponding instructions in task files. SRC-1: `rightmemory/prompt.py`, `rightmemory/assistant.py`, `rightmemory/assistant_context.py`.

> Follow the canonical role instructions below. Use the embedded package references as the schema and rule source of truth.
> --- `rightmemory/prompt.py`

#### RT-OBJ-runtime-config
Label: RuntimeConfig

Symbolic dataclass/configuration loaded from role-specific TOML and root resolution. Stored locally; fixed consumer rules choose retrieval backend, executor/model settings, roots and synchronization. Ordinary loaders bind `state_root` to the active root; nested isolated runtimes replace it with staged state and disable sync. This object controls dispatch, not semantic admission of each candidate. SRC-1: `rightmemory/config.py`, `rightmemory/runtime.py`.

> return self.config.role in AUTOMATIC_WRITE_ROLES and self.config.memory_root == self.config.state_root
> --- `rightmemory/runtime.py`

#### RT-OBJ-semantic-operation
Label: Semantic operation record

Symbolic operation identity, phases, candidate/start/landed commit metadata and pending effect states persisted through `SemanticOperationStore` under the memory root. The runtime and supervisor use it for replay, prepared publication and post-commit effects. Output text in the record is descriptive, not a separate approval. Operation input may also contain natural-language candidate evidence; its semantic consumers belong to Update, not phase dispatch. SRC-1: `rightmemory/runtime.py`, `rightmemory/isolated_write.py`.

> if record.phase not in FINAL_PHASES:
>     return
> effects = store.list_pending_effects(operation_id)
> --- `rightmemory/runtime.py`

### Routes

#### RT-RTE-agent-retrieval
Label: Internal agent retrieval

Owner/progression: caller supplies need/session; runtime loads context; inference model chooses IDs/source ranges/recent candidates using role read tools; renderer resolves selections and emits source text; runtime records success. Decision policy is package Retrieve guidance interpreted by the model plus strict symbolic selection validation. Operating mode: open requests, not a bounded curriculum. No answer oracle is supplied to determine relevance; validation is a structural/source oracle only. Standalone and CLI have different output interfaces but converge on the renderer. SRC-1: `rightmemory/runtime.py`, `rightmemory/retrieve_selection.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered source selections, or the renderer's no-strong-match message; invalid terminal output raises after applicable retries.
- Later read-back: Snapshot/diff/pending context, saved model/provider session state and delivery coverage shape later retrieval calls.
- Delegated visibility: The caller receives rendered text; standalone tools are role-selected, while CLI agents inspect equivalent files through provider-native tools.
- Selection predicate: Model judgment over current query and supplied context, constrained to resolvable selector fields; not all available material is necessarily returned.
- Invalidation or expiry: Changes since delivered commits and changed-material notices refresh context; new CLI conversations reset retrieval context; include-returned re-resolves prior delivery.
- Activation or effect: Delivery and bookkeeping are wired; downstream host use or changed decisions are unobserved.
- Evidence limits: No model trace establishes relevance, completeness or host compliance; native assistant retrieval is a different route.

> standalone retrieve must finish through the native terminal selector, not text
> --- `rightmemory/runtime.py`

> if len(output) > self.max_output_chars:
>     raise RetrieveSelectionError(
>         f"resolved retrieve output is {len(output)} characters; "
>         f"select less content to stay within {self.max_output_chars}"
>     )
> --- `rightmemory/retrieve_selection.py`

#### RT-RTE-embedding-retrieval
Label: Independent embedding retrieval

Owner/progression: runtime dispatches to `EmbeddingRetriever`; source corpus → best passage similarity per entry → candidate-count cutoff → service reranker → result-count cutoff → source-order rendering. Code decides counts, not the model. Operating mode: independent open queries. The query is not an answer oracle, and ranking is not a correctness check. Components are [RT-CMP-embedding-model](#rt-cmp-embedding-model) and [RT-CMP-reranker-model](#rt-cmp-reranker-model). SRC-1: `rightmemory/embedding_retrieval.py`, `rightmemory/runtime.py`, `rightmemory/config.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected original entry text or an empty-corpus message; oversize output errors without truncation.
- Later read-back: Derived vector cache can be reused; per-query bookkeeping records source fingerprint/versions, not an exclusion of prior results.
- Delegated visibility: Service receives query and search passages; caller receives rendered source text, not raw embedding vectors.
- Selection predicate: Highest passage dot-product per source entry, then candidate-count limit and reranker result-count selection.
- Invalidation or expiry: Text/model/root identify cached vectors; changed source fingerprint retries the corpus once; model identity mismatches cause service errors.
- Activation or effect: Retrieval delivery is wired; applied host guidance and retrieval-quality benefit are unobserved.
- Evidence limits: Service-error fallback uses a configured agent; generic rendering ValueError is not that fallback. Remote service internals and deployment identity are not supplied.

> except EmbeddingServiceError:
>     if self.config.agent_cli is None and self.config.model_id is None:
>         raise
> --- `rightmemory/runtime.py`

> # Every query already allows previously returned content, including --include-returned calls.
> return result.text
> --- `rightmemory/runtime.py`

#### RT-RTE-isolated-update
Label: Isolated semantic Update admission

Trigger/owner: synchronous Update or queued evidence batch. The role model proposes concrete edits and may reject all candidates; code can veto publication for dirty/uncommitted work, forbidden paths, invalid candidate structure or a changed semantic base. Ordinary callers supply evidence, not final wording. Package Update/module instructions guide semantic admission, with `corrections.md` as a late edit-feedback check. Resulting memory and retained batch evidence persist; detailed memory revision semantics are left to the memory analyst. Operating mode: open evidence reconciliation, not an experiment. No expected-answer oracle establishes factual correctness. SRC-1: `rightmemory/cli.py`, `rightmemory/runtime.py`, `rightmemory/isolated_write.py`, `rightmemory/prompts/update.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Model's summary from the admitted operation; last-write result and operation outcome distinguish prepared, committed and no-change cases.
- Later read-back: Landed Memory/Agent Corrections reach later retrieval; retained candidates/operation outcomes support later accounting and recovery.
- Delegated visibility: Nested executor receives worktree and staged state; active root publication remains supervisor-owned. CLI executor capabilities can exceed allowed commit paths.
- Selection predicate: Model keep/merge/skip/edit judgment; supervisor applies role/path/regular-file and applicable candidate validation, checking intermediate commits before collapse.
- Invalidation or expiry: Active semantic-base changes reject stale candidates; operational-only changes can be rebased and revalidated. Prepared/final operation identities support retry rather than unconditional reexecution.
- Activation or effect: Candidate commits can reach the active root, followed by state/publication/pressure effects; no observed downstream decision or improvement is supplied.
- Evidence limits: Semantic judgment is requested, not independently verified; publication checks do not prevent arbitrary external effects of full-access executors.

Recovery: exceptions are recorded; running failures archive failed provider-session state; prepared operations can resume publication; post-terminal effects are separately marked and retried. There is no demonstrated universal automatic rollback of already published state or external effects. Human veto is not per-content approval in automatic mode; approval-gated orchestration authorizes evidence submission, not the final stored edit.

> Candidates are evidence, not stored wording or destination instructions. Most candidate content should be filtered out. Pursuit is read-only context, not an Update destination.
> --- `rightmemory/prompts/update.md`

> # Squashing must not conceal a forbidden intermediate write.
> for commit in commits:
>     self._validate_commits(worktree, [commit])
> --- `rightmemory/isolated_write.py`

#### RT-RTE-native-assistant
Label: Native assistant Retrieve and Update protocol

The main host agent owns submissions/delegation, native children own semantic reading/editing, and the model-free assistant service owns preparation, claims and receipts. Retrieve returns host-selected context from live files; Update receives a persistent task worktree and canonical instructions. Submission identity is stable `(session_id, request_id)` plus evidence equality; task/batch/operation identities govern publication. The service does not itself decide relevance or stored wording. Operating mode: open host requests and ready batches; no answer oracle is supplied. SRC-1: `rightmemory/assistant.py`, `rightmemory/assistant_context.py`, `rightmemory/assistant_write.py`, `skills/rightmemory-assistant/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Context preparation returns source/instruction/pending paths; submission returns saved/duplicate state; completion returns a landed-commit receipt, not just a prepared candidate.
- Later read-back: Live active files supply later retrieval; task records and stable submissions support recovery across command invocations.
- Delegated visibility: Native Retrieve child reads supplied directories and returns useful context/sources; native Update child sees task instructions, candidates and isolated worktree. Host owns context isolation.
- Selection predicate: Host semantic judgment selects returned content and edits; completion validates/imports commits through the supervisor and checks task currency.
- Invalidation or expiry: Changed semantic base rejects stale native edits; explicit retry replaces/fences stale work; prepared work retries completion without repeating semantic work.
- Activation or effect: Program publication and receipt are wired; native model behavior, use of retrieved material and adherence to single-delegation instructions are unobserved.
- Evidence limits: No internal agent selector/history guarantee applies to native retrieval; commands and skill cannot establish host runtime permissions or actual compliance.

Admission/rejection/recovery: the host child may keep/merge/skip evidence under Update rules; service/writer veto stale, dirty or invalid commits. Local completion publishes through the writer; Git-backed completion uses coordinator finalization and then external completion. Rejected edits can be corrected in the same worktree; successful publication can report deferred cleanup warnings. No routine human approval of each edit is required by this skill.

> # The no-change path must also pass complete graph validation.
> self.supervisor._validate_candidate(worktree, [])
> --- `rightmemory/assistant_write.py`

> A saved candidate is pending evidence, not confirmation that it became memory.
> --- `skills/rightmemory-assistant/SKILL.md`

#### RT-RTE-maintenance-cycles
Label: Pruner and Insight cycles

Distinct role executions share the automatic-write publication machinery, not semantic objectives. Pruner code checks generation due state before model execution, then supplies boundary/history/grace context. Insight watch claims trigger points and invokes a cycle; the prompt asks for meaningful reflections in new logs or a no-op, not direct Memory edits. Historian is an associated read-only recovery consumer of history, not another writer. SRC-1: `rightmemory/prune.py`, `rightmemory/runtime.py`, `rightmemory/cli.py`, `rightmemory/prompts/pruner.md`, `rightmemory/prompts/insight.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Not-due message, prune removal/checkpoint summary, or Insight log/no-op summary.
- Later read-back: Prune ledgers/grace affect later prune judgment; remaining memory reaches retrieval; prior Insight logs are sources for later Insight cycles.
- Delegated visibility: Role model receives memory and relevant role-specific history; Insight write grant/publication paths are limited to insight_logs.
- Selection predicate: Deterministic due/pressure triggers, followed by model judgment under role prompts; no independent expected-answer oracle for usefulness or pruning truth.
- Invalidation or expiry: Prune generations and grace checkpoints govern reconsideration; shared isolated-operation fencing/recovery governs publication, not semantic correctness.
- Activation or effect: Active memory may shrink or logs may accumulate; changed future task performance is unobserved.
- Evidence limits: Pruner and Insight do not have identical validation coverage: Insight skips whole-graph candidate validation, retaining path/tree checks. Log production alone establishes neither successful reflection nor memory promotion.

Admission: models propose deletions/checkpoints or logs and can no-op; code vetoes invalid publication. Prior ledgers/logs and package instructions shape proposals. Recovery follows operation records; no per-cycle human content approval is shown in these internal routes. These objectives are distinct from revising runtime code or model parameters.

> Keep writes scoped to `insight_logs/*.md`; leave active Memory edits to
> Update and explicitly requested `maintain-rightmemory` work.
> --- `rightmemory/prompts/insight.md`

#### RT-RTE-manual-maintenance
Label: Explicit host maintenance

An explicit user maintenance request authorizes host-native inspection/editing under `maintain-rightmemory`; it forbids invoking Update or another RightMemory model role. This is a source-authored procedure, not a program-enforced equivalent of the Update supervisor. The skill supplies schema/module rules and preserves Pursuit references; proposal and final edit judgment remain with the host under the authorized request. Operating mode: explicit maintenance, with no independent answer oracle. SRC-1: `skills/maintain-rightmemory/SKILL.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Requested changes, validation and landed/push results, or no commit.
- Later read-back: Edited memory/corrections/supporting references can reach later consumers; immutable update records must not be edited.
- Delegated visibility: Host receives real files/history; no separate internal model role is to be launched by this workflow.
- Selection predicate: Explicit requested scope plus host judgment informed by package rules, current state and history.
- Invalidation or expiry: Clean-root and captured branch/HEAD fences before landing; validation immediately before commit and after fast-forward; otherwise stop/report changed state.
- Activation or effect: Protocol affords publication of validated edits; compliance and downstream use are unobserved.
- Evidence limits: Validation and Git commands are instructions to the host, not mandatory runtime admission of every filesystem edit.

Admission/recovery: human request supplies authority for the requested changes without a routine preview ceremony. Host can stop for missing target/unsafe ambiguity. Temporary worktree and exact fast-forward preserve the inspected base; the skill forbids absorbing unrelated changes. This is not evidence of automatic rollback after a host violates the procedure.

> Never call `rightmemory update`, submit candidates, or invoke another RightMemory model role.
> --- `skills/maintain-rightmemory/SKILL.md`

#### RT-RTE-pursuit-editor
Label: Human Pursuit editor admission

Web service passes an operation, expected revision and session ID to `PursuitStore.apply`. Code applies allowed symbolic map actions to candidates, validates changes, journals before/after files and history, and later flushes a checkpoint through its Pursuit supervisor. The human-facing browser path supplies the proposed change; symbolic code decides admissibility. No inference model or answer oracle is required for the inspected editor route. SRC-1: `rightmemory/web/service.py`, `rightmemory/pursuit_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pending snapshot/action result; flush returns checkpoint outcome. Opening-context generation flushes pending edits and checks revisions around context construction.
- Later read-back: Canonical Pursuit files become context for retrieval and copied opening context; journal state supports pending-edit continuation.
- Delegated visibility: Browser receives snapshots/results; opening-context text is returned for host use rather than automatically executing a coding agent.
- Selection predicate: Allowed operation types, revision/session ownership, declared changed paths, role paths, graph validation and restricted mechanical Memory-reference repair.
- Invalidation or expiry: Revision conflicts and dirty-root/base fences reject unsafe edits; undo/redo use editor history and checkpoint logic rather than unconstrained raw file replacement.
- Activation or effect: Validated checkpoints can change canonical map state; actual host adoption of copied context is unobserved.
- Evidence limits: Browser authorship does not prove every API caller is human; no semantic truth oracle for user direction or deployment authorization audit is supplied.

Admission/rejection/recovery: code rejects out-of-role paths and non-mechanical Memory changes; the operator chooses content. Journaling retains before/after material and cursor for undo/redo; publication checks the exact validated commit. This gate is distinct from Update's prohibition on Pursuit writes.

> if not self._reader._is_pursuit_edge_removal(old, new, memory_paths):
>     raise PursuitStoreError("write_failed", "Pursuit edits may change Memory only to repair deleted references.", 500)
> --- `rightmemory/pursuit_store.py`

#### RT-RTE-sync-admission
Label: Incoming synchronized state admission

`SyncManager` fetches configured upstream state, stages a candidate, checks incoming paths and validates the merged result before publishing. Structural conflicts/repair needs can require configured or native reconciliation. Upstream actors propose state; software gates publication; repair models/hosts can propose semantic repairs, without a per-content human approval requirement in the inspected pipeline. Operating mode: configured synchronization/repair, not an improvement experiment. Structural validation is not an answer oracle for remote content. SRC-1: `rightmemory/sync.py`, `rightmemory/runtime.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synced/error/repair state, with retrieval refresh able to leave repair pending rather than execute a model repair itself.
- Later read-back: Published incoming graph, guidance, queue and record state can reach later consumers according to their own routes.
- Delegated visibility: Repair candidate and recorded context go to the applicable reconciler; remote implementations and actual actors are external.
- Selection predicate: Configured upstream; synchronized-path allowlist, regular-file checks, guidance/queue/record checks and graph validation.
- Invalidation or expiry: Active start-commit and candidate-tip fences precede fast-forward publication; prepared repair records permit recovery.
- Activation or effect: Source permits admission of structurally validated upstream state; semantic correctness and downstream behavioral use are unobserved.
- Evidence limits: This is a separate admission surface, not evidence that every admitted remote value passed local Update semantic judgment. Detailed transport and all repair combinations are not exhaustively audited.

Rejected candidates are not ordinary active-root edits. Repair guidance and operation metadata govern correction/retry; publication rechecks the active base. No universal rollback of remote side effects is established.

> if inspection.repair is None:
>     candidate_commit = self._required_head(candidate.path)
>     self._publish_candidate(candidate_commit, start_commit, candidate)
>     return SyncResult("synced", "validated incoming memory published")
> --- `rightmemory/sync.py`

#### RT-RTE-file-import
Label: Shared file-view import

A configured file-view connection is refreshed before retrieval or explicitly by a caller. HTTP packages are extracted into a temporary candidate, validated with expected view identity/namespace and promoted. A Git-file target dispatches to a separate transport; its full implementation is not audited in this record. Provider-authored content, not local Update, supplies the incoming package; code decides package validity. Operating mode: configured refresh, with no semantic answer oracle or per-refresh human approval shown. SRC-1: `rightmemory/shared_view_files.py`, `rightmemory/runtime.py`, `rightmemory/assistant_context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pulled/stale/unavailable status; later retrieval can render valid imported source material.
- Later read-back: Import directories under .runtime/shared_views/imports persist for subsequent retrieval.
- Delegated visibility: Local readers/host children can inspect approved-format package content; transport receives the configured target identity/credentials.
- Selection predicate: Connection and view type select refresh target; HTTP package validation checks expected view ID and namespace before promotion; retrieval selection remains separate.
- Invalidation or expiry: Successful refresh replaces the import; failed refresh retains a valid existing import and marks stale rather than proving freshness.
- Activation or effect: External context becomes available to later source selection; delivery and host use are separate, unobserved effects.
- Evidence limits: Structural package validity does not establish content truth. Git-file dispatch and stale fallback are inspected, but no claim is made here that all transport branches share the HTTP extractor's checks.

Admission/recovery: provider proposes package content; validator can reject it. HTTP failure removes the temporary candidate; prior valid import can continue serving. Detailed publishing approval, generative view construction and question-view semantics remain available to specialist inspection rather than being inferred from this import route.

> validate_file_view_package(
>     temp,
>     expected_view_id=expected_view_id,
>     namespace_id=heading_id,
> )
> promote_directory_candidate(temp, final)
> --- `rightmemory/shared_view_files.py`

### Claims

#### RT-CLM-native-publication
Label: Completion receipt marks publication

The native-assistant skill claims completion only after program publication; preparation is not enough. Implementation in [RT-RTE-native-assistant](#rt-rte-native-assistant) supports this distinction at the inspected service boundary, not truthful reporting by every host. SRC-1: `skills/rightmemory-assistant/SKILL.md`.

> Only the program's completion receipt confirms that candidate work reached the active root. A prepared candidate is not a completed update.
> --- `skills/rightmemory-assistant/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-role-policy
Label: Package policy to role judgment

Consumer: internal role inference model or native assistant child. Channel: assembled instructions and role/schema/reference text. Force: natural-language behavioral guidance; horizon: each role invocation, with provider continuation where configured. Separate symbolic grants and publication gates constrain permitted results but do not guarantee compliance with semantic policy. SRC-1: `rightmemory/prompt.py`, `rightmemory/runtime.py`, `rightmemory/assistant.py`; [RT-OBJ-role-instructions](#rt-obj-role-instructions), [RT-RTE-isolated-update](#rt-rte-isolated-update).

> Stay within the command-selected {role} role and its instructions for this memory store.
> --- `rightmemory/prompt.py`

#### RT-BAP-host-context
Label: Retrieved guidance to host work

Consumer: enclosing coding agent. Channel: retrieval return or native child's context handoff plus the shipped orchestration skill. Force: requested guidance subordinated to current user instructions/evidence, not a symbolic command dispatcher. Horizon: current task and later sessions when retained content is retrieved again. The source establishes supply and requested use, not activation or causal benefit. SRC-1: `skills/rightmemory-auto-orchestrator-cli/SKILL.md`, `skills/rightmemory-assistant/SKILL.md`; [RT-RTE-agent-retrieval](#rt-rte-agent-retrieval), [RT-RTE-native-assistant](#rt-rte-native-assistant).

> Apply relevant guidance in the work itself; do not merely quote or acknowledge it.
> --- `skills/rightmemory-auto-orchestrator-cli/SKILL.md`

## Annotations

none
