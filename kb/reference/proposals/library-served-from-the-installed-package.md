---
description: "Proposal: stop copying the Commonplace library and global types into installed projects; agents and commands read them from the installed package, and a project holds only its own content, collection-local types, and skill copies"
type: ../types/design-proposal.md
tags: [kb-maintenance]
---

# Library served from the installed package

`commonplace-init` copies the whole framework library into every project: `kb/commonplace/{notes,reference,instructions}/` and the global types under `kb/types/`. The commands, however, already come from one user-level uv tool ([ADR 064](../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)). The copy exists only so that agent reads stay inside the project directory, where harnesses allow them without prompts. This proposal removes the copy. A project would hold its own content, its collection-local types, and copies of the promoted skills. Everything framework-owned would be read from the installed package.

**Warning for anyone who copies projects.** Today a copied Commonplace project carries the library and global types with it. Under this proposal it would not. A copy would carry the project's content, its local types, its skill copies, and the project's recorded Commonplace version. Everything else works only on a machine where that version of the tool is installed and set up. Anyone whose workflow starts from a copied project should expect it to stop working without that install step once this ships.

## Current state (as of 2026-09-23)

- `commonplace.scaffold_manifest` copies the source trees `kb/notes`, `kb/reference`, and `kb/instructions` to `kb/commonplace/<collection>/`, and `kb/types` to `kb/types`. [ADR 021](../adr/021-ship-library-content-under-kb-commonplace.md) chose that layout to separate the library from user content. It did not argue that the library has to sit inside the project.
- ADR 021 also specified a `.commonplace` version marker and a drift check. `init_project.py` writes neither, so a project today records no Commonplace version.
- Code hardcodes project paths into the copy: review gates (`review/paths.py`), the critique instruction (`review/critique.py`), and library types (`lib/type_resolver.py`).
- Code also depends on exact global type paths. `kb/types/type-spec.md` is the root contract. Validation rules are keyed to `type-spec`, `tag-readme`, and `agentic-system-analysis-result`. Index generation expects `generated-index` and `tag-readme`.
- 13 collection-local schemas build on a global schema through `$ref`: 10 on `note.schema.yaml` and 3 on `note-base.schema.yaml`. `note.schema.yaml` differs from `note-base` only by forbidding `status:`.
- The promoted skills name library artifacts they expect to read. Instructions: `re-ingest`, `ingest-paper-with-code`, `draft-ingest-report`, `run-review-batches`, and `assess-a-claim-bearing-artifact-against-external-literature`. Reference: `commands`, `control-plane-goals`, and `link-vocabulary`. Global type specs: `note`, `instruction`, and `type-spec`. Those artifacts link further into the library.
- Claude Code reads files outside the project without prompts only for directories listed in `permissions.additionalDirectories`. That setting is allowed in user-level `~/.claude/settings.json`. It also covers Grep, Glob, and read-only Bash search. Edits there still follow the permission mode. A symlink does not bypass the setting: permission checks look at the link target as well. Codex's sandbox already allows reads outside the project.
- Directory symlinks and junctions are unreliable on Windows. The design must not depend on them.

## Proposed shape

**Package, read-only.** This holds the library collections, the global types and their schemas, the review gates, and the critique instruction. Commands read them as package data. Agents read them under a library root that a command prints, such as `commonplace-library`, parallel to `commonplace-source`.

**Project, owned.** This holds the project's collections, its collection-local types, and copies of the promoted skills. It also records the Commonplace version the project was set up with, which the proposed replacement for ADR 021's unimplemented marker would carry.

**What crosses the boundary:**

- `type:` pointers to global types. The existing `kb/types/...` form becomes a reserved prefix that the resolver maps to the library root.
- The `note-base` rule. The validator applies it to every typed artifact. A local schema describes only its own fields and never uses `$ref` outside its own `types/` directory. Global schemas keep their `$ref`s to each other, because they all live in the package.
- Agent read access. The install or setup step writes the library root, computed by the command, into the user's harness settings.

**Project types are collection-local only.** A project never adds a global type. If two of its collections want the same type, each keeps its own copy. This [rests on](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) the claim that directory-scoped types are cheaper than global types.

## Option space

### How agents learn the library root

- **A. A command, frontloaded.** Committed files say "the library root is the output of `commonplace-library`". Where the harness supports session-start hooks, a committed hook runs the command and puts the root into context. That [spares execution context](../../notes/frontloading-spares-execution-context.md) the lookup. The hook calls only a command, so it behaves the same on every OS. Operativity: the agent consumes the root through the control-plane file and the hook. A harness without hooks costs one command call per session.
- **B. A gitignored per-machine file.** Init writes the absolute root into a local-only file the harness loads, such as `CLAUDE.local.md`. This needs no extra call, but it depends on each harness having a local-file convention. Codex's equivalent is unconfirmed. The file also goes stale when the tool moves.
- **Rejected: a symlink or junction at `kb/commonplace`.** It would keep every existing path valid, but Windows support is unreliable, and it still needs the permission setting.

**Candidate: A**, with B allowed as a per-harness optimization.

### How skills reach the instructions they use

Skills stay copied, because harnesses discover them only in project or user skill directories. The instructions they name would not be copied. Options:

- **A. Resolve through the library root.** Skill text names library artifacts relative to the library root. This adds no new prerequisite: 7 of the 10 promoted skills already call `commonplace-*` commands, so the tool must be installed anyway. `cp-skill-connect`, `cp-skill-convert`, and `cp-skill-revise-autoreason` call none. Without the tool, those three would lose library reads they currently get from the copy.
- **B. Bundle dependencies into the skill directory.** At init, each skill carries copies of the library artifacts it names. This keeps skills self-contained, but the dependency closure is transitive: instructions link to other instructions and notes. It also recreates a partial library copy per skill, with its own drift.
- **C. Move skill-only instructions into the skill in the source repo.** An instruction used by just one skill moves into that skill's `references/`, as `cp-skill-write-multistage` already does. Shared instructions such as `re-ingest`, used by both `cp-skill-ground` and `cp-skill-ingest`, still need A or B.

**Candidate: A, with C where an instruction has exactly one consuming skill.** Every skill that reads the library must check that the root resolves. If it does not, the skill stops with the install instruction instead of improvising without the library.

### What a copied project can do

With the tool absent, a copied project still works as a plain-Markdown KB. Reading and searching the project's notes, and following links between them, work anywhere. Validation, review, typed authoring, and library-dependent skills need the tool at the recorded version. Options for making that visible:

- The control-plane template states the requirement and the recorded version at the top.
- The health check and the library-reading skills report a missing or mismatched tool with the exact install command.
- Validation reports an unresolvable `kb/types/` pointer as "Commonplace library not available", not as a broken type.

These are complementary. **Candidate: all three.** They are the in-system form of the warning above.

### Links from project notes into the library

Relative links into `kb/commonplace/` stop resolving. Options: link to the library's published web pages; or add a library link scheme that the validator resolves through the package. ADR 021 found project-to-library links rare. **Candidate: published web pages**, with no new link scheme until links in that direction turn out to be common.

## Forces

- **Version floating.** Today each project's copy is pinned and upgrades arrive as a reviewable diff. Served from the package, the library changes silently on `uv tool upgrade`. In return, library/code skew disappears: the library always matches the commands that read it. The recorded project version limits the risk by making a mismatch detectable, though not by preventing it.
- **Portability of a project repository.** A clone or copy is no longer self-sufficient for framework work. This is the cost behind the warning above.
- **Reproducibility.** Two machines with different tool versions read different libraries for the same project. The recorded version makes that visible. It does not make it impossible.
- **Source repo divergence.** Here, `kb/types/` and the library collections are authored files. In a project they are names that resolve into the package. This is the same kind of divergence ADR 021 already accepted for `kb/notes/` becoming `kb/commonplace/notes/`.
- **Harness coupling.** Read permission depends on a per-harness setting. Claude Code's is documented and user-level. Codex needs none. Other runtimes must be checked one at a time.
- **Loss of `status:` ban.** Making `note-base` implicit drops `note.schema.yaml`'s `status:` ban from local types that don't restate it.

## Non-goals

- Changing where the Commonplace source repo authors its library or types.
- Removing the skill copies; harness discovery still requires them.
- Supporting project-owned global types.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy. The upgrade path is to re-run setup and delete the copy. Detecting that is in scope; preserving the layout is not.

## Open choices

- Whether the recorded project version is a floor, an exact pin, or advisory. It could also be a range the tool checks.
- Whether the harness-settings write belongs to `commonplace-init`, a separate setup command, or a printed instruction the operator applies.
- Whether `kb/types/` stays the reserved prefix for global types, or global types get an explicit package form. The reserved prefix leaves existing artifacts unchanged. An explicit form makes the package origin visible to an agent opening the pointer.
- Whether the implicit `note-base` rule ships first, as a separate change, since it is useful in the source repo on its own.

## Adoption criteria

Adopt when all of the following hold:

- The library-root command and read permission are demonstrated end to end without prompts in Claude Code and Codex, on Linux, macOS, and Windows.
- Every promoted skill resolves its library reads through the root, or bundles them under option C, and fails clearly when the root is absent.
- Commands no longer read library content, gates, or global types from project paths.
- Operators who distribute projects by copying have been told what a copy will and will not carry.

---

Relevant Notes:

- [ADR 021 — Ship library content under kb/commonplace](../adr/021-ship-library-content-under-kb-commonplace.md) — see-also: the layout this proposal would partly supersede
- [ADR 064 — Install Commonplace commands as a user-level uv tool](../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — see-also: the runtime placement this proposal extends to the library
- [ADR 027 — Package scaffold assets without source-tree symlinks](../adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — see-also: the package-data boundary the library would be served from
- [Architecture](../architecture.md) — part-of: the installed topology this would change
- [Collections and types](../collections-and-types.md) — see-also: the type-resolution contract the reserved prefix would extend
