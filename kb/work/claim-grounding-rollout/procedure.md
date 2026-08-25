# Grounding cleanup procedure

Restored 2026-08-24 from the claim-pull implementation workshop, which trimmed
it to this form and then deleted it on closure after running only cohort 01
(two notes). The prospective rule now ships — [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
plus [`cp-skill-ground`](../../instructions/cp-skill-ground/SKILL.md)
— but the retrospective half was left without a home while 66 of the 68
ingest-citing notes remain ungrounded. This is Channel 1 of
[three-channels](../literature-disposition/three-channels.md), and this workshop owns it.

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

**Record the scope of a negative, not just the verdict.** A "no external source"
result is only ever "not found in what was searched." Written without its bound,
it reads as "checked," which is a stronger claim than the evidence supports and
suppresses the later widening that would find the source — the mechanism in
[stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md),
whose scope already covers "any artifact a consumer treats as exhaustive."

The near-miss: connect correctly rejected `addressability-grain` from Pirolli —
"the source assumes the target is unknown, which is the premise the note
discharges" — while its actual nearest literature is storage read amplification,
never searched because the cohort was scoped by the label "navigation." Of five
notes later inventoried per-claim, one fell inside that label.

**This is not an argument against broad sweeps.** Two searches do different jobs
and neither replaces the other. A targeted search derived from the claim's own
mechanism is cheap and precise when you can already name the mechanism — asking
*who else studies cost granularity?* reaches storage systems in one step. A broad
sweep is expensive and imprecise but finds the tradition you could not have named,
which is exactly the case that produced this near-miss. Run both; prefer the
targeted one first because it is cheap, and treat the broad one as the check on
what the targeting assumed.

The rule binds harder on the broad sweep, not softer. A wide search produces the
strongest illusion of exhaustiveness — "we looked everywhere and found nothing"
is the most suppressive negative available — so a broad sweep must record its
angles, and its findings are reading assignments rather than verdicts.

**Do not bulk-populate.** 192 of 286 ingests are cited by no note, and claims are
pulled because demand identifies which proposition matters and in whose terms. A
sweep over every ingest reverts to the push model whose novelty polarity
discarded the premises notes actually lean on. The rollout ratio is the argument:
two demand-driven entries in the Pirolli ingest grounded, narrowed, or repaired
**eight** frozen uses across two notes.

## Executing a cohort

Enough to hand to an agent cold. Follow
[the procedure](./procedure.md); these are its literal routes.

**Your first task is step 1**, which a cohort manifest deliberately does not do for you:
inventory each target's load-bearing claims **from the note itself, before
reading any source**, and record them here as a table of `ID | target | claim as
frozen | source-side need` — the shape [cohort 01](./cohort-01.md) used.
Reading the source first lets its vocabulary decide what counts as a claim, which
is how the first pass over-attributed two claims it later had to retract.

**To ground a claim:**

```
Invoke cp-skill-ground
with Target: <exact ingest path or canonical source URL>
and Claim needed: <source-side proposition or question>.
```

**When the named snapshot is missing** (the blocked items below):

```
Read and execute kb/instructions/re-ingest.md with Target: <exact ingest path>.
```

Do not ground a claim by reading the ingest's existing analysis prose — only the
checksum-verified snapshot establishes a source claim. A verbatim extract may
span wrapped lines; matching normalizes whitespace.

## Cohort 01 baseline, carried from the closed source-grounding workshop

The claim-pull rollout's own run is the baseline against which "pressure for
finer identity" is judged. [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
records the decision — "V1 has no claim IDs, merge, deduplication, or
reconciliation protocol" — but not the evidence for it, which was held in a
workshop now deleted.

Two demand-driven Claims entries in the Pirolli ingest were enough to ground,
narrow, or repair **eight** frozen uses across two notes, each entry carrying the
source proposition, extracts and locations, scope, confidence, and limitation.
Whole-ingest links sufficed: the source lens derived one pair per note, judged
every use against the complete section, passed both repaired notes, and left no
stale pair. **No ambiguous claim identity, similar-entry accumulation, or need
for a thin intermediate node was observed** — in a run of two entries over two
notes, which is what that finding is worth. It does not settle whether a denser
corpus earns claim IDs or separate nodes.

The run also confirmed that transfer belongs in the target: Pirolli grounded the
human proximal-cue/distal-source structure while the notes separately argued what
carries to bounded-context agents. No source was unavailable, and no case needed
an artifact-level disposition handoff — both untested paths that cohort 02
deliberately exercises.

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
