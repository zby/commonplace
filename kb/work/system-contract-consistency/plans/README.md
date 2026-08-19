# Resolution plans

These are implementation plans and completed outcomes for the ten
contradictions rechecked on 2026-08-19. They are workshop state, not new system
authority. Each open plan names the durable contracts, code, tests, or owner
workshop that must absorb its outcome before the finding can close; completed
outcomes record the guard that keeps a closed contradiction from recurring.

| Finding | Recommended resolution | Plan |
|---|---|---|
| I1 | Supersede the unimplemented marker contract and make preserve-only/manual upgrades explicit | [Shipping and upgrade](./i1-shipping-upgrade.md) |
| I2 | Treat the generated install as a tested projection with an explicit dependency policy | [Install projection integrity](./i2-install-projection-integrity.md) |
| V1 | Make `commonplace-validate all` the one recursive, non-fail-fast full-validation path | [Validate all](./v1-validate-all.md) |
| I3 | Scaffold contracts for every routed writable collection and classify `kb/types/` consistently | [Installed topology](./i3-installed-topology.md) |
| S1 | Define captured-content immutability with `genre` as the sole ingest-time correction | [Snapshot mutation boundary](./s1-snapshot-mutation-boundary.md) |
| T1 | Adopt collection-scoped tag membership claims and bound tag-link routing to that scope | [Tag scope](./t1-tag-scope.md) |
| E1 | Retain native Windows support and remove or pair every channel-specific promoted procedure | [Windows execution](./e1-windows-execution.md) |
| F1 | **Resolved 2026-08-19:** unsupported generic freshness acceptance was withdrawn until a real non-review target exists | [Completed outcome](./f1-freshness-accept.md) |
| M1 | Complete the four remaining migration-residue packets; text promotion is resolved and guarded | [Migration residue](./m1-migration-residue.md) |
| C1 | **Resolved 2026-08-19:** quote verification is documented and exact console-script/reference parity is enforced | [Completed outcome](./c1-command-catalogue.md) |

## Execution order

1. **Settle installed-product inputs:** I3 defines the collection roles,
   discovery semantics, and machine-readable topology shape; S1 settles the
   sources mutation boundary; I2 decides the shipped bundle and omitted-edge
   policy.
2. **Record and materialize the contract:** I1's successor marks ADR 021
   superseded and records the chosen topology, bundle, and preserve-only upgrade
   semantics. I3 then finishes sources/work templates and library routing with
   the S1 and I2 inputs.
3. **Close projection and validation:** I2 implements projection closure and
   packaged-product acceptance. V1 exposes one truthful full check without
   losing orphan-type or top-level-landing coverage.
4. **Remove independent contradictions:** S1 and the I3 source template close
   together even if their edits are prepared separately. F1 is already closed
   under C1's command-parity guard.
5. **Finish scoped owner work:** T1 precedes the areas packet of M1. V1 supplies
   the shell-neutral validation path needed by E1. E1 remains owned by the
   execution-channel workshop and must include a native-Windows evidence run.
6. **Sweep representation residue:** run the M1 packets after their governing
   contracts are settled, then retain narrow guards against reintroducing the
   retired executable examples.

The implementation must not hardcode today's collection or command counts.
Tests compare declared/discovered sets with consumed sets so later additions
fail at the boundary that drifted.
