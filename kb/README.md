# KB Routing

Browsing on GitHub? Start with the [rendered site](https://zby.github.io/commonplace/), the [site homepage](./index.md), the [consultation guide](./consult.md), or the [topic guides](./tags/README.md).

This `kb/` tree is organized by filesystem contracts.

A directory under `kb/` is a collection when it contains a local `COLLECTION.md`.
Subdirectories inside a collection are normally areas. A `COLLECTION.md` inside
a non-collection namespace is an ordinary collection; a `COLLECTION.md` inside
another collection is invalid and reported by validation.

In this source repository, common collection roots include:

- [`kb/theory/`](./theory/README.md)
- [`kb/notes/`](./notes/README.md)
- [`kb/reference/`](./reference/README.md)
- [`kb/instructions/`](./instructions/README.md)
- [`kb/tags/`](./tags/README.md)
- [`kb/agent-memory-systems/`](./agent-memory-systems/README.md)
- [`kb/agentic-systems/`](./agentic-systems/README.md)
- [`kb/agentic-system-analyses/`](./agentic-system-analyses/README.md)
- [`kb/sources/`](./sources/README.md)
- [`kb/articles/`](./articles/README.md)
- [`kb/types/`](./types/README.md)
- [`kb/work/`](./work/README.md)

In installed projects, shipped Commonplace library content may live under
`kb/commonplace/<collection>/`. The `kb/commonplace/` directory is a namespace,
not a collection, unless it carries its own `COLLECTION.md`; its descendant
`COLLECTION.md`-bearing directories are the collections.

Use collection-local `COLLECTION.md` files for writing conventions, type
offerings, and outbound-linking rules. `kb/types/` is both the global framework
type surface and a collection; its type specs keep their self-contained global
semantics while its `COLLECTION.md` governs local authoring and routing.
