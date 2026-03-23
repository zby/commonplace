<!-- REVIEW-METADATA
note-path: kb/notes/backlinks.md
last-full-review-note-sha: e367c7ce4cbf1c62cfb5dd4da9e357c34e7580b3
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: e367c7ce4cbf1c62cfb5dd4da9e357c34e7580b3
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: backlinks.md ===

Claims identified: 14

## Step 1: Claims extracted

1. [The gap] "no note knows who links TO it" -- scope claim about current system state.
2. [The gap] "An agent reading `deploy-time-learning-the-missing-middle.md` -- referenced by 40+ files -- sees only the notes it cites, not the notes that cite it" -- specific quantitative claim (40+ files).
3. [The gap] "Grep-based discovery exists (`rg 'note-title.md' --glob '*.md'`), but agents have to think to run it" -- causal claim: manual grep imposes a cognitive/initiative cost.
4. [Use-case enumeration] Four concrete use cases: hub identification, source-to-theory bridge, impact assessment, tension surfacing. Implicit scope claim: these are the concrete use cases for backlinks.
5. [Non-use-cases] Three non-use-cases: creating new notes, orphan detection, index maintenance. Implicit scope claim: backlinks don't help with these.
6. [Non-use-cases / orphan detection] "a batch maintenance task already handled by grep-based checks" -- factual attribution to existing maintenance tooling.
7. [Source-to-theory bridge] "Ingest reports in `kb/sources/` link TO KB notes (e.g., koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining)" -- specific factual attribution about an existing link.
8. [Design options] Four design options: A (generated report), B (generated footer), C (manual bidirectional), D (hybrid). Implicit scope claim: these cover the design space.
9. [Option B] "similar to how `sync_topic_links.py` generates Topics footers from frontmatter" -- factual claim about existing tool.
10. [Option C] "~16% of notes still lack even outbound Relevant Notes sections" -- specific quantitative claim.
11. [Trade-offs] "The system prioritises inline links as prose" -- definitional claim about system values.
12. [Trade-offs] "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes" -- factual claim about system architecture boundary.
13. [Open questions] Hub identification and source bridging framed as "highest value"; tension surfacing as "lower frequency" -- relative-priority claim.
14. [Relevant Notes] "backlinks are a special case of link visibility; the 'click decision' framework applies to deciding whether to follow an inbound link too" -- extension claim applied to link-contracts-framework.

## Step 2: Completeness and boundary cases

The note's implicit space is "where backlinks would concretely help agents working in the KB." The four use cases and three non-use-cases together claim to partition agent tasks with respect to inbound link visibility.

**BC1: Staleness/supersession detection -- "has this note been replaced by a better one?"** An agent reading a note might want to know if a newer note extends, refines, or effectively replaces it. Use case 4 (tension surfacing) covers "contradicts" links, but supersession is different from contradiction: a note might be quietly outgrown by a newer note that extends it without disagreeing. The note frames tension surfacing around "who disagrees with this?" which does not capture "who has moved beyond this?"

**BC2: Synthesis trigger detection -- "are enough inbound links converging here to warrant a synthesis note?"** Use case 2 (source-to-theory bridge) is framed as sources grounding theory. Use case 1 (hub identification) is framed as reading-time orientation. But a distinct use is: an agent seeing many inbound links from different angles might recognise a synthesis opportunity. This is partially covered by use case 1 but sits between use cases 1 and 2 without clearly belonging to either.

**BC3: Cross-directory inbound links -- links from kb/instructions/, CLAUDE.md, or scripts.** The note's examples focus on note-to-note and source-to-note backlinks. An instruction file referencing a note creates a dependency that use case 3 (impact assessment) should catch, but the note scopes its analysis implicitly to kb/notes/ and kb/sources/. Editing a note depended on by an instruction is a different failure mode than editing a note depended on by another note.

**BC4: The simplest case -- a note with exactly one inbound link.** Does the backlink machinery justify itself? Hub identification (use case 1) focuses on the high-inbound-count case. The Open Questions section asks about a noise threshold, which shows awareness of this boundary, but the use cases themselves do not address whether single-inbound-link notes benefit.

**BC5: Inbound links carrying different relationship types (extends vs. exemplifies vs. grounds).** The note mentions relationship semantics in use case 3 ("3 notes use this as foundation -- changing the core claim affects them. 2 notes merely exemplify it -- those are safe"), but the design options mostly discuss whether relationship types can be inferred mechanically. The boundary case is: does the value proposition of use cases 1 and 3 hold without relationship types, or does it degrade to a bare count that is little better than grep output?

## Step 3: Grounding alignment

**G1: link-contracts-framework.md** -- The Relevant Notes section claims "the 'click decision' framework applies to deciding whether to follow an inbound link too." The link-contracts note defines the click decision as five questions a reader asks when encountering a link (lines 21-28). This framework is explicitly about outbound links a reader encounters while reading. It never discusses inbound links or backlinks. The extension to inbound links is the backlinks note's own inference. The inference is plausible -- the same five questions would apply when an agent sees "this note is referenced by X" -- but it is not stated in the source.

**G2: koylanai-personal-brain-os.ingest.md** -- The note claims this ingest report "links to storing-llm-outputs-is-constraining." Verified: the ingest report's "Already established" section (line 32) includes `[storing-llm-outputs-is-constraining](../notes/storing-llm-outputs-is-constraining.md)` with relationship type "exemplifies." Attribution is accurate, including the direction of the link (ingest report links TO KB note).

**G3: maintenance-operations-catalogue-should-stage-distillation-into-instructions.md** -- The note claims orphan detection is "a batch maintenance task already handled by grep-based checks" and links to this catalogue. Verified: the catalogue contains an "Orphan note detection" section (lines 24-35) with a bash script that greps for notes with no inbound links. Attribution is accurate.

**G4: generate-instructions-at-build-time.md** -- Option B references `sync_topic_links.py` as a precedent for generated footer sections. The script exists at `scripts/sync_topic_links.py`. The linked note discusses build-time generation as a general pattern. Attribution is consistent.

**G5: The /ingest pipeline boundary claim** -- The Trade-offs section states "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes." The koylanai ingest report confirms this pattern: connections are listed in the ingest report, and the KB note `storing-llm-outputs-is-constraining.md` does not contain a backlink to the ingest report. Claim is consistent with observed system behaviour.

## Step 4: Internal consistency

**IC1: Non-use-case (orphan detection) vs. use case 1 (hub identification).** The note categorically places orphan detection in the non-use-case list because it "doesn't need read-time visibility." Hub identification is listed as a use case because seeing inbound link counts at read time "would change how carefully the agent reads and whether it risks editing." The distinction rests on whether read-time visibility matters for the task. For orphan detection (a batch maintenance sweep), the note argues it does not. For hub identification (an in-the-moment reading decision), it does. This is internally consistent -- the boundary is read-time vs. batch, not the underlying data. However, there is a tension: the note also says backlinks "measure the same thing" as orphan detection, which implicitly concedes that the same data serves both purposes and the only difference is the presentation layer. This weakens the categorical separation.

**IC2: The "~16% of notes still lack even outbound Relevant Notes sections" statistic (option C).** This is used to argue that manual backlinks would be unreliable because agents already fail at the simpler task of outbound links. The argument is internally consistent -- it uses an a fortiori move (if outbound fails, bidirectional will fail harder).

**IC3: The note's consistent use of "visible at reading time" vs. "searchable on demand."** The gap section, use cases, design options, and trade-offs all maintain this distinction without drift. The design options are organised around this axis (A = not visible, B = visible, C = visible but manual, D = hybrid). No definition drift detected.

**IC4: Open Questions section vs. use case prioritisation.** The note frames hub identification and source bridging as "highest value" in the Open Questions, and earlier in the use cases the ordering (1-4) mirrors this priority. Tension surfacing is last and labelled "lower frequency." This is consistent across sections.

---

WARN:
- [Completeness] The use-case enumeration does not cover staleness/supersession detection. The note frames tension surfacing (use case 4) around "contradicts" links, but a note superseded by a newer note that "extends" rather than "contradicts" it would not be caught. An agent reading an outdated note would benefit from backlinks showing "note Y extends and supersedes the claim here," and this is distinct from the four listed use cases.
- [Internal consistency] The note places orphan detection in the non-use-case list while promoting hub identification as use case 1, but concedes they "measure the same thing" (inbound link count). The stated difference -- that orphan detection does not need read-time visibility -- is defensible, but the note's own phrasing ("Backlinks measure the same thing as hub identification") undermines the categorical separation by admitting the data is identical. This leaves the distinction resting entirely on a presentation-layer argument that the note does not develop.

INFO:
- [Completeness] The use cases do not consider inbound links from outside kb/notes/ and kb/sources/ -- for example, from kb/instructions/ or CLAUDE.md. Use case 3 (impact assessment: "what breaks if I change this?") would miss dependencies from instructions or configuration files, which are arguably higher-stakes than note-to-note dependencies.
- [Completeness] The design options (A-D) do not consider an on-demand tool/skill approach: an agent command that, given a note path, returns its inbound links interactively without producing a stored report or modifying note footers. This sits between option A (batch report) and option B (stored footer) and could satisfy use cases 1 and 3 without the maintenance burden of B or the invisibility of A.
- [Completeness] The value proposition of use cases 1 and 3 depends partly on whether backlinks carry relationship types (extends, exemplifies, contradicts). The note acknowledges this in use case 3 and in option B's cons, but does not address whether bare counts (without relationship types) are sufficient for hub identification, or whether the use case degrades significantly without semantic annotation.
- [Grounding] The Relevant Notes claim that "the 'click decision' framework applies to deciding whether to follow an inbound link too" is a reasonable inference but is the backlinks note's own extension. The link-contracts note discusses only outbound links encountered during reading and does not mention inbound links or backlinks.

PASS:
- [Grounding] The claim that koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining was verified against the ingest report. Attribution is accurate, including the direction of the link (ingest report links TO KB note).
- [Grounding] The claim that orphan detection is handled by grep-based maintenance checks was verified against the maintenance operations catalogue, which contains an orphan detection procedure with a bash script.
- [Grounding] The reference to `sync_topic_links.py` as precedent for option B (generated footer sections) was verified: the script exists at scripts/sync_topic_links.py.
- [Grounding] The claim that the /ingest pipeline keeps connections in the ingest report rather than modifying KB notes was verified by checking both the ingest report and the referenced KB note -- no cross-link from the KB note back to the ingest report exists.
- [Internal consistency] The distinction between "visible at reading time" and "searchable on demand" is maintained consistently across the gap section, use cases, design options, and trade-offs. No definition drift detected.
- [Internal consistency] The design options (A-D) form a coherent spectrum from fully automated/invisible to fully manual/semantic, and the trade-offs section maps cleanly onto this spectrum.

Overall: 2 warnings, 4 info
===
