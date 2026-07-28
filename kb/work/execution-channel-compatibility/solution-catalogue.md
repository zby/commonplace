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

### 2. Launch the agent runtime from an activated project shell

The operator activates `.venv`, then starts `codex` or `claude` as a child of that shell.

- Strength: simple, project-scoped, and already works for command-line runtimes whose later subprocesses inherit the runtime environment.
- Limitation: unsuitable for an already-running desktop singleton, ambiguous for IDE/app launch brokers, and one process environment cannot represent several simultaneous project venvs.

### 3. Runtime-native session environment handoff

A session hook writes environment changes into a runtime-owned channel that is applied to every later tool subprocess.

- Strength: matches the actual fresh-process execution model and keeps environment project/session scoped.
- Limitation: runtime-specific. Claude exposes `CLAUDE_ENV_FILE`; current Codex `SessionStart` needs verification for any equivalent before this can be treated as portable.
- Open design: whether Commonplace should request or depend on a Codex environment-file/output capability.

### 4. Project-local runtime environment configuration

The runtime config declares environment overrides for subprocesses, such as Codex `shell_environment_policy`.

- Strength: applies centrally to tool calls without rewriting instructions.
- Limitation: an explicit `PATH` replacement is machine-specific unless the runtime supports project-relative prepend plus inherited-value composition. Trust, configuration precedence, and worktree resolution also matter.

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
- Limitation: `.envrc` presence is inert until authorized, and marker variables do not prove the current file was applied. Native Windows and desktop application launches do not provide a portable direnv baseline; agent runtimes may inherit a launcher's prepared environment without running the directory hook themselves. Multi-project switching and worktree authorization therefore remain runtime- and launch-path-dependent.
- Evidence boundary: the allowed Claude Code report and unallowed Codex initialized-project report establish opposite effective environments. They do not isolate whether the agent runtime executes the hook or merely inherits its parent process environment.

## Likely compositions to test

These are hypotheses, not rankings:

1. **Verifier + inherited environment for CLI + runtime handoff for managed surfaces.** Minimal when every runtime supplies environment propagation.
2. **Verifier + project-aware shims for Windows desktop + inherited environment elsewhere.** Preserves bare commands without global project selection.
3. **Verifier + portable package commands + declared `rg`/Git prerequisites.** Absorb only shell semantics that are load-bearing and retain established external tools.
4. **Verifier + full executable-instruction compilation + an availability mechanism.** Compilation resolves wording/syntax; environment or shims resolve command discovery.
5. **Standardized POSIX substrate + portability checks.** Reject native shell parity and make the support boundary explicit.
6. **Verifier + directory-aware manager on POSIX + a separate native-Windows mechanism.** Retain the proven current path where it operates, while treating Windows desktop command discovery as an independent problem rather than pretending `.envrc` is cross-platform.

## Evidence needed before selection

- Whether each Codex and Claude surface inherits the launcher environment and whether it reuses one process across projects.
- Whether a runtime-native environment handoff exists and survives resume/compact/worktree transitions.
- Whether Codex project configuration can prepend a project-relative directory to inherited `PATH` without copying the machine's full path.
- Whether `PreToolUse` command rewriting preserves normal approval and sandbox semantics.
- Whether runtime-bundled `rg` is a documented contract on every supported surface.
- Whether each agent surface executes a directory-environment hook, inherits an already prepared launcher environment, or ignores project directory changes; repeat for unallowed files, worktrees, and multi-project switching.
- How many shell constructs remain after package-owned operations are separated from ordinary navigation.
- How generated instructions are checked, reviewed, updated, and excluded from duplicate search results.
