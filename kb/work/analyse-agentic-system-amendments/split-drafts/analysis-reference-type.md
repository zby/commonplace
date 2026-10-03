# Analysis reference type draft

Intended owner: `kb/agentic-systems/types/analysis-reference.md`.
Promote with `type: types/type-spec.md`, `name: analysis-reference`, a trigger
specific description and `schema: ./analysis-reference.schema.yaml`.

An analysis reference is workflow-owned navigation to one accepted complete
analysis set. Its stable destination is `kb/agentic-systems/reviews/<slug>.md`.
The destination belongs to one stable source identity. Publication replaces its
selection only after validation and independent review of the exact new set.

## Frontmatter

| Required field | Meaning |
|---|---|
| `type` | `agentic-systems/types/analysis-reference.md` |
| `description` | Accepted overview's retrieval description, copied unchanged |
| `generated-by` | `analyse-agentic-system`; provenance of the reference |
| `analysis-run` | Selected run ID |
| `source-identity` | Stable source identity in the accepted overview register |
| `reviewed-revision` | Accepted set's reviewed boundary |
| `analysis-artifact` | `kb/agentic-system-analyses/retained/<run-id>/ARTIFACT.yaml` |
| `analysis-artifact-sha256` | SHA-256 of the manifest bytes |

Retain the existing pin field names to limit consumer changes. Changing the type
and location does not remove any identity or hash check. Validators require path
run ID, manifest run ID, overview boundary and source identity to agree.

## Body

Code renders only `# <System>` and one labelled link, `Read the accepted
analysis`, to the retained overview. Relative links resolve from the reference.
Do not copy Bounded synthesis, Limitations or member content into the body.
The overview must itself expose limitations and reconciliation. A reference is
not a semantic acceptance certificate by itself; publication checks the gates.

## Historical and ordinary artifacts

Do not retype ordinary authored reviews. Replace current generated reviews only
under the adopted migration authority, retaining their historical versions in
Git. Archive generated reviews remain historical and outside current selection.
