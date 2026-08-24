# Grounding cleanup procedure

Restored 2026-08-24 from the claim-pull implementation workshop, which trimmed
it to this form and then deleted it on closure after running only cohort 01
(two notes). The prospective rule now ships — [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
plus [`ground-source-dependent-claims.md`](../../instructions/ground-source-dependent-claims.md)
— but the retrospective half was left without a home while 66 of the 68
ingest-citing notes remain ungrounded. This is Channel 1 of
[three-channels](./three-channels.md), and this workshop owns it.

Deliberately **not** promoted to `kb/instructions/`. It fires only on a corpus
sweep, which is one-off migration work — the same call
`decide-what-documentation-an-llm-needs.md` recorded for its own audit half.
Delete it when the sweep is done, not before.

## Procedure

Repair a frozen cohort of pre-rule source dependencies. **The unit is one target
claim, not one ingest.**

1. Record each target path, revision, and claim **before source reading**.
2. Run the grounding instruction for its exact source-side need. If the local
   observation is absent, use normal re-ingest and retry.
3. Compare the target with the selected normalized claim, scope, limitation,
   and transfer.
4. Disposition it as false positive, unavailable, grounded, narrowed,
   contradicted/repaired, retained local delta, or literature handoff.
5. Prefer the selected normalized wording exactly, link the ingest, validate,
   and run source-as-gate review.
6. Record unavailable sources, repairs, and similar-entry accumulation.

Do not infer Claims from old ingest prose, mutate existing entries, or ground a
secondary resource against the primary snapshot.

A run closes when every item has a terminal disposition or named blocker and its
validation and review result is recorded. Treat observed pressure for
reconciliation or finer identity as later design evidence.

## Two additions from this session's evidence

**Step 1's ordering is load-bearing, not bookkeeping.** Recording the target's
claim in its own language before reading the source is what prevents the
over-attribution that has now occurred twice: the first worked case called C1 and
C3 subsumed, and a blind pass tightened both to needs-narrowing. A reader holding
target and source together reads thematic overlap as support.

**Do not bulk-populate.** 192 of 286 ingests are cited by no note, and claims are
pulled because demand identifies which proposition matters and in whose terms. A
sweep over every ingest reverts to the push model whose novelty polarity
discarded the premises notes actually lean on. The rollout ratio is the argument:
two demand-driven entries in the Pirolli ingest grounded, narrowed, or repaired
**eight** frozen uses across two notes.

## Corpus state at freeze (2026-08-24)

| Measure | Count |
|---|---|
| Tracked ingests | 286 |
| Name-paired snapshot present and checksum-verified | 265 |
| Named snapshot missing (routes to re-ingest) | 21 |
| Named snapshot present with wrong bytes | 0 |
| Ingests with populated `Claims` | 1 |
| Notes citing an ingest | 68 |
| Distinct ingests cited by a note | 94 |
| — groundable now | 87 |
| — blocked on a missing snapshot | 7 |
| Ingests cited by nobody | 192 |

The 94 cited ingests are the working universe. The 192 uncited ones are not a
queue.

**Blocked on re-ingest**, worth running in parallel since they gate cohort items:

- `agents-explore-but-agents-ignore-llms-lack-environmental`
- `discoverphysics-benchmarking-llms-out-of-the-box-scientific`
- `from-entropy-to-epiplexity-rethinking-information-computational`
- `language-models-like-humans-show-content-effects-on-reasoning`
- `lessons-from-building-ai-agents-for-financial-services`
- `palantir-ontology-vs-decision-traces`
- `we-should-take-text-optimization-more-seriously`
