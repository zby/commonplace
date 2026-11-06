# Worker costs before turn 5

Coordinator extraction from retained execution.json records after turn 4. Turn 1 measurements remain in `turn-01/coordination.md`. These figures exclude coordinator work, scheduling gaps, operator attention and future validation. Earlier worker statements of unknown costs describe availability at their handoff, not zero expenditure. Cost is the harness-reported field, with currency unspecified in these records; it is not verified billing. Seconds are elapsed wall time, not model compute. Cache reads are separate from input/output tokens.

| Turn | Role | Seconds | Input | Output | Cache read | Reported cost |
|---|---|---:|---:|---:|---:|---:|
| turn-02 | critic | 259.979 | 48643 | 3292 | 488576 | 1.1396060000000001 |
| turn-02 | explorer-a | 337.794 | 69632 | 4270 | 616320 | 1.5261399999999998 |
| turn-02 | explorer-b | 349.416 | 39116 | 4140 | 527360 | 1.1255199999999999 |
| turn-02 | integration | 269.762 | 40272 | 3466 | 443008 | 1.019028 |
| turn-03 | critic | 226.552 | 41125 | 3322 | 264320 | 0.84167 |
| turn-03 | explorer-a | 377.978 | 48626 | 4322 | 728320 | 1.43068 |
| turn-03 | explorer-b | 426.842 | 59756 | 4695 | 950272 | 1.7825819999999999 |
| turn-03 | integration | 198.445 | 57785 | 3754 | 270592 | 1.0361420000000001 |
| turn-04 | critic | 290.139 | 53003 | 3534 | 498560 | 1.20529 |
| turn-04 | explorer-a | 321.47 | 37348 | 4780 | 535040 | 1.1475199999999999 |
| turn-04 | explorer-b | 344.528 | 46977 | 4698 | 598656 | 1.303326 |
| turn-04 | integration | 286.295 | 66439 | 4260 | 606848 | 1.4842380000000002 |

## Evidence

- turn-02/critic: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-55-19-455Z_01a1aca2-e69f-7780-a986-1b2ef09c282e.jsonl.subagent/214193c5-c08c-4148-85ec-cfa4520ecc75/execution.json`
- turn-02/explorer-a: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-43-51-321Z_01a1ac98-6698-702d-ad26-ccf95ac30811.jsonl.subagent/cc8cb62f-49fd-4252-a0c2-bb7ab30e6933/execution.json`
- turn-02/explorer-b: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-49-29-612Z_01a1ac9d-900b-75a6-ab62-9d2a0984703d.jsonl.subagent/5b45b8a4-70a4-480b-b695-4f6bbffa635d/execution.json`
- turn-02/integration: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-59-39-881Z_01a1aca6-dfe8-778d-b7f4-04afea828e38.jsonl.subagent/3582eaad-c740-47b6-9fd0-954fdea22de0/execution.json`
- turn-03/critic: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-18-15-943Z_01a1acb7-e787-738b-b4e7-9d02c4fd856c.jsonl.subagent/9a4aa3bf-cf8e-4498-b8cd-da5075cc809b/execution.json`
- turn-03/explorer-a: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-04-50-228Z_01a1acab-9c33-701e-870c-1370ebae7d81.jsonl.subagent/24c4f3b8-e031-47db-870e-8f0858728b33/execution.json`
- turn-03/explorer-b: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-11-08-676Z_01a1acb1-6283-72a2-9f9c-1eff4940abe5.jsonl.subagent/d53c5bf3-0714-4484-a839-e17a6aef5dda/execution.json`
- turn-03/integration: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-22-02-948Z_01a1acbb-5e44-7489-8f5f-1050617de540.jsonl.subagent/6735a35c-2f30-456a-9e0a-4eed60b2e926/execution.json`
- turn-04/critic: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-36-56-414Z_01a1acc9-005e-76e5-b80f-40344c090406.jsonl.subagent/73708b18-be4d-4cd6-9f4d-6c01c56e495c/execution.json`
- turn-04/explorer-a: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-25-49-537Z_01a1acbe-d361-7171-ad3a-bec9291cb3de.jsonl.subagent/86f8e8cc-0ac5-400d-8802-3b08882aba54/execution.json`
- turn-04/explorer-b: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-31-11-450Z_01a1acc3-bcd9-7336-8999-d9c159ee2c84.jsonl.subagent/b7d2d44e-39a6-4ada-a475-076bb72edf0e/execution.json`
- turn-04/integration: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-41-46-979Z_01a1accd-6f63-72cc-b98b-c37351e04169.jsonl.subagent/beec8fbe-1c3d-4623-8bf5-0801493b2691/execution.json`
