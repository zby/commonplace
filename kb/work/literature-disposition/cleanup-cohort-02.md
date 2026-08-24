# Cleanup cohort 02 — frozen 2026-08-24

Frozen at repository `6cdb3c10`. Cohort 01 was the claim-pull rollout's own run
(`agents-navigate-by-deciding-what-to-read-next`, `linking-theory`); this is the
first cohort under [the restored procedure](./cleanup-procedure.md).

Blob revisions are recorded so a later session can tell whether a target moved
under it. Verify with `git rev-parse --short HEAD:<path>`.

## Selection basis

Not alphabetical and not "most ingests." Three criteria, in order:

1. **Load-bearing** — a defect in a heavily cited note propagates, so grounding
   it returns the most per unit of work.
2. **Groundable now** — the named snapshot verifies by checksum, except where a
   blocked item is included deliberately to exercise that path.
3. **Exercises disposition variety** — the procedure requires a cohort that can
   produce narrowing or contradiction, not only missing citations. Two items
   below are selected because they are *likely to fail*.

Five targets, 16 note-to-ingest pairs. Small enough to finish; wide enough to
test the procedure's disposition vocabulary.

## Cohort-specific note

**One target is contaminated.** [claim-inventory.md](./claim-inventory.md)
already publishes recalled claims and tradition placements for
`knowledge-storage-does-not-imply-contextual-activation`. Inventory that note
from the note itself first; then treat those placements as reading assignments,
never as findings. They were recalled, not read.

## Targets

### 1. `knowledge-storage-does-not-imply-contextual-activation` — blob `2438659f`

190 inbound references, the highest in the corpus. Five cited ingests, four
groundable, one blocked.

- `agents-explore-but-agents-ignore-llms-lack-environmental` — **blocked**, needs re-ingest
- `llm-agents-are-not-always-faithful-self-evolvers`
- `machine-studying`
- `the-second-brain-trap-2041486539067154753`
- `verbalizable-representations-global-workspace-llms`

**Expected to be the hardest item, and chosen for it.** The
[claim inventory](./claim-inventory.md) found its two halves disjoint: the famous
claim — knowledge present without affecting the next action — is recalled as
Tulving's availability/accessibility distinction and cited to nobody, while the
half 158 reviews and a type spec actually consume is the wholly local `read-back`
definition. All five cited ingests are LLM-side. So grounding should surface a
**corpus gap** rather than a claim: the source that would settle its central
proposition is not captured, and is cognitive psychology rather than anything in
the current corpus. That outcome is a `literature handoff`, and it is a direct
test of whether the procedure reports a missing tradition instead of grounding
the claim in whatever ingest is nearest.

**Progress 2026-08-24 — one bounded grounding pull complete; disposition still
open.** The target's context-to-action discussion supplied this source-side
need: whether explicitly consulted documentation is consistently followed by
implementation and verification in observed coding-agent traces. [Gao and
Chen's trace study](../../sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md)
was captured and ingested, then received one demand-driven Claims entry:
"In Gao and Chen's observational coding-agent traces, explicit documentation
consultation was not consistently coupled to immediate implementation and
verification: the code-edit association depended on statistical adjustment,
while test and build actions were less frequent within the next three events in
both unadjusted and adjusted analyses." All three retained extracts matched the
checksum-verified primary snapshot, and the populated ingest passed
`commonplace-validate` cleanly.

This grounds only the paper's short-horizon observational result. It does not
establish the note's general proposition, identify consultation with contextual
activation, or replace the cognitive-psychology source assignment above. The
target remains unchanged at its frozen blob; comparison, disposition, any note
edit, and source-lens review remain open.

### 2. `axes-of-artifact-analysis` — blob `85748ef0`

178 inbound, one cited ingest (`intern-s2-mobius-arxiv-v1`). The clean
high-dependency, single-source case — the control against which the harder items
read.

### 3. `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` — blob `53c418cd`

15 inbound, five cited ingests, all groundable.

- `convexbench-can-llms-recognize-convex-functions`
- `gsm-dc-llm-reasoning-distracted-irrelevant-context`
- `llm-webagents-long-context-reasoning-benchmark`
- `paulsen-maximum-effective-context-window-mecw`
- `verbalizable-representations-global-workspace-llms`

**Tests multi-source composition.** Whether five separately grounded claims
compose into one local claim, or whether the note leans on a composite no single
source supports — the exact defect found in the Pirolli case, where two separate
results were merged into a pointer-level tradeoff the source never makes. Also
shares an ingest with target 1, so it tests whether one ingest serves two
different demands without entry conflict.

### 4. `exact-implementation-does-not-validate-a-requirement` — blob `c32dc467`

19 inbound, four cited ingests, three groundable, one blocked
(`lessons-from-building-ai-agents-for-financial-services`).

**Deliberately includes a blocked item** so the run exercises re-ingest routing
and the `unavailable` disposition rather than discovering that path mid-sweep.

### 5. `bitter-lesson-selects-against-unearned-reach-not-against-structure` — blob `3e9c4546`

13 inbound, three cited ingests, all groundable.

- `in-search-of-lost-domain-generalization`
- `the-risks-of-invariant-risk-minimization`
- `wikipedia-bitter-lesson`

**Selected as the most likely contradiction.** The bitter lesson is a widely
paraphrased claim, one of its sources is a Wikipedia article rather than Sutton's
text, and the note asserts a *reading* of it. If any item in this cohort returns
`contradicted/repaired` or `narrowed`, this is the one.

## Recording

Per target: claim as stated before source reading, disposition, resulting
`Claims` entries, note repair if any, validation result, and source-lens verdict.
Record candidate precision and unavailable sources; make no corpus-recall claim.

## Expected distribution

Recorded before the run, and **sealed** in
[cohort-02-prediction.md](./cleanup-cohort-02-prediction.md). Do not open that
file while executing this cohort: a stated distribution is an anchor, and an
executor who knows the prediction will tend to produce it — the same charitable
bias this procedure exists to defeat, in a new costume. Open it when judging the
finished run.
