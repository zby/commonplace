---
description: "Lamport argues prose proofs hide their own logical structure; hierarchical numbered steps with named justifications make each step separately checkable, on twenty years of anecdotal practitioner evidence"
source: https://lamport.azurewebsites.net/pubs/proof.pdf
captured: "2026-08-27"
capture: pdftotext
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 3fb23c0f0718e408105bfffff1b496a34ca1bb36b082731393594ceedae52145
ingested: "2026-08-27"
type: kb/sources/types/ingest-report.md
domains: [proof-structure, verifiability, decomposition, writing-conventions]
---

# Ingest: How to Write a 21st Century Proof

## Classification

An argumentative methodology essay: it advocates a way of writing, works one
example (Spivak's corollary to the Mean Value Theorem) through successive
revisions, specifies a notation for the method, and answers objections. Section 5
is a practitioner report embedded in that argument — twenty years of personal
use, two referee comments, one correspondent's email, one re-found published
error — so the practitioner lens applies alongside the essay lens below. The
capture is a `pdftotext` extraction of the author's own PDF; prose is faithful,
but reflowed mathematical notation is lossy in places, so formula-bearing spans
are poor candidates for verbatim retention.

Author: Leslie Lamport — Turing Award winner, author of the earlier *How to Write
a Proof* (1993/1995), and designer of TLA+ and its TLAPS prover. Strong authority
on the method and on the formal end of it; the evidence he offers for its effect
on error rates is explicitly anecdotal and self-reported.

## Summary

Lamport argues that mathematical notation modernized while proofs did not: proofs
are still 17th-century prose, which makes them hard to read and easy to get wrong.
Prose hides two things a checker needs — whether a sentence asserts or justifies,
and which previously stated facts a justification uses. His remedy is two
principles, structure and naming: write the proof as numbered steps, give every
step an explicit justification citing named facts, and expand any step recursively
into a sub-proof rather than a lemma when its justification grows past a line.
Hierarchical numbering then scopes citation — a step may cite only names visible at
or above its own level, because a step proved under an assumption does not hold
outside it — and a mandatory terminal Q.E.D. step forces the proof to end at what
was to be shown. Working Spivak's four-sentence textbook proof through this
transformation exposes a first step that cannot be proved, an unstated appeal to
a numbered theorem, and a missing explanation of why the proof proves the
corollary. How far to expand a step is set by the checker, not by the material:
"if the truth of a statement is not completely obvious, or if you suspect that
there may be just the slightest possibility that it is not correct, then more
detail is needed," and a student needs more than a mathematician. Levels of about
four to ten steps read best. Lamport is careful about what this buys — structured
proofs make error elimination "possible, not inevitable" — and about cost: the
structured version of Spivak's proof runs about 40% longer, and he expects
machine-checked proofs to stay impractical for mathematicians for decades, while
arguing that learning to write the formal form teaches the informal one.

## Quotes

- **Source extract (verbatim):** How much detail is necessary? For example, why do 1.1 and the hypothesis of the corollary, which asserts that f is differentiable on I , imply that f is differentiable on [a, b]? The proof is assuming the fact that a and b in the interval I implies that [a, b] is a subset of I . Should this also be mentioned? If you are writing the proof to show someone else that the theorem is correct, then the answer depends on the sophistication of the reader. A beginning student needs more help understanding a proof than does a mathematician. If you are writing the proof for yourself to make sure that the theorem is correct, then the answer is simple: if the truth of a statement is not completely obvious, or if you suspect that there may be just the slightest possibility that it is not correct, then more detail is needed.
  - **Source location:** Section 3, "Hierarchical Structure", p. 7 (paragraphs beginning "How much detail is necessary?")
- **Source extract (verbatim):** My earlier paper on structured proofs described how effective they are at catching errors. It recounted how only by writing such a proof was I able to re-discover an error in a proof of the Schroeder-Bernstein theorem in a well-known topology text [2, page 28].
  - **Source location:** Section 5, "Experience", p. 16
- **Source extract (verbatim):** Eliminating errors requires care. Structured proofs make it possible, not inevitable.
  - **Source location:** Section 5, "Experience", p. 17 (immediately after the correspondent's quoted email)

## Connections Found

This is an anchor for a case the KB does not currently hold anywhere in its
library: how a written artifact's own form is engineered so that a reader can
check it a piece at a time. Nothing under `kb/notes/` or `kb/reference/` treats
structured proof, and the KB names no artifact where step size is stated as a
design variable, so the source opens ground rather than restating it.

Its heaviest bearing is as outside evidence for
[structured output is easier for humans to review](../notes/structured-output-is-easier-for-humans-to-review.md),
which argues from readability alone that separating assertion from justification
converts one holistic judgment into focused per-part checks; Lamport supplies a
long-run practitioner case in a genre where each check has a truth condition,
including a referee who reported the structure "might well be the only way to
present long proofs" both detailed and readable. It is a worked per-convention
instance for
[human writing structures transfer to LLMs because failure modes overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md),
naming the specific failures prose proofs permit and the structural rule
introduced against each, and it supplies a tradition
[the soft-bound survey](../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md)
does not list, in that survey's own terms: the bounded processor is the step's
checker and the adaptation is hierarchical decomposition plus naming.

It also qualifies several existing claims from the authoring side.
[Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md)
bounds evaluation by what an oracle can assess; Lamport makes step size the free
variable that bound fixes, explicitly reader-relative.
[Short composable notes](../notes/short-composable-notes-maximize-combinatorial-discovery.md)
justifies one-claim atomicity by bounded-context co-loading; Lamport reaches a
rule of the same shape from an independent warrant, that the unit is sized so its
checker can decide it.
[The verifiability gradient](../notes/verifiability-gradient.md)
gains an occupied and defended intermediate point, with the far end priced by
someone who built it, and
[causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md)
gains a cost qualification on the proof route.
[Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md)
gets a documented case where they are coupled rather than independent: constraining
the output form is reported to change what the writer does — "Writing the
structured proof of Figure 3 forced us to write a justification for each step."
The proof-sketch discipline ("Proof sketches are fine, but they are not proofs")
is the layout
[an insufficient summary precedes the source rather than replacing it](../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md)
predicts, and the internalized "curious child" who asks *why?* at every assertion,
together with the correspondent who found his error only when rewriting the proof
for another reader, bears on
[the adversarial writing-is-thinking loop](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md).

Among already-captured sources it sits opposite
[MAKER](./meyerson-maker-million-step-llm-zero-errors.ingest.md) on a shared
sizing rule with opposite oracle strength — MAKER decomposes maximally because a
hard per-step oracle exists, Lamport expands until a human checker stops asking
why — and it disagrees with
[Naur](./programming-as-theory-building.ingest.md) on a shared axis: Naur bounds
what a written artifact can carry of the understanding behind it, while Lamport
holds that in the proof case what goes missing is structure and naming, and
demonstrates recovering it. [Agentic code reasoning](./agentic-code-reasoning.ingest.md)
measures the explicit-premise trade Lamport reports qualitatively as about 40%
more space.

## Extractable Value

1. **The checkable unit is sized to its checker.** Lamport states this as an
   authoring rule — expand a step while any doubt remains, and expand further for
   a less sophisticated reader. The KB applies the idea in at least four places
   (note atomicity, review budgets, oracle domain, microagent steps) and states it
   nowhere as a general claim. This source is the outside precedent for writing it
   down. [deep-dive]

2. **Hierarchical numbering scopes which prior claims a claim may cite.** A step
   may legally cite only steps visible at or above its level, because a step
   proved under an assumption does not hold where that assumption is out of scope.
   The KB's traversal-as-reasoning framing in
   [title as claim](../notes/title-as-claim-enables-traversal-as-reasoning.md) has
   no equivalent rule limiting which claims a claim may lean on. [deep-dive]

3. **"Structured proofs make it possible, not inevitable."** A precise statement
   of what artifact form buys and what it does not: the form removes the excuse,
   the diligence still has to be supplied. Directly usable wherever the KB claims
   that structure improves reviewability. [quick-win]

4. **A mandatory terminal step that restates the goal.** Requiring every proof to
   end at what was to be shown structurally forecloses an argument that never
   connects to its own conclusion — an omission Spivak's published proof actually
   has. This is a cheap, transferable rule for claim-bearing document types.
   [quick-win]

5. **Recursive expansion instead of extraction.** When a justification outgrows a
   paragraph, Lamport replaces it with a nested sub-proof rather than a named
   lemma, on the grounds that extraction "would submerge the interesting results
   in a sea of lemmas." That is a live counter-consideration to the KB's default
   of splitting into separate artifacts, and it supplies the nesting rule the flat
   Toulmin section model in
   [claim notes](../notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md)
   lacks. [deep-dive]

6. **Learning the formal form to write the informal one better.** Lamport prices
   full formalization (19 lines of TLA+ definitions for the calculus needed; the
   machine-checked proof itself decades from practical) and still argues the
   formal exercise teaches informal writing. A concrete cost-and-payoff data point
   for movement along the
   [verifiability gradient](../notes/verifiability-gradient.md) and for
   [codification](../notes/definitions/codification.md). [just-a-reference]

## Limitations (our opinion)

This is our editorial judgment, not the author's.

**What is not argued.** The essay's core empirical claim — that structuring
catches errors prose hides — rests on evidence Lamport himself labels anecdotal:
his own twenty years of practice, two referee comments, one correspondent's email,
and one error re-found in a 1955 textbook. That set is selected by outcome. The
successes are visible; proofs he structured that still carried errors, or errors
found without structuring, are not counted. Nothing here separates the effect of
the structural form from the effect of the extra care that adopting an unfamiliar
form occasions, which is the same confound
[process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md)
warns about; Lamport's own "forced us to write a justification for each step"
concedes the coupling without measuring it.

**What is dismissed rather than engaged.** Section 6 answers three objections and
opens by asserting that no objection Lamport recalls was based on a rational
argument. The strongest of them — that structured proofs do not explain why the
proof works — is answered by pointing to proof sketches, which is a change of
medium rather than a reply; the "great literature" objection is answered by an
architecture analogy that is asserted, not tested. Read this section as advocacy.

**Where the claim is scoped narrower than the prose suggests.** The mechanism
depends on the medium: every step is a mathematical assertion with a truth value,
and the checker's question ("why does this follow?") has a determinate answer at
each level. Transfer to a KB of design claims is not licensed by this source,
because a design note's steps are not entailments and there is no analogue of the
appeal to axioms that terminates the child's *why?*. The
[MAKER](./meyerson-maker-million-step-llm-zero-errors.ingest.md) comparison
sharpens this: per-step checking pays where a per-step oracle exists, and this
source does not tell us what to do where one does not.

**Time-bound predictions.** The hypertext argument was written in 2011 and assumed
readers would soon browse proofs as collapsible trees; the "next decade or two"
paper-first premise has partly expired, and the forecast that machine-checked
proof would remain impractical "for decades" is now testable against proof
assistants that have moved considerably since. Neither prediction is load-bearing
for the structural argument, but neither should be cited as current.

## Recommended Next Action

Write a note in `kb/notes/` stating the general claim that the checkable unit is
sized to its checker, citing this ingest as the outside precedent and the KB's
four existing instances — note atomicity in
[short composable notes](../notes/short-composable-notes-maximize-combinatorial-discovery.md),
the review budget in ADR 079, oracle domain in
[warranted autonomy](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md),
and the microagent step in the
[MAKER ingest](./meyerson-maker-million-step-llm-zero-errors.ingest.md) — as cases
of it.
