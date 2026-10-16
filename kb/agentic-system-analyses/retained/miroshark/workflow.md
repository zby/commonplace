---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MiroShark workflow account: asynchronous report request, parallel section delegation, bounded retrieval, synthesis and retained delivery."
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
---

# MiroShark workflow report

## Workflow account

### Selected workflow and evidence

This account selects **report generation from an existing simulation**. It exposes a complete shipped request-to-artifact path with model planning, parallel delegation, local rejection, recovery and delivery. It does not join simulation, interviews and publication into a mandatory pipeline. Simulation preparation and execution remain upstream routes in [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) and [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds).

The [boundary](boundary.md) fixes SRC-1 and the reviewed commit. This account inspects implementation in `backend/app/api/report.py` and `backend/app/services/report_agent.py`, including planning, parallel orchestration, synthesis and download beyond the baseline's section-loop account. Inline comments describe intent, not measured latency or coherence. No target execution, report artifact or provider response was supplied or produced. Successful delegation, synthesis quality and delivery to an actual user remain unobserved.

### Request and planning

The caller supplies `simulation_id` and optionally `force_regenerate`. The report API resolves the simulation and project, graph ID and stored simulation requirement. It rejects missing or invalid prerequisites. It does not require evidence here that simulation rounds completed successfully. Without forced regeneration, an existing completed report can satisfy the request immediately. Otherwise it allocates separate report and task IDs, obtains graph tools from Flask's storage extension, and starts a background thread carrying the request locale. The immediate response identifies work in progress, not a finished answer ([WF-RTE-report-delivery](#wf-rte-report-delivery)).

The background worker constructs ReportAgent with graph ID, simulation ID, requirement and graph tools. ReportAgent plans an outline using graph statistics, entity types and at most ten related facts. The model proposes section titles; code constructs the outline and saves it without per-section human approval. A planning exception produces a default three-section outline. This fallback maintains progression; it does not verify that the fallback fits the evidence (SRC-1, `backend/app/services/report_agent.py`).

### Delegation and context boundaries

Application code, not a planner agent's tool call, schedules one worker per outline section through a bounded ThreadPoolExecutor. Each worker receives its section, the outline and access to the ReportAgent's retrieval/model services. It gets its own section message history, propagated locale/context variables and, where enabled, a separate reasoning recorder. It does **not** get sibling drafts. The actual parallel call passes an empty previous-sections list. The helper's ability to accept prior excerpts in [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) must not be mistaken for delivery of those excerpts on this path (SRC-1, `backend/app/services/report_agent.py`).

Workers return `(index, title, content)`. The coordinator saves each result as it finishes, while positional slots preserve outline order for synthesis. Only returned text crosses this section-context boundary; complete section conversations and tool observations are not automatically merged into another worker's model window. The section mechanism is annotated below rather than redeclared.

### Verification, rejection and recovery

Within a section, the model proposes tool calls or a final answer; code parses and dispatches only the first tool call per response. The normal final-answer branch rejects completion before two calls. Responses combining a tool call with a final answer receive corrective messages twice; a third conflict degrades to executing the first call. Quotas and an eight-iteration ceiling limit this local negotiation. Exhaustion forces content generation without the normal minimum-call condition. These are formatting and activity checks, not factual verification or an expected-answer oracle ([RT-RTE-report-sections](runtime.md#rt-rte-report-sections)).

The orchestration worker catches section-generation exceptions and returns an error placeholder as section content. Consequently a section error need not fail the report. After workers return, synthesis receives only the first 3,000 characters of each generated section, not every source observation or necessarily every conclusion. It asks a model for cross-section insights; it does not veto or revise the original sections. Fewer than two sections, an empty response or synthesis failure can yield no synthesis, while assembly proceeds. A nonempty synthesis is appended to the last section. Cross-section checking is therefore partial-context model interpretation, not an acceptance gate (SRC-1, `backend/app/services/report_agent.py`; [WF-RTE-report-delivery](#wf-rte-report-delivery)).

### Delivery and failure ownership

The coordinator assembles saved sections, marks the report completed, saves it and updates progress. The API background task completes only when the returned report has completed status; otherwise it fails the task. Outer generation exceptions create a failed report with an error and attempt to save failure progress. The caller can request another generation. This is retry/new-artifact recovery, not rollback of already saved sections or graph/tool effects. Existing completed-report preference in the start path avoids automatically replacing an older finished result with a newer failed one (SRC-1, `backend/app/api/report.py`, `backend/app/services/report_agent.py`).

Delivery here means a retained report reachable through report-details and Markdown-download endpoints, not merely a successful HTTP start response. No user approval or factual-quality threshold is required at this handoff. Completed status can coexist with section placeholders and omitted synthesis. Saving and exposing the artifact establish implementation wiring, not actual user receipt or a reliable forecast.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-report-delivery
Label: Report orchestration and delivery

Endpoints: caller's report request → API background worker → outline and parallel section workers → optional synthesis → saved report and HTTP retrieval. Owners: report API for admission/task lifecycle; ReportAgent for orchestration; ReportManager for file retention. This route is the outer request-to-delivery mechanism, distinct from the contained section retrieval loop in [RT-RTE-report-sections](runtime.md#rt-rte-report-sections). It is not another declaration of that loop. Source: SRC-1, `backend/app/api/report.py`, `backend/app/services/report_agent.py`, implementation layer.

The caller selects the simulation and regeneration option. Models propose outline, section and synthesis prose; code admits the outline, collects returned sections and declares completion after assembly. No per-content human veto is required. Operating mode is open simulation analysis; no reference-answer oracle is supplied. Guidance includes the simulation requirement, graph context, outline and section/synthesis prompts. What persists is report metadata, outline, section files, final Markdown and progress/log records, not a demonstrated improvement to the report machinery. Rejection/recovery includes prerequisite HTTP errors, fallback outline, section placeholders and failed outer-report state; regeneration is caller-directed, not automatic semantic rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: report/task IDs and generating status, or an existing completed report ID, or an admission error; background work later returns a completed or failed Report.
- Later read-back: ReportManager reloads retained reports for details/download; non-forced generation can reuse a completed report.
- Delegated visibility: section workers receive section/outline and local tool observations, not sibling drafts; synthesis receives up to 3,000 characters per returned section; HTTP consumers receive serialized report data or Markdown.
- Selection predicate: valid simulation/project/graph/requirement and initialized storage for new generation; outline selects section work; nonempty synthesis is appended to the last section.
- Invalidation or expiry: force regeneration bypasses reuse and allocates a new report ID; no semantic expiry is enforced by the inspected generation path; failed work can leave saved partial sections.
- Activation or effect: saves report files and exposes retrieval/download; no observed report generation, user consumption or predictive benefit.
- Evidence limits: completed status does not exclude section placeholders or skipped synthesis; source-only inspection cannot establish provider behavior, factual accuracy, successful storage or user receipt.

The parallel handoff explicitly withholds prior section drafts:

> previous_sections=[],  # parallel: sections don't see each other
> --- `backend/app/services/report_agent.py`

The section failure boundary converts an exception into returnable content:

> except Exception as e:
>     logger.error(f"Section {section_num} ({section.title}) failed: {e}")
>     content = (
>         f"*(Section generation error: {e})*"
>     )
> --- `backend/app/services/report_agent.py`

Synthesis sees truncated text:

> all_content = "\n\n---\n\n".join(
>     sec[:3000] for sec in generated_sections
> )
> --- `backend/app/services/report_agent.py`

Completion follows assembly rather than a quality verdict:

> report.markdown_content = ReportManager.assemble_full_report(report_id, outline)
> report.status = ReportStatus.COMPLETED
> report.completed_at = datetime.now().isoformat()
> --- `backend/app/services/report_agent.py`

The start API can preserve access to an older finished artifact:

> existing_report = ReportManager.get_report_by_simulation(
>     simulation_id, prefer_completed=True
> )
> --- `backend/app/api/report.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

Workflow-specific handoff: the parallel caller supplies `previous_sections=[]`; no prior-section excerpts reach these workers on the selected route. Each worker returns only indexed title/content to the orchestrator. Completion order affects progress reporting, not final positional placement. SRC-1, `backend/app/services/report_agent.py`; the empty-list passage is retained in [WF-RTE-report-delivery](#wf-rte-report-delivery).

Workflow-specific rejection ownership: ReportAgent's section code rejects a simultaneous tool call and final answer twice, then degrades to tool execution. It can reject an early answer for insufficient calls, but the forced-finish path bypasses that normal minimum. The runtime record supplies the minimum/exhaustion passages. A checked local conflict passage establishes the corrective branch:

> if conflict_retries <= 2:
>     # First two times: discard this response, ask LLM to reply again
>     messages.append({"role": "assistant", "content": response})
> --- `backend/app/services/report_agent.py`

The outer coordinator, not a reviewing agent, recovers from a raised section error by retaining a placeholder. Neither these retries nor optional cross-section synthesis establish semantic acceptance of the report.
