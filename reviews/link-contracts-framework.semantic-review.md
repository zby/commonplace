=== SEMANTIC REVIEW: link-contracts-framework.md ===

Claims identified: 14

1. "When a reader encounters a link, they're silently asking" five questions (What is it, Why click, What cost, How trustworthy, What if I don't click) — enumeration in "Every link needs to earn a click decision"
2. The "link contract" is making answers to those five questions cheap — definition in same section
3. Inline link minimum bar = descriptive anchor text + local context — enumeration in "Link contract: minimal information"
4. Annotated link = short "decision hint" next to the link: what it is + why + cost — definition in same section
5. Link intent taxonomy has 9 items (Definition, How-to, Reference, Example, Rationale, Evidence, Tool, Related, Index/Hub) — enumeration in "Link intent taxonomy"
6. Once links have intent, you can enforce three rules (term -> definition, instruction -> how-to, claim -> evidence) — enumeration in same section
7. Four recommendations for making link decisions obvious — enumeration in "Making link decisions obvious"
8. Index page quality bar has three requirements — enumeration in "Index page quality bar"
9. Agents do constrained exploration; five preference rules follow from intent and cost metadata — claim + enumeration in "LLM/agent implications"
10. Automated tests split into three categories: Deterministic, LLM rubric, Corpus compatibility — taxonomy in "Automated tests for linking"
11. "Five rules that work" — enumeration in final section
12. See distilled observations in agents-navigate-by-deciding-what-to-read-next and two-kinds-of-navigation — attribution claim in intro
13. Annotated link pattern conveys "what it is + why + cost" — definition in "Link contract: minimal information"
14. The note frames itself as "source material" and "reference framework" — scope claim in title and intro

WARN:
- [Completeness] The "five questions a reader silently asks" omit a question that the note's own content elsewhere treats as important: "How does this relate to what I'm reading?" The note's own "Making link decisions obvious" section recommends "when to click" language and contextual placement, which addresses the relationship between the link target and the reader's current task — a question distinct from the five listed. The five questions are framed as destination-oriented (what is it, what will it cost) but the decision also depends on the reader's current state and goal. This is arguably the most important question for an agent ("Is this relevant to my current task?"), and agents-navigate-by-deciding-what-to-read-next makes it the central concern: "how likely is this pointer to lead somewhere relevant." The five-question enumeration covers the target but not the reader-target fit.

- [Completeness] The link intent taxonomy lists "Related: nearby topic, optional expansion" as a category. However, the KB's own CLAUDE.md convention states: "'Related' is not a relationship." The note offers "Related" as a valid link intent with a real definition ("nearby topic, optional expansion"), while the broader KB convention treats it as a non-relationship. These serve different purposes (the note is about reader-facing link types; CLAUDE.md is about authoring discipline), but the tension is worth flagging since this note is positioned as reference material for the KB's own linking practices. Adopting this taxonomy as-is would conflict with the existing convention.

- [Grounding — scope mismatch] The intro says "See agents-navigate-by-deciding-what-to-read-next and two-kinds-of-navigation for the distilled observations." This implies those two notes are distillations of this source material. However, the relationship is looser than that. agents-navigate-by-deciding-what-to-read-next develops an independent argument about pointer context and navigation cost that goes well beyond this note's framework (it covers skills, search tools, index entries, and frontmatter descriptions — none of which appear here). two-kinds-of-navigation distinguishes local vs long-range navigation, a distinction this note does not make. The distilled notes are not distillations of this source; they are independent arguments that share thematic overlap. The attribution overstates the derivation relationship.

INFO:
- [Completeness] The "Five rules that work" is labeled as a self-contained summary, but rule 5 ("If something is required to proceed, summarize it — don't outsource to a link") introduces a concept not developed anywhere else in the note: the distinction between required and optional links. The "click decision" section touches on it with question 5 ("What happens if I don't click?"), but the note never develops a framework for distinguishing required from optional dependencies. Rule 5 effectively imports a design principle that the body doesn't ground.

- [Completeness] The "LLM/agent implications" section lists five preference heuristics but does not mention search at all. The note covers inline links, annotated links, index pages, and automated tests — but an agent's first interaction with the knowledge base is often search, not link-following. two-kinds-of-navigation identifies search as one of the two fundamental navigation modes, yet this note's agent guidance assumes the agent is already reading a document and encountering links.

- [Completeness] The automated tests taxonomy separates "Deterministic," "LLM rubric," and "Corpus compatibility," but the third category contains items that are deterministic (orphan detection, checking whether index entries have one-line descriptions). The boundary between "Deterministic" and "Corpus compatibility" is unclear — corpus compatibility appears to mean "tests that require understanding the corpus graph" rather than "tests that are non-deterministic," but this is not stated.

- [Internal consistency] The note's title says "Link contracts framework" but the body heading says "Link contracts framework — source material." The frontmatter description calls it a "Reference framework for systematic, testable linking," while the intro says "Saved as reference for when we start building concrete link practices." The note simultaneously frames itself as a framework (ready to use) and as source material (input for future work). This dual framing is understandable for a note capturing external input, but a reader may be uncertain whether to treat the taxonomy and rules as adopted conventions or as candidates under consideration.

PASS:
- [Internal consistency] The five questions in "Every link needs to earn a click decision" align consistently with the annotated link pattern. The annotated link examples each address "what it is + why + cost," which maps to questions 1, 2, and 3. The pattern is coherent.
- [Internal consistency] The link intent taxonomy and the enforcement rules are consistent. Each enforcement rule maps to a taxonomy item: new terms -> Definition, instructions -> How-to, strong claims -> Evidence. No enforcement rule references an intent not in the taxonomy.
- [Internal consistency] The "Five rules that work" are internally consistent with the body. Rules 1-4 each correspond to advice given in earlier sections (banned anchors, decision hints, grouping by intent, index quality bar). No rule contradicts earlier content.
- [Grounding alignment] two-kinds-of-navigation links back to this note as "link contracts source material," confirming the bidirectional reference. The relationship framing in that note is accurate — it treats this note as reference material, not as a source it distills from.
- [Internal consistency] The three automated test categories (Deterministic, LLM rubric, Corpus compatibility) collectively cover the space implied by the note's earlier sections: anchor text quality (deterministic), link purpose clarity (LLM), and graph-level conventions (corpus). No section of the note introduces a testable property that doesn't appear in at least one test category.

Overall: 3 warnings, 4 info
===
