---
{
  "type": "note",
  "description": "RSIAgent separates task verification, Actor-owned memory reconciliation and curriculum selection; source wiring supports reusable experience but reported gains do not isolate criticism-driven improvement.",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-24-rsiagent-01",
  "source-identity": "https://github.com/AetherLabsAI/RSIAgent",
  "reviewed-revision": "a9e56263f6deaa493496ad6b155fe24bf131bc12",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/result.md",
  "analysis-result-sha256": "0f1dd28fa8ffe6c2cc18b0b24c542a5c19e5e2934bea0685d0f4c93af8570482"
}
---

# RSIAgent: verified experience, Actor-owned memory and curriculum search

**Evidence basis:** source code and repository documentation at commit `a9e56263f6deaa493496ad6b155fe24bf131bc12`, inspected 2026-09-24. No live benchmark run was performed. [Exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/result.md).

RSIAgent is a computer-use runtime with an improvement loop around it. An Actor executes Python/Bash programs and requests visual observations. A separate Verifier investigates the candidate environment. A Curriculum chooses further practice from outcomes and the Actor's diagnosis. The same Actor that performed a task then distills and reconciles its durable memory. The implementation separates those roles instead of treating a task PASS as approval of every explanation or memory lesson (exact result RTE-1, RTE-3, RTE-4, RTE-8).

| Mode | What carries forward | Main control |
|---|---|---|
| Broad exploration | Actor memory after each completed wave | Parallel tasks start from shared memory; their Actors consolidate in order after the wave finishes |
| Deep exploration | Memory plus Curriculum context across target/practice cycles | PASS and FAIL can teach; default Curriculum review may request practice after PASS, requiring a fresh target attempt afterward |
| Frozen evaluation | The final host memory snapshot | No learning writeback or Curriculum; official evaluation follows agent execution |

These are wired paths, not observations of a successful run. The OSWorld and ALE adapters use the shared runtime but differ in failure behavior: failed frozen-memory upload can leave an OSWorld task running memory-OFF, while ALE evaluation raises. A stable host memory hash therefore does not establish successful guest attachment or use. [Phase-3 controls](https://github.com/AetherLabsAI/RSIAgent/blob/a9e56263f6deaa493496ad6b155fe24bf131bc12/benchmarks/osworld/pipeline.py), [task attachment](https://github.com/AetherLabsAI/RSIAgent/blob/a9e56263f6deaa493496ad6b155fe24bf131bc12/benchmarks/osworld/task.py).

## Memory and revision

The durable bank is an unconstrained Actor-owned directory. The harness supplies its filename/size inventory; the Actor chooses which file bodies to read. Curriculum may inspect a disposable copy but cannot write changes back. Host audits reject boundary violations and preserve byte history; they do not validate the truth of learned lessons. The reconciliation prompt explicitly asks the Actor to find conflicting assertions, unsupported causal explanations and overbroad conclusions, and to revise or remove them (OBJ-6, RTE-7, RTE-8, RTE-9, RTE-10). [Memory contracts](https://github.com/AetherLabsAI/RSIAgent/blob/a9e56263f6deaa493496ad6b155fe24bf131bc12/explore/charter.py).

Memory also includes continuation mechanisms. Target execution can produce retained WORK LOG summaries for later calls or fresh attempts. Verifier recovery transforms and retains its own action/result history, selecting a session by role/model identity. These qualify as trace-fed learning routes under the comparison contract even though they do not demonstrate improvement. The complete comparison includes both per-task continuation and cross-task bank reuse. It leaves aggregate content form, curation and behavioral force uncertain because no actual learned bank was available (OBJ-8, OBJ-9, RTE-11, RTE-12).

## Verification and improvement evidence

The configured target Verifier uses a rollback-protected guest view; failed rollback prevents safe grading. An alternate executor uses read-only candidate mounts and private namespaces. Actor-authored done checks and the legacy Verifier branch use different controls, so the isolation guarantee does not extend to every probe path. Remote service changes are outside guest rollback. Local task verdicts depend on model-chosen investigations; the official benchmark oracle remains outside the learning loop (RTE-2, RTE-3, RTE-5).

Curriculum is instructed to maintain hypotheses about Actor bottlenecks and change them when evidence contradicts them. Outcomes and retained diagnoses can alter later practice selection: this is a wired reflective route. Memory criticism and revision are supported procedures; actual formulated theories, their criticism and improvement attributable to that process remain uninspected. Reflection, automatic memory writing and improved capacity are separate findings.

The documentation reports higher aggregate partial-credit scores with RSI. It also states that the aggregates mix retained baseline scores with selected RSI runs/checkpoints and unmatched budgets or evaluation scopes. Those results support an attributed bundle-level improvement claim, not causal attribution to memory reconciliation or theory criticism (CLM-2). [Reporting scope](https://github.com/AetherLabsAI/RSIAgent/blob/a9e56263f6deaa493496ad6b155fe24bf131bc12/docs/PAPER.md).

## Scope

This review covers the shared runtime, learning/memory controls and principal OSWorld/ALE adapters. Provider weights, benchmark oracle implementations, VM internals, actual memory contents and live execution are excluded. Configured model names resolve through providers; the fixed-weight statement is a source claim, not an inspected immutable weight identity. Candidate-linked trajectories and memory snapshots, plus matched intervention comparisons, would be needed to establish recall faithfulness or criticism-driven improvement.

---

- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the two-way relation between represented Actor limitations and later practice selection.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the stronger claim requiring operative theory criticism and attributable improved capacity.
