---
description: Filesystem-first startup-OS KB with persona folders, cron heartbeats, browser PTY, and embedded HTML apps; strongest reviewed example of merging library, workshop, and agent runtime into one product
type: note
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: 2026-04-03
---

# Cabinet

Cabinet is a self-hosted Next.js/TypeScript knowledge base and "AI team" product built by Hila Shmuel. It keeps page content as markdown files on disk, layers browser editing and a reconnectable terminal on top, and treats agent personas, workspaces, jobs, and internal chat as first-class residents of the same tree. The repo I inspected was `hilash/cabinet` on `main`, latest commit `87b8e25` dated 2026-04-03.

**Repository:** https://github.com/hilash/cabinet

## Core Ideas

**Filesystem-first content, hybrid operational substrate.** Cabinet's durable knowledge surface really is a directory tree under `data/`: pages are directories with `index.md` plus assets, or standalone `.md` files, with special handling for `index.html`, PDFs, and CSVs. But the "no database" story is only true for page content. Operational state also lives in `data/.cabinet.db` (SQLite tables for sessions, messages, activity, job runs, and mission tasks) plus a growing set of JSON and JSONL sidecars under `.agents/` and `.chat/`.

**The "AI team" is a persona-and-daemon layer around Claude Code.** Personas are markdown files in `data/.agents/{slug}/persona.md`, seeded from a hidden `.library/` of prebuilt roles like CEO, CTO, QA, and Content Marketer. A daemon process schedules cron heartbeats, spawns reconnectable PTY sessions, exposes output over HTTP/WebSocket, and currently routes everything through a single provider: `claude --dangerously-skip-permissions`.

**Heartbeats turn freeform runs into structured side effects.** Cabinet does not rely on autonomous background agents silently mutating state. It prompts each persona with its body, memory files, inbox, focus areas, goals, and task inbox, then requires a fenced ````memory```` epilogue with fields like `CONTEXT_UPDATE`, `LEARNING`, `MESSAGE_TO`, `SLACK`, `GOAL_UPDATE`, and `TASK_CREATE`. Post-processing regexes parse that block and write markdown memories, JSON tasks, JSONL Slack messages, goal counters, and session transcripts.

**Git is the recovery interface, not just backup.** Page CRUD calls trigger a debounced auto-commit flow, and the UI exposes per-page log, diff, and restore operations. This makes edits inspectable and reversible in a way most "AI workspace" tools do not. The trade-off is coarse history isolation: Cabinet stages `.` before committing, so the commit unit is "whatever changed in the data dir recently," not an intentional knowledge mutation.

**Cabinet collapses library, workshop, and executable artifacts into one tree.** Agent workspaces, task inboxes, session logs, embedded `index.html` apps, linked repos via `.repo.yaml`, and ordinary markdown pages all sit under the same browsable structure. This is the product's strongest differentiator: it is not just a note system with an agent bolt-on, but an integrated operating surface where documents, agent outputs, and executable artifacts share the same filesystem metaphor.

## Comparison with Our System

Cabinet is much closer to the "productized workshop layer" than Commonplace. Commonplace has the sharper theory of knowledge shape and maturity; Cabinet has the stronger integrated surface for actually running agents against a shared file tree every day.

| Dimension | Cabinet | Commonplace |
|---|---|---|
| Primary aim | Self-hosted startup operating system where humans and agents work in one markdown tree | Knowledge system for agent-operated curation, reasoning, and methodology distillation |
| Durable knowledge shape | Markdown pages with simple frontmatter, wiki-links, direct title/body/tag search, WYSIWYG editing | Markdown notes with typed templates, retrieval-oriented descriptions, semantic link phrases, curated indexes |
| Workshop layer | Concrete and productized: personas, workspaces, task inboxes, Slack-like channels, cron heartbeats, browser PTY | Partly explicit, partly still theoretical: tasks, workshops, skills, and work dirs exist, but not as one integrated operating UI |
| Context engineering | Prompt assembly from persona body + memory files + focus snippets + inbox + goals + tasks | Routing through AGENTS instructions, skill triggers, indexes, descriptions, and deliberate progressive disclosure |
| Learning/update model | Append-oriented memory capture and task/message extraction from heartbeat output | Curated note-writing, linking, review, validation, and maturation into reusable artifacts |
| Validation/governance | Path-safety checks, cron validation, failure auto-pause, budgets, and some notification rules; little content validation | Deterministic structural validation plus semantic review bundles for content quality |
| History/recovery | Auto-committed git repo inside the content tree with restore UI | Normal repo history with intentional commits and stronger review discipline, but less turnkey UI support |
| Integration surface | Embedded HTML apps, linked repos, browser terminal, WYSIWYG editor, agent dashboard | Repo-native text artifacts, scripts, and harness instructions; fewer integrated runtime surfaces |

Cabinet is stronger where the problem is "make the KB feel like a place a team can work." The product joins pages, workspaces, terminals, schedules, and agent personas into one inspectable surface. Commonplace is stronger where the problem is "make accumulated knowledge stay meaningful over time." We invest more in note types, link semantics, retrieval filters, and review discipline; Cabinet invests more in operational smoothness.

The deepest difference is that Cabinet merges library and workshop by product design, while Commonplace still treats that bridge as an architectural problem to be solved carefully. Cabinet shows the upside of collapsing them: agents can leave visible work products in place immediately. It also shows the cost: once everything is one workspace, the system needs stronger promotion, deduplication, and validation layers to keep the growing artifact pile from becoming merely well-organized residue.

## Borrowable Ideas

**Localized repo bindings with `.repo.yaml`.** Attaching repo metadata to a subtree is a clean way to keep code context near the notes that depend on it. In Commonplace this could support code-adjacent workshops or related-system investigations without a central registry. Ready to borrow when we have recurring note-local code context, not before.

**First-class visible workspaces for long-running agents.** Cabinet's `workspace/`, `sessions/`, `tasks/`, and `memory/` directories make agent work legible without opening a database browser or external dashboard. This is the strongest concrete reference for the [workshop layer](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md). Needs a concrete use case first, but the pattern is real.

**Failure budgets and auto-pause for autonomous agents.** Budget counters plus "pause after three consecutive failures" are small but solid governance mechanisms. We can borrow this now for any recurring maintenance agent or background review loop.

**Embedded executable artifacts inside the knowledge tree.** The `index.html` plus `.app` convention is a minimal way to make executable prototypes first-class KB items. This is compelling for demos, visualizations, or task-specific tools, but it needs a concrete workshop use case in Commonplace before it is worth adding.

**Reconnectable browser PTY sessions with buffered output.** Cabinet's daemon keeps detached Claude sessions alive and makes their output retrievable after the UI disconnects. If we ever expose long-running agent tasks through a UI, this is a good implementation reference. Needs a UI use case first.

## Curiosity Pass

**Filesystem-first content, hybrid operational substrate.** The property this claims is inspectability and portability. Mechanistically, Cabinet really does achieve that for content pages: they are plain files with assets beside them. But the repo also contains SQLite, JSON, and JSONL operational stores, so the simpler and truer claim is "files for knowledge, hybrid stores for operations." The "no database" language is product framing, not a literal architecture description.

**The AI team is a persona-and-daemon layer around Claude Code.** The promised property is a working team of differentiated agents. The mechanism is lighter than that phrase suggests: personas are prompt files, the provider registry currently has one real backend, and the daemon is mostly a session/orchestration layer around Claude CLI. Still, this is more than naming. Schedules, workspaces, inboxes, and channel routing give the personas enough operational separation to matter. The genuine contribution is not new multi-agent cognition; it is making a single-model runtime feel like an inspectable team workspace.

**Heartbeats turn freeform runs into structured side effects.** This is the cleanest codified boundary in the repo. A heartbeat can actually create durable artifacts, increment counters, and hand tasks to other personas. But the ceiling is limited by the extraction mechanism: regexes over self-reported model output. Even if it works perfectly, it can only relocate the model's claims into structured files. It cannot verify that a `LEARNING` is true, that a `GOAL_UPDATE` was earned, or that the resulting memory is the right thing to keep.

**Git is the recovery interface, not just backup.** This mechanism genuinely produces a property the raw files do not have: diffable, revertible history. The simpler alternative is periodic snapshots, but git is better because it exposes structured restore and comparison. The weakness is granularity. Because commits stage `.`, Cabinet's history is inspectable but not especially intention-preserving under multi-agent or high-churn use.

**Cabinet collapses library, workshop, and executable artifacts into one tree.** The benefit is fluid movement between reading, running, drafting, and reviewing. That is real product value, and the simpler alternative is stitching together separate tools. But the mechanism mostly improves interface coherence, not knowledge semantics. The split messaging substrates (`messages` in SQLite for generic chat, `.agents/.slack/*.jsonl` for agent Slack) and unused mission-task schema are signs that the unified operating model is still forming.

**"Knowledge compounds" is currently accumulation more than distillation.** Sessions, context files, learnings, task handoffs, digests, and workspaces all persist, so the system definitely compounds artifacts. What it does not yet do is strongly promote, deduplicate, or validate them into a curated knowledge layer. Even if the current loop works perfectly, its ceiling is "agents leave behind organized operational residue," not the richer cross-session knowledge curation that Commonplace is trying to optimize.

## What to Watch

- Whether the richer operational schema (`sessions`, `activity`, `mission_tasks`) becomes a coherent runtime model or remains partly unused scaffolding beside file-based task and Slack systems
- Whether Cabinet adds a real promotion layer from agent residue into curated knowledge, rather than continuing to accumulate context files and transcripts without stronger distillation
- Whether the provider abstraction becomes real beyond Claude Code, or stays as future-facing interface design
- Whether git history becomes more selective than `git add .`, especially if multiple agents begin editing the same tree concurrently
- Whether embedded apps and `.repo.yaml` mature into durable KB primitives with stable conventions instead of staying impressive but lightly coupled differentiators

---

Relevant Notes:

- [A functioning knowledge base needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: Cabinet is the clearest reviewed system where the workshop layer is already productized rather than mostly theoretical
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — foundation: Cabinet's files, git history, and linked repos make agent work inspectable even when the runtime is highly automated
- [Context engineering](../definitions/context-engineering.md) — exemplifies: persona body + memory + inbox + focus-area prompt assembly is a concrete context-engineering loop
- [Distillation](../definitions/distillation.md) — contrasts: Cabinet accumulates agent residue reliably, but most of that accumulation is not yet strong distillation into reusable knowledge
- [Codification](../definitions/codification.md) — sharpens: the heartbeat epilogue parser is a real codified boundary inside an otherwise natural-language workflow
- [Deterministic validation should be a script](../deterministic-validation-should-be-a-script.md) — contrasts: Cabinet has solid runtime safeguards, but comparatively thin content-validation machinery
- [Agent runtimes decompose into scheduler, context engine, and execution substrate](../agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — exemplifies: Cabinet visibly contains all three layers in one product
