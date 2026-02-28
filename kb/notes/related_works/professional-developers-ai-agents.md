# Professional Software Developers and AI Agent Use

**Paper:** https://arxiv.org/html/2512.14012v1

## Summary

This research investigates how experienced software developers (3+ years professional experience) actually use AI agents for coding, contrasting real-world practice with "vibe coding" approaches that prioritize flow over code quality.

### Methodology

- **Field Observations (N=13)**: Screen-recorded sessions where experienced developers tackled real work tasks using preferred agentic tools, followed by semi-structured interviews
- **Qualitative Survey (N=99)**: A 15-minute survey gathering broader developer perspectives

### Key Findings

1. **Developers want control, not autonomy** - Professional developers exercise deliberate control over agents rather than trusting them blindly
2. **Validation is essential** - They validate all agent outputs before accepting
3. **Planning before implementation** - Developers plan extensively before letting agents work
4. **Task suitability matters** - Agents work well for straightforward, well-described tasks but struggle with complex problems
5. **Control enables enjoyment** - Developers enjoy agent use when they retain control

### Notable Quote

> "There is no way I'll EVER go back to coding by hand" (S28)

Yet this doesn't mean abandoning oversight—developers actively supervise agent behavior.

## Relevance to llm-do

This paper provides empirical validation for llm-do's design philosophy.

### Alignment with llm-do Architecture

| Paper Finding | llm-do Implementation |
|--------------|----------------------|
| Developers want control, not autonomy | Imperative control flow—Python owns the logic (`if`, `for`, `try/except`), not a declarative graph DSL |
| Validation of all agent outputs | Approval system—tool calls gated with syscall-like approvals; pattern-based rules |
| Plan extensively before implementation | Workers as focused units—decomposition into composable, well-scoped workers |
| Agents work well for straightforward tasks | Worker design—each worker has clear instructions, tools, and boundaries |
| Maintaining software quality standards | Progressive stabilizing—extract stable LLM patterns into deterministic, testable Python code |

### Core Insight Validation

The paper's central finding—**"Professional developers exercise deliberate control over agents rather than trusting them blindly"**—is exactly what llm-do's architecture enables:

1. **Visible distribution boundaries** - The system explicitly marks where you cross from deterministic (tools) to stochastic (LLM workers), so developers know when trust is required

2. **Bidirectional refactoring** - As patterns stabilize, stabilize them to code; as edge cases multiply, soften back to prompts. This matches the paper's observation that developers "leverage their expertise to ensure quality"

3. **Bounded recursion** - Depth limits prevent runaway delegation, supporting the observed developer need for predictable behavior

## Implications

This paper supports positioning llm-do as aligned with professional practice:

- The approval system directly addresses the "validation of outputs" finding
- Progressive stabilizing is the systematic approach to what developers do informally (gradually trusting and extracting patterns)
- The "Unix philosophy for agents" matches how experienced developers actually want to work—with control, oversight, and the ability to stabilize patterns over time

---

Relevant Notes:
- [stabilisation-is-learning](../agentic-systems-learn-through-three-distinct-mechanisms.md) — the developer behaviors observed here (validate, extract patterns, stabilise) are empirical evidence of the crystallisation loop this note formalises as continuous learning
