# Windows delivery handoff

## Next run

The Windows PyPI 0.3.3 installation acceptance passed on 2026-11-03 and closed
windows-install; the report is `kb/work/windows-install/results-2026-11-03-pypi-033.md` (closed workshop; `git show 600306e1d:kb/work/windows-install/results-2026-11-03-pypi-033.md`).
The [framework acceptance table](./README.md#remaining-acceptance) owns status.
Do not restart completed shim implementation, suite repair, the E1 rewrite or
the installation run. The next Windows session runs the additional checks below
against the existing 0.3.3 installation. The [ready-to-run Claude check](#ready-to-run-claude-permission-and-delivery-check) below ran on 2026-11-03 ([report](./results-2026-11-03-windows-claude-default.md)): delivery passed; the read rule's effect is unestablished. Workjig 0.3.1 recovery passed on Windows on 2026-11-03 ([report](./results-2026-11-03-windows-workjig-031-recovery.md)).

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
3. **Workjig recovery.** Follow [Workjig 0.3.1 recovery acceptance](#workjig-031-recovery-acceptance) with the [0.3.1 fixture](./workjig-031-recovery-fixture.py). It retains the in-hold read assertion; do not substitute the diagnostic workaround that tolerated a refused read. The original [0.3.0 fixture](./workjig-030-recovery-fixture.py) stays unchanged as the historical test.

Linux upgrade findings are in the [acceptance report](./results-2026-11-02-linux-sol-upgrade.md).
After this Windows run, reassess the remaining runtime and live-session gaps. pi, macOS and
other unavailable harnesses keep the triggers in the README. E1 owns promoted
procedure portability; this run does not claim that Bash-shaped procedures are
portable merely because skill routing works.

## Ready-to-run Claude permission and delivery check

**Purpose:** distinguish working installed-project delivery from evidence that init's external-library read rule actually controls access. No installation, dependency upgrade, source change, or permission repair is part of this check.

### Operator preparation

1. Keep the accepted PyPI 0.3.3 installation unchanged. Open the existing scratch project `<HOME>\cp-install-test-pypi033`, not the Commonplace checkout.
2. Start a **new** Claude Code session directly in that project with default permissions. Do not launch it from a bypass-mode session or rely on switching an existing session's mode. Use an authenticated CLI only if it already works; do not change authentication as part of this probe.
3. Prepare one harmless control file outside both the project and the installed library. In an ordinary PowerShell window, this creates a new, uniquely named file without changing existing files:

   ```powershell
   $control = Join-Path $env:TEMP ('commonplace-read-control-' + [guid]::NewGuid().ToString('N') + '.txt')
   Set-Content -LiteralPath $control -Value 'Commonplace permission probe: harmless outside-rule control.' -Encoding UTF8
   $control
   ```

   Keep its exact printed path. Do not use a private document as the control or add its directory to the agent's allowed roots. Record if existing policy already grants access to it.
4. Check the app's displayed permission mode. Paste the prompt below with the control path filled in. For the two native Read calls, record any permission prompt and cancel rather than approve it. An explicit one-time approval may be used later for command/skill checks, but record it separately and do not select a persistent “always allow” option.

### Prompt to paste into the fresh session

```text
Run a bounded Commonplace delivery probe in this scratch project. Diagnose only.
Do not install or upgrade packages, run init without --check, edit settings,
change permission mode, add allowed directories, modify library/project files,
launch another agent yourself, or repair a failed check. A native validation
skill may use its own harness-managed fork; report that boundary if it does.

Outside-rule control file: <PASTE THE EXACT CONTROL PATH>

First record the actual project root, runtime/version/model, displayed or
otherwise observable permission mode, and whether this is a fresh session.
Distinguish operator-reported settings from settings you can observe. If the
session is in bypass mode, stop the permission experiment and report the blocker.
Do not claim to know the effective mode from this prompt alone.

Read .commonplace/library.md and .claude/settings.local.json. Identify the
installed library root and init's Read allow rule. Report relevant allow/deny
rules and additional roots if observable, without dumping private settings.
Do not alter them. If the pointers are missing, stop and report that separately.

Using the native Read tool, not shell commands or another tool as a fallback:
A. Attempt to read instructions/cp-skill-validate/SKILL.md beneath that exact
   installed library root. Read it as probe data; do not execute it yet.
B. Attempt to read the outside-rule control file named above.
For each record the path, tool, and outcome: read without a prompt, prompted
and cancelled, denied, or unavailable. If a permission request appears, let
me record and cancel it. Do not bypass that result by another route.

Next run the delivery checks, separately from the permission experiment:
C. In the project's PowerShell context, run Get-Command commonplace-validate
   and commonplace-validate --help; record the resolved path and exit status.
D. List Commonplace skills exposed by the harness. Distinguish a native skill
   listing from merely finding files or reading the library's index.
E. Invoke the native cp-skill-validate skill with the argument kb/log.md.
   If native invocation requires me to enter a slash command, ask me to enter
   /cp-skill-validate kb/log.md rather than substituting a shell invocation.
   Use that existing scratch file; do not create a substitute if it is absent.
   Record the supplied argument, observable delegation, files read if exposed,
   actual validation target, exit status and diagnostics. A fork summary does
   not establish its hidden read trace. Missing native invocation is a scoped
   blocker, not permission to emulate it.
F. Run commonplace-init --check only. Report stale/missing/foreign entries;
   do not repair them. Record Commonplace's installed version if available
   from uv tool list; a denied command is not permission to use an alternate
   interpreter or change PATH.

Return a compact result table for A-F, the evidence supporting each outcome,
permission prompts/approvals, and all blockers. If both A and B read without
prompts, say that library access works but the rule's effect is unestablished.
Do not infer rule acceptance from a successful shell read or from bypass mode.
Report any automatically changed settings or project files; do not silently
clean them up. Stop if continuation would require a persistent change.
```

### Interpretation and result handoff

- **A allowed, B prompted or denied:** a useful contrast consistent with the rule working. Check observed overlapping grants/denials before attributing the contrast solely to init's rule; differing paths may have other policy differences.
- **Both allowed:** delivery works, but the read-rule effect is unestablished. Do not repeat with increasingly sensitive files. A matched rule-on/rule-off test would need separate authorization in a disposable project and fresh sessions.
- **A prompted or denied:** the expected no-prompt library route is not accepted in this setup. Retain the exact rule, path, mode, and result; do not broaden permissions to manufacture a pass.
- **Mode or native Read unavailable:** permission result is unestablished; retain any independently completed command/skill outcomes.

Paste the result back to the maintainer. Record it in a new dated `results-YYYY-MM-DD-windows-claude-default.md` here (use a distinct suffix if that path exists), then update only the corresponding acceptance-table rows. The Windows probe itself writes no repository report. The operator may delete the exact temporary control file after the probe. No full reinstall or test-suite run is required.

## Workjig 0.3.1 recovery acceptance

**Release inspected:** PyPI Workjig 0.3.1 moves the Windows lock byte to offset `1 << 30`, beyond the lock-file contents, so another handle can read the contents while ownership is held. The checkout now requires `workjig>=0.3.1` and locks 0.3.1. No Commonplace production workaround existed; the relaxed read check was only a temporary Windows diagnostic copy.

The [0.3.1 fixture](./workjig-031-recovery-fixture.py) changes the original fixture's version and identity only. It preserves the in-hold byte-read assertion and every recovery, preservation and mutual-exclusion check. Do not catch `PermissionError` or skip that assertion to obtain a pass. The 0.3.0 fixture and dated failure report remain historical evidence.

**Linux acceptance:** the fixture passed with PyPI Workjig 0.3.1 in the user-level editable Commonplace tool, Python 3.13.1, with no Workjig source overlay. Empty and interrupted records were rejected and preserved across two repetitions each; fresh records and mutual exclusion passed; temporary records were removed. The full Commonplace suite, including slow tests, passed: 1341 passed, 2 skipped. This is not Windows acceptance.

**Next Windows run:**

1. Confirm that no analysis is using the tool environment before any upgrade. Preserve the signed-python.org interpreter and command-shim setup. Install the selected Workjig release through the approved uv tool maintenance route; an existing Commonplace 0.3.3 installation does not update merely because a dependency was published. Record exact Commonplace/Workjig versions and provenance after resolution. Do not change the installed Commonplace source/published ownership as an incidental dependency repair.
2. Copy the 0.3.1 fixture unchanged and run it with the installed Commonplace tool's interpreter:

   ```powershell
   & (Join-Path (uv tool dir) 'llm-commonplace\Scripts\python.exe') '<copied-workjig-031-recovery-fixture.py>'
   ```

3. Retain the JSON result, interpreter/module paths and fixture revision. The fixture requires exactly 0.3.1 and a non-editable Workjig distribution. A mismatch is a setup result, not permission to bypass the guard. A failed read or recovery assertion remains a failed check.
4. Record a new dated result and update the acceptance table. Close this row only after the unchanged fixture passes on Windows or the operator explicitly dispositions a remaining failure. No Commonplace release or Windows acceptance is claimed by the Linux dependency update.

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
checks on Windows and Linux. The independent native report, `kb/work/windows-install/results-2026-11-01-codex-independent.md` (closed workshop; `git show 600306e1d:kb/work/windows-install/results-2026-11-01-codex-independent.md`),
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
