# Review Bundle

Review run id: 2304
Target: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md

=== PAIR REVIEW START: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/completeness-boundary-cases ===
### Summary
The note does not present a closed taxonomy, but it does use a representational-form gradient and a cost framework for when restatement is needed. Boundary cases map cleanly: symbolic schema fields sit at the codified end, ordinary LLM-read prose sits at the prose end, mixed Markdown splits by operative part, local obvious references need less reinforcement, and distant or conditional uses need more.

### Findings
- PASS: The graded scope handles the main boundary cases instead of claiming an exhaustive or binary framework. Conditional facts are explicitly called out as costlier because branching must move into either prose templates or process constraints.
- PASS: Adjacent cases near the boundary, such as Markdown frontmatter or structured prose, are covered by the "between them" scope paragraph: the more formal, local, and obvious the application, the fewer restatements are required.

## Result: PASS
=== PAIR REVIEW END: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/completeness-boundary-cases ===

=== PAIR REVIEW START: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/explanatory-reach ===
### Summary
The note gives a mechanism, not just a pattern: formal names propagate by dereference, while LLM-read prose requires an interpretive act whose reliability decays with distance, non-obviousness, and conditionality. The falsifiable test section makes the claim meaningfully vulnerable to counterevidence.

### Findings
- PASS: The central explanation is load-bearing. If the premise were varied so that prose declarations propagated with the same reliability as formal references, the conclusion would change; the note explicitly says the claim would be wrong.
- PASS: The note avoids ad-hoc protection by naming the weak point and an ablation: compare frontmatter-only declaration against point-of-use restatement and measure downstream behavior.
- PASS: The cost section strengthens explanatory reach by explaining why denormalization is not free and why a normalized check is the compensating mechanism.

## Result: PASS
=== PAIR REVIEW END: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/explanatory-reach ===

=== PAIR REVIEW START: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/grounding-alignment ===
### Summary
The linked notes support the major premises: representational form distinguishes prose from symbolic consumers, codification marks the transition to formal assigned consequences, and underspecified instructions explain why LLM application of a declared fact is interpretive rather than dereferential. The broader denormalize-and-check consequence is a synthesis built on those premises rather than a claim directly stated by one source.

### Findings
- PASS: The `representational-form` and `codification` links are accurately used to ground the prose-versus-symbolic contrast. Those notes explicitly distinguish prose interpretation from symbolic consumers with assigned consequences.
- PASS: The `agentic systems interpret underspecified instructions` link aligns with the note's claim that even deterministic LLM behavior does not make natural-language application equivalent to formal dereference.
- INFO: The footer relation to `a derived copy of recomputable truth must be checked or absent` is plausible but synthetic. That linked note grounds the checked-copy rule and mentions status as a candidate trust mark, while the target note applies the rule to prose restatement reach; it should not be read as direct evidence that a status banner instance is already established there.

## Result: PASS
=== PAIR REVIEW END: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/grounding-alignment ===

=== PAIR REVIEW START: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/internal-consistency ===
### Summary
The note is internally consistent. Its opening says single-source-of-truth is unsafe for prose, then narrows that with "often," cost, scope, and testing sections that make the requirement graded rather than universal.

### Findings
- PASS: There is no contradiction between "restate it there" and "the check can stay normalized"; the note distinguishes agent-facing propagation from machine-checkable drift control.
- PASS: The scope section is consistent with the title and body: "prose has no reliable dereference" means no formal propagation operation, not that every prose declaration always fails to influence later interpretation.
- PASS: The testing section's admission that the claim is currently intuition does not undercut the earlier argument; it correctly states the current evidential status and the falsifier.

## Result: PASS
=== PAIR REVIEW END: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/internal-consistency ===

=== PAIR REVIEW START: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/load-bearing-qualifiers ===
### Summary
The central qualifiers are doing work. "LLM-read," "reliable," "declared fact," "where it applies," and the graded scope are all necessary boundaries for the argument; removing them would create a broader and less defensible claim.

### Findings
- PASS: "LLM-read prose" is intentional domain scoping. The mechanism depends on an LLM interpreting natural-language context, so this is not an unnecessary narrowing of a broader prose theorem.
- PASS: "Reliable" is load-bearing because the note allows that a model may sometimes infer the declared fact correctly; the claim is about dependable propagation, not total absence of influence.
- PASS: "Declared fact" and "where it applies" are load-bearing because the problem arises when a prior declaration must govern a later context. The argument does not claim every repeated phrase or every linked premise should be duplicated.
- PASS: The scope material is not redundant. It prevents overextension by tying the recommendation to representational form, locality, obviousness, and conditionality.

## Result: PASS
=== PAIR REVIEW END: kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md :: semantic/load-bearing-qualifiers ===
