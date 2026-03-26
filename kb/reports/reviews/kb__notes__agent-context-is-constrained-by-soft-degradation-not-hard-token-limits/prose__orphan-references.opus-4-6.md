<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/orphan-references
model: opus-4.6
gate-hash: 0fa53bb4476c0b558b1103b0fb2fa5faff181b2c
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:38+01:00
-->
## Orphan references review

### Specific claims scanned

| Claim | Source provided | Context sufficient |
|---|---|---|
| "lost in the middle" (Liu et al., 2023) | Yes, with arxiv link | Yes — "established primacy and recency bias" |
| "context rot" (Anthropic, 2025) | Yes, with link | Yes — identified as Anthropic's term |
| Paulsen MECW (2025) | Yes, with arxiv link | Yes — "usable context can be far below advertised windows and is task-dependent" |
| "power-law error scaling with distractor count" (Yang et al., 2025) | Yes, via GSM-DC link | Yes — "in math problems" specifies domain |
| "success rates from 40-50% to under 10%" (Chung et al., 2025) | Yes, with arxiv link | Yes — "injecting irrelevant task sequences into a web agent benchmark" |
| "Bolt-on retrieval (iRAG)" | Yes, same Chung et al. source | Yes — "provided only modest improvement" with caveat |
| "F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100" (Liu et al., 2026) | Yes, via ConvexBench link | Yes — "even though total tokens (5,331 at depth 100) were far below context limits" |
| "kappa approximately 1" and "kappa = 0.28" (Relevant Notes, Ebrahimi et al.) | Yes, with arxiv link | Yes — "sharing factor" defined, caveat about training-time evidence |

Every empirical claim, named study, percentage, and specific data point in the note is sourced with a link and accompanied by enough local context for legibility. No orphan references found.

Clean pass.
