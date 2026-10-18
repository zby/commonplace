# Batch 21 current release review

**Review result: existing tests support the correction mechanism, not current
launch readiness. The root helper currently refuses the release.** The two
changed production files do not themselves establish a new reset algorithm or
change the frozen drivers. A mixed-package regression and a harness-native
outer dispatch contract are still missing.

## Boundary and evidence

Independent review at origin HEAD
`67482d6cf903522dd6313f51c56eeeba26c3fd1d`, compared with reset baseline
`f12f9a7467f4b01a5777bf8f65f109560b05e848`. This review owns only this file.
It authorizes no implementation, launch, source acquisition, retained-run
transition, integration, seal refresh or ownership clearance.

Read the complete [correction README](./batch-21-corrections/README.md),
[plan](./batch-21-corrections/plan.json),
[preparation evidence](./batch-21-corrections/preparation-checks.json) and
[helper](./bash-21-corrections.sh), the disposable feedback/reset/publication
tests, and the [batch 22 harness route](./batch-22-execution.md) and its JSON
packets as comparison only. Collection and method-maintenance authority were
read. No instantiated job prompts or worker logs were read. Code-reachability
review remains a separate parent/worker responsibility.

A read-only Python hash/HEAD check against the active plan found:

- All nine worktree HEADs equal their recorded `method-revision`.
- Every entry in all nine `native-files` lists matches its recorded hash,
  including native command entry points and the driver.
- All five root `runtime-files` match their recorded hashes.
- Every frozen driver has the same recorded hash
  `491fcdd9a319c1f2c37796025285ab600901fcaa9519de68fc498243b5d9785c`.
  One representative was read completely. No frozen method was edited here.

This verifies these selected bindings, not the whole worktree/source state,
all publication bytes or exclusive ownership. I did not run the real checker.

## What existing tests prove

| Evidence | Established by assertions | Not established |
| --- | --- | --- |
| `artifactrun/test_feedback_reentry.py` (16 cases) | Full/compact toy scheduling; one/two author refusals survive the first fixed point; handouts contain feedback; synthesis-like correction reaches toy publishability; retained-counter exhaustion stops; verifier self-feedback reproduces ambiguous two-version basis | Historical packages, real analysis declarations, external publication, analytical repair or harness dispatch |
| `artifactrun/test_reset.py` (10 cases) | Dependency closure rather than chronological truncation; preserved upstream work; fresh sequence; interrupted reset fence/recovery; CLI reset; modern budget floor | Old commands obeying the pending fence; old retained budgets being renewed; actual publication effects |
| `agentic_analysis/test_reset_publication.py` (8 cases) | Actual reset hook/journal/tree installation on temporary publications; exact predecessor archive; changed-byte republication; altered/integrated publication refusal; interrupted reset does not clobber later writes | Feedback-to-frozen-driver continuation; substantive content validation (publication validation is scripted in this fixture) |
| `agentic_analysis/test_publication.py` (20 cases) | Pinned assembly/provenance and effect failure classifications; uncertain journals; local blocked/out-of-scope handling; narrow real bounded validation adapter | Full substantive analysis validation for complete corrected reports or mixed-package correction |

The feedback file has 12 delivery cases, two verifier counterexamples and two
legacy-budget cases. Its `summary` completion assertion establishes toy
`publishable`, not exact-byte filesystem republication. Separate effect tests
supply that latter evidence. The legacy test monkeypatches the current
`Run.attempt_count`; it does not execute an old package.

Preparation's reported 942-test pass and 14 mocked shell scenarios are historical
preparation evidence, not rerun results from this review. Mocked CLI/agent
scenarios cannot establish native recovery or project-tool compatibility.

## Effect of the current code diff

`git diff f12f9a746..HEAD -- src/commonplace` contains exactly:

- `lib/agentic_analysis/rules.py`: retained profile bytes can be supplied to
  comparison validation only at the retained location with manifest members.
- `lib/systems_matrix.py`: coverage counts warranted local negatives; two exact
  historical profile hashes get a narrow reader exception; new candidates
  remain strict; matrix readers supply retained bytes.

These are profile validation/reader changes, not changes to reset, engine,
store, operator judgment or publication-hook files. The unchanged frozen local
packages, not current origin validation, perform later native refusal and
analytical advancement. Therefore a new current validator branch must not be
presented as automatically executing in an old driver's correction. Conversely,
unchanged reset files alone do not prove the mixed-package route: dynamic
handler loading and later serialized-state consumption still need a bounded
bridge test. The parent should close exact reachability, not infer it from
filenames or passing toy tests.

**The broad root guard is a present blocker, not a test failure.** Before any
helper action it requires no Git diff from `reset-code-commit` anywhere under
`src/commonplace`, `pyproject.toml` or `uv.lock`, and refuses untracked package
code. The two production changes trigger `Reset code/dependencies changed`
even though the five individually pinned runtime files match. This follows
from the guard and the read-only Git diff; no real helper launch was attempted.
Its import check also requires the origin package: calling it from an arbitrary
old worktree is not an available workaround. Do not update hashes or remove the
guard mechanically. A reviewed release must deliberately select and bind its
external reset environment or explicitly justify a narrow guard revision.

## Smallest additional disposable evidence

These are proposed tests, not implemented or run here. Their purpose is to close
the release boundary, not re-test nine systems or launch models.

1. **Mixed-package bridge, two engine families.** In temporary fixtures only,
   use the selected external reset implementation and actual frozen judgment/
   scheduling modules, isolated in separate interpreters. Cover the old retained
   counter family and the newer floor-consuming family. Complete a synthetic
   publication, reset the selected verifier, check closure/archive/upstream
   identity, deliver all exact-version refusals, then advance with the frozen
   package. Assert feedback remains effective and reachable, no stale verdict
   application runs first, no acquire/opening reruns, fresh dependent verification
   occurs, and exact changed publication bytes/journal agree. Include exhaustion
   of a retained author as a stop, without another reset. Reuse immutable local
   method inputs; never install dependencies, contact sources or point a fixture
   at retained run state. Two family representatives are sufficient only after
   reachability review confirms no other relevant package differences.
2. **Three correction shapes within that bridge.** Parameterize one/two upstream
   authors (including a dependency-related boundary/runtime pair), profile author,
   and preserved synthesis author with its accepted upstream verifier applications.
   Assert all refusals are installed before *any* advance. A toy report/other pair
   alone does not cover boundary-dependent refresh; the synthesis case must not
   substitute self-refusing a verifier. If frozen behavior stops legitimately,
   retain the stop as a release limit, not weaken assertions to force success.
3. **Outer harness dispatch contract, entirely mocked.** Exercise the proposed
   parent route with synthetic paths/handles: broad code guard refusal before
   effects; admitted reset before all feedback before coordinator start; partial
   feedback failure prevents dispatch; one-shot ledger collision prevents reuse;
   interrupted wait retains ownership; coordinator/inspect/verification failure
   stops the batch and preserves transcripts/archive references; case two cannot
   start before case one is terminal and verified. Assert project-scoped exposed
   tool invocation, fixed model/effort and fresh context; assert no `pi`/other
   agent subprocess. These are orchestration assertions, not idle proof.

Do not add a redundant retained-profile corpus test to prove reset. Existing
synthetic historical-coverage tests already exercise strict candidate validation,
exact bytes/metadata matching, retained-versus-draft permission and unresolved
local-negative coverage. If origin validation is shown reachable during the
external reset, add a spy/assertion at that real bridge boundary with one strict
candidate and one synthetic pinned reader case; test the demonstrated call path,
not every Cartesian combination of two unrelated validators.

## Test selection and actual outcomes

Executed with existing dependencies, offline and without synchronization; no
models, network, installs, targets or retained-run transitions:

```bash
UV_OFFLINE=1 uv run --no-sync pytest tests/commonplace/artifactrun/test_feedback_reentry.py tests/commonplace/artifactrun/test_reset.py tests/commonplace/agentic_analysis/test_reset_publication.py tests/commonplace/agentic_analysis/test_publication.py -m '' -p no:cacheprovider
```

**54 passed in 17.98s**, exit 0.

```bash
UV_OFFLINE=1 uv run --no-sync pytest tests/commonplace/comparison/test_historical_coverage.py tests/commonplace/agentic_analysis/test_profile.py -k 'not real_allowlist and (historical or pinned or working_or_draft or validation_consumer)' -m '' -p no:cacheprovider
```

**18 passed, 23 deselected in 3.87s**, exit 0. This selects synthetic historical
coverage, pinned prior-limit consumers and the new profile-validation consumer.
The real retained-publication allowlist reader was deliberately excluded.
These 72 passes are selected disposable evidence, not a full subsystem/repository
release gate. `git diff --check` passed. Owned Markdown validation with
`commonplace-validate kb/work/agentic-system-reruns/batch-21-current-release-review.md`
succeeded: one text file, zero failures and zero warnings.

For a later code change to the reset/dispatch boundary, the repository-required
selection is `general/` plus all `artifactrun/` and `agentic_analysis/` tests,
with `-m ''` to include relevant slow coverage. For the present two production
files and changed profile contract, add `comparison/`, `validation/` and `docs/`
consumer suites. A complete pre-push gate remains `uv run pytest -m ''`.
Those wider selections were not run under this review's disposable-only scope.

## Recommended harness-native route, not an execution commission

Preserve the prepared correction policy while replacing only the assistant's
outer CLI dispatch. A later reviewed parent-held release should:

1. Obtain explicit same-run recovery authority, writer exclusion and project-tool
   capability/profile diagnostics **before reset**. An absence of processes,
   matching hashes or terminal attempt records does not release prior writers.
2. Exclusively create the absent one-shot ledger and retain the nine assignments,
   selected reset environment, manifest/payload bindings and ownership decisions.
   Keep the selected external reset and frozen package identities distinct.
3. For each case, serially perform its guarded external reset and exact closure/
   archive/preserved-member checks. Then invoke the frozen `commonplace-run judge`
   for every role/version with exact `--findings TEXT`. Check each refusal and
   check all remain effective/ready before handing ownership to a coordinator.
   No advance is permitted between reset and complete feedback delivery.
4. Start one fresh project-scoped `commonplace-coordinator` through exposed
   `subagent` (`action: start`, `agentScope: project`, existing case worktree as
   `cwd`, `openai/gpt-6.1-sol`, medium). Supply the existing run/prefix and explicit
   deviation: **no prepare/start/acquire; this is authorized same-run feedback
   correction, not fresh source-first analysis**. Have it read the complete local
   frozen driver, use its resume/status discipline, and follow only printed
   native handouts. The parent owns reset/refusal; the coordinator must not
   reinterpret findings or issue additional operator judgments.
5. Retain the handle, wait through the exposed tool, record the terminal result
   before removing the handle, and preserve interrupted-wait ownership. Inspect
   through the case's frozen prefix and verify current completion/publication
   maps before the next case. Stop the entire correction batch on failure; do
   not import batch 22's independent-target continuation assumptions. Preserve
   events, full command errors, transcripts, partial state, budget counts and
   predecessor archives. No automatic retry, reset-budget cycling or cleanup.

The frozen driver can launch its native analytical rounds under the fixed
profile; the outer parent still admits only one correction coordinator at a
time. Old counters remain binding for seven cases; only MehmetGoekce LLM Wiki
and ClawVault consume the reset budget floor. Initial recorded headroom is not
a guarantee that refreshed dependencies can finish.

Batch 22 contributes the exposed-tool/handle/ledger pattern only. Its packets
forbid old findings and old-run reuse and prepare new workspaces; copying them
would contradict batch 21's feedback and same-run commission. Analysts still
receive only native generated handoffs. No workshop/audit packet should become
an extra analytical input. There is no Bash agent-CLI fallback if the exposed
tool, fresh isolation or nested profile support is unavailable.

## Launch readiness blockers, separate from passing review checks

- Current broad origin-code guard refuses the two-file diff. Reset implementation
  selection and any guard change need deliberate review, not a refreshed seal.
- No reviewed batch-21 harness-native dispatch packet/ledger contract yet replaces
  the operator shell launch branch; mixed-package/ordering evidence above remains
  to be supplied under separate implementation/test authority.
- This commission grants review only. Exclusive prior-writer clearance, current
  full binding/publication/source checks and an effectful execution grant are
  outstanding here. This session exposes no subagent launch tool; no diagnostic
  or delegation was attempted, and future execution must stop if unavailable.
- New completion would still mean internal publication only. Fresh fixed intake,
  independent exact-byte audit and separate integration authority remain required.
  Seven unselected held publications, canonical sets and incident/owner holds
  remain protected.

No production/test files, preparation seals, frozen methods or unrelated work
were changed. This review does not claim semantic correction or idle clearance.
