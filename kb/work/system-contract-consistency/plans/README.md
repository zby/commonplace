# Resolution plans

Plans for findings that need more than a one-line disposition. The workshop
[README](../README.md) is the finding index and states the implementation
order; findings without a plan here are local fixes whose authority the README
names. These files are workshop state, not system authority.

| Plan | State |
|---|---|
| [T1 tag-scope closure tracker](./t1-tag-scope.md) | Transferred to tag-contract convergence; closes here after its adoption tests |
| [E1 Windows execution](./e1-windows-execution.md) | Owned by execution-channel compatibility; now also owns `commonplace-validate all` |
| [Contract-change gate](./contract-change-gate.md) | Required before closure; first application is ADR 086, retrospectively |

Plans for I1, I2, I3, V1, M1, C1, F1 and S1 were deleted on 2026-09-25 after
those findings closed; git history keeps them.

Implementation must not hardcode today's collection or command counts. Tests
compare declared or discovered sets with consumed sets so later additions fail
at the boundary that drifted.
