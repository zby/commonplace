---
description: Since agents can't carry vocabulary or decisions between reads, the harness should auto-inject referenced context — definitions once per session, ADRs when relevant. The trigger mechanism (type, link semantics, term detection) is an open question; the need follows directly from statelessness.
type: structured-claim
traits: []
areas: [claw-design]
status: speculative
---

# Agent statelessness means the harness should inject context automatically

Since [agents are stateless](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md), they can't carry definitions, decisions, or vocabulary between reads. An agent that reads a note linking to [crystallisation](../notes/crystallisation.md) doesn't know the definition unless it follows the link — at the cost of a tool call, context space, and a decision. The knowledge is in the KB but not in the context window.

The remedy is automatic context injection: when the harness loads a document, it identifies references that the agent will need and injects appropriate content. This extends [document affordances](./document-types-should-be-verifiable.md) from "what operations can I perform on this document" to "what context gets loaded alongside this document."

How the harness identifies what to inject is an open design question. Document type is one signal — a `definition` type could trigger auto-injection. But link semantics (referential vs argumentative), frontmatter metadata, or even term detection in the document text could also serve as triggers. The claim here is about the *need* for injection, not the mechanism.

## Evidence

### Definitions as the first case

Definitions are the cleanest case for auto-injection and motivate a `definition` type:

- **They're small.** Under 200 characters in the description, a few paragraphs in the body. The context cost is low.
- **They're stable.** Definitions change rarely. Once loaded, they remain valid for the session.
- **They're referential, not argumentative.** You don't need to evaluate a definition — you need to have it available. Auto-injection matches the link semantics: "as defined in" doesn't require the agent to decide whether to follow the link.
- **They should be loaded once per session.** A definition doesn't need re-reading. The harness could track which definitions have been injected and skip duplicates — paying the context cost once, not on every reference.

This would make definitions behave like imported constants in a programming language: declared once, available everywhere in scope.

### The `definition` type

For the harness to identify definitions, they need a machine-readable type. The current three definitional notes ([crystallisation](../notes/crystallisation.md), [stabilisation](../notes/stabilisation.md), [distillation](../notes/distillation.md)) are `type: note`. A `type: definition` would:

- Signal the harness to auto-inject on first reference
- Assert checkable structural properties: has examples, has negative examples ("Not X:"), links to sibling definitions, bounded length
- Make the title convention (topical) part of the type contract — definitions are a recognized exception to [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md)
- Prevent unbounded growth — a definition that needs Evidence/Reasoning/Caveats is really a `structured-claim` about the term, not a definition

### Beyond definitions: other candidates for injection

The need for auto-injection isn't limited to definitions. Different kinds of referenced documents would benefit from different injection strategies:

| What to inject | When | Rationale |
|------|-------------------|-----------|
| Definitions | On first reference, once per session | Vocabulary must be present for correct reasoning |
| Area indexes | When entering a topic area | Navigation context reduces dead-end traversals |
| ADRs | When modifying related code | Decisions constrain implementation; must be visible |
| Specs | When implementing related features | Specs define the contract |

Each row is a hypothesis about what context is needed when. The trigger mechanism — type-based, link-semantic, metadata-driven — may differ per case. The harness tests these hypotheses by observing whether auto-injection improves agent outcomes vs. explicit loading.

## Reasoning

The [context-loading strategy](./context-loading-strategy.md) currently describes a static hierarchy: CLAUDE.md (always) → skill descriptions (always) → skill bodies (on invoke) → task-specific docs (on demand). Automatic injection adds a dynamic layer: documents loaded reactively based on what the agent is reading.

This sits between "always loaded" and "on demand" — call it "on reference." The agent doesn't request the definition; the harness provides it. The agent doesn't need to know the definition exists; the injection mechanism ensures it arrives.

The hierarchy becomes:
1. **Always** — CLAUDE.md, skill descriptions
2. **On reference** — definitions (first time), related ADRs, relevant indexes
3. **On invoke** — skill bodies
4. **On demand** — methodology notes, source reviews

## Caveats

**Requires our own harness.** On Claude Code, the agent decides what to read. There's no interception point between "agent sees a link" and "agent follows the link." Auto-injection requires a harness that parses loaded documents, identifies links to typed targets, and injects content before returning the document to the agent. Straightforward to build but impossible on someone else's runtime.

- **Context budget:** Even small definitions add up. With 20 technical terms, auto-injecting all on first reference might cost 4-5K tokens. Is that worth it? Probably yes for definitions (they're the vocabulary), but the budget question sharpens for larger types.
- **Staleness:** If a definition is injected once per session and later updated during the session, the agent has the stale version. Definitions are stable enough that this is unlikely, but ADRs or specs might not be.
- **Granularity:** Should the harness inject the full definition note or just the description? For definitions, the description might suffice. For ADRs, you probably want the full decision.
- **Discovery:** Auto-injection helps when the agent reads a document that links to a definition. But what about when the agent writes a response using a term it doesn't link to? That requires term detection, not just link detection — a harder problem.

---

Relevant Notes:
- [document types should be verifiable](./document-types-should-be-verifiable.md) — foundation: types assert checkable structural properties; this note extends affordances from operations to retrieval
- [instructions are typed callables](../notes/instructions-are-typed-callables.md) — parallel: that note gives skills type signatures; this note gives documents retrieval profiles
- [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — motivates: the agent can't remember definitions, so the harness must provide them
- [context-loading strategy](./context-loading-strategy.md) — extends: adds an "on reference" layer between "always loaded" and "on demand"
- [human-LLM differences are load-bearing for knowledge system design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — motivates: the "cannot fill gaps" row in the dual-audience table is exactly the problem context injection addresses; tier separation handles the writing side, injection handles the loading side
- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — context: definitional notes are an identified exception to claim titles; the `definition` type would formalize this

Topics:
- [claw-design](./claw-design.md)
