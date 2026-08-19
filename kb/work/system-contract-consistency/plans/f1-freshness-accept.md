# F1 plan — Remove generic freshness accept until it has a consumer

**State:** open. `V1_ACCEPT_TARGET_KINDS` remains empty, so the published command
rejects `review-pair` and every other target kind.

## Resolution selected

Delete the placeholder command and unreachable transition. Do not implement a
non-review target merely to justify already-exposed scaffolding. Future generic
acceptance returns with the first real non-review target and an end-to-end
proposal, schema, transition, and test.

## Work

1. Remove `commonplace-freshness-accept` from `[project.scripts]` and delete
   `src/commonplace/cli/freshness_accept.py`.
2. Delete `V1_ACCEPT_TARGET_KINDS` and `accept_target_observations()` from
   `transitions.py`, then remove imports used only by that path. Keep
   `InputObservation`, `parse_input_observation`, and `parse_target_key`, which
   are used by ack and retire.
3. Delete the two rejection-only accept tests; they currently preserve the
   disabled state rather than a capability.
4. Remove current-facing accept material from `commands.md`,
   `freshness-architecture.md`, `freshness-schemas.md`, `lib-modules.md`, and
   `README-REVIEW-SYSTEM.md`. Correct the package map, transition table, command
   list, schema examples, review-system boundary, and accept-only claims about
   stored content.
5. Write a successor or refinement for accepted ADR 052. Preserve its general
   store and review-first migration decisions, but explicitly retract the claim
   that a generic accept transition currently ships; link ADR 052 to that
   refinement so an accepted decision does not remain a live contrary witness.
6. Leave collection freshness and other non-review targets in their existing
   proposals. Update both the freshness-module and
   `artifact-freshness-and-referential-checks` workshops: current-looking claims
   that generic accept ships become dated historical evidence, and the live
   finding is marked resolved only after removal.
7. Remove the entry point and its command-reference section in the same F1
   change. C1's completed parity test fails if only one side changes. Because
   package metadata changes, reinstall the editable uv tool after tests.

## Completion

No package, live code path, current reference, or help surface exposes
`commonplace-freshness-accept`. Remaining mentions are dated historical evidence
or future proposals that do not claim an executable exists, and ADR 052 no
longer presents the withdrawn command as accepted current behavior.
