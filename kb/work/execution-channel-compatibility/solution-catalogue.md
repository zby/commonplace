# Execution-channel solution catalogue

## Purpose

This is an option inventory, not a recommendation. Several mechanisms may compose because they act at different layers: installation can ensure a tool exists, environment propagation can make it discoverable, compilation can make an instruction literal for one shell, and a portable package entry point can remove a shell utility dependency entirely.

Every option must eventually be tested against the same worked cases: bare `commonplace-validate --help`, bare `rg`, a compound Bash-shaped procedure, native Windows Codex desktop execution, and two simultaneous projects or worktrees.

## Evaluation dimensions

- can be investigated and verified from each target environment without assuming a source checkout, fixed content path, writable repository, or unavailable shell/tool;
- preserves bare command names used by instructions;
- remains project-scoped across multiple projects and worktrees;
- works in CLI, IDE, desktop, and cloud surfaces;
- handles fresh subprocesses rather than assuming a persistent shell;
- covers external tools as well as Commonplace's Python entry points;
- avoids global version conflicts;
- preserves sandbox and approval behavior;
- keeps failure loud and remediation actionable;
- avoids per-use LLM translation and unnecessary context;
- has a clear canonical source, update path, and review target.

## Options

### 1. Declared prerequisites plus bare-command session verification

Installation instructions tell the operator how to establish the tool environment. Session start invokes the same bare commands later instructions use and reports failure.

- Strength: tests the effective channel rather than inferring it from `.venv` existence.
- Limitation: detects but does not provide missing command discovery.
- Role: necessary control for every other option, not a complete solution alone.

### 2. Launch the agent runtime with a project-prepared environment

The operator starts `codex` or `claude` as a child of a process whose environment already prepends the current project's venv command directory. Activation is one implementation, not the mechanism itself. Candidate implementations include:

- activate `.venv`, then launch the runtime from that shell;
- use a native wrapper that establishes the project root, verifies `.venv`, temporarily prepends `.venv/bin` or `.venv\Scripts`, optionally sets `VIRTUAL_ENV`, and launches the runtime;
- for a project actually managed as a uv project, use `uv run -- codex ...` so uv supplies the project environment to the child process.

Python documents activation as prepending the venv's command directory to `PATH` and setting `VIRTUAL_ENV`; running installed scripts does not otherwise require the activation script. A native PowerShell wrapper can therefore provide the relevant child-process environment without executing `Activate.ps1`. Its root-discovery algorithm must not silently make Git a new prerequisite: accept an explicit root or establish another bounded project-root rule when Git is unavailable.

The uv variant has a different ownership boundary. Ordinary `uv run` locks and synchronizes the project before launching the command. That can create or update project/environment state, so it is not merely a session-start activation substitute and conflicts with this workshop's installation/session separation. `uv run --no-sync -- codex ...` is a candidate for an already installed environment, but whether `--frozen` is also required to preclude lockfile updates needs a worked probe. The Commonplace source checkout retains `uv.lock`, making this candidate concrete there; initialized projects and package-only installs may not expose the same uv project state, so it cannot yet be treated as the cross-layout launcher.

For Codex CLI tests, `-c allow_login_shell=false` is an orthogonal hardening option: current Codex documentation says it rejects login-shell requests and makes omitted requests non-login, reducing the chance that a profile rewrites the inherited baseline. It does not create or hand off the project environment. Codex documents `shell_environment_policy.inherit = "all"` as the default for spawned processes, but the probe must still establish actual inheritance on each surface.

- Strength: project-scoped, requires no change to the later bare commands, and is directly testable for command-line runtimes.
- Limitation: `uv` or a profile wrapper must itself be installed and discoverable before launch. These launchers start the CLI; they do not prepare an already-running desktop singleton or prove that an IDE/application launch broker preserves the child environment. One runtime process also cannot represent several project venvs simultaneously.

### 3. Runtime-native session environment handoff

A session hook writes environment changes into a runtime-owned channel that is applied to every later tool subprocess.

- Strength: matches the actual fresh-process execution model and keeps environment project/session scoped.
- Limitation: runtime-specific. Claude exposes `CLAUDE_ENV_FILE`; current Codex `SessionStart` needs verification for any equivalent before this can be treated as portable.
- Open design: whether Commonplace should request or depend on a Codex environment-file/output capability.

### 4. Project-local runtime environment configuration

The runtime config declares environment overrides for subprocesses, such as Codex `shell_environment_policy`.

- Strength: applies centrally to tool calls without rewriting instructions.
- Limitation: an explicit `PATH` replacement is machine-specific unless the runtime supports project-relative prepend plus inherited-value composition. Current Codex configuration documents inherited-environment selection and literal overrides, but not project-relative `PATH` prepend/interpolation. Trust, configuration precedence, worktree resolution, and desktop-app behavior also matter.

### 5. Persistent user or machine `PATH`

Add a venv or command directory to the Windows user/system environment so desktop applications see it.

- Strength: reaches applications that do not inherit an interactive shell.
- Limitation: globally selecting one project's `.venv\Scripts` breaks project isolation and version identity; changes may require restarting applications or signing in again. Do not conflate this with venv activation, which changes only one process tree.

### 6. Project-aware global dispatcher shims

Install stable bare-name shims in a user-level directory already on `PATH`. Each shim finds the nearest project root and delegates to that project's `.venv/bin` or `.venv\Scripts` executable.

- Strength: preserves bare command names in desktop applications while selecting the venv from each tool call's working directory.
- Limitation: requires a trustworthy global install/update mechanism, careful root discovery, complete command coverage, and explicit behavior outside a project. `pytest` and non-Commonplace tools complicate the boundary.

### 7. Explicit venv executable paths

Instructions invoke `.venv/bin/commonplace-validate` or `.venv\Scripts\commonplace-validate.exe`.

- Strength: direct and independent of inherited `PATH`.
- Limitation: violates the desired identical bare command surface, branches by channel, leaks installation layout into every instruction, and increases context and maintenance cost.

### 8. Per-tool environment prefix or command rewrite

Before each shell tool call, prepend the project venv and cache variables using shell-native syntax, potentially through a `PreToolUse` hook.

- Strength: works with fresh subprocesses even when session start cannot persist environment.
- Limitation: adds per-call overhead and runtime-specific shell rewriting; hook trust, approval preservation, quoting, compound commands, and non-shell tool paths need proof.

### 9. Portable package entry points absorb shell logic

Move load-bearing `find`/`xargs`/`sed`/pipeline behavior behind tested `commonplace-*` Python commands. Instructions call one stable console entry point.

- Strength: package-owned semantics can be tested on POSIX and Windows; removes silent shell translation and utility-flag differences.
- Limitation: does not solve discovery of the `commonplace-*` entry point itself and should not absorb ordinary navigation merely to avoid declaring a common prerequisite such as `rg`.

### 10. Paired channel-specific literal procedures

Canonical instructions carry separate POSIX and PowerShell commands, clearly labelled and behaviorally tested.

- Strength: explicit, reviewable, and does not require a compiler.
- Limitation: every consumer carries irrelevant branches; parity drifts; the agent still selects the branch; the surface grows across all executable instructions.

### 11. Channel-compiled instruction artifacts

At install, session start, or explicit refresh, resolve canonical instructions into a channel-specific literal form.

Possible compilation boundaries:

- promoted skills only;
- all canonical instructions that invoke tools;
- those instructions plus required linked references;
- the control plane and install/operator guidance as well.

- Strength: removes runtime branching and can emit shell-native commands and path conventions.
- Limitation: compilation does not install or expose tools. It creates derived copies, review/freshness obligations, search duplication, update drift, and a source-checkout problem. The initial inventory already shows that promoted skills alone are too narrow.

### 12. Standardized execution environment

Declare WSL, a dev container, a managed image, or another POSIX environment as the execution substrate even on Windows.

- Strength: sharply reduces shell and tool variance and may preserve existing instructions unchanged.
- Limitation: narrows supported channels, imposes operator/runtime setup, and does not automatically solve environment inheritance inside the chosen substrate.

### 13. Runtime-bundled tool reliance

Treat a tool bundled by an agent runtime—potentially `rg`—as available without separate project installation.

- Strength: zero project setup where the bundle is contractual.
- Limitation: bundling may differ by runtime, surface, version, or sandbox and may be undocumented. A bundled binary is not necessarily exposed under the expected bare name or with the required behavior.

### 14. Commonplace-managed tool installation

Installation ensures required third-party tools are present, either in the project environment or a managed tool directory.

- Strength: makes availability explicit and versionable.
- Limitation: Python venvs do not naturally own native utilities such as `rg` and Git; platform packaging, licenses, updates, caches, and executable discovery become Commonplace responsibilities.

### 15. Capability-shaped instructions with deterministic dispatch

Canonical instructions name required operations rather than shell spellings; a deterministic resolver selects a registered implementation based on verified capabilities.

- Strength: separates semantic intent from shell syntax and can combine package commands, native tools, or runtime facilities.
- Limitation: risks recreating a compiler/runtime abstraction with a large mapping surface; only justified where repeated operations and verified implementations exist.

### 16. Directory-aware shell environment manager

A shell hook such as direnv reads authorized project-local configuration on directory entry and prepares the environment before bare commands run.

- Strength: project-scoped and already proven in the POSIX source-checkout reports. An allowed and loaded `.envrc` placed `.venv/bin` on the baseline `PATH` received by every fresh Claude Code tool shell, without requiring persistent shell state.
- Limitation: `.envrc` presence is inert until authorized, and marker variables do not prove the current file was applied. Direnv publishes a Windows binary/package path and a PowerShell hook, so native Windows is a real candidate rather than an automatic rejection. However, its own overview still states a Unix-like OS prerequisite, and `.envrc` remains Bash evaluated in a Bash subprocess. Open native-PowerShell/Bash-discovery and Git-Bash path-conversion reports make it unsuitable as a presumed cross-platform contract without a current Windows probe. Desktop application launches also do not automatically receive an interactive-shell hook. Multi-project switching and worktree authorization therefore remain runtime- and launch-path-dependent.
- Evidence boundary: the allowed Claude Code report and unallowed Codex initialized-project report establish opposite effective environments. They do not isolate whether the agent runtime executes the hook or merely inherits its parent process environment.

## Native Windows Codex application boundary

The current Codex documentation narrows what the launcher proposals can claim:

- the Windows app uses the native Windows agent with PowerShell by default, or can switch the agent to WSL after an application restart;
- its integrated-terminal selection is independent of the agent execution environment;
- project local-environment setup scripts run in the agent environment when a worktree is created, while actions run in the integrated terminal;
- the documentation does not state that either mechanism can export a project environment into all later agent tool calls.

Therefore `uv run codex`, venv activation followed by `codex`, and a PowerShell `codexv` function are CLI candidates, not answers to the workshop's native Windows desktop forcing case. A profile-wide venv activation is also rejected because it globally selects one project. The desktop candidates still needing evidence are runtime-native project configuration or handoff, project-aware global dispatch shims, a documented app-local environment mechanism with persistent tool-call effects, or selecting WSL as the standardized substrate.

## Likely compositions to test

These are hypotheses, not rankings:

1. **Verifier + inherited environment for CLI + runtime handoff for managed surfaces.** Minimal when every runtime supplies environment propagation.
2. **Verifier + project-aware shims for Windows desktop + inherited environment elsewhere.** Preserves bare commands without global project selection.
3. **Verifier + portable package commands + declared `rg`/Git prerequisites.** Absorb only shell semantics that are load-bearing and retain established external tools.
4. **Verifier + full executable-instruction compilation + an availability mechanism.** Compilation resolves wording/syntax; environment or shims resolve command discovery.
5. **Standardized POSIX substrate + portability checks.** Reject native shell parity and make the support boundary explicit.
6. **Verifier + directory-aware manager on POSIX + a separate native-Windows mechanism.** Retain the proven current path where it operates, while treating Windows desktop command discovery as an independent problem rather than pretending `.envrc` is cross-platform.
7. **Verifier + project-prepared launcher for CLIs + a separate desktop mechanism.** Use activation, a native wrapper, or a proven no-sync uv invocation only where the runtime is launched as a child; do not generalize CLI inheritance to the Windows app.

## Evidence needed before selection

- Whether each Codex and Claude surface inherits the launcher environment and whether it reuses one process across projects.
- Whether a runtime-native environment handoff exists and survives resume/compact/worktree transitions.
- Whether Codex project configuration can prepend a project-relative directory to inherited `PATH` without copying the machine's full path.
- Whether `PreToolUse` command rewriting preserves normal approval and sandbox semantics.
- Whether runtime-bundled `rg` is a documented contract on every supported surface.
- Whether each agent surface executes a directory-environment hook, inherits an already prepared launcher environment, or ignores project directory changes; repeat for unallowed files, worktrees, and multi-project switching.
- How many shell constructs remain after package-owned operations are separated from ordinary navigation.
- How generated instructions are checked, reviewed, updated, and excluded from duplicate search results.
- Whether `uv run --no-sync` uses the already installed Commonplace venv without creating/updating a lockfile or environment in every supported layout; if not, whether a non-mutating uv invocation exists or uv belongs only to a different install model.
- Whether `allow_login_shell = false` plus the documented inherited-environment default preserves a launcher-prepared venv across actual Codex CLI tool calls on native Windows.
- Whether Windows app local-environment setup scripts affect later agent tool calls or only perform worktree setup, and whether the application exposes any supported per-project environment handoff.

## Documentation grounding for candidate mechanics

- [Codex configuration reference](https://developers.openai.com/codex/config-reference) — `allow_login_shell`, `shell_environment_policy`, and CLI `--cd`/`-C` behavior.
- [Codex Windows app](https://learn.chatgpt.com/docs/windows/windows-app) and [local environments](https://learn.chatgpt.com/docs/environments/local-environment) — native PowerShell versus WSL agent execution, the independent integrated terminal, worktree setup scripts, and actions.
- [uv project command execution](https://docs.astral.sh/uv/concepts/projects/run/) and [locking/synchronizing](https://docs.astral.sh/uv/concepts/projects/sync/) — arbitrary child commands, automatic lock/sync, `--no-sync`, and `--frozen`.
- [Python virtual environments](https://docs.python.org/3/library/venv.html) — platform command directories, activation effects, direct script execution, and non-portability of venv directories.
- [direnv installation](https://direnv.net/docs/installation.html), [shell hooks](https://direnv.net/docs/hook.html), and [execution model](https://direnv.net/man/direnv.1.html) — Windows packaging, the PowerShell hook, authorization, and Bash-subprocess evaluation of `.envrc`.
