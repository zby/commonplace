# System contract consistency audit

**Audit date:** 2026-07-29

**Scope:** current Commonplace contracts outside the linking and lineage domains

## Verdict

Commonplace has ten confirmed cross-surface contradictions outside the ones already owned by the [linking-contract-consistency](../linking-contract-consistency/README.md) workshop and the [lineage ledger](../lineage-mechanisms/current-contradictions.md). The highest-risk cluster is not an isolated stale sentence: the source-to-install projection has no single contract shared by the accepted shipping decision, scaffold manifest, generated control plane, installed files, upgrade behavior, and validation workflow.

A pristine `commonplace-init` currently produces a KB whose shipped collections contain **433 broken local links**, whose shared global types add **14 more**, and whose reference collection gains one projection-specific validation failure. The advertised `all` validation procedure does not inspect those nested shipped collections. This makes the installed form both less coherent than the source form and capable of reporting completion without examining the broken surface.

The remaining contradictions repeat three mechanisms:

- an exception or migration landed in its primary schema or decision record but not in every consumer;
- a scope word such as “all,” “every,” or “supported” is broader than the mechanism that enforces it;
- a command or workflow was exposed before its accepted input domain existed.

## Standard used

A **confirmed contradiction** needs two current, operative witnesses that cannot both be followed over the same declared scope. An advertised command with an empty legal input domain also qualifies. A missing future feature, an explicitly historical statement, or an unimplemented proposal does not.

Priorities mean:

- **P0** — a fresh install or completion signal is unsound;
- **P1** — a current supported workflow, trusted mark, or system-definition contract can direct incompatible actions;
- **P2** — a narrower current reference or authoring surface teaches a rejected or invalid shape.

## Findings at a glance

| ID | Priority | Contradiction | Immediate consequence | Existing owner |
|---|---|---|---|---|
| I1 | P0 | The accepted shipping decision promises a refreshable, marker-guarded four-collection library; init installs three collections, no marker, and never refreshes changed files | Package upgrades leave old library and skill files installed indefinitely | none |
| I2 | P0 | Source-valid relative paths are copied into a different installed topology without translating or shipping their targets | A pristine install introduces 447 broken local links and one type-resolution failure | none |
| V1 | P0 | `validate all` means one-level collection globbing, while installed collections live two levels deep | The normal completion path skips the entire shipped library | [validation](../validation/README.md), but this installed-layout case is not recorded there |
| I3 | P1 | The generated control plane calls sources/work collections without installing contracts, and calls `kb/types/` not a collection while installing its contract | Read-before-write is impossible for two routed destinations; the global type collection is misclassified | none |
| S1 | P1 | Snapshots are both immutable and mutable in place, while ingest both must and must not perform the mutation | Ingestion cannot obey its collection, type, and skill contracts together | none |
| T1 | P1 | Tag completeness is stated and routed across collections but checked and generated within one collection | A validated mark can falsely license a reader to stop searching | [tag-scope proposal](../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md) |
| E1 | P1 | Native Windows is supported, but promoted procedures contain unpaired POSIX-only commands | Selected skills can be non-operative on a declared channel | [execution-channel compatibility](../execution-channel-compatibility/README.md) |
| F1 | P1 | `commonplace-freshness-accept` is published for non-review targets, but no non-review target kind is accepted | Every invocation reaches an unconditional unsupported-kind error | [freshness module review](../freshness-module-review/README.md) |
| M1 | P2 | Accepted metadata/type migrations coexist with current docs that prescribe the retired representation | Agents can author schema-invalid or semantically retired artifacts from live guidance | none |
| C1 | P2 | The CLI reference and executable catalogue enumerate different command surfaces | A shipped command is absent from its claimed reference while an unusable one is documented | none |

## I1 — The accepted shipping and upgrade contract is not the initializer's contract

The accepted [ADR 021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) fixes all of the following as the installed shape:

- four library collections under `kb/commonplace/`, including `agent-memory-systems`;
- a `kb/commonplace/.commonplace` version/drift marker;
- overwrite of a clean shipped tree on upgrade, with refusal only when marker-backed drift is detected.

The current [scaffold manifest](../../../src/commonplace/scaffold_manifest.py) copies only `notes`, `reference`, and `instructions`. It installs no marker. The [initializer](../../../src/commonplace/cli/init_project.py) preserves every existing differing file; it has no prior-version baseline with which to distinguish a practitioner edit from an old package version. [ADR 037](../../reference/adr/037-promote-skills-into-runtime-surfaces-by-copying.md) explicitly says projected skill upgrades require manual diff-and-merge. [INSTALL.md](../../../INSTALL.md) accurately narrows re-init to picking up *new* scaffold files, while the current [architecture reference](../../reference/architecture.md) still says `commonplace-init` can re-sync the library on upgrade.

These are not alternative layers of one behavior. A file that changed between package releases is “different” in the installed tree, so init preserves it whether or not the user ever touched it. `pip install --upgrade` plus `commonplace-init` therefore cannot perform the update that ADR 014 and ADR 021 describe.

**Needed decision:** either implement marker-backed canonical refresh, including an explicit policy for locally changed shipped files and projected skills, or amend the accepted decision and every upgrade claim around a deliberately manual update mechanism. Independently decide whether `agent-memory-systems` remains in the shipped bundle; current code and current architecture silently disagree with the accepted ADR.

## I2 — The source-to-install path projection produces a broken library

ADR 021's [path-audit appendix](../../reference/adr/021-shipping-model-path-audit-option-e.md) explicitly did not scan `kb/types/`. It also made two conditions of the chosen layout: ship `agent-memory-systems`, and replace primary links into omitted `sources` with external citations. Neither condition holds in the current scaffold.

The consequences are measurable in a pristine generated project:

| Surface | Source checkout | Pristine installed shape |
|---|---:|---:|
| `notes` | 321 files, 0 warning-bearing notes, 0 failures | 134 warning-bearing notes, 405 missing-link warnings, 0 failures |
| `reference` | 123 files, 0 warning-bearing notes, 1 pre-existing filename failure | 21 warning-bearing notes, 27 missing-link warnings, 2 failures |
| `instructions` | 83 files, 0 warning-bearing notes, 0 failures | 1 warning-bearing note, 1 missing-link warning, 0 failures |
| shared `kb/types` | 8 files, 0 warnings, 0 failures | 4 warning-bearing type specs, 14 missing-link warnings, 0 failures |

The 405 broken note links divide into 246 links to omitted sources, 116 to omitted agent-memory-system reviews, 23 to omitted agentic-system analyses, 19 to global types whose relative depth changed, and one to omitted task content. The additional installed-reference failure is [text-contract-profiles.md](../../reference/text-contract-profiles.md): its source-valid file-relative pointer to a global type resolves under `kb/commonplace/types/` after shipping, even though ADR 021's own rule says global type pointers must stay repository-relative `kb/types/...` paths.

The shared type contracts show the complementary failure. Files such as [instruction.md](../../types/instruction.md), [note.md](../../types/note.md), [review-gate.md](../../types/review-gate.md), and [type-spec.md](../../types/type-spec.md) stay at top-level `kb/types/`, but their `../notes/...` and `../reference/...` markdown links assume the source checkout. In an install, those targets moved under `kb/commonplace/`. A future user file at the old relative target could silently turn a broken library link into a link to unrelated user content.

**Needed outcome:** make the generated install a tested product shape. A clean-install acceptance test should validate every shipped collection and shared type with zero projection-introduced failures or warnings. The shipping contract must then choose, per dependency class, to ship the target, translate the link, replace it with an external citation, or remove the dependency. Source-tree validation cannot establish installed-tree integrity after a non-identity path transform.

### Reproduction

From the Commonplace source root:

```bash
audit_root=$(mktemp -d /tmp/commonplace-contract-audit-XXXXXX)
commonplace-init --root "$audit_root" --name audit
cd "$audit_root"
commonplace-validate commonplace/notes
commonplace-validate commonplace/reference
commonplace-validate commonplace/instructions
commonplace-validate kb/types
```

The counts above came from this procedure on 2026-07-29. Link-health findings are warnings, so the notes, instructions, and types commands still exit successfully; reference fails for the projection-specific type pointer plus the source checkout's existing 71-character ADR filename.

## V1 — “Validate all” does not mean all collections

The promoted [validation skill](../../instructions/cp-skill-validate/SKILL.md) implements `all` with `kb/*/COLLECTION.md`. That works only for collections one level below `kb/`. Installed library collections live at `kb/commonplace/{notes,reference,instructions}/`, so the glob skips every one of them. This is especially consequential because it hides I2 from the normal full-validation path.

The [commands reference](../../reference/commands.md) gives a second meaning of the same operation: a hardcoded loop over `types notes reference instructions agent-memory-systems sources`. In the source checkout this omits the current `agentic-systems` and `articles` collections. In an installed project it again names user-root paths rather than the nested shipped collections. The source repository currently has nine top-level collection contracts; neither procedural enumeration is the authoritative set across both supported layouts.

**Needed outcome:** one collection enumerator should own full validation. The implementation already has recursive collection discovery in [project_paths.py](../../../src/commonplace/lib/project_paths.py); expose or consume that behavior rather than serializing collection names or depth assumptions in instructions. Add a test that `all` covers every discovered collection exactly once in both source and generated-install fixtures.

## I3 — The installed collection topology contradicts its control plane

The generated [AGENTS template](../../../AGENTS.md.template) defines a collection as a `kb/` subtree with a local `COLLECTION.md`, tells agents to read that contract before writing, and routes both `kb/sources/` and `kb/work/` as collections. It simultaneously calls `kb/types/` a “global type surface, not a collection.”

The manifest does the inverse in material form:

- it copies [kb/types/COLLECTION.md](../../types/COLLECTION.md), whose first paragraph explicitly says the directory is a collection;
- it creates `kb/sources/` and `kb/work/` without either collection contract;
- it supplies source type specs whose extension instructions depend on the sources collection's Types menu.

The contradiction reaches executable procedures. [cp-skill-snapshot-web](../../instructions/cp-skill-snapshot-web/SKILL.md) says the snapshot type comes from `kb/sources/COLLECTION.md`; [ingest-directory](../../instructions/ingest-directory.md) names that file as a prerequisite; [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) hard-fails any writable collection without a contract. A pristine install therefore cannot satisfy its read-before-write rule for sources or workshops, while it is instructed to ignore the contract that actually governs the global types it received.

**Needed outcome:** derive the control-plane routing table and starter contracts from one declared installed topology. If sources and work are writable collections, scaffold contracts adequate to their actual type and link semantics. If they are support directories until a user opts in, stop routing them as collections and make source skills own a contract-independent default. Correct the `kb/types/` classification either way.

## S1 — Snapshot immutability has an undeclared write exception

The [sources collection contract](../../sources/COLLECTION.md) says snapshots preserve captured content, “Don't edit” them, and later states categorically that snapshots are immutable. [ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md), the [snapshot type](../../sources/types/snapshot.md), and the [ingest-report type](../../sources/types/ingest-report.md) instead require ingestion to correct `genre` in place when closer reading changes the classification. ADR 045 acknowledges that the snapshot is no longer fully immutable.

The ingest skill supplies a third incompatible boundary: [cp-skill-ingest](../../instructions/cp-skill-ingest/SKILL.md) says its direct output is only the `.ingest.md` report and repeats “Write only the `.ingest.md` report directly,” while its loaded type contract can require a snapshot edit. A validation step conditionally mentions a snapshot the run edited, but no step authorizes or performs the required correction.

**Needed outcome:** choose and name the mutable envelope. The minimal resolution is to define content immutability separately from a small mutable capture-metadata set, revise the collection's categorical language, and explicitly authorize the ingest skill to update `genre`. If whole-file immutability is load-bearing, move corrected classification to a mutable companion and change ADR 045's single-ground-truth decision.

## T1 — Tag completeness has incompatible scopes

This contradiction is already fully evidenced in the active [tag-scope proposal](../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md):

- the [tag-readme type](../../types/tag-readme.md) says a marked page links “every” note carrying the tag;
- the generated listing and validator operate within the tag README's collection;
- the site hook routes matching tags across collection boundaries;
- the root control-plane search recipe scans several collections, while [navigation.md](../../reference/navigation.md) uses a notes-only recipe.

The live witness is [trace-learning-techniques-in-related-systems.md](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md), which carries `learning-theory` but none of the children declared by [learning-theory-README.md](../../notes/learning-theory-README.md). Validation passes because it checks only the notes collection; the unqualified reader-facing coverage claim is false at the wider scope other consumers imply.

**Needed outcome:** adopt one of the proposal's scoped designs. The non-negotiable invariant is narrower: no mark may license skipping a search wider than the scope the validator actually checked.

## E1 — Supported native Windows and promoted procedures disagree

[INSTALL.md](../../../INSTALL.md) and the generated control plane explicitly support native Windows and PowerShell. The current manifest promotes eight skills unchanged into runtime surfaces. At least three contain unpaired POSIX-only procedures:

- [cp-skill-health-check](../../instructions/cp-skill-health-check/SKILL.md), the recovery path for environment failures, depends on `test`, shell command substitution, POSIX `.venv/bin`, `direnv`, and `bash -c`;
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) uses `xargs -r` and calls the guard load-bearing;
- [cp-skill-validate](../../instructions/cp-skill-validate/SKILL.md) implements its only `all` procedure as a Bash `if`/`for` program.

The issue is not that PowerShell spelling is absent from every historical example. These are current promoted instructions, copied as executable runtime authority onto a platform the installer declares supported. The [execution-channel workshop](../execution-channel-compatibility/README.md) now owns the broader solution space; the earlier focused [portability proposal](../self-improvement-cluster-operationalization/windows-portability-for-promoted-skills.md) records the same consumer/channel mismatch.

**Needed outcome:** complete that workshop's evidence gathering, then either provide portable entry points, channel-paired procedures, or channel-resolved installed artifacts. A support declaration must be tested against the procedures it delivers, not only against Python package installation.

## F1 — Generic freshness acceptance has an empty accepted domain

`pyproject.toml` publishes `commonplace-freshness-accept`. The [commands reference](../../reference/commands.md), [freshness architecture](../../reference/freshness-architecture.md), and [freshness schemas](../../reference/freshness-schemas.md) describe it as observation refresh or initial acceptance for non-review targets and say it rejects `review-pair`.

The live [transition implementation](../../../src/commonplace/freshness/transitions.py) defines `V1_ACCEPT_TARGET_KINDS = frozenset()`. `accept_target_observations()` first rejects `review-pair`, then rejects every target not in that empty set. There is no input for which the advertised transition can succeed.

This is not merely deferred generalization: the executable and its current reference are shipped before the first supported consumer exists. The [freshness module review](../freshness-module-review/README.md) already owns the finding; older findings in that workshop were not imported here because current code has changed.

**Needed outcome:** remove the command and current-facing documentation until a non-review target kind ships, or ship that target and its end-to-end acceptance path. Keeping a deliberately unusable executable as a placeholder makes `--help` indistinguishable from implemented capability.

## M1 — Accepted representation migrations left active consumers behind

Several breaking migrations changed schemas and much of the corpus without invalidating every current reader or authoring surface:

| Adopted/current contract | Conflicting current surface |
|---|---|
| [ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md) deletes global note `status`; [note.schema.yaml](../../types/note.schema.yaml) rejects it | [available-types.md](../../reference/available-types.md) says the base note has status; the [notes README](../../notes/README.md) promises every note a seedling-to-current maturity mark; [document-system-README.md](../../notes/document-system-README.md) still names a global status ladder |
| [ADR 004](../../reference/adr/004-replace-areas-with-tags.md) replaces `areas` with freeform `tags` and removes Topics footers | [areas-exist-because-useful-operations-require-reading-notes-together.md](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) says the current collection assigns areas and prescribes `areas:`/Topics behavior; [stale-indexes-are-worse-than-no-indexes.md](../../notes/stale-indexes-are-worse-than-no-indexes.md) teaches the same retired mechanism |
| [type-loading.md](../../reference/type-loading.md) requires a path-valued `type:` and says bare enum values fail | [document-types-should-be-verifiable.md](../../notes/document-types-should-be-verifiable.md) uses `type: note`, `type: spec`, and `type: structured-claim` as current executable examples; [storage-architecture.md](../../reference/storage-architecture.md) still describes collection-local lookup with global fallback instead of lexical path resolution |
| [snapshot.schema.yaml](../../sources/types/snapshot.schema.yaml) requires `type: kb/sources/types/snapshot.md` | The authoritative [snapshot type](../../sources/types/snapshot.md) tells authors to set `type: snapshot` |
| [note-base.schema.yaml](../../types/note-base.schema.yaml) requires both `description` and `type`; the [convert skill](../../instructions/cp-skill-convert/SKILL.md) writes both | [text.md](../../types/text.md) says adding frontmatter with at least a description promotes text to note |

Each row is narrow, but together they show a migration failure mode: the changed representation has no complete consumer inventory. Current documents that validate cleanly can still teach the previous system because semantic validation does not compare examples or descriptive claims with schemas.

**Needed outcome:** every breaking ADR needs a checked migration manifest covering schema/code, type specs, collection contracts, skills, current reference, navigation heads, examples, templates, and tests. Add focused lexical sentinels for retired load-bearing identifiers until the migration closes; do not attempt a general semantic-contradiction engine.

## C1 — The command catalogue drifts from the executable surface

The scripts table in [pyproject.toml](../../../pyproject.toml) publishes 22 `commonplace-*` entry points. [commands.md](../../reference/commands.md), whose declared role is the reference for commands shipped by `llm-commonplace`, has 21 command sections. It omits the working `commonplace-verify-quotes` command while documenting the unusable generic accept command from F1.

This is the lowest-priority finding because omission alone does not break execution. It is still a current catalogue inconsistency and an inexpensive detector for broader drift.

**Needed outcome:** assert parity between console-script names and command-reference sections, with an explicit allowlist only for intentionally internal commands. Capability status should be recorded separately from mere executable presence.

## Root causes

The ten findings reduce to four systemic causes.

### 1. The installed form is not an acceptance-test target

Most path, collection, validation-depth, and upgrade contradictions are invisible in the source checkout. Init tests assert that selected files exist and copies match their sources; they do not operate the generated KB as a consumer would. A non-identity projection needs product-level tests over the output, not only unit tests over the copier.

### 2. Decisions and migrations do not carry a consumer manifest

ADR 004, ADR 021, ADR 044, and ADR 045 each changed a concept with many readers. Their primary implementation moved, but navigation, examples, skills, or installed projections retained the old contract. The linking workshop found the same mechanism in another domain.

### 3. Scope is encoded in prose and reimplemented by traversal choices

“Every tagged note,” “all collections,” and “supported on Windows” are scope claims. The validator, glob, site hook, and promoted procedure each select their own scope rather than consuming a shared declaration.

### 4. Presence is mistaken for capability

A console entry point, a help page, or a copied skill proves discoverability, not operativity. Generic freshness accept has no accepted target; Windows skills have no executable channel; an installed type contract can be present while its rationale links are broken.

## Resolution order

1. **Repair the installed product boundary.** Reconcile ADR 021, the manifest, current architecture, and upgrade semantics; add a pristine-install acceptance fixture; decide the shipped dependency set; eliminate projection-introduced link and type failures.
2. **Make full validation truthful.** Discover collections recursively in both source and install layouts, and make clean-install validation part of release verification.
3. **Resolve the snapshot write boundary.** This is a small three-surface contradiction with a direct authoring consequence.
4. **Finish already-owned P1 work.** Tag scope, execution channels, and generic freshness accept already have evidence and owners; carry their outcomes back into durable contracts and code.
5. **Run the representation-migration sweep.** Remove the status/areas/bare-type residue and add targeted migration guards.
6. **Add cheap parity checks.** Console scripts versus command docs, generated routing versus installed contracts, promoted skills versus declared channels, and type-spec examples versus schema-valid fixtures.

## Exclusions and non-findings

- Linking vocabulary, direction, grammar, and enforcement remain in the [linking workshop](../linking-contract-consistency/README.md); lineage carrier and invalidation conflicts remain in the [lineage ledger](../lineage-mechanisms/current-contradictions.md). They were used as a method model, not recounted as new findings.
- The nested `kb/work/dialectical-sample/COLLECTION.md` is under a tracked validation-ignore marker. It is an intentional workshop fixture, not a live nested-collection failure. A proposal that still calls it a current validation failure is stale, but that proposal drift is not itself elevated here.
- Deferred collection-level freshness, generic lineage storage, semantic link validation, and similar missing consumers are design gaps until two live contracts choose incompatible behavior.
- Historical context inside ADRs was not treated as current. ADR 021 is included because its status is accepted and its Decision/Consequences sections make present-tense installed guarantees that current reference still partly repeats.
- The older freshness review's snapshot-pruning concern was rechecked and excluded: current code now prunes unreferenced snapshots. Only generic accept remains live.
- A first validator run from the source checkout against an absolute path in `/tmp` exposed a repository-root assumption and traceback. That invocation crossed project roots and was discarded; all reported install counts were rerun from inside the generated project.

## Closure condition

This workshop closes when every finding is either resolved in durable system artifacts or transferred to a named active workshop/proposal with an owner and acceptance criteria. The report itself should not become a second authority surface: after resolution, delete this workshop and retain only the ADRs, reference updates, tests, or transferable notes produced from it.
