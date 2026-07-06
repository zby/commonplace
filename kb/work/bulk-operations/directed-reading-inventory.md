# Directed-reading contract inventory

This scan treats directed reading as: read selected material through an explicit lens and produce a lens-shaped result. The system has more instances than the original ingest/connect workshop framed.

## Stable contracts

- `kb/instructions/cp-skill-ingest/SKILL.md` reads a source through the KB-assimilation lens and writes an `.ingest.md` report. Its direct write should be the ingest report; delegated snapshot and connect steps may write their own artifacts.
- `kb/instructions/ingest-directory.md` is directory ingest: read selected files as a source tree, analyse relevance under the ingest lens, and write a directory `.ingest.md`.
- `kb/instructions/cp-skill-connect/SKILL.md` reads one artifact through the graph-integration lens and writes a connect report without changing library artifacts.
- `kb/agent-memory-systems/types/agent-memory-system-review.md` is type-driven directed reading: read a repository and existing KB frame through a code-grounded related-system review lens, then write the review note required by the type.
- `kb/sources/types/source-review.md` is an older source-extraction type: read an external source, summarize key points, assess project relevance, and record open questions. Its `llm-do` wording is project-specific and should be generalized or retired separately.

## Generated review prompts

The note-review system is directed reading even though it does not use handwritten instruction notes. `src/commonplace/review/protocol/prompt.py` renders run-specific prompts that include:

- the target note or target note batch
- the gate definitions as the evaluative lens
- pre-resolved markdown links and unresolved-link warnings
- reading boundaries that restrict follow-up reads to links in the target note
- exact sentinel and decision-line output contracts

`commonplace-create-review-run --with-prompt`, `commonplace-run-review-bundle`, and gate sweeps all use this shape. The review system is a stronger instance of frontloading than the ad hoc instruction-note experiments because the caller precomputes link resolution and output parsing constraints before the reviewer starts reading.

`kb/instructions/review-triage.md` is the adjacent triage case: read stale review pairs and diffs through a gate-relevance lens, then either acknowledge insignificant changes or leave them for full review.

## General instruction methods

- `kb/instructions/evaluate-log-entry-for-note-creation.md` reads a log proposal through novelty, mechanism, compression, traversal, and prediction tests, then chooses the smallest sufficient outcome.
- `kb/instructions/evaluate-scenarios/SKILL.md` reads scenario files and referenced instruction sources through a context-cost lens, then writes a cost report.
- Workshop instruction notes such as `instructions-amem-automation-quality.md` are the ad hoc form: the caller selects documents, states the lens, and names the report destination.

## Directed-editing hybrids

Some workflows read through a lens and then edit the target rather than only writing a report:

- `kb/instructions/revise-note.md` and iterative revise skills read a note and nearby context through flow, cohesion, and fidelity lenses, then update the note.
- `kb/instructions/refresh-agent-memory-review-taxonomy.md` reads existing reviews through a taxonomy-consistency lens and updates only ambiguous taxonomy prose.
- `kb/instructions/fix-warnings/fix-review-warnings.md` consumes accepted warning reviews and target notes through a fix-application lens, then applies the minimal correction.
- `kb/instructions/re-ingest.md` reruns source analysis and reads inbound links to verify whether references or downstream artifacts need updates.

These belong near directed reading conceptually, but they are not pure report-producing contracts. Their output authority is higher because they mutate library or instruction artifacts.

## Boundaries

Not every skill that reads files is directed reading. `cp-skill-snapshot-web` captures sources, `cp-skill-validate` runs deterministic checks, `cp-skill-convert` transforms file shape, and `cp-skill-write` primarily authors a new artifact under collection and type contracts. They may frontload context, but the central operation is not reading a target through a semantic lens to produce a lens-shaped judgment.
