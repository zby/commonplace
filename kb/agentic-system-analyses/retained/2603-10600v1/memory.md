---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory analysis of trajectory-informed memory generation: trace-derived tips, consolidation, description-based retrieval and advisory prompt delivery."
run-id: AAS-2026-10-14-2603-10600v1-a956324c9a82-01
source-identity: https://arxiv.org/html/2603.10600v1
reviewed-boundary: "arxiv-2603.10600v1-html-captured-2026-10-14"
---

# Trajectory-informed memory generation memory report

## Boundary and evidence

The subject is the documented memory pipeline, frozen at the HTML capture declared in [boundary](boundary.md#source-register). Direct inspection of SRC-1, §§3.1–3.3 and §§4.1–4.2, supports the account below; the supplied runtime supplies provisional route identities and retained passages. The evidence layers are doctrine/design and reported operation, never inspected implementation or observed execution. Inspection used a text rendering of the frozen HTML; quotations refer to the original capture.

Included surfaces are completed trajectories, extraction intermediates, task/subtask guidance, consolidation, search representations, metadata, both retrieval alternatives and initial prompt integration. No executable CLI, hooks, registered tools, service operations, persistence caller or maintenance program is supplied by this document boundary. Consequently their dispatch and actual reload cannot be checked. This is not evidence that a separate implementation lacks them. Model-provider parameter state is opaque; its known roles and fixity limits remain in [RT-CMP-gpt4](runtime.md#rt-cmp-gpt4) and [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding). External linked works and page assets remain excluded as in boundary.

| Entry point / operation | Directly inspected source anchor | Covering records / remaining limit |
|---|---|---|
| Completed trajectory intake; labeled or inferred outcome; attribution | SRC-1, §§3.1.1–3.1.3 | [MEM-OBJ-trajectories](#mem-obj-trajectories), [MEM-OBJ-intermediate-representation](#mem-obj-intermediate-representation), [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction); raw artifact retention and correctness unverified |
| Whole-task and segmented-subtask extraction; domain-specific and generic tips | SRC-1, §§3.1.3–3.1.4 | [MEM-OBJ-tips](#mem-obj-tips), extraction annotation below; independent model calls are described, not a host isolation mechanism |
| Generalize, cluster, deduplicate, resolve conflicts, synthesize | SRC-1, §§3.2.1–3.2.3 | [MEM-OBJ-descriptions](#mem-obj-descriptions), [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation); no inspectable merge history or rejected-output artifact |
| Vector and structured storage | SRC-1, §3.2.4 | [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-OBJ-metadata](#mem-obj-metadata); physical schema, transactions and reload unspecified |
| Similarity filtering/ranking and optional caps | SRC-1, §3.3.1; §§4.1.4, 4.2.2–4.2.3 | [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval); configured cap is not universal |
| Model-guided query; generic null-context eligibility | SRC-1, §3.3.2; §4.1.4 | [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection); complete query and prompt unavailable |
| Format and deliver guidance to next task | SRC-1, §3.3.3; §4.1.2 | [RT-BAP-guidelines-channel](runtime.md#rt-bap-guidelines-channel), [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution); delivery does not prove activation |
| Evaluate application state and compare memory configurations | SRC-1, §§4.1.3–4.2 | [RT-CLM-reported-results](runtime.md#rt-clm-reported-results); aggregate reports do not establish a per-tip acceptance or withdrawal gate |
| Expiry, rollback, pruning, raw-trace reload and mid-run context compaction | Inspected SRC-1, §§3.1–3.3 and §4.1 | No specified consumer or maintenance implementation; prevents conclusions about those lifecycle operations, not an evidenced absence |

## Core ideas

The retained behavioral product is a tip, not a replayed trajectory. Model analysis turns thoughts, actions and outcomes into conditional prescriptions. Management can further change their meaning by merging complementary steps and choosing between contradictory advice. Later agents receive selected prescriptions and explanatory purpose, not necessarily the evidence from which the prescriptions were derived. See [MEM-OBJ-tips](#mem-obj-tips) and [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation).

Retrieval separates access keys from guidance. Generalized or original descriptions group tips; dense embeddings support similarity; metadata supports filtering and precedence; the agent interprets the tip text. These parts must not be treated as interchangeable memory representations. SRC-1, §§3.2.1–3.3.3; [MEM-OBJ-descriptions](#mem-obj-descriptions), [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-OBJ-metadata](#mem-obj-metadata).

Source trust is outcome-conditioned rather than independently guaranteed. Extraction can infer success from the agent's own reflections. Consolidation gives successful-source and recovery guidance precedence, but this does not test whether a merged prescription is correct. The same source supplies adverse configurations, so selection and delivery cannot guarantee benefit. SRC-1, §§3.1.1, 3.2.3; [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction), [RT-CLM-reported-results](runtime.md#rt-clm-reported-results).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-trajectories
Label: Agent execution trajectories

Source-native identity: complete task trajectories containing sequential invocations, prompts/contexts, responses including thoughts/reflections, actions/results and optional evaluations. Representational form is mixed: natural-language reasoning plus action/result and outcome structures whose exact serialization is unspecified. Storage substrate and durable retention of the raw input are unspecified. Lineage is the agent's completed execution, optionally augmented by external evaluation. The extraction consumer interprets this evidence; the ordinary later-task retrieval consumer is not described as reading raw trajectories. SRC-1, §3.1.1.

Distinct identity: input evidence to [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction), not that transformation route or the agent model; runtime declares no corresponding object.

> Each trajectory represents a complete task execution from initial user request through final outcome.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### MEM-OBJ-intermediate-representation
Label: Structured intermediate representation

Source-native identity: extraction output containing categorized thoughts, patterns/confidence scores, evaluation intelligence, success patterns, trajectory identifier, task intent, step count and outcome classification. Natural-language interpretations coexist with structured categories, numerical confidence and identifiers. No persistent substrate, archival horizon or later task retrieval is specified. Decision attribution reads it to trace decisions backward; tip generation receives the resulting analyses. Confidence scores do not independently certify causal explanations. SRC-1, §§3.1.1–3.1.2.

Distinct identity: intermediate evidence within [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction), rather than a retained tip or route. Runtime's route account supports the distinction; it declares no object counterpart.

> The causal analysis module uses an LLM to trace backwards through the agent’s reasoning steps to identify which decisions led to the observed outcome.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### MEM-OBJ-tips
Label: Strategy, recovery and optimization tips

Source-native identity: generated and consolidated memory-entry guidance: content, explanatory purpose, concrete steps, trigger and optional negative example. This operative part is natural language, including API names interpreted as advice by the model, not executable API grants. Storage is the declared memory system alongside vectors and structured attributes; vendor, on-disk layout and actual persistence are unspecified. Generated text derives from attributed trajectory outcomes; consolidated successors can combine several source trajectories. Later agents receive selected content, purpose, steps and trigger with displayed category and priority. Source reasoning chains and raw evidence are not specified as part of that delivery. SRC-1, §§3.1.3, 3.2.3–3.2.4, 3.3.3.

Distinct identity: guidance artifacts transformed by [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation) and delivered through [RT-BAP-guidelines-channel](runtime.md#rt-bap-guidelines-channel), not those routes or authority channel. No supplied object counterpart.

> The system also generates both domain-specific and generic tips from the same trajectory, maximizing precision and coverage.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

This is the authors' precision/coverage rationale, not measured quality of each entry. Purpose preserves an explanatory field; its presence does not establish full retained attribution or criticism. The intended horizon is across tasks/sessions. Attained persistence and content-dependent activation are unobserved. The runtime extraction and consolidation theory accounts remain the relevant bounded assessments.

#### MEM-OBJ-descriptions
Label: Task and subtask descriptions

Source-native identity: original task descriptions, generated subtask descriptions and canonical cluster descriptions. They are natural language, transformed by entity abstraction, action normalization and removal of task-specific context. Their stored embeddings have separate identity below. Subtask segmentation also records source step ranges, applications and purpose, although later persistence of all segmentation fields is unspecified. Canonical descriptions are re-embedded and stored with consolidated tips, replacing individual per-trajectory descriptions; task-level tips instead index by original task description. The clustering model and retrieval selector consume these access representations. They are not necessarily the advice the later agent sees. Storage implementation is unspecified beyond the memory/index description. SRC-1, §§3.1.4, 3.2.1–3.2.4, 3.3.1.

Distinct identity: access text used in [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation) and [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval), not those operations; no supplied object counterpart.

> This description is re-embedded and stored alongside the consolidated tips, replacing the individual per-trajectory descriptions.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### MEM-OBJ-metadata
Label: Structured tip metadata

Source-native identity: unique tip identifiers and category, priority, application context, task category, source trajectory identifiers/outcome information, with creation timestamp specified for consolidated entries. Filterable attributes and identifiers have symbolic consumption by retrieval and grouping; outcome descriptions retain a natural-language component interpreted during consolidation. Underlying structured store and schema are unspecified. Source IDs become plural after consolidation. This is lineage information, not proof that underlying source artifacts remain dereferenceable. Category, priority and source success/failure shape merge precedence; application/category attributes shape retrieval; category and priority also appear in rendered guidelines. Creation time alone establishes no expiry rule. SRC-1, §§3.1.3, 3.2.3–3.2.4, 3.3.2–3.3.3.

Distinct identity: control/provenance attributes used by [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation) and [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection), not guidance prose or either route. The consolidation passage retained in runtime supports precedence; no supplied object counterpart.

#### MEM-OBJ-embeddings
Label: Dense vector embeddings

Source-native identity: dense tip-content/purpose embeddings, generalized-description embeddings, re-embedded canonical descriptions and query embeddings. Representational form is distributed-parametric numerical representation, not natural-language guidance. Stored memory vectors enter vector storage; query-vector persistence is unspecified. Lineage is text transformed by the unspecified embedding model [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding), not agent parameter training. Clustering and retrieval consume cosine similarities; the agent receives text rather than these vectors. SRC-1, §§3.2.2–3.3.1.

Distinct identity: model outputs and search state, not the embedding component or [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval). No supplied object counterpart. The paper describes both content/purpose vectors and description-based indexing; it does not specify their exact index relationship, compatibility checks or stale-vector replacement protocol. The corresponding runtime component already retains the minimum source passage for the content/purpose representation.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction)

The raw-to-derived chain is [MEM-OBJ-trajectories](#mem-obj-trajectories) → [MEM-OBJ-intermediate-representation](#mem-obj-intermediate-representation) → decision analyses → [MEM-OBJ-tips](#mem-obj-tips). External reports and inferred self-reports are alternative evidential inputs, not alternative checkpoints. Model-produced guidance is intended for durable later-task consumption after consolidation. Raw-log acquisition does not itself establish retained learning. SRC-1, §§3.1.1–3.1.4.

Subtask segmentation receives the full trajectory and retains source ranges; per-subtask calls focus on logical phases and return 2–4 tips each. This controls what extraction calls see but does not establish a runtime stack frame, destruction of isolated context, or later raw-context reload. Whole-task extraction remains an alternative. Human initiation or supplying a trajectory is not per-tip approval; initialization authorship and raw-ingest control remain unspecified. Subsequent model transformation is positively described despite that uncertainty.

#### On [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation)

Curation changes both access representations and behavioral content: descriptions lose entities/context; clustering pools source tips; deduplication and synthesis replace text; conflict precedence selects among prescriptions. The pipeline's LLM is the semantic admission decision maker, while storage I/O is unspecified. Outcome metadata supplies preference evidence, not an independently evaluated merged successor. No documented per-entry human approval, rejected-tip archive, reversible history or withdrawal consumer can be established from SRC-1, §§3.2.1–3.2.4. These are limits, not absent implementation claims.

Consolidated tips preserve source IDs and explanatory purpose by the entry design. Canonical descriptions explicitly replace per-trajectory descriptions. Neither implies all original causal reasoning survives or that source IDs resolve into a later evidence-reading route. Material merged away is not described as a later prompt input. This limits auditing and rationale-preservation conclusions without denying the supported provenance fields.

#### On [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval)

A new task automatically triggers selection before reasoning. Query text is embedded; stored description similarity admits candidates and optional top-k determines the selected associated tips. This is system-selected supply to the consumer, not a foreground agent explicitly requesting a particular memory artifact. Stored guidance persists independently of its selection into one initial prompt. Threshold filtering keeps some external material out of the window; it is not removal from an already accumulated conversation. SRC-1, §3.3.1.

Top-k limits item count, not token count. The reported top-3 and uncapped alternatives prevent a universal five-tip or token-budget claim; runtime already records those counterexamples. No truncation policy for a single long tip is specified. Content/purpose vectors and description vectors must not be silently treated as one fully specified index.

#### On [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection)

The selector receives the new task, infers domain/category and relevant guidance categories, and constructs a query retaining generic null-application tips as candidates. The described evaluation adds priority-weighted ranking and top five. The selected retained parts are tips, not source trajectories. Delivery remains the same initial guidelines channel; an extra selection call does not establish agent-initiated memory-tool use, deployed delegation or unsolicited asynchronous delivery. SRC-1, §§3.3.2–3.3.3, 4.1.4. Exact selected text, token budget and actual filtering compliance remain unobserved.

#### On [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution)

The formatting step exposes priority, category, content, purpose, implementation steps and trigger to the model. It does not specify delivery of source IDs, complete decision attribution or raw evidence. The memory has advisory authority through natural-language interpretation, not fixed executable semantics. No observed trace closes delivery-to-activation. SRC-1, §3.3.3; the runtime authority-path record retains the placement passage.

The reported memory corpus comes from train/dev trajectories, while held-out tasks test later guidance use. AppWorld evaluates final application states, not the validity of each tip. The paper's proposed recurring feedback cycle does not establish that test outcomes trigger online memory writes, rejection or rollback. SRC-1, §§4.1.3–4.1.5. No mid-task eviction, compaction checkpoint or reload route is specified by the inspected account.

## Write side

Acquisition starts with completed agent executions and optional evaluation reports; the identity of the intake controller and physical trace retention are unspecified. Known subsequent authorship is computational: semantic extraction and backward attribution propose category-specific guidance. Strategy, recovery and optimization categories admit more than successful replay. Unlabeled extraction infers outcomes; benchmark outcome labels are not a universal gate. SRC-1, §§3.1.1–3.1.3; [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction).

Management then performs the documented semantic admission stage. Its instructions request abstraction, equivalence grouping, deduplication, conflict precedence and synthesis. These requests establish a design, not reliable semantic preservation. A successful trajectory can still contain incorrect advice; a canonical cluster can combine different scopes. The document supplies no independent post-merge test addressing those cases. SRC-1, §§3.2.1–3.2.4; [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation).

Replacement of individual descriptions and removal of duplicate/contradictory guidance are specified at the semantic level. Physical deletion, rejected-candidate retention, expiry, explicit withdrawal, rollback and failed-merge recovery are not specified in the inspected management account. No later consumer of a rejection or withdrawal artifact can therefore be traced. Retained source IDs are not a substitute for such an artifact. Evaluation reports support aggregate comparisons, not a proven maintenance loop. Reasons survive at least as intended explanatory-purpose text, but complete attribution preservation and later source-evidence access remain unresolved. No alternative checkpoint or summary-reload form is specified. See [MEM-OBJ-tips](#mem-obj-tips), [MEM-OBJ-descriptions](#mem-obj-descriptions) and [MEM-OBJ-metadata](#mem-obj-metadata).

## Read-back

The actual documented later-consumer role is the next task's ReAct agent. Both [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval) and [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection) select retained tips from a task request; neither is merely an uncalled storage API. Both are design-level routes, without deployed wiring evidence. They differ in numerical-only matching versus model-derived query criteria, not in the guidance channel. SRC-1, §§3.3.1–3.3.3.

The selector includes selected tips in initial context after task context and before standard instructions. The model interprets them; ordering does not establish instruction-hierarchy priority or compliance. Raw traces, unselected tips and clustering evidence are not specified as delivered. Description keys and metadata affect selection before this consumption boundary. Thresholds, item caps and category/domain filtering determine inclusion; no universal token budget follows. SRC-1, §§3.3.1–3.3.3; [RT-BAP-guidelines-channel](runtime.md#rt-bap-guidelines-channel).

This is trace-fed cross-task guidance, not weight updating and not current-turn accumulation. No independent evidence establishes a foreground memory pull, mid-run reload, compaction or context-frame disposal. Aggregate performance comparisons show the authors' reported treatment outcomes, including harmful configurations, not which specific retained reason changed an action. [RT-CLM-reported-results](runtime.md#rt-clm-reported-results) prevents upgrading presence/delivery into activation or guaranteed learning benefit.

## Integration issues

- No correction to a supplied runtime fact is required. No new declaration duplicates a supplied record: the six new operative objects distinguish artifacts and representations from supplied components, routes and authority channels.
- [MEM-OBJ-embeddings](#mem-obj-embeddings) and [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding): SRC-1, §§3.2.4–3.3.1 describes content/purpose vectors and description-indexed retrieval without executable index relationships. Preserve both positive descriptions; do not infer a single complete schema.
- [MEM-OBJ-tips](#mem-obj-tips), [MEM-OBJ-metadata](#mem-obj-metadata) and [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation): purpose and source IDs are specified, but full attribution preservation, source dereference and merge-history access are not. This prevents a claim of end-to-end rationale auditing.
- [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval) and [RT-CLM-reported-results](runtime.md#rt-clm-reported-results): §4.1.4's five-tip language is bounded by later top-3 and uncapped experiments, already identified by runtime. Budget classifications must remain configuration-specific; no token cap is known.
- [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution) and [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation): source §§3–4 leaves initialization control, physical persistence/reload, per-tip rejection, withdrawal, online update scheduling and rollback unresolved. These prevent implemented-lifecycle and exercised self-improvement conclusions, not the bounded design account.

## Limitations and checks

The supplied run ID, reviewed boundary and source identity were copied exactly. Source inspection stayed within the registered frozen HTML and the supplied boundary/runtime members. No target execution, external lookup or other analysis exposure was used. The capture's design prose and attributed evaluation do not supply an observed merge, vector-store artifact, selection trace, consumer action trace or independently verified benefit. No absence record is justified by these missing implementation details.

Deterministic validation: the invocation's validate-output command passed the member content check. It reported that invocation residue was not checked. This establishes neither job acceptance nor claim support; the check covers structure and quote occurrence, not evidential sufficiency.
