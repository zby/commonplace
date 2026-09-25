# Execution-environment probe: <runtime / surface / OS / interface>

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v7-2026-09-25`
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
| Runtime started after last install / `uv tool update-shell` | yes / no / unknown | stated / unknown |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | | observed / unknown |
| `pyproject.toml` | | observed / not run |
| `kb/instructions/COLLECTION.md` | | observed / not run |
| `.commonplace/library.md` | | observed / not run |
| `kb/commonplace/instructions/COLLECTION.md` (legacy copy) | | observed / not run |
| `.claude/skills/`, `.agents/skills/` | | observed / not run |
| Known reader/vendor path | | observed / unknown |
| Legacy residue: workspace `.venv` / `.envrc` (presence only) | | observed / not run |

Provisional class (all that match): source-like / initialized-project-like / legacy-copied-library / reader/vendor / package-only / other / unknown

## Library reachability

Complete only when `.commonplace/library.md` was observed.

| Observation | Result | Basis |
|---|---|---|
| `.commonplace/library.md` readable | | observed |
| Library root named (normalized) | | observed |
| Skills listed in the index (count only) | | observed |
| `<library root>/instructions/COLLECTION.md` readable by file-read tool | yes / denied / not found / prompt declined | observed |
| Sampled skill stub: name, names an absolute library path, target readable | | observed / not run |

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | | | | observed / unknown |
| `rg --version` | | | | observed / unknown |

Init-output warning printed by `commonplace-validate --help`: none / <class only>

## Command authority

| Observation | Result | Basis |
|---|---|---|
| `uv` resolved | | observed / not run |
| `uv tool dir --bin` (normalized) | | observed / not run |
| Resolved `commonplace-validate` is inside `<UV_TOOL_BIN>` | yes / no — shadowed by <normalized path> / not resolved | observed / unknown |
| `<UV_TOOL_BIN>` is on process `PATH` | | observed / not run |
| `commonplace-init --check` exit status and finding classes | | observed / not run |

Interpretation (not installed / installed but not visible to this process / shadowed / expected authority / unknown) and basis:

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

- Observed instruction root (workspace `kb/instructions`, `<library root>/instructions`, or vendor root; normalized):
- Exact search:
- Result (record a sandbox denial for an outside-workspace root separately):
- Or not run because:

### Python identity

- Launcher selected by an active instruction:
- Version, `sys.executable`, and environment identity:
- Or not run because:

### Git

- Repository root:
- Single-fixture status command (`--ignored`) and result:
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
