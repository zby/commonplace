---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Source-grounded runtime baseline of Agent Skills for Context Engineering: skill delivery, research admission, router evaluation and selected persistent-context examples."
run-id: AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01
reviewed-boundary: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
---

# Agent Skills for Context Engineering runtime report

## Runtime account

### Claimed work and entry paths

The target distributes agent instructions and maintains those instructions through a file-based research workflow. It is not one enclosing runtime. External hosts supply discovery, model execution, permissions and any deployed sandbox. The [boundary](boundary.md) freezes SRC-1 and describes the complete-artifact, partial-loop scope. This report adds implementation inspection, not execution evidence. Operation, instruction compliance and benefit remain unobserved for the routes below.

The ordinary consumption path is installation of a skill directory or plugin, followed by host-selected loading and interpretation. The Open Plugins manifest supplies `./skills/`; the README also supports marketplace installation and manual copying. The claimed name/description-first policy is not a loader implemented by that manifest. [RT-RTE-skill-delivery](#rt-rte-skill-delivery) distinguishes symbolic discovery metadata from the natural-language guidance delivered after selection. [RT-BAP-skill-instruction](#rt-bap-skill-instruction) identifies its conditional authority. SRC-1, `.plugin/plugin.json`, `README.md`, `skills/context-fundamentals/SKILL.md`.

### An ordinary maintenance invocation, through return

A manual or scheduled `loop_step.py --allow-fetch` invocation reads configuration and retained queues. It first reaps closed runs, checks failure and parked budgets, then either creates a run from the oldest inbox item or advances the oldest active run by its `updated_at`. Creation is rechecked under the inbox lock and executed by a subprocess calling `research_loop.py init`. Initialization writes a source queue, thread, run state, evaluation draft and proposal scaffold and invokes repository validation. The invocation returns an initialized event rather than also fetching that source. A later step reloads initialized state, retrieves permitted HTTP(S) content, writes raw bytes and pointers, and invokes `research_loop.py retrieve` to record the retrieved state. A further step parks the run for evaluation. The next-step owner is then a human or judge agent, not an internal scheduler model. Failures produce parked/quarantine records and event/failure logs; no-op exits 78. [RT-RTE-research-step](#rt-rte-research-step). SRC-1, `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`.

The wider research-to-skill procedure is a protocol: an agent or human reads rubrics, evaluates sources, proposes changes, records novelty and prepares a PR. Explicit CLI subcommands record these stages; they do not implement a mandatory ordered transition guard. For example, `pr-ready` writes caller text and sets state without first calling run validation. Mechanism promotion is a separate append route with a readiness subprocess and a reviewer string, but with important forcing cases below. Its registry/ledger writes do not themselves edit published skill bodies or install them in hosts. [RT-RTE-mechanism-promotion](#rt-rte-mechanism-promotion). SRC-1, `researcher/runbooks/autonomous-research-loop.md`, `researcher/scripts/research_loop.py`.

### Material alternates and forcing cases

1. **Readiness bypass is a supported option.** The parser exposes `--allow-unready`; accepted/candidate proposals pass the promotion branch when it is true even if readiness fails. The reviewer argument must be nonempty, but the inspected branch does not authenticate its human origin. This narrows the README's promotion guarantee to a default-path protocol, not an invariant. SRC-1, `researcher/scripts/research_loop.py`.
2. **Closed-state validation is materially different.** A caller can use `close` to write a closure with a supported status and reason. `validate_run.py` then checks state and closure instead of active-run source, proposal, novelty and PR readiness. Promotion calls that validator and does not separately require an active state. Thus a supported close-then-promote sequence can satisfy this readiness predicate without passing active publish-readiness checks. This is an inspected code path, not a demonstrated executed bypass. SRC-1, `researcher/scripts/research_loop.py`, `researcher/scripts/validate_run.py`.
3. **No-paid-model claims do not cover all shipped callers.** The conservative scheduler parks judgment, whereas the router calls Cursor `Agent.prompt` and the optimizer calls an Anthropic-compatible endpoint. Router cost checks bound estimated plans and maximum attempts; they do not meter actual billed dollars. The effectiveness runner is only a planner/scaffold. [RT-RTE-router-benchmark](#rt-rte-router-benchmark), [RT-RTE-prompt-optimization](#rt-rte-prompt-optimization), [RT-ABS-effectiveness-executor](#rt-abs-effectiveness-executor).
4. **Queue atomicity is not universal.** Although inbox/parked/done operations shown in the step driver use named locks, its run-local retrieval queue update uses direct `write_text`. Manual `retrieve` also accepts no file and still records retrieved state. Neither the atomicity slogan nor a retrieved label establishes byte-complete evidence capture. SRC-1, `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`.

### Effects, authority and control envelope

Capability surface differs from current grants. The maintenance scripts can write repository-local files and launch Python subprocesses. Opt-in fetching uses urllib, checks HTTP(S) schemes, reads at most 1,500,001 bytes and writes at most 1,500,000, and supplies a 30-second urlopen timeout. The inspected function is not a domain allowlist or a demonstrated total-operation deadline. Fetch truncation is returned but the retrieved-state transition does not veto it. The repository's merge/push restriction is an instruction to agents/humans; the inspected workflow does not implement an OS credential or filesystem isolation boundary. Actual host grants, provider-native tools and remote execution behavior remain outside supplied evidence. SRC-1, `researcher/scripts/loop_step.py`, `researcher/runbooks/autonomous-research-loop.md`.

The router sends only rendered names/descriptions and the task through its own prompt construction, with `settingSources: []`. This is a working-context selection mechanism at the caller, not proof of every SDK-internal context exclusion. The digital-brain helper selects retained ideas/bookmarks/posts into a printed scaffold without a model call or persistence of that scaffold. The optimizer uses fresh capture/analyzer/optimizer requests rather than a shared accumulating context; capture itself accumulates assistant blocks and tool results until completion or its turn cap. API users can supply tool executors and iteration callbacks; the inspected CLI optimization call does not supply tools or an executor. These alternatives prevent attributing either universal tool confinement or general task correctness to the optimizer. SRC-1, `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`.

### Coverage added and limits retained

Added SRC-1 implementation coverage includes full router/shared utilities/effectiveness runner, full run-readiness validator and step driver, research-loop recording/promotion/parser paths, the full digital-brain draft consumer, optimization-loop orchestration, capture's nonstreaming/tool-executor path, optimizer request construction, skill-generation write path and CLI artifact reload. Added doctrine coverage includes the research runbook, README and context-fundamentals body; the plugin manifest is configuration evidence. Streaming capture, analyzer parsing/fallback internals, skill-generator model-output parsing, export/CAS enforcement, the remaining examples, CI and helper scripts are not fully traced here. They remain available but uninspected, not absent. No whole-system safety, privacy, learning or performance conclusion follows.

## Shared records

### Components

#### RT-CMP-cursor-model
Label: Cursor router model

Source-native identity: configured `item.modelId`, default `composer-2`, passed to Cursor `Agent.prompt`. Representational form: distributed-parametric provider model; parameters reside outside repository storage. The caller changes prompts, not weights; provider-side parameter changes are uninspected. Exact model snapshot is not pinned by this caller. A mutable model ID/service can resolve to another implementation; endpoint resolution guarantees are external. SRC-1, `researcher/benchmarks/sdk-runner/src/common.ts`, `researcher/benchmarks/sdk-runner/src/runRouter.ts`.

> model: { id: item.modelId },
> --- `researcher/benchmarks/sdk-runner/src/runRouter.ts`

#### RT-CMP-minimax-model
Label: MiniMax optimization model

Source-native identity: `MiniMax-M2.1` by default at configurable `https://api.minimax.io/anthropic`, shared across capture, analyzer and optimizer construction. Representational form: distributed-parametric provider model, not repository-local weights. The inspected orchestration revises text, not model parameters; provider internals are uninspected. Exact weights/version are not pinned. The configurable endpoint/model alias can resolve differently over time. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`.

> self.capture = TraceCapture(api_key=api_key, base_url=base_url, model=model)
> self.analyzer = TraceAnalyzer(api_key=api_key, base_url=base_url, model=model)
> self.optimizer = PromptOptimizer(api_key=api_key, base_url=base_url, model=model)
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`

### Operative objects

#### RT-OBJ-skill-body
Label: Context fundamentals instruction body

Identity: `skills/context-fundamentals/SKILL.md` Markdown body. Form: natural-language guidance, stored in a Git-tracked file, consumed through host/model interpretation. Its frontmatter description is a separate selection input rather than proof that the body was activated. It advises finite attention budgets, task-specific routing and progressive disclosure. SRC-1, `skills/context-fundamentals/SKILL.md`.

> Keep the boundary crisp: if a skill or document is activated, load it fully rather than partially — partial loads create confusing gaps that degrade reasoning quality.
> --- `skills/context-fundamentals/SKILL.md`

### Routes

#### RT-RTE-skill-delivery
Label: Published skill delivery

Endpoints: repository skill directories/manifests to an external host and model. Owner: host chooses discovery/loading; model or human interprets the selected body. Metadata paths are symbolic; descriptions and body instructions are natural language. README installation and manual directory copies are alternate entry paths, not enforcement code. SRC-1, `README.md`, `.plugin/plugin.json`, `skills/context-fundamentals/SKILL.md`.

- Immediate return: uninspected — external host implementation and installation execution are not supplied.
- Later read-back: inapplicable — this traced route distributes static shipped instructions, not use-accumulated content.
- Delegated visibility: uninspected — host determines which agents receive selected bodies.
- Selection predicate: task relevance as judged by the host/agent against skill descriptions; the selected body's own activation guidance further narrows its intended use.
- Invalidation or expiry: uninspected — host cache/update behavior is external.
- Activation or effect: intended instruction delivery; compliance or changed behavior is not observed.
- Evidence limits: manifest and author guidance establish packaging and policy, not host loader correctness.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.
> --- `README.md`

#### RT-RTE-research-step
Label: Conservative research advancement

Endpoints: inbox/configuration and run-state files to initialized/retrieved/parked/done state and event logs. Owner: deterministic Python selects and advances; external human/judge owns evaluation. Symbolic JSON/JSONL state and CLI dispatch govern effects; source content and generated scaffolds remain prose/data. The scheduler runs a single action per invocation and reloads state later. SRC-1, `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`.

- Immediate return: JSON or human-readable event; exit 78 for no-op, otherwise the step main returns zero.
- Later read-back: later steps reload run-state and queues to select work and reap closed runs.
- Delegated visibility: parked records and run files expose pending work to external reviewers; no internal judge invocation in this inspected driver.
- Selection predicate: daily/active/parked/failure budgets, oldest discovered inbox record, then oldest active updated timestamp.
- Invalidation or expiry: closure moves runs to done; parked entries are removed on closure; no general source-content expiry is enforced here.
- Activation or effect: local file writes, fixed Python subprocess calls and opt-in HTTP GET; source evaluation is parked.
- Evidence limits: subprocess internals beyond inspected paths, scheduler deployment and actual queue contents are not execution evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: caller/config supplies mission and budgets; code chooses work; human or judge may later evaluate and veto under the runbook. Operating mode: open source queue under budgets, not an answer-key curriculum. Answer oracle: none supplied by the step driver. Trigger: repeated invocation. Proposed product changes and admission belong to the subsequent research protocol, not this housekeeping step. Recovery parks fetch/state failures, quarantines initialization failures and logs events.

> park_run(run_id, "needs source evaluation by human or judge agent")
> --- `researcher/scripts/loop_step.py`

#### RT-RTE-mechanism-promotion
Label: Mechanism registry admission

Endpoints: run-local `mechanism-proposal.jsonl` to mechanism registry and accepted/rejected ledgers. Owner: CLI caller supplies proposals and `reviewed_by`; code branches on status recommendation. Guidance: runbook requires rubric application, novelty and recorded human review before promotion. The admitted projection retains activation scenario, behavior change, evidence IDs and failure modes; the ledger retains rationale and reviewer. These JSON fields are symbolic record structure carrying prose; later semantic judgment is external. SRC-1, `researcher/scripts/research_loop.py`, `researcher/scripts/validate_run.py`, `researcher/runbooks/autonomous-research-loop.md`.

- Immediate return: zero after append operations and a validated/closed state update; exceptions reject invalid IDs, duplicates, unsupported status or default-path failed readiness.
- Later read-back: runbook directs subsequent researchers to read registry before claiming novelty; this is a prescribed later consumer, not observed use.
- Delegated visibility: registry/ledgers are repository files available to subsequent agents and reviewers.
- Selection predicate: caller's accepted/candidate/rejected recommendation; accepted/candidate require readiness unless allow-unready; duplicate IDs reject.
- Invalidation or expiry: no removal or rollback in this function; multi-record append failure can leave earlier writes intact.
- Activation or effect: registry and ledger append, not automatic publication of a skill or installation into a host.
- Evidence limits: reviewer identity is a string, not authenticated human approval; closed-state readiness checks less than active publish readiness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: human or agent may author the proposal; caller determines reviewer text and status; code can reject structurally, but human per-content control is unresolved. Mode: open research proposals. Answer oracle: none; readiness checks structure, source status and required reports rather than reference answers. Trigger/objective: admitting nonduplicate, evidence-supported mechanisms. Rejection is ledgered; recovery/rollback after partial append requires external intervention. Product editing and push/merge remain separate instructed human-approval operations.

Guarantee owner: promotion CLI. Enforcement point: nonempty reviewer check and readiness branch. Guarantee strength: protocol. Covered path: normal accepted/candidate promotion with active-run readiness and no override. Alternate paths: rejected ledger, explicit allow-unready, closed-state validator and direct file edits outside this CLI. Required external contract: truthful reviewer identity, meaningful evaluation content, compliant file writers and human merge control.

- guarantee implementation conclusion status: wired
- guarantee operation conclusion status: uninspected

> if not readiness_ok and not args.allow_unready:
>                 raise ValueError("run readiness must pass before promoting accepted or candidate mechanisms")
> --- `researcher/scripts/research_loop.py`

> if current_state == "closed":
>                 # Closed runs are terminal. validate_run only enforces publish
>                 # readiness for active runs; closed runs are validated by their
>                 # own closure.json plus repo-level checks.
>                 self.validate_closure()
> --- `researcher/scripts/validate_run.py`

#### RT-RTE-router-benchmark
Label: Description-only routing evaluation

Endpoints: corpus index, skill frontmatter, fixture and routing template to Cursor requests, result files, summary and history. Owner: TypeScript enumerates prompt/model/replications, seeds skill ordering and bounds concurrency; [RT-CMP-cursor-model](#rt-cmp-cursor-model) proposes a ranking; code scores it. Only names/descriptions, not skill bodies, are rendered by this caller. SRC-1, `researcher/benchmarks/sdk-runner/src/common.ts`, `researcher/benchmarks/sdk-runner/src/runRouter.ts`.

- Immediate return: console summary and files; dry-run returns a plan without SDK calls; unavailable key/dependency aborts execution.
- Later read-back: resume scans existing result files and skips matching prompt/model/rep filenames; history remains for later analysis, not automatic skill revision here.
- Delegated visibility: SDK receives rendered task/descriptions with repo cwd and settingSources empty; further provider context/tools are external.
- Selection predicate: corpus-index skill list and configured fixture/model/rep set; predicted top-1/top-3 compared with expected_primary_skill.
- Invalidation or expiry: no-resume disables reuse; default reuse validates basic identity fields, not matching current descriptions, fixture hash or success status.
- Activation or effect: paid model calls when enabled, result/summary/history writes; does not activate selected skill bodies.
- Evidence limits: estimated budget is not runtime billing enforcement; ranking parsing is not host activation; result production is not inspected observed execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode: bounded fixture evaluation. Answer oracle: fixture author's `expected_primary_skill`, used by exact string equality; secondary/rejected fields do not enter the shown scoring. Computational decision: ranking and equality score. Human contribution: fixture/reference design and any subsequent description changes outside this runner. Admission: none automatically; results can inform later proposals. Recovery: one retry for malformed ranking, per-item exception records, resume on later invocation. Cost control is a preflight protocol over estimates and attempt counts, with an explicit unsafe-no-cost-cap entry option; no claim of a hard dollar ceiling is warranted.

> local: { cwd: REPO_ROOT, settingSources: [] },
> --- `researcher/benchmarks/sdk-runner/src/runRouter.ts`

> record.top1_correct = parsed[0] === prompt.expected_primary_skill;
> --- `researcher/benchmarks/sdk-runner/src/runRouter.ts`

#### RT-RTE-prompt-optimization
Label: Trace-fed prompt and skill generation

Endpoints: task/current system prompt to capture trace, analyzer output, optimized prompt, artifacts and optionally generated skill directory. Owner: optimization loop invokes capture/analyzer/optimizer using [RT-CMP-minimax-model](#rt-cmp-minimax-model); code computes weighted scores and continuation, model proposes rewritten text. CLI optimize supplies no tools; library callers can provide definitions, arbitrary executor callbacks and per-iteration callbacks. Capture marks success when no tool calls remain; that is not an answer oracle. SRC-1, `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/optimizer.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/skill_generator.py`.

- Immediate return: LoopResult with final prompt/scores; optional CLI output file and generated SKILL.md.
- Later read-back: subsequent rounds consume the revised current_prompt; separate generate-skill CLI reloads summary.json and final_prompt.txt into a minimal result, not complete saved iterations.
- Delegated visibility: analyzer/optimizer receive formatted inputs in separate calls; capture invokes the supplied executor with tool name/input and returns tool results to its model.
- Selection predicate: max iterations, score threshold, convergence/regression rules, max prompt-growth ratio and use-best-prompt finalization.
- Invalidation or expiry: per-invocation artifact names can overwrite prior files; no automatic published-skill installation or versioned rollback is shown.
- Activation or effect: a continued round passes updated text as system_prompt; generation writes skill/reference files but later host activation is unobserved.
- Evidence limits: score bookkeeping can associate the just-scored trace with the subsequently generated prompt; final reported improvement is not an independent test of that final prompt.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: task caller starts optimization; model proposes, code admits unless growth guard retains current text, without per-round human approval. No authenticated human veto gate is shown inside this loop; caller controls stopping/configuration. Generated skill writes are direct, not research-loop readiness-gated. Recovery: capture catches errors and records trace failure, missing executors return mock results; regression rules can stop and select best_prompt, but are not a versioned transactional rollback. Mode: repeated evaluation on one supplied task. Answer oracle: none independently supplied; weighted score combines no-more-tools success, analyzer score and tool-error penalties.

Guidance and theory account: optimizer request uses original prompt, task, analysis patterns, weaknesses, recommendations and a truncated analyzer-thinking excerpt to ask for a replacement. Full content-directed criticism/blame and resulting changed reliance are not established by the inspected request builder alone. What persists is prompt text, formatted trace/analysis/optimization artifacts and summary fields; generated skills expose separate activation/concept/guideline prose. Addressability: prompt and generated Markdown sections are editable, not hidden weight updates. Persistence horizon: next round within one run is wired; separate artifact reload is wired; later installed-host behavior is unobserved.

Theory-builder conditions 1–4: condition 1 conclusion status: uninspected — no particular model-produced theory unit was inspected; condition 2 conclusion status: afforded — revised instruction content is supplied as next-round system text, but dependence on a formulated theory's assertions is unobserved; condition 3 conclusion status: uninspected — request/score wiring alone does not establish claim-specific criticism and blame; condition 4 conclusion status: uninspected — iteration is wired, but iteration of qualifying criticism is not established. Learning: uninspected — no demonstrated capacity gain or final-prompt causal comparison. Reflection: afforded — trace/analysis represent aspects of the prompt-controlled agent and feed its later prompt, but representation fidelity and operation are unobserved. Reflective theory builder: uninspected — qualifying method criticism was not inspected. Autonomous theory builder: uninspected — computational orchestration does not establish all theory-building operations. These are separate conclusions, not bundled negatives.

> current_prompt = new_prompt
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`

> if executor:
>                 result = executor(tool_block.name, tool_block.input)
>             else:
>                 result = f"[Mock result for {tool_block.name}]"
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`

> if not tool_use_blocks:
>                     trace.final_response = (
>                         text_blocks[0].text if text_blocks else None
>                     )
>                     trace.success = True
>                     break
> --- `examples/interleaved-thinking/reasoning_trace_optimizer/capture.py`

#### RT-RTE-idea-draft
Label: Retained idea to draft scaffold

Endpoints: content ideas/posts and knowledge bookmarks JSONL to stdout Markdown. Owner: deterministic Python; caller supplies idea ID/partial match. JSON keys determine selection, while retained idea/insight strings are natural-language content inserted into a scaffold. SRC-1, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`.

- Immediate return: printed scaffold or not-found error string, without a model call or draft write.
- Later read-back: ideas, bookmarks and past posts are reloaded each invocation; this consumer does not implement their write/admission mechanisms.
- Delegated visibility: stdout is available to caller; subsequent agent delivery is not traced.
- Selection predicate: first exact/substring ID or idea match; tag intersection or category/pillar for first five bookmarks; same pillar for first three posts.
- Invalidation or expiry: no freshness predicate; missing files return empty lists, malformed JSON and schema lines are skipped.
- Activation or effect: inserted content affects scaffold construction; no observed effect on a later authored post.
- Evidence limits: retained-data producer, review and downstream publishing remain untraced here; file presence does not prove learning.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return related[:5]
> --- `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`

### Claims

#### RT-CLM-maintenance-guarantees
Label: README maintenance guarantees

Claimed operation: no paid-model calls/outbound writes in the loop, recorded human reviewer plus readiness for promotion, universal queue atomicity, and human merge/push control. SRC-1, `README.md`. The inspected controls support narrower claims: conservative step-driver behavior, default promotion protocol with supported exceptions, named queue locks on some paths, and instructed human approval. They do not establish a repository-wide isolation envelope or universal queue atomicity.

> Mechanism promotion requires a recorded human reviewer and a passing run-readiness check.
> --- `README.md`

> All queue mutations are atomic (temp file + `os.replace`) and serialized via `fcntl` locks.
> --- `README.md`

Counter-witness for the broad queue claim: the run-local retrieval update in SRC-1, `researcher/scripts/loop_step.py`, directly writes the queue without a lock/temp replacement in that function:

> queue.write_text("\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n", encoding="utf-8")
> --- `researcher/scripts/loop_step.py`

### Evidenced absences

#### RT-ABS-effectiveness-executor
Label: Effectiveness runner execution stage

- implementation conclusion status: absent

Bounded absence: SRC-1 at the frozen revision, complete inspection of `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts`, following dry-run and non-dry-run branches and searching its Stage 3 executor/call path. The file discovers task metadata, constructs condition plans and forecasts costs; non-dry-run prints a not-wired message, creates a results directory and returns zero. No effectiveness execution is implemented in that runner. This does not establish absence of evaluations elsewhere and prevents treating its successful exit or plan as body-effectiveness evidence.

> "Stage 3 executor not yet wired in v2.2.x scaffold. See researcher/benchmarks/PLAN.md for the v2.4.0 implementation contract. " +
> --- `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts`

### Behavioral-authority paths

#### RT-BAP-skill-instruction
Label: Skill body instruction authority

Consumer: external host's model/agent. Channel: activated Markdown skill body, including [RT-OBJ-skill-body](#rt-obj-skill-body). Force: natural-language behavioral guidance, not a symbolic permission gate. Horizon: the invocation/session in which the host supplies the body; repeat loading and cache horizons are external. SRC-1, `README.md`, `skills/context-fundamentals/SKILL.md`. Delivery is prescribed by [RT-RTE-skill-delivery](#rt-rte-skill-delivery); reliable compliance and later operation are unobserved.

> Treat context as a finite attention budget, not a storage bin.
> --- `skills/context-fundamentals/SKILL.md`

## Annotations

none
