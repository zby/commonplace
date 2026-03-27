Key claims extracted from each section:

- **Section 1 (What is a good agentic KB)**: criterion = contextual competence; constraint = bounded context; "just put everything in context doesn't work."
- **Section 2 (Three properties)**: discoverable → composable → trustworthy; dependency order: discoverability is foundation; composability depends on both discoverability and trustworthiness; trustworthiness depends on discoverability.
- **Section 3 (Operations, body)**: "Three operations transform accumulated knowledge" (constraining, distillation, discovery). Then: "A fourth operation works by subtraction: **Pruning**." So the body distinguishes *transformation* (three operations) from *subtraction* (pruning).
- **Section 3 (Operations, table)**: lists five rows — accumulation, constraining, distillation, discovery, pruning — treating all five symmetrically.
- **Compressed summary**: "Four operations transform accumulated knowledge: constraining improves trustworthiness, distillation improves discoverability, discovery improves composability... and pruning removes stale knowledge."
- **Section 4 (Reach)**: accumulation is where reach varies most; constraining preserves reach but doesn't create it; distillation can preserve or destroy reach; discovery creates reach.
- **Section 5 (Tension)**: reach vs. action value; resolution: both coexist; operations serve different needs.
- **Section 6 (Authored knowledge)**: authoring produces reach; extraction systems produce adaptive knowledge.

---

**WARN — body/summary mismatch on operation classification**

The body explicitly distinguishes transformation (constraining, distillation, discovery) from subtraction (pruning): "Three operations transform accumulated knowledge... A fourth operation works by subtraction: Pruning." This is a deliberate conceptual distinction — transformation acts on existing knowledge to improve its properties; subtraction removes knowledge from the store.

The compressed summary collapses this: "Four operations transform accumulated knowledge: constraining..., distillation..., discovery..., and pruning removes stale knowledge." Pruning is now listed as a transforming operation. This contradicts the body's category structure. The inconsistency isn't merely terminological — it affects the reader's understanding of what pruning does (remove vs. transform).

**INFO — pruning definition vs. table example**

The body defines pruning as "removes knowledge that is outdated, contradictory, or low-value." The table example includes "marking a superseded claim `outdated`" alongside "Deleting an outdated note." Marking is not removing. A marked-outdated note remains in the KB and can still be loaded, linked, and mislead. The definition covers only hard removal; the example introduces soft pruning without updating the definition. This is also flagged in the completeness-boundary-cases review; it recurs here as a local inconsistency within the operations section.

**Definition drift: none observed**

"Contextual competence," "bounded context," "reach," "discoverable," "composable," "trustworthy," "accumulation," "constraining," "distillation," "discovery" — all used consistently across sections. No drift detected.

**Pairwise contradiction checks: none found**

- "Discoverability is the foundation" (section 2) is consistent with composability depending on both discoverability and trustworthiness — discoverability is foundational because the other two can't function without it.
- "Constraining preserves reach but doesn't create it" (section 4) is consistent with "constraining primarily improves trustworthiness" (section 3) — trustworthiness and reach are orthogonal dimensions.
- "Reach matters most when knowledge leaves the KB" (section 5, tension) is consistent with "a compact theory replaces many facts under bounded context" — two different reasons reach is practical, not competing claims.

One WARN (body/summary mismatch on pruning classification), one INFO (pruning definition vs. example scope).
