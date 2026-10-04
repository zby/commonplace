---
description: "Proposal: one validation surface for analysts, acceptance and maintainers, with cross checks declared by document and directory types and resolved from the artifact graph instead of a job"
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Type-declared cross checks and one validation surface

`commonplace-analysis-check` and `commonplace-validate` serve the same
purpose: a deterministic, non-mutating check whose findings a writer repairs
before submission. They share the per-file pipeline and the quotation
matcher. They differ in where their context comes from, how they present
findings, and which unit they can check. This proposal records the option
space for closing that gap, and for letting types own the cross checks that
today live in framework code keyed by hardcoded type paths.

## Current state (as of 2026-10-04)

- `commonplace-analysis-check <run-state> <job> [draft]` reads the run's
  recorded definition, builds the named job without replay, and applies the
  job's validator to the draft ([ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md)).
  An analyst member's validator runs the full `commonplace-validate` file
  pipeline on the draft, then adds four run-context checks: record references
  resolve against the members accepted so far; `run-id` and
  `reviewed-boundary` match the run state and boundary; declared record IDs
  carry the analyst's prefix; and every attributed blockquote occurs exactly
  once in the frozen Git checkout or capture named by the run state. A
  wrapper adds a rule name and a repair sentence to each refusal. The command
  exits 0, 1 or 2 and appends counts to the job's scratch log. ADR 105 and the
  [acceptance-check plan](../../work/analysis-collection-split/reliability/analyst-acceptance-check-plan.md)
  both name integration with `commonplace-validate` as the later direction.
- `commonplace-validate` runs base, type-rule and schema checks per file
  ([validation contract](../validation-contract.md)). A directory with
  `ARTIFACT.yaml` also receives its set rule
  ([ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md)):
  member identity against the overview, record references across members,
  the amendment index and comparison references. The run-state type rule
  verifies a complete run end to end, including every member's quotations
  against the frozen source through the absolute `source.path` the run state
  records. The validator therefore already reads evidence outside the
  repository, anchored on the run-state artifact rather than on a working
  member.
- Quotation checking is one library with three resolvers. `verbatim` prose
  quotes resolve against the linked KB file. Ingest `## Quotes` blockquotes
  resolve against the name-paired, git-ignored snapshot pinned by
  `snapshot_sha256` ([ingest report](../../types/ingest-report.md)); a missing
  snapshot reports the extracts as unverified, never as passing. Analysis
  blockquotes resolve against the run's frozen source
  ([source contract](../../agentic-system-analyses/instructions/agentic-analysis-sources.md)).
  Standalone validation of an analysis member only shape-checks its
  blockquotes and warns, because the member alone names no source root.
- The imperative rules for the collection-local analysis types are framework
  Python in `validation.py`, registered under six hardcoded type paths. The
  live proposal on
  [generalized validation and imperative extension](./generalized-validation-invalidation-and-imperative-extension.md)
  defers a declarative dereferencing primitive until a collection-local type
  needs a check its schema and review criterion cannot enforce. The analysis
  member and set types are now that case, beside `tag-readme`.
- The boundary, synthesis and verification drafts carry no `type:`. Their
  required fields and sections are checked by job functions.
- The [analysis set type](../../agentic-system-analyses/types/agentic-system-analysis-set.md)
  admits only finished sets: a complete disposition requires six members and
  any other disposition exactly one. `ValidationRun` accepts byte overrides for
  any path, including a manifest, but no command exposes a draft override.

## Problem

Two check surfaces exist for one feedback loop. The analysis check obtains
its context from a job name: the job constructor supplies the run state,
boundary, sibling members and declaration prefix. The validator obtains its
context from the artifact graph: frontmatter, links, the containing
directory and name-paired files. The job route cannot serve a maintainer
who validates a retained member, and the artifact route cannot serve an
analyst who holds an unsubmitted draft. The two also disagree on severity
(refusals only against pass, warn, fail and info), on availability (a
missing source is a refusal in one and an unverified notice in the other)
and on presentation (rule and repair prefixes parsed from strings against
labelled findings and JSON diagnostics with stable IDs).

Separately, the checks that make an analysis member valid in its set are
properties of the member and set types, yet neither type can state them.
The type spec says in prose that quotations resolve and identities agree;
the enforcement sits in framework code the type author cannot see from the
spec, selected by type path.

## Options

### A. Fold the analysis check into the validator as a run-context mode

The validator gains an invocation that names a run state and a job, or
infers the job from the draft's location, and applies the existing job
validator. Workers call one command. Operativity: worker rules and the
engine name the same entry point; the job constructors remain the context
source. This is the smallest change and leaves both problems above in
place: context is still job-shaped, and types still own no checks.

### B. Resolve context from the artifact graph

A member already declares `run-id`, `reviewed-boundary` and, for the memory
member, `source-identity`. Its directory holds its siblings. The run state at
`state/<run-id>/` names the frozen source. Validation of a member inside a
run's output directory can find its set and its run state by location and
declared identity, with no job name. Draft checking becomes validating the
directory with the draft's bytes replacing its slot. The "set so far" rule
becomes: references resolve among the members present. A reference to a
member not yet accepted fails as unresolved, which is the refusal the
analyst receives today.

Operativity: the set type admits a working set, either by relaxing the
finished-set branches or through a sibling working-set type; the validator
exposes a draft override; worker rules name the validator with the output
directory. Checks that depend on run progress rather than on artifacts
remain workflow checks unless option E records them: the last-round rule
for returned findings, blockers required after a failed set check, and the
frozen checkout's cleanliness. The declaring prefix moves to the member type,
since it is a property of the runtime, memory or epistemic report, not of
the job.

### C. Types declare their cross checks

A type spec selects framework primitives with parameters instead of the
framework selecting types by path. Four primitives cover every imperative
rule shipped today:

1. quotations resolve against a declared source: the linked file for
   `verbatim`, the pinned snapshot for an ingest, the set's frozen source for
   an analysis member;
2. identity fields agree with a named container or sibling: members with the
   overview, the profile with the memory member, members with the run state;
3. references of a stated grammar resolve within a scope: record IDs within
   the set, comparison references within the set's declarations;
4. a derived listing equals its recomputation: the `tag-readme` complete
   mark.

The framework ships the primitives and their resolvers; the KB remains data
because the vocabulary is closed and inspectable. The six-path registrations
leave `validation.py`. Operativity: type-rule dispatch reads the type spec's
declarations; a changed declaration changes the type spec, so review
freshness re-checks the cohort as it does for any spec edit
([ADR 084](../adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).
The oracle for each primitive is the referent it dereferences; the warrant
stops where the source contract says it does, at occurrence and identity,
never at claim support.

### D. One registry for frozen evidence

Generalize the ingest snapshot precedent. A registered frozen source has an
identity, a revision or checksum, a kind and a local access root kept
outside tracked content. Ingest snapshots, analysis checkouts and captures
are entries. A blockquote attribution names a registered source path, and
one resolver serves every type. The run state stops being the only route to
a checkout, and a retained set stays verifiable after its run directory is
gone whenever the registry holds the entry. Operativity: the freeze step
registers; the validator's resolver consults; an absent entry yields an
unverified notice, which strict callers may refuse.

### E. Record run progress as a declared artifact

The run directory already records progress in two layers. The engine keeps
per-job records (hand-outs, failures, acceptance, blocks) and event reports
in its own JSON under `workflow-state/`. The definition's control flow leaves
round-numbered files: memory reports, reconciliations, set checks and
verifications. What no file states is the workflow-level state the control
flow holds in variables: the current round, why it opened (returned findings
or blockers), which memory report it consumes, and the remaining correction
budget. The acceptance check recovers these from job names and from the
prompt the engine wrote for the job. The run-state type excludes phase and
correction state by decision, so the artifact would be a sibling in the run
directory, code-written like the run state and the manifest.

Such an artifact is a derived copy of engine records and file presence, so it
is checked against its recomputation or it is absent. Two forms satisfy
that: a derived view, a function over the run directory that a status
command or the validator calls; or a materialized typed artifact the engine
writes at each step and validation recomputes.

What it buys: the run-progress checks in B stop being workflow-only, because
the last-round and blockers rules read declared facts; the acceptance check
needs no job argument, since the draft's location and the progress identify
the job; the validator learns which members are accepted, which is the set
so far, and which strictness applies; operators and handoffs read progress
without the engine; and other code-scheduled workflows reuse the same
artifact kind. Operativity: the engine writes or derives it; the validator,
the check command and the handoff consume it; a change in control flow then
changes a visible contract where today it changes a loop variable.

### Assumptions each option changes

| Standing assumption | Replacement | Options |
|---|---|---|
| Validation reads only the repository and its ignored snapshots | Validation reads registered, pinned local sources; the run-state rule already does | B, D |
| A directory artifact is a finished set | A directory artifact may be in progress; the type states what each state requires | B |
| Imperative type rules are framework code keyed by type path | A type spec selects framework primitives | C |
| Acceptance context comes from the job | Context comes from the artifact graph; the job names the target and the strictness | B, C |
| Intermediate drafts are untyped | Boundary, synthesis and verification drafts are collection-local types whose schemas own their shape | B |
| A finding is a string with a rule prefix | A finding carries rule, subject, location, reason, expected value and repair | A, B, C |
| Run progress is control-flow state the definition holds | Run progress is a declared fact of the run directory, derived from or checked against engine records and files | E |

## Forces

- **The derived-copy rule.** Where ground truth is available, a mismatch
  fails. Where it is unavailable, the result is unverified, never a pass
  ([a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)).
  Acceptance requires resolution; a maintainer may accept unverified. The
  checker reports facts and the caller sets strictness.
- **A schema cannot dereference.** Every cross check needs an imperative
  primitive. The question is who selects it, not whether it exists.
- **The KB is data.** Arbitrary KB-side code stays rejected. A declarative
  selection of shipped primitives preserves the substrate.
- **Two worked cases.** The older proposal warns that a vocabulary designed
  from one example fixes its accidents. Analysis members and `tag-readme`
  give two unlike cases, and ingest quotes a third resolver; this is the
  minimum the older proposal's adoption criterion asks for, not a surplus.
- **Repair belongs to the finding.** Expected values, candidate ranges and
  repair sentences are what made the analysis check usable. They must
  survive unification as structured fields, not as text the caller parses.
- **Run-progress checks stay in the workflow until progress is declared.**
  A type can state what a valid member contains. It cannot know which round
  this is unless the run directory says so (option E).
- **Measurement continues.** ADR 105 counts check runs and refusals by rule
  from the scratch log. A unified surface emits the same counts through its
  JSON result or the engine's records.
- **Bounded reads.** Following an absolute `source.path` is what the run-state
  rule does today. A registry root bounds where the validator may read.
- **Repeated set validation.** A run validates its working set once per
  draft. The run's parse and byte caches already serve repeated requests.

## Free choices

- One command or two: the validator gains a mode, or a thin command keeps
  its name and exit codes while calling the same library. ADR 105 calls the
  name, text output and exit statuses implementation choices.
- Working set: relax the set schema's finished-set branches, or add a
  working-set type the output directory carries until finalization.
- Declaration placement: in the type spec's frontmatter beside `schema`, or
  in a sidecar beside the schema file.
- Access roots: the run state stays the source of truth, or a registry
  replaces it and the run state points into the registry.
- Progress: a derived view over the run directory, or a materialized
  artifact the engine writes; a global workflow type, or one local to the
  analysis collection.

## Adoption criteria

- Unify the surface (A or B) when a second separately commissioned analysis,
  or a maintainer sweep over retained sets, shows the same checks requested
  from more than one surface. The TODO in ADR 105 names the observations to
  count.
- Adopt type-declared primitives (C) when their declarations replace the
  six-path analysis registrations and the `tag-readme` rule with no primitive
  introduced for a single type. Design the vocabulary from both cases
  together, as the older proposal requires.
- Adopt a registry (D) when a third source kind needs resolution, or when
  retained sets must verify without their run directories.
- Adopt a declared progress artifact (E) when a second consumer beyond the
  acceptance check needs round facts, such as the handoff, an operator status
  view or validator strictness, or when a second definition runs on the
  engine.
- Measure refusals by rule before and after from the scratch log and the
  validator's JSON output; a unified surface that loses rule or repair
  detail fails its own purpose.

---

Relevant Notes:

- [ADR 105 — Let analysts run their acceptance check before submission](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md) — extends: the decision whose TODO names this integration and whose check functions this proposal keeps as the primitive library
- [Generalized validation invalidation and imperative extension](./generalized-validation-invalidation-and-imperative-extension.md) — narrows: option B there deferred a declarative dereferencing primitive until a collection-local type needed one; this proposal supplies that case
- [The validation contract](../validation-contract.md) — rests-on: the base, type-rule and schema sources and the dereferencing limit that make a primitive necessary
- [ADR 095 — Directory artifacts add shared set validation](../adr/095-directory-artifacts-add-shared-set-validation.md) — rests-on: the directory artifact as the unit a working set would reuse
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why resolvable mismatches fail and unavailable sources report unverified
- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — rests-on: why a type that asserts a cross check should also be the place that selects its enforcement
- [Collections and types](../collections-and-types.md) — see-also: how a type is named and resolved, which a declaration in the spec would reuse
