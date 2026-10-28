---
description: Commonplace commands install once per OS user through uv tool, while project environments retain only project and development dependencies
type: reference/types/adr.md
tags: []
status: accepted
---

# 064-Install Commonplace commands as a user-level uv tool

**Status:** accepted  
**Date:** 2026-08-08

**Windows amendment (2026-10-28).** On Windows the uv tool is built over the python.org interpreter: `uv tool install --python <path to python.org python.exe>`, with the commands started through the shims in `INSTALL.md`. Installing that interpreter is a Windows prerequisite with a stated reason, not troubleshooting: Smart App Control decides by reputation, and the uv-managed CPython builds and uv's generated launchers are unsigned. The tool environment's `Scripts\python.exe` is then a copy of python.org's PSF-signed `venvlauncher.exe`, and the stdlib extensions load from the signed install. The layout, the command authority and the editable-install rules above are unchanged. The operator decided this on 2026-10-28.

Evidence: one Windows 11 Home machine with Smart App Control on and Avast, McAfee and Defender registered, 2026-10-28. Positive controls first: Smart App Control blocked one uv launcher, and Avast sandboxed two others on their first run. Over the signed interpreter, about 50 launches through the shims, including each of the 25 commands once, a validation sweep and a 21-module stdlib extension probe, produced no Code Integrity, Defender or Avast record. Over the uv-managed CPython 3.14.9 every command started, but Smart App Control refused 4 of the 21 probed stdlib extensions at load time (`_decimal`, `_asyncio`, `_overlapped`, `pyexpat`; 7 refusals in all). Avast also sandboxed the venv's `python.exe` on its first run. On 2026-10-26 the same machine had refused the uv-managed 3.13.17 outright. A machine with Smart App Control off ran the uv-managed variant without any record.

Alternatives weighed. *uv-managed Python only* keeps uv as the sole prerequisite, but it fails silently: commands start, and `asyncio` or XML parsing fails later, which a user does not read as an install problem. *Signed Python as troubleshooting only* inherits that silent failure, because the user must first recognise the symptom. *A plain `--target` folder over the signed interpreter, without a uv tool* passed the same tests, but it leaves the `uv tool` layout, so `uv tool list`, `commonplace-init` and the health check would not recognise the install. Where antivirus blocks the default tool path, the documented fallback is another `UV_TOOL_DIR`, which keeps the layout. Where the user has no administrator rights for the machine-scope install, the fallback is the uv-managed interpreter with the same shims, with its known limit: commands start, but Smart App Control may refuse stdlib extensions at load time. One free choice is left open: whether the prerequisite should apply only when Smart App Control is on. It applies to every Windows install for now, because Smart App Control's state can change only from on to off, and the signed interpreter costs nothing where it is off.

Limits: the evidence is one machine, observed within one hour. Reputation verdicts vary between runs and over time, so acceptance in ordinary use over days is not yet shown. A later record of Smart App Control or antivirus acting on the signed interpreter, its tool environment or the shims would reopen this amendment. The amendment says nothing about macOS or Linux, which keep uv-managed interpreters.

Operativity: `INSTALL.md` carries it. The Windows prerequisite is in step 1, the Windows install command in step 2, and the shim step, the extension-refusal symptom and the two fallbacks in the Windows troubleshooting section. Installers and agents following the procedure read it at install time.

## Context

ADR 014 installed Commonplace into a project-local venv and used direnv to put that venv's executable directory on `PATH`. That made command discovery depend on shell activation state. Fresh agent tool calls, desktop runtimes, IDE processes, native Windows sessions, and CI jobs do not reliably share the installer shell's environment. The resulting recovery instructions split by platform and runtime even though the installed command set was the same.

The `commonplace-*` entry points are framework operator commands, not project dependency executables. uv already provides an isolated tool environment, a stable user-level executable directory, editable installs, interpreter selection, upgrades, and a CI-friendly tool-bin override. A native Windows experiment run before adoption reported positive fresh-PowerShell and agent-runtime results; the supported test was process restart and bare-name command resolution, not venv activation or one IDE's integrated terminal.

## Decision

Install Commonplace commands once per OS user as a uv tool (`uv tool install`, then `uv tool update-shell`); a source checkout installs as an editable tool. Ordinary source changes flow through the editable install; dependency, entry-point, build-metadata, and packaged-scaffold changes require a reinstall. Exact commands live in `INSTALL.md` and `AGENTS.md`.

The uv tool executable directory is the command authority. `commonplace-*` commands are invoked by bare name in every project. `uv tool update-shell` makes the user-environment change durable, but already-running shells, IDEs, desktop agents, and services must be restarted. One installed Commonplace command version per OS user is an accepted invariant; an editable install therefore changes the commands used by every project for that user.

Project environments retain project and development dependencies. `pytest`, `ruff`, and documentation builders run through `uv run`; `pytest` is no longer a runtime dependency of `llm-commonplace`. Optional command dependencies remain uv-tool extras selected during installation.

`commonplace-init` creates no Commonplace-specific venv or `.envrc`. Its generated control-plane template gives one unconditional bare-name rule. Init diagnostics warn about missing entry points and commands resolving outside uv's tool directory; the health check, not init, inspects legacy or shadowing `.envrc` residue and never deletes it. The health-check skill distinguishes the resulting failure classes.

CI uses the same primitive: jobs install the editable checkout or built wheel with `uv tool install` and verify bare-name commands on native Windows and POSIX runners.

These choices are operative through package metadata, the scaffold manifest and `commonplace-init`, the generated `AGENTS.md.template`, install instructions, the promoted health-check skill, and CI workflow jobs.

## Considered alternatives

**Keep the project-local venv and improve activation instructions.** This preserves per-project Commonplace versions, but activation still changes only one process and its children. Every independent shell, IDE, agent service, and Windows launch path remains a separate propagation problem. More activation branches would document the failure mode rather than remove it.

**Use pip or pipx as an equal installation authority.** Both can expose commands, but equal authorities multiply upgrade, editable-install, interpreter, executable-directory, and CI instructions. uv is already required for this repository's project dependency environment and supplies the needed tool lifecycle in one interface, so the shipped contract has one authority.

**Generate launcher wrappers inside each project.** Wrappers could select a project-specific tool version, but they would add a new dispatcher, platform-specific launcher formats, and another scaffold surface before any incompatible-project case requires simultaneous versions. The one-active-version tradeoff is simpler and accepted until a worked case falsifies it.

**Use `uv run commonplace-*` for framework commands.** This binds command availability back to each project's dependency metadata and environment. It also conflates framework operators with project-only executables. `uv run` remains the authority for development dependencies, not installed Commonplace commands.

The proposal's free choices were resolved as follows: explicit Python `>=3.11`; warning rather than init refusal; report-only legacy cleanup; `pytest` moved to the development group; and user-level single-version semantics accepted. The Windows experiment supported `uv tool update-shell` for the launch classes tested. Support for any additional desktop or IDE runtime remains conditional on a fresh-process check in that runtime.

## Consequences

- Commands survive shell restarts without per-project activation and use the same invocation on POSIX and Windows.
- A newly installed or updated tool is not visible to already-running processes; documentation and diagnostics must require a full restart of the consuming launch class.
- Projects cannot independently pin incompatible Commonplace command versions for one OS user. Switching to an editable checkout affects all of that user's projects.
- A project `.venv` is no longer evidence about Commonplace command health. It may still be required by the project and cannot be removed automatically.
- uv reports executable conflicts instead of silently choosing an owner. Recovery inspects and removes the shadowing authority rather than defaulting to `--force`.
- CI, release smoke tests, local source development, and published installs exercise the same installation primitive.
- Supersedes ADR 014's project-venv and direnv command discovery; ADR 027's package-data model remains.

---

Relevant Notes:

- [Commonplace architecture](../architecture.md) — implemented-by: the installed command and scaffold surfaces
- [Instruction generation](../instruction-generation.md) — implemented-by: the scaffold no longer generates command-environment state
- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — supersedes: project-venv and direnv command discovery
- [027-package-scaffold-assets-without-source-tree-symlinks](./027-package-scaffold-assets-without-source-tree-symlinks.md) — supersedes: `.envrc.template` as an included root template, while retaining explicit package-data inclusion
