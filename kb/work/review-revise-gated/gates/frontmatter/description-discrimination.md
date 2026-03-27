---
gate_id: frontmatter/description-discrimination
name: Description discrimination
lens: frontmatter
watches: [title, description]
staleness: changed
---

## Failure mode

The description restates the title or is so generic that it would not help an agent pick this note from a short result list.

## Test

Read the title and the description together. Ask whether the description adds retrieval value beyond the title.

Strong descriptions add at least one of:

- mechanism
- scope
- implication
- context

Descriptions that only paraphrase the title or say "this note discusses X" fail the gate.

## Example (fail)

- Title: `approvals guard against llm mistakes not active attacks`
- Description: "The approval system protects against LLM errors rather than deliberate attacks"

## Example (pass)

- Title: `approvals guard against llm mistakes not active attacks`
- Description: "A determined attacker controls the prompt and can social-engineer approval; approvals catch the common case of tool misuse from hallucination or misunderstanding"
