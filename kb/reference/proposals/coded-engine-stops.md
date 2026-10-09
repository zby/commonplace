---
description: "Proposal: give workflow-engine stops a kind from a small closed set, and give uncertain stops the evidence to inspect before retrying, so a coordinator can branch on stops without parsing prose"
type: reference/types/design-proposal.md
---

# Coded engine stops

The workflow engine reports why an invocation ended only in prose. This
proposal gives each stop a kind from a small closed set, and gives an
uncertain stop the evidence to inspect before anyone retries. It is
deliberately minimal: engine stops only, not handler or validator errors.

## Current state (as of 2026-10-08)

A `Stop` carries a prose reason, the job, the attempt and an `uncertain`
flag (`src/commonplace/artifactrun/engine.py`). The engine creates stops in a
few places:

- a model attempt closed as failed: the coordinator reported a failure, the
  worker wrote a problem, the primary output is missing, a file input
  changed while the attempt was open, or a refusal was answered with nothing
  new;
- a code job could not run because the set directory no longer holds a
  pinned member;
- a code job's handler raised, with `uncertain` set when it raised
  `UncertainEffectError`;
- a model job exhausted its max attempts;
- scheduling stalled on a wait cycle.

These are told apart only by wording, with one exception: the `uncertain`
flag is already a coded stop kind of one bit. The analysis skill escalates
every stop to the operator alike: it preserves the evidence and stops
(`kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md`).
Tests pin stops by matching reason text. An uncertain stop says that an
external effect's outcome is unknown, but not where its evidence is; for
analysis publication that is the effect journal and the run report, and
finding the journal today means reading `publication.py`. The failure
record already keeps the handler's trace.

gbrain ([retained analysis](../../agentic-systems/reports/retained-archive/AAS-2026-09-23-gbrain-01/result.md),
commit `61d577470`) gives every error a
registered code, a class that fixes retryability and exit code, and a fix
expressed as data. It never answers an unknown mutation outcome with
"retry"; it points at a receipt or a status read instead. Most of that
machinery serves remote callers, consent and spend, which Commonplace does
not have.

## Options

1. **Keep prose stops.** No change. A consumer that wants to handle a stop
   kind reads the wording, and every wording change can silently break it.
2. **A stop kind from a closed set.** Each engine stop names one kind
   alongside its reason, widening the existing `uncertain` bit to an
   enumeration. The prose reason stays for people. The set is engine-owned
   and small; a new kind is an engine change. Two axes compete for the
   kind. One is origin: failed by the coordinator or worker, stale inputs,
   handler error, uncertain effect, exhausted attempts, stalled scheduling.
   The other is disposition: what the coordinator may do next, retry,
   inspect first, or hand to the operator. The decision a coordinator makes
   repeatedly is the second, and the origin is already in the failure
   record, so if this option is adopted the kind codes the disposition.
3. **Evidence on uncertain stops.** An uncertain stop also names what to
   inspect before retrying, supplied by the consumer that owns the effect,
   since `api-design.md` leaves effect recognition to consumers. The engine
   carries it through; it never suggests a retry for an uncertain stop.
   Mechanically this is one field: the uncertain-effect error carries an
   evidence pointer, and the engine copies it onto the failure record and
   the stop beside the trace it already keeps.

Options 2 and 3 are independent. A larger registry, fixes expressed as
commands, consent and actor fields, a richer exit-code set, a per-item
failure ledger and a source scanner enforcing codes are left out: each
answers a scale or a caller Commonplace does not have.

## Forces

- The coordinator is an agent; prose is readable to it, but a decision it
  is expected to make repeatedly should not depend on wording.
- Most stops need the operator anyway. A kind only pays off where a
  consumer would act differently by kind.
- Engine stop kinds are few and stable; handler failures are many and
  domain-specific, and already end as a failed attempt with a recorded
  reason. Coding them would be a large migration with no consumer.
- Uncertainty is the costliest stop to mishandle: a blind retry can repeat
  a publication. The evidence pointer addresses that case directly.
- No stop kind is known that the coordinator should handle alone. The
  obvious candidate, advancing again after a file input changed under an
  open attempt, is wrong: under the fixed declaration a file changing
  mid-run is a method change, and the run is unpublishable against it, so
  that stop belongs to the operator. Until a kind with a coordinator-only
  disposition is found, option 2 serves only the tests.
- A handler that raises to say "not yet" looks like a handler error. The
  analysis assembly job does this today for an uncovered relation
  ([consumer surface](../../work/workflow-requirements/consumer-surface.md)).
  A coded handler-error kind would carry that misuse forward without
  telling it from a bug; the remedy is readiness, not a stop code. This is
  the strongest reason to keep handler errors out of the set.

## Candidate selection

Option 3 now, at the minimal scale above, when the publication effect is
next touched. Option 2 stays on the frontier until its adoption criterion
arrives; its operativity section shows it has no consumer today.

## Operativity

- **Option 2.** No consumer distinguishes stop kinds today; the skill
  escalates all of them. Consumers would be the tests, which could assert
  kinds instead of wording, and the coordinator through the skill, if a
  stop kind with a coordinator-only disposition is found (see Forces).
  Without such a rule the kind is recorded but not acted on.
- **Option 3.** The consumer is the operator or coordinator handling an
  uncertain stop, through the run status and the analysis run report. The
  analysis publication and acquisition effects would supply their
  evidence.

## Adoption criteria

- Option 2: a skill or command rule that handles some stop kind without the
  operator, or a test cleanup that would otherwise keep matching stop
  wording.
- Option 3: the next uncertain stop an operator has to diagnose by reading
  code to find the journal, or any second consumer-owned external effect.
  The first condition very likely holds already, since the journal's
  location is in code and the run report marks journal states unverified.
