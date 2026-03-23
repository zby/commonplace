=== SEMANTIC REVIEW: type-system-enforces-metadata-that-navigation-depends-on.md ===

Claims identified: 10

1. "The navigation argument assumes documents *have* descriptions" (para 1)
2. "descriptions don't appear spontaneously — the type system is what makes them exist" (para 1)
3. "The note base type defines `description` as the only required field" (para 2)
4. "Any document that crosses from text to note must acquire a description" (para 2)
5. "validation can check that it's present, non-empty, and discriminating" (para 2)
6. "Without this enforcement, a knowledge base degrades quickly" (para 3) — causal
7. "Agents writing notes under time pressure skip metadata. Human authors forget." (para 3) — causal mechanism
8. "The result is a collection of documents that can only be navigated by opening each one" (para 3) — consequence
9. "The type system's role here is not routing... but ensuring the routing data exists at all" (para 4) — distinction
10. "The catalogue is only useful if it's comprehensive; the type system is the mechanism that makes it comprehensive" (para 4) — scope claim

WARN:
- [Completeness] The note claims "validation can check that it's present, non-empty, and discriminating" (para 2). "Present" and "non-empty" are deterministic checks, but "discriminating" is a judgment call requiring LLM evaluation. The note treats all three as equivalent enforcement mechanisms, but they sit at very different points on the verification cost spectrum. The note base type spec (types/note.md) acknowledges this gradient ("from deterministic... through LLM rubric... to corpus-level"), but this note collapses it. The enforcement story is weaker for the property that matters most — a description that is present but non-discriminating ("This is a note about types") satisfies the deterministic checks while still failing the navigation purpose the note argues for.
- [Completeness] The note claims "the type system is the mechanism that makes [the catalogue] comprehensive" (para 4). Boundary case: a document that is promoted to `note` type (has frontmatter and a description field) but whose description is a placeholder or boilerplate — e.g. `description: TODO` or `description: A note`. The type system creates the obligation, but the note's own argument requires quality enforcement (discriminating descriptions), which the type system alone cannot guarantee. The claim that the type system "makes it comprehensive" overstates the mechanism — it makes it structurally complete but not semantically comprehensive. The catalogue analogy ("a library where some books have catalogue cards and some don't") maps to presence, not quality.
- [Completeness] Boundary case: agents or humans who create notes outside the KB workflow — e.g., copying a markdown file directly, or an external tool generating notes. The type system's enforcement depends on validation being run; without `/validate` in the workflow, the obligation exists on paper but is not actually enforced. The note conflates the type definition (which creates the obligation) with actual enforcement (which requires tooling in the workflow). The text-to-note boundary is only enforced if something checks it.

INFO:
- [Completeness] The note frames the degradation scenario as binary: either enforcement exists and navigation works, or it doesn't and "the result is a collection of documents that can only be navigated by opening each one." A middle ground exists — partial compliance (say, 80% of notes have descriptions) still enables useful navigation for most queries. The degradation is gradual, not cliff-like. The note's rhetoric implies a sharper boundary than the actual failure mode.
- [Grounding] The note claims the navigation argument "assumes documents have descriptions," referencing types-give-agents-structural-hints-before-opening-documents.md. That note does indeed make this assumption ("The type plus description let an agent narrow from hundreds of files to the few it needs") and explicitly links back to the current note as the mechanism that ensures descriptions exist. The dependency is real but circular in exposition — each note cites the other as its justification. This is not a grounding error (both notes are transparent about the relationship), but a reader following links will loop.
- [Internal consistency] The note distinguishes the type system's role as "not routing... but ensuring the routing data exists at all" (para 4). But paragraph 2 says "the type creates the obligation, and `/validate` checks compliance" — splitting the enforcement across two mechanisms (type definition + validation tooling). The note's title attributes enforcement to "the type system," but the body reveals it is a two-part mechanism (type definition + validation). This is not a contradiction — the type system includes validation — but the note could be read as claiming types alone do the enforcement, when validation is equally load-bearing.

PASS:
- [Grounding] Claim 3: "The note base type defines `description` as the only required field." Verified against types/note.md, which states in its Global fields table that `description` is the only field marked Required: Yes. All other fields (type, traits, tags, status) are marked No. Attribution is accurate.
- [Grounding] Claim 4: "Any document that crosses from text to note must acquire a description." Verified against types/text.md, which defines promotion as "add frontmatter with at least a `description` field." The claim accurately represents the text-to-note transition.
- [Grounding] The note's claim that its role is enforcement (not routing) is consistent with the parent note why-notes-have-types.md, which separates "Navigation" and "Metadata enforcement" as distinct roles (sections 1 and 2) and assigns this note to the enforcement role specifically.
- [Internal consistency] The note maintains a consistent distinction throughout between the navigation role (attributed to the sibling note) and the enforcement role (claimed here). No definition drift detected — "enforcement" consistently means "ensuring metadata exists," not "ensuring metadata is correct" or "ensuring metadata is used."
- [Internal consistency] The catalogue analogy in paragraph 4 ("a library with a catalogue... the catalogue is only useful if it's comprehensive") faithfully represents the body's argument. No elision of tensions between summary and body.

Overall: 3 warnings, 2 info
===
