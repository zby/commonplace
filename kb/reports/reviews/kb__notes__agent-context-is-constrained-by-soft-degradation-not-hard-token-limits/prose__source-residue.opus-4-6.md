<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/source-residue
model: opus-4.6
gate-hash: 29263b6146e1c186126a999e6ad86569c5395c24
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:38+01:00
-->
## Source residue review

### Claimed generality

The title and opening establish the note's scope: agent context windows in general, not any specific task domain.

### Body scan

Domain-specific content in the body:

- "lost in the middle" — attributed to Liu et al. as a named finding. Not residue.
- "context rot" — attributed to Anthropic as their term. Not residue.
- "power-law error scaling with distractor count in math problems" — explicitly scoped to "math problems" and attributed to GSM-DC. Not residue.
- "success rates from 40-50% to under 10%" — attributed to Chung et al. web agent benchmark. Not residue.
- "F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100" — attributed to ConvexBench. Not residue.
- "A CPU signals overflow. A human says 'I'm confused.'" — illustrative analogy, clearly marked as contrast. Not residue.
- "Providers advertise hard token limits" — general observation about the market, not domain-specific.

All domain-specific vocabulary, examples, and data points are properly attributed and framed as evidence from specific sources. The note's general claims are written in its own voice without adopting the vocabulary of any particular source.

No source residue found. Clean pass.
