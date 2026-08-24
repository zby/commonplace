# Writing conventions for kb/sources/

## Text contract and fidelity

This collection contains tracked analyses of external sources plus local
reading copies. The quality goal is **faithful
capture** plus **clear ingest analysis**.

Two roles, two shapes — don't blur capture and analysis in the same file:

- **Snapshots** under the ignored `kb/sources/.snapshots/` directory preserve
  source content as captured. Don't edit, summarise, or annotate them. Trim
  only what the capture tool grabbed by accident and note the trim in capture
  metadata. They are local materializations, not tracked authority.
- **Ingest reports** under `kb/sources/` own durable source identity, capture
  provenance, genre, the exact primary-snapshot checksum, and the analysis.
  They are named `<name>.ingest.md`.

## Title and description conventions

**Snapshots** — derive from the source: article slug, repo + issue number, paper
title slug. Capture tooling normally sets this; manual snapshots follow the
same pattern. The name is a convenience, not identity.

**Ingest reports and source reviews** — use the primary snapshot's basename for
ingest reports, with `.ingest.md` replacing `.md`. For source reviews, use a
slug for the source title or central claim.

**Description** (in ingest reports and source reviews) — name what the source says and where it lands, not just the source title.

## How to add a source

```bash
# URL → local snapshot + tracked ingest in one go
cp-skill-ingest https://example.com/some-article

# Or snapshot first, ingest later
cp-skill-snapshot-web https://example.com/some-article
cp-skill-ingest kb/sources/.snapshots/some-article.md
```

The ingest skill picks the snapshot backend by URL: GitHub API for issues and
pull requests, the X SDK for posts, Poppler for PDFs, and Trafilatura for
ordinary web pages.

## Local cache validation

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

## Claims in ingest reports

Every ingest report has exactly one `## Claims` section immediately before
`## Connections Found`. Claims retain bounded source-side propositions and
their primary-source support. This lets a tracked ingest support later checks
when its local snapshot is unavailable. Keep target-specific transfer reasoning
in the artifact that uses the claim, not in the ingest.

The empty section is exactly:

```markdown
## Claims

No claims have been grounded yet.
```

A populated entry has this shape:

```markdown
- **Claim (paraphrase):** <bounded source-side proposition>
  - **Source extract (verbatim):** <exact supporting content>
  - **Source location:** <human-resolvable locator for that extract>
  - **Scope:** <population, conditions, and exclusions>
  - **Confidence:** <scoped prose>
  - **Limitation:** <boundary needed to prevent overstatement>
```

Use one or more adjacent `Source extract (verbatim)` / `Source location` pairs.
Repeat both fields when support is non-contiguous. Scope, confidence, and
limitation apply to the complete entry.

## Outbound links

**Snapshots are immutable local inputs.** Don't add, edit, or annotate after
capture: changing any byte changes the checksum. Never author a durable link to
`.snapshots/`. A citation of what the source says points to the external
`source` URL; a citation of Commonplace's analysis points to the ingest.

**Ingest reports and source reviews** carry the active outbound surface — the analysis cites where the source lands in the rest of the KB. Inline for strongest commitment, with a connective word that fits (e.g. `as in [title](path)`); footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and other sources for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported) or `kb/instructions/` (executing readers don't follow source links).

**Labels (apply to ingest reports and source reviews; the snapshot itself is never the link author):**

| label | destinations | reader-need |
|---|---|---|
| `derived-from` | external | this ingest analysis or source review is worked out from the original external source already in hand |
| `is-evidence-for` | notes, agent-memory | this source bears materially on the target claim or analysis, without asserting that the target has incorporated it |
| `abstracted-from` | notes | this claim was abstracted from this source |
| `rests-on` | notes | this source-side design or rule depends on this theoretical claim |
| `compares-with` | notes, sources, agent-memory, agentic-systems | compare this source or analysis with a target on a named shared axis |
| `defined-in` | notes/definitions | reader may not know the term |
| `see-also` | notes, reference, sources, agent-memory, agentic-systems, external | adjacent companion; use sparingly |

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. A raw capture awaiting classification may remain frontmatter-free as implicit `text`; once classified, it follows the selected type contract.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Descriptions of the commonplace system → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- External agent-memory system reviews → `kb/agent-memory-systems/`
- External agentic-system and harness analyses → `kb/agentic-systems/`
- Work-in-progress on a source → `kb/work/`
- Generated reports → `kb/reports/`
