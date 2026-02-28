---
description: Directories buy one–two orders of magnitude of human-navigable scale over flat files, and enable local conventions per subsystem — but each new directory taxes routing, search config, skills, and cross-directory linking
type: note
traits: []
status: seedling
areas: [document-system]
---

# Why directories despite their costs

The claw uses [files not database](./files-not-database.md) for simplicity and human navigability. But a flat directory with hundreds of files isn't really navigable — you're back to needing tooling (search, indexes) to find anything, which is what a database gives you. Directories preserve the human-navigability guarantee at scale. Not at every scale — but for one or two orders of magnitude more files before the same problem recurs.

## What directories give us

**Scale without tooling.** A `notes/` directory with 30 files is browsable. With 300, it isn't. Splitting into `notes/`, `claw-design/`, `sources/`, `adr/` keeps each directory in the browsable range. This isn't infinite — at thousands of notes you'd need deeper nesting or actual search infrastructure — but it extends the files-not-database sweet spot considerably.

**Local conventions per subsystem.** Some directories benefit from their own rules that don't need to generalise. Tasks have lifecycle subdirectories (`backlog/`, `active/`, `completed/`). Sources have an ingest pipeline. These are what the [workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) note calls "small, self-contained subsystems with their own conventions." Directories are natural boundaries for them.

**Different metabolic rates.** Sources churn fast (new ones arrive, get ingested, some get pruned). ADRs are nearly permanent. Notes are somewhere in between. Separating by metabolic rate lets you apply different lifecycle expectations — a 200-file `sources/` directory is normal; 200 files in `adr/` would signal something wrong.

## Types and directories are orthogonal

Types assert structural properties of individual documents — what sections are expected, what metadata is required, what's checkable. Directories group documents by topic, lifecycle, provenance, or whatever convention the user finds useful. These are independent axes.

A task in `tasks/active/` has `type: task` defining its structure (Goal, Tasks checklist, Current State). The `active/` directory tells you its lifecycle stage. Moving it to `completed/` changes the lifecycle signal without changing its type or structure.

A `structured-claim` works identically whether it lives in `notes/`, `notes/related-systems/`, or `claw-design/`. The directory carries provenance or topic grouping; the type carries structural expectations.

If types depended on directories, you'd need to redefine types whenever someone creates a new subdirectory. If directories encoded type information, you'd lose the freedom to organise by whatever dimension matters — topic, lifecycle, provenance, project area. The [document classification](./document-classification.md) system should work across any directory structure. Validation, search, and linking operate on individual documents via frontmatter, not on directory conventions.

## Operational costs of directories

Each new top-level directory imposes a registration tax across multiple places:

1. **CLAUDE.md routing table** — the "Where Things Go" table maps content types to directories. New directory = new row + routing heuristic prose explaining when to use it vs neighbours.
2. **qmd-collections.yml** — each directory needs its own collection entry for search indexing. Currently 11 entries.
3. **Skills hardcode directory lists** — `/connect` searches across three hardcoded directories (`notes/`, `claw-design/`, `sources/`). `/validate` only knows about `notes/`. `/convert` only knows about `notes/`. Adding a directory means auditing every skill.
4. **WRITING.md** — the "Where It Goes" section duplicates routing guidance. The templates table lists directory-specific templates.
5. **generate_notes_index.py** — needs to be invoked per directory (the script itself is directory-agnostic, but someone has to know to run it).

Softer costs:

6. **Cross-directory links** — relative path depth varies. `notes/foo.md` links to `../claw-design/bar.md`, but `notes/subdir/foo.md` needs `../../claw-design/bar.md`. More directories = more relative-path arithmetic.
7. **Agent routing decisions** — every new directory is a classification decision an agent has to make. The `notes/` vs `claw-design/` heuristic is already non-trivial ("Is it about general systems connecting LLMs and software, or about a specific genre — the claw genre?"). More directories = more routing errors.

## Current stance

The registration tax is real but manageable at the current scale (~6 top-level directories). The benefits — human navigability, local conventions, metabolic separation — outweigh the costs. The danger point is if we keep adding directories without noticing the cumulative tax: each one is small, but the aggregate burden on routing, skills, and search config grows linearly.

Mitigations to consider if directory count grows:
- A single registry file that skills and config derive from (instead of N hardcoded lists)
- Convention that subdirectories within a collection (like `notes/agent-learnings/`) don't need registration — only top-level collections do
- Tooling to validate that all collections are consistently registered

For now, the right default is: be reluctant to create new top-level directories. Subdirectories within existing collections are cheap. New collections are expensive.

---

Relevant Notes:
- [files not database](./files-not-database.md) — the foundational bet that directories extend
- [a functioning claw needs a workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — local conventions per directory are proto-workshop subsystems
- [document classification](./document-classification.md) — the type system that operates independently of directory structure
- [context loading strategy](./context-loading-strategy.md) — routing decisions are part of the context loading problem

Topics:
- [document-system](./document-system.md)
