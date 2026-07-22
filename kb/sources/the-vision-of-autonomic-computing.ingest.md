---
description: "Kephart & Chess 2003, origin of MAPE-K and the four self-* properties; the primary source behind the KB's reference-model-not-definition reading of self-adaptive loops."
source_snapshot: "the-vision-of-autonomic-computing.md"
ingested: "2026-07-22"
type: kb/sources/types/ingest-report.md
domains: [self-adaptive-systems, control-loops, self-improving-systems, agent-architecture]
---

# Ingest: The Vision of Autonomic Computing

Source: the-vision-of-autonomic-computing.md
Captured: 2026-07-22
From: https://jmvidal.cse.sc.edu/library/kephart03a.pdf

## Classification

Genre: conceptual-essay -- an IEEE Computer 2003 cover feature titled "The Vision of Autonomic Computing." Despite the peer-reviewed venue and reference list, it presents no methodology or data of its own; it is a manifesto and research agenda that argues by biological and economic analogy (the autonomic nervous system, cells, ant colonies, supply webs) and lays out engineering and scientific challenges. The capture-time `scientific-paper` label was corrected to `conceptual-essay` in the snapshot to match its evidential kind.
Domains: self-adaptive-systems, control-loops, self-improving-systems, agent-architecture
Author: High. Jeffrey Kephart and David Chess, IBM T.J. Watson Research Center, writing the paper that named the field and introduced the MAPE-K loop and the managed-element / autonomic-manager split. This is the canonical, heavily-cited origin document for autonomic and self-adaptive computing.

## Summary

Kephart and Chess argue that rising software complexity is outstripping human capacity to install, configure, tune, and maintain systems, and that the only remaining option is autonomic computing -- systems that manage themselves given high-level policies from administrators. They organize self-management into four aspects (self-configuration, self-optimization, self-healing, self-protection) and propose an architecture of interacting autonomic elements, each a managed element coupled with an autonomic manager that monitors, analyzes, plans, and executes over shared knowledge (the MAPE-K loop, drawn in Figure 2 without yet being named as such). Autonomic elements are framed as goal-directed agents that negotiate service relationships with a full life cycle (specification, location, negotiation, provision, operation, termination), making an autonomic system a multiagent system on a service-oriented infrastructure. The paper closes with engineering challenges (element and relationship life cycles, security, goal specification) and scientific challenges (behavioral abstractions, robustness theory, multiagent learning and optimization, negotiation theory), stressing that emergent global behavior is hard to derive from local rules and that multiagent adaptation breaks single-agent learning guarantees.

## Connections Found

This snapshot's role is the missing origin source for a lineage the KB already engages through its derivatives. Two settled notes -- [a proposal-selection loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and the [self-improving system definition](../notes/definitions/self-improving-system.md) -- both anchor the same claim (MAPE-K and its relatives are engineering reference models, not membership definitions of self-improvement or self-adaptation) but cite only the downstream self-adaptive-systems captures ([Weyns](./weyns-software-engineering-self-adaptive-systems-tour.md); [Petrovska, Erjiage, and Kugele 2025](./defining-self-adaptive-systems-systematic-literature-review.md)). This paper is where MAPE-K originates, so it belongs under those notes as primary evidence for the reference-model reading. Secondarily it sits alongside [Ashby's ultrastability](./ashby-design-for-a-brain-ultrastability.md) as an external self-regulation precedent the self-improving-systems cluster measures itself against, and it is the historical head of a control-loop lineage that contemporary agent-harness captures ([the self-healing agent harness](./the-self-healing-agent-harness-2048912026018484317.md), [harness engineering is cybernetics](./harness-engineering-is-cybernetics-2030416758138634583.md)) re-enact in miniature. The relationships that matter here are to notes that already exist; there is no need to pre-map its ties to other captures.

## Extractable Value

1. **Origin citation for the reference-model-not-definition claim.** The KB currently grounds its "MAPE-K is a reference model, not a definition" reading in two derivative sources; this paper is the primary source that introduced the loop, and citing it closes the gap in both the proposal-selection note and the self-improving-system definition. [quick-win]
2. **The managed-element / autonomic-manager split as the origin of structure-vs-governance separation.** The paper's separation of a managed element (structure) from an autonomic manager that governs it by monitoring and control is an early, explicit statement of the same separation the KB frames as runtime structure determining governance control surfaces -- useful as historical grounding for that architecture-neutral claim. [just-a-reference]
3. **The four self-* properties as a decomposition vocabulary.** Self-configuration, self-optimization, self-healing, and self-protection are a durable, retrieval-friendly vocabulary for classifying what a self-managing loop actually does; the paper's own note that these "distinctions will blur into a more general notion of self-maintenance" is a useful caution against treating them as hard categories. [just-a-reference]
4. **Multiagent adaptation breaks single-agent learning guarantees.** The scientific-challenges section states plainly that when elements adapt to an environment made of other adapting elements, convergence guarantees fail and optimization techniques assuming a stationary environment "fail pathologically." This is a transferable warning for any KB claim about composed adaptive agents or nested self-improving loops. [experiment]
5. **The staged-autonomy adoption path.** The paper's milestone ladder -- collect and aggregate, then advise, then act on low-level decisions, then act on higher-level ones -- is a reusable framing for how much autonomy to grant an agent loop over time, and maps onto trust-graded delegation arguments elsewhere in the KB. [just-a-reference]
6. **Goal-specification as the residual human surface and its failure mode.** Kephart and Chess argue that policy specification stays human, that autonomy magnifies the consequences of a goal-specification error, and that systems must guard against "inconsistent, implausible, dangerous, or unrealizable" goals. This is a durable operational warning about where the leverage and the risk concentrate in policy-driven autonomy. [just-a-reference]

## Limitations (our opinion)

Editorial opinion. As a conceptual essay this is a vision, not a validated design, and the conceptual-essay lens applies: the central mechanism is argued almost entirely by biological and economic analogy (autonomic nervous system, cells, ant colonies, supply webs, markets) without testing whether the analogy holds -- naming the field "autonomic" does not itself explain how local element rules produce desired global behavior, which the paper elsewhere admits is an unsolved, "highly nontrivial" inversion problem. The framing is largely unfalsifiable as stated: nearly any self-managing system can be read as an instance. It is also a 2003 IBM manifesto with an institutional interest in positioning autonomic computing as "the only option remaining," and its infrastructure assumptions (Web/grid services, OGSA, UDDI, the semantic Web) are dated. For the KB the value is precisely as a primary origin and vocabulary source, not as evidence that the vision was achieved; the honest downstream read is the KB's existing one -- these loops are reference models, and the paper itself supplies no membership test.

## Recommended Next Action

Add an `evidence` reverse edge from [a proposal-selection loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) to this snapshot, citing Kephart & Chess as the origin of the MAPE-K reference-model tradition the note already invokes through Weyns and Petrovska. Fold the same citation into the [self-improving system definition](../notes/definitions/self-improving-system.md) if the author judges it warranted while making that edit.
