# Case packet

Neutral case identifier: case-a23b180adead23

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# The framework is often larger than the durable contribution

An agent writing about a situation that fits a familiar framework has that framework active — loaded into context or activated in weights — and active knowledge tends to leak into the artifact. The strongest case is discovery: an authoring agent uses a large body of familiar knowledge to derive a small contribution and reproduces the derivation. But no derivation is required; an agent that merely names framework X tends to pad the artifact with X's details. Either way, a future consumer with access to the same parametric knowledge can reconstruct the framework; what changed was the recognition that this situation is an instance of it.

The size of what was active during writing is therefore a poor guide to retained size. The framework content explains what the author drew on, but only the parts future consumers cannot reliably reconstruct or activate must survive. Which parts those are remains [observer-relative].

## Recognition can be the durable contribution

When an artifact applies a familiar framework to a particular case, the durable contribution may be only:

> When **this observable condition** occurs, treat **this apparent task** as **this named kind of problem**, and use the corresponding framework to **perform this operation**.

The framework name addresses knowledge the consumer can reconstruct; the condition, mapping, and operation preserve what it did not reliably supply. Repeating the framework adds value only when it supplies something the name cannot: accessibility, disambiguation, warrant, or fidelity.

By that same measure, framework content — or the derivation that produced the contribution — must remain wherever it carries one of those values — when it is evidence the consumer must be able to check, when the consumer cannot reconstruct it, or when a particular version or interpretation has authority. Stripping a derivation always trades away auditability: a claim without its reasoning must be taken on trust. Participating in discovery does not make every part of the reasoning path part of the discovery, but reconstructability alone does not make warrant or exactness expendable.

## Minimal by default, grown on demand

Reconstructability is not the only reason to compress. A note records one case, and what the case contributes is the recognition — the cue, the mapping, the local fact. The framework behind it is shared across many notes, so it belongs in an artifact of its own, linked rather than re-taught inline, since [short composable notes maximize combinatorial discovery]. The write-time default is therefore minimal prose with a link standing where the framework recap would have gone: the graph carries the reconstructable load structurally, so no single note has to.

Minimal means minimal background, not minimal anchor. The dangerous compression cuts in the wrong direction: it drops the condition, mapping, or local fact — the case's actual contribution — while framework prose survives, or it drops the framework link entirely. The link matters because [knowledge storage does not imply contextual activation]: the name and cue are what trigger the consumer's reconstruction, and without them it fails silently. The anchor — framework name, link, and recognition condition — costs one line and is non-negotiable; the tutorial is what gets cut.

The default is also the cheaper one to correct. Adding a missing warrant or example when a consumer demonstrably misses it — a failed behavioral test, a real miss in use — is cheap and targeted. Trimming a bloated note later is expensive: it means re-deriving the boundary between scaffolding and load-bearing material, the judgment the behavioral test below exists to settle. And at write time the consumer population is unknown: over-retention bakes in an assumption about a weak reader who may never arrive, while minimal-plus-linked defers the decision to read time, when the actual consumer is present. Grow on demand, not on imagination.

## Examples

### Cue only: heterogeneous parts activate ontology

Suppose a description of a reflective system puts software components, functional roles, processes, retained artifacts, and levels of description into one list of "parts." A capable agent already knows ontology. The useful note preserves the diagnostic connection:

> When proposed parts do not all stand in the same relation to the whole, treat the task as ontology design: distinguish entity kinds and parthood relations before enumerating components.

Ontology was needed to derive the rule, but consumers that can reconstruct it from the name do not need the tutorial repeated.

### Cue plus local fact: a timeout activates idempotency

Suppose a service charges a card and times out before acknowledging success. A software agent already knows idempotency, but it cannot infer the system-specific ordering. The project note should retain both the cue—treat retries as an idempotency problem—and the local fact that the irreversible action precedes acknowledgement. Generic distributed-systems guidance can be reconstructed; the duplicate-charge risk and relevant operation boundary cannot.

### Relation only: two systems share a mechanism

Suppose two systems use different terminology but both precompute a stable part of a later reasoning task and insert the result into a bounded call. The consumer may know both systems and understand partial evaluation without recognizing the relation between them. The note should retain the comparison, shared mechanism, and consequences, not teach either system or partial evaluation again. The contribution is the edge, not either endpoint.

## Test the retained boundary behaviorally

For an agent consumer, semantic inspection cannot establish whether a framework name is an adequate address. Compare representative behavior with the name alone, the name plus a recognition condition, and the fuller framework restatement or derivation. If a smaller form preserves the contribution's effect, the removed material was scaffolding; if behavior degrades, the missing explanation, example, or warrant belongs in the retained result.

The boundary varies with the model, task, and consumer population. The test establishes a validity window, not a timeless compression.

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

shared frameworks live as their own composable artifacts, so each note carries only its case's contribution
