---
description: "Proposal: derive a plan's check and apply jobs from the artifact type's layout, with standard handlers from the engine's reuse modules, so a plan lists only the jobs that write and consumer Python holds only what reaches outside the artifact"
type: reference/types/design-proposal.md
---

# Plans without consumer code

The engine runs a typed directory artifact through a plan: model jobs
write candidates, code jobs check and judge them, and a coverage gate
releases publication ([ADR 113](../adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md)).
A consumer supplies a plan, a type and any handlers. The first consumer,
the agentic-system analysis, needed a package of handlers beside a plan of
about 330 lines. This proposal asks how much of both the type already
determines, and designs a compact plan from which a loader derives the
rest, so that consumer Python holds only the checks that reach outside the
artifact. The direction is the operator's (2026-10-09): the type should
define most of the type-dependent work, and code extensions should be the
special cases.

## Current state (as of 2026-10-09)

The engine (`src/commonplace/artifactrun/`) is driven by two declarations:
the plan, loaded as `Plan`, and the type's `layout` frontmatter
([ADR 111](../adr/111-directory-types-declare-their-layout.md)). The layout
gives each role its path, its document type, the identity fields it copies
from other roles, the roles it may cite and whether a disposition requires
it; the engine derives relations, permitted roles and coverage from it. The
plan names each model job's role, instruction, inputs, outputs, parameters
and max attempts, and each code job's inputs and handler by dotted path.
Input addresses name roles directly (`address: role`), and a draft
validates in its role through `commonplace-validate --artifact --role`,
the same call the shared check and the worker's self-check make.

The analysis plan has twenty-five jobs. Five are consumer-shaped code:
`open`, `acquire`, `record-check`, `assemble` and `publish`. Ten are
model jobs, one per role. The other ten are check or apply jobs, and each
restates what the layout already says about its role: the candidate from
the filling job's primary output, the incumbent, the producer attempt and
its answered refusal, partner roles from cites and identity sources, the
criteria from the role's type and schema, and a slot parameter for draft
validation. Their handlers are mostly wrappers: the three analyst checks
share one function that names the role and partners; the three apply
handlers share two. The engine tests' toy plan has the same shape, with
five check handlers made by one factory from a job name, a role and a
partner tuple.

What the wrappers add beyond the shared check is small and of two kinds.
Shape, which compares the candidate with partner members or its own
fields: declared record IDs surviving a correction, the memory report's
source identity matching the opening's, limits carried from a verification
into the synthesis. And checks that consult something outside the
artifact: the boundary's binding to the run parameters and the frozen
source, the record check that runs before verification, and effect
verification at acquisition and publication. Pinned-artifact validation
refuses a member type with no Python type rule, registered through one
hard import at the end of `src/commonplace/lib/validation.py`.

The workshop's [consumer surface](../../work/workflow-requirements/consumer-surface.md)
review rejected engine-generated check pairs because the engine must not
know what a content check is, and it recorded a movable boundary: the
coordinator may take over a code job's interpretation while bookkeeping
stays in code. One production analysis has run through the engine
(2026-10-09, in the log).

## Problem

A consumer whose checks are purely structural should run from its type and
a short plan. Today it writes one handler per check job to hold a role and
a partner tuple, a verdict parser, an opener and a publisher, registers a
type rule it does not need, and declares every check job's inputs by
hand, copying the layout. Each copy is one more place for the generic logic
to drift, and the plan is long enough that its mission content, which
roles are written, in what order, from what, is hard to see.

## What the type determines and what it does not

The split follows ADR 110: shape belongs to the type, mission to the
instruction.

**From the layout alone**, for a role R: the check job that judges
candidates for R, with every input named above and the standard check as
its handler; the draft-validation parameters for R's filling job; and, for
a role that verifies others, the apply job that judges the verified roles'
handed versions over the verifier's relations. Publication is a
coverage-gated copy with destination parameters.

**Mission, which stays declared**: which roles are model-written, with
which instruction, max attempts and auxiliary outputs. Which members a
worker reads, since reads exceed cites: the profile reads the
reconciliation it may not cite. Ordering between tiers: the profile and the
synthesis wait for record verification to accept the records, a judgment
gate the layout cannot infer because the reconciliation reads the same
records unverified. And the special cases: opening, acquisition, the
boundary's source binding, the record check and assembly.

**Not derivable at all**: effect verification. No schema states that a Git
checkout is still what a record says.

## Options

1. **Standard handlers in the engine's reuse modules.** The engine ships
   one handler for each recurring code job: a check, a verdict application,
   a directory publish and a minimal opener. A consumer with a domain check
   writes its own, as the analysis does now. The shared check learns its
   role and partners from the declaration through an accessor exposing the
   job's declared inputs on the code attempt: the candidate's role is the
   role of the job that produces the candidate input, and the partner roles
   are the role inputs. Nothing is repeated. A `parameters` block on code
   jobs was the alternative; it lets the strings drift from the inputs.

2. **Declared individual checks.** A job lists check functions by dotted
   path, each taking the candidate the standard handler built and returning
   reasons. This keeps the integration idea, a declaration naming a Python
   function, one level finer. The candidate carries the attempt, so a check
   reads the opening metadata or a handed input without more plumbing.

3. **Shape checks move into the type.** Identity fields in the layout,
   schema constants and type rules cover the analysis artifact's shape
   checks. How a type selects a rule without the hard import is the subject
   of [type-selected Python validation checks](./type-selected-python-validation-checks.md)
   and is not re-decided here. Pinned-artifact validation treats a type
   with no rule as schema-only rather than unsupported.

4. **Layout identity sources name the run parameters.** The engine fixes
   the parameters in the run metadata. Letting an identity source name
   them makes a member's binding to its run, such as the boundary's run id
   and source identity, a shape check in draft validation, so the opener
   stops duplicating it. A generic rule that declared identifiers survive a
   correction, given the type's identifier grammar, joins the correction
   protocol the same way.

5. **A compact plan expanded by a loader.** The plan lists the jobs that
   write and the consumer's own code jobs. A loader in the reuse modules,
   not in the engine's scheduling, expands it into the full plan: one check
   job per filled role, one apply job per verifying role, draft-validation
   parameters, criteria from the roles' types, and a coverage-gated publish
   from the disposition. The engine receives the expanded plan and fixes
   it in the run metadata, so `status`, `judge` and the attempt records see
   ordinary job names and the engine's non-goal holds. A job that fills a
   role takes the role's name, since one role has at most one filler and a
   job fills at most one role; derived jobs are named `check-<role>` and
   `apply-<role>`. An entry declares only mission:

   ```yaml
   - role: memory
     instruction: jobs-engine/analyse-memory.md
     max_attempts: 3
     outputs: [report, answers]
     reads: {boundary: required, runtime: order-only}
   - role: record-verification
     reads: {boundary: required, record-check: output}
   - role: memory-profile
     reads: {boundary: required, runtime: required, memory: required,
             epistemic: required, reconciliation: required}
     verified-by: [record-verification]
   ```

   `reads` defaults to the role's cites and identity sources. `verified-by`
   expands into one accepted-judgment input per read member that verifier
   covers. Plan-level `inputs` name what every model job receives, such as
   the opening metadata. The analysis plan drops to roughly 80 lines, and
   the loader's fidelity is testable: its expansion of the compact analysis
   plan must equal today's hand-written plan, job for job.

6. **The coordinator judges.** For a consumer without a verifier, the
   coordinator reads the verification and records the judgment through the
   operator command. This is the movable boundary the workshop recorded. It
   removes the deterministic part that applies a verdict to the exact
   versions the verifier was handed, so it suits only consumers that do not
   need that precision.

A typed artifact-run directory, with the artifact, the run metadata and
acquired sources as declared parts so that "outside the artifact" becomes
"inside the run", is noted and not proposed: option 4 covers the one case
the analysis artifact has at a fraction of the cost.

## Choices within option 5

- **Where "verifies" lives.** The loader must know that record-verification
  judges the records. Either the plan says so on the verifier's entry, or
  the type declares `verifies` beside `cites` as a second relation kind.
  Candidate: the type. That a published analysis contains verified records
  is part of what the artifact is, and the relation
  `record-verification:cites:runtime` already carries acceptance semantics
  through coverage. This amends ADR 111's layout vocabulary; the apply
  job's scope then names `verifies` relations.
- **Reads against cites.** `reads` stays in the plan, defaulting to cites
  plus identity sources, so most entries declare nothing. Widening the
  type's `cites` to mean reads would make the validator read mission.
- **Verification gates.** A per-entry `verified-by` list. A plan-level
  default that gates every member read after its verifier is simpler and
  wrong for the reconciliation.
- **The standard apply handler.** Blockers `none` accepts every verified
  role; entries refuse the addressed roles, or the single verified role
  when there is one. The synthesis-specific "limit not carried" check
  becomes a type rule between the synthesis and its verification, under
  option 3. The record-check gate, that a verifier must address structural
  failures, stays a declared check on the apply job, under option 2.
- **Extra checks.** A per-entry `checks` list under option 2 for the
  boundary's frozen-source binding and the memory source identity, until
  option 4 makes them shape.

## Forces

- Per-job configuration in Python is the cheapest thing to write and the
  easiest to let drift from the declaration it mirrors. Deriving it from the
  job's inputs, or from the layout, has no second copy.
- The engine's non-goal, no validation policy and no knowledge of content
  checks, draws the line between the reuse modules and the engine's
  scheduling. Options 1 and 5 both stay on the reuse side: the engine
  still receives a full plan.
- Shape belongs to the type and mission to the instruction (ADR 110). Max
  attempts, instructions, reads and gates are mission and stay in the plan.
- A second declaration shape is worth its cost only if it stays faithful
  to the hand-written plan. The fidelity test makes that a property the
  tests hold, not a hope.
- Role and job are different things: a role is a position the type
  declares, a job is a unit of work. Naming the filling job after its role
  removes a redirection without conflating them; derived jobs keep their
  own names.
- Effect verification cannot be declared. Any declarative route ends at a
  named function for it.
- The toy plan in the engine tests is a second consumer that exists today,
  so the standard handlers and the loader have a test subject before any
  new consumer does.

## Candidate selection

Options 1 and 3 first, with the input-spec accessor, proven by deleting the
engine tests' check handlers. Option 5 second, with the choices above,
proven by the fidelity test against the hand-written analysis plan and
then by switching the analysis skill to the compact plan. Option 4 after,
since it deletes the checks the opener and the analyst check still carry.
Option 2 as the escape for what remains. Option 6 waits for a consumer
that needs it.

## Operativity

- **Options 1 and 5.** Consumed by a plan naming handlers in the reuse
  modules, read by the loader, which the engine's `start` already calls to
  fix the declaration. The first such plan is the engine tests' toy plan;
  the second is the compact analysis plan, consumed by the analysis skill
  through `commonplace-analysis start`.
- **Option 3.** Consumed by pinned-artifact validation at publication.
- **Option 4.** Consumed by draft validation through the layout parser.
- **Option 2.** Consumed by the standard check and apply handlers, which
  call the listed functions.
- **Option 6.** Consumed by the coordinator through a consumer's skill;
  the operator command exists, the rule in a skill does not.

The automated evaluation these options add is the standard check's draft
validation, warranted by the type contracts and schemas. It establishes
form and relations, not analytical truth.

## Adoption criteria

- Options 1 and 3: the engine tests' toy plan runs to publication with no
  handler outside the engine's reuse modules.
- Option 5: the loader's expansion of a compact analysis plan equals the
  hand-written plan job for job, asserted by a test; then one analysis
  runs through the compact plan to publication.
- Option 4: the opener's run-binding checks are deleted after draft
  validation reports the same mismatches.
- Option 2: a consumer needs a check that consults the attempt and that
  option 4 does not cover, other than effect verification, which is such a
  check already.
- Option 6: a consumer where a verdict's subjects are the current members
  and the coordinator's judgment call is simpler than a routing handler.
- The "verifies" choice: an ADR revising ADR 111's layout vocabulary, or a
  recorded decision to keep it in the plan.
