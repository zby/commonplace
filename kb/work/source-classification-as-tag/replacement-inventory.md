# Source Classification Replacement Inventory

Captured: 2026-04-19

## Summary

- source snapshots: 80
- ingest reports: 80
- generated report artifacts: 2
- JSON sidecars: 16

## Replacement Table

| Artifact bucket | Count | Old field/value | New field/value | Existing tags? | Action |
| --- | ---: | --- | --- | --- | --- |
| source snapshots | 36 | `type: academic-paper` | `type: snapshot`; prepend `tags: [academic-paper]` | no | Rewrite frontmatter. |
| source snapshots | 13 | `type: blog-post` | `type: snapshot`; prepend `tags: [blog-post]` | no | Rewrite frontmatter. |
| source snapshots | 1 | `type: documentation` | `type: snapshot`; prepend `tags: [documentation]` | no | Rewrite frontmatter. |
| source snapshots | 1 | `type: encyclopedia-article` | `type: snapshot`; prepend `tags: [encyclopedia-article]` | no | Rewrite frontmatter. |
| source snapshots | 3 | `type: github-repo` | `type: snapshot`; prepend `tags: [github-repo]` | no | Rewrite frontmatter. |
| source snapshots | 1 | `type: practitioner-report` | `type: snapshot`; prepend `tags: [practitioner-report]` | no | Rewrite frontmatter. |
| source snapshots | 4 | `type: web-page` | `type: snapshot`; prepend `tags: [web-page]` | no | Rewrite frontmatter. |
| source snapshots | 13 | `type: x-article` | `type: snapshot`; prepend `tags: [x-article]` | no | Rewrite frontmatter. |
| source snapshots | 4 | `type: x-post` | `type: snapshot`; prepend `tags: [x-post]` | no | Rewrite frontmatter. |
| source snapshots | 1 | `type: x-thread` | `type: snapshot`; prepend `tags: [x-thread]` | no | Rewrite frontmatter. |
| source snapshots | 2 | missing `type:` / no frontmatter | unchanged | n/a | Leave as text docs for this migration. |
| source snapshots | 1 | `type: text` | unchanged | no | Leave as text docs for this migration. |
| ingest reports | 18 | `type: conceptual-essay` | `type: ingest-report`; `source_type: conceptual-essay` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 4 | `type: conversation-thread` | `type: ingest-report`; `source_type: conversation-thread` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 2 | `type: design-proposal` | `type: ingest-report`; `source_type: design-proposal` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 17 | `type: practitioner-report` | `type: ingest-report`; `source_type: practitioner-report` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 31 | `type: scientific-paper` | `type: ingest-report`; `source_type: scientific-paper` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 4 | `type: tool-announcement` | `type: ingest-report`; `source_type: tool-announcement` | n/a | Move analytical classification to `source_type`. |
| ingest reports | 1 | `type: ingest-report` | preserve `source_type: conceptual-essay` | n/a | No type rewrite needed. |
| ingest reports | 3 | `type: ingest-report` | preserve `source_type: scientific-paper` | n/a | No type rewrite needed. |
| generated report artifacts | 2 | `type: note` | unchanged | n/a | Out of scope. |
| JSON sidecars | 12 | `"type": "x-article"` | `"family": "x-article"` | n/a | Rename sidecar family key. |
| JSON sidecars | 3 | `"type": "x-post"` | `"family": "x-post"` | n/a | Rename sidecar family key. |
| JSON sidecars | 1 | `"type": "x-thread"` | `"family": "x-thread"` | n/a | Rename sidecar family key. |

## Exceptions Left As Text Docs

- `kb/sources/letta-memgpt-stateful-agents.md` - no parseable frontmatter / missing `type:`; no replacement in this migration.
- `kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.md` - explicit `type: text`; no replacement in this migration.
- `kb/sources/voooooogel-multi-agent-future.md` - no parseable frontmatter / missing `type:`; no replacement in this migration.

## Notes

- No current source snapshot candidate has an existing `tags:` field, so source-family tag insertion is mechanically simple for the non-exception snapshot set.
- Ingest reports that already have `type: ingest-report` also already have `source_type:` and should be preserved.
- This table is a pre-action review artifact; it does not itself rewrite corpus files.
