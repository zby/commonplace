---
description: "Lynn's conceptual analysis: goals select which source features enter a blend; humans via a predictive-processing goal node, LLMs via externalized proxy-goals"
source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1849083/full
captured: "2026-11-01"
capture: trafilatura
capture_scope: full-source
doi: "10.3389/fpsyg.2026.1849083"
genre: scientific-paper
snapshot_sha256: 7359d6a069e5cedf3b9458e093ea80f686edfb0f11666e0965983e535d4bfcce
ingested: "2026-11-01"
occasion: "the epistemic-relevance-and-conceptual-blending workshop (kb/work/epistemic-relevance-and-conceptual-blending/) screened this paper as evidence-register entry E20 from an operator-supplied external review; the workshop needs the paper's own account of what role goals play in its theory of conceptual blending, and what it proposes as the corresponding mechanism in language models."
type: types/ingest-report.md
domains: [conceptual-blending, proxy-goals, predictive-processing, embodied-cognition]
learning_claims: true
---

# Ingest: Conceptual blending in humans and language models

## Classification

This is a peer-reviewed conceptual-analysis article in *Frontiers in
Psychology* (vol. 17, 2026; received April, published July 2026; three named
reviewers). It reports no experiment. Its only computational artifact is a
supplementary Python toy model, a vector symbolic architecture (VSA) of one
example, which the author calls "a model-building hypothesis". The capture is
the full article text without figures or the supplementary script.
Author: Spencer K. Lynn, a single author at Charles River Analytics (from the
correspondence address). He has prior work on Bayesian predictive-processing
cognitive architectures (Scruff, 2019) and on embodied generative agents
(AAAI symposium, 2023), which this paper builds on. The author reports using
Gemini and ChatGPT for literature review and Copilot to generate the toy code.

## Summary

The paper asks what decides which elements of two source concepts are
inherited into a blend. Conceptual blending (Fauconnier and Turner's
conceptual integration theory) is the construction of a new concept from a
selective combination of source features; "house boat" and "boat house" take
different features from the same two sources. Lynn's answer is that a goal
selects the features. In humans the goal is "foregrounding" features relevant
to it: in the running example, the goal of understanding a never-seen Osprey
tiltrotor selects propeller orientation and wings from "helicopter" and
"airplane" and ignores window count. He proposes predictive processing as a
candidate mechanism. A goal or context node is a parent in a generative
hierarchy. It raises the precision of goal-relevant features, roles and
affordances of the co-active source concepts and lowers the precision of
irrelevant ones. A blend node integrates the selected features into a
hypothesis tested against observations, simulations, linguistic context or
action possibilities. Prediction error, generated when the blend fails the
goal, revises which features are kept. Human goals are ultimately rooted in
physiological regulation (allostasis); "goal" is used at neurocognitive,
behavioral and toy-model levels, which the paper separates. For language
models, Lynn proposes "proxy-goals": the purposiveness comes from instruction
tuning, RLHF and DPO, prompt framing, the context window, in-context learning
and decoding, not from an internal causal model of a goal. Blending arises as
the model "composes statistically associated features, roles, and
constraints" into a continuation; the outputs are "distributionally novel
blends". The goal "is a proxy signal that steers token probabilities" and is
"more like working-memory than a revisable, hierarchical controller". Lynn
then claims three differences. First, LLMs hold linguistic traces of
image-schematic and force-dynamic structure (containment, support, blockage
and similar patterns) without the perception-action grounding that makes them
operative constraints. Second, attention-weighted superposition means
conflicting constraints produce interference during decoding: tokens
"lexically consistent with all constraints while not satisfactorily
addressing any", which he calls "generic compromises". Third, in-context
learning gives short-term adaptation but no lasting model change, and
reflection needs prompted scaffolding. He qualifies these as differences of
organization, not an all-or-none opposition. The proposed remedy is an
"intermediate affordance layer" in which a goal becomes an affordance
specification, then a candidate, a causal test and a revision. Every
mechanism claim is conceptual.

## Contribution assessment (our opinion)

The problem is real and old: conceptual integration theory describes
selective projection well but has said less about what drives the selection.
The paper's main addition is a clearly stated candidate answer: the goal is
a precision-setting parent node, with error-driven revision of the blend.
That answer connects blending theory to predictive-processing vocabulary, and
it makes "goal-relevance" an explicit selection variable rather than an
after-the-fact description. The human mechanism is a reasonable synthesis of
existing predictive-processing accounts of concepts (Michel) and goals
(Barrett). The author hedges it properly as one candidate within a contested
program. It is not tested: the VSA toy shows only that the selection
can be implemented, and the paper gives no observation that would distinguish
it from rival accounts of selective projection. The LLM side is weaker as a
mechanism claim. "Proxy-goal" mostly relabels a widely accepted point, that a
model's apparent purposiveness comes from training, alignment and the prompt.
The superposition-to-"generic compromise" step cites only toy-model
superposition work (Elhage et al.) and offers no measurement of compromise
outputs. The most testable contribution is that generic-compromise
prediction, together with the claim that an affordance layer would reduce
it. Neither is tested here. Originality relative to Sato (2025) on
prompt-induced blending in LLMs, which the paper cites, cannot be judged from
this capture.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the workshop's question, this source is the anchor statement of
goal-selected projection as the *productive* mode of blending. It is the
first artifact in the KB to treat conceptual blending at all. It enters the
KB as a conceptual comparison partner, not as evidence: every connection
below is a comparison, because the paper offers no data.

It compares with [LLM generation can hide a relaxed goal where human writing
exposes a stall](../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md)
on what LLM output looks like when a set of constraints cannot all be met.
That note conjectures an argmax over plausibility that silently drops one
conjunct. Lynn conjectures superposition interference that addresses every
constraint weakly. The two rival mechanisms predict different signatures:
one conjunct missing, against all conjuncts thinly served. Neither has been
measured.

It compares with [Human analogies can motivate functions without determining
component boundaries](../theory/human-analogies-suggest-functions-not-component-boundaries.md)
on inferring an engineered architecture from a human cognitive mechanism.
Lynn's "intermediate affordance layer" moves directly from a human
predictive-processing hierarchy to a recommended AI component. The note's
test separates the function that may transfer (goal-conditioned feature
selection with error-driven revision) from the component boundary that does
not follow.

It compares with [Psychology-to-agent transfer needs per-principle
failure-mode testing](../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md)
on goal-gated selection. That note judged goal-relevant filtering of memory
retrieval mostly decorative for agents. Lynn's goal gates which features
enter a constructed concept, not which memories are retrieved, so the
earlier verdict does not obviously cover it.

It compares with [Knowledge storage does not imply contextual
activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md)
on available against operative knowledge. Lynn's claim that LLMs hold
"linguistic traces" of image schemas without making them "operative
constraints" draws the same distinction. He locates the missing gate in
embodied grounding; the note locates it in contextual activation.

It compares with [World models assess explanatory-reach through
action-conditioned prediction](../theory/world-models-assess-explanatory-reach-through-action-conditioned.md)
on closed act-test-revise loops. Lynn's "goal to affordance specification to
candidate realization to causal test to revision" applies that loop to
concept construction.

It compares with [LLM learning phases fall between human learning
modes](../theory/llm-learning-phases-fall-between-human-learning-modes.md)
on mapping LLM adaptation onto human learning. Lynn's third difference treats
in-context learning as short-term adaptation without lasting change. The note
argues the phases do not map one-to-one onto human modes, which bounds how far
that contrast can be read as a dichotomy.

Among sources, it compares with the [seed-programmed autonomous general
learning ingest](./seed-programmed-autonomous-general-learning.ingest.md) as
another architecture proposal for goal-driven causal model construction and
revision; Thórisson's has implementation cases, Lynn's has a toy script. It
compares with the [interpolation, extrapolation, hyperpolation
ingest](./interpolation-extrapolation-hyperpolation.ingest.md), whose
vocabulary for novelty relative to a training distribution could make Lynn's
"distributionally novel blends" more precise.

Lynn's interference claim should not be added to the empirical
irrelevant-context studies already in the KB as one more instance of a common
mechanism. It concerns conflicting task constraints, not unlicensed context
content, and it is not measured.

## Learning Claims (our opinion)

**The mechanism on its own terms.** In Lynn's human account, a blend is a
hypothesis built under a goal and revised by error. The goal node sets
precision over source features. The blend node predicts observations.
Prediction error flows upward and changes which features are retained,
suppressed or reweighted, cycle by cycle, until the blend is stable. In the
Osprey example, "helicopter" and "airplane" each fail as whole categories,
but selected features of each jointly explain the observed flight. For LLMs,
Lynn claims adaptation is transient: in-context learning can approximate
Bayesian updating, but there is no "lasting model change or explicit causal
roll-out", and reflection depends on prompted protocols rather than an
intrinsic uncertainty-aware controller.

**Mapping onto Commonplace concepts.** Judged against [theory
builder](../theory/definitions/theory-builder.md), the human blending loop as
Lynn describes it meets *consumption* (the blend governs categorization and
action) and *iteration* (error results shape the next cycle). It is close to
*criticism* in form (the blend is tested against observations), but the error
signal is precision-weighted belief update, not criticism aimed at what a
stated unit says. Its *localized content* is at most the toy model's labeled
VSA vectors; in the brain the paper claims no stated units. So it maps onto
the gradient-like error elimination the definition contrasts with criticism,
not onto theory building. That mapping is ours; Lynn does not use these
terms. Persistence of the human blend is claimed across encounters (blends
become "entrenched") but not argued. For the LLM side, Lynn's "no lasting
model change" matches the KB's within-episode persistence grade for
in-context adaptation. His view that the remedy is an internal controller
differs from Commonplace's route, which keeps revision in external,
addressable artifacts. Lynn does not consider that alternative.

**What it adds or questions.** Under [learning inside a fixed decomposition
inherits its
mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md),
Lynn's account fixes the decomposition outside the learner: the source
concepts, the goal and the image-schema vocabulary are supplied, and only
precision over features is updated. The Osprey blend improves within that
space; the account does not say how a wrong source pair or a missing image
schema gets corrected. The paper's learning claims are a plausible mechanism
at best. No improvement is observed and no causal evidence is offered, so
they neither support nor challenge the KB's account. They add one useful
distinction: selection by goal relevance and correction by error are separate
operations, and the second is what keeps the first honest.

## Extractable Value

1. **The role of goals in Lynn's theory, in his terms** -- the goal answers the "central puzzle" of what motivates the inheritance of specific source elements. It foregrounds goal-relevant features and lets the blend omit goal-irrelevant ones. In the predictive-processing implementation, the goal is a parent node that raises precision of expected-relevant features and lowers precision of irrelevant or misleading ones, and the blend is then tested; prediction error, generated "when the candidate blend fails to satisfy the goal", revises the selection. Goals are disambiguated by level: allostatic regulation, behavioral task or desired state, and high-level prediction in the toy model. For the workshop, the key point is that selection and test are coupled in one loop: goal relevance chooses features, and observation decides whether the combination holds. [quick-win]
2. **The proposed LLM mechanism, in his terms** -- language models produce "distributionally novel blends" under "proxy-goals" supplied by instruction tuning, RLHF/DPO, prompt framing, the context window, in-context learning and decoding. Blending is the composition of statistically associated features through attention-weighted superposition. The goal is externalized ("residing in the context window, the instructions, and human preferences"), acts "more like working-memory than a revisable, hierarchical controller", and does "not encode explanations of why a particular blend should exist or how it would work". The paper explicitly says LLMs have structured representations; the claimed difference is the source and grounding of purposiveness and whether the control loop is closed. [quick-win]
3. **A tension for the workshop's watched failure** -- the workshop watches two useful ideas being fused because both serve one goal. Lynn presents goal-selected fusion as blending working correctly. On his account, what separates a productive blend from an unsupported relation is not the selection but the subsequent test against observation. His LLM account gives the model the selection without that internal test. Read that way (our interpretation, not Lynn's claim), an unsupported relation would be a goal-selected blend that no error signal has checked. This is a conjecture for the workshop to weigh, not evidence. [experiment]
4. **Two rival signatures for unsatisfiable constraints** -- Lynn's "generic compromise" (all constraints thinly addressed) and the KB's relaxation note (one constraint silently dropped) predict observably different outputs. A small comparison on prompts with deliberately conflicting constraints could discriminate them. Both are unmeasured conjectures at present. [experiment]
5. **A fresh case for the function-versus-boundary test** -- the affordance-layer recommendation is a direct human-to-AI component inference. The transferable function is goal-conditioned selection plus error-driven revision; whether it needs a dedicated affordance layer, or can live in external artifacts or tool loops, is not argued. [just-a-reference]
6. **Pointer to the direct LLM-blending source** -- Lynn cites Sato (2025), "The way we prompt: conceptual blending, neural dynamics, and prompt-induced transitions in LLMs" (arXiv 2505.10948), as evidence that LLMs blend. It is not ingested and may carry the empirical content this paper lacks. [just-a-reference]

## Limitations (our opinion)

Nothing in the paper tests its mechanisms. The human account is one candidate
implementation inside predictive processing, a program the author himself
calls broad and contested. The paper offers no observation that predictive
processing explains and a simpler selective-projection account does not. The
Osprey walkthrough is an illustration whose outcome is built into its setup:
the goal node is defined so that the right features win. The toy VSA script
was not in the capture and is described as an in-principle demonstration.

The LLM mechanism is hard to vary in only one place, the generic-compromise
claim; elsewhere "proxy-goal" absorbs any source of LLM purposiveness
(training, alignment, prompt, tools, decoding), so it rules out little. The
superposition-to-compromise step rests on toy-model superposition work, not on
evidence about decoding under conflicting constraints. It may also be
explained more simply: an aligned model hedges or averages under conflicting
instructions without any representational interference.

The three differences are stated as a contrast with an idealized human. The
claim that "humans detect and repair incoherence proactively" ignores the
large human literature on unnoticed incoherence. The comparison is therefore
asymmetric: LLM brittleness is described from engineering observations, human
competence from theory. The paper does not discuss how goal-driven selection
fails in humans, for example motivated or goal-congruent projection that
stabilizes because no disconfirming observation arrives. That is exactly the
failure the occasion concerns, so the paper says nothing direct about when
goal-selected blends go wrong.

The capture omits the four figures and the supplementary code; the text
describes them sufficiently for this analysis.

## Recommended Next Action

Update the E20 entry in the epistemic-relevance-and-conceptual-blending
workshop's evidence register with Lynn's two-part answer (goals set precision
over source features and are coupled to an error test in humans; LLM goals
are externalized proxy-goals with no internal error-driven revision), marked
as conceptual and untested. Record the tension in Extractable Value item 3 as
an open question for the workshop's review point.

---

Relevant Notes:

- [Conceptual blending in humans and language models (Lynn 2026)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1849083/full) — derived-from: the analysis is worked out from this article
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) — compares-with: rival conjectural mechanisms for LLM output under unsatisfiable constraints
- [Human analogies can motivate functions without determining component boundaries](../theory/human-analogies-suggest-functions-not-component-boundaries.md) — compares-with: inferring an AI component from a human cognitive mechanism
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — compares-with: goal-gated selection in concept construction versus memory retrieval
- [Knowledge storage does not imply contextual activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md) — compares-with: available versus operative knowledge
- [World models assess explanatory-reach through action-conditioned prediction](../theory/world-models-assess-explanatory-reach-through-action-conditioned.md) — compares-with: closed act-test-revise loops
- [LLM learning phases fall between human learning modes](../theory/llm-learning-phases-fall-between-human-learning-modes.md) — compares-with: mapping in-context adaptation onto human learning modes
- [Seed-programmed autonomous general learning](./seed-programmed-autonomous-general-learning.ingest.md) — compares-with: architectures for goal-driven causal model construction and revision
- [Interpolation, extrapolation, hyperpolation](./interpolation-extrapolation-hyperpolation.ingest.md) — compares-with: novelty relative to a training distribution
