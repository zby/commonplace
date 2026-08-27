# F1 outcome — Generic freshness accept is withdrawn until it has a consumer

**State:** resolved 2026-08-19.

## Resolution

The placeholder command and unreachable transition were deleted. [ADR
065](../../../reference/adr/065-publish-only-supported-freshness-transitions.md)
amends ADR 052 and permits generic initial acceptance to return only with the
first adopted non-review target and its end-to-end identity, input, producer,
operator, and test contracts.

## Implemented

1. Removed `commonplace-freshness-accept` from `[project.scripts]` and deleted
   `src/commonplace/cli/freshness_accept.py`.
2. Deleted `V1_ACCEPT_TARGET_KINDS` and `accept_target_observations()` from
   `transitions.py`, and removed imports used only by that path. Kept
   `InputObservation`, `parse_input_observation`, and `parse_target_key`, which
   are used by ack and retire.
3. Deleted the two rejection-only tests that preserved the disabled state
   rather than testing a capability.
4. Removed current-facing accept material from `commands.md`,
   `freshness-architecture.md`, `freshness-schemas.md`, `lib-modules.md`, and
   `README-REVIEW-SYSTEM.md`. The package map, transition table, command list,
   schema examples, review-system boundary, and stored-content claims now
   describe status, acknowledgement, retirement, and review-owned capture.
5. Added ADR 065 and linked it from ADR 052. The general store and review-first
   migration remain accepted; the generic accept clause no longer remains a
   contrary accepted witness.
6. Left collection freshness and other non-review targets in proposals. Updated
   both the freshness-module and
   `artifact-freshness-and-referential-checks` workshops: current-looking claims
   that generic accept shipped are now dated historical evidence, while the
   active proposal makes registration a future adoption choice.
7. Removed the entry point and command-reference section in the same change.
   C1's exact parity guard remained equal; the 2026-08-27 baseline observes 22
   names on each side after later paired additions.

## Verification

- The focused freshness-transition and command-catalogue tests pass (9 tests).
- Exact command/reference parity was 21 to 21 at closure and is 22 to 22 at the
  2026-08-27 baseline; the test hardcodes neither count.
- The complete suite passes (489 tests), as do deterministic validation of all
  21 changed Markdown artifacts and the focused Ruff check. The Ruff run
  excludes three pre-existing `TRY004` findings in retained parser code.
- Reinstalling the editable uv tool produced 21 launchers. The deleted accept
  launcher is absent and the retained status launcher runs.
- The shared [workshop index](../../README.md) is corrected in the 2026-08-27
  rebaseline so it no longer presents generic acceptance as live.

## Completion

No package, live code path, current reference, help surface, or active-workshop
summary exposes `commonplace-freshness-accept` as current. ADR 052 no longer
presents the withdrawn command as accepted behavior. Remaining substantive
mentions are dated historical evidence or completed outcomes.
