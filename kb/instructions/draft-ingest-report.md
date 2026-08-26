---
description: Use in a fresh worker context after snapshotting and connection discovery to write or repair one ingest report from an explicit snapshot and connect report.
type: kb/types/instruction.md
---

# Draft an ingest report

Use this instruction only as the delegated drafting stage of source ingest. The
caller has already resolved the target, captured the source, guarded its
checksum, and run connection discovery. You own the analysis and the one output
report. The caller owns orchestration, final handoff checks, and user reporting.

Do not invoke `cp-skill-ingest`, `cp-skill-connect`,
`cp-skill-snapshot-web`, or another orchestration skill. Do not spawn another
agent.

## Inputs

Require the caller to supply these values in the task:

- `mode`: `create` or `repair`
- `snapshot_path`: one Markdown source snapshot
- `connect_report_path`: its completed, non-empty connect report
- `output_path`: the `.ingest.md` report to write
- `snapshot_sha256`: the expected lowercase SHA-256 of the exact snapshot bytes
- `retained_quotes`: the complete Quotes section to place in the report
- `code_grounding_context`: `none` or the prepared paper-with-code context
- `validation_failures`: `none` in `create` mode; a non-empty list of exact
  failures in `repair` mode

For a fresh output, the caller supplies this exact `retained_quotes` value:

```markdown
## Quotes

No source quotes have been retained yet.
```

For a same-checksum refresh, the caller supplies the incumbent Quotes block
unchanged. In both cases, treat the supplied block as opaque retained text.

Stop without writing if a required value or input file is missing, unreadable,
inconsistent, or invalid for the selected mode. In `create` mode, do not read
or reuse an existing `output_path`; replace it only after the checksum check
passes. In `repair` mode, read any existing output only after the authoritative
inputs below. Use the supplied failures as a repair target, then check the
whole artifact rather than assuming the listed failures are exhaustive.

The snapshot and connect report are the complete source and discovery inputs.
Do not browse the web, rerun connection discovery, or run broad KB searches.
You may open a durable local artifact explicitly named in the connect report
only when needed to verify a connection you may keep. Never follow or cite a
local snapshot link in the durable report.

## Procedure

1. Read these authoritative files in order:
   1. `kb/sources/COLLECTION.md`
   2. `kb/sources/types/ingest-report.md`
   3. `snapshot_path`
   4. `connect_report_path`

   The ingest-report type spec wins if it conflicts with this instruction, but
   it never authorizes changing `retained_quotes`. If the report cannot satisfy
   both, stop and return that conflict.

2. Compute SHA-256 from the exact bytes of `snapshot_path`. Require it to equal
   `snapshot_sha256` before analysis. Do not hash a companion PDF, JSON, image,
   or extracted text file.

   In `repair` mode, read the existing `output_path` only after this check. If
   it does not exist, draft it from the authoritative inputs. Treat an existing
   draft as a repair candidate, not as source evidence.

   `retained_quotes` is authoritative retained text, not an analysis input. Do
   not derive it from the snapshot, connect report, or repair candidate.

3. Analyze the source under the ingest-report contract and the installed KB's
   goals and local collection contracts. In the Commonplace source repository,
   "our" means agent-operated KB methodology. In another installed KB, it
   means that project's declared system, work, codebase, policy, product, or
   domain. Derive capture metadata from the snapshot frontmatter. Do not copy
   snapshot `type`, `description`, `genre`, or `tags`.

   Preserve snapshot `capture_scope` when present. Treat `abstract`, `excerpt`,
   and `partial-source` as analysis boundaries; never present one as a full
   reading of the source.

   From the connect report, select settled connections, relationship roles,
   synthesis opportunities, and tensions. Do not transcribe its candidate
   inventory. Treat `Maintenance Observations` as non-actionable context. Write
   `Connections Found` as compact prose naming the source's role, such as
   anchor, technical basis, counterpoint, legal disposition, public statement,
   or limitation. If no casebook notes yet exist for the target collection,
   say so plainly instead of mapping relationships among already captured
   sources or speculating about future note links. Drop weak, duplicate, and
   speculative connections. One relationship bearing on the source's likely
   role is sufficient. Never cite, link to, or name the generated connect report
   in the ingest.

4. For an experiment-bearing source—an intervention, benchmark, ablation,
   controlled study, or other empirical evaluation used as design
   evidence—read the fixed-decomposition note linked under `Relevant Notes`.
   Identify:

   - the signals and histories available to condition behavior;
   - the responses or operations the learner could compose;
   - the mappings its hypothesis class could express; and
   - the representations, partitions, and design choices fixed outside its
     effective update space.

   Separate improvement inside that space from evidence for the fixed
   decomposition. Attribute an ablation only to the choice it varies. Carry any
   material consequence into `Connections Found`, `Extractable Value`, or
   `Limitations (our opinion)`.

5. Write `output_path` under the ingest-report contract:

   - classify the source and identify the author signal;
   - summarize it in one decision-oriented paragraph;
   - state its compact role in the current KB;
   - list three to seven goal-relative, connection-relative value items, each
     with an effort tag;
   - state genre-appropriate limitations as our opinion; and
   - recommend exactly one specific advisory next action.

   Keep an irrelevant source's report short. Explain the mismatch and recommend
   source-only filing or no promotion when appropriate.

   Put the snapshot's retained `source`, `captured`, `capture`, optional
   `capture_scope`, and flat adapter fields in frontmatter along with
   `snapshot_sha256`. Set `genre` from the closer reading. Do not create a
   `capture_metadata` field. Do not write the removed `source_snapshot` or
   `code_revisions` fields. Do not link to `.snapshots/` or cite a machine-local
   checkout such as `related-systems/`.

   Place `retained_quotes` immediately before `## Connections Found`, verbatim.
   Preserve every character, line ending, blank line, heading, and entry in the
   supplied block. Do not interpret, normalize, merge, re-indent, or rewrite it,
   and do not write another Quotes section. In `repair` mode, replace any Quotes
   block in the repair candidate with the supplied value rather than using the
   candidate's version.

   Do not describe whether quotes are retained outside `retained_quotes`.
   Retention state changes when grounding appends to that block. Use `(snapshot
   required)` only for a named claim that needs broader source context than the
   retained extracts supply, never merely because the Quotes block was empty at
   draft time.

   When `code_grounding_context` is `none`, omit `secondary_sources` and the
   `Code Grounding` section. Otherwise apply its pinned commit URLs, claim
   classifications, source citations, and evidence boundaries. State what code
   was executed. Do not turn static inspection into a reproduction claim.

6. Recompute the snapshot checksum after writing and require it still to equal
   `snapshot_sha256`. Run:

   ```bash
   commonplace-validate {output_path}
   ```

   Fix only `output_path` and rerun validation until it passes cleanly. Confirm
   that every `Extractable Value` item has an effort tag and that
   `Recommended Next Action` contains one action. Recheck that the Quotes block
   is byte-for-byte equal to `retained_quotes` and immediately precedes
   `## Connections Found`. If validation cannot pass without changing that
   block, return the failure without changing it. Do not edit the snapshot,
   connect report, a connected artifact, an index, a collection file, or any
   other library artifact.

7. Return only the validation result and the report's single recommended next
   action. Do not return a second analysis or an alternative draft in
   conversation.

---

Relevant Notes:

- [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — rests-on: experiment ingests must separate learning inside an effective update space from evidence for design choices fixed outside it
