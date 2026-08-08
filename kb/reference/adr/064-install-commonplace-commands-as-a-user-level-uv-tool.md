---
description: Commonplace commands install once per OS user through uv tool, while project environments retain only project and development dependencies
type: ../types/adr.md
tags: []
status: accepted
---

# 064-Install Commonplace commands as a user-level uv tool

**Status:** accepted  
**Date:** 2026-08-08

## Context

ADR 014 installed Commonplace into a project-local venv and used direnv to put that venv's executable directory on `PATH`. That made command discovery depend on shell activation state. Fresh agent tool calls, desktop runtimes, IDE processes, native Windows sessions, and CI jobs do not reliably share the installer shell's environment. The resulting recovery instructions split by platform and runtime even though the installed command set was the same.

The `commonplace-*` entry points are framework operator commands, not project dependency executables. uv already provides an isolated tool environment, a stable user-level executable directory, editable installs, interpreter selection, upgrades, and a CI-friendly tool-bin override. A native Windows experiment run before adoption reported positive fresh-PowerShell and agent-runtime results; the supported test was process restart and bare-name command resolution, not venv activation or one IDE's integrated terminal.

## Decision

Install published commands with:

```text
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

Install a source checkout with `uv tool install --python ">=3.11" --editable .`. Ordinary source changes flow through the editable install; dependency, entry-point, build-metadata, and packaged-scaffold changes require `uv tool install --reinstall --python ">=3.11" --editable .` so uv refreshes the existing environment.

The uv tool executable directory is the command authority. `commonplace-*` commands are invoked by bare name in every project. `uv tool update-shell` makes the user-environment change durable, but already-running shells, IDEs, desktop agents, and services must be restarted. One installed Commonplace command version per OS user is an accepted invariant; an editable install therefore changes the commands used by every project for that user.

Project environments retain project and development dependencies. `pytest`, `ruff`, and documentation builders run through `uv run`; `pytest` is no longer a runtime dependency of `llm-commonplace`. Optional command dependencies remain uv-tool extras selected during installation.

`commonplace-init` creates no Commonplace-specific venv or `.envrc`. Its generated control-plane template gives one unconditional bare-name rule. Init diagnostics warn about missing declared entry points, commands resolving outside uv's tool directory, the exact legacy generated `.envrc`, and edited `.envrc` files that may shadow the tool. They never delete residue. The health-check skill distinguishes package absence, missing tool-directory `PATH`, executable shadowing, incomplete installation, legacy residue, and runtime-specific environment propagation.

GitHub Actions uses the same primitive. Jobs configure a job-local uv tool executable directory, append it to `$GITHUB_PATH`, install either the editable checkout or built wheel with `uv tool install`, and verify commands in later steps. Wheel smoke tests enumerate every declared entry point and initialize and validate a temporary project on native Windows and POSIX runners.

These choices are operative through package metadata, the scaffold manifest and init command, generated `AGENTS.md.template`, contributor and install instructions, the promoted health-check skill, and GitHub workflow jobs. Package installation and `commonplace-init` deploy the behavior to consumers; source agents load the root instructions directly; CI enforces the release path on each run.

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
- ADR 014's project-venv and direnv command-discovery choice is superseded. ADR 027's explicit package-data model remains, with `.envrc.template` removed from its included root templates.

---

Relevant Notes:

- [Commonplace architecture](../architecture.md) — implemented-by: the installed command and scaffold surfaces
- [Instruction generation](../instruction-generation.md) — implemented-by: the scaffold no longer generates command-environment state
- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — supersedes: project-venv and direnv command discovery
- [027-package-scaffold-assets-without-source-tree-symlinks](./027-package-scaffold-assets-without-source-tree-symlinks.md) — supersedes: `.envrc.template` as an included root template, while retaining explicit package-data inclusion
