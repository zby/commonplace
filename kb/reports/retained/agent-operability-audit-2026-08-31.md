# Agent operability audit — 2026-08-31

This frozen report evaluates Commonplace from the position of an agent that
must understand the project, choose and execute valid actions, verify the
result, and leave the system better prepared for later work. It asks how to
make the whole system more agent-intuitive, agent-ergonomic, and
agent-accretive while preserving correctness and warrant and reducing model,
tool, elapsed-time, and human-attention costs.

The central result is that Commonplace already has most of the right knowledge
primitives, but it does not yet compile them into an adequate operating view.
The repository is a strong knowledge substrate and a weak cockpit. An agent
can usually discover the applicable contracts, evidence, state, and commands,
but it must reconstruct the relationship among them during each task. That
reconstruction consumes context, repeats across agents, hides lifecycle debt,
and leaves the learning loop open.

The highest-leverage change is to make a bounded **operation** the unit the
agent experiences. Each operation should expose its purpose, current state,
authority, relevant inputs, valid actions, expected effects, cost, acceptance
checks, and resumable outcome. A derived project-status view should tell the
agent which operations now matter. A task-specific context compiler should
assemble only the material needed for the selected operation. Execution should
produce a compact receipt. Evidence from receipts should enter a governed
candidate queue from which useful learning can become a note, skill, check,
cue, or system change and later be tested, relaxed, or retired.

This design does not replace authored Markdown, Git history, collection
contracts, or deterministic commands. It makes those authorities legible at
the moment of action.

## Result in operator terms

Commonplace should optimize for this sequence:

1. Show the agent what is true now and what deserves attention.
2. Let the agent select a named, bounded operation.
3. Compile the smallest sufficient and provenance-preserving context for it.
4. Expose valid actions with authority, effects, cost, and recovery information.
5. Verify the result and emit a compact, resumable receipt.
6. Turn only consequential evidence into a governed learning candidate.
7. Promote, test, and eventually retire retained guidance according to observed
   effects.

The practical priority is therefore not to add more prose, more autonomous
agents, or a vector database. It is to add a thin agent-operations layer over
the sources and commands that already exist. The first useful slice is a
read-only situation report, consistent compact and machine-readable command
results, project-version coherence checks, lifecycle validation, and one
operation-packet pilot.

## Evaluation frame

The three qualities in the request are related but distinct:

| Quality | Operational meaning | Failure signal |
|---|---|---|
| Agent-intuitive | The current situation suggests the next valid actions and makes their consequences apparent without repository archaeology. | The agent must infer hidden state, search for the controlling contract, or guess which command owns a transition. |
| Agent-ergonomic | The system minimizes context volume, tool calls, retries, switching, and human decisions while keeping correctness and warrant as hard constraints. | Large fixed loads, verbose diagnostics, repeated discovery, ambiguous failures, and manual state reconciliation consume the run. |
| Agent-accretive | Work leaves governed evidence that improves later selection, execution, or evaluation, while obsolete guidance is discoverable and removable. | Useful corrections die in chat history, observations accumulate without consumers, or rules grow without effect measurement and retirement. |

The objective is lexicographic rather than a loose weighted average:

1. Satisfy correctness, warrant, authority, and safety constraints.
2. Among satisfactory paths, minimize human judgment, loaded context, model
   calls, tool calls, elapsed time, and rework.
3. Prefer paths that create a measured improvement for future operations.

This follows Commonplace's declared goal of increasing useful,
well-warranted knowledge work per unit of human judgment, while making explicit
that a cheap but unreliable path is not an optimization.

## Inputs, snapshot, and method

The repository corpus was inspected at commit
`7ced7b1dd67566c138be6e74efce23fa671193ea` on 2026-08-31. The worktree was
clean at the start of the audit. Unrelated uncommitted changes appeared while
this report was being written; they were not inspected as evidence or changed
by this audit.

The audit covered:

- the root doctrine, collection contracts, type contracts, skill instructions,
  package scaffold, command implementations, and architecture documentation;
- the navigation, write, validation, review, freshness, lifecycle, and upgrade
  paths an agent encounters;
- the current proposals and workshops that already address parts of the
  problem;
- read-only command output, repository counts, Git activity, and this
  checkout's local Commonplace store; and
- actual review-link consumption telemetry, not only the cost of links offered
  to a reviewer.

The analysis used lexical search, scoped file listings, source inspection,
command help, deterministic validation, SQLite queries against the local store,
and small shell measurements. It did not change the subject while gathering
evidence. No web sources were needed. Byte counts are a reproducible proxy for
possible prompt volume, not a provider-specific token count.

The synthesis was produced by Codex under the repository's `AGENTS.md` and the
`operator-brief` instruction. The runtime did not expose a more specific model
identifier. The recommendations are design judgment; the measurements below
are the evidence that constrains that judgment.

## The driver-seat test

At any point in a run, I want the system to answer seven questions:

1. What outcome am I trying to produce?
2. What is true now, and which evidence is relevant?
3. Which actions are valid and within my authority?
4. What will each action read, write, cost, and invalidate?
5. How will I know that the action succeeded?
6. How can the work be resumed, reversed, or repaired?
7. What, if anything, should change for the next agent?

Commonplace makes nearly every answer available in principle. The problem is
that the answers live in different places: doctrine, collection contracts,
type files, skills, READMEs, proposals, workspaces, Git, the SQLite store, and
individual command conventions. The agent must join them in its own bounded
context. That is exactly the repeated inference the system should frontload.

## What is already strong

The target design should preserve the following properties.

### Authored authority is inspectable

Markdown and Git make durable knowledge, system definitions, provenance, and
change history inspectable without a proprietary runtime. Collection and type
contracts constrain content close to the artifacts they govern. The
[storage architecture](../../reference/storage-architecture.md) correctly
separates authored truth from derived and operational state.

### Progressive disclosure is already the intended navigation model

The [navigation design](../../reference/navigation.md) starts with cheap
lexical and curated surfaces and allows an agent to decide what to open next.
The notes on
[agent-directed navigation](../../notes/agents-navigate-by-deciding-what-to-read-next.md),
[fluid resolution](../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md),
and
[local materialization](../../notes/local-materialization-should-outperform-distant-declarations.md)
give the right theoretical basis. The missing piece is an execution-oriented
projection of those surfaces, not a different theory of navigation.

### Deterministic and semantic checks are separated

Structural checks are code. Semantic review is snapshot-anchored and records
its model partition, inputs, outcome, and freshness. This is substantially more
trustworthy than treating any last model answer as current truth. The
[freshness architecture](../../reference/freshness-architecture.md) and
[review architecture](../../reference/review-architecture.md) are reusable
foundations for broader impact tracking.

### Skills are bounded procedures rather than one universal prompt

The promoted skills expose recognizable operations such as write, connect,
ground, ingest, and validate. This is much closer to an agent-usable interface
than a single all-purpose instruction. The improvement is to give the
operations a shared envelope and state model, not to collapse them.

### Human authority is treated as scarce and consequential

The system distinguishes evidence from acceptance and does not silently turn
model output into doctrine. That boundary should remain. The future system
should spend human attention only where authority or judgment actually
requires it and should make those decisions easy to inspect.

### Review telemetry demonstrates the right loading pattern

The retained
[review-link availability baseline](./review-link-availability.md) found a
median offered cost of 67,009 bytes of linked artifacts and a p90 of 148,267
bytes. In the later local telemetry examined for this audit, 752 of 957
completed review pairs with link-use data opened no linked artifact. Among the
205 pairs that did open links, the median consumed linked content was 60,370
bytes and the p90 was 152,363 bytes. Only 10 of the 957 pairs reported stopping
for budget; 947 reported sufficiency.

This does not prove review quality. It does show a valuable interface pattern:
offer cheap, well-described affordances and let the agent load evidence on
demand. Do not force every available relation into context.

## Evidence of the operating gap

The measurements below describe one live checkout, not an invariant property
of every installed Commonplace project. Together they show where the present
interface makes an agent reconstruct or carry state.

| Surface | Observation on 2026-08-31 | Operational consequence |
|---|---:|---|
| Always-loaded root doctrine | `AGENTS.md` was 23,803 bytes and 3,206 words. | Orientation has a meaningful fixed cost before local contracts or task evidence. |
| Ordinary note-write fixed inputs | Root doctrine, write skill, notes collection contract, and note type totaled 58,426 bytes before the target and related artifacts. | A routine operation starts with a large invariant load that could partly be compiled or referenced by hash. |
| Notes discovery surface | A complete title listing was 53,931 bytes; title plus description listings were about 163.6 KB before body search. | Corpus-wide candidate generation is too expensive to repeat as an incidental step in every operation. |
| Skill corpus | Ten promoted `cp-skill-*` instructions totaled about 128 KB; the largest was 26,747 bytes. | Selective skill activation is essential, and common envelopes should not be copied into every skill. |
| Deterministic validation | Notes reported 408 passes and 5 failures across 413 artifacts; work reported 608 passes and 1 failure across 609 artifacts. The default note output exceeded 9,600 lines. | The checks find real state, but the default presentation obscures the decision-ready summary and spends output context. |
| Review freshness | The local store had 8,734 registered review-pair targets: 271 fresh and 8,463 stale. | Freshness is represented precisely but not converted into a small prioritized decision surface. |
| Review execution | The store held 6,879 jobs: 6,521 completed, 205 failed, and 153 queued. Those queued jobs represented 775 pairs; failed jobs represented 1,070 pairs. | Backlog, failure, and current warning state require manual joins across several command outputs. |
| Current warnings | Nine actionable warning findings affected four notes, while 1,437 additional warning pairs were stale. | The distinction between actionable current evidence and historical debt exists, but an agent must ask for it deliberately. |
| Workshop registry | `kb/work/` had 74 top-level directories. The active-work README resolved to 57 distinct directories, leaving 17 unlisted. | The lifecycle contract is not fully enforced; a cold-start agent cannot trust the registry as complete. |
| Workshop freshness | `semantic-search-replacement` remained active even though current source and documentation no longer used the qmd path it was created to replace. | Finished, superseded, or irrelevant work can keep attracting attention. |
| Task state | One backlog task declared every subtask complete; a recurring task pointed to a missing file; no active task artifact was present. | Directory placement and content can disagree without producing a compact lifecycle error. |
| Candidate capture | `kb/log.md` contained 44 physical lines but 28,902 bytes and 3,626 words, including long undated observations with no explicit status or consumer. | Potential learning accumulates, but it is hard to rank, deduplicate, promote, or retire. |
| Proposal frontier | There were 29 live proposal files. Median age was 34 days; 16 were older than 30 days and 5 older than 60 days. | The design frontier is visible but not ordered by dependency, consequence, evidence, or next review trigger. |
| Project upgrades | `commonplace-init` preserves differing installed files, and installed-project updates are a manual diff-and-merge process. No project scaffold version or canonical projection lock was found. | A project can silently combine one user-level CLI version with older copied doctrine, skills, and library artifacts. |
| Command protocol | Twenty-two `commonplace-*` commands exposed independent interfaces. Four advertised an explicit `--json` mode; compact summaries, stable action identifiers, plan/apply, and receipts were not uniform. | Agents need command-specific parsing and cannot reliably chain every operation without rereading help or source. |
| Repository activity | August 2026 contained 829 commits and 6,556 file-change events, including 1,917 under `kb/work/` and 1,888 under `kb/sources/`. | At this change rate, manually maintained registries and copied projections need mechanical reconciliation. Activity alone does not establish defect rate. |

The local store occupied about 696 MB, including a 43 MB SQLite database and
1,179 review-job directories. Size alone is not a defect. It does make
retention, supersession, cancellation, and garbage-collection ownership part
of the operating design rather than optional housekeeping.

## Diagnosis: the system is artifact-complete but operation-incomplete

### The interface presents components, not the situation

The repository has commands for validation, freshness, warnings, jobs,
snapshots, relocation, and review. It has separate registries for work, tasks,
proposals, and reports. Each component can answer a local question. No single
read-only projection answers: “What needs attention now, why, and what can I do
about it?”

The result is fragmented observability. A sophisticated agent can reconstruct
the situation, but doing so is expensive and fragile. A new agent cannot tell
whether silence means health, an unqueried subsystem, or a stale registry.

### The system repeatedly charges for invariant reasoning

An operation commonly reloads broad doctrine, a long skill, a collection
contract, a type, target content, and corpus discovery output. Much of that
material is stable or reducible to the clauses relevant to one operation. The
[frontloading principle](../../notes/frontloading-spares-execution-context.md)
applies directly: resolve known scope, authority, paths, and checks before the
model call rather than asking every agent to derive them again.

The risk is not only token cost. Broad context increases the number of
plausible instructions, stale alternatives, and unrelated artifacts the model
must distinguish. Context economy and accuracy are aligned when the compiler
removes irrelevant choices without hiding provenance.

### Lifecycle state is declared but not closed

Workshops, tasks, proposals, review pairs, jobs, and observations all have
different partial notions of active, complete, stale, superseded, or retained.
Some are encoded in directories, some in prose, some in SQLite, and some only
in a README. Several declared invariants are not validated. The system can
therefore accrete work faster than it retires or promotes it.

This is a control problem, not a request for more cleanup instructions. Every
durable queue needs an owner, explicit states, allowed transitions, a next
trigger, and a terminal disposition.

### The learning path stops between noticing and uptake

The
[agent-memory coverage assessment](../../reference/agent-memory-coverage.md)
and
[change-candidate inventory](../../reference/where-change-candidates-come-from-in-commonplace.md)
already identify validation, the log, connect reports, freshness, and agent
initiative as noticing channels. None provides an end-to-end path from an
observed event to a ranked candidate, governed promotion, situation-specific
activation, and measured behavioral effect.

As a result, Commonplace is accretive mainly when an operator deliberately
runs a writing or review workflow. It does not yet learn economically from
ordinary successful and failed operations.

### Installation can separate the command from its doctrine

One editable user-level command installation can serve several projects while
each project contains copied library and skill material. Preservation of local
edits is correct, but without a recorded source version and three-way upgrade
base the system cannot distinguish intentional customization from accidental
drift. An agent can execute a current command under an older textual contract
without receiving a compatibility warning.

### Errors are informative but not uniformly actionable

A validator can emit thousands of passing rows around a few failures. A review
job can fail with a provider exit code. A stale pair can represent an important
regression or harmless historical evidence. These are facts, not yet actions.
An ergonomic interface attaches a stable diagnostic identifier, consequence,
owner, and permitted next transitions to each relevant fact.

## Target operating model

The smallest coherent target has four layers:

```text
Authored authority
Markdown + Git + collection/type contracts + canonical skills
        |
        v
Derived situation model
indexes + dependency graph + operational state + version/health projection
        |
        v
Bounded operation
goal + scope + authority + context packet + actions + checks + budget
        |
        v
Verified receipt
result + changed inputs + evidence + cost + recovery + candidate signals
        |
        +----------> no durable lesson: retain only normal history/state
        |
        v
Governed learning candidate
review -> promote to note/skill/check/cue/change -> evaluate -> retain/relax/retire
```

The upper layer remains authoritative. Everything in the derived situation
model must be rebuildable or have an explicit operational-state owner. The
operation packet is transient and must cite hashes or paths back to its inputs.
The receipt records enough state to resume or explain the operation without
replaying a raw conversation. Promotion remains a separate authority-bearing
transition.

### Design rules for the target

1. **Offer affordances; do not preload possibilities.** Show a compact action
   table and load details only when selected.
2. **Compile from closed inputs.** Operation-specific compilers take declared
   paths, modes, state, and contracts. Avoid a generic context-provider
   framework whose hidden selection logic becomes a new authority.
3. **Keep one canonical source.** Derived indexes, graph edges, packets, and
   projections cite or hash the canonical artifact and never become a second
   editable doctrine.
4. **Make authority explicit at the transition.** Reading, proposing,
   validating, applying, promoting, and retiring are different permissions.
5. **Prefer stable identifiers to prose parsing.** Diagnostics, operations,
   candidates, and effects need IDs that commands and agents can carry.
6. **Separate plan, apply, and receipt.** A mutating operation first resolves
   its exact targets and consequences, applies only with the required
   authority, then emits the observed result.
7. **Capture high-signal evidence before raw traces.** Intent, corrections,
   retries, failures, operator decisions, checks, and outcomes are cheaper and
   safer than retaining every conversational token.
8. **Require a consumer and retirement rule for durable state.** A register
   without a query, transition, or cleanup owner is deferred entropy.
9. **Measure behavior, not artifact count.** More notes, gates, or links are
   valuable only when they improve representative operations.

## Recommended capabilities

### 1. A read-only situation and next-action projection

Add one compact front door—provisionally `commonplace-status`—that composes
existing deterministic endpoints without replacing them. Its default output
should fit in a small terminal view. It should also have a stable structured
form for agents and drill-down commands for evidence.

The projection should include:

- project identity, Git state, configuration, command version, scaffold or
  library version, and detected projection skew;
- active and resumable operations, including unfinished apply plans;
- validation failures summarized by stable diagnostic ID and affected scope;
- current actionable review findings, queue failures, and materially stale
  cohorts rather than a dump of every pair;
- unregistered, contradictory, aged, or superseded workshops and tasks;
- proposals and learning candidates that have reached their next trigger; and
- ranked candidate actions.

Each candidate action should state:

| Field | Question answered |
|---|---|
| ID and operation kind | What can another command select without parsing prose? |
| Reason | Why is this action being offered now? |
| Expected effect | What state or artifact would change? |
| Authority | Can the agent read, propose, plan, apply, promote, or retire? |
| Cost estimate | What files, context bytes, model calls, or human decisions are expected? |
| Risk and reversibility | What could be harmed, and how is recovery performed? |
| Acceptance check | What proves completion? |
| Drill-down | How can the agent inspect the supporting evidence? |

The ranking should be deterministic where possible: blocking failures before
warnings, current evidence before stale evidence, explicit due triggers before
age alone, and high-consequence dependency impact before cosmetic debt. Model
judgment can rank ambiguous candidates after the deterministic filter, with
its evidence and partition recorded.

This command should remain read-only. It is a projection, not an autonomous
scheduler and not a new source of truth.

### 2. Project-version coherence and a three-way upgrade path

Record the framework inputs from which a project was initialized or last
upgraded. The exact storage format should be decided with the packaging design,
but the record needs at least:

- framework/package version and source identity;
- hashes of canonical copied library artifacts and projected skills;
- the prior baseline needed to distinguish local edits from upstream edits;
- the active command version and supported schema range; and
- declared local overrides.

`commonplace-status` should diagnose four cases separately: current,
intentionally customized, upstream update available, and incompatible skew. An
upgrade operation should generate a three-way plan showing unchanged updates,
local-only edits, upstream-only edits, and conflicts. Applying that plan should
be explicit and should emit a receipt. Rerunning initialization should not be
the upgrade mechanism.

This is a prerequisite for trusting every later compiled context. A perfect
packet assembled from an unknown mixture of versions is precisely wrong.

### 3. Lifecycle contracts enforced as state machines

Give workshops, tasks, proposals, review jobs, learning candidates, and other
durable queues explicit states and mechanically checked transitions. Not every
class needs the same schema, but each needs:

- a stable identity and owner;
- created and last-material-change times;
- current state;
- the event or evidence that permits the next transition;
- a next review or wake trigger;
- links to outputs and dependencies; and
- terminal dispositions such as completed, promoted, rejected, superseded,
  cancelled, or expired.

Extend deterministic validation to catch at least:

- a workshop directory missing from its active registry or required framing;
- a completed checklist left in backlog;
- a recurring task whose target is absent;
- a live proposal with no current-state anchor or next review trigger;
- a queue item whose dependency or owner disappeared; and
- derived review state eligible for an owner-approved cleanup plan.

Age should raise attention, not decide deletion. The system should generate a
retirement or reconciliation plan and preserve authority at apply time.

### 4. A closed, operation-specific context compiler

Generalize the existing
[deterministic write-context proposal](../../reference/proposals/deterministic-write-context-assembly.md)
into a family of small compilers, one per consequential operation kind. Do not
start with a universal provider API. Start with operations whose inputs and
acceptance are already understood: write one note, validate and repair one
artifact, triage current review warnings, resume one workshop, and plan one
upgrade.

An operation packet should contain:

```text
operation ID and kind
requested outcome and acceptance criteria
current state and resume point
scope and explicit exclusions
authority and allowed effects
canonical inputs with paths, roles, hashes, and freshness
only the applicable contract clauses
ranked optional evidence with descriptions and size estimates
available actions and expected transitions
budget or stopping policy
unresolved choices that actually require judgment
required verification and receipt destination
```

The packet should explain why each included item is present and expose omitted
but available evidence as an on-demand route. It should be inspectable as a
build product and reproducible from its declared inputs. It should not persist
as an alternative editable instruction.

The compiler can shrink context in three ways without weakening doctrine:

- resolve known paths, types, and collection scope before the model call;
- select relevant clauses while retaining citations to the complete binding
  source; and
- replace repeated discovery listings with a ranked, query-specific result
  that records why each candidate was offered.

### 5. One command protocol for human and agent consumers

Keep the existing composable commands, but give them a common response
envelope. Every diagnostic command should support a concise default and a
stable structured result. Every consequential mutation should support the
equivalent of inspect, plan, apply, and receipt, even if the exact flags differ
for a sound domain reason.

The common envelope should distinguish:

- `status`: success, warning, blocked, failed;
- `diagnostics`: stable ID, severity, subject, reason, and evidence route;
- `actions`: stable ID, required authority, expected effect, and command form;
- `summary`: counts and the highest-priority next decision;
- `details`: optional rows or artifacts, not emitted by default;
- `provenance`: command version, configuration, and input identity; and
- `receipt`: observed changes, checks, cost, and resume or recovery state.

In particular, `commonplace-validate` should default to the compact result that
an agent needs—counts, failing subjects, diagnostic IDs, and next drill-down—
instead of printing every passing artifact. A full transcript remains useful
behind an explicit verbosity option. Structured output should be a protocol,
not merely “whatever the command currently serializes.”

### 6. A derived retrieval and change-impact model

Build a read-only graph and text index from canonical artifacts before adding
semantic retrieval. The graph should encode declared and deterministically
derivable relations such as:

- collection and type membership;
- outbound and computed inbound links;
- tag membership and curated navigation;
- contract-to-governed-artifact dependencies;
- canonical skill-to-projection and package-to-scaffold dependencies;
- ADR, proposal, implementation, test, and documentation relations where
  explicitly declared; and
- freshness inputs and review cohorts.

Use SQLite FTS5 or an equivalent local lexical ranker as the first retrieval
baseline. A result should include path, title, description, matched passage,
relation to the operation, authority or artifact role, freshness, byte cost,
and ranking explanation. The agent can then open exact passages or whole files.

This model serves two separate needs:

1. **Retrieval:** what evidence is likely to help this operation?
2. **Impact:** if this binding artifact changes, what must be checked,
   regenerated, reviewed, or upgraded?

Optional embeddings should be added only if a representative task suite shows
that lexical, curated, and graph retrieval miss consequential evidence. A
semantic index without a measured recall gap would create another freshness
and compatibility problem before proving value.

### 7. Compact work receipts before broad trace capture

Every named operation should emit a small structured receipt, stored according
to its retention needs. The receipt should record:

- intended outcome and operation ID;
- input identities and important derived state;
- selected action and authority used;
- artifacts or operational records changed;
- checks and results;
- model, tool, context-byte, elapsed-time, and human-decision costs when
  available;
- retries, unexpected failures, operator corrections, and deviations from the
  plan;
- resume, recovery, or rollback information; and
- candidate-learning signals.

This is not a transcript. It is a high-signal execution record. Raw traces may
be useful for a bounded debugging or research run, but default trace retention
creates privacy, volume, selection, and replay problems. Receipts capture the
events most likely to improve later behavior at a fraction of the cost.

This recommendation changes the order in the current
[agent-memory gap plan](../../reference/commonplace-agent-memory-gap-plan.md):
establish receipts and their consumers before broad session-trace capture.
Trace extraction can then be tested against receipts to determine whether the
extra data finds additional useful candidates.

### 8. A governed learning-candidate queue

Replace or absorb the unstructured role of `kb/log.md` with candidate records
that can be queried and closed. A candidate is not accepted knowledge. It is a
claim that some observed evidence may justify changing a future consumer.

Each candidate should name:

- the observed event and receipt or artifact that supports it;
- signal type: correction, failure, retry, repeated sequence, missing context,
  unexpected success, cost outlier, or structural inconsistency;
- affected operation and scope;
- consequence and recurrence evidence;
- proposed consumer and destination, such as a note, skill, validator, cue,
  retrieval feature, or code change;
- confidence and known counterevidence;
- status, owner, and next evidence or review trigger; and
- final disposition and effect-measurement link.

Deterministic extractors should nominate obvious signals first. A semantic
model can consolidate, classify, or challenge candidates, but should not
promote them by itself. Repeated observations should update one candidate
rather than append new prose lines.

### 9. Situation-triggered cues and effect evaluation

After the receipt and candidate paths work, allow a promoted lesson to activate
only in the situation where it is useful. Begin with deterministic cues:
operation kind, collection, artifact type, command diagnostic, path pattern,
explicit user correction, or known state transition. Use semantic activation
only where deterministic signals cannot express the applicability condition.

Every cue should declare its source, applicability condition, priority,
recommended action, expiry or review trigger, and tolerated false-positive
cost. A cue that fires often but does not improve behavior should be relaxed or
retired. This prevents the always-loaded doctrine from becoming the graveyard
of every lesson.

Evaluation must close the loop. Compare representative operations before and
after a promoted change. Measure escaped errors, acceptance quality, human
decisions, retries, context bytes, calls, elapsed time, and later reversals.
The existing proposals for
[ablation baselines](../../reference/proposals/ablation-baselines-for-the-declared-objective.md)
and
[gate learning](../../reference/proposals/gate-learning-from-accepted-edits.md)
should supply part of this layer.

### 10. Guarded automation based on authority and reversibility

Autonomy should be graduated by the kind of transition, not by a global
“autonomous agent” setting.

| Transition | Default authority |
|---|---|
| Read, index, measure, and propose | Automatic |
| Regenerate a disposable derived view | Automatic when inputs and producer are known |
| Run deterministic checks | Automatic |
| Produce a mutation plan | Automatic |
| Apply a bounded, reversible, mechanically verified maintenance change | Policy-controlled; may become automatic after calibration |
| Change authored semantic content or system definitions | Explicit task authority plus required review |
| Promote a learning candidate into binding behavior | Human or calibrated independent-review gate |
| Retire durable evidence or accepted doctrine | Explicit authority and preserved rationale |

This spends operator judgment at semantic and authority boundaries while
letting agents perform cheap inspection and derivation freely.

## Dependency-ordered implementation sequence

The sequence matters more than a calendar estimate.

### Slice 0: establish the benchmark

Record a small golden task set before changing the interface. It should include
cold-start orientation, writing one note, repairing one validation failure,
triaging current warnings, resuming a workshop, upgrading a customized
project, and incorporating one operator correction. Capture correctness,
human decisions, context bytes, model and tool calls, elapsed time, rework, and
escaped errors.

This need not be a large evaluation framework. A small honest baseline prevents
the project from mistaking added machinery for improved operation.

### Slice 1: make the current situation legible

Implement the read-only status projection and add concise and structured modes
to validation and the most-used state commands. Give diagnostics and offered
actions stable IDs. Use existing endpoints as inputs.

Acceptance: a cold-start agent can identify the highest-priority current
failure, lifecycle contradiction, review action, and version mismatch from one
small result and can drill into each without loading unrelated rows.

### Slice 2: make versions and lifecycles trustworthy

Add the project-source manifest, skew diagnostics, upgrade planning, and
deterministic checks for workshop and task contradictions. Define retention
and terminal transitions for review jobs and candidates before adding more
background producers.

Acceptance: the agent can prove which command, doctrine, library, and skill
versions govern an operation, and every durable queue item has a valid next or
terminal transition.

### Slice 3: pilot compiled operations

Define the common operation envelope and compile packets for three high-value
paths: write one note, validate and repair one artifact, and triage current
review warnings. Reuse the proposed per-artifact write brief rather than adding
a separate instruction family.

Acceptance: compared with the baseline, the agent reaches an equally or more
accurate result with less loaded context and fewer discovery calls, and the
packet can be reproduced from its declared inputs.

### Slice 4: add retrieval and impact projections

Build the derived graph, backlinks, FTS baseline, and change-impact queries.
Feed their ranked routes into operation packets. Measure missed relevant
artifacts and irrelevant loads before considering embeddings.

Acceptance: representative operations find required evidence and downstream
checks with an explicit ranking explanation and no authored duplicate index.

### Slice 5: emit receipts and close candidate lifecycle

Have the three pilot operations emit receipts. Extract deterministic candidate
signals from corrections, failures, retries, and cost outliers. Move existing
unresolved log observations into the queue only through a bounded migration
that gives each item an owner and disposition.

Acceptance: a later agent can resume or explain an operation from its receipt;
each candidate is deduplicated, queryable, and closable; normal runs do not
retain raw conversations by default.

### Slice 6: add activation, effect evaluation, and calibrated automation

Promote a small number of candidates into scoped cues or checks. Run the golden
tasks and ablations. Automate only transitions whose failure cost and
reversibility are understood.

Acceptance: retained interventions demonstrate an improvement on the declared
objective, and ineffective guidance has a working relaxation or retirement
path.

## Existing work to reuse rather than duplicate

This audit integrates and reorders existing work; it does not claim that every
component is new.

| Existing artifact | Role in the target |
|---|---|
| [Deterministic write-context assembly](../../reference/proposals/deterministic-write-context-assembly.md) | Starting design for closed operation-specific context compilation. |
| [Per-artifact write briefs](../../reference/proposals/per-artifact-write-briefs.md) | Candidate payload within write-operation packets. |
| [KB graph loader workshop](../../work/kb-graph-loader/README.md) | Derived topology and retrieval substrate. |
| [Backlink surfacing](../../reference/proposals/backlink-surfacing.md) | Cheap inbound relation affordance. |
| [Lifecycle-management workshop](../../work/lifecycle-management/README.md) | State and retirement semantics for durable artifacts. |
| [Agent-memory coverage](../../reference/agent-memory-coverage.md) and [gap plan](../../reference/commonplace-agent-memory-gap-plan.md) | Requirements for candidates, activation, effects, and authority. |
| [Periodic connect-report mining](../../reference/proposals/periodic-connect-report-mining.md) | One candidate source, but only after a real queue and consumer exist. |
| [Error-catching workshop](../../work/error-catching/README.md) | Gate calibration and failure evidence. |
| [Agent-runtime design workshop](../../work/agent-runtime-design/README.md) | Execution, approval, and runtime-boundary constraints. |
| [Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md) | Declared economic objective and evaluation frame. |

The main synthesis introduced here is the combination of a situation
projection, a shared operation envelope, compiled task context, a uniform
action protocol, receipts, and a closed learning lifecycle. It also changes
the priority of several existing ideas: status and version coherence precede
more autonomous behavior; receipts precede broad trace capture; a lexical and
graph baseline precedes vector retrieval; and lifecycle consumers precede more
candidate producers.

## What not to build first

- **Do not replace canonical Markdown with a database-native authoring model.**
  A database is useful for derived indexes and operational transitions. Making
  it the primary semantic authority would sacrifice direct inspection, Git
  provenance, and graceful degradation before showing an operational gain.
- **Do not make semantic or vector search the default answer to navigation.**
  First measure the recall gap left by lexical, curated, and graph retrieval.
- **Do not capture and replay every agent trace by default.** High-signal
  receipts should establish whether raw traces add useful learning.
- **Do not put every lesson into always-loaded doctrine.** Use scoped cues and
  compile applicable clauses into the operation packet.
- **Do not build one universal context-provider framework.** Closed compilers
  with explicit inputs are easier to trust, test, and replace.
- **Do not let a model autonomously rewrite or retire accepted semantic
  content.** Promotion and retirement cross an authority boundary.
- **Do not add another manual register without its validator and consumer.** A
  list that can silently drift increases apparent control while reducing
  actual trust.
- **Do not treat more agents as the primary improvement.** Parallelism can
  reduce latency for separable work, but it multiplies context assembly,
  coordination, and reconciliation when the operation contract is unclear.
- **Do not use a single global confidence or authority score.** Evidence
  quality, applicability, action permission, and reversibility are different
  dimensions.

## Evaluation suite for the finished system

The following scenarios test whether the design is genuinely easier to drive:

| Scenario | Required result |
|---|---|
| Cold start | Identify project purpose, current blockers, active work, and top valid actions without reading broad directory listings. |
| Note write | Produce a contract-valid, connected note with necessary evidence while loading less fixed context than the current path. |
| Validation recovery | Move from one stable diagnostic ID to a verified repair without scanning passing output. |
| Review triage | Separate current actionable evidence from stale history and select the next pair or disposition. |
| Workshop resume | Recover purpose, last verified state, open decisions, and next check from the registry and latest receipt. |
| Customized-project upgrade | Distinguish upstream change, local customization, and conflict; produce and apply an inspectable plan. |
| Operator correction | Capture the correction as evidence, associate it with the affected operation, and avoid premature global promotion. |
| Guidance effect | Show whether a promoted skill clause, cue, or gate improves acceptance or cost and retire it when it does not. |

For each scenario, preserve outcome correctness and warrant, then compare:

- human decisions and minutes;
- total input and output bytes presented to models;
- model and tool calls;
- elapsed time and retries;
- defects caught before handoff and escaped after handoff;
- later reversals or corrective edits; and
- useful candidates promoted, rejected, deduplicated, and retired.

Artifact count, graph density, and queue throughput are diagnostic measures,
not success criteria.

## Final recommendation

Build a small cockpit before adding a larger brain.

The first implementation milestone should produce five things:

1. a read-only, compact, structured project-status and next-action view;
2. concise and stable command diagnostics, beginning with validation;
3. a project-source manifest and version-skew diagnosis;
4. lifecycle validation for workshops and tasks; and
5. a reproducible operation-packet schema piloted on note writing.

Then measure those changes against a small golden task suite. If they do not
reduce reconstruction work while preserving or improving outcomes, fix the
interface before building automated learning. If they do, add receipts, the
candidate lifecycle, task-aware retrieval, scoped activation, and effect
evaluation in that order.

The ideal Commonplace agent should not feel as though it is wandering a good
library with a box of specialized tools. It should feel as though it is
operating a well-instrumented system: the library remains visible and
inspectable, but current state, valid controls, consequences, and feedback are
present at the point of decision. That is what makes the system intuitive.
Loading only what the selected operation needs makes it ergonomic. Turning
verified outcomes into tested, scoped, and retireable improvements makes it
accretive.

## Limits

- This is a repository and local-state audit, not a controlled user study.
  Agent difficulties were inferred from the interface and measured costs, then
  checked against the system's own design claims.
- The local review store is operational state accumulated by this checkout. It
  is not part of a clean clone and may include intentionally retained history.
- Byte volume does not measure comprehension, attention, or provider billing
  exactly. It establishes order of magnitude and comparative load.
- Git activity establishes change pressure, not that the changed artifacts are
  defective.
- The report did not benchmark alternative search engines, context compilers,
  or status rankings. It recommends experiments and acceptance conditions for
  doing so.
- Concurrent uncommitted changes that appeared after evidence gathering were
  excluded, so this report should be treated as a dated snapshot rather than a
  statement about the later worktree.
- Recommendations that become shipped behavior need their own proposal or ADR,
  implementation, and validation. This report is retained evidence and design
  synthesis, not binding system definition.
