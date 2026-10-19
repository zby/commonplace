---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of Agent Skills for Context Engineering: research read-back, trace-derived instructions, file context and illustrative memory APIs."
run-id: AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01
source-identity: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
reviewed-boundary: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
---

# Agent Skills for Context Engineering memory report

## Boundary and evidence

The target is a skill corpus with a research maintenance plane and shipped examples, not a deployed universal memory service. SRC-1 is the Git source in [boundary](boundary.md#source-register), frozen at `9ff0c99108b36d3b886defd825d8ac1f47dba374`. The checkout HEAD and clean working tree were rechecked. This report retains the boundary's **complete artifact, partial loop** scope. Source inspection supports implementation and doctrine/design findings; no target program, test, provider or example was executed.

Memory scope follows the supplied runtime routes: research state and mechanism admission, router results, retained digital-brain content, and trace-fed prompt/skill production. Direct reads add the memory, filesystem, context-selection, masking and structured-summary helpers, private artifact access/materialization, export projection and removal protocol. Static published instructions are context inputs, but not themselves evidence of use-accumulated read-back. Provider models remain opaque components as recorded in runtime. No new source is introduced.

| Entry point or memory operation | SRC-1 paths | Coverage and prevented conclusion |
| --- | --- | --- |
| Skill discovery and activation | `README.md`, `.plugin/plugin.json`, `skills/context-fundamentals/SKILL.md` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction); host implementation and update/cache invalidation external. |
| Research queues, retrieval, closure and promotion CLI | `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`, `researcher/scripts/validate_run.py` | Supplied [RT-RTE-research-step](runtime.md#rt-rte-research-step), [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion); direct closure/promotion reads and novelty CLI inspection add [MEM-OBJ-registry](#mem-obj-registry), [MEM-RTE-novelty-check](#mem-rte-novelty-check). Acquisition completeness and authenticated review are not established. |
| Registry/ledger read-back and rejection | `researcher/scripts/novelty_check.py`, `researcher/scripts/research_loop.py` | Direct reads establish positive registry consumption, distinct rationale retention and rejection limits. |
| Private artifact APIs and candidate freezing | `researcher/scripts/artifact_store.py` | Direct reads of CAS put/get, artifact head/get/verify/materialize and freeze/materialize; [MEM-OBJ-artifact-body](#mem-obj-artifact-body). Schema validation, tree traversal, editable-policy enforcement and fake-capability internals not fully traced. No production consumer/deployment assurance. |
| Export and withdrawal | `researcher/scripts/export_policy.py`, `researcher/runbooks/public-export-correction.md` | Direct projector/render and full correction runbook reads; [MEM-OBJ-public-projection](#mem-obj-public-projection). Policy loader/scanner/staging checker internals not fully inspected; no complete privacy or automatic downstream withdrawal claim. |
| Router/effectiveness | `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts` | Supplied [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark), [RT-ABS-effectiveness-executor](runtime.md#rt-abs-effectiveness-executor); no new run evidence or automatic skill-change consumer. |
| Digital-brain retained-data consumer | `examples/digital-brain-skill/SKILL.md`, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py` | Direct skill and selection/scaffold reads; annotation on [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft). Other module writes, weekly-review/contact/idea helpers inventoried/searched, not fully traced. No all-module admission/deletion guarantee. |
| Optimizer, analyzer and generate-skill alternate CLI | `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/skill_generator.py` | Supplied [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization); direct artifact saving, analyzer formatting, display formatting, generation and artifact-reload reads add three operative parts below. Streaming capture and parser/fallback internals remain uninspected. |
| Vector/graph API and temporal alternatives | `skills/memory-systems/scripts/memory_store.py`, `skills/memory-systems/references/implementation.md` | Full helper read; direct reference consolidation/integrator reads. [MEM-RTE-memory-access](#mem-rte-memory-access). No persistent cross-process store or wired host integration established. |
| Offload, cleanup, plan checkpoints and reload | `skills/filesystem-context/scripts/filesystem_context.py` | Full helper read including main/demo dispatch; [MEM-RTE-file-offload](#mem-rte-file-offload), [MEM-RTE-plan-reload](#mem-rte-plan-reload). No installed model tool/read-back wiring. |
| Masking, summaries, budgets, trimming and lazy loading | `skills/context-optimization/scripts/compaction.py`, `skills/context-fundamentals/scripts/context_manager.py`, `skills/context-compression/scripts/compression_evaluator.py` | Full compaction helper; context builder/trimming/lazy-loading and structured summarizer/probe callback inspected. [MEM-RTE-context-selection](#mem-rte-context-selection). Validator, evaluator scoring and probe extraction internals not fully traced; no reliable hard tokenizer ceiling or deployed compactor claim. |
| Model-edited text and opaque/numerical alternatives | `skills/self-managed-context/references/harness-protocol.md`, `skills/latent-briefing/SKILL.md`, `skills/context-compression/SKILL.md` | Direct full protocol/latent skill and compression core reads; [MEM-CLM-context-protocols](#mem-clm-context-protocols). External reference implementations/tensors unavailable in registered source; no attribution of their operation to target. |
| Other included memory/context surfaces | `skills/multi-agent-patterns/scripts/coordination.py`, `skills/bdi-mental-states/SKILL.md`, `skills/hosted-agents/scripts/sandbox_manager.py`, `skills/project-development/scripts/pipeline_template.py`, `examples/book-sft-pipeline/scripts/pipeline_example.py`, `examples/llm-as-judge-skills/src/agents/evaluator.ts`, `examples/long-horizon-prompt-lab/`, `examples/x-to-book-system/` | Available but uninspected or signature-inventoried only: worker handoff/isolation, RDF state, sandbox lifetimes, batch checkpoints, training-data/parameter lineage, evaluator artifacts, prompt-lab retention and book workflow not closed. Prevents corpus-wide enumeration, learning, delegation-isolation or checkpoint-recovery conclusions. |
| Remaining governance, migrations and claim/inventory tools | `researcher/scripts/governance_policy.py`, `researcher/scripts/build_inventory.py`, `researcher/scripts/migrate_legacy.py`, `researcher/scripts/schema_contract.py`, `governance/` | Bounded withdrawal/supersession search only. Missing full lifecycle and provenance transformations prevent a universal admission/withdrawal account. |

The last two rows retain unresolved included responsibilities rather than silently excluding them. External hosts, actual private queues/CAS state, provider internals and execution traces remain outside supplied evidence; available uninspected files are not access gaps.

## Core ideas

1. **Research memory has a real software reader.** Promotion projects a proposal into a compact registry, retaining review rationale separately in a ledger. The novelty CLI later tokenizes accepted/candidate registry entries and corpus text. It does not read the rejected ledger in that path. Thus retained rejection is not the same as rejection-aware novelty selection. [MEM-OBJ-registry](#mem-obj-registry), [MEM-RTE-novelty-check](#mem-rte-novelty-check).
2. **Trace-to-instruction transformation is stronger than logging, but weaker than demonstrated learning.** The optimizer can feed rewritten system text to another capture invocation. Saving `trace.txt` retains a truncated display, not the full in-memory trace. Separate skill generation from saved artifacts loses still more lineage because it reconstructs no iterations. [MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace), [MEM-OBJ-final-prompt](#mem-obj-final-prompt), [MEM-OBJ-generated-skill](#mem-obj-generated-skill).
3. **Context engineering is mostly composable helpers plus guidance.** File offload, in-memory observation masking, priority selection and regex summaries are implemented; host invocation, eviction from an already accumulated window and reliable successor delivery are often the integrator's responsibility. Returning a compact reference cannot itself remove the original from a host window. [MEM-RTE-file-offload](#mem-rte-file-offload), [MEM-RTE-context-selection](#mem-rte-context-selection).
4. **Labels overstate some helper capabilities.** The memory helper uses hash-seeded random vectors, not learned semantic embeddings; its integrated query ignores `time_filter`, and entity-context access differs from session-filtered query access. Its consolidation method is empty. These are bounded implementation findings, not a claim that the corpus lacks useful memory design guidance. [MEM-OBJ-vector-store](#mem-obj-vector-store), [MEM-RTE-memory-access](#mem-rte-memory-access), [MEM-ABS-helper-consolidation](#mem-abs-helper-consolidation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-registry
Label: Mechanism registry and review ledgers

Part of: [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion)

This is the route's retained output, not a duplicate route. Source-native storage: Git/local JSONL files `researcher/mechanisms/registry.jsonl` and accepted/rejected ledgers. Registry IDs, statuses and field names are symbolic selectors; activation scenario, behavior change and failure modes are natural-language content. Promotion copies evidence claim IDs into `evidence`; accepted/rejected event ledgers retain reviewer text, run directory, timestamp and rationale. Authorship is caller-supplied proposal content; physical I/O and default readiness rejection are software-controlled, with the supplied runtime's bypass and closed-state limits. SRC-1, `researcher/scripts/research_loop.py`.

> "rationale": proposal.get("review_rationale", ""),
> --- `researcher/scripts/research_loop.py`

> "evidence": proposal.get("evidence_claim_ids", []),
> --- `researcher/scripts/research_loop.py`

Later novelty computation consumes registry text, not ledger rationale; subsequent human/agent registry reading is prescribed in the supplied parent. The ledger preserves reasons, but its presence establishes neither a software rationale consumer nor authenticated human approval. Rejected proposals remain events without registry insertion in this function.

#### MEM-OBJ-vector-store
Label: VectorStore numerical index and text metadata

Source-native identity: `VectorStore.vectors` and associated metadata/entity/time indexes in the in-memory helper. Numerical vectors have distributed-parametric representational form (synthetic dense values, not learned weights), consumed by cosine ranking; metadata keys/indexes are symbolic, and stored fact strings are natural-language content. This is not a learned embedding model or a weight update. Initial facts and metadata come from library callers; integrated writes explicitly retain fact text, entity, time and session. Low-level `add` does not itself copy its text argument into metadata, so returned `text` can be empty. SRC-1, `skills/memory-systems/scripts/memory_store.py`.

> rng = np.random.default_rng(hash(text) % (2**32))
> return rng.standard_normal(self.dimension)
> --- `skills/memory-systems/scripts/memory_store.py`

The hash-seeded stub supplies equality-related repeatability within a hash environment, not semantic similarity or pinned cross-process embedding provenance. No runtime model parameters reside in this index. Closest supplied route is [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft), but this is a different in-memory helper, not digital-brain JSONL.

#### MEM-OBJ-property-graph
Label: PropertyGraph and temporal edges

Source-native identity: node/edge dictionaries, name registry and indexes in `PropertyGraph`/`TemporalKnowledgeGraph`. Substrate is Python process memory; keys, relationship types and temporal comparison are symbolic, while arbitrary prose properties require interpretation outside these graph operations. Callers supply relationships and validity intervals; no automatic entity extraction is established. Name equality reuses nodes and can update properties. Explicit temporal query operations filter interval metadata; integrated `store_fact` instead calls ordinary relationship creation. SRC-1, `skills/memory-systems/scripts/memory_store.py`.

> if valid_until is None or datetime.fromisoformat(valid_until) > query_time:
> --- `skills/memory-systems/scripts/memory_store.py`

Distinct from [MEM-OBJ-vector-store](#mem-obj-vector-store): graph traversal and temporal edge checks have different selectors and do not share the vector query's session gate. No supplied runtime counterpart after comparison.

#### MEM-OBJ-reasoning-trace
Label: In-memory trace and saved display

Part of: [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

The route's input evidence part is distinct from rewritten instructions. `ReasoningTrace` carries task/system prompt, provider thinking strings, tool names/inputs/results, outcome and accounting in process memory. Prose is natural language; identifiers, counts and success flags drive symbolic bookkeeping. Tool data originates in caller callbacks or mock results, not necessarily real environment action. Analyzer formatting passes full thinking strings but only 200 characters of each tool result. The saved `iteration_N/trace.txt` is a display projection with thinking cut to 500 characters per block and tool results to 100. It is not a lossless checkpoint of the full trace object. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`.

> parts.append(thinking.content)
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`

> lines.append(thinking.content[:500] + "..." if len(thinking.content) > 500 else thinking.content)
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`

The producer label “trace” therefore does not establish complete later auditability. Analysis/optimization reports are further derived text; no inspected automatic route reconstructs a full capture from this display file.

#### MEM-OBJ-final-prompt
Label: Optimized system text and final artifacts

Part of: [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

Natural-language revised instructions are held in `current_prompt`, optional iteration `optimized_prompt.txt`, and `final_prompt.txt`. `summary.json` separately stores symbolic scores/counts and task text. Model-generated revisions have software growth/continuation selection, not per-round human approval. Reasons and patterns reside in separate analysis/optimization reports; the next capture receives the chosen prompt as system text, not those complete reports. The source does not guarantee the prompt itself preserves its reasons. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`; supplied parent supplies the update/score caveats.

> f.write(result.final_prompt)
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`

Within-run capture consumes revised text; cross-invocation `generate-skill` reads final text plus summary, not saved iteration traces or analysis. The latter is a genuine durable consumer, but not a recovered full optimization history. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`.

#### MEM-OBJ-generated-skill
Label: Generated SKILL.md and references

Part of: [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

Distinct output part: a model-generated natural-language Markdown skill, discovery description and activation/practice/guideline sections, plus references `optimized_prompt.txt`, `optimization_summary.json`, `patterns_found.json`. The generator directly writes files. It prompts on collected patterns/recommendations/changes but only the first 500 characters of initial/final prompt; references retain the full final prompt. Pattern references retain descriptions/suggestions/iteration, not every original evidence excerpt. Saving reasons near a body does not establish that a host loads them. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/skill_generator.py`.

> Final: {final_prompt[:500] if final_prompt else "N/A"}...
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/skill_generator.py`

The separate artifact CLI constructs a `LoopResult` without iterations, so collected pattern/change lineage is empty on that entry path. Later installation/activation is uninspected, not guaranteed by directory generation. The route overlaps no supplied published-skill object: [RT-OBJ-skill-body](runtime.md#rt-obj-skill-body) names the shipped context-fundamentals body, not this generated output.

#### MEM-OBJ-artifact-body
Label: Content-addressed bytes and access metadata

Source-native identities: `LocalContentAddressedStore`, `LocalArtifactStore`, `CandidateFreezer` files. Exact-byte bodies live under SHA-256 storage; labels, typed artifact references, bindings and freeze receipts are separate symbolic access/provenance metadata. Bytes can encode text, JSON or opaque payloads: storage hashing does not establish their representational form or trust. `get` checks authority, availability, binding and classification before retrieving/validating bytes; `materialize` writes a fresh destination and verifies digest. Candidate freezing snapshots a tree, checks expected digest/policy and stores file bodies and a receipt; materialization verifies the tree and publishes a fresh directory. SRC-1, `researcher/scripts/artifact_store.py`.

> if reference["availability"] != "available":
>     raise ContractError("ARTIFACT_UNAVAILABLE", "artifact is not available for use")
> --- `researcher/scripts/artifact_store.py`

> authority.require("artifact.read", resource_id)
> --- `researcher/scripts/artifact_store.py:383-405`

These are implemented storage/reconstruction operations, not demonstrated model read-back. Bounded search of non-test Python under `researcher/` for `LocalArtifactStore`, `CandidateFreezer`, imports and get/materialize calls found definitions/internal calls rather than a production evaluation/agent caller. No supplied runtime counterpart after comparison. Admission origin remains caller-supplied bytes/classification/candidate; schema/policy checks are not evidence of human content approval. Availability checks do not establish an implemented withdrawal propagation workflow.

#### MEM-OBJ-public-projection
Label: Public research projection and private receipt

Source-native output: `project_source` emits `CitationMetadata` or `ResearchSummary` JSON marked public-derived/durable; renderer writes staged files plus export manifest, and returns a private render receipt carrying source digests. Field selection and manifest IDs/digests are symbolic; retained summary prose remains natural language. Lineage is a checked source digest plus transform/policy digests, not a verbatim public source copy. Allowed source fields are copied rather than generated by an LLM. SRC-1, `researcher/scripts/export_policy.py`.

> for field in transform["allowed_source_fields"]:
>     if field in source:
>         projection[field] = source[field]
> --- `researcher/scripts/export_policy.py`

The render branch rejects changed source bytes, invokes scanning and staging validation, and cleans temporary output on exceptions. Full enforcement internals remain uninspected. No later model consumer is established; publication/correction and downstream index marking are protocol roles, not demonstrated deployed wiring. This export product is distinct from [MEM-OBJ-registry](#mem-obj-registry) and has no supplied runtime counterpart.

### Routes

#### MEM-RTE-novelty-check
Label: Registry and corpus novelty read-back

Endpoints: caller proposal text/file/stdin plus retained registry/skills/fixtures/runs to overlap report. Python selects sections, removes stopwords and compares token sets with Jaccard similarity. Source: SRC-1, `researcher/scripts/novelty_check.py`. Distinct from admission in [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion): this route consumes its retained projection and advises subsequent reviewers; it does not promote.

- Immediate return: JSON or text overlap report and verdict.
- Later read-back: subsequent CLI invocation reads accepted/candidate registry entries and eligible corpus documents accumulated through research.
- Delegated visibility: report is stdout for caller/reviewer; registry text is not automatically sent to a model here.
- Selection predicate: structured proposal sections, accepted/candidate status, nonzero token overlap; ranked top ten mechanisms/documents with at most thirty shared terms each; default threshold 0.18.
- Invalidation or expiry: registry status affects admission to comparison; partial/template skill proposals are skipped; no general content-age expiry.
- Activation or effect: report can inform external novelty judgment; no automatic published-skill revision or observed reviewer compliance.
- Evidence limits: lexical overlap is not semantic identity; rejected ledger rationale is not an input in this inspected path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposal authorship is external; code decides advisory verdicts `pass`, `human_review`, `likely_duplicate`, not content approval. A human/agent decides next changes under the research protocol; no answer oracle or authenticated veto inside this comparator. Mode is open proposal comparison, triggered by caller invocation. Retained registry evidence/failure-mode strings affect overlap, while reasons stored only in the ledger do not.

> if entry.get("status") in {"accepted", "candidate"}:
>     entries.append(entry)
> --- `researcher/scripts/novelty_check.py`

#### MEM-RTE-memory-access
Label: Illustrative vector and graph access

Endpoints: caller facts/relationships to in-memory vector/graph state and query result dictionaries. Owner: Python API caller supplies content; code ranks, filters and traverses. SRC-1, `skills/memory-systems/scripts/memory_store.py`. Distinct helper from supplied runtime routes.

- Immediate return: stored mutation, query list or entity context dictionary.
- Later read-back: uninspected — public operations enable later access while the same object survives, but the demo is not an enclosing agent consumer or durable cross-process reload route.
- Delegated visibility: returned dictionaries belong to library caller; no model/tool registration is shown in this file.
- Selection predicate: query cosine scores above zero and limit five by default, current-session filter plus optional entity; entity-context alternative retrieves ten entity-index memories without the session predicate, and graph traversal has no session predicate.
- Invalidation or expiry: explicit temporal graph methods check validity intervals; integrated retrieve ignores its time_filter argument; consolidate is empty.
- Activation or effect: API storage/retrieval capability, not demonstrated influence on a later agent decision.
- Evidence limits: random embedding stub, process-memory lifetime and absent traced model consumer prevent semantic-recall, cross-session durability or learning conclusions.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

No content-approval gate is shown in these write methods: caller supplies, software stores; human authorship/control is unresolved. No answer oracle or candidate-evaluation mode is involved. Ordinary integrated facts carry timestamps but relationships are not automatically assigned temporal validity. The Markdown reference describes a context integrator using `retrieve_entity`, which does not match this helper's exposed `retrieve_entity_context`; it is guidance, not a wired adapter.

> filters: Dict[str, Any] = {"session_id": self.session_id}
> --- `skills/memory-systems/scripts/memory_store.py`

#### MEM-RTE-file-offload
Label: Tool output offload and cleanup

Endpoints: `ToolOutputHandler.process_output` to scratch file plus compact returned reference, or unchanged short output. Code decides by character-based token estimate; caller decides whether to pass its result to a model. Raw file content is unchanged text; summary/path reference is derived display/access metadata. SRC-1, `skills/filesystem-context/scripts/filesystem_context.py`.

- Immediate return: inline output or formatted path/source/token-estimate/summary string.
- Later read-back: uninspected — files persist and the returned path affords manual/file-tool access, but no reader method or enclosing model reload is wired in this helper.
- Delegated visibility: caller receives compact reference; filesystem permissions/host tools govern other agents' access.
- Selection predicate: offload when len(content)//4 exceeds threshold 2000 by default; first five stripped lines summarized to 300 characters, then reference uses 200 summary characters.
- Invalidation or expiry: explicit cleanup removes scratch files older than 3600 seconds by default; main demo additionally deletes its scratch directory.
- Activation or effect: externalized full output with compact substitute available; no removal of a previously appended host message is implemented.
- Evidence limits: an extant pointer may outlive cleanup; no automatic refresh of stale references or semantic summary guarantee.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Caller supplies raw tool text and invokes write/cleanup; code admits by size, without per-content human review. Cleanup is physical deletion, not a semantic rejection or tombstone. Distinct from [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft), which reads existing JSONL rather than offloading observations.

> if self.scratch_pad.should_offload(output):
>     ref: Dict[str, Any] = self.scratch_pad.offload(output, source=tool_name)
>     return self.scratch_pad.format_reference(ref)
> --- `skills/filesystem-context/scripts/filesystem_context.py`

#### MEM-RTE-plan-reload
Label: File plan checkpoint and reconstruction

Endpoints: caller-authored `AgentPlan` to JSON file and later `AgentPlan.load`, with `progress_summary` as a compact alternate display. Objective/descriptions/notes are natural language; step IDs/status and first-unfinished selection are symbolic. SRC-1, `skills/filesystem-context/scripts/filesystem_context.py`. Separate from offload because the state, read method and invalidation differ; no supplied runtime counterpart.

- Immediate return: save prints a path; load reconstructs objective, timestamps and steps; current_step returns first non-completed/non-cancelled step.
- Later read-back: save/load demo explicitly reconstructs a plan for a simulated context refresh; actual model continuation is uninspected.
- Delegated visibility: JSON file and optional compact progress string, subject to caller delivery.
- Selection predicate: exact requested path reloads full plan; progress summary selects counts and current step rather than all notes.
- Invalidation or expiry: save overwrites that path; no versioned history/automatic freshness check; scratch cleanup can remove a co-located plan file.
- Activation or effect: reconstructed task state available to caller, not proven agent task compliance.
- Evidence limits: the shipped main is a demonstration, not deployment; no automatic context-refresh hook.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Caller authors/edits state; code saves without human approval checks. Complete-step notes can preserve reasons if supplied; compact progress output does not retain all such rationale. Storage is a checkpoint, not evidence of an automatic trace-to-policy update.

> loaded_plan = AgentPlan.load("demo_scratch/current_plan.json")
> --- `skills/filesystem-context/scripts/filesystem_context.py`

#### MEM-RTE-context-selection
Label: Composable context selection and summarization

Endpoints: caller-provided sections/messages/observations/spans/references to returned context text, shortened messages, masked observations or structured summary. Python rules own selection; no common host scheduler invokes all these independent helpers. SRC-1, `skills/context-fundamentals/scripts/context_manager.py`, `skills/context-optimization/scripts/compaction.py`, `skills/context-compression/scripts/compression_evaluator.py`. Distinct from static distribution [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery).

- Immediate return: constructed/shortened text or message list; ObservationStore.mask returns substitute plus reference ID; StructuredSummarizer returns sectioned text.
- Later read-back: ObservationStore.retrieve serves retained raw text by exact ID while process state survives; lazy loader serves requested summary/detail files with session cache; structured summarizer merges new spans into its existing object. Host successor delivery is uninspected.
- Delegated visibility: values returned to caller; probe evaluation explicitly passes compressed context and question to supplied model_response_fn, without prescribing its provider.
- Selection predicate: priority-ordered whole sections fitting estimated budget; trimming keeps last system message, last marked summary and recent fitting messages; observation masking uses character length (200 default), not token count; summary regexes extract file changes/reads/decisions; need_detail flag chooses cached whole-file detail rather than summary.
- Invalidation or expiry: observation FIFO eviction at max_size (1000 default); cache refresh only by forced detail reload; structured summary keeps original file-path change entry and displays last five decisions, with no raw-span recovery built in.
- Activation or effect: context transformation/callback delivery capability; no proven installed agent activation or benefit.
- Evidence limits: independent helper calls do not establish automatic compaction; approximate/mixed token estimates and preserved oversized system/summary preclude a universal hard budget guarantee.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

No human per-span approval is required by these methods. Callers supply original content and invoke updates; regex/priority/size rules admit derived content. This is not model-based semantic consolidation. StructuredSummarizer stores symbolic section lists plus natural-language extracts in process memory; changes are truncated to 100 characters, decisions to 150, and repeated file modifications are not updated once their path exists. Intent/current-state/next-step extraction remains empty in the inspected extractor. A formatted section heading does not prove information was retained.

> if file_info["path"] not in existing_mod_paths:
>     self.sections["files_modified"].append(file_info)
> --- `skills/context-compression/scripts/compression_evaluator.py`

> response = model_response_fn(compressed_context, probe.question)
> --- `skills/context-compression/scripts/compression_evaluator.py`

Probe generation/scoring is an evaluation affordance with an external callback, not automatic acceptance of a new compactor. Detailed scoring internals remain uninspected. For ordinary transforms, no independent answer oracle is consumed. Whole-window isolation/stack-frame behavior is not established by these utilities; only selected values cross their function boundaries, while any existing host context remains outside their control.

### Claims

#### MEM-CLM-context-protocols
Label: Documented model-edited and latent context protocols

Claimed operation, not a target runtime implementation: SRC-1, `skills/self-managed-context/references/harness-protocol.md`, describes mirrored editable messages, protected system/task prefix, role folding, fit/shrink gates, budget nudges and rollback. A replacement note should retain ruled-out alternatives and reasons, tried commands, verified values and next step; it enters later turns as context, not privileged system authority. Rejected growth keeps the previous context; rollback can discard recent turns irrecoverably. The reference also reports external skill-evolution/RL/cache-reuse protocols. Their weights, released code and results are not independently frozen here.

> A rejected edit leaves the context unchanged and does not count as a change.
> --- `skills/self-managed-context/references/harness-protocol.md`

> Rollback notice on overflow: states that the newest turns were rolled back and are unrecoverable, the cumulative turns lost, the remaining room, an instruction to condense this turn only, and the list of commands whose output blew the budget with advice to re-run them with less output. Only an applied context edit resets escalation; dipping under the limit does not, because that happens every cycle of a livelock.
> --- `skills/self-managed-context/references/harness-protocol.md`

SRC-1, `skills/latent-briefing/SKILL.md`, describes task-conditioned selection of worker KV positions through attention scores/shared masks/MAD threshold. Numerical KV state would be distributed representation, not the readable task/summary text; no actual tensor provenance, persistence or worker deployment is inspected. It explicitly excludes API-only inaccessible-KV stacks. SRC-1, `skills/context-compression/SKILL.md`, additionally describes anchored, regenerative and opaque compression. Opaque contents cannot be classified as readable text solely from their summary label. These are declared alternatives, not a demonstrated installed memory loop. Closest supplied record is [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery): these are additional instruction content, not additional evidence that the host implements it.

> API-only stacks where internal KV tensors are inaccessible: use `context-compression`, `memory-systems`, or `multi-agent-patterns`.
> --- `skills/latent-briefing/SKILL.md`

### Evidenced absences

#### MEM-ABS-helper-consolidation
Label: Integrated helper consolidation implementation

- implementation conclusion status: absent

Bounded to full `skills/memory-systems/scripts/memory_store.py` at SRC-1's reviewed revision: method/signature search and full read show `IntegratedMemorySystem.consolidate` contains only its production suggestions and `pass`. It performs no merge, invalidation or archive. This does not establish corpus-wide absence: `skills/memory-systems/references/implementation.md` includes a separate consolidation sketch. That sketch calls undefined-in-class validity/index rebuilding methods and uses edge-list operations unlike the executable helper's edge dictionary. It is not a counterexample establishing this method's wiring. Prevents treating its API/docstring as implemented maintenance.

> - Archive obsolete facts (invalidate, do not discard)
> """
> pass
> --- `skills/memory-systems/scripts/memory_store.py`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-step](runtime.md#rt-rte-research-step)

Storage/authority: retained symbolic run state and queue timestamps direct later scheduler selection, parking and closure reaping; raw source bytes/pointers are evidence for a separate reviewer, not scheduler instructions. This is software control state, distinct from source-derived knowledge. The supplied route establishes actual state reload; it does not establish a human/judge consuming every captured byte. SRC-1, `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`; supplied route supplies passages and limits.

#### On [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion)

Read-back addition: [MEM-RTE-novelty-check](#mem-rte-novelty-check) establishes a concrete registry consumer beyond the prescribed reviewer. The consumer reads only accepted/candidate projections and does lexical overlap, not rationale evaluation. Rejected-ledger storage and preserved reasons remain useful evidence without establishing changed later reliance. No automatic skill-body editing follows promotion. SRC-1, `researcher/scripts/novelty_check.py`, `researcher/scripts/research_loop.py`.

#### On [RT-RTE-idea-draft](runtime.md#rt-rte-idea-draft)

Raw/derived and trust: JSONL ideas/bookmarks/posts are file-backed accumulated content, while rendered scaffold is a derived stdout view. Script selection does not check archival status, recency or evidence reliability; first matching idea, first five related bookmarks and first three same-pillar posts survive. Bookmark display includes only its first key insight; similar-post context is type/URL, not full post prose or performance rationale. File content supplies draft material rather than authenticated instructions. SRC-1, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`.

> output += f"  Insight: {bm['key_insights'][0]}\n"
> --- `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`

Authorship/admission: root skill instructs agent/user capture, voice-first authoring and append-only archive marking; this consumer implements neither write approval nor archive filtering. Thus an `archived` label alone cannot guarantee withdrawal from this route. The external host would have to deliver voice/module instructions and enforce edits. SRC-1, `examples/digital-brain-skill/SKILL.md`.

#### On [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization)

Trace-fed chain: capture object → formatted analyzer input → analysis/patterns/recommendations → replacement prompt → later capture system text is wired in source. Full thinking is used at analysis, tool outputs are truncated; optimizer receives a truncated analyzer-thinking excerpt per supplied route. Fresh request contexts isolate capture, analyzer, optimizer and generator: only formatted inputs/results cross, not an inherited provider conversation or complete reasoning state. This resembles selected-input frames, but the window contains copied values, not dereferenceable references. Returned analysis and rewritten prompts survive the calls; hidden provider state does not acquire a traced retrieval route. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/analyzer.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/skill_generator.py`.

Durable alternative: artifact `generate-skill` reloads summary/final text without iterations, unlike direct generation from in-memory LoopResult. It cannot preserve iteration evidence by virtue of the same output label. See the three part records. Natural-language instructions can shape next capture through system text; actual compliance, qualifying criticism, improved future capacity and exercised self-improvement remain unobserved. The supplied parent's independent theory-builder/learning/reflection statuses are not replaced by logging or these source connections.

#### On [RT-RTE-router-benchmark](runtime.md#rt-rte-router-benchmark)

Retained result files have symbolic scoring/resume authority: a later invocation can skip work based on filenames/basic identity even if descriptions, fixture or success status changed, as supplied runtime records. This is result reuse, not semantic memory adoption or skill-body learning. Description-only requests restrict caller-visible context; `settingSources: []` does not inspect SDK/provider state. The retained history has no inspected automatic instruction-revision consumer. SRC-1, `researcher/benchmarks/sdk-runner/src/runRouter.ts`; supplied record supplies supporting passages.

## Write side

Acquisition and admission differ by surface. Research retrieval retains raw bytes and pointers; later human/agent evaluation is parked by the conservative step driver. Retrieval labels do not ensure complete bytes or content approval. Promotion admits a selected projection under structural/default readiness checks, reviewer strings and supported bypasses; registry append and human merge are separate. Rationale survives in a ledger but the demonstrated novelty reader omits it. [RT-RTE-research-step](runtime.md#rt-rte-research-step), [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion), [MEM-OBJ-registry](#mem-obj-registry).

The optimizer is the clearest automatic trace-fed behavior-shaping write: model analysis/proposals and software continuation/growth rules produce text for later system input. It has no per-update human approval gate. Display artifacts, final prompt and generated skill are different checkpoints with different losses and consumers. Raw tool payloads may be executor or mock outputs; trace provenance is therefore mixed, and final-prompt scores are not independent evidence of its effectiveness. [MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace), [MEM-OBJ-final-prompt](#mem-obj-final-prompt), [MEM-OBJ-generated-skill](#mem-obj-generated-skill), [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization).

Library helpers accept caller-authored facts, observations, plans and spans without establishing who approved each content item. Physical writes are not human admission. Regex extraction, masking, priority selection, file truncation and interval filtering are implemented transformations with limited semantics; they do not inherit the sophistication of memory-framework names in instruction prose. Missing learned embeddings or durable storage is not missing initialization content: caller facts, node updates and subsequent transformations are known. [MEM-RTE-memory-access](#mem-rte-memory-access), [MEM-RTE-context-selection](#mem-rte-context-selection).

Rejection/withdrawal has several distinct outcomes. Promotion can reject into a ledger or fail a default readiness/duplicate check; it does not retract an existing mechanism. Vector helper consolidation does nothing. Observation FIFO and scratch cleanup discard raw content without tombstones; overwritten plan/artifact paths are not versioned rollback. Export's correction runbook instead prescribes disabling renders, retaining private evidence, a human-reviewed correction/tombstone PR and downstream unavailable/superseded index marking. That is a later-consumer protocol, not inspected automatic invalidation. It explicitly warns that deletion cannot undo distribution. SRC-1, `researcher/runbooks/public-export-correction.md`; [MEM-OBJ-public-projection](#mem-obj-public-projection).

> Publication is not reversible. A later deletion cannot make already distributed data private again.
> --- `researcher/runbooks/public-export-correction.md`

## Read-back

The evidence supports three different strengths:

- **Wired retained-state readers:** repeated research steps, novelty computation, router resume, digital-brain scaffold selection, and separate optimizer artifact-to-skill generation. The actual later consumer is code or a generator request, not necessarily the final deployed agent. Model-facing optimizer revisions also cross capture invocations within a run. Relevant supplied routes and [MEM-RTE-novelty-check](#mem-rte-novelty-check) name those limits.
- **Storage/reconstruction affordances:** vector/graph query APIs, plan save/load, observation IDs, scratch paths and CAS materialization. Exact-path access is not relevance selection, and a file pointer is not proof a later model followed it. Budget, lifetime and stale-pointer risks remain beside the individual routes/objects.
- **Instruction-only or external-host paths:** installed skill activation, mirrored model edits, latent KV handoff, opaque compression and downstream export tombstones. Sources describe consumer roles and mechanisms but do not freeze their host implementations or actual delivered payloads. [MEM-CLM-context-protocols](#mem-clm-context-protocols), [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction).

There is no demonstrated independent unsolicited memory push in the inspected helpers. This is a scope limit, not a corpus-wide absence: all direct helpers require caller operations, while the described mirror protocol would automatically expose edited messages on later turns. Source labels alone cannot identify whether that delivery occurs in a real host. Reasons may survive as notes, ledger entries or analysis reports, yet a consumer that receives only a projection cannot be credited with reading them.

## Integration issues

1. **Runtime enrichment, not correction:** [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) names prescribed later research reading. [MEM-RTE-novelty-check](#mem-rte-novelty-check) adds implemented accepted/candidate registry comparison. Its omitted ledger rationale/rejections prevents treating registry novelty as complete retained-decision reuse. SRC-1, `researcher/scripts/novelty_check.py`.
2. **Parts of a supplied route:** [MEM-OBJ-registry](#mem-obj-registry) is promotion output; [MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace), [MEM-OBJ-final-prompt](#mem-obj-final-prompt), [MEM-OBJ-generated-skill](#mem-obj-generated-skill) are distinct parts of [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization). None replaces the parent route. No other duplicate is identified after comparison with supplied declarations.
3. **Artifact fidelity clarification:** the supplied optimizer route's “formatted artifacts” is correct but must not become “full raw trace persistence.” Display truncation and no-iterations CLI reconstruction materially constrain lineage and later reasons. The three optimizer part records retain that distinction; no supplied fact is contradicted.
4. **Instruction versus shipped behavior:** [MEM-ABS-helper-consolidation](#mem-abs-helper-consolidation) and [MEM-RTE-memory-access](#mem-rte-memory-access) prevent importing design claims about semantic, temporal or durable memory into the executable helper. A Markdown integrator/consolidator sketch is not the same API. Scope is SRC-1 helper and inspected reference sections, not all external frameworks.
5. **Unresolved admission/withdrawal integrations:** CAS authorization inputs, freeze policies and export scanners were only partially traced; production consumer, human approval source and downstream tombstone/index implementation remain unresolved. [MEM-OBJ-artifact-body](#mem-obj-artifact-body), [MEM-OBJ-public-projection](#mem-obj-public-projection). No privacy guarantee or end-to-end withdrawal is licensed.
6. **Unresolved included breadth:** multi-agent/RDF/sandbox helpers, book training pipeline, other evaluator/prompt-lab examples, digital-brain producers and remaining governance/claim/migration tools lack end-to-end inspection as listed in coverage. Their missing lifecycle, consumer and isolation facts prevent whole-system memory, learning or recovery conclusions. They remain included responsibilities, not absent mechanisms.

No correction to a supplied source fact is asserted; supplied-runtime annotations and new source findings narrow downstream interpretations.

## Limitations and checks

Only source-level wiring, storage capability and attributed doctrine are established. No execution, causal benefit, authenticated reviewer, private deployment state, complete external source capture, provider tensor provenance or target-wide self-improvement is established. Bounds on uninspected parts are retained in the coverage table and integration issues; no available source was represented as inaccessible. Strong claims were checked against contrary paths: session versus entity retrieval, explicit temporal operations versus ignored integrated time filter, reference consolidation sketch versus executable pass, full analyzer thinking versus lossy saved display, direct generation versus artifact reconstruction, archived-label doctrine versus consumer selection, and removal policy versus irreversible distribution.

Method inputs were read completely, including bounded runtime/record-contract reads and the runtime trailing-line check. Source identity/HEAD and clean working tree were rechecked before source analysis. Worker identity is reported separately. Deterministic validation: the supplied `commonplace-run validate-output` command exited successfully and reported “Member content check passes; invocation residue not checked.” It checks form and quotation occurrence, not analytical correctness or job acceptance.
