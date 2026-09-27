# Recovery instruction forward test

Date: 2026-09-27. This is a simulated instruction test, not a record of runtime failures. No specialist was launched, no worker was messaged, no agent listing was requested, and no publication or live failure injection was attempted.

The acceptance question is whether each fixture has a safe explicit next step that preserves independent evidence and reports completion accurately. All five do, including both branches of fixture C. The instructions leave some operational details open, but those gaps do not authorize local substitution for a missing specialist, publication of unsupported findings, or reuse of an exposed draft.

## Boundary and instruction identity

The probe read only `AGENTS.md`, `kb/work/COLLECTION.md`, [Analyse an Agentic System](../../../instructions/analyse-agentic-system/SKILL.md), and [Analyse agent memory](../../../instructions/analyse-agent-memory.md). It did not inspect the reliability workshop, audits, or prior analyses. The probe report itself is the sole owned output.

Instruction SHA-256 values at inspection:

- `analyse-agentic-system/SKILL.md`: `75f4ac90c1de0283d36f1a36c26c3478e0f74f1b31d1c0af92d4006fc093fdf8`.
- `analyse-agent-memory.md`: `4c5ae2555eda3623f12c02d062dd37d1634ddc3b17d0cac48e14e0f58f580743`.

The type contracts and command implementations were outside the read boundary. This test assesses what the two procedures instruct; it does not establish runtime scheduling behavior or validator coverage.

## A. Mandatory specialist launch fails after the input is frozen

**Fixture:** The memory specialist cannot launch because the runtime reports a thread limit. The input is already frozen.

**Next actions:** Preserve the frozen input and its hash. Report the failed launch and execution blocker to the supervising coordinator. End the analysis coordinator's turn when needed to release capacity. Do not run the specialist pass in that coordinator's context, interrupt an agent and assume capacity was released, or inspect an agent listing. Establish that the failed launch left no writer owning the report path before replacement. The supervisor can then commission a fresh specialist against the same input and output path and resume the coordinator after the specialist ends.

**Owner:** The analysis coordinator preserves its run; the supervisor schedules recovery; the fresh specialist owns the memory report and classifications.

**Continuation and publication:** A correctable scheduling failure leaves the run `running`. Integration resumes only after the specialist report passes the run, source, boundary, input-hash, completion and source-anchor checks. A missing mandatory specialist is an execution blocker, not a brief completed lens. Publication remains unavailable until the normal complete-result conditions hold. Abandonment instead marks the run `failed` and requires a new run ID.

**Instruction gap:** Step 5 assumes a supervising coordinator exists. A root coordinator has no explicitly named escalation recipient or capacity-release arrangement. It can safely report the blocker and stop, but successful automatic resumption is not specified. The instructions also do not define which runtime signal proves output ownership is resolved; until it is resolved, they explicitly prohibit a second writer.

## B. Finished specialist report, failed notification

**Fixture:** The specialist finished its report and checks, then `send_message` failed with a thread-limit error.

**Next actions:** Keep the finished report. Return its path, final SHA-256, report status, integration issues, and the notification failure in the specialist's final response, then end the turn. Do not retry through agent listings or claim that the notification arrived. The supervisor can relay path, hash and status without analytical prose. The coordinator retrieves and verifies the report itself.

**Owner:** The specialist owns the report and truthful final return. The supervisor owns relay and scheduling. The coordinator owns acceptance and integration.

**Continuation and publication:** Notification failure does not erase successful report checks or independently turn a complete report into a blocked analysis. Conversely, a report marked complete does not establish delivery, integration, or publication. Integration may continue once the report is actually available and its identities and checks are accepted. The whole run still requires its own semantic verification and publication checks.

**Instruction gap:** None material for the stated fixture. The completion event and retained report provide the explicit alternative to notification. If neither the final return nor report is accessible, recovery becomes a separate access blocker; the fixture does not establish that failure.

## C. Correction cannot be delivered

### Substantive classification correction

**Fixture:** A classification needs substantive correction, but `followup` fails.

**Next actions:** Retain the correction request as an unresolved integration issue. Report the communication failure through the available final return and yield capacity when required. Wait for capacity or retain the blocker. Return the issue to the specialist when communication resumes; a fresh specialist may be commissioned under the same frozen boundary only after the first writer's ownership is resolved. Do not perform the substantive reanalysis in the coordinator or describe the stale classification as accepted.

**Owner:** The supervisor arranges capacity and ownership; the specialist owns reanalysis; the coordinator owns the unresolved issue and later integration.

**Continuation and publication:** The run can remain `running` while recovery is possible. Stale or unsupported lens work must be rerun before continuing. The fixture's required substantive correction blocks publication until a valid specialist return resolves it. Abandonment invokes the failed-run rule.

**Instruction gap:** Step 6 permits retaining explicit uncertainty for substantive conflicts, then requires rerunning stale or unsupported lens work. The fixture falls on the required-rerun side. The boundary could be stated more explicitly: uncertainty preserves a supported limitation or disagreement; it must not conceal a known classification error or substitute for required specialist reanalysis.

### Mechanical citation endpoint correction

**Fixture:** Only a citation endpoint is wrong. The pinned passage still supports exactly the same finding.

**Next actions:** Confirm there is no active competing report writer. Inspect the pinned passage and check support for the unchanged finding. The coordinator may then repair the endpoint, disclose the mechanical edit in both the report and Reconciliation, rerun source verification, and bind the final corrected report hash. Do not clamp a number to EOF without checking the passage. Inspect each dependent check's exit status and stderr. If inspection changes the classification, evidence basis, scope or supported finding, return to the substantive branch.

**Owner:** The coordinator owns the permitted mechanical repair, support check, disclosure, verification and hash update. Specialist ownership of substantive findings remains unchanged.

**Continuation and publication:** The report can be integrated after the corrected bytes pass verification and the run/result identities bind those bytes. This repair alone establishes neither completion of the whole analysis nor publication.

**Instruction gap:** The permission to edit is explicit, but the transfer from specialist report ownership to coordinator maintenance is not operationally specified. The inherited no-competing-writers rule supplies the safe default: wait until ownership is resolved before editing.

## D. A filtered listing exposes an unrelated completed analysis

**Fixture:** Before the exact result and candidate are frozen, a filtered status lookup delivers substantive text from an unrelated completed analysis.

**Next actions:** Stop the exposed coordinator's analysis, mark its run `failed` for prior-analysis exposure, and return the failure. A fresh coordinator must begin a new run with clean source-only inputs. Do not publish the exposed draft, reuse its analytical draft as input, or treat disclosure as restoring independence. Replacement work uses completion events or the commissioned report path for status.

**Owner:** The exposed coordinator records and reports failure. The supervisor arranges a fresh coordinator and clean input boundary. The fresh coordinator owns the new analysis.

**Continuation and publication:** The failed run cannot resume or publish. Only the new independent run may proceed to its normal publication conditions. A failed run does not invoke the completed-run handoff command.

**Instruction gap:** No material gap if substantive analysis was delivered. If the listing contained only a name and completion status, that would violate the listing prohibition but would not establish the substantive exposure named in the failure rule. The fixture must distinguish those payloads; this test uses the substantive case. No empirical claim is made that a path filter behaves this way.

## E. Zero exits with wrapper truncation of source evidence

**Fixture:** Commands exit zero, but the wrapper reports that 274 tokens were truncated from a load-bearing source passage.

**Next actions:** Treat the truncated read as non-evidence. Split the batch and reread the required passage in bounded output from the same frozen source. Inspect command and wrapper delivery for truncation. Read enough surrounding text to assess support; retain the minimum verbatim supporting excerpt only after receiving it. Revisit any finding already based on the incomplete delivery. If the source pin changes or cannot be verified, fail the run and start another.

**Owner:** The agent making the evidence claim owns the bounded reread and support check. The coordinator owns integration of any corrected finding.

**Continuation and publication:** Zero exits and a requested line range do not establish delivered coverage. Continue the affected claim only after the necessary passage is delivered and inspected, or preserve a justified limitation that does not assert the missing support. A load-bearing claim that remains unsupported blocks publication. Successful quote matching is necessary where required but does not replace semantic support checking.

**Instruction gap:** None material. Both procedures explicitly cover aggregate wrapper limits as well as individual-command truncation. The number 274 does not create an exception.

## Validation

`commonplace-validate --full kb/work/agentic-analysis-reliability/recovery-probe.md` returned exit code 0 and `PASS (clean)`, with no warnings or failures. As a frontmatter-free workshop text, the file has no structural requirements; this result does not independently certify the scenario reasoning. No commits were made.
