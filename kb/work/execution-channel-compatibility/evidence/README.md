# Execution-channel probe evidence

Store one report per execution-channel probe. Reports are append-only observations, not normative instructions.

## Naming

Use:

```text
YYYY-MM-DD-<runtime>-<surface>-<os>-<interface>-<short-id>.md
```

Examples:

```text
2026-07-28-codex-app-windows-powershell-a1.md
2026-07-28-codex-cli-wsl-bash-b1.md
2026-07-28-claude-code-linux-bash-c1.md
```

The short id only distinguishes repeated runs. Do not put usernames, hostnames, or secrets in filenames.

Use the same naming scheme for later rounds and record the round inside the report. A repeat of an environment first creates a new report and links the prior related report so the observations can be compared. Once the newer report fully reproduces the same environment and differs only because the procedure was revised, the superseded report may be retired; record that supersession in the retained report. Keep reports that contradict one another or describe non-equivalent environments.

The procedure ID distinguishes revisions within a round. Keep reports produced by older procedure IDs unchanged; later synthesis must account for fields that an earlier revision did not request.

## Reports under older models

The three reports dated 2026-07-28 used procedure v4–v6, written for the project-venv and direnv command model that [ADR 064](../../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) replaced, and before [ADR 086](../../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) moved the library into the installed package. Their tool-call persistence, tool discovery and bare-name results remain usable; their venv, direnv and `kb/commonplace/` layout findings describe the old model only. Procedure v7 reports are not directly comparable on those fields.

## Current coverage — 2026-11-03

The October Windows report in this directory used v6 on an old checkout.
Later Windows and Linux acceptance is summarized in the
[retained delivery record](../../../reports/retained/framework-delivery-acceptance-2026-11-03.md),
but those runs did not execute this workshop's breadth protocol. The
[November rebaseline](../rebaseline-2026-11-03.md) is source inspection and
evidence reconciliation, not a new runtime report. Revise v7 for supported
Windows shims before commissioning a current comparable breadth run.

## Evidence discipline

- Start from [result-template.md](./result-template.md).
- Follow [the probe procedure](../probe-procedure.md) without repairing the environment.
- Treat `not run` with an explicit unmet prerequisite as valid evidence; do not fill template cells by assuming source-checkout paths or invoking unobserved tools.
- Record exact versions and launch paths where visible.
- Bound command output and redact secrets; never dump the full environment.
- Before sharing or saving, normalize workspace, home/profile, and temporary-directory prefixes and complete the procedure's mandatory disclosure review on the final payload.
- Never retain raw `direnv status`, marker values, configuration/profile contents, alias targets, function definitions, unrestricted Git status, or secret-scanner matches.
- Use `observed`, `documented`, `inferred`, and `unknown` consistently.
- A contradictory report remains; later synthesis explains the differing runtime/version/channel conditions instead of overwriting it.
- Do not edit another agent's report to normalize its result. Add a correction note or a new run.

An agent that cannot write the repository should return a completed template to the operator. Lack of write permission is itself a channel fact but should not trigger escalation solely to store workshop evidence.
