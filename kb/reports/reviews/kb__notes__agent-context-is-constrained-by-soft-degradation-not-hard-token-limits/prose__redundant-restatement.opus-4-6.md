<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/redundant-restatement
model: opus-4.6
gate-hash: 6cc3055529559635ff4f21cc2bd4fc22bf3e9ec4
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:38+01:00
-->
## Redundant restatement review

### Section-opening analysis

**Volume** — Opens: "More tokens dilute attention. The 'lost in the middle' finding..." Immediately presents new evidence. No restatement.

**Complexity** — Opens: "LLMs pay interpretation overhead proportional to context complexity." New claim with its own evidence. No restatement.

**Open questions** — Opens: "Volume and complexity are distinguishable but not fully separable..." Advances the analysis by noting a limitation of the preceding framework. No restatement.

**The soft bound is invisible** — Opens: "This is the critical property. The hard limit is visible — exceed it and the API returns an error. The soft bound is invisible at every level." The second sentence briefly re-states the hard/soft distinction from the opening paragraph, but this is a one-sentence transition that sets up the new three-level analysis. Deleting it would require the reader to hold the hard/soft distinction in memory across two intervening sections. The restatement is minimal and functional.

**Consequences** — Opens: "Don't trust the number on the box." New actionable claim. No restatement.

### Assessment

Each section advances rather than re-explains. The one borderline case (invisibility section's opening) is a single-sentence bridge, well below the threshold of "a full re-explanation."

No redundant restatement found. Clean pass.
