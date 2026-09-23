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
- The wheel build (`[tool.hatch.build.targets.wheel.force-include]` in `pyproject.toml`) copies the library trees as they are, with no processing. 132 library files contain `../sources/` links. `kb/sources/` does not ship, so those links dangle in every installed copy. ADR 021's linking principle made the external source the primary citation. Nothing enforces it at build time.
- Code hardcodes project paths into the copy: review gates (`review/paths.py`), the critique instruction (`review/critique.py`), and library types (`lib/type_resolver.py`).
- Code also depends on exact global type paths. `kb/types/type-spec.md` is the root contract. Validation rules are keyed to `type-spec`, `tag-readme`, and `agentic-system-analysis-result`. Index generation expects `generated-index` and `tag-readme`.
- 13 collection-local schemas build on a global schema through `$ref`: 10 on `note.schema.yaml` and 3 on `note-base.schema.yaml`. `note.schema.yaml` differs from `note-base` only by forbidding `status:`.
- The promoted skills name library artifacts they expect to read. Instructions: `re-ingest`, `ingest-paper-with-code`, `draft-ingest-report`, `run-review-batches`, and `assess-a-claim-bearing-artifact-against-external-literature`. Reference: `commands`, `control-plane-goals`, and `link-vocabulary`. Global type specs: `note`, `instruction`, and `type-spec`. Those artifacts link further into the library.
- Claude Code reads files outside the project without prompts only for directories listed in `permissions.additionalDirectories`. That setting is allowed in user-level `~/.claude/settings.json`. It also covers Grep, Glob, and read-only Bash search. Edits there still follow the permission mode. A symlink does not bypass the setting: permission checks look at the link target as well. Codex's sandbox already allows reads outside the project.
- Directory symlinks and junctions are unreliable on Windows. The design must not depend on them.

## Proposed shape

**Package, read-only.** This holds the library collections, the global types and their schemas, the review gates, and the critique instruction. Commands read them as package data. Agents read them under a library root that a command prints, such as `commonplace-library`, parallel to `commonplace-source`.

**Project, owned.** This holds the project's collections, its collection-local types, and copies of the promoted skills. It also records which Commonplace versions it accepts. This record replaces ADR 021's unimplemented marker (see **Versioning** below).

**What crosses the boundary:**

- `type:` pointers to global types. A global type is named by its bare name, such as `type: note`. A collection-local type keeps its path form (`./`, `../`, or `kb/…`, ending in `.md`). The form alone tells the resolver which kind it has, with no fallback between them. A bare name `X` resolves to `types/X.md` under the library root. In the source repo it resolves to `kb/types/X.md`, so the source repo and installed projects write the same pointer. `type-spec` names itself: `type: type-spec`. (Details under **Global types by bare name** below.)
- The `note-base` rule. The validator applies it to every typed artifact. A local schema describes only its own fields and never uses `$ref` outside its own `types/` directory. Global schemas keep their `$ref`s to each other, because they all live in the package.
- Agent read access. The install or setup step writes the library root, computed by the command, into the user's harness settings.

**Versioning.** The library has no version of its own. It is package data, so its version is the `version` of `llm-commonplace` in `pyproject.toml`. A project records the versions it accepts as a PEP 440 specifier, such as `>=0.2,<0.3`. Commands compare the specifier with the installed package's version using standard Python packaging tools. This reuses existing tooling instead of defining a marker format.

**Release steps.** Once projects read the library straight from the package, the wheel build is the only point where the library can be prepared for readers who lack the source repo. Before building, the release process:

1. Regenerates the library's indexes, so committed navigation matches the content that ships.
2. Checks that no shipped artifact links into a directory that does not ship, `kb/sources/` especially. Under ADR 021's linking principle the external source is the link target. A remaining link to a local ingest fails the build; it is not rewritten silently.
3. Ships only the library collections, global types, gates, and templates. The wheel's include list already excludes `kb/work/`, `kb/reports/` state, and `kb/sources/` content. A check that the list still holds keeps it that way.

These steps run as one command or build hook, not as a checklist, so a release cannot skip them.

**Global types by bare name.** The alternative was to keep `kb/types/...` as a reserved prefix. That prefix would look like a path but name no file in an installed project, so an agent that opened it would find nothing. A bare name says plainly that the type must be looked up. This partly reverses [ADR 018](../adr/018-types-are-path-references-to-instruction-docs.md), which replaced type names with paths. ADR 018's main problem with names was guessing: a name was looked up in the collection's `types/` first and then in `kb/types/`, so one name could mean different files. That guessing does not return here. A bare name only ever means a global type, and a local type is only ever named by its path. Global types form a small, closed set that the package owns (9 today), because projects never add one. ADR 018 kept paths so an agent could open the type file directly. Local types keep that. Global types lose it, but under this proposal they are no longer project files anyway.

Framework validation rules would be keyed by bare name instead of by canonical path ([ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). The mapping from installed `kb/commonplace/...` paths back to source `kb/...` paths goes away. A local type with the same name as a global one still gets none of the framework's rules, because a local type is only ever named by its path. Migration rewrites about 800 `type:` lines in the source repo mechanically; most of them are `note` (519) and `instruction` (130).

A prefixed form such as `commonplace:note` was considered. It would make the origin visible and leave room for other libraries. It is not adopted because Commonplace is the only library a project reads. A prefix can be added if a second library appears.

**Type lookup command.** A command such as `commonplace-type` takes a `type:` value (bare name or path) or an artifact path. It reports the resolved type spec, its schema, and whether the type is global or collection-local. An option prints the spec itself. Operators use it to check what a type means without knowing where the library is installed. Agents can use it as a shortcut: one call replaces finding the library root and building the path. This is a lookup, not the authoring interface ADR 018 rejected. The type spec stays an ordinary file the agent reads and follows, and nothing requires the command before writing. It uses the same resolver as the validator, so what it reports matches what validation checks.

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
- Validation reports a bare type name it cannot resolve because the library is missing as "Commonplace library not available", not as a broken type.

These are complementary. **Candidate: all three.** They are the in-system form of the warning above.

### Links from project notes into the library

Relative links into `kb/commonplace/` stop resolving. Options: link to the library's published web pages; or add a library link scheme that the validator resolves through the package. ADR 021 found project-to-library links rare. **Candidate: published web pages**, with no new link scheme until links in that direction turn out to be common.

## Forces

- **Version floating.** Today each project's copy is pinned and upgrades arrive as a reviewable diff. Served from the package, the library changes silently on `uv tool upgrade`. In return, library/code skew disappears: the library always matches the commands that read it. The recorded project version limits the risk by making a mismatch detectable, though not by preventing it.
- **Portability of a project repository.** A clone or copy is no longer self-sufficient for framework work. This is the cost behind the warning above.
- **Reproducibility.** Two machines with different tool versions read different libraries for the same project. The recorded version makes that visible. It does not make it impossible.
- **Source repo divergence.** Here, the library collections are authored files. In a project they are read through the library root. This is the same kind of divergence ADR 021 already accepted for `kb/notes/` becoming `kb/commonplace/notes/`. Type pointers do not diverge: bare names read the same in both places.
- **Harness coupling.** Read permission depends on a per-harness setting. Claude Code's is documented and user-level. Codex needs none. Other runtimes must be checked one at a time.
- **Loss of `status:` ban.** Making `note-base` implicit drops `note.schema.yaml`'s `status:` ban from local types that don't restate it.

## Non-goals

- Changing where the Commonplace source repo authors its library or types.
- Removing the skill copies; harness discovery still requires them.
- Supporting project-owned global types.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy. The upgrade path is to re-run setup and delete the copy. Detecting that is in scope; preserving the layout is not.

## Open choices

- Where the project keeps its version specifier. One candidate is a `[tool.commonplace]` table in a `pyproject.toml`. That suits Python projects, but a non-Python project would need a `pyproject.toml` just to hold this one field.
- Whether a version mismatch stops commands or only warns.
- Whether the release steps run as a hatch build hook or as a separate command run before `uv build`.
- Whether the harness-settings write belongs to `commonplace-init`, a separate setup command, or a printed instruction the operator applies.
- Whether the implicit `note-base` rule ships first, as a separate change, since it is useful in the source repo on its own.

## Adoption criteria

Adopt when all of the following hold:

- The library-root command and read permission are demonstrated end to end without prompts in Claude Code and Codex, on Linux, macOS, and Windows.
- Every promoted skill resolves its library reads through the root, or bundles them under option C, and fails clearly when the root is absent.
- Commands no longer read library content, gates, or global types from project paths.
- Every global `type:` pointer uses its bare name. The validator rejects path-form pointers to global types, and the type lookup command resolves both forms.
- Operators who distribute projects by copying have been told what a copy will and will not carry.

---

Relevant Notes:

- [ADR 021 — Ship library content under kb/commonplace](../adr/021-ship-library-content-under-kb-commonplace.md) — see-also: the layout this proposal would partly supersede
- [ADR 064 — Install Commonplace commands as a user-level uv tool](../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — see-also: the runtime placement this proposal extends to the library
- [ADR 027 — Package scaffold assets without source-tree symlinks](../adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — see-also: the package-data boundary the library would be served from
- [Architecture](../architecture.md) — part-of: the installed topology this would change
- [Collections and types](../collections-and-types.md) — see-also: the type-resolution contract that bare global names would change
- [ADR 018 — Types are path references to instruction docs](../adr/018-types-are-path-references-to-instruction-docs.md) — see-also: the path-valued type decision this proposal would partly reverse for global types
- [ADR 048 — Imperative type rules dispatch by canonical path](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md) — see-also: the rule-keying this proposal would move to bare names
