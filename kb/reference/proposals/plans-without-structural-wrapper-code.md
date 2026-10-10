---
description: "Proposal: a compact plan from which a loader derives check and apply jobs out of the type's layout, run by standard handlers under a named verification protocol, so consumer Python holds only the consumer's own checks"
type: reference/types/design-proposal.md
---

# Plans without structural wrapper code

The engine runs a typed directory artifact through a plan: model jobs
write candidates, code jobs check and judge them, and a coverage gate
releases publication ([ADR 113](../adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md)).
A consumer supplies a plan, a type and any handlers. The first consumer,
the agentic-system analysis, needed a package of handlers beside a plan of
498 lines. This proposal removes the wrapper code that restates the
layout: a loader derives the structural jobs from the type, standard
handlers run them, and the consumer keeps only its own checks, its opener,
acquisition, assembly and effect verification. The direction is the
operator's (2026-10-09): the type defines most of the type-dependent work,
and code extensions are the special cases. The design below is decided;
what remains is the sequence and the adoption criteria.

## Current state (as of 2026-10-09)

The engine (`src/commonplace/artifactrun/`) is driven by two declarations:
the plan, loaded as `Plan`, and the type's `layout` frontmatter
([ADR 111](../adr/111-directory-types-declare-their-layout.md),
[ADR 114](../adr/114-directory-types-declare-what-a-role-verifies.md)).
The layout gives each role its path, its document type, the identity
fields it copies from other roles, the roles it cites, the roles it
verifies and whether a disposition requires it. The engine derives
`identity`, `cites` and `verifies` relations from it and requires an
accepted judgment over each for publication. The shared check's scope
never includes a `verifies` relation; only an apply job judging the
handed subject covers it. The plan names each model job's role,
instruction, inputs, outputs, parameters and max attempts, and each code
job's inputs and handler by dotted path. Input addresses name roles
directly, and a draft validates in its role through
`commonplace-validate --artifact --role`, the call the shared check and the
worker's self-check both make.

The analysis plan has twenty-five jobs. Four are the consumer's own code:
`open`, `acquire`, `assemble` and `publish`. Ten are model jobs, one per
role. The other eleven are check, apply or artifact-check jobs, and each
restates what the layout already says about its roles: the candidate from
the filling job's primary output, the incumbent, the producer attempt and
its answered refusal, partner roles from cites and identity sources, the
criteria from the role's type and schema, and the validation parameters.
Their handlers are wrappers: the three analyst checks share one function
that names the role and partners; the three apply handlers share two. The
engine tests' toy plan has the same shape, with five check handlers made
by one factory from a job name, a role and a partner tuple.

What the wrappers add beyond the shared check is of two kinds. Shape,
which compares the candidate with partner members or its own fields:
declared record IDs surviving a correction, the memory report's source
identity matching the opening's, limits carried from a verification into
the synthesis. And checks that consult something outside the artifact: the
boundary's binding to the run parameters and the frozen source, the
feedback an author receives with cited records, and effect verification at
acquisition and publication. The report check that runs before
verification is structural: it validates the record roles as one snapshot
and writes the findings, including the artifact-level findings a role
check filters out, for the verifier to read.
Pinned-artifact validation refuses a member type with no Python type rule,
registered through one hard import at the end of
`src/commonplace/lib/validation.py`.

The workshop's [consumer surface](../../work/workflow-requirements/consumer-surface.md)
review rejected engine-generated check pairs because the engine must not
know what a content check is, and recorded a movable boundary: the
coordinator may take over a code job's interpretation while bookkeeping
stays in code. [The protocol as implemented](../../work/workflow-requirements/verification-protocol.md)
records what the engine, the shared check module and the analysis each
fix today. One production analysis has run through the engine.

## Problem

A consumer whose checks are structural should run from its type and a
short plan. Today it writes one handler per check job to hold a role and a
partner tuple, a verdict parser, an opener and a publisher, registers a
type rule it does not need, and declares every check job's inputs by hand,
copying the layout. Each copy is one more place for the generic logic to
drift, and the plan is long enough that its mission content, which roles
are written, in what order, from what, is hard to see.

## What the type determines and what it does not

The split follows ADR 110: shape belongs to the type, mission to the
instruction. The derivation holds for a consumer that adopts the named
protocol below. Adopting it is a plan choice; the layout does not imply
it, and a consumer with its own verdict language derives no apply job.

**From the layout alone**, for a role R: the check job that judges
candidates for R, with every input named above and the standard check as
its handler; and, for
a role that verifies others, the apply job that judges the verified roles'
handed versions over the `verifies` relations. Publication is a
coverage-gated copy with destination parameters.

**Mission, which stays declared**: which roles are model-written, with
which instruction, max attempts and auxiliary outputs. Which members a
worker reads, since reads exceed cites: the profile reads the
reconciliation it may not cite. Ordering between tiers: the profile and the
synthesis wait for report verification to accept the records, a gate the
layout cannot infer because the reconciliation reads the same records
unverified. Whether a verifier is handed a structural report before it
judges. And the consumer's own jobs: opening, acquisition, the boundary's
source binding and assembly.

**Not derivable at all**: effect verification. No schema states that a Git
checkout is still what a record says.

## Design

### Standard handlers in the reuse modules

The engine's reuse modules ship one handler for each recurring code job: a
check, a verdict application, a artifact check that validates its role inputs
as one snapshot and writes the findings as a document, a directory publish
and a minimal opener. A consumer with a domain check writes its own, as the
analysis does for its four jobs. The shared check learns its role and partners from the
declaration through an accessor exposing a code job's declared inputs on
the code attempt: the candidate's role is the role of the job that
produces the candidate input, and the partner roles are the role inputs.
Nothing is repeated, and a `parameters` block naming the same strings is
not used because it lets them drift from the inputs.

### Shape checks in the type

Identity fields in the layout, schema constants and type rules cover the
analysis artifact's shape checks. How a type selects a rule without the
hard import is the subject of
[type-selected Python validation checks](./type-selected-python-validation-checks.md)
and is not re-decided here; pinned-artifact validation treats a type with
no rule as schema-only rather than unsupported.

A type rule that reads a partner's content needs that partner in the
role's `cites`, so the derived check's snapshot holds it and the check's
judgment covers the relation. The synthesis therefore cites the record and
profile verifications, whose Limits it carries; `cites` demands no actual
citation, it is the scope a member's references and its rules may read.

A rule supplies a finding; it does not say whose version the finding
refuses. Every layout and rule finding names the role it belongs to
(ADR 111), and that is the attribution the standard handlers consume. The
limits rule between the synthesis and its verification reports a limit the
synthesis does not carry at the synthesis's role; the apply job, validating
the exact synthesis the verifier was handed against that exact verdict,
refuses the synthesis rather than the verdict, with Blockers `none`.

### The named verification protocol

Three of the analysis's conventions become a named, fixed protocol in the
reuse modules, which the standard apply handler implements:

- **The verdict document.** A verifying role's type declares `## Blockers`
  and `## Limits`, each exactly `none` or a list with one entry per
  finding. A verdict that fails its own content check is refused like any
  candidate and judges nothing.
- **Subject addressing.** With several subjects, every blocker starts with
  the role it addresses. With one subject, no prefix.
- **The partial-verdict policy.** Blockers `none` accepts every subject's
  handed version that validation did not refuse. Otherwise each addressed
  subject's handed version is refused with its blockers as findings, and a
  subject no blocker addresses is not judged at all: its gate stays
  unsettled until a blocker-free verdict. Accepting a subject another
  verifier has already accepted would also be coherent; this is the
  protocol's policy, fixed until a consumer needs another.

The standard apply handler validates the verdict and each handed subject
together, the subjects placed at their roles, and routes findings by the
role they name: findings at the verdict's role refuse the verdict and
nothing is applied; findings at a subject's role refuse that subject's
handed version, with the verdict's Limits appended, whatever Blockers
says. It does not infer blame from which rule ran. It refuses a subject
only for verdict-dependent findings: those at the subject's role that
appear with the verdict placed and do not appear without it, found by
validating twice. A finding the subject shows on its own belongs to the
subject's check, which already refused it; an apply that repeated it would
be the later refusal in force and would drop the blockers the check
carried forward from the subject's answered refusal, since the apply's
own Blockers section is `none`. Its refusal of a
subject is the subject's blockers followed by the verdict's Limits, plus
whatever a declared `feedback` function appends.

What stays the analysis's own: the report-check gate, that a verifier must
address structural failures, as a declared check on the apply job; the
feedback composition with cited records, as a declared `feedback`
function; and the materiality rules that say what a blocker and a limit
are, as instruction and type prose. A verification document keeps its
`verifies` stage field, checked by the type rule against its role, until
the rule derives it from the layout; the loader reads nothing from it.

### The compact plan

The plan lists the jobs that write and the consumer's own code jobs. A
loader in the reuse modules, not in the engine's scheduling, expands it
into the full plan: one check job per filled role, one apply job per role
with `verifies`, criteria from the roles'
types, and a coverage-gated publish from the disposition. The engine
receives the expanded plan and fixes it in the run metadata, so `status`,
`judge` and the attempt records see ordinary job names and the engine's
non-goal holds. A job that fills a role takes the role's name; derived
jobs are named `check-<role>` and `apply-<role>`. An entry declares only
mission:

```yaml
- role: memory
  instruction: jobs-engine/analyse-memory.md
  max-attempts: 3
  outputs: [report, answers]
  reads: {boundary: required, runtime: order-only}
- job: report-check
  handler: commonplace.artifactrun.handlers.artifact_check
  inputs: [boundary, runtime, memory, epistemic, reconciliation]
- role: report-verification
  reads: {boundary: required, report-check:findings: optional}
  checks:
    - {function: commonplace.lib.agentic_analysis.verification.report_check_gate,
       inputs: {findings: report-check:findings}}
  feedback: commonplace.lib.agentic_analysis.verification.cited_records
- role: memory-profile
  reads: {boundary: required, runtime: required, memory: required,
          epistemic: required, reconciliation: required}
  verified-by: [report-verification]
```

Plan keys and names use hyphens in both the compact and the full form;
the loader refuses a key or name with an underscore, so a misspelt plan
fails at start ([ADR 116](../adr/116-one-word-per-concept-across-prose-and-code.md)).

The syntax, stated so that the loader does not invent it:

- **Model entries.** `instruction` is a path relative to the plan file's
  directory, expanded to a library path. `files: {<name>: <library path>}`
  declares named file inputs such as contracts. `criteria` names groups as
  today. The loader adds the plan-level `inputs` and the validation
  `inputs` to every role-filling entry; the engine's own loader already
  adds the refusal input, and the frame prints the role and artifact
  lines the check command needs. `defaults.parameters` is merged under an entry's `parameters`.
- **Input names.** A role read is named after the role. A `job:output`
  read is named after the job when the output is the job's only one, else
  `<job>-<output>`, so the boundary's read of acquisition's one output is
  `acquire`. A read `refusal:<role>` is the filling job's latest refusal,
  named `<role>-refusal`. A name that today differs from this,
  such as the profile verifier's `profile` for the memory profile, is
  renamed in its instruction rather than given a naming syntax.
- **Reads.** `reads` defaults to the role's cites and identity sources,
  `required`. An explicit `reads` replaces the default, so an entry that
  names any read names them all. A read is a role, checked against the
  layout, or an output of a declared job in the form `job:output`, checked
  against the plan. Its mode is `required`, `optional` or `order-only`. An
  optional read absent at hand-out is an absent input, not a stop. An
  order-only read is handed and its version recorded, but a change to it
  does not make the job ready again; it maps to the engine's `order-only`
  input. Reads shape only the model job's hand-out.
- **Derived inputs.** The derived check takes its partners from the
  layout, not from `reads`: the roles the candidate's role copies identity
  from as required role inputs, since the layout refuses a member whose
  identity source is absent, and the roles it cites as optional role
  inputs, so the check covers the relations to the partners present
  whatever the model job was handed; plus the candidate, the producer
  attempt read order-only so that an identical rerun is not rechecked,
  the answered refusal, and the answers when the filling job declares a
  second output. A role a model job reads but does not cite, such as the
  reconciliation for the profile, is not a check partner: a change to it
  re-readies the model job, which is what matters, and not the check. The derived apply receives, from the verifier's
  attempt, the handed version of every role the verifier read, named
  `<role>-handed`, so its content acceptance covers the verdict's `cites`
  relations; the subjects are those the verifier role verifies. An
  incumbent or the opening metadata is an input of a declared check, not a
  derived one. An input only a declared
  check needs, which the model job must not see, is declared on the check
  entry's `inputs` in the same read grammar and reaches only the derived
  job.
- **Gates.** `verified-by` names verifiers; it expands into one
  accepted-judgment input over `<verifier>:verifies:<read>` for each read
  that verifier verifies. A verifier that verifies none of the entry's
  reads is an error. There is no plan-level default gating every read
  after its verifier; that would be wrong for the reconciliation.
- **Extensions.** `checks` lists functions, each either a bare dotted
  path or a mapping `{function: <dotted path>, inputs: {<name>: <read>}}`.
  Each receives the candidate the standard handler built and returns
  reasons; the candidate carries the attempt, so a check reads its own
  inputs and any handed input without more plumbing. `feedback` names one function receiving the subject role,
  its blockers and the handed snapshot and returning text the refusal
  appends. Both are consumed by the standard handlers, which call them.
- **Extensions.** A code job may carry an `extensions` mapping the engine
  fixes with the declaration and never interprets, exposed to the handler.
  The loader writes `checks` and `feedback` there; a check's declared inputs
  become ordinary job inputs. `frozen-source` stays a plan-level key in the
  expanded plan too, and handlers read it from the run. The name is distinct from
  `parameters`, which on a model job are substituted into its hand-out
  and on an attempt are the run's.
- **Publish.** The loader derives no publish job unless the plan asks for
  one. The analysis keeps its own assembly and publication, so the standard
  directory publish waits for a consumer without a publisher.
- **Standard jobs on roles.** A `job:` entry is a code job that neither
  fills a role nor is derived, running a standard handler over roles. Its
  `inputs` as a list name roles; as a mapping they take the full read
  grammar. Its `outputs` default to the handler's documented outputs,
  `findings` for the artifact check, and are declared otherwise. The artifact check
  validates its role inputs as one snapshot, writes the findings, and
  judges nothing. A consumer's own code jobs, opening, acquisition,
  assembly and publication, keep today's full form.
- **Names.** A consumer job named `check-<role>` or `apply-<role>` for a
  role the loader derives is an error, not a replacement; a consumer that
  needs its own check for a derived role declares it with `checks`. The
  loader's names differ from today's plan in twelve jobs:

  | Today | Derived |
  |---|---|
  | reconcile, check-reconcile | reconciliation, check-reconciliation |
  | verify, apply-verify | report-verification, apply-report-verification |
  | profile, check-profile | memory-profile, check-memory-profile |
  | verify-profile, apply-verify-profile | profile-verification, apply-profile-verification |
  | synthesize, check-synthesize | synthesis, check-synthesis |
  | verify-synthesis, apply-verify-synthesis | synthesis-verification, apply-synthesis-verification |

  The other thirteen keep their names. A run directory started under the
  old names is not resumed under the new ones, which is the driver's
  existing rule for old or mixed run directories.
- **Criteria.** A derived check, apply or standard job's criteria are the
  type closure of its roles: each role's type spec, its schema and the
  base schemas it references, plus one plan-level group, conventionally
  `check`, for files that type rules read but no type references, if any
  remain once the records contract is inside the set type. Model jobs keep
  naming their groups explicitly, as today.
- **The frozen source.** A plan-level `frozen-source: <role>` names the
  member whose `source` field pins the source the run may inspect. The
  loader passes it to every derived check, apply and artifact check, which read
  the field from that role's input; where the job has no such input, the
  loader adds the role as a required role input, and a derived apply uses
  the handed version when the verifier read the role. It is a plan declaration because it
  is the run's authorization to inspect a checkout, not shape; the type
  cannot say what a run is allowed to read. Without a pin, quotation
  validation fails rather than reporting quotations as unverified, so for
  the pinning role's own candidate the standard check runs the declared
  checks first, the boundary's binding to acquisition, and inspects the
  candidate's source only when they pass. Authority stays with
  acquisition.
- **The rest of the plan.** The consumer's own code jobs, the criteria
  groups model jobs name, plan-level `inputs` every model job receives,
  such as the opening metadata, and run parameters keep today's form. A
  plan-level `defaults` block carries `max-attempts` for entries that do
  not say. The standard handlers validate with the library's parent as the
  project root, which holds for a source checkout and the analysis
  worktrees; a package-installed consumer would need the run metadata to
  record the root, and none exists.

The compact analysis plan is 237 lines against the hand-written 498: the
criteria groups take about 45 and the four full-form jobs about 60.
Widening the type's `cites` to mean reads was rejected because it would
make the validator read mission.

### The hand-out template and derived type inputs

Each analysis job instruction is about half boilerplate: read order, the
follow list, what the inputs are, answers, the self-check and the return.
This extension, approved 2026-10-09, moves that boilerplate into one file
the plan names and derives the type inputs from the layout, so a job
instruction holds only its mission.

- **The engine keeps the frame.** The hand-out module still writes the
  "Follow <instruction> with:" line, the input lines, the reading batches,
  the problem line and the worker-identity section. A plan-level
  `handout: <path>`, relative to the plan file like an entry's
  instruction, names a Markdown file the engine renders as one section of
  that frame, after the input lines and before the reading batches. A plan
  without the key gets today's prompt, so the toy plan is untouched. One
  composer: the template fills its slot and nothing else.
- **Slots are lines.** Every `name = value` line the frame prints is
  available in the template as `{name}` with the same value, and no other
  slot exists; the frame prints `role` for role-filling jobs and
  `artifact`, the run's artifact directory, so `{role}` and `{artifact}`
  are lines. So `{output}` and `{output-answers}` are paths, as the lines
  are, and `{member-type}` and `{<role>-type}` are the
  handed type files. The per-job `validation-artifact` and
  `validation-role` parameters go: they duplicated those two lines, and
  the check command reads `{command-path}/commonplace-validate {output}
  --artifact {artifact} --role {role}`. A run parameter the template needs is declared in
  the plan's `parameters`, which prints it as a line; `{param:<name>}` and
  `{artifact}` appear only there, so the plan is the one place that
  substitutes run values. An unknown placeholder is a plan error at
  start. One conditional: a paragraph whose first line is `[<name>]` is
  kept, without the marker, when the prompt has that line, so
  `[output-answers]` marks the answers paragraph and `[refusal]` would
  mark a repair one; a condition must name a line some job prints or one
  of the frame's `output-*` or `previous-*` families, so a plan cut down
  for a test does not fail on a paragraph no job needs. Decided 2026-10-09 after the first version gave
  `{output}` the output's name while the line gave its path, and the
  template used a third notation to reach the line. The same rule placed
  the command path: the opener had written it inside the opening JSON,
  which no slot reaches, so the analysis's start passes it as a run
  parameter and the check command renders whole.
- **Derived type inputs.** Each role-filling model job receives as file
  inputs its own role's type as `member-type` and the type of each role it
  reads as `<role>-type`. These replace the `files:` entries that named
  type specs; `files:` stays for shared contracts a member type refers
  to, such as the records contract. The set type is not handed to
  workers: a producer needs its member type, the types of what it reads
  and the contracts those name, and nothing about the whole artifact,
  whose shape it learns only through what it is handed and the check's
  findings (decided 2026-10-09; the first version handed the set type
  through a `type` input address, now unused). The template itself is a
  pinned file input of every model job, rendered rather than listed, so
  editing it re-hands-out the job.
- **Precedence, stated once in the template.** The member type owns what
  the member contains and wins over the mission file on conflict; the
  worker rules own execution. The hand-out is the complete write procedure, and the
  repository's authoring skills do not apply to a worker: they assume an
  operator, the KB as evidence and KB destinations. This is the split the
  connect skill already makes, execution in the skill and the contract in
  the type.
- **Mission files shrink** to a purpose sentence and what the job must
  establish and challenge. The loader does not police this.
- **Layout facts as lines** (decided 2026-10-10, under
  [frontloading](../../notes/frontloading-spares-execution-context.md)).
  The frame prints, for a role-filling job, `identity`, the fields it
  repeats and from which roles, and `cites`, the roles it may cite, and
  for a verifying role `verifies`; the prompt section says each in one
  sentence, and a `[verifies]` paragraph names the blocker addressees, so
  no job instruction restates the layout and no producer learns its scope
  from a failed check. The opening's `capture-directory` and
  `source-identity` become plan parameters printed as lines, as
  `command-path` did, so no worker reads the opening JSON. Deferred with
  its trigger: a list of the limits the synthesis must carry would need a
  consumer code job reading the verdicts; it waits for a run in which the
  limit-not-carried refusal actually fires. A list of citable records was
  considered and dropped: the writer reads the cited members anyway, and
  the destination follows from the ID by one case change and the prefix's
  member.
- **Ordering.** This lands with the contract moves: the boundary contract
  into the boundary type; the records contract stays a shared member-level
  contract that the member types declaring or citing records refer to;
  the sources contract splits into the boundary type, for what a source
  declaration is, and the worker rules, for how to inspect and quote. The
  set type keeps its minimal maintainer body and is read by the validator
  and maintainers only. A member type with its referenced contracts is
  then the complete contract for its producer, testable without a set,
  and reusable by another directory artifact.

### Run binding as identity

The engine fixes the run parameters in the run metadata. Letting a layout
identity source name them makes a member's binding to its run, such as the
boundary's run id and source identity, a shape check in draft validation,
so the opener stops duplicating it. A generic rule that declared
identifiers survive a correction, given the type's identifier grammar,
joins the correction protocol the same way. This comes last because it
deletes checks the opener and the analyst check carry until then.

## Sequence

1. Standard handlers and the input accessor, proven by deleting the engine
   tests' check handlers. Done 2026-10-09 for the check and the artifact check;
   the directory publish and the minimal opener wait for step 3, since the
   toy plan has nothing to test them on. No analysis shape check qualified
   for the type without rule selection or run binding, so that part folds
   into step 4 and the type-selected checks proposal.
2. The named protocol as the standard apply handler's contract, proven on
   the toy plan's verifier. Done 2026-10-09.
3. The compact plan and its loader, with the `checks` and `feedback`
   extensions, proven by the fidelity tests and then by switching the
   analysis skill to the compact plan. The extensions are part of this
   step, not a later escape: the report-check gate and the cited-records
   feedback need them on the first compact analysis plan. Done 2026-10-09
   except the production run: the analysis runs on the compact plan, the
   wrappers are deleted, and the fidelity test applies the decided
   differences to a frozen copy of the hand-written plan and requires
   equality. The judgment test compared each wrapper with its standard
   replacement on the same pins before the wrappers went; the profile and
   synthesis checks were not compared, since their derived jobs lack the
   reconciliation partner. The
   [implementation review](../../work/workflow-requirements/compact-plan-implementation-review.md)
   of 2026-10-09 found one regression and four gaps, with these rulings:
   the run metadata records the compact plan's own digest at expansion and
   integration compares that with the shipped file, keeping the type
   guard; a derived apply gets its frozen-source input as stated above;
   the type closure uses the validator's reference resolver, not its own;
   a code job whose judgment stopped holding because an optional basis
   input disappeared becomes ready, model jobs unchanged; and the fidelity
   test asserts every derived job's declared checks and feedback. All five
   are fixed as of 2026-10-09.
4. Run binding as identity, deleting the opener's and the analyst check's
   remaining duplicates.
5. The hand-out template, in three parts: template support in the engine
   and loader with the toy plan untouched; the analysis template, the
   mission-file shrink and the derived type inputs with the old contract
   files still in place; then the contract moves, one commit each,
   boundary, records, sources. Independent of step 4. The first two parts
   are done 2026-10-09: the toy prompts are byte-identical, the ten
   mission files hold about 2,900 words from 4,950, and the plan is 219
   lines. The contract moves are done the same day: the boundary contract
   is in the boundary type; the sources contract is deleted, its
   declaration rules and evidence-layer table in the boundary type, its
   inspection and quotation rules in the worker rules, and its
   evidence-interpretation rules, what a finding may claim from its
   evidence, in the records contract; the records contract is referred to
   from the seven record-citing member types; no worker receives the set
   type. One analysis to publication remains, the operator's call.
   Alongside, [ADR 115](../adr/115-analysis-records-are-cited-by-markdown-links.md)
   made record citations Markdown links resolved by the validator's link
   code within the layout's `cites` scope, so the records contract keeps
   what a record means and the custom token scanner is gone: the
   citation relation is declared at both levels, `cites` as its schema
   and links as its instances.

## Not taken

- **The coordinator judges.** For a consumer without a verifier, the
  coordinator could read the verification and record the judgment through
  the operator command, the movable boundary the workshop recorded. It
  removes the deterministic part that applies a verdict to the exact
  versions the verifier was handed, so it waits for a consumer that does
  not need that precision.
- **A typed artifact-run directory**, with the artifact, the run metadata
  and acquired sources as declared parts so that "outside the artifact"
  becomes "inside the run". Run binding as identity covers the one case
  the analysis has at a fraction of the cost.
- **Subjects declared in the plan** rather than the type: decided against
  in ADR 114.
- **Configurable verdict policies.** One fixed protocol, named; a second
  policy is added when a consumer needs it, not before.

## Forces

- Per-job configuration in Python is the cheapest thing to write and the
  easiest to let drift from the declaration it mirrors. Deriving it from the
  job's inputs, or from the layout, has no second copy.
- The engine's non-goal, no validation policy and no knowledge of content
  checks, draws the line between the reuse modules and the engine's
  scheduling. The handlers and the loader both stay on the reuse side: the
  engine still receives a full plan.
- Shape belongs to the type and mission to the instruction (ADR 110). Max
  attempts, instructions, reads and gates are mission and stay in the plan.
- A second declaration shape is worth its cost only if it stays faithful to
  the hand-written plan. The fidelity tests make that a property the tests
  hold, not a hope.
- Role and job are different things: a role is a position the type
  declares, a job is a unit of work. Naming the filling job after its role
  removes a redirection without conflating them.
- Effect verification cannot be declared. Any declarative route ends at a
  named function for it.
- The toy plan in the engine tests is a second consumer that exists today,
  so the handlers and the loader have a test subject before any new
  consumer does.

## Operativity

- **Standard handlers and the compact plan.** Consumed by a plan naming
  handlers in the reuse modules, read by the loader, which the engine's
  `start` already calls to fix the declaration. The first such plan is the
  engine tests' toy plan; the second is the compact analysis plan, consumed
  by the analysis skill through `commonplace-analysis start`.
- **Shape checks in the type.** Consumed by pinned-artifact validation at
  publication and by draft validation in the standard check.
- **Run binding as identity.** Consumed by draft validation through the
  layout parser.
- **Extensions.** Consumed by the standard check and apply handlers, which
  call the listed functions.

The automated evaluation this adds is the standard check's draft
validation, warranted by the type contracts and schemas. It establishes
form and relations, not analytical truth.

## Adoption criteria

- Step 1: the engine tests' toy plan runs to publication with no check
  handler outside the engine's reuse modules.
- Step 2: the toy plan's apply job is the standard handler, and tests
  show a verdict with one blocker refuses the addressed subject and leaves
  the others unsettled; a verdict-dependent finding refuses its subject
  with Blockers `none`; a finding the subject shows on its own is left to
  its check, and a blocker-free verdict still accepts that subject over
  the `verifies` relation, since the verdict records what the verifier
  judged and structural currency is the check's business. Done
  2026-10-09.
- Step 3: the loader's expansion of a compact analysis plan is equivalent
  to the hand-written plan, asserted by four tests. Equivalence is equality
  of each job's inputs, outputs and parameters after the renamings listed
  above, with handlers compared by substitution: a consumer wrapper may be
  replaced by the standard handler, and a judgment test shows the two
  record the same judgments on the same inputs. Criteria are compared by
  inclusion, not equality: a recording criterion snapshot lists the files
  validation opens, and the derived set must include them. Today's groups
  are cumulative and over-include, for instance `check-profile` pins the
  reconciliation type the profile does not cite; the extras are intended
  removals, listed by the test. A
  semantic-change test shows that one edit to a compact entry changes the
  expansion. A migration test shows that the gates once named as `cites`
  relations are `verifies` relations with the same acceptances. An
  execution test runs the expanded plan through the engine tests' scenario
  to the same judgments and coverage as the hand-written one. Then one
  analysis runs through the compact plan to publication, with the
  report-check gate and the cited-records feedback as declared functions
  and the consumer's apply handlers deleted. All but the production run
  are met as of 2026-10-09; the run is the operator's call.
- Step 4: the opener's run-binding checks are deleted after draft
  validation reports the same mismatches.
- Step 5: the toy plan's prompts change only by the frame's `role` and
  `artifact` lines, which the slots rule added; no analysis job instruction says what an input is or
  where it comes from, and none names an output, an answers file or the
  check command, though a mission names the inputs it works from; no model
  job in the compact analysis plan lists a type under `files:`; the
  boundary and sources contract files are gone, the records contract is
  referred to only from member types, and no worker receives the set
  type; and one analysis runs to publication on the templated hand-outs.
