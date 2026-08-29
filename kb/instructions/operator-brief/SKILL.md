---
name: operator-brief
description: Explain an existing complex technical finding to an operator when its practical meaning is obscured by implementation detail, task-local terminology, or a long causal chain. Do not use for routine updates or simple answers.
type: kb/types/instruction.md
user-invocable: true
argument-hint: "[technical finding path, finding id, or pasted finding]"
---

# Operator brief

Make the operator understand the practical meaning of a complex technical finding and any decision it requires while preserving the technical finding as the evidence-bearing authority.

## Input

Use the technical finding supplied in `$ARGUMENTS`, named by the user, or already established in the current task. Read the complete finding and any directly referenced material needed to interpret it. If the finding cannot be identified, ask for it rather than reconstructing one from hints.

Do not edit the finding, its subject, or supporting artifacts unless the user separately asks for those changes.

## Write the brief

Start with what happens, why it matters, or what the operator needs to decide. Keep conditions that control reachability, scope, impact, or confidence next to the claims they qualify. Do not turn a narrow but serious problem into a general one, or make a qualified conclusion sound certain.

Use ordinary domain language and the active project vocabulary normally. Expand or define terms coined for this task and terms inherited from artifacts that have no canonical definition. A literal code or schema identifier may remain, but state what it represents before relying on the identifier. Do not promote vocabulary during this operation.

Add only enough mechanism to connect the practical account to the technical finding. Put deeper mechanism after the practical explanation. When the technical finding is retained in a file or report, point to its exact path and finding identifier under a natural phrase such as `Technical basis`; do not reproduce its evidence in the brief. If no retained finding exists, keep a clearly labelled technical finding after the practical explanation and keep evidence there rather than mixing it into the opening.

State a proposed action only when the technical finding establishes it. Prefer the required outcome or invariant over speculative patch mechanics. If the operator must choose among real alternatives, state that decision and its material trade-off. If no operator decision is needed, do not manufacture one.

Use headings or bullets only when they make the particular explanation easier to inspect. The skill has no mandatory output template or word limit.

## Verify

Before returning, compare the brief with the technical finding:

- The opening lets the intended operator say what happens and why it matters without first loading implementation context.
- Important reachability conditions, scope, impact, and uncertainty survived the translation.
- Every task-local or definitionless term needed by the brief is expanded or defined, and every retained identifier has a stated role.
- The technical basis points to the evidence-bearing finding when one exists; the brief does not present a pointer or unsupported summary as evidence.
- The explanation requests only a decision the finding actually requires.
