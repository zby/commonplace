# Framework delivery

## Commission

Posed by the operator on 2026-09-23. Decide how Commonplace delivers what agents read — the framework library, global types, review gates, and skills — to installed projects. The selected design is written back into the [library-served-from-the-installed-package proposal](../../reference/proposals/library-served-from-the-installed-package.md), which it will largely replace.

## Problem

Today `commonplace-init` copies the library and the skills into every project. The copy causes two problems:

- **Confusion.** Users cannot tell framework files from their own.
- **Divergence.** The copy is never refreshed after the first init, so after an upgrade the commands run new code against old gates and types. Each project sits at its own version.

## Operator direction and constraints

- **Copy GBrain by default** (2026-09-23). GBrain is Commonplace's dominant competitor. Depart from a GBrain method only for a Commonplace-specific reason, and record the reason.
- **One tree, one channel** (2026-09-24). The uv-installed package is the only tree that commands, agents, and harnesses read. There is no separate plugin tree and no per-project copy. uv is the only release channel. A derived copy is allowed only where a platform cannot read the package in place (Windows is the known case), and it must carry a version stamp and a hash check. This departs from GBrain, whose CLI and plugins install through separate channels and can skew.
- **No hooks** (2026-09-24). No harness hooks until hooks are standardised. At least one enterprise user runs their own harness.
- **Harness-neutral base** (2026-09-24). The design rests on files, a shell, the `commonplace-*` commands, and a project `AGENTS.md`. Agent Skills and harness plugins are optional layers above that base. The base must still let an agent find a library instruction that the user names in conversation, outside any skill.

## Working design

Three layers. Each works without the ones above it.

1. **Base, for every harness.** The package's data is the library, laid out as a plugin: skills, instructions, notes, reference, types, and gates, linked by relative paths. The `commonplace-*` commands read it as package data. `commonplace-init` writes a project `AGENTS.md` stating that `commonplace-library` prints the library root. An agent asked for a named instruction runs the command and reads under that root. Setup grants the harness read access to the root where the harness needs it.
2. **Skills, where the harness supports Agent Skills.** Setup links each `cp-skill-*` directory from the harness's skill directory into the package. A router skill (`commonplace-library`) carries a generated index of the library with relative links, so an agent that is asked for an instruction can find it through the skill's description.
3. **Harness-specific extras.** In Claude Code, a link-mode plugin serves the package in place. Nothing is copied, and a moved package is picked up after one session. The user must accept the plugin's path command once, in their own terminal.

Rejected so far, with reasons:

- A hidden, gitignored copy in the project: it keeps the divergence.
- A plugin tree published separately from the package (GBrain's route): the one-tree constraint.
- Hooks, including a session-start hook that prints the library root: the no-hooks constraint.
- Instructions served over MCP, including GBrain's `get_skill`: it needs an MCP server, clients handle MCP instructions unreliably, and tool schemas cost context (see the survey).

## Open questions

- **The enterprise harness.** Does it read `AGENTS.md` or another instruction file? Can the agent run shell commands? Can it read files outside the project? Does it support Agent Skills, and from which directories? The operator is asked; the base layer assumes the first three.
- **Codex with a real uv installation.** Where package data lives and whether the path survives upgrades and Python changes; user-level skill symlinks; broken links after a move; whether Codex plugins can be served in place. Requested from Codex in [codex-probe-request.md](./codex-probe-request.md).
- **The router skill.** Does its description make an agent load it when the user names an instruction in conversation, in Claude Code and in Codex?
- **The source checkout.** Do the same relative links work where `kb/` itself is the tree and `.claude/skills/` holds symlinks into `kb/instructions/`?
- **Windows.** Link mode is unsupported, and symlinks are unreliable. Are directory junctions usable, or is the version-stamped copy needed?
- **Plugin approval.** In the operator's terminal the interactive prompt offered only "abort"; `--accept-command <sha256>` worked. The cause is unknown, and setup documentation depends on it.

## Evaluation boundary

- Harnesses: Claude Code and Codex, plus the base layer in any harness that meets its stated assumptions.
- Operating systems: Linux, macOS, and Windows.
- Places: the source checkout and an installed project.
- Upgrade cases: an upgrade that changes a skill, one that changes only library files, and one that moves the install location.

## Coupling

- [agent-operability-second-slice](../agent-operability-second-slice/README.md) builds install baselines and a three-way upgrade plan for copied framework files. Without the library copy, its subject shrinks to whatever copies remain. Coordinate before either side ships.
- [system-contract-consistency](../system-contract-consistency/README.md) holds findings I1 (shipping and upgrade contracts disagree) and I2 (the install projection breaks library links). Both change meaning once the library stops being copied.

## Closure

Close when the working design, or its replacement, is written back into the proposal, each open question is answered or deferred with a trigger, and each departure from GBrain has a recorded reason. Then delete this directory and its entry in `kb/work/README.md`.

## Working files

- [comparable-systems-survey.md](./comparable-systems-survey.md) — how harnesses and 14 comparable systems deliver skills and libraries, from web research and the local clones
- [gbrain-delivery-methods.md](./gbrain-delivery-methods.md) — code-grounded study of GBrain v0.54.1.0's delivery methods and what carries over to a Python/uv package
- [probe-results.md](./probe-results.md) — 2026-09-24 probes: a Claude Code link-mode plugin served in place from a package directory, and a Codex skill symlinked into it
- [codex-probe-request.md](./codex-probe-request.md) — request to a Codex agent to repeat the probes with a real uv installation, including the router skill and the `AGENTS.md` fallback; Codex appends its reply here
- `codex-probe-results.md` — Codex's results (pending)
