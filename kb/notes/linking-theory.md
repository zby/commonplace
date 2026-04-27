---
description: Links are decision points; link quality is the reduction of navigation uncertainty per token of context consumed. Grounds our relationship vocabulary, title-as-claim, and position-encodes-strength practices under one model.
type: kb/types/note.md
tags: [links]
status: seedling
---

# Linking theory

We have link practices — relationship types ([ADR 009](../reference/adr/009-link-relationship-semantics.md)), title-as-claim, context phrases, position conventions — but no theory explaining *why* these practices work and *when* they break down. This note collects the grounding claims and builds toward one.

## Established claims about linking

Seven notes across the KB argue what makes links work. They cluster into three groups.

### Links as navigation decisions

[Agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) models every link encounter as a decision: follow or skip? The decision is always probabilistic — the agent can't know what the target contains until loading it. What makes it tractable is *context*: information surrounding the pointer that hints at what the target contains. The more context a pointer carries, the cheaper the navigation decision.

When the title carries the argument, the pointer itself becomes the hint — every link text, every search result, every index entry does navigation work without additional context. Title-as-claim is the shortcut that works across all pointer types.

[Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) adds the progressive-disclosure constraint: the title layer is the cheapest disclosure layer. If titles are claims, agents decide what to load from the title alone. If titles are topics, agents must load notes to discover what they argue — the disclosure layer fails.

### Links as argument structure

[Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — when titles are claims, following links reads as a reasoning chain. "since [structure enables navigation]" composes grammatically; "since [navigation notes]" doesn't. The note graph becomes scannable arguments. Link semantics ("since", "because", "but") encode relationship types — Toulmin warrants connecting grounds to claims.

[Claim notes should use Toulmin-derived sections for structured argument](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — title-as-claim is the Toulmin claim; "since"/"because" link semantics encode warrants. Not all claim-titled notes need the full Toulmin scaffold, but the scaffold reveals what claim titles are doing implicitly.

[Link strength is encoded in position and prose](./link-strength-is-encoded-in-position-and-prose.md) — an inline "since [X]" that uses a note as a premise carries more weight than a footer entry. Position and prose encode commitment level, creating a weighted graph orthogonal to relationship type.

### Links as maintenance surface

[Title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — claim titles expose what each note commits to, so reviewing the KB becomes scanning hypotheses: "do I still believe this?" Maintenance cost scales with *doubtful claims*, not total notes. Topic titles hide commitments behind labels that require opening every file.

[Title as claim makes overlap between notes visible](./title-as-claim-makes-overlap-between-notes-visible.md) — two claim titles arguing the same thing are obviously redundant at the index level. Two topical titles covering the same territory are invisible until you read both. Overlap detection becomes a scanning task rather than a reading task, and the benefit compounds with KB size.

## Candidate theory: links as decision-cost reducers

The claims above share a common mechanism: **links are decision points, and link quality is the reduction of navigation uncertainty per unit of context consumed.**

Every interaction with the knowledge graph involves a decision under bounded context: follow this link? Load this note? Open this search result? Each decision has a cost — context consumed to make it — and a value — probability of reaching task-relevant information. Link quality is the efficiency of that exchange: how much uncertainty about the target does the link context eliminate, relative to the context budget it consumes?

Each practice instantiates this principle:

- **Typed relationships** (extends, contradicts, grounds) beat "related" because they carry more decision-relevant information per word. "Related" eliminates zero uncertainty about what following the link will do for the reader's task.

- **Claim titles** beat topical titles because they compress the note's commitment into the pointer. A claim title is a one-line summary of what you'll get; a topical title says only what territory you'll enter.

- **Position encodes strength** because inline links pay for their context with the surrounding argument — the prose advances the argument while hinting at the target, making the marginal context cost near zero. Footer links must pay for their context out-of-band.

- **"Related" is not a relationship** — it carries zero bits of decision-relevant information, the linking equivalent of a null description.

### Content registers constrain link direction

The decision-cost model needs one more axis: the content layer of the source and target. [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md) argues that theory, description, and prescription have different quality goals and maintenance directions. Those differences constrain which links are load-bearing.

A theory can cite a description as evidence while remaining generally stated; a description can cite theory as rationale for why the system is shaped that way; a prescription can cite both theory and system description because procedures must be justified and executable against the current system. Reversing those relationships changes the maintenance contract. If a theory depends on a specific description for its formulation, the link reveals that the artifact has not yet been abstracted into theory. If an instruction omits the descriptive system target it acts on, executability suffers.

So relationship vocabulary is not enough by itself. A `grounds` or `rationale` edge has different consequences depending on whether it crosses theory, description, or prescription. Link review should check both the local relationship phrase and the register-crossing contract.

### What the theory predicts

If link quality is decision-cost reduction, the theory predicts:

1. **Vocabulary size is a trade-off.** Too few relationship types and you can't discriminate; too many and authoring cost exceeds the discrimination benefit. Our five types — extends, grounds, contradicts, enables, exemplifies — should be evaluated against common agent tasks.

2. **Different tasks need different link types.** An agent verifying a claim should prioritize "grounds" and "contradicts" links. An agent looking for examples should prioritize "exemplifies". The vocabulary is useful to the extent that agent tasks decompose along the same axes.

3. **Untyped links work in small KBs but fail at scale.** With few notes, every link target is roughly equally likely to be useful — decision cost is low regardless. As the note count grows, untyped links provide no discrimination.

4. **Link density has diminishing returns.** Each additional link adds decision points. If the marginal link carries less decision-relevant information than the context cost of processing it, it hurts navigation rather than helping it.

5. **Maintenance cost scales with exposed commitments.** Popperian maintenance works because claim titles externalize decision-relevant information. Any practice exposing commitments at low context cost — claim titles, typed relationships, context phrases — will reduce maintenance effort.

## Open questions

- **How do relationship type and position interact?** A "contradicts" link in a footer is arguably more important than an "exemplifies" link inline. Do type and position compose additively, or does one dominate?

- **Is the vocabulary the right one?** Our five types were borrowed from arscontexta and adapted. Are there common agent navigation patterns that need a type we don't have? Are there types we never use in practice?

- **Can we measure decision cost?** The theory is only testable if we can observe agents making navigation decisions and measure whether typed links lead to better choices. Agent trace analysis might provide this.

---

Relevant Notes:

- [ADR 009: Link relationship semantics](../reference/adr/009-link-relationship-semantics.md) — decision: the specific vocabulary this theory aims to ground
- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds: the navigation-decision model
- [title-as-claim-enables-traversal-as-reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — grounds: claim titles as argument structure
- [title-as-claim-exposes-commitments-enabling-popperian-maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — grounds: claim titles as maintenance surface
- [title-as-claim-makes-overlap-between-notes-visible](./title-as-claim-makes-overlap-between-notes-visible.md) — grounds: claim titles as redundancy detector
- [link-strength-is-encoded-in-position-and-prose](./link-strength-is-encoded-in-position-and-prose.md) — extends: position as a second axis the theory needs to account for
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — enables: progressive disclosure depends on title-layer quality
