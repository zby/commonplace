---
description: "Proposal: replace project-activated Commonplace command environments with one user-level uv tool installation, using the same editable tool model for source work and fresh-process PATH verification"
type: ../types/design-proposal.md
traits: [has-external-sources]
tags: [architecture]
---

# User-level uv tool installation for Commonplace commands

## Current state (as of 2026-08-08)

The `llm-commonplace` 0.1.4 package declares 22 `commonplace-*` console entry points. The full-install guide nevertheless installs the package into each consuming project's `.venv`, then depends on activation or a generated `.envrc` to put that environment's command directory on `PATH`. The source checkout uses the same project environment. Native Windows cannot rely on the documented direnv path, so its source-checkout instructions carry activation, `.venv\Scripts`, and explicit `.exe` fallbacks.

This separates successful package installation from successful command discovery. A shell may contain the executables while an agent process cannot resolve them; a desktop runtime may not inherit the shell that activated the environment; and each consuming project must prepare a Python environment even though Commonplace exposes an application command surface rather than an import dependency for that project's code.

uv has a separate tool-installation model for this case. `uv tool install` creates an isolated user-level tool environment and exposes every executable supplied by the target package through one tool executable directory. `uv tool update-shell` adds that directory to common shell configuration files, and `uv tool install --editable <directory>` makes ordinary source changes visible without reinstalling. uv does not expose executables supplied only by dependencies, so source-only tools such as `pytest` and `ruff` need their own invocation path.

The repository's GitHub Actions surface is currently the Pages workflow. It installs `.[docs]` with pip and invokes `properdocs`, an executable supplied by a dependency rather than by `llm-commonplace`. GitHub Actions can nevertheless exercise the same Commonplace tool installation as users: the official `astral-sh/setup-uv` action installs uv and accepts an explicit tool executable directory, while `$GITHUB_PATH` publishes that directory to later workflow steps. Commands not supplied by `llm-commonplace`, including `properdocs`, remain project-environment commands run through `uv run`.

The current uv documentation warrants shell configuration, not command visibility inside every independently launched desktop or IDE agent process. Native Windows runtime inheritance therefore remains an evidence gate. It must not be inferred from success in the PowerShell process that ran the installer.

A separately reported editable-install failure occurred while pip tried to download Hatchling through a proxy value containing spaces. That is an invalid proxy configuration, not a command-PATH failure. A published wheel installed as a uv tool avoids that particular editable build, but this proposal does not claim to repair proxy configuration or guarantee offline installation.

## Problem

Commonplace currently assigns one responsibility to three mechanisms:

- Python packaging creates the commands.
- A project venv chooses which package instance owns them.
- activation or direnv makes them discoverable to later processes.

The third mechanism is the weak link. It depends on shell hooks and launch inheritance outside Commonplace's control, and its fallback differs between POSIX and Windows. The project-level isolation bought by the second mechanism also has a cost: every KB has setup state unrelated to its Markdown content, while an agent working across projects can inherit whichever venv happened to prepare its launcher.

The source checkout adds another branch. Contributors need the commands to follow source edits, but that requirement currently selects a different install procedure rather than a development form of the same tool procedure.

The design target is one answer to “where do `commonplace-*` commands come from?” across published and source installations. It should preserve bare command names, work without shell activation, make all package entry points appear together, and fail visibly when a fresh process cannot resolve them.

## Option space

### A. One user-level uv tool, editable for source work

Install a published release as a user-level tool:

```text
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

Install a source checkout into the same tool slot with one changed flag:

```text
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

Ordinary Python and canonical scaffold-file edits then take effect without reinstalling. Changes to dependencies, entry-point metadata, or the build/install configuration require the editable install to be rerun. Reinstalling `llm-commonplace` from the package index replaces the editable checkout.

This is the leading option because it makes release and development differ only in the package source. Its accepted cost would be one active Commonplace tool version per OS user: installing an editable checkout also makes that checkout serve commands invoked in other KB projects.

### B. Keep project-local venvs and add native launch instructions

Retain version selection per project and document activation or launcher-specific environment propagation for every supported runtime. This preserves project pins but leaves the forcing failure intact for desktop applications and fresh agent processes that do not inherit the prepared shell. It also retains different POSIX and Windows recovery paths.

### C. Keep project-local venvs and require explicit executable paths

Avoid `PATH` entirely by making every instruction invoke `.venv/bin/commonplace-*` or `.venv\Scripts\commonplace-*.exe`. This is deterministic inside a known checkout, but it makes every executable instruction platform-dependent and couples the installed KB layout to Python's venv layout.

### D. Add a Commonplace-owned dispatcher or runtime integration

Install a stable global command that locates a project environment, or teach each agent runtime how to inject the right project command directory. This could preserve per-project versions, but it introduces a new resolution layer or runtime-specific integrations before a demonstrated need for simultaneous incompatible Commonplace versions.

## Candidate design under option A

The uv tool environment becomes the installation authority for all `commonplace-*` commands. A consuming KB contains Commonplace content, skills, and operational state, but no package venv and no `.envrc` generated by `commonplace-init`. Commands continue to derive their working project from their arguments and current working directory.

`uv tool update-shell` is a one-time user setup step, followed by restarting the relevant shell, IDE, and agent runtime. Installation is not considered healthy merely because the command works in the installer process. A fresh-process check must resolve every Commonplace entry point declared by the installed distribution. `commonplace-init` and `cp-skill-health-check` may report that evidence and the repair command, but neither can retroactively change its parent process's environment.

The source checkout uses the editable form of the same tool installation. Developer-only commands run through the uv project environment, for example `uv run pytest` and `uv run ruff check`. That environment may still be materialized as `.venv`, but it is test/dependency state managed by uv, not the command-discovery contract, and nobody activates it.

GitHub Actions uses the same tool installation rather than a CI-specific package procedure. A workflow installs uv with a pinned `astral-sh/setup-uv` action, selects a job-local tool executable directory, publishes that directory through `$GITHUB_PATH`, and then runs `uv tool install`. Source-installation checks use `--editable .`; release smoke tests install the built wheel. A later step invokes the installed `commonplace-*` commands by bare name, so the workflow tests both entry-point materialization and process-to-process PATH publication. Project-only and dependency executables such as `pytest`, `ruff`, and `properdocs` continue to run through `uv run`.

Published upgrades use `uv tool upgrade llm-commonplace`. Source metadata or dependency changes rerun the editable install. A release smoke test replaces the editable tool with the built wheel, verifies it, and may then restore the editable install for continued development.

Existing consumer `.envrc` and `.venv` artifacts are migration residue. A new init run must not silently delete them under the existing non-destructive scaffold contract. The migration should identify an unchanged generated `.envrc` as removable and warn when it can still shadow the user-level tool; edited files remain entirely user-owned.

## Forces and consequences

**Cross-platform command spelling.** uv installs the target package's executable set on Linux, macOS, and Windows. This removes the `.venv/bin` versus `.venv\Scripts` branch from Commonplace command calls. It does not make Bash-shaped instruction bodies portable; that remains the concern of [channel-compiled instruction artifacts](./channel-compiled-instruction-artifacts.md).

**Process inheritance.** A persistent tool directory is a better baseline than an activated project shell, but configuration written for a shell may still not reach a desktop application. The design needs native fresh-process evidence, especially on Windows, before claiming universal command discovery.

**Version isolation.** One tool slot is simpler than one environment per KB, but projects can no longer select different Commonplace versions merely by entering different directories. The source editable install also affects all local projects. This is acceptable only if Commonplace continues to prefer one current runtime over project-specific backwards compatibility.

**Entry-point completeness.** uv exposes all executables supplied by `llm-commonplace` together, which matches the package's command-family boundary. It does not expose dependency executables such as `pytest`; active instructions must stop treating those as part of the installed consumer command surface.

**Shell mutation.** `uv tool update-shell` changes user shell configuration. The install guide must say so, make the step explicit, and give `uv tool dir --bin` as the diagnostic source of truth. Non-interactive automation needs a process-scoped way to add that directory instead of mutating a profile.

**Ephemeral automation.** CI does not need a different installation primitive merely because its filesystem is temporary. It needs a channel-specific way to carry the selected tool executable directory into later steps. GitHub Actions supplies that channel through `$GITHUB_PATH`; it must not run `uv tool update-shell` or infer success from the installation step alone.

**Executable conflicts.** uv refuses to overwrite executables it does not own unless forced. The migration must diagnose a conflicting pipx, pip, or manual installation rather than recommending `--force` by default.

**Build isolation and proxies.** Published wheels reduce local build requirements for ordinary installs. Editable source installs still need their declared build backend, and every networked install still depends on valid index and proxy configuration.

## Operativity

For published installations, `INSTALL.md` directs the operator through the uv tool channel; uv materializes the package entry points and updates shell configuration; a newly launched shell, IDE, or agent process consumes the resulting `PATH` with ordinary executable-lookup force.

For source work, root `AGENTS.md` and contributor documentation direct the operator to the editable variant. uv's editable installation redirects the same package commands to checkout source, while `uv run` supplies project-only test and development dependencies.

For GitHub Actions, the workflow installs uv, publishes a job-local uv tool executable directory through `$GITHUB_PATH`, and installs either the editable checkout or built wheel with `uv tool install`. Later steps consume bare `commonplace-*` names with ordinary executable-lookup force. The Pages build consumes `properdocs` through `uv run --extra docs`, because dependency executables are outside the Commonplace command-family contract.

For initialized projects, the generated control-plane template tells agents to use bare `commonplace-*` names without a venv branch. `commonplace-init` and `cp-skill-health-check` inspect the current process's entry-point resolution and report missing names. That check is warranted only for the process in which it runs; it cannot establish that a different desktop launcher inherits the same environment.

## Native Windows confirmation experiment

This experiment decides the native Windows runtime evidence gate for option A. Run it from a clean checkout in native Windows PowerShell, not WSL. It changes durable user state: the editable install replaces any existing `llm-commonplace` uv tool, and `uv tool update-shell` changes supported shell configuration. Use a test Windows user or record `uv tool list` first and be prepared to restore the prior installation.

### Install from the checkout

From the repository root, record the baseline and install the checkout:

```powershell
git status --short
git rev-parse HEAD
uv --version
uv tool list
uv tool install --python ">=3.11" --editable .
uv tool update-shell
uv tool dir
uv tool dir --bin
```

The checkout must be clean before the experiment. Save the commit ID, uv version, pre-install tool list, and both reported directories. Fully close PowerShell, Windows Terminal, and every desktop or IDE runtime that will be tested, including background, tray, and helper processes. Launching another tab or window inside an existing process is not a fresh-process test.

### Verify from an independent PowerShell process

Launch PowerShell independently from the Windows Start menu. Do not activate a venv or run any project setup. From the repository root, run:

```powershell
$toolBin = [IO.Path]::GetFullPath((uv tool dir --bin).Trim())
$commands = @(
    Get-Content pyproject.toml |
        Select-String '^commonplace-[A-Za-z0-9-]+\s*=' |
        ForEach-Object { ($_.Line -split '\s*=')[0].Trim() }
)

$missing = @()
$outsideToolBin = @()
foreach ($name in $commands) {
    $hit = Get-Command $name -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($null -eq $hit) {
        $missing += $name
        continue
    }
    $actualBin = [IO.Path]::GetFullPath((Split-Path -Parent $hit.Source))
    if ($actualBin -ne $toolBin) {
        $outsideToolBin += [ordered]@{ name = $name; source = $hit.Source }
    }
}

& commonplace-validate --help *> $null
$helpExit = $LASTEXITCODE
$result = [ordered]@{
    timestamp = (Get-Date).ToString('o')
    commit = (git rev-parse HEAD)
    windows = [Environment]::OSVersion.VersionString
    powershell = $PSVersionTable.PSVersion.ToString()
    uv = (uv --version)
    tool_dir = (uv tool dir)
    tool_bin = $toolBin
    command_count = $commands.Count
    missing = $missing
    outside_tool_bin = $outsideToolBin
    validate_help_exit = $helpExit
}
$evidence = Join-Path $env:TEMP 'commonplace-windows-uv-tool-powershell.json'
$result | ConvertTo-Json -Depth 4 | Tee-Object -FilePath $evidence
Write-Host "Evidence: $evidence"

if ($commands.Count -eq 0 -or $missing.Count -ne 0 -or
    $outsideToolBin.Count -ne 0 -or $helpExit -ne 0) {
    throw 'Commonplace uv tool verification failed.'
}
```

This stage passes when the command count is 22 for the pinned current state, `missing` and `outside_tool_bin` are empty, and `validate_help_exit` is `0`. A command resolving outside `uv tool dir --bin` is a shadowing failure even if it runs.

### Verify each desktop and IDE agent runtime

List every Windows desktop application and IDE agent runtime the support claim is intended to cover. For each one, record the product and version, terminate all of its processes, relaunch it through its normal Windows launcher rather than from the verified PowerShell, open this checkout, and give its agent this read-only request:

```text
Do not change files, activate a venv, use WSL, or substitute an IDE-integrated
terminal for the agent command runner. In the agent's native Windows execution
environment, report $PSVersionTable.PSVersion, run `uv tool dir --bin`, run
`(Get-Command commonplace-validate -CommandType Application).Source`, and run
`commonplace-validate --help`. Return the exact paths and exit status. If the
agent cannot run native PowerShell, report its actual execution environment
instead of substituting another consumer's result.
```

Repeat the commands in an IDE's integrated terminal only as a separately labelled diagnostic. An integrated-terminal pass does not establish that the IDE's agent subprocess received the same environment.

Record one row per consumer, not merely one row per product:

| Runtime and version | Launch route | Consumer | Native Windows or WSL | `uv tool dir --bin` | Resolved command | Help exit | Result |
|---|---|---|---|---|---|---:|---|
| `<product version>` | `<Start menu/taskbar/etc.>` | `agent` or `integrated terminal` | `<environment>` | `<path>` | `<path>` | `<code>` | `pass` or `fail` |

An agent row passes only when its command runner is native Windows PowerShell, resolves `commonplace-validate` from the same directory reported by `uv tool dir --bin`, and receives exit status `0`. Preserve every agent's exact output with the PowerShell JSON result. The evidence supports only the named runtime versions and launch routes actually tested.

### Interpret the result

- **PowerShell and every claimed agent runtime pass:** option A has evidence for durable command discovery on the named Windows configurations.
- **PowerShell passes but an agent runtime fails:** uv tool installation works, but `uv tool update-shell` is not a sufficient PATH authority for that runtime. Add and test a supported runtime-specific mechanism or exclude that launch class from the support claim.
- **Only an integrated terminal passes:** the IDE agent remains unverified; terminal inheritance cannot substitute for agent-process evidence.
- **PowerShell fails:** diagnose PATH publication, executable conflicts, or installation failure before drawing conclusions about any desktop or IDE runtime.
- **A runtime uses WSL:** record it as a separate WSL launch class; it says nothing about native Windows inheritance.

## Adoption plan

This sequence applies only after the proposal is accepted. Each phase has an exit condition so documentation cannot outrun observed behavior.

1. **Prove the installation primitive.** Install a built wheel into isolated uv tool directories on Linux and native Windows. Verify that all 22 declared entry points resolve and that representative commands run. Install the checkout editably, change one command implementation and one canonical scaffold input, and verify both changes are observed without reinstalling. Add a GitHub Actions check that installs uv, publishes a job-local tool executable directory through `$GITHUB_PATH`, installs the checkout editably, and resolves the command family by bare name in a later step. Exit when the published, editable, and GitHub Actions cases pass.
2. **Prove fresh-process visibility.** Run the supported shell update, close the installer process, and test from new Bash/zsh and PowerShell processes. On native Windows, run the [confirmation experiment](#native-windows-confirmation-experiment) in every desktop and IDE agent runtime the support claim will name. If a runtime's agent process cannot resolve the tool directory, option A is incomplete for that launch class until a supported environment mechanism is added or the support claim is narrowed. Exit only with retained evidence for each claimed launch class.
3. **Change the installation and development contracts together.** Make uv tool installation canonical in the full-install guide and editable uv tool installation canonical in source instructions. Move source-only verification and dependency executables, including the Pages build's `properdocs`, to `uv run`. Stop generating `.envrc` and remove activation, direnv, project-command-directory, and `.exe` fallback branches from active instructions. Exit when no active install or command instruction contradicts the new authority.
4. **Change scaffold and recovery behavior.** Remove `.envrc` from the scaffold/package manifest, make generated control-plane instructions unconditional, and teach init-time and health-check diagnostics to distinguish a missing tool, a missing tool-directory `PATH` entry, an executable conflict, and legacy project-environment residue. Exit when a fresh initialized project contains no command-environment setup state and the recovery message is platform-neutral.
5. **Migrate and release.** Document replacement of project-local installs, non-destructive cleanup of legacy `.envrc`/`.venv` artifacts, switching between published and editable tools, upgrades, optional extras, and automation setup. Build the release artifacts; install the wheel as a uv tool in clean POSIX and Windows environments and in GitHub Actions; enumerate all entry points; initialize and validate a temporary project; then run the full software suite. Exit when the release checklist exercises the same install path users are told to follow.

If adopted, the implemented decision should become an ADR that revises ADR 014's project-venv and direnv choice. This proposal then leaves the live frontier under the proposal-archive procedure.

## Free choices

- **Desktop and IDE PATH authority.** Whether `uv tool update-shell` alone reaches each supported native Windows agent runtime, or separate documented environment steps are required. Decided per launch class by fresh-process evidence, not shell or integrated-terminal success.
- **Global version policy.** Whether one active version per OS user is an accepted Commonplace invariant or whether a demonstrated incompatible-project case requires a dispatcher or namespaced tool slot.
- **Python request.** Whether installation fixes `--python ">=3.11"` explicitly or relies on uv selecting an interpreter compatible with package metadata.
- **Diagnostic force.** Whether `commonplace-init` merely warns when some entry points are absent or refuses to report a healthy initialization.
- **Legacy residue.** Whether an exactly matching generated `.envrc` is only reported or may be removed with explicit operator consent; edited files cannot be removed automatically.
- **Development dependencies.** Whether `pytest` remains a runtime dependency of the published package or moves entirely into the development group once consumer command instructions stop relying on its executable.

## Adoption criteria

- Every `[project.scripts]` entry resolves by bare name in fresh supported processes after the documented install, including a retained native Windows PowerShell result.
- Each native Windows desktop or IDE agent claim is demonstrated after a true process restart or explicitly excluded; PowerShell and integrated-terminal inheritance are not substituted as agent-process evidence.
- An editable source install observes ordinary Python and scaffold changes without reinstalling, while metadata/dependency reinstall boundaries are documented and tested.
- A clean initialized KB contains neither `.venv` nor `.envrc` as command-discovery requirements.
- No active instruction requires activation, direnv, `uv run commonplace-*`, or platform-specific venv executable paths.
- A wheel-installed smoke test initializes and validates a temporary project on POSIX and native Windows before publication.
- GitHub Actions installs the editable checkout and the built wheel through `uv tool install`, publishes the tool executable directory without mutating a shell profile, and resolves all package entry points by bare name in a later step.
- The one-active-version consequence and the editable-checkout effect on other projects are prominent in contributor documentation.
- Invalid proxy configuration, optional external tools, and shell-language portability are described as separate problems rather than credited to this change.

## Out of scope

- Reader installs, which use the vendored Markdown KB and no Python commands.
- Making non-Python tools such as `rg`, Git, or shell utilities universally available.
- Translating Bash-shaped skills or instructions into PowerShell.
- Repairing corporate proxy URLs, certificates, credentials, or offline package indexes.
- Supporting simultaneous incompatible Commonplace versions without a worked case that requires them.

---

Relevant Notes:

- [ADR 014 — Scripts as Python package, one-tree model](../adr/014-scripts-as-python-package-one-tree-model.md) — compares-with: retains its package entry points while revisiting its project-venv and direnv command-environment choice
- [Channel-compiled instruction artifacts](./channel-compiled-instruction-artifacts.md) — compares-with: separates package command discovery from the wider unresolved problem of shell-shaped executable instructions
- [Instruction generation](../instruction-generation.md) — compares-with: current scaffold pipeline whose `.envrc` output and command guidance would change under option A
- [Operative change](../../notes/definitions/operative-change.md) — rests-on: frames the install docs, uv tool directory, process environment, and command lookup as the consumer/channel/force path that must actually operate
- [uv tools](https://docs.astral.sh/uv/concepts/tools/) — evidenced-by: target-package executable exposure, tool-directory PATH behavior, dependency-executable exclusion, and upgrade semantics
- [uv CLI reference](https://docs.astral.sh/uv/reference/cli/) — evidenced-by: editable tool installation, `update-shell`, `--python`, and `uv tool dir --bin` behavior
- [Using uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/) — evidenced-by: the supported GitHub Actions installation path for uv and source-project execution through `uv run`
- [setup-uv environment and tools](https://github.com/astral-sh/setup-uv/blob/main/docs/environment-and-tools.md) — evidenced-by: explicit uv tool and tool-executable directories and GitHub Actions environment propagation
