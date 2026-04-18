---
description: Change gate wording without invalidating accepted reviews — update stored accepted reviews, then append gate-migration acceptance events that preserve the accepted note baseline
type: instruction
---

# Migrate semantics-preserving gate changes

Use this instruction only when the gate meaning stays the same. If the gate semantics change, run fresh reviews instead.

## Steps

1. Edit the target gate files.
2. Update the stored accepted review text to match the new gate wording. Keep the canonical stored decision aligned.
3. For each affected current acceptance, append a new acceptance event with:
   - `acceptance_kind = gate-migration`
   - the same `accepted_review_id`
   - the same `accepted_note_sha`
   - the same `accepted_note_commit`
   - the same `model_id`
   - the new `accepted_gate_sha`
4. Do not advance the accepted note baseline during this migration.
5. Verify the affected pairs no longer appear as `gate-changed`.
