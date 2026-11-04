# Framework delivery acceptance — 2026-11-03

## Consumer and evidence boundary

This dated record supports installed-project delivery guidance in
[INSTALL.md](../../../INSTALL.md) and acceptance of the delivery mechanisms in
[ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md).
It retains bounded observations, not a claim that every platform, harness or
upgrade path is certified. It is not the remaining-work register.

The checks used the framework-delivery workshop's revision-7 probe protocol
and its Windows delivery handoff. The probe package uses synthetic tokens to
show which library files an agent actually read. Synthetic package revisions
V1–V4 are not Commonplace releases. The Windows installed-package checks used
PyPI Commonplace 0.3.3; the recovery checks used Workjig 0.3.1.

## Earlier baseline and Windows installed delivery

The revision-7 Linux probes recorded index-only named-skill reads and native
worker delegation in Claude Code and Codex. Codex initially returned literal
`$ARGUMENTS` through the index route; a fresh rerun passed after the index's
argument-routing instruction was amended. Claude's earlier stub substituted
the placeholder at both occurrences, motivating the corresponding wording
repair. Those initial failures remain in the historical reports, not converted
to passes by the later correction. Stock pi stopped when no subagent was
available. These observations do not certify unnamed-task triggering or large
skill indexes.

The October 31 Windows installed-project checks used a non-editable Git-main
build at `55700da28`, signed python.org 3.14.7 and shims. Claude listed all 12
skills and passed forked validation with an argument, but the initial session
ran with bypass permissions; its later mode-switch reads did not establish the
read rule's effect. Fresh Codex CLI sessions listed all 12 skills and passed
stub and no-stub index argument routes. They also exposed environment limits:
initial invalid-working-directory errors, unavailable uv/rg in that sandbox,
and an unrequested init attempt after a missing-stub warning which the sandbox
refused. Later successful installation checks do not establish procedure
portability or make that attempted repair acceptable. The execution-channel
compatibility work retains responsibility for those procedure questions.


The Windows PyPI installation repeat passed on Windows 11 with signed
python.org Python, Smart App Control enabled, and regenerated command shims.
All 25 commands and init/check/landing checks passed in the restarted desktop
app and an Explorer-started process. No shadowing warning or security-log
record was observed. These observations do not establish long-term antivirus
behavior or support for the Linux-only analysis workflow.

A fresh default-permission Claude desktop session rooted in a disposable
installed project resolved the shim, listed all 12 native Commonplace skills,
ran native `cp-skill-validate kb/log.md` in a fork, and passed init check.
The read-rule effect was not established by that run.

The later Codex check used an existing source-rooted desktop chat, not a fresh
installed-project session. Its bundled executable reported
`codex-cli 0.166.0-alpha.5.1`; the desktop app version and exact model were not
established. Commands ran in `C:/Users/zzbby/cp-install-test-pypi033` under a
workspace-write sandbox. It passed:

- bare shim discovery and command help;
- shell reads of the project pointer, stub and installed skill;
- index-based validation of `kb/log.md` with the argument preserved;
- `commonplace-init --check`, with all 26 outputs `ok`.

No native Commonplace skills were supplied to that source-rooted chat. That
is not evidence of installed-project native-discovery failure. The run did not
test a native invocation, fork, worker, upgrade or restart. The tool inventory
needed an approved escalation after a `.lock` access denial; other listed
checks ran without escalation. No repair was performed. Shell reads do not
test Claude's native Read permission rule.

## Windows Claude read-rule defect

Four fresh default-permission Claude desktop sessions used disposable projects
with the same installed library and different rule spellings. The operator
accepted workspace trust and rejected every file-read prompt. Native Read of
the installed validation skill produced these results:

| Rule | Observation |
|---|---|
| Init-generated `Read(//C:/…/**)` | Prompted and was rejected |
| No read rule | Prompted and was rejected |
| `Read(//c/…/**)` | Content returned |
| `Read(~/…/**)` | Content returned |

No user-level Claude settings existed; managed policy was not observable.
The paired rule-on/rule-off result shows that init's drive-letter spelling did
not grant the intended access in this configuration. The successful variants
were judged by returned content under the operator's prompt-rejection policy,
not by a separate prompt-observation channel. Other drives, UNC paths and
libraries outside the home directory were not tested.

An earlier default-mode run returned both the library and an outside-rule
control file under the original rule. That observation remains unexplained;
it does not cancel the later matched comparison.

**Operator disposition:** on 2026-11-03, defer the product fix until a Windows
user reports library-read prompts. At that trigger, the init/library maintainer
should test generation of `//<lowercase drive>/<path>` in one disposable project.
This record preserves that decision; it does not authorize implementing the
fix early. The current install guidance must not promise prompt-free Windows
reads from the generated rule.

## pi user-level worker copy on Linux

On Linux `6.8.0-147-generic`, pi 1.3.0 with `openai/gpt-6-astra` / low thinking
loaded an unchanged user-level copy of the checkout subagent extension and
`commonplace-worker` definition in a disposable Commonplace 0.3.3 project.
The active user installation and settings were not changed.

An initial attempt stopped before delegation because the scratch project lacked
the probe's library-routing instruction. After adding the protocol-supplied
instruction, a fresh parent followed the installed skill stub and launched one
worker through the harness-provided `subagent` tool. The worker read the
installed probe file and returned `DELEGATED-STEP-V1`. The parent did not read
that file. The worker's persisted conversation contained only its handoff;
a parent-only marker was absent. Both processes exited zero, and 988 hashed
fixture files remained unchanged. No extension change was needed.

This establishes installed-copy discovery and a fresh-conversation file read,
not complete execution of all delegating skills, Windows/macOS workers,
continuation or nesting. Earlier stock-pi probes had no subagent facility and
correctly stopped. A previously blocked Sol API route was not retested.

## pi live-session synthetic upgrades on Linux

A separate pi 1.3.0 / OpenAI Astra run used the copied probe package, an actual
interactive TUI and a read-only model tool selection. One process and saved
conversation remained alive across eight prompts; a final fresh process
received one prompt. No delivery hooks or observer extensions were used.

| Change | Observed result |
|---|---|
| Same-root V1→V2 library update | All init outputs remained `ok`; explicit rereads returned V2 without init, reload or restart |
| V3 skill description and body change | Both read-skill stubs and the library index became stale; init repaired them; rereading returned V3 and the new body marker |
| Metadata after init | Tool-free questions still returned the originally loaded description |
| Actual TUI `/reload` | A tool-free answer returned the new description, including a second marker never previously exposed through model prompts or reads |
| Editable install followed by a source bump to V4 | All ten pointers/settings outputs were stale; before repair, explicit reads through them still returned the old shared-data V3 snapshot |
| Init after the move | The same session's native skill invocation followed the repaired stub into the source library and returned V4 without another reload |
| Fresh process | Native skill invocation also read V4 and exited zero |

These results distinguish rereading file contents, repairing generated pointers,
and refreshing the harness's loaded skill metadata. The prompts explicitly
requested current file reads. They do not establish automatic upgrade detection,
a real Commonplace release transition, or another runtime's refresh behavior.

## Workjig recovery

The unchanged strict Workjig 0.3.1 recovery fixture passed on Linux and Windows,
including reading evidence through another handle while the lock was held.
The Windows run used the installed Commonplace tool's signed Python interpreter.
The earlier 0.3.0 Windows in-lock read failure remains historical; a relaxed
diagnostic variant was not acceptance of the original fixture. Commonplace
added no production locking workaround.

## Closure disposition

On 2026-11-03 the operator approved deferring the real-release upgrade repeat
until the next published Commonplace release transition, and other-runtime live
upgrade checks until a user reports upgrade trouble or a relevant runtime
changes resource loading. The operational owners, triggers and required checks
are retained in [INSTALL.md](../../../INSTALL.md#maintainer-acceptance-triggers),
including the existing platform/workload deferrals and Windows read-rule defect.
The workshop closes on that bounded basis, not because the deferred cases
passed. Procedure portability and multi-day antivirus observation remain with
their separate ongoing work.

## Provenance and retained limits

Detailed dated observations, revision-7 probe package, worker requirements,
checkout nesting verification, and both strict recovery fixtures remain
recoverable in Git. The completed workshop's 46 tracked files were removed,
not promoted wholesale into a permanent register. Product guidance and this
bounded evidence summary are retained; no new workshop redirects were added.

Historical records:

- Windows installation: commit `600306e1d`, under `kb/work/windows-install/`.
- Windows delivery, matched read rules, strict recovery and Codex check:
  commit `c20a49abe`, under `kb/work/framework-delivery/`.
- Linux worker copy and live-session upgrades: commit `6bb76a807`, same directory.

For example, `git show 6bb76a807:kb/work/framework-delivery/results-2026-11-03-linux-pi-live-upgrades.md`
retrieves the complete live-session record. Raw Linux sessions were retained
locally under the reports' named temporary evidence directories; this summary
does not depend on those directories surviving. Disposable Linux tools,
projects and credential copies were removed.

No additional acceptance follows for macOS, enterprise policy, large indexes,
real-release transitions or cross-runtime live upgrades. Further coverage must
be recorded separately rather than silently broadening this dated result.
