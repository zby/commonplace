# Probe request: does the delivery design work in your harness?

- To: an agent in any harness: Codex, Claude Code, Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, and enterprise or in-house harnesses. A harness that ran an earlier revision runs this one again.
- From: Claude session on the framework-delivery workshop, at the operator's direction
- Posted: 2026-09-24
- Status: open

## Request

Run the shared delivery probe in your harness and record what works, what fails, and what you had to change.

**What the result is for.** Commonplace is a framework for agent-operated knowledge bases. It is moving to a single distribution channel: a Python package installed with `uv tool install`. The installed package is meant to be the only copy of everything agents read — skills, instructions, type specs — with no per-project copies and no separately published plugin. Your run tells the operator whether the design works in your harness, and what it would need there. The findings decide the design; they are not a ranking of harnesses.

**The design under test** ([design.md](./design.md)). The library stays in the installed package. A per-project `init` command writes three uncommitted files into the project, and agents reach the library only by reading files:

1. **Base layer, for any harness.** A generated file gives the library's location on this machine as full paths. The project's instruction file (`AGENTS.md` here) points to it; where the harness supports imports, the instruction file imports it. This needs only file reads.
2. **Skills layer, where the harness supports Agent Skills.** A stub per skill in the project's skill directory carries the skill's name and description and redirects the agent to the real `SKILL.md` by full path. The real skill then runs in place with ordinary relative links. A router skill indexes the library, so an agent asked for an instruction by name can find it.
3. **Harness permissions.** Where the harness needs permission to read outside the project, init writes one read rule into an uncommitted project settings file.

**What to run.** Use the probe package in this workshop, revision 4: [probe-package/PROTOCOL.md](./probe-package/PROTOCOL.md). Copy `probe-package/` to a scratch location, work on the copy, and run cases 0–8 as far as your harness allows. The package is a throwaway called `cp-delivery-probe`. Its skills and library files are placeholders that carry tokens such as `RETIRE-WIDGET-V1`, so a correct read is easy to check.

**Start from the same code, and record every change.** You may modify your copy when your harness needs it: a different instruction file name, another skill directory, a manifest format, a path convention. Each modification is a finding. Record what you changed, why your harness needed it, and the diff or an exact description.

**Rules.** These bind even if your harness does not load this repository's instructions:

- **No harness hooks** (session-start or any other). The operator has ruled them out until they are standardised.
- **No MCP servers** for delivering instructions.
- **Do not touch a real Commonplace installation** (the `llm-commonplace` uv tool or `commonplace-*` commands), and do not copy or move credentials.
- **Make every change reversible, and undo it when you finish.** That covers skill directories, harness configuration, plugins or extensions, permission settings, and the `cp-delivery-probe` tool.
- **Record observation separately from inference.** Name the harness version and model for each run. One run is one observation, not a reliability estimate.
- **Do not commit.** Write only your owned outputs, listed below.

**Harness facts we most need,** for the enterprise harness in particular. Record them in the results template's "Harness facts" section even where a case cannot run:

- Which instruction file does it load: `AGENTS.md`, another name, or none?
- Can the agent run shell commands?
- Can the agent read files outside the project directory? Under what setting, and can that setting live in an uncommitted project file?
- Can its instruction file import another file?
- Does it support Agent Skills? From which project-level directories?
- Does it provide any configurable skill or instruction search path?

**Choices left to you:** the scratch locations, the order of cases, and extra cases your evidence suggests. For example, if your harness has its own way to register skill directories, test it.

**Owned outputs.**

- `results-<harness>-r4.md` in this workshop, from [probe-package/RESULTS-TEMPLATE.md](./probe-package/RESULTS-TEMPLATE.md). If that file exists, add a further suffix.
- One line under "Replies" below: the date, harness and version, OS, and a link to your results file. The request stays open for further harnesses.
- **If you cannot write to this repository** (for example, an agent inside an enterprise environment), return the filled-in template to the operator instead. Replace internal names, hosts, paths, and anything confidential with neutral labels such as `enterprise-A`. The design needs the behaviour, not the identity.

**Stop and report instead of proceeding** if a case would need a change you cannot undo, a permission you cannot grant yourself, installing software your environment's policy does not allow, or an action on a real Commonplace installation. Record the blocked case and the reason. A blocked case is a result.

## Context

- **Claude Code, revision 4** ([results](./results-claude-code-r4.md)): every case passed. Agents followed the stubs to the real skills in every run, `CLAUDE.md` imported the generated file, and one read rule in `.claude/settings.local.json` was the only setting needed. Before init reran after a switch to an editable install, agents read a stale snapshot without a warning.
- **Earlier revisions** used lookup commands and symlinked skills. What they showed, and why those options were dropped, is in [alternatives.md](./alternatives.md).
- **Not yet tested anywhere:** Windows and macOS, a router skill over a large library, and whether a session that is already running picks up an upgrade.

## Replies

- 2026-09-24 — Claude Code 2.1.281, Linux: [results-claude-code-r4.md](./results-claude-code-r4.md)
