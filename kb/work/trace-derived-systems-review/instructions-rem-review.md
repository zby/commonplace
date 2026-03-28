# Instructions: Review REM for Trace-Derived Learning

## Goal

Evaluate the existing related-system review of REM against [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md) and determine whether REM belongs in the survey.

This is not a new review — [REM](../../notes/related-systems/REM.md) already has a related-system note. The task is to assess its trace-derived learning placement and, if warranted, add it to the survey note.

## Targets

- Repo: `https://github.com/satyammistari/REM`
- Local clone: `related-systems/REM`
- Existing review: `kb/notes/related-systems/REM.md`

## Why this candidate matters

REM's consolidation pipeline (episodes → keyword-clustered groups → LLM-extracted semantic facts) is a trace-to-artifact transformation. The question is whether the transformation is deep enough to count as trace-derived learning or whether it is closer to simple memory storage with LLM compression.

## Inputs

Read all of:

1. [REM review](../../notes/related-systems/REM.md)
2. The REM repository (already cloned at `related-systems/REM/`)
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [cass-memory](../../notes/related-systems/cass_memory_system.md) — closest analogue (both consolidate raw interactions into scored facts)
5. [Cognee](../../notes/related-systems/cognee.md) — another database-first extraction system

## Questions to answer

1. What is REM's actual source trace: raw episode content strings, LLM-parsed metadata, or both?
2. What are the trigger boundaries for learning: per episode, periodic consolidation, or manual?
3. What intermediate artifacts does REM create: semantic memory facts with confidence scores, typed by fact_type — is this structured enough to count as an extraction schema?
4. Does the consolidation pipeline stop at symbolic artifacts (semantic facts), or is there any weight promotion path?
5. On axis 1 of the current survey (ingestion pattern), is REM best read as a service-owned backend (like OpenViking/cass-memory) or something else?
6. On axis 2 (promotion target), is REM purely artifact-learning?
7. Does REM strengthen, weaken, or split any claim in the current survey note? Specifically: does the keyword-clustering + LLM-compression consolidation represent a distinct extraction pattern not already covered?

## Output spec

- Update the existing REM review note to include a `Trace-derived learning placement` section
- In that section, state REM's position on both survey axes and whether it should be added to the survey note
- If REM should be added, write its five-stage entry (Trigger, Source format, Extraction, Promotion, Scope) for the survey note
- Run semantic review on the updated review note
- Run `/validate` on the updated review note

Write concisely. Prioritize implementation-backed claims over README framing — the existing review already documents several README claims that do not match the code.
