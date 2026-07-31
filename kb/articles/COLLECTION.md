# Writing conventions for kb/articles/ (editorial profile)

Editorial/expository [profile](../reference/text-contract-profiles.md): outward-facing articles distilled from the KB and published on the [documentation site](../reference/documentation-site.md). Adopted by [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md).

**Audience and quality goal.** Highly technical readers with no KB context. The quality goal is **explanatory clarity with technical depth, plus a clear onward path into the KB**. The primary goal is to explain, not impress: a reader should understand the article's claims, mechanisms, evidence, and limits. An article must stand on its own and leave its reader knowing where in the KB to go next.

**Expository method.** Prefer a concrete case before a new abstraction when the case makes the mechanism easier to see. Examples are working parts of the argument, not decoration: say what each example establishes, derive the general claim explicitly, and return to the example when a later section depends on it. State causal links, comparison axes, qualifications, and transitions instead of leaving the reader to infer them.

**Prose register.** Write in direct, functional language. Prefer plain words, explicit verbs, and concrete descriptions. Cut wording whose main effect is to sound elevated, clever, dramatic, or important. For each conspicuously vivid phrase, ask what understanding would be lost if it were stated literally. If none, use direct wording. Metaphor and memorable phrasing are allowed only when they make a mechanism, contrast, or boundary easier to grasp.

**Drafting order.** The first version should be the simplest complete explanation. Establish the central idea, its support or mechanism, concrete grounding, material limits, and the onward path before trying to make the article memorable or easy to circulate. Simple means direct language and organization, not reduced technical content. Do not deliberately add hooks, emotional framing, surprise, stories, or memorable phrasing for promotional effect during this explanatory pass.

Only after the explanation passes review may a separate editorial pass consider spreadability in the sense of Jenkins, Ford, and Green or stickiness in the sense of Heath and Heath's *Made to Stick*. Any such edit must preserve or improve clarity, precision, completeness, and honest statements of confidence and limits.

**Reader-only body.** Agent-facing structure lives in frontmatter; the body is prose for the reader — no footer link tables, link labels, or graph-traversal glosses. In-prose relative links into `kb/` are deliberate invitations to go deeper; a closing "where to go next" section is welcome.

**Titles and descriptions.** Titles are headlines addressed to the reader, not claim-titles. The frontmatter `description` remains what it is everywhere in this KB — a retrieval filter for agents; the reader-facing abstract is the article's opening paragraph.

**Attribution and lifecycle.** Every article carries a `byline` and a `status` (`draft`, `published`, `superseded`, `withdrawn`). Publication freezes the body: corrections happen by dated annotation, a successor article, or withdrawal — never a silent rewrite. These are editorial conventions, not schema: the [type spec](./types/article.md) starts nearly empty and gains constraints only as failure modes are collected.

**Drafting and publication.** Drafts live under `kb/articles/drafts/`, where this contract and the article type still bind but ProperDocs does not publish or index them. [Publish an article](../instructions/publish-an-article.md) by relocating the finished draft to the collection root, changing `status` to `published`, adding a `published: YYYY-MM-DD` date, and listing it in `README.md`. ProperDocs renders the lifecycle status under the title. A published body is frozen; only a dated annotation may be added in place.

**Lineage.** `source_notes` lists the repo-root paths of the notes the article distils; when present, validation checks that each resolves. There is no freshness registration — find affected articles by search.

## Review

Treat these as the operative tests for collection conformance:

- Can a technical reader with no KB context state the article's main claims, how they are supported, and their material limits?
- When an example precedes an abstraction, does the prose say what the example establishes and carry that result into the general argument? Examples-first exposition is allowed; unexplained anecdotes are not.
- Does each paragraph explain, support, qualify, or advance the argument?
- Can an elevated phrase, metaphor, dramatic sentence, or flourish be replaced with plainer language without losing explanatory content? If so, require the replacement.
- Do not request hooks, emotional framing, stories, or quotable phrasing until the explanatory tests above pass. In a later circulation or memorability pass, require every added technique to preserve or improve understanding. Repeated ornamental or sales-like phrasing warrants a warning; rhetoric that substitutes for mechanism, evidence, or qualification fails the contract.

## Outbound links

In-prose links to the `external` destination are authorized for primary attribution, canonical sources, and material an external reader should be able to inspect directly; they carry no formal identifier. External prospecting is part of article research, not `cp-skill-connect`.

## Types

| type | file | use for |
|---|---|---|
| `article` | `./types/article.md` | outward-facing dated articles distilled from the KB |

## What does NOT belong here

- Transferable claims and theory → `kb/notes/`
- Shipped-system description → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- In-flight exploration → `kb/work/`
- Article drafts → `kb/articles/drafts/`
- Captured external material → `kb/sources/`
