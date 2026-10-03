# Implement the report collection split

Draft plan awaiting adoption. Read the [coverage audit](./contract-coverage-check.md)
and [input comparison](./input-coverage.md) before choosing this plan over shortening.
Implement only after the prototype checks and migration choices are accepted. Isolation landed in `ee81c5586`; recheck current
status and open runs before editing. Do not resume old runs under a changed method.

## Proposed migration dispositions

| Cohort | Proposed disposition |
|---|---|
| `AAS-2026-10-02-dynamic-cheatsheet-01` | Mechanically migrate and repin; retain as prior accepted evidence, without selecting it by directory scan |
| `AAS-2026-10-03-dynamic-cheatsheet-02` | Mechanically migrate and repin; convert its current generated review to the selected reference |
| `layout-migration-2026-10-01/` | Move byte for byte as historical migration evidence; its recorded old paths/hashes remain historical data |
| `reports/retained-archive/` | Move byte for byte, preserve historical frontmatter and exclusions; redirect old public member URLs |
| Existing ordinary authored reviews | Keep unchanged |
| Historical generated reviews | Preserve producing bytes/contracts; repair public routes through redirects, not silent retyping |
| Ignored state | Inventory; finish under old method or retain stopped recovery evidence under original identity. Never migrate into a resumable new-method run |

Check these dispositions against the actual review/pin inventory before adoption.
The two retained sets belong to the same source; selection stays with the current
published review, subject to identity/hash verification. Historical archives need
no procedural pin preservation per the operator's proposal premise, but public
links still need a disposition. Do not change their bytes to repair links.

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

1. Accept contract coverage/measurement results, reference semantics and bounded
   migration authority. Inventory current consumers and open runs.
2. Prepare destination/types/consumer changes in an isolated implementation tree.
   Keep the publication gate closed while contracts and readers disagree.
3. Dry-run relocation and examine its automatic link and pin effects. Use bare
   commonplace relocation commands; inspect their actual APIs before selecting
   one. Commit relocation-command results alone as required by root doctrine.
4. Commit bounded retyping, hash-map evidence and consumer/publication changes
   separately, with explicit file staging. Verify unchanged analytical content.
   Intermediate relocation commits are not publishable product states.
5. Promote navigation/references and redirects only with valid destination sets.
   Validate, run required checks, rescan old forms, and record migration acceptance.

## Acceptance

- Both contracts are sufficient; the complete per-role packet comparison records
  actual savings and compares the shortening alternative.
- Current migrated sets validate; content/source/record identities are unchanged
  outside authorized mechanical edits. Every old/new hash is recorded and pins
  resolve. Archives and the earlier migration evidence retain exact hashes.
- Overview links expose members and reconciliation without duplicate synthesis.
- Readers reproduce the selected source, revision, tier, manifest and memory
  fields; prior runs/archives never join current populations by accident.
- Publication tests cover initial selection, replacement, failures and interruptions
  from the publication draft. A stale or invalid reference blocks the site build.
- Site boundary tests prevent working-state/candidate/recovery leakage; historical
  public URLs resolve to supported targets.
- Run focused tests, then `uv run pytest -q` and `uv run ruff check .`; run relevant
  bare commonplace-validate checks and site/redirect checks. Probe package/init
  behavior in a temporary consuming project if affected; never init this checkout.
- Rescan old forms and record remaining historical hits. Record accepted ADR and
  migration evidence before commissioning any separate live analysis.
