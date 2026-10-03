# Publish an accepted analysis by reference

Draft instruction for maintainers of the analysis workflow. Preserve exact
accepted evidence while selecting a public analysis that readers can reproduce.
This is a design contract; it does not provide a callable publication command yet.

## Inputs and authority

Receive a complete run, independently reviewed and deterministically validated
member bytes, a manifest pinning those bytes, the run's unchanged opening method,
a stable source identity and reference destination, and the expected incumbent
reference hash (or explicit absence). The coordinator owns publication; workers
write only their assigned outputs. Method inputs include both collection
contracts, applicable types and this publication contract.

## Acceptance and selection

Validate the candidate set and reference as their intended destinations. Verify
member hashes, run/boundary/source agreement, review coverage of the exact candidate
bytes and the unchanged method. The reference selects only complete sets; blocked
and out-of-scope outcomes keep their existing disposition rules and do not replace
a complete incumbent. Check the overview for usable member/reconciliation links
and an explicit account of unresolved limitations before acceptance.

There is one selected reference per source identity. Reject duplicate identities
at different destinations and refuse a replacement for a different identity.
Current comparison and synthesis populations resolve references, never infer the
latest analysis by scanning all retained directories. Explicit historical-set
selection records its input commit and pins and cannot silently become current.

## Initial publication and replacement

Copy accepted bytes unchanged into a new retained run directory. Never overwrite
an existing retained run. Stage and validate the reference privately. Recheck the
incumbent immediately before replacement. Replace the reference atomically, then
record run completion. The reference is the public selection; navigation derives
from it and must not independently select another run. Commit the retained set and
reference together before the site build exposes their selection.

Exclude state, candidates, run-state files and recovery copies from site output.
Publish only the retained member allowlist and explicitly supported historical
archive members. Archive visibility grants no current comparison eligibility.

## Failure and interruption

For ordinary exceptions, restore the prior reference and remove only new outputs
owned by this publication attempt. Keep recovery copies until completion. Before
resuming, compare the reference, retained member hashes and completion state with
the expected publication outputs. An exact match permits completion recognition;
unchanged incumbent plus no new retained set permits retry. Partial retained sets,
a new reference with incomplete state, or changed incumbent require recovery,
not blind retry. Mark uncertainty explicitly and prevent normal continuation.

An interruption before selection leaves the prior selection valid. After reference
replacement, the new selected set must already be complete and valid even if run
completion was interrupted. A fresh site build must verify selected references
and fail on dangling or invalid pins. Test first publication, replacement, stale
incumbent, write failure, partial retained copy, and interruption on each side of
reference replacement. Do not treat atomic single-file writes as a transaction
over the whole output set.
