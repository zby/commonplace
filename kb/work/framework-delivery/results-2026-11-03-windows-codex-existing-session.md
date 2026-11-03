# Windows Codex existing-session delivery check (2026-11-03)

## Purpose and setup

The operator requested an independent repeat of the delivery workshop's
installation checks after the Claude run. Followed the bounded existing-install
route in the [Windows handoff](./windows-delivery-handoff.md), without reinstalling
or repairing anything.

- Runtime: Codex desktop chat. The bundled executable reports
  `codex-cli 0.166.0-alpha.5.1`; the desktop app version and exact model identifier
  were not established. That CLI version does not identify the desktop app.
- OS: `Microsoft Windows NT 10.0.26300.0`, from .NET.
- Chat root: `C:/Users/zzbby/commonplace`, source HEAD `e8087b7f1`.
  This was not a fresh session rooted in the installed project.
- Command working directory for installed-project checks:
  `C:/Users/zzbby/cp-install-test-pypi033`.
- Permissions: workspace-write sandbox; the scratch project and installed
  library were readable but outside the writable workspace roots.
- Installed tool: `uv tool list` reports `llm-commonplace v0.3.3`.
- Library root, read from the project's `.commonplace/library.md`:
  `C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace`.
- No app restart was performed or established. Antivirus state, interpreter
  signature and Workjig version were not rechecked in this bounded run.

## Results

| Check | Observation and scope |
|---|---|
| Bare command discovery and help | In the scratch project's PowerShell context, `Get-Command commonplace-validate` resolved to `C:/Users/zzbby/.local/commonplace-shims/commonplace-validate.cmd`; `commonplace-validate --help` exited 0. The same route also worked from the checkout. |
| Project pointers and installed-library read | Read the project's `AGENTS.md`, `.commonplace/library.md`, and `.agents/skills/cp-skill-validate/SKILL.md`. Followed the supplied absolute pointer and read the installed skill body using PowerShell `Get-Content`, without escalation. This establishes shell-based library access, not a Claude Read-rule result. |
| Native skill listing | No `cp-skill-*` skills were exposed in this chat's supplied native skill catalog. This chat began in the source checkout; the observation does not establish installed-project discovery failure. Stub files on disk are not native listing evidence. |
| Index route with an argument | Applied the installed `cp-skill-validate` instructions through the library index, carrying `kb/log.md` as the argument. `commonplace-validate kb/log.md` exited 0: `VALIDATION SUCCESS`, target and scope `kb/log.md`, 1 file analysed, 1 text file, 0 failures and 0 warnings. The file already existed and was empty. No native invocation or harness-managed fork was exercised. |
| Pointer freshness | `commonplace-init --check` exited 0: all 26 entries were `ok` (12 Claude stubs, 12 agent stubs, library pointer and Claude settings). No init repair was run. |
| Tool inventory | The sandboxed `uv tool list` failed opening the tool directory's `.lock` with access denied. An approved escalated retry exited 0 and reported 0.3.3. This was an inventory read, not an installation or upgrade. |

## Limits and side effects

No native Read tool or matched outside-rule control was used. No result about
Claude permissions follows from these shell reads. No fresh installed-project
session, native argument substitution, worker facility, upgrade, or missing-init
case was tested. The current source-session catalog cannot substitute for a
fresh installed-project skill-discovery check.

`git status --short` in the scratch directory failed with “this operation must
be run in a work tree”, so Git could not establish its before/after state.
The probe issued no project-write commands: only reads, help, validation and
init's check mode. No installation, PATH, settings or project files were
intentionally changed. The uv inventory needed an approval; the other delivery
checks ran sandboxed without escalation.

An optional OS query through `Get-CimInstance` was denied; .NET supplied the OS
version instead. `codex --version` returned its version with access-denied
warnings about temporary arg0-directory cleanup and PATH-alias creation. Neither
diagnostic was repaired. The repository's pre-existing untracked `.codex/`
directory was left alone. This report and its README link are the only intended
repository edits; no commit was made.

Command execution, shell library reads, index-based argument handling and pointer
freshness passed for the existing Windows 0.3.3 installation in this session.
Fresh-session native skill discovery remains outside this result's coverage.
