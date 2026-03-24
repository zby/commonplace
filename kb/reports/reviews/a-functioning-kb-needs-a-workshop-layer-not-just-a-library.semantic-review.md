<!-- REVIEW-METADATA
note-path: kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
last-full-review-note-sha: 546b8b87cfa3e95bcdee1c16a58844911da0bc0e
last-full-review-note-commit: 27532d61411f48d7ac184faa56e165b067ffac9b
last-full-review-at: 2026-03-24T12:00:00+01:00
last-accepted-note-sha: 546b8b87cfa3e95bcdee1c16a58844911da0bc0e
last-accepted-note-commit: 27532d61411f48d7ac184faa56e165b067ffac9b
last-accepted-at: 2026-03-24T12:00:00+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md ===

Claims identified: 16

1. The KB's current type system (text, note, structured-claim, spec, adr, review, index) is oriented toward permanence; documents move up a maturity ladder. [Para 1]
2. The wikiwiki principle animates this ladder: capture with zero friction, then refine in place. [Para 1]
3. The status field modulates commitment but not lifecycle -- a seedling and a current note are structurally identical. [Para 1]
4. Some existing types already strain the permanence framing: `review` is dated and its findings can go stale. [Para 1]
5. A functioning KB needs to support "work in motion" -- documents with lifecycles, state changes, interactions, and outcomes. [Para 2]
6. The task system is the clearest example, having state machines (backlog -> active -> completed), directional dependencies, and expiration. [Para 2]
7. Library documents accumulate value over time; workshop documents consume value over time. [Library/workshop distinction]
8. Six properties distinguish library from workshop: value trajectory, state, relationships, time sensitivity, success state, end state. [Table]
9. The distinction is useful but not exhaustive; some documents straddle both layers. [Paragraph after table]
10. Six temporal document types beyond tasks: decision threads, experiments/probes, queues/inboxes, reviews (periodic), collaborative threads, session logs. [Temporal document types]
11. The relationship between library and workshop is bidirectional. [Bridges]
12. Two kinds of bridges: extraction (workshop -> library) and composition (library -> workshop). [Bridges]
13. Spec mining is at the "deterministic end" of extraction bridges; extraction is broader and also produces non-deterministic artifacts like notes, ADR drafts, and judgment precedents. [Extraction bridges]
14. The task system is the "only workshop-like subsystem" and lives "entirely outside the KB." [Current state]
15. Workshop and library should likely remain parallel hierarchies rather than share a type system. [Open questions]
16. The Tulving mapping to workshop/operational space "may be decorative rather than load-bearing." [Open questions]

WARN:
- [Completeness] The six-property table draws a clean binary between library and workshop, and the paragraph that follows correctly acknowledges "the distinction is useful but not exhaustive" with the living checklist/runbook example. However, the table itself still forces exclusive categories (value "Accumulates" vs. "Consumed"; end state "Remains in KB" vs. "Archived or deleted"). A document like a recurring retrospective template -- which is consumed during each use but also accumulates refinements across uses -- does not fit either column. The caveat paragraph helps, but the table's clean dichotomy could mislead readers who scan the table and skip the prose. A third column ("Hybrid") or a note row in the table itself would make the non-exhaustiveness visible at the structural level, not just in surrounding prose.

- [Completeness] The enumeration of six temporal types (decision threads, experiments/probes, queues/inboxes, reviews, collaborative threads, session logs) is hedged with "would likely need," which is appropriate. A boundary case that sits between categories: **a research spike** -- a time-boxed investigation that produces understanding but not necessarily a decision, artifact, or testable hypothesis. It resembles an experiment (time-boxed, has conclusion) but lacks a hypothesis; it resembles a decision thread but produces understanding rather than a choice. It could be forced into "experiments/probes" but the fit is strained because the note defines those as "hypothesis-driven." Research spikes are exploration-driven. This is worth flagging because the KB itself frequently does this kind of work (exploring a source to see if it's relevant, investigating a concept without a clear question).

- [Grounding alignment] The note claims that extraction bridges include spec mining "at the deterministic end" and links to spec-mining-as-codification.md. The spec mining note is exclusively about extracting deterministic verifiers from observed behavior -- it never discusses non-deterministic extraction. The workshop note then extends to say extraction "is broader -- it also produces non-deterministic library artifacts like notes, ADR drafts, and judgment precedents." This extension is the note's own move, not grounded by the linked source. The link placement (mid-sentence, right before the broadening) could lead readers to think the spec mining note endorses the full scope of extraction bridges, when it only grounds the deterministic subset. The note should either place the link before the broadening or add a brief signal like "beyond what spec mining covers."

INFO:
- [Completeness] The simplest possible workshop document is a single to-do item ("fix typo in X"). This maps to the task type, but it strains several of the six properties: a trivial task has no meaningful "state machine" (it is either not-done or done), no "directional dependencies," and arguably no "value consumption" trajectory. The framework targets the interesting complex case. This is fine -- frameworks often do -- but the note does not acknowledge that many real workshop items are degenerate instances of the model.

- [Grounding alignment] The note references the three-space agent memory model and says "workshop documents map roughly to the 'operational space.'" The three-space note maps operational space to "Friction observations, methodology, session artifacts" with "High churn." This aligns with workshop documents' lifecycle properties. But the three-space note's operational space also includes "methodology," which in this KB is a library-like category (methodology notes accumulate and refine). The mapping is loose rather than precise, which the note's own hedging ("map roughly") acknowledges.

- [Grounding alignment] The note references constraining.md in the Relevant Notes section, claiming "extraction bridges are constraining: collapsing workshop process outcomes into permanent library artifacts." The constraining note defines constraining as "narrowing the interpretation space" of underspecified specs. Collapsing workshop outcomes into library artifacts is not obviously about narrowing interpretation space -- it is about transferring knowledge across layers. The connection works if you read "extraction" as a form of commitment (choosing what to keep from a process), but this is an inference, not a direct application of the constraining definition. The fit is plausible but somewhat stretched.

- [Grounding alignment] The note claims the wikiwiki principle "animates this ladder" and links to the wikiwiki principle note. That note confirms: it describes "text -> note -> structured-claim" as an in-place refinement ladder. It also adds a caveat that "the ladder is a library pattern" and workshop documents "follow the opposite trajectory." Both notes agree on the scope. The phrasing "animates this ladder" could be read as if the wikiwiki principle covers the entire KB, but the workshop note immediately qualifies this by discussing what the ladder does not cover.

- [Internal consistency] The note concedes in "Current state of the gap" that the task system "works adequately with its own conventions" and that expanding the workshop layer is "where most of the new design work will be needed" -- framing this as a future concern. Yet the title claims "a functioning knowledge base needs a workshop layer" (present tense, unconditional). The body's evidence is drawn from the task system (which works outside the KB) and projected future types (decision threads, experiments, etc.) that do not yet exist. The argument is forward-looking rather than grounded in demonstrated current pain. This is not a contradiction -- the note explicitly marks the gap as fine "for now" -- but the title's strength exceeds the body's evidence.

PASS:
- [Internal consistency] The library/workshop distinction is used consistently throughout the note. Library is always associated with accumulation, permanence, and bidirectional links; workshop is always associated with consumption, expiration, and directional dependencies. No definition drift detected.
- [Internal consistency] The description field faithfully represents the body. It mentions both layers, correctly identifies the gap, names key workshop properties, and includes the bridges concept.
- [Internal consistency] The open questions section is genuinely open -- it does not smuggle in conclusions that contradict the body. The suggestion that the Tulving mapping "may be decorative" is consistent with the body's cautious phrasing ("map roughly"). The tentative recommendation toward parallel hierarchies is consistent with the cited why-directories note.
- [Grounding alignment] The note's reference to claw-learning-loops-must-improve-action-capacity-not-just-retrieval is accurate. That note argues the KB needs "action-oriented knowledge types (preferences, procedures, precedents, voice)," and this note's claim that "workshop documents are precisely the kind of action-oriented artifacts that produce those knowledge types" is a reasonable inference.
- [Grounding alignment] The note now acknowledges `review` as an existing type that strains the permanence framing. The document-classification.md source confirms review has a "dated" property, consistent with the note's characterization.
- [Grounding alignment] The note's reference to instructions-are-typed-callables is used in the open questions to ask whether "extraction bridges could be formalised as skills with workshop-input, library-output signatures." The typed-callables note does describe skills with type signatures. The extension to workshop-input/library-output signatures is the workshop note's own speculative move, which is appropriate for an open question.
- [Completeness] The library/workshop binary now includes an explicit non-exhaustiveness caveat with concrete examples (living checklist, runbook, task templates). This addresses the primary completeness gap from the prior review.
- [Completeness] Collaborative threads are now included in the temporal types enumeration, with a clear lifecycle and explicit distinction from session logs.

Overall: 3 warnings, 5 info
===
