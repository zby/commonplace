---
type: kb/types/note.md
description: "ContextPilot combines task-local memory and context editing with outcome-trained parameters; its control paths and recovery choices bound claims about autonomous context management."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-contextpilot-01
source-identity: https://github.com/Tencent/ContextPilot
reviewed-revision: 782cbb6611fb610c4cf6fafda6022b7e89cae191
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/result.md
analysis-result-sha256: 90d80a12cfa4d0aaf659617a3585228453563cad2a6f480d8357cfd86a5aaa43
---

# ContextPilot

Evidence basis: repository implementation, tests and documentation at [revision 782cbb66](https://github.com/Tencent/ContextPilot/tree/782cbb6611fb610c4cf6fafda6022b7e89cae191), frozen on 2026-09-25; no inference or training experiment was run.

ContextPilot is a long-context question-answering runtime with a separate training path. Its default evaluator creates a fresh agent for each question. A finite-state wrapper guides analysis, planning, indexing, search, reading, memory writing, cleanup, review and final answer submission. The model supplies choices and content within that sequence; the host also performs deterministic recovery actions. Repository-owned inference and the ContextPilot-specific training interfaces are included here. External model internals, data validity and unused vendored framework features are excluded.

The state machine filters offered tools and rejects returned actions outside the allowed set. That control has two material limits. A state with no matching configured tool falls back to the full catalog. The alternate base loop checks returned actions against all configured tools, rather than only those offered on that turn. Tool availability is therefore a property of the selected execution path and configuration.

Memory is external to the prompt but normally local to the task. Structured memories and simple notes retain content and short summaries. Every payload includes catalogs of available keys and summaries; model-requested reads return complete entries and related-entry summaries. Relations use deterministic overlap and optional embeddings. Their explanations describe why entries are linked, not why their claims should be believed. API-failure recovery can automatically load the last inserted entry, so successful review does not necessarily mean the model chose or assessed it.

Context editing changes the rendered view while retaining original history. Supplied summaries, exact-span truncation and remote compression can replace selected messages on later calls. Compression failure falls back to random word sampling. Restoration exists as a callable method but is absent from the default tool catalog; token-window deletion also does not grant the same restoration eligibility as ordinary edit tools. The token-window pass can exhaust eligible turns and return an oversized payload. These are bounded implementation branches, not evidence that every run loses needed facts.

The training path captures pre-action state, selects branches by context-length and uncertainty signals, and samples alternative continuations. Descendant terminal rewards become intermediate snapshot means; query-relative advantages feed actor parameter updates. This is a wired learning mechanism with persistent checkpoint output. It does not independently establish causal credit for each intermediate statement or editing action. Training-loop activation also depends on dataset `agent_name` or configuration: the generic fallback is `single_turn_agent`, and the external transformed dataset was not inspected.

Answer scoring uses supplied benchmark references and, for open-ended training answers, a configured model judge with exact-match fallback on failure. Those criteria govern rewards, not factual acceptance of every note or plan. Actor updates have a numerical-gradient veto; scheduled validation and checkpoint saving do not establish a demonstrated improvement-before-admission gate. Default checkpoints omit optimizer state, limiting exact continuation claims.

The strongest supported contribution is connected task-context reuse plus a conditional, outcome-driven parameter-learning path. Reported performance gains remain claims at this evidence boundary. Reflection is wired through representations of current history, memory and context usage that mediate later behavior. Dispositional self-improvement is wired for the configured training arrangement; actual update-dependent operation and favorable improvement are unobserved. Theory-bearing plans and notes are possible, but content-directed criticism of an operative theory and capacity improvement attributable to it remain uninspected.

The exact result preserves these route distinctions and the normalized memory profile. Recalled-content faithfulness and the complete controlled classification of branch-selection signals remain explicitly uncertain. Task-linked original/edited context, exact weights and matched interventions would resolve more than aggregate benchmark scores alone.

---

- [Inference state machine](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot_fsm.py) — evidenced-by: tool admission and deterministic recovery.
- [Context and memory implementation](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot.py) — evidenced-by: stores, payload edits and alternate base loop.
- [Training branch coordination](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/experimental/agent_loop/agent_loop.py) — evidenced-by: selection, subtree reward and conditional agent-loop dispatch.
- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/result.md) — see-also: source records, memory profile and epistemic ledger.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: criticism and improved capacity remain separate claims.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: self-representation mediates later behavior.
- [Self-improving system](../../notes/definitions/self-improving-system.md) — defined-in: disposition, occurrence and favorable outcome have distinct evidence requirements.
