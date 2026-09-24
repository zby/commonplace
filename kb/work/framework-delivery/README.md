# Framework delivery

## Commission

Posed by the operator on 2026-09-23. Decide how Commonplace delivers what agents read — the framework library, global types, review gates, and skills — to installed projects. The selected design is written back into the [library-served-from-the-installed-package proposal](./design.md), which it will largely replace.

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

Three layers. Each works without the ones above it. Updated 2026-09-24 with the [Codex results](./results-codex.md).

1. **Base, for every harness.** The library, laid out as a plugin (skills, instructions, notes, reference, types, and gates), installs as wheel shared data under `<uv tool environment>/share/commonplace/`. That is the conventional place for a program's read-only data, and its path does not change with the tool's Python version. The `commonplace-*` commands read it there, or from the source tree in an editable install, where shared data would be an install-time snapshot. `commonplace-init` writes a project `AGENTS.md` naming two commands: `commonplace-library` prints the library root, and `commonplace-instruction <name>` prints the path of one instruction (or lists them). An agent asked for a named instruction runs the command and reads the file it prints. Setup grants the harness read access to the root where the harness needs it; Codex needed none. Project files never contain the library path, because it differs per machine and per uv tool directory.
2. **Skills, where the harness supports Agent Skills.** Setup links each `cp-skill-*` directory from the harness's user-level skill directory into the package. Skills find library files through the same commands as the base layer, by name. Relative links stay in the text as a convenience, not as the route a skill depends on: agents in Codex misresolved them against the symlink path before recovering. A router skill (`commonplace-library`) indexes the library by instruction name, so an agent asked for an instruction in conversation finds it through the skill's description.
3. **Harness-specific extras.** In Claude Code, a link-mode plugin serves the `share/commonplace/` tree in place: its path command prints that directory, Claude Code links its top-level entries, and nothing is copied. A moved tree is picked up after one session. The user must accept the path command once, in their own terminal, and Claude Code's read permissions must include the `share/commonplace/` directory itself. Link mode was probed with a stand-in directory, not yet with a real `share/` install. Codex has no equivalent that serves in place: its local-marketplace plugins are copied into its cache and go stale on a uv upgrade, so Codex uses layer 2 only.

**Keeping skill links valid.** With the tree under `share/`, upgrades and Python changes keep the path, so linked skills see new content at once. Codex confirmed this with revision 3: links made under Python 3.12 survived a reinstall on 3.13 without repair. (With package data, a Python change moved the path, and Codex silently dropped the dangling skills.) Links can still go wrong: after a switch between editable and normal installs, a changed uv tool directory, or an uninstall. Without hooks nothing can repair links when that happens, so the design detects and repairs them:

- Skill setup is idempotent. It replaces links that point into any Commonplace install location, and it leaves unrelated entries alone.
- The health check, and every `commonplace-*` command where the check is cheap, reports dangling or misdirected skill links and names the setup command that repairs them. In Codex's revision 3 run, both directions of the editable/normal switch were detected and repaired by one setup call.

Rejected so far, with reasons:

- A hidden, gitignored copy in the project: it keeps the divergence.
- A plugin tree published separately from the package (GBrain's route): the one-tree constraint.
- Hooks, including a session-start hook that prints the library root: the no-hooks constraint.
- Instructions served over MCP, including GBrain's `get_skill`: it needs an MCP server, clients handle MCP instructions unreliably, and tool schemas cost context (see the survey).
- Codex plugins from a local marketplace: Codex copies them into its cache, which breaks the one-tree constraint.
- Relative links as the route skills depend on: agents misresolve them through symlinks. A `readlink -f` instruction fixed that in Codex on Linux, but it is not portable, and the command route already works everywhere.

## Open questions

- **The enterprise harness.** Does it read `AGENTS.md` or another instruction file? Can the agent run shell commands? Can it read files outside the project? Does it support Agent Skills, and from which directories? The operator is asked; the base layer assumes the first three. If it is built on Codex's app-server, `skills/extraRoots/set` may let it discover the package's skills in place with no links; Codex observed discovery only.
- **The router skill at scale.** It worked with a three-entry index in Codex. Does it still select the right instruction with an index the size of the real library?
- **The source checkout.** In the source repo the library is `kb/` itself and `.claude/skills/` holds symlinks into `kb/instructions/`. Do the commands and skills behave the same there? The editable install resolved the library into the source tree in both dry runs.
- **Skill names.** A `.claude-plugin/plugin.json` in the tree makes Codex prefix skill names (`cp-delivery-probe:delivery-probe-read`), even for plain symlinks. Documentation and invocation guidance must not assume the bare name.
- **Windows and macOS.** Not tested. On Windows, link mode is unsupported and symlinks are unreliable. Are directory junctions usable, or is the version-stamped copy needed?
- **Plugin approval.** In the operator's terminal the interactive prompt offered only "abort"; `--accept-command <sha256>` worked. The cause is unknown, and setup documentation depends on it.
- **Running sessions.** Neither harness was tested for picking up an upgrade inside a session that was already running.

## Next steps

1. Agents in other harnesses run the shared probe, as requested in [harness-probe-request.md](./harness-probe-request.md): Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, a full Claude Code rerun, and enterprise harnesses. Enterprise results may come back through the operator, anonymised.
2. Update the working design from their results, then write the selected design back into the proposal.

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
- [probe-package/](./probe-package/PROTOCOL.md) — the shared probe: a throwaway uv package whose data is the plugin-shaped tree, commands for the base layer, a test project, the protocol every harness runs, and a results template. Testers modify a copy and record the modifications
- [codex-probe-request.md](./codex-probe-request.md) — request to a Codex agent to run the shared probe; Codex appends its reply here
- [harness-probe-request.md](./harness-probe-request.md) — request to agents in other harnesses, including enterprise ones, to run the shared probe (revision 3)
- [results-codex.md](./results-codex.md) — Codex's run of the shared probe (2026-09-24), with supplemental findings from its first fixture
- `results-<harness>.md` — one results file per further harness, from the template
