# Execution-environment probe: Codex / API / POSIX Linux-like interface

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-2026-07-28`
- Prior related report: none observed

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | `2026-07-28`; local timezone `Europe/Warsaw`; time of day unknown | observed |
| Runtime and surface | Codex via API | observed |
| Runtime version | unknown | unknown |
| OS and version | POSIX/Linux-like paths observed; OS/version not exposed | inferred |
| Tool execution interface | POSIX shell | observed |
| Workspace/current directory | `/home/zby/llm/commonplace` | observed |
| Launch path | unknown | unknown |
| Sandbox/approval/write scope | workspace-write; repository and `/tmp` writable; no broader permission requested | observed |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | `/home/zby/llm/commonplace` | observed |
| `pyproject.toml` | present | observed |
| `kb/instructions/COLLECTION.md` | present | observed |
| `kb/commonplace/instructions/COLLECTION.md` | absent | observed |
| Known reader/vendor path | none observed | observed |
| Project `.venv` at observed root | present | observed |

Provisional class: **Commonplace source-like checkout**

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | succeeded, exit `0`; usage/help output returned | `/home/zby/llm/commonplace/.venv/bin/commonplace-validate` | bare command is discoverable in this call | observed |
| `rg --version` | succeeded, exit `0`; `ripgrep 15.2.0 (rev e89fff89ac)` | `/home/zby/.npm-global/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg` | bare command is discoverable and reports version | observed |

Expected venv entry point check: observed `expected_venv_entrypoint=true` for `.venv/bin/commonplace-validate`.

## Tool-call persistence

Applicable interface: yes

| State | First call | Second call | Persists? |
|---|---|---|---|
| PID | `2` | `2` | same reported PID; process identity alone is inconclusive |
| Working directory | `/home/zby/llm/commonplace` | `/home/zby/llm/commonplace` | same, but the runtime supplies this cwd on each call |
| Probe environment variable | `present` | empty/unset | no |
| Probe shell function | function present | not found | no |

Conclusion and basis: environment-variable and shell-function state did not persist between separate tool calls. The repeated PID and cwd do not establish shell-state persistence. The probe variable and function were removed in the second call as required.

## Tool discovery

| Name | Resolution | Kind/source | Behavior verified? | Basis |
|---|---|---|---|---|
| `python` | `/home/zby/llm/commonplace/.venv/bin/python` | executable, project venv | version only: Python 3.13.1 | observed |
| `python3` | `/home/zby/llm/commonplace/.venv/bin/python3` | executable, project venv | version and identity verified | observed |
| `py` | absent | — | no | observed |
| `pytest` | `/home/zby/llm/commonplace/.venv/bin/pytest` | executable, project venv | no | observed |
| `uv` | `/snap/bin/uv` | executable, system-managed Snap path | no | observed |
| `git` | `/usr/bin/git` | executable, system | repository probes verified | observed |
| `find` | `/usr/bin/find` | executable, system | no | observed |
| `sed` | `/usr/bin/sed` | executable, system | no | observed |
| `xargs` | `/usr/bin/xargs` | executable, system | no | observed |
| `wc` | `/usr/bin/wc` | executable, system | no | observed |
| `sort` | `/usr/bin/sort` | executable, system | no | observed |
| `curl` | `/usr/bin/curl` | executable, system | no | observed |
| `roughdraft` | `/home/zby/.npm-global/bin/roughdraft` | executable, npm-global | no | observed |
| `qmd` | `/home/zby/.npm-global/bin/qmd` | executable, npm-global | no | observed |
| `ruff` | `/home/zby/llm/commonplace/.venv/bin/ruff` | executable, project venv | no | observed |
| `mkdocs` | `/home/zby/llm/commonplace/.venv/bin/mkdocs` | executable, project venv | no | observed |
| `sqlite3` | `/usr/bin/sqlite3` | executable, system | no | observed |
| `jq` | `/usr/bin/jq` | executable, system | no | observed |
| `gh` | `/usr/bin/gh` | executable, system | no | observed |
| `codex` | `/home/zby/.npm-global/bin/codex` | executable, npm-global | no | observed |
| `claude` | absent | — | no | observed |

## Fixture-backed behavior

### ripgrep

- Observed instruction root: `kb/instructions`
- Exact search: `rg -n -m 1 --glob '*.md' '^# ' kb/instructions`
- Result: exit `0`; representative match `kb/instructions/ingest-directory.md:6:# Ingest a directory`

### Python identity

- Launcher selected by an active instruction: `python3` (the loaded project instructions explicitly require `python3` for stdlib-only tooling)
- Version, `sys.executable`, and environment identity: Python `3.13.1`; `sys.executable=/home/zby/llm/commonplace/.venv/bin/python3`; `sys.prefix=/home/zby/llm/commonplace/.venv`; `sys.base_prefix=/home/zby/.local/share/uv/python/cpython-3.13.1-linux-x86_64-gnu`; `VIRTUAL_ENV` empty

### Git

- Repository root: `/home/zby/llm/commonplace`, from `git rev-parse --show-toplevel` exit `0`
- Status access: `git status --short` exit `0`; the worktree had many pre-existing modified files and untracked paths. The status was observed, not changed by the probe.

## Findings

1. **The observed environment is a source-like checkout with a project venv and both universal bare probes succeeding.** — observed. Evidence: the four layout checks, command exits `0`, and command-resolution paths.
2. **Bare-command success does not require an activated venv in this call.** — observed. Evidence: `python3` and `commonplace-validate` resolved into `.venv`, while `VIRTUAL_ENV` was empty.
3. **Separate POSIX tool calls did not preserve shell environment or function state.** — observed. Evidence: the variable and function were present in call A and absent in call B; repeated PID/cwd are insufficient to contradict this.
4. **`rg` resolves from the Codex installation rather than the project venv or `/usr/bin`.** — observed. Evidence: `command -v rg` and `rg --version`.
5. **The current worktree is not clean.** — observed. Evidence: `git status --short`; this probe did not modify the pre-existing changes.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| PowerShell or `cmd.exe` state probe | current execution interface is POSIX shell; no applicable Windows state probe |
| Behavioral checks for tools other than `rg`, Python identity, and Git | Round 1 procedure requires an active instruction, exact behavior, and safe fixture for each additional check; those prerequisites were not established |
| `python` `sys.executable` identity | active instructions select `python3`; the procedure does not permit choosing another launcher arbitrarily |
| Second project/worktree comparison | no second already-prepared project or worktree was exposed by the current runtime |

## Unknowns

- Runtime version and exact launch path.
- OS distribution/version beyond the POSIX/Linux-like paths visible to the probe.
- Whether the current command resolution is stable across resumed, compacted, or differently launched sessions.
- Runtime-native environment handoff, session hooks, sandbox behavior for individual tools, and project/worktree switching behavior.
- Behavioral compatibility of the discovered tools not covered by the fixture-backed checks.

## Candidate implications

These are provisional observations for the catalogue, not rankings. The result supports testing [declared prerequisites plus bare-command session verification](../solution-catalogue.md#1-declared-prerequisites-plus-bare-command-session-verification) because both universal commands were directly verified, and [runtime-native session environment handoff](../solution-catalogue.md#3-runtime-native-session-environment-handoff) or [project-local runtime environment configuration](../solution-catalogue.md#4-project-local-runtime-environment-configuration) because shell state did not persist between calls. The Codex-resolved `rg` path is evidence to examine [runtime-bundled tool reliance](../solution-catalogue.md#13-runtime-bundled-tool-reliance), not proof that the bundle is a cross-surface contract.
