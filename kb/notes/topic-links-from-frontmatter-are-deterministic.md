---
description: The areas-to-Topics mapping is mechanical — now implemented as scripts/sync_topic_links.py
type: note
traits: []
areas: [links]
status: outdated
---

# Topic links from frontmatter are deterministic

**Implemented.** See [ADR-001: Generate Topic links from frontmatter](../adr/001-generate-topic-links-from-frontmatter.md).

The `areas:` frontmatter field lists which indexes a note belongs to. The Topics footer section contains markdown links to those same indexes. The mapping is mechanical: read `areas`, write links. This was a concrete stabilization candidate — now automated via `scripts/sync_topic_links.py`.

See [storing LLM outputs is stabilization](../../notes/storing-llm-outputs-is-stabilization.md) for the general pattern.

Topics:
- [links](./links.md)
