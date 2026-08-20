---
description: "Predicts that, for distant or non-obvious uses of a natural-language declaration, generated local materialization will outperform declaration-only presentation without creating a second maintenance authority"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis, computational-model]
---

# Local materialization should outperform distant natural-language declarations

**Local materialization** means rendering a canonical fact beside the passage or instruction whose correct output depends on it. This note advances a statistical conjecture: across a preregistered sample of LLM tasks in which the declaration is distant or applying it requires a non-obvious inference, local materialization should produce a higher rate of correct, non-contradictory application than declaration-only presentation. A difference of zero or less on a held-out evaluation set would refute the conjecture. It is currently untested.

## Why local materialization might help

A use site is the passage or instruction whose correct output depends on the fact. In a formal system, an immutable binding under a fixed environment has assigned resolution semantics. Code that reads the binding receives its value through those semantics rather than reconstructing it from surrounding prose. This property belongs to the defined consumer; it does not guarantee that one declaration is available in every program or context.

Natural-language content has no equivalent operation with assigned consequences. A fact declared in frontmatter, such as `user-verified: true`, affects a later output only if the declaration conditions that output and the model applies the fact at the relevant use site. Even deterministic decoding does not uniquely specify this application: [agentic systems can produce behavior consistent with an interpretation that the instruction does not determine](./agentic-systems-interpret-underspecified-instructions.md). This difference motivates testing local materialization, but it does not establish that reliability declines monotonically with distance.

Instead of maintaining independent prose copies, an assembler can keep one canonical symbolic value and render an exact value or fixed derived label at each use site. The local view removes the need to recover a distant declaration while preserving a single maintenance authority.

What can be materialized safely depends on [representational form, or how retained content is encoded and consumed](./definitions/representational-form.md). Literal values and mechanically derived labels can be regenerated or checked against their source. A contextual natural-language consequence generally cannot be certified by deterministic equality. It needs explicit lineage and judgment-based review, or it should be omitted when its maintenance risk exceeds the expected benefit.

## Costs

- **Bulk.** Each local view adds text, and the extra context can reduce performance elsewhere.
- **Conditional applicability.** A conditional fact requires either template branching or a renderer that emits the local view only when the committed condition holds.
- **Verification.** Literal or derived views need a deterministic guard; interpretive consequences instead need human or assay review.

## Testing the conjecture

The experiment should compare three primary arms: declaration only, a human-authored point-of-use restatement, and a point-of-use view generated from the canonical value. It should also include a matched control with the same local position, emphasis, and approximate token budget but no restatement of the fact, so that the intervention tests more than added salience.

The experiment should vary three pressures independently: token or section distance, intervening competing content, and the inferential non-obviousness of applying the declaration. The task and model sample should be preregistered and stratified by fact type. Evaluation should measure both whether the downstream output applies the fact correctly and whether it contradicts the canonical value elsewhere. The primary comparison is the rate of correct, non-contradictory application on a held-out evaluation set.

The statistical claim fails if generated local materialization does not beat declaration-only presentation under the stated conditions. It also fails operationally if any gain in local application is offset by enough added contradiction or context cost that correct, consistent task performance is no better. Until that comparison exists, local materialization is a candidate intervention rather than a default rule.

---

Relevant Notes:

- [Codification](./definitions/codification.md) — contrasts: a symbolic consumer assigns consequences to a binding; the natural-language consumer studied here does not have that reference operation
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: both move information to consumption time, but frontloading precomputes known inputs while local materialization tests whether proximity changes behavioral use
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — exemplifies: a displayed verification label may take the checked branch when it is mechanically derived from `user-verified`; a contextual judgment cannot
- [Links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md) — extends: a reader may not follow a reference, so content required at every use must arrive through an enforced consumption path or be present locally
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — contrasts: absent boundaries can make content over-reach, while absent dereference can make a declaration under-reach
