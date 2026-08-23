# Minimal v1 implementation plan

The scope is fixed in [state.md](./state.md). This plan contains only work
required to ship it. Future extensions are not work packages here; the final
ADR records them under `Postponed`.

For recovery, set one phase `IN_PROGRESS` before editing. Record its active
write set and exact next action in `state.md`. A phase is complete only when its
checks and results are recorded there.

## P0 — Baseline and recovery

Completed on 2026-08-22.

Evidence:

- current tracked and worktree source counts recorded in `inventory.md`;
- affected contracts, code, tests, and links located;
- single recovery state and navigation entry created;
- no implementation files changed.

## P1 — Write the exact v1 shape

Completed on 2026-08-22.

Turn the accepted direction into two concrete examples, not another design
survey.

Create `v1-shape.md` with:

- an ordinary ingest's exact frontmatter before and after;
- a code-grounded ingest with several commit-pinned `implementation`
  secondaries;
- the exact mapping of capture metadata into the ingest and the
  primary-snapshot checksum definition;
- the local source-materialization directory and lookup rule;
- the body lines removed because the new fields contain the same information;
- explicit mappings for the two current irregular `source_snapshot` values.

Keep the current headings and analytical obligations. A sentence remains if it
interprets, justifies, qualifies, or applies a field, even when it repeats the
field's value while doing so.

Exit evidence:

- both examples are schema-ready and contain no placeholder choice;
- the ordinary example needs no empty secondary list;
- the code example supports more than one repository and only the
  `implementation` role;
- the user accepts the examples.

## P2 — Implement v1

Implement the accepted examples as one coherent system change.

Required surfaces:

- source collection contract, ingest and source-snapshot type specs, schemas,
  and the source, capture-metadata, genre, and checksum authority displaced
  from the snapshot;
- ordinary ingest, snapshot, paper-with-code, re-ingest, and directory guidance
  needed to expose only the accepted v1 input domain;
- GitHub and X capture commands, ordinary web/PDF snapshot instructions, local
  materialization lookup, duplicate detection, and canonical source URL
  extraction;
- ignore and publication rules;
- targeted schema, extraction, capture-command, type-contract, documentation,
  and scaffold tests.

Implementation rules:

- one durable representation for primary and secondary source identity;
- `snapshot_sha256` covers the exact primary Markdown snapshot bytes and never
  changes as a side effect of cache recreation;
- no compatibility copy of `source_snapshot` or `code_revisions` after the
  repository migration;
- no body-format redesign;
- no accepted secondary role other than `implementation`;
- no directory-primary workflow.

Exit evidence:

- ordinary and multi-repository examples validate;
- invalid roles, mutable implementation identifiers, and invalid cardinality
  fail clearly;
- local cache hit, miss/refetch, and unavailable-source behavior are tested;
- exact checksum matches, mismatches, and duplicate local copies are tested;
- targeted tests and validation pass.

## P3 — Migrate repository data

Create `migration.tsv` before bulk edits. It must contain one row per tracked
ingest, source snapshot or capture asset, and dependent library link, with a
terminal state and notes column.

For each ingest/source unit:

1. verify and write its durable primary, capture, and secondary fields;
2. compute `snapshot_sha256` from the unchanged primary Markdown snapshot and
   preserve that file at the adopted ignored local path;
3. remove only body lines that directly duplicate the new fields;
4. validate the migrated ingest;
5. replace durable-library links to the retiring snapshot with the external
   source, ingest, or another target that supports the original sentence;
6. stop tracking the source body and capture assets only after the row's prior
   steps are complete.

The two irregular current pointers get explicit rows and one-off dispositions;
they do not add a directory input mode.

Exit evidence:

- a fresh scan has exact set parity with `migration.tsv`;
- every row is terminal;
- every tracked ingest validates under v1;
- sampled diffs show no unrelated body rewriting;
- no retiring source file remains the target of a durable library link;
- regenerated local material stays ignored.
- no checksum changed merely because its source file moved.

## P4 — Verify, record the ADR, and close

Run:

- relevant collection validation;
- `uv run pytest`;
- `uv run ruff check .`, recording repository-wide baseline findings honestly,
  plus a scoped check proving the redesign introduced no remaining finding;
- package, scaffold, and documentation publication checks;
- one fresh-checkout reconstruction test with source material absent, covering
  both an exact reconstruction and a changed-source checksum mismatch.

Write one ADR that records the implemented source authority, local
materialization, ingest fields, implementation-secondary semantics, and corpus
migration. Put every considered but unimplemented extension only in its
`Postponed` section; do not create a workshop backlog.

Then archive or dispose of the proposal according to the proposal lifecycle,
remove this workshop and its navigation entry, and commit only the exact
workshop change set.

Exit evidence:

- all checks and their results are recorded in `state.md`;
- the ADR and shipped contracts agree;
- no non-terminal migration row remains;
- no durable behavior depends on this workshop.
