---
description: "Use to gather an initial, comparable execution-capability report from any environment in which Commonplace is read or operated"
type: types/instruction.md
---

# Probe the current Commonplace execution environment

## Outcome

Produce one evidence report describing what the current agent can actually execute and read. This is reconnaissance across the environments in which Commonplace can be used, not a pass/fail installation test. A missing `commonplace-*` command is expected in a reader install; a missing Git checkout is expected in some projects; and a tool that cannot be tested remains `unknown` rather than failed.

This instruction is the Round 1 breadth probe. Run it unchanged so reports remain comparable. Later rounds may repeat an environment with narrower, deeper tests selected from the gaps in the first reports; they create new reports rather than editing the baseline.

Procedure ID: `execution-channel-round1-v7-2026-09-25`.

The first constraint is implementability: run a check only after its prerequisites are available in the current environment. Do not assume the agent is in the Commonplace source checkout, has Git metadata, can see a project root, uses Bash, can write files, or can launch a second session. Record a skipped check and its missing prerequisite instead of inventing a substitute.

### Command and library model under test

Two decisions set what a healthy environment looks like:

- **Commands** ([ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)). `commonplace-*` commands come from one user-level uv tool installation. The uv tool executable directory (`uv tool dir --bin`) is the command authority, and `uv tool update-shell` adds it to the user's `PATH`. A process started before that change does not see it until the process is fully restarted. A project `.venv` or `.envrc` is not part of command discovery; its presence is at most residue from the older project-venv model.
- **Library** ([ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md)). Projects hold no copy of Commonplace's instructions, types, or skills. The library lives in the installed package's shared data (or the source tree's `kb/` for an editable install). `commonplace-init` writes gitignored pointers into each project: `.commonplace/library.md` with the library root and a skill index, one stub per promoted skill in `.claude/skills/` and `.agents/skills/`, and a Claude Code read rule. An agent reaches library text by reading files at absolute paths outside the workspace.

The probe therefore separates three questions: does a bare command resolve, does it resolve to the uv tool authority, and can the agent read the library that the project points to.

## Boundaries

This is an observational procedure. Do not make the environment pass:

- do not modify `PATH`, activate a venv, or restart the runtime;
- do not install, upgrade, reinstall, or repair tools, and do not run `commonplace-init` without `--check`;
- do not edit profiles, hooks, runtime settings, execution policies, or project files;
- do not switch to an explicit executable path after a bare command fails;
- do not request broader permissions solely to complete or save the probe;
- do not recursively search outside the workspace to find a Commonplace installation; the only paths outside the workspace this probe reads are the uv tool directory and the library root named by `.commonplace/library.md`;
- do not run commands that dump the full environment, credential stores, configuration files, shell profiles, or unrestricted repository status.

The procedure may set the uniquely named `COMMONPLACE_SHELL_PROBE` variable and shell function in one tool process to test persistence. Remove them in the second call when they persist.

Except for that deliberate persistence test, every command block must be self-contained. Recompute working paths and shell variables inside each tool call; never depend on a variable assigned by an earlier block.

## Invocation brief

Give another agent this instruction by a path it can already read, or paste the instruction into its task:

> Probe the currently open environment using the execution-channel procedure. Treat source checkouts, initialized projects, reader/vendor installs, package-only environments, and unrecognized layouts as valid observations. Run only checks whose prerequisites you first establish. Do not activate, install, repair, reconfigure, restart, or broaden permissions. Normalize local identifiers and complete the mandatory disclosure review on the final payload before returning it. Save the report under the workshop evidence directory only if that path already exists and is writable within your normal scope.

An agent does not need access to this workshop repository to perform the probe. If it cannot write here, its response is the evidence artifact for an operator to copy later.

## 1. Identify the survey run

Record:

- round: `1 — landscape breadth`;
- procedure ID: `execution-channel-round1-v7-2026-09-25`;
- any prior related report, otherwise `none`.

## 2. Record identity from available runtime facts

Record the following without adding a new command merely to fill a field:

- UTC date and local timezone, if exposed;
- agent product, surface, and version, if exposed;
- OS and version, if exposed;
- execution interface used by tool calls: PowerShell, POSIX shell, `cmd.exe`, direct process execution, remote service, or unknown;
- workspace path supplied by the runtime, or the current directory if no workspace concept is exposed; retain it for local comparisons but normalize it in the final report;
- launch path (terminal-launched CLI, desktop application, IDE extension, cloud surface), sandbox/approval mode, and write scope, when visible to the agent;
- whether the runtime process was started after the most recent Commonplace install or `uv tool update-shell`, if the operator or runtime states it; otherwise `unknown`. Do not infer it.

Mark unavailable facts `unknown`. Do not infer the tool-call shell from an integrated-terminal preference.

## 3. Classify only the layout that is observable

Use the runtime's workspace root when it exposes one; otherwise use the current tool-call directory. Test only paths relative to that root.

| Observed path or fact | Provisional class |
|---|---|
| `pyproject.toml` and `kb/instructions/COLLECTION.md` | Commonplace source-like checkout |
| `.commonplace/library.md` | initialized project-like layout |
| `kb/commonplace/instructions/COLLECTION.md` without `.commonplace/library.md` | pre-ADR-086 copied-library project (legacy) |
| a Commonplace vendor path named by loaded project instructions | reader/vendor layout |
| bare `commonplace-*` command but none of the above | package-only or externally managed layout |
| none of the above | other/unknown |

These are observational labels, not installation verdicts. More than one row can match; record every match. If the current directory is below the workspace root and the runtime does not expose that root, record `workspace root unknown`; do not search arbitrary ancestors or the filesystem.

Also record, as presence only, two residue signals from the older project-venv model: a workspace `.venv` directory and a workspace `.envrc` file. Neither is expected to affect command discovery. Do not read `.envrc`, do not run `direnv`, and do not inspect `.venv` contents.

PowerShell:

```powershell
$WorkspaceRoot = (Get-Location).Path
$Candidates = 'pyproject.toml','kb\instructions\COLLECTION.md','.commonplace\library.md','kb\commonplace\instructions\COLLECTION.md','.claude\skills','.agents\skills','.venv','.envrc'
foreach ($Candidate in $Candidates) {
  [pscustomobject]@{ Path = $Candidate; Present = Test-Path (Join-Path $WorkspaceRoot $Candidate) }
}
```

POSIX shell:

```sh
workspace_root=$PWD
for candidate in pyproject.toml kb/instructions/COLLECTION.md .commonplace/library.md kb/commonplace/instructions/COLLECTION.md .claude/skills .agents/skills .venv .envrc; do
  if [ -e "$workspace_root/$candidate" ]; then
    printf 'present=%s\n' "$candidate"
  else
    printf 'absent=%s\n' "$candidate"
  fi
done
```

For `cmd.exe`, use `cd` to record the current directory and `if exist <relative-path> (...)` for the same paths. For a direct-process interface with no shell expressions, use any runtime-provided file inspection capability; otherwise leave layout classification `unknown`.

If a loaded project instruction names a different reader/vendor path, record that path and whether it is readable. Do not require it to match any conventional root.

## 4. Check library reachability

Run this step only when `.commonplace/library.md` was observed, and use the runtime's ordinary file-read capability rather than a shell command where one exists.

1. Read `.commonplace/library.md`. Record whether the read succeeded. Record the library root it names only after normalizing it as described in step 10 (`<UV_TOOLS>` or `<WORKSPACE>`-relative when it falls under those prefixes). Do not copy the skill index into the report; record only how many skills it lists.
2. Read `<library root>/instructions/COLLECTION.md` by absolute path. Record success, or the exact denial or not-found message class (sandbox denial, permission prompt declined, not found).
3. If `.claude/skills/` or `.agents/skills/` was observed, pick one `cp-skill-*` subdirectory, read its `SKILL.md`, and record whether it is a stub that names an absolute library path, and whether that path is readable. Record the skill name only.

A readable pointer file whose library root is not readable is the finding this step exists to catch; it is not a reason to search for the library elsewhere.

When `.commonplace/library.md` is absent, record this step `not run: no init outputs`. In a source-like checkout the library is the workspace's own `kb/`, so its absence there is expected.

## 5. Run the two universal bare-name probes

If the agent has a process-execution tool, attempt these through the same interface later instructions would use, each as a normal bare command and in a separate tool call:

```text
commonplace-validate --help
rg --version
```

Both attempts are implementable even when the command is absent: command-not-found is the observation. If the agent has no process-execution tool, record both as `not run: no execution interface`. Record exit status when the runtime exposes it and retain only bounded useful output. Run command-resolution inspection in a later tool call so repeated success also shows that the runtime supplies a stable baseline environment to distinct calls; it does not show that those calls share one shell process.

Also record whether `commonplace-validate --help` printed a warning about missing or stale init outputs. Record the warning class only (missing stub, stale stub, missing routing file, stale read rule), not the paths it names.

Interpret `commonplace-validate` in light of the layout class and step 2:

- in an initialized project or source checkout, absence indicates a command-discovery failure: either the tool is not installed, or this process was started before `uv tool update-shell` took effect. Record which is supported by evidence; if the launch time is `unknown`, say both remain possible;
- in a reader install, absence is compatible with the install mode;
- when the install mode is unknown, do not classify absence as an installation failure;
- success is not yet proof that the command comes from the uv tool authority. Step 6 checks that.

## 6. Inspect command resolution and authority

Run only the branch matching the already observed execution interface.

### Native PowerShell

`Get-Command` is a PowerShell facility, so it needs no external executable:

```powershell
Get-Command -Name 'commonplace-validate','rg','uv' -All -ErrorAction SilentlyContinue |
  Select-Object Name, CommandType, Source, Version
```

### POSIX shell

`command -v` is a shell facility:

```sh
command -v commonplace-validate 2>/dev/null || true
command -v rg 2>/dev/null || true
command -v uv 2>/dev/null || true
```

### Authority comparison

If `uv` resolved, run `uv tool dir --bin` as a separate bare command. It is read-only. Record whether the directory it prints:

- contains the resolved `commonplace-validate` (expected authority);
- differs from the resolved location (a shadowing executable earlier on `PATH`; record the normalized shadowing path);
- is absent from the process `PATH` while `commonplace-validate` did not resolve (the installed tool is not visible to this process).

Compare path entries exactly; do not print the full `PATH`. In PowerShell, split `$env:PATH` on `[IO.Path]::PathSeparator` and compare entries case-insensitively after trimming a trailing separator. In a POSIX shell, test membership with `case ":$PATH:" in *":<dir>:"*)`.

If `uv` did not resolve, record authority `unknown: uv not resolvable`. Do not look for uv's default tool directory by guessing a path.

If `commonplace-init` resolved and `.commonplace/library.md` was observed, run `commonplace-init --check` once. It reports stale init outputs without writing. Record its exit status and the classes of finding, not the paths.

### `cmd.exe`

`cmd.exe` has no shell-native command-provenance facility equivalent to `Get-Command` or `command -v`. Keep the invocation results and mark provenance `unknown` unless the runtime already exposes a resolver. Do not assume `where.exe` is available. `uv tool dir --bin` may still be run if `uv --version` succeeds as a bare command.

### Direct process execution or unknown interface

If the runtime exposes no command-resolution facility, keep the invocation results and mark provenance `unknown`. Do not introduce a shell solely for this check.

## 7. Test whether separate tool calls share shell state

Run this step only when the observed execution interface is PowerShell or a POSIX shell. The two blocks must be separate agent tool calls. This tests whether process state set in one tool call reaches later tool calls, without changing `PATH`.

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
function_result=$(commonplace_shell_probe_function)
printf 'step=A\npid=%s\ncwd=%s\nvariable=%s\nfunction_result=%s\n' "$$" "$PWD" "$COMMONPLACE_SHELL_PROBE" "$function_result"
```

### POSIX call B

```sh
if command -v commonplace_shell_probe_function >/dev/null 2>&1; then function_present=true; else function_present=false; fi
printf 'step=B\npid=%s\ncwd=%s\nvariable=%s\nfunction_present=%s\n' "$$" "$PWD" "${COMMONPLACE_SHELL_PROBE:-}" "$function_present"
unset COMMONPLACE_SHELL_PROBE
unset -f commonplace_shell_probe_function 2>/dev/null || true
```

The call-A function invocation emits only the controlled literal `present`; the call-B lookup discards resolver output and emits only a boolean. Neither call prints a function definition. Record PID and working directory as call context, not as persistence tests. PID equality is not evidence of process persistence: isolated containers or PID namespaces can assign the same PID to fresh processes. The unchanged working directory is also inconclusive because this Round 1 probe does not mutate it and runtimes commonly choose the workspace directory for every fresh call. Use only the deliberately mutated variable and function as the shell-state persistence evidence.

For `cmd.exe`, direct execution, or a remote tool API, record this step as `not run: no applicable state probe specified`. That gap is evidence for the next revision of this instruction.

## 8. Discover the wider tool surface before invoking it

The initial landscape census covers these command names:

```text
python python3 py pytest uv git find sed xargs wc sort curl
roughdraft qmd ruff mkdocs sqlite3 jq gh codex claude
```

Discovery is not behavioral compatibility. Use only the resolution facility already established for the current interface:

PowerShell:

```powershell
$Names = 'python','python3','py','pytest','uv','git','find','sed','xargs','wc','sort','curl','roughdraft','qmd','ruff','mkdocs','sqlite3','jq','gh','codex','claude'
foreach ($Name in $Names) {
  Get-Command $Name -All -ErrorAction SilentlyContinue |
    Select-Object @{Name='RequestedName';Expression={$Name}}, Name, CommandType, Source, Version
}
```

POSIX shell:

```sh
for name in python python3 py pytest uv git find sed xargs wc sort curl roughdraft qmd ruff mkdocs sqlite3 jq gh codex claude; do
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

## 9. Run only fixture-backed behavioral checks

Behavioral checks require both a resolved executable and a suitable local target.

### ripgrep

Run a representative search only if `rg` resolved and one of these instruction roots was observed and readable:

- source-like: `kb/instructions` in the workspace;
- initialized project: `<library root>/instructions`, where step 4 read the library root from `.commonplace/library.md` and confirmed it readable;
- reader/vendor: the already known readable Commonplace instruction root, if that installation includes one.

Search that root for Markdown headings. In PowerShell, after assigning the observed path to `$InstructionRoot`:

```powershell
rg -n -m 1 --glob '*.md' '^# ' $InstructionRoot
```

In a POSIX shell, after assigning the observed path to `instruction_root`:

```sh
rg -n -m 1 --glob '*.md' '^# ' "$instruction_root"
```

In `cmd.exe`, run the same `rg` flags with the observed root quoted as a Windows path. Record the exact command with the root normalized. A search of the library root tests whether a shell process, not only the file-read tool, may read outside the workspace; record a sandbox denial as a separate finding from step 4. If no instruction root was observed, the version probe is sufficient and the search is `not run: no safe fixture`.

### Python identity

Run a version probe only for Python launcher names that resolution discovery found. Run the following identity program only through the launcher that later project instructions would actually use; preserve a multi-token launcher such as `py -3`. If the launcher cannot be determined from loaded instructions, do not choose one arbitrarily.

```text
<selected-python-launcher> -c "import sys; print('executable='+sys.executable); print('prefix='+sys.prefix); print('base_prefix='+sys.base_prefix)"
```

Adapt only the outer quoting to the observed shell and record the exact invocation.

### Git

Run `git rev-parse --show-toplevel` only if Git resolved. If it establishes that the current workspace is a Git worktree and the layout probe established a specific Commonplace fixture (`kb/instructions/COLLECTION.md` or `.commonplace/library.md`), run `git status --short --ignored -- <that-single-fixture>` to test status access with bounded output; an init output should show as ignored. Do not run an unrestricted status command or characterize the cleanliness of the whole worktree. If no fixture was established, record the status check `not run: no bounded fixture`. Git absence or a non-Git project is a valid result.

### Other tools

Do not invent smoke tests for the remaining tools. A behavioral probe enters this instruction only after the inventory identifies an active Commonplace instruction, the exact behavior it relies on, and a safe fixture available in the target layout. Until then, report resolution only.

## 10. Draft the report

Use [the result template](./evidence/result-template.md) when accessible. Otherwise reproduce its headings in the agent response.

- Mark conclusions `observed`, `documented`, `inferred`, or `unknown`.
- Identify this as Round 1 and link a prior related report when one exists.
- For every unrun check, state `not run` and the unmet prerequisite.
- Bound output and do not dump the full environment or full `PATH`.
- Preserve command-not-found results, aliases, shadowing executables, sandbox denials, unreadable library roots, and absent content trees.
- Separate install mode, command discovery, command authority, library reachability, behavioral compatibility, and runtime process semantics.
- Do not use fresh tool-shell behavior to infer launcher inheritance. Failed mutation persistence rules out setting state once inside a tool call; it does not test whether a runtime inherits the `PATH` of the process that launched it.
- Do not generalize from one report. Include the environment identity available to the agent, subject to the disclosure review below.

To compare launch paths, worktrees, two projects, or a runtime before and after a restart, run this same instruction independently in each already prepared environment and compare the reports. The probing agent is not required to create, relaunch, or switch environments itself.

Later rounds should start from the Round 1 reports, name the exact unknown or candidate they test, and reuse only applicable sections of this instruction. They must state any added prerequisite and its capability gate before adding a command.

## 11. Review disclosure, then return the report

Perform this review on the final report payload—not only on notes or an earlier draft—before finalizing, attaching, sending, or committing it. A local draft may exist while the review runs. This review is mandatory and requires no additional tool.

### Normalize local identifiers

After all path comparisons are complete, replace local prefixes in the report while preserving the suffix needed for provenance:

- the observed workspace root becomes `<WORKSPACE>`;
- the directory printed by `uv tool dir` becomes `<UV_TOOLS>`, and the directory printed by `uv tool dir --bin` becomes `<UV_TOOL_BIN>`;
- the user home/profile directory becomes `<HOME>`;
- the platform temporary directory becomes `<TEMP>`;
- usernames, hostnames, email addresses, machine identifiers, and private network addresses are omitted unless the investigation specifically requires them.

Replace the more specific prefix first: workspace and uv tool directories before the home prefix. Keep public system paths such as `/usr/bin/rg` or `C:\Windows\System32\...` when they establish provenance. A normalized result such as `<UV_TOOL_BIN>/commonplace-validate` or `<UV_TOOLS>/llm-commonplace/share/commonplace` retains the evidence this workshop needs.

### Inspect for material that must not leave the environment

Confirm that the final payload contains none of the following:

- passwords, API keys, access or refresh tokens, cookies, session identifiers, authorization headers, private-key blocks, credential-bearing URLs, connection strings, or cloud access identifiers;
- full environment or `PATH` dumps;
- `.envrc` contents, shell-profile contents, runtime settings files, alias targets, or function definitions;
- the skill index or other contents of `.commonplace/library.md` beyond the normalized library root and a skill count;
- unrestricted Git status output, unrelated project filenames, home-directory listings, scratchpad paths, or memory-store paths;
- raw command output beyond the bounded lines needed to establish a reported fact.

If suspicious material is present, replace it with `[REDACTED:<category>]` and keep only the capability conclusion it supported. If redaction would destroy the evidence, mark that result `withheld from shared report` and state the non-sensitive conclusion. Never quote a suspected secret while asking whether it is safe.

If the runtime already provides a secret scanner and the completed report already exists as a readable file, it may be run as an additional check. Do not install a scanner, write a temporary copy, broaden permissions, or treat scanner absence as a blocker. Configure any scanner to return only category and line number, never the matched value. This optional scan does not replace the mandatory content review.

### Append the disclosure attestation

The report is not complete until it ends with:

```markdown
## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes / not applicable
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent
- Optional automated scan: not run / passed / findings redacted
- Withheld or residual sensitive-looking material: none / <non-sensitive description and reason>
```

Only after this section is accurate may the agent return or persist the report. Stop after reporting; do not remediate the environment.
