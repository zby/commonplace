---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "PageIndex document memory: separately retained page text, derived outlines, discovery metadata, tool read-back and caller-owned transcripts."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
source-identity: https://github.com/VectifyAI/PageIndex
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
---

# PageIndex memory report

## Boundary and evidence

This report covers the shipped document-memory loop at the [boundary](boundary.md): local PDF admission, retained pages/outlines/metadata, discovery and selective delivery, deletion and cache repair, alternative file builders, optimizer cache input and diagnostic output, caller-managed chat transcripts, framework tools and notebook consumers. Cloud client wiring is included; remote storage, selection, model weights and live instructions are opaque. All findings use SRC-1 at the frozen commit. HEAD was rechecked as `af92d9658a6a9c0ae31171b43198db28951af2f4`. No target code, tests, notebooks or provider calls were executed.

Direct inspection extended the supplied runtime with complete `pageindex/local_store.py`, submission and read/management methods in `pageindex/local_api.py`, structure/page/removal/discovery helpers in `pageindex/agent_tools.py`, summary methods and bookkeeping removal in `pageindex/utils.py`, and cache loading, candidate ownership, selection and CLI output in `pageindex/tree_optimize.py`. These supply implementation evidence, not observed operation. Other coverage below explicitly relies on supplied runtime findings rather than implying fresh inspection.

| Entry point or memory operation | Source path | Coverage and limit |
|---|---|---|
| PDF submission; Flash/classic production and refusal | `pageindex/local_api.py`, `pageindex/flash/api.py`, `pageindex/page_index_classic.py` | Direct wrapper read; [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine). Deep parser internals rely on runtime; no extraction-accuracy conclusion. |
| Tree/pages/metadata save and reload | `pageindex/local_store.py`, `pageindex/local_api.py` | Direct; [MEM-OBJ-tree](#mem-obj-tree), [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-doc](#mem-obj-doc). |
| Browse, structure and page tools | `pageindex/agent_tools.py` | Direct; [MEM-RTE-document-readback](#mem-rte-document-readback). |
| Delete, malformed metadata fallback, manifest rebuilding | `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/agent_tools.py` | Direct; [MEM-RTE-store-maintenance](#mem-rte-store-maintenance). |
| Flash summaries and document description | `pageindex/utils.py`, `pageindex/local_api.py` | Direct selected transformation methods; [MEM-OBJ-tree](#mem-obj-tree), [MEM-OBJ-doc](#mem-obj-doc); scheduler lifecycle supplied by runtime. |
| External heading cache and optimizer logs/output | `pageindex/tree_optimize.py` | Direct; [MEM-OBJ-headings-cache](#mem-obj-headings-cache), annotation on [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine). Cache's initial author/provenance unresolved; no trace-origin inference. |
| CLI Flash/classic/Markdown and direct builders | `run_pageindex.py`, `pageindex/page_index_md.py`, `pageindex/page_index_classic.py` | Supplied [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders); no inferred automatic import into managed store. |
| Chat Completions, Responses, Messages; stream alternatives | `pageindex/local_chat.py`, `pageindex/client.py` | Supplied [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history); no durable session store established by these paths. |
| Framework registrations and management opt-in | `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py`, `pageindex/agent_tools.py` | Supplied [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools); actual host histories and extra tools uninspected. |
| Cloud upload/getters/MCP/managed chat | `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`, `pageindex/client.py` | Supplied [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools); server lifecycle and retrieval transformations inaccessible, preventing cloud-memory classifications beyond client-visible affordances. |
| Six cookbook consumers, including separate vision pipeline | `cookbook/pageindex-vision-rag.ipynb`, `cookbook/pageindex-flash-demo.ipynb`, `cookbook/pageindex-citation.ipynb`, `cookbook/pageindex-indexing-cost-demo.ipynb`, `cookbook/pageindex-multimodal.ipynb`, `cookbook/pageindex-query-pricing-demo.ipynb` | Boundary inventory and [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook); notebook source wiring only, not embedded-output execution evidence. |
| Contract evaluators, example trees and benchmark illustrations | `tests/`, `examples/`, `assets/`, `README.md` | Boundary and runtime supply selected test/claim coverage. Remaining fixture bytes and evaluation bodies not inspected here; prevents exhaustive evaluator or independent performance conclusions. No evaluator-to-production-memory update demonstrated. |

## Core ideas

PageIndex retains document knowledge, not merely a conversation cache. A local document separates source-derived page text from derived navigation material and descriptive metadata. Later tools load the outline without full text, then selected pages. The outline's summaries can influence what the answering model elects to read, but are not an answer oracle. See [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-tree](#mem-obj-tree), [MEM-RTE-document-readback](#mem-rte-document-readback).

Persistence and context reduction are different mechanisms. Storing pages makes later retrieval possible. Omitting page text from an outline and limiting tool responses controls one model invocation's context without deleting the underlying evidence. Leaf/parent summary calls also isolate work in separate selected-input frames; only returned titles/summaries escape into the tree. Neither implies compaction of an accumulated answering conversation. Supplied [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history) instead exposes raw appendable tool history for caller-managed reuse.

Admission is mostly software/model-controlled after caller initiation. Generated summaries and descriptions do not receive per-content human approval in local submission. The caller may be human or programmatic; submitting a PDF is not approval of every generated claim. Content reaches the answering model as evidence through tools, while shipped managed instructions have a separate policy channel. Delivery is wired; compliance, answer dependence and improvement are unobserved. SRC-1: `pageindex/local_api.py`, `pageindex/agent_tools.py`; [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-pages
Label: Stored page text

Source-native identity: `docs/<doc_id>/pages.json`, a list of `page_index`/`markdown` entries. Natural-language extracted document content is wrapped in symbolic page indexes and JSON fields; the index addresses source location rather than semantic relevance. Substrate: local filesystem JSON. Lineage: submitted PDF → PyPDF2 extraction → surrogate scrubbing → numbered strings. This is source-derived text, not an agent execution trace, and the field name `markdown` does not establish layout-faithful OCR. Local submission does not retain the original PDF in this store method. These are retained results of [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), not another declaration of that route. SRC-1: `pageindex/local_api.py`, `pageindex/local_store.py`.

> pages = [{"page_index": i + 1, "markdown": text}
>                  for i, text in enumerate(page_texts)]
> --- `pageindex/local_api.py`

Consumers: local OCR getters return page lists or joined text; tree-with-text reconstruction uses these pages; page tools select requested numbered entries for answering models. The text has evidential authority by model interpretation, not executable tool-policy authority. Retained indefinitely by these save/read methods until deletion; no TTL is implemented there. Storage capability alone is not the read-back finding: the shipped tool/QA connection is [MEM-RTE-document-readback](#mem-rte-document-readback).

#### MEM-OBJ-tree
Label: Stored document tree

Source-native identity: `docs/<doc_id>/tree.json`. Substrate: local JSON. Split by consumption: symbolic `node_id`, page spans and `nodes` support fixed traversal and reconstruction; natural-language titles, summaries and optional `key_items` describe/navigation-guide the document for a model. It is derived document material, not retained weights or a conversation trace. Production differs across Flash layout/refinement and classic model extraction; compare [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders). Distinct identity from both producer routes. SRC-1: `pageindex/local_api.py`, `pageindex/utils.py`.

> self._store.save_document(
>                 doc_id, meta, remove_fields(structure, fields=["text"]), pages)
> --- `pageindex/local_api.py`

The managed store omits node text; `_load_tree_with_text` reconstructs it from separately stored pages. `_format_tree_node` selectively exposes summaries when requested. Tool structure retrieval requests summaries and no text. Therefore the model-visible outline is not all retained source content.

Flash summary lineage includes raw text reuse for short leaves, model summaries for longer leaves, and parent summaries based on opening text plus child titles/summaries. Merged same-page leaves may acquire generated titles. This is automatic document transformation, not trace-fed learning. No per-summary human approval or independent expected-answer reference appears in the inspected methods; parsing and fallback admit the text. Reasons for a summary's wording are not a separately retained field in this path. Document evidence remains reachable via pages, but that is not a retained justification for each generated statement.

> if count_tokens(text, model=self._model) < self._small_node_tokens:
>             return text.strip()
> --- `pageindex/utils.py`

> [{'title': c.get('title', ''), 'summary': c.get('summary', '')} for c in children],
> --- `pageindex/utils.py`

Later consumer: an answering/selection model receives outline descriptions through tools and may choose pages accordingly; deterministic reconstruction consumes spans. Authority is navigation evidence for the model and addressing authority for code. Actual relevance, factual fidelity and answer effects are unobserved.

#### MEM-OBJ-doc
Label: Document metadata and manifest cache

Source-native identities: `docs/<doc_id>/doc.json` and `manifest.json`'s `docs` mapping. Substrate: local JSON. Natural-language `description` comes from a generated document distinction sentence; symbolic fields carry IDs, names, status, creation time, page count, mode and caller JSON metadata. Caller metadata authorship and whether a human deliberately approved it are unresolved; local validation checks serializability, not truth. No counterpart object is declared in runtime; these are distinct retained outputs of [RT-RTE-local-submit](runtime.md#rt-rte-local-submit). SRC-1: `pageindex/local_api.py`, `pageindex/local_store.py`, `pageindex/utils.py`.

> description = generate_doc_description(
>             create_clean_structure_for_description(structure, top_level_only=True),
>             model=self._summary_model,
>         )
> --- `pageindex/local_api.py`

`doc.json`'s presence gates reads; the manifest is discovery/cache data, not the page-content store. Getters can fall back to valid cached metadata if the marker exists but metadata is malformed. Listing prefers a valid cached entry, otherwise reads metadata from disk; it reconstructs the set from document directories. Thus repair is cache membership/format recovery, not semantic document curation or guaranteed freshness against an external manual edit.

> meta = cached.get(name)
>             if not _is_valid_meta(meta, name):
>                 meta = _read_json(self._docs / name / "doc.json")
> --- `pageindex/local_store.py`

Discovery tools expose names/descriptions/status and filtered caller metadata; a model must judge relevance rather than receive local semantic ranking. Natural-language descriptions guide document choice; the marker and valid metadata control software availability. These forces differ even though the same store holds them. Deletion and repair are traced in [MEM-RTE-store-maintenance](#mem-rte-store-maintenance).

#### MEM-OBJ-headings-cache
Label: External headings cache

Source-native identity: optimizer `--headings`, loaded by `load_headings_cache`. Filesystem JSON is converted to a page-keyed mapping of heading records; titles are natural-language document labels and `page`/`kind` supply symbolic routing/filter values. Initial detection author, human approval and whether a model or deterministic process generated the cache are uninspected. Known subsequent transformation must not be suppressed by that provenance gap. SRC-1: `pageindex/tree_optimize.py`.

Part of: [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine)

This object is a retained-input part of that broader route, not a second refinement route. It offers an alternative to model-proposed headings. `children_from_cache` selects the node's page span and configured heading kinds, excludes its own normalized title, creates candidates and submits them to ownership/cost selection. Its downstream consumer is the optimizer; admitted titles/spans can enter a revised tree, and managed submission can retain that product. Direct optimizer callers own persistence.

> cached = own(children_from_cache(node, args.cache, args.kinds))
>         if cached:
>             candidates.append(("cache", cached))
> --- `pageindex/tree_optimize.py`

The cached path does not run the model-proposal branch's explicit printed-heading substring rejection. `own_children` rejects certain known/outside-own-section headings, but missing printed matches alone do not veto a cached heading. Consequently a universal printed-heading admission guarantee would be too strong. Whether an actual cache contained an unprinted heading is unobserved.

> A heading not found on its page decides nothing.
> --- `pageindex/tree_optimize.py`

### Routes

#### MEM-RTE-document-readback
Label: Document tool read-back

Endpoints/progression: later QA invocation → model chooses discovery/structure/page tools → document resolution and completion checks → local getter reload → response selection/formatting → tool-result channel into answering context. Owner: model chooses semantic reads; PageIndex code chooses response slices and enforces local tool scope. Distinct from the encompassing [RT-RTE-document-chat](runtime.md#rt-rte-document-chat) and framework loop affordance [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools): this record isolates the shared retained-content selection/delivery chain, spanning both caller paths. SRC-1: `pageindex/agent_tools.py`, `pageindex/local_api.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured success/error envelopes, including discovery metadata, an outline part or selected page strings and follow-up hints.
- Later read-back: stored document material reaches a later chat/tool invocation; model semantic choice is required for ordinary tool retrieval, not automatic unsolicited content supply.
- Delegated visibility: answering model sees returned metadata, selected outline chunk or included pages; store loading can read more locally than is delivered to the model.
- Selection predicate: discovery uses offset/limit, time ordering and optional local scope; local query/relevance search is rejected. Structure uses resolved document plus requested part; page retrieval uses requested page specification and response-size selection, not a relevance scorer.
- Invalidation or expiry: deleting the marker prevents future managed reads; response omissions remain reloadable by another request. Earlier delivered tool strings are not recalled from a caller transcript.
- Activation or effect: response delivery is wired; actual changed choices, answers and benefit remain unobserved.
- Evidence limits: source-only account; external runners own repeated invocation and live cloud tools have opaque selection policies.

> tree = client.get_tree(entry["id"], node_summary=True,
>                                include_text=False).get("result")
> --- `pageindex/agent_tools.py`

Outline formatting strips text and splits around a nominal 95,000-character budget. A leaf with no children can remain oversized, so outline partitioning is not a strict maximum either. Page tools construct a numbered map, select requested valid pages and admit the first valid page even if it exceeds budget; subsequent pages must fit. The nominal constant is 100,000 with a 0.95 internal factor. These are serialized-character heuristics, not token-window guarantees. The next-step envelope names omitted pages/outline parts, making further requests possible without retaining every source page in the current window.

> if not included or budget - size >= 0:
>             content.append(entry)
>             included.append(page)
>             budget -= size
> --- `pageindex/agent_tools.py`

No new content admission occurs in this read route. Requests come from model/caller action, with code selecting delivery portions; guidance asks the model to match documents and use structure first for larger PDFs. Those instructions do not enforce reading order or turn external document text into trusted policy. The stack-frame analogy fits isolated indexing/summary calls only partially: inputs are passed by value and results escape, while tool retrieval is explicit reload from a store, not automatic dereferencing of a pointer in the model window.

#### MEM-RTE-store-maintenance
Label: Store withdrawal and cache repair

Endpoints/progression: direct SDK deletion or opt-in management tool → resolve ID → unlink `doc.json` → attempt directory removal → remove manifest entry; alternatively later listing/getter → discover surviving markers and validate/fallback metadata → opportunistically repair manifest. Owner: API/store code; caller or model with an explicitly granted remover initiates deletion. Distinct from [RT-RTE-local-submit](runtime.md#rt-rte-local-submit)'s new-document admission and [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools)'s capability registration. SRC-1: `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/agent_tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/not-found from SDK; management tool reports per-document deleted/not-found/failed results. Listing returns current recognized metadata.
- Later read-back: future document discovery/content getters require a surviving marker; repaired manifest supports subsequent metadata reads. Prior returned strings and external file outputs are outside this withdrawal.
- Delegated visibility: tools receive names and management outcomes, not deleted page content; local filesystem deletion uses host authority.
- Selection predicate: valid direct ID or resolved scoped names; management validates nonempty string lists, deduplicates and limits to ten before deleting. Cache repair selects safe directories with markers and valid cached or on-disk metadata.
- Invalidation or expiry: unlinking the marker withdraws managed availability; no timer, tombstone history or document rollback is supplied by these methods.
- Activation or effect: code changes future getter/list visibility; actual deletion/recovery execution is unobserved.
- Evidence limits: recursive cleanup ignores errors and manifest write suppresses OSError, preventing a secure-erasure or multi-file transactional guarantee. No externally retained transcript or model-provider copy is revoked.

> (doc_dir / "doc.json").unlink()
> --- `pageindex/local_store.py`

> if doc_dir.is_dir():
>             shutil.rmtree(doc_dir, ignore_errors=True)
> --- `pageindex/local_store.py`

Admission/recovery: deletion is admitted by software after valid input/resolution, without an additional human per-document confirmation inside the tool. Default built-in read tools omit management; the SDK still exposes deletion. There is no QA oracle or improvement objective in this maintenance route. Repair follows structural metadata validation and filesystem existence, not model judgment or human curation. Recovery from withdrawal requires an external backup or re-submission, not an inspected undo mechanism. Save uses per-file temporary-write/fsync/replace, not a transaction across tree/pages/marker/manifest; partial save failure is not guaranteed to roll back. See also [RT-RTE-local-submit](runtime.md#rt-rte-local-submit).

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine)

Memory-specific lineage: retained document text feeds candidate headings and derived summaries, not execution-outcome traces. Candidate costs/events form diagnostic data; accepted children form the later navigation product. The optional optimizer CLI log stores configuration, before/after metrics, ID map and decision events. The revised JSON does not automatically carry that event rationale, and the inspected CLI writer does not wire the log into subsequent answering. Logs therefore do not establish trace-fed policy learning. External cached headings are separately identified in [MEM-OBJ-headings-cache](#mem-obj-headings-cache). SRC-1: `pageindex/tree_optimize.py`, `pageindex/utils.py`.

> "before": result["before"], "after": result["after"],
>                    "id_map": result["id_map"], "events": result["log"]},
> --- `pageindex/tree_optimize.py`

Within a summary run, child summaries are delivered to later parent-summary invocations; across runs, managed-store trees can deliver them to answering models. That is document-derived retention at two horizons, not evidence that a summary is semantically lossless. Raw source remains separately reachable. The generated text does not preserve a model's hidden reasoning or an explicit per-claim justification; optional optimizer event records explain structural choices instead.

#### On [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history)

Memory substrate is caller-held Python/JSON transcript values unless the caller persists them. Responses `items` and Messages `messages` expose earlier tool turns for later invocation; history is raw interaction material rather than a derived memory summary. Selection of which history survives is caller-owned. Messages strips unexecuted final tool uses and request cache marks, so appendable history is not necessarily byte-for-byte provider output. Chat Completions does not supply the same appendable tool history. These distinctions and their minimum passages are supplied by the cited runtime record (SRC-1: `pageindex/local_chat.py`). Provider caching metadata is not evidence of transcript compaction, long-term learning or a durable server-side session. Caller reuse is afforded/wired at the interface, not observed.

#### On [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders)

Retained output is caller-owned tree JSON, with optional node text/summaries and document description according to builder flags. A CLI result is not a managed-store marker/pages set. Overwriting the derived output path is replacement, not versioned curation. Classic model verification can affect what survives generation, but the cited runtime record shows bounded repair/fallback rather than guaranteed correction. Markdown thinning is an alternative transformation, not PDF-store admission. Later generic file consumers are unspecified, so this surface alone establishes persistence capability, not a demonstrated read-back route (SRC-1: `run_pageindex.py`, `pageindex/page_index_classic.py`, `pageindex/page_index_md.py`).

#### On [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools)

Remote IDs afford later client getters; their existence does not reveal whether the remote representation is a tree, page corpus, embeddings, trace store or mixed state. Server-side storage form, provenance, update control, expiry and semantic curation remain uninspected because server implementation is unavailable. Local cached MCP sessions/catalogs are access/instruction state, not demonstrated durable learned memory. Remote instructions arrive via a policy channel, whereas retrieved tool content arrives as evidence. The cited runtime record supplies client wiring and minimum passages (SRC-1: `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`, `pageindex/agent_tools.py`).

#### On [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook)

The selector consumes the retained/fetched outline without text and question; selected node IDs are symbolic access metadata. Notebook code maps spans to PDF page images, then delivers those images to a separate answer call. Selection reasoning is not automatically passed to the answer frame. Page images are source representations, distinct from the local store's extracted strings and not evidence of a parametric update. Files/variables may survive for caller reuse; a cross-session history store or cleanup policy is not established by the supplied cells. Source-only pipeline wiring and minimum passages are supplied by runtime (SRC-1: `cookbook/pageindex-vision-rag.ipynb`).

## Write side

Managed local admission starts with caller-selected PDF content and serializable optional metadata. Code validates input, extracts pages, builds/refines the tree, checks result acceptability and spans, assigns identity and saves. Caller initiation and filesystem authority are not per-content human approval. Source text and generated descriptions share no independent semantic truth gate. Flash/classic checks are route-specific: a direct builder can return a result refused by managed submission. The minimum supporting passages and controls are in [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders).

Known derivations are PDF → [MEM-OBJ-pages](#mem-obj-pages), document structure/text → [MEM-OBJ-tree](#mem-obj-tree), and selected tree descriptions → [MEM-OBJ-doc](#mem-obj-doc). Flash parent summaries consume derived child summaries, so later consumers can receive twice-transformed content rather than complete source text. A concise-coverage prompt requests completeness; it cannot establish it. Short leaves may bypass generation by retaining raw text, and failed nodes can receive fallbacks. This alternative prevents equating every `summary` field with model-authored abstraction. No independently verified capacity improvement follows from retaining these products.

The optimizer's optional cache is a separate admission path with unresolved initial provenance and known downstream filtering/selection. Cached and model proposals share cost admission but do not share all source-text checks. Optional decision logs retain some structural reasons; normal retrieved trees do not necessarily include those reasons, and no later answer route reading the log is established. See [MEM-OBJ-headings-cache](#mem-obj-headings-cache) and the refinement annotation.

Maintenance is structural rather than semantic: marker withdrawal, directory cleanup and manifest repair affect availability, not correction of a mistaken passage. [MEM-RTE-store-maintenance](#mem-rte-store-maintenance) traces the later-consumer effect and the non-revocation of already copied content. No automatic update from chat success/failure into a changed durable document, prompt or model parameter is established by the inspected write paths; this is a scoped limit, not a repository-wide evidenced absence.

## Read-back

The ordinary chain is request-led: question → model chooses tool → code resolves document and selects response portion → retained metadata/outline/pages delivered as tool evidence → model chooses next step. Local discovery is paged/time-sorted rather than semantic search. The automatic selection inside a requested response is not an unsolicited push. Outline summaries help a model target page ranges; page indexes alone are addresses, not relevance judgments. [MEM-RTE-document-readback](#mem-rte-document-readback) records exact selectors, budgets and delivery limits.

Direct getters expose full or reconstructed representations without proving a consumer. The shipped chat drivers and framework tool callbacks establish consumer wiring/affordance; the vision notebook supplies a distinct explicit outline-to-image-to-answer chain. See [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools), [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook). Locally, scope checks restrict built-in tool lookups under the managed driver, not every SDK/host capability. Cloud own-model targeting is textual rather than the same structural allowlist.

Working-context controls exclude text from outlines, paginate/slice evidence, isolate summary/expansion/vision calls and let callers reintroduce earlier tool history by value. Omitted pages remain stored and reloadable; discarded call frames leave returned products, not a model-window pointer that dereferences itself. There is no established automatic eviction or summary of accumulated chat turns in the supplied drivers. Provider prefix-cache annotations do not change that finding. Actual later history reuse, model compliance and answer dependence remain unobserved.

## Integration issues

1. **Qualification to supplied admission claim.** [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) describes rejection of unprinted headings broadly. In SRC-1 `pageindex/tree_optimize.py`, the explicit substring test is in `propose_children`; `children_from_cache` reaches `own_children` without that test, and absent printed matches alone do not reject. [MEM-OBJ-headings-cache](#mem-obj-headings-cache) retains the countercase and minimum passages. Consequence: limit the printed-heading guarantee to model proposals; do not infer all optimizer inputs share it. No actual bad cache or operational failure is claimed.
2. **No duplicate declarations proposed.** New objects are retained products/inputs, whereas the nearest supplied records are producer/consumer routes. The cache is explicitly a part of refinement; the read-back route spans managed and framework consumers rather than replacing either. Maintenance is distinct from capability registration and submission. Annotations retain the supplied IDs instead of redeclaring their referents.
3. **Cache origin unresolved.** [MEM-OBJ-headings-cache](#mem-obj-headings-cache) has known file loading and admission but unspecified initial author/detection process. This prevents assigning a human/model or trace-origin classification to the input; it does not prevent describing later software transformation.
4. **Remote state unresolved.** [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools) affords remote read-back but leaves server storage, selection, update and expiry inaccessible. No local result is generalized to cloud internals.
5. **Evaluator coverage bounded.** Boundary inventories shipped tests/examples and benchmark illustrations; this report has not exhaustively read them. It cannot establish a complete evaluator inventory, QA effectiveness or evaluator-driven persistent update. Static optimizer diagnostics and classic verification are covered by [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders), not promoted to observed evaluation results.
6. **External histories and withdrawal.** [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history) delegates persistence/selection to callers. [MEM-RTE-store-maintenance](#mem-rte-store-maintenance) withdraws future store reads, not copied content. Actual history reuse and external retention policies are unknown; store deletion cannot be represented as universal forgetting.

## Limitations and checks

The source boundary and run identity were rechecked against supplied boundary/runtime and Git HEAD; no evidence source was added. Evidence is implementation plus supplied source-grounded findings, with no execution or causal experiment. Deep extraction heuristics, all evaluator bodies, example bytes and remote/dependency implementations are not independently established here. Source access and line reading do not establish semantic correctness, model compliance, secure erasure or benefit. Learning and self-improvement are not inferred from persistence or proxy-cost reduction.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check is run before return; its successful result checks form, identity, references and quotation occurrence, not analytical acceptance.
