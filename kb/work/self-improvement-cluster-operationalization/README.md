# Operationalizing the self-improving-systems cluster

## Goal

Turn the [self-improving-systems cluster](../../notes/self-improving-systems-README.md) into methodology that guides Commonplace's own changes, while keeping it good research — the maintainer's working premise is that these are the same program, because every ambiguity or contradiction left in the theory surfaces as a failure at application time.

The trigger finding (full-cluster review, 2026-07-21): the cluster currently fails its own operativity test. In its own vocabulary, it has no reliable consumer, channel, or force into actual change decisions — nothing loads it when someone modifies a skill, validator, type spec, or collection contract, and the shipped review system (the repo's most developed evaluation machinery) is never read through the cluster's loop vocabulary. Hygiene defects found in the same review were fixed directly (world-models tagging gap, misattributed profile citation, explanatory-reach link, cumulativity-test exclusion left implicit, slug-length failure).

## Three authority paths

The cluster can reach change-time behavior along three paths, and the cluster's own theory grades them. The workshop treats all three as real design targets, not just the first:

1. **Wired** — instructions, review gates, and `AGENTS.md` routing load the (distilled) theory whenever Commonplace's behavior-determining organization is being changed. The strongest wire; enumeration-like.
2. **User-invoked** — the maintainer tells the agent to consult the cluster for a given change. No engineering needed; the human is the retrieval wire, so it does not scale past the maintainer's own noticing.
3. **Link-mediated discovery** — the agent, navigating tags, links, and descriptions, decides on its own that the change at hand needs the cluster. Best-effort by construction — [retrieval failure is reflection failure](../../notes/retrieval-failure-is-reflection-failure.md) applies to the cluster itself — so this path puts its load on the cluster's findability: descriptions that match change-time queries, links from the artifacts agents actually touch when changing the system.

Paths 2 and 3 already exist in weak form; path 1 does not exist at all. Which mix to build is a design decision this workshop owns, not a foregone conclusion in favor of maximal wiring.

## Sequencing (fixed by the maintainer)

- **Phase 0 — close ambiguities and contradictions.** Work the ledger below. Items may be resolved in the library notes directly, parked explicitly as open questions, or split out; what they may not do is stay silently ambiguous into phase 1.
- **Phase 1 — audit the existing operational artifacts against the theory.** The first distillation step is not writing new guidance but checking whether the theory suggests changes to what already operates: `kb/instructions/` (skills, gates, FIX-SYSTEM, review instructions), and the behavioral-authority artifacts — `src/` code, validators, type specs in `kb/types/`, `COLLECTION.md` contracts, `AGENTS.md`. Per artifact, the theory supplies the questions: what consumes it, through which channel, with what force; which loop function (search, evaluation, retention) it implements; where it automates evaluation, whether its oracle's warranted domain is respected; where it retains commitments, whether their scope is stated and their retrieval wire holds. Substantial; execute only after phase 0.
- **Later phases (order undecided, to be set by phase 1 results):** read the review system through the loop vocabulary (criteria as oracles, review pairs as evaluation instances, freshness baselines as retention bookkeeping); distill a change-time instruction digest into `kb/instructions/`; give the declared Commonplace frame a single citable anchor; instrument subsequent ADRs and significant changes as the ongoing evidence stream the cluster currently lacks.

## Ambiguity ledger (phase 0)

Grows as application surfaces more; shrink it by resolving in the library, not here.

- **`warn` outcome vs. the loop's evaluation criterion** — the loop note requires rejection to be an event distinct from the arrival of the next candidate; where does the review system's `warn` sit — rejection, deferred acceptance, or something the theory lacks a slot for?
- **Canonical frame** — the declared boundary exists only inside [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md); repeated applications will re-derive and silently diverge without a reusable anchor.
- **Operation-depth ontology** — open TODO in [reflective coverage](../../notes/reflective-coverage-is-graded-across-representational-forms.md): ordered list vs. capability profile/partial order.
- **Closure-note TODOs** — tacit-but-stable human expertise as retained methodology; literal boundary closure vs. the human-dependency-only reading ([closure note](../../notes/methodological-and-computational-closure-track-different-changes.md)).
- **Stub note** — [reflection puts a system's own organization inside its action environment](../../notes/reflection-makes-own-organization-part-of-the-action-environment.md) is mostly open questions; decide whether to run the self-ontology investigation or fold it into the coverage note's open questions.
- **Cumulativity's environment-mediated exclusion** — now stated in the [profile note](../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md); verify the stated form survives contact with real cases in phase 1.

### Resolved

- **Three senses of "reach"** (2026-07-21) — `explanatory-reach` and `reach-assessment` registered as rare compounds carrying the main sense; registration paragraph lives in [reach-assessment](../../notes/definitions/reach-assessment.md) (retitled to the hyphenated form). The search sense renamed to **search range**; the one oracle-side leak ("proof reach") renamed to **proof surface**. Deliberate residue: the two route-note titles and the first-principles title keep spaced "reach" (title quotes lag by convention; rename only if a title-level collision ever bites), and frozen fixtures under `kb/work/error-catching/` plus source-ingest link texts were left untouched.

## What closes the workshop

- The phase 1 audit executed, with every suggested change dispositioned: applied, turned into a proposal, or rejected with reasons recorded.
- An explicit decision on the authority-path mix (which of the three paths carries the cluster, and what was built or deliberately not built for each).
- The ledger empty — each item resolved in a library note or explicitly parked there as an open question.
- Durable outputs extracted to the library (instruction digest, reference mapping, ADRs as warranted) and this directory deleted.

## Bookkeeping

Findings and drafts live as files in this directory; phase 1 per-artifact audit results go under `audit/`. Resolutions land in the library notes they concern, with only pointers kept here.

---

Links:

- [Self-improving systems tag README](../../notes/self-improving-systems-README.md) — tests: the cluster whose operational fitness this workshop exercises
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: the form/verification/authority axes the operationalization must settle for the cluster's own content
- [Retrieval failure is reflection failure](../../notes/retrieval-failure-is-reflection-failure.md) — grounds: why authority paths 2 and 3 are best-effort and what strengthening the wire means
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../notes/false-positive-generation-is-filtered-before-retention.md) — draws-on: the automate-search-first rule the audit applies to existing automation
- [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — depends-on: the declared frame and single worked trace all applications currently rest on
- [Where change candidates come from in Commonplace](../../reference/where-change-candidates-come-from-in-commonplace.md) — draws-on: the observed search surface the audit starts from
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rationale: why the change-time digest should carry answers, not derivations
