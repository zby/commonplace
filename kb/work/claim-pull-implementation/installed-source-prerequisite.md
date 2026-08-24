# Installed-source prerequisite

Commit `bffedcae` (`Install sources as a user collection`) added generic
`kb/sources/COLLECTION.md` and `README.md` templates plus manifest, test, and
documentation changes. Claim-pull does not own that implementation.

Before claim-pull implementation begins, accept evidence that:

- focused and full tests passed;
- the wheel contains both templates;
- a fresh installation creates both source collection heads and validates its
  landings; and
- initialization reruns preserve user edits to both files.

Claim-specific behavior stays in the ingest type and grounding path; existing
user-owned collection contracts are not assumed to upgrade.
