# Review and editing commands

Posed by the operator on 2026-11-19. Redesign the commands around the full editorial pass, the main operation for improving a note. Use **Review and editing** as the operator-facing name. “Revision system” suggested version control on first reading.

The full pass can review a note, select edits from the findings, and publish the edited text. The operator can commission that work without choosing each edit. Some runs stop for a decision. Describe autonomy through what the system can decide and where the operator takes over. The [current operating guide](../../reference/README-REVIEW-SYSTEM.md#improvement-procedures) describes the procedures and their publication rules.

**State on 2026-11-19:** the operator adopted the [command proposal](./command-proposal.md) as the starting design. It holds the command map, the worked example and the migration decision. Not implemented. What remains is the parser change with its callers, a new ADR, and the system's rename to **Review and editing system** in the operating guide.

## Interface to test

The starting proposal is `commonplace-revise NOTE` for the full pass and `commonplace-review NOTE --criteria prose` for findings alone. Test whether a first-time operator can predict which invocation may change the note. An existing findings-only invocation must never silently gain authority to edit.

Trace one full run through a stop. Show what the system already did, the decision left to the operator, and the exact command that gives effect to that decision. Use the example to settle the follow-up verbs. Today `record RUN` prepares pending answers, while `answers record FILE` saves decisions already made. Applying approved edits is a third action. The [command reference](../../reference/commands.md) gives the current contracts.

## Closure

Close when the operator agrees on a current-to-proposed command map, a worked example from full pass through continuation, and a migration decision for existing callers and commands embedded in saved continuation records. Record which invocations write the note, write findings or decisions, or hold a candidate for publication. Coordinate proposed CLI changes with the [review workflow workshop](../review-on-workjig/README.md) before implementation.
