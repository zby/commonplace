---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Pal runtime baseline: coordinated knowledge work, direct ingestion, scheduled maintenance, controls and Git synchronization."
run-id: AAS-2026-10-17-pal-e313a0902289-01
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
---

# Pal runtime report

## Runtime account

Pal ships a model-coordinated personal knowledge application. Its leader routes requests to specialists; specialists read and write files, SQL and knowledge stores or invoke external services. Code supplies the tools and persistence, while natural-language instructions supply much of the workflow and governance. This account inspects SRC-1 implementation and instruction strings at the frozen commit. It adds detailed coverage of `app/main.py`, `app/router.py`, all agent and tool modules, `pal/instructions.py`, `pal/config.py`, `db/session.py`, `context/load_context.py`, `evals/run.py`, `evals/__init__.py`, security/governance cases, the extended evaluator's cleanup and suite driver, `Dockerfile`, `compose.yaml`, `scripts/entrypoint.sh` and `pyproject.toml`. These supply implementation or doctrine/design, not observed runs. No target code was executed; successful operation, activation of retrieved material and benefit remain unobserved.

### Ordinary invocation and control ownership

For an ordinary knowledge question, a user enters through AgentOS's team API, optional Slack interface, or the shipped Python team driver. AgentOS binds the `pal` team and exposes the specialist agents separately. The Slack adapter requests user-identity resolution; the precise identity propagation and API session/authentication contracts reside in external Agno. The leader is `TeamMode.coordinate`, using the generation component [RT-CMP-openai-responses](#rt-cmp-openai-responses). Its next-step choice is a model decision under the routing table: knowledge questions go to Navigator; compilation, lint and configured research go to their specialists. Greetings can terminate at the leader. [SRC-1: `app/main.py`, `pal/team.py`]

The leader requests brief delegation and synthesis. Navigator receives its own instructions, tool list, knowledge handle and database, with history, memory and session-search settings; the team has different history limits. The API passes a delegated question into an external team runtime, not an inspected in-process deterministic workflow. The precise member-input filtering, history scoping, tool-result propagation and cancellation/retry behavior remain dependency-internal. The requested brief handoff resembles an isolated task frame, but source configuration does not establish its exact context boundary or prove that only a return value escapes. [SRC-1: `pal/team.py`, `pal/agents/navigator.py`]

Navigator is instructed to read the wiki index, select relevant article files, fall back through manifest/raw files and then live sources, and synthesize an answer. SQL captures and schema creation are additional paths under the same agent. The return goes through the leader's requested synthesis to the caller. Files persist in the configured context directory; sessions, vectors and user data use PostgreSQL. There is no inspected Pal-level transaction spanning the model workflow, files and database. See [RT-RTE-navigator-work](#rt-rte-navigator-work) and [RT-RTE-team-dispatch](#rt-rte-team-dispatch). [SRC-1: `pal/instructions.py`, `pal/tools/build.py`, `db/session.py`]

Working-context controls include configured team history of five runs, Navigator history of ten runs, past-session search limits of ten and five respectively, and requested selective file reads/per-source summaries. These limit or reshape supplied material rather than proving a host compaction algorithm. Removed older history may be reachable through session search, but exact selection and compaction are uninspected. Plain accumulated tool results are not a separate retention mechanism here. Agentic memory and learned-knowledge integration are wired through Agno; the memory specialist owns their revision analysis. [SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/instructions.py`]

### Four forcing cases and material alternate routes

1. **Direct ingestion versus the leader sync chain.** `/wiki/ingest` calls ordinary Python ingestion functions without leader or Researcher. It can accept text even when Researcher is not configured, and URL ingest can save a stub rather than extracted content. This defeats both an unconditional “every ingest is model-mediated” claim and an unconditional “every file change is pushed” claim. The route does not call Syncer. See [RT-RTE-raw-ingest](#rt-rte-raw-ingest). [SRC-1: `app/router.py`, `pal/tools/ingest.py`]
2. **Direct specialists versus role restrictions.** AgentOS exposes the specialist list, including Syncer even when the team's conditional member list excludes it. Compiler and Linter receive context-root FileTools, not role-specific read/write roots; “only writes wiki” and “do not modify concepts” are prompt restrictions rather than distinct filesystem grants. Deletion tools are disabled, but overwrite-capable tools remain. See [RT-CLM-control-scope](#rt-clm-control-scope). [SRC-1: `app/main.py`, `pal/team.py`, `pal/tools/build.py`]
3. **Scheduled work and independent synchronization.** Startup registers cron jobs that call the team API, a direct context-reload route, and conditional direct Git pull. Compile and lint custom routes also invoke the team, but HTTP `completed` describes return from the call, not checked article completeness. Git startup/pull can change context without a leader decision, and a local commit can survive a failed push. See [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance), [RT-RTE-context-refresh](#rt-rte-context-refresh) and [RT-RTE-git-sync](#rt-rte-git-sync). [SRC-1: `app/main.py`, `app/router.py`, `pal/tools/git.py`]
4. **Evaluation driver versus universal safety claims.** The extended evaluator deletes raw/wiki content before its pipeline suite. That host path is outside agent FileTools controls but inside the shipped application boundary. Unified evals call the actual team and judge responses/tool calls; they are not a runtime approval gate. See [RT-RTE-evaluation-driver](#rt-rte-evaluation-driver). [SRC-1: `evals/extended_smoke.py`, `evals/run.py`]

Inspected tool assembly grants no general-purpose shell tool or configurable arbitrary plugin loader. This is a bounded description of the lists, not an absence claim about Agno, MCP server internals or provider capabilities. The explicit subprocess route is Git with fixed operation argument lists plus a model-provided commit message. Exa MCP exposes a remote web-search surface, Parallel performs search/extraction, and Google/Slack adapters can produce external effects. Provider-native execution, external callbacks, remote-worker internals and durable scheduler implementation are not supplied for inspection. Their guarantees cannot be inferred from Pal's tool descriptions. [SRC-1: `pal/tools/build.py`, `pal/tools/git.py`, `pal/team.py`, `pal/config.py`]

### Guarantees, grants and deployment envelope

The capability surface is wider than a single deployed grant set. Researcher requires `PARALLEL_API_KEY`; Google tools require three configuration strings; leader SlackTools require a token, while the incoming Slack interface also requires a signing secret. Git team membership and startup/pull scheduling require token plus repository URL, but direct Syncer exposure is not gated in the same way. No live environment or service permissions were supplied, so the current grant set is uninspected. [SRC-1: `pal/config.py`, `pal/agents/researcher.py`, `app/main.py`, `pal/team.py`]

| Load-bearing guarantee | Owner and enforcement point | Strength and coverage | Alternate paths / external contract | Conclusion statuses |
|---|---|---|---|---|
| No file deletion / no email sending | Tool assembler disables FileTools deletion and Gmail send/reply tools | Protocol at the configured tool surface, not a whole-process invariant | File overwrites, SQL mutations, Git operations and evaluator cleanup are different effects. Depends on Agno honoring tool options and path confinement. | implementation conclusion status: wired; operation conclusion status: uninspected |
| User-scoped SQL | Navigator instruction requires `user_id` predicates; SQLTools receives a schema and engine, not a visible per-user query wrapper | Policy on Navigator SQL, not demonstrated database isolation | Direct SQL tool behavior, database roles/RLS and framework identity substitution are external/uninspected; shared context files are not shown user-partitioned | implementation conclusion status: claimed; operation conclusion status: uninspected |
| Confirm external effects | Navigator governance asks for confirmation for external attendees/messages | Policy on Navigator decisions | Leader sends Slack directly; schedules ask for posts; Google calendar updates are enabled. No inspected per-call approval middleware ties all paths together. | implementation conclusion status: claimed; operation conclusion status: uninspected |
| Every context change pushed | Leader sync-chain instruction and Syncer tools | Policy for leader workflows; Git execution best effort | Direct ingest, specialist API, reload, evaluator cleanup and startup/pull do not all traverse the chain. Requires credentials, network and remote acceptance. | implementation conclusion status: claimed; operation conclusion status: uninspected |
| Authorized HTTP access | AgentOS authorization configuration and custom-router authentication dependency | Deployment guarantee conditional on external Agno authentication | Default runtime is production, but shipped Compose explicitly selects development; direct Python/eval calls are not HTTP-gated. | implementation conclusion status: wired; operation conclusion status: uninspected |

The exact control evidence is retained in [RT-CLM-control-scope](#rt-clm-control-scope). These scoped claims should not be promoted to global invariants. Deployment uses one application with file/database/network access, not demonstrated per-agent OS isolation. Compose mounts source and context, publishes API and database ports, and sets development mode; the Docker image installs Git and a token-supplying credential helper. These establish machinery capable of effects, not production hardening or a deployed permission audit. [SRC-1: `Dockerfile`, `compose.yaml`, `app/main.py`]

### Admission and recovery boundaries

Model tool selection admits wiki/knowledge/file changes without a visible per-content human gate. Direct ingest admits caller-supplied content through fixed Python writes. Git pull admits remotely authorized repository changes. Source/configuration changes require ordinary external development/redeployment; `pyproject.toml` defines dependencies and packaging, while Compose enables source reload. No inspected route autonomously replaces Pal's Python program or model weights. This last statement is restricted to the traced routes, not opaque provider processing. [SRC-1: `pal/tools/build.py`, `pal/tools/ingest.py`, `pal/tools/wiki.py`, `pal/tools/knowledge.py`, `pal/tools/git.py`, `pyproject.toml`, `compose.yaml`]

Recovery is uneven: URL extraction errors become persistent stubs; Git returns explicit timeout/failure strings and preserves a local commit when push fails; manifest and index/state writes are independent writes. Repeated title slugs overwrite a raw file while appending manifest entries. There is no inspected atomic commit of an entire compile or automatic lint-to-repair transition. A model may report or recover using tools, but no supplied run demonstrates it. Tracing mechanisms for future knowledge reuse does not establish learning, a theory builder or successful self-improvement. [SRC-1: `pal/tools/ingest.py`, `pal/tools/wiki.py`, `pal/tools/git.py`, `pal/agents/linter.py`]

## Shared records

### Components

#### RT-CMP-openai-responses
Label: OpenAIResponses generation and judging

Source-native identity: `OpenAIResponses(id="gpt-5.4")` in leader, specialists and evaluator judge. Representational form: distributed-parametric model; remote provider substrate, with Python client configuration locally. Pal does not expose operational weight updates; provider-internal parameter changes are uninspected. Exact version is not pinned by a weight digest or dated snapshot; whether this named endpoint can resolve to changed backing weights is uninspected, so immutable identity cannot be assumed. No inspected Pal route changes parameters. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/compiler.py`, `pal/agents/linter.py`, `pal/agents/researcher.py`, `pal/agents/syncer.py`, `evals/__init__.py`.

> model=OpenAIResponses(id="gpt-5.4"),
> --- `pal/team.py`

#### RT-CMP-openai-embedder
Label: OpenAIEmbedder routing representation

Source-native identity: OpenAIEmbedder `text-embedding-3-small`. Representational form: distributed-parametric remote embedding model; derived dense vectors stored through PgVector alongside hybrid-search machinery in PostgreSQL. No inspected weight-update route is configured. Exact provider implementation/version is not pinned beyond the model ID; backing-endpoint mutability and provider parameter changes remain uninspected. New vectors are data updates, not evidence of model training. SRC-1: `db/session.py`.

> search_type=SearchType.hybrid,
> embedder=OpenAIEmbedder(id="text-embedding-3-small"),
> --- `db/session.py`

### Operative objects

#### RT-OBJ-agent-instructions
Label: Leader and specialist instructions

Source-native identity: `LEADER_INSTRUCTIONS`, Navigator instruction assembly, and specialist instruction strings. Representational form: natural language interpreted by generation models; stored as Python string constants, with configuration-dependent assembly and runtime user-ID substitution requested from Agno. These are shipped guidance, not dynamically retained experience. Role-specific prescriptions differ from shared tool grants. SRC-1: `pal/team.py`, `pal/instructions.py`, `pal/agents/compiler.py`, `pal/agents/linter.py`.

> **Delegate briefly.** Pass the user's question with enough context. Don't over-specify.
> --- `pal/team.py`

#### RT-OBJ-manifest
Label: Raw manifest compile flags

Source-native identity: `raw/.manifest.json`, JSON list stored in context files. Representational form: symbolic filenames, timestamps and booleans; titles/source strings supply descriptive content. Ingest appends entries and Compiler's tool marks the first matching filename compiled. The flag is not derived by checking article output. SRC-1: `pal/tools/ingest.py`.

> if entry["file"] == filename:
>     entry["compiled"] = True
>     _write_manifest(raw_dir, manifest)
>     return f"Marked as compiled: {filename}"
> --- `pal/tools/ingest.py`

### Routes

#### RT-RTE-team-dispatch
Label: Team dispatch and synthesis

Endpoints and progression: team caller → leader → selected specialist → leader synthesis → caller. The user, schedule or Python driver supplies the trigger; model policy chooses delegation under [RT-OBJ-agent-instructions](#rt-obj-agent-instructions). External Agno owns actual execution and identity propagation. State includes team/member database handles, configured history and memory/search interfaces. Operating mode: open requests, including fixed scheduled prompts; no answer oracle for dispatch. Proposer and decision-maker: leader model; caller supplies goal, not approval for every downstream action. SRC-1: `pal/team.py`, `app/main.py`.

> mode=TeamMode.coordinate,
> --- `pal/team.py`

- Immediate return: Team response, requested to synthesize specialist output; streaming enabled on Slack and the Python smoke driver.
- Later read-back: Team enables database-backed history, agentic memory and past-session search; precise serialization and later selection are dependency-internal.
- Delegated visibility: Brief question plus enough context is requested; exact forwarded state and member-return filtering are uninspected Agno behavior.
- Selection predicate: Leader's model decision under request-type routing, with Navigator the default and greetings allowed directly.
- Invalidation or expiry: Five history runs and ten past sessions to search are configured for the leader; retention/expiry beyond these selection bounds is uninspected.
- Activation or effect: Delegation, synthesis and optional leader Slack posting are afforded/wired; actual model decisions unobserved.
- Evidence limits: Instruction compliance, exact context isolation and completed effects lack run evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-navigator-work
Label: Navigator retrieval and action

Endpoints: leader or direct agent caller → Navigator → wiki/files/knowledge/SQL or configured services → agent answer. Model chooses tools; Python assemblies bind concrete handles. Guidance requests classify/recall/read/act/learn and wiki-first knowledge lookup. Operating mode: open requests. SQL/file/knowledge writes are model-proposed and tool-admitted without a general content-approval gate; external-effect confirmation is requested from the user but not visibly enforced by a wrapper. No answer oracle; retrieved sources are evidence, not a reference outcome. Callers can reject a proposed external effect through requested confirmation; no shown gate covers every tool action. Recovery uses source fallbacks and model interpretation of tool results. Persisted files or SQL can be overwritten/updated by later tool actions; no shared rollback transaction is shown. SRC-1: `pal/instructions.py`, `pal/agents/navigator.py`, `pal/tools/build.py`, `pal/tools/knowledge.py`.

> 1. Read the wiki index (`read_wiki_index`) first — scan for relevant articles
> 2. Pull specific concept articles or summaries via `read_file` as needed
> --- `pal/instructions.py`

- Immediate return: Navigator answer/tool result to the direct caller or leader.
- Later read-back: Saved files, SQL and knowledge entries can reach later tool reads; configured memory/session search is additional dependency-mediated reuse.
- Delegated visibility: Leader receives specialist output; exact inclusion of underlying tool results is uninspected.
- Selection predicate: Model interprets intent, index, metadata and query results; lookup tools then execute requested identifiers/queries.
- Invalidation or expiry: Prompt asks to verify missing learning references and favor corrections/recency; no uniform file/SQL expiry is implemented in inspected Pal code.
- Activation or effect: Can execute SQL, save files/metadata, search externally and mutate configured calendars; successful behavior change through retrieved material is unobserved.
- Evidence limits: SQLTools/FileTools/provider implementations and real user identity isolation are external; requested confirmation is not demonstrated enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-raw-ingest
Label: Raw content admission

Endpoints: Researcher tool call or direct `/wiki/ingest` → `_do_ingest_text`/`_do_ingest_url` → raw file plus manifest. Caller supplies title/content or URL; extraction may propose fetched content. Python writes admit it without semantic review; initiating a request is not proof of human approval of the extracted text. Model guidance shapes Researcher source choice and tags; the direct route does not use that prompt. Operating mode: open ingestion, no answer oracle. Rejection: missing URL/text returns HTTP 400, extraction failure becomes a stub rather than rejection. Recovery: later manual fetch/text ingestion is suggested; overwrites and manifest appends are not one transaction. SRC-1: `app/router.py`, `pal/tools/ingest.py`, `pal/agents/researcher.py`.

> stub = extracted or f"Source: {url}\n\n*(Content pending — configure PARALLEL_API_KEY or use ingest_text.)*"
> file_path.write_text(frontmatter + stub + "\n")
> --- `pal/tools/ingest.py`

- Immediate return: File/content status string; HTTP wraps it as `ingested`, including possible stubs.
- Later read-back: Compiler reads raw content and manifest; Navigator can read uncompiled raw files.
- Delegated visibility: Researcher result may reach leader; direct route bypasses all agents and sync chain.
- Selection predicate: Caller or model selects title/URL/text; code slugifies title to a filename, truncating to 80 characters.
- Invalidation or expiry: Same slug overwrites file and appends another manifest entry; no expiry or duplicate-content rejection is shown in these functions.
- Activation or effect: Writes frontmatter/content then manifest, with compiled false; article completion or useful extraction is not guaranteed.
- Evidence limits: Remote extraction and model source-selection quality are unobserved; direct route text has precedence when both text and URL are supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-wiki-maintenance
Label: Compilation and lint maintenance

Endpoints: scheduled team request, custom route or direct specialist API → Compiler/Linter → files and wiki metadata → response/report. Compiler model proposes summaries/concepts/index under source-tracking and additive guidance; tools admit writes and compile flags without verifying citations or checking outputs. Linter model diagnoses contradictions/staleness/thinness and writes a report/state, not an automatic repair. Human per-content veto is not shown; neither model judgment nor source citation is an answer oracle. Operating mode: open maintenance requests and fixed periodic prompts. Invalid/missing information can be flagged by the model, but no mandatory lint-before-admission or report-to-Compiler repair chain is wired. Recovery/rollback is local overwrite or separately available Git history, not transactional automatic undo. SRC-1: `app/router.py`, `app/main.py`, `pal/agents/compiler.py`, `pal/agents/linter.py`, `pal/tools/wiki.py`, `pal/tools/ingest.py`.

> - **Additive**: New information enriches existing articles. Note contradictions, don't silently overwrite.
> - **Source-tracked**: Every claim links back to the raw source that supports it.
> --- `pal/agents/compiler.py`

> Include these as suggestions in the report, not direct edits.
> --- `pal/agents/linter.py`

- Immediate return: Agent/team response, lint report path by instruction, or custom-route `completed` response.
- Later read-back: Wiki articles/index are available to Navigator and later maintenance; manifest flags select subsequent compiles.
- Delegated visibility: Team leader may synthesize maintenance output and is asked to call Syncer; direct specialist calls bypass leader.
- Selection predicate: Compiler instructed to choose compiled-false entries; force HTTP request instead asks team to recompile all, conflicting with normal incremental-only guidance and leaving resolution to the model. Linter reads index/articles and applies requested checks.
- Invalidation or expiry: State counts/timestamps are explicitly writable; lint stale threshold is a prompt criterion, not automatic article invalidation.
- Activation or effect: Tool wiring allows article/index/state/manifest updates and report persistence; correct completed compilation and subsequent repair remain unobserved.
- Evidence limits: Neither flags nor HTTP completion attest source fidelity; no supplied compiled corpus or run demonstrates the intended chain.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-context-refresh
Label: Context routing metadata refresh

Endpoints: CLI, daily schedule or `/context/reload` → loader → `pal_knowledge` insertion. Software discovers files and proposes fixed path/size/tag/timestamp metadata; insert/upsert admits it. Recreate can delete the entire knowledge vector index, including non-file entries. Caller chooses recreate, not individual metadata records; no per-record human gate. Operating mode: deterministic refresh, dry-run preview available, no answer oracle. Recovery guidance says non-file entries will rebuild organically, not restore from a snapshot. SRC-1: `context/load_context.py`, `app/main.py`, `app/router.py`.

> name=f"File: {rel_path}",
> text_content=text_content,
> upsert=True,
> --- `context/load_context.py`

- Immediate return: Loaded count or dry-run preview, not document contents.
- Later read-back: Knowledge search can return compact routing entries; agents must subsequently read files for content.
- Delegated visibility: Loader does not delegate; later specialist queries can independently retrieve its entries.
- Selection predicate: Recursive files with md/txt/yaml/yml/json suffixes, sorted; tags parsed from frontmatter or general-context fallback.
- Invalidation or expiry: Upsert by entry name is requested; recreate wipes all vector entries. Removed files are not explicitly pruned during ordinary refresh.
- Activation or effect: Calls knowledge insertion/embedding machinery; no observed routing benefit.
- Evidence limits: Agno upsert/search behavior is external; metadata is not full content and cannot establish complete answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-git-sync
Label: Context Git synchronization

Endpoints: leader/direct Syncer → fixed Git tools; startup initializer and HTTP/scheduled pull independently → context repository/remote. Model proposes commit messages and timing on the Syncer route; code stages all changes, commits and pushes. Remote repository writers propose incoming changes, admitted by Git fetch/checkout/pull under configured credentials. No per-file local human approval or semantic review is shown. Operating mode: open requests and periodic pull; no answer oracle. Guidance asks final sync after file changes. Rejection is command/network failure, not content evaluation. Git history offers possible manual recovery; code returns errors, does not automatically revert a failed multi-command sequence. SRC-1: `pal/tools/git.py`, `pal/team.py`, `pal/agents/syncer.py`, `app/main.py`, `app/router.py`.

> return f"Committed locally but push failed: {out}"
> --- `pal/tools/git.py`

- Immediate return: Git success/failure/status strings; startup prints initialization result.
- Later read-back: Pulled files become available to file consumers; pushed commits can be fetched by later instances; actual remote reuse unobserved.
- Delegated visibility: Leader can receive Syncer output, but startup and direct pull are independent of delegation.
- Selection predicate: Push stages all pending context changes; pull uses current configured remote branch with rebase/autostash; initialization prefers origin/main if available.
- Invalidation or expiry: Git changes replace working-tree content; no Pal-level TTL or selective semantic conflict resolver.
- Activation or effect: Subprocess Git with 60-second timeout can commit/push/pull; actual credentials and remote permission envelope are unknown.
- Evidence limits: Intermediate init/stage command results are not all enforced before later commands; no demonstrated cross-instance convergence or reliable push-after-every-write.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-evaluation-driver
Label: Evaluation calls and state cleanup

Endpoints: evaluator CLI → actual team → response/tool-call evaluators → console results. Extended suite additionally clears raw/wiki before pipeline tests and propagates session IDs across dependencies. Software chooses cases; models generate answers and judge criteria/accuracy, while ReliabilityEval checks configured expected tool calls. Answer oracles: source-authored expected outputs, expected tool names, and criteria, consumed by Agno evaluators; judging uses gpt-5.4. Operating mode: bounded test suite, not a production approval mechanism. No inspected automatic successor selection, code revision, or deployment gate consumes these results. Cleanup itself admits deletion without model or per-file human approval; recovery is not supplied by the cleanup function. SRC-1: `evals/run.py`, `evals/__init__.py`, `evals/cases/security.py`, `evals/cases/governance.py`, `evals/extended_smoke.py`.

> # --- Knowledge pipeline tests (clean state first) ---
> print("\n\n>>> Cleaning raw/ and wiki/ for knowledge pipeline tests...")
> _clean_raw_and_wiki()
> --- `evals/extended_smoke.py`

- Immediate return: Printed pass/fail/error counts, durations and optional reasons/previews; extended suites return result lists.
- Later read-back: Dependent extended tests can reuse returned session IDs; effects on the real files/team persistence can survive a case. No automatic result-to-runtime-policy read-back was found in the inspected runner.
- Delegated visibility: Actual team delegation applies; evaluator consumes response content or structured team response, not proof of every external side effect.
- Selection predicate: Category registry/CLI and suite order; dependent tests skip if prerequisites fail.
- Invalidation or expiry: Extended cleanup removes files/directories except placeholders, recreating wiki subdirectories; sessions are not thereby proven cleared.
- Activation or effect: Drivers can exercise real tools and destructive fixture preparation; none were run in this analysis.
- Evidence limits: Test definitions are not passing results. Response-level governance judging does not independently verify database isolation or external non-effects.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### RT-CLM-control-scope
Label: Governance scope and alternate paths

Claimed operation: instructions describe user-scoped SQL as a hard security boundary, prohibit sending/deletion, and require confirmation/sync. Actual inspection supports distinct policy and tool-surface mechanisms, not a single global guarantee. SRC-1: `pal/instructions.py`, `pal/tools/build.py`, `pal/team.py`, `app/main.py`, `evals/extended_smoke.py`.

> **Data isolation**: Every query must be scoped to `user_id = '{{user_id}}'` — every INSERT, SELECT, UPDATE, DELETE. No exceptions. New tables must always include `user_id`. This is a hard security boundary.
> --- `pal/instructions.py`

> SQLTools(db_engine=get_sql_engine(), schema=PAL_SCHEMA),
> FileTools(base_dir=PAL_CONTEXT_DIR, enable_delete_file=False),
> --- `pal/tools/build.py`

> tools.append(GmailTools(send_email=False, send_email_reply=False, list_labels=True))
> tools.append(GoogleCalendarTools(allow_update=True))
> --- `pal/tools/build.py`

> After any workflow that creates or modifies files in context/, **always delegate
> to Syncer as the final step** to commit and push changes to GitHub. This ensures
> the knowledge base is durable and available everywhere.
> --- `pal/team.py`

> agents: list = [a for a in [navigator, researcher, compiler, linter, syncer] if a is not None]
> --- `app/main.py`

The counterexamples are the direct ingest route, independent specialist exposure, broad context-root file grants and evaluator deletion. SQL scoping has no visible Pal query-rewriting enforcement in the inspected assembly. This does not establish that the external runtime or deployed database lacks further controls; it prevents attributing such controls to inspected Pal code. SMTP/API send exclusions likewise constrain the configured Gmail adapter, not every possible external effect.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-guidance
Label: Shipped agent guidance authority

Consumer: leader and specialist generation calls. Channel: configured instruction strings and model-visible tool descriptions. Force: model-interpreted directive, not guaranteed compliance; role grants are separately bound by tool assembly. Horizon: each configured invocation until code/configuration reload changes guidance. SRC-1: `pal/team.py`, `pal/instructions.py`, `pal/agents/compiler.py`, `pal/tools/build.py`. Evidence: [RT-OBJ-agent-instructions](#rt-obj-agent-instructions) and [RT-CLM-control-scope](#rt-clm-control-scope). Static shipped guidance is not evidence of trace-fed revision.

## Annotations

none
