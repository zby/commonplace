---
description: The five empirically observed context-file writing styles (descriptive, prescriptive, prohibitive, explanatory, conditional) are not stylistic variation — they correspond to different strategies for narrowing the interpretation space agents face, trading off constraint against generalisability
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Writing styles are strategies for managing underspecification

An [empirical study of AI context files](../sources/context-engineering-ai-agents-oss.md) across 466 open-source projects identified five writing styles in convention sections: descriptive, prescriptive, prohibitive, explanatory, and conditional. The authors treat these as stylistic variation, but viewed through the [underspecification lens](./agentic-systems-interpret-underspecified-instructions.md), each style is a distinct strategy for narrowing the interpretation space — and the choice encodes how much autonomy the author grants the agent.

## The five styles as constraint strategies

**Prescriptive** — "Follow the existing code style and conventions." Direct imperatives that select a single interpretation. The agent's job is compliance, not judgment. Best where any deviation is a bug.

**Prohibitive** — "Never commit directly to the main branch." Eliminates specific interpretations without prescribing alternatives. The agent retains autonomy within the remaining space. Cheaper than prescriptions: forbidding a few bad outcomes costs less than enumerating all acceptable ones.

**Descriptive** — "This project uses the Linux Kernel Style Guideline." Documents what exists without directing action. The agent must infer correct behavior from described state — narrowing through context rather than directive.

**Explanatory** — "Avoid hard-coded waits to prevent timing issues in CI environments." Attaches a warrant to a rule. The warrant adds no direct constraint, but enables generalisation: an agent that understands *why* can extend the principle to unanticipated situations. More tokens for better coverage of the long tail.

**Conditional** — "If you need to use reflection, use ReflectionUtils APIs." Encodes branching logic: different situations, different interpretations. This partitions the interpretation space rather than uniformly narrowing it. Each branch is precise, but selecting which branch applies is itself an interpretation act.

## Style choice encodes autonomy allocation

The styles form a spectrum from tight constraint to loose context:

```
prescriptive → prohibitive → conditional → explanatory → descriptive
  (comply)      (avoid)       (branch)     (understand)   (infer)
```

Moving left buys reliability at the cost of coverage — prescriptive instructions handle their case perfectly but say nothing about adjacent ones. Moving right buys coverage at the cost of reliability — descriptive context helps the agent handle novel situations but risks unexpected interpretations.

The [underspecification note](./agentic-systems-interpret-underspecified-instructions.md) identifies this same tradeoff: narrowing interpretations versus preserving ambiguity. Prescriptive style constrains within the instruction medium — committing to one interpretation without extracting it to code. Descriptive style deliberately keeps the space open, because the author trusts the agent's judgment or cannot enumerate the cases.

## Interaction with loading tier

Style choice interacts with where an instruction sits in the [loading hierarchy](./instruction-specificity-should-match-loading-frequency.md). Always-loaded instructions (CLAUDE.md) occupy context every session and should favour prescriptive and prohibitive styles — tight constraint, few tokens. On-demand instructions (skill bodies, WRITING.md) load in task context where the agent needs judgment, so explanatory and descriptive styles earn their token cost through better generalisation.

The KB's own CLAUDE.md illustrates this: universal rules are prescriptive ("No wiki-links"), guardrails are prohibitive ("Don't create files unless necessary"), and the routing table is descriptive — documenting what exists so the agent infers where things go. Detailed writing guidance lives in WRITING.md, loaded on demand, where explanatory style ("description is a retrieval filter, not a summary") justifies its token cost.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the interpretation-space model that gives these styles their theoretical grounding
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — applies: style choice interacts with loading tier — always-loaded favours prescriptive/prohibitive, on-demand can afford explanatory
- [legal drafting solves the same problem as context engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's narrowing techniques (defined terms, enumeration, canons of interpretation) operate within instructions; writing styles describe how instructions are framed — two complementary taxonomies of the same activity
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: prescriptive style is constraining within the instruction medium, short of extracting to code
- [context engineering for AI agents in OSS](../sources/context-engineering-ai-agents-oss.md) — source: the empirical taxonomy of five writing styles observed across 466 open-source projects
- [Toulmin Argument (Purdue OWL)](../sources/purdue-owl-toulmin-argument.md) — grounds: the "warrant" concept used in the explanatory style description originates from Toulmin's argumentation model
