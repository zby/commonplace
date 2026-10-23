# Theory rename execution

## Authority and checkpoint

The operator authorized implementation, allowed navigation repairs in
semantically frozen records, and waived review/freshness continuity. ADR 123
records the selected policy. The project scaffold keeps Notes.

Workshop decisions committed as `c30ebacfb`. The execution inventories use that
HEAD and the completed evidence split. The original inventory files remain
pre-sort evidence; the new `execution-*.tsv` files are the relocation worklists.

The fresh command dry run finds 427 payload files (425 Markdown, two schemas),
four fewer than the baseline: the evidence work moved five artifacts out and
added one theory-facing finding. There are 2,122 candidate Markdown update
paths: 1,123 tracked and 999 local. Path counts include the `CLAUDE.md` alias of
`AGENTS.md`; the symlink must remain a symlink.

State and affected originals are checkpointed outside the repository at
`/tmp/commonplace-theory-rename-66xwi2cr/`. The SQLite online backup passed
`PRAGMA integrity_check`. No database key migration is commissioned. That local
backup is recovery material, not a portable library dependency.

## Preservation route

`execution-relocation-updates.tsv` records each candidate's original SHA-256
and selected action. `execution-protected.tsv` identifies 1,072 candidates to
restore from the checkpoint after the command: 999 local files and 73 tracked
exact records. Verify their bytes against the recorded hashes before and after.
This bounded restoration must not touch any unrelated concurrent changes.

The tracked obligations are:

- 20 archived exact analysis results; their ignore marker explicitly declares
  immutable snapshots. Published current analysis-set members are also
  hash-pinned, but none appears in this dry run's update list.
- One ignored workshop experiment baseline landing, under an explicit frozen
  experiment marker.
- Four exact simplification experiment inputs/treatments, pinned in that
  experiment's README.
- One retained frozen trial protocol.
- One retained assessment explicitly declared an exact record at its original
  terminology boundary.
- 40 experimental cohort inputs and six retained experimental versions.

ADRs, legacy memory reviews and archived generated review projections receive
navigation repairs without changing their findings or source boundaries. The
archived projections pin their result inputs, not their own prose bytes; their
links can change while those result pins stay unchanged. A validation-ignore
marker alone is not evidence that a whole collection is byte-frozen.

The 516 affected ingests with Quotes sections have separate quote-section
hashes in the checkpoint. Verify them unchanged after backlink repair. Snapshot
files and checksums are not migration targets. Retain all existing redirect
source keys; retarget 164 values, add 423 moved-page redirects (not the two
briefs), and six generated-index redirects. Types directories receive no
virtual index, matching `index_directory.SKIP_DIR_NAMES`.

## Multi-consumer change packet

1. **Authoritative declaration:** ADR 123, the relocated collection contract,
   library build manifest and current routing. Note type remains unchanged.
2. **Scope/enforcement:** this checkout and installed library only; explicit
   runtime scopes already landed. Scaffold Notes is deliberately outside the
   renamed population.
3. **Consumer classes:** baseline `reference-files.tsv` and `residual-live.tsv`
   retain the repository-wide search. Update build/CI, local schemas and type
   instances, procedures, root instructions, current reference, tests and site
   publication class by class. Generic runtime refactoring is complete; do not
   replace it with Theory-specific eligibility. Namespace follow-up pending.
4. **Byte pins:** preserve the exact subset above and all published analysis
   members. No repinning or review-baseline migration. Verification pending.
5. **Spellings:** baseline searches cover `kb/notes/`, relative Markdown links,
   `notes/types/`, collection slots, `<library>/notes/`, `commonplace:notes/`,
   Python path components and brace-list examples. Generic note terms stay.
6. **Generated/projected forms:** switch shipped build layout and library
   routing; site discovers Theory. Init stubs keep their existing destinations.
   Installation and site probes pending.
7. **Fresh install:** must still create Notes, not Theory; test both library
   availability and scaffold independence.
8. **Existing installs/clones:** consumers keep custom collections and refresh
   pointers through init; reconcile library references separately. This source
   checkout never runs init. No compatibility alias is commissioned.
9. **Diagnostics:** no new diagnostic promises or migration command are added.
10. **Acceptance probe:** full suite, validation, site build, wheel/sdist and
    disposable fresh/existing consumer scenarios remain required.
11. **Drift guard:** retain generic arbitrary-collection tests and packaging/
    landing integrity checks; add explicit library-Theory/scaffold-Notes checks.
12. **Historical witnesses:** baseline inventories, exact captures, old review
    identities, source quotes and historical redirect keys stay old. Historical
    decision prose is not mechanically relabelled as current policy.
13. **Identity conventions:** local type pointers become `theory/types/...`;
    note and brief stems stay paired. Old review keys remain historical.
14. **Shared exclusions:** no new eligibility predicate. Keep validation-ignore
    and explicit-scope behavior; byte preservation is this migration's bounded
    handling, not a new runtime exclusion feature.
15. **Relocation effects:** preserve protected bytes; validate the relocated
    contract, local types, briefs and grounding bound before release.

## Execution status

- Workshop decisions committed.
- Post-sort dry run, move/backlink/redirect manifests and state backup complete.
- Preservation obligations identified; restoration must be verified at apply.
- ADR recorded before relocation.
- Directory relocation, namespace follow-up and release verification pending.

Do not release an intermediate tree. Keep relocation/backlinks in their own
commit. Do not remove this workshop until the final verification and consumer
upgrade instruction are complete.
