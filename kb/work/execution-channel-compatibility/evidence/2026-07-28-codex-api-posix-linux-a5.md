# Execution-environment probe: Codex / API / POSIX Linux-like interface

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v6-2026-07-28`
- Prior related report: none retained; this v6 run supersedes the removed initial run for the same environment

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | `2026-07-28`; local timezone `Europe/Warsaw`; time of day unknown | observed / unknown |
| Runtime and surface | Codex via API | observed |
| Runtime version | unknown | unknown |
| OS and version | POSIX/Linux-like execution paths; OS/version not exposed | inferred / unknown |
| Tool execution interface | POSIX shell, Bash-backed | observed |
| Workspace/current directory | `<WORKSPACE>` | observed |
| Launch path | unknown | unknown |
| Sandbox/approval/write scope | workspace-write; workspace and `/tmp` writable; no broader permission requested | observed |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | `<WORKSPACE>` | observed |
| `pyproject.toml` | present | observed |
| `kb/instructions/COLLECTION.md` | present | observed |
| `kb/commonplace/instructions/COLLECTION.md` | absent | observed |
| Known reader/vendor path | none observed | observed |
| Project `.venv` at observed root | present | observed |
| Workspace `.envrc` | present | observed |

Provisional class: **Commonplace source-like checkout**

### Project-venv environment signals

| Signal | Result | Basis |
|---|---|---|
| Expected venv command directory | `<WORKSPACE>/.venv/bin` | observed |
| Expected venv command directory is on process `PATH` | true | observed; membership only, full `PATH` not recorded |
| `VIRTUAL_ENV` | unset | observed |
| `VIRTUAL_ENV` identifies the observed project venv | false | observed |
| direnv marker variables set | `DIRENV_DIR`, `DIRENV_FILE`, `DIRENV_DIFF`, and `DIRENV_WATCHES` set | observed; values not recorded |

The unset `VIRTUAL_ENV` is not used to infer that no activation or environment preparation occurred.

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | succeeded, exit `0`; bounded usage/help output returned | `<WORKSPACE>/.venv/bin/commonplace-validate` | bare command is discoverable in this call | observed |
| `rg --version` | succeeded, exit `0`; `ripgrep 15.2.0 (rev e89fff89ac)` | `<HOME>/.npm-global/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg` | bare command is discoverable and reports version | observed |

Expected venv entry point check: observed `expected_venv_entrypoint=true` for `<WORKSPACE>/.venv/bin/commonplace-validate`.

## Tool-call persistence

Applicable interface: yes

| Observation | First call | Second call | Interpretation |
|---|---|---|---|
| PID | `2` | `2` | context only; equality is inconclusive |
| Working directory | `<WORKSPACE>` | `<WORKSPACE>` | context only; not mutated by Round 1 |
| Probe environment variable | `present` | empty/unset | did not persist |
| Probe shell function | function invocation returned controlled `present` | not found | did not persist |

Conclusion and basis: environment-variable and shell-function state did not persist between separate tool calls. The repeated PID and working directory do not establish process persistence. The probe state was removed in the second call as required.

## Tool discovery

| Name | Resolution | Kind/source | Behavior verified? | Basis |
|---|---|---|---|---|
| `python` | `<WORKSPACE>/.venv/bin/python` | executable, project venv | no | observed |
| `python3` | `<WORKSPACE>/.venv/bin/python3` | executable, project venv | version and identity verified | observed |
| `py` | absent | — | no | observed |
| `pytest` | `<WORKSPACE>/.venv/bin/pytest` | executable, project venv | no | observed |
| `uv` | `/snap/bin/uv` | executable, system-managed Snap path | no | observed |
| `direnv` | `/usr/bin/direnv` | executable, system | `direnv status` verified | observed |
| `git` | `/usr/bin/git` | executable, system | repository probes verified | observed |
| `find` | `/usr/bin/find` | executable, system | no | observed |
| `sed` | `/usr/bin/sed` | executable, system | no | observed |
| `xargs` | `/usr/bin/xargs` | executable, system | no | observed |
| `wc` | `/usr/bin/wc` | executable, system | no | observed |
| `sort` | `/usr/bin/sort` | executable, system | no | observed |
| `curl` | `/usr/bin/curl` | executable, system | no | observed |
| `roughdraft` | `<HOME>/.npm-global/bin/roughdraft` | executable, npm-global | no | observed |
| `qmd` | `<HOME>/.npm-global/bin/qmd` | executable, npm-global | no | observed |
| `ruff` | `<WORKSPACE>/.venv/bin/ruff` | executable, project venv | no | observed |
| `mkdocs` | `<WORKSPACE>/.venv/bin/mkdocs` | executable, project venv | no | observed |
| `sqlite3` | `/usr/bin/sqlite3` | executable, system | no | observed |
| `jq` | `/usr/bin/jq` | executable, system | no | observed |
| `gh` | `/usr/bin/gh` | executable, system | no | observed |
| `codex` | `<HOME>/.npm-global/bin/codex` | executable, npm-global | no | observed |
| `claude` | absent | — | no | observed |

## Fixture-backed behavior

### ripgrep

- Observed instruction root: `kb/instructions`
- Exact search: `rg -n -m 1 --glob '*.md' '^# ' kb/instructions`
- Result: exit `0`; representative matches included `kb/instructions/write-instruction.md:6:# Write an Instruction` and `kb/instructions/ingest-directory.md:6:# Ingest a directory`.

### direnv state

- Workspace `.envrc` found by direnv: yes.
- Workspace `.envrc` allowed: yes.
- Loaded RC identity: current workspace.
- Expected project-venv command directory on `PATH`: yes.
- Baseline-provider interpretation and basis: **consistent with direnv preparing the current baseline**. The workspace `.envrc` was found, allowed, and loaded; its expected venv command directory was also on `PATH`. This is a point-in-time observation and does not establish behavior in a fresh launcher or another workspace.

### Python identity

- Launcher selected by an active instruction: `python3` (the loaded project instructions require `python3` for stdlib-only tooling).
- Version, `sys.executable`, and environment identity: Python `3.13.1`; `sys.executable=<WORKSPACE>/.venv/bin/python3`; `sys.prefix=<WORKSPACE>/.venv`; `sys.base_prefix=<HOME>/.local/share/uv/python/cpython-3.13.1-linux-x86_64-gnu`; `VIRTUAL_ENV=None`.

### Git

- Repository root: `<WORKSPACE>`, from `git rev-parse --show-toplevel` exit `0`.
- Single-fixture status command and result: `git status --short -- kb/instructions/COLLECTION.md` exited `0` with no output; no status conclusion is made about other paths.

## Findings

1. **The observed environment is a source-like checkout with a project venv and both universal bare probes succeeding.** — observed. Evidence: the layout checks, command exits `0`, and command-resolution paths.
2. **Bare-command success is consistent with the current workspace `.envrc` preparing the process baseline, without `VIRTUAL_ENV` being set.** — observed / inferred. Evidence: direnv found/allowed/loaded the current `.envrc`, the venv command directory was on `PATH`, and `VIRTUAL_ENV` was unset; the causal attribution remains a point-in-time interpretation.
3. **Separate POSIX tool calls did not preserve shell environment or function state.** — observed. Evidence: the variable and function were present in call A and absent in call B; repeated PID/cwd are insufficient to contradict this.
4. **`rg` resolves from the Codex installation rather than the project venv or `/usr/bin`.** — observed. Evidence: command resolution and the version probe.
5. **The discovered `rg` is compatible with the Round 1 heading-search fixture.** — observed. Evidence: the exact search exited `0` and returned Markdown headings.
6. **The active `python3` launcher executes the project-venv interpreter.** — observed. Evidence: Python `3.13.1`, project-venv `sys.executable` and `sys.prefix`.
7. **Git repository access works, and the bounded Commonplace collection fixture has no reported status changes.** — observed. Evidence: `git rev-parse` exited `0`; the single-fixture status command exited `0` with empty output.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| PowerShell or `cmd.exe` state probe | current execution interface is POSIX shell; no applicable Windows state probe |
| Behavioral checks for tools other than `rg`, Python identity, and Git | Round 1 requires an active instruction, exact behavior, and safe fixture for each additional check; those prerequisites were not established |
| `python` identity program | active instructions select `python3`; the procedure does not permit choosing another launcher arbitrarily |
| Second project/worktree comparison | no second already-prepared project or worktree was exposed by the current runtime |
| Parent-shell, resumed-session, and compacted-session inheritance | these require a prepared alternate launch path or session state not exposed to this probe |

## Unknowns

- Runtime version and exact launch path.
- OS distribution/version beyond the POSIX/Linux-like paths visible to the probe.
- Whether the current direnv-prepared baseline is inherited by a parent-launched runtime, resumed session, compacted session, or another workspace.
- Runtime-native environment handoff, session hooks, sandbox behavior for individual tools, and project/worktree switching behavior.
- Behavioral compatibility of the discovered tools not covered by the fixture-backed checks.

## Candidate implications

These are provisional observations for the solution catalogue, not rankings. The result supports testing [declared prerequisites plus bare-command session verification](../solution-catalogue.md#1-declared-prerequisites-plus-bare-command-session-verification) because both universal commands were directly verified, and [project-local runtime environment configuration](../solution-catalogue.md#4-project-local-runtime-environment-configuration) because the current `.envrc` was allowed and loaded with the project venv directory on `PATH`. The non-persistence result supports examining [runtime-native session environment handoff](../solution-catalogue.md#3-runtime-native-session-environment-handoff) or [launching the agent runtime from an activated project shell](../solution-catalogue.md#2-launch-the-agent-runtime-from-an-activated-project-shell) in a later prepared-environment probe; this report does not test either mechanism. The Codex-resolved `rg` path is evidence to examine [runtime-bundled tool reliance](../solution-catalogue.md#13-runtime-bundled-tool-reliance), not proof that the bundle is a cross-surface contract.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes — workspace root → `<WORKSPACE>`, user profile directory → `<HOME>`; the workspace prefix was replaced before the home prefix. No usernames, hostnames, email addresses, machine identifiers, or network addresses appear.
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent — `PATH` was tested by membership only; `direnv status` was classified through the shell-native filter so raw status never entered the transcript; `.envrc`, shell-profile contents, alias targets, function definitions, and direnv marker values were not read or recorded; Git status was restricted to one named fixture.
- Optional automated scan: not run — no scanner established in this environment; the procedure forbids installing one
- Withheld or residual sensitive-looking material: none
