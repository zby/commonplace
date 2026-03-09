---
description: Evans argues that separating modeling (schema creation) from classification (schema application) tames LLM non-determinism — a practitioner case study of stabilisation via taxonomy freezing
source_snapshot: eric-evans-ai-components-deterministic-system.md
ingested: 2026-03-09
type: practitioner-report
domains: [stabilisation, classification-systems, LLM-integration, domain-driven-design]
---

# Ingest: AI Components for a Deterministic System (An Example)

Source: eric-evans-ai-components-deterministic-system.md
Captured: 2026-03-09
From: https://www.domainlanguage.com/articles/ai-components-deterministic-system/

## Classification

Type: **practitioner-report** — Evans built a concrete system (domain classification of OpenEMR code modules), reports what worked and what didn't, and extracts transferable design principles. It has a conceptual essay layer (the modeling-vs-classification distinction), but the article is grounded in a working implementation with specific results, not pure theory.

Domains: stabilisation, classification-systems, LLM-integration, domain-driven-design

Author: Eric Evans, creator of Domain-Driven Design. His authority is in software architecture and strategic design, not ML/NLP per se. His DDD lens is what makes the article distinctive — he frames the LLM integration problem as a modeling/classification boundary, which is a DDD concept transplanted into the AI domain.

## Summary

Evans demonstrates that asking an LLM to both create a classification scheme and apply it in a single step produces inconsistent, incomparable results. His solution: separate the modeling phase (generate or select a canonical taxonomy) from the classification phase (apply frozen categories to individual items). Using OpenEMR code classification as a case study, he shows that adopting published standards like NAICS for generic domains yields dramatically better consistency than custom LLM-generated categories. He also explores iterative refinement with critic/judge models for cases where custom taxonomies are needed, and proposes an incremental update pattern for evolving schemas. The key claim: "Creating a classification system is a modeling task, which is much harder than the classification task itself."

## Connections Found

The `/connect` discovery found 7 connections, all in the learning-theory cluster.

**Strong connections:**

- **[stabilisation](../notes/stabilisation.md)** — exemplifies: Evans' "freeze the taxonomy" is stabilisation on the heavy end of the spectrum — committing to a single interpretation (the taxonomy) before operating deterministically within it.
- **[storing LLM outputs is stabilisation](../notes/storing-llm-outputs-is-stabilization.md)** — exemplifies: Evans' frozen taxonomy is the specific instance already cited under "Strategy 1: Constrain the generator." The source provides the concrete OpenEMR case study behind that reference.
- **[agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)** — exemplifies: "What domain does this code address?" is semantically underspecified (admits multiple valid category schemes) AND execution-indeterminate (inconsistent formats across runs). Evans' solution is interpretation narrowing — pre-resolve the modeling ambiguity so the classification step has a single valid scheme.
- **[spec mining as crystallisation](../notes/spec-mining-as-crystallisation.md)** — exemplifies: Evans' iterative refinement phase (sampling, critic, judge) is spec mining — observing LLM behavior and extracting a frozen schema. NAICS is the extreme case where someone else already mined the spec.
- **[bitter lesson boundary](../notes/bitter-lesson-boundary.md)** — grounds: Evans' modeling/classification split maps to the arithmetic/vision-feature distinction. Classification against a frozen schema is arithmetic-regime (spec IS the problem). Creating the schema is vision-feature-regime (spec is a theory about useful categories). Evans' advice to use NAICS is an arithmetic-regime choice: adopt a spec that already exists.
- **[crystallisation and softening navigate the bitter lesson boundary](../notes/crystallisation-and-softening-navigate-the-bitter-lesson-boundary.md)** — exemplifies: Evans' incremental updates pattern (check against existing categories, add genuinely new ones) is the soften/re-crystallise cycle operating on a taxonomy.

## Extractable Value

1. **The NAICS consistency result** — Evans reports that classification against NAICS yielded identical high-confidence results across multiple runs, while custom taxonomies varied each time. This is concrete evidence for the stabilisation claim, not just a theoretical argument. [just-a-reference] — cite-worthy data point for the stabilisation note.

2. **The critic/judge refinement pipeline failing** — Evans tried sampling + critic + judge models and found they didn't improve results for his use case. This negative result is valuable: the iterative refinement loop doesn't always help, and simpler approaches (adopt a published standard) can outperform elaborate pipelines. [quick-win] — add as a caveat to spec-mining-as-crystallisation.

3. **The incremental update pattern** — prompting the LLM to check new items against an existing category set and only add genuinely new ones. This is a concrete implementation of the soften/re-crystallise cycle: the categories are mostly frozen but have a controlled expansion path. [experiment] — could inform how we handle schema evolution in the KB's own type system.

4. **"Generic domain" heuristic for when to use published standards** — Evans' DDD framing: if classification isn't your competitive advantage, use established taxonomies rather than inventing your own. This maps to the bitter lesson boundary but adds a practical decision heuristic. [quick-win] — strengthens the bitter-lesson-boundary note with a practitioner-friendly decision rule.

5. **The modeling/classification task separation as a general design principle** — Evans frames this as a concern-separation principle: don't ask one prompt to both create and apply a schema. The existing analysis note captures this, but the analysis note is in a legacy directory with broken cross-references. The principle deserves a home in the current KB structure. [deep-dive] — requires deciding whether to migrate the legacy analysis note or write a fresh note.

## Limitations (our opinion)

**What is not visible:**

- **Sample size of one.** Evans tested this on a single codebase (OpenEMR) for a single task (domain classification of code modules). The dramatic consistency improvement from NAICS may not generalize to tasks where published standards don't exist or where the taxonomy doesn't align well with the actual structure. He acknowledges this implicitly ("When a domain is generic... use established standards") but the positive results are only shown for the best case.

- **No comparison of classification quality, only consistency.** Evans shows that NAICS-based classification is more *consistent* across runs. He does not evaluate whether the consistent answers are *correct* — whether NAICS categories actually capture the meaningful domain distinctions in OpenEMR's codebase. Consistency and accuracy are different properties; you can get perfectly consistent wrong answers. The KB's [oracle strength spectrum](../notes/oracle-strength-spectrum.md) is relevant here: Evans' verification is effectively measuring reproducibility, which is a weak oracle for correctness.

- **The critic/judge negative result is underspecified.** Evans says advanced refinement techniques "didn't improve results for this particular use case" but doesn't explain why. Was the task too simple for iterative refinement? Were the critic prompts poorly designed? Was the base taxonomy already good enough? Without this analysis, we can't tell whether the negative result generalizes or is specific to his setup.

- **Survivorship bias in the "use published standards" recommendation.** Evans happened to choose a domain (business sectors) where a well-maintained, comprehensive published standard (NAICS) exists. Many practical classification tasks don't have this luxury. The recommendation to "look for published standards" is sound but the article doesn't address what to do when no adequate published standard exists — which is arguably the more common and harder case.

- **The DDD framing imports assumptions.** Evans' distinction between "core domain" (invest in custom modeling) and "generic subdomain" (use published standards) comes from DDD. This framing assumes you can cleanly separate what's strategic from what's generic — which is itself a modeling task that requires judgment. The bitter lesson boundary note in this KB raises the harder question: even for your "core domain," is hand-crafted taxonomy a temporary expedient that scale will eat?

## Recommended Next Action

File as reference. The specific data points noted above (NAICS consistency result, critic/judge negative result) can be added as supporting evidence to existing notes during regular maintenance passes.
