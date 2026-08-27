# Tag-contract convergence plans

These plans stage one invariant as separately reviewable changes. They are
workshop state, not adopted system authority.

| Phase | Outcome | Dependency |
|---|---|---|
| 0 | **Complete:** [activation boundary, decisions, inventory, and fixture](./00-readiness.md) | Current workshop and implementation audit |
| 1 | [Dormant semantic foundation and exact resolver](./01-semantic-resolver.md) | Minimal I3 `kb-root` model |
| 2 | [Consumer convergence and contract activation](./02-consumer-convergence.md) | Phase 1; V1 for full product coverage |
| 3 | [Canonical heads and migration](./03-canonical-heads-migration.md) | Phases 1–2; I1/I2 for installed migration |
| 4 | [Cleanup and empirical follow-up](./04-cleanup-and-follow-up.md) | Cleanup can be reviewed independently; experiment follows resolver and heads |

Phase 1 may land alone only because it changes no operative contract or
consumer. Phase 2 activates the accepted contract once and closes the original
scope contradiction in behavior. Phase 3 completes the chosen canonical
representation and breaking migration. Phase 4 must not be folded into either
change merely because it also touches tags.
