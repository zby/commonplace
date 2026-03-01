# Eric Evans: AI Components for a Deterministic System

Source: https://www.domainlanguage.com/articles/ai-components-deterministic-system/

This note analyzes Eric Evans' article on integrating LLM-based components into deterministic software systems and explores how its framework validates and extends llm-do's design.

## Article Overview

Evans identifies a fundamental tension: LLMs produce non-deterministic outputs that resist integration into structured, conventional software. Using domain classification in code repositories as an example, he proposes separating concerns to manage this tension.

### Core Principles

1. **Separate Modeling from Classification**
   - *Modeling*: Creating categorization schemes (exploratory, creative)
   - *Classification*: Assigning categories within a scheme (repeatable, deterministic)
   - Treat these as fundamentally different tasks

2. **Create Canonical Categories First**
   - Freeze a taxonomy before classification begins
   - Ensures comparable results across invocations

3. **Leverage Established Standards**
   - Use published classification systems (NAICS, ISO, etc.) for generic domains
   - "Published languages have great advantages! They are worth looking for."

4. **Human-Driven Modeling for Core Domains**
   - For custom categorization: "have humans drive the modeling in an exploratory, iterative process"
   - LLMs excel at classification *within* human-designed frameworks

## Alignment with llm-do

Evans' framework maps directly to llm-do's core philosophy:

| Evans' Concept | llm-do Equivalent |
|----------------|-------------------|
| Modeling (exploratory) | LLM workers exploring options |
| Classification (repeatable) | Extracted Python tools |
| Frozen taxonomy | Schemas (`input_model_ref`, `output_model_ref`) |
| "Stabilize the categories" | "Extend with LLMs, stabilize with code" |

The unified calling convention in llm-do means transitioning from modeling to classification is local—callers don't change when a worker becomes a tool.

### Schema-Driven Design

llm-do already supports Evans' "canonical categories first" via:
- `input_model_ref` / `output_model_ref` in worker frontmatter
- Pydantic models as frozen contracts
- Validation at trust boundaries

## Potential Extensions

### 1. Leverage Established Standards for Generic Subdomains

When workers deal with generic subdomains, reference established taxonomies rather than letting LLMs invent categories:

| Domain | Standard to Consider |
|--------|---------------------|
| Business sectors | NAICS codes |
| Document types | ISO standards |
| Licenses | SPDX identifiers |
| Commit messages | Conventional Commits |
| Error categories | HTTP status codes, syslog severity |

**Implementation**: Document this as a pattern; add examples showing workers that use external taxonomies.

### 2. Judge Model Pattern for Taxonomy Selection

Evans describes iterative refinement with a "judge" model:

```
1. Sampling worker: generates N candidate categorization schemes
2. Judge worker: evaluates candidates against criteria (coverage, overlap, specificity)
3. Output: frozen schema for downstream classification workers
```

This could be:
- A documented meta-pattern
- A reusable worker template
- An example in `examples/taxonomy-generation/`

### 3. Explicit Modeling vs Classification Phase Markers

Consider a worker config flag:

```yaml
---
name: categorize_files
phase: classification  # vs "modeling" for exploratory work
---
```

This could:
- Enable stricter validation (same input → same output expected)
- Trigger warnings if outputs vary too much across runs
- Guide approval policies (classification = lower risk, more automatable)

### 4. Two-Phase Workflow Documentation

Document the pattern explicitly:

**Phase 1: Modeling (human-in-loop)**
- Workers generate candidate schemas
- Human reviews, refines, selects
- Output: frozen Pydantic model or enum

**Phase 2: Classification (automated)**
- Workers use frozen schema
- Repeatable, testable
- Progressive stabilization candidate

## Implications for Progressive Stabilization

Evans reinforces the stabilization workflow with clearer triggers:

**Signals to stabilize** (worker → tool):
- Classification task with frozen taxonomy
- Consistent output structure across runs
- High repeatability requirement

**Signals to keep stochastic**:
- Exploratory modeling phase
- Evolving requirements
- Edge cases requiring judgment

## Distribution Boundaries

Evans' modeling/classification distinction maps to llm-do's distribution boundaries. "Freeze a taxonomy before classification" is a specific instance of the broader pattern that [storing LLM outputs is stabilization](../storing-llm-outputs-is-stabilization.md) — collapsing a distribution to a point, then working deterministically with the result.

| Type | Input→Output | Testing Approach |
|------|--------------|------------------|
| Tools (classification) | Same→Same | `assert result == expected` |
| Workers (modeling) | Same→Distribution | Sample and check invariants |

Schema validation sits at the trust boundary between these. The two testing approaches map to the [two distinct testing targets](../storing-llm-outputs-is-stabilization.md) for stabilized artifacts: testing the distribution (does the prompt reliably produce good output?) vs testing the sample (is this specific output good?).

## Summary

Evans' article validates llm-do's core approach ("extend with LLMs, stabilize with code") while suggesting we could be more explicit about:

1. The modeling/classification boundary
2. When to use established standards
3. How to generate and freeze taxonomies
4. Phase markers in worker configuration

The key insight: LLMs are excellent classifiers but unreliable modelers. Design systems that leverage this asymmetry. [The bitter lesson](../../sources/wikipedia-bitter-lesson.md) provides the counter-argument: general-purpose methods scaling with computation have historically outperformed hand-crafted domain knowledge, which suggests that freezing human-designed taxonomies may be a temporary engineering expedient rather than a durable design principle. Whether Evans' approach survives as a wise division of labor or gets dissolved by scaling model capability is an open question.

## References

- Article: https://www.domainlanguage.com/articles/ai-components-deterministic-system/
- Evans' DDD work: https://www.domainlanguage.com/
- [agentic systems interpret fuzzy specifications](../agentic-systems-interpret-fuzzy-specifications.md) — fuzzy vs precise semantics, interpretation narrowing, stabilise/soften
- Related: [adaptation-agentic-ai-analysis.md](../research/adaptation-agentic-ai-analysis.md)
