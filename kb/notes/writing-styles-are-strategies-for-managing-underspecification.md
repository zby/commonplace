---
description: The five empirically observed context-file writing styles (descriptive, prescriptive, prohibitive, explanatory, conditional) are not stylistic variation — they correspond to different strategies for narrowing the interpretation space agents face, trading off constraint against generalisability
type: note
traits: [has-external-sources]
areas: [claw-design, computational-model]
status: seedling
---

# Writing styles are strategies for managing underspecification

An [empirical study of AI context files](../sources/context-engineering-ai-agents-oss.md) across 466 open-source projects identified five writing styles in convention sections: descriptive, prescriptive, prohibitive, explanatory, and conditional. The authors frame these as stylistic variation. But viewed through the [underspecification lens](./agentic-systems-interpret-underspecified-instructions.md), each style is a different strategy for narrowing the space of valid interpretations an agent can select from — and the choice of style encodes how much autonomy the author wants the agent to have for that particular instruction.

## The five styles as constraint strategies

**Prescriptive** — "Follow the existing code style and conventions." Direct imperatives that select a specific interpretation. This is maximal narrowing: the agent's job is compliance, not judgment. Best for instructions where any deviation is a bug.

**Prohibitive** — "Never commit directly to the main branch." Eliminates specific interpretations from the space without prescribing what to do instead. The agent retains autonomy within the remaining space. Prohibitions are cheaper than prescriptions because they constrain without over-specifying — you can forbid a few bad outcomes without enumerating all acceptable ones.

**Descriptive** — "This project uses the Linux Kernel Style Guideline." Documents what exists without giving instructions. The agent must infer the right behavior from the described state. This leaves the interpretation space wide but provides evidence the agent uses to select — it's implicit narrowing through context rather than explicit narrowing through directives.

**Explanatory** — "Avoid hard-coded waits to prevent timing issues in CI environments." Adds a warrant after a rule. The explanation doesn't narrow the interpretation space for the stated rule (the agent would follow "avoid hard-coded waits" either way), but it enables generalisation: an agent that understands *why* can apply the principle to novel situations the author didn't anticipate. This trades off instruction economy against robustness — more tokens for better coverage of the interpretation space's long tail.

**Conditional** — "If you need to use reflection, use ReflectionUtils APIs." Encodes branching logic: different situations get different interpretations. This partitions the interpretation space rather than uniformly narrowing it. The instruction is precise within each branch but requires the agent to correctly identify which branch applies — which is itself an interpretation act.

## Style choice encodes autonomy allocation

The styles form a spectrum from tight constraint to loose context:

```
prescriptive → prohibitive → conditional → explanatory → descriptive
  (comply)      (avoid)       (branch)     (understand)   (infer)
```

Moving left gives reliability at the cost of coverage — prescriptive instructions handle their specific case perfectly but say nothing about adjacent cases. Moving right gives coverage at the cost of reliability — descriptive context helps the agent handle novel situations but may lead to unexpected interpretations.

This is the same tradeoff the [underspecification note](./agentic-systems-interpret-underspecified-instructions.md) identifies between narrowing interpretations and preserving ambiguity. Prescriptive style is stabilisation within the instruction medium — committing to one interpretation without extracting it to code. Descriptive style is deliberately keeping the interpretation space open because the author trusts the agent's judgment (or can't enumerate the cases).

## Interaction with loading tier

Style choice interacts with where an instruction lives in the [loading hierarchy](./context-loading-strategy.md). Always-loaded instructions (CLAUDE.md) compete for attention every session, so they should favour concise prescriptive and prohibitive styles — tight constraint, few tokens. On-demand instructions (skill bodies, WRITING.md) are loaded in task context where the agent needs judgment, so explanatory and descriptive styles earn their token cost by enabling better generalisation.

The claw's own CLAUDE.md reflects this: universal rules are prescriptive ("No wiki-links"), guardrails are prohibitive ("Don't create files unless necessary"), and the routing table is descriptive (documenting what exists so the agent can infer where things go). The detailed writing guidance lives in WRITING.md — loaded on demand, where the explanatory style ("description is a retrieval filter, not a summary — the test: ...") justifies its token cost.

---

Relevant Notes:
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the interpretation-space model that gives these styles their theoretical grounding
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — applies: style choice interacts with loading tier — always-loaded favours prescriptive/prohibitive, on-demand can afford explanatory
- [legal drafting solves the same problem as context engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's narrowing techniques (defined terms, enumeration, canons of interpretation) operate within instructions; writing styles describe how instructions are framed — two complementary taxonomies of the same activity
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — extends: prescriptive style is stabilisation within the instruction medium, short of extracting to code
- [context engineering for AI agents in OSS](../sources/context-engineering-ai-agents-oss.md) — source: the empirical taxonomy of five writing styles observed across 466 open-source projects

Topics:
- [claw-design](./claw-design.md)
- [computational-model](./computational-model.md)
