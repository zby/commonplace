---
description: "Proposal: make shipped skills ordinary instruction files, generate gitignored skill stubs in the source checkout as init does in projects, and split repo-only skills into harness tools and methodology instructions"
type: reference/types/design-proposal.md
tags: []
---

# Shipped skills as instructions, with generated stubs everywhere

Installed projects reach a skill through a generated stub that points at the real skill in the library ([ADR 086](../adr/086-projects-read-the-library-from-the-installed-package.md)). The source checkout does not: its harness skill directories are committed relative symlinks into `kb/instructions/<name>/`. Daily development therefore never exercises the route every installed project depends on. This proposal would close that gap and, in the same change, stop treating skills as a special file format. It is written as a candidate amendment to ADR 086.

The proposal has two genuine design decisions: how the checkout generates its stubs, and where the list of local-only skills lives, together with how repo harness tools reach both harnesses. The rest is mechanical relocation.

## Current state (as of 2026-09-27)

- **Shipped skills.** `MANIFEST.promoted_skills` (ten `cp-skill-*` names) plus `MANIFEST.router_skill` (`cp-skill-library`) in `src/commonplace/scaffold_manifest.py` define what a project receives. Each lives as `kb/instructions/<name>/SKILL.md`. Their frontmatter already carries `type: types/instruction.md` next to the harness fields (`name`, `description`, `user-invocable`, `allowed-tools`, `context: fork`, `model`, `argument-hint`). Two have bundled files: `cp-skill-write-multistage` (`agents/`, `references/`) and `cp-skill-snapshot-web` (`KNOWN-LIMITATIONS.md`).
- **Library code.** `library.skills()` (`src/commonplace/lib/library.py`) lists only manifest skills and raises when `<name>/SKILL.md` is missing. `library.render_stub()` copies the real file's frontmatter, adds a `$ARGUMENTS` pass-through when the real skill uses it, and tells the agent to resolve relative links against the real file. `render_routing()` writes each skill's `SKILL.md` path into the skill index in `.commonplace/library.md`.
- **Stale-stub warnings.** `warn_if_stale()` runs only in a directory tree that contains `.commonplace/`, which `commonplace-init` creates.
- **Source checkout.** `.claude/skills/` and `.agents/skills/` each hold 16 committed relative symlinks into `kb/instructions/`: the 11 shipped skills and five repo-only skills (`analyse-agentic-system`, `synthesize-agent-memory-landscape`, `scan-agentic-system-transfer`, `operator-brief`, `roughdraft-review`). A sixth repo-only folder, `kb/instructions/evaluate-scenarios/SKILL.md`, has harness frontmatter but no projection. `AGENTS.md` forbids running `commonplace-init` here and carries a Windows fallback paragraph for checkouts that cannot materialize symlinks.
- **Inbound links to repo-only skills** (counted at this date): `analyse-agentic-system` 40, `synthesize-agent-memory-landscape` 5, `scan-agentic-system-transfer` 3, `operator-brief` 1 (from `AGENTS.md`), `roughdraft-review` 0.
- **Code that special-cases skill folders.** `src/commonplace/lib/index_directory.py` (`_subdir_link_target`, which picks the sole `.md` in a `cp-skill-*` folder) and `src/commonplace/docs/properdocs_hooks.py` (`COLLECTION_MAX_DEPTH`, justified by single-`SKILL.md` subdirectories).
- **Init in the checkout.** Reading `_migrate_legacy_copies()` in `src/commonplace/cli/init_project.py`: it treats `kb/types/` as a legacy library copy, and in an editable install the library root is this repository's `kb/`, so each file there compares equal to itself. Unguarded, an init run here would remove the global types. Init also writes the routing file, the Claude Code read rule, template files, and a `.gitignore` block.

## Proposed shape

1. **Shipped skills become ordinary instruction files.** A single-file skill becomes a flat `kb/instructions/<name>.md`. A skill with bundled files stays a folder with an ordinarily named main file. The harness frontmatter stays on the file, because the [instruction type](../../types/instruction.md) already lets the runtime consumer govern additional frontmatter. The only `SKILL.md` files anywhere become generated stubs. The Agent Skills format expects a skill's directory name to match its `name`; stubs keep that shape, so the real file's name no longer has to.
2. **The checkout generates stubs the way init does.** Stubs in `.claude/skills/` and `.agents/skills/` are rendered by `library.render_stub()` and gitignored, replacing the committed symlinks. In the editable install the library root is this repository's `kb/`, so the stubs point into the working tree.
3. **`library.skills()` keeps listing manifest skills** and resolves each name to its instruction file instead of requiring `<name>/SKILL.md`. `render_stub()` and `render_routing()` take that file path.
4. **Repo-only skills split by role.**
   - *Harness tools with no KB role* (`roughdraft-review`, `operator-brief`) leave `kb/` and become plain repo harness skills: real `SKILL.md` folders under the harness directories, not KB artifacts. The one `AGENTS.md` link to `operator-brief` would point to its new location.
   - *Methodology skills* (`analyse-agentic-system`, `synthesize-agent-memory-landscape`, `scan-agentic-system-transfer`) stay in `kb/instructions/` as instructions, so they keep validation, link checking, and review gates. They receive stubs in the checkout from a second, local-only list that does not ship.
   - `evaluate-scenarios` has to be classified into one of these two groups, or have its harness frontmatter removed if nothing invokes it as a skill.

## Why

- **The checkout exercises the installed route.** `$ARGUMENTS` pass-through, frontmatter copying, relative-link resolution against the real file, and stale-stub warnings would run in daily development. Today only tests and installed projects exercise them. This applies the project's commitment to develop Commonplace by using it.
- **The Windows symlink caveat goes away.** The fallback paragraph in `AGENTS.md` ("Source checkout command installation") can be cut.
- **Skills stop being a special file format.** A shipped skill becomes an instruction that the manifest promotes. It is found by the same `description:` search as any other instruction. This matches ADR 086's harness-neutral base, where Agent Skills are an optional layer over files that an agent reads by path.

## Decision (i): how the checkout generates stubs

| Option | Gains | Costs |
|---|---|---|
| **Run `commonplace-init` here**, after guarding the migration against a library root inside the project | One code path for projects and the checkout. `.commonplace/` exists, so stale-stub warnings fire. The skill index in `library.md` is also exercised. | Lifts the `AGENTS.md` prohibition. Init writes files the checkout may not want (routing file, read rule, templates, a `.gitignore` block), and the migration guard is new code whose only purpose is this case. |
| **A stubs-only mode or command** (for example a flag on init, or a separate command) | Writes only the stubs and their `.gitignore` entries. No migration risk. | A second entry point. Stale-stub warnings do not fire unless the mode also creates `.commonplace/` or the warning check learns another trigger. The skill index goes unexercised. |

Operativity: under either option, the Claude Code and Codex skill discovery consumes the stubs as it does in projects, and the command's `.gitignore` handling keeps them out of commits. For the first option, `warn_if_stale()` consumes `.commonplace/` unchanged. For the second option, the warning path has no consumer in the checkout until one is built.

## Decision (ii): the local-only list and harness tools

**Where the local-only stub list lives.** It must not be the shipping manifest, because that manifest defines what projects receive. Candidates: a repo-local config file read by the generator, or a second field in a repo-only module. Nothing is proposed beyond "outside `scaffold_manifest.py`". Whichever generator is chosen in decision (i) is the consumer that would read it.

**How harness-tool skills reach both harnesses.** Claude Code reads `.claude/skills/` and Codex reads `.agents/skills/`. Whether current Claude Code also reads `.agents/skills/` is unverified; if it does, one copy would serve both and this choice disappears. Otherwise:

| Option | Cost |
|---|---|
| Two copies, one per harness directory | They can drift. |
| One real directory plus a directory symlink | Brings back the Windows symlink problem this proposal removes. |
| Stubs from the local-only list | Requires a real file to point at, which puts the tools back into `kb/` as KB artifacts. |

Operator leaning: two copies. The files are small and rarely change, so drift is the cheapest of the three costs. This is a leaning, not a decision.

## Costs

- A fresh clone needs one generation command before skills work.
- Adding a skill or changing a description needs a rerun. Commands already warn on stale stubs where `.commonplace/` exists (see decision (i)).
- Each skill use costs one extra read in the checkout, as it already does in projects.
- **One-time relocation.**
  - Roughly 110 library files outside `kb/reports/` and `kb/work/` mention `SKILL.md` (270 including them), counted at the current-state date. Some mentions are about stubs or harness mechanics and would stay.
  - Tests that assume skill folders include `tests/commonplace/cli/test_init_project.py`, `tests/commonplace/lib/test_index_directory.py`, `tests/commonplace/docs/test_type_contract_integrity.py`, `test_agentic_system_instruction_composition.py`, and `tests/scenarios/*`.
  - The special cases in `index_directory.py` and `properdocs_hooks.py` change or go.
  - `commonplace-relocate-note` rewrites inbound links. Relative links inside a skill body change depth when a folder becomes a flat file, for example `../../types/` in `cp-skill-write`; those need separate edits.
  - The `AGENTS.md` sections "Skills" and "Source checkout command installation", and ADR 086's wording about the real `SKILL.md`, change to match.

## Adoption criteria

- Decision (i) is taken. If init is chosen, a test shows init in a checkout-shaped project with an in-project library root removes nothing from the library.
- Decision (ii) is taken, including whether Claude Code reads `.agents/skills/`, checked against the current harness.
- Each repo-only skill, including `evaluate-scenarios`, is assigned to the harness-tool or methodology group.
- A trial in the checkout confirms that one shipped skill with bundled files (`cp-skill-write-multistage`) and one flat skill run through generated stubs in both harnesses, with `$ARGUMENTS` and relative links resolving correctly.
