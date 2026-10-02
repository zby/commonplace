# Review rerun acceptance

## Trigger and scope

The operator authorized fixing the metadata exposure, its recovery rule and
the uncommitted-incumbent blocker reported in
`kb/messages/20260905T175059Z-codex-review-machinery-maka-05-session-audit.md`.
The operator will run another analysis. This change does not publish run 05,
rewrite generated Maka findings, or commit the previous run to unlock reruns.

## Destination inspection and replacement

`commonplace-agentic-analysis-publication inspect-destination` takes only the
destination and source identity. Its successful output contains eligibility,
existence and the expected review digest, or `absent`. It emits no incumbent
prose, description or findings. The procedure calls it before source analysis
and saves the digest in the new run's Run prose. Prepare and publish both
require that digest; neither can silently accept a different incumbent.

A dirty or untracked generated review is replaceable when its exact review
hash and canonical retained-result hash match the recorded completed
publication and source identity. A clean committed generated review still
requires the matching retained result. Missing evidence, unrecorded edits,
different-source collisions and deleted incumbents fail. These checks establish
replacement provenance, not that the previous analysis satisfies the current
method; they add no legacy reader or completion-validation fallback.

Publication keeps exact `incumbent-review.md` and `incumbent-result.md` recovery
copies in the new run before replacing public output. It rejects conflicting
recovery copies. It rechecks incumbent bytes after validation and immediately
before replacement, and retains ordinary rollback behavior. This does not
claim an atomic transaction across processes or crash-proof publication.

The read-only check of the real Maka destination accepted digest
`0d6dde43a1a9dd7c65018189c40123fb497972697b1f4ced45288ea2dd0432e7`:
the uncommitted run-04 projection and retained result matched the publication
record. No public bytes or prior run state were changed by this check.

## Prior-analysis exposure

A coordinator that reads prior-review prose or prior substantive audit findings
before freezing its result and candidate must stop, fail that run for exposure,
and restart in a fresh coordinator context with a new run ID and source-only
inputs. Disclosure cannot restore independence. A later separately commissioned
audit records its timing and does not retroactively affect already frozen
artifacts; analytical revisions still require a fresh context. This is an
execution rule, not a claim that deterministic validation detects exposure.

## Other audit dispositions

- The system-name mismatch was correctly caught. Startup now points directly
  to the correct run-state type and tells the worker to choose its source-native
  name once and reuse it exactly. No initializer is added.
- The specialist's missing bounded-absence record was corrected through the
  intended return-and-reconcile path. Existing structural checks do not certify
  that every negative natural-language claim has a sufficient search boundary.
- Source-read truncation remains governed by bounded-read requirements. A new
  source-reading helper or inspection ledger is outside this fix.
- Whole-system coverage and semantic support remain explicit analytical limits,
  not inferred from structural validation or publication success.

## Verification

Regression tests exercise safe CLI output, vacant destinations, consecutive
uncommitted publications, tracked and untracked incumbents, missing or changed
evidence/receipts, source mismatch, stale expected digests, destination drift,
reserved recovery filenames, conflicting recovery copies, preservation of a
concurrent edit and rollback to the earlier uncommitted publication.

All 750 tests pass. Repository Ruff, changed-document validation and diff
checks pass. The real destination trial was read-only; production publication
under the new contract remains for the operator's fresh run.
