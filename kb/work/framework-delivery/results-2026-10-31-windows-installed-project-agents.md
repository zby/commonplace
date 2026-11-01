# Windows installed-project agent checks (2026-10-31)

Item 4 of the [Windows delivery handoff](./windows-delivery-handoff.md): agents rooted in an initialised scratch project, not in this checkout, on the afflicted Windows machine.

## Setup

- Install: `llm-commonplace` built from GitHub `main` (`55700da28`), non-editable, over python.org 3.14.7, with the `INSTALL.md` shims. Installation record: [windows-install run 4](../windows-install/results-2026-10-31-afflicted-main-run4.md).
- Project: `<HOME>\cp-install-test-run4`, initialised by that run, Git repository with one commit. `.commonplace/library.md` and the stubs point at `<tool env>/share/commonplace`, outside the project.
- Smart App Control on; Defender, Avast and McAfee present.

## Claude Code: not run

The Claude Code CLI bundled with the desktop app (2.1.308) was run headless (`claude -p`) from the project. It exited at once with `Not logged in · Please run /login`: the desktop app authenticates its own sessions and the bundled CLI does not share that login. Signing in is the operator's action. Not covered, so: whether Claude Code honours the generated `Read(//C:/Users/…/**)` rule, native skill listing, and `/cp-skill-validate <arg>` through a stub. A desktop Code session rooted in the scratch project, or a logged-in CLI, can run them.

## Codex

`codex-cli 0.166.0-alpha.5.1`, the Codex desktop app's CLI, logged in with ChatGPT; default model. Each check was a fresh `codex exec --ephemeral` session with `-C <project>`, started one at a time.

| Check | Sandbox | Result |
|---|---|---|
| A. Skill listing and bare command | `read-only` | **Pass.** All 12 `cp-skill-*` skills listed from `.agents/skills/`. `commonplace-validate --help` ran and `Get-Command` resolved to `.local\commonplace-shims\commonplace-validate.cmd`. The first three commands failed with `CreateProcessWithLogonW failed: 267` (invalid directory); they ran after Codex dropped the project as the working directory. |
| B. Stub with an argument: `$cp-skill-validate kb/log.md` | `workspace-write` | **Pass.** Read the stub, then the real `SKILL.md` in the installed library by full path; applied `kb/log.md` as `$ARGUMENTS`; ran `commonplace-validate "kb/log.md"` in the project, exit 0, `VALIDATION SUCCESS`. No permission setting was needed. |
| C. `$cp-skill-health-check`, diagnose only | `workspace-write` | **Pass for the shim rule.** It reported every one of the 25 commands as "shim recognised (uv tool; matching interpreter and entry point)", with no shadowing; `commonplace-init --check` all `ok`; `validate landings` passed. It could not run `uv tool list` or `rg` (see below) and named that as the only issue. |
| E. Index route, no stubs: `.agents/skills/` moved aside, "Run the Commonplace validation skill on kb/log.md" | `workspace-write` | **Pass.** Found the skill through `.commonplace/library.md`, read the real `SKILL.md`, applied `kb/log.md` as the argument, exit 0. The validator then warned that stubs were missing, and the agent ran `commonplace-init` unprompted; the sandbox refused to write `.agents/skills` (exit 1). The stubs were restored with init afterwards; `--check` all `ok`. |

No check changed a project file; `git status` showed only the two templates from run 4's gap 1.

### Codex sandbox account

Commands in Codex's sandbox run as a separate local account (`whoami`: `codexsandboxoffline`). Its `PATH` holds the user `Path` entries, and it can reach `<HOME>\.local` (shims and the tool environment) and `C:\Program Files\Python314`. But `Get-Command uv` and `Get-Command rg` found nothing, though their WinGet directories under `<HOME>\AppData\Local\Microsoft\WinGet\Packages\` exist for it, and `WindowsApps` was denied. Inference: that account cannot read the executables in the user's `AppData`. Under this sandbox, Commonplace commands work, but procedures that call `uv` or `rg` do not. `rg` is a required prerequisite of the connect and search steps. Not tested: installing `rg` and `uv` outside `AppData`, or Codex's other sandbox settings.

## Not covered

- Claude Code (above). pi is not installed on this machine.
- Upgrade cases: changed skill, library-only change, moved installation, already-running session.
- Probe revision 7's package; these checks used the real project instead.
