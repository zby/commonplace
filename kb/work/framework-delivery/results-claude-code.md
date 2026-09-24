# Delivery probe results: Claude Code

- Harness and version: Claude Code 2.1.281, fresh headless sessions (`claude -p --permission-mode default --output-format stream-json`)
- Model: claude-opus-5-5 (1M context), the configured default; no override
- Operating system: Linux (Ubuntu 24.04, x86_64)
- uv and Python versions: uv 0.12.17; Python 3.12.8 and 3.13.1
- Tester (agent or person) and date: Claude Code agent (Opus 5.5), 2026-09-24, at the operator's request
- Probe package revision (see PROTOCOL.md): revision 3, at checkout HEAD `154ef280`. `pyproject.toml` and `cli.py` hashes matched the ones Codex recorded for revision 3.

**Result.** With user-level permission rules in place, every case that could run in an agent session passed. Without them, the base layer fails in `default` mode: the lookup commands and the library read are both denied. After a switch to an editable install, the read rule no longer covered the library root. In one run the denied agent then read the stale `share/` snapshot through the skill's relative link.

**Earlier aborted run.** An earlier Claude Code session started this probe at 15:34 the same day and was stopped by the operator for unrelated file edits. Its evidence was not used. Its leftovers were undone before this run: the uv tool, a local marketplace, and three permission entries plus a marketplace entry in `~/.claude/settings.json`. The settings file was restored to that session's backup, whose SHA-256 matched.

## Harness facts

- Instruction file it loads: `CLAUDE.md`. The test project's `CLAUDE.md` imports `AGENTS.md` with `@AGENTS.md`, and the agent followed it. The user-level `~/.claude/CLAUDE.md` also loads in every session.
- Can the agent run shell commands? Yes, but in `default` mode each command must match an allow rule or be approved. Headless sessions cannot approve, so an unmatched command is denied.
- Can the agent read files outside the project, and under what setting? Only with a `Read(//<path>/**)` allow rule or a `permissions.additionalDirectories` entry covering the path. Either one works from user-level `~/.claude/settings.json`, which covers every project. A `cat` of the same file through Bash was also blocked.
- Agent Skills support and skill directories: user-level `~/.claude/skills/`, project-level `.claude/skills/`, and plugins.
- Does it follow symlinked skill directories? Yes. Skills are listed under their bare names (`delivery-probe-read`), even though the tree contains `.claude-plugin/plugin.json`. Codex prefixed the same links.
- Plugin or extension mechanism: marketplace plugins, which are copied into a cache by default. A command-source entry in link mode serves a directory in place (see `probe-results.md`). The command must be accepted by the user outside the agent session.

## Cases

Every model case ran in a fresh session with the protocol's prompt. Logs are summarised here; the raw stream-JSON logs were in the scratchpad and were removed at cleanup.

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install | Pass | Python 3.12 install. `cp-delivery-probe-library` printed `~/.local/share/uv/tools/cp-delivery-probe/share/cp-delivery-probe/library`. All four commands were on `PATH`. | — |
| 1 Base layer | Fail with no permission rules | The agent ran the instruction command four ways (combined, separately, and `command -v`). Every call was denied. It reported no tokens and said why. | 4 Bash denials |
| 2 Read permission | Pass with two rules | Allowing only the two commands: the command ran, then the Read of the printed file was denied. Commands + `Read(//…/share/cp-delivery-probe/**)`: `RETIRE-WIDGET-V1`, `SHARED-STEP-V1`, no denials. Commands + `additionalDirectories` for the same directory: same result. The same rules in user-level settings: same result. | none with both rules |
| 3 Skills (link) | Pass | `install-skills ~/.claude/skills --mode link`. The session listed both skills, loaded `delivery-probe-read`, used both commands, and read `SHARED-STEP-V1` and `PROBE-NOTE-TYPE-V1` from `share/`. No relative-link use. | none |
| 3 Skills (copy) | Not run | The link case passed. | — |
| 4 Router skill | Pass | In a project with no `AGENTS.md` or `CLAUDE.md`, the prompt selected `delivery-probe-library` without naming it. The agent used the instruction command and reported `CALIBRATE-GADGET-V1`. | none |
| 5 Upgrade, same Python | Pass | Bump to V2 and reinstall on 3.12. Links still `ok`. Fresh base and skill sessions reported V2 tokens. | none |
| 5 Upgrade, Python change | Pass without repair | Reinstall of V2 on 3.13. Link targets were unchanged, `--check` reported `ok`, and the commands printed no warning. A fresh skill session reported V2. | none |
| 6 Harness plugin | Pending | The marketplace was added. The install, run from the agent session, refused with `command_source_refused` and printed the command hash `225e4796…9c66d0`. It needs the operator's terminal. | — |
| 7 Editable install | Fail before repair; pass after | Editable install of V2: the commands pointed at the source tree and warned `elsewhere` for both links. The Read rule did not cover the source tree. **Run 1 (V2 in both trees):** the Read of the source file and a `cat` were denied. The agent then loaded the router skill, resolved its real path into `share/`, followed the relative link, and read the `share/` snapshot. It reported V2, which was correct only because the two trees matched. **Run 2 (source bumped to V3, `share/` still V2):** the same denials, then the agent stopped without tokens. **After repair** (`install-skills` repointed both links, plus a Read rule for the source tree): fresh base and skill sessions reported V3 from the source tree. | Run 1: 3 denials. Run 2: 3 denials. After repair: none |
| 7 Return to normal | Pass, with expected repair | Normal reinstall of V3 on 3.13. The commands warned `elsewhere`. One `install-skills` call restored the `share/` targets. A fresh skill session reported V3 from `share/`. | none |
| Extra: dangling link | Silent drop | A symlink `~/.claude/skills/delivery-probe-dangling` to a missing directory. The session's skill list omitted it, and nothing was written to stderr. | — |
| Extra: running session | Observed once | This tester's own interactive session, started before case 3, listed the two probe skills in a system message right after `install-skills` linked them. Content read through a link is read at invocation, so an upgrade at the same path would also be seen. Upgrading while a session runs was not tested separately. | — |

## Modifications to the package

None. In the scratch copy, only the supplied `tools/bump.py` changed files: to V2 for case 5, then to V3 after the editable install.

## Consequences for the design

- **Observed:** in Claude Code, the base layer needs two user-level permission entries: Bash allow rules for the lookup commands, and read access to the library root. Setup has to write them. In Codex it needs neither.
- **Observed:** the read entry names a concrete path. It survived the upgrade and the Python change, because the `share/` path did not move. It did not cover the root after a switch to an editable install.
- **Observed once:** a denied agent reached a stale copy through a skill's relative link. **Inferred:** skills should not keep the relative-link fallback. Setup should repair the permission entry and the skill links in one call, and the checks should report an uncovered root.
- **Observed:** Claude Code drops a dangling skill silently, as Codex does. The lookup commands' warnings are the only signal.
- **Observed:** Claude Code lists linked skills under bare names; Codex prefixes them. Guidance must not assume either form.

## Cleanup

Pending until case 6 finishes. To be undone: the `cp-delivery-probe` uv tool, the two skill links (already removed before case 6), the `cp-delivery-probe-market` marketplace and plugin, and the `permissions` block added to `~/.claude/settings.json`. The pre-run settings file is backed up in the scratchpad and will be restored and verified by hash. No hooks were used, no credentials were touched, and the real `llm-commonplace` installation was not changed.
