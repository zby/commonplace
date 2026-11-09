---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MemexOS memory: session distillation, Git-backed wiki revision, classification precedents, feedback repair and requested retrieval."
run-id: AAS-2026-11-07-memexos-5cd34a715eb7-01
source-identity: https://github.com/liushengyu/memexos
reviewed-boundary: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
---

# MemexOS memory report

## Boundary and evidence

MemexOS retains collected sources and derived wiki pages, not just a conversation history. The memory scope includes source admission, session rendering and distillation, classification and taxonomy state, staged knowledge revision, feedback and review reuse, search indexes, requested retrieval and working-context selection. The frozen source is SRC-1 at the reviewed commit above, as registered in [boundary](boundary.md#source-register). The supplied runtime is a provisional implementation account, not execution evidence.

Direct inspection added session parsing/rendering, admission output normalization, raw naming/validation, URL capture, usage extraction/judging/verification, classification sampling/precedents/settlement/sync, FTS indexing, qmd configuration/update/query, search display/deduplication/get and adaptive rerank budgeting. English vault and admission instructions provide doctrine/design; Python provides implementation. No target execution, model call, test run or live user vault was used. External provider weights, CLI context internals, qmd storage internals, collectors' live responses and ordinary agents' final reasoning remain outside the inspected implementation. Available localized instructions, evaluator outcome artifacts and lower-level media collectors were not fully read; their presence establishes neither equivalence nor benefit.

### Coverage inventory

All source paths below are SRC-1 commit-relative paths. “Runtime” means supplied findings, not independently repeated inspection. An unresolved row remains included in the memory scope.

| Entry point or operation | Source path and inspection | Records or missing fact and prevented conclusion |
|---|---|---|
| CLI dispatch and initialization | Direct `src/memexos/cli.py`; runtime `src/memexos/scaffold.py` | [MEM-OBJ-raw](#mem-obj-raw), [RT-CLM-schema-change](runtime.md#rt-clm-schema-change). Init and static AGENTS are not accumulated experience; sample-vault initialization provenance is not assessed. |
| Sessions list/show/docs; unattended intake | Direct `src/memexos/intake/sessions.py`, `src/memexos/intake/admit.py`, `src/memexos/prompts/en/admission.md` | [MEM-OBJ-session-snapshots](#mem-obj-session-snapshots), [MEM-RTE-session-distillation](#mem-rte-session-distillation), [RT-RTE-source-admission](runtime.md#rt-rte-source-admission). External compaction summaries can enter the rendering; their production is opaque. |
| Manual raw placement, add-url and plugin capture | Direct `src/memexos/capture/add.py`, `src/memexos/rawfile.py`; runtime plugin loader | [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-assets](#mem-obj-assets), [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading). Caller-requested capture is an alternative to admission-agent selection. Human authorship of every request is unresolved. |
| Video, visual companions, transcription | Direct grouping in `src/memexos/pipeline/stage.py`, classification digest and English vault contract; media implementations not inspected in depth | [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-assets](#mem-obj-assets). Transcript and visual/model reading are distinct provenance; actual frame selection, ASR quality, retained numerical media state and lower-level rejection coverage are uninspected, preventing complete media-transformation claims. |
| Catalog classify/backlog/redo, draft check/decision/sync | Direct selected ranges of `src/memexos/catalog/classify.py`; taxonomy internals searched, not fully read | [MEM-OBJ-catalog](#mem-obj-catalog), [MEM-OBJ-taxonomy](#mem-obj-taxonomy), [MEM-RTE-catalog-reuse](#mem-rte-catalog-reuse). Proposal-validation and judge-screen internals remain incompletely inspected; no complete taxonomy-admission invariant follows. |
| Ingest, lint, fix, correct, publication/hold/discard | Direct `src/memexos/pipeline/stage.py`, maintenance portion of `src/memexos/pipeline/compile.py`; runtime writer/gates | [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-review](#mem-obj-review), [MEM-OBJ-ledgers](#mem-obj-ledgers), [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). |
| Inbox decisions/apply, console abandon, nightly | Runtime `src/memexos/inbox.py`, `src/memexos/console/actions.py`, `src/memexos/schedule.py` | [MEM-OBJ-inbox](#mem-obj-inbox), [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance). Full research-cache/triage transformations not independently inspected; no complete account of every field reaching apply. |
| Usage extract/report/judge/verify; feedback | Direct `src/memexos/usage.py`, maintenance consumer in `src/memexos/pipeline/compile.py` | [MEM-OBJ-usage](#mem-obj-usage), [MEM-OBJ-feedback](#mem-obj-feedback), [MEM-RTE-usage-repair](#mem-rte-usage-repair). Raw transcript retention alone is not this derived repair path. |
| Reindex, search/get, model setup | Direct `src/memexos/search/{fts,engine,cli,qmd,rerank}.py` | [MEM-OBJ-fts](#mem-obj-fts), [MEM-OBJ-vectors](#mem-obj-vectors), [RT-RTE-search-get](runtime.md#rt-rte-search-get), [MEM-RTE-rerank-budget](#mem-rte-rerank-budget). |
| Agent/structured calls and registered tools | Runtime `src/memexos/backends/{base,tools,anthropic_api,openai_compat,claude_code,codex}.py` | [RT-RTE-backend-execution](runtime.md#rt-rte-backend-execution). Read caps and call isolation are included; external CLI compaction and provider hidden state remain opaque. No independent push-memory hook is established by these routes. |
| Evaluation acquisition and later consumers | Direct suite map `src/memexos/evals/__init__.py`; runtime retrieval caller; usage excludes eval-kind records from ordinary judging | [MEM-OBJ-usage](#mem-obj-usage), [MEM-RTE-usage-repair](#mem-rte-usage-repair). Retrieval/tooluse/gate2 suites are included, but full evaluator storage and automatic proposal-coverage transformations remain uninspected. No score or automatic evaluator-driven improvement claim. |

## Core ideas

1. **Sources and working knowledge have different lifecycles.** Raw material is appended; agents rewrite wiki material in staging. Sources sections retain paths to evidence, not a guarantee of fidelity. Session snapshots are already model-distilled before compilation; “raw” is not synonymous with verbatim external evidence ([MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-session-snapshots](#mem-obj-session-snapshots), [MEM-OBJ-wiki](#mem-obj-wiki)).
2. **Reuse occurs at several consumers.** Published pages inform asking agents; classification history informs later classifiers; review problems inform repair writers; usage traces can become verified repair jobs. These differ in authority and admission. None establishes improved capacity or reliable compliance merely by persisting ([MEM-RTE-catalog-reuse](#mem-rte-catalog-reuse), [MEM-RTE-usage-repair](#mem-rte-usage-repair), [RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages)).
3. **Retrieval is requested, then selected by software.** Search ranks retained wiki and raw content, ordinarily excludes inbox hits, and can suppress a raw hit in favor of its compiled source page. Get reloads the requested file, so the index payload and final page need not have identical freshness. There is no demonstrated unsolicited delivery to ordinary consumers in these routes ([RT-RTE-search-get](runtime.md#rt-rte-search-get), [MEM-OBJ-fts](#mem-obj-fts)).
4. **Separate model calls exchange files and reports, not an inspected shared conversation.** Context caps, role-specific prompts and a stage preserve selected material across calls without replaying all traces. An extra, smaller feedback loop stores rerank timing to change future retrieval cost, not knowledge truth ([RT-RTE-backend-execution](runtime.md#rt-rte-backend-execution), [MEM-RTE-rerank-budget](#mem-rte-rerank-budget)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw sources

Identity: retained `raw/` source files, excluding the separately assessed session, feedback and asset parts below. Substrate: vault filesystem and Git history; natural-language extracted web/document/transcript content with symbolic provenance headers. This is distinct from the draft workspace [RT-OBJ-stage](runtime.md#rt-obj-stage), and is the input of [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) and [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish), not a duplicate of either route. Initial content can be external capture, local documents, manual placement or plugin output; calling it raw does not establish its authenticity. Direct `add-url` scrubs the body then writes, without running the admission reviewer. `rawfile` validates headers and chooses unused names. Binary documents can be copied unchanged by admission; their readable interpretation is not established by that copy. SRC-1: `src/memexos/capture/add.py`, `src/memexos/rawfile.py`, `src/memexos/intake/admit.py`.

> body, hits = scrub(body, secrets)
> --- `src/memexos/capture/add.py`

> while path.exists():
>     path = raw_dir / f"{stem}-{n}{ext}"
>     n += 1
> --- `src/memexos/rawfile.py`

Consumer: compiler reads pending raw files; later search can deliver raw content directly, so wiki approval is not a universal source-consumption gate. Vault instructions say embedded commands are data, not commands; that is requested interpretive discipline, not an enforcement guarantee. See [RT-RTE-search-get](runtime.md#rt-rte-search-get).

#### MEM-OBJ-session-snapshots
Label: Session snapshots

Identity: `snap-*` admitted as session sources. Substrate: Markdown in raw and Git. Form: natural-language conclusions/data plus symbolic session-key/date metadata. Distinct derived part of the raw-source family, with mixed person/agent/tool origin, not raw chat replay. No exact counterpart in runtime: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) declares the enclosing admission route. The admission model selects and authors; software normalizes and writes. Reasons are requested inside the distilled body and admission ledger, but retention of all original reasoning or failed experiments is not assured. Later compiler and asking agents can read snapshots; they are knowledge input, not code or learned model weights. SRC-1: `src/memexos/intake/admit.py`, `src/memexos/prompts/en/admission.md`.

> Only distilled conclusions and data: what was decided and why, what happened, what went wrong, where numbers come from. Drop dead ends
> --- `src/memexos/prompts/en/admission.md`

> "fetched_via": "session-snapshot (distilled by the admission agent)"}, body, fallback)
> --- `src/memexos/intake/admit.py`

#### MEM-OBJ-feedback
Label: Feedback sources

Identity: sentence-targeted `raw/feedback/` files, distinct from usage feedback JSON and ordinary snapshots. Natural-language facts/evidence with symbolic `pages`, `claim`, session/provided-by headers; filesystem/Git substrate. Input can be admission-distilled conversations or owner decision facts. `write_output` falls back to a snapshot when feedback validation raises ValueError, so not all attempted feedback remains in this part. `pending_feedback` excludes corrected/held and `route: inbox-apply` material; correct reads remaining files. Doctrine asks the writer to cite feedback on changed pages, not blindly follow rewrite instructions. Closest supplied referent: [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance), which is a route rather than this artifact. SRC-1: `src/memexos/rawfile.py`, `src/memexos/intake/admit.py`, `src/memexos/pipeline/stage.py`, `src/memexos/templates/vault/en/AGENTS.md`.

> Feedback contains only facts and evidence; how to rewrite is your call. If it says how the page "should be written", do not copy that
> --- `src/memexos/templates/vault/en/AGENTS.md`

#### MEM-OBJ-assets
Label: Source attachments

Identity: `raw/assets/` original bundles/images, distinct from the source's text display. Filesystem/Git storage; encodings can include symbolic document bundles and opaque binary images, not necessarily natural-language propositions. Admission HTML conversion preserves the original alongside extracted text; binary documents can instead be retained directly under raw. Asset copying is not a model judgment of its content. Compiler pending selection and FTS exclude assets. Vault doctrine affords page embedding and visual interpretation; the full downstream image-delivery path is uninspected here. Closest runtime route is [RT-RTE-source-admission](runtime.md#rt-rte-source-admission); no object counterpart. SRC-1: `src/memexos/intake/admit.py`, `src/memexos/pipeline/stage.py`, `src/memexos/search/fts.py`.

> shutil.copy2(src, bundle / src.name)
> --- `src/memexos/intake/admit.py`

#### MEM-OBJ-wiki
Label: Wiki pages

Part of: [RT-OBJ-stage](runtime.md#rt-obj-stage)

The stage's operative Markdown content part, with a published continuation in the live vault after merge; not a replacement for the workspace container. Source-native kinds: sources/entities/concepts/topics plus index and log. Natural-language claims, summaries, contradictions and citations; symbolic paths/frontmatter and wikilinks; filesystem/Git storage. Compiler/lint/fix/correct/inbox writers propose edits; program checks/review constrain publication as in [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). Knowledge can be merged/split/repaired; historical Git copies are not the active content. Source summaries and links retain evidential pointers; they do not necessarily retain every derivation or rejected version's reasons. Later search/get, classifiers' effective frontmatter view and maintenance writers consume different parts. Citation/source-strength rules are interpretive guidance at answering agents, not host-level answer constraints. SRC-1: `src/memexos/templates/vault/en/AGENTS.md`, `src/memexos/catalog/classify.py`, `src/memexos/pipeline/stage.py`.

> Each page: a one-sentence definition → the body → a **Sources** section listing the `raw/` files or external links that support it
> --- `src/memexos/templates/vault/en/AGENTS.md`

#### MEM-OBJ-inbox
Label: Inbox material

Part of: [RT-OBJ-stage](runtime.md#rt-obj-stage)

The stage's inbox text part and its live continuation: natural-language unresolved questions/options/recommendations, reports and candidate text, with symbolic tags/queue metadata. Filesystem/Git stores published reports/candidates; runtime also describes local decision state. Unlike wiki pages, it is ordinarily excluded from search results. Model uncertainty can lead to candidates rather than raw; owner decisions or qualifying agent items can later enter apply. A blocked report is not the held branch payload itself. Lint deletes old top-level Markdown by mtime; nested candidates do not fall under that glob. Distinct from [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance), which owns progression. SRC-1: `src/memexos/intake/admit.py`, `src/memexos/pipeline/compile.py`, `src/memexos/search/engine.py`.

> old = [p for p in (cfg.vault / "inbox").glob("*.md") if time.time() - p.stat().st_mtime > days * 86400]
> --- `src/memexos/pipeline/compile.py`

#### MEM-OBJ-ledgers
Label: Processing ledgers

Identity: ingested/held/corrected/fixed-reviews text sets plus admission JSONL reasons/decisions. Symbolic paths, keys and statuses govern later software selection; natural-language reasons retain a different, interpretive part. Filesystem/Git `.memex/` substrate. Admission reasons record model choices, not independently verified warrant. Processing sets derive from orchestration, not author-written summaries; they can suppress another compile/correction/fix or stop retries without changing wiki claims. Runtime declares the owning routes, not this state object: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission), [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). SRC-1: `src/memexos/pipeline/stage.py`, `src/memexos/intake/admit.py`.

> seen = ledger(vault, "ingested.txt") | ledger(vault, "held.txt")
> --- `src/memexos/pipeline/stage.py`

#### MEM-OBJ-review
Label: Retained review results

Identity: local gate2 `review.json` judgments and `report.json` mode/raws/outcome, including synthesized feedback fix jobs. Filesystem state directory, not the same as published knowledge. Symbolic verdict/importance/covered fields drive program decisions; natural-language claim/evidence/reason fields guide writers. This is distinct from the authority path [RT-BAP-review-verdicts](runtime.md#rt-bap-review-verdicts), whose quoted evidence supplies the gate decision. Reviews preserve targeted criticism and source text, not necessarily the complete reviewer context. `unfixed_reviews` selects review.json directories absent from fixed-reviews.txt; report.for_writer renders problems; fix writes revised wiki through normal staging. A no-problem review is marked handled without writer/review. SRC-1: `src/memexos/usage.py`, `src/memexos/pipeline/compile.py`.

> "raw_location": p["raw_location"], "reason": f"{p['reason']} ({res['summary'][:200]})"})
> --- `src/memexos/usage.py`

#### MEM-OBJ-usage
Label: Usage events and feedback

Identity: local usage events/judgments/feedback/source-errors/feedback-status JSONL. Symbolic event keys, page references, status and selectors; natural-language bounded question/answer/reason/evidence excerpts. Filesystem state directory outside committed wiki; not an opaque embedding or complete transcript. Parsed Claude/Codex session logs are the upstream trace. Extraction removes/remaps material before the judge receives it. Judge writes reasons/bad-page feedback; verifier can create the separately declared review object. `summary`/report feeds operator displays and lint's optional 30-day, 6,000-character usage context. A “helped” verdict is attributed model judgment, not demonstrated learning. Distinct state consumed by [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance); no supplied object counterpart. SRC-1: `src/memexos/usage.py`, `src/memexos/pipeline/compile.py`.

> return usage.report_text(cfg, days=30)[:6000]
> --- `src/memexos/pipeline/compile.py`

#### MEM-OBJ-catalog
Label: Source catalog

Identity: `.memex/catalog.jsonl`, append history with latest entry per raw selected by load. Filesystem/Git substrate. Symbolic category/usage/evidence/durability/model/taxonomy identifiers; natural-language summary and scope note. Numerical screen probabilities are localized scores, not distributed model parameters. Derived from sampled source content, classifier and optional screen; writer page overrides can supersede selected fields for effective display/sync. Lineage includes taxonomy version, model/backend and timestamp; it is not complete raw-reading evidence. Consumers: compile classification prompt, search classification display, taxonomy checks and later classification precedents. Distinct from [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish), whose input it supplies. SRC-1: `src/memexos/catalog/classify.py`.

> cat[r["raw"]] = r
> --- `src/memexos/catalog/classify.py`

#### MEM-OBJ-taxonomy
Label: Taxonomy and draft registry

Identity: `.memex/taxonomy.md` and `.memex/taxonomy-nodes.jsonl`. Filesystem/Git substrate. Natural-language definitions/includes/excludes/rationale and symbolic official/draft identities, lifecycle events and membership. Distinct from source-specific [MEM-OBJ-catalog](#mem-obj-catalog); no exact supplied object counterpart. Initial taxonomy/scaffold authorship is static shipped content; subsequent model proposals, stability rechecks and caller decisions alter retained definitions/state. `run_batch` prepends taxonomy text; `check` rehomes unknowns, expires idle drafts, requests decisions on sufficiently stable drafts; `decide` approves/merges/rejects and moves catalog membership. The source calls decisions “person,” but function/API identity alone does not authenticate a human. Internals of taxonomy screen/propose are incompletely inspected. SRC-1: `src/memexos/catalog/classify.py`, `src/memexos/catalog/taxonomy.py`.

> prompt = tx.md.read_text(encoding="utf-8") + i18n.prompt("classify_task", drafts=drafts_section(cfg, tx, cat), n=len(rels)) + items
> --- `src/memexos/catalog/classify.py`

#### MEM-OBJ-fts
Label: Full-text index

Identity: built-in SQLite FTS5 cache with docs path/title/size/mtime and tokenized title/body. Symbolic encoding, not dense parameters. Derived mechanically from wiki/raw/inbox files; raw/assets and hidden directories are excluded, index.md is not indexed. Source files remain the canonical content: snippets are read from files even when index metadata is cached. Incremental refresh compares size/mtime, removes disappeared paths, and can rebuild damaged indexes; missing/unusable index falls back to file scan. These are cache consistency mechanisms, not semantic knowledge curation. Same enclosing route as [RT-RTE-search-get](runtime.md#rt-rte-search-get); distinct object. SRC-1: `src/memexos/search/fts.py`.

> INDEXED_DIRS = ("wiki", "raw", "inbox")
> --- `src/memexos/search/fts.py`

> gone = [(i, p) for p, (i, _, _) in known.items() if p not in seen]
> --- `src/memexos/search/fts.py`

#### MEM-OBJ-vectors
Label: qmd retained index

Identity: per-vault named qmd SQLite index and generated YAML configuration, with local qmd.json embedding marker. Vectors are distributed numerical representations derived from retained text; config/marker/paths and returned title/body snippets are symbolic/text parts with different roles. This is not the model parameters in [RT-CMP-qmd](runtime.md#rt-cmp-qmd). Detailed vector schema/chunking/provenance inside qmd is external and uninspected. The marker names embedding model and time, not immutable parameters or per-vector verified lineage. Generated config indexes Markdown with exclusions including assets/.memex/log/index. Update then embed admits derived content without per-vector human approval; changed model settings can clear readiness while forced embedding runs. Returned snippets are readable display, not the opaque vector payload. SRC-1: `src/memexos/search/qmd.py`.

> _save_marker(cfg, model, embedded=False)
> --- `src/memexos/search/qmd.py`

### Routes

#### MEM-RTE-session-distillation
Label: Session distillation and later compilation

Part of: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission)

This is the trace-to-snapshot subroute, not a replacement for the multi-channel admission container. Trigger: intake selects idle top-level sessions. Code selects by age/source/ledger and excludes known own-run paths; the model decides reading depth, reusable conclusions and admission under the five-question rubric. Inputs mix user statements, agent prose and tool outcomes. Session show abbreviates tool arguments/results, caps assistant text at 12,000 characters and compaction carry-over at 3,000, removes reminders/reasoning, and permits turn paging/result-char adjustments. The admission model authors snapshots and decisions; host scans selected outputs, normalizes headers and persists snapshots, candidates or rejection reasons. Starting intake is not human approval per content. Manual snapshots are a separate afforded person-agreement procedure, not a requirement imposed on unattended intake. SRC-1: `src/memexos/intake/sessions.py`, `src/memexos/intake/admit.py`, `src/memexos/prompts/en/admission.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: intake counts and admission outputs/ledger; show returns a requested rendering, not a retained model context.
- Later read-back: admitted snapshots enter pending_raw and compiler prompts/files, then derived wiki becomes searchable across sessions.
- Delegated visibility: worker gets session metadata and tools to request selected turns/documents; only its selected output files/decisions cross to post-processing.
- Selection predicate: time/idle/source/top-level/ledger filters followed by model value, novelty, durability, traceability and safety choices; scanner can veto admitted or uncertain text.
- Invalidation or expiry: reject retains ledger reason but no admitted snapshot; uncertain retains candidates; blocked output stays out of raw; ledger keys suppress later ordinary admission.
- Activation or effect: retained distilled knowledge can guide future compiler and answering calls; actual changed answers or improved capacity are unobserved.
- Evidence limits: snapshots need not preserve every command/outcome or correct the upstream model's unsupported claims; external host compaction is only parsed, not implemented here.

> if text.startswith("This session is being continued from a previous conversation"):
>     return "[summary carried over after context compaction] " + short(text, CONTINUED_MAX)
> --- `src/memexos/intake/sessions.py`

Admission/rejection are software/model controlled under the rule set; no expected-answer oracle or bounded experiment is established. Recovery includes manual candidate decisions and later new sources, not automatic reconstruction of omitted transcript detail. The requested reasons travel in snapshot bodies and admission reasons, but no mandatory later read of the full admission rationale is established. This is a trace-fed knowledge write, not evidence of weight learning.

#### MEM-RTE-catalog-reuse
Label: Classification and retained precedent reuse

Distinct from [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish): produces classifications and revisable category definitions rather than wiki prose. Also supplies [RT-RTE-search-get](runtime.md#rt-rte-search-get) metadata. Trigger: ensure/backlog/redo/check or explicit category decision/sync. Code builds source digest (default 2,500 characters, optional visual overview 1,200), selects URL/author precedents, taxonomy and drafts. Worker proposes fields/drafts; optional judge screen can override primary domain; registry/settle checks may refuse drafts or use fallbacks. Rows append with provenance. Later writer overrides are detected against catalog history; sync keeps selected novel page values rather than indiscriminately replacing them. SRC-1: `src/memexos/catalog/classify.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: classified count, lifecycle notes or decision result/changed paths; sync updates source frontmatter and index grouping.
- Later read-back: subsequent classifiers receive retained same-URL and same-author classifications; compiler receives batch classifications; search/get displays effective source metadata.
- Delegated visibility: classification uses a temporary context with sampled text, taxonomy/drafts and selected precedents, not full earlier classifier sessions.
- Selection predicate: up to two earlier same-URL rows and three same-author rows per new raw, plus requested raw batch; primary screen adoption and canonicalization constrain final domain.
- Invalidation or expiry: append history preserves older rows while load selects latest; expired/rejected/merged drafts cause reassignment; explicit redo and writer overrides can replace effective classifications.
- Activation or effect: selected labels/scope guidance reach later models, and symbolic fields change grouping/provisional display; reliable downstream evidence-sensitive wording is not observed.
- Evidence limits: sampled source evidence can omit decisive content; model/screen agreement is no truth oracle; full taxonomy proposal validation and screen internals are not established here.

> same = [r for r in by_url.get(str(fm.get("url") or "").rstrip("/"), []) if r["raw"] != rel][-2:]
> --- `src/memexos/catalog/classify.py`

> peers = [r for r in by_who.get(str(who), []) if r["raw"] != rel][-3:] if who else []
> --- `src/memexos/catalog/classify.py`

Admission: classifier/screen/registry control ordinary rows and draft proposals; caller decisions control official approval/merge/rejection, with human identity unresolved at the API. Mode is open classification plus thresholded draft stability checks, not correctness-tested learning. Stability threshold defaults in check are eight works, three days, 0.8 recheck retention; idle expiry default is sixty days. No independent answer oracle is supplied. Recovery is append/reassign/sync or operator revision, not automatic restoration of semantic truth. Definitions and reasons can persist, but whether these constitute theory criticism is left unestablished rather than inferred from category revision.

#### MEM-RTE-usage-repair
Label: Usage traces to repairs

Distinct cross-stage chain overlapping [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance)'s verify/fix segment and [RT-RTE-search-get](runtime.md#rt-rte-search-get)'s consumer activity; it is not a duplicate of either route. Trigger: usage judge/verify and later fix/lint, optionally scheduled according to runtime. Parser extracts question/calls/opened pages/answer from local host logs, also recognizing direct reads. Judge selects real, unjudged, answered non-follow-up events, ten per call; question/answer excerpts are capped before judging. Model judgment generates bad-page feedback or source-error records; verifier reads feedback and sources and emits review-format problems when confirmed. Fix consumes those retained problems and writes staged wiki; lint separately consumes optional usage report context. SRC-1: `src/memexos/usage.py`, `src/memexos/pipeline/compile.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: extraction/judgment/verification counts and local state; feedback CLI can report read-only failure to persist without failing its command.
- Later read-back: retained feedback enters verifier, confirmed review enters fix, report enters lint; published revisions enter search/get.
- Delegated visibility: judge gets selected question/search/open/answer excerpts, not every original tool outcome; verifier gets feedback prompt and vault read access; fix gets rendered problems/reasons.
- Selection predicate: extraction scans recent 35-day candidate logs containing relevant strings, skips own-run paths; judge selects real/non-follow-up events not previously judged; verifier selects pending feedback up to max_n; fix selects unfixed directories by ledger.
- Invalidation or expiry: failed model calls remain retryable; rejected/unsure verifier statuses no longer satisfy pending; fixed-review ledger suppresses repair replay; extraction replaces rescanned recent events while preserving older retained ones.
- Activation or effect: trace-derived problems can cause publication of revised knowledge; delivery and merge are inspectable wiring, not an observed behavioral improvement.
- Evidence limits: parsing/truncation and missing host logs can omit relevant evidence; bad-page judgments and source verification are model judgments, not an external expected-answer oracle or causal benefit measure.

> append_jsonl(d / "feedback.jsonl", fb)
> append_jsonl(d / "source-errors.jsonl", srcerr)
> --- `src/memexos/usage.py`

The verifier proposes confirmed/rejected/unsure and problems; code admits confirmed nonempty problems to fix jobs. Gates can veto the resulting writer proposal; humans need not approve each repair. Reason/source passages persist in review and reach fix through rendered problems; search/get does not automatically return the entire repair history with the page. Usage input originates in external person/agent sessions, whereas Gate 2 review is produced from the system's own draft; both can feed repair but have different trace origins. No improved capacity, full self-representation, content-directed theory revision or exercised self-improvement follows just from this chain.

#### MEM-RTE-rerank-budget
Label: Retained timing controls retrieval budget

Distinct from [RT-RTE-search-get](runtime.md#rt-rte-search-get)'s request progression: a trace-fed local policy-state update used by later calls. Identity of retained result: `rerank-speed.json` per_doc/load_ms, symbolic numerical scalar data in local state, not neural weights or knowledge text. Trigger: qmd rerank with rank_ms and positive candidate count. Code estimates seconds per document, smooths equally with an older estimate, persists it best effort, and reads it to choose the next head budget. Human per-update approval is not required. SRC-1: `src/memexos/search/rerank.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reranked head plus untouched tail, or original fused order on failure.
- Later read-back: _speed loads per_doc on later searches; budget_k uses configured seconds divided by estimate to select how many candidates to rerank.
- Delegated visibility: qmd receives question and bounded candidate passages; timing scalar, not prior semantic judgments, crosses calls.
- Selection predicate: first run min(k, 8); measured budget uses max(5, min(k, int(budget / per))); passage is initial 1,500 body characters plus matched snippet up to 600.
- Invalidation or expiry: unreadable/missing estimate uses first-run behavior; successful timing overwrites/smooths state; no TTL is established by this file.
- Activation or effect: persisted timing can change future number of reranked candidates and hence ordering; six seconds is a default budget target, not a hard runtime guarantee.
- Evidence limits: no measured latency or answer-quality improvement supplied; read-only environments may skip persistence; scalar history does not retain explanatory rationale.

> per = per if old is None else 0.5 * old + 0.5 * per
> --- `src/memexos/search/rerank.py`

This is automatic admission of operational measurements, not model-selected knowledge or theory criticism. Recovery is fallback ordering/default budget; no answer oracle applies to the timing estimate. The source implements a future control dependency but supplies no observed activation or causal benefit.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Read-back is supplied by [MEM-OBJ-wiki](#mem-obj-wiki), not by Git history alone. Raw/session sources can themselves already be derived. Review/rework retains criticisms in [MEM-OBJ-review](#mem-obj-review); fixed/held state changes future selection rather than semantic content. Writer authors; program merges; neither makes publication a human per-content decision. Discard/hold do not delete the original raw source; a held branch is retained draft, not ordinary searchable live knowledge. Direct stage inspection confirms separate branch payload and shortened blocked-report display (SRC-1, `src/memexos/pipeline/stage.py`):

> body = i18n.t("hold.entry", time=time.strftime("%H:%M:%S"), branch=self.branch, reason=reason, files=files,
>               base=self.base[:7], vault=self.vault) + f"\n\n```\n{report[-4000:]}\n```\n\n"
> --- `src/memexos/pipeline/stage.py`

#### On [RT-RTE-search-get](runtime.md#rt-rte-search-get)

Direction: the caller requests a question/keywords or page; internal automatic ranking is selection within that request, not an unsolicited memory push. Search is not limited to compiled wiki. Direct source inspection adds the CLI's transformation: engine requests a.n + 6 hits; detail reads up to 400,000 characters, computes classification/source counts/snippets; dedupe drops raw when the matching compiled source page is in the hit set, then truncates to a.n (default eight). Text display clips snippet to 160 characters; JSON keeps the computed snippet. Source counts and classification are access/trust cues, not the supporting passages themselves. Get defaults to all lines and supports --from/--lines; name lookup prefers wiki stems over raw, but explicit existing contained paths can select other vault files. Actual final answer reliance remains unobserved. SRC-1: `src/memexos/search/cli.py`.

> return [h for h in hits if not (h.get("compiled_page") and f"wiki/sources/{h['compiled_page']}.md" in paths)]
> --- `src/memexos/search/cli.py`

#### On [RT-RTE-backend-execution](runtime.md#rt-rte-backend-execution)

Working-context isolation keeps admission, classification, writer and reviewer calls separate; files/reports are the selected cross-call result, not shared hidden-state memory. The supplied runtime establishes fresh API message lists, output caps and reviewer diff truncation/reload access. This resembles a frame whose selected results escape, but not a reference-counted memory heap: copied prompt text is by value, and file reachability does not establish relevance or live model awareness. Underlying CLI compaction remains opaque. No extra claim of an internally implemented summary/replay path is made (SRC-1 paths and supporting passages in the supplied route and runtime account).

#### On [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance)

Separate retained inputs matter: raw feedback files enter correct; local usage feedback enters verify then review-format fix; inbox decisions enter apply. These are not one undifferentiated memory store. Correct can remove its transient correct-results.json before publishing and mark feedback corrected; the event retains outcomes, while the changed wiki remains the answering consumer's content. Direct maintenance source supports the transient/persistent distinction (SRC-1, `src/memexos/pipeline/compile.py`):

> results_file.unlink(missing_ok=True)            # results are for the program, not the vault
> --- `src/memexos/pipeline/compile.py`

## Write side

### Acquisition and admission

[MEM-RTE-session-distillation](#mem-rte-session-distillation) is an automatic trace-fed knowledge write: model-selected conclusions become immutable-source input and then mutable wiki knowledge. The host parser's compact rendering is an intermediate read representation, not by itself an adopted memory artifact. Upstream host compaction summaries are an alternative trace form, not evidence that MemexOS authored those summaries. The manual session-snapshot procedure asks person agreement, whereas unattended intake uses model decisions plus scanner veto. That counterexample prevents classifying all snapshot admission as human controlled.

For [MEM-OBJ-raw](#mem-obj-raw), direct capture uses request plus body scrubbing/header validation. Document copy paths use allowed roots, suffix/size checks and selected text scanning; HTML can retain original and extracted text separately. Binary copy, video/visual lower layers and external plugins prevent a universal text-scan guarantee. Authorship, physical copying and admission are separate operations. Classification supplies later interpretation metadata, not initial truth validation ([MEM-RTE-catalog-reuse](#mem-rte-catalog-reuse)).

### Transformation, maintenance and withdrawal

[MEM-OBJ-wiki](#mem-obj-wiki) is automatically authored/revised under conditional checks, not approved line by line by its owner. [MEM-OBJ-review](#mem-obj-review) and [MEM-RTE-usage-repair](#mem-rte-usage-repair) preserve targeted reasons and deliver them to later writers, establishing more than passive log retention. However later retrieval generally supplies page text and source pointers, not the full criticism chain. A trace-fed artifact update is established; improved future action and causal benefit are not.

Catalog precedents and revised taxonomy definitions also shape later proposals. [MEM-RTE-catalog-reuse](#mem-rte-catalog-reuse) separates automatic row/draft admission from explicit category decisions. Writer-overridden metadata can survive sync, so catalog history is not the only authority on display. Unknown initialization control does not erase these subsequent transformations.

Rejection is local to a path: admission reject keeps reasons, uncertain keeps candidates, scanner block excludes output, gate failure can hold a branch, service unavailability can discard, feedback verification can decline a reported error, draft taxonomy expiry rehomes members, and lint ages out top-level inbox reports. These do not amount to a universal forgetting operation. Raw append-only doctrine, Git history and current-file selection have distinct horizons. FTS removes disappeared paths at refresh; qmd removal behavior inside its external update remains uninspected. A source or page withdrawn outside these flows has no established immediate all-index purge guarantee ([MEM-OBJ-fts](#mem-obj-fts), [MEM-OBJ-vectors](#mem-obj-vectors), [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)).

## Read-back

Ordinary answering uses the shipped search → get → cite instruction and the wired returning CLI. The requester chooses the question, optional keywords/mode and subsequent page; code selects candidates, fusion order, reranking, inbox filter, deduplication and final budget. Ranking models see bounded passages, not necessarily the relevant tail of a page. Raw can be returned independently of wiki compilation. Displayed classification is guidance about evidence use, not an enforced answer policy ([RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages), [RT-RTE-search-get](runtime.md#rt-rte-search-get)).

Write-side read-back has different consumers: ledger sets suppress repeated work; taxonomy/catalog histories guide classifiers and sync; raw snapshots guide compilers; review/feedback reasons guide fix/correct; usage summaries guide lint. [MEM-RTE-rerank-budget](#mem-rte-rerank-budget) reads measurement history to adjust future selection cost. None is inferred from the mere existence of a store: each has an identified caller. API tools afford further requested file reads; opaque provider context-management behavior is not promoted to an inspected route.

Context control occurs before and within calls: session paging/reminder removal/result abbreviation, classifier digests/precedents, distinct writer/reviewer scopes, report rendering, usage excerpts, search snippets/rerank passages and explicit get slicing. Files remain reachable for a later request even when omitted from a prompt. Invocation-local tool accumulation is not automatically long-term memory; selected summaries/files that reach later calls are. There is no claim that a stored artifact necessarily occupies, or is live in, a later model window.

## Integration issues

- No supplied runtime finding requires correction on the inspected evidence. Search's raw path, gate-off exception, publication/index lag and human-approval limits survive attempted counterexamples. The added CLI deduplication and classification override details refine, rather than contradict, its account.
- Explicit parts: [MEM-OBJ-wiki](#mem-obj-wiki) and [MEM-OBJ-inbox](#mem-obj-inbox) are content parts of [RT-OBJ-stage](runtime.md#rt-obj-stage); [MEM-RTE-session-distillation](#mem-rte-session-distillation) is part of [RT-RTE-source-admission](runtime.md#rt-rte-source-admission). They must not replace their larger workspace/admission containers.
- Possible overlap requiring reconciliation: [MEM-RTE-usage-repair](#mem-rte-usage-repair) spans trace extraction/judge plus the verify/fix segment already in [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance). Preserve the distinct trace-origin and raw-to-derived chain; no automatic identity/supersession is asserted. [MEM-RTE-rerank-budget](#mem-rte-rerank-budget) is an update loop within search, not another declaration of the search request route.
- Retained vectors versus model parameters: [MEM-OBJ-vectors](#mem-obj-vectors) and [RT-CMP-qmd](runtime.md#rt-cmp-qmd) must stay separate. qmd chunk/embedding provenance and internal removal are uninspected; preventing mixed-model queries at every possible configuration transition is not established by its marker alone.
- Included unresolved parts: media/frame/ASR transformations, full taxonomy screen/propose validation, inbox research-cache transformations, localized prompt equivalence and evaluator-specific retained artifacts are not fully inspected. Their named coverage rows prevent complete all-route safety, context completeness or evaluator-driven improvement conclusions; they do not negate the positive source-supported routes here.
- [MEM-OBJ-taxonomy](#mem-obj-taxonomy) retains revisable definitions and rationale, but this report does not establish formulated-theory criticism/iteration from stability scores or category changes. [MEM-RTE-usage-repair](#mem-rte-usage-repair) establishes repair wiring, not demonstrated learning, reflection or exercised self-improvement. Any stronger independent mapping needs its own content and causal evidence.

## Limitations and checks

The source HEAD was rechecked as bb9e9b2ac0adbca87d13a9f7600867128b5f71b9. Reads stayed within the registered source and supplied members; no new source identity or method substitution was introduced. The complete invocation, contracts and supplied members were read with truncated delivery recovered before further analysis. No target execution or dependency installation occurred.

The findings are implementation wiring and attributed doctrine, not observed use or causal experiments. External host logs, models and services have opaque or unavailable operational state. Available but uninspected source branches remain named in coverage rather than recast as absences. No quantitative quality, successful security enforcement, instruction compliance, model training, reliable truth improvement or complete withdrawal guarantee is asserted.

Validation: the required role-specific commonplace-validate command passed with no errors. Deterministic validation checks form and quote occurrence, not semantic completeness or acceptance.
