# Installed-source prerequisite

Commit `bffedcae` (`Install sources as a user collection`) added generic
`kb/sources/COLLECTION.md` and `README.md` templates plus manifest, test, and
documentation changes. Claim-pull does not own that implementation.

Claim-pull implementation required evidence that:

- focused and full tests passed;
- the wheel contains both templates;
- a fresh installation creates both source collection heads and validates its
  landings; and
- initialization reruns preserve user edits to both files.

Claim-specific behavior stays in the ingest type and grounding path; existing
user-owned collection contracts are not assumed to upgrade.

## Accepted evidence

Accepted in the 2026-08-24 readiness check:

- the 17 focused scaffold/install tests passed;
- the full test suite passed: 532 tests;
- the built wheel contained both source collection templates;
- a fresh wheel installation created both collection heads and passed
  `commonplace-validate landings`; and
- an initialization rerun preserved edits to both user-owned files.

This prerequisite is closed. Claim-pull must not reimplement its scaffold work.
