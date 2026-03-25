# Directories can replace type fields for structural exemptions

## Observation

During the frontmatter review sweep (2026-03-25), two patterns emerged where notes needed different treatment from the default `note` type — but adding new type field values felt like unnecessary bureaucracy.

**Definitions** — term-pinning notes like `constraining.md`, `distillation.md`, `codification.md`, `context-engineering.md`. These have bare-noun titles by nature (the title IS the term). The frontmatter review's composability check should exempt them, but the check had no way to distinguish them from notes with lazy topical titles.

**Articles** — extended multi-claim theory notes like `a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md`. These have topical titles because you can't compress a multi-part theory into one claim sentence. The title-body alignment check flags them because the title covers only the first section, but splitting them would break the argument chain.

## What we did

For definitions: moved 4 notes to `kb/notes/definitions/`. The directory makes the exemption structural — the selector and review instructions can route by path. No type field needed, no schema change, no frontmatter to keep in sync. The directory IS the type signal.

For articles: not yet moved, but the same pattern applies. A `kb/notes/articles/` directory would signal "multi-claim extended argument" and exempt the note from single-claim title conventions.

## Why directories work here

The [why-notes-have-types](../../notes/why-notes-have-types.md) note lists six roles: navigation, metadata enforcement, verification, extensibility, output quality, maturation. The directory approach serves a seventh: **review routing**. The frontmatter review, prose review, and complexity review need to know what conventions apply to a note. A directory is a stronger signal than a type field because:

1. **No sync problem.** A type field can drift from reality (note says `definition` but reads like a claim). A file in `definitions/` can't be in the wrong directory by accident — someone moved it there.
2. **Cheaper than schema changes.** Adding a type value requires updating WRITING.md, validation, type templates. Creating a directory requires `mkdir`.
3. **Visible in the filesystem.** An agent scanning the directory tree sees `definitions/constraining.md` and knows immediately what kind of note it is, before reading frontmatter.

The trade-off: directories impose physical separation. A definition in `definitions/` is one path segment further from its neighbors. Every inbound link needs `./definitions/` instead of `./`. For heavily-linked notes (constraining has ~240 inbound links), the migration cost is real.

## When to use directories vs types vs traits

Emerging heuristic:

- **Directory** when the distinction routes review checks, the set is small and stable, and physical grouping aids browsing. Definitions and articles fit.
- **Type field** when the distinction affects structure (required sections, affordances) and the note participates in the general `kb/notes/` population. Structured-claim, ADR, index fit.
- **Trait** when the property is additive and doesn't change the note's fundamental kind. `has-comparison`, `has-external-sources` fit.

## Open questions

- Should articles get their own directory now (one candidate) or wait until there are 3+?
- Are there other candidates for directory-as-type? Brainstorming notes (`brainstorming-*.md`) share conventions but there are only a few.
- Should `definitions/` have a local type template (`definitions/types/definition.md`) even though the directory is the primary signal?
- How does this interact with the `type` field? Should definitions have `type: definition` as well as being in the directory, or is the directory sufficient?
