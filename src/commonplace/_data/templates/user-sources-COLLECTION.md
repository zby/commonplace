# Writing conventions for kb/sources/

<!--
This is your project's sources collection. Once installed, this contract
belongs to your project; Commonplace does not synchronize it with later
changes to this template. Adapt the generic rules below when the project
needs a narrower source policy.
-->

## Purpose and scope

This collection contains tracked analyses and durable records of external
sources. Tracked ingest reports are collection content and own durable source
identity, an immutable snapshot checksum, and project-relative analysis. Local
captures under the ignored `.snapshots/` directory are immutable inputs, not
collection artifacts or durable link targets.

## Quality goal

Preserve faithful source identity and capture provenance while keeping what
the source says separate from project-relative analysis.

## Titles, descriptions, and files

- Name an ingest report `<snapshot-slug>.ingest.md`.
- Use the external source's title as the document title.
- Write a retrieval-oriented description that says what the source establishes
  and why it matters to this project.
- Treat every capture under `.snapshots/` as immutable. Create a new capture
  under a distinct basename when the observed source changes rather than
  editing the old capture.
- Never change an existing ingest's `snapshot_sha256`. Changed source bytes are
  a new observation with a distinct snapshot basename and ingest path.
- Never author a durable link into `.snapshots/`.

`commonplace-validate kb/sources` keeps hidden captures outside ordinary
artifact and schema validation, but it audits retained Markdown snapshots
against the tracked ingests. It indexes exact `source` URL values independently
of checksums, so a legacy checksum-less ingest or a changed observation is
reported as related rather than unrelated. A derived ingest can account for
exact precursor bytes with `original_snapshot_sha256`, as when an English
translation is the primary observation and the retained source-language capture
is its input. The sweep warns when an ingest's checksum locates its exact bytes
only under a
different filename, when an alternate file redundantly duplicates an already
valid pair, and when no ingest matches either the URL or checksum. A tracked
ingest whose ignored snapshot is simply absent does not warn.

## Quotes in ingest reports

Every ingest report has exactly one `## Quotes` section immediately before
`## Connections Found`. It retains only exact source wording and a
human-resolvable locator. Do not put paraphrases, scope judgments, confidence
assessments, limitations, or target-specific transfer reasoning in this
section.

The empty section is exactly:

```markdown
## Quotes

No source quotes have been retained yet.
```

A populated item has this shape:

```markdown
- **Source extract (verbatim):** <exact supporting content>
  - **Source location:** <human-resolvable locator for that extract>
```

Repeat the complete pair when support is non-contiguous. Quotes are
append-only: append new items without rewriting or deleting incumbent ones.

## Declaring source-checking requirements

A source-dependent claim links the tracked ingest, never the local snapshot.
An ordinary ingest link declares that its Quotes section is sufficient for
semantic checking. When checking requires the full observation, include the
exact marker `(snapshot required)` in the ingest link text. The semantic
grounding gate then derives and verifies the name-paired snapshot and fails if
it is unavailable or invalid. It never silently falls back from an unmarked
link to ambient snapshot state.

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
