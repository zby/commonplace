# Plan: Installed Collection Routing

## Problem

Installed Commonplace projects currently put shipped library content under `kb/commonplace/`, with collection-shaped children such as `kb/commonplace/notes/` and `kb/commonplace/reference/`. That shape is awkward for agents because it requires them to know that the parent is not a collection while the grandchildren are.

A registry in `AGENTS.md` would make one harness easier, but startup files vary across agents (`CLAUDE.md`, `AGENTS.md`, and others). Making a startup file the structural source of truth would add synchronization and portability problems.

## Fundamental Requirements

- Agents must find relevant KB material with minimal reasoning.
- Python tooling and agents must agree on what a collection is.
- The installed KB must be understandable by inspection.
- User-authored content and shipped Commonplace content must not be confused.
- Users should not be encouraged to edit shipped Commonplace library content.
- Installed reference docs must document Commonplace well.
- Installed skills/instructions must be operational from the installed project.
- Collection contracts should stay close to the artifacts they govern.
- Cross-links inside shipped content should keep working after installation.
- The design should work across agent harnesses without depending on one startup-file convention.
- The ongoing operating model should be simpler than the install process.

## Candidate Direction

Prefer a filesystem convention over a registry:

- a collection is a direct child of `kb/` containing `COLLECTION.md`;
- for `kb/foo/`, the collection contract is `kb/foo/COLLECTION.md`;
- Python and agents use the same rule;
- startup-file routing is optional frontloading, not required for correctness.

This points toward installed shipped collections as top-level, visibly library-owned directories, possibly using names such as:

```text
kb/cmpl-reference/
kb/cmpl-instructions/
kb/cmpl-notes/
```

This is not yet a final decision. The unresolved part is how source layout, installed layout, and link rewriting should relate.

## Design Alternatives

1. **Keep source layout, rewrite on install.** Source stays `kb/notes`, `kb/reference`, `kb/instructions`; installer copies them to `kb/cmpl-*` and rewrites links.
2. **Rename source collections to installed names.** Source uses `kb/cmpl-notes`, `kb/cmpl-reference`, `kb/cmpl-instructions`; installer mostly copies verbatim.
3. **Hybrid.** Move only some shipped surfaces, such as product reference docs, to `cmpl-*` source paths while rewriting or copying others.
4. **Do not install shipped notes by default.** Install only product docs and operational skills; make them self-contained or promote only the needed subset of notes.

## Questions To Audit

- How many links from `kb/reference/` and `kb/instructions/` point into `kb/notes/`?
- How many cross-links exist among `kb/notes/`, `kb/reference/`, and `kb/instructions/`?
- Which links are operational dependencies versus explanatory references?
- Which non-link path surfaces would need rewriting: frontmatter type paths, prose paths, generated indexes, skill instructions?
- Is `cmpl-*` the right prefix, or should installed library collections use a clearer name?
- Should `kb/agent-memory-systems/` remain uninstalled by default?
- Should canonical routing live in installed `kb/README.md`, with agent startup files left for later frontloading?

## Next Step

Run a link and path-surface audit before choosing an implementation. The audit should estimate the cost of each alternative, especially the cost of installer rewriting versus source collection renaming.

