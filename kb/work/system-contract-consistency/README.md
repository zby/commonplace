# System contract consistency workshop

**Opened:** 2026-07-29

**Last full recheck:** 2026-08-23

**Last plan refresh:** 2026-08-27 (T1 tag semantics and navigation boundary)

**State:** seven findings remain open; C1 and F1 were resolved on 2026-08-19,
and S1 was resolved on 2026-08-23. Plans and outcomes are recorded in the
[plan index](./plans/README.md). T1's design was refreshed after a separate tag
semantic contract and grounded search literature landed; implementation status
is unchanged.

**Scope:** current Commonplace contracts outside the linking and lineage
domains

## Current verdict

Seven of the ten confirmed contradictions remain open. C1 closed by documenting
the omitted executable and enforcing exact catalogue parity. F1 closed by
withdrawing a generic freshness command that had no legal target. S1 closed
when ADR 072 moved durable genre authority to the tracked ingest and restored
whole-file immutability for local snapshots. Three other findings received
partial repairs at one edge, but both conflicting witnesses remain live:

- E1: the health check gained one PowerShell-paired step and dropped obsolete
  activation instructions, but several promoted procedures are still
  POSIX-only;
- V1: the skill and command reference now agree, but they agree on the same
  one-level glob that omits nested shipped collections;
- I3: the global type collection now explains its dual role, but the generated
  control plane still denies that role and installed sources/work still lack
  contracts;

The install-integrity result worsened from 447 broken links on 2026-07-29 to
**516** on 2026-08-19: 502 in the three shipped library collections and 14 in
the shared global types. The installed reference collection also had one
projection-specific type-resolution failure. The advertised full-validation
procedure still skips all three shipped collections, so it can report
completion without examining this broken surface.

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
| I2 | P0 | Source-valid local paths are copied through a topology change without shipping or translating their targets | A pristine install has 516 broken links and one type failure | [Install projection integrity](./plans/i2-install-projection-integrity.md) |
| V1 | P0 | Both documented `all` procedures use `kb/*/COLLECTION.md`, while installed library collections are nested below `kb/commonplace/` | The normal completion path skips the shipped library | [Validate all](./plans/v1-validate-all.md) |
| I3 | P1 | Generated routing treats sources/work as collections without contracts and treats contract-bearing `kb/types/` as not a collection | Read-before-write is impossible at two routed destinations and discovery excludes a real collection | [Installed topology](./plans/i3-installed-topology.md) |
| S1 | P1 | **Resolved 2026-08-23:** the tracked ingest owns durable `genre`; a local snapshot's optional genre is provisional and its bytes remain immutable after capture | ADR 072 removes the mutation exception and aligns the collection, types, and ingest write boundary | [Completed outcome](./plans/s1-snapshot-mutation-boundary.md) |
| T1 | P1 | Tag coverage is stated and routed beyond one collection but generated and checked within one collection | A validated mark can falsely license a reader to skip the exact membership query that would expose omissions | [Tag scope](./plans/t1-tag-scope.md) |
| E1 | P1 | Native Windows is supported, but promoted skills retain unpaired POSIX-only commands | Selected recovery and authoring procedures are non-operative on a declared channel | [Windows execution](./plans/e1-windows-execution.md) |
| F1 | P1 | **Resolved 2026-08-19:** the unsupported generic accept entry point, transition, schema, and current-facing claims were withdrawn | ADR 065 requires a concrete non-review target before the surface can return | [Completed outcome](./plans/f1-freshness-accept.md) |
| M1 | P2 | Three accepted representation migrations retain live guidance; the text-promotion and snapshot-pointer packets closed on 2026-08-19 | Agents can still author schema-invalid or semantically retired artifacts from current docs | [Migration residue](./plans/m1-migration-residue.md) |
| C1 | P2 | **Resolved 2026-08-19:** 21 console scripts now have 21 unique command-reference sections | An exact set-parity test prevents one-sided catalogue changes | [Completed outcome](./plans/c1-command-catalogue.md) |

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
witness. Separately, [architecture.md](../../reference/architecture.md) still
makes the broader claim that init can “re-sync” the library on upgrade.

The selected plan preserves current behavior rather than inventing an
unimplemented drift protocol: settle I2's exact bundle, mark ADR 021
superseded, restate the surviving namespace decision, and state one
missing-files-only transition and manual upgrade procedure across ADRs, code,
tests, install docs, and architecture.

## I2 — The install projection breaks the library graph

The source notes, reference, instructions, and shared types validate without
missing-link warnings. Copying selected content under `kb/commonplace/` while
keeping shared types at `kb/types/` and omitting dependency collections breaks
otherwise valid paths:

| Installed surface | Files with broken links | Broken links | Failures |
|---|---:|---:|---:|
| `kb/commonplace/notes` | 150 | 468 | 0 |
| `kb/commonplace/reference` | 23 | 33 | 1 |
| `kb/commonplace/instructions` | 1 | 1 | 0 |
| `kb/types` | 4 | 14 | 0 |
| **Total** | **178** | **516** | **1** |

Resolved against their intended source targets, the 516 broken edges divide as
follows:

| Intended target class | Broken edges |
|---|---:|
| `kb/sources/` | 321 |
| `kb/agent-memory-systems/` | 112 |
| `kb/agentic-systems/` | 29 |
| `kb/types/` | 29 |
| `kb/notes/` | 9 |
| `kb/reference/` | 5 |
| `AGENTS.md`, `tasks/`, `src/`, `kb/articles/`, `kb/reports/` | 10 |
| `kb/log.md` | 1 |

The sole failure is [text-contract-profiles.md](../../reference/collection-prototypes.md):
its file-relative `type:` pointer reaches global `kb/types/` in the source but
resolves to absent `kb/commonplace/types/` after installation. Shared type
contracts exhibit the inverse depth change when they link back into notes or
reference.

The resolution plan treats init as a build projection with an explicit
source-to-installed map, an explicit disposition for omitted dependencies, one
code-safe link rewriter, and a strict packaged-wheel acceptance test. The
current-system recommendation is to retain the three documented library
collections and replace omitted first-party and source edges with stable public
or canonical external targets. Expanding the bundle remains coherent, but must
be chosen explicitly before the I1 successor ADR.

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

These counts were reproduced on 2026-08-19. Missing links are warnings, so exit
status alone cannot establish product integrity. Reference exits nonzero only
for the projection-specific type pointer; the previously reported source
filename failure no longer exists.

## V1 — “Validate all” still means one depth

[commands.md](../../reference/commands.md) no longer contains its stale
hardcoded collection list. It now matches the promoted [validation
skill](../../instructions/cp-skill-validate/SKILL.md): both loop over
`kb/*/COLLECTION.md`. That removes the previous second meaning but preserves the
core gap. A pristine install contains seven `COLLECTION.md` files; the glob sees
four and misses all three nested shipped collections.

[project_paths.py](../../../src/commonplace/lib/project_paths.py) already has a
recursive `collection_dirs()`, but no `all` procedure consumes it. It also
filters out any path containing `types`, so it returns six of the seven install
collections, and in the source checkout it can include the deliberately ignored
`kb/work/dialectical-sample` fixture. The full-validation enumerator therefore
must include the I3 disposition of global types, prune
`.commonplace-validation-ignore`, carry repository-relative paths rather than
basenames, continue after failures, and own one aggregate result.

Collection discovery is not the whole current `types` target: support type
specs under paths such as `kb/reports/types/` and `kb/tasks/types/` may have no
enclosing collection. `all` must cover those exactly once after collection
runs. It must also run the existing direct-child-of-`kb/` landing check once,
without silently imposing that landing rule on nested library collections.

## I3 — Installed routing and material topology disagree

[kb/types/COLLECTION.md](../../types/COLLECTION.md) now correctly explains that
`kb/types/` is both global in reach and a collection by contract. The source
control plane and architecture agree. The generated
[AGENTS.md.template](../../../AGENTS.md.template) still says it is “not a
collection,” while `collection_dirs()` excludes it.

[collection_conformance.py](../../../src/commonplace/review/collection_conformance.py)
also excludes every contract under a `types` path even though accepted [ADR
060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md)
places `kb/types/` inside collection-conformance review.

The template also routes `kb/sources/` and `kb/work/` as writable collections
and requires their contract to be read before writing. The scaffold creates the
directories but installs neither `COLLECTION.md` nor a landing for either.
Write and connect can therefore hard-fail on a pristine install. Snapshot-web's
newly hedged contract pointer does not supply the missing contract that ingest
and type extension still require.

The selected topology makes sources and work genuine scaffolded user
collections, classifies types as the global type collection, and keeps
`kb/commonplace/` as a namespace rather than a collection. A package-owned
machine-readable declaration must drive or be parity-checked against manifest,
routing, discovery, top-level landing coverage, and smoke tests.

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
did not change. I3's future installed source template must project this resolved
contract rather than revive the old exception.

## T1 — Tag completeness claims have incompatible scopes

The active [tag-scope
proposal](../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md)
and the newer [semantic contract for tags and tag
heads](../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md)
remain unadopted. The [tag-readme type](../../types/tag-readme.md) and current
routing use unqualified “every note” language across collection-facing
surfaces, while generation and validation index one collection.

The live witness is
[trace-learning-techniques-in-related-systems.md](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md),
which carries `learning-theory` but none of the six children declared by the
notes collection's
[learning-theory-README.md](../../notes/learning-theory-README.md). Its
`covered_by` claim is therefore false at cross-collection scope while validation
passes because it checks only notes. Under the proposed participating set, the
live reference proposal omitted by the `artifact-analysis` head is the second
violation.

The selected scope remains one namespace per KB root, with membership claims
ranging over explicitly participating library collections in the concrete
projection. A shared resolver drives validation, generated augmentation,
connect, recipes, and every exact-membership skip rule. Host and vendored roots
remain independent, and shared `kb/types/` admits no tags because it has no
single root owner.

The semantic contract now states what the mechanism means. Assigning a tag
asserts that an artifact belongs to a reusable candidate set for a recurring
information need. It does not assert that every query should load every member.
The resolver recovers exact membership; a canonical head supplies stable
definition and contextual routing; task-level search may find relevant material
outside one tag or rank its members for the current query. A `complete` or
`covered_by` mark may license skipping only the exact membership operation it
replaces. It cannot certify that broader discovery is complete.

The grounded navigation corpus now bounds that distinction. [Pirolli's
information-foraging account](../../sources/pirolli-proximal-information-scent-distal-content.ingest.md)
models selection of unseen content from proximal cues. [Teevan and
colleagues](../../sources/teevan-perfect-search-engine-orienteering.ingest.md)
observed human searchers combining contextual local steps with direct jumps.
[Tombros and
Sanderson](../../sources/tombros-sanderson-query-biased-summaries.ingest.md)
found better human relevance judgments from query-biased summaries than from a
static surrogate. [Milo's contextual-map account](../../sources/nick-milo-mocs-definition.ingest.md)
and the [Luhmann Archive's selective-entry-point
record](../../sources/luhmann-archive-schlagwortregister.ingest.md) separately
bound the curated-head comparison. These are human, practitioner, and
historical sources. They motivate an agent-side comparison but do not establish
LLM behavior or choose a resolver presentation.

The implementation plan still moves the 20 existing per-tag heads to canonical
`kb/tags/` paths and adds a twenty-first `trace-learning` head. That tag remains
the source for website navigation and the derived matrix Boolean, with the
review contract enforcing its evidence requirements. Redundant source-family
tags are removed, and source and installed projection fixtures guard the
boundary. The combined adopting ADR must also settle the semantic proposal's
head, provisional-vocabulary, reuse-check, tag-relation, and result-presentation
choices.

No T1 implementation has landed: no adopting ADR, shared resolver,
participation declarations, `kb/tags/` collection, canonical-head relocation,
or consumer migration exists. T1 still consumes I3's root and collection
topology, I2's installed bundle, I1's upgrade semantics, and V1's truthful full
check. Its [refreshed plan](./plans/t1-tag-scope.md) treats an agent navigation
trial as follow-up evidence rather than a structural closure gate unless the
future ADR claims a retrieval-performance improvement.

## E1 — Native Windows support and promoted procedures disagree

Native Windows and PowerShell remain supported, and the manifest now promotes
nine skills. [cp-skill-health-check](../../instructions/cp-skill-health-check/SKILL.md)
improved its uv-tool step and removed the old `direnv`, `bash -c`, and active
`.venv/bin` instructions. Its layout, projection, and legacy-residue checks
still use unpaired Bash constructs such as `test`, `&&`, `||`, and `sed`.
[cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) still uses the
GNU-sensitive `xargs -r` guard, while
[cp-skill-validate](../../instructions/cp-skill-validate/SKILL.md) still embeds a
Bash `if`/`for` program.

The [execution-channel
workshop](../execution-channel-compatibility/README.md) remains the owner, but
its earlier project-venv premise is stale under the current user-level uv-tool
installation model and its evidence is Linux-only. The plan retains Windows,
uses V1's package-owned target dispatcher (including `all`), replaces connect's
pipeline with a runtime-native algorithm, pairs the pre-command health checks,
audits all nine promoted skills and their execution declarations, and adds
native-Windows CI and evidence.

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
and the generic tables remain. The C1 parity test now observes 21 published
commands and 21 unique command sections, so a one-sided reintroduction fails.

The dated [freshness-module review](../freshness-module-review/findings.md) and
historical artifact-freshness implementation documents retain the old command
only as explicitly marked evidence. The active collection-freshness proposal
describes initial registration as future work rather than claiming that a
generic command ships. The shared `kb/work/README.md` still has a stale
one-line freshness-module summary because it already contained unrelated
uncommitted edits; that navigation-only cleanup remains pending rather than
sweeping another change into this outcome.

## M1 — Three representation migrations retain live residue

Three audited rows remain active. The text-promotion and snapshot-pointer rows
closed on 2026-08-19:

| State | Current contract | Guidance disposition |
|---|---|---|
| Open | [ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md) and [note.schema.yaml](../../types/note.schema.yaml) remove global note `status` | The type-reference exposition sweep corrected the former catalogue, notes landing, document-system landing, and workshop-layer opening; the directory-scoped-type note and a full present-tense consumer sweep remain. |
| Open | [ADR 004](../../reference/adr/004-replace-areas-with-tags.md) replaces `areas` and Topics footers | [areas-exist-because-useful-operations-require-reading-notes-together.md](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) teaches the retired mechanism as current |
| Open | [collections-and-types.md](../../reference/collections-and-types.md) and the resolver require path-valued `type:` | The type-reference exposition sweep corrected storage architecture and consolidated the reference model; [document-types-should-be-verifiable.md](../../notes/document-types-should-be-verifiable.md) and related type-ladder notes still use current bare-type examples. |
| **Resolved** | [snapshot.schema.yaml](../../sources/types/snapshot.schema.yaml) requires `type: kb/sources/types/snapshot.md` | [snapshot.md](../../sources/types/snapshot.md) now gives the same path-valued default. A schema-derived parity test covers the type spec, collection Types menu, and snapshot skill; existing emitter tests cover X and GitHub captures. |
| **Resolved** | [note-base.schema.yaml](../../types/note-base.schema.yaml) requires `description` and `type`, while convert writes `type: kb/types/note.md` and never grants verification | The text contract, root and reference guides, and five conceptual notes now require complete note frontmatter in their text-promotion passages. A schema-derived check covers the authoritative text contract and converter template; a scoped regression scan rejects retired shortcuts in all eight current consumers. |

The [migration plan and manifest](./plans/m1-migration-residue.md) records both
completed packets and their guards. The other rows remain starting witness sets
rather than complete inventories. Their packets must still distinguish
explicit history from current instructions and add narrow guards for the
retired executable forms.

## C1 — Command-catalogue parity is resolved

The scripts table in [pyproject.toml](../../../pyproject.toml) publishes 21
`commonplace-*` entry points, and [commands.md](../../reference/commands.md) now
has 21 unique matching command sections. The new quote-verification section
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
projections retained the old contract.

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

1. **Settle the installed-product inputs.** I3 defines the collection roles,
   discovery semantics, and machine-readable topology shape; I2 chooses which
   dependency classes ship and which receive explicit external projections.
   S1's source mutation boundary is already settled by ADR 072.
2. **Record the combined decision (I1).** The successor ADR marks ADR 021
   superseded and records the actual bundle, topology, and preserve-only upgrade
   semantics.
3. **Finish material topology (I3).** Scaffold sources/work contracts using the
   resolved ADR 072 boundary, apply I2's library routing, and align discovery
   and conformance review.
4. **Close the projection and test the packaged product (I2).** Translate every
   included edge and make unresolved dependencies fail release acceptance.
5. **Expose truthful full validation (V1).** Consume the same collection
   enumeration, retain orphan-type and top-level-landing coverage, and replace
   the shell loop.
6. **Land the other repairs.** T1 consumes the settled I3/I2/I1 product boundary
   and V1's truthful full check. Its adopting ADR reconciles the scope and
   semantic proposals, limits marks to exact-membership shortcuts, and keeps
   contextual head traversal distinct from task-level search. T1 then precedes
   M1's areas packet. E1 also consumes V1 and remains with the
   execution-channel workshop. I3 must copy S1's resolved source contract into
   the installed sources template.
7. **Finish the M1 sweep and cheap drift guards.** Retain focused parity and
   lexical checks at the boundaries that drifted.

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
named owner with those criteria. The workshop must then be deleted so it does
not become a second authority surface.
