# Windows delivery handoff

## Purpose and authority

The operator requested this consolidated task list after reviewing distribution,
delivery and installation on 2026-10-30. Its purpose is to let an agent on the
Windows machine resume implementation without reconstructing several workshops.
This session gathers the work; it does not perform the implementation or claim
new runtime evidence. The prompt below commissions a later implementation run
when the operator invokes it.

Use this file as the cross-workshop queue. The linked workshops retain detailed
evidence and task-specific requirements. Update this queue as work finishes;
do not create another competing backlog. Close this handoff when every item is
done or explicitly deferred with a trigger, and put durable outcomes in the
code, tests, installation guide, skills and owning ADRs.

## Resume prompt

> Read `kb/work/framework-delivery/windows-delivery-handoff.md` and the root
> `AGENTS.md`. Implement the remaining Windows delivery work in priority order.
> Recheck current code and machine state before changing anything; do not repeat
> completed work merely because an older workshop says it is open. Start with
> shim diagnostics, then the Windows suite and skill portability. Record exact
> coverage and evidence, and update this checklist. Pause for the support-scope
> decisions identified below and for any required full app restart. Do not
> publish a release, weaken security settings, or change unrelated files.

## Starting point: distinguish decisions from evidence

- Distribution remains one user-level uv tool. The library stays in that
  installation; init writes project pointers and skill stubs. No new installer,
  plugin distribution channel, or copied project library is requested.
- Windows requires signed python.org Python 3.14 plus the documented command
  shims. The rejected `uv pip install --target` proposal is not the next step.
  Read [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)
  and [INSTALL.md](../../../INSTALL.md) for the adopted procedure.
- The repository version and latest local tag were **0.3.2 / v0.3.2** at this
  review. Check the actual installed version and package availability; a local
  tag alone does not prove a PyPI publication or a successful installation.
- [Windows guide run 3](../windows-install/results-2026-10-28-afflicted-install-md-run3.md)
  used published **0.3.1**. Reinstall, shims, init, check, landing validation and
  the first Git commit passed. Later documentation fixes landed in `b9852e7ce`.
  The run used fresh children with registry-derived PATH, not a restarted app;
  in-runtime skill discovery and final runtime checks were not run.
- [Windows test-suite progress](../windows-test-suite/README.md) last records
  848 passed, 1 failed, 18 skipped and 2 collection errors. This is historical,
  not the current result. Current CI runs the full suite only on Linux.
- Agentic analysis is deliberately Linux-only. Do not silently expand support
  to make the Windows suite green.

## Execution boundaries

The implementation run may change Commonplace code, tests, CI, canonical skills,
installation documentation and these workshops as needed for the tasks below.
Read each affected contract and test-selection rule before editing. Do not patch
the separately maintained Workjig dependency here. Do not run `commonplace-init`
in this source checkout; use disposable initialized projects.

Before machine changes, inspect installed versions and paths, back up the user
PATH and record antivirus products and Smart App Control state. Explain any
needed install or persistent environment change before doing it. Never disable
Smart App Control or add antivirus exceptions as an automatic repair. Start one
executable at a time; never sweep launchers in parallel. Do not launch through
WMI or `powershell -EncodedCommand`: that pattern previously triggered Avast.
Use a fully restarted shell/app for environment inheritance acceptance; a child
with a synthesized PATH is a narrower test, not a substitute.

Inspect Git status and preserve unrelated changes. Keep commits scoped to the
owning workshop if commits are requested. Parallel writers need disjoint file
ownership; otherwise work serially. This file does not itself launch workers.

## Implementation queue

### 1. Recognize supported command shims

- [x] Reproduce the diagnostic from `installation_warnings()` in
  `src/commonplace/cli/init_project.py`. It currently recommends removing the
  shim PATH entry that INSTALL.md requires.
- [x] Make init and `kb/instructions/cp-skill-health-check/SKILL.md` distinguish
  supported shims from genuine command shadowing. Choose the recognition method
  from current code and layout; do not simply trust every `.cmd` or suppress
  every outside-bin warning.
- [x] Add regression coverage for supported shims and an unrelated shadowing
  executable. Preserve ordinary uv-bin and POSIX behavior.
- [x] Update INSTALL.md's temporary ignore-the-warning advice after the fix.

**Done:** the supported install gets no contradictory repair advice, while an
unrelated shadowing install remains visible. Verify in a disposable project on
Windows and run the required affected/general tests.

Owner and evidence: [windows-install](../windows-install/README.md).

### 2. Rebaseline and finish the Windows suite

- [ ] Run the current full suite on native Windows using the signed interpreter
  and a short, non-virtualized uv cache path. Record the commit, Python version,
  shell, exact invocation, failures, skips and collection errors. Follow the
  [suite workshop](../windows-test-suite/README.md), including the PowerShell 5.1
  empty-argument hazard. Do not assume the old failure count still applies.
- [ ] Reconcile Workjig's currently installed API with Commonplace's run locks.
  `src/commonplace/headless/jobs.py` still imports `fcntl`; raising the dependency
  minimum to Workjig 0.2.0 did not itself remove that import.
- [ ] **Decision gate:** ask whether `commonplace-task` / headless operations
  must work on Windows before implementing a portable run-lock migration or
  excluding those operations. Analysis itself remains Linux-only.
- [ ] **Decision gate:** Windows validation/site generation can import Linux-only
  analysis locking indirectly. Ask whether those read-only consumers must work
  on Windows; do not infer that Linux-only execution forbids portable reading,
  or silently overturn the previous reverted import change.
- [ ] Fix remaining supported behavior and test defects. Skip only genuinely
  unsupported features, with explicit reasons; preserve assertions and isolation.
- [ ] Once the supported suite passes locally, enable pytest on `windows-latest`
  in `.github/workflows/ci.yml`. Keep Linux passing and record actual CI results,
  not just configuration changes. Fix PowerShell argument passing if needed.

**Done:** all supported tests pass on native Windows and CI; exclusions and
command support boundaries are explicit. Existing Windows wheel smoke checks
are not evidence that the full suite passes.

Owner: [windows-test-suite](../windows-test-suite/README.md).

### 3. Make promoted procedures portable

Read the complete [E1 plan](../execution-channel-compatibility/e1-windows-execution.md)
and its linked audit. Derive the current promoted-skill set from the manifest;
do not copy an old skill count.

- [ ] Add package-owned `commonplace-validate all`, using contract-based
  collection discovery, ignore markers, continued execution after failures and
  one aggregate result. Make the validation skill a thin caller.
- [ ] Replace connect's POSIX tag/path pipeline with a package operation or
  shared Python helper. Preserve an empty-match test: zero tag matches must
  never broaden into a repository-wide search.
- [ ] Pair all health-check preflights that must work before package commands
  are available, including layout, skills/pointers and validator checks.
- [ ] Complete the current skill audit's checksum/byte-preservation, web-capture
  temporary-file and runtime-native orchestration dispositions. Retain byte
  identity requirements; do not substitute text-normalizing operations.
- [ ] Explicitly resolve Bash-specific tool declarations and add the E1 narrow
  static check for incompatible shell idioms.
- [ ] Exercise the resulting procedures natively: health preflight, arbitrary
  target validation, `validate all`, connect's empty-tag case, and snapshot
  temporary-file handling. Test stub/library paths for separator leaks.

**Done:** every executable promoted step is shell-neutral, runtime-native or
explicitly paired, with the audit and required Windows evidence recorded.
Checkpoint after the first two package operations: replan remaining skill work
from the current manifest instead of attempting an unbounded rewrite.

Owner: [execution-channel-compatibility](../execution-channel-compatibility/README.md).

### 4. Complete installed-project delivery acceptance

- [ ] Test the current published package separately from the editable checkout,
  recording provenance and effective command/library paths. Avoid switching the
  user's active tool while another analysis is running; use isolated tool
  directories where practical.
- [ ] Fully restart the intended Windows app. From an agent rooted in a scratch
  initialized project, verify bare commands, library reads outside the workspace,
  native skill discovery, and invocation through a stub with arguments.
- [ ] Follow [probe revision 7](./probe-package/PROTOCOL.md) for relevant cases.
  Record whether Claude Code honors the generated Windows read rule. Do not
  reuse agents rooted in the Commonplace checkout as installed-project evidence.
- [ ] Where Codex is available, repeat the no-stub index route with arguments
  after the routing-file fix, using sessions rooted in the scratch project.
- [ ] Where pi is available, test INSTALL.md's user-level extension and worker
  copy in an installed scratch project (probe case 10), not just this checkout's
  project extension. If unavailable, defer to the next installed-project pi run.
- [ ] Cover or explicitly defer upgrade cases: changed skill, library-only
  change, moved installation and an already-running session. Record stale-path
  behavior; a restart requirement is a result, not necessarily a defect.

**Done:** the operator can distinguish package installation, command execution,
library access, skill routing and worker delivery, with outcomes recorded for
only the runtimes actually tested. Ask for an app restart when needed and leave
an exact resume step; do not keep retrying within the old process.

Owner: [framework-delivery](./README.md). The separate execution-channel probe
is [v7](../execution-channel-compatibility/probe-procedure.md); an older v6 run
on an old checkout does not close it. Run it only after installation is stable:
that probe collects evidence without repairing the environment during the run.

### 5. Reconcile records and close completed work

- [ ] Replace stale “v0.2.0 only”, “no Windows evidence” and “no Windows CI”
  summaries with scoped current outcomes. Preserve dated historical reports.
- [ ] Update this checklist and the owning workshops after each completed batch.
  Give deferrals a trigger and blockers an exact next action.
- [ ] Run relevant `commonplace-validate` checks for Markdown changes; follow
  `tests/README.md` for code, shared consumers and relevant slow tests. Packaging
  or entry-point changes also require INSTALL.md's editable-installation checks.
- [ ] Close workshops only when their own closure conditions are met; extract
  durable decisions before deleting temporary material. Do not publish a release
  without a separate operator request.

## Deferred outside a quick Windows implementation run

- **Antivirus field use:** [signed-Python observation](../windows-signed-python-field-use/README.md)
  resumes when a user with Smart App Control or third-party antivirus agrees to
  at least a week of ordinary use. Keep it deferred, not a reason to wait at the
  terminal. Trafilatura's successful launch had an Avast exception already in
  place; do not call it clean-machine acceptance.
- **macOS:** run the install and delivery acceptance when a macOS host is
  available. Windows cannot close that item.
- **Other harnesses / enterprise policy / large skill index:** gather evidence
  when an actual user or environment is available. Do not build speculative
  harness integrations during this pass.

## Progress record

Append one short entry per batch: commit tested, task IDs, changes, exact test
selection/results, runtime/restart state, evidence path, and remaining blocker
or resume step.

- **2026-10-30, item 1 (shim diagnostics).** Tested on `91a4361ee` plus the
  uncommitted fix, Python 3.14 from python.org, installed tool published 0.3.1
  with the INSTALL.md shims on the user `PATH`; no app restart, no install
  change. Reproduced: init flagged all 25 shims as shadowing. Change: init
  accepts a `.cmd` only when it is the snippet's launcher line for that
  command's entry point and runs the existing `python.exe` of
  `<uv tool dir>\llm-commonplace`; the health-check skill applies the same rule
  by reading the resolved file; INSTALL.md no longer says to ignore the warning,
  except for 0.3.2 and earlier. After the fix, `installation_warnings()` with the
  real `PATH` returned no warnings. Under `uv run`, the project venv's
  executables were still reported. The patched init in a scratch project
  exited 0 without warnings, and `--check` was clean. Tests:
  `test_init_project.py -k installation_warnings` 7 passed, covering a
  supported shim, an unrelated `.cmd`, another interpreter, another command's
  shim, a missing interpreter, a venv executable and a uv-bin install. Full fast
  suite (`uv run pytest --continue-on-collection-errors`, Git Bash): 854 passed,
  18 skipped, 1 failed (`commonplace-task --help`), 2 collection errors
  (`headless/test_jobs.py`, `test_tasks.py`); all three are the `fcntl` import
  in item 2. Not run: the editable reinstall of the user tool. Running it would
  switch the user's active 0.3.1 install. Next: item 2.
