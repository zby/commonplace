# Workshop: write-brief sidecars

## Goal

Implement the operator's adoption, on 2026-09-26, of Option 3 of the [per-artifact write-brief proposal](../../reference/proposals/per-artifact-write-briefs.md): optional durable write briefs, delivered to writers by a validated pointer (Route A).

The operator fixed three choices:

- **Placement:** a brief is a sidecar `<slug>.brief.md` next to the document it commissions.
- **Authority:** an agent may write a brief when the write is commissioned. It binds later writers as intent until a user amends it, and current user direction always prevails.
- **Freshness:** editing a brief affects the next write of its target only. There are no review or freshness consequences.

Evidence: [full write briefs cut edit drift; one-line briefs did not](../../notes/evidence/full-write-briefs-cut-edit-drift-one-line-briefs-did-not.md).

## What closes this workshop

1. The ADR is accepted, and every consumer class in [change-packet.md](./change-packet.md) is marked done.
2. The acceptance probe passes from a fresh temporary project, and `uv run pytest` passes.
3. The rescan for the old form has been run and recorded in the packet.
4. The proposal is archived as adopted, via [retire an artifact](../../instructions/retire-artifact.md).

Then delete the workshop.

## Bookkeeping

- `change-packet.md` — the consumer inventory required by [change a contract that several consumers read](../../instructions/change-a-contract-that-several-consumers-read.md).
- The ADR is drafted directly in `kb/reference/adr/`.
