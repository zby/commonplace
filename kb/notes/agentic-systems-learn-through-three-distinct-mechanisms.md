---
description: Deployed agentic systems learn through three distinct mechanisms — stabilisation (committing to an interpretation of an underspecified spec), crystallisation (prompt→code phase transition), and distillation (extracting procedures from reasoning in the same medium). All are capacity change per Simon; they differ in what changes and whether the medium transitions.
type: structured-claim
traits: []
areas: [learning-theory]
status: current
---

# Agentic systems learn through three distinct mechanisms

Herbert Simon: learning is [any change that produces a more or less permanent change in a system's capacity](learning-is-capacity-change.md) for adapting to its environment. In deployed agentic systems — systems that combine LLMs with persistent artifacts — we've identified three distinct mechanisms by which this happens:

| Mechanism | Operation | What changes | Medium transition |
|-----------|-----------|-------------|-------------------|
| **Stabilisation** | underspecified spec → committed interpretation | Output predictability | No — same medium, tighter constraints |
| **Crystallisation** | prompt → code | Verification regime, consumer, executability | Yes — natural language → executable |
| **Distillation** | discursive → procedural | Rhetorical mode, information density | No — same medium, different organization |

All three are learning in Simon's sense — they produce permanent changes in the system's capacity. They differ in what changes and whether the medium transitions. Each trades [generality for compound gains in reliability, speed, and cost](learning-is-capacity-change.md), but through different operations.

## Stabilisation

Every act of stabilisation fits Simon's definition. When you commit to an interpretation of an underspecified spec — store an LLM output, write a convention, extract a deterministic function — you increase the system's adaptive capacity for the specific case stabilised. In practice this narrows the distribution of outputs (the system becomes more predictable), but the deeper operation is resolving [semantic underspecification](./agentic-systems-interpret-underspecified-instructions.md): choosing one interpretation from the space the spec admits.

### The spectrum of stabilisation

Stabilisation isn't just crystallisation (prompt → schema → code). It starts earlier and includes smaller acts:

| Stabilisation | What changes | Capacity gain |
|--------------|-------------|---------------|
| [Store an LLM output](storing-llm-outputs-is-stabilization.md) | Commit to one interpretation | One decision becomes permanent |
| Write a description field | Enable search without reading | One note becomes findable |
| Create a convention | Make future operations predictable | All operations of that kind become faster |
| Add structured sections | Enable type-specific operations | The document affords new workflows |
| Extract a deterministic function | Move from LLM to code | One operation becomes reliable, fast, free |

Each step trades generality (the document/process could have been anything) for something more specific and reliable. The mechanism is the same across the whole spectrum — it's just that full crystallisation changes the substrate entirely, making the compound gain largest.

### Softening is also learning

The reverse — softening, replacing a stabilised component with a general-purpose one — is also learning. It increases generality at the cost of the compound. When scale makes a general approach good enough on reliability+speed+cost, the [bitter lesson boundary](bitter-lesson-boundary.md) tells you to soften. Both directions are capacity change; they just operate on different [dimensions of capacity](learning-is-capacity-change.md).

### The KB as evidence

The KB itself demonstrates this. Every session that improves notes, sharpens connections, or discovers principles is stabilisation — and therefore learning. From fixing a typo (narrow scope) to discovering design principles (wide scope), the mechanism is the same: reduce variance, increase capacity. This is why [the KB already has a learning loop](../claw-design/automating-kb-learning-is-an-open-problem.md) — the open problem is automating the judgment-heavy stabilisations.

## Crystallisation

[Crystallisation](deploy-time-learning-the-missing-middle.md) is the most dramatic form of stabilisation — it crosses a medium boundary. Natural language instructions become executable code. The consumer changes (LLM → interpreter/runtime). The verification regime changes (underspecified semantics → precise semantics, indeterministic execution → deterministic). It's a phase transition: the nature of the artifact changes fundamentally.

The [verifiability gradient](deploy-time-learning-the-missing-middle.md) — from restructured prompts through schemas and evals to deterministic code — is a compound capacity gradient: reliability, speed, and cost all improve together as you move down it. At the top sit [dynamic agents](dynamic-agents-runtime-design.md) — maximum generality, minimum reliability. At the bottom sits deterministic code — minimum generality, maximum reliability. The system's learning trajectory is its movement along this gradient.

## Distillation

[Distillation](../claw-design/skills-derive-from-methodology-through-distillation.md) is the mechanism by which a body of discursive reasoning (methodology notes, design arguments, source reviews) becomes operational procedure (skills). Unlike crystallisation, there is no phase transition — both input and output are natural language consumed by an LLM. What changes is the rhetorical mode: exploratory, multi-perspective argument becomes step-sequenced instruction.

The separation is deliberate: reasoning is factored out of the operational path, not lost. The methodology KB remains accessible for edge cases the distilled skill doesn't cover. This makes distillation a context-budget operation — it exists because [agent statelessness](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) makes it too expensive to load the full reasoning every session.

## Reasoning

### The three mechanisms are distinct, not synonyms

It matters to distinguish them because conflating them produces confused designs:

- If you think skills are **crystallised** methodology, you'll expect them to be more verifiable than they are (they're still natural-language instructions interpreted by an LLM — semantically underspecified and execution-indeterministic).
- If you think skills are **stabilised** methodology, you'll focus on constraining agent behavior rather than on extracting the right procedures.
- If you recognise skills as **distilled** methodology, you'll focus on the right questions: what to extract, what to leave in the source, how to maintain the derivation relationship.

Similarly, treating crystallisation as "just more stabilisation" misses the phase transition — the qualitative change when an operation moves from underspecified, indeterministic substrate to precise, deterministic substrate.

### The stabilise/soften cycle is a learning cycle

The stabilise/soften cycle described in [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) is, viewed through Simon's definition, a learning cycle. Each stabilisation step resolves semantic underspecification — committing to an interpretation and (often) eliminating execution indeterminism — making the system more capable for the specific case it handles. Each softening step reintroduces underspecification, making the system more capable for the general case. The cycle isn't maintenance — it's how the system learns.

### Continuous learning is stabilisation during deployment

AI labs frame "continuous learning" as adapting a deployed model to new data without retraining — the hot topic in production AI. The claim here is that stabilisation through versioned artifacts [achieves the same goals](./continuous-learning-is-stabilisation-during-deployment.md) — durable adaptation, task-specific knowledge accumulation, improved performance over time — and does it better on inspectability, rollback, verification, and composability. The continuous learning problem is a special case: stabilisation that happens during deployment, on the basis of deployment experience.

## Caveats

- **Not all learning is covered by these three.** Weight-based learning captures distributional knowledge (style, tone, world knowledge) that doesn't reduce to explicit artifacts. The claim is that these three mechanisms cover most of what *deployed* systems need for continuous improvement, not everything.
- **Stabilisation requires curation.** Artifacts go stale, schemas need updating, conventions drift. The process assumes an active curation loop, whether human-driven or automated.
- **The compound gain only fully applies to operations that completely crystallise.** Partially stabilised operations — where a script handles 80% of cases and an LLM handles the rest — get partial gains, and the boundary needs ongoing maintenance.
- **Distillation may be a special case of stabilisation viewed differently.** One could argue that extracting procedures from reasoning IS narrowing the distribution — the agent's behavior is more constrained with a skill than with fifteen methodology notes. The distinction is in intent: stabilisation constrains, distillation extracts. Whether this holds up as a true separate mechanism or resolves into a perspective on stabilisation remains to be seen.

---

Relevant Notes:
- [learning-is-capacity-change](learning-is-capacity-change.md) — foundation: provides the capacity decomposition (generality vs reliability+speed+cost) that makes this claim precise
- [deploy-time-learning](deploy-time-learning-the-missing-middle.md) — foundation: defines the three timescales and the verifiability gradient; develops the crystallisation mechanism in detail
- [skills-derive-from-methodology-through-distillation](../claw-design/skills-derive-from-methodology-through-distillation.md) — foundation: develops the distillation mechanism; distinguishes it from crystallisation and stabilisation
- [continuous-learning-is-stabilisation-during-deployment](./continuous-learning-is-stabilisation-during-deployment.md) — extends: the specific argument that AI labs' continuous learning is achievable through artifact-based stabilisation
- [bitter-lesson-boundary](bitter-lesson-boundary.md) — connects: the calculator/vision-feature boundary determines when stabilisation is permanent vs when softening is needed
- [storing-llm-outputs-is-stabilization](storing-llm-outputs-is-stabilization.md) — instance: the simplest form of stabilisation-as-learning
- [automating-kb-learning-is-an-open-problem](../claw-design/automating-kb-learning-is-an-open-problem.md) — applies: the KB's manual learning loop is stabilisation; automating the judgment-heavy parts is the open problem
- [dynamic-agents-runtime-design](dynamic-agents-runtime-design.md) — exemplifies the pre-stabilisation state: ephemeral agents at the top of the verifiability gradient
- [oracle-strength-spectrum](oracle-strength-spectrum.md) — the Karpathy verifiability properties (resettable, efficient, rewardable) map to oracle strength; determines when stabilisation is possible
- [methodology-enforcement-is-stabilisation](../claw-design/methodology-enforcement-is-stabilisation.md) — applies: the instruction → skill → hook → script gradient is stabilisation applied to methodology
- [agent-statelessness-makes-skill-layers-architectural](../claw-design/agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — motivates: explains why distillation is architecturally necessary, not just convenient

Topics:
- [learning-theory](./learning-theory.md)
