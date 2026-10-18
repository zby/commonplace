# Batch 21 AREX route review

## Decision

**Sound as a preparation route for AREX, conditional on unchanged bindings and
later execution clearance.** Resetting only from `memory-profile` preserves
both the report verifier's latest output and its installing application
acceptance. A subsequent operator refusal reaches `report-verification`.
The preserved `apply-report-verification` is **not ready**: its complete pins
are unchanged. Ordinary scheduling therefore cannot replay its old acceptance
before the correction. The historical-handed scheduling exception does not
create readiness.

This resolves the specific blocker in the
[application-reset review](./batch-21-application-route-review.md). It is not
a fresh semantic audit, proof that the eventual repair will succeed, or launch
permission. The mixed batch's other eight routes remain the original
**verifier-reset** routes, not application resets; their conditional findings in
[the mechanism review](./batch-21-correction-mechanism.md) are not independently
recertified here. The parent owns implementation, coordination and release.

Only this report was written. No native reset, judge, advance, inspection,
handout operation or handler was invoked. No target execution, acquisition,
installation, source/method/configuration/state edit, worker prompt/log read,
delegation, integration or commit occurred. In-memory record projections were
used; no disposable synthetic fixtures or test suites were executed.

## Evidence and exact bindings

The AREX row of [batch-21.json](./batch-21.json) supplies these literal paths:

- `W` = `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-arex-skill`.
- `R` = `W/kb/agentic-system-analyses/state/AAS-2026-10-15-arex-skill-1871063034b5-01`.
- Frozen command directory = `W/.venv/bin`.
- Frozen method = `a320038ed1a423b051eedbcec593172f8c2032f4`.

Fresh read-only checks found:

- `R/run.json` SHA-256 is
  `ba7a6a34f11a8ff67c283d67af3ac9a31adb352ad0f810b5fd8c8557d564759f`.
- The complete active attempt filename/hash map equals the bound map of 33
  records. There are no open attempts, operator attempts or pending-reset marker.
- Frozen `artifactrun/{run,engine,handlers,store,plan}.py` and `cli/run.py`
  equal their recorded method commit, checked with `git show`.
- Engine, handlers, store and plan also equal the inspected origin files.
  The complete origin/frozen `run.py` difference is the new pending-reset fence,
  budget-file loading/counting, and its `json` import. Readiness, refusal and
  scheduling logic are identical. The frozen CLI has no reset command.

The decisive full file digests under `W/src/commonplace/` are:

| File | SHA-256 |
| --- | --- |
| `artifactrun/run.py` | `45ec62ef68e55991096ddb4790eef6cb0d32c7e865ac54066a4eb14fb48365b6` |
| `artifactrun/engine.py` | `eec3d74427e9c6e40e294484075907a21a8868f72acd914e9362dc69ea737e73` |
| `artifactrun/handlers.py` | `8b428dd6560cd89aed9243fac1e64591b680871e410704b8cb2e571ecd3e3690` |
| `artifactrun/plan.py` | `b947eccd34eb18b902ee7a3b99a3857e125ea8979a3a8997bdd7a129929f81ae` |

Read-only Python instantiated `Run(RunStore(R))` without locks and called current
`affected_jobs`. A projection removed affected attempts and their judgments,
cleared only in-memory interpretation caches, and appended a hypothetical
operator refusal. It did not allocate sequences, materialize files, invoke
handlers or persist records. A separate projection in AREX's frozen Python and
package independently confirmed readiness and eligibility. Both invocations
set `PYTHONDONTWRITEBYTECODE=1`. Hypothetical refusal IDs were not native records;
their sequence positions were later than all retained judgments.

## Exact reset and preservation result

Current `affected_jobs(run, "memory-profile")` returns exactly ten jobs:

```text
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

Neither `report-verification` nor `apply-report-verification` is in that set.
In the projected active records, the surviving members are exactly boundary,
runtime, memory, epistemic, workflow, reconciliation and report-verification.
The report verifier's member **and** latest primary output both remain:

```text
723c9f818d94009e031cd973ad667524185c7996aba1088312a4816a8d97bb5e
```

Its installing judgment is `000023-apply-report-verification-0`, belonging to
completed attempt `000023-apply-report-verification`. That attempt and all six
of its acceptances survive and still hold. Reset removes profile/public
producers and their installing acceptances, not merely their files. Immutable
predecessor versions must remain evidence in the later native archive.

This closure follows `src/commonplace/artifactrun/reset.py:41–101`: optional
candidate-check context and refusal edges are not reset dependencies. The
actual projection establishes that this exclusion does not accidentally leave
a ready upstream check here. This review did not execute publication withdrawal
or re-certify its external guards. Later authorized reset must still use the
pinned current-origin external reset API and publication hook, preserve the
predecessor/effects, and enforce exclusive operation across the old engine's
missing pending-reset fence, as specified in the mechanism review.

## Initial code fixed point and refusal delivery

The frozen declaration is interpreted by `plan.py:365–378`, which supplies an
optional self-refusal input to every role-filling model job. Thus the absence
of an explicit self-refusal entry in raw `run.json` is not a delivery gap.
`engine.py:177–227` permits a native refusal of this installed model-filled
role. No historical `--version` workaround is needed. Under exclusive parent
coordination the intended member must equal the digest above before and after
judgment. Native transport is `--findings TEXT`, not `--findings-file`.

The [bound feedback](./batch-21-corrections/feedback/arex-skill.md) currently has
SHA-256 `314a5f19333bcaf7d33a0e27f587ffdd9c6a8496cbe1099d6bd5b331539e638f`.
With that prospective refusal, origin and frozen projections agree:

| Observation after projected reset and refusal | Result |
| --- | --- |
| Effective report-verifier refusal | The new hypothetical operator refusal |
| Resolved self-refusal's refused version | Exact surviving verifier digest above |
| Ready model jobs | `report-verification`, `memory-profile` |
| Eligible code jobs | None |
| Report verifier's pending-producer wait | Empty |
| Memory profile's pending-producer wait | `report-verification` |
| Eligible model jobs after budget check | Only `report-verification` |
| Preserved report application's full resolved pin map | Equal to its completed attempt's full pin map |
| Preserved report application ready | False |

The wait for `memory-profile` comes through its required verification judgments:
`_input_producers` includes both ends of their report-verification relations.
Consequently old holding subject acceptances do not let a fresh profile open
while report verification is pending. `engine.py:477–498,551–581` runs eligible
code to a fixed point first, then applies these model-producer waits.

### Optional disappearance and historical-handed exception

The comparison covered every surviving code job, not just the application.
No surviving code job is ready. Only order-only incumbent pins differ for
`check-boundary`, `check-workflow` and `check-reconciliation`; these differences
do not trigger work. Resetting the downstream profile/public roles removes
no non-order-only input from the surviving report application. Its candidate,
verifier attempt, handed subjects, handed answered-refusal and criteria are
all unchanged, including optional absences.

Frozen `run.py:271–298` explicitly handles disappearing optional inputs: model
jobs do not rerun on absence; code jobs can rerun when disappearance invalidates
a judgment from their last completion. That path cannot awaken this application
because none of its pins disappeared. Its six acceptances still hold. A live
operator refusal is not an application input and does not itself invalidate
those bases.

The application's completed-subject exception **is true**, and its computed
model-producer set is empty (`run.py:304–435` in origin; seven lines earlier
in frozen code). This is safe here only because it remains unready. That
exception waives a producer wait; it neither deletes its prior completion nor
forces reapplication. Resetting the application, changing one of its criteria,
or otherwise making it ready would invalidate this proof and can restore the
rejected replay route. Rechecking unchanged bindings is therefore essential,
not optional conservatism.

## Correction closure, self-check and future application

The report verifier declares only the primary `verification` output, not an
auxiliary answers output. Frozen worker rules explicitly allow correction of
a verifier's own accepted output and require roles without answers to repair
in the primary output alone. `engine.py:389–449` rejects completion with the
same refused primary bytes and no new auxiliary version. The route cannot
close unchanged by claiming an answers channel that this job lacks, and the
worker rules forbid artificial changes merely to bypass this check.

A completed substantive correction changes the latest verifier output. The
preserved application then sees a new candidate and a new completed attempt,
including its handed refusal; it becomes ready to check **that** output.
`handlers.py:157–178,205–254` checks the verdict itself before judging handed
subjects. If self-review finds defects, it refuses the candidate and returns
without judging those subjects. If valid, it accepts/installs the new verifier
output and applies its independent blockers or acceptances to the exact handed
subject versions. No unconditional positive judgment is built into the route.
The no-answers branch does not independently machine-check a semantic response
to the audit: substantive disposition still needs worker authorship and audit.

The prospective operator refusal concerns old version V. Acceptance of corrected
version V2 does not supersede a refusal of V (`run.py:172–195`). Instead, after
completion, the old refusal no longer matches the producer's latest output.
Even before installation, loss of that match is **not** semantic clearance;
a failed application or newly refused candidate remains a stop to resolve.

Self-refusal disappearance does not make the verifier rerun: optional absence
is ignored for model readiness. The application pins the *handed* refusal from
the completed attempt, not the live refusal, so the latter's disappearance does
not invalidate its new basis. Once its new snapshot is applied, unchanged pins
make it unready again. The model's self-refusal identity check also prevents
spending another attempt just because restored earlier bytes expose a refusal
already read in a completed attempt. None of these rules guarantees convergence
for arbitrary bad workers or repeated defects; ordinary refusal/budget stops
must remain intact.

Fresh profile and synthesis work then follows normal dependencies. Profile
reads verified subject claims, not the report-verifier narrative directly;
synthesis explicitly reads the installed report-verification member. Resetting
profile itself ensures it is regenerated even if renewed subject claims have
unchanged canonical identity. Native checks, later verifiers and a fresh
exact-byte public audit remain necessary to establish propagation of the
witness disposition rather than merely successful scheduling.

## Semantic scope and attempt headroom

The [retained audit](./audits/post-migration/AAS-2026-10-15-arex-skill-1871063034b5-01.md)
and feedback identify the installed-library-state witness in accepted
`MEM-OBJ-library-state` and `RT-RTE-library-update`, with exact frozen source
locators. This review treats that audit as the supplied discrepancy, not as a
newly proven source-side finding. No AREX target source was acquired or executed.

Frozen `verify-reports.md` permits independent source tracing and consequential
omission investigation. Frozen `follow-worker-rules.md` requires repair of the
assigned role only and routing necessary supporting-record corrections to their
analyst. The proposed independent disposition fits that responsibility under
the explicit audit-assisted commission. The parent must retain that explicit
exception to the ordinary prior-analysis exclusion; workers must not browse
the audit or unrelated historical analyses. The feedback asks for either a
supported narrow capability or a concrete missing link/boundary exclusion,
not a positive classification. PassNet and deletion-coverage limits remain.
A genuine need for aspect-record repair returns through normal blocker routing;
it does not authorize the verifier to edit another role.

Frozen `attempt_count` counts all retained attempts and ignores current reset's
budget floor. Fresh counts after projection are:

- Report verifier: **1/3**, hence two further attempts, not three fresh ones.
- Boundary: **1/2**; runtime, memory, epistemic, workflow and reconciliation:
  **1/3** each. These retained jobs are not initially pending, but independent
  record-repair requests can consume their remaining attempts and trigger peers.
- Memory profile and profile verifier: **0/3** each; synthesis and synthesis
  verifier: **0/2** each, because their old attempts are in the reset closure.

There is initial headroom and no projected scheduling cycle. There is no
promise that all possible repairs fit the remaining budgets. Exhaustion,
failed correction, unsupported record change or a boundary change must return
to the parent; another reset is not permission to evade a stop.

## Prospective regression tests and release limits

These tests would establish transition behavior beyond this read-only proof.
They are recommendations for a **separately authorized disposable synthetic
fixture**, not commands executed here and not permission to mutate held runs.
A missing or negative result withholds execution clearance; it must not be
made positive by patching frozen methods or weakening the semantic request.

1. Reproduce the ten-job reset with current-origin reset/hook imports and the
   old-family engine. Assert that verifier attempt `000022`, application
   `000023`, verifier installation and predecessor archives survive exactly;
   profile/public effects are retired. Preserve changed-publication and
   integrated-result refusal guards and interrupted-reset exclusion.
2. Record an installed-verifier refusal using exact multiline findings bytes.
   Run the real code fixed point in the fixture: assert no old application
   attempt is created, refusal remains effective, only report verification
   opens, and the handout carries the exact payload and previous verification.
3. Cover absent optional auxiliary/answered-refusal inputs, downstream optional
   member disappearance, order-only incumbent drift and stale judgment bases.
   As a negative control, reset the application instead and expose the rejected
   old-acceptance replay. Preserve the historical-handed exception's intended
   behavior without confusing it with readiness.
4. Try unchanged primary output with no auxiliary channel: closure must fail.
   Try a substantively revised but structurally invalid verdict: self-review
   must refuse it and judge no handed subjects. Then use a valid revised verdict
   and assert installation/subject judgments address the fresh completed record.
5. Verify old V feedback is not canceled by any application before its delivery,
   V2 acceptance does not count as same-version supersession, handed feedback
   stays stable after live refusal disappears, and repeated advance does not
   loop or reapply unchanged pins. Include a genuine new refusal and restoration
   of earlier bytes to exercise the already-read self-refusal identity rule.
6. Complete ordinary profile/public regeneration for both a supported narrow
   capability and a supported negative/missing-link disposition; also test a
   verifier blocker routed to an aspect author. Assert dependency waits,
   independent later verification and a current terminal publish completion,
   not merely coverage or an old receipt. Check old-family retained budget
   exhaustion and downstream budgets without crediting the new budget floor.

`tests/commonplace/artifactrun/test_completed_handed_scheduling.py` was read,
not run. Its historical-verdict and own-answered-refusal cases explain the wait
exception but do not test this installed-verifier/downstream-reset route.

Execution still requires parent-owned writer exclusion, complete binding and
publication/effect rechecks, authorized native operations, independent semantic
audit of the exact renewed publication, and separate integration authority.
This report clears only the proposed AREX mechanism at preparation level.

## Validation

This is frontmatter-free workshop text under `kb/work/COLLECTION.md`. Only this
report is eligible for validation in this commission. `commonplace-validate`
passed for this path: one text file, zero failures and zero warnings. This is
not a transition test or semantic clearance. No graph-discovery work was
commissioned; `cp-skill-connect` would require a separately scoped request.
