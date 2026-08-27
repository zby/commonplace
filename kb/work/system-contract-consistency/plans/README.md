# Resolution plans

These are implementation plans and completed outcomes for the ten
contradictions rechecked at commit `6660bd2a` on 2026-08-27. The generated
[witness ledger](../baseline-2026-08-27.md) classifies changed and stale
witnesses. These files are workshop state, not new system authority.
Each open plan names the durable contracts, code, tests, or owner workshop that
must absorb its outcome before the finding can close; completed outcomes record
the guard that keeps a closed contradiction from recurring.

I1, I2, I3, and V1 are separate implementation packets within one
installed-product architecture program: topology, projection, upgrade, and
whole-product validation must share one model without becoming one correlated
patch.

| Finding | Recommended resolution | Plan |
|---|---|---|
| I1 | Supersede the unimplemented marker contract with ownership-aware upgrades; preserve-only is at most an explicit interim limit | [Shipping and upgrade](./i1-shipping-upgrade.md) |
| I2 | Compile and test the selected hybrid evidence-local edition with explicit dependency dispositions | [Install projection integrity](./i2-install-projection-integrity.md) |
| V1 | Make `commonplace-validate all` the one recursive, non-fail-fast full-validation path | [Validate all](./v1-validate-all.md) |
| I3 | Add explicit, pairwise-disjoint `kb-root`s, root-local types, complete user scaffolds, and contract-based collection discovery | [Installed topology](./i3-installed-topology.md) |
| S1 | **Resolved 2026-08-23:** make the tracked ingest authoritative for genre and keep local snapshots whole-file immutable | [Completed outcome](./s1-snapshot-mutation-boundary.md) |
| T1 | **Transferred:** retain the contradiction and close it only after the dedicated tag workshop proves consumer convergence | [Owner handoff](./t1-tag-scope.md) |
| E1 | Retain native Windows support and implement the manifest-derived portability dispositions | [Windows execution](./e1-windows-execution.md) |
| F1 | **Resolved 2026-08-19:** unsupported generic freshness acceptance was withdrawn until a real non-review target exists | [Completed outcome](./f1-freshness-accept.md) |
| M1 | Complete Areas/Topics after tag adoption; the other four migration packets are resolved and guarded | [Migration residue](./m1-migration-residue.md) |
| C1 | **Resolved 2026-08-19:** quote verification is documented and exact console-script/reference parity is enforced | [Completed outcome](./c1-command-catalogue.md) |

Workshop-wide outcome: promote the [contract-change implementation
gate](./contract-change-gate.md) before closure.

## Execution order

1. **Rebaseline — complete for this cycle:** use the named-commit ledger, not
   inherited prose counts.
2. **Workshop architecture — complete:** the
   [decision packet](../installed-product-edition-decision.md) selects one
   hybrid evidence-local edition, disjoint host and Commonplace `kb-root`s,
   root-local types, five scoped ownership values, one projection compiler,
   and hash-aware upgrades. The [impact
   ledger](../disjoint-root-impact-ledger.md), [ADR
   draft](../successor-installation-adr-draft.md), and [implementation
   packets](../disjoint-root-implementation-packets.md) make the choice
   reviewable without activating it.
3. **Implement the dormant I3 foundation plus V1:** add explicit root objects,
   overlap rejection, root-local path/type resolution, contract-based
   collection discovery, and a structured recursive suite before projection
   cleanup.
4. **Implement I2:** one compiler-like projection for wheel and editable-source
   modes, accepted by V1 over a pristine initialized artifact.
5. **Activate fresh installs, then finish I1:** route the compiled Commonplace
   root to `commonplace-library/kb/`, update generated surfaces, then migrate
   legacy `kb/commonplace/` through ownership-aware reconciliation. Label
   preserve-only explicitly if it ships as an interim limit.
6. **Continue E1; independent M1 packets are complete:** use the
   [manifest-derived E1 audit](../../execution-channel-compatibility/e1-promoted-skill-rebaseline-2026-08-27.md)
   to implement portability. Global status and path-valued types were resolved
   and guarded on 2026-08-27.
7. **Consume the tag owner:** let `tag-contract-convergence` implement its
   staged program, then recheck T1 here. Areas/Topics waits for that outcome.
8. **Promote the contract-change gate, record outcomes, and close.**

The implementation must not hardcode today's collection or command counts.
Tests compare declared/discovered sets with consumed sets so later additions
fail at the boundary that drifted.
