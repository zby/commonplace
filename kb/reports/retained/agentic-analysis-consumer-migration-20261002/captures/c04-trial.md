# C04 fixture synthesis — storage evidence in four main results

This is a procedure trial on synthetic test fixtures, not a finding about
external systems. The output remains in the workshop because its inputs are a
local test corpus. No production review or public synthesis was replaced.

## Evidence boundary

Selection: all four generated main reviews in the isolated fixture repository.
Three declare code-grounded evidence; one declares doc-grounded evidence. All
fixture analysis cutoffs are 2026-09-04. The bundle contains the full retained
results, compact review identities, comparison contracts, method code, and
instructions. The fixture repository has no legacy collection, local run
state, or source checkout.

- Bundle: `/tmp/commonplace-c04-ao19i4vg/evidence`
- Manifest SHA-256: `f3a118a842b37f2b62123c8962bba29cb3d5cecdbdf2671a07143d640e4fdb46`
- Matrix SHA-256: `f778407205bcd3c6db209eff6757b175d3a474a14b1dea6e3bd1cded2ee6755f`
- Verification mode: local; no independent semantic checker.

The selection is a fixture population and supports no claim about the size,
coverage, or prevalence of the production corpus. Its full result paths below
are relative to the isolated bundle, not this checkout's published collection.

## Code-grounded fixtures

One of one fixtures with an assessed storage set at wired-or-stronger evidence
has file storage. That same fixture also has SQLite storage. It contributes one
system to the denominator despite having two storage values.

The other two code-grounded fixtures are excluded from that denominator:
`claimed-fixture` supplies only a claimed vector-storage value, and
`unknown-fixture` leaves storage uninspected. The trial therefore supports no
whole-population claim that all three use files or that the excluded fixtures
lack file storage.

In `wired-fixture`, canonical record `OBJ-1` describes session notes in Markdown
files and a SQLite lookup index rebuilt from those notes. This supports the
two-store classification and a primary-record/derived-index distinction in
this fixture. Its Runtime account says no dynamic check was planned. The
record therefore does not establish an observed rebuild, successful recovery,
or a performance advantage.

Intended evidence citation: `kb/reports/retained/agentic-system-analysis/AAS-2026-09-04-wired-fixture-01/result.md`,
Shared records → Operative objects, `OBJ-1`; full-result SHA-256
`f06af7058957d128f9dd587b42d1383cc5eca0392889641a6e2ad6df96d98cdf`.
Its compact-review SHA-256 is
`3cc4ea235b42720379bf61a0f56c0367258730f05a09cc95e5ca06d934a3225f`.

## Doc-grounded fixture

`doc-fixture` declares a claimed SQLite value. It appears here as documentation
coverage and contributes nothing to the implementation/operation denominator.
No inspected or observed SQLite behavior is inferred from that value.

## Query ledger

- Fields: `source_tier`, `storage_substrate`, `storage_substrate_assessment`,
  `storage_substrate_basis`.
- Eligible: code-grounded, known storage set, basis wired, observed, or causally
  supported. Numerator: membership of `files` in that set, once per row.
- Numerator / denominator: **1 / 1**.
- Included and matched run: `AAS-2026-09-04-wired-fixture-01`.
- Excluded runs: `AAS-2026-09-04-claimed-fixture-01` (claimed basis),
  `AAS-2026-09-04-unknown-fixture-01` (uninspected), and
  `AAS-2026-09-04-doc-fixture-01` (doc-grounded).
- Withheld: whole-population storage prevalence, negative storage claims for
  excluded rows, observed operation, recovery reliability, and causal benefit.

The executable query, final verification, and broader rejection checks are
recorded in [C04 acceptance](./c04-acceptance.md).
