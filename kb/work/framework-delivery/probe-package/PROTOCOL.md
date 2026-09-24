# Delivery probe protocol

A shared test for every harness. Each tester starts from this package, runs the same cases, and records the results in the workshop. The goal is to learn whether the framework-delivery design (see `../design.md`) works in your harness, and what it would take to make it work.

## Rules

- **Start from the same code.** Copy `probe-package/` to a scratch location and work on the copy. Do not edit the package in the workshop.
- **Modify the copy when your harness needs it.** Record every modification in your results file: what you changed, why the harness needed it, and the diff or an exact description. A modification that makes a case pass is a finding, not a workaround to hide.
- **Do not use harness hooks.** The design must not depend on them until hooks are standardised.
- **Do not touch any real Commonplace installation**, its commands, or credentials.
- **Undo everything afterwards:** run `cp-delivery-probe-init --remove` in each project, uninstall the tool, and remove any setting you added by hand.
- **Separate observation from inference** in your results. Say which harness and model version ran each case.

## The package

`cp-delivery-probe` is a normal Python package. Its `library/` directory is the only tree, laid out like a KB: `instructions/` and `types/`, with each skill in its own directory under `instructions/`. The wheel installs it as shared data under `<tool environment>/share/cp-delivery-probe/`, a path without a Python version in it. An editable install reads it from the source tree instead.

- `instructions/*.md` and `types/*.md` each carry a token such as `RETIRE-WIDGET-V1`. An agent that followed the file reports the token.
- `instructions/delivery-probe-read/` is a skill. It reaches a library instruction (`../shared-step.md`), a type (`../../types/probe-note.md`), and a file in its own directory (`./references/read-detail.md`) by ordinary relative links. It calls no command.
- `instructions/delivery-probe-library/` is a router skill. Its description says to use it when a delivery-probe procedure is named, and its body links each library entry.

Agents reach the library by reading files; no agent route runs a command. `cp-delivery-probe-init [project] [--check | --remove]` stands in for `commonplace-init` and writes three uncommitted, machine-specific outputs into a project:

- a **stub** per skill in `.claude/skills/` and `.agents/skills/`: a `SKILL.md` with the real skill's frontmatter and one instruction, to read the real `SKILL.md` at its absolute path and follow it;
- **`.cp-delivery-probe/library.md`**: the library root and entry points as full paths. The test project's `AGENTS.md` points to it, and its `CLAUDE.md` imports it with `@.cp-delivery-probe/library.md`;
- a Claude Code **read rule** for the library root in `.claude/settings.local.json`, merged with any existing settings.

It also adds its outputs to `.gitignore`. Init is idempotent: it replaces its own outputs, removes stubs for skills the package no longer has, and leaves anything else alone. `--check` reports each output as `ok`, `stale`, `missing`, `foreign`, or `extra` and exits non-zero on any problem. An output is stale when it differs from what init would write now: the library moved, or a skill's frontmatter changed.

`cp-delivery-probe-library` prints the library root, for testers. Like every Commonplace command would, it first checks the current project's init outputs and warns on stderr when they are stale.

`tools/bump.py <n>` bumps the version and every token to `-V<n>`, for the upgrade cases. `test-project/` holds the `AGENTS.md` and `CLAUDE.md` described above.

## Cases

Use a fresh agent session for each case. Copy `test-project/` to a scratch directory and start sessions there. Stubs go into that project's skill directory, not a user-level one. Record the prompt you used if it differs from the one given.

0. **Install and init.** `uv tool install --python 3.12 <copy>`, then `cp-delivery-probe-init` in the test project. Record `--check` output.
1. **Base layer, no skills.** Remove the skill stubs for this case only (delete the stub directories, or run the case before init writes them and rerun init afterwards). Ask: "Follow the retire-widget procedure from the delivery-probe library and report its tokens." Pass: `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. Record every tool call, how the agent found the file, and every permission prompt or denial.
   - a. With the harness's instruction file importing `library.md` where the harness supports imports (Claude Code: the test project's `CLAUDE.md`). Record whether the agent had the path without reading any file first.
   - b. Without the import (Claude Code: a `CLAUDE.md` containing only `@AGENTS.md`). The agent must read `library.md` itself.
2. **Read permission.** Record whether init's read rule was enough, and which prompts or denials remain. Then remove the rule (edit `settings.local.json`) and repeat case 1a once, to confirm the rule is what allowed the reads. Restore it with init.
3. **Stub skill.** Ask: "Run the delivery-probe-read check." Pass: `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, and `READ-DETAIL-V1`, all read from the installed library. Record whether the agent read the real `SKILL.md`, how it resolved each relative link, and any failed read before success. **Run this case three times**, each in a fresh session; stub-following is the main question.
4. **Router through a stub.** In a second project with no `AGENTS.md` or `CLAUDE.md`, run init. Ask: "Calibrate the gadget using the delivery-probe procedure." Do not name the skill. Pass: the agent loads `delivery-probe-library`, follows it to the real skill, and reports `CALIBRATE-GADGET-V1`.
5. **Upgrade.**
   - a. Run `python3 tools/bump.py 2` in your copy, then `uv tool install --python 3.12 --reinstall <copy>`. Without rerunning init, check that `--check` reports all `ok`, and repeat cases 1a and 3 once. Pass: `-V2` tokens.
   - b. Change `delivery-probe-read`'s description in your copy (for example, append " Version two."), then reinstall. `--check` should report that skill's stubs `stale`, and `cp-delivery-probe-library` should warn. Rerun init and check again.
   - c. Reinstall with `--python 3.13`. `--check` should still report all `ok`, and a fresh case 3 session should still pass.
6. **Editable install.** `uv tool install --reinstall --editable <copy>`. The outputs still point into `share/`, so `--check` should report stubs, `library.md`, and the rule `stale`. Record what a fresh case 3 session does before the repair. Then rerun init, run `python3 tools/bump.py 3` without reinstalling, and repeat cases 1a and 3. Pass: `-V3` tokens read from the source tree. Finish with a normal reinstall and one more init.
7. **Skill names.** Record the names under which the harness lists the stubs.
8. **Fresh clone before init.** In a copy of the test project with no init outputs, start a session and ask case 1's question. Record whether the missing `library.md` (and, in Claude Code, the failing import) causes an error, and what the agent does.

## Package revisions

- **Revision 1** (commit `90e0ef8a`): skills relied on relative links; `install-skills` refused existing entries. Codex ran this revision.
- **Revision 2**: skills and router used the commands first, because agents in Codex misresolved relative links through the skill symlinks. `install-skills` became idempotent and gained `--check`.
- **Revision 3**: the plugin tree moved from package data to wheel shared data, whose path does not change with the Python version. Codex and Claude Code ran this revision ([Codex](../results-codex.md), [Claude Code](../results-claude-code.md)).
- **Revision 4** (2026-09-24): follows the design's decisions. `cp-delivery-probe-init` writes per-project stubs that redirect to the real skill in the installed library, a generated `library.md` with the library's full paths, and one Claude Code read rule, on every platform, with no symlinks. The tree mirrors a KB layout, so skills use ordinary relative links. No agent route runs a command: the lookup commands and `install-skills` are gone. The Claude Code plugin manifest, the marketplace, and the plugin-path command are gone, because the plugin layer was dropped.

Record the revision you started from in your results file.

## Known results before revision 4 (2026-09-24, Linux, uv)

- The shared-data path stayed the same across a Python 3.12→3.13 reinstall, in Codex and in Claude Code. An editable install reads the source tree; its shared data is a stale install-time snapshot.
- Codex needed no permission settings. Claude Code in `default` mode needed an allow rule for each lookup command and read access to the library root; both worked from user-level settings.
- An agent that read a library file at its real path followed the file's relative link correctly in both harnesses. Relative links failed only through symlinked skills in Codex.
- Both harnesses dropped a dangling symlinked skill without an error.
- Codex listed symlinked skills with a plugin-name prefix while the tree had a `.claude-plugin/plugin.json`; Claude Code listed bare names.

## Recording results

Copy `RESULTS-TEMPLATE.md` to `../results-<harness>.md` in the workshop and fill it in. One file per harness and revision; if the file exists, add a suffix such as `-r4`.
