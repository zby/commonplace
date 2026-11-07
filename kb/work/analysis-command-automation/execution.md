# Implementation and verification record

## Authority and ownership

The operator commissioned implementation by one Sol worker, a commit, then
parent verification and repairs. At most three fresh implementation attempts
are authorized if substantial redesign requires reverting an implementation
and revising the plan. No live analyses, campaign runs, publication integration
or evidence cleanup are authorized.

Baseline: `a0c12bcd3` (resolve full commit before launch). Shared checkout has
pre-existing edits outside this task: the gist-expansion workshop, its triage
script/tests and scripts README, an ingest, the episode-evidence theory note,
and a shared workshop navigation edit. Preserve them and do not stage them as
implementation work. The parent owns scheduling, acceptance and recovery.

## Attempt 1

- Worker: project `commonplace-worker`, model `openai/gpt-6.1-sol`.
- Scope: implement the complete plan, using the existing analysis workflow;
  deterministic fixtures and real checks; no model-backed analysis execution.
- Owned production surfaces: analysis CLI/library, necessary headless seams,
  affected test suites, canonical analysis skill, command reference and any
  directly necessary execution-contract/installation surfaces. Read destination
  contracts before authoring KB changes. Avoid dependency changes unless needed;
  report a dependency/API gap rather than silently expanding into Workjig.
- Owned workshop surfaces: this directory. Shared `kb/work/README.md` may have
  only this workshop's entry updated, but must not be staged with unrelated
  navigation work. `scripts/README.md` and gist artifacts are not owned.
- Commit explicit owned files only, with the required applicable trailers.
  Include workshop artifacts; leave shared navigation unstaged.
- Acceptance: plan's single-system/batch/fixture/recovery requirements, required
  selected tests including relevant slow cases, lint and KB validation. Record
  exact coverage and limits. No bypassing method pinning or output validation.
- Stop/escalate: unstated consequential policy, conflicting writer ownership,
  unavailable required dependency/API, destructive recovery or effects outside
  scope. Design choices expressly left open by the plan are delegated when
  supported by inspected code and tests; record their resolution.
- Worker session: `01a1b796-304b-7581-9069-3db7fd24f080`;
  runtime model `openai/gpt-6.1-sol`; no nested delegation.
- Implementation and local verification: complete. Parent review remains
  pending. The implementing commit contains this record; its hash is returned
  in the worker completion report.

## Implemented boundary

The [seam/decision map](./decisions.md) records delegated choices. The
[consumer packet](./contract-change.md) records contract maintenance and
projection/installation decisions. ADR 125 adopts command-owned lifecycle and
bounded queues; ADR 118 is explicitly amended rather than silently contradicted.
One run profile supplies all roles. No dependency or production profile expansion
was needed.

`analyse` is a one-target queue; `batch` uses the same lifecycle. Preparation
records the chosen destination before effects. The pinned child owns idempotent
allocation and emits durable execution results. The coordinator invokes only
that worktree's commands, never imports a second workflow or changes global cwd.
Target leases survive into orphan children. Workjig remains the sole worker
reservation/acknowledgement authority. Unknown effects pause claims, not trigger
replacement allocations. Signals stop new claims and drain owned children.

The canonical skill is now an invocation/reporting adapter. Command reference,
CLI help and ADR agree. The analysis skill is not scaffold-promoted; existing
checkout projections are symlinks and generic installed stubs do not change.

## Acceptance evidence by layer

| Required case | Evidence |
| --- | --- |
| Full preparation → pinned subprocess → fake workers | `test_complete_prepared_command_correction_audit_and_fresh_controller`; production source is copied into an independent committed fixture method; real binding, source, member and publication checks |
| Frozen command installation | `test_complete_route_installs_frozen_environment_offline` also calls the production installer, installs the committed lockfile with networking disabled, verifies local command binding and completes through the fake harness |
| Input validation / no intake acquisition | malformed locator, duplicate SSH/HTTPS/case aliases, local/document requirements, invalid revision and unknown-field tests; method/setup is forbidden in these tests |
| Preparation refusal / evidence | installation failure retained, dirty startup and stale default method rejected; no alternate destination/revision |
| Local versus publication | blocked/out-of-scope prepared-command fixtures retain `published: false`, distinct `local-complete`; complete fixture publishes |
| One harness / role responses / corrections | complete prepared command gives runtime and memory corrections from verifier-specific responses, real acceptance active; unexpected role/attempt checks enabled |
| Worker problem, missing output, nonzero, usage and delay | prepared-command scenarios plus existing headless and slow workflow suites; no credentials or remote source transport |
| Advisory failure/skip/uncertainty | outer failed-audit result remains local-complete; worker stops retain skipped audit; existing audit suite covers unsupported harness/timeout/failure; inspection exposes unsettled auditor launches even after advisory failure |
| Same-run resume | explicit selected resume after existing retry retains pi-luna profile/run and unchanged role launch counters; completed-controller restart launches nothing |
| Allocation crash | journal written before directory creation; fresh call recovers exact reservation; legacy allocation cannot steal it; parameter/profile mismatch refused |
| Unsettled worker | killed pinned workflow with a sleeping fake worker remains operator-attention; explicit target selection does not acknowledge or relaunch it |
| Four slots / slot reuse | six barrier-controlled targets at both scheduler and scripted-command layers; release one slot starts the fifth before unrelated long jobs finish |
| Mixed results and isolation | publications, local completion, ordinary stops and unsettled command outcomes remain distinct; opposite release orders preserve receipts, source identities, logs and run/worktree bindings |
| Ownership / interruption | concurrent controller refused; inherited lease survives parent descriptor close; SIGTERM drains four children and leaves two pending; SIGKILL restart refuses live orphan leases, then reconciles exact completed bindings |
| Stale recovery evidence | explicit selection cannot reuse a cached stopped inspection after lease/reconciliation failure |
| No integration / cleanup | complete fixture leaves origin main and status unchanged; prepared worktrees, preparation records, logs and failed-run evidence remain |

The smaller scheduler fixtures are scripted prepared commands, not analysis
quality evidence. The representative command fixtures run the real workflow,
validators and publication acceptance. Most substitute installation cost with a
fixture-local command directory; the offline-install case closes that boundary
using the unmodified production installer. Dependencies are immutable shared
inputs; Git, worktrees, counters, barriers and outputs are independent per test.

## Verification record

- **Final foreground `uv run pytest -m ''`: 1430 passed, 2 skipped in 625.05 s.**
  This is the complete `tests/commonplace/` suite without the default slow-test
  filter: general, analysis, headless, docs, installation and all consumer suites.
  It includes all 37 new automation cases (26 fast, 11 slow), the actual offline
  frozen installation, real checks/publication, correction and recovery fixtures.
  Log: `/tmp/analysis-command-automation-foreground.log`.
- Existing skips: optional `mkdocs_redirects.plugin` is unavailable; Windows-only
  directory-junction case does not apply on Linux. No new skips were added.
- Selected final fast iteration:
  `uv run pytest tests/commonplace/agentic_analysis/test_automation.py tests/commonplace/agentic_analysis/test_worktree.py -q`
  passed 73 tests / 11 deselected. All those slow cases were included in the final
  complete run. Earlier slow command iterations and the independent production
  installer probe also passed. No paid calls.
- Two earlier complete runs launched with shell `&` failed only
  `tooling/test_isolated_codex.py::test_operator_stop_reaps_process_and_retains_evidence[2]`
  because the background pytest process inherited SIGINT ignored. `/proc` confirmed
  the ignored signal disposition. The isolated foreground two-signal rerun passed;
  the final foreground complete run passed. No test assertion, timeout or isolation
  was changed. This was an invocation-environment failure, not a repaired product
  defect. Earlier logs remain in `/tmp/analysis-command-automation-pytest.log` and
  `/tmp/analysis-command-automation-pytest-final.log`.
- `uv run ruff check .` and `git diff --check`: passed after the final suite.
- KB validation: canonical skill, command reference, ADR 118, ADR 125 and workshop
  passed with zero failures/warnings; the completed record is validated again
  before commit.
- Temporary installed-project probe at
  `/tmp/analysis-command-automation-install-probe`: fresh init, repeat init,
  `--check` and collection-landing validation passed. No init ran in this checkout.

## Remaining boundaries and parent handoff

No live analysis, provider call, campaign, publication integration or cleanup
was run. Deterministic workers identify their provenance as fake; fixtures prove
execution and recovery, not analytical quality or provider capacity. POSIX local
file locks are required; network filesystems and live-provider behavior are not
established. Before a pilot, the operator still chooses committed method,
provider concurrency allowance, free storage/inodes and worktree placement.
Four analyses at the default three role workers permit twelve role workers;
audits occupy their analysis's slot afterward.

Uncertain acquisition/publication effects, interrupted auditors and failed
preparations remain explicit operator recovery cases. The command does not
clear them, skip failed targets or allocate replacements. Existing worktrees
keep their original commands and method/profile bindings. No existing evidence
was owned for cleanup.

All initially dirty unrelated paths remain unstaged. Another writer added
`kb/sources/dreaming-with-a-dynamic-workflow-cookbook.ingest.md` during this work;
it is also outside scope and excluded. Shared workshop navigation remains
unstaged. The subsequent [parent acceptance](./parent-review.md) records the
completed independent review, local repairs and full-suite verification. The
workshop is retained for operator handoff and later archival; a live pilot
remains separately authorized.
