---
type: types/note.md
description: "Acceptance record for the Theory library rename: runtime scope, publication, installed Notes consumer, residual references and preserved evidence."
---

# The Theory rename passed publication and installed-consumer checks

## Decision and scope

The rename is complete. This record closes the implementation acceptance gate
for [ADR 123](../../../reference/adr/123-theory-names-the-commonplace-library-collection.md).
This KB uses `kb/theory/`; the shipped library uses `theory/`. The **note** type,
generic note APIs and `source_notes` remain unchanged. Runtime commands select
explicit collections rather than assuming Notes or Theory.

Consuming projects keep their Notes scaffolds and customized contracts. They do
not acquire a Theory twin or a dual-root library alias. Follow the
[upgrade instruction](../../../instructions/upgrade-the-theory-library-layout.md)
for library-reference reconciliation; a project's own collection rename needs
separate authorization. Review/freshness path continuity was explicitly waived.

## Implementation and acceptance

The [closeout verification](verification.json) records the repeated full suite,
site build, redirect checks, artifact validation and post-test preservation checks.

- `9c7563bf7` separately relocated 427 files and repaired backlinks. Two briefs
  and two schemas are not published pages.
- `e4c1bfcf1` shipped Theory while preserving Notes consumer scaffolds.
  `f698aa90d` reconciled current contracts, instructions and upgrade guidance.
- `138bb42ab` completed publication: 423 moved-page redirects, 164 retargeted
  existing redirects and six generated-index redirects, **593 changes** total.
  All 220 existing Notes source keys remain. Generated files reach redirect
  consumers before they snapshot the page set. The site build completed and
  all 593 changed redirects had correct HTML and built destinations.
- The integration suite passed **1,437 tests**, including slow wheel/sdist
  builds. Ruff, redirect validation and collection-landing validation passed.
  Protected-history link warnings and unrelated site warnings remain; the site
  is not claimed to be warning-free.
- All six isolated installed-project stages passed: installation, note writing,
  first ingest, read-only answer, second ingest and fresh read-only answer.
  A non-editable local-source installation exposed library Theory and project
  Notes without a Theory twin. Agent instruction loading, separate ingestion
  workers, source/snapshot preservation and read-only answer boundaries were
  checked. No product repair or supervisor assistance was required.

The captured rehearsal summary (`records/installed-rehearsal.md`, retained as
unpublished data; [checkpoint copy](https://github.com/zby/commonplace/blob/3fd74968d/kb/work/theory-collection-rename/installed-rehearsal.md))
records the source commit, Codex/Linux runtime, evidence locations and stage boundaries.
This is not evidence of a PyPI release, Pi execution, live capture, other operating
systems or arbitrary consumers. Keep the raw disposable run until the operator
accepts its disposal.

## Final residual-reference disposition

`dc1f0e67a` repaired live reading targets and collection/type pointers in seven
additional workshop documents. Earlier follow-up repaired eleven live
workshop framings/drafts. These are navigation repairs, not revisions of dated
findings or trial inputs.

[Residual dispositions](residual-dispositions.tsv) classify **570 tracked
readable files** still containing old path forms after those repairs, excluding
the closing workshop and this retained evidence packet. Each row records the
file, matching lines, content hash, role and disposition. This is a spelling
inventory, not a broken-link count. It distinguishes:

- Valid consumer Notes paths, generic test/example identities, upgrade search
  strings and historical redirect source keys.
- Dated findings and decisions, completed targets, captured prompts/results,
  pinned manifests and copied experimental gates. Historical prose may retain
  its original namespace even where navigation to the same artifact is repaired.
- External consuming repositories, explicitly pinned pre-rename benchmark
  checkouts and provisional historical lifecycle alternatives.
- Six files referring to already-retired targets absent from the relocation
  population. No successor or new vocabulary was invented for them; these are
  pre-existing references, not an unfinished Theory migration.

The earlier tracked-plus-local scan found 20,138 matching paths, including
18,675 report-state paths and 1,056 report-cache paths. These local counts do not
confer mutation authority. Review packets and state were not rewritten,
acknowledged, carried forward or re-keyed. No unclassified live target remains
within the audited rename scope; this does not certify every historical link.

## Preservation and closure

[Final preservation checks](preservation.json) compare the recovery checkpoint
with the closed implementation: all **1,072 protected paths**, **516 ingest
Quotes sections** and their full affected ingest frontmatters are unchanged.
Current pinned analysis members have no diff from the preflight base. All seven
SQLite tables retain identical row counts and values; integrity is `ok`.
`CLAUDE.md` remains a symlink to `AGENTS.md`.

[Retained-input hashes](retained-inputs.json) identify thirteen exact machine
inventories and one exact rehearsal-summary capture from checkpoint `3fd74968d`.
The original `moves.tsv`, `relocation-updates.tsv`, `redirect-changes.tsv` and
`inventory-summary.json` describe **pre-sort planning**, not execution. Use the
`execution-*` inventories for the actual relocation, protection and redirect
population. These retained files are historical evidence, not an executable
migration queue.

The completed workshop and its Active Workshops entry are removed. Durable
policy lives in ADR 123, the upgrade instruction and the current contracts, not
a permanent shadow workshop. Explicit publication redirects remain by operator
decision; removing them is separate future work. Replacement review/freshness
design and the broader Work/Tasks lifecycle design remain outside this change.

The rename-specific release hold is cleared. This does not perform or certify a
package release beyond the acceptance scope above.
