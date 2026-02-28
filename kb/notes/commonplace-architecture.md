---
description: The commonplace repo's own internal layout — what exists, what's missing, and the decision to put global types in CLAUDE.md instead of kb/types/
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Commonplace architecture

The commonplace repo is itself a claw — it uses its own knowledge system to document the methodology for building claws. This note covers the repo's own layout, distinct from the [two-tree installation architecture](./commonplace-installation-architecture.md) that emerges when commonplace is installed into another project.

## Current layout

```
commonplace/
    kb/
      WRITING.md
      types/                         ← empty — see "Global types" below
      log.md                         ← improvement log (append-only)
      notes/
        types/                       ← note types (structured-claim, adr, etc.)
        related-systems/
        research/
        meta/
        *.md                         ← methodology and theory notes
      sources/
        types/                       ← source types (source-review)
        *.md                         ← reference material
      tasks/
        types/                       ← task types (active, backlog, recurring)
        backlog/
        active/
        completed/
    skills/                          ← skill templates (connect, convert, ingest, snapshot-web, validate)
    scripts/                         ← standalone tools (index generation, topic sync, snapshots)
    LICENSE
```

## What's missing

| Artifact | Status | Notes |
|----------|--------|-------|
| `.claude/skills/` | Missing | Rendered skills for commonplace's own use — need to render from `skills/` |
| `CLAUDE.md` | Missing | The repo's own instructions, routing table, and knowledge system section |
| `README.md` | Missing | Project overview for GitHub |

## Global types belong in CLAUDE.md, not kb/types/

The [installation architecture](./commonplace-installation-architecture.md) spec calls for `kb/types/` to hold global types — the maturity ladder (`text` and `note`). But these types are policy rules, not structural templates. The distinction:

- **Collection types** (notes/types/, sources/types/, tasks/types/) define concrete structural templates the agent reads when creating a specific document kind. They earn their own files because each is a multi-section scaffold.
- **Global types** define when a document promotes from one maturity level to another: no frontmatter means `text`, has frontmatter means `note`. This is a two-sentence rule, not a template.

Putting the maturity ladder in CLAUDE.md costs zero hops — it's always loaded. Putting it in `kb/types/` costs one hop and adds a directory that exists only to hold a trivial distinction. The collection types justify their directories because agents read them repeatedly during document creation. The global types don't — the agent internalizes "no frontmatter = text" once and never looks it up again.

Decision: drop `kb/types/` as a required directory. Encode the text/note maturity boundary in CLAUDE.md. Update the installation architecture spec to match.

## Naming inconsistency: related_works vs related-systems

The repo has both `kb/notes/related-systems/` (documented in the architecture spec) and `kb/notes/related_works/` (undocumented, uses underscores). These should be reconciled — either merge into one or document both.

## Open Questions

- Should skills/ include an install script, or is that separate tooling?
- What goes in CLAUDE.md for the commonplace repo itself vs what gets generated for installed projects?

---

Relevant Notes:
- [commonplace-installation-architecture](./commonplace-installation-architecture.md) — the two-tree design for installed projects; this note covers the repo's own layout
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — foundation: why collection-level types/ directories work but a global types/ directory is overhead
- [context-loading-strategy](./context-loading-strategy.md) — constrains: what goes in CLAUDE.md vs what the agent reads on demand

Topics:
- [claw-design](./claw-design.md)
