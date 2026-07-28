# Execution-environment probe: Claude Code / CLI / Linux / POSIX shell / source-like checkout

- Survey round: `1 — landscape breadth`
- Procedure ID: `execution-channel-round1-v3-2026-07-28`
- Prior related report: none for this runtime; contrasting environment reports are [2026-07-28-codex-api-posix-linux-a1.md](./2026-07-28-codex-api-posix-linux-a1.md) and [2026-07-28-codex-api-posix-linux-a2.md](./2026-07-28-codex-api-posix-linux-a2.md)

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | `2026-07-28T09:46:03Z`; local timezone `CEST` (`+0200`) | observed |
| Runtime and surface | Claude Code, terminal CLI | documented |
| Runtime version | unknown (not exposed to the agent; no extra command run to obtain it) | unknown |
| OS and version | Linux `6.8.0-136-generic` | observed |
| Tool execution interface | POSIX shell, Bash (`/bin/bash`, process comm `bash`) | observed |
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
| PID | `251323` | `251398` | context only; differing PIDs are consistent with fresh processes |
| Working directory | `/home/zby/llm/commonplace` | `/home/zby/llm/commonplace` | context only; not mutated by Round 1 |
| Probe environment variable | `present` | empty/unset | did not persist |
| Probe shell function | function present (definition printed) | not found | did not persist |

Conclusion and basis: observed — deliberately mutated shell state (`COMMONPLACE_SHELL_PROBE` and `commonplace_shell_probe_function`) did not survive into the next tool call. Each call receives a fresh shell process. Nonetheless the project venv command directory was on `PATH` in every call, so the baseline environment is supplied per call rather than carried by a persistent shell.

## Tool discovery

| Name | Resolution | Kind/source | Behavior verified? | Basis |
|---|---|---|---|---|
| `python` | `/home/zby/llm/commonplace/.venv/bin/python` | executable, project venv | no | observed |
| `python3` | `/home/zby/llm/commonplace/.venv/bin/python3` | executable, project venv | yes: identity program (below) | observed |
| `py` | absent | — | no | observed |
| `pytest` | `/home/zby/llm/commonplace/.venv/bin/pytest` | executable, project venv | no | observed |
| `uv` | `/home/zby/.local/bin/uv` | executable, user-local | no | observed |
| `direnv` | `/usr/bin/direnv` | executable, system | yes: `direnv status` (below) | observed |
| `git` | `/usr/bin/git` | executable, system | yes: root and bounded fixture status (below) | observed |
| `find` | shell **function** shim, no path | Bash function installed by the runtime's shell profile; execs the Claude Code binary as `bfs` (`-S dfs -regextype findutils-default`), falling back to `command find` when that binary is missing | no | observed |
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
| `claude` | `/home/zby/.local/bin/claude` | executable, user-local | no | observed |

`find` is the only non-executable resolution: a runtime-injected Bash function, not the system `find(1)`. Its presence does not establish findutils semantics for this channel.

## Fixture-backed behavior

### ripgrep

- Observed instruction root: `kb/instructions` (source-like)
- Exact search: `rg -n -m 1 --glob '*.md' '^# ' "$instruction_root"` with `instruction_root=kb/instructions`
- Result: exit `0`; headings returned across the instruction tree, including `kb/instructions/COLLECTION.md:1:# Writing conventions for kb/instructions/ (prescriptive profile)`.

### direnv state

- Workspace `.envrc` found by direnv: yes (`Found RC path` is the workspace `.envrc`)
- Workspace `.envrc` allowed: yes
- Loaded RC identity: current workspace
- Expected project-venv command directory on `PATH`: yes
- Baseline-provider interpretation and basis: observed — found here, allowed, loaded here, and venv present on `PATH`. This is the "consistent with direnv preparing the current baseline" combination. It is a point-in-time observation for one tool process and does not prove that a fresh session or launcher will execute the hook.

### Python identity

- Launcher selected by an active instruction: `python3` (project `AGENTS.md`/`CLAUDE.md` instructs "Use `python3`" for stdlib tooling, and directs calling `commonplace-*` and `pytest` by bare name on Linux/macOS)
- Invocation: `python3 -c "import os,sys; print('executable='+sys.executable); print('prefix='+sys.prefix); print('base_prefix='+sys.base_prefix); print('VIRTUAL_ENV='+str(os.environ.get('VIRTUAL_ENV')))"`
- Result: `executable=/home/zby/llm/commonplace/.venv/bin/python3`; `prefix=/home/zby/llm/commonplace/.venv`; `base_prefix=/home/zby/.local/share/uv/python/cpython-3.13.1-linux-x86_64-gnu`; `VIRTUAL_ENV=None`. The bare launcher is the project venv interpreter (uv-provided CPython 3.13.1 base) even though `VIRTUAL_ENV` is unset.

### Git

- Repository root: `/home/zby/llm/commonplace` (`git rev-parse --show-toplevel`, exit `0`); the workspace is a Git worktree
- Single-fixture status command and result: `git status --short -- kb/instructions/COLLECTION.md` — exit `0`, empty output (fixture unmodified). Bounded status access works; the wider worktree state was not characterized.

## Findings

1. **The workspace is a Commonplace source-like checkout.** — observed. `pyproject.toml` and `kb/instructions/COLLECTION.md` present, `kb/commonplace/instructions/COLLECTION.md` absent, plus `.venv` and `.envrc`.
2. **Bare-name project commands work: `commonplace-validate` resolves to the project venv.** — observed. This is the opposite result from the initialized-project Codex reports, where the same bare command was not found despite an existing venv entry point.
3. **The project venv command directory is on `PATH` in every fresh tool call while `VIRTUAL_ENV` is unset.** — observed. Confirms the procedure's warning: an unset `VIRTUAL_ENV` is not evidence that no environment preparation occurred.
4. **direnv is the plausible baseline provider here, established by status fields rather than marker presence.** — observed. `.envrc` found here, allowed, and loaded here, with the venv `bin` on `PATH`.
5. **Separate POSIX tool calls do not preserve shell mutations.** — observed. The probe variable and function existed in call A and were absent in call B, with differing PIDs. Activation-style state cannot be established once and reused; per-call baseline injection is what makes bare names work.
6. **`find` is a runtime-injected Bash function shim, not the system executable.** — observed. The runtime's shell profile replaces `find` with a wrapper that execs the Claude Code binary as `bfs`. A discovered command name in this channel may be a runtime shim with different semantics; the census's "resolution" column is not evidence of tool identity.
7. **`rg` is the system copy, not a runtime-bundled binary.** — observed. `/usr/bin/rg` 14.1.0, contrasting with the Codex environment where `rg` resolved inside the Codex npm package vendor directory.
8. **Python identity is project-scoped by bare launcher.** — observed. `python3`, `pytest`, `ruff`, and `mkdocs` all resolve inside the project venv.
9. **Git metadata and bounded status access are available.** — observed. Worktree root established; single-fixture status succeeded.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| Runtime version | Not exposed to the agent; procedure forbids adding a command merely to fill an identity field |
| Launch path | Not visible to the agent |
| `cmd.exe` / direct-execution branches of steps 3, 5, 7 | Interface is a POSIX shell |
| PowerShell branches of steps 3, 5, 6, 7 | Interface is a POSIX shell |
| Reader/vendor path readability | No vendor path named by loaded project instructions |
| Behavioral probes for the remaining census tools (`uv`, `sed`, `xargs`, `wc`, `sort`, `curl`, `roughdraft`, `qmd`, `ruff`, `mkdocs`, `sqlite3`, `jq`, `gh`, `codex`, `claude`, `pytest`, `python`) | No active instruction, exact relied-on behavior, and safe fixture combination established |

## Unknowns

- Claude Code version and the exact launch path of this session.
- Whether the same `PATH` baseline would be present in a session launched by other means (desktop app, IDE extension, web, cron/headless), or from a different starting directory.
- Whether the direnv hook, rather than an inherited parent-shell environment, is what actually injects `PATH` into each fresh tool process; the status fields are consistent with direnv but do not isolate the mechanism.
- Whether other census names are also runtime shims; only `find` was classified as a function because only it failed to resolve to a path.
- Behavioral compatibility of discovered tools beyond `rg`, `direnv`, `git`, and `python3`.

## Candidate implications

Provisional, for one environment only; not a ranking. See [the solution catalogue](../solution-catalogue.md).

- This report is the positive control for **option 1 (declared prerequisites plus bare-command session verification)**: a cheap bare-name probe distinguished this channel from the Codex initialized-project channel where the same command was absent.
- It is direct evidence for **option 4 (project-local runtime environment configuration)**: an allowed, loaded `.envrc` yields working bare names per call without any persistent shell.
- Finding 5 constrains **option 2 (launch from an activated project shell)**: activation cannot be assumed to carry, since shell state is discarded between calls; what carries is whatever the runtime injects into each fresh process.
- Finding 7 weakens **option 13 (runtime-bundled tool reliance)** as a cross-surface contract: `rg` came from the runtime bundle under Codex and from `/usr/bin` here, so its provenance is channel-dependent.
- Finding 6 is evidence to examine under **option 6 (project-aware global dispatcher shims)**: shims are already in play in this channel, installed by the runtime rather than by Commonplace, and they can silently change a command's semantics.
