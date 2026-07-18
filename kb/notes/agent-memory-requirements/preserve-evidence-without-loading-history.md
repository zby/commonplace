---
description: "Trace retention should preserve evidence for audit and extraction without making raw history the agent's default context"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
---

# Preserve Evidence Without Making History The Next Context

A memory system needs a capture substrate that keeps enough source material for later extraction, audit, debugging, and rework of adapted artifacts. But capture is not loading: the point is to preserve evidence without making history the acting agent's next context. Broad trace retention is useful because the future consumer is often unknown at capture time, while ordinary execution should still load only the material that earns its context budget.

Text-heavy traces are often cheap to retain: prompts, model outputs, tool calls, file diffs, command output, and small structured artifacts. Large media, datasets, telemetry firehoses, regulated material, and multi-user streams change the calculation. Payload form and volume control per-session storage cost; user scope and behavioral authority control aggregate cost and governance.

[Session history should not be the default next context](../session-history-should-not-be-the-default-next-context.md) because persistence and loading are separate decisions. Store-everything is only a capture posture. Raw traces should usually remain outside the acting agent's ordinary context, loading only for provenance checks, dispute resolution, debugging, rework, or evaluation.

## Session Lifecycle

Session lifecycle is part of this requirement, not just an implementation detail. A realistic system needs a boundary where live work becomes durable evidence: commit, checkpoint, archive, retry, or abandon. [OpenViking](../../agent-memory-systems/reviews/openviking.md) is the strongest reviewed example: `commit_async` snapshots a live session, archives it, records a task, and runs extraction in the background. [WUPHF](../../agent-memory-systems/reviews/wuphf.md) makes the same pressure visible from the other side by treating fresh sessions as the runtime default and rebuilding continuity through broker-selected memory.

## Methods

- Complete session traces with tool calls, timestamps, outputs, errors, and final artifacts.
- Structured event logs that capture actions, decisions, errors, approvals, and produced artifacts without preserving every token.
- Session checkpoints, commit records, retry handles, and archive directories that let follow-up work resume, audit, or rework artifacts from a bounded run.
- Artifact provenance records that link durable notes, policies, decisions, tests, scripts, or plugins back to the sessions and sources that produced them.
- Redacted trace stores where secret scrubbing and retention policy run before extraction or model inspection.
- Selective capture in high-risk domains where privacy, legal retention, media payloads, or data volume make broad logging unacceptable.

## Evaluation Questions

- Does the system separate capture from activation?
- Can retained evidence support audit, debugging, and later extraction?
- Are payload form, privacy, user scope, and behavioral authority handled before broad retention becomes the default?
- Can a failed or interrupted session be resumed, retried, or inspected?

---

Relevant Notes:

- [Session history should not be the default next context](../session-history-should-not-be-the-default-next-context.md) - grounds the capture/loading split
- [A functioning KB needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - frames work state as a separate lifecycle layer
