---
description: "Proposal: stop copying the framework library and global types into projects, because the copy confuses users and diverges from the installed package; agents and commands read the package in place, and skills remain the one managed copy"
type: ../types/design-proposal.md
tags: [kb-maintenance]
---

# Library served from the installed package

In this proposal, *the library* means everything Commonplace owns and a project only reads: the library collections (notes, reference, instructions), the global types and their schemas, the review gates, the critique instruction, and the templates.

## Problem

`commonplace-init` copies the library into every project: `kb/commonplace/{notes,reference,instructions}/` and the global types under `kb/types/`. This copy causes two problems.

**Confusion.** The copy sits next to the project's own collections, under the same `kb/` directory and in the same git history. Users cannot tell which files are theirs and which belong to the framework. Several hundred framework files appear in their file tree, their searches, and their `git status`.

**Divergence.** The same content exists in two places: the installed package and each project's copy. The two drift apart. `commonplace-init` never overwrites an existing file, so after the first init the copy stays at that version. When the tool is upgraded, the commands run new code against an old copy of the gates and types. Each project holds its own version, and an agent or user can edit the copy without anything noticing.

A fix that only hides the copy solves the first problem and not the second. This proposal removes the copy. The skills are the one exception: harnesses discover skills only in skill directories, so skills stay copied, and they are managed as copies whose drift is checked.

## Current state (as of 2026-09-23)

- `commonplace.scaffold_manifest` copies the source trees `kb/notes`, `kb/reference`, and `kb/instructions` to `kb/commonplace/<collection>/`, and `kb/types` to `kb/types`. It also scaffolds the project's own `kb/notes/` collection, so a project has `kb/notes/` (its own) next to `kb/commonplace/notes/` (the library). [ADR 021](../adr/021-ship-library-content-under-kb-commonplace.md) chose this layout to separate the library from user content, and it kept the library inside the project.
- `init_project.py` copies a file only when the target does not exist. An existing file that differs is reported, not replaced. There is no update path for the copy.
- ADR 021 specified a `.commonplace` version marker and a drift check. `init_project.py` writes neither, so a project records no Commonplace version.
- The commands come from one user-level uv tool, with one active version per OS user ([ADR 064](../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)).
- The wheel build (`[tool.hatch.build.targets.wheel.force-include]` in `pyproject.toml`) copies the library trees as they are, with no processing. 132 library files contain `../sources/` links. `kb/sources/` does not ship, so those links dangle in every installed copy.
- Code hardcodes the copy's project paths: review gates (`review/paths.py`), the critique instruction (`review/critique.py`), and library types (`lib/type_resolver.py`).
- Review baselines identify criteria by repository-relative paths. `freshness/versioning.py` requires snapshot inputs to resolve inside the repository.
- Code depends on exact global type paths. `kb/types/type-spec.md` is the root contract. Validation rules are keyed to `type-spec`, `tag-readme`, and `agentic-system-analysis-result`. Index generation expects `generated-index` and `tag-readme`.
- 13 collection-local schemas build on a global schema through `$ref`: 10 on `note.schema.yaml` and 3 on `note-base.schema.yaml`. `note.schema.yaml` differs from `note-base` only by forbidding `status:`.
- The promoted skills name library artifacts they read: the instructions `re-ingest`, `ingest-paper-with-code`, `draft-ingest-report`, `run-review-batches`, and `assess-a-claim-bearing-artifact-against-external-literature`; the reference artifacts `commands`, `control-plane-goals`, and `link-vocabulary`; and the global type specs `note`, `instruction`, and `type-spec`. Those artifacts link further into the library. `cp-skill-ground` and `cp-skill-ingest` word some references twice: "in a source checkout use X; in an installed project use Y".
- Claude Code reads files outside the project without prompts only for directories listed in `permissions.additionalDirectories`. User-level settings allow it, and it also covers Grep, Glob, and read-only Bash search. A symlink does not bypass it. Codex's sandbox already allows reads outside the project.
- Directory symlinks and junctions are unreliable on Windows.
- Harness plugins can carry skills together with other files. Claude Code copies marketplace plugins into a per-version cache under `~/.claude/plugins/cache`. Since v2.1.229 a marketplace entry can instead name a command that prints a plugin directory; in link mode Claude Code uses that directory in place and re-runs the command once per session. Link mode does not work on Windows. A plugin cannot declare components outside its own directory. Codex copies plugins, including local ones, into its own cache. OpenCode accepts absolute skill paths in its configuration. Codex and Gemini CLI follow symlinked skill folders.

## What the fix must provide

1. Library files are not in the user's collections, searches, or `git status`.
2. The installed package holds the only copy of the library on a machine.
3. Commands and agents read the library from the package.
4. Skills, the one unavoidable copy, find the library files they name, and a skill that differs from the installed package is detected.
5. When the library is unavailable, commands and skills say so plainly.

## Option space

### Where the library lives

**A. Read in place from the installed package.** No project holds a copy. Commands read the library as package data. Agents read it under a library root that a command such as `commonplace-library` prints. In the source repo the command prints the repository's `kb/`, so the same relative paths work in both places. This satisfies requirements 1–3, and the library always matches the code that reads it.

It costs three pieces of machinery that exist only because the library is outside the project directory:

- *Root discovery.* Where the harness supports session-start hooks, a hook runs the library-root command and puts the root into context. That [spares execution context](../../notes/frontloading-spares-execution-context.md) the lookup. A harness without hooks costs one command call per session.
- *Read permission.* Setup adds the library root to the user's harness read settings. The root moves when the uv tool directory moves, for example after a Python upgrade, so the library-root command also checks that the setting still covers it.
- *Review identity.* A package criterion gets a logical identifier relative to the library root, such as `commonplace:instructions/review-gates/prose/source-residue.md`. It contains neither a version nor an absolute path. Project criteria keep repository-relative paths. One resolver picks the root from the identifier and never falls back between package and project. Freshness still compares criterion text: an upgrade with identical text stays fresh, and edited text yields `criterion-changed`. Switching over retires the baselines whose criteria gain package identities, once; historical results stay under their original identities.

*Operativity:* commands consume package paths and review identities in code. Agents consume the root through the hook or the control-plane file, and through skill text. Setup writes the permission setting and the skills.

**B. Hidden, gitignored copy inside the project.** Setup writes the library into a directory such as `.commonplace/library/`, out of `git status` and out of default searches. This needs none of A's machinery: paths are relative, reads are inside the project, and review criteria keep repository-relative paths. But it keeps the second copy, so it does not solve divergence. A variant makes the copy a cache: every command compares a recorded version with the installed tool and regenerates the copy when they differ. That narrows divergence to the window between an upgrade and the next command, and it silently discards edits to the copy. **Fallback if A's read permission proves unworkable in a required harness.**

**C. One plugin-shaped tree, delivered through harness plugins.** The package ships the skills and the library as one directory tree shaped as a harness plugin. Skills reach library files by paths relative to their own location, so no path is rewritten and no library root is looked up inside a skill. Each harness receives the tree through its own plugin mechanism:

- *Claude Code:* a marketplace entry names a Commonplace command that prints the tree's location inside the installed package. In link mode the tree is used in place, so it always has the tool's version. On Windows, where link mode does not work, the ordinary plugin install copies the whole tree into Claude Code's cache.
- *Codex:* the plugin install copies the whole tree into Codex's cache. A copy of the whole tree stays consistent with itself; it can only fall behind the tool as a unit.
- *Harnesses without plugins:* user-level links to, or copies of, the skill directories inside the tree.

Drift checking becomes one comparison per harness: the version of the tree the harness loaded against the installed tool's version. Commands still read the library as package data and still need option A's review identities. Agents outside a skill still need the library's location, which a hook calling a Commonplace command can supply.

This option makes the harness plugin, not the project, the delivery unit for everything agents read. Several comparable systems ship their skills and methodology libraries this way. Unverified: whether link mode re-runs the command after `uv tool upgrade` moves the package; whether agents read files inside a plugin directory without permission prompts; whether skill-relative links resolve the same way in the source checkout, where skills are symlinked from `kb/instructions/`; and how a plugin update channel stays in step with `uv tool upgrade` where the plugin is copied.

A and C are alternatives for the agent-facing side. Neither is selected yet.

**Rejected: a symlink or junction at `kb/commonplace`.** It keeps the library in view, and symlinks and junctions are unreliable on Windows.

### Where skill copies live

Skills are the one place where this proposal cannot follow ordinary software installation. Installed software stays where it was installed, because its lookup path, such as `PATH`, is a list the user can extend. Harnesses look for loose skills only in a fixed set of directories, and the package's location cannot be added to that set. Configurable skill paths have been requested for Claude Code and Codex and closed. Plugins (option C) and OpenCode's skill-path setting are the exceptions. Links into the package would avoid a copy, as `uv tool` does for executables, but they are unreliable on Windows and would need a second install mode. So outside option C, skills are copied. This is a workaround for a missing harness feature, and harnesses will probably add extensible skill search paths eventually. The skill-copy machinery should therefore stay small and easy to delete: no reconciliation workflow, no records that outlive it. Keeping skills small also helps in the meantime. A skill that carries its procedure and reads frequently changing detail from library files does less harm when its copy is stale.

- **User-level skill directories (candidate).** Setup installs the promoted skills once per machine, into each harness's user-level skill directory. This matches ADR 064: the tool has one active version per OS user, so the skills need only one copy per user too. Projects then contain no framework copies at all. A project's own skills stay project-level. Two things are unverified: whether every required harness discovers user-level skills, and how project-level skills shadow user-level ones of the same name in the source checkout, which has its own skill symlinks.
- **Per-project skill directories.** This is today's placement. There is one copy per project, each of which can drift separately, and projects must decide whether to commit them.

### How skills name library files

- **Compile paths at setup (candidate with user-level skills).** Setup rewrites each library reference in a skill to the file's absolute path under the library root. The agent reads the path as written, with no lookup. The installed skills are specific to one machine, which costs nothing when they live at user level and are not committed. A plain prefix swap is ambiguous, because a project has its own `kb/notes/` and `kb/notes/x.md` could mean either file. So the source text must mark library references explicitly. Setup fails if a marked reference names a file the package does not ship.
- **Name files relative to the root.** Skill text names `<library root>/instructions/re-ingest.md`, and the agent takes the root from context. The skill text is the same on every machine, which suits per-project copies that may be committed. Each skill must say how to get the root when no hook supplied it.
- **Move single-use instructions into the skill.** An instruction used by just one skill moves into that skill's `references/`, as `cp-skill-write-multistage` already does. This works alongside either option above.

Either naming option removes the two-branch wording in `cp-skill-ground` and `cp-skill-ingest`.

### Keeping skill copies in step with the package

The skills stay a copy, so the divergence problem applies to them. **Candidate: detect drift in code, overwrite on setup.** The library-root command and the health check compare each installed promoted skill with what setup would produce now: the current package's skill rendered with the current library root. Both inputs can be recomputed, so no installation record is needed. A mismatch covers a changed skill, a missing or extra file, and a moved library root. The command then stops with the setup instruction. Promoted skills are framework-owned, so setup overwrites them; a local edit to one is not preserved. This cannot stop a harness from loading a stale skill before any command runs, so setup after an upgrade stays necessary.

### Global type pointers

Global types leave `kb/types/`, so their pointers change, and a local schema's `$ref` to a global schema stops resolving.

- **Bare names (candidate).** A global type is named by its bare name, such as `type: note`. A collection-local type keeps its path form (`./`, `../`, or `kb/…`, ending in `.md`). The form alone tells the resolver which kind it has, with no fallback between them. A bare name `X` resolves to `types/X.md` under the library root, which is `kb/types/X.md` in the source repo, so both places write the same pointer. This partly reverses [ADR 018](../adr/018-types-are-path-references-to-instruction-docs.md). ADR 018 objected to names because a name was looked up first in the collection's `types/` and then in `kb/types/`, so one name could mean different files. That guessing does not return: a bare name only ever means a global type. Global types are a small, closed set that the package owns (9 today). Framework validation rules would be keyed by bare name instead of canonical path ([ADR 048](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). The migration rewrites about 800 `type:` lines mechanically. A lookup command such as `commonplace-type` is an optional convenience that reports what a pointer resolves to.
- **A reserved `kb/types/` prefix.** It would look like a path but name no file in a project, so an agent that opened it would find nothing.

**Schema references.** The validator applies the `note-base` rule to every typed artifact, and a local schema never uses `$ref` outside its own `types/` directory. This drops `note.schema.yaml`'s `status:` ban from local types that do not restate it.

### Making an unavailable library visible

- The control-plane template states that the project needs the tool and names the accepted versions.
- The health check and the skills that read the library report a missing tool, a stale skill, or an uncovered library root with the exact command that fixes it.
- Validation reports a bare type name it cannot resolve because the library is missing as "Commonplace library not available", not as a broken type.

**Candidate: all three.**

### Links from project notes into the library

Relative links into `kb/commonplace/` stop resolving. ADR 021 found project-to-library links rare. **Candidate: link to the library's published web pages**, with no new link scheme until such links turn out to be common.

## Separable changes

These are useful in any layout. They can ship before, after, or without the relocation.

- **A prepared reader copy at build time.** The package build stages the library, replaces links to local ingests with their canonical external source URLs, regenerates navigation, and fails on any unresolved local link. Authored source files, with their grounding under [ADR 073](../adr/073-untracked-source-snapshots-require-ingest-grounding.md), stay unchanged. This fixes today's 132 dangling `../sources/` links.
- **A recorded version range.** The project records the Commonplace versions it accepts as a PEP 440 specifier, compared with the installed `llm-commonplace` version. This fills ADR 021's missing marker.
- **The implicit `note-base` rule.** It is useful in the source repo on its own.

## Forces

- **One copy against local control.** Reading the package in place removes divergence between the library and the code. The price is that the library changes on `uv tool upgrade`, with no diff for the user to review. The recorded version range makes an unwanted upgrade detectable.
- **Harness coupling.** Option A depends on each harness allowing reads outside the project. Claude Code's setting is documented and user-level, and Codex needs none. Other runtimes must be checked one at a time. Option B avoids this at the cost of keeping a copy.
- **Visibility against discoverability.** The library no longer appears in searches of the project. Agents must search the library root explicitly.
- **Portability.** A copied or cloned project carries no library. It still works as a plain-Markdown KB, but framework work needs the tool installed and set up on each machine.
- **Migration cost.** Existing projects re-run setup and delete `kb/commonplace/` and the global types. Review baselines for moved criteria are retired and rebuilt once. Bare type names add a mechanical rewrite of about 800 lines in the source repo.

## Non-goals

- Changing where the source repo authors its library or types.
- Distributing grounding evidence for the library's claims, or relaxing grounding requirements for source authoring or project-owned content.
- Removing the skill copies; harness discovery still requires them.
- Supporting project-owned global types. A project that wants one type in two collections keeps a copy in each, which [rests on](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) the claim that directory-scoped types are cheaper than global types.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy. Setup detects it and tells the operator to delete it; preserving the layout is out of scope.

## Open choices

- Whether every required harness discovers user-level skills, and how the source checkout avoids duplicate project-level and user-level skills.
- Where the project keeps its version range. A `[tool.commonplace]` table in `pyproject.toml` suits Python projects, but a non-Python project would need that file for one field.
- Whether a version mismatch or a stale skill stops commands or only warns.
- Whether the harness-settings write belongs to `commonplace-init`, a separate setup command, or a printed instruction the operator applies.

## Adoption criteria

Adopt option A or C when all of the following hold for the chosen option:

- A set-up project contains no library files and no global types, and commands read the library, gates, and global types only from the package.
- Agents read the library without permission prompts in Claude Code and Codex, on Linux, macOS, and Windows. Under A this means the library-root command and read permission, with a moved library root detected. Under C it means each harness's plugin delivery, with a tree whose version differs from the installed tool detected.
- Every promoted skill finds the library files it names, in the source repo and in installed projects, with no text that branches between them. A skill that no longer matches the installed package is detected and refreshed by setup.
- Review checks show stable package identities across installation moves, unchanged freshness for identical criterion text, `criterion-changed` for edited text, and a clear failure for an unavailable criterion. Package and project criteria cannot shadow each other.
- A transition rehearsal keeps review history, retires only the affected baselines, and builds new ones through completed reviews.
- Every global `type:` pointer uses its bare name, and the validator rejects path-form pointers to global types.
- Operators who distribute projects by copying have been told what a copy carries.

Fall back to option B if a required harness cannot grant reads outside the project.

Revisit the skill copies when the required harnesses can discover skills from a configurable location. At that point skills can be read in place from the package like the rest of the library, and the copy and its drift check can be deleted.

---

Relevant Notes:

- [ADR 021 — Ship library content under kb/commonplace](../adr/021-ship-library-content-under-kb-commonplace.md) — see-also: the layout this proposal would supersede
- [ADR 064 — Install Commonplace commands as a user-level uv tool](../adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — see-also: the user-level placement this proposal extends to the library and skills
- [ADR 027 — Package scaffold assets without source-tree symlinks](../adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — see-also: the package-data boundary the library would be served from
- [Architecture](../architecture.md) — part-of: the installed topology this would change
- [Collections and types](../collections-and-types.md) — see-also: the type-resolution contract that bare global names would change
- [ADR 018 — Types are path references to instruction docs](../adr/018-types-are-path-references-to-instruction-docs.md) — see-also: the path-valued type decision bare names would partly reverse
- [ADR 048 — Imperative type rules dispatch by canonical path](../adr/048-imperative-type-rules-dispatch-by-canonical-path.md) — see-also: the rule-keying bare names would change
