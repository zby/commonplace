# text

The root type. A markdown file with no frontmatter.

`text` represents a thought captured before it has enough shape to structure. The absence of frontmatter *is* the type — no `type: text` field is needed or possible.

## Structural test

- File does not start with `---`

## Validation

No type-specific schema, title, slug, or link-health checks apply. Repository
boundary checks may still apply; see the [validation
contract](../reference/validation-contract.md).

## Semantics

- Text has no implied maturity or verification state.
- When a text file gains frontmatter, conversion never adds `user-verified`; verification requires a later explicit human attestation.
- A text file that persists without structuring is a candidate for pruning.

## Promotion

`text` → [note](./note.md): add valid note frontmatter with both required
fields:

- `description` — a non-empty retrieval description that discriminates the
  artifact from nearby notes; and
- `type: kb/types/note.md` — the path that selects the base note contract.

`traits` and `tags` are optional in the note schema; `cp-skill-convert`
initializes both as empty lists. Conversion must leave `user-verified` absent
because only a later explicit human attestation can add it. Use
`cp-skill-convert` or perform the same conversion manually.
