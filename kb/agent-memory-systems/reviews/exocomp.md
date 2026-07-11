---
description: "Exocomp review: Go multi-agent coding workbench with YAML roles, .exocomp ledgers, sandboxed tools, skills, and recovery"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Exocomp

Exocomp, from Cookie Engineer's `cookiengineer/exocomp`, is a self-hosted Go multi-agent coding workbench for local projects and local or OpenAI-compatible inference servers. It coordinates a planner and short-lived specialist agents through embedded YAML roles, sandboxed file/program tools, `.exocomp` project ledgers, skill packages, JSONL subprocesses, and session recovery rather than through a vector store or learned memory service.

**Repository:** https://github.com/cookiengineer/exocomp

**Reviewed commit:** [eb7dc19d408a1e1ac55f847c07cbb8881808cfcc](https://github.com/cookiengineer/exocomp/commit/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc)

**Source directory:** `related-systems/cookiengineer--exocomp`

## Core Ideas

**Roles are prompt packages with tool and program authority.** Embedded YAML role files define planner, architect, coder, tester, summarizer, exploiter, and webscanner agents. `Roles.go` parses those files into role templates, while `NewAgent` renders the selected role prompt and installs the role's allowed tools and allowed programs into the new agent ([source/agents/Roles.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/agents/Roles.go), [source/agents/NewAgent.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/agents/NewAgent.go), [source/agents/planner.yaml](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/agents/planner.yaml)).

**The planner manages work through a subprocess hierarchy.** The default planner role is instructed to delegate rather than write code itself, and it can call `agents.Hire` to start short-lived child agents with their own role, prompt, sandbox, and JSONL frontend. The parent records child messages and context usage in memory, then pulls a final work report through `agents.Await`; `agents.Inquire` can launch a temporary summarizer over a child transcript ([docs/USAGE.md](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/docs/USAGE.md), [source/tools/Agents.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Agents.go)).

**Project memory is explicit `.exocomp` JSON.** The current checkout stores requirements, bug reports, and changelog entries under `.exocomp/requirements.json`, `.exocomp/bugs.json`, and `.exocomp/changelog.json` in the playground. Architect, coder, tester, and planner prompts tell agents to read or update those ledgers through tools, making project coordination state visible outside chat history ([source/tools/readRequirements.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/readRequirements.go), [source/tools/writeRequirements.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/writeRequirements.go), [source/tools/writeBugs.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/writeBugs.go), [source/tools/writeChangelog.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/writeChangelog.go)).

**Skills are manual prompt extensions with executable scripts.** The `skills` tool reads `skills/<name>/SKILL.md` packages from the playground, checks their allowed tools and programs, and lets an agent load, unload, or execute them. Loading a skill inserts the skill body as an additional system message; executing a script runs an allowed runtime under sandbox path rewriting, timeout, idle, and 16 MB output controls ([source/tools/readSkills.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/readSkills.go), [source/tools/Skills.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Skills.go), [source/types/Skill.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Skill.go), [source/types/Session.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Session.go)).

**Context efficiency is decomposition plus blunt caps.** Every chat-completion request sends the agent's current message list and installed tool schemas; there is no token-budgeted retrieval layer or automatic compaction before model invocation. Efficiency comes from role separation, child-agent isolation, explicit ledgers, tool/program output caps, context-usage display, and optional summarizer inquiry rather than from semantic memory selection ([source/types/Session.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Session.go), [source/tools/Programs.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Programs.go), [source/utils/bytes/ContextBuffer.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/utils/bytes/ContextBuffer.go), [TODO.md](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/TODO.md)).

**Recovery preserves continuity, not learned guidance.** TTY and web clients restore `.exocomp/session.json` and `.exocomp/agents/*.json` when present, then write the active session and child agents back on shutdown. Debug mode can also snapshot raw request and response JSON under `.exocomp/debug/`. These files preserve state and traces, but I did not find code that distills them into lessons, rules, validators, ranking state, or role changes ([source/types/Recovery.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Recovery.go), [source/ui/tty/Client.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/ui/tty/Client.go), [source/ui/web/Server.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/ui/web/Server.go)).

## Artifact analysis

- **Storage substrate:** `files` — The central retained behavior-shaping state persists as repo-embedded YAML roles, playground `agents/*.yaml` and `skills/*`, playground `.exocomp/*.json` ledgers, `.exocomp/session.json`, `.exocomp/agents/*.json`, `.exocomp/debug/*.json`, and Go source/tool schemas. I did not find a database, vector store, graph store, or model-weight memory substrate.
- **Representational form:** `prose` `symbolic` — Role prompts, skill bodies, requirements, bug descriptions, changelog descriptions, work reports, chat messages, and summaries are prose; YAML/JSON metadata, tool schemas, Go handlers, allowed-tool/program lists, sandbox checks, context counters, and script runtimes are symbolic.
- **Lineage:** `authored` `imported` `trace-extracted` — Built-in roles, tool code, schemas, and local skills are authored or imported; project ledgers are deliberate tool-written outputs from agents and users; session, child-agent, debug, and work-report records derive from runtime traces. The trace-extracted material remains continuity or audit state, not automatically distilled guidance.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Requirements, bugs, changelog entries, restored messages, reports, and summaries advise later agents as knowledge artifacts; role prompts and loaded skills instruct; tool schemas, allowlists, sandbox resolvers, timeouts, and output caps enforce action boundaries; planner delegation and tool dispatch route work; parsers, schema-bound arguments, Go declaration parsing, and permission checks validate writes and calls.

**Role definitions.** Embedded role YAML under `source/agents/` is parsed at startup, and playground `agents/*.yaml` can override or add roles when the `agents` tool boots. The operative parts are prose role prompts plus symbolic model, temperature, allowed-program, and allowed-tool fields. Their behavioral authority is system-definition authority because they become the initial system message and executable surface for each agent ([source/agents/Roles.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/agents/Roles.go), [source/tools/readAgents.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/readAgents.go), [source/agents/SetRole.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/agents/SetRole.go)).

**Project ledgers.** `.exocomp/requirements.json`, `.exocomp/bugs.json`, and `.exocomp/changelog.json` are structured JSON stores containing prose behavior specifications, bug descriptions, and change descriptions keyed by file and symbol. They are knowledge artifacts when listed or searched, and they gain instruction-like force because role prompts tell coders to implement requirements, prioritize bug reports, and log changes ([source/tools/Requirements.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Requirements.go), [source/tools/Bugs.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Bugs.go), [source/tools/Changelog.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Changelog.go)).

**Session and child-agent state.** Current session messages live in memory during a run and are backed up to `.exocomp/session.json`; child agents are backed up to `.exocomp/agents/*.json`. Restored state can shape the next TTY or web session, but it remains raw conversation and agent state rather than a curated memory artifact ([source/types/Session.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Session.go), [source/types/Recovery.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Recovery.go)).

**Tools, schemas, and sandboxing.** Tool schemas are selected from generated schema sets only when a role allows the specific tool function; calls route through namespace implementations. `resolveSandboxPath` and `sanitizeSandboxPath` prevent path escape, while `Programs` and `Skills` restrict executables and cap output. These artifacts carry enforcement and validation authority over what an agent can observe, write, execute, or spawn ([source/tools/Toolset.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Toolset.go), [source/tools/resolveSandboxPath.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/resolveSandboxPath.go), [source/tools/sanitizeSandboxPath.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/sanitizeSandboxPath.go)).

**Skills.** Playground skill packages combine Markdown frontmatter, prose instructions, allowed-tool/program metadata, and optional Go scripts. Loading a skill promotes its prose body into a system message for the current session; executing a script promotes its script metadata into controlled program execution only after the skill is loaded and runtime permissions pass ([source/tools/Skills.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/tools/Skills.go), [source/types/Session.go](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/source/types/Session.go)).

**Promotion path.** Exocomp promotes human requests into planner tasks, planner tasks into specialist-agent prompts, architect output into requirement entries, tester output into bug entries, coder output into changelog and fixed-bug state, and loaded skills into additional system messages. The promotion is explicit and tool-mediated; it does not include source citations, semantic review, automatic relevance matching, or trace-derived lesson synthesis.

## Comparison with Our System

| Dimension | Exocomp | Commonplace |
|---|---|---|
| Primary purpose | Local multi-agent coding, testing, and security workbench | Typed methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Go process state, YAML roles, `.exocomp` JSON, playground skills, recovery files | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports |
| Memory unit | Requirements, bug reports, changelog entries, session messages, child-agent reports, skills | Notes, reviews, instructions, sources, ADRs, indexes, validation and review artifacts |
| Context strategy | Full session context, role isolation, manual ledger lookup, manual skill load, child-agent reports | Search, indexes, authored links, collection/type contracts, skills, validation, review workflows |
| Governance | Role allowlists, sandbox paths, schema-bound tool calls, timeouts, output caps | Frontmatter schemas, collection contracts, citations, validation, semantic review, git lifecycle |

Exocomp and Commonplace both favor inspectable local artifacts over opaque hosted memory. The difference is artifact ambition. Exocomp records operational coordination state for a coding run: what to implement, what failed, what changed, what agents said, and what prompt extensions were loaded. Commonplace records durable methodology knowledge under stronger type, citation, review, and replacement contracts.

Exocomp is stronger on live orchestration. Its planner can spawn role-bounded subprocesses, place them in sub-sandboxes, await their reports, and coordinate them through shared ledgers. Commonplace has skills and review workflows, but not a built-in multi-agent process tree with resumable child-agent state.

Commonplace is stronger on durable knowledge governance. Exocomp's ledgers are easy for agents to read and write, but their schemas are thin, their provenance is mostly path/symbol metadata, and there is no semantic review before an entry shapes later work. That tradeoff fits a local workbench; it would be too loose for long-lived methodology claims.

### Borrowable Ideas

**Role packages as permission bundles.** Commonplace skills could more explicitly pair prose instructions with allowed command/tool surfaces and expected artifact responsibilities. Ready as a skill-authoring convention; actual enforcement needs harness support.

**Narrow project ledgers for active coordination.** Exocomp's requirements/bugs/changelog split keeps live coding state out of freeform chat. Commonplace workshops could use similarly narrow Markdown or JSON ledgers for active review, migration, or validation work. Ready for workshop-local experiments.

**Sub-agent completion reports.** `agents.Quit` plus `agents.Await` gives the parent a bounded report instead of requiring it to consume an entire child transcript. Commonplace could formalize delegated-worker reports as temporary workshop artifacts with task, evidence, result, and residual risk. Ready when a workflow uses several workers.

**Playground skills with executable scripts.** Exocomp's skill loading is a useful model for local task affordances: prose instruction first, script execution only through declared and allowed runtimes. Borrowable where the skill package remains inspectable and execution remains sandboxed.

**Do not borrow raw recovery as knowledge governance.** Restoring a session is valuable continuity, but it does not classify authority, freshness, evidence, or review status. Commonplace should keep recovered traces below curated artifacts unless a workflow promotes them through review.

## Write side

**Write agency:** `manual` `automatic` — Humans and local authors can provide role YAML and skill packages; agents and the system write project ledgers, session backups, child-agent backups, work reports, debug snapshots, and tool-call records. The automatic side is mostly persistence and agent-mediated acquisition/update, not a curation loop over existing memory.

**Curation operations:** `none` — I did not find automatic deduplication, consolidation, synthesis, decay, or learned promotion over retained memory. Bug fixing can mark an existing bug report as fixed, and session shutdown backs up current state, but those are requested tool/state updates rather than an autonomous truth-maintenance or learning policy.

## Read-back

**Read-back:** `both` — Exocomp supports pull through explicit `requirements`, `bugs`, `changelog`, `files`, `agents`, and `skills` calls; it also pushes retained memory when TTY/web startup restores `.exocomp/session.json` and `.exocomp/agents/*.json`, and when a loaded skill is inserted as a system message.

**Read-back signal:** `coarse` — Recovery pushes the saved session and known child agents at session startup if backup files exist, and loaded skills remain present as system messages until unloaded or the session changes. I did not find identifier, lexical, embedding, or judgment-based memory selection for push.

**Faithfulness tested:** `no` — The code restores session state and injects loaded skill bodies, but I did not find with/without tests showing that recovered memory or loaded skills change downstream behavior faithfully.

Pull paths are explicit from the acting agent's perspective: the planner and specialists must call ledger, file, skill, or child-agent tools to retrieve current project memory or reports. The roles instruct those calls, but the memory does not enter the prompt through a relevance selector before each action.

The push paths are coarse and pre-invocation. TTY and web sessions choose recovered state before the session proceeds; skill loading rewrites the session message list so the skill body becomes a system message before the next model call. Static role prompts and tool schemas are baseline system definition, not memory read-back.

Selection and scope are simple. The recovery path is all-or-nothing for the current playground's saved session and agents; skill read-back is manual by skill name; ledger lookup is by explicit list/search calls over `.exocomp` files. There is no top-k selector, token budget, embedding search, or stale-state filter around read-back.

Authority at consumption varies. Restored session messages are continuity context, child-agent reports are advisory knowledge, loaded skills are instruction, and tool schemas/allowlists are enforcement. Effective authority is not verified from code because the repository does not measure whether a model obeys a restored message, report, ledger entry, or loaded skill.

## Curiosity Pass

**The freshest change is storage hygiene.** The reviewed commit moves requirements, bugs, and changelog storage into `.exocomp/`, aligning the operational ledgers with session, child-agent, and debug recovery state rather than scattering generated files at the project root ([commit eb7dc19](https://github.com/cookiengineer/exocomp/commit/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc)).

**The "memory limitation" answer is mainly orchestration.** The README frames tools as a way to beat context length and agent-memory limits, but the current implementation mostly decomposes work into roles, subprocesses, explicit ledgers, and bounded command output rather than retrieving semantically relevant past knowledge.

**The read-back model depends on role discipline.** Planner, coder, tester, and architect prompts say which ledgers to consult and update, but the code does not force a coder to read requirements before editing or a tester to inspect existing bugs before writing tests.

**Skills have high authority once loaded.** A skill body becomes a system message, which is a strong channel for behavior change. The relevance decision is manual, though: the agent has to list/load the skill, and no matcher decides that a skill applies to the current task.

**Recovery can carry stale context forward.** Restored sessions preserve prior messages and possibly prior system messages. I did not find expiry, pruning, or authority labeling on recovered state, so recovery is useful but weakly governed.

**Some documented ambitions are not implemented yet.** The TODO lists tool-call shrinking and agent-history compression as future work, so the current review should not treat those as existing context-efficiency mechanisms ([TODO.md](https://github.com/cookiengineer/exocomp/blob/eb7dc19d408a1e1ac55f847c07cbb8881808cfcc/TODO.md)).

## What to Watch

- Whether `.exocomp` ledgers gain richer provenance, schemas, freshness checks, or validation gates. That would determine whether they remain coordination notes or become trustworthy project knowledge artifacts.
- Whether session recovery gains pruning, expiry, or authority labels. Without that, raw restored context can silently shape later behavior.
- Whether agent-history compression or tool-call shrinking moves from TODO into `Session.go`. That would materially change the context-efficiency story.
- Whether `agents.Inquire` summaries become persisted artifacts or feed the ledgers. That would create a real trace-to-summary path.
- Whether skill loading gains relevance matching, activation hooks, or policy review. That would shift read-back from manual/coarse behavior toward targeted push.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Exocomp stores ledgers and recovery state, but most project memory returns only through explicit tool calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Exocomp's roles, ledgers, session files, tools, skills, and reports differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: requirements, bugs, changelogs, work reports, summaries, and restored traces advise later action.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: role prompts, tool schemas, allowed-program lists, loaded skills, sandbox rules, and validation checks instruct or constrain behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames Exocomp's main mechanism: routing local project state and role-bounded capabilities into multi-agent coding work.
