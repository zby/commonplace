# Framework delivery acceptance

## Goal and authority

Posed by the operator on 2026-09-23 to decide how installed projects receive
Commonplace's library and skills. The design is adopted in
[ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md).
The remaining goal is to establish that agents in installed projects can find
and read that library, invoke skills with arguments, use the required worker
facility, and recover correctly after upgrades or installation moves.

This is an acceptance workshop. ADR 086, its amendments and
[INSTALL.md](../../../INSTALL.md) govern the product. Preserve these constraints:

- One user-level uv tool contains the code and library. Projects receive
  pointers and skill stubs, not a copied library or a second plugin channel.
- Init owns project pointers; session start does not repair the installation.
  Never run init in this source checkout.
- The base route uses standing instructions and the library index; native
  skills add a second route. Both must work without hooks or an MCP server.
- Skills needing workers use a harness-provided sub-agent, including a harness
  extension. Shell-launched headless processes are not an emulation (ADR 086's
  worker amendment). The analysis workflow's workers have a separate contract.
- The signed-Python/shim Windows prerequisite is adopted in
  [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md).
  It supersedes the original assumption that every platform needs identical setup.

Evaluation covers Claude Code and Codex, the base route in other qualifying
harnesses, Linux/macOS/Windows, source and installed-project layouts, and
changed-skill, library-only, moved-install and running-session upgrade cases.
A result applies only to its recorded runtime, permissions and installation.

## Evidence established

Current baseline: PyPI **0.3.3**, release commit `526de4edd`, Workjig 0.3.0.
The [2026-11-02 Linux acceptance report](./results-2026-11-02-linux-sol-upgrade.md)
adds isolated PyPI installation, synthetic upgrade, pi catalog and recovery evidence.

| Surface | Evidence and limit |
|---|---|
| Release and supported suite | [Release CI](https://github.com/zby/commonplace/actions/runs/41342248088) passed tests and wheel install/init checks on Windows and Linux. The Windows test-suite workshop is closed; analysis execution remains Linux-only. |
| Linux installed delivery | Revision 4 [Claude Code](./results-claude-code-r4.md) and [Codex](./results-codex-r4.md) establish baseline routes and upgrade observations. Revision 7 [Claude Code](./results-claude-code-r7.md), [Codex](./results-codex-r7.md) and [pi](./results-pi-r7.md) add index, missing-init, worker and argument checks. Read each report's rooting and coverage limits. |
| Linux follow-up | [Sol acceptance report](./results-2026-11-02-linux-sol-upgrade.md): isolated PyPI 0.3.3 init/check/landings passed. Fresh Codex Sol read old V2 through stale pointers, then V4 through repaired moved-root pointers after a library-only update without another init. Synthetic versions are not real releases. |
| Windows install | PyPI 0.3.3 acceptance, 2026-11-03 (`kb/work/windows-install/results-2026-11-03-pypi-033.md` (closed workshop; `git show 600306e1d:kb/work/windows-install/results-2026-11-03-pypi-033.md`)): INSTALL.md steps 1–4 over signed python.org Python with Smart App Control on, shims rerun; all 25 commands, init/check/landings passed in the restarted desktop app and an Explorer-started process, with no shadowing warning or security-log record. Earlier Git-main run 4 and the independent Codex run are in the same directory's history. The windows-install workshop closed on 2026-11-03. |
| Windows agent routing | [Installed-project report](./results-2026-10-31-windows-installed-project-agents.md): Claude Code and Codex listed skills and passed stub arguments; Codex passed the no-stub index route. Claude's read-rule effect was not established. PyPI 0.3.3, 2026-11-03 ([default-permission report](./results-2026-11-03-windows-claude-default.md)): in a fresh default-mode Claude session rooted in the scratch project, the shim resolved, all 12 skills were natively listed, native `cp-skill-validate kb/log.md` passed in a fork, and `--check` was clean. |
| pi workers | [Requirements](./sub-agent-requirements.md) and [checkout verification](./pi-nesting-control.md) cover the extension's worker/depth budgets. The [2026-11-03 installed-copy check](./results-2026-11-03-linux-pi-worker-copy.md) passed on Linux with pi 1.3.0 and OpenAI Astra: unchanged user-level extension/definition, installed-project worker discovery, fresh conversation, and delegated installed-file read. This does not establish other platforms or complete delegating-skill workloads. The earlier Sol route's no-credit result remains historical. |

The original [Windows 0.3.0 report](./results-windows-install-030.md) is retained
because the installation and antivirus workshops still use its findings.
Template recreation after renaming the control-plane templates is an accepted,
documented 0.3.3 limit. Revisit it when init's lifecycle changes or it interferes
with an upgrade; it does not block acceptance here.

The [2026-11-03 Codex existing-session check](./results-2026-11-03-windows-codex-existing-session.md)
independently passed the active 0.3.3 shim route, shell library reads,
index-based validation with a file argument, and all 26 init freshness entries.
It began in the source checkout, so it adds no fresh installed-project native
skill-discovery or permission-rule evidence.

## Remaining acceptance

This table is the single status list. The [Windows handoff](./windows-delivery-handoff.md)
provides the next run's instructions, not a separate implementation backlog.

| Item | Next action or trigger | Evidence needed |
|---|---|---|
| Claude Windows read rule | Defect found 2026-11-03; deferred by the operator until a Windows user reports library-read prompts. Then make init write `//<lowercase drive>/…` on Windows and confirm with one disposable project. | [Matched test](./results-2026-11-03-windows-claude-read-rule-matched.md): in default mode the library read prompted both with init's `Read(//C:/…/**)` rule and with no rule, and went through with `Read(//c/…/**)` or `Read(~/…/**)`. init's rule has no effect on Windows. The earlier [default-permission probe](./results-2026-11-03-windows-claude-default.md), whose reads went through under the same rule, is unexplained. |
| Upgrade acceptance | Linux pi synthetic live-session checks passed. Repeat applicable cases for a real release transition or another runtime, or obtain an explicit deferral with a trigger before closure. | [Live-session report](./results-2026-11-03-linux-pi-live-upgrades.md): pi 1.3.0 / OpenAI Astra reread V2 without init, followed the V3 skill body after init, and refreshed advertised metadata through the actual TUI `/reload`. A path move left stale pointers reading V3; init repair let the same session and a fresh process read V4. Prompts explicitly requested current reads; no automatic recovery or real Commonplace release transition is certified. |
| Focused Workjig recovery | Passed on Linux and Windows; reopen on a Workjig locking change. | Windows, 2026-11-03 ([report](./results-2026-11-03-windows-workjig-031-recovery.md)): the unchanged [0.3.1 fixture](./workjig-031-recovery-fixture.py), in-hold read included, passed with PyPI Workjig 0.3.1 under the installed Commonplace 0.3.3 tool's signed python.org interpreter. Linux passed with the full suite (1341 passed, 2 skipped). The historical 0.3.0 fixture failed on Windows on the in-hold read. |
| pi installed worker copy | Passed on Linux; reopen when the extension's installation or launch path changes, or another platform needs acceptance. | [Installed-copy report](./results-2026-11-03-linux-pi-worker-copy.md): pi 1.3.0, OpenAI Astra, PyPI Commonplace 0.3.3. The unchanged user-level copy launched one fresh worker from a disposable installed project. The worker read the installed probe file and returned its token; the parent did not read it. Initial probe-routing setup failure is retained separately. |
| macOS | Deferred until a macOS host is available. | Published-package install plus installed-project delivery checks. |
| Other harnesses and enterprise policy | Deferred until an actual user/environment is available. | [Probe request](./probe-request.md): standing-instruction loading, external reads, skill/index routes and worker availability under normal policy. Internal details may be anonymized. |
| Large index, unnamed tasks and additional skill metadata | Deferred until a real workload or harness requires these cases. | Verify discovery and triggering at that scale, including metadata beyond name/description; do not infer coverage from the small synthetic index. |

E1 procedure portability belongs to
[execution-channel compatibility](../execution-channel-compatibility/e1-windows-execution.md).
Multi-day antivirus acceptance belongs to
[signed-Python field use](../windows-signed-python-field-use/README.md).
Their implementation queues are not duplicated here and they do not block the
bounded Windows installation repeat.

## Running and recording checks

- [Windows handoff](./windows-delivery-handoff.md): next machine run and its boundaries.
- [Run prompts](./run-prompts.md): isolated harness runs and upgrade preparation.
- [Probe protocol](./probe-package/PROTOCOL.md): revision 7 fixture, dated to
  2026-10-24, with the 2026-11-01 worker-rule clarification. Compare the relevant
  fixture behavior with current init before treating it as release acceptance.
- [Probe request](./probe-request.md): external respondents' outcomes and limits.

Keep dated reports unchanged except to repair references. Write each new result
to a new dated file; record package/commit, runtime, project root, permissions,
restart state, exact cases, observations, workarounds and omissions. Update this
table from those results. Probe failures do not authorize changing support scope,
security policy or the delivery architecture. Bring such decisions to the operator.

## Closure

Close when each remaining item has evidence or an explicit deferral with a
trigger. The Windows PyPI repeat, Linux pi worker-copy check and Linux pi
synthetic live-session upgrade checks passed on 2026-11-03. Real-release and
cross-runtime upgrade coverage still needs evidence or explicit disposition;
do not silently defer it merely because a release passed CI. Promote any new
durable rule to INSTALL.md, the owning ADR or instructions. Transfer still-live
deferrals and evidence needed by their owners before deleting this directory
and its entry in the workshop index.
