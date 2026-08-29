---
description: "Whole-book comparison of AI Agents in Depth with Commonplace, separating broad architectural convergence from differences in memory admission, epistemic warrant, governance, and orchestration"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, synthesis]
tags: [computational-model, context-engineering, agent-memory, evaluation, self-improving-systems, tool-loop]
---

# AI Agents in Depth

**Evidence basis:** complete first-hand reading of the 189,919-word English manuscript and reference answers, repository-level status material, and a purposive sample of companion code and retained experiment evidence at commit [`a18a5f7`](https://github.com/bojieli/ai-agent-book/tree/a18a5f764589396d903d8faeaed205489a21bf4b), captured 2026-08-29; comparison against Commonplace is frozen at `b006c9d7`. I checked the corresponding canonical Chinese introduction only for one translation-sensitive phrase; I did not perform a systematic Chinese comparison, inspect every companion project, or run credentialed experiments.

The book and Commonplace agree on architecture much more than they disagree. Both put the model inside a host-owned loop; treat context as a routed, bounded working set rather than a synonym for a prompt; use progressive disclosure to keep instructions and capabilities discoverable; separate raw trajectories from maintained knowledge; assign exact checks and irreversible effects to symbolic mechanisms; and distinguish retained change from demonstrated improvement. Their recommended governed paths add independent review, reversible release, later activation, and objective-relative benefit checks. The book's strongest chapters—context engineering, knowledge-base maintenance, evaluation, continual evolution, and multi-agent coordination—offer close parallels to Commonplace's central claims.

The consequential differences are narrower. The book uses broad pedagogical categories where Commonplace keeps control, representational, authority, and epistemic axes separate. It makes full accumulated history the lossless ReAct baseline, while Commonplace treats session history as only one possible next-context source. It admits user memories through an LLM's “useful later” judgment, while Commonplace requires a declared output specification for open-domain retention. It requires both knowledge proposer and reviewer to be tool-using agents, while Commonplace chooses evaluator form from the typed target and available oracle. It also occasionally overstates what execution or an ablation diagnoses. Its self-evolution rule correctly prevents a candidate from weakening its own validators; Commonplace additionally specifies how that machinery could be revised through a distinct higher-authority loop.

This is an analysis of architectural doctrine with independent teaching implementations, not of one deployed agent runtime. The repository explicitly says its shared Python package contains packaging and provider plumbing while teaching code remains in separate chapter directories ([shared-package scope](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/agentbook/__init__.py#L1-L15)). Its operational ledger is unusually candid that cloning, installing, or smoke-testing an experiment does not establish completion and that a complete experiment may have a negative result ([status semantics](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/docs/EXPERIMENT_STATUS.md#L1-L23)). Those facts improve the evidence quality of the repository, but they also prevent treating its many projects as one validated production system.

## Scope and evidence boundary

- **Run/result:** `AAS-2026-08-29-ai-agent-book-01`.
- **Target classification:** architectural doctrine with independent teaching implementations. It spans runtime construction, memory/context subsystems, builder and improvement planes, and coordination mechanisms; it is not an enclosing runtime.
- **Boundary kind:** **complete artifact, partial loop**. The complete English introduction, Chapters 1–10, afterword, and reference answers are inside the boundary. Repository metadata, status ledgers, shared plumbing, and representative claim-relevant code/results are also inside. Model providers, external tools and repositories, deployment environments, cited systems, and human decisions remain external.
- **Frozen revisions:** book repository `a18a5f764589396d903d8faeaed205489a21bf4b`; Commonplace comparison evidence `b006c9d76e10139c68678494d836239f68c61666`.
- **Overall evidence tier:** **doc-grounded**. Representative routes reach stronger claim-local statuses, but implementation was not inspected for every material route across the 93 English companion projects.
- **Language limit:** the English edition is a community translation that may lag the Chinese original ([edition notice](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/docs/en/README.md#L21-L36)). Apart from a targeted check of the introduction's multi-agent wording, this analysis supports claims about the frozen English artifact, not exact canonical Chinese wording or coverage.
- **Operational limit:** no credentialed rerun or deployment observation was performed. Retained results establish only the campaigns and producer bytes their provenance supports.

The selected subject is not itself primarily a memory, knowledge, or context-engineering system. Those are embedded topics in a ten-chapter work whose offered result is general agent architecture. The legacy agent-memory review route is therefore **not detected** and was not invoked; no separate publication authority for such a review was granted.

## Source register

| ID | Source and identity | Evidence layer | Inspected scope and access gap |
|---|---|---|---|
| `SRC-1` | English manuscript and reference answers at `a18a5f7` | Doctrine/design | All 189,919 words. External examples remain attributed reports; the Chinese original was not systematically compared, apart from the matching introduction passage for one translation-sensitive claim. |
| `SRC-2` | Repository metadata, status files, shared plumbing, and representative chapter implementations at `a18a5f7` | Implementation and reported operation, separated by path | Deep samples cover the host loop, context ablations, memory/RAG, tool discovery, a codified business rule, event scheduling, evaluation, self-modification, and manager coordination. Unsampled projects cannot inherit their statuses. |
| `SRC-3` | Committed validation records, manifests, ledgers, and result bundles reachable at `a18a5f7` | Observed run or causal experiment only where provenance and design permit | Several records are narrow, negative, historical, or omit a producer revision. They do not establish deployment behavior. |
| `SRC-4` | Commonplace doctrine and linked notes at `b006c9d7` | Doctrine/design and shipped-system contract | Used only for comparison. Later Commonplace edits affected procedure, not the comparison claims in this report. |

## Shared system records

The register below prevents the book's pedagogical categories from silently becoming one runtime topology.

### Components and operative objects

| ID | Generic identity | Role in the book's architecture |
|---|---|---|
| `CMP-1` | Host-owned agent runtime | Builds model requests, schedules calls, dispatches actions, retains current-run state, handles errors, and stops. A representative Chapter 1 path is **wired**; the book-wide component is **claimed**, not one shared implementation. |
| `CMP-2` | External model/provider | Chooses text, tool calls, summaries, judgments, or candidates. Provider operation is external and **uninspected** except through retained receipts. |
| `CMP-3` | Tools, executors, and environment interfaces | Perform observations and effects; representative discovery, code, filesystem, subprocess, and browser routes are **wired** in separate teaching projects. |
| `CMP-4` | Memory, knowledge-base, retrieval, and context mechanisms | Write, structure, index, select, and deliver `OBJ-4`; several Chapter 3 routes are **wired** and have retained runs. |
| `CMP-5` | Evaluation and experiment mechanisms | Define tasks, capture trajectories, apply deterministic or model-based checks, and retain `OBJ-5`; bounded campaigns are **observed**. |
| `CMP-6` | Continual-evolution updater | Diagnoses trajectories and proposes changes to `OBJ-6`; the sampled Chapter 9 code-change path is **wired** through canary eligibility, not production activation. |
| `CMP-7` | Multi-agent coordinator or family | Allocates work, transports messages/artifacts, settles results, and cancels workers; a Chapter 10 single-process manager route is **wired**. |
| `CMP-8` | Human/operator | Sets objectives, supplies high-level judgment, approves high-risk changes, and owns external deployment decisions. These responsibilities are **claimed**; no deployment instance was inspected. |

| ID | Operative object | Form and substrate |
|---|---|---|
| `OBJ-1` | Current task trajectory | Natural-language and structured messages in process or retained traces. |
| `OBJ-2` | System instructions, Skills, tool definitions, and runtime status | Natural language plus schemas/files, resident or progressively loaded. |
| `OBJ-3` | Tool calls, results, and asynchronous events | Structured messages carrying effects, observations, provenance, and errors. |
| `OBJ-4` | Persistent user memory, knowledge files, raw evidence, and derived indexes | Natural-language or symbolic files, JSON, graphs, vector indexes, and version history. |
| `OBJ-5` | Evaluation task, trajectory, rubric/check, result, and diagnostic evidence | Mixed natural-language and symbolic records in manifests, traces, and result bundles. |
| `OBJ-6` | Behavior-changing knowledge, instruction, program, or parameter artifact | Natural language, symbolic code/configuration, or distributed-parametric weights. |
| `OBJ-7` | Handoff, message, shared-work, and settlement artifact | Natural-language or structured files/messages, usually current-run coordination state. |
| `OBJ-8` | External environment state | Filesystems, databases, services, browser state, users, simulators, and the physical world; normally outside the repository boundary. |

### Routes and claim ceiling

| ID | Ordinary progression | Strongest supported status in this boundary | Main limit |
|---|---|---|---|
| `RTE-1` | Request and context → model → tool call → host dispatch → result → later model call → terminal result/stop | **wired** in the Chapter 1 lab; a five-arm retained run is **observed** | It is an optional experiment, not a book-wide runtime or deployment. |
| `RTE-2` | Resident metadata/status/history → selection, loading, compression, or isolation → bounded model context | **claimed** throughout; several Skill, schema, and compression paths are **wired** | Context presence does not by itself establish behavioral activation or faithful compression. |
| `RTE-3` | Conversation/evidence → memory write/consolidation/index → later retrieval → invocation | **wired** in Chapter 3 samples; later-answer use is **observed** in retained campaigns | Some demos push the whole store; some pull selectively. Not every comparison isolates memory benefit. |
| `RTE-4` | Evaluation task/trajectory → verifier or judge → result/diagnosis → maintainer or updater → next experiment | General route **claimed**; bounded evaluation campaigns are **observed** | A check result does not itself establish causal diagnosis, acceptance for deployment, or later integration. |
| `RTE-5` | Operational evidence → diagnosis → candidate artifact → independent gates → acceptance → retention → later activation/rollback | General route **claimed**; candidate-through-canary decision **wired**; older-byte decision record **observed** | Production activation and executed rollback are absent from the sampled experiment. |
| `RTE-6` | Task/decomposition → worker contexts/actions → messages/artifacts → verification/settlement → cancellation/integration | General patterns **claimed**; one manager route **wired**; an older campaign **observed** | The sample settles a model-reported result rather than independently verifying it first, and has no distributed recovery. |
| `RTE-7` | Training data/rollout → loss or reward → optimization → checkpoint → external serving | **claimed** | Training and checkpoint acceptance/activation were not inspected end to end; direct weight adaptation is not automatically a truth-apt knowledge route. |
| `RTE-8` | External event → provenance/urgency routing → queue, cancellation, or parallel branch → model/tool task → completion event | Runtime path **wired**; subprocess mechanics **observed** | The retained Chapter 6 campaign does not exercise semantic event routing through a model. |

The ten central book claims use these routes:

| ID | Book claim | Comparison disposition |
|---|---|---|
| `CLM-1` | An agent combines a model, context, and tools, with the Harness owning execution, state, constraints, verification, and correction. | Strong agreement; the three-term formula is a compact interface view, not a competing runtime definition. |
| `CLM-2` | Context bounds capability and should be composed through stable prefixes, routing, Skills, compression, and isolation. | Strong agreement; the default treatment of accumulated history differs. |
| `CLM-3` | Persistent memory/knowledge needs hierarchy, files, indexes, governed writes, and later retrieval. | Strong agreement on structure; disagreement on open-domain admission and on treating user memory and shared knowledge as one problem at different scales. |
| `CLM-4` | Tools and model-written code expand the action space; code can compose capabilities and enforce exact constraints. | Agreement on mechanism; treating successful execution as proof of logical consistency and its result as an objective correctness standard is an overclaim without a typed target and adequate oracle. |
| `CLM-5` | Events and multimodality expand observation/action across time; safe points and lower-level controllers keep synchronous models usable. | Strong agreement, with deployment guarantees external. |
| `CLM-6` | Evaluate the model-plus-Harness system with typed tasks, resettable state, trajectories, verifiers, statistics, and diagnostic evidence. | Very strong agreement; one model-swap diagnostic and some prose expectations exceed retained evidence. |
| `CLM-7` | Choose post-training only after locating the failure and deciding whether context, knowledge, instruction, program, or weights are the right carrier. | Strong agreement; the carrier list mixes representational form with consumption force. |
| `CLM-8` | Continual evolution converts operational evidence into gated, reversible changes across knowledge, instructions, programs, and weights. | Very strong agreement; production activation is not shown, and the book does not specify a higher-governance route for revising the current safety root. |
| `CLM-9` | Multi-agent work is justified by distinct information, objectives, or controlled separation and needs topology, boundaries, messages, lifecycle, verification, and budgets. | Broad agreement. The opening two-axis grid is a basic map that the rest of the chapter expands; Commonplace treats the additional dimensions as co-equal classifiers. The English introduction's “ultimate form” wording is translation-specific and not a reliable canonical maturity claim. |
| `CLM-10` | Security must move from attacked context into independently enforced execution and data layers. | Strong agreement; Commonplace names capability surface, grant set, isolation envelope, and aggregate authority more explicitly. |

### Evidenced absences

| ID | Recorded search boundary | Finding and prevented conclusion |
|---|---|---|
| `ABS-1` | Complete repository topology, package documentation, chapter READMEs, and representative entry paths | No integrated book-wide runtime or deployment path. This prevents deployment-wide behavior or reliability claims. |
| `ABS-2` | Full Chapter 8 prose | No end-to-end checkpoint proposal, acceptance, persistence, serving activation, monitoring, and rollback contract with named owners. This prevents treating `RTE-7` as a specified deployment lifecycle. |
| `ABS-3` | Complete sampled Chapter 9 self-modification experiment | No canary traffic execution, production activation, behavioral read-back, or executed rollback. This prevents calling its accepted candidates observed self-improvement. |
| `ABS-4` | Full Chapter 10 prose/reference answers plus sampled manager implementation | No general enforcement path for child-capability attenuation, secret partition, aggregate action bounds, durable message recovery, or distributed settlement. This prevents treating prompts, tool lists, browser contexts, or an in-process lock as a deployment isolation/consistency guarantee. |
| `ABS-5` | Frozen-tree search for two Chapter 7 ledger-listed result paths | The named full 7-3 and 7-4 evidence files are not present. This prevents upgrading the corresponding manuscript tables from reported operation to an audited retained run. |
| `ABS-6` | Saved Chapter 6 acceptance runner and artifacts | No model call or `AgentRuntime` semantic event path occurs in that campaign. This prevents calling its passed subprocess gates observed asynchronous-agent judgment. |
| `ABS-7` | Complete sampled Chapter 2 compression path plus the full chapter and answers | No independent semantic-faithfulness gate checks the compressed result against its source. This prevents claiming preservation of qualifiers, negation, provenance, or decision-relevant meaning. |
| `ABS-8` | Complete 60×4 Chapter 3 sequential-memory runner and canonical result | No otherwise matched no-memory arm exists. This prevents attributing answer quality causally to memory presence, even though retention, read-back, context presence, and cued activation are observed. |
| `ABS-9` | Complete sampled Chapter 10 manager, worker, and bus path | No independent coordinator-side verifier acts before first-result settlement. This prevents calling the winner the first verified result; the route selects the first model-reported `target_found`. |

### Behavioral-authority paths

| ID | Consumer, channel, force, and horizon |
|---|---|
| `BAP-1` | Model consumes prompt, status, Skill, or tool specification through request context; it guides or prescribes model choice for the current call/run, but remains model-mediated. |
| `BAP-2` | Model consumes a tool result or event through a later request; it supplies evidence or a request with provenance-dependent force for that invocation. |
| `BAP-3` | Later model invocation consumes selected user memory or knowledge through pushed context or a retrieval tool; it is advisory evidence unless another contract raises its force, and may persist across sessions. |
| `BAP-4` | Maintainer, updater, or release runner consumes evaluation evidence through traces, reports, or manifests; force ranges from advice to an enforcing candidate gate for the declared campaign. |
| `BAP-5` | Later runtime consumes an accepted knowledge, instruction, program, or checkpoint artifact through retrieval, loading, installation, or serving; its force and horizon depend on artifact class. The general path is **claimed**; sampled production activation is not established. |
| `BAP-6` | Subagent consumes a task/handoff through prompt, message, and artifact references; it binds or guides the delegated run, while isolation and permissions require separate enforcement. |
| `BAP-7` | Executor consumes a codified guard through a predicate at the mutation boundary; it has binding permit/deny force for one mediated action. |

## Runtime account

The book's operative center is a host-owned loop even though the memorable formula names only model, context, and tools. Chapter 1 explicitly expands that formula into a Model–Harness structure: the Harness builds context, exposes tools, maintains loops and state, and applies permissions, verification, and correction ([boundary and Harness](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter1.md#L11-L29)). This closes the apparent gap with [Commonplace's tool-loop definition](../notes/agent-is-a-tool-loop.md). The difference is vocabulary: the book calls event triggers, communication, Skills, and subagent delegation part of a broad “tool system,” while Commonplace records trigger, scheduler, instruction, coordination, action, and state routes separately because they have different owners and guarantees.

The representative Chapter 1 runtime makes the control boundary concrete. It constructs a request, calls an external provider, parses model output, executes recognized tools sequentially, appends results, and repeats until terminal text, an error, or an iteration limit ([loop implementation](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/chapter1/context/agent.py#L703-L958)). The host—not the model—owns the tool map, execution, state, and stop. Its ordinary success marker means that a non-empty terminal answer was produced, not that the task was correct.

The claim-relevant alternates expose useful forcing cases:

- `NO_HISTORY` filters what the provider receives but retains the instance's internal trajectory. It is a request-construction ablation, not a stateless runtime.
- `NO_TOOL_RESULTS` still executes calls and returns protocol-shaped empty tool messages. It removes result content, not the tool-result event.
- No-tools and no-reasoning arms alter the capability or model-visible reasoning contract. The retained run found no degradation from the no-reasoning arm, so the repository removed the corresponding broad claim rather than explaining the result away ([Chapter 1 experiment ledger](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/chapter1/EXPERIMENT_LEDGER.md#L1-L16)).
- Malformed JSON, unknown tools, provider exceptions, empty replies, and the maximum-iteration cap route to explicit errors or bounded termination. Those are host invariants over the sampled path, not correctness guarantees.
- The included Python interpreter restricts built-ins but runs in process and includes file/remote PDF access. That is a capability surface, not evidence of an OS isolation envelope.

The book generalizes the loop well. Dynamic tool discovery changes which schemas enter `RTE-2` and which names the host may dispatch. Event-driven interaction changes when a turn begins and where cancellation is safe. Multi-agent coordination changes who receives a subtask and how results return. None of these transfers scheduling or action ownership into model weights.

Load-bearing guarantees remain path-specific:

| Property | Owner and enforcement point | Status and strength | Limit |
|---|---|---|---|
| Maximum Chapter 1 iterations and recognized tool dispatch | `CMP-1`, loop counter and tool map | **wired** invariant on `RTE-1` | Bounds execution; does not establish task correctness or deployment isolation. |
| Refund eligibility on the sampled codified path | `CMP-3`, server predicate before mutation | **wired** invariant relative to implemented policy through `BAP-7` | Exact execution can implement the wrong business rule. The paired campaign found no performance gain. |
| Queue, cancellation, and completion bookkeeping | `CMP-1`, event dispatcher/task manager | **wired** invariants for the teaching route; subprocess mechanics **observed** | Semantic urgency is a replaceable policy and was not exercised by the retained campaign. |
| Evaluation result shape and bounded task reset | `CMP-5`, runner and verifier | **wired** protocol/invariant for named campaigns | A shaped result or passed gate does not guarantee semantic discrimination or deployment acceptance. |
| Candidate isolation and canary decision | `CMP-5`/`CMP-6`, fixed runner checks and external sandbox | Current route **wired**; historical older-byte decision **observed**; invariant over mediated writes plus an external sandbox contract for candidate execution | Grants canary eligibility only; activation and rollback actuator are outside the sample. |
| First settlement in sampled manager route | `CMP-7`, one-process lock and settled flag | **wired** invariant inside one event loop | No independent coordinator-side verifier, crash recovery, or distributed consensus. |

## Lens scopes and outputs

The full memory/context and epistemic lenses were both triggered. The book makes retained-memory, later-context, knowledge-production, evaluation, and behavior-change claims across nearly every chapter, so a surface treatment would have hidden the transitions that matter. Both lenses therefore used **full** scoping over the complete English artifact and the representative code/result boundary. The subject remained a general agent-architecture book rather than a memory system, so the legacy agent-memory review route was not detected and was not invoked.

### Memory and context lens

The useful question is not simply whether the repository contains memory. It is whether bytes are retained, selected later, delivered into an operative path, used by the receiving model, and responsible for an outcome. Those are different transitions:

| Inspected path | Retention, read-back, and activation status | Evidence-bounded consequence |
|---|---|---|
| Chapter 1 agent instance across separate `execute_task` calls | State retention and the later request path are **wired**. `NO_HISTORY` filters the provider request but does not delete the internal trajectory. Cross-call operation and activation were **uninspected**. | The ablation is about request construction, not a stateless runtime or a deletion policy. |
| Chapter 3 sequential memory-state campaign, 60 cases × four representations | Retention, sequential read-back, final memory-only context presence, and use in explicitly memory-cued answers are **observed**. Pass counts were 48/60 notes, 52/60 enhanced notes, 51/60 JSON cards, and 49/60 advanced cards ([runner](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/chapter3/user-memory/run_evaluation.py), [result](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/chapter3/user-memory/validation/latest.json)). | The route demonstrates retained state and cued use. `ABS-8` leaves memory-versus-no-memory benefit and ordinary unprompted activation **uninspected**. |
| Chapter 3 agent-directed pull retrieval | Generated queries, selected raw chunks, answer context, answers, and judge records are **observed** in the 60-case campaign. | It demonstrates agent-directed retrieval and cued use, not the causal advantage of iterative agent search: no live matched non-agentic arm exists. |
| Plain, contextual, and dual-layer retrieval | Holding queries fixed, prefixes changed ordered BM25 selection in 48/60 cases and the selected set in 36/60: that selector effect is narrowly **causally supported**. Downstream pass/reward moved from 47/60 and 0.775, to 52/60 and 0.8135, to 57/60 and 0.9167 ([result](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/chapter3/contextual-retrieval-for-user-memory/validation/latest.json)). | The downstream differences are only **observed**. The answer prompt and joint judge saw arm labels, the campaign used one seed, and no calibrated blinded inferential protocol was retained. Prefixes affected selection; they did not enter answer context. |
| Chapter 9 accepted program candidate | Candidate bytes, checks, hashes, and canary eligibility are **observed** for historical producer bytes; later consumption is **absent** in the sampled experiment. | Retention is not persistent adaptation. No canary traffic, production activation, adherence, benefit, or executed rollback was observed. |
| Chapter 10 message bus | Current-run message history, settlement, termination, and cleanup are **wired**; historical mechanics are **observed**. | The bus is coordination state, not durable cross-process memory. First-result settlement also does not verify the winning payload. |

The memory objects also have different authority. Raw conversations and tool results are evidence records. Extracted notes, summaries, contextual prefixes, diagnoses, and handoffs are derived artifacts that may omit qualifications or add claims. Reviewed source, where the book's production KB workflow is followed, can acquire a bounded acceptance record. Serving indexes and rankings remain derivatives: they make material findable but add no truth authority. The teaching user-memory implementation is intentionally weaker than that doctrine because it lets one model mutate JSON directly and pushes the complete store into later calls.

### Epistemic lens

Here, *truth-apt* means capable of being true or false; an *ampliative* transformation adds a claim that is not entailed by its inputs. These distinctions prevent a successful operation from silently becoming evidence for a stronger claim.

| Transformation or disposition | Representative book routes | Supported interpretation |
|---|---|---|
| Acquisition/import | Tool results, events, conversations, web pages, corpora, and demonstrations | Provenance can preserve who reported what. Import does not make the report true, complete, fresh, or instruction-authoritative. |
| Non-ampliative reshaping or entailed derivation | Deterministic grouping, counts, formal predicates, verifier outputs, and statistics over warranted inputs | The result is warranted only inside the encoded target, input, computation, and validity window. Indexing, compression, extraction, and preprocessing remain indeterminate when semantic preservation is unchecked. |
| Ampliative candidate production | Generalized preferences, factor hierarchies, model answers, judge verdicts, root-cause diagnoses, impact predictions, synthetic answers, and research syntheses | These are conjectures until a separate evaluator checks a named target and an acceptance decision records intended use and scope. Retention or confident wording adds no warrant. |
| Disposition and integration | KB review/merge, dataset admission, run acceptance, candidate gate, canary/deployment, later serving | Each accepts a different object for a different use. Protocol completion, task success, hypothesis support, canary eligibility, deployment, and later benefit are not interchangeable. |
| Direct behavior adaptation | Generated program changes, SFT/RL gradients, checkpoint replacement, and rollback | When no individual proposition is asserted, these are policy changes rather than knowledge claims. They still require behavioral evaluation and operational governance. |

Chapter 9 contains the strongest inspected discovery-and-selection segment. Historical failure evidence is grouped; a diagnosis and expected effects are proposed; external compile, replay, regression, compatibility, safety, and hash checks are applied; two candidates reach canary eligibility and a negative control is rejected. That acceptance licenses the tested candidate for a canary, not the diagnosis as the unique cause, general transfer, deployment, or improvement. The lifecycle stops before later activation.

The book also separates three kinds of authority in practice, even when it does not always name them separately:

| Authority | What establishes it | What it does not establish |
|---|---|---|
| Behavioral authority | A prompt, retrieved memory, result, handoff, installed artifact, or weight path reaches a consumer and can influence behavior. | Truth, permission, or successful activation. |
| Epistemic authority | A source or evaluator warrants a claim for a named target, domain, and scope. | The right to execute an effect or deploy an artifact. |
| Operational authority | Host code, an executor predicate, gate, coordinator, or operator can permit, block, settle, deploy, or roll back a transition. | Truth of the payload or correctness outside the mediated path. |

This distinction explains several apparent successes. A one-process lock has operational authority to settle a race, but no epistemic authority over the winner's profile. A refund predicate has operational authority on the mediated mutation path and exact semantics relative to its code, but execution does not prove that the code matches the intended business rule. A prompt or tool list can influence or restrict model choice, but it is not by itself a grant set or isolation envelope.

## Cross-lens reconciliation

The lenses converge on five anti-conflations:

1. **Storage is not read-back.** Chapter 9 retains accepted candidate files without any sampled later consumption. Chapter 10's bus retains only current-run coordination state.
2. **Read-back is not activation or benefit.** The later targeted Chapter 3 inspection supersedes the packet-limited claim that activation was unobserved: cued answer use is **observed**. The no-memory counterfactual and unprompted use remain **uninspected**.
3. **Context presence is not semantic preservation.** Compression and memory extraction can reshape truth conditions; contextual prefixes can change ranking without entering model context; retrieval rank supplies no warrant.
4. **Operational selection is not epistemic acceptance.** A protocol can complete, a race can settle, or a candidate can pass a gate without verifying the stronger hypothesis, payload, or deployment claim.
5. **Retained acceptance is not lifecycle integration.** The book's strongest sampled updater stops at canary eligibility, and Chapter 8 leaves checkpoint serving and rollback outside a complete named route.

These conclusions amend, rather than replace, the canonical route register. `RTE-3` now distinguishes complete-store push, sequential memory rewriting, agent-directed pull retrieval, and index-side contextual selection. `BAP-3` records selected raw chunks—not contextual prefixes—as the answer-model input. `RTE-5` and `BAP-5` remain incomplete until an accepted artifact is actually consumed later.

## Where the book and Commonplace agree

### The agent is the situated loop, not the model alone

The formula `Agent = LLM + Context + Tools` is pedagogically compressed, but the book does not commit the common error of equating an agent with an autonomous model. It explicitly assigns context construction, state, tool execution, stopping, permissions, verification, and correction to the Harness. Commonplace's [agent-as-tool-loop](../notes/agent-is-a-tool-loop.md) and [optional-loop](../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) accounts draw the boundary more operationally, but the causal allocation agrees. The model proposes; host code situates, executes, and bounds.

### Context engineering is information supply under a budget

Chapter 2 defines context engineering as selecting and structuring everything the model actually sees, including rules, tool descriptions, task state, and retrieved knowledge—not as polishing one prompt ([Chapter 2 opening](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter2.md#L1-L35)). It also calls context an organizational and documentation problem. This is almost the same claim as Commonplace's [context-engineering definition](../notes/definitions/context-engineering.md): route the right knowledge into a bounded context at the right time, with scoping and maintenance as part of the job.

### Progressive disclosure is the default answer to large capability libraries

The book's Skill catalog, hierarchical knowledge summaries, dynamic tool schemas, and subagent isolation all follow one rule: keep discriminating metadata visible, then load detail only when a task selects it ([Skills](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter2.md#L762-L829)). Commonplace agrees through [Skills as instructions plus routing and execution policy](../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [frontloading](../notes/frontloading-spares-execution-context.md), and curated navigation. Both treat discoverability and selective loading as architectural properties, not search-engine conveniences.

### Raw accumulation is not usable memory or knowledge

Chapter 3 separates the append-only trajectory from repeatedly rewritten, merged, and pruned long-term memory ([trajectory versus memory](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md#L72-L86)). Its production knowledge workflow goes further: raw evidence stays immutable, a proposer submits the smallest complete diff, an independent reviewer returns to the evidence, and derived indexes are rebuilt after acceptance ([governed update](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md#L503-L532)). This agrees with [raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), with Commonplace's source/library separation, and with the rule that indexes are derived serving artifacts rather than the authority for a claim.

### Files, links, indexes, and Git are a serious knowledge substrate

The book endorses plain-text, filesystem-organized knowledge when it is linked, indexed, progressively summarized, version-controlled, and reviewed. It explicitly warns that a flat pile of files becomes less retrievable as it grows. That matches Commonplace's position that agent memory needs [discoverable, composable, trusted knowledge](../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md), not a folder whose existence is mistaken for contextual availability.

### Storage, delivery, and behavioral effect are separate

Across Chapters 2, 3, and 9, the book distinguishes retained history from the context actually sent, retained candidates from activated capabilities, and updater validity from later adherence and benefit. Commonplace makes the same separations in [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The book's Chapter 3 experiments add useful bounded evidence: memory and retrieval routes are exercised, while the Chapter 9 self-modification experiment stops honestly at canary eligibility.

### Natural language and symbolic mechanisms should be combined by function

The book uses language for open-ended interpretation and code for exact scheduling, predicates, schemas, and effects. Its best example has a server recompute refund eligibility from trusted state before mutation, rather than trusting a model-supplied checklist. Commonplace's [codification definition](../notes/definitions/codification.md) and [codify-versus-model heuristics](../notes/codify-versus-llm-decision-heuristics.md) make the same allocation: symbolic execution narrows interpretation where the specification and oracle support it; model judgment remains useful where the target cannot yet be completely stated.

### Security guarantees must sit outside the attacked context

The book says a model inside the context being attacked cannot guarantee that it detects injection. It therefore layers context defenses beneath external execution review and stable data-layer constraints ([guardrail layers](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter1.md#L454-L476)). Commonplace's [privilege-quarantine](../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) account reaches the same conclusion: a low-privilege reader of untrusted material and a separately governed actor are stronger than asking one privileged context to ignore hostile text.

### Evaluation is a typed evidence pipeline, not one score

Chapter 7 evaluates the model-plus-Harness system, not the model in isolation. It asks for task definitions, resettable state, tools, protocols, verifiers, full trajectories, paired comparisons, statistics, and first-error attribution ([evaluation object](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter7.md#L1-L23), [failure attribution](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter7.md#L441-L531)). Commonplace likewise says [verification needs a typed target](../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) and that [diagnostic richness bounds outer-loop learning](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Both distinguish task outcome, process evidence, causal attribution, acceptance, operational continuation, and warrant.

### Continual evolution is proposal, selection, retention, and activation

Chapter 9 opens by rejecting the idea that stored experience is already learning. Its strong route is immutable evidence → diagnosis → local candidate → independent checks → release decision → activation/adherence measurement → consolidation and rollback ([continual-evolution loop](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md#L3-L90), [release and activation](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md#L271-L317)). This agrees with [proposal-selection requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and with [governing behavior-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md).

### Change can live in context, instructions, programs, or weights

The book repeatedly asks builders to fix a failure in the cheapest, most inspectable adequate carrier before retraining. Chapter 8 reserves dynamic or citation-sensitive facts for retrieval and uses weights for distributed capabilities that are not cleanly expressible outside the model ([carrier choice](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter8.md#L389-L411), [chapter synthesis](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter8.md#L801-L833)). Commonplace similarly treats continual learning as [co-evolution across representational forms](../notes/treat-continual-learning-as-representational-form-coevolution.md), not as a synonym for fine-tuning.

### Multi-agent value requires separation and coordination

Chapter 10 does not argue that more agents automatically improve answers. It makes new information a strong first value test, while its reference answer also names different objectives and context isolation as benefits ([value test](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter10.md#L47-L76), [reference answer](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/reference-answers.md#L392-L397)). The chapter then adds a data plane, control plane, permissions, status, budgets, cancellation, settlement, and failure handling ([data/control plane](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter10.md#L103-L191)). This agrees with Commonplace's [multi-dimensional orchestration space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md), [coordination guarantees](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), and rule that [synthesis is not error correction](../notes/synthesis-is-not-error-correction.md). Commonplace additionally foregrounds control benefits—privilege separation, scheduling, persistence, recovery, and accountability—that need not add information to an answer.

### Negative evidence is part of the result

The repository often corrects its own prose expectations instead of converting a passed protocol into a success story. Active tool discovery achieved equal accuracy in both three-task arms; the codified-rule treatment did not significantly beat control; one distillation experiment produced a nonsignificant gain; a multi-agent society intervention failed to diffuse its custom event. The status ledger retains those negative results beside completed gates ([selected statuses](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/docs/EXPERIMENT_STATUS.md#L28-L73)). This is one of the strongest practical agreements with Commonplace's evidence discipline.

## Where the book and Commonplace diverge

The table distinguishes a real disagreement from a difference in vocabulary, default, scope, or evidence. This matters because the book often supplies, in a later chapter or reference answer, a qualification that closes an apparent early conflict.

| Kind | Divergence | Consequence |
|---|---|---|
| Genuine retention-policy disagreement | Chapter 3 lets an extraction call retain facts it judges “useful later,” guided by selectivity, abstraction, and structure ([memory admission](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md#L15-L41)). Commonplace requires [a declared output specification](../notes/open-domain-memory-retention-needs-a-declared-output-spec.md) before open-domain material is admitted. | The book's heuristic can produce a plausible store without a stable contract for what the store is for, what must be excluded, or how future usefulness is judged. Its later evaluation framework helps but does not replace the admission specification. |
| Unsupported epistemic inference | Chapter 5 says that code which runs proves its own logical consistency and that its execution result supplies an objective correctness standard ([opening claim](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter5.md#L3-L11)). | Successful execution establishes a much narrower property: one program reached a result under one environment and input. It does not establish that the requirements, translation into code, environment model, or result oracle are correct. Chapter 7's own typed-target and verifier methodology supplies the missing qualifications. |
| Governance-granularity difference | Chapter 9 says that a business Agent must not modify the validators, tests, thresholds, audit logs, or backups that approve **its own** updates ([safety boundary](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md#L331-L364)). Commonplace says [machinery persists by warrant, not position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md): a distinct higher-governance loop may revise that machinery. | The current-gate invariant agrees: a candidate cannot rewrite its own exam. The book does not say whether a separate authority may revise the safety root, so this is an underspecified governance level, not an established disagreement about permanent immutability. |
| Definition versus safety policy | The book normatively reserves “self-evolution” for a candidate, independent regression/safety checks, and release gate. Commonplace's [self-improving-system definition](../notes/definitions/self-improving-system.md) also classifies direct, gateless evidence-responsive self-change, while treating proposal selection as a safer subtype. | This is not advice to deploy gateless updates. It keeps a descriptive membership test separate from the safety architecture used to govern one pathway. |
| Default/scenario tradeoff | Chapter 2 presents the complete accumulated interaction as the direct lossless ReAct context, with compression when production constraints demand it ([history baseline](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter2.md#L31-L36), [second request](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter2.md#L185-L231)). Commonplace says [session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md). | The book optimizes first for a lossless single-task baseline; Commonplace optimizes first for task-shaped selection from durable artifacts. The book's later compression, progress documents, and context isolation narrow the difference substantially. |
| Analytical-granularity difference | The book calls user memory and a shared knowledge base “the same problem at different scales” because they share retrieval, compression, staleness, and conflict mechanisms ([Chapter 3 framing](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md#L3-L9)). | Commonplace treats their scope, subject, privacy, evidence, authority, write policy, and maintenance lifecycle as independent axes. Shared technology does not establish one problem identity. |
| Evaluator-form policy difference | Chapter 3 says both proposer and reviewer “must be Agents,” because both need open-ended search, evidence retrieval, comparison, and tests ([review workflow](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md#L503-L516)). | Commonplace selects human, deterministic, or model evaluators by target and oracle. A review role may need agentic execution in this scenario, but “Agent” is not a universal validity condition for proposal or acceptance. |
| Analytical-granularity difference | Chapter 9's four update carriers—experience knowledge, prompts/Skills, programs/Harnesses, and parameters—combine artifact role with encoding. | Commonplace's [representational form](../notes/definitions/representational-form.md) is orthogonal to behavioral authority: knowledge and a Skill may both be natural language while one advises and the other binds. The book's list is useful routing doctrine, not a form taxonomy. |
| Unsupported causal inference | Chapter 7 suggests that no gain from a stronger model identifies the Harness as the bottleneck ([model-versus-Harness diagnosis](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter7.md#L9-L23)). | No gain is also compatible with metric ceiling/noise, saturation, distribution mismatch, model–Harness interaction, or another unchanged limit. A discriminating intervention is required before causal closure. |
| Scenario/default tradeoff | Chapter 4 prefers general executors when composition is cheap, and Chapter 5 presents a coding agent plus filesystem as the core of open-ended general agents. Commonplace starts from specification completeness, oracle strength, failure cost, and host-controlled composition. | Both accept hybrid designs. The book gives a builder default for open-ended digital work; Commonplace gives decision conditions and keeps the framework's internal loop optional. |
| Analytical-granularity difference, with translation uncertainty | Chapter 10 begins with shared/isolated context × peer/manager/decentralized topology as its basic map, then separately covers data/control planes, lifecycle, budgets, permissions, settlement, and failures. The [community English introduction](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/introduction.md#L41-L60) also calls multi-agent collaboration the “ultimate form,” but the [canonical Chinese introduction](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book/introduction.md#L45-L58) at the same commit only describes an extension to system-level collaboration. | Commonplace makes scheduler, decomposition, context, persistence, authority, guarantees, and return artifacts co-equal classification axes instead of treating two as the introductory grid and the rest as later operating concerns. This is not a source-wide omission. The English phrase should not be elevated into a canonical maturity ladder. |
| Predictive-emphasis difference | The afterword predicts that stronger models will absorb fixed-task layers of the Harness while new Harness functions recur at the capability frontier ([co-evolution](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/afterword.md#L27-L35)). Commonplace likewise distinguishes decomposition on a fixed task from a frontier that model improvement can reopen. | The accounts substantially agree. The residual difference is modal: the book predicts recurring frontier expansion categorically, while Commonplace leaves the future natural-language, symbolic, parametric, or mixed decomposition contingent. |
| Doctrine–teaching-implementation gap | The production doctrine requires evidence-bearing PRs, independent retrieval, permissions, and external gates. Some demos instead let one model directly mutate JSON, push the whole memory store into every call, compress without a semantic checker, or settle the first model-reported result. | These samples are intentionally legible teaching paths. They show that the repository implements weaker routes than it recommends; they should not be reported as the book's preferred production architecture. |
| Security-granularity difference | The book correctly moves guarantees to execution/data layers, but usually discusses tool lists, permission policies, sandboxes, and VFS zones together. | Commonplace separately records capability surface, grant set, isolation envelope, privilege quarantine, and aggregate authority. The direction agrees; Commonplace makes it harder to infer isolation from an allowlist or container label. |

Two suspected divergences do **not** survive full-book reading. First, the three-term agent formula does not omit the runtime once Chapter 1's Model–Harness expansion is included. Second, the book does not claim that SFT always memorizes while RL always generalizes; Chapter 8 explicitly bounds that slogan to a tendency under named experimental conditions. Treating either as a fundamental conflict would misrepresent the source.

## Chapter-by-chapter comparison

| Chapter | Main contribution | Strongest agreement | Strongest divergence or qualification | Evidence ceiling |
|---|---|---|---|---|
| [1 — Fundamentals](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter1.md) | Model–Harness account, tool loop, observation/action spaces, guardrails, recurring patterns | Agent behavior belongs to a host-owned loop with external constraints and stop conditions | The word “tools” covers triggers, communication, Skills, and delegation that Commonplace keeps analytically separate | Representative loop **wired**; five-arm result **observed**; no deployment |
| [2 — Context engineering](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter2.md) | Context construction, cache discipline, source marking, Skills, compression, isolation | Context is a scarce information-supply system; progressive disclosure and isolation beat indiscriminate loading | Complete history is the lossless baseline; Commonplace starts from task-shaped next-context selection. Sample compression has no semantic-preservation checker | Doctrine plus selected **wired** demos; causal support is route-local |
| [3 — Memory and knowledge bases](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter3.md) | Cross-session memory, retrieval, structured indexes, filesystem KBs, governed maintenance | Raw evidence, reviewed knowledge, and serving indexes are separate; changes should be small, reviewable, and reversible | “Useful later” admission, memory/KB identity, and mandatory agent reviewers are stronger than Commonplace accepts. Teaching demos are weaker than the chapter's production doctrine | Several write/read-back routes **wired** and retained campaigns **observed**; benefit/causality varies by ablation |
| [4 — Tools](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter4.md) | Tool interface fidelity, discovery, MCP, execution safety, collaboration surfaces | Capability disclosure, permission, execution, and feedback are distinct host responsibilities | General-executor default is less conditional; the broad design does not fully specify identity, revocation, credential delegation, and isolation as one protocol | Discovery route **wired**; three-task result **observed**, with equal accuracy |
| [5 — Coding agents](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter5.md) | Code as meta-capability, artifacts, business-rule codification, bootstrapping | Use code for exact, trusted checks while language handles incomplete/open interpretation | Successful execution does not by itself prove logical consistency relative to the intended specification or make the result an objective correctness oracle; coding agent plus filesystem is a scenario thesis, not a universal agent core | Refund guard **wired**; 60-pair no-gain result **observed** |
| [6 — Interaction](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter6.md) | Provenance-bearing events, safe points, cancellation, voice/computer/robot loops | Symbolic scheduling and low-level safety should surround slower semantic model decisions | The retained “real” campaign tests subprocess mechanics, not the advertised semantic event route | Runtime **wired**; mechanics **observed**; model routing **uninspected** by that campaign |
| [7 — Evaluation](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter7.md) | Whole-system tasks, verifiers/judges, traces, metrics, statistics, scientific iteration | Typed targets, oracle-bounded conclusions, diagnostic traces, paired comparisons, and stage gates | A no-gain model swap does not uniquely identify a Harness bottleneck; two ledger-listed result bundles are absent | Strong doctrine; bounded campaigns **observed**; no book-wide causal conclusion |
| [8 — Post-training](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter8.md) | Pre-/mid-training, SFT, RL, reward, data/environment design, carrier choice | Post-training is one behavior-change carrier; dynamic/citable facts often belong outside weights | Checkpoint acceptance, serving activation, monitoring, and rollback ownership are underspecified | Book-wide route **claimed**; external training/serving **uninspected** in this sample |
| [9 — Continual evolution](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md) | Evidence capture, diagnosis, four update carriers, candidate gates, consolidation, rollback | Retention is not demonstrated improvement; the recommended governed path separates candidates, independent checks, activation, later benefit, and recovery | The book protects the current approval machinery from the business Agent it governs but leaves higher-governance revision unspecified | Candidate-to-canary route **wired**; historical older-byte decision **observed**; activation absent |
| [10 — Multi-agent collaboration](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter10.md) | Context/topology patterns, data/control planes, handoffs, settlement, failure handling | Multiple agents help through new information, distinct objectives, or controlled separation plus explicit coordination | The opening two-axis grid does not classify all later control-plane dimensions; the English “ultimate form” phrase is translation-specific; sampled first-result settlement lacks independent verification | Manager route **wired**; historical run **observed**; no distributed/deployment guarantee |

The afterword's useful synthesis is that model and surrounding agent system co-evolve: fixed-task functions may move into stronger models while new Harness functions emerge at the frontier. Commonplace substantially agrees; it states the recurrence as a contingent decomposition choice rather than a categorical forecast.

## Scenario-relative assessment

The book is most useful to Commonplace as convergent architectural doctrine and as a catalogue of small forcing cases. It is not a competing deployed system and should not be scored as one.

| Setting | Assessment | Practical use |
|---|---|---|
| Teaching or designing a general digital agent | **Strong agreement.** The Model–Harness split, bounded context, tool loop, external checks, and failure-led iteration are sound starting points. | Use the book's sequence and examples; preserve Commonplace's finer route and authority distinctions when turning them into a system contract. |
| Building a production memory or KB subsystem | **Agreement on the mature doctrine; real divergence at admission and evaluation.** The reviewed-source/index workflow is strong, while “useful later” capture and mandatory agent reviewers are too broad. | Require a declared output specification, source-grounded acceptance, evaluator choice by typed target, freshness rules, and an explicit read-back/activation test. |
| Safety-critical or irreversible tool use | **Directional agreement, insufficient deployment evidence.** The book puts predicates and safety controls outside attacked context, but sampled mechanisms establish only named mediated paths. | Specify capability surface, grant set, isolation envelope, privilege boundaries, alternate paths, and aggregate authority independently. |
| Continual improvement of symbolic artifacts | **Strong middle-loop agreement.** The Chapter 9 candidate, regression, safety, lineage, and canary gate are the book's best implemented governance example. | Adopt the candidate-selection structure, but do not call the sampled change an improvement until later activation and objective-relative behavioral benefit are observed. Monitoring and rollback are separate governance and recovery requirements. |
| Post-training and weight updates | **Conceptual agreement, incomplete lifecycle.** Failure localization and carrier choice are good; the full checkpoint release path is absent. | Treat training as one behavior-change carrier and add named data admission, checkpoint acceptance, serving, monitoring, and rollback owners. |
| Multi-agent systems | **Conditional agreement.** New evidence, distinct objectives, private work, control boundaries, budgets, and verification can justify orchestration; agent count is not a maturity measure. | Start from information gain or control/isolation benefit and cost, then choose scheduler, decomposition, context, authority, persistence, guarantees, and return artifacts separately. |

Concrete evidence could change this assessment:

- A systematic canonical-Chinese comparison could confirm or remove wording-level tensions currently attributed only to the community English translation.
- An integrated entry path exercising the advertised runtime, memory, evaluation, update, security, and deployment routes could raise the overall evidence tier above `doc-grounded`.
- Repeated, arm-neutral, blinded memory studies with an otherwise matched no-memory control could establish whether retention and retrieval cause downstream benefit, not merely cued use.
- An observed raw-evidence → proposer → independent review → merge → rebuilt index → later reliance route could close the doctrine–implementation gap in Chapter 3.
- Canary traffic, production activation, and repeated objective-relative benefit could turn Chapter 9's retained candidate-selection result into evidence about persistent adaptation. Observed monitoring and rollback paths would separately strengthen its deployment governance and recovery claim.
- Independent source-to-field verification before Chapter 10 settlement, plus durable recovery and enforced child-authority attenuation, could support stronger epistemic and distributed-system guarantees.

## Limitations

| Status | Boundary or gap | Conclusion it prevents |
|---|---|---|
| `uninspected` | The complete English artifact was read, but only one translation-sensitive phrase was checked against the canonical Chinese. | No book-wide claim about exact canonical wording, omissions, or emphasis. |
| `uninspected` | Companion implementations and retained results were sampled purposively rather than exhaustively across all 93 English projects. | No repository-wide implementation or behavior claim from a sampled route; a sample-local absence remains local unless a full-tree search is recorded. |
| `uninspected` | Providers, external tools and servers, browsers, training/serving stacks, deployment controllers, human review, and physical environments remained outside the boundary. | No claim about their permissions, isolation, fidelity, availability, current checkpoint, or deployed behavior. |
| `uninspected` | No fresh credentialed experiment or deployment run was performed. Several retained artifacts identify historical, older, dirty, or incomplete producer provenance. | No transfer of historical observations to frozen current code and no new causal intervention. |
| `absent` | `ABS-1`: there is no integrated book-wide runtime/deployment path in the complete repository boundary. | No system-wide reliability, security, memory coherence, recovery, or continual-improvement grade. |
| `absent` | `ABS-2`, `ABS-3`, and `ABS-9`: checkpoint lifecycle, sampled candidate activation, and sampled independent result verification do not complete; the sampled updater also has no executed rollback path. | No claim of governed post-training deployment, observed improvement from the retained candidate, verified multi-agent settlement, or demonstrated updater recovery. |
| `absent` | `ABS-7` and `ABS-8`: sampled compression lacks a semantic-preservation gate and sequential memory evaluation lacks a no-memory arm. | No general preservation guarantee for compressed context and no causal memory-benefit estimate. |
| `uninspected` | Commonplace comparison claims are frozen at `b006c9d7`; later procedure edits are not comparison evidence. | No claim that this report assesses every later Commonplace procedural change. |

## Verification

- Target identity was resolved to clean commit `a18a5f764589396d903d8faeaed205489a21bf4b`; the source checkout was not modified.
- The complete English introduction, Chapters 1–10, afterword, and reference answers were divided into three chapter packets and read completely. Packet hashes were `e9ebcc6c…`, `02ca086a…`, and `feabe4e5…`.
- Independent memory/context and epistemic lens reports were read completely and verified at SHA-256 `26f77f9e…` and `f37acf3a…`; their conflicting activation statements were reconciled using the later targeted Chapter 3 inspection.
- Source, component, object, route, claim, absence, and behavioral-authority identifiers are used consistently. Observation is not transferred across producer revisions or upgraded to causality without a discriminating design.
- `commonplace-validate kb/agentic-systems/ai-agent-book.md`: **PASS (clean)**; frontmatter, title, filename, local links, proposal boundary, and note schema all passed with no warnings or failures.
- `commonplace-validate kb/agentic-systems/README.md`: **PASS (clean)**; the collection landing edit passed with no warnings or failures.

---

Relevant Notes:

- [Agent is a tool loop](../notes/agent-is-a-tool-loop.md) — rests-on: supplies the operative boundary that reveals the book's three-term formula as a compressed interface view rather than a rival architecture.
- [Open-domain memory retention needs a declared output specification](../notes/open-domain-memory-retention-needs-a-declared-output-spec.md) — compares-with: states the clearest genuine retention-policy divergence.
- [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: separates retained bytes, later delivery, cued use, and causal benefit across Chapters 3 and 9.
- [Verification needs a typed target before it needs an oracle](../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) — rests-on: explains why code execution, protocol gates, judges, and statistics license different scopes.
- [A proposal-selection loop requires search, evaluation, and retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rests-on: locates the strength and stopping point of Chapter 9's candidate loop.
- [Agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — compares-with: expands Chapter 10's context/topology matrix without rejecting its conditional design advice.
- [Orchestration needs privilege quarantine, not permission scope](../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) — rests-on: bounds the book's tool-list, sandbox, and role-level security claims.
