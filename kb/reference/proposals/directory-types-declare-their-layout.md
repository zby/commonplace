---
description: "Proposal: a directory type declares the layout of its instances, so membership, roles, nesting and cross-member relations come from one external definition instead of filename conventions and code."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Directory types declare their layout

A directory type is already defined outside its instances: a manifest points
at a type spec, and the type spec names a schema. What that definition cannot
do is describe the directory. It sees a flat set of sibling Markdown files and
encodes everything else, roles, nesting, completeness and relations, in
filename conventions, schema branches and Python keyed by type path.

This proposal gives the directory type a layout: a declared set of paths under
the artifact root, each with a role, and for each role the expected document
type, when it is required, whether it is hashed, and how it relates to other
roles. Membership becomes "matches a layout entry". Whole-set validation,
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
- The analysis run keeps its source register in `boundary.md` beside
  `output/`, outside the artifact, because the artifact cannot contain a
  parent-level file. Before synthesis, workflow code and one type rule
  substitute it for the absent overview by path convention.
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

- Nothing below the root can be a member, so an artifact cannot include a
  file that belongs to it but lives one level up or down. The analysis set's
  declaration source sits outside the artifact for this reason alone.
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
entries, each binding a relative path or pattern under the artifact root to a
role. A role states:

- the expected document type at that slot, checked against the member's own
  `type:` declaration, so each fact has one owner;
- when the slot is required, as a condition the validator can evaluate from
  the instance, such as another member's field value;
- whether the manifest must hash the slot;
- relations to other roles: which role supplies identity fields this member
  must repeat, and which roles' declarations this member may cite.

Membership is matching a layout entry. Paths the layout does not mention are
governed by the type's open or closed policy, scoped to the directories the
layout declares, so a nested working tree such as job workspaces can sit
inside the artifact root without becoming members or failures.

The manifest keeps its ADR 095 role: recognition marker and instance metadata.
It does not restate layout.

Consumers read the layout instead of restating it. Whole-set validation
derives required members and hash expectations from it. Manifest construction
derives which files to pin from it. Workflow slot maps derive from it. Member
mode, in the companion proposal, resolves a file's role from its path relative
to the nearest manifest and applies the role's relations.

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
  Hash requirements apply only to manifest entries that exist. A coordinator
  can validate the working directory mid-run and read the relation findings
  while treating the missing-member findings as expected.
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

The analysis set in one candidate vocabulary. This is an illustration of the
decisions above, not a shipped format; the keys and their spelling are free
choices.

```yaml
type: types/type-spec.md
name: agentic-system-analysis-set
schema: ./agentic-system-analysis-set.schema.yaml   # manifest metadata only
layout:
  roles:
    boundary:
      path: boundary.md
      type: agentic-system-analyses/types/agentic-system-analysis-boundary.md
    overview:
      path: output/overview.md
      type: agentic-system-analyses/types/agentic-system-analysis-overview.md
      hashed: true
    runtime:
      path: output/runtime.md
      type: agentic-system-analyses/types/agentic-system-runtime-report.md
      hashed: true
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    memory:
      path: output/memory.md
      type: agentic-system-analyses/types/agent-memory-analysis-report.md
      hashed: true
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    epistemic:
      path: output/epistemic.md
      type: agentic-system-analyses/types/agentic-system-epistemic-report.md
      hashed: true
      identity: {from: boundary, fields: [run-id, reviewed-boundary]}
      cites: [boundary, runtime, memory, epistemic]
    reconciliation:
      path: output/reconciliation.md
      type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
      hashed: true
      cites: [boundary, runtime, memory, epistemic]
    memory-profile:
      path: output/memory-profile.md
      type: agentic-system-analyses/types/agent-memory-profile.md
      hashed: true
      identity: {from: memory, fields: [source-identity]}
      cites: [runtime, memory, epistemic]
  required:
    always: [boundary, overview]
    by: {role: overview, field: result-disposition}
    complete: [runtime, memory, epistemic, reconciliation, memory-profile]
  closed: [output]
```

What each key decides:

- `roles` are keyed by name; imperative rules and member-level findings use
  the name. `path` is a literal relative path; no pattern form until a type
  needs one.
- `type` is the expected type at the slot, compared with the member's own
  `type:` declaration.
- `hashed` means whole-set validation requires a manifest hash for the slot.
  A working manifest without hashes fails whole-set validation because the set
  is not whole; no phase concept is needed.
- `identity` names the role whose listed fields this member must repeat
  verbatim.
- `cites` is the citation scope: the roles whose declarations resolve this
  member's references. A role may list itself.
- `required` has one discriminator and per-value lists, mirroring the schema
  branch the set uses today. A value with no list requires only `always`.
- `closed` names the directories where an undeclared Markdown file fails. The
  root stays open because run state and job workspaces live there.

The nearest-manifest search bound for a member lookup is the deepest declared
path depth. Manifest construction pins exactly the `hashed` roles present.
Workflow slot constants become lookups into `roles`.

### Operativity

Consumers would be the validator's directory path, the finalize step, the
analysis workflow's slot constants and its round-close record check, and any
future directory type. No consumer reads a layout today; the layout
representation and its reader must be built. The oracle is the actual files
at declared paths and their declared facts. Nested membership amends ADR 095's
direct-children rule and needs an amending decision when it ships.

## Consequences of adoption on its own

What becomes checkable through the type, without the companion proposal:

- The analysis set's membership, completeness by disposition and hash binding
  validate from the declaration instead of the schema's filename properties.
  Same checks, one owner.
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

- An ADR amending ADR 095: nested membership, layout as the owner of
  membership, the manifest schema reduced to instance metadata, a type-only
  working manifest, and partial-instance validation semantics.
- The validation contract, the type-spec contract and the set type document
  are rewritten for directory types.
- **Working and retained instances differ.** The working instance has
  `boundary.md` at its root; the retained copy has only the output members,
  with the boundary's sections embedded in the overview. One layout cannot
  require the boundary and also describe retained sets as they are. The
  choices are to retain the boundary file as a member, which adds a file to
  frozen published sets and needs a migration or a tolerance for older sets,
  or to let the identity and citation source fall back to the overview when
  the boundary is absent, which is the current stand-in logic made explicit.
  This is an operator decision and the first thing adoption must settle.
- **Source declarations need one owner.** After assembly the overview and the
  boundary both carry the source register, so both declare the `SRC-*` IDs
  and the duplicate-declaration check would fire. The layout forces the rule
  that the boundary owns source declarations and whole-set validation checks
  the overview's register against it, or the reverse once the boundary is
  not a member.

## Options

### Where the layout lives

- **In the type spec's frontmatter.** One file defines the type. The type spec
  is already the authoring contract, and its frontmatter is already
  structured. Frontmatter grows for directory types only.
- **In the schema file under a reserved keyword.** Keeps the type spec
  unchanged. Mixes a layout vocabulary into a JSON Schema document whose
  validator ignores it.
- **In a separate layout file named by the type spec.** Cleanest separation.
  One more file per directory type and one more resolution step.

### How relations are expressed

- **Declared data for identity and citation scope, code for the rest.** The
  selected direction. Small vocabulary; the imperative remainder is keyed by
  role.
- **All relations in code keyed by role.** Smallest change to the definition.
  The layout then declares only paths, types, requiredness and hashing, and
  member mode still needs the rule set to know what a role relates to.
- **A constraint language.** Rejected, as in ADR 095 and the
  [type-selected Python validation proposal](./type-selected-python-validation-checks.md).

### Nesting

- **Nested paths allowed.** The selected direction. Resolves the declaration
  source by placement: the analysis manifest moves to the run root and
  `boundary.md` becomes a member. Requires the ADR 095 amendment and a
  scoped open-membership policy.
- **Flat only.** Preserves ADR 095 unchanged. The declaration source stays
  outside the artifact and the companion proposal must let a type name
  external context, which is a different widening.

## Forces

- **A layout is a small language.** ADR 095 rejected external directory
  formats. The flat schema was the first draft of this language and has met
  its limits in completeness branches and the external boundary file. Keep
  the vocabulary to what the analysis set needs: literal paths and one pattern
  form, expected type, a requiredness condition, hashing, two relation kinds.
- **One directory type exists.** This is the YAGNI counterweight. The
  proposal's warrant is that the analysis set already needs nesting and roles,
  and that the companion proposal cannot be built without them.
- **Hashing follows roles, not phases.** A working instance cannot pin bytes
  that change each round. Whether hashing is a role property or an instance
  phase property is open; ADR 095 binds any supplied hash either way.
- **Closed membership over a tree is impractical.** A run root holds state and
  workspaces that are not members. Membership policy must scope to declared
  directories or the type cannot sit at the root.
- **Recognition still needs the manifest.** A layout tells the validator what
  an instance contains; the manifest tells it where an instance begins. The
  type-only working manifest is what makes a half-built instance visible, and
  a replay must see no change from writing it.
- **Drift between layout and code.** Until the workflow reads the layout, two
  statements of the member names coexist. Adoption should retire the code
  constants, not add a third copy.

## Free choices

The layout's concrete representation, the pattern syntax, the form of the
requiredness condition, how roles key imperative rules, and whether the
manifest schema stays JSON Schema or derives from the layout are
implementation choices. Start from the analysis set's six reports, its
boundary file and its disposition-based completeness, and declare nothing the
set does not need.

## Adoption criteria

A candidate implementation must demonstrate that:

- A directory type declares its members by path with roles, and the validator
  derives membership, requiredness and hash expectations from that declaration
  rather than from the schema's filename properties.
- A member below the root, or beside the manifest's parent, can be declared
  and validated as a member, with the direct-children rule amended by decision.
- Undeclared paths inside the root follow a scoped membership policy and do
  not fail an open subtree.
- A role's declared relations are applied by whole-set validation and are
  available to a member-level lookup by path.
- Manifest construction and the analysis workflow's slot handling read the
  layout, and their member-name constants are retired.
- The analysis set validates as it does today, including completeness by
  disposition and hash binding, with its layout declared rather than coded.
- Deterministic success establishes the declared structure, not analytical
  truth or semantic support.
