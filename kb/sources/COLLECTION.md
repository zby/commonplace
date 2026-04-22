# Writing conventions for kb/sources/ (descriptive register)

## Register and fidelity

Descriptive [register](../notes/definitions/register.md): captured external sources (papers, articles, GitHub issues, tweets, READMEs) and their ingest analyses. Sources are stamped, not authored — the quality goal is **faithful capture** plus **clear ingest analysis**.

Two roles, two shapes — don't blur capture and analysis in the same file:

- **Snapshots** preserve source content as captured. Don't edit, summarise, or annotate them. Trim only what the capture tool grabbed by accident (navigation chrome, ad markup) and note the trim in capture metadata.
- **Ingest reports** classify the source, summarise load-bearing claims, and propose connections into the rest of the KB. They live next to the snapshot as `<name>.ingest.md`.

## Title and description conventions

**Snapshots** — derive from the source: article slug, repo + issue number, paper title slug. Capture tooling normally sets this; manual snapshots follow the same pattern.

**Ingest reports and source reviews** — same basename as the snapshot for ingest reports (with `.ingest.md` suffix). For source reviews, use a slug for the source title or central claim.

**Description** (in ingest reports and source reviews) — name what the source says and where it lands, not just the source title.

## How to add a source

```bash
# URL → snapshot + ingest in one go
cp-skill-ingest https://example.com/some-article

# Or snapshot first, ingest later
cp-skill-snapshot-web https://example.com/some-article
cp-skill-ingest kb/sources/some-article.md
```

The ingest skill picks the snapshot backend by URL (GitHub API for issues/PRs, X SDK for tweets, WebFetch for everything else).

## Outbound links

**Snapshots are immutable.** Don't add, edit, or annotate after capture — whatever links the original content carried stay as captured, and we never author new ones into a snapshot. Running connect on a snapshot still works (connect never mutates its target) and is useful: the report's authoring signal is reverse-edge — which library notes (typically in `kb/notes/`) should add `evidence` or `derived-from` links pointing at this snapshot.

**Ingest reports and source reviews** carry the active outbound surface — the analysis cites where the source lands in the rest of the KB. Inline for strongest commitment, with a connective word that fits (e.g. `as in [title](path)`); footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and other sources for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported) or `kb/instructions/` (executing readers don't follow source links).

**Labels (apply to ingest reports and source reviews; the snapshot itself is never the link author):**

| label | destinations | reader-need |
|---|---|---|
| `evidence` | notes | this source corroborates the claim |
| `derived-from` | notes | this claim was abstracted from this source |
| `rationale` | notes | this design or rule rests on this claim |
| `compares-with` | sources, agent-memory | this source covers a similar/parallel system |
| `defined-in` | notes/definitions | reader may not know the term |
| `see-also` | any | adjacent companion; use sparingly |

## Types

| type | file | use for |
|---|---|---|
| `snapshot` | `kb/sources/types/snapshot.md` | verbatim external source captures |
| `ingest-report` | `kb/sources/types/ingest-report.md` | analysis of how a snapshot fits the KB |
| `source-review` | `kb/sources/types/source-review.md` | structured extraction + relevance review |
| `text` (implicit) | no frontmatter | raw captures awaiting classification |

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Descriptions of the commonplace system → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- External agent-memory system reviews → `kb/agent-memory-systems/`
- Work-in-progress on a source → `kb/work/`
- Generated reports → `kb/reports/`
