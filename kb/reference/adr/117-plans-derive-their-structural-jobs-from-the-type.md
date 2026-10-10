---
description: "A compact plan lists the jobs that write; a loader derives check and apply jobs from the type's layout, standard handlers run them under a named verification protocol, and the prompt is composed from the frame's lines"
type: reference/types/adr.md
status: accepted
---

# 117 — Plans derive their structural jobs from the type

**Status:** accepted
**Date:** 2026-10-10
**Amends:** [ADR 113](./113-artifact-runs-execute-declared-plans-with-pinned-judgments.md): its open items, standard handlers and plan compaction, are decided, and its consequence that every check job needs a handler no longer holds.

**Amended 2026-10-10:** revision 1 memory profiles and their compatibility path are removed, the schema requires version 2, and the profile's comparison-version check went with them; the analysis keeps two declared checks, the boundary's binding to acquisition and the report-check gate. The verification protocol's grammar is one layout finding for any role with `verifies`, its addressees taken from that list, so the apply handler enforces nothing the validator does not.

## Context

ADR 113 gave the engine a plan and a type. The first consumer, the
agentic-system analysis, then needed a package of handlers beside a plan
of 498 lines. Ten of its twenty-five jobs were check or apply jobs that
restated what the layout already said about their roles: the candidate,
the incumbent, the producer's attempt and answered refusal, the partners
from `cites` and `identity`, the criteria from the roles' types. Their
handlers were wrappers naming a role and a partner tuple. Every copy was a
place for the generic logic to drift, and the plan's mission content,
which roles are written in what order from what, was hard to see. Each
job instruction was half boilerplate: read order, what the inputs are,
the answers protocol, the self-check and the return line, repeated ten
times with small differences. The operator's direction (2026-10-09): the
type defines most of the type-dependent work, and code extensions are the
special cases.

The forces that recur: a per-job configuration in Python is the cheapest
thing to write and the easiest to let drift from the declaration it
mirrors; a second declaration shape is worth its cost only if it stays
faithful to the hand-written one; a worker should not discover at run time
what code already knows; and a member's producer should need as little as
possible of the whole artifact.

## Decision

**A compact plan.** The plan lists the jobs that write, one entry per
role named after the role, with its instruction, reads, max attempts,
outputs, gates and the consumer's own checks, plus the consumer's own code
jobs in full form. A loader in the reuse modules expands it into the full
plan the engine fixes at start: one `check-<role>` job per filled role and
one `apply-<role>` job per role with `verifies`, their inputs taken from
the layout, not from the entry's reads; identity sources as required
inputs, cited roles as optional, the producer's attempt order-only, and
criteria as the type closure of the roles plus one plan-level contracts
group. `reads` shapes only the model job's hand-out. A `job:` entry runs a
standard handler over roles. Plan keys and names are hyphenated, and the
loader refuses an underscore. The run records the compact file's digest,
and integration compares that with the shipped plan.

**Standard handlers.** The reuse modules ship the check, the verification
application and the artifact check. A handler learns its role and
partners from the job's declared inputs through an accessor; nothing is
repeated in a parameters block. The consumer keeps opening, acquisition,
assembly, publication and effect verification, which no declaration can
derive.

**A named verification protocol**, fixed, not configurable. A verifying
role's document carries `## Blockers` and `## Limits`, each `none` or a
list; with several subjects every blocker starts with the role it
addresses; Blockers `none` accepts every subject's handed version that
validation did not refuse, otherwise each addressed subject is refused and
an unaddressed one stays unsettled. The apply handler validates the
verdict and each handed subject together, routes findings by the role
they name, and refuses a subject only for findings that appear with the
verdict placed and not without it; a finding the subject shows on its own
belongs to its check. Consumer policy enters through two extensions on an
entry: `checks`, functions returning findings, with their own inputs; and
`feedback`, one function appending to a subject's refusal. The frozen
source is a plan-level key naming the member whose `source` field pins
it, a run's authorization rather than shape.

**The prompt is composed from its own lines.** The engine's frame prints
`name = value` lines for the job, its inputs, outputs, parameters, the
role, the artifact and, from the layout, `identity`, `cites` and
`verifies`. A plan-level `prompt-section` names a file the engine renders
into the frame, whose placeholders are exactly those lines and nothing
else, with a paragraph marked `[<name>]` kept when the prompt has that
line. Run values a worker needs, the command path, the source identity,
the capture directory, are plan parameters printed as lines, so no worker
reads the opening's JSON. Each model job receives its member type and the
types of the roles it reads; the set type is not handed to workers.

**Where the rules live.** The member type owns what a member contains and
wins over the job instruction; the worker rules own execution; a job
instruction holds what the job must establish and challenge. The records
contract stays a shared member-level contract that the record-citing
types refer to; the boundary contract is in the boundary type; the
sources contract is split between the boundary type and the worker rules.

**Run identity.** A layout identity source may name `run`, so
a member's binding to its run is a shape check in draft validation, and a
member type registers its identifier grammar so that a correction cannot
drop an identifier its accepted version declared. The analysis keeps
three declared checks: the boundary's binding to acquisition, the
report-check gate and the profile's comparison version.

## Considered alternatives

**Subjects declared in the plan** rather than the type's `verifies`:
decided against in ADR 114, since the type would not notice a plan that
omitted verification.

**A parameters block on code jobs** naming role and partners: lets the
strings drift from the inputs the accessor reads.

**Widening `cites` to mean reads**: would make the validator read
mission; `reads` stays in the plan.

**Configurable verdict policies**: one fixed protocol; a second policy
when a consumer needs it. Accepting a subject another verifier accepted
would also be coherent and was not taken.

**Slots as their own vocabulary**: the first renderer gave `{output}` the
output's name while the line gave its path, and the template reached the
line through a third notation; slots became the lines.

**Two template files**, one for answering jobs: would repeat the rest;
one conditional paragraph instead.

**Handing the set type to workers**, with the records contract moved
into it: reversed the same day, because a producer should need its member
type, the types it reads and the contracts those name, and nothing about
the whole artifact; the member type with its contracts is then the
complete contract for a producer, testable without a set.

**A list of citable records in the prompt**: dropped, the writer reads
the cited members anyway and the destination follows from the ID.
**A list of limits the synthesis must carry**: deferred until a run shows
the limit-not-carried refusal firing.

**The coordinator judges** for consumers without a verifier, and **a typed
artifact-run directory**: left for a consumer that needs them.

## Consequences

The analysis plan is 219 lines against 498; its ten mission files hold
about 2,900 words from 4,950; the consumer's wrapper handlers are deleted
and its Python holds opening, acquisition, assembly, publication and three
declared checks. A second consumer with structural checks writes a compact
plan and no handlers. Fidelity tests hold the expansion equal to a frozen
copy of the hand-written plan after the decided differences, and a
judgment test showed each wrapper and its standard replacement recording
the same judgments before the wrappers went.

Operativity: the analysis skill starts runs through `commonplace-analysis
start`, which expands the compact plan; the loader, the standard handlers
and the prompt renderer are the engine's reuse modules; draft validation
consumes the run identity and the identifier grammar; the plan loader's
refusal of underscores and the type-closure test enforce the declaration
forms. Every rule a worker meets comes through the prompt, the member
type, the records contract and the worker rules.

Limits. One consumer has exercised this; the one production analysis to
publication on the compact plan and the templated prompts has not yet run,
so whether workers follow the new prompts and write link citations
correctly is untested. The standard handlers validate with the library's
parent as the project root, which holds for a source checkout and the
analysis worktrees and not for a package-installed consumer. Pinned
validation still refuses a member type with no Python rule; treating it as
schema-only waits on the type-selected checks proposal. The derived apply
job's judgment covers the `verifies` relation only; that a verdict was
right is the verifier's business, not the engine's.
