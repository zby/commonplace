---
description: "A failure retained as a lesson helps tasks that retrieve it; retained as a maintained check it improves selection for later candidates in its domain and amortizes validation"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Oracle accumulation improves selection for later candidates in its maintained domain

A system can retain two different things from a failure. The **lesson** — what went wrong and why — improves future proposals. The **check** — a test, validator, type constraint, or invariant that would have caught the failure — improves the evaluation of future proposals. Where recurrent failures can be partially formalized, a maintained check can prevent recurrence across later candidates in its domain. Reuse can also amortize validation work, subject to the corpus costs below. The system is not only learning a better policy; it is learning a better selection environment for later policies within the maintained domain of its checks.

## The two channels ride different wires

The difference is not subtle bookkeeping: the channels have different delivery guarantees. A retained lesson helps exactly the tasks that retrieve it, and [a miss first breaks the affected reflective path](./a-retrieval-miss-is-a-local-reflective-path-failure.md) — the standing weakness of the artifact-retention wire is that delivery remains best-effort. Once wired into an enforcement channel — a validation pass, a CI run, a schema gate — a retained check runs against every candidate in its scope, whether or not anything remembered to look. For that fragment of retained knowledge, accumulation restores the exhaustive consumption that the retrieval wire lost.

The traced [tag-readme episode](./evidence/tag-readme-trace-observed-causal-connection.md) shows this event in miniature. A prose `rg` recipe missed a tagged member. The later `covered_by` mark and validator made the relevant child-tag partition exhaustive and caught the miss, which then prompted a correction to the prose. The observed event concerns `covered_by`; the separate `complete` promise was not observed failing. Both representational precision and the consumption wire changed for the enforced partition rule.

## Accumulation moves the warranted-autonomy boundary

[Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md): a loop may evaluate on its own exactly where an oracle discriminates well enough for the stakes. That note treats the boundary as given for each decision. Accumulation can move it, but regression coverage and oracle-domain expansion are different achievements. A failure-derived check immediately protects against the observed failure class. It expands warranted autonomy only when held-out incidents, fault injection, adversarial cases, or outcome calibration demonstrate relevant discrimination beyond the originating case, and only while monitoring confirms that the discrimination persists.

This is what “migration inward is earned rather than waited for” means operationally: the warrant is a residue of operation rather than a design-time allocation. The same reuse can preserve [the readable-artifact loop's bounded validation radius](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), because a useful check is authored once and applied to later changes in its neighborhood.

## Relation to oracle hardening

[Oracle strength spectrum](./oracle-strength-spectrum.md) supplies the per-component operation: manufacture a check with above-chance discrimination, amplify an already discriminating signal through decorrelated repetition, and monitor it for proxy rot. [Spec mining is the operational mechanism](./spec-mining-as-codification.md) that converts recurrent failures into candidate checks; measured discrimination is a separate admission requirement. Repeating the operation and retaining its outputs strengthens the selection side independently of the proposal side. [An agent-first engineering effort reports one practitioner instance](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md): in the Codex team's reported codebase, recurring manual AI-slop cleanup was replaced by repository-encoded standards and automated cleanup, alongside structural tests and custom linters that enforce architecture and other rules. The report also says engineers responded to failures by adding tools, linters, or structural tests. It does not trace each check to a specific recurring failure or test later discrimination, so it illustrates accumulation without establishing the note's broader selection-environment claim.

## Scope

- The channel exists only where failures can be partially formalized. At the soft end of the spectrum — judgment calls, taste, research selection — failures yield lessons but not checks, so this compounding is unavailable; that boundary belongs to the spectrum note, not this one.
- An accumulated oracle is an enforced artifact, and enforcement cuts both ways: a wrong check on the exhaustive wire is exhaustively wrong. That is [unearned authority](./a-consumption-channel-delivers-force-without-the-history-that.md) — force delivered without the history that earned it — in its strongest position. The spectrum's monitor step and [relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) are therefore the corpus's brake.
- Accumulation is not free retention. Checks can overlap, become correlated, invite gaming, and impose execution, triage, and maintenance costs; a drifted failure boundary is a false floor. The claim concerns reusable validation work per improvement, not declining total system cost. Whether a corpus improves discrimination net of those costs is an empirical question for each deployment.

## Open Questions

- Does selection-environment retention dominate policy retention in mature systems — is there a crossover point after which most of a system's learning resides in its oracles?
- Is there a usable metric for selection-environment strength — such as coverage of past failure classes or discrimination on injected faults — so that accumulation could be tracked rather than observed anecdotally?
