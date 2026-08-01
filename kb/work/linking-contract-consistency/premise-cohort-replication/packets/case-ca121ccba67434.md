# Case packet

Neutral case identifier: case-ca121ccba67434

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Agent context is constrained by soft degradation, not hard token limits

Agent context windows have two bounds: a hard token limit and a soft degradation surface. The hard limit is the maximum tokens the model accepts — exceed it and the API rejects the request. The soft bound is where performance silently degrades: missed instructions, shallow reasoning, ignored context — while output remains well-formed.

The soft bound is the binding constraint — performance degrades well before the hard limit is reached. What constrains work is not running out of tokens but the quality of what those tokens do, driven by at least three dimensions: volume, complexity, and relevance/interference. Other factors — information arrangement and prompt framing — also shift the degradation surface, often by changing one of these dimensions indirectly.

## Dimensions of the soft bound

### Volume

More tokens dilute attention. The "lost in the middle" finding ([Liu et al., 2023]) established primacy and recency bias — models overweight information near the beginning and end of the context, underweighting the middle. Because agent prompts face the same flat-sequence selection problem, this positional bias applies whenever the model must recover the right items from a long unscoped context. Anthropic (the AI lab) calls this **context rot** ([2025]). Paulsen's Maximum Effective Context Window (MECW) work confirms that usable context can be far below advertised windows and is task-dependent ([Paulsen, 2025]).

### Relevance/interference

Not all tokens are equal. Irrelevant context is not merely extra volume; it can actively interfere with task execution. GSM-DC, a math-reasoning benchmark with synthetic distractors, shows power-law error scaling with distractor count ([Yang et al., 2025]). The interaction with reasoning depth is the key signal: distractors hurt more as the task requires more dependent steps, and they degrade both reasoning path selection and arithmetic execution.

The same pattern appears at the agent-workflow level. Chung et al. find that injecting irrelevant task sequences into web-agent benchmarks collapses success rates from 40-50% to under 10% ([Chung et al., 2025]). The failures are not just slower retrieval from a larger context; agents loop, lose objectives, and treat stale history as live problem state. Bolt-on retrieval (iRAG) provides only modest improvement in that benchmark, which is weak but useful evidence that irrelevant context often needs to be excluded or scoped away rather than compensated for after loading.

This is why the mitigation is architectural. Summarization can shrink irrelevant material, but it does not by itself decide whether the material belongs in the active problem frame. Selective loading, scoped state, and sub-agent boundaries attack relevance/interference directly by preventing non-task state from competing with the task.

### Complexity

Some forms of context complexity add interpretation overhead. Every layer of [indirection costs context and interpretation overhead], and deeper compositional structure may impose similar costs. ConvexBench, a benchmark on compositional symbolic reasoning, shows complexity-driven collapse at low token counts: F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100, even though total tokens (5,331 at depth 100) were far below context limits ([Liu et al., 2026]). The shared mechanism is that both agent operations and symbolic reasoning fail when the model must carry many intermediate dependencies without scoped subproblems or externalized state. Compositional depth, not volume, was the bottleneck.

### Open questions

Volume, complexity, and relevance/interference are distinguishable but not fully separable — reducing volume often reduces complexity and interference as side effects.

The main unresolved question is interaction, not existence. GSM-DC cleanly shows that distractor count and reasoning depth interact in synthetic math problems; web-agent benchmarks show an agent-level analogue under long multi-session histories. We do not yet know how stable the interaction surface is across natural-language tasks, partially relevant material, or different model families.

## The soft bound is invisible

The hard limit is visible — exceed it and the API returns an error. The soft bound is invisible at every level.

**To the practitioner.** The model doesn't signal when it crosses the soft bound. Output remains well-formed; problems surface downstream. A CPU signals overflow. A human says "I'm confused." An LLM produces fluent output whether it reflects the supplied context or leaves large portions unused.

**To the benchmarker.** The soft bound is not a single number. It shifts with task type, compositional depth, relevance mix, information arrangement, and prompt framing. Model updates shift the degradation surface without notice.

**To the market.** Providers advertise hard token limits because those are clean, comparable numbers. They don't publish soft degradation surfaces — those are task-dependent and hard to characterize. The number on the box describes the bound that rarely binds; the bound that actually constrains work has no number.

## Consequences

**Don't trust the number on the box.** Usable context depends on what you're doing, how you arrange it, and which model version you're running.

**Silent degradation makes heuristic design rational.** Front-loading critical content, decomposing complexity, isolating scopes, compressing aggressively, and excluding irrelevant state are the rational strategy, not a placeholder until better measurement arrives. This is how [surveyed traditions facing soft bounds] have operated.

**Programmatic constructability is the genuine advantage.** You can programmatically choose every token that enters the context. This creates a distinctive tension: **high control over inputs, low observability of effective processing.** The engineering opportunity is real, but it must be exercised against a bound you cannot directly observe. Default-loading session history is the most common way this advantage goes unexercised — [session history should not be the default next context]. The [heaviest-fork feasibility note] extends these consequences to work split across sub-agents.

---

Relevant Notes:

- [Context efficiency is the central design concern] — **extends**: ranks this note's soft-bound claim as the binding feasibility face of context scarcity
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget] — extends (KB-internal conjecture, not benchmarked): proposes failure workarounds as a further load source on this soft bound — defects in interpreted artifacts converting into per-encounter re-routing load — argued from mechanism and two worked instances, unlike the measured dimensions above
- [On the "Induction Bias" in Sequence Models (Ebrahimi et al., 2026)] — candidate mechanism (volume dimension): transformers learn largely length-specific solutions in isolation and show much weaker sharing when lengths are mixed
  - Caveat: training-time evidence on synthetic tasks, not direct measurement of inference-time context degradation
- [GSM-DC ingest] — exemplifies (relevance/interference dimension): power-law error scaling with distractor count in math reasoning, with reasoning-depth interaction
- [Web agent benchmark ingest (Chung et al., 2025)] — exemplifies (relevance/interference dimension): agent-level catastrophic degradation from injected irrelevant task sequences; iRAG provides only modest relief
- [ConvexBench ingest] — exemplifies (complexity dimension): compositional depth collapse at low token counts
- [Paulsen MECW] — exemplifies (volume dimension): usable context drastically below advertised windows, task-dependent

## Artifact B

# Information value is observer-relative

What makes information valuable is not a property of the data alone but of the data-observer pair: the observer's prior knowledge, computational capacity, available tools, and goals all determine what they can extract.

## Prior work

Observer-relative information value is not a new idea. Several traditions have developed it independently:

- **Relevance theory** (Sperber & Wilson, 1986) — information is relevant when it connects with existing assumptions to yield cognitive effects. Relevance is defined relative to the individual's cognitive environment, not as a property of the message.
- **Value of information in decision theory** (Marschak, Radner) — information has value only if it changes a decision. Two agents facing different decisions assign different value to the same data, even with identical processing capacity.
- **Bounded rationality** (Simon) — decision-makers have limited computational capacity, so they satisfice rather than optimize. The value of information depends on processing capacity, not just content.
- **Bayesian decision theory** — the expected improvement from observing data depends on the observer's prior beliefs and utility function.

Classical information theory (Shannon, Kolmogorov) is the exception — it deliberately abstracts away the observer. Shannon entropy measures surprise given a probability model; Kolmogorov complexity measures the shortest generating program. Neither depends on who is observing. This abstraction is powerful for communication engineering but misses what matters for knowledge systems: the same content in a different arrangement can teach more, even though nothing changed by classical measures.

**TODO:** This literature survey is from the agent's training data, not systematic. Revisit with deep search once that capability is operational — there are likely more relevant traditions (philosophy of information, situated cognition) and specific results worth ingesting.

## Why this matters for the KB

The idea is well-established in other fields. What's specific to our context is applying it to the design of an agent-operated knowledge base, where the primary reader is an agent under [bounded context] — every token loaded must earn its place.

### What to keep

Observer-relativity shapes inclusion decisions. A note's value depends on whether the agent can connect it to what it already has in context — an isolated fact is worth less than a design principle that links to five other notes, because the principle creates extraction opportunities across sessions. This is why [KB goals] matter: they define what the observer is trying to do, which determines what counts as valuable.

Observer-relativity also determines resolution. The minimum required retained natural-language content is the gap between what its target use requires and what its intended consumers can reliably contribute from parametric knowledge, loaded context, live inspection, tools, or reasoning. The gap may be:

- **Substance** the consumer lacks: facts, observations, arguments, or methods.
- **A connection the consumer will not reliably make:** a relation, recognition condition, or operation that activates otherwise familiar knowledge.
- **What reconstruction cannot preserve:** warrant, provenance, exact wording or membership, a governing version, or an authoritative local choice.

Reconstructability and activation are separate tests because [knowledge storage does not imply contextual activation] — a model may explain a framework perfectly when asked yet fail to recognize the present situation as an instance of it. Where the boundary falls — when a framework name plus a recognition condition suffices, and when tutorial, warrant, or exact content must remain — is developed in [the framework is often larger than the durable contribution], together with a behavioral test for it. The result depends on the consumer population: a cue that resolves for one model may fail for another, and a compact agent-facing note may be opaque to a first-time human. Self-containedness therefore means supplying what intended consumers need, not reproducing everything relevant to the topic.

### How to present

Several KB conventions are optimizations for the agent observer:

- **[Title as claim]** — a claim title lets the agent extract the main point without loading the note. It is a precomputed view for the lowest-cost reading: scanning titles in an index.
- **Descriptions as retrieval filters** — the description field exists because the agent needs to decide relevance before reading the full note. A good description reshapes the note for the "should I read this?" decision.
- **[Short composable notes]** — many short notes give more combinatorial coverage than few long ones for a reader with bounded context.
- **[Progressive refinement]** — each level (text → note → structured-claim) adds structure that makes the content more extractable. A structured claim with Evidence/Reasoning/Caveats is more accessible to an agent than the same argument in unstructured text.

More broadly, reshaping knowledge for a specific observer creates value. In information-theoretic terms this is lossy compression — it discards information. But for the target reader, the reshaped view can be more valuable than the source because it makes previously unreachable structure accessible. Multiple observer-shaped views of the same source aren't redundant — each targets a different observer.

### What observer-relativity doesn't help with

**[Discovery] cost is observer-relative** but not easily optimized — the data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. [Naming] is the partial solution: once a structure has a name, recognizing instances becomes cheap.

**[Reverse-compression] is the failure mode** — expanding text without adding extractable structure. More tokens, no more value for the reader.

## Open Questions

- Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?
- Is the agent the only important reader? Humans read the KB too — during review, when directing inquiry, when evaluating quality — and the KB is published on the web for external readers.
- What should we assume about the agent — a frontier model with strong reasoning, or a weaker model that needs more scaffolding? The answer shapes what counts as "accessible structure."

---

Relevant Notes:

- [Epiplexity paper] — related formalization: epiplexity captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity

## Under-review context phrase

observer-relativity is what makes the soft bound task-dependent
