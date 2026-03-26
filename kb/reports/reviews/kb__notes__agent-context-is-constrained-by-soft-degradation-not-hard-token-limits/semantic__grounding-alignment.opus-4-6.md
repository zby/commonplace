<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: semantic/grounding-alignment
model: opus-4.6
gate-hash: bcdd500e6c1fe6d609dd9c680963a3db4f141452
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:07:01+01:00
-->
## Grounding alignment review

Sources followed (5): GSM-DC ingest, Chung et al. web-agent ingest, ConvexBench ingest, Paulsen MECW snapshot, Ebrahimi et al. induction-bias paper. Also followed linked notes: effective-context, indirection-is-costly.

### Source-by-source attribution check

**Paulsen MECW** — The note claims "usable context can be far below advertised windows and is task-dependent." The source confirms: "MECW is, not only, drastically different from the MCW but also shifts based on the problem type." Accurate, no scope mismatch.

**GSM-DC (Yang et al., 2025)** — The note claims "power-law error scaling with distractor count in math problems." The ingest confirms: "accuracy degrades with distractor count following a power law whose exponent grows with reasoning depth." Accurate.

**Chung et al. (2025)** — The note claims "injecting irrelevant task sequences into a web agent benchmark collapses success rates from 40-50% to under 10%." The ingest confirms: "success rates collapse from 40-50% at baseline to under 10% at 150k tokens." The note adds "Bolt-on retrieval (iRAG) provided only modest improvement, suggesting irrelevant context may need to be excluded rather than compensated for — though this rests on a single retrieval approach." The hedge matches the ingest's own limitation ("iRAG is one retrieval strategy"). Accurate.

**ConvexBench (Liu et al., 2026)** — The note claims "F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100, even though total tokens (5,331 at depth 100) were far below context limits" and "Compositional depth, not volume, was the bottleneck." The ingest confirms both claims and characterises the degradation as "an attention-distribution and reasoning-horizon problem, not a token-capacity problem." Accurate.

**Ebrahimi et al. (2026)** — The Relevant Notes section labels this as "candidate mechanism (volume dimension): transformers learn length-specific solutions in isolation (sharing factor kappa approximately 1) and suffer destructive interference at mixed lengths (kappa = 0.28)." The source confirms: Observation 4.1 shows kappa near 1 for all transformer formats; Observation 4.2 shows kappa = 0.28 specifically for CoT. The caveat ("training-time evidence on synthetic tasks, not direct measurement of inference-time context degradation") appropriately scopes the connection.

**Indirection note** — The note says "Every layer of indirection costs context and interpretation overhead." The linked note confirms this claim is its central thesis. Accurate.

**Effective-context note** — Cited inline: "Effective context is task-relative and complexity-relative, not a fixed model constant." The linked note's body and description confirm this. The relationship label "sharpens" is accurate.

### Domain coverage

- **Volume dimension**: grounded by Paulsen, GSM-DC, Chung et al. Three independent sources.
- **Complexity dimension**: grounded by ConvexBench (primary), with indirection note as mechanism link.
- **Invisibility argument**: the three-level analysis (practitioner/benchmarker/market) is the note's own analytical contribution, not sourced to any single paper. Appropriate — it synthesizes the pattern across sources.
- **Consequences**: the "heuristic design is rational" and "programmatic constructability" arguments are inferences from the evidence. They follow logically from the invisibility and task-dependence premises.

### Inference checks

**INFO — Ebrahimi placement under "volume dimension" is loose.** The Ebrahimi paper studies training-time data efficiency and weight sharing across sequence lengths in synthetic state-tracking tasks. The note places it under "candidate mechanism (volume dimension)." The connection chain is: transformers learn length-specific solutions at training time, so at inference time, longer contexts may encounter out-of-distribution length regimes. This is plausible but has an unverified step — the paper does not test inference-time degradation. The "candidate mechanism" label and caveat mitigate the gap, but a reader following the link expecting direct evidence for the volume dimension of inference-time soft degradation will find training-time data efficiency results instead.

**INFO — "too small for pure attention dilution" inference is not grounded in a stated threshold.** The Open Questions section says "GSM-DC's degradation occurs at token counts that appear too small for pure attention dilution to explain (our inference, not the paper's)." The note correctly flags this as its own inference. However, the threshold for what counts as "too small for pure attention dilution" is not specified, making the inference hard to evaluate. The note could be strengthened by stating the approximate token counts of the GSM-DC experiments and referencing what scale pure attention dilution is typically observed at, or by softening to "may be too small."

### Verdict

No WARN-level issues. All five primary sources are accurately represented. Vocabulary matches source terminology. Scope of claims matches scope of evidence. The two INFO items identify places where inferential chains extend slightly beyond what individual sources establish, but in both cases the note signals tentativeness appropriately. The central argument — soft degradation, not hard limits, is the binding constraint — is well-grounded in converging evidence.
