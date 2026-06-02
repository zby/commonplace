---
description: Auto-generated directory - run commonplace-refresh-indexes to rebuild
type: kb/types/index.md
index_source: directory
---

# Instructions Directory

← [Parent](../index.md)

## Subdirectories

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
- [write-agent-memory-system-review/](./write-agent-memory-system-review/SKILL.md)

## Files

- [Complexity Review](./complexity-review.md) *(instruction)* - Complexity review wrapper — keep the old entrypoint, but route execution through the gate bundle
- [Evaluate a log entry for note creation](./evaluate-log-entry-for-note-creation.md) *(instruction)* - Evaluate a kb/log.md entry that suggests a new note — read the notes index first, load related notes, and decide whether to reject, fold into existing artifacts, keep in the log, or create a genuinely new note
- [Example: Onboard a Second Brain on Commonplace](./example-onboard-second-brain.md) *(instruction)* - One worked recipe for onboarding an operator who wants to build a personal Second Brain on top of Commonplace. Use as a starting template, not the canonical path.
- [Fix system](./FIX-SYSTEM.md)
- [Ingest a directory](./ingest-directory.md) *(instruction)* - Ingest a directory of related files (e.g. a cloned code repository) as a single source unit, producing one coherent `.ingest.md` that cites evidence across files.
- [Maintain curated indexes](./maintain-curated-indexes.md) *(instruction)* - Audit and maintain curated sections of generated-tail index pages — evaluate editorial groupings, check for orphaned notes, and split or merge indexes where needed.
- [Migrate semantics-preserving gate changes](./migrate-semantics-preserving-gate-changes.md) *(instruction)* - Change gate wording without invalidating accepted reviews — update stored accepted reviews, then append gate-migration acceptance events that preserve the accepted note baseline
- [Prose Review](./prose-review.md) *(instruction)* - Prose review wrapper — keep the old entrypoint, but route execution through the gate bundle
- [Re-Ingest](./re-ingest.md) *(instruction)* - Re-ingest a source whose .ingest.md report is stale — regenerate the analysis against current KB state, then update all notes that reference the old report.
- [Refresh agent-memory review taxonomy](./refresh-agent-memory-review-taxonomy.md) *(instruction)* - Use when refreshing existing agent-memory-system reviews for the current artifact taxonomy without doing a full source re-review
- [Review sweep](./review-sweep.md) *(instruction)* - Batch review sweep — run the selector, triage note-changed pairs, and execute direct-write review runs for the rest
- [Review system](./REVIEW-SYSTEM.md)
- [Review triage](./review-triage.md) *(instruction)* - Inspect diffs for note-changed review pairs and ack insignificant changes — run before a review sweep to reduce the review queue
- [Revise Note](./revise-note.md) *(instruction)* - Editorial revision of a single KB note — rewrites for logic, flow, and cohesion. Reads linked notes for context. Edits the file in place and reports changes.
- [Run a review bundle on one note](./run-review-bundle-on-note.md) *(instruction)* - Run review gates on one note from inside a live agent harness
- [Verify review quote grounding](./verify-review-quote-grounding.md) *(instruction)* - Verify that quote-anchored citations in a code-grounded review resolve to verbatim text in the reviewed source, run against the live checkout before it is discarded.
- [Write an Instruction](./write-instruction.md) *(instruction)* - Create a new instruction in kb/instructions/ by distilling repeated manual operations into a reusable, execution-optimized procedure.
- [Writing conventions for kb/instructions/ (prescriptive register)](./COLLECTION.md)
