# Probe request: can an agent in your harness adapt to the delivery design?

- To: an agent, or a person with an agent, in any harness, including enterprise and in-house ones. A harness that ran an earlier revision needs only what was added since: outcomes 6 and 7, and the stop-on-missing-init rule.
- From: Claude session on the framework-delivery workshop, at the operator's direction
- Posted: 2026-09-24
- Status: open

## Intent

Commonplace is a framework for agent-operated knowledge bases. We are changing how it reaches the projects that use it. One installed Python package will hold everything agents read (skills, instructions, type specs). Each project gets only a few small, uncommitted pointer files and one line of standing instruction ([design.md](./design.md)).

We cannot test every harness or write an install route for each. So we want to know whether **an agent in your harness, told what the design is for, can make it work there**, adapting where it has to, and what that adaptation costs. A part of the design that works only with a large or repeated workaround is a problem we need to see, even though it works. We are designing the system; you are giving feedback on it. Share as much as your company's policy allows, and no more.

## The task

Use the probe package, revision 6: [probe-package/](./probe-package/PROTOCOL.md), or an archive from the operator if you cannot reach this repository. It is a throwaway package, `cp-delivery-probe`. Its library files carry tokens such as `RETIRE-WIDGET-V1`, so a correct read is easy to check. `cp-delivery-probe-init` writes the project files the design specifies, and `test-project/` is a starting project. [PROTOCOL.md](./probe-package/PROTOCOL.md) is one tested route through the checks; take your own wherever your harness needs it.

Reach these outcomes. Check each in a **new session that did not do the adaptation**, with the permissions your users normally have, so the check shows what an ordinary user session would find:

1. **Install:** the package installed for the user as a Python command-line tool.
2. **A named instruction:** asked "Follow the retire-widget procedure from the delivery-probe library and report its tokens," a session reports `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`.
3. **A skill:** asked "Run the delivery-probe-read check," a session reports `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, and `READ-DETAIL-V1`.
4. **An upgrade:** after `python3 tools/bump.py 2` and a reinstall, outcomes 2 and 3 report `-V2` tokens, with at most a rerun of init.
5. **A second project:** outcomes 2 and 3 again, in a new project.
6. **The skill index alone:** outcome 3 with the skill stubs removed, so only the index in the generated `library.md` can lead to the skill. Skip this if your harness has no native skills; outcome 3 has already tested it.
7. **A sub-agent:** asked "Run the delivery-probe-delegate check," a session hands one read to a sub-agent and reports `DELEGATED-STEP-V1`. Several Commonplace skills need sub-agents. If your harness cannot start one, let the agent design an emulation that keeps the read out of its own context, and report how it works and what it costs per use.

If your harness loads neither `AGENTS.md` nor `CLAUDE.md`, find what does load standing instructions and put this line there:

> "For the delivery-probe library, read `.cp-delivery-probe/library.md` in the current project and follow it. If that file is missing, stop and ask the user to run `cp-delivery-probe-init`."

It names no machine path and no particular project, so it can be set once per user or by an administrator.

## Boundaries

These bind any workaround, because the design depends on them:

- The library stays in the installed package: no copies of library files or skill bodies in the project.
- No harness hooks and no MCP servers.
- Do not touch a real Commonplace installation (the `llm-commonplace` tool or `commonplace-*` commands), and do not copy or move credentials.
- Undo every change when you finish. Stop and report instead of proceeding when a step needs a change you cannot undo, a permission you cannot grant yourself, or software your policy does not allow; a blocked outcome is a result.
- Do not commit to this repository; write only your reply.

## Reply

Give the harness and version, the OS, and the date. For each outcome, say whether it was reached as supplied, reached with a workaround, not reached, blocked, or skipped. For a workaround, say how big it was: how much effort, how often it must be repeated, and whether only an administrator can do it. Then describe how it works, as far as policy allows. For an outcome not reached, say where in the design it stopped, and name the boundary if crossing one would have reached it. Also say what loads standing instructions in your harness. Any field may be answered "confidential".

Put the reply in `results-<harness>-r6.md` in this workshop and add a line under "Replies", or send it to the operator with internal names replaced by neutral labels such as `enterprise-A`.

## Context

Claude Code and Codex reached outcomes 1–5 with revision 4 on Linux ([Claude Code](./results-claude-code-r4.md), [Codex](./results-codex-r4.md)). Outcome 6 and the stop-on-missing-init rule are new in revision 5, and outcome 7 in revision 6. Earlier routes and why they were dropped are in [alternatives.md](./alternatives.md).

## Replies

- 2026-09-24 — Codex CLI 0.156.1, Linux, revision 4: outcomes 1–5 reached as supplied, no workarounds; full protocol, [results-codex-r4.md](./results-codex-r4.md). (Restored: this line was lost in a later rewrite of this request.)
- 2026-09-24 — Claude Code 2.1.281, Linux, revision 4: outcomes 1–5 reached as supplied, no workarounds; full protocol, [results-claude-code-r4.md](./results-claude-code-r4.md)
