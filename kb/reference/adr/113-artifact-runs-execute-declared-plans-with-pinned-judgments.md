---
description: "A generic engine runs the analysis workflow: a plan declares jobs over a typed artifact's roles, one command advances the run from disk, code jobs judge member versions against pinned inputs, and a draft validates in its role"
type: reference/types/adr.md
status: accepted
---

# 113 — Artifact runs execute declared plans with pinned judgments

**Status:** accepted
**Date:** 2026-10-09

**Amended by:** [ADR 117](./117-plans-derive-their-structural-jobs-from-the-type.md). The two open items below, standard handlers and plan compaction, are decided there; the consequence that every check job needs a handler no longer holds; the analysis command's `report` subcommand is `inspect` (ADR 116).

## Context

The analysis workflow's schedule was prose. The coordinating agent read the
skill, chose the next step, launched workers, checked their outputs and
carried values between steps in its own context. The batch 01 trace audit
(2026-09-28) found what that costs: a step that failed under exit status
zero followed by validation of a stale report, workers guessing a contract
filename, and correction turns for a report that had already passed. When
the conversation ended, progress was recoverable only by reading files by
hand. Harness-native code scheduling existed in one harness, inside a
sandbox that cannot run Commonplace commands.

The first code scheduler (2026-09-29) replayed the definition from the
start on every step and reran each accepted job's validator against the
current set. That validator read sibling members that were not declared
inputs. A sibling added later changed the verdict of a job whose inputs
were unchanged, and the engine reopened a job whose repair belonged to a
later correction job. A verification recorded only the role it judged, so
replacing the member left no trace that the judgment was stale.

A draft could be checked in its artifact's context only inside the
workflow, through a private helper and a separate analyst command.
`commonplace-validate` checked a file alone or a whole artifact, never one
candidate in its role.

Each of these recurs if the decision is reverted: an interpreted schedule
drifts, an untracked read makes verdicts volatile, and a judgment without
a pinned subject goes stale silently.

## Decision

This adopts the model of the proposal "Code-scheduled workflows", now
archived, and replaces its first implementation. It adopts stage one of
the proposal "Document validation in working-set context", now archived.
It retires the proposal "Record acceptance reads and judged versions", now
archived, whose problem the judgment model below answers.

**An engine runs artifact runs.** The engine is `commonplace.artifactrun`.
An artifact run executes a plan with parameters and produces one typed
directory artifact. The engine exists for composite artifacts: artifacts
whose members have types of their own and are made by separate jobs that
must agree. A single document never goes through a plan.

**A plan is a declaration file.** It names the artifact type and lists
jobs. A model job names its role, instruction, inputs, outputs,
parameters and max attempts. A code job names its inputs, outputs and a
handler by dotted path into the package. An input has an address: a
library file, a member by role, a job's latest completed output, its
latest completed attempt record, a version that record was handed, a
judgment by role, relation and outcome, a producer's current refusal, or
the artifact's coverage. Roles, relations and required members come from
the type's layout ([ADR 111](./111-directory-types-declare-their-layout.md));
the plan adds only who produces what from what. Starting a run fixes the
plan and the type for that run.

**One command advances.** `commonplace-run advance` closes the attempts
the coordinator reports, runs every ready code job to a fixed point, then
hands out every ready model job as a prompt that pins the version of every
input. Every output version is kept and identity is by content. A job is
ready when its required inputs are present and some input changed since
its last completed attempt; it waits while a producer of its inputs is
pending. No invocation depends on an earlier process. A failure leaves a
record and stops the invocation; an external effect with an unknown
outcome stops it as uncertain.

**Judgments are the one primitive.** A code job records a judgment of a
subject version, accepted or refused, with findings, a basis and a scope.
The basis is the job's pinned inputs. The scope is the declared relations
the judgment covers; the subject's role is at one end of each, and the
version at the other end is in the basis. A judgment holds while its basis
is current. An acceptance of the producing job's latest completed output
installs that version as the role's member. A refusal is an input of the
refused job, and an attempt that read it has answered it. Only code jobs
judge: a model-written verification is a document that a code job reads,
judging the exact versions the verifier was handed. The operator may judge
from the command line and leaves the same record.

**Coverage is engine-derived.** The artifact is publishable when every
role its disposition requires is present, every member has a holding
acceptance, and every relation between members is covered by a holding
acceptance with that relation in scope and the other member in its basis.
A job declares coverage as a required input. Publication copies the
current members out, pinned.

**State lives beside the artifact.** The artifact is the run's `artifact/`
directory. Versions, attempts, judgments, hand-outs and failure records
are its siblings, never members, so the artifact validates as it stands at
every moment and publication is a copy.

**A draft validates in its role.** `commonplace-validate <draft> --artifact
<directory> --role <role>` places the draft's bytes at the role's path,
validates the working artifact and reports the findings attributed to that
role, with absent-member findings dropped. An undeclared role or an
unavailable type fails explicitly; nothing is written. The engine's shared
check and a worker's self-check call this same path.

**The engine's core imports no consumer.** Its core modules know nothing of
validation, Git or files outside the store. Its reuse modules, candidate
checks, frozen sources, journaled effects, worktrees and the run report,
serve any consumer and import none; a test pins both boundaries. A
consumer supplies a plan, a type and the handlers the plan names. The
analysis consumer's lifecycle is `commonplace-analysis prepare`, `start`,
`report` and `integrate`.

The words are plan, artifact run, engine, reuse modules, consumer, attempt
(one execution of a job), judgment and coverage. Code identifiers carry the
same words.

## Considered alternatives

**Keep the schedule in prose.** The status quo. The trace audit's failures
were interpretation failures, and a run's state lived in one conversation.

**Harness-native dynamic workflows.** Available in one harness only, and
its sandbox cannot run commands, so the deterministic steps would still
have needed the parent conversation.

**Recovery kept by the agent.** Four options were weighed: no recovery,
a blocked outcome the coordinator investigates, repair jobs run by fresh
workers, or both. The blocked outcome won and became the engine's stop
with its failure record. Repair jobs were left for when blocked rounds are
seen to fill the coordinator's context; none have been.

**Core inside the analysis package, extracted later.** Cheaper up front
and favoured by the expectation that harnesses will bring their own
schedulers. Lost: a separate module can be tested without a model or the
analysis package, and the boundary enforces that the engine imports no
consumer.

**Repair the first engine by recording acceptance reads.** The retired
proposal's own candidate: log every path the acceptance validator read and
recheck against that recorded context. The engine generalizes the same
response. A code job reads only its declared inputs, every judgment
records those pinned inputs as its basis, and a verifier's handed versions
resolve from its attempt record, so no untracked read exists to log.

**Fixed snapshots with explicit commits.** A whole-set snapshot store and
commit protocol. It answers many writers over shared storage; a run has
one coordinator under a lock with whole-state writes.

**Hashes only, or filtering later roles by stage.** Hashes without bytes
cannot be rechecked exactly; the engine keeps every version instead.
Stage order does not identify corrected versions of earlier roles.

**Rerun the validator against current files on every step.** The first
engine's behaviour and the observed defect.

**Member-role declaration in frontmatter.** A second statement of
membership beside the manifest and layout, changing what `type` means for
every consumer. With a layout the role follows from the path.

**Workflow-only context assembly.** The private helper and a separate
check command. Standalone validation stayed file-only and the next
directory type would repeat the helper.

**Stage two, role-scoped context reading.** Reading only the siblings a
role's relations name. Deferred behind three triggers, costly reads, a
sibling's parse failure blocking unrelated drafts, and attribution
differing from origin, none of which the analysis artifact shows. Not
adopted and dropped with the proposal.

**Coverage recomputed by the publication handler.** It produced hundreds
of judgment inputs, diverged from the engine's own reading of which
acceptances hold, and raised a failure where it should have waited.

**The artifact type as a file input.** A mid-run edit would make handlers
validate against a layout the engine does not schedule by. The type is
fixed with the plan; member types and schemas stay live file inputs.

**Snapshotting file inputs.** A snapshot would have to mirror every file
an instruction links to. File inputs are pinned by digest at hand-out and
checked at completion; runs needing more use a worktree pinned to a commit.

**Names.** `setrun` and `runset` for the run were rejected, the first for
carrying "set", the second for reading as a set of runs; "set" for the
produced directory gave way to artifact; the reuse modules got no package
or name of their own.

**Left open.** Whether a member can itself be composite is out of scope
(2026-10-09). Standard handlers that let a plan run without consumer code
are the live proposal "Plans without consumer code". Compacting the plan
file is deferred. The first engine's coded stop kinds remain a live
proposal.

## Consequences

A run resumes from disk in any session. Every judgment names the exact
versions it rested on, and replacing a member shows which acceptances went
stale and which relations are uncovered. A worker, the acceptance check
and the operator validate a draft through one command. A second consumer
needs a plan, a type and handlers, nothing in the engine.

The engine is proven on scenario tests, a toy plan and one production
analysis: the Dynamic Cheatsheet run of 2026-10-09, compared same-model in
the log with the previous workflow's run. The operator chose a coherence
review over an end-to-end proof before that run (2026-10-08), and one run
does not establish production fitness.
Every check job still needs a handler, mostly a wrapper naming its role
and partners. Runs started under the first engine do not resume; their
retained data is kept. Raising a job's max attempts is a plan change, so
a run exhausted under the fixed plan ends or is overridden, never raised.

The decision reaches behaviour through four consumers. The analysis skill
and its run driver bind the coordinator to `commonplace-analysis` and
`commonplace-run`. The engine's loader consumes the plan file. The
validator consumes `--artifact` and `--role`. The layout of ADR 111
supplies roles and relations to both the engine and the validator.

The decision is tested with one consumer, one coordinator per run and
members that are single documents. It has not been exercised with
concurrent coordinators on one run, with composite members, or with a
plan whose code jobs are declared out of dependency order, which the
engine tolerates at the cost of a wasted run.
