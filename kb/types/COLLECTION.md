# Writing conventions for kb/types/

## Purpose and quality goal

This collection is Commonplace's global type surface. Its artifacts are system-definition contracts used across collections: they describe artifact shape, declare schemas, and supply authoring and review instructions for each global type.

Quality goal is **self-contained checkability + economy**. A type spec must tell authors, readers, validators, and type-conformance reviewers what an instance asserts without requiring collection-specific reinterpretation. Keep global contracts small enough to load wherever the type is used; collection-specific structure belongs in a collection-local type instead.

`kb/types/` remains the global type layer. Making it a collection supplies the authoring and outbound-link contract required of artifacts authored here; it does not make type semantics collection-relative.

## Title and body conventions

- Name a type spec after the type it defines.
- Follow the `type-spec` contract in [`type-spec.md`](./type-spec.md); its schema and body own structural and semantic type requirements.
- Do not place collection-local types here. Put them under `kb/<collection>/types/` and list them in that collection's `COLLECTION.md`.

## Outbound links

Author each outbound link from the reader need at its source. Inline links may supply definitions or shipped-system context; footer links carry an authorized label and context phrase.

- **→ `kb/notes/`** — search when a theoretical claim explains why a global type contract has its shape, or when a defined term is needed to interpret it. Labels: `rests-on`, `defined-in`, `see-also`.
- **→ `kb/reference/`** — search when an accepted decision or shipped subsystem determines how a global type contract operates. Labels: `depends-on`, `evidenced-by`, `see-also`.

Do not link to external sources or into `kb/work/`, `kb/sources/`, `kb/agent-memory-systems/`, or `kb/agentic-systems/` from global type specs. Put supporting evidence or unfinished design work in the appropriate collection and link to the promoted result.

## Types

Every authored Markdown artifact in this collection is a type spec and carries `type: kb/types/type-spec.md`. The root [`type-spec.md`](./type-spec.md) is self-referential. Schema files are symbolic sidecars, not Markdown artifacts.

## What does not belong here

- Collection-local type contracts → that collection's `types/` directory
- Shipped architecture and decisions → `kb/reference/`
- Transferable theory → `kb/notes/`
- Procedures not defining a type's content contract → `kb/instructions/`
- Work in progress → `kb/work/`
