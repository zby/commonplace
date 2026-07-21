# Operationalizing the self-improving-systems cluster

## Goal

Turn the [self-improving-systems cluster](../../notes/self-improving-systems-README.md) into methodology that guides Commonplace's own changes, while keeping it good research — the maintainer's working premise is that these are the same program, because every ambiguity or contradiction left in the theory surfaces as a failure at application time.

The trigger finding (full-cluster review, 2026-07-21): the cluster currently fails its own operativity test. In its own vocabulary, it has no reliable consumer, channel, or force into actual change decisions — nothing loads it when someone modifies a skill, validator, type spec, or collection contract, and the shipped review system (the repo's most developed evaluation machinery) is never read through the cluster's loop vocabulary. Hygiene defects found in the same review were fixed directly (world-models tagging gap, misattributed profile citation, explanatory-reach link, cumulativity-test exclusion left implicit, slug-length failure).

## Three authority paths

The cluster can reach change-time behavior along three paths, and the cluster's own theory grades them. The workshop treats all three as real design targets, not just the first:

1. **Wired** — instructions, review gates, and `AGENTS.md` routing load the (distilled) theory whenever Commonplace's behavior-determining organization is being changed. The strongest wire; enumeration-like.
2. **User-invoked** — the maintainer tells the agent to consult the cluster for a given change. No engineering needed; the human is the retrieval wire, so it does not scale past the maintainer's own noticing.
3. **Link-mediated discovery** — the agent, navigating tags, links, and descriptions, decides on its own that the change at hand needs the cluster. Best-effort by construction — [retrieval failure is reflection failure](../../notes/retrieval-failure-is-reflection-failure.md) applies to the cluster itself — so this path puts its load on the cluster's findability: descriptions that match change-time queries, links from the artifacts agents actually touch when changing the system.

Paths 2 and 3 already exist in weak form; path 1 does not exist at all. Which mix to build is a design decision this workshop owns, not a foregone conclusion in favor of maximal wiring — and the framework below reframes the choice: 2 and 3 are the fallback route of a two-layer system, not merely weaker wiring.

## Framework: this is a two-layer build

The library already holds the theory of what this workshop is doing. [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) supplies the architecture, and the operationalization should be built as an instance of it:

- The change-time digest planned below is a **derived fast path** — action-shaped, cheaper, and strictly narrower than the cluster.
- The cluster is the **generator layer and stays live**: a change situation the digest does not cover drops back to the theory. Authority paths 2 and 3 are that fallback route.
- **Recurrence is the promotion signal**: fallback reasoning that repeats is what earns a place in the digest. The digest's content is therefore not designed upfront — the phase-1 audit and the instrumented future changes are the first samples of fallback traffic, and they decide what gets promoted.
- The digest must declare its **coverage**, so an out-of-coverage change routes to the cluster instead of being mis-served by a checklist that silently does not apply.

Wiring and maintenance are settled vocabulary, not new design: the digest is judgment-dependent derived prose, so it takes the **managed-staleness** regime, and the [link grammar](../../reference/link-vocabulary.md#lineage-semantics) already authorizes exactly this edge — `operationalized-from` for the `kb/notes/` methodology → `kb/instructions/` procedure pairing, recorded at the source in an `Operationalized into:` footer, a source change flagging a judgmental recheck. That is also the phase-0 discipline going forward: theory revisions create no derived-artifact debt today (no derived layer exists yet), but once the digest exists, every later cluster revision owes it the structure note's **correspondence check**. The eventual mechanical support is already named too: [where change candidates come from](../../reference/where-change-candidates-come-from-in-commonplace.md) flags theory-to-implementation lineage as what a wider freshness substrate would need to cover.

## External-theory delegation (2026-07-21, decision pending)

The maintainer's direction — delegate to established theories wherever they suffice, keep only the Commonplace-specific kernel local — is assessed against the cluster's current state in [external-delegation-assessment](./external-delegation-assessment.md), which dispositions an external (ChatGPT) delegation proposal item by item. Headline: the stance is already the recorded conservative-extension stance; the open decisions are the goal revision extending it to the methodology layer (recommended), PDSA/MAPE-K as digest-phase hosts (adopt the no-duplication commitment now, bind the host only after a worked case), and an assurance-case/GSN inheritance candidate for warrant recording.

## Sequencing (fixed by the maintainer)

- **Phase 0 — close ambiguities and contradictions.** Work the ledger below. Items may be resolved in the library notes directly, parked explicitly as open questions, or split out; what they may not do is stay silently ambiguous into phase 1.
- **Phase 1 — audit the existing operational artifacts against the theory.** The first distillation step is not writing new guidance but checking whether the theory suggests changes to what already operates: `kb/instructions/` (skills, gates, FIX-SYSTEM, review instructions), and the behavioral-authority artifacts — `src/` code, validators, type specs in `kb/types/`, `COLLECTION.md` contracts, `AGENTS.md`. Per artifact, the theory supplies the questions: what consumes it, through which channel, with what force; which loop function (search, evaluation, retention) it implements; where it automates evaluation, whether its oracle's warranted domain is respected; where it retains commitments, whether their scope is stated and their retrieval wire holds. Substantial; execute only after phase 0.
- **Later phases (order undecided, to be set by phase 1 results):** read the review system through the loop vocabulary (criteria as oracles, review pairs as evaluation instances, freshness baselines as retention bookkeeping); write up the two-layer promotion mechanism as the cluster's second worked case — it passes the loop's evaluation criterion cleanly (pre-promotion verification is a gate distinct from candidate generation, unlike `warn`) and the digest will be its live instance; distill a change-time instruction digest into `kb/instructions/` as the two-layer fast path described under Framework, carrying `operationalized-from` lineage and a declared coverage region; give the declared Commonplace frame a single citable anchor; instrument subsequent ADRs and significant changes as the ongoing evidence stream the cluster currently lacks.
- **Parasuraman inheritance (blocked on maintainer's machine).** Per the [external-theory evaluation](./external-theory-evaluation.md) (finding 7) and the maintainer's decision (2026-07-21): inherit the per-function-grading *form* of the actor-allocation profile from Parasuraman, Sheridan & Wickens (2000, IEEE SMC-A 30(3), 286–297) — not base the theory on it. Step 1, **from a machine with open egress** (this session's policy 403s all web hosts; a Sonnet ingestion run confirmed and documented this): snapshot + ingest the paper into `kb/sources/` via `cp-skill-snapshot-web`/`cp-skill-ingest`. Candidate URLs: `https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf`, `https://ntrs.nasa.gov/api/citations/20205003378/downloads/NASA-TM-20205003378.pdf` (verify it is this paper on open), `https://www.academia.edu/36874333/A_Model_for_Types_and_Levels_of_Human_Interaction_with_Automation`. Step 2, any session after the source exists: add a Provenance entry to the [profile note](../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md)'s actor-allocation section — per-function grading inherited, with three flagged departures: no within-function level ladder (per the commensurability argument in the closure/measurement notes), functions are improvement-pathway functions (search, evaluation, retention) rather than task-performance stages (acquisition, analysis, decision selection, action implementation), and allocation does not establish warrant (their automation-reliability discussion supports this; connect to [warranted autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md)). Optional: one paragraph mapping their four stages onto the loop functions. The self-aware-computing coverage comparison (finding 7's other half) stays separate and undecided.

## Ambiguity ledger (phase 0)

Grows as application surfaces more; shrink it by resolving in the library, not here.

- **`warn` outcome vs. the loop's evaluation criterion** — analyzed in [warn-outcome-vs-loop-evaluation](./warn-outcome-vs-loop-evaluation.md): by the loop note's own test, gates as currently consumed are not evaluation; two candidate resolutions (reclassify gates as search vs. extend the theory with retain-with-obligation), decided by an empirical check on the fix reports that must run on a machine with the local review data.
- **Canonical frame** — the declared boundary exists only inside [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md); repeated applications will re-derive and silently diverge without a reusable anchor. The theoretical half is settled — the definition's Provenance now states the predicate is frame-indexed (bearer is a bounded system, not a substrate; [external-theory evaluation](./external-theory-evaluation.md), finding 3) — but the reusable citable anchor for Commonplace's own declared frame remains to build.
- **Operation-depth ontology** — open TODO in [reflective coverage](../../notes/reflective-coverage-is-graded-across-representational-forms.md): ordered list vs. capability profile/partial order.
- **Closure-note TODOs** — tacit-but-stable human expertise as retained methodology; literal boundary closure vs. the human-dependency-only reading ([closure note](../../notes/methodological-and-computational-closure-track-different-changes.md)).
- **Stub note** — [reflection puts a system's own organization inside its action environment](../../notes/reflection-makes-own-organization-part-of-the-action-environment.md) is mostly open questions; decide whether to run the self-ontology investigation or fold it into the coverage note's open questions.
- **Cumulativity's environment-mediated exclusion** — now stated in the [profile note](../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md); verify the stated form survives contact with real cases in phase 1.
- **"Promotion" vocabulary watch** — three related uses circulate: case-promotion into a fast path ([two-layer note](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md)), artifact promotion from workshop to library ([COLLECTION.md](../COLLECTION.md)), and authority promotion from advice toward enforcement (constraining notes). Likely one sense family — "move into a more binding or durable layer" — rather than a collision, but assess against the [write-time collision rule](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) during the audit.

### Resolved

- **Membership tense** (2026-07-21) — resolved in the [definition](../../notes/definitions/self-improving-system.md): membership is read over a declared assessment horizon, mirroring operativity; the dispositional attribution (a standing pathway, exercised or not) stays available but must be marked as a different claim. A matching misuse case guards the dormant-pathway reading. From [external-theory evaluation](./external-theory-evaluation.md), finding 2.
- **"Closure" collision with the autopoietic sense** (2026-07-21) — contrast paragraph added to the [closure note](../../notes/methodological-and-computational-closure-track-different-changes.md) pointing at the reflective-system exclusions, per the write-time collision rule. From [external-theory evaluation](./external-theory-evaluation.md), finding 5.

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
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the generator/fast-path architecture the operationalization instantiates
- [Link vocabulary — lineage semantics](../../reference/link-vocabulary.md) — depends-on: `operationalized-from` and its judgmental-recheck maintenance regime, the authorized edge for the digest
