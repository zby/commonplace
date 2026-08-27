# I1 plan — Make framework upgrades ownership-aware

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. See the
[witness ledger](../baseline-2026-08-27.md). ADR 021 remains the contradictory
operative witness; architecture's former “re-sync” wording is stale and no
longer part of the finding.

## Resolution selected

Keep ADR 021's useful `kb/commonplace/` namespace decision, but supersede its
unimplemented marker and refresh protocol with explicit ownership classes and
a prior-version baseline. Preserve-only describes current behavior and may be
documented as an interim limitation. It is not the terminal architecture for a
large framework-owned projection.

The [installed-product decision](../installed-product-edition-decision.md)
selects the concrete edition, logical roots, five per-file ownership classes,
and base/desired-hash transition this plan will promote through a successor
ADR. The workshop packet is an implementation input, not durable authority.

The terminal transition is:

- user-owned paths are never overwritten automatically;
- framework-owned paths unchanged since installation are replaced safely;
- framework-owned paths edited locally are preserved and reported as forks;
- upstream-removed framework paths are reported as obsolete and removed only
  by a deliberate prune operation.

Projected runtime skills follow the same rule as framework library content.
Generated control-plane templates need an explicit ownership/customization
classification rather than being treated as an undifferentiated file set.

## Work

1. Adopt the installed-product decision in the successor installation ADR. I3
   supplies roles and logical roots, I2 supplies the hybrid edition and
   projection map, and S1 supplies the installed sources boundary. The upgrade
   mechanism is generic; T1 supplies later migration inputs and acceptance
   criteria rather than its own updater.
2. Extend the manifest model with owner and upgrade policy for each projected
   entry. Define the status of library files, projected skills, user collection
   heads, generated templates, shared framework types, and user extensions.
3. Persist an installed per-file manifest or equivalent containing enough
   package identity, target path, ownership, and prior bytes/hash information to
   distinguish an unchanged old framework file from a local fork. Do not use
   presence alone as provenance.
4. Implement and test the four terminal transitions above. A prune command or
   explicit mode may remove confirmed obsolete framework-owned paths only after
   showing the exact targets; ordinary init remains non-destructive toward
   ambiguous and user-owned paths.
5. Write a successor ADR that restates the surviving namespace decision and
   replaces ADR 021's bundle, marker, drift, and refresh clauses. Mark ADR 021
   superseded and reconcile ADRs 014 and 037, architecture, `INSTALL.md`, and
   command documentation.
6. If terminal upgrades cannot land in the first release, document preserve-only
   as an explicit interim limitation and open a separate upgrade-mechanism
   proposal with the terminal acceptance criteria below. Do not present manual
   reconciliation of the whole framework tree as the steady-state workflow.

## Verification

- The selected edition is identical across scaffold, wheel, sdist, tests, and
  docs, and the installed ownership manifest covers every projected file.
- A same-version rerun reports framework files as unchanged without rewriting
  them.
- An unchanged old framework file upgrades to the new package bytes.
- A locally edited framework file and projected skill retain their local bytes,
  are reported as forks, and are not confused with merely old upstream bytes.
- New upstream paths are added. Removed upstream paths are reported as obsolete
  and survive until the explicit prune path is invoked.
- User-owned content and user collection contracts are never overwritten.
- A corrupted or missing ownership baseline fails safely rather than guessing.
- A checked-in pre-upgrade fixture and a fresh scaffold converge on all
  unchanged framework-owned paths while preserving sentinel user content.

I1 is complete only when the ADR chain, reference, installer, and tests describe
the same ownership-aware transition. An interim preserve-only release does not
close I1; it only removes misleading upgrade claims while the terminal proposal
remains open.
