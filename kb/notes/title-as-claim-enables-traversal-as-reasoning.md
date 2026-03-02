---
description: When note titles are claims rather than topics, following links between them reads as a chain of reasoning — the file tree becomes a scan of arguments, and link semantics (since, because, but) encode relationship types
type: note
traits: [has-external-sources]
areas: [document-system, links]
status: seedling
---

# Title as claim enables traversal as reasoning

Don't name notes like topics ("thoughts on memory"). Name them like claims ("structure enables navigation without reading everything").

When you link to a claim-titled note, the link becomes part of your argument:

> "because [approvals guard against LLM mistakes not active attacks](../notes/approvals-guard-against-llm-mistakes-not-active-attacks.md), we can separate the security boundary from the approval UX"

The title IS the reasoning. Traversal IS thinking. The title functions as a typed signature — you know what you're getting before you load the full note. A topic label like "memory notes" is an undocumented function; a claim like "structure enables navigation" tells you the return value. This connects to how [types applied to documents mark affordances](../notes/instructions-are-typed-callables.md) — a claim title is an affordance declaration.

## Why it works

Inline links carry richer relationship data than metadata fields. The prose surrounding a link encodes WHY the linked note matters here — "because [X]" is a causal claim, "since [Y]" is a foundation claim, "but [Z]" is a tension. Claim-as-title makes these constructions possible, because topic labels don't compose grammatically. You can write "since [claims must be specific enough to be wrong]" but not "since [specificity notes]." The [link contracts framework](./link-contracts-framework.md) formalizes this as a "link intent taxonomy" — argumentative links ("since", "because") and referential links ("see", "as defined in") are different intents that require different anchor context.

Progressive disclosure depends on this. The first disclosure layer is titles. If titles are claims, agents can curate what to load based on what each note argues. If titles are topics, agents must load notes to discover what they argue — the disclosure layer fails. This is why [CLAUDE.md works as a router, not a manual](./context-loading-strategy.md) — the loading hierarchy assumes that titles and descriptions carry enough signal for agents to decide what to load next.

**Practical benefits:**
- scanning file tree = scanning arguments
- following links = following reasoning chains
- the vault becomes readable without opening files

## Where it breaks: multi-claim documents

The pattern works best for ideas that ARE single claims. It breaks for **compositional documents** — specs, frameworks, classification systems — that embody multiple independent design choices.

[Document classification](./document-classification.md) is a clear example. It contains several distinct claims: "types assert structure not subject matter," "status is orthogonal to type," "a document has exactly one base type but zero or more traits," "text is the root type." Each could be a standalone claim note. But no single claim subsumes them all — any attempt produces something so abstract it's useless ("documents should be classified").

The traversal-as-reasoning framing explains why. A claim-titled note can serve as a premise: "since [X], therefore Y." A multi-claim document can't serve as a single premise because it IS multiple premises. When you write "see [document classification](…)," you're not invoking a reasoning step — you're pointing to a reference. The link semantics shift from argumentative ("since," "because") to referential ("see," "as defined in").

| Document kind | Title convention | Link semantics | Role in traversal |
|---|---|---|---|
| Single-claim (insight, rationale) | Claim title | "since [X]", "because [X]" | Premise in reasoning chain |
| Multi-claim (spec, framework) | Topical title | "see [X]", "as defined in [X]" | Reference, not premise |
| Definitional (term pinning) | The term itself | "see [X]", "[X] means..." | Reference, not premise |

**Definitional notes** are a second exception. Notes like [crystallisation](../notes/crystallisation.md), [stabilisation](../notes/stabilisation.md), and [distillation](../notes/distillation.md) pin down how a technical term is used in this project. Their titles are the terms they define — topical by nature. They function as reference entries: you link to them for precision ("as defined in [crystallisation]"), not as premises in reasoning chains. Like specs, they can link TO claim-notes for justification while carrying topical titles themselves.

The two layers coexist. Specs link TO their constituent claim-notes for justification ([document types should be verifiable](./document-types-should-be-verifiable.md) is the rationale extracted from the classification spec). Claim-notes link TO specs as the system they support. But they have different title conventions because they play different roles in traversal.

This maps onto the existing type system: notes with claim titles may be promoted to `type: structured-claim` when the argument matures; `spec`, `index`, and other structural types carry topical titles. The title convention (claim vs topical) is independent of the type — any `note` can use a claim title.

## The shadow side

Not every idea decomposes into a single declarative sentence — some are relational, procedural, emergent, or compositional. When reformulation feels forced, the question is whether the insight isn't ready or the format can't accommodate it. The type system makes this explicit: if you can't write a claim title, the note stays `type: note` with a topical title, and that's fine.

---

Relevant Notes:
- [programming-language types applied to documents mark affordances](../notes/instructions-are-typed-callables.md) — extends: claim titles are affordance declarations, telling you what reasoning operations a note supports
- [document types should be verifiable](./document-types-should-be-verifiable.md) — example: a claim extracted from a multi-claim spec, enabling it to serve as a premise
- [document classification](./document-classification.md) — example: a multi-claim spec that gets a topical title because no single claim subsumes its content
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds: claim titles make the navigation decision cheap by carrying the argument in the pointer itself
- [two kinds of navigation](./two-kinds-of-navigation.md) — extends: claim titles improve both local link-following (inline prose reads as reasoning) and long-range search (titles convey arguments without loading)
- [what works](./what-works.md) — grounded by: the "prose-as-title convention" pattern this note theorizes and shows where it breaks
- [context-loading strategy](./context-loading-strategy.md) — enables: claim titles are what make the first layer of progressive disclosure work in the loading hierarchy
- [link contracts framework](./link-contracts-framework.md) — extends: argumentative vs referential link semantics are a concrete instance of the link intent taxonomy
- [Toulmin argument](../sources/purdue-owl-toulmin-argument.md) — grounds: Toulmin's formal argumentation model (claim/grounds/warrant/qualifier/rebuttal/backing) is the theory behind what this note describes — claim titles are Toulmin claims, and "since"/"because" link semantics encode warrants
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.working.md) — validates from inside: an agent operating in a curated graph describes first-person the qualitative difference between following propositional links ("since [X]") and browsing embedding-based similarity results — the strongest external validation of the claim-as-traversal mechanism

Source:
- Adapted from [arscontexta methodology note](https://github.com/agenticnotetaking/arscontexta) on the same topic, with the multi-claim boundary analysis added

Topics:
- [document-system](./document-system.md)
- [links](./links.md)
