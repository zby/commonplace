---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Stigmergy memory: evidence retention, layered wiki synthesis, source-preserving revision, alias admission and scoped read-back."
run-id: AAS-2026-11-08-stigmergy-2de42cc04367-01
source-identity: https://github.com/sturlese/stigmergy
reviewed-boundary: "0ca8bb1963ad9cf43eaf2c18329998023a9caa4f"
---

# Stigmergy memory report

## Boundary and evidence

Stigmergy retains submitted team material, compiles linked knowledge pages, and supplies those pages to later filing and reader invocations. The frozen boundary is SRC-1 at `0ca8bb1963ad9cf43eaf2c18329998023a9caa4f`, as registered in [boundary](boundary.md#source-register). This report includes original artifacts, readable extraction, source pages, derived pages and their control metadata, contradictions, aliases, index fragments/vectors, change evidence, repair, recompile, replay, withdrawal and the shipped reader surfaces. It excludes provider internals and external hosts' own conversational memory. No tenant corpus or executed target trace was supplied. Source inspection establishes wiring, not actual reuse, reliability or improved performance.

The supplied runtime is provisional evidence for routes explicitly cited below. Direct reads added here concern SRC-1 implementation in capture evidence/extraction/source rendering; knowledge context/pages/sources/contradictions/aliases and selected writer branches; change storage; index fragmentation/search; server service shaping; admin wiki; Slack context/show-it-here; replay and erasure. The packaged librarian skill and evaluation README provide doctrine/design, not proof of compliance or successful evaluations. CLI declarations and bridge registration were checked against the runtime inventory. No target code, tests or providers were executed.

| Entry or operation | Source path(s), SRC-1 | Coverage and conclusion limit |
|---|---|---|
| Console dispatch and bridge registration | `pyproject.toml`, `src/stigmergy/bridge/server.py` | Direct declarations/search: index, server, bridge, librarian, boot, credential, Slack, admin; bridge exposes search/read/list/describe/ask/submit/status/delete, not a second knowledge store. Main runtime account supplies dispatcher tracing. |
| MCP, upload and Slack admission | `src/stigmergy/server/mcp_server.py`, `src/stigmergy/server/service.py`, `src/stigmergy/slack/capture.py` | Supplied [RT-RTE-layer-routing](runtime.md#rt-rte-layer-routing), [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing); direct writer membership recheck and extraction entry. Parser internals and all adapter provenance branches not exhaustively inspected. Human authorship of every submitted artifact is not established. |
| Original bytes, readable derivatives, source archive | `src/stigmergy/capture/evidence.py`, `src/stigmergy/capture/extraction.py`, `src/stigmergy/capture/source.py`, `src/stigmergy/knowledge/sources.py` | Direct: [MEM-OBJ-artifact](#mem-obj-artifact), [MEM-OBJ-source](#mem-obj-source). Extraction dispatch inspected; full media-specific parsers/OCR prompts remain uninspected, preventing a fidelity guarantee. |
| Filing selection, projection and gates | `src/stigmergy/knowledge/context.py`, `src/stigmergy/knowledge/writer.py`, `src/stigmergy/knowledge/layered.py` | Context and selected writer branches direct; projection implementation supplied by runtime. [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), annotations below. |
| Page bodies, headers, contradictions | `src/stigmergy/knowledge/pages.py`, `src/stigmergy/knowledge/contradictions.py`, `src/stigmergy/knowledge/writer.py` | Direct: [MEM-OBJ-knowledge-body](#mem-obj-knowledge-body), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-contradiction-data](#mem-obj-contradiction-data), [MEM-OBJ-contradiction-display](#mem-obj-contradiction-display). |
| Garden repair, aliases, recompile | `src/stigmergy/knowledge/writer.py`, `src/stigmergy/knowledge/aliases.py` | Direct selected repair/alias/recompile branches plus supplied [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission); [MEM-RTE-alias-recording](#mem-rte-alias-recording). Full entity merge implementation and all tombstone rules remain uninspected. |
| Index build, push hook, embeddings and search | `src/stigmergy/index/fragments.py`, `src/stigmergy/index/search.py`, `src/stigmergy/index/build.py`, `src/stigmergy/server/webhook.py` | Fragment/search direct; builder/hook from [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence). [MEM-OBJ-fragment](#mem-obj-fragment), [MEM-OBJ-fragment-vector](#mem-obj-fragment-vector). No observed convergence. |
| Search/read/list/describe and question answering | `src/stigmergy/server/service.py`, `src/stigmergy/answer/service.py`, `src/stigmergy/answer/synthesize.py` | Reader shaping direct; answer trajectory supplied by [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer). [MEM-RTE-scoped-reading](#mem-rte-scoped-reading). Detailed listing pagination and entity timelines not fully read; no exhaustive enumeration guarantee inferred. |
| Backoffice and Slack excerpt readers | `src/stigmergy/admin/wiki.py`, `src/stigmergy/server/service.py`, `src/stigmergy/slack/context.py`, `src/stigmergy/slack/show_it_here.py` | Direct reader implementations; frontend invocation details remain supplied boundary inventory, not direct UI audit. [MEM-RTE-scoped-reading](#mem-rte-scoped-reading). |
| Change records and crash recovery | `src/stigmergy/changes/model.py`, `src/stigmergy/changes/store.py`, `src/stigmergy/knowledge/writer.py` | Direct: [MEM-OBJ-knowledge-changes](#mem-obj-knowledge-changes), maintenance annotation. UI patch authorization and patch decompression not fully inspected; no arbitrary-reader patch access asserted. |
| Delete and entity maintenance | `src/stigmergy/knowledge/writer.py` | Direct `_delete`, `_entity`, reference sweeping; [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) annotation. Master-gated explicit merge/rename/delete is an alternative to model-authored content, not per-plan approval. |
| Layer/workspace erasure and reset | `src/stigmergy/ops/erase_layer.py`, `src/stigmergy/ops/erase_workspace.py`, `src/stigmergy/ops/erasure.py`, `src/stigmergy/ops/reset.py` | Direct purge/workspace run and bounded function search; rewrite/rebuild outline also supplied runtime. Reset implementation only inventoried: exact provider cleanup remains uninspected. Prevents all-copies deletion or complete reset claims. |
| Workspace replay/handover | `src/stigmergy/ops/replay_workspace.py` | Direct export/import/handover: [MEM-RTE-workspace-replay](#mem-rte-workspace-replay). Source-to-target re-filing, not vector copying. |
| Evaluation and development feedback | `evals/README.md` | Direct attributed evaluator contract; [RT-RTE-product-admission](runtime.md#rt-rte-product-admission) supplies release procedure. Evaluation report/history/spend artifacts are retained research/operational evidence; no production automatic feedback route established here. Individual runners and their gate implementations remain uninspected in this member. |
| Queue, audit, job reports, graph measures, roster/session state | `src/stigmergy/server/service.py`, `src/stigmergy/knowledge/writer.py`, `src/stigmergy/ops/erase_layer.py`, `src/stigmergy/ops/replay_workspace.py` | Direct call sites/purge queries establish these state surfaces, not complete schemas. Queue operation markers support recovery; roster is re-read for authority; graph measures are counts. Full report/audit consumption and initial roster administration remain uninspected. Prevents treating all logs as learned knowledge or claiming complete trace-fed update coverage. |

## Core ideas

1. **The archive and synthesis have different lifecycles.** Raw artifacts and extracted source pages retain the evidence basis; the wiki is a mutable compilation. Capture update gates preserve existing cited prose, but explicit deletion, recompile and history erasure are counterexamples to globally append-only knowledge. See [MEM-OBJ-source](#mem-obj-source), [MEM-OBJ-knowledge-body](#mem-obj-knowledge-body) and the maintenance annotation.
2. **Memory crosses invocations through selected content, not a persistent chat.** Later filing receives a bounded catalog, candidates and source evidence; a question receives scoped search and tool results. A fresh question ledger is not conversation memory. The source is consulted alongside existing derived claims rather than merely appended to chat. See [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context), [MEM-RTE-scoped-reading](#mem-rte-scoped-reading).
3. **Symbolic controls and natural-language authority coexist.** ACLs, page identity and alias resolution are code-consumed metadata; bodies and contradiction explanations are model/human-interpreted evidence. The supplied trust instruction does not make malicious corpus text inert by itself. See [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data).
4. **Automatic curation is not demonstrated learning.** Filing, alias extraction and garden repair change what future consumers can find. This establishes durable behavior-shaping material, not improved future capacity or successful epistemic correction. [MEM-RTE-alias-recording](#mem-rte-alias-recording) traces a narrow derived-content-to-metadata update; no weight training is implied.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-artifact
Label: Original and readable artifact objects

Source-native identity: original ArtifactRef bytes and ExtractedArtifact readable objects. Substrate: private content-addressed evidence store; `S3EvidenceStore` implements remote storage, while `MemoryEvidenceStore` is an exposed in-process alternative, not durable by itself. Originals can be text, documents, images or Slack material. Text carries natural-language evidence; image/document bytes are opaque at storage and become readable through parsers/OCR. Opaque bytes are not automatically a symbolic knowledge representation. Readable text is a derived natural-language representation; digest, media, byte count and extractor metadata are symbolic lineage, not a readable substitute for originals.

Acquisition is caller-supplied, with local bridge/cloud/Slack alternatives in [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing). Actual author, truth and any prior model origin of submitted material are unresolved per capture; adapter identity does not prove human origin. Software validates admissibility and extraction limits, not semantic truth. The writer records extraction metadata before planning; source rendering copies readable content and provenance into [MEM-OBJ-source](#mem-obj-source). The filing and later reading consumers principally see that text, not the original binary. Distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan): these are proposal inputs, not plan output. SRC-1, `src/stigmergy/capture/evidence.py`, `src/stigmergy/capture/extraction.py`, `src/stigmergy/knowledge/writer.py`.

> class ExtractedArtifact:
>     original: schema.ArtifactRef
>     readable_ref: str
>     readable_sha256: str
>     readable_bytes: int
>     result: ExtractionResult
> --- `src/stigmergy/capture/extraction.py`

> queue.record_extraction(conn, item["id"], {"artifacts": [a.metadata() for a in extracted]})
> --- `src/stigmergy/knowledge/writer.py`

#### MEM-OBJ-source
Label: Immutable readable source page

Source-native identity: `sources/YYYY/MM/<capture-id>.md`, physically under the selected layer where restricted. Substrate: Markdown/YAML files in tenant Git history, plus referenced original/readable evidence objects. Body: natural-language extracted evidence and framing, not necessarily a verbatim transcription of the original medium. Header: symbolic provenance including submitter, times, ACL, origin, acquisition, participants, original/readable hashes, extractor/version/OCR pages and optional resolution intent. These access/provenance fields are separate from content validity. Parser checks source path, ID, heading and metadata shape.

Lineage: capture envelope plus extracted artifacts; no claim that every source originates as an agent execution trace. Later consumers: filing source-evidence selection, recompile, indexed reader operations and answering. Ordinary writer paths prevent source mutation, but master delete and layer/workspace erasure can withdraw it. A source-only publication is possible after rejected synthesis. Distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan): retained evidence survives even when the plan does not. SRC-1, `src/stigmergy/capture/source.py`, `src/stigmergy/knowledge/sources.py`; publication limits: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing).

> body.append(item.result.text)
> --- `src/stigmergy/capture/source.py`

> "readable_sha256": item.readable_sha256,
> "extractor": item.result.extractor,
> "extractor_version": item.result.extractor_version,
> "ocr_pages": list(item.result.ocr_pages),
> --- `src/stigmergy/capture/source.py`

#### MEM-OBJ-knowledge-body
Label: Derived knowledge page body

Source-native identity: bodies of note, concept, entity and project pages under `wiki/notes`, `wiki/concepts`, `wiki/entities`, `wiki/projects`, including restricted projections. Substrate: Markdown in Git, copied into the reader index. Form: natural-language claims, timelines, explanations and relationships interpreted by later model/human readers. Wikilinks also yield symbolic graph edges. This is a persisted output of [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan), not the transient proposal itself. Distinct identity: admitted body versus planned mutation.

Lineage: source text and selected existing graph, model proposal, code mutation and projection. Normal update preserves cited blocks and local attributions; it can add new dated state instead of overwriting old claims. This favors evidence retention, not necessarily an error-free current-state interpretation. Capture delete can remove duplicates subject to gates; explicit master operations and recompile offer different replacement/withdrawal controls. Later filing receives selected whole candidate bodies; read APIs and answers receive selected excerpts/fragments. Actual consumer authority is evidence interpreted by the model, bounded by mutation and answer checks, not executable instructions. SRC-1, `src/stigmergy/knowledge/pages.py`, `src/stigmergy/knowledge/writer.py`; [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data).

> lost = _lost_source_backed_lines(page.body, body)
> if lost:
>     raise ExistingSourceBlockNotPreserved(target_path, lost)
> missing_attributions = source_attributions(page.body) - source_attributions(body)
> if missing_attributions:
>     raise KnowledgeWriteError("planned update drops existing local source attribution")
> --- `src/stigmergy/knowledge/writer.py`

#### MEM-OBJ-page-metadata
Label: Knowledge page metadata

Source-native identity: page YAML ID, type, title, editorial status, dates, ACL, sources, entity type and aliases. Substrate: same Git files as [MEM-OBJ-knowledge-body](#mem-obj-knowledge-body) and corresponding indexed fields. Distinct operative part: fixed code rules interpret metadata for identity, authorization, graph/source linkage, name matching and filtering; prose body quality does not certify these fields. Status vocabulary is editorial (`seed`, `developing`, `mature`, `evergreen`), not demonstrated epistemic warrant.

Lineage: render code mints identity and copies source/ACL; proposal can supply supported create metadata/status and aliases, but update is path-addressed and cannot rename/retype via create fields. Alias classifier and explicit entity operations are additional authors. No universal human per-content approval: source caller can choose input/layer, model/code admit resulting fields, master authorizes explicit operations. Future filing matches entity/project names; service search expands entity names/aliases and applies access metadata. Distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan): this is accepted persisted control state. SRC-1, `src/stigmergy/knowledge/pages.py`, `src/stigmergy/knowledge/writer.py`, `src/stigmergy/server/service.py`.

> # An update is path-addressed. Model-supplied create metadata cannot rename or retype it.
> --- `src/stigmergy/knowledge/writer.py`

> STATUSES = ("seed", "developing", "mature", "evergreen")
> --- `src/stigmergy/knowledge/pages.py`

#### MEM-OBJ-contradiction-data
Label: Contradiction structured payload

Source-native identity: canonical HTML-comment payload keyed by `con_<uuid>` in a knowledge body. Substrate: Git Markdown, URL-safe base64 encoding of JSON. Form: symbolic envelope with natural-language claim/explanation values. Encoding is inspectable, not an opaque provider memory. Code validates ID/status and exact canonical render; this controls preservation and removal, not which claim is true. Model-proposed conflicts must cite the current source or supplied source evidence. Normal page mutation cannot rewrite existing claims; missing records are reappended. Resolution requires an explicitly named contradiction, master permission and an accepted update of every affected candidate page.

Distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan): proposal becomes a retained canonical record. Later filing parses it into `filed_contradictions`, preserving explanation and claim/source data; downstream readers instead receive rendered warnings as described next. Reasons are available to later filing; that does not demonstrate criticism occurred or changed reliance. SRC-1, `src/stigmergy/knowledge/contradictions.py`, `src/stigmergy/knowledge/context.py`, `src/stigmergy/knowledge/writer.py`.

> record = _decode(match.group("data"))
> if record.contradiction_id != match.group("id"):
>     raise ContradictionContractError("contradiction ids do not match")
> block = match.group(0)
> if block != render(record):
>     raise ContradictionContractError("contradiction block is not canonical")
> --- `src/stigmergy/knowledge/contradictions.py`

#### MEM-OBJ-contradiction-display
Label: Visible contradiction warning

Source-native identity: rendered warning, explanation and claims/sources generated with the canonical payload. Substrate: same Markdown body and its index/read display. Natural-language form interpreted by model/human readers; source/date references provide symbolic addressing. Distinct from [MEM-OBJ-contradiction-data](#mem-obj-contradiction-data): readable warning versus serialization used for validation, preservation and named resolution. There is no supplied runtime object counterpart; [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) is upstream. Truncation may omit the warning on an initial page-head read; it is not guaranteed every later answer receives every conflict. SRC-1, `src/stigmergy/knowledge/contradictions.py`, `src/stigmergy/server/service.py`.

> f"> [!WARNING] Unresolved contradiction `{record.contradiction_id}`",
> f"> {_one_line(record.explanation)}",
> --- `src/stigmergy/knowledge/contradictions.py`

#### MEM-OBJ-fragment
Label: Indexed page fragments

Source-native identity: Fragment ordinal, start/end offsets, heading trail and text. Substrate: fragment objects during build, stored index fragments for later scoped reads/search. Text is natural-language material sliced from source/wiki bodies, not a semantic summary; offsets/ordinal/trail and page binding support fixed retrieval rules. Lineage: deterministic heading/length splitting with overlapping windows; short pages remain whole. Distinct from [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context): persistent retrieval substrate versus fresh question ledger. Producer/consumer wiring is [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence); exact index storage schema is supplied runtime evidence, not a direct schema audit here. SRC-1, `src/stigmergy/index/fragments.py`, `src/stigmergy/index/search.py`.

> return [Fragment(index, start, end, trail, body[start:end]) for index, (start, end, trail) in enumerate(spans)]
> --- `src/stigmergy/index/fragments.py`

#### MEM-OBJ-fragment-vector
Label: Fragment embedding vectors

Source-native identity: stored dense fragment embeddings generated from page title, heading trail and fragment text; not a readable claim set. Substrate: Postgres/pgvector index as traced in [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence). Form: distributed numerical representation; symbolic model/host/content keys govern compatibility/cache reuse. Lineage is derived from readable content, not model weight updates. Query embeddings compare against these representations to rank retained fragments; snippets and explicit fragment references then expose text. Distinct from [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model): output vectors versus provider parameters. No supplied runtime object duplicates the stored vectors. SRC-1, `src/stigmergy/index/fragments.py`, `src/stigmergy/index/search.py`; remote fixity and version limits remain in that component record.

> def embed_text(title: str, fragment: Fragment) -> str:
>     """The text a fragment is embedded as: its page title, its heading trail, and its words."""
>     head = f"{title[:TITLE_CHARS]} › {fragment.trail}" if fragment.trail else title[:TITLE_CHARS]
>     return f"{head}\n{fragment.text}"
> --- `src/stigmergy/index/fragments.py`

#### MEM-OBJ-knowledge-changes
Label: Change manifest and exact patch evidence

Source-native identity: ChangeRecord and referenced compressed exact patch. Substrate: tenant Postgres `knowledge_changes` rows; compressed patch in evidence store; corresponding Git commit/history. Manifest is symbolic path/action/hash/count/contradiction metadata with natural-language reasons; patch contains exact changes, not just display summary. Hash/byte/reference metadata is not the patch payload. These parts support audit and recovery rather than becoming filing context automatically. Reasons supplied at commit can survive in manifests; crash recovery may substitute a generic recovery summary when rebuilding missing bookkeeping. A reason's retention does not establish later model consumption of that reason.

Distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan): evidence of admitted effects, not proposal. [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) supplies publication context. Recovery calls `get_change_by_commit`, avoiding fresh plan generation when operation commit exists, although extraction can run again to restore references. Layer erasure can drop/rewrite ledger entries and old patch references, so “append-only” in the module description is an ordinary-path property. SRC-1, `src/stigmergy/changes/model.py`, `src/stigmergy/changes/store.py`, `src/stigmergy/knowledge/writer.py`, `src/stigmergy/ops/erase_layer.py`.

> patch = diff.exact_patch(repo, parent_commit_sha, commit_sha)
> compressed = diff.compressed_patch(patch)
> patch_ref = evidence.put(compressed)
> --- `src/stigmergy/changes/store.py`

### Routes

#### MEM-RTE-alias-recording
Label: Link variant to retained alias

A new `[[Entity|variant]]` link or a scheduled garden scan supplies candidates to the typed classifier. Candidate selection compares links before/after the write, rejects already-owned/ambiguous names and enforces eligibility. `llm.choose` receives entity title/type/summary/aliases, candidate text and surrounding sentence. Code applies a probability threshold of 0.75 and guarded metadata write, then writer gates/project/commit admit the result. Software can reject/skip; no human approval of each alias is required. Mode: ongoing captures and bounded scheduled maintenance, not a supervised training curriculum; model judgment is not an expected-answer oracle. Proposal guidance distinguishes aliases from descriptions/roles/products. Parameters are not updated by this route.

Distinct part of the broader maintenance/filling account: neither supplied route separately identifies the typed alias admission operation. This route spans [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) and [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission); it is not wholly contained in exactly one.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-candidate accepted/rejected/skipped probability report and changed-page originals for recovery.
- Later read-back: persisted entity aliases enter later name matching, query expansion and catalog candidate selection.
- Delegated visibility: classifier receives the entity summary and candidate sentence, not the complete corpus or process credentials.
- Selection predicate: eligible new variant links, normalized name ownership checks, rotating candidate offset; default record cap eight and ten-second window, with garden caller-specific limits.
- Invalidation or expiry: failures/time/candidate caps skip candidates; failed metadata writes restore prior text; outer writer gates can prevent publication. Accepted alias has no TTL in inspected metadata.
- Activation or effect: alias changes name resolution inputs for future invocations; actual improved retrieval or classifier correctness is unobserved.
- Evidence limits: source-origin may be mixed human/agent material; the immediate automatic input is derived wiki link text, not evidence of learning from an evaluated agent trace.

SRC-1, `src/stigmergy/knowledge/aliases.py`, `src/stigmergy/knowledge/writer.py`, `src/stigmergy/server/service.py`, `src/stigmergy/knowledge/context.py`.

> decision = "accepted" if probability >= THRESHOLD else "rejected"
> report.append({**entry, "decision": decision, "probability": round(probability, 4)})
> if decision == "accepted":
>     accepted.append(candidate)
> --- `src/stigmergy/knowledge/aliases.py`

#### MEM-RTE-scoped-reading
Label: Requested retained knowledge delivery

Endpoints: reader/host request to scoped BrainService index operations, then tool JSON or human display. Search combines lexical, vector, entity-intersection and graph-neighbor arms before final ranking. Model-directed answering uses those services, but direct callers can independently search, read, batch-read, list or describe an entity. Backoffice WikiService calls the same service for pages/graph/search; Slack's button re-resolves its owner and reads a cited page. Selection is request-driven, not an independent push memory daemon. Code owns scoping/shaping; external agent/human chooses what to do with returned evidence. No per-read knowledge change is admitted and no expected-answer oracle participates.

Distinct from [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer): these are also exposed non-answer products, without its verifier. Overlap in underlying retrieval is deliberate, not identity of the returned product. [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) produces the backing state.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked hits/snippets, bounded page bodies plus navigation, listing/entity projections, or sanitized rendered human view.
- Later read-back: material accumulated through earlier captures/maintenance is selected from the index for a later request; answer synthesis consumes it through tools; external host reuse after receipt remains uninspected.
- Delegated visibility: tenant/audience-scoped fused text; models see fenced untrusted bodies, humans receive sanitized Markdown/HTML or Slack excerpts.
- Selection predicate: question/query and optional filters/entity hints, explicit page or fragment address, listing constraints or cited-page click; backend scopes before presenting/fusing visible rows.
- Invalidation or expiry: index convergence/rebuild replaces retrieval state; deleted content disappears after corresponding index update. Slack page token expires after 3600 seconds or capacity eviction and rechecks clicker identity; page content itself is re-read rather than embedded in token.
- Activation or effect: delivery of retained evidence and symbolic navigation references is wired; user/model reliance is not observed and raw API output has no answer-verification guarantee.
- Evidence limits: direct index library functions do not establish a consumer absent a caller; this route is supported by service/UI/Slack callers, not inferred just from storage APIs. Detailed listing and frontend branches are not fully inspected.

Budgets: default search returns five hits; page head is 6000 characters, batch read up to five, navigation capped at twenty. A fragment request returns center plus up to one neighbor each side within the body budget. Page heads include fragment reload instructions. Backoffice body cap is 200000 characters; Slack excerpt cap is 2800, so neither is equivalent to an uncapped full source. SRC-1, `src/stigmergy/server/service.py`, `src/stigmergy/index/search.py`, `src/stigmergy/admin/wiki.py`, `src/stigmergy/slack/show_it_here.py`, `src/stigmergy/slack/context.py`.

> page["excerpt_note"] = (f"This body is the first {PAGE_EXCERPT} characters of a longer page; read "
>                         f"`{page['path']}#<n>` for fragment n of {total}, e.g. `{page['path']}#2`.")
> --- `src/stigmergy/server/service.py`

> lambda service: service.read_page(path),
> --- `src/stigmergy/slack/show_it_here.py`

#### MEM-RTE-workspace-replay
Label: Landed capture replay into fresh workspace

The operator exports layers/people and eligible landed capture requests, imports into a different fresh active workspace, and queues new envelopes with deterministic target-specific IDs/idempotency keys. It rebuilds through the ordinary writer rather than transporting already-derived wiki content. Source export refuses an outstanding capture queue and Slack-linked source; deleted-source captures are excluded. Explicit source:target confirmation and operator selection control replay admission, but they do not approve each future model-authored page. Handover is a separate symbolic session/token move after target readiness checks, with an explicit unlanded-count override. There is no semantic answer oracle or automated improvement objective. Distinct from [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission): cross-workspace re-enqueue/handover versus in-place maintenance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: exported workspace/capture data, queued/already-queued counts and optional handover receipt.
- Later read-back: target writer consumes replayed envelopes and retained artifact references; later readers use newly compiled target wiki/index. Handover directs live shared users' sessions/tokens there and suspends source.
- Delegated visibility: copied principals/groups and capture envelopes; downstream filing retains ordinary scoped views, not arbitrary source tenant state.
- Selection predicate: landed captures with no non-live artifact reference, enabled principals; import order must include every exported capture exactly once.
- Invalidation or expiry: nonfresh/same/inactive target or mismatched confirmation refuses; deterministic keys prevent duplicate enqueue; handover refuses outstanding target work or unexpected unlanded count. No automatic rollback of a performed import/handover is established.
- Activation or effect: re-enqueue and session routing are implemented, not evidence the target compilation is equivalent or better.
- Evidence limits: export/import bodies were inspected, not all CLI/operator authorization branches; external artifact availability and all live token behavior remain unobserved.

SRC-1, `src/stigmergy/ops/replay_workspace.py`.

> envelopes.append(envelope.model_copy(update={"capture_id": replay_id(target.id, original),
>                                              "idempotency_key": f"{_KEY_PREFIX}{original}"}))
> --- `src/stigmergy/ops/replay_workspace.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

Memory-specific admission: source caller supplies content, not approval of each generated page; software/model choose and gate the synthesis. Actual raw origin remains per-capture unresolved. The archival source is retained even on source-only fallback. Retained output is evidence-linked prose and metadata, not model parameter changes. Input need not be execution traces; a submitted execution report could be compiled by the same mechanism, but this does not establish an automatic trace-learning loop.

Direct context inspection refines the budget description. Named entities/projects plus up to twelve lexically overlapping candidates are selected, not semantic vector neighbors. Catalog summary is a code-derived first prose line, at most 160 characters, with citations/emphasis removed. Up to twelve cited sources are ranked by non-stopword lexical overlap, subject to 64-reference, 128-KiB-per-file, 2-MiB-total-read and 100000-body-byte limits. Thus citations and facts in the retained page can be absent from catalog summaries; source provenance is not fully reproduced there. SRC-1, `src/stigmergy/knowledge/context.py`.

> MAX_CONTEXT_SOURCE_EVIDENCE = 12
> MAX_CONTEXT_SOURCE_BYTES = 100_000
> MAX_CONTEXT_SOURCE_REFERENCES = 64
> MAX_CONTEXT_SOURCE_FILE_BYTES = 128 * 1024
> MAX_CONTEXT_SOURCE_READ_BYTES = 2 * 1024 * 1024
> --- `src/stigmergy/knowledge/context.py`

The 768-KiB test during trimming measures compact JSON, while `render_context` emits indented JSON and rechecks. Therefore the nominal cap is not a guarantee every selected context successfully renders: whitespace overhead can cause rejection after selection. This qualifies the runtime's safe budget description, not the existence of its trimming mechanism.

> rendered = json.dumps(context, ensure_ascii=False, sort_keys=True, indent=2)
> if len(rendered.encode("utf-8")) > MAX_PLANNER_CONTEXT_BYTES:
>     raise ValueError("filing context exceeds its byte limit")
> --- `src/stigmergy/knowledge/context.py`

> return len(json.dumps(context, ensure_ascii=False, sort_keys=True).encode("utf-8"))
> --- `src/stigmergy/knowledge/context.py`

Working-context control: whole selected objects are popped, not summarized in-place. Omitted repository material remains stored, but planner has no dereference tool in that invocation. Separate temporary view/worktree isolates nonselected layers and discarded proposals; projected durable outputs are the deliberate escape from that frame. A later filing can select different pages; that is read-back across invocations, not a live reference inside the old model window.

#### On [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

Direct reads show distinct retained outcomes and veto points. Garden repair only projects a clean layer; remaining violations return no stored repair. Garden aliases are a separate classifier-based metadata update, with rotating candidates. Recompile preflights all source pages, clears derived pages except broader-layer keep paths, then reconstructs source by source with relevant prior-page hints. A failed source/revision aborts the temporary compilation; it is not the capture path's source-only fallback. Recompile retains original evidence and can preserve prior identities; it is not trace compaction or a summary checkpoint. SRC-1, `src/stigmergy/knowledge/writer.py`.

> if _introduced(check(view.root), tolerated):
>     # A repair that leaves the layer dirty stores nothing; the repository check reports it.
>     return requests, {}
> --- `src/stigmergy/knowledge/writer.py`

> safe_context["recompile"] = {
>     "prior_pages": [_recompile_prior_page_context(prior_pages[path]) for path in sorted(prior_pages)],
> }
> --- `src/stigmergy/knowledge/writer.py`

Explicit entity merge/rename/delete and page deletion require current master permission. The requester supplies paths, rationale and merge evidence where required; code transforms files and gates publication. Identity changes are not model-authored ordinary page updates. Source deletion removes cited units, contradiction records and source declarations; dangling wikilinks become plain text and empty pages may cascade-delete. Git history survives ordinary deletion, unlike history erasure. SRC-1, `src/stigmergy/knowledge/writer.py`.

> """Remove what pointed at deleted physical paths from every page that can no longer resolve it:
> wikilinks become plain text, and units, contradictions, and declarations citing a deleted
> source go. A page left with nothing but its heading is deleted in turn."""
> --- `src/stigmergy/knowledge/writer.py`

Layer purge also redacts queue requests/extractions/reports, job stats, audit arguments/results and admin arguments by layer/capture/name patterns; rewrites changes/commit references and drops affected graph-measure history. Workspace erase deletes the remote repository through an injected remover, tenant rows, indexes, unreferenced evidence and checkout; if evidence storage is absent it does not execute that evidence deletion block. This is managed-surface withdrawal, not proof of deletion from external caches/backups or earlier human/agent contexts. SRC-1, `src/stigmergy/ops/erase_layer.py`, `src/stigmergy/ops/erase_workspace.py`.

> if evidence is not None:
>     deleted = sum(1 for ref in _garbage(conn, item["id"])
>                   if not references.is_live(conn, ref) and evidence.delete(ref))
> --- `src/stigmergy/ops/erase_workspace.py`

Recovery reads operation-marked Git commits and existing change records before deciding to regenerate bookkeeping; capture recovery can rerun extraction and record references. A source's retained content, reference bookkeeping and summary are separate recovery products. Reasons retained in [MEM-OBJ-knowledge-changes](#mem-obj-knowledge-changes) are not shown as automatic future planner instructions.

#### On [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer)

Memory consumer authority remains evidentiary, not instruction authority. The model can request additional retained fragments/pages, whereas the filing planner cannot reload omitted context. Raw retrieval differs from verifier-bounded answer output. The supplied route establishes fresh question state, same-context correction and a separate evidence-only budget completion. It does not persist answers into shared knowledge, remove old turns through durable compaction, or establish later-question summary read-back. Any external host doing so lies outside the inspected boundary. This is working-context selection and bounded recovery, not a trained or evolving conversation memory. Evidence: that supplied route and [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context); direct SRC-1 reader budget/fragment implementation in `src/stigmergy/server/service.py`.

#### On [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data)

Persisted reasons have unequal exposure. Contradiction explanations and sourced page bodies can reach later filing or readers; generic mutation reasons reside in change manifests, with no demonstrated automatic model reader here. Catalog summaries strip local citation formatting. Alias metadata reaches a fixed name-resolution consumer, distinct from body interpretation. The packaged instruction's evidence rules request caution for OCR, correction/retraction and earlier/current state, but actual model compliance or improved future action was not observed. SRC-1, `src/stigmergy/knowledge/librarian_skill.md`, `src/stigmergy/knowledge/context.py`, `src/stigmergy/changes/store.py`.

> When the source corrects or retracts a fact that another visible page states, update that page
> too: add the correction beside the corrected line, and emit a contradiction when both cannot stand.
> --- `src/stigmergy/knowledge/librarian_skill.md`

## Write side

The acquisition-to-retention chain is [MEM-OBJ-artifact](#mem-obj-artifact) → [MEM-OBJ-source](#mem-obj-source) → [MEM-OBJ-knowledge-body](#mem-obj-knowledge-body) and [MEM-OBJ-page-metadata](#mem-obj-page-metadata), followed by [MEM-OBJ-fragment](#mem-obj-fragment) and [MEM-OBJ-fragment-vector](#mem-obj-fragment-vector). Source records preserve raw/readable lineage; derived pages preserve local source attributions. The source is rendered extracted evidence, not the original binary and not the planner's summary. Mixed/unknown authorship stays unknown rather than becoming “agent experience” merely by passing through a model.

Admission mechanisms differ from physical I/O. Explicit/default/classified layer choice governs capture access; the writer checks current membership, then proposes/gates pages without a mandatory human content approval. Rejected mutable synthesis can leave an archived source. Alias classifier threshold changes metadata; garden code vetoes unclean repairs; master authority gates recompile, named contradiction resolution and explicit destructive operations. Recompile failure abandons its temporary compilation. See supplied [RT-RTE-layer-routing](runtime.md#rt-rte-layer-routing), filing and maintenance annotations and [MEM-RTE-alias-recording](#mem-rte-alias-recording).

Raw operational traces include queue/extraction/model telemetry, job/audit records and evaluation history. They are not all derived memory. Concrete automatic transformations inspected here use captured evidence or derived wiki state: source compilation, link-to-alias admission and violation-to-repair. No supplied evidence establishes an autonomous production cycle using evaluation scores to replace prompts or model parameters. Evaluation README describes real-run history/report retention and a release gate; release machinery is the separately supplied [RT-RTE-product-admission](runtime.md#rt-rte-product-admission), not ordinary filing. Its claim of tests proving contracts is attributed design language, not this run's result. SRC-1, `evals/README.md`.

> Real runs append one row to `history.ndjson`. Fake backends exercise plumbing and append nothing.
> --- `evals/README.md`

Retention includes contradiction reasons and claim/source pairs; mutation reasons go to manifests, not automatically back into the filing prompt. Generic bookkeeping can be reconstructed after crash without preserving the original reason string. This bounds the claim that the system retains “why” its knowledge changed. Alternative checkpoint forms are source/archive, derived Git snapshots, indexed fragments/vectors and recovery ledgers, not a demonstrated conversational compactor's trace-to-summary memory. Their consumers and rollback/invalidation differ.

Withdrawal deliberately exceeds additive update rules: normal delete removes current files and reference-bearing units; history erasure rewrites repository/ledger state and purges managed evidence where unreferenced; index convergence controls when readers stop seeing old material. Complete deletion from provider or external reader copies remains unsupported. Replay can rederive knowledge in a different workspace from eligible retained captures, with explicit order and identity changes, so retained derivation need not be identical across compilations.

## Read-back

Two main consumer classes share the corpus but not the selector. Filing uses source-text lexical/name matching and bounded source-evidence expansion in a safe layer view. Answering starts with a code search, then the model requests tools under question budgets; direct readers bypass answer synthesis entirely. Both are request-rooted chains. Automatic context selection in filing is not an unsolicited background push: it runs because a capture/recompile invocation requests a plan. Source register and routes do not establish deployment exercise.

[MEM-RTE-scoped-reading](#mem-rte-scoped-reading) identifies the concrete read products: ranked/excerpted search, explicit page/fragment reads, list/entity projections, backoffice views and Slack cited-page display. Query/entity/layer constraints are actual selector inputs; an explicit page ID merely requests that file, not evidence of a relevance judgment. Vector ranking selects text references, not an interpretable numerical explanation. Source trust metadata and visible warnings can be omitted from a bounded excerpt; verification must operate on surfaced material, not an assumed whole corpus.

Working-context control is selection rather than ordinary turn accumulation: safe filing views exclude other layers; byte trimming drops whole objects with no in-call reload. Reader excerpts retain a fragment address for on-demand reload. Answer correction retains history; budget completion starts from gathered evidence, not a durable replacement session summary. In the frame analogy, isolation and disposal fit selected inputs plus returned results. It breaks for persistent corpus artifacts because their later reach depends on a new selector/request, not a reference remaining live in the old context. No Stigmergy-owned external-host compaction or subagent runtime is established by these routes.

## Integration issues

- **Budget qualification:** [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) describes a 768-KiB bounded context. Direct SRC-1 `src/stigmergy/knowledge/context.py` shows compact-size trimming and indented-size final checking; contexts can fail rendering after selection. Preserve a possible rejection rather than infer guaranteed delivery within budget. Its trimming precedence also retains one candidate while dropping excess evidence before removing that last candidate; “candidate tails first” must not imply all candidates precede all evidence in eviction.
- **Additional mechanisms, not duplicate records:** [MEM-RTE-alias-recording](#mem-rte-alias-recording) spans capture and scheduled maintenance with a distinct typed admission; [MEM-RTE-scoped-reading](#mem-rte-scoped-reading) overlaps answer retrieval but returns independent unverified products; [MEM-RTE-workspace-replay](#mem-rte-workspace-replay) adds cross-workspace reconstruction. Their overlap with [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) and [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) is not replacement identity.
- **New objects versus supplied proposal/context:** all declared retained objects are distinct from [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) and [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context). Contradiction serialization/display, page metadata/body and fragment text/vector are material operative parts with different consumers, not competing labels for one indivisible memory object. No possible duplicate requiring supersession identified.
- **Unresolved included surfaces:** full extraction/OCR parser fidelity, all entity merge and recompile tombstone branches, listing pagination, frontend rendering, evaluation gate implementation, reset cleanup, audit/report readers and initial roster administration were not completely inspected. Their source paths and prevented conclusions are retained in the coverage table. Existing positives remain valid; none implies exhaustive memory or erasure safety.
- **Evidence gap:** no live corpus, independent trace or causal intervention was supplied. Retention and read-back wiring support architectural memory capacity, not activation, improved capacity, successful correction, production isolation or all-copies erasure. Provider endpoint/weight provenance remains separately limited by the supplied runtime component records.

## Limitations and checks

The source HEAD was rechecked as `0ca8bb1963ad9cf43eaf2c18329998023a9caa4f`. Evidence and identity stayed within SRC-1; no new source, execution, delegation, publication or target mutation occurred. The method inputs were the complete invocation, memory job, worker rules, collection/type contracts, shared records contract and the supplied boundary/runtime versions. No prior analysis or style exemplar was consulted.

Deterministic validation: passed using the invocation's prepared `commonplace-validate` command with `--artifact` and `--role memory`. This checks form, relations and quotation occurrence, not semantic support, actual operation or acceptance. The substantive limitations above remain.
