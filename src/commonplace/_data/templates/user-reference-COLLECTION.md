# Writing conventions for kb/reference/

These defaults are ready to use. Customize them only when the project needs
different conventions; no sections require filling in. Use the project's
declared KB goals and scope to decide which subjects belong here. Do not invent
project requirements to customize this file.

Once installed, this contract belongs to your project. Commonplace does not
synchronize it with later template changes.

## Purpose and scope

This collection describes the project's current or recorded past state:
its structure, terminology, interfaces, policies, and decisions. A project
may concern a product, research activity, organization, or other domain;
reference documents describe the particulars readers need to understand it.

Put general claims and explanations in `kb/notes/`, procedures in
`kb/instructions/`, external-source analyses in `kb/sources/`, and unfinished
investigations in `kb/work/`.

## Quality goal

A reference document is worth keeping when it helps a reader understand the
project accurately or find an authoritative fact. Describe what is established
and distinguish it from proposals, assumptions, and unknowns. Verify factual
details against the relevant records or implementation rather than inventing
missing information.

## Title and body conventions

- Use a title naming the specific subject, such as "Document review roles"
  or "Source selection policy".
- State what the document covers at the start. Organize details around the
  questions readers need answered; use tables or lists when they help lookup.
- When describing past state, identify the period or version. Keep current
  descriptions aligned with the facts they describe.
- Link to authoritative detail rather than duplicating it unnecessarily.
- When frontmatter includes a `description`, name the subject and the question
  this document answers.

## Outbound links

Link when following the target helps a reader understand, verify, or use the
artifact. Put supporting links inline where they matter. Optional footer links
use `- [title](path) — label: specific reason to follow the link`. Do not add
links merely to fill a footer or create a reciprocal link.

Use these destinations and labels for connection discovery and authored links:

| Destination | When to search or link | Authorized labels and meanings |
|---|---|---|
| `kb/reference/` | Find the surrounding structure, related descriptions, or definitions. | `part-of`: situates the subject in a larger whole; `contains`: identifies a component; `defined-in`: explains a term; `see-also`: gives related context. |
| `kb/notes/` | Find reasoning behind a described choice or policy. | `rests-on`: identifies a claim the choice depends on; `defined-in`: explains a term; `see-also`: gives related reasoning. |
| `kb/instructions/` | Find how to act on the described subject. | `procedure`: gives the how-to. |
| `kb/sources/`, `kb/reports/retained/` | Find evidence for a factual description or decision. | `evidenced-by`: supports or qualifies the description; `see-also`: gives relevant context. |
| `external` | Cite an identified authoritative record or definition. | `evidenced-by`: supplies evidence; `defined-in`: defines a term; `see-also`: gives relevant context. |

Use relative Markdown links for local targets. Link only to existing artifacts.
Do not link to temporary work, ignored snapshots, report caches, or local
report state. Connection discovery does not search the open web; `external`
authorizes links to already identified targets.

## Type eligibility

A typed artifact in this collection may use a global Commonplace type, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path. Frontmatter-free Markdown is implicit `text`.
