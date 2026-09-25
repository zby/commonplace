# One-pass AutoReason experiment on the compounding note

User direction, 2026-09-25: run one pass of AutoReason on the compounding note, preserving the original for review. The one-pass limit overrides the skill's default maximum of five passes; actor roles, checks, bounded recovery and judging rules stay unchanged.

Purpose: inspect whether this workflow produces a useful meaning-preserving editorial revision, and retain successful and rejected candidates so the trial can inform later workflow evaluation. One note cannot establish general effectiveness or cost superiority. This is not an experiment on the truth of the note's scientific claims.

Target: `kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md`.
Original SHA-256: `87f830ec33d99003450b8dac030c7c080dad1dde7a31a89679b48c172b5d0b19`.
Protocol: `kb/instructions/cp-skill-revise-autoreason/SKILL.md`.
Protocol SHA-256: `78ba60c18097643e95919ab6159c081e1b8c0402ba0e2feeacdf5ab73698e5b8`; exact copy in `protocol.md`.
Started: 2026-09-25T06:41:59.722524+00:00.
Runner: Codex, GPT-6 family; exact runtime model ID not supplied.

All workers are fresh, receive only their role inputs, and own disjoint run files. Judges see only anonymized candidates. The parent schedules, checks semantic fidelity and records outcomes. Earlier AutoReason failures do not enter worker contexts. Relative links in candidate copies retain the target note's original resolution context.

Normal budget: seven fresh agents for one pass; early-stop or bounded repair/sidecar paths follow the frozen skill. Track actual calls, elapsed time and retained bytes; token cost is unknown unless supplied by the harness.

Closure: finish the single pass or its required early-stop/sidecar, record all rankings and fidelity checks, present the candidate/diff or no-change result, and retain the bundle while the user reviews the experiment. Applying a candidate requires explicit approval. Do not delete evidence as routine cleanup while the experiment's disposition remains open. No implementation or skill changes are authorized by this trial.

Current execution state: `run-state.json`.

## Trial complete

See [summary.md](./summary.md) and [proposed.diff](./proposed.diff). One pass used seven actors with no retries. The synthesis won 9–6–3 and passed all checks. The source remains unchanged; human review and application disposition are pending.
