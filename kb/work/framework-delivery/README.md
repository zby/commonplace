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
No new runtime evidence is claimed by this reorganization (2026-11-01).

| Surface | Evidence and limit |
|---|---|
| Release and supported suite | [Release CI](https://github.com/zby/commonplace/actions/runs/41342248088) passed tests and wheel install/init checks on Windows and Linux. The Windows test-suite workshop is closed; analysis execution remains Linux-only. |
| Linux installed delivery | Revision 4 [Claude Code](./results-claude-code-r4.md) and [Codex](./results-codex-r4.md) establish baseline routes and upgrade observations. Revision 7 [Claude Code](./results-claude-code-r7.md), [Codex](./results-codex-r7.md) and [pi](./results-pi-r7.md) add index, missing-init, worker and argument checks. Read each report's rooting and coverage limits. |
| Windows install | [Run 4](../windows-install/results-2026-10-31-afflicted-main-run4.md): all 25 commands, init/check/landings, restarted app and Explorer-started process passed on Git main. [Independent Codex](../windows-install/results-2026-11-01-codex-independent.md): representative commands and 821 tests passed; no fresh install or restart. Neither is PyPI 0.3.3 acceptance. |
| Windows agent routing | [Installed-project report](./results-2026-10-31-windows-installed-project-agents.md): Claude Code and Codex listed skills and passed stub arguments; Codex passed the no-stub index route. Claude's read-rule effect was not established. |
| pi workers | [Requirements](./sub-agent-requirements.md) and [checkout verification](./pi-nesting-control.md) cover the extension's worker/depth budgets. INSTALL.md prescribes the user-level copy; installed-project acceptance remains pending. |

The original [Windows 0.3.0 report](./results-windows-install-030.md) is retained
because the installation and antivirus workshops still use its findings.
Template recreation after renaming the control-plane templates is an accepted,
documented 0.3.3 limit. Revisit it when init's lifecycle changes or it interferes
with an upgrade; it does not block acceptance here.

## Remaining acceptance

This table is the single status list. The [Windows handoff](./windows-delivery-handoff.md)
provides the next run's instructions, not a separate implementation backlog.

| Item | Next action or trigger | Evidence needed |
|---|---|---|
| Windows PyPI installation | Next Windows run; owned by [windows-install](../windows-install/README.md). | Follow INSTALL.md steps 1–4 for 0.3.3, rerun shims, test fresh processes inside/outside the restarted app, and record package provenance. |
| Claude Windows read rule | In that run if a default-permission session or authenticated CLI is available; otherwise retain the exact blocker. | Agent rooted in the scratch project reads one file inside the rule and one outside it. If both are permitted independently, report the rule's effect as unestablished. |
| Upgrade acceptance | After the PyPI checkpoint, choose the next bounded upgrade probe. | Distinguish changed skill metadata, library-only change, moved installation and an already-running session; record pointer warnings, reads before/after init and any required restart. Existing probe results are partial evidence, not full current-release acceptance. |
| Focused Workjig recovery | Next Windows run if released dependency tests or a bounded verification fixture are available. | Against installed Workjig 0.3.0: existing interrupted-marker bytes remain unchanged and rejected; a new lock is accepted. Record package provenance; no local source overlay. A missing fixture is a blocker, not a pass. |
| pi installed worker copy | Deferred until the next installed-project pi run. | INSTALL.md user-level extension and worker copy, then probe case 10 in a scratch project; use the requirements checklist. |
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
trigger. After the Windows repeat, reassess the upgrade and recovery items;
do not silently defer them merely because a release passed CI. Promote any new
durable rule to INSTALL.md, the owning ADR or instructions. Transfer still-live
deferrals and evidence needed by their owners before deleting this directory
and its entry in the workshop index.
