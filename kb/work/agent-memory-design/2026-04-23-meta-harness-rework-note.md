# Meta-Harness as Rework Input

Target: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

This is a rework note, not a fresh critique. [Meta-Harness](../../agent-memory-systems/reviews/meta-harness.md) does not overturn the current design argument. It hardens a few parts of it and suggests where the next revision should get more operational.

## What Meta-Harness strengthens

- **Raw traces are load-bearing.** The design note already links the paper ingest for this, but the repo review strengthens the claim with code-grounded evidence: rich traces are not just provenance material; they are the substrate that later improvement loops actually inspect.
- **Oracle quality is the bottleneck.** Meta-Harness works because the mutation surface and evaluation loop are explicit. That supports the note's existing claim that corrections and procedure-like patterns are easier to learn from than discoveries.
- **Some durable learning targets should be executable.** The design note already allows scripts/tests/checks as promotion targets. Meta-Harness is a clean external example where the learned artifact is harness code, not prose memory.

## What it does not settle

- It does **not** justify the full four-layer architecture by itself.
- It does **not** solve the open-ended discovery oracle problem.
- It does **not** show that a general agent memory system should be benchmark-optimized in the same way. It is a workshop optimizer under strong task-specific oracles.

## Rework implications

1. **Add a domain-spec section.** Before any automated memory-learning loop, the note should name the need for a written domain spec: evaluation unit, fixed vs mutable parts, budget, held-out split, leakage risks, and candidate interface.
2. **Sharpen workshop vs library language.** Meta-Harness is best read as a workshop optimizer whose outputs may later be distilled into library artifacts. The note should make that boundary clearer.
3. **State executable promotion more explicitly.** When the learned lesson is really about retrieval, context assembly, or action scaffolding, the right target may be code or a check, not a prose memory.
4. **Strengthen the anti-summary point.** The note should say more directly that compressed artifacts are not drop-in substitutes for raw traces during debugging, redistillation, or outer-loop improvement.

## Working judgment

Meta-Harness should inform the rework as an **implementation-level hardening** of the current argument, not as a replacement architecture. It strengthens the note's oracle story, trace-retention story, and system-definition-to-code story. The main addition it pushes is: before discussing automated learning from memory, specify the domain and oracle contract of the loop.
