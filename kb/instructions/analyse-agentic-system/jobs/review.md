---
description: "Job of an analyse-agentic-system run: write the body of the compact generated review from the validated set"
type: types/instruction.md
---

# Write the review body

Write `review-body.md`: the body of the compact public review, generated solely from the validated set in `output/` and its primary-source anchors. Give the file frontmatter with one field, `description`: a one-sentence retrieval description of the system's mechanism and limits. Code adds the other fields.

Follow the Body section of the [generated review type](../../../agentic-systems/types/generated-review.md): open with `# <System>`, then one line starting `Evidence basis:` with what the analysis is grounded in, when the evidence was captured, and the reviewed revision; then prose organized by the system's operation, citing set records by ID. Every claim is present in the set; introduce no finding of your own. Give no product ranking, adoption advice, system-wide grade, or transfer recommendation.
