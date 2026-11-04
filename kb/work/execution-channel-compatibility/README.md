# Execution-channel compatibility workshop

## Goal

Catalogue the system differences that can make a Commonplace instruction executable in one environment and non-operative in another, then compare the available solution families without assuming that instruction compilation is the answer.

The forcing case is intentionally small: after installation has established the user-level tool and, on Windows, its supported signed-Python shims, a fresh session should be able to invoke `commonplace-validate --help` by bare command name, exactly as later agent tool calls will. A native Windows desktop application may not see the updated `PATH` until it is fully restarted, and a source checkout's editable installation selects one active Commonplace command version per OS user. Since ADR 086 the agent must also read library files (instructions, types, skills) at the installed package's root, outside the workspace. Executable instructions therefore depend on an execution channel composed from operating system, shell, agent runtime, process/environment semantics, working directory, sandbox, installed tools, launch-time environment inheritance, and read access outside the workspace.

The workshop widens the existing [channel-compiled instruction artifacts proposal](../../reference/proposals/channel-compiled-instruction-artifacts.md). That proposal already distinguishes compiling promoted skills, the whole instructions tree, and the control plane. Here compilation remains one candidate in a broader catalogue. The unit under investigation is not just the promoted skill: it is every instruction-bearing artifact that invokes Commonplace's Python entry points or another external tool.

## Current state — 2026-11-03

The operator requested a current-state update before further work. The
[source rebaseline](./rebaseline-2026-11-03.md) now selects **11 promoted skills
plus one router**, **25 package commands**, and all three canonical instruction
trees. This update ran no runtime probe and changed no production behavior.
The August audit and September census remain historical, not current counts.

**What is settled:** Windows installed delivery and supported package CI have
bounded acceptance. Linux pi's user-level worker copy and synthetic live-session
upgrades also passed. The delivery workshop is closed; INSTALL.md owns its
remaining release/platform/runtime triggers. Procedure portability remains here.

**What still needs work:** validate's aggregate shell loop, connect's guarded
pipeline, health-check layout/presence tests, snapshot capture and byte handling,
AutoReason's filesystem preparation, required-reference coverage, and the
runtime interpretation of tool metadata. Ingest already names native byte-copy
alternatives; health Step 6 is plain argv, not a POSIX program. Do not carry the
old blanket classifications forward.

**Newly identified conflicts:** the old E1 plan to add `validate all` conflicts
with the current CLI's explicit, tested rejection of broad literal scopes. The
v7 breadth probe also lacks the supported Windows-shim authority rule. Resolve
those before implementation or a new comparable Windows survey. A retired
analysis command remains in a non-promoted instruction; the rebaseline names it
for a separate consumer-aware repair.

**Next:** revise the breadth probe with a new procedure ID, then choose one
bounded E1 slice and its runtime fixtures. No production changes or expanded
support claims are authorized by this status update.

## Previous closure review (2026-11-01; historical)

Keep open. PyPI 0.3.3 and supported Windows/Linux CI supersede the older
release and CI summaries below. Native installed-project command and skill
routing evidence now exists in the
[retained delivery acceptance record](../../reports/retained/framework-delivery-acceptance-2026-11-03.md).
The delivery workshop closed on 2026-11-03; its deferred acceptance triggers
now belong to INSTALL.md. E1's portability work below remains open.
The independent Codex report, `kb/work/windows-install/results-2026-11-01-codex-independent.md` (closed workshop; `git show 600306e1d:kb/work/windows-install/results-2026-11-01-codex-independent.md`),
could run uv and rg in its sandbox; the prior sandbox failure is specific to
that earlier run, not a universal Windows restriction.

E1 still owns portable validation-all, connect's empty-tag handling, health
preflights, byte-preserving operations and the static shell-idiom check.
The broader inventory, v7 capability survey and non-Python tool dispositions
also remain unfinished. Successful installation does not satisfy these closure
conditions. Rebaseline from the current manifest before the next E1 batch.

## Historical rebaselines (2026-09-25 through 2026-10-27)

The dated statements below describe their checkpoints. Current status and
counts are above; do not treat old absence claims as current blockers.

The workshop opened on 2026-07-28 under the project-venv command model (ADR 014). Two later decisions changed the ground:

- [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) installs commands once per OS user as a uv tool. Project-venv discovery, activation and direnv stopped being part of the problem.
- [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) serves the library from the installed package; projects get gitignored pointers (`.commonplace/library.md`, skill stubs, a Claude Code read rule) instead of copies.

The rebaseline brought the working documents in line: the [solution catalogue](./solution-catalogue.md) marks each option operative, active, open, fallback or retired; the [probe procedure](./probe-procedure.md) is v7 and checks command authority and library reachability instead of venv and direnv state; the [inventory](./inventory.md) has fresh counts and a first classification of non-promoted instructions. The three July [evidence reports](./evidence/README.md) stay as observations of the old model.

**Division of work with E1.** The [E1 plan](./e1-windows-execution.md), moved into this workshop when the system-contract consistency workshop closed, owns making the promoted skills work on native Windows: the package commands and paired preflights named in the [E1 rebaseline](./e1-promoted-skill-rebaseline-2026-08-27.md), and one native-Windows run after they land. This workshop keeps what E1 does not cover: non-promoted instructions and the control plane, per-surface command visibility and library reachability, the classification of non-Python tools, and the disposition of the channel-compilation proposal.

**Blocking gap at the September checkpoint.** No native-Windows evidence had
then been retained. Later Windows reports supersede that absence claim; a
current breadth-protocol run is still distinct from delivery acceptance.

**Recheck 2026-10-24.** Nothing here changed after 2026-09-30 except mechanical path rewrites. Against the repository on 2026-10-24:

- The [evidence directory](./evidence/README.md) still holds only the three July reports from the retired project-venv model. No run of probe v7 exists on any surface, Windows or otherwise.
- E1 items remain open: `commonplace-validate` has no `all` target; `cp-skill-health-check` pairs PowerShell forms only in Step 4 (uv tool) and Step 5 (legacy residue), while Steps 1, 2 and 6 are Bash-only; 13 promoted skills still declare `allowed-tools: Bash` with no recorded disposition; no Windows CI exists.
- The library's theory collection moved from `kb/notes/` to `kb/theory/` (ADR 123) while project scaffolds keep `kb/notes/`. The [inventory](./inventory.md) still names `kb/notes/` for library files; its counts predate the move and the 2026-10 command changes (`commonplace-analysis`, `commonplace-task` added; `commonplace-agentic-analysis-*` removed) and need a re-count before the dependency map is trusted.
- Everything released is still v0.2.0 (2026-09-25); the probe must run against a release that carries the current init, which the framework-delivery workshop then owned (now closed; the current
  baseline and limits are in the retained delivery acceptance record above).

**Recheck 2026-10-27.** The first native-Windows report exists: [2026-10-27-codex-app-windows-powershell-a1.md](./evidence/2026-10-27-codex-app-windows-powershell-a1.md), taken from the Codex desktop app's PowerShell tool calls. It observed bare `commonplace-validate` and `rg` resolving, the former from the user-level uv tool bin, so the app inherits the user `PATH` after a restart, and no shell state surviving between tool calls. It ran procedure v6 on a checkout from 2026-08-08, so its layout section describes the retired project-venv model, and a v7 run is still open. The Windows command-delivery work done alongside it, shims over a signed or a uv-managed interpreter under Smart App Control and antivirus, belonged to windows-install, closed on 2026-11-03 (`git show 600306e1d:kb/work/windows-install/README.md`): its round 1 plan, the run of that plan on a second machine, and the round 2 plan are in that directory's history, and the harness run superseded five shorter reports that were retired from this directory the same day.

## First consideration: implementable evidence gathering

The first stage is a landscape survey of every environment in which Commonplace can be read or operated, not a test limited to supported source checkouts. Its procedure must be executable from source checkouts, initialized projects, reader/vendor installs, package-only environments, worktrees, and restricted or remote agent surfaces. It may not require a path, executable, shell feature, repository, writable destination, or second environment until the agent has established that prerequisite.

An unestablished prerequisite produces `not run` plus the reason. It does not license improvising a platform-specific substitute, repairing the environment, or calling the environment broken. This constraint outranks completeness of any single report: comparable partial evidence is more useful than a nominally complete procedure that some target agents cannot execute.

## Survey rounds

Evidence gathering is deliberately iterative:

1. **Round 1 — landscape breadth.** Run the typed probe unchanged in as many materially different environments as are available. Establish layout, bare command resolution, tool-call process semantics, broad tool discovery, and only the small behavior checks whose fixtures already exist.
2. **Round 2 — targeted depth.** Revisit selected environment classes after Round 1 identifies consequential unknowns. Add a behavioral check only when its prerequisite and the exact Commonplace instruction that depends on it are known.
3. **Later rounds — candidate verification.** Repeat against prepared launch paths, projects, worktrees, and proposed mechanisms to test isolation, inheritance, update, and failure behavior.

Each run creates a new report and identifies its round, procedure revision/date, and prior related report. Never overwrite the broad baseline with a deeper run. A later round may narrow its question, but it inherits the same implementability rule.

## Scope

### Instruction surfaces

- `AGENTS.md`, `AGENTS.md.template`, and the executable parts of `INSTALL.md`;
- every canonical artifact under `kb/instructions/`, including non-promoted instructions and references bundled with skills;
- the skill stubs and `.commonplace/library.md` that `commonplace-init` writes in projects (ADR 086), as the route by which agents reach canonical text; in this source checkout `.claude/skills/` and `.agents/skills/` are symlinks to `kb/instructions/`, and canonical sources remain the inventory authority;
- scripts or reference procedures that an instruction directly tells an agent to execute;
- source-checkout and initialized-project layouts, including worktrees; the library that a project reads lives in the installed package, not in the project.

Historical examples that no active instruction routes to are out of the first inventory. They enter only if a live consumer makes them executable guidance.

### Execution systems

- Commonplace source checkouts, initialized projects, projects still holding a pre-ADR-086 library copy, reader/vendor installs, package-only installations, and unrecognized layouts;
- Linux and macOS POSIX shells;
- native Windows PowerShell;
- Windows `cmd.exe` and direct-process tool interfaces where no persistent shell is exposed;
- WSL;
- Codex CLI, IDE, and desktop-app execution;
- Claude Code local and cloud execution;
- fresh sessions, resumed sessions, compaction, subprocess tool calls, and worktree setup;
- sandboxed and unsandboxed command execution where the difference changes availability.

### Tool dependencies

The inventory begins with three classes and stays open to discoveries:

1. **Commonplace and Python surface** — `commonplace-*` from the user-level uv tool, uv itself, Python launchers, and `pytest`/`ruff` as development dependencies run through `uv run`.
2. **Repository/navigation surface** — especially `rg`, plus Git and filesystem/text utilities such as `find`, `sed`, `xargs`, `wc`, and `sort`.
3. **Workflow-specific surface** — curl, Roughdraft, runner CLIs, and any optional tool an instruction treats as required or provides a fallback for.

For each tool, distinguish presence, bare-name resolution, behavioral compatibility, sandbox access, and whether failure is loud. Finding an executable on `PATH` does not establish that its flags or semantics match another system's tool of the same name.

## Working invariant

Installation owns installing the package as a user-level uv tool and making its bin directory discoverable to later processes (ADR 064). Source checkouts use the editable form of that same user-level installation; project development dependencies remain separate. `commonplace-init` owns the per-project pointers into the library (ADR 086). Session start does not repair either. Verification runs the same bare command expected later—initially `commonplace-validate --help`—and reports a channel-specific remediation if that fails; every command also warns about stale init outputs.

This invariant is provisional only in the sense that the exact probe may change. The separation of responsibilities is fixed for the workshop: installation establishes tools, init establishes pointers, and verification checks the effective execution channel.

## Questions

1. What capability facts actually determine an execution channel? Do OS, shell, path layout, environment inheritance, and tool inventory co-vary enough to form named profiles, or must they remain independent axes?
2. Which agent surfaces launch every tool call in a fresh process, which preserve environment, and which offer a runtime-native environment handoff?
3. Does a native Windows desktop application see the uv-tool bin directory after `uv tool update-shell` and a full restart, and how should a long-lived process report that it needs one?
4. Which instructions depend only on bare `commonplace-*` resolution, and which also depend on Bash syntax or external Unix utilities?
5. Which external tools are true prerequisites, runtime-bundled conveniences, optional accelerators, or replaceable implementation details?
6. If instructions are compiled, what is the compilation boundary: promoted skills, all executable instructions, their directly invoked references, or the control plane too?
7. What checks a compiled or otherwise derived instruction against its canonical source, and which form receives semantic review?
8. Which differences should Commonplace absorb behind portable Python entry points, and which should remain explicit operator/runtime requirements?
9. Can each runtime and its sandbox read the library root outside the workspace, by file-read tool and by shell process, including native Windows paths?

## Required work products

- [Current rebaseline](./rebaseline-2026-11-03.md) — November source census, all 12 skill dispositions, retained-evidence limits and next decision boundary.
- [inventory.md](./inventory.md) — inventory method, historical counts, current-scope pointer, tool-dependency schema and unfinished graph coverage.
- [solution-catalogue.md](./solution-catalogue.md) — candidate mechanisms and their trade-offs; no preferred architecture until worked cases eliminate options.
- [probe-procedure.md](./probe-procedure.md) — typed instruction for capability-gated evidence gathering from any current Commonplace environment, with native-Windows Codex as the forcing case rather than the assumed layout. Frozen revision v7 (2026-09-25); revise its authority comparison before the next current Windows run.
- [E1 Windows execution plan](./e1-windows-execution.md) — current promoted-procedure plan, separating completed delivery from open portability work and the unresolved aggregate-validation contract.
- [E1 promoted-skill rebaseline](./e1-promoted-skill-rebaseline-2026-08-27.md) — manifest-derived static inventory and disposition of every promoted skill selected on 2026-08-27; it records no native-Windows runtime result.
- [evidence/](./evidence/README.md) — append-only probe reports from different agents, runtimes, operating systems, shells, and launch paths.
- A dated capability matrix for each observed environment class: install/layout mode, execution interface, command lookup and authority, library reachability, process persistence, restart requirement, worktree behavior, bundled tools, and sandbox constraints.
- An instruction-to-tool dependency map covering all canonical instructions, not only promoted skills.
- Independently collected reports spanning source, initialized-project, reader/vendor, CLI, IDE/application, native Windows, POSIX, WSL, and restricted/remote environments where those environments are available to an investigator.
- Worked probes, only where their prerequisites are observed, for at least:
  - bare `commonplace-validate --help` after installation, in a process started after `uv tool update-shell`;
  - reading a library file from an initialized project, through `.commonplace/library.md` and through a skill stub;
  - bare `rg --version` and one representative search;
  - a Bash-shaped compound instruction using a pipeline or `xargs` on a channel where that exact instruction and shell are available;
  - native Windows Codex desktop execution;
  - a second project or worktree showing that init outputs and the shared user-level tool behave as expected there.
- A disposition for the existing channel-compilation proposal: adopt, narrow, combine with another mechanism, or reject.

## Method

1. **Establish probe implementability.** For each requested observation, state its shell, tool, fixture, layout, permission, and launch prerequisites. Remove or gate any check whose prerequisites are not established in the target environment.
2. **Run the breadth round.** Apply the unchanged baseline probe across materially different environments and preserve one report per run.
3. **Inventory canonical sources.** Record executable commands, shell constructs, path assumptions, required tools, fallbacks, and consumers. Generated skill copies are checked for drift but not counted twice.
4. **Repeat selectively for depth.** Documentation and the inventory identify exact unknowns; later capability-gated probes establish actual command lookup, environment inheritance, and tool behavior. Record partial observations with date and version rather than forcing every report through a source-checkout test suite.
5. **Classify dependencies.** Mark each tool required, optional, bundled-but-not-guaranteed, or replaceable. Record who installs it and how session start verifies it.
6. **Evaluate solution families against worked cases.** A mechanism that makes `commonplace-*` resolve but leaves `rg` or Bash-only pipelines broken has not solved the instruction surface.
7. **Select the smallest combination.** Compilation, environment propagation, shims, and portable commands may address different layers. Do not demand one universal mechanism if the evidence supports a composition.
8. **Promote durable results.** Architecture decisions go to ADRs/reference; transferable mechanisms go to notes; operative procedures and checks go to instructions/code. Delete the workshop after promotion.

## Non-goals

- creating or reinstalling the user-level tool, or rerunning init, at session start;
- reintroducing per-project Commonplace command versions (rejected by ADR 064);
- translating shell languages mechanically before cataloguing the actual semantic dependencies;
- treating tool presence as proof of compatible behavior;
- editing production instructions from this workshop; E1 owns the promoted-skill changes;
- expanding declared platform support without an explicit later decision;
- requiring a probe agent to be in this source checkout, create a fixture, relaunch its runtime, or prepare a second environment.

Probe runs are evidence collection, not production edits. Agents may add a report under this workshop's `evidence/` directory, but must not change PATH, install a tool, rerun init, or repair configuration during the run.

## Closure

The workshop closes when:

1. a repeatable sweep accounts for every executable locus in the scoped instruction graph;
2. every external tool has an ownership and verification classification;
3. the capability matrix contains independently gathered, explicitly partial evidence from the materially distinct Commonplace environments available for investigation, including native-Windows Codex, without treating source-checkout access as universal;
4. the solution catalogue has been tested against the worked cases rather than ranked from intuition;
5. the chosen mechanism or composition covers all instructions that use Python tools and the required non-Python tools such as `rg`;
6. derived-artifact, review-target, source-checkout, initialized-project, library-reachability, and worktree consequences are explicit; and
7. durable decisions and procedures have been promoted and the workshop navigation entry can be removed.

## Grounding

- [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — commands as a user-level uv tool; restart requirement; one version per user.
- [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) — library served from the installed package; init-written pointers; no hooks. The retained delivery record supplies later bounded Windows and Linux evidence.
- [E1 plan](./e1-windows-execution.md) — owner of promoted-skill native-Windows work.
- [Channel-compiled instruction artifacts](../../reference/proposals/channel-compiled-instruction-artifacts.md) — existing option space for compiling skills, the instructions tree, the control plane, or a later-bound form.
- [Windows portability for promoted skills](../self-improvement-cluster-operationalization/windows-portability-for-promoted-skills.md) — prior audit finding and narrower portability proposal.
- [Instruction generation](../../reference/instruction-generation.md) — current install-time generation and canonical/generated boundaries.
- [Generate KB skills at build time, don't parameterise them](../../theory/generate-instructions-at-build-time.md) — rationale for compilation when install-time-known variation would otherwise remain in runtime instructions.
- [Frontloading spares execution context](../../theory/frontloading-spares-execution-context.md) — timing test for install-time versus session-time resolution.
- [Tool availability is package-owned and Git is never invoked](../../reference/adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md) — adjacent precedent for deciding which dependencies belong behind package code.
