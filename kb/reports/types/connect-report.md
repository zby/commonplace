---
type: kb/types/type-spec.md
name: connect-report
description: Discovery report for possible KB connections from one source artifact
schema: kb/reports/types/connect-report.schema.yaml
---

# Connect report

## Authoring Instructions

Use `connect-report` for discovery-only connection work. **Every connection section describes candidate edges for a future writer to act on, not edges already encoded anywhere.** The connect skill never edits the source artifact or any other library artifact — the report is the entire deliverable and the only direct write. Readers of the report should treat its contents as suggestions to evaluate, not as state already in the KB.

A connect report records evidence for future KB authoring; it is not itself a durable knowledge claim.

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

- Every item in `Connections Found` must pass the articulation test: `[source] connects to [target] because [specific reason].`
- Pick relationship labels from the **authorised set declared in the source collection's `COLLECTION.md`** for the source→destination pair. Each authorised label carries a reader-need; use the label whose reader-need matches the connection's purpose. Do not propose labels outside the authorised set.
- If a candidate passes the articulation test but no authorised label fits, route it to `Off-authorisation Candidates` — do not invent a label or downgrade to `see-also` to make it fit.
- Reject candidates that are merely "related", keyword-only matches, too obvious to help traversal, or likely to confuse an agent following the link.
- Keep a candidate only if an agent, or another intended KB consumer named by the collection contract, gains something concrete by following the link.
- If a target artifact has `status: seedling` or `status: speculative`, flag load-bearing labels such as `grounds`, `mechanism`, or `derived-from`. Additive labels such as `extends`, `exemplifies`, and `enables` are fine.

## Sections

All sections list **candidates** — recommended edges, not committed ones. Whoever consumes the report decides which to author and where.

- Put candidate outbound edges from the source under `Connections Found`. For an authored source, these are recommendations for a future edit of the source. For an immutable source (e.g. a snapshot under `kb/sources/`), these are recommendations for whichever artifact carries the source's authored surface (typically the matching `.ingest.md`).
- Put return links worth adding from the target side under `Bidirectional Candidates`.
- Put notes in **other** collections that should link **to** this source — under their own `COLLECTION.md` rules — under `Reverse-edge Candidates`. Especially load-bearing when the source is immutable or has narrow outbound (snapshots, system reviews).
- Put candidates that pass the articulation test but have no authorised label for the source→destination pair under `Off-authorisation Candidates`. Each entry should suggest either extending the destination's authorised set in `COLLECTION.md` or rejecting as off-scope.
- Put candidate targets without frontmatter under `Raw Text Candidates`, not under `Connections Found`.
- Include weak matches in `Rejected Candidates` when they explain why obvious search hits were not kept.
- Use `Index Membership` for indexes where the source might belong (a future writer would add the entry; connect does not).
- Use `Synthesis Opportunities` only for higher-order claims implied by multiple notes; do not create the synthesis note during connect.
- Use `Flags` for split candidates, unresolved tensions, no-connections findings, or other follow-up work.
- Use `Maintenance Observations` for report-local observations discovered during traversal that are not connection candidates.
- If a section has no content, write `None` rather than deleting the section.

## Maintenance Observations

Use this section only for durable issues or follow-up signals:

- stale or broken links
- clear contradictions
- duplicated or redundant artifacts
- competing ownership between artifacts
- repeated unnamed mechanisms or abstractions
- collection-contract gaps, such as useful candidates with no authorised label
- synthesis opportunities durable enough for later promotion

Do not include routine candidate links, ordinary topical overlap, weak associations, or anything already captured in the connection sections.

Downstream connection consumers may ignore this section. A later explicit maintenance or triage step may promote entries from this section into `kb/log.md`, notes, reference docs, instructions, ADRs, collection rules, or other local artifacts.

## Edge Cases

- If no genuine connections are found, report that honestly and include which indexes and searches were checked.
- If a source connects to five or more notes across three or more topic areas and makes more than one independent assertion, flag it as a split candidate.
- If two candidates conflict, flag the tension without resolving it.
- If traversal reveals unconnected notes, flag them but do not treat them as part of the current connect result.

## Quality Gates

- Verify every candidate path exists before including it as a connection.
- Remove any connection that cannot complete the sentence: "[A] connects to [B] because [specific reason]."
- Do not propose regular note connections to raw text files; route them to `Raw Text Candidates`.
- Do not create synthesis notes, edit indexes, mutate library artifacts, or write side files from a connect report.

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

**Description listing scan:**
- Scoped `rg` listing over {destination} -- flagged candidates: {candidates with reasons}

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

## Reverse-edge Candidates

- [other-source](../../notes/other-source.md) → source -- **evidence**: {note that should author a link TO this target under its own COLLECTION.md rules}

## Off-authorisation Candidates

- [target](../../reference/target.md) -- {reason the candidate connects + which authorised set it falls outside, with a suggestion to extend or reject}

## Raw Text Candidates

- [text-file](../../notes/text-file.md) -- potential **extends**: {reason this text is relevant}

## Rejected Candidates

- [rejected](../../notes/rejected.md) -- {reason rejected}

## Index Membership

- [index-name](../../notes/index-name.md) -- {what the source would contribute to this area}

## Synthesis Opportunities

{Two or more notes that together imply a higher-order claim not yet captured, or "None"}

## Maintenance Observations

{Report-local traversal observations that are not connection candidates, or "None"}

## Flags

- {split candidates, tensions, no-connections finding, or "None"}
```
