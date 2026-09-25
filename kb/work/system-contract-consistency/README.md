# System contract consistency workshop

**Opened:** 2026-07-29

**Last full rescan:** 2026-09-25, at commit `3e13281c` (after ADR 086)

**Scope:** current Commonplace contracts outside the linking and lineage
domains

## Current verdict

ADR 086 (projects read the library from the installed package, 2026-09-25)
removed the project-local library copy. That dissolved the installed-product
program that dominated the previous cycle: I1, I2 and V1 closed by
supersession, and I3 closed with a scaffold fix. M1 was already resolved. A
fresh wheel install now initializes, validates in every scaffolded collection,
and migrates an old `kb/commonplace/` copy as INSTALL.md describes.

The 2026-09-25 rescan used three read-only scouts over three surfaces: install
and delivery, reference and ADRs against code, and the skills, collection
contracts and type specs that direct agents. It found no P0. It found eight P1
contradictions and a longer P2 tail. G1 closed with ADR 088, and D1, A1, A2, L1, K1, O1, X1, and X2 closed the same day. The largest cluster is ADR 086 residue:
the migration rewrote 847 frontmatter `type:` values to bare names but left the
prose rules that teach the path form, and left older accepted ADRs making
present-tense guarantees about the copy. That is the "decision reached its
primary implementation but not every consumer" mechanism again, and the
workshop's first real evidence for the [contract-change
gate](./plans/contract-change-gate.md).

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
| R1 | P1 | Rename steps in convert, autoreason and revise-note use `git mv` plus hand-fixed links; write and retire-artifact say never rename manually | Manual renames skip the ProperDocs redirect and the pure relocation commit |
| U1 | P1 | `note.md` says a substantive edit must remove `user-verified`; the full pass, revise-note and fix-review-warnings edit bodies and keep it | A trusted human-verification mark survives agent rewrites |
| V2 | P1 | `cp-skill-validate all` turns `kb/types/` into the reserved `types` target, which sweeps every `kb/**/types/*.md` and ignores validation-ignore markers; `\|\| exit` then aborts | The full-validation procedure fails falsely on report cache and never runs later collections, landings, or redirects (source checkout) |
| N1 | P1 | cp-skill-ground routes a missing or mismatched snapshot to re-ingest; re-ingest requires a distinct basename and report, but snapshot-web refuses a second capture of the same `source` and ingest stops on several reports per `source` | Snapshots are gitignored, so on any fresh clone the prescribed remedy is blocked. Moderate confidence; needs a design choice, not a wording fix |
| V3 | P2 | `validation-contract.md` says `commonplace-validate types` covers "the complete global and local type inventory"; the target globs only the project and includes ignored cache | Same root as V2; in an installed project the library's global types are never checked by this target |
| X3 | P2 | Residue left from the 2026-09-25 cleanup: ADRs 059 and 066 lack the required `## Considered alternatives` section; ADR 073 says the snapshot marker lives in the gate while `job_prompt.py` hardcodes it (uncertain) | A retrofit needs the deciding reasoning, which may only be in git history |
| T1 | P1 | Tag coverage stated beyond one collection, checked within one | **Transferred** to [tag-contract convergence](../tag-contract-convergence/README.md); [closure tracker](./plans/t1-tag-scope.md) |
| E1 | P1 | Native Windows supported; promoted skills keep unpaired POSIX commands (health check, connect `xargs -r`, validate's Bash loop) | **Owned** by [execution-channel compatibility](../execution-channel-compatibility/README.md); [plan](./plans/e1-windows-execution.md). E1 now also owns the package-owned `commonplace-validate all` target |

Witness paths and line numbers for each new finding are in the [rescan
witness file](./rescan-2026-09-25.md). Re-derive them before acting; they go
stale quickly.

## Closed findings

| ID | Closed | How |
|---|---|---|
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
| M1 | 2026-09-25 | Areas/Topics residue gone: the areas note was rebuilt around its surviving claim, remaining mentions are historical, and `note-base.schema.yaml` (`additionalProperties: false`) rejects an `areas:` field. Global status, path-valued types, snapshot pointer and text promotion closed earlier |
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

1. **ADR 086 residue (G1, A1, K1, X1 type items).** One packet: fix the type
   specs, `cp-skill-write`, the reports contract, and reference prose; add
   amended-by markers to ADRs 022, 027, 038, 068 (and 014, 039 where their
   Consequences still speak in the present tense). Apply the contract-change
   gate retrospectively to ADR 086 while doing it. Add a guard that rejects a
   path-valued global `type:` in type-spec prose examples.
2. **Workflow fixes (R1, U1, V2/V3, D1, O1).** Each is a local procedure or
   code change with a clear authority to align with.
3. **N1.** Needs a design choice for recapturing a source whose snapshot is
   absent or changed; route to the owner of the ingest workflow.
4. **P2 sweep (A2, L1, X2).**
5. **Owners:** E1 continues in execution-channel compatibility; T1 closes here
   after the tag workshop's adoption tests.
6. **Promote the contract-change gate, then delete this workshop.**

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
