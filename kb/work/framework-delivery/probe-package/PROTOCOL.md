# Delivery probe protocol

A shared test for every harness. Each tester starts from this package, runs the same cases, and records the results in the workshop. The goal is to learn whether the framework-delivery working design (see `../README.md`) works in your harness, and what it would take to make it work.

## Rules

- **Start from the same code.** Copy `probe-package/` to a scratch location and work on the copy. Do not edit the package in the workshop.
- **Modify the copy when your harness needs it.** Record every modification in your results file: what you changed, why the harness needed it, and the diff or an exact description. A modification that makes a case pass is a finding, not a workaround to hide.
- **Do not use harness hooks.** The design must not depend on them until hooks are standardised.
- **Do not touch any real Commonplace installation**, its commands, or credentials.
- **Undo everything afterwards:** uninstall the tool, remove the skills you installed, and remove any marketplace, plugin, or permission entry you added.
- **Separate observation from inference** in your results. Say which harness and model version ran each case.

## The package

`cp-delivery-probe` is a normal Python package. Its package data under `src/cp_delivery_probe/plugin/` is the only tree:

- `library/instructions/` and `library/types/`: Markdown files, each carrying a token such as `RETIRE-WIDGET-V1`. An agent that followed the file reports the token.
- `skills/delivery-probe-read/`: a skill that reads two library files. It finds them through the commands below, with relative links only as a fallback when commands cannot run.
- `skills/delivery-probe-library/`: a router skill. Its description says to use it when a delivery-probe procedure is named, and its body indexes the library by name, with the same command-first route.
- `.claude-plugin/plugin.json`: makes the same tree a Claude Code plugin.

Commands:

| Command | Prints |
|---|---|
| `cp-delivery-probe-library` | the library root |
| `cp-delivery-probe-instruction [name]` | one instruction's path, or the list of names |
| `cp-delivery-probe-plugin-path` | the plugin directory (for Claude Code's link mode) |
| `cp-delivery-probe-install-skills <dir> [--mode link\|copy] [--remove \| --check]` | installs the skills into a harness skill directory as links or marked copies, removes them, or reports their status. Installing is idempotent: it replaces entries the package manages (links into any install of it, or marked copies) and leaves anything else alone |

`cp-delivery-probe-library` and `cp-delivery-probe-instruction` also warn on stderr when an installed probe skill is dangling, points at another install, or is a stale copy. They check `~/.agents/skills`, `~/.claude/skills`, and any directories in `CP_DELIVERY_PROBE_SKILL_DIRS` (separated by the OS path separator). Set that variable if your harness uses another skill directory.

`tools/bump.py <n>` bumps the version and every token to `-V<n>`, for the upgrade cases. `test-project/` holds an `AGENTS.md` (with a `CLAUDE.md` importing it) that tells an agent how to find the library without skills. `claude-marketplace/` is a local Claude Code marketplace for case 6.

## Cases

Use a fresh agent session for each case unless the case says otherwise. Copy `test-project/` to a scratch directory and start sessions there. Record the prompt you used if it differs from the one given.

0. **Install.** `uv tool install --python 3.12 <copy>`. Record the output of `cp-delivery-probe-library` and check that it is on `PATH` for your harness.
1. **Base layer, no skills.** In the test project, ask: "Follow the retire-widget procedure from the delivery-probe library and report its tokens." Pass: `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. Record how the agent found the file, and every permission prompt or denial.
2. **Read permission.** If case 1 needed approval to read the library, record the least setting that removes it (a directory allow-list, sandbox mode, or similar), and whether a user-level setting can grant it once for all projects.
3. **Skills.** If your harness supports Agent Skills, run `cp-delivery-probe-install-skills <your harness's user-level skill dir>` (`--mode link` first). Ask: "Run the delivery-probe-read check." Pass: `SHARED-STEP-V1` and `PROBE-NOTE-TYPE-V1`, read from the installed package. Record whether the agent used the commands or the relative-link fallback, and any failed reads before success. If the harness does not discover linked skills, retry with `--mode copy` and record both outcomes.
4. **Router skill.** Keep the skills installed. In a fresh session in a project without `AGENTS.md`, ask: "Calibrate the gadget using the delivery-probe procedure." Do not name the skill. Pass: the agent loads `delivery-probe-library` and reports `CALIBRATE-GADGET-V1`.
5. **Upgrade.** Run `python3 tools/bump.py 2` in your copy, then `uv tool install --python 3.12 --reinstall <copy>`. Repeat cases 1 and 3 in new sessions. Pass: `-V2` tokens. Then reinstall with `--python 3.13`. The install path changes, so symlinked skills dangle. Record what the harness does with them: an error, a silent drop, or a stale copy. Run `cp-delivery-probe-library` and record whether its warning appears. Then run `install-skills <dir>` again, without `--remove`, and record whether a fresh session finds the skills again.
6. **Harness plugin (optional).** If your harness has a plugin or extension mechanism, record whether it can serve `cp-delivery-probe-plugin-path`'s directory in place or must copy it. For Claude Code, `claude plugin marketplace add <copy>/claude-marketplace`, then `claude plugin install cp-delivery-probe@cp-delivery-probe-market` from your own terminal. An agent session cannot accept the path command.
7. **Editable install (optional).** `uv tool install --editable <copy>` and repeat case 1. The library root is then the source tree.

## Package revisions

- **Revision 1** (commit `90e0ef8a`): skills relied on relative links; `install-skills` refused existing entries. Codex ran this revision ([results](../results-codex.md)).
- **Revision 2** (2026-09-24): skills and router use the commands first, because agents in Codex misresolved relative links through the skill symlinks. `install-skills` is idempotent and has `--check`. The lookup commands warn about dangling, misdirected, or stale skills, because Codex silently drops dangling skills.

Record the revision you started from in your results file.

## Known results (2026-09-24, Linux, uv)

- Package data installs under `<uv tool dir>/cp-delivery-probe/lib/python3.X/site-packages/cp_delivery_probe/plugin/`.
- A reinstall or `uv tool upgrade` at the same Python version keeps that path, and linked skills see the new content immediately.
- Changing the tool's Python version changes the path. Symlinked skills dangle until `install-skills` runs again; Codex drops them without an error.
- An editable install resolves the library to the source tree.
- Claude Code (see `../probe-results.md`) serves the plugin in place through link mode. Codex copies local-marketplace plugins into its cache.
- A copied skill's relative links point outside the package, so copies depend on the command route.

## Recording results

Copy `RESULTS-TEMPLATE.md` to `../results-<harness>.md` in the workshop and fill it in. One file per harness; if two testers use the same harness, add a suffix.
