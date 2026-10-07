# Workflow API design sketch

Version-1 proposal for review, not an adopted amendment to
[the requirements](./requirements.md). The
[Python sketch](./api_sketch.py) contains only public declarations, result
records and necessary operations. Behavior is `...`; this is not a working
engine or a complete analysis job set.

## Public boundary

- `JobSet`, `ModelJob`, `CodeJob` and `Read` declare the work.
- `advance(directory, jobs, completions=...)` is the coordinator's only call.
- `CodeContext.read()` supplies pinned declared inputs.
- `accept_candidate()` and `refuse_candidate()` record structural checks.
- `apply_verdict()` translates a consumer-parsed model verdict into judgments
  of the exact member versions the verifier read.
- `Completion`, `Handout`, `Stop` and `Advance` carry coordinator data.

There is no public engine object, storage API, pin constructor, generic
judgment constructor, restoration method or operator override command.
Code handlers return named output bytes; context judgment calls are staged
and committed with those bytes only when the handler succeeds.

The type spec supplies member slots, relations and disposition requirements.
Jobs declare all possible relation partners in advance. Readiness waits for
required inputs and excludes producers/checks for members the disposition
does not require. Assembly and publication use the type's active obligations.
The type-loading adapter is internal, not a configurable public protocol.

## Correctness kept behind the boundary

Every attempt pins its declared reads, including absence, before work starts.
Model prompts point to those immutable copies. Completion uses opening pins,
not live files. `previous=True` adds pinned prior outputs to the prompt
without making them rerun triggers.

Ordinary reads compare content identities. A `verdict` read also compares
the producing input identities: identical verdict text about different
members must cause the apply job to run again. Repeating identical text
against identical inputs changes nothing. This is a proposed exception to
requirement 4's blanket content-only currency rule.

`apply_verdict()` gets subject versions and basis from the verifier's retained
attempt. Its caller supplies parsed findings and relation scopes, never hashes
or pins. The engine validates those scopes against the producer's declared
member inputs. A verdict about A cannot authorize B. A late acceptance cannot
restore A over B; historical restoration is not available in version 1.
This narrows requirement 6's unconditional installation rule.

The apply handler must first validate the verdict document. Structural
acceptance of that document and semantic application of its findings are
separate calls, committed atomically. A stale verifier document can remain
historical, but cannot supply holding coverage for replacements.

## Restricted correction ownership

Version 1 supports one designated semantic apply job per member, declared in
`verifier_owners`. It emits the complete findings for that member on each
verdict, not incremental findings from arbitrary judges. Structural rejection
of a candidate is recorded separately and does not erase semantic findings.
A later current, blocker-free verdict withdraws that owner's earlier blockers;
a stale verdict cannot withdraw findings about a newer version.

The engine supplies the producer's correction findings as a declared read.
A successful changed candidate answers the structural rejection it read;
semantic findings remain pending until the designated verifier evaluates the
replacement. Answered findings alone do not repeatedly schedule the producer.
New actionable findings do. An unchanged primary output answering its own
refusal fails, even if an auxiliary answers document changed.

This is a deliberate restriction of requirements 5 and 7, not a general
solution for overlapping judges. The complete analysis declaration must prove
that each member has only one semantic owner. If it needs multiple owners,
return to this decision rather than silently retaining only the latest refusal.

## Recovery and publication

State has one fixed location: `workflow-state/` beside `output/` in the run
directory. Attempt staging is not authoritative. Immutable output storage
and one final attempt record precede materializing derived member slots.

Reserve the attempt budget at opening. Finish, failure and explicit
abandonment consume that reservation; resuming the same attempt does not
consume another. A live worker is never inferred dead. The coordinator must
stop/join it before reporting abandonment. Failure stops the invocation;
a later invocation can retry within the bound. This changes scenario 12's
uncounted killed-worker behavior.

Publication remains consumer code, gated by holding acceptance reads whose
scopes cover the active type obligations. It copies pinned inputs and retains
the provenance needed to identify what each verification judged without the
run directory. Environment and incumbent checks remain consumer-owned.

External-effect recognition is necessary for acquire and publish, but is not
part of this public sketch. Reuse consumer-specific recognition routines
internally: established complete effects commit, established absent effects
may retry, uncertain effects stop. The implementation design must connect
those routines to recovery before these jobs run; this sketch does not claim
that returning bytes alone models external effects.

## Deferred

- Operator judgments, explicit overrides and historical restoration.
- Arbitrary semantic judges and overlapping refusal aggregation.
- Public versions, pins, produced-output records and currency fingerprints.
- Configurable storage, declaration discovery and effect-adapter protocols.
- Engine-provided untracked context injection. Workers may still follow their
  instructions for untracked context; consequential consistency needs checks.
- Generated check pairs, decorators, historical-read APIs and change diffs.

These features are not needed to review or implement the first consumer's
scheduling boundary. Do not add them until a demonstrated consumer need
requires them.

## Before implementation

Complete the analysis declaration and check these transitions:

1. A verdict about A finishes after B is installed: no authorization of B or
   restoration of A. Identical verdict bytes about B still reach the apply job.
2. One of two workers finishes; the other stays open across advance calls and
   can later be explicitly abandoned within a bounded budget.
3. Structural rejection and the designated semantic owner's findings both
   reach a correction; neither erases the other or causes an endless rerun.
4. Changed-input reruns receive prior outputs without self-triggering.
5. A non-complete boundary suppresses record work but permits assembly.
6. Every active relation has a check supplying holding coverage; stale or
   missing coverage blocks publication.
7. Interrupted staging and slot materialization recover without treating
   uncommitted bytes as accepted members.

These are review and future test obligations, not passing test results.
