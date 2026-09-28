---
description: "Draft ADR for typed directory artifacts: a shared schema owns membership rules; ARTIFACT.yaml identifies the type and records instance metadata"
type: reference/types/adr.md
---

# ADR draft — Typed directory artifacts

**Status:** Draft — design direction agreed; not implemented.
**Date:** 2026-09-28

Resolve the open choices and pass the acceptance checks before promoting
this draft to a numbered ADR.

## Context

Individually valid documents can form an invalid set: a member may be
missing, members may describe different runs, or a reference in one may
lack a declaration in another. The first production instance is an
agentic-system analysis, whose complete output consists of an overview,
runtime report, memory report and epistemic report.

The [validation contract](../../reference/validation-contract.md) already
combines JSON Schema over parsed documents with imperative type rules.
Extending that model to directories lets explicit validation, collection
sweeps and workflow consumers enforce the same set contract. The model
must accommodate other member names and counts without requiring the
analysis workflow's exact-version guarantees everywhere.

## Decision

A directory artifact is a set of local Markdown documents with its own
path-valued type. Use a small Commonplace-specific format, JSON Schema
for declarative constraints, and ordinary file validation for its parts.

### Recognition and type identity

A fixed-name `ARTIFACT.yaml` at the directory root identifies the artifact,
independently of member filenames. Call it the manifest. Its `type` names
a Commonplace type spec; the spec's `schema` field resolves the shared
`.schema.yaml` used by every instance of that type. Type specs remain
typed `types/type-spec.md`. Existing type resolution and collection
eligibility apply, including global types and the workshop staging
exception.

The manifest contains instance metadata, such as member hashes keyed by
path. It does not repeat or override the schema's rules. A type requiring
no instance metadata can have a manifest containing only `type`. Presence
of a malformed or invalid manifest fails artifact validation; successful
file checks cannot substitute for that failure.

### Membership belongs to the shared schema

The schema defines member paths, any expected types, member-count and
hash requirements, and these independent membership constraints:

| Constraint | Meaning |
|---|---|
| Required member | Must be present and satisfy its declared constraints |
| Optional member | May be absent; must satisfy its declared constraints when present |
| Closed membership | Rejects members not covered by the schema's member declarations |
| Open membership | Permits additional, undeclared members |

Here, **undeclared** means not covered by the schema's member declarations,
not absent from the manifest. For example, a schema may require
`summary.md` and permit an optional `appendix.md`. Adding `notes.md` fails
under closed membership and is allowed under open membership.

Requiredness, permission for additional members, and expected type are
separate constraints. The schema need not prescribe a type for every
member. Files need no manifest entry merely to be required, optional or
permitted; an entry is needed when instance metadata such as a required
hash must be supplied. Listing a file cannot authorize it against a
closed schema.

### Loading and schema input

The loader discovers actual files within the membership scope: the files
considered for membership under the directory's path and traversal rules.
It must include optional and undeclared files, even when they have no
manifest entry. `ARTIFACT.yaml` itself is excluded. The exact scope and
path rules remain open below.

The loader constructs one schema input object:

- `manifest`: the parsed `ARTIFACT.yaml`, preserving its instance data.
- `members`: an object keyed by relative member path. Each value uses
  `ParsedDocument.to_validation_object()`: `frontmatter`, `body`,
  `headings`, `links` and `body_dates` from the actual file.

This lets the schema constrain actual fields, including a member's
`frontmatter.type`. Manifest data cannot supply or overwrite member
content. JSON Schema does not read files; the loader supplies this object
for validation without persisting a copy of member contents.

Members must be readable and parseable. A manifest entry asserts that
its file exists, so a missing file named by such an entry fails loading
even when the schema would otherwise permit its absence. Merely declaring
an optional member in the schema makes no such assertion.

### Encoding

Both the manifest's `members` and the schema input's `members` are
mappings keyed by the member's relative path. A manifest entry holds that
member's instance metadata; the only field defined now is `sha256`, the
lowercase hexadecimal SHA-256 of the file's bytes:

```yaml
type: reports/types/<set-type>.md
members:
  overview.md:
    sha256: <64 lowercase hex digits>
  runtime.md:
    sha256: <64 lowercase hex digits>
```

Keying by path makes each file a named property, so the membership rules
are ordinary JSON Schema keywords over the actual files:

| Constraint | Schema expression |
|---|---|
| Required member | `members.required` |
| Optional member | Listed in `members.properties`, absent from `required` |
| Closed membership | `members.additionalProperties: false` |
| Open membership | `members.additionalProperties` omitted or `true` |
| Expected type | Require an object-valued `frontmatter` and its `type` field, then constrain that field with `const` or `enum` |
| Required hash | Require the manifest's member map, the member entry and its `sha256` field; conditional requirements use `if`/`then` on actual member presence |
| Membership depending on content | `if` on one member's fields, `then` require another member |

The table abbreviates nested schema locations. `properties` alone does
not require a field or reject a non-object value. Required fields need
`required` at their containing object, and object constraints need
`type: object`. A presence condition must also require the field it tests.

For example, this fragment requires two members, permits an optional
third, rejects all others, fixes the runtime report's type, and requires
both required members' hashes:

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
required: [manifest, members]
properties:
  members:
    type: object
    required: [overview.md, runtime.md]
    properties:
      overview.md: {}
      runtime.md:
        type: object
        required: [frontmatter]
        properties:
          frontmatter:
            type: object
            required: [type]
            properties:
              type: {const: types/agentic-system-runtime-report.md}
      appendix.md: {}
    additionalProperties: false
  manifest:
    type: object
    required: [type, members]
    properties:
      type: {type: string}
      members:
        type: object
        required: [overview.md, runtime.md]
        properties:
          overview.md: {$ref: '#/$defs/hashedMember'}
          runtime.md: {$ref: '#/$defs/hashedMember'}
$defs:
  hashedMember:
    type: object
    required: [sha256]
    properties:
      sha256:
        type: string
        maxLength: 64
        pattern: '^[0-9a-f]{64}$'
```

The example's requiredness checks include missing containing objects,
null frontmatter, missing type fields and entries without hashes. Schema
validation establishes hash format and presence; the loader still checks
the bytes. A manifest entry cannot authorize a forbidden member, because
`additionalProperties` applies to the discovered files, not to the
manifest. The local `$defs` entry constrains hash metadata, not a member's
document schema.

The set schema constrains only which members exist and which type each
declares. It does not `$ref` member schemas, because ordinary file
validation already applies them and a reference would validate members
twice.

JSON Schema cannot compare values across the instance. The loader
therefore checks that each manifest entry names a discovered file and
that each supplied hash matches the bytes. Imperative type rules check
agreement between members, as the next section assigns.

### ARTIFACT.yaml only adds checks

Directory and collection traversal retain all ordinary file discovery
and validation. Every file receives the checks it would receive without
the manifest: base, schema and imperative checks for typed documents,
and the existing rules for bare text. This applies to required, optional
and undeclared files, including working files such as `run-state.md`.
Ordinary file validation continues even when the manifest is invalid.

Set validation adds membership, integrity and cross-member checks.
Identity agreement, unique record declarations and cross-member reference
resolution belong to the analysis set's imperative type rules. The
framework owns loading and ordinary file validation; it does not hardcode
analysis filenames, member counts, or relationships. No executable
manifest hooks or general graph-query language are introduced.

Report the set and its members as one artifact, retaining the identity
of each failing member. Share execution so members are not validated or
counted twice. Files outside the membership scope keep their ordinary
validation and reporting. The exact CLI and JSON representation remains
open.

### Traversal and artifact checking have separate call boundaries

Directory and collection traversal discover files and schedule ordinary
file checks and artifact checks. The shared artifact-checking operation
loads one artifact's membership, validates its members and applies its
set rules. It does not start a directory traversal or validate unrelated
working files. Workflow type rules call this operation directly when
checking their outputs; they do not call the directory-validation entry
point.

The analysis membership scope must exclude run state and any other
workflow control file whose validation checks that same analysis set.
Those files still receive ordinary checks through the surrounding
traversal or explicit file validation. The scope or layout must express
this separation; the generic loader must not hide particular filenames.
The exact layout remains a discovery choice below.

All these calls share one validation-run context for the same candidate
bytes. Completed evaluations are reused so that a member reached through
both traversal and a workflow check is evaluated once. Re-entering an
evaluation still in progress fails with the dependency cycle identified;
an in-progress evaluation is never treated as a successful result.

### Integrity and the analysis instance

Hashes are optional in the generic format. The set schema decides where
they are required. An omitted hash causes no warning or failure when the
schema permits omission; every supplied hash must be well-formed and
match the actual bytes. Hashing and parsing use the same bytes. Hash
presence does not change which membership or content checks run.

For a complete analysis, the external version pin must cover the manifest
bytes and all four members, including the overview. The output layout is:

```text
<run-id>/
  ARTIFACT.yaml
  overview.md
  runtime.md
  memory.md
  epistemic.md
```

The overview is an ordinary member. The manifest does not list or hash
itself. The byte coverage above is required; its representation is still
an open choice between these alternatives:

- **Stored member hashes.** The analysis schema requires hashes for all
  four members in the manifest. An external hash of the manifest binds
  those declarations and, through verification, the member bytes. A
  mismatch identifies the changed member. Updating a member requires
  updating its manifest entry and the external pin.
- **Computed set digest.** The workflow records a digest computed from
  the manifest bytes and the sorted member paths and file hashes. The
  analysis schema need not require stored hashes, so the manifest may
  contain only `type`. Member edits require one external pin update. A
  mismatch does not identify the changed member unless the pin record
  also retains per-member hashes. Including the manifest bytes binds
  its type and any instance metadata as well as the document contents.

The shared analysis schema and pin fields must follow the selected
alternative. Neither is selected by this draft. Generic optional hashes
retain the same semantics under either alternative: a supplied hash must
still be verified. Replacing a member and any stored hash must change
the externally checked version.

The first type specs and fixtures are collection-local. The analysis set
spec and its adjacent schema belong under `kb/reports/types/`, with a
manifest type value of `reports/types/<set-type>.md`; the filename remains
to be chosen. This test scope does not restrict global directory types,
but no global type or fixture is required for this work.

### Consumer guarantees

| Consumer | Input | Required behavior |
|---|---|---|
| Explicit directory validation | Directory contents and resolved type | Runs ordinary file checks and set checks; reports member diagnostics under the artifact |
| Collection validation | Continuing file discovery | Adds each recognized set's checks without losing file coverage or counting members twice |
| Analysis publication | Candidate bytes at intended paths | Calls the shared artifact check directly and rejects an invalid candidate set |
| Analysis completion and comparison loading | Retained set and recorded workflow identity | Calls the artifact check without directory traversal; rejects an invalid set, a wrong set type, or a version different from the recorded pin |

Shared set validation replaces equivalent consumer checks. Guarantees
requiring evidence outside the set, such as frozen-source identity and
publication state, retain their workflow owners. Success establishes the
properties expressed by the deterministic rules; it does not establish
analytical truth or semantic support from quotations.

## Considered alternatives

**Keep specialized verification or anchor the set on one Markdown member.**
Specialized checks avoid a new artifact model but leave ordinary directory
validation without the set guarantee. A designated member's type rule
could check its siblings, but recognition would depend on that member.
The separate manifest provides one recognition convention and lets the
overview receive the same integrity checks as other members.

This reverses the [revised layering](../agentic-analysis-output-documents/transition-plan.md#revised-layering-2026-09-28-during-implementation)
recorded earlier on 2026-09-28, which chose "one recognition rule, not a
manifest framework, since only the analysis set has an entry type." The
analysis set is still the only production instance. The manifest is
preferred anyway for the two reasons above. Its generality is also cheap
([Encoding](#encoding)): membership rules are standard JSON Schema
keywords, so the added framework cost is the loader, not a rule language.

**Put rules in each manifest.** Instance-local schemas would allow repeated
analyses to diverge. A shared schema gives one contract per type. The
manifest name `ARTIFACT.yaml` was preferred to `MANIFEST.yaml` to emphasize
that it declares one typed artifact.

**Use an external format or directory-validation library.** The operator
initially requested an existing language, then accepted a local format
because the adapters appeared more costly than the required checks. The
2026-09-28 survey recorded these fit assessments:

| Option | Assessment |
|---|---|
| [Data Package v2](https://datapackage.org/standard/data-resource/) | Supplies paths and hashes, but its table-oriented schemas would still require Commonplace member typing and validation extensions |
| [DirSchema](https://materials-data-science-and-informatics.github.io/dirschema/main/manual/) | Directory rules and content plugins, including a [raw-byte interface](https://materials-data-science-and-informatics.github.io/dirschema/main/reference/dirschema/json/handler/), could host an adapter; the inspected [dependencies](https://github.com/Materials-Data-Science-and-Informatics/dirschema/blob/main/pyproject.toml) required Python `<3.11` and Pydantic 1 |
| [directory-schema-validator](https://github.com/jpoehnelt/directory-schema-validator) | Its directory-as-JSON representation is useful precedent; its regex content checks would still need Markdown parsing and Commonplace validation |
| [CUE](https://cuelang.org/docs/howto/validate-data-files-using-file-embedding/) | Adds a language and toolchain while still requiring Markdown extraction and imperative-check integration |
| [RO-Crate](https://github.com/ResearchObject/ro-crate/blob/main/docs/_specification/1.2/data-entities.md) | Content-profile declarations do not execute Commonplace checks; JSON-LD and a separate constraint mechanism add machinery |

These are bounded fit judgments, not a claim that no suitable library
exists. Choosing a local format makes its loading contract Commonplace's
maintenance responsibility.

**Give the schema only manifest data.** Code would have to compare all
member content itself, and manifest-only discovery would miss undeclared
files. Supplying actual parsed members lets the shared schema constrain
the directory contents.

**Require hashes universally.** Editable sets may need structure and
consistency checks without exact-version upkeep. Hash requirements
therefore belong to individual set types.

## Consequences

Operators gain one validation target for a complete artifact, and
consumers share its checks. Authors can define membership requirements
without changing framework code. Commonplace takes on directory loading,
path handling and grouped diagnostics as maintained contracts.

A shared-schema revision changes the rules applied to existing instances.
Member hashes pin content, not the validation method. Reproducing an
analysis's historical validation requires the types, schemas and code
from its recorded `inputs-commit`; validating it under the current method
answers a different question.

The first version covers local Markdown sets with arbitrary member names
and counts, required and optional members, open and closed membership,
and optional hashes. It does not cover nested directory artifacts,
automatic migration of existing sidecar pairs, change-triggered
revalidation or freshness registration. The latter remain separate
proposals: [collection-as-artifact freshness](../../reference/proposals/collection-as-artifact-freshness.md)
and [generalized validation invalidation and imperative extension](../../reference/proposals/generalized-validation-invalidation-and-imperative-extension.md).

## Open choices before implementation

1. **Discovery and paths.** Define the membership scope, subdirectory and
   non-Markdown handling, duplicate paths, symlinks and containment.
   Discovery must expose undeclared files before the schema decides
   whether they are allowed. Resolve the scope or layout that keeps
   workflow control files such as `run-state.md` outside the analysis
   membership while preserving their ordinary traversal checks.
2. **Reporting.** Define the CLI and `analysed_artifacts` JSON path/type
   representation, member diagnostics, and direct validation of a single
   member. The validator's default messages for `maxProperties`,
   `minProperties` and object-level `not` print the whole `members` object,
   including bodies; reporting must shorten them, or such checks move to
   imperative rules.
3. **Analysis integration.** Choose the set type filename and one of the
   [integrity representations](#integrity-and-the-analysis-instance).
   Define its schema requirements, external pin fields and exact digest
   encoding. Specify their use in publication, completion and comparison
   loading, including current-method versus historical validation. Resolve
   the update cost with the output-documents workshop's open init-repin
   item; stored member hashes and a computed digest have different costs.

These choices complete the agreed model; they do not reopen its
allocation of rules to the schema or its preservation of ordinary checks.

## Acceptance checks before promotion

Use the real analysis set and collection-local fixtures. Fixtures may
prove generality; no second production type is required. Demonstrate the
format before implementation, then enforce these cases with tests.

| Area | Required cases |
|---|---|
| Recognition and coverage | A malformed or invalid manifest fails even when files pass. With either a valid or invalid manifest, failures in a declared member and an undeclared file remain visible through directory validation and collection sweeps. Members are not counted or validated twice. |
| Required and optional members | Under both membership policies, missing required files fail, absent optional files pass, and present optional files receive their declared checks even without manifest entries. |
| Required fields in the schema example | Missing or non-object containing values fail. Bare runtime Markdown, null frontmatter, an omitted type field and an incorrect type fail. A missing manifest member map, missing hash entries and entries without `sha256` fail. |
| Open and closed membership | The same extra file is allowed by an open schema and rejected by a closed one. A manifest entry cannot authorize a forbidden member. An invalid extra note still fails ordinary checks under open membership. |
| Minimal manifest | For a type requiring no instance metadata, a manifest containing only `type` still enables all membership checks against actual files. |
| Generality and type resolution | Different filenames and fewer and more than four members work without framework changes. Collection eligibility and workshop staging rules hold. Two instances with different hashes use the same type and shared schema. |
| Integrity | Permitted hash omissions pass; missing required hashes and malformed or mismatched supplied hashes fail. Content checks run with and without hashes. |
| Analysis contract | A complete four-member set passes under the selected integrity representation. The external pin covers the manifest and all members, including the overview. Changing a member, its path, the manifest type or other manifest metadata changes the checked version. Missing members, wrong types, invalid content despite a correct type declaration, mixed identities, duplicate IDs and unresolved references fail. |
| Consumer agreement | Directory validation, sweeps and workflow consumers agree on set validity. Publication checks candidate bytes; completion and comparison loading check the expected type and version. Workflow guarantees outside the set remain enforced. |
| Validation call boundaries | Directory and collection validation with a complete run state terminate without repeated member checks. Direct run-state validation reaches the same artifact checks without starting traversal. Invalid members and invalid workflow files remain visible. An actual dependency cycle fails explicitly rather than recursing or silently passing. |
| Resolved loading contract | Path and diagnostic fixtures cover the choices above, and equivalent checks have one owner. |
