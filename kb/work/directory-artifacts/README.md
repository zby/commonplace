# Directory artifacts: validating a set of documents as one artifact

## Commission

Posed by the operator on 2026-09-28. Commonplace validates one Markdown
document at a time: a `type:` line names a type spec, the spec's schema
states the document's structure, and type rules in the validator add what
a schema cannot express. The agentic-system analysis output is becoming a
set of four typed documents in one run directory, whose integrity (a
manifest of member hashes, identity agreement, identifiers declared once
across members, a profile citing records another member declares) is a
property of the set, not of any member. During the transition the
operator directed that these checks become a validator type rule on the
set's entry document and that a run directory validate as one artifact,
then judged that extending validation from single notes to directories
is an architectural change to the validator's model and must be planned
before it is implemented. This workshop owns that planning.

A candidate implementation exists as commit `6d8d9fd0` ("Check the
analysis set through a type rule on the overview"), made under the
mid-flight direction and reverted in `597055b5`. It is evidence of what
the change touches, not a decision: a set rule in `validation.py`,
directory-to-overview resolution in `project_paths.py`, a sweep that
yields the overview for such a directory, and consumers (publication, the
comparison loader) calling validate instead of re-checking. Its
recognition rule (a directory whose `overview.md` carries the overview
type) and its manifest location (the overview's `members` field) are
superseded by the chosen path below.

## Question

How should the validator model an artifact composed of several typed
documents in one directory, so that validating the directory gives the
same guarantees as validating a note? The operator's constraint: reuse an
existing language for the directory spec instead of inventing one.

## Chosen path (2026-09-28)

A directory artifact is described by a
[Frictionless Data Package v2](https://datapackage.org/standard/data-resource/)
descriptor, constrained by a JSON Schema profile, with Commonplace adding
only the member-type check and the cross-member type rules.

| Concern | Carried by |
|---|---|
| Recognition: this directory is one artifact | the standard descriptor filename, `datapackage.json` |
| Which files the set contains, at which paths, of which declared types, how many | a JSON Schema profile of the descriptor (existing languages) |
| Existence and integrity of each file | Data Package `path` and `hash` semantics |
| Each file has its declared type and conforms to it | the validator: one comparison, then ordinary note validation |
| Value equality and citation resolution across members | type rules (code) |

- **Recognition.** A directory containing `datapackage.json` is one
  artifact. The filename is hardcoded, as `COLLECTION.md`, `README.md`
  and `SKILL.md` are; the type spec does not declare it.
- **Manifest.** The descriptor lists each member as a resource with
  `path` and `hash` (`sha256:`-prefixed; the standard's default is MD5).
  The standard permits extra properties, so each resource carries
  `commonplace_type`, the member's expected type; the standard's own
  `type` property means something else (`"table"`). The manifest leaves
  the overview's frontmatter: the overview becomes an ordinary member,
  and the descriptor pins its hash like any other member's.
- **Directory spec.** The set type's profile is a JSON Schema over the
  descriptor, extending the base Data Package schema and stored in
  `kb/types/`. It requires resources by path and declared type, and
  states cardinality with `contains`, `minContains` and `maxContains`.
  Validating it reuses the JSON Schema pipeline notes already use.
- **Member conformance.** Data Package constrains file content only for
  tabular resources (Table Schema), so this step is Commonplace's. The
  validator reads each member's `type:` value, compares it with
  `commonplace_type`, and validates the member under that type. Member
  findings are reported under the directory artifact, naming the member.
- **Cross-member checks.** Identity agreement across members, identifiers
  declared once, and record-citation resolution cannot be written in
  JSON Schema. They stay imperative type rules of the set type, as the
  [validation contract](../../reference/validation-contract.md) already
  places referential checks.
- **Dependency.** The `frictionless` library is optional. Checking hashes
  and validating the descriptor against a JSON Schema are small, so the
  language can be adopted without the library unless the library earns
  its place.

Rejected alternatives:

- **dirschema**, a path-regex plus JSON Schema directory language, fits
  the problem closely but has one release (0.1.0, May 2023), requires
  Python `<3.11` and pins `pydantic<2`, so it cannot be installed here.
- **RO-Crate with SHACL** could express cross-member equality
  declaratively, but brings JSON-LD, schema.org vocabulary and a second
  constraint language for checks a type rule already covers.
- **BagIt** covers hashes only, with no member typing.
- **A home-grown manifest** (`MANIFEST.yaml`, or `members` in the
  overview's frontmatter) was dropped in favour of the standard
  descriptor.

## Open questions

1. **How the descriptor names its set type.** Type rules dispatch by
   type-spec path (ADR 048). Leaning: a package-level `commonplace_type`
   names a set type spec whose `schema:` is the profile, keeping one
   identity mechanism; the descriptor's `$schema` may also name the
   profile for external tools. To settle before implementation.
2. **What `commonplace-validate <dir>` and a collection sweep report.**
   One artifact per descriptor; members are not also reported as
   standalone notes. The exact JSON envelope entry (`analysed_artifacts`
   path and type) is undecided.
3. **Second instance.** Whether skill directories (open membership, no
   hashes) should test the model. They would need an open-set profile
   and hash-free resources; `SKILL.md` stays as the external standard
   requires.
4. **Nesting.** Whether a directory artifact may contain another. Default:
   no.
5. **Sidecar pairs.** Whether the write-brief and snapshot-pairing base
   rules should migrate onto the model; a clean migration would be
   evidence the model is general.
6. **Source.** Ingest the Data Package v2 specification into
   `kb/sources/` so the ADR cites it rather than this summary.

## Boundary and inputs

The analysis set is the first instance and the evaluation boundary: the
design must serve it and must not be sized for instances that do not
exist. A second instance enters only if it already exists in the
repository (open question 3). Inputs: the
[transition plan](../agentic-analysis-output-documents/transition-plan.md)
and its revised-layering section; the
[consumer inventory](../agentic-analysis-output-documents/consumer-inventory-20260928.md);
the member type specs under `kb/types/`; the
[type-spec contract](../../types/type-spec.md) and the
[validation contract](../../reference/validation-contract.md); commit
`6d8d9fd0` and its tests. The operator has also asked for a review of the
analysis code's size and its redundant checks, which this workshop may
inform but does not own.

Coupling: the [output-documents workshop](../agentic-analysis-output-documents/README.md)
owns the set design and the producer transition, whose remaining commits
proceed on the approved plan with set checks in run-state verification.
Moving the manifest from the overview's `members` field into
`datapackage.json` changes that set design; it is applied when this
workshop's ADR lands, not before. The refresh batch in
`kb/work/agentic-memory-refresh/batch-01-handoff.md` waits on that
transition, not on this workshop.

## Closure

Close when an ADR records the directory-artifact model, its
implementation has landed with tests, the analysis set validates through
it from a clean checkout, and the redundant checks it replaces in
run-state verification, publication and the comparison loader have been
removed. If the decision is to keep set checks outside the validator,
record that and close without implementation.
