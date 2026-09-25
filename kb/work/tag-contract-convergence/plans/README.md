# Tag-contract convergence plans

These plans stage one invariant as separately reviewable changes. They are
workshop state, not adopted system authority.

| Phase | Outcome | Dependency |
|---|---|---|
| 0 | **Complete:** [activation boundary, decisions, inventory, and fixture](./00-readiness.md), rebaselined 2026-09-25 for ADR 086 | Current workshop and implementation audit |
| 1 | [Dormant semantic foundation and exact resolver](./01-semantic-resolver.md) | None; ready |
| 2 | [Consumer convergence and contract activation](./03-consumer-convergence.md) | Phase 1 |
| 3 | [Canonical heads and host migration](./04-canonical-heads-migration.md) | Phases 1–2 |
| 4 | [Cleanup, navigation trial, and Gwern-style browsing trial](./05-cleanup-and-follow-up.md) | Cleanup can be reviewed independently; trials follow resolver and heads |

Phase 1 may land alone only because it changes no operative contract or
consumer. Phase 2 activates the accepted contract once and closes the original
scope contradiction in behavior. Phase 3 completes the chosen canonical
representation and breaking migration. Phase 4 must not be folded into either
change merely because it also touches tags.
