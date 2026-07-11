# text

The root type. A markdown file with no frontmatter.

`text` represents a thought captured before it has enough shape to structure. The absence of frontmatter *is* the type — no `type: text` field is needed or possible.

## Structural test

- File does not start with `---`

## Validation

Always valid. No checks apply.

## Semantics

- Text has no implied maturity or verification state.
- When a text file gains frontmatter, conversion never adds `user-verified`; verification requires a later explicit human attestation.
- A text file that persists without structuring is a candidate for pruning.

## Promotion

`text` → [note](./note.md): add frontmatter with at least a `description` field. Use `/cp-skill-convert` or do it manually.
