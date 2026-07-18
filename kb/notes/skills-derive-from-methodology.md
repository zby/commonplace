---
description: The methodology→skill relationship is same-medium derivation, with the methodology retained as live fallback — distinct from codification and constraining
type: ./types/structured-claim.md
traits: [has-comparison, title-as-claim]
tags: []
---

# Skills derive from methodology

Skills in a knowledge base are worked out from the methodology KB. The `/connect` skill encodes procedures — scan descriptions, run the articulation test, check agent traversal value — that were reasoned out across a constellation of methodology notes: the [Toulmin argument structure](./claim-notes-should-use-toulmin-derived-sections-for-structured.md), the [Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) review, the [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) convention, the [link relationship semantics](../reference/adr/009-link-relationship-semantics.md). The skill works because it encodes the right procedures. But it can't explain why those procedures are right, or help adapt them when they don't fit.

What is this relationship? The project has two terms for related phenomena — codification and constraining — and neither is quite right. Getting the relationship right matters because it determines how we think about maintaining, improving, and extending skills.

## Evidence

### It is not codification

[Codification](./definitions/codification.md) in this project means the prompt→code phase transition: natural language instructions becoming executable logic. The medium changes. The consumer changes (LLM → interpreter/runtime). The verification regime changes. It is like a physical phase transition — the nature of the artifact changes dramatically.

The methodology→skill relationship has none of these properties. The input is markdown consumed by an LLM. The output is markdown consumed by an LLM. There is no phase change. What changes is the *rhetorical mode* — discursive, multi-perspective, argumentative reasoning becomes procedural, step-sequenced instruction — but the substance remains natural language processed by the same kind of reader.

### It is not constraining

[Constraining](./definitions/constraining.md) narrows the output distribution through techniques — structured output schemas, few-shot examples, tighter prompts, hooks. A skill probably does produce more predictable agent behavior than dumping fifteen methodology notes into context and saying "figure it out." But narrowing the distribution is a *side effect*, not the defining operation. You don't write a skill in order to constrain the agent; you write it to give the agent the procedures it needs without the reasoning overhead.

[Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) already maps the enforcement gradient (instruction → skill → hook → script) as a constraining spectrum. That note is about *how reliably methodology is followed*. This note is about a different question: *what is the relationship between the methodology and the skill's content?*

### It is two-layer derivation in the same medium

The relationship is the one described in [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md), one level down: the methodology KB is the generator layer, and the skill is the fast path worked out from it for a declared consumer — an agent executing a workflow under a context budget. The skill's substantive procedures add no claims the methodology does not already support; what changes is form, order, and operational detail. The reasoning that produced the procedures is not discarded — it stays in the KB — but it is factored out of the operational path.

Key properties:

- **Same substance, different concentration.** Both are natural language for LLM consumption. No phase change — reorganization for use.
- **The source stays live.** In codification, the "soft" form is superseded. Here the methodology remains the fallback layer — you return to it when the skill doesn't cover your case. A domain where claim-titles don't work well requires going back to the methodology to reason about what to change.
- **The process requires judgment.** Producing a skill isn't mechanical compilation. A different person reading the same methodology would produce a meaningfully different skill. What to extract, what to leave behind, what sequence to impose on ideas that aren't inherently sequential — these are the region and selection choices of the two-layer structure's coverage bet, and they encode a hypothesis about which cases the skill will actually face.
- **The skill can't reconstruct the source.** Someone reading only the `/connect` skill can follow the steps but can't adapt them to novel situations. The reasoning that produced those steps is absent from the output.
- **The loss is deliberate, not accidental.** The [agent-statelessness note](./agent-statelessness-makes-routing-architectural-not-learned.md) identifies "lossy compilation" as creating systematic blind spots — reasoning omitted from a skill is permanently unavailable at runtime, and the agent has no "something feels off" signal when it hits a case where the omitted reasoning would have mattered. The two-layer framing sharpens this: factoring the warrant out of the procedure is the *defining operation*, and the remedy is the structure's fallback path made concrete — provenance links from skill steps back to the methodology that justifies them, so the agent can load the reasoning on demand when the procedure doesn't cover the case.

The word "compilation" — in its original, pre-computing sense of "gathering together from various sources" — fits the gathering aspect. But a compilation (anthology, collected works) preserves its sources relatively intact, and the computing sense implies a phase transition (source code → binary) that doesn't happen here. The agent-statelessness note uses "compiled vs. source" as a productive systems-engineering metaphor, and its substantive arguments stand; this note's framing refines it: same medium, no phase change, deliberate separation rather than mechanical translation.

## Reasoning

### Why the distinction matters

The three relationships describe different operations on the same gradient:

| Relationship | Operation | What changes | Medium transition |
|------|-----------|-------------|-------------------|
| Codification | prompt → code | Verification regime, consumer, executability | Yes — natural language → executable |
| Constraining | wide distribution → narrow | Output predictability | No — same medium, tighter constraints |
| Skill derivation | discursive → procedural | Rhetorical mode, information density | No — same medium, different organization |

Conflating them produces confused designs. If you think skills are codified methodology, you'll expect them to be more verifiable than they are (they're still stochastic). If you think skills are constrained methodology, you'll focus on constraining agent behavior rather than on extracting the right procedures. If you recognize the two-layer relationship, you'll focus on the right questions: what to extract, what to leave in the source, and how to maintain the derivation so a methodology revision reaches the skills worked out from it.

### The skill tier is a context-budget artifact

Since [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md), producing the skill isn't optional — it's driven by context economics. You can't load fifteen methodology notes every session. The skill exists because context is finite and expensive. The methodology must be maintained because the skill can't handle edge cases.

This connects to the [loading frequency hierarchy](./instruction-specificity-should-match-loading-frequency.md): CLAUDE.md (always loaded, slim) → skill descriptions (always loaded, suggestive) → skill bodies (loaded on invoke) → methodology notes (loaded on demand). Working the skill tier out from the methodology tier is what produces that hierarchy; the loading order is the architectural consequence.

### For agents, the two-layer split is permanent infrastructure

For a human, procedures extracted from reasoning are a convenience that can eventually be transcended through understanding. For an LLM agent, the skill and the source must be co-maintained indefinitely because no reader will ever internalize either. The [agent-statelessness note](./agent-statelessness-makes-routing-architectural-not-learned.md) develops this point at length — the relationship is architectural, not pedagogical, precisely because the agent never graduates from needing the loaded context.

## Caveats

- **Not all skills are worked out from methodology.** [Cramer's skill synthesis](https://x.com/zeeg/status/2032179291031806408) demonstrates an alternative path: producing skills directly from domain artifacts (commit history, security patches, external standards) without an intermediate theory-building step — from "here are 200 security patches" straight to "here is how to find IDORs." That is a different lineage: the resulting rules generalize beyond the artifacts that prompted them, so the skill is abstracted from its sources, entering the [discovery lifecycle](./definitions/discovery-lifecycle.md) at conjecture and earning authority through use, rather than being checkable against a retained generator. The practical tradeoff follows from the lineage: methodology-sourced skills degrade to "consult the methodology"; artifact-sourced skills degrade to "consult the raw artifacts" — a much harder fallback for an agent.
- **The source is only valuable if maintained.** Methodology notes that drift out of date while skills stay current create a false source — a designer who consults them will reason from outdated premises. This is the two-layer structure's staleness discipline applied at skill scale: a methodology revision makes review of the skills worked out from it due.

---

Relevant Notes:

- [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the general structure this note instantiates one level down — generator layer, fast path, fallback, and the maintenance regimes for worked-out content
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — distinguishes: that note covers enforcement reliability (how reliably is methodology followed); this note covers derivation (how skill content relates to methodology content)
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — refines: that note's substantive arguments (permanent infrastructure, systematic blind spots, no graceful degradation) stand; this note gives the methodology→skill relationship its two-layer reading
- [codification: the missing middle](./deploy-time-learning-is-the-missing-middle.md) — distinguishes: codification involves a phase transition in medium; skill derivation does not
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — enables: the loading hierarchy is the architectural consequence of the skill tier being worked out from the methodology tier
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — example source: one of several methodology notes the /connect skill was worked out from
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured.md) — example source: the Toulmin structure became the skill's articulation test
- [Toulmin Argument (Purdue OWL)](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html) — source: the formal argumentation framework referenced as methodology input to the /connect skill
- [Skill Synthesis (Cramer)](https://x.com/zeeg/status/2032179291031806408) — counterexample: skills produced directly from domain artifacts (commit history, patches) without an intermediate theory layer — abstracted lineage, not derivation from a retained generator

Operationalized into:

- [/connect skill](../instructions/cp-skill-connect/SKILL.md) — this methodology note's procedures are worked into the skill's operational sequence
