# Rejected alternatives

The options considered for delivering the library and skills, and why each was rejected. [design.md](./design.md) describes only the chosen design. Keep this file so a rejected option is not reopened without new evidence. Each entry names what would make it worth reconsidering, where something would.

## Where the library lives

- **A hidden, gitignored copy in the project.** It keeps the divergence between the copy and the installed code. A variant that regenerates the copy when versions differ narrows the divergence to the window after an upgrade, and it silently discards edits to the copy.
- **A symlink or junction at `kb/commonplace`.** It keeps the library in the project's view, and symlinks and junctions are unreliable on Windows.
- **Package data under `site-packages`.** Its path changes with the tool's Python version. In Codex, linked skills then dangled and were dropped without a warning ([results-codex.md](./results-codex.md), revision 2). Under the chosen design it would also invalidate the read rule, the stubs, and `library.md` on every Python change. Wheel shared data under `share/` keeps one path ([probe-results.md](./probe-results.md), uv section).

## How harnesses find skills

- **Full skill copies in the project.** They go stale on every upgrade that changes a skill, and their relative links into the library point nowhere, so each skill would have to look up library files through commands.
- **Symlinks from a skill directory into the package** (rejected by the operator, 2026-09-24). They avoid any copy and followed upgrades at once in both harnesses ([results-claude-code.md](./results-claude-code.md), [results-codex.md](./results-codex.md)). Symlinks are unreliable on Windows, and the operator ruled out platform-specific install paths: if one platform needs copies, every platform copies. The probes also found that agents in Codex resolved relative links against the symlink's location, not the target's.
- **A per-user setup command writing user-level skills and settings** (rejected by the operator, 2026-09-24). It saves one init run per project after some upgrades, but the skills would load in every project on the machine, including projects that do not use Commonplace, and it adds a second install command with its own scope.
- **Stubs that find their skill through a lookup command.** They avoid a machine-specific path, but add a command call and a Claude Code permission rule to every skill use. Stubs are not committed anyway, so the machine-specific path costs nothing.
- **Skill paths compiled at install** (init rewrites library references inside skills to absolute paths). Stubs give the same result with one absolute path per skill and no rewrite of skill text.

## How agents find the library outside a skill

- **Lookup commands** (`commonplace-library` to print the root, `commonplace-instruction <name>` to print an instruction's path). They worked in both harnesses (revisions 2 and 3), but they cost a command call per session, need a shell, and in Claude Code need a permission rule per command ([results-claude-code.md](./results-claude-code.md), cases 1–2). The generated `library.md` costs the same read or less and needs neither.
- **The library path written into `AGENTS.md`.** It saves one read, but `AGENTS.md` is committed and the path differs per machine, so every teammate's init would rewrite a committed file.
- **A relative-link fallback in skills** (revisions 2 and 3: commands first, relative links if commands fail). After a switch to an editable install, a Claude Code agent denied the source tree followed the fallback into the stale `share/` snapshot and reported the old version ([results-claude-code.md](./results-claude-code.md), case 7). Under the chosen design, relative links are the only route and resolve from the real skill's location, which init keeps current.

## Harness plugins

- **A plugin tree published separately from the package** (GBrain's route). It breaks the one-tree constraint: the CLI and the plugins install through separate channels and can skew.
- **Codex plugins from a local marketplace.** Codex copies them into its cache, which then goes stale on a uv upgrade ([results-codex.md](./results-codex.md), case 6).
- **A Claude Code link-mode plugin** (dropped 2026-09-24). Its marketplace entry runs a command that prints the package directory, and Claude Code links that directory into its cache instead of copying it ([probe-results.md](./probe-results.md)). Its one advantage over skills in the project, relinking by itself after the install moves, is lost because init must rerun after a move anyway. It costs a manual approval by each user in their own terminal, prefixed skill names, and a second route to document and check, and link mode does not work on Windows. Reconsider it if Commonplace ships something that must be a plugin component.

## Mechanisms ruled out by constraints

- **Hooks,** including a session-start hook that prints the library root. Ruled out until hooks are standardised; at least one enterprise user runs their own harness.
- **Instructions served over MCP,** including GBrain's `get_skill`. It needs an MCP server, clients handle MCP instructions unreliably, and tool schemas cost context ([comparable-systems-survey.md](./comparable-systems-survey.md)).

## Smaller choices

- **`permissions.additionalDirectories` instead of a `Read` rule** for Claude Code. Both removed the read denials ([results-claude-code.md](./results-claude-code.md), case 2). The `Read` rule is read-only; `additionalDirectories` adds the directory to the workspace. A `Read` rule also covers Grep and Glob per Claude Code's documentation; that was not probed.
- **A reserved `kb/types/` prefix for global types.** It would look like a path but name no file in a project, so an agent that opened it would find nothing. Bare names were chosen instead.
- **One stub for the whole library instead of one per skill.** Skills would no longer trigger on their own descriptions, and invocation by skill name would be lost.
- **Making commands fail instead of warn on stale init outputs.** A stale read can happen before any command runs, so failing would not close the gap; detection stays at command time, with the developer procedure to rerun init after a switch (review by a Codex agent, 2026-09-24).
- **Banning project-owned shared types.** The earlier proposal required a project to copy such a type into each collection. That is a product restriction, not a consequence of package delivery, and the [types note](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) allows global types whose structure is reusable across collections. Projects keep path-form pointers such as `kb/types/my-type.md` (same review).
- **Committable stubs with a `~/…` path.** The uv tool directory differs on Windows and with a custom `UV_TOOL_DIR`, so this would bring back platform differences.

## Evidence by probe revision

| Revision | What it tested | Results |
|---|---|---|
| Early probes | Claude Code link-mode plugin with a stand-in directory; a Codex skill symlink; uv shared data | [probe-results.md](./probe-results.md) |
| 1–2 | Symlinked skills with relative links, then commands first; package data under `site-packages` | [results-codex.md](./results-codex.md) |
| 3 | Shared data under `share/`; user-level symlinked skills; lookup commands | [results-codex.md](./results-codex.md), [results-claude-code.md](./results-claude-code.md) |
| 4 | The chosen design: per-project stubs, generated `library.md`, one read rule | [results-claude-code-r4.md](./results-claude-code-r4.md) |
