# AutoReason compounding trial: synthesis preferred, source unchanged

The one-pass trial produced a meaning-preserving editorial candidate. All three blind judges ranked the synthesis above the critic-led revision and the original. The independent auditor and final parent fidelity check passed; deterministic validation at the intended source path was clean. The user has not yet accepted or rejected the proposed edit.

## Outcome and changes

| Candidate | Borda points | Disposition |
|---|---:|---|
| Original (A) | 3 | Retained unchanged as baseline |
| Critic-led revision (B) | 6 | Valid alternative, not selected |
| Synthesis (AB) | 9 | Proposed candidate; pending user review |

The candidate separates direct uptake from the three links of indirect reinvestment, makes the Agent Optimizers allocator-and-consumption requirement easier to read, and presents Harness Benefit measurement evidence before the final compounding implication. Title and description are unchanged. The exact edit is in [proposed.diff](./proposed.diff); the complete candidate is [current_a.md](./current_a.md).

## Execution and evidence

- Source: `kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md`.
- Original SHA-256: `87f830ec33d99003450b8dac030c7c080dad1dde7a31a89679b48c172b5d0b19`; unchanged at completion.
- Candidate SHA-256: `114efebda48038356d11121adfd56e4e5222026cbad487c61d34b2ea2f7025b4`.
- Frozen skill SHA-256: `78ba60c18097643e95919ab6159c081e1b8c0402ba0e2feeacdf5ab73698e5b8`; exact copy in `protocol.md`.
- User override: one pass, original stays untouched for review. The frozen protocol's role prompts, constraints, checks and judging rule were retained.
- Seven fresh actors: critic, B author, synthesizer, auditor, three parallel blind judges. No reruns, sidecar, missing outputs or protocol recovery.
- Started 2026-09-25T06:41:59.722524+00:00; completed 2026-09-25T06:53:33.874307+00:00; elapsed 11.6 minutes including orchestration and checks. Actor timestamps record dispatch/handoff observations, not billed latency.
- Model provenance: Codex, GPT-6 family; exact runtime model ID not supplied. Token and financial cost were not supplied by the harness.
- [Pass result](./pass_01/result.md), [parent candidate checks](./pass_01/candidate_checks.md), [independent audit](./pass_01/auditor/output.md), [judge 1](./pass_01/judges/judge_1.md), [judge 2](./pass_01/judges/judge_2.md), [judge 3](./pass_01/judges/judge_3.md), and `final-validation.json` retain the evidence.

## What this trial establishes

This is one observed successful traversal of the current protocol: all roles returned usable artifacts, the candidates passed the safeguards, and the judges consistently preferred the modest reorganization. It supplies a reviewable proposal. User usefulness remains pending. One note, one model family and one pass do not establish general effectiveness, convergence, cost advantage, or superiority to a simpler edit. No simpler-workflow comparison or test of the old semantic-drift cases was run. Earlier failure reports were not supplied to any actor.

## Retention and next decision

Keep the full bundle while the user reviews the trial and decides its experimental disposition. No live note, skill or implementation was changed, and no commit was made. Application requires explicit approval. A later retained case should distinguish observed results from diagnostic hypotheses and should preserve this run's actual outcome; no semantic failure was observed here. A durable searchable failure store has not been implemented by this trial.
