---
description: Use in a fresh worker context after snapshotting and connection discovery to write or repair one ingest report from an explicit snapshot and connect report.
type: types/instruction.md
---

# Draft an ingest report

Write a faithful, reusable account of what the source contributes to the
installed KB and what its evidence supports.

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
- `occasion`: `none` or the caller's question or job that brought the source
  in, stated before the source was read
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
Read a conditional instruction linked below when its trigger applies, and any
note that instruction requires. You may also open a durable local
artifact explicitly named in the connect report only when needed to verify a
connection you may keep. Never follow or cite a local snapshot link in the
durable report.

## Procedure

1. Read these authoritative files in order:
   1. `kb/sources/COLLECTION.md`
   2. the global [`ingest-report`](../types/ingest-report.md) type spec
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
   domain. The loaded type owns metadata, section contents, and occasion
   semantics. Derive capture metadata from the snapshot frontmatter and use
   the connect report as candidate discovery input. Treat its `Maintenance
   Observations` as non-actionable context. One settled connection is sufficient.

   For scientific papers, use your pretrained knowledge of the NeurIPS
   reviewing methodology as a coherent framework for the experimental
   `Contribution assessment (our opinion)`, adapted to the paper's contribution
   type. Interpret it through Commonplace's Popperian approach: assess progress
   on the problem through conjectures, criticism, comparison with rivals, and
   tests of their consequences. Credit explanations, error elimination, and
   evidence or tools that enable stronger tests; surviving criticism leaves
   claims open to revision. Use the learned methodology to inform the short
   paragraph, with the ingest contract governing its scope and uncertainty.

   Choose analytical emphasis from the source. Continue analysis only when you
   can name an unresolved question and explain how answering it could materially
   change the interpretation, evidential scope, useful contribution, or
   recommended next action. Apply this stopping rule after satisfying the
   required report sections and evidence checks.

4. For an experiment-bearing source—an intervention, benchmark, ablation,
   controlled study, or other empirical evaluation used as design
   evidence—identify the tested comparison and consequential representations,
   component boundaries, interfaces, or other design choices held fixed.
   Distinguish improvement within that decomposition from evidence comparing
   alternative decompositions. Attribute an ablation only to the choice it
   varies. Carry material consequences into `Connections Found`,
   `Extractable Value`, or
   `Limitations (our opinion)`.

   When a result materially depends on the tested decomposition, keep that
   qualification beside the result in `Summary`, `Connections Found`, and
   `Extractable Value` wherever it appears. Name only architectural details
   needed to understand the comparison or bound its reuse; an exhaustive
   decomposition or architectural taxonomy is not required.

5. If the source's subject or mechanism is learning or adaptation, including
   a conceptual account with no empirical results, read and apply
   [Assess learning claims during ingest](./assess-learning-claims-during-ingest.md).
   Otherwise skip this step and omit the `Learning Claims (our opinion)`
   section.

6. Write only `output_path` under the ingest-report contract. Do not create a
   `capture_metadata` field or cite a machine-local checkout such as
   `related-systems/`.

   Place `retained_quotes` immediately before `## Connections Found`, verbatim.
   Preserve every character, line ending, blank line, heading, and entry in the
   supplied block. Do not interpret, normalize, merge, re-indent, or rewrite it,
   and do not write another Quotes section. In `repair` mode, replace any Quotes
   block in the repair candidate with the supplied value rather than using the
   candidate's version.

   When `code_grounding_context` is `none`, omit `secondary_sources` and the
   `Code Grounding` section. Otherwise apply its pinned commit URLs, claim
   classifications, source citations, and evidence boundaries. State what code
   was executed. Do not turn static inspection into a reproduction claim.

7. Recompute the snapshot checksum after writing and require it still to equal
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

8. Return only the validation result and the report's single recommended next
   action. Do not return a second analysis or an alternative draft in
   conversation.

---

Relevant Notes:

- [Weight-resident methodologies provide context-efficient behavioral compression](../notes/weight-resident-methodologies-compress-behavior-in-context.md) — rests-on: the NeurIPS cue selects a learned methodology without restating its detailed rules
- [Theory builder](../notes/definitions/theory-builder.md) — rests-on: the Popperian interpretation connects problems, conjectures, criticism, and revision
