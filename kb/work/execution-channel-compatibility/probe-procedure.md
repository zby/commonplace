---
description: "Use to gather an initial, comparable execution-capability report from any environment in which Commonplace is read or operated"
type: kb/types/instruction.md
---

# Probe the current Commonplace execution environment

## Outcome

Produce one evidence report describing what the current agent can actually execute. This is reconnaissance across the environments in which Commonplace can be used, not a pass/fail installation test. A missing project venv is expected in a reader install; a missing Git checkout is expected in some packaged or copied installations; and a tool that cannot be tested remains `unknown` rather than failed.

This instruction is the Round 1 breadth probe. Run it unchanged so reports remain comparable. Later rounds may repeat an environment with narrower, deeper tests selected from the gaps in the first reports; they create new reports rather than editing the baseline.

Procedure ID: `execution-channel-round1-v4-2026-07-28`.

The first constraint is implementability: run a check only after its prerequisites are available in the current environment. Do not assume the agent is in the Commonplace source checkout, has Git metadata, can see a project root, uses Bash, can write files, or can launch a second session. Record a skipped check and its missing prerequisite instead of inventing a substitute.

## Boundaries

This is an observational procedure. Do not make the environment pass:

- do not activate a venv or modify `PATH`;
- do not install, upgrade, or repair tools;
- do not edit profiles, hooks, runtime settings, execution policies, or project files;
- do not switch to an explicit venv executable after a bare command fails;
- do not request broader permissions solely to complete or save the probe;
- do not recursively search outside the workspace to find a Commonplace installation.

The procedure may set the uniquely named `COMMONPLACE_SHELL_PROBE` variable and shell function in one tool process to test persistence. Remove them in the second call when they persist.

Except for that deliberate persistence test, every command block must be self-contained. Recompute working paths and shell variables inside each tool call; never depend on a variable assigned by an earlier block.

## Invocation brief

Give another agent this instruction by a path it can already read, or paste the instruction into its task:

> Probe the currently open environment using the execution-channel procedure. Treat source checkouts, initialized full projects, reader/vendor installs, package-only environments, and unrecognized layouts as valid observations. Run only checks whose prerequisites you first establish. Do not activate, install, repair, reconfigure, or broaden permissions. Return a completed evidence report; save it under the workshop evidence directory only if that path already exists and is writable within your normal scope.

An agent does not need access to this workshop repository to perform the probe. If it cannot write here, its response is the evidence artifact for an operator to copy later.

## 1. Identify the survey run

Record:

- round: `1 — landscape breadth`;
- procedure ID: `execution-channel-round1-v4-2026-07-28`;
- any prior related report, otherwise `none`.

## 2. Record identity from available runtime facts

Record the following without adding a new command merely to fill a field:

- UTC date and local timezone, if exposed;
- agent product, surface, and version, if exposed;
- OS and version, if exposed;
- execution interface used by tool calls: PowerShell, POSIX shell, `cmd.exe`, direct process execution, remote service, or unknown;
- workspace path supplied by the runtime, or the current directory if no workspace concept is exposed;
- launch path, sandbox/approval mode, and write scope, when visible to the agent.

Mark unavailable facts `unknown`. Do not infer the tool-call shell from an integrated-terminal preference.

## 3. Classify only the layout that is observable

Use the runtime's workspace root when it exposes one; otherwise use the current tool-call directory. Test only paths relative to that root.

| Observed path or fact | Provisional class |
|---|---|
| `pyproject.toml` and `kb/instructions/COLLECTION.md` | Commonplace source-like checkout |
| `kb/commonplace/instructions/COLLECTION.md` | initialized full project-like layout |
| a Commonplace vendor path named by loaded project instructions | reader/vendor layout |
| bare `commonplace-*` command but no visible Commonplace content tree | package-only or externally managed layout |
| none of the above | other/unknown |

These are observational labels, not installation verdicts. If the current directory is below the workspace root and the runtime does not expose that root, record `workspace root unknown`; do not search arbitrary ancestors or the filesystem.

PowerShell can inspect the two conventional roots with built-in facilities:

```powershell
$WorkspaceRoot = (Get-Location).Path
[pscustomobject]@{
  WorkspaceRoot = $WorkspaceRoot
  SourceManifest = Test-Path (Join-Path $WorkspaceRoot 'pyproject.toml')
  SourceInstructions = Test-Path (Join-Path $WorkspaceRoot 'kb\instructions\COLLECTION.md')
  InstalledInstructions = Test-Path (Join-Path $WorkspaceRoot 'kb\commonplace\instructions\COLLECTION.md')
  ProjectVenvDirectory = Test-Path (Join-Path $WorkspaceRoot '.venv')
  WorkspaceEnvrc = Test-Path (Join-Path $WorkspaceRoot '.envrc')
}
```

POSIX shells can inspect the same roots with shell built-ins:

```sh
workspace_root=$PWD
for candidate in pyproject.toml kb/instructions/COLLECTION.md kb/commonplace/instructions/COLLECTION.md .venv .envrc; do
  if [ -e "$workspace_root/$candidate" ]; then
    printf 'present=%s\n' "$candidate"
  else
    printf 'absent=%s\n' "$candidate"
  fi
done
```

For `cmd.exe`, use `cd` to record the current directory and `if exist <relative-path> (...)` for the same four paths. For a direct-process interface with no shell expressions, use any runtime-provided file inspection capability; otherwise leave layout classification `unknown`.

If a loaded project instruction names a different reader/vendor path, record that path and whether it is readable. Do not require it to match either conventional root.

### Record only environment signals relevant to the project venv

If a project `.venv` was observed at the workspace root, record whether its platform-specific command directory is an exact entry in the effective process `PATH`, plus the value of `VIRTUAL_ENV`. Do not print the full `PATH`.

PowerShell:

```powershell
$WorkspaceRoot = (Get-Location).Path
$VenvScripts = (Join-Path $WorkspaceRoot '.venv\Scripts').TrimEnd('\')
$PathEntries = @($env:PATH -split [IO.Path]::PathSeparator)
[pscustomobject]@{
  ProjectVenvCommandDirectory = $VenvScripts
  ProjectVenvOnPath = [bool]($PathEntries | Where-Object { $_.TrimEnd('\') -ieq $VenvScripts })
  VirtualEnv = $env:VIRTUAL_ENV
  VirtualEnvMatchesProject = ($env:VIRTUAL_ENV -and (([string]$env:VIRTUAL_ENV).TrimEnd('\') -ieq (Join-Path $WorkspaceRoot '.venv').TrimEnd('\')))
  DirenvDirSet = [bool]$env:DIRENV_DIR
  DirenvFileSet = [bool]$env:DIRENV_FILE
  DirenvDiffSet = [bool]$env:DIRENV_DIFF
  DirenvWatchesSet = [bool]$env:DIRENV_WATCHES
}
```

POSIX shell:

```sh
workspace_root=$PWD
printf 'project_venv_command_directory=%s\n' "$workspace_root/.venv/bin"
case ":${PATH:-}:" in
  *":$workspace_root/.venv/bin:"*) printf 'project_venv_on_path=true\n' ;;
  *) printf 'project_venv_on_path=false\n' ;;
esac
printf 'VIRTUAL_ENV=%s\n' "${VIRTUAL_ENV:-}"
if [ "${VIRTUAL_ENV:-}" = "$workspace_root/.venv" ]; then
  printf 'virtual_env_matches_project=true\n'
else
  printf 'virtual_env_matches_project=false\n'
fi
if [ -n "${DIRENV_DIR:-}" ]; then printf 'DIRENV_DIR_set=true\n'; else printf 'DIRENV_DIR_set=false\n'; fi
if [ -n "${DIRENV_FILE:-}" ]; then printf 'DIRENV_FILE_set=true\n'; else printf 'DIRENV_FILE_set=false\n'; fi
if [ -n "${DIRENV_DIFF:-}" ]; then printf 'DIRENV_DIFF_set=true\n'; else printf 'DIRENV_DIFF_set=false\n'; fi
if [ -n "${DIRENV_WATCHES:-}" ]; then printf 'DIRENV_WATCHES_set=true\n'; else printf 'DIRENV_WATCHES_set=false\n'; fi
```

These signals are deliberately separate. A project venv command directory can be injected into every fresh tool process even when `VIRTUAL_ENV` is unset and no shell state persists. An observed `.envrc` plus set direnv marker variables does **not** show that the current workspace's `.envrc` was allowed or loaded: the markers can describe direnv state inherited from another directory or an unallowed file. Do not attribute the baseline provider until the conditional direnv check below, and do not use an unset `VIRTUAL_ENV` alone to claim that no activation or environment preparation occurred.

Record only whether the direnv marker variables are set. Never print their values: `DIRENV_DIFF` and `DIRENV_WATCHES` may contain encoded environment state, and `.envrc` itself may contain secrets. Do not read or quote `.envrc` during the general probe.

## 4. Run the two universal bare-name probes

If the agent has a process-execution tool, attempt these through the same interface later instructions would use, each as a normal bare command and in a separate tool call:

```text
commonplace-validate --help
rg --version
```

Both attempts are implementable even when the command is absent: command-not-found is the observation. If the agent has no process-execution tool, record both as `not run: no execution interface`. Record exit status when the runtime exposes it and retain only bounded useful output. Run command-resolution inspection in a later tool call so repeated success also shows that the runtime supplies a stable baseline environment to distinct calls; it does not show that those calls share one shell process.

Interpret `commonplace-validate` in light of the layout class:

- in a full install or source checkout with a prepared venv, absence may indicate command-discovery failure;
- in a reader install, absence is compatible with the install mode;
- when install mode or venv location is unknown, do not classify absence as an installation failure;
- success is not yet proof that the command belongs to the current project—record resolution provenance next where possible.

## 5. Inspect command resolution with the current shell

Run only the branch matching the already observed execution interface.

### Native PowerShell

`Get-Command` is a PowerShell facility, so it needs no external executable:

```powershell
Get-Command -Name 'commonplace-validate','rg' -All -ErrorAction SilentlyContinue |
  Select-Object Name, CommandType, Source, Version
```

If `.venv` was observed at the workspace root, inspect the expected entry point without invoking it:

```powershell
Test-Path (Join-Path (Get-Location) '.venv\Scripts\commonplace-validate.exe')
```

Do not run this path check when no project `.venv` was observed.

### POSIX shell

`command -v` is a shell facility:

```sh
command -v commonplace-validate 2>/dev/null || true
command -v rg 2>/dev/null || true
```

If `.venv` was observed at the workspace root, inspect the expected entry point without invoking it:

```sh
if [ -x "$PWD/.venv/bin/commonplace-validate" ]; then
  printf 'expected_venv_entrypoint=true\n'
else
  printf 'expected_venv_entrypoint=false\n'
fi
```

### `cmd.exe`

`cmd.exe` has no shell-native command-provenance facility equivalent to `Get-Command` or `command -v`. Keep the invocation results and mark provenance `unknown` unless the runtime already exposes a resolver. Do not assume `where.exe` is available. Run `if exist .venv\Scripts\commonplace-validate.exe (...)` only when `.venv` was already observed.

### Direct process execution or unknown interface

If the runtime exposes no command-resolution facility, keep the two invocation results and mark provenance `unknown`. Do not introduce a shell solely for this check.

## 6. Test whether separate tool calls share shell state

Run this step only when the observed execution interface is PowerShell or a POSIX shell. The two blocks must be separate agent tool calls. This tests the central question—whether activation-like process state could affect later tool calls—without changing `PATH`.

### PowerShell call A

```powershell
$env:COMMONPLACE_SHELL_PROBE = 'present'
function commonplace_shell_probe_function { 'present' }
[pscustomobject]@{
  Step = 'A'
  PID = $PID
  Cwd = (Get-Location).Path
  Variable = $env:COMMONPLACE_SHELL_PROBE
  Function = (Get-Command commonplace_shell_probe_function -ErrorAction SilentlyContinue).CommandType
}
```

### PowerShell call B

```powershell
[pscustomobject]@{
  Step = 'B'
  PID = $PID
  Cwd = (Get-Location).Path
  Variable = $env:COMMONPLACE_SHELL_PROBE
  Function = (Get-Command commonplace_shell_probe_function -ErrorAction SilentlyContinue).CommandType
}
Remove-Item Env:COMMONPLACE_SHELL_PROBE -ErrorAction SilentlyContinue
Remove-Item Function:commonplace_shell_probe_function -ErrorAction SilentlyContinue
```

### POSIX call A

```sh
export COMMONPLACE_SHELL_PROBE=present
commonplace_shell_probe_function() { printf 'present\n'; }
printf 'step=A\npid=%s\ncwd=%s\nvariable=%s\n' "$$" "$PWD" "$COMMONPLACE_SHELL_PROBE"
type commonplace_shell_probe_function 2>/dev/null || true
```

### POSIX call B

```sh
printf 'step=B\npid=%s\ncwd=%s\nvariable=%s\n' "$$" "$PWD" "${COMMONPLACE_SHELL_PROBE:-}"
type commonplace_shell_probe_function 2>/dev/null || true
unset COMMONPLACE_SHELL_PROBE
unset -f commonplace_shell_probe_function 2>/dev/null || true
```

Record PID and working directory as call context, not as persistence tests. PID equality is not evidence of process persistence: isolated containers or PID namespaces can assign the same PID to fresh processes. The unchanged working directory is also inconclusive because this Round 1 probe does not mutate it and runtimes commonly choose the workspace directory for every fresh call. Use only the deliberately mutated variable and function as the shell-state persistence evidence.

For `cmd.exe`, direct execution, or a remote tool API, record this step as `not run: no applicable state probe specified`. That gap is evidence for the next revision of this instruction.

## 7. Discover the wider tool surface before invoking it

The initial landscape census covers these command names:

```text
python python3 py pytest uv direnv git find sed xargs wc sort curl
roughdraft qmd ruff mkdocs sqlite3 jq gh codex claude
```

Discovery is not behavioral compatibility. Use only the resolution facility already established for the current interface:

PowerShell:

```powershell
$Names = 'python','python3','py','pytest','uv','direnv','git','find','sed','xargs','wc','sort','curl','roughdraft','qmd','ruff','mkdocs','sqlite3','jq','gh','codex','claude'
foreach ($Name in $Names) {
  Get-Command $Name -All -ErrorAction SilentlyContinue |
    Select-Object @{Name='RequestedName';Expression={$Name}}, Name, CommandType, Source, Version
}
```

POSIX shell:

```sh
for name in python python3 py pytest uv direnv git find sed xargs wc sort curl roughdraft qmd ruff mkdocs sqlite3 jq gh codex claude; do
  if ! command -v "$name" >/dev/null 2>&1; then
    printf '%s=absent\n' "$name"
  elif [ -n "${BASH_VERSION:-}" ]; then
    kind=$(type -t "$name")
    if [ "$kind" = file ]; then
      printf '%s=file:%s\n' "$name" "$(command -v "$name")"
    else
      printf '%s=%s\n' "$name" "$kind"
    fi
  else
    resolved=$(command -v "$name")
    case "$resolved" in
      /*) printf '%s=file:%s\n' "$name" "$resolved" ;;
      *) printf '%s=present-non-file-or-unknown-kind\n' "$name" ;;
    esac
  fi
done
```

For `cmd.exe` or direct execution, attempt no extra process merely to build a census unless the runtime already exposes executable discovery. Record the wider census `not run` when no such facility is established.

Classify aliases, functions, builtins/cmdlets, and executables separately. Do not print alias targets or function definitions during Round 1: runtime-injected wrappers may contain local implementation details, and kind alone is enough to prevent mistaking them for ordinary executables. A command called `curl`, `sort`, or `find` does not establish Unix-compatible semantics.

## 8. Run only fixture-backed behavioral checks

Behavioral checks require both a resolved executable and a suitable local target.

### ripgrep

Run a representative search only if `rg` resolved and one of these instruction roots was observed:

- source-like: `kb/instructions`;
- initialized full project-like: `kb/commonplace/instructions`;
- reader/vendor: the already known readable Commonplace instruction root, if that installation includes one.

Search that root for Markdown headings. In PowerShell, after assigning the observed path to `$InstructionRoot`:

```powershell
rg -n -m 1 --glob '*.md' '^# ' $InstructionRoot
```

In a POSIX shell, after assigning the observed path to `instruction_root`:

```sh
rg -n -m 1 --glob '*.md' '^# ' "$instruction_root"
```

In `cmd.exe`, run the same `rg` flags with the observed root quoted as a Windows path. Record the exact command. If no instruction root was observed, the version probe is sufficient and the search is `not run: no safe fixture`.

### direnv state

Run `direnv status` only if command discovery found `direnv` and the layout probe observed a workspace `.envrc`. This is a read-only status check; do not run `direnv allow`, `direnv exec`, or an activation command.

Do not copy the full status output into the report. Record only:

- whether `Found RC path` identifies the observed workspace `.envrc`;
- the `Found RC allowed` boolean;
- whether `Loaded RC path` identifies the same workspace `.envrc`, a different workspace, or no loaded file;
- whether the expected project-venv command directory is on the effective `PATH`.

Do not record `DIRENV_CONFIG`, watch entries, timestamps, `allowPath`, or allow hashes. They do not answer this probe and disclose local paths or persistent identifiers unnecessarily.

Interpret the fields together:

- **found here, not allowed, venv absent from `PATH`** — the workspace `.envrc` exists but has not prepared this execution environment; a matching `Loaded RC path` does not override failed authorization;
- **found here, allowed, loaded here, venv present on `PATH`** — consistent with direnv preparing the current baseline;
- **loaded from a different workspace** — direnv state was inherited from elsewhere; marker-variable presence must not be attributed to the current workspace;
- any other combination — record the exact booleans and classify the provider `unknown` pending a deeper probe.

This is a point-in-time observation for one tool process. It does not prove that a desktop launcher, fresh session, or future directory change will execute the direnv hook.

### Python identity

Run a version probe only for Python launcher names that resolution discovery found. Run the following identity program only through the launcher that later project instructions would actually use; preserve a multi-token launcher such as `py -3`. If the launcher cannot be determined from loaded instructions, do not choose one arbitrarily.

```text
<selected-python-launcher> -c "import os,sys; print('executable='+sys.executable); print('prefix='+sys.prefix); print('base_prefix='+sys.base_prefix); print('VIRTUAL_ENV='+str(os.environ.get('VIRTUAL_ENV')))"
```

Adapt only the outer quoting to the observed shell and record the exact invocation.

### Git

Run `git rev-parse --show-toplevel` only if Git resolved. If it establishes that the current workspace is a Git worktree and the layout probe established a specific Commonplace `COLLECTION.md` fixture, run `git status --short -- <that-single-fixture>` to test status access with bounded output. Do not run an unrestricted status command or characterize the cleanliness of the whole worktree; that state is irrelevant to the execution-channel survey. If no fixture was established, record the status check `not run: no bounded fixture`. Git absence or a non-Git installed project is a valid result.

### Other tools

Do not invent smoke tests for the remaining tools. A behavioral probe enters this instruction only after the inventory identifies an active Commonplace instruction, the exact behavior it relies on, and a safe fixture available in the target layout. Until then, report resolution only.

## 9. Report and stop

Use [the result template](./evidence/result-template.md) when accessible. Otherwise reproduce its headings in the agent response.

- Mark conclusions `observed`, `documented`, `inferred`, or `unknown`.
- Identify this as Round 1 and link a prior related report when one exists.
- For every unrun check, state `not run` and the unmet prerequisite.
- Bound output and do not dump the full environment or full `PATH`.
- Preserve command-not-found results, aliases, global resolution, sandbox denials, and absent content trees.
- Separate install mode, command discovery, behavioral compatibility, and runtime process semantics.
- Treat `.envrc` presence, direnv marker presence, authorization, loaded-file identity, and effective `PATH` as separate facts.
- Do not use fresh tool-shell behavior to infer launcher inheritance. Failed mutation persistence rules out activating once inside a tool call; it does not test whether a runtime launched from an activated parent shell passes that baseline to every fresh child.
- Do not generalize from one report. Include the exact environment identity available to the agent.
- Stop after reporting; do not remediate the environment.

To compare launch paths, worktrees, or two projects, run this same instruction independently in each already prepared environment and compare the reports. The probing agent is not required to create, activate, relaunch, or switch environments itself.

Later rounds should start from the Round 1 reports, name the exact unknown or candidate they test, and reuse only applicable sections of this instruction. They must state any added prerequisite and its capability gate before adding a command.
