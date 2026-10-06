---
description: "Proposal: a directory type declares the layout of its instances, so membership, roles and cross-member relations come from one external definition instead of filename conventions and code."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Directory types declare their layout

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 111](../../adr/111-directory-types-declare-their-layout.md): the [analysis set type](../../../agentic-system-analyses/types/agentic-system-analysis-set.md) declares the layout and the validation contract describes layout checks. The pre-adoption state, in which the boundary sat outside the artifact and member names were repeated across seven modules, and the candidate vocabulary remain here — design texture only.

A directory type is defined outside its instances: a manifest points at a
type spec, and the type spec names a schema. That definition cannot describe
the directory. It sees a flat set of sibling Markdown files and encodes
everything else, roles, completeness and relations, in filename conventions,
schema branches and Python keyed by type path.

This proposal gives the directory type a layout: a declared set of files
beside the manifest, each with a role, and for each role the expected
document type, when it is required, and how it relates to other roles.
Membership becomes "matches a layout entry". Whole-set validation,
member-level validation, manifest construction and workflow code read the
same declaration.

The operator selected this design on 2026-10-06. It is not shipped behavior.
The companion proposal
[document validation in working-set context](../type-declared-cross-checks-and-one-validation-surface.md)
depends on this one; this one does not depend on it.

## Current state (as of 2026-10-06)

- [ADR 095](../../adr/095-directory-artifacts-add-shared-set-validation.md)
  recognizes a directory artifact by `ARTIFACT.yaml` at its root. Membership
  is visible Markdown files directly beside the manifest. `member_paths` in
  `src/commonplace/lib/directory_artifact.py` keeps direct children only.
- The type's schema receives `{manifest, members}`. The one directory type,
  the [analysis set](../../../agentic-system-analyses/types/agentic-system-analysis-set.md),
  encodes each role as a `members.properties.<filename>` entry with a
  constant document type, encodes completeness as an if/then on the
  overview's `result-disposition`, and requires a hash per manifest entry.
- Cross-member relations, identity agreement, record-reference resolution and
  comparison-field checks, are Python rules registered per directory type path
  in `src/commonplace/lib/validation.py`. They run only on whole directories.
- The analysis run's working artifact is `output/`, with its manifest at
  `output/ARTIFACT.yaml`. The run root beside it holds process files: run
  state, the frozen source record, every report version, round files and job
  workspaces. The boundary, `boundary.md`, is also at the run root, outside
  the artifact. Before synthesis, workflow code and one type rule substitute
  it for the absent overview by path convention.
- Publication in `src/commonplace/lib/agentic_publication.py` copies the
  `output/` members into `retained/<system>/`, the same flat shape. The
  retained set has no `boundary.md`; the overview embeds the boundary's two
  sections verbatim at assembly, and the whole-set identity check reads run
  and boundary identity from the overview.
- Layout facts are repeated in code. Member filenames are hard-coded in
  `src/commonplace/lib/agentic_set.py` (member-name constants and the
  `memory.md` probe), `agentic_finalize.py` (the set names), `agentic_workflow.py`
  (slot constants and `boundary.md`), `agentic_records.py` (the overview as
  source-register holder), `systems_matrix.py` and `validation.py` (the
  hand-written profile exclusion, the reconciliation lookup and the boundary
  path substitution), and `analysis_worktree.py` and `agentic_publication.py`
  (the overview as publication destination). The schema's filename properties
  state the same facts again.

## Problem

The external definition does not own the directory it defines:

- The analysis set's declaration source, the boundary, is written outside
  the artifact, so its identity and declarations reach the set only through
  code that substitutes it for the absent overview. Nothing in the definition
  says it belongs to the set.
- Roles exist only as filenames. A member's relations to other members, who
  supplies its identity, whose declarations it may cite, are nowhere in the
  definition and must be code.
- Completeness is a schema branch on one member's field. A second directory
  type with a different completion rule writes a second idiom.
- Every consumer that needs layout facts restates them, and they can drift.

A single member checked in its set's context, which the companion proposal
describes, needs a role lookup and per-role relations. Neither can be built on
a definition that does not describe the directory.

## Design

### The layout

The directory type's spec carries a `layout` in its frontmatter. A layout is
a set of roles keyed by name. Each role states:

- `path`: a literal filename beside the manifest. Membership stays direct
  children of the manifest's directory, as ADR 095 has it. No pattern form
  until a type needs one.
- `type`: the expected document type at that slot, compared with the member's
  own `type:` declaration, so each fact has one owner.
- when the slot is required, as a condition the validator evaluates from the
  instance, such as another member's field value.
- `identity`: one or more sources, each a role and the fields this member
  must repeat verbatim from it. A member may take run identity from one role
  and another field from a second, as the memory profile does today.
- `cites`: the roles whose declarations resolve this member's references. A
  role may list itself.

Membership is matching a layout entry. A Markdown file beside the manifest
that matches no entry is governed by the type's open or closed policy.

The manifest keeps its ADR 095 role: recognition marker, instance metadata
and hash requirements. Its schema stays JSON Schema and no longer lists
filenames. The layout says nothing about content identity: which members a
frozen instance pins belongs to publication integrity and freezing, and a
supplied hash always binds.

Relations split between data and code. Identity agreement and citation scope
are declared. Record-ID grammar, quotation anchoring and comparison-field
validation stay imperative, registered per role rather than per type path.

### Working instances

- **A working instance declares itself from the first write.** The workflow
  writes a type-only manifest when it creates the artifact root and lets its
  finishing step overwrite it with pinned metadata. Recognition works
  throughout the instance's life. A replay must see no change from writing
  it.
- **Whole-set validation of an incomplete instance is informative.** Absent
  required members are one finding class. Relation checks run over the
  members present. A working manifest without hashes fails whole-set
  validation until the set is complete, which is correct and needs no phase
  concept.
- **Findings carry the role they belong to.** A dangling reference belongs to
  the citing role, an identity mismatch to the member that disagrees, a
  duplicate declaration to each declaring role. A caller that wants one
  member's findings filters by role.

These let the workflow replace its private set-check code with one directory
validation and a role filter before the companion proposal's member mode
exists.

### The analysis set

The layout decisions for the set are below. The workflow's acceptance,
round-close and publication code moved onto the layout on 2026-10-06. The
remaining adoption, the synthesis and verifications as members, the overview
thinned to an entry page and drafts checked through `commonplace-validate`,
is specified in
[adopting the declared layout in the analysis workflow](../adopt-declared-layout-in-the-analysis-workflow.md).

- **The boundary moves into `output/`.** Setup creates `output/` with the
  type-only manifest and the boundary job writes `output/boundary.md` as the
  first member. The working and retained instances then have one flat
  layout, and the artifact stays drawn around the product rather than the
  run directory. A withheld run already produces an overview-only `output/`,
  and its disposition comes from the boundary the job wrote, so the boundary
  is present and `required.always` holds. A boundary job that is refused
  outright writes nothing and the run does not close; its `output/` is an
  incomplete working instance in gitignored state, which is the expected
  shape of a failed run.
- **Publication copies the boundary** with the other members. No fallback to
  the overview is carried in the type.
- **The boundary owns source declarations.** After assembly the overview and
  the boundary both carry the source register. The boundary is the declaring
  role; the overview's embedded sections are a copy, which whole-set
  validation checks against its source instead of treating as a second
  declaration.
- **The one retained set is regenerated** by a fresh run rather than migrated
  or tolerated. Its original boundary file is not recoverable, and the
  boundary type's `source` block is absent from the overview.
- **Legacy sets are out of scope.** Four tracked manifests under
  `kb/agentic-systems/reports/retained/` and `retained-archive/` declare
  type paths that no longer exist and already fail validation. Their
  collection calls that tree frozen history from before the analysis
  collection. The layout changes nothing for them.

### Illustration

One candidate vocabulary; the keys and their spelling are free choices.

```yaml
type: types/type-spec.md
name: agentic-system-analysis-set
schema: ./agentic-system-analysis-set.schema.yaml   # manifest metadata and hashes
layout:
  roles:
    boundary:
      path: boundary.md
      type: agentic-system-analyses/types/agentic-system-boundary.md
    overview:
      path: overview.md
      type: agentic-system-analyses/types/agentic-system-analysis-overview.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
    runtime:
      path: runtime.md
      type: agentic-system-analyses/types/agentic-system-runtime-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory:
      path: memory.md
      type: agentic-system-analyses/types/agent-memory-analysis-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    epistemic:
      path: epistemic.md
      type: agentic-system-analyses/types/agentic-system-epistemic-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    reconciliation:
      path: reconciliation.md
      type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory-profile:
      path: memory-profile.md
      type: agentic-system-analyses/types/agent-memory-profile.md
      identity:
        - {from: boundary, fields: [run-id, reviewed-boundary]}
        - {from: memory, fields: [source-identity]}
      cites: [runtime, memory, epistemic]
  required:
    always: [boundary, overview]
    by: {role: overview, field: result-disposition}
    complete: [runtime, memory, epistemic, reconciliation, memory-profile]
```

`required` has one discriminator and per-value lists, mirroring the schema
branch the set uses today; a value with no list requires only `always`. The
set is closed, as its schema is today. Manifest construction lists the roles
present. Workflow slot constants become lookups into `roles`.

The identity entries reproduce today's check in full. `set_identity_errors`
in `src/commonplace/lib/agentic_set.py` requires every member, the
reconciliation and the profile included, to carry the overview's run and
boundary identity, and the profile to match the memory report's source
identity. With the boundary a member, the boundary becomes the source of run
identity and the overview is checked against it like every other member;
today the overview is the reference because the boundary is not in the set.

### Consumers

The validator's directory path, manifest construction, the finalize step,
the analysis workflow's slot constants and its round-close record check, and
any future directory type. No consumer reads a layout today; the layout
reader must be built. The oracle is the actual files at declared paths and
their declared facts: deterministic success establishes declared structure,
not analytical truth.

## Consequences

What becomes checkable through the type, without the companion proposal:

- Membership and completeness by disposition validate from the declaration
  instead of the schema's filename properties. Same checks, one owner.
- Boundary agreement moves from workflow code into the type. With the boundary
  a member and the identity source, whole-set validation checks run and
  boundary identity directly, before synthesis and without the overview.
- Citation resolution becomes role-scoped. The profile citing a source
  directly, or a report citing a role outside its scope, is a type finding.
  Today the pooled checker cannot see scope and the profile is excluded by
  hand.
- A mid-run directory validation reports relation findings per role. The
  workflow's round-close record check, its private body assembly and the
  memory-profile rule's path heuristic retire in favour of one directory
  validation and a role filter.
- The hard-coded member filenames listed under current state go, except
  where code names the overview as the publication entry point under ADR 102;
  those become lookups of the entry role rather than deletions.
- A reader of the type spec sees what an instance contains.

What it costs:

- An ADR amending ADR 095: layout as the owner of membership, the manifest
  schema reduced to instance metadata and hashes, the type-only working
  manifest, and partial-instance validation semantics. The ADR records the
  alternatives below.
- The validation contract, the type-spec contract and the set type document
  are rewritten for directory types.
- The retained set is regenerated and the publication step copies one more
  file.

## Alternatives considered

For the implementing ADR to record.

- **Layout in the schema file under a reserved keyword.** Rejected: hides a
  layout vocabulary inside a JSON Schema document whose validator ignores it.
- **Layout in a separate file named by the type spec.** Rejected while one
  directory type exists: one more file and one more resolution step for no
  separation the frontmatter does not give.
- **All relations in code keyed by role.** Rejected: member mode would still
  need the rule set to know what a role relates to, so the layout would be
  the schema's filename properties renamed.
- **A constraint language.** Rejected, as in ADR 095 and the
  [type-selected Python validation proposal](../type-selected-python-validation-checks.md).
- **Hashing as a layout property.** Rejected: content identity is not
  structure, and a role-level flag would need a phase concept to let working
  instances validate.
- **Nested paths in one artifact.** Deferred. A path could descend into
  subdirectories without manifests of their own. It needs the direct-children
  rule amended and a membership policy scoped to declared directories, and
  the only use found, reaching the boundary by moving the manifest to the
  run root, draws the artifact around the run directory instead of the
  product. Reopen when a type needs a subdirectory of members.
- **Nested directory artifacts.** Left aside, not designed. The analysis run
  shows the shape that may be wanted: a run directory that is itself an
  artifact, holding its process files and, as a member, the product artifact
  it publishes. That is composition of artifacts, a different question from
  layout.
- **Manifest at the run root, members under `output/`, retained tree
  reshaped to match.** Rejected: the artifact would be the run directory with
  process files inside it as tolerated non-members, and the retained tree
  would carry `output/` into the library and move every link to a retained
  overview.
- **Boundary stays outside the artifact, with a fallback to the overview.**
  Rejected: the declaration source stays outside the definition, and the
  companion proposal would have to let a type name external context.

## Free choices

The layout's key vocabulary, the form of the requiredness condition and how
roles key imperative rules. Start from the analysis set's six reports, its
boundary and its disposition-based completeness, and declare nothing the set
does not need. Until the workflow reads the layout, two statements of the
member names coexist; retire the code constants rather than adding a third
copy.

## Adoption criteria

A candidate implementation must demonstrate that:

- A directory type declares its members by filename with roles, and the
  validator derives membership and requiredness from that declaration rather
  than from the schema's filename properties.
- The boundary is written inside `output/` and declared as a member of the
  analysis set, and the working and retained instances validate under the
  same layout.
- A role's declared relations are applied by whole-set validation and are
  available to a member-level lookup by filename.
- Manifest construction and the analysis workflow's slot handling read the
  layout, and their member-name constants are retired.
- The analysis set validates as it does today, including completeness by
  disposition, with its layout declared rather than coded and its hash
  binding unchanged.
- Publication copies the boundary into the retained set, the overview's
  embedded boundary sections are checked against it, and the regenerated
  retained set passes.
- Deterministic success establishes the declared structure, not analytical
  truth or semantic support.
