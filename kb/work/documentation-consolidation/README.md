# Documentation consolidation

Posed by the operator on 2026-11-18 and refocused on 2026-11-19.

## Motivation

Documentation grows, goes out of date, and misleads. Agents rarely read free-standing reference files, and humans find long reference manuals inconvenient when deciding what to do. Adding or reorganizing prose files does not fix that.

Every document needs a clear answer to two questions:

1. **What exact task does this document serve, and for whom?** If no concrete task needs it, retire it after rehoming anything unique.
2. **Where does that task activate?** Move rules, procedures, and tool references onto the **activation path** — the surface already loaded at the point of use (just as `cp-skill-write` names `commonplace-validate` at its validation step).

## Activation paths and document roles

- **Agent activation path.** Rules, procedures, and tool invocations belong where the triggering task loads them: a skill body, a collection contract, a type spec, `AGENTS.md` (only for cross-task rules with no single trigger), `--help`, a validator message, a test, or a comment beside the constrained code. A pointer in `AGENTS.md` that says "for task X, read Y" is a skill in the wrong place.
- **Human overview.** Assume the human can use an agent, and that the agent knows how to retrieve current operational details (via skills, `--help`, and live code). Aim human-directed docs at stable, higher-level concepts that let a person choose a request or decide whether to run a workflow — what it does, what it may publish, what it costs, and when it needs a decision — rather than volatile flags, inventories, or implementation detail.
- **Reference and architecture.** Kept only where code, `--help`, and ADRs do not cheaply supply the answer (cross-component invariants, composed current state across amended ADRs, or declared project frames). Prose copies of behaviour drift and should be cut once their unique detail sits on an activation path or in `--help`.

Use the [reference collection's economy tests](../../reference/COLLECTION.md#text-contract-and-fidelity) and the [seven-case documentation study](../../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) as the baseline. Coordinate with [ADR routing](../adr-routing/README.md) where the needed context is a binding ADR; do not build a parallel ADR index here.

## Current order of work

1. **Review, revise, and command activation paths (done — `1149e4305`).** Added promoted `cp-skill-review` and `cp-skill-revise` (with capability/limitation boundaries), extracted Pi reviewer setup into `kb/instructions/run-review-from-pi.md`, removed the review-guide pointers from `AGENTS.md` and `AGENTS.md.template`, shrank `README-REVIEW-SYSTEM.md` (63 KB → 6.0 KB) to a high-level human overview, moved `commands.md`'s unique details into live `--help`, and shrank `commands.md` (43 KB → 4.2 KB) to a checked command catalogue wired from both `AGENTS.md` and `AGENTS.md.template`.
2. **First audit of reference docs by task and activation path (`535020d1f`, `d439edf34`; dispositions still open).** Moved orphaned authoring, delegation, analysis-method, and continuation rules onto their activation paths (`cp-skill-write`, `kb/types/collection-contract.md`, `AGENTS.md`, `cp-skill-add-collection`, `maintain-analysis-method.md`, and code comments in `revise.py`), fixed verified stale claims across 15 `kb/reference/` documents, and trimmed redundant/speculative prose. Kept system-coupled worked-case and declaration notes as valid miscellaneous reference notes.
   - The [reflective-system classification](../../theory/evidence/commonplace-as-a-reflective-system.md) introduces the tag-readme improvement-loop mapping, now in `kb/theory/evidence/`; direct citations to its findings remain. The analysis design brief’s quality standards are in `kb/agentic-system-analyses/COLLECTION.md` and its method-evolution priorities in `maintain-analysis-method.md`.
3. **Human entry points (done).** Promoted `getting-started.md` and `getting-started.brief.md` to `kb/reference/`, linked them from `kb/reference/README.md` and `kb/index.md`, and rewrote `kb/reference/README.md` around the high-level human-doc principle (replacing the stale 155-line "How to" mechanics and drifting 35-line ADR list).
4. **Skill pruning (after reference triage).** Review existing skills and remove any that add trigger noise without earning a dedicated activation path.
   - **Validation:** use `commonplace-validate` at the write, conversion, or promotion step that knows the target. The standalone command still serves explicit checks; no default skill trigger is needed.
   - **AutoReason:** keep `cp-skill-revise-autoreason` available for explicit trials in this checkout. The trials did not show enough benefit to offer it by default in consuming projects.
   - **Multistage writing:** keep the procedure reachable from `cp-skill-write` and `cp-skill-revise`, without a separate installed trigger. The operator recalls that its notes developed too many detailed threads instead of sustaining one main claim. The November 13 run produced the [revision-order note](../../theory/resolve-revision-choices-before-polishing-text-that-depends-on-them.md); acceptance shows that the run finished, not that the result was more focused than an ordinary draft. Tuning is deferred. If revisited, start with a note the operator found diffuse and identify which threads its main claim could do without.

## Takeover: decide what earns a page

On 2026-11-20 the operator asked to resume the reference cleanup and suggested a home for explanations that are useful in Commonplace's own terms before a more general claim is worth formulating. The November 19 analysis is a candidate list, not a disposition: check current callers and the passage each needs. A reference-index entry shows discoverability, not need. Do not treat a prose trim as settling whether to keep the page.

Recent decisions provide three controls: routine navigation went back to agent instructions and the tag contract; instruction generation lost its standalone page but kept the setup/runtime distinction in architecture; link vocabulary stayed because callers need a shared meaning that local permission alone cannot supply.

**Pilot in use:** `kb/reference/case-studies/` holds ordinary reference notes under the [reference contract](../../reference/COLLECTION.md#text-contract-and-fidelity), not a new collection or type.

First case: [Where change candidates come from in Commonplace](../../reference/case-studies/where-change-candidates-come-from-in-commonplace.md). The [connect-report mining proposal](../../reference/proposals/periodic-connect-report-mining.md) uses its distinction between noticing a problem and turning it into a candidate.

Keep [the declared frame](../../reference/commonplace-declared-frame.md) as the reference for who and what counts as part of Commonplace, and [the program objective](../../reference/commonplace-declared-frame.md#what-commonplace-chooses-to-count) for what counts as progress.

Keep [Commonplace as an instrument](../../reference/case-studies/commonplace-as-an-instrument.md) in `case-studies/`, not among the declarations. Its reader is a maintainer deciding what operating this KB has shown and what still needs testing. The [ablation proposal](../../reference/proposals/ablation-baselines-for-the-declared-objective.md) uses it to distinguish two questions: do the parts work together here, and does using them beat doing the same work without them?

Collection prototypes: authors choosing a starting contract now reach the installed templates from the add-collection skill. Readers asking what survives copying use [ADR 069](../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md). No separate inventory. For control-plane goals, the project’s root instructions supply the goals, the install guide tells the operator how to fill them in, and [ADR 014](../../reference/adr/014-scripts-as-python-package-one-tree-model.md#decision) carries forward the reason goals precede skill selection. No separate reference page or new ADR.

Scenario architecture: the [write-a-note scenario](../../../tests/scenarios/write-a-note.md) distinguishes a write from optional link discovery. The evaluation procedure consumes that scenario directly; the reference page duplicated the worked example and installed layout.

Workflow handoffs: [storage roles](../../reference/storage-architecture.md#storage-roles) distinguishes a named output another invocation may consume from the producer’s private replay records. The handoff test belongs there rather than on a separate page.

The [ordinary-note status case](../../reference/case-studies/what-would-status-current-assert.md) records why collection-relative endorsement was rejected for `current`. It preserves the design question without turning the outcome into a rule for future fields.

Design rationale: keep [the recovery guide](../../reference/design-rationale-management.md) separate from content routing. A maintainer reconsidering an implementation needs to find its reasons and distinguish a recorded choice from one inferred after the fact.

## Files in this workshop

- [reference-analysis.md](./reference-analysis.md) — empirical audit of the 30 top-level `kb/reference/` documents (duplication, unique content, stale statements, live consumers).

## What closes this workshop

- Every retained reference document has an explicit task it serves, and stale copies are removed or moved onto their activation paths.
- Agent tasks reach their needed rules and commands along their natural activation paths without being told a reference file's name; human overviews stay short and decision-oriented.
- Any skill removals decided in step 4 are applied or split out, and untested cases are recorded. Opening this workshop does not authorize an unchecked repository-wide deletion sweep.
