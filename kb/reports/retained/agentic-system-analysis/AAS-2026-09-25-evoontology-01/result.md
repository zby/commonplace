---
type: agentic-system-analysis-result
description: "EvoOntology ontology/evolution layer with host-agent construction, semantic read-back, recorded-score gates and alternate mutation paths"
run-id: AAS-2026-09-25-evoontology-01
system: EvoOntology
run-date: "2026-09-25"
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "ddbb1c991de5a33e27eb32bc86a4212a7537e01e"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Accumulated or revised project ontology content, workload questions, observable trajectories, project/run/checkpoint/evaluation records, derived causal knowledge, and host-mediated Schema/Tool revisions; their shipped file/in-memory representations, retrieval and reminder routes. Static unrevised plugin instructions are method, not learned memory. External host/provider internals, benchmark task-agent runtimes and experimental reproduction are excluded."
  axes:
    storage_substrate:
      assessment: known
      basis: afforded
      values: [files, in-memory]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, RTE-8]
      note: "JSON/JSONL and host-edited code/prose files with loaded Python dictionaries; graph is content organization. Native SQLite is the inspected environment, not the retained memory store. Host revision persistence is afforded."
    representational_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, RTE-8]
      note: "Definitions, evidence descriptions and causal reports coexist with structured IDs, lifecycle/state fields, scores and editable executable/schema/tool definitions. No included route changes model parameters."
    lineage:
      assessment: known
      basis: afforded
      values: [authored, imported, other-compiled, trace-extracted]
      records: [RTE-1, RTE-3, RTE-4, RTE-8, RTE-9]
      note: "Human/host authored records, supplied history and externally recorded observations, deterministic manifests and reports, and host trace-derived patches/causal knowledge."
    behavioral_authority:
      assessment: known
      basis: afforded
      values: [knowledge, instruction, routing, ranking, validation, enforcement]
      records: [RTE-2, RTE-3, RTE-4, RTE-5, RTE-8]
      note: "Semantic prose is guidance; retained aliases/definitions affect lexical ranking; active/lifecycle state selects eligible content; saved gate input governs formal admission; host-revised instructions/code can acquire instruction or enforcement force. These authorities belong to different consumers."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic, manual]
      records: [RTE-1, RTE-3, RTE-4, RTE-7, RTE-8, RTE-9]
      note: "Automatic recording/normalization and host model authoring on invocation; direct supplied/manual authored content and file/code edits remain supported. No autonomous background evolver is inferred."
    curation_operations:
      assessment: known
      basis: afforded
      values: [dedup, evolve, invalidate, promote, synthesize]
      records: [RTE-1, RTE-2, RTE-4, RTE-5, RTE-7, RTE-8]
      note: "Normalized-question merging, revision of stored objects and code, lifecycle exclusion while retaining objects, candidate promotion, and new host-generated explanations/semantic claims. No decay or retained-content consolidation mechanism was established."
    read_back_direction:
      assessment: known
      basis: afforded
      values: [pull, push]
      records: [RTE-2, RTE-3, RTE-4]
      note: "Data agents request semantic results; evolvers are instructed to request previous records; Claude SessionStart hook automatically injects due summaries. Core read and hook paths are wired; external host's use is afforded."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse]
      records: [RTE-3]
      note: "SessionStart selects workspace-level due summaries by active-workspace availability and count/time thresholds. Identifier and lexical matching are requested retrieval here, not additional push signals."
    trace_learning:
      assessment: known
      basis: afforded
      values: ["yes"]
      records: [RTE-4, RTE-8, OBJ-7]
      note: "An invoked host evolver is explicitly commissioned to transform retained task/tool evidence into durable semantic/code/instruction revisions and reusable causal knowledge. Core alone supplies persistence/gates, not inference; raw logging alone is excluded."
    trace_source:
      assessment: known
      basis: afforded
      values: [tool-traces, trajectories]
      records: [OBJ-4, RTE-3, RTE-4, RTE-9]
      note: "Task questions, observable semantic/native calls, results, errors and final answers feed diagnosis. The inspected normalization does not preserve agent reasoning prose."
    learning_scope:
      assessment: known
      basis: afforded
      values: [cross-task, per-project]
      records: [RTE-4, RTE-8, OBJ-7]
      note: "Batch diagnosis changes a reusable project ontology/system and earlier run knowledge informs later rounds/runs. Scope follows later consumers rather than session IDs."
    learning_timing:
      assessment: known
      basis: afforded
      values: [offline, staged]
      records: [RTE-4, RTE-5, RTE-8]
      note: "Post-task frozen-batch diagnosis and candidate/evaluation/publication stages; recording during a task is acquisition, not an additional online learning route."
    distilled_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-7, RTE-4, RTE-8]
      note: "Trace-derived semantic claims, causal explanations and revised prompts plus structured semantic objects or executable/schema/tool patches. Same routes and scope as trace_learning."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-5, OBJ-6]
      note: "No retained execution evidence of dependence on recalled content was commissioned or inspected. Gate logic and instructed ablations cannot establish an observed dependence test; excluded benchmark reproduction prevents a wider negative claim."
---

# EvoOntology agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-evoontology-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/evoontology.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-evoontology-01/memory-report.md`

**Memory analysis report SHA-256:** `90332bb54f6537bec8774cab422a35678fbacfe462d35226f0123112de7773e0`

## Boundary and evidence

Evidence basis: frozen Git implementation and source doctrine/reported results at `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`, cutoff 2026-09-25. No target execution or observed causal experiment. This is EvoOntology's deterministic ontology/memory and evolution layer plus its shipped Claude Code and Codex plugin contracts. Classification: memory/knowledge/context-engineering system with a builder/improvement workflow and MCP tool surface. Boundary: complete artifact, partial loop. The layer serves model-dependent operations, while external host agents perform construction, diagnosis, tool choice and much evaluation.

Included: core store/models, semantic runtime/MCP and operation dispatch, workload/task recording, bounded SQLite execution, trajectory triggers, evaluation aggregation and evolution state, plugin instructions/hooks and their core copies. Commit-tree inspection verified all 28 core blob identities are identical in each plugin copy to the root core; root anchors apply to that implementation. Benchmark EvolutionAdapter interfaces and their three launcher/result wrappers are inspected only to bound integration. Full benchmark task-agent runtimes, datasets, private expected answers, remote models, host scheduling/tool policies and deployment are excluded. Those exclusions prevent certifying whole-agent autonomy, model identity, operational isolation, benchmark fairness/correctness or performance reproduction. No paper, ingest, prior review or other system's findings supplies evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/ruc-datalab/EvoOntology`; access root `/home/zby/llm/commonplace/related-systems/ruc-datalab--EvoOntology` | `ddbb1c991de5a33e27eb32bc86a4212a7537e01e` | Implementation: root core, equivalent plugin core, hooks and benchmark adapter boundaries. Doctrine/design: host skills/AGENTS and architecture. Reported operation: README performance, kept separate | Commit-addressed selected blobs/ranges; no worktree evidence | `evoontology/runtime/mcp_server.py:51-143`; `evoontology/runtime/ops.py:98-124,158-186,218-279`; `evoontology/evolution/session.py:390-450`; `README.md:27-30,60-86,108-114,158-180`; detailed anchors on records | Host/provider internals and benchmark executions excluded; no candidate-linked output or causal intervention. Prevents upgrading code or policy to observed learning |

## Shared records

### Components

CMP-1 — Deterministic ontology store and semantic runtime/MCP. Python parses five JSON content families into in-memory objects, returns bounded semantic navigation and a session manifest, and dispatches operations. Symbolic implementation conclusion status: wired. Model dependency lies at the served host-agent interface, not an embedded model inference loop. Source: SRC-1 `evoontology/ontology/store.py:22-105`; `evoontology/runtime/mcp_server.py:51-143`; `evoontology/runtime/runtime.py:96-151,262-329`.

CMP-2 — Build/evolution workflow, session and evaluation gate machinery. Python owns task/workload persistence, state transitions, paired-score or judge-verdict aggregation, validation and selected publication. Proposal/diagnosis and score production are delegated. Implementation conclusion status: wired for deterministic operations; whole semantic process conclusion status: afforded through host skill contracts. Source: SRC-1 `evoontology/workflow.py:55-298`; `evoontology/evolution/session.py:102-214,287-322,390-450`; `evoontology/evaluation/evaluation.py:1-118`.

> This module owns the aggregation gate and the A/B anonymization helpers; it does
> not implement ``score_fn`` or call the judge model — those belong to the
> benchmark adapter and the Evolver respectively.
> --- `evoontology/evaluation/evaluation.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

CMP-3 — External host data-agent, Builder, Evolver and optional LLM Judge roles plus plugin integration. Distributed-parametric components are host/provider models: exact model version/weights and changes during operation are uninspected. The inspected core serves tools and the skills prescribe model work; it does not establish an executed training/weight-update operation. Native host identity/model routing and approval are external. Parameter-fixity conclusion status: uninspected; instruction delivery affordance conclusion status: afforded. Source: SRC-1 `plugins/evoontology-codex/AGENTS.md:3-32,46-84`; `plugins/claude-code/skills/evo-evolve/SKILL.md:1-26,66-73`; `evoontology/evaluation/evaluation.py:8-15`. Human contributions include source/business-scope resolution, authorization and requested budget; computational host contributions include candidate generation, causal attribution and judge output. Their actual exercise is not observed.

CMP-4 — External evaluation adapter launch/result boundary. BIRD, DDR-10K and InsightBench adapters launch scenario-specific subprocesses against a named semantic version and return metrics/cases/artifact paths. They do not by those return values prove paired conditions or a gate_input for formal publication. The caller must connect evaluation evidence to the session gate. Source: SRC-1 `evoontology/evolution/adapter.py:14-56`; `benchmarks/bird/evolution_adapter.py:42-90`; `benchmarks/ddr_10k/evolution_adapter.py:41-110`; `benchmarks/insightbench/evolution_adapter.py:40-97`. Implementation conclusion status: wired launch/return interface; evaluator correctness and provider configuration: uninspected.

### Operative objects

OBJ-1 — Content Layer semantic objects and relations: Terms, Mappings, Relations, Constraints and Evidence stored in five JSON families. Terms state definitions/scope; mappings associate concepts with sources/tables/columns/filter/grain; relations connect terms; constraints state applicability/rules; evidence records source/query/result/method/time. Natural-language claims and symbolic IDs/links coexist. Implementation conclusion status: wired parsing/storage/serving; semantic grounding conclusion status: claimed by builder doctrine, not certified by reference validity. Source: SRC-1 `evoontology/ontology/models.py:57-196`; `evoontology/ontology/store.py:22-37`; `plugins/evoontology-codex/skills/build-ontology/SKILL.md:137-171,177-229`.

> @dataclass(frozen=True)
> class Evidence:
>     id: str
>     source: str = ""
>     query: str = ""
>     result: str = ""
>     validation_method: str = ""
>     timestamp: str = ""
> 
>     @classmethod
>     def from_dict(cls, data: Dict[str, Any]) -> "Evidence":
>         return cls(
>             id=data["id"],
>             source=str(data.get("source", "")),
>             query=str(data.get("query", "")),
>             result=str(data.get("result", "")),
>             validation_method=str(data.get("validation_method", "")),
>             timestamp=str(data.get("timestamp", "")),
> --- `evoontology/ontology/models.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

For OBJ-1, rationale is partially retained and selectively delivered: mapping validation text is loaded but not emitted by resolve, whereas linked Evidence query/result/method/time is emitted. Constraint block severity remains advisory to the data agent. Source: SRC-1 `evoontology/ontology/models.py:99-119,179-196`; `evoontology/runtime/runtime.py:380-392,413-479`.

>         return {
>             "id": evidence.id,
>             "source": evidence.source,
>             "query": evidence.query,
>             "result": evidence.result,
>             "validation_method": evidence.validation_method,
>             "timestamp": evidence.timestamp,
>         }
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

OBJ-2 — Schema Layer representation rules. Runtime Python dataclasses/parser defaults and shipped ontology-schema instruction define what the layer can represent. These are symbolic code plus natural-language authoring doctrine. Versions copied by SemanticStore contain content records rather than a frozen Python schema. Host-mediated schema revision is a distinct RTE-8 operation. Source: SRC-1 `evoontology/ontology/models.py:57-196`; `evoontology/ontology/store.py:22-37,179-197`; `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:11-17,139-184`. Full arbitrary schema-edit activation/recovery is uninspected.

For OBJ-2, the schema view is derived from currently loaded dataclasses, not saved per-version Schema configuration. Source: SRC-1 `evoontology/visualization/renderer.py:429-458`.

> def build_schema_view() -> Dict[str, Any]:
>     """Describe the current Schema Layer from the Core model definitions."""
>     return {
>         "object_types": [
>             {"name": name, "description": description,
>              "fields": [f.name for f in dataclasses.fields(model)]}
>             for name, model, description in _SCHEMA_OBJECTS
> --- `evoontology/visualization/renderer.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

OBJ-3 — Tool Layer configuration, runtime access and session manifest. Current tools/runtime code implements bounded browse/resolve and operation schemas; manifest describes active version/counts, tool guidance and the need to validate mappings against real data. Not a separate learned model or graph database. Source: SRC-1 `evoontology/runtime/runtime.py:96-151`; `evoontology/runtime/mcp_server.py:68-139`; `plugins/evoontology-codex/AGENTS.md:46-60`. Runtime serving conclusion status: wired; host loading/following is afforded, unobserved.

>             "### When to use semantic tools",
>             "- Call resolve_semantics with the concepts you plan to use; it returns the "
>             "corresponding tables, columns, constraints, and supporting evidence.",
>             "- Use browse_semantics only when you need to discover what concepts are "
>             "available.",
>             "- Resolved mappings are guidance, not final answers — always validate "
>             "against the actual data with your native query tools.",
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

For OBJ-3, the tool view similarly derives current registry/runtime definitions. Source: SRC-1 `evoontology/visualization/renderer.py:461-476`.

> def build_tool_view(store: SemanticStore) -> Dict[str, Any]:
>     """Describe the current Tool Layer from the real runtime/tool registry."""
>     layer = SemanticLayer(store)
>     tools = []
>     for spec in TOOLS:
>         schema = spec.get("inputSchema", {})
> --- `evoontology/visualization/renderer.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

OBJ-4 — Workload questions and recorded trajectories/observations. Project/data-source identity, origin, question IDs, tool events, results, final answer and task status accumulate in JSON. Native tools can be observed through RTE-9 or caller-supplied events; the layer is not an omniscient observer. Large results retain a bounded preview and size summary, losing full output. Source: SRC-1 `evoontology/workflow.py:62-230`; `evoontology/trajectory/trajectory.py:1-10,31-50,53-102,105-172`. Recording/truncation conclusion status: wired. Truth/completeness of externally supplied observations remains uninspected.

> def truncate_result(result: Any) -> Dict[str, Any]:
>     """Trim an oversized tool result to a bounded preview + summary.
> 
>     Keeps the full result only when small; otherwise stores a truncated preview,
>     a ``result_truncated`` flag, and a stable ``result_summary``. Used by the
>     Data Agent adapter when recording native tool calls.
>     """
>     text = str(result)
>     lines = text.splitlines()
>     too_long = len(text) > _RESULT_MAX_CHARS or len(lines) > _RESULT_MAX_LINES
>     if not too_long:
>         return {"result": result, "result_truncated": False, "result_summary": text}
> 
>     preview = "\n".join(lines[:_RESULT_MAX_LINES])[:_RESULT_MAX_CHARS]
>     return {
>         "result": preview,
>         "result_truncated": True,
>         "result_summary": f"{len(lines)} lines, {len(text)} chars; "
>         f"preview shows first {_RESULT_MAX_LINES} lines / {_RESULT_MAX_CHARS} chars.",
> --- `evoontology/trajectory/trajectory.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

OBJ-5 — Workspace/version state, active pointer, candidate/run and checkpoints. Files retain content versions, mutable pointer, run parent/round/budget/current hypothesis/candidate, rejects and completion. These are operational state with later read-back, not epistemic endorsement. Source: SRC-1 `evoontology/ontology/store.py:122-197`; `evoontology/evolution/session.py:102-163,195-214,236-270,390-450`. Formal publication protects an existing official destination against differing content, while RTE-7 can overwrite via lower-level paths. Implementation conclusion status: wired.

OBJ-6 — Evaluation plans/reports, grounded-evidence references and candidate admission records. Caller supplies metrics/cases/artifact paths/provenance/gate_input; a formal candidate gate consumes paired values or decoded judge verdicts. Grounding evidence bodies belong to OBJ-1, while evaluation records are evidence for successor choice. Neither record label nor nonempty path attests that an evaluation occurred. Source: SRC-1 `evoontology/evolution/session.py:287-322,419-450`; `evoontology/evolution/adapter.py:43-56`. Implementation conclusion status: wired storage/aggregation; provenance accuracy and causal design: uninspected.

OBJ-7 — Retained evolution explanations: problem maps, causal hypotheses, rejected explanations, unresolved uncertainty and final reports. Host Evolver produces and later rereads them under RTE-4 and RTE-8. Natural-language causal claims are distinct from OBJ-5 control fields and OBJ-6 comparative records; a current hypothesis and rejected notes are wired session fields, richer reports and later use are afforded host obligations. Source: SRC-1 `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:30-45,119-129,172-176,234-253,270-289`; `evoontology/evolution/session.py:195-214,236-270`.


> 1. Update the problem map and causal understanding.
> 2. Mark solved problems, remaining limitations, newly discovered issues, and disproven explanations.
> 3. Preserve the main validated mechanisms, rejected hypotheses, and unresolved uncertainty needed for later rounds.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

> Read:
> 
> - `references/project-context.md`;
> - `references/workload-experience.md`;
> - `references/ontology-layer-data-boundary.md`;
> - previous evolution records and accumulated knowledge, if they exist.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

For OBJ-1, the aggregate remains the Content Layer family identity shared with the memory specialist. Its combined per-object epistemic disposition is superseded by the following distinct parts; no ID is reassigned.

OBJ-8 — Term definitions and scope: readable domain meanings authored by Builder/Evolver and served to Data Agent. Candidate truth-apt semantic interpretation, with IDs/aliases as auxiliary routing data. Source and form: SRC-1 `evoontology/ontology/models.py:57-79`; OBJ-1 evidence; RTE-1, RTE-2, RTE-4.

OBJ-9 — Mapping claims: concept-to-table/column/filter/grain associations, combining prose and symbolic source references, authored by Builder/Evolver and interpreted by Data Agent. Candidate truth-apt claims about how a domain concept is realized in data. Source: SRC-1 `evoontology/ontology/models.py:83-120`; OBJ-1 evidence; RTE-1, RTE-2, RTE-4.

OBJ-10 — Relation claims: typed relationships between terms, with scope/description/reference fields, authored by Builder/Evolver and served to Data Agent. A asserted domain relationship is truth-apt; edge identifiers only identify it. Source: SRC-1 `evoontology/ontology/models.py:124-145`; OBJ-1 evidence; RTE-1, RTE-2, RTE-4.

OBJ-11 — Constraint statements: applicability/rule/severity and object references, authored by Builder/Evolver and served as advice. A factual restriction can be truth-apt; a desired policy is a non-truth-apt instruction. The schema alone does not decide which a supplied instance contains. Source: SRC-1 `evoontology/ontology/models.py:149-175`; OBJ-1 and BAP-1 evidence; RTE-1, RTE-2, RTE-4.

OBJ-12 — Evidence payloads: source/query/result/validation-method/time claims attributed to observations and supplied to later Data Agent or Evolver. These attest what a tool supposedly returned; they do not alone warrant the linked semantic interpretation. Source: SRC-1 `evoontology/ontology/models.py:178-196`; OBJ-1 evidence; RTE-1, RTE-2, RTE-9.

For OBJ-4, its aggregate identity remains workload/observations. Its heterogeneous epistemic disposition is superseded by OBJ-13 and OBJ-14.

OBJ-13 — Workload question catalog and construction metadata: supplied/generated questions, normalized text, provenance, source identity and topic. Questions request analysis rather than assert answers; provenance fields make truth-apt assertions about origin. Producer is caller plus deterministic preparation; consumers Builder/task recorder. Source: SRC-1 `evoontology/workflow.py:62-166`; OBJ-4 and RTE-3 evidence.

OBJ-14 — Observable task/tool records and final-answer claims: recorded calls/results/errors and final answer, with host/external producers and built-in SQLite branch. Consumer is later Evolver; truncation loses original suffixes. Final answers may be ampliative, but their generating host is excluded and their transformation is indeterminate here. Source: SRC-1 `evoontology/workflow.py:168-230,239-286`; `evoontology/trajectory/trajectory.py:22-102`; OBJ-4 evidence.

For OBJ-6, the aggregate remains evaluation/admission records. Its per-part epistemic disposition is superseded by OBJ-15 and OBJ-16.

OBJ-15 — Supplied evaluation evidence: metric/case vectors, decoded judge verdicts, provenance, artifact references and no-regression assertion. External evaluator/host produces, session consumes. Numeric and natural-language result assertions are truth-apt within named tasks/protocol, with truth unverified by ingestion. Source: SRC-1 `evoontology/evolution/session.py:287-322,419-450`; OBJ-6 and RTE-5 evidence.

OBJ-16 — Computed gate result and terminal disposition: Boolean acceptance and numeric comparison derived from supplied scores/verdicts, then accepted/incomplete state. Producer deterministic gate/session; consumer content publication and later state readers. The gate predicate has formal truth within supplied inputs; it does not entail a true causal explanation or general improvement. Source: SRC-1 `evoontology/evaluation/evaluation.py:28-71`; `evoontology/evolution/session.py:390-450`; RTE-5 evidence.


### Routes

RTE-1 — Workspace initialization and initial ontology build/publication. Trigger: user invokes a host build skill; host resolves source, analytical goals and fixed_split/rolling_trajectory mode, then proposes semantic objects from workload and read-only exploration. Codex instructions require competing-grounding comparison, reproducible evidence and revision of unsupported objects. The host writes the five record families, annotates limitations and calls publish_ontology_build. The Python gate refuses an already active workspace, validates the chosen content and sets active/initializes evolution state; visual presentation failure is separately reported. Proposal and semantic verification owner: host Builder with user clarification where needed. Deterministic veto: structure/reference/load validation. Effects: filesystem state and returned presentation, not certified factual truth. Source: SRC-1 `plugins/evoontology-codex/skills/build-ontology/SKILL.md:43-91,137-171,177-261`; `evoontology/runtime/ops.py:218-229`; `evoontology/validate.py:64-147`. Implementation conclusion status: wired initial publication; grounded semantic construction conclusion status: afforded.

> def publish_ontology_build(arguments):
>     workspace = _workspace(arguments)
>     if (workspace / "active.json").exists():
>         raise ValueError("An active ontology already exists; evolve it instead")
>     version = str(arguments.get("version") or "ontology_v0")
>     result = validate_semantics({"workspace": str(workspace), "version": version})
>     if not result.get("passed"):
>         raise ValueError(f"Ontology validation failed: {result}")
>     SemanticStore.set_active(workspace, version)
>     evolution_status(arguments)
>     return {"status": "published", "active_version": version,
>             "presentation": _present(arguments, version)}
> --- `evoontology/runtime/ops.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>     def _check_refs(field_value, *, label: str, allowed: set):
>         refs = field_value
>         if isinstance(refs, dict):
>             refs = refs.get("source_refs", [])
>         if not isinstance(refs, list):
>             return
>         for ref in refs:
>             if str(ref) not in allowed:
>                 errors.append(f"{label}: unresolved evidence ref {ref!r}")
> --- `evoontology/validate.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

Guidance here asks the Builder to formulate reusable definitions, mappings and constraints from the current workload/data. Formulation: afforded; evidence-oriented proposal/criticism of ambiguous grounding: afforded. Storage and subsequent serving: wired. Operative semantic use through what a claim says, valid criticism and improved future capacity: uninspected. Parts are addressable by object IDs, fields and references; that does not make each claim true. The validator checks referenced IDs when supplied and successful loading; it does not execute an Evidence.query or verify an asserted business meaning. Initial publication has no paired-improvement requirement, appropriately separate from evolution.

RTE-2 — Browse/resolve and manifest delivery. Trigger: a data-agent tool/resource request; owner: deterministic semantic runtime. It reloads selected workspace/version, performs bounded concept matching and linked return, then supplies mappings/relations/constraints/evidence and provenance/status. The host chooses later queries/actions. Result scope labels such as supported are computed from related-object availability, not independently established data truth. Resource manifest is returned on explicit resources/read; external auto-loading is not assumed. Persistence is read-only on these calls; active-pointer changes affect subsequent unpinned calls, while task-resolve can pin its task version. Source: SRC-1 `evoontology/runtime/mcp_server.py:70-114,115-139`; `evoontology/runtime/runtime.py:262-329`; `evoontology/workflow.py:288-297`. Implementation conclusion status: wired; changed host behavior: uninspected.

>         for result in results:
>             if result.get("status") == "unresolved":
>                 result["coverage_status"] = "unavailable"
>             elif result.get("status") == "ambiguous":
>                 result["coverage_status"] = "partial"
>             elif result.get("mappings") or result.get("relations") or result.get("constraints"):
>                 result["coverage_status"] = "supported"
>             else:
>                 result["coverage_status"] = "partial"
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

For RTE-2, browse requires a query and ranks active catalog entries by token overlap and exact phrase match; it returns at most six entries. Resolve handles at most five mentions but can expand ambiguous matches and linked evidence, so these are entry limits, not a total token budget. Only active/validated lifecycle states are selected. Source: SRC-1 `evoontology/runtime/runtime.py:16-19,52-53,155-219,262-378,394-479`.

>         if not query:
>             return {
>                 "status": "needs_query",
>                 "items": [],
>                 "catalog_total": catalog_total,
>                 "version": self.version,
>                 "note": "Provide a specific query. Full-catalog enumeration is disabled.",
>             }
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>         query_tokens = _tokens(query)
>         ranked = []
>         for item in items:
>             search_text = item.pop("_search_text", "")
>             if _has_contradictory_tokens(query_tokens, _tokens(search_text)):
>                 continue
>             overlap = sorted(query_tokens & _tokens(search_text))
>             phrase_match = query in search_text.lower()
>             if not overlap and not phrase_match:
>                 continue
>             score = (2 if phrase_match else 0) + len(overlap)
>             item["match_rationale"] = {
>                 "phrase_match": phrase_match,
>                 "overlap_tokens": overlap,
>             }
>             ranked.append((score, item))
>         ranked.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

> def _is_active(item: Any) -> bool:
>     return getattr(item, "lifecycle_state", "active") in _ACTIVE_STATES
> --- `evoontology/runtime/runtime.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

RTE-3 — Observation/trajectory recording and evolution trigger selection. Trigger: explicit start/event/finish operations, built-in query/resolve wrappers, or an external benchmark adapter's append; completed data tasks require at least one nonerror native-tool event. Event IDs reject conflicting duplicate records but cannot attest caller truth. Workload preparation reuses same-data history, excludes marked validation/heldout/test trajectories, preserves provenance and deduplicates normalized question text. Fixed_split accepts only registered construction IDs and disables automatic history/generated questions. A trigger/checkpoint route reports evolution due; Claude's SessionStart hook adds a reminder, while Codex doctrine asks for a status call and explicitly forbids automatically starting evolution. Owners: deterministic selection/recording; host decides whether to invoke evolution. Source: SRC-1 `evoontology/workflow.py:62-166,168-230`; `evoontology/trajectory/trajectory.py:1-10,105-172`; `plugins/claude-code/scripts/check-reminder.py:24-65`; `plugins/claude-code/hooks/hooks.json:1-15`; `plugins/evoontology-codex/AGENTS.md:62-84`. Implementation conclusion status: wired for recording/reminder; continuous autonomous evolution is not established.

>         if fixed:
>             # Imported fixed-split IDs must be explicitly enumerated at setup.
>             # Do not discover history or synthesize tasks across a benchmark boundary.
>             allowed = set(project["boundary"].get("construction_question_ids", []))
>             if candidates and not allowed:
>                 raise ValueError("Register boundary.construction_question_ids before importing fixed-split questions")
>             for q, _ in candidates:
>                 if not isinstance(q, dict) or q.get("id") not in allowed:
>                     raise ValueError("Question is outside the registered construction boundary")
>             existing = [q for q in existing if q["id"] in allowed]
>             skipped.append("fixed_split: automatic history and generated questions disabled")
> --- `evoontology/workflow.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>         if status == "completed" and not any(not e.get("error") for e in task["native_tool_calls"]):
>             raise ValueError("A completed data task needs at least one observed native tool result")
>         task.update(task_status=status, final_answer=final_answer, recorded_at=now_iso())
>         TrajectoryStore(self.root).append(task)
>         write_json(path, task)
> --- `evoontology/workflow.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

> Before a session, check whether evolution is due by calling the MCP tool
> `evolution_status` with `workspace` set to `<project-root>/.evoontology`.
> 
> If `check.evolution_due` is true, remind the user that `/evolve-ontology` is
> available. Never start evolution automatically.
> --- `plugins/evoontology-codex/AGENTS.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

For RTE-3, Claude reminder selection is coarse push: SessionStart scans active base/nested workspaces, computes due status from count/time/checkpoint state and sends due summaries via additionalContext. Consumer is host agent; selected material is workspace-level accumulated-state metadata, not matched ontology entries. Codex uses an instructed status request; neither starts evolution automatically. Source: SRC-1 `plugins/claude-code/scripts/check-reminder.py:24-65`; `evoontology/trigger/trigger.py:104-158`; `plugins/evoontology-codex/AGENTS.md:62-68`.

>     for root in roots:
>         trigger = EvolutionTrigger(str(root))
>         trigger.initialize()
>         result = trigger.check()
>         if result["evolution_due"]:
>             label = root.name if root != base else "workspace"
>             reminders.append(
>                 f"EvoOntology: evolution is due ({result['reason']}) for {label}. "
>                 f"Run /evo-evolve to review and improve the ontology layer."
>             )
> --- `plugins/claude-code/scripts/check-reminder.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>                 "systemMessage": visible_message,
>                 "hookSpecificOutput": {
>                     "hookEventName": "SessionStart",
>                     "additionalContext": context,
>                 }
> --- `plugins/claude-code/scripts/check-reminder.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

RTE-4 — Evolution diagnosis, candidate patches and provisional validation. Trigger: user-requested evolution with eligible data; host Evolver reads prior records, current ontology/tools/Builder/runtime and evaluation setup, freezes objective/protocol/budget and creates/resumes an EvolutionSession. It should diagnose failure and missing coverage, compare competing causal explanations, choose one primary falsifiable mechanism, preserve parent and verify intended capability change before formal evaluation. Python begin_round records supplied hypothesis/candidate strings and enforces finite round budget; it does not perform that reasoning or prove activation. Candidate content is written separately; tool/schema/code edits use RTE-8. Source: SRC-1 `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:19-48,52-86,88-196`; `plugins/claude-code/skills/evo-evolve/SKILL.md:19-44,66-73`; `evoontology/evolution/session.py:102-163,195-214`. Host-mediated proposal/criticism conclusion status: afforded; state/budget implementation conclusion status: wired.

> 2. Convert the mechanism into a clear, falsifiable hypothesis describing:
>    * Current limitation;
>    * Why it causes the observed problem;
>    * Expected system behavior change if correct;
>    * Evidence that supports or falsifies the hypothesis.
> 3. Design the intervention based on project structure, evidence, and problem characteristics.
>    * Prefer solutions that directly test the hypothesis, have clear scope, and are reversible.
>    * Do not expand changes unnecessarily or repeatedly apply low-value patches.
> 4. Keep the primary intervention localized to the attributed Content, Tool, or Schema level.
>    * Multiple dependent components may be modified when all changes serve the same primary mechanism.
>    * Improvements must not come from permanently disabling, removing, or bypassing the ontology layer.
>    * Diagnostic ablation may serve as attribution evidence, not as the final successful solution.
> 5. Preserve the Parent and record Candidate changes, expected effects, and rollback methods.
> 6. Run representative cases, targeted replay, or low-cost exploratory experiments to verify that the Candidate changes the intended capability or behavior.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>         run = self._require_running()
>         if run["round"] >= int(run["budget"]["max_rounds"]):
>             self.mark_incomplete("budget_exhausted")
>             raise EvolutionBudgetExhausted(
>                 f"Budget exhausted after {run['round']} rounds; extend the "
>                 "budget (with user confirmation) or end the run"
>             )
>         run["round"] += 1
>         run["current_hypothesis"] = str(hypothesis or "")
>         run["current_candidate"] = str(candidate_version or "")
>         self._save_run()
>         return int(run["round"])
> --- `evoontology/evolution/session.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

Guidance is explicitly a theory route: the host must state a limitation, proposed cause, expected behavior change and evidence that could falsify it. Formulation and content-directed criticism: afforded by skill instructions; correct host execution: uninspected. Hypothesis string, reject notes and evidence references persist; the skills prescribe rereading prior causal understanding and disproven explanations. Operative use of those explanations rather than merely reading them: uninspected. Conditional content/code revision: afforded, with wired storage interfaces. An improvement in future capacity attributable to criticism: uninspected. Addressability is object/file/dimension/hypothesis granularity, with causal adequacy uninspected. Preference for cross-case reproducibility/testing value is instructed; a codified preference for explanatory reach among evidence-fitting hypotheses was not established by this gate.

RTE-5 — Paired evaluation, formal gate and version promotion/rejection/checkpoint. Trigger: host submits evaluation and requests accept on a running session's current candidate. Proposal and evaluative evidence originate with host/adapter; deterministic core validates content, selects latest matching round/candidate evaluation gate_input, demands unacceptable_regressions=False and optional frozen protocol match, then recomputes acceptance. Ground-truth mode requires nonempty equally sized finite numeric vectors and unique matching case_ids; candidate mean must exceed parent mean. Judge mode requires nonempty valid winners and Boolean critical_error; candidate must win more than parent with zero critical errors. Gate authority is arithmetic over supplied records. It does not establish evaluation provenance, matched models/budgets, independent validation, replication or regression truth merely because these fields were supplied. Source: SRC-1 `evoontology/evolution/session.py:287-322,390-450`; `evoontology/evaluation/evaluation.py:28-71`; `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:198-261`. Implementation conclusion status: wired; paired experiment correctness: uninspected.

>         supplied = next((s.get("gate_input") for s in summaries if s.get("gate_input")), None)
>         if not isinstance(supplied, dict):
>             raise EvolutionError("Record candidate evaluation gate_input before publication")
>         if supplied.get("unacceptable_regressions") is not False:
>             raise EvolutionError("Evaluation must explicitly rule out unacceptable regressions")
>         protocol = supplied.get("protocol")
>         expected = run.get("acceptance", {}).get("protocol")
>         if expected and protocol != expected:
>             raise EvolutionError("Gate protocol differs from the frozen acceptance protocol")
>         if protocol == "ground_truth":
>             parent = supplied.get("parent_scores", [])
>             candidate = supplied.get("candidate_scores", [])
>             cases = supplied.get("case_ids", [])
>             if not parent or len(parent) != len(candidate) or len(cases) != len(parent) or len(set(cases)) != len(cases):
>                 raise EvolutionError("Gate needs paired scores with unique matching case_ids")
>             if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in parent + candidate):
>                 raise EvolutionError("Gate scores must be finite numbers")
>             return EvaluationGate.decide_gt(parent, candidate)
>         if protocol == "llm_judge":
>             verdicts = supplied.get("verdicts", [])
>             if not verdicts or any(v.get("winner") not in {"parent", "candidate", "tie"}
>                                    or not isinstance(v.get("critical_error"), bool) for v in verdicts):
>                 raise EvolutionError("Gate needs nonempty valid judge verdicts")
>             return EvaluationGate.decide_judge(verdicts)
> --- `evoontology/evolution/session.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>     def decide_gt(parent_scores: List[float], candidate_scores: List[float]) -> Dict[str, Any]:
>         if not parent_scores or not candidate_scores:
>             raise ValueError("parent_scores and candidate_scores must be non-empty")
>         parent_avg = sum(parent_scores) / len(parent_scores)
>         candidate_avg = sum(candidate_scores) / len(candidate_scores)
>         return {
>             "accept": candidate_avg > parent_avg,
>             "parent_score": parent_avg,
>             "candidate_score": candidate_avg,
>             "delta": candidate_avg - parent_avg,
>             "protocol": "ground_truth",
> --- `evoontology/evaluation/evaluation.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>             if verdict.get("critical_error"):
>                 e_c += 1
> 
>         accept = (e_c == 0) and (w_c > w_p)
>         return {
>             "accept": accept,
>             "candidate_wins": w_c,
>             "parent_wins": w_p,
>             "ties": ties,
>             "candidate_critical_errors": e_c,
>             "protocol": "llm_judge",
> --- `evoontology/evaluation/evaluation.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

On acceptance, content is copied to a new official name, active is switched, checkpoint advances, then run status is saved. Reject appends a hypothesis/metrics/artifact/notes summary and stays running. Incomplete stops do not switch active/checkpoint; certain external-stop reasons require a minimum rejected count, while interruption/permission reasons can stop immediately. Finalize refuses running status. Formal copy publication refuses differing preexisting official content, but the multi-file accept sequence does not constitute a whole-system transaction and RTE-7 bypasses this route. Recovery is explicit resume and safe identical destination reuse; changed schema/tool code requires separate rollback. Source: SRC-1 `evoontology/evolution/session.py:179-191,236-270,390-417,452-489`; `evoontology/ontology/store.py:179-197`.

>         # Validate the Candidate loads before anything else changes.
>         SemanticStore.load_version(self.workspace, candidate)
>         target = str(new_version or "").strip() or self._next_official_version()
>         SemanticStore.publish(self.workspace, candidate, target)
>         EvolutionTrigger(str(self.workspace)).advance_checkpoint()
>         run["status"] = ACCEPTED
>         run["accepted_version"] = target
>         run["end_reason"] = ""
>         run["gate"] = gate
>         self._save_run()
> --- `evoontology/evolution/session.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

Answer-oracle access is mode-specific. Ground-truth mode takes caller-provided score vectors; skill doctrine reserves expected answers for an external evaluator and forbids Builder/Evolver reading them. The core neither obtains expected answers nor attests the score function. Judge mode uses a model comparison without requiring a reference answer; EvaluationGate only aggregates supplied verdicts. Anonymize/decode helpers exist, but the returned mapping must be handled correctly by the external caller. Actual blinded judging and repeated trials are uninspected. Benchmark wrappers return metrics/cases/artifact paths and leave formal gate_input construction to the caller. RTE-5 permits comparison-based revision for the named task set; it is not a proof of individual semantic claims or causal attribution.

For RTE-5, candidate evaluation is not bound to content bytes by a digest in the inspected gate. build_experience hides open-run evaluation summaries, but this display filtering is not a role permission boundary over raw files/core operations. Candidate annotations live under reports/<candidate>.json; content copying does not rename them to reports/<official>.json, so later official-version display need not carry the same annotations. Source: SRC-1 `evoontology/evolution/session.py:419-450`; `evoontology/workflow.py:299-352`; `evoontology/ontology/store.py:179-197`. The data-boundary reference broadly says to advance checkpoint after a completed evolution run; the explicit skill/session preserve it on Incomplete and advance on Accept. That narrower implemented behavior governs this account. Source: SRC-1 `plugins/evoontology-codex/skills/evolve-ontology/references/ontology-layer-data-boundary.md:137-138`; `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:291-298`; `evoontology/evolution/session.py:410-411,486-489`.

>     report = read_json(root / "reports" / (safe_id(version) + ".json"), {})
> --- `evoontology/workflow.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

> After an evolution run completes, update the evolution checkpoint so the same
> trajectory batch is not reused as a new evolution cycle.
> --- `plugins/evoontology-codex/skills/evolve-ontology/references/ontology-layer-data-boundary.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

RTE-6 — Plugin/stdio MCP entry and operation dispatch. Trigger: configured host launches MCP and sends JSON-RPC. tools/list advertises semantic and operation tools; tools/call dispatches browse/resolve or any named operation handler, catches exceptions into JSON error results, and returns serialized data. Caller may specify workspace/version. Source: SRC-1 `evoontology/runtime/mcp_server.py:51-143`; `evoontology/runtime/ops.py:238-279`; `plugins/evoontology-codex/AGENTS.md:8-32`. Implementation conclusion status: wired. Capability surface includes query, record, version mutation, lifecycle and visualization; actual host grants/approval are uninspected. The server's operation list is not a read-only semantic-only grant. External host shell/Python/file tools provide material alternatives to MCP enforcement.

RTE-7 — Direct low-level version save/active switch and Python promote/publish alternatives. Trigger: MCP save_version/set_active_version or direct library caller. save_version overwrites the five files for a requested name after list-type checks; set_active checks only directory existence. Legacy promote replaces an existing destination; publish protects differing existing content but does not itself run EvaluationGate. Thus formal evolution publication is one admission mechanism, not a universal prerequisite for changing operative content. Owners/proposers: caller supplies records/version; local store performs writes. Rejection/rollback: limited type/path/existence or destination equality checks; prior versions/explicit active switch may recover content, but overwrite can lose it. Source: SRC-1 `evoontology/runtime/ops.py:98-114,238-255`; `evoontology/ontology/store.py:122-197`. Implementation conclusion status: wired. Guidance is caller-supplied policy/knowledge, whose theory and evidence quality is uninspected on this path.

>         root = ensure_workspace(path)
>         version_dir = root / "versions" / version
>         version_dir.mkdir(parents=True, exist_ok=True)
>         for family, (filename, _) in _FAMILIES.items():
>             items = records.get(family, [])
>             if not isinstance(items, list):
>                 raise TypeError(f"records[{family!r}] must be a list")
>             (version_dir / filename).write_text(
>                 json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
>             )
> --- `evoontology/ontology/store.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

>     def set_active(cls, path: Optional[PathLike], version: str) -> None:
>         """Point ``active.json`` at ``version``."""
>         root = ensure_workspace(path)
>         version_dir = root / "versions" / version
>         if not version_dir.is_dir():
>             raise FileNotFoundError(f"Semantic version missing: {version_dir}")
>         active_file = root / "active.json"
>         active_file.write_text(
>             json.dumps({"active_version": version}, ensure_ascii=False, indent=2),
>             encoding="utf-8",
>         )
> --- `evoontology/ontology/store.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

RTE-8 — Host-mediated Schema/Tool/prompt/workflow/runtime revisions. Trigger: causal attribution to representation, tool or workflow limitations. Both host evolve skills authorize localized related component edits, require a primary hypothesis and recorded rollback, then prescribe capability and paired tests. Python content-version copy moves only five content families; it is not a snapshot/rollback mechanism for arbitrary code or instructions. Proposal, file-write admission, capability grants and rollback belong to the external host/operator environment. Source: SRC-1 `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:11-17,139-196,270-298`; `plugins/claude-code/skills/evo-evolve/SKILL.md:11-17`; `evoontology/ontology/store.py:22-37,179-197`. Revision conclusion status: afforded. Semantic theory guidance inherits RTE-4's afforded formulation/criticism, uninspected operative reasoning and uninspected capacity benefit; code execution/activation beyond the shipped source is not observed. These edits can make the layer's own behavior change, distinct from external query-answer output.

> Evolution operates along three dimensions — **Content, Tool, and Schema**.
> When the attributed mechanism involves related prompt, workflow, or runtime
> components, they may be modified as part of the corresponding evolution
> dimension.
> 
> All Candidate changes must be traceable to their target dimension and
> reversible to the Parent state.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

RTE-9 — Bounded SQLite execution and explicit external-tool observation. Trigger: running recorded task with an absolute SQLite file path and query, or caller records another tool's result. The built-in path opens SQLite mode=ro, limits large values, authorizes SELECT/READ/FUNCTION/RECURSIVE except load_extension, limits progress, returns at most 100 rows plus truncation flag and records event/error. Other environments rely on host native tools and caller-supplied event data. Principal is the requesting host; executor is local SQLite for the built-in branch, external tool otherwise. Source: SRC-1 `evoontology/workflow.py:189-230,239-286`; `plugins/evoontology-codex/AGENTS.md:78-84`. Implementation conclusion status: wired read-only query and event persistence. Guarantee owner is SQLite URI/authorizer/progress boundary; strength local invariant over that branch, not an external-tool or filesystem-wide guarantee. Returned data is observation evidence with source/query scope, not an ontology interpretation by itself.

>         connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
>         if hasattr(connection, "setlimit"):
>             connection.setlimit(sqlite3.SQLITE_LIMIT_LENGTH, 1_000_000)
>         # Read-only URI prevents writes; authorizer also prohibits attachments,
>         # pragmas and extension loading. Progress limit bounds expensive scans.
>         allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION,
>                    sqlite3.SQLITE_RECURSIVE}
>         def authorize(action, arg1, arg2, database_name, trigger):
>             if action == sqlite3.SQLITE_FUNCTION and str(arg2).lower() == "load_extension":
>                 return sqlite3.SQLITE_DENY
>             return sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY
>         connection.set_authorizer(authorize)
>         calls = 0
>         def progress():
>             nonlocal calls
>             calls += 1
>             return int(calls > 1000)
>         connection.set_progress_handler(progress, 1000)
> --- `evoontology/workflow.py` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

### Claims

CLM-1 — README says ontology content is workload-grounded, continuously adapts from execution trajectories and exposes active semantic access. Claim conclusion status: claimed. Source: SRC-1 `README.md:27-30,60-72`. RTE-2 and RTE-3 implement storage/access/recording; RTE-4 depends on host invocation and skill execution. A due reminder is not a launched autonomous evolution loop.

> EvoOntology is the first self-evolving ontology layer for data agents, aiming to bridge the **agent-data gap** over heterogeneous tables, files, and databases. It exposes a versioned **Ontology Layer through MCP tools**, grounds that layer in real workload evidence, and continuously adapts it from execution trajectories.
> - 🔌 Universal Agent Plugin as MCP: Seamlessly integrates with Claude Code, Codex, and other AI agents.
> - 🤖 Automatic Ontology Construction: Builds a tailored ontology layer directly from your data.
> - ♻️ Continuous Self-Evolution: Continuously evolves and refines the ontology layer based on interaction history.
> --- `README.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

CLM-2 — README says semantic objects commit after data verification and candidates publish only after paired reproducible improvement. Claim conclusion status: claimed. Source: SRC-1 `README.md:64-68,110-114`. Builder/evolver doctrine prescribes semantic verification and controlled evaluation; deterministic validation is structural, formal gate accepts supplied evidence, and RTE-7 provides alternate mutation. The claim holds only as a compliant workflow expectation with external contracts, not a universal enforced publication guarantee.

> | **Active access** | Retrieve only the semantics needed for the current step through MCP tools instead of injecting the full ontology. |
> | **Grounded construction** | Build around the workload and commit semantic objects only after verification against the underlying data. |
> | **Targeted evolution** | Diagnose interaction trajectories and apply localized updates to the interconnected Content, Schema, and Tool Layers. |
> | **Gated versioning** | Publish a Candidate only when paired evaluation shows a reproducible improvement over its Parent. |
> | **Agent integration** | Connect the ontology workspace and MCP runtime directly to supported agents through plugins. |
> --- `README.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

CLM-3 — README reports aggregate gains over ReAct on DDR-Bench, InsightBench and BIRD across a named four-backbone analysis subset. Claim conclusion status: claimed. Source: SRC-1 `README.md:158-180`. The repository report is not an observed run or causal intervention in this analysis; no particular semantic mechanism's effect is established.

> Across the four-backbone analysis subset, the builder-constructed **Initial Ontology Layer** improves over **ReAct without an Ontology Layer**, and self-evolution produces a further gain with **EvoOntology** on all three benchmarks.
> 
> | Benchmark | Primary metric | ReAct without Ontology Layer | Initial Ontology Layer | EvoOntology | Gain over ReAct |
> | --- | --- | ---: | ---: | ---: | ---: |
> | DDR-Bench (10-K) | Trajectory-Wise | 69.5 | 81.8 | **89.5** | **+20.0** |
> | InsightBench | Insight | 53.2 | 54.0 | **54.2** | **+1.0** |
> | BIRD | Execution Accuracy (EX) | 63.6 | 68.7 | **72.4** | **+8.8** |
> 
> <p align="center"><sub>Results use the four-backbone analysis subset in the <a href="https://arxiv.org/abs/2609.15779">paper</a>: GPT-5.5, GPT-5.6-sol, Claude-Sonnet-5, and Claude-Opus-4.8. DDR-Bench values are reported directly in Tables 2 and 8; InsightBench and BIRD values are one-decimal means of the Figure 3 scores and match the stage gains stated in the accompanying analysis. See Tables 1, 3, and 4 for the full six-backbone results and evaluation protocols.</sub></p>
> --- `README.md` @ `ddbb1c991de5a33e27eb32bc86a4212a7537e01e`

### Evidenced absences

None asserted. Uninspected host execution, provider internals, data truth and causal experiments are explicit limitations, not absence records.

### Behavioral-authority paths

BAP-1 — Data Agent consumes returned semantic objects and manifest through MCP/tool/resource text. Force: advisory knowledge and navigation instruction; horizon current analytical step/task. It must query/validate actual data under host doctrine. Constraint severity labels do not themselves block native SQL. Source: SRC-1 `evoontology/runtime/runtime.py:143-149,262-329`; `plugins/evoontology-codex/AGENTS.md:51-56`; RTE-2.

BAP-2 — Builder/Evolver consumes shipped skills, stored ontology, trajectories, prior hypotheses/notes and evaluation evidence through host context/file/tool reads. Force: instruction plus advisory evidence; horizon build or bounded evolution run and future rounds. Source: SRC-1 `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md:28-48,88-196,234-289`; RTE-1, RTE-3, RTE-4, RTE-8. Host following and actual criticism unobserved.

BAP-3 — EvolutionSession consumes gate_input scores/verdicts and validation result. Force: formal accept/reject enforcement and publication; horizon current candidate/round. Epistemic authority limited to consistency of supplied values and accepted protocol. Source: SRC-1 `evoontology/evolution/session.py:390-450`; RTE-5.

BAP-4 — Later semantic loads consume active.json or requested/task-pinned version and lifecycle state. Force: routing/selection of operative content; horizon subsequent call. Alternate pointer/content writes can change this without formal gate. Source: SRC-1 `evoontology/ontology/store.py:63-118,145-155`; `evoontology/runtime/mcp_server.py:75-89`; RTE-2, RTE-7.

BAP-5 — Host/session receives evolution reminder and status. Force: advisory invocation prompt, not automatic start. Claude hook supplies context/status; Codex asks host to check and remind. Source: SRC-1 `plugins/claude-code/scripts/check-reminder.py:24-65`; `plugins/evoontology-codex/AGENTS.md:62-68`; RTE-3.

BAP-6 — SQLite executor consumes query and authorizer rules. Force: deterministic operation restriction and bounded results; horizon one built-in query. Does not restrict independent host tools. Source: SRC-1 `evoontology/workflow.py:239-286`; RTE-9.

## Runtime account

An ordinary Codex build starts from a user's analytical goal. The host reads the build skill, resolves/persists project mode and data boundary, prepares questions, explores data and proposes semantic records. It invokes save_version, annotate_ontology_version and publish_ontology_build. The last command checks structural validity, activates the initial content and initializes trigger state. Data tasks explicitly start a record pinned to an ontology version, request semantic resolution, execute read-only SQLite or host tools, record observed outputs and finish a trajectory. Semantic use alone is not a complete trajectory recorder. Future requests pull retained semantic content, and session reminders can advertise accumulated evolution work.

A requested evolution resumes an open run or creates one with parent/protocol/budget. Host reasoning diagnoses and attributes problems, writes a candidate, submits external paired evaluation and calls formal acceptance. Rejected candidates leave the session running and should change the next hypothesis; accepted content becomes active and advances checkpoint; incomplete leaves those unchanged. Formal terminal checking is wired, but evidence generation, matched conditions, replication, semantic criticism and continuation scheduling depend on the host skill. Codex reuses authorized budgets and announces quick/full profiles; Claude's inspected skill asks explicit budget/source confirmation. These are host policies, not checks that the core verifies happened.

Material alternatives are semantic-only use, direct MCP operation calls, Python store APIs, host file/code changes, external tool observations, native SQLite, and three benchmark subprocess adapter wrappers. The two plugin core copies are byte-identical; host instructions and hooks differ. Runtime loop responsibilities stop at returned MCP data/state or external adapter result. No own autonomous LLM scheduler is inferred from evolution-trigger state. The capability surface includes local path selection/read/write, SQL read, model-dependent host operations and external benchmark subprocesses; actual credentials, host approvals, OS permissions and complete tool grants are uninspected. Bounds on SQL or returned semantic objects do not form a deployment-wide isolation guarantee.

For diagnosis/proposal the host model and user supply interpretation and scope; deterministic code stores hypotheses and rejects some invalid structures. For comparison/admission the external evaluator supplies scores/judgments, the host supplies gate records, and Python recomputes arithmetic/predicate veto. Humans may veto costs/scope through host policy. Expected-answer access belongs only to configured ground-truth evaluators when that mode is chosen; a judge model is not automatically an answer oracle. Modes are fixed-split benchmark/workload experiments and rolling-trajectory project use, with distinct design/validation separation obligations. The source's record checks do not prove those obligations were followed.

| Static forcing case | Route/anchor | Supported consequence and limit |
|---|---|---|
| Missing/malformed gate input or protocol mismatch | RTE-5, SRC-1 `evoontology/evolution/session.py:419-450` | Formal accept refuses missing/no-regression assertion, unpaired/nonfinite scores or malformed verdicts. It evaluates supplied records, not provenance truth |
| Direct active switch or overwrite | RTE-7, SRC-1 `evoontology/ontology/store.py:122-197` | Operative content can change outside formal gate; existence/type checks differ from semantic/evaluation checks |
| Query write/extension or overlarge result | RTE-9, SRC-1 `evoontology/workflow.py:254-285` | Read-only URI/authorizer/progress/row limits bound built-in query; external native tools have separate grants |
| Rejection, budget or interruption | RTE-4, RTE-5, SRC-1 `evoontology/evolution/session.py:195-214,236-270,452-489` | Reject remains running; begin_round enforces budget; supported incomplete reasons can end without pointer/checkpoint change. Host supplies actual continuation |

Execution preflight: **no dynamic check planned**. Considered a gate-record fixture, direct-pointer fixture and native SQLite replay. Static source makes the admission and responsibility boundaries inspectable without executing the project. No host model, MCP server, benchmark subprocess, database, credentials or target test was invoked; no unexecuted check is counted as a failure or observed effect.

| Route | Immediate return | Later read-back/delegated visibility | Selection predicate | Invalidation/expiry | Activation/effect limit |
|---|---|---|---|---|---|
| RTE-1 | Published initial version/presentation or validation error | Content served to later agents; known limitations/reports retained | Explicit workspace/version and structural validity | Existing active workspace blocks this initial path; RTE-7 alternatives differ | Wired publication, afforded semantic construction; data truth uninspected |
| RTE-2 | Bounded objects/manifest/status | Explicit requests read changed content; host receives tool text | Query/mention/context/version and active lifecycle filtering | Active/version/lifecycle changes alter selection; semantic expiry not inferred | Return wired, correct application/benefit uninspected |
| RTE-3 | Saved event/task/status/reminder | Histories/questions/trajectories enter later workload/evolution; host reminder visible | Data source, split, origin, normalized question, checkpoint/trigger | Marked heldout/test data excluded by selected preparation branch; caller correctness external | Recording/selection wired; whole trajectory truth and automatic evolution uninspected |
| RTE-4 | Candidate/round state or budget refusal | Host skill calls for prior hypotheses/problems/rejections before next proposal | Parent/run/candidate IDs and budget; semantic prioritization host-owned | Superseded hypothesis/candidate can be retained in reject record; explicit incomplete stops | State wired, reasoning/criticism afforded |
| RTE-5 | Accepted version or gate error; reject/incomplete/final state | New active content and run/evaluation records affect later calls/runs | Latest matching round/candidate gate input plus protocol predicate | Formal reject/incomplete retains parent; content-copy retry only if identical | Admission wired; matched experiment/reproducibility uninspected |
| RTE-6 | JSON-RPC result/error/resource | Host consumes tool output; each semantic call can reload version | Advertised tool name/workspace/version | Request error rejects operation; external host lifecycle unknown | Dispatch wired, host response uninspected |
| RTE-7 | Saved path/active version | Next active load can immediately see changed records | Caller-selected name; types/existence or publish destination equality | Explicit pointer rollback possible; overwritten bytes not automatically retained | Direct change wired; no formal evolution warrant follows |
| RTE-8 | Host edit/test result outside core | Later runtime/prompt/schema can consume changed code/instructions | Host hypothesis, file capabilities and policy | Rollback required by skill, not supplied by content active pointer | Edit affordance; actual deployment/recovery uninspected |
| RTE-9 | Query output/error or external-event acknowledgement | Persisted tool evidence feeds task finalization and later analysis | Running task, event ID, DB path and authorizer | Duplicate conflicting event rejected; result truncation loses detail | Built-in observation wired; externally reported observation truth uninspected |

## Lens scoping

### Memory/context scope

Full lens triggered by versioned semantic content, recorded task/evaluation evidence and later evolution use: OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6 and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9. Scope includes content/schema/tool representation, write/maintenance/retrieval, host-directed learning and lower-level mutation alternatives; excludes benchmark runtime interiors and provider state. Fresh input SHA-256 `d72c9bac738e612b710cedbe48171c90c2a198b49351c393658551b6d2d83e1c`. Static shipped skills are doctrine, not accumulated memory.

### Epistemic scope

Full lens triggered by grounding/causal-attribution/evaluation claims CLM-1, CLM-2, CLM-3 and semantic/evidence/hypothesis objects. Standalone epistemic procedure executed locally over SRC-1 and all material routes, separating semantic claim creation from structural checking, score aggregation, operational reliance and read-back. Host reasoning, underlying data correctness, reference answers and observed effect remain outside established evidence.

## Lens outputs

### Memory/context lens

The fresh specialist's mapped fourteen-axis profile is in frontmatter. Its complete report was checked against run identity, SRC-1 pin, boundary, input and method digests; its exact SHA-256 is in Run identity. The report is provenance, while all adopted material findings are retained here on canonical records.

The core retains semantic meanings and evidence in files and loaded dictionaries, then supplies lexical/identifier-selected entries through requested tool calls. Graph describes content topology, not a graph database; SQLite is the inspected environment. OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6 and OBJ-7 include prose and symbolic fields/code. Initial static instructions are excluded from learned memory; trace-derived changes to those instructions or code under RTE-8 are included.

Acquisition and derivation differ. RTE-3 and RTE-9 record/truncate raw evidence; RTE-1 extracts and deduplicates questions for later construction. These alone are not semantic learning. The qualifying trace-fed routes are RTE-4 and RTE-8: an invoked host transforms task/tool evidence into semantic claims, causal explanations and code/prompt/schema revisions, then later data-agent or Evolver calls can consume them. Trace learning is therefore yes at afforded basis, across tasks within a project, offline and staged, with natural-language and symbolic outputs. It does not establish observed conjectural learning or improved capacity. No opaque provider-memory or hypothetical compaction branch is included.

RTE-2 supplies pull retrieval, and RTE-4 prescribes later pull of previous explanations. RTE-3 supplies Claude's coarse push of due summaries; Codex's status call remains requested. Identifiers and lexical queries are pull selectors, not extra push signals. The same scope governs every comparison axis, including low-level writes and afforded host code/instruction edits. Semantic returns have knowledge force; retained state can route/rank, gate input can enforce admission, and revised code/instructions can carry other force at their particular consumer. Those consumers must not be conflated.

Content and rationale continuity are partial. Linked Evidence fields are returned, but full mapping validation/history is not universally supplied; OBJ-7 retention/read-back is richer in host doctrine than core fields. Content pointers do not restore prior Schema/Tool code, and candidate annotations are not automatically renamed on official publication. Faithfulness remains not determinable: instructed activation tests and reported benchmark gains do not supply an observed content-dependence intervention. These bounds preserve the specialist's findings without upgrading host affordances to executed learning.

### Epistemic lens

#### 1. Source-and-claim boundary

System/revision/scope: see Run identity, SRC-1 and Boundary and evidence. Question: what gives retained semantics or a proposed improvement warrant, and what permits later reliance? Assessed families: RTE-1 construction; RTE-2 serving; RTE-3 acquisition/trigger; RTE-4 diagnosis; RTE-5 formal evaluation/admission; RTE-6 dispatch; RTE-7 alternate writes; RTE-8 self-layer revision; RTE-9 observation. Excluded host reasoning/provider internals and full benchmark evaluators prevent certifying semantic criticism, evidence authenticity, whole-agent execution and improvement. Claims: CLM-1, CLM-2 and CLM-3; evidence layers remain implementation, doctrine/design and attributed reported operation. No observed-run or causal source was inspected. Architectural status below is distinct from conclusion status; implemented means the code supports a route, not that an instance ran.

#### 2. Epistemic-object inventory

Generic identity, form and storage are canonical-owned; see the listed records. Heterogeneous aggregates OBJ-1, OBJ-4 and OBJ-6 are disposed through their registered parts, not reassigned.

| Object | Lineage and producer/consumer | Candidate truth-apt content and claimed role | Evidence and limit |
|---|---|---|---|
| OBJ-8 | See RTE-1, RTE-4; host to Data Agent | Proposed meaning/scope of a business term | SRC-1 models:57-79 via OBJ-1; structural typing does not verify meaning |
| OBJ-9 | See RTE-1, RTE-4; host to Data Agent | A source/filter/grain realizes a business concept | SRC-1 models:83-120 via OBJ-1; data reproduction remains host-owned |
| OBJ-10 | See RTE-1, RTE-4; host to Data Agent | Proposed relationship between terms | SRC-1 models:124-145 via OBJ-1; valid IDs do not establish the relation |
| OBJ-11 | See RTE-1, RTE-4; host to Data Agent | A factual restriction or a desired rule; instance needed to distinguish | SRC-1 models:149-175 via OBJ-1; severity is advisory under BAP-1 |
| OBJ-12 | Caller/native result to semantic record, then Data Agent/Evolver | What query/result/method was observed; evidential support for linked claims | SRC-1 models:178-196 via OBJ-1; external observation truth/interpretation unverified |
| OBJ-13 | Caller/history/generated question to Builder/task recorder | Questions themselves have no asserted answer; provenance asserts origin | RTE-1, RTE-3 anchors; generated question support requires interpretation |
| OBJ-14 | Native SQLite or external host, then later Evolver | Observable output/error and final-answer assertions | RTE-3, RTE-9 anchors; clipping loses detail, external answer generation excluded |
| OBJ-7 | Host diagnosis from traces, then later Evolver | Hypothesis about limitation, cause, predicted effect and falsifier | RTE-4 anchors; actual reasoning/operative use uninspected |
| OBJ-15 | External evaluator/host to session gate | Score/verdict/provenance/no-regression assertions about a comparison | RTE-5 anchors; supplying them does not attest the comparison |
| OBJ-16 | Deterministic gate/session to publication/state reader | Predicate over recorded inputs; terminal status is operational disposition | RTE-5 anchors; formal arithmetic warrants no wider explanation |
| OBJ-2 | Shipped or revised schema to parser/host | Representation policy/code; no required candidate truth-apt output | RTE-8 anchors; hypothesized benefit is OBJ-7 rather than inferred from code |
| OBJ-3 | Runtime/registry to host; possible host revision | Access behavior and instructions; manifest counts derive from loaded records | RTE-2, RTE-8 anchors; counts describe store state, not truth of content |
| OBJ-5 | Core/caller state to dispatcher/session/trigger | IDs, budgets, pointer and lifecycle controls; hypothesis content separately OBJ-7 | RTE-3, RTE-5, RTE-7 anchors; operational status is not epistemic endorsement |

The shorthand models anchors in this table refer to the full SRC-1 path `evoontology/ontology/models.py` already quoted on OBJ-1; no additional source identity is introduced.

#### 3. Authority-route ledger

Every row has one functional kind. Generic endpoints/context/persistence are in the canonical route; BAP references specify consumer/channel/force/horizon. All rows are static architectural findings with no observed candidate execution. A mismatch marker of none means no additional mismatch beyond its explicit limit.

| Route / function | Architectural status; content/update relation | Target, evaluator/condition, timing and result | Epistemic license; operational force and authority path | Evidence, claim, mismatch and limit |
|---|---|---|---|---|
| RTE-1 / content transformation | doctrine only; truth-apt transformation: ampliative conjecture | OBJ-8, OBJ-9, OBJ-10 and truth-apt OBJ-11; Builder interprets workload/data at build time | Proposed semantics, not established truth; later advisory use BAP-1, authoring instruction BAP-2 | Build skill:137-201 on RTE-1; CLM-1, CLM-2; mismatch: code does not synthesize or certify meaning |
| RTE-1 / check/evidence production | doctrine only; no content change | Same semantic candidates; reproduce data, compare alternatives and coverage before publish | May support named scope if performed; host veto/revise under BAP-2 | Build skill:137-171,209-229 on RTE-1; CLM-2; no observed probes |
| RTE-1 / check/evidence production | implemented; no content change | Candidate five-file content; validator checks lists/IDs/references/loadability | Structural consistency only; validation result can block initial publication BAP-3 | validate:64-147 on RTE-1; CLM-2; mismatch: structural success is not semantic verification |
| RTE-1 / disposition/acceptance | implemented; no content change | Valid initial candidate and no existing active workspace; publisher accepts operational deployment | Intended use initial project semantics; operational grant, not truth endorsement; BAP-4 | ops:218-229 on RTE-1; CLM-2; semantic warrant external |
| RTE-1 / lifecycle integration | implemented; no content change | After initial publication, selected content becomes loadable via active pointer | Integrates operationally admitted content for later retrieval; BAP-4 then BAP-1 | RTE-1 anchors; CLM-1; no observed candidate-linked integration |
| RTE-2 / operational admission/selection/consumption | implemented; no content change | OBJ-8, OBJ-9, OBJ-10, OBJ-11, OBJ-12; query, IDs, active state and lexical/context match select returns | Relevance/eligibility only; supplies advisory knowledge BAP-1 and routing BAP-4 | runtime:155-219,262-479 on RTE-2; CLM-1; supported coverage means available links, not truth |
| RTE-2 / content transformation | implemented; truth-apt transformation: entailed derivation | OBJ-3 manifest counts/version from loaded store at request | Descriptive count/version within store semantics; no endorsement of content; BAP-1 | runtime:96-151 on OBJ-3; CLM-1; exact source state controls premise |
| RTE-3 / content transformation | implemented; truth-apt transformation: acquisition/import | OBJ-14 supplied observable records; recorder accepts caller data or wrappers' results | Preserves attribution-shaped inputs, truth unknown for caller events; BAP-2 later evidence | workflow:168-230 on RTE-3; CLM-1; external capture completeness unknown |
| RTE-3 / content transformation | implemented; truth-apt transformation: non-ampliative reshaping | OBJ-14 observable message extraction and prefix truncation; OBJ-13 normalized question dedup | Keeps selected provenance, degrades completeness; does not derive general semantics; BAP-2 | trajectory:22-102 and workflow:62-166 on OBJ-4/RTE-3; CLM-1; lost suffix unrecoverable from record |
| RTE-3 / retention | implemented; no content change | OBJ-13 and OBJ-14 persisted by task/question/trajectory writes | Availability only, not acceptance; later host read BAP-2 | RTE-3 anchors; CLM-1; explicit host recording required |
| RTE-3 / operational admission/selection/consumption | implemented; non-truth-apt policy/content update: due reminder | Retained count/time/checkpoint at Claude SessionStart; due status selected | Advisory invocation cue BAP-5; no semantic warrant or automatic evolution | trigger/hook anchors on RTE-3; CLM-1; Codex branch doctrine only |
| RTE-4 / content transformation | doctrine only; truth-apt transformation: ampliative conjecture | OBJ-7 and proposed semantic revisions; Evolver diagnoses eligible traces and compares causal explanations | Candidate causal/semantic theory; no automatic warrant; BAP-2 | Evolve skill:88-196 on RTE-4; CLM-1; formulation afforded, execution uninspected |
| RTE-4 / check/evidence production | doctrine only; no content change | OBJ-7 predicted mechanism/effect; representative replay, capability test and falsifier | Potential content-directed criticism within stated test scope; BAP-2 informs revise/continue | RTE-4 anchors; CLM-2; a stated test is not evidence it ran |
| RTE-4 / retention | implemented for hypothesis/reject fields, doctrine only for rich causal reports; no content change | OBJ-7 string/notes/reference plus host problem maps; persist during rounds/rejects | Keeps explanation/history for later host diagnosis BAP-2; no intrinsic acceptance | session:195-214,236-270 and skill:234-289 on OBJ-7; CLM-1; empty strings allowed |
| RTE-4 / behavior/policy adaptation | doctrine only; non-truth-apt policy/content update: change next intervention after criticism | Host updates candidate/reliance from revised problem map | Conditional future hypothesis/action choice BAP-2; content critique and improvement not observed | RTE-4 and OBJ-7 anchors; CLM-1; not inferred from storage |
| RTE-5 / content transformation | implemented; truth-apt transformation: acquisition/import | OBJ-15 host evaluation results normalized into session | Retains supplied score/verdict assertions, unknown external warrant; BAP-3 later consumes | session:287-322 on RTE-5; CLM-2; no source authentication/content digest |
| RTE-5 / check/evidence production | implemented; truth-apt transformation: entailed derivation | OBJ-16 computed from OBJ-15: paired finite scores/unique IDs/protocol/no-regression assertion or valid judge verdicts | Correct gate predicate within supplied numbers/booleans; no claim of matched experiment; BAP-3 | session:419-450 and evaluation:28-71 on RTE-5; CLM-2; mismatch: record validity versus experimental validity |
| RTE-5 / disposition/acceptance | implemented; no content change | Current candidate passes structure and gate; accept for later project use, or gate error/reject/incomplete | Operational successor criterion: higher mean or more candidate wins without critical errors; BAP-3 | session:390-450 on RTE-5; CLM-2; no per-claim semantic acceptance follows |
| RTE-5 / retention | implemented; no content change | Normalized evaluations and run/reject records saved | Inspectable history/reliance inputs, not proof; BAP-2 and BAP-3 | session:236-270,287-322 on RTE-5; CLM-2; artifact paths can name external uncaptured evidence |
| RTE-5 / lifecycle integration | implemented; no content change | Accepted content copied to official version, active pointer/checkpoint updated | Later content selection BAP-4 then advisory BAP-1; formal-path acceptance precedes this transition | session:390-417 and store:179-197 on RTE-5; CLM-1, CLM-2; code/schema/report filename continuity not guaranteed |
| RTE-5 / lineage/freshness/recovery | implemented; no content change | Existing differing official destination refused; incomplete preserves active/checkpoint | Content recovery/progression only BAP-4; sequential writes are not full transaction | RTE-5 anchors; CLM-2; external code and alternate writes outside this protection |
| RTE-6 / operational admission/selection/consumption | implemented; no content change | Caller-selected listed operation dispatched; errors serialized | Capability access, no semantic license; BAP-1 through BAP-6 according to handler | MCP:51-143 on RTE-6; no independent claim; host role isolation uninspected |
| RTE-7 / retention | implemented; truth-apt transformation: acquisition/import | Caller content saved into possibly existing version files | Retains supplied assertions without formal gate; later BAP-4/BAP-1 | store:122-155 and ops:98-114 on RTE-7; CLM-2; mismatch: alternate write can bypass formal admission |
| RTE-7 / operational admission/selection/consumption | implemented; no content change | Named existing directory can become active | Permits later consumption BAP-4 without epistemic acceptance; not lifecycle integration | RTE-7 anchors; CLM-2; pointer switch proves no semantic test |
| RTE-7 / lineage/freshness/recovery | implemented; no content change | Pointer switch, promote overwrite, publish destination comparison | Caller-directed content recovery/mutation BAP-4, no historical immutability guarantee | store:158-197 on RTE-7; CLM-2; overwritten content may be lost |
| RTE-8 / behavior/policy adaptation | doctrine only; non-truth-apt policy/content update: Schema/Tool/prompt/code patch | Host uses OBJ-7 diagnosis to choose localized edits and rollback method | Can change later capabilities/selection/instructions BAP-2; code changes do not themselves formulate truth | Evolve skill:11-17,139-196 on RTE-8; CLM-1; actual host write admission external |
| RTE-8 / check/evidence production | doctrine only; no content change | Candidate mechanism and claimed benefit; instructed capability, paired and regression tests | Limited by experiment design if executed; host can reject BAP-2 | RTE-4, RTE-5, RTE-8 anchors; CLM-2; formal content gate does not cover all code state |
| RTE-8 / lineage/freshness/recovery | doctrine only; no content change | Parent preservation/reversible file edits | Host-managed recovery obligation BAP-2; active pointer recovers content only | RTE-8 anchors; CLM-2; schema/tool current-code views prevent inferring historical snapshot |
| RTE-9 / check/evidence production | implemented built-in, doctrine only external execution; truth-apt transformation: acquisition/import | OBJ-14 native SQLite query output, or external tool observation supplied by host | SQLite directly produces bounded data evidence; arbitrary supplied observation truth unknown; BAP-6/BAP-2 | workflow:239-286 on RTE-9; CLM-2; observed data does not entail semantic interpretation |
| RTE-9 / operational admission/selection/consumption | implemented; no content change | SQL authorizer, read-only URI and bounds restrict built-in query | Permits bounded read and blocks specified operations BAP-6; operational safety not epistemic truth | RTE-9 anchors; no independent claim; no host-wide isolation |

All shortened code locators in this ledger point through the corresponding canonical record to full SRC-1 paths and retained quotations. No second source or record register is implied.

#### 4. Per-object lifecycle disposition

For OBJ-8, OBJ-9 and OBJ-10, the instructed Builder/Evolver interpretation route is **ampliative conjecture**: semantic meaning/mapping/relationship does not follow merely from a query result. No candidate instance was inspected. Each object has the following separate phase dispositions: observation/anomaly RTE-9 implemented for SQLite and RTE-3 implemented recording, with host diagnosis RTE-4 doctrine only; conjecture RTE-1/RTE-4 doctrine only; derived consequence RTE-4 doctrine only; test/evidence RTE-1/RTE-4 doctrine only for semantic testing and RTE-5 implemented for supplied-score arithmetic; acceptance RTE-1 implemented structural initial admission and RTE-5 implemented bundle successor choice; lifecycle integration RTE-1/RTE-5 implemented content activation followed by RTE-2 retrieval. **Observed candidate state: no instance observed for every phase of each object.** Accepted scope would be the named project/version for later analytical use, not universal truth or separate verification of every statement. BAP-1, BAP-2, BAP-3 and BAP-4 govern the transitions. Sources: their canonical records and RTE-1, RTE-4, RTE-5. Missing evidence is candidate-linked semantic probes, actual formulation/criticism, comparison provenance and subsequent consumption.

For OBJ-7, transformation is **ampliative conjecture** about a limitation, cause, expected change and falsifier. No candidate instance was inspected. Observation/anomaly: RTE-3 implemented evidence capture plus RTE-4 doctrine only interpretation; conjecture: RTE-4 doctrine only; derived consequence: RTE-4 doctrine only; test/evidence: RTE-4/RTE-8 doctrine only capability/criticism tests plus RTE-5 implemented record predicate; acceptance: RTE-4 doctrine only validated/rejected mechanism bookkeeping, while RTE-5 implements candidate-bundle choice rather than accepting the causal explanation as such; lifecycle integration: RTE-4 doctrine only later reliance on retained causal knowledge. **Observed candidate state: no instance observed in every phase.** Intended scope is later project diagnosis/intervention; no accepted explanatory scope is evidenced. RTE-4 hypothesis/reject storage is retention, not acceptance or lifecycle integration. Source: OBJ-7/RTE-4 quotations; missing evidence is host reasoning, claim-directed criticism and attributable later capacity.

For OBJ-11, transformation is **indeterminate** without an instance. A supplied constraint may import a rule, conjecture a factual applicability restriction, or express a desired policy. Preserved lineage is whatever source/evidence references the host supplied; RTE-1 checks structure, RTE-2 serves it, RTE-4 may revise it and RTE-5 selects a bundle. A block label is not native-tool enforcement. Needed evidence: an actual rule, its domain/provenance, test and consuming action. No factual discovery lifecycle is imposed on a policy.

For OBJ-12, applicable transformation is **acquisition/import**, with possible non-ampliative formatting. Discovery lifecycle: not applicable for recording attributed observations. Warrant is the original query/result/method scope, unknown for externally supplied truth and degraded if the underlying result was clipped. RTE-9, RTE-1 and RTE-2 acquire/store/return it; those routes do not derive the semantic interpretation it supports. Missing evidence: original capture and candidate-specific grounding relation.

For OBJ-13, question text has no candidate truth-apt answer. Its provenance assertions undergo acquisition/import and normalized deduplication, a non-ampliative reshaping under RTE-1/RTE-3. Discovery lifecycle: not applicable to those provenance fields. Correct origin/support remains unverified; generated questions need evidence references but no resulting answer truth is established.

For OBJ-14, observable tool records undergo acquisition/import then non-ampliative extraction/truncation under RTE-3/RTE-9; discovery lifecycle is not applicable to that recording. Final-answer content has **indeterminate** transformation because excluded host inference could copy, derive or conjecture it. Preserved lineage includes task/version/tool inputs and clipped outputs; checks establish completion-shaped records, not answer correctness. An actual host trace and claim-linked evidence would distinguish those possibilities.

For OBJ-15, transformation is **acquisition/import** followed by non-ampliative normalization. Discovery lifecycle: not applicable to storing supplied evaluation assertions. RTE-5 retains origin-shaped fields and numeric cases; their warrant remains with excluded evaluators. Missing evidence: raw comparison, reference/judge provenance, design isolation and candidate-byte binding.

For OBJ-16, transformation is **entailed derivation** of the gate predicate within finite supplied values and explicit flags. Discovery lifecycle: not applicable. RTE-5 implements pairing/form checks, arithmetic and terminal transition. This licenses only the predicate over recorded inputs; it cannot transfer supplied-score truth to an explanatory mechanism, matched-condition claim or future transfer claim.

For OBJ-3, manifest counts/version undergo **entailed derivation** from loaded state under RTE-2; discovery lifecycle: not applicable. Premises are that loaded store, not the factual truth of stored claims. No lifecycle record for OBJ-3's tool behavior/instruction part: no candidate truth-apt output for that part; direct adaptation route RTE-8.

No lifecycle record for OBJ-2: no candidate truth-apt output for this object; relevant direct-adaptation or update route RTE-8. No lifecycle record for OBJ-5's operational state: no candidate truth-apt output for that part; relevant update routes RTE-3, RTE-4, RTE-5 and RTE-7. Its hypothesis content is separately disposed as OBJ-7. OBJ-1, OBJ-4 and OBJ-6 are aggregates whose per-part dispositions are supplied above.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design and source | Implemented routes | Observed/causal support | Supported conclusion and mismatch |
|---|---|---|---|---|
| CLM-1 | README workload-grounded evolving semantic layer; host build/evolve method, see canonical claim | RTE-1, RTE-2, RTE-3, RTE-5, RTE-6 support state/access; RTE-4/RTE-8 reasoning is host doctrine | None inspected; no causal design available | Wired store/read-back plus afforded trace-directed revision. Reminder is not continuous autonomous evolution |
| CLM-2 | README grounded commit/paired reproducible publication; skills demand grounding, matched evaluation and rejection | RTE-1 structural gate; RTE-5 supplied-record predicate and promotion; RTE-7 alternatives | None inspected; no candidate-bound experiment | Formal path can reject invalid/non-improving supplied records. Universal verified/reproducible admission exceeds enforcement; alternate writes, code rollback and external evidence remain material limits |
| CLM-3 | README reported aggregate benchmark gains, source layer reported operation | Inspected CMP-4 launch/return adapters do not reproduce those experiments | No observed run or intervention; component effects and confounding unassessed | Attributed performance claim only. Aggregate outcome cannot certify semantic mechanism, recalled-content dependence or future capacity |

#### 6. Bounded conclusion

The source supports acquisition, retention and selected retrieval of semantic content and observable evidence, with structural checks and a formal comparison predicate that changes operational reliance. Retrieval preserves some source query/result/method fields; clipping and partial rationale delivery limit reconstructed warrant. Arithmetic derives a gate result from supplied values within a narrow formal domain. That domain excludes the truth of the supplied observations, experiment design and explanation.

The host method explicitly affords semantic and causal conjectures, competing explanations, falsifiers and later retention of rejected/validated mechanisms. Its operative formulation, actual content-directed criticism and improved future capacity remain separate uninspected links. Initial structure acceptance and formal higher-score/more-wins bundle acceptance permit content activation for a project; they do not individually establish every semantic claim. RTE-7 also permits use without formal acceptance, so that use is not lifecycle integration. RTE-8 affords direct system-definition adaptation with host-owned recovery. These findings identify distinct sources of operational authority and potential warrant without assigning the system one epistemic verdict.

## Reconciliation

The specialist proposal MEM-OBJ-1 maps to OBJ-7, retained evolution explanations. All exact tokens in its profile were remapped; all other supplied canonical IDs keep their original referents. OBJ-8, OBJ-9, OBJ-10, OBJ-11 and OBJ-12 register distinct Content Layer parts; OBJ-13 and OBJ-14 split workload from observations; OBJ-15 and OBJ-16 distinguish supplied evaluation assertions from the computed disposition. The parent aggregates remain identified with explicit superseded per-part epistemic dispositions, not reassigned IDs.

Material integration issues are resolved as follows: (1) explanation retention/read-back is wired in limited fields and afforded in richer host reports; (2) supplemental RTE-7, RTE-8 and RTE-9 preserve low-level writes, host code revision and observation boundaries; (3) formal gate assurance remains route-specific, and evaluation is not content-digest-bound; (4) Schema/Tool views derive current code, so content pointers do not promise code rollback; (5) linked evidence payloads are readable but supplied truth and constraint enforcement remain limited; (6) Claude reminder is coarse push, Codex status and semantic manifest are requested/instructed reads; (7) reasons are not universally retained or consumed by data agents; (8) the whole trace-learning union stays afforded, with raw acquisition excluded; (9) candidate report filenames are not automatically promoted, bounding display continuity; (10) the broad checkpoint reference conflicts with explicit terminal behavior, so accepted advances and incomplete preserves the checkpoint in this account. Every issue is carried on its affected canonical record and lens finding; none remains a publication blocker.

The parent and specialist used the same frozen SRC-1. The parent asked about alternate writes and Schema/Tool views and supplied supplemental IDs during the commission; these are coordinated refinements, not claimed independent convergence. The epistemic overlay ran locally under its standalone procedure, treating deterministic structure/arithmetic separately from semantic warrant. No source pin, frozen input bytes or specialist conclusions were silently strengthened.

## Bounded synthesis

EvoOntology's strongest established contribution is a versioned semantic layer with bounded on-demand access, explicit task observations and a formal evolution transition that recomputes acceptance from supplied comparison evidence. Host skills add a richer method: competing grounding explanations, falsifiable causal hypotheses, capability tests, regression review and retained rejected explanations. Those instructions are an affordance; the deterministic gate cannot certify their semantic execution.

The distinction is operationally consequential. Initial validation checks structure/references/loadability. Formal evolution checks paired numeric vectors or decoded judge verdicts and an explicit no-regression assertion. Low-level save/active APIs can still change operative content outside that formal path. Content publication copies five record files; it does not version arbitrary schema/tool/runtime edits. A user can reason about the formal path's vetoes without mistaking them for a universal guarantee over every available write surface.

A standing self-improvement pathway has conclusion status **afforded** at this partial-loop boundary: host-directed evidence-responsive changes to the layer's own content/access/schema can feed later operation, and content adoption/read-back is wired. Actual occurrent self-improvement and attributable capacity benefit are **uninspected**; aggregate gains are **claimed**. Conjectural learning has conclusion status **uninspected**: its formulation/criticism method is explicitly afforded, but the causal chain from operative theory through valid criticism to improved future capacity was not observed. Reflection has conclusion status **afforded** for the host Evolver's representation of its own ontology/tool/schema limitations and proposed interventions; actual representation-mediated changes or a reflective theory-builder loop remain uninspected. These are independent properties, not an autonomy grade.

For a data agent requesting retained semantics, the code establishes controlled retrieval and provenance-bearing records, while source truth and correct downstream use remain external. For evolution, the core supplies state and selected admission predicates, while the host must supply matched, trustworthy evaluation and semantic criticism. Frozen candidate-linked traces, provenance-bound evaluation results, replayed acceptance/rollback, and explicit handling of schema/tool edits would change the unresolved conclusions. No cross-system ranking or Commonplace transfer advice is given.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| Host reasoning/scheduling/tool policy uninspected | CMP-3, RTE-1, RTE-4, RTE-8 | Shipped skill contracts and MCP endpoints | Actual content-directed criticism, model fixity, complete grants or autonomous execution | Frozen host/provider implementation and linked runs |
| Supplied evaluation records are not observed experiments | OBJ-6, RTE-5, CLM-2, CLM-3 | Session record normalization and gate | Matched conditions, score truth, reproducibility, causal improvement | Candidate/version-bound raw runs and independent comparison design |
| Semantic grounding exceeds structural validation | OBJ-1, RTE-1, RTE-2 | Record/reference/load checks and skill doctrine | Truth of business definitions/mappings/constraints/evidence | Reproducible data probes linked to each claim |
| Alternate writes and code edits have different admission/recovery | RTE-7, RTE-8, BAP-4 | Store APIs and host revision instructions | Universal gate/immutable-version/whole-system rollback guarantee | Enforced capability boundary and versioned tested code/schema recovery |
| External observation provenance and truncated outputs | OBJ-4, RTE-3, RTE-9 | Caller events and bounded SQLite recorder | Completeness/truth of arbitrary tool traces and full-output reconstruction | Authenticated native captures and retained full outputs where needed |
| No dynamic activation or faithful-use intervention | RTE-2, RTE-5, CLM-3 | Static source and reported aggregates | Semantic recall dependence or attributable future capacity gain | Controlled recalled-content interventions and linked downstream actions |

## Verification and blockers

### Semantic verification

Checked source-only identity, host/core responsibilities and material alternate admissions. Formal gate arithmetic is separate from externally supplied provenance, regression judgment and paired-condition truth; reference checking is separate from semantic grounding. Core plugin copies match root blobs. All nine routes have explicit immediate return, later read-back, delegated visibility, selection, invalidation and effect limits. Native SQLite restrictions are not generalized to independent host tools. Candidate theory formulation, operative use, criticism, revision and capacity benefit remain separate; reflection is scoped to the host-mediated route. The specialist profile was checked against all scoped branches: RTE-1 historical-question acquisition, RTE-3/RTE-9 raw recording and clipping, RTE-4 semantic/rationale synthesis, RTE-5 evaluation/control retention, RTE-7 alternate writes and RTE-8 code/instruction revisions. Only RTE-4/RTE-8 supply the qualifying trace-learning transformations; dependent source/scope/timing/form axes use those same branches. Core operations remain wired, the host transformation union afforded. RTE-3 coarse push specifies its consumer, SessionStart trigger, state/count/time selector and selected due summaries; requested identity/lexical retrieval is not added to push signals. All known aggregate values include the authorized host-edit branch and exclude provider/benchmark internals explicitly. Faithfulness remains not determinable. The sparse epistemic overlay separates check, disposition, retention and integration, and all unobserved candidate phases remain no instance observed. Report/input identity and anchors were checked; canonical IDs are unique and mapped without substring substitution.

### Deterministic validation

Target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-evoontology-01/result.md`. Integrated result passed full validation cleanly. All retained quotations were matched against complete pinned blobs, and full-path citation ranges were checked against their file boundaries. No target execution was used.

### Blockers

None.
