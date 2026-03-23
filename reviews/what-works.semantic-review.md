=== SEMANTIC REVIEW: what-works.md ===

Claims identified: 14

**Claim inventory:**

1. [Prose-as-title] Note titles that work as claims when linked make the graph self-documenting.
2. [Prose-as-title] "Since [[thin adapters reduce coupling between providers and runtime]]" reads as prose and tells you what the note argues without opening it.
3. [Prose-as-title] Titles-as-labels ("adapter notes", "runtime thoughts") destroy this property.
4. [Prose-as-title] Multi-claim documents (specs, frameworks) get topical titles because no single claim subsumes their content.
5. [Template fields] Template fields like `description:` and `type:` guide agents to supply metadata at the moment of creation.
6. [Template fields] This is more reliable than documentation rules that the agent reads at session start and forgets.
7. [Template fields] The `areas: []` field nudges agents toward curated area indexes.
8. [Discovery-first] Checking findability *before* saving prevents orphan accumulation.
9. [Discovery-first] Four questions enumerate the complete findability check: title as claim, description adds info, linked from index, linkable without dragging context.
10. [Frontmatter] YAML frontmatter turns a directory of markdown files into a queryable collection.
11. [Frontmatter] In practice, `areas` and `description` are the fields that get queried.
12. [Semantic search] `rg` handles structured queries but discovering *conceptually related* notes requires semantic search.
13. [Semantic search] Both tools embody the pattern described in "files beat a database": files remain the source of truth while derived indexes provide capabilities files alone cannot.
14. [Public/internal] Keeping knowledge system artifacts out of public docs prevents coupling.

---

## Step 2: Completeness and boundary cases

### Framework: "What works" as a collection

The note's title and opening line claim to catalog "patterns that have proven valuable in practice." This implicitly defines a space: all patterns in this KB methodology that have demonstrated practical value.

**Boundary cases tested:**

- **Link semantics and relationship typing.** The KB methodology invests heavily in link semantics (since/because/contradicts). This is a separate operational pattern from prose-as-title — you can have claim titles without enforcing link relationship types. The note mentions link semantics only in passing ("reads as prose") but never identifies explicit relationship labeling as a proven pattern in its own right.
- **Progressive disclosure / loading hierarchy.** The linked note title-as-claim-enables-traversal-as-reasoning.md discusses progressive disclosure as a major benefit. The what-works note never mentions progressive disclosure or context budgets as a working pattern, despite this being central to the KB's agent-oriented design.
- **The `/connect` workflow.** CLAUDE.md lists `/connect` as a key step in content creation. The note covers discovery-first (a pre-save check) but not the post-save connection workflow, which is a distinct operational pattern.
- **Quality scoring / maintenance patterns.** files-not-database.md references note quality scores as a proven approach. Maintenance and curation patterns are absent from what-works.
- **Workshop layer.** The vocabulary section of CLAUDE.md defines a workshop layer for work-in-flight documents. If it exists as a named concept, it may be a proven pattern — or it may not yet be proven. Either way, its absence is notable.

### Framework: Discovery-first four questions (Claim 9)

The note enumerates exactly four findability questions. This is a scope claim ("four questions").

**Boundary cases tested:**

- **Temporal findability.** Can someone find this note six months from now when terminology has drifted? None of the four questions address temporal robustness — they all test findability at the moment of creation.
- **Search findability vs. navigation findability.** The four questions focus on navigation (titles, indexes, links). None directly test whether the note is discoverable via keyword search or semantic search (e.g., "does the description contain terms someone would search for?"). The "description adds information beyond the title" question partially covers this but doesn't explicitly frame it as a search concern.
- **Cross-directory findability.** A note in `kb/notes/related-systems/` must be findable from the main notes directory. The four questions don't distinguish between same-directory and cross-directory discovery.

---

## Step 3: Grounding alignment

### Claim 1-4 grounded by title-as-claim-enables-traversal-as-reasoning.md

The what-works note says: "The theory behind this — why title as claim enables traversal as reasoning — also identifies where it breaks: multi-claim documents (specs, frameworks) get topical titles because no single claim subsumes their content."

**Attribution accuracy:** PASS. The linked note does identify exactly this boundary — its "Where it breaks: multi-claim documents" section discusses specs and frameworks that require topical titles, and the reasoning matches (no single claim subsumes their content).

**Vocabulary check:** The what-works note says "the graph self-documenting." The linked note never uses the phrase "self-documenting" — it says "scanning file tree = scanning arguments" and "following links = following reasoning chains." The inference from "scanning arguments" to "self-documenting" is reasonable but is the what-works note's own gloss, not the source's language.

### Claim 13 grounded by files-not-database.md

The what-works note says: "Both tools embody the pattern described in files beat a database: files remain the source of truth while derived indexes (qmd's embeddings, rg's grep) provide capabilities files alone cannot."

**Attribution accuracy:** PASS. The files-not-database note explicitly states: "The pattern is: files as source of truth, derived indexes for capabilities files alone can't provide." This is nearly verbatim.

**Domain coverage:** The files-not-database note frames this pattern in terms of deferring schema commitment and incremental constraining. The what-works note uses the pattern more narrowly (just to describe rg + qmd complementarity). This is a valid narrowing, not a problematic expansion.

### Claim 6: "more reliable than documentation rules that the agent reads at session start and forgets"

This causal claim ("template nudges are more reliable than documentation rules") is not grounded by any linked source. It is presented as a practice observation. No linked source is cited for this specific reliability comparison.

---

## Step 4: Internal consistency

**Definition drift check:** The note uses "queryable" in the Frontmatter section (YAML as queryable structure via grep) and implicitly in the Semantic search section (qmd as a different kind of query). The two uses are compatible — grep queries structured fields, qmd queries semantic content — but the note never explicitly distinguishes them, which could create ambiguity about what "queryable" means.

**Cross-section consistency:** The Discovery-first section says "Does the title work as a claim?" as one of four pre-save checks. The Prose-as-title section acknowledges that multi-claim documents get topical titles. These are consistent — the four-question check applies to notes, and multi-claim documents are an acknowledged exception. No contradiction.

**Summary faithfulness:** The opening line ("Patterns that have proven valuable in practice") faithfully frames the body as a collection of proven patterns. No tensions are elided.

**Frontmatter path discrepancy:** The Frontmatter section uses the path `docs/notes/` in its example grep commands (`rg '^areas:.*architecture' docs/notes/`), while the rest of the KB uses `kb/notes/`. This is an internal inconsistency — either the examples are stale (from a time when the directory was called `docs/`) or they refer to a different project context.

---

WARN:
- [Completeness] The note claims to catalog "patterns that have proven valuable in practice" but omits several patterns that appear proven within this KB: link relationship semantics (since/because/contradicts), progressive disclosure / loading hierarchy, and the `/connect` post-save workflow. These are at least as operationally significant as the patterns included. The collection's implicit scope is underspecified — it is unclear whether omission means "not proven" or "not yet documented here."
- [Internal consistency] The Frontmatter section uses example path `docs/notes/` in grep commands, but the KB's actual path is `kb/notes/`. This is either a stale example from a prior directory structure or a copy from a different project context. Either way it would mislead a reader who tries to run the commands.

INFO:
- [Completeness] The Discovery-first four questions (Claim 9) test findability at the moment of creation but do not address temporal findability — whether the note remains discoverable as terminology drifts over time. This may be intentional scoping, but the note presents the four questions as a complete check without qualifying their temporal limitation.
- [Completeness] The Discovery-first four questions focus on navigation-based findability (titles, indexes, links) but do not explicitly test search-based findability (keyword or semantic). The description question partially covers this, but the gap between "description adds information" and "description contains searchable terms" is meaningful.
- [Grounding] The what-works note describes claim-titled notes making "the graph self-documenting." The linked source (title-as-claim-enables-traversal-as-reasoning.md) never uses the term "self-documenting" — it describes "scanning file tree = scanning arguments." The inference is reasonable but is the what-works note's own vocabulary, not the source's.
- [Grounding] Claim 6 ("template nudges are more reliable than documentation rules that the agent reads at session start and forgets") is presented as established practice knowledge but is not grounded by any linked source. It reads as an observation from experience, which is fine for a review-type note, but a reader might mistake it for a sourced finding.

PASS:
- [Grounding] Claim 4 (multi-claim documents get topical titles) accurately reflects the linked source title-as-claim-enables-traversal-as-reasoning.md, which devotes a full section to this boundary condition with the same reasoning.
- [Grounding] Claim 13 (files as source of truth with derived indexes) is nearly verbatim from files-not-database.md. Attribution is accurate and the domain narrowing is valid.
- [Internal consistency] The Prose-as-title section's acknowledgment of multi-claim exceptions is consistent with Discovery-first's "title as claim" check — the exception is scoped to specs/frameworks, not notes, so no contradiction arises.
- [Internal consistency] The opening summary ("Patterns that have proven valuable in practice") faithfully frames the body content. No tensions are elided between summary and body.
- [Internal consistency] No definition drift detected across sections for key terms (template, frontmatter, semantic search). Each term is used consistently within its section.

Overall: 2 warnings, 4 info
===
