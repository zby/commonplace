---
description: "Try when extracting a standalone note from source material and the note may draw a stronger conclusion than the source supports."
type: types/instruction.md
---

# Check what a note extraction adds

Distinguish the claim you are extracting from any inference you add to make the note stand on its own.

When the operator names this instruction for an extraction, read the source material in context. Before drafting:

1. State the weakest claim the note needs to carry forward. If the source uses it as a premise, ask what the reader could no longer conclude without it. If the source only records an observation, state the observation before proposing an explanation.
2. State the claim you would give the note. If you are just moving a settled argument and its qualifications, proceed with the extraction. Otherwise name the extra inference.
3. Try one concrete case in which the source claim holds but the added inference fails. For a claim of necessity, try to achieve the same outcome without the proposed mechanism. Keep the resources, available information, and success conditions fixed. If the alternative needs a condition to change, name it: you have found a boundary, not a counterexample under the original conditions.
4. State what survives the contrast. Keep the stronger claim if you can justify the inference; otherwise narrow it or identify the unresolved premise. Failing to think of an alternative is not a justification.

If the source will cite the extracted note, check that the citation sentence says no more than the note supports. Propose any correction rather than editing the source unless it is in scope.

**Example — extracting a note from an article.** An article describes a learning loop in which a model diagnoses failures and proposes repairs. The extracted note says the model *must* diagnose failures for the loop to improve. Suppose the harness can try every available patch within budget and a test can recognize a repair. The loop can then improve without a diagnosis. The note can explain when diagnosis helps the model find a repair outside that search, but the article should not cite it as establishing a universal requirement.
