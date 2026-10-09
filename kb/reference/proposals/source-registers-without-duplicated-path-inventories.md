---
type: reference/types/design-proposal.md
description: "Proposal: remove the Source register's duplicated path inventory so later analysis findings can cite any inspected path in their frozen source"
---

# Source registers without duplicated path inventories

## Problem

The boundary author lists source paths before the specialists discover all
paths needed for their findings. Judges have treated that list as an exhaustive
inventory, making source discovery a defect the record loop cannot repair. Each
finding already carries a source ID and commit-relative path, and the source
ID fixes its repository and revision.

## Current state (as of 2026-10-01)

The source contract requires a Source register with inspected paths and
citation anchors, and requires each source-dependent finding to name a source
ID and local anchor that exists at the frozen revision. It does not explicitly
make the register's anchor list an exhaustive citation whitelist. In fresh Luna
run `AAS-2026-10-01-instinctual-memory-01`, the boundary listed three
implementation anchors and scoped the source unit to modules including the
later-inspected paths. Both record judges nevertheless required those further
paths in the register. Reconciliation could not amend the boundary, and final
verification stopped the run before synthesis.

The runtime and source register were frozen at the same clean commit. The
stop included the judges' inventory interpretation, not an unknown repository revision.
The final reconciliation also lost a formal amendment and conflict marker;
removing the inventory would not repair those independent faults. Another
trial altered a generated quotation while copying it; that is a separate
retained-content integrity issue.

## Forces

Keep source identity, revision, evidence layer and inspected scope visible.
Every finding must remain traceable to an existing path at the frozen revision.
Avoid an inventory whose author cannot yet know later discoveries, and avoid
another correction route solely to maintain duplicated information. Source
membership and quotation occurrence do not establish semantic support.

## Options and operative paths

### Remove the register's path inventory

Keep source identity, revision, evidence layer and inspected scope in the
register; retain the full local anchor on each finding. The source contract
would stop requiring a second list of those paths. Workers would consume that
rule as authoring authority, and validators and judges would resolve the
finding's source ID and path against the frozen source rather than a copied
inventory. Existing source-resolution and quote-generation code supplies the
revision boundary; no consumer would treat mere file existence as support.

### Register every source path before analysis

The boundary job could enumerate all paths up front. Later workers and judges
would consume that inventory as their allowed citation surface. This preserves
the current rule, but increases boundary work and context, and mixes inspected
anchors with files that were merely enumerated.

### Add boundary correction after report verification

The judge could return missing paths to a boundary author. Code would consume
that return as authority to change the Source register and repeat affected
checks. This preserves the inventory at the cost of another correction route
and a mutable boundary document. The frozen source revision would remain fixed.

## Adoption criteria

The operator must choose whether register membership means a frozen source
unit or an exhaustively enumerated file surface. A trial must demonstrate that
a specialist can cite a newly inspected path at the same revision without
reopening the boundary, while an unknown source ID or nonexistent path is
still refused. Quote-copy integrity and formal reconciliation retention remain
separate decisions. This proposal does not change the shipped contract.
