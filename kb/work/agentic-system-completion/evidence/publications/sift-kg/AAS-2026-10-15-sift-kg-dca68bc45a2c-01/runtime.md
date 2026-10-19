---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "sift-kg runtime baseline: document extraction, graph production, review/application, narration and later agent-facing retrieval at the frozen commit."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
---

# sift-kg runtime report

## Runtime account

### Work and evidence

sift-kg converts documents into a saved entity/relation graph, offers a separate duplicate-resolution and review workflow, derives prose and visualization from saved state, and exposes graph neighborhoods and topology to a later caller. It is not the enclosing conversational agent. The caller chooses commands; Python owns stage progression; models interpret bounded inputs rather than choose arbitrary tools or the next workflow stage. The bundled agent skill requests persistent use of the graph, but the external host owns session scheduling and final answers. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`, `.agents/skills/sift-kg/SKILL.md`; [RT-RTE-graph-retrieval](#rt-rte-graph-retrieval).

All findings below are implementation or doctrine/design at the boundary's commit, not observed runs. No target code, tests, examples, providers or experiments were executed. Added SRC-1 inspection covers the model adapter; both extraction paths and prompts; discovery; reader, chunker and OCR adapters; graph builder, pre-deduplication, graph load/save and community/subgraph consumers; resolver, reviewer and surgery engine; narration's main flow, description and rewrite branches; export dispatch and viewer generation. These are additional paths under the existing source register, not new sources. Provider and dependency internals, deployed grants, actual extraction accuracy, host compliance and causal benefit remain unobserved.

### Ordinary invocation and ownership

A user or host-agent process invokes `sift extract ./documents/ -o output/`, then `sift build -o output/`, optionally resolves/reviews/applies merges, narrates and views the result, and later queries it. Packaging binds `sift` to the Typer application; `python -m sift_kg` imports the same application. SRC-1: `pyproject.toml`, `src/sift_kg/__main__.py`, `src/sift_kg/cli.py`.

1. CLI configuration combines flags, environment, `.env`, project YAML and defaults. It selects model, output location, domain and document/OCR backend and validates keys for recognized remote providers. The library functions instead accept explicit parameters and instantiate the adapter without the CLI's configuration/key checks. Credential availability is not authorization to spend a particular amount. SRC-1: `src/sift_kg/config.py`, `src/sift_kg/pipeline.py`.
2. Recursive, extension-filtered document discovery feeds a reader. Local text or OCR is converted to a plain string; chunking uses approximately 10,000 characters with 10% overlap and boundary adjustment. File stems become document identities and extraction filenames. Schema-free extraction can first persist a model-generated domain. A separate first-chunk summary supplies context to each chunk call. Async chunk tasks share a semaphore and model client, then Python gathers and deduplicates their results into per-document JSON. [RT-RTE-document-extraction](#rt-rte-document-extraction), [RT-RTE-schema-discovery](#rt-rte-schema-discovery).
3. Build reloads all extraction JSONs, constructs a new graph rather than incrementally editing the old saved graph, applies automatic normalization/deduplication, saves `graph_data.json`, detects communities and writes review flags. Review flags do not quarantine edges: the graph has already been saved. [RT-RTE-graph-build](#rt-rte-graph-build).
4. Resolution reloads the graph and proposes same-entity merges plus variant relationships. Review can automatically or interactively change statuses in YAML. A separate application command mutates the graph for confirmed merges and rejected relations. [RT-RTE-entity-resolution](#rt-rte-entity-resolution), [RT-RTE-review-application](#rt-rte-review-application).
5. Narration reads the graph and extraction contexts, requests prose/descriptions/labels and saves sidecars. Query/search/topology later reload graph or sidecar state and return selected JSON or text. Viewer/export are additional downstream consumers, not model approval stages. [RT-RTE-narrative-generation](#rt-rte-narrative-generation), [RT-RTE-graph-retrieval](#rt-rte-graph-retrieval), [RT-RTE-view-export](#rt-rte-view-export).

The library convenience driver stops at extract → build → optional narrate. It neither resolves nor reviews. Its `max_cost` is passed separately to extraction and a new narration client, not enforced as a shared pipeline account. SRC-1: `src/sift_kg/pipeline.py`.

> run_extract(doc_dir, model, domain, output_dir, max_cost=max_cost)
> run_build(output_dir, domain)
> --- `src/sift_kg/pipeline.py`

### Controls, guarantees and forcing cases

The capability surface is host Python file I/O, configured model calls, optional OCR services and browser opening. The effective grant set is whatever filesystem permissions, credentials and provider access the invoking process has; none is supplied as deployment evidence. This is not an inspected sandbox envelope. The adapter's sync/async requests carry model, messages, timeout and temperature, not tool declarations; it returns text and software parses selected fields. The bounded search for alternate executors is recorded in [RT-ABS-tool-execution](#rt-abs-tool-execution). External host shell access must not be attributed to the model adapter. SRC-1: `src/sift_kg/extract/llm_client.py`, `src/sift_kg/config.py`, `src/sift_kg/ingest/ocr.py`, `src/sift_kg/visualize.py`.

Four source-supported forcing cases constrain the ordinary-path account:

- **Approval is status-based, not universally human.** The README's approval claim is stronger than the mechanics. Default CLI review automatically confirms proposals whose minimum member confidence is at least 0.85; cross-type same-name proposals assign 0.95 in code. Build also automatically folds near-duplicate names before proposal review. Manual YAML editing and library application are materially equivalent application paths. Therefore only the confirmed-status gate is an implementation invariant for the surgery engine, not a guarantee of per-content human approval. [RT-CLM-merge-approval](#rt-clm-merge-approval), [RT-RTE-graph-build](#rt-rte-graph-build), [RT-RTE-review-application](#rt-rte-review-application).
- **A cost limit can be exceeded.** Discovery and document summaries run before the extraction chunk budget check. The check occurs before semaphore acquisition, so waiting tasks can pass it together and later spend beyond the threshold. Single-document/text extraction has no `max_cost` parameter. Narration checks only description admissions; overview, chains, timeline, naming and rewrites are outside that check. This is best-effort local accounting, not a provider spend cap or deployment guarantee. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/narrate/generator.py`, `src/sift_kg/pipeline.py`; [RT-RTE-document-extraction](#rt-rte-document-extraction).
- **An edited source need not invalidate its cache.** The cache test compares model string, domain name and chunk size, not source text, mtime or domain contents. Two recursive paths with the same stem target the same filename. `--force` is a recovery path, not automatic changed-document detection. An empty chunk result after exhausted model/parse failure can still enter a persisted document with no document-level error and be counted as successful by the CLI. [RT-RTE-document-extraction](#rt-rte-document-extraction). This qualifies the skill's changed-document claim without deciding downstream memory assessments.
- **Confirmed variants are not inserted by application.** Resolver emits DRAFT `EXTENDS` entries to relation review, but application only removes REJECTED edges and applies confirmed entity merges. It has no confirmed-relation insertion loop. Thus variant proposals do not by themselves establish new graph links. [RT-RTE-entity-resolution](#rt-rte-entity-resolution), [RT-RTE-review-application](#rt-rte-review-application).

Load-bearing guarantees and their coverage:

| Guarantee | Owner and enforcement | Strength and covered paths | Alternate paths and external contract |
|---|---|---|---|
| Only confirmed proposals enter entity surgery | `MergeFile.confirmed` filter, then `apply_merges` | invariant for that engine; CLI and library use it | Status can be written by threshold code, a human or another caller; build pre-dedup bypasses this stage. No authenticated approver contract. |
| Extraction spends only up to the requested budget | Extraction task admission check and usage tracking | best effort for bulk chunk scheduling, not a hard limit | Summary/discovery, queued tasks, direct extraction, narration subcalls and OCR fall outside full coverage; requires provider-reported/priced usage. |
| Extract only explicit supported relations | Natural-language extraction rules | policy request to the model | JSON parsing/Pydantic validate shape and confidence ranges, not source entailment, quotation identity or allowed type membership; build transformations can further change graph content. Requires model compliance for semantic fidelity. |
| Ask before paid extract/resolve | Bundled skill interpreted by host agent | protocol outside CLI enforcement | Direct CLI/library calls do not require an approval prompt; narration is also paid. Requires host-agent compliance and user interaction. |

For the confirmed-status guarantee: implementation conclusion status: wired. For the cost-check mechanism: implementation conclusion status: wired. For the extraction-rule request: implementation conclusion status: wired. For the host confirmation protocol: implementation conclusion status: claimed. For all four: operation conclusion status: uninspected. These statuses concern the scoped mechanisms, not proof that the broader desired outcomes hold. SRC-1: `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/engine.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/prompts.py`, `.agents/skills/sift-kg/SKILL.md`.

### Context, coordination and recovery

Working-context control is code-selected input, not a conversational compactor: chunk windows keep most document text out of each call; a first-chunk summary adds shared context; resolver limits identity fields and selects overlapping batches; narration selects top-degree entities and bounded relation/context payloads; graph retrieval restores a selected neighborhood on demand. Each model call starts with at most an optional system message and one user message, without earlier turns. The frame analogy fits independent call inputs and returned text; it does not imply sub-agents with identities or a persistent pointer-bearing model window. Durable extraction/schema/graph files, not prior model context, support later invocations. [RT-CMP-llm-client](#rt-cmp-llm-client), [RT-RTE-document-extraction](#rt-rte-document-extraction), [RT-RTE-entity-resolution](#rt-rte-entity-resolution), [RT-RTE-narrative-generation](#rt-rte-narrative-generation).

Async semaphores and `gather` coordinate work inside one process. Adapter retries handle rate limits, timeouts, empty responses and generic errors with finite counts and waits. Exhaustion either propagates or is caught by a stage, sometimes producing an empty result/fallback prose. Output files are written directly; inspected save/application bodies contain no multi-artifact transaction or undo log. Rebuilding from retained extractions reconstructs a graph but does not replay approved surgery automatically. Recovery of an exact prior graph therefore requires an external copy, while regeneration can recover a different graph. Concurrent writers and interrupted writes are not experimentally characterized. SRC-1: `src/sift_kg/extract/llm_client.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/resolve/io.py`.

The inspected change-admission surface is domain/configuration changes, discovered schema, extracted knowledge, deterministic graph changes, reviewed surgery and derived prose. Those admission paths are detailed below. Source/package changes remain ordinary maintainer changes; no product-writing model route was found in the bounded executor search. This does not characterize external hosts or development processes.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LLMClient and selected completion model

Source-native identity: `LLMClient`, using a caller/configured LiteLLM model string, defaulting in configuration to `openai/gpt-4o-mini`. Its Python adapter is symbolic code; the selected model is distributed-parametric content behind a provider/local endpoint. Numerical parameters reside outside sift-kg's stored artifacts. No inspected call trains or updates those parameters. Exact weights/version are not pinned by the default model name or package dependencies; configurable or mutable endpoints may resolve differently. Provider internals, hidden state and model identity at execution are uninspected. SRC-1: `src/sift_kg/extract/llm_client.py`, `src/sift_kg/config.py`, `pyproject.toml`.

> messages.append({"role": "user", "content": prompt})
> return messages
> --- `src/sift_kg/extract/llm_client.py`

> response = await litellm.acompletion(
>     model=self.model,
>     messages=messages,
>     timeout=self.timeout,
>     temperature=0.1,
> )
> --- `src/sift_kg/extract/llm_client.py`

#### RT-CMP-sem-hash
Label: SemHash pre-deduplication model dependency

Source-native identity: `SemHash.from_records` and `self_deduplicate`, described in the module as Model2Vec-based. This supplies distributed-parametric similarity behind symbolic name grouping and threshold selection. Storage, exact model version and provider/download resolution are dependency-internal and uninspected; sift-kg does not pass an immutable revision. No parameter update is requested by the inspected adapter. Mutable dependency/model resolution cannot be ruled out. Selected duplicate mappings, not weights, affect the built graph. SRC-1: `src/sift_kg/graph/prededup.py`, `pyproject.toml`.

> sh = SemHash.from_records(records=records, columns=["text"])
> result = sh.self_deduplicate(threshold=threshold)
> --- `src/sift_kg/graph/prededup.py`

#### RT-CMP-sentence-transformer
Label: Optional SentenceTransformer resolution clustering

Source-native identity: `SentenceTransformer`, default `all-MiniLM-L6-v2`. Numerical weights and encoded name/alias vectors are distributed-parametric; local model/cache storage is controlled by the dependency, vectors are transient in the function. The adapter calls `encode`, not training; exact weights revision is unpinned and a model identifier may resolve differently. KMeans fits current clustering centers, not the sentence model; those current-run centers and labels are not saved here. This branch runs only when embeddings are requested and clustering reaches the encoding branch; small sets return unchanged. Dependency/model service internals are uninspected. SRC-1: `src/sift_kg/resolve/clustering.py`, `src/sift_kg/resolve/resolver.py`.

> model = SentenceTransformer(model_name)
> embeddings = model.encode(texts, show_progress_bar=False)
> --- `src/sift_kg/resolve/clustering.py`

#### RT-CMP-ocr-backends
Label: Opaque OCR components behind document readers

Source-native identity: Kreuzberg's selectable Tesseract, EasyOCR or PaddleOCR backend and Google Cloud Vision's `document_text_detection`. Learned recognition state, where used, is distributed-parametric; implementation, parameter storage and updates are dependency/service-internal and uninspected. The adapters request inference and do not request training. Backend names and API method are not immutable model pins; remote/model resolution and service-side updates are not controlled here. Kreuzberg page/configuration handling and GCV image submission are inspectable symbolic adapters. No deployed choice or credentials are supplied. These opaque alternatives prevent exact OCR-model mutability claims rather than establish an absent learned component. SRC-1: `src/sift_kg/ingest/kreuzberg_extractor.py`, `src/sift_kg/ingest/ocr.py`, `src/sift_kg/ingest/pdfplumber_extractor.py`.

> image = vision.Image(content=image_bytes)
> response = client.document_text_detection(image=image)
> --- `src/sift_kg/ingest/ocr.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-schema-discovery
Label: Sampled corpus to reusable discovered domain

The bulk extraction owner selects first-chunk prefixes from at most five pending documents; direct text extraction selects one prefix. A completion model proposes entity/relation definitions. Software uppercases names, builds typed configuration, rejects an empty entity-type result and persists a concrete domain YAML. On caught discovery failure extraction continues schema-free. The proposed change is extraction guidance, admitted automatically without per-schema human approval. Users can hand-edit or replace the file/custom domain, force rediscovery or remove it; there is no versioned rollback in this path. Guidance asks for a corpus-specific schema with descriptions and source/target type lists. Persisted symbolic type keys and constraints become code configuration, while natural-language descriptions/hints are interpreted by the next extraction model. SRC-1: `src/sift_kg/domains/discovery.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/prompts.py`.

> if not entity_types:
>     raise ValueError("Discovery returned no entity types")
> --- `src/sift_kg/domains/discovery.py`

- Immediate return: Concrete DomainConfig or caught discovery failure with schema-free continuation.
- Later read-back: `discovered_domain.yaml` is loaded on later extraction and build invocations in the output directory.
- Delegated visibility: Sample text and domain context reach the configured completion provider; the next extraction receives definitions, not the whole sampled corpus.
- Selection predicate: Schema-free mode without a usable reused schema, or forced rediscovery; samples are positional prefixes, not semantic retrieval.
- Invalidation or expiry: Force bypasses reuse; missing/corrupt YAML can trigger discovery. No content-hash expiry is implemented in the inspected loader.
- Activation or effect: Wiring replaces the active domain and changes subsequent prompt/schema-normalization inputs; actual model compliance or quality benefit is unobserved.
- Evidence limits: SRC-1 implementation/design only; no generated schema run or comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: model proposes; typed parsing and nonempty-type check decide computational admission; a later file editor can replace or veto future use. Answer oracle: none in this route—document samples are input evidence, not expected schema answers. Operating mode: open corpus-derived generation, not a bounded experiment/curriculum. Improvement trigger: missing/forced schema, not measured extraction error.

Theory account: the domain expresses category definitions and directional constraints, not an inspected explanatory revision history. If these definitions are treated as a local theory of corpus organization, the supported properties are separate: theory-builder conditions 1–4: (1) afforded—whole definitions are localized and replaceable; (2) wired—content is incorporated into extraction prompts and build constraints, with model semantic uptake unobserved; (3) uninspected—no supplied content-directed criticism/revision trace, and discovery itself requests design rather than criticism; (4) uninspected—reused schema is wired, but no retained criticism-to-next-round path is established. Addressability: per-type descriptions and source/target lists are inspectable/editable. Persistence: file reuse across invocations. Learning: improved future extraction capacity is not established by an independent outcome comparison. Reflection: corpus schema does not by itself represent sift-kg's own operation. Reflective theory builder and autonomous theory builder: uninspected for this pathway; automatic generation alone does not establish all internal criticism/iteration operations. No exercised self-improvement attribution is made.

#### RT-RTE-document-extraction
Label: Document text to per-document extraction JSON

Trigger/principal: an invoking user, host or library caller supplies documents/text. Reader/chunker code owns selection; the completion model supplies semantic judgments; Pydantic/aggregation code admits results. Context is a domain-conditioned chunk plus the generated first-chunk document summary, not a full conversation. Semaphore/gather coordinate chunks across the bulk run. Document identity is `Path.stem`; entity identities at this stage are names/types. Persisted JSON contains natural-language names, contexts and evidence plus symbolic typed records/metadata. Executor effects are provider requests and output-file writes, not model-selected filesystem actions. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`, `src/sift_kg/ingest/reader.py`, `src/sift_kg/ingest/chunker.py`.

> if existing.model_used != model:
>     return f"model changed ({existing.model_used} → {model})"
> if existing.domain_name != domain_name:
>     return f"domain changed ({existing.domain_name} → {domain_name})"
> if existing.chunk_size != chunk_size:
>     return f"chunk size changed ({existing.chunk_size} → {chunk_size})"
> return None
> --- `src/sift_kg/extract/extractor.py`

> if max_cost and llm.total_cost_usd >= max_cost:
>     return doc_id, ExtractionResult(source_document=doc_id, chunk_index=chunk.chunk_index)
> async with sem:
> --- `src/sift_kg/extract/extractor.py`

- Immediate return: DocumentExtraction list, including cache hits/read errors, plus CLI counts and tracked total cost; direct text API returns one DocumentExtraction.
- Later read-back: Build reloads extraction JSON; narration reloads context fields; repeated extraction reloads cached DocumentExtraction records.
- Delegated visibility: Chunk text, document ID, selected domain guidance and document summary reach the provider. OCR may separately disclose page images to GCV.
- Selection predicate: Recursive supported-extension discovery; cache config comparison; then character windows with overlap. Bulk chunk budget check precedes the shared semaphore.
- Invalidation or expiry: Model string/domain name/chunk size mismatch or force; not source-content identity. Same-stem inputs collide at the output identity.
- Activation or effect: Valid decoded items enter retained extraction records; bad items are skipped and caught chunk failures return empty results. Semantic accuracy and later host behavior are unobserved.
- Evidence limits: No observed requests or artifact-production trace. Source has no entailment or verbatim-quote comparison against input; parse success is not factual verification.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes content; software admits shape-valid entities/relations and deduplicates same name/type, selecting highest confidence and collecting contexts. A user can force or edit files, but workflow initiation is not per-content approval. API/parse failure and malformed-item skipping are computational rejection, not human validation. Recovery includes adapter retries, empty summary fallback, chunk-empty fallback and re-extraction. The chunk docstring mentions entity-only fallback, but the inspected body returns an empty ExtractionResult on caught failure. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/llm_client.py`.

Answer oracle: none; documents supply evidence and prompts request explicit extraction, not a scored expected answer. Operating mode: open supplied-document processing. Trigger for changed knowledge: new/config-stale/forced inputs. Guidance includes explicit-information and original-language evidence rules; extracted knowledge and metadata persist, not a record of model reasoning. Uses [RT-CMP-llm-client](#rt-cmp-llm-client) and the optional [RT-CMP-ocr-backends](#rt-cmp-ocr-backends).

#### RT-RTE-graph-build
Label: Extraction files to rebuilt saved graph and review flags

Build's Python code owns the next steps: load sorted JSONs, skip errored documents, pre-deduplicate, create stable type/name IDs, resolve relation endpoints, add provenance nodes/edges, optionally normalize/prune/fix direction, save graph and communities, and produce relation-review entries. Same IDs aggregate entities; relation addition defaults to canonicalized triples with support mentions. Material state is a NetworkX MultiDiGraph in memory and JSON on disk. Build starts a new graph; it does not load the prior graph's reviewed modifications. SRC-1: `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`.

> # Pre-dedup: merge near-identical entity names deterministically
> canonical_map = prededup_entities(extractions)
> --- `src/sift_kg/graph/builder.py`

- Immediate return: KnowledgeGraph for library callers; CLI reports counts, review flags and graph filename.
- Later read-back: Graph/communities are loaded by resolve, apply, narrate, query/topology/search and downstream presentation.
- Delegated visibility: No completion model call; SemHash may load its model dependency for fuzzy matching. File consumers receive transformed graph records, not every source passage.
- Selection predicate: All parseable extraction JSONs in the output directory, excluding errored documents; supported endpoint names and optional normalization rules determine graph inclusion.
- Invalidation or expiry: Explicit rebuild replaces saved graph and community assignments. Old surgery is not automatically replayed; review files are written when flags exist, not globally cleared.
- Activation or effect: Software automatically admits graph changes and review flags after saving the graph; flags are not a publication gate.
- Evidence limits: Inspected transformations establish wiring, not correctness of name equivalence, schema fit or communities; no benchmark or run evidence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/decision roles: code proposes and decides normalized IDs, deterministic groups, configured canonical handling and postprocessing; [RT-CMP-sem-hash](#rt-cmp-sem-hash) contributes fuzzy groups at default 0.95 threshold. Users can configure/disable postprocessing or replace inputs, not approve each pre-dedup collapse. SemHash failure logs and leaves deterministic grouping available. There is no expected-answer oracle. Operating mode: open rebuild of supplied extraction state. Persistent guidance consists of configured types/canonical names and resulting graph/review files; rollback to exact previous graph requires an external copy. Source-level pre-dedup merges are distinct from the confirmed-proposal surgery gate.

#### RT-RTE-entity-resolution
Label: Saved graph to merge and variant proposals

A CLI/library caller requests resolution; Python groups non-DOCUMENT entities by type and chooses overlapping name-sorted batches (100 entities, overlap 20) or optional embedding clusters. For PERSON, surname/title handling affects grouping. The completion model receives names, aliases and only selected identity attributes, not full graph evidence. It proposes duplicates/variants; software filters IDs/members and deduplicates overlapping proposals. Cross-type identical normalized names also yield code-generated DRAFT proposals, selecting highest-degree canonical and assigning 0.95 member confidence, after the model-task path. SRC-1: `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/clustering.py`.

> identity_keys = {"role", "title", "occupation", "position", "aka"}
> --- `src/sift_kg/resolve/resolver.py`

- Immediate return: MergeFile plus relation-review variant entries; CLI writes proposal YAML and appends nonduplicate variants to review YAML.
- Later read-back: Review and application reload the YAML. Library append lacks the CLI's existing-variant deduplication.
- Delegated visibility: Selected identity payloads/domain context reach the completion model; optional embeddings receive name/alias strings.
- Selection predicate: Selected/all graph entity types except DOCUMENT by default, groups of at least two; batching limits which candidate pairs are compared.
- Invalidation or expiry: Explicit resolve can replace proposal file when proposals exist; no graph-version binding or expiry is checked before application.
- Activation or effect: Proposals persist, but resolve itself does not save a changed graph. EXTENDS entries remain proposals; application has no insertion path for confirmed relations.
- Evidence limits: Overlap does not prove all distant duplicates meet in a batch; no supplied resolution trace or accuracy comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision/admission: model proposes semantic sameness and confidence; code proposes cross-type sameness, filters and writes DRAFT records; review supplies downstream status admission. Users can reject/edit before applying. Operating mode: open candidate comparison, not a curriculum/experiment. Answer oracle: none; confidence is model judgment or a code constant, not comparison to a reference identity answer. Guidance distinguishes duplicates from variants and warns against merging distinct people/subtypes; reasons and confidence persist, not critic histories. Rejection/recovery: caught model failure yields empty results for that batch; optional clustering exceptions fall back to sorted overlapping batches; rerun or edit proposals. Uses [RT-CMP-llm-client](#rt-cmp-llm-client), optionally [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer).

#### RT-RTE-review-application
Label: Review statuses to graph surgery

The caller starts review/application separately. `review_merges` auto-confirms high-confidence DRAFT proposals before interactive remaining-item decisions; CLI defaults also auto-reject relation entries at confidence <=0.5 and auto-confirm at >=0.85. Human choices approve, reject, skip or quit; EOF/interrupt behaves as quit. CLI writes returned status edits to YAML. Direct editing is an alternate admission channel. Application loads current graph and files, uses confirmed entity proposals, validates node existence, merges attributes/sources/aliases, rewrites edges, drops self-loops and removes members; rejected relation triples are removed in both directions. A relation CONFIRMED status is not an insertion instruction. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/engine.py`, `src/sift_kg/pipeline.py`.

> if auto_approve_threshold < 1.0 and min_conf >= auto_approve_threshold:
>     proposal.status = "CONFIRMED"
>     auto_approved.append(proposal)
> --- `src/sift_kg/resolve/reviewer.py`

> return [p for p in self.proposals if p.status == "CONFIRMED"]
> --- `src/sift_kg/resolve/models.py`

- Immediate return: Review statistics and status-file writes; application counts and a graph save only when merges/removals occurred.
- Later read-back: Updated graph enters all later retrieval/narration/export paths; review YAML remains readable for repeated application.
- Delegated visibility: Human reviewer sees member names/IDs/confidence/reason, or relation endpoints/evidence/flag information. No completion model participates in review/application itself.
- Selection predicate: DRAFT status for review; threshold or human choice for confirmation/rejection; CONFIRMED merges and REJECTED relations for surgery, with node existence checks.
- Invalidation or expiry: No expiry or authenticated approver identity; rerun may skip missing nodes. Rebuild replaces the saved surgery result unless decisions are reapplied.
- Activation or effect: Confirmed valid merges and rejected existing relations mutate the graph; confirmed proposed variants alone do not add edges.
- Evidence limits: Human approval is not universal; no supplied reviewer execution or exact rollback trace. Confirmation status does not authenticate who or what set it.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: prior model/code proposes; threshold code or a human decides status; manual file writers can replace decisions. A human can veto remaining items or change automated statuses before application but is not required to inspect every auto-approved item. Answer oracle: no fixed reference answer; manual validity judgment is not a supplied gold-answer evaluator. Operating mode: open threshold/manual review. Admission trigger: caller invokes review/apply against current files. Guidance is proposal reason, evidence and thresholds. What persists: statuses/reasons and mutated graph, not a reversible patch set. Recovery: skipped/quitted drafts remain pending, invalid graph IDs are skipped; exact undo is external backup/reconstruction, not an inspected engine primitive. Guarantee owner/filter and scope are given above; relation flagging does not enforce exclusion while pending.

#### RT-RTE-narrative-generation
Label: Saved graph and extraction contexts to derived prose

A CLI/library caller requests full narration or communities-only regeneration. Code ranks entities, takes up to 50 for overview and 150 adjacent relations, derives chains/timeline, and describes up to 250 entities of degree at least three. Model calls generate overview, chains, timeline, descriptions and labels. Description payloads include local relations and available name-matched source contexts; these are selected summaries, not the whole corpus. Regex-detected filler phrases trigger one rewriting pass with a request to preserve facts. Model failure can retain original prose or placeholder failure prose; successful rewrite is not revalidated for factual equivalence. SRC-1: `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py`.

> Keep everything else EXACTLY the same. Do not add new information. Do not change facts. Only fix the flagged phrases.
> --- `src/sift_kg/narrate/generator.py:621-651`

- Immediate return: Path to narrative Markdown or communities JSON, with cost summary in CLI.
- Later read-back: Descriptions feed search/view and optional export callers; community labels feed topology/query/view and narration's cache reuse; narrative is a saved reader-facing artifact.
- Delegated visibility: Selected graph identities, relations, evidence/context excerpts and domain guidance reach the completion provider; independent calls return only text.
- Selection predicate: Degree ranks, caps, chain/event availability and description toggle; cached nonplaceholder labels can bypass detection/naming; banned-pattern matches select rewrites.
- Invalidation or expiry: Explicit narration/regeneration; themed labels can be reused without graph revision checks. Description sidecar is written only when descriptions exist, so skipped generation does not establish deletion of old prose.
- Activation or effect: Software writes model-produced prose/labels without mandatory human acceptance. Factual compliance, rewrite preservation and downstream answer improvement are unobserved.
- Evidence limits: Request to avoid filler/additions is policy, not an invariant; cost checks cover description scheduling rather than every narration call.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/decision roles: software selects graph payload and rewrite targets, model proposes text, software admits returned strings. Humans can edit/reject downstream files but are not in the per-output write gate. Answer oracle: none; banned-phrase regexes are a style check, not an expected factual answer. Operating mode: open derived generation; trigger is caller request and style violations. Guidance persists indirectly as derived prose; shipped prompt rules remain static. Recovery includes caught-call fallbacks and regeneration, with no versioned prose rollback. This is style-directed rewriting under unchanged instructions, not established content-directed criticism of a theory of sift-kg's operation. Uses [RT-CMP-llm-client](#rt-cmp-llm-client).

#### RT-RTE-graph-retrieval
Label: Agent or human request to saved-state retrieval

The invoking principal owns the request and any follow-up. Query loads graph JSON, uses exact ID first or case-insensitive name/alias substring matching, then chooses highest substantive degree and returns other matches. BFS selects neighbors on a clean undirected graph; output restores directed substantive edges and selected evidence/support fields from the original graph. Search can return descriptions and direct relations; topology loads communities and computes structural summaries. JSON selection rules are symbolic; names, evidence and descriptions retain natural-language interpretation for the caller. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`, `src/sift_kg/graph/knowledge_graph.py`.

> candidates.sort(key=lambda c: _sub_degree(c[0]), reverse=True)
> matched_id = candidates[0][0]
> --- `src/sift_kg/cli.py`

- Immediate return: JSON by default for query/topology, optional pretty output; search supports JSON flag. Unmatched query returns null match/empty subgraph.
- Later read-back: This is the later consumer of saved graph, community labels and optional descriptions. It does not itself write new knowledge.
- Delegated visibility: Calling host receives a selected result; no sift-kg model call. Host's further context injection, persistence or answer policy is outside this implementation.
- Selection predicate: Exact ID or substring plus optional type filter, degree ordering, requested hop depth; metadata nodes/edges removed for substantive neighborhoods.
- Invalidation or expiry: Each invocation reloads current files; no TTL or admission-status filter for pending relations. Missing graph or required topology communities produces CLI error.
- Activation or effect: Returned data can guide caller behavior, but actual agent uptake is unobserved. Return omits full raw document text and full edge mention lists.
- Evidence limits: CLI is not an autonomous session-start scheduler, and delivered graph data is not proof of answer grounding or completeness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: caller selects request; deterministic code matches and ranks. No model candidate judgment, successor admission or answer oracle in this read route. Operating mode: caller-directed lookup. The bundled skill additionally allows loading small graphs directly and recommends topology/query for larger graphs, a host-context policy rather than an enforced memory-size limit. SRC-1: `.agents/skills/sift-kg/SKILL.md`; [RT-BAP-agent-skill](#rt-bap-agent-skill).

#### RT-RTE-view-export
Label: Saved graph to browser and export consumers

CLI/library callers load the graph and request HTML or a supported export. Viewer loads descriptions, loads communities or computes a fallback on the full graph, strips metadata, applies filters and writes HTML plus injected shipped UI; optional browser opening is a host effect. Native JSON export preserves the graph representation; analytical exports strip document/provenance nodes and flatten attributes, optionally incorporating caller-supplied descriptions. SRC-1: `src/sift_kg/pipeline.py`, `src/sift_kg/visualize.py`, `src/sift_kg/export.py`.

- Immediate return: Output file/directory path and optional browser launch.
- Later read-back: HTML/JSON/GraphML/GEXF/CSV/SQLite are reader/downstream-consumer artifacts; this path does not reload them into extraction automatically.
- Delegated visibility: Selected graph data and descriptions reach browser/export readers; arbitrary external reader behavior is outside the frozen implementation.
- Selection predicate: Requested format; viewer neighborhood/source/confidence/top filters; optional community focus and supplied sidecars.
- Invalidation or expiry: Explicit regeneration overwrites destination; no automatic regeneration on graph surgery is established.
- Activation or effect: Rendered/exported data is wired; actual browser exploration or external analysis is unobserved. Viewer fallback communities need not match saved topology communities.
- Evidence limits: No rendered execution supplied; inspection establishes generation and data preparation, not UI security, layout quality or downstream accuracy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### RT-CLM-merge-approval
Label: Universal approval claim versus narrower confirmed-status gate

SRC-1 doctrine/design, `README.md`:

> Nothing gets merged without your approval — the LLM proposes, you verify. Every extraction links back to the source document and passage.
> --- `README.md`

The claimed operation is universal human approval and source linkage. [RT-RTE-review-application](#rt-rte-review-application) establishes a confirmed-status filter, but automatic confirmation and [RT-RTE-graph-build](#rt-rte-graph-build)'s pre-dedup merges defeat universal per-content human approval. Source/evidence fields afford traceability; they do not prove passage entailment or quote identity. This is a qualified implementation finding, not an observed failure rate.

### Evidenced absences

#### RT-ABS-tool-execution
Label: No model-selected tool executor in the inspected shipped request paths

- implementation conclusion status: absent

Searched SRC-1 at d786991c024f5401f113fc0cb70aee96dd1bd3bf: `src/`, `.agents/`, `pyproject.toml`; query `litellm|subprocess|exec\(|eval\(|completion\(|tools=|importlib|entry.points`, followed by complete adapter read and caller traces in extraction/discovery/resolution/narration. The only completion request construction found is in `src/sift_kg/extract/llm_client.py`; its sync/async bodies pass model/messages/timeout/temperature and return textual content. The positive request witness is retained in [RT-CMP-llm-client](#rt-cmp-llm-client). Inspected callers parse data or consume prose, rather than dispatch provider tool calls. This supports absence of a model-selected tool executor in these shipped completion routes, not absence of native dependency subprocesses, service internals or external host-agent tools. It prevents attributing autonomous shell/callback/remote-worker authority to sift-kg's completion model on this evidence.

### Behavioral-authority paths

#### RT-BAP-domain-guidance
Label: Domain guidance to extraction and build consumers

Consumer: completion model for extraction; Python graph build for symbolic type/canonical constraints. Channel: configured or discovered DomainConfig inserted into prompt text and passed as build parameters. Force: natural-language policy request for semantic extraction, fixed software transformation for configured canonical names and optional normalization. Horizon: current call, plus later invocations that reload a saved domain. This distinguishes delivered guidance from reliable model compliance. SRC-1: `src/sift_kg/extract/prompts.py`, `src/sift_kg/domains/discovery.py`, `src/sift_kg/graph/builder.py`; [RT-RTE-schema-discovery](#rt-rte-schema-discovery), [RT-RTE-graph-build](#rt-rte-graph-build).

> ENTITY TYPES (use ONLY these — do not invent new types):
> {entity_types_section}
> IMPORTANT: Every entity must use one of the types listed above. Do not create new entity types.
> --- `src/sift_kg/extract/prompts.py`

#### RT-BAP-agent-skill
Label: Bundled skill to host-agent workflow

Consumer: an external agent that loads the bundled skill. Channel: natural-language skill instructions requesting session-start orientation, graph-first answers, retrieval choices, context-size restraint and user confirmation before paid extraction/resolution. Force: advisory/protocol text interpreted by that host, not a CLI enforcement point. Horizon: sessions where the host supplies and follows it; no host execution supplied. SRC-1: `.agents/skills/sift-kg/SKILL.md`; [RT-RTE-graph-retrieval](#rt-rte-graph-retrieval).

> **Always confirm with the user before running extract or resolve** — these make LLM API calls that cost money.
> --- `.agents/skills/sift-kg/SKILL.md`

The same file directs graph-first responses and retention of topology in session context. This is a shipped behavior request, not evidence of actual cross-session continuity, automatic capability installation or reliable host approval.

## Annotations

none
