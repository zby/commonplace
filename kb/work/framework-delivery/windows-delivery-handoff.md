# Windows delivery handoff

## Next run

The operator requested the cross-workshop handoff on 2026-10-30 and, after
0.3.3 shipped, requested one more Windows run on 2026-11-01. The immediate goal
is to close [windows-install](../windows-install/README.md) with a PyPI install.
The [framework acceptance table](./README.md#remaining-acceptance) owns status.
Do not restart completed shim implementation, suite repair or the E1 rewrite.

> Follow INSTALL.md steps 1–4 using `llm-commonplace==0.3.3` from PyPI over
> signed python.org Python, then rerun the shim snippet. Record the installed
> version, origin, Workjig version and effective command/library paths. Verify
> command startup one at a time, scratch-project init, `--check` and landing
> validation in fresh processes inside and outside the fully restarted desktop
> app. A Git-main install or checkout test run does not substitute for PyPI.
> Preserve active control-plane files; record template recreation as the known
> accepted limit. Write a new dated report under windows-install and update
> the acceptance table. Stop with an exact resume step if a restart, permission
> or environment prerequisite is missing.

Avoid changing the active user tool while another analysis is running. Use
isolated tool directories where practical, but identify which layout and PATH
were tested. An isolated install does not establish acceptance of the user's
active command route unless that route is also checked.

## Additional checks when prerequisites are available

1. **Claude read rule.** Start a default-permission session rooted in the new
   project (or use an authenticated CLI). Inspect the effective mode and read
   rule. Compare a read inside the installed library with one outside its rule.
   The [previous report](./results-2026-10-31-windows-installed-project-agents.md)
   allowed both, so it could not attribute access to the rule. Record prompts,
   denials and permission mode; do not count bypass mode as rule acceptance.
2. **Agent delivery.** In a fresh agent rooted in that project, check the bare
   command, library reads, native skill listing and a stub with an argument.
   Report each separately. Codex's index-with-arguments route already passed
   on Git main; repeat only where needed for the new installation's acceptance.
3. **Workjig recovery.** If a bounded fixture or released dependency tests are
   available, verify that installed Workjig 0.3.0 preserves and rejects an
   existing interrupted lock marker and accepts a fresh lock. Do not patch
   Workjig, use a source overlay or infer this result from Commonplace's suite.
   Record an unavailable fixture as a remaining blocker.

Upgrade cases are the next planning checkpoint after this run. pi, macOS and
other unavailable harnesses keep the triggers in the README. E1 owns promoted
procedure portability; this run does not claim that Bash-shaped procedures are
portable merely because skill routing works.

## Execution boundaries

Read the root AGENTS.md and INSTALL.md. Use disposable initialized projects;
never run init in this source checkout. Before machine changes, record antivirus
products and Smart App Control state, inspect installed paths, and back up the
user PATH. Explain needed installation or persistent environment changes.

Never disable Smart App Control or add antivirus exceptions as a repair.
Launch one executable at a time, never a parallel launcher sweep. Do not launch
through WMI or `powershell -EncodedCommand`; that pattern previously triggered
Avast. A child with a synthesized PATH is not a fully restarted app. Preserve
unrelated files and do not publish another release as part of acceptance.

Record sandbox versus escalated execution, pre-existing antivirus exceptions,
and whether the app was actually restarted. Missing tools or inaccessible
working directories are scoped observations, not a reason to improvise a new
installation procedure. Findings requiring a product change return to the
owning workshop before expanding this run.

## Supported-suite acceptance

The Windows test-suite workshop closed on 2026-11-01. Its fixes are in code,
tests and CI shipped in 0.3.3. [Release CI 41342248088](https://github.com/zby/commonplace/actions/runs/41342248088)
at `526de4edd` passed tests, wheel install, entry-point resolution and scratch
checks on Windows and Linux. The [independent native report](../windows-install/results-2026-11-01-codex-independent.md)
records 821 passed and 13 skipped, including collected slow tests, with no
failures or collection errors. Its skip and antivirus limits remain in that
report. Linux-only analysis tests are excluded from Windows collection.
Reopen suite investigation on a supported Windows CI regression.

## Release acceptance record

- **2026-11-01, 0.3.3 release preparation (Linux).** Operator authorized a
  maintenance release with template recreation retained as a documented known
  limit. Updated package/lock version and reconciled current suite status.
  `uv run pytest -m '' -q`: 1342 passed, 1 skipped in 282.79 seconds;
  `uv run ruff check .`: passed. An earlier full-suite invocation was stopped
  by the 200-second tool timeout without a verdict; the completed rerun above
  is the test result. Editable metadata refresh passed. `uv build` built the
  wheel from the sdist. An isolated non-editable wheel install loaded every
  entry point and passed init, check and landing validation; rerunning init
  preserved both active control-plane files and reproduced the documented
  template recreation. Both edited workshop files validated with no failures
  or warnings. No new native Windows or agent-scenario run was performed.
  Release commit `526de4edd` subsequently passed Windows and Linux
  [CI run 41342248088](https://github.com/zby/commonplace/actions/runs/41342248088),
  including software tests and wheel-install smoke checks. Published both
  wheel and sdist to PyPI and pushed annotated tag `v0.3.3` with release notes.
  A separate isolated Linux install of `llm-commonplace==0.3.3` from PyPI
  passed all entry-point loads, init/check/landings and active control-plane
  preservation; known template recreation was reproduced. Native Windows
  acceptance from PyPI is still the next machine-specific check.
