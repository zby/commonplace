# Execution-channel compatibility workshop

## Goal

Catalogue the system differences that can make a Commonplace instruction executable in one environment and non-operative in another, then compare the available solution families without assuming that instruction compilation is the answer.

The forcing case is intentionally small: after installation has placed Commonplace commands in the user-level uv-tool bin directory, a fresh session should be able to invoke `commonplace-validate --help` by bare command name, exactly as later agent tool calls will. A native Windows desktop application may not inherit a shell's updated `PATH`, and a source checkout's editable installation selects one active Commonplace command version per OS user. This exposes a larger issue than environment activation: executable instructions depend on an execution channel composed from operating system, shell, agent runtime, process/environment semantics, working directory, sandbox, installed tools, and launch-time environment inheritance.

The workshop widens the existing [channel-compiled instruction artifacts proposal](../../reference/proposals/channel-compiled-instruction-artifacts.md). That proposal already distinguishes compiling promoted skills, the whole instructions tree, and the control plane. Here compilation remains one candidate in a broader catalogue. The unit under investigation is not just the promoted skill: it is every instruction-bearing artifact that invokes Commonplace's Python entry points or another external tool.

## First consideration: implementable evidence gathering

The first stage is a landscape survey of every environment in which Commonplace can be read or operated, not a test limited to supported source checkouts. Its procedure must be executable from source checkouts, initialized full projects, reader/vendor installs, package-only environments, worktrees, and restricted or remote agent surfaces. It may not require a path, executable, shell feature, repository, writable destination, or second environment until the agent has established that prerequisite.

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
- generated `.claude/skills/` and `.agents/skills/` copies as consumption surfaces, while their canonical sources remain the inventory authority;
- scripts or reference procedures that an instruction directly tells an agent to execute;
- source-checkout and installed-KB layouts, including worktrees.

Historical examples that no active instruction routes to are out of the first inventory. They enter only if a live consumer makes them executable guidance.

### Execution systems

- Commonplace source checkouts, initialized full projects, reader/vendor installs, package-only installations, and unrecognized layouts;
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

1. **Project Python surface** — `commonplace-*`, `pytest`, Python, uv, and venv discovery.
2. **Repository/navigation surface** — especially `rg`, plus Git and filesystem/text utilities such as `find`, `sed`, `xargs`, `wc`, and `sort`.
3. **Workflow-specific surface** — curl, Roughdraft, runner CLIs, and any optional tool an instruction treats as required or provides a fallback for.

For each tool, distinguish presence, bare-name resolution, behavioral compatibility, sandbox access, and whether failure is loud. Finding an executable on `PATH` does not establish that its flags or semantics match another system's tool of the same name.

## Working invariant

Installation owns installing the package as a user-level uv tool and making its bin directory discoverable to later processes. Source checkouts use the editable form of that same user-level installation; project development dependencies remain separate. Session start does not repair installation. It runs the same bare command expected later—initially `commonplace-validate --help`—and reports a channel-specific remediation if that fails.

This invariant is provisional only in the sense that the exact probe may change. The separation of responsibilities is fixed for the workshop: installation establishes tools; session start verifies the effective execution channel.

## Questions

1. What capability facts actually determine an execution channel? Do OS, shell, path layout, environment inheritance, and tool inventory co-vary enough to form named profiles, or must they remain independent axes?
2. Which agent surfaces launch every tool call in a fresh process, which preserve environment, and which offer a runtime-native environment handoff?
3. How can a native Windows desktop application inherit the uv-tool bin directory after `uv tool update-shell`, and how should a long-lived process report that it needs a restart?
4. Which instructions depend only on bare `commonplace-*` resolution, and which also depend on Bash syntax or external Unix utilities?
5. Which external tools are true prerequisites, runtime-bundled conveniences, optional accelerators, or replaceable implementation details?
6. If instructions are compiled, what is the compilation boundary: promoted skills, all executable instructions, their directly invoked references, or the control plane too?
7. What checks a compiled or otherwise derived instruction against its canonical source, and which form receives semantic review?
8. Which differences should Commonplace absorb behind portable Python entry points, and which should remain explicit operator/runtime requirements?

## Required work products

- [inventory.md](./inventory.md) — repeatable inventory method, initial counts, execution surfaces, tool-dependency schema, and known gaps.
- [solution-catalogue.md](./solution-catalogue.md) — candidate mechanisms and their trade-offs; no preferred architecture until worked cases eliminate options.
- [probe-procedure.md](./probe-procedure.md) — typed instruction for capability-gated evidence gathering from any current Commonplace environment, with native-Windows Codex as the forcing case rather than the assumed layout.
- [E1 promoted-skill rebaseline](./e1-promoted-skill-rebaseline-2026-08-27.md) — manifest-derived static inventory and disposition of every promoted skill selected on 2026-08-27; it records no native-Windows runtime result.
- [evidence/](./evidence/README.md) — append-only probe reports from different agents, runtimes, operating systems, shells, and launch paths.
- A dated capability matrix for each observed environment class: install/layout mode, execution interface, command lookup, process persistence, session hooks, environment handoff, worktree behavior, bundled tools, and sandbox constraints.
- An instruction-to-tool dependency map covering all canonical instructions, not only promoted skills.
- Independently collected reports spanning source, initialized-project, reader/vendor, CLI, IDE/application, native Windows, POSIX, WSL, and restricted/remote environments where those environments are available to an investigator.
- Worked probes, only where their prerequisites are observed, for at least:
  - bare `commonplace-validate --help` after installation;
  - bare `rg --version` and one representative search;
  - a Bash-shaped compound instruction using a pipeline or `xargs` on a channel where that exact instruction and shell are available;
  - native Windows Codex desktop execution;
  - a second project or worktree proving that any solution remains project-scoped.
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

- creating or reinstalling the user-level tool or a project environment at session start;
- globally activating one project's venv for all applications;
- translating shell languages mechanically before cataloguing the actual semantic dependencies;
- treating tool presence as proof of compatible behavior;
- editing production instructions while the option space is still being catalogued;
- expanding declared platform support without an explicit later decision;
- requiring a probe agent to be in this source checkout, create a fixture, relaunch its runtime, or prepare a second environment.

Probe runs are evidence collection, not production edits. Agents may add a report under this workshop's `evidence/` directory, but must not change PATH, activate a venv, install a tool, or repair configuration during the run.

## Closure

The workshop closes when:

1. a repeatable sweep accounts for every executable locus in the scoped instruction graph;
2. every external tool has an ownership and verification classification;
3. the capability matrix contains independently gathered, explicitly partial evidence from the materially distinct Commonplace environments available for investigation, including native-Windows Codex, without treating source-checkout access as universal;
4. the solution catalogue has been tested against the worked cases rather than ranked from intuition;
5. the chosen mechanism or composition covers all instructions that use Python tools and the required non-Python tools such as `rg`;
6. derived-artifact, review-target, source-checkout, installed-KB, and worktree consequences are explicit; and
7. durable decisions and procedures have been promoted and the workshop navigation entry can be removed.

## Grounding

- [Channel-compiled instruction artifacts](../../reference/proposals/channel-compiled-instruction-artifacts.md) — existing option space for compiling skills, the instructions tree, the control plane, or a later-bound form.
- [Windows portability for promoted skills](../self-improvement-cluster-operationalization/windows-portability-for-promoted-skills.md) — prior audit finding and narrower portability proposal.
- [Instruction generation](../../reference/instruction-generation.md) — current install-time generation and canonical/generated boundaries.
- [Generate KB skills at build time, don't parameterise them](../../notes/generate-instructions-at-build-time.md) — rationale for compilation when install-time-known variation would otherwise remain in runtime instructions.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — timing test for install-time versus session-time resolution.
- [Tool availability is package-owned and Git is never invoked](../../reference/adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md) — adjacent precedent for deciding which dependencies belong behind package code.
