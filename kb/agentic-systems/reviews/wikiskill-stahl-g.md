---
type: kb/types/note.md
description: "Stahl-G's independent WikiSkill implementation: host-agent learning requests, persistent Wiki updates, and score-gated skill adoption."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-17-wikiskill-stahl-g-01
source-identity: https://github.com/Stahl-G/wikiskill
reviewed-revision: "9df975b2145a0e924f344f2a3d116e11d3f025ac"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md
analysis-result-sha256: d6a4b32fa658039947b437460c8e9e70207ab3e867012f0e0da195f456544c8a
---

# WikiSkill (Stahl-G)

Evidence basis: static source-code and shipped-instruction inspection at [commit 9df975b](https://github.com/Stahl-G/wikiskill/tree/9df975b2145a0e924f344f2a3d116e11d3f025ac), 2026-09-17. This is **Stahl-G's independent implementation**, not the WikiSkill paper authors' code.

WikiSkill is an improvement workflow around an existing agent. It runs practice tasks, records outcomes, asks a Maintainer to update a persistent Wiki, asks a Proposer for a candidate skill, and retains that skill only when its validation score improves. The product controller returns work requests; the host owns model calls, tools and actual execution. Separate research paths invoke Codex directly, including an optional macOS isolation backend.

## Operation and authority

The normal loop is baseline validation → training with the current skill → Wiki maintenance → proposal → candidate validation → admission or rejection. The operator chooses tasks, scoring, rounds and host. Numeric scores come from an authorized external scorer or supplied ratings. The controller owns stage progression and strict successor selection; models supply diagnoses and proposed guidance.

> return improvement(candidate, incumbent, direction) > threshold
> --- https://github.com/Stahl-G/wikiskill/blob/9df975b2145a0e924f344f2a3d116e11d3f025ac/src/wikiskill/score_rules.py

Wiki updates and skill adoption have separate admission rules. Product patterns require valid source IDs and nonblank content, but are retained before candidate evaluation. A rejected skill therefore leaves the Wiki available to later optimizers. Score admission licenses the instruction bundle for the configured comparison; it does not independently validate each explanation in the Wiki.

Records preserve actual output files, scores, configuration and artifact hashes. Scoring failures retain output and require explicit retry. Changed task inputs or scorer conditions block comparison continuation. Installation is a separate operation with replacement checks, backups and guarded restoration. These controls support inspectable comparisons and recovery; scorer execution still has normal host permissions.

Native-role handoffs request fresh executor, Maintainer and Proposer contexts, require agent-ID binding, and limit executor payloads to task and selected skill. The binding is explicitly host-reported. Actual context separation and tool permissions depend on the enclosing host; they are not established by recording an ID. The isolated research backend is a distinct deployment-dependent path and does not extend its isolation to ordinary product use.

## Memory and learning

The persistent Wiki supplies reusable patterns; skills supply instructions; raw outcomes and traces supply evidence. Product learning contexts select completed training records for the current round and supply the Wiki and feedback. Research maintenance supplies the full Wiki with bounded trace excerpts. Research proposers receive an index, incumbent skill and summarized impacts, with full patterns and trajectories available for requested reads.

This wires staged learning across tasks through durable files, without requiring model-weight updates. Automatic trace compaction also creates retained optimizer context. Delivery is established; actual use of recalled content and measured benefit were not verified in this analysis. Generic product output files can contain opaque payloads, so a complete representation classification is intentionally undetermined.

Retained reasons vary by route. General product context includes proposal notes; native learning context removes those notes from prior gate history. Research impact summaries carry purpose and motivating pattern references, but not every rationale or diff, and some resume paths lose rationale metadata. A retained skill therefore does not guarantee that later diagnosis receives its original explanation.

The isolated spreadsheet study supplies training reference-cell feedback and checks successful proposer trace reads. Those checks establish reference-count consistency and file access, not that an explanation caused the resulting proposal. Reference visibility also differs across paths; there is no universal guarantee that all learning roles are denied reference answers.

## Scope

This review establishes implemented and afforded routes, not observed improvement or causal effects. Host/provider internals, live datasets/services and historical performance experiments were not audited. Runtime checks were static; no paid model calls or benchmark executions were performed.

Wiki/skill rules can form a revisable theory, but source-level delivery, edits and score feedback do not establish complete reflective theory refinement. Candidate-linked diagnosis, distinguishing tests and later behavioral traces would be needed. The score gate supports bounded operational adoption, not general truth or transfer guarantees.

The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md) retains source quotations, runtime forcing cases, memory comparison fields, both lenses and their limitations.

---

- [Theory refinement](../../notes/definitions/theory-refinement.md) — defined-in: the distinction between revising retained rules and establishing their evidence-responsive correction
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — defined-in: consumer, channel, force and horizon used to distinguish instruction delivery from activation
