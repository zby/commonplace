---
description: "GORE researchers distinguish goal interpretation from responsibility and propose runtime governance, while leaving benefits for adaptive agents untested."
source: https://doi.org/10.1007/s00766-026-00476-7
captured: "2026-11-16"
capture: pdftotext
capture_scope: full-source
doi: "10.1007/s00766-026-00476-7"
genre: scientific-paper
snapshot_sha256: 8aec99a99f1982411637d031cdfc072425a94dd0425939a8ca626bbbe6a35a79
ingested: "2026-11-16"
occasion: "What can requirements engineering contribute, and what are its limits, for understanding operationalization, goal authority, and revisable knowledge in agent-operated knowledge work?"
type: types/ingest-report.md
domains: [goal-oriented requirements engineering, reasoning authority, participatory modeling, adaptive agents]
learning_claims: true
---

# Ingest: GORE mapping reflections, impact, and the way forward

## Classification

A scientific reflection combining a retrospective on an earlier systematic mapping, new bibliometrics and exploratory screening, experience-based judgments, and a research agenda. It is not an updated systematic mapping of GORE. Authors Jennifer Horkoff and nine colleagues include the authors of the original mapping and foundational goal-modeling researchers. Their expertise gives the conceptual proposals context, but their involvement also makes this an interested assessment of the field's relevance.

## Summary

Horkoff and colleagues revisit their mapping of 246 GORE publications through 2015, examine 264 publications citing it as of May 2026, and propose directions for goal modeling in LLM-supported software engineering and agentic systems. Citation counts establish visibility rather than influence. Title and selectively retrieved abstract screening suggests that 122 of 230 non-secondary citing studies mention empirical evaluation; this is not directly comparable to the original mapping's more detailed coding. The authors describe industrial adoption barriers, including maintenance and tooling integration, and warn that automated model generation can lose the negotiation and shared understanding produced by collaborative modeling. They ask whether explicit qualities, alternatives, decompositions, and trade-offs improve agents beyond simple statements of intent. For adaptive agents, they distinguish runtime authority to interpret goals from retained human or organizational responsibility, and propose persistent goal models for monitoring and governance. These agentic applications remain a research agenda rather than demonstrated improvements.

## Contribution assessment (our opinion)

The important contribution appears to be a problem formulation: GORE may supply explicit intentions, dependencies, responsibilities, and trade-offs where contemporary agent workflows leave them implicit, but adaptation challenges stable design-time interpretations. The reflection usefully turns a claim of renewed relevance into questions about delegation, model maintenance, and human participation that could support discriminating tests. Its bibliometrics demonstrate continuing scholarly visibility, not successful uptake or causal influence. The conceptual agenda seems more consequential than the lightweight citation screening, although it does not establish that GORE outperforms simpler governance representations. Originality relative to the wider agent-governance literature is not established by this capture; the proposed contribution does not depend on such priority.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a conceptual comparison for [intent-framed delegation](../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md): it explicitly separates delegated runtime goal interpretation from responsibility retained by human or organizational actors. The Commonplace note supplies more concrete information, authority, coordination, and recovery conditions; the paper does not test those conditions or justify transferring goal-setting authority to an executor. Its open question about whether richer goal semantics improve agent behavior also compares with [intent controlling a local choice](../theory/intent-controls-choices-by-distinguishing-live-alternatives.md). That note supplies a necessary discrimination test: added qualities or decompositions must change a live choice to exert control. Neither artifact establishes that a graphical goal model is the best representation for doing so. These comparisons make the paper useful for separating requirements structure from effective operational control, not as empirical support for adopting GORE in Commonplace.

## Learning Claims (our opinion)

The paper describes two different mechanisms. Collaborative goal modeling may produce learning through stakeholder negotiation and correction, which automatic generation could bypass. Separately, it describes agents trained through interaction and feedback, including an oracle that corrects wrong or incomplete responses. Its proposed Tropos extension distinguishes agents and goals fulfilled by design from those fulfilled through learning. Those are source categories, not equivalents of Commonplace's distinction between using and revising stated knowledge. Neither a learned capability nor a stakeholder goal is automatically an explanatory theory.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), explicit goals, dependencies, and rationales offer localized content, although normative goals must be distinguished from conjectures about how to achieve them. Consumption of that content is proposed through monitoring and agent direction, not demonstrated for an implemented adaptive system here. Content-directed criticism is plausible in collaborative correction and proposed satisfaction analysis, but the paper specifies no working process that criticizes identified operational assumptions rather than merely scoring goal attainment. Iteration is proposed through feedback and controlled evolution; the article does not demonstrate a cycle retaining a stated criticism and using it to revise the next operational conjecture. Persistent post-deployment goal models are an intended cross-run governance resource, not evidence that criticism persists across runs or problems. Improved future capacity is therefore an open empirical claim, separate from all four conditions.

The useful tension for revisable knowledge is that a persistent goal model can preserve accountability while its operational interpretation changes. Yet the paper leaves unresolved who can revise the model, the interpretation, and the governing criteria. Following the boundary in [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvements in agent behavior under a supplied goal hierarchy would not by themselves validate that hierarchy or its satisfaction measures. The reflection offers no comparison varying these choices. Its design-versus-learning distinction usefully names a problem but is too coarse to establish which parts of a knowledge-work system remain open to criticism.

## Extractable Value

1. **Separate goal interpretation, goal revision, and responsibility.** The source directly distinguishes runtime reasoning authority from retained responsibility. For agent-operated KBs, our further distinction is between permission to choose means, permission to revise an operational interpretation, and permission to change the goal itself. The paper motivates this separation without supplying a complete authority protocol. [quick-win]
2. **Treat richer requirements semantics as a testable intervention.** Qualities, alternatives, dependencies, and trade-offs are candidate inputs, not proof of control. Compare a simple intent statement with richer representations on choices where their contents predict different actions, holding authority and available evidence constant. This turns the paper's open question into a bounded test rather than an argument for importing a notation wholesale. [experiment]
3. **Keep governance representations criticizable without equating goals with theories.** A persistent model can record whose intentions govern and which constraints apply, while operational conjectures about achieving them remain revisable. The paper motivates runtime governance but does not resolve authority for changing the reference model or prove that its categories fit knowledge work. [deep-dive]
4. **Evaluate modeling as an activity as well as a product.** Automated goal extraction may preserve an artifact while removing stakeholder negotiation and shared understanding. This is a mechanism-based warning to investigate, not a measured loss established here; model correctness alone would not settle it. [experiment]

## Limitations (our opinion)

The citation analysis samples papers citing one mapping, not the current GORE field. Its title/abstract screening uses different inclusion and evaluation-detection procedures from the original mapping. The reported 53% versus 63.4% therefore does not establish declining empirical rigor. Citation visibility cannot establish adoption, influence on research direction, or benefit to users. The original mapping also filtered for citation counts and struggled with subjective coding, including abandoned relationship labels, which bounds any longitudinal interpretation.

The industrial uptake and education judgments are explicitly experience-based. They suggest maintenance, integration, and participatory mechanisms worth testing but do not estimate prevalence or identify which intervention would improve adoption. Reports of LLM goal-model generation are summaries of other studies, not reproduced comparisons in this article.

Most importantly, the article does not implement or evaluate the proposed agentic governance mechanisms. Framework descriptions are not code-grounded findings. Its broad characterization of contemporary agents as incrementally trained does not distinguish weight updates from changing prompts, memory, workflows, or interpretations. The proposed two-concept Tropos extension is attributed to a submitted paper, not validated here as sufficient. Explicit goal structure may make responsibility discussable without making consumption reliable or ensuring appropriate revision. The source does not decide how to distinguish legitimate adaptation from goal drift, authorize revision of stakeholder intentions, or establish epistemic criticism of a KB's claims. Those gaps narrow its role to conceptual framing and test design rather than a ready operational methodology.

## Recommended Next Action

Review `kb/theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md` specifically for whether it sufficiently distinguishes authority to choose means, reinterpret an operational goal, and revise the governing goal, using this source as a conceptual comparison rather than evidence of effectiveness.
