# Establish the planning-free review baseline

## Commission and completion boundary

The operator asked to finish the separation of planning-free operations from
workflows that choose the work, using the existing explicit-plan path before
adding a framework. Establish one fixed editing pass and one report-only
criterion as independent operations. Keep unsettled selection stops and exact
final-publication approval. Leave review-result typing, planning-stability
experiments and broader composition for later work.

This change establishes command, instruction and regression-test boundaries.
It does not establish model judgment quality. No new paid worker call or live
artifact publication is authorized or performed as part of this change.

## Implemented boundary

- New revision runs require `--plan FILE` or `--assess`. Bare repeats retain the
  recorded mode. Changed artifact text requires a new choice, preventing a
  repeat after publication from silently starting assessment.
- A fixed plan owns purpose, protected claims, passes and scopes. Combining
  fixed-plan execution with CLI purpose/defend options is rejected rather than
  silently ignoring them. The existing plan schema and depth rules remain.
- Fixed-plan execution constructs no assessment request. Editors in both modes
  receive `execute-a-revision-pass.md`, not the assessment/dispatch procedure.
- Fixed-plan publication binds the plan, execution instruction, selected pass
  definitions, relevant profiles, brief and accepted outputs. Changes to the
  assessment instruction, unselected pass text or unused profile do not
  invalidate it. Assessment-led runs still bind their planning inputs.
- One gate id over one artifact remains report-only. A failure does not select
  more work or start editing. Fresh results still skip redundant calls.
- Multiple fixed passes remain supported, but are composition, not evidence
  for the reliability of an individual operation. `--assess` and `full-pass`
  remain available as explicitly planning-containing paths.

## Consumer change packet

| Contract surface | Treatment |
|---|---|
| Authoritative declaration | ADR 127, CLI mode selection and revision execution; operator recipe in the simplification-pass guide. |
| Scope and enforcement | CLI requires a mode before opening a new revision; the fixed-plan branch never constructs the assessment request. Worker instructions constrain semantic scope; code does not prove semantic compliance. |
| Consumer classes | Updated CLI parser/help/options/report, worker request construction, execution/planning instructions, guide, command reference, architecture, ADR and workshop priorities. Tests cover revision and single-criterion review. No schema, type, root rule, control-plane template or promotion interface changes. |
| Inventory searches | `rg -l 'run revise' --glob '*.py' --glob '*.md' --glob '*.yaml' src tests kb` found 13 files during implementation; `rg -l 'revise-an-article-or-note' kb/instructions` found one direct composition sibling. The other consumers were found through source constants and the scoped reference/workshop search. |
| Byte-pinned consumers | `rg -l --hidden --no-ignore '"job": "assessment"\|revise-an-article-or-note.md' kb/reports/state/review/runs/revise` found two retained files. Run records are historical: no rewrite, deletion or re-pin. Instruction changes generate new worker identities when those inputs are used. Existing publication contexts cannot authorize the new context. |
| Old spellings | Searched `run revise`, `revise-an-article-or-note`, `named_plan`, assessment and plan-option consumers. Current teaching must name `--assess`; bare repeat commands remain valid because mode is recorded. |
| Generated and projected forms | Editable command and library load source changes directly. No skill stub, entry-point, scaffold layout, generated index or redirect change. |
| Fresh installation | Scratch-project probe uses bare installed commands and shared library files; fixed empty plan must finish without workers. |
| Existing installations and clones | No data migration. Old runs without `mode` require explicit `--plan` or `--assess`; callers keep their recorded files. Init refresh must leave project content unchanged. |
| Diagnostics | Missing mode and conflicting fixed-plan CLI constraints fail before workers; reports expose `mode`. Tests exercise both diagnostics. |
| Acceptance probe | Fresh scratch init, repeat init, missing-mode refusal, empty fixed-plan execution and bare replay, with zero launches and unchanged target. |
| Drift guard | CLI consumer tests capture actual worker inputs, forbid assessment-request construction in fixed mode, and exercise replay/publication after planner-only changes. Single-criterion test checks one result and no edit even for a failing judgment. |
| Historical witnesses | Older trial records and prior design sections remain historical. Current workshop headers point to this boundary. No retained run is silently adapted. |
| Identity conventions and exclusions | Existing artifact-hash run paths, pass discovery by `effort`, pair identities and freshness predicates remain. The new execution instruction has no `effort`, so it is not a selectable pass. |
| Relocation effects | None: no artifacts relocated. |

## Verification

Focused fake-harness selection: 51 tests passed. It covers fixed scope and
protected-claim delivery, absence of an assessment artifact, no planner request,
private preparation, publication from replay, explicit mode switching, and
report-only gate failure. Existing selection, brief-conflict, validation and
publication-boundary tests also pass in that selection.

Final development selection: **343 passed**, using
`uv run pytest tests/commonplace/general tests/commonplace/review_workflows tests/commonplace/relocation tests/commonplace/docs -m '' -q`.
This includes the additional checks that missing legacy mode or missing captured
plan never fall back to assessment. No slow tests are declared in these suites;
headless runtime and analysis implementation were not changed. Ruff passed.
Explicit validation of all 11 changed Markdown files returned zero failures
and zero warnings. The command/reference rescan found only explicit new-run
modes, valid recorded-mode repeats and historical descriptions.

The installed-project probe at `/tmp/review-fixed-plan-probe-z1UX9b` passed
fresh initialization, refresh and `--check`; a bare new revision failed with
exit 2; an empty fixed plan and its bare repeat both completed with zero
launches, no assessment artifact and a clean checkout. This probes installation
and routing, not editing judgment. The earlier published article and theory
note still match their approved candidate hashes.

These Python tests check workflow code; they are not steps added to live
note-review or editing workflows. Unrelated ingest, validation and workshop
changes in the shared checkout are outside this commission and remain untouched.
The command reference has a disjoint pre-existing ingest edit; only its review
section belongs to this change.

## Next evaluation

For a separately commissioned paid trial, fix one artifact, purpose, pass,
scope and protected claims before launch; do not ask an assessor to choose
them. Inspect the diff for scope and meaning preservation, retain the worker's
report and failure cases, and publish only after explicit approval. Evaluate
one criterion independently in the same way. Planning stability and combined
workflows need their own evidence; neither fake-worker replay checks nor the
two earlier assessment-led Sol trials close that question.
