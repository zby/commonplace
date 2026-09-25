---
description: "Conjecture and criticism, causal self-representation, and persistent artifact editing supply different precedents for a theory builder's operations; similarity on one does not establish the others"
type: note
traits: [title-as-claim, synthesis, has-external-sources]
tags: [learning-theory, deploy-time-learning, self-improving-systems, foundations]
---

# Theory building has distinct epistemic, structural, and implementation precedents

A system can criticize a theory of an external subject without representing
itself. It can use a causally connected self-representation without criticizing it.
It can also edit persistent files without formulating criticism of what a
theory says. These possibilities separate three questions when comparing
systems: how errors are criticized, what the representation is about, and
how changes persist and affect operation. A precedent for one does not
establish the others.

A [theory builder](./definitions/theory-builder.md) names the system that
proposes theories, acts on them, criticizes what they say, and builds on the
result. [Reflection](./definitions/reflective-system.md)
adds a relation between a system and a representation of itself. Retained
text and code around a fixed model supply one implementation. Keeping these
questions separate makes both attribution and experiment design more precise.

## Popper supplies the epistemic basis

Popper's schema, `P1 → TT → EE → P2`, describes problems, tentative theories,
attempted error elimination, and the further problems that result. Criticism
can replace a theory or expose a new problem; the schema does not prescribe
local edits or a repository layout
([A Realist View of Logic, Physics, and History](../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
His treatment of linguistic formulation and criticism includes informal
arguments before symbolic formalization
([Epistemology Without a Knowing Subject](../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).

Commonplace adds the conditions for attributing this method to a particular
system: its theories are stated in localized units, guide its decisions
through what they say, are criticized for what they say, and are revised
through iteration, where the result of criticism shapes the next round.
How far that result persists is graded. These conditions contain no success
condition. Whether a builder improves its
capacity for future action is a separate learning claim, tested rather than
assumed. Artifact availability alone does not establish the conditions, and a
changed decision does not establish improvement. The epistemic basis therefore
leaves work for a concrete account of consumption, consequences, and
persistence.

EITHER and FORTE serve a narrower role as precedents for connecting failed
consequences to candidate repair locations. Their proof-guided repair shows
what [addressability](./definitions/addressable-theory.md#precedent)
can make possible under a supplied representation. It does not define every
tentative theory, require small revisions, or establish the same capability
for interpreted prose. One invocation over a supplied theory and training set
is a theory builder at a low grade of persistence: the repaired theory is a
new conjecture, re-tested on the examples, and nothing persists beyond the run
([theory builder, boundary cases](./definitions/theory-builder.md#boundary-cases)).
Their precedent value lies in assigning blame, not in persistence.

## Reflection supplies the structural relation

Computational reflection supplies the causally connected self-representation
relation inherited by the [reflective-system definition](./definitions/reflective-system.md#provenance-and-departures).
Runtime models and requirements representations give concrete ways to expose
selected aspects of a system to its own operation.

In Rainbow, probes and gauges update an architectural model; a constraint
evaluator triggers adaptation through supplied strategies and effectors.
Its specified types, properties, operators, and strategies determine the
available adaptations. That is a working model-to-system path, not evidence
that the system learns those choices
([Rainbow (snapshot required)](../sources/rainbow-architecture-based-self-adaptation.ingest.md),
architecture-layer infrastructure and architectural style).
Requirements Reflection proposes runtime requirements objects synchronized
with an architectural representation. The synchronization is a design
challenge in that paper, not an evaluated learning mechanism
([Requirements Reflection (snapshot required)](../sources/requirements-reflection-runtime-entities.ingest.md),
challenges 1–2).

These comparisons matter when the theory concerns the modifying system's
organization. A runtime self-model can be causally operative while its
assumptions are closed to criticism. Conversely, a theory builder whose theories
concern an external subject need not be reflective. Improving an adaptation outcome
does not by itself establish learning of the model or its revision machinery.

## Persistent workspaces supply an implementation comparison

Workspace Optimization keeps model weights fixed while revising typed code
and role context. Prediction failures are routed to responsible surfaces,
and replay supplies feedback on earlier transitions after edits. Its DreamTeam
implementation uses a supplied role decomposition and evaluation machinery
([Workspace Optimization (snapshot required)](../sources/workspace-optimization-how-to-train-your-agent.ingest.md),
§§2–4 and Appendix B).

This is a concrete comparison for keeping learned changes in artifacts that
later calls consume. It does not establish learning of a continuing system's
own improvement procedure. The retained source reports adaptation within game
runs. Changes carried across the levels of one run meet the iteration
condition when criticism aims at what the revised code and context say; their
persistence reaches the run, not later sessions. The benefit of the complete arrangement also does not isolate the effect of
criticism, addressability, or retaining an assembled theory.

Fixed weights constrain where learned changes persist. They do not hold model
processing fixed across different inputs, establish content use, or show that
explicit artifacts outperform reconstruction. Those are separate comparisons
of [the arrangements actually run](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

## Research positioning and comparison

Commonplace's [research arrangement](./commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#research-program-and-development-path)
pursues recursive self-improvement within Schmidhuber's broad program, using
interpreted methodology and selective codification. This states the research
objective and chosen realization, a theory builder whose learning is under
test. It does not replace the Popperian account
of criticism or the structural condition for reflection, and it supplies no
result showing that the combined arrangement works.

A comparison should therefore name which question it asks. A runtime-model
comparison concerns what criticism aimed at what a theory says adds to
learning beyond a causally operative self-model. An editable-workspace
comparison concerns the supplied theory and its use beyond persistence and
repair. A persistence comparison concerns which work is kept rather than
reconstructed, and for how long. None can inherit the conclusion of another
merely because the systems share some machinery.

## Scope

These are bounded conceptual and implementation precedents, not a priority
claim or an exhaustive ranking of earlier systems. A full claim that a
reflective theory builder learns needs connected evidence of theory use, consequences, criticism, and
later influence, plus evidence of improved capacity. Partial findings remain
reportable at their own strength. Neither their combination nor resemblance
to a predecessor establishes superiority over simpler arrangements.

The precedents already supply recurrent use of revised theories, incremental
revision, localized repair, a bounded sample-efficiency result, and
human-engineered seeds. This program must not claim those features as new.
Fixed supplied machinery is not inherently defective when it is warranted
general machinery over the declared reach.

---

Relevant Notes:

- [Theory builder](./definitions/theory-builder.md) — defined-in: the four conditions for attributing conjecture and criticism to a system, with learning left to test
- [Reflective system](./definitions/reflective-system.md) — grounds: causal self-representation is separate from learning
- [Addressable theory](./definitions/addressable-theory.md) — contrasts: a structural property whose expected benefit is empirical
- [Machinery persists by warrant, not position in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — grounds: supplied machinery is assessed by its warrant over the declared reach
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — extends: learning within supplied choices does not establish their adequacy
