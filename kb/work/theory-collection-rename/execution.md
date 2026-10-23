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
   replace it with Theory-specific eligibility. Namespace and portable skill
   routing landed in `e4c1bfcf1` and `f698aa90d`; live workshop follow-up is
   `af299464c`. Final historical/workshop residual disposition remains open.
4. **Byte pins:** preserve the exact subset above and all published analysis
   members. No repinning or review-baseline migration. All protected hashes,
   Quotes sections, affected ingest frontmatter and baseline store rows were
   reverified after the namespace/publication batch.
5. **Spellings:** baseline searches cover `kb/notes/`, relative Markdown links,
   `notes/types/`, collection slots, `<library>/notes/`, `commonplace:notes/`,
   Python path components and brace-list examples. Generic note terms stay.
6. **Generated/projected forms:** switch shipped build layout and library
   routing; site discovers Theory. Init stubs keep their existing destinations.
   Installation and site probes passed; the generated-index redirect test
   additionally verifies actual emitted HTML, not just validator acceptance.
7. **Fresh install:** must still create Notes, not Theory; test both library
   availability and scaffold independence.
8. **Existing installs/clones:** consumers keep custom collections and refresh
   pointers through init; reconcile library references separately. This source
   checkout never runs init. No compatibility alias is commissioned.
9. **Diagnostics:** no new diagnostic promises or migration command are added.
10. **Acceptance probe:** 1,437 tests passed including slow wheel/sdist builds;
    authored-file, redirect and landing validation passed. The site built and
    all 593 rename redirects and targets were checked. Fresh non-editable
    install and all six installed scenarios passed. Customized Notes refresh
    is covered by the installation regressions and disposable consumer probe.
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

- Workshop decisions committed as `c30ebacfb`; ADR and execution checkpoint
  committed as `45f5b7061`.
- Post-sort manifests and state backup complete.
- Directory relocation committed alone as `9c7563bf7`: 427 files moved and
  approved command-produced backlinks updated across 1,470 Git paths.
- All 1,072 protected candidate paths and 516 ingest quote sections verified
  byte-identical after apply. `CLAUDE.md` remains a symlink.
- First namespace batch changes the build manifest/CI/library description,
  repository article tooling, library routing template, actual local type
  instances and schemas, Theory landing/contract, root routing and tag
  participation. Project scaffold paths and templates remain Notes.
- Regression tests explicitly distinguish library Theory from scaffold Notes,
  including customized Notes contract preservation on refresh.
- General + installation suites, including slow build coverage: 110 passed.
  Complete suite including slow workflow tests: 1,426 passed in 290.94 seconds
  (`/tmp/theory-rename-first-integration.log`). Ruff and diff checks passed.
- `commonplace-validate theory`: success, 442 files analysed, zero failures and
  warnings; orphan notices remain. Tags contract and collection landings pass.
- Editable tool metadata refreshed successfully. The plain reinstall command
  failed because tool resolution applied the seven-day cutoff to workjig;
  retrying with `--exclude-newer-package workjig=2026-10-23` honored the
  repository's declared workjig exception without changing dependencies or the
  lockfile. Commands still resolve from the user-level tool.
- Disposable consumer `/tmp/commonplace-theory-consumer-ukTvqz`: fresh init,
  `--check`, custom Notes contract preservation on refresh, library-Theory
  routing and absence of a Theory twin all passed. Init was not run here.
- Publication committed as `138bb42ab`. Shared generated-index selection fixes
  validator recognition. An early site-hook event makes virtual pages visible
  before the redirect plugin snapshots its inputs. Both regression tests failed
  before that event-order fix and passed afterward. Four obsolete analysis-method
  destinations now resolve to their replacements; four keys targeting deleted
  types without a successor were removed. All 220 historical Notes source keys
  remain. Redirect and landing validation report no failures or warnings.
- Site build completed in 147.29 seconds. All 593 manifest changes have emitted
  redirect HTML and built targets, including the six virtual indexes. Historical
  capture links and unrelated anchor/index warnings remain; the build is not
  claimed warning-free. Evidence: `/tmp/theory-site-final-build.log` and
  `/tmp/theory-site-redirect-acceptance.json`.
- Current contracts, instruction defaults, routing, prose and consumer upgrade
  guidance committed as `f698aa90d`. All 76 changed KB documents validate.
  Complete suite: 1,437 passed in 286.82 seconds, including slow tests
  (`/tmp/theory-rename-final-integration.log`); Ruff and diff checks pass.
- Preservation recheck: 1,072 protected paths, 516 Quotes sections and all 516
  affected ingest frontmatters unchanged. No current pinned analysis member
  changed. All rows in all seven backed-up SQLite tables remain byte-equivalent
  at the row-value level, with identical counts; integrity check is `ok`.
  `CLAUDE.md` remains a symlink to `AGENTS.md`.
- Non-editable installed rehearsal passed all stages with automatic project
  instruction loading and unchanged installation inventories. See
  [installed rehearsal](./installed-rehearsal.md). It uses Codex CLI, not Pi;
  no live source capture or PyPI release installation is claimed.
- Final rescan found two additional live workshop draft type pointers and
  current framing routes. Commit `af299464c` repairs those in 11 validated
  artifacts without changing exact records or provisional lifecycle choices.
- [Residual audit checkpoint](./residual-audit.md) records tracked and ignored
  spelling searches, established dispositions and the remaining per-role work.
  Remaining: finish historical/workshop residual disposition, retain the final
  acceptance record and close this workshop. Do not call the
  full rename release-ready until that audit and closeout are complete.

Do not release an intermediate tree. Keep relocation/backlinks in their own
commit. Do not remove this workshop until the final verification and consumer
upgrade instruction are complete.
