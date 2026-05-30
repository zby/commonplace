---
description: "Agno personal knowledge agent with file/wiki compilation, PgVector routing metadata, Agno learnings, SQL facts, scheduled maintenance, and tool routing"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Pal

Pal is Agno's personal knowledge agent for turning personal context, raw sources, structured notes, email, calendar, Slack, and web research into a navigable working memory. At the reviewed commit it is a concrete AgentOS app: a coordinating Pal team leader delegates to Navigator, Researcher, Compiler, Linter, and optional Syncer agents; Agno supplies the agent/team runtime, session storage, learning machinery, scheduler, Slack interface, knowledge abstractions, and eval framework.

**Repository:** https://github.com/agno-agi/pal

**Reviewed commit:** [6516b8ede0c085e48f39f3bd04cb85b475a855dc](https://github.com/agno-agi/pal/commit/6516b8ede0c085e48f39f3bd04cb85b475a855dc)

## Core Ideas

**Memory is split across routing metadata, learned operations, files, wiki, SQL, and Agno sessions.** The README names five context systems: `pal_knowledge`, `pal_learnings`, `context/wiki/`, `context/`, and `pal_*` SQL tables ([`README.md`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/README.md)). The implementation backs `pal_knowledge` and `pal_learnings` with Agno `Knowledge` objects over PgVector hybrid search plus content tables, while Agno session/chat state uses `PostgresDb` ([`pal/agents/settings.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/settings.py), [`db/session.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/db/session.py)). That makes the storage substrate mixed: Postgres tables for framework memory and user facts, PgVector for routing/search metadata, and Git-syncable files for durable context and compiled wiki artifacts.

**`pal_knowledge` is a metadata router, not the source of truth.** `context/load_context.py` scans markdown, text, YAML, and JSON files under `context/`, extracts frontmatter tags, and writes compact `File:` entries into `pal_knowledge`; it explicitly avoids embedding file contents and uses FileTools to read them on demand ([`context/load_context.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/context/load_context.py)). The Navigator instructions preserve that boundary: `pal_knowledge` stores `File:`, `Schema:`, `Source:`, and `Discovery:` entries, while raw content stays in native stores ([`pal/instructions.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/instructions.py)). As a knowledge artifact, it advises routing. When an agent follows a `Discovery:` entry to skip broad search, the same entry has ranking and routing influence but still does not contain canonical evidence.

**Raw-to-wiki compilation is a file-level distillation pipeline.** Researcher can save URL or text inputs into `context/raw/` as markdown with YAML frontmatter and a manifest entry; Parallel extraction is optional, and a missing key produces stubs rather than blocking ingest ([`pal/tools/ingest.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/tools/ingest.py), [`pal/agents/researcher.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/researcher.py)). Compiler reads uncompiled manifest entries, writes summaries under `wiki/summaries/`, updates concept articles under `wiki/concepts/`, maintains source links and related links, marks raw files compiled, and updates `wiki/index.md` plus `.state.json` ([`pal/agents/compiler.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/compiler.py), [`pal/tools/wiki.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/tools/wiki.py)). Raw files are source/evidence knowledge artifacts. Wiki summaries, concept pages, and the index are compiled knowledge artifacts; the index also gains system-definition-like routing force because Navigator is instructed to read it first for knowledge questions.

**Structured personal data lives in SQL, isolated from Agno framework tables.** Pal bootstraps a separate PostgreSQL schema named `pal` and sets the search path so SQLTools operate on user tables there, while Agno knowledge/session tables remain in the default schema ([`db/session.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/db/session.py)). Navigator instructions tell the agent to create `pal_` tables on demand, include `user_id` on every table, scope every query by `user_id`, and use tags as cross-table connectors for notes, people, projects, and decisions ([`pal/instructions.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/instructions.py)). The table schemas are symbolic system-definition artifacts when they constrain storage and retrieval; rows are structured knowledge artifacts unless a downstream workflow uses them to trigger action.

**Tool routing is mostly instruction-shaped, not a separate planner service.** The Pal leader is an Agno `Team` in coordinate mode with instructions that require delegation for almost everything beyond greetings; Navigator handles SQL, files, Exa, Gmail, Calendar, wiki reads, and manifest reads; Researcher, Compiler, Linter, and Syncer each receive narrower tool surfaces ([`pal/team.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/team.py), [`pal/tools/build.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/tools/build.py)). These instructions and tool assignments are system-definition artifacts: they route, deny direct answering, limit email sending, disable file deletion, and decide which agent can touch which substrate.

**Scheduled maintenance is first-class AgentOS configuration.** Startup registers idempotent schedules for context refresh, daily briefing, wiki compile, inbox digest, learning summary, weekly review, wiki lint, and optional sync pull ([`app/main.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/app/main.py)). Most schedules call `/teams/pal/runs`, so they exercise the same team routing path as user requests; context reload and sync pull bypass the team through direct endpoints ([`app/router.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/app/router.py)). This gives maintenance artifacts behavioral authority through time: the scheduler repeatedly activates compilation, linting, reload, summaries, and sync independent of a user prompt.

**Learning and search history are largely inherited from Agno.** Pal configures the team leader and Navigator with `LearningMachine(... LearningMode.AGENTIC)`, `add_learnings_to_context`, `enable_agentic_memory`, past-session search, chat history, and limited history windows ([`pal/team.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/team.py), [`pal/agents/navigator.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/navigator.py)). Pal adds instruction policy around learning names such as `Retrieval:`, `Pattern:`, and `Correction:`, but the extraction, search-history mechanics, and agentic memory behavior come from Agno rather than local code ([`pal/instructions.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/instructions.py)). Researcher also receives Agno learning when enabled, while Compiler, Linter, and Syncer are effectively stateless workers with datetime/context and shared knowledge but no configured learning loop ([`pal/agents/researcher.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/researcher.py), [`pal/agents/compiler.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/compiler.py), [`pal/agents/linter.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/linter.py)).

**Evaluation covers routing, governance, security, knowledge behavior, and smoke flows.** The repo includes Agno eval runners for agent-as-judge, reliability, and accuracy cases, plus local smoke tests with regex assertions ([`evals/run.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/run.py), [`evals/smoke.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/smoke.py)). Cases check tool routing, knowledge-system explanations, scheduled-task awareness, no direct email sending, no file deletion, no destructive SQL/git behavior, `user_id` scoping, and secret non-disclosure ([`evals/cases/routing.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/cases/routing.py), [`evals/cases/knowledge.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/cases/knowledge.py), [`evals/cases/governance.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/cases/governance.py), [`evals/cases/security.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/cases/security.py)). These eval definitions are system-definition artifacts only if operators run them as gates; otherwise they are audit knowledge artifacts.

## Comparison with Our System

| Dimension | Pal | Commonplace |
|---|---|---|
| Primary aim | Personal agent over heterogeneous personal sources | Agent-operated KB methodology and artifact governance |
| Main substrate | Agno AgentOS, Postgres/PgVector, SQLTools, FileTools, context files, Git sync | Git-tracked typed markdown collections, generated indexes, validation and review commands |
| Raw sources | `context/raw/*.md` plus `.manifest.json` | `kb/sources/`, work artifacts, source snapshots |
| Compiled artifacts | `context/wiki/summaries/`, `context/wiki/concepts/`, `wiki/index.md` | Notes, reviews, ADRs, instructions, indexes |
| Operational memory | Agno `LearningMachine` into `pal_learnings` plus past session search | Skills, AGENTS instructions, review results, command outputs, notes |
| Structured data | Agent-created `pal_*` SQL tables scoped by `user_id` | Frontmatter, schemas, indexes, and scripts rather than ad hoc SQL tables |
| Activation | Team instructions, tool surfaces, scheduler, Agno memory/context injection | Navigation conventions, skills, type specs, validation, semantic review, generated indexes |
| Evaluation | Agno evals plus smoke scripts | Deterministic validation plus semantic review bundles |

Pal is more application-shaped than commonplace. It starts from live user workflows: chat, Slack, email, calendar, web research, SQL capture, daily briefs, and scheduled wiki maintenance. Commonplace starts from a durable knowledge library and procedure system. Pal's strength is operational reach across native interfaces; commonplace's strength is tighter artifact contracts, explicit collection registers, and review/validation lifecycle.

The closest overlap is the raw-to-compiled split. Pal's `raw/` to `wiki/` pipeline resembles a small, personal version of source snapshot to authored note, with the same need to preserve source lineage and avoid flattening everything into one vector store. Pal makes the index-first retrieval idea concrete: a compact wiki index is the intended first read, and source files stay available on demand.

The largest difference is behavioral authority. Pal gives many instructions directly to runtime agents and schedulers. If the leader says "everything else must be delegated," that is an active routing rule. If Navigator says "read wiki index first," that is an activation policy. Commonplace usually records comparable rules in type specs, skills, AGENTS instructions, and validation commands; Pal packages them inside an always-on personal assistant runtime.

## Borrowable Ideas

**Keep routing metadata separate from canonical content.** Ready to borrow. Pal's `pal_knowledge` boundary is crisp: metadata points to files, schemas, source capabilities, and discoveries; content remains in native stores. Commonplace already does this with indexes and search, but Pal's `Discovery:` entries suggest a lightweight way to cache cross-source routing discoveries without pretending they are source evidence.

**Use an index-first compiled wiki for personal source corpora.** Ready to borrow for workshop or project contexts. A small `wiki/index.md` that lists summaries and concept pages gives an agent a predictable first read before opening full files. Commonplace's generated directory indexes are broader and less semantic; a project-scoped concept index could be useful when source volume grows.

**Make scheduled maintenance exercise the same user-facing route.** Worth borrowing cautiously. Pal sends most maintenance through `/teams/pal/runs`, which tests the same routing and tool surfaces used interactively. Commonplace could run scheduled sweeps through existing commands and skills, but should keep deterministic commands for validation and index generation where model variance is unnecessary.

**Treat SQL as a separate substrate for volatile structured facts.** Needs a concrete use case. Pal's `pal_*` tables are useful for notes, people, projects, decisions, and tag joins. Commonplace should not move core methodology notes into SQL, but a workshop layer might benefit from structured task/contact/decision state that later promotes into markdown artifacts.

**Borrow the agent-tier memory rule.** Ready as a design heuristic. Pal gives full memory to leader and Navigator, while specialist workers mostly stay stateless. Commonplace skills can mirror this: long-lived routing and review memory belongs near coordinator surfaces, while one-shot drafting or linting workers should receive focused context.

**Do not borrow opaque agentic learning without review if authority increases.** Pal's Agno learning is useful for operational preferences and retrieval strategies, but it is weaker as durable methodology because the local code does not expose extraction criteria, confidence, decay, or review gates. Commonplace should promote such items only after they become inspectable notes, instructions, tests, or skills.

## Trace-derived learning placement

Pal qualifies as trace-derived learning, but the qualifying mechanism is mostly Agno-provided rather than locally implemented. The local code configures Agno `LearningMachine`, agentic memory, session search, chat history, and learning-context injection; the local instructions define preferred learning categories and correction precedence.

**Trace source.** Source traces include user/team conversations stored by Agno, chat history windows, past session search results, and user corrections observed during interaction. Pal also has operational traces from scheduled prompts and eval runs, but the durable learning path in the inspected code is the Agno learning/session machinery configured on the leader, Navigator, and optionally Researcher.

**Extraction.** Extraction is delegated to Agno's `LearningMachine` in `LearningMode.AGENTIC`. Pal's own contribution is policy: save `Retrieval:`, `Pattern:`, and `Correction:` learnings; search before saving; update rather than duplicate; prefer recent learnings; let corrections win ([`pal/instructions.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/instructions.py)). The repo does not include a local extractor, judge, scoring policy, decay rule, or promotion workflow for learned items.

**Storage substrate.** Raw conversations and session history live in Agno/Postgres session storage, including `pal_contents` according to the project docs ([`CLAUDE.md`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/CLAUDE.md)). Distilled operational learnings live in `pal_learnings` and `pal_learnings_contents`, backed by PgVector hybrid search and Postgres content storage ([`db/session.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/db/session.py), [`pal/agents/settings.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/agents/settings.py)). Raw ingested documents and compiled wiki files are separate file substrates; they are source-derived distillation, not the trace-derived learning path.

**Representational form.** Raw traces are mixed conversation/session records. Distilled learnings are prose entries with symbolic prefixes such as `Retrieval:`, `Pattern:`, and `Correction:`. Past-session search likely uses embeddings through Agno's storage/search stack, but no local code trains weights or rankers. SQL schemas and team instructions are symbolic system-definition artifacts, not outputs of the learning loop at this commit.

**Lineage.** Lineage is weak for `pal_learnings`. A learning may include dates if the agent follows instructions, but the code does not require source session IDs, source message links, confidence, trigger reason, evaluator identity, or invalidation metadata. Raw-to-wiki artifacts have stronger local lineage through manifest entries, frontmatter, and source lists than Agno learnings do.

**Behavioral authority.** Raw sessions are knowledge artifacts when searched as evidence. Distilled `pal_learnings` become system-definition artifacts when Agno injects them into leader or Navigator context via `add_learnings_to_context`, because they can change retrieval order, preference handling, and future response behavior. Explicit `Correction:` entries have the strongest authority by instruction: they always win over conflicting learnings.

**Scope and timing.** Scope is per Pal deployment and likely per user/session identity. Timing is online during normal interaction, with weekly learning-summary schedules querying the learned state rather than implementing a separate training pass ([`app/main.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/app/main.py)).

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Pal should be placed as an application that consumes framework-provided agentic memory rather than as a novel local trace-learning algorithm. It strengthens the survey distinction between configured learning authority and inspectable learning mechanism: Pal gives learned items real runtime influence, but the extraction oracle is mostly outside the reviewed repo.

## Curiosity Pass

**The README's "every interaction improves the next one" claim is directionally true but implementation-dependent.** The local code enables Agno learning and context injection, but the repo does not show the extractor, filtering policy, decay policy, or review workflow. A review should credit the configured Agno behavior without overstating Pal-specific learning machinery.

**The strongest local memory design is actually the source split, not the learning loop.** `pal_knowledge` as metadata, `raw/` as evidence, `wiki/` as compiled prose, SQL as structured facts, and files as user-authored context are all visible and inspectable. `pal_learnings` is behaviorally important but less auditable from local code.

**The wiki index has more authority than an ordinary index.** Navigator is instructed to read it first and Compiler is instructed to keep all paths usable by `read_file`. That makes `wiki/index.md` both a knowledge artifact and an activation/routing surface.

**Git sync is practical but broad.** Syncer can commit and push all `context/` changes, and `init_context_repo` uses `git add -A` inside the context repo ([`pal/tools/git.py`](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/tools/git.py)). That is acceptable for Pal's dedicated context directory, but it would be too coarse for a shared methodology repo without stronger ownership boundaries.

**Evaluation is present but not obviously wired as a release gate.** The eval suite is a valuable behavior specification. The reviewed code does not show an automated requirement that evals pass before scheduled tasks, deployment, or sync.

## What to Watch

- Whether Agno exposes more inspectable lineage for `LearningMachine` outputs, including source session IDs, confidence, and invalidation rules.
- Whether `pal_learnings` gains review, merge, retirement, or promotion into durable files when an item becomes high-authority.
- Whether wiki compilation becomes less prompt-only by adding deterministic checks for source links, stale articles, duplicates, and broken references.
- Whether the SQL schema conventions become executable migrations or validators rather than only Navigator instructions.
- Whether scheduled maintenance results become typed artifacts with provenance, not just prompts and Slack posts.

---

Relevant Notes:

- [behavioral authority](../../notes/definitions/behavioral-authority.md) - classifies: Pal's metadata, learnings, wiki index, instructions, scheduler, and evals have different force depending on consumer and channel
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw files, wiki articles, SQL rows, session traces, and reports when consumed as evidence or context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: team instructions, tool assignments, scheduler entries, SQL schemas, correction precedence, and evaluation gates when they route or constrain behavior
- [lineage](../../notes/definitions/lineage.md) - frames: Pal's manifest/frontmatter lineage is stronger than its Agno learning lineage at this commit
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: Pal's learned items and wiki index matter because they are injected or read before future action
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - positions: Pal is a framework-enabled agentic-memory application, not a locally novel trace extractor
