# Operationalization, Goals, and Grounded Concepts

## Commission and boundary

**Posed by the Commonplace operator on 2026-11-16. Status: research framing and experiment proposals; no experiments run.** Investigate whether requirements-engineering (RE) distinctions improve agent-operated knowledge work, especially article improvement. The intended reader is a maintainer deciding which distinction deserves a local test, not which RE framework to adopt.

Commonplace already separates usable guidance from successful outcomes, local conformance from upstream adequacy, and search from adoption. RE may make some missing premises easier to locate. The candidate contribution is **better discrimination among repairs**, not a unifying theory of agency, learning, concepts, and economics. An ordinary task checklist may do equally well at lower cost.

This commission authorizes this workshop and its Active Workshops entry only. It does not authorize experiments, additional ingestion, delegation, commits, library edits, new definitions, schemas, or governance machinery. The parent independently reviews source fidelity and experiment discrimination. Later execution needs a separate commission fixing tasks, budget, permissions, and evidence retention. Nothing here promotes theory or adopts an objective.

Close when the six threads below each have a bounded disposition: a useful distinction with a discriminating test, coverage by existing KB claims, rejection, or explicit deferral with the missing evidence named. The operator may stop at a reviewed proposal without running it. Any later durable extraction needs separate authorization and review; then follow the workshop lifecycle rather than retaining a permanent literature folder.

## Evidence boundary: six slots, not six available papers

The following is the commissioned source coverage. All five available ingests, including the separately commissioned Jureta 2008 paper, passed independent source review with no material issues. Acceptance of an ingest is not evidence of successful transfer to Commonplace.

| Commissioned slot | Available evidence and restriction |
|---|---|
| Zave and Jackson, *Four Dark Corners of Requirements Engineering* (1997) | [Full author-manuscript ingest (snapshot required)](../../sources/four-dark-corners-requirements-engineering.ingest.md), dated 16 July 1996. It is not a verified copy of the exact 1997 journal text or pagination. Sections 2, 4, 5 and the completion criteria support the comparisons below. |
| Gunter et al., *A Reference Model for Requirements and Specifications* (2000) | Journal DOI `10.1109/52.896248`, IEEE Software 17(3):37–43. Full text remains unavailable through the attempted public routes; no ingest and no substantive claims here. The separate ICRE extended abstract, DOI `10.1109/ICRE.2000.855609`, is not a substitute. Bibliographic records disagree on author ordering; no title page was recovered to adjudicate it. |
| Jureta, Mylopoulos and Faulkner, *A core ontology for requirements* (2009) | Applied Ontology 4(3–4):169–244, DOI `10.3233/AO-2009-0069`. Full journal text remains blocked; no ingest and no journal-content claim here. The additional 2008 paper below does not fill this slot. |
| Whittle et al., RELAX (2009) | [Full conference author-manuscript ingest (snapshot required)](../../sources/relax-uncertainty-self-adaptive-systems.ingest.md), DOI `10.1109/RE.2009.36`. Language, semantics and a concept-document case study, not a demonstrated adaptive controller. |
| Souza et al., *Awareness Requirements for Adaptive Systems* (2011) | [Full SEAMS paper ingest (snapshot required)](../../sources/awareness-requirements-adaptive-systems.ingest.md), DOI `10.1145/1988008.1988018`, pp. 60–69. Prototype monitoring and constructed scenarios, not a completed diagnosis-and-adaptation loop. |
| Horkoff et al., mapping reflections (2026) | [Full version-of-record ingest (snapshot required)](../../sources/horkoff-gore-mapping-reflections-2026.ingest.md), DOI `10.1007/s00766-026-00476-7`, Requirements Engineering 31, article 20; online 12 October, print issue December 2026. A reflection on the earlier mapping, not a new comprehensive systematic mapping. Agentic uses are an agenda, not tested benefits. |

**Additional, independently named source:** Jureta, Mylopoulos and Faulkner, [*Revisiting the Core Ontology and Problem in Requirements Engineering* (snapshot required)](../../sources/revisiting-core-ontology-requirements-engineering-2008.ingest.md), RE 2008, DOI `10.1109/RE.2008.13`, arXiv:0811.4364v1. Its author note calls it essentially the IEEE version. Served bytes print October 22, 2018 despite the November 2008 v1 identifier; neither original-2008 bytes nor a separate 2018 research version is established. Its project-local, revisable approximation relation supplies a conceptual comparison, not a demonstrated transfer to Commonplace or a claim about the blocked 2009 article.

All five available captures contain full paper text; text extraction does not preserve complete graphical notation. Ingest analysis is an interpretation, not primary evidence. Snapshot-marked links require the exact checksum-paired local reading copies for semantic review; no raw copies or operational-state links are published here. The blocked slots constrain coverage, but do not prevent testing distinctions independently supported by the available material. A supplied authorized journal copy would enable a separate ingestion decision, not an automatic expansion of this workshop.

## Six distinct threads

In each thread, **source** names the paper's contribution, **KB** the current account, and **question** our proposed transfer. These are not six components of an assumed common mechanism.

### A. Operationalization: desired outcome, domain knowledge, machine actions

**Source:** Zave and Jackson distinguish desired environmental properties R, implementable specifications S, and domain knowledge K, requiring `K, S ⊢ R`. Their completion criteria additionally require informal validation of R and K, implementability, and consistency. A conditional satisfaction argument does not establish that its assumptions are true or that the customer's desire serves a wider purpose. Their “requirements refinement” can introduce environmental assumptions or change requirements; it is not simply a synonym for program derivation.

**KB:** [Actionable methodology](../../theory/definitions/actionable-methodology.md) means guidance usable by a particular operator to choose available interventions for a given task and setting. It implies neither correctness nor success. Keep the [task-relative operationalization account](../operationalization-executability-automation/README.md): task, executor and objective are fixed for the comparison; broadening task scope is a separate claim. Operationalization makes knowledge usable here, execution performs the work, and automation assigns specified functions to computation. These are not compulsory successive stages.

**Question:** Does stating the assumed connection between an article edit and a reader's task expose a bad repair sooner than an ordinary editing checklist? For example, repairing headings cannot resolve contradictory advice. The desired outcome may initially be imprecise; a question to the operator can operationalize it during execution without authorizing a new goal. Where reader success cannot be independently judged, `K, S ⊢ R` is a reasoning prompt, not a proved guarantee. [Experiment 1](./experiments.md#1-operationalization-comparison) tests that narrower use.

### B. Bounded agency: control, observation, reasoning

**Source:** Zave and Jackson separately classify who controls an action and whether the machine can observe it. Their implementability discussion explicitly distinguishes implementability in principle from practical speed limits. RELAX further distinguishes environmental properties, observable monitors, and the relation used to infer the former from the latter.

**Question:** Can an instruction require an inaccessible fact or an action outside the agent's permissions while appearing executable? Reading tools can expand observation without granting control; write access can expand control without revealing the right edit. Retained knowledge can supply an inference, but may be stale. An executable procedure can reduce reasoning demands without improving either access boundary. Test these changes separately rather than label all of them “more capable agency.”

The [bounded-context orchestration model](../../theory/bounded-context-orchestration-model.md) concerns explicit state, symbolic scheduling, feasible calls and independent batches in a closed world. That is not equivalent to the RE environment–machine boundary. A live collaborator's independently changing intent is not stored state merely because the scheduler has a goal field. RE's distinctions alone also do not predict attention failures or the cost of reasoning over accessible evidence. Matched hidden-fact and denied-action variants in Experiments 1–2 can reveal those limits.

### C. Goal interpretation and authority

**Source:** Zave and Jackson's zoo example bounds goal regress by fixing subject matter as well as a goal. It does not establish who may choose that boundary. Horkoff et al. distinguish delegated runtime reasoning authority from responsibility retained by humans or organizations, and explicitly ask whether richer goal semantics improve agents beyond simple intent statements.

**KB and question:** [Objective revision needs an outside license](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md); [late disambiguation is not necessarily genuine goal change](../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md). Does a separate statement of problem-domain scope help an agent challenge a deficient request without silently replacing it? Method-choice delegation is not goal-redefinition authority. A challenge can be correct even when the agent must not implement the alternative. Conversely, initiative within the authorized end should not be scored as drift.

Keep four questions apart: what goal was intended; what bears epistemically on the current question; what is instrumentally attractive for another goal; and whether a proposed conceptual relationship is warranted. The [blending workshop](../epistemic-relevance-and-conceptual-blending/findings.md) has one motivating episode, not frequency or causal proof. Misinterpretation, association, answer format, and persistence of an earlier frame remain competing explanations. [Experiment 3](./experiments.md#3-goal-authority-and-a-tempting-alternative) does not presume blending caused any substitution. Goal-negotiated conversations remain owned by [chatbot-goal-state](../chatbot-goal-state/README.md).

### D. Tentative knowledge and adaptation

**Source:** RELAX specifies stakeholder-bounded flexibility and observation assumptions. Awareness Requirements specify runtime constraints on other requirements or domain assumptions; their implemented monitor evaluates instrumented scenarios, while full feedback-loop construction remains future work. Jureta 2008 makes the approximation of an ill-defined quality by a measurable constraint local and revisable; it leaves methodological support for justification open.

**Question:** Does separately naming assumptions and their possible defeat help locate a failed inference or only produce more labels? A missed outcome underdetermines whether execution, the domain model, the goal formulation, or the observation failed. Monitoring an alert does not identify its cause. Changing behavior within a permitted envelope does not show revision of knowledge, and changing a threshold does not show improvement.

The [three-way LLM diagnosis](../../theory/llm-output-deviation-requires-three-way-diagnosis.md) separates underspecification, interpreter failure and sampling variation for fixed assembled input. It is not a complete diagnosis of stale retrieval or false environmental premises. A [theory builder](../../theory/definitions/theory-builder.md) must consume stated theories, criticize their content and retain criticism into another round; monitoring alone supplies no such demonstration. [Fixed-decomposition limits](../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) further ask whether the needed correction can be expressed at all. [Experiment 2](./experiments.md#2-assumption-failure-diagnosis) includes indistinguishable traces where withholding unique blame is the correct result.

### E. Grounding and conceptual revision

**Source:** Zave and Jackson call an informal written connection of a primitive formal term to environmental phenomena a *designation*. They distinguish a potentially false assertion about independently designated phenomena from a formal definition extending vocabulary. They do **not** use “definition” to mean every connection to reality. Their student/enrollment example shows how apparently similar formulas can differ in empirical content. This is not a complete method for conceptual revision.

For comparison, the opening of [Chang's operationalism entry](../../sources/operationalism-sep.ingest.md#quotes) reports Bridgman's stronger identification of a concept with its measuring operations. That historical meaning claim is not our task-relative meaning of operationalization. No further philosophical survey is needed to pose the local contrast: does a chosen use specify a convention, or assert something that observations can contradict?

**Working distinctions, not adopted vocabulary:** stipulation chooses a use; grounding connects a term to a phenomenon or practice; an empirical conjecture can be false; conceptual revision changes the concept after criticism. One passage can do several of these. Ask how earlier propositions should be read after meaning changes, and which downstream inferences survive. Silent redefinition can remove a counterexample by changing the subject rather than improving an explanation. Mere terminology repair can instead preserve every empirical claim. [Experiment 4](./experiments.md#4-conceptual-revision-across-propositions) distinguishes these by consequences, not word matching.

### F. Commitments and economics

**KB:** [Commitment versus derivation](../../theory/commitment-not-derivation-creates-new-ground-truth.md) concerns retained resolutions not determined by their sources; it does not say that adopting a claim makes it empirically true. [Search control](../../theory/lightweight-search-control-does-not-license-adoption.md) allocates investigation without licensing adoption. Engineering choices, epistemic adoption, and resource commitments should therefore be compared without assuming one acceptance standard.

**Question:** Which choices depend on conjectures about expected returns, and when is testing those conjectures worth its cost? A procedure may be usable but too costly; an informative experiment may still be the wrong use of operator attention. The available RE comparisons do not settle allocation among undeveloped investigations. Record setup, model work, tool calls, and operator review separately in proposed tests; do not impose a numerical expected-value controller or adopt a maximand. The [economics workshop](../open-ended-work-economics/README.md) owns automatic-search guidance; the [reusable-support proposal](../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md) still needs comparative reuse evidence. Neither is confirmed by this RE framing. The [shared-epistemic-layer claim](../../theory/open-ended-knowledge-work-shares-one-epistemic-layer-across-roles.md) is a comparison target, not a premise that forces these six threads into one account.

## Next decision

Recommend **Experiment 2, assumption-failure diagnosis**, for a separately authorized first pilot. It tests the strongest practical candidate—making the premise linking action to outcome inspectable—without first requiring consensus on broad article quality. Seeded faults and indistinguishable traces can expose both useful discrimination and unjustified certainty. A failure against the matched checklist would favor using ordinary task guidance rather than adding an RE-specific representation.

[Experiments](./experiments.md) supplies four proposals only. No positive result would establish general transfer, complete RE coverage, or learning across problems. Source acquisition and broader graph discovery remain separate decisions, not prerequisites for producing more workshop text.
