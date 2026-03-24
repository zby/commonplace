<!-- REVIEW-METADATA
note-path: kb/notes/backlinks.md
last-full-review-note-sha: 435bea6c25549bd7ec10d7bf8217c14df2144be6
last-full-review-note-commit: cfa5a80e97f831f42b58fa223260538a6c79282f
last-full-review-at: 2026-03-24T12:00:00+00:00
last-accepted-note-sha: 435bea6c25549bd7ec10d7bf8217c14df2144be6
last-accepted-note-commit: cfa5a80e97f831f42b58fa223260538a6c79282f
last-accepted-at: 2026-03-24T12:00:00+00:00
last-acceptance-kind: full-review
review-type: semantic-review
-->

=== SEMANTIC REVIEW: backlinks.md ===

Claims identified: 15

## Step 1: Claims extracted

1. [The gap] "no note knows who links TO it" -- scope claim about current system capability.
2. [The gap] "An agent reading `deploy-time-learning-the-missing-middle.md` -- referenced by 40+ files" -- specific quantitative claim.
3. [The gap] "Grep-based discovery exists ... but agents have to think to run it" -- causal claim: grep imposes an initiative cost that reduces discovery.
4. [Use cases] Four use cases enumerated: hub identification, source-to-theory bridge, impact assessment, tension surfacing. Implicit scope claim: these are the concrete use cases where backlinks help agents.
5. [Use case 1] "Seeing '3 notes extend this, 2 exemplify it, 1 contradicts it' would change how carefully the agent reads and whether it risks editing" -- causal claim linking inbound visibility to reading behavior.
6. [Use case 2] "Ingest reports in `kb/sources/` link TO KB notes (e.g., koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining)" -- specific factual attribution about an existing link direction.
7. [Use case 2] "the theory note doesn't know it has practitioner evidence pointing at it" -- claim about current system state.
8. [Non-use-cases] Three non-use-cases: creating new notes, orphan detection, index maintenance. Implicit scope claim: backlinks do not help with these.
9. [Non-use-cases / orphan detection] "a batch maintenance task already handled by grep-based checks" -- factual attribution to existing tooling, plus "Backlinks measure the same thing as hub identification" -- equivalence claim.
10. [Design options] Four options (A-D) enumerated. Implicit scope claim: these cover the design space for backlink implementation.
11. [Option B] "similar to how `sync_topic_links.py` generates Topics footers from frontmatter" -- factual claim about existing tooling as precedent.
12. [Option C] "~16% of notes still lack even outbound Relevant Notes sections" -- specific quantitative claim used in an a fortiori argument.
13. [Trade-offs] "The system prioritises inline links as prose" -- definitional claim about system values.
14. [Trade-offs] "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes" -- factual claim about architectural boundary.
15. [Relevant Notes] "backlinks are a special case of link visibility; the 'click decision' framework applies to deciding whether to follow an inbound link too" -- extension claim mapping an outbound-link framework onto inbound links.

## Step 2: Completeness and boundary cases

The note implicitly defines a space of "where backlinks would concretely help agents working in the KB." The four use cases and three non-use-cases together claim to partition agent tasks with respect to inbound link visibility. The four design options claim to cover implementation approaches.

**BC1: Staleness/supersession detection.** An agent reading a note might benefit from seeing that a newer note extends or supersedes it -- not by contradicting it (use case 4) but by moving past it. A note quietly outgrown by a successor that "extends" rather than "contradicts" would not be caught under use case 4's framing of "who disagrees with this?" This is a distinct read-time need that sits outside all four enumerated use cases.

**BC2: Cross-directory inbound links (from kb/instructions/, CLAUDE.md, or scripts).** The note's examples focus on note-to-note and source-to-note backlinks. But an instruction referencing a note creates a dependency that use case 3 (impact assessment) should catch. Editing a note depended on by an instruction is arguably higher-stakes than editing one depended on by another note, yet the note implicitly scopes its analysis to kb/notes/ and kb/sources/.

**BC3: A note with exactly one inbound link (the minimal case).** Use case 1 (hub identification) emphasizes the high-inbound-count scenario ("40+ files," "10 other notes build on it"). The Open Questions section acknowledges a noise threshold, but the use cases themselves do not address whether single-inbound-link notes benefit from backlink visibility. This is the simplest possible instance of the concept.

**BC4: An on-demand interactive tool approach.** The four design options span batch report (A), stored footer (B), manual links (C), and hybrid (D). None describes an on-demand agent skill that, given a note path, returns its inbound links interactively without producing a stored artifact or modifying footers. This sits between A (batch, no read-time visibility) and B (stored, always visible) and could satisfy use cases 1 and 3 without the maintenance burden of B or the invisibility of A.

**BC5: Value without relationship types.** Use case 3 explicitly depends on relationship semantics ("3 notes use this as foundation ... 2 notes merely exemplify it -- those are safe"). Use case 1's example also uses typed relationships ("3 notes extend this, 2 exemplify it, 1 contradicts it"). But the design options acknowledge that relationship types "can't be inferred mechanically." The boundary case is: does the value proposition of use cases 1 and 3 hold with bare counts only, or does it degrade to something little better than grep output? The note does not resolve this tension.

## Step 3: Grounding alignment

**G1: link-contracts-framework.md (Relevant Notes link).** The note claims "the 'click decision' framework applies to deciding whether to follow an inbound link too." The link-contracts note defines the click decision as five questions a reader asks when encountering a link. This framework is explicitly about outbound links a reader encounters during reading. It never mentions inbound links, backlinks, or the scenario of an agent evaluating links pointing at the note it is currently reading. The extension to inbound links is the backlinks note's own inference. The inference is plausible -- the same five questions would apply when an agent sees "this note is referenced by X" -- but it is not stated in the source.

**G2: koylanai-personal-brain-os.ingest.md (use case 2 example).** The note claims this ingest report "links to storing-llm-outputs-is-constraining." Verified: the ingest report's "Already established" section includes the link with relationship type "exemplifies." The attribution is accurate, including the directionality.

**G3: maintenance-operations-catalogue-should-stage-distillation-into-instructions.md (non-use-case: orphan detection).** The note claims orphan detection is "a batch maintenance task already handled by grep-based checks" and links to this catalogue. Verified: the catalogue contains an "Orphan note detection" section with a bash script that greps for notes with no inbound links. The attribution is accurate.

**G4: generate-instructions-at-build-time.md (Relevant Notes link, option B precedent).** Option B references `sync_topic_links.py` as precedent for generated footer sections and the Relevant Notes footer links to this note as a "related pattern: deterministic generation from structured data." The generate-instructions note discusses build-time generation as a general pattern. The connection is reasonable -- both involve deterministic generation -- but the specific domains differ.

**G5: The /ingest pipeline boundary claim.** The Trade-offs section states "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes." Verified against the koylanai ingest report: connections are listed there, and `storing-llm-outputs-is-constraining.md` does not contain a backlink to the ingest report. Consistent with observed behavior.

## Step 4: Internal consistency

**IC1: Non-use-case (orphan detection) vs. use case 1 (hub identification).** The note places orphan detection in the non-use-case list while promoting hub identification as use case 1. The stated distinction is that orphan detection "doesn't need read-time visibility" while hub identification requires it. However, the note also states "Backlinks measure the same thing as hub identification (inbound link count)," conceding the underlying data is identical. The categorical separation rests entirely on a presentation-layer argument (read-time vs. batch). This is defensible, but the note's own equivalence statement weakens the categorical boundary.

**IC2: Use case 3 depends on relationship types, but the design options show they are hard to get.** Use case 3's value proposition presupposes typed relationships. Option B's cons note that "relationship semantics can't be inferred mechanically." Option C provides types but is unreliable ("~16% of notes still lack even outbound Relevant Notes sections"). Option D defers typing to optional agent annotation. The note does not resolve whether use case 3 delivers meaningful value without relationship types.

**IC3: Consistent use of "visible at reading time" vs. "searchable on demand."** The gap section, use cases, design options, and trade-offs all maintain this distinction. No definition drift detected.

**IC4: Open Questions section vs. use case ordering.** The Open Questions section frames hub identification and source bridging as "highest value" and tension surfacing as "lower frequency." This is consistent with the ordering and emphasis of the use cases (1-4) throughout the note.

---

WARN:
- [Completeness] The use-case enumeration does not cover staleness/supersession detection. Use case 4 (tension surfacing) is framed around "who disagrees with this?" but a note superseded by a newer note that extends rather than contradicts it would not be caught. This is a distinct read-time need outside all four listed use cases.
- [Internal consistency] The note places orphan detection in the non-use-case list but concedes it and hub identification (use case 1) "measure the same thing" (inbound link count). The distinction rests on whether read-time visibility matters, but the note's own equivalence statement undermines the categorical separation without developing the presentation-layer argument that would restore it.

INFO:
- [Completeness] The use cases implicitly scope to kb/notes/ and kb/sources/ without addressing inbound links from kb/instructions/, CLAUDE.md, or scripts. Use case 3 (impact assessment) would miss these higher-stakes dependencies.
- [Completeness] The design options (A-D) do not include an on-demand interactive tool/skill approach -- an agent command that returns inbound links for a given note without producing a stored artifact or modifying footers. This would sit between options A and B and could satisfy use cases 1 and 3 without the trade-offs of either.
- [Completeness] The value proposition of use cases 1 and 3 depends on relationship types (extends, exemplifies, contradicts), but the design options show these are hard to obtain mechanically. The note does not address whether bare inbound counts (without relationship types) are sufficient for these use cases or whether they degrade to glorified grep output.
- [Grounding] The Relevant Notes claim that "the 'click decision' framework applies to deciding whether to follow an inbound link too" is a reasonable inference, but the link-contracts-framework note discusses only outbound links encountered during reading and never mentions inbound links or backlinks. The extension is the backlinks note's own move, not an attribution.

PASS:
- [Grounding] The claim that koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining was verified against the ingest report. Attribution is accurate, including link direction.
- [Grounding] The claim that orphan detection is handled by grep-based maintenance checks was verified against the maintenance operations catalogue, which contains an orphan detection section with a bash script.
- [Grounding] The claim that the /ingest pipeline keeps connections in the ingest report rather than modifying KB notes was verified by checking both the ingest report and the referenced KB note.
- [Grounding] The link to generate-instructions-at-build-time.md as a "related pattern: deterministic generation from structured data" is a reasonable analogy, though the source note discusses path placeholder resolution rather than backlink generation specifically.
- [Internal consistency] The distinction between "visible at reading time" and "searchable on demand" is maintained consistently across all sections. No definition drift detected.
- [Internal consistency] The design options (A-D) form a coherent spectrum from fully automated/invisible to fully manual/semantic, and the trade-offs section maps cleanly onto this spectrum.
- [Internal consistency] The open questions section's priority ordering is consistent with the emphasis and ordering of the use cases throughout the note.

Overall: 2 warnings, 4 info
===
