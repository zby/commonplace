# Tag-contract convergence plans

These plans stage one invariant as separately reviewable changes. They are
workshop state, not adopted system authority.

| Phase | Outcome | Dependency |
|---|---|---|
| 0 | **Complete:** [activation boundary, decisions, inventory, and fixture](./00-readiness.md), rebaselined 2026-09-25 for ADR 086 | Current workshop and implementation audit |
| 1 | [Dormant semantic foundation and exact resolver](./01-semantic-resolver.md) | None; ready |
| 2 | [Finding trial: does any tag page help find things?](./02-finding-trial.md) | Phase 1; decides the scope of Phases 3–4 |
| 3 | [Consumer convergence and contract activation](./03-consumer-convergence.md) | Phases 1–2 |
| 4 | [Canonical heads and host migration](./04-canonical-heads-migration.md) | Phases 1–3 |
| 5 | [Metadata cleanup](./05-cleanup-and-follow-up.md) | Independent |

Phase 1 may land alone only because it changes no operative contract or
consumer. Phase 2 tests usefulness before any contract work: if no tag page
beats plain description search, Phases 3–4 shrink or close. Phase 3 activates
the accepted contract once and closes the original scope contradiction in
behavior. Phase 4 completes the chosen canonical representation and breaking
migration. Phase 5 must not be folded into another change merely because it
also touches tags.
