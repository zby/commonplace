# KB Routing

This `kb/` tree is organized by filesystem contracts.

A directory under `kb/` is a collection when it contains a local `COLLECTION.md`.
Subdirectories inside a collection are normally areas. A `COLLECTION.md` inside
a non-collection namespace is an ordinary collection; a `COLLECTION.md` inside
another collection is invalid and reported by validation.

In this source repository, common collection roots include:

- `kb/notes/`
- `kb/reference/`
- `kb/instructions/`
- `kb/agent-memory-systems/`
- `kb/agentic-systems/`
- `kb/sources/`
- `kb/work/`

In installed projects, shipped Commonplace library content may live under
`kb/commonplace/<collection>/`. The `kb/commonplace/` directory is a namespace,
not a collection, unless it carries its own `COLLECTION.md`; its descendant
`COLLECTION.md`-bearing directories are the collections.

Use collection-local `COLLECTION.md` files for writing conventions, type
offerings, and outbound-linking rules. Use `kb/types/` for global type specs;
`kb/types/` is a framework type surface, not a collection.
