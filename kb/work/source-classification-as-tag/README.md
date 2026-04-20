# Workshop: source-classification-as-tag

## Question

Collapse source-snapshot classification `type:` values into a single `type: snapshot` with the content family carried as a free-form tag in `tags:`.

The known classification values are:

- Snapshot-origin families currently present in source snapshots: `academic-paper`, `blog-post`, `documentation`, `encyclopedia-article`, `github-repo`, `practitioner-report`, `web-page`, `x-article`, `x-post`, `x-thread`.
- Ingest-report analytical families currently leaking into `.ingest.md` `type:` fields: `scientific-paper`, `conceptual-essay`, `design-proposal`, `tool-announcement`, `practitioner-report`, `conversation-thread`.
- Producer-only families emitted by tools or skill instructions but not necessarily present in current snapshot files: `github-issue`, `forum-thread`, `news-article`.

The migration target differs by artifact role:

- Source snapshots become `type: snapshot` and gain a content-family tag.
- Ingest reports become `type: ingest-report`; their analytical classification lives in `source_type:`.
- Existing generated or raw-text exceptions are handled explicitly in the inventory before rewriting.

## Why this workshop exists

The source-snapshot classification values have no sidecar files in `kb/sources/types/` — they are string stamps placed by the snapshot and ingest flows, not type contracts with templates or instructions. Treating them as first-class types would require inventing stubs that do not describe authoring (these artifacts are not authored) or meaningfully distinct shape (they share `source`, `captured`, `capture`, plus a few optional per-kind fields). The honest encoding is one snapshot type, one schema, content family as a tag.

This workshop supersedes the earlier source-classification branch of the path-valued-type migration plan. The path migration should only handle real type contracts after this cleanup lands.

## Decisions

- **Unified type name:** `snapshot`. Accurately describes the artifact — the file under `kb/sources/` is a captured copy; `source` is the upstream original the file points at.
- **No dedicated classification field.** Content family goes in existing `tags:`. Free-form.
- **No controlled vocabulary.** Tags are not enum-validated. New families do not need schema edits.
- **No conditional schemas.** Fields that exist only on some kinds (`status_id`, `conversation_id`, `post_count`) become plain optional fields on the snapshot schema.
- **No shape differences beyond optional fields.** Every snapshot validates against one schema.
- **Ingest reports keep analytical classification.** `source_type:` remains the field for the ingest report's interpretation of the source. It may use values that are not snapshot-origin families.
- **JSON sidecars mirror snapshot family metadata only where useful.** X/Twitter JSON sidecars should stop using `"type"` for the family if that would conflict with markdown `type: snapshot`; prefer `"family"` or `"tags"` there.
- **Generated indexes rely on tags.** Discovery of "all academic-paper snapshots" happens through tag-based surfaces, not by grepping `type:`.

## Snapshot schema (proposed shape)

Required frontmatter:

- `source` — canonical URL of the original
- `captured` — ISO date or datetime of capture
- `capture` — capture mechanism (`web-fetch`, `xdk`, `pdf-read`, ...)
- `type` — literal `snapshot` (rewritten to the path-valued form by the later path-valued-type migration)

Optional frontmatter:

- `description` — one-line gloss
- `tags` — free-form list; content family lives here
- `status_id`, `conversation_id`, `post_count` — x-platform metadata when applicable
- `api_url` — GitHub API URL when applicable
- any other per-kind metadata currently in use

## Migration steps

Each step has a pre-action review gate: prepare the candidate list and show the exact replacement before acting.

1. **Create `kb/sources/types/snapshot.instructions.md` + `snapshot.schema.yaml`.** Minimal instructions doc stating the type is stamped by snapshot tooling and not authored directly, plus the unified schema. No template is needed unless direct human authoring becomes a real workflow.
2. **Inventory source collection artifacts.** Save the inventory as a workshop artifact before rewriting. Separate at least these buckets:
   - source snapshots: direct child `kb/sources/*.md`, excluding `README.md`, `dir-index.md`, `*.ingest.md`, and `*.report-*.md`
   - ingest reports: `kb/sources/*.ingest.md`
   - generated report artifacts: `kb/sources/*.report-*.md`
   - raw or malformed exceptions: files without frontmatter, files with missing `type:`, and explicit `type: text`
   - JSON sidecars: `kb/sources/*.json`
3. **Review the exact replacement table.** For each affected value, show: file count, artifact bucket, old field, new field, and whether tags already exist.
4. **Normalize ingest reports first.** For every `.ingest.md` report whose `type:` is an analytical classification, rewrite `type:` to `ingest-report` and move or preserve the old value as `source_type:`. If `source_type:` already exists, preserve it and only fix `type:`.
5. **Batch rewrite source snapshot frontmatter.** For each source snapshot, rewrite `type: <family>` to `type: snapshot`, and prepend `<family>` to `tags:` while preserving existing tags. Missing-type or explicit-text snapshots must get an explicit family decision in the pre-action review before rewriting.
6. **Update snapshot producers.**
   - `cp-skill-snapshot-web`: stamp `type: snapshot` and put the selected family in `tags:`.
   - `commonplace-x-snapshot`: stamp markdown as `type: snapshot`, add `tags: [x-post|x-thread|x-article]`, and update the JSON sidecar field from `"type"` to `"family"` or equivalent.
   - `commonplace-github-snapshot`: stamp markdown as `type: snapshot`, add a GitHub family tag such as `github-issue` or `github-pr`.
   - `cp-skill-ingest`: keep report `type: ingest-report`; write analytical classification to `source_type:`.
7. **Confirm generated tag/index coverage.** Do not add a source-specific display rule; family discovery should come from the existing tag surfaces after snapshots carry family tags.
8. **Sweep remaining type-role references.** Grep the repo for classification values. Rewrite references only where the value is still being treated as a frontmatter `type:`. Keep or clarify references where the value is a tag, `source_type:`, prose classification label, or historical example.
9. **Regenerate indexes.** Run the index refresh path that rebuilds `kb/sources/dir-index.md` after the generator/display behavior is settled.
10. **Validate.** `uv run pytest` and the KB validator pass under the enum-typed scheme that still governs non-source real types. Path-valued types are out of scope for this bundle.

## Relation to other work

- Path-valued type migration — this workshop is a prerequisite so the path migration does not need classification stub type docs.
- `cp-skill-snapshot-web` and `cp-skill-ingest` — consumers of the classification logic; updated in step 6.

## Not changing

- `ingest-report` and `source-review` are real authoring/skill-structured types with existing sidecars. Their type contracts stay intact; this workshop only normalizes ingest-report frontmatter where analytical classifications have leaked into `type:`.
- `capture:` mechanism field — orthogonal axis (how it was captured, not what it is). Stays as-is.
- Non-source classification (`connect-report`, authoring types, etc.) — outside this workshop.

## Open questions

- Tag-index generation tooling. Does it extend `kb/notes/tags-index.md` machinery to `kb/sources/`, or live as its own generator? Follow-up, not a blocker for this workshop.
- What tag should GitHub pull-request snapshots use if/when supported: `github-pr`, `github-issue`, or a shared `github-thread` family?
- How should explicit `type: text` and missing-type snapshot exceptions be classified? The inventory gate must decide file by file.

## Closure

This workshop closes when:

- Every source snapshot has `type: snapshot` and a content-family tag.
- Every ingest report has `type: ingest-report`; analytical classification, where present, lives in `source_type:`.
- Snapshot producers stamp the new shape.
- Generated source indexes remain useful after `type:` stops carrying source family.
- No source-family or ingest analytical classification value appears as a frontmatter `type:` anywhere in the corpus, except in historical prose or explicit migration documentation.
- The path-valued type migration is unblocked from needing source-classification stub type docs.
