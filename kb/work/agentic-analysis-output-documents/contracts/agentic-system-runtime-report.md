# Agentic system runtime report (draft type)

The member of a run's retained set that carries the runtime baseline: the
traced invocation and its alternate and forcing routes, the execution
preflight and probe evidence, and the canonical records the coordinator's
runtime pass established. It annotates records the memory report declares
with the runtime pass's own classifications. Set-wide conventions, the
namespace, the declaration grammar, status fields, source anchors and the
quotation contract, are those of the
[overview](./agentic-system-analysis-overview.md#the-set).

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-runtime-report.md` |
| `description` | Yes | Retrieval description naming the system and the runtime boundary traced |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's frozen revision or capture identity |

## Required sections

### Runtime account

`## Runtime account` traces the ordinary shipped invocation and every
material alternate or forcing route selected by the producing skill. For
each material loop it identifies the trigger and principal, identities,
next-step owner, decision policy and representational form, context,
state, executor and effect boundary, runtime-client controls, persistence,
coordination and return, recovery, and terminal output. A load-bearing
guarantee also names its owner, enforcement point, guarantee strength,
covered and alternate paths, required external contract, and separate
conclusion-status fields.

For material diagnosis, candidate comparison, admission and successor
selection, identify who proposes, decides, and can veto. Describe
computational and human contributions separately when they share a step.
Record answer-oracle access independently: a supplied expected answer or
reference outcome, its provider, and how it governs judgment. Model
judgment alone is not evidence of an answer oracle. State improvement
triggers and the evidenced operating modes (open requests, bounded
experiments or curricula, or multiple modes), attaching oracle use to the
relevant mode. Give explicit `uninspected` or `inapplicable` reasons where
coverage stops. These are descriptive findings, not an autonomy grade.
Component fixity belongs on `CMP-*` records and revision admission on the
admitting `RTE-*` records.

For every focused test or probe selected by the producing skill, the
account contains one execution-preflight record:

`check ID | intended conclusion | command, test, or script identity | required dependencies and authority | availability evidence | execution disposition: ran or not run | execution outcome or non-execution reason | conclusion prevented`

Each check ID is unique inside the run. Execution disposition is separate
from conclusion status. `not run` does not mean a failed check or absent
system behavior, and supports no negative finding; a command attempt that
stops before the target check executes leaves the target check `not run`.
When no dynamic check was selected, state `no dynamic check planned` and
list the checks considered and why static evidence was sufficient.

### Probe evidence

`## Probe evidence` contains one capsule per executed check, or `none`:

`source ID | check ID | UTC execution time | evidence layer | intervention and comparison, or none for an observational run | fixture or input identity | exact command, test node, or reusable-script identity | relevant environment | execution outcome and exit status | raw output inline, or resolvable exact-output location plus byte length and SHA-256 | design and confounding limits | exact conclusion supported and affected canonical IDs`

The check ID joins the capsule to its preflight record. Fixture or input
identity uses an immutable revision or byte length and SHA-256 when
content is not already canonical. Record a command verbatim; identify a
reusable script by path plus immutable revision or SHA-256. The relevant
environment names the runtime, tool, package, and service versions and
non-secret configuration needed to interpret the result, and records only
credential availability, never credential values. A `causal experiment`
capsule includes an actual intervention and comparison; otherwise the
capsule is `observed run` evidence. A digest without resolvable retained
bytes may identify missing output but cannot by itself support an
`observed` or `causally supported` conclusion. The capsule stays inline.

### Shared records

`## Shared records` contains the six kind headings `### Components`,
`### Operative objects`, `### Routes`, `### Claims`, `### Evidenced
absences`, and `### Behavioral-authority paths`, each holding the records
of that kind this member declares, or `none declared in this member`; a
kind that is empty across the whole set says `none found within
<boundary>` here.

Component and operative-object records preserve source-native identity,
representational form, storage substrate, and evidence. For
distributed-parametric components used by inspected routes, distinguish
parameter changes during operation from exact-version pinning or mutable
endpoint resolution, each with its own evidence status. Inaccessible
provider internals remain explicitly uninspected; fixed weights do not
imply absence of learning through other retained material.

Route records preserve endpoints, progression, owner, context/state/action
effects, applicable status fields, and evidence. Each route also records
immediate return, later read-back, delegated visibility, selection
predicate, invalidation or expiry, activation or effect, and evidence
limits, with an explicit inapplicable or uninspected reason instead of an
empty field. Memory read-back means material accumulated or changed
through use affects a later consumer invocation; static shipped material
and ordinary current-run state are not read-back. Activation requires
evidence that delivered material changed behavior. For materially distinct
mechanisms admitting changes to the product, retained knowledge or
instructions, capabilities, or production machinery, record trigger,
proposed change, admission, rejection ability, and rollback or recovery.
Group writes governed by the same mechanism. Routine logs, counters and
unchanged checkpoint persistence need no separate revision account unless
they alter later decisions or recovery.

Each admitting route names the guidance that shaped the proposal, what it
says, and what persists: formulated theories, criticisms, input/outcome
records, parameters, or other source-native material. It describes
applying, deriving from, criticizing, revising or replacing, and retaining
or reconstructing a theory in ordinary terms. Record the degree to which
its assumptions, scope conditions, and parts are individually inspectable
and revisable, and the boundary over which that addressability judgment
holds. Addressability is a graded finding recorded separately from the
theory-builder conditions; condition 1 needs only its minimum, where the
whole theory is one unit that carries content. A rule set can express a
theory without retaining its historical rationale. Record what it claims
and how its structure exposes assumptions, scope conditions, and parts; do
not classify it from the storage label alone. Missing rationale does not
establish absent formulated criticism of its content. Where rationale is
retained, the record states whether a later route reads it.

A theory route gives separate conclusion statuses and evidence for each
[theory-builder](../../../notes/definitions/theory-builder.md) condition,
labelled "theory-builder conditions 1–4": localized content, consumption,
content-directed criticism with its resulting revision or changed
reliance, and iteration. No condition is inferred from its neighbours.
Consumption means decisions depend on what the theory says; storage,
citation, or delivery alone does not establish it, and derivation under an
unchanged theory does not establish criticism. Criticism is itself stated
and can blame the test, the data, or an auxiliary assumption; the record
names the claim challenged, the result, and where blame was placed. A
score selecting variants does not count. For prose, a contradiction is an
interpretation unless a codified check produced it. A theory can survive
criticism without a text change, with changed reliance or test selection.
A theory rejected whole and replaced by a new conjecture has been revised.
Iteration counts when the result of criticism is kept and shapes the next
round, including rounds within one run; a critic whose report no next
round takes up fails it. Rebuilding a theory from retained criticisms
counts; retained input/outcome records alone do not. Whole replacement of
a theory meets condition 1 at its minimum. Persistence is a graded finding
recorded separately, like addressability: within one reasoning episode,
across the rounds of one run, across runs on the same task, or across
problems and sessions; the record names what persists, the grade it
reaches, and the later consumer that takes it up. Freezing a product for
deployment by another system ends the builder at the freeze.

Membership has no success condition, so learning is a separate claim,
labelled "learning". It identifies the improved capacity for future
action, its assessment boundary, the evidence of improvement, and the
evidence supporting attribution; membership, revision, persistence, or
connected steps alone do not establish it. Capacity need not already have
been exercised. A claim about later capacity traces persistence to that
time; a claim about later or recurrent use traces the retained result and
its consumer. The `trace_learning` comparison axis retains its specified
memory-write meaning; its value alone does not establish learning.

The record distinguishes absent formulation or criticism from inaccessible
model processing: opacity alone establishes neither presence nor absence.
For reflection it identifies selected aspects inside the declared system
boundary, their self-representation, and the two-way causal path: aspect
changes can update the representation, and representation-mediated
operations can affect later behavior. Subject matter alone does not
establish that path, and direct modification of represented machinery is
not required. The reflective theory-builder qualifier is more specific:
the builder's method texts meet conditions 1–4 and are criticized against
records of the builder's own operation. The autonomous qualifier is
recorded role by role, from the decision roles in the Runtime account:
computation performs every operation inside the builder's boundary, and
users who only supply problems and judge products are outside it.
Autonomy does not establish that the operations are reliable. Reflection,
autonomy, and improved capacity remain separate claims.

Claim records preserve claimed operation and source. An evidenced absence
carries an `absent` conclusion status, its searched boundary (the searched
roots or files, query, and revision), evidence, and the conclusion it
supports or prevents. A behavioral-authority path records consumer,
channel, force, and horizon.

### Annotations

`## Annotations` holds the runtime pass's fields on records the memory
report declares, each as `#### On RTE-10 — Short label` followed by only
the lens-specific fields: the admitting-route and theory-route fields
above, decision roles, operating mode, answer oracle, and links to
runtime-declared records. It repeats no generic identity, evidence
passage or memory finding. State `none` when the runtime pass annotated no
memory-declared record.

## Template

```markdown
---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} runtime report

## Runtime account

## Probe evidence

## Shared records

### Components

### Operative objects

### Routes

### Claims

### Evidenced absences

### Behavioral-authority paths

## Annotations
```
