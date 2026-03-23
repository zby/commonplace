=== SEMANTIC REVIEW: a-knowledge-base-should-support-fluid-resolution-switching.md ===

Claims identified: 12

1. "Good thinking is not staying at one level of abstraction -- it is constantly moving between levels" (opening paragraph)
2. "A knowledge base that supports good thinking must support this motion fluidly" (opening paragraph)
3. "Titles vs bodies are a resolution pair" -- claim titles give zoomed-out view, note bodies give zoomed-in (body, "Titles vs bodies" section)
4. "following links between claim titles reads as a chain of reasoning at the abstract level" (body, "Titles vs bodies" section)
5. "Indexes and notes operate at different resolutions" (body, "Indexes and notes" section)
6. "local link-following is narrow and contextual; search and index browsing are broad and orienting" -- attributed to two-kinds-of-navigation (body, "Indexes and notes" section)
7. "Link semantics encode zoom direction" -- "since" zooms into foundation, "extends" zooms out to generalization, "contradicts" shifts laterally (body, "Link semantics" section)
8. "Progressive disclosure is a resolution gradient" (body, "Progressive disclosure" section)
9. "resolution-switching fluidity" as a quality criterion complementing retrieval accuracy (evaluative criterion section)
10. Four concrete symptoms of poor resolution-switching enumerated as exhaustive list of symptoms (evaluative criterion section)
11. "Resolution-switching is the navigation skill that makes discovery possible" (connection to discovery section)
12. "A KB that traps you at one level suppresses discovery" (connection to discovery section)

WARN:
- [Completeness] The note enumerates four mechanisms that serve resolution-switching (titles/bodies, indexes/notes, link semantics, progressive disclosure) and frames them as "several mechanisms" the KB "already has." However, the note's own description field and frontmatter mention `tags`, which provide a cross-cutting resolution layer not discussed. Tags group notes orthogonally to the index hierarchy and enable resolution switching along a different axis (thematic vs structural). A reader treating this list as comprehensive would miss an existing mechanism.

- [Completeness] The four symptoms of poor resolution-switching ("Notes with no outbound links," "Indexes with bare links," "Topic-titled notes," "Missing relationship articulation") are presented as "concrete symptoms" but omit a plausible symptom implied by the note's own framework: notes with no *inbound* links. A note nobody links to is invisible from the zoomed-out view -- you can only reach it via search, which means the zoom-in path from indexes/other notes is broken. This is the converse of the first listed symptom (no outbound links = can't zoom out) but is not mentioned.

- [Grounding] The note says "Link semantics encode zoom direction" and attributes directional meaning: "'Since [X]' zooms into a foundation -- following it takes you deeper" and "'This extends [Y]' zooms out toward a generalization." The linked source (link-strength-is-encoded-in-position-and-prose.md) does discuss "since" and "extends" as relationship words, but it frames them as *strength signals* and *role indicators* (premise vs structural vs tension), not as zoom directions. The source says "since [X]" indicates a premise link with strongest weight; it does not say anything about zooming in or out. The directional/spatial interpretation (zoom in, zoom out, shift laterally) is the note's own inference layered on top of the source's vocabulary. This is reasonable but could mislead a reader into thinking the zoom-direction framing comes from the link-strength note.

INFO:
- [Completeness] The note discusses descriptions only in passing (the progressive disclosure section mentions "on-demand descriptions" as a medium layer). The description field is arguably an intermediate resolution layer between title and body -- it gives more than the title but less than the full note. The instruction-specificity note explicitly places descriptions in the loading hierarchy. The resolution-switching note could be clearer about whether descriptions constitute a distinct resolution level or are subsumed by the title/body pair.

- [Completeness] The note's boundary cases for "resolution-switching" are entirely about human-like reading navigation (zooming in, zooming out, following links). Search-based resolution switching -- where an agent adjusts query specificity (broad keyword vs narrow phrase) to control the resolution of results -- is not discussed. The two-kinds-of-navigation source does describe search as a distinct navigation mode, and the note acknowledges it ("search and index browsing are broad and orienting"), but search is only placed at one resolution level (broad). In practice, search can operate at varying resolutions depending on query specificity.

- [Grounding] The note says "This is the two kinds of navigation distinction: local link-following is narrow and contextual; search and index browsing are broad and orienting." The source (two-kinds-of-navigation.md) does describe these two modes, but it frames indexes as sitting "in between" -- "local navigation in form" but functioning "like a curated search result." The note here groups indexes with search as "broad and orienting," which flattens the source's three-tier framing (links / indexes-as-bridge / search) into a two-tier framing (narrow / broad). The simplification is not wrong but loses a nuance the source explicitly highlights.

- [Internal consistency] The "connection to discovery" section says "you can only see the particular as an instance of the general if you can move between the two levels." This implies two levels. But the discovery source (discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) describes three depths of abstraction (shared feature, shared structure, generative model), and the note itself discusses multiple levels throughout. The phrase "the two levels" appears to refer specifically to "the particular" and "the general" from the discovery note's title, which is accurate, but using "two" in a note that is otherwise about fluid movement across many levels creates a minor ambiguity.

PASS:
- [Grounding] The attribution to title-as-claim-enables-traversal-as-reasoning.md is accurate. That source explicitly says "following links between them reads as a chain of reasoning" and "the file tree becomes a scan of arguments" -- the note's claim that "following links between claim titles reads as a chain of reasoning at the abstract level" faithfully represents this.
- [Grounding] The attribution to instruction-specificity-should-match-loading-frequency.md is accurate. That source explicitly describes a four-level loading hierarchy (CLAUDE.md, skill descriptions, skill bodies, task-specific docs) layered from always-loaded/broad to on-demand/narrow. The note's characterization of this as "a resolution gradient" is a legitimate reframing, and the source's content supports it.
- [Grounding] The characterization of the discovery note's "three depths of abstraction" is accurate. The source does describe shared feature, shared structure, and generative model as three abstraction depths in connection-making.
- [Internal consistency] The note's definition of "resolution-switching" remains stable throughout. It consistently means movement between abstraction levels (broad/narrow, general/specific, landscape/territory). No definition drift detected.
- [Internal consistency] The evaluative criterion section follows logically from the mechanisms section -- the symptoms of poor resolution-switching are genuine failure modes of the four mechanisms described earlier (no outbound links breaks zoom-out via link semantics; bare index links break zoom-in via indexes; topic titles break the title/body resolution pair; missing relationship articulation breaks link-semantic zoom direction). The internal logic is sound.

Overall: 3 warnings, 4 info
===
