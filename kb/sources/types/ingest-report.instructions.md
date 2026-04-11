# Ingest-Report Instructions

Use `ingest-report` for source ingestion analysis. An ingest report records how one source snapshot fits the KB; it is an analysis artifact, not the source itself.

## Metadata

- Set `source_snapshot` to the source snapshot filename or repo-root path.
- Set `source_type` to the classification of the source being ingested.
- Use `type: ingest-report` for the artifact type.
- Use `domains` for two to four topic tags that make the report searchable.
- Use file-relative Markdown links in the report body.

## Source Type

Choose one `source_type`:

- `scientific-paper` for peer-reviewed papers or preprints with methodology, data, or citations.
- `practitioner-report` for reports from someone who built something and describes what worked or failed.
- `conceptual-essay` for framings, analogies, or theoretical positions.
- `design-proposal` for RFCs, API designs, or architecture proposals for a specific system.
- `tool-announcement` for new tool, library, or framework releases.
- `github-issue` for bug reports, feature requests, or PRs from a specific repo.
- `conversation-thread` for discussion without a single authorial thesis.

## Sections

- `Classification` identifies the source type, domain tags, and author signal.
- `Summary` is one paragraph for someone deciding whether to read the full source.
- `Connections Found` summarizes the companion connect report and explains how the source fits the current KB.
- `Extractable Value` lists three to seven items, ordered by reach and novelty relative to existing KB connections.
- `Limitations (our opinion)` states where the source should not be trusted or over-generalized.
- `Recommended Next Action` chooses one specific next action.

## Extraction Standards

- Base extractable value on what is new relative to the connect report.
- Mark extractable value items with effort tags: `[quick-win]`, `[experiment]`, `[deep-dive]`, or `[just-a-reference]`.
- Assess reach: high-reach findings explain why something works beyond the source's local context; context-bound observations should be flagged.
- Before writing limitations, ask what is surprising, what simpler account could explain the result, and whether the central claim is hard to vary.
- Be specific in the recommended action: name the note to update, the note to write, the brainstorming question, or why the source should only be filed as a reference.
