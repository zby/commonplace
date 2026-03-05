---
source_snapshot: this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md
ingested: 2026-03-05
type: conversation-thread
domains: [domain-onboarding, vocabulary-bootstrapping, learning-theory, prompt-engineering]
---

# Ingest: Minimum Viable Ontology / Domain Maps

Source: this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md
Captured: 2026-03-05
From: https://x.com/melodyskim/status/2029332670115614799

## Classification
Type: conversation-thread — A tweet thread introducing a concept ("minimum viable ontology") with a vibecoded prototype (domainmaps.co), replies, and discussion. No developed argument or methodology.
Domains: domain-onboarding, vocabulary-bootstrapping, learning-theory, prompt-engineering
Author: @melodyskim — product/design practitioner who vibecoded the domainmaps.co prototype. Unknown depth of expertise, but the "conceptual thresholds" framing shows pedagogical awareness.

## Summary

Melody Kim proposes the idea of a "minimum viable ontology" — a curated list of key terms needed to quickly orient yourself in a new domain and improve your prompts when working with AI. She built domainmaps.co to showcase the concept, generating domain maps for areas like 3D graphics. She frames these in pedagogical terms as "conceptual thresholds" — the vocabulary that, once acquired, unlocks comprehension of a domain. In the replies, she notes these could function as "skills for humans" and hints they could also steer AI agents toward correct domain-specific behavior. The prototype uses AI-generated lists with links to examples, choosing flat lists over graphs for simplicity.

## Connections Found

/connect identified three genuine connections to the existing KB, plus a primary connection identified on review:

1. **[context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** — exemplifies: a minimum viable ontology is knowledge distilled to fit within context constraints. When doing deep work, you cannot load full domain methodology into the context window — so you compress it into the smallest vocabulary that still enables effective operation. This is progressive disclosure applied to domain knowledge: the MVO is the always-loaded layer, with full methodology available on demand.

2. **[agent-statelessness-means-harness-should-inject-context-automatically](../notes/agent-statelessness-means-harness-should-inject-context-automatically.md)** — extends: domain maps address the human-facing version of the same problem. An agent needs vocabulary injected because it cannot carry it between sessions; a human entering a new domain needs that same vocabulary bootstrapped because they lack domain experience. Both identify "minimum viable vocabulary" as the enabler of effective operation.

3. **[discovery-is-seeing-the-particular-as-an-instance-of-the-general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)** — exemplifies: domain maps operationalize the insight that "once named, recognizing further instances becomes cheap." The "conceptual thresholds" concept is the pedagogical term for this phenomenon — names unlock recognition.

4. **[distillation](../notes/distillation.md)** — exemplifies: a domain map is a distillation — targeted extraction from the full body of domain knowledge into a focused artifact shaped by the specific circumstance of a newcomer. The rhetorical shift is expert-knowledge to orientation vocabulary.

A synthesis opportunity was flagged: these notes together suggest that a minimum viable ontology is what you get when you apply distillation under context-efficiency pressure — compress domain knowledge into the smallest set of terms that still enables effective operation within a finite context window.

## Extractable Value

1. **The "minimum viable ontology" framing** — a crisp name for the concept of identifying the smallest vocabulary that makes a domain navigable. We have the pieces (distillation, naming-as-bottleneck, vocabulary injection) but not this label. [quick-win]

2. **"Conceptual thresholds" as pedagogical grounding** — the tweet explicitly connects to threshold concept theory from education research. Worth investigating whether threshold concepts (Meyer & Land) have been formally studied in the context of AI prompting or domain onboarding for agents. [deep-dive]

3. **Domain maps as "skills for humans"** — the parallel between agent skills (distilled procedures) and domain maps (distilled vocabulary) is suggestive. Both are targeted distillations that enable operation in a domain without full understanding. [just-a-reference]

4. **AI-generated domain maps as a practical tool** — the prototype uses LLMs to generate the initial ontology, then envisions expert curation. This is the generator/verifier pattern from our KB: AI generates candidates, experts verify and curate. [just-a-reference]

5. **Flat lists vs. graphs for vocabulary** — the design choice to use lists rather than knowledge graphs for simplicity. Relevant to our own index design decisions — flat directory indexes vs. structured topic graphs. [just-a-reference]

## Recommended Next Action

File as reference. The "minimum viable ontology" label names the intersection of distillation and context-efficiency pressure — compress domain knowledge into vocabulary that fits the context window. The source itself is thin (a tweet thread with a prototype), but the concept connects cleanly to existing KB architecture: progressive disclosure, context loading strategy, and frontloading are all mechanisms for achieving minimum viable context loads, and MVO applies the same logic to domain knowledge rather than system instructions.
