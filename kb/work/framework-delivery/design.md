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
2. The installed package holds the only copy of the library on a machine. A derived copy is allowed only where a platform cannot read the package in place, and it carries a version stamp and a hash check.
3. Commands and agents read the library from the package.
4. Skills find the library files they name, and a skill link or copy that no longer serves the installed package is detected.
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

Three layers. Each works without the ones above it.

1. **Base layer, for every harness.** The library installs as wheel shared data under `<uv tool environment>/share/commonplace/`. That path does not change with the tool's Python version or on upgrade. The tree is laid out as a plugin: skills, instructions, notes, reference, types, and gates. Commands read it there. In an editable install, commands read the source tree instead, because shared data is an install-time snapshot. The project's `AGENTS.md` names two commands: `commonplace-library` prints the library root, and `commonplace-instruction <name>` prints the path of one instruction, or lists them. An agent asked for a named instruction runs the command and reads the file it prints. Project files never contain the library path, because it differs per machine.
2. **Skills layer, where the harness supports Agent Skills.** Setup links each `cp-skill-*` directory from the harness's user-level skill directory into the package. Skills find library files through the same commands, by name. A router skill (`commonplace-library`) indexes the library by instruction name, so an agent asked for an instruction in conversation finds it through the skill's description.
3. **Harness-specific extras, optional.** In Claude Code, a link-mode plugin can serve the `share/commonplace/` tree in place: its marketplace entry runs a command that prints the directory, and Claude Code links the directory's top-level entries without copying them. Each user must accept that command once, in their own terminal. Codex copies local-marketplace plugins into its cache, so Codex uses layer 2 only.

### Harness permissions are part of setup

The base layer does not work in Claude Code without permission rules. In `default` permission mode, a fresh session was denied every call to the lookup commands. With the commands allowed, reading the printed file was denied, because it lies outside the project. Two rules together removed every denial:

- a Bash allow rule for each lookup command (`Bash(commonplace-library:*)`, `Bash(commonplace-instruction:*)`);
- read access to the library root, either as a `Read(//<root>/**)` allow rule or as an entry in `permissions.additionalDirectories`.

Both worked from user-level settings (`~/.claude/settings.json`), so one write covers every project. Codex needed no rules: its default sandbox allows the commands and the reads.

The read rule names a concrete path, so it covers only one library root. The root is stable across upgrades and Python changes. It changes on a switch between an editable and a normal install, and when the uv tool directory changes. Those are the same events that break skill links, so the same repair handles both.

A root that the rule does not cover is worse than a denial. In one Claude Code run after a switch to an editable install, the agent was denied the source-tree file. It then followed the skill's relative link, which still pointed into `share/`, and read the stale shared-data snapshot. The tokens matched only because the source and the snapshot were at the same version. A second run under the same conditions stopped without an answer. Two changes follow:

- Setup writes the rule for the current root and repairs the skill links in the same call. The checks below report a root the rule does not cover.
- Skills drop the relative-link fallback. The base layer already assumes a shell, and the fallback is the route by which a denied agent reached a stale copy. (Inferred from one run; the stale read has not been reproduced deliberately.)

### Keeping links and rules valid

Without hooks, nothing repairs links or rules when an install changes, so the design detects problems and gives the one command that repairs them.

- Setup is idempotent. It replaces skill links that point into any Commonplace install location, leaves unrelated entries alone, and rewrites the Commonplace permission entries for the current root.
- The health check, and the lookup commands where the check is cheap, report dangling or misdirected skill links and an uncovered library root, and name the setup command. Both harnesses tested so far drop a dangling skill without an error, so these checks are the only signal.
- In both harnesses, links made before a Python 3.12→3.13 reinstall still resolved afterwards, with no repair. Switches between editable and normal installs were detected and repaired by one setup call in each direction.

### Skill names

Codex prefixes a skill with the plugin name when the tree contains `.claude-plugin/plugin.json` (`cp-delivery-probe:delivery-probe-read`), even when the skill is a plain symlink. Claude Code listed the same links under their bare names. Documentation and invocation guidance must not assume either form.

## Proposed change to the install procedure

This is the user-visible form of the design. It changes `INSTALL.md` steps 3–6, "Pre-approve Commonplace commands", "Resulting layout", and "Updating". The reader install and steps 1–2 are unchanged.

**Step 3, `commonplace-init`, stops copying the library.** It creates the project's own KB directories and collection heads, and an `AGENTS.md.template` that names `commonplace-library` and `commonplace-instruction`. It no longer creates `kb/commonplace/`, the global types under `kb/types/`, or skill copies under `.agents/skills/` and `.claude/skills/`. If it finds a `kb/commonplace/` copy from an earlier release, it tells the operator to delete it.

**New step, per user and per machine: `commonplace-setup`** (name not settled). Run it once after installing the tool, and again after any switch between editable and normal installs or any change of the uv tool directory. It:

- links each `cp-skill-*` skill and the router skill into the user-level skill directory of each harness it finds (`~/.claude/skills`, `~/.agents/skills`, and directories the operator names). On Windows it copies them instead, with a version stamp and a hash check;
- writes Claude Code's user-level permission entries: Bash allow rules for the lookup commands, and read access to the current library root;
- prints, but cannot perform, the optional Claude Code plugin install, which the user must accept in their own terminal;
- with `--check`, reports each link and rule as `ok`, `missing`, `dangling`, `elsewhere`, or `stale-copy`, and exits non-zero on any problem.

Setup is a separate command from `commonplace-init` because the two have different scopes: init runs once per project, setup once per user and machine, and setup must rerun when the install changes while init does not.

**Step 5 shrinks to a check.** Skills are no longer projected per project. The step becomes: run `commonplace-setup --check`. For a harness whose skill directory setup does not know, pass that directory to setup.

**"Pre-approve Commonplace commands" becomes part of setup** for the two lookup commands and the library read. Pre-approving the other `commonplace-*` commands stays optional. It moves from `.claude/settings.local.json` to user-level settings, because the tool is installed per user.

**Resulting layout.** The project contains `kb/` with its own collections and collection-local types, and `AGENTS.md` or `CLAUDE.md`. It contains no `kb/commonplace/`, no global types, and no skills.

**Updating.** After `uv tool upgrade llm-commonplace`, nothing else is needed: the library path is unchanged, so linked skills and the read rule already point at the new content. After switching between an editable and a normal install, rerun `commonplace-setup`. Rerunning `commonplace-init` is no longer the way to pick up library changes.

**Migrating an existing project.** Install the new tool, run `commonplace-setup`, then delete `kb/commonplace/`, the global type files under `kb/types/`, and the `cp-skill-*` copies under `.agents/skills/` and `.claude/skills/`. Review baselines whose criteria move to package identities are retired once and rebuilt (see "Review identity").

## Parts the install change depends on

### Review identity

A package criterion gets a logical identifier relative to the library root, such as `commonplace:instructions/review-gates/prose/source-residue.md`. It contains neither a version nor an absolute path. Project criteria keep repository-relative paths. One resolver picks the root from the identifier and never falls back between package and project. Freshness still compares criterion text: an upgrade with identical text stays fresh, and edited text yields `criterion-changed`. The switch-over retires the baselines whose criteria gain package identities, once. Historical results stay under their original identities.

### Global type pointers

Global types leave `kb/types/`, so their pointers change, and a local schema's `$ref` to a global schema stops resolving.

- **Bare names (candidate).** A global type is named by its bare name, such as `type: note`. A collection-local type keeps its path form (`./`, `../`, or `kb/…`, ending in `.md`). The form alone tells the resolver which kind it has, with no fallback between them. A bare name `X` resolves to `types/X.md` under the library root, which is `kb/types/X.md` in the source repo, so both places write the same pointer. This partly reverses [ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md). ADR 018 objected to names because a name was looked up first in the collection's `types/` and then in `kb/types/`, so one name could mean different files. That lookup does not return: a bare name only ever means a global type. Global types are a small, closed set that the package owns (9 today). Framework validation rules would be keyed by bare name instead of canonical path ([ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). The migration rewrites about 800 `type:` lines mechanically.
- **A reserved `kb/types/` prefix.** It would look like a path but name no file in a project, so an agent that opened it would find nothing.

**Schema references.** The validator applies the `note-base` rule to every typed artifact, and a local schema never uses `$ref` outside its own `types/` directory. This drops `note.schema.yaml`'s `status:` ban from local types that do not restate it.

### How skills name library files

Skills name library files by instruction name and look them up with `commonplace-instruction`, or with `commonplace-library` for non-instruction files. The same text works in the source checkout and in installed projects, which removes the two-branch wording in `cp-skill-ground` and `cp-skill-ingest`. An instruction that only one skill uses can move into that skill's `references/`, as `cp-skill-write-multistage` already does.

### Making an unavailable library visible

- The control-plane template states that the project needs the tool and names the accepted versions.
- The health check and the lookup commands report a missing tool, a dangling or misdirected skill, a stale skill copy, or an uncovered library root, with the exact command that fixes it.
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
- **Relative links as a route skills depend on.** Agents in Codex misresolved them through symlinks, and in Claude Code a denied agent reached a stale snapshot through them.
- **Skill paths compiled at setup** (setup rewrites library references in skills to absolute paths). The command route gives the same result without machine-specific skill text or a rewrite step.
- **Package data under `site-packages`.** Its path changes with the Python version, which left linked skills dangling; Codex then dropped them silently.
- **A symlink or junction at `kb/commonplace`.** It keeps the library in the project's view, and symlinks and junctions are unreliable on Windows.

## Forces

- **One copy against local control.** Reading the package in place removes divergence between the library and the code. The price is that the library changes on `uv tool upgrade`, with no diff for the user to review. The recorded version range makes an unwanted upgrade detectable.
- **Setup writes user-level harness settings.** Claude Code needs permission entries that setup must write into the user's own settings file. That is a larger footprint than copying files into the project, and an operator who manages settings centrally must apply the entries themselves.
- **Harness coupling.** The base layer depends on each harness allowing the lookup commands and reads outside the project, by default or through a user-level setting. Claude Code and Codex allow it; other harnesses are being checked through the shared probe.
- **Visibility against discoverability.** The library no longer appears in searches of the project. Agents search the library root explicitly.
- **Portability.** A copied or cloned project carries no library. It still works as a plain-Markdown KB, but framework work needs the tool installed and set up on each machine.
- **Migration cost.** Existing projects rerun setup and delete their copies. Review baselines for moved criteria are retired and rebuilt once. Bare type names add a mechanical rewrite of about 800 lines in the source repo.

## Non-goals

- Changing where the source repo authors its library or types.
- Distributing grounding evidence for the library's claims, or relaxing grounding requirements for source authoring or project-owned content.
- Supporting project-owned global types. A project that wants one type in two collections keeps a copy in each, which [rests on](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) the claim that directory-scoped types are cheaper than global types.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy. Init detects it and tells the operator to delete it.

## Open choices

- The setup command's name, and whether a stale skill or an uncovered root stops commands or only warns.
- Whether setup edits the user's Claude Code settings file directly or prints the entries for the operator to apply. Direct edits suit most users; enterprise users may manage settings centrally.
- Where the project keeps its version range. A `[tool.commonplace]` table in `pyproject.toml` suits Python projects, but a non-Python project would need that file for one field.
- How the source checkout avoids listing each skill twice: once from its project-level `.claude/skills/` symlinks and once from the user-level links that setup writes.

## Adoption criteria

Adopt when all of the following hold:

- A set-up project contains no library files, no global types, and no skills, and commands read the library, gates, and global types only from the package.
- After setup, agents read the library without permission prompts in Claude Code and Codex, on Linux, macOS, and Windows. A root that the permission rules do not cover, and a skill link that no longer serves the installed package, are detected.
- Every promoted skill finds the library files it names, in the source repo and in installed projects, with no text that branches between them.
- Review checks show stable package identities across installation moves, unchanged freshness for identical criterion text, `criterion-changed` for edited text, and a clear failure for an unavailable criterion. Package and project criteria cannot shadow each other.
- A transition rehearsal keeps review history, retires only the affected baselines, and builds new ones through completed reviews.
- Every global `type:` pointer uses its bare name, and the validator rejects path-form pointers to global types.
- Operators who distribute projects by copying have been told what a copy carries.

Revisit the skill links when the required harnesses can discover skills from a configurable location. At that point the harnesses can read skills in place like the rest of the library, and the links and their checks can be deleted.

---

Relevant Notes:

- [ADR 021 — Ship library content under kb/commonplace](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) — the layout this design would supersede
- [ADR 064 — Install Commonplace commands as a user-level uv tool](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — the user-level placement this design extends to the library and skills
- [ADR 027 — Package scaffold assets without source-tree symlinks](../../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — the package-data boundary the library would be served from
- [Architecture](../../reference/architecture.md) — the installed topology this would change
- [Collections and types](../../reference/collections-and-types.md) — the type-resolution contract that bare global names would change
- [ADR 018 — Types are path references to instruction docs](../../reference/adr/018-types-are-path-references-to-instruction-docs.md) — the path-valued type decision bare names would partly reverse
- [ADR 048 — Imperative type rules dispatch by canonical path](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md) — the rule keying bare names would change
