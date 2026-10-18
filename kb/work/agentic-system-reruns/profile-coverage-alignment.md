# Profile coverage alignment for fresh analyses

**The validator now counts warranted local learning negatives as classified
coverage. The final complete suite passed: 1,684 tests, including slow tests.**
This completes the implementation gate left open at preparation commit
`0355617f1`. It does not repair an old run or authorize batch execution.

## Rule and consumers

The [profile type](../../agentic-system-analyses/types/agentic-system-memory-profile.md)
owns the rule. Its existing schema already permits these controlled values and
coverage labels, so no schema version or field change was needed.

`validate_comparison` counts both local `yes` and warranted local `no` findings
when checking classified coverage. A known `no` unit plus an unresolved included
unit requires a `partial` axis. A local `no` still requires known unit coverage
and an evidenced-absence record. One unit cannot assert both values. An
unresolved-only inventory does not become partial without classified findings.

The projection remains unchanged: incomplete learning coverage never yields
system-wide `no`, and any `yes` suppresses that union negative. Local negatives
and their evidence remain in the unit inventory. Unresolved learning cannot
make its trace source inapplicable. CSV export, matrix statistics and
complete-value consumers retain those distinctions.

Consumers checked:

- Producer and verifier packets load the owning type through the plan's
  `memory-profile-type` binding. Their instructions need no duplicate rule.
- `profile_member_comparison` resolves profile findings against declared member
  records. New-candidate callers use strict current coverage rules.
- The directory-artifact rule and `validate_draft_in_role` enforce that rule for
  working candidates. Synthetic consumer tests exercise both unresolved labels.
- Retained-artifact validation and `load_results` consume the same comparison
  implementation. Their historical compatibility is bounded below.
- Projection, CSV and matrix statistics keep the existing existence-union rules.

## Two immutable historical consumers

A corpus scan found two already-published profiles using the old convention:
EchoWiki and Interview Doc Agent. Their indeterminate aggregate retains a local
negative. Strictly applying the new convention to every historical reader would
break full inherited-corpus validation before any new run could open.

A documented `BACKCOMPAT` exception therefore recognizes only these exact full
profile byte hashes:

- EchoWiki: `0712abad6df9c56751dcef17d50008ee46962eb0e40bac836df5b5a2178ed32a`.
- Interview Doc Agent: `a5a82049e2fcb5538700295acfc63d41285cd37717879ade977b99c7c9ef434d`.

Retained readers must supply those bytes, and their parsed metadata must match
the metadata being validated. The directory rule supplies this context only
for a pinned direct canonical retained artifact, not a working run artifact or
an unpinned role draft. Ordinary
producer and role-draft calls remain strict. Tests reject missing bytes,
changed body/frontmatter, mismatched metadata and unrelated profiles. Record
resolution, controlled vocabulary and absence warrants remain enforced.

The exception preserves the historical labels and suppresses system-wide `no`;
it does not silently normalize them to partial or clear their content. Remove
the current-corpus exception when both profiles are replaced by independently
audited new publications. No new analyses of those systems are commissioned
here. All retained publication bytes and root files remain unchanged.

## Verification and limits

- `uv run pytest -m ''`: **1,684 passed in 289.01 seconds** in the final run.
  An earlier full run passed 1,683 tests before adding the retained-directory
  draft-gate regression.
- The actual retained comparison reader loads **182 rows**, including both
  historical cases with their original indeterminate labels and local evidence.
- New tests cover local negatives plus unresolved units, mixed yes/no/unknown
  inventories, unresolved-only inventories, unit-scoped absence, source
  applicability, CSV roundtrips, statistics, nonmutation, role validation and
  narrow historical reading without a working-candidate bypass.
- Earlier development runs exposed the intended old-validator failures, a
  frontmatter-result API mistake in the compatibility check, and a missing raw
  content field in a synthetic reader fixture. These were corrected before the
  passing full run; no assertion or isolation was removed.
- Final log: `/tmp/commonplace-batch-22-alignment-final-tests.txt`; earlier log:
  `/tmp/commonplace-batch-22-alignment-full-tests.txt`.

This is deterministic verification, not a guarantee of a fresh analysis's
semantic quality. Secure LLM Wiki's old method, candidate, refusal and attempts
remain untouched. Fresh publications still need independent exact-byte audits
and separately authorized integration. Source acquisition, worktree setup and
batch dispatch remain unperformed.
