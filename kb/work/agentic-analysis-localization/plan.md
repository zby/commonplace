# Localize agentic analysis machinery

## Intent and authority

The operator requested this plan on 2026-10-01. Agentic-system analysis is
focused research machinery, so its instructions, types and reports should
belong to `kb/agentic-systems/` rather than the general Commonplace library.
The operator agreed that moving reports into this collection resolves the
collection-local type eligibility constraint.

This session authorizes writing the plan and its workshop navigation entry.
It does not authorize executing the migration. A later implementation session
must receive that authorization. This plan does not authorize new analyses,
source refreshes, changes to analytical judgments, or corpus regeneration.

Completion means the collection owns its analysis method and outputs, existing
results remain readable and verifiable, and the relocated types validate
without changing the general type eligibility rules. Close this workshop when
implementation and acceptance are complete, durable decisions are recorded,
and any remaining work has an explicit destination.

## Target layout

```text
kb/agentic-systems/
  COLLECTION.md
  README.md
  instructions/
    analyse-agentic-system/
      SKILL.md
      drive-a-code-scheduled-run.md
      jobs/
    agentic-analysis-boundary.md
    agentic-analysis-sources.md
    agentic-analysis-records.md
    synthesize-agent-memory-landscape/
      SKILL.md
    refresh-agent-memory-review-taxonomy.md
  types/
    generated-review.md + schema
    agentic-system-analysis-set.md + schema
    agentic-system-analysis-run-state.md + schema
    agentic-system-analysis-overview.md + schema
    agentic-system-runtime-report.md + schema
    agent-memory-analysis-report.md + schema
    agentic-system-epistemic-report.md + schema
    agentic-system-reconciliation-report.md + schema
  reports/
    state/<run-id>/       # local working runs
    retained/<run-id>/    # tracked frozen sets
  reviews/
  reviews-archive/
  comparisons/
```

Use `agentic-systems/types/<name>.md` as the relocated types' identities.
Keep a single `COLLECTION.md` at the collection root. The instruction and
report directories are areas of that collection, not nested collections.
The generic instruction, type-spec and base schemas remain global.

Landscape synthesis and taxonomy maintenance are proposed companion moves:
confirm their direct dependencies before relocation. Keep the Commonplace
transfer scan in `kb/instructions/`; update its input paths. Its current
Commonplace baseline and interest brief give it a separate purpose.

Analysis-specific Python modules and CLI entry points remain where they are
for this migration. Removing them from the package or designing a separate
extension is deferred. Moving the documents under this collection already
removes them from the packaged library's current shipped trees.

## 1. Establish the migration boundary

Reinspect Git status before implementation. At planning time there are pending
edits to the analysis skill, its boundary job, workflow code, and two workflow
test files. Preserve those edits. Identify their owner and whether they must
land before this migration; do not fold them into relocation commits.

Inventory the current method, schemas, generated reviews, retained sets,
ignored run directories, runtime skill symlinks, and direct consumers. Record
the exact old-to-new path map and counts before changing files. Search literal
paths as well as Markdown links, type identities, schema constants and rule
registrations. Include trial tools, comparison readers and review machinery.
Inspect historical archive markers and contracts so obsolete reports are not
silently reclassified as current sets.

Quiesce active analysis and publication runs before moving their method or
state. Runs pin the method commit: moving the method changes that boundary.
Before any mutation, decide which unfinished runs must finish under the old
method, which can be abandoned, and whether any require an explicit migration.
Do not replace an old run's method commit with the new one to make it resume.

## 2. Record collection ownership and migration permission

Record a durable decision for collection-specific instructions, local report
types, and report lifecycle areas. Amend the applicable parts of ADR 084
(lifecycle operations live in `kb/instructions/`) and ADR 087 (named analysis
report types are global). Preserve their unrelated decisions.

State a bounded exception to frozen-set immutability for this migration:
allow only declared path/type rewrites and the hashes derived from them.
Keep analytical bodies, source boundaries, evidence assessments, record IDs,
run IDs and historical method commits unchanged. Record old and new hashes
and the transformation used. If preserving a reference requires a broader
change, stop that item and resolve it explicitly before proceeding.

Update collection and routing contracts to permit collection-specific
instructions. Carry the needed instruction authoring and composition rules
into the new owning contract or an explicitly loaded shared instruction;
moving files must not silently drop the rules previously inherited from
`kb/instructions/COLLECTION.md`. Update AGENTS.md's canonical skill-location
guidance and affected general instructions' link restrictions.

## 3. Relocate documents and adapt consumers

Use the Commonplace relocation commands for documents and directories.
Commit relocation results separately from content edits, as required by the
repository Git rules. Keep the migration quiescent across intermediate commits;
rename commits may precede the code that makes the new paths operative.

Update both `.agents/skills/` and `.claude/skills/` projections for moved
skills. Preserve skill names and invocation interfaces. Repair relative
links, worker contract paths and schema references at their new locations.

Update the workflow's jobs, state root, type values and schema loading;
the set loader's retained root and set type; run-state path checks;
publication output allowances and method paths; and type-specific validation
registrations. Pin instructions, shared contracts and local schemas as method
inputs without accidentally pinning changing outputs as method files.

Update direct consumers together: handoff, finalize and publication commands,
comparison readers, landscape synthesis, taxonomy maintenance, transfer scan,
trial tooling and relevant tests. Repair navigation and live documentation.
Historical proposals and workshop evidence need an explicit disposition when
they mention the old layout; preserve historical meaning rather than applying
a repository-wide text replacement.

Set ignore and validation boundaries for `reports/state/`: ordinary collection
validation skips it, while explicit workflow validation still checks selected
runs. Keep `reports/retained/` tracked and included in collection validation.
Define these lifecycles in the collection contract and relevant types.

## 4. Migrate existing results and references

Prepare a deterministic dry run against copies before altering published sets.
Use the inventory to distinguish current sets from historical archived forms.
The relocation commands do not supply the complete type and hash migration.

For current sets, move the directories, rewrite only the declared type values
and required path references, recompute member hashes in `ARTIFACT.yaml`, then
recompute manifest hashes in generated reviews and applicable run records.
Update downstream path/hash references that claim current verifiability.
Historical commit-bound syntheses retain their original input commit and
provenance; do not present their old hashes as pins for migrated current bytes.

Preserve byte equality between corresponding working and retained output copies
where a complete run's validation requires it. Audit relative citations after
the move; any necessary rewrite belongs in the declared transformation.
Keep a machine-readable mapping of old paths/hashes to new paths/hashes and
acceptance evidence in a durable retained migration report under this collection.

Do not migrate ignored state blindly. Inventory it separately, preserve useful
recovery copies, and apply only the disposition established before relocation.
If an existing artifact cannot be migrated mechanically, preserve it under an
explicit historical policy and report the unresolved consumer before cutover.

## 5. Acceptance and cutover

- Validate every relocated type and instruction and the whole target collection
  with `commonplace-validate`.
- Validate every migrated retained set, each generated review's manifest pin,
  and each complete run record included in the migration.
- Compare pre/post analytical content, source provenance and record identities;
  require every byte change to belong to the declared transformation.
- Run focused workflow, publication, member-type, instruction-composition and
  comparison-reader tests, then required development checks through uv.
- Exercise publication with a scripted fixture, including incumbent replacement,
  method-change rejection and failure before public replacement. Do not launch
  a new external-system analysis merely to check relocated paths.
- Rebuild comparison outputs in an isolated destination and verify that selected
  systems, evidence tiers, axis values and supporting records remain equivalent.
  Expect provenance path/hash fields to change.
- Build and inspect the package using the installation procedure: generic skills
  and types remain available; relocated analysis documents are excluded; shipped
  links resolve under the build hook's rules. Confirm repo skill discovery.
- Search for remaining old operational paths and type identities. Classify
  historical references explicitly; no live consumer may require a retired path.

Keep raw pre-migration bytes and the mapping available until acceptance passes.
If hash migration or publication checks fail, leave analysis runs quiescent and
repair or restore from those exact bytes; do not continue with a partially
verifiable corpus. Do not force-reset unrelated work.

Commit explicit files in coherent groups. Commit messages state counts moved,
what was preserved and what was deferred, with applicable Decision and Workshop
trailers. Remove this workshop and its navigation entry after the retained
migration evidence and durable contracts are complete.

## Technical basis

- [Collection and type resolution](../../reference/collections-and-types.md) — local types are eligible only in their owning collection.
- [Instruction placement decision](../../reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) — the lifecycle instruction placement rule needs amendment.
- [Global report types decision](../../reference/adr/087-source-and-report-types-are-global-library-types.md) — the analysis types' current global status needs a scoped amendment.
- [Analysis collection contract](../../agentic-systems/COLLECTION.md) — current publication, retention and regeneration rules.
- [Published set contract](../../agentic-systems/types/agentic-system-analysis-set.md) — closed membership and member hashing.
