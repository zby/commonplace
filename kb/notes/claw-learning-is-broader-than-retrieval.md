---
description: A Claw's learning loop must improve action capacity (classification, planning, communication), not just retrieval — question-answering is one mode among many
type: note
traits: []
areas: [claw-design]
status: speculative
---

# Claw learning is broader than retrieval

## The narrow framing

The [KB learning loop note](./automating-kb-learning-is-an-open-problem.md) frames the KB's value as "question-answering capacity" — a note is valuable if it helps answer a question. This works as a model for a reference knowledge base, but project_claw is a [Claw](../sources/simon-willison-karpathy-claws.md): an AI-assisted system that accumulates context and evolves with use. The KB is its most developed subsystem, but the system's purpose is broader than lookup.

## What a Claw actually does

A Claw acts on behalf of the user. The accumulated context — notes, decisions, indexes, conventions — doesn't just make answers findable, it makes the agent's *actions* more competent. Concretely:

- **Classification** — routing incoming items based on accumulated judgment about categories, priorities, the user's preferences. The KB holds the criteria and precedents.
- **Communication** — drafting responses that reflect the user's voice, values, and relationship context. The KB holds the style, the stance, the history.
- **Planning** — decomposing goals into steps using knowledge of what's worked before, what constraints exist, what resources are available. The KB holds the operational memory.
- **Pattern recognition** — noticing when something incoming resembles a past situation and surfacing relevant precedent. The KB holds the case library.

You *can* frame all of these as answering a question ("What category does this belong to?" "What would I say to this?") but that stretches the concept past usefulness. The common thread isn't question-answering — it's **contextual competence**: the ability to act appropriately given accumulated knowledge about the domain, the user, and the project.

## What changes for the learning loop

If the KB's value is action capacity rather than retrieval accuracy, several things shift:

**Evaluation.** "Did it answer correctly?" becomes "Did it act appropriately?" — harder to measure, more dependent on user judgment, and irreducibly subjective in many cases. The [KB learning loop](./automating-kb-learning-is-an-open-problem.md) already identifies evaluation as the hardest open problem; broadening the scope makes it harder still.

**What counts as knowledge.** A retrieval-oriented KB stores facts and relationships. An action-oriented KB also needs to store:
- **Preferences** — how the user wants things done, not just what's true
- **Procedures** — workflows and sequences, not just reference material
- **Judgment precedents** — past decisions and their reasoning, so future similar cases can be handled consistently
- **Voice and style** — patterns in how the user communicates, enabling the agent to act as a credible proxy

[Koylanai's Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) already stores all four: voice guides and brand files for style, AGENT.md decision tables for procedures, decisions.jsonl and failures.jsonl for judgment precedents, and values/goals YAML for preferences. It demonstrates that practitioner-built Claws converge on action-oriented knowledge types even without a theoretical framework for why.

**Document types.** The current [document classification](./document-classification.md) system — base types like `note`, `spec`, `review` — is oriented around structural properties of reference knowledge. Preferences, procedures, and judgment precedents don't fit neatly into these categories. If the KB grows to store action-oriented knowledge, the type system may need to accommodate content whose value is "enabling correct action" rather than "answering questions."

**Mutation types.** The [boiling cauldron](./automating-kb-learning-is-an-open-problem.md) proposes extract, split, synthesise, relink, reformulate, regroup — all oriented around making knowledge more findable and better structured. An action-oriented system might also need:
- **Codify preference** — turn an observed pattern in user decisions into an explicit rule
- **Capture procedure** — extract a workflow from repeated actions
- **Consolidate precedents** — when several past decisions on similar cases exist, extract the underlying policy

**The "need more usage" conclusion still holds** — but the usage that matters isn't just queries and failed retrievals. It's the full range of agentic actions: classifications made, communications drafted, plans executed. The feedback signal is richer but also noisier.

## The retrieval frame isn't wrong, just partial

The [KB learning loop note](./automating-kb-learning-is-an-open-problem.md) is internally coherent and its analysis of the retrieval-oriented learning problem is sound. This note doesn't invalidate that — it argues that retrieval learning is one layer of a larger system. The boiling cauldron, quality gates, and surfacing rate problems all still apply to the retrieval layer. But the Claw needs a learning loop at the action layer too, and that's a different (harder) problem.

## Open Questions

- How do you capture feedback on actions? Query logs are comparatively simple; action outcome logs require knowing what "success" means for each action type.
- Is the action layer's learning loop decomposable into domain-specific sub-loops (one for classification, one for communication, etc.) or is it irreducibly holistic?
- Does the [three-space memory model](./three-space-agent-memory-maps-to-tulving-taxonomy.md) help here? Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice. Maybe each space has its own learning dynamics. The [predicted failure modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) of flat memory — operational debris polluting search, identity scatter, insights trapped in session state — are exactly what you'd expect when action-oriented knowledge types are forced into a retrieval-oriented structure.
- [Crystallisation as continuous learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) frames system-level adaptation as artifact accumulation. The action layer's learning loop would need the same framework but applied to different artifact types — preference codifications, procedure captures, precedent consolidations — rather than the note/link mutations the boiling cauldron describes.

---

Relevant Notes:
- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — the retrieval-oriented learning loop analysis; this note argues it's one layer of a broader problem
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — addresses the retrieval layer's evaluation with a composite oracle from structural and LLM-hybrid signals; the action layer would need different signals entirely (preference consistency, procedure effectiveness, precedent alignment)
- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — the three memory spaces may map to different learning dynamics: semantic (knowledge), procedural (operations), episodic (self/preferences)
- [three-space-memory-separation-predicts-measurable-failure-modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the predicted failures of flat memory are symptoms of forcing action-oriented knowledge into a retrieval-oriented structure
- [scenarios](./scenarios.md) — the current scenario set is retrieval-oriented; an action-oriented framing would add classification, communication, and planning scenarios
- [koylanai-personal-brain-os (ingest)](../sources/koylanai-personal-brain-os.ingest.md) — exemplifies: a practitioner-built Claw that already stores preferences, procedures, judgment precedents, and voice as distinct knowledge types
- [stabilisation-is-learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — grounds: the artifact-accumulation model of learning applies, but action-oriented learning needs different artifact types than note/link mutations
- [document-classification](./document-classification.md) — implication: current document types are structured for reference knowledge; action-oriented knowledge types may not fit the existing base types
- [a functioning claw needs a workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — concretizes: workshop documents (tasks, decision threads, experiments) are the action-oriented artifacts that produce preferences, procedures, and precedents; the workshop→library extraction bridge is where action-capacity learning is harvested
- [deep search is connection methodology applied to a temporarily expanded corpus](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) — exemplifies: deep search is active research capacity — the agent discovers what it doesn't know rather than retrieving what it does, making it a concrete case of action beyond retrieval

Topics:
- [claw-design](./claw-design.md)
