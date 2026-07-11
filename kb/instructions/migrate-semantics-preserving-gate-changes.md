---
description: Carry current gate verdicts across a wording-only criterion edit without treating the edit as a fresh review
type: kb/types/instruction.md
---

# Migrate semantics-preserving gate changes

Use this instruction only when a verdict gate's wording changes without changing the judgment it asks for. If its meaning, scope, severity, exceptions, or output contract changes, run fresh assays instead.

Acknowledgement reuses completed evidence and upserts the current snapshot baseline; it does not append an event or rewrite the stored result. Because ack snapshots both sides, every affected note must still match its accepted note snapshot. If a note also changed, rerun that pair rather than silently accepting both changes together.

## Steps

1. Before editing, run the selector for the intended note scope under every affected model partition. Only migrate pairs that are currently fresh; resolve or rerun any pair already reported as `note-changed`, `criterion-changed`, or `missing-review`. A fresh pre-edit pair proves that both current files match its accepted snapshots.
2. Edit the gate file. Keep the criterion semantically equivalent; prose cleanup alone is not evidence that a behavioral change is harmless.
3. Select the affected pairs under each model partition and confirm they are stale only because the criterion changed:

   ```bash
   commonplace-review-target-selector {gate-id} --model-partition {model-partition} --note {note-paths...} --reason criterion-changed --json
   ```

4. Acknowledge each verified pair. This preserves its completed verdict evidence while replacing the one current acceptance row with snapshots of the unchanged note and edited criterion:

   ```bash
   commonplace-ack-review {note-path} --model-partition {model-partition} {gate-id}
   ```

5. Rerun the same selector without `--reason`. An empty `targets` list means the migrated pairs are fresh. Inspect the accepted result rather than claiming that acknowledgement produced a new decision.
