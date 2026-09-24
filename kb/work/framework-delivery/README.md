# Framework delivery

## Commission

Posed by the operator on 2026-09-23. Decide how Commonplace delivers what agents read — the framework library, global types, review gates, and skills — to installed projects. On 2026-09-24, at the operator's direction, the proposal `library-served-from-the-installed-package` was moved into this workshop as [design.md](./design.md) and removed from `kb/reference/proposals/`, so the design is kept in one place while it changes.

## Problem

Today `commonplace-init` copies the library and the skills into every project. The copy causes two problems:

- **Confusion.** Users cannot tell framework files from their own.
- **Divergence.** The copy is never refreshed after the first init, so after an upgrade the commands run new code against old gates and types. Each project sits at its own version.

## Operator direction and constraints

- **Copy GBrain by default** (2026-09-23). GBrain is Commonplace's dominant competitor. Depart from a GBrain method only for a Commonplace-specific reason, and record the reason.
- **One tree, one channel** (2026-09-24). The uv-installed package is the only tree that commands, agents, and harnesses read. There is no separate plugin tree and no per-project copy. uv is the only release channel. A derived copy is allowed only where a platform cannot read the package in place (Windows is the known case), and it must carry a version stamp and a hash check. This departs from GBrain, whose CLI and plugins install through separate channels and can skew.
- **No hooks** (2026-09-24). No harness hooks until hooks are standardised. At least one enterprise user runs their own harness.
- **Harness-neutral base** (2026-09-24). The design rests on files, a shell, the `commonplace-*` commands, and a project `AGENTS.md`. Agent Skills and harness plugins are optional layers above that base. The base must still let an agent find a library instruction that the user names in conversation, outside any skill.

## Design

The design, and the alternatives rejected so far, are in [design.md](./design.md). Its core is a proposed change to the install procedure: `commonplace-init` stops copying the library, and a per-user setup command links the skills and writes the harness permissions. Keep the design only there; this README holds the commission, constraints, and open questions.

## Open questions

- **The enterprise harness.** Does it read `AGENTS.md` or another instruction file? Can the agent run shell commands? Can it read files outside the project? Does it support Agent Skills, and from which directories? The operator is asked; the base layer assumes the first three. If it is built on Codex's app-server, `skills/extraRoots/set` may let it discover the package's skills in place with no links; Codex observed discovery only.
- **The router skill at scale.** It worked with a three-entry index in Codex. Does it still select the right instruction with an index the size of the real library?
- **The source checkout.** In the source repo the library is `kb/` itself and `.claude/skills/` holds symlinks into `kb/instructions/`. Do the commands and skills behave the same there? The editable install resolved the library into the source tree in both dry runs.
- **Skill names.** A `.claude-plugin/plugin.json` in the tree makes Codex prefix skill names (`cp-delivery-probe:delivery-probe-read`), even for plain symlinks. Documentation and invocation guidance must not assume the bare name.
- **Windows and macOS.** Not tested. On Windows, link mode is unsupported and symlinks are unreliable. Are directory junctions usable, or is the version-stamped copy needed?
- **Plugin approval.** In the operator's terminal the interactive prompt offered only "abort"; `--accept-command <sha256>` worked. The cause is unknown, and setup documentation depends on it. The Claude Code rerun's case 6 is pending on this.
- **Running sessions.** A running Claude Code session listed skills linked after it started. An upgrade inside a running session was not tested in either harness.
- **Centrally managed settings.** Claude Code needs user-level permission entries. Can setup write them where settings are managed centrally, or must it print them?

## Next steps

1. Finish the Claude Code rerun's case 6 (the link-mode plugin served from a real `share/` install) and its cleanup.
2. Agents in other harnesses run the shared probe, as requested in [harness-probe-request.md](./harness-probe-request.md): Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, and enterprise harnesses. Enterprise results may come back through the operator, anonymised.
3. Update [design.md](./design.md) from their results.

## Evaluation boundary

- Harnesses: Claude Code and Codex, plus the base layer in any harness that meets its stated assumptions.
- Operating systems: Linux, macOS, and Windows.
- Places: the source checkout and an installed project.
- Upgrade cases: an upgrade that changes a skill, one that changes only library files, and one that moves the install location.

## Coupling

- [agent-operability-second-slice](../agent-operability-second-slice/README.md) builds install baselines and a three-way upgrade plan for copied framework files. Without the library copy, its subject shrinks to whatever copies remain. Coordinate before either side ships.
- [system-contract-consistency](../system-contract-consistency/README.md) holds findings I1 (shipping and upgrade contracts disagree) and I2 (the install projection breaks library links). Both change meaning once the library stops being copied.

## Closure

Close when the operator decides the design: an adopted design becomes an ADR and an `INSTALL.md` change; a design left undecided goes back to `kb/reference/proposals/` as a proposal. Before closing, each open question is answered or deferred with a trigger, and each departure from GBrain has a recorded reason. Then delete this directory and its entry in `kb/work/README.md`.

## Working files

- [design.md](./design.md) — the design, including the proposed install procedure; the only place it is kept
- [comparable-systems-survey.md](./comparable-systems-survey.md) — how harnesses and 14 comparable systems deliver skills and libraries, from web research and the local clones
- [gbrain-delivery-methods.md](./gbrain-delivery-methods.md) — code-grounded study of GBrain v0.54.1.0's delivery methods and what carries over to a Python/uv package
- [probe-results.md](./probe-results.md) — 2026-09-24 probes: a Claude Code link-mode plugin served in place from a package directory, and a Codex skill symlinked into it
- [probe-package/](./probe-package/PROTOCOL.md) — the shared probe: a throwaway uv package whose data is the plugin-shaped tree, commands for the base layer, a test project, the protocol every harness runs, and a results template. Testers modify a copy and record the modifications
- [codex-probe-request.md](./codex-probe-request.md) — request to a Codex agent to run the shared probe; Codex appends its reply here
- [harness-probe-request.md](./harness-probe-request.md) — request to agents in other harnesses, including enterprise ones, to run the shared probe (revision 3)
- [results-codex.md](./results-codex.md) — Codex's run of the shared probe (2026-09-24), with supplemental findings from its first fixture
- [results-claude-code.md](./results-claude-code.md) — Claude Code's run of the shared probe (2026-09-24); case 6 pending
- `results-<harness>.md` — one results file per further harness, from the template
