# Discovery examples — working material

Extended examples illustrating the dual structure of discovery and the three depths of abstraction. These are raw observations, not yet processed into structured claims. Source material for [discovery is seeing the particular as an instance of the general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md).

## Mathematical lemma extraction

A mathematician has Theorem A and Theorem B, apparently unrelated. She notices the proofs share structure — similar moves, similar appeals. She extracts the common structure as a Lemma. The Lemma is a *new node* in the knowledge graph that didn't exist before. Both theorems now link to it, and the link is both factual (they depend on it) and illuminating (seeing the shared foundation changes understanding of both).

Category theory takes this to its logical extreme — abstracting so aggressively that group theory and topology become instances of the same structure. The abstraction makes the similarity *nameable*, and once named, recognizing further instances becomes cheap.

**Depth:** shared structure (lemma) or generative model (category theory). The clean case — positing the general and recognizing the particulars co-arise in a single step.

## Darwin's theory of evolution

Darwin took four observations that were separately unremarkable — variation exists, more offspring are born than survive, traits are heritable, environment exerts pressure — and saw that taken together as axioms, they produce a theorem: populations adapt over time. Each observation was known to breeders, Malthus, naturalists. Nobody was hiding information. The creative act was seeing that these statements from different domains are premises of the same argument.

Crucially, Darwin proposed the model *without knowing the mechanism of any of its components*. He didn't know what generates variation (mutations), how heredity works (DNA), or the biochemistry of selection pressure. The model operates at a level of abstraction *above* all those mechanisms. It says: I don't care *how* variation is produced, only *that* it exists. Given these abstract properties, adaptation follows necessarily.

This is mathematical in its core. Evolution by natural selection is a theorem about any system satisfying those axioms — which is why the same logic appears in genetic algorithms, immune system antibody selection, market competition, and cultural evolution. The empirical work was necessary not to prove the theorem but to **identify the right axioms**. The Galapagos finches didn't prove natural selection; they showed Darwin which abstract properties to attend to.

**Depth:** generative model. Darwin didn't just find shared structure — he proposed an abstract machine that *produces* the observed phenomena as outputs. The model explains why the similarity exists and predicts where else it should appear.

## Fleming's discovery of penicillin

This feels different — a contaminated petri dish, mold killing bacteria. Where's the "extraction"? But other microbiologists had seen mold contamination. Some had probably seen inhibition zones. Fleming's contribution was recognizing that this specific anomaly *could be* an instance of something general — that there might exist a category of substances that could be extracted, purified, and used therapeutically.

But the dual structure is less clean here than in the mathematical case. Fleming's initial recognition was narrow: this mold produces something that kills bacteria, and that's worth investigating. The full general category — antimicrobials as a therapeutic class — codified gradually over the next decade through the work of Florey, Chain, and others. The particular and the general didn't co-arise in a single moment; the particular prompted a *direction* and the general emerged through sustained work.

**Depth:** shared feature initially (this substance kills bacteria), graduating to generative model over a decade of work by multiple contributors. Shows the dual structure stretched across time, not the tight simultaneity of lemma extraction.

## Epistemic fragility at depth

A shared feature is easy to verify or refute. A generative model can be compellingly wrong — phlogiston, caloric theory, and luminiferous ether were all generative models that unified diverse phenomena under a single abstract machine, and all turned out to be false. The power of deep abstraction and its epistemic fragility are the same property: the model explains so much that disconfirming evidence can always be accommodated until the whole edifice collapses at once.

## The Luhmann reframing

A common framing in Zettelkasten-adjacent writing contrasts "topical" linking (filing by category) with "semantic" or "mechanistic" linking (connecting by shared deep structure). [Arscontexta's](../notes/related-systems/arscontexta.md) "controlled disorder engineers serendipity through semantic rather than topical linking" is the clearest statement.

This framing is useful but the dichotomy is false. Topic and mechanism are the same cognitive operation — recognizing similarity — applied at different depths of abstraction. Topic is shallow recognition (these are both about economics). Mechanism is deeper (these both describe systems that degrade under structural overload). But once you *see* the shared mechanism, linking by it is exactly as easy as linking by topic.

Luhmann's actual move wasn't "link by mechanism instead of topic." It was **link by judgment instead of category**. A filing cabinet uses pre-determined classification. Luhmann's Zettelkasten replaces that with individual decisions: THIS note connects to THAT note for THIS specific reason. The reason might be topical, mechanistic, analogical, or contrastive — what matters is that a human judged the connection worth making and articulated why.

## Maturation candidates

Each of these could become a standalone structured-claim with adequate support:

1. **Topic and mechanism are the same cognitive operation at different depths** — needs cognitive science support or counter-examples
2. **Luhmann's move was judgment-based linking, not mechanism-based linking** — checkable against Luhmann scholarship
3. **Discovery has a dual structure** — Darwin and Fleming gesture at this but Fleming strains the claim. More cases needed from philosophy of science
4. **The three-depth hierarchy** — is this a real hierarchy or post hoc arrangement? Gentner's structure-mapping theory may support or refine it. Possible Alexander source.
5. **Epistemic fragility scales with abstraction power** — needs its own argument with historical grounding
6. **Recognition, not linking, is the hard problem** — the most actionable claim for KB design
7. **Naming structures amortizes discovery cost** — already operationalized in /connect; could be grounded in concept formation literature

## Open Questions

- Can you build practices that push connections from "shared feature" toward "generative model"?
- Two distinct discovery problems get conflated: (1) noticing that existing notes share structure, and (2) inventing the abstraction that makes the similarity visible (genuine theoretical creativity). These probably need different system support.
