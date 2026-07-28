# Execution-environment probe: Claude Code / CLI / Linux / POSIX shell / source-like checkout

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v4-2026-07-28`
- Prior related report: none retained; this v4 run supersedes the removed v3 run for the same environment. Contrasting environments: [2026-07-28-codex-api-posix-linux-a1.md](./2026-07-28-codex-api-posix-linux-a1.md), [2026-07-28-codex-api-posix-linux-a4.md](./2026-07-28-codex-api-posix-linux-a4.md)

This is a fresh full run of the `v4` procedure in the same environment, not an edit of the `v3` report. All commands were re-executed; nothing was carried over.

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | `2026-07-28T09:55:13Z`; local timezone `CEST` (`+0200`) | observed |
| Runtime and surface | Claude Code, terminal CLI | documented |
| Runtime version | unknown (not exposed to the agent; no extra command run to obtain it) | unknown |
| OS and version | Linux `6.8.0-136-generic` | observed |
| Tool execution interface | POSIX shell, Bash `5.2.21(1)-release` (`/bin/bash`, process comm `bash`) | observed |
| Workspace/current directory | `/home/zby/llm/commonplace` | observed |
| Launch path | unknown | unknown |
| Sandbox/approval/write scope | tool calls run under a user-selected permission mode; Bash is sandboxed by default with an explicit escalation parameter; workspace and a session scratchpad directory are writable | documented |

## Observable layout

| Capability or path | Result | Basis |
|---|---|---|
| Runtime-supplied workspace root | `/home/zby/llm/commonplace` (declared primary working directory; matches tool-call cwd) | observed |
| `pyproject.toml` | present | observed |
| `kb/instructions/COLLECTION.md` | present | observed |
| `kb/commonplace/instructions/COLLECTION.md` | absent | observed |
| Known reader/vendor path | none named by loaded project instructions | observed |
| Project `.venv` at observed root | present | observed |
| Workspace `.envrc` | present | observed |

Provisional class: **Commonplace source-like checkout**

### Project-venv environment signals

| Signal | Result | Basis |
|---|---|---|
| Expected venv command directory | `/home/zby/llm/commonplace/.venv/bin` | observed |
| Expected venv command directory is on process `PATH` | true | observed |
| `VIRTUAL_ENV` | unset | observed |
| `VIRTUAL_ENV` identifies the observed project venv | false | observed |
| direnv marker variables set | `DIRENV_DIR`, `DIRENV_FILE`, `DIRENV_DIFF`, and `DIRENV_WATCHES` all set | observed |

Baseline provider attributed below under fixture-backed direnv state, not from marker presence alone.

## Universal bare-name probes

| Command | Result and exit status | Resolved source | Interpretation | Basis |
|---|---|---|---|---|
| `commonplace-validate --help` | usage text for the deterministic KB validator; exit `0` | `/home/zby/llm/commonplace/.venv/bin/commonplace-validate` | bare command resolves to the project venv entry point | observed |
| `rg --version` | `ripgrep 14.1.0` (PCRE2 10.42, JIT available); exit `0` | `/usr/bin/rg` | bare command resolves to a system executable, not a runtime-bundled or project copy | observed |

Expected venv entry point check: observed `expected_venv_entrypoint=true` for `.venv/bin/commonplace-validate`.

## Tool-call persistence

Applicable interface: yes

| Observation | First call | Second call | Interpretation |
|---|---|---|---|
| PID | `254016` | `254021` | context only; differing PIDs are consistent with fresh processes |
| Working directory | `/home/zby/llm/commonplace` | `/home/zby/llm/commonplace` | context only; not mutated by Round 1 |
| Probe environment variable | `present` | empty/unset | did not persist |
| Probe shell function | present (kind: function) | not found | did not persist |

Conclusion and basis: observed — the deliberately mutated shell state (`COMMONPLACE_SHELL_PROBE` and `commonplace_shell_probe_function`) did not survive into the next tool call. Each call receives a fresh shell process. The project venv command directory was nevertheless on `PATH` in every call, so the baseline environment is supplied per call rather than carried by a persistent shell. This rules out establishing activation-like state *inside* a tool call; it says nothing about whether a runtime launched from an already-activated parent shell would pass that baseline down to each fresh child.

## Tool discovery

Kinds are recorded per the `v4` census; alias targets and function definitions are deliberately not reproduced.

| Name | Resolution | Kind/source | Behavior verified? | Basis |
|---|---|---|---|---|
| `python` | `/home/zby/llm/commonplace/.venv/bin/python` | file, project venv | no | observed |
| `python3` | `/home/zby/llm/commonplace/.venv/bin/python3` | file, project venv | yes: version and identity program (below) | observed |
| `py` | absent | — | no | observed |
| `pytest` | `/home/zby/llm/commonplace/.venv/bin/pytest` | file, project venv | no | observed |
| `uv` | `/home/zby/.local/bin/uv` | file, user-local | no | observed |
| `direnv` | `/usr/bin/direnv` | file, system | yes: `direnv status` (below) | observed |
| `git` | `/usr/bin/git` | file, system | yes: root and bounded fixture status (below) | observed |
| `find` | no path | **function** — a shell function supplied by the runtime's shell initialization, not the system `find(1)` executable | no | observed |
| `sed` | `/usr/bin/sed` | file, system | no | observed |
| `xargs` | `/usr/bin/xargs` | file, system | no | observed |
| `wc` | `/usr/bin/wc` | file, system | no | observed |
| `sort` | `/usr/bin/sort` | file, system | no | observed |
| `curl` | `/usr/bin/curl` | file, system | no | observed |
| `roughdraft` | `/home/zby/.npm-global/bin/roughdraft` | file, npm-global | no | observed |
| `qmd` | `/home/zby/.npm-global/bin/qmd` | file, npm-global | no | observed |
| `ruff` | `/home/zby/llm/commonplace/.venv/bin/ruff` | file, project venv | no | observed |
| `mkdocs` | `/home/zby/llm/commonplace/.venv/bin/mkdocs` | file, project venv | no | observed |
| `sqlite3` | `/usr/bin/sqlite3` | file, system | no | observed |
| `jq` | `/usr/bin/jq` | file, system | no | observed |
| `gh` | `/usr/bin/gh` | file, system | no | observed |
| `codex` | `/home/zby/.npm-global/bin/codex` | file, npm-global | no | observed |
| `claude` | `/home/zby/.local/bin/claude` | file, user-local | no | observed |

`find` is the only non-`file` resolution in the census. Its kind alone establishes that a discovered name in this channel need not be the ordinary executable, without recording the wrapper's implementation.

## Fixture-backed behavior

### ripgrep

- Observed instruction root: `kb/instructions` (source-like)
- Exact search: `rg -n -m 1 --glob '*.md' '^# ' "$instruction_root"` with `instruction_root=kb/instructions`
- Result: exit `0`; 35 first-heading matches across the instruction tree, including `kb/instructions/ingest-directory.md:6:# Ingest a directory` and `kb/instructions/compression-bundle/README.md:1:# Compression bundle`. Recursion, glob filtering, anchored patterns, and the `-m` limit all behaved as the instruction expects.

### direnv state

- Workspace `.envrc` found by direnv: yes (`Found RC path` is the workspace `.envrc`)
- Workspace `.envrc` allowed: yes
- Loaded RC identity: current workspace
- Expected project-venv command directory on `PATH`: yes
- Baseline-provider interpretation and basis: observed — the "found here, allowed, loaded here, venv present on `PATH`" combination, which the procedure marks as consistent with direnv preparing the current baseline. Point-in-time for one tool process; it does not prove a fresh session, a different launcher, or a later directory change will execute the hook.

### Python identity

- Launcher selected by an active instruction: `python3` (project `AGENTS.md`/`CLAUDE.md` instructs "Use `python3`" for stdlib tooling, and directs calling `commonplace-*` and `pytest` by bare name on Linux/macOS)
- Invocation: `python3 -c "import os,sys; print('executable='+sys.executable); print('prefix='+sys.prefix); print('base_prefix='+sys.base_prefix); print('VIRTUAL_ENV='+str(os.environ.get('VIRTUAL_ENV')))"`
- Result: `python3 --version` reports `Python 3.13.1`; `executable=/home/zby/llm/commonplace/.venv/bin/python3`; `prefix=/home/zby/llm/commonplace/.venv`; `base_prefix=/home/zby/.local/share/uv/python/cpython-3.13.1-linux-x86_64-gnu`; `VIRTUAL_ENV=None`. The bare launcher is the project venv interpreter (uv-provided CPython base) even though `VIRTUAL_ENV` is unset.

### Git

- Repository root: `/home/zby/llm/commonplace` (`git rev-parse --show-toplevel`, exit `0`); the workspace is a Git worktree
- Single-fixture status command and result: `git status --short -- kb/instructions/COLLECTION.md` — exit `0`, empty output (fixture unmodified). Bounded status access works; the wider worktree state was not characterized.

## Findings

1. **The workspace is a Commonplace source-like checkout.** — observed. `pyproject.toml` and `kb/instructions/COLLECTION.md` present, `kb/commonplace/instructions/COLLECTION.md` absent, plus `.venv` and `.envrc`.
2. **Bare-name project commands work: `commonplace-validate` resolves to the project venv.** — observed. The opposite result from the initialized-project Codex reports, where the same bare command was not found despite an existing venv entry point.
3. **The project venv command directory is on `PATH` in every fresh tool call while `VIRTUAL_ENV` is unset.** — observed. Confirms the procedure's warning that an unset `VIRTUAL_ENV` is not evidence that no environment preparation occurred.
4. **direnv is the plausible baseline provider here, established from status fields rather than marker presence.** — observed. `.envrc` found here, allowed, and loaded here, with the venv `bin` on `PATH`.
5. **Separate POSIX tool calls do not preserve shell mutations.** — observed. The probe variable and function existed in call A and were absent in call B, with differing PIDs. What makes bare names work is per-call baseline injection, not retained state.
6. **`find` resolves to a runtime-supplied shell function, not an executable.** — observed via the `v4` kind classification. A name appearing in the census is not evidence of the conventional tool's identity or semantics; only the kind was recorded.
7. **`rg` is the system copy, not a runtime-bundled binary.** — observed. `/usr/bin/rg` 14.1.0, contrasting with the Codex environment where `rg` resolved inside the Codex npm package vendor directory. Tool provenance is channel-dependent.
8. **Project Python identity is established by bare launcher.** — observed. `python3` is CPython 3.13.1 inside the project venv; `python`, `pytest`, `ruff`, and `mkdocs` also resolve there.
9. **Git metadata and bounded status access are available.** — observed. Worktree root established; single-fixture status succeeded.
10. **Repeating the probe in the same environment reproduced every `v3` result.** — observed. Across the two runs, only PIDs and the timestamp differed; the `v4` additions (kind classification, version capture) added detail without contradicting the earlier report.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| Runtime version | Not exposed to the agent; the procedure forbids adding a command merely to fill an identity field |
| Launch path | Not visible to the agent |
| PowerShell branches of steps 3, 5, 6, 7 | Interface is a POSIX shell |
| `cmd.exe` / direct-execution branches of steps 3, 5, 7 | Interface is a POSIX shell |
| Reader/vendor path readability | No vendor path named by loaded project instructions |
| Behavioral probes for the remaining census tools (`python`, `pytest`, `uv`, `sed`, `xargs`, `wc`, `sort`, `curl`, `roughdraft`, `qmd`, `ruff`, `mkdocs`, `sqlite3`, `jq`, `gh`, `codex`, `claude`) | No active instruction, exact relied-on behavior, and safe fixture combination established |
| Launcher-inheritance test (does a runtime started from an activated parent shell pass that baseline to fresh children?) | Requires launching a second session under controlled conditions; out of scope for Round 1 and for a probe forbidden to relaunch environments |

## Unknowns

- Claude Code version and the exact launch path of this session.
- Whether the same `PATH` baseline appears in sessions started by other means (desktop app, IDE extension, web, cron/headless) or from a different starting directory.
- Which mechanism actually injects the venv `PATH` entry into each fresh tool process — the direnv hook itself, or an environment inherited from the launching parent. The status fields are consistent with direnv but do not isolate the mechanism, and failed mutation persistence does not test inheritance.
- Whether census names other than `find` are also runtime-supplied wrappers behind an executable path; the kind check only distinguishes non-`file` resolutions.
- Behavioral compatibility of discovered tools beyond `rg`, `direnv`, `git`, and `python3`.

## Candidate implications

Provisional, for one environment only; not a ranking. See [the solution catalogue](../solution-catalogue.md).

- Positive control for **option 1 (declared prerequisites plus bare-command session verification)**: a cheap bare-name probe distinguished this channel from the Codex initialized-project channel, where the same command was absent despite an equivalent venv entry point.
- Direct evidence for **option 4 (project-local runtime environment configuration)**: an allowed, loaded `.envrc` yields working bare names in every call without any persistent shell.
- Finding 5 constrains **option 2 (launch the agent runtime from an activated project shell)** in one direction only: activation cannot be performed inside a tool call and reused. Whether launching from an activated shell works remains untested here, so this report neither supports nor refutes that option.
- Finding 7 weakens **option 13 (runtime-bundled tool reliance)** as a cross-surface contract: `rg` came from the runtime bundle under Codex and from `/usr/bin` here.
- Finding 6 is evidence for **option 6 (project-aware global dispatcher shims)**: shims already exist in this channel, installed by the runtime rather than by Commonplace, so a dispatcher strategy would be layering onto an occupied namespace.
