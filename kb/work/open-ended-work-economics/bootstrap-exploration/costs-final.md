# Final worker costs

Extracted by the coordinator from all 20 retained execution records after turn 5. These are measured worker totals only: coordinator usage, operator attention, scheduling gaps and validation after the runs are excluded. Seconds are elapsed wall time, not compute time. The harness cost field has no currency label in these records and is not verified billing. Cache-read tokens are separate. Earlier unknowns remain accurate accounts of what was available at handoff; `costs-before-turn-05.md` preserves that intermediate view.

| Turn | Worker seconds | Input tokens | Output tokens | Cache read | Reported cost |
|---|---:|---:|---:|---:|---:|
| turn-01 | 1245.103 | 216470 | 17008 | 1342592 | 4.357692 |
| turn-02 | 1216.951 | 197663 | 15168 | 2075264 | 4.810294 |
| turn-03 | 1229.817 | 207292 | 16093 | 2213504 | 5.091074 |
| turn-04 | 1242.432 | 203767 | 17272 | 2239104 | 5.140374 |
| turn-05 | 1356.437 | 260761 | 20076 | 2838656 | 6.450066 |
| **Total** | **6290.740** | **1085953** | **85617** | **10709120** | **25.849500** |

## Audit paths

- turn-01/critic: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-28-46-540Z_01a1ac8a-984b-7396-b62e-81d3fa1f45dc.jsonl.subagent/823b5172-0060-4375-a193-6a629cb9daef/execution.json`
- turn-01/explorer-a: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-15-42-053Z_01a1ac7e-9fe4-7782-880c-de1483f0bc6a.jsonl.subagent/bb3c3ac0-548e-43a0-9403-5b11053449ab/execution.json`
- turn-01/explorer-b: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-22-26-921Z_01a1ac84-cd68-7403-a32f-24570b4f5f0d.jsonl.subagent/26092fe3-65ab-441f-ae65-41a21ec2c6bf/execution.json`
- turn-01/integration: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-32-56-053Z_01a1ac8e-66f5-71d1-bf33-5923e9495be9.jsonl.subagent/0fc52ede-9bba-4cf7-bbe4-ce3b58f684b5/execution.json`
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
- turn-05/critic: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-58-27-736Z_01a1acdc-b498-72d8-9b27-f95297a4faa7.jsonl.subagent/4ef203b2-bf82-44a0-8acd-025d36732171/execution.json`
- turn-05/explorer-a: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-47-09-228Z_01a1acd2-5a2b-77a2-b390-51bbd7bd43da.jsonl.subagent/d6355483-bcdb-4625-a7f8-be5d4ee90485/execution.json`
- turn-05/explorer-b: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T17-53-10-352Z_01a1acd7-dcd0-711b-a404-0b427da79ce6.jsonl.subagent/074e353d-f6a7-4518-9b86-2c23f521abb1/execution.json`
- turn-05/integration: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T18-03-08-498Z_01a1ace0-fd51-77d3-b980-f03a2dce1f46.jsonl.subagent/40959e5d-feb4-41c7-98f2-15147a4a5a2f/execution.json`
