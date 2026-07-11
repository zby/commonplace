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

- Editing a **state contract** (criteria) invalidates **assay evidence** — the artifact stands; rerun the criterion. For a closed-ended gate that means a verdict; for open-ended critique it means a report. This is review freshness (ADR 032/038 plus the schema-v5 result-kind amendment): acceptance caches completed evidence keyed on `(note_hash, criterion_hash, model)`, formally a "verifying trace" in the Build Systems à la Carte sense.
- Editing a **history contract** (process) invalidates **artifacts** — existing assay results may stand, but the artifacts may be worth regenerating. Re-review is the wrong response when the changed process is not itself observable in the artifact: the conformance pair can PASS again while the actual deficiency (content produced by a worse method) stays invisible to unchanged criteria.

Cache-key design predicts both observed failure modes: a key too coarse invalidates spuriously (process text in the hashed gate → every wording tweak stales a cohort); a key too fine misses dependencies (the pre-ADR-038 bug — type spec invisible to the hash, acceptances falsely fresh).

The load-bearing disanalogy with caching: cache entries are recomputable — invalidate and re-derive. Provenance records are not. A record of history is a journal entry, not a cache entry; no invalidation policy recovers one that was never written. Hence the non-retrofittability rule: **state can be re-examined at any time; history can only be recorded at the time.** Recording is the one feature YAGNI cannot defer.

## Evidence radius and carried witnesses

The kernel says review sees state; this section defines what "state" a reviewer can actually afford. The reviewer never searches — it dereferences: the conformance harness already enforces this mechanically (pre-resolved link table, "do not search for alternate targets"). So a contract criterion is **review-decidable** when:

1. its evidence set is *enumerated by the artifact itself* — the note names its witnesses via links, quotes, or provenance fields; and
2. the gate declares a bounded *evidence radius*: radius 0 = the note text alone; radius 1 = the note plus specifically cited targets.

The formal anchor is the NP-verifier asymmetry: generation is search, review is checking-with-a-witness — cheap only if the artifact carries its own certificate. A note that cites its sources has reified its consultation history into state; "faithful to its *cited* sources" is a bounded radius-1 check whose cost the note author controls. A note that doesn't cite makes the check impossible in principle: "faithful to everything the author read" is history, enforceable only by the skill at production time.

This adds a third test to the type-spec sieve: every semantic criterion gets an explicit radius. Radius-ω criteria (they quantify over the generation context) have two exits — **witness-ify** (rewrite as radius ≤ 1 plus a new state requirement: quote anchors, `source_snapshot:`, citation lists) or **move to the skill**. Example: ingest-report's "base extractable value on connect discovery" is radius-ω by design (the connect report is ephemeral and must not be cited) → skill. "Limitations names what this source omits" is radius-1 through the `source_snapshot` pointer.

### The carried-witness family

Several existing KB mechanisms are the same move — reify something into the artifact's state to lower the radius of a check or reasoning step:

| carried witness | reifies | radius reduced |
|---|---|---|
| citation / source list | the enumeration of the evidence set | ω → 1 (check becomes bounded) |
| quote anchor (ADR 023) | the evidence excerpt | 1 → 0 for the quoted claim |
| title-as-claim link text | the target's thesis | 1 → 0 for graph reasoning (traversal-as-reasoning *is* radius reduction) |
| `description:` frontmatter | the relevance decision | 1 → 0 for retrieval routing |
| provenance field (`source`, `captured`, `produced_by`) | a history fact | undecidable → trusted record |

The family splits into two validity regimes:

- **Checkable witnesses** — ground truth still dereferenceable (link text vs target title, quote anchor vs repo file, description vs body). These are derived copies of recomputable truth: *checked or absent*.
- **Credence witnesses** — ground truth gone or external (provenance fields, quotes from a decayed source). Unrecomputable by construction; the record is the ground truth now, and validity rests on trusting the recorder.

A witness's regime can change over time: a quote anchor into an external repo is checkable until the source moves, then silently becomes credence — the decay spectrum with a concrete mechanism attached.

### Gaps this exposes (write down, don't build)

- **Radius-1 assay results have unhashed inputs.** Acceptance pins `(note, criterion)`; when a semantic gate judged the note against its link targets, a later edit to a target stales nothing. Currently absorbed as fuzz (strictness follows behavioral authority); the principled escalation is a factored `(note, cited-target)` pair per load-bearing evidence edge.
- **Link text is a checkable witness that nothing checks.** The validator verifies link *health* (targets resolve) but never compares link display text to the target's current title. When a claim-title is revised, every inline restatement across the KB stays frozen at the old claim, and traversal-as-reasoning degrades silently — agents trust the carried witness at radius 0. Both sides are in the repo; the check is a cheap join. Candidate validator feature; also the cleanest concrete example of one surface (a markdown link) carrying a checkable witness in its text and a health-checked pointer in its path, with only the pointer verified today.

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

## Philosophy-of-science anchors

The KB already borrows from philosophy of science once (Carnap's explication, in the definition type — see the [philosophy-borrowing](../philosophy-borrowing/README.md) workshop); these would join that habit. Selected for load-bearing fit, not survey completeness:

- **Context of discovery vs context of justification** (Reichenbach 1938, *Experience and Prediction*) — the kernel's direct ancestor: how a claim was produced is assessed separately from whether the presented evidence supports it. The post-positivist critique (production circumstances *do* bear on warrant) and science's answer — the methods section, which drags relevant history into the reviewable record — is the witness-ify move, institutionalized. Review-binds-state is justification; the skill owns discovery.
- **Virtual witnessing** (Shapin & Schaffer 1985, *Leviathan and the Air-Pump*) — Boyle's literary technology: detailed experimental narrative and apparatus engravings turn distant readers into "virtual witnesses" because re-running the experiment is unaffordable. This is the carried-witness family's lineage, vocabulary included — quote anchors are engravings of the air-pump. Candidate alternative name for the mechanism: *virtual witness*.
- **The replication crisis and pre-registration** — both failure modes at institutional scale: peer review checks state (the paper) while validity depended on history (p-hacking, the garden of forking paths — Gelman & Loken; fabrication caught by data forensics, never by referees). Pre-registration is L1 recording with a hard timestamp: it converts "we didn't hypothesize after the results" from a credence claim into a checkable witness (registered protocol vs published analysis, a cheap diff). Registered reports move review to production time — the "only the skill can enforce it" exit, made institutional.
- **Verificationism / operationalism — the cautionary borrow.** "A type spec may state only what a reviewer can check from the artifact" is the Vienna Circle's verification principle scoped to contracts; the criterion-radius sieve is Bridgman's operationalism applied per-criterion. Borrow with the failure history attached: strict verificationism collapsed (excluded the meaningful, self-undermined). Our version survives because it is bounded — radius-ω properties are not *meaningless*, they are *not review-enforceable*, and route through records or trusted process instead. That softening is what verificationism never allowed itself.
- **Testimony** (for the credence regime) — trusting a provenance field is trusting testimony: calibrate trust in the recorder, not the claim; expect chain degradation (testimony about testimony). Underdetermination (Duhem–Quine) rhymes with "any state is consistent with many histories" but points the other way (theory underdetermined by data); cite cautiously if at all.

## Planned library outputs (not yet written)

Three artifacts to extract when this angle closes: two theory notes, then a design proposal that cites them instead of arguing the theory inline. Both notes carry `has-external-sources`. The honest novelty claim for both: the parts are all known — what is new is the composition, applied to knowledge artifacts whose semantic layer is reviewed by LLM judges.

**Core note — DRAFTED as a seedling:** [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md). Title settled in a naming round: "review-time verification sees state, not history" fell to the hidden-dichotomy hazard (reads as "history doesn't matter"); "unrecorded history is unverifiable" fell as tautological-or-false (forensics leakage); the temporal-asymmetry form survived. The seedling is deliberately short — claim, two bridges, three boundaries (leakage, decay, bounded reviewer), non-retrofittability plus the contracts corollary, one-line Reichenbach anchor. Still outside it, pending scope decisions: the review-decidable definition with bounded evidence radius, the carried-witness family with its checkable/credence regimes, Shapin's virtual witnessing, and the credence-goods anchor — grow the seedling or split (see open questions).

**Corollary note — DRAFTED as a seedling:** [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md). Pure-claim note as planned: the two propagation semantics, the misleading-not-wasteful point, the cache-key framing with both failure modes, the replication-crisis witness, and a closing line handing the non-recomputable half to the core note. The graduated ladder stayed out — design guidance, reserved for the proposal.

**Design proposal** (in `kb/reference/proposals/`): the type-spec/skill contract migration. Contents: the three-layer sieve (schema / semantic contract / process) with the criterion-radius test as its third question; witness-ify-or-move-to-skill as the two exits for radius-ω criteria; reify-as-provenance for process-defined types; the `produced_by` convention adopted immediately (L1 is the only non-retrofittable rung); and L2–L4 written down as deferred escalation paths, per YAGNI.

## Open questions

- Naming: does "verification locus" survive scrutiny as the axis name? Alternatives: "state/history split", "product vs production contract". Expect rounds.
- Naming the decidability feature: "review-decidable" (leans on who/when), "witness-carrying" / "self-witnessing" (sharpest mechanism, jargon risk), "virtual witness" (Shapin's term, historically exact, borrowed prestige), "evidence-closed", "locally checkable" (collides with collection-local). "Bounded evidence radius" as the underlying measure regardless.
- Do the phil-sci borrows (Reichenbach, virtual witnessing, pre-registration, bounded verificationism) get sources snapshotted/ingested before the notes are written, or are they cited from the literature like Darby & Karni?
- Does the ladder's L1 `produced_by` belong in frontmatter (per-artifact) or the event ledger (per-derivation-event)? `model-provenance.md` argues events for canonical notes; one-shot derivatives may differ.
- Is decay-of-verifiability worth its own treatment (re-fetchable snapshots, moving upstream repos), or a paragraph in the core note?
- Does the carried-witness family outgrow the core note into a third note of its own? `title-as-claim-enables-traversal-as-reasoning` already owns part of the territory; a split would need a boundary against it.
- Where does the reviewer's *linked neighborhood* end for "state"? The conformance gate already answers this operationally (pre-resolved links only); the note should state it as a boundary, not rediscover it.

---

Relevant Notes:

- [ADR 038](../../reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — depends-on: the watched note←type edge this theory generalizes
- [verifiability gradient](../../notes/verifiability-gradient.md) — contrasts: orthogonal axis — cost/mechanism of checking vs what can be checked at all, and when
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the recomputable special case; provenance records are the non-recomputable complement
- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — grounds: the build-product model the invalidation corollary formalizes
- [model provenance](./model-provenance.md) — see-also: the model edge as an instance of the ladder
- [current practices and theory](./current-practices-and-theory.md) — see-also: the descriptive inventory this frame reorganizes
