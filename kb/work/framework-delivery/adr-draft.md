---
description: "Draft ADR 086: installed projects read the Commonplace library, global types, gates, and skills in place from the uv tool's shared data, through init-written skill stubs and a gitignored routing file, instead of a copy under kb/commonplace/"
type: kb/reference/types/adr.md
tags: []
---

# 086-Projects read the library from the installed package instead of a copy

**Status:** draft. Not yet decided and not implemented. The number 086 is reserved for this decision. It lives in the [framework-delivery workshop](./README.md) until the operator decides it; on adoption it moves to `kb/reference/adr/`.
**Date:** not yet decided (drafted 2026-09-24)
**Supersedes (on adoption):** [ADR 021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) (library shipped as a copy under `kb/commonplace/`)
**Partly reverses (on adoption):** [ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md) (path-valued `type:` for global types) and [ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md) (type rules keyed by canonical path)

## Context

In this ADR, *the library* means everything Commonplace owns and a project only reads: the library collections (notes, reference, instructions), the global types and their schemas, the review gates, the critique instruction, the templates, and the promoted skills.

`commonplace-init` copies the library into every project: the collections to `kb/commonplace/`, the global types to `kb/types/`, and the skills to `.claude/skills/` and `.agents/skills/`. The copy causes two problems.

- **Confusion.** Several hundred framework files sit next to the project's own collections, in its searches and its git history. Users cannot tell which files are theirs.
- **Divergence.** Init never overwrites an existing file, so the copy stays at the version of the first init. After a tool upgrade, new commands run against old gates, types, and skills. Each project holds its own version, and edits to the copy go unnoticed. The copy also ships 132 files with `../sources/` links that dangle, because `kb/sources/` does not ship.

Hiding the copy would fix the confusion but not the divergence.

The operator set these constraints for the choice ([workshop README](./README.md#operator-direction-and-constraints)):

- **Copy GBrain by default** (2026-09-23). GBrain is Commonplace's dominant competitor. Depart from a GBrain delivery method only for a Commonplace-specific reason, and record the reason.
- **One tree, one channel** (2026-09-24). The uv-installed package is the only tree that commands, agents, and harnesses read. Projects get no copy of framework content, and uv is the only release channel.
- **One install path on every platform** (2026-09-24). No platform-specific install paths. Symlinks are unreliable on Windows, so nothing is linked.
- **Init only, per project** (2026-09-24). No per-machine setup command.
- **No hooks** (2026-09-24), until hooks are standardised. At least one enterprise user runs their own harness.
- **Harness-neutral base** (2026-09-24). The design rests on files and a project `AGENTS.md`, with Agent Skills as an optional layer. An agent must still find a library instruction the user names in conversation, outside any skill.

## Decision

The library stays in the installed package, and projects read it there. `commonplace-init` writes only small, machine-specific, uncommitted files that point to it. The full design is in [design.md](./design.md) while the workshop exists.

**Where the library lives.** The library installs as wheel shared data under `<uv tool environment>/share/commonplace/`. That path does not change on upgrade or with the tool's Python version. The tree mirrors the source repository's `kb/` layout, so relative links between library files resolve the same way in the source checkout and in the installed tree. Commands read the library there; in an editable install they read the source tree instead.

**Base layer, for every harness.** Init writes a gitignored `.commonplace/library.md` holding the library root and its entry points as full paths, and a skill index: each skill's name, description, and full `SKILL.md` path. The index emulates the skills mechanism for harnesses that have none: an agent whose task matches a description reads that `SKILL.md` and follows it (operator decision, 2026-09-24). The committed `AGENTS.md` tells the agent to read that file; the committed `CLAUDE.md` imports it, so Claude Code has the paths in context from session start. From there the agent reads library files by full path. No agent route runs a command. Committed files never contain the library path, because it differs per machine.

**Skills layer, where the harness supports Agent Skills.** From the same skill list, init writes a stub per `cp-skill-*` skill, plus the router skill, into `.claude/skills/` and `.agents/skills/`. A stub carries the real skill's name and description and one instruction: read the real `SKILL.md` at its absolute path in the library and follow it, resolving links relative to that file. Skills therefore keep ordinary relative links, and the two-branch wording ("in a source checkout use X; in an installed project use Y") goes away. The stub approach was chosen by the operator (2026-09-24) at a known cost of one extra read per skill use. The stubs stay alongside the index because the harness applies a native skill's frontmatter, which the index cannot: forked context (13 of 16 skills), model choice, tool limits, and invocation by name.

**Harness permission.** Init writes one Claude Code rule, `Read(//<library root>/**)`, into the uncommitted `.claude/settings.local.json`. Codex needs none.

**Keeping init's outputs current.** Init is idempotent: on a rerun it overwrites its own stubs, routing file, and read rule, and leaves the project's own files alone. Every `commonplace-*` command recomputes init's outputs and warns, naming the init command, when a stub, the routing file, or the read rule is missing or stale. `commonplace-init --check` reports the same without writing.

**Parts the change depends on.** These ship with the delivery change:

- *Review identity.* A package criterion gets a logical identifier relative to the library root, such as `commonplace:instructions/review-gates/prose/source-residue.md`, with no version or absolute path. Project criteria keep repository-relative paths. One resolver picks the root from the identifier and never falls back between package and project. Baselines whose criteria move to package identifiers are retired once and rebuilt; historical results keep their original identifiers.
- *Bare global type names.* A global type is named by its bare name (`type: note`) and resolves to `types/<name>.md` under the library root. Collection-local and project-shared types keep the path form (`./`, `../`, or `kb/…`). The form alone selects the resolver, with no fallback, so a bare name cannot be shadowed. Framework validation rules are keyed by bare name. Local schemas stop using `$ref` to global schemas; the one restriction `note.schema.yaml` adds over `note-base`, its ban on `status:`, is restated in each local schema that inherited it, so the change does not alter which artifacts validate.
- *An unavailable library is visible.* The `AGENTS.md` template says the project needs the tool, and that an agent finding no `.commonplace/library.md` stops and asks for `commonplace-init` instead of looking for the library elsewhere. Commands and the health check report missing or stale init outputs with the fixing command. Validation reports a bare type name it cannot resolve because the library is missing as "Commonplace library not available", not as a broken type.

**Migration.** Rerunning init in an existing project compares each old framework copy (`kb/commonplace/`, global types under `kb/types/`, copied `cp-skill-*` directories) with the installed version. A matching file is removed or replaced by a stub. A differing file is kept and listed for the operator, because it may carry a local change and the old copies have no version marker.

## Considered alternatives

Each option below lost to a constraint or to evidence from the workshop's probes. [alternatives.md](./alternatives.md) holds the full list with evidence links.

**Keep a copy in the project.** A hidden, gitignored copy keeps the divergence. A variant that regenerates the copy on version change narrows divergence to the window after an upgrade, but silently discards edits. A symlink or junction at `kb/commonplace` keeps the library in the project's view and is unreliable on Windows.

**Serve package data from `site-packages`.** That path changes with the tool's Python version. In Codex, linked skills then dangled and were dropped with no warning. Under this design it would also invalidate every stub, routing file, and read rule on each Python change. Shared data under `share/` keeps one path.

**Other ways for harnesses to find skills.**

- *Full skill copies* go stale on every upgrade that changes a skill, and their relative links into the library point nowhere.
- *Symlinks into the package* followed upgrades at once in both harnesses, but the operator rejected them (2026-09-24): symlinks are unreliable on Windows, and no platform gets its own install path. Codex agents also resolved relative links against the symlink's location, not the target's.
- *A per-user setup command* writing user-level skills was rejected by the operator (2026-09-24). The skills would load in every project on the machine, including ones that do not use Commonplace, and it adds a second install command.
- *Stubs that look up their skill through a command*, and *skill text rewritten with absolute paths at install*, both lost to plain stubs. The first adds a command call and a permission rule per skill use; the second rewrites skill text for no gain over one absolute path per stub. A single stub for the whole library would lose per-skill triggering and invocation by name. *The skill index alone*, without stubs, would work in every harness but lose the frontmatter-driven behaviour above in harnesses that have native skills.

**Other ways to find the library outside a skill.** Lookup commands (`commonplace-library`, `commonplace-instruction <name>`) worked in both harnesses but cost a command call per session, need a shell, and need a permission rule per command in Claude Code. Writing the path into the committed `AGENTS.md` would make every teammate's init rewrite a committed file. A relative-link fallback in skills led a Claude Code agent, after an editable-install switch, into the stale `share/` snapshot.

**Harness plugins.** GBrain delivers through a plugin tree published separately from its CLI. This design departs from GBrain here, for the operator's one-tree reason: separate channels let the CLI and the plugins skew. Codex local-marketplace plugins are copied into Codex's cache, which goes stale on a uv upgrade. A Claude Code link-mode plugin was dropped (2026-09-24): its one advantage, relinking after the install moves, is lost because init must rerun after a move anyway, and it costs a manual approval per user, prefixed skill names, a second route to maintain, and no Windows support. Reconsider it if Commonplace ships something that must be a plugin component.

**Hooks and MCP.** A session-start hook printing the library root is ruled out by the no-hooks constraint. Serving instructions over MCP, as GBrain's `get_skill` does, is a second departure from GBrain: it needs an MCP server, clients handle MCP instructions unreliably, and tool schemas cost context.

**Smaller choices.** A `Read` rule was chosen over `permissions.additionalDirectories` because it is read-only; both removed the denials. Bare type names were chosen over a reserved `kb/types/` prefix, which would look like a path that names no file in a project. Project-owned shared types stay allowed, because banning them is a product restriction that package delivery does not require. Committable stubs with a `~/…` path were rejected because the uv tool directory differs on Windows and under a custom `UV_TOOL_DIR`.

**Left open.** Whether a stale stub or an uncovered root makes commands stop or only warn. Stopping would not close the stale-read gap (see Consequences), so the draft warns. Also open: where a project records its accepted Commonplace version range; a `[tool.commonplace]` table in `pyproject.toml` suits Python projects but not others.

## Consequences

**Easier.** The library, gates, and types can no longer drift from the installed code, because there is one copy per machine. Project trees, searches, and `git status` contain only the project's files. A normal `uv tool upgrade`, or a change of the tool's Python version, updates skills, instructions, and types in place with no init rerun. Skills lose their two-branch wording.

**Harder or riskier.**

- The library changes on upgrade with no diff for the user to review. A recorded version range (a separate change, below) makes an unwanted upgrade detectable.
- Each clone on each machine needs `commonplace-init` once, because none of init's outputs is committed. A copied project carries no library; it still works as plain Markdown, but framework work needs the tool.
- An upgrade that adds, removes, or renames a skill, or changes a description, leaves stubs stale in every project until init reruns there. Commands warn; nothing prevents it.
- Every skill use costs one extra read for the stub.
- After a switch between editable and normal install, or a change of the uv tool directory, stubs and `library.md` point at the old root. In both probed harnesses a fresh agent session then read the stale `share/` snapshot with no warning, because the file-only route runs no command. Command-time checks cannot catch a read that happens before any command runs. The mitigation is procedural: rerun init right after such a switch. The risk falls on developers, not on ordinary upgrades.
- Init writes harness settings into the project. A centrally managed Claude Code policy may override the read rule.
- Migration costs: projects delete their library copy and rerun init; review baselines for moved criteria are rebuilt once; the source repository rewrites about 800 `type:` lines to bare names.

**Separate changes.** Three changes are useful in any layout and are decided separately: a prepared reader copy at build time that replaces local ingest links with canonical source URLs and fails on unresolved links (the adoption criteria in [design.md](./design.md#adoption-criteria) require it before adoption); a recorded PEP 440 version range per project, which fills ADR 021's missing version marker; and applying the `note-base` rule implicitly.

**Operativity path.** `commonplace-init` consumes the decision when it writes stubs, `library.md`, the read rule, and `.gitignore` entries. Agents consume it through two channels: the harness's skill discovery loads a stub, whose instruction carries a skill's binding force to the real `SKILL.md`; and the committed `AGENTS.md` (or the `CLAUDE.md` import) points them to `library.md`, as advisory routing. `commonplace-*` commands consume it in code: they read the library from the package, resolve review identities and bare type names, and warn on stale init outputs. `INSTALL.md` steps 3–6, "Resulting layout", and "Updating" change to match.

**Where the decision stops applying.** The evidence is probe revision 4 on Linux only. Claude Code and Codex passed every case ([Claude Code](./results-claude-code-r4.md), [Codex](./results-codex-r4.md)), including the silent stale read after an install-mode switch. They differed once: in a clone without init, the Codex agent did not stop but answered from a nearby source checkout. The `AGENTS.md` template rule above answers that; it is untested. Replies from other harnesses (Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, enterprise harnesses) to the [probe request](./probe-request.md) are still pending. Untested and outside the decision's evidence: Windows and macOS, the router skill with a full-size index, the source checkout replacing its committed skill symlinks with stubs, upgrades during a running session, centrally managed settings, and skills whose harness reads metadata beyond name and description from the skill directory. The design assumes seven harness properties (H1–H7 in [design.md](./design.md#what-the-design-assumes-about-a-harness)): a user-level uv tool install, something that loads standing instructions into every session (the pointer line names no machine path or project, so a user-level or administrator-set prompt serves when `AGENTS.md` is not loaded), file reads outside the project, following an instruction to read a file by absolute path, project-level Agent Skills discovery (skills layer only), a shell (commands only), and sub-agents with a fresh context (skills that need workers). A harness that lacks H1, H3, or H4 is outside this decision and needs an operator decision of its own. In a harness without sub-agents, the skills that need workers stop with a blocker; no emulation is planned, and the operator chose to wait until harnesses provide sub-agents (2026-09-24). Revisit the stubs when the required harnesses can discover skills from a configurable location on every platform; the stubs and their checks can then be deleted.
