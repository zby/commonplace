---
description: Auto-generated directory - run commonplace-refresh-indexes to rebuild
type: index
index_source: directory
---

# Instructions Directory

← [Parent](../index.md)

## Subdirectories

- [cp-skill-compile-collections/](./cp-skill-compile-collections/SKILL.md)
- [cp-skill-connect/](./cp-skill-connect/SKILL.md)
- [cp-skill-convert/](./cp-skill-convert/SKILL.md)
- [cp-skill-ingest/](./cp-skill-ingest/SKILL.md)
- [cp-skill-revise-autoreason/](./cp-skill-revise-autoreason/SKILL.md)
- [cp-skill-revise-iterative/](./cp-skill-revise-iterative/SKILL.md)
- [cp-skill-snapshot-web/](./cp-skill-snapshot-web/)
- [cp-skill-validate/](./cp-skill-validate/SKILL.md)
- [cp-skill-write/](./cp-skill-write/SKILL.md)
- [evaluate-scenarios/](./evaluate-scenarios/SKILL.md)
- [fix-warnings/](./fix-warnings/)
- [review-gates/](./review-gates/)

## Files

- [Complexity Review](./complexity-review.md) - Complexity review wrapper — keep the old entrypoint, but route execution through the gate bundle
- [Evaluate a log entry for note creation](./evaluate-log-entry-for-note-creation.md) - Evaluate a kb/log.md entry that suggests a new note — read the notes index first, load related notes, and decide whether to reject, fold into existing artifacts, keep in the log, or create a genuinely new note
- [Fix system](./FIX-SYSTEM.md)
- [Maintain curated indexes](./maintain-curated-indexes.md) - Audit and maintain curated sections of generated-tail index pages — evaluate editorial groupings, check for orphaned notes, and split or merge indexes where needed.
- [Migrate semantics-preserving gate changes](./migrate-semantics-preserving-gate-changes.md) - Change gate wording without invalidating accepted reviews — update stored accepted reviews, then append gate-migration acceptance events that preserve the accepted note baseline
- [Prose Review](./prose-review.md) - Prose review wrapper — keep the old entrypoint, but route execution through the gate bundle
- [Re-Ingest](./re-ingest.md) - Re-ingest a source whose .ingest.md report is stale — regenerate the analysis against current KB state, then update all notes that reference the old report.
- [Review sweep](./review-sweep.md) - Batch review sweep — run the selector, triage note-changed pairs, and execute direct-write review runs for the rest
- [Review system](./REVIEW-SYSTEM.md)
- [Review triage](./review-triage.md) - Inspect diffs for note-changed review pairs and ack insignificant changes — run before a review sweep to reduce the review queue
- [Revise Note](./revise-note.md) - Editorial revision of a single KB note — rewrites for logic, flow, and cohesion. Reads linked notes for context. Edits the file in place and reports changes.
- [Run a review bundle on one note](./run-review-bundle-on-note.md) - Run review gates on one note from inside a live agent harness
- [Write an Agent Memory System Review](./write-agent-memory-system-review.md) *(note)* - Write or update a code-grounded agent memory system review from a GitHub repository checkout.
- [Write an Instruction](./write-instruction.md) - Create a new instruction in kb/instructions/ by distilling repeated manual operations into a reusable, execution-optimized procedure.
- [Writing conventions for kb/instructions/ (prescriptive register)](./COLLECTION.md)
