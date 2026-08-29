# Writing conventions for kb/reports/

<!--
This is your project's reports collection. Once installed, this contract
belongs to your project; Commonplace does not synchronize it with later
changes to this template. Adapt the generic rules below when the project
needs narrower report policies.
-->

## Purpose and scope

This collection contains analytical outputs, evaluation records, and local
operational evidence consumed as reports rather than as library claims or
system definitions. Placement is decided by retention policy and consumer,
not by the filename or by whether a tool generated the artifact.

Transferable claims belong in `kb/notes/`; shipped-system descriptions and
decisions in `kb/reference/`; procedures in `kb/instructions/`; unfinished
reasoning and run traces in `kb/work/`; and external sources in `kb/sources/`.

## Policy areas

Every report payload lives in exactly one first-level policy area:

| Area | Retention policy |
|---|---|
| `cache/` | Ignored outputs that are safe to delete and regenerate from authoritative inputs. |
| `state/` | Ignored local evidence or state whose owning workflow controls cleanup. |
| `retained/` | Durable report records kept with the project. |
| `types/` | Collection-local structural contracts, not report payloads. |

Do not put report payloads directly at the collection root. Moving a report
between areas changes its retention contract.

## Quality goal

Make the report sufficient for the operation that consumes it without making
it impersonate a durable knowledge claim. State the subject, inputs or source
state, method, result, and material limits to the degree needed to interpret
or reproduce the output. Record model and instruction provenance when an LLM
judgment is part of the evidence and the workflow does not retain it elsewhere.

`cache/` may optimize for cheap regeneration. `state/` follows the producing
workflow's integrity and cleanup rules. `retained/` must be understandable
from a clean checkout without ignored files.

## Titles and descriptions

- Name the analysis, experiment, or result; "Report" alone is not a
  discriminating title.
- When frontmatter is present, use a retrieval-oriented `description` that
  identifies the subject and why the exact output matters.
- Frontmatter-free Markdown is permitted for deliberate unstructured output.
- Preserve exact captures when fidelity is the report's purpose. Mark a copied
  fixture subtree with `.commonplace-validation-ignore` instead of presenting
  a foreign collection's local type as a live report type.

## Maintenance semantics

- Deleting a cache entry must lose no unique evidence, decision, or unresolved
  state. Its authoritative inputs and producing operation remain discoverable.
- Git ignore status never licenses deletion from `state/`; follow the owning
  workflow's completion or retirement rule.
- Correct a living retained report in place. Preserve a dated or frozen
  observation as an exact record and create a new observation when its measured
  state changes.
- Extract any transferable claim, binding rule, system premise, or unfinished
  work lifecycle to its proper collection.

## Outbound links

Reports may inspect any project surface. Use relative Markdown links and state
why the target matters. Inline links may carry ordinary evidential or
procedural context. Footer-shaped formal edges use this authorized set:

| label | destinations | reader need |
|---|---|---|
| `derived-from` | sources, external | inspect the source material from which the report was produced |
| `is-evidence-for` | notes, reference, reports | inspect the durable claim, decision, or report record on which this output bears |
| `compares-with` | notes, reference, sources, reports | compare two artifacts on a named shared axis |
| `see-also` | any durable collection, external | inspect useful adjacent context when no stronger relation applies |

The destination collection separately decides whether it may author a
reciprocal edge. A formal edge into this collection targets `retained/`;
`cache/` and `state/` may be mentioned inline only as local operational
context.

Tracked library artifacts must not depend on an ignored `cache/` or `state/`
file being present. Summarize the evidence in the tracked artifact or promote
the exact report to `retained/` first.

## Type eligibility and validation

A typed report may use a shared type under `kb/types/` or a local type under
`kb/reports/types/`. Frontmatter-free Markdown is implicit `text`.

The `.commonplace-validation-ignore` markers under `cache/` and `state/`
exclude those data-bearing subtrees from collection-scoped validation. They do
not hide files from ordinary discovery, and explicit file validation still
applies a typed report's contract.
