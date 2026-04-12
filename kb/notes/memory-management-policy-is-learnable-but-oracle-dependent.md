---
description: AgeMem stores facts in memory but learns the governing policy in weights; it is a clean subsymbolic case of durable learning, but one that depends on task-completion oracles the KB lacks
type: note
traits: [has-external-sources, title-as-claim]
tags: [learning-theory]
status: current
---

# Memory management policy is learnable but oracle-dependent

[AgeMem](../sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md) trains an LLM agent through RL to decide when and how to use six memory operations: Add, Update, Delete (LTM) and Retrieve, Summary, Filter (STM). The results are strong — 23-49% improvement over no-memory baselines, 8-9 percentage points attributable to RL training specifically. This is genuine learning in [Simon's sense](./learning-is-not-only-about-generality.md): a capacity change that persists and improves adaptation.

## What it learns: the policy, not the operations

The six operations are hand-crafted tools — their specs fully capture what they do. "Store this key-value pair" has a single correct implementation. What AgeMem learns through RL is the **policy for when to apply them**: when storing something is worth the cost, when summarising is better than retrieving verbatim, when filtering is needed.

This policy cannot be fully specified in advance. "Store information that will be useful later" is a theory about what being useful means, not a definition. Different tasks, contexts, and trajectories make different memory decisions optimal. In [bitter lesson](./bitter-lesson-boundary.md) terms, the operations are the calculator part (specifiable, deterministic), while the composition policy is the vision-feature part (learnable, benefits from scale). AgeMem's results confirm: the RL-trained policy outperforms both no-memory baselines and the LLM's own instruction-following attempts. The hand-crafted heuristics of systems like [A-MEM](../sources/a-mem-agentic-memory-for-llm-agents.ingest.md) are plausible theories about memory management, not definitions of it.

## Why it works: the oracle

AgeMem succeeds because it has a **clear oracle**: task completion. Did the agent complete the ALFWorld task? Did it answer the HotpotQA question correctly? The reward signal is unambiguous, and it propagates backward through the trajectory to credit memory decisions. The step-wise GRPO mechanism broadcasts advantages across all timesteps specifically because memory operations (storing a fact early) are temporally distant from their payoff (using it later).

The RL training works because the evaluation problem is already solved — task completion is a verifiable, binary signal.

## What it accumulates: facts without reach

AgeMem's LTM Add is [accumulation](./learning-is-not-only-about-generality.md) — the most basic learning operation — but only at the low-reach end. It stores **facts**: "the key is on the table," specific observations about the current task state. Facts are [adaptive knowledge](./an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md): useful for the immediate context but without [reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — they don't transfer to other situations. The value of a stored fact depends entirely on **retrievability**: a fact that can't be found when needed is dead weight.

AgeMem's STM operations (Retrieve, Summary, Filter) are [distillation](./definitions/distillation.md) — extracting and compressing from a larger body of information into the working context, shaped by the current task. The LTM curation operations (Update, Delete) refine and retire stored facts.

None of this produces knowledge with reach. [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — positing abstractions and recognizing instances — is what produces theories, the highest-reach items accumulation can store. AgeMem accumulates facts and learns to manage them well, but never moves up the reach gradient from facts to theories.

This scope limitation is also what enables the oracle. The value of a stored fact resolves within the current episode — it either helped complete the task or it didn't. Knowledge with reach, where value depends on questions not yet asked, has no such resolution point.

## How it stores what it learns: split substrate

To close the learning loop, AgeMem accepts a substrate split: facts go into a memory store (somewhat inspectable key-value pairs), but the policy for managing them goes into model weights (opaque, non-diffable, only changeable through retraining).

This makes AgeMem the clean weight-side case in the KB's updated learning taxonomy. Per [continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md), the relevant criterion is not "did weights change?" but "did adaptive capacity change durably?" AgeMem obviously qualifies: the learned policy persists and later behavior depends on it. The interesting question is therefore not whether AgeMem is really learning, but what the weight substrate buys and what it gives up relative to durable symbolic artifacts.

Commonplace stores both in the same medium — files in a repo. A fact ("AgeMem uses GRPO") and a policy ("always search before writing") are both markdown artifacts. Policies are themselves knowledge: searchable, linkable, refinable, composable with other notes. You can [constrain](./definitions/constraining.md) a policy (move it from a convention to a script), [distil](./definitions/distillation.md) it (extract a skill from methodology notes), or [discover](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) that two policies are instances of the same principle. Policies participate in the same [accumulation](./learning-is-not-only-about-generality.md) loop as everything else.

In AgeMem, the policy can't be searched, linked to the facts it manages, or refined incrementally. This is the deeper version of the [inspectable substrate](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) argument: not just "can you inspect the policy?" but "can the policy participate in the knowledge system it governs?" In a unified substrate, policies improve through the same mechanisms as everything else. In a split substrate, they don't. [Learning substrates, backends, and artifact forms](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) names the contrast cleanly: AgeMem puts the governing policy in a subsymbolic substrate, while commonplace tries to keep both policies and facts in a symbolic artifact substrate.

## Comparison to KB learning

AgeMem's oracle (task completion) is exactly what the KB's [automating learning](./automating-kb-learning-is-an-open-problem.md) problem lacks. The boiling cauldron's mutations — Extract, Synthesise, Relink, Regroup, Retire — don't have task-completion equivalents. "Did this connection improve the KB?" depends on what questions will be asked in the future, how the KB's focus evolves, and whether the connection enables reasoning chains that don't yet exist. Evaluating KB mutations is itself a vision-feature problem with no clear answer.

AgeMem's policy learns *which facts help complete tasks*. The KB needs a policy that learns *which connections help answer questions that haven't been asked yet*. The first has a training signal. The second doesn't — or at least, not enough of one yet. AgeMem confirms the diagnosis from the automating-KB-learning note: the bottleneck is the oracle, not the learning mechanism.

But the comparison cuts both ways. **AgeMem has a closed learning loop; we don't.** It trains, improves, and the improvement persists — no human needed. The KB's learning is still entirely manual: human + agent, every session. AgeMem solved it for its domain by accepting trade-offs we're not willing to make (opaque policy, facts without reach, split substrate) — but it *solved* it. Theoretical advantages in substrate design don't count for much while the loop is open.

## What AgeMem teaches us

1. **Memory management decomposes into selection and distillation.** LTM operations (what to remember) are relevance judgments. STM operations (what to load into working context) are distillation. The two require different skills, which is why AgeMem's curriculum trains them separately.

2. **Composition policy is the hard part.** The operations are easy; knowing when to use them is hard. This matches the boiling cauldron's "mutations differ on two axes" analysis — the judgment-heavy parts are where the value lies.

3. **Curriculum structure matters.** AgeMem's three-stage training (LTM first, STM second, coordination third) decomposes a complex learning problem into manageable stages. If the KB's learning loop is ever automated, a similar curriculum — learn to extract before learning to connect, learn to connect before learning to synthesise — would likely be needed.

4. **Base models underuse memory operations.** Post-training, AgeMem agents increase Add operations from 0.92 to 1.64 per episode. Base models with access to memory tools don't use them enough. Even without RL, better prompting or skill design could improve the KB's human+agent loop.

## The inspectability-learnability spectrum

AgeMem is not the only approach to memory management policy. [Fofadiya & Tiwari's adaptive budgeted forgetting](../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) specifies the policy as an explicit formula — relevance = f(recency, frequency, semantic alignment) — with constrained optimization to enforce a hard memory budget. The policy is fully inspectable: you can see exactly why a memory was pruned. But it cannot adapt: the formula is fixed at design time, tuned on benchmarks, and applies uniformly regardless of task.

This establishes a spectrum across systems reviewed in this KB:

| System | Policy mechanism | Inspectability | Adaptability | Oracle needed? |
|---|---|---|---|---|
| Fofadiya & Tiwari | explicit formula + constrained optimization | full — formula is readable | none — weights are fixed | no |
| [Cludebot](../agent-memory-systems/reviews/cludebot.md) | Generative Agents scoring formula + type-specific decay | high — formula is readable, decay rates are configured | limited — dream cycles reorganize but don't retrain | no |
| [cass-memory](../agent-memory-systems/reviews/cass_memory_system.md) | confidence-decayed playbook bullets + Jaccard conflict detection | high — confidence scores and conflict rules are inspectable | moderate — confidence updates from feedback | no |
| AgeMem | RL-trained policy in weights | none — policy is opaque | full — learns from task-completion reward | yes — task completion |

The pattern: inspectable policies avoid oracle dependency because their designers embed the judgment upfront. Learned policies need oracles because the judgment emerges from training signal. The more you can specify in advance, the less you need to learn — but the less you can adapt to tasks the designer didn't anticipate.

Fofadiya & Tiwari's key empirical finding — that controlled forgetting *improves* performance rather than merely maintaining it under budget — suggests that even a fixed formula can outperform unbounded accumulation. But a missing random-pruning baseline leaves open whether the specific formula or simply budget enforcement drives the improvement (see [ingest limitations](../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md#limitations-our-opinion)).

---

Relevant Notes:

- [continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — sharpens: AgeMem is the clean weight-side case because its adaptive change is durable, not because weight updates are the definition of learning
- [Learning substrates, backends, and artifact forms](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: names AgeMem's policy as a subsymbolic substrate case and contrasts it with symbolic artifact approaches
- [bitter lesson boundary](./bitter-lesson-boundary.md) — grounds: memory operations are calculators, the policy for composing them is a vision feature; AgeMem's hybrid architecture confirms the boundary's prediction
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — extends: AgeMem confirms the evaluation gap is the real bottleneck — RL can learn memory policy, but only with a clear oracle, which KB learning lacks
- [a good agentic KB maximizes contextual competence](./an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) — grounds: LTM Add value depends on discoverability (retrievability of stored facts); the three-property framework explains why weight-based memory policy can't produce the articulated relationships a KB needs
- [distillation](./definitions/distillation.md) — applies: AgeMem's STM operations (Retrieve, Summary, Filter) are distillation — extracting focused content for working context
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: AgeMem's LTM Add is accumulation (the basic learning operation) at the low-reach end; the reach gradient from facts to theories frames what AgeMem does and doesn't do
- [first-principles reasoning selects for reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — grounds: AgeMem operates on facts (adaptive, no reach), not rules (explanatory, reach)
- [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — contrasts: AgeMem learns at training time through weights; deploy-time learning through symbolic artifacts during deployment; same behavioral changes, different substrates
- [inspectable substrate defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — contrasts: AgeMem's split substrate (facts in store, policy in weights) vs commonplace's unified substrate (both in files)
- [constraining during deployment is continuous learning](./constraining-during-deployment-is-continuous-learning.md) — contrasts: AgeMem is training-time learning achieving what deploy-time constraining achieves; they differ on inspectability but AgeMem has closed the loop
- [adaptive budgeted forgetting (Fofadiya & Tiwari)](../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) — extends: the inspectable-side counterpart to AgeMem's opaque policy; explicit relevance formula vs RL-trained weights, establishing the inspectability-learnability spectrum for memory management policy
