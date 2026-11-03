# Windows Claude default-permission and delivery check (2026-11-03)

## Purpose

Run the handoff's [ready-to-run Claude check](./windows-delivery-handoff.md#ready-to-run-claude-permission-and-delivery-check). It separates working installed-project delivery from evidence that init's `Read(//<library root>/**)` allow rule controls access.

## Setup

- Machine: Windows 11 Home 10.0.26300, Smart App Control on. Installation: `llm-commonplace` 0.3.3 from PyPI with Workjig 0.3.1, over python.org 3.14.7, with the `INSTALL.md` shims ([Workjig report](./results-2026-11-03-windows-workjig-031-recovery.md)).
- Project: the existing scratch project `<HOME>\cp-install-test-pypi033`, not the checkout.
- Probe session: a new Claude Code desktop-app session rooted in that project, `claude-opus-5-5`, effort medium. The maintainer's session started it through the app's session tool with `permission_mode: default`. The app's session metadata reports `permissionMode: "default"`; the probe could not see the on-screen indicator. No earlier turns.
- The prompt was the handoff's prompt unchanged, with the control path filled in. The control file was a new one-line file in `%LOCALAPPDATA%\Temp`, outside the project and the library.
- Grants observed: the project's `.claude/settings.local.json` holds only init's library rule; no deny rules or additional directories. No user-level `~\.claude\settings.json` exists. Managed and app-level policy were not observable. The app added one extra working directory, a shared notes folder, to the session.

## Results

| Check | Outcome |
|---|---|
| A. Native Read of `<library>/instructions/cp-skill-validate/SKILL.md` | Content returned, no denial. |
| B. Native Read of the control file | Content returned, no denial. |
| C. `Get-Command commonplace-validate`, `--help` | Resolved to `<HOME>\.local\commonplace-shims\commonplace-validate.cmd`; `--help` exit 0. |
| D. Native skill listing | The harness's own skill list showed all 12 `cp-skill-*` skills, independently of the stub files on disk. |
| E. Native `cp-skill-validate` with `kb/log.md` | Invoked through the Skill tool, no slash command needed. It ran in a harness-managed fork and reported `VALIDATION SUCCESS`, target `kb/log.md`, 0 failures, 0 warnings. The fork's exit status and read trace are not visible. |
| F. `commonplace-init --check` | Exit 0; all 26 entries `ok`. `uv tool list`: `llm-commonplace v0.3.3`. |

No tool call returned a denial. The probe cannot see permission prompts; a cancelled prompt would have made A or B fail, and both returned content. Whether the operator saw any prompt was not recorded. No settings or project files changed; `git status` matched the starting state.

## Interpretation

Both reads succeeded without a prompt, so by the handoff's rule: **library access and installed-project delivery work, but the read rule's effect is unestablished.** In this setup a default-mode Claude Code session read a file in `%LOCALAPPDATA%\Temp` that no observed rule covers. Whatever allows that also allows library reads, so this run cannot attribute the library read to init's rule. A matched rule-on/rule-off test in a disposable project needs separate operator authorization; it was not run.

Delivery checks C–F pass in a default-permission session rooted in an installed project. That extends the [2026-10-31 installed-project report](./results-2026-10-31-windows-installed-project-agents.md) to the PyPI 0.3.3 installation.

## Not covered

- What allows the outside-rule read: an app default, a managed policy, or the Read tool's own scope. Not observable from the session.
- The fork's read trace in E: its summary does not show that it read the library `SKILL.md`.

The control file `C:\Users\zzbby\AppData\Local\Temp\commonplace-read-control-81f1abe694644e82812be941abb54735.txt` was left in place; the operator may delete it.
