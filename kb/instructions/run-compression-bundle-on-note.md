---
description: 'Review one note against the compression gates (edit-strategy: compress, fold, delete, rehome) without writing review-DB state.'
type: kb/types/instruction.md
---

# Run the compression bundle on one note

Review a specific note against the compression gates without using the review database.

This is a deliberately separate, no-DB analogue of `kb/instructions/run-review-batches.md`: the compression gates live at `kb/instructions/compression-bundle/` rather than under the production `kb/instructions/review-gates/` catalog, so they never get swept into `--all-gates` or write review-DB acceptance state. Use it when the goal is a disposable edit-strategy report, not accepted review state.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- optional second argument: `{output-path}` — repository-relative Markdown path for the sub-agent's report. If omitted, write it next to the target note as `<note-name>-compression-bundle-review.md`.

## Gate bundle

Use these gate files, in this order:

1. `kb/instructions/compression-bundle/core-claim-obscured.md`
2. `kb/instructions/compression-bundle/branch-bloat.md`
3. `kb/instructions/compression-bundle/detail-overhang.md`
4. `kb/instructions/compression-bundle/marginal-value-redundancy.md`

Do not resolve gates through `commonplace-create-review-run`. Do not use selectors, review runs, review DB writes, acknowledgement commands, or ingestion commands.

## Procedure

1. Read the target note.
2. Read the four gate files above.
3. Concatenate the gate definitions into a reviewer packet. Preserve each gate's `gate_id`, name, failure mode, test, and examples.
4. Start a fresh sub-agent and give it:
   - the target note path and full note text;
   - the concatenated gate packet;
   - the output contract below.
5. Ask the sub-agent to review the note against every gate independently. It should not edit the note.
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

## Reviewer Bias

The compression bundle is intentionally edit-strategy oriented. It should flag true, coherent, and locally defensible material when the material does not earn its current context cost. Prefer compression, folding, deletion, demotion to open question, or rehoming over additive repair unless extra wording is necessary to preserve the core claim.

## Do Not

- Do not mutate the target note.
- Do not run `commonplace-create-review-run`.
- Do not run `commonplace-ingest-bundle-output`.
- Do not write review DB state.
- Do not skip any gate in the bundle.
