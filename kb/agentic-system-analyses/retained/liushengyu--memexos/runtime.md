---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MemexOS runtime baseline: unattended source admission, staged compilation, review, maintenance and later retrieval at the frozen revision."
run-id: AAS-2026-11-07-memexos-5cd34a715eb7-01
reviewed-boundary: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
---

# MemexOS runtime report

## Runtime account

### What the system does and who advances it

MemexOS turns collected material into a Git-backed wiki and provides search/get to later agents. Its consequential work is not one answering conversation: an admission worker chooses sources, a writer edits a staging worktree, program checks and a model reviewer control normal publication, and later callers retrieve the published files. All findings below use SRC-1 at the boundary's frozen revision. They concern inspected implementation or attributed design, not an executed target. No target code or tests were run, and no production trace or causal experiment was supplied. Successful operation, instruction compliance and benefit remain unobserved.

The CLI command map includes capture, intake, catalog, ingest, lint, fix, correct, search/get, inbox, schedule/nightly, console and evaluation. `python -m memexos` reaches that CLI. Init creates the vault layout, ledgers, instructions and a CLAUDE.md alias; it preserves existing template files rather than replacing them during subsequent init. See SRC-1, `src/memexos/cli.py`, `src/memexos/scaffold.py`, and the boundary's entry-point evidence. Manual source placement and explicit capture commands are alternative triggers; admission by the intake worker is not a prerequisite for every raw file consumed by ingest.

The ordinary selected invocation is `memex ingest` after a source lands. Code loads configuration/language, opens an event run, checks review-service cooldown and pause, yields to waiting writers, and obtains the write lock for each batch. Pending raw paths exclude attachments, feedback, already-ingested paths and held paths. Video transcript/companion grouping can exceed the nominal batch size. Classification is added to the prompt, with an unclassified fallback on classification failure. The compile prompt tells the writer to read AGENTS.md, read the sources, write related pages/index/log, and put unresolved decisions in inbox. The writer receives a fresh backend call rooted in staging, not a resumed conversation ID. The terminal CLI result is a status code plus events and retained files, not an answer to the original source's subject matter (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`, `src/memexos/prompts/en/compile.md`; [RT-RTE-compile-publish](#rt-rte-compile-publish)).

Stage.open commits pending raw changes, freezes the base commit and creates a timestamped branch/worktree. Writer success leads to Gate 1; failed checks are returned to another writer call for bounded rework. Optional self-check selects new unmarked sentences, pairs them with nearby source passages and asks a judge about support. Flagged material prompts rework; unavailable self-check proceeds to review. Gate 2 obtains structured claim/key-point/overwrite/injection judgments, then program rules compute pass/fail. Critical bad claims and substantive unsupported or undisclosed overwrites block; noncritical bad claims block only above 5%, and must-point coverage below 80% blocks. These thresholds operate on the reviewer's reported inventory, not an independently complete inventory of actual claims. Passing can retain minor problems for later fix (SRC-1, `src/memexos/pipeline/selfcheck.py`, `src/memexos/pipeline/gate2.py`).

Only after this does ingest add machine ledgers and call Stage.publish. Publish commits the worktree and merges the branch into the live vault; merge failure aborts the merge. It then removes staging, attempts synchronous full-text refresh and starts a detached reindex process. Full-text-refresh exceptions are swallowed; vectors follow asynchronously. Therefore publication success is not proof of index freshness. A failed writer discards its attempt; failed checks can retain a held branch and mark raw paths held, preventing automatic retry. Review unavailability discards the draft and writes a cooldown marker. These are different recovery states, not one universal retry policy. Console abandon can delete a non-live held branch and remove its raw paths from held.txt so they queue again (SRC-1, `src/memexos/pipeline/stage.py`, `src/memexos/pipeline/compile.py`, `src/memexos/console/actions.py`).

### Three forcing cases and the resulting guarantee limits

1. **Gate 2 disabled or no review-relevant change.** The public prose says unchecked batches are never published, but `review()` explicitly returns code 4 for `pipeline.gate2 = off`; review_loop returns `off`, and ingest continues to publication. Lint/fix/correct/inbox also accept `off`. Even with enforcement enabled, gate2.run returns pass without a model call when no wiki/index change is found. Correct and inbox apply additionally skip review when their wiki/index diff is empty. Fix with zero reported problems publishes only its ledger update without writer/review. These are supported caller branches, not hypothetical direct internal API calls (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/gate2.py`, `src/memexos/inbox.py`).

2. **Backend changes under the same writer Policy.** Writer grants edits to wiki/, inbox/, index.md and log.md, with no command/web grant. Claude Code exposes only selected tools and path permission rules. API backends resolve local file paths and apply write-root checks. Codex instead selects workspace-write for the whole cwd; its adapter does not narrow that workspace to the writer's four paths, and command prefixes are advisory prompt text. Gate 1 independently rejects disallowed tracked changes in the staged diff, but cannot undo an earlier out-of-worktree process effect. Codex custom-provider configuration also disables its normal user-config isolation. Thus a capability declaration, an adapter's grant translation and the deployed external sandbox are not equivalent (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/backends/claude_code.py`, `src/memexos/backends/codex.py`, `src/memexos/backends/tools.py`; [RT-RTE-backend-execution](#rt-rte-backend-execution)).

3. **Changes outside model compilation.** Intake directly admits raw/candidate material after scanning; inbox script actions capture sources and apply catalog/category decisions; plugin code runs in the host Python process. Those paths do not become Gate-2-controlled merely because staged wiki writing is. Human decisions exist for selected inbox items, but open agent-resolvable items can enter the automatic apply queue. The human is not an approval gate on every wiki edit or every source (SRC-1, `src/memexos/intake/admit.py`, `src/memexos/inbox.py`, `src/memexos/plugins/__init__.py`; [RT-RTE-inbox-maintenance](#rt-rte-inbox-maintenance), [RT-RTE-extension-loading](#rt-rte-extension-loading)).

The load-bearing **publication gate** is owned by compile/inbox orchestration, enforced at caller branches before Stage.publish. Guarantee strength: protocol, conditional on the selected path and configuration; implementation conclusion status: wired; operation conclusion status: uninspected. It covers staged wiki-writing routes when checks are enabled, not arbitrary vault edits, capture, machine-ledger writes or host extensions. It needs external model/provider availability and useful, correctly shaped judgments. “Pass” is not a truth invariant. Stage.publish itself has no independent gate check. The **writer file-scope control** is owned jointly by the backend adapter and Gate 1. Guarantee strength: protocol for the checked diff, not a uniform deployment guarantee for all process effects; implementation conclusion status: wired; operation conclusion status: uninspected. External CLI permission and sandbox semantics remain an external contract. The **staging separation** keeps the writer's draft in a separate worktree; it does not establish an atomic multi-file filesystem view for concurrent readers during a Git merge (SRC-1, `src/memexos/pipeline/stage.py`, `src/memexos/pipeline/gate1.py`, `src/memexos/backends/codex.py`).

### Maintenance, coordination and read-side boundaries

Nightly runs intake, configured maintenance steps and finally ingest. Its default list includes classification/catalog sync, evaluation coverage, usage judging/verification, fix and inbox operations. It catches exceptions per step and emits nightly.done even after step failures; that event is completion of the driver, not proof that all work succeeded. Console job starts spawn detached CLI processes and consult running-job state; write-side jobs use locks for shared vault mutation. Ingest releases the write lock between batches. Intake holds a separate intake lock and acquires the write lock around post-processing/capture/commits, not around the whole model call. Inbox queues have a six-hour stale-queued recovery rule (SRC-1, `src/memexos/schedule.py`, `src/memexos/default_config.toml`, `src/memexos/console/actions.py`, `src/memexos/intake/admit.py`, `src/memexos/inbox.py`).

Search/get are returning computations: a caller supplies question/keywords or page name, code selects retained material and returns text/JSON to that caller. They do not own the caller's next reasoning step. Auto search combines FTS and available qmd vectors, fuses ranks, optionally reranks and removes inbox hits unless requested/configured. Other modes select keyword, vector or qmd deep behavior, with fallbacks. Get reloads a resolved file and can return a line slice. The shipped vault instructions request search → get → cite, but cannot establish that external agents follow this sequence or that delivered content changes their answers (SRC-1, `src/memexos/search/engine.py`, `src/memexos/search/cli.py`, `src/memexos/templates/vault/en/AGENTS.md`; [RT-RTE-search-get](#rt-rte-search-get)).

Working context is partitioned by backend calls and filesystem work areas. Admission is given a selected batch plus scoped roots; writer/reviewer calls receive different prompts/tools; API loops accumulate current tool exchanges, but a new call starts a new message list. Review diff is truncated at 600,000 characters with an instruction to open files for the rest. Tool results have output/read caps. These are context-selection and call-isolation mechanisms, not proof of model compliance or a complete compaction policy. Files and gate reports cross calls; model hidden state does not have an inspected cross-call persistence path. CLI internal context management remains external and uninspected (SRC-1, `src/memexos/intake/admit.py`, `src/memexos/backends/anthropic_api.py`, `src/memexos/backends/openai_compat.py`, `src/memexos/backends/tools.py`, `src/memexos/pipeline/gate2.py`).

Added inspection beyond the boundary worker's initial scope used the same SRC-1: backend routing and all four execution adapters, API tools, Gate 1/Gate 2/self-check, selected intake post-processing and inbox action paths, plugin registration, scaffold, search orchestration/reranking, qmd model/update logic and judge selection. These add implementation evidence, not sources or observed runs. Remaining available but uninspected detail includes individual site collectors, full classifier internals, complete localized prompts, evaluator outcomes and dependency internals; no translation equivalence, complete security audit or performance result is asserted. Knowledge revision and theory/learning assessments belong to the later specialists; this baseline establishes the routes and their control points.

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code model service

Source-native identity: configured `claude-code` backend, selectable per role or `backend:model`. Form: distributed-parametric model behind an external CLI; local adapter and permission arguments are symbolic code. Storage substrate: provider parameters outside SRC-1; output/error artifacts under the caller's workdir. No parameter update is issued by the inspected adapter. Exact model version is not pinned: default config leaves model empty and uses the CLI default; a supplied model name need not be an immutable weight identity. A mutable service/default can resolve to another model; provider-side changes are uninspected. Evidence: SRC-1, `src/memexos/backends/claude_code.py`, `src/memexos/default_config.toml`.

> model = ""          # empty = the CLI's default model
> --- `src/memexos/default_config.toml`

#### RT-CMP-codex
Label: Codex model service

Source-native identity: `codex` backend. Form: distributed-parametric model plus symbolic CLI adapter. Storage: external provider/CLI; event stream and final output in workdir. No parameter update is issued in the inspected adapter. Exact version is not pinned; absent explicit selection it reads the user's configured model. A name/default can resolve to a different provider model; provider updates are uninspected. SRC-1, `src/memexos/backends/codex.py`.

> return self.section.get("model") or str(user_config(str(codex_home())).get("model") or "")
> --- `src/memexos/backends/codex.py`

#### RT-CMP-anthropic-api
Label: Anthropic API model service

Source-native identity: `anthropic` backend. Form: distributed-parametric model accessed through the SDK; symbolic host tool loop. Storage: provider parameters, plus local tool transcript/output artifacts. No training/update request appears in the inspected loop. Default config names a model family/default rather than immutable parameters; exact weight version is unestablished, and endpoint/model resolution can change outside SRC-1. Provider internals are uninspected. SRC-1, `src/memexos/backends/anthropic_api.py`, `src/memexos/default_config.toml`.

> resp = client.messages.create(messages=messages, tools=tools, **params)
> --- `src/memexos/backends/anthropic_api.py`

#### RT-CMP-openai-compatible
Label: OpenAI-compatible model service

Source-native identity: `openai` or a named backend section with type openai. Form: distributed-parametric model accessed through Chat Completions, with symbolic host tool dispatch. Storage: remote or local server parameters; local transcript/output artifacts. Inspected calls do not train parameters. Model must be configured, but no immutable parameter digest is established. Base URL and model are configurable; the endpoint can serve different weights independently of this revision. Internals remain uninspected. SRC-1, `src/memexos/backends/openai_compat.py`, `src/memexos/default_config.toml`.

> body: dict = {"model": self.model(), "messages": messages}
> --- `src/memexos/backends/openai_compat.py`

#### RT-CMP-jev
Label: Jev judge service

Source-native identity: optional `judge.backend = jev`. Form: distributed-parametric hosted decision model; local thresholds/requests are symbolic. Storage: external service parameters; emitted usage events locally. No parameter update is established by the inspected caller. Exact model version is not pinned: configured default `jev-latest` is a mutable model name. Service may change its resolution; its internals and claimed calibration are uninspected. SRC-1, `src/memexos/judge.py`, `src/memexos/default_config.toml`.

> self.url, self.model = s.get("url"), s.get("model") or "jev-latest"
> --- `src/memexos/judge.py`

#### RT-CMP-qmd
Label: qmd local model components

Source-native identity: qmd embedding, reranker and query-generation components used by optional search modes. Each has distributed-parametric form and externally managed local model-file storage. Embeddings also produce numerical retained vectors in the qmd index; these are not parameter training. For the embedding model, inspected code selects a URI or qmd default and can request forced re-embedding after its model-name setting changes; no weight update is issued. Exact parameter digest is not pinned, and a configurable URI/default can resolve differently. For the reranker, inspected code selects the installed qmd model and performs inference; no parameter update or exact parameter pin is established, and package/model defaults can change. For query generation, deep mode delegates to qmd's pipeline; exact version, parameter mutation and resolution policy are uninspected because qmd internals are excluded. There is no claim that these components share one state or invalidation rule. SRC-1, `src/memexos/search/qmd.py`, `src/memexos/search/rerank.py`, `src/memexos/default_config.toml`.

> e = run([exe, "--index", index_name(cfg), "embed"] + (["-f"] if changed else []), env=_env(cfg), timeout=3600 * 3)
> --- `src/memexos/search/qmd.py`

### Operative objects

#### RT-OBJ-stage
Label: Staging worktree

Source-native identity: Stage.dir and staging branch based on the live vault HEAD. Form: symbolic Git/worktree organization containing natural-language Markdown source/wiki/inbox content; those content parts retain their own interpretation and are left to the memory analyst. Substrate: filesystem worktree, Git object database and branch refs. Its distinct runtime identity is the isolated draft workspace and merge/recovery mechanism, not a second declaration of every wiki object. SRC-1, `src/memexos/pipeline/stage.py`.

> git(self.vault, "worktree", "add", "-q", "-b", self.branch, str(self.dir), self.base)
> --- `src/memexos/pipeline/stage.py`

#### RT-OBJ-policy
Label: Backend Policy

Source-native identity: backends.Policy passed by each caller. Form: symbolic lists/booleans for writable/readable paths, command prefixes, web/network and deny patterns. Substrate: in-process dataclass translated into CLI arguments or API tool checks. Writer's concrete grant is four write destinations, unlike admission/research grants. It is not itself an OS isolation envelope. SRC-1, `src/memexos/backends/base.py`, `src/memexos/pipeline/compile.py`.

> return backends.Policy(write=[d / "wiki", d / "inbox", d / "index.md", d / "log.md"])
> --- `src/memexos/pipeline/compile.py`

### Routes

#### RT-RTE-source-admission
Label: Source admission

Endpoints: configured sessions/RSS/plugin collectors → selected batch → worker decisions.jsonl → raw files/candidates/admission ledger. Code owns collection/progression and physical I/O; worker proposes per-item admit/reject/uncertain and extracted outputs under admission prompt guidance. Post-processing restricts decision keys to the offered batch, uses output basenames, checks document roots, scans selected text and blocks scanned hits before admission. Rejection is software/model-controlled here, not per-content human approval; uncertain candidates can later receive an owner decision. Operating mode: open incoming material filtered in batches. Answer oracle: no expected-answer oracle established; admission criteria guide model judgment. Persistence includes admitted source files, candidates, reasons and ledger state; failed URL captures are recorded for bounded retry. Later wiki interpretation has its own gate, not this admission rule. SRC-1, `src/memexos/intake/admit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI prints run/count summary; worker returns a Result and may leave decision/output files.
- Later read-back: admitted raw paths are selected by ingest; admission ledger/state affects later collection and capture retry.
- Delegated visibility: worker receives selected item metadata and configured readable roots; output files and decisions cross back to host post-processing.
- Selection predicate: configured sources, requested source/time/batch filters, offered item keys and model decisions; text scan can veto admit/uncertain.
- Invalidation or expiry: failed capture retry is bounded to fewer than three recorded failures; ledger retains decisions; complete source lifecycle is not assessed here.
- Activation or effect: host writes/copies accepted material or queues capture under the write lock; downstream answer changes are unobserved.
- Evidence limits: scanner coverage of selected outputs does not establish a universal no-secret guarantee across all capture and copy routes; worker.ok is not required before post_process except quota stopping.

> if hits and dec in ("admit", "uncertain"):
>     row["decision"] = "blocked"
> --- `src/memexos/intake/admit.py`

#### RT-RTE-compile-publish
Label: Compile and publish

Endpoints: pending raw batch → staged writer → Gate 1 → optional self-check → review/rework → ledgers and publication. Program owns scheduling, retries, structural checks and final merge; writer proposes textual changes; reviewer supplies judgments; deterministic Gate 2 rules decide on those judgments. Human intervention is not required for normal admission; unresolved questions are requested in inbox. Guidance is compile/AGENTS/rework prompts and classification context; proposed changes are wiki/index/log/inbox text, while machine ledgers are added by code. Operating mode: unattended open-source batches with bounded repair rounds, not a controlled experiment. Answer oracle: raw source comparison is requested from models, but no independently supplied correct-answer oracle is established. Reject/discard/hold and merge-abort paths provide recovery; Git commits afford later reversion, not automatic semantic rollback. SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/gate1.py`, `src/memexos/pipeline/gate2.py`, `src/memexos/pipeline/stage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ingest returns success, failure/held or nothing-to-do statuses; events record draft/check/publication outcomes.
- Later read-back: published wiki can be read by search/get and later maintenance; failed/passing review directories can feed fix.
- Delegated visibility: writer sees staging cwd; reviewer gets paths, rubric, diff and read-only file access; rework gets rendered problems, not the earlier model session.
- Selection predicate: pending paths minus ingested/held ledgers, batch limit plus companion grouping; publication requires Gate 1 and accepted review outcome, with configured off exception.
- Invalidation or expiry: discard removes attempt/worktree; hold preserves branch and suppresses raw retry; review cooldown expires by timestamp.
- Activation or effect: Git merge changes live vault; FTS refresh is attempted, detached reindex follows; effect on later model behavior is unobserved.
- Evidence limits: review is probabilistic judgment under deterministic thresholds; enabled checks do not prove every claim was inventoried or true, and readers have no established multi-file snapshot guarantee.

> if (cfg.get("pipeline.gate2") or "enforce") == "off":
>     return 4, {}, Path()
> --- `src/memexos/pipeline/compile.py`

> if code == 4:
>     return "off", dirs, rep
> --- `src/memexos/pipeline/compile.py`

> add_to_ledger(stage.dir, "ingested.txt", raws)
> --- `src/memexos/pipeline/compile.py`

#### RT-RTE-backend-execution
Label: Backend execution and fallback

Endpoints: agent/structured role call → configured backend chain → CLI subprocess or API tool loop → Result/artifacts/events. Router owns backend choice: skips unavailable backends, marks quota exhaustion, retries transient structured calls, and stops on real failures rather than freely hopping models. Writer separately retries transient agent failures using a resume instruction plus existing worktree state. The model owns tool requests and final text; adapters own execution and result parsing. Policy is translated, not uniformly enforced by one kernel boundary. CLI providers own internal next-step loops; API loops append assistant/tool results and continue until final answer, refusal, timeout or turn limit. SRC-1, `src/memexos/backends/__init__.py`, `src/memexos/backends/claude_code.py`, `src/memexos/backends/codex.py`, `src/memexos/backends/anthropic_api.py`, `src/memexos/backends/openai_compat.py`, `src/memexos/backends/tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Result with text/parsed object, status, model, usage, errors, denials and tried backends; local execution artifacts retained per adapter.
- Later read-back: quota marks govern later routing; current draft files govern rework; transcripts are not automatically replayed as conversation history by the inspected router.
- Delegated visibility: caller supplies prompt/cwd/images and Policy; structured calls use read-only tools/sandbox and attached context, agents receive broader task-specific grants.
- Selection predicate: ordered role chain or fixed @backend; availability, quota and transient/limited/error classifications determine progression.
- Invalidation or expiry: quota marks expire by configured retry interval and clear on success; CLI sessions requested ephemeral/nonpersistent; API message lists are call-local.
- Activation or effect: tool requests can read/write/execute according to adapter path; denial is recorded without necessarily failing the whole model run.
- Evidence limits: deployed CLI enforcement is external; Codex commands are advisory and workspace scope is broader than Policy.write; API command-prefix checks are not an OS sandbox on the allowed executable.

> break        # a real failure (bad output, refusal): do not hop backends, report it
> --- `src/memexos/backends/__init__.py`

> sandbox = "workspace-write" if policy.write or policy.commands else "read-only"
> --- `src/memexos/backends/codex.py`

> return self.section.get("isolate", True) is not False and not custom_provider
> --- `src/memexos/backends/codex.py`

> return any(p == w or w in p.parents for w in self.writes)
> --- `src/memexos/backends/tools.py`

Additional alternate-channel limit: OpenAI-compatible tools advertise fetch_url only when web is enabled, but `_call` dispatches that name without rechecking web. The loop consumes provider-returned function names directly. A provider response containing that name can therefore reach fetch even when it was not advertised; no inspected local allowlist rejects it before dispatch. This is a code-level response-shape case, not an observed model action or a claim that compliant providers emit unadvertised tools. Anthropic server-native search/fetch is separately assembled only for policy.web; neither provider's native internals are audited. SRC-1, `src/memexos/backends/openai_compat.py`, `src/memexos/backends/anthropic_api.py`.

> if name == "fetch_url":
>     from memexos.capture import fetch
> --- `src/memexos/backends/openai_compat.py`

#### RT-RTE-inbox-maintenance
Label: Inbox and feedback maintenance

Endpoints: reports, owner choices, agent-resolvable items and usage feedback → scripted actions or staged writer → updated sources/catalog/wiki and status events. Code queues decided report items before open agent items that do not need local work and have required web evidence; queued stale work can reopen after six hours. Owner chooses/dismisses selected issues, not every change. Free-text owner decisions can become raw feedback; scripts handle candidate capture/category/blocked-branch decisions without a writer. Other queued items use Writer and review only when wiki/index changes. Separately usage.verify asks a worker about feedback and emits confirmed problems in the gate2 review format for fix; fix/lint/correct use the shared staging machinery. Guidance: item body/triage/decision/research, maintenance prompts and review problems. Operating mode: open maintenance requests with bounded batches/rework. Answer oracle: no expected-answer oracle established; model source verification is not one. Program gates can veto staged changes; failures requeue, hold or discard; undo applies only to not-yet-applied decision states. SRC-1, `src/memexos/inbox.py`, `src/memexos/usage.py`, `src/memexos/pipeline/compile.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: action success/failure, item status events, feedback status, and staged writer Result/statuses.
- Later read-back: decisions, feedback files, review directories and ledgers feed later apply/correct/fix; published text feeds search/get.
- Delegated visibility: writer receives selected items and shortened original bodies, with owner decision or agent task and research references; verifier gets feedback context and read-only vault access.
- Selection predicate: pending feedback/unfixed review limits and inbox queue predicates; no-problem fix and unchanged wiki/index paths can avoid model review.
- Invalidation or expiry: completed ledgers suppress repeated work; stale queued items can reopen; lint expires old inbox Markdown by configured age.
- Activation or effect: scripted source/catalog changes or reviewed wiki merges; improved later answer capacity has not been observed.
- Evidence limits: software does not require a human decision for all queued agent items; decision API caller identity alone does not prove a human authored a given decision.

> return (human + agent)[:max_n]
> --- `src/memexos/inbox.py`

> if res["verdict"] == "confirmed" and res["problems"]:
>     rec["fix_dir"] = str(to_fix_job(cfg, f, res))
>     rec["status"] = "to_fix"
> --- `src/memexos/usage.py`

#### RT-RTE-search-get
Label: Search and get

Endpoints: external caller's question/keywords → FTS/qmd/fusion/optional reranking → selected hits → caller's requested get → file text. Code owns retrieval progression and representation conversion, caller owns choice of reads and downstream answer. FTS-only, vector and deep modes are material alternatives; missing qmd or empty non-keyword results can fall back to FTS. Rerank failure keeps fused order and emits degradation notes. Ranking uses symbolic fusion or optional distributed components, not an expected-answer oracle. SRC-1, `src/memexos/search/engine.py`, `src/memexos/search/cli.py`, `src/memexos/search/rerank.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: text or JSON hits with title/path/classification/snippet metadata; get returns header and requested file lines.
- Later read-back: this is the later read-back consumer of published knowledge; read/search events can also feed usage summaries, but do not prove subsequent reliance.
- Delegated visibility: caller receives bounded hit metadata and explicitly requested page text; ranking models receive passages, not necessarily complete pages.
- Selection predicate: question/keywords/mode, available indexes, rank fusion, optional reranking, inbox filter, deduplication and result limits; get normalizes names/paths and resolves a file.
- Invalidation or expiry: indexes refreshed separately; no proof every retrieval sees the most recent publication; page text is reloaded at get time.
- Activation or effect: delivery to caller stdout; final answer behavior remains the caller's responsibility and is unobserved.
- Evidence limits: available code establishes retrieval, not relevance quality, complete evidence delivery or obedience to vault citation instructions.

> if not hits and mode != "keyword":
>     hits = fts.search(cfg.vault, db, terms, max(n * 2, cand), degraded, kws)
> --- `src/memexos/search/engine.py`

> lines = (cfg.vault / rel).read_text(encoding="utf-8", errors="replace").splitlines()
> --- `src/memexos/search/cli.py`

#### RT-RTE-extension-loading
Label: Extension and capability loading

Endpoints: installed memexos.plugins entry-point registration/configuration → imported host module → collection/fetch/capture hooks. Installed package registrant proposes code; installation/environment and config determine admission, not a model review gate. Enabled controls intake participation, but fetch/capture handlers can import and use modules regardless of enabled intake status. Python import executes host code without the model Policy wrapper. Guidance: plugin hook interface and ADMISSION text, which can also enter the worker prompt. Persistence is installed module/config and its collected content; rejection ability is missing registration/import failure or intake disabled, with the latter not a universal plugin veto. Recovery is operator package/config replacement; automatic transactional plugin rollback is not established by this loader. Operating mode: host configuration/extension, not model-generated self-modification; human versus automated installation is unresolved. Answer oracle: inapplicable to module loading. Product updates outside this inspected loader are ordinary package/operator changes, not an established automatic improvement loop. SRC-1, `src/memexos/plugins/__init__.py`, `src/memexos/intake/admit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: imported module or hook output; enabled() skips ImportError.
- Later read-back: installed modules affect later host calls; plugin ADMISSION text affects later admission prompts; captured outputs can enter ingest.
- Delegated visibility: plugin executes in the host process; model grant boundaries do not sandbox plugin code.
- Selection predicate: entry-point names, plugin-specific enabled for intake, FETCH handler names or URL handles for fetch/capture.
- Invalidation or expiry: no loader TTL or automated revision expiry established; package/config state supplies later loads.
- Activation or effect: code import and invoked hooks can extend host capabilities; actual deployment is unobserved.
- Evidence limits: no third-party package or installation trace supplied; this is a shipped extension affordance and wiring, not evidence of exercised arbitrary-code compromise.

> for ep in entry_points(group="memexos.plugins"):
>     mods.setdefault(ep.name, ep.value)
> --- `src/memexos/plugins/__init__.py`

> return importlib.import_module(_all()[name])
> --- `src/memexos/plugins/__init__.py`

### Claims

#### RT-CLM-checked-publication
Label: Checked publication claim

Claimed operation: compiler documentation says it never publishes anything the review did not pass. SRC-1, `src/memexos/pipeline/compile.py`, doctrine/design. The implemented off and no-change paths in [RT-RTE-compile-publish](#rt-rte-compile-publish) qualify this assertion. Gate outcomes are not evidence of semantic correctness or model independence: default reviewer fallback can use Claude Code, and the code's same-family metric is not a veto. Implementation conclusion status: wired for the conditional gate; operation conclusion status: uninspected.

> review cannot run (quota, network) the batch is discarded and compiling pauses briefly rather than
> publishing unchecked text.
> --- `src/memexos/pipeline/compile.py`

#### RT-CLM-schema-change
Label: Schema change proposal contract

Claimed operation: the vault rules ask agents to propose schema changes in inbox rather than silently work around them, with the person approving new page kinds. Natural-language instruction admission is therefore a proposed human/agent collaboration, not an unrestricted writer grant to rewrite AGENTS.md. Gate 1 excludes that file from allowed changes, while scaffold preserves existing files. This establishes the shipped request and structural scope restriction; it does not establish actual schema evolution, compliance, content-directed criticism or iterative theory building. SRC-1, `src/memexos/templates/vault/en/AGENTS.md`, `src/memexos/pipeline/gate1.py`, `src/memexos/scaffold.py`.

> **propose a change** (write it to the inbox) instead of quietly working around it.
> --- `src/memexos/templates/vault/en/AGENTS.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-writer-guidance
Label: Writer task guidance

Consumer: writer model selected through the backend router. Channel: compile/rework prompt, requested full AGENTS.md read, classifications and check problems. Force: natural-language task/policy request, with separate symbolic tool and diff enforcement; delivery does not establish compliance. Horizon: one call and further calls re-reading current worktree/guidance; shipped static rules are not accumulated memory merely because repeatedly read. Retained revision findings belong to specialists. SRC-1, `src/memexos/prompts/en/compile.md`, `src/memexos/pipeline/compile.py`.

> You maintain this knowledge base. First read AGENTS.md in full, then compile the raw files below following its §2.1 "Automatic mode"
> --- `src/memexos/prompts/en/compile.md`

#### RT-BAP-review-verdicts
Label: Review verdict authority

Consumer: gate2.decide and compile review_loop. Channel: structured reviewer object then code-derived errors/warnings/pass status; rework receives rendered problems. Force: symbolic admission decision on model-produced fields, plus natural-language feedback to the next writer. Horizon: batch rework rounds and later fix through retained review files. Required contract: correctly shaped and useful model judgments; program thresholds do not establish their truth or completeness. SRC-1, `src/memexos/pipeline/gate2.py`, `src/memexos/pipeline/compile.py`.

> return (0 if not errors else 1), rep
> --- `src/memexos/pipeline/gate2.py`

#### RT-BAP-retrieved-pages
Label: Retrieved page delivery

Consumer: external asking agent or person. Channel: search metadata and get text. Force: informational natural-language content; vault doctrine requests citation and evidence-strength-sensitive wording, not mandatory host-level control of the answer. Horizon: later caller invocation across sessions while pages remain available. This distinguishes reachable retained material from demonstrated activation. SRC-1, `src/memexos/search/cli.py`, `src/memexos/templates/vault/en/AGENTS.md`.

> 3. Answers **cite** wiki pages (which cite `raw/`); check the source classification before citing and word it per §2.1.4
> --- `src/memexos/templates/vault/en/AGENTS.md`

## Annotations

none
