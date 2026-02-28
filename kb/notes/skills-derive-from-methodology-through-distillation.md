---
description: The methodology→skill relationship is distillation (extracting operational procedures from discursive reasoning in the same medium) — distinct from crystallisation (prompt→code phase transition) and stabilisation (narrowing output distribution)
type: structured-claim
traits: [has-comparison]
areas: [claw-design]
status: seedling
---

# Skills derive from methodology through distillation

Skills in a claw are derived from the methodology KB. The `/connect` skill encodes procedures — scan descriptions, run the articulation test, check agent traversal value — that were reasoned out across a constellation of methodology notes: the [Toulmin argument structure](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md), the [Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) review, the [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) convention, the [link contracts framework](./link-contracts-framework.md). The skill works because it encodes the right procedures. But it can't explain why those procedures are right, or help adapt them when they don't fit.

What is this derivation relationship? The project already has two terms for related phenomena — crystallisation and stabilisation — but neither is quite right. Getting the term right matters because it determines how we think about maintaining, improving, and extending skills.

## Evidence

### It is not crystallisation

[Crystallisation](../notes/deploy-time-learning-the-missing-middle.md) in this project means the prompt→code phase transition: natural language instructions becoming executable logic. The medium changes. The consumer changes (LLM → interpreter/runtime). The verification regime changes. It is like a physical phase transition — the nature of the artifact changes dramatically.

The methodology→skill relationship has none of these properties. The input is markdown consumed by an LLM. The output is markdown consumed by an LLM. There is no phase change. What changes is the *rhetorical mode* — discursive, multi-perspective, argumentative reasoning becomes procedural, step-sequenced instruction — but the substance remains natural language processed by the same kind of reader.

### It is not stabilisation

[Stabilisation](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) narrows the output distribution through techniques — structured output schemas, few-shot examples, tighter prompts, hooks. A skill probably does produce more predictable agent behavior than dumping fifteen methodology notes into context and saying "figure it out." But narrowing the distribution is a *side effect*, not the defining operation. You don't write a skill in order to constrain the agent; you write it to give the agent the procedures it needs without the reasoning overhead.

[Methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) already maps the enforcement gradient (instruction → skill → hook → script) as a stabilisation spectrum. That note is about *how reliably methodology is followed*. This note is about a different question: *what is the relationship between the methodology and the skill's content?*

### Distillation fits

Distillation in the original chemical sense: heat a mixture, the volatile components evaporate, condense them separately. What you get is purer — the essential substance separated from everything else. The residue isn't waste; it's just not what you needed for this purpose.

The methodology KB is the mixture — arguments, counterarguments, examples, historical context, tensions, worked-through reasoning, wrong turns. The skill is the distillate — the operational procedures extracted from all that reasoning. The residue is the argumentative context that produced those procedures. It isn't discarded (it stays in the KB) but it's factored out of the operational path.

Key properties that map well:

- **Same substance, different concentration.** Both are natural language for LLM consumption. No phase change. Just purification.
- **The residue has value.** In crystallisation, the "soft" form is superseded. In distillation, the source material remains useful — you return to it when the distillate doesn't cover your case. A domain where claim-titles don't work well requires going back to the methodology to reason about what to change.
- **The process requires judgment.** Distillation isn't mechanical compilation. A different person reading the same methodology would distil a meaningfully different skill. What to extract, what to leave behind, what sequence to impose on ideas that aren't inherently sequential — these are design decisions.
- **The distillate can't reconstruct the source.** Someone reading only the `/connect` skill can follow the steps but can't adapt them to novel situations. The reasoning that produced those steps is absent from the output.
- **The loss is deliberate, not accidental.** The [agent-statelessness note](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) identifies "lossy compilation" as creating systematic blind spots — reasoning omitted from a skill is permanently unavailable at runtime, and the agent has no "something feels off" signal when it hits a case where the omitted reasoning would have mattered. Reframed as distillation, this sharpens: the separation of reasoning from procedure isn't an unfortunate side effect of compression. It's the *defining operation*. You deliberately factor out the warrant and keep the procedure. This points toward a remedy the compilation framing doesn't suggest: provenance links from skill steps back to the methodology that justifies them, so the agent can load the reasoning on demand when the procedure doesn't cover the case.

The word "compilation" — in its original, pre-computing sense of "gathering together from various sources" — also fits the gathering aspect. But it misses the purification aspect: a compilation (anthology, collected works) preserves its sources relatively intact. Distillation transforms them. The agent-statelessness note uses "compiled vs. source" as a productive systems-engineering metaphor, and its substantive arguments stand. But "compilation" implies a phase transition (source code → binary) that doesn't happen here. Distillation refines the metaphor: same medium, no phase change, deliberate separation rather than mechanical translation.

### The ML resonance is useful but inexact

Knowledge distillation in ML means training a smaller model to reproduce the behavior of a larger one. The student handles common cases efficiently but can't do everything the teacher can. Structurally similar: the skill (small, cheap to load) reproduces the *behavior* the full methodology KB (large, expensive to load) would produce, for common cases. Edge cases still need the teacher.

But ML distillation is a one-shot training process. Claw distillation is ongoing — the methodology evolves, and skills must evolve with it. The relationship is maintained, not frozen.

## Reasoning

### Why the distinction matters

The three terms — crystallisation, stabilisation, distillation — describe different operations on the same gradient:

| Term | Operation | What changes | Medium transition |
|------|-----------|-------------|-------------------|
| Crystallisation | prompt → code | Verification regime, consumer, executability | Yes — natural language → executable |
| Stabilisation | wide distribution → narrow | Output predictability | No — same medium, tighter constraints |
| Distillation | discursive → procedural | Rhetorical mode, information density | No — same medium, different organization |

Conflating them produces confused designs. If you think skills are crystallised methodology, you'll expect them to be more verifiable than they are (they're still stochastic). If you think skills are stabilised methodology, you'll focus on constraining agent behavior rather than on extracting the right procedures. If you recognise skills as distilled methodology, you'll focus on the right questions: what to extract, what to leave in the source, how to maintain the derivation relationship.

### Distillation is a context-budget operation

Since [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md), the distillation isn't optional — it's driven by context economics. You can't load fifteen methodology notes every session. The skill exists because context is finite and expensive. The methodology must be maintained because the skill can't handle edge cases.

This connects to the [context-loading strategy](./context-loading-strategy.md): CLAUDE.md (always loaded, slim) → skill descriptions (always loaded, suggestive) → skill bodies (loaded on invoke) → methodology notes (loaded on demand). Distillation is the process that produces the skill tier from the methodology tier. The loading hierarchy is the architectural consequence.

### For agents, distillation is permanent infrastructure

For a human, distilled procedures are a convenience that can eventually be transcended through understanding. For an LLM agent, the distillate and the source must be co-maintained indefinitely because no reader will ever internalize either. The [agent-statelessness note](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) develops this point at length — the relationship is architectural, not pedagogical, precisely because the agent never graduates from needing the loaded context.

## Caveats

- **The term may be imperfect.** Chemical distillation separates components of a mixture; what's happening here is more like extracting implications from reasoning. The metaphor captures purification-without-phase-change, but breaks if pushed to "what are the volatile vs. non-volatile components?"
- **Not all skills are distilled from methodology.** Some encode procedures that were never reasoned out discursively — they were designed directly as operational instructions. Distillation describes a *derivation relationship*, not a universal property of skills.
- **The residue is only valuable if maintained.** Methodology notes that drift out of date while skills stay current create a false source — a designer who consults them will reason from outdated premises. The distillation metaphor doesn't inherently address this maintenance burden.

---

Relevant Notes:
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — distinguishes: that note covers enforcement reliability (how reliably is methodology followed); this note covers derivation (how skill content relates to methodology content)
- [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — refines: that note's substantive arguments (permanent infrastructure, systematic blind spots, no graceful degradation) stand; this note offers "distillation" as a more precise term for the methodology→skill relationship it calls "compilation"
- [crystallisation: the missing middle](../notes/deploy-time-learning-the-missing-middle.md) — distinguishes: crystallisation involves a phase transition in medium; distillation does not
- [context-loading strategy](./context-loading-strategy.md) — enables: the loading hierarchy is the architectural consequence of distillation; skill tier exists because methodology tier is too expensive to load routinely
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — example source: one of several methodology notes that the /connect skill distils
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — example source: Toulmin structure is distilled into the skill's articulation test

Topics:
- [claw-design](./claw-design.md)
