---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "TheKnowledge memory: retained sources and wiki content, derived selectors, correction examples, recovery state and host-session checkpoints."
run-id: AAS-2026-10-14-theknowledge-319a64927ee3-01
source-identity: https://github.com/BadWally/TheKnowledge
reviewed-boundary: aca6e29e69c6a72b697b8178841d03e6296ee3fc
---

# TheKnowledge memory report

## Boundary and evidence

This report covers the whole-system memory surfaces in the supplied [boundary](boundary.md#boundary-and-evidence): source retention, wiki authorship and later consumption, policy/example reuse, remote notebooks, operational recovery and development-session checkpoints. SRC-1 is the repository at `aca6e29e69c6a72b697b8178841d03e6296ee3fc`; checkout HEAD was rechecked against that identity. Additional source reads below are implementation evidence, except `CLAUDE.md` and hook instructions where the finding concerns requested agent behavior. No target, tests, model provider or service was executed. Delivery wiring is not observed compliance or benefit.

The runtime baseline is provisional. Its supplied records establish the ingestion, deposit, finalization, retrieval/answer, research/query, policy and skill routes. Direct reads extend those records with alternative context selection, example-bank consumers, demand feedback, evaluations, deletion/recovery and artifact filing. The coverage inventory keeps available but uninspected material visible rather than claiming that the primary RAG path covers it.

| Entry point or memory operation | SRC-1 path; inspection basis | Coverage, missing fact and conclusion prevented |
|---|---|---|
| CLI/MCP dispatch | `src/gateway/cli.py`, `src/gateway/mcp_server.py`; direct bounded dispatch/function searches, plus supplied runtime | Found context, related, preflight, correction, demand, recovery, question and artifact alternatives; selected bodies traced below. Not every registered operation inspected. |
| Incremental ingestion, plan repair and rejected plans | `src/gateway/ops/ingest.py`, `src/gateway/ops/apply_plan.py`; runtime plus direct filter/source-page reads | [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki](#mem-obj-wiki). Converter-specific lineage and batch/legacy admission remain individually uninspected. |
| Deposit and drain | `src/gateway/ops/committer.py`, `src/gateway/commit_gate.py`; direct renderer, dispatch and selected gate branches | [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit); queue retained payload is distinct from admitted page. |
| Retrieve, answer, search, related | `src/gateway/ops/retrieve.py`, `src/gateway/search_index.py`, `src/gateway/retrieval_index.py`; direct selection/assembly/index reads, supplied answer route | [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-OBJ-section-vectors](#mem-obj-section-vectors). Related dispatch found; full co-citation implementation not inspected, so no complete related ranking account. |
| Page-neighborhood context | `src/gateway/ops/context_op.py`; direct complete read | [MEM-RTE-neighborhood-fetch](#mem-rte-neighborhood-fetch); identifier-directed root and graph expansion differ from question ranking. |
| Correction and example read-back | `src/gateway/ops/filter_correct.py`, `src/gateway/filter/examples.py`, `src/gateway/filter/semantic.py`; direct complete reads | [MEM-RTE-example-correction](#mem-rte-example-correction). Legacy-backfill producer found in `src/gateway/ops/example_bank.py`, body uninspected; original label provenance unresolved there. |
| Distillation, bootstrap, policy-edit, skill emission | `src/gateway/ops/finetune.py`; direct prompt/threshold read; other paths supplied runtime | [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap), [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit), [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission). Domain discovery/promotion/demotion bodies remain uninspected; live-policy provenance is not universalized. |
| Demand miss recording, clustering and preflight | `src/gateway/demand_ledger.py`, `src/gateway/ops/demand_cluster.py`, `src/gateway/ops/preflight.py`; direct complete reads; retrieve producer supplied runtime | [MEM-RTE-demand-feedback](#mem-rte-demand-feedback); empty synthesis output is not acquired evidence. |
| Daily domain digest | `src/gateway/ops/daily_digest.py`; direct complete read | [MEM-RTE-digest-authoring](#mem-rte-digest-authoring); separate direct draft-write admission. |
| Judge evaluation and retained trend | `src/gateway/evaluate/runner.py`, `src/gateway/evaluate/persistence.py`, `src/gateway/evaluate/wiki_context.py`, `src/gateway/ops/status.py`; direct reads | [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention); status reads trend. Judge rubric and reference provenance not fully inspected. Retrieval/merge evaluator gates remain supplied runtime findings. |
| Retraction and supersession | `src/gateway/pollers/pubmed_retractions.py`, `src/gateway/lint/retracted_citations.py`, `src/gateway/ops/reingest.py`; direct complete reads | [MEM-RTE-source-maintenance](#mem-rte-source-maintenance); no automatic claim withdrawal established. Cascade implementation and arXiv revision poller not fully inspected. |
| De-path, restore, reverse-merge, contradiction revert | `src/gateway/ops/remediate.py`, `src/gateway/ops/reverse_merge.py`, `src/gateway/commit_gate.py`, `src/gateway/provenance.py`; direct producers and selected apply branches | [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery); reverse-merge consumer body beyond dispatch not fully read, so exact preservation of intervening edits remains unresolved. |
| Section edit, concept creation and question skeletons | `src/gateway/ops/edit_section.py`, `src/gateway/ops/concept_add.py`, `src/gateway/ops/question.py`; direct complete reads | [MEM-RTE-local-amendments](#mem-rte-local-amendments). Citation-add, MOC-add and citation-capture bodies uninspected; no common admission claim for them. |
| Research plans, notebooks and source maps | `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py`; supplied runtime | [RT-RTE-research-query](runtime.md#rt-rte-research-query). Remote selected corpus and model processing opaque; mappings do not expose them. |
| NotebookLM output filing and revision | `src/gateway/ops/nlm.py`; direct artifact builder/create read; revision dispatch inventoried | [MEM-RTE-artifact-filing](#mem-rte-artifact-filing); upload/sync and slide revision bodies not fully inspected. |
| Host compaction/resumption | `.claude/settings.json`, `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `CLAUDE.md`; direct complete reads | [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor), [MEM-OBJ-session-state](#mem-obj-session-state). Host summary/tail/checkpoint alternatives opaque. |
| Scheduler, watcher, browser, six shipped editorial/research skills | `src/gateway/scheduler.py`, `src/gateway/watcher.py`, `web/src/api.ts`, `.claude/skills/`; supplied boundary/runtime | Included drivers and instruction surfaces, not evidence of deployment. Complete watcher cursor, inbox-triage transformations and browser editing behavior uninspected. |
| Other maintenance/navigation/export surfaces | `src/gateway/ops/`, `src/gateway/lint/`, `src/gateway/pollers/`, `migrations/`; direct file inventory; boundary top-level inventory | Backfills, orphan discharge, agenda/digest builders, contradiction sweeper/drift, rotation, migrations, publish-Notion and other poller bodies remain uninspected. Their exact transformations, admission and later consumer chains cannot be inferred from names. Retained sidecars, domain pages and provider payloads not individually assessed for truth. |

External provider internals, host context eviction, deployment state and unshipped consumers remain outside the frozen source. Available source paths left uninspected are limits of this report, not access gaps or evidenced absences.

## Core ideas

1. **Content and its selectors are separate memory.** Raw bodies and wiki prose persist on disk; the lexical index, links, draft flags and vectors determine what reaches later calls. Retrieval reloads selected section bodies but uses derived selection state. Filesystem retention alone does not establish model visibility. [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-OBJ-section-vectors](#mem-obj-section-vectors).
2. **Admission is route-specific.** Validated plans, verbatim deposit rendering, validated local edits, direct daily-digest writes and remote artifact wrappers have different gates. A draft can reach answer context before strict finalization. The common gateway surface is not one universal content-quality check. [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit), [MEM-RTE-local-amendments](#mem-rte-local-amendments), [MEM-RTE-digest-authoring](#mem-rte-digest-authoring).
3. **Retained experience has several different consumers.** Correction rationales are read into future filter prompts; gaps are read into clustering and preflight; recovery provenance supplies restoration content; evaluation trends reach status displays. Only the first directly supplies past decision explanations to a later scoring model. These chains do not establish improved capacity. [MEM-RTE-example-correction](#mem-rte-example-correction), [MEM-RTE-demand-feedback](#mem-rte-demand-feedback), [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery), [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention).
4. **Trust labels and revocation metadata do not decide truth or universal exclusion.** Page trust is a small ranking term; authored pages default to neutral. PubMed retractions and source supersession retain source bodies and produce review signals rather than rewriting every dependent claim. [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-RTE-source-maintenance](#mem-rte-source-maintenance).
5. **Session memory is requested, not automatically materialized by the hook.** The host receives an instruction to have the agent select, write and commit a checkpoint. Exact host compaction products are unknown. Later reread is also an instruction, with a verification/escalation requirement. [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor), [MEM-OBJ-session-state](#mem-obj-session-state).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source bodies and source metadata

Source-native identity: `raw/<type>/<id>.md` and associated source sidecars. Distinct from the transient admission envelope [RT-OBJ-plan](runtime.md#rt-obj-plan); closest producer is [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship). The body is retained source text, not an execution trace or necessarily untransformed original: converters can extract/normalize acquired material. Converter-by-converter provenance, sidecar encoding and initial externally populated vault history remain uninspected. Markdown bodies are natural-language content on the local filesystem. YAML identifiers, domains, filter scores, correction metadata, corpus IDs, backlinks and revocation links are symbolic access/lifecycle state; textual rationales are interpreted prose. These parts have different mutation rules.

Consumers include later plan authorship, filter correction, daily digest, evaluator source-body loading and remote upload/query routes. At those consumers the body is evidence/content, not a mandatory execution policy. Domain/ID fields drive software selection. Raw admission can succeed without wiki-source admission, including rejected or review sources. Source bodies remain retained under the inspected ingest protocol; later reingest and retraction mutate metadata, not the old body. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/ops/reingest.py`, `src/gateway/pollers/pubmed_retractions.py`; [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship).

> old_front["superseded_by"] = actual_new_id
> write_atomic(old_raw_path, fm.serialize(old_front, old_body))
> --- `src/gateway/ops/reingest.py`

#### MEM-OBJ-wiki
Label: Wiki page bodies and page metadata

Source-native identity: filesystem markdown under `wiki/`, including sources, concepts, entities, synthesis, MOCs, proposals, artifacts and newly exposed questions. This is retained output, not [RT-OBJ-plan](runtime.md#rt-obj-plan)'s current-run proposal. Natural-language page bodies carry claims/summaries; symbolic frontmatter supplies type, slug, domain, draft state, source references and navigation. Source-page construction copies title/type/link/filter metadata and a generic summary; it is not itself full source retention. Generated bodies can come from plan models, remote synthesis, local answers, daily digests or caller-authored deposits and edits. Original author identity is unresolved where the API accepts caller text.

Later retrieval, neighborhood fetch, plan updates, evaluation and human/Obsidian readers consume selected parts. Prose has evidential/interpretive authority; validators and software act on structured metadata separately. Draft metadata changes finalization and ranking, not universal eligibility. Reasons for model-authored individual claims need not survive beyond citations and optional plan/log rationale; no general later rationale-reader is established. Different producers retain different lineage. SRC-1: `src/gateway/ops/committer.py`, `src/gateway/ops/concept_add.py`, `src/gateway/ops/question.py`, `src/gateway/ops/retrieve.py`; closest supplied [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer).

> content = fm.serialize(front, body)
> --- `src/gateway/ops/committer.py`

#### MEM-OBJ-search-index
Label: Lexical sections and access metadata

Source-native identity: FTS5/SQLite derived index at `.index/wiki.db`, distinct from canonical [MEM-OBJ-wiki](#mem-obj-wiki) and the encoder [RT-CMP-qwen3-embedding](runtime.md#rt-cmp-qwen3-embedding). Closest supplied consumer is [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). Text section rows are natural-language copies consumed by symbolic lexical ranking; page/domain/link/mtime/size/trust rows are symbolic selectors. Refresh scans raw and wiki markdown, replaces changed entries by mtime/size and removes missing-file rows. This is rebuildable derived state, not new knowledge authorship; equal mtime/size is the inspected unchanged predicate, not a content-hash proof.

Ranking combines BM25, title/slug signal, inbound links, page-kind, draft penalty and a small page-level trust term. Source-type/filter-score metadata yield source-page trust; authored pages without source type use neutral trust. This changes ordering, not eligibility, and does not establish per-claim factual reliability or inherited source trust on entity prose. Selected section bodies are reread from disk. SRC-1: `src/gateway/search_index.py`.

> key += _W_TRUST * (h.trust - 0.5)
> return key
> --- `src/gateway/search_index.py`

> for rel in set(in_db) - set(on_disk):
>     _remove_file(conn, rel)
>     stats.removed += 1
> --- `src/gateway/search_index.py`

#### MEM-OBJ-section-vectors
Label: Dense retrieval vectors and lexical dedup vectors

Source-native identity: separate `EmbeddingIndex` stores for ordinary lexical dedup and neural retrieval, with namespace/key/vector/model-version rows; numeric vectors are distributed representations, symbolic keys locate pages/sections. This is numerical memory derived from retained content, not new model weights. Closest supplied records are [RT-CMP-qwen3-embedding](runtime.md#rt-cmp-qwen3-embedding) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer); the vectors are distinct from their generating component and consuming route. Storage is SQLite plus a retrieval process cache keyed by database mtime. Dedup and dense retrieval must not be treated as one neural store. Exact installed vectors and their initial encoder provenance are not supplied.

Dense selection reads section vectors, embeds the current question and returns nearest section keys; lexical/current-file lookups then gate and render content. Missing store, encoder failure or dimension mismatch can degrade to lexical-only. The inspected dense cache does not test exact weight identity when dimensions match. Query-time rank freshness after edits is distinct from live body freshness. Rebuild/update scheduling and all removal branches for both vector stores were not exhaustively traced. SRC-1: `src/gateway/retrieval_index.py`, `src/gateway/embedding_index.py`; parameter fixity/version limits remain in the supplied component record.

> return EmbeddingIndex(encoder=retrieval_encoder(),
>                       db_path=paths.retrieval_embedding_db_path())
> --- `src/gateway/retrieval_index.py`

#### MEM-OBJ-examples
Label: Filter decision examples

Source-native identity: `Example` YAML at `.knowledge/policies/<domain>/examples/<source-id>.yaml`. Distinct from the candidate policy produced by [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation). Natural-language rationale/excerpt/title and symbolic decision/score/version/pin fields coexist; they are assessed separately at their consumers. Storage overwrites per source/domain rather than appending every correction. Retained excerpt is capped at 500 characters; source metadata snapshot is not a full original document.

Filter prompting consumes decision, score, pin label, rationale and ID, but not the stored excerpt/snapshot body. Distillation instead consumes sampled titles and rationales capped at 240 characters. Bank initialization can come from legacy backfill; exact legacy decision provenance is uninspected. Correction writes are traced below. The module advertises high-confidence automatic pins, but bounded search of `src/gateway/` for `pinned_by=` found concrete producer calls in correction and legacy-backfill, not ordinary ingest. This is a limitation on claimed automatic accumulation, not a repository-wide absence record. SRC-1: `src/gateway/filter/examples.py`, `src/gateway/filter/semantic.py`, `src/gateway/ops/finetune.py`, `src/gateway/ops/filter_correct.py`.

> f"- **{ex.decision}** ({ex.score:.2f}, {ex.pinned_by}): "
> f"{ex.rationale.strip() or '(no rationale)'} "
> f"[id={ex.source_id}]"
> --- `src/gateway/filter/semantic.py`

#### MEM-OBJ-demand
Label: Retained demand gaps and trigger identities

Source-native identity: `.knowledge/demand/gaps.jsonl` and `triggered.json`. Raw user/agent query text is natural-language request history, not an already supported knowledge claim. Caller/timestamp/trigger IDs are symbolic operational state. Clusters and transient lexical vectors are derived selector state; display centroid is a member text, not a model-written summary. Closest supplied [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) identifies the producer; this object and [MEM-RTE-demand-feedback](#mem-rte-demand-feedback) establish distinct later consumers.

Preflight reads raw gaps by word overlap; clustering re-embeds retained text and may enqueue a synthesis intent. Trigger IDs suppress repeated submissions and survive re-embedding. No closed-gap removal or semantic resolution test was established in these consumers. SRC-1: `src/gateway/demand_ledger.py`, `src/gateway/ops/preflight.py`.

> "text": rec.text,
> "caller": rec.caller,
> "recorded_at": rec.recorded_at,
> --- `src/gateway/demand_ledger.py`

#### MEM-OBJ-provenance
Label: Operational provenance and recovery material

Source-native identity: `.knowledge/provenance/nodes.jsonl` with `decision_basis`, and separate contradiction resolution acts. Distinct from [RT-OBJ-intent](runtime.md#rt-obj-intent)'s queue lifecycle, although the node carries its intent ID. Symbolic paths, branch decisions, policy versions and act IDs control recovery; embedded saved page text/claims are natural-language payloads. The generic provenance writer accepts a mapping: its documentation's full replay claim is not proof that every producer fills every field. Gate de-path retains exact page content; merge recovery uses recorded reattachments. This is operational history with specific recovery consumers, not a general model-training dataset.

Remediation reads nested provenance paths to preserve reachable pages; restore reads the latest matching de-path node; reverse-merge builds a plan from tombstone plus provenance; contradiction reversion locates an act and removes its materialized Contested section. Those fields have software authority at the recovery consumer. Their mere presence does not establish successful restoration or interpretation of all audit reasons by a later model. SRC-1: `src/gateway/provenance.py`, `src/gateway/ops/remediate.py`, `src/gateway/ops/reverse_merge.py`, `src/gateway/commit_gate.py`; [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery).

> "depathed_content": depathed_content,
> --- `src/gateway/commit_gate.py`

#### MEM-OBJ-eval-results
Label: Persisted evaluation runs and trends

Source-native identity: `.knowledge/eval/<domain>/runs/<timestamp>.yaml` and `trend.csv`; separate goldens supply reference questions/outcomes. Symbolic scores/counts/tokens and model-written result explanations are stored on disk. The runner derives results from retained wiki/source context plus goldens; initial golden authorship/provenance and all judge rubric details are uninspected. Closest supplied [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit) uses different deterministic gate goldens; these judge-run outputs are not its admission envelope or evidence of passing those gates.

The status operation reads the newest two CSV means and displays their difference. Full YAML result replay into an automatic content or policy rewrite was not established by inspected consumers. These are retained assessments, not necessarily behavior-shaping derived instructions. SRC-1: `src/gateway/evaluate/runner.py`, `src/gateway/evaluate/persistence.py`, `src/gateway/ops/status.py`.

> latest_score = float(trend[-1]["mean_score"])
> if len(trend) >= 2:
>     prior_score = float(trend[-2]["mean_score"])
> --- `src/gateway/ops/status.py`

#### MEM-OBJ-artifact
Label: NotebookLM payloads and display wrappers

Source-native identity: downloaded `.pdf`, `.m4a` or `.md` output and a wiki artifact markdown wrapper containing notebook/artifact IDs, local path, origin question and source-list display. Payload bytes are separate from the readable wrapper. PDF/audio encoding and exact remotely generated contents remain uninspected; their model-visible interpretation cannot be inferred from the wrapper. Wrapper prose is natural-language display, IDs/paths are symbolic references. Remote notebook state is provider-held and opaque. Closest supplied [RT-CMP-notebooklm](runtime.md#rt-cmp-notebooklm) and [RT-RTE-research-query](runtime.md#rt-rte-research-query) concern the service/corpus route, not these filed outputs.

Wrapper markdown can enter generic indexing; binary content does not become searchable prose by being linked. An afforded human/Obsidian file-opening path is not an inspected model reload chain for its payload. Normal creation passes an empty explicit source list. Briefing uses `.md` for both payload and wrapper: the later write replaces the downloaded report at the same path. SRC-1: `src/gateway/ops/nlm.py`, `src/gateway/search_index.py`; [MEM-RTE-artifact-filing](#mem-rte-artifact-filing).

> sources_used=[],
> )
> write_atomic(page_path, artifact_page)
> --- `src/gateway/ops/nlm.py`

#### MEM-OBJ-session-state
Label: Agent-authored development checkpoint

Source-native identity: requested `docs/session-state.md`, persisted as markdown and requested Git commit. Distinct from the hook delivery [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor). The requested summary contains open contracts, files mid-edit, decisions, rejected approaches with reasons and next action. It is derived working-memory prose, not a verbatim session transcript, and not necessarily wiki-domain knowledge. The hooks do not mechanically inspect or select old turns, write this file or commit it. Agent authorship and verification are requested; exact source turns, any host-generated summary/verbatim tail and actual checkpoint creation remain uninspected.

Later foreground sessions are asked to reread and verify selected checkpoint sections against files, escalating disagreement. Natural-language instruction has interpretive authority, not programmatic stale-state rejection. Retention horizon can span compactions/sessions if the agent writes and commits as requested; replacement can omit older context. Reasons for rejected approaches are explicitly requested for a later reader. SRC-1: `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `CLAUDE.md`; supplied [RT-BAP-session-state](runtime.md#rt-bap-session-state) provides delivery evidence.

> ## Rejected approaches this session
> (one line each with reason — helps the next session avoid relitigating)
> --- `.claude/hooks/precompact-snapshot.sh`

### Routes

#### MEM-RTE-neighborhood-fetch
Label: Requested page neighborhood fetch

Closest supplied route [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) ranks question-relevant sections; this route instead resolves a caller-selected path/slug/title and walks links. CLI/MCP context request → root resolution → breadth-first link expansion → markdown/JSON rendering → caller. Code owns selection, caller supplies query/depth/optional budget and a free-form logging identity. It is a read operation, not content admission or human approval. Later agent/human consumption is afforded by the shipped interface and `CLAUDE.md` retrieval ladder; installed external caller behavior is unobserved. SRC-1: `src/gateway/ops/context_op.py`, `CLAUDE.md`.

- Immediate return: Root and neighbor bodies in markdown, or JSON root/neighbor objects; errors for ambiguity, missing caller and invalid controls.
- Later read-back: Previously retained pages reach this new requested invocation; logging additionally retains caller/target/depth/counts.
- Delegated visibility: Returned bodies omit most frontmatter; JSON includes selected identity metadata. No model invoked internally; external agent receives only the return if its host calls this tool.
- Selection predicate: Literal path, normalized slug or unique title substring; followable source/entity/concept/MOC/synthesis links to requested depth. Budgeted neighbors sort by shared root domain and inbound count.
- Invalidation or expiry: Live files reread; missing neighbors skipped, cycles deduplicated. No response persistence or expiry apart from log metadata.
- Activation or effect: Supplies existing knowledge to caller; actual decision changes unobserved. Root is always whole; JSON ignores budget; no budget is applied when omitted.
- Evidence limits: Not the same selector or strict bound as retrieve; title-scan kinds exclude questions/artifacts but a literal path can resolve markdown outside those kinds. External caller permissions and consumption uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if fmt == "json":
>     # Budget does not apply to JSON (structured consumers page themselves).
>     rendered = _render_json(pages)
> --- `src/gateway/ops/context_op.py`

#### MEM-RTE-example-correction
Label: Filter correction and example reuse

Distinct from candidate production [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation); overlaps the filter step in [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) without duplicating either whole route. Explicit CLI/MCP correction → validate decision/source/domain and permitted metadata diff → rewrite raw correction block → pin YAML example → future domain example selection → filter prompt. Caller proposes include/exclude and rationale; software validates shape and stores an endpoint score. The label user-correction is not proof the caller is human. No separate approver or truth oracle. Recovery is another overwrite; no automatic prior-example restoration. Guidance remains current policy plus past decisions; correction rationale persists and is actually read by the next selected filter invocation. SRC-1: `src/gateway/ops/filter_correct.py`, `src/gateway/filter/examples.py`, `src/gateway/filter/semantic.py`, `src/gateway/ops/ingest.py`.

- Immediate return: Correction outcome and touched raw path; example is written as a second retained result.
- Later read-back: `load_all` and policy strategy select examples; `_format_examples` delivers their labels/scores/rationales/IDs as filter calibration guidance. Distillation reads a separate sample.
- Delegated visibility: Filter sees full policy and formatted selected examples plus current source head, normally at most 16,000 characters; stored example excerpts are not delivered by this formatter.
- Selection predicate: Explicit corrected source/domain; policy example count and balanced/recent/corrections-weighted strategy, with final count truncation. Correction preference does not ensure every correction is selected.
- Invalidation or expiry: Per-source example overwritten; malformed entries skipped on load; no inspected time expiry or old-policy invalidation.
- Activation or effect: Trace-derived decision/rationale can influence future scoring and admission. Model compliance, changed decision accuracy and improved future capacity unobserved.
- Evidence limits: This preserves source decision feedback, not full task traces. Ordinary automatic high-confidence pinning is not established by inspected ingest; initial legacy provenance remains unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> examples = select_examples(load_all(effective_domain), policy)
> --- `src/gateway/ops/ingest.py`

Theory boundary: this route applies policy and decision rationales rather than generating an inspected criticism of the policy itself. The localized policy account and independent theory-builder/learning limits remain in [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation). A corrected example can change reliance at scoring without replacing a policy; it does not by itself establish content-directed theory criticism or iterative theory building.

#### MEM-RTE-demand-feedback
Label: Miss history to demand trigger

Closest supplied [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) provides retrieval-gap production; this route owns subsequent gap consumption. Retrieval miss → best-effort raw query record; explicit demand-cluster trigger → reload/count/embed/cluster → recurrence gate and trigger-ID check → synthesis intent → ordinary thin renderer/gate. Explicit preflight independently reads raw gaps and retrieved sections to report coverage. Code decides cluster admission and queue submission; caller opts into triggering, not per-content approval. No expected-answer oracle. The payload contains no acquired answer prose, so the label canonicalization trigger cannot establish autonomous research/synthesis. SRC-1: `src/gateway/demand_ledger.py`, `src/gateway/ops/demand_cluster.py`, `src/gateway/ops/preflight.py`, `src/gateway/ops/committer.py`; [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit).

- Immediate return: Cluster counts/trigger status when enabled; without trigger returns empty clusters rather than computing a report. Preflight returns overlapping gaps and section-count coverage heuristic.
- Later read-back: Gap JSONL is reloaded in later clustering/preflight calls; triggered IDs suppress resubmission; queue worker later consumes retained intent.
- Delegated visibility: inapplicable — clustering/preflight and normal drain rendering use code, not a synthesis model. The queued body's value is empty.
- Selection predicate: Unique query text, occurrence counts, lexical cosine proximity and cold-start-qualified recurrence mass; preflight uses words longer than three characters with any overlap. Trigger IDs use eligible member-text hashes.
- Invalidation or expiry: Re-embedding changes encoder, retains raw text/counts and trigger IDs. No inspected gap resolution/expiry; post-trigger gaps can still appear in preflight.
- Activation or effect: Can enqueue and render a synthesis-shaped page with empty body, question title and member query strings as synthesizes entries; it does not supply a researched answer. Empty sections subsequently fail retrieval rendering's content gate.
- Evidence limits: Queue submission is not canonical commit, acquired evidence or demonstrated enrichment; full gate domain/dedup outcome on these inputs unobserved. Stored gaps have mixed human/agent caller provenance, not authenticated origins.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "body": "",
> "synthesizes": member_texts[:5],  # top members as synthesis sources
> "demand_trigger": True,
> --- `src/gateway/demand_ledger.py`

#### MEM-RTE-digest-authoring
Label: Recent-source digest authorship

Distinct alternate producer of [MEM-OBJ-wiki](#mem-obj-wiki), closest supplied [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship). Routine call → scan recent domain raw sources → prompt model → construct draft page → direct atomic write under wiki-author. Code selects, model writes prose, code admits any returned summary absent call exception; no page validator or per-content human approval is invoked here. Operating mode is a periodic/requested summary, not a reference-answer experiment. Current source heads and instruction to summarize findings shape the proposal; source IDs persist as included works. Existing daily page yields no-op; insufficient sources skips; call failure rejects write. SRC-1: `src/gateway/ops/daily_digest.py`.

- Immediate return: Written/skipped/failure summary and domain/date/source count.
- Later read-back: Draft synthesis body is indexed and can reach retrieve/answer; strict finalization is separate.
- Delegated visibility: Model receives at most ten source heads, each capped at 800 characters, selected in filesystem scan order after domain/time filtering; not full papers or previous operational logs.
- Selection predicate: Domain match, ingested timestamp in requested lookback, at least one source and no existing output for that domain/date.
- Invalidation or expiry: Date-specific output remains; rerunning same date skips instead of refreshing. No automatic rollback on low-quality model prose inspected.
- Activation or effect: Adds derived knowledge summary, not demonstrated trace learning or filter improvement. Draft status does not prevent later RAG delivery.
- Evidence limits: Prompt asks parenthesized source IDs, not inline source wikilinks for each claim; source list is not proof of per-claim support. This direct writer differs from validated apply-plan.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> source_ids = [s["id"] for s in sources[:_MAX_SOURCES_IN_PROMPT]]
> page_content = _build_page(domain, date_str, source_ids, summary_text)
>
> with file_lock(_LOCK_NAME):
>     out_path.parent.mkdir(parents=True, exist_ok=True)
>     write_atomic(out_path, page_content)
> --- `src/gateway/ops/daily_digest.py`

#### MEM-RTE-evaluation-retention
Label: Wiki assessment retention and display

Distinct from deterministic policy gate [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit). Explicit evaluate → goldens/context loader → model judge per golden → per-run YAML and trend CSV; later status → last trend rows → score/delta display. Code owns selection and persistence, model proposes assessments. Goldens provide reference material; their authorship and judge interpretation not fully inspected. No product rewrite admitted by this runner; a human/operator may interpret display, but subsequent decisions are not observed. SRC-1: `src/gateway/evaluate/runner.py`, `src/gateway/evaluate/wiki_context.py`, `src/gateway/evaluate/persistence.py`, `src/gateway/ops/status.py`.

- Immediate return: EvalRunSummary and persisted paths via operation wrapper; error for missing goldens or oversized assembled context.
- Later read-back: Status reloads trend CSV and compares the newest two means. Full per-run YAML consumption by an automatic maintenance/updating model remains uninspected.
- Delegated visibility: Judge gets selected domain synthesis bodies, first 20 concept lines, first 15 entity lines and raw sources named in synthesis metadata, skipping bodies over 30,000 characters; total default ceiling 750,000 characters raises rather than trims.
- Selection predicate: Domain metadata and golden limit; source IDs collected from synthesis entries. No retrieval-query rank selection in this loader.
- Invalidation or expiry: Timestamped results and append-only trend; no inspected automatic expiry, result invalidation after wiki edits or live candidate promotion.
- Activation or effect: Retains model assessments and exposes operator comparison; no demonstrated improvement or automatic prose/policy revision follows.
- Evidence limits: XML-like wrapping is a prompt-format convention, not proved injection resistance. Score history is not causal attribution or evidence that every skipped source was judged.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> write_run(summary)
> append_to_trend(summary)
> return summary
> --- `src/gateway/evaluate/runner.py`

#### MEM-RTE-source-maintenance
Label: Source retraction and supersession signals

Closest supplied [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) produces sources; this route maintains their validity/lineage metadata and signals dependent review, not initial authorship. PubMed poll → XML retraction detection → raw frontmatter stamp/cursor; lint → direct/cascade findings. Explicit reingest → ordinary ingest of new input → raw successor/predecessor metadata → affected citation-page list. Code checks provider XML and source state; caller supplies revised input/domain but human authorship/approval is unresolved. No semantic truth oracle. Failed fetch/parse or failed conversion prevents the corresponding update; superseded old body remains intact. SRC-1: `src/gateway/pollers/pubmed_retractions.py`, `src/gateway/lint/retracted_citations.py`, `src/gateway/ops/reingest.py`.

- Immediate return: Poll counts/errors/cursor state; lint review findings; reingest old/new IDs and affected pages.
- Later read-back: Lint reads raw retraction flags and wiki citation graph; later reingest checks superseded_by; citation consumers can still read retained old bodies/pages. Returned affected list affords operator review, not automatic revision.
- Delegated visibility: inapplicable — inspected maintenance uses code, provider metadata and explicit input conversion. Future models may receive old claims through ordinary retrieval.
- Selection predicate: PubMed IDs and 30-day cursor interval unless already retracted; lint scans PubMed/arXiv retracted raw IDs; reingest identifies exact old citation tokens.
- Invalidation or expiry: Retraction flags remain; cursor advances after fetch. Supersession links preserve both raw sources; no automatic dependent claim replacement or rollback across the separate metadata writes inspected.
- Activation or effect: Produces review obligations/signals; inspected search/retrieve assembly does not consult retracted/superseded fields as exclusion filters or output warnings.
- Evidence limits: Retraction detection also matches broad retraction substrings, not independently verified scientific validity. Version-ID helper does not force the computed version ID into ingest: actual successor ID comes from its output. No complete remote corpus withdrawal or all-consumer invalidation account.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if retracted and not front.get("retracted"):
>     front["retracted"] = True
>     front["retracted_at"] = _now_iso()
> --- `src/gateway/pollers/pubmed_retractions.py`

> actual_new_id = new_front.get("id") or new_id
> --- `src/gateway/ops/reingest.py`

#### MEM-RTE-corpus-recovery
Label: Corpus deletion and recorded recovery

Extends, but does not redeclare, ordinary deposit admission [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit). Remediate scan → exclude MOCs/artifacts and inbound/provenance-reachable paths → queue de-path → gate records text and deletes; explicit restore → latest recorded text → queue → gate recreate. Explicit reverse-merge and contradiction-revert use typed queue dispatch to recovery handlers. Code selects remediation candidates and admits recovery through contained gate writes; caller requests restore/revert without per-content approval. No model authorship or truth oracle. Missing target/content/act or unsafe path can reject/dead-letter. Recovery itself changes future knowledge availability, not a change to model parameters. SRC-1: `src/gateway/ops/remediate.py`, `src/gateway/ops/reverse_merge.py`, `src/gateway/commit_gate.py`, `src/gateway/provenance.py`.

- Immediate return: Candidate/skip list or queued recovery intent receipt, followed separately by worker disposition.
- Later read-back: Provenance nested paths prevent some deletions; latest recorded de-path body supplies restore; contradiction act identifies the page edge to remove. Recreated files can return to lexical indexing on refresh.
- Delegated visibility: inapplicable — selected recovery is deterministic code; stored page text passes through queue/gate without a model.
- Selection predicate: Remediation uses index inbound counts and recursive decision_basis paths; restore searches provenance in reverse order for exact target; contradiction revert searches first matching Contested/loser-source page.
- Invalidation or expiry: Delete removes file; lexical refresh removes derived rows. Restore creates saved text; contradiction success marks act reverted. Dense-vector cleanup and all reverse-merge preservation rules not fully inspected.
- Activation or effect: Changes canonical availability; saved content has direct reconstruction authority. Contradiction revert removes the matching Contested section rather than deleting both underlying claims.
- Evidence limits: Remediation labels its submitted candidates depathed before drain, not proof of completed deletion. Candidate safety is checked at scan; apply-time reachability recheck was not found in the inspected de-path handler. No crash/concurrency or restoration success observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for node in reversed(provenance.read_nodes(root=root)):
>     basis = node.get("decision_basis", {}) or {}
>     if basis.get("reversal_type") == "depath" and basis.get("target") == target_rel:
>         content = basis.get("depathed_content")
>         if content:
>             return content
> --- `src/gateway/ops/reverse_merge.py`

#### MEM-RTE-local-amendments
Label: Caller-authored local page amendments

Closest supplied [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) uses model plans; these operations take explicit caller text or construct a question skeleton. Section-edit validates the full replaced page, honors existing draft metadata and writes under wiki-author; concept-add validates constructed metadata/body, permits draft citation downgrade and force overwrite; question-new checks slug/status/existence then directly writes a skeleton. Caller is proposer and possible editor, but human control is unresolved. Validators can veto edit/concept; skeleton creation has narrower checks. No semantic answer oracle; no automatic prior-content rollback inspected. SRC-1: `src/gateway/ops/edit_section.py`, `src/gateway/ops/concept_add.py`, `src/gateway/ops/question.py`.

- Immediate return: Written path/summary or validation/existence errors; question creation returns metadata path.
- Later read-back: Updated/created markdown can reach index/retrieve/context; question-list scans retained question metadata with domain/status filters.
- Delegated visibility: inapplicable — no model is called internally; caller submits replacement prose/body or title.
- Selection predicate: Explicit path and case-insensitive named level-two section; concept slug/domain and force; question slug/status. Local selection is address targeting, not content-ranked recall.
- Invalidation or expiry: Section replacement preserves other text/frontmatter; forced concept creation replaces existing file; question creation refuses overwrite; no automatic expiration inspected.
- Activation or effect: Alters retained content or task-question navigation, not validated factual entailment. Edit can intentionally remove section text and associated citations when validator still accepts the result.
- Evidence limits: Edit validates before acquiring its write lock; concept-add uses its own per-slug lock. These are not CommitGate admission and should not inherit its CAS/provenance guarantees. Other cite/MOC authoring surfaces remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> val = validator.validate_wiki_page(
>     front, body, "concept", draft=draft
> )
> --- `src/gateway/ops/concept_add.py`

#### MEM-RTE-artifact-filing
Label: Remote artifact download and wrapper filing

Distinct output path from [RT-RTE-research-query](runtime.md#rt-rte-research-query). Explicit slides/audio/briefing request → registered notebook ID → service generation/polling → download → wrapper write/log. Code checks registry/service status/download success; remote service authors payload, code authors wrapper. No semantic page validation, source-support gate or per-content human approval in this inspected function. Topic supplies guidance, not an expected answer oracle. Failed create/status/timeout/download returns failure; previous downloads/remote artifacts are not shown to roll back on later wrapper failure. SRC-1: `src/gateway/ops/nlm.py`.

- Immediate return: Local payload/wrapper paths and notebook receipt, or service/download error.
- Later read-back: Wrapper is ordinary indexed markdown; PDF/audio opening is afforded to human/Obsidian clients by local link and live NotebookLM URL. Automatic model consumption of downloaded payload remains uninspected.
- Delegated visibility: Provider gets notebook ID/focus; exact corpus visible to synthesis is opaque. Later local retrieval receives wrapper, not decoded audio/PDF content.
- Selection predicate: Domain registry and topic-derived dated slug; polls status up to ten minutes. Explicit source-list value is empty at normal wrapper creation.
- Invalidation or expiry: Date/slug can target existing files; live provider URLs are not immutable payload guarantees. Briefing download is overwritten by wrapper at the same .md path.
- Activation or effect: Retains files/references without establishing citation completeness. For briefing, final local file is display wrapper rather than retained generated report text.
- Evidence limits: Download success does not establish grounding; source-list placeholder is not bidirectional content lineage. Slide-revision and notebook upload/sync bodies remain incompletely inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> page_path = artifact_dir / f"{slug}.md"
> --- `src/gateway/ops/nlm.py`

> artifact_type="briefing",
> suffix="briefing",
> extension=".md",
> --- `src/gateway/ops/nlm.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-example-calibration
Label: Retained decision rationale into filter scoring

Consumer: filter model, normally Haiku, followed by software threshold comparison. Channel: selected example lines in policy/system prefix. Force: natural-language calibration guidance; score threshold is separate symbolic admission. Horizon: subsequent source requests until example replacement or selector exclusion. Distinct from [RT-BAP-authorship-prompt](runtime.md#rt-bap-authorship-prompt), which supplies source/page writing guidance to a plan model; closest supplied [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation) instead produces a candidate policy. Trace-origin mixture is correction/legacy labels plus rationale; human identity and initial legacy provenance unresolved. No model weight update or demonstrated improvement. SRC-1: `src/gateway/filter/semantic.py`, `src/gateway/filter/examples.py`; passages in [MEM-OBJ-examples](#mem-obj-examples) and [MEM-RTE-example-correction](#mem-rte-example-correction).

## Annotations

#### On [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship)

Memory consumers receive selected retained source/page content, not an unrestricted prior-agent transcript. Raw-to-page authoring is content derivation, not necessarily trace learning. The retained body and metadata parts are separated in [MEM-OBJ-raw](#mem-obj-raw) and [MEM-OBJ-wiki](#mem-obj-wiki). Direct filter reads confirm selected example rationale reuse from [MEM-OBJ-examples](#mem-obj-examples). SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/filter/semantic.py`; supplied record provides source/page caps, fallback and rejected-plan passages. Rejected plan/error retention remains an operator repair surface; an automatic next-session reloader was not established.

#### On [RT-OBJ-intent](runtime.md#rt-obj-intent)

Body prose is caller payload, not operational control state or an automatically supported claim. Later worker interpretation depends on typed dispatch: reversal and policy-edit bypass normal rendering; demand_trigger alone does not. Stored queue result/lease metadata controls retry/recovery rather than giving the model knowledge. The ordinary rendered page is a different retained object. SRC-1: `src/gateway/ops/committer.py`; direct dispatch passages support [MEM-RTE-demand-feedback](#mem-rte-demand-feedback) and [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery). No universal queue-to-knowledge admission inference.

#### On [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)

Retained prose reaches answer via code-selected, current-body sections and metadata wrappers. Query is the targeting input, domain is a filter/quota input, citations surviving truncation define the later answer ID set. Source trust changes page order rather than exclusion, and entity/concept prose defaults to neutral without source-type metadata. Derived rank stores and live content differ in invalidation. SRC-1: `src/gateway/ops/retrieve.py`, `src/gateway/search_index.py`, `src/gateway/retrieval_index.py`; [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-OBJ-section-vectors](#mem-obj-section-vectors). Supplied record retains budget exception and citation-stripping passages; membership remains distinct from entailment.

#### On [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation)

Candidate derivation reads decision/rationale traces, not complete raw source bodies or full operational logs. Prompt sampling takes up to forty include and forty exclude entries, and rationales up to 240 characters; title comes from stored frontmatter snapshot or source ID. Candidate summary retains some derivation explanation, but a later installed consumer of that explanation is not established. SRC-1: `src/gateway/ops/finetune.py`; [MEM-OBJ-examples](#mem-obj-examples). Monthly calibrator reads counts and logs a recommendation once per ready domain; it does not execute distillation. SRC-1: `src/gateway/ops/filter_calibrator.py`.

> if ts.ready and ts.domain not in already_logged:
>     log.append(
>         "calibration-distill-ready",
> --- `src/gateway/ops/filter_calibrator.py`

#### On [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission)

Retained emitted skill text gives domain knowledge and usage instructions to a later host agent only after discovery/loading. It is deterministic curation of policy/MOC/title content, not evidence of learning from execution traces. The supplied route's title-derived open threads and missing recent-log read prevent classifying module-description claims as implemented trace-fed update. SRC-1: `src/gateway/ops/skill_emit.py`; supplied record provides the write passage and consumer limits.

#### On [RT-RTE-research-query](runtime.md#rt-rte-research-query)

Retained query-plan YAML, notebook registry and source maps control resumption/corpus access/citation resolution. These symbolic records are distinct from remote corpus content and locally filed synthesis prose. Source-map title matches identify uploaded sources but do not show all material the opaque model actually used. Existing wiki retrieval can later consume admitted synthesis; failed persistent promotion need not revoke already written local pages. SRC-1: `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py`; supplied route provides application/review passages. Remote corpus deletion/retraction propagation remains unresolved here; artifact wrapper retention is separately traced in [MEM-RTE-artifact-filing](#mem-rte-artifact-filing).

#### On [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor)

Raw-to-derived-to-consumer chain is old foreground working memory → requested selected checkpoint prose → requested later foreground reread/verification. Trigger is host PreCompact; selector/author is requested foreground agent, not the shell hook. Alternative host verbatim tail/summary forms remain opaque; source does not disclose preferentially evicted old turns or retained tool results. On SessionStart, hook text is automatically supplied context, but checkpoint reload is requested on existence/mtime condition and is not script-performed. SRC-1: `.claude/settings.json`, `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `CLAUDE.md`; [MEM-OBJ-session-state](#mem-obj-session-state).

Working-context control: model subprocesses are per-call frames with capped selected inputs and returned score/plan/prose; the supplied runtime establishes ordinary no-tools/no-session-persistence controls. Only returned material and explicit persisted artifacts cross back, not a guaranteed reusable internal reasoning transcript. Foreground compaction is different: opaque host eviction plus requested external checkpoint. The by-value frame lens fits isolated calls, but a persisted path is only a reload cue, not an automatic reference in the model window. CLAUDE also requests fresh sessions between long loop streams; exact host `/clear`, compaction and resume behavior remain outside this repository's implementation evidence.

## Write side

Acquisition produces [MEM-OBJ-raw](#mem-obj-raw); ordinary admission is split into raw retention, optional filtered source-page admission and optional validated plan admission. Calling ingest is not per-generated-claim human approval. Force inclusion changes the filter path; drafts lower citation checks but remain consumable. Source conversion lineage is local to each adapter and not exhausted by the canonical markdown label. [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship).

Later authorship can use selected existing wiki pages, but the admitted pages need not preserve the complete reasoning that generated their revisions. Rejected plan responses/errors can persist without becoming accepted knowledge. Deposits instead carry caller prose verbatim into thin rendering and CommitGate; queued receipt and canonical page admission remain separate. [RT-OBJ-plan](runtime.md#rt-obj-plan), [RT-OBJ-intent](runtime.md#rt-obj-intent), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit).

Alternative local edits/concept creation use explicit validation, question skeletons use narrower direct checks, daily digests directly write drafts, and artifact filing checks service status rather than page grounding. Starting any of these workflows does not establish who authored/approved its content. These admission distinctions prevent a universal grounding or serialization claim. [MEM-RTE-local-amendments](#mem-rte-local-amendments), [MEM-RTE-digest-authoring](#mem-rte-digest-authoring), [MEM-RTE-artifact-filing](#mem-rte-artifact-filing).

Trace-fed transformation is clearest in correction reuse: past decision/rationale → YAML example → selected calibration lines → future filter score and threshold decision. The reason is both retained and read. Distillation creates candidate criteria and summary from selected example traces but stops before live policy adoption. Bootstrap and policy-edit have separate live admission controls; skill emission derives host instruction content from currently retained policy/navigation/title material. No automatic successful fine-tuning or improved capacity follows. [MEM-RTE-example-correction](#mem-rte-example-correction), [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap), [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit), [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission).

Gap traces and evaluations are different. Demand clusters can cause queue submission, but the retained result is an empty-bodied synthesis-shaped payload, not a grounded answer. Judge assessments persist and trend display has a later consumer; an automatic theory/content update from those results is not established. [MEM-RTE-demand-feedback](#mem-rte-demand-feedback), [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention).

Cleanup can physically delete a page while saving exact content in operational provenance for later restoration. Retraction/supersession flags instead preserve content and signal review. Strict finalization can clear draft state; abandon removes page/backlinks. None of these statuses establishes universal withdrawal from all local and remote consumers. [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery), [MEM-RTE-source-maintenance](#mem-rte-source-maintenance), [RT-RTE-draft-finalization](runtime.md#rt-rte-draft-finalization).

## Read-back

The ordinary pull chain is requested question → lexical/dense selection → live section text → truncated/metadata-wrapped blocks → answer model. Multi-domain quotas and draft inclusion materially change the selected context. Its requested budget is not a strict maximum, and surviving source-ID membership is not entailment. Whole-page neighborhood pull, evaluation-wide domain selection and remote notebook querying are separate consumers/selectors, not variations that can inherit one shared guarantee. [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [MEM-RTE-neighborhood-fetch](#mem-rte-neighborhood-fetch), [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention), [RT-RTE-research-query](runtime.md#rt-rte-research-query).

There is no independent unsolicited vault-wide context push established by these explicit tools. Within an invoked ingest, code automatically selects existing pages and past decision examples; within a host session, event hooks automatically deliver instructions, then ask the agent to reread the checkpoint. Emitted skills afford host-triggered instruction delivery but loading/activation remains unobserved. These stages distinguish request, automatic selection and delivery from changed behavior. [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [MEM-RTE-example-correction](#mem-rte-example-correction), [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor), [RT-BAP-domain-skill](runtime.md#rt-bap-domain-skill).

Recovery reads saved content as reconstruction input; preflight reads raw gaps as planning diagnostics; status reads score trends as operator display. APIs that can store/reload arbitrary fields are not thereby general consumer routes. The concrete inspected consumers above support these specific paths, not hypothetical agent learning from every retained log. [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery), [MEM-RTE-demand-feedback](#mem-rte-demand-feedback), [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention).

## Integration issues

1. **No supplied fact corrections or record duplicates asserted.** New objects are distinct retained results/selectors beside supplied component/admission/route records; new routes cover separately exposed operations. Annotations preserve supplied IDs. No new declaration is a strict part of exactly one supplied referent: source/wiki/index objects span multiple supplied producer/consumer routes, while the intent remains annotated rather than redeclared.
2. **Universal citation/admission doctrine needs route qualification.** The supplied runtime already distinguishes plan/deposit/draft routes. Direct digest writing adds a model-prose path without the full validator; question skeletons and artifact wrappers also use separate narrow gates. Consequence: gateway-only doctrine does not establish every retained claim was checked. SRC-1: `src/gateway/ops/daily_digest.py`, `src/gateway/ops/question.py`, `src/gateway/ops/nlm.py`; [MEM-RTE-digest-authoring](#mem-rte-digest-authoring), [MEM-RTE-local-amendments](#mem-rte-local-amendments), [MEM-RTE-artifact-filing](#mem-rte-artifact-filing), [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only).
3. **Demand-trigger semantics are narrower than the label.** Normal worker does not branch on demand_trigger into research or a synthesis model. It renders the empty body and treats query strings as synthesis metadata. Exact later gate outcome remains unobserved. Consequence: recurring gaps support trace-fed queue work, not demonstrated knowledge enrichment. SRC-1: `src/gateway/demand_ledger.py`, `src/gateway/ops/committer.py`; [MEM-RTE-demand-feedback](#mem-rte-demand-feedback), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit).
4. **Automatic example accumulation remains unresolved.** Bank documentation names high-confidence pins, but the bounded producer search found correction and legacy-backfill calls; ordinary ingest reads the bank without pinning in its inspected filter body. Initial legacy examples and other possible producers need separate provenance checks. Consequence: example reuse is wired, not automatic capture of every past filter decision. SRC-1: `src/gateway/filter/examples.py`, `src/gateway/ops/ingest.py`, `src/gateway/ops/example_bank.py`; [MEM-OBJ-examples](#mem-obj-examples), [MEM-RTE-example-correction](#mem-rte-example-correction), [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation).
5. **Retraction/supersession do not close downstream withdrawal.** Maintainers flag raw sources and report dependents, but inspected retrieve/index code lacks corresponding exclusion/warning handling. Reingest's computed -vN helper is not forced into the converter output ID. Remote removal, dependent revision and other consumers remain unresolved. Consequence: no all-consumer freshness guarantee. SRC-1: `src/gateway/ops/reingest.py`, `src/gateway/pollers/pubmed_retractions.py`, `src/gateway/search_index.py`, `src/gateway/ops/retrieve.py`; [MEM-RTE-source-maintenance](#mem-rte-source-maintenance), [RT-RTE-research-query](runtime.md#rt-rte-research-query).
6. **Trust comments overstate per-claim downstream force if read literally.** The contradiction branch says the loser stays retrievable and down-weighted by trust, but search computes page-level trust, neutral for authored pages without source-type metadata. Individual losing entity claims are not independently reweighted in inspected assembly. Consequence: keep resolution-act policy separate from retrieval truth/reliability. SRC-1: `src/gateway/commit_gate.py`, `src/gateway/search_index.py`, `src/gateway/ops/retrieve.py`; [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-OBJ-provenance](#mem-obj-provenance).
7. **Briefing payload and wrapper collide.** Report download extension is .md, identical to wrapper page path; later wrapper write replaces downloaded report text. Normal explicit source list is empty. Consequence: artifact receipt/file path alone cannot establish retained report content or bidirectional source lineage. SRC-1: `src/gateway/ops/nlm.py`; [MEM-OBJ-artifact](#mem-obj-artifact), [MEM-RTE-artifact-filing](#mem-rte-artifact-filing).
8. **Recovery and vector invalidation remain partially inspected.** Remediation uses current inbound/provenance checks at scan, while inspected de-path handler checks existence and records content rather than repeating reachability. Full reverse-merge handling and dense cleanup after deletes/edits were not exhausted. Consequence: no concurrent safe-cleanup or fully fresh-ranking guarantee beyond scoped code. SRC-1: `src/gateway/ops/remediate.py`, `src/gateway/commit_gate.py`, `src/gateway/retrieval_index.py`; [MEM-RTE-corpus-recovery](#mem-rte-corpus-recovery), [MEM-OBJ-section-vectors](#mem-obj-section-vectors).
9. **Host/context uncertainty stays local.** Snapshot and reread instructions are wired; actual checkpoint production, host-generated summaries/tails, preferential eviction and downstream compliance remain opaque. Distinct hook versus CLAUDE mtime predicates remain as supplied runtime identified. Consequence: no reliable resumption or complete trace compaction assertion. SRC-1: `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `CLAUDE.md`; [MEM-OBJ-session-state](#mem-obj-session-state), [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor).
10. **Remaining included surfaces are named coverage limits.** Converter/poller/migration lineage, discovery/promotion/demotion, cite/MOC edits, inbox triage, scheduler/watcher cursor details, exports, slide revision and other maintenance bodies need route-specific investigation before whole-system curation/admission claims. Goldens/judge provenance and full result consumers remain uninspected. Evidence and prevented conclusions are beside their paths in the coverage table; no absent finding is inferred from noninspection. [MEM-RTE-evaluation-retention](#mem-rte-evaluation-retention), [MEM-RTE-local-amendments](#mem-rte-local-amendments), [MEM-RTE-artifact-filing](#mem-rte-artifact-filing).

## Limitations and checks

Source identity and checkout HEAD match the supplied full revision. Required invocation, member types, boundary, complete runtime, collection, worker rules and complete record contract were read; bounded read continuations were recovered. Source paths remain in SRC-1 at that revision. Only assigned outputs and worker identity were written; no source mutation, target execution, test execution, provider call or agent launch occurred.

Strong source labels were challenged against concrete downstream consumers: bounded context against whole-root/first-block/JSON exceptions; example storage against formatted prompt fields; demand enrichment against empty renderer output; artifact retention against .md wrapper overwrite; trust against page-level selectors; withdrawal against actual read filters. These countercases narrow conclusions without discarding the supported delivery/reuse/recovery paths.

Validation: invocation-specific `commonplace-run validate-output` passed after correcting one quotation attribution; the final check was rerun against this complete output. A passing result establishes structure, identity, references and quote occurrence, not completeness, truth, exercised behavior, benefit or acceptance. Uninspected included paths and opaque external state remain limits even after that check.
