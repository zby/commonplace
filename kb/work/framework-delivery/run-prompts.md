# Run an isolated delivery check

Use the [Windows handoff](./windows-delivery-handoff.md) for the PyPI 0.3.3
acceptance run. Use this page for a synthetic harness or upgrade probe after
selecting its cases from the [acceptance table](./README.md#remaining-acceptance).

## Preparation

Read the [protocol](./probe-package/PROTOCOL.md) and [request](./probe-request.md).
Revision 7 models init as of 2026-10-24, not every later release change. Compare
the behavior under test with current init before running; record differences
rather than silently changing the shared fixture. The worker rule was clarified
on 2026-11-01 to require a harness-provided sub-agent.

Choose one harness and a unique scratch root. Copy the probe package there.
Use isolated `UV_TOOL_DIR` and `UV_TOOL_BIN_DIR` for every uv tool operation;
put that bin directory first on PATH for the sessions in the run. Do not touch
the real Commonplace user tool or credentials. Initialize the copied test
project and record init and check output.

Every test agent must start rooted in the initialized scratch project. A worker
inheriting this checkout's instructions is not evidence about an installed
project. Use a new top-level session for harness scenarios when necessary;
this is distinct from the skill worker facility tested by case 10.

Run one harness at a time. Concurrent file mutations and inherited environments
make upgrade evidence ambiguous. Record OS, shell, harness/model, package
revision, permissions, effective library path and any environment changes.

## Prompt

> Run only the selected delivery-probe cases in this isolated project using
> probe-package/PROTOCOL.md. Read the installed pointers and skill stubs; do not
> use the Commonplace source checkout to answer a missing-library question.
> Follow ADR 086's worker rule: a worker-dependent skill uses a harness-provided
> sub-agent; if none exists, stop that case with "no sub-agent available".
> Do not emulate one with a shell-launched harness. Record observed tokens,
> arguments, file paths, prompts/denials and any workaround. Separate observed
> behavior from inference. An unavailable case is a result, not permission to
> install an integration or change security settings. Return results for a new
> dated report; do not overwrite a previous run.

## Upgrade coverage

Select the cases that distinguish the current unknown. Case 5 exercises a
library change and skill metadata change; case 6 exercises an install-mode
switch. Record reads before and after init. An already-running session is a
separate case: retain it across the change and compare with a fresh session.
Do not count the fixture's move as proof about a real release's directory move.

For installed-project pi worker acceptance, use INSTALL.md's user-level copy,
then case 10 in the scratch project. The source checkout's extension does not
establish that the user-level installation loads correctly. Use the
[sub-agent requirements](./sub-agent-requirements.md) for any deeper check.

## Finish

Use [RESULTS-TEMPLATE.md](./probe-package/RESULTS-TEMPLATE.md) for a new
`results-<date>-<harness>-<scope>.md`. Record selected cases, omissions and cleanup.
Remove probe-owned outputs with `cp-delivery-probe-init --remove`, uninstall
only the isolated `cp-delivery-probe` tool and remove the scratch root. Keep
needed evidence before cleanup. Update the README acceptance table from the
result; do not create another backlog in the report.
