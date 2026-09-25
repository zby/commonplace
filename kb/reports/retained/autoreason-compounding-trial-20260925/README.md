# AutoReason compounding trial: preferred revision still hard to read

On 2026-09-25, one AutoReason pass produced a revision that passed fidelity checks and won all three blind model comparisons. The operator still found it hard to read, as recorded in the later [gradual-rewrite rationale](./captures/proposed_gradual-rationale.md). After reviewing that proposal, the operator decided to keep autorevision experimental and stop further experiments for now. Neither revision was applied; the original note remains unchanged.

This dated report closes the workshop. Its consumer is a future operator review of whether to resume or change AutoReason. It records this trial and its disposition; it does not change the skill or schedule further work.

## Trial and measured result

The input was [Compounding is tested in later improvement, not by the accepting metric](../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), preserved as [original.md](./captures/original.md). The user authorized one pass instead of the protocol's default allowance of up to five, with the live note untouched for review.

Seven fresh agents filled the critic, revision author, synthesizer, auditor, and three blind-judge roles. The [frozen protocol](./captures/protocol.md) retains their role prompts and constraints; [run-state.json](./captures/run-state.json) records the task-specific overrides, input files, actor identities, timestamps, and hashes. Model provenance was Codex, GPT-6 family; the exact runtime model ID, token usage, and financial cost were not supplied.

Each judge ranked synthesis above critic-led revision above original. With 3/2/1 Borda scoring:

| Candidate | Points | Trial result |
|---|---:|---|
| Original (A) | 3 | Preserved as baseline |
| Critic-led revision (B) | 6 | Passed checks |
| Synthesis (AB) | 9 | Selected for operator review |

The independent auditor and parent semantic-fidelity check passed. Deterministic validation at the intended live path was clean. There were no reruns, missing outputs, or substantive-revision sidecar. Elapsed time was 11.6 minutes, including orchestration and checks. The [pass result](./captures/pass_01/result.md), [audit](./captures/pass_01/auditor/output.md), and [validation record](./captures/final-validation.json) preserve these observations. The [selected candidate](./captures/current_a.md) and [diff](./captures/proposed.diff) retain the proposed edit.

## Operator review and interpretation

The [critic](./captures/pass_01/critic/output.md) identified an important ordering problem: three substantial study discussions separated the protocol's introduction from its practical measures and baselines. B added a roadmap sentence; AB omitted it. Neither moved the practical protocol ahead of the studies. The selected revision improved local organization while retaining that teaching sequence.

The later [gradual proposal](./captures/proposed_gradual.md) instead introduces a hypothetical running example, defines terms as they appear, and places the studies after the requirements. It is a separate post-trial proposal, not an AutoReason output or a blindly judged candidate. A subsequent read-only check found unchanged frontmatter, link targets and occurrence counts, and the text from Scope onward; validation at the intended live path was clean. Those checks do not establish semantic equivalence. In particular, its new ladder may imply an ordering absent from the original, and its comparison with Harness Benefit may blur ordinary task uptake with uptake in a later improvement episode. It was not approved or applied.

The diagnostic hypothesis is that the protocol's ban on new examples and restriction of the author's reordering to local changes limited useful ways to explain the argument. This trial did not test a relaxed protocol, so it cannot establish that cause. The observed limit is narrower: unanimous relative preference among these candidates, alongside fidelity checks, did not settle the operator's reading difficulty. One note, one pass, and judges from one model family do not establish general effectiveness or cost advantage. Scientific sources were not independently reverified.

## Final disposition and retention

The operator's closing instruction was: “autorevision needs to stay experimental” and “I don't see reason to continue these experiments for now.” The experiment is closed without application. The skill remains experimental; no further trials or protocol changes are commissioned by this record. No failure-store machinery was implemented.

The [capture manifest](./capture-manifest.json) records all 36 preserved files and their SHA-256 hashes. The capture includes the original, all candidates, judgments, protocol, checks, and the separate gradual proposal and rationale. Files are preserved byte for byte. Historical paths, pending-review statuses, and cleanup instructions inside the capture describe the earlier run state; this report records the final disposition. Captured local type and link paths are data, not live report contracts.

Retain this frozen record for any future decision to revisit AutoReason. The temporary workshop is closed; interpretation of this result does not require its old location or ignored operational state.
