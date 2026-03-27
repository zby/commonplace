---
note: kb/notes/backlinks.md
gate: semantic/internal-consistency
---

Key claims extracted from each section:

- **Gap**: grep-based discovery exists but agents "have to think to run it" — implying grep is insufficient for read-time link visibility.
- **Non-use-cases/orphan detection**: orphan detection is "a batch maintenance task already handled by grep-based checks" — implying grep is sufficient for that task.
- **Design option A**: "not visible when reading a note; agents must know to run the script" — restates the gap criticism of on-demand tools.
- **Design option C**: "~16% of notes still lack even outbound Relevant Notes sections" — used to argue manual backlinks are unreliable.
- **Trade-offs**: notes with many inbound links "would get long sections that don't read naturally" — applied to options with in-note content (B and D).
- **Question framing (gap section)**: "The question is whether inbound connections should be visible at reading time."

## Grep sufficiency tension

The gap section treats "agents have to think to run grep" as a problem. The non-use-cases section accepts grep as the adequate solution for orphan detection. These claims are not directly contradictory — orphan detection is a prompted batch maintenance task, while read-time link visibility is an unprompted reading-time need. But the note never makes this distinction explicit.

INFO: the note uses the same tool (grep / scripts) as a criticism in the gap section and as a justification in the non-use-cases section without articulating why the distinction holds. A reader encountering option A ("agents must know to run the script") and orphan detection ("handled by grep-based checks") in the same note gets no explanation for why the same limitation is acceptable in one case and not the other. The implicit answer (batch vs. reading-time need) should be stated.

## Question framing vs. design option A

The gap section closes with: "The question is whether inbound connections should be visible at reading time, and if so, how." This frames read-time visibility as the goal being evaluated. But option A (generated report, not in notes) remains a live option throughout the design section and is not rejected in the trade-offs. The question framing implies the answer will be yes-or-no on read-time visibility; the design section actually explores four options, one of which answers "no" to the framing question.

INFO: the question framing in the gap section ("should inbound connections be visible at reading time?") doesn't match the design space actually explored, which includes option A as a legitimate answer of "no." This isn't a contradiction but it creates a mismatch between how the problem is posed and how the analysis proceeds.

## Trade-off coverage for option D vs. option B

The trade-offs section says: "A backlinks footer with 12 entries is metadata, not prose — notes with many inbound links would get long sections that don't read naturally." This framing applies to generated content in notes (option B, and option D's generated layer). Option D's description says agents "optionally annotate the relationship type" to add depth over time. But the trade-offs section's noise concern applies equally to D's unannotated state. The note acknowledges "unannotated backlinks are noisy" as a D con, but the trade-offs section's prose-readability concern is raised without distinguishing between B and D.

INFO: the trade-offs section doesn't clearly distinguish why option D's noise is different from option B's noise. D's theoretical advantage (incremental annotation) is stated in D's description but not carried into the trade-offs comparison. A reader looking only at the trade-offs section would not see why D is preferable to B on the prose-readability dimension.

## Source boundary tension with use case 2

Use case 2 (source-to-theory bridge) presents source-backlinks as a positive: "backlinks would let an agent see how well-grounded a theoretical claim is." The trade-offs section then flags this as a concern: "backlinks would create implicit two-way relationships between sources and notes — useful (use case 2) but it changes the boundary between the two layers."

The note doesn't resolve this. Use case 2 is listed without qualification; the trade-offs section identifies it as a tension without recommending or rejecting source inclusion in the backlink scope. The two sections are not contradictory (the note is speculative), but the tension is set up and left fully open.

No WARN — this is an appropriate unresolved tension for a speculative note. INFO: use case 2 motivates including sources in backlink scope; the trade-offs section flags this as a layer-boundary concern; the open questions section doesn't ask which use cases justify which trade-offs, which would have been the natural place to connect them.

## No definition drift or summary/body mismatch

The term "backlinks" is used consistently throughout to mean inbound links from other notes. There is no compressed summary section, so summary/body mismatch doesn't apply.

## Overall

No WARNs. Three INFOs: (1) the grep-sufficiency distinction (batch vs. reading-time) is implicit rather than stated; (2) the question framing ("visible at reading time?") doesn't match a design space that includes option A as a valid "no" answer; (3) option D's advantage over B on prose readability isn't carried through to the trade-offs section.
