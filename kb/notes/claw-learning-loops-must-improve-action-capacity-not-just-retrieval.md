---
description: A Claw learning loop must target contextual competence (execution, classification, planning, communication), not just retrieval accuracy — question-answering is one mode among many
type: kb/types/note.md
traits: []
tags: []
status: seedling
---

# Claw learning loops must improve action capacity not just retrieval

## The narrow framing

The [KB learning loop note](./automating-kb-learning-is-an-open-problem.md) frames KB value as "question-answering capacity" — a note is valuable if it helps answer a question. But a [Claw](https://simonwillison.net/2026/Feb/21/claws/) — an AI-assisted system that accumulates context and evolves with use — does more than look things up.

## What a Claw actually does

A Claw acts on behalf of the user. The accumulated context — notes, decisions, indexes, conventions — doesn't just make answers findable, it makes the agent's *actions* more competent. At least these modes benefit from accumulated context:

- **Execution** — carrying out multi-step tasks (writing code, editing files, running scripts) using knowledge of project conventions, past approaches, and tool capabilities. The KB holds the operational knowledge that makes execution reliable rather than naive.
- **Classification** — routing incoming items based on accumulated judgment about categories, priorities, the user's preferences. The KB holds the criteria and precedents.
- **Communication** — drafting responses that reflect the user's voice, values, and relationship context. The KB holds the style, the stance, the history.
- **Planning** — decomposing goals into steps using knowledge of what's worked before, what constraints exist, what resources are available. The KB holds the operational memory.
- **Pattern recognition** — noticing when something incoming resembles a past situation and surfacing relevant precedent. The KB holds the case library.

You *can* frame each of these as answering a question ("What category does this belong to?" "What would I say to this?"), but that stretches the concept past usefulness. The common thread is **contextual competence**: the ability to act appropriately given accumulated knowledge about the domain, the user, and the project.

## What changes for the learning loop

If the KB's value is action capacity rather than retrieval accuracy, the learning loop needs different knowledge types, different mutations, and different evaluation — in roughly that order of difficulty.

**Knowledge types.** A retrieval-oriented KB stores facts and relationships. An action-oriented KB also needs to store things like:
- **Preferences** — how the user wants things done, not just what's true
- **Procedures** — workflows and sequences, not just reference material
- **Judgment precedents** — past decisions and their reasoning, so future similar cases can be handled consistently
- **Voice and style** — patterns in how the user communicates, enabling the agent to act as a credible proxy
- **Domain models** — structured representations of entities and relationships in the user's domain (e.g., "a PR belongs to a branch belongs to a repo") that enable correct reasoning about domain structure

This list is illustrative, not exhaustive. [Koylanai's Personal Brain OS](https://x.com/koylanai/status/2025286163641118915) — a single practitioner's self-reported system — appears to store several of these: voice guides for style, AGENT.md decision tables for procedures, decision/failure logs for precedents, and values/goals YAML for preferences. This is anecdotal evidence, but it suggests that practitioner-built Claws converge on action-oriented knowledge types even without a theoretical framework for why.

The current [available types](../reference/available-types.md) system — base types like `note`, `spec`, `review` — is oriented around structural properties of reference knowledge. If the KB grows to store action-oriented knowledge, the type system may need to accommodate content whose value is "enabling correct action" rather than "answering questions."

**Mutations.** The [boiling cauldron](./automating-kb-learning-is-an-open-problem.md) proposes extract, split, synthesise, relink, reformulate, regroup, retire — mostly oriented around findability and structure, though synthesise is generative (creates new knowledge) and retire is maintenance. An action-oriented system might also need mutations like:
- **Codify preference** — turn an observed pattern in user decisions into an explicit rule
- **Capture procedure** — extract a workflow from repeated actions
- **Consolidate precedents** — when several past decisions on similar cases exist, extract the underlying policy

**Evaluation.** This is the hard part. "Did it answer correctly?" has a relatively clear signal. "Did it act appropriately?" is harder to measure, more dependent on user judgment, and the feedback loop is slower — you may not know an action was wrong until much later. The [KB learning loop](./automating-kb-learning-is-an-open-problem.md) already identifies evaluation as the hardest open problem; broadening from retrieval to action makes it harder still. The usage that matters isn't just queries and failed retrievals — it's the full range of agentic actions: classifications made, communications drafted, plans executed. The feedback signal is richer but also noisier.

## The retrieval frame isn't wrong, just partial

The [KB learning loop note](./automating-kb-learning-is-an-open-problem.md) is internally coherent and its analysis of the retrieval-oriented learning problem is sound. This note argues that retrieval learning is one layer of a larger system. What transfers directly from the retrieval layer to the action layer:

- The **boiling cauldron** loop structure — propose mutations, evaluate, iterate. The action layer needs different mutation types (codify preference, capture procedure, consolidate precedents) but the loop itself is the same.
- **Quality gates** — action-oriented artifacts need quality criteria too, though the criteria differ (preference consistency, procedure effectiveness rather than retrieval accuracy).
- **Surfacing rate** as a health metric — if accumulated action knowledge doesn't improve agent behavior, the learning loop isn't working.

What doesn't transfer is the evaluation model, as described above. That's where the action layer becomes a genuinely different (and harder) problem.

## Open Questions

- How do you capture feedback on actions? Query logs are comparatively simple; action outcome logs require knowing what "success" means for each action type.
- Is the action layer's learning loop decomposable into domain-specific sub-loops (one for classification, one for communication, etc.) or is it irreducibly holistic?
- Does the [three-space memory model](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) help here? Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice — suggesting each space might have its own learning dynamics.
- The [predicted failure modes](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) of flat memory — operational debris polluting search, identity scatter, insights trapped in session state — are exactly what you'd expect when action-oriented knowledge types are forced into a retrieval-oriented structure. This is circumstantial evidence for the claim.
- [Constraining](./definitions/constraining.md) frames system-level adaptation as artifact accumulation. The action layer's learning loop would need the same framework but applied to different artifact types — preference codifications, procedure captures, precedent consolidations — rather than the note/link mutations the boiling cauldron describes.

---

Relevant Notes:

- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — the retrieval-oriented learning loop analysis; this note argues it's one layer of a broader problem
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — addresses the retrieval layer's evaluation with a composite oracle from structural and LLM-hybrid signals; the action layer would need different signals entirely (preference consistency, procedure effectiveness, precedent alignment)
- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — the three memory spaces may map to different learning dynamics: semantic (knowledge), procedural (operations), episodic (self/preferences)
- [flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — the predicted failures of flat memory are symptoms of forcing action-oriented knowledge into a retrieval-oriented structure
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — the current scenario set is retrieval-oriented; an action-oriented framing would add classification, communication, and planning scenarios
- [koylanai-personal-brain-os (ingest)](https://x.com/koylanai/status/2025286163641118915) — exemplifies: a practitioner-built Claw that already stores preferences, procedures, judgment precedents, and voice as distinct knowledge types
- [deploy-time-learning](./deploy-time-learning-is-the-missing-middle.md) — grounds: the artifact-accumulation model of learning applies, but action-oriented learning needs different artifact types than note/link mutations
- [available types](../reference/available-types.md) — implication: current document types are structured for reference knowledge; action-oriented knowledge types may not fit the existing base types
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — concretizes: workshop documents (tasks, decision threads, experiments) are the action-oriented artifacts that produce preferences, procedures, and precedents; the workshop→library extraction bridge is where action-capacity learning is harvested
- [brainstorming how to enrich web search](./brainstorming-how-to-enrich-web-search.md) — exemplifies: enriched web search is active research capacity — the agent discovers what it doesn't know rather than retrieving what it does, making it a concrete case of action beyond retrieval
