# Claim-pull implementation plan

## Behavior

### Scope

V1 guards Commonplace's two promoted artifact-writing paths:
`cp-skill-write` and `cp-skill-write-multistage`. The guard runs when a
candidate adds or materially changes a dependency on a named external source.
It applies regardless of the writable target collection.

In `cp-skill-write`, run the guard after drafting but before the first durable
write. In `cp-skill-write-multistage`, run it against `candidate.md` before
promotion; a blocked dependency leaves the workshop and candidate intact but
does not change the target. Unchanged source-dependent wording does not
retrigger.

This is not a universal write interceptor. V1 does not detect unattributed
prior art, prevent direct manual edits, or amend every specialized workflow
that can edit Markdown. The source review lens can detect unsupported uses that
are linked to an ingest; it cannot find an unnamed source dependency.

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

When a candidate in either guarded writer adds or materially changes a named
external-source dependency, the writer resolves the exact ingest and reads
Claims.

- If an entry supports the dependency, prefer its exact
  `Claim (paraphrase)` wording, link the ingest, and keep transfer reasoning in
  the target.
- Otherwise stop without saving that dependency and report the literal
  grounding instruction with `Target` and `Claim needed` filled in.

The writer does not invoke grounding, read the snapshot, edit the ingest, or
introduce a result protocol. An ordinary write stops before saving; a
multistage write records the blocker and retains its workshop without promoting
the candidate.

Its refusal names the source-checkout instruction at
`kb/instructions/ground-source-dependent-claims.md` or the installed copy under
`kb/commonplace/instructions/`, with both inputs filled in.

### Review

Add a virtual verdict-kind `source` review lens. Within the artifact scope
already selected by `--note` or `--user-verified`, `source` derives every source
pair and `source/<slug>` keeps only the named ingest. Here `<slug>` is the
filename with `.ingest.md` removed. `--all-gates`
includes `source`; report-kind `critique` remains opt-in. Source pairs have no
`watches:` declaration and therefore never qualify for trivial-change
acknowledgement.

The lens does not introduce or expand review scan roots. Explicit `--note`
paths and directories keep their current behavior. `--user-verified` keeps the
current top-level `kb/notes/` and `kb/reference/` scan. Wider project-specific
review scope belongs to the existing review-configuration proposal.

For each resolved Markdown link from a selected artifact to
`kb/sources/<slug>.ingest.md`, derive one `(artifact, ingest)` pair. Ignore URL
fragments when resolving identity and deduplicate repeated links to the same
ingest. An artifact with no resolved ingest link produces no source pair. A
purely adjacent link still produces a pair; the wrapper treats it as making no
support claim.

The persisted `criterion_path` is the exact ingest path and its public
criterion ID is `source/<slug>`. Path normalization, stored-path rendering,
request expansion, selector applicability, and create-jobs revalidation must
all recognize the same mapping. A source path outside `kb/sources/`, a file not
ending `.ingest.md`, an unknown slug, or a selected artifact that does not link
the requested ingest is rejected or skipped through the normal selector
contract.

The complete raw ingest file is the criterion-side snapshot and freshness
input. Existing two-file freshness therefore makes the pair stale when either
the artifact or ingest changes. The source-conformance wrapper is mechanical
prompt scaffolding, like the existing type and collection wrappers: it tells the
reviewer to compare each articulated source-dependent use with the complete
Claims section, apply the outcome mapping below, and return the worst outcome.
The judgment-bearing particulars remain in the artifact's use and the ingest's
Claim, Scope, Confidence, and Limitation fields.

The wrapper is deliberately outside the freshness hash. A future edit that
changes its semantics is a review-system upgrade and requires an explicit
corpus-wide re-review or acknowledgement; it must not be presented as ordinary
file-triggered staleness. No synthetic criterion text, third freshness input,
or database-schema change is introduced.

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
Before dispatching a worker for any existing output, `cp-skill-ingest` makes an
exact byte-for-byte backup outside `kb/` using a platform-native byte copy and
verifies the backup's SHA-256 against the incumbent. If it cannot create and
verify that backup, it stops before dispatch. It retains the backup until the
replacement has passed all handoff checks and final validation.

The existing drafting handoff gains only `retained_claims`. New and approved
changed-observation drafts receive the canonical empty section; same-checksum
refresh receives the incumbent section. Claim append is a deterministic
Claims-only edit owned by the parent ingest skill and does not invoke the
drafting worker.

The primary worker may continue writing the final `output_path` directly. The
parent checks the snapshot checksum, exact retained Claims block, handoff
constraints, and full validation. If the primary attempt fails, keep its failed
candidate at `output_path` for the existing single repair worker and pass the
same `retained_claims`. If the repair attempt or final validation still fails,
restore the verified backup to `output_path` with an exact byte copy, verify the
restored SHA-256, and report that re-ingest failed with the incumbent restored.
Delete the backup only after either a validated replacement or a verified
restore. If copying or verification of the restore fails, keep the backup, stop,
report both paths and hashes, and do not claim that the incumbent was restored.

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

This recovery contract covers ordinary handled failures. V1 deliberately does
not add staging, atomic rename, locks, compare-and-swap, concurrent-writer
coordination, or recovery after the parent process or machine crashes between
overwrite and restore. Same-ingest concurrent writes remain last-writer-wins.
Those are TODOs to revisit only after an observed failure warrants the extra
machinery.

Permanent routes:

- source checkout: `Read and execute kb/instructions/re-ingest.md with Target: <path>.`
- installed project: `Read and execute kb/commonplace/instructions/re-ingest.md with Target: <path>.`

## Order

1. Accept the [installed-source prerequisite](./installed-source-prerequisite.md).
2. Make re-ingest Claims-safe.
3. Add Claims to the type, schema, template, drafting instruction, and corpus.
4. Promote the grounding instruction and add the ingest-owned append handoff.
5. Add the bounded guard to both promoted writer paths.
6. Implement and document the source review lens.
7. Run tests and the retained semantic cases in
   [claims-shape-evidence.md](./claims-shape-evidence.md).
8. Promote the ADR, then freeze and complete the first cohort under
   [cleanup-plan.md](./cleanup-plan.md).
9. Record the rollout findings. Hand the ingest-extraction and
   intermediate-node evidence to
   [source-grounding](../source-grounding/README.md), and hand cases dispositioned
   as `literature handoff` to
   [literature-disposition](../literature-disposition/README.md).

## Acceptance

- Every ingest has one Claims section; migration changes no old checksum or
  analysis.
- Same-checksum refresh retains Claims; failed refresh restores the incumbent.
- Re-ingest never dispatches against an existing output without a verified
  exact-byte backup; handled final failure restores the incumbent hash.
- Changed observation is approved, same-source, same-path, and empty-Claims or
  it does not change the report.
- Grounding reuses or appends one primary-source-supported entry and changes no
  incumbent entry.
- Similar entries require no merge, identity, or conflict machinery.
- Both promoted writers either reuse adequate normalized wording or stop with
  the exact grounding route; neither dispatches grounding or mutates an ingest.
- An ordinary blocked write leaves no target change; a blocked multistage write
  retains its candidate and workshop without promotion.
- Source pairs derive from resolved ingest links and become stale when either
  input changes.
- `source`, `source/<slug>`, stored ingest paths, direct job creation, and
  `--all-gates` agree on source-pair identity and applicability.
- Source selection uses the existing `--note` or `--user-verified` artifact
  scope and does not silently widen review roots.
- Source verdicts apply the stated pass/warn/fail contract, including adjacent
  links and mixed uses.
- The raw ingest, not synthetic wrapper text, is the criterion freshness input;
  a semantic wrapper change is documented as a system-wide re-review event.
- Fresh installs receive the coherent files. Initialization may add absent
  files but does not upgrade differing old copies.
- The first cleanup cohort is frozen by target path, revision, and claim. Every
  item has a terminal disposition or named blocker, and its validation and
  source-review result are recorded.
- Cleanup records unavailable sources, repairs, and similar-entry accumulation
  as rollout evidence. It does not add reconciliation, identity, concurrency,
  or recovery machinery merely because the plan anticipated those pressures.

## Completion and handoff

The prospective implementation is complete after steps 1–7. This workshop is
complete only after steps 8–9 and every acceptance condition above. In
particular, starting the cleanup cohort does not satisfy completion.

The first cleanup cohort validates this rollout; it is not the authoritative
source-corpus decision. Its results supply two conclusions back to
`source-grounding`: whether the promoted Claims contract answers the extraction
question in practice, and whether whole-ingest links remain sufficient without
an intermediate claim node. `source-grounding` stays open until it separately
decides its source corpus, ingests accepted sources, and records rejected ones.

The cleanup cohort owns its bounded claim-level grounding, narrowing, repair,
and retained-local-delta dispositions. A case that requires an artifact-level
merge, retirement, inbound rewiring, or a broader cohort judgment receives the
`literature handoff` disposition. This plan records and hands off that case; it
does not silently absorb `literature-disposition`'s remaining cohort.

The broader search for unnamed external dependencies is also a successor, not
part of this rollout. The source lens checks resolved ingest links and must not
be described as a prior-art detector. Any later corpus sweep should preserve
the source-grounding boundary: model recall may nominate reading, but only a
captured and read source can settle a claim.

After the durable ADR and instructions are promoted, the first cohort is
complete, and these handoffs are recorded, close this workshop under the
`kb/work/` collection contract rather than retaining it as permanent
documentation.
