# Probe request: does the delivery design work in your harness?

- To: an agent, or a person, working in any harness: Codex, Claude Code, Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, and enterprise or in-house harnesses. A harness that ran an earlier revision runs this one again.
- From: Claude session on the framework-delivery workshop, at the operator's direction
- Posted: 2026-09-24
- Status: open

## Intent

Commonplace is a framework for agent-operated knowledge bases. We are deciding how it reaches the projects that use it. The plan is that one installed Python package holds everything agents read (skills, instructions, type specs), and each project gets only a few small, uncommitted files that point into that package ([design.md](./design.md)).

The design rests on six assumptions about the harness, listed with what each "no" would change in [design.md, "What the design assumes about a harness"](./design.md#what-the-design-assumes-about-a-harness). Your answers tell us which assumptions hold in your harness. The goal is to learn whether the design works for you, or what it would need; this is not a ranking of harnesses.

**Answer at whatever depth you can.** A few yes/no answers from what you know already decide most of it. "Unknown" and "not allowed here" are useful answers. Stop at any level below.

## Level 1: six questions, from what you know

No setup needed. For each, answer yes, no, or unknown, with a sentence of detail if you have it:

1. **Install.** May a user install a Python command-line tool at user level, for example with `uv tool install`? From PyPI, or only from an internal index or a wheel file?
2. **Project instructions.** Does the agent read instructions from a file in the repository? Which file name (`AGENTS.md`, `CLAUDE.md`, other)? Can that file import another file?
3. **Reads outside the project.** Can the agent read a file under the user's home directory, outside the project? If it needs a setting, who can set it (the user, per project or globally; only an administrator), and can the setting live in an uncommitted project file?
4. **Following a pointer.** If an instruction file says "read the file at `<absolute path>` and follow it", does the agent do that?
5. **Skills.** Does the harness discover Agent Skills (`SKILL.md` directories)? From which project directories?
6. **Shell.** Can the agent run shell commands?

## Level 2: a ten-minute check, with nothing installed

This tests questions 2–5 directly. Everything it creates can be deleted afterwards.

1. Outside the project (for example, in your home directory), create a file `probe-target.md` containing: "Reading this file means reporting the token `POINTER-OK`."
2. In the project's instruction file, add: "For the delivery probe, read `<absolute path to probe-target.md>` and follow it."
3. If the harness supports skills, create `<project skill directory>/probe-stub/SKILL.md` with frontmatter `name: probe-stub` and `description: Use only when asked to run the probe stub.`, and the body: "Read `<absolute path to probe-target.md>` and follow it."
4. In fresh sessions, ask: "Run the delivery probe." and, if you created the stub, "Run the probe stub." Record whether the agent reported `POINTER-OK`, and any permission prompt or denial.

## Level 3: the full protocol

The probe package, revision 4, tests the whole design, including upgrades and install-mode switches: [probe-package/PROTOCOL.md](./probe-package/PROTOCOL.md). Copy `probe-package/` to a scratch location, work on the copy, and run cases 0–8 as far as your harness allows. You may modify your copy where your harness needs it (a different instruction file, another skill directory, a path convention). Each modification is a finding: record what you changed and why.

## Rules

These bind at every level, even if your harness does not load this repository's instructions:

- **No harness hooks** and **no MCP servers** for delivering instructions.
- **Do not touch a real Commonplace installation** (the `llm-commonplace` uv tool or `commonplace-*` commands), and do not copy or move credentials.
- **Undo every change when you finish:** files you created, settings, and the `cp-delivery-probe` tool.
- **Record observation separately from inference,** and name the harness version and model. One run is one observation, not a reliability estimate.
- **Stop and report instead of proceeding** if a step would need a change you cannot undo, a permission you cannot grant yourself, or software your environment's policy does not allow. A blocked step is a result.
- **Do not commit.** Write only your owned outputs.

## How to reply

- **If you can write to this repository:** put your answers in `results-<harness>-r4.md` in this workshop. For Level 3, use [probe-package/RESULTS-TEMPLATE.md](./probe-package/RESULTS-TEMPLATE.md); for Levels 1–2, a short list of answers is enough. Then add one line under "Replies" below: the date, harness and version, OS, the level you reached, and a link to your file.
- **If you cannot** (for example, inside an enterprise environment), send your answers to the operator. Replace internal names, hosts, paths, and anything confidential with neutral labels such as `enterprise-A`. The design needs the behaviour, not the identity.

## Context

- **Claude Code, revision 4** ([results](./results-claude-code-r4.md)): every case passed at Level 3. All six assumptions hold on Linux; one read rule in `.claude/settings.local.json` was the only setting needed.
- **Earlier revisions** used lookup commands and symlinked skills. What they showed, and why those options were dropped, is in [alternatives.md](./alternatives.md).
- **Not yet tested anywhere:** Windows and macOS, a router skill over a large library, and whether a session that is already running picks up an upgrade.

## Replies

- 2026-09-24 — Claude Code 2.1.281, Linux, Level 3: [results-claude-code-r4.md](./results-claude-code-r4.md)
