---
description: "AI Fluency explainer mapping operator competence beyond prompts onto delegation, description, discernment, and diligence for agent work."
source_snapshot: "shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.md"
ingested: "2026-06-22"
type: kb/sources/types/ingest-report.md
source_type: conceptual-essay
domains: [ai-fluency, context-engineering, orchestration, verification]
---

# Ingest: AI Agents: Four Skills More Important Than a Good Prompt

Source: [shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.md](./shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.md)
Captured: 2026-06-22
From: https://mezha.ua/articles/shi-agenti-chotiri-navichki-yaki-vazhlivishi-za-dobriy-prompt-311970/

## Classification

Type: conceptual-essay -- the article explains and adapts the AI Fluency framework for agent users. It offers vocabulary and a practice frame rather than reporting an original experiment, a shipped system, or a specific implementation.
Domains: ai-fluency, context-engineering, orchestration, verification
Author: Kyrylo Balalin, writing for Mezha. The source is a practitioner-facing explainer based on Rick Dakan and Joseph Feller's AI Fluency framework and Anthropic Academy materials, not a primary framework paper.

## Summary

The article argues that prompt engineering is only one slice of competent AI-agent use. It presents AI Fluency as four simultaneous operator skills: Delegation (choosing what to hand to the model), Description (describing product, process, and behavior), Discernment (checking product, process, and behavior), and Diligence (responsibility, ethics, transparency, and accountability). It distinguishes automation, augmentation, and agency as interaction modes that load those skills differently, with agency putting the heaviest burden on diligence and continuous monitoring. The most KB-relevant move is the shift from "good prompt" to a broader operator loop: choose the right task, describe it through the right durable surfaces, inspect both output and process, and accept responsibility for the result. For this KB, Delegation also needs a second reading: in an orchestrated system, delegation is a scheduling and frontloading strategy, not only a user's decision to assign work to an agent.

## Connections Found

The companion connect report found the article fits the KB as an operator-facing vocabulary layer over existing mechanisms. It connects most strongly to [agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md), because product/process/performance Description is a practical decomposition of narrowing the model's interpretation space. It also supports [instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md): durable descriptions for repeated work belong in prompts, project instructions, skills, and AGENTS/CLAUDE surfaces rather than in one prompt. Its Automation/Augmentation/Agency split corroborates [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), because higher autonomy raises the verification and audit burden. The delegation nuance adds a synthesis connection to [frontloading spares execution context](../notes/frontloading-spares-execution-context.md), [symbolic scheduling over bounded LLM calls](../notes/bounded-context-orchestration-model.md), and [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../notes/feasibility-is-the-heaviest-forks-net-load.md): delegation can move work up to a parent/scheduler, across to siblings, or down to a child as a residual task. Source-to-source comparisons point to [Professional Software Developers Don't Vibe, They Control](./professional-software-developers-dont-vibe-they-control.ingest.md), [Lessons from Building AI Agents for Financial Services](./lessons-from-building-ai-agents-for-financial-services.ingest.md), [Harness Engineering](./harness-engineering-leveraging-codex-agent-first-world.ingest.md), and [Components of A Coding Agent](./components-of-a-coding-agent-raschka.ingest.md): all move the center of gravity away from prompt wording toward task selection, context, skills, control surfaces, and verification.

## Extractable Value

1. **Operator fluency as the human-side complement to context engineering** -- Existing KB notes mostly describe system-side mechanisms: routing, loading, scoping, constraining, and verification. The four Ds add a compact operator-side layer: Delegation selects the right task and mode, Description narrows interpretation, Discernment checks product/process/behavior, and Diligence assigns responsibility. This framing is new relative to the connection set even though each mechanism already has a KB home, but the eventual note should not reduce delegation to operator choice alone. [deep-dive]

2. **Delegation is overloaded between operator skill and orchestration strategy** -- In AI Fluency, Delegation is the operator's decision about what to give the model and in what mode. In Commonplace's orchestration vocabulary, delegation is also a scheduler/frontloading move: decide which work the parent or symbolic system performs, which work siblings perform, and what residual prompt a child receives. This connects the source to frontloading and bounded-context scheduling rather than only user training. [quick-win]

3. **Product/process/performance Description as a usable taxonomy for instruction surfaces** -- The source gives a clean way to explain why "prompt engineering" is too narrow: product description often lives in the immediate request, process description may live in skills or task instructions, and performance description may live in AGENTS.md/CLAUDE.md or system/project instructions. This is a quick way to operationalize [instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md) for users. [quick-win]

4. **Discernment should check process and behavior, not just output** -- The source makes a useful distinction between product discernment (is the result right?), process discernment (did the model follow the intended route and evidence requirements?), and performance discernment (did it behave with appropriate uncertainty and attention?). This strengthens the KB's verification vocabulary for agent work, especially where the output looks polished but the process was not faithful. [experiment]

5. **Agency changes discernment from proofreading into audit** -- In the source's mode taxonomy, automation can often be checked once, augmentation requires iterative checking, and agency requires monitoring a chain of actions. This is a concrete operator-facing version of the automation/verification boundary: autonomy raises verification continuity, not just verification strictness. [quick-win]

6. **Diligence-first as step zero before delegation** -- The article argues beginners may need to establish boundaries, values, data constraints, and quality criteria before deciding what to delegate. The KB has strong machinery for authority, verification, and context, but less explicit user-facing guidance that responsibility boundaries should precede task delegation. [experiment]

7. **"Intent engineering" is a vocabulary gap, not yet a claim** -- The source ends by contrasting context engineering ("what the agent knows") with intent engineering ("the right desires"). This may be useful local vocabulary later, but the article only teases it. Treat it as a candidate term to define or reject after a stronger source appears. [just-a-reference]

## Limitations (our opinion)

This is a secondary conceptual explainer, so it should not carry the same weight as the AI Fluency source materials, an empirical study, or a production build report. It adapts the framework into a media article and gives plausible examples, but it does not test whether the four Ds improve outcomes or whether users can reliably learn them. The "AI Fluency Index" and "only about 30% of conversations" statistic appears in the article without enough local methodological detail to use as evidence.

The essay is also translated from Ukrainian into English for this corpus. The original snapshot is preserved at [shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.md](./shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.md), but subtle wording around `Discernment`, `Diligence`, and "intent engineering" may carry translation loss. Use the translation for routing and analysis, but check the original or primary AI Fluency materials before promoting exact terminology.

Finally, the framework is broad enough to risk becoming a checklist rather than an explanation. The article itself warns against that, but any promoted note should map the four Ds to local mechanisms and failure modes rather than merely adopting the named taxonomy. In particular, it should separate the source's operator-level use of Delegation from the KB's orchestration-level use of delegation as task splitting, sub-agent handoff, and frontloading.

## Recommended Next Action

Write a note titled "Operator fluency complements context engineering" that maps Delegation, Description, Discernment, and Diligence onto existing KB mechanisms: task/mode selection, underspecification management, verification/oracle strength, instruction-surface placement, and responsibility boundaries. Include a section that explicitly separates operator delegation from orchestration delegation/frontloading: humans choose what work should be assigned, while schedulers and parent agents decide where derivation should happen and what residual task a child call receives. Keep it as a synthesis note grounded in this source plus [Professional Software Developers Don't Vibe, They Control](./professional-software-developers-dont-vibe-they-control.ingest.md), [Harness Engineering](./harness-engineering-leveraging-codex-agent-first-world.ingest.md), and the frontloading/orchestration notes, not as an adoption of the AI Fluency framework wholesale.
