---
description: "A filesystem assigns every artifact a location unconditionally, while type is opt-in and non-partitioning, so COLLECTION.md and type-spec contracts cannot substitute for each other"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, type-system]
status: seedling
---

# Directory placement is total, frontmatter classification is partial

In a file-based knowledge base, the substrate places every artifact at exactly one path. Location is therefore *total*: the filesystem assigns each file a value on this axis, the values are mutually exclusive (a file lives in one directory), and there is no opt-out — a file cannot exist without a location. Location is also *spatial*: co-location creates neighborhoods that scoped search, browsing, and curated indexes operate over. The substrate enforces these properties for free — no validation, no sync.

Every other axis a KB layers on — type, tags, traits, status — is *partial*. It lives in frontmatter, and frontmatter is optional: a file with no frontmatter is implicit `text`, asserting no type at all. Even when present, a type is a within-document property (this document has these sections) rather than a partition of the corpus: one type appears across many directories, and one directory holds many types, and a type's cohort is scattered — assembled only by query, never by proximity. Type *labels* documents; location *partitions* the space.

## Why the asymmetry matters

Because location is total and type is partial, the two contracts keyed to them cannot substitute for each other.

The **location contract** is the [collection](../reference/definitions/collection.md)'s `COLLECTION.md` — it governs by position. Because position is the one thing every artifact in a subtree shares unconditionally, a location contract can bind the whole subtree, including files that carry no type. This is why the [register](./definitions/text-contract.md) (the theoretical, descriptive, or prescriptive quality goal), the linking policy, and the scope attach to a collection — a directory — and not to a type: they must hold for every artifact in the region whether or not it opted into a type.

The **type contract** is the type-spec — it governs by structure: schema, required sections, frontmatter fields. It binds only the documents that declare that type, and says nothing about where they live. A `structured-claim` has the same shape in `kb/notes/` or `kb/reference/`.

Neither can be expressed as the other:

- You cannot encode "everything here is theoretical register" as a type. Types do not partition the corpus, and untyped files would escape the rule entirely; only a location contract reaches every file in the subtree.
- You cannot encode "this document has Evidence and Reasoning sections" as a location. Many structures coexist in one directory and the same structure recurs across directories; only a type contract travels with the document.

The independence of the two axes is not a coincidence of the current design — it follows from location being total and type being partial. That asymmetry is the mechanism behind the older observation that types and directories are orthogonal.

## An assignment rule, not an identification

Nothing forces the directory tree to carry the collection/register semantics. A KB that routes kind-first can spend its directory tree on type — a `decisions/` folder — and it then gets totality for kind while content area becomes a declared, partial axis. Which classification receives the substrate's free enforcement is a design choice. The rule is: assign the directory tree to the classification that needs its properties —

- **totality**, for clauses that must bind artifacts before or without their cooperation: admission and routing ("what belongs here"), rules that hold for untyped and malformed files;
- **exclusivity**, for properties that cannot be coherently conjoined: a single quality goal, a single maintenance regime;
- **neighborhood**, for clauses about relations among artifacts: link vocabulary, duplicate policy, browse order, index membership.

Classifications that need portability instead — obligations that should travel with an artifact wherever it lives — go on declared axes, whatever the assignment.

The two assignments compose within one tree. In Commonplace, `kb/reference/adr/` is a type-shaped subdirectory inside a collection: the ADR type-spec carries the portable shape contract, but ADRs also need a neighborhood — a numbered, browsable decision log — so the type claims directory real estate at the level where it needs spatial properties, while admission to `kb/reference/` remains the collection's clause. Both axes take directories, each for the property it lacks elsewhere.

## Co-placement: guarantee containment

Contract clauses reference each other, and that couples their placement: **a clause that consumes another clause's guarantee must have its scope contained in the guarantor's.** A link grammar promising that `since [title](./x.md)` reads as prose consumes a guarantee about link targets' titles; the grammar quantifies over the whole collection (any artifact may cite any other), so the title convention must quantify over at least the same set — stated at the collection level with typed exceptions declared where the grammar can see them, not scattered across type specs. The failure signature is a location-wide mechanism silently depending on a kind-scoped guarantee: sound for today's artifacts, broken by the first artifact of another type.

## Consequences

- **Two independent operations.** Moving a file changes which location contract governs it; editing its frontmatter type changes which type contract governs its structure. Because the axes are independent, the two operations never have to happen together.
- **Register lives at the collection, not the type.** Commonplace assigns the total axis to content area, so the register — a quality goal that must bind every local artifact and cannot be conjoined with a second one — is a property of place. A `note` reads as theoretical in `kb/notes/` and descriptive in `kb/reference/` precisely because the collection, not the type, carries the register.
- **The tree's totality is spent on one classification.** Whatever receives it, every classification layered in frontmatter is declared and partial. A design that wants another total axis must simulate it with validation — a checked, mandatory field — and accepts that the substrate no longer enforces it for free.

## Scope

The claim is about file-based KBs, where the substrate forces a unique path per artifact. In a database-backed store the total axis need not be a tree: a primary key is total but flat, and several total partitions can coexist (any NOT NULL column). The directory tree's specialness is a property of the file substrate, not of knowledge bases in general. Overlay mechanisms — symlinks, hardlinks, generated views — deliberately weaken exclusivity; where a KB uses them, the totality claims apply to the canonical location, and the overlay is a derived copy.

---

Relevant Notes:

- [why directories despite their costs](./why-directories-despite-their-costs.md) — extends: supplies the mechanism behind its "types and directories are orthogonal" observation
- [why notes have types](./why-notes-have-types.md) — grounds: establishes that type is opt-in and free-form, the premise that makes type partial rather than total
- [a knowledge base holds theories, descriptions, and prescriptions](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — extends: the content-layer role that collection and type jointly identify, here explained by register attaching to the total axis
- [a universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — grounds: what stays universal is what derives from the consumer or substrate, which licenses treating file-substrate properties as framework-level claims
- [open-ended collection text contracts](../reference/proposals/open-ended-collection-text-contracts.md) — derived-from: the proposal whose contract-decomposition rule (placement by quantifier across surfaces) this claim generalizes
