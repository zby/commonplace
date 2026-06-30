# Marginal-Value Redundancy Review v3

**Gate:** kb/work/agent-note-improvement/compression/marginal-value-redundancy.md
**Target:** kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md

## Result
WARN

## Findings
- WARN: `## Scope` should not remain in its current standalone form. Its useful contribution is the graded representational-form boundary, but the section mostly restates the note's established contrast: codified artifacts dereference, prose does not, and less obvious applications need reinforcement. Keeping it as a separate section spends a full chunk on a boundary that could be folded into the core mechanism with lower context cost.

## Suggested Revision
Delete the standalone `## Scope` section and fold its useful boundary into the mechanism before `## Costs`. For example, extend the denormalization paragraph with one compact sentence: "This need scales with representational form and locality: schema fields, types, and function signatures can rely on dereference; prose-like, distant, or non-obvious uses need reinforcement." This preserves the guardrail against over-applying the claim while removing the recap section.
