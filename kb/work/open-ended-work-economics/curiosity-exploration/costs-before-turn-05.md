# Worker costs before turn 5

Measured from the 16 completed workers' `execution.json` usage and timestamps, located through the retained per-worker return records. All inherited `openai/gpt-6-astra`, requested thinking `medium`. No descendants were launched. These are harness-reported model costs, not independently reconciled billing. Cache-read tokens are counted separately from input. Coordinator work, operator attention, and counterfactual opportunity costs are excluded/unknown; no claim of cost-effectiveness follows.

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

Totals: 665121 input tokens; 48957 output tokens; 6080384 cache-read tokens; $15.179444 reported worker cost; 49.27 summed worker minutes. Sequential scheduling means no worker-time overlap, but parent coordination gaps are not included.

No operator intervention occurred between turns after permission to run all five without pauses. No experiments or implementation were performed. The first trial is not a matched comparison; differences in topics, instructions, evidence and model work prevent inferring superiority from totals.
