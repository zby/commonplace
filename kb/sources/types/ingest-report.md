---
type: kb/types/type-spec.md
name: ingest-report
description: Durable source record and analysis of how one external source fits the KB
schema: kb/sources/types/ingest-report.schema.yaml
---

# Ingest report

## Authoring Instructions

Use `ingest-report` for source ingestion analysis. An ingest report is the
tracked, durable record of one URL-backed primary source and the KB analysis
derived from a local reading copy. It is not a copy of the source.

The primary reading copy lives under ignored `kb/sources/.snapshots/`. Its
path is local state and never appears in tracked frontmatter or links.

Assess fit relative to the installed KB's goals, local collection contracts, and current connection context. Interpret "our theory", "our stack", "our codebase", and "our practices" through those local goals and contracts.

## Metadata

- Keep the H1 title text, including the `Ingest:` prefix, to at most 100
  characters.
- Write `description` as a one-line retrieval filter between 50 and 250
  characters.
- Set `source` to the canonical external URL of the primary source.
- Set `captured` to the date or datetime of the observation used for the
  analysis, and `capture` to its capture mechanism.
- Set `genre` to the primary source's evidential genre.
- Set `snapshot_sha256` to the lowercase SHA-256 of the exact bytes of the
  primary Markdown snapshot. The hash includes frontmatter, line endings, and
  the presence or absence of a final newline. It excludes companion files.
- When the primary snapshot was mechanically derived from another retained
  snapshot, set `original_snapshot_sha256` to the lowercase SHA-256 of those
  exact precursor bytes. This gives the derivation input durable identity
  without treating a cache path as provenance or as a second primary source.
- Use `type: kb/sources/types/ingest-report.md` for the artifact type.
- Use `domains` for two to four topic tags that make the report searchable.
- Copy capture-adapter metadata such as `status_id`, `conversation_id`,
  `post_count`, and `api_url` under its existing flat field name. Do not copy a
  snapshot's `type`, `description`, `genre`, or `tags`; set ingest `genre` from
  the closer reading.
- For a code-grounded ingest, add one `secondary_sources` item for every
  inspected implementation repository. Each item has
  `role: implementation` and a GitHub commit URL containing the full
  40-character SHA. Do not record machine-local checkout paths.
- Do not use the removed `original_snapshot`, `source_snapshot`, or
  `code_revisions` path fields.
- Link to durable KB artifacts and external sources in the report body. Never
  link to the local `.snapshots/` cache or generated connect reports.

## Genre

The ingest's `genre` is the durable source classification. Use the vocabulary
and meanings in [snapshot.md](./snapshot.md). A local snapshot may contain a
capture-time genre, but it is not authoritative. Set or correct the ingest
field after reading the source. The vocabulary is open: an off-list value warns
rather than fails. V1 has no operative local extension path that adds a known
value and its Limitations lens to this fixed ingest type. A recurring off-list
genre therefore remains warned until an ingest-side vocabulary mechanism is
adopted; a collection-local snapshot type does not extend this contract.

## Sections

- `Classification` justifies the source genre and identifies the author signal.
- `Summary` is one paragraph for someone deciding whether to read the full source.
- `Code Grounding` is required when `secondary_sources` is present. Link the
  reviewed revisions and pinned source files; distinguish mechanisms confirmed
  by inspection, experiment support artifacts that were present but not run,
  and claims that remain paper-only. State what code, if any, was executed.
- `Claims` appears exactly once, immediately before `Connections Found`. It
  retains bounded source-side propositions with exact primary-source support so
  later readers can judge a use without relying on the local snapshot.
- `Connections Found` summarizes the connection discovery findings and explains how the source fits the current KB, as compact prose naming the source's role (for example: anchor, technical basis, counterpoint, legal disposition, public statement, limitation) rather than a transcribed candidate list. Drop weak, speculative, or duplicate edges; keep only settled, durable judgments. If no casebook notes exist yet, say so plainly instead of substituting a full map of relationships to other already-captured sources, or framing the section as prospective connections for notes that do not exist yet. The generated connect report is working context only; do not cite it, link to it, or name its path in the ingest report.
- `Extractable Value` lists three to seven items, ordered by reach and novelty relative to the installed KB's goals and existing KB connections.
- `Limitations (our opinion)` states where the source should not be trusted or over-generalized.
- `Recommended Next Action` chooses one specific advisory next action. The ingest report recommends; it does not perform promotion.

## Claims Shape

Use this exact section when no claims have been grounded:

```markdown
## Claims

No claims have been grounded yet.
```

Use this shape for every populated entry:

```markdown
- **Claim (paraphrase):** <bounded source-side proposition>
  - **Source extract (verbatim):** <exact supporting content>
  - **Source location:** <human-resolvable locator for that extract>
  - **Scope:** <population, conditions, and exclusions>
  - **Confidence:** <scoped prose>
  - **Limitation:** <boundary needed to prevent overstatement>
```

Normalize the claim as a source-side proposition. Do not put a target-specific
transfer argument in the entry. Use one or more adjacent `Source extract
(verbatim)` / `Source location` pairs, repeating both when support is
non-contiguous. Scope, confidence, and limitation bound the complete entry.

## Extraction Standards

- Base extractable value on what is new relative to the connection context discovered by connect.
- Favor value that changes, supports, limits, or operationalizes the installed KB's current claims, decisions, policies, practices, or local domain work.
- Useful value classes include evidence for an existing claim, contradiction or limitation affecting current KB content, reusable method or workflow, data point or empirical result, vocabulary or framing that improves retrieval and discussion, operational warning or failure mode, and candidate artifact to write, update, retire, or review.
- Mark extractable value items with effort tags: `[quick-win]`, `[experiment]`, `[deep-dive]`, or `[just-a-reference]`.
- Assess reach: high-reach findings explain why something works beyond the source's local context; context-bound observations should be flagged.
- Before writing limitations, ask what is surprising, what simpler account could explain the result, and whether the central claim is hard to vary.
- Be specific in the recommended action: name the note, reference document, runbook, instruction, policy, ADR, product requirement, dataset, incident note, or other local artifact to write, update, retire, or review. Filing as a source-only reference or scheduling a focused brainstorm are also valid when that is the right destination.
- Notes remain the default promotion target for transferable claims, but the recommended action may point to another local artifact type when collection contracts make that the better home.

## Limitations Standards

`Limitations (our opinion)` is editorial judgment — label it as opinion. Name what is missing, cite a relevant KB note when one exists, and state what the gap means for the source's conclusions. The lens depends on the ingest's `genre`:

- **Scientific papers** — what was not tested: missing or naive baselines, limited benchmarks, configurations the literature or this KB already discusses, claims that do not generalize beyond the tested setup.
  Released source can confirm that a mechanism is implemented or expose its
  configuration, but static inspection does not reproduce training, benchmark,
  throughput, or quality results. State the remaining outcome-evidence gap.
- **Practitioner reports** — what is not visible: survivorship bias (what worked is reported, failed attempts are not), sample size of one, unacknowledged context such as team size, budget, or existing infrastructure.
- **Conceptual essays and conversation threads** — what is not argued: reasoning by analogy without testing whether the analogy holds, cherry-picked supporting examples, conflating naming something with explaining it, unfalsifiable framings.
- **Tool announcements and design proposals** — what is not shown: vendor bias and flattering benchmarks, missing failure modes or scaling limits, gaps between the announced design and real use.
- **GitHub issues and code repositories** — what is not durable: a single reporter's or author's view, point-in-time state that later commits may overturn, project history that records decisions without their later outcomes.
- **Court opinions** — what is not settled: interlocutory or preliminary rulings that later proceedings may overturn, jurisdiction-specific reasoning that may not generalize, procedural posture (for example, a motion to dismiss) that limits what the ruling actually decides.
- **News articles and official statements** — what is not independently verified: reliance on sources with their own interests, framing that reflects the outlet's or issuer's editorial stance, developing situations where later reporting may contradict early claims.
- **Any other genre** (the vocabulary is open) — fall back to the generic questions: what is surprising, what simpler account could explain it, whether the central claim is hard to vary, and what interests the author has in the framing. When a new genre recurs, add a dedicated lens here alongside its vocabulary entry in [snapshot.md](./snapshot.md).

## Template

```markdown
---
description: "{one-line retrieval filter}"
source: {canonical external URL}
captured: "{date or datetime from snapshot frontmatter}"
capture: {capture mechanism from snapshot frontmatter}
genre: {source genre}
snapshot_sha256: {lowercase SHA-256 of the exact snapshot file bytes}
ingested: "{YYYY-MM-DD}"
type: kb/sources/types/ingest-report.md
domains: [{tag1}, {tag2}, {tag3}]
---

# Ingest: {source title}

## Classification

{Brief genre justification without repeating the field as a label.}
Author: {credibility signal}

## Summary

{One paragraph}

## Claims

No claims have been grounded yet.

## Connections Found

{Summary of connect discovery: which notes, what relationships, and what this source adds}

## Extractable Value

1. **{item}** -- {why it matters relative to existing KB connections}. [{effort}]

## Limitations (our opinion)

{Where this source should not be trusted or over-generalized}

## Recommended Next Action

{One specific action}
```

For a code-grounded paper ingest, add this frontmatter field:

```yaml
secondary_sources:
  - role: implementation
    source: https://github.com/{owner}/{repo}/commit/{40-character-sha}
```

Add this section after `Summary`:

```markdown
## Code Grounding

{Pinned repositories, claim-bearing source citations, inspection result, and execution status}
```
