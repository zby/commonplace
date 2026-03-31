Key claims extracted from each section:

- **Section 1 (What is a good agentic KB)**: criterion = contextual competence; constraint = bounded context; "just put everything in context doesn't work."
- **Section 2 (Three properties)**: discoverable, composable, trustworthy; dependency structure: discoverability is foundation, composability depends on both others, trustworthiness depends on discoverability.
- **Section 3 (Operations)**: body distinguishes *transformation* (constraining, distillation, discovery) from *subtraction* (pruning): "Three operations transform accumulated knowledge... A fourth operation works by subtraction: Pruning." Table lists all five symmetrically.
- **Section 4 (Reach)**: accumulation is where reach varies most; constraining preserves reach; distillation can preserve or destroy reach; discovery creates reach.
- **Section 5 (Tension)**: reach vs. action value; resolution: both coexist, operations serve different needs.
- **Section 6 (Authored knowledge)**: authoring produces reach; extraction produces adaptive knowledge (with hedge).
- **Compressed summary**: "Three operations transform accumulated knowledge: constraining improves trustworthiness, distillation improves discoverability, discovery improves composability and produces the highest-reach items to accumulate. A fourth operates by subtraction: pruning removes stale knowledge."

---

**Body/summary alignment on operation classification**

The body explicitly distinguishes transformation from subtraction: "Three operations transform accumulated knowledge... A fourth operation works by subtraction." The compressed summary preserves this distinction: "Three operations transform accumulated knowledge... A fourth operates by subtraction: pruning removes stale knowledge." ✓ — The summary correctly maintains the body's category structure.

**INFO — summary compresses the authored-vs-extracted nuance**

The body's final section includes an important hedge: "This isn't a claim that extraction can never produce knowledge with reach — an LLM that extracted causal explanations from papers might." The summary says "Authoring — the act of judgment that explains *why* — is the primary source of knowledge with reach" without the hedge. The summary's claim is technically accurate (authoring is the *primary* source, not the *only* source), but the nuance is lost. A reader who only reads the summary could take a stronger position than the body supports.

**Definition drift: none observed**

"Contextual competence," "bounded context," "reach," "discoverable," "composable," "trustworthy," "accumulation," "constraining," "distillation," "discovery," "pruning" — all used consistently across sections. No term shifts meaning between its introduction and later use.

**Pairwise contradiction checks**

- "Discoverability is the foundation" (section 2) vs. composability depending on both discoverability and trustworthiness — consistent; discoverability is foundational because the other two can't function without it, but trustworthiness is independently needed for composability.
- "Constraining preserves reach but doesn't create it" (section 4) vs. "constraining primarily improves trustworthiness" (section 3) — consistent; trustworthiness and reach are orthogonal dimensions.
- "Reach matters most when knowledge leaves the KB" (section 5) vs. "a compact theory replaces many facts under bounded context" (also section 5) — consistent; two complementary reasons reach is practical, not competing claims.
- "Authoring produces reach" (section 6) vs. "extraction can't produce knowledge with reach" — the body explicitly does NOT make the latter claim; it hedges. Consistent.

**INFO — pruning definition vs. example scope**

The body says pruning "removes or deprecates" knowledge. The analysis of pruning's effects says "removing a stale note eliminates a source of wrong premises" — this describes only hard removal, not deprecation. A deprecated-but-present note can still be loaded and used as a premise. The effects analysis and the definition are slightly misaligned in scope. (Also flagged in completeness-boundary-cases review.)

---

No WARN-level contradictions. Two INFOs: summary compresses the extraction hedge, and pruning effects analysis covers only hard removal despite the definition including deprecation.
