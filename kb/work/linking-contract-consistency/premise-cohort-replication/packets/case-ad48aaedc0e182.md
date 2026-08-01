# Case packet

Neutral case identifier: case-ad48aaedc0e182

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# First principles are inherited constraints, not design choices

A companion note shows which rules a universal framework *cannot* keep as universals: first-order content taxonomies [demote to guarded defaults] because they are not universal — the next kind of KB breaks them. This note is the other half: the rules that genuinely constrain the design space and therefore cannot demote.

The membership test: **a rule is a first principle iff it arrives in the constraint packet of one of the framework's boundary commitments** — the *consumer* it serves, the *substrate* it is built on, the *domain* it commits to (knowledge), or the *machinery* it has built. The commitments themselves are chosen, sometimes for features unrelated to the constraints they bring — files picked for ubiquity and tooling, not for how placement behaves. But every such choice is a packet deal: whichever substrate is chosen, its limitations come along whole, and the framework cannot cherry-pick the features it likes out of the bundle. What is unchoosable is not the boundary but the unbundling — and that is the sense in which a first principle is *inherited*: it comes with a commitment, never on its own terms.

Nor does composition escape a packet: a framework can combine parts built on different substrates, but each part still answers to its own substrate's limitations — artifacts held in files obey the file packet even when acceptance state lives in a database next door. Machinery coherence fits the same shape, just later: building machinery of a given kind is the choice, and its coherence rules are the packet. These four are the boundary commitments currently visible; the list is open, like the list of principles itself.

The two halves are therefore not symmetric. Design choices are *positions within* the design space: a rival can be swapped in while every boundary commitment stays, so a framework aiming at universality can offer several and let a collection pick — they demote to guarded defaults. First principles are *boundaries of* the design space: there is no rival position to demote to, and dropping one means re-choosing a boundary commitment and taking a different packet whole — not reconfiguration but a different framework.

## The principles that currently pass the test

Each is named with the boundary it inherits from. The list is what passes today, not a closed set.

1. **Bounded context / context economy** — inherited from the *consumer's architecture*. The reader attends to one finite window in which everything competes (since [context efficiency is the central design concern in agent systems]), and the binding pressure is silent degradation before any hard limit (since [agent context is constrained by soft degradation, not hard token limits]). Specific length norms are *local strategies* serving this economy; the economy itself cannot be opted out of while the consumer is an LLM.

2. **Composability / co-loading** — inherited from *how the consumer ingests artifacts*: files load as whole units into one shared window, so an artifact's usefulness is decided by what it does when co-present with others (see [short composable notes maximize combinatorial discovery]). The inherited form is weak — every artifact must stay usable when loaded alone, without dragging in unrelated claims. The stronger "citable as a bare premise" rule is a theoretical-register design choice layered on top, not the principle.

3. **Substrate asymmetry** — inherited from the *file substrate*. Directory placement is total (every file has exactly one location, no opt-out) while frontmatter classification is partial and opt-in, so location contracts and type contracts encode different guarantees and cannot substitute for each other (because [directory placement is total, frontmatter classification is partial]). On files this asymmetry is not negotiable.

4. **Answerability** — inherited from the *domain commitment* to knowledge. Every artifact must answer to something outside itself and can therefore be wrong or stale; a collection that cannot state what its artifacts answer to and what makes one stale is not holding knowledge (see [the complement note's scope test], which states the answerability property; the [knowledge-artifact] definition supplies the artifact class this commitment quantifies over). Which relation an artifact bears — to the world, a system, an outcome, a source — is local; *having* one is not.

5. **Declaration obligation** — inherited from *machinery coherence*. Every writable collection must carry a loadable contract, because the machinery routes and validates by reading that contract; a collection without one is an operational defect regardless of content. The complement note treats this as the surviving second-order universal (its shipped instance is ADR 017's `COLLECTION.md`).

6. **Admission discipline** — inherited from *machinery coherence*. Once taxonomies are opened into extensible sets, some admission brake is required: without one, the open sets proliferate until no convention is shared — which is the other way to stop being a framework. As with composability, the inherited form is weak — *an* admission discipline must exist — while the specific worked-case guard (entries admitted only after surviving use in a real collection, never from anticipation) is the discipline this framework chose, layered on top. The complement note identifies that guard as the load-bearing piece that lets closed taxonomies safely open.

7. **Derived-copy rule** — inherited from *machinery coherence*. A copy of information recomputable from a ground-truth source must be machine-checked against that source or not exist; a hand-maintained-and-trusted copy is a trap (because [a derived copy of recomputable truth must be checked or absent]). Any framework that caches recomputable values inherits this, since a silently stale trusted cache corrupts the consumers that trust it.

## Contrast: rules that look like principles but demote

The membership test earns its keep by *excluding* rules that feel foundational but are positions the framework chose and could re-choose. Each of these demotes to a guarded default per the complement note:

- The **three [registers]** (theoretical / descriptive / prescriptive) — a proven bundle, but a new kind of KB can need a fourth; they demote to default text-contract profiles.
- **Link-label sets** — `extends`, `grounds`, `contradicts`, and the rest are a collection-owned selection from a shared catalogue, not a universal vocabulary.
- **Type sets** — open and collection-local; the framework fixes that types *exist* and are path-valued (machinery), not *which* types there are (choice).
- **Spending the directory tree on content-area** rather than on kind — a routing decision a given KB makes, reversible without touching the framework.
- **Status / lifecycle enums** — the existence of a lifecycle is machinery; the specific values, and whether status fuses structural state with first-person endorsement, are a choice sitting one level too high.

The tell in every case: you can name a rival that also works *under the same boundary commitments*. When no rival exists — because the only alternative is to change the consumer, substrate, or domain, or to break the machinery — the rule is inherited, and the list above collects the ones currently visible.

## Caveats

The durable content is the *test*, not the enumeration: a later principle may be recognized as inherited, or one of these may turn out to be a disguised choice with an unnoticed rival, and neither outcome would touch the test itself. The test defines first-principle status rather than deciding it — the rival-hunt is how the test is applied, and application is fallible in both directions. And "inherited" is always relative to a framework's own boundary commitments: a framework that changed consumer or substrate would inherit a different set. So these are first principles *of this framework*, not of knowledge bases in general.

---

Relevant Notes:

## Artifact B

# Short composable notes maximize combinatorial discovery

The library layer (`kb/notes/`) exists for co-loading. [Discovery] — seeing shared structure across particulars — requires co-presence: you can't find that three notes share unnamed structure if only one fits in context. Under [bounded context], the number of notes that fit determines the surface area for cross-cutting connections. Short, atomic notes maximize that surface area.

The gain is probabilistic, not mechanical — not every pair yields a discovery. What matters is breadth of *independent* perspectives. Notes from distant domains are more likely to reveal shared structure than additional notes within the same topic. The library should be optimized for this: many small, independently authored claims that can be loaded together in varied combinations.

[Resolution-switching] complements this. Claim titles and descriptions give broad surface-level pairing without loading full bodies; full notes are loaded selectively where depth is needed. Short notes make both modes cheaper.

## Prior work

Atomic, composable units are a recurring design principle:

- **Zettelkasten** (Luhmann) — one idea per note, connections between notes. "One claim, one note" is Luhmann's atomicity principle. The most direct ancestor.
- **Modular design** (Parnas, 1972) — modules hide design decisions and expose interfaces. The Unix philosophy ("do one thing well, compose through pipes") is the same principle applied to programs.
- **Faceted classification** (Ranganathan, 1933) — describe items along independent combinable facets rather than a single hierarchy. Composable notes are facets.

What's specific to our context is the bounded-context motivation: atomicity here is driven by a hard token limit that makes co-loading capacity the scarce resource, not by filing convenience or code maintainability.

**TODO:** This survey is from the agent's training data, not systematic. Zettelkasten methodology in particular has extensive practitioner literature on atomicity trade-offs worth ingesting.

## The design rule

**One claim, one note.** The title states the claim, the body supports it, the footer connects it. If a note has multiple `##` sections making independent claims, that's a signal to decompose.

**Longer synthesized views belong in workshops or are generated.** Theory overviews, campaign understanding, multi-note summaries — these are *consumers* of library notes, not library notes themselves. They live in `kb/work/` as workshop artifacts with lifecycles, or are generated (like indexes). When the purpose is served, the workshop artifact expires but the library notes remain available for recombination.

## Evidence

The improvement log provides examples. Entries tagged ABSTRACTION and SYNTHESIS are discoveries made by co-loading notes and recognizing shared structure:

- "shared unnamed structure: execution-boundary compression" — found across five notes from different theoretical angles
- "two independent decompositions of agent memory from different traditions that together predict a two-axis taxonomy" — found by co-loading notes grounded in cognitive science alongside notes grounded in computer architecture

The structure emerged from the *juxtaposition* of independent perspectives. A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure — it would have pre-committed to one narrative instead of leaving the connections available for discovery.

## Tension with argument coherence

Some arguments genuinely need space — the reasoning from premises to conclusion loses force when atomized. [Evolving understanding needs holistic rewrite, not composition] — when a consumer needs the whole picture, reconciling into a single narrative beats composing fragments.

The resolution: coherent narratives are workshop artifacts, not library artifacts. The library stores premises and conclusions as separate composable notes. The workshop assembles them into narratives for a specific purpose. When the narrative expires, the atomic notes remain.

---

Relevant Notes:

## Under-review context phrase

co-loading is why composability is inherited from how the consumer ingests artifacts
