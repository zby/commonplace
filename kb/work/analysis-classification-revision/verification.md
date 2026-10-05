# Implementation verification and full-run handoff

## Outcome and gates

The classification revision is implemented and verified. State: **awaiting
full-run evidence**. The operator authorized the implementation commit on
2026-10-05. G1–G3 are satisfied; the implementation commit supplies G4's method
revision. G5 has not been attempted. No external analysis run, publication,
integration or comparison refresh was performed.

The [decisions](./decisions.md) fix the representation and semantics;
[ADR 107](../../reference/adr/107-classify-memory-by-scoped-findings.md) retains
the implemented architectural choice. The [semantic cases](./semantic-cases.md)
retain all 13 synthetic acceptance cases and their evidence limits.

## Changed surfaces

- Canonical profile type and schema: revision-2 scoped units and single-value
  findings replace independently authored value/evidence copies.
- Shared records, memory and epistemic types, nine job packets and overview:
  all ten axes retain natural units, supported facts and named unresolved parts.
  Independent epistemic properties remain separate. The shared contract delivers
  the operative self-improvement attribution test.
- Runtime comparison reader, projection and scheduled-profile acceptance:
  revision 2 is mandatory for new workflow profiles; frozen revision 1 remains
  readable. Structure, controlled values, references, bounded negatives and
  incompatible applicability assertions are checked without classifying prose.
- Matrix CSV, table, statistics, comparison README, taxonomy and landscape
  instructions: retain version, unit findings, coverage rationale and local
  evidence. Statistics separate revisions and do not upgrade weak duplicate
  witnesses or turn incomplete/inapplicable coverage into absence.
- Tests: revision-2 schema, canonical records, unions, exports, strength,
  applicability, historical reading, actual packet composition, scheduled-job
  rejection and synthetic publication with positive-plus-unresolved coverage.

No source-acquisition, preparation, publication identity or general scheduling
redesign was necessary. Record-member schemas remain unchanged because their
existing source-native fields can express the revised distinctions. Manifest,
set and finalization consumers use the shared validator and retain identity and
byte-pin checks; they do not need a frozen-data migration.

## Multi-consumer change packet

### Declaration, scope and diagnostics

The profile type, shared records and schema declare the contract. Runtime
`validate_comparison` enforces structure, reference resolution and incompatible
combinations; job acceptance enforces revision 2. Semantic verifiers judge the
actual warrant, inventory completeness and concealed gaps. Neither schema
validation nor a canonical ID proves a positive or negative claim.

The packet-composition tests inspect actual absolute declared inputs and
read-first loading paths, rather than following incidental definition or
workshop links. New rules reach source authors, reconciliation, record/profile
verifiers and public synthesis through their existing dependencies. No workshop
file is a runtime input.

### Discovery and rescan

Exact-name searches inspected code, tests, scripts, local method/types,
comparison instructions and reference readers. Final `rg -l` rescan counts:

| Pattern | Scope | Files |
|---|---|---:|
| `memory-comparison` | src, tests, scripts, analysis collection, agentic systems, reference | 90 |
| `write_agency` | src, tests, scripts, kb | 127 |
| `read_back_signal` | src, tests, scripts, kb | 120 |
| `agent-memory-profile.md` | src, tests, scripts, kb | 37 |
| `agentic-analysis-records.md` | src, tests, scripts, kb | 55 |

These are file counts, not consumer counts. Remaining old shapes are historical
retained/probe/audit/proposal evidence, deliberate revision-1 tests and the
marked compatibility reader/schema branch. ADRs 093 and 103 are explicitly
marked amended instead of rewriting their historical rationale.

### Consumer disposition

| Consumer class | Disposition |
|---|---|
| Validators/resolvers | Shared dual reader; current-write gate at scheduled profile acceptance. |
| Schemas/derived copies | Profile schema permits exactly the two carrier revisions; runtime adds semantic-shape checks. |
| Emitters | Profile packet emits v2; matrix serializer derives unions and preserves units, notes and revision. |
| Migration scripts | None: historical reclassification is not authorized or warranted. |
| Projected skills | Canonical analysis and landscape skill symlinks remain unchanged; no new skill name or promotion status. |
| Collections/types/templates | Canonical local types updated; governing collection scope unchanged. |
| Control-plane templates | No identifier, routing or installed skill-set change; no template change required. |
| Reference/ADRs | Comparison interface documented; ADR 107 amends earlier classification decisions. |
| Tests/fixtures | New current-workflow fixtures are v2; real historical-reader fixtures remain v1. |
| Published views | Reader interfaces updated; existing publications left unchanged pending separately authorized refresh. No URL or redirect changes. |

No frozen member bytes were rewritten, so no manifest hash was re-pinned.
Method files remain covered by publication's existing method-path checks. No
relocations, accidental identity matches, new corpus predicate or exclusion set
were introduced. Current-set enumeration still supplies matrix/site population
and excludes archives and local state. Existing selected consumers fail on
missing/invalid required sets rather than silently dropping them.

### Installed delivery

`commonplace-source` reports `/home/zby/llm/commonplace/src/commonplace`, the
editable command environment for this checkout. Analysis skills remain
repo-local; generic init does not install an external-analysis collection.
The relevant installed product is therefore unchanged scaffold/pointer delivery,
not a migrated profile copied into a new project.

Temporary-project probe at `/tmp/commonplace-classification-install-OpjUVw`:

1. `commonplace-init --root <scratch>` created the standard scaffold and pointers.
2. `commonplace-init --root <scratch> --check` passed.
3. Repeating init preserved existing scaffold files; repeating `--check` passed.
4. From scratch, `commonplace-validate notes`, `reference`, `instructions` and
   `landings` passed with zero failures or warnings.

A scratch `commonplace-validate types` returned `No notes matched target.`
(exit 1): this scaffold has no local type definitions. It is not proof of type
validation or an installation defect. The repository `types` check separately
passed for 34 files, and schema/member/loading tests cover analysis contracts.
No `commonplace-init` was run in this checkout.

## Verification results

Coordinator checks after integration:

| Command/check | Result |
|---|---|
| `uv run pytest` | 1107 passed; 64 slow tests deselected by project configuration. |
| `uv run pytest -m slow` | All 64 slow tests passed. Together both selections cover all 1171 collected tests. |
| Targeted slow workflow/member/finalization selection | 59 passed before the complete slow selection. |
| `uv run ruff check .` | All checks passed. |
| `git diff --check` | Passed. |
| Explicit `commonplace-validate` for all 20 changed/new canonical Markdown files | Success; zero failures or warnings per file. |
| Explicit validation of workshop README, plan, decisions and semantic cases | Success; zero failures or warnings. |
| `commonplace-validate kb/agentic-system-analyses/retained/dynamic-cheatsheet` | Success; frozen revision-1 set remains valid. |
| `commonplace-validate types` | Success; 34 files, zero failures or warnings. |
| Real current-set `load_results` / CSV / statistics | Frozen Dynamic Cheatsheet loaded as revision 1 without reclassification. |

Tests demonstrate accepted positive findings beside unresolved included units,
rejection of malformed/reference-defective or structurally incompatible claims,
and retained absence/coverage/strength distinctions. The legal but unsupported
request-only `synthesize` fixture intentionally passes structural checks and
has an expected semantic-verifier blocker. It is not an executed model verdict;
source truth remains the independent verifier's responsibility.

## Independent semantic review

Worker preflight returned `COMMONPLACE_WORKER_OK`; exposed agent-depth and
nesting limits were unknown. Workers used fresh sessions and disjoint write
scopes. Two read-only semantic integration reviews were delegated; the review
workers did not modify files or launch workers.

The first review returned five findings:

| Finding | Repair and final review disposition |
|---|---|
| F1: axis rationale lost in projection/export | Added axis notes to both revision projections, CSV and rendering; resolved. |
| F2: contradictory whole-axis inapplicability accepted | Added prerequisite checks for positive/unresolved trace learning and direction; complete bounded negatives remain admissible; resolved. |
| F3: wholly inapplicable inventory counted as complete empty profile | Reject that `known` shape; defensive statistics preserve inapplicability; resolved. |
| F4: self-improvement attribution test missing from operative packets | Shared contract now supplies it; ten actual composition paths test delivery; resolved. |
| F5: acceptance assertions exceeded synthetic evidence | All 13 cases now retain source-native fixture facts, expected semantic dispositions and honest enforcement limits; resolved. |

The final independent review inspected the integrated surfaces and judged all
13 synthetic semantic dispositions faithful under their specified facts. It
reported no remaining consequential defect. It independently loaded the real
frozen current set as revision 1. This is review of the revision and fixture
judgments, not an independent external-source analysis or efficacy experiment.

The revision-1 validator is not byte-for-byte behaviorally identical: canonical
ID and reverse applicability checks are tighter. The real retained consumer
passes. No affected historical consumer requiring a broader shim was found;
old write-agency values are not reinterpreted. Matching producing-method
contracts remain necessary for historical semantic conformance questions.

## Diff and authority boundaries

The coordinator reviewed the tracked implementation diff and the new synthetic
case/consumer tests, decisions, ADR and semantic record. No retained analysis,
probe, source snapshot or old run was changed. Existing workshop navigation
edits and probe files were preserved. A concurrent untracked
`kb/reference/proposals/publishing-analyses-with-unresolved-issues.md` appeared
during implementation; it was left untouched and is not part of this work.

## Operator handoff

No unresolved semantic or compatibility decision blocks implementation. The
operator authorized the implementation commit on 2026-10-05. Its Git commit
identifies the method revision; no self-referential hash is embedded here. The
method must be committed before standard isolated preparation. Stage complete
explicit implementation artifacts only, preserving unrelated changes and the
original probe evidence. For broader link discovery around ADR 107, `cp-skill-connect`
is optional follow-up, not a runtime or full-run prerequisite.

After a method commit and separate launch authorization, the revised procedure
is ready for a fresh standard isolated Dynamic Cheatsheet run against
source revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, unless the operator
chooses another target. Use the normal analysis skill and code-scheduled
workflow, a new run ID and the committed method. Do not resume or repair
`AAS-2026-10-05-dynamic-cheatsheet-1599d863aa7f-01` or change its method commit.

Publication/integration and comparison refreshes require separate applicable
authority. Retain the fresh run's actual outcome and disposition any findings
before workshop closure. No claim that the revision improves full-run behavior
is established yet.
