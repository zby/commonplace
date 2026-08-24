# Claim-pull cleanup

Repair a frozen cohort of pre-rule source dependencies after the prospective
path ships. The unit is one target claim, not one ingest.

1. Record each target path, revision, and claim before source reading.
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

The first run closes when every item has a terminal disposition or named
blocker and its validation/review result is recorded. Treat observed pressure
for reconciliation or finer identity as later design evidence.
