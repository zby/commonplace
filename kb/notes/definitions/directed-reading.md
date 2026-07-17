---
description: "Definition - directed reading is reading selected material through an explicit task lens to produce a lens-shaped artifact or judgment"
type: kb/types/definition.md
tags: [computational-model]
---

# Directed reading

Workshop usage has treated "directed reading" loosely as reading material for a purpose. This definition sharpens the term to the three-condition case: reading selected material through an explicit task lens to produce a lens-shaped artifact or judgment.

The term names a consumption pattern: the reader is not asked to absorb a source generally, but to attend to the parts that matter for a stated question, frame, comparison, extraction goal, or output contract.

The output may be a report, review, synthesis, candidate-link list, limitation analysis, recommendation, or inline answer. What makes the reading directed is that the lens determines what counts as relevant and what shape the result should take.

## Scope

Use the term directed reading when all three conditions hold:

- selected material is named or bounded before the main reading pass;
- a lens states what the reader is trying to see in that material;
- the result is shaped by that lens rather than by the source's native structure alone.

A stabilising behavioural check confirms the three conditions: would the lens actually change the reading path? A real directed-reading lens determines what the reader can ignore, what counts as evidence, and what shape the answer must take. If the same output would be produced by reading the source in its native order and summarising the visible points, the task is probably ordinary reading, summarisation, or synthesis rather than directed reading in the technical sense. The term sits close enough to those activities that it loses discriminatory power without this check.

Common KB instances include source ingestion, connection discovery, code-grounded reviews, review-gate evaluation, literature synthesis, and one-off instruction notes that tell a sub-agent which documents to read and what to produce.

Directed reading can be stable or ad hoc. Stable directed-reading contracts have reusable lenses and output contracts, so they belong in skills, type specs, generated prompts, or other system-definition artifacts. Ad hoc directed reading supplies the lens at runtime, often through a frontloaded instruction note that lets a clean-context sub-agent execute without rediscovering source selection, relevance, or output shape.

## Exclusions

Directed reading is not ordinary reading, browsing, or retrieval. Finding material may precede it, but the term applies to the lens-shaped reading pass, not to source discovery by itself.

Directed reading is not all summarization. A summary may preserve the source's own structure; directed reading selects and organizes according to an external task lens.

Directed reading is not automatically promotion into durable KB content. The result can remain an advisory report, temporary work artifact, or inline judgment unless a later step gives it stronger authority.

Directed reading is not the same as frontloading. Frontloading prepares context before a bounded call; directed reading is one task that often benefits from frontloading.

Directed reading is not directed editing. Directed-editing workflows also read through a lens, but their output authority includes mutating the target artifact or another library artifact. They belong nearby conceptually, but this term is reserved for the lens-shaped reading pass and its report or judgment.

## Misuse Cases

- Calling any request to "read this" directed reading when no lens and lens-shaped output are supplied.
- Treating the source's table of contents as the lens. The lens must come from the task, KB frame, or output contract.
- Using a stable skill contract and also writing a one-off instruction note that merely restates the same procedure.
- Letting a directed-reading report silently become committed KB state without an explicit promotion or editing step.

## Relationship to use-shaped production

Directed reading is often the input-side phase of producing a use-shaped artifact: selected material is consumed under a task lens before being reshaped for a downstream consumer. This overlap is strong enough that the notions should not be used as rivals. If the only important fact is that recorded material was reshaped for a downstream consumer, plain language — summarized, condensed, worked out from — suffices.

Keep the term directed reading only when the reading contract matters independently: the source bounds, lens, relevance rules, or output contract need to be discussed before the resulting artifact exists. A review pass that reads a pull request through a safety lens and returns "ship / do not ship" is directed reading that produces no reshaped artifact. Reworking workshop material already understood by the author into a durable note can be reshaping without a distinct directed-reading pass.

## Relationship to context engineering

[Context engineering](./context-engineering.md) decides what knowledge reaches a bounded call and how it is framed. Directed reading fits that architecture as a consumption-side pattern: a caller or system bounds the material, supplies a lens, and asks the reader to spend context on the semantic work that remains.

[Frontloading](../frontloading-spares-execution-context.md) is the usual preparation technique. It resolves paths, source selection, relevant context, and output shape before the reader starts. This is especially useful for sub-agent handoffs, where an instruction note can define the clean context boundary.

## Status

This note is a seedling and may turn out to be redundant. The `## Relationship to use-shaped production` section narrows directed reading to the input-side phase of producing a use-shaped artifact and keeps the term only when the reading contract matters independently of the resulting artifact. If the independent-reading-contract case turns out to be rare, retire this note in favour of plain reading-and-reshaping language.

---

Relevant Notes:

- [context engineering](./context-engineering.md) - architectural frame: directed reading is a bounded-context consumption pattern
- [frontloading spares execution context](../frontloading-spares-execution-context.md) - mechanism: pre-resolving paths, lens, context, and output shape keeps the reading pass focused
- [ad hoc prompts extend the system without schema changes](../ad-hoc-prompts-extend-the-system-without-schema-changes.md) - application: one-off directed-reading prompts carry task-specific judgment without adding schema
