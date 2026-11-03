---
description: "Simon 1962: evolved complex systems are nearly decomposable hierarchies, so short-run questions localize to one subsystem with others entering as aggregates; a mechanism for scale opacity"
source: https://www2.econ.iastate.edu/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf
captured: "2026-11-03"
capture: pdftotext
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267
ingested: "2026-11-03"
occasion: "what near-decomposability says about why a question about a hierarchical system localizes to one subsystem with the rest entering through short interfaces, as a candidate mechanism for the inspection-cost measure behind the opaque modifier in kb/theory/definitions/representational-form.md and kb/theory/opacity-depends-on-the-inspection-question-and-budget.md."
learning_claims: true
type: types/ingest-report.md
domains: [near-decomposability, hierarchy, complex-systems, interaction-locality]
---

# Ingest: The Architecture of Complexity (Simon, 1962)

## Classification

This is a theoretical essay, read as a lecture to the American Philosophical Society and published in its Proceedings (vol. 106, no. 6, 1962). It argues across physical, biological, social and symbolic systems by parable and example. It gives one back-of-envelope probability model (the watchmakers) and cites, without reproducing, the Simon–Ando aggregation theorem for nearly decomposable dynamic systems. Simon himself says the theories have "relevance" to other domains, not "application". The conceptual-essay lens fits better than the scientific-paper lens: the cross-domain claims rest on analogy, and no claim is tested here.
Author: Herbert A. Simon, then at Carnegie Institute of Technology, co-developer with Newell of early problem-solving programs and of the cited aggregation theory with Ando. This is a canonical text in complex-systems and design theory.

## Summary

Simon argues that complexity frequently takes the form of hierarchy, meaning nested subsystems with or without authority relations, and that hierarchies share four content-independent properties. First, hierarchies evolve far faster than flat systems of comparable size, because stable intermediate forms cap the work lost to each disruption. The watchmaker Hora, who builds 10-part subassemblies, finishes about 4,000 times faster than Tempus, whose 1,000-part watch falls apart on interruption. In problem solving, cues of progress play the role of stable subassemblies, as in the clicking-safe example. Second, hierarchies are nearly decomposable. Interactions within subsystems are strong and fast, and interactions between subsystems are weak. In the short run each subsystem behaves approximately independently of the others. In the long run each depends on the others only through aggregates, as in the building example where, after rooms equilibrate, one thermometer per room suffices. Subsystems are identified operationally as blocks of large coefficients in an interaction matrix, given a chosen tolerance ε for off-block entries. Third, near-decomposability makes such systems comprehensible and compactly describable: cross-part detail "can be ignored", whereas a complex non-hierarchic system may escape observation because analysing it would exceed our "capacities of memory or computation". Fourth, descriptions come as state descriptions (blueprints) or process descriptions (recipes), and problem solving translates between them. Simon closes with speculation about genetic programs and recapitulation.

## Quotes

> among the subsystems are weak, but not negligible.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; end of the sentence defining a theory of nearly decomposable systems (two-column capture interleaves its start with footnote 15)

> ( a ) in a nearly decomposable system, the shortrun behavior of each of the component subsystems
> is approximately independent of the short-run behavior of the other components; ( b ) in the long
> run, the behavior of any one of the components
> depends in only an aggregate way on the behavior
> of the other components.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; the two main propositions

> W e have seen that hierarchies have the property
> of near-decomposability. Intra-component linlzages are generally stronger than intercomponent
> linkages. This fact has the effect of separating
> the high-frequency dynamics of a hierarchy-involving the internal structure of the componentsfrom the low frequency dynamics-involving interaction among components.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Summary: Near Decomposability

> The watches the men made consisted of about
> 1,000 parts each. Tempus had so constructed his
> that if he had one partly assembled and had to put
> it down-to answer the phone say-it immediately
> fell to pieces and had to be reassembled from the
> elements. The better the customers liked his
> watches, the more they phoned him, the more difficult it became for him to find enough uninterrupted
> time to finish a watch.
> The watches that Hora made were no less complex than those of Tempus. But he had designed
> them so that he could put together subassemblies
> of about ten elements each. Ten of these subassemblies, again, could be put together into a larger
> subassembly; and a system of ten of the latter subassemblies constituted the whole watch. Hence,
> when Hora had to put down a partly assembled
> watch in order to answer the phone, he lost only a
> small uart of his work, and he assembled his
> watches in only a fraction of the man-hours it
> took Tempus.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — The Evolution of Complex Systems; watchmaker parable

> Now if p is about .Ol-that
> is, there is one
> chance in a hundred that either watchmaker will
> he interrupted while adding any one part to an assembly-then a straightforward calculation shows
> that it will take Tempus, on the average, about
> four thousand times as long to assemble a watch
> as Hora.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — The Evolution of Complex Systems; watchmaker calculation result

> case as a limit, and as a first approximation.
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; left-column fragment 1 of the approximation sequence: the decomposable (perfect gas) case as a limit and first approximation

> can use a theory of perfect gases. for example, to
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; left-column fragment 2; the next line's right column interleaves footnote 15 text

> gases if they are not too dense. As a second ap-
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; left-column fragment 3, start of the definition sentence; footnote 15 text occupies the right column and an intervening line

> proximation, we may move to a theory of nearly
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; left-column fragment 4 of the definition sentence; line continues with footnote 15 in the right column

> decomposable systems, in which the interactions
> --- `kb/sources/.snapshots/herbert-simon-architecture-of-complexity.md` @ `sha256:f158ed330d3752913429be86047c75f6471a06814ee82d7f1cc9d6803f754267` — Nearly Decomposable Systems; left-column fragment 5 of the definition sentence; the sentence ends with the earlier retained item "among the subsystems are weak, but not negligible."

## Connections Found

For the occasion, the source's role is a **candidate mechanism** for the scale source of opacity. [Opacity depends on the inspection question and budget](../theory/opacity-depends-on-the-inspection-question-and-budget.md) states that "coupling can defeat local reasoning even where each unit remains readable" and that "there is no single size at which every question about an artifact becomes opaque", but it names no structural condition that decides when a question stays local. Simon's near-decomposability supplies one. A question about a subsystem's short-run behavior needs only that subsystem's strong internal interactions. Other subsystems enter through a few aggregate variables. Inspection cost then tracks the size of the strongly coupled block that contains the question plus the number of aggregates crossing its boundary, not total size. The same mechanism explains why the opacity judgment is question-relative. The answer depends on the time horizon (short run versus long run) and on the tolerance ε, which corresponds to "acceptable cost". Whether this transfers to symbolic artifacts depends on reading interaction as dependency or information flow between units. That reading is our transfer, not Simon's claim, and it bears on the opaque modifier in [representational form](../theory/definitions/representational-form.md) only for scale, not for the reference's form or deliberate obfuscation.

Simon's description argument also bears on that note, more weakly. "How complex or simple a structure is depends critically upon the way in which we describe it", and finding the redundancy requires "the right representation". This supports treating inspection cost as relative to the description and reference in hand rather than as an intrinsic property of the system.

For the general KB, the source is the **interaction-structure counterpart** to the Parnas-anchored locality cluster. [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) and the [Parnas 1972 ingest](./parnas-1972-criteria-decomposing-systems-modules.ingest.md) draw boundaries around decisions likely to change. Simon draws them where interaction is weak, and adds a time-scale split between short-run independence and long-run aggregate dependence. The two are different locality criteria, change locality and interaction locality, and the KB currently names only the first. Near-decomposability does not appear anywhere else in the KB.

The watchmaker argument is an early form of the topology step in [Topology, isolation, and verification form a causal chain for reliable agent scaling](../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md). Completion probability decays exponentially with the length of an unprotected sequence, and stable intermediates cap the loss. Simon's failure mode is interruption that destroys partial work, not wrong output, so the essay supports the topology step only. The [Tu hierarchical-MAS ingest](./xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) makes the same probabilistic argument formally. Simon's "span" (number of subsystems per level, after span of control) names the managerial-capacity branching constraint that the Tu ingest says [Decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) leaves unnamed. His cues of progress as stable subassemblies also bear on that note's advice to save reusable intermediates.

Simon's operational definition of subsystems as clusters of interaction frequency compares with [Areas exist because useful operations require reading notes together](../theory/areas-exist-because-useful-operations-require-reading-notes-together.md). Both ground grouping in interaction rather than declared membership.

- [The Architecture of Complexity (PDF)](https://www2.econ.iastate.edu/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf) — derived-from: JSTOR reprint of Proc. APS 106(6), 1962
- [Opacity depends on the inspection question and budget](../theory/opacity-depends-on-the-inspection-question-and-budget.md) — is-evidence-for: near-decomposability is a candidate mechanism for when scale leaves a local question affordable
- [Representational form](../theory/definitions/representational-form.md) — see-also: the opaque modifier whose scale source this mechanism would explain
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — compares-with: interaction locality and its time-scale split versus change locality and impact closure
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — is-evidence-for: the watchmaker parable supports the topology step only
- [Decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — is-evidence-for: span as a branching constraint; progress cues as stable intermediates
- [Areas exist because useful operations require reading notes together](../theory/areas-exist-because-useful-operations-require-reading-notes-together.md) — compares-with: grouping identified by interaction frequency
- [Parnas 1972 ingest](./parnas-1972-criteria-decomposing-systems-modules.ingest.md) — compares-with: boundary criterion, anticipated change versus interaction intensity
- [Tu hierarchical-MAS ingest](./xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) — compares-with: hierarchy against exponential sequential failure; span versus managerial capacity

## Learning Claims (our opinion)

**Mechanism on its own terms.** Simon's adaptive mechanism is selection that retains stable intermediates. In evolution, random assembly is directed only by the stability of what forms, and stable configurations become building blocks for further construction. In problem solving, search is "selective trial and error". Selectivity comes from two sources, and Simon equates both with feedback of information from the environment. One is noting the consequences of tried paths. The other is previous experience, meaning re-trying paths that solved a similar problem; its evolutionary analogue is reproduction. A partial result recognized as progress acts as a stable subassembly. Hierarchy is the outcome, because hierarchies "are the ones that have the time to evolve".

**Mapping onto Commonplace concepts.** Against [theory builder](../theory/definitions/theory-builder.md), biological evolution in Simon's account meets none of the conditions in a stated form: no localized theory is criticized, so it falls under the trial-and-error side of the theory-builder definition's contrast between trial and error and the critical method. Simon's problem solver is closer but still underdetermined by the essay. *Localized content*: the essay does not say whether the solver holds a stated theory or only stated partial results; open. *Consumption*: heuristics and prior solutions guide search; plausible but unspecified. *Content-directed criticism*: progress cues and translating a process description back into a state description to recognize success test candidate solutions against a stated goal. That is error elimination aimed at outputs, not at a theory; weak. *Iteration*: progress cues spur or abandon lines of search within one problem; reuse of prior solutions gives persistence across problems. Supported as description, not as demonstrated mechanism. The essay makes no learning claim in the sense of improved capacity for future action beyond the remark that experience reduces search.

**What it adds or puts in question.** The essay adds a reason why retained intermediates matter to adaptation that does not depend on criticism: they cap the loss from disruption and turn exponential search into search proportional to the number of levels. That bears on persistence grades, not on the criticism condition. It also supplies a structural precondition for the selective repair that [addressable theory](../theory/definitions/addressable-theory.md) depends on: blame can be localized to a part only where interactions between parts are weak on the time scale of the test. Simon does not argue this; it is our mapping, and it is untested here. The essay sharpens one point in [learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) without supporting or challenging it: in Simon's account the decomposition is not fixed in advance but emerges from which intermediates prove stable, so the partition itself is selected.

## Extractable Value

1. **Near-decomposability as the mechanism behind scale opacity** — Whether a question about a large artifact is affordable depends on the interaction structure, not on size. If the units the question concerns form a strongly coupled block whose links to the rest are weak, the inspector reads that block and treats the rest as a few aggregates. If coupling is dense, or one hub links strongly to everything (Simon's "consumption subsystem" in the economy), local reasoning fails even though each unit is readable. This turns the opacity note's bare remark that "coupling can defeat local reasoning" into a stated condition. Transferring it to programs or KBs requires reading interaction as dependency or information flow; Simon's theorem covers linear dynamic systems with an interaction matrix. [quick-win]
2. **Question-relativity gets a time-scale and a tolerance** — The same system localizes for short-run questions and requires aggregate coupling for long-run ones, and what counts as decomposable depends on the chosen ε. Mapped to inspection, the horizon of the behavioral question and the acceptable approximation error both belong beside an opacity judgment, which fills out the note's "question … and acceptable cost". [quick-win]
3. **Candidate inspection-cost measure** — One conjecture follows. Inspection cost for a question ≈ the size of the ε-block containing the question's units + the number of aggregate variables crossing the block boundary, for the question's horizon. This is our construction, not Simon's, and it needs a worked case on a real codebase or KB dependency graph before it can enter the definition. [deep-dive]
4. **Two locality criteria, change and interaction** — Parnas's change-anticipation criterion and Simon's interaction-intensity criterion are distinct grounds for drawing boundaries. Localized retention's "impact closure" is an interaction-locality condition stated in change terms, and Simon's time-scale split would sharpen it: locality holds in the short run, while long-run coupling persists through aggregates. [deep-dive]
5. **Span as a named branching constraint** — Simon's span (subsystems per level) is a citable anchor for the open quick-win in the Tu ingest: naming managerial capacity as a branching constraint in the decomposition heuristics note. [quick-win]
6. **Watchmaker as precedent and boundary for the topology step** — Hierarchy pays even without verification when failures destroy partial work, which bounds how far the topology–isolation–verification chain is "strict". [quick-win]
7. **Description-relative complexity** — Redundancy, near-decomposability (the "empty world hypothesis") and recoding make compact description possible, and Simon concludes that simplicity requires finding the right representation. This is vocabulary support for treating complexity and inspection cost as relative to a representation. [just-a-reference]
8. **State versus process descriptions** — The blueprint/recipe distinction and problem solving as translating between them are adjacent to KB discussions of specifications and procedures but carry no settled connection. [just-a-reference]

## Limitations (our opinion)

The essay reasons by cross-domain analogy and says so: Simon offers "relevance", not "application", and leaves judgment to specialists. The one rigorous result, the Simon–Ando aggregation theorem, is cited rather than stated. It applies to dynamic systems described by a nearly decomposable coefficient matrix, so its use for symbolic artifacts such as programs, prompts or notes rests on an unargued mapping from heat flow or bond strength to dependency. The essay gives no measure of inspection cost. It shows that a description loses little information under near-decomposability, which is a different quantity from the cost of answering a question.

Simon flags his own selection effect: we may find the world hierarchic because the non-hierarchic parts "elude our understanding and observation". For the occasion this cuts both ways. Artifacts that are opaque by dense coupling may simply be under-represented in the cases that make near-decomposability look common, so the mechanism explains affordable cases without showing they predominate. His drawing example also names the characteristic error of hierarchic representation: detail about relations between subparts of different parts "has no place in the outline and is likely to be lost". A localized inspection answer is wrong exactly where those weak cross-block links matter on the question's horizon.

The watchmaker numbers are illustrative; Simon says the estimate should not be taken seriously beyond its direction. The interruption model has no wrong outputs, so it says nothing about verification. The essay names hub exceptions (the consumption subsystem) without a theory of when they arise, so it cannot predict which artifacts will resist localization.

## Recommended Next Action

Update [Opacity depends on the inspection question and budget](../theory/opacity-depends-on-the-inspection-question-and-budget.md), section "Scale", with one paragraph citing this ingest. Name near-decomposability as the structural condition under which a question about a large artifact stays affordable: strong coupling inside a block, weak coupling across blocks, and other blocks entering as aggregates for the question's horizon and tolerance. Name dense coupling and hub components as the conditions that make scale opaque. Mark the transfer from Simon's dynamic systems to dependency structure as conjectural, and add an `evidenced-by` footer entry.
