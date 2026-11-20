---
description: Repair a claim-strength finding when the note already supports a more informative title without any body edits
type: types/edit-operation.md
effort: judgment
decision: none
responds-to: [frontmatter/claim-strength]
---

# Repair a claim title

Make the title assert the contestable claim that the existing note supports.
The session agent handles any file relocation after publication.

## Steps

1. Read the supplied `finding`, the whole note, and any supplied brief and role
   report. Check that the finding still applies. If the title assumes the hard
   point and asserts an obvious consequence, put the hard point in the main
   clause. If it merely states a truism, state the non-obvious result the body
   supports. Do not choose a new thesis.
2. Check the proposed title against the opening, evidence, examples and scope.
   Preserve the claim's force: for example, do not turn a possibility into a
   claim that something occurs routinely. Check that the description adds the
   mechanism or scope without asserting more than the title and body support.
   Keep the resulting filename slug within 70 characters. Do not move the file.
3. If these checks pass, edit only the first H1 and, if needed, the description
   line. Leave notes marked `user-verified` or with a separate frontmatter title
   unchanged. If the body, brief or inbound use prevents a coherent title-only
   repair, return unchanged and identify the exact obstacle. Do not repair the
   body or suggest a full rewrite just because a local clarification is needed.

## Report

Name the claim the title now states and the passage that supports it. If the
note remains unchanged, name the conflicting passage or other reason. If it
needs a local clarification, explain what distinction the operator must settle.

## Preserve

Keep the body, all other frontmatter, the note path and every other file.
