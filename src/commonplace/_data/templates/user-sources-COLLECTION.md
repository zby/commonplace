# Writing conventions for kb/sources/

<!--
This is your project's sources collection. Once installed, this contract
belongs to your project; Commonplace does not synchronize it with later
changes to this template. Adapt the generic rules below when the project
needs a narrower source policy.
-->

## Purpose and scope

This collection contains tracked analyses and durable records of external
sources. Tracked ingest reports are collection content. Local captures under
the ignored `.snapshots/` directory are immutable inputs, not collection
artifacts or durable link targets.

## Quality goal

Preserve faithful source identity and capture provenance while keeping what
the source says separate from project-relative analysis.

## Titles, descriptions, and files

- Name an ingest report `<snapshot-slug>.ingest.md`.
- Use the external source's title as the document title.
- Write a retrieval-oriented description that says what the source establishes
  and why it matters to this project.
- Treat every capture under `.snapshots/` as immutable. Create a new capture
  when the observed source changes, and update the tracked record's provenance
  rather than editing the old capture.
- Never author a durable link into `.snapshots/`.

## Outbound links

Use links only when they help a reader understand or apply the source analysis.
Inline links carry load-bearing relationships. Footer links use a label plus a
context phrase that states why the reader should follow the link.

| label | destinations | reader need |
|---|---|---|
| `derived-from` | external | reach the external source from which this analysis was produced |
| `is-evidence-for` | notes, reference | inspect the local claim or decision on which this source bears |
| `compares-with` | notes, reference, sources | compare artifacts on a named shared axis |
| `see-also` | notes, reference, sources, external | inspect a useful adjacent artifact when no stronger relation applies |

The destination collection's contract decides whether it may author a
reciprocal link.

## Type eligibility

A typed artifact in this collection may use a local type spec under
`kb/sources/types/` or a shared type spec under `kb/types/`. Its `type:` value
is the path to that contract. Frontmatter-free Markdown is implicit `text` only
for deliberate unstructured source work. Captures under `.snapshots/` may use
the local snapshot contract even though they are not collection content.
