---
description: The methodology→skill relationship can preserve natural-language form and a live methodology fallback; derivation tracks content dependence, separately from codification or constraining
type: theory/types/structured-claim.md
traits: [has-comparison, title-as-claim]
tags: [method-guided-action, artifact-analysis, learning-theory]
---

# Skills derive from methodology

The [connect skill](../instructions/cp-skill-connect/SKILL.md) asks what a reader gains by following a proposed link. Naming a shared topic is not enough: the writer has to say why one note helps the reader use the other. This resembles the [test for an unstated assumption](./an-assumption-worth-disputing-is-worth-stating.md): both ask the writer to supply a missing reason. The skill gives an agent a decision to make; the methodology explains why the distinction matters.

What is this relationship? The project has two terms for related phenomena — codification and constraining — and neither is quite right. Getting the relationship right matters because it determines how we think about maintaining, improving, and extending skills.

## Evidence

### Derivation alone is not codification

[Codification](./definitions/codification.md) moves a rule or operation from natural-language into symbolic form, where consumers are held to a reference that fixes what it permits. Rewriting instructions as code is one route. Adopting a pinned model package, decoding included, as the reference for an operation is another; the text and physical consumer need not change.

Working methodology into a skill does neither by itself. In the case considered here, both are Markdown interpreted as natural language, and no model package is adopted as their governing reference. What changes is the *rhetorical mode* — discursive, multi-perspective, argumentative reasoning becomes procedural, step-sequenced instruction. The skill remains natural-language under that path. Adopting a model could separately codify its use without changing the derivation relationship.

### Derivation is distinct from constraining

[Constraining](./definitions/constraining.md) commits choices that narrow valid readings or behaviors, or rank the valid ones. A skill can do that as well as make agent behavior more predictable, but neither effect defines its derivation from methodology. Derivation asks where the skill's procedures come from; constraining asks which readings or behaviors the retained choices exclude or rank. You write the skill considered here to supply procedures without their full reasoning overhead.

[Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) already maps the enforcement gradient (instruction → skill → hook → script) as a constraining spectrum. That note is about *how reliably methodology is followed*. This note is about a different question: *what is the relationship between the methodology and the skill's content?*

### It is two-layer derivation in the same medium

The relationship is the one described in [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md), one level down: the methodology KB is the generator layer, and the skill is the fast path worked out from it for a declared consumer — an agent executing a workflow under a context budget. The skill's substantive procedures add no claims the methodology does not already support; what changes is form, order, and operational detail. The reasoning that produced the procedures is not discarded — it stays in the KB — but it is factored out of the operational path.

Key properties:

- **Same substance, different concentration.** Both remain natural language under the consumption path considered here — reorganization for use, not adoption of a semantic reference.
- **The source stays live.** Codification can replace natural-language interpretation for an operation without making its source reasoning obsolete. Here the methodology remains the fallback layer — you return to it when the skill doesn't cover your case. A domain where claim-titles don't work well requires going back to the methodology to reason about what to change.
- **The process requires judgment.** Producing a skill isn't mechanical compilation. A different person reading the same methodology would produce a meaningfully different skill. What to extract, what to leave behind, what sequence to impose on ideas that aren't inherently sequential — these are the region and selection choices of the two-layer structure's coverage bet, and they encode a hypothesis about which cases the skill will actually face.
- **The steps do not determine their rationale.** Someone reading only the `/connect` steps can follow them, but the steps alone need not explain why a particular check matters.
- **Omission keeps the routine case short.** A skill can leave out an argument without making it unavailable. A link from a step to its rationale gives the reader a direct route; search may offer another.


## Reasoning

### Why the distinction matters

The three relationships answer different questions and can coexist:

| Relationship | Operation | What changes | Representational-form transition |
|------|-----------|-------------|-------------------|
| Codification | rewrite into symbolic form or adopt a governing reference | What fixes permitted behavior | Yes — natural-language → symbolic under the path |
| Constraining | commit choices that exclude or rank readings or behaviors | Interpretation space | Not required |
| Skill derivation | discursive → procedural | Rhetorical mode, information density, operational detail | Not required; natural-language is preserved here |

Conflating them produces confused designs. Derivation alone supplies neither a governing semantic reference nor mechanically checkable consequences. Even a codified skill under an adopted model can be opaque, so codification alone would not make it affordable to inspect. If you think only about constraining methodology, you'll focus on excluded behavior rather than on extracting the right procedures. If you recognize the two-layer relationship, you'll focus on the right questions: what to extract, what to leave in the source, and how to maintain the derivation so a methodology revision reaches the skills worked out from it.

### The skill tier is a context-budget artifact

When the full reasoning takes more context than a routine task warrants, a short procedure lets the reader act without loading it all. Keeping the source available serves a different need: deciding what to do when a step does not fit.

This connects to the [loading frequency hierarchy](./instruction-specificity-should-match-loading-frequency.md): CLAUDE.md (always loaded, slim) → skill descriptions (always loaded, suggestive) → skill bodies (loaded on invoke) → methodology notes (loaded on demand). Working the skill tier out from the methodology tier is what produces that hierarchy; the loading order is the architectural consequence.

### Test whether the fallback is usable

Give an agent a case the skill does not cover, without telling it which source to open. Can it recognize the mismatch and find the relevant reasoning before acting? [A fresh session cannot rely on remembering an earlier lookup](./agent-statelessness-makes-routing-architectural-not-learned.md), but a link or a subject search may be enough. If the reader misses the exception, clarify the step’s limits; if it notices the exception but cannot find the source, improve the route.

## Caveats

- **Not all skills are worked out from methodology.** [Cramer's skill synthesis](https://x.com/zeeg/status/2032179291031806408) demonstrates an alternative path: producing skills directly from domain artifacts (commit history, security patches, external standards) without an intermediate theory-building step — from "here are 200 security patches" straight to "here is how to find IDORs." That is a different lineage: the resulting rules generalize beyond the artifacts that prompted them, so the skill is abstracted from its sources, entering the [discovery lifecycle](./definitions/discovery-lifecycle.md) at conjecture and earning authority through use, rather than being checkable against a retained generator. The practical tradeoff follows from the lineage: methodology-sourced skills degrade to "consult the methodology"; artifact-sourced skills degrade to "consult the raw artifacts" — a much harder fallback for an agent.
- **The source is only valuable if maintained.** Methodology notes that drift out of date while skills stay current create a false source — a designer who consults them will reason from outdated premises. This is the two-layer structure's staleness discipline applied at skill scale: a methodology revision makes review of the skills worked out from it due.

---

Relevant Notes:

- [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the general structure this note instantiates one level down — generator layer, fast path, fallback, and the maintenance regimes for worked-out content
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — distinguishes: that note covers enforcement reliability (how reliably is methodology followed); this note covers derivation (how skill content relates to methodology content)
- [codification](./definitions/codification.md) — contrasts: codification changes form under a consumption path, by rewriting or adoption; skill derivation alone does neither
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — enables: the loading hierarchy is the architectural consequence of the skill tier being worked out from the methodology tier
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — example source: one of several methodology notes the /connect skill was worked out from
- [Skill Synthesis (Cramer)](https://x.com/zeeg/status/2032179291031806408) — counterexample: skills produced directly from domain artifacts (commit history, patches) without an intermediate theory layer — abstracted lineage, not derivation from a retained generator

Operationalized into:

- [/connect skill](../instructions/cp-skill-connect/SKILL.md) — this methodology note's procedures are worked into the skill's operational sequence
