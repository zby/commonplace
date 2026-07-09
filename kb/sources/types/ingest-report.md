---
type: kb/types/type-spec.md
name: ingest-report
description: Analysis artifact recording how a source snapshot fits the KB
schema: kb/sources/types/ingest-report.schema.yaml
---

# Ingest report

## Authoring Instructions

Use `ingest-report` for source ingestion analysis. An ingest report records how one source snapshot fits the KB; it is an analysis artifact, not the source itself.

Assess fit relative to the installed KB's goals, local collection contracts, and current connection context. Interpret "our theory", "our stack", "our codebase", and "our practices" through those local goals and contracts.

## Metadata

- Set `source_snapshot` to the source snapshot filename or repo-root path.
- Set `source_type` to the classification of the source being ingested.
- Use `type: kb/sources/types/ingest-report.md` for the artifact type.
- Use `domains` for two to four topic tags that make the report searchable.
- Use file-relative Markdown links in the report body for durable KB artifacts and source snapshots. Do not link to generated connect reports.

## Source Type

Choose one `source_type`:

- `scientific-paper` for peer-reviewed papers or preprints with methodology, data, or citations.
- `practitioner-report` for reports from someone who built something and describes what worked or failed.
- `conceptual-essay` for framings, analogies, or theoretical positions.
- `design-proposal` for RFCs, API designs, or architecture proposals for a specific system.
- `tool-announcement` for new tool, library, or framework releases.
- `github-issue` for bug reports, feature requests, or PRs from a specific repo.
- `conversation-thread` for discussion without a single authorial thesis.
- `code-repository` for a repository whose implementation, structure, documentation, or project history is the source.
- `court-opinion` for judicial rulings, orders, or opinions issued by a court.
- `news-article` for journalistic reporting on current events from a news outlet.
- `official-statement` for a statement, release, or announcement issued by an organization, agency, or public figure in an official capacity.

## Sections

- `Classification` identifies the source type, domain tags, and author signal.
- `Summary` is one paragraph for someone deciding whether to read the full source.
- `Connections Found` summarizes the connection discovery findings and explains how the source fits the current KB. The generated connect report is working context only; do not cite it, link to it, or name its path in the ingest report.
- `Extractable Value` lists three to seven items, ordered by reach and novelty relative to the installed KB's goals and existing KB connections.
- `Limitations (our opinion)` states where the source should not be trusted or over-generalized.
- `Recommended Next Action` chooses one specific advisory next action. The ingest report recommends; it does not perform promotion.

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

`Limitations (our opinion)` is editorial judgment — label it as opinion. Name what is missing, cite a relevant KB note when one exists, and state what the gap means for the source's conclusions. The lens depends on `source_type`:

- **Scientific papers** — what was not tested: missing or naive baselines, limited benchmarks, configurations the literature or this KB already discusses, claims that do not generalize beyond the tested setup.
- **Practitioner reports** — what is not visible: survivorship bias (what worked is reported, failed attempts are not), sample size of one, unacknowledged context such as team size, budget, or existing infrastructure.
- **Conceptual essays and conversation threads** — what is not argued: reasoning by analogy without testing whether the analogy holds, cherry-picked supporting examples, conflating naming something with explaining it, unfalsifiable framings.
- **Tool announcements and design proposals** — what is not shown: vendor bias and flattering benchmarks, missing failure modes or scaling limits, gaps between the announced design and real use.
- **GitHub issues and code repositories** — what is not durable: a single reporter's or author's view, point-in-time state that later commits may overturn, project history that records decisions without their later outcomes.
- **Court opinions** — what is not settled: interlocutory or preliminary rulings that later proceedings may overturn, jurisdiction-specific reasoning that may not generalize, procedural posture (for example, a motion to dismiss) that limits what the ruling actually decides.
- **News articles and official statements** — what is not independently verified: reliance on sources with their own interests, framing that reflects the outlet's or issuer's editorial stance, developing situations where later reporting may contradict early claims.

## Template

```markdown
---
description: "{one-line retrieval filter}"
source_snapshot: "{input filename}"
ingested: "{YYYY-MM-DD}"
type: kb/sources/types/ingest-report.md
source_type: {source type}
domains: [{tag1}, {tag2}, {tag3}]
---

# Ingest: {source title}

Source: {filename}
Captured: {date from frontmatter}
From: {source URL from frontmatter}

## Classification

Type: {source type} -- {brief justification}
Domains: {tag1}, {tag2}, {tag3}
Author: {credibility signal}

## Summary

{One paragraph}

## Connections Found

{Summary of connect discovery: which notes, what relationships, and what this source adds}

## Extractable Value

1. **{item}** -- {why it matters relative to existing KB connections}. [{effort}]

## Limitations (our opinion)

{Where this source should not be trusted or over-generalized}

## Recommended Next Action

{One specific action}
```
