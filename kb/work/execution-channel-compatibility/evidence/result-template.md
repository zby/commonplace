# Execution-environment probe: <runtime / surface / OS / interface>

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v6-2026-07-28`
- Prior related report: none / path

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | | observed / unknown |
| Runtime and surface | | observed / documented / unknown |
| Runtime version | | observed / unknown |
| OS and version | | observed / unknown |
| Tool execution interface | | observed / documented / unknown |
| Workspace/current directory | | observed |
| Launch path | | observed / unknown |
| Sandbox/approval/write scope | | observed / unknown |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | | observed / unknown |
| `pyproject.toml` | | observed / not run |
| `kb/instructions/COLLECTION.md` | | observed / not run |
| `kb/commonplace/instructions/COLLECTION.md` | | observed / not run |
| Known reader/vendor path | | observed / unknown |
| Project `.venv` at observed root | | observed / not run |
| Workspace `.envrc` | | observed / not run |

Provisional class: source-like / initialized-full-project-like / reader/vendor / package-only / other / unknown

### Project-venv environment signals

Complete only when a project `.venv` was observed.

| Signal | Result | Basis |
|---|---|---|
| Expected venv command directory | | observed / not run |
| Expected venv command directory is on process `PATH` | | observed / not run |
| `VIRTUAL_ENV` | | observed / not run |
| `VIRTUAL_ENV` identifies the observed project venv | | observed / not run |
| direnv marker variables set | | observed / not run |

Marker presence alone does not identify the baseline provider. Do not include marker values or `.envrc` contents.

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | | | | observed / unknown |
| `rg --version` | | | | observed / unknown |

Expected venv entry point check: observed result / not run because no project venv was observed

## Tool-call persistence

Applicable interface: yes / no

| Observation | First call | Second call | Interpretation |
|---|---|---|---|
| PID | | | context only; equality is inconclusive |
| Working directory | | | context only; not mutated by Round 1 |
| Probe environment variable | | | |
| Probe shell function | | | |

Conclusion and basis:

Use only the mutated variable and function to determine shell-state persistence.

## Tool discovery

| Name | Resolution | Kind/source | Behavior verified? | Basis |
|---|---|---|---|---|
| `python` | | | | observed / not run |
| `python3` | | | | observed / not run |
| `py` | | | | observed / not run |
| `pytest` | | | | observed / not run |
| `uv` | | | | observed / not run |
| `direnv` | | | | observed / not run |
| `git` | | | | observed / not run |
| `find` | | | | observed / not run |
| `sed` | | | | observed / not run |
| `xargs` | | | | observed / not run |
| `wc` | | | | observed / not run |
| `sort` | | | | observed / not run |
| `curl` | | | | observed / not run |
| `roughdraft` | | | | observed / not run |
| `qmd` | | | | observed / not run |
| `ruff` | | | | observed / not run |
| `mkdocs` | | | | observed / not run |
| `sqlite3` | | | | observed / not run |
| `jq` | | | | observed / not run |
| `gh` | | | | observed / not run |
| `codex` | | | | observed / not run |
| `claude` | | | | observed / not run |

## Fixture-backed behavior

### ripgrep

- Observed instruction root:
- Exact search:
- Result:
- Or not run because:

### direnv state

- Workspace `.envrc` found by direnv: yes / no / unknown
- Workspace `.envrc` allowed: yes / no / unknown
- Loaded RC identity: current workspace / different workspace / none / unknown
- Expected project-venv command directory on `PATH`: yes / no / not run
- Baseline-provider interpretation and basis:
- Or not run because:

Do not include raw status output, watch entries, timestamps, `allowPath`, hashes, marker values, or `.envrc` contents.

### Python identity

- Launcher selected by an active instruction:
- Version, `sys.executable`, and environment identity:
- Or not run because:

### Git

- Repository root:
- Single-fixture status command and result:
- Or not run because:

## Findings

Number findings so later synthesis can cite them.

1. **<finding>** — observed / documented / inferred / unknown. Evidence: ...

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| | |

## Unknowns

- <what the current agent could not establish>

## Candidate implications

Link relevant options from [the solution catalogue](../solution-catalogue.md). Keep implications provisional: this report describes one environment and does not rank solutions.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes / not applicable
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent
- Optional automated scan: not run / passed / findings redacted
- Withheld or residual sensitive-looking material: none / <non-sensitive description and reason>
