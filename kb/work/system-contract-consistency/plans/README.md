# Resolution plans

These are implementation plans and completed outcomes for the ten
contradictions rechecked on 2026-08-19. T1 was refreshed on 2026-08-27 after
the tag semantic contract and grounded search literature supplied a sharper
navigation boundary. These files are workshop state, not new system authority.
Each open plan names the durable contracts, code, tests, or owner workshop that
must absorb its outcome before the finding can close; completed outcomes record
the guard that keeps a closed contradiction from recurring.

| Finding | Recommended resolution | Plan |
|---|---|---|
| I1 | Supersede the unimplemented marker contract and make preserve-only/manual upgrades explicit | [Shipping and upgrade](./i1-shipping-upgrade.md) |
| I2 | Treat the generated install as a tested projection with an explicit dependency policy | [Install projection integrity](./i2-install-projection-integrity.md) |
| V1 | Make `commonplace-validate all` the one recursive, non-fail-fast full-validation path | [Validate all](./v1-validate-all.md) |
| I3 | Scaffold contracts for every routed writable collection and classify `kb/types/` consistently | [Installed topology](./i3-installed-topology.md) |
| S1 | **Resolved 2026-08-23:** make the tracked ingest authoritative for genre and keep local snapshots whole-file immutable | [Completed outcome](./s1-snapshot-mutation-boundary.md) |
| T1 | Define KB-wide semantic membership, resolve it per root and projection, limit marks to membership shortcuts, and give heads canonical `kb/tags/` paths | [Tag scope](./t1-tag-scope.md) |
| E1 | Retain native Windows support and remove or pair every channel-specific promoted procedure | [Windows execution](./e1-windows-execution.md) |
| F1 | **Resolved 2026-08-19:** unsupported generic freshness acceptance was withdrawn until a real non-review target exists | [Completed outcome](./f1-freshness-accept.md) |
| M1 | Complete the three remaining migration-residue packets; text promotion and the snapshot pointer are resolved and guarded | [Migration residue](./m1-migration-residue.md) |
| C1 | **Resolved 2026-08-19:** quote verification is documented and exact console-script/reference parity is enforced | [Completed outcome](./c1-command-catalogue.md) |

## Execution order

1. **Settle installed-product inputs:** I3 defines the collection roles,
   discovery semantics, and machine-readable topology shape; I2 decides the
   shipped bundle and omitted-edge policy. S1's source mutation boundary is
   already settled by ADR 072.
2. **Record and materialize the contract:** I1's successor marks ADR 021
   superseded and records the chosen topology, bundle, and preserve-only upgrade
   semantics. I3 then finishes sources/work templates and library routing with
   ADR 072's resolved source boundary and the I2 inputs.
3. **Close projection and validation:** I2 implements projection closure and
   packaged-product acceptance. V1 exposes one truthful full check without
   losing orphan-type or top-level-landing coverage.
4. **Carry resolved inputs forward:** I3's installed source template projects
   S1's resolved ADR 072 contract. F1 is already closed under C1's
   command-parity guard.
5. **Finish tag and channel owner work:** after I3, I2, and I1 settle the
   installed-product boundary, T1 consumes that boundary and V1's truthful full
   check. Its adopting ADR must reconcile the scope and semantic proposals,
   distinguish exact membership recovery from head traversal and task-level
   search, and avoid claiming untested agent retrieval gains. T1 then precedes
   the areas packet of M1. E1 also consumes V1, remains owned by the
   execution-channel workshop, and must include a native-Windows evidence run.
6. **Sweep representation residue:** run the M1 packets after their governing
   contracts are settled, then retain narrow guards against reintroducing the
   retired executable examples.

The implementation must not hardcode today's collection or command counts.
Tests compare declared/discovered sets with consumed sets so later additions
fail at the boundary that drifted.
