---
description: Shipped Commonplace architecture — installed project layout, packaged runtime, scaffolded library under kb/commonplace/, starter user collections, promoted skills, and the library/user boundary
type: kb/types/note.md
traits: []
tags: []
---

# Commonplace architecture

This note describes the architecture Commonplace ships into projects: the installed `kb/` tree, the package-provided command surface, and the runtime skill-discovery layer.

## Installed project layout

```text
project/
    kb/
      commonplace/                 ← shipped library (read-only by convention)
        notes/                     ← methodology theory
          types/
          *.md
        reference/                 ← shipped-system documentation + ADRs
          adr/
          types/
          *.md
        instructions/              ← methodology procedures + cp-skill-* skills
          review-gates/
          cp-skill-write/
          *.md
      types/                       ← shared global types (`text`, `note`, `instruction`, ...)
      notes/                       ← user's own notes; starts with COLLECTION.md and README.md
        types/
      reference/                   ← user's own reference; starts with COLLECTION.md and README.md
        types/
      instructions/                ← user's own instructions; starts with COLLECTION.md and README.md
      sources/                     ← user's tracked source records
        .gitignore                 ← keeps .snapshots/ local
        .snapshots/                ← local source reading copies
        types/
      tasks/                       ← user's task lifecycle
        backlog/
        active/
        completed/
      work/                        ← user's workshop / in-flight material
      reports/                     ← user's generated operational artifacts
        connect/
        types/
      log.md                       ← user's operational log
    .claude/skills/cp-skill-*/     ← known runtime skill projection
    .agents/skills/cp-skill-*/     ← known runtime skill projection
    AGENTS.md                      ← project control-plane file (from AGENTS.md.template)
```

The shipped library sits under `kb/commonplace/` as a single boundary the user treats as read-only. The user's own collections (`kb/notes/`, `kb/reference/`, `kb/instructions/`) are peers to the library at the top level of `kb/`. They start without user-authored artifacts but with a minimal `COLLECTION.md` contract and a curated `README.md` landing. Shared global types stay at top-level `kb/types/` so both the library and the user's own types can reference them with invariant absolute paths.

The framework implementation itself is not vendored into the project. It is installed once per OS user as an isolated uv tool and exposed through `commonplace-*` commands in uv's user-level executable directory. Projects do not need a Commonplace-specific venv, activation step, or `.envrc`. One tool installation supplies the active command version to all projects for that user.

The Python package carries the scaffold inputs as packaged data in built wheels. In the source checkout, the same inputs are read directly from the canonical repo paths rather than through duplicate scaffold files or source-tree symlinks.

## Surface by role

| Area | Role |
|------|------|
| `kb/commonplace/notes/` | Shipped transferable methodology theory |
| `kb/commonplace/reference/` | Shipped-system documentation plus ADR history |
| `kb/commonplace/instructions/` | Shipped methodology procedures and cp-skill-* skills |
| `kb/types/` | Shared global type contracts — library and user both use and extend |
| `kb/notes/`, `kb/reference/`, `kb/instructions/` | User's own collections, each with a starter `COLLECTION.md` contract and `README.md` landing |
| `kb/*/types/` | Collection-local structural contracts for specialised documents |
| `kb/sources/` | Tracked ingests/source reviews plus ignored local captures under `.snapshots/` |
| `kb/tasks/` | User's task lifecycle artifacts |
| `kb/work/` | User's temporal workshop material |
| `kb/reports/` | User's generated operational artifacts |
| `.claude/skills/`, `.agents/skills/` | Known runtime skill projections — copies of the `kb/commonplace/instructions/` skill directories; other runtimes may need their own projection |

## How the shipped surface is produced

`commonplace-init` is the install step that materialises the KB surface inside a project. It does four things:

1. Creates the directory shell under `kb/` — the user's collections, the user-space directories, and the `kb/commonplace/` hierarchy.
2. Copies shipped library trees into `kb/commonplace/{notes,reference,instructions}/`. Shared `kb/types/` and user-space type scaffolds (`kb/sources/types/`, `kb/reports/types/`) land at their conventional top-level locations. A nested `kb/sources/.gitignore` keeps `.snapshots/` local without changing a project's root ignore file.
3. Scaffolds a minimal `COLLECTION.md` contract and curated `README.md` landing into each empty user collection, giving write skills a conventions stub and readers a stable entry point.
4. Promotes selected skills into known `.claude/skills/cp-skill-*/` and `.agents/skills/cp-skill-*/` runtime surfaces as real copied directories of `kb/commonplace/instructions/<name>/`, and resolves the project-specific `AGENTS.md.template`. The canonical skill directories stay installed under `kb/commonplace/instructions/`; agent runtimes with a different discovery surface may need to copy, register, or import those directories themselves.

Command installation precedes this scaffold step. `uv tool install --python ">=3.11" llm-commonplace` installs a published release; contributors use `uv tool install --python ">=3.11" --editable .` from the source checkout. `uv tool update-shell` persists uv's executable-directory addition, and newly launched shells, IDEs, and agent processes then resolve the commands by bare name. Development-only executables such as `pytest` and `ruff` stay in the source project's dependency environment and run through `uv run`.

The result is that the agent's hot path stays inside the project tree. It reads `AGENTS.md`, the target collection's `COLLECTION.md`, and the relevant type files directly from the installed KB rather than jumping out to a separate framework checkout.

The scaffold input side has two modes. Built wheels include canonical KB trees under `commonplace/_data/` via explicit Hatch `force-include` mappings. Editable source checkouts fall back to the repository's canonical `kb/` paths and root templates, so contributors do not maintain duplicate scaffold copies.

## Boundary between library and user content

The shipped system draws a structural boundary at `kb/commonplace/`:

- **Library-provided content** — everything under `kb/commonplace/`. Read-only by convention; `commonplace-init` can re-sync it on upgrade.
- **User content** — everything else under `kb/`, including the user's own `notes/`, `reference/`, `instructions/`, sources, tasks, workshops, reports, and log. The project owns this tree outright.
- **Shared ground** — `kb/types/` is the one top-level collection both library and user extend. Both sides reference types via absolute `kb/types/...` paths, which stay invariant across our repo and a user's install.

A user who wants to extend a shipped type copies it from `kb/commonplace/<collection>/types/` into their own collection's `types/` directory. A user who wants to cite a shipped note from their own notes links across the boundary with a relative path like `../commonplace/notes/...` — the link structure works, but most users won't do this because their KBs are about different domains.

Re-running `commonplace-init` is safe: shipped files matching the scaffold are preserved; user-authored files are never overwritten.

## Path invariance across source and ship

Our repo works with `kb/notes/`, `kb/reference/`, `kb/instructions/` at the top level — the same position the user will work from in their own empty collections. Shipped content appears at `kb/commonplace/<collection>/` in a user's install. ADR-021 documents how references survive this remapping:

- **Sibling-relative markdown links** (`../notes/foo.md` from an instruction, `../reference/adr/010.md` from a note) are invariant because `kb/commonplace/` wraps siblings together.
- **Frontmatter type pointers** split: shared global types use absolute `kb/types/...` paths (invariant because shared types stay at top level), and collection-local types use file-relative paths like `./types/structured-claim.md` or `../types/adr.md` (invariant because the file-to-types relationship inside a collection is preserved under wrapping).
- **Generic natural-language references** (e.g. "a collection such as `kb/notes/`") are semantic labels that resolve to whatever `kb/notes/` means in the reader's context — our library in our repo, the user's collection in an install.

The type resolver in `src/commonplace/lib/type_resolver.py` accepts both absolute and file-relative `type:` values, so the same frontmatter strings work in both trees.

## Why `kb/commonplace/reference/` is part of the shipped surface

The installed system needs reference documentation about how its own architecture works, and that documentation must live where the agent already searches. Shipping `kb/commonplace/reference/` keeps the explanatory layer adjacent to the rest of the library: architecture notes, ADRs, and operator guidance all resolve through the same collection.

Project-authored reference material lives in the user's own `kb/reference/` collection next to the library copy. The two coexist as peers.

---

Relevant Notes:

- [Reference](./README.md) — overview of the shipped reference collection and operator guide
- [021-Ship library content under kb/commonplace](./adr/021-ship-library-content-under-kb-commonplace.md) — decision: the library/user boundary and path invariance rules this architecture implements
- [027-Package scaffold assets without source-tree symlinks](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — decision: package scaffold assets through explicit wheel includes plus source-checkout fallback
- [064-Install Commonplace commands as a user-level uv tool](./adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — decision: the command-installation authority and project-environment removal
- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: package-and-init model that ADR-021 refines with the `kb/commonplace/` namespace
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: the skills-first model and the core/local type split
- [collections and types](./collections-and-types.md) — how shipped type definitions are located and resolved, including file-relative pointers to collection-local types
