# Type-menu clause audit

## Scope and method

This audit covers every row in the eight collection `## Types` sections that enumerate artifact types. It asks whether each row carries a rule that would be lost when the menu is removed. The check compared the row with the rest of its `COLLECTION.md`, the referenced type contract, and the artifact types actually used in that collection.

[`kb/types/COLLECTION.md`](../../types/COLLECTION.md) is not in scope because it already derives the type of each artifact rather than presenting a menu. The nested dialectical sample collection is also not in scope because it is a workshop fixture with a single local rule, not one of the menus being retired.

## Result

No clause needs to move into a type spec. The type-wide restrictions mentioned by the menus are already owned by their type contracts. Most remaining prose repeats the collection's scope or structure.

Two collection-specific policies exist only in menu rows and must be preserved as ordinary collection prose when the menus are removed:

- Definitions of KB vocabulary belong under `kb/notes/definitions/`.
- A raw source capture may remain frontmatter-free while it awaits classification.

Review gates create no additional classification problem for this audit. They belong to the instructions collection, and [`review-gate`](../../types/review-gate.md) is an instruction type. Its path is its complete type identity; classifying it as an instruction does not require inheritance or a second `type:` value. The review-gate contract owns its particular schema, body shape, catalog identity, and verdict protocol, while the collection contract supplies the shared prescriptive context.

## Row dispositions

“Drop” means that removal loses no binding information because the named owner already states the rule. “Preserve locally” means that the clause should become ordinary prose in that collection rather than a type-wide rule.

| collection | menu row | disposition |
|---|---|---|
| `agent-memory-systems` | `agent-memory-system-review` | Drop. The collection's Structure section and the [local review contract](../../agent-memory-systems/types/agent-memory-system-review.md) already own the source-tier distinction and `lightweight/` placement. |
| `agent-memory-systems` | `note` | Drop. Cross-system analysis is already part of the collection's scope and Structure section; the global [note contract](../../types/note.md) owns the shape. |
| `agent-memory-systems` | `index` | Drop. The collection's Structure section distinguishes its hand-authored README, and the [generated-index contract](../../types/generated-index.md) already restricts generated indexes to build output. |
| `agentic-systems` | `note` | Drop. System, feature, and cross-system analysis are already named in the collection's scope and Structure section. |
| `agentic-systems` | `index` | Drop. The [generated-index contract](../../types/generated-index.md) owns the build-time-only restriction; the collection already describes its hand-authored README. |
| `articles` | `article` | Drop. The collection opening and lifecycle already say that articles are outward-facing, dated distillations, and the [article contract](../../articles/types/article.md) owns their form. |
| `instructions` | `instruction` | Drop. Procedures, skills, wrappers, and review gates are already part of the collection's prescriptive scope. The [instruction contract](../../types/instruction.md) and [review-gate contract](../../types/review-gate.md) own their respective forms. |
| `instructions` | `index` | Drop. The [generated-index contract](../../types/generated-index.md) owns the build-time-only restriction. |
| `notes` | `note` | Drop. Transferable theory is the collection's declared text contract; the [note contract](../../types/note.md) owns the form. |
| `notes` | `structured-claim` | Drop. The [local contract](../../notes/types/structured-claim.md) already requires the evidence and reasoning structure. |
| `notes` | `definition` | Preserve locally. Add the `kb/notes/definitions/` placement rule to ordinary collection prose. Do not put it in the global [definition contract](../../types/definition.md), which is also valid in other collections. |
| `notes` | `tag-readme` | Drop. The [tag-readme contract](../../types/tag-readme.md) owns the filename, weight gate, and optional validated marks. |
| `notes` | `index` | Drop. The [generated-index contract](../../types/generated-index.md) already says generated indexes are virtual build output and must not be committed. |
| `reference` | `note` | Drop. The collection scope supplies “shipped-system reference”; the global note contract supplies the artifact form. |
| `reference` | `adr` | Drop. The collection's ADR conventions and the [local ADR contract](../../reference/types/adr.md) already own the role and form. |
| `reference` | `design-proposal` | Drop. The collection's Proposal exception and the [design-proposal contract](../../reference/types/design-proposal.md) already own placement under `proposals/` and retirement behavior. |
| `reference` | `definition` | Drop. The collection scope narrows the global definition form to shipped-system vocabulary; there is no extra rule in the row. |
| `reference` | `index` | Drop. The [generated-index contract](../../types/generated-index.md) owns the build-time-only restriction. |
| `sources` | `snapshot` | Drop. Capture boundaries are already stated by the collection opening and the [snapshot contract](../../sources/types/snapshot.md). |
| `sources` | `ingest-report` | Drop. The collection opening and [ingest-report contract](../../sources/types/ingest-report.md) already distinguish analysis from capture. |
| `sources` | `source-review` | Drop. The collection's title conventions and the [source-review contract](../../sources/types/source-review.md) already own its role and form. |
| `sources` | implicit `text` | Preserve locally. State in ordinary collection prose that a raw capture may remain frontmatter-free while awaiting classification. Once classified as a snapshot or another type, it follows that contract. |
| `work` | `note` | Drop. The workshop lifecycle already explains pre-promotion artifacts, and the global note contract owns note form. |
| `work` | `instruction` | Drop. Temporary procedures are already admitted by the workshop scope; the instruction contract owns their form. |
| `work` | `structured-claim` | Drop. The real notes-local contract owns the form, while the workshop's future eligibility rule owns permission to reference it. |
| `work` | `index` | Drop. The generated-index contract owns the restriction. |
| `work` | implicit `text` | Drop. The collection opening already says that incomplete workshop artifacts may be plain Markdown without frontmatter. |

## Actual-use check

A normalized scan of resolved `type:` pointers confirms that the menus are neither inventories nor authorization boundaries:

- `kb/instructions/` contains 46 artifacts whose type is `review-gate`. The menu describes gates as instructions without naming that type path, so it is not an exact inventory.
- `kb/work/` contains an ADR and a type spec that its menu does not list. This is expected for a lifecycle layer that can stage work for any collection and test type contracts.
- The collections with local type specs use `type-spec` for those specs, but their menus do not list it.
- `kb/sources/` contains two global `note` artifacts that its menu does not list.
- The `index` rows have no committed generated-index instances, as required by that contract.

These mismatches are evidence against repairing or expanding the menus. The artifact's path-valued `type:` pointer identifies its contract; validator policy should decide whether that path is eligible in the artifact's collection.

## Migration handoff

When the menus are removed:

1. Add the notes definition placement sentence to [`kb/notes/COLLECTION.md`](../../notes/COLLECTION.md).
2. Add the raw-capture allowance to [`kb/sources/COLLECTION.md`](../../sources/COLLECTION.md).
3. Do not migrate any row into a type spec and do not add a `review-gate` menu row. The existing review-gate contract remains the exact type definition for those instruction artifacts.
4. Delete all other row prose after the consumers and validator no longer treat menus as authorization.
5. Replace the work menu with the lifecycle exception already specified in the [implementation plan](plan.md): any artifact under `kb/work/` may reference any valid type spec.
