# Failure prevention follow-ups

**Historical discussion list.** The [successor's triage](../agentic-system-completion/method-follow-ups.md) records current dispositions as of 2026-10-19. In particular, the local-negative rule below has been superseded, generic verification questions and publication naming have shipped, and the new headless engine changes path delivery and attempt evidence. Read the triage before commissioning follow-up work; the original observations and decisions below remain historical.

## Purpose and decisions

Retain the operational review requested on 2026-10-15: which observed rerun
errors could be eliminated or made less likely. This is a bounded review of
workshop records and selected current implementations, not a new audit of every
run. It authorizes no implementation, old-run recovery, launch or method change.
Numbering preserves the conversational list so later discussion can refer to it.

The operator corrected two priorities:

- Pi retries have already been increased. Evaluate that mitigation before
  recommending more retry layers.
- Disk exhaustion was a one-time incident. Defer additional capacity safeguards
  until more batch processing is planned; this rerun is expected to finish soon.

The next discussion is item 3, removing path transcription. No design has been
selected. Frozen methods and worktrees must not be patched to apply follow-ups.

## 1. Provider failures: existing mitigation, measure before adding retries

The [fresh-start selection](./retry-selection-2026-10-15.md) identifies 31
provider/transport cases among 39 candidates. This selected historical inventory
is not a current failure rate or proof that current retry handling is inadequate.

Commit `59c29bc261fafe00caf2313d4b986aa4ba3ef4de`, dated 2026-10-14,
“Classify subagent failures from the final assistant response,” fixes stale
failure metadata after Pi recovers inside one worker process. Intermediate errors
remain in returned messages; the latest assistant response and process outcome
control classification. Blocking and asynchronous regression tests cover recovery
and terminal failure after recovery.

At inspection, user-level `/home/zby/.pi/agent/settings.json` had retries enabled,
`maxRetries: 8`, `baseDelayMs: 5000`, and `maxAgentDelayMs: 60000`. That file is
outside repository history; the commit does not date the retry-count increase.
The operator reports the increase was recent. Improvement in the observed failure
rate was not measured in this review.

The [driver](../../agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md)
also permits explicitly authorized bounded worker relaunches. Adding those on top
of Pi retries can multiply request attempts and waiting time. Do not prioritize
another layer without post-mitigation evidence. Coordinator failures, semantic
refusals, invalid outputs and uncertain effects need their separate handling.

## 2. Disk capacity: deferred until more batch processing

Six selected runs were interrupted by disk exhaustion. The
[disk incident](./disk-recovery-batches.md) and later external worktree placement
retain the mitigations. Future batch processing should consider free-space and
inode checks, monitoring and an admission reserve on both filesystems, based on
measured growth. Do not delete failed evidence automatically.

Operator decision: not a change for the nearly finished current rerun. Revisit
when planning another substantial batch.

## 3. Remove manual path transcription

The latest o-o run stopped when its coordinator omitted a hyphen in a supplied
prompt path; see [the exact-run selection](./retry-selection-2026-10-15.md).
Earlier workers reconstructed validation paths incorrectly. The
[validation-path investigation](./validation-path-maintenance.md) established
correct absolute producer paths and literal validation commands, not a producer
bug. Current instructions already require exact use.

Candidate improvements for discussion:

- Preserve harness-independent orchestration: the step program writes the complete
  worker invocation and prints its absolute path; the orchestrator launches workers.
  A code-owned agent launcher was proposed and rejected in discussion.
- The driver already supplies a fixed short wrapper into which the orchestrator
  inserts the printed path. Printing the wrapper with that path already inserted
  would remove one substitution, not add a missing substantive handoff.
- Current worker invocations already supply literal validation commands. The
  investigation established correct delivery, not a missing producer interface.

Coordinator launch and worker validation are different failure points. Current
handoff generation already performs most of the proposed work; residual model
transcription error does not by itself justify another interface. No implementation
was selected. Preserve fresh-context isolation, worker-profile binding, round
barriers, result reporting and acceptance checks.

## 4. Explain the local-negative profile case

Secure LLM Wiki stopped over a profile/validator interpretation conflict; see
[its deferred outcome](./retry-selection-2026-10-15.md). Current validation can
retain a local trace-learning “no” alongside an unresolved alternative under an
overall `uninspected` or `not-determinable` assessment. It intentionally rejects
`partial` without a positive finding. Do not invent a positive or drop an opaque
branch to pass validation.

Proposed follow-up: a worked example and clearer diagnostic before considering
validator changes. Existing regression tests confirm representation of this case:

```text
uv run pytest -q tests/commonplace/comparison/test_systems_matrix.py::test_revision2_partial_axis_cannot_promote_only_local_negatives tests/commonplace/comparison/test_systems_matrix.py::test_revision2_local_negative_survives_unresolved_axis_without_system_no
3 passed in 0.19s
```

This checks the current representation, not the failed run's substantive findings
or clearance of its hold.

## 5. Verify conditions, fallback paths and policy strength

Several audit holds involve loss of a condition or strengthening of a claim:

- [ContextPilot](./audits/bash-current-contextpilot.md): omitted route selector
  and generic fallback.
- [OpenRSI](./audits/unintegrated/AAS-2026-10-14-openrsi-c72dec9967a3-01.md):
  omitted private-answer read access despite a read-only mount; no actual leakage
  established.
- [Agent Skills](./audits/unintegrated/AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01.md):
  a preference became an unconditional prohibition.

Proposed follow-up: generic source-first verification questions about activation,
fallbacks, bypasses, preference versus enforcement, and preservation of necessary
qualifications in public synthesis. Do not forward historical findings to fresh
analysts as evidence. These are prevention proposals, not authorization to repair
held publications.

## 6. Enforce worker write scope where practical

Dense-mem wrote unauthorized identity metadata; the
[failed-batch record](./failed-batch-reruns.md) preserves the unresolved incident.
The [LLM Context Base audit](./audits/unintegrated/AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01.md)
confirms an unauthorized sibling placeholder write and removal, without established
accepted-byte impact.

Proposed follow-up: evaluate enforced allowed-write locations. Restricting only
`write` and `edit` is insufficient while Bash can write elsewhere. Before/after
mutation checks are detection, not containment, and can miss write-then-delete
activity. No containment design is selected.

## 7. Retain attempt-indexed worker traces

Repeated audits could verify publication bytes but could not recover worker
execution evidence. The current launcher uses non-persisted child sessions and
returns child messages through parent tool details.

Proposed follow-up: persist per-attempt event logs and terminal results separately
from the coordinator's final response, with concise in-context summaries. This
would reduce audit and coordinator-failure costs; it would not itself prevent
provider errors. Retention, storage growth and access boundaries need design.

## 8. Complete the deferred publication namespace change

Four different-owner wiki sources collide with an existing publication slug.
The [workshop README](./README.md#publication-namespace-follow-up-after-all-runs-finish)
retains the operator's plan: migrate GitHub publications to `owner--project`
after all analyses finish, including affected links and validators. Keep run IDs
immutable. Different log keys do not resolve publication collisions. No migration
or rerun is authorized by this list.

## Limits

No complete post-mitigation failure-rate comparison was performed. Prompt-cache
expiry, provider pressure and context exhaustion remain unestablished causes of
the stream failures. Existing holds, reservations and independently owned edits
remain untouched. This record saves proposals and operator decisions; it is not
an implementation plan or new acceptance gate.
