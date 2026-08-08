# Pi Subprocess Subagents Expose an Approval-Routing Choice

## Status

This is baseline evidence for the agent-runtime workshop, not a design decision. It records how one small, widely used runtime wires subagents, tool selection, and approval at a pinned revision. It then extracts questions that a future review skill should ask of other runtimes, including systems that call themselves harnesses.

The inspected repository is `badlogic/pi-mono` at commit `fc3554e16defffcf76553b1bd12f676adf26d0a4`, committed on 2026-08-06. The relevant subagent implementation is shipped as an extension example rather than as a protected primitive of the agent core.

## Observed Pi wiring

Pi's example discovers named agent definitions from Markdown files. An agent definition may declare a model, system prompt, and comma-separated tool names. The subagent extension starts a separate Pi process for each invocation. It passes the declared tools through `--tools`, uses JSON print mode, disables session persistence, ignores child stdin, and reads structured events from child stdout.

This gives each child:

- a separate process and model context;
- a configured model and system prompt;
- a tool-name allowlist when the definition declares one;
- independent output, usage accounting, cancellation, and exit status.

The tool-name allowlist is stronger than prompt-only tool hiding. `createAgentSession()` retains the supplied names as an allowlist. `AgentSession` filters built-in, custom, and dynamically registered tools against it when rebuilding the registry. An extension cannot use `setActiveTools()` to expose a registered tool whose name was excluded from the child's allowlist.

The allowlist is not yet a complete capability grant. Built-in path tools accept absolute paths, so `cwd` is a resolution base rather than an authority boundary. The Bash tool starts a local shell and normally exposes the process environment. Extension code is ordinary host-privileged JavaScript or TypeScript. A list such as `read, grep, bash` therefore constrains Pi tool dispatch without necessarily constraining all effects available through those tools or through loaded extension code.

## Approval does not cross the subprocess boundary

The example has no protocol for a child tool call to request a decision from the parent UI. Child stdin is ignored. Stdout is consumed as a one-way JSON event stream. The parent does not send approval responses back to a pending child invocation.

The extension does contain a parent-side confirmation, but it answers a different question. When project-local agent definitions are enabled, the parent can ask whether to run a repository-controlled agent definition. That decision occurs before the child starts. It does not approve or deny later tool calls made inside the child.

Pi also ships a permission-gate example. It asks through the local extension UI when a dangerous Bash command is encountered. Without a UI, it blocks the command. A subprocess started by the subagent example is headless, so this kind of extension cannot forward its unresolved decision to the parent. It must either resolve the call from preconfigured policy or fail closed.

The current wiring therefore distinguishes three things that a review must not collapse:

1. approving the use of a subagent definition;
2. selecting the child's visible and dispatchable tools;
3. approving a concrete effect attempted during child execution.

Pi implements the first two in its example. It does not connect the third to the parent UI.

## Two interpretations to preserve

The missing approval channel can be interpreted as a limitation. A child may discover that it needs authority not known when it was launched. Without escalation or suspension, it must fail, improvise within its existing authority, or be restarted under a different configuration. Work may be lost, and a runtime cannot support a claim that any nested invocation can wait for live human approval.

It can also be interpreted as a useful simplification. Direct approval requests from many concurrent children could overload the user, hide which request belongs to the main task, and let internal decomposition determine the volume and timing of interruptions. A runtime may instead require children to run headlessly under authority assigned at delegation time. An unresolvable need could return to the parent as an ordinary structured result. The parent could replan, perform the operation itself, or decide whether the user needs to see one broader request.

These interpretations imply different runtime contracts, but this workshop does not choose between them yet. In particular, the Pi example does not provide a structured `needs-capability` result, a resumable child checkpoint, or an attenuated grant type. Those are possible designs suggested by the case, not observed Pi behavior.

## Baseline comparison questions

A review of an agent runtime should establish:

- Which principals can cause an approval prompt: only a root run, any worker, a policy service, or none?
- If a child needs unresolved authority, does it prompt directly, route through its parent, suspend, fail closed, return an escalation result, or silently continue through another channel?
- Is child authority fixed before launch, derived per effect, or expandable during execution?
- Does a parent approval cover one invocation, one task, a delegation subtree, or a persistent policy scope?
- Can a parent pass only an attenuated subset of its own grant, and is that enforced across every effect channel?
- Does the child receive a tool-name surface, scoped capability handles, an isolated execution environment, or some combination?
- Is the approval transport bidirectional and correlated with stable request identities?
- Can a pending child and its continuation survive UI disconnect, parent restart, or child process loss?
- How are concurrent child requests aggregated, ordered, suppressed, or presented so that operator attention remains bounded?
- What happens to completed child work when a later effect is denied or requires broader authority?
- Does the shipped UI exercise the claimed mechanism, or does the runtime merely expose hooks from which an integrator could build it?

The operator-attention question belongs beside authority and durability in a comparison. A system that can route every nested request to the user is not necessarily better than one that deliberately prevents nested prompts. The review should describe the actual routing and its consequences before judging which work stories it supports.

## Code-grounded evidence

- [Subagent extension README](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/examples/extensions/subagent/README.md) — separate processes, agent definitions, project-agent confirmation, and documented limitations.
- [Subagent launcher](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/examples/extensions/subagent/index.ts#L267-L429) — JSON-mode arguments, `--tools`, ignored stdin, streamed stdout, cancellation, and cleanup.
- [Agent discovery](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/examples/extensions/subagent/agents.ts#L11-L74) — model, prompt, source, and tool-name fields.
- [SDK tool selection](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/src/core/sdk.ts#L54-L73) — documented tool allowlist and denylist.
- [AgentSession registry filtering](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/src/core/agent-session.ts#L2463-L2554) — enforcement of allowed and excluded tool names across built-in and extension tools.
- [Permission-gate extension](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/examples/extensions/permission-gate.ts#L13-L33) — local UI approval and fail-closed behavior when no UI exists.
- [Path resolution](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/src/core/tools/path-utils.ts#L44-L50) and [local Bash execution](https://github.com/badlogic/pi-mono/blob/fc3554e16defffcf76553b1bd12f676adf26d0a4/packages/coding-agent/src/core/tools/bash.ts#L87-L108) — evidence that tool-name restriction and effect confinement are different properties.
