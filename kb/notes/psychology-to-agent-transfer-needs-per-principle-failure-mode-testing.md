---
description: Brainstorming a methodology for evaluating cognitive-science-to-agent transfer — assembled from three existing KB notes and tested against Youssef's five psychology principles as worked examples
type: note
traits: [has-external-sources, title-as-claim]
tags: [learning-theory]
status: seedling
---

# Psychology-to-agent transfer needs per-principle failure-mode testing

The KB has a recurring tension: cognitive science analogies keep appearing in agent memory discourse (Tulving's taxonomy, Conway's self-memory system, Damasio's somatic markers), but it's unclear whether they transfer mechanistically or just provide vocabulary. The [three-space memory note](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) leaves this open explicitly: "whether the cognitive science analogy adds explanatory power beyond [simpler advice] remains to be seen."

Three existing KB notes contain the components of a methodology for testing this. This note assembles them and runs the test against [Youssef's five psychology principles for AI memory](../sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.ingest.md).

## The methodology

**Component 1: Per-convention failure-mode matching.** From [human writing structures transfer because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md): don't assume wholesale transfer. For each proposed principle, ask: "what specific failure does this address in humans, and does the agent exhibit that failure?" The Lampinen results show this must be done per-convention — some transfer, some don't, and you can't tell without checking.

**Component 2: Intermediate-position warning.** From [LLM learning phases fall between human modes](./llm-learning-phases-fall-between-human-learning-modes.md): LLM phases don't map 1:1 to human cognition. Pre-training conflates evolution and learning; in-context conflates learning and retrieval. Analogies that assume a clean mapping will systematically mispredict what helps.

**Component 3: The simpler-mechanism test.** If a principle's engineering value reduces to a standard information retrieval concept, the psychology is naming, not explaining. The analogy is decorative — useful for communication, misleading for design.

## Youssef's five principles as test cases

### 1. Hierarchical temporal organization (Conway)

*Human failure addressed:* Memories become harder to access as they age and multiply; temporal hierarchy (lifetime periods → general events → specific episodes) provides retrieval structure.

*Does the agent exhibit this failure?* Yes — flat memory stores without temporal indexing do degrade retrieval as they grow. The [flat-memory predictions note](./flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) documents this: operational debris pollutes search.

*Simpler mechanism:* Temporal indexing with decay weighting. This is standard information retrieval — you don't need Conway's Self-Memory System to justify organizing memories by time. The hierarchical structure (lifetime periods → general events → episodes) doesn't have a clear agent analogue; agents don't have "lifetime periods."

*Verdict:* The failure mode transfers. The mechanism doesn't — it reduces to temporal indexing. **Decorative.**

### 2. Goal-relevant filtering (working self)

*Human failure addressed:* Irrelevant memories intrude on goal pursuit. Conway's "working self" gates memory accessibility based on current goals.

*Does the agent exhibit this failure?* Yes — agents retrieve irrelevant memories during task execution. This is a real retrieval problem.

*Simpler mechanism:* Query-time context matching — filter retrieved memories by relevance to the current task. This is what every RAG system does. The "working self" framing adds the idea that current goals should *suppress* irrelevant memories, not just boost relevant ones. Suppression is marginally interesting — it suggests negative filtering, not just positive scoring — but agents don't have involuntary memory intrusion. They only "remember" what they query for.

*Verdict:* Failure mode partially transfers (retrieval noise is real, involuntary intrusion is not). Mechanism reduces to relevance filtering with a minor insight about negative scoring. **Mostly decorative**, with a small genuine contribution.

### 3. Emotional weighting (Damasio)

*Human failure addressed:* Without somatic markers, humans struggle to make decisions (Damasio's patients with ventromedial prefrontal damage show impaired decision-making despite intact reasoning).

*Does the agent exhibit this failure?* Not obviously. Agents don't exhibit decision paralysis from lack of emotional metadata. They decide based on whatever's in context. The specific failure — "can reason but can't decide" — doesn't describe LLM behavior.

*Simpler mechanism:* Priority metadata (urgency, confidence, surprise) attached to stored knowledge, influencing retrieval ranking. Several reviewed systems already do this — Cludebot uses decay scoring, cass-memory uses confidence tracking. But these are retrieval priority heuristics, not somatic markers. The Damasio framing implies the metadata should influence *decision-making*, not just *retrieval ranking* — a distinction that might matter if agents need to weigh competing goals.

*Verdict:* Failure mode doesn't clearly transfer. Mechanism reduces to priority metadata. **Decorative**, unless agents develop competing-goal architectures where the decision-making distinction becomes relevant.

### 4. Narrative coherence (Bruner)

*Human failure addressed:* Humans organize experience into stories; memories without narrative structure are harder to integrate, recall, and use for identity construction.

*Does the agent exhibit this failure?* Partially — context windows stuffed with disconnected facts do degrade output quality compared to coherently organized context. But "narrative" is a strong claim. What agents need is *relevance coherence* — all context items should relate to the task and each other. This is the KB's existing scoping concern.

*Simpler mechanism:* Context composition with relevance filtering and ordering. The "narrative" framing adds the idea that temporal sequence and causal connection matter, which is true but doesn't require Bruner — it's document design.

*Verdict:* Failure mode partially transfers (incoherent context hurts, but the failure is about relevance, not narrative). **Decorative.**

### 5. Co-emergent self-model (Klein & Nichols)

*Human failure addressed:* Identity and memory construct each other. The self-model determines what's remembered; what's remembered shapes the self-model. Identity disorders show what happens when this loop breaks.

*Does the agent exhibit this failure?* This is the most interesting case because it doesn't reduce to retrieval. Current agents have a static self-model (system prompt, persona) that doesn't evolve with accumulated memory. Whether this is a *failure* depends on whether the task requires long-term identity coherence. For bounded tasks (coding, Q&A), no. For persistent agents (long-running assistants, autonomous agents), possibly yes — the system prompt doesn't adapt to what the agent has learned.

*Simpler mechanism:* There isn't an obvious one. A system prompt that updates based on accumulated experience is qualitatively different from static configuration. The bootstrapping problem (need identity to filter memories, need memories to construct identity) is genuine and doesn't reduce to information retrieval.

*Verdict:* Failure mode may transfer for persistent agents. Mechanism is genuinely novel. **Not decorative** — but addresses a failure mode most current agents don't exhibit because they aren't persistent enough for it to matter.

## The pattern

Four of five principles reduce to information retrieval concepts: temporal indexing, relevance filtering, priority metadata, coherent context composition. The psychology provides vocabulary and bibliography but not mechanism. The engineering solutions already exist in the agent memory literature and don't need Conway, Damasio, or Bruner to justify them.

The fifth principle (co-emergent self-model) is the exception. It doesn't reduce, it addresses a genuine architectural problem, and it names a feedback loop that the KB hasn't explored. But it applies to a class of agents (persistent, identity-bearing) that barely exists yet.

This pattern — four decorative, one genuine but premature — may be typical of cognitive-science-to-agent transfer proposals. The principles that address well-understood retrieval problems are easy to propose and easy to reduce. The principles that address genuinely novel problems are harder to evaluate because the target systems don't exist yet.

## What this implies for the Tulving question

The three-space note asks whether the Tulving mapping (semantic/episodic/procedural → knowledge/self/operational) is decorative. This methodology suggests: **test each space separation against its failure mode.** Does conflating knowledge and operational memory cause search pollution? (Probably yes — test it.) Does conflating self-knowledge and knowledge memory cause identity scattering? (Only if the agent has an identity to scatter.) Does the separation require Tulving, or does it reduce to "separate persistent from transient with different retention policies"?

The bet is that the separation is useful but the Tulving mapping is decorative — the same conclusion four of five Youssef principles reach.

## Open questions

- Is there a version of the methodology that can evaluate principles for *future* agent architectures, not just current ones? The co-emergent self-model is genuinely interesting but can't be tested against systems that don't exist yet.
- Does the "decorative but useful for communication" category have value? Psychology vocabulary might help interdisciplinary teams think about agent memory even if the mechanisms don't transfer. Naming is not nothing.
- The ingest notes a source-to-source tension: [deepfates](../sources/the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici-2036857868914483592.ingest.md) and Youssef diagnose the same problem (AI memory is broken) but propose opposite solutions (weight updates vs architecture). The failure-mode methodology could adjudicate: which failure modes require weight changes and which can be addressed architecturally?

---

Relevant Notes:

- [human writing structures transfer because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — foundation: provides the per-convention failure-mode matching methodology this note generalizes
- [LLM learning phases fall between human modes](./llm-learning-phases-fall-between-human-learning-modes.md) — foundation: the intermediate-position warning that prevents 1:1 human-to-LLM mapping
- [three-space agent memory echoes Tulving's taxonomy](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) — extends: this note's methodology directly addresses the "decorative?" question left open there
- [Youssef: psychology principles for AI memory](../sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.ingest.md) — source: the five principles used as worked examples
- [flat memory predicts specific cross-contamination failures](./flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) — evidence: documents the search pollution failure mode that principles 1 and 2 address
- [deepfates LLM memory critique](../sources/the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici-2036857868914483592.ingest.md) — contradicts source: same diagnosis, opposite solution — weight updates vs architecture
