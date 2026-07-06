# Verification locus: state, history, and what review can bind

Working theory file. This angle came out of the type-as-review-gate work (ADR 038 and the follow-ups that made conformance prompts reference the type spec and made `--all-gates` uniform). It supplies the theoretical spine for questions this workshop already owns: what lineage must record, which dependency edges deserve which invalidation machinery, and why provenance is the one thing that cannot be deferred.

Status: literature sweep done (snapshots + ingests in `kb/sources/`, listed below). Library notes deliberately NOT written yet — claim names need scrutiny rounds first.

## The kernel

Review-time verification is memoryless. A checker arriving after production sees the artifact's **state** — its text plus reachable records — never its **history**. Any state is consistent with many histories, so history-dependent properties (how sources were gathered, what the author consulted, whether judging was blind, which model produced it) are undecidable from the artifact *in principle*, not merely expensive to check. They are verifiable only at production time.

Two bridges convert a history property into something checkable later:

1. **Records (attestation).** A record made at production time turns a history fact into a state fact. This is why provenance exists as a field: W3C PROV, in-toto/SLSA attestations, audit trails, appellation certification for process-defined goods. The verifier checks the record and trusts the recorder.
2. **Re-derivability (reproducibility).** Make the process deterministic and its inputs preserved, and history becomes re-verifiable from state forever, no trust needed — reproducible builds, Nix content-addressed derivations (Thompson's Trusting Trust is the classic motivation: no state inspection reveals a compromised toolchain; deliberately not snapshotted — too far from this KB). The stronger, decay-proof bridge; usually unavailable for LLM production (nondeterministic process, changing world), so records are our default.

Refinement so the dichotomy doesn't overclaim: some history is re-verifiable from the world for a while (snapshot fidelity, while the URL still serves the same bytes). Verifiability **decays**; recording is insurance against decay. State-vs-history is the limit of that spectrum, not a metaphysical binary.

## Corollary 1: contracts partition by verification locus

A contract enforced by later review can bind only state properties. History requirements written into a review-facing contract are dead letters — the reviewer either ignores them or confabulates compliance. In economics terms, process properties are **credence attributes** (Darby & Karni 1973; Dulleck & Kerschbamer 2006): unverifiable by the consumer even after consumption, which is why certification and labeling regimes exist.

Applied to Commonplace types, this yields a three-layer sieve over every line of a type spec:

| layer | verifier | placement |
|---|---|---|
| Structure (sections exist, fields, enums, counts) | deterministic validator | push down into the schema |
| Semantic contract (content qualities judgeable from the artifact + linked neighborhood) | LLM reviewer via the type-conformance gate | stays in the type spec — this is its real job |
| Process (how it was produced) | producer, at production time only | push out to the skill, or reify as a provenance record the artifact must carry |

A type whose semantic layer is empty after the sieve is diagnostic, not a failure: its conformance pair carries no information and costs nothing to keep fresh. Better honestly empty than padded with restated schema rules (the derived-copy failure).

Process-defined types (snapshots are the exemplar) are handled by reification: the type demands the *record* of the process (`source`, `captured`, `capture` mechanism), the skill/tool owns the *act*, and review checks the record plus observable boundaries, trusting the process for what it cannot observe.

## Corollary 2: the two contract halves have different invalidation semantics

- Editing a **state contract** (criteria) invalidates **verdicts** — the artifact stands; re-judge it. This is review freshness (ADR 032/038): the acceptance table is a cache of judgments keyed on `(note_hash, gate_hash, model)`, formally a "verifying trace" in the Build Systems à la Carte sense.
- Editing a **history contract** (process) invalidates **artifacts** — the verdicts stand; the artifacts may be worth regenerating. Re-review is the wrong response: the conformance pair would PASS again while the actual deficiency (content produced by a worse method) stays invisible to the unchanged criteria.

Cache-key design predicts both observed failure modes: a key too coarse invalidates spuriously (process text in the hashed gate → every wording tweak stales a cohort); a key too fine misses dependencies (the pre-ADR-038 bug — type spec invisible to the hash, acceptances falsely fresh).

The load-bearing disanalogy with caching: cache entries are recomputable — invalidate and re-derive. Provenance records are not. A record of history is a journal entry, not a cache entry; no invalidation policy recovers one that was never written. Hence the non-retrofittability rule: **state can be re-examined at any time; history can only be recorded at the time.** Recording is the one feature YAGNI cannot defer.

## The graduated invalidation ladder

Process edits should cost what their retroactive reach actually is — one classification at edit time, not a cohort of trivial-acks:

| level | mechanism | when |
|---|---|---|
| L0 untracked | nothing | wording polish of a skill; the overwhelming default |
| L1 recorded | artifacts carry `produced_by` (skill + version/date) | always-on insurance; the only non-retrofittable level |
| L2 queried | bump skill version; query provenance for artifacts predating it; batch decision (leave / mark outdated / regenerate) | an improvement that genuinely matters retroactively |
| L3 watched | opt-in factored `(note, skill)` pair, skill on the gate side | process fidelity is part of the artifact's warrant (snapshots); reuses the factored-pairs proposal |
| L4 in-spec | the rule goes into the type spec / `## Review`; full conformance blast radius | the "process improvement" actually changed what a good artifact looks like — it was criteria all along |

The L4 test doubles as the honesty check on the whole migration: if exporting a rule to a skill would change what a *good artifact* looks like, it was never process, and moving it silently recreates the bug ADR 038 fixed.

## Generalization: every note is a derivative

A note's derivation inputs include at least: its type spec, the skill that produced it, the user input/conversation, consulted sources, and the producing model. ADR 038 made exactly one of these edges watched (`note ← type spec`, via the conformance pair). The general lineage model this workshop is after can be stated as: **assign every derivation edge a rung on the ladder** — watched (hashed pair), recorded (provenance field / event ledger), or untracked — by the edge's invalidation semantics and retroactive reach, not uniformly.

This gives existing workshop threads a common frame:

- `model-provenance.md` — the model edge is L1/L2 territory (recorded on derivation events, queried on model deprecation), never L3 for canonical notes.
- Open tension 10 (canonical artifacts with derivative update events) — merge-back events are records (L1) on the update event, not a reclassification of the artifact.
- Open tension 11/12 (edge-state infrastructure; ranking links by disruption probability) — the ladder *is* the ranking, with storage weight following the rung: watched edges need relational edge-state, recorded edges need an append-only surface, untracked edges need nothing.
- `general-lineage-refresh-state-design.md` — its input-version model is the L2/L3 machinery generalized.
- The peer workshop [bulk-operations](../bulk-operations/README.md) owns the execution half: L2/L3 responses (regenerate a cohort, re-review a cohort) are staged bulk operations, and its minimal-run-record question is L1 applied to the bulk run itself — a run record is reified history and cannot be reconstructed after the run. Its integrate-stage laundering worry is the credence problem: a worker output's uncertainty status is a history fact that must ride on the merged artifact as a recorded claim or be lost.

## Literature anchors

Snapshots and ingests in `kb/sources/`:

- **Build Systems à la Carte** (Mokhov, Mitchell, Peyton Jones 2018) — rebuilders, verifying vs constructive traces, early cutoff; the formal home of verdict-invalidation. [snapshot](../../sources/build-systems-a-la-carte.md), [ingest](../../sources/build-systems-a-la-carte.ingest.md)
- **W3C PROV-Overview** (Groth & Moreau 2013) — the standards model for reified history (entities, activities, agents). [snapshot](../../sources/prov-overview.md), [ingest](../../sources/prov-overview.ingest.md)
- **in-toto: providing farm-to-table guarantees for bits and bytes** (Torres-Arias et al., USENIX Security 2019) — attestation chains for supply-chain steps; layout = process contract, link metadata = records. [snapshot](../../sources/in-toto-farm-to-table-guarantees.md) (condensed full-paper capture), [ingest](../../sources/in-toto-farm-to-table-guarantees.ingest.md)
- **On Doctors, Mechanics, and Computer Specialists: The Economics of Credence Goods** (Dulleck & Kerschbamer) — the survey carrying the credence-goods framework. Snapshot is the full-text 2001 University of Vienna working-paper precursor (same authors and core model; the published JEL 2006 version is access-blocked): [snapshot](../../sources/dulleck-kerschbamer-doctors-mechanics-computer-specialists.md), [ingest](../../sources/dulleck-kerschbamer-doctors-mechanics-computer-specialists.ingest.md)
- **Free Competition and the Optimal Amount of Fraud** (Darby & Karni 1973, Journal of Law and Economics 16(1), 67–88) — origin of credence qualities; paywalled, deliberately not snapshotted — cite from the literature directly.

## Planned library outputs (not yet written)

1. Core note — candidate claim-title: "Review-time verification sees state, not history" (with reification, re-derivability, decay, and non-retrofittability inside it). Naming hazards: "state" overloaded in software; avoid "intrinsic/extrinsic" (philosophy baggage) and bare "observability" (collides with the verifiability gradient's rewardability).
2. Corollary note — candidate claim-title: "Criteria edits invalidate verdicts; process edits invalidate artifacts". Composes with `link-graph-plus-timestamps-enables-make-like-staleness-detection`.
3. Design proposal in `kb/reference/proposals/` — the type-spec/skill migration: three-layer sieve, reify-as-provenance for process-defined types, `produced_by` convention adopted at L1, L2–L4 deferred as written-down gaps.

Both notes carry `has-external-sources` and cite the anchors above. What is novel is the composition applied to LLM-reviewed knowledge artifacts, not the parts.

## Open questions

- Naming: does "verification locus" survive scrutiny as the axis name? Alternatives: "state/history split", "product vs production contract". Expect rounds.
- Does the ladder's L1 `produced_by` belong in frontmatter (per-artifact) or the event ledger (per-derivation-event)? `model-provenance.md` argues events for canonical notes; one-shot derivatives may differ.
- Is decay-of-verifiability worth its own treatment (re-fetchable snapshots, moving upstream repos), or a paragraph in the core note?
- Where does the reviewer's *linked neighborhood* end for "state"? The conformance gate already answers this operationally (pre-resolved links only); the note should state it as a boundary, not rediscover it.

---

Relevant Notes:

- [ADR 038](../../reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — depends-on: the watched note←type edge this theory generalizes
- [verifiability gradient](../../notes/verifiability-gradient.md) — contrasts: orthogonal axis — cost/mechanism of checking vs what can be checked at all, and when
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the recomputable special case; provenance records are the non-recomputable complement
- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — grounds: the build-product model the invalidation corollary formalizes
- [model provenance](./model-provenance.md) — see-also: the model edge as an instance of the ladder
- [current practices and theory](./current-practices-and-theory.md) — see-also: the descriptive inventory this frame reorganizes
