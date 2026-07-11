# Remove global note status and add committed user verification

## Goal

Replace the global note lifecycle field `status` with one narrowly defined, repository-visible attestation:

```yaml
user-verified: true
```

The result should let GitHub and other file-only renderers distinguish user-verified notes without treating maturity, currency, conjecture, supersession, and review state as one global axis.

This plan is complete when the shipped type surface, authoring and review workflows, selectors, renderer, documentation, tests, and existing content agree on the new model; status-dependent note behavior is gone; and status fields belonging to other domains remain intact.

## Decisions fixed by this plan

### Field spelling

Use `user-verified` in YAML, code-facing references, prose, and presentation labels.

The hyphenated key is valid YAML. Code accesses it explicitly, for example with `meta.get("user-verified")`. Using one spelling across every surface is more important here than attribute-style access or matching the snake-case spelling of other multiword fields.

### Meaning

`user-verified: true` means:

> A human user explicitly attests that the current substantive contents of this artifact have been verified.

The field is optional and, when present, may only be `true`. Absence means there is no current user attestation; it does not mean the artifact is false, low-quality, or unreviewed by every process.

This is load-bearing committed metadata, not a mark and not a cache of the local review database. The repository field is the published ground truth for presentation. Review records may inform the user's decision, but neither review acceptance nor freshness automatically computes `user-verified`.

### Revocation

A substantive edit to a user-verified artifact must remove `user-verified`. Reverification is a new explicit human action after the edit. Mechanical changes that are already covered by an explicit human-approved trivial-change workflow may preserve the attestation.

Do not add a content hash, verifier identity, or timestamp in this change. Git history provides the initial audit trail, and those fields can be added later if a demonstrated requirement justifies them.

### Selector semantics

The committed field is also the selector source of truth. Replace `--current` with `--user-verified`; that option selects exactly the artifacts whose current frontmatter contains `user-verified: true`.

Do not derive selector membership from review acceptance, review freshness, an inferred maturity state, or the former `current` cohort. Unverified artifacts remain selectable through explicit note or directory paths. There is no backwards-compatibility alias for `--current`.

### Scope of status removal

Remove the global note meanings `seedling`, `current`, `speculative`, and `outdated`. Do not blindly remove or rename unrelated fields also called `status`, including:

- ADR lifecycle status (`accepted`, `superseded`, `deprecated`);
- review-job execution status (`queued`, `completed`, `failed`);
- application-domain status fields in specialized types or collections;
- X/Twitter URL terminology and other ordinary prose uses of “status.”

Specialized types may continue to define a local `status` when it has one coherent type-specific meaning. The base note type must no longer supply or imply one.

## Migration rules

Inventory artifacts by resolved type and old note status before editing. Do not use a repository-wide textual deletion.

| Old global note status | Migration |
|---|---|
| `seedling` | Remove `status`. Do not add `user-verified`. |
| `current` | Treat as a candidate for `user-verified: true`, not automatic proof of human verification. Bulk conversion requires an explicit user confirmation that the affected cohort represents prior human attestations; otherwise leave the field absent until verified. |
| `speculative` | Remove `status` only after preserving the conjectural force in the artifact’s title or body where it matters. Update the `kb/notes/` contract so hypotheses remain recognizable without a global enum. Verification may attest that a note responsibly presents a conjecture; it does not turn the conjecture into established fact. |
| `outdated` | Resolve individually: delete obsolete material, update it, or preserve supersession/history explicitly in prose, links, or collection/type-local metadata. Do not translate `outdated` into “not user-verified,” because the two claims are unrelated. |

The implementation should emit and retain an inventory report during migration so the user can approve the `current` cohort and inspect all `speculative` and `outdated` decisions. The report is workshop bookkeeping and should be deleted when the workshop closes unless it proves durably useful.

## Implementation sequence

### 1. Establish the schema boundary

- Add optional `user-verified` with the only valid value `true` to the shared structured-artifact frontmatter surface so note-derived artifact types can expose the same presentation signal.
- Remove the global note `status` property and its four-value enum.
- Make ordinary note-derived schemas reject `status`, rather than silently accepting it through `additionalProperties: true`.
- Apply the same prohibition to direct `note-base` descendants that are ordinary note artifacts, such as tag READMEs.
- Keep direct `note-base` descendants with an intentional local lifecycle, especially ADRs, on their own declared status enum.
- Add schema-resolution tests proving both sides: note-family `status` fails, `user-verified: true` passes, `user-verified: false` fails, and ADR status still passes.

This step must respect the existing schema inheritance shape: `note.schema.yaml` is inherited by most note types, while ADR and tag-README schemas currently reference `note-base.schema.yaml` directly.

### 2. Update authoring and editing contracts

- Rewrite `kb/types/note.md` around optional user attestation rather than commitment level.
- Remove status from note templates and examples; new notes start without `user-verified`.
- Update `cp-skill-write`, `cp-skill-convert`, and any packaged templates so creation or conversion never grants verification.
- Replace “seedling → current” language with the actual operations: structure an artifact, review it, and optionally obtain explicit user verification.
- Add the revocation rule to the authoring/editing instructions that can modify verified artifacts.
- Update subtype documentation such as definition and structured-claim specs where they currently inherit or repeat the global status contract.
- Preserve specialized local status documentation, notably the ADR type.

### 3. Decouple operational tooling from note status

- Remove the `status == seedling` branch from promotion-candidate generation. Reframe the report around unstructured text and, if still useful, structured artifacts lacking `user-verified`.
- Rename the review selector `--current` to `--user-verified`, filtering on committed `user-verified: true`. There is no backwards-compatibility alias.
- Keep explicit note and directory selection for reviewing unverified material. Add a broader selector only if an existing workflow cannot be expressed without it; do not infer that “all notes” and “user-verified notes” are interchangeable.
- Update the trivial-change acknowledgement command consistently. It may preserve `user-verified` only under its explicit human-authorized trivial-change semantics.
- Remove seedling counts and promotion language from deterministic validation and health/report outputs unless a replacement answers a real operational question.
- Update command references, review runbooks, architecture documentation, and tests for the renamed selection semantics.

Review acceptance and review freshness remain criterion-specific local workflow state. Neither becomes a universal verified Boolean.

### 4. Make committed verification visible in presentation

- Update the MkDocs metadata hook to render a clear “User verified” label or badge when `user-verified: true` is present.
- Retain rendering of specialized `status` values, such as ADR lifecycle status; the renderer must not assume every `status` is the removed note lifecycle.
- Confirm on a representative Markdown fixture that GitHub exposes `user-verified: true` from committed frontmatter without requiring the review database or a generated site.
- Do not add a duplicated in-body trust banner in this change. The committed frontmatter is the portable signal; MkDocs may enhance its presentation without becoming its source of truth.

### 5. Migrate repository content deliberately

- Generate the resolved-type/status inventory and separate global note statuses from specialized statuses.
- Remove `seedling` after confirming the artifact belongs to the global note lifecycle.
- Present the `current` cohort for the one-time user-attestation decision described above, then apply the confirmed mapping consistently.
- Review every `speculative` note and preserve necessary epistemic qualification in content or collection conventions before removing the field.
- Review every `outdated` note and resolve its currency/supersession information explicitly.
- Remove status from collection indexes, definitions, instructions, reference documents, source reports, fixtures, and installed templates only where those artifacts inherited the global note status.
- Apply the equivalent migration to the Epistack casebook repository separately: its collection does not need an expandable status vocabulary, and its notes begin without `user-verified` unless the user verifies them.

The sibling Epistack repository is a separate write and commit boundary; do not sweep it into the Commonplace migration commit.

### 6. Reconcile the design record

- Replace or retire the assertion-force/status proposal: its proposed residual global lifecycle is superseded by this decision.
- Update the extensible-controlled-vocabularies workshop to record that note status was removed rather than made collection-expandable.
- Rework the reader-facing-unreviewed-banner proposal: user verification is committed presentation metadata, while review state remains local and criterion-specific. Retire the proposal if the verified signal satisfies its actual presentation requirement.
- Update theory notes and collection contracts that currently use `seedling`, `current`, or `speculative` as conceptual machinery, not merely frontmatter.
- Record the implemented architectural decision in an ADR because it changes the global type contract, validation surface, rendering semantics, and command interface.

### 7. Verify and close

- Run targeted schema, validation, selector, promotion-report, rendering-hook, and review-command tests while implementing each layer.
- Run `commonplace-validate` through `cp-skill-validate` on every changed KB artifact and then on the migrated KB batch.
- Run the full `pytest` suite.
- Search for residual global lifecycle values and classify every match as intentional specialized status, historical discussion, fixture, URL, or missed migration.
- Build the documentation site and inspect representative unverified, user-verified, and ADR pages.
- Commit in reviewable slices: schema/type contract; tooling and tests; content migration; documentation/design reconciliation; Epistack migration in its own repository.
- Promote durable conclusions, delete this workshop and temporary inventories, and remove its entry from `kb/work/README.md`.

## Acceptance criteria

- Ordinary note-family artifacts reject global `status` and accept only optional `user-verified: true`.
- ADR and review-job statuses continue to work unchanged.
- No creation workflow grants user verification implicitly.
- Substantive editing instructions revoke user verification; trivial preservation is explicitly authorized rather than inferred.
- GitHub-visible committed Markdown carries the verification assertion without access to local review state.
- MkDocs visibly distinguishes user-verified artifacts while still showing specialized statuses.
- Review selection no longer relies on `status: current`.
- Every former `speculative` and `outdated` artifact has an explicit, reviewed disposition.
- No old `current` artifact is represented as user-verified without user confirmation of that migration cohort.
- Deterministic validation and the full test suite pass.

## Non-goals

- Computing verification from review acceptance or freshness.
- Making note status collection-expandable.
- Introducing a global maturity, currency, confidence, endorsement, or supersession field.
- Recording verifier identity, verification time, or a content digest.
- Treating user verification as proof that every claim is true; it is an explicit human attestation to the artifact as written.
- Renaming unrelated status concepts merely because they use the same word.
