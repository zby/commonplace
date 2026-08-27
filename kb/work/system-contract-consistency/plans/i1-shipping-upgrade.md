# I1 plan — Make Commonplace upgrades ownership-aware

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. See the
[witness ledger](../baseline-2026-08-27.md). ADR 021 remains the contradictory
operative witness; architecture's former “re-sync” wording is stale and no
longer part of the finding.

## Resolution selected

Preserve ADR 021's intent that installed Commonplace content is isolated and
read-only, but supersede its nested `kb/commonplace/` layout, unimplemented
marker, and refresh protocol. The destination is the disjoint
`commonplace-library/kb/` root. Preserve-only describes current behavior and
may be documented as an interim limitation; it is not the terminal
architecture for a large Commonplace-owned projection.

The [installed-product decision](../installed-product-edition-decision.md)
selects the concrete edition, pairwise-disjoint `kb-root`s, five scoped
per-file ownership values, legacy-layout migration, and base/desired-hash
transition this plan will promote through a successor ADR. The workshop packet
is an implementation input, not durable authority.

The terminal transition is:

- user-owned paths are never overwritten automatically;
- `commonplace-managed` paths unchanged since installation are replaced safely;
- Commonplace-owned paths edited locally are preserved and reported as forks;
- upstream-removed Commonplace paths are reported as obsolete and removed only
  by a deliberate prune operation.

Projected runtime skills follow the same rule as Commonplace library content.
Generated control-plane templates need an explicit ownership/customization
classification rather than being treated as an undifferentiated file set.

## Work

1. Promote the workshop's successor ADR only with the activation packet. I3
   supplies disjoint `kb-root`s and root-local identities, I2 supplies the
   hybrid edition and projection map, and S1 supplies the installed sources boundary. The upgrade
   mechanism is generic; T1 supplies later migration inputs and acceptance
   criteria rather than its own updater.
2. Extend the manifest model with ownership and upgrade policy for each projected
   entry. Define the status of library files, projected skills, user collection
   heads, generated templates, host-root Commonplace type replicas, and user
   extensions. Use `commonplace-managed`, `commonplace-replica`, `user-seed`,
   `user-owned`, and `installer-state` only as declared field values.
3. Persist an installed per-file manifest or equivalent containing enough
   package identity, target path, ownership, and prior bytes/hash information to
   distinguish an unchanged old Commonplace file from a local fork. Do not use
   presence alone as provenance.
4. Implement and test the terminal transition table in the decision packet. A
   prune command or explicit mode may remove confirmed obsolete
   `commonplace-managed` paths only after showing the exact targets; ordinary
   init remains non-destructive toward ambiguous and user-owned paths.
5. Migrate known legacy projections from `kb/commonplace/` only after the new
   `commonplace-library/kb/` tree builds and validates. Preserve unknown or
   edited legacy files as forks. Report clean legacy paths as obsolete and
   remove them only through the deliberate prune operation; never recursively
   delete the legacy directory.
6. Promote the [successor ADR draft](../successor-installation-adr-draft.md),
   mark ADR 021 superseded, and reconcile ADRs 014 and 037, architecture,
   `INSTALL.md`, and command documentation in the activation sequence.
7. If terminal upgrades cannot land in the first release, document preserve-only
   as an explicit interim limitation and open a separate upgrade-mechanism
   proposal with the terminal acceptance criteria below. Do not present manual
   reconciliation of the whole framework tree as the steady-state workflow.

## Verification

- The selected edition is identical across scaffold, wheel, sdist, tests, and
  docs, and the installed ownership manifest covers every projected file.
- Fresh products declare disjoint host and Commonplace roots; legacy migration
  never needs an outer-root exclusion or recursive deletion.
- A same-version rerun reports Commonplace files as unchanged without rewriting
  them.
- An unchanged old Commonplace file upgrades to the new package bytes.
- A locally edited Commonplace file and projected skill retain their local bytes,
  are reported as forks, and are not confused with merely old upstream bytes.
- New upstream paths are added. Removed upstream paths are reported as obsolete
  and survive until the explicit prune path is invoked.
- User-owned content and user collection contracts are never overwritten.
- A corrupted or missing ownership baseline fails safely rather than guessing.
- A checked-in legacy `kb/commonplace/` fixture and a fresh scaffold converge
  on all unchanged Commonplace-owned paths at the new root while preserving
  sentinel user content.

I1 is complete only when the ADR chain, reference, installer, and tests describe
the same ownership-aware transition. An interim preserve-only release does not
close I1; it only removes misleading upgrade claims while the terminal proposal
remains open.
