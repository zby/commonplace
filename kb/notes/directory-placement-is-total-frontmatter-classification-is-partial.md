---
description: "Canonical paths cover every file before validation and supply locality; opt-in types supply portability. Validation can encode similar policy on either surface, but native guarantees differ."
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, type-system]
status: seedling
---

# Directory placement is total, frontmatter classification is partial

In a file-based knowledge base, every file has a canonical path before any parser or validator accepts it. Location is therefore *physically total*: the filesystem assigns every file a value on this axis, with no opt-out. At a chosen routing level, that location is exclusive, even though the path also lies within ancestor scopes. Location is also *spatial*: co-location creates neighborhoods for scoped search, browsing, and curated indexes. The filesystem supplies the address and neighborhood without metadata synchronization, but it does not enforce the semantic clauses attached to them.

Declared classifications, by contrast, can be optional or mandatory. In Commonplace, frontmatter is optional: the validator treats a file without it as implicit `text`, but the file declares no `type:` value. Type is therefore *partial over the physical files before validation*. A validator can require every admitted artifact to have a type, making classification total over that valid subset. But this is an additional enforcement rule, not a property of the file substrate. Even when present, a type describes a document's structure rather than its canonical neighborhood: one type can appear across many directories, one directory can hold many types, and queries assemble the type's cohort. In this configuration, type *labels* documents while location *partitions* the physical space.

## Why the asymmetry matters

These surfaces have different native guarantees, not different expressive powers. A policy can be encoded in a directory contract, a required field, a type, or a convention. Moving it between surfaces, however, changes when it applies, how failure appears, and what neighborhood it creates.

The **location contract** is the [collection](../reference/definitions/collection.md)'s `COLLECTION.md`; position selects it. The path identifies the applicable contract before the document cooperates, including for files with missing or malformed frontmatter. Agents, reviews, or validators must still enforce the contract's semantic clauses. Commonplace places the [text contract](./definitions/text-contract.md)—quality goal, linking policy, and scope—on this surface because those clauses are intended to cover every file in the region.

The **type contract** is the type-spec; a declaration selects it. It governs structure: schema, required sections, and frontmatter fields. In an opt-in system, it applies only to documents that declare the type. The declaration is portable, however: the same global type can retain its shape when the document moves between collections.

Translating a clause between the surfaces does not preserve their native guarantees:

- A mandatory type can encode "every valid artifact is theoretical," but a missing or malformed declaration escapes the rule until validation. The resulting cohort also has no canonical neighborhood unless another mechanism builds one.
- A dedicated directory can encode "everything routed here has Evidence and Reasoning sections," but doing so spends that directory level on shape, prevents other shapes from sharing the same immediate neighborhood, and changes the structural obligation when the document moves.

In Commonplace's opt-in type model, `COLLECTION.md` and a type-spec are therefore not interchangeable without changes to the enforcement and routing model. This asymmetry explains the older observation that types and directories are orthogonal.

## An assignment rule, not an identification

Nothing forces the directory tree to carry collection or text-contract semantics. A KB that routes kind-first can spend its directory tree on type—a `decisions/` folder—and gain pre-validation coverage and neighborhood for kind while declaring content area elsewhere. Choosing which classification receives the substrate's native properties is a design decision. Assign the directory tree to the classification that needs:

- **pre-validation coverage**, for admission and routing rules that must select a contract even for untyped or malformed files;
- **canonical exclusivity**, when one primary classification is needed at a particular routing level, while allowing contracts on ancestor scopes to compose;
- **neighborhood**, for clauses about relations among artifacts: link vocabulary, duplicate policy, browse order, index membership.

Classifications that instead need portability—obligations that should travel with an artifact wherever it lives—fit declared axes. Validation can make such an axis mandatory and total over admitted artifacts, but it adds an enforcement dependency. It also does not select a value for malformed files before the check runs.

The assignments can compose within one tree: Commonplace gives ADRs a browsable subdirectory neighborhood inside `kb/reference/`, while their type-spec carries the structural contract and the surrounding collection retains its text contract.

Moving a file and changing its declared type remain distinct edits, though admission or cross-contract constraints can require both in one valid transition.

## Scope

The claim concerns canonical placement in a file-based corpus before validation. A database can make several classification fields mandatory without giving any of them tree locality; filesystem overlays require the KB to designate one canonical location. The claim does not imply that directory contracts enforce their own semantics or that declared metadata cannot be mandatory. It means only that those guarantees come from additional machinery rather than physical placement.

---

Relevant Notes:

- [why directories despite their costs](./why-directories-despite-their-costs.md) — extends: supplies the mechanism behind its "types and directories are orthogonal" observation
- [why notes have types](./why-notes-have-types.md) — grounds: establishes that type is opt-in and free-form, the premise that makes type partial rather than total
- [a knowledge base holds theories, descriptions, and prescriptions](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — extends: the content-layer role that collection and type jointly identify, here explained by register attaching to the total axis
- [a universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — grounds: what stays universal is what derives from the consumer or substrate, which licenses treating file-substrate properties as framework-level claims
- [042-Register becomes a default profile under open-ended text contracts](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — derived-from: the originating Commonplace application of placement by quantifier, not independent evidence for this substrate claim
