---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM Wiki memory: file-based claim reuse, metadata feedback, synthesis re-entry and non-installed prompt proposals."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
source-identity: https://github.com/kenhuangus/llm-wiki
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
---

# LLM Wiki memory report

## Boundary and evidence

This report covers the retained inputs, knowledge pages, access state, metrics and later consumers of LLM Wiki at the revision in [boundary](boundary.md#boundary-and-evidence). Scope follows all supplied runtime routes, including alternate drivers, direct API edits, maintenance and synthesis. Evidence is SRC-1 implementation and doctrine/design, not a deployment trace. No target code was executed. All implementation statuses below mean wiring, not observed successful use or benefit.

Direct reads added or rechecked `tools/common.py` (configuration, state, logging and serialization), `tools/normalize.py`, `tools/extract.py`, `tools/integrate.py`, `tools/query.py`, `tools/index.py`, `tools/lint.py`, `tools/curated_monitor.py`, `tools/newsletter_agent.py`, `tools/create_eval_set.py`, `clear_rss_state.py`, `AGENTS.md`, and bounded relevant sections of `tools/rss_monitor.py`, `tools/retrospective_validator.py`, `tools/metrics_collector.py`, `tools/prompt_optimizer.py`, `tools/paper_agent.py` and `api_server.py`. Searches checked callable/CLI surfaces, retained-state writes, deduplication, deletion and paper/long-form context handling in SRC-1. Other driver, model-client, UI and research details below are explicitly supplied runtime findings, not independently repeated audits.

| Entry point or operation | Source paths, SRC-1 | Coverage and evidence basis |
|---|---|---|
| File/URL acquisition and monitors | `tools/ingest.py`, `tools/arxiv_monitor.py`, `tools/cve_monitor.py`, `tools/github_monitor.py`, `tools/rss_monitor.py`, `tools/curated_monitor.py` | Supplied [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion) and [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers); direct RSS and curated reads; [MEM-OBJ-ingested-ids](#mem-obj-ingested-ids), [MEM-RTE-curated-poll](#mem-rte-curated-poll). Other feed-specific freshness rules not fully re-audited; no complete feed-coverage conclusion. |
| Normalize/extract/integrate functions and CLI dispatch | `tools/normalize.py`, `tools/extract.py`, `tools/integrate.py` | Direct full reads, [MEM-OBJ-normalized](#mem-obj-normalized), [MEM-OBJ-extracted](#mem-obj-extracted), [MEM-OBJ-wiki-body](#mem-obj-wiki-body), [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata); annotate [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission). |
| Batch, daemon, unified daemon, CVE immediate driver, manual watcher | `tools/pipeline_all.py`, `tools/daemon.py`, `tools/unified_daemon.py`, `tools/cve_monitor.py`, `tools/watchdog_monitor.py` | Supplied [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers). Different destination/mtime/sidecar rules retained, not collapsed into an exactly-once pipeline. |
| Browser/API edits, uploads, ingestion, search, article, backlinks, logs and history | `api_server.py`, `ui/src/App.jsx` | Direct API read/save/history/backlink reads and endpoint search; UI/ingestion details supplied by [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation). Git history is a read affordance over external commits, not an automatic save checkpoint. |
| Search and catalog | `tools/query.py`, `tools/index.py` | Direct full reads; annotations on [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata). BM25 is reconstructed from files, not a retained embedding store. |
| Deep/light lint, retrospective validation | `tools/lint.py`, `tools/retrospective_validator.py` | Direct lint and validator selection/update reads; supplied [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance); separate body and metadata consequences below. |
| Prompt optimization, metrics, evaluation-set construction | `tools/prompt_optimizer.py`, `tools/metrics_collector.py`, `tools/create_eval_set.py`, `eval_set_index.json`, `eval_set/` | Direct schema, fixture builder and evaluation reads; supplied [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization); [MEM-OBJ-eval-set](#mem-obj-eval-set). Actual ignored metrics DB unavailable: no outcome/history reconstruction. |
| Research agenda scan and results | `research_agenda.md`, `tools/research_agent.py` | Supplied [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance), not independent execution evidence. Detailed agenda parsing and stored research notes not re-audited here; prevents claiming all agenda constraints or actual searches were applied. |
| Newsletter, paper and long-form generation | `tools/newsletter_agent.py`, `tools/paper_agent.py`, `tools/paper_agent_long.py` | Direct newsletter and paper read/projection/finalize reads; long-form search plus supplied [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption); [MEM-OBJ-newsletters](#mem-obj-newsletters). Generated papers unavailable, so no claims about actual output or criticism quality. |
| Dedup inspection/reset | `tools/common.py`, `check_rss_state.py`, `clear_rss_state.py` | Direct schema/reset and search of inspector; [MEM-RTE-rss-reset](#mem-rte-rss-reset). Reset affects admission history, not withdrawal of knowledge. |
| Static instructions, provider state, host contexts | `AGENTS.md`, `tools/prompts.py`, `tools/common.py` | Direct governance read; supplied [RT-OBJ-prompts](runtime.md#rt-obj-prompts), [RT-CMP-main-model](runtime.md#rt-cmp-main-model), [RT-CMP-openrouter-model](runtime.md#rt-cmp-openrouter-model), [RT-BAP-agent-doctrine](runtime.md#rt-bap-agent-doctrine). Provider internals and coding-agent host context are excluded/unavailable; no hidden-memory or host-compaction conclusion. |

The inspected Python routes do not register model-selected tools: the supplied [RT-RTE-model-call](runtime.md#rt-rte-model-call) is a completion helper. Exposed functions, HTTP handlers and CLI callers still offer materially different read/write paths. Deployment settings, opaque provider state, ignored `state.db`/`metrics.db`, external feed responses and Obsidian execution remain outside the available evidence, as recorded by the boundary. Tracked scientific claims and target-authored success reports are not independent validation of this mechanism.

## Core ideas

1. **Retention is a chain of projections, not a lossless knowledge graph.** Normalized text survives beside model-derived JSON, but integration projects that JSON to claim text/confidence/source ID. Evidence sentences, entities and relationships can remain in the sidecar without reaching the later merge. Existing body text, not the original extraction object, becomes future model context ([MEM-OBJ-extracted](#mem-obj-extracted), [MEM-OBJ-wiki-body](#mem-obj-wiki-body)).
2. **Knowledge text and access/control state have different authority.** Page bodies reach models as user-message context. SQLite deduplication and page metadata drive fixed Python rules. A source-count increment is an integration count rather than proof of independent corroboration, yet retrospective validation can use it to increase confidence ([MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata), [MEM-OBJ-ingested-ids](#mem-obj-ingested-ids)).
3. **Review flags do not remove material from later reads.** Conflict notes/status survive as text/metadata, but query and synthesis selection do not enforce quarantine. Newsletter generation additionally assigns verified=true and confidence=0.95 after only a length gate. Its output returns to the same searchable wiki ([MEM-OBJ-newsletters](#mem-obj-newsletters), annotations on [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance)).
4. **Retained experience can steer proposal selection without installing a new method.** Metrics/failure rows select optimizer hypotheses, while candidate prompt text is not installed. This preserves a genuine trace-to-decision path but not an operative candidate-to-next-extraction path ([RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)).
5. **Context is selected anew for each call.** Prefix limits, page-count limits and structured projections determine what survives across model invocations. Files remain available to code, but omitted text is not an automatically dereferenceable pointer in a model window ([RT-RTE-model-call](runtime.md#rt-rte-model-call), annotations below).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-normalized
Label: Normalized source documents

Source-native identity: `raw/normalized/<domain>/<hash>.md`, produced by `normalize_file`. Storage: Markdown/YAML files. Natural-language operative part: original UTF-8 text or extracted PDF text, not a conversation trace. Symbolic access/lineage part: eight-character content hash, local source path, domain and timestamps in frontmatter. These parts have different consumption: extraction sends only the body to the model and copies the ID into its result. Input authorship/trust is unresolved per item; normalization does not independently authenticate its content. PDF extraction is a transformation, not a guarantee of preserving all source information. SRC-1: `tools/normalize.py`, `tools/extract.py`, `tools/common.py`.

Closest supplied record [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion) is a driver, not this persistent object; no supplied object counterpart. Re-running normalization can overwrite the same content-derived path and refresh metadata despite immutable-raw doctrine. Existing sidecar presence may then suppress extraction in the batch route. No freshness binding between metadata and sidecar is checked there (supplied driver record).

> file_id = get_hash(content)
> --- `tools/normalize.py`

> with open(target_path, 'w', encoding='utf-8') as f:
>     f.write(normalized_content)
> --- `tools/normalize.py`

#### MEM-OBJ-extracted
Label: Extraction sidecars

Source-native identity: `<normalized filepath>.json`, written by `extract_knowledge`. Storage: JSON file. Natural-language parts are model-generated claims and evidence descriptions; symbolic structure consists of JSON keys/arrays, confidence values and copied `source_id`. This is derived source knowledge, not raw execution history. The model proposes content, Python parses JSON and writes it, and a caller supplies the source path; invocation is not per-claim human approval. SRC-1: `tools/extract.py`, `tools/integrate.py`.

Integration uses the claims' text/confidence and `source_id`; it does not reconstruct evidence from omitted fields. Entities, relationships and evidence may remain inspectable in the JSON but are not automatically a consumer-visible knowledge graph. Parseability is the executable admission test, not correctness or a complete schema. Invalid JSON exits before replacing a sidecar; an old file can consequently remain on disk. Batch existence checks and direct integration are distinct later consumers. Closest supplied [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) covers its production/consumption route; this object has no supplied object counterpart.

> extracted["source_id"] = meta.get("id", "unknown")
> --- `tools/extract.py`

> new_claims_body += f"- {claim['text']} (Confidence: {claim['confidence']}, Source: [[{data.get('source_id')}]])\n"
> --- `tools/integrate.py`

#### MEM-OBJ-wiki-body
Label: Integrated wiki page bodies

Source-native identity: body of the destination constructed by `integrate_knowledge`; storage: wiki Markdown files. Representational form: natural-language claims, confidence/source annotations and any model-produced history/conflict explanations. Link strings become symbolic matching inputs to the API backlink finder but do not execute their referenced content. Lineage: sidecar claim projection, old page body and optional model merge; direct API edits and lint annotations can independently replace/augment it. SRC-1: `tools/integrate.py`, `tools/lint.py`, `api_server.py`.

Closest supplied [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) describes a delivery/authority path, not the object; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) describes its updater. No supplied object counterpart. A body may retain reasons when model text or lint descriptions include them; only their delivery is wired, not their correctness or guaranteed historical completeness. Its next integration consumes the whole prior body; paper/newsletter consumers receive bounded excerpts, not necessarily its rationale or citations. Search scans current complete file text. Retention horizon crosses processes/runs until overwrite; Git recovery depends on external commits, not the file write itself.

> input_text = f"Old Claims:\n{exist_body}\n\nNew Claims:\n{new_claims_body}"
> --- `tools/integrate.py`

#### MEM-OBJ-wiki-metadata
Label: Wiki page metadata

Source-native identity: frontmatter of integration destinations and later validator updates. Symbolic form: `id`, `source_count`, `confidence`, `verified`, `status`, dates and path/domain fields; substrate: YAML within Markdown. This is not the body's factual evidence. Python consumes it for retrospective confidence changes, research selection and catalog display; newsletter passes selected fields onward as text. SRC-1: `tools/integrate.py`, `tools/retrospective_validator.py`, `tools/index.py`, `tools/newsletter_agent.py`; research selector supplied by [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance).

No supplied object counterpart; closest supplied [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) acknowledges a separate symbolic channel, which this object specifies. On integration, confidence/verified/status start afresh at 0.8/false/current; old ID and incremented count survive, with status optionally changed by the new completion's marker. Thus validation improvements or old conflict status are not stable invariants. Increments do not check source-ID distinctness. Weekly reinforcement checks count and confidence, not new source text; it can raise confidence even on conflict pages because that loop has no status exclusion. This is an implemented metadata feedback path, not corroboration established by the evidence.

> metadata['source_count'] = exist_meta.get('source_count', 0) + 1
> --- `tools/integrate.py`

> if page['source_count'] >= 3 and page['confidence'] >= 0.75:
> --- `tools/retrospective_validator.py`

> new_confidence = min(0.9, page['confidence'] + 0.05)
> --- `tools/retrospective_validator.py`

#### MEM-OBJ-ingested-ids
Label: Monitor deduplication rows

Source-native identity: `state.db` table `ingested_ids(source,item_id,ingested_at)`; symbolic SQL rows with primary key `(source,item_id)` on local disk. The code owns admission and physical writes after monitor decisions; no per-row human review. These are access/admission metadata, not retained source claims. Monitors query row existence before processing an item. Closest supplied [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers) names shared deduplication, but no supplied object counterpart. SRC-1: `tools/common.py`, `tools/rss_monitor.py`; other monitor consumers found by scoped searches of `tools/arxiv_monitor.py`, `tools/cve_monitor.py`, `tools/github_monitor.py`.

The label ingested does not imply successful wiki integration: RSS also writes rows when relevance filtering rejects an item. These rows suppress future acquisition, including after a keyword configuration change, until removed or another ID arrives. Payload is not a summary of the rejection reason: it stores source, ID and timestamp. Original trigger/evidence therefore cannot be reconstructed from this row alone. Actual DB contents and operator reset history were not supplied.

> "PRIMARY KEY (source, item_id))"
> --- `tools/common.py`

> mark_ingested("rss", entry_id)  # mark so we don't re-check
> --- `tools/rss_monitor.py`

#### MEM-OBJ-eval-set
Label: Evaluation fixture files and manifest

Source-native identity: `eval_set/` and `eval_set_index.json` produced by `create_eval_set`. Substrate: copied Markdown, generated sidecar JSON and manifest JSON. Natural-language test inputs come from normalized sources; symbolic manifest fields select file paths. The builder groups by domain, takes traversal-order prefixes, fills from the largest domain, then caps at target count 50. Software selection/copying is not human adjudication of expected answers. Initial provenance of every shipped fixture is not audited here. SRC-1: `tools/create_eval_set.py`, `tools/prompt_optimizer.py`.

No supplied object counterpart; distinct from [RT-OBJ-metrics](runtime.md#rt-obj-metrics), which stores measured outputs, and closest route [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization). The evaluator uses only the first ten manifest entries that exist, invokes the current extractor and reloads their sidecars. Outputs are overwritten by extraction and are not independent reference answers. No claim of benchmark representativeness, correctness or candidate-prompt effect follows. Source evidence/reasons in fixtures need not appear in aggregated confidence metrics.

> for idx, item in enumerate(self.eval_set[:10]):  # Test on first 10 for speed
> --- `tools/prompt_optimizer.py`

#### MEM-OBJ-newsletters
Label: Weekly Pulse synthesis pages

Source-native identity: `wiki/synthesis/newsletters/<date>_pulse.md`. Natural-language model synthesis and title block plus distinct symbolic frontmatter; substrate: Markdown file. The metadata is assigned by software after a nonempty/minimum-length test, not established through source validation. Derived input is at most five 400-character body prefixes per category from recent pages. Counts describe all selected recent paths, not just those delivered. SRC-1: `tools/newsletter_agent.py`.

No supplied object counterpart; closest [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) is its route. Newsletters can re-enter query and future newsletter selection because their destination is under wiki and only index/log are excluded by those selectors. Prior synthesis is therefore not reliably separated from original evidence. Body authority remains model-interpreted context; verified/confidence fields are fixed-rule/display inputs for later code. The newsletter context formatter omits the status it collected, so conflict status is not conveyed as a dedicated field. A snippet could still include a conflict note: this is loss of the explicit status channel, not proof that all conflict information disappears.

> if not newsletter_body or len(newsletter_body) < 200:
> --- `tools/newsletter_agent.py`

> f"confidence: 0.95\n"
> f"verified: true\n"
> --- `tools/newsletter_agent.py`

### Routes

#### MEM-RTE-curated-poll
Label: Curated source polling

Endpoints/progression: retained `wiki/synthesis/curated-sources.md` table → source-name strings → DuckDuckGo news requests → dated raw Markdown → later ingestion drivers. Owner/selector is `get_curated_sources`/`check_curated_sources`. The second table column is interpreted as query text, not as an executable URL or trusted-source verification. The table's upstream authorship/admission is unresolved for individual entries; subsequent transformation is fully inspectable. External search supplies proposals; code accepts results with a filename-existence gate and writes metadata/summary. No per-result human veto, independent answer oracle or rollback. Mode: open acquisition on CLI or monitor-driver invocation. SRC-1: `tools/curated_monitor.py`.

Distinct identity: selected subroute of the supplied batch driver, rather than another declaration of its complete ingestion route.
Part of: [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion)

- Immediate return: Raw-file writes, monitor log and fetched count.
- Later read-back: Later polls reread the current retained table; raw results are available to normalize/extract/integrate drivers.
- Delegated visibility: Search service receives each source-name query; downstream model receives derived source bodies through normal ingestion.
- Selection predicate: Pipe-prefixed nonseparator/non-Rank table lines with nonempty second column; at most two news results per query; new dated filename required.
- Invalidation or expiry: Existing same-name dated files suppress rewrites; date change permits another filename; table edits affect next poll, not previously integrated pages.
- Activation or effect: Query selection and raw persistence are wired; no evidence that a changed table improved acquisition or that any run exercised it.
- Evidence limits: Table trust and initial authorship unresolved; external search relevance/freshness unobserved; editable query text is not an authoritative allowlist.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> results = list(ddgs.news(keywords=source, max_results=2))
> --- `tools/curated_monitor.py`

#### MEM-RTE-rss-reset
Label: RSS admission-state reset

Endpoints/progression: explicit `clear_rss_state.py` launch → SQLite DELETE for RSS rows → subsequent RSS monitor can reacquire those IDs. Owner: helper code under invoking OS authority. The caller decides to reset, but human identity is not enforced; no individual content approval. Change proposed/admitted is deduplication state deletion, not claim rejection. No model guidance, independent answer oracle, experiment or automatic rollback. Mode: maintenance command. Distinct from [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers), which reads/writes monitor state, and [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation), which edits content. SRC-1: `clear_rss_state.py`, `tools/common.py`, `tools/rss_monitor.py`.

- Immediate return: Deleted-row count and instruction to rerun monitor.
- Later read-back: Next RSS existence query no longer finds removed rows; candidate IDs become eligible for rechecking.
- Delegated visibility: inapplicable — the helper performs local SQL and prints status, with no model delivery.
- Selection predicate: All rows with source RSS, using the relative `state.db` in command cwd.
- Invalidation or expiry: Deletes only matching admission records; raw/normalized/wiki files and extracted sidecars remain independently retained.
- Activation or effect: Deletion and potential reacquisition are wired, not observed; this is not knowledge withdrawal or safe reprocessing of a whole pipeline.
- Evidence limits: A wrong cwd addresses another DB or fails; actual state/history unavailable; no cascading cleanup or reversal supplied by this helper.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> cur = conn.execute('DELETE FROM ingested_ids WHERE source = "rss"')
> --- `clear_rss_state.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

Read-back chain: normalized body → extraction completion/JSON sidecar → reduced new-claims text → old destination body plus new claims → replacement body → later merge, query or synthesis. Direct inspection of SRC-1: `tools/extract.py`, `tools/integrate.py` confirms the supplied progression. Extraction retains a structured source representation, not a compressed conversation. New-page creation bypasses the merge model; empty merge appends old/new text. A nonempty merge may replace old rationale without checking preservation. Invalid JSON does not admit a new sidecar; existing pages can nevertheless be independently overwritten by API edits. Authorship is model/caller content plus software projection, and software owns admission/I/O; starting ingestion is not human approval of each retained claim.

Source trust is natural-language guidance in [RT-OBJ-prompts](runtime.md#rt-obj-prompts) and host doctrine [RT-BAP-agent-doctrine](runtime.md#rt-bap-agent-doctrine), not a hard downstream confidence cap. [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata) is assigned separately from per-claim confidence. Thus provenance and reasons are partly retained but neither complete evidence transfer nor source-tier enforcement follows.

#### On [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion)

The supplied route's existence-based extraction suppression and unconditional sidecar reintegration make retained files control future processing. Domain/title/category choices determine which old body is reloaded. It is destination-specific reuse, not semantic entity resolution. A previous integration does not invalidate the sidecar or certify successful processing. Repeated integration can increment source_count for the same sidecar, enabling the reinforcement condition in [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata). This is a source-supported countercase to interpreting the count as independent sources; no execution test is claimed. Evidence: supplied record plus SRC-1: `tools/integrate.py`, `tools/retrospective_validator.py` direct reads.

#### On [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers)

Persistent source IDs/raw files/sidecars/wiki pages outlive the queue and schedule counters. The supplied fixed daemon destination concentrates unrelated sources into one later merge context; the CVE immediate destination and batch destinations create other read-back histories. Raw-adjacent sidecar checks and normalized-adjacent sidecar storage do not identify the same checkpoint. This prevents a single global exactly-once or coherent-source-history account. Alerts target humans but do not remove the just-written content from future consumers. Evidence and passages supplied by this route, SRC-1: `tools/daemon.py`, `tools/unified_daemon.py`, `tools/cve_monitor.py`.

#### On [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation)

Direct saves replace the file without the extraction, source-tier, merge-history or validation gates. A browser edit can be human-authored, but a generic API request establishes no authenticated per-content human review. Subsequent search/article and model consumers read this saved replacement. Git history and commit-content endpoints afford requested historical retrieval; save itself does not checkpoint in Git. A historical version can be fetched and then submitted through the save route, but no automatic rollback chain is wired by these endpoints. Backlinks use literal `[[basename]]`/`[[path]]` substring matches over current files; they do not prove provenance integrity. SRC-1: `api_server.py` direct read; browser flow supplied in the runtime record.

#### On [RT-OBJ-metrics](runtime.md#rt-obj-metrics)

SQLite extraction rows retain timestamp, source ID, confidence/count aggregates, validity/error and prompt version, not full source text or the complete failed completion. Integration rows retain conflict/count/confidence deltas. Experiment rows and `wiki/experiments.md` retain hypothesis, metrics, decision and notes. These are symbolic traces and natural-language summaries, respectively, not model-parameter learning. Update consumer: optimizer code queries recent failures and baseline aggregates; failure category then selects hypothesis focus. Later text generation sees current prompt plus selected hypothesis, not a full trace replay. Experiment notes may also enter generic wiki search/synthesis because those selectors exclude only particular filenames, not all operation reports. SRC-1: `tools/metrics_collector.py` direct schema read; [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) supplies the decision/retention passages and window semantics. Actual DB payloads and all initial row producers are not independently reconstructed here.

#### On [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

Memory result: failure aggregates shape future proposal choice; experiment rows/count and kept baseline can affect later cycles. Candidate wording is neither persisted as an active prompt nor installed by the supplied commit method. Retained decision reason/hypothesis is not the complete proposed method or a criticism-to-live-method chain. Evaluation reloads fresh extraction sidecars from at most ten fixture inputs ([MEM-OBJ-eval-set](#mem-obj-eval-set)); conflict rate is constant zero. Rejection changes Git history/index, not a safe restoration of installed candidate state. Consequently raw traces → derived hypothesis/decision is wired, while derived prompt → later production extractor is not wired on this updater. Learning benefit and candidate activation remain unestablished independently of the real metrics feedback. Evidence/passages supplied by the runtime route, SRC-1: `tools/prompt_optimizer.py`, `tools/prompts.py`; fixture evaluator directly rechecked.

#### On [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance)

Deep lint consumes basename identities plus 600-character body prefixes; returned JSON/list and filename membership are software gates, with a model proposing descriptions. Duplicate basenames collapse in the dictionary, so not every named page is unambiguously targeted. Existing status=conflict skips another tag write. Otherwise a description is inserted into the body and status becomes conflict. The retained description can enter a later full-body merge or sufficiently early excerpt; no guarantee preserves all compared context or evidence behind it. Lightweight lint warns about missing fields and high unverified confidence rather than lowering confidence or deleting claims. SRC-1: `tools/lint.py` direct read.

> path_map = {os.path.basename(c['path']): c['path'] for c in claims_to_check}
> --- `tools/lint.py`

Weekly validation selects by filesystem mtime, detects pre-existing body tags and updates status/confidence. Its count-based reinforcement can repeatedly raise confidence up to 0.9 without fetching sources. Modified mtime affects future recentness selection, including newsletter inclusion. Research scans then consume retained metadata under supplied confidence/age/coverage rules; an increased confidence may change future validation-task selection without new factual evidence. Research notes preserve task labels/results, not proof of actual search or completed experimentation. The weekly route does not call the separate contradiction helper (supplied runtime finding). Raw-to-derived chain here is prior page/metadata → rule-based new metadata → subsequent selectors, not factual revalidation. SRC-1: `tools/retrospective_validator.py` direct update reads; research details supplied by the annotated route.

#### On [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption)

BM25 query is requested by CLI/API query text; code reloads complete current Markdown including frontmatter, removes only index/log, tokenizes by whitespace, scores and returns the top five positive scores. It does not expand links, filter conflict/outdated/unverified pages or supply a persistent semantic-vector index. Catalog regeneration instead projects metadata to a human-readable Markdown listing with pending review; it is not the BM25 store. API article requests deliver a chosen full file; API search snippet budget is supplied by the runtime record. SRC-1: `tools/query.py`, `tools/index.py`, `api_server.py`.

Paper selection tests topic substrings across current page text, retains an intermediate 5,000-character prefix, then sends only 2,000 characters for each of the first five matches. Frontmatter can consume this budget. Analysis returns structured insights; the draft prompt projects key_findings/gaps/novel_connections, not the entire original page evidence or the returned contradictions field (SRC-1: `tools/paper_agent.py`, direct source reads/search). Ordinary paper critique gets a 20,000-character draft prefix. Its `## IMPROVED DRAFT` split discards an earlier review when that marker occurs; otherwise the whole result survives. The next round consumes the resulting draft, not necessarily explicit prior criticism. Final Markdown persists under papers, outside generic wiki queries. Long form skips critique and separately generates sections; its final metadata can still say iterations=2 because it reuses finalization. This label is not evidence of two critiques. SRC-1: `tools/paper_agent.py`, `tools/paper_agent_long.py`; latter orchestration supplied by runtime plus direct search.

> improved = result.split("## IMPROVED DRAFT")[1].strip()
> --- `tools/paper_agent.py`

Newsletter CLI selection is independent code-driven recent-page supply, not a foreground relevance request. It reads mtime-selected pages, groups by path/domain and sends five entries per bucket with 400-character body prefixes. This is automatic selection on invocation, not proof of an independent deployed weekly scheduler. Model generation is length-gated, then written under wiki for subsequent consumers ([MEM-OBJ-newsletters](#mem-obj-newsletters)). Full files remain accessible to code, but omitted text cannot be recovered inside the same model call without another external file-selection operation. No turn-history compactor or alternative conversation checkpoint is established by these routes.

## Write side

Acquisition and normalization preserve source-derived text, not independent truth. Monitors and generic callers can supply inputs; normalizer software transforms them without human content approval. Deduplication can admit a durable rejection marker even without a raw document. Resetting that marker reopens admission but leaves earlier products untouched ([MEM-OBJ-ingested-ids](#mem-obj-ingested-ids), [MEM-RTE-rss-reset](#mem-rte-rss-reset)). Curated table initialization remains unresolved, while its subsequent table-to-search-to-raw transformation is known ([MEM-RTE-curated-poll](#mem-rte-curated-poll)).

Knowledge authoring uses model extraction, executable parsing, claim projection and optional model merge. Software admits usable output, with no demonstrated factual oracle or content-specific human veto. Empty merge preserves old body by append, whereas nonempty merge can discard it: that counterpath prevents a universal lossless-history claim. API edits bypass this machinery. These mechanisms and their lineage are in [MEM-OBJ-normalized](#mem-obj-normalized), [MEM-OBJ-extracted](#mem-obj-extracted), [MEM-OBJ-wiki-body](#mem-obj-wiki-body) and annotations on [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) and [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation).

Maintenance includes warning-only lint, model-proposed conflict descriptions and deterministic status/confidence updates. A retained conflict rationale may later reach model context, but source comparison evidence is truncated and filename routing can be ambiguous. Neither a conflict status nor low confidence withdraws a page from BM25 or synthesis. Newsletter admission can promote derived content to verified/high-confidence metadata without validation ([MEM-OBJ-newsletters](#mem-obj-newsletters)). These are distinct admission mechanisms, not one confidence-based acceptance policy.

For evaluation/cleanup/rejection, retained parse failures and metrics affect later proposals; invalid JSON blocks new extraction output, short newsletter output blocks its page write, and lint parsing/membership gates can reject proposed tags. Already-retained artifacts do not thereby disappear. Git reset in the optimizer is not content restoration, and RSS cleanup only removes admission rows. In the inspected query/API/lint/validator/integrator/helper surfaces, no cascading source-withdrawal mechanism was established. This is an inspection limit, not an evidenced absence across every repository branch. Direct edits or external Git operations can remove/replace content, but subsequent invalidation of dependent synthesis/sidecars is not demonstrated. References: [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization), [MEM-RTE-rss-reset](#mem-rte-rss-reset), annotations on [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance).

Trace-fed writes must be distinguished from logging. `wiki/log.md` appends operational summaries (SRC-1: `tools/common.py`); API logs expose them to a requesting caller, and paper topic scans can select a matching log because they exclude only index. This is potential text reuse, not semantic experience distillation. Metrics feed hypothesis selection, but the proposed prompt is not installed. Weekly page metadata updates do feed later code selectors. None of these retained results alone establishes improved future capacity, learned weights or exercised self-improvement.

## Read-back

- **Requested reads:** CLI/API query → reconstructed BM25 → top-five paths/scores; article request → full current file; history request → external Git commits; backlinks request → literal link matches; logs request → operation log. These are different consumers and channels, not a model auto-retrieval service. Evidence: [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation), [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), SRC-1: `api_server.py`, `tools/query.py`.
- **Write-triggered reuse:** destination existence triggers whole old-body delivery to the merge model. The caller's path, rather than semantic targeting, selects the retained object. The full sidecar's richer fields are not part of that context. Evidence: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [MEM-OBJ-extracted](#mem-obj-extracted).
- **Automatic selection after driver/CLI triggers:** recentness/category rules supply newsletter context; topic/traversal rules supply paper context; elapsed-time rules launch maintenance in the unified driver. These are code selectors with bounded prefixes, not consumer-chosen arbitrary read-back. Only completion/derived text crosses the fresh-call boundary. Discarding each call resembles popping a frame with selected inputs and one return value; files are external retained objects, but no model-visible reference has automatic reachability. Evidence: annotations on [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), [RT-RTE-model-call](runtime.md#rt-rte-model-call), [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers).
- **Symbolic reuse:** monitor item IDs suppress acquisition; sidecar existence suppresses extraction; metadata selects research/validation and catalog entries; metrics select optimizer proposals. The relevant authority is a Python predicate, not instruction-following by a model. SRC-1: `tools/common.py`, `tools/retrospective_validator.py`, `tools/index.py`; supplied [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance), [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization).

Static shipped prompts and AGENTS doctrine are not accumulated read-back under this contract. They guide calls/host sessions if loaded, while the optimizer's unrealized candidate installation remains a separate finding. Provider-side retention, weight updates, host compaction and hidden alternative checkpoints are uninspected, not proven absent. Delivery of text or flags is wired; compliant behavior, changed decisions in actual runs and benefit remain unobserved.

## Integration issues

1. **No correction to a supplied fact is required.** This report refines several broad supplied records rather than replacing them. No new declaration is a duplicate of a supplied referent: the object declarations identify stored material where runtime declared routes/authority paths; curated polling is explicitly a part of [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion); RSS reset is a distinct helper. [MEM-OBJ-eval-set](#mem-obj-eval-set) is input material, not [RT-OBJ-metrics](runtime.md#rt-obj-metrics). Containers and parts can coexist.
2. **Count-based confidence feedback needs reconciliation attention.** Repeated sidecar integration increments a count without uniqueness, and reinforcement uses this count without status exclusion. This supports a possible metadata confidence increase without new corroboration, not an observed failure or quality gain. It qualifies the meaning of source_count and validation in [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata), [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance). Evidence: SRC-1: `tools/integrate.py`, `tools/retrospective_validator.py`.
3. **Synthesis trust and re-entry are separate from original-source trust.** [MEM-OBJ-newsletters](#mem-obj-newsletters) receives verified/high-confidence metadata from a length gate, may summarize previous newsletters, and omits explicit status in context formatting. It can enter later query/maintenance/synthesis. This qualifies any inference of independent evidence or validated knowledge from [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption). Evidence: SRC-1: `tools/newsletter_agent.py`, `tools/query.py`, `tools/retrospective_validator.py`.
4. **Unresolved lineage and deployment facts remain local.** Per-item source authenticity, initial curated-table authorship and complete metric-row producer coverage are not established. Actual state/metrics DBs, historical commits made by operators, provider storage and generated papers are unavailable. These limits prevent reconstructing genuine admission history, all failure-to-update provenance, successful rollback or exercised model feedback. They do not erase the known table transformation, metadata loop or metrics selectors ([MEM-RTE-curated-poll](#mem-rte-curated-poll), [MEM-OBJ-ingested-ids](#mem-obj-ingested-ids), [RT-OBJ-metrics](runtime.md#rt-obj-metrics)).
5. **Reasons do not uniformly survive context projection.** Extraction evidence fields are omitted from integration; paper analysis contradictions are omitted from drafting's insight projection; an ordinary critique's separate review may be dropped; long form bypasses critique. Finalization's iterations label is consequently not a uniform trace of criticism. Reconciliation must not infer retained reason-directed iteration or theoretical improvement from that label. SRC-1: `tools/extract.py`, `tools/integrate.py`, `tools/paper_agent.py`, `tools/paper_agent_long.py`; [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), [MEM-OBJ-extracted](#mem-obj-extracted). Actual criticism content is unobserved.
6. **Withdrawal remains a bounded unresolved mechanism question.** RSS reset removes admission state rather than source claims; conflict tagging is not read exclusion; external edits/history can replace content without a demonstrated cascade. No complete dependency invalidation/withdrawal conclusion is warranted beyond inspected surfaces ([MEM-RTE-rss-reset](#mem-rte-rss-reset), [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation), [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance)).

## Limitations and checks

The source HEAD was rechecked as d2bd485921f6c7b6071afbb389f44ab8e4e83c69 and its working tree was clean. Run/source identity matches the supplied boundary. Method identity is the supplied invocation, member type, worker rules and records contract, all read completely; no method revision was supplied, so none is inferred. The coverage table distinguishes direct reads, source searches and supplied findings. No target runtime, test, provider call or experiment was launched.

This account establishes file/SQL retention and code-controlled delivery, not successful production operation, faithful preservation, source truth, actual model compliance or causal benefit. It does not classify opaque provider state from client behavior. Candidate-to-live prompt feedback is not established even though trace-to-proposal and metadata-to-selector paths are real. Content validation checks form and quotation occurrence, not these analytical conclusions.

Validation result: the required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
