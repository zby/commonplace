=== SEMANTIC REVIEW: document-classification.md ===

Claims identified: 11

1. "A document has exactly one type." (Base types section)
2. "`text` has no frontmatter and no requirements." (Base types section)
3. "Every other type extends `note`" (Base types section)
4. "it defines the shared fields (description, status, traits, areas) that all structured documents carry" (Base types section, referring to note)
5. "The `type` field is a free-form string." (Base types section)
6. The base types table enumerates seven types: text, note, spec, review, index, adr, structured-claim. (Base types table)
7. "`structured-claim` extends `note` with required argument sections: `## Evidence`, `## Reasoning`, and optionally `## Caveats`." (Below the table)
8. "It represents a fully developed argument — the Toulmin scaffold applied to a claim-titled note." (Below the table)
9. "The promotion path is `note` -> `structured-claim`: when a note's argument matures enough to fill Evidence/Reasoning sections, it earns the type." (Below the table)
10. The migration table maps five old types to new encodings. (Migration section)
11. "was subject matter, not structure" (Migration table, explaining why `design` became `note`)

WARN:
- [Completeness] The base types table lists seven types, but the note says "The `type` field is a free-form string" and that "directory-scoped `types/` folders document the structural expectations for each." This creates a tension: the table reads as an exhaustive enumeration ("The table below lists the common values") but the linked note directory-scoped-types-are-cheaper-than-global-types.md explicitly argues that types like `adr`, `review`, and `index` should be directory-local specializations, not global base types. A boundary case: a `source-review` type (mentioned in directory-scoped-types-are-cheaper-than-global-types.md under "Where affordances actually live") is absent from this table — is it a base type or a directory-scoped type? The note does not clarify the boundary between "common values" listed here and directory-scoped types documented elsewhere. This is a real gap: an agent reading only this spec cannot tell whether to add new types to this table or to a directory-scoped types/ folder.

- [Grounding / domain coverage] The note claims that `note` "defines the shared fields (description, status, traits, areas)" but when checking types/note.md, the global fields listed there are: `description`, `type`, `traits`, `tags`, and `status`. The note says "areas" but the actual spec says "tags." This is a vocabulary mismatch — `areas` was likely the old name for what is now `tags`. The attribution does not match the source.

INFO:
- [Completeness] The migration table maps five old types but does not mention `spec`, `review`, or `index`, which appeared in the old flat enum listed in document-types-should-be-verifiable.md ("The original type system used a flat enum: design, analysis, insight, research, comparison, spec, review, index"). This implies `spec`, `review`, and `index` survived unchanged, but the note does not state this explicitly. A reader encountering one of these old types would not know whether migration is needed.

- [Completeness] Boundary case: a document that is both a `spec` and an `adr` (e.g., an architecture decision that includes implementation-ready detail with Design/Implementation sections AND Context/Decision/Consequences sections). The note asserts "A document has exactly one type" but does not address how to resolve cases where a document satisfies the structural tests for multiple base types. The traits system handles combinatorial properties, but base type conflicts are not discussed.

- [Completeness] Boundary case: a `text` file that contains YAML frontmatter but lacks a `description` field. The table says `note` requires "Has frontmatter with description" and `text` requires "No frontmatter." A file with frontmatter but no description falls between the two structural tests. Neither type covers it.

- [Internal consistency] The note's type field says `type: spec`, and the description says "Taxonomy overview." The base types table defines `spec` as having "Design/Implementation sections," but this note has "Base types" and "Migration from old flat types" sections, not Design/Implementation. By the note's own structural test for `spec`, this note may not qualify as one. This is a minor self-referential inconsistency — the note classifies itself using a type whose structural test it does not satisfy.

PASS:
- [Grounding] The link to document-types-should-be-verifiable.md as "design rationale" is accurate. That note provides the full argument for why types should assert verifiable structural properties, and this note implements that design.
- [Grounding] The link to types/note.md for "global fields, status ladder, traits, and design principles" is accurate. That spec does define all of those elements.
- [Grounding] The description of `structured-claim` as extending `note` with Toulmin-derived sections aligns with claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md, which develops the full rationale and explicitly maps to Toulmin components.
- [Grounding] The migration table's treatment of `design` as "was subject matter, not structure" is grounded in document-types-should-be-verifiable.md, which argues at length that "design" dominated the KB without doing discriminatory work.
- [Grounding] The migration of `insight` to "structured-claim (developed argument) or note (claim title, free-form body)" matches the promotion path described in the Toulmin note.
- [Internal consistency] The seven base types form a coherent hierarchy: `text` (no frontmatter) at the bottom, `note` (frontmatter + description) as the base structured type, and five specializations with progressively more structural requirements. No pairwise contradictions found.
- [Internal consistency] The migration table is consistent with the base types table — every "new encoding" in the migration table refers to a type or type+trait combination that exists in the base types table or the traits system defined in types/note.md.

Overall: 1 warning, 4 info
===
