# Audit: a context-operation interface bounds context policy

This is the Step 8 audit of `draft.md` in new-write mode. There is no
`original.md`, so no incumbent-reconciliation check applies. The findings below
follow the required audit order and do not rewrite the draft.

## 1. Claim delta against the skeleton

Status: resolved

Finding: CD-1 — The planned causal and scope structure is otherwise preserved.

Anchor: the opening and mechanism in `draft.md:9-13`, especially “Holding the
retained substrate, model, and resource budget fixed, the interface bounds the
projections that policy can realize,” “define `Reach(I, S, x; M, B)`,” and
“Those gains do not add a view outside `Reach`”; the planned applications in
`## Architectural contrasts`, `## Evaluation consequence`, and `## Scope`.

Action: `keep`

Basis: these passages realize the claim skeleton's eight-paragraph plan in its
specified order. They keep the central result conditional on fixed substrate,
model, and budget; distinguish structural reach from achieved use; treat
controller gains as within-interface gains; preserve the source-tier and
non-ranking limits; and add no benchmark quantity. The draft also preserves the
skeleton's confidence: the reachable-set account is presented as a local
definition and inference, while named-system statements are scoped to described
architectures or pinned static wiring. Apart from CD-2 and CD-3 below, no
planned commitment is omitted or altered in causality, scope, confidence,
quantity, or recommendation.

Resolution: Kept the justified causal and scope structure in `candidate.md`.

Status: resolved

Finding: CD-2 — The access/transformation sentence is a draft addition to the
ordered paragraph plan, but it is already authorized support.

Anchor: `draft.md:11`, “In particular, [access and transformation impose
distinct burdens](./access-burden-and-transformation-burden-are-distinct-query-dimensions.md):
finding retained input does not imply that the interface can turn it into the
view the call needs.”

Action: `keep`

Basis: the ordered paragraph bullets do not call for this sentence explicitly,
so it is a claim delta. Claim-disposition item 6, however, explicitly assigns
the distinction `cite existing` and authorizes only its interface-design
consequence here. The cited note establishes the system-relative separation of
locating inputs from transforming them, and the sentence performs one local
mechanism job rather than opening a second claim cluster.

Resolution: Kept the cited local consequence in `candidate.md`.

Status: resolved

Finding: CD-3 — The draft omits the skeleton's load-bearing definition of the
fixed budget.

Anchor: `draft.md:9`, “Holding the retained substrate, model, and resource
budget fixed,” and `draft.md:11`, “fixed budget `B`.”

Action: `clarify`

Basis: the skeleton defines `B` as including active-context, call, time, and
tool limits where applicable. The draft names `B` but never makes those
components recoverable. Which resource caps are fixed changes the legal traces
and therefore `Reach`; this is a planned truth condition, not decorative
detail.

Resolution: Added that `B` includes applicable active-context, model-call,
time, and tool-use limits.

## 2. One-importable-proposition artifact shape

Status: resolved

Finding: AS-1 — The title, description, opening, and body expose one importable
central proposition.

Anchor: the description, “improving context selection within a fixed operation
interface cannot establish that the interface admits every useful
active-context projection”; the title, “A context-operation interface bounds
the projections its policy can realize”; the opening claim at `draft.md:9`; and
the body sections `## Architectural contrasts`, `## Evaluation consequence`,
and `## Scope`.

Action: `keep`

Basis: claim-disposition item 1 assigns exactly this proposition as the central
contribution. The description is a discriminating retrieval filter, the title
is a composable claim, and the opening states the fixed-premise form before any
examples. The comparison paragraphs witness operation/composition and
controller-placement differences; the evaluation paragraph derives a use of
the same bound; and the scope paragraphs limit it. None needs an independent
citation or revision boundary. The traits `title-as-claim`, `has-comparison`,
and `has-external-sources` are authorized by `kb/types/note.md`; omission of
`synthesis` correctly preserves the default body-composability rule.

Resolution: Kept the title, description, opening, section shape, and authorized
traits in `candidate.md`.

## 3. Grounding against reconstruction and actual sources

Status: resolved

Finding: G-1 — The central formalization and internal premises preserve their
epistemic roles.

Anchor: `draft.md:9-13`, especially the local definition of
“context-operation interface,” the definition of `Reach`, and “This is the
context-projection instance of the more general result that [learning inside a
fixed decomposition inherits its omissions](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).”

Action: `keep`

Basis: the interface definition and selected contribution come from
authoritative user direction; they are not presented as an empirical source
result. `Reach` and the policy-bound conclusion are the reconstruction's
explicit structural inference from the definitions. The linked runtime,
access/transformation, fixed-decomposition, and storage/activation notes state
the internal premises the draft imports. The causal force remains conditional:
when observations, computation, tools, model capability, budget, or editable
operation definitions change, the draft says a premise changed.

Resolution: Kept the formalization and internal premises with their existing
conditional force.

Status: resolved

Finding: G-2 — The three ingest-dependent architecture claims require the
promotion source guard.

Anchor: `draft.md:17`, “A [practitioner account of recursive language
models](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md)
describes model-authored programmatic search and transformation before explicit
exposure or return,” “The paper-described
[lambda-RLM](../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md)
replaces arbitrary programs with a small typed combinator language,” and
“Paper-described [agentic context
management](../sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md)
fixes two memory operations and learns when to invoke or abstain from them.”

Action: `ground`

Basis: these are substantive named-source dependencies. Their retained Quotes
appear proposition-matched: the RLM Quotes cover model-written transformation,
printed exposure, and symbolic return; the lambda-RLM Quotes cover replacement
of open-ended code with a fixed typed combinator runtime; and the ACM Quotes
cover the two operations plus learned invocation and abstention. Promotion must
still apply the required grounding-alignment guard to each use. The ingests'
Summary, Connections, and Extractable Value sections are analysis and are not
source support.

Resolution: Applied `semantic/grounding-alignment` through each ingest's direct
Quotes route. The RLM extracts support model-written exploration and
transformation plus printed or returned exposure; the lambda-RLM extracts
support replacing arbitrary code with a fixed typed combinator runtime; and the
ACM extracts support exactly two context-management tools plus learned
invocation and abstention. All three uses pass. The RLM sentence in
`candidate.md` was narrowed to those retained terms. No snapshot was used and
no Quotes were added.

Status: resolved

Finding: G-3 — The Virtual Context and Letta architecture claims also require
the promotion source guard, which is not presently satisfiable from retained
Quotes.

Anchor: `draft.md:19`, “Pinned static reviews show [Virtual
Context](../agent-memory-systems/reviews/virtual-context.md) using a host proxy
to assemble an initial view and
[Letta](../agent-memory-systems/reviews/letta.md) combining pushed core blocks
with model-requested access to other retained material.”

Action: `ground`

Basis: the pinned code-grounded reviews support the wording at audit time:
Virtual Context's reviewed request path assembles and injects selected material
before the provider call, while Letta's reviewed prompt path pushes core blocks
and leaves recall/archive content behind explicit agent-called tools. The
sentence correctly limits that evidence to static wiring. It nevertheless makes
two substantive named-source dependencies, so promotion requires the direct
tracked-source guard rather than reliance on review prose alone. The tracked
Letta ingest exists but its complete Quotes section says that no source quotes
have been retained; no direct Virtual Context ingest exists under `kb/sources/`.
The required grounding therefore needs new retained direct-source evidence for
these two uses.

Resolution: Removed both named-system dependencies from `candidate.md`. The
candidate states host/proxy and mixed push/pull controller placement as
analytical interface categories, so no Virtual Context or Letta source claim
remains to ground.

Status: resolved

Finding: G-4 — Source fact, cross-system inference, user-directed scope, and
unsupported performance completion remain visibly distinct.

Anchor: `draft.md:17`, “The comparison is between source-described
architectures, not verified executions or a performance ranking”; `draft.md:19`,
“Static wiring supports these architecture descriptions, not runtime
correctness” and “controller placement does not by itself determine structural
reach”; and `draft.md:29`, “They do not estimate the causal performance effect
of changing any one coordinate.”

Action: `keep`

Basis: the first two qualifications preserve the practitioner/paper versus
pinned-code evidence tiers recorded in reconstruction. The controller-placement
sentence is the reconstruction's analytical inference from independently
defined coordinates, not attributed to any source as a measured result. The
non-ranking and tradeoff language is the user-directed scope boundary expressed
as possibility, and the draft supplies no unsupported benchmark, runtime-
correctness, or causal-performance completion.

Resolution: Kept the source-tier, inference, and non-ranking qualifications for
the retained source claims; removed the two static-review claims whose direct
source grounding was unavailable.

## 4. Specificity at load-bearing truth conditions

Status: resolved

Finding: SP-1 — “Retained substrate” currently sweeps projectable state and
retained controller state into one definition even though the argument treats
them differently.

Anchor: `draft.md:9`, “The retained substrate is state available outside a
bounded model input,” together with `draft.md:19`, “Changing a retained
invocation policy is not by itself a change to operation semantics or
composition rules.”

Action: `clarify`

Basis: reconstruction explicitly separates retained controller state, such as
a learned invocation policy, when it selects projections but is not itself
projected into the current input. The opening's unqualified definition can make
that policy part of `S`, even though the formalization treats policy as the
selector over traces and permits policy improvement while the retained
substrate is fixed. The boundary between projectable retained material and
retained selector state changes which premise an intervention changes, so it is
load-bearing.

Resolution: Defined the retained substrate as projectable retained state and
separated retained controller state when it selects projections without itself
being projected.

Status: resolved

Finding: SP-2 — “A rival” does not identify the comparison that can test
interface adequacy.

Anchor: `draft.md:23`, “Testing interface adequacy requires a rival or
constraint-changing intervention.”

Action: `clarify`

Basis: a rival controller operating over the same operation set would remain a
within-interface test, while the reconstruction specifically requires a rival
operation/composition set or another constraint-changing intervention. Leaving
the noun implicit changes the licensed implication of the evaluation test.

Resolution: Replaced “a rival” with “a rival operation/composition interface.”

## 5. Relevance and audience

Status: resolved

Finding: RA-1 — The draft stays addressed to runtime designers and evaluators,
and each paragraph performs work required by that audience.

Anchor: `draft.md:9-13` defines the comparison object and mechanism;
`## Architectural contrasts` supplies the two discriminating contrast families;
`## Evaluation consequence` supplies the controlled-coordinate test; and
`## Scope` separates reach from activation and expressivity from preference.

Action: `keep`

Basis: this matches the brief's reader outcomes. The draft omits Scroll, Prime
Agent, Fractal, AgeMem, Recuris, OpenViking, Playground, the optional boundary
cases, benchmark quantities, and matrix statistics exactly as the skeleton
directs. The five retained named systems each distinguish either composition
language or controller placement. No paragraph becomes a survey entry, and the
notation and source-tier qualifications are introduced where an evaluator
needs them.

Resolution: Kept the audience-facing structure while removing the two
unnecessary named controller-placement examples; the analytical placement
contrast remains.

## 6. Compression and prose

Status: resolved

Finding: CP-1 — The remaining repetition is functional rather than filler.

Anchor: `draft.md:13`, “Those gains do not add a view outside `Reach`, nor do
they show that excluded projections are unnecessary,” and `draft.md:23`,
“Gains with one fixed operation set show that a policy was useful in the tested
regime. They do not establish that excluded operations are unnecessary.”

Action: `keep`

Basis: the first occurrence completes the mechanism's inference; the second
turns it into the evaluator-facing interpretation required by the commission.
Likewise, the two contrast paragraphs reuse RLM and ACM for different
coordinates rather than repeating system descriptions. The draft has no setup
or recap paragraph, no exhaustive table, and no prose branch that can be cut
without losing a planned definition, inference, application, or boundary.

Resolution: Kept the functional repetition and compressed structure.

## Counts and evidence needs

- `keep`: 7 findings
- `remove`: 0 findings
- `ground`: 2 findings, covering five named-source dependencies
- `clarify`: 3 findings
- `ask user`: 0 findings

No finding needs user input. G-2 can use evidence already retained in the three
ingests' Quotes sections, subject to the required promotion guards. G-3 needs
new retained direct-source evidence for the Virtual Context and Letta uses
before those named-source dependencies can pass promotion.
