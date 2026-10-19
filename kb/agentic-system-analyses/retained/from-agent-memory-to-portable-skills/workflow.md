---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of From Agent Memory to Portable Skills: scoped NAMS distillation through synthesis, rejection gates, human review and published delivery."
run-id: AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01
reviewed-boundary: "neo4j-article-2026-10-18-99f91d4da959"
---

# From Agent Memory to Portable Skills workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **a scoped memory request becoming a published skill available to a later agent**. It is selected because the article explicitly connects request, seven-stage construction, human review and delivery. It exposes both computational and human rejection points. This is an artifact-building workflow, not execution of the generated skill's task. No particular incident-triage run, generated procedure or successful consumer execution is supplied. The frozen article supports a documented workflow, not an observed successful run (SRC-1, `article.html`, “Distilling a Skill from Memory,” “Inside the Distillation Pipeline,” “Nothing Ships Unreviewed,” and “How a Published Skill Reaches Your Agents”; [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation), [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery)).

The inspected boundary is the article's skill-distillation and governance subsystem. The article body, pipeline description and review/delivery captions were inspected from the frozen HTML. The enclosing agents' memory production, task execution, tool permissions and consumer selection policy are not established here. Linked documentation and evaluations are outside this capture. Those limits prevent claims of an autonomous end-to-end task executor or independently verified interoperability ([boundary](boundary.md#boundary-and-evidence); SRC-1, `article.html`, delivery and pipeline sections).

### 1. Caller hands scope to a queued job

A caller initiates distillation through HTTP, MCP or the dashboard. The scope limits which conversations can supply evidence. The trigger enqueues a run on Redis; the distiller, rather than the initiating caller or synthesis model, owns the documented pipeline progression. The job is pollable, but the initial response, job-identity format, polling protocol and caller identity are unspecified. Initiating it is not approval of the content it will generate (SRC-1, `article.html`, “Distilling a Skill from Memory” and “Inside the Distillation Pipeline”; [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

The distiller resolves scope to conversations, takes a per-workspace lock and waits for scoped memory to settle. It then consolidates recurring actions into frequency-weighted clusters, separating effective patterns from anti-patterns using tool-call outcomes. The state handed forward includes decisions with reasoning/action/result, tool calls and recorded statuses, touched entities, and surrounding messages, observations and reflections. This is evidence preparation, not a supplied expected answer for the finished skill (SRC-1, `article.html`, “Inside the Distillation Pipeline”; [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

### 2. Deterministic construction delegates only textual synthesis

Topology is derived from recorded traces before synthesis. Tool-grounded steps obtain their tool name, typed inputs/outputs and expected status from recorded calls; judgment steps remain description-based. Dependencies and branch types reflect recorded orderings. Fewer than three recorded steps yields prose instead of a skeletal graph. Consequently, the selected workflow has a documented representation branch: a published package is not necessarily a typed graph, and topology derivation does not establish that a downstream host enforces that topology (SRC-1, `article.html`, “AIP Procedure Graphs in NAMS”; [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph), [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

The consequential model handoff is to a Python grounded-synthesis endpoint. It supplies up to 400 interleaved, PII-redacted snippets. The model returns claims and step annotations—names, descriptions and completion criteria—with source references. It is not assigned topology design or code generation. The capture does not expose snippet ranking when the scope exceeds the bound, so the model's visibility cannot be equated with the complete snapshot. Nor does this service call establish a general multi-agent delegation protocol (SRC-1, `article.html`, “Inside the Distillation Pipeline”; [RT-CMP-llm](runtime.md#rt-cmp-llm), [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

### 3. Software can reject before persistence

The service drops claims without sources; the worker then re-checks references against the actual subgraph. This separates model proposal from computational admission. Reference existence does not establish that the source entails a claim. Grounding, coverage, coherence, specification lint and PII checks precede persistence. Grounding must clear 0.9 and recurring-pattern coverage 0.6; the capture gives no score formulas or executed gate results (SRC-1, `article.html`, “Inside the Distillation Pipeline”; quotations in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) and [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls)).

A concrete documented rejection branch is a scope containing two or more separable procedures: the pipeline withholds it and suggests splitting rather than shipping a blended skill. This establishes a bounded recovery recommendation, not an automatic scope rewrite or a completed retry. Responsibility for accepting the suggestion, resubmitting scope and recovering a failed job is unspecified. Queue retries, crash handling, lock release and transaction rollback are also not exposed. The gates are therefore documented controls, not verified reliability guarantees (SRC-1, `article.html`, “Inside the Distillation Pipeline”; [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls)).

### 4. Persistence hands a pending product to a human

An accepted construction writes the skill subgraph and packaged artifact into Neo4j, pending human review. The package contains provenance frontmatter, a procedure and reference material; grounding edges link the stored skill back to supporting memory. Persistence finishes construction but does not finish publication (SRC-1, `article.html`, “What Distillation Produces” and “Inside the Distillation Pipeline”; [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package), [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

A reviewer receives steps showing tool bindings, input/output contracts, completion conditions and supporting memory. The reviewer can approve or reject after following that evidence. Human judgment is a separate publication decision, not merely acknowledgment of a machine pass. The capture does not specify a review rubric, rejection-state persistence, editing/resubmission loop or who owns recovery after rejection. No review record demonstrates how a reviewer actually applied the criteria (SRC-1, `article.html`, “Nothing Ships Unreviewed” and its review caption; quotation in [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery)).

### 5. Publication enables delivery, not demonstrated task success

The documented delivery condition is a published skill. It can be loaded into Claude Code, fetched through the NAMS MCP server, or consumed over REST. That makes the approved package available for later invocation; it does not prove a particular agent retrieved it, interpreted it correctly or completed a task. The consumer host owns tool access and task execution. Consumer-side skill matching, version selection and mandatory graph execution are not established (SRC-1, `article.html`, “How a Published Skill Reaches Your Agents”; quotation in [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery), authority limits in [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption)).

Thus the workflow's documented deliverable is a reviewed, published SKILL.md package accessible at consumer interfaces. No actual delivered package or receiving-agent trace is supplied. A claim that the next agent succeeds, or improves because of this package, would cross the evidence boundary.

### Post-delivery maintenance is bounded, not a guaranteed recovery chain

The article also describes comparing a grounded step's expected tool status with current ToolCall status. A mismatch can flag contradiction even while citations survive. This detects a specific changed backing condition; it does not locate the causal fault in the procedure or prove automatic withdrawal from delivery (SRC-1, `article.html`, “Keeping Skills Honest: Governance and Drift”; [RT-RTE-drift-check](runtime.md#rt-rte-drift-check)).

For single-step drift, repairStep takes the workspace lock, follows merged sources to survivors, drops deleted sources, revalidates and creates a superseding patch while leaving other steps untouched. With no surviving grounding it declines and flags full re-distillation. That explicit refusal bounds repair: it cannot manufacture evidence. It also does not establish restoration of tool success. The source does not specify an automatic drift-to-repair invocation, mandatory patch re-approval, installed-package refresh or an executed full re-distillation. These maintenance capabilities therefore remain adjacent documented routes, not invented automatic continuations of the selected delivery workflow (SRC-1, `article.html`, “Bounded, Node-Level Repair”; quotations and branch details in [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)

Workflow role: owns construction through a pending product, not publication. The source-reference return contract constrains the synthesis handoff; software can discard unsupported proposals and withhold the whole candidate. The separable-procedure branch returns a split suggestion, but leaves resubmission ownership and subsequent success unresolved. Neither queue completion nor model return alone meets the workflow's delivery condition.

#### On [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery)

Workflow role: the human veto separates artifact persistence from publication. The package becomes eligible for the documented consumer interfaces only as a published skill. Actual receipt and task execution remain beyond the demonstrated handoff. Rejection is supported; an editing, retry or appeal procedure after rejection is not established by the capture.

#### On [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)

Workflow role: a bounded post-delivery maintenance branch, not evidence of automatic recovery. A one-step diff gives a reviewer a narrower change to inspect, but does not establish that review must approve the patch before release. The no-survivor branch escalates to a full re-distill flag rather than completing replacement; its eventual delivery cannot be inferred.
