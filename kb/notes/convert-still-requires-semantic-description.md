# Convert still requires semantic description

The `/convert` skill was redesigned to be purely structural — add frontmatter with fixed values (`type: note`, `status: seedling`, `traits: []`, `areas: []`) and align the filename to the title.

But `description` breaks this pattern. Writing a good description requires reading and understanding the content — it's a semantic judgment. We kept it because frontmatter without a description is structurally complete but practically useless (description enables progressive disclosure — agents decide whether to load a note based on title + description).

Options if we want to make convert fully syntactic:
- Leave description empty and add it in a later semantic step (but then the note is "structured" yet unfindable)
- Auto-generate from the first paragraph (mechanical, but often poor quality)
- Accept that description is the one semantic judgment convert must make

Currently we accept the third option. If a script replaces the skill, this is the part that still needs LLM involvement.
