---
description: "Proposal: a directory type declares the layout of its instances, so membership, roles and cross-member relations come from one external definition instead of filename conventions and code."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Directory types declare their layout

A directory type is already defined outside its instances: a manifest points
at a type spec, and the type spec names a schema. What that definition cannot
do is describe the directory. It sees a flat set of sibling Markdown files and
encodes everything else, roles, completeness and relations, in
filename conventions, schema branches and Python keyed by type path.

This proposal gives the directory type a layout: a declared set of files
beside the manifest, each with a role, and for each role the expected document
type, when it is required, and how it relates to other roles. Membership becomes "matches a layout entry". Whole-set validation,
member-level validation, manifest construction and workflow code would all
read the same declaration.

The operator selected this direction. It is not shipped behavior or an
implementation commission. The companion proposal
[document validation in working-set context](./type-declared-cross-checks-and-one-validation-surface.md)
depends on this one; this one does not depend on it.

## Current state (as of 2026-10-06)

- [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md)
  recognizes a directory artifact by `ARTIFACT.yaml` at its root. Membership
  is visible Markdown files directly beside the manifest; descendants are
  outside membership, and the ADR names nested membership as deferred, not
  foreclosed. `member_paths` in `src/commonplace/lib/directory_artifact.py`
  iterates one directory and keeps direct children only.
- The type's schema receives `{manifest, members}`. The one existing
  directory type, the
  [analysis set](../../agentic-system-analyses/types/agentic-system-analysis-set.md),
  encodes each role as a `members.properties.<filename>` entry with a
  constant document type, and encodes completeness as an if/then on the
  overview's `result-disposition`. Hash requirements are per manifest entry.
- Cross-member relations, identity agreement, record-reference resolution and
  comparison-field checks, are Python rules registered per directory type path
  in `src/commonplace/lib/validation.py`. They run only on whole directories.
- The analysis run's working artifact is `output/`, with its manifest at
  `output/ARTIFACT.yaml`. The run keeps its source register in `boundary.md`
  at the run root beside `output/`, outside the artifact. Before synthesis,
  workflow code and one type rule substitute it for the absent overview by
  path convention.
- Publication in `src/commonplace/lib/agentic_publication.py` copies the
  output members into `retained/<system>/`. The retained set has no
  `boundary.md`; the overview embeds the boundary's two sections verbatim at
  assembly, and the whole-set identity check reads run and boundary identity
  from the overview.
- Layout facts are repeated in code: member-name constants in
  `src/commonplace/lib/agentic_set.py` and `agentic_finalize.py`, the
  current-slot map in `src/commonplace/lib/agentic_workflow.py`, and the
  schema's filename properties each state which files make the set.
- ADR 095 considered and rejected external directory formats such as Data
  Package, DirSchema and RO-Crate, because their adapters would still need
  Commonplace's Markdown representation, type resolution and imperative checks.

## Problem

The external definition does not own the directory it defines. Four
consequences follow:

- The analysis set's declaration source, the boundary, is written outside
  the artifact, so its identity and declarations reach the set only through
  code that substitutes it for the absent overview. Nothing in the definition
  says it belongs to the set.
- Roles exist only as filenames. A member's relations to other members, who
  supplies its identity, whose declarations it may cite, are nowhere in the
  definition and must be code.
- Completeness is a schema branch on one member's field. A second directory
  type with a different completion rule writes a second idiom.
- Every consumer that needs layout facts restates them. The schema, the
  finalize step, the workflow and the set module each list the member names,
  and they can drift.

A single member checked in its set's context, which the companion proposal
describes, needs a role lookup and per-role relations. Neither can be built on
a definition that does not describe the directory.

## Selected direction: a layout in the directory type

The directory type declares its layout. Conceptually a layout is a list of
entries, each binding a filename beside the manifest to a role. A role
states:

- the expected document type at that slot, checked against the member's own
  `type:` declaration, so each fact has one owner;
- when the slot is required, as a condition the validator can evaluate from
  the instance, such as another member's field value;
- relations to other roles: which role supplies identity fields this member
  must repeat, and which roles' declarations this member may cite.

Membership is matching a layout entry. A Markdown file beside the manifest
that matches no entry is governed by the type's open or closed policy.
Membership stays flat, as ADR 095 has it: the analysis set's boundary moves
into the artifact root instead of the root moving up to meet it, so the
working instance and the retained instance have one shape.

The manifest keeps its ADR 095 role: recognition marker and instance metadata.
It does not restate layout.

Consumers read the layout instead of restating it. Whole-set validation
derives required members from it. Manifest construction derives the member
names from it. Workflow slot maps derive from it. Member
mode, in the companion proposal, resolves a file's role from its filename
beside its manifest and applies the role's relations.

Relations split between data and code. Identity agreement and citation scope
are simple enough to declare. Record-ID grammar, quotation anchoring and
comparison-field validation stay imperative, registered per role rather than
per type path. The split is stated in the type, not hidden in the rule set.

Three further decisions make the layout useful before any member-level
validation exists:

- **A working instance declares itself from the first write.** A workflow
  that builds a directory artifact writes a type-only manifest when it creates
  the artifact root and lets its finishing step overwrite it with pinned
  metadata. Recognition then works throughout the instance's life, not only
  at the end.
- **Whole-set validation of an incomplete instance is informative.** Required
  members that are absent are one finding class. Relation checks, identity
  agreement and citation resolution, run over the members that are present.
  A coordinator can validate the working directory mid-run and read the
  relation findings while treating the missing-member findings as expected.
- **Findings carry the role they belong to.** A relation finding names the
  role whose member it is about: a dangling reference belongs to the citing
  role, an identity mismatch to the member that disagrees, a duplicate
  declaration to each declaring role. A caller that wants one member's
  findings filters by role.

Together these let a workflow replace its private set-check code with one
directory validation and a filter, before the companion proposal's member
mode exists. Member mode then adds what filtering cannot: reading only the
context a role needs, checking scratch bytes at an intended destination, and
failing explicitly when context is unusable instead of reporting the context's
own defects.

### Illustration

The analysis set in one candidate vocabulary, as the type spec's frontmatter
would carry it. This is an illustration of the decisions above, not a shipped
format; the keys and their spelling are free choices.

```yaml
type: types/type-spec.md
name: agentic-system-analysis-set
schema: ./agentic-system-analysis-set.schema.yaml   # manifest metadata and hashes
layout:
  roles:
    boundary:
      path: boundary.md
      type: agentic-system-analyses/types/agentic-system-analysis-boundary.md
    overview:
      path: overview.md
      type: agentic-system-analyses/types/agentic-system-analysis-overview.md
    runtime:
      path: runtime.md
      type: agentic-system-analyses/types/agentic-system-runtime-report.md
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory:
      path: memory.md
      type: agentic-system-analyses/types/agent-memory-analysis-report.md
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    epistemic:
      path: epistemic.md
      type: agentic-system-analyses/types/agentic-system-epistemic-report.md
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    reconciliation:
      path: reconciliation.md
      type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
      cites: [boundary, runtime, memory, epistemic]
    memory-profile:
      path: memory-profile.md
      type: agentic-system-analyses/types/agent-memory-profile.md
      identity: {from: memory, fields: [source-identity]}
      cites: [runtime, memory, epistemic]
  required:
    always: [boundary, overview]
    by: {role: overview, field: result-disposition}
    complete: [runtime, memory, epistemic, reconciliation, memory-profile]
```

What each key decides:

- `roles` are keyed by name; imperative rules and member-level findings use
  the name. `path` is a literal filename; no pattern form until a type
  needs one.
- `type` is the expected type at the slot, compared with the member's own
  `type:` declaration.
- `identity` names the role whose listed fields this member must repeat
  verbatim.
- `cites` is the citation scope: the roles whose declarations resolve this
  member's references. A role may list itself.
- `required` has one discriminator and per-value lists, mirroring the schema
  branch the set uses today. A value with no list requires only `always`.
- The set is closed, as its schema is today: an undeclared Markdown file
  beside the manifest fails. Run state, report versions and job workspaces
  live at the run root, outside the artifact.

A member lookup finds the manifest in the member's own directory. Manifest
construction lists the roles present. Workflow slot
constants become lookups into `roles`. Hash requirements stay in the manifest
schema, as today; the layout says nothing about content identity.

### Operativity

Consumers would be the validator's directory path, the finalize step, the
analysis workflow's slot constants and its round-close record check, and any
future directory type. No consumer reads a layout today; the layout
representation and its reader must be built. The oracle is the actual files
at declared paths and their declared facts. Membership stays within ADR 095's
direct-children rule; the amending decision covers what the layout takes over
from the schema and from code.

## Consequences of adoption on its own

What becomes checkable through the type, without the companion proposal:

- The analysis set's membership and completeness by disposition validate from
  the declaration instead of the schema's filename properties. Same checks,
  one owner. Hash binding is unchanged and stays with the manifest schema.
- Boundary agreement moves from workflow code into the type. With the boundary
  a member and named as the identity source, whole-set validation checks run
  and boundary identity directly, before synthesis and without the overview.
- Citation resolution becomes role-scoped. The profile citing a source
  directly, or a report citing a role outside its scope, is a type finding.
  Today the pooled checker cannot see scope and the profile is excluded by
  hand.
- A mid-run directory validation reports relation findings per role on the
  members present. The workflow's round-close record check, its private body
  assembly and the memory-profile rule's path heuristic can be retired in
  favour of one directory validation and a role filter.
- Manifest construction and workflow slot handling read the layout, and the
  member-name constants in four modules go.
- A reader of the type spec sees what an instance contains, which the type
  spec contract already asks of a type for its non-validator readers.

What it costs or forces:

- An ADR amending ADR 095: layout as the owner of membership, the manifest
  schema reduced to instance metadata and hashes, a type-only working
  manifest, and partial-instance validation semantics.
- The validation contract, the type-spec contract and the set type document
  are rewritten for directory types.
- **The boundary becomes a published member.** Today the working instance has
  `boundary.md` at its root while the retained copy has only the output
  members, with the boundary's sections embedded in the overview. One layout
  cannot require the boundary and describe retained sets as they are. The
  operator's decision (2026-10-06) is to retain the boundary: the boundary
  job writes it inside `output/`, publication copies it with the other
  members, and no fallback to the overview is carried in the type. The one
  retained set predates this and is regenerated by a fresh run rather than
  migrated or tolerated, since its original boundary file is not recoverable
  and the boundary type's `source` block is absent from the overview.
- **The boundary owns source declarations.** After assembly the overview and
  the boundary both carry the source register, so both would declare the
  `SRC-*` IDs and the duplicate-declaration check would fire. The boundary is
  the declaring role; the overview's embedded sections are a copy, and
  whole-set validation checks that copy against its source instead of
  treating it as a second declaration.

## Options

### Where the layout lives

- **In the type spec's frontmatter.** The selected option. One file defines
  the type. The type spec is already the file a reader opens to learn what a
  type is, its frontmatter is already structured and already read by the
  loader for `name` and `schema`, and the type-spec contract asks a type to
  show its non-validator readers what an instance contains. A `layout` key
  for six roles is about forty lines, and the type-spec schema can check its
  shape. Frontmatter grows for directory types only.
- **In the schema file under a reserved keyword.** Rejected: it hides a
  layout vocabulary inside a JSON Schema document whose validator ignores it.
- **In a separate layout file named by the type spec.** Rejected while one
  directory type exists: one more file per type and one more resolution step
  for no separation the frontmatter does not already give.

### How relations are expressed

- **Declared data for identity and citation scope, code for the rest.** The
  selected direction. Small vocabulary; the imperative remainder is keyed by
  role.
- **All relations in code keyed by role.** Smallest change to the definition.
  The layout then declares only paths, types and requiredness, and
  member mode still needs the rule set to know what a role relates to.
- **A constraint language.** Rejected, as in ADR 095 and the
  [type-selected Python validation proposal](./type-selected-python-validation-checks.md).

### Nesting

- **Flat only, boundary inside the artifact.** The selected direction. The
  working artifact root is already `output/`, flat and the same shape as a
  retained set; the boundary is the one file outside it. Moving the boundary
  into `output/` brings the declaration source inside the artifact, keeps
  ADR 095's direct-children rule, and keeps one layout for working and
  retained instances.
- **Nested paths allowed.** Deferred. The manifest would move to the run
  root with members under `output/`. That amends ADR 095, needs a membership
  policy scoped to declared directories because run state and job workspaces
  live at the run root, and gives the working instance a shape the retained
  set lacks, so publication would need a path mapping or the retained tree
  would change. No type needs it.
- **Flat only, boundary outside.** Preserves ADR 095 unchanged but leaves the
  declaration source outside the artifact, and the companion proposal must
  let a type name external context, which is a different widening.

## Forces

- **A layout is a small language.** ADR 095 rejected external directory
  formats. The flat schema was the first draft of this language and has met
  its limits in completeness branches and the external boundary file. Keep
  the vocabulary to what the analysis set needs: literal filenames, expected
  type, a requiredness condition, two relation kinds.
- **One directory type exists.** This is the YAGNI counterweight. The
  proposal's warrant is that the analysis set already needs roles and an
  in-artifact declaration source, and that the companion proposal cannot be
  built without them.
- **Content identity is not layout.** Which members a frozen instance pins,
  and when, belongs to publication integrity and freezing, a concern larger
  than directory structure that ADR 095 and ADR 102 only begin. The layout
  declares structure; the manifest schema keeps the set's hash requirements
  as today, and a supplied hash always binds. A working manifest without
  hashes therefore fails whole-set validation until the set is complete,
  which is correct and needs no phase concept in the layout.
- **One shape for working and retained instances.** Publication copies
  members by name into `retained/<system>/`. A layout whose working paths
  carry a prefix the retained set lacks needs a path mapping or a changed
  retained tree. Keeping the artifact root at `output/` and moving the
  boundary into it keeps one layout for both.
- **Recognition still needs the manifest.** A layout tells the validator what
  an instance contains; the manifest tells it where an instance begins. The
  type-only working manifest is what makes a half-built instance visible, and
  a replay must see no change from writing it.
- **Drift between layout and code.** Until the workflow reads the layout, two
  statements of the member names coexist. Adoption should retire the code
  constants, not add a third copy.

## Free choices

The layout's key vocabulary, the form of the requiredness condition and how
roles key imperative rules are implementation choices. The manifest schema stays JSON Schema and keeps instance metadata
and hash requirements. Start from the analysis set's six reports, its
boundary file and its disposition-based completeness, and declare nothing the
set does not need.

## Adoption criteria

A candidate implementation must demonstrate that:

- A directory type declares its members by path with roles, and the validator
  derives membership and requiredness from that declaration
  rather than from the schema's filename properties.
- The boundary is written inside the artifact root and declared as a member,
  with membership still direct children of the manifest's directory.
- A role's declared relations are applied by whole-set validation and are
  available to a member-level lookup by path.
- Manifest construction and the analysis workflow's slot handling read the
  layout, and their member-name constants are retired.
- The analysis set validates as it does today, including completeness by
  disposition, with its layout declared rather than coded and its hash
  binding unchanged.
- Publication copies the boundary into the retained set, the overview's
  embedded boundary sections are checked against it, and the regenerated
  retained set passes under the new layout.
- Deterministic success establishes the declared structure, not analytical
  truth or semantic support.
