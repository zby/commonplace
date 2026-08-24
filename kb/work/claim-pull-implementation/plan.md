# Claim-pull implementation plan

## Behavior

### Grounding

The explicit grounding instruction receives:

```text
Target: <exact ingest path or canonical source URL>
Claim needed: <source-side proposition or question>
```

It reads the complete Claims section. If an entry answers the request, it
returns that entry unchanged. Otherwise it reads the name-paired,
checksum-verified primary snapshot, constructs one entry in the fixed shape,
and sends this minimal handoff to `cp-skill-ingest`:

```yaml
claim_append_request:
  ingest_path: <exact path>
  snapshot_path: <name-paired, checksum-matching path>
  entry: <complete Markdown entry>
```

`cp-skill-ingest` rechecks the checksum and extracts, appends the entry without
changing any existing entry or any section outside Claims, validates, and
reports success. It replaces the canonical empty sentence on the first append.
Similar, narrower, or disputed entries may coexist. Missing primary bytes or
secondary authority stops without mutation.

Snapshot pairing stays name-derived:
`kb/sources/<slug>.ingest.md` pairs with
`kb/sources/.snapshots/<slug>.md`. `snapshot_sha256` verifies the named file; it
does not discover another snapshot. A missing or mismatched named file routes to
re-ingest.

### Writing

When a candidate adds or materially changes a named external-source dependency,
`cp-skill-write` resolves the exact ingest and reads Claims.

- If an entry supports the dependency, prefer its exact
  `Claim (paraphrase)` wording, link the ingest, and keep transfer reasoning in
  the target.
- Otherwise stop without saving that dependency and report the literal
  grounding instruction with `Target` and `Claim needed` filled in.

The writer does not invoke grounding, read the snapshot, edit the ingest, or
introduce a result protocol. Unchanged sourced wording does not retrigger.

Its refusal names the source-checkout instruction at
`kb/instructions/ground-source-dependent-claims.md` or the installed copy under
`kb/commonplace/instructions/`, with both inputs filled in.

### Review

Add a virtual `source` review lens: `source` selects all pairs and
`source/<ingest-slug>` selects one ingest. For each resolved Markdown link from
a reviewable artifact to an ingest, derive one `(artifact, ingest)` pair. The
wrapper treats a purely adjacent link as making no support claim.

The ingest is the criterion-side freshness input. A fixed wrapper asks whether
Claims support the target's articulated use, scope, and transfer. Existing
two-input freshness makes the pair stale when either file changes.

The pair is a verdict gate. Judge every source-dependent use and return the
worst outcome:

- `pass`: every use is supported within the selected entry's bounds, or the
  link is purely adjacent and makes no support claim;
- `warn`: support is plausible but the selected claim, retained qualifier, or
  transfer is not articulated clearly enough to verify; or
- `fail`: any use lacks a supporting entry, exceeds its scope or limitation, or
  asserts an unsupported transfer.

### Re-ingest

Implement this first. Same-checksum refresh must retain every Claims entry and
its Markdown content through the existing primary and one repair attempt.
`cp-skill-ingest` keeps the incumbent until the replacement validates and
restores it after an ordinary failed attempt.

The existing drafting handoff gains only `retained_claims`. New and approved
changed-observation drafts receive the canonical empty section; same-checksum
refresh receives the incumbent section. Claim append is a deterministic
Claims-only edit owned by the parent ingest skill and does not invoke the
drafting worker.

A different checksum requires explicit user approval and is allowed only for
the same canonical source and path when Claims are empty. Populated Claims
block it. `re-ingest` performs the post-success inbound audit but no second
report rewrite.

```yaml
re_ingest_request:
  ingest_path: <exact ingest path>
  snapshot_path: <name-paired snapshot path>
  allow_checksum_change: false | true
```

The first call uses `false`; after disclosure and approval, retry with `true`.

Permanent routes:

- source checkout: `Read and execute kb/instructions/re-ingest.md with Target: <path>.`
- installed project: `Read and execute kb/commonplace/instructions/re-ingest.md with Target: <path>.`

## Order

1. Accept the [installed-source prerequisite](./installed-source-prerequisite.md).
2. Make re-ingest Claims-safe.
3. Add Claims to the type, schema, template, drafting instruction, and corpus.
4. Promote the grounding instruction and add the ingest-owned append handoff.
5. Add the bounded writer guard.
6. Implement and document the source review lens.
7. Run tests and the two retained semantic cases.
8. Promote the ADR, then begin the cleanup cohort.

## Acceptance

- Every ingest has one Claims section; migration changes no old checksum or
  analysis.
- Same-checksum refresh retains Claims; failed refresh restores the incumbent.
- Changed observation is approved, same-source, same-path, and empty-Claims or
  it does not change the report.
- Grounding reuses or appends one primary-source-supported entry and changes no
  incumbent entry.
- Similar entries require no merge, identity, or conflict machinery.
- The writer either reuses adequate normalized wording or stops with the exact
  grounding route; it never dispatches or mutates.
- Source pairs derive from resolved ingest links and become stale when either
  input changes.
- Source verdicts apply the stated pass/warn/fail contract, including adjacent
  links and mixed uses.
- Fresh installs receive the coherent files. Initialization may add absent
  files but does not upgrade differing old copies.
