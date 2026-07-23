# Writing conventions for kb/articles/ (editorial profile)

## Text contract and the onward path

Editorial (expository) [profile](../notes/definitions/text-contract.md): outward-facing articles distilled from the KB, published on the [documentation site](../reference/documentation-site.md) for readers outside the project. This profile is being exercised as the worked case of the [external articles collection proposal](../reference/proposals/external-articles-collection.md); it is not yet promoted to the shared [profile catalogue](../reference/text-contract-profiles.md).

**Audience: highly technical** — researchers and builders of agent and knowledge systems. Self-contained means "no KB context assumed", never "simplified"; articles carry full technical weight.

**Quality goal: clarity plus a clear onward path.** An article must stand on its own for a reader with no KB context, and leave that reader knowing where in the KB to go next. Self-containment is the floor, not the ceiling: an article that reads well but strands its reader has failed the contract. The onward path is an editorial obligation, not a claim about conversion or analytics.

**Orientation: every article is an entry point into the KB.** Its job is to lead the reader in, not to replace what the KB establishes.

## Reader-only body

All agent-facing structure lives in frontmatter; the body is reader-only prose.

- No footer link tables, no `Relevant Notes` sections, no link labels.
- No first-use glosses aimed at graph traversal; define terms inline where a technical reader needs them.
- In-prose links into `kb/` are deliberate invitations to go deeper — the onward path — not leakage. Use relative paths; the site renders them as working links. A closing "where to go next" section in prose is encouraged.
- Lineage lives in `source_notes` frontmatter (not rendered), never in the body.

## Title and description conventions

Titles are headlines or topical, addressed to the reader — not claim-titles. The frontmatter `description` stays what it is everywhere in this KB: a retrieval filter for agents. The human-facing abstract is the article's opening paragraph; the two are different texts.

## Attribution and lifecycle

An article carries a `byline` and is a first-person-committed public statement. `status` is one of:

- `draft` — in progress. The page renders with its status visible in the metadata badge; while the collection's published face is small, drafts may sit in the collection root.
- `published` — dated (`published: YYYY-MM-DD`); the body is frozen. Corrections become a dated annotation under a `## Corrections` heading, a superseding article, or a withdrawal — never a silent rewrite.
- `superseded` — set `superseded_by` to the successor's repo-root path; the body stays frozen.
- `withdrawn` — the body stays frozen; state why in a dated annotation.

Maintenance semantics: a published article is a dated record. When its source notes evolve, the question is "would we still say this?" and the remedy is a follow-up article, not an in-place edit.

## Lineage

`source_notes` lists the repo-root paths of the notes and reference documents the article distils. Validation checks that each path resolves. Discovery of affected articles after a note changes is by search (`rg "source_notes" kb/articles/`); there is no freshness registration.

## Types

| type | file | use for |
|---|---|---|
| `article` | `./types/article.md` | outward-facing dated articles distilled from the KB |

## What does NOT belong here

- Transferable claims and theory → `kb/notes/`
- Shipped-system description → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- In-flight exploration → `kb/work/`
- Captured external material → `kb/sources/`
