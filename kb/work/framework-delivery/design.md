# Design: library served from the installed package

This is the workshop's only design document. It replaced the proposal `kb/reference/proposals/library-served-from-the-installed-package.md` on 2026-09-24, so the design is kept in one place while it changes. The probe results it cites are in [results-codex.md](./results-codex.md), [results-claude-code.md](./results-claude-code.md), and [probe-results.md](./probe-results.md).

In this design, *the library* means everything Commonplace owns and a project only reads: the library collections (notes, reference, instructions), the global types and their schemas, the review gates, the critique instruction, the templates, and the promoted skills.

## Problem

`commonplace-init` copies the library into every project: `kb/commonplace/{notes,reference,instructions}/`, the global types under `kb/types/`, and the skills under `.agents/skills/` and `.claude/skills/`. The copy causes two problems.

**Confusion.** The copy sits next to the project's own collections, under the same `kb/` directory and in the same git history. Users cannot tell which files are theirs and which belong to the framework. Several hundred framework files appear in their file tree, their searches, and their `git status`.

**Divergence.** `commonplace-init` never overwrites an existing file, so after the first init the copy stays at that version. When the tool is upgraded, the commands run new code against an old copy of the gates, types, and skills. Each project holds its own version, and an agent or user can edit the copy without anything noticing.

Hiding the copy would solve the first problem but not the second. This design removes the copy.

## Constraints

The operator's constraints are recorded in the [workshop README](./README.md#operator-direction-and-constraints): copy GBrain by default, one tree and one channel (uv), no hooks, and a harness-neutral base. They bind every choice below.

## What the fix must provide

1. Library files are not in the user's collections, searches, or `git status`.
2. The installed package holds the only copy of the library on a machine. Harnesses discover skills only in their own skill directories, so `commonplace-init` writes a stub there for each skill that redirects to the real skill in the package. The stubs are written the same way on every platform.
3. Commands and agents read the library from the package.
4. Skills find the library files they name, and a stub that no longer matches the installed package is detected.
5. When the library is unavailable or unreadable, commands and skills say so plainly.

## Current state (as of 2026-09-24)

- `commonplace.scaffold_manifest` copies the source trees `kb/notes`, `kb/reference`, and `kb/instructions` to `kb/commonplace/<collection>/`, and `kb/types` to `kb/types`. It also scaffolds the project's own `kb/notes/` collection, so a project has `kb/notes/` (its own) next to `kb/commonplace/notes/` (the library). [ADR 021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) chose this layout.
- `init_project.py` copies a file only when the target does not exist. There is no update path for the copy, and a project records no Commonplace version, although ADR 021 specified a marker.
- The commands come from one user-level uv tool, with one active version per OS user ([ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)).
- The wheel build (`force-include` in `pyproject.toml`) ships the library trees as package data under `lib/python3.X/site-packages/`, a path that changes with the tool's Python version. 132 library files contain `../sources/` links. `kb/sources/` does not ship, so those links dangle in every installed copy.
- Code hardcodes the copy's project paths: review gates (`review/paths.py`), the critique instruction (`review/critique.py`), and library types (`lib/type_resolver.py`).
- Review baselines identify criteria by repository-relative paths. `freshness/versioning.py` requires snapshot inputs to resolve inside the repository.
- Code depends on exact global type paths. `kb/types/type-spec.md` is the root contract. Validation rules are keyed to `type-spec`, `tag-readme`, and `agentic-system-analysis-result`. Index generation expects `generated-index` and `tag-readme`.
- 13 collection-local schemas build on a global schema through `$ref`: 10 on `note.schema.yaml` and 3 on `note-base.schema.yaml`. `note.schema.yaml` differs from `note-base` only by forbidding `status:`.
- The promoted skills name library artifacts they read. `cp-skill-ground` and `cp-skill-ingest` word some references twice: "in a source checkout use X; in an installed project use Y".

## The design

Two layers. The base works without the skills layer.

1. **Base layer, for every harness.** The library installs as wheel shared data under `<uv tool environment>/share/commonplace/`. That path does not change with the tool's Python version or on upgrade. The tree mirrors the source repo's `kb/` layout: `instructions/` (with each skill in its own directory there), `notes/`, `reference/`, `types/`, and the gates. It needs no plugin manifest, because no harness plugin serves it. Commands read it there. In an editable install, commands read the source tree instead, because shared data is an install-time snapshot. The project's `AGENTS.md` names two commands: `commonplace-library` prints the library root, and `commonplace-instruction <name>` prints the path of one instruction, or lists them. An agent asked for a named instruction outside any skill runs the command and reads the file it prints. Committed project files never contain the library path, because it differs per machine.
2. **Skills layer, where the harness supports Agent Skills.** `commonplace-init` writes a stub for each `cp-skill-*` skill, and for the router skill, into the project's skill directories (`.claude/skills/`, `.agents/skills/`). A stub is a `SKILL.md` with the real skill's name and description and one instruction: read the real `SKILL.md` at its absolute path in the installed library and follow it, resolving its links relative to that file. The agent then runs the real skill in place, so skills are written as ordinary skills, with ordinary relative links to their own files, to library instructions, and to types. No skill calls a lookup command.

### Why stubs

Harnesses discover skills only in their own skill directories, so something has to be written there. Stubs are the smallest thing that works on every platform (operator decision, 2026-09-24). They act like a symlink that costs one extra read each time a skill is used. The alternatives were worse:

- Symlinks avoid the extra read, but they are unreliable on Windows, and the operator ruled out platform-specific install paths.
- Full copies go stale on every upgrade that changes a skill, and their relative links into the library point nowhere unless each skill looks files up through commands.
- A stub that calls a lookup command to find its skill works without an absolute path, but it adds a command call and a Claude Code permission rule for every skill use.

A stub carries a path specific to one machine. That costs nothing extra: stubs are not committed, and init has to rerun after the events that move the path anyway (below).

The layout condition matters. Because the installed tree mirrors `kb/`, a skill's relative link such as `../re-ingest.md` or `../../types/note.md` is correct both in the source checkout and in the installed library. That removes the two-branch wording ("in an installed project use X; in the source checkout use Y") without adding anything. Today's two layouts, `kb/commonplace/instructions/` and `kb/instructions/`, are the reason the branches exist.

Evidence so far: in both harnesses, an agent that read a library file at its real path followed the file's relative link correctly (`retire-widget` → `shared-step`). The relative-link failures in Codex came from symlinked skills, where the agent resolved `..` against the link's location; a stub has no symlink. Not yet tested: whether agents reliably follow the stub's redirect instead of acting on its description alone, and whether any skill metadata that a harness reads from the skill directory itself (frontmatter fields beyond name and description, or files such as Codex's `agents/`) must be copied into the stub.

### Harness permissions are part of init

In Claude Code, reading outside the project needs a permission rule. In `default` permission mode, a fresh session was denied every call to the lookup commands. With the commands allowed, reading the printed file was denied, because it lies outside the project. Two rules together removed every denial:

- read access to the library root, either as a `Read(//<root>/**)` allow rule or as an entry in `permissions.additionalDirectories`;
- a Bash allow rule for each lookup command (`Bash(commonplace-library:*)`, `Bash(commonplace-instruction:*)`). Stubs do not need these; only the base layer's route through `AGENTS.md` does.

Both worked from user-level settings and from a settings file passed with `--settings`. Project settings were not tested, but Claude Code merges them the same way (inferred). Init therefore writes them per project: the command rules name no path, so they can go in the committed `.claude/settings.json`; the read rule names this machine's library root, so it goes in the uncommitted `.claude/settings.local.json`. Codex needed no rules: its default sandbox allows the commands and the reads.

The read rule and the stubs name the same concrete root. The root is stable across upgrades and Python changes. It changes on a switch between an editable and a normal install, and when the uv tool directory changes. Init rewrites the rule and the stubs in the same run.

A root that the rule does not cover is worse than a denial. In one Claude Code run after a switch to an editable install, the agent was denied the source-tree file. It then followed a symlinked skill's relative link into `share/` and read the stale shared-data snapshot. A second run under the same conditions stopped without an answer. With stubs, the same failure takes a stub that still points into `share/` after the switch. The checks below report that case, and one init rerun fixes it.

### Keeping stubs and rules current

Without hooks, nothing refreshes stubs or rules when the install changes, so the design detects problems and gives the one command that repairs them: rerun `commonplace-init` in the project.

- Init is idempotent. On a rerun it overwrites stubs and permission entries that carry its marker, and it leaves the project's own files, skills, and settings alone. This changes today's rule that init never overwrites an existing file; that rule stays for the project's own KB files.
- A stub is current when its path points at the current library root and its name and description match the real skill. An upgrade leaves stubs current unless a skill was added, removed, or renamed, or its description changed.
- The health check, and the lookup commands where the check is cheap, report a missing, extra, or stale stub in the current project and an uncovered library root, and they name the init command. Both harnesses tested so far drop a broken skill without an error (observed for dangling symlinks), so these checks are the only signal.

### Skill names

Codex listed the probe's symlinked skills with a prefix (`cp-delivery-probe:delivery-probe-read`), and Claude Code listed them under their bare names. Codex's first run tied the prefix to the tree's `.claude-plugin/plugin.json`. The installed tree no longer has a manifest, and stubs sit in the project's own directory, so the bare names should hold in both harnesses. That is inferred, not tested.

## Proposed change to the install procedure

This is the user-visible form of the design. There is no per-machine setup step: after installing the tool, everything happens in `commonplace-init`, per project. It changes `INSTALL.md` steps 3–6, "Pre-approve Commonplace commands", "Resulting layout", and "Updating". The reader install and steps 1–2 are unchanged.

**Step 3, `commonplace-init`.** On a new project it creates the project's own KB directories and collection heads, and an `AGENTS.md.template` that names `commonplace-library` and `commonplace-instruction`. It no longer creates `kb/commonplace/` or the global types under `kb/types/`. On every run, new or not, it:

- writes a stub for each `cp-skill-*` skill and the router skill into `.claude/skills/` and `.agents/skills/`, overwriting only its own earlier stubs, and removes stubs for skills the package no longer has;
- writes Claude Code's permission entries: read access to this machine's library root in `.claude/settings.local.json`, and Bash allow rules for the lookup commands in `.claude/settings.json`;
- with `--check`, reports each stub and entry as `ok`, `missing`, or `stale` without writing anything, and exits non-zero on any problem.

If init finds a `kb/commonplace/` copy from an earlier release, it tells the operator to delete it.

**Step 5 shrinks to a check.** Run `commonplace-init --check`. For a harness whose skill directory init does not know, pass that directory to init.

**"Pre-approve Commonplace commands" becomes part of init** for the library read and the two lookup commands. Pre-approving the other `commonplace-*` commands stays optional.

**A new clone or a new machine.** Each person who clones the project runs `commonplace-init` once in their clone, because the stubs and the read rule are specific to the machine. Stubs and `.claude/settings.local.json` are not committed.

**Resulting layout.** The project contains `kb/` with its own collections and collection-local types, `AGENTS.md` or `CLAUDE.md`, the uncommitted stubs, and the two Claude Code settings files. It contains no `kb/commonplace/`, no global types, and no skill bodies.

**Updating.** After `uv tool upgrade llm-commonplace`, skills, instructions, and types change in place; nothing else is needed. If the upgrade added, removed, or renamed a skill or changed a description, the lookup commands warn in each project until `commonplace-init` reruns there. After switching between an editable and a normal install, rerun init: it rewrites the stubs and the read rule for the new root.

**Migrating an existing project.** Install the new tool, delete `kb/commonplace/` and the global type files under `kb/types/`, and rerun `commonplace-init`, which replaces the old `cp-skill-*` copies with stubs. Old copies carry no marker, so init has to recognise them by name the first time. Review baselines whose criteria move to package identities are retired once and rebuilt (see "Review identity").

## Parts the install change depends on

### Review identity

A package criterion gets a logical identifier relative to the library root, such as `commonplace:instructions/review-gates/prose/source-residue.md`. It contains neither a version nor an absolute path. Project criteria keep repository-relative paths. One resolver picks the root from the identifier and never falls back between package and project. Freshness still compares criterion text: an upgrade with identical text stays fresh, and edited text yields `criterion-changed`. The switch-over retires the baselines whose criteria gain package identities, once. Historical results stay under their original identities.

### Global type pointers

Global types leave `kb/types/`, so their pointers change, and a local schema's `$ref` to a global schema stops resolving.

- **Bare names (candidate).** A global type is named by its bare name, such as `type: note`. A collection-local type keeps its path form (`./`, `../`, or `kb/…`, ending in `.md`). The form alone tells the resolver which kind it has, with no fallback between them. A bare name `X` resolves to `types/X.md` under the library root, which is `kb/types/X.md` in the source repo, so both places write the same pointer. This partly reverses [ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md). ADR 018 objected to names because a name was looked up first in the collection's `types/` and then in `kb/types/`, so one name could mean different files. That lookup does not return: a bare name only ever means a global type. Global types are a small, closed set that the package owns (9 today). Framework validation rules would be keyed by bare name instead of canonical path ([ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). The migration rewrites about 800 `type:` lines mechanically.
- **A reserved `kb/types/` prefix.** It would look like a path but name no file in a project, so an agent that opened it would find nothing.

**Schema references.** The validator applies the `note-base` rule to every typed artifact, and a local schema never uses `$ref` outside its own `types/` directory. This drops `note.schema.yaml`'s `status:` ban from local types that do not restate it.

### How skills name library files

Skills link to library files by ordinary relative links, which resolve because the agent reads the skill at its real location and the installed tree mirrors `kb/` (see "Why stubs"). An instruction that only one skill uses can move into that skill's `references/`, as `cp-skill-write-multistage` already does.

### Making an unavailable library visible

- The control-plane template states that the project needs the tool and names the accepted versions.
- The health check and the lookup commands report a missing tool, a missing or stale stub, or an uncovered library root, with the exact command that fixes it.
- Validation reports a bare type name that it cannot resolve because the library is missing as "Commonplace library not available", not as a broken type.

### Links from project notes into the library

Relative links into `kb/commonplace/` stop resolving. ADR 021 found project-to-library links rare. **Candidate:** link to the library's published web pages, with no new link scheme until such links turn out to be common.

## Separable changes

These are useful in any layout and can ship before, after, or without the rest.

- **A prepared reader copy at build time.** The package build stages the library, replaces links to local ingests with their canonical external source URLs, regenerates navigation, and fails on any unresolved local link. Authored source files, with their grounding under [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md), stay unchanged. This fixes today's 132 dangling `../sources/` links.
- **A recorded version range.** The project records the Commonplace versions it accepts as a PEP 440 specifier, compared with the installed `llm-commonplace` version. This fills ADR 021's missing marker.
- **The implicit `note-base` rule.** It is useful in the source repo on its own.

## Rejected alternatives

- **A hidden, gitignored copy in the project.** It keeps the divergence. A variant that regenerates the copy when versions differ narrows the divergence to the window after an upgrade, and it silently discards edits to the copy.
- **A plugin tree published separately from the package** (GBrain's route). It breaks the one-tree constraint.
- **Hooks,** including a session-start hook that prints the library root. They break the no-hooks constraint.
- **Instructions served over MCP,** including GBrain's `get_skill`. It needs an MCP server, clients handle MCP instructions unreliably, and tool schemas cost context (see [the survey](./comparable-systems-survey.md)).
- **Codex plugins from a local marketplace.** Codex copies them into its cache, which breaks the one-tree constraint.
- **A Claude Code link-mode plugin** (dropped 2026-09-24). Its marketplace entry runs a command that prints the `share/` directory, and Claude Code links that directory into its cache instead of copying it. The earlier probe showed this works with a stand-in directory. It adds nothing over linked skills: its one advantage, relinking by itself after the install moves, is lost because init must rerun after a move anyway to rewrite the read permission. It also costs a manual approval by each user in their own terminal, prefixed skill names that duplicate the linked skills, and a second route to document and check, and link mode does not work on Windows. Reconsider it only if Commonplace ships something that must be a plugin component.
- **Full skill copies** in the project. They go stale on every upgrade that changes a skill, and their relative links into the library point nowhere, so each skill would have to look up library files through commands.
- **Stubs that find their skill through a lookup command.** They avoid a machine-specific path, but add a command call and a Claude Code permission rule to every skill use, and the stubs are not committed anyway.
- **Skill paths compiled at install** (init rewrites library references in skills to absolute paths). Stubs give the same result with one absolute path per skill and no rewrite of skill text.
- **Package data under `site-packages`.** Its path changes with the Python version, which would invalidate Claude Code's read rule on every Python change. It would also move every stub's path.
- **A per-user setup command** (rejected by the operator, 2026-09-24). It would install skills into user-level skill directories and write user-level Claude Code settings once per machine. It saves one init run per project after an upgrade, but the skills would then load in every project on the machine, including projects that do not use Commonplace, and it adds a second install command with its own scope.
- **Skill links into the package** (rejected by the operator, 2026-09-24). They avoid the copy and followed upgrades at once in both harnesses. But symlinks are unreliable on Windows, so Windows would need copies, and the operator ruled out platform-specific install paths: if one platform needs copies, every platform copies.
- **A symlink or junction at `kb/commonplace`.** It keeps the library in the project's view, and symlinks and junctions are unreliable on Windows.

## Forces

- **One copy against local control.** Reading the package in place removes divergence between the library and the code. The price is that the library changes on `uv tool upgrade`, with no diff for the user to review. The recorded version range makes an unwanted upgrade detectable.
- **Init writes harness settings into the project.** Claude Code needs permission entries, which init writes into the project's `.claude/` settings files. Where settings are managed centrally, a managed policy may override them.
- **Harness coupling.** The base layer depends on each harness allowing the lookup commands and reads outside the project, by default or through a setting. Claude Code and Codex allow it; other harnesses are being checked through the shared probe.
- **Visibility against discoverability.** The library no longer appears in searches of the project. Agents search the library root explicitly.
- **Portability.** A copied or cloned project carries no library. It still works as a plain-Markdown KB, but framework work needs the tool installed and `commonplace-init` run in each clone.
- **One extra read per skill use.** Every skill invocation first reads the stub, then the real skill. The operator accepted this cost (2026-09-24).
- **Stale stubs between an upgrade and init.** An upgrade that adds, removes, or renames a skill, or changes a description, leaves every project's stubs stale until init reruns there. The check makes this visible but does not prevent it.
- **Migration cost.** Existing projects delete their library copy and rerun init. Review baselines for moved criteria are retired and rebuilt once. Bare type names add a mechanical rewrite of about 800 lines in the source repo.

## Non-goals

- Changing where the source repo authors its library or types.
- Distributing grounding evidence for the library's claims, or relaxing grounding requirements for source authoring or project-owned content.
- Supporting project-owned global types. A project that wants one type in two collections keeps a copy in each, which [rests on](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) the claim that directory-scoped types are cheaper than global types.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy. Init detects it and tells the operator to delete it.

## Open choices

- Whether a stale skill or an uncovered root stops commands or only warns.
- Where the project keeps its version range. A `[tool.commonplace]` table in `pyproject.toml` suits Python projects, but a non-Python project would need that file for one field.
## Adoption criteria

Adopt when all of the following hold:

- An initialised project contains no library files and no global types, and its only framework files are marked stubs and settings entries, and commands read the library, gates, and global types only from the package.
- After `commonplace-init`, agents read the library without permission prompts in Claude Code and Codex, on Linux, macOS, and Windows. A root that the permission rules do not cover, and a stub that no longer matches the installed package, are detected.
- Every promoted skill, reached through its stub, finds the library files it links to, in the source repo and in installed projects, with no text that branches between them. Agents follow the stubs reliably in the required harnesses.
- Review checks show stable package identities across installation moves, unchanged freshness for identical criterion text, `criterion-changed` for edited text, and a clear failure for an unavailable criterion. Package and project criteria cannot shadow each other.
- A transition rehearsal keeps review history, retires only the affected baselines, and builds new ones through completed reviews.
- Every global `type:` pointer uses its bare name, and the validator rejects path-form pointers to global types.
- Operators who distribute projects by copying have been told what a copy carries.

Revisit the stubs when the required harnesses can discover skills from a configurable location on every platform. At that point the harnesses can read skills in place like the rest of the library, and the stubs and their checks can be deleted.

---

Relevant Notes:

- [ADR 021 — Ship library content under kb/commonplace](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) — the layout this design would supersede
- [ADR 064 — Install Commonplace commands as a user-level uv tool](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — the user-level placement this design extends to the library and skills
- [ADR 027 — Package scaffold assets without source-tree symlinks](../../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — the package-data boundary the library would be served from
- [Architecture](../../reference/architecture.md) — the installed topology this would change
- [Collections and types](../../reference/collections-and-types.md) — the type-resolution contract that bare global names would change
- [ADR 018 — Types are path references to instruction docs](../../reference/adr/018-types-are-path-references-to-instruction-docs.md) — the path-valued type decision bare names would partly reverse
- [ADR 048 — Imperative type rules dispatch by canonical path](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md) — the rule keying bare names would change
