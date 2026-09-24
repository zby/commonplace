# Delivery probe results: Codex, revision 4

**Result.** The generated routing file, per-project stubs, router selection, ordinary upgrade, and Python-version change worked in Codex on Linux. All three initial stub runs followed the real skill and resolved its relative links correctly. Codex needed no additional read permission. After switching to an editable install, a fresh session silently read the old shared-data snapshot until init repaired the pointers. A fresh clone without init recovered by searching a nearby source checkout; this run does not establish that missing initialization causes the agent to stop.

- Harness and version: codex-cli 0.156.1; fresh `codex exec --ephemeral` sessions, plus app-server discovery and one fresh permission-test thread.
- Model: configured `gpt-6-astra`, high reasoning effort, without an override. The app-server thread-start response confirmed both values.
- Operating system: Ubuntu 24.04.5 LTS, Linux x86_64.
- uv and Python versions: uv 0.12.17; Python 3.12.8 and 3.13.1.
- Tester and date: Codex agent, 2026-09-24, at the operator's request.
- Probe package: revision 4 at checkout `09740c30dd6e5d6504042cf37e143fd543a5fcbc`.
- Scratch root: `/tmp/cp-probe-r4-hca4hft2`, called `R` below.

## Controls and reproducibility

The package was copied unchanged to `R/package`. `UV_TOOL_DIR`, `UV_TOOL_BIN_DIR`, and `UV_CACHE_DIR` pointed to `R/tools`, `R/bin`, and `R/cache`. The source, installed tool, and test projects were separate directories. The real Commonplace tool was not changed.

Every model case used the protocol's prompt verbatim in a fresh session. Fourteen CLI sessions explicitly selected `read-only`; the supplemental app-server session selected `workspace-write` and `on-request`, and its returned settings confirmed those choices. The outer test runner had unrestricted filesystem access after the operator resumed the interrupted setup; that is distinct from the tested child sandboxes. No test used a sandbox bypass.

Hooks were disabled for every invocation. Unrelated discovered skills were disabled through per-process `skills.config` overrides; no user configuration was written. The base-layer project had both sets of probe stubs removed, and the router project had neither `AGENTS.md` nor `CLAUDE.md`. No plugin or instruction-serving MCP server was installed or used. These are individual observations, not reliability estimates.

The pre-interruption CLI preflight reported 0.155.1. After resumption, discovery and every model invocation reported 0.156.1. This probe did not upgrade Codex. The results above concern 0.156.1.

Initial fixture SHA-256 values:

```text
pyproject.toml: 7e464171f739329aca4541eafa5875028395ef4a7469210c555446777553ef9d
src/cp_delivery_probe/cli.py: 3a00575d64ac734fbff100c1799bc6202dd2a0a40649d0ceeb2ca9a915ac8bd3
PROTOCOL.md: 33f2560a161dd9366439ec6fe219f95cdc945946dab2c7c7841dc438e0e02dd5
```

## Harness facts

- **Instruction file:** `AGENTS.md`. The supplemental thread reported exactly `R/base/AGENTS.md` as its instruction source. The supplied `CLAUDE.md` imports were not the route used by Codex.
- **Shell commands:** available. The model read files with shell `cat`; this tests file-based delivery without lookup commands, not operation in a harness without a shell or file-reading tool.
- **Reads outside the project:** succeeded in the tested read-only and workspace-write sandboxes without an additional read rule. Removing `.claude/settings.local.json`'s rule did not change the result. This does not establish behavior under a custom restrictive filesystem policy.
- **Instruction-file imports:** no native import route was established or used. Case 1a is not applicable to this run. The documented instruction discovery mechanism loads instruction files by directory and configured fallback filename; it does not establish a Claude-style `@` import for this fixture. See the [official instruction-discovery documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **Agent Skills:** discovery returned both project stubs from `.agents/skills/`, with `scope: repo`, `enabled: true`, `pluginId: null`, and `errors: []`. Names were `delivery-probe-read` and `delivery-probe-library`, without a prefix. The installed source tree had no plugin manifest.
- **Other skill directories:** discovery also returned user skills under `~/.agents/skills/` and system skills under `~/.codex/skills/.system/`. The generated `.claude/skills/` copies were not the discovered paths in this run; this is not an exclusive-directory support claim.
- **Project permission settings:** Codex required none for this route. Init's machine-specific Claude rule remained in the uncommitted project settings file; removing it and restoring it were confined to the fixture.
- **Configurable search paths:** not exercised here. The [earlier Codex report](./results-codex.md) records discovery through `skills/extraRoots/set`; that result is not evidence of a complete installation or upgrade workflow. This run used ordinary project discovery.

## Cases

`L` below is `R/tools/cp-delivery-probe/share/cp-delivery-probe`; `S` is `R/package/library`.

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install and init | Pass | Normal Python 3.12 install. Init wrote four stubs, `library.md`, and the read rule. `--check` reported six `ok`. | None in the completed setup. Before interruption, the sandbox prevented Snap's uv launcher from starting. |
| 1a Base layer, file imported | Not applicable | No native import route was used; Codex followed `AGENTS.md` and read the routing file itself. | — |
| 1b Base layer, file read by the agent | Pass | With no probe skills, read `library.md`, the instructions index, the procedure, and its shared step. Returned `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. Four successful read commands. | None |
| 2 Read permission | Pass | With the Claude settings emptied, the base prompt produced the same V1 result and four successful reads. A separate app-server thread with verified workspace-write/on-request settings also produced V1 with four reads. | No approval request or denial |
| 3 Stub skill, run 1 | Pass | Read stub → real skill → shared step, type, and skill-local reference. All three V1 tokens. Also read `library.md`; six read commands total. | None; no failed read |
| 3 Stub skill, run 2 | Pass | Same files and V1 tokens; six read commands. Reference-read order differed. | None; no failed read |
| 3 Stub skill, run 3 | Pass | Same files and V1 tokens; six read commands. | None; no failed read |
| 4 Router through a stub | Pass | Without either instruction file, the calibration prompt selected the router. Read router stub → real router → `calibrate-gadget.md`; returned `CALIBRATE-GADGET-V1`. | None |
| 5a Upgrade, same Python | Pass | Bumped to V2 and reinstalled on Python 3.12. No init rerun: six `ok`. Fresh base and skill sessions read V2 from `L`. | None |
| 5b Description change | Pass | Appended ` Version two.` to the read skill's description and reinstalled. Exactly its two stubs were `stale`; the tester's library-root command warned about both. One init rerun restored six `ok`. | — |
| 5c Python change | Pass | Reinstalled on Python 3.13. No init rerun: six `ok`. A fresh skill session read all three V2 tokens from the unchanged `L` path. | None |
| 6 Editable install, before repair | Silent stale read | Editable install made all six outputs `stale`. Source was then bumped to V3 without reinstalling; shared data retained V2. A fresh skill session followed the old stub and reported V2 from `L`, calling the check passed, with no warning. | None |
| 6 Editable install, after repair | Pass | One init run per initialized test project changed its pointers to `S`. Fresh base and skill sessions read V3 from source without reinstalling. Main-project `--check`: six `ok`. | None |
| 6 Return to normal install | Pass after repair | Normal V3 reinstall made the source-pointing outputs stale. One init rerun restored six `ok`; a fresh skill session read V3 from `L`. | None |
| 7 Skill names | Observed | Discovery listed both project stubs under bare names, with no plugin prefix. | — |
| 8 Fresh clone before init | Observed recovery outside the intended route | Missing `library.md` caused a failed read, not a session-start error. The agent searched the fixture's parent tree and its Codex directory, found the nearby package source, and returned its V1 tokens. It did not run init or explain the missing initialization in its final answer. | One missing-file error; no permission denial |

### Base-layer read trace

Case 1b made exactly these four shell reads, in order:

```text
cat .cp-delivery-probe/library.md
cat L/instructions/README.md
cat L/instructions/retire-widget.md
cat L/instructions/shared-step.md
```

Every command exited zero. The permission-control and supplemental workspace-write sessions followed the same sequence. The V2 base session used the same paths; the repaired editable base session substituted `S` for `L`. No model session ran a library lookup command.

### Fresh-clone trace and limitation

Case 8 made four shell calls:

1. Read the missing `.cp-delivery-probe/library.md` (exit 1).
2. Print the working directory, search `R` and `~/.codex` for instruction/probe-related filenames, and locate `cp-delivery-probe-init` on PATH.
3. Read that executable's wrapper and `S/instructions/retire-widget.md`.
4. Read `S/instructions/shared-step.md` and search `R` for routing files, implementation files, and `AGENTS.md` files.

The final response contained only the two V1 tokens. Both installed and source content were V1 at this point, so matching tokens cannot establish that the correct installation was selected. The nearby source checkout made this recovery possible. This is evidence against assuming that an absent routing file necessarily makes Codex stop; it does not predict what a clone without a nearby source checkout would do.

## Modifications to the package

No implementation or harness-adaptation changes were needed. Only the protocol's version/token bumps and description edit changed the scratch package. All files in the workshop's original probe package retained their initial hashes.

Execution adaptations:

- Used isolated uv tool, executable, and cache directories. Added the isolated executable directory to child-session PATH without editing shell configuration.
- Used separate base, skill, router, and uninitialized projects so base cases had no skill stubs. Restored the base project's settings with init after the permission test; removed its regenerated skill stubs before further base cases.
- Repeated case 1b where the upgrade protocol asks for case 1a, because this run used the explicit-read route.
- Moved the V3 source bump ahead of the pre-repair editable-session check, so source and shared-data tokens differed. This makes a stale read distinguishable. Repair then changed only init's outputs; the successful V3 reads still occurred without a package reinstall.
- Added one app-server permission case to verify returned sandbox, approval, model, and instruction-source settings directly.

## Consequences for the design

- **Observed:** Codex followed these stubs and their relative links successfully, including all three required initial repetitions. Bare names held without a plugin manifest. No Codex-specific package changes were needed.
- **Observed:** the generated routing file supplied the base-layer route without skills or lookup commands. The three initial skill runs also read it, adding a read beyond the stub, real skill, and three references.
- **Observed:** normal content upgrades and the Python-version change preserved the routing paths. Description drift was detected and repaired as designed. These tests used `uv tool install --reinstall`, not `uv tool upgrade`.
- **Observed:** command-time detection did not warn the model during the pre-repair editable run, because its file-only route never executed the check. **Inferred:** the developer procedure must repair pointers immediately after a mode switch; the tested design does not prevent intervening stale reads.
- **Observed:** the uninitialized clone recovered from neighboring source files without reporting the missing routing file. **Inferred:** if stopping on missing initialization is required, state that requirement explicitly in the project instruction template and test it. The current fixture does not enforce that behavior.
- **Not established:** Windows/macOS behavior, running-session upgrades, a full-size router index, promoted skills with richer frontmatter or `agents/` metadata, the actual Commonplace source-checkout migration, and centrally restricted filesystem policies. This probe's skills have only name/description frontmatter and ordinary Markdown references.

## Cleanup

Ran `cp-delivery-probe-init --remove` in the three initialized projects, then uninstalled `cp-delivery-probe` using the isolated uv directories. Confirmed removal of the generated routing directories, skill stubs, Claude settings files, tool environment, and both executables. Removed the scratch source, projects, cache, runner scripts, raw traces, and generated app-server schemas after recording these results. Normal Codex runtime logging was not rewritten.

No user-level skills, plugins, shell settings, or real Commonplace installation were changed. Credentials were not copied or moved. Codex configuration contained no probe entries. Its hash differed from the pre-interruption baseline, with a modification timestamp before the first model session; those unrelated changes were left untouched. It remained unchanged between the resumed-run checkpoint and cleanup.

Only this report and the reply line in [probe-request.md](./probe-request.md) were written in the repository. No commit was made.
