---
description: Closure under its own recommendations — an agent extends a methodology only where it specifies its reason-vs-codify and verification decisions, bounded by verification cost
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining]
status: seedling
---

# A methodology is agent-extensible only where it is closed under its own recommendations

An LLM can consume a theory and act on it, so encoding a good methodology is one way of building capability: point an agent at the methodology and it executes. The stronger move is that the agent can also *extend* the system the methodology governs — writing the code, schema, or validator the methodology calls for. But that self-extension is not free-floating. An agent can extend a methodology autonomously **only where the methodology specifies the decisions its own extension requires**. Call this closure under its own recommendations.

## The condition

Extending a methodology-governed system forces two meta-decisions:

1. **Representational form** — should the next artifact stay prose to be interpreted, or be frozen into deterministic code, schema, or grammar? A methodology is closed on this axis when it hands the agent the criteria to decide, rather than leaving the agent to guess. Commonplace supplies these as the [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) and the [constraining gradient](./methodology-enforcement-is-constraining.md) from convention to code; the decision itself is [codification](./definitions/codification.md).
2. **Verification** — once the artifact exists, how does the agent know it is correct? A methodology is closed on this axis when it tells the agent what oracle to build or invoke.

Where both are specified, the loop closes: the agent reads the methodology, recognizes a case, produces the artifact the methodology prescribes, and verifies it — all without stepping outside the methodology. Where either is missing, the agent must improvise the meta-decision, and improvised meta-decisions are exactly where two sessions diverge — [because natural-language instructions are interpreted, not executed](./agentic-systems-interpret-underspecified-instructions.md).

## Verification is the ceiling, not understanding

Closure makes self-extension *possible*; it does not make it unbounded. The binding constraint is that the agent can produce an artifact only as reliably as it can check that artifact, since [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). A methodology closed on representational form but open on verification will generate artifacts the agent cannot confirm — output, not automation. This reframes what a methodology's verification machinery (typed artifacts, validators, review gates) is *for*: it is not bureaucracy around the knowledge, it is what raises the ceiling on how far an agent can extend the system from the methodology alone.

So the power of an agent-executable methodology is not set by how much the agent understands — understanding is assumed — but by two properties of the methodology itself: how completely it specifies its own extension decisions, and how cheaply the results of those decisions can be verified.

## Why the artifact is retained, not re-derived

Closure explains *how* an agent produces a codified artifact from the methodology; it does not argue the agent should reproduce it each session. A persisted symbolic artifact is deterministic and inspectable in a way a re-derivation is not — re-deriving pays the cost again and risks two interpretations drifting apart. This is the reason an agentic system keeps a knowledge base of committed artifacts rather than a single theory document the agent re-expands on demand: the methodology *generates* the artifact via closure, and the KB *retains* it so nobody re-derives it. In agent systems [the prescription/implementation boundary collapses](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — the prescription and the code it becomes are the same retained thing at different points on the constraining gradient.

## Scope

- **Closure is a direction, not a binary.** No real methodology fully specifies every extension decision it could face; the claim is that agent-autonomy scales with how much it specifies, and stalls at the first meta-decision it leaves open.
- **The counter worth taking seriously.** A capable agent brings general competence and can improvise the reason-vs-codify and verification decisions the methodology omits. Where that improvisation is reliable, closure buys less. The claim's force therefore tracks how *consequential and divergence-prone* the omitted meta-decisions are — high for what-to-codify and how-to-verify, low for cosmetic choices.
- **This is a property of the methodology-as-agent-input, not of any one system.** Commonplace is the worked example, not the claim; the principle should hold for any methodology handed to an agent to execute and extend.
