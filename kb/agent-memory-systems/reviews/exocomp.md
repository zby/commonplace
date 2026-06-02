---
description: "Exocomp review: Go multi-agent coding workbench with YAML roles, sandboxed tools, JSON ledgers, and session recovery"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# Exocomp

Exocomp, from Cookie Engineer's `cookiengineer/exocomp` repository, is a self-hosted Go multi-agent environment for local coding and testing workflows. It runs role-specialized agents against OpenAI-compatible local inference servers, exposes terminal, JSONL, web, and webview interfaces, and coordinates work through sandboxed tools, subprocess agents, and project-local JSON ledgers rather than a vector memory store.

**Repository:** https://github.com/cookiengineer/exocomp

**Reviewed commit:** [6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5](https://github.com/cookiengineer/exocomp/commit/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5)

**Last checked:** 2026-06-01

## Core Ideas

**Roles are authored prompt-and-capability packages.** Agent behavior starts from embedded YAML role files for planner, architect, coder, tester, summarizer, exploiter, and webscanner. Each role bundles prose instructions, model and temperature defaults, allowed tools, and allowed programs; `NewAgent` renders the role prompt into the first system message and installs the role's tool/program permissions (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/agents/Roles.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/agents/NewAgent.go, https://github.com/cookiengineer/exocomp/tree/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/agents).

**Multi-agent work is a process hierarchy.** The planner can hire short-lived subprocess agents through the `agents.Hire` tool. A child agent receives its own role, prompt, sandbox, and JSONL frontend; the parent keeps a live in-memory record of the child's emitted messages and context usage, then retrieves a final work report through `agents.Await` (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/docs/USAGE.md, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/Agents.go).

**The shared project memory is explicit tool-written JSON.** Requirements, bug reports, and changelog entries are stored as `exocomp-requirements.json`, `exocomp-bugs.json`, and `exocomp-changelog.json` under the playground. The role prompts tell architects, coders, testers, and planners to read and write those ledgers through tools instead of relying only on chat history (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/readRequirements.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/writeRequirements.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/readBugs.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/writeChangelog.go).

**Skills are manual prompt extensions with executable scripts.** The `skills` tool reads `SKILL.md` packages from the playground, validates allowed tools and programs, and lets an agent load, unload, or execute skill scripts. Loading a skill inserts the skill body as an additional system message; executing a skill runs an allowed runtime with sandbox path rewriting and output limits (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/types/Skill.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/Skills.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/types/Session.go).

**Context efficiency is mostly process isolation and manual compression.** Exocomp asks the inference server for context length and tracks prompt-token usage, but each chat-completion request sends the full current message list and all currently available tool schemas. It limits program and skill-script output to 16 MB, times out long executions, keeps subprocess agents separate, and provides `agents.Inquire` to summarize another agent's conversation through a summarizer agent; it does not implement vector retrieval, token-budgeted memory selection, or automatic conversation compaction (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/types/Session.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/tools/Agents.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/utils/bytes/ContextBuffer.go).

**Recovery preserves sessions rather than learning from them.** TTY and web sessions restore `.exocomp/session.json` and `.exocomp/agents/*.json` when present, then back up the active session and known child agents on shutdown. Debug mode can also snapshot raw request and response JSON. These are continuity artifacts and audit traces, not a learned memory pipeline (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/types/Recovery.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/ui/tty/Client.go, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/ui/web/Server.go).

## Artifact analysis

- **Storage substrate:** `files` — Go-embedded YAML under `source/agents/`, with an extension hook that reads `agents/*.yaml` from the playground at tool boot
- **Representational form:** `mixed` — Mixed prose and symbolic permissions: role prompts, model defaults, temperature, allowed tools, and allowed programs

**Embedded and playground-provided role definitions.** The storage substrate is Go-embedded YAML under `source/agents/`, with an extension hook that reads `agents/*.yaml` from the playground at tool boot. The representational form is mixed prose and symbolic permissions: role prompts, model defaults, temperature, allowed tools, and allowed programs. Lineage is authored configuration, either shipped in the repository or supplied by the local playground. Behavioral authority is system-definition artifact authority: the role package defines the initial system prompt and the executable surface available to the agent.

**Session message history and recovery files.** The storage substrate is in-memory `Session.Agent.Messages` during a run and `.exocomp/session.json` plus `.exocomp/agents/*.json` for TTY/web recovery. The representational form is structured JSON containing prose chat messages, tool-call records, role metadata, and context-usage counters. Lineage is raw runtime interaction: user messages, assistant outputs, tool results, child-agent message streams, and restored prior state. Behavioral authority is continuity context when restored or retained in the current request; it is a knowledge artifact and soft instruction context, not curated durable guidance.

**Requirements, bugs, and changelog ledgers.** The storage substrate is project/playground JSON files: `exocomp-requirements.json`, `exocomp-bugs.json`, and `exocomp-changelog.json`. The representational form is symbolic JSON with prose fields for behaviors, bug descriptions, and change descriptions. Lineage is deliberate agent tool use, not passive transcript mining: architects define requirements, testers report bugs, coders mark fixes and log changes. Behavioral authority is mixed: these files are knowledge artifacts when planners or agents list/search them, and system-definition artifacts when role prompts require later agents to prioritize bug reports, implement requirements, or log changes.

**Tool schemas and tool handlers.** The storage substrate is Go source code plus embedded JSON schemas generated into the binary. The representational form is symbolic: JSON-schema-like function definitions, Go method dispatch, sandbox path resolvers, allowed-program checks, timeouts, and output caps. Lineage is authored implementation. Behavioral authority is system-definition authority over what agents may observe, mutate, execute, spawn, or report.

**Skill packages.** The storage substrate is `skills/<name>/SKILL.md` and `skills/<name>/scripts/*` in the playground. The representational form is mixed: Markdown frontmatter, prose instructions, allowed-tool/program metadata, and executable scripts. Lineage is imported or locally authored skill material. Behavioral authority becomes system-definition authority only after manual `skills.Load`, which inserts the skill body as a system message; scripts have executable authority only through `skills.Execute` and the role's allowed programs.

**Sub-agent work reports and summaries.** The storage substrate is initially the parent process's in-memory `Agents.contents` map and, for recovered agents, `.exocomp/agents/*.json`. The representational form is chat-message JSON plus prose work reports returned through `agents.Quit`; `agents.Inquire` can create a temporary summarizer-agent output but does not persist a separate summary artifact. Lineage is child-agent execution output. Behavioral authority is advisory context for the parent planner when pulled through `agents.Await` or `agents.Inquire`.

**Promotion path.** Exocomp's most concrete promotion path is user request -> planner delegation -> architect requirements -> coder/tester action -> bugs/changelog updates -> planner read-back. That promotes transient conversation into structured JSON ledgers through explicit tool calls, not through automatic trace extraction. A second path is authored skill package -> manual load -> system-message authority. Neither path includes semantic validation, item-level provenance beyond file/symbol fields, or automatic relevance-gated activation.

## Comparison with Our System

| Dimension | Exocomp | Commonplace |
|---|---|---|
| Primary purpose | Local multi-agent coding and testing workbench | Typed, agent-operated methodology knowledge base |
| Main substrate | Go process state, project JSON files, YAML roles, playground skills, `.exocomp` recovery | Git-tracked Markdown collections, type specs, sources, indexes, reports, and validation outputs |
| Memory unit | Session messages, work reports, requirements, bug reports, changelog entries, skills | Notes, reviews, instructions, source snapshots, ADRs, generated indexes, review reports |
| Activation | Full session context, restored state, manual tool lookup, manual skill load, subprocess reports | Mostly explicit search/index/link/skill pull, with validation and review gates |
| Governance | Role tool/program allowlists, sandbox path checks, timeouts, output caps | Collection contracts, frontmatter schemas, validation, semantic review, git diff lifecycle |
| Context control | Subprocess isolation, output caps, context usage display, ad hoc summarizer inquiry | Lexical routing, curated/generated indexes, artifact types, source snapshots, review workflows |

Exocomp and Commonplace both prefer inspectable local artifacts over opaque managed memory. The difference is what gets treated as durable knowledge. Exocomp's durable project memory is operational and task-specific: requirements, bug reports, changelogs, recovered session state, and skill prompts. Commonplace's durable memory is library-shaped: typed artifacts with collection contracts, citations, validation, and review status.

Exocomp is stronger on live agent orchestration. The planner can spawn role-bounded workers, keep them in isolated sandboxes, await reports, and route work through shared ledgers. Commonplace has skills and review workflows, but it does not natively model a subprocess agent team with role-specific tools and resumable child-agent state.

Commonplace is stronger on artifact governance. Exocomp's JSON ledgers are easy for agents to read and write, but they have thin schemas, no citation discipline, no validation lifecycle beyond tool-level parsing, and no semantic review before a recorded requirement or bug influences later action. That is appropriate for a local coding workbench but too weak for durable methodology claims.

**Read-back:** `both` — But not relevance-gated. Role prompts and restored sessions are pushed unconditionally into the agent's context; requirements, bugs, changelogs, work reports, file contents, and skills enter through explicit tool calls or manual skill loading

### Borrowable Ideas

**Role packages as permissioned prompt bundles.** Commonplace skills could more explicitly pair prose instructions with allowed command/tool surfaces and expected artifact responsibilities. Ready as a skill-authoring convention; enforcement would need harness support.

**Project ledgers for coordination state.** Exocomp's requirements/bugs/changelog split is a practical way to keep multi-agent coding coordination out of freeform chat. Commonplace workshop runs could use similarly narrow JSON or Markdown ledgers for active review work. Ready for workshop-local experiments.

**Sub-agent work reports as first-class artifacts.** The `agents.Quit`/`agents.Await` pattern gives the parent a bounded completion report instead of a whole transcript. Commonplace could formalize sub-agent reports as temporary workshop artifacts with source task, result, and residual risk. Ready when a workflow uses multiple worker agents.

**Output caps around executable tools.** Exocomp's 16 MB output buffer and idle/time limits are blunt but useful context-protection controls. Commonplace command wrappers should keep explicit output budgets and pointer-to-full-output patterns for high-volume runs. Ready now for command design.

**Do not borrow recovery as memory governance.** Resuming a raw session is useful continuity, but it does not distinguish evidence, instruction, stale state, or validated knowledge. Commonplace should keep recovered traces below curated artifacts unless they are promoted through review.

## Curiosity Pass

**The "memory limitation" answer is mostly decomposition, not retrieval.** The README frames tools as an effort to beat context length and memory limits, but the implementation mostly splits work into roles, subprocesses, and explicit ledgers rather than retrieving semantically relevant past material (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/README.md, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/types/Session.go).

**Manual skill loading is intentionally powerful but not activation logic.** A loaded skill becomes a system message, which is high authority, but the trigger is an agent's explicit `skills.Load` call and permission check. There is no matcher deciding that a skill is relevant before an action.

**Session recovery can carry stale authority forward.** Restored message histories preserve prior system messages and conversation context, which is convenient for continuity but weakly governed. I did not find expiry, pruning, or stale-state checks for recovered sessions.

**The summary path is live and disposable.** `agents.Inquire` summarizes another agent's conversation by launching a summarizer in a temp directory, then returns the final message. That helps a planner inspect work without loading a full child transcript, but the summary is not itself a durable promoted artifact.

**The web/API docs are thinner than the code surface.** The API document lists session and settings routes, while the server code exposes additional session routes for config, tools, and direct tool calls (https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/docs/API.md, https://github.com/cookiengineer/exocomp/blob/6a4ff3122104f25f94873a4ead1ca8d7ce3cc2c5/source/ui/web/Server.go).

## What to Watch

- Whether requirements, bugs, and changelogs gain stronger schemas, provenance, or validation. That determines whether the ledgers remain coordination notes or become trustworthy project knowledge artifacts.
- Whether session recovery gains pruning, expiry, or authority labeling. Without that, restored raw traces can silently shape later behavior.
- Whether `agents.Inquire` summaries become persisted or referenced by work reports. If they do, Exocomp would gain a real trace-to-summary artifact path that should be re-evaluated for trace-derived placement.
- Whether skill loading gains relevance matching or pre-action hooks. That would change read-back from manual pull/always-load behavior toward engineered activation.
- Whether context controls move from token display and output caps to budgeted prompt assembly. That would make Exocomp's process decomposition less dependent on agent discipline.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Exocomp stores ledgers and recovery state, but most project memory returns through explicit tool calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Exocomp's role YAML, session JSON, tool schemas, ledgers, skills, and work reports differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: recovered transcripts, work reports, bug lists, changelog entries, and requirements can serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: role prompts, tool schemas, allowed-program lists, loaded skills, and sandbox rules instruct or constrain behavior.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - relates: Exocomp splits retained state across repo-embedded YAML, playground JSON, `.exocomp` recovery files, and local skill directories.
