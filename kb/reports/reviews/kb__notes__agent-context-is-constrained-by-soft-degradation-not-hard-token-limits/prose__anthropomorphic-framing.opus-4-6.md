<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/anthropomorphic-framing
model: opus-4.6
gate-hash: 4a8b5ccec3e5b0e7174b4392cd3f2325e401e9d7
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:38+01:00
-->
## Anthropomorphic framing review

### Scan results

- "The model doesn't signal when it crosses the soft bound" — "signal" is a systems term. Technical, not anthropomorphic.
- "An LLM produces confident output whether it attended to your context or silently ignored half of it" — "attended" refers to the attention mechanism. "Silently ignored" means failed to incorporate without error signal. Both are behavioral descriptions, not mental-state attributions.
- "missed instructions, shallow reasoning, ignored context" — "reasoning" is standard LLM-discourse usage. "Missed" and "ignored" describe output behavior, not intentional mental states.
- "A CPU signals overflow. A human says 'I'm confused.'" — explicit analogy contrasting system behaviors. The human comparison is illustrative and clearly labeled.
- "the LLM to maintain the mapping in working memory" — appears only in the linked indirection note, not in this note.

The note consistently uses behavioral and functional language. It describes what the model produces and how outputs degrade, not what the model "understands," "believes," or "knows." Where mental-sounding terms appear ("attended," "ignored," "reasoning"), they are standard technical shorthand in the LLM research community and do not imply human-like cognition.

No anthropomorphic framing issues found. Clean pass.
