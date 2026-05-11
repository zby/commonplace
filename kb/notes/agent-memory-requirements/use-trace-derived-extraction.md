---
description: "Trace-derived extraction is an after-the-fact learning path that must respect signal quality, review, and readable-artifact versus distributed-parametric learning boundaries"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Use Trace-Derived Extraction As Meta-Learning

Trace-derived extraction is the parallel path for memory that was not captured while understanding was live, or that only becomes visible across later traces. Session logs contain latent memory-creation opportunities, but those opportunities differ by oracle strength.

Corrections are strongest because the log contains both a negative and positive signal. Silent failures are weaker: the task appears completed, but the trace shows errors, retries, fallback paths, warning output, or weakened guarantees. Preferences are distributed over many accept/reject events. Procedures show up as recurring action sequences. Discoveries and broad syntheses have the weakest immediate oracle; their value often appears only through later reuse.

Without an explicit signal-quality distinction, automated or semi-automated extraction can give weak-signal discoveries, preferences, or syntheses the same apparent authority as corrected errors. That creates trust and lifecycle failures: low-confidence memories look durable, reviewers cannot tell which candidates need stronger evidence, and activation mechanisms may spend context on lessons that were never well grounded.

## Readable-Artifact And Distributed-Parametric Learning

This requirement mainly describes readable memory artifacts because they can be inspected, diffed, promoted, and rolled back. Systems such as [AgeMem](../../agent-memory-systems/source-only/agemem.md) show a different path: traces train a distributed-parametric policy for Add/Update/Delete/Retrieve/Summary/Filter actions. That path belongs where the oracle is strong enough to justify learned memory-management policy; it should not be smuggled in as ordinary artifact promotion.

## Memory Evolution

Extraction needs an evolution operation, not only creation. New memory may update, split, merge, re-tag, or contextualize nearby old memory. The comparative review flags [A-MEM's evolution step](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) because new notes update neighboring notes' context and tags, while [Hindsight](../../agent-memory-systems/reviews/hindsight.md) and [Cludebot](../../agent-memory-systems/reviews/cludebot.md) show CRUD and dream-cycle variants. The requirement is not that every system automate this immediately; it is that the architecture leave room for old memory to be revised by new evidence instead of only appending candidates.

## Methods

- Narrow, schema-constrained extraction prompts for one signal type at a time.
- Classifiers or simple rules for explicit events: user correction, command failure, retry, fallback, approval, rejection, or repeated tool sequence.
- Batch analysis over many sessions for preferences, procedures, and recurring failure patterns.
- Manual observation inboxes that let agents record noticed improvement opportunities without interrupting the current task.
- Human or agent review queues for weak-oracle candidates such as discoveries, broad design principles, or high-impact policy changes.
- Confidence, source pointers, and candidate status fields so extracted items do not masquerade as durable knowledge.
- Evolution proposals that update tags, context summaries, links, nearby notes, or existing observations when new evidence changes how older memory should be read.

## Evaluation Questions

- Does extraction distinguish strong corrections from weak discoveries?
- Are weak-oracle candidates prevented from gaining durable authority by default?
- Can new evidence update nearby old memory rather than only appending new records?
- Is distributed-parametric or policy learning limited to domains with sufficiently strong feedback?

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) - surveys trace-mining systems across artifacts, policies, and procedures
- [Codification and relaxing navigate the bitter lesson boundary](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) - frames when learned policy can replace artifact-side control
