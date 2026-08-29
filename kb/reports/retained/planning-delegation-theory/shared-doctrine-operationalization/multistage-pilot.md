# Multistage doctrine-compression pilot

## Decision

Adopt the lean candidate at SHA-256
`9e6893a96d3731edd092c5f9276b9acd7e8b7b4e69cf7dc251b177456dc6c6ba`.
It removes duplicated generic delegation rules while retaining the exact role
ownership, evidence, review, repair, drift, recovery, and mutation controls
that determine workflow behavior. It is one line, 16 words, and 117 bytes
smaller than the tested baseline. It adds no state, branch, handoff, exception,
or runtime fallback.

The first candidate remains rejected. It added doctrine-delta framing, grew by
two lines and twelve words, and did not reduce operational complexity. The lean
candidate makes only the omission that the verified doctrine paths license.

## Compared versions

| Version | Identity | SHA-256 | Size |
|---|---|---|---|
| Tested baseline | `git show 44ab1fbe:kb/instructions/cp-skill-write-multistage/SKILL.md` | `ccb0f2ceeb984b41c5ab11706a2160a4ccbdc9ed8bec57e80513ce0f25aef812` | 219 lines, 1,537 words, 11,391 bytes |
| Rejected first candidate | temporary working-tree candidate | `30b646c2d05bab982a7f2e7b960b4c1fd94ff6c2a59ad0ded380ec253a674792` | 221 lines, 1,549 words, 11,499 bytes |
| Adopted lean candidate | live `kb/instructions/cp-skill-write-multistage/SKILL.md` | `9e6893a96d3731edd092c5f9276b9acd7e8b7b4e69cf7dc251b177456dc6c6ba` | 218 lines, 1,521 words, 11,274 bytes |
| Shared promotion reference | live `references/promotion.md` | `6e950a138fe1283b208c3dd0c323410f76093ae9cee8c00fd55a1d3d8065758c` | 94 lines, 566 words, 4,104 bytes |

The lean candidate changes only the opening delegation account. The tail from
`## 1. Commission one artifact` is byte-identical to the baseline. It removes
three parent duties — scheduling workers, integrating returns, and handling
recovery — and the generic sentence that workers write only their run artifacts
and do not delegate. It retains parent ownership of the commission, authority
boundary, privileged context, and every live mutation.

## Control carriers

| Removed generic control | Carrier used by the lean candidate |
|---|---|
| Parent scheduling and integration | Root `AGENTS.md`/`CLAUDE.md`: the parent retains scheduling and integration. Every stage still addresses its launch, verification, and integration steps to the parent. |
| Parent recovery | The same root rule, plus `references/promotion.md`: the parent executes every mutation and recovery step. |
| No unauthorized nested delegation | Root `AGENTS.md`/`CLAUDE.md`: nested delegation requires explicit authorization and silence means no. |
| Worker write scope | The retained role clauses are stricter: the reconstructor owns only `reconstruction.md`; the author owns only `claim-disposition.md` and `candidate.md`; the reviewer writes one immutable review and edits nothing. |

Codex fresh workers receive root `AGENTS.md` as binding repository instruction.
Two direct Claude Code 2.1.251 probes established the same delivery through
automatically loaded `CLAUDE.md` → `AGENTS.md` for native non-fork
`general-purpose` workers. See [Claude native-worker doctrine
delivery](./claude-native-worker-doctrine-delivery.md). The scaffold template
also carries the same rules for consuming projects. A different runtime may
omit a root rule only after its own delivery path is verified; otherwise the
parent must state the rule in the worker packet.

The test criterion asked workers to trace every removed generic control to
root doctrine. Its purpose was to reject a control with no delivered carrier.
The write-scope half is not stated as a root assignment, but it does not need
inheritance: the candidate retains more specific role-level carriers. This
satisfies the criterion's purpose. Requiring the weaker generic sentence to
come from root as well would reward duplicate wording rather than preserve a
control.

## Scenario results

The original Codex traces compared the baseline with the rejected first
candidate:

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

Their state-machine findings remain valid because the lean candidate has the
same sections 1–6. Their overall rejection depended on the then-unverified
Claude delivery path and is superseded by the direct probe.

The lean comparison then used four fresh evaluators: one Codex and one native
Claude worker per scenario. The two Claude workers were blinded with neutral
version names and opposite version ordering. All four independently found no
behavioral or authority divergence and recommended the lean candidate.

| Required behavior | Baseline | Lean candidate on Codex | Lean candidate on native Claude |
|---|---|---|---|
| Source reconstruction remains incumbent-blind | Pass | Pass | Pass |
| Substantive evidence invalidates reconstruction and dependent stages | Pass | Pass | Pass |
| Post-incumbent evidence causes a fresh reconstructor and fresh author through both reveals | Pass | Pass | Pass |
| Changed candidate bytes consume the one repair and receive a different fresh reviewer | Pass | Pass | Pass |
| Acceptance binds the exact candidate digest | Pass | Pass | Pass |
| Live-target drift without rebase authority stops promotion and retains the run | Pass | Pass | Pass |
| Advisory means change while contribution, evidence, isolation, and authority remain fixed | Pass | Pass | Pass |
| A binding but unsuitable route returns worker → parent → user | Pass | Pass | Pass |
| Role write scope and no unauthorized nested delegation remain binding | Pass | Pass | Pass |

The drift trace had the same 12 control states and ten outbound worker or reveal
handoffs in both versions. The adaptation trace had the same nine control
states and eight ordinary directed handoffs. Neither version added or removed
an operational branch, retry, mutation, digest check, or exception.

The baseline's worker-side no-delegation sentence was itself conditional on the
same delivery path: workers do not receive the skill body. A worker learned the
rule from ambient doctrine or from its task packet under either version. The
lean candidate exposes that real dependency instead of appearing to remove a
rule the baseline delivered directly to workers.

## Complexity judgment

Operational complexity is unchanged. Interpretive and maintenance complexity
decrease modestly: one verified root rule now has one carrier instead of being
restated in the skill, and no runtime-test branch or fallback packet variant is
introduced. Exact role ownership remains local because it varies by stage.

The dependency is deliberate. A change to the root Delegation paragraph
recommissions this skill under the instruction collection and type contracts.
That broad dependency is cheaper than maintaining duplicate generic controls
inside every commissioning skill.

## Checks

- `commonplace-validate` passed for the adopted skill and every changed
  workshop artifact.
- The promoted-skill scaffold projection test passed all 18 cases against the
  lean candidate.
- The generic skill-creator validator rejected the existing Commonplace-only
  frontmatter keys `argument-hint`, `context`, `type`, and `user-invocable`.
  This is the pre-existing validator-compatibility boundary recorded by the
  earlier refinement, not a candidate defect.
- `git diff --check` passed.

No cachebuster or reinstall is needed. The source-checkout projections are
symlinks, and no dependency, entry point, build metadata, or scaffold package
changed.
