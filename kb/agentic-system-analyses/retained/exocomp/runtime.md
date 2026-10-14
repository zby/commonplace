---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Exocomp runtime baseline: planner inference, contractor processes, tool effects, operator routes and change admission at the frozen source revision."
run-id: AAS-2026-10-14-exocomp-692bb27c35f9-01
reviewed-boundary: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
---

# Exocomp runtime report

## Runtime account

### Work and evidence basis

Exocomp supplies an enclosing software-work runtime. A planner interprets an operator request, hires role-specific agents, reads project records, and asks for work reports. Contractors can write project files and execute installed programs according to their role's grants. The planner prompt specifies clarification, planning, specification, coding, testing and refinement; these are model instructions, not a coded phase machine. The prompt even calls the timeline three phases before listing six. Implementation supports delegation and tool effects, not reliable adherence to those phases or correct finished software. See [RT-CLM-role-separation](#rt-clm-role-separation), [RT-RTE-planner-chat](#rt-rte-planner-chat) and [RT-RTE-contractor-work](#rt-rte-contractor-work). SRC-1: `source/agents/planner.yaml`, `source/engine/Session.go`, `source/tools/Agents.go`.

All findings below are implementation or doctrine/design findings at the boundary's frozen commit. No target commands, tests, providers or services were executed. The boundary registers historical session artifacts, but this report does not use them to establish current-revision operation. Activation, role compliance, successful execution and benefit remain unobserved. Source availability is not execution evidence.

Additional inspected coverage under SRC-1 includes `source/tools/Toolset.go`, `source/tools/Programs.go`, `source/tools/Files.go`, `source/tools/Skills.go`, `source/tools/resolveSandboxPath.go`, `source/tools/sanitizeSandboxPath.go`, `source/tools/getAgentWorkReport.go`, `source/tools/Requirements.go`, `source/utils/ast/HasSymbol.go`, `source/adapters/DeepSeek.go`, `source/types/Config.go`, `source/ui/web/routes/session/CallTool.go`, `source/ui/web/routes/session/SendChatRequest.go`, `source/agents/coder.yaml`, and `toolchain/utils/Build.go`. Correction inspection additionally covers `source/tools/Humans.go`, `source/tools/writeRequirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/schemas/ToolCall.go` and `source/types/Command.go`. These add implementation evidence within the already registered repository, not new sources.

### Shipped invocation and ordinary loop

The main `exocomp` command dispatches config, agent, terminal/tty/term, web and webview modes. `exocomp-agent` ships agent and terminal modes; `exocomp-web` ships agent, config and web modes. `agimus connect` restores an existing `.exocomp` project into a new debug sandbox and opens an assistant-role terminal through `actions.Debug`. Webview starts the same web server with a native client rather than a different inference engine. SRC-1: `source/cmds/exocomp/main.go`, `source/cmds/exocomp-agent/main.go`, `source/cmds/exocomp-web/main.go`, `source/cmds/agimus/main.go`, `source/actions/Debug.go`, `source/actions/Webview.go`.

An ordinary fresh invocation is `exocomp terminal` in planner mode, followed by an operator's project request. CLI configuration and the embedded planner template determine agent name, role, model, temperature, system prompt and grants. A terminal client constructs a Session and installs the role-filtered toolset and provider adapter. The user request becomes a message. Session sends an OpenAI-compatible, non-streaming chat-completions request with accumulated messages, tool schemas and automatic tool choice. A provider-selected model chooses prose or tool calls. DeepSeek adaptation rewrites function-name dots to underscores for requests and reverses that encoding in responses; it does not supply an independent evaluator. SRC-1: `source/agents/NewAgent.go`, `source/ui/tty/Client.go`, `source/engine/Session.go`, `source/adapters/DeepSeek.go`.

Session takes the first response choice, appends its assistant message, executes parsed tool calls sequentially, appends tool results and requests another completion. A response without tool calls ends this inference chain, returning control to the client; this is not necessarily project completion. The loop has no inspected bound on tool-call rounds. The terminal renders messages and exits on a reported chat error. Session's `Waiting` check is a busy-state control for chat requests, not a universal transaction lock: initialization and direct tool routes do not use that gate, and the read/check and write/set are separate critical sections. SRC-1: `source/engine/Session.go`, `source/ui/tty/Client.go`. Decision roles, operating mode and oracle limits are in [RT-RTE-planner-chat](#rt-rte-planner-chat).

When the planner calls Hire, a distinct child process and conversation receive the selected task prompt, role and sandbox. The child chooses its own role-default model because Hire's executable arguments do not pass a model override. The parent-side bookkeeping Agent is constructed with `tool.Model`; it must not be treated as proof of the child model's identity. Await blocks on that child's completion channel, extracts its Quit work report and returns that report to the planner's next inference. The parent tool stores child messages from stdout for inspection, but the planner does not automatically receive the entire child conversation. Shared filesystem effects are not rolled back when the child finishes or is fired. See [RT-RTE-contractor-work](#rt-rte-contractor-work). SRC-1: `source/tools/Agents.go`, `source/agents/NewAgent.go`, `source/tools/getAgentWorkReport.go`.

### Effect boundaries and forcing routes

Three forcing cases test the strongest doctrine against material alternate paths:

1. **No Files.Write grant does not mean no code-writing capability.** The planner has `programs.Execute` and `go`; Programs admits an allowed executable name and sanitizes path-looking arguments, but starts an ordinary host process. `go run` can execute project code whose internal file and network operations do not pass through Files or Session. Role separation therefore combines an enforced tool-method filter with much weaker prompt-level task restrictions. This is a source-supported capability counterexample, not a demonstrated escape. See [RT-RTE-program-execution](#rt-rte-program-execution) and [RT-CLM-role-separation](#rt-clm-role-separation). SRC-1: `source/agents/planner.yaml`, `source/tools/Programs.go`.
2. **Tool effects need not be proposed by the model.** Terminal slash commands and HTTP POST `/api/session/calltool` call Session.CallTool directly. They retain the installed-tool and tool-specific HasMethod check (including Humans.Answer's exception to literal method-array membership) but bypass model selection and the chat busy-state gate. The browser has its own Waiting flag, which is client cooperation, not server-wide enforcement. The web listener uses `:3000` rather than a loopback-only listen address; the inspected route registration and handler add no caller-authentication gate. Host networking controls and exposure are unknown. See [RT-RTE-client-tools](#rt-rte-client-tools). SRC-1: `source/ui/tty/Client.go`, `source/ui/web/Server.go`, `source/ui/web/routes/session/CallTool.go`, `app/engine/Session.go`.
3. **Skills have a two-stage admission path and are not current role grants.** The Skills tool checks required programs and methods before marking a skill loaded. Ordinary model, terminal and HTTP calls pass qualified names such as `skills.Load`, so Session's bare-name `skills` branch does not insert the body; generic tool notices reach the conversation instead. System-message insertion is a separate helper/bare-name API capacity. Skill execution checks a loaded script and allowed runtime, then executes Go code as a host process. This extends instructional content and script selection, not the role's grant arrays. Session.LoadSkill alone computes missing programs but only gates missing tools; Skills.Load enforces both before changing loaded state. Direct helper use is thus a weaker alternate admission path. An embedding calling Session.CallTool with bare name `skills` can invoke both the tool check and the helper; the shipped parsers instead supply qualified names. No embedded role grants a skills method in the inspected YAML set. See [RT-RTE-skill-loading](#rt-rte-skill-loading) and [RT-ABS-skill-grants](#rt-abs-skill-grants). SRC-1: `source/tools/Skills.go`, `source/engine/Session.go`, `source/tools/readSkills.go`, `source/agents/`.

The selected effect paths cover central model calls, host callbacks, direct operator tools, contractor subprocesses, filesystem writes and extension scripts. Inference payloads advertise function schemas, not a separate provider-native execution channel; provider internal tools or retention remain uninspected. No remote-worker isolation or deployed container policy is established. Filesystem helper checks are lexical path checks: they compare relative paths but do not resolve symlinks. This limits confinement even for file-helper paths; process-internal operations have the broader host-process boundary. SRC-1: `source/engine/Session.go`, `source/tools/resolveSandboxPath.go`, `source/tools/sanitizeSandboxPath.go`, `source/tools/Programs.go`.

### Guarantees and their actual owners

| Claimed or load-bearing rule | Owner and enforcement point | Strength and covered paths | Required external contract and limit | Separate conclusion statuses |
|---|---|---|---|---|
| Session dispatch requires an installed tool and its HasMethod approval | Runtime toolset construction, Session.GetTool/CallTool and tool-specific HasMethod | invariant relative to the installed tool map and predicates, not literal role-array membership; covers returned model calls, terminal commands and web CallTool. Humans.HasMethod admits Answer even without an Answer entry | Client/embedding code must install the intended map; public SetTool can replace it. Does not govern subprocess-internal operations or guarantee downstream answer delivery. Evidence: [RT-OBJ-role-grants](#rt-obj-role-grants), [RT-RTE-client-tools](#rt-rte-client-tools). | implementation conclusion status: wired; operation conclusion status: uninspected |
| Role-specific work and correctness | Role prompt interpreted by the model | policy; prompts say planner must orchestrate and coder must verify, but allowed Go execution is broader than those instructions | Model compliance and correct external tests are required; no general approval gate accompanies Files.Write or Programs.Execute. Evidence: [RT-CLM-role-separation](#rt-clm-role-separation), [RT-RTE-file-admission](#rt-rte-file-admission). | doctrine conclusion status: claimed; operation conclusion status: uninspected |
| Work occurs in a sandbox folder | Runtime path helpers and process working directory | best effort; lexical traversal checks cover file-tool and selected argument paths; subprocess directory is not OS isolation | Requires trust in permitted code, symlink layout and host permissions. No deployed isolation envelope was supplied. Evidence: [RT-RTE-program-execution](#rt-rte-program-execution), [RT-RTE-file-admission](#rt-rte-file-admission). | implementation conclusion status: wired; confinement conclusion status: uninspected |
| Await postpones next inference until child terminates | Agents tool, process.done channel and sequential response handling | protocol; Await blocks only when that named process is still registered | Child must emit a usable Quit record; finished/report presence does not validate work. Evidence: [RT-RTE-contractor-work](#rt-rte-contractor-work). | implementation conclusion status: wired; operation conclusion status: uninspected |
| Long-running programs and agents can be cancelled | Programs timeout/output buffer; Agents timeout and liveness watchdog | best effort; direct children have timeout/cancellation wiring | OS process termination and descendant behavior remain external; no evidence that all descendant work is stopped. Evidence: [RT-RTE-program-execution](#rt-rte-program-execution), [RT-RTE-contractor-work](#rt-rte-contractor-work). | implementation conclusion status: wired; operation conclusion status: uninspected |

### Persistence, recovery and change admission

Planner response handling and destruction call Recovery.BackupSession; it writes session JSON and agent JSON, including contractor records reachable through the Agents tool. Constructors reload a backup and recovered agents. RestoreSession creates new HTTP/mutex/tool infrastructure and relocates playground/sandbox paths; it does not revive child processes. Await on restored metadata therefore reads a recorded report rather than waiting on the original process. Backup return values are not checked in the inspected response-handler calls, so a successful chat return is not a persistence-success guarantee. Ordinary file writes are direct overwrites, not atomic multi-file commits. SRC-1: `source/engine/Session.go`, `source/engine/Recovery.go`, `source/ui/tty/Client.go`, `source/ui/web/Server.go`, `source/tools/Agents.go`.

Working-context controls inspected here are distinct child conversations, separate helper/bare-name API capacity for skill system-message insertion/removal, and the afforded Inquire summarizer route. The ordinary qualified Skills.Load/Unload chain changes loaded objects and appends tool notices, not system-message bodies. Inquire converts only child user/assistant prose to single-line text, omits system/tool messages and tool-call structure, and asks a separate summarizer process to condense it. It returns the final emitted message's Content, not a checked complete work record. It does not replace the source child conversation. The shipped role YAMLs do not grant Inquire, so this is not an established default planner route. See [RT-RTE-agent-inquire](#rt-rte-agent-inquire). SRC-1: `source/tools/Agents.go`, `source/utils/chat/SummarizeMessages.go`, `source/agents/`.

Normal inference passes Agent.Messages wholesale before adapter transformation. Session.UnloadSkill removes the matching skill body while preserving other system and non-system messages; qualified Skills.Unload calls do not reach this helper, so loaded-state removal alone does not remove previously injected instructions. A token counter measures usage but does not in this inspected loop trim or summarize the conversation. The child context resembles a separate frame only for message selection: task input and report cross its boundary, while shared files outlive it and the parent retains a transcript object. Neither transcript storage nor report presence establishes improved future capacity. SRC-1: `source/engine/Session.go`, `source/tools/Agents.go`.

Product changes enter immediately through granted file methods or permitted program execution. Requirements.Signoff marks an in-memory entry implemented after a Go AST symbol-presence check, not a behavior or test oracle. The writer serializes only unimplemented entries; later reads reconstruct implemented entries from source with empty Behavior, rather than recovering a durable signoff decision or the original specification. The planner prompt requests human confirmation of the implementation plan, but the inspected write and execution methods do not enforce per-content confirmation. These are separate admission decisions: an operator starting the workflow is not an approver of each resulting write. See [RT-RTE-file-admission](#rt-rte-file-admission) and [RT-RTE-requirement-signoff](#rt-rte-requirement-signoff). Retained record transformations are left to the memory analyst rather than treating all persistence as one revision mechanism.

Build and installer drivers admit executable changes through Go compilation and copying embedded assets to a selected prefix. This is an operator-driven production path, not a demonstrated model-driven self-update loop. EXOCOMP_AGENT can substitute the contractor executable at launch, adding an external trust boundary. Build/installation success and binary provenance are not established. See [RT-RTE-build-install](#rt-rte-build-install). No learning, reflection, autonomous theory-building or exercised self-improvement conclusion follows merely from these paths.

## Shared records

### Components

#### RT-CMP-planner-model
Label: Planner model

Source-native identity: the planner template's `deepseek-v4-pro:cloud`, subject to CLI/configuration override and provider alias resolution. Representational form: distributed-parametric model; request prompts are natural-language inputs, not its parameter substrate. Storage substrate: external inference service's model storage, uninspected. Parameters are not updated by the inspected Exocomp request path; provider-side parameter changes are uninspected. Exact model version is not pinned by a weight digest or immutable endpoint identity. A mutable service/alias can resolve to another model. SRC-1: `source/agents/planner.yaml`, `source/agents/NewAgent.go`, `source/types/Config.go`, `source/engine/Session.go`.

> model: deepseek-v4-pro:cloud
> --- `source/agents/planner.yaml`

> if provider.Alias != "" {
> return provider.Alias
> } else {
> return model
> }
> --- `source/types/Config.go`

#### RT-CMP-coder-model
Label: Coder model

Source-native identity: the coder template's `huihui_ai/Qwen3.6-abliterated:35b`, subject to the child configuration/provider resolution. Representational form: distributed-parametric. Storage substrate: external service model storage, uninspected. No parameter update is sent by the inspected Session route; provider-side mutation is unknown. The name is not an exact weights/version pin, and a mutable endpoint can change its resolution. Hire omits a model flag, so the child's default need not match the parent's bookkeeping model. Other roles can select other defaults; no inference about their weights follows from this coder example. SRC-1: `source/agents/coder.yaml`, `source/agents/NewAgent.go`, `source/tools/Agents.go`, `source/types/Config.go`.

> model: huihui_ai/Qwen3.6-abliterated:35b
> --- `source/agents/coder.yaml`

#### RT-CMP-summarizer-model
Label: Inquire summarizer model

Source-native identity: the model passed as tool.Model to the summarizer child by Agents.Inquire, rather than necessarily the summarizer role's default. Representational form: distributed-parametric. Storage substrate: external inference service model storage, uninspected. Exocomp sends inference requests, not parameter updates; provider-side mutation remains unknown. No exact weight version is pinned and mutable provider/alias resolution can select another model. This is a separate decision invocation over filtered child prose, not the coder's foreground decision step. SRC-1: `source/tools/Agents.go`, `source/agents/NewAgent.go`, `source/types/Config.go`.

> fmt.Sprintf("--role=\"%s\"", "summarizer"),
> fmt.Sprintf("--model=\"%s\"", tool.Model),
> --- `source/tools/Agents.go`

### Operative objects

#### RT-OBJ-role-grants
Label: Role grants

Source-native identity: Agent.AllowedTools and Agent.AllowedPrograms copied from embedded role templates; the operative installed map is built by Toolset. Admission also depends on each installed tool's HasMethod predicate. Representational form: symbolic arrays and method maps consumed by tool-specific admission predicates. Literal membership is not universal: Humans.HasMethod accepts Answer outside its Methods array when the Humans tool is installed. This qualifies capability admission independently of successful answer delivery; see [EPI-RTE-human-answers](epistemic.md#epi-rte-human-answers). Storage substrate: shipped YAML embedded in the program and in-memory Agent/tool objects; Agent values can also be serialized in recovery JSON. This record concerns capability admission, not the memory account of the whole recovered Agent. Role prompt bodies have a different consumer and are covered by [RT-BAP-role-prompt](#rt-bap-role-prompt). SRC-1: `source/agents/NewAgent.go`, `source/tools/Toolset.go`, `source/engine/Recovery.go`, `source/tools/Humans.go`.

> AllowedPrograms: template.AllowedPrograms,
> AllowedTools:    template.AllowedTools,
> --- `source/agents/NewAgent.go`

> case "programs":
> tool = NewPrograms(allowed_methods, playground, sandbox, allowed_programs)
> --- `source/tools/Toolset.go`

> // NOTE: Special case, required for UI/UX integration
> if method == "Answer" {
> return true
> --- `source/tools/Humans.go`

### Routes

#### RT-RTE-planner-chat
Label: Planner chat

Operator/CLI message → Session → configured inference service → assistant message → granted tools → next inference, or client return. Owner of progression is Session code; the model proposes the next tool calls, subject to installed tools and their HasMethod predicates, not universally literal grant membership. Policies combine natural-language role instructions and symbolic dispatch. Open operator requests are the operating mode; there is no curriculum or candidate-selection experiment in this route. No expected answer/reference outcome is supplied by Session. External tests invoked through tools can produce evidence, but that is not an independent answer oracle in the inference loop. Human task authorship and downstream approval requests are distinct from per-tool veto.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A tool-free response ends the chain; client receives rendered/serialized assistant and tool messages or an error. Tool calls cause another completion before chat return.
- Later read-back: Planner session backup can restore accumulated messages on later startup; debug request/response snapshots are separate diagnostics, not automatically fed back here.
- Delegated visibility: Child work is delivered through requested Agents tools; the parent request does not automatically contain every child message.
- Selection predicate: Configured model/alias and first response choice; valid tool-call parsing, installed-tool lookup and tool-specific HasMethod approval govern dispatch, including Humans.Answer's special admission.
- Invalidation or expiry: No conversation expiry is imposed by this request method; restore uses current backup contents. HTTP/status/parse failures return errors.
- Activation or effect: Implemented calls can perform host effects and append tool messages; actual model compliance and successful effects were not observed.
- Evidence limits: No execution trace for this revision; provider internals and any provider-side context retention are uninspected.

SRC-1: `source/engine/Session.go`, `source/ui/tty/Client.go`, `source/adapters/DeepSeek.go`. Model mutability: [RT-CMP-planner-model](#rt-cmp-planner-model).

> Messages:    session.Agent.Messages,
> Stream:      false,
> Tools:       session.GetToolSchemas(),
> ToolChoice:  "auto",
> --- `source/engine/Session.go`

> if len(chat_response.Choices) > 0 {
> return session.ReceiveChatResponse(chat_response.Choices[0].Message)
> } else {
> return fmt.Errorf("Empty choices, maybe incompatible API?")
> }
> --- `source/engine/Session.go`

#### RT-RTE-contractor-work
Label: Contractor work

Planner Hire → Agents tool → child agent-mode process → child Session/tools → stdout records → Await work report. Agents owns process startup, stdout collection, termination bookkeeping and completion signaling; the child model owns proposed work steps. The coder is the concrete inspected example, using [RT-CMP-coder-model](#rt-cmp-coder-model). Inputs are a natural-language task, role and symbolic directory/URL arguments. The parent does not pass its full conversation or grant arrays. Child role templates determine grants. Distinct contexts isolate message accumulation, not filesystem or OS authority.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hire returns a generated name/task notice after process start; Await blocks on process.done then returns the extracted Quit work report or an error.
- Later read-back: Parent recovery can serialize child Agent messages/status and reload them; it does not recreate a running process handle.
- Delegated visibility: Parent tool collects child stdout messages and token-usage updates; planner receives requested report/list results, and shared project file effects are visible independently.
- Selection predicate: Role and task are planner-selected; sandbox resolves relative to the parent's sandbox; executable defaults to os.Executable with EXOCOMP_AGENT override.
- Invalidation or expiry: Context timeout defaults to 30 minutes; liveness watchdog can cancel stale output; Fire cancels a registered child. Files already changed persist.
- Activation or effect: Child can operate its granted tools; parent next inference after Await sees the report. No child success or behavioral compliance was observed.
- Evidence limits: Process exit status is not used as the report-validity criterion in read_process; presence of a Quit work report sets finished status. Report truth, completion and descendant termination remain unverified.

Decision roles: planner proposes task/role, Agents resolves and launches, child proposes effects, installed tools and their HasMethod predicates admit them. Operating mode: open delegated task. No answer oracle validates the work report. Capability admission is role-template/toolset construction; host operator can replace EXOCOMP_AGENT, while Fire is a runtime cancellation tool. Guidance comes from parent task plus child role prompt; report/transcript and project effects can persist. Recovery of metadata does not roll back product effects. SRC-1: `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`, `source/agents/coder.yaml`, `source/ui/jsonl/Client.go`.

> if os.Getenv("EXOCOMP_AGENT") != "" {
> exe = os.Getenv("EXOCOMP_AGENT")
> }
> --- `source/tools/Agents.go:514-516`

> if running == true {
> <-process.done
> }
> --- `source/tools/Agents.go`

> if getAgentWorkReport(agent) != "" {
> agent.FinishedAt = schemas.NewDatetime()
> agent.Status = "finished"
> } else {
> agent.FinishedAt = schemas.NewDatetime()
> agent.Status = "failed"
> }
> --- `source/tools/Agents.go`

#### RT-RTE-agent-inquire
Label: Agent inquire

Selected child Agent messages → deterministic text projection → fresh summarizer process → final stdout message Content → calling tool context. Agents owns projection/process invocation; the summarizer model performs natural-language condensation under a role prompt requesting factual compression. Projection keeps user/assistant Content in single-line form and omits tools, system instructions and tool-call arguments. The summarizer is not given a complete child execution record. Model component: [RT-CMP-summarizer-model](#rt-cmp-summarizer-model). SRC-1: `source/tools/Agents.go`, `source/utils/chat/SummarizeMessages.go`, `source/agents/summarizer.yaml`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Synchronous tool string containing the final emitted message Content, or a summarization error.
- Later read-back: If invoked through Session, the returned summary becomes a tool message eligible for later inference/backup. The original child transcript is not replaced by this summary.
- Delegated visibility: A separate temporary-directory child receives projected prose, not tool results or system messages; only its parsed final message Content crosses back.
- Selection predicate: Caller-selected recorded agent name and SummarizeMessages flags true, true, false; last stdout line is parsed as the summary message.
- Invalidation or expiry: Process timeout defaults to 30 minutes; successful process completion removes the temporary directory. Summary remains a snapshot even if the original child continues work.
- Activation or effect: Reduced prose can be delivered to the caller's later inference; no factual completeness or behavioral activation was observed.
- Evidence limits: None of the embedded role YAMLs grants agents.Inquire; grant-dependent library capacity is not default planner activation. Final message Content can contain a tool-report envelope and is not validated against a reference summary.

Decision roles: caller chooses the child; code chooses source fields; summarizer proposes condensed text; parse/process success admits the result without human content approval. Operating mode: requested summarization, not a curriculum or answer-oracle experiment. Instructional guidance asks preservation of facts and removal of redundancy, but implementation neither compares the result against a reference nor proves preservation. The admitted summary is a context result, with no automatic revision of the original child record. No theory-building or learning conclusion is asserted.

> messages := utils_chat.SummarizeMessages(agent.Messages, true, true, false)
> --- `source/tools/Agents.go`

> line := strings.TrimSpace(lines[len(lines)-1])
> summary := schemas.Message{}
> --- `source/tools/Agents.go`

#### RT-RTE-program-execution
Label: Program execution

Granted programs.Execute → allowed executable-name test → argument sanitization → host process → buffered stdout/stderr result. Programs owns admission/execution; the calling model or direct client proposes executable and arguments. A name allowlist does not restrict the instructions interpreted by Go or another granted program. Path-looking arguments are sanitized; internal operations of the program are not mediated by that check. Operating mode: open tool-selected host work. Go/test output can inform the caller, but Programs provides no reference answer or semantic correctness oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synchronous tool string with command/output on success, or an error; Session's generic error branch retains the error text rather than guaranteeing the separate result buffer reaches the model.
- Later read-back: Tool messages can enter session recovery; program-created files can be read later through filesystem/tool paths. No replay of the program itself is guaranteed.
- Delegated visibility: A contractor's output stays in its context unless reported; its filesystem effects can cross the conversation boundary.
- Selection predicate: Exact executable membership in AllowedPrograms and granted Execute method; path-containing arguments pass sanitizeSandboxPath.
- Invalidation or expiry: Ten-minute context deadline, cancellation after silent output, and 16MB output buffer limit; these are process controls, not content rollback.
- Activation or effect: exec.CommandContext runs with Sandbox as working directory and empty stdin; arbitrary permitted program behavior can affect host resources under OS permissions.
- Evidence limits: No deployed OS sandbox or execution supplied; descendants, network restrictions and executable provenance are unknown.

Product/capability implications: runtime admits execution after name/argument checks, not after human approval. Role guidance and current conversation shape the model's proposal. A model can propose Go code or tests; filesystem effects persist without automatic rollback or a correctness admission gate. This counterexample bounds the planner's no-code policy without claiming an observed bypass. SRC-1: `source/tools/Programs.go`, `source/engine/Session.go`, `source/agents/planner.yaml`.

> if slices.Contains(tool.AllowedPrograms, program) {
> --- `source/tools/Programs.go`

> cmd := exec.CommandContext(ctx, program, program_arguments...)
> cmd.Dir = tool.Sandbox
> --- `source/tools/Programs.go`

#### RT-RTE-client-tools
Label: Client tools

Terminal slash command or browser/HTTP tool request → Session.CallTool → installed tool method → result message. Direct client control changes the proposing principal, not the downstream tool-specific HasMethod predicate. For an installed Humans tool, Answer is admitted even outside the literal Methods array; downstream answer delivery is a separate question, as [EPI-RTE-human-answers](epistemic.md#epi-rte-human-answers) records. The server does not require a prior model tool call. Browser CallTool's payload constructs Function.Name from `name`; its separate `method` argument is unused in that inspected method, so server parsing of the supplied name is decisive. SRC-1: `source/ui/tty/Client.go`, `app/engine/Session.go`, `source/ui/web/routes/session/CallTool.go`, `source/engine/Session.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Terminal records the tool message; HTTP returns the last message on success or a handler error. Direct CallTool does not itself request the next inference.
- Later read-back: Effects and accumulated tool messages can be consumed by later chat or backup; direct calls do not independently trigger the response-handler backup path.
- Delegated visibility: Direct requests can use the installed Agents tool to act on parent-visible contractors; child grants remain separate.
- Selection predicate: Terminal command parser or HTTP tool-call parser followed by Session.GetTool and HasMethod; no additional per-effect approval gate is visible in these handlers.
- Invalidation or expiry: Browser Waiting is a local cooperative flag; Session.CallTool lacks the SendChatRequest busy check. Server/tool timeouts depend on the selected method.
- Activation or effect: Same tool executor and host effects as model-proposed calls, without model selection.
- Evidence limits: No supplied caller-authentication or deployment-network evidence; route registration and CallTool handler themselves add no authentication check. Successful browser operation is unobserved.

Decision roles: direct caller proposes; fixed parsing, installed-tool lookup and tool-specific HasMethod predicates decide; a human can choose not to send a request, but remote caller identity is unresolved. Operating mode: explicit manual/API operation. No answer oracle. For writes or execution, admission and rollback are those of the selected route, not a new UI approval procedure.

> err6 := session.CallTool(tool_id, tool_name, tool_method, tool_arguments)
> --- `source/ui/web/routes/session/CallTool.go`

> return http.ListenAndServe(":"+server.URL.Port(), nil)
> --- `source/ui/web/Server.go`

> if tool != nil && tool.HasMethod(method) == true {
> result, err0 := tool.Call(method, arguments)
> --- `source/engine/Session.go`

#### RT-RTE-file-admission
Label: File admission

Granted Files.Write → resolveSandboxPath → FormatFileBuffer → os.WriteFile. This is the inspected ordinary product-write route available to a coder, distinct from process execution. The model or direct client supplies path/content, while software decides lexical-path and formatting admission. Role instructions request minimal, verified changes; there is no per-write human veto or test-success check in this method. Natural-language guidance influences proposal generation; symbolic helper checks and file content formatting determine accepted I/O. SRC-1: `source/tools/Files.go`, `source/tools/resolveSandboxPath.go`, `source/agents/coder.yaml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A written-file notice or sanitized error appended by Session as a tool message.
- Later read-back: Written source files persist in the project and can be consumed by Files.Read, installed programs or later project invocations.
- Delegated visibility: Shared directory effects survive contractor context termination; visibility follows assigned directory and project path, not report delivery.
- Selection predicate: Files.Write grant, resolved path inside the lexical sandbox boundary and successful formatting/I/O.
- Invalidation or expiry: A later write replaces content; no automatic versioned rollback is implemented by this method.
- Activation or effect: Immediate project file creation/overwrite under host permissions; later compilation/execution requires separate action.
- Evidence limits: Symbolic traversal check does not resolve symlinks; no observed write, tests or successful product build.

Admission trigger is a tool call; proposed change is arbitrary supplied file content. Runtime can reject path/format/I/O failures, not semantic defects. Human content authorship is possible on direct routes but is not established for model-selected writes. Files persist; rationale persists only if separately recorded. Test output is not required here and no expected-answer oracle is supplied. Operating mode: open project editing.

> err2 := os.WriteFile(resolved, buffer, 0666)
> --- `source/tools/Files.go`

> relative, err2 := filepath.Rel(sandbox_root, resolved_path)
> --- `source/tools/resolveSandboxPath.go`

#### RT-RTE-skill-loading
Label: Skill loading

Construction-time project skill discovery or explicit Skills.List catalog refresh → requested Skills.Load from that catalog → requirements checks → loaded_skills entry → generic Session tool notice on ordinary qualified calls. Session.LoadSkill system-message insertion is a separate helper/bare-name API capacity, not the final step of that shipped chain. ToolCall.GetName returns `tool + "." + method`, terminal Command.Name preserves the qualified name, and the web handler forwards GetName. GetTool resolves qualified names, but CallTool's special branches require name == "skills"; ordinary `skills.Load` and `skills.Unload` therefore bypass those branches. List calls readSkills despite the constructor's boot-only comment; readSkills clears and rebuilds contents. This refreshes discovery, not existing loaded_skills objects or injected system messages. Loaded Go scripts may subsequently run through Skills.Execute. Discovery reads `<playground>/skills/<name>/SKILL.md`, requires parsed name/directory agreement and recognizes `.go` scripts. Skill text is natural language interpreted by the model; metadata/script maps are symbolic; executable script content is symbolic program input. No new program/tool grants are appended by this inspected path. SRC-1: `source/tools/readSkills.go`, `source/tools/Skills.go`, `source/engine/Session.go`, `source/schemas/ToolCall.go`, `source/types/Command.go`, `source/ui/tty/Client.go`, `source/ui/web/routes/session/CallTool.go`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Ordinary qualified Load/Unload calls append generic tool success/error notices, without invoking the system-message helpers. Execute returns script output/error. A separate bare-name Session.CallTool embedding can run the helper after tool success; direct helper calls return an error or nil.
- Later read-back: Skill files persist externally and are rediscovered on construction or explicit Skills.List within the same process. Load reads the current catalog; loaded objects supply later Execute selection. Ordinary tool notices can persist in session messages, but are not skill-body injection. Bodies separately inserted through the helper/bare-name API can persist there. List alone does not replace loaded objects or reinject changed bodies.
- Delegated visibility: Skills use the child's playground for discovery and its sandbox for execution; a child body does not automatically enter the parent conversation.
- Selection predicate: Caller-selected discovered name, missing-program/tool checks in Skills.Load, loaded script membership and runtime allowlist for Execute.
- Invalidation or expiry: List clears/rebuilds the discovery catalog, leaving loaded_skills and session messages unchanged. Load can replace the loaded object from the refreshed catalog; ordinary qualified Unload removes loaded state but not system-message bodies. On the separate helper path, Session.LoadSkill detects duplicates by body text, not name, so inserting changed text can append a new body without removing the old one. Session.UnloadSkill removes matching bodies, preserving other turns and older differing bodies. Script execution has timeout/output cancellation like Programs.
- Activation or effect: Ordinary qualified calls change catalog/loaded-object state and append generic tool notices; they do not deliver the skill body at system-message priority. Separate helper/bare-name API use affords that priority delivery/removal, not observed compliance. Loaded scripts run as ordinary host processes, not within a new OS isolation boundary.
- Evidence limits: Current embedded roles do not grant skills methods. Granting/installing the tool alone would not repair the qualified-name branch mismatch. Helper/bare-name API capacity is inspected, but no shipped parser invokes that injection chain and operation is unobserved. Session.LoadSkill called directly does not enforce missing programs like Skills.Load does.

Admission trigger is an explicit load request against the construction-time or List-refreshed catalog. Catalog refresh, loaded-object replacement and message injection are separate steps; no file watcher or automatic same-name body replacement is established by these methods. Caller/model proposes the selected skill; Skills decides loaded-state admissibility. Session decides instruction insertion only on the separate helper/bare-name API path. File authorship may be human or computational and is not fixed by discovery. No human approval or answer oracle validates the body's instruction quality. Ordinary Unload removes loaded state, not injected instruction bodies; Session.UnloadSkill separately affords instruction removal. Neither rolls back prior script/file effects. Operating mode: explicit extension selection; no experiment/curriculum. The runtime does not automatically revise the skill body or criticize a formulated theory in this route, so no theory-builder property is inferred.

> func (tool *Skills) List() (string, error) {
>
> readSkills(tool)
> --- `source/tools/Skills.go`

> for name, _ := range tool.contents {
> delete(tool.contents, name)
> }
> --- `source/tools/readSkills.go`

> if len(missing_tools) == 0 && len(missing_programs) == 0 {
> tool.loaded_skills[skill.Name] = skill
> --- `source/tools/Skills.go`

> return tool + "." + method, nil
> --- `source/schemas/ToolCall.go`

> command.Name = strings.TrimSpace(name)
> command.Method = strings.TrimSpace(command.Name[strings.LastIndex(command.Name, ".")+1:])
> --- `source/types/Command.go`

> } else if name == "skills" && method == "Load" {
> --- `source/engine/Session.go`

> } else if name == "skills" && method == "Unload" {
> --- `source/engine/Session.go`

The following passages support the separate helper capacity, not ordinary qualified-call delivery.

> if message.Role == "system" && message.Content == skill.Body {
> index = m
> break
> }
> --- `source/engine/Session.go:566-569`

> system_messages = append(system_messages, &schemas.Message{
> Role:    "system",
> Content: skill.Body,
> Created: schemas.NewDatetime(),
> })
> --- `source/engine/Session.go`

#### RT-RTE-requirement-signoff
Label: Requirement signoff

Caller-selected specification path/symbol → Requirements.Signoff → reread requirements → read source → AST symbol check → in-memory IsImplemented update → unimplemented-only serialization. This is a status-admission mechanism, not a product correctness guarantee. Planner has Signoff in its role grants. Software decides source parse/symbol existence; the calling model or direct client chooses what to sign off. No human signature is intrinsically required despite the method name. SRC-1: `source/tools/Requirements.go`, `source/utils/ast/HasSymbol.go`, `source/agents/planner.yaml`, `source/tools/writeRequirements.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Implemented-status notice or error.
- Later read-back: writeRequirements serializes only unimplemented entries, omitting the signed-off entry. readRequirements clears the map, reconstructs implemented entries from source with empty Behavior, then imports JSON only at missing file/symbol keys. Later tools/UI consume that reconstructed view, not persisted signoff status or necessarily the original authored behavior. See [MEM-RTE-requirement-update](memory.md#mem-rte-requirement-update) and [EPI-RTE-requirement-refresh](epistemic.md#epi-rte-requirement-refresh).
- Delegated visibility: Project requirements are addressed using playground-relative records after sandbox/path checks, allowing planner consumption of contractor specifications.
- Selection predicate: Existing path/symbol specification, readable source and HasSymbol for the expected type.
- Invalidation or expiry: Source changes alter reconstructed entries; source-first collisions can discard authored Behavior and signoff serialization omits implemented entries. Source deletion need not recover the discarded specification. This method neither proves ongoing behavioral satisfaction nor supplies rollback history.
- Activation or effect: Sets IsImplemented true in memory and rewrites pending requirements JSON without implemented entries; does not persist that true decision, compile, execute tests or compare behavior against the natural-language specification.
- Evidence limits: No observed signoff; helper inspection supports structural admission only, not complete behavior verification.

Trigger/proposal is a signoff call. Admission can reject missing source, symbol or I/O; no test oracle or expected behavioral answer is used. Guidance is role/specification content interpreted by the caller. Operating mode: open project status update. What persists through this writer is the remaining unimplemented specifications, not the signed-off specification/status. Implemented status is regenerated from source; its empty Behavior can displace authored intent. No automatic criticism/revision of explanatory content is established.

> if utils_ast.HasSymbol(source, specification.Symbol, specification.Type) == true {
> tool.mutex.Lock()
> specification.IsImplemented = true
> --- `source/tools/Requirements.go`

> if specification.IsImplemented == false {
> --- `source/tools/writeRequirements.go`

> Behavior:      "",
> IsImplemented: true,
> --- `source/tools/readImplementedRequirements.go`

> _, exists := tool.contents[file][symbol]
>
> if exists == false {
> tool.contents[file][symbol] = specification
> }
> --- `source/tools/readRequirements.go`

#### RT-RTE-build-install
Label: Build and install

Operator-selected source build → Go compiler → build/installer assets → installer copies assets to `<prefix>/bin`. BuildExocomps produces exocomp, exocomp-agent and agimus artifacts for build and embedded-asset locations; InstallExocomp copies exocomp and exocomp-agent. Owner is the toolchain/installer code and invoking operator, not the foreground Session. Executable build/installation is symbolic production machinery. SRC-1: `toolchain/actions/BuildExocomps.go`, `toolchain/utils/Build.go`, `installer/actions/InstallExocomp.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compiler process result/build notice; installation reports copied paths or returns an error.
- Later read-back: A later operator invocation can execute installed binaries; build success and that invocation are unobserved.
- Delegated visibility: Installed/overridden executable can determine subsequent contractor runtime; existing children are not updated by a file copy.
- Selection predicate: Operator-selected OS/base directory/prefix, compiler success and available embedded asset bytes.
- Invalidation or expiry: Later builds/copies replace artifacts; these methods provide no version rollback or coordinated atomic multi-binary installation.
- Activation or effect: Installation writes executable files; live execution requires a subsequent launch.
- Evidence limits: Tracked asset placeholders are not built binary evidence; external dependencies and actual compilation/distribution success remain unestablished.

Admission trigger is operator build/install invocation, proposed change is source-derived executable content. Compiler/I/O can reject, but no behavioral test gate appears in these methods. Human selection of source content is not established by running the driver. What persists is compiled/copied artifacts; guidance/provenance beyond the selected source and build arguments is unresolved. Operating mode: manual production workflow; no answer oracle or automatic evidence-responsive runtime update is shown. The executable-override authority is separately described in [RT-RTE-contractor-work](#rt-rte-contractor-work).

> cmd := exec.Command("go", args...)
> cmd.Dir = cwd
> cmd.Env = env
> --- `toolchain/utils/Build.go`

> path := filepath.Join(prefix, "bin", "exocomp")
> err12 := os.WriteFile(path, buffer1, 0755)
> --- `installer/actions/InstallExocomp.go`

### Claims

#### RT-CLM-role-separation
Label: Role separation and sandbox claim

Claimed operation: planner coordinates rather than writes code; all agents access only their own sandboxes. Source: planner prompt, doctrine/design. Tool/method filtering supplies a real admission mechanism, but role semantics and OS confinement do not follow from it. Planner's permitted Go process is a source-supported forcing case against reading those statements as universal runtime guarantees. See [RT-RTE-program-execution](#rt-rte-program-execution), [RT-RTE-file-admission](#rt-rte-file-admission) and [RT-OBJ-role-grants](#rt-obj-role-grants). SRC-1: `source/agents/planner.yaml`, `source/tools/Programs.go`, `source/tools/resolveSandboxPath.go`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> - You NEVER write production code or unit tests yourself
> - You ALWAYS orchestrate
> --- `source/agents/planner.yaml`

> All agents can only access the files within
> their own sandboxes.
> --- `source/agents/planner.yaml`

### Evidenced absences

#### RT-ABS-skill-grants
Label: Embedded skill grants

- implementation conclusion status: absent

Searched boundary: frozen SRC-1 revision b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251, all `source/agents/*.yaml`, query `skills\.` alongside allowed-tools/program listings. No embedded role's allowed-tools list includes a skills method. This supports absent default role grants, not absent Skills implementation, project files or externally installed tools. [RT-RTE-skill-loading](#rt-rte-skill-loading) therefore describes an afforded mechanism rather than observed/default activation. Positive neighboring evidence confirms ordinary grants and role-derived Toolset construction. SRC-1: `source/agents/planner.yaml`, `source/agents/coder.yaml`, `source/agents/architect.yaml`, `source/agents/tester.yaml`, `source/agents/summarizer.yaml`, `source/agents/exploiter.yaml`, `source/agents/webscanner.yaml`, `source/tools/Toolset.go`.

> for _, tool_name := range allowed_tools {
> --- `source/tools/Toolset.go`

### Behavioral-authority paths

#### RT-BAP-role-prompt
Label: Role prompt authority

Consumer: configured planner/contractor model. Channel: rendered embedded role prompt supplied as system messages plus task messages; Session.LoadSkill or a bare-name Session.CallTool embedding can append an additional system body; ordinary qualified Skills.Load tool calls do not reach that helper and supply only generic tool notices. Force: model-interpreted instruction priority, not a tool invariant or evidence of compliance. Horizon: agent conversation, including recovered messages across project sessions. Role text and symbolic grants have different consumers; prose restrictions are not enforced merely by copying grant arrays. SRC-1: `source/agents/NewAgent.go`, `source/engine/Session.go`, `source/agents/planner.yaml`. See [RT-OBJ-role-grants](#rt-obj-role-grants), [RT-RTE-skill-loading](#rt-rte-skill-loading).

> Prompt:          prompt,
> Temperature:     temperature,
> Messages:        render_messages(prompt),
> --- `source/agents/NewAgent.go`

## Annotations

none
