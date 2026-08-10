# Semantic audit v3

Target: `candidate.md`, with relative links resolved as if the candidate lived in `kb/notes/`.

Scope: all nine complete gates under `kb/instructions/review-gates/semantic/`. Grounding checks used only the candidate's directly linked sources and notes. No incumbent, earlier candidate, workshop history, prior report, transitive link target, or review-store state was inspected.

## Overall result

**PASS with INFO. No material blocker remains.** There are no WARN findings. The only evidentiary caveat is narrow: the source cited at `candidate.md:18` directly supports passive assent to finished prose, but not the candidate's more specific anchoring inference.

## Gate results

### semantic/completeness-boundary-cases — PASS

Anchors: `candidate.md:10`, `candidate.md:12`, `candidate.md:14`, `candidate.md:20`.

The candidate expressly calls the three operations “candidate operations” and “not a canonical or complete taxonomy,” so it does not claim exhaustive coverage. Boundary probes remain coherent:

- An empty challenge report leaves no dispositions to resolve but still produces an inspectable attempt, not evidence that the checker was effective.
- Multiple or upheld challenges map to the per-challenge status and final-disposition requirements at line 14.
- An unresolved challenge at acceptance maps to the explicit unresolved marker; `Investigate` alone remains interim.
- One actor occupying more than one role does not collapse the roles, because line 14 separates role identity from actor allocation.
- Rendering, transcription, and stylistic editing are explicitly outside the unsettled-commitment boundary at line 10.
- Justified rejection is included as an artifact outcome, while persistence without later use is explicitly excluded from the later-system outcome at line 20.

The outcome list is also introduced as “at least three outcomes,” not as a complete taxonomy.

### semantic/conceptual-role-conflation — PASS

Anchors: `candidate.md:10-14`, `candidate.md:20`.

The text keeps the practitioner accounts, the candidate's synthesis, the three operations, possible methods, actor allocations, and measured outcomes in distinct roles. Line 12 is especially explicit that the sources motivate reported practices while the present artifact contributes an unvalidated relocation and synthesis. “Acceptance” is likewise treated as admission authority rather than evidence of an artifact, understanding, or later-system outcome. The occasional broad use of “checks” is resolved by the named operation definitions and does not permit a materially different attribution or contribution.

### semantic/explanatory-reach — PASS

Anchors: `candidate.md:8`, `candidate.md:10`, `candidate.md:14`, `candidate.md:16`, `candidate.md:20`.

The central distinction has a load-bearing mechanism: a defined input plus a stage-specific trace exposes what was attempted and handed off, while correctness and effects require independent adjudication or comparison. Removing or mismatching the recorded input, report, or disposition breaks auditability; adding independent outcome evidence changes what can be claimed about effect. The note also identifies observations that would bear on the stronger claims—critic discrimination, error correlation, upheld-finding dispositions, and comparator-specific outcomes—rather than protecting those claims with an escape hatch.

### semantic/explication-quality — PASS

Anchor: `candidate.md:3` (`type: kb/types/note.md`).

This gate requires `kb/types/definition.md`; the candidate is a note, so the gate's applicability precondition is not met. No explication-quality finding is applicable.

### semantic/grounding-alignment — INFO

Anchors: `candidate.md:12`, `candidate.md:16`, `candidate.md:18`, `candidate.md:20`, `candidate.md:32-35`.

The main grounding routes align:

- The three practitioner sources directly report definite formulation, premise or route exposure, counterexample search, and revision or switching. Line 12 accurately presents them as motivation from reported practice, not controlled validation or a canonical taxonomy.
- `reasoning-production-is-not-reasoning-evaluation.md` supports testing whether a critic distinguishes a valid conclusion from the route actually presented.
- `error-correction-works-above-chance-oracles-with-decorrelated-checks.md` supports discrimination and error-correlation as separate requirements; the candidate correctly treats prompt, runner, or report variation as interventions rather than proof of independence.
- `llm-generation-relaxes-goals-where-human-writing-stalls.md` labels its own mechanism conjectural, matching line 18's qualification.
- `when-is-it-better-to-think-without-words.md` directly reports credible nonsense and false precision as human-writing failure modes.
- The four Relevant Notes support the narrower claims assigned to them: allocation needs independent warrant; inspectability enables review without proving success; discriminative power and decorrelation are distinct; and persistence, activation, and verification are separable.

One inference is plausible but not airtight. At line 18, the substantive-AI-writing source explicitly argues that readers may passively accept an approximate word once prose is already present. It does not itself establish an anchoring mechanism. The candidate's “may” and the open empirical question at line 25 keep this from becoming scope overreach, but “anchor the reviewer” should be read as the candidate's hypothesis, not as a directly sourced result.

### semantic/internal-consistency — PASS

Anchors: `candidate.md:10`, `candidate.md:12`, `candidate.md:14`, `candidate.md:16`, `candidate.md:18`, `candidate.md:20`.

The sections preserve the same distinction throughout: records establish attempted execution and inspectability, not correctness, justified disposition, comparative benefit, or a composition-equivalent outcome. `Investigate` as an interim status is consistent with accepting an explicit unresolved marker as a final disposition. Distinct roles do not become distinct actors, and the closing claim does not expand beyond the evidence limits established earlier.

### semantic/load-bearing-qualifiers — PASS

Anchors: `candidate.md:8-10`, `candidate.md:16`, `candidate.md:20`.

The central qualifiers do work. “Recorded” supplies the audit trail; “attempted” prevents execution records from becoming efficacy evidence; “composition” connects the operation synthesis and solo-writing comparator; “distributed” motivates handoff and allocation records; and the unsettled-commitment boundary excludes tasks whose commitments were resolved elsewhere. Deleting any of these from the applicable claim would change its mechanism or scope. The title itself states the broader record-versus-effect result without unnecessarily restricting it to a particular actor allocation.

### semantic/underspecified-assertions — PASS

Anchors: `candidate.md:10`, `candidate.md:14`, `candidate.md:16`, `candidate.md:20`.

Potentially broad terms are resolved where they become load-bearing. The trace is instantiated as input, report, status, or disposition records; checker success is operationalized as error-class discrimination against independently adjudicated passages; whole-loop testing requires a named comparator and outcome; and “composition's effects” is separated into artifact, human-understanding, and later-system outcomes. The note openly identifies the missing task-specific completeness criterion rather than presenting an unspecified criterion as settled. A future experiment would still need a concrete blinding and measurement protocol, but that implementation choice does not leave the candidate's present auditability claim with two materially different meanings.

### semantic/unearned-generality — PASS

Anchors: `candidate.md:8`, `candidate.md:10-12`, `candidate.md:18-20`.

The abstract terms used by the central claim are earned by developed distinctions. “Actor” is instantiated by human, agent, and policy; “effects” is decomposed into three outcome classes; and “operations” is instantiated by the three named bundles. The argument remains grounded in substantive-claim composition and does not inflate a prose-specific case into a claim about all workflows or all learning. Its general claim—that an execution trace does not by itself establish effect—rules out treating any of the named outcome classes as proved by acceptance or inspectability alone.

## Blocker statement

No material semantic blocker remains. The line 18 anchoring language is an INFO-level attribution boundary, not a failure of the central claim or its evidentiary route.
