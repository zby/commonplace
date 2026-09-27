# Evaluation additions, second chunk

## Scope and decision

On 2026-09-27 the operator requested the next chunk. This pass reads the next
ten open evaluation suggestions in stable queue order. All ten qualify under
the unchanged head: each develops what a check, comparison, or experiment
can establish and the limits on that inference.

This is a metadata placement decision. It does not certify the truth of a
note, reproduce its experiments, or reopen its source grounding. Note bodies,
head definitions, original reviewer words, and frozen baselines are unchanged.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-047 | [A checked outcome licenses retaining an episode, not abstracting its explanation](../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) | The note separates outcome checks from valid and faithful process evidence, explains what one checked episode warrants, and requires separate evidence before abstracting its explanation. |
| ADD-056 | [Competing causal theories can guide distinguishing experiments](../../notes/competing-causal-theories-can-guide-distinguishing-experiments.md) | The constructed causal models agree observationally but disagree under intervention. The note specifies a discriminating experiment and explains why finite results provide statistical discrimination rather than final verification. |
| ADD-057 | [Compounding is tested in later improvement, not by the accepting metric](../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) | The note requires later improvement episodes, displaced productivity measures, causal traces, and baselines before claiming compounding. Its worked studies explicitly distinguish acceptance, uptake, attribution, and sustained effects. |
| ADD-075 | [A quotes-route rollout grounded more claim uses without earning claim identifiers](../../notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md) | The rollout fixes the claim-use unit, compares non-random cohorts, and limits its conclusion to a descriptive gap rather than a causal effect of representation. Those are substantive assessment and inference boundaries. |
| ADD-078 | [Exact implementation does not validate a requirement against its objective](../../notes/exact-implementation-does-not-validate-a-requirement.md) | The note separates local conformance to a requirement from evidence that the requirement serves an objective. It specifies the outcome, ablation, and composition checks needed for the latter relation and competing failure explanations. |
| ADD-081 | [False-positive generation is filtered; false-positive acceptance becomes operative](../../notes/false-positive-generation-is-filtered-before-retention.md) | The note explains what an acceptance oracle filters, why its false positives become operative, and why later correction requires further evaluation. Its oracle-limit analysis is substantive alongside its improvement-loop mechanism. |
| ADD-101 | [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) | The note separates retrieval, loading, transformation, activation, outcome, and upkeep, then fixes the task and conditions needed for an end-to-end comparison. Retrieval metrics alone are explicitly insufficient. |
| ADD-103 | [Known-target discovery benchmarks show reachability, not discovery closure](../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) | The note distinguishes target reconstruction from prospective discovery, explains leakage controls and proxy-oracle construction, and states which research decisions remain outside the benchmark. |
| ADD-104 | [Learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) | The dedicated fixed-layer section explains why improvement within one effective update space cannot validate alternatives held outside the experiment. The ACM and Meta-Harness cases develop that inference limit. |
| ADD-116 | [LLM output deviation requires three-way diagnosis because remedies target different relations](../../notes/llm-output-deviation-requires-three-way-diagnosis.md) | The note compares fixed-input resampling, meaning-preserving prompt variation, and conformance checks, specifying what each can identify. Worked studies separate observed variation from causal attribution and distinguish masking from repair. |

## Parent checks and accounting

Three original learning-theory gaps close after checking the supporting tags:

- PG-043 / ADD-057: compounding concerns how a system's retained changes help
  produce later changes to its own machinery, fitting self-improving-systems.
- PG-071 / ADD-081: the error asymmetry concerns candidate evaluation and
  operative retention, fitting improvement-loop and its self-improving-systems
  parent. Both were already present; learning-theory was missing.
- PG-081 / ADD-116: the note diagnoses output deviation and the remedies that
  target its causes, fitting llm-reliability.

This pass adds thirteen assignments across ten notes: ten evaluation and
three learning-theory parents. No assignments are removed. The evaluation
head is selective, so no additional curated entries are required. Complete
parent heads continue to route through the supported children.

The workshop now records 69 accepted addition entries, three duplicate removal
closures, and 134 open additions. All 68 original placement findings remain
resolved. PC-07 has 29 resolved and 100 open parent-gap entries.

## Verification

`commonplace-validate` passed on all sixteen changed files and on the tags
collection: zero failures and zero warnings. Separate checks confirmed thirteen
additions, no removals, ten unchanged note bodies, five unchanged heads, all
queue counts, and all fifteen recorded final hashes. `git diff --check` passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the ten note inputs and five heads read. The head
hashes are unchanged because this pass applies their existing inclusion rules.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/checked-outcome-licenses-episode-retention-not-abstraction.md` | `c433e02823d059b324a5b13588c1c614edc23d7776cbc3b840a32dc59259b1b0` | `655a104f475e3dcde65441805939e33b21ea189b89607104c25b6b3549a4c681` |
| `kb/notes/competing-causal-theories-can-guide-distinguishing-experiments.md` | `5bd482a09a674161cbc3ae70b7a0934204a9000d671c2d358fcf2d73fbc60a3b` | `a2e737bb4531fb0890bb3e927824060603781dd96e7a500ea2c18f865977f329` |
| `kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md` | `5a7a17fbe114becbfb7b9c4e2b7de2d2a4d2a295c4e19857362ae609de877aa0` | `23a59ad48d91e066e268dd106a7f46065c0e67cd0596b820208d56b2979cde87` |
| `kb/notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md` | `e65269ff9fa3f42cb31bbb1c23e732520612300777c7a3e6883ba1178d6becb1` | `b3b47d4e3ec4ad937f983496ff320a582792969d4c3b601705ab89f683afbce6` |
| `kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `0b1ca481ded77c87f11860c4738d9b627123b29654920eb1c6be3cd31d156b23` | `d37d7de94fd126263fd4427f3a5e3530c2595218fcfdbd4cc062169dc61d96ba` |
| `kb/notes/false-positive-generation-is-filtered-before-retention.md` | `3b71626a6683b400ce6d11ae423f545ad5ffe74262c09bffcfb57fc959bc5c5b` | `7ecaf4116da0b42fdad5186bfb74e17e933866a61cc787359d51403e6fbd2f24` |
| `kb/notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md` | `a55f18e7a11861b11645022db693e72b9d89dca5e5013543b44811fd1ce29058` | `5a5792a796dcc7ce9c5d1e67dde4ee145763a49458523845e0141990137b3887` |
| `kb/notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md` | `3d94c6ba3ccd6cd09977438bfe9ea8fe5c90be8e447c48a4439733b26d204f57` | `21a1f2e9854555cfbb556f5e49210365ef5a1f3d6d1a24b481fce9098e52a6af` |
| `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` | `7e336447cc9a9dbe68ae7f0c42decbafe3b889f838bdd8b042d75e1b350ffba8` | `e605bc55eccb63be62dbcc6d0dab7070062edb9b2bb91a4abbccbd0a23543b72` |
| `kb/notes/llm-output-deviation-requires-three-way-diagnosis.md` | `971412246481083a7d4acf782b33088629a7ddaa808362fe4e9ce7a900f602cb` | `6bcb84c9ed762f2e6887cba2ceb120b82c8f5e4737ce31df8124d4b546f40949` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/self-improving-systems-README.md` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| `kb/tags/improvement-loop-README.md` | `d52cb75a943a852508c0d6d52e024ae68870608916209a3225510dda44f63f1f` | `d52cb75a943a852508c0d6d52e024ae68870608916209a3225510dda44f63f1f` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
