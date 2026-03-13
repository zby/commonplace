# Connection Report: Thread by @melodyskim (Minimum Viable Ontology / Domain Maps)

**Source:** [Thread by @melodyskim](../../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md)
**Date:** 2026-03-09
**Depth:** standard

**Note:** This is a raw source (`type: x-thread`, no frontmatter beyond capture metadata). An ingest file already exists at [this-tweet-had-me-thinking-...ingest.md](../../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md) with four connections previously identified. This report evaluates whether those connections hold and whether additional ones exist.

## Core Concepts

The source proposes "minimum viable ontology" (MVO) — the smallest set of terms needed to orient yourself in a new domain and improve prompts when working with AI. Key elements:
- **Conceptual thresholds** (pedagogical term) — vocabulary that, once acquired, unlocks domain comprehension
- **Domain maps** — curated term lists (not graphs) as orientation tools
- **AI-generated, expert-curated** — LLM generates initial maps, experts could "bless" them
- **"Skills for humans"** — parallels agent skills, but for human domain onboarding
- **Context for agents** — could steer agents toward correct domain-specific behavior

## Discovery Trace

**Index scan:**
- Read `../../notes/index.md` — scanned all 147 entries. Flagged candidates:
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — MVO is distillation under context pressure
  - [distillation](../../notes/distillation.md) — domain maps are targeted extraction of domain knowledge
  - [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — naming unlocks recognition
  - [agent-statelessness-means-harness-should-inject-context-automatically](../../notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — vocabulary injection for stateless agents
  - [information-value-is-observer-relative-because-extraction-requires-computation](../../notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — MVO makes domain structure accessible to bounded observers
  - [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — contextual competence through vocabulary
  - [agent-statelessness-makes-routing-architectural-not-learned](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — every session is "day one" parallels entering a new domain
  - [areas-exist-because-useful-operations-require-reading-notes-together](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) — areas as orientation scopes
  - [sift-kg](../../notes/related-systems/sift-kg.md) — schema discovery from sources
  - [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) — accumulation as learning

**Topic indexes:**
- Read [learning-theory](../../notes/learning-theory-index.md) — confirmed distillation and discovery as primary connection paths. No additional candidates beyond index scan.
- Read [related-systems-index](../../notes/related-systems/related-systems-index.md) — no direct candidate, but sift-kg's schema discovery parallels MVO generation.

**Semantic search (via qmd):**
- Query: "minimum viable ontology domain terms orientation getting situated new domain conceptual thresholds" on notes collection
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (93%) — already links to MVO ingest; strong, genuine connection
  - [areas-exist-because-useful-operations-require-reading-notes-together](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) (50%) — weaker; areas are KB-internal, MVO is domain-external
  - [thalo-type-comparison](../../notes/related-systems/thalo-type-comparison.md) (38%) — surface overlap on "types"; no semantic connection
  - [document-system](../../notes/document-system-index.md) (35%) — surface overlap on classification; no semantic connection
  - [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) (33%) — index boundary concept is structurally parallel but too abstract to be useful
  - Remaining results (33% and below): learning-theory, mechanistic-constraints, areas, Evans, discovery — either already flagged or too weak
- Query: "minimum viable ontology domain maps curated term lists skills for agents" on sources collection
  - [ingest report](../../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md) (93%) — self-match
  - [source itself](../../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md) (56%) — self-match
  - Other sources (45% and below): no genuine connections found in source collection beyond those already captured in ingest

**Keyword search:**
- `rg "ontology|vocabulary|terminology|onboarding|domain map|conceptual threshold" kb/notes/` — 19 files matched
  - Most matches are incidental vocabulary usage (e.g., "ontology" in Thalo comparison, "terminology" in various notes)
  - [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — uses "defined terms" as orientation vocabulary for legal domain; parallel to MVO
  - [agent-statelessness-means-harness-should-inject-context-automatically](../../notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — "vocabulary" matches; already flagged
- `rg "melodyskim|2029332670115614799" kb/` — confirmed source is referenced only from context-efficiency note and sources index

**Link following:**
- From context-efficiency note: followed links to frontloading, indirection, progressive disclosure. These are mechanisms for context efficiency but don't connect specifically to MVO's domain-orientation concept.
- From distillation note: followed links to constraining, skills-derive-from-methodology. Skills-as-distillation parallel is interesting but already captured in the ingest's "skills for humans" observation.
- From discovery note: the "once named, recognizing further instances becomes cheap" insight is the strongest conceptual match. MVO operationalizes this by bootstrapping the naming.

## Connections Found

The ingest file already identified four connections. After full discovery, I confirm all four and add one additional connection:

### Confirmed from ingest (with evaluation)

1. [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **exemplifies**: MVO is distillation under context-efficiency pressure — compress domain knowledge into the smallest vocabulary that fits the context window. This note already links to the ingest file with exactly this framing. The strongest connection; the note's architectural responses (progressive disclosure, frontloading) are the mechanism-level answers to the problem MVO solves at the vocabulary level. **Already linked from the context-efficiency note.**

2. [agent-statelessness-means-harness-should-inject-context-automatically](../../notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — **extends**: domain maps address the human-facing version of the same problem. An agent needs vocabulary injected because it cannot carry it between sessions; a human entering a new domain needs the same vocabulary bootstrapped. Both identify "minimum viable vocabulary" as the enabler of effective operation. The harness injection mechanism is specifically about definitions — and MVO is about identifying which definitions matter most.

3. [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — **exemplifies**: MVO operationalizes the insight that "once named, recognizing further instances becomes cheap." The "conceptual thresholds" concept is the pedagogical term for this phenomenon — names unlock recognition. The discovery note's claim that "naming structures amortizes discovery cost" is exactly what a domain map does for a newcomer.

4. [distillation](../../notes/distillation.md) — **exemplifies**: a domain map is a distillation — targeted extraction from the full body of domain knowledge into a focused artifact shaped by the specific circumstance of a newcomer needing orientation. The rhetorical shift is expert-knowledge to orientation vocabulary.

### New connection

5. [information-value-is-observer-relative-because-extraction-requires-computation](../../notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — **exemplifies**: MVO makes domain structure accessible to a bounded observer (a newcomer who lacks domain computation). The full domain knowledge contains the same information regardless of whether an MVO exists, but the bounded observer (human or agent entering a new domain) cannot extract that structure without the vocabulary bootstrap. MVO is a concrete instance of "deterministic transformation that adds zero classical information but makes structure accessible to bounded observers."

**Bidirectional candidates** (reverse link also worth adding):
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) <-> source — already linked from the note to the ingest file. The reverse link (source -> note) is implicit through the ingest.
- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) <-> source — the source gives a concrete external example of "naming amortizes discovery cost" that would strengthen the discovery note's case.

## Rejected Candidates

- [areas-exist-because-useful-operations-require-reading-notes-together](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) — areas are KB-internal operational scopes; MVO is about external domain orientation. The word "area" might map to "domain" but the mechanisms are different: areas optimize context loading for an existing KB, MVO bootstraps vocabulary for a domain the reader knows nothing about.
- [sift-kg](../../notes/related-systems/sift-kg.md) — sift-kg's "schema discovery" (ask LLM to design entity/relation types from document samples) is mechanistically similar to MVO generation (ask LLM to identify key terms from a domain). But the purposes diverge: sift-kg discovers schema for structured extraction, MVO discovers vocabulary for human orientation. Surface mechanism overlap without semantic depth.
- [agent-statelessness-makes-routing-architectural-not-learned](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — the "every session is day one" parallel is tempting but imprecise. Agent statelessness is about an agent that forgets between sessions; MVO is about a human (or agent) entering a genuinely unfamiliar domain. These are different problems (amnesia vs. ignorance) even if both produce "not oriented."
- [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — legal "defined terms" serve a similar orientation function (bootstrapping shared vocabulary), but the connection is too indirect. Legal defined terms constrain interpretation of a specific document; MVO bootstraps comprehension of an entire domain. The mechanisms share a surface shape but the scale and purpose differ.
- [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) — MVO is accumulated knowledge (low reach — domain-specific terms), but saying "MVO is accumulation" is too obvious to be useful as a link.
- [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — "contextual competence" is what MVO aims to bootstrap, but the synthesis note is about KB architecture, not domain onboarding. The connection would be "MVO is a tool for achieving contextual competence in a new domain" — true but generic.
- [two-kinds-of-navigation](../../notes/two-kinds-of-navigation.md) — domain maps could be seen as a navigation aid, but the note is about KB navigation modes (links vs search), not domain orientation.

## Index Membership

- No index membership recommended for the raw source. The ingest file is already listed in [sources/index.md](../../sources/index.md). Connections to KB notes are through the ingest file, not the raw source.
- The ingest file connects to areas: learning-theory (via distillation, discovery, information-value) and kb-design (via context-efficiency, agent-statelessness).

## Synthesis Opportunities

The ingest file already flagged one synthesis opportunity: **MVO = distillation under context-efficiency pressure**. After this discovery round, a sharper formulation emerges:

**MVO as bounded-observer vocabulary bootstrap.** Three notes together imply a claim not yet captured:
- [information-value-is-observer-relative](../../notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — structure is present but inaccessible to bounded observers
- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — naming amortizes discovery cost
- [distillation](../../notes/distillation.md) — targeted extraction for a specific context budget

Together these suggest: **The minimum viable vocabulary for a domain is the set of names that, once acquired, maximally reduce the extraction cost for a bounded observer entering that domain.** This frames MVO not as "what terms should I learn" but as an optimization problem: given a bounded observer (human or agent) and a domain, which names provide the greatest reduction in the computation needed to extract useful structure from domain artifacts?

This synthesis would be a note in `../../notes/`, not a source observation. It would ground the pedagogical concept of "conceptual thresholds" in the KB's information-theoretic framework.

## Flags

- The raw source (`x-thread` type, no frontmatter beyond capture metadata) is thin — a tweet thread with replies, no developed argument. The ingest file captures all extractable value. Future connections should link to the ingest file, not the raw source.
- No split candidate — the source makes one point (MVO concept) with limited elaboration.
