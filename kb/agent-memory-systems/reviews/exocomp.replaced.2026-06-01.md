---
description: "Local Go coding-agent harness with role prompts, subprocess agents, tool allowlists, sandbox path checks, coordination JSON, and loadable skills"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Exocomp

> Replaced 2026-06-01. See [exocomp](./exocomp.md) for the current review.

Exocomp is Cookie Engineer's self-hosted multi-agent coding environment for Go projects. It wraps an OpenAI-compatible local or external inference server with role-specific system prompts, tool schemas, sandboxed file/program tools, subprocess contractor agents, and project coordination files for requirements, bugs, and changelog state.

**Repository:** https://github.com/cookiengineer/exocomp

**Reviewed commit:** [30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3](https://github.com/cookiengineer/exocomp/commit/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3)

## Core Ideas

**Role behavior is split between prose prompts and symbolic capability sets.** Each implemented agent constructor embeds a role prompt as the first system message and pairs it with explicit `AllowedTools` and `AllowedPrograms` fields on the `types.Agent` object ([agents/Planner.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Planner.go), [agents/Coder.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Coder.go), [types/Agent.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/types/Agent.go)). The prompt is a prose system-definition artifact because it instructs the model; the allowlists are symbolic system-definition artifacts because `Toolset`, `Session.GetTool`, `Programs.Execute`, and `Skills.Execute` enforce them at runtime ([tools/Toolset.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Toolset.go), [types/Session.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/types/Session.go), [tools/Programs.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Programs.go), [tools/Skills.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Skills.go)).

**The planner is a manager, not a coding agent.** `Planner.txt` tells the planner to clarify with the human, plan phases, delegate to architect/coder/tester/summarizer agents, track artifacts, and never write production code or tests itself ([agents/Planner.txt](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Planner.txt)). The implementation gives the planner `agents.Hire`, `agents.Fire`, read-only file access, and no program execution or file writes ([agents/Planner.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Planner.go)). This makes coordination itself the primary behavior surface: the planner's memory of work lives in its message history and in the project coordination files produced by workers.

**Subagents are real subprocesses with inherited project context.** `agents.Hire` resolves the requested child sandbox under the parent sandbox, creates the folder if needed, starts the Exocomp binary in `jsonl` mode, sets the child process working directory to that sandbox, and sets the child's `--playground` to the parent sandbox ([tools/Agents.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Agents.go)). The parent keeps per-agent message histories in memory by reading the child's JSONL output and can summarize a child with a temporary summarizer subprocess through `agents.Inquire` ([tools/Agents.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Agents.go)). The subprocess tree is therefore a runtime task-state mechanism, not a persistent agent-memory database.

**Sandboxing is path-based and capability-based.** The README defines the current working directory as the sandbox, and the code enforces that model-visible file paths resolve under the configured sandbox before read/write/list/stat/copy operations ([README.md](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/README.md), [tools/resolveSandboxPath.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/resolveSandboxPath.go), [tools/Files.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Files.go)). Program execution is separately limited to the role's allowed program names, and path-like command arguments are sanitized back into sandbox-relative paths ([tools/Programs.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Programs.go), [tools/sanitizeSandboxPath.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/sanitizeSandboxPath.go)). The sandbox is not a container or OS policy in the inspected code; it is a runtime contract around Exocomp's tools.

**Coordination state is durable JSON in the playground.** The requirements, bugs, and changelog tools persist their maps to `exocomp-requirements.json`, `exocomp-bugs.json`, and `exocomp-changelog.json` in the parent playground ([tools/writeRequirements.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/writeRequirements.go), [tools/writeBugs.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/writeBugs.go), [tools/writeChangelog.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/writeChangelog.go)). Requirements are system-definition artifacts when architects define implementable function, interface, struct, and test contracts for coders and testers; bugs are knowledge artifacts until the coder consumes them as repair obligations; changelog entries are audit knowledge artifacts that document what changed ([tools/Requirements.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Requirements.go), [tools/Bugs.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Bugs.go), [tools/Changelog.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Changelog.go)).

**Skills add prompt and script surfaces under the same authority model.** The skills tool scans `skills/*/SKILL.md`, parses frontmatter for allowed programs and tools, and can load a skill body as an additional system message if the current agent already has the required capabilities ([tools/readSkills.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/readSkills.go), [utils/skill/ParseSkill.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/utils/skill/ParseSkill.go), [types/Session.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/types/Session.go)). Skill scripts are executed only through supported runtimes already present in the agent's allowed programs ([tools/Skills.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Skills.go)). This is close to commonplace skills in shape, but Exocomp treats loaded skill bodies as live prompt policy rather than typed KB artifacts with review status.

## Comparison with Our System

| Dimension | Exocomp | Commonplace |
|---|---|---|
| Primary retained state | Role prompts, allowlists, skills, session messages, `exocomp-*.json` coordination files | Typed markdown notes, instructions, reviews, sources, generated indexes, validation outputs |
| Storage substrate | Go source, embedded prompt text, project-local JSON files, in-memory sessions | Git-tracked markdown and JSON/YAML artifacts, generated indexes, review records |
| Representational form | Mixed prose prompts, symbolic Go code, symbolic JSON state, tool schemas | Mostly prose notes/instructions plus symbolic schemas, scripts, indexes, validators |
| Behavioral authority | Prompts instruct; allowlists and sandbox checks enforce; coordination JSON routes and constrains workers | Type contracts, instructions, validators, review gates, authored links, and skills shape later agents |
| Activation | Runtime session construction, chat-completions tool calls, planner hiring subprocesses | Search/navigation, skill loading, instruction following, validation and review commands |
| Lifecycle | Runtime sessions plus project files; no built-in status, archive, supersession, or index regeneration for coordination artifacts | Frontmatter status, git history, generated indexes, review workflows, validation, archival replacement |

Exocomp is more of an agent harness than a knowledge base. Its strongest memory-like design is not retrieval: it is authority routing. The planner, architect, coder, tester, summarizer, and pentester roles each receive different prompts and different executable surfaces, so the same project state changes behavior through which role is allowed to consume or mutate it.

Commonplace makes artifact contracts explicit and durable. Exocomp's implementation has the same underlying distinctions, but they are implicit in code: requirements instruct future agents, bugs advise and obligate repair, changelog entries audit, prompts instruct, tool schemas expose options, allowlists enforce, and sandbox functions reject out-of-scope paths. That gives Exocomp a practical authority lattice without a written artifact taxonomy.

The main tradeoff is operational immediacy versus inspectable lineage. Exocomp can turn a human request into a planner-managed subprocess tree with coders and testers operating in project folders. Commonplace is slower but stronger when a future agent must know why an artifact exists, which source it came from, whether it is current, and how to retire or regenerate it.

Exocomp does not qualify as trace-derived learning in the inspected implementation. It records live session messages and parent-side summaries, and agents can manually write requirements, bugs, changelog entries, or skills, but there is no durable extraction pipeline that consumes conversation/tool traces and promotes distilled lessons into retained behavior-changing artifacts.

**Read-back:** both — role prompts are injected at session construction, and agents can load skills or read coordination files through tools.

## Borrowable Ideas

**Use role allowlists as part of the artifact contract.** Ready to borrow for agentic KB operations. Commonplace already has skills and commands, but Exocomp's constructors make the operational boundary easy to audit: a planner can hire, an architect can define requirements, a coder can write and run Go, a tester can write tests and report bugs. A commonplace workshop could express worker ownership with the same explicit tool/program matrix.

**Persist coordination files beside the project, not inside the chat.** Ready to borrow where a task has multiple worker roles. `exocomp-requirements.json`, `exocomp-bugs.json`, and `exocomp-changelog.json` give short-lived agents a shared surface that survives individual message windows. The commonplace analogue would be a workshop-local state file with typed entries and validation, not a free-form chat summary.

**Treat path sandbox checks as behavior-shaping infrastructure, not just safety code.** Ready as a design principle. Exocomp's sandbox boundary defines what an agent can know and change, which makes it a system-definition artifact in practice. Commonplace worker workflows should make source roots, writable roots, and generated-output roots similarly explicit.

**Borrow the subprocess contractor model cautiously.** Useful when role separation matters more than shared context. Exocomp's planner can launch fresh role-specialized agents, but the inspected implementation keeps most dialogue state in memory and uses summaries for status. Commonplace would need stronger durable handoff records before relying on this pattern for long-running KB maintenance.

**Do not borrow implicit lifecycle semantics.** The coordination JSON files are useful, but they lack frontmatter-like status, source lineage, review state, and retirement rules. Commonplace should preserve those lifecycle controls when adopting any Exocomp-style project state.

## Curiosity Pass

**The README lists more roles than `NewAgent` actually implements.** `agents/Types.go` lists architect, coder, pentester, planner, summarizer, and tester, while `NewAgent` returns constructors for architect, coder, planner, summarizer, and tester and leaves researcher as a TODO; the README also names roles such as researcher, reverser, and threat hunter ([agents/Types.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Types.go), [agents/NewAgent.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/NewAgent.go), [README.md](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/README.md)). The review should treat those additional roles as planned or partial unless the code path is present.

**The pentester constructor appears to embed the architect prompt.** `Pentester.go` declares `pentester_prompt` but calls `renderPrompt(name, string(architect_prompt))`, which means the inspected code may give pentester agents architect instructions instead of pentester instructions ([agents/Pentester.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/agents/Pentester.go)). That matters because Exocomp's role model depends on prompt authority matching capability authority.

**Subagent timeout policy is conversation-progress based.** Hired agents run with a ten-minute context, but a background loop cancels after one minute without new messages; another goroutine removes finished processes from the active map ([tools/Agents.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Agents.go)). This is a simple task lifecycle mechanism, but it is not a durable work queue.

**Tool schemas are manually curated API surfaces.** JSON files such as `Agents.json` and `Programs.json` describe callable functions and parameters, while Go code separately implements the methods ([tools/Agents.json](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Agents.json), [tools/Programs.json](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Programs.json), [tools/Agents.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Agents.go), [tools/Programs.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/tools/Programs.go)). This is powerful but creates a schema/code drift surface to watch.

**Debug artifacts are useful but local and ephemeral.** In debug mode, session inference writes `.exocomp-request.json` and `.exocomp-response.json` under the sandbox ([types/Session.go](https://github.com/cookiengineer/exocomp/blob/30cee64a2c1b4d759e6dcaa6a06446fcd1309bb3/types/Session.go)). Those files can support diagnosis, but the inspected implementation does not promote them into reviewed lessons, tests, or policies.

## What to Watch

- Whether requirements, bugs, and changelog files gain schemas, status fields, source IDs, or review rules that make them stronger durable memory artifacts.
- Whether session histories or debug request/response files become source traces for automatic summarization, lesson extraction, or skill generation.
- Whether role constructors and README role tables converge, especially for pentester/researcher/reverser/threat-hunter support.
- Whether sandboxing moves from path checks in tool implementations toward OS/container isolation for executed programs and skill scripts.
- Whether skills gain provenance, review status, versioning, or retirement semantics instead of being loaded directly from local `SKILL.md` files.

---

Relevant Notes:

- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: bugs, changelog entries, session summaries, and debug traces when consumed as evidence or advice
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, allowlists, tool schemas, sandbox checks, requirements, and loaded skills when they instruct or enforce behavior
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: Exocomp's main design move is routing different authority through different agent roles
- [representational form](../../notes/definitions/representational-form.md) - sharpens: Exocomp mixes prose prompts, symbolic Go code, JSON coordination state, and tool schemas
- [lineage](../../notes/definitions/lineage.md) - cautions: coordination files need source and revision lineage before becoming trustworthy long-term memory
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - compares-with: Exocomp activates retained behavior by constructing sessions and exposing tools, not by retrieval alone
