# System contract consistency workshop

**Opened:** 2026-07-29

**Last full rescan:** 2026-09-25, at commit `3e13281c` (after ADR 086)

**Latest follow-up:** 2026-09-25, at commit `2959ee61` plus concurrent
working-tree cleanup; [findings and probes](./rescan-2026-09-25-followup.md).

**Scope:** current Commonplace contracts outside the linking and lineage
domains

## Current verdict

All findings from the 2026-09-25 rescan and its follow-up are closed except
T1 and E1, which are held by owner workshops. The contract-change gate is
promoted. The closed tables below record how each was resolved.

ADR 086 (projects read the library from the installed package) removed the
project-local library copy, which dissolved the previous cycle's
installed-product program. The rescan's largest cluster was ADR 086 residue:
its mechanical rewrite changed 847 frontmatter `type:` values but not the
prose rules teaching the old form, left older accepted ADRs making present-tense
guarantees about the copy, and silently broke 33 byte pins on retained
analysis results. ADRs 087 and 088 then reworked type naming, and the
follow-up scan found that their migration still missed local schema
constants, quoted values, and collision reporting (I4, H1, H2). Each case is
the "decision reached its primary implementation but not every consumer"
mechanism, and together they are the worked evidence for the
[contract-change gate](./plans/contract-change-gate.md).

## Standard used

A **confirmed contradiction** needs two current, operative witnesses that
cannot both be followed over the same declared scope. An advertised command
with an empty legal input domain also qualifies. A missing future feature, an
explicitly historical statement, or an unimplemented proposal does not.

- **P0** — a fresh install or completion signal is unsound;
- **P1** — a current supported workflow, trusted mark, or system-definition
  contract can direct incompatible actions;
- **P2** — a narrower reference or authoring surface teaches a rejected or
  invalid shape.

## Open findings

| ID | Pri | Contradiction | Consequence |
|---|---|---|---|
| T1 | P1 | Tag coverage stated beyond one collection, checked within one | **Transferred** to [tag-contract convergence](../tag-contract-convergence/README.md); [closure tracker](./plans/t1-tag-scope.md) |
| E1 | P1 | Native Windows supported; promoted skills keep unpaired POSIX commands (health check, connect `xargs -r`, validate's Bash loop) | **Owned** by [execution-channel compatibility](../execution-channel-compatibility/README.md); [plan](./plans/e1-windows-execution.md). E1 now also owns the package-owned `commonplace-validate all` target |

Witness paths and line numbers for each new finding are in the [rescan
witness file](./rescan-2026-09-25.md). Re-derive them before acting; they go
stale quickly. I4, H1, H2 and Q1 have their witnesses and reproduction results
in the [follow-up scan](./rescan-2026-09-25-followup.md), which also extends X1
with remaining type-field table errors. X1's project-shared-type complaint is
superseded by ADR 088, which deliberately dropped that eligibility.

## Closed findings

| ID | Closed | How |
|---|---|---|
| X3 | 2026-09-25 | ADR 073 records that prompt scaffolding also recognizes the snapshot marker; ADRs 059 and 066 carry Considered alternatives reconstructed from their commits and proposal, with inferred points marked |
| I4 | 2026-09-25 | Init's migration also rewrites a local schema's `kb/...` type constant to the ADR 088 form and handles single-quoted type values; a second run changes nothing |
| H1 | 2026-09-25 | `commonplace-init --check`, which the health check runs, reports a project `kb/types/<name>.md` that collides with a library global type as `collision` |
| H2 | 2026-09-25 | Type collisions raise a distinct `TypeCollisionError` that type-review selection lets through, so the selector fails with the collision instead of returning no targets |
| Q1 | 2026-09-25 | Retirement requires pytest only when it touched code, tests or their inputs, or `properdocs.yml`; Markdown-only retirements rely on the validator checks |
| N1 | 2026-09-25 | An absent capture is reported as "not available on this machine" instead of routing to re-ingest; a changed source becomes a new observation: `cp-skill-snapshot-web` and the capture commands accept `reobserve`/`--reobserve` and write a date-named capture, `cp-skill-ingest` treats several ingests of one URL as separate observations, and `re-ingest` gains a **New observation** path. The grounding-alignment gate still fails on an absent capture |
| V2, V3 | 2026-09-25 | The `types` target skips validation-ignored subtrees, so it no longer fails on report cache; `cp-skill-validate all` runs every check and reports failure at the end; the validation contract states the target's real scope. A package-owned `validate all` remains E1's |
| R1 | 2026-09-25 | Convert, autoreason, and revise-note rename through `commonplace-relocate-note` (dry run, then `--apply`) and commit relocations alone; revise-note leaves renames to a separate step |
| U1 | 2026-09-25 | Revise-note, the full pass (after applied body edits), fix-review-warnings, and the ASD-STE100 rewrite remove `user-verified`, as the note type requires for substantive edits |
| D1 | 2026-09-25 | The installed `AGENTS.md.template` now permits nested delegation within existing authority, matching the root `AGENTS.md` and the instruction type |
| A1 | 2026-09-25 | ADRs 014, 022, 027, 038, and 039 carry amended-by markers for ADR 086; 068, 086, and 087 for ADR 088 |
| A2 | 2026-09-25 | ADR 082's operativity path states FAIL force; ADR 064 no longer claims init inspects `.envrc`; ADRs 073 and 076 carry amended-by markers for 076 and 078 |
| L1 | 2026-09-25 | Notes, agentic-systems, and agent-memory-systems contracts link tracked ingests, never local snapshots |
| K1 | 2026-09-25 | `write-instruction.md` and the instructions contract describe checkout symlinks and init-written stubs instead of copies |
| O1 | 2026-09-25 | The compression bundle's default report path is `kb/reports/cache/compression-bundle/` |
| X1, X2 | 2026-09-25 | Generated-index spec renamed `generated-index`; type specs teach file-relative `schema:`; prototype pages describe ready-to-use contracts; per-gate partitions described as not declared; CLI help for `validate --output` and `create-review-jobs --model-partition` corrected; notes, articles, instruction-type, onboarding, and workshop-run residue fixed. Remainder is X3 |
| G1 | 2026-09-25 | [ADR 088](../../reference/adr/088-type-values-are-paths-on-a-two-root-search-path.md) made every type value a path under a KB root; the type specs, `cp-skill-write`, the reports contract, and reference pages now teach that form, and validation rejects bare names with the path to use |
| I1 | 2026-09-25 | Superseded: ADR 086 replaced ADR 021's marker-backed copy with reading the library in place |
| I2 | 2026-09-25 | Superseded: no install projection remains; `hatch_build.py` rewrites links leaving the library and fails the build on unresolved ones |
| V1 | 2026-09-25 | Superseded: a fresh install has no nested collections; the residual package-owned `all` target moved to E1 |
| I3 | 2026-09-25 | `fd573556` made `kb/types` a collection; `85cd8ef4` scaffolds a `kb/work` contract and tests that every routed project collection ships one |
| M1 | 2026-09-25 | Areas/Topics procedure residue gone: the areas note was rebuilt around its surviving claim and remaining mentions are historical. Correction from the follow-up: the schema permits extra frontmatter fields and does not reject `areas:`. Closure rests on the procedural migration, not that claimed enforcement. Global status, path-valued types, snapshot pointer and text promotion closed earlier |
| S1 | 2026-08-23 | ADR 072: the tracked ingest owns durable genre; snapshots stay whole-file immutable |
| C1 | 2026-08-19 | Exact console-script/command-reference parity test |
| F1 | 2026-08-19 | ADR 065 withdrew the generic freshness accept command |

Closed plans and the superseded disjoint-root design (decision packet, impact
ledger, successor ADR draft, implementation packets, 2026-08-27 witness
ledger) were deleted on 2026-09-25; git history keeps them.

## Root causes

1. **Decisions and migrations lack consumer manifests.** ADR 086 is the fresh
   example: the mechanical frontmatter rewrite was inventoried and tested, the
   prose rules teaching the old form were not, and older ADRs were not marked
   amended. G1, A1, K1 and part of X1 follow from it.
2. **Scope is prose reimplemented as traversal.** "All collections" and "the
   complete type inventory" are claims; the skill's glob and the `types`
   target's walk each select their own set (V2, V3).
3. **Parallel procedures drift.** Rename, verification-mark, and re-ingest
   rules live in one authoritative place and are restated or bypassed in
   several procedures (R1, U1, N1).
4. **Presence is mistaken for capability.** Unchanged from the last cycle; E1
   is its remaining instance.

## Implementation order

1. **Owners:** E1 continues in execution-channel compatibility, including a
   package-owned `commonplace-validate all`; T1 closes here after the tag
   workshop's adoption tests.
2. **Contract-change gate — promoted 2026-09-25** as
   [change a contract that several consumers read](../../instructions/change-a-contract-that-several-consumers-read.md),
   loaded from the ADR type's operativity-path rule; worked applications are
   in the [gate plan](./plans/contract-change-gate.md).

## Exclusions and non-findings

- Linking vocabulary, direction, and grammar remain in the [linking
  workshop](../linking-contract-consistency/README.md); lineage conflicts in
  the [lineage ledger](../lineage-mechanisms/current-contradictions.md).
- Init no longer copies `kb/sources/types` or `kb/reports/types`: [ADR
  087](../../reference/adr/087-source-and-report-types-are-global-library-types.md)
  (accepted 2026-09-25) made the seven source and report types global library
  types and retyped local snapshots with their ingest checksums re-pinned.
- Proposals that still describe the `kb/commonplace/` layout (for example the
  tag-scope proposal) are unadopted and outside the standard.
- `kb/work/dialectical-sample/COLLECTION.md` and report-cache contracts sit
  under validation-ignore markers or gitignore; they are not live collections.

## Closure condition

This workshop closes after every open finding is resolved in durable system
artifacts or transferred to a named owner with acceptance criteria, the
contract-change gate is promoted, and transferred findings are rechecked
against their witnesses. Then delete the workshop so it does not become a
second authority surface.
