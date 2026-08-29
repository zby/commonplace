# Multistage doctrine-compression pilot

## Decision

Keep the current `cp-skill-write-multistage` bytes. The doctrine-compressed
candidate preserved behavior on the verified Codex path, but it did not reduce
states, branches, handoffs, or exceptions. It also made parent integration and
recovery and the no-nested-delegation rule depend on root-doctrine delivery on
the shared Claude projection, where that delivery remains unverified.

Adding a runtime test and fallback would introduce a new branch solely to
recover controls that the current skill states once. The current skill is the
simpler complete design across its supported canonical projections.

## Compared versions

| Version | Identity | SHA-256 | Size |
|---|---|---|---|
| Current baseline | `git show 0acef622:kb/instructions/cp-skill-write-multistage/SKILL.md` | `ccb0f2ceeb984b41c5ab11706a2160a4ccbdc9ed8bec57e80513ce0f25aef812` | 219 lines, 1,537 words, 11,391 bytes |
| Doctrine-compressed candidate | temporary working-tree candidate | `30b646c2d05bab982a7f2e7b960b4c1fd94ff6c2a59ad0ded380ec253a674792` | 221 lines, 1,549 words, 11,499 bytes |
| Shared promotion reference | live `references/promotion.md` | `6e950a138fe1283b208c3dd0c323410f76093ae9cee8c00fd55a1d3d8065758c` | 94 lines, 566 words, 4,104 bytes |

The candidate changed only the opening delegation account. It called each
commission a delta from Commonplace doctrine, made live mutation and user-owned
decisions explicit, and removed four direct defaults: parent scheduling,
integration, and recovery, plus no nested delegation. All stage, evidence,
digest, repair, review, drift, rollback, and promotion text remained identical.

The canonical directory is projected through both
`.agents/skills/cp-skill-write-multistage` and
`.claude/skills/cp-skill-write-multistage`. The candidate could therefore not
be scoped to the verified Codex path without a new runtime-specific mechanism.

## Scenario results

Two fresh workers compared both versions and recorded event-level traces:

- [Drift, evidence, and repair](./pilot-trace-drift-evidence-repair.md) — an
  edit receives a well-formed review block for missing evidence;
  `cp-skill-ground` adds substantive evidence after incumbent reveal; fresh
  reconstruction and authorship produce changed bytes; a different reviewer
  accepts the new digest; live-target drift then blocks promotion.
- [Unsuitable intermediate route](./pilot-trace-route-adaptation.md) — an
  advisory chronological reconstruction would collapse two causally distinct
  stages, while a dependency ledger or scoped prose can preserve the same
  contribution from the same authorized evidence. A binding-format
  counterfactual tests return of control.

Both versions passed both scenario state machines on verified Codex:

| Required behavior | Current | Candidate on verified Codex |
|---|---|---|
| Source reconstruction remains incumbent-blind | Pass | Pass |
| Substantive evidence invalidates reconstruction and dependent stages | Pass | Pass |
| Post-incumbent evidence causes a fresh reconstructor and fresh author through both reveals | Pass | Pass |
| Changed candidate bytes consume the one repair and receive a different fresh reviewer | Pass | Pass |
| Acceptance binds the exact candidate digest | Pass | Pass |
| Live-target drift without rebase authority stops promotion and retains the run | Pass | Pass |
| Advisory means change while contribution, evidence, isolation, and authority remain fixed | Pass | Pass |
| A binding but unsuitable route returns worker → parent → user | Pass | Pass |

The drift trace had the same 12 control states and ten outbound worker or reveal
handoffs in both versions. The adaptation trace had the same nine control
states and eight ordinary directed handoffs. Neither version added or removed
an operational branch, retry, mutation, digest check, or exception.

## Why the candidate lost

Codex delivered root `AGENTS.md` to both fresh pilot workers. On that verified
path, the candidate could safely inherit parent scheduling, integration, and
recovery and silence-means-no-delegation. Its stage-specific inputs, evidence
boundaries, outputs, acceptance, and return triggers remained explicit.

The same inference is not licensed for Claude Code. Step 0 established the
canonical Claude projection but did not verify binding root-doctrine delivery
to a fresh worker. On that path the candidate left general integration and
recovery ownership implicit and no longer prohibited nested delegation. Stage
clauses still made the intended result plausible, but plausible recovery is not
a binding control path.

The candidate therefore exchanged four explicit defaults for an unverified
consumption-path dependency. It also grew by two lines and twelve words. A
fallback clause would add a delivery-test branch and another packet variant.
The baseline states the four defaults once and leaves all task-specific role
commissions already compressed. There was no repeated generic stage prose left
to remove safely.

The temporary candidate was reverted. The live skill again has the exact
baseline SHA-256 shown above.

## Checks

- `commonplace-validate` passed for the temporary candidate and both trace
  artifacts.
- The promoted-skill scaffold projection test passed all 18 cases against the
  temporary candidate.
- The generic skill-creator validator rejected the existing Commonplace-only
  frontmatter keys `argument-hint`, `context`, `type`, and `user-invocable`.
  This is the pre-existing validator-compatibility boundary recorded by the
  earlier refinement, not a candidate defect.
- After rejection, the live skill matched commit `0acef622` byte for byte.

No skill cachebuster, reinstall, or lineage update is needed because no live
skill bytes changed.
