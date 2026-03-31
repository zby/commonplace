The note presents one framework: four pointer types ordered by context density (inline links > index entries > skill descriptions > search results), grounded in the fundamental navigation decision ("should I follow this?").

---

**Framework: Four pointer types by context density**

Grounding: "Every pointer asks the same question: should I follow this? ... The more context a pointer carries, the cheaper the navigation decision."

- Simplest: a single inline link in explanatory prose. Maximum context — the agent knows what's there and why it matters before deciding. ✓
- Most extreme: a bare search result showing only a filename. Minimum context — the agent must load the target to judge relevance. ✓
- Between: a link in a bullet list without relationship articulation (e.g., "See also: [note.md]"). Less context than inline but more than a search result (at least the link text is visible). The note doesn't explicitly address bare-link lists, but they fall naturally between inline and index entries. ✓
- Adjacent: **backlinks** — pointers in the reverse direction (what links TO this note, visible from the target). INFO — the note covers only forward navigation (choosing what to read next). Backlinks carry different context (the linking note's perspective on the relationship) and create a different decision problem (should I visit who links to me?). They're not covered, which is appropriate for the note's scope but could be noted as an extension.
- Adjacent: **algorithmic recommendations** (e.g., "similar notes" from embeddings). These are generated pointers with minimal context — similar to search results but without the agent having formulated a query. Not covered. Outside scope.

**Design implications coverage**

Four levers (one per pointer type). Each is specific and actionable. The [title-as-claim] shortcut that "works across all of these" is a clean generalization. ✓

No WARN. One INFO on backlinks as an uncovered reverse-navigation pointer type.
