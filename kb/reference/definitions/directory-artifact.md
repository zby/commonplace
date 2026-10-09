---
description: "Definition — a directory artifact is a directory whose manifest names a directory type; the type's layout declares its member roles and relations, and the directory validates as one unit"
type: types/definition.md
tags: []
---

# Directory artifact

A **directory artifact** is a directory whose root holds a manifest,
`ARTIFACT.yaml`, whose `type` field names a directory type. The directory
is one validation unit, as a single typed file is. Its members are the
direct Markdown children that match a role of the type's layout.

A **directory type** is a type spec whose frontmatter carries a `layout`.
The layout declares the **roles** an instance has: for each, the file at
the directory root that fills it, the document type expected there, the
roles whose fields it repeats (`identity`), the roles whose declarations
its references resolve against (`cites`) and the roles whose acceptance
its verdict settles (`verifies`). It also declares which roles every
instance has and which a discriminating field adds, and whether a file
matching no role is a finding (`membership: closed`) or admitted
(`membership: open`). A role is a position the type declares; the file
that fills it is a member; a role's name is the same whatever file fills
it.

The manifest selects the type and may pin members: an entry under
`members` maps a filename to a digest that its bytes must match. Whether
every member must be pinned is the type's rule, not the layout's. A type
may require further manifest metadata through its schema, which
constrains the manifest only.

A **working instance** is a directory artifact whose manifest names only
its type. It is recognised from its first member; validation reports its
absent required members and checks the relations its present members
reach, and a candidate for a role can be validated in that role without
being written. A **finished instance** is one whose manifest pins what the
type requires; what makes it frozen is the collection's rule for the area
it is retained in.

## Boundaries

- A directory of typed files with no manifest is not a directory artifact;
  its files validate one by one and no relation between them is checked.
- Nested members are not declared: every role is a direct child. A
  directory artifact inside another is composition, which the layout
  vocabulary does not describe.
- A directory type's layout owns membership and relations. The type's
  schema owns the manifest's metadata. A type rule computes what needs a
  grammar, such as record declarations and references. Nothing else about
  the directory's structure is declared anywhere.
- The artifact-run engine runs plans against typed directory artifacts and
  derives their relations from the layout; a role, a relation and a member
  mean here what they mean there.

The exact checks are in the
[validation contract](../validation-contract.md#directory-artifacts); the
decisions are [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md),
[ADR 111](../adr/111-directory-types-declare-their-layout.md) and
[ADR 114](../adr/114-directory-types-declare-what-a-role-verifies.md). The
first directory type is the
[analysis set](../../agentic-system-analyses/types/agentic-system-analysis-set.md).
