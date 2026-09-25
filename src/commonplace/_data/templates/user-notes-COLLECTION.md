# Writing conventions for kb/notes/

These defaults are ready to use. Customize them only when the project needs
different conventions; no sections require filling in. Use the project's
declared KB goals and scope to decide which subjects belong here. Do not invent
project requirements to customize this file.

Once installed, this contract belongs to your project. Commonplace does not
synchronize it with later template changes.

## Purpose and scope

This collection retains claims, explanations, definitions, and synthesis that
help readers reason about the project's domain. Keep one main contribution
per note, with enough context to understand it without the conversation that
produced it.

Put descriptions of the project's current state and recorded decisions in
`kb/reference/`, procedures in `kb/instructions/`, external-source analyses in
`kb/sources/`, and unfinished investigations in `kb/work/`.

## Quality goal

A note is worth keeping when it improves a reader's understanding, judgment,
or decisions within the KB's scope. Explain why the claim holds and under
which conditions. Distinguish evidence, inference, and conjecture; state
uncertainty rather than filling gaps with unsupported claims.

## Title and body conventions

- For a claim, use a title that states the claim. For a definition, name the
  term; for a synthesis, name the question or relationship it explains.
- State the main contribution early. Include the reasoning, evidence, and
  limits needed to assess it; omit unrelated material.
- Use plain language and the same term for the same concept. Explain terms
  the intended reader may not know.
- When frontmatter includes a `description`, say what the note establishes
  and when a reader would need it.

## Outbound links

Link when following the target helps a reader understand, verify, or use the
artifact. Put supporting links inline where they matter. Optional footer links
use `- [title](path) — label: specific reason to follow the link`. Do not add
links merely to fill a footer or create a reciprocal link.

Use these destinations and labels for connection discovery and authored links:

| Destination | When to search or link | Authorized labels and meanings |
|---|---|---|
| `kb/notes/` | Find related claims, definitions, and disagreements. | `extends`: develops the target's claim; `contradicts`: disagrees with the target; `defined-in`: explains a term; `see-also`: offers useful adjacent reasoning. |
| `kb/reference/` | Find project facts or decisions bearing on the claim. | `evidenced-by`: supplies evidence for the claim; `see-also`: gives relevant project context. |
| `kb/instructions/` | Find a procedure that helps apply the claim. | `procedure`: gives the how-to. |
| `kb/sources/`, `kb/reports/retained/` | Find source analyses or retained results supporting or limiting the claim. | `evidenced-by`: supplies evidence; `see-also`: gives relevant context. |
| `external` | Cite an identified source or definition. | `evidenced-by`: supplies evidence; `defined-in`: defines a term; `see-also`: gives relevant context. |

Use relative Markdown links for local targets. Link only to existing artifacts.
Do not link to temporary work, ignored snapshots, report caches, or local
report state. Connection discovery does not search the open web; `external`
authorizes links to already identified targets.

A useful note need not have connections to existing notes.

## Type eligibility

A typed artifact in this collection may use a global type, named by its path under the library root such as `type: types/note.md`, or a local type spec under this collection's `types/` directory, named by its path under the KB root such as `type: notes/types/<name>.md`. Frontmatter-free Markdown is implicit `text`.
