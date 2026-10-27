# Native Windows PowerShell probe

- Round: 1
- Procedure ID: `execution-channel-round1-v6-2026-07-28`
- Date: `2026-10-27`
- Runtime/surface: Codex desktop tool-call execution
- Operating system/interface: Windows / PowerShell
- Prior related report: none for native Windows; contrasts with the POSIX reports in this directory

## Layout and environment

| Observation | Result | Status |
|---|---|---|
| `pyproject.toml` at workspace root | present | observed |
| `kb/instructions/COLLECTION.md` | present | observed |
| `kb/commonplace/instructions/COLLECTION.md` | absent | observed |
| project `.venv` | present | observed |
| workspace `.envrc` | present | observed |
| project `.venv\Scripts` exact entry in effective `PATH` | false | observed |
| `VIRTUAL_ENV` | unset | observed |
| direnv marker variables | all unset | observed |

Provisional layout class: Commonplace source-like checkout with a project venv. The workspace is not treated as an installation verdict.

## Universal bare-name probes

| Command | Result | Resolution |
|---|---|---|
| `commonplace-validate --help` | exit 0; bounded help output | succeeded |
| `rg --version` | exit 0; ripgrep 15.2.0 with PCRE2 | succeeded |

## Command resolution

| Name | Kind | Source |
|---|---|---|
| `commonplace-validate` | Application | `<USER-LOCAL>\\.local\\bin\\commonplace-validate.exe` |
| `rg` | Application | `<CODEX>\\bin\\rg.exe` |

Expected project entry point `.venv\\Scripts\\commonplace-validate.exe`: present.

## Shell-state persistence

PowerShell call A created the process-local environment variable `COMMONPLACE_SHELL_PROBE=present` and a process-local function. Call B observed both absent. Separate tool calls do not preserve shell mutations. PID and working directory were not used as persistence evidence.

## Fixture-backed behavior

`rg -n -m 1 --glob '*.md' '^# ' kb\\instructions` succeeded and returned a heading from the observed instruction root.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| Codex CLI launched from a prepared parent environment | this run used the desktop tool-call interface, not a separately launched CLI comparison |
| Windows `cmd.exe` state probe | no `cmd.exe` execution interface was used |
| second project/worktree isolation | no second prepared project was available in this probe |
| Codex desktop local-environment handoff | this probe observes the current channel only; it does not change or inspect app configuration |
| workflow-specific behavioral checks | no exact live instruction and safe fixture were established for each tool |

## Disclosure attestation

Workspace, user-local, and runtime installation prefixes were normalized. No environment dump, profile content, direnv marker value, function definition, unrestricted Git status, credential, or secret-scanner match was retained.
