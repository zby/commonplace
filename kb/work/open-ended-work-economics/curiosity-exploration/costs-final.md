# Final measured worker costs

All five turns completed: twenty fresh workers, sequential explorer A, explorer B, critic, integrator per turn. No descendants launched. All workers inherited `openai/gpt-6-astra`, requested thinking `medium`; none was a bulk/simple retrieval assignment. No Sol assignment was needed. Explorer budgets were depth 2/workers 2; critics and integrators zero/zero.

## Measurements

Read from each completed worker's `execution.json` usage and start/end timestamps, located through the retained per-worker return records. These are harness-reported model costs, not independently reconciled billing. Cache-read tokens are separate from input. Coordinator work, operator attention and counterfactual opportunity costs are excluded/unknown. No claim of cost-effectiveness follows.

| Turn | Worker | Elapsed seconds | Input tokens | Output tokens | Cache-read tokens | Reported cost (USD) |
|---|---|---:|---:|---:|---:|---:|
| turn-01 | critic | 172.3 | 37341 | 2547 | 352896 | 0.853656 |
| turn-01 | explorer-a | 247.8 | 49906 | 5134 | 466816 | 1.222576 |
| turn-01 | explorer-b | 199.6 | 55852 | 3370 | 347008 | 1.074028 |
| turn-01 | integration | 208.1 | 38308 | 2829 | 417792 | 0.942322 |
| turn-02 | critic | 156.4 | 41825 | 2624 | 391552 | 0.941002 |
| turn-02 | explorer-a | 216.8 | 47552 | 3459 | 527744 | 1.176214 |
| turn-02 | explorer-b | 217.9 | 36112 | 3348 | 434944 | 0.963464 |
| turn-02 | integration | 158.7 | 51385 | 2575 | 265216 | 0.907816 |
| turn-03 | critic | 177.9 | 38007 | 2652 | 381952 | 0.894622 |
| turn-03 | explorer-a | 181.3 | 42678 | 3005 | 354816 | 0.931846 |
| turn-03 | explorer-b | 191.3 | 31756 | 3018 | 315520 | 0.783980 |
| turn-03 | integration | 128.2 | 36292 | 2733 | 150016 | 0.649586 |
| turn-04 | critic | 169.3 | 40202 | 2639 | 434432 | 0.968402 |
| turn-04 | explorer-a | 177.2 | 37119 | 3149 | 385920 | 0.914560 |
| turn-04 | explorer-b | 193.2 | 38674 | 3052 | 378368 | 0.917708 |
| turn-04 | integration | 160.1 | 42112 | 2823 | 475392 | 1.037662 |
| turn-05 | critic | 141.6 | 37141 | 2938 | 203904 | 0.722214 |
| turn-05 | explorer-a | 170.8 | 33447 | 3090 | 349056 | 0.838026 |
| turn-05 | explorer-b | 172.5 | 39573 | 3141 | 293120 | 0.845900 |
| turn-05 | integration | 198.2 | 46013 | 3608 | 575232 | 1.215762 |

Totals: **821295 input tokens; 61734 output tokens; 7501696 cache-read tokens; $18.801346 reported worker cost; 60.65 summed worker minutes.** Cache-write tokens: 0. Sequential scheduling means no worker-time overlap, but parent coordination gaps are not included. Token totals reflect repeated context, not unique evidence read.

The [pre-final record](./costs-before-turn-05.md) was available to all final-turn roles and is preserved unchanged. Their final cost discussion correctly covers only sixteen workers; this report supplies the completed accounting.

## Interventions and limits

The operator authorized the second exploration and explicitly instructed all five turns without pauses. There were no between-turn operator interventions. The coordinator selected/replanned each question and intentionally did not adopt turn 2's proposed exclusive verification chronology; turn 3's coordination retains the reason. Thus trajectory is not evidence of autonomous question selection.

No experiments, implementation, extraction, commits or deletion occurred. The first run remains intact. The only source mutation was eleven grounded verbatim excerpts added to the Formal Theory of Creativity ingest's Quotes section. Broader focused literature search was not completed. Existing sources and repository arguments supported the documentary inquiry; no new external-source ingest was created.

No matched baseline, role ablation or causal comparison was run. Comparing first- and second-run costs cannot establish superior steering: topics, instructions, evidence and model work differ. Local session and audit paths in return records support accounting on this machine; research findings are in the Markdown results, not dependent on private reasoning transcripts.
