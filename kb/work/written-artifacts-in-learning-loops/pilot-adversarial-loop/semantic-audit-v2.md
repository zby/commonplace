# Direct semantic audit v2

Target: `candidate.md`

## Scope and method

This audit applies every gate in `kb/instructions/review-gates/semantic/` directly to the target. It does not register or update review-store state. Candidate-relative links were resolved as though `candidate.md` lived in `kb/notes/`.

Grounding inspection stopped at the candidate's direct evidence. It covered the three linked practitioner snapshots; the linked notes on reasoning production versus evaluation, LLM goal relaxation, human-analogy transfer, inspectability, error correction, and vibe-noting; and the linked practitioner snapshots on substantive AI writing and wordless thought. No transitive link was followed. No incumbent, earlier candidate, workshop history, or prior audit, friction, or semantic report was consulted.

## Summary

| Gate | Result |
|---|---|
| `semantic/completeness-boundary-cases` | PASS |
| `semantic/conceptual-role-conflation` | PASS |
| `semantic/explanatory-reach` | PASS |
| `semantic/explication-quality` | INFO |
| `semantic/grounding-alignment` | PASS |
| `semantic/internal-consistency` | INFO |
| `semantic/load-bearing-qualifiers` | PASS |
| `semantic/underspecified-assertions` | WARN |
| `semantic/unearned-generality` | PASS |

One material blocker remains. In the concrete loop, the bare disposition `reject` does not say whether the acceptor rejects the challenge or rejects the claim. Those are opposite decisions, and the preceding taxonomy explicitly distinguishes them. A trace containing only `reject` therefore cannot make the disposition auditable in the sense the note claims.

## Gate results

### PASS — `semantic/completeness-boundary-cases`

Anchors: `candidate.md:10`, `candidate.md:12`, `candidate.md:14`, `candidate.md:20`.

The note explicitly calls the three operations a “compact synthesis” and “not a canonical or complete taxonomy of composition” (`candidate.md:12`). Its coverage claim is correspondingly narrow: unsettled substantive commitments before acceptance, not all writing activity.

Boundary probes map without forcing an extra category:

- A single unsettled factual claim maps to commitment, challenge, and disposition.
- A true conclusion reached through an invalid route maps to route exposure and route-directed challenge (`candidate.md:16`).
- An unsupported challenge maps to rejection with cited support (`candidate.md:12`).
- A challenge that cannot yet be resolved maps to retained explicit uncertainty.
- Settled rendering, transcription, and stylistic editing are expressly outside the boundary (`candidate.md:10`).

Reader simulation, fresh criticism, stabilization, changed understanding, actor selection, and measured outcomes are also explicitly placed outside the operation taxonomy. No tested case clearly falls outside the coverage the note actually claims.

### PASS — `semantic/conceptual-role-conflation`

Anchors: `candidate.md:12`, `candidate.md:14`, `candidate.md:18`, `candidate.md:20`.

The load-bearing role distinctions are explicit:

- operations are separated from possible methods and possible outcomes (`candidate.md:12`);
- checker and acceptor are roles, while human, agent, and policy are possible role occupants (`candidate.md:14`);
- a recorded attempt is separated from successful performance and justified disposition (`candidate.md:10`, `candidate.md:14`); and
- acceptance authority is separated from artifact, human-understanding, and later-system outcomes (`candidate.md:18`, `candidate.md:20`).

The practitioner sources are described as motivation for the current synthesis, not as prior authors of this taxonomy or as validation of its relocation. No passage permits two materially different assignments among term, source account, current synthesis, role, actor, method, and outcome.

### PASS — `semantic/explanatory-reach`

Anchors: title at `candidate.md:8`; mechanism at `candidate.md:10` and `candidate.md:14`; performance boundary at `candidate.md:16`.

The mechanism is load-bearing: defined stage inputs plus preserved input/report/disposition traces expose which operation and handoff was attempted. The same records contain no independent truth condition for whether an objection identified a real fault or whether a disposition was justified, so inspectability does not entail performance.

The premise-variation test changes the conclusion in the expected places. Remove the preserved, stage-linked trace and the auditability claim fails. Vary checker quality and auditability can remain while the effect claim changes, which is precisely the distinction the note explains. The claim is also falsifiable at its positive edge: a trace that lacks the asserted input, stage linkage, report, or disposition would not make the attempted loop inspectable. The qualifications identify boundaries rather than insulating an otherwise unsupported effect claim.

### INFO — `semantic/explication-quality`

Anchor: `candidate.md:3`.

This gate declares `requires_type: kb/types/definition.md`; the candidate declares `type: kb/types/note.md`. The Carnap explication test is therefore not applicable. This INFO is an applicability result, not a defect in the candidate's local explanations of its three operations.

### PASS — `semantic/grounding-alignment`

Anchors: `candidate.md:12`, `candidate.md:16`, `candidate.md:18`, and the direct grounding links at `candidate.md:32-35`.

The direct evidence supports the limited routes the candidate attributes to it:

- The Graham, Karlsson, and Karnofsky snapshots report committing ideas to definite form, exposing premises and routes to criticism or counterexamples, investigating weaknesses, and revising, switching, rejecting, or retaining a view. The candidate accurately labels its three bundles as a compact synthesis of reported practice, not a canonical taxonomy or controlled validation.
- The reasoning-production note supports testing whether a critic evaluates the presented route rather than reconstructing a sound route to the same conclusion. The error-correction note supports discrimination rather than aggregate agreement and the need to account for correlated errors when checks are combined.
- The substantive-AI-writing snapshot supports the narrower attribution that reviewing already generated prose can invite passive assent. The goal-relaxation mechanism is explicitly retained as conjectural. The wordless-thought snapshot directly supports the counterboundary that human writing can stabilize credible nonsense and false precision.
- The actor-allocation, inspectability, and vibe-noting links support, respectively, reopening role allocation, treating readable traces as inspectable rather than self-validating, and separating persistence from activation and verification.

The candidate does not silently upgrade these sources into performance evidence. It expressly says that they provide neither calibrated critics nor a before-and-after comparison and that no supplied source compares the distributed loop with solo composition or naive delegation (`candidate.md:16`, `candidate.md:20`). No scope overreach or invalid cited inference remains under the inspected direct-evidence boundary.

### INFO — `semantic/internal-consistency`

Anchors: `candidate.md:12` and `candidate.md:14`.

The central claims remain consistent across the note: traces establish inspectability but not quality; roles do not determine actors; authorship and approval are not performance tests; and acceptance is not an artifact, understanding, or later-system outcome.

There is, however, likely vocabulary drift in the disposition list. The taxonomy distinguishes “reject the challenge with cited support” from “reject the claim” (`candidate.md:12`), while the concrete loop compresses both to bare `reject` (`candidate.md:14`). This is not an additional contradiction beyond the WARN below, but it is an internal sign that the concrete loop no longer preserves the taxonomy's distinction.

### PASS — `semantic/load-bearing-qualifiers`

Anchors: title at `candidate.md:8`; scope at `candidate.md:10`; concrete loop at `candidate.md:14`; outcome scope at `candidate.md:20`.

The central qualifiers do work in the reasoning:

- `recorded` supplies the trace on which auditability depends;
- `attempted` prevents the trace from being treated as proof of successful checking or effect;
- unsettled commitments and pre-acceptance placement distinguish discovery and adjudication from settled rendering, transcription, and style work; and
- the distributed-workflow scope is used by the allocation, distinct-role, and handoff claims.

The later `For KB-writing evaluation` clause scopes the three named outcome tests as an application rather than narrowing the title-level auditability claim. Deleting the central qualifiers either breaks the trace mechanism or erases an explicit counterexample boundary.

### WARN — `semantic/underspecified-assertions`

Anchor: `candidate.md:14`.

Smallest useful passage:

> “investigate, revise, narrow, switch, reject, or retain an unresolved marker”

The object of `reject` is unresolved. Two reasonable readings remain:

1. reject the challenge as unsupported and retain the claim; or
2. reject the claim because the challenge succeeds.

The nearby taxonomy confirms that these are not synonymous readings: it lists “reject the challenge with cited support” and “reject the claim” as separate dispositions (`candidate.md:12`). Choosing between them changes the accepted artifact, the evidence needed to justify the disposition, and whether a later evaluator should score the acceptor as upholding or overturning the challenge. Because the note's central mechanism depends on an inspectable disposition, this ambiguity is material rather than cosmetic.

Other apparently broad phrases are resolved nearby: the task-specific trace is instantiated as the exact input, premise-linked report, and per-challenge disposition; approval is limited to admission authority; and each named outcome receives an operational consequence. The benchmark's exact success criteria and control construction remain intentionally pending rather than being presented as established performance (`candidate.md:10`, `candidate.md:16`).

### PASS — `semantic/unearned-generality`

Anchors: title at `candidate.md:8`; operation definitions at `candidate.md:12`; role allocation at `candidate.md:14`; KB-specific outcome application at `candidate.md:20`.

The title stays at the level argued by the body: composition checks recorded around claims, premises, inferential routes, challenges, and dispositions. The functional term `operation` is earned by a concrete input/output account for each stage and by its synthesis across multiple reported writing practices. `Actor` is needed to range over the explicitly separated human, agent, and policy implementations without claiming that they perform equally. `Artifact outcome` and `later-system outcome` are locally defined and expressly scoped to KB-writing evaluation rather than projected as a universal taxonomy. Downgrading these terms would remove cases or distinctions the reasoning actually uses, not merely make the same single example more concrete.

## Material-blocker determination

**Yes: one material blocker remains.** The concrete loop must make the target of `reject` explicit so its disposition trace distinguishes retaining the claim after rejecting a challenge from rejecting the claim after upholding a challenge. No other material semantic blocker was found under the full gate catalogue and the restricted direct-evidence boundary.
