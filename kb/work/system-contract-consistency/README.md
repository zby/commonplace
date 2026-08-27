# System contract consistency workshop

**Opened:** 2026-07-29

**Last full recheck:** 2026-08-27

**Audited commit:** `6660bd2ad0d53938551ac283f60463f3c3d91b8e`

**Last plan refresh:** 2026-08-27 (full rebaseline, installation program,
and T1 transfer)

**State:** seven findings remain open; C1 and F1 were resolved on 2026-08-19,
and S1 was resolved on 2026-08-23. Plans and outcomes are recorded in the
[plan index](./plans/README.md). T1 remains an open finding here, but its design
and implementation have transferred to the dedicated
[tag-contract convergence workshop](../tag-contract-convergence/README.md).

**Scope:** current Commonplace contracts outside the linking and lineage
domains

## Current verdict

Seven of the ten confirmed contradictions remain open. C1 closed by documenting
the omitted executable and enforcing exact catalogue parity. F1 closed by
withdrawing a generic freshness command that had no legal target. S1 closed
when ADR 072 moved durable genre authority to the tracked ingest and restored
whole-file immutability for local snapshots. Several witnesses changed without
closing their findings:

- E1: the health check gained one PowerShell-paired step and dropped obsolete
  activation instructions, but several promoted procedures are still
  POSIX-only;
- V1: the promoted skill's one-level glob now sees five of eight installed
  collection contracts and still omits all three nested shipped collections;
- I3: installed sources gained a contract and the generated control plane
  stopped denying that types is a collection, but installed work remains
  contractless and discovery still excludes the global type collection;

The install-integrity result is now **532** missing-link warnings across 181
files: 518 in the three shipped library collections and 14 in shared global
types. Installed reference also has one projection-specific type failure. The
advertised full-validation procedure still skips all three shipped
collections, so it can report completion without examining this broken
surface. The generated counts, stale-witness dispositions, and reproduction
boundary are recorded in the [2026-08-27 witness
ledger](./baseline-2026-08-27.md).

The recurring mechanisms remain:

- an exception or migration landed in its primary schema or decision record
  but not in every consumer;
- a scope word such as “all,” “every,” or “supported” is broader than the
  mechanism that enforces it;
- a command or workflow was exposed before its accepted input domain existed;
- a non-identity install projection is tested as a copier rather than operated
  as the product a user receives.

## Standard used

A **confirmed contradiction** needs two current, operative witnesses that
cannot both be followed over the same declared scope. An advertised command
with an empty legal input domain also qualifies. A missing future feature, an
explicitly historical statement, or an unimplemented proposal does not.

Priorities mean:

- **P0** — a fresh install or completion signal is unsound;
- **P1** — a current supported workflow, trusted mark, or system-definition
  contract can direct incompatible actions;
- **P2** — a narrower current reference or authoring surface teaches a rejected
  or invalid shape.

## Findings at a glance

| ID | Priority | Current contradiction | Immediate consequence | Plan |
|---|---|---|---|---|
| I1 | P0 | Accepted ADR 021 promises four shipped collections, a marker, and marker-backed refresh; init ships three, writes no marker, and preserves every differing file | Package upgrades cannot update existing project-local library or skill copies as promised | [Shipping and upgrade](./plans/i1-shipping-upgrade.md) |
| I2 | P0 | Source-valid local paths are copied through a topology change without shipping or translating their targets | A pristine install has 532 missing-link warnings and one type failure | [Install projection integrity](./plans/i2-install-projection-integrity.md) |
| V1 | P0 | The promoted skill's `all` procedure uses `kb/*/COLLECTION.md`, while installed library collections are nested below `kb/commonplace/` | The normal completion path skips the shipped library | [Validate all](./plans/v1-validate-all.md) |
| I3 | P1 | Generated routing treats installed work as a collection without a contract, while discovery and conformance exclude contract-bearing `kb/types/` | Read-before-write is impossible for installed workshop writes and a real collection remains outside collection consumers | [Installed topology](./plans/i3-installed-topology.md) |
| S1 | P1 | **Resolved 2026-08-23:** the tracked ingest owns durable `genre`; a local snapshot's optional genre is provisional and its bytes remain immutable after capture | ADR 072 removes the mutation exception and aligns the collection, types, and ingest write boundary | [Completed outcome](./plans/s1-snapshot-mutation-boundary.md) |
| T1 | P1 | Tag coverage is stated and routed beyond one collection but generated and checked within one collection | A validated mark can falsely license a reader to skip the exact membership query that would expose omissions | [Transferred owner and closure tracker](./plans/t1-tag-scope.md) |
| E1 | P1 | Native Windows is supported, but promoted skills retain unpaired POSIX-only commands | Selected recovery and authoring procedures are non-operative on a declared channel | [Windows execution](./plans/e1-windows-execution.md) |
| F1 | P1 | **Resolved 2026-08-19:** the unsupported generic accept entry point, transition, schema, and current-facing claims were withdrawn | ADR 065 requires a concrete non-review target before the surface can return | [Completed outcome](./plans/f1-freshness-accept.md) |
| M1 | P2 | One accepted representation migration retains live guidance; four independent packets are now resolved and guarded | Agents can still follow the retired Areas/Topics grouping contract until tag adoption supplies its replacement | [Migration residue](./plans/m1-migration-residue.md) |
| C1 | P2 | **Resolved 2026-08-19:** the current 22 console scripts have 22 unique command-reference sections | An exact set-parity test prevents one-sided catalogue changes without freezing the count | [Completed outcome](./plans/c1-command-catalogue.md) |

## I1 — Shipping and upgrade contracts disagree

Accepted [ADR 021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md)
still specifies four library collections, including `agent-memory-systems`, a
`kb/commonplace/.commonplace` marker, and marker-backed replacement of a clean
shipped tree. The [scaffold manifest](../../../src/commonplace/scaffold_manifest.py)
ships only notes, reference, and instructions. Init writes no marker and
preserves every differing existing target because it has no prior-version
baseline.

Most current surfaces already describe that implementation. [ADR
014](../../reference/adr/014-scripts-as-python-package-one-tree-model.md)
sets missing-files-only, non-destructive behavior and explicitly rejects
automatic synchronization. [ADR
037](../../reference/adr/037-promote-skills-into-runtime-surfaces-by-copying.md)
requires manual diff-and-merge for projected skills, and
[INSTALL.md](../../../INSTALL.md) says reruns acquire new scaffold files rather
than replace existing ones. ADR 021 remains the marker-backed replacement
witness. Architecture's former “re-sync” wording is now stale and no longer a
current witness.

Preserve-only reruns are the honest current and possible interim contract, but
they are not a credible terminal upgrade design for hundreds of framework-owned
files. The revised plan first settles product ownership, then records prior
framework hashes so an upgrade can replace unchanged framework files, preserve
and report locally edited forks, never overwrite user-owned paths, and report
upstream removals for deliberate pruning. T1 supplies migration inputs; it does
not build a parallel upgrade mechanism.

## I2 — The install projection breaks the library graph

The source notes, reference, instructions, and shared types validate without
missing-link warnings. Copying selected content under `kb/commonplace/` while
keeping shared types at `kb/types/` and omitting dependency collections breaks
otherwise valid paths:

| Installed surface | Files with broken links | Broken links | Failures |
|---|---:|---:|---:|
| `kb/commonplace/notes` | 146 | 462 | 0 |
| `kb/commonplace/reference` | 30 | 55 | 1 |
| `kb/commonplace/instructions` | 1 | 1 | 0 |
| `kb/types` | 4 | 14 | 0 |
| **Total** | **181** | **532** | **1** |

Resolved against their intended source targets, the 532 broken edges divide as
follows:

| Intended target class | Broken edges |
|---|---:|
| `kb/sources/` | 335 |
| `kb/agent-memory-systems/` | 101 |
| `kb/types/` | 34 |
| `kb/agentic-systems/` | 31 |
| `kb/notes/` | 9 |
| `kb/reference/` | 5 |
| `src/` | 5 |
| `kb/articles/`, `kb/reports/` | 6 |
| `AGENTS.md`, `kb/tasks/` | 4 |
| `kb/log.md` | 1 |
| `kb/work/` | 1 |

The sole failure is the installed copy of [the tag semantic contract
proposal](../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md):
its repository-relative collection-local type pointer remains under absent
top-level `kb/reference/types/` instead of projecting under
`kb/commonplace/reference/types/`. Shared type contracts exhibit the inverse
depth change when they link back into notes or reference.

The resolution plan treats init as a build projection with an explicit
source-to-installed map, an explicit disposition for omitted dependencies, one
code-safe link rewriter, and a strict packaged-wheel acceptance test. The
[installed-product decision](./installed-product-edition-decision.md) compares
the self-contained, thin, curated, and hybrid options and recommends one hybrid
evidence-local edition: complete methodology, a fixed-point closure of tracked
source analyses, and immutable publication links for omitted review corpora
and other first-party material. It also selects three logical roots, five
per-file ownership classes, one compiler, and hash-aware upgrades. A successor
installation ADR must adopt that packet before implementation. Wheel and
editable-source installation must invoke the same compiler-like projection.

### Reproduction

From the Commonplace source root:

```bash
audit_root=$(mktemp -d /tmp/commonplace-contract-audit-XXXXXX)
commonplace-init --root "$audit_root" --name audit
cd "$audit_root"
commonplace-validate kb/commonplace/notes
commonplace-validate kb/commonplace/reference
commonplace-validate kb/commonplace/instructions
commonplace-validate kb/types
```

These counts were reproduced at the audited commit on 2026-08-27. Missing links
are warnings, so exit status alone cannot establish product integrity. The
reference collection exits nonzero for the projection-specific type pointer.

## V1 — “Validate all” still means one depth

[commands.md](../../reference/commands.md) no longer publishes its former
hardcoded collection list. The promoted [validation
skill](../../instructions/cp-skill-validate/SKILL.md) remains the operative
`all` procedure and loops over `kb/*/COLLECTION.md`. A pristine install now
contains eight `COLLECTION.md` files; the glob sees five and misses all three
nested shipped collections.

[project_paths.py](../../../src/commonplace/lib/project_paths.py) already has a
recursive `collection_dirs()`, but no `all` procedure consumes it. It also
filters out any path containing `types`, so it returns seven of the eight install
collections, and in the source checkout it can include the deliberately ignored
`kb/work/dialectical-sample` fixture. The full-validation enumerator therefore
must include the I3 disposition of global types, prune
`.commonplace-validation-ignore`, carry repository-relative paths rather than
basenames, continue after failures, and own one aggregate result.

Collection discovery is not the whole current `types` target: support type
specs under paths such as `kb/reports/types/` and `kb/tasks/types/` may have no
enclosing collection. `all` must cover those exactly once after collection
runs. V1 should expose a stable Python aggregate result before rendering text,
with optional JSON as a secondary interface. It must also run the existing
direct-child-of-`kb/` landing check once, without silently imposing that landing
rule on nested library collections.

## I3 — Installed routing and material topology disagree

[kb/types/COLLECTION.md](../../types/COLLECTION.md) correctly explains that
`kb/types/` is both global in reach and a collection by contract. The generated
[AGENTS.md.template](../../../AGENTS.md.template) now defines collections by a
local contract and no longer contains the former “not a collection” witness.
`collection_dirs()` still excludes `kb/types/`, so material contract and
runtime discovery continue to disagree.

[collection_conformance.py](../../../src/commonplace/review/collection_conformance.py)
also excludes every contract under a `types` path even though accepted [ADR
060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md)
places `kb/types/` inside collection-conformance review.

The template routes `kb/sources/` and `kb/work/` as writable collections and
requires their contract to be read before writing. The scaffold now installs a
sources contract and landing. It still creates only the work directory, so a
workshop write can hard-fail on a pristine install.

The selected topology makes sources and work genuine scaffolded user
collections, classifies types as the global type collection, and keeps
`kb/commonplace/` as a namespace rather than a collection. Extend the existing
`ScaffoldManifest` with role, owner, writability, source/projection, template,
upgrade, and logical-root data instead of creating a second topology inventory.
Runtime discovery still follows concrete `COLLECTION.md` files so user-created
collections remain visible.

## S1 — Snapshot immutability contradiction is resolved

[ADR 072](../../reference/adr/072-ingests-own-source-authority-and-snapshots-are-local.md)
supersedes ADR 045's placement and mutation exception. The tracked ingest owns
durable `genre`; a local snapshot may retain a provisional capture-time value,
but ingestion writes its closer-reading judgment only to the report. Because
the ingest checksum covers every snapshot byte, the snapshot now remains
whole-file immutable after capture.

The [sources collection](../../sources/COLLECTION.md), [snapshot
type](../../sources/types/snapshot.md), [ingest-report
type](../../sources/types/ingest-report.md), and
[cp-skill-ingest](../../instructions/cp-skill-ingest/SKILL.md) now agree on the
same boundary: snapshotting may create the ignored reading copy; ingestion
writes only the tracked report and verifies that the reading copy's checksum
did not change. The installed source template now projects this resolved
contract; I3 retains only its manifest and routing parity obligation.

## T1 — Tag completeness claims have incompatible scopes

The [tag-readme type](../../types/tag-readme.md) and current routing still use
unqualified “every note” language across collection-facing surfaces, while
generation and validation index one collection. The concrete witness remains
[trace-learning-techniques-in-related-systems.md](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md):
it carries `learning-theory` but none of the six children declared by
[learning-theory-README.md](../../notes/learning-theory-README.md). Validation
passes because it checks only notes. Under the proposed participating set, the
live reference proposal omitted by the complete `artifact-analysis` head is a
second witness.

No local wording repair can close this finding. It requires a semantic model,
logical-root ownership, exact membership resolution, consumer convergence,
published projection behavior, and a breaking corpus migration. Those design
and implementation responsibilities have therefore transferred to the
[tag-contract convergence workshop](../tag-contract-convergence/README.md).
The two reference proposals remain unadopted inputs, not authority.

This parent workshop retains only the audit finding, its witnesses,
installed-product dependencies I1/I2/I3/V1, and the [handoff and closure
tracker](./plans/t1-tag-scope.md). T1 closes here when the owner workshop's
adoption tests show that every exact-membership consumer uses the same
projection-relative set and the original witnesses no longer contradict the
implemented contract. The later agent navigation experiment is follow-up, not
a closure gate unless an adopted decision makes a retrieval-performance claim.

## E1 — Native Windows support and promoted procedures disagree

Native Windows and PowerShell remain supported, and the manifest now promotes
ten skills. [cp-skill-health-check](../../instructions/cp-skill-health-check/SKILL.md)
improved its uv-tool step and removed the old `direnv`, `bash -c`, and active
`.venv/bin` instructions. Its layout, projection, and legacy-residue checks
still use unpaired Bash constructs such as `test`, `&&`, `||`, and `sed`.
[cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) still uses the
GNU-sensitive `xargs -r` guard, while
[cp-skill-validate](../../instructions/cp-skill-validate/SKILL.md) still embeds a
Bash `if`/`for` program.

The [execution-channel
workshop](../execution-channel-compatibility/README.md) remains the owner, but
its runtime evidence remains Linux-only. Its [2026-08-27 promoted-skill
audit](../execution-channel-compatibility/e1-promoted-skill-rebaseline-2026-08-27.md)
now derives the selected set from `MANIFEST.promoted_skills`, uses the current
user-level uv-tool model, and classifies every executable locus. The plan
retains Windows, uses V1's package-owned target dispatcher, moves connect's
deterministic tag/path enumeration behind T1's resolver, pairs only true
preflight checks, consolidates byte-level and orchestration work behind shared
package/runtime operations, and adds native-Windows CI and runtime evidence.

## F1 — Generic freshness acceptance is withdrawn

**Resolved 2026-08-19.** [ADR
065](../../reference/adr/065-publish-only-supported-freshness-transitions.md)
amends accepted [ADR
052](../../reference/adr/052-general-freshness-store-review-first-migration.md):
v1 has only `review-pair` targets, so review finalization owns baseline creation
and replacement. Generic initial acceptance may return only with an adopted
non-review target and its complete registration contract.

The package entry point, CLI module, unreachable transition, empty target-kind
set, rejection-only tests, JSON schema, and current-facing documentation were
removed together. Status, acknowledgement, retirement, capture finalization,
and the generic tables remain. The C1 parity test now observes 22 published
commands and 22 unique command sections, so a one-sided reintroduction fails.

The dated [freshness-module review](../freshness-module-review/findings.md) and
historical artifact-freshness implementation documents retain the old command
only as explicitly marked evidence. The active collection-freshness proposal
describes initial registration as future work rather than claiming that a
generic command ships.

## M1 — One representation migration retains live residue

Only Areas/Topics remains active. Global note status and path-valued types
closed on 2026-08-27; text promotion and the snapshot pointer closed on
2026-08-19:

| State | Current contract | Guidance disposition |
|---|---|---|
| **Resolved** | [ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md), [note-base.schema.yaml](../../types/note-base.schema.yaml), and [note.schema.yaml](../../types/note.schema.yaml) remove global note `status` | Current guidance now teaches the actual shared fields and no maturity ladder. A parsed-frontmatter guard confines `status` to declared ADR and article lifecycle values; a scoped guidance check rejects retired current wording. |
| Open | [ADR 004](../../reference/adr/004-replace-areas-with-tags.md) replaces `areas` and Topics footers | [areas-exist-because-useful-operations-require-reading-notes-together.md](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) teaches the retired mechanism as current |
| **Resolved** | [collections-and-types.md](../../reference/collections-and-types.md) and the resolver require path-valued `type:` | Current examples use resolvable paths. A parsed scan validates every visible active artifact's frontmatter and the inventoried executable examples; only ADR 012 retains the pre-path enum as dated history. |
| **Resolved** | [snapshot.schema.yaml](../../sources/types/snapshot.schema.yaml) requires `type: kb/sources/types/snapshot.md` | [snapshot.md](../../sources/types/snapshot.md) now gives the same path-valued default. A schema-derived parity test covers the type spec, collection Types menu, and snapshot skill; existing emitter tests cover X and GitHub captures. |
| **Resolved** | [note-base.schema.yaml](../../types/note-base.schema.yaml) requires `description` and `type`, while convert writes `type: kb/types/note.md` and never grants verification | The text contract, root and reference guides, and five conceptual notes now require complete note frontmatter in their text-promotion passages. A schema-derived check covers the authoritative text contract and converter template; a scoped regression scan rejects retired shortcuts in all eight current consumers. |

The [migration plan and manifest](./plans/m1-migration-residue.md) records all
four completed packets and their guards. The Areas/Topics packet still must
distinguish explicit history from current instructions and add a narrow guard
for the retired executable form after the tag-contract outcome supplies its
replacement.

## C1 — Command-catalogue parity is resolved

The scripts table in [pyproject.toml](../../../pyproject.toml) publishes 22
`commonplace-*` entry points, and [commands.md](../../reference/commands.md) now
has 22 unique matching command sections. The quote-verification section
documents its targets, `--show-matches`, result classes, and exit behavior.

[test_command_catalogue_integrity.py](../../../tests/commonplace/docs/test_command_catalogue_integrity.py)
parses both live surfaces, rejects duplicate command headings, and asserts exact
set equality without fixing the expected count. F1's later removal changed both
sets together, so catalogue parity remained intact without changing the guard.

## Root causes

### 1. The installed form is not an acceptance-test target

Init tests prove selected files were copied. They do not operate the generated
KB as a consumer would. A non-identity projection needs product tests over its
output, including warnings, rather than only unit tests over its copier.

### 2. Decisions and migrations lack consumer manifests

ADRs 004, 021, 044, and 045 changed concepts with many readers. Primary
implementations moved while navigation, examples, skills, or installed
projections retained the old contract. Naming one operativity path did not
inventory independent consumer classes, generated forms, or installed
migrations; the workshop-wide contract-change gate addresses that process gap.

### 3. Scope is prose reimplemented as traversal

“Every tagged note,” “all collections,” and “supported on Windows” are scope
claims. Validator, glob, site hook, and promoted procedure each select their
own set rather than consuming a shared declaration. T1 also showed that an
exact membership shortcut and a task-level discovery stop are different
permissions; using “search” for both hides the boundary the mark actually
checks.

### 4. Presence is mistaken for capability

A console entry point, help page, copied skill, or installed contract proves
presence, not that any legal invocation or supported execution channel works.

## Implementation order

1. **Rebaseline at a named commit — complete for this cycle.** The witness
   ledger classifies open, partial, stale, new, and count-only changes at
   `6660bd2a`.
2. **Installed-product recommendation — complete.** The decision packet selects
   the hybrid evidence-local edition, logical-root boundaries, ownership
   classes, projection policy, and terminal upgrade policy. Adopt it in the
   successor installation ADR before coding the projection.
3. **Implement minimal I3 plus V1.** Extend `ScaffoldManifest` enough to expose
   roles and roots, keep runtime discovery contract-based, and land the
   recursive structured validation suite. V1 may truthfully report current
   product failures; that makes it I2's acceptance harness.
4. **Implement I2.** Build one compiler-like projection for wheel and editable
   sources, disposition every dependency edge, and test the actual fresh
   install through V1.
5. **Finish I3 and I1.** Complete templates and routing parity, then supersede
   ADR 021 with ownership-aware upgrade behavior. Preserve-only may be an
   explicitly temporary release constraint, not the terminal architecture.
6. **Continue E1; independent M1 packets are complete.** Implement the
   manifest-derived promoted-skill audit's dispositions and gather native
   Windows evidence. Global-note-status and path-valued-type cleanup closed on
   2026-08-27; Areas/Topics still waits for tags.
7. **Consume the tag owner outcome.** The tag-contract workshop implements its
   semantic/resolver, consumer, and migration phases against the settled
   installed-product boundary. This workshop then rechecks T1's original
   witnesses.
8. **Finish Areas/Topics and the process guard.** Promote the contract-change
   implementation gate, record outcomes, and delete this workshop.

## Workshop-wide durable outcome

Closing the individual contradictions is insufficient if a later
cross-cutting contract change again inventories only one consumer. The
[contract-change gate plan](./plans/contract-change-gate.md) must promote a
small implementation/review instruction covering:

- authoritative declaration and declared scope;
- current operative consumer classes;
- generated and projected forms;
- fresh-install consequence and existing-install migration;
- acceptance test and drift guard;
- explicitly historical retained witnesses.

This is a review aid, not a general semantic-contradiction detector and not an
ADR file inventory.

## Exclusions and non-findings

- Linking vocabulary, direction, grammar, and enforcement remain in the
  [linking workshop](../linking-contract-consistency/README.md); lineage carrier
  and invalidation conflicts remain in the [lineage
  ledger](../lineage-mechanisms/current-contradictions.md).
- `kb/work/dialectical-sample/COLLECTION.md` is beneath a tracked validation
  ignore marker. It is not a live nested-collection defect, but collection
  enumeration must prune it.
- Deferred collection freshness, generic lineage storage, semantic-link
  validation, and similar missing consumers remain design gaps until live
  contracts choose incompatible behavior.
- Historical ADR context is not current authority. ADR 021 remains included
  because it is accepted and its Decision and Consequences still make
  present-tense guarantees.
- The freshness module review's remaining implementation findings are outside
  this contract workshop. Its generic-accept finding is resolved here; its
  dated reproduction remains historical evidence.

## Closure condition

This workshop closes only after every plan's acceptance criteria are satisfied
in durable system artifacts or the finding is explicitly transferred to a
named owner with those criteria, the contract-change gate is promoted, and all
transferred findings are rechecked against their original witnesses. The
workshop must then be deleted so it does not become a second authority surface.
