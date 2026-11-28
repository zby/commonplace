---
description: "When a local check passes but the task fails, distinguish a faulty implementation, a failed handoff, and a requirement that never tested what the user needed."
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, evaluation]
---

# A check can pass without testing what the user needs

Suppose a validator checks that a note contains an *Evidence* heading. A note with that heading and an empty section passes. If the requirement was “reject notes without the heading,” the validator is right. If the objective was “help readers check the claim,” the heading is only a proxy. More tests of heading detection cannot establish that the section contains useful evidence.

Name the **implementation, requirement, and objective** before deciding what to fix. Exactness describes how the implementation meets the requirement. Whether meeting the requirement serves the objective is a separate question. The same validator can settle a formatting question and leave an editorial question open. If formatting is the entire task, no additional test of editorial quality is needed.

[Fintool’s engineering report](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) gives a practical example. Its system maps company-specific fiscal periods to calendar dates and has “200+ test cases just for period extraction.” For Apple, the report maps Q1 2024 to October–December 2023. Even a correct date range does not show that a revenue answer is correct. If the extractor returned the wrong dates, inspect the mapping. If it returned the right dates but the retrieval step ignored them, fix the handoff. Neither failure is a reason to abandon fiscal-period normalization.

When the parts meet their requirements and the handoffs work, test the assumption that the chosen requirements jointly deliver the intended result. If that assumption fails, revise it without treating locally correct work as defective. The heading check might still be worth keeping for formatting; it should no longer stand in for a review of the evidence. Whether to keep the check depends on whether anyone needs that narrower result.

---

Relevant Notes:

- [A proximate target is checked for achievement, not for warrant](./a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — extends: separates achieving a target from showing that pursuing it advances the objective.
