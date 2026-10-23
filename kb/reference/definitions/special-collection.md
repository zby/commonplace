---
description: "Definition — a special collection is one whose fixed name under kb/ Commonplace commands rely on for a system role: tags, sources, reports, work, types and agentic-system-analyses"
type: types/definition.md
tags: []
---

# Special collection

A **special collection** is a [collection](./collection.md) whose fixed name
directly under `kb/` Commonplace commands rely on to perform a system role.
Moving or renaming it breaks that role, because no configuration, alias or
discovery step tells the commands where else to look.

Every other collection is **ordinary**: commands treat it only through what
they are given, such as an explicit target path or collection name, and its
name grants it no privilege.

## Current special collections

| Collection | Role the commands rely on |
|---|---|
| [`tags`](../../tags/COLLECTION.md) | The KB's single tag namespace: tag heads, and the `participating:` list that says which collections' `tags:` lines count. Required in every KB, even when empty. |
| [`sources`](../../sources/COLLECTION.md) | Tracked source ingests and their local snapshots; source recognition, snapshot handling and grounding checks read this location. |
| [`reports`](../../reports/COLLECTION.md) | Fixed output and state locations: commands write `cache/` and `state/` here (including the review store), and the site leaves both out. |
| [`work`](../../work/COLLECTION.md) | The workshop layer: validation allows collection-local types from other collections here, and lifecycle checks scan it. |
| [`types`](../../types/COLLECTION.md) | The global type layer: a `type:` value such as `types/note.md` resolves into it on the library search path. |
| [`agentic-system-analyses`](../../agentic-system-analyses/COLLECTION.md) | The analysis workflow's fixed roots: runs are written under `state/`, and current and archived analyses are read from `retained/` and `retained-archive/`. |

The collection contract states each collection's role in its own words. The
[collection-contract type](../../types/collection-contract.md) does not declare
roles: special status lives in the commands, and this list records it.

## What the term excludes

- **Scaffolded collections.** `notes`, `reference` and `instructions` are
  seeded by `commonplace-init` and shipped in the library, but commands no
  longer rely on their names; operations take an explicit scope. Their names
  are defaults, not roles.
- **Site layout.** The menu's handling of `agent-memory-systems` or
  `agentic-systems` is this site's presentation choice, not a system role.
- **Fixed directories that are not collections.** `kb/messages/` and
  `kb/tasks/` have fixed locations but no `COLLECTION.md`.
- **Path rules inside an ordinary collection**, such as the proposal archive
  under `kb/reference/proposals/archive/`. They belong to that collection's
  contract and the code that reads them.

## Misuse

- Treating a special collection as a default input to generic operations.
  Being special names one role; it does not make the collection's artifacts
  tag members, evidence or validation targets.
- Inferring special status from a collection's name or contract. A collection
  becomes special only when a command starts relying on its location, and
  that change should add it here.
- Relocating a special collection with the relocation commands alone. Its
  role moves only with a code change.

---

Relevant Notes:

- [Collection](./collection.md) — defined-in: the boundary and contract every special collection also has
- [Collections and types](../collections-and-types.md) — see-also: how collection and type contracts compose, and the operational details of the special collections
