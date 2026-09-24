# Delivery probe protocol

A shared test for every harness. Each tester starts from this package, runs the same cases, and records the results in the workshop. The goal is to learn whether the framework-delivery design (see `../design.md`) works in your harness, and what it would take to make it work.

## Rules

- **Start from the same code.** Copy `probe-package/` to a scratch location and work on the copy. Do not edit the package in the workshop.
- **Modify the copy when your harness needs it.** Record every modification in your results file: what you changed, why the harness needed it, and the diff or an exact description. A modification that makes a case pass is a finding, not a workaround to hide.
- **Do not use harness hooks.** The design must not depend on them until hooks are standardised.
- **Do not touch any real Commonplace installation**, its commands, or credentials.
- **Undo everything afterwards:** uninstall the tool, and remove the stubs and any permission entry you added.
- **Separate observation from inference** in your results. Say which harness and model version ran each case.

## The package

`cp-delivery-probe` is a normal Python package. Its `library/` directory is the only tree, laid out like a KB: `instructions/` and `types/`, with each skill in its own directory under `instructions/`. The wheel installs it as shared data under `<tool environment>/share/cp-delivery-probe/`, a path without a Python version in it. An editable install reads it from the source tree instead.

- `instructions/*.md` and `types/*.md` each carry a token such as `RETIRE-WIDGET-V1`. An agent that followed the file reports the token.
- `instructions/delivery-probe-read/` is a skill. It reaches a library instruction (`../shared-step.md`), a type (`../../types/probe-note.md`), and a file in its own directory (`./references/read-detail.md`) by ordinary relative links. It calls no command.
- `instructions/delivery-probe-library/` is a router skill. Its description says to use it when a delivery-probe procedure is named, and its body links each library entry.

Harnesses discover skills only in their own skill directories. `cp-delivery-probe-install-skills <dir>` writes a **stub** there for each skill: a `SKILL.md` with the real skill's frontmatter and one instruction, to read the real `SKILL.md` at its absolute path and follow it. The real skill then runs in place.

| Command | Does |
|---|---|
| `cp-delivery-probe-library` | prints the library root |
| `cp-delivery-probe-instruction [name]` | prints one instruction's path, or lists the names |
| `cp-delivery-probe-install-skills <dir> [--remove \| --check]` | writes the stubs into a skill directory, removes them, or reports each as `ok`, `stale`, `missing`, `foreign`, or `extra`. Writing is idempotent: it replaces its own stubs, removes stubs for skills the package no longer has, and leaves anything else alone |

The first two commands also warn on stderr when a stub in `./.claude/skills` or `./.agents/skills` (relative to the current directory), or in a directory listed in `CP_DELIVERY_PROBE_SKILL_DIRS`, is stale or extra. A stub is stale when its content differs from what `install-skills` would write now: the real skill moved, or its frontmatter changed.

`tools/bump.py <n>` bumps the version and every token to `-V<n>`, for the upgrade cases. `test-project/` holds an `AGENTS.md` (with a `CLAUDE.md` importing it) that tells an agent how to find the library without skills.

## Cases

Use a fresh agent session for each case. Copy `test-project/` to a scratch directory and start sessions there. Stubs go into that project's skill directory, not a user-level one. Record the prompt you used if it differs from the one given.

0. **Install.** `uv tool install --python 3.12 <copy>`. Record the output of `cp-delivery-probe-library` and check that it is on `PATH` for your harness.
1. **Base layer, no skills.** Ask: "Follow the retire-widget procedure from the delivery-probe library and report its tokens." Pass: `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. Record how the agent found the file, and every permission prompt or denial.
2. **Read permission.** If case 1 needed approval, record the least setting that removes it. Where the harness allows it, put the setting in the project's own settings, and record whether a part that names the library path can stay out of committed files.
3. **Stub skill.** Run `cp-delivery-probe-install-skills <project skill dir>` in the test project. Ask: "Run the delivery-probe-read check." Pass: `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, and `READ-DETAIL-V1`, all read from the installed library. Record whether the agent read the real `SKILL.md`, how it resolved each relative link, and any failed read before success. **Run this case three times**, each in a fresh session; stub-following is the main question.
4. **Router through a stub.** In a second project without `AGENTS.md`, install the stubs. Ask: "Calibrate the gadget using the delivery-probe procedure." Do not name the skill. Pass: the agent loads `delivery-probe-library`, follows it to the real skill, and reports `CALIBRATE-GADGET-V1`.
5. **Upgrade.**
   - a. Run `python3 tools/bump.py 2` in your copy, then `uv tool install --python 3.12 --reinstall <copy>`. Without rerunning `install-skills`, check that `--check` reports `ok`, and repeat case 3 once. Pass: `-V2` tokens.
   - b. Change `delivery-probe-read`'s description in your copy (for example, append " Version two."), then reinstall. `--check` should report that stub `stale`, and the lookup commands should warn. Rerun `install-skills` and check again.
   - c. Reinstall with `--python 3.13`. `--check` should still report `ok`, and a fresh session should still find the skills.
6. **Editable install.** `uv tool install --editable <copy>` (with `--reinstall` if needed). The stubs still point into `share/`, so `--check` should report them `stale`. Record what a fresh case 3 session does before the repair. Then rerun `install-skills`, run `python3 tools/bump.py 3` without reinstalling, and repeat case 3. Pass: `-V3` tokens read from the source tree. Finish with a normal reinstall and one more `install-skills`.
7. **Skill names.** Record the names under which the harness lists the stubs, from case 3.

## Package revisions

- **Revision 1** (commit `90e0ef8a`): skills relied on relative links; `install-skills` refused existing entries. Codex ran this revision.
- **Revision 2**: skills and router used the commands first, because agents in Codex misresolved relative links through the skill symlinks. `install-skills` became idempotent and gained `--check`.
- **Revision 3**: the plugin tree moved from package data to wheel shared data, whose path does not change with the Python version. Codex and Claude Code ran this revision ([Codex](../results-codex.md), [Claude Code](../results-claude-code.md)).
- **Revision 4** (2026-09-24): follows the design's decisions. Skills are delivered as per-project stubs that redirect to the real skill in the installed library, on every platform, with no symlinks. The tree mirrors a KB layout, so skills use ordinary relative links and call no command. The Claude Code plugin manifest, the marketplace, and the plugin-path command are gone, because the plugin layer was dropped.

Record the revision you started from in your results file.

## Known results before revision 4 (2026-09-24, Linux, uv)

- The shared-data path stayed the same across a Python 3.12→3.13 reinstall, in Codex and in Claude Code. An editable install reads the source tree; its shared data is a stale install-time snapshot.
- Codex needed no permission settings. Claude Code in `default` mode needed an allow rule for each lookup command and read access to the library root; both worked from user-level settings.
- An agent that read a library file at its real path followed the file's relative link correctly in both harnesses. Relative links failed only through symlinked skills in Codex.
- Both harnesses dropped a dangling symlinked skill without an error.
- Codex listed symlinked skills with a plugin-name prefix while the tree had a `.claude-plugin/plugin.json`; Claude Code listed bare names.

## Recording results

Copy `RESULTS-TEMPLATE.md` to `../results-<harness>.md` in the workshop and fill it in. One file per harness and revision; if the file exists, add a suffix such as `-r4`.
