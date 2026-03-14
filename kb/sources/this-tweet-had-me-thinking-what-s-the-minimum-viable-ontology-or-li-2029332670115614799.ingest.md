---
description: Tweet thread proposing "minimum viable ontology" — the smallest term list to orient a newcomer in a domain — with a vibecoded prototype (domainmaps.co) and pedagogical framing via "conceptual thresholds"
source_snapshot: this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md
ingested: 2026-03-09
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

`/connect` confirmed the four connections from the previous ingest and discovered one new connection:

1. **[context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** — exemplifies: a minimum viable ontology is knowledge distilled to fit within context constraints. When doing deep work, you cannot load full domain methodology into the context window — so you compress it into the smallest vocabulary that still enables effective operation. This note already links back to this ingest file.

2. **[agent-statelessness-means-harness-should-inject-context-automatically](../notes/agent-statelessness-means-harness-should-inject-context-automatically.md)** — extends: domain maps address the human-facing version of the same problem. An agent needs vocabulary injected because it cannot carry it between sessions; a human entering a new domain needs that same vocabulary bootstrapped because they lack domain experience. Both identify "minimum viable vocabulary" as the enabler of effective operation.

3. **[discovery-is-seeing-the-particular-as-an-instance-of-the-general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)** — exemplifies: domain maps operationalize the insight that "once named, recognizing further instances becomes cheap." The "conceptual thresholds" concept is the pedagogical term for this phenomenon — names unlock recognition.

4. **[distillation](../notes/distillation.md)** — exemplifies: a domain map is a distillation — targeted extraction from the full body of domain knowledge into a focused artifact shaped by the specific circumstance of a newcomer. The rhetorical shift is expert-knowledge to orientation vocabulary.

5. **[information-value-is-observer-relative](../notes/information-value-is-observer-relative.md)** — exemplifies (NEW): MVO makes domain structure accessible to a bounded observer who lacks the computation to extract it from raw domain artifacts. The full domain knowledge contains the same information regardless of whether an MVO exists, but the bounded observer (human or agent entering a new domain) cannot extract that structure without the vocabulary bootstrap. MVO is a concrete instance of "deterministic transformation that adds zero classical information but makes structure accessible to bounded observers."

A synthesis opportunity emerged from the new connection: three notes together (information-value, discovery, distillation) imply a claim not yet captured — the minimum viable vocabulary for a domain is the set of names that, once acquired, maximally reduce the extraction cost for a bounded observer entering that domain. This frames MVO not as "what terms should I learn" but as an optimization problem over extraction cost for bounded observers.

## Extractable Value

1. **The "minimum viable ontology" framing** — a crisp name for the concept of identifying the smallest vocabulary that makes a domain navigable. We have the pieces (distillation, naming-as-bottleneck, vocabulary injection) but not this label. [quick-win]

2. **"Conceptual thresholds" as pedagogical grounding** — the tweet explicitly connects to threshold concept theory from education research. Worth investigating whether threshold concepts (Meyer & Land) have been formally studied in the context of AI prompting or domain onboarding for agents. [deep-dive]

3. **MVO as bounded-observer vocabulary bootstrap** — the new connection to information-value reframes MVO as an optimization problem: given a bounded observer and a domain, which names provide the greatest reduction in extraction cost? This is a synthesis that goes beyond the source itself but is enabled by the connection. [experiment]

4. **Domain maps as "skills for humans"** — the parallel between agent skills (distilled procedures) and domain maps (distilled vocabulary) is suggestive. Both are targeted distillations that enable operation in a domain without full understanding. [just-a-reference]

5. **AI-generated domain maps as generator/verifier pattern** — the prototype uses LLMs to generate the initial ontology, then envisions expert curation ("blessed by experts"). This is the generator/verifier pattern: AI generates candidates, experts verify and curate. [just-a-reference]

6. **Flat lists vs. graphs for vocabulary** — the design choice to use lists rather than knowledge graphs for simplicity. Relevant to our own index design decisions — flat directory indexes vs. structured topic graphs. [just-a-reference]

## Limitations (our opinion)

This is a conversation thread, so the checks focus on what is not argued:

- **No criteria for what makes a term "threshold."** The thread names the concept of "minimum viable ontology" but provides no framework for deciding which terms belong in it. Is 3D's MVO 10 terms or 100? What makes a term a threshold concept vs. merely useful vocabulary? The pedagogical literature on threshold concepts (Meyer & Land) does provide criteria (transformative, irreversible, integrative, bounded, troublesome), but the thread doesn't engage with them.

- **No evidence the prototype works.** The domainmaps.co tool is described as "vibecoded" and self-tested. There is no evaluation — no comparison of prompt quality with vs. without domain maps, no user study of onboarding speed, no expert evaluation of whether the AI-generated lists capture the right terms. The claim that this "helps" rests entirely on the author's subjective experience.

- **Conflates naming with explaining.** Having a list of terms is not the same as understanding a domain. The thread acknowledges this implicitly ("linked out to examples vs. bringing them in") but doesn't address whether term lists without explanations actually reduce the comprehension gap. Our note on [discovery](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) argues that naming amortizes discovery cost — but only if the name carries the right associations. A bare term list may not achieve this.

- **Selection of examples is editorial, not principled.** When asked how domains and term boundaries are chosen, the author responds "currently just an editorial decision, but could use a framework to think about." This is honest but means the prototype is an illustration of a concept rather than a validated method.

- **Unfalsifiable as stated.** "A curated term list helps you get oriented" is hard to disagree with, which is a sign the claim may not be saying enough to be wrong about. The interesting question — which terms, how many, and whether AI can identify them — is not addressed.

## Recommended Next Action

Write a note titled "Minimum viable vocabulary is the set of names that maximally reduces extraction cost for a bounded observer" connecting to [information-value-is-observer-relative](../notes/information-value-is-observer-relative.md), [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md), and [distillation](../notes/distillation.md) — it would argue that the pedagogical concept of "conceptual thresholds" and the tweet's "minimum viable ontology" are instances of bounded-observer extraction cost reduction, grounding an intuitive idea in the KB's information-theoretic framework.
