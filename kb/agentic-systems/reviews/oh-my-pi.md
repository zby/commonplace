---
type: kb/types/note.md
description: "oh-my-pi's coding runtime, optional trace-derived memory, delegated sessions, and the limits of its schema, edit, advisor and experiment checks."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-05-oh-my-pi-01
source-identity: https://github.com/can1357/oh-my-pi
reviewed-revision: be6cb8217cd4c1dafcc86793ae5d809ea4d7396a
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-01/result.md
analysis-result-sha256: f088fbd407c7a8a9a964d88035e472adc7e23c419522b47c9e7903b877f1b0b7
---

# oh-my-pi

Evidence basis: source code and shipped documentation inspected on 2026-09-05 at [`be6cb8217cd4c1dafcc86793ae5d809ea4d7396a`](https://github.com/can1357/oh-my-pi/tree/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a); no target execution or causal experiment.

Oh-my-pi is an enclosing coding runtime. Its CLI, editor/protocol clients and SDK wrap a common session and model/tool loop. It assembles project instructions, tools and optional memory; delegates work to separately configured sessions; and retains selected context for later work. Its checks have distinct scopes: output shape, edit applicability, execution permission, analyzer feedback, model judgment and experiment disposition. Their outcomes do not provide one common correctness guarantee.

## Runtime and delegated work

The SDK resolves configuration, model credentials, session identity and context. The loop transforms messages at the provider boundary, streams a response, validates tool arguments, executes permitted calls and returns results to the next model turn. Session reconstruction follows branch ancestry, compaction and reset boundaries; a persisted conversation is not a transaction over external effects. ([Session construction](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/sdk.ts#L1435-L1498), [model boundary](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/agent/src/agent-loop.ts#L1593-L1639), [history reconstruction](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/session/session-context.ts#L410-L499).)

Workers have their own sessions, prompts and tool surfaces, while selected credentials, memory resources and artifacts can be shared. The inspected executor constructs sessions directly despite its name `runSubprocess`. Checkout isolation is optional and defaults off. When enabled, successful changes can be captured as patches or branches and applied; conflicts have explicit recovery paths. Worker output schemas are real controls, but strictness, overrides, unusable schemas and prose fallback qualify the README's broad typed-result promise. Ordinary valid-schema mismatches reject even in permissive mode. ([Worker construction](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/task/executor.ts#L3318-L3437), [isolation default](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/config/settings-schema.ts#L4852-L4859), [output admission](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/task/executor.ts#L668-L812).)

Tool approval defaults to `yolo`. The wrapper still applies explicit policies and resolves approval against revised execution arguments. Required approval without UI fails the call; pending provider safety checks have stronger handling. These are controls over wrapped dispatch, not evidence of OS containment. ([Default](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/config/settings-schema.ts#L4100-L4123), [wrapper](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/extensibility/extensions/wrapper.ts#L180-L345).)

## Memory and later context

Memory backends and Auto-Learn are separately disabled by default. Enabled local memory extracts prior persisted sessions, consolidates them into project summaries and optional procedure bundles, and supplies bounded guidance to later prompts. Explicit lessons share the summary's injection budget and a per-session cache: a durable new lesson need not enter the current prompt. Local guidance explicitly asks the model to verify remembered material against current repository evidence. ([Settings](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/config/settings-schema.ts#L2987-L3054), [cache and budget](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/memories/index.ts#L210-L293), [memory instructions](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/prompts/memories/read-path.md#L1-L17).)

Auto-Learn can run a private capture model over a completed trajectory and write reusable managed skills. Their discovery continues after capture is disabled; loaded procedures carry instruction authority. Alternative Mnemopi/Hindsight adapters share selected parent memory with workers, while Sharpshooter injects prior project decisions as instructions unless the user overrides them. Sharpshooter's literal-quote check proves occurrence, not that the quote warrants the decision. ([Capture](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/autolearn/controller.ts#L73-L150), [continued discovery](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/discovery/builtin.ts#L309-L336), [decision framing](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/sharpshooter/backend.ts#L78-L125), [admission](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/sharpshooter/extract.ts#L252-L310).)

These are wired retention, distillation and read-back routes. No inspected execution establishes faithful recall, appropriate procedure selection or improved behavior. The exact result's comparison fields cover session/local memory and managed skills, with alternative backends explicitly outside that normalized scope.

## Checks and their authority

Hashline can reject unrecoverable stale anchors, recover compatible edits, or allow head/tail drift with a warning. It checks applicability, not program correctness. LSP diagnostics arrive after writes. Reviewer verdicts and advisor notes are model judgments; advisor blockers can enforce interruption while their content remains advice for the primary model to weigh. ([Hashline](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/crates/pi-edit/src/modes/hashline/patcher.rs#L185-L250), [LSP ordering](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/lsp/writethrough.ts#L347-L472), [advisor delivery](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/session/session-advisors.ts#L1220-L1290).)

Autoresearch connects harness measurements, model-supplied keep/discard decisions, Git effects, retained records and later iterations. The logger can keep experiments with supplied-versus-parsed metric discrepancies or scope deviations recorded as warnings. Its operational selection is wired; faithful improvement and correctness judgments remain partly model policy. ([Disposition and records](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/autoresearch/tools/log-experiment.ts#L124-L217).)

## Scope

For long coding work, session reconstruction and optional memory explain how selected context survives. For delegated edits, isolation and recovery explain integration under configuration-dependent limits. For review and optimization, findings and measurements can change execution without independently certifying their interpretation.

This analysis selectively traces the whole runtime's material routes. It excludes deployed configuration, provider and remote-memory internals, exhaustive tool/platform coverage, and benchmark validation. Candidate-linked executions, recall interventions and declared deployment forcing tests would be needed to establish activation, reliability or causal gains.

---

- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-01/result.md) — see-also: canonical records, both lenses, full anchors, normalized memory scope and limitations
