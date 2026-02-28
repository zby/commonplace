---
description: Concrete use cases for the knowledge system — upstream change analysis and proposing our own changes
type: note
traits: []
areas: [claw-design]
status: current
---

# Scenarios

What do we actually use the knowledge system for? Start here, work backward to what's needed.

## Upstream change analysis

1. **Notice** a change — upstream PR, RFC, or our own design idea (e.g. traits API, deferred tool results handler)
2. **Analyze** how it applies to our work — what does it enable, break, or change?
3. **Write comments** — PR reviews, supporting arguments, change requests, questions
4. **Document the comments** — they need to be grounded in evidence, not just opinion

Step 4 is where the knowledge system earns its keep. To write a good comment we need to:
- Scan the relevant code
- Read our existing notes on the affected area
- Find prior decisions that constrain or inform the response

The question for the knowledge system: does it make step 4 faster and better than just reading code and grepping? These scenarios are the concrete evaluation criteria a [KB learning loop](./automating-kb-learning-is-an-open-problem.md) would need to optimise against — but we don't yet have enough logged usage of them to design that loop.

## Proposing our own changes

1. **Have an idea** — a design change, new feature, or architectural improvement
2. **Build the case** — why is this needed? What does it improve? What are the trade-offs?
3. **Write the proposal** — PR description, RFC, or upstream issue
4. **Ground it in evidence** — link to code, prior decisions, and design rationale

Same documentation need as upstream analysis, but the direction is reversed — we're producing the argument instead of responding to one. The knowledge system should help assemble the case: what have we already decided, what constraints exist, what prior art is relevant.

Topics:
- [claw-design](./claw-design.md)
