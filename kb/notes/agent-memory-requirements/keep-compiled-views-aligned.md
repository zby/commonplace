---
description: "Generated cues, prompt files, indexes, and assistant-specific views need source-of-truth rules so they do not drift into authority"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
status: current
---

# Keep Memory Roles And Compiled Views From Drifting

Memory systems often create derived surfaces: a note produces a cue, a policy produces a checklist, a convention produces a lint rule, a guide produces an `AGENTS.md` excerpt, or a trace-derived observation produces a generated reminder. These surfaces put knowledge where it can act, but they become dangerous when they turn into independent sources of truth.

The system should distinguish storage forms by memory role and reconstruction cost: durable authored memory, raw evidence, generated navigation views, operational reports, trust ledgers, compiled behavior views, and external authority surfaces. A rebuildable index should not become a policy. A temporal review judgment should not be hidden where staleness checks cannot read it. A ticket, report, dashboard, or source file may remain the true authority even when the memory system keeps a distilled view of it.

## Source-Of-Truth Rules

Every behavior-changing derivative needs source-of-truth rules. A library-derived cue should be treated as a compiled view, not as a separate policy. It should carry provenance, source version or hash, generation time, owner, and regeneration rules. If the source changes, the cue must regenerate or be marked stale. Direct edits to compiled cues should either flow back to the source or remain candidate-stage material.

This applies more strongly to system-definition artifacts than to ordinary summaries because drift can change behavior. [Always-loaded context mechanisms in agent harnesses](../always-loaded-context-mechanisms-in-agent-harnesses.md) shows that behavior-shaping context can live in many places: prompts, files, tool descriptions, capabilities, configs, skills, and memory. The more surfaces exist, the more explicit the authority model must be.

[Synapptic](../../agent-memory-systems/reviews/synapptic.md) provides a concrete compiled-view pattern: the YAML profile is the durable state, while Claude memory, Cursor rules, Copilot instructions, `AGENTS.md`, and other assistant files are render targets with target-specific filtering. That is closer to the right authority model than treating every emitted prompt file as an independent memory.

## Evaluation Questions

- Can every generated or compiled surface name its authoritative source?
- Does the system detect stale compiled views after source changes?
- Are behavior-changing views governed more strictly than ordinary summaries?
- Can direct edits to compiled views flow back to the source or remain candidate-stage?

---

Relevant Notes:

- [Always-loaded context mechanisms in agent harnesses](../always-loaded-context-mechanisms-in-agent-harnesses.md) - maps the many places behavior-shaping context can live
- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - places compiled-view drift inside the broader memory boundary
