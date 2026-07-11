---
description: Produce a disposable edit-strategy report for one note using the unanchored compression criteria
type: kb/types/instruction.md
---

# Run the compression bundle on one note

Review a specific note against the compression criteria without using the review database.

This is deliberately separate from the snapshot-anchored assay pipeline in `kb/instructions/run-review-batches.md`. Its files retain `gate_id` and “compression gate” as local historical names, but they are unanchored edit-strategy criteria, not review-system gates: they never enter `--all-gates`, acquire a persisted result kind, or write acceptance state. Use them when the goal is a disposable report rather than fresh review evidence.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- optional second argument: `{output-path}` — repository-relative Markdown path for the sub-agent's report. If omitted, write it next to the target note as `<note-name>-compression-bundle-review.md`.

## Compression criteria

Use these criterion files, in this order:

1. `kb/instructions/compression-bundle/core-claim-obscured.md`
2. `kb/instructions/compression-bundle/branch-bloat.md`
3. `kb/instructions/compression-bundle/detail-overhang.md`
4. `kb/instructions/compression-bundle/marginal-value-redundancy.md`

Do not route these criteria through selectors or review jobs. Do not write review DB state or invoke acknowledgement or ingestion commands.

## Procedure

1. Read the target note.
2. Read the four criterion files above.
3. Concatenate the criterion definitions into a reviewer packet. Preserve each file's `gate_id`, name, failure mode, test, and examples; `gate_id` is part of this bundle's report vocabulary, not a persisted review identity.
4. Start a fresh sub-agent and give it:
   - the target note path and full note text;
   - the concatenated gate packet;
   - the output contract below.
5. Ask the sub-agent to apply every criterion independently. It should not edit the note.
6. Save the returned Markdown report to `{output-path}`.

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

## Suggested Revision

<short edit plan that preserves the strongest claim while reducing context cost>
```

Omit per-gate finding sections when a gate has no findings beyond a concise PASS summary. Do not emit PASS-per-paragraph output.

`PASS`, `INFO`, and `WARN` here are local report labels. They are not review-system decisions, and the report has no `REPORT` completion marker because it is not finalized into the review store.

## Reviewer Bias

The compression bundle is intentionally edit-strategy oriented. It should flag true, coherent, and locally defensible material when the material does not earn its current context cost. Prefer compression, folding, deletion, demotion to open question, or rehoming over additive repair unless extra wording is necessary to preserve the core claim.

## Do Not

- Do not mutate the target note.
- Do not create or finalize review jobs for these criteria.
- Do not write review DB state.
- Do not skip any gate in the bundle.
