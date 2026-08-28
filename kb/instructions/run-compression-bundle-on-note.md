---
description: Produce a disposable edit-strategy report for one note using the unanchored compression criteria and high-impact synthesis
type: kb/types/instruction.md
---

# Run the compression bundle on one note

Review a specific note against the compression criteria without using the review database.

This is deliberately separate from the snapshot-anchored assay pipeline in `kb/instructions/run-review-batches.md`. Its files retain `gate_id` and “compression gate” as local historical names, but they are unanchored edit-strategy criteria, not review-system gates: they never enter `--all-gates`, acquire a persisted result kind, or write freshness-baseline state. Use them when the goal is a disposable report rather than fresh review evidence.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- optional second argument: `{output-path}` — repository-relative Markdown path for the sub-agent's report. If omitted, write it next to the target note as `<note-name>-compression-bundle-review.md`.

## Compression criteria

Use these criterion files, in this order:

1. `kb/instructions/compression-bundle/core-claim-obscured.md`
2. `kb/instructions/compression-bundle/branch-bloat.md`
3. `kb/instructions/compression-bundle/detail-overhang.md`
4. `kb/instructions/compression-bundle/marginal-value-redundancy.md`

After the four criteria, apply `kb/instructions/compression-bundle/high-impact-simplification-synthesis.md` to the artifact and the combined findings. This synthesis has no independent verdict; it selects the few structural changes most worth authorial attention.

Do not route these criteria through selectors or review jobs. Do not write review DB state or invoke acknowledgement or ingestion commands.

## Dispatch

The parent reads the target once immediately before dispatch and reads the four
criteria plus the synthesis instruction. It launches one fresh reviewer with a
complete packet containing:

- the target path as identity and the captured full note text as the sole
  authoritative assessed bytes; the reviewer does not reopen the live path;
- the four criteria in the required order, preserving each `gate_id`, name,
  failure mode, test, and examples, followed by the synthesis instruction;
- `{output-path}` and the output contract below; and
- the boundary that the target artifact, rather than ambient conversation or
  topic familiarity, supplies its intended contribution.

The reviewer independently applies every criterion, synthesizes the combined
findings, and writes only `{output-path}`. It does not edit the note, write
review-database state, or delegate. It chooses its analytic route within those
bounds.

The parent verifies that the report exists and satisfies the output contract,
then closes, terminates, or releases the single-use reviewer. If a fresh worker
cannot be launched, stop rather than reuse a context that may share the
author's framing.

## Output Contract

The sub-agent report should be plain Markdown:

```markdown
# Compression Bundle Review: <note title>

**Target:** `<note-path>`
**Bundle:** `kb/instructions/compression-bundle/`

## Overall Result

PASS|INFO|WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS|INFO|WARN | ... |
| compression/branch-bloat | PASS|INFO|WARN | ... |
| compression/detail-overhang | PASS|INFO|WARN | ... |
| compression/marginal-value-redundancy | PASS|INFO|WARN | ... |

## Findings

### compression/<gate-id>

- WARN|INFO: <specific location and action>

## High-impact Simplification Opportunities

### 1. <short opportunity name>

- Location: <heading and smallest useful quotation or section range>
- Reader problem: <why this materially obscures the claim, structure, or flow>
- Direction: <possible compression, fold, deletion, or reorganization>
- Combines: <relevant compression findings, or “cross-cutting”>
- Preserve or decide: <meanings, implications, or structural choices that constrain the revision>
```

Omit per-gate finding sections when a gate has no findings beyond a concise PASS summary. Do not emit PASS-per-paragraph output. Report zero to three high-impact opportunities; write `None` when no opportunity clears the synthesis threshold.

`PASS`, `INFO`, and `WARN` here are local report labels. They are not review-system decisions, and the report has no `REPORT` completion marker because it is not finalized into the review store.

## Reviewer Bias

The compression bundle is intentionally edit-strategy oriented. It should flag true, coherent, and locally defensible material when the material does not earn its current context cost. Prefer compression, folding, deletion, demotion to open question, or rehoming over additive repair unless extra wording is necessary to preserve the core claim.

The final synthesis is selective rather than exhaustive. It may combine several findings into one larger revision, but it must leave semantic or evidential choices unresolved instead of hiding them inside a cleaner rewrite.

## Do Not

- Do not mutate the target note.
- Do not create or finalize review jobs for these criteria.
- Do not write review DB state.
- Do not skip any gate in the bundle.
