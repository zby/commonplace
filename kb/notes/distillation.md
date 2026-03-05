---
description: Definition — distillation is targeted extraction from a larger body of reasoning into a focused artifact shaped by specific circumstances (use case, context budget, agent) — one of two co-equal learning mechanisms alongside stabilisation, and the dominant one in knowledge work
type: note
traits: []
areas: [learning-theory]
status: current
---

# Distillation

One of two co-equal learning mechanisms in deployed agentic systems, alongside [stabilisation](./stabilisation.md). Distillation is **targeted extraction** — taking a body of reasoning and producing a focused artifact shaped by specific circumstances: a use case, a context budget, an agent.

## Why distillation exists

Different operational contexts need different things from the same body of knowledge. An agent connecting notes needs a step-by-step procedure — not fifteen methodology notes about Toulmin argument structure, link contracts, and title-as-claim conventions. An agent validating notes needs a different extraction from the same methodology. A smaller-context agent needs a more compressed version of either.

[Agent statelessness](./agent-statelessness-makes-routing-architectural-not-learned.md) makes this architectural rather than convenient. Each session starts fresh, so the reasoning that produced a procedure can't be "remembered" — it must either be loaded (expensive) or distilled into something that fits the context budget.

## How distillation works

The rhetorical mode shifts to match the target. The content is selected and compressed to fit the circumstances. What stays constant is the medium — unlike [crystallisation](./crystallisation.md), distillation typically stays in natural language consumed by an LLM.

| Source → Distillate | Rhetorical shift | Target |
|---|---|---|
| Methodology → Skill | Argumentative → procedural | Agents performing a specific workflow |
| Workshop → Note | Exploratory → assertive | Future agents and sessions needing the insight |
| Research → Design principle | Observational → prescriptive | Decision-making in a particular area |

Targeting is itself information loss — selecting what's relevant to one context means discarding what's relevant to others. This is why the source persists: it serves many targets, and each distillation chooses a different subset. Multiple distillations of the same source are normal. Reading only the `/connect` skill, you can connect notes but can't adapt the procedure to a novel situation. The methodology notes handle that.

## The dominant mechanism in knowledge work

Most KB learning is distillation. The typical cycle: explore messily → notice patterns → extract insight → write a note. The resulting note might then get [stabilised](./stabilisation.md) (better description, structured sections, eventually code), but the initial learning act — the one that creates new knowledge — is extraction from a larger body of reasoning.

Stabilisation constrains what already exists. Distillation creates something new from something larger. In a knowledge system, creation matters more than hardening — you need something worth hardening first.

## Relationship to stabilisation

Stabilisation and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not stabilised** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Stabilised** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, crystallised script) |

Stabilisation asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

You can distil without stabilising (extract a skill — still natural language, still underspecified). You can stabilise without distilling (store an LLM output — no extraction from reasoning involved). The full compound gain comes when both apply.

Not distillation: moving a validation check to code (crystallisation — the operation is commitment, not extraction); storing an LLM output (stabilisation — commitment, no extraction from reasoning).

---

Relevant Notes:
- [stabilisation](./stabilisation.md) — co-equal mechanism: constraining the interpretation space, orthogonal to distillation
- [crystallisation](./crystallisation.md) — the far end of stabilisation; sometimes follows distillation (extract a procedure, then crystallise it to code)
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as the mechanism behind skill creation
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — why distillation is architecturally necessary: context budget constraints
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the substrate (repo artifacts) through which distillation operates
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: capacity decomposes into generality vs reliability+speed+cost; distillation trades source completeness for operational efficiency
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — grounds: reframes distillation as bounded information extraction; deterministic transformations create information for bounded observers

Topics:
- [learning-theory](./learning-theory.md)
