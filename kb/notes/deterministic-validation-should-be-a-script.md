---
description: Half of /validate's checks are hard-oracle (enums, link resolution, frontmatter structure) and could run as a Python script in milliseconds instead of burning LLM tokens via the skill
type: note
traits: []
status: seedling
areas: [document-system]
---

# Deterministic validation should be a script

Our `/validate` skill runs all checks through an LLM (Sonnet), including checks that are purely deterministic. Comparing with [Thalo's 32 validation rules](./related-systems/thalo-type-comparison.md) — all of which are deterministic scripts — reveals that we're spending LLM tokens on work a Python script could do in milliseconds.

The split follows the [oracle strength spectrum](./oracle-strength-spectrum.md):

**Hard oracle (→ script):**
- Frontmatter valid (delimiters, YAML parse, no duplicate keys)
- Description exists and non-empty
- Type/traits/status match allowed enums
- Link targets resolve to existing files
- Areas-Topics footer sync (already have `sync_topic_links.py`)
- Unknown frontmatter fields (flag typos like `descrption:`)
- Required sections per type (spec → Design/Implementation, adr → Context/Decision/Consequences)

**Soft oracle (→ stays in skill):**
- Description quality (discrimination, mechanism vs summary)
- Composability (title works as inline prose)

A validation script could run as a pre-commit hook or in CI, giving instant feedback. The `/validate` skill would then only need to run the judgment-based checks, making it cheaper and faster.

Topics:
- [document-system](./document-system.md)
