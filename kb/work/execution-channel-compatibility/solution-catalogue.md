# Execution-channel solution catalogue

## Purpose

This is an option inventory, not a recommendation. Several mechanisms may compose because they act at different layers: installation can ensure a tool exists, `PATH` propagation can make it discoverable, a portable package entry point can remove a shell utility dependency, and an instruction's wording can be made shell-neutral.

Every option must eventually be tested against the same worked cases: bare `commonplace-validate --help` in a freshly started process, bare `rg`, a compound Bash-shaped procedure, native Windows Codex desktop execution, reading a library file from an initialized project, and a second project or worktree.

## Rebaseline, 2026-09-25

The catalogue was first written on 2026-07-28, when `commonplace-*` commands came from each project's `.venv` and direnv put that venv on `PATH` (ADR 014). Two later decisions settled or removed several options:

- [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) installs the commands once per OS user as a uv tool. `uv tool update-shell` puts the tool executable directory on the user's `PATH`; already-running processes must be restarted to see it. One active Commonplace version per OS user is an accepted invariant. The project-venv discovery problem that options 2, 6, 7 and 16 addressed no longer exists.
- [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) keeps the library (instructions, types, skills) in the installed package and gives projects gitignored pointers to it. There are no per-project copies to compile or keep in sync. ADR 086 also rules out session hooks until they are standardised, and it rests on files plus `AGENTS.md` rather than any one harness.

Each option below now carries a **status**: *operative* (adopted by an ADR or shipped code), *active* (owned by an open plan), *open* (still a candidate), *fallback* (kept only for a runtime the adopted mechanism fails in), or *retired* (the problem it solved is gone, or an ADR rejected it). Retired entries stay so the reason is not lost; their July detail is in git history.

What remains open is narrower than in July:

1. **Command visibility per launch class.** Does each runtime surface (CLI, IDE extension, Windows desktop app, cloud) see the user `PATH` after `uv tool update-shell` and a full restart? ADR 064 records a positive Windows experiment for the launch classes it tested; other surfaces need a fresh-process check.
2. **Library reachability.** Can each runtime and its sandbox read files outside the workspace at the library root, by file-read tool and by shell?
3. **Shell dependence of instruction text.** Which load-bearing Bash constructs and POSIX utilities remain, promoted skills and the rest of the instruction collection alike.
4. **Non-Python tools.** Whether `rg`, Git and the other external tools are prerequisites, runtime-bundled, or replaceable, and who verifies them.

## Evaluation dimensions

- can be investigated and verified from each target environment without assuming a source checkout, fixed content path, writable repository, or unavailable shell/tool;
- preserves bare command names used by instructions;
- works with one user-level Commonplace version shared by all of a user's projects (ADR 064);
- works in CLI, IDE, desktop, and cloud surfaces, including a process started before the latest install;
- handles fresh subprocesses rather than assuming a persistent shell;
- covers external tools as well as Commonplace's Python entry points;
- lets an agent read library text at the installed root, inside the runtime's sandbox;
- preserves sandbox and approval behavior;
- keeps failure loud and remediation actionable;
- avoids per-use LLM translation and unnecessary context;
- keeps one canonical tree for library text (ADR 086), with a clear update path and review target;
- needs no hooks and no per-machine setup command beyond install and `commonplace-init` (ADR 086).

## Options

### 1. Declared prerequisites plus bare-command session verification — operative

Installation instructions tell the operator how to establish the tool environment. Verification invokes the same bare commands later instructions use and reports failure.

- Status: adopted by ADR 064. `cp-skill-health-check` checks bare-name resolution and ownership relative to `uv tool dir --bin`; every `commonplace-*` command also warns when init outputs are stale (ADR 086).
- Strength: tests the effective channel rather than inferring it from files on disk.
- Limitation: detects but does not provide command discovery. The health check's own preflight still contains POSIX-only blocks; [E1](../system-contract-consistency/plans/e1-windows-execution.md) owns pairing them.

### 2. Launch the agent runtime with a prepared environment — retired

Starting `codex` or `claude` from a shell that had activated the project venv, or through `uv run -- codex`, made the venv visible to that runtime. With commands in the user-level tool directory there is no project environment to prepare. The residue of this option is operational: after `uv tool update-shell`, start the runtime from a new process. ADR 064 states that requirement.

`uv run` stays the authority for project development dependencies only; ADR 064 rejects `uv run commonplace-*`.

### 3. Runtime-native session environment handoff — fallback

A session hook writes environment changes into a runtime-owned channel applied to every later tool subprocess (Claude Code's `CLAUDE_ENV_FILE`).

- Role now: only for a runtime surface that does not see the user `PATH` even after a restart.
- Limitation: runtime-specific, and ADR 086's no-hooks constraint rules it out as a shipped mechanism until hooks are standardised. It could still be an operator-side workaround documented per runtime.

### 4. Runtime environment configuration — fallback

The runtime's own configuration sets subprocess environment, such as Codex `shell_environment_policy`.

- Role now: fallback for the same failure as option 3.
- Limitation: an explicit `PATH` value is machine-specific. ADR 086 already has `commonplace-init` write one machine-specific, uncommitted harness setting (the Claude Code read rule), so an init-written, gitignored runtime setting is a known pattern. It would still need per-runtime support for prepending to the inherited `PATH` rather than replacing it.

### 5. Persistent user `PATH` — operative

Add the command directory to the user environment so every newly started process sees it.

- Status: this is what `uv tool update-shell` does under ADR 064. The July objection (it selects one project's venv globally) no longer applies: the directory holds one user-level tool, and one version per user is accepted.
- Limitation: running processes do not see the change. On Windows a desktop application may need a full quit and restart, not a new window. Whether each surface actually rereads the user environment on restart is the open item for native Windows Codex.

### 6. Project-aware dispatcher shims — retired

Global shims that chose each project's venv from the working directory. ADR 064 rejects per-project launcher wrappers until an incompatible-project case requires simultaneous versions.

### 7. Explicit venv executable paths — retired

Instructions calling `.venv/bin/commonplace-validate`. There is no Commonplace venv to name, and the option broke the bare-command surface.

### 8. Per-tool environment prefix or command rewrite — fallback

A `PreToolUse` hook rewrites each shell call to prepend the command directory.

- Role now: last-resort fallback for a surface that ignores user `PATH`.
- Limitation: hook-based, so excluded by ADR 086's no-hooks constraint as a shipped mechanism; approval preservation, quoting and non-shell tools were never proven.

### 9. Portable package entry points absorb shell logic — active

Move load-bearing `find`/`xargs`/`sed`/pipeline behavior behind tested `commonplace-*` commands, so instructions call one stable entry point.

- Status: selected by [E1](../system-contract-consistency/plans/e1-windows-execution.md) for promoted skills. Planned items: `commonplace-validate all`, a package tag/path resolver replacing `cp-skill-connect`'s `rg -l | xargs -r rg` pipeline, and shared byte operations (checksum, verified copy and restore) for ingest, ground and snapshot-web. The per-skill dispositions are in the [E1 rebaseline](./e1-promoted-skill-rebaseline-2026-08-27.md).
- Open: the same treatment for non-promoted instructions, which E1 does not cover. [inventory.md](./inventory.md) lists them.
- Limitation: does not absorb ordinary navigation merely to avoid declaring `rg` as a prerequisite.

### 10. Paired channel-specific literal procedures — active, limited

Canonical instructions carry separate POSIX and PowerShell commands, clearly labelled and tested.

- Status: E1 restricts pairing to checks that must run before a package command can be trusted: the health-check preflight and snapshot-web's discovery of optional capture tools. Workflow semantics go to option 9 instead, so the two implementations of failure handling and byte preservation that full pairing would create never arise.

### 11. Channel-compiled instruction artifacts — open, likely narrow or reject

Resolve canonical instructions into a channel-specific literal form. The existing [proposal](../../reference/proposals/channel-compiled-instruction-artifacts.md) considers promoted skills, the whole instructions tree, and the control plane as boundaries.

ADR 086 changes where compilation could happen:

- **Build time** already has a hook: `hatch_build.py` prepares the library copy that ships in the wheel and rewrites links leaving it. But the wheel is platform-independent, so the build does not know the consumer's shell.
- **Install time** has no Commonplace hook; `uv tool install` runs none.
- **Init time** would mean writing channel-specific copies into each project, which ADR 086 rejected to keep one tree per machine and to stop copies diverging.
- **A per-channel second tree** inside the installed package (for example a PowerShell rendering beside the canonical one) would keep one install but add a second tree to review and keep in sync.

Given options 9 and 10 remove most channel-specific text, compilation now has little left to resolve. Provisional disposition for the proposal: narrow or reject, pending the inventory's count of shell constructs that remain after E1.

### 12. Standardized execution environment — retired for now

Declaring WSL, a dev container, or a POSIX image as the only supported substrate. E1 selected retaining native Windows support, because installation, `PATH` ownership and skill stubs already work there.

### 13. Runtime-bundled tool reliance — open

Treat a tool bundled by an agent runtime, potentially `rg`, as available without separate installation.

- Limitation: bundling may differ by runtime, surface, version, or sandbox and may be undocumented. The July Claude Code report found `find` supplied as a runtime shell function, which shows that a resolved name is not an executable with known behavior.

### 14. Commonplace-managed tool installation — open

Installation ensures third-party tools such as `rg` are present, as uv-tool extras or a managed tool directory.

- Limitation: uv does not naturally own native utilities such as `rg` and Git. Platform packaging, licences, updates and discovery become Commonplace's responsibility.

### 15. Capability-shaped instructions with deterministic dispatch — open, low priority

Instructions name required operations; a resolver maps each to a verified implementation. Option 9 covers the repeated operations found so far, so this is justified only if a large set of operations remains that no package command should own.

### 16. Directory-aware shell environment manager (direnv) — retired

Direnv put the project venv on `PATH` for tool shells. ADR 064 removed `.envrc` from init; the health check reports a leftover `.envrc` as residue and never deletes it. The July probe reports that exercised direnv remain valid evidence about the old model only.

## Library reachability (new with ADR 086)

ADR 086 adds a layer that did not exist in July: an agent must read library files outside the workspace. The ADR's mechanisms are:

- `.commonplace/library.md`, referenced from `AGENTS.md` and imported by `CLAUDE.md`, gives absolute paths;
- skill stubs redirect to the real `SKILL.md` by absolute path;
- init writes a Claude Code `Read(//<library root>/**)` rule; Codex is reported to need none.

The channel questions this raises:

- whether each runtime's sandbox lets the file-read tool, and separately a shell process such as `rg`, read the library root;
- whether native Windows paths in `library.md` and stubs (drive letters, backslashes, a custom `UV_TOOL_DIR`) are followed correctly by each harness;
- whether a stale pointer after switching between editable and normal install is detected before an agent reads from the old root. ADR 086 records this as a known silent failure, mitigated only by rerunning init.

ADR 086's evidence is Linux-only. Windows and macOS are outside it.

## Native Windows Codex application boundary

Current Codex documentation says the Windows app runs its agent natively with PowerShell by default, or in WSL after a switch and restart; its integrated terminal is configured separately from the agent environment; and local-environment setup scripts run when a worktree is created. None of that exports an environment into later tool calls.

Under ADR 064 the app does not need a project environment. It needs to see the user `PATH` that `uv tool update-shell` wrote, which requires the app process to be started after that change. The remaining desktop questions are:

- whether quitting and restarting the app (not only opening a new window or thread) picks up the new user `PATH`;
- whether its sandbox permits reading the library root outside the workspace;
- whether it treats a skill's `allowed-tools: Bash` as binding when the agent's shell is PowerShell (see the E1 rebaseline).

Options 3, 4 and 8 apply only if the restart check fails.

## Current composition and open decisions

The adopted composition is: user `PATH` via `uv tool update-shell` with a restart (option 5), bare-command verification in the health check and every command (option 1), library pointers written by init (ADR 086), portable package commands for load-bearing shell logic (option 9), and paired preflight only where diagnosis must precede the package (option 10).

Open decisions before the workshop can close:

- whether `rg` and Git are declared prerequisites (with verification), runtime-bundled conveniences, or something Commonplace installs (options 13 and 14);
- whether non-promoted instructions receive the option 9 treatment, and in what order;
- the disposition of the channel-compilation proposal (option 11);
- which fallback, if any, is documented for a surface that ignores the user `PATH` after a restart (options 3, 4, 8);
- how `allowed-tools: Bash` is handled on native Windows.

## Evidence needed before closure

- A native-Windows run of the v7 probe in the Codex desktop app after a full restart, recording command authority and library reachability.
- The same probe in at least one IDE-extension surface and one cloud surface.
- A worktree or second-project run showing that init outputs and the shared tool behave as expected there.
- The inventory's classification of non-promoted instructions, to size options 9 and 11.
- Documentation or observation of whether runtime-bundled `rg` is a contract on each surface.

## Documentation grounding for candidate mechanics

- [Codex configuration reference](https://developers.openai.com/codex/config-reference) — `shell_environment_policy` and related subprocess settings.
- [Codex Windows app](https://learn.chatgpt.com/docs/windows/windows-app) and [local environments](https://learn.chatgpt.com/docs/environments/local-environment) — native PowerShell versus WSL agent execution, the independent integrated terminal, worktree setup scripts.
- [uv tools](https://docs.astral.sh/uv/concepts/tools/) — tool environments, the tool executable directory, and `uv tool update-shell`.
