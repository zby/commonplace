---
description: Separated Evidence and Reasoning sections let human reviewers check facts and logic independently — a purely readability argument that doesn't depend on LLM behavior at all
type: note
areas: [document-system]
status: seedling
---

# Structured output is easier for humans to review

Even if LLMs neither reason better through structure ([failure-mode transfer](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md)) nor produce better content through continuation ([distribution activation](./structure-activates-higher-quality-training-distributions.md)), structured output is easier for humans to evaluate and critique.

A claim with separated Evidence and Reasoning sections lets a reader check each independently — "are these facts right?" and "does this logic follow?" are easier questions than "is this essay correct?" The separation turns a holistic judgment call into a series of focused checks, each with a clearer standard of correctness.

This argument doesn't depend on LLMs at all. It's purely about readability. Structured document types become a guarantee that LLM output arrives in a form amenable to human review. The same principle applies to human-written documents — scientific papers are easier to review than essays for the same reason — but it's especially valuable for LLM output because the reviewer can't assume shared background or intent with the author.

---

Relevant Notes:
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — complementary: a first independent argument for structured types (failure-mode transfer)
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — complementary: a second independent argument (distribution selection)
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types

Topics:
- [document-system](./document-system.md)
