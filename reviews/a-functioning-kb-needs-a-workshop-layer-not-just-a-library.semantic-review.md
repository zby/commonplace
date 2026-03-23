=== SEMANTIC REVIEW: a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md ===

Claims identified: 14

1. The KB's current type system (text, note, structured-claim, spec, adr) is a "maturity ladder" where documents move toward permanence. [Para 1]
2. The wikiwiki principle animates this ladder. [Para 1]
3. The status field modulates commitment but not lifecycle; a seedling and a current note are structurally identical. [Para 1]
4. A functioning knowledge base needs to support "work in motion" -- documents with lifecycles, state changes, interactions, and outcomes. [Para 2]
5. The task system is the clearest example, having state machines, directional dependencies, and expiration. [Para 2]
6. Library documents accumulate value over time; workshop documents consume value over time. [Library/workshop distinction]
7. Six properties distinguish library from workshop: value trajectory, state, relationships, time sensitivity, success state, end state. [Table]
8. Five temporal document types beyond tasks: decision threads, experiments/probes, queues/inboxes, reviews (periodic), session logs. [Temporal document types]
9. The relationship between library and workshop is bidirectional. [Bridges]
10. Two kinds of bridges are needed: extraction (workshop -> library) and composition (library -> workshop). [Bridges]
11. Spec mining is at the "deterministic end" of extraction bridges; extraction is broader and also produces non-deterministic artifacts. [Extraction bridges]
12. The task system is the "only workshop-like subsystem" and lives "entirely outside the KB." [Current state]
13. Workshop and library should likely remain parallel hierarchies rather than share a type system. [Open questions]
14. The Tulving mapping to workshop/operational space "may be decorative rather than load-bearing." [Open questions]

WARN:
- [Completeness] The library/workshop binary may not be exhaustive. A plausible boundary case is a **living checklist or runbook** -- a document that is used repeatedly during work (consumed like a workshop document) but also refined in place over time (accumulated like a library document). The note's table forces a choice: value trajectory is either "accumulates" or "consumed." A checklist that gets better each time it is used occupies both columns simultaneously. The note's own example of "task templates that pull in relevant library content" hints at this hybrid but classifies it as a composition bridge rather than acknowledging it as a document that is genuinely both library and workshop.

- [Completeness] The enumeration of five temporal document types (decision threads, experiments/probes, queues/inboxes, reviews, session logs) is presented with "would likely need" hedging, but a prominent boundary case is missing: **collaborative threads or conversations** -- multi-turn exchanges between human and agent (or agent and agent) that have state, produce decisions, and either get archived or extracted. These are distinct from session logs (which the note frames as "what happened in a work session") because a collaborative thread's purpose is to reach a decision or produce an artifact, not to record what happened. Given that this KB is operated by agents in conversation, this omission is notable.

- [Grounding alignment] The note claims the type system is "text, note, structured-claim, spec, adr" and calls it a "maturity ladder." The linked document-classification.md lists seven base types (text, note, spec, review, index, adr, structured-claim), not five. The note omits `review` and `index`. This matters because `review` -- a type that "examines specific existing code; has Findings; dated" -- has temporal, lifecycle-like properties (it is dated, its findings may become stale). Omitting it from the library types weakens the claim that the existing type system is purely a permanence ladder; `review` is a counter-example that sits closer to workshop territory even within the current library hierarchy.

INFO:
- [Completeness] The simplest possible instance of a workshop document is a single to-do item ("fix typo in X"). This maps cleanly to the task type, but it strains the six-property framework: a trivial task has no meaningful "state machine" (it goes from not-done to done), no "directional dependencies," and no meaningful "value consumption." The framework is designed for the complex case and may over-formalize simple workshop items. This is not necessarily a problem -- frameworks often target the interesting cases -- but the note doesn't acknowledge that many workshop items are degenerate instances of the model.

- [Grounding alignment] The note claims the wikiwiki principle "animates this ladder" and links to the wikiwiki principle note. The wikiwiki principle note confirms this: it describes "text -> note -> structured-claim" as an in-place refinement ladder. However, the wikiwiki note also explicitly adds a caveat (in its own Caveats section) that "the ladder is a library pattern" and that workshop documents "follow the opposite trajectory." This bidirectional acknowledgment is clean -- both notes agree. Flagging as INFO only because the workshop note's phrasing ("animates this ladder") could be read as if the wikiwiki principle covers the entire KB, when both notes agree it specifically does not cover workshop documents.

- [Grounding alignment] The note references spec mining as the "deterministic end" of extraction bridges. The spec-mining-as-codification.md note describes spec mining as "extracting deterministic verifiers from observed stochastic behavior." This is accurately attributed. However, the workshop note extends the concept: it says extraction bridges "also produce non-deterministic library artifacts like notes, ADR drafts, and judgment precedents." The spec mining note does not discuss non-deterministic extraction at all -- it is exclusively about deterministic codification. The extension is reasonable (the workshop note is explicitly going beyond spec mining), but readers could mistake the linked source as grounding the broader claim about non-deterministic extraction when it only grounds the deterministic subset.

- [Grounding alignment] The note references the three-space agent memory model and says "workshop documents map roughly to the 'operational space.'" The three-space note maps operational space to "Friction observations, methodology, session artifacts" with "High churn." This does align with workshop documents' lifecycle properties. But the three-space note's operational space also includes "methodology" -- a category that feels more library-like (methodology accumulates and refines). The mapping is loose rather than precise.

- [Internal consistency] The note says in "Current state of the gap" that the task system "lives entirely outside the KB" with "no document type in the classification hierarchy." But in the opening paragraph, it uses tasks as the primary example of workshop documents to argue for expanding the KB. If tasks already work "adequately with their own conventions" (as the note concedes), the argument for a workshop layer rests on the claim that *other* temporal types (decision threads, experiments, etc.) will also be needed. The note acknowledges this ("this is fine for now") but the tension between "tasks work fine outside" and "the KB needs a workshop layer" is somewhat unresolved -- the argument depends on projected future needs rather than demonstrated current pain.

PASS:
- [Internal consistency] The library/workshop distinction is used consistently throughout the note. Library is always associated with accumulation, permanence, and bidirectional links; workshop is always associated with consumption, expiration, and directional dependencies. No definition drift detected.
- [Internal consistency] The compressed summary (the description field: "the current type system models permanent knowledge (library) but not in-flight work with state machines, dependencies, and expiration (workshop)") faithfully represents the body. It mentions both layers, correctly identifies the gap, and names the key workshop properties (state machines, dependencies, expiration).
- [Grounding alignment] The note's reference to the claw-learning note is accurate. That note does argue the KB needs "action-oriented knowledge types (preferences, procedures, precedents, voice)," and the workshop note's claim that "workshop documents are precisely the kind of action-oriented artifacts that produce those knowledge types" is a reasonable inference that the claw-learning note itself endorses in its own Relevant Notes section.
- [Grounding alignment] The note's reference to why-directories-despite-their-costs is used only in the open questions section to support the idea that "local conventions per subsystem" is the right default. This is a modest, accurately scoped reference.
- [Internal consistency] The open questions section is genuinely open -- it does not smuggle in conclusions that contradict the body. The suggestion that the Tulving mapping "may be decorative" is consistent with the body's cautious phrasing ("map roughly to the 'operational space'").

Overall: 3 warnings, 5 info
===
