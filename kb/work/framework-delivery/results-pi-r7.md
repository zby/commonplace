# Delivery probe results: pi, revision 7

- Harness and version: pi 1.3.0, fresh headless JSON sessions.
- Model: `openai/gpt-6.1-sol`, thinking `medium`, for every model case.
- Operating system: Linux, Ubuntu, x86_64; kernel `6.8.0-147-generic`.
- uv and Python versions: uv 0.13.4; CPython 3.12.8 and 3.13.1.
- Tester (agent or person) and date: pi agent, 2026-10-24, at the operator's request.
- Probe package revision: 7, copied from this workshop without harness-specific package edits.

**Result.** File delivery, native stubs, index-only skills, upgrades, missing-init handling and argument forwarding worked. The three native-stub runs and three index-only runs all passed. Case 10 did not reach the delegated token: the fresh session stopped with `no sub-agent available`, without reading the target. These results describe pi without a sub-agent extension, not the repository's extended pi configuration. The editable-install switch also reproduced a silent read through stale pointers before init repaired them.

## Harness facts

- **Instruction file:** the session reported the project's `AGENTS.md` as loaded in initial context. It did not have the generated library's paths until it read `.cp-delivery-probe/library.md`. The `@` lines in the supplied `CLAUDE.md` did not provide an imported library in these runs. Case 1c was not applicable.
- **Shell commands:** available through the built-in `bash` tool. Model cases used only `read`; no model case invoked a shell command.
- **Outside-project reads:** worked with ordinary account permissions, both with and without the Claude Code read rule. No per-read permission prompts or denials occurred. Project trust is resource-loading permission, not a filesystem sandbox.
- **Agent Skills:** pi supports `.pi/skills/` and `.agents/skills/` project locations, and user `~/.pi/agent/skills/` and `~/.agents/skills/` locations, according to its installed documentation. This run directly verified project `.agents/skills/` discovery. No user-level skills were installed or changed. The `.claude/skills/` copies were generated but not used by these sessions.
- **Project trust:** each launch used `--approve`, a one-process trust decision. This is necessary to make project skill discovery explicit in headless sessions; there was no interactive trust prompt or saved trust-setting change. Unapproved project skills were not tested.
- **Sub-agents:** stock pi does not supply a sub-agent tool. The supervising checkout has a project extension, but it was not projected into the scratch projects. All case sessions explicitly disabled extension discovery. The case 10 session neither started a worker nor devised an emulation. This does not establish that a headless CLI emulation is impossible.
- **Project-local permission settings:** init's uncommitted `.claude/settings.local.json` existed, but its read rule was unnecessary for pi. No pi permission configuration was added. Init's `.gitignore` kept its machine-specific outputs uncommitted.

### Environment and session isolation

The operator authorised isolated uv tool directories so this run could coexist with another harness's probe. All installs, reinstalls and uninstall used:

```text
root=/tmp/cp-probe-pi-r7-Yl3TOros
UV_TOOL_DIR=<root>/tools
UV_TOOL_BIN_DIR=<root>/bin
PATH=<root>/bin:<original PATH>
```

The package copy was `<root>/package`; projects were `<root>/project`, `<root>/project2`, and `<root>/fresh`. No installation targeted the default user-level uv tool directory. Separate unscoped `uv tool list` checks confirmed the default user installation had no `cp-delivery-probe` during this run.

Every model case was a new process in its scratch project, with no setup conversation or previous case history:

```text
pi --mode json --no-session --no-extensions --no-mcp --approve \
  --model openai/gpt-6.1-sol --thinking medium '<protocol prompt>'
```

No hooks or MCP servers were used. The existing pi credential configuration remained in place; no credentials were copied or moved. `--no-session` kept these case conversations in memory; the runner captured JSON events and stderr under the scratch root for inspection before cleanup.

Protocol prompts were used verbatim, including the allowed natural-language echo invocation. Case 7 used an additional observation prompt: “Report which project instruction file was loaded into your initial context and list the available delivery-probe skill names and their paths. Do not run the skills.”

## Cases

No permission prompts or denials occurred in any case. The expected missing-file read in case 8 was the only tool error.

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install and init | Pass | Isolated `uv tool install --python 3.12 <root>/package`. Init created eight stubs, `library.md`, `.gitignore`, and both control-plane templates; it wrote `.claude/settings.local.json`. `--check`: ten `ok`, exit 0. | None |
| 1a Base layer, file imported | Not applicable to imports; base read passed | Stubs removed. Supplied `CLAUDE.md` retained. No automatic library import was observed: the agent first read `library.md`, then the real router, retire procedure and shared step. Both V1 tokens returned. | None |
| 1b Base layer, file read by the agent | Pass | With `CLAUDE.md` reduced to `@AGENTS.md`, the same four reads returned `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. | None |
| 1c Alternate standing-instruction mechanism | Not applicable | Project `AGENTS.md` already supplied the pointer and missing-init rule. | None |
| 2 Read permission | Pass; Claude rule not required | With `.claude/settings.local.json` replaced by `{}`, the same base-layer reads and V1 tokens succeeded. Restored supplied `CLAUDE.md` and reran init afterwards. | None |
| 3 Stub skill, run 1 | Pass | Read project stub, `library.md`, real skill, shared step, note type, and local reference. All three V1 tokens. | None |
| 3 Stub skill, run 2 | Pass | Read project stub, real skill and its three linked files, then `library.md`. All three V1 tokens. | None |
| 3 Stub skill, run 3 | Pass | Read project stub, real skill and its three linked files. All three V1 tokens. | None |
| 4 Router through a stub | Pass | Second project had neither adopted `AGENTS.md` nor `CLAUDE.md`; init wrote only the templates. The unnamed calibration request selected `.agents/skills/delivery-probe-library/SKILL.md`, followed its pointer to the real router, then read `calibrate-gadget.md`. Returned `CALIBRATE-GADGET-V1`. | None |
| 5a Upgrade, same Python | Pass, with stub-restoration qualification below | Bump to V2 and normal Python 3.12 reinstall. Before any init rerun, `--check` gave ten `ok` and the no-stub base session returned both V2 tokens. After restoring the temporarily removed stubs with init, the skill session returned all three V2 tokens. | None |
| 5b Description change | Pass | Appending ` Version two.` made exactly the two read-skill stubs **and `library.md`** stale. `--check` exited 1; the library command warned about those three outputs. One init rerun restored ten `ok`. | None |
| 5c Python change | Pass | Normal reinstall using Python 3.13.1: ten `ok` without init, and a fresh native-stub session returned all three V2 tokens. | None |
| 6 Editable install | Pass after repair; silent stale-pointer read before repair | Editable reinstall made all ten outputs stale. Before repair, a fresh skill session read V2 files under `share/`, with no warning. Init redirected outputs into the source tree; bump to V3 without reinstall then produced both base V3 tokens and all three skill V3 tokens from `<root>/package/library/`. A final normal Python 3.13 reinstall and init restored ten `ok`; another fresh skill session read V3 under `share/`. | None |
| 7 Skill names | Pass | Bare names: `delivery-probe-delegate`, `delivery-probe-echo`, `delivery-probe-library`, `delivery-probe-read`; all paths under project `.agents/skills/`. | None |
| 8 Fresh clone before init | Pass | First read of `.cp-delivery-probe/library.md` returned `ENOENT`. Session stopped and asked the user to run `cp-delivery-probe-init`; it did not search elsewhere or run init itself. No startup import error was reported. | One expected missing-file error, not a permission denial |
| 9 Emulated skill, run 1 | Pass | Both stub directories removed. Read `library.md`, real read skill from its index, then all three linked files. All three V1 tokens. | None |
| 9 Emulated skill, run 2 | Pass | Same five-read route and V1 tokens. | None |
| 9 Emulated skill, run 3 | Pass | Same five-read route and V1 tokens. Init restored stubs afterwards. | None |
| 10 Sub-agent | Fail; stopped safely | Read delegate stub and real skill, then returned exactly `no sub-agent available`. No read of `delegated-step.md`, no worker launch, and no emulation attempt. No delegated token was returned. | None |
| 11 Stub with arguments | Pass | Prompt: “Run the delivery-probe-echo check with the argument kumquat”. Read stub, real echo skill and shared step; returned `SHARED-STEP-V1` and `ECHO-V1 kumquat`. The model carried the argument; no harness `$ARGUMENTS` substitution occurred on file reads. | None |

### Second-project outcome check

After the final normal V3 reinstall, init refreshed the second project's read-skill descriptions and routing index. Two additional fresh sessions in that project repeated the named retire procedure and the read skill. The first followed the native router stub and returned `RETIRE-WIDGET-V3` and `SHARED-STEP-V3`; the second followed the read stub and returned all three V3 read-skill tokens. Both used only successful reads. This supplements case 4 with the probe request's named-instruction and skill outcomes in a second project, still without adopted `AGENTS.md` or `CLAUDE.md` there.

### Case 0 output set

Init reported these eight stubs and the generated routing/settings files. `--check` printed `ok:` for each of these ten paths:

```text
.claude/skills/delivery-probe-read
.claude/skills/delivery-probe-delegate
.claude/skills/delivery-probe-echo
.claude/skills/delivery-probe-library
.agents/skills/delivery-probe-read
.agents/skills/delivery-probe-delegate
.agents/skills/delivery-probe-echo
.agents/skills/delivery-probe-library
.cp-delivery-probe/library.md
.claude/settings.local.json
```

`AGENTS.md.template` and `CLAUDE.md.template` appeared beside the adopted `AGENTS.md` and `CLAUDE.md`. Init also created its `.gitignore` block.

The exact read rule written was:

```text
Read(//tmp/cp-probe-pi-r7-Yl3TOros/tools/cp-delivery-probe/share/cp-delivery-probe/**)
```

### Base-layer tool traces

For cases 1a, 1b and 2, every call was `read`, with no offset or limit. Each session made these four calls in this order:

1. `.cp-delivery-probe/library.md`
2. `<installed-library>/instructions/delivery-probe-library/SKILL.md`
3. `<installed-library>/instructions/retire-widget.md`
4. `<installed-library>/instructions/shared-step.md`

Here `<installed-library>` expands exactly to `/tmp/cp-probe-pi-r7-Yl3TOros/tools/cp-delivery-probe/share/cp-delivery-probe`. The initial `AGENTS.md` pointer led to the routing file, whose skill index led to the router. Neither the library's absolute path nor its body was automatically imported. There were no failed reads or permission requests in these traces.

### Relative links, arguments and upgrade qualifications

All three native skill runs read the **real** `SKILL.md` before resolving its links. They resolved `../shared-step.md`, `../../types/probe-note.md` and `./references/read-detail.md` from the installed real skill directory, not from the stub directory. No failed relative-link reads occurred. All three index-only runs did the same after reading the index.

Case 11's ordinary file reads delivered literal `$ARGUMENTS` text to the model. The model used the invocation's `kumquat` argument when following the real skill; it did not report the literal placeholder. This tests the protocol's natural-language invocation, not pi's `/skill:name` command expansion.

In case 5a, init was rerun only to recreate the stubs removed for the repeated no-skills base test. Its report said it created the eight stubs and preserved both templates; it did not refresh the existing library pointer or settings. Nevertheless, the skill result was obtained after that restoration, not in a strictly no-init sequence. The pre-restoration ten-`ok` check and V2 base read are the direct evidence for no required pointer refresh. Case 5c separately passed both check and native skill without any init rerun.

In case 6, the pre-repair read preceded the V3 bump, as the protocol specifies. It proves use of the stale `share/` location without a warning; it does not demonstrate a source/share token divergence at that instant, since both still held V2.

## Modifications to the package

No harness-specific modifications. Only these protocol-directed source changes were made to the scratch copy:

1. `python3 tools/bump.py 2`: package version became `2.0.0` and library tokens became V2.
2. Append the exact text ` Version two.` to the one-line `description:` value in `library/instructions/delivery-probe-read/SKILL.md`.
3. `python3 tools/bump.py 3`: package version became `3.0.0` and library tokens became V3, without reinstalling the editable package.

The workshop's package was not edited. Project-only changes were temporary stub deletion/restoration, replacing `CLAUDE.md` with `@AGENTS.md` for case 1b, removing the Claude read rule for case 2, and creating the second and uninitialised projects. No library bodies were copied into a project.

## Consequences for the design

- **Observed:** pi can use the supplied `AGENTS.md` pointer, native `.agents/skills/` stubs, and the routing file's skill index. No harness-specific package change was needed for file delivery. The index succeeded in three fresh sessions, not a statistical reliability estimate.
- **Observed:** headless native-skill discovery worked with explicit project trust. **Inferred:** unattended launch instructions should state their trust choice; these results should not be read as evidence that untrusted project skills load automatically.
- **Observed:** pi did not need the Claude read rule. Its ordinary filesystem permissions allowed outside-project reads.
- **Observed:** a description change invalidated the indexed description in `library.md` as well as the two stubs. Reporting only stale stubs would omit part of the current generated surface.
- **Observed:** the editable switch left usable old paths, so a file-only session read from them without the CLI's stale-output warning. **Inferred:** install-mode switches must be followed immediately by init; a command warning cannot protect sessions that run no command.
- **Observed:** the delegate skill stopped safely but did not obtain a worker in this stock scratch configuration. The supervising repository extension was not inherited merely because the parent session had it. **Inferred:** delegated skills need an explicitly supplied worker facility or a tested emulation route. This run does not certify the checkout extension, nested delegation, or automatic headless emulation.
- **Observed:** the model carried `kumquat` across the stub hop without textual harness substitution. No administrator change or per-use operator workaround was required for this argument case.

## Cleanup

Completed `cp-delivery-probe-init --remove` in all three scratch projects, including the uninitialised fresh clone. Uninstalled `cp-delivery-probe` with the same isolated `UV_TOOL_DIR` and `UV_TOOL_BIN_DIR`; the isolated `uv tool list` then reported `No tools installed`. Deleted `/tmp/cp-probe-pi-r7-Yl3TOros`, including package changes, projects, runner, and JSON logs, and confirmed the root no longer existed.

The result's required template sections and local Markdown links were checked with Python; `git diff --check` passed. No `commonplace-validate` command was run because the probe commission prohibited every `commonplace-*` command. No runtime code changed, so pytest was not applicable.

No persistent pi trust setting, user skill, hook, or MCP configuration was changed. The real `llm-commonplace` installation and all `commonplace-*` commands were left untouched. The default user-level tool list was checked separately for the prohibited shared probe installation. Only this result file and its reply line are this run's repository outputs; concurrent Codex and source-ingest changes were not authored by this run.
