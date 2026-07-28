# Execution-environment probe: Codex / API / POSIX / initialized project-like

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v4-2026-07-28`
- Prior related report: none retained; this v4 run supersedes the removed v3 run for the same environment

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | `2026-07-28`; local timezone `Europe/Warsaw`; time of day unknown | observed |
| Runtime and surface | Codex via API | documented |
| Runtime version | unknown | unknown |
| OS and version | POSIX/Linux-like execution paths; version not exposed | inferred / unknown |
| Tool execution interface | POSIX shell, Bash-backed | observed |
| Workspace/current directory | `/home/zby/llm/commonplace-test-installed` | observed |
| Launch path | unknown | unknown |
| Sandbox/approval/write scope | workspace-write; current workspace, memories directory, and `/tmp` writable | observed |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | `/home/zby/llm/commonplace-test-installed` | observed |
| `pyproject.toml` | absent | observed |
| `kb/instructions/COLLECTION.md` | present | observed |
| `kb/commonplace/instructions/COLLECTION.md` | present | observed |
| Known reader/vendor path | none observed | observed |
| Project `.venv` at observed root | present | observed |
| Workspace `.envrc` | present | observed |

Provisional class: **initialized full-project-like**

### Project-venv environment signals

| Signal | Result | Basis |
|---|---|---|
| Expected venv command directory | `/home/zby/llm/commonplace-test-installed/.venv/bin` | observed |
| Expected venv command directory is on process `PATH` | false | observed |
| `VIRTUAL_ENV` | unset | observed |
| `VIRTUAL_ENV` identifies the observed project venv | false | observed |
| direnv marker variables set | `DIRENV_DIR`, `DIRENV_FILE`, `DIRENV_DIFF`, and `DIRENV_WATCHES` set | observed |

Possible baseline provider and basis: **unknown**. The workspace `.envrc` and direnv markers are present, but v4 requires the authorization and `PATH` facts to be considered together.

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | command not found; exit `127` | unresolved | bare command unavailable despite an executable project entry point | observed |
| `rg --version` | `ripgrep 15.2.0`; exit `0` | `/home/zby/.npm-global/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg` | bare command discoverable and reports version | observed |

Expected venv entry point check: observed `expected_venv_entrypoint=true` for `.venv/bin/commonplace-validate`.

## Tool-call persistence

Applicable interface: yes

| Observation | First call | Second call | Interpretation |
|---|---|---|---|
| PID | `2` | `2` | context only; equality is inconclusive |
| Working directory | `/home/zby/llm/commonplace-test-installed` | `/home/zby/llm/commonplace-test-installed` | context only; not mutated |
| Probe environment variable | `present` | empty/unset | did not persist |
| Probe shell function | function present | not found | did not persist |

Conclusion and basis: environment-variable and shell-function state did not persist between separate tool calls. Repeated PID and working directory do not establish process persistence. The probe state was removed in the second call. This rules out activating once inside a tool call, but does not test whether a runtime-launched parent shell passes its baseline to fresh children.

## Tool discovery

All resolved entries below were classified as ordinary executable files by the v4 POSIX census. No aliases, functions, or builtins were observed for the listed names.

| Name | Resolution | Behavior verified? | Basis |
|---|---|---|---|
| `python` | `/usr/bin/python` | version only: Python 3.12.3 | observed |
| `python3` | `/usr/bin/python3` | version only: Python 3.12.3 | observed |
| `py` | absent | no | observed |
| `pytest` | `/usr/bin/pytest` | no | observed |
| `uv` | `/snap/bin/uv` | no | observed |
| `direnv` | `/usr/bin/direnv` | `direnv status` verified | observed |
| `git` | `/usr/bin/git` | repository probe attempted | observed |
| `find` | `/usr/bin/find` | no | observed |
| `sed` | `/usr/bin/sed` | no | observed |
| `xargs` | `/usr/bin/xargs` | no | observed |
| `wc` | `/usr/bin/wc` | no | observed |
| `sort` | `/usr/bin/sort` | no | observed |
| `curl` | `/usr/bin/curl` | no | observed |
| `roughdraft` | `/home/zby/.npm-global/bin/roughdraft` | no | observed |
| `qmd` | `/home/zby/.npm-global/bin/qmd` | no | observed |
| `ruff` | absent | no | observed |
| `mkdocs` | absent | no | observed |
| `sqlite3` | `/usr/bin/sqlite3` | no | observed |
| `jq` | `/usr/bin/jq` | no | observed |
| `gh` | `/usr/bin/gh` | no | observed |
| `codex` | `/home/zby/.npm-global/bin/codex` | no | observed |
| `claude` | absent | no | observed |

## Fixture-backed behavior

### ripgrep

- Observed instruction root: `kb/commonplace/instructions`
- Exact search: `rg -n -m 1 --glob '*.md' '^# ' "$PWD/kb/commonplace/instructions"`
- Result: exit `0`; headings found, including `ingest-directory.md:6:# Ingest a directory`.

### direnv state

- `Found RC path` identifies the observed workspace `.envrc`: yes.
- `Found RC allowed`: false.
- `Loaded RC path` identifies the same workspace `.envrc`: yes.
- `Loaded RC allowed`: false.
- Expected project-venv command directory on effective `PATH`: no.
- Interpretation: **the workspace `.envrc` exists but has not prepared this execution environment**. The matching `Loaded RC path` does not override failed authorization. This is a point-in-time observation; no provider beyond the unprepared direnv state was established.

### Python identity

- Launcher selected by an active instruction: none established.
- Version probes: `python --version` and `python3 --version` both returned Python `3.12.3`.
- Identity program: not run because the procedure does not permit choosing a launcher arbitrarily.

### Git

- Repository root: not established; `git rev-parse --show-toplevel` exited `128`.
- Single-fixture status command: not run because the workspace is not a Git worktree.

## Findings

1. **The workspace is initialized full-project-like.** — observed. Both instruction trees, `.venv`, and `.envrc` are present.
2. **The project venv is not exposed through bare command discovery.** — observed. Its `commonplace-validate` entry point exists, but `.venv/bin` is not on `PATH` and the bare command is unavailable.
3. **The current `.envrc` has not prepared this execution environment.** — observed. Direnv found and reports the same RC path as loaded, but both authorization booleans are false and the project venv is absent from `PATH`.
4. **The revised census found only executable files among resolved tools.** — observed. No aliases, functions, or builtins were reported.
5. **Global ripgrep is executable and compatible with the observed fixture.** — observed. The version probe and heading search succeeded.
6. **Separate POSIX tool calls do not preserve shell mutations.** — observed. The variable and function were present in call A and absent in call B; this does not establish parent-shell inheritance behavior.
7. **The workspace has no Git worktree metadata.** — observed. `git rev-parse --show-toplevel` failed with exit `128`.
8. **Python is globally available, but project Python identity is unknown.** — observed / unknown. No active instruction selected a launcher for the identity check.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| Python identity program | No launcher selected by an active instruction |
| Git fixture status | `git rev-parse` did not establish a worktree |
| Behavioral probes for other tools | No active instruction, exact behavior, and safe fixture combination established |

## Unknowns

- Runtime version and exact launch path.
- OS distribution/version beyond the POSIX/Linux-like paths visible to the probe.
- Parent-shell/runtime inheritance behavior for environment setup.
- Behavioral compatibility of discovered tools not covered by the fixture-backed checks.

## Candidate implications

These are provisional observations for the solution catalogue, not rankings. The result supports examining declared prerequisites plus bare-command verification, runtime-native session environment handoff, and project-local runtime environment configuration. The Codex-resolved `rg` path is evidence to examine runtime-bundled tool reliance, not proof that the bundle is a cross-surface contract.
