# Disjoint-root implementation packets

**Status:** reviewable implementation sequence. No packet is implemented by
this workshop-only change.

**Decision source:** [installed-product decision](./installed-product-edition-decision.md)

## Program rule

The successor architecture is one program, but it must not land as one
correlated mega-patch. Each packet below has a bounded activation surface,
tests, and a rollback boundary. Dormant foundations may land before current
guidance changes. No accepted ADR or current-facing document may claim a
future state without naming that staged boundary.

## Packet 0 — Freeze the decision and fixtures

**Outcome:** make the intended behavior executable as fixtures without changing
the current installer.

- Encode source, fresh-host, optional-reader, and legacy nested-layout fixture
  shapes.
- Record the two installed root identities and selected paths.
- Record source-to-installed path expectations and ownership transition cases.
- Keep the successor ADR as a workshop draft.

**Acceptance:** fixtures demonstrate that `kb/`, `commonplace-library/kb/`,
and optional `commonplace/kb/` are non-overlapping and independently
selectable.

## Packet 1 — Add the dormant `kb-root` foundation

**Outcome:** provide one Python-owned root, collection, path, and type model
without switching init or current guidance.

- Add explicit root identity and physical boundary records.
- Reject overlapping declared roots.
- Discover collections recursively inside one selected root, including type
  collections and excluding validation-ignore boundaries.
- Make root-relative artifact and type identities carry the root identity.
- Make review/store path identities capable of carrying that identity without
  switching current installed behavior.
- Resolve `kb/...` from the owning root and remove the need for a future
  cross-root fallback.
- Keep source checkout defaults behaviorally equivalent while the installed
  product still uses its current layout.

**Acceptance:** focused source and synthetic multi-root tests pass; no current
install projection or documentation has changed.

## Packet 2 — Implement V1 over explicit roots

**Outcome:** one structured, recursive, non-fail-fast full-validation suite
becomes available before product repair.

- Select declared roots explicitly.
- Validate every discovered collection in each root.
- Validate type specs outside collection coverage exactly once.
- Run repository-level checks once.
- Return stable Python results before text or optional JSON rendering.
- Keep coverage and severity separate.

**Acceptance:** the suite truthfully reports current installed failures and
proves which roots and collections it examined. This becomes I2's acceptance
harness.

## Packet 3 — Build the install-projection compiler

**Outcome:** compile the desired Commonplace root without yet migrating an
existing host in place.

- Extend the manifest along orthogonal root, role, ownership, and
  materialization axes.
- Compute the hybrid evidence closure.
- Project the Commonplace KB into `commonplace-library/kb/`, including its own
  `types/`.
- Project selected Commonplace type replicas into host `kb/types/`.
- Rewrite included paths and disposition omitted dependencies.
- Build the complete desired tree in a temporary location.
- Use the same compiler for wheel, sdist, and editable-source inputs.

**Acceptance:** compiled products are byte-identical for the same revision,
contain no snapshots or unresolved local dependencies, and pass V1 with zero
missing-link warnings under the release policy.

## Packet 4 — Activate fresh installation

**Outcome:** new projects receive the disjoint installed product.

- Switch init to the compiled product.
- Write installer state atomically after validation and materialization.
- Derive promoted skill sources and generated templates from declared roots.
- Scaffold complete host sources and work collections.
- Activate root-aware review, publishing, navigation, and command consumers
  required to operate the fresh product.
- Update current install, architecture, navigation, type, command, and skill
  documentation in the same activation sequence.
- Promote the successor ADR when the operativity path is true.

**Acceptance:** a wheel-installed and editable-installed fresh project each
contain `host-kb` at `kb/` and `commonplace-kb` at
`commonplace-library/kb/`; every generated surface names the same paths.

## Packet 5 — Reconcile and migrate existing installs

**Outcome:** I1 reaches the terminal ownership-aware upgrade contract.

- Read and validate installer state before mutation.
- Apply base/desired hash transitions to managed and replica files.
- Preserve user-owned files, deliberate deletions, and local forks.
- Detect known legacy `kb/commonplace/` projections.
- Install and validate the new disjoint root before classifying legacy paths as
  obsolete.
- Provide a separate exact-target prune operation; never recursively delete a
  legacy directory.

**Acceptance:** clean, modified, missing, already-current, unknown, and
upstream-removed fixtures follow the selected transition table. Sentinel user
content survives migration and prune refusal cases.

## Packet 6 — Converge dependent consumers

**Outcome:** E1 and the tag workshop consume the common root model rather than
recreating path traversal.

- Move promoted-skill path enumeration and deterministic traversal behind
  portable Python operations.
- Run native-Windows CI and the runtime probe over declared roots.
- Let tag Phase 1 resolve exact membership within a selected `kb-root` without
  embedded-root exclusions.
- Activate tag consumers in Phase 2 and move root-local heads in Phase 3.

**Acceptance:** the impact ledger is refreshed by consumer class; all
cross-consumer fixtures use the same root-local results; cross-root unions are
explicit navigation operations.

## Packet 7 — Close authority and migration residue

**Outcome:** make the new implementation the only current contract.

- Point earlier installation ADRs forward and mark their superseded clauses.
- Remove retired nested-root and shared-type claims from current guidance.
- Run lexical guards for `kb/commonplace/` only where it remains a legacy
  migration witness, and for `commonplace/kb/` only where it means reader mode.
- Complete the Areas/Topics migration after tag adoption.
- Promote the contract-change gate after this program and one independent
  change have exercised it.
- Recheck the I1/I2/I3/V1/E1/T1 witnesses and record outcomes before deleting
  the workshops.

**Acceptance:** every current operative surface agrees; retained contradictory
text is explicitly historical; workshop closure criteria pass.

## Dependency flow

Packets 0 and 1 precede V1. V1 precedes projection acceptance. The compiler
precedes fresh-install activation. Fresh installation precedes legacy
migration so the destination product is already known-good. E1 portability
work that does not depend on roots may proceed independently, but tag semantic
activation waits for the root foundation and V1. Authority cleanup is last.
