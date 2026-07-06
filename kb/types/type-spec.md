---
type: kb/types/type-spec.md
name: type-spec
description: Authoring and validation contract for path-valued Commonplace type specifications
schema: kb/types/type-spec.schema.yaml
---

# Type spec

A type-spec doc is the authoring and validation contract for one Commonplace artifact type. Artifact frontmatter stores the repo-relative path to this doc in `type:`, and this file serves several consumers differently: an author writing a new instance reads it for what to write, someone unfamiliar with the type reads it for what to expect from an instance before opening one, and the validator and the type-conformance reviewer — specified below — read it to check conformance.

## Required Frontmatter

- `type`: `kb/types/type-spec.md`. The root type spec is self-referential and uses the same value.
- `name`: short human-facing type name.
- `description`: retrieval description for the type contract.
- `schema`: repo-relative path to the `.schema.yaml` file that validates artifacts of this type, or `null` when the type has no schema.

## Validation Contract

Two systems check conformance to a type — split by mechanical vs. judgment, not frontmatter vs. body — and a type-spec author writes for both without mixing them:

- **The deterministic validator** checks the [symbolic](../notes/definitions/representational-form.md) half: frontmatter fields, enums, path patterns, and syntactic body shape (required headings, section counts, link health, date formats) — whatever the named `.schema.yaml` can statically specify (e.g. `review-gate.schema.yaml` requires `## Failure mode`/`## Test` headings). It parses structure; it never judges meaning.
- **The type-conformance review gate** checks the semantic half: everything about an instance that is not mechanically checkable — a `description`'s routing quality, a title's claim-shape, whether the body's claims hold up — judged against this file's body, read as [prose](../notes/definitions/representational-form.md) authoring instructions applied by an LLM reviewer ([ADR 038](../reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)). It runs at review time, after the artifact exists, from the finished artifact alone.

Do not restate a schema rule in body prose. The validator already enforces it, so the restatement adds no protection — it only spends the reviewer's judgment re-confirming something already guaranteed, instead of on the properties only a reviewer can check.

## Writing Shape

- Write the body as a **content contract**: checkable properties of a conforming instance, in a form the type-conformance gate can apply directly. Prefer "what a conforming instance contains or claims" over "how to produce one" — production process (which sources to gather, what steps to run, which skill to invoke) is invisible to the reviewer (see Validation Contract), so it belongs in a skill or instruction, linked rather than embedded. This split is aspirational: not every type has a companion skill yet, and some content quality is easiest to state as a light process nudge — but the closer the body stays to content, the more of it the review gate can actually enforce.
- State what the type is for and when an author should choose it over a neighboring type — the same statement is what tells a reader what to expect from an instance before opening one.
- Document the frontmatter fields (required and optional) as a reference for authors; the schema is the sole source of truth for requiredness. Keeping this table in sync with the schema is symbolic-layer bookkeeping, not a semantic judgment — nothing automates the comparison today; that's a validator gap to note, not a reviewer criterion.
- When `schema` is non-null and implies body structure beyond `type`/`name`/`description`, include a `## Template` an authoring agent can copy. Following the template is what actually keeps a new instance schema-aligned in most cases — an author does not need to read the schema directly. For the corner cases the template doesn't cover, the validator's error messages guide the fix; that is where alignment is really enforced, not in the frontmatter table above.
- Add a `## Review` section only if the writing contract above is not enough to guide a reviewer on its own — e.g., the authoring prose is narrative (background, comparisons, rationale) rather than a checklist. It restates the same criteria in reviewer-facing form, so it is a hand-sync obligation, not a one-time addition: nothing else catches it drifting from the body above.

## Template

````markdown
---
type: kb/types/type-spec.md
name: {type-name}
description: "{Retrieval description for this type contract}"
schema: {kb/types/{type-name}.schema.yaml or null}
---

# {Type name}

{What this type is for, and when to choose it over a neighboring type.}

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `{this type spec's own repo path}` |
| `description` | Yes | {retrieval description for instances of this type} |

## Template

```markdown
{a copyable frontmatter + body skeleton matching the schema}
```
````

---

Relevant Notes:

- [ADR 038 — Type-conformance reviews use the type spec as the gate](../reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — depends-on: the conformance wrapper's fallback (no `## Review` section needed) is what makes this file's body itself the operative test
- [review architecture](../reference/review-architecture.md) — see-also: the code that renders the conformance wrapper and reads this file as gate text
- [representational form](../notes/definitions/representational-form.md) — grounds: the symbolic/prose split this section names is that definition's inspection-method rule (test symbolic, read prose) applied to the validator vs. the type-conformance reviewer
- [a derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a `## Review` section restating the rest of the body, and hand-checking frontmatter/schema consistency, are both derived-copy risks this file's Writing Shape avoids by default
- [document-types-should-be-verifiable](../notes/document-types-should-be-verifiable.md) — grounds: why a type contract must assert checkable properties, and why that same contract is what tells a reader what to expect from an instance before opening it — applied here to the contract for type contracts themselves
