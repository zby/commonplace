=== SEMANTIC REVIEW: backlinks.md ===

Claims identified: 14

## Step 1: Claims extracted

1. [The gap] "no note knows who links TO it" -- scope claim about the current system.
2. [The gap] "An agent reading `deploy-time-learning-the-missing-middle.md` -- which is referenced by 10+ files -- sees only the notes it cites, not the notes that cite it." -- specific factual claim (10+ files).
3. [The gap] "The system provides grep-based discovery (`rg 'note-title.md' --glob '*.md'`), but that's a manual step agents have to think to perform." -- causal claim: manual grep is a cognitive-cost barrier.
4. [Use case enumeration] Four concrete use cases: hub identification, source-to-theory bridge, impact assessment, tension surfacing. Implicit scope claim: these are THE concrete use cases.
5. [Non-use-cases] Three non-use-cases: creating new notes, orphan detection, index maintenance. Implicit scope claim: backlinks don't help with these.
6. [Source-to-theory bridge] "The new `docs/sources/` directory stores ingested external references." -- factual claim about directory name.
7. [Source-to-theory bridge] "Ingest reports link TO KB notes (e.g., koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining)" -- specific factual attribution.
8. [Design options] Four design options: A (generated report), B (generated footer), C (manual bidirectional), D (hybrid). Implicit scope claim: these cover the design space.
9. [Option B] "similar to how `sync_topic_links.py` generates Topics footers from frontmatter areas" -- factual claim about existing tool behavior.
10. [Option B] "Precedent: ADR-001 (generate topic links from frontmatter)" -- factual attribution to an ADR.
11. [Option C] "44% of notes currently lack Relevant Notes sections at all" -- specific quantitative claim.
12. [Trade-offs] "The system prioritises inline links as prose." -- definitional claim about system values.
13. [Trade-offs] "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes." -- factual claim about system behavior.
14. [Relevant Notes] "backlinks are a special case of link visibility; the 'click decision' framework applies to deciding whether to follow an inbound link too" -- causal/extension claim about the link-contracts-framework.

## Step 2: Completeness and boundary cases

The note's implicit space is "where backlinks would help agents working in the KB." The four use cases and three non-use-cases together claim to cover the space of agent tasks with respect to inbound link visibility.

Boundary cases tested:

**BC1: Staleness detection -- "has this note been superseded?"** An agent reading a note might want to know if any newer note contradicts, replaces, or refines it. This overlaps with use case 4 (tension surfacing) for contradiction, but "superseded by" is different from "contradicts." A note might be quietly deprecated by a newer, better note that extends rather than contradicts it. The note's framing of tension surfacing emphasizes "disagrees," not "replaces." This is ambiguously covered.

**BC2: Synthesis opportunity detection -- "are enough notes converging on this topic to warrant a synthesis note?"** The source-to-theory bridge (use case 2) is framed as sources pointing at theory notes. But KB notes also point at each other, and convergence of several notes toward the same concept is a synthesis signal. This is partially covered by hub identification (use case 1), but hub identification is framed as reading-time orientation, not as a trigger for writing. An agent deciding "should I write a synthesis note?" would benefit from backlinks differently than an agent deciding "how carefully should I read this?"

**BC3: A note with zero outbound links but many inbound links.** Hub identification (use case 1) would flag this as foundational. But the interesting boundary is: a note with zero outbound links might be a definitional anchor (like a vocabulary term) that many notes depend on but that itself depends on nothing. The note doesn't distinguish between hubs-by-authority (many notes build on this) and hubs-by-centrality (many notes touch this topic).

**BC4: Inbound links from outside kb/notes/ -- e.g., from kb/instructions/ or CLAUDE.md.** The note's examples focus on note-to-note and source-to-note backlinks. Instructions that reference a note (e.g., WRITING.md linking to a type template) create a different kind of dependency. Editing such a note could break an instruction, not just another note. The note's analysis of "what breaks if I change this?" (use case 3) would miss these cross-directory dependencies.

**BC5: The simplest case -- a single inbound link.** Does backlink machinery justify itself for a note with one inbound link? Hub identification says no (it's a leaf). The note doesn't discuss a threshold below which backlinks add noise rather than signal.

## Step 3: Grounding alignment

**G1: link-contracts-framework.md** -- The backlinks note claims the link-contracts framework's "click decision" applies to inbound links too. The link-contracts note (lines 19-29) defines the click decision as 5 questions a reader asks when encountering a link: "What is it? Why should I click now? What will it cost? How trustworthy is it? What happens if I don't click?" This framework is explicitly about outbound links encountered during reading. The extension to inbound links (backlinks) is the backlinks note's own inference. It is a reasonable inference -- the same questions apply when an agent sees "this note is referenced by X" -- but the link-contracts note does not discuss inbound links or backlinks at all.

**G2: koylanai-personal-brain-os.ingest.md** -- The backlinks note claims this ingest report "links to storing-llm-outputs-is-constraining." Verified: the ingest report's "Already established" connections section includes `[storing-llm-outputs-is-constraining](../notes/storing-llm-outputs-is-constraining.md)` with relationship type "exemplifies." Attribution is accurate.

**G3: maintenance-operations-catalogue-should-stage-distillation-into-instructions.md** -- The backlinks note claims orphan detection is "already handled by the existing grep-based maintenance checks" in this catalogue. Verified: the catalogue includes an "Orphan note detection" section with a bash script that greps for notes with no inbound links. Attribution is accurate. However, the backlinks note says backlinks "don't unlock new capability" for orphan detection, which is a stronger claim than the source supports -- the source just provides a procedure, it doesn't claim the procedure is sufficient.

**G4: 001-generate-topic-links-from-frontmatter.md** -- The backlinks note references this as "ADR-001" and links to it as a precedent for option B. This file does not exist in the repository. The ADR directory contains only ADRs 002-005. The note cannot be grounded because the source is missing. The claim "ADR-001 (generate topic links from frontmatter) -- same pattern, different link type" cannot be verified.

**G5: "docs/sources/" path claim** -- The note says "The new `docs/sources/` directory stores ingested external references." The actual directory is `kb/sources/`, not `docs/sources/`. This is a factual error about the system's own structure.

## Step 4: Internal consistency

**IC1: The non-use-case for orphan detection vs. use case 1 (hub identification).** The note says orphan detection is NOT a backlink use case because "already handled by grep-based maintenance checks." But hub identification IS a use case, and the difference between "zero inbound links" (orphan) and "many inbound links" (hub) is a matter of degree on the same measurement. If backlinks help with hub identification by showing inbound link counts, they trivially also improve orphan detection by making zero-inbound-link status visible at read time. The note draws a categorical boundary (orphan detection = not a use case, hub identification = use case) on what is actually a continuum. The note's defense is that orphan detection "doesn't unlock new capability," but by that standard, neither does hub identification -- grep already provides inbound link counts on demand.

**IC2: The 44% statistic appears in two places (option C and the Trade-offs section) and is used consistently** in both to argue that manual backlink maintenance would be unreliable. Internal use is consistent, though the number itself is stale (see WARN below).

**IC3: The note's framing of "visible at reading time" vs "searchable" is consistent throughout.** The gap section, use cases, and design options all maintain the same distinction. No definition drift detected.

---

WARN:
- [Completeness] The use-case enumeration omits staleness/supersession detection. The note frames tension surfacing (use case 4) around "contradicts" links, but a note superseded by a newer, better note that "extends" rather than "contradicts" would not be caught by that framing. An agent reading an outdated note would benefit from seeing "note Y extends and replaces the claim here" via backlinks, and this is distinct from the four listed use cases.
- [Grounding] The note cites "ADR-001 (generate topic links from frontmatter)" as precedent for option B, but the file `001-generate-topic-links-from-frontmatter.md` does not exist in the repository. The grounding claim cannot be verified. If the ADR was removed or renamed, the precedent argument for option B hangs on a missing source.
- [Grounding] The note states "The new `docs/sources/` directory" but the actual path is `kb/sources/`. This is a factual error about the system's own directory structure.
- [Internal consistency] The note categorically separates orphan detection (non-use-case) from hub identification (use case 1), but both depend on inbound link counts. The argument that orphan detection "doesn't unlock new capability" applies equally to hub identification, since grep already provides both. The note's own logic for dismissing orphan detection undermines the parallel use case it promotes.
- [Grounding] The "44% of notes currently lack Relevant Notes sections at all" figure appears to be stale. Current data shows approximately 184 of ~218 notes (including subdirectories) have "Relevant Notes:" sections, putting the without-rate at roughly 16%, not 44%. The 44% figure may have been accurate when written but weakens the maintenance-burden argument for option C as stated.

INFO:
- [Completeness] The use-case enumeration does not consider inbound links from outside kb/notes/ (e.g., from kb/instructions/, CLAUDE.md, or scripts). An agent assessing impact before editing (use case 3) would miss cross-directory dependencies. This is a boundary case that could expand the scope of the impact-assessment use case.
- [Completeness] The design-options enumeration (A-D) does not consider a query-time / on-demand tool approach: an agent skill or script that, given a note path, returns its inbound links on request without any stored artifact or footer. This would be distinct from option A (which produces a report) and lighter than option B (which modifies notes). It sits between A and B but is not clearly covered by either.
- [Grounding] The Relevant Notes link to link-contracts-framework claims "the 'click decision' framework applies to deciding whether to follow an inbound link too." The link-contracts note's click decision framework is framed entirely around outbound links encountered during reading. The extension to inbound links is a plausible inference but is the backlinks note's own move, not stated in the source.

PASS:
- [Grounding] The claim that koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining was verified against the ingest report. Attribution is accurate, including the direction of the link (ingest report links TO KB note, not vice versa).
- [Grounding] The claim that orphan detection is handled by grep-based maintenance checks was verified against the maintenance operations catalogue, which contains a bash script for exactly this purpose.
- [Grounding] The "10+ files" reference count for deploy-time-learning-the-missing-middle.md was verified: 46 files in kb/notes/ reference it. The claim is accurate and conservative.
- [Internal consistency] The distinction between "visible at reading time" and "searchable on demand" is maintained consistently across the gap section, use cases, and design options. No definition drift detected.
- [Internal consistency] The design options (A-D) form a coherent spectrum from fully automated/invisible to fully manual/semantic, and the trade-offs section maps cleanly onto this spectrum without contradicting any option's characterization.

Overall: 5 warnings, 3 info
===
