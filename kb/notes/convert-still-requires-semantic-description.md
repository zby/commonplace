# Convert still requires semantic description

The `cp-skill-convert` skill is mostly structural — add frontmatter with fixed
structural values (`type: kb/types/note.md`, `traits: []`, `tags: []`), leave
`user-verified` absent, and align the filename to the title while repairing
backlinks.

But `description` breaks this pattern. Writing a good description requires
reading and understanding the content — it is a semantic judgment. We kept it
because the note schema requires both `description` and `type`; frontmatter
without a description is invalid, not merely hard to retrieve. The requirement
also serves progressive disclosure: agents decide whether to load a note from
its title and description.

Options if we want to make convert fully syntactic:
- Leave the artifact as text until a later semantic step can supply a valid description
- Auto-generate from the first paragraph (mechanical, but often poor quality)
- Accept that description is the one semantic judgment convert must make

Currently we accept the third option. If a script replaces the skill, this is the part that still needs LLM involvement.
