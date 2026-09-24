# Framework delivery

## Commission

Posed by the operator on 2026-09-23. Evaluate how Commonplace should deliver what agents read — the framework library, global types, review gates, and skills — to installed projects, and select the options that the [library-served-from-the-installed-package proposal](../../reference/proposals/library-served-from-the-installed-package.md) should adopt.

Operator direction, same date: GBrain is Commonplace's dominant competitor, and its methods are the default design to copy. Depart from a GBrain method only where evidence shows a Commonplace-specific reason, and record that reason.

## Problem

Today `commonplace-init` copies the library and the skills into every project. The copy causes two problems:

- **Confusion.** Users cannot tell framework files from their own.
- **Divergence.** The copy is never refreshed after the first init, so after an upgrade the commands run new code against old gates and types. Each project sits at its own version.

Skills complicate any fix. Most harnesses discover loose skills only in fixed directories, so something must appear there. Harness plugins are the main exception.

## Options under evaluation

The proposal records the options in full. In short:

- **Where the library lives:** A — read in place from the installed package, with a command that prints its location; B — a hidden, gitignored copy in the project; C — one plugin-shaped tree holding skills and library, delivered by each harness's plugin mechanism.
- **How skills reach harnesses:** plugins; user-level copies; per-project copies; links to one canonical tree (claude-obsidian); stubs that fetch the current skill text from the installed tool at use time (GBrain).
- **How copies are kept in step:** comparing with a fresh rendering; install-time hashes with a three-way comparison (GBrain); ownership markers that refuse to overwrite unmarked files (hyalo, OKF Harness).

## Evaluation boundary

- Harnesses: Claude Code and Codex are required. Others are recorded where the evidence is cheap.
- Operating systems: Linux, macOS, and Windows.
- Both places the skills must work: the source checkout and an installed project.
- Upgrade cases: a `uv tool upgrade` that changes a skill, one that changes only library files, and one that moves the install location.

## Open probes

- Does Claude Code's link-mode plugin re-run its path command after `uv tool upgrade` moves the package?
- Can agents read files inside a plugin directory without permission prompts, in Claude Code and in Codex?
- Do skill-relative links resolve the same way in the source checkout, where `.claude/skills/` holds symlinks into `kb/instructions/`?
- How does a copied plugin (Codex, Claude Code on Windows) stay at the uv tool's version?
- Which GBrain methods carry over to a Python package, and which depend on GBrain's own runtime or MCP server?

## Coupling

- [agent-operability-second-slice](../agent-operability-second-slice/README.md) builds install baselines and a three-way upgrade plan for copied framework files. If this workshop removes the library copy, that work's scope shrinks to whatever copies remain, such as skills. Coordinate before either side ships.
- [system-contract-consistency](../system-contract-consistency/README.md) holds findings I1 (shipping and upgrade contracts disagree) and I2 (the install projection breaks library links). Both change meaning if the library stops being copied.

## Closure

Close when the selected options are written back into the proposal, the open probes are answered or explicitly deferred with a trigger, and each departure from GBrain's methods has a recorded reason. Then delete this directory and its entry in `kb/work/README.md`.

## Working files

- [comparable-systems-survey.md](./comparable-systems-survey.md) — how harnesses and 14 comparable systems deliver skills and libraries, from web research and the local clones
- [gbrain-delivery-methods.md](./gbrain-delivery-methods.md) — code-grounded study of GBrain v0.54.1.0's delivery methods and what carries over to a Python/uv package
