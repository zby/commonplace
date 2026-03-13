---
description: Vibe coding works because code is inspectable, not just verifiable — a KB adds that same inspectability to knowledge work, enabling augmentation even where automation is blocked on oracle construction
type: note
traits: []
tags: [kb-design]
status: seedling
---

# Vibe-noting

Vibe coding works with LLMs not just because code has hard oracles (tests pass or fail) but because code is a **stored, structured, inspectable artifact**. A stateless agent starting a new session can read the codebase, orient itself, and build on what's there. The oracles help verify, but the artifact itself enables continuity.

Most knowledge work doesn't produce artifacts like that. Decisions live in Slack threads, reasoning evaporates after meetings, analysis sits in documents nobody can navigate. An LLM starting a new session has nothing to read, so it can't orient — every session starts from zero.

A knowledge base adds exactly that missing layer: structured, linked, readable artifacts for knowledge work. Notes are to reasoning what code files are to implementation — persistent state an agent can inspect, understand, and build on. You don't need to plan every note perfectly, you just need to keep writing and linking, and the accumulated structure makes each subsequent session more productive — the same flywheel that makes vibe coding work. The flywheel can also compound negatively: poorly written or incorrectly linked notes can mislead a stateless agent, making orientation worse than starting fresh. The weak oracles that make KB automation hard (see below) also mean there's no cheap way to detect this degradation.

## The reverse-compression failure mode

The common failure mode of vibe-noting is [reverse-compression](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md): a human offers one sentence, the agent expands it into a full article grounded in its training knowledge, but the article carries no more [epiplexity](./information-value-is-observer-relative-because-extraction-requires-computation.md) than the original sentence. It reads like depth — paragraphs, structure, examples — but the LLM is just expanding a compact signal without adding extractable structure for the reader.

A KB that links notes to each other should resist this because each link can add information the original sentence didn't contain. The network, not the prose, is where epistemic complexity accumulates. But resistance is not automatic — see the [full analysis](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) for why links must be load-bearing, not decorative.

## The tension with verification

There's a connection to [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md): code has hard oracles (tests) which is why it *automates*. A KB has weaker oracles (is this connection right? is this synthesis good?) — so vibe-noting might enable productive *augmentation* without crossing to automation. But that may be the point: a KB doesn't need to automate knowledge work, it needs to make augmentation dramatically better.

This suggests two independent axes for LLM-assisted work (this framing is the note's own contribution — the boundary-of-automation note covers only the verification axis):
- **Inspectability** — can the agent orient itself? (enables continuity across sessions)
- **Verifiability** — can the agent check its own output? (enables automation)

Code scores high on both. Knowledge work without a KB scores low on both. A KB raises inspectability without necessarily raising verifiability — and that may be sufficient for a qualitative improvement in augmentation.

## Origin: process illustration

The idea emerged during a triage of `kb/log.md` and the writing of the [automation/verification boundary](./the-boundary-of-automation-is-the-boundary-of-verification.md) synthesis note. The conversation below produced the initial draft, which was then further processed through a semantic review that caught: the flywheel's negative-compounding risk, an overstated grounding claim, and a reversed link mapping. Those fixes are incorporated into the note above. The original conversation is preserved as an illustration of the vibe-noting process itself — an ephemeral exchange converted into a durable artifact.

> **User:** there is this idea that vibe coding works with llms - because the code is a stored artifact that at each new session can be inspected and the llm can orient itself. When doing other tasks the results are much less structured and it is harder to get any idea what is going on. A kb like ours adds this structure to more broad knowledge work - maybe we'll enable vibe-noting?
>
> **Agent:** That's a sharp observation. The insight is that vibe coding doesn't just work because code has hard oracles (tests) — it works because code is a stored, structured, inspectable artifact that lets a stateless agent orient itself at session start. The oracles help verify, but the artifact itself enables continuity.
>
> Most knowledge work doesn't produce artifacts like that. Decisions live in Slack threads, reasoning evaporates after meetings, analysis sits in documents nobody can navigate. An LLM starting a new session has nothing to read, so it can't orient — every session starts from zero.
>
> A KB like this one adds exactly that missing layer: structured, linked, readable artifacts for knowledge work. The notes are to reasoning what code files are to implementation — persistent state an agent can inspect, understand, and build on.
>
> The "vibe-noting" framing is nice because it captures something specific: you don't need to plan every note perfectly, you just need to keep writing and linking, and the accumulated structure makes each subsequent session more productive — the same flywheel that makes vibe coding work.
>
> There's a tension with the note we just wrote though: code has hard oracles (tests pass/fail) which is why it automates. A KB has weaker oracles (is this connection right? is this synthesis good?) — so vibe-noting might enable productive augmentation without crossing to automation. Which is actually the point: the KB doesn't need to automate knowledge work, it needs to make augmentation dramatically better.

The agent then drafted this initial version directly from the conversation:

> **Vibe coding** works with LLMs not just because code has hard oracles (tests pass or fail) but because code is a **stored, structured, inspectable artifact**. A stateless agent starting a new session can read the codebase, orient itself, and build on what's there. The oracles help verify, but the artifact itself enables continuity.
>
> Most knowledge work doesn't produce artifacts like that. Decisions live in Slack threads, reasoning evaporates after meetings, analysis sits in documents nobody can navigate. An LLM starting a new session has nothing to read, so it can't orient — every session starts from zero.
>
> A knowledge base adds exactly that missing layer: structured, linked, readable artifacts for knowledge work. Notes are to reasoning what code files are to implementation — persistent state an agent can inspect, understand, and build on. You don't need to plan every note perfectly, you just need to keep writing and linking, and the accumulated structure makes each subsequent session more productive — the same flywheel that makes vibe coding work.
>
> **The tension with verification:** code has hard oracles (tests) which is why it *automates*. A KB has weaker oracles — so vibe-noting might enable productive *augmentation* without crossing to automation. This suggests two independent axes: **Inspectability** (can the agent orient itself?) and **Verifiability** (can the agent check its output?). Code scores high on both. Knowledge work without a KB scores low on both. A KB raises inspectability without necessarily raising verifiability — and that may be sufficient for a qualitative improvement in augmentation.

A semantic review then caught: the flywheel's negative-compounding risk (bad notes mislead), an overstated grounding claim (the two-axes framework is this note's contribution, not grounded in the boundary-of-automation note), and a reversed link mapping (vibe-noting produces library artifacts, not workshop artifacts — though at steady state it shifts to workshops). Those fixes are incorporated into the note body above.

The note itself is an example of what it describes: an ephemeral exchange captured as a structured artifact, then refined through semantic review into something a future session can orient from.

---

Relevant Notes:

- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — tension: code automates because it's verifiable; a KB improves augmentation because it's inspectable; these are independent axes
- [agent-statelessness-means-harness-should-inject-context-automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — complements: that note solves orientation through harness injection; this note argues that artifact structure (inspectability) is the prerequisite that makes injection useful
- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — extends: vibe-noting is the augmentation path while full automation remains blocked on oracle construction
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: currently vibe-noting produces library artifacts directly because the KB is still being built; at steady state, vibe-noting shifts to workshops — rough captures that get consumed, refined, and promoted to library or discarded
