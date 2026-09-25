# Design: library served from the installed package

This is the workshop's only design document. It replaced the proposal `kb/reference/proposals/library-served-from-the-installed-package.md` on 2026-09-24. It describes the chosen design only; the options rejected along the way, and the evidence behind each, are in [alternatives.md](./alternatives.md).

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

Two layers. The base works without the skills layer, and emulates it for harnesses that have none.

1. **Base layer, for every harness.** The library installs as wheel shared data under `<uv tool environment>/share/commonplace/`. That path does not change with the tool's Python version or on upgrade. The tree mirrors the source repo's `kb/` layout: `instructions/` (with each skill in its own directory there), `notes/`, `reference/`, `types/`, and the gates. It needs no plugin manifest, because no harness plugin serves it. Commands read it there. In an editable install, commands read the source tree instead, because shared data is an install-time snapshot. `commonplace-init` writes `.commonplace/library.md` into the project: the library root and the library's entry points (the instructions index, `notes/tags-README.md`, the types), each as a full path, and a skill index giving each skill's name, description, and full `SKILL.md` path. The skill index emulates the skills mechanism: an agent whose task matches a description reads that `SKILL.md` and follows it. The committed `AGENTS.md` says to read that file for the Commonplace library. The committed `CLAUDE.md` imports it (`@.commonplace/library.md`), so Claude Code has the paths in context from the start of a session. From there the agent reads files by full path, and links inside library files resolve relative to each file. No agent route runs a command. Committed project files never contain the library path, because it differs per machine.
2. **Skills layer, where the harness supports Agent Skills.** From the same skill list, `commonplace-init` writes a stub for each `cp-skill-*` skill, and for the router skill, into the project's skill directories (`.claude/skills/`, `.agents/skills/`). The router is a new skill, `cp-skill-library`, that indexes the library's instructions by name. A stub is a `SKILL.md` with the real skill's name and description and one instruction: read the real `SKILL.md` at its absolute path in the installed library and follow it, resolving its links relative to that file. The agent then runs the real skill in place, so skills are written as ordinary skills, with ordinary relative links to their own files, to library instructions, and to types. No skill calls a lookup command.

### Why stubs

Harnesses discover skills only in their own skill directories, so something has to be written there. A stub is the smallest thing that works the same way on every platform (operator decision, 2026-09-24). It acts like a symlink that costs one extra read each time a skill is used. A stub carries a path specific to one machine; that costs nothing, because stubs are not committed and init reruns after the events that move the path.

Because the installed tree mirrors `kb/`, a skill's relative link such as `../re-ingest.md` or `../../types/note.md` is correct both in the source checkout and in the installed library. That removes the two-branch wording ("in an installed project use X; in the source checkout use Y"), which exists today only because the two layouts differ.

In Claude Code and Codex, probe revision 4 confirmed the route ([Claude Code](./results-claude-code-r4.md), [Codex](./results-codex-r4.md)). In Claude Code's five skill sessions and router session, the agent followed the stub to the real skill and resolved every relative link from the real location, with no failed read ([results](./results-claude-code-r4.md)). Not yet tested: stubs in Codex, and whether a harness reads skill metadata from the skill directory itself (frontmatter fields beyond name and description, or files such as Codex's `agents/`) that init must copy into the stub.

### Why both a skill index and stubs

Some harnesses have no skills mechanism, so the base layer carries a skill index that emulates one (operator decision, 2026-09-24). The index could also replace the stubs, but a stub keeps what only a native skill gets. The harness applies the skill's frontmatter: 13 of the 16 skills run in a forked context (`context: fork`), 9 choose a model, all 16 limit their tools, and all 16 can be invoked by name. A native skill's description is also always in the harness's view. With the index alone, Claude Code sees the descriptions through the `CLAUDE.md` import, but an agent in a harness without imports sees them only after it chooses to read `library.md`. Both are generated from the same skill list, so keeping the stubs adds no source of drift. Whether the index triggers skills reliably is untested; probe revision 5 tests it (case 9).

### Why a generated routing file

An agent outside a skill needs the library root. `library.md` supplies it (operator decision, 2026-09-24). It costs one read per session at most, and nothing in Claude Code, where `CLAUDE.md` imports it; after that the root stays in context. It needs no shell and no command permission. It lists entry points, not every instruction, because the library has its own navigation. It also lists every skill, so it goes stale when the root moves or when a skill is added, removed, or renamed or its description changes, the same events that make the stubs stale. The path is machine-specific, so the file is gitignored and `AGENTS.md` only points to it.

### Harness permissions are part of init

In Claude Code, reading outside the project needs a permission rule. Init writes a `Read(//<root>/**)` allow rule for this machine's library root into the uncommitted `.claude/settings.local.json`. Revision 4 showed that this one rule is the only setting Claude Code needs, and that without it the reads are denied. Codex needs no rule: its default sandbox allows the reads.

The read rule, the stubs, and the generated file name the same concrete root. The root is stable across upgrades and Python changes. It changes on a switch between an editable and a normal install, and when the uv tool directory changes. Init rewrites all three in the same run.

**Risk after an install-mode switch.** After a switch to an editable install and before init reruns, the stubs and `library.md` still point into `share/`, which uv leaves as a stale snapshot. Revision 4 observed this in Claude Code: a fresh session read the old version with no warning, because no agent route runs a command that could warn. The risk is limited to install-mode switches and uv tool directory changes, which developers make, not to ordinary upgrades, where the path does not move. The guarantee is therefore narrow: stale outputs are detected when a `commonplace-*` command or `init --check` runs, not when an agent reads files. Making commands fail instead of warn would not change this, because the stale read can happen before any command runs. The developer procedure is: rerun `commonplace-init` immediately after any switch.

### Keeping init's outputs current

Without hooks, nothing refreshes the stubs, the generated file, or the read rule when the install changes, so the design detects problems and gives the one command that repairs them: rerun `commonplace-init` in the project.

- Init reads and writes every file as UTF-8 and accepts a UTF-8 byte-order mark when reading. Windows PowerShell 5.1 writes one, and a settings file starting with it crashed the probe's init on Windows.
- Init is idempotent. On a rerun it overwrites its own stubs, generated file, and read rule, and it leaves the project's own files, skills, and settings alone. This changes today's rule that init never overwrites an existing file; that rule stays for the project's own KB files.
- A stub, and the skill index in `library.md`, are current when their paths point at the current library root and their names and descriptions match the real skills. An upgrade leaves stubs current unless a skill was added, removed, or renamed, or its description changed.
- Every `commonplace-*` command runs one cheap check: it recomputes init's outputs for the current project and compares them with the files. A missing, extra, or stale stub, a stale generated file, or a read rule for another root produces a warning that names the init command. This is command-time detection: agents run `commonplace-validate` often, so a stale output surfaces at the next command, but a read before that is not caught. Both harnesses tested drop a broken skill without an error, so these checks are the only signal.

### What the design assumes about a harness

Replies to the [probe request](./probe-request.md) report outcomes and the size of any workaround, and describe the workaround as far as the respondent's company policy allows: an agent in the harness may adapt the design and say whether each outcome was reached, which part of the design the workaround changed, how much effort it took, how often it repeats, and whether an administrator was needed. A description of the workaround shows what the design should provide itself. A part of the design that needs a large or repeated workaround is a design problem even where it works. An outcome that was not reached points to the assumption that failed: outcome 1 (install) to H1, outcome 2 (a named instruction) to H2–H4, outcome 3 (a skill) to H4–H5. Each assumption is listed with what a "no" would change.

| Assumption | Needed for | If the answer is no |
|---|---|---|
| H1. Commonplace can be installed as a user-level uv tool. | Everything | The package can come from an internal package index or a wheel file instead of PyPI; uv supports both. If no user-level Python tool install is allowed at all, this design has no channel, and the operator must choose another. |
| H2. Something loads standing instructions into every session: `AGENTS.md`, another file, a user-level setting, or a system prompt. | The base layer | The pointer to `library.md` goes into whatever does load standing instructions. The pointer names no machine path and no particular project ("read `.commonplace/library.md` in the current project; if it is missing, stop and ask for init"), so it can be set once per user or by an administrator, not once per project. Init writes it where that mechanism is a file it can reach. If nothing loads standing instructions, the user gives the pointer in every session, a per-session workaround. |
| H3. The agent can read files outside the project, at the uv tool directory, by default or through a setting the user can make. | Both layers | Reads outside the project are impossible, so the library would have to sit inside the project. That means a gitignored copy refreshed by init, which breaks the one-tree constraint and was rejected (see [alternatives.md](./alternatives.md)). It would need an operator decision for that harness. |
| H4. The agent follows a written instruction to read another file by absolute path and act on it. | Both layers (the `library.md` pointer and the stubs) | Neither route works. The fallback is full copies of what the agent must read, which were rejected; operator decision. |
| H5. The harness discovers Agent Skills from a project directory. | The skills layer only | The skill index in `library.md` stands in: an agent picks a skill by its description there and reads its `SKILL.md`. The skill loses what only the harness applies: forked context, model choice, tool limits, and invocation by name. |
| H6. The agent can run shell commands. | The `commonplace-*` commands, not delivery | Delivery works; command-time checks and KB maintenance commands do not. |
| H7. The agent can start sub-agents with a fresh context. | Skills that need workers (`cp-skill-ingest`, `cp-skill-write-multistage`, `cp-skill-revise-autoreason`, `analyse-agentic-system`), and forked execution (`context: fork`, 13 of 16 skills) | Forked skills run in the calling session instead. For skills that need workers, sub-agents are emulated, so that users of such harnesses can start using Commonplace (operator decision, 2026-09-24). The emulation is designed per harness by an agent working there; probe case 10 collects designs, for example another session of the harness started from the shell, or a session the user starts with a worker packet. The skills are less useful this way: separate contexts may be weaker or slower, and a step may need the user. An adopted emulation would also revise skill rules that forbid it today; `cp-skill-ingest` forbids launching the harness CLI as a worker. |

Claude Code and Codex satisfy H1–H7 on Linux (probe revision 4; H7 from their native sub-agent tools, not yet probed). Codex has no import in its instruction file, so it reads `library.md` itself, at the cost of one read per session.

### Skill names

Claude Code lists the stubs under their bare names. Codex prefixed skills with a plugin name while the probe tree carried a plugin manifest; the installed tree no longer has one, so bare names are expected there too, but that is untested.

## Proposed change to the install procedure

This is the user-visible form of the design. There is no per-machine setup step: after installing the tool, everything happens in `commonplace-init`, per project. It changes `INSTALL.md` steps 3–6, "Pre-approve Commonplace commands", "Resulting layout", and "Updating". The reader install and steps 1–2 are unchanged.

**Step 3, `commonplace-init`.** On a new project it creates the project's own KB directories and collection heads, and templates for `AGENTS.md` (which points to `.commonplace/library.md`) and `CLAUDE.md` (which imports `AGENTS.md` and `.commonplace/library.md`). The `CLAUDE.md` template is new; only `AGENTS.md.template` exists today. It no longer creates `kb/commonplace/` or the global types under `kb/types/`. On every run, new or not, it:

- writes a stub for each `cp-skill-*` skill and the router skill into `.claude/skills/` and `.agents/skills/`, overwriting only its own earlier stubs, and removes stubs for skills the package no longer has;
- writes `.commonplace/library.md` with this machine's library root, entry points, and skill index;
- writes Claude Code's read rule for this machine's library root into `.claude/settings.local.json`;
- adds its outputs to `.gitignore`;
- with `--check`, reports each stub and entry as `ok`, `missing`, or `stale` without writing anything, and exits non-zero on any problem.

If init finds a `kb/commonplace/` copy from an earlier release, it tells the operator to delete it.

**Step 5 shrinks to a check.** Run `commonplace-init --check`. The source checkout does not run init (operator decision, 2026-09-25). It is where the library is authored, and its committed `.claude/skills/` and `.agents/skills/` symlinks cover all its skills, including five that are not promoted. For a harness whose skill directory init does not know, pass that directory to init.

**"Pre-approve Commonplace commands" stays optional.** Delivery needs only the read rule, which init writes. Agents run `commonplace-*` commands in ordinary work, and pre-approving them is unchanged.

**A new clone or a new machine.** Each person who clones the project runs `commonplace-init` once in their clone, because the stubs, the generated file, and the read rule are specific to the machine. None of them is committed.

**Resulting layout.** The project contains `kb/` with its own collections and collection-local types, `AGENTS.md` and `CLAUDE.md`, and init's uncommitted outputs: the stubs, `.commonplace/library.md`, and `.claude/settings.local.json`. It contains no `kb/commonplace/`, no global types, and no skill bodies.

**Updating.** After `uv tool upgrade llm-commonplace`, skills, instructions, and types change in place; nothing else is needed. If the upgrade added, removed, or renamed a skill or changed a description, `commonplace-*` commands warn in each project until `commonplace-init` reruns there. After switching between an editable and a normal install, rerun init: it rewrites its outputs for the new root.

**Migrating an existing project.** Install the new tool and rerun `commonplace-init`. Init inventories the old framework copies: `kb/commonplace/`, the global type files under `kb/types/`, and the `cp-skill-*` directories under `.claude/skills/` and `.agents/skills/`. It compares each file with the installed package's version. A file that matches is removed, and a skill copy that matches is replaced by a stub. A file that differs is left in place and listed, because it may carry a local change; a matching name does not show that a file is disposable. The old copies carry no version marker, so a differing file may also be an unmodified file from an older release; the operator decides which. This follows the agent-operability workshop's constraint that no upgrade operation silently overwrites a differing file. Review baselines whose criteria move to package identities are retired once and rebuilt (see "Review identity").

## Parts the install change depends on

### Review identity

A criterion file outside the repository, in the installed library, is identified relative to the library root, such as `commonplace:instructions/review-gates/prose/source-residue.md`. The identity contains neither a version nor an absolute path. A criterion file inside the repository keeps its repository-relative path; in the source checkout, where the library is the repository's own `kb/`, that covers the library too, so the checkout's existing review baselines keep their identities (implementation decision, 2026-09-25). The identity's form decides where it resolves; there is no fallback between library and project. Freshness still compares criterion text: an upgrade with identical text stays fresh, and edited text yields `criterion-changed`. The switch-over retires the baselines whose criteria gain package identities, once. Historical results stay under their original identities.

### Global type pointers

Global types leave `kb/types/`, so their pointers change, and a local schema's `$ref` to a global schema stops resolving.

A global type is named by its bare name, such as `type: note`. A collection-local type keeps its path form (`./`, `../`, or `kb/…`, ending in `.md`). The form alone tells the resolver which kind it has, with no fallback between them. A bare name `X` resolves to `types/X.md` under the library root, which is `kb/types/X.md` in the source repo, so both places write the same pointer. This partly reverses [ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md). ADR 018 objected to names because a name was looked up first in the collection's `types/` and then in `kb/types/`, so one name could mean different files. That lookup does not return: a bare name only ever means a global type. Global types are a small, closed set that the package owns (9 today). Framework validation rules would be keyed by bare name instead of canonical path ([ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md)). The migration rewrites about 800 `type:` lines mechanically.

A project that wants its own type shared across collections keeps the path form, for example `type: kb/types/my-type.md`. Bare names are reserved for the package's global types, so the two cannot shadow each other.

Bare names reach beyond `type:` lines. Each global type spec names its schema as `schema: kb/types/X.schema.yaml`, and seven global schemas pin `const: kb/types/X.md`. The type resolver requires every type doc and schema to sit under the project's `kb/`, and `validate_instance` rewrites `type:` to the canonical path before schema checks. Type rules are keyed by canonical path. All of these change with the resolver. The rewrite covers about 776 tracked frontmatter `type:` lines, plus body examples and 60 test lines; gitignored review state under `kb/reports/` holds about 1,900 more, which are regenerated rather than rewritten.

**The project's report and source types.** `kb/reports/types/` and `kb/sources/types/` are the contracts of the project's own reports and sources collections. Init keeps writing them into the project, as it does today (operator decision, 2026-09-25). Their schemas `$ref` the global `note.schema.yaml`; like other local schemas, they restate what they need instead.

**Schema references.** A local schema that builds on a global schema refers to it as `commonplace:types/<name>.schema.yaml`, which the validator resolves in the installed library. This keeps validation exactly as it is: each local schema still inherits what it inherited before, including `note.schema.yaml`'s ban on `status:`. It replaces an earlier plan to apply `note-base` implicitly to every typed artifact, which would have started validating local types that inherit nothing today (implementation decision, 2026-09-25).

**Where the library is.** `library_root()` finds the library: the source tree's `kb/` in an editable install, otherwise the tool's shared data. The environment variable `COMMONPLACE_LIBRARY_ROOT` overrides both; tests use it to make a temporary repository its own library, as the source checkout is.

### How skills name library files

Skills link to library files by ordinary relative links, which resolve because the agent reads the skill at its real location and the installed tree mirrors `kb/` (see "Why stubs"). An instruction that only one skill uses can move into that skill's `references/`, as `cp-skill-write-multistage` already does.

### Making an unavailable library visible

- The control-plane template states that the project needs the tool and names the accepted versions. It also says that if `.commonplace/library.md` is missing, the agent stops and tells the user to run `commonplace-init`, instead of looking for the library elsewhere. In Codex's revision 4 run, an agent in a clone without init searched nearby directories, found a source checkout, and answered from it without reporting the missing file; Claude Code stopped on its own. The template rule is untested.
- The health check and every `commonplace-*` command report a missing or stale stub, a stale generated file, or an uncovered library root, with the exact command that fixes it. A missing tool shows up as a missing command, and `AGENTS.md` says the project needs the tool.
- Validation reports a bare type name that it cannot resolve because the library is missing as "Commonplace library not available", not as a broken type.

### Links from project notes into the library

Relative links into `kb/commonplace/` stop resolving. ADR 021 found project-to-library links rare. **Candidate:** link to the library's published web pages, with no new link scheme until such links turn out to be common.

## Separable changes

These are useful in any layout and can ship before, after, or without the rest.

- **A prepared reader copy at build time.** The package build stages the library, replaces links to local ingests with their canonical external source URLs, regenerates navigation, and fails on any unresolved local link. Authored source files, with their grounding under [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md), stay unchanged. This fixes today's 132 dangling `../sources/` links.
- **A recorded version range.** The project records the Commonplace versions it accepts as a PEP 440 specifier, compared with the installed `llm-commonplace` version. This fills ADR 021's missing marker.
- **The implicit `note-base` rule.** It is useful in the source repo on its own.

## Rejected alternatives

See [alternatives.md](./alternatives.md).

## Forces

- **One copy against local control.** Reading the package in place removes divergence between the library and the code. The price is that the library changes on `uv tool upgrade`, with no diff for the user to review. The recorded version range makes an unwanted upgrade detectable.
- **Init writes harness settings into the project.** Claude Code needs permission entries, which init writes into the project's `.claude/` settings files. Where settings are managed centrally, a managed policy may override them.
- **Harness coupling.** The base layer depends on each harness allowing reads outside the project, by default or through a setting, and on the harness reading `AGENTS.md`. Claude Code and Codex allow it; other harnesses are being checked through the shared probe.
- **Visibility against discoverability.** The library no longer appears in searches of the project. Agents search the library root explicitly.
- **Portability.** A copied or cloned project carries no library. It still works as a plain-Markdown KB, but framework work needs the tool installed and `commonplace-init` run in each clone.
- **One extra read per skill use.** Every skill invocation first reads the stub, then the real skill. The operator accepted this cost (2026-09-24).
- **Stale stubs between an upgrade and init.** An upgrade that adds, removes, or renames a skill, or changes a description, leaves every project's stubs stale until init reruns there. The check makes this visible but does not prevent it.
- **Migration cost.** Existing projects delete their library copy and rerun init. Review baselines for moved criteria are retired and rebuilt once. Bare type names add a mechanical rewrite of about 800 lines in the source repo.

## Non-goals

- Changing where the source repo authors its library or types.
- Distributing grounding evidence for the library's claims, or relaxing grounding requirements for source authoring or project-owned content.
- Backwards compatibility for projects with an existing `kb/commonplace/` copy, beyond the migration's preservation rule.

## Open choices

- Whether a stale skill or an uncovered root stops commands or only warns.
- Where the project keeps its version range. A `[tool.commonplace]` table in `pyproject.toml` suits Python projects, but a non-Python project would need that file for one field.

## Adoption criteria

Adopt when all of the following hold:

- An initialised project contains no library files and no global types, and its only framework files are marked stubs and settings entries, and commands read the library, gates, and global types only from the package.
- After `commonplace-init`, agents read the library without permission prompts in Claude Code and Codex, on Linux, macOS, and Windows. A root that the permission rules do not cover, and a stub that no longer matches the installed package, are detected.
- Every promoted skill, reached through its stub, finds the library files it links to, in the source repo and in installed projects, with no text that branches between them. Agents follow the stubs reliably in the required harnesses.
- Review checks show stable package identities across installation moves, unchanged freshness for identical criterion text, `criterion-changed` for edited text, and a clear failure for an unavailable criterion. Package and project criteria cannot shadow each other.
- The review transition keeps review history, retires only the affected baselines, and builds new ones through completed reviews.
- Every global `type:` pointer uses its bare name, and the validator rejects path-form pointers to global types.
- Operators who distribute projects by copying have been told what a copy carries.
- The built package has no unresolved local links: the prepared reader copy (see "Separable changes") is in place. Mirroring the `kb/` layout fixes links among shipped files, but not links into collections the package omits.
- Migration keeps and lists a framework file that differs from the installed package.

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
