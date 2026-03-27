---
note: kb/notes/backlinks.md
gate: semantic/completeness-boundary-cases
---

The note contains three enumerations: four use cases, three non-use-cases, and four design options. Each is tested below.

## Use cases

The grounding definition (implicit): situations where knowing which notes link TO a given note would help an agent navigate or act.

Boundary cases tested:

**Simplest instance — a note with exactly one inbound link.** The open questions section raises the threshold question directly ("is there a threshold below which backlinks add noise rather than signal?"), but doesn't categorize single-inbound-link notes into the use case taxonomy. Is one inbound link enough for hub identification? For impact assessment? The use cases say "3 notes extend this, 2 exemplify it" (hub) and "3 notes use this as foundation" (impact), implying count matters. The note defers the threshold question without placing it in relation to the use cases. INFO: the boundary between "backlink-worthy" and "noise" intersects all four use cases but is handled only as an open question, not as a scoping constraint on which use cases apply.

**Adjacent concept: deletion impact.** Use case 3 (impact assessment) is framed as "what breaks if I *change* this?" — editing a claim. Deletion is a stricter action (all dependents break regardless of how the change is framed). The note doesn't treat deletion as a variant of impact assessment or exclude it as a non-use-case. INFO: deletion impact is a boundary case of impact assessment that falls just outside the stated framing ("change" vs. "delete") without being addressed.

**Adjacent concept: co-citation / similarity.** Notes that are frequently co-cited together are thematically related. An agent on note X could find similar notes by examining what other notes link to X's same hub targets. This is distinct from the four use cases (it's about X's peers, not X's dependents or sources). The non-use-cases section doesn't address it. INFO: co-citation discovery is adjacent to but distinguishable from the stated use cases; its absence isn't an unaddressed gap given the note doesn't claim exhaustive coverage, but it sits near the boundary.

## Non-use-cases

**Orphan detection boundary:** "Backlinks measure the same thing as hub identification (inbound link count), but orphan detection doesn't need read-time visibility." This claim conflates the underlying data (inbound link count) with the use case. Hub identification asks "is this count high enough to signal centrality?" Orphan detection asks "is this count zero?" The underlying data is identical, but treating them as measuring "the same thing" implies the use cases are more interchangeable than they are. WARN: the sentence equates hub identification and orphan detection by their data substrate while the actual distinction is threshold and purpose. This understates why orphan detection is a non-use-case (it's a batch task, not a read-time need) and overstates the similarity.

## Design options

The design space is implicitly structured along two axes: visibility (at read time vs. on demand) and authorship (machine-generated vs. human-curated). The four options occupy three of the four quadrants (on-demand/generated = A; read-time/generated = B; read-time/manual = C; read-time/hybrid = D). The fourth quadrant — on-demand/manual — is not named as an option.

**Between A and B: always-loaded index file.** A standalone backlinks index (e.g., `kb/backlinks-index.md`), loaded at session start rather than embedded in individual notes, sits between option A (run a script) and option B (in the note). This is a design option the note doesn't consider. INFO: the design space skips a plausible hybrid where the data is pre-computed (like B) but stored separately (like A), making it load-optional rather than forced into every note.

**Between C and D: LLM-inferred relationship annotation.** A script generates the bare inbound link list (option D's first layer), and an LLM pass annotates relationship types rather than waiting for human agents to do it sporadically. This is a point between C (manual semantics) and D (machine list + optional human enrichment). INFO: the possibility of automated semantic annotation isn't explored — it would change D's core weakness ("unannotated backlinks are noisy") without adding the maintenance burden of C.

## Overall

WARN on the orphan-detection framing conflating data substrate with use-case equivalence. INFOs on deletion impact (boundary of use case 3), the always-loaded index option (gap in design space), and LLM annotation (gap between C and D). The use cases and design options are otherwise well-bounded for a speculative note.
