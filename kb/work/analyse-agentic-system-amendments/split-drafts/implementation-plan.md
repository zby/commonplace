# Implement the report collection split

Draft plan awaiting adoption. Read the [coverage audit](./contract-coverage-check.md)
and [input comparison](./input-coverage.md) before choosing this plan over shortening.
Implement only after the prototype checks and migration choices are accepted. Isolation landed in `ee81c5586`; recheck current
status and open runs before editing. Do not resume old runs under a changed method.

## Dispositions of existing material

Operator decision, 2026-10-03: nothing is migrated; every analysis is
regenerated under the new method.

| Cohort | Disposition |
|---|---|
| `reports/retained/` (two Dynamic Cheatsheet sets, `layout-migration-2026-10-01/`) | Stay in place as frozen history. Add the validation exclusion when the member types move. |
| `reports/retained-archive/` | Stays in place, unchanged. Existing redirects into it stay valid. |
| The one generated review | Retire when the member types move; regenerate that system first. |
| Hand-authored reviews | Keep unchanged. |
| Ignored state | Finish under the old method or keep as stopped evidence under the original identity. Never resume under the new method. |

The new collection starts with empty `state/`, `retained/` and
`retained-archive/`. No hash map, repinning or bounded migration authority is
needed. The comparison population is empty until analyses are regenerated.

## Documents and type changes

Promote both collection contracts and the new landing. Move the analysis
method to the new collection's `instructions/`: the skill directory, run
driver, job instructions and the three shared analysis contracts. Update the
skill projections and the method paths resolved in workflow code. Landscape
synthesis and taxonomy refresh stay. Move all seven current
analysis member/set/run-state type specs and schema sidecars together. Replace
current identities `agentic-systems/types/<name>.md` with
`agentic-system-analyses/types/<name>.md`; keep generated-review's historical type
in the old owner. Update schema constants, relative schema references and member
link rules. Add the reference type/schema. Name the publication instruction in
its type and maintenance consumption path. Promote the method-maintenance draft
and wire its mandatory authoring route. Move unique instruction-maintenance
rules out of the old contract only after a verified mandatory loading path exists.

Update the parent proposal and Sol-plan item 1 to supply the new contract. Worker
jobs writing collection artifacts receive it in read-first and dependency hashes.
No worker packet names a file in the old collection.

## Consumer inventory before mutation

Complete the 15-field packet in
[the contract-change procedure](../../../instructions/change-a-contract-that-several-consumers-read.md).
Search old path roots, type identities, generated-review fields, generated-by
predicates, reference discovery and public exclusions across tracked and ignored
state. Save patterns, hit counts and per-consumer dispositions. History stays
marked as history rather than rewritten indiscriminately.

Cover workflow/checkout/publication/set/analysis code, method-change guards,
validators, record and member links, matrix/table/statistics scripts, public
synthesis, taxonomy maintenance, transfer scans, command documentation, skill
projections, package/init surfaces, site navigation, member allowlists and redirects.
Use one shared selected-reference predicate for current comparison membership.
CLI selection flags and table provenance columns need an explicit transition;
update them and their callers together rather than leaving review-specific names
with undocumented changed meaning. No consumer-demanded compatibility is known.

## Order and commits

1. Accept contract coverage/measurement results and the publication design.
   Inventory current consumers and open runs.
2. Prepare destination/types/consumer changes in an isolated implementation tree.
   Keep the publication gate closed while contracts and readers disagree.
3. Dry-run relocation and examine its automatic link and pin effects. Use bare
   commonplace relocation commands; inspect their actual APIs before selecting
   one. Commit relocation-command results alone as required by root doctrine.
4. Commit type-identity, consumer and publication changes separately, with
   explicit file staging. Add the validation exclusion for the old
   `reports/retained/` and retire the one generated review in the same step.
   Intermediate relocation commits are not publishable product states.
5. Validate, run required checks, rescan old forms and record acceptance.
   The relocation covers method and type files only; no retained set moves.

## Acceptance

- Both contracts are sufficient; the complete per-role packet comparison records
  actual savings and compares the shortening alternative.
- The old `reports/` tree is byte for byte unchanged and excluded from
  validation and from the comparison population. The new collection's
  `retained/` and `retained-archive/` are empty.
- Overview links expose members and reconciliation without duplicate synthesis.
- Readers reproduce the selected source, revision, tier, manifest and memory
  fields; prior runs/archives never join current populations by accident.
- Publication tests cover first publication of a system, replacement with the
  move of the superseded set to the archive, failures and interruptions.
  Two sets of one source in `retained/`, or a directory whose name does not
  match its set's source, fail validation.
- Site boundary tests prevent working-state/candidate/recovery leakage; historical
  public URLs resolve to supported targets.
- Run focused tests, then `uv run pytest -q` and `uv run ruff check .`; run relevant
  bare commonplace-validate checks and site/redirect checks. Probe package/init
  behavior in a temporary consuming project if affected; never init this checkout.
- Rescan old forms and record remaining historical hits. Record the accepted
  ADR before commissioning any separate live analysis.
