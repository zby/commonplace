---
description: Proposes that discovery has a dual structure — positing a new general concept while recognizing existing particulars as instances of it — and that similarity-based connections vary by abstraction depth (shared feature → shared structure → generative model), not link kind. Scoped to similarity connections; contrastive and causal links are a different axis.
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: seedling
---

# Discovery is seeing the particular as an instance of the general

A common framing in Zettelkasten-adjacent writing contrasts "topical" linking (filing by category) with "semantic" or "mechanistic" linking (connecting by shared deep structure). The claim is that topical linking produces no surprise — you open the economics drawer and find economics — while mechanism-based linking engineers serendipity.

This framing is useful but the dichotomy is false — at least for connections based on shared structure. Topic and mechanism are not different *kinds* of similarity link. They are the same cognitive operation — recognizing similarity — applied at different depths of abstraction. Topic is shallow recognition (these are both about economics). Mechanism is deeper (these both describe systems that degrade under structural overload). But once you *see* the shared mechanism, linking by it is exactly as easy as linking by topic. The bottleneck is never the linking. The bottleneck is the *recognition*.

(This analysis covers similarity-based connections — the axis from surface resemblance to deep structural analogy. Knowledge systems also need contrastive links (contradicts, supersedes), causal links (caused, enabled), and temporal links (preceded). Those aren't similarity at any depth; they're different relationship types. The hierarchy below applies to the similarity axis specifically.)

This matters because [controlled disorder engineers serendipity through semantic rather than topical linking](./related-systems/arscontexta.md) gets the prescription slightly wrong. Luhmann's actual move wasn't "link by mechanism instead of topic." It was **link by judgment instead of category**. A filing cabinet uses pre-determined classification. Luhmann's Zettelkasten replaces that with individual decisions: THIS note connects to THAT note for THIS specific reason. The reason might be topical, mechanistic, analogical, or contrastive — what matters is that a human judged the connection worth making and articulated why.

## The dual structure of discovery

Discovery — whether in mathematics, science, or a knowledge base — has a dual structure that can't be decomposed:

1. You **posit something general** that didn't previously exist as a named concept
2. You **simultaneously recognize** that things you already knew are *instances* of it

The general doesn't exist until you see the particular as an instance of it. And the particular wasn't legible as an instance until you posited the general. They co-arise.

### Mathematical lemma extraction

A mathematician has Theorem A and Theorem B, apparently unrelated. She notices the proofs share structure — similar moves, similar appeals. She extracts the common structure as a Lemma. The Lemma is a *new node* in the knowledge graph that didn't exist before. Both theorems now link to it, and the link is both factual (they depend on it) and illuminating (seeing the shared foundation changes understanding of both).

Category theory takes this to its logical extreme — abstracting so aggressively that group theory and topology become instances of the same structure. The abstraction makes the similarity *nameable*, and once named, recognizing further instances becomes cheap.

### Darwin's theory of evolution

Darwin took four observations that were separately unremarkable — variation exists, more offspring are born than survive, traits are heritable, environment exerts pressure — and saw that taken together as axioms, they produce a theorem: populations adapt over time. Each observation was known to breeders, Malthus, naturalists. Nobody was hiding information. The creative act was seeing that these statements from different domains are premises of the same argument.

Crucially, Darwin proposed the model *without knowing the mechanism of any of its components*. He didn't know what generates variation (mutations), how heredity works (DNA), or the biochemistry of selection pressure. The model operates at a level of abstraction *above* all those mechanisms. It says: I don't care *how* variation is produced, only *that* it exists. Given these abstract properties, adaptation follows necessarily.

This is mathematical in its core. Evolution by natural selection is a theorem about any system satisfying those axioms — which is why the same logic appears in genetic algorithms, immune system antibody selection, market competition, and cultural evolution. The empirical work was necessary not to prove the theorem but to **identify the right axioms**. The Galapagos finches didn't prove natural selection; they showed Darwin which abstract properties to attend to.

Darwin's move goes beyond lemma extraction: he didn't just find shared structure, he proposed a **generative model** — an abstract machine that *produces* the observed phenomena as outputs. The model explains why the similarity exists and predicts where else it should appear.

### Fleming's discovery of penicillin

This feels different — a contaminated petri dish, mold killing bacteria. Where's the "extraction"? But other microbiologists had seen mold contamination. Some had probably seen inhibition zones. Fleming's contribution was recognizing that this specific anomaly *could be* an instance of something general — that there might exist a category of substances that could be extracted, purified, and used therapeutically.

But the dual structure is less clean here than in the mathematical case. Fleming's initial recognition was narrow: this mold produces something that kills bacteria, and that's worth investigating. The full general category — antimicrobials as a therapeutic class — crystallized gradually over the next decade through the work of Florey, Chain, and others. The particular and the general didn't co-arise in a single moment; the particular prompted a *direction* and the general emerged through sustained work. Fleming's case shows the dual structure stretched across time and multiple contributors, not the tight simultaneity of lemma extraction.

## Three depths of abstraction in connection

These examples suggest a hierarchy of connection depth:

| Depth | Operation | Example | Power |
|-------|-----------|---------|-------|
| **Shared feature** | Name a surface similarity | "Both involve capacity limits" | Descriptive — organizes but doesn't explain |
| **Shared structure** | Extract a common pattern | The lemma; "both follow: load → graceful degradation → threshold → catastrophic failure" | Structural — reveals form but not cause |
| **Generative model** | Propose an abstract machine that produces both phenomena | Natural selection; "both are outputs of: systems that optimize for efficiency under normal load sacrifice resilience to overload" | Explanatory — explains why the similarity exists and predicts new instances |

Each level subsumes the previous. A generative model implies shared structure implies shared features. But they're increasingly powerful, increasingly hard to discover, and increasingly epistemically risky. A shared feature is easy to verify or refute. A generative model can be compellingly wrong — phlogiston, caloric theory, and luminiferous ether were all generative models that unified diverse phenomena under a single abstract machine, and all turned out to be false. The power of deep abstraction and its epistemic fragility are the same property: the model explains so much that disconfirming evidence can always be accommodated until the whole edifice collapses at once.

## The discovery problem

The hard problem in knowledge systems is not *linking* (once you see a connection, articulating it is straightforward) but *recognition* — seeing that two things share structure at some level of abstraction.

Recognition cost scales with abstraction depth:
- Surface similarity (topic): cheap. Embeddings, keywords, filenames get you there.
- Structural similarity (pattern, proof technique): expensive. Requires understanding what a note is really about, then comparing that understanding across notes.
- Generative similarity (shared causal process): very expensive. Requires not just comparing but *inventing the dimension along which the comparison becomes visible*.

The mathematical tradition offers a partial solution: **develop vocabulary for naming structures**. Once a structure has a name (a lemma, a category, an algebraic property), recognizing new instances of it becomes cheap. The naming amortizes the discovery cost. In a knowledge system, this means the highest-value act isn't linking two notes that share a mechanism — it's **creating a new note that names the mechanism**. Once you have a note titled "Systems degrade when you exceed their structural capacity," linking cognitive load and architecture to it is trivial. The hard creative work was seeing the pattern and giving it a name.

## Open Questions

- Can you build practices that push connections from "shared feature" toward "generative model"? The [elaborative encoding requirement](./related-systems/arscontexta.md) pushes from bare adjacency to articulated connection. Is there an equivalent push toward deeper abstraction?
- Two distinct discovery problems get conflated: (1) noticing that existing notes share structure (O(N^2) comparison), and (2) inventing the abstraction that makes the similarity visible (genuine theoretical creativity). These probably need different system support. LLMs might help with (1); (2) is less clear.
- The hierarchy (feature → structure → generative model) maps loosely onto the [three levels of concreteness in the Alexander note](./alexander-patterns-and-knowledge-system-design.md) (patterns as document types → generative processes → centers strengthening centers). Is this the same axis, or just a coincidence of having three levels?

---

Relevant Notes:

- [arscontexta](./related-systems/arscontexta.md) — refines: the "controlled disorder" claim is right about judgment-based linking but the topic-vs-mechanism framing is a false dichotomy
- [Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md) — extends: the adjacency-vs-connection distinction maps to recognition depth, not link kind
- [alexander-patterns-and-knowledge-system-design](./alexander-patterns-and-knowledge-system-design.md) — parallels: the three levels of concreteness in that note (document types → generative processes → centers) may map to the feature/structure/generative-model hierarchy
- [stabilisation](./stabilisation.md) — suggestive parallel: the stabilisation spectrum (constraint strength) and the discovery hierarchy (abstraction depth) are both gradients where each step trades generality for power, though they operate on different axes
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — grounds: the recognition cost hierarchy maps to computational bounds on structure extraction (epiplexity)

Distilled into:

- [/connect skill](../instructions/connect/SKILL.md) — the "name the mechanism" insight is operationalized as abstraction opportunity logging in Phase 5 reflection

Topics:

- [learning-theory](./learning-theory.md)
