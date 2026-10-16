---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Exocomp's instructed Go feature workflow: specification, contractor implementation, testing, repair and operator delivery, with report-acceptance limits."
run-id: AAS-2026-10-14-exocomp-692bb27c35f9-01
reviewed-boundary: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
---

# Exocomp workflow report

## Workflow account

### Selection and evidence

The representative workflow is an operator's Go feature request handled by the planner through architect, coder and tester contractors. It is selected because the shipped planner prompt connects these roles into one lifecycle, rather than merely listing independent tools. The workflow is an instructed coordination policy over implemented chat and contractor mechanisms, not an enforced phase machine or an observed successful project. [WF-CLM-project-phases](#wf-clm-project-phases) records that policy; [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) supply the implemented handoffs.

The evidence is SRC-1 implementation and doctrine/design at the frozen revision. Added inspection within that registered source covers `source/agents/architect.yaml`, `source/agents/tester.yaml`, the Quit/Await/Fire and process-finalization portions of `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`, and the Quit hook in `source/ui/jsonl/Client.go`. Planner and coder prompts were also reread. Correction inspection additionally covers method-name construction in `source/tools/Toolset.go`, exact membership and dispatch in `source/tools/Requirements.go`, and tool admission in `source/engine/Session.go`; these supply implementation evidence for the specification obstruction below. No target execution or tests were performed. No stored historical session is used as evidence that this complete workflow ran.

### Request, plan and specification

1. **Clarify and plan.** The operator sends the feature request to the planner. Session supplies accumulated messages and role-filtered tools to the configured model. The model chooses exploration and human-question calls; the prompt asks it to identify affected paths/symbols and a verification plan. Session executes valid granted calls and continues inference, but does not require clarification before delegation. A tool-free answer ends the current chat chain, not necessarily the project. See [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat). SRC-1: `source/agents/planner.yaml`, `source/engine/Session.go`.
2. **Delegate specification.** The planner chooses an architect task and sandbox through Hire. The child receives its generated name, role, task prompt, playground, sandbox and server URL; it does not receive the full planner conversation. Architect instructions ask for precise requirements that coders and testers can consume without further discovery. Requirements are the intended project artifact handoff, separate from the child's prose report, but ordinary architect Define* calls are obstructed at this revision. Toolset lowercases every character after the first in method names: the architect's `requirements.DefineFunc` grant installs `Definefunc`, and similarly installs `Defineinterface`, `Definestruct` and `Definetype`. Requirements.HasMethod uses exact membership, while Requirements.Call dispatches the original mixed-case names. A call using `DefineFunc` fails admission; a call using `Definefunc` passes membership but matches no dispatch branch. Thus valid Hire/Await delegation does not establish production of new requirements through the instructed tools. Existing requirements may still be read, and the child may return prose, but neither supplies the claimed new artifact automatically. [WF-CLM-project-phases](#wf-clm-project-phases) retains the dispatch evidence. SRC-1 implementation: `source/tools/Toolset.go`, `source/tools/Requirements.go`, `source/engine/Session.go`; doctrine/design: `source/agents/architect.yaml`. The planner is instructed to Await the architects, inspect requirements and ask the human to confirm the implementation plan; these downstream steps cannot be assumed to receive the newly specified artifacts from this obstructed route. Confirmation is requested model behavior, not a mandatory write-admission predicate. See [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) and [WF-CLM-project-phases](#wf-clm-project-phases). SRC-1: `source/tools/Agents.go`, `source/agents/architect.yaml`, `source/agents/planner.yaml`.

### Implementation, verification and repair

3. **Delegate implementation.** The policy assigns a coder per package, prioritizing reported bugs over new features. The planner supplies a concrete task and directory; the coder can read available specifications through requirements tools and change files through its granted methods. This downstream capability does not repair the architect's Define* obstruction: a newly requested feature's specification cannot be assumed to exist merely because the architect returned a report. The same missing-artifact limit applies to tester consumption below. File admission checks paths, formatting and I/O, not conformance to the specification. Program execution admits allowed executable names and arguments, not correct program behavior. Coder instructions request Go-toolchain verification and change logging, but these are not preconditions for a write or a Quit report. Files are changed before planner report acceptance; the handoff is not an isolated patch awaiting merge. See [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-program-execution](runtime.md#rt-rte-program-execution) and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work). SRC-1: `source/agents/coder.yaml`, `source/tools/Files.go`, `source/tools/Programs.go`.
4. **Delegate tests and inspect results.** The instructed next role is a tester per package. It can read requirements/source, write tests, execute Go and add bugs. Its prompt requires `go test`, but neither report extraction nor product writes require proof that tests ran or passed. Tests can provide task-specific behavioral checks chosen by the tester; the runtime supplies no independent reference answer validating test adequacy. The rule that testers write only unit tests is prose: the tester has Files.Write and permitted Go execution, not a test-file-only capability boundary. [WF-CLM-project-phases](#wf-clm-project-phases) supplies the testing contract; [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) and [RT-CLM-role-separation](runtime.md#rt-clm-role-separation) bound its enforcement. SRC-1: `source/agents/tester.yaml`, `source/agents/planner.yaml`.
5. **Repair or reconsider.** Newly reported bugs are supposed to trigger a separately hired coder. The planner owns that scheduling choice; Session does not automatically hire a repair worker or enforce a retest loop. Human-requested feature changes are instructed to restart clarification as a separate project. Thus a bug report or failing test can inform the planner's next action, but does not implement an automatic rollback or rejection of files already written. See [WF-CLM-project-phases](#wf-clm-project-phases), [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) and [RT-RTE-file-admission](runtime.md#rt-rte-file-admission). SRC-1: `source/agents/planner.yaml`.

Requirements.Signoff is a different acceptance operation: it sets implemented status after an AST symbol-presence check. It can reject missing source/symbols or I/O failures, but does not run tests or compare behavior with the requirement text. It is available to the planner, not an enforced final lifecycle gate. See [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff). SRC-1: `source/tools/Requirements.go`, `source/agents/planner.yaml`.

### Contractor failure and delivery

Await provides a real synchronization boundary: it waits for a registered process to finish before returning a report to the planner. Hire returns earlier with the assigned agent name/task. Parent bookkeeping retains child messages, while the planner's requested Await result contains an extracted report, not a complete transcript or validated artifact bundle. Files remain separately visible in the assigned project directories. [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) supplies this mechanism. SRC-1: `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`.

The inspected failure path is a child terminating without a nonempty Quit report: process finalization marks it failed, and Await returns an error. Fire explicitly cancels a registered child and waits for its completion; the timeout/watchdog can also cancel a child. None restores prior files. The planner can choose another Hire or ask the human after receiving the tool error, but the inspected mechanism does not itself choose a replacement task. Recovery of session metadata does not revive the child process. See the contractor annotation below and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work). SRC-1: `source/tools/Agents.go`.

A crucial limit is that **child exit success and parent report acceptance use different criteria**. Quit uses a phrase in the message to choose exit success, while the parent ignores the Wait result and accepts any nonempty extracted Quit report. A child reporting inability without that phrase can therefore exit with status 1 yet be marked finished and supply a report to Await. This is a source-supported path, not an observed event or a claim that the planner necessarily mistakes it for correct work. The annotation retains its passages. SRC-1: `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`, `source/ui/jsonl/Client.go`.

There are three delivery boundaries: the child emits its Quit report; Await delivers that report to the planner's next inference; the planner emits an operator-facing response and leaves project files/records available. Project completion is the prompt's condition that no work remains, followed by user refinement, not a coded terminal certificate. Neither a finished child status nor a tool-free final response establishes correct software, passing tests or durable backup success. See [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat), [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) and [WF-CLM-project-phases](#wf-clm-project-phases). SRC-1: `source/agents/planner.yaml`, `source/engine/Session.go`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-project-phases
Label: Project phases

Claimed operation: planner-led clarification, planning, architect specification, human plan confirmation, coder implementation, tester verification, separately delegated bug repair and user refinement. This is SRC-1 doctrine/design, not demonstrated phase compliance. The instructed architect-to-project requirements handoff also has a known implementation obstruction, not merely missing execution evidence: Toolset installs lowercased-suffix Define* method names, whereas Requirements checks exact membership and dispatches mixed-case Define* names. No spelling reaches the ordinary definition branches through this installed tool. Contractor delegation remains implemented, but subsequent coder/tester access to newly authored requirement artifacts is not established by that delegation. This correction qualifies the lifecycle claim rather than declaring a second identity for the runtime dispatch route. Compared with [RT-CLM-role-separation](runtime.md#rt-clm-role-separation), this claim has distinct identity: lifecycle ordering and cross-role handoffs rather than restrictions on role capabilities. It uses the already declared execution routes [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) and [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work), without redeclaring them. SRC-1: `source/agents/planner.yaml`, `source/agents/architect.yaml`, `source/agents/tester.yaml`; implementation obstruction: `source/tools/Toolset.go`, `source/tools/Requirements.go`, `source/engine/Session.go`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> The specification phase is completed when all features were correctly specified
> and when all architects are done. Use the "humans" tool to let the user
> confirm the implementation plan. Afterwards, all specifications and their
> implementation status can be observed with the "requirements" tool.
> --- `source/agents/planner.yaml`

> You write all specifications down with the "requirements" tool.
> --- `source/agents/architect.yaml`

The obstruction is in the installed method spelling, not the absence of definition implementations:

> method := strings.ToUpper(tmp2[0:1]) + strings.ToLower(tmp2[1:])
> --- `source/tools/Toolset.go`

> tool = NewRequirements(allowed_methods, playground, sandbox)
> --- `source/tools/Toolset.go`

> func (tool *Requirements) HasMethod(method string) bool {
> return slices.Contains(tool.Methods, method) == true
> }
> --- `source/tools/Requirements.go`

> } else if method == "DefineFunc" {
> --- `source/tools/Requirements.go`

> } else if method == "DefineInterface" {
> --- `source/tools/Requirements.go`

> } else if method == "DefineStruct" {
> --- `source/tools/Requirements.go`

> } else if method == "DefineType" {
> --- `source/tools/Requirements.go`

> return "", fmt.Errorf("requirements.%s: Invalid method.", method)
> --- `source/tools/Requirements.go`

> if tool != nil && tool.HasMethod(method) == true {
> --- `source/engine/Session.go`

> - ALWAYS run "go test" with the "programs" tool
> --- `source/agents/tester.yaml`

> If there are newly created bug reports, these need to be fixed by a separately
> hired "coder" agent.
> --- `source/agents/planner.yaml`

> The incremental Refinement Phase reoccurs until no work is left to be done to
> fulfill the user's feature request. In this phase you will ask the user with
> the "humans" tool whether there are changes to be made to the codebase.
> --- `source/agents/planner.yaml`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work)

Workflow verification boundary: process completion releases Await; nonempty Quit report extraction admits a work report without validating task satisfaction. Child exit selection and parent report acceptance are distinct. Source inspection establishes the possible status-1/nonempty-report path, not its exercise. SRC-1 implementation: `source/tools/Agents.go`, `source/tools/getAgentWorkReport.go`, `source/ui/jsonl/Client.go`.

> if strings.Contains(strings.ToLower(message), "my work is done") {
> --- `source/tools/Agents.go`

> if success == true {
> os.Exit(0)
> } else {
> os.Exit(1)
> }
> --- `source/ui/jsonl/Client.go`

> process.cmd.Wait()
> --- `source/tools/Agents.go`

> if getAgentWorkReport(agent) != "" {
> agent.FinishedAt = schemas.NewDatetime()
> agent.Status = "finished"
> } else {
> agent.FinishedAt = schemas.NewDatetime()
> agent.Status = "failed"
> }
> --- `source/tools/Agents.go`

> if message.Role == "tool" && strings.HasPrefix(message.Content, "agents.Quit: Work Report\n") {
> return strings.TrimSpace(strings.TrimPrefix(message.Content, "agents.Quit: Work Report\n"))
> }
> --- `source/tools/getAgentWorkReport.go`

Workflow recovery owner: Agents can cancel and report failure; the planner chooses whether/how to reassign. No-report termination rejects report delivery through Await, while already applied file effects remain outside that acceptance decision.

> return "", fmt.Errorf("agents.Await: Agent \"%s\" never finished with a work report!", name)
> --- `source/tools/Agents.go`
