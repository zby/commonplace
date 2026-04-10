# Token Wiki review workshop

Workshop for analyzing `related-systems/token-wiki/` (10 chapters on token management across
four production LLM harnesses: Claude Code, Cline, Codex, OpenCode) against commonplace theory.

**Entry points:**

- [`chapter-analyses.md`](./chapter-analyses.md) — per-chapter ingest-style summaries: central
  claim, mechanisms, data points, and the KB note each chapter lands against.
- [`synthesis.md`](./synthesis.md) — main synthesis doc. Maps token-wiki findings onto existing
  KB theory, identifies three genuine gaps (cache economics, observability, output-token
  reservation), surfaces the tension with the bounded-context orchestration model, and lists
  candidate follow-ups (new notes and additions to existing notes) for later human review.

**Status.** Workshop-layer analysis. No KB files were modified.

**Recommended next actions** (from `synthesis.md` §5):

1. Promote to a `kb/notes/related-systems/token-wiki.md` review (highest immediate value).
2. Write new note: *Prompt caching is a second scarce resource that constrains context
   management mechanisms.*
3. Add observability as a fifth operational component in the context-engineering definition.
4. Smaller additions to: context-efficiency, soft-degradation, scoping, loading-frequency,
   always-loaded, frontloading, session-history, bounded-context-orchestration notes.
