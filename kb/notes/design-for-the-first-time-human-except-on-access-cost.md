---
description: "Uses competent-newcomer ergonomics as a property-by-property default, then isolates access paths that charge a consumer for a selected slice or a whole artifact"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Design for the first-time human, except on access cost

A useful starting heuristic for a system an LLM agent consumes is to inspect it
as if a competent human were using it for the first time. Clear names,
discoverable organization, orientation cues, honest labels, and readable prose
can serve both consumers. The heuristic transfers one property at a time. It is
not evidence that the consumers behave alike, and it stops wherever the
operations or needs relevant to that property diverge.

## Access mode, not consumer identity

The cleanest boundary is **access cost**. A selected-slice path identifies and
returns a relevant region before the consumer processes it. A whole-artifact
path admits the entire container to the consumer's working set. This note calls
the resulting consumer cost *sublinear* or *linear* relative to artifact size.
The terms describe material the consumer must process, not the work performed
inside a search engine or index.

A human using headings, scrolling, or find-in-page can attend to a selected
region of a large rendered artifact. An agent given only a whole-file read
loads every returned byte into [bounded
context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md),
where irrelevant material consumes volume and can add interference. Reverse the
interfaces and the ordering can reverse: an agent with a scoped query can load
one slice, while a human facing an unstructured blob may have to inspect the
whole. Consumer identity therefore does not determine access cost; the exposed
path and the comparison currency do.

## One authority can supply different access paths

When consumers have different cheap paths, give each a view or query interface
that selects before it charges that consumer, while retaining one authoritative
source. A human can receive a rendered, browsable view with find-in-page. An
agent can receive a scoped search or query result. These are consumer-specific
materializations of one content authority, not independent copies that may
silently disagree.

A complete reference index, for example, need not sit on an agent's default
read path to earn its keep. It can be generated for human browsing while the
agent reaches the same membership through a scoped query. The useful routing
depends on which access path is available and cheap for the current consumer,
not on choosing one audience as the winner.

## Scope

The comparison must hold the requested information and required reliability
fixed. A smaller slice is not cheaper if it omits context that the task then has
to recover through several reads. Nor can human attention, agent context tokens,
latency, and implementation work be treated as one numerical cost without a
declared conversion.

Access cost is not the only boundary of the newcomer-human heuristic. Loaded
text can act as instruction for an agent because [instructions and content
share one token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md).
An agent may also resolve an underspecified instruction where a maintainer would
ask for clarification. This note isolates access paths because they admit the
structural response above, not because they are the only or most frequent
difference.

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: whole-artifact agent access consumes bounded context, which makes the access-path exception matter
- [Two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — extends: applies the selected-slice/whole-artifact distinction to full-text and index-level collection operations
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](./feasibility-is-the-heaviest-forks-net-load.md) — mechanism: a scoped query reduces the material loaded by the fork whose net load determines feasibility
- [Human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — extends: sharpens one row of the broader comparison into an access-path boundary and a per-consumer materialization response
- [Agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — mechanism: a pointer or query can select a target before the whole artifact enters context
- [LLM contexts interpret instructions and content through the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md) — bounds: access is one difference; loaded text also lacks a program/data boundary in the model's token medium
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — bounds: access is one difference; an agent may also choose an interpretation and proceed under ambiguity
