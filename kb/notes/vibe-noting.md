---
description: Vibe coding works because code is inspectable, not just verifiable — a KB adds that same inspectability to knowledge work, enabling a similar flywheel for reasoning
type: note
traits: []
areas: [kb-design]
status: seedling
---

# Vibe-noting

Vibe coding works with LLMs not just because code has hard oracles (tests pass or fail) but because code is a **stored, structured, inspectable artifact**. A stateless agent starting a new session can read the codebase, orient itself, and build on what's there. The oracles help verify, but the artifact itself enables continuity.

Most knowledge work doesn't produce artifacts like that. Decisions live in Slack threads, reasoning evaporates after meetings, analysis sits in documents nobody can navigate. An LLM starting a new session has nothing to read, so it can't orient — every session starts from zero.

A knowledge base adds exactly that missing layer: structured, linked, readable artifacts for knowledge work. Notes are to reasoning what code files are to implementation — persistent state an agent can inspect, understand, and build on. You don't need to plan every note perfectly, you just need to keep writing and linking, and the accumulated structure makes each subsequent session more productive — the same flywheel that makes vibe coding work.

## The tension with verification

There's a connection to [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md): code has hard oracles (tests) which is why it *automates*. A KB has weaker oracles (is this connection right? is this synthesis good?) — so vibe-noting might enable productive *augmentation* without crossing to automation. But that may be the point: a KB doesn't need to automate knowledge work, it needs to make augmentation dramatically better.

This suggests two independent axes for LLM-assisted work:
- **Inspectability** — can the agent orient itself? (enables continuity across sessions)
- **Verifiability** — can the agent check its own output? (enables automation)

Code scores high on both. Knowledge work without a KB scores low on both. A KB raises inspectability without necessarily raising verifiability — and that may be sufficient for a qualitative improvement in augmentation.

## Origin: conversation transcript

The idea emerged during a triage of `kb/log.md` and the writing of the [automation/verification boundary](./the-boundary-of-automation-is-the-boundary-of-verification.md) synthesis note. The conversation that produced it:

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

The note itself is an example of what it describes: an insight that emerged in conversation, captured as a structured artifact so a future session can find it, orient from it, and build on it.

---

Relevant Notes:

- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — tension: code automates because it's verifiable; a KB improves augmentation because it's inspectable; these are independent axes
- [agent-statelessness-means-harness-should-inject-context-automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — foundation: the inspectability a KB provides is exactly what stateless agents need for orientation
- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — extends: vibe-noting is the augmentation path while full automation remains blocked on oracle construction
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — relates: the workshop layer is where vibe-noting happens; the library is where its outputs accumulate

Topics:

- [kb-design](./kb-design.md)
