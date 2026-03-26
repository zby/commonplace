<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: prose/unbridged-cross-domain
model: opus-4.6
gate-hash: c05f580b14cb126f3c25acf576d48929a72c4401
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:14:37+01:00
-->
## Unbridged cross-domain evidence review

### Source domains vs argument domain

The note claims generality about **agent context** (LLM context processing in general). Sources span:

- **Liu et al., 2023 (lost in the middle)** — LLM information retrieval. Same domain. No bridge needed.
- **Anthropic, 2025 (context rot)** — LLM engineering practice. Same domain. No bridge needed.
- **Paulsen MECW** — LLM context window measurement. Same domain. No bridge needed.
- **GSM-DC (Yang et al., 2025)** — math reasoning with distractors. Narrower domain.
- **Chung et al., 2025** — web agent multi-session tasks. Same domain (agent context). No bridge needed.
- **ConvexBench (Liu et al., 2026)** — symbolic convexity checking. Narrower domain.

### Bridge analysis

**GSM-DC**: The note cites "power-law error scaling with distractor count in math problems" — it names the source domain (math problems). The note then treats this as evidence for the general Volume dimension. The bridge (math reasoning degradation transfers to general LLM context because the mechanism is attention dilution, which is architecture-level) is not explicitly stated. However, the note uses GSM-DC alongside Chung et al. (web agents), which covers a different task type with the same degradation pattern. The convergence across task types implicitly argues for architecture-generality, but this argument is not made explicit.

**ConvexBench**: The note cites specific results from symbolic convexity checking and concludes "Compositional depth, not volume, was the bottleneck." The bridge to general agent context (compositional depth degrades LLM performance regardless of task domain) is not stated, though the mechanism (attention distribution / reasoning horizon limitation) is architecture-level and plausibly task-general.

### Findings

**INFO — Cross-domain convergence argument is implicit.** The note cites evidence from math reasoning (GSM-DC), web agent tasks (Chung et al.), and symbolic reasoning (ConvexBench) to support claims about agent context in general. The diversity of task domains is actually the strongest evidence for generality, but the note never explicitly makes this convergence argument — it presents each source as evidence for its respective dimension without stating that the cross-domain consistency supports architectural generality. A single sentence noting that the pattern appears across diverse task types would strengthen the bridge.
