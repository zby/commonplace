---
description: "Proposal: let a simple consumer of the engine run from its plan and directory type alone, with standard handlers from the engine's reuse modules, so that only checks reaching outside the artifact need consumer Python"
type: reference/types/design-proposal.md
---

# Plans without consumer code

The engine runs a typed directory artifact through a plan: model
jobs write candidates, code jobs check and judge them, and a coverage gate
releases publication. A consumer supplies a plan, a type and any
handlers; the engine is `commonplace.artifactrun`, and its reuse modules,
such as `artifactrun/checks.py`, serve any consumer. The first consumer, the agentic-system
analysis, needed a package of handlers beside its plan. This proposal
asks what a second, simpler consumer would still have to write in Python,
and how to reduce that to the checks that reach outside the artifact.

## Current state (as of 2026-10-09)

The engine (`src/commonplace/artifactrun/`) is generic and already driven by two
on-disk declarations: the plan YAML, loaded as `Plan`, and the type's `layout`
frontmatter from [ADR 111](../adr/111-directory-types-declare-their-layout.md).
The layout gives roles, their document types, identity fields copied between
roles, citation partners and the roles a disposition requires; the engine
derives relations, permitted roles and coverage from it. The plan names
each model job's role, instruction, inputs and max attempts, and each code
job's inputs and handler. The declaration is data; code jobs name their
handlers by dotted path, as the workshop's
[API design](../../work/workflow-requirements/api-design.md) decided.

Four things keep a new consumer from running on declarations alone:

- Every code job names a handler, and the handler alone knows which role
  its candidate fills and which partner roles it is judged against. The
  shared check in `src/commonplace/artifactrun/checks.py` already does the work:
  snapshot the partners, validate the candidate as a draft at its role
  against the pinned criteria, check a frozen source, check the answers to
  the refusal the producer answered, and judge over the relations the
  validation examined, with the scope derived from the snapshot. The
  analysis package's check handlers are mostly wrappers that supply the role
  and partner strings; a few add checks of their own.
- Code jobs take no parameters, and a code attempt exposes neither its job
  name nor its declared inputs. A shared handler therefore cannot learn its
  configuration from the declaration.
- Pinned-set validation refuses a member type that has no Python type rule
  registered, and rules register through one hard import of the analysis
  rule module at the end of `src/commonplace/lib/validation.py`. A type with
  only a schema cannot publish.
- Opening and publication are consumer handlers carrying their run naming,
  destination and archive paths as constants.

The engine's own tests show the same: their toy type and toy plan are
generic, yet they still need test handlers. Which checks must stay in code
depends on what they consult. The analysis artifact's domain checks split into
those that compare the candidate with partner members or its own fields,
such as a source identity copied from another report or a comparison
version, and those that consult something outside the artifact: the run
parameters at opening, the producer's previous version across a correction,
and the checkout and frozen source on disk. The type's schema constrains
only the manifest, and a layout identity source names only a role, so
nothing declarative describes the second group today.

The workshop's [consumer surface](../../work/workflow-requirements/consumer-surface.md)
review weighed a declared generic check against a consumer helper and chose
the helper, which became the shared check above. It rejected engine-generated
check pairs because the engine must not know what a content check is. Its
[README](../../work/workflow-requirements/README.md) records a movable
boundary: the coordinator may take over a code job's interpretation while
bookkeeping stays in code.

## Problem

A consumer whose checks are purely structural should run from its
declaration and its type. Today it must write one handler per check job to
hold two strings, a verdict parser, an opener and a publisher, and register
a type rule it does not need. The lines of Python are few, but each is a
consumer-specific copy of generic logic, and each copy is one more place for
the generic logic to drift.

## Options

The options are mostly independent; they are ordered from least to most
declarative.

1. **Standard handlers in the engine's reuse modules.** The engine ships one
   handler for each recurring code job: a check, a verdict application, a
   directory publish and a minimal opener. The declaration still lists
   every job but names only these. A consumer with a domain check writes
   its own handler, as the analysis package does now. The shared check must
   then learn its role and partners from the declaration. Two sources: a
   `parameters` block on code jobs, mirroring the one model jobs have, which
   is a small engine change but lets the strings drift from the job's
   inputs; or an accessor exposing the job's declared inputs on the code
   attempt, from which the handler derives the candidate's role and the
   partner roles with nothing repeated. The declaration is fixed at start,
   so an accessor fits the rule that fixed values get accessors.

2. **Declared individual checks.** A code job lists check functions by
   dotted path, each taking the candidate the standard handler built and
   returning reasons. The standard handler runs the generic steps, calls
   each listed check and judges. This keeps the integration idea of the
   handler, a declaration naming a Python function, one level finer. The
   candidate carries the attempt, so a listed check can read the opening
   metadata, the producer's attempt record or a handed input without more
   plumbing. Trust is unchanged: the plan already names code, and lives
   under the consumer's instruction tree, not in the validated repository
   content that [type-selected Python validation checks](./type-selected-python-validation-checks.md)
   worries about.

3. **Shape checks move into the type.** A check that compares the candidate
   with partner members or constrains its own fields is shape, and draft
   validation runs inside the standard check. Identity fields in the
   layout, schema constants and type rules cover the analysis artifact's cases.
   A complex shape check is a type rule; how a type selects one without the
   hard import is the subject of [type-selected Python validation checks](./type-selected-python-validation-checks.md)
   and is not re-decided here. Pinned-set validation would treat a type
   with no rule as schema-only rather than unsupported.

4. **Layout identity sources name the run parameters.** The engine fixes
   the parameters in the run metadata. Letting an identity source name them
   makes a member's binding to its run, such as the boundary's run id and
   source identity, a shape check in draft validation, so the opener stops
   duplicating it. A generic rule that declared identifiers survive a
   correction, given the type's identifier grammar, would join the
   correction-protocol step the same way. What remains outside both is
   effect verification, the checkout and frozen source, which stays code by
   nature.

5. **Check pairs generated from the type.** A loader in the reuse modules,
   not the engine's scheduling, expands a plan listing only model jobs: one check per
   model role, with partners from the layout's citation and identity
   relations, a coverage-gated publish from the disposition. The engine
   still receives an ordinary full plan and fixes the expanded form in
   the run metadata. This respects the non-goal the consumer-surface review
   applied to engine-generated pairs. It adds a second declaration shape
   that must stay faithful to the hand-written analysis plan, or that
   plan becomes a special case again.

6. **The coordinator judges.** For a consumer without a verifier, or whose
   verdicts need no routing, the verdict application disappears: the
   coordinator reads the verification and records the judgment through the
   operator command. This is the movable boundary the workshop recorded.
   It removes the most domain-shaped code and also the deterministic part
   that applies a verdict to the exact versions the verifier was handed, so
   it suits only consumers where that precision is not needed.

A typed artifact-run directory, with the artifact, the run metadata and
acquired sources as declared parts so that "outside the artifact" becomes
"inside the run", is noted and not proposed: option 4 covers the one case the
analysis artifact has at a fraction of the cost.

## Forces

- Per-job configuration in Python is the cheapest thing to write and the
  easiest to let drift from the declaration it mirrors. Deriving it from the
  job's inputs has no second copy.
- The engine's non-goal, no validation policy and no knowledge of content
  checks, draws the line between options 1 and 5 on one side and anything
  engine-generated on the other. Both can be met in the engine's reuse modules.
- Shape belongs to the type and mission to the instruction
  ([ADR 110](../adr/110-every-analysis-output-has-a-type.md)). Max attempts,
  instructions and inputs are mission and already plain YAML in the
  plan; moving them into the type spec would make the validator read
  mission. The declaration can stay a plan file.
- Effect verification cannot be declared: no schema states that a Git
  checkout is still what a record says. Any declarative route ends at a
  named function for it.
- A second declaration shape, option 5, is worth its cost only after the
  standard handlers have shown which fields a compact form needs. Built
  first, it codifies a shape only the analysis artifact has used.
- The toy plan in the engine tests is a second consumer that exists
  today, so the standard handlers have a test subject before any new
  consumer does.

## Candidate selection

Options 1, 3 and the schema-only acceptance in pinned validation first, with
the input-spec accessor rather than code-job parameters, proven by removing
the engine tests' handlers. Option 4 next, since it deletes checks the
analysis opener duplicates. Options 2 and 6 as the escape for what remains,
option 2 by default. Option 5 waits for the adoption criterion below.

## Operativity

- **Options 1 to 4.** The change is consumed by a plan naming
  handlers in the engine's reuse modules, read by the engine's loader, which already binds
  handlers by dotted path. The first such declaration is the engine tests'
  toy plan; the second would be the analysis plan once its wrapper
  handlers are replaced. Option 4 is consumed by draft validation through
  the layout parser.
- **Option 5.** Nothing consumes it yet; a compact declaration format and its loader
  must be built, and the analysis plan would be the test of fidelity.
- **Option 6.** The change is consumed by the coordinator through the consumer's skill
  that tells it when to judge; the operator command exists, the rule in a
  skill does not.

## Adoption criteria

- Options 1 and 3: a second consumer, or the engine tests' toy
  plan, runs to publication with no handler outside the engine's reuse modules.
- Option 4: the opener's run-binding checks are deleted after draft
  validation reports the same mismatches.
- Option 2: a consumer needs a check that consults the attempt and that
  option 4 does not cover, other than effect verification, which is such a
  check already.
- Option 5: two plans exist whose check pairs are hand-written copies of
  what the layout states.
- Option 6: a consumer where a verdict's subjects are the current members and
  the coordinator's judgment call is simpler than a routing handler.
