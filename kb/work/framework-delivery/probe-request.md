# Probe request: can an agent in your harness adapt to the delivery design?

- To: an agent, or a person with an agent, working in any harness: Codex, Claude Code, Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, and enterprise or in-house harnesses. A harness that ran an earlier revision runs this one again.
- From: Claude session on the framework-delivery workshop, at the operator's direction
- Posted: 2026-09-24
- Status: open

## Intent

Commonplace is a framework for agent-operated knowledge bases. We are changing how it reaches the projects that use it. One installed Python package will hold everything agents read (skills, instructions, type specs), and each project gets only a few small, uncommitted files that point into that package ([design.md](./design.md)).

We cannot test every harness ourselves, and we cannot write a separate install route for each. So the question is not whether our exact files work unchanged in your harness. It is whether **an agent working in your harness, told what the design is for, can make it work there**, adapting where it has to. If it can, the design is good enough for your harness. If it cannot, we need to know which outcome it could not reach.

**Report outcomes, not mechanisms.** Your agent may build whatever workaround your harness needs. Tell us whether each outcome below was reached. You do not have to say how, and you should not include anything confidential.

## What to give the agent

- The probe package, revision 4: copy [probe-package/](./probe-package/PROTOCOL.md) to a scratch location. It is a throwaway Python package called `cp-delivery-probe`. Its library files carry tokens such as `RETIRE-WIDGET-V1`, so a correct read is easy to check. `cp-delivery-probe-init` writes the project files the design calls for, as they work in Claude Code and Codex.
- This request, as the statement of intent. [PROTOCOL.md](./probe-package/PROTOCOL.md) describes one tested way to run each check; the agent may follow it or take its own route.

## Outcomes to reach

In a scratch project, working as your users would:

1. **Install.** The package is installed for the user, as a Python command-line tool (for example with `uv tool install`, from PyPI, an internal index, or a wheel file).
2. **A named instruction.** Asked "Follow the retire-widget procedure from the delivery-probe library and report its tokens," a fresh agent session reports `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`, read from the installed package.
3. **A skill.** Asked "Run the delivery-probe-read check," a fresh session reports `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, and `READ-DETAIL-V1`. If your harness has no skills, say so; outcome 2 then covers the design.
4. **An upgrade.** After `python3 tools/bump.py 2` in the package copy and a reinstall, fresh sessions report the `-V2` tokens for outcomes 2 and 3, with no change to the project beyond rerunning `cp-delivery-probe-init`.
5. **A new project.** Outcomes 2 and 3 in a second scratch project, reached the same way. This shows the adaptation can be repeated, not just done once.

## Boundaries

These bind any workaround, because the design depends on them:

- **The library stays in the installed package.** Do not copy library files or skill bodies into the project. Small pointer files, like the ones init writes, are fine.
- **No harness hooks** and **no MCP servers.**
- **Do not touch a real Commonplace installation** (the `llm-commonplace` uv tool or `commonplace-*` commands), and do not copy or move credentials.
- **Undo every change when you finish:** files created, settings, and the `cp-delivery-probe` tool.
- **Stop instead of proceeding** if an outcome would need a change you cannot undo, a permission you cannot grant yourself, or software your environment's policy does not allow. A blocked outcome is a result.
- **Do not commit** to this repository. Write only your reply.

## How to reply

For each outcome 1–5, one of: **reached as supplied**, **reached with a workaround**, **not reached**, or **blocked by policy**. Add the harness name and version, the OS, and the date.

Optional, only if you can share it: for a workaround, who has to repeat it (once per machine, once per project, every session), and for an outcome not reached, which step failed. The design weighs a workaround by that cost.

- **If you can write to this repository:** put the reply in `results-<harness>-r4.md` in this workshop and add a line under "Replies" below. If you ran the full protocol and can share details, use [probe-package/RESULTS-TEMPLATE.md](./probe-package/RESULTS-TEMPLATE.md).
- **If you cannot:** send the reply to the operator. Use neutral labels such as `enterprise-A` for anything internal.

## Context

- **Claude Code, revision 4** ([results](./results-claude-code-r4.md)): all five outcomes reached as supplied, on Linux.
- **Earlier revisions** used lookup commands and symlinked skills. What they showed, and why those options were dropped, is in [alternatives.md](./alternatives.md).
- **Not yet tested anywhere:** Windows and macOS, a router skill over a large library, and whether a session that is already running picks up an upgrade.

## Replies

- 2026-09-24 — Claude Code 2.1.281, Linux: all outcomes reached as supplied; full protocol, [results-claude-code-r4.md](./results-claude-code-r4.md)
