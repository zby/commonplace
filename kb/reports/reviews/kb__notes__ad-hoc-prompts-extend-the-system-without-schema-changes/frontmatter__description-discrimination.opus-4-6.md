FAIL

The description is a near-synonym restatement of the title:

- "ad hoc prompts" → "natural language prompts"
- "extend the system" → "absorb new requirements"
- "without schema changes" → "without changing the deterministic base"

The only additions are "any system with an LLM agent layer" (scope) and "deterministic base" (slight precision on "schema changes"). Neither adds retrieval-discriminating content.

The description does not mention:
- **Mechanism**: homoiconicity (instructions and content share the same representation)
- **Scope**: where on the constraining spectrum prompts sit (loosest end)
- **Trade-off**: zero validation and zero reuse — the cost of the flexibility
- **Implication**: the maturation trajectory from ad hoc prompt → extracted skill

An agent scanning a result list cannot distinguish this note from a note titled "LLM agents accept natural language to change behavior" based on this description. Rewrite to add mechanism or implication — e.g., "Homoiconicity makes this possible: because instructions and content share the same token medium, a markdown file can be both documentation and an executable behavior constraint — no registration, no type system gatekeeping."
