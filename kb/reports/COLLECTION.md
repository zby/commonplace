---
type: types/collection-contract.md
---

# Writing conventions for kb/reports/ (report collection)

## Purpose and scope

This collection contains analytical outputs, evaluation records, and local
operational evidence that are consumed as reports rather than as library
claims or system definitions. Placement here is justified by the output's
retention policy and consumer, not by its filename or by the fact that a tool
generated it.

A report belongs here only when a named operation consumes the report itself.
Transferable claims belong in `kb/theory/`; descriptions of the shipped system
and its decisions belong in `kb/reference/`; executable procedures belong in
`kb/instructions/`; and reasoning whose value is consumed by unfinished work
belongs in `kb/work/`.

## Policy areas

Every report artifact lives in exactly one first-level policy area:

| Area | Retention policy | Typical contents |
|---|---|---|
| `retained/` | Durable report records kept with the project. Payloads are tracked. | Evaluation corpora, experiment reports, measurements, and exact records cited by later work. |
| `types/` | Collection-local structural contracts, not report payloads. | Optional project-authored report contracts; command-produced generic report types are global. |

The published site includes retained reports. Inside `retained/`, a subtree carrying a
`.commonplace-validation-ignore` marker is left out of the site as well as
validation; mark exact captures and trial bundles so, keeping the report that
interprets them published.

Keep report payloads under `retained/`. Use the [workflow state collection](../workflow-state/COLLECTION.md) for records owned by a workflow.

## Quality goal

Make the report sufficient for the operation that consumes it without making
it impersonate a durable knowledge claim. State the subject, inputs or source
state, method, result, and material limits to the degree needed to interpret
or reproduce the output. Record the model and prompt or instruction identity
when an LLM judgment is part of the evidence and the producing workflow does
not already retain them.

`retained/` must be understandable from a clean checkout without relying on ignored files.

## Titles, descriptions, and exact records

- Use a title that names the analysis, experiment, or result. A title such as
  "Report" does not distinguish the artifact.
- When frontmatter is present, write a retrieval-oriented `description` that
  identifies the subject and why the exact output is retained.
- Frontmatter-free Markdown is permitted for deliberate unstructured output.
- Preserve an exact capture when fidelity is the report's purpose. If a copied
  artifact carries another collection's local type only as captured data, put
  a `.commonplace-validation-ignore` marker at the capture-set root rather than
  presenting that copy as a live typed artifact of this collection.

## Maintenance semantics


- A retained report is changed according to its declared role. Correct a
  living report in place; preserve a dated or frozen observation as an exact
  record and create a new observation when the measured state changes.
- Local evidence notes are the one interpreted form `retained/` keeps as
  durable artifacts: a `types/note.md` artifact whose bounded inference
  concerns only Commonplace's own choices or their measured effects, beside
  the raw records it interprets. Its formal edges use this collection's labels
  below. An inference that keeps a free variable belongs in
  `kb/theory/evidence/`.
- If a report develops a transferable claim, binding rule, system premise, or
  unfinished-work lifecycle, extract that content to its proper collection.
  Do not broaden `retained/` into a second notes, reference, instructions, or
  workshop collection.

## Outbound links

Reports may inspect any project surface. Use relative Markdown links for live
navigation and state in prose why the target matters. Inline links may carry
ordinary evidential or procedural context. Footer-shaped formal edges use this
small authorized set:

| label | destinations | reader need |
|---|---|---|
| `derived-from` | sources, external | inspect the source material from which the report was produced |
| `is-evidence-for` | theory, reference, reports | inspect the durable claim, decision, or report record on which this output bears |
| `compares-with` | theory, reference, sources, reports | compare two artifacts on a named shared axis |
| `see-also` | any durable collection, external | inspect useful adjacent context when no stronger relation applies |

The destination collection separately decides whether it may author a
reciprocal edge. A formal edge into this collection targets `retained/`;
workflow state may be mentioned inline only as local operational context.

Tracked library artifacts must not depend on an ignored workflow state file being
present. Summarize the needed evidence in the tracked artifact or
promote the exact report to `retained/` first. Tracked artifacts may cite a
`retained/` report when the exact record is useful to their reader.

## What does not belong here

- A generated explanation or synthesis whose claim should survive the run →
  `kb/theory/` or `kb/reference/` according to its consumer.
- A procedure named "report" because it produces one → `kb/instructions/`.
- Drafts, deliberation, and run traces consumed by an unfinished investigation
  → `kb/work/`.
- External source captures and their durable analyses → `kb/sources/`.
- Build outputs with no report consumer → their build cache, not `kb/reports/`.
