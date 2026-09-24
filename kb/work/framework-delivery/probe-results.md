# Probe results

Run 2026-09-24 on Linux with Claude Code 2.1.281 and codex-cli 0.155.1. The fixture was a fake package directory laid out as a plugin: `.claude-plugin/plugin.json`, `skills/cp-probe/SKILL.md`, and `library/instructions/probe-target.md`. The skill links to the library file as `../../library/instructions/probe-target.md` and asks the agent to report a token from it. The fixture and the test plugin were removed afterwards.

## Claude Code: plugin served in place (link mode)

Setup: a local marketplace whose entry is `{"source": "command", "command": "<script>", "mode": "link"}`. The script prints the package's plugin directory, standing in for a command such as `commonplace-plugin-path`.

| Question | Result |
|---|---|
| Can an agent session accept the command? | No. `--yes` is ignored inside a Claude Code session, and the non-interactive install only displays the command. The operator accepted it from their own terminal with `--accept-command <sha256>`, taken from the `--json` run. The interactive prompt offered only "abort" in the operator's terminal; the cause was not established. |
| Is anything copied? | No. The cache entry `~/.claude/plugins/cache/<market>/<plugin>/<version>/` holds symlinks to the package's top-level entries (`skills`, `library`, `.claude-plugin`). Its version is `<plugin.json version>-<hash of the printed path>`. |
| Does the skill load and resolve its relative link? | Yes. Claude resolved `../../library/...` against the skill's cache path, and the operating system followed the link into the package. |
| Can it read the library file without a prompt? | Only if both locations are allowed. With neither allowed, the read needed permission. Allowing only `~/.claude/plugins/cache` was not enough, because permission checks follow the link to its target. Allowing the cache and the package directory (`--add-dir`, standing in for `permissions.additionalDirectories`) let it read without any prompt. |
| Does it follow a moved package? | Yes. After the printed path changed, the per-session background re-run created a new cache version linked to the new path, and `installed_plugins.json` switched `installPath` to it, recording the old path under `previousProducerPaths`. Content changed inside an unchanged path needs no re-run, because the entries are links. |

Consequences for the design:

- Setup must add the package's install directory to Claude Code's read permissions. Allowing only the plugin cache does not work.
- Each user must accept the path command once, in their own terminal or the `/plugin` screen. `commonplace-init` run by an agent cannot accept it.
- An upgrade at an unchanged install path is seen immediately. A moved install path is seen after one session's background run.
- Not tested: Windows, where link mode is documented as unsupported.

## Codex: skill symlinked from the package

Setup: the scratch project's `.agents/skills/cp-probe` was a symlink to the package's skill directory. `codex exec -s read-only` was run in that project.

- Codex discovered the skill. It listed it as `cp-probe:cp-probe`; the reason for that name was not investigated.
- The agent's first attempt resolved the relative link against `.agents/` and failed. Its second attempt went through the skill's own path (`.agents/skills/cp-probe/../../library/...`). The operating system resolves `..` from the symlink's target, so that read the file inside the package and returned the correct token.
- No permission prompt appeared: the read-only sandbox allows reads outside the project.

Consequences: symlinks from a skill directory into the package work in Codex. Skills should state that links are relative to the skill's own directory. User-level `~/.agents/skills`, a real uv installation, and Codex's own plugin mechanism were not tested.

## uv: a Python-independent install path (2026-09-24)

A minimal hatchling package installed files through `[tool.hatch.build.targets.wheel.shared-data]` (`"data" = "share/sdprobe"`), with uv 0.12.17 on Linux, in an isolated `UV_TOOL_DIR`.

- The files landed in `<uv tool dir>/sdprobe/share/sdprobe/`. That path has no Python version in it, unlike package data under `lib/python3.X/site-packages/`. The command found it as `Path(sys.prefix) / "share" / "sdprobe"`.
- After `uv tool install --python 3.13 --reinstall` with a new version, the path was unchanged. A symlink made before the change still resolved, and it showed the new content.
- Under `uv tool install --editable`, the shared-data files were an install-time snapshot: an edit to the source file did not appear in `share/`. Package data in an editable install resolves to the source tree (see results-codex.md, case 7), so for editable installs the commands should read the source tree.

Consequence: serving skills and library from shared-data instead of package data would keep skill links valid across Python changes. That would remove the dangling-link case that Codex drops silently. Not yet tested with a harness, on macOS or Windows, or with the Claude Code link-mode plugin (whose printed path would then be the `share/` directory).
