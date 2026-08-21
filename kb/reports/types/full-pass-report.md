---
type: kb/types/type-spec.md
name: full-pass-report
description: Stateful report for one full-improvement pass and any asynchronous disposition resolution
schema: kb/reports/types/full-pass-report.schema.yaml
---

# Full-pass report

## Authoring Instructions

Use `full-pass-report` only for the packet produced by `kb/instructions/run-full-improvement-pass-on-note.md`. The report is authoritative for the pass's disposition and resolution. Its packet-owned `.txt` captures are immutable; resolving the report changes only its resolution fields and the canonical `Resolution` section.

`source` is the historical repository-relative logical path read at pass start. It identifies the artifact copied to `source_capture` and hashed by `source_sha256`; set all three once and never realign `source` after a rename, rehome, merge, or delete. The packet's `<note-name>` directory, frontmatter description, H1, and displayed Target likewise retain the pass-start path or title. Do not retrofit retained packets when the live artifact moves.

The guard compares the capture with the artifact at historical `source` and does not resolve redirects, so `missing` is the expected result after a rename. A later pass may resolve `source` through the validated flat redirect map in `properdocs.yml` to discover this packet as history for the live note; that lookup does not mutate the packet or change the guard target.

`merge_target` is also a repository-relative logical path. Capture fields are normalized packet-relative `.txt` paths and must resolve to regular non-symlink files inside the report's packet directory. Never substitute a capture path for a logical path when invoking an assessment method.

A `merge` disposition requires all merge-target fields. Other dispositions set them to null. A `keep` report begins `resolution: not-required`; `delete` and `merge` reports begin `pending`. Any of them may become `superseded` when its pre-transition live-version guard finds changed text. Only explicit user authority may accept, reject, or apply an alternative. A missing input or corrupted capture requires reconciliation and does not change resolution automatically.

Render the `Resolution` section exactly from the structured fields. Quote a terminal ISO-8601 `resolved_at` value in YAML so it remains a string rather than becoming a YAML timestamp object. Null values and an empty `resulting_paths` list render as an em dash. Non-empty resulting paths render as comma-separated code spans.

## Template

```markdown
---
description: "Full improvement pass over <pass-start source title>"
type: kb/reports/types/full-pass-report.md
source: kb/notes/example.md
source_capture: source.txt
source_sha256: <lowercase SHA-256>
pass_id: <unique pass ID>
disposition: keep
merge_target: null
merge_target_capture: null
merge_target_title: null
merge_target_sha256: null
resolution: not-required
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
---

# Full Improvement Pass: <pass-start source title>

<packet body>

## Resolution

**Status:** not-required
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
```
