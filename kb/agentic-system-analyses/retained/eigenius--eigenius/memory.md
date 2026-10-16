---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Eigenius memory: document decision replay, retained knowledge and executable resources, query selection, and maintenance limits."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
source-identity: "https://github.com/eigenius/eigenius"
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
---

# Eigenius memory report

## Boundary and evidence

This member covers the platform's retained document decisions, generated artifacts, layer-resident knowledge/programs, retrieval, notebook publication and maintenance seams. It inherits the complete-artifact, partial-loop boundary from [boundary](boundary.md), not a claim of exhaustive operational inspection. The source is SRC-1 at the frozen revision above. All new findings below are implementation findings; source comments supply attributed design intent. No target execution, provider call, test or demo was run. No observed activation or improvement is established.

Direct reads extended the supplied runtime in `kernel/src/dcg/draw.rs`, `kernel/src/dcg/pipeline.rs`, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/dcg/proposer_record.rs`, `crates/eigenius-encoding/src/formalize.rs`, `crates/eigenius-encoding/src/claim_kind.rs`, `kernel/src/server/query.rs`, `kernel/src/server/hooks.rs`, `kernel/src/server/gc.rs`, `kernel/src/query/evaluate/similarity.rs`, `kernel/src/query/vector/search.rs`, `kernel/src/layer/consolidate.rs`, `clients/eigenius-ts/src/notebook.ts`, `clients/eigenius-ts/src/client.ts`, `notebooks/src/runtime/publishedNotebooks.ts` and `crates/eigenius-encoding/tests/served_formalization.rs`. Searches additionally checked CLI dispatch, MCP registration and task/vector-indexing locations. These are added scopes within the registered source, not new sources.

| Entry point / operation | Source path, SRC-1 | Coverage and conclusion limit |
|---|---|---|
| Served formalization, branch/inline/live decisions | `crates/eigenius-encoding/src/formalize.rs`, `kernel/src/dcg/pipeline.rs`, `kernel/src/dcg/draw.rs` | Direct reads; [MEM-OBJ-proposal-draw](#mem-obj-proposal-draw), [MEM-RTE-draw-retention](#mem-rte-draw-retention); supplements [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize). |
| Reading selection and context budget | `kernel/src/dcg/reading_ranker.rs` | Direct record/replay and context-builder reads; [MEM-OBJ-selection-record](#mem-obj-selection-record); supplied [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection) supplies membership checks. |
| Other decision seams | `kernel/src/dcg/sense_ranker.rs`, `kernel/src/dcg/proposer_record.rs`, `crates/eigenius-encoding/src/claim_kind.rs` | Sense source search; direct proposal/key and kind-record reads. Separate parts below retain key and provenance differences; full sense provider transformation remains uninspected. |
| Load, tombstones, program output and institution rejection | `kernel/src/server/load.rs`, `kernel/src/commit/phases.rs`, `kernel/src/server/programs.rs` | Supplied runtime evidence in [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), not independent full rereads. [MEM-OBJ-layer-resources](#mem-obj-layer-resources) records broader storage contents. |
| Query and FIBER INTO | `kernel/src/server/query.rs`, `kernel/src/query/evaluate/similarity.rs`, `kernel/src/query/vector/search.rs` | Direct reads; [MEM-RTE-query-resources](#mem-rte-query-resources) includes a write path omitted from runtime's selected routes. |
| Registered agent tools | `orchestration/src/mcp/server.ts` | Registration search checks query, inspect, load, program execution, formalization/result and task tools against supplied runtime. Administrative GC/consolidation are not inferred to be MCP tools. Full SDK method inventory remains uninspected. |
| Post-commit refresh and vector derivation | `kernel/src/server/hooks.rs`, `kernel/src/task/sweep.rs`, `kernel/src/query/vector/indexing.rs` | Direct hook read plus driver/indexing search; [MEM-OBJ-vector-segment](#mem-obj-vector-segment), [MEM-RTE-index-refresh](#mem-rte-index-refresh). Full embedder transport, text-index construction and retry internals remain uninspected; no completeness guarantee. |
| Consolidation and GC | `kernel/src/layer/consolidate.rs`, `kernel/src/server/consolidate.rs`, `kernel/src/server/gc.rs` | Direct consolidation merge-body and GC-handler reads plus entry-point search; [MEM-RTE-state-maintenance](#mem-rte-state-maintenance). Full backend deletion/crash consistency remains uninspected. |
| CLI forcing surfaces | `cli/src/main.rs` | Dispatch search located Query, task Sweep/Reindex and database Consolidate; full local/offline variants not traced. It would be misleading to attribute the server handler's full semantics to every CLI variant. |
| Notebook publish and reopen | `clients/eigenius-ts/src/client.ts`, `clients/eigenius-ts/src/notebook.ts`, `notebooks/src/runtime/publishedNotebooks.ts` | Direct reads; [MEM-OBJ-notebook-cells](#mem-obj-notebook-cells), [MEM-RTE-notebook-reopen](#mem-rte-notebook-reopen). Local-file/autosave and merge-resolution persistence only located by search; their recovery semantics remain unresolved. |
| Evaluator | `crates/eigenius-encoding/tests/served_formalization.rs` | Direct full test read; compares inline replay artifact with CLI fixture, not three successive branch-replay invocations. No passing outcome supplied. |
| Included but unresolved surfaces | `ontologies/`, `scripts/`, `crates/`, `storage/rocksdb/`, `storage/tikv/`, `kernel/src/task/`, `kernel/src/server/reflect.rs` | Bootstrap/importers, broader institution evaluators, reflection APIs, durable task resume, backend consistency and every demo remain available but uninspected. Initial authorship/trust of imported resources, complete lifecycle coverage and a general critique/learning loop cannot be concluded. |

External provider weights and services are outside the frozen artifact; repository adapters remain inside it. The provider components' mutability/version limits are supplied by [RT-CMP-proposer-model](runtime.md#rt-cmp-proposer-model), [RT-CMP-reading-model](runtime.md#rt-cmp-reading-model) and [RT-CMP-completion-model](runtime.md#rt-cmp-completion-model). No additional provider state was acquired.

## Core ideas

1. **A recorded decision is executable replay input, not only an audit log.** Four seam-specific JSON records become typed ProposalDraw resources on a document branch. Later formalization deserializes them into decision implementations. Their symbolic fields choose or refuse decisions; natural-language rationales remain inspectable but do not become general instructions. [MEM-RTE-draw-retention](#mem-rte-draw-retention).
2. **The branch's lifetime is weaker than the phrase “persistent replay” suggests.** The next run reads the old draws before recreating its glossary branch. Replayed arms are not recorded again. Consequently a successful all-replay run can leave its new branch without the old draws: a third default-branch run is not guaranteed to find the first run's decisions. This is a source-grounded integration issue, not an observed failure. [MEM-RTE-draw-retention](#mem-rte-draw-retention).
3. **Persistence does not confer one uniform authority.** A result blob is fetchable data; load separately admits its resources. Retained program bodies are executable symbolic content. Institution declarations affect later dispatch and admission. Notebook cells are reopened editable source. Vector segments rank candidates rather than certify claims. [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact), [RT-BAP-retained-program](runtime.md#rt-bap-retained-program), [MEM-BAP-institution-refresh](#mem-bap-institution-refresh).
4. **Read-back is requested and selected, not an unsolicited memory push into an enclosing agent.** Formalization requests select document recordings; EigenQL selects resources or similarity candidates; notebook reopen follows cell IRIs. Post-Load indexing is an automatic write/refresh, not automatic model-context delivery. [MEM-RTE-query-resources](#mem-rte-query-resources), [MEM-RTE-index-refresh](#mem-rte-index-refresh).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-proposal-draw
Label: ProposalDraw resource

SRC-1, `kernel/src/dcg/draw.rs`: a symbolic resource envelope on a persistent layer chain, containing seam, question key, JSON record, optional model name and timestamp. A JSON string here is serialized structured data, not a natural-language prompt merely because it uses a string field. The record's rationale/gloss parts have separate interpretive uses below. Draw IRIs hash seam and key under the supplied namespace; their identity does not hash the answer. Model/timestamp fields are provenance, not the replay lookup predicate. Closest supplied record is [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), a route, not this stored object; no supplied object counterpart.

> r.set(
>             iri(&format!("{ENC}:draw_record"))?,
>             Value::String(
>                 serde_json::to_string(&d.record)
>                     .map_err(|e| format!("serialize draw record: {e}"))?,
>             ),
>         );
> --- `kernel/src/dcg/draw.rs`

#### MEM-OBJ-selection-record
Label: SelectionRecord

Part of: [MEM-OBJ-proposal-draw](#mem-obj-proposal-draw)

SRC-1, `kernel/src/dcg/reading_ranker.rs`: selection payload stores sentence, document SHA, prior selection glosses, candidate skeleton/gloss/semantic strings, abstention, chosen index, rationale, runners-up and model. The document SHA is access/identity metadata, not recoverable full document text. Choice and abstention are symbolic decision data; glosses and rationale are natural language. The rationale is retained stated justification, not authenticated hidden model reasoning. Replay returns it alongside the choice, but computes the key without rationale or model. The candidate object is a material payload part, distinct from the supplied selection route [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection).

> Some(ReadingSelection {
>                     chosen: r.chosen,
>                     rationale: r.rationale.clone(),
>                     runners_up: r.runners_up.clone(),
>                 })
> --- `kernel/src/dcg/reading_ranker.rs`

#### MEM-OBJ-rank-record
Label: RankRecord

Part of: [MEM-OBJ-proposal-draw](#mem-obj-proposal-draw)

SRC-1, `kernel/src/dcg/sense_ranker.rs`, `crates/eigenius-encoding/src/formalize.rs`: sense-ranking records supply the replay ranker with question-dependent order/ranking data. These are symbolic parser inputs stored through the same JSON/resource substrate, not learned parameters. Source search establishes sentence, context and word sense pools enter key construction, and replay misses return no answer for caller fallback. The full rationale/probability transformation has not been independently read; it prevents treating all four payloads as equally explained or equally fail-closed. This part has no separate supplied object counterpart; it belongs to the formalization route, not to provider weights.

> None // a miss is a NON-ANSWER; the caller falls back, nothing is recorded
> --- `kernel/src/dcg/sense_ranker.rs`

#### MEM-OBJ-proposal-record
Label: ProposalRecord

Part of: [MEM-OBJ-proposal-draw](#mem-obj-proposal-draw)

SRC-1, `kernel/src/dcg/proposer_record.rs`: retained symbolic question/answer includes sentence, document hash, prior glosses, hole variable/type/kind, candidate keys/surfaces and Proposal. Natural-language surfaces contextualize the decision; the returned Proposal controls resolver proposals. A replay miss returns the default empty proposal. Empty ranked proposals are retained refusals, not missing logs. The exact full Proposal structure and downstream rationale use are left to the supplied resolver account; no claim of rationale-driven criticism is made. No supplied object counterpart.

> /// A recorded proposal: the exact question put to the proposer, and the answer it gave. An
> /// EMPTY `proposal.ranked` is a recorded refusal ("no presented candidate is the referent") —
> /// stored like any answer, so a draw containing refusals still replays with 0 misses.
> --- `kernel/src/dcg/proposer_record.rs`

#### MEM-OBJ-kind-record
Label: KindRecord

Part of: [MEM-OBJ-proposal-draw](#mem-obj-proposal-draw)

SRC-1, `crates/eigenius-encoding/src/claim_kind.rs`: record stores sentence, chosen gloss, kind IRIs and optional natural-language rationale. Kind IRIs are symbolic classification outputs; rationale supports review rather than determining classification at its operational consumer. The key is only sentence plus gloss, unlike selection/proposal's full document hash and contextual inputs. This limits the source's broad description that a different question cannot replay silently. Authoring of old external kind files and actual human sign-off remain unresolved; record comments describe untrusted judgment, not an enforced human admission gate. No supplied object counterpart.

> /// The classifier's stated reasoning, when it gave one. `default` so draws recorded before
>     /// this field still replay (the replay key is sentence+gloss; the rationale is for review).
> --- `crates/eigenius-encoding/src/claim_kind.rs`

#### MEM-OBJ-layer-resources
Label: Layer-resident resources

SRC-1, `kernel/src/server/query.rs`, `kernel/src/layer/consolidate.rs`, with supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). This container is the branch/layer resource corpus, broader than [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource) and distinct from the unlanded [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact). Symbolic resource IDs, properties, executable bodies and declarations share the layer substrate with prose fields interpreted by humans/models. Parent chains, definitions and tombstones determine visibility. Original provenance is heterogeneous: callers, generated artifacts, program/query outputs and imports. Admission mechanism must be traced per path, not inferred from the common substrate. Known consumers are query evaluation, document parsing, program resolution, institution-index rebuild and notebook reopen. The first-seen definition/tombstone rule is witnessed under [MEM-RTE-state-maintenance](#mem-rte-state-maintenance).

#### MEM-OBJ-vector-segment
Label: Vector index segment

SRC-1, `kernel/src/server/hooks.rs`, `kernel/src/query/vector/search.rs`: layer/index-keyed derived numerical vectors and optional HNSW graph, with symbolic subject IDs, model/dimension/metric metadata. Dense representations are distributed-parametric content used for similarity, not evidence of updated provider weights. Retained segments derive from indexed resource material through an embedder; exact source-property extraction and provider internals remain uninspected. This is a distinct derived object, not the original text or [RT-CMP-reading-model](runtime.md#rt-cmp-reading-model). No supplied counterpart. Search validates segment shape and skips shadowed subjects; [MEM-RTE-query-resources](#mem-rte-query-resources) establishes its later selector, while [MEM-RTE-index-refresh](#mem-rte-index-refresh) establishes automatic refresh. No exact external embedding-model version or provider fixity is established by a model IRI.

#### MEM-OBJ-notebook-cells
Label: Published Notebook and Cell resources

SRC-1, `clients/eigenius-ts/src/notebook.ts`: content-addressed Notebook/Cell resources store ordered cell identities and editable source/configuration. Natural-language markdown/formalization prose, symbolic query/program references and notebook metadata have different consumers. They are published source, not a complete persisted execution transcript. Search of `notebooks/src/runtime/notebookStore.ts` identifies outputs as not persisted across reloads; this is narrower than claiming no execution results persist anywhere, since formalization results and program traces have separate stores. Notebook resources are a distinct part of the general resource corpus, with no supplied object counterpart.

> /** All resources to send via Load (Notebook + unique cells). */
>   resources: readonly EigonResource[];
> --- `clients/eigenius-ts/src/notebook.ts`

### Routes

#### MEM-RTE-draw-retention
Label: Draw retention and replay

This is the write/read-back subroute of the supplied formalization task, not another end-to-end task.

Part of: [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)

Caller triggers formalization; code reads a previous document branch or accepts inline records, installs seam-specific replay/live implementations, recreates document glossary state and appends only live recorded exchanges. SRC-1, `crates/eigenius-encoding/src/formalize.rs`, `kernel/src/dcg/pipeline.rs`, `kernel/src/dcg/draw.rs`. Code controls physical persistence; a live model supplies decisions, not commit authorization. Generic inline/CLI callers leave human authorship and per-content approval unresolved. No answer oracle or improvement trigger is required: mode is open-request encoding/reproduction. Guidance is current prose, lexicon/context and seam prompts; admission parses records and follows parser/emitter rules, not a general truth adjudication. Errors can abort, but branch reset/glossary persistence precedes later strict-emission errors and is not shown rolled back.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: draw count as part of formalizer output; the task/artifact return remains in the parent route.
- Later read-back: next default-branch formalization selects ProposalDraw resources by type and seam, parses their JSON and uses keyed answers; inline records provide an alternative delivery path without requiring branch retention.
- Delegated visibility: replay implementations receive structured questions; live rankers receive seam context, not an enclosing agent conversation. The record omits full document text in favor of its hash where specified above.
- Selection predicate: explicit live bypasses stored draws; inline supplies its seam map; branch mode reads prior head. Empty seam array is treated as no recording. Within a replay implementation the question key selects an answer; miss semantics differ by seam.
- Invalidation or expiry: changed key causes miss; no time expiry was found in this bounded route. Branch recreation removes the old draw-bearing head from this branch, and replay arms contribute no replacement transcript. Other roots may preserve old layers but are not automatically selected by this default route.
- Activation or effect: replay can return prior choices, rankings, refusals and classifications without a new model call; actual replay hits and later effects are unobserved.
- Evidence limits: same document ID does not guarantee indefinite replay, complete reproduction or correct interpretation. Kind keys do not encode all contextual inputs. Concurrent same-document handling and full backend CAS behavior remain uninspected.

The decisive lifecycle countercase is executable code, not only a warning comment:

> let _ = backend.delete_branch(&branch);
>                 backend
>                     .put_branch(&branch, self.base.id())
>                     .map_err(|e| PipelineError::Persist(format!("point {branch} at base: {e}")))?;
> --- `kernel/src/dcg/pipeline.rs`

> /// Every live arm's recorded exchanges, by seam. Replayed arms contribute nothing.
> --- `crates/eigenius-encoding/src/formalize.rs`

> if resources.is_empty() {
>         return Ok(0);
>     }
> --- `kernel/src/dcg/draw.rs`

Together these show why “zero new draws” is not equivalent to “old draws remain available through the new head.” The supplied test deliberately uses inline draws and asserts zero committed draws; it does not test the next branch-based round (SRC-1, `crates/eigenius-encoding/tests/served_formalization.rs`). A mixed replay/live round similarly appends only its live subset unless the chosen base independently contains old draws.

#### MEM-RTE-query-resources
Label: Query retained resources

Distinct from program execution and Load: caller EigenQL enters the Query handler, resolves a branch/layer, executes with institution/component/embedding registries, returns a resource result document, and may persist FIBER INTO resources through WithRetroactive. SRC-1, `kernel/src/server/query.rs`, `kernel/src/query/evaluate/similarity.rs`, `kernel/src/query/vector/search.rs`. It overlaps their shared persister but has no supplied route counterpart. Code owns selection and admission; caller supplies query and optional write expression. Caller identity does not establish human approval. This is an open request with no general expected-answer oracle. INTO can fail before or during commit; commit uses default policy, no institution admission context, and post-persist hook warnings do not undo the commit. Read-side institution dispatch is distinct from AutoOnLoad admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/error and encoded result document; INTO additionally returns output IRIs and advancement/merge information.
- Later read-back: each query invocation selects retained chain resources. INTO-produced resources become available to subsequent queries or other chain consumers when admitted.
- Delegated visibility: evaluator sees selected read layer and runtime registries; the requesting MCP/SDK/notebook caller receives query results, not the entire corpus automatically. An external agent may interpret those results, but its subsequent decisions are outside this traced consumer.
- Selection predicate: EigenQL structure and predicates; similarity chooses text, vector or hybrid based on hints/active indexes. Query text is embedded for vector matching; top-k search filters shadowed subjects. Explicit limits override derived pools; TOP-derived pools overfetch with a floor. This is relevance ranking, not mere identifier targeting.
- Invalidation or expiry: branch/layer visibility and tombstones govern resource selection; mismatched vector metadata errors. Missing segments are skipped, so an incomplete sweep can reduce retrieval rather than make content absent from storage.
- Activation or effect: retained values affect returned bindings/rankings; INTO can add resources. No observed use, model-context injection, scientific verification or retrieval-benefit result supplied.
- Evidence limits: a storage API alone would not establish this consumer; the handler-to-evaluator wiring does. Full FIBER semantics and all caller displays remain uninspected. Search budget is a candidate bound, not a model token budget.

> let scores = fuse_rrf(&text_hits, &vector_hits, k);
> --- `kernel/src/query/evaluate/similarity.rs`

> crate::commit::PipelineKind::WithRetroactive,
>                 crate::commit::EmissionKind::Child,
>                 working,
> --- `kernel/src/server/query.rs`

#### MEM-RTE-index-refresh
Label: Post-commit index refresh

SRC-1, `kernel/src/server/hooks.rs`: a post-commit host hook rebuilds institution dispatch state; another optionally schedules vector sweep then reindex. Distinct maintenance consumers, sharing a commit trigger, not a new model inference route. Closest supplied record [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) mentions refresh but does not declare this asynchronous transformation route. Host/embedder configuration permits it; resource declarations select active indexes. Admission is software-controlled derivation, not per-vector human approval. Mode is maintenance, with no answer oracle or demonstrated improvement trigger. Failures log/surface task information; a committed resource is not rolled back because its vector derivation failed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook returns without waiting for detached embedder work; absent coordinator or active indexes makes vector scheduling a no-op.
- Later read-back: later query similarity uses persisted segments; later institution dispatch uses rebuilt index/runtime. Finished successful sweeps need not leave a TaskStore record; segments are their retained product.
- Delegated visibility: institution rebuild reads declarations from the new chain; sweep receives layer and embedder registry. Exact property extraction/batching transport remains uninspected, not assumed to include every resource field.
- Selection predicate: post-Load hook checks optional coordinator and active VectorIndex declarations; sweep covers new-layer content and reindex targets pre-existing layers built under superseded models.
- Invalidation or expiry: reindex replaces derived segments for changed model declarations; failures may leave missing segments or a mixed-model chain. GC can cancel sweeps for deleted layers.
- Activation or effect: derived numerical state changes later ranking inputs; institution rebuild changes available dispatch metadata. No observed ranking, dispatch or benefit supplied.
- Evidence limits: asynchronous derivation is non-gating; commit success does not certify retrieval completeness. Full text-index write lifecycle, embedding-provider identity/fixity and all durable resume paths remain unresolved.

> coord.trigger_reindex_async(reindex_layer).await
> --- `kernel/src/server/hooks.rs`

The complete hook must be inspected before interpreting successful task lookup as a full derivation history: it explicitly distinguishes successful sweeps from persisted reindex/failure records. This record does not classify these segments as learned scientific claims or logs transformed into general instructions.

#### MEM-RTE-state-maintenance
Label: Layer consolidation and collection

SRC-1, `kernel/src/layer/consolidate.rs`, `kernel/src/server/gc.rs`, with supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) for rejection/cascade. Distinct from knowledge admission: caller-requested consolidation collapses an existing layer range; GC gathers roots and invokes collection with deletion hooks. Software controls the transformation/deletion; a generic administrative caller does not establish human curation. These are maintenance requests, not model-authored summaries or an improvement experiment. Full consolidation admission/CAS and GC engine contracts are not independently traced.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: consolidated layer/branch outcome at the server seam or GC marked/unreachable/swept/protected counts; estimates do not themselves delete content.
- Later read-back: later layer resolution uses the consolidated bodies/tombstones or installed redirect; collected layers cease to be available through deleted storage. A branch head/tag/task pin can retain history independently of another branch's reset.
- Delegated visibility: consolidation reads a requested range; GC sees branch heads, tag targets and current-session non-terminal task layer pins. No model-context window is involved.
- Selection predicate: consolidation walks head-to-root and retains first modification per IRI, including tombstones; GC uses gathered roots and default configuration, with age-protection accounting in its response.
- Invalidation or expiry: tombstones suppress resolution without proving physical erasure; consolidation can preserve their suppression. GC deletes eligible unreachable layers, distinct from a content verdict. Full metadata-blob expiry and completed-task result deletion remain uninspected.
- Activation or effect: maintenance changes resolution/storage topology, not the meaning of a prose summary. Deletion hooks provide cache eviction/sweep cancellation inputs; successful consistency was not observed.
- Evidence limits: no general erasure guarantee, historical reconstruction guarantee or crash-atomicity conclusion. Current-session task-root gathering is not proof that all sessions' nonterminal tasks are pinned.

> for tomb in layer.tombstoned_iris() {
>             if !seen_iris.insert(tomb.clone()) {
>                 continue;
>             }
>             consolidated_tombstones.insert(tomb.clone());
>         }
> --- `kernel/src/layer/consolidate.rs`

> .filter(|r| !r.status.is_terminal())
>                     .map(|r| r.layer_head)
> --- `kernel/src/server/gc.rs`

#### MEM-RTE-notebook-reopen
Label: Publish and reopen notebook

SRC-1, `clients/eigenius-ts/src/client.ts`, `clients/eigenius-ts/src/notebook.ts`, `notebooks/src/runtime/publishedNotebooks.ts`. Shipped caller route distinct from the generic Load route it invokes. Caller-edited notebook source is converted to content-addressed resources, auto-committed via Load and later reconstructed by inspecting Notebook and referenced Cells. Generic SDK use leaves human authorship unresolved; browser publish affords explicit user action but does not require human approval of each model-produced claim. Open publication/reopening, not an oracle-scored improvement mode. Load rejection returns failed publish; reopening missing resources throws. No automatic execution follows merely from the inspected reopen function.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: publish returns Notebook/Cell IRIs plus Load outcome; reopen returns NotebookJson or error.
- Later read-back: later caller chooses a published notebook IRI; inspect fetches the notebook and each referenced cell, then reconstructs editable cells. Subsequent execution can re-run retained query/prose/program configuration through the supplied runtime routes.
- Delegated visibility: ordered notebook metadata/source reaches the editor; outputs are not silently reconstructed as prior execution evidence.
- Selection predicate: explicit notebook identity, then cell references; content addressing/deduplication does not establish topical relevance ranking. Listing/search is a separate discovery surface, not fully traced here.
- Invalidation or expiry: resources must remain resolvable in the current chain; missing Notebook/Cell errors interrupt reopen. New content can have new content-addressed IDs; deletion obeys layer visibility and GC limits above.
- Activation or effect: retained source/configuration can guide a later requested cell execution, including formalize land configuration; no observed reopening or automatic rerun supplied.
- Evidence limits: published source is not a full checkpoint of ephemeral outputs, browser UI state or external runtime effects. Local save/autosave and merge-resolution recovery remain uninspected.

> return resourcesToNotebookJson(notebookIri, resources);
> --- `notebooks/src/runtime/publishedNotebooks.ts`

> if (!load.ok) {
>       // `response` is dropped, not forwarded: it is a `LoadResponse`, and this outcome is
>       // typed at `{ publish, load }`. That is what makes the field optional.
>       return { ok: false, message: load.message, errors: load.errors };
>     }
> --- `clients/eigenius-ts/src/client.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-recorded-decision
Label: Recorded decision replay authority

Consumer: seam-specific replay implementation and parser/resolver/lander. Channel: branch- or inline-loaded structured record, selected by question key. Force: symbolic choice/ranking/proposal/classification output, not optional background prose; refusal/abstention can withhold an output. Horizon: later invocation while accessible and key-compatible, subject to branch-reset limit. SRC-1, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/dcg/proposer_record.rs`, `crates/eigenius-encoding/src/formalize.rs`; minimum witness is the returned stored ReadingSelection in [MEM-OBJ-selection-record](#mem-obj-selection-record). Distinct from [RT-BAP-retained-program](runtime.md#rt-bap-retained-program): these records answer bounded decision seams, not arbitrary retained program dispatch.

#### MEM-BAP-institution-refresh
Label: Retained institution dispatch authority

Consumer: institution-index/runtime rebuild, then subsequent institution dispatch. Channel: symbolic declarations read from the committed chain and mapped to registered external/in-process implementations. Force: changes dispatch/admission context; malformed entries can be logged and skipped, and unavailable orchestrator implementations cannot be conjured by declarations. Horizon: later operations under rebuilt runtime, not necessarily the Load batch that first declares them. SRC-1, `kernel/src/server/hooks.rs`; supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) bounds same-batch authority. Distinct from retained program execution and the broader host registration route.

> *self.institution_runtime.write().await = Arc::new(runtime);
> --- `kernel/src/server/hooks.rs`

## Annotations

#### On [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact)

Memory consumer is explicit result fetch, followed optionally by Load. Its metadata-blob persistence differs from chain admission and from draw retention. Raw source-to-encoded-resource transformation occurs before the blob; fetching does not certify approval. Opaque encoded bytes and the decoded/rendered ESL/JSON presentation must not be treated as different authorities merely because the display is readable. Model decisions/selection rationales have separate records above. Terminal write errors and unspecified result expiry limit durable checkpoint claims (SRC-1, `kernel/src/server/formalize.rs`, supplied parent record and [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)).

#### On [RT-OBJ-program-resource](runtime.md#rt-obj-program-resource)

Later IRI resolution is a real executable read-back route, unlike arbitrary storage methods with hypothetical consumers. Its symbolic body and model-interpreted completion strings remain separate consumption paths. Produced resources/traces can persist without establishing an automatic trace-to-instruction or trace-to-policy transformation. No such later trace-derived policy consumer is established in this bounded inspection; durable task recovery remains unresolved rather than absent. SRC-1, `kernel/src/server/programs.rs`, `kernel/src/program/eval_io.rs`, supplied [RT-RTE-program-execution](runtime.md#rt-rte-program-execution).

#### On [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection)

Working-context control is code-selected decision framing: current full document, sentence and earlier selected glosses, with at most twelve shown structure groups. Raw pool remains outside the shown model presentation; the chosen answer/rationale crosses back. This is not accumulated-chat compaction or cross-session conversational memory. The call-frame analogy fits selected inputs and return value, but fails as a pointer model: document/glosses are passed by value in model context, not dereferenceable retained-store addresses. SRC-1, `kernel/src/dcg/reading_ranker.rs`:

> const MAX_STRUCTURES_SHOWN: usize = 12;
> --- `kernel/src/dcg/reading_ranker.rs`

> (DOCUMENT.into(), ctx.document.trim().to_string()),
>         (EARLIER.into(), prior.join("\n")),
>         (SENTENCE.into(), ctx.sentence.trim().to_string()),
> --- `kernel/src/dcg/reading_ranker.rs`

No token-budget or document-truncation guarantee follows from the structure-group count. Reload of retained decisions happens through draw replay, not by bringing removed chat turns back into this frame.

## Write side

The acquisition paths have different control and trust boundaries:

- Prose/inline draw callers supply inputs; live models supply judgments; recorders serialize exchanges; direct branch persistence retains them without a mandatory human sign-off. Source labels, document hashes and candidate keys preserve lineage but not truth. A recorded refusal is retained outcome data, while its replay supplies a later decision. This raw-exchange-to-structured-draw-to-replay chain gives prior execution an operational consumer without parameter training or evidence of improved capacity. [MEM-RTE-draw-retention](#mem-rte-draw-retention).
- Automatic glossary augmentation precedes parsing. Its direct persister path is not the Load admission pipeline, and it can survive later artifact failure. The supplied source explicitly distinguishes builder insertion from validation (SRC-1, `kernel/src/dcg/pipeline.rs`). Initial lexicon/bootstrap provenance remains unresolved, while the subsequent branch reset and glossary transformation are known.
- Generated artifacts are proposals/results until a caller loads them. Notebook `land` can automate that admission; generic caller identity cannot be replaced with a claim of human curation. Load structural/retroactive/institution rejection, cascade tombstones and retained audit siblings are scoped by [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). Audit survival is not proof that a later scientific reasoner consumes the rejection's rationale.
- Program outputs and FIBER INTO persist through WithRetroactive, not universal AutoOnLoad gating. They can be consumed as later resources; a raw trace is not thereby a derived instruction. [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), [MEM-RTE-query-resources](#mem-rte-query-resources).
- Vector refresh is automatic content-to-numerical-index derivation. Its source is resource material, not necessarily agent experience. It must not be conflated with trace-fed learning merely because it is asynchronous and retained. [MEM-RTE-index-refresh](#mem-rte-index-refresh).
- Consolidation preserves latest definitions and suppression markers; it is not semantic summarization. GC removes eligible unreachable storage, not rejected beliefs as such. Notebook publication retains editable source and references rather than full outputs. [MEM-RTE-state-maintenance](#mem-rte-state-maintenance), [MEM-RTE-notebook-reopen](#mem-rte-notebook-reopen).

Rationale retention is heterogeneous. Reading replay carries the rationale back with the decision; kind rationales are explicitly for review rather than consumed judgment criteria. Neither establishes a criticism/revision cycle. Full proposal/sense rationale consumer chains and human review operation remain unresolved. No learning or self-improvement outcome is inferred from recording/reproduction.

## Read-back

The strongest documented later consumer is the replay implementation: it turns selected retained exchanges into parser decisions. Exact contextual keys give bounded protection against stale answers but differ by seam; they do not guarantee semantic correctness. Read-back is triggered by another formalization request, not an unsolicited push to an agent. Retaining an old layer elsewhere does not make it selected by the default document branch. [MEM-RTE-draw-retention](#mem-rte-draw-retention).

The second class is requested graph consumption: query/inspect results, program IRI execution, institution rebuild and notebook reopen. Query selection may use structural predicates, lexical matching, numerical similarity or hybrid ranking; explicit identity resolution is not the same selection operation. Result counts/candidate pools are not context-token budgets. No inspected route automatically selects all relevant scientific evidence for a model. [MEM-RTE-query-resources](#mem-rte-query-resources), [RT-BAP-retained-program](runtime.md#rt-bap-retained-program), [MEM-BAP-institution-refresh](#mem-bap-institution-refresh), [MEM-RTE-notebook-reopen](#mem-rte-notebook-reopen).

Static shipped ontologies and prompt templates are context dependencies, not evidence of material accumulated through use. Current-document prior glosses are working discourse context until recorded; stored copies can later participate in replay keys. The decision-frame budget and omitted structure alternatives are covered in the reading-selection annotation, not mislabeled conversation-memory eviction.

## Integration issues

1. **Persistent replay horizon needs qualification.** [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize) correctly says draws are read before branch rebuilding, but readers must not infer indefinite persistence at that branch. Direct reset plus live-only recording gives the all-replay/mixed-subset countercase in [MEM-RTE-draw-retention](#mem-rte-draw-retention). This qualifies horizon rather than disputing that next-invocation replay is wired. Old roots/base contents and concurrent same-document cases remain unresolved.
2. **Different question keys.** The runtime's keyed-selection account holds for [MEM-OBJ-selection-record](#mem-obj-selection-record), and proposal keys include contextual identity; [MEM-OBJ-kind-record](#mem-obj-kind-record) uses sentence/gloss only. No universal full-context invalidation guarantee should span the four seams. Full sense/proposal rationale consumers remain unresolved; this prevents equal treatment of retained reasons.
3. **Additional write route.** [MEM-RTE-query-resources](#mem-rte-query-resources) establishes FIBER INTO admission through WithRetroactive. It extends, rather than duplicates, [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and [RT-RTE-program-execution](runtime.md#rt-rte-program-execution). Any universal admission summary must include it and distinguish read-side institution dispatch from write-side AutoOnLoad.
4. **Record identity.** No likely duplicate declarations remain after comparison: draw retention is explicitly part of the task route; four payload objects are parts of the draw envelope; corpus is broader than supplied program/artifact objects. Index refresh, query, notebook reopening and maintenance have distinct endpoints/consumers, although they share persistence infrastructure. [MEM-OBJ-layer-resources](#mem-obj-layer-resources) intentionally remains a valid container rather than superseding those parts.
5. **Retrieval completeness and deletion limits.** [MEM-RTE-index-refresh](#mem-rte-index-refresh) is non-gating, so successful admission does not establish complete vector recall. Full text-index maintenance, backend deletion consistency, cross-session task roots, task/result expiry and embedding-provider pinning remain unresolved. [MEM-RTE-state-maintenance](#mem-rte-state-maintenance) cannot certify erasure or complete recovery.
6. **Uninspected operative alternatives.** Bootstrap/importers, wider evaluator/institution routes, reflection API, local/offline CLI mutations, SDK breadth, autosave/merge recovery and durable task resume remain named in coverage above. This prevents a whole-system learning, reflection or maintenance-completeness assessment, not the supported positive findings about replay, query and publication. No peer epistemic/workflow member was supplied; potential cross-role overlaps cannot be checked here.

## Limitations and checks

Source HEAD was rechecked as `836498ebd99733067d45aa6f7b09d4ff5035dd99`; source status was clean. The invocation, member types, collection, worker rules and records contract were read completely, including bounded runtime and contract continuations. Model identity was obtained from PI_PROVIDER/PI_MODEL and effort from PI_REASONING_LEVEL. No prohibited prior analyses or target execution were used.

The served/CLI comparison test uses four inline recordings and requires an external DB snapshot plus WordNet data. Its source contract supports artifact-comparison intent, not successful execution, branch replay longevity, scientific fidelity or benefit (SRC-1, `crates/eigenius-encoding/tests/served_formalization.rs`). Implementation findings do not establish deployment grants, provider truthfulness, model compliance, actual retention under failure, or a general theory-building/criticism loop. No content-directed criticism is inferred from type validation, logging or selection alone.

Validation: the supplied validate-output command exited 0 and reported “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” A content pass establishes structure, references and quotation occurrence, not semantic acceptance or observed operation.
