# Invariants under composition

## Commission and question

Posed by the operator on 2026-11-04 during the prompt-semantics rewrite. Initially parked; resumed the same day for at least five rounds of fresh-context brainstorming, independent critique, revision and cleanup. Every new element must distinguish a case, expose a missing obligation or change a proposed check.

How can we build larger systems from smaller components while preserving the properties the larger system relies on? The starting insight is that interactions need not be strong to break an important invariant. Locating a component to change and establishing that the change preserves required properties are separate achievements.

## Current result

Five rounds are complete, using ten fresh-context agents. The working account connects a named requirement to concrete probes: interleave checking and use, challenge a no-mutation premise, or compare public observations across executions. After a local edit, re-establish affected premises before reusing an argument. Passing an isolated component test does not discharge these obligations.

The evidence consists of constructed finite examples and an explicitly bounded reading of Commonplace's freshness architecture. It establishes neither a runtime defect nor a general method for discovering every dependency. The literature informs the examples; no theorem has been adopted for prompt behavior.

- [Working account](./working-account.md): the candidate argument, probe-selection table and worked cases.
- [Source assessments](./source-assessments.md): reading scope, proposed transfers, limits and parked leads.
- [Round record](./rounds.md): what each brainstorm added, how critique changed it, and what cleanup removed.

The numerical example shows that convergence can coexist with crossing a required bound. Its calculation stays in the round record. Small-gain machinery, chaos and catastrophe theory remain parked until a concrete KB case needs them.

## Connection to the preceding workshop

- [Near-decomposability may make local inspection affordable](../../theory/near-decomposability-may-make-local-inspection-affordable.md): motivates separating weak interaction from preservation of requirements.
- [Clear instructions can compose into an unsettled contract](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md): distinguishes an unsettled requirement from failure to preserve an agreed one.
- [Addressable theory](../../theory/definitions/addressable-theory.md): concerns locating and revising parts; preservation needs further evidence.

## Next test and closure

The next proposed test adds retained state: two calls over two public documents share a cache whose population may depend on the first call's confidential bit. Specify the cache and public observations first, then enumerate finite histories and compare with a public-only cache control. Its role is to test whether the account catches an indirect dependence after the direct output-order leak is removed. This test has not been run.

The commission covers bounded investigation, not runtime implementation or library promotion. Before promotion, test whether the account changes a maintainer's decision in a further KB case, and ground any retained source claims through the source workflow. Close by extracting supported conclusions and necessary source records, or recording why no useful transfer survives, then removing this workshop and its index entry.
