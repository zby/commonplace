---
description: Read-back-when-relevant is a memory primitive with its own placement axes, independent of how memory was written; architectures and reviews that elaborate the write/learn loop while treating read-back as one retrieval bullet are under-specifying half the system
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, context-engineering]
status: seedling
---

# The read-back path needs the same placement treatment as the write path

Memory-system design tends to lavish structure on one half of the loop and starve the other. The write/learn side gets named stages — trace source, extraction trigger, oracle, storage substrate, representational form, lineage, scope, timing. The read side gets a single question: *can the system retrieve the memory?* This is an asymmetry of attention, not of importance. The path from stored memory back into an action is a design surface with its own degrees of freedom, and those degrees of freedom are not determined by how the memory was written.

## Read-back-when-relevant is not retrieval

The first thing the asymmetry hides is that "read" is two operations, not one. Retrieval is *pull*: the agent (or user) poses a query and the system returns matching material. Read-back-when-relevant is *push*: the system surfaces a past lesson against an action the agent did not think to ask about. Since [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), a system can ace retrieval — produce the fact on demand — and still never fire it before the action it would have changed. [Behavior-changing memory must activate before the mistake](./agent-memory-requirements/activate-behavior-changing-memory.md), which a pull interface cannot guarantee, because the cue to pull is exactly what a novice user or an activation-limited agent is missing.

So read-back-when-relevant is a distinct primitive. Collapsing it into retrieval is what produces the thin treatment: if read is "just a query," one bullet suffices. Once read-back is seen as push-before-action, it needs to specify *when* it fires, *what* trips it, and *with what force* it lands — none of which a query answers.

## The read-back placement axes

The write/learn loop is specified by asking where the signal comes from and how it becomes durable. The read-back path is specified by a parallel but different set of questions:

- **Trigger and relevance signal** — what trips the read-back. Explicit reference, skill or tool invocation, situation/action match against typed cues, or always-on loading. Matching can be rules, embeddings, action classifiers, or LLM relevance judgments. This is the cue-design problem, and it is independent of the storage substrate the memory sits in.
- **Direction: push or pull** — does the system answer only when asked (pull) or surface unprompted against the current action (push)? A system can support one and not the other. The push side is the part retrieval benchmarks do not test.
- **Timing relative to action** — before the risky step or after it. Before-action read-back changes the next move; after-action read-back can only explain or audit. The defining requirement is that behavior-changing memory loads *before* the action it governs.
- **Selection and scope** — how much loads and how it competes for context. Read-back inherits the soft-degradation constraint: an over-broad push dilutes cues and can suppress the very activation it intends. Scope (this action, this task, this project) is a read-back decision, not a write decision.
- **Behavioral authority at consumption** — the force the surfaced memory carries when it lands: advice, instruction, enforcement, routing, or audit trigger. The same stored note can be read back as a soft reminder or as a hard gate; [behavioral authority](./definitions/behavioral-authority.md) is set on the consumption path, not fixed at write time.
- **Faithfulness test** — whether a fired read-back actually changes the action, checked by WITH/WITHOUT comparison or post-action trace audit rather than assumed from the fact that it entered context.

These axes describe the read-back path of any retained artifact, whoever wrote it and however it is stored.

## The two paths are independent

The key claim is that you cannot read the read-back design off the write design. A memory can be written by an elaborate trace-distillation loop and then exposed only through pull retrieval, leaving its highest-authority lessons inert until someone asks. Conversely, a memory written by a one-line manual note can be given a sharp situation-trigger, push direction, before-action timing, and enforcement authority — a fully specified read-back path over a trivially specified write path. Write-side richness does not transfer to the read side, because the write axes (where the signal came from, how it was distilled, where it persists) and the read axes (what trips it, which direction, when, with what force) range over different choices. Specifying one leaves the other open.

This is why the attention asymmetry is a real defect and not just uneven prose. A system or a review that fully characterizes the learning loop and answers "yes, it can retrieve" has described how memory is *made* and left undescribed how memory *acts*. Half the behavior-shaping mechanism is unspecified.

## Application: give read-back a parallel placement section

The clearest place this bites is memory-system analysis. The [agent-memory-system review type](../agent-memory-systems/types/agent-memory-system-review.md) gives trace-derived learning a nine-point placement section — trace source, extraction, storage substrate, representational form, lineage, behavioral authority, scope, timing, survey placement — and gives read-back a single comparison bullet asking whether activation can beat question-answer retrieval. The fix is symmetry: a read-back placement section with the axes above, applied whenever a reviewed system has a non-trivial activation path, so reviews capture *how memory acts* as systematically as they capture *how memory is learned*. The same discipline applies to designing a memory system, not only to reviewing one: the read-back path deserves an explicit specification, not a retrieval checkbox.

## Scope

The claim is about specification discipline, not about always building elaborate read-back. For stable, high-frequency, low-cost constraints, always-loaded instructions are the right and trivial read-back path; the point is that "always-loaded" is itself a placement choice that should be named, not the absence of one. The axes are a checklist for *where the design decisions are*, and a system is free to take the cheap option on any axis — as long as the choice is made rather than defaulted by treating read as retrieval.

## Open Questions

- Which read-back axis most often goes unspecified in practice — trigger, direction, or authority-at-consumption?
- Can a read-back placement section be filled from code inspection as reliably as the trace-derived learning section, or is activation harder to observe statically than learning?
- Do the read-back axes collapse for purely knowledge-artifact memory (evidence consumed as advice), or do trigger and timing still matter when the force is only advisory?

---

Relevant Notes:

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — extends: develops the storage/context/behavior distinction into a named set of read-back design axes
- [activate behavior-changing memory before the mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — grounds: supplies the before-action requirement and the loading-method family this note generalizes into placement axes
- [memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) — grounds: names activation as a first-class operational axis alongside capture and lifecycle
- [charting the knowledge-access problem beyond RAG](./charting-the-knowledge-access-problem-beyond-rag.md) — contrasts: charts the pull-side access and transformation problem; this note carves out the push-side activation problem it lists as one dimension
- [behavioral authority](./definitions/behavioral-authority.md) — defined-in: the force-at-consumption axis read-back sets independently of write time
- [agent-memory-system review type](../agent-memory-systems/types/agent-memory-system-review.md) — evidence: a review contract that elaborates the write/learn placement into nine points while compressing read-back into a single lens bullet
