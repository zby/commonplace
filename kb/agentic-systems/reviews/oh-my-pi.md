---
type: types/note.md
description: "oh-my-pi's coding runtime, alternate memory representations, and distinct rule-repair and experiment-admission mechanisms"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-oh-my-pi-01
source-identity: https://github.com/can1357/oh-my-pi
reviewed-revision: be6cb8217cd4c1dafcc86793ae5d809ea4d7396a
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-oh-my-pi-01/result.md
analysis-result-sha256: 74786c9df528b7060aa64405570829e1ce7ee8f0eb06b1ddad49c7878af71c3c
---

# oh-my-pi

**Evidence basis:** source code and shipped doctrine at commit `be6cb8217cd4c1dafcc86793ae5d809ea4d7396a` (2026-09-05; package version 18.1.10), analysed 2026-09-26. No runtime or causal experiment was executed. This is a whole-system runtime analysis with explicit limits, not current-tip coverage. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-26-oh-my-pi-01/result.md) retains the evidence, canonical records and bounded memory profile.

## Runtime and control

oh-my-pi encloses the coding loop: CLI/SDK entry, session and context assembly, model dispatch, tool execution, steering, task workers and retained state. The model proposes content and tool calls; symbolic code governs scheduling and continuation. Interactive, print and client-protocol modes share substantial session machinery. Tools return observations and effects into later turns; successful execution alone does not certify the resulting work. Exact records: RTE-1, RTE-3 and RTE-5.

The tool wrapper checks policy again after an extension revises arguments. Required approval without an interactive UI fails. Task workers, however, switch to unattended `yolo` mode while retaining explicit tool policies. Extensions also expose direct command execution. These are distinct control boundaries: a registered-tool approval check does not establish global process isolation. Optional worktree apply-back checks run status and Git applicability, with recovery artifacts on failure; neither check proves task correctness. Exact records: RTE-2, RTE-3 and RTE-4; [wrapper source](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/extensibility/extensions/wrapper.ts).

## Retained context and memory

Session continuity reconstructs a selected branch around checkpoints. Maintenance alternatives include prose summaries, handoff text, rasterized conversation archives, mechanical shrinking with recovery references, and opaque provider-native replacement history. A readable display summary therefore does not identify everything the model consumes. Exact records: OBJ-12, OBJ-13, RTE-15 and RTE-16.

Cross-session backends differ in authority and selection. Local rollout processing derives project summaries and lessons; detailed files can be requested. Mnemopi retains scoped facts/episodes with lexical/vector access and ranking metadata. Hindsight exposes remote recall/reflect and curated bank material whose internal algorithms remain opaque. Sharpshooter extracts friction-selected project decisions and supplies them as instructions. Local memory explicitly asks for verification against current repository evidence; decision-memory wording carries stronger instructional force. Exact records: RTE-17, RTE-18, RTE-19 and RTE-20.

Durable trace-derived material has wired later consumers, satisfying the analysis profile's `trace_learning` write/read-back criterion. That does not establish improved capacity. Representation, selection and transformation aggregates remain uncertain where included payloads or services are opaque. The profile explicitly excludes auxiliary saved-rule, managed-skill and experiment routes; the whole-system account covers them separately.

## Revision and warrant

The `/omfg` path turns a complaint into a stream rule, checks its matcher against assistant history, and feeds a failed candidate plus stated failure into another proposal. This wires all four [theory-builder conditions](../../notes/definitions/theory-builder.md) for **matcher-applicability repair**. Human adoption remains part of the broader save route. A match does not prove that the rule detected the complained-of error, that its corrective instructions work, or that future work improves. Exact records: RTE-8 and RTE-9; [controller source](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/modes/controllers/omfg-controller.ts).

Managed skills provide another instruction-revision path, with structural/path checks and authored-skill precedence. Autoresearch instead changes an external project: it runs a benchmark, records results, accepts an agent-supplied keep/discard decision, commits or reverts, and supplies notes/results to later rounds. A supplied metric differing from the parsed value produces a warning with both values retained. The machinery enforces repository consequences; it does not independently enforce improvement or correctness. Exact records: RTE-10, RTE-11, RTE-12, RTE-13 and RTE-14.

The source supports bounded reflection through prior assistant behavior, saved rules and later control, and a standing complaint-responsive self-change pathway. It supplies no observed learning gain or occurrent self-improvement. Benchmarking external product changes does not itself improve the harness.

## Scope

Provider weights, external service internals, actual deployment grants and candidate-linked runs were not inspected. Review/advisor judgments, checker results, retained summaries and successful application have different warrant. Evidence that would change the assessment includes a retained rule-repair/adoption/use trace, explicit experiment criticism shaping subsequent hypotheses, or controlled dependence on recalled material.
