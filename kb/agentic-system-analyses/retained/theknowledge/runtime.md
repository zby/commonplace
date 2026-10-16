---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "TheKnowledge runtime baseline: incremental authorship, durable deposits, retrieval, remote research and instruction admission at the frozen Git boundary."
run-id: AAS-2026-10-14-theknowledge-319a64927ee3-01
reviewed-boundary: aca6e29e69c6a72b697b8178841d03e6296ee3fc
---

# TheKnowledge runtime report

## Runtime account

### Work and evidence

TheKnowledge turns sources into canonical filesystem knowledge, authors and maintains wiki pages, and supplies retained content to later human and model queries. It is not an enclosing general-purpose agent runtime. Python code owns most next-step decisions; model calls return scores, plans or prose to that code. The enclosing Claude Code host owns foreground agent sessions and compaction. This account uses SRC-1 implementation and doctrine/design at the boundary's revision. No target execution, installed service, provider interaction or test run was supplied or performed. Every operational result, activation and benefit below remains unobserved. See [boundary](boundary.md#boundary-and-evidence).

The initial boundary inspection covered shipped entry points. Additional inspection here covered plan parsing and prompts, both model clients, VLM permissions, incremental ingest and validation/application, deposit rendering and draining, CommitGate admission, retrieval assembly, answer generation, remote research/query, policy distillation/bootstrap/edit, skill emission, draft closing/finalization, scheduler execution, web authentication and host hooks. These are additional implementation anchors under SRC-1, not new sources. Detailed source acquisition adapters, individual migrations, reversal implementations and every maintenance command were not exhaustively inspected; this report does not generalize the selected enforcement points to them.

### Ordinary invocation: ingest with optional authorship

An ordinary authored ingestion is `wiki ingest <input> --domain <domain> --with-plan`. CLI dispatch calls `ingest`; file, canonical-markdown and URL entry paths converge on canonical text admission. The user or foreground agent selects the input/domain and flags; that initiation is not approval of each generated page. The CLI rejects an explicit nonexistent policy when authorship is requested. Source conversion precedes source-schema/hash/wikilink checks. A per-source lock encloses immutable-body comparison, filtering, raw/source-page writes and index/log bookkeeping. SRC-1: `src/gateway/cli.py`, `src/gateway/ops/ingest.py`; [RT-RTE-ingest-authorship](#rt-rte-ingest-authorship).

For a new source, filter code loads domain criteria and selected examples, invokes the filter model, and compares its score with policy thresholds. Raw markdown persists even when the source is review/rejected/skipped/errored; a wiki source page is written for included or no-domain decisions. `--force-include` skips the filter model. The identical-source path may backfill a missing source page and may run authorship against already-retained raw text. Thus source admission, wiki-source admission and generated-page admission are separate results. SRC-1: `src/gateway/ops/ingest.py`.

Authorship code constructs a task system prompt and supplies source text plus selected existing pages. Source bodies are capped at 16,000 characters; existing pages are selected by title-query/domain ranking, with an unranked glob fallback, a 30-page ceiling and a 60,000-byte budget. Existing pages are kept whole; the first can exceed the budget. The plan model returns JSON-shaped updates and contradictions. Code parses the expected source ID and full-page updates, validates, applies, or feeds parse/validation errors and the prior response back for one repair attempt. The default client has no model tools: it is a returning computation, not a worker free to write the vault. Model identities and mutability are recorded separately below. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/plan.py`, `src/gateway/llm/client.py`.

`apply_plan` validates every update before entering `wiki-author`, then writes per-file atomically with saved prior text for rollback on exceptions. Backlinks, contradictions and log writes follow page writes. Its guarantee is an exception-recovery protocol, not a crash-atomic multi-page transaction: rollback itself suppresses `OSError`, validation occurs before lock acquisition, and no shared CommitGate CAS is used on this path. An authorship failure does not undo the source ingest; the outer operation can return success with a warning and a saved rejected plan. These distinctions matter to callers deciding whether knowledge was actually authored. SRC-1: `src/gateway/ops/apply_plan.py`, `src/gateway/ops/ingest.py`.

> wiki authorship failed (source page still committed):
> --- `src/gateway/ops/ingest.py`

### Material alternate routes and forcing cases

**1. Durable asynchronous deposits versus synchronous plans.** MCP `wiki_deposit` validates a typed payload and identity, enqueues a content-addressed intent, and returns a receipt. Canonical writing requires the separate shipped CLI commit-worker. It reclaims expired leases, claims an intent, renders caller-supplied markdown without an authorship model, and calls CommitGate. The gate serializes on `librarian-commit`, checks committed history/fencing, runs deterministic dedup and contradiction/domain routing, classifies per-page HEAD changes, and commits explicit paths with an intent trailer. It does not call `apply_plan` or its page-schema/citation-loss validation on the inspected normal deposit commit path. Its mutex differs from `wiki-author`, and HEAD CAS does not compare a live uncommitted filesystem edit. A blanket “all canonical writes are one validated serial commit” is therefore unwarranted. SRC-1: `src/gateway/mcp_server.py`, `src/gateway/ops/deposit.py`, `src/gateway/ops/committer.py`, `src/gateway/commit_gate.py`; [RT-RTE-deposit-commit](#rt-rte-deposit-commit).

> Body is passed through VERBATIM (agent-supplied markdown).
> --- `src/gateway/ops/committer.py`

The shape validator accepts source deposits, but the drain renderer rejects that page type and dead-letters it. `volatile` adds `canonicalize: False` to the receipt; the inspected `drain_once` normal-deposit branch nevertheless renders and commits without testing that flag. Treat the receipt as an advisory result, not established noncanonicalization. Durable claims require at least one resolvable ingested-source link at enqueue, not proof that each claim is supported. Atomic file replacement establishes restart-visible intent storage, not an inspected fsync/power-loss guarantee. SRC-1: `src/gateway/ops/deposit.py`, `src/gateway/ops/committer.py`, `src/gateway/intent_queue.py`.

**2. Draft grounding versus strict grounding.** A plan can admit drafts with citation errors downgraded, and retrieval includes drafts by default. It removes placeholder-only sections and marks draft blocks but does not require finalization before later consumption. `wiki finalize` restores strict validation, clears draft metadata only after success, and writes under `wiki-author`; abandonment deletes the draft and removes backlinks. The draft-closer dispatches easy cases to this validator and escalates failures. Its documentation says both a one-source limit and a per-line citation limit apply, but `_is_easy_win` checks only the latter. No autonomous attribution-quality conclusion follows. SRC-1: `src/gateway/ops/apply_plan.py`, `src/gateway/ops/retrieve.py`, `src/gateway/ops/finalize.py`, `src/gateway/agents/draft_closer.py`; [RT-RTE-draft-finalization](#rt-rte-draft-finalization).

**3. Model calls are not one isolation envelope.** Planning/filtering normally use `claude -p --tools "" --no-session-persistence`; answer uses a direct Anthropic SDK call, with a separate API key and cacheable context prefix; VLM permits the host Read tool and passes `--dangerously-skip-permissions`. The SDK answer call sends messages/system/model/max_tokens, not a shell tool declaration. The VLM path's explicit image argument and description prompt are scope guidance, not an OS sandbox. Scheduler jobs use arbitrary `shell=True` commands in the knowledge root. Foreground agents and extensions inherit whatever host permissions the deployment grants, which are not supplied here. SRC-1: `src/gateway/llm/client.py`, `src/gateway/llm/api_client.py`, `src/gateway/vlm.py`, `src/gateway/scheduler.py`.

> tools="Read",
> extra_args=["--dangerously-skip-permissions"],
> --- `src/gateway/vlm.py`

**4. Policy-edit gates versus other policy producers.** Privileged policy-edit has a server-environment principal check, queued admission and apply-time evaluator gates. But `bootstrap-domain` writes a schema-valid model-generated policy directly and can overwrite an existing non-proposal policy with `force`; it does not traverse those gates. Distillation writes candidates, not the live policy. Generated domain skills also write directly under `.claude/skills/`. Thus the dual evaluator gate is a policy-edit-route property, not a universal instruction or policy admission guarantee. SRC-1: `src/gateway/ops/policy_edit.py`, `src/gateway/commit_gate.py`, `src/gateway/ops/bootstrap_domain.py`, `src/gateway/ops/finetune.py`, `src/gateway/ops/skill_emit.py`; [RT-RTE-policy-edit](#rt-rte-policy-edit), [RT-RTE-policy-bootstrap](#rt-rte-policy-bootstrap), [RT-RTE-policy-distillation](#rt-rte-policy-distillation).

### Consumption, research and coordination

Retrieval combines lexical section ranking with optional dense retrieval and weighted reciprocal-rank fusion on the single-domain path. Multi-domain queries instead use per-domain lexical quotas and round-robin interleaving. Code reloads section text, skips empty/placeholders, truncates long sections, adds XML-like page metadata and stops at the overall budget only after at least one block exists. The first block may exceed the requested budget; truncation can remove a trailing citation. Therefore “bounded” describes controls with these exceptions, not a strict context-length or complete-provenance invariant. The answer model receives the resulting block, not the whole vault. Postprocessing strips citation IDs absent from that block; it does not check that surviving claims are entailed. Optional filing always uses draft application. SRC-1: `src/gateway/ops/retrieve.py`, `src/gateway/ops/answer.py`; [RT-RTE-retrieve-answer](#rt-rte-retrieve-answer).

> if total + len(block) > budget_chars and blocks:
>     break
> --- `src/gateway/ops/retrieve.py`

Research is a larger code-owned sequence: select/infer a registered domain, generate/load query plans, optionally return for human review, search adapters, filter candidates, materialize sources, test corpus sparsity, create/register persistent and session notebooks, push sources, map citations, probe indexing settlement, request analysis, build/apply a synthesis plan, then best-effort promote sources into the persistent corpus. Source-upload failures are isolated; failure through plan application abandons the session; post-application promotion failures are warnings and leave wiki output in place. An ordinary `query` consumes the persistent notebook, reloads/builds its source map, renders citation markers and files through `apply_plan`, automatically drafting when every resolved citation is an external unresolved marker. Provider-internal corpus selection and model reasoning are opaque. SRC-1: `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py`; [RT-RTE-research-query](#rt-rte-research-query).

Browser operations return asynchronous task receipts for ingest/query; web middleware checks bearer authentication for nonpublic `/api/` endpoints and limits non-GET requests per token. This protects that HTTP mount, not CLI calls, MCP functions or filesystem access. MCP's separate read server registers an explicit allowlist, while the ordinary `run()` starts the full registered server. The read-tier label is not literally side-effect-free: its own contract permits logs and FTS healing, and retrieve misses also have a best-effort DemandLedger producer. The selected mount is a tool grant set, not proof that the host lacks shell or direct-filesystem capabilities. SRC-1: `src/gateway/web/routes/ops.py`, `src/gateway/web/app.py`, `src/gateway/web/auth.py`, `src/gateway/tier.py`, `src/gateway/mcp_server.py`, `src/gateway/ops/retrieve.py`.

Scheduled maintenance has a code cron selector, per-job lock, failure cooldown and one-hour subprocess ceiling. The scheduler persists last-run/exit/duration state; no shipped automatic test-to-code-rewrite loop is established by this mechanism. Converter and poller extensions require package registration/code changes; hardcoded commit/deposit thresholds require code-review/merge by doctrine. Those product/machinery admissions depend on contributor/host Git practice, not a running model gate established here. SRC-1: `src/gateway/scheduler.py`, `CLAUDE.md`, `src/gateway/ops/policy_edit.py`.

### Guarantee ledger

Each row separates implementation from operation. External contracts are prerequisites, not verified deployment facts.

| Guarantee and owner | Enforcement and strength | Covered paths; alternate paths and limits | Required external contract | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| Immutable raw body; ingest code | Existing-body comparison inside per-source lock; protocol | Incremental canonical ingestion; other writers/manual filesystem writes not established by this check | Cooperative locks and writable local filesystem | wired | uninspected |
| Validated authored page admission; apply-plan code | Parse/schema/citation checks, citation-loss and shrink guards; protocol | Plans and strict finalization; draft downgrade, deposit and direct filesystem paths differ. Citation shape is not factual entailment | Caller uses these operations; current files stable across validation/write gap | wired | uninspected |
| Multi-page application; apply-plan code | Snapshots plus per-file replacement and exception rollback; best effort | Plan page writes; crash recovery and rollback failure not covered as all-or-nothing; postcommit bookkeeping separate | Filesystem rename semantics; restore succeeds | wired | uninspected |
| Deposit receipt survives process restart; IntentQueue | JSON temporary-file replacement before enqueue return; protocol | Deposits; watcher pending state and web task receipts not equated with this queue. Power-loss durability not established | Same-filesystem rename and retained disk state | wired | uninspected |
| Serialized/fenced deposit Git admission; CommitGate | Commit mutex, stale-token comparison, HEAD CAS and exact history trailer matching; protocol | Cooperating gate workers; synchronous plan lock, uncommitted edits, external Git users and shell access are alternate routes | Git history retained; peers obey same gate/locks; no adversarial queue mutation | wired | uninspected |
| Read mount excludes build tools; MCP factory | Explicit allowlist registration; invariant | Read server tool dispatch only; full server, CLI, shell and derived read side effects remain | Host actually mounts read server and restricts other capabilities | wired | uninspected |
| HTTP authentication; web middleware | Bearer verification default-deny for nonpublic `/api/`; protocol | HTTP API; public health/static content and non-HTTP calls outside check | Secret handling, TLS/exposure and token configuration | wired | uninspected |
| Grounded answer; answer code/model | Prompt-only facts constraint plus unknown-ID stripping; policy | Direct answer generation; preserves possible unsupported prose and misused valid IDs | Model compliance and adequate retrieved evidence | wired | uninspected |
| Policy-edit change control; enqueue/gate code | Principal allowlist, version-at-enqueue, retrieval floor and proposed dedup golden checks; protocol | Policy-edit only; bootstrap/force/manual/config changes bypass it; explicit dev missing-golden skips exist | Server env trustworthy, goldens representative, queue protected | wired | uninspected |

Evidence for these rows is retained in the corresponding route records and the forcing-case passages above: SRC-1 `src/gateway/ops/ingest.py`, `src/gateway/ops/apply_plan.py`, `src/gateway/intent_queue.py`, `src/gateway/commit_gate.py`, `src/gateway/mcp_server.py`, `src/gateway/web/app.py`, `src/gateway/ops/answer.py`, `src/gateway/ops/policy_edit.py`.

## Shared records

### Components

#### RT-CMP-claude-haiku
Label: Claude Haiku filter component

Source-native identity: `claude-haiku-4-5-20251001`, selected by `model_for("filter")`; distributed-parametric model, provider-side weights, accessed through the Claude CLI. The dated request identifier is fixed in shipped defaults; an exact weight/version digest and provider alias contract are not pinned in SRC-1. A mutable provider endpoint may resolve differently; this is uninspected. Inspected calls perform inference, not a parameter-update operation; provider-side parameter changes remain uninspected. Used in filter and distillation calls. SRC-1: `src/gateway/llm/config.py`, `src/gateway/ops/finetune.py`, `src/gateway/ops/ingest.py`.

> DEFAULT_FILTER_MODEL = "claude-haiku-4-5-20251001"
> --- `src/gateway/llm/config.py`

#### RT-CMP-claude-opus
Label: Claude Opus authorship and vision component

Source-native identity: `claude-opus-4-7`; distributed-parametric model with opaque provider-side storage. Selected for ordinary large-source authorship and VLM. Parameters are not updated by inspected inference routes; provider internals are uninspected. The request name is pinned in code but exact weights are not; mutable endpoint resolution remains outside evidence. VLM and plan grants differ even when they select this same model. SRC-1: `src/gateway/llm/config.py`, `src/gateway/plan.py`, `src/gateway/vlm.py`.

> DEFAULT_PLAN_AUTHORSHIP_MODEL = "claude-opus-4-7"
> --- `src/gateway/llm/config.py`

#### RT-CMP-claude-sonnet
Label: Claude Sonnet bounded generation component

Source-native identity: `claude-sonnet-4-6`; distributed-parametric model with opaque provider storage. Used for small-source plans, domain bootstrap, query planning and local answer generation; answer permits a caller model override. No parameter changes are performed by these inspected inference routes. Neither an exact weight snapshot nor provider endpoint immutability is established; the name is a default, not a reproducibility guarantee. SRC-1: `src/gateway/llm/config.py`, `src/gateway/ops/answer.py`, `src/gateway/ops/ingest.py`.

> _DEFAULT_MODEL = "claude-sonnet-4-6"
> --- `src/gateway/ops/answer.py`

#### RT-CMP-qwen3-embedding
Label: Qwen3 retrieval encoder

Source-native identity: checked-in `mlx-community/Qwen3-Embedding-4B-4bit-DWQ` at dimension 2560. Distributed-parametric weights load locally through MLX; dense vectors are derived numerical retrieval state. The inspected encoder performs inference and normalization, not training. No model revision/digest is supplied to `load`; a mutable model identifier can resolve differently. Environment precedence can replace the selected encoder; exact production weights and installation are uninspected. This is separate from deterministic lexical hashing used by the deposit dedup index. SRC-1: `.knowledge/retrieval.yaml`, `src/gateway/retrieval_encoder.py`.

> self._model, self._tok = load(self.model_id)
> --- `src/gateway/retrieval_encoder.py`

#### RT-CMP-notebooklm
Label: NotebookLM remote synthesis component

Source-native identity: NotebookLM accessed by `NlmCLIClient`. Distributed-parametric synthesis is supplied by an external service whose exact model, weights, storage and parameter-update behavior are uninspected. No exact model version is pinned in the inspected query/research invocation; service-side model replacement is unresolved. Local notebook IDs and source maps are not model-version pins. SRC-1: `src/gateway/ops/query.py`, `src/gateway/research/orchestrator.py`.

> response = nlm_client.notebook_query(notebook_id, question)
> --- `src/gateway/ops/query.py`

### Operative objects

#### RT-OBJ-plan
Label: Plan and WikiUpdate admission payload

Source-native identity: Python `Plan`, `WikiUpdate` and `Contradiction`, parsed from model JSON. Symbolic fields determine target/type/operation; embedded markdown carries natural-language knowledge. This record identifies the admission envelope, not the retained wiki body. Storage is current-run Python objects; rejected response/error text can persist under `.knowledge/rejected-plans/`. Authorship parser checks source ID and update shape before page validators. SRC-1: `src/gateway/plan.py`, `src/gateway/ops/ingest.py`.

> target_path: str          # e.g. "wiki/entities/semaglutide.md"
> update_kind: str          # "create" | "update"
> content: str              # full canonical markdown text (frontmatter + body)
> rationale: str = ""
> --- `src/gateway/plan.py`

#### RT-OBJ-intent
Label: Intent queue admission envelope

Source-native identity: `Intent`, with payload, identity, optional dependency and content-addressed ID. Symbolic lifecycle/control data are JSON files under `.knowledge/intents/<state>/`; deposited body text is natural-language payload, interpreted separately by later readers. Lease/fencing and results persist beside lifecycle state. Git intent trailers supply a separate committed-history identity. SRC-1: `src/gateway/intent_queue.py`, `src/gateway/ops/deposit.py`, `src/gateway/commit_gate.py`.

> submitted/<intent_id>.json
> claimed/<intent_id>.json
> authored/<intent_id>.json
> committed/<intent_id>.json
> rejected/<intent_id>.json
> dead_lettered/<intent_id>.json
> --- `src/gateway/intent_queue.py`

### Routes

#### RT-RTE-ingest-authorship
Label: Incremental ingest and authored page admission

Endpoints/progression: CLI/MCP/browser ingestion → converter/canonical source checks → filter → raw/source page → optional plan model → parse/validate/apply → operation result. Code owns progression; caller owns input/domain/flags. Filter score and prose plan are model proposals, while thresholds and validators decide admission. No per-content human approval is wired in the normal path; force inclusion is a caller override, whose human identity is unresolved. Operating mode is an open source-ingest request with one bounded repair attempt; there is no expected-answer oracle. Guidance is source content, selected existing pages and the shipped authorship/schema prompt. Proposed full-page changes can be rejected before write; exception rollback is best effort, rejected plans can be saved. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/ops/apply_plan.py`, `src/gateway/plan.py`.

- Immediate return: OperationResult distinguishes source admission from authorship warnings/report; CLI maps it to printed outcome.
- Later read-back: Canonical source/page writes can be loaded by later authorship and retrieval calls; saved rejected plans are operator repair material, not automatically accepted pages.
- Delegated visibility: Model receives capped source and whole selected existing pages; no full repository or ordinary tools are granted by the default plan call.
- Selection predicate: Source type/input dispatch; domain policy thresholds for source-page admission; title-ranked domain pages with glob fallback for authorship context.
- Invalidation or expiry: Existing-source body equality gives no-op/backfill; page updates replace text; rejected-plan scratch has no inspected expiry.
- Activation or effect: Code can persist accepted pages and metadata; actual model compliance and downstream behavioral activation are unobserved.
- Evidence limits: Source inspection only; converter-by-converter behavior and factual entailment of generated claims are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _MAX_REPAIR_ATTEMPTS = 1
> --- `src/gateway/ops/ingest.py`

> except OSError:
>     pass  # best-effort restore; report the original failure
> --- `src/gateway/ops/apply_plan.py`

#### RT-RTE-deposit-commit
Label: Durable deposit to Git admission

Endpoints/progression: `wiki_deposit` → deposit validation/submit → receipt; shipped commit-worker → lease claim/render → gate → Git/result state. Identity is caller-supplied for ordinary deposits and enters the intent hash; a queue receipt is not principal authentication or canonical admission. Code renders supplied markdown, decides dedup/domain/CAS outcomes and can reject, quarantine or dead-letter. Human authorship of payload is unresolved; no human approval is required in the drain. Operating mode is an asynchronous open deposit request; no answer oracle is used for ordinary commits. Admission guidance is the gate's deterministic policies and caller content. Rollback/recovery uses recorded write sets, startup recovery and lease reclamation; overlap can require manual merge. SRC-1: `src/gateway/ops/deposit.py`, `src/gateway/ops/committer.py`, `src/gateway/commit_gate.py`, `src/gateway/intent_queue.py`.

- Immediate return: Queued intent ID and retry hint; terminal disposition arrives later through polling/drain result.
- Later read-back: Worker reloads durable JSON; Git history resolves redelivery; committed markdown enters later retrieval and dedup.
- Delegated visibility: Thin renderer gets intent payload and relevant HEAD blob; gate gets authored writes, base OIDs and fencing token, not a separate authoring model context.
- Selection predicate: Payload shape/backlog admission, lease claiming and gate-dispatch keys; dedup/domain/CAS policies determine canonical target or failure.
- Invalidation or expiry: Lease expiry requeues stranded claims; stale fencing is rejected; exact intent trailer matches suppress committed redelivery.
- Activation or effect: Normal path writes files, stages explicit paths and creates an intent-tagged Git commit; volatile receipt is not enforced as a skip by inspected drain code.
- Evidence limits: No concurrency/crash execution supplied; HEAD comparisons do not protect live uncommitted edits or noncooperating writers; source deposits can queue but cannot render.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if current is not None and fencing_token < current:
> --- `src/gateway/commit_gate.py`

> self._git("add", "--", *[str(p) for p in touched])
> --- `src/gateway/commit_gate.py`

#### RT-RTE-draft-finalization
Label: Draft validation and finalization

Endpoints/progression: Human/agent finalize request or draft-closer stale-draft scan → page/type checks → strict validator → clear metadata/write/log, or return/escalate errors. Code owns decisions; automatic closer proposes candidates, full validator can veto. There is no expected truth oracle and no human approval on automatic easy cases. This is bounded maintenance, not model-directed revision. It applies existing schema/citation guidance without revising it. Abandonment is an explicit deletion alternative with backlink removal; no automatic undo is inspected. SRC-1: `src/gateway/ops/finalize.py`, `src/gateway/agents/draft_closer.py`.

- Immediate return: Finalized path or unresolved errors; closer returns finalized/escalated/skipped counts.
- Later read-back: Updated draft/finalization metadata and unchanged body are consumed by later retrieval/maintenance; escalation text is retained in the log.
- Delegated visibility: inapplicable — the inspected closer is code, not a delegated model; it scans page frontmatter/body and invokes finalize.
- Selection predicate: Stale-draft findings; easy-win implementation checks no line has more than one source link, not the documented synthesizes-count condition.
- Invalidation or expiry: Successful finalization removes draft metadata; abandon deletes the page and removes source backlinks.
- Activation or effect: Strictly validated draft can become nondraft; no citation truth or autonomous attribution quality is established.
- Evidence limits: Already-nondraft pages return failure despite the docstring's no-op claim; no supplied maintenance execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> strict_front, body, page_type, draft=False, body_line_offset=body_offset
> --- `src/gateway/ops/finalize.py`

#### RT-RTE-retrieve-answer
Label: Retained wiki retrieval and local answer

Endpoints/progression: Explicit question → retained section ranking/assembly → direct Anthropic inference → strip unknown citation IDs → answer/log → optional draft plan. Code selects context and postprocesses; model proposes answer prose. Caller can request filing, but no per-claim human approval is wired. The operating mode is open question answering; an expected answer/reference outcome is not used. Guidance asks only context-supported facts and inline citations, but the code does not verify entailment. Draft filing can be rejected by `apply_plan`; subsequent strict finalization is separate. SRC-1: `src/gateway/ops/retrieve.py`, `src/gateway/ops/answer.py`, `src/gateway/llm/api_client.py`.

- Immediate return: Bounded-with-exceptions page blocks and metadata, or answer text/valid source IDs/stripped IDs/usage; empty retrieval avoids the model call.
- Later read-back: Retrieval reads retained wiki content; optional answer draft is available to later retrieval; misses can add demand gaps for later demand processing.
- Delegated visibility: Answer model receives the assembled selected block plus question and system constraints, not all indexed pages; API prefix requests ephemeral caching.
- Selection predicate: Single-domain hybrid lexical/dense RRF or lexical-only; multi-domain lexical quotas; empty/placeholder sections excluded, drafts admitted and marked by default.
- Invalidation or expiry: Derived index healing and content reload follow canonical files; provider cache lifetime is external; filing creates a draft rather than changing model weights.
- Activation or effect: Code supplies retained content and removes unknown-ID links; actual factual compliance and later behavioral effects remain unobserved.
- Evidence limits: Section truncation may drop citations; first block can exceed requested total budget; valid citation membership is not semantic support.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if sid in valid:
>     return m.group(0)
> stripped.append(sid)
> return ""
> --- `src/gateway/ops/answer.py`

#### RT-RTE-research-query
Label: Remote research corpus construction and query filing

Endpoints/progression: Research request or resumed query plan → code-owned acquisition/filter/materialization → session NotebookLM upload/analysis → cited plan/application → best-effort persistent promotion; later query → persistent notebook response/source-map rendering → synthesis plan. Caller provides problem/domain and optionally edits/reviews a plan; review is opt-in, not compulsory per-output approval. Model/provider proposes queries, scores and synthesis; local code decides thresholds and plan admission, remote internals decide uninspected synthesis. Operating mode is open research with optional staged human review; no expected-answer oracle is used in this loop. Guidance is domain policy, research prompt, generated or edited queries and citations; retained results include plans, corpus mappings and wiki pages. Failure through application abandons session; source uploads isolate individual errors, while post-apply promotion failure is warning-only. SRC-1: `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py`.

- Immediate return: Optional plan review gate, no-op/error, or authored-page summary; ordinary query returns plan application outcome.
- Later read-back: `--execute` reloads retained query plans; later query uses persistent notebook IDs/corpus/source maps; wiki retrieval consumes accepted synthesis pages.
- Delegated visibility: External services receive uploaded URLs/text and research/query prompts; exact remotely indexed subset and model-visible corpus are not available from local bookkeeping alone.
- Selection predicate: Registered domain/policy, adapter query plan, acceptance thresholds, corpus sparsity check, successful pushes and citation/source-map resolution.
- Invalidation or expiry: Session abandonment/promotion and retry registration control registry state; missing source map triggers rebuild; provider retention/index expiry remains uninspected.
- Activation or effect: Gateway can materialize raw sources, create remote notebooks and file wiki synthesis; downstream effects and remote grounding success are unobserved.
- Evidence limits: Settle probing measures distinct cited sources, not proof of complete indexing; review and corpus quality gates are bypassable modes, not universal guarantees.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> edit and resume with `wiki research --execute {session_id}`
> --- `src/gateway/research/orchestrator.py`

> plan_result = apply_plan(plan, draft=draft)
> --- `src/gateway/research/orchestrator.py`

#### RT-RTE-policy-distillation
Label: Example-fed editorial policy candidate distillation

Endpoints/progression: Finetune request/threshold check → load current policy and example bank → model distillation → parsed criteria → optional calibration → candidate version YAML. Code owns progression and candidate admission; model proposes criteria, human review/promotion is declared but not performed by `distill_prompt`. Default threshold is 500 examples, overridable by caller; prompt caps include/exclude examples separately. Operating mode is bounded example-fed candidate generation, not autonomous deployment. Optional held-out calibration supplies reference labels when available; its dataset provenance and scoring implementation were not inspected here, so no oracle correctness or candidate-quality result is established. Rejection occurs for missing policy/examples/threshold or unparseable response. Live policy is not overwritten, so keeping the incumbent is the local recovery mechanism. SRC-1: `src/gateway/ops/finetune.py`.

- Immediate return: Candidate path, examples count, summary and optional calibration F1.
- Later read-back: Candidate YAML persists for review; automatic promotion/next-round reuse is not wired by this function.
- Delegated visibility: Model sees current domain topic/criteria and sampled example titles plus capped rationales, not all source bodies or the full bank.
- Selection predicate: Domain bank and threshold; first sampled include/exclude examples under the prompt cap.
- Invalidation or expiry: Timestamped candidate versions preserve alternatives; no inspected expiry or automatic live replacement.
- Activation or effect: Writes proposed future filter guidance, not model weights or a live policy update.
- Evidence limits: No candidate execution, human promotion, improved future capacity or causal benefit supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Theory account: Editorial inclusion/exclusion criteria are localized guidance about what belongs in a domain; the prompt asks to derive tighter criteria from existing decisions, add evidenced criteria and remove nondiscriminating ones. A whole candidate replaces criteria lists but preserves other domain fields. Current criteria are consumed during generation; candidate criteria persist in version YAML with summary and optional calibration metrics. This is an inspectable revision request, not evidence that the model formulated a specific criticism naming claim, outcome and blame.

- theory-builder conditions 1–4: Condition 1 conclusion status: wired — full criteria lists are localized natural-language units. Condition 2 conclusion status: wired — prompt construction and candidate serialization use their contents. Condition 3 conclusion status: uninspected — inspected prompting requests changes but exposes no actual content-directed criticism with blame and changed reliance. Condition 4 conclusion status: uninspected — candidate retention does not establish a next criticism round consuming its result.
- Addressability: Criteria are individually inspectable list items; assumptions and scope may be implicit in their prose. Exact candidate contents are not assessed.
- Persistence: Candidate YAML across sessions; later human reviewer is intended, not observed.
- learning: uninspected — improvement in future action and attribution are not supplied; example accumulation and candidate generation alone do not establish it.
- Reflection: Example decisions represent prior filter operation and can shape candidate policy, but inspected candidate generation stops before live installation; both live causal directions are not established here.
- Reflective theory builder: uninspected — content-directed criticism and retained iterative reliance are unresolved.
- Autonomous theory builder: uninspected — human promotion remains part of declared deployment and conditions 3–4 are unresolved independently.

> "4. Removes criteria that are redundant or never appear to discriminate.",
> --- `src/gateway/ops/finetune.py`

#### RT-RTE-policy-bootstrap
Label: Model-authored live policy bootstrap

Endpoints/progression: CLI/MCP/browser description/slug → existing-policy/proposal checks → reference-policy prompt → model generation → strict policy validation with one corrective attempt → direct live YAML write, or draft YAML/error. Caller proposes problem/slug and optional force; model supplies criteria; code decides schema admission without per-content human approval. Operating mode is open domain creation; schema reference is guidance, not an expected semantic answer oracle. Force can overwrite a non-proposal existing policy; no automatic backup/revert is implemented in the inspected commit helper. This is separate from policy-edit and distilled candidate admission. SRC-1: `src/gateway/ops/bootstrap_domain.py`.

- Immediate return: Written policy path/warnings or errors and best-effort draft.
- Later read-back: Filter reloads live policy; generated criteria can govern future source admission.
- Delegated visibility: Model sees description, slug and shipped reference policy/schema guidance, with errors on the second attempt.
- Selection predicate: Valid slug, proposal/existing-policy checks and strict policy validator; force permits overwrite except promoted-policy cases.
- Invalidation or expiry: Replacement under bootstrap lock; no inspected policy version history/rollback in this write helper.
- Activation or effect: Direct policy file write changes future filter input without going through CommitGate evaluator gates.
- Evidence limits: No evidence of semantic quality or model compliance beyond shape validation; no supplied future filter run.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Theory account: The generated editorial criteria formulate domain scope guidance. Reference-policy/schema text shapes the proposal. Validator errors can drive another proposal, but schema repair is not demonstrated criticism of the policy's domain theory. What persists is criteria and description hash in live/draft YAML.

- theory-builder conditions 1–4: Condition 1 conclusion status: wired — criteria lists are localized text. Condition 2 conclusion status: wired — accepted policy is loadable by filter decisions. Condition 3 conclusion status: uninspected — no domain-theory criticism/result/blame is exposed by the schema retry. Condition 4 conclusion status: uninspected — no retained content-directed criticism guiding another theory round is established.
- Addressability: Named YAML criteria and domain fields are separately inspectable/editable; rationale for each rule need not persist.
- Persistence: Live policy across source requests; candidate draft persists on final validation failure.
- learning: uninspected — revised policy availability does not demonstrate improved capacity or attribution.
- Reflection: uninspected — description-led bootstrap does not by itself establish representation of this system's own operation and both causal directions.
- Reflective theory builder: uninspected — criticism of its own method from operation is not established.
- Autonomous theory builder: uninspected — computational authorship/admission alone does not establish conditions 3–4.

> if result.ok:
>     return _commit_policy(slug, data, warnings + [str(w) for w in result.warnings])
> --- `src/gateway/ops/bootstrap_domain.py`

#### RT-RTE-policy-edit
Label: Privileged queued policy replacement

Endpoints/progression: CLI policy mapping/reason → server-environment principal allowlist → shape/version-at-enqueue → intent queue → worker special dispatch → evaluator gates → contained policy write/Git provenance, or dead-letter. Caller proposes full replacement; code checks configured principal and gates. “Human CLI only” is intent and MCP surface restriction, not human authentication against shell-capable agents. Operating mode is explicit policy replacement with bounded golden checks; retrieval goldens provide expected relevance and merge goldens expected dedup decisions. Retrieval floor tests current FTS behavior; proposed dedup parameters are separately evaluated. No evaluation of every editorial criterion or trust/contradiction change is established. Enqueue checks version; the inspected apply helper does not recheck it against disk, so concurrent queued versions are not a proven stale-write exclusion. Recovery uses CommitGate write/commit machinery; rollback after acceptance is not automatic in this helper. SRC-1: `src/gateway/ops/policy_edit.py`, `src/gateway/ops/committer.py`, `src/gateway/commit_gate.py`.

- Immediate return: Rejection or intent receipt; later terminal status after worker gates.
- Later read-back: Accepted policy persists in tracked YAML/Git and can be consumed by later filter/policy-dependent operations; provenance carries reason/principal/version.
- Delegated visibility: Worker gets policy payload via durable intent; evaluator receives goldens and proposed dedup parameters, not a delegated model judge.
- Selection predicate: Configured allowlisted principal, valid domain/policy/reason/version; retrieval recall floor and proposed merge-map nonregression; contained target.
- Invalidation or expiry: Enqueue version rejects known stale proposal; worker lease expiry and dead-letter handling follow queue protocol. Apply-time version freshness remains unresolved.
- Activation or effect: Gate can commit replacement policy; actual consumer reload/use and successful improvement are unobserved.
- Evidence limits: Missing goldens may be dev-skipped explicitly; bootstrap, shell/filesystem and other config writers are alternate paths. Gates do not prove all changed policy semantics improve.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Theory account: Full policy mappings may include domain criteria; this route does not itself formulate or criticize them. It preserves caller reason and applies deterministic nonregression checks to a subset of proposed behavior. Numerical regression alone is not content-directed criticism.

- theory-builder conditions 1–4: Condition 1 conclusion status: afforded — a full mapping can carry localized criteria. Condition 2 conclusion status: wired — dedup proposal content determines gate simulation. Condition 3 conclusion status: uninspected — no formulated theory criticism with blame is established. Condition 4 conclusion status: uninspected — retained reason/provenance is not demonstrated iterative criticism consumption.
- Addressability: Policy fields are inspectable/editable; gate coverage is limited to tested behavior.
- Persistence: Tracked policy/provenance across sessions; later consumers are policy-dependent operations.
- learning: uninspected — no improved future capacity/attribution evidence supplied.
- Reflection: uninspected — change-control and reasons alone do not establish both representation-mediated causal directions.
- Reflective theory builder: uninspected — no criticism of method against its own operation records is established.
- Autonomous theory builder: uninspected — proposer/human contribution unresolved and conditions 3–4 unresolved.

> dev_skip = bool(os.environ.get("GATEWAY_DEV_SKIP_POLICY_GATES"))
> --- `src/gateway/commit_gate.py`

> This is change-control + an unspoofable audit principal, not a hard boundary
> against a process that already has shell access: a build-tier agent with full
> Bash can shell out to any ``wiki`` command, so an in-request allowlist was never
> a hard boundary against that agent.
> --- `src/gateway/ops/policy_edit.py`

#### RT-RTE-skill-emission
Label: Retained domain skill generation

Endpoints/progression: Explicit skill-emit → policy/MOC/synthesis-title loaders → deterministic render/cap → `.claude/skills/wiki-<domain>/SKILL.md` write/log. Code proposes and admits derived instruction text; caller selects domain; no per-content human review or semantic answer oracle. Mode is deterministic instruction derivation, not model learning. Guidance includes domain inclusion/exclusion criteria, selected entity/concept links, recent synthesis titles and usage commands. Regeneration replaces output; no automatic previous-version rollback in this function. The generated text's claimed triggers require external host skill discovery. Contrary to module-description claims of recent log consumption, inspected rendering obtains open threads from synthesis titles and does not load recent logs. SRC-1: `src/gateway/ops/skill_emit.py`.

- Immediate return: Generated path and line count or missing-policy/MOC error.
- Later read-back: Persisted skill can be discovered/read by later Claude Code sessions; automatic host loading and actual use are unobserved.
- Delegated visibility: inapplicable — renderer is deterministic code; later host/model receives only emitted content when discovery/loading occurs.
- Selection predicate: Policy/MOC presence; first concept/entity links and reverse-filename-ordered domain synthesis titles with count caps.
- Invalidation or expiry: Regeneration overwrites skill; 295-line rendering cap can omit tail content; no inspected expiry.
- Activation or effect: Writes a host instruction artifact, not executable plugin code or model parameters; later behavioral effect remains unobserved.
- Evidence limits: Automatic regeneration at every claimed bootstrap/promote/steward trigger was not established by inspected callers; module claim is not substituted for wiring.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> skill_path.write_text(content, encoding="utf-8")
> --- `src/gateway/ops/skill_emit.py`

#### RT-RTE-session-reanchor
Label: Development-session compaction and resumption instructions

Endpoints/progression: Claude Code PreCompact/SessionStart events → configured shell hooks → stdout instruction → foreground agent requested snapshot/commit or reread/verification. Host owns actual compaction; scripts emit instructions rather than writing/checking state themselves. Agent is the proposed author/decider; human is asked to resolve disagreement. Operating mode is session maintenance, not a tested theory revision loop; no answer oracle. Guidance enumerates contracts, mid-edit files, decisions, rejected approaches and next step. Retained document should carry selected working memory to later sessions; failure recovery depends on host/agent compliance. SRC-1: `.claude/settings.json`, `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `CLAUDE.md`.

- Immediate return: Hook stdout becomes additional host context; it is not a completed snapshot receipt.
- Later read-back: Requested `docs/session-state.md` snapshot and commit can survive sessions; SessionStart instruction asks reread under an mtime condition, while CLAUDE's condition differs.
- Delegated visibility: Host injects hook text into foreground session; which old turns are removed, verbatim tail/host summary retained and exact delivery are outside inspected implementation.
- Selection predicate: Host event matchers; snapshot sections select unresolved work/decisions; reanchor text uses existence/mtime predicate.
- Invalidation or expiry: Next snapshots can replace state; instructions ask verification against tree and escalation of disagreement, not automatic stale-state rejection.
- Activation or effect: Wired request to external host/agent, not guaranteed file write, commit or resume compliance.
- Evidence limits: No host trace or target session provided; exact compaction semantics and mtime condition success remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> After writing the file, commit with message: 'session-state: precompact snapshot'
> --- `.claude/hooks/precompact-snapshot.sh`

### Claims

#### RT-CLM-gateway-only
Label: Gateway-only canonical write doctrine

Claimed operation: Agents must use gateway operations rather than writing raw/wiki directly. This is foreground natural-language instruction plus checks/review, not established filesystem isolation. Model-only plan calls limit tool grants, while shell-capable hosts and separate writers remain outside that local protection. SRC-1: `CLAUDE.md`; see [RT-RTE-ingest-authorship](#rt-rte-ingest-authorship) and [RT-RTE-deposit-commit](#rt-rte-deposit-commit).

> 1. **No direct writes to `wiki/` or `raw/`.** All writes go through the gateway: `wiki <subcommand>` (CLI) or `wiki_*` (MCP). Direct file writes are caught by the validator and `git diff` review.
> --- `CLAUDE.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-authorship-prompt
Label: Authorship guidance into plan generation

Consumer: Claude plan model. Channel: task system prompt and selected source/existing-page user prompt. Force: natural-language requested conventions/integration behavior; parser/validator supplies separate symbolic admission force. Horizon: current generation and one error-fed repair, then resulting retained pages may reach later consumers. Delivery is wired; compliance is unobserved. SRC-1: `src/gateway/plan.py`, `src/gateway/ops/ingest.py`; [RT-RTE-ingest-authorship](#rt-rte-ingest-authorship).

> - Keep all existing claims and their citations intact.
> - Add new claims from this source with `[[sources/<id>]]` citations.
> - Update the Sources section to include the new source.
> - Update the Related section if new cross-references are warranted.
> --- `src/gateway/plan.py`

#### RT-BAP-domain-skill
Label: Generated domain guidance into host sessions

Consumer: Claude Code foreground agent when host discovers/loads generated skill. Channel: persisted `.claude/skills/wiki-<domain>/SKILL.md` with description/triggers and prose criteria. Force: interpretive instruction, not an executable access-control gate. Horizon: later sessions until regeneration; installed/discovered grant and activation remain unobserved. SRC-1: `src/gateway/ops/skill_emit.py`; [RT-RTE-skill-emission](#rt-rte-skill-emission).

> f"triggers: [wiki-{domain}]",
> --- `src/gateway/ops/skill_emit.py`

#### RT-BAP-session-state
Label: Snapshot guidance into resumed development

Consumer: foreground Claude Code agent. Channel: hooks stdout and requested later file reread. Force: host-delivered natural-language instruction to snapshot/reanchor and verify; no script-level enforcement that the file was written/read. Horizon: compaction and subsequent sessions when the state document persists. SRC-1: `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`; [RT-RTE-session-reanchor](#rt-rte-session-reanchor).

> If docs/session-state.md exists and its mtime is newer than this session's start, re-read it before any plan-or-write action. Verify each ## Open contract and ## File mid-edit against the working tree. Flag any disagreement to the user before proceeding.
> --- `.claude/hooks/session-start-reanchor.sh`

## Annotations

none
