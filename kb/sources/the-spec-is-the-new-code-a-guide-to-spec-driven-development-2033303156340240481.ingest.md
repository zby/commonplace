---
description: MercadoLibre engineering lead's practitioner guide to Spec Driven Development — the spec/plan/task/implement cascade as methodology for eliminating agent ambiguity, with ecosystem convergence evidence and maturity-level progression
source_snapshot: the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.md
ingested: 2026-03-16
type: practitioner-report
domains: [spec-driven-development, agent-architecture, context-engineering, constraining]
---

# Ingest: The Spec Is the New Code — A Guide to Spec Driven Development

Source: the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.md
Captured: 2026-03-16
From: https://x.com/juliandeangeIis/status/2033303156340240481

## Classification

Type: practitioner-report — DeAngelis describes a methodology MercadoLibre is rolling out to ~20,000 developers, grounded in hands-on workshops and a concrete four-step process. Not purely conceptual: there's a real deployment at scale, though the post focuses on methodology rather than empirical results.

Domains: spec-driven-development, agent-architecture, context-engineering, constraining

Author: @juliandeangeIis — engineering lead at MercadoLibre (Latin America's largest e-commerce platform). Credibility comes from deploying SDD to a 20,000-developer organization with 5,000+ workshop attendees. This is practice at unusual scale, not theory.

## Summary

DeAngelis argues that AI coding agents fail primarily because of ambiguous instructions, not model limitations. His solution is Spec Driven Development (SDD): a four-step methodology — specify (functional requirements), plan (technical decisions), decompose (ordered tasks), implement (one task at a time per agent session). The post documents ecosystem convergence on this pattern (GitHub Spec Kit at 77k stars, OpenAI Symphony, Claude Code's Plan Mode) and introduces a three-level maturity model: Spec-First (write and discard), Spec-Anchored (spec lives in the repo), and Spec-as-Source (spec is the primary artifact, code is regenerated to match). Key design choice: the functional spec is deliberately technology-agnostic, separating "what" from "how" to reduce LLM uncertainty. DeAngelis acknowledges SDD's tradeoffs — 2-3x token cost, learning curve, overhead for small changes — and reports that hands-on workshops, not explanations, drive adoption at MercadoLibre.

## Connections Found

The `/connect` discovery found 6 strong and 8 moderate connections, forming a dense cluster around the KB's underspecification-constraining-context-engineering core.

**Strong connections:**

- [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) (grounds) — SDD's "ambiguity problem" IS the KB's underspecification framework in practitioner language. "The biggest bottleneck isn't the model... it's the human giving the instructions" is the underspecification thesis stated as methodology.

- [constraining](../notes/constraining.md) (exemplifies) — The spec/plan/task/implement cascade is a progressive constraining pipeline. Each step trades generality for reliability: functional spec narrows behavior, plan commits architecture, task breakdown commits execution units.

- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) (exemplifies) — The backoffice example (idempotency, authorization, which backoffice?) is a textbook disambiguation failure, not a changing requirement. SDD addresses this by specifying requirements before coding.

- [what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md](./what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) (contradicts/extends) — The direct counterargument. Augment argues SDD fails without bidirectional spec maintenance because specs decay. DeAngelis acknowledges 2-3x token cost but doesn't address the maintenance problem. Together they form the key tension: upfront specification vs spec-as-living-document.

- [deploy-time-learning-is-agile-for-human-ai-systems](../notes/deploy-time-learning-is-agile-for-human-ai-systems.md) (extends) — SDD's maturity levels (Spec-First -> Spec-Anchored -> Spec-as-Source) trace the waterfall -> agile -> deploy-time learning trajectory. Spec-as-Source — where the spec is the primary artifact and code is regenerated to match — is exactly the deploy-time learning position that "some prose should remain permanently load-bearing."

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (exemplifies) — The source explicitly states: "you're engineering its entire context window in one shot." This is independent practitioner convergence on context-as-scarce-resource.

**Moderate connections:** specification-level-separation (functional/technical split maps to the spec-level separation framework), decomposition-rules-for-bounded-context-scheduling (task breakdown follows bounded-context scheduling rules), programming-practices-apply-to-prompting (SDD systematizes SE practices for agent instruction), writing-styles-as-underspecification-management (spec format is a prescriptive writing style for maximal constraint), legal-drafting parallel (Given/When/Then is contract-like), and two sources — professional-software-developers-dont-vibe-they-control (empirical backing) and harness-engineering (complementary production evidence).

## Extractable Value

1. **Ecosystem convergence evidence for upfront specification** — GitHub Spec Kit (77k stars), OpenAI Symphony, The Ralph Loop, Plan Mode in Claude Code and Cursor all independently converge on the specify-then-plan-then-implement pattern. This is strong practitioner convergence signal that the KB's underspecification/constraining framework correctly predicts practitioner behavior. High-reach: the convergence pattern is robust across different architectures and philosophies. [quick-win]

2. **The maturity-level progression as a constraining trajectory** — Spec-First (discard after delivery) -> Spec-Anchored (lives in repo) -> Spec-as-Source (primary artifact, code regenerated). This maps directly to the constraining spectrum and the deploy-time learning trajectory. The progression names something the KB theory predicts but hasn't observed in a practitioner-defined framework. High-reach: the progression describes a general pattern for any artifact that starts temporary and becomes load-bearing. [quick-win]

3. **Functional/technical separation as LLM uncertainty reduction** — "Separating functional from technical reduces LLM uncertainty" because mixing "the user can authenticate with Google" with "use NextAuth.js with JWT strategy and store sessions in Redis" forces the agent to juggle two concerns simultaneously. This is a concrete operationalization of specification-level separation. Medium-reach: the claim is plausible but unverified empirically. [just-a-reference]

4. **Given/When/Then as agent-verifiable acceptance criteria** — Acceptance criteria in structured format become both the test plan and the agent's self-verification instrument. The agent can check its own implementation against them. This connects to the verifiability gradient in [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md). Medium-reach: the format is well-established in BDD but its effectiveness for LLM self-verification is undemonstrated. [experiment]

5. **Adoption at scale: workshops over documentation** — "The best way to teach the value of SDD is not to explain it. It's to practice it." 5,000+ developers in hands-on workshops at MercadoLibre. This is rare evidence about how to adopt a methodology in a large engineering organization. Low-reach: highly context-specific to MercadoLibre's culture and scale. [just-a-reference]

6. **Task-level agent agnosticism** — Self-contained tasks with embedded context enable swapping agents mid-project (Claude Code -> Cursor -> Codex) because the spec and plan travel with the task, not with the agent session. This is a concrete architecture for avoiding agent lock-in and enabling parallelism. Medium-reach: depends on task isolation quality. [experiment]

## Curiosity Gate

**What is most surprising?** The 77k stars on GitHub's Spec Kit and the speed of ecosystem convergence. Multiple tools with fundamentally different architectures (autonomous agents, interactive coding assistants, infinite loops) all arriving at the same spec/plan/task pattern independently. This isn't just "best practices propagating" — it suggests the constraining framework genuinely predicts where practitioners end up under selection pressure from agent failure modes.

**What's the simpler account?** The simpler account of SDD is: "write detailed requirements before coding." This is 1970s software engineering (Royce's waterfall paper). The question is whether the spec/plan/task decomposition adds anything beyond what good requirements engineering always provided. DeAngelis's answer is that the agent context window makes this mandatory rather than aspirational — agents cannot ask clarifying questions mid-implementation the way human developers do. This is a hard-to-vary claim: if agents COULD reliably ask clarifying questions, SDD's value proposition weakens significantly.

**Is the central claim hard to vary?** The claim "agents fail because instructions are ambiguous" is hard to vary — changing it to "agents fail because models are weak" produces different predictions (better models would fix the problem, which SDD proponents deny). The claim that SDD's specific four-step process is the right solution is easier to vary — other approaches to reducing ambiguity (bidirectional specs, interactive clarification, test-driven development) could produce similar outcomes. The methodology is one solution to a well-identified problem, not the only solution.

## Limitations (our opinion)

**What is not visible:**

- **No empirical evidence of effectiveness.** The post describes methodology and adoption metrics (5,000 workshop attendees) but offers zero data on outcomes: defect rates, rework cycles, agent success rates, developer satisfaction, or code quality with vs without SDD. The 20,000-developer deployment is impressive scale, but scale of adoption is not evidence of effectiveness. The KB's [professional-developers study](./professional-software-developers-dont-vibe-they-control.ingest.md) provides more empirical grounding for the same thesis.

- **Spec maintenance is not addressed.** This is the Achilles' heel that the [Augment SDD critique](./what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) identifies. DeAngelis's Spec-Anchored and Spec-as-Source levels imply specs must be maintained, but the post offers no mechanism for keeping specs current as code evolves. The tradeoff section acknowledges token cost but not maintenance cost. At MercadoLibre's scale (20,000 developers), spec decay would be a significant problem.

- **Survivorship bias in ecosystem convergence.** The post cites tools that converge on SDD (Spec Kit, Symphony, Ralph Loop) but doesn't mention tools that tried different approaches or abandoned specs. The convergence may be real, but the post doesn't account for alternative explanations: maybe these tools converge because they copy each other's patterns, not because spec-first is independently discovered as optimal.

- **The "2-3x token cost" tradeoff is underexplored.** At MercadoLibre scale, 2-3x token cost across 20,000 developers is a massive infrastructure and cost commitment. The post frames this as an acceptable tradeoff without quantifying what "dramatically better results" means or at what complexity threshold SDD becomes cost-effective vs direct prompting.

- **No failure modes described.** When does SDD fail? What happens when the spec is wrong? When the plan doesn't match the codebase? When task decomposition creates dependencies the agent can't resolve? A methodology guide that describes only the happy path — especially one from someone deploying it at scale — should have encountered and documented failure modes by now.

- **"Spec-as-Source" is aspirational, not demonstrated.** The post acknowledges "we're not fully there yet" for Spec-as-Source, but frames it as the inevitable trajectory. The KB's [constraining](../notes/constraining.md) and [codification](../notes/codification.md) notes suggest this trajectory is more complex than the post implies — full codification requires the spec to be formally verifiable, not just "well-written."

## Recommended Next Action

Write a note titled "Practitioner convergence on upfront specification confirms underspecification as the binding constraint" connecting to [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md), [constraining](../notes/constraining.md), and [deploy-time-learning-is-agile-for-human-ai-systems](../notes/deploy-time-learning-is-agile-for-human-ai-systems.md). The note would argue: multiple independent tools and methodologies (SDD, Spec Kit, Symphony, Plan Mode) converge on the same pattern — specify upfront, plan technically, decompose into bounded tasks — because underspecification is the binding constraint in agent systems. The maturity-level progression (Spec-First -> Spec-Anchored -> Spec-as-Source) maps to the constraining spectrum and predicts the deploy-time learning trajectory. Ground it with the Augment counterargument about spec maintenance as the unsolved lifecycle problem.
