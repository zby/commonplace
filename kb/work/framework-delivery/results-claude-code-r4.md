# Delivery probe results: Claude Code, revision 4

- Harness and version: Claude Code 2.1.281, fresh headless sessions (`claude -p --permission-mode default --output-format stream-json`)
- Model: claude-opus-5-5 (1M context), the configured default; no override
- Operating system: Linux (Ubuntu 24.04, x86_64)
- uv and Python versions: uv 0.12.17; Python 3.12.8 and 3.13.1
- Tester (agent or person) and date: Claude Code agent (Opus 5.5), 2026-09-24, at the operator's request
- Probe package revision (see PROTOCOL.md): revision 4, at commit `69d58a6d`

**Result.** Every case passed. Agents reached the library only by reading files, with no lookup commands. The one read rule that init wrote into the project's `.claude/settings.local.json` was enough for every read. The stub hop worked the same way in all runs: stub, then the real `SKILL.md`, then its relative links. One risk was found: before init reran after a switch to an editable install, a stub still pointed into the stale `share/` snapshot, and the agent read old content with no warning (case 6).

## Harness facts

- Instruction file it loads: `CLAUDE.md`, which here imports `AGENTS.md` and `.cp-delivery-probe/library.md` with `@`. An import of a missing file did not cause an error (case 8).
- Can the agent run shell commands? Yes. Read-only commands inside the project ran without approval; commands outside the project or with `$` expansion needed approval, which a headless session cannot give.
- Can the agent read files outside the project, and under what setting? With a `Read(//<root>/**)` allow rule. In this run the rule sat in the project's uncommitted `.claude/settings.local.json`, the first test of a project-level rule. Without it, the Read tool and `ls` of the library were denied (case 2).
- Does it read project-level skill directories, and which? `.claude/skills/`. The stubs under `.agents/skills/` were not needed by Claude Code.
- Can permission settings live in the project, and can a machine-specific part stay uncommitted? Yes: `.claude/settings.local.json`, which init also listed in `.gitignore`.

## Cases

Every model case ran in a fresh session with the protocol's prompt. The raw stream-JSON logs were in the scratchpad and were deleted at cleanup.

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install and init | Pass | Python 3.12 install. Init wrote four stubs, `library.md`, the read rule, and a `.gitignore` block. `--check`: six `ok`. | — |
| 1a Base layer, file imported | Pass | No skill stubs. With `library.md` imported by `CLAUDE.md`, the agent's first call read the instructions index by full path, then `retire-widget.md` and its linked `shared-step.md`. `RETIRE-WIDGET-V1`, `SHARED-STEP-V1`. 3 tool calls. | none |
| 1b Base layer, file read by the agent | Pass | `CLAUDE.md` imported only `AGENTS.md`. The agent read `library.md` with a Bash `cat`, tried one `$`-expansion command (denied), then read the index and both files. Same tokens. 6 tool calls. | 1 Bash denial, not blocking |
| 2 Read permission | Pass | With init's rule: no denials in any case. With `settings.local.json` emptied: the Read and an `ls` of the library were denied, and the agent stopped and pointed at the missing rule. Init restored it. | Without the rule: 2 denials |
| 3 Stub skill, run 1 | Pass | Skill tool loaded the stub; the agent read the real `SKILL.md` in `share/`, then `../shared-step.md`, `../../types/probe-note.md`, and `./references/read-detail.md`, each resolved from the real skill's directory. `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, `READ-DETAIL-V1`. | none |
| 3 Stub skill, run 2 | Pass | Same trace as run 1. | none |
| 3 Stub skill, run 3 | Pass | Same trace as run 1. | none |
| 4 Router through a stub | Pass | Project with no `AGENTS.md` or `CLAUDE.md`. The prompt selected `delivery-probe-library` without naming it; the agent read the real router skill, then `calibrate-gadget.md`. `CALIBRATE-GADGET-V1`. | none |
| 5a Upgrade, same Python | Pass | Bump to V2 and reinstall. No init rerun: `--check` six `ok`. Fresh base and skill sessions reported V2. | none |
| 5b Description change | Pass | After a description change and reinstall, `--check` reported exactly the two stubs of that skill `stale`, and `cp-delivery-probe-library` warned about them. One init rerun: six `ok`. | — |
| 5c Python change | Pass | Reinstall on Python 3.13: six `ok` with no init rerun; a fresh skill session reported V2. | none |
| 6 Editable install | Pass after repair; silent stale read before it | Editable install: `--check` reported all six outputs `stale`. The source was then bumped to V3 while `share/` still held V2. **Before repair**, a fresh skill session followed the stub into `share/` and reported V2, with no warning, because the agent ran no command that could warn. **After one init rerun**, the stubs, `library.md`, and the rule pointed at the source tree, and fresh base and skill sessions reported V3. Returning to a normal install: the command warned, one init rerun repaired it, and a fresh session reported V3 from `share/`. | none |
| 7 Skill names | Observed | Claude Code listed the stubs as `delivery-probe-library` and `delivery-probe-read`, with no prefix. | — |
| 8 Fresh clone before init | Pass | A copy of the test project with only `AGENTS.md` and `CLAUDE.md`. The session started without error despite the failing import. The agent found no `library.md`, did not guess a location, and told the user to run init. | 2 Bash denials (checking whether the init command exists) |

## Modifications to the package

None. In the scratch copy, only the supplied `tools/bump.py` and the protocol's description edit (case 5b) changed files.

## Consequences for the design

- **Observed:** stubs work in Claude Code. In five skill sessions (case 3 three times, 5a, 5c) and the router case, the agent followed the stub to the real skill and resolved its relative links from the real location, with no failed read.
- **Observed:** the generated `library.md` works as the base-layer route. Imported, it costs no tool call; read by the agent, it costs one.
- **Observed:** one `Read` rule in the project's `.claude/settings.local.json` is the only setting Claude Code needs.
- **Observed:** a normal upgrade and a Python change need no init rerun; a description change is detected and repaired by one rerun.
- **Observed:** after an editable/normal switch and before the init rerun, agents read the stale `share/` snapshot silently. With no command in the agent's route, the check cannot warn the agent. **Inferred:** this risk is limited to install-mode switches, which developers make; the design should say so, and the developer procedure should rerun init right after a switch.
- **Observed:** a fresh clone without init fails safely: the agent says what is missing and does not guess.

## Cleanup

Ran `cp-delivery-probe-init --remove` in both test projects and uninstalled the tool. No user-level setting was changed: `~/.claude/settings.json` kept its SHA-256, and the user-level skill directories were untouched. The scratch copies and logs were deleted. No hooks were used, no credentials were touched, and the real `llm-commonplace` installation was not changed.
