---
description: Separated Evidence and Reasoning sections let human reviewers check facts and logic independently — a purely readability argument that doesn't depend on LLM behavior at all
type: kb/types/note.md
traits: [title-as-claim]
tags: [type-system]
---

# Structured output is easier for humans to review

Even if failure-mode transfer does not make an LLM reason better and [structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md), structured output remains easier for humans to evaluate and critique.

A claim with separated Evidence and Reasoning sections lets a reader check each independently — "are these facts right?" and "does this logic follow?" are easier questions than "is this essay correct?" The separation turns a holistic judgment call into a series of focused checks, each with a clearer standard of correctness.

This argument doesn't depend on LLMs at all. It's purely about readability. Structured document types become a guarantee that LLM output arrives in a form amenable to human review. The same principle applies to human-written documents — scientific papers are easier to review than essays for the same reason — but it's especially valuable for LLM output because the reviewer can't assume shared background or intent with the author.

---

Relevant Notes:

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — complementary: a first independent argument for structured types (failure-mode transfer)
- [Structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md) — contrasts: bounds a causal rationale that this note's reviewability argument does not need
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types
- [Toulmin Argument (Purdue OWL)](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html) — evidenced-by: Toulmin's separation of grounds from warrant is the theoretical basis for why Evidence/Reasoning sections make review easier — each targets a different verification question
