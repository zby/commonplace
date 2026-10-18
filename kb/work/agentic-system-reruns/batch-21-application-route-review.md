# Batch 21 application-route review

## Decision

**Do not release the proposed nine-case application-reset route.** The 11/7-job
closures are correct, and the targeted primary outputs survive. However,
ordinary scheduling does **not** prioritize these refused producers over the
reset application job. The application can reissue its old acceptance of the
exact refused version before any model handout opens. That later acceptance
supersedes the new operator refusal. This affects all nine cases, although the
boundary refusal survives in the three boundary/runtime cases.

AREX has an additional distinction: resetting `apply-report-verification`
retains the verifier's completed output but removes its installing acceptance.
Its verifier **member does not survive**. Explicit `--version` can still address
the surviving latest output and make its producer ready; this is not the
vanished-synthesis problem in the [earlier review](./batch-21-correction-mechanism.md).
But the old application is allowed to run first and accept that verifier
output again, canceling the feedback before the verifier reads it.

This is an independent preparation review, not execution authority or a
replacement parent plan. Only this report was authored. No real reset, judge,
advance, handout opening, handler execution, worker launch, target execution,
source acquisition, installation, integration, commit or state/configuration
edit was performed. No worker prompts or logs were read. Method instruction
files and attempt/judgment metadata were inspected. Audit findings are inputs,
not newly established source-side semantic judgments.

## Evidence boundary and checks

Case identities, literal worktrees, command directories and method revisions
come from [batch-21.json](./batch-21.json); the correction purpose comes from
[batch-21.md](./batch-21.md) and this review's supplied alternative. Origin HEAD
was `f12f9a7467f4b01a5777bf8f65f109560b05e848`.

For each of the nine, freshly checked:

- `run.json` SHA-256 and active attempt filename/hash map equal the batch pins;
- frozen engine, run, CLI, store and standard handler files equal their own
  recorded method revision, using `git show`;
- all target roles equal their filler job's latest primary output **before**
  reset projection; there are no open attempts or operator attempt records;
- current `affected_jobs` returns the claimed closure;
- removing affected attempts and judgments in memory preserves each target
  output, but not necessarily its installed membership;
- the application job resolves exactly the same complete input pins as its
  prior completed application, even after the hypothetical new refusals.

The engine, store and handler bytes are identical across all nine. The old
`run.py` differs from origin only in pending-reset fencing and budget-floor
support, not scheduling or refusal supersession. Old-family CLI files have no
reset command. Mehmet and ClawVault have the newer reset-aware family.

Read-only evaluation used `Run(RunStore(R))`, without a store lock, and
`affected_jobs`. An in-memory projection removed affected record objects,
added hypothetical operator-refusal objects, and inspected readiness,
producers, resolved pins and refusal selection. No projection was persisted.
Frozen Python environments independently confirmed the first eligible code job
for the first eight cases; their first job was the reset application, despite
pending target corrections. AREX's initial native projection stopped on the
assertion that its member survived. Subsequent origin interpretation established
that its latest output survives while its member does not. The relevant frozen
scheduling methods have the same bytes/behavior as origin.

A separate in-memory projection reissued the prior application's judgment
objects at later sequence positions. All targeted runtime, workflow, profile
and AREX verifier refusals then ceased to be in force. Only boundary refusals
remained. This is a record-semantics probe, **not** execution of the application
handler or proof that a later real handler must succeed. One preliminary probe
used attempt-scale rather than judgment-scale sequence numbers and failed;
its result was discarded. The successful probes used positions later than
all existing judgments (`CodeAttempt.judgments` scales attempt sequence by
1,000).

Not freshly certified: writer idleness/ownership, preparation and source
cleanliness, complete startup-file binding, external publication maps, all
publication-hook guards, integrations, or semantic adequacy of any repair.
The observed blocker precedes those execution-clearance questions.

## Closures and case results

The seven report-application cases have exactly this forward closure:

```text
apply-report-verification
memory-profile
check-memory-profile
profile-verification
apply-profile-verification
synthesis
check-synthesis
synthesis-verification
apply-synthesis-verification
assemble
publish
```

JAZ and Mehmet have exactly:

```text
apply-profile-verification
synthesis
check-synthesis
synthesis-verification
apply-synthesis-verification
assemble
publish
```

These closures retain the report/profile verifier's model attempt and immutable
output, not the acceptance by its application job. The source author members
survive. Verifier membership is removed with the application acceptance; merely
retaining the producer attempt does not install its primary output.

| Case | Frozen method | Refused roles | Prior application | Result if old claims are reapplied |
| --- | --- | --- | --- | --- |
| Supermemory | `a568c6dc489ad546374536b642c3889ce23149a8` | runtime | `000056` report | runtime feedback superseded |
| ContextPilot | `4266dabc470929df0ff753e57fee0c55d7b87fc6` | boundary, runtime | `000084` report | runtime feedback superseded; boundary remains |
| OpenRSI | `f7732e9c6bc5622031571d2d429bc017253eb64f` | runtime | `000056` report | runtime feedback superseded |
| ModularRSI | `8414ddbd35da24645c020789bd824cb9749fa677` | runtime, workflow | `000077` report | both feedback payloads superseded |
| JAZ | `a568c6dc489ad546374536b642c3889ce23149a8` | memory-profile | `000074` profile | profile feedback superseded |
| Autogenesis | `a320038ed1a423b051eedbcec593172f8c2032f4` | boundary, runtime | `000054` report | runtime feedback superseded; boundary remains |
| MehmetGoekce LLM Wiki | `fb6ad58fd2fdc0e595e1e6671079b98e2e29730f` | memory-profile | `000031` profile | profile feedback superseded |
| ClawVault | `fb6ad58fd2fdc0e595e1e6671079b98e2e29730f` | boundary, runtime | `000023` report | runtime feedback superseded; boundary remains |
| AREX-Skill | `a320038ed1a423b051eedbcec593172f8c2032f4` | report-verification | `000023` report | verifier feedback superseded |

Each prior application has an accepted judgment of the named non-boundary
subject at exactly its current latest primary-output version. The case's full
version digests remain in the batch publication map. AREX's target is
`723c9f818d94009e031cd973ad667524185c7996aba1088312a4816a8d97bb5e`.
The earlier synthesis digest is not the target of this alternative.

## Why ordinary scheduling defeats the feedback

The decisive implementation is:

- `src/commonplace/artifactrun/engine.py:128–149,477–498,551–581`:
  advance runs code to a fixed point **before** opening model attempts. Code
  jobs wait only on their computed pending model producers.
- `src/commonplace/artifactrun/run.py:304–435`:
  `producers`, `_input_producers` and `_consumes_completed_subjects` exempt a
  code consumer of a completed verifier attempt and its handed member inputs
  from waiting on that verifier's new pending work.
- `src/commonplace/artifactrun/handlers.py:157–178,205–254`:
  application validates the completed verdict and its handed correction
  context, then judges the verdict and handed subjects. It does not consume
  the newly issued live operator refusal.
- `src/commonplace/artifactrun/run.py:172–195`:
  `superseded` accepts any later same-role/same-version acceptance covering
  the refusal's scope. An empty refusal scope is covered by any acceptance
  scope. No explicit override or fresh model attempt is required.

In these actual declarations, application inputs are the verifier's output,
completed attempt, handed subjects, handed answered-refusal and criteria.
Handed subject producer identity points to the verifier's completed work for
scheduling purposes, not to a pending runtime/profile correction. Application
has no live role, judgment or refusal input that restores the necessary wait.
Its computed model-producer set is empty after the completed-subject exemption.
Resetting it makes it ready because it has no surviving completion.

Thus the ordering is not “refused author, check, refreshed verifier, apply.”
The first eligible code job is the old verdict application. Its input pins
match the old application exactly. With unchanged external evidence and
successful validation it can issue the same accepted claims at a newer
sequence. The claims cancel the new refusals before `_open_model_attempts`
selects workers. A real handler failure instead stops the run; it is not a
supported feedback-delivery mechanism.

Old candidate-check acceptances retained in state do not themselves supersede
newer refusals: they have older sequence positions. Ordinary candidate checks
that read a producer's own answered refusal retain their pending-producer wait.
The specific hazard here is a **new application of an old completed verdict**,
not old records changing sequence spontaneously. Holding-basis checks and
coverage do not protect refusal selection: `superseded` does not call `holds`.

The intended exception is covered by
`tests/commonplace/artifactrun/test_completed_handed_scheduling.py`, especially
`test_late_completed_verdict_applies_before_ready_or_exhausted_rerun` and
`test_only_a_completed_record_consumer_skips_the_verifier_wait`. Those tests
were read, not run. Their safe historical-version example differs from this
proposal: here the old accepted subject is **still** the producer's latest
output, so the later acceptance can cancel the new refusal.

## AREX: valid correction responsibility, unsupported delivery sequence

The [AREX payload](./batch-21-corrections/feedback/arex-skill.md) asks the
report-verifier author to dispose of the installed-state witness, not to
produce a positive classification. The frozen `verify-reports.md` permits
independent source tracing and consequential omission investigation. Frozen
`follow-worker-rules.md` allows correction of a verifier's own accepted output
and requires necessary record repairs to be routed to the declaring analyst.
The [audit](./audits/post-migration/AAS-2026-10-15-arex-skill-1871063034b5-01.md)
requires a supported public disposition, not a prescribed verdict. Assigning
that verification responsibility is reasonable under this explicit audit-assisted
commission; the payload is not authority to edit aspect records or publication.

The native judge accepts an explicit existing version even when no role member
is currently installed (`engine.py:177–227`). `refusal_in_force` matches the
producer's latest primary output, not installed membership. Therefore pinned
AREX verifier feedback can initially become effective after application reset;
this is stronger than the failed earlier synthesis route, whose producer
attempt was removed. Nevertheless, application immediately has permission to
reinstall and accept the same verifier output. It need not read the new refusal.
AREX has no auxiliary answers output, so an eventual correction of this role
would need substantive primary-output change; unchanged refused bytes cannot
close successfully through an invented answers channel.

Normal profile and synthesis dependencies can propagate a renewed verifier
assessment **if it is actually renewed and applied**. This review establishes
neither that renewal under the proposed sequence nor semantic propagation into
a correct public conclusion. Fresh exact-byte audit remains necessary.

## Guards any later supported route still needs

These are acceptance conditions for parent replanning, not a substitute
launch sequence. None removes the scheduling blocker above.

- Pin every role/version/payload separately, including both ModularRSI roles.
  Require member/latest-output equality before reset and verify the exact
  surviving primary output afterward. Distinguish a retained output from an
  installed member; explicitly pinned versions do not create members.
- Deliver all multi-role refusals before any advance. Boundary then runtime,
  or runtime then workflow, does not itself enforce worker order. Native
  dependency scheduling must still control correction order and peer refresh.
  Do not attach cross-role bases as an automatic feedback-expiration device.
- Use native `--findings TEXT`, not `--findings-file`. Transport pinned UTF-8
  text as one argument, without shell evaluation. Preserve findings bytes and
  judgment identities. Explicit `--version` is not a compare-and-swap guard:
  recheck state under exclusive coordination and confirm effective refusal
  input resolution before any worker scheduling. Do not add scope/override
  tricks to evade the later-acceptance problem.
- Recheck initial and dependency-induced attempt headroom against the frozen
  engine. Old methods ignore the reset budget floor. Retained counts/limits:
  Supermemory runtime 1/3; ContextPilot boundary 1/2 and runtime 2/3; OpenRSI
  runtime 1/3; ModularRSI runtime 2/3 and workflow 1/3; JAZ profile 2/3;
  Autogenesis boundary 1/2 and runtime 1/3; AREX verifier 1/3. Mehmet and
  ClawVault consume current reset's new budget floor. Boundary changes can
  trigger all specialist authors; dependency reruns and failed corrections
  can exhaust retained old-method budgets. No fresh-budget guarantee follows
  for untouched jobs, and another reset is not permission to evade exhaustion.
- Old frozen CLIs cannot reset. Any separately authorized reset needs the
  pinned current-origin external API and publication-hook import binding,
  not origin CLI dispatch against a foreign run or mixed frozen/current
  modules. Old engines also lack pending-reset fencing; external exclusion
  must prevent their operations during reset/recovery.
- Preserve predecessor attempts, judgments, versions and publication effects;
  verify exact reset closure, completed reset and publication withdrawal before
  further work. Reject open writers, changed bindings, uncertain effects or
  an integrated publication. Source/method edits, manual acceptance patches,
  forced positives and uncommissioned role substitutions remain excluded.
- A later candidate route needs a separately authorized disposable regression
  proving feedback survives the first code fixed point and reaches **every**
  target, including AREX's non-member/latest-output state. It must also prove
  budgets, multi-role order, publication protection and terminal currency.
  No mutation fixture or pytest suite was executed in this review.

Preserving a verifier output while resetting its application is a supported
structural operation. Treating that preserved verdict as fresh, independent
verification or assuming it waits for new feedback is not supported. No one
of the nine is cleared under the supplied ordinary-advance sequence. The
parent retains route selection, implementation, coordination and release.

## Validation

This is frontmatter-free workshop text under `kb/work/COLLECTION.md`.
Validation is limited to this report, not the held runs or their publications.
No broader graph discovery was commissioned; `cp-skill-connect`, if desired,
requires a separately scoped request.
