# Batch 02: launch verified; both pipelines stopped

## Assignment and launch

On 2026-10-12 the batch coordinator resumed the pair blocked in
[batch 01](./batch-01.md): Academic Research Skills and ACE. Source identities
and lack of conflicting assignments were retained from that batch; no historical
findings were supplied to either fresh analysis coordinator. Both requested
current upstream tips, without revision pins.

Origin was clean on `main` at method commit
`211129c85fe4794bd8a111066e3d0ecae7f6a3c6`. The batch coordinator's runtime
exposed `openai/gpt-6.1-sol`, medium. Its standing worker diagnostic succeeded.
A separate fresh coordinator then verified the previously failing nested path
with explicit arguments:

```json
{
  "agent": "commonplace-worker",
  "agentScope": "project",
  "cwd": "/home/zby/llm/commonplace",
  "task": "This is a Commonplace worker-launch diagnostic. Reply with COMMONPLACE_WORKER_OK and any agent-depth or nesting-limit values explicitly exposed in your runtime instructions; report unknown otherwise. Do not read files, use tools, invoke skills, spawn workers, or modify anything.",
  "model": "openai/gpt-6.1-sol",
  "thinkingLevel": "medium"
}
```

Its exact returned result was:

```text
COMMONPLACE_WORKER_OK
agent-depth: unknown
nesting-limit: unknown
```

This clears the observed lookup blocker, not a maximum-depth or capacity claim.
Two fresh project-scoped `commonplace-coordinator` sessions were dispatched in
one parallel call, with explicit `openai/gpt-6.1-sol` / medium overrides. Each
performed its own successful diagnostic. Analytical workers used `pi-sol`.

## Academic Research Skills

- Source: `https://github.com/Imbad0202/academic-research-skills`.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/academic-research-skills-af879d1883bd`.
- Command directory: the worktree's `.venv/bin`.
- Preparation record: the worktree path plus `.preparation.json`.
- Run: `AAS-2026-10-12-academic-research-skills-af879d1883bd-01`.
- Frozen source: `related-systems/Imbad0202--academic-research-skills/` in that worktree,
  commit `d1e51716e53fc371727ea6164dd709fc8ea28c97`.
- Reserved publication destination: `kb/agentic-system-analyses/retained/academic-research-skills/`.

Acquisition and boundary jobs completed. Runtime attempt `000005-runtime`
reported prior-analysis exposure and failed. The last advance exited **2**,
with no separate stderr reported. Its exact output was:

```text
stop runtime 000005-runtime: the worker reported a problem; the worker wrote: # Problem

Stopped under `follow-worker-rules.md` § Avoid prior-analysis exposure. A source search of `shared/cross_model_verification.md` exposed audit-derived bakeoff findings in line 67, including measured recall and latency comparisons attributed to `audits/bakeoff-gpt-5-6-sol-codex-2026-08-19.md`. The audit file itself was not opened, but its findings were delivered in the tool result. The worker rule requires stopping when any tool exposes audit findings and states that this run cannot use the worker's work.

No runtime report was written. No target code, tests, examples, providers or services were executed; no source or coordinator-owned state was modified. Report validation was not run because no report was produced. Recovery requires coordinator action; this worker has no authority to resume after the exposure.
publishable: no
```

The [inspection JSON](./batch-02-academic-research-skills-inspect.json) was
captured unchanged using this run's command environment after the coordinator
returned. It reports `state: stopped`, `publishable: false`, no open attempts,
and the failed runtime attempt. Evidence remains under the worktree's
`kb/agentic-system-analyses/state/AAS-2026-10-12-academic-research-skills-af879d1883bd-01/`:
`run.json`, `effects/acquire.json`, `artifact/boundary.md`,
`artifact/ARTIFACT.yaml`, `state/attempts/`, `state/versions/`,
`state/judgments/000004-check-boundary-0.json`, and the boundary/runtime
handouts under `state/handouts/`.

No publication occurred. No fresh publication audit or integration is due.
The worker's report is retained evidence, not an independent source audit.
The source's embedded audit findings raise a consequential interpretation
question: does the prior-analysis exposure rule intentionally exclude upstream
system evidence of this kind? This batch does not decide that question or edit
the method. Recovery requires a separate operator decision under the
[driver's stop rules](../../agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md).
Do not reuse the exposed worker's work, strip source content, or bypass the stop.
Pause affected work if deciding the rule requires shared-method maintenance.

## ACE

- Source: `https://github.com/ace-agent/ace`.
- No worktree/path-prefix, run ID or frozen source boundary was returned.

The coordinator called:

```bash
commonplace-analysis prepare --name ACE
```

Exact returned output:

```text
name must contain lowercase letters, digits and hyphens


Command exited with code 1
```

The uppercase preparation label was a coordinator error, not a demonstrated
source or runtime failure. The coordinator followed the skill's instruction to
stop after preparation failure and did not retry. No analytical workers ran.
Unblock with an operator-authorized fresh preparation using lowercase `ace`;
no source scope change is needed. This batch does not silently retry a stopped
pipeline.

## Disposition and next decision

Both targets remain incomplete. The old nested lookup blocker was not reproduced;
the current blockers replace it in the checklist. Neither run published, so no
auditor was commissioned and no integration was attempted. All worktrees and
traces remain preserved. No method edits, cleanup, push or downstream regeneration
occurred.

Stop this batch for the source-exposure recovery decision and permission to
retry ACE preparation. No next pair was launched while that potentially shared
rule question remains unresolved. No corpus-refresh completion is claimed.
Bookkeeping validation and its commit are performed by the batch coordinator;
they do not validate the unpublished analysis.
