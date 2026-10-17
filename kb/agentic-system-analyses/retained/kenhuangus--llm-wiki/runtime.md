---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM Wiki runtime baseline: ingestion, retained-content consumption, alternate drivers and incomplete prompt-change admission at the frozen Git boundary."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
---

# LLM Wiki runtime report

## Runtime account

### Evidence and control model

This account uses SRC-1 at the revision fixed in [the boundary](boundary.md#boundary-and-evidence). It inspects implementation and shipped doctrine, not an executed deployment. No target program or test was run. Operation, model compliance, improvement and performance remain unobserved. Additional detailed coverage within the registered repository includes `tools/prompts.py`, `tools/prompt_optimizer.py`, `tools/research_agent.py`, `tools/retrospective_validator.py`, `tools/lint.py`, `tools/newsletter_agent.py`, `tools/curated_monitor.py`, `tools/cve_monitor.py`, the relevant generation and critique methods in `tools/paper_agent.py`, and the long-form orchestration override in `tools/paper_agent_long.py`. These provide implementation or doctrine/design evidence, not new sources or run evidence.

LLM Wiki is principally a set of Python-controlled file-processing workflows. Models return text or JSON; Python determines stage order, paths, schedules, parsing and writes. The production model client sends two messages and consumes a completion, rather than exposing a model-driven tool-dispatch loop. The principal is the invoking OS process, API caller or daemon operator; an authenticated end-user identity is not propagated through the inspected pipeline. Source IDs identify ingested material, not an actor's authority. The externally served models are separately identified in [RT-CMP-main-model](#rt-cmp-main-model) and [RT-CMP-openrouter-model](#rt-cmp-openrouter-model). Neither model receives an explicit tool grant in this client (SRC-1: `tools/common.py`, `tools/extract.py`, `tools/integrate.py`, `api_server.py`).

### Ordinary invocation, end to end

A concrete shipped ordinary invocation is `python tools/pipeline_all.py` from the repository root. It polls arXiv, CVE, GitHub, RSS and curated monitors using subprocesses; recursively discovers files under `raw/auto_ingest/` and `raw/manual/`; normalizes them; extracts only normalized Markdown without a JSON sidecar; integrates every discovered sidecar; and rebuilds `wiki/index.md`. The next-step owner throughout is the batch driver, not the model ([RT-RTE-batch-ingestion](#rt-rte-batch-ingestion)). An operator may first use `tools/ingest.py` to copy a file or download an HTTP(S) URL. Its dated destination-name existence check is distinct from monitor SQLite deduplication (SRC-1: `tools/pipeline_all.py`, `tools/ingest.py`, `tools/common.py`).

Normalization extracts PDF text or reads UTF-8, hashes content to eight hexadecimal characters, and writes Markdown with YAML metadata under `raw/normalized/<domain>/`. Empty/unreadable sources return without a failing process exit. Extraction strips frontmatter, passes the entire body with a shipped extraction instruction, parses JSON, adds the normalized source ID and writes `<normalized>.md.json`. JSON parsing is a real gate, but it is not a schema, factual-evidence or confidence-range validator. Integration consumes only claim text/confidence plus source ID for its claim body: extracted entities, relationships and evidence sentences are not automatically delivered to the merge call. A new destination writes those claims without a merge-model call. An existing destination supplies the old body and new claims to a merge model, accepts any nonempty result, recognizes a conflict marker, or appends claims if the call returns empty. It then directly rewrites Markdown and logs the operation (SRC-1: `tools/normalize.py`, `tools/extract.py`, `tools/integrate.py`; [RT-RTE-knowledge-admission](#rt-rte-knowledge-admission)).

> extracted = json.loads(content_out)
> --- `tools/extract.py`

> input_text = f"Old Claims:\n{exist_body}\n\nNew Claims:\n{new_claims_body}"
> --- `tools/integrate.py`

The output is persisted wiki pages, normalized files, JSON sidecars, a catalog and log entries, not a returned conversational answer. Subsequent search rereads Markdown and constructs BM25 over lowercased whitespace tokens on each request. `index.py` builds a Markdown catalog, not the persistent search index implied by the batch driver's “semantic BM25 index” message. The API returns up to five positive-score paths with snippets; article requests return full files. Neither query nor article delivery filters out conflict or unverified pages (SRC-1: `tools/query.py`, `tools/index.py`, `api_server.py`; [RT-RTE-wiki-consumption](#rt-rte-wiki-consumption)).

### Material alternate paths and forcing cases

Four forcing cases test broader claims rather than treating the batch path as universal:

1. **Existing page, empty or unconstrained model output.** History preservation and conflict handling are prompt requests. A nonempty completion replaces the body without checking that old claims survived. An empty completion instead appends new claims. Metadata starts with confidence 0.8, verified false and current status; only old ID/source count are explicitly retained before the optional conflict marker changes status. Therefore even an earlier conflict status is not a hard admission barrier. This falsifies a runtime invariant of preserved history or conflict-paused ingestion (SRC-1: `tools/integrate.py`, `tools/prompts.py`; [RT-RTE-knowledge-admission](#rt-rte-knowledge-admission)).
2. **Critical CVE through alternate drivers.** The CVE monitor writes an alert for scores at least 9 and still invokes its immediate pipeline for scores at least 7. Its output is `security/cve/<title>.md`; the batch driver can subsequently integrate the sidecar elsewhere. The daemon instead routes all integrations to `concepts/agentic-ai/test-integration.md`, regardless of detected domain. It writes its critical alert after processing rather than waiting for human approval. The unified daemon calls source-processing methods, not `WikiDaemon.run()`, so the latter's periodic lint/index scheduling is not inherited. These are different control paths and destinations (SRC-1: `tools/cve_monitor.py`, `tools/daemon.py`, `tools/unified_daemon.py`; [RT-RTE-scheduled-drivers](#rt-rte-scheduled-drivers)).
3. **Browser/API edit and upload.** A user can bypass extraction and merge prompts by posting article content. The React save handler supplies the editor text; the API writes it directly. Upload writes bytes under `raw/manual/`; URL ingestion schedules a background pipeline and returns before processing. The watcher and API select a newest normalized file, unlike the daemon's output-path parsing. Concurrent or unsuccessful normalization can therefore break the assumed input/output association; no execution of that case is established (SRC-1: `ui/src/App.jsx`, `api_server.py`, `tools/watchdog_monitor.py`; [RT-RTE-api-mutation](#rt-rte-api-mutation)).
4. **Optimizer rejection after no actual prompt installation.** A proposed prompt is generated, but `commit_prompt_change` neither writes it nor switches `ACTIVE_PROMPTS`. Evaluation launches the existing extraction script on at most ten fixtures. Rejection runs `git reset HEAD~1`, even when the attempted commit returned no hash. This is not restoration of a candidate prompt, and a default mixed reset does not restore working-tree file contents. It can move unrelated history/index state. A “KEPT” experiment is not evidence that the proposal entered later extraction (SRC-1: `tools/prompt_optimizer.py`, `tools/prompts.py`; [RT-RTE-prompt-optimization](#rt-rte-prompt-optimization)).

A manual-drop watcher observes newly created files nonrecursively, waits one second, and runs subprocess stages with repository-root cwd. It stops after failed normalize/extract subprocesses, but does not stop on a failed integrate before attempting index and logging completion. The batch driver likewise ignores `run_command`'s false results at its call sites and ends with a success-labelled log. The API catches background pipeline exceptions without turning the earlier queued response into completion evidence. These are best-effort workflows, not a transaction spanning artifacts (SRC-1: `tools/watchdog_monitor.py`, `tools/pipeline_all.py`, `api_server.py`).

### Guarantees, grants and external contracts

| Load-bearing expectation | Owner/enforcement point, coverage and counterpath | Strength and statuses | External contract |
|---|---|---|---|
| Structured extraction | `extract_knowledge` requires JSON parsing before sidecar write; merge output, API edits and newsletters bypass that gate; no full schema validation there | guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected | Model must supply usable claims/fields, not merely parseable JSON |
| Preserve attribution, history and conflicts | Merge prompt requests preservation; Python recognizes `STATUS: CONFLICT`, but does not verify preservation or block writes; new pages and direct edits do not traverse merge judgment | guarantee strength: policy; implementation conclusion status: claimed; operation conclusion status: uninspected | Model must interpret and follow rules; human review must happen externally |
| Human escalation | CVE monitor/daemon write alert files; catalog lists pending review; these are notifications rather than pre-write approval gates | guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected | A human or host must notice, review and act |
| Local inference | Main endpoint tried up to four times; context-error text can shortcut to OpenRouter; configured backup local model is not used by this function | guarantee strength: no claimed guarantee; implementation conclusion status: wired; operation conclusion status: uninspected | Primary or cloud provider availability, response contract and confidentiality |
| Article containment | API read/save/history use normalized-path string-prefix tests; upload, ingest-domain and integrate-path construction have different controls. Prefix equality is not path-component containment and does not resolve symlinks | guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected | Host filesystem permissions and deployment exposure; no proven sandbox boundary |

These scoped findings are grounded in SRC-1: `tools/extract.py`, `tools/prompts.py`, `tools/integrate.py`, `tools/cve_monitor.py`, `tools/daemon.py`, `tools/index.py`, `tools/common.py`, `api_server.py`. No exploitation or isolation test was performed.

The **capability surface** includes filesystem writes, URL/feed requests, subprocess launch, Git history reads and optimizer Git index/history mutation. The **current grant set** cannot be reconstructed without the operator's environment, provider keys and OS permissions. The **deployed isolation envelope** is also unobserved. The shipped API main binds loopback, but this is not proof about another ASGI deployment. It configures wildcard CORS and no authentication dependency on the inspected endpoints. Subprocesses inherit host authority; use of argument lists does not constitute a sandbox. There is no inspected model-native shell/tool dispatch in the production helper, but diagnostic provider requests and arbitrary externally operated coding-agent hosts are not thereby constrained by it (SRC-1: `api_server.py`, `tools/common.py`, `tools/daemon.py`, `tools/prompt_optimizer.py`, `AGENTS.md`).

### Context, recovery and improvement boundaries

Each helper call builds a fresh system/user pair. There is no turn-history accumulator to compact in this client. Code selects what crosses invocations: extraction drops frontmatter; merge includes the old body and a reduced new-claim projection; paper analysis selects at most five matching pages and delivers their first 2,000 characters; critique delivers only the first 20,000 draft characters and passes the improved draft, not necessarily the review, to the next round. Newsletter delivery selects at most five entries per bucket with 400-character snippets. These are code-controlled context filters with files still available for later reads, not a proven semantic summarization guarantee. Separate calls resemble frames with only a completion escaping; unlike references into shared memory, the supplied text is copied and omitted content has no automatic reachability inside the model window (SRC-1: `tools/common.py`, `tools/extract.py`, `tools/integrate.py`, `tools/paper_agent.py`, `tools/newsletter_agent.py`).

Recovery is local: model retries/fallback, subprocess timeouts in daemon paths, exception logging, and low-priority requeue on exceptions escaping `process_source`. Explicit extract/integrate failure returns do not take that requeue branch. Queues/counters/schedule timestamps are in memory, while source deduplication, sidecars, wiki files and metrics survive independently. `scan_auto_ingest` checks a sidecar next to the raw file even though normal extraction writes next to the normalized file; repeated scans may enqueue the same raw source. No inspected multi-artifact commit/lock makes these stages atomic, and CLI paths with relative `tools/...` arguments require a suitable cwd (SRC-1: `tools/common.py`, `tools/daemon.py`, `tools/pipeline_all.py`).

Production changes are admitted in distinct ways: automated claim writes; direct caller edits; model-assisted deep-lint tags; deterministic retrospective metadata updates; synthesis writes; and the incomplete optimizer proposal/evaluation path. Their owners, vetoes, modes and oracles are recorded below. Research “SUCCESS” can mean only producing a query or identifying a task; paper external search returns a placeholder. None of those labels establishes a completed research experiment, validated knowledge gain or improved operational capacity (SRC-1: `tools/research_agent.py`, `tools/paper_agent.py`, `tools/prompt_optimizer.py`; [RT-RTE-research-maintenance](#rt-rte-research-maintenance)). Memory-specific revision analysis is left to the memory member.

## Shared records

### Components

#### RT-CMP-main-model
Label: Configured primary inference model

Source-native identity: `LLM_MAIN_URL`, `LLM_MAIN_MODEL`, `LLM_MAIN_API_KEY` in SRC-1: `tools/common.py`. Representational form: distributed-parametric model behind a text chat-completions interface. Storage substrate: external model-server weights and serving infrastructure, not the wiki filesystem. Default model string is `google/gemma-4-26b-a4b:3`; environment can override it. Exact weights/version are not pinned by this repository. The endpoint can serve a different model after configuration or server changes. No parameter-update operation is sent by the inspected client; provider-side parameter changes and state are uninspected, not proven fixed.

> LLM_MAIN_MODEL  = os.environ.get("LLM_MAIN_MODEL", "google/gemma-4-26b-a4b:3")
> --- `tools/common.py`

#### RT-CMP-openrouter-model
Label: Configured cloud fallback model

Source-native identity: `OPENROUTER_URL`, `OPENROUTER_MODEL`, `OPENROUTER_API_KEY` in SRC-1: `tools/common.py`. Representational form: distributed-parametric; storage substrate: external provider. Default name `anthropic/claude-3.5-sonnet` is a configurable provider identifier, not a weight digest or exact immutable version. A mutable endpoint/provider mapping can resolve to another model. No client-side training/update request is present in the helper; provider internals, parameter mutability during service and opaque retained state remain uninspected.

> cloud_node = (OPENROUTER_URL, OPENROUTER_MODEL, OPENROUTER_KEY, "OpenRouter (Cloud)")
> --- `tools/common.py`

### Operative objects

#### RT-OBJ-prompts
Label: Extraction and integration instructions

Source-native identity: extraction/integration string constants in `tools/prompts.py`. Natural-language rules interpreted by the model; storage substrate is tracked Python source loaded into process memory. They prescribe evidence, confidence, attribution and merging. Distinct symbolic operative part: the `ACTIVE_PROMPTS` dictionary and accessor lookup choose named constants by fixed Python rules. Selection is process-local; the setter does not persist a source edit. Both parts are declared here because they have different consumers and mutability, not because a dictionary turns instruction meaning into symbolic enforcement (SRC-1: `tools/prompts.py`).

> ACTIVE_PROMPTS = {
>     "extraction": "EXTRACTION_PROMPT_V1",
>     "integration": "INTEGRATION_PROMPT_V1"
> }
> --- `tools/prompts.py`

#### RT-OBJ-metrics
Label: Operational evaluation metrics

Source-native identity: `MetricsCollector`, extraction records and prompt experiments. Symbolic rows/columns in SQLite `metrics.db`; human-readable experiment notes are also appended to `wiki/experiments.md`. Failures are queried over 24 hours and baseline aggregates over seven days, with hardcoded fallbacks when aggregates are falsey. These records influence optimizer proposal selection and comparisons; model-assigned confidence is not an independently adjudicated correctness label (SRC-1: `tools/metrics_collector.py`, `tools/prompt_optimizer.py`).

> avg_confidence = cursor.fetchone()[0] or 0.72
> --- `tools/metrics_collector.py`

### Routes

#### RT-RTE-model-call
Label: Completion request and fallback

Endpoints/progression: Python caller → primary HTTP chat completion → optional OpenRouter → returned string or empty string. Owner: `call_local_model`; retries and provider selection are symbolic code, instructions/input are natural language. Context is a fresh system/user message pair, temperature 0.7 and max_tokens 30000; primary timeout is 180 seconds per attempt. Context/size/exceeded error text triggers early fallback; other failures allow up to four primary attempts with two-second waits. Configured `LLM_BACK_*` values are not selected here. Consumer components are [RT-CMP-main-model](#rt-cmp-main-model) and [RT-CMP-openrouter-model](#rt-cmp-openrouter-model). SRC-1: `tools/common.py`.

- Immediate return: First nonempty completion content, or empty string after failure/no cloud key.
- Later read-back: inapplicable — the helper itself saves no completion or conversation; callers own persistence.
- Delegated visibility: The selected primary provider receives both messages; fallback can deliver the same input to a cloud provider.
- Selection predicate: Primary first; error/empty result/retries then fallback if a cloud key exists.
- Invalidation or expiry: Per-call messages discarded by client return; provider retention is uninspected.
- Activation or effect: HTTP inference request is wired; successful content steers downstream parsing/writing only through each caller.
- Evidence limits: No live response, latency, confidentiality, provider-state or compliance evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> {"role": "system", "content": system_prompt},
> {"role": "user", "content": input_text}
> --- `tools/common.py:141-152`

#### RT-RTE-batch-ingestion
Label: Batch source-to-wiki driver

Endpoints/progression: monitor subprocesses/raw files → normalized Markdown → extraction sidecars → integration → catalog/log. Owner: `pipeline_all.main`; principal is CLI OS process. Domain derives from parent directory; category is entities for github/cve, concepts otherwise; title derives from sidecar basename. State includes path existence and output artifacts; selection is symbolic, extraction/merge use model interpretation. Trigger is explicit CLI launch, operating mode an open source-processing batch, not a controlled experiment. Software admits artifacts without per-item human approval. Failure can reject a stage, but the batch continues; no aggregate rollback is implemented. SRC-1: `tools/pipeline_all.py`, `tools/normalize.py`, `tools/extract.py`, `tools/integrate.py`.

- Immediate return: Console progress and final completion log after subprocess attempts; no aggregate success object.
- Later read-back: JSON existence suppresses later extraction; every sidecar can be reintegrated; old wiki body reaches later merge calls.
- Delegated visibility: Monitor processes receive configuration; extraction/merge subprocesses receive paths and providers receive selected text via [RT-RTE-model-call](#rt-rte-model-call).
- Selection predicate: All discovered raw files; normalized Markdown lacking a sidecar for extraction; all JSON sidecars for integration.
- Invalidation or expiry: No sidecar freshness/content invalidation check or integrated marker in this driver.
- Activation or effect: Direct artifact creation/rewriting and catalog rebuild are wired; model meaning changes remain unobserved.
- Evidence limits: Completion labels do not establish successful stages, idempotence or trustworthy output.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # For simplicity, we just integrate. integrate.py handles deep merging.
> --- `tools/pipeline_all.py`

#### RT-RTE-knowledge-admission
Label: Extraction and claim admission

Endpoints/progression: normalized body → requested JSON → parsed sidecar → new claims → optional merge with existing body → wiki page overwrite. Owners: extraction/integration Python functions; model proposes claim and merge content; code decides parseability, destination and nonempty-result acceptance. The caller supplies category/subcategory/title, not a demonstrated per-content human veto. Guidance is [RT-OBJ-prompts](#rt-obj-prompts); normalized IDs and source citations persist, but integration omits extracted evidence/relationships/entities from its constructed body. Operating mode is open ingestion. Answer oracle: none independent; model evidence/confidence judgments are not expected-answer references. Trigger is a stage invocation; proposed change is retained claims or merged body. Rejection is JSON parse failure or runtime exception, not substantive review. Empty merge falls back to append; direct file writes provide no transactional rollback. SRC-1: `tools/extract.py`, `tools/integrate.py`, `tools/prompts.py`.

- Immediate return: Sidecar/page write plus log and console message; extraction parsing failure exits nonzero.
- Later read-back: Existing destination body is supplied as old claims in later integrations and wiki consumers reread saved Markdown.
- Delegated visibility: Provider sees normalized body for extraction, and old body plus formatted claims for merge; not the complete extraction object.
- Selection predicate: Target existence chooses model merge versus direct initial write; any nonempty merge text is accepted.
- Invalidation or expiry: Destination is overwritten; source count increments per integration, not independently verified distinct evidence.
- Activation or effect: Writes are wired; preservation, correct contradiction detection and resulting behavioral benefit are not observed.
- Evidence limits: Model-requested rules do not establish compliance; arbitrary parsed JSON can fail later field access.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if merged_body_raw:
>     if "STATUS: CONFLICT" in merged_body_raw:
>         metadata['status'] = 'conflict'
> --- `tools/integrate.py`

#### RT-RTE-scheduled-drivers
Label: Daemon and immediate source drivers

Endpoints/progression: monitor polls → raw-file priority queue → stage subprocesses → fixed daemon destination; CVE monitor additionally invokes its own immediate pipeline; watcher handles manual creates; unified daemon schedules further components. Owners are code schedulers, with model roles confined to called stages. PriorityQueue stores `(priority, source_path)` in memory; CVSS heuristics choose critical/high/default priority. Daemon processes at most ten entries per cycle. Unified periods are four-hour optimization, six-hour research, weekly validation and fortnightly paper generation; zero initial timestamps make tasks initially due. It does not call the base daemon's lint/index loop. Trigger is launch followed by polls/time/file events, with no per-item human approval gate. Alert output is advisory, not a veto. Recovery is timeout/error handling and limited exception requeue, not durable queue restoration. SRC-1: `tools/daemon.py`, `tools/unified_daemon.py`, `tools/watchdog_monitor.py`, `tools/cve_monitor.py`.

- Immediate return: Continuous service until shutdown; per-source console/log/metrics outputs; watcher returns after stage attempts.
- Later read-back: Monitors consult shared deduplication state; scan/path checks, normalized files and wiki bodies affect later cycles.
- Delegated visibility: Subprocesses receive file paths; providers receive stage inputs; critical alert files target a human with no delivery acknowledgment.
- Selection predicate: CVSS/source-path priority and scan sidecar checks; watcher created-file event; CVE thresholds at 7 and 9; unified elapsed-time rules.
- Invalidation or expiry: Queue/schedule state lost on restart; persisted artifacts/dedup state have separate lifetimes.
- Activation or effect: Scheduling, integrations, metrics and alert writes are wired; notification uptake and successful continuous operation unobserved.
- Evidence limits: Different destination and scheduling behavior prevents treating all drivers as one equivalent loop.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> [sys.executable, 'tools/integrate.py', json_path,
>  'concepts', 'agentic-ai', 'test-integration'],
> --- `tools/daemon.py`

#### RT-RTE-api-mutation
Label: API and browser mutation

Endpoints/progression: React editor → article POST → direct Markdown overwrite; upload → raw/manual bytes; ingest request → background download/normalize/extract/integrate/index. Owner: API handlers/background task; React human supplies editor text, but arbitrary API caller identity remains unresolved. Trigger is request submission. Human authorship of a browser edit differs from software admission: backend applies no content approval, merge or source-trust review. User can choose not to submit; backend can reject its path check or fail I/O, with no automatic rollback. Git endpoints read history rather than making saves into commits. The runtime-client boundary is HTTP/JSON, Pydantic URL-list/domain input and inherited server filesystem/network authority. SRC-1: `api_server.py`, `ui/src/App.jsx`.

- Immediate return: Save/upload success responses, or queued-source count before background completion; reads return content/history/results.
- Later read-back: Saved text is read by article/search and later model consumers; uploaded files can enter batch/watcher processing.
- Delegated visibility: Browser receives full article/edit content; ingestion subprocesses and providers receive selected source content.
- Selection predicate: Requested article path; ingest domain/URLs; newest raw and normalized files selected by mtime during background processing.
- Invalidation or expiry: Save overwrites content; no built-in version checkpoint or expiry; history depends on externally existing Git commits.
- Activation or effect: Caller-supplied content bypasses model admission and is wired to durable file effects.
- Evidence limits: No authenticated principal, live-server test or deployed exposure established; string-prefix path checks are not comprehensive isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> with open(target, 'w', encoding='utf-8') as f:
>     f.write(content)
> return {"status": "success"}
> --- `api_server.py`

#### RT-RTE-prompt-optimization
Label: Prompt proposal and metric ratchet

Endpoints/progression: recent extraction failures/baseline → rule-selected hypothesis → model-generated prompt → attempted Git commit → existing extractor on first ten available fixtures → threshold decision → log or reset. Owner/proposer: code selects failure focus, model proposes wording, code thresholds decide keep/reject; no human review in cycle. Guidance asks targeted improvements while maintaining structure/rules. Proposed content is not installed or retained as a new active prompt by `commit_prompt_change`. It stages the existing prompts file and commits the repository index; commit failure does not abort evaluation. Evaluation `prompt_type` does not switch the active prompt. Rejection invokes reset independently of a successful candidate commit. A keep updates in-memory baseline before logging, so logged baseline fields can already equal new metrics. SRC-1: `tools/prompt_optimizer.py`, `tools/prompts.py`, `tools/metrics_collector.py`.

Operating mode: bounded fixture evaluation, triggered manually or by unified schedule. Answer oracle: process success/JSON load and self-reported confidence aggregates, not independent expected answers. Conflict rate is set to zero without integration evaluation. Thresholds reward confidence/validity/conflict deltas with tolerances; this does not isolate a proposal's effect because its installation link is missing. Human veto is external intervention only; code rejection exists but its recovery is Git history/index movement rather than demonstrated prompt restoration.

- Immediate return: Boolean keep decision with experiment log, or false when generation fails.
- Later read-back: Metrics feed future failure focus/baseline/count; active prompt text remains selected from shipped registry unless changed externally.
- Delegated visibility: Generator gets current prompt and selected hypothesis, not a full raw-failure transcript; fixture extractors use their own imported prompt registry.
- Selection predicate: More than five failures targets JSON; CVSS error among fewer failures targets extraction; otherwise confidence improvement. First ten fixture records bound evaluation.
- Invalidation or expiry: Recent-failure/baseline time windows; failed decisions reset HEAD but do not implement safe candidate rollback.
- Activation or effect: Generation/evaluation/decision/log/Git side effects are wired; candidate-to-live-prompt activation is not wired in the inspected method.
- Evidence limits: No observed optimization; a keep label or metric delta establishes neither installed prompt change nor better extraction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # For now, just log the change (full implementation would modify prompts.py)
> --- `tools/prompt_optimizer.py`

> 'conflict_rate': 0.0,  # Would need integration test
> --- `tools/prompt_optimizer.py`

> ['git', 'reset', 'HEAD~1'],
> --- `tools/prompt_optimizer.py`

Theory assessment boundary: the prompt-method proposal/evaluation route, not opaque model reasoning. The localized method text is individually readable and replaceable; named rules provide finer addressability than a whole opaque model, but the updater requests whole-prompt replacement. Theory-builder conditions 1–4: condition 1 conclusion status: wired — explicit prompt rules state a method; condition 2 conclusion status: wired — current prompt content is sent to generation/extraction consumers, while candidate consumption is not wired; condition 3 conclusion status: uninspected — generated content-directed criticism is not supplied, and score-based keep/reject is not itself claim/blame-directed criticism; condition 4 conclusion status: uninspected — no retained criticism-to-next-method iteration is demonstrated. Persistence: metrics/experiment notes survive runs; the new prompt proposal is not saved by this implementation. Learning: uninspected — no improved future capacity or attribution evidence. Reflection: metrics represent extraction behavior and shape subsequent proposal focus, but proposed prompt text is not installed; no complete method-revision feedback is established. Reflective theory builder: uninspected for conditions 3–4. Autonomous theory builder: uninspected for those internal operations, although scheduling/proposal/evaluation steps have computational owners.

Self-improvement assessment: objective is better extraction confidence/validity and fewer conflicts over repeated optimizer cycles in the shipped workflow. Failure evidence can shape a proposal (link 1 wired). Link 2, installation into behavior-determining prompts, is missing in `commit_prompt_change`; link 3 for that candidate and link 4 of subsequent dependence are consequently unestablished. Actual or successful self-improvement cannot be attributed. This does not negate the independent retained-metrics feedback or wiki read-back paths.

#### RT-RTE-research-maintenance
Label: Research tasks and maintenance admissions

Endpoints/progression: agenda/wiki scan → prioritized hypotheses → selected execution branches → metrics/experiment notes; separately recent-page validation or deep lint → metadata/conflict writes. Owners: research code, validator code and lint code; models generate query/outline or propose conflict descriptions. Research agenda parsing recognizes selected headings and supplies hardcoded thresholds; it does not execute all prose constraints. Unified driver executes top two hypotheses. Coverage execution returns a query without actual search; validation/update mark tasks identified; synthesis generates an outline without saving a comparison page. Retrospective validation's weekly route checks existing conflict tags and source-count/confidence thresholds; the available model `check_contradiction` helper is not called there. Deep lint does request model comparison of truncated page bodies, maps returned filenames to paths and writes conflict tags. These are distinct maintenance admission mechanisms, not one evidence-validation guarantee. SRC-1: `tools/research_agent.py`, `tools/retrospective_validator.py`, `tools/lint.py`, `tools/unified_daemon.py`.

Trigger/mode: scheduled or CLI open maintenance, not independently grounded experiments. Answer oracle: none independent; counts/confidence/status rules and model judgments are selectors, not expected-answer references. Software proposes/admits writes; no per-result human veto. Model parse errors or membership checks can reject lint results; source-count rules admit confidence increments automatically. Recovery is caught exceptions/logging, with no automatic previous-page restoration. Guidance persists as agenda/code/prompts; results persist as notes, reports and changed metadata, not demonstrated new corroborating evidence.

- Immediate return: Research result dictionaries and logs; validation report and counts; lint console output/tag writes.
- Later read-back: Future page scans consume changed metadata/content; research/experiment records retain tasks, not proof that requested searches occurred.
- Delegated visibility: Query/outline model gets task text; deep lint gets first 600 body characters per included page with basename identities.
- Selection predicate: Coverage targets, confidence below 0.75, 90-day mtime, model-page groups; validator recent mtime and reinforcement thresholds; deep lint included pages.
- Invalidation or expiry: Files are overwritten/tagged; recentness is mtime-based; no independent source-revalidation expiry rule in weekly validation.
- Activation or effect: Metadata and lint conflict writes are wired; research branch success need not change wiki content.
- Evidence limits: No new-source validation, completed external experiment or claimed quality gain is established by these labels.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result['pages_affected'] = 0  # Would be updated after actual search
> --- `tools/research_agent.py`

> # For now, just check if page has [CONFLICT] tags
> --- `tools/retrospective_validator.py`

#### RT-RTE-wiki-consumption
Label: Search and synthesis consumers

Endpoints/progression: retained Markdown → BM25/API article delivery, or selected wiki excerpts → model insights/newsletter → saved outputs. Search owner is query code; paper topic selection is caller choice, coverage-count code or model-selected allowed topics. Newsletter selection is time/bucket code; model proposes text; nonempty/length rules admit it. Paper generation performs two critique/improve calls then writes a draft; long form overrides this with per-section generation and explicitly skips critiques. These are separate output modes, not guaranteed equivalent quality gates. Trigger is API/CLI request or scheduled paper cycle; open generation rather than evaluated experiments. Answer oracle: none independent. Paper external-source helper returns a placeholder, not live literature search. Humans can edit later through a separate route, not veto each automated output. Recovery is parsing/fallback behavior and write exceptions, without substantive admission review. SRC-1: `tools/query.py`, `api_server.py`, `tools/paper_agent.py`, `tools/paper_agent_long.py`, `tools/newsletter_agent.py`.

- Immediate return: Search paths/scores or full article; paper metadata/path and newsletter console/log output after persistence.
- Later read-back: Newsletters saved under wiki enter subsequent search and potentially later synthesis; paper drafts persist under papers but this inspected generator does not reload prior papers as feedback.
- Delegated visibility: Search API adds 300-character snippets; paper analysis delivers at most five matching pages truncated to 2,000 characters each, then structured insights to drafting; newsletter sends five snippets per bucket; critiques receive a 20,000-character draft prefix.
- Selection predicate: Positive BM25 scores/top five; topic-string containment and traversal order for paper pages; mtime/category buckets for newsletter; generated output length for newsletter admission.
- Invalidation or expiry: Queries reload current files; dated newsletter/paper filenames can be overwritten on rerun; omitted context is reachable only through a subsequent file-selection operation.
- Activation or effect: Delivery, model requests and saved synthesis paths are wired; warranted novelty, factual accuracy and behavior-changing activation are unobserved.
- Evidence limits: Critique instructions do not demonstrate content-directed theoretical criticism or benefit; long-form route bypasses critique entirely.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # For now, return placeholder
> # In production, this would query arXiv API, Semantic Scholar, etc.
> --- `tools/paper_agent.py`

> # Skip critique iterations to preserve length
> --- `tools/paper_agent_long.py`

### Claims

#### RT-CLM-prompt-ratchet
Label: Claimed prompt improvement ratchet

Claimed operation: optimizer tests modifications, keeps improvements and reverts failures. Source layer: doctrine/design in SRC-1: `tools/prompt_optimizer.py`; implementation qualification is [RT-RTE-prompt-optimization](#rt-rte-prompt-optimization), which separates a working score/decision path from missing candidate installation and unsafe recovery semantics.

> Tests prompt modifications, keeps improvements, reverts failures.
> --- `tools/prompt_optimizer.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Prompt guidance to model completion

Consumer: primary/fallback inference model. Channel: system message populated from [RT-OBJ-prompts](#rt-obj-prompts) and function-local generation instructions. Force: natural-language guidance requiring interpretation, not Python enforcement of attribution or truth. Horizon: current call; shipped strings are reloaded in later processes, while optimizer candidates do not reach this path through the inspected commit method. SRC-1: `tools/common.py`, `tools/prompts.py`, `tools/prompt_optimizer.py`.

> def get_extraction_prompt():
>     """Get the currently active extraction prompt."""
>     prompt_name = ACTIVE_PROMPTS["extraction"]
>     return globals()[prompt_name]
> --- `tools/prompts.py`

#### RT-BAP-wiki-context
Label: Retained wiki text as model context

Consumer: integration, paper and newsletter model calls. Channel: selected old body, page excerpts or snippets in user-message content. Force: informational context interpreted by models, not executable authority or proven compliance with embedded instructions. Horizon: later invocations across workflow runs; actual changed behavior remains unobserved. A separate symbolic channel exists where validator/research code consumes confidence/status/source_count metadata under fixed rules. The current record describes the text-to-model path, not a substitute for memory's per-part findings. SRC-1: `tools/integrate.py`, `tools/paper_agent.py`, `tools/newsletter_agent.py`, `tools/retrospective_validator.py`.

> newsletter_body = call_local_model(system_prompt, input_text)
> --- `tools/newsletter_agent.py`

#### RT-BAP-agent-doctrine
Label: Coding-agent governance contract

Consumer: externally hosted compatible coding agent or human maintainer. Channel: repository `AGENTS.md` natural-language instructions; force depends on host loading and interpretation, not automatically on the Python programs. Horizon: maintenance sessions where that host supplies it. It requests source trust, historical-claim retention, raw immutability and escalation. Python paths do not thereby inherit those requirements as enforced gates, and no supplied execution shows this host activated. SRC-1: `AGENTS.md`, `tools/normalize.py`, `tools/integrate.py`.

> - DO NOT modify files in `/raw/` once written.
> - DO NOT delete conflicting claims without human approval.
> - DO NOT promote Tier 3 claims to verified without validation.
> --- `AGENTS.md`

## Annotations

none
