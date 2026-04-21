---
type: kb/types/type-spec.md
name: connect-report
description: Discovery report for possible KB connections from one source artifact
schema: kb/reports/types/connect-report.schema.yaml
---

# Connect report

## Authoring Instructions

Use `connect-report` for discovery-only connection work. A connect report records evidence for future KB mutations; it is not itself a durable knowledge claim.

## Metadata

- Set `source` to the repo-root target artifact path, for example `kb/sources/source-name.md`.
- Set `source_has_frontmatter` to `true` when the source starts with YAML frontmatter and `false` for raw `text` files.
- Use `depth: quick`, `standard`, or `deep` to match the discovery pass that was actually run.
- Use file-relative Markdown links in the report body.

## Discovery Trace

- Capture actual query strings, scores when available, and the evaluated or rejected candidates in `Discovery Trace`.
- The trace must say which indexes were read, which searches were run, which candidates were followed, and why candidates were kept or rejected.
- A trace that only lists keywords without query strings, scores when available, or candidate evaluations is insufficient.

## Connection Standards

- Every item in `Connections Found` must pass the articulation test: you can say specifically why the source connects to the target.
- Use relationship labels only when the reason is explicit:
  - `extends` when the source adds a dimension to the target.
  - `grounds` when the source provides a foundation for the target.
  - `contradicts` when the source creates a real tension with the target.
  - `exemplifies` when the source is a concrete instance of the target.
  - `synthesizes` when the source combines multiple insights.
  - `enables` when the source makes the target actionable.
- Reject candidates that are merely "related", keyword-only matches, too obvious to help traversal, or likely to confuse an agent following the link.
- Ask what an agent gains by following the link. Keep links that provide reasoning foundation, implementation pattern, trade-off awareness, or a concrete example.
- If a target note has `status: seedling` or `status: speculative`, flag load-bearing relationships such as `grounds`, `foundation`, or `synthesizes`. Additive relationships such as `extends`, `exemplifies`, and `enables` are fine.

## Sections

- Put reverse links that are also worth adding under `Bidirectional Candidates`.
- Put candidates without frontmatter under `Raw Text Candidates`, not under `Connections Found`.
- Include weak matches in `Rejected Candidates` when they explain why obvious search hits were not kept.
- Use `Index Membership` for indexes where the source might belong, even if no direct note-to-note link should be added.
- Use `Synthesis Opportunities` only for higher-order claims implied by multiple notes; do not create the synthesis note during connect.
- Use `Flags` for split candidates, unresolved tensions, no-connections findings, or other follow-up work.
- If a section has no content, write `None` rather than deleting the section.

## Edge Cases

- If no genuine connections are found, report that honestly and include which indexes and searches were checked.
- If a source connects to five or more notes across three or more topic areas and makes more than one independent assertion, flag it as a split candidate.
- If two candidates conflict, flag the tension without resolving it.
- If traversal reveals unconnected notes, flag them but do not treat them as part of the current connect result.

## Quality Gates

- Verify every candidate path exists before including it as a connection.
- Remove any connection that cannot complete the sentence: "[A] connects to [B] because [specific reason]."
- Do not propose regular note connections to raw text files; route them to `Raw Text Candidates`.
- Do not create synthesis notes, edit indexes, or mutate library notes from a connect report.

## Template

```markdown
---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "{repo-root source path}"
source_has_frontmatter: {true|false}
date: "{YYYY-MM-DD}"
depth: standard
---

# Connection Report: {source title}

**Source:** [{source title}]({relative source link})

## Discovery Trace

**Index scan:**
- Read [notes index](../../notes/dir-index.md) -- flagged candidates: {candidates with reasons}

**Topic indexes:**
- {topic index reads and candidates, or "None"}

**Body search:**
- rg "{actual query}" -- {results and evaluation}

**Link following:**
- {candidate neighborhoods traversed and what they revealed}

## Connections Found

- [target](../../notes/target.md) -- **extends**: {specific reason why this connection exists}

## Bidirectional Candidates

- [target](../../notes/target.md) <-> source -- **contradicts**: {reason the return path is also useful}

## Raw Text Candidates

- [text-file](../../notes/text-file.md) -- potential **extends**: {reason this text is relevant}

## Rejected Candidates

- [rejected](../../notes/rejected.md) -- {reason rejected}

## Index Membership

- [index-name](../../notes/index-name.md) -- {what the source would contribute to this area}

## Synthesis Opportunities

{Two or more notes that together imply a higher-order claim not yet captured, or "None"}

## Flags

- {split candidates, tensions, no-connections finding, or "None"}
```
