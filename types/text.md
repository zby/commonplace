# text

The root type. A markdown file with no frontmatter.

`text` represents a thought captured before it has enough shape to structure. The absence of frontmatter *is* the type — no `type: text` field is needed or possible.

## Structural test

- File does not start with `---`

## Validation

Always valid. No checks apply.

## Semantics

- Implicit `status: seedling` — text files are provisional by nature
- When a text file gains frontmatter (promotion to [note](./note.md)), its status should be set explicitly
- A text file that persists without promotion is a candidate for pruning

## Promotion

`text` → [note](./note.md): add frontmatter with at least a `description` field. Use `/convert` or do it manually.
