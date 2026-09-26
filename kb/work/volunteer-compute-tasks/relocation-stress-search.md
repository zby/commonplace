# Relocation stress search

Find consequential relocation defects through extensive generated testing, then
return small examples that the maintainer can verify directly. This task
protects the KB's links and files during moves. Follow the setup, ownership, and
submission rules in the [shared handoff](./README.md).

## Inputs and baseline

Read the [command contracts](../../reference/commands.md#commonplace-relocate-note),
[implementation](../../../src/commonplace/lib/relocation.py), and existing
[note](../../../tests/commonplace/cli/test_relocate_note.py) and
[directory](../../../tests/commonplace/cli/test_relocate_directory.py) tests.

```bash
python -m pytest tests/commonplace/cli/test_relocate_note.py tests/commonplace/cli/test_relocate_directory.py
```

## Search commission

Build temporary KB graphs with identifiable artifact contents. Generate legal
note moves, renames, directory moves, and sequences mixing them. Explore
interactions among inbound, outbound, self, and sibling links; anchors; nested
directories; code examples; declared frontmatter references; and redirects.
Prioritize multi-step failures that ordinary example tests are unlikely to hit.

Check these properties where the baseline contract supports the input:

- Each supported reference still resolves to the same logical artifact after
  a successful move, with its anchor preserved. Merely resolving to some file
  is insufficient.
- Files outside the move retain their contents except for required reference
  and configuration updates; code examples and unrelated prose stay intact.
- Dry runs do not modify the project. Rejected operations do not clobber an
  existing destination or lose source contents.
- Declared frontmatter references and redirects preserve their documented
  meaning through repeated moves.

Give artifacts stable identities in the generator. Compute expected graph
changes independently; calling the production link-rewriter to calculate the
expected result would conceal its errors. Do not assume byte-identical output
after a move-and-return: equivalent link spelling may change.

Use generated or exhaustive small graphs and shrink failing graphs and move
sequences. Search volume is a means, not an acceptance score. Record graph sizes,
sequence lengths, supported syntax, seeds, and stopping budget. Keep unsupported
Markdown features separate from failures within documented behavior.

## Acceptance

Return a minimal fixture and deterministic pytest case for each defect. For
link failures, show the original artifact identity and the actual target after
each relevant move. For mutation or data-loss failures, show the small file
tree and byte differences. Confirm the failure through the public command or
its normal entry path, not only an internal helper given impossible inputs.

The valuable output is a new, reachable preservation failure with a reusable
regression test. A large fuzzing framework, coverage increase, or an unshrunk
random failure alone does not satisfy the task. Fixes may be separate follow-up
patches; a relocation architecture rewrite is outside this commission.
