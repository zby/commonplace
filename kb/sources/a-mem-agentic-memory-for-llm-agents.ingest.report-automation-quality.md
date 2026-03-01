# Automated linking improves retrieval but may degrade navigability

Three sources converge on a single trade-off in knowledge linking from different angles. A-MEM demonstrates empirically that automated memory evolution — constructing notes, linking by embedding similarity, and reorganizing context when new memories arrive — improves QA accuracy on long-term conversational benchmarks. Notes Without Reasons argues from first principles and agent testimony that embedding-based connections carry no reasons and erode an agent's trust in the entire linking infrastructure. The open-problem note frames the same tension structurally: the judgment-heavy mutations (connections, groupings, synthesis) are exactly the operations that automated systems execute most crudely. The question is whether these positions contradict each other or whether they measure different things.

## They measure different things

A-MEM and Notes Without Reasons are not contradictory. They evaluate knowledge systems against different criteria and both succeed on their own terms.

**A-MEM optimizes for retrieval.** Its benchmarks (LoCoMo, DialSim) measure whether the system can answer questions correctly. In this frame, a link is valuable if it brings the right memory into context when a question arrives. Embedding similarity is a good-enough proxy for relevance — cosine proximity surfaces memories that share vocabulary and topic, which is usually sufficient for QA. The ablation study shows that memory evolution (strengthening context, updating neighbors) adds value beyond initial link generation, confirming that automated reorganization improves retrieval. But the benchmarks never ask: can an agent inspect this link and decide whether to follow it? The evaluation treats the memory system as a retrieval black box that either surfaces the right answer or does not.

**Notes Without Reasons optimizes for navigability.** The article's core concern is not whether the system retrieves correct answers but whether an agent can reason about the link structure itself. When a link carries a reason ("since X contradicts Y on the question of Z"), the agent can estimate relevance before following the link, prune irrelevant paths, and build chains of reasoning across multiple hops. When a link carries only implicit similarity, the agent must follow it to discover whether it matters — wasting context tokens and, worse, learning to discount all links when enough of them lead nowhere. The credibility erosion argument is specific: noisy links degrade the value of good links by training the agent to distrust the infrastructure.

**The distinction is adjacency versus connection.** A-MEM's links are adjacency: "these two memories are near each other in embedding space, and an LLM judged the proximity genuine." Notes Without Reasons argues that adjacency is different in kind from connection: a connection is a propositional claim about a relationship ("extends," "contradicts," "grounds"), not a confidence score about similarity. The difference matters for navigation but may not matter for retrieval. A retrieval system only needs to surface relevant memories; a navigation system needs the agent to understand why each link exists so it can decide what to read next.

## What evaluation would capture both?

An evaluation that captures both retrieval and navigability would need at least two measurement dimensions:

**Retrieval accuracy** — the dimension A-MEM already measures. Given a question, does the system surface the right content? Standard QA benchmarks work here: precision, recall, F1 over answer correctness. A-MEM's existing evaluation is sound for this purpose.

**Navigability metrics** — the dimension neither A-MEM nor Notes Without Reasons measures empirically. These would test whether an agent can use the link structure to reason, not just retrieve. Possible measures:

- *Hop cost*: how many links must an agent follow to reach relevant content from an arbitrary starting point? Lower is better, but only if the hops are informative (the agent learns something at each step, not just that it took a wrong turn).
- *Pruning accuracy*: can an agent correctly predict whether a link is worth following based on the link's metadata alone, without following it? This directly tests whether links carry enough reason to support decision-making.
- *Trust calibration*: does the agent's confidence in link quality match actual link quality? In a system with noisy links, an agent should develop low trust; in a system with curated links, high trust. The pathological case Notes Without Reasons describes is low trust in a mixed system where noise buries signal.
- *Reasoning chain coherence*: when an agent follows a multi-hop path, does the resulting chain of reasoning make structural sense? Or do hops jump between unrelated topics connected only by vocabulary overlap?

An evaluation framework that scored both retrieval accuracy and navigability would make the trade-off concrete and measurable rather than theoretical.

## The vocabulary gap: accretion versus curation

A-MEM's operation vocabulary tells us what it can and cannot do to knowledge.

**A-MEM's vocabulary: construct, link, evolve, retrieve.** All four operations are accretive — they add or augment but never subtract. "Construct" creates a new note. "Link" connects it to existing notes. "Evolve" updates context and tags of existing notes when new memories arrive. "Retrieve" surfaces memories for questions. Even "evolve," the most sophisticated operation, only strengthens or contextualizes — it never splits, merges, retires, or fundamentally reorganizes.

**The boiling cauldron vocabulary: extract, split, synthesise, relink, reformulate, regroup, retire.** This vocabulary includes curation operations that reduce, restructure, and remove. "Split" breaks a compound note into atomic claims. "Synthesise" creates a new note that says something neither source said alone. "Retire" removes artifacts that have outlived their usefulness. "Regroup" proposes organizational structures that do not yet exist. These are destructive and constructive in ways that A-MEM's vocabulary is not.

**What the gap tells us.** The gap is not just a feature list difference — it reflects a deeper architectural assumption. A-MEM treats memory as monotonically growing: new memories arrive, get connected, and evolve context, but nothing is ever removed, split, or fundamentally restructured. This is sufficient for the conversational QA benchmarks it targets, where the task is remembering what was said, not organizing knowledge for future reasoning.

The boiling cauldron vocabulary assumes that knowledge organization is itself a form of knowledge — that the act of splitting a compound claim, synthesizing two notes into a third, or retiring an obsolete grouping creates value that mere accumulation cannot. This is the curation hypothesis: a well-organized knowledge base with fewer, sharper notes and more precisely articulated links outperforms a larger, noisier one, at least for navigability.

A-MEM's success on retrieval benchmarks does not test this hypothesis because retrieval does not require organizational clarity — it only requires that the right memory be somewhere in the top-k nearest neighbors. The curation hypothesis would be tested by navigability evaluations that reward an agent for traversing a reasoning chain, not just for surfacing a correct answer.

## The underlying question

The real question these three sources circle is whether automated knowledge systems need to do curation or whether accumulation with embedding-based linking is sufficient. A-MEM says accumulation works for retrieval. Notes Without Reasons says accumulation degrades navigability. The open-problem note says curation is the part we cannot yet automate because it requires judgment.

If the system only needs to answer questions, A-MEM's approach may be sufficient and its efficiency advantages (85-93% fewer tokens per operation) are compelling. If the system needs to support an agent's ongoing reasoning — letting it build arguments, trace implications, discover tensions — then the link infrastructure needs to carry reasons, and the operation vocabulary needs to include curation. These are genuinely different system goals, not a disagreement about methods.

The pragmatic path forward is probably both: embedding-based retrieval for question-answering (where speed and coverage matter) layered with curated propositional links for navigation (where precision and trust matter). The open question is whether these two layers can coexist without the noise from the first degrading the signal in the second — which is exactly the credibility erosion problem Notes Without Reasons identifies.
