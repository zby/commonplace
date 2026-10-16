---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "WikiSkill runtime baseline: host-driven work requests, native handoffs, feedback admission and two research execution paths."
run-id: AAS-2026-10-15-wikiskill-baafad05d35e-01
reviewed-boundary: da6984caca09d5f81b2336cf3067b59c0c18bb1e
---

# WikiSkill runtime report

## Runtime account

WikiSkill ships a controller for improving reusable instructions, not a replacement for the user's agent. Its ordinary product path records work, delegates execution to a host, admits Wiki patterns, proposes a skill, and compares the candidate with an incumbent. The controller owns phase transitions and retained versions; the host owns model inference, normal tools, permissions and actual subagent creation. This distinction does not extend to all shipped paths: the research engine and isolated Spreadsheet study launch Codex themselves (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/engine.py`, `src/wikiskill/isolated/runtime.py`).

This is source inspection at the boundary's frozen revision, not a target run. No provider, test, example or preflight was executed. All route implementation statuses below concern wiring; exercised operation, reliable model compliance and benefit are uninspected. Added implementation coverage beyond the boundary's initial inspection includes full product, native handoff, feedback and installation modules; scorer trust; research engine; selected role-factory and legacy executor bodies; isolated study invocation, payload, learning and gate bodies; isolated runtime policy and execution; tool specifications; numeric acceptance rules and CLI routing. These are all SRC-1, not additional sources. Uninspected domain adapters and bundled evaluation artifacts cannot establish measured improvement here.

### Ordinary invocation and responsibility handoffs

The installed `wikiskill` CLI routes product commands through `product_cli`; MCP wraps the same product functions. `start` fixes train/validation tasks, hashes declared input files, optionally copies an initial skill or inherits a previous workspace's skill, patterns and feedback, and writes configuration and its digest. Product state is reconstructed from configuration plus event files; hash checks protect referenced artifacts and the current skill ([RT-OBJ-product-journal](#rt-obj-product-journal)). Workspace locks serialize cooperating writers, rather than separating agent permissions (SRC-1, `src/wikiskill/cli.py`, `src/wikiskill/mcp_server.py`, `src/wikiskill/product.py`).

A host principal repeatedly asks `next` or native `dispatch` for work. Baseline tasks use validation cases and the initial skill; train tasks use the retained skill. A request has its own ID, phase, round, task ID and skill pointer. The controller strips the top-level reference/expected/gold/score fields from task payloads. In native mode it stages a role instruction and minimal payload, asks the host to create a fresh child, then requires the coordinator to bind the returned host ID. The host waits and returns a result-file pointer; `collect` copies actual output into journal-owned artifacts and invokes scoring or accepts a supplied finite score. A request result carries runtime/model provenance fields, but these fields do not attest model identity or isolation ([RT-RTE-product-round](#rt-rte-product-round), [RT-RTE-native-handoff](#rt-rte-native-handoff)).

After train completion, the controller issues one Maintainer request containing current-round training outcomes, existing Wiki patterns, user feedback, retained skill and gate history. It admits sourced patterns, then issues the Proposer a new context reflecting the committed Wiki. The Proposer returns a complete skill or `no_action`. Candidate validation uses the same validation task list; only a score improvement strictly greater than the configured minimum changes the retained skill pointer. Rejection keeps the incumbent, not the pre-learning Wiki. The controller advances rounds and eventually returns complete status with retained skill, Wiki and history; export or installation makes a further downstream consumption path ([RT-RTE-product-round](#rt-rte-product-round), [RT-RTE-skill-install](#rt-rte-skill-install)).

### Alternate and forcing routes

Four forcing cases bound the ordinary account:

1. **Native isolation versus direct submission.** Freshness is a host protocol plus declared metadata, not a filesystem sandbox. `bind` checks a nonempty ID, runtime, `fresh` label and ID nonreuse, but explicitly records that the evidence is host-reported. Direct product and MCP workflows without configured native runtime do not require a binding. Even a bound request can be submitted through product APIs without `collect`'s output-directory containment check. Thus the stronger native collection invariant does not cover all submission paths ([RT-RTE-native-handoff](#rt-rte-native-handoff)).
2. **Trusted checker versus arbitrary host effects.** An external scorer needs a local fingerprint receipt; task hashes and scorer fingerprint consistency are rechecked. Nevertheless it runs as a subprocess with ordinary host permissions, not inside an evaluation sandbox. Direct dependencies, imported code and a host agent with terminal access are outside the MCP tool-list separation. With no configured scorer, a caller supplies the score. Numeric admission is deterministic but does not establish truthful or valid evaluation ([RT-RTE-product-round](#rt-rte-product-round)).
3. **Feedback policy versus numeric improvement.** The feedback-first API reuses learning requests but replaces numeric admission with supplied paired verdicts. Explicit human requirements change the rule: ties can be admitted when every requirement check is fulfilled, there are no regressions and no worse case. General feedback instead requires more better than worse cases and no regressions. Evidence text and optional comparison artifacts are retained, not independently verified. This prevents a system-wide claim that admission always means strict numeric improvement ([RT-RTE-feedback-gate](#rt-rte-feedback-gate)).
4. **Host-neutral product versus research execution.** `evolve` calls domain rollouts and optimizer factories, while the isolated single-round Spreadsheet study uses a separate native runtime and tool boundary. The legacy Codex helper requests `workspace-write` and inherits host environment except `CODEX_HOME`; the isolated study explicitly disables tools/features and supplies a dedicated policy. Neither isolation policy can be attributed to the ordinary product path ([RT-RTE-research-evolve](#rt-rte-research-evolve), [RT-RTE-isolated-study](#rt-rte-isolated-study)).

### Guarantees and their limits

| Guarantee | Owner and enforcement | Strength, coverage and external contract | Conclusion statuses |
|---|---|---|---|
| Recorded task/configuration/artifact consistency | Product `_load`, `_check_task_files`, immutable-write helper, lock | Invariant for cooperating product API calls against unchanged local records. Hash-linked replay detects changes relative to local metadata; it is not authenticated storage against a writer who can rewrite both data and hashes. No isolation from normal host tools is established. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Fresh role context | Native dispatcher, binder and host | Protocol: configured native requests require delegation metadata before successful task/learning/proposal submission. Host must really create a fresh child. Direct unconfigured product/MCP use and research runners have different controls. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Candidate admission | Product `_advance`, feedback `finish`, research `evolve`, study `run` | Invariant only for each respective selection predicate and supplied evaluator results. No invariant of better real-world behavior. Candidate rejection leaves learning artifacts available. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Scorer authorization | Local trust store, `require`, comparison check | Policy implemented by product APIs; binds workspace, command, executable/direct files, project and timeout. Requires operator-owned trust storage and honest authorization. MCP omits approval tools; arbitrary shell/Python access can still reach them. Imported dependencies are not all fingerprinted. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Isolated research reads/tools | Isolated runtime configuration, tool server, OS policy and audit | Deployment guarantee sought only for the pinned macOS study. Requires compatible Codex, `sandbox-exec`, provider behavior and audit correctness; no executed deployment is established here. Not a product-wide guarantee. | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface is broader than any single role's grant: the host can have shell, files, native subagents and arbitrary normal tools; a scorer is executable code; the research controller accepts custom loader/role callbacks. The current native product grant is a role request plus inherited host permissions, not an independent tool allowlist. The isolated study instead gives Spreadsheet a bash tool and learning roles staged reads plus structured finish. The actual deployed isolation envelope and provider internals remain unobserved (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/scorer_trust.py`, `src/wikiskill/engine.py`, `src/wikiskill/isolated/tools_server.py`, `src/wikiskill/isolated/runtime.py`).

## Shared records

### Components

#### RT-CMP-host-model
Label: Caller-selected host model

The product consumes externally generated task outputs and role submissions; the distributed-parametric component is the host's selected model, with parameters on external provider infrastructure. WikiSkill does not modify those parameters. Exact model versions are not pinned by product code: requests say `caller_selected`, and provenance fields are caller-supplied. Whether a mutable endpoint resolves to a different model is controlled externally and uninspected. Host context, tools and inference are outside the controller's execution boundary (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/native_agents.py`).

> No model is invoked and no sandbox or account configuration is changed here.
> --- `src/wikiskill/product.py`

#### RT-CMP-research-model
Label: Research inference and optimizer models

Research inference and optimizer calls use configured model/effort strings; both consume distributed-parametric model services through Codex. Weights are not stored locally and no inspected route updates them. Legacy inference and optimizer names may differ; the isolated runner accepts only `gpt-5.6-luna`/`high`. These names and catalog checks pin a requested identity, not an inspectable weight digest. Mutable endpoint resolution and provider-side parameter changes remain uninspected (SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/officeqa/rollout.py`, `src/wikiskill/isolated/runtime.py`).

> if (model, effort) != ('gpt-5.6-luna', 'high'):
> --- `src/wikiskill/isolated/runtime.py`

### Operative objects

#### RT-OBJ-product-journal
Label: Product event journal

Symbolic JSON event records on the local filesystem carry sequence, previous-event hash, type, value and referenced artifact hashes. Fixed Python replay rules determine phase, requests, results, patterns, current skill and gate history. This is controller state and integrity metadata; the natural-language skill and pattern contents have distinct downstream interpretation and are not claimed here as symbolic theories (SRC-1, `src/wikiskill/product.py`).

> if e['sequence'] != i or e['previous'] != s['last_hash']: raise ValueError('Event history is incomplete or changed')
> --- `src/wikiskill/product.py`

Replay rechecks recorded artifacts and retained skill. Local writers can still alter both journal and hash metadata; the quote establishes a consistency check, not adversarial tamper-proof storage. Retries supersede failed requests; completed submissions are idempotent only when the repeated supplied content agrees with the sealed result.

### Routes

#### RT-RTE-product-round
Label: Numeric product learning round

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Status and pending request descriptors; record/learn/propose return updated status rather than model answers.
- Later read-back: Accepted skill enters later task requests; existing patterns and human feedback enter later learning contexts and may be inherited by a new workspace.
- Delegated visibility: Task requests omit named reference fields; learning context includes current-round training records, Wiki, human feedback and gate history. Native payload restrictions are separately assessed below.
- Selection predicate: Baseline and candidate use validation split; learning uses train split. Acceptance requires direction-adjusted improvement strictly above min_improvement; no_action does not pass the numeric gate.
- Invalidation or expiry: Fixed rounds; changed configuration/task inputs/scorer comparison fail checks. Rejection retains incumbent; sourced Wiki updates already committed are not rolled back by the skill gate.
- Activation or effect: Controller changes current_skill only on acceptance and delivers its artifact pointer to subsequent requests. Whether agents read it or change behavior is uninspected.
- Evidence limits: Numeric validity is checked, but scores and source citations do not attest evaluator correctness, source entailment or model compliance.

Owner/progression: host calls start/next, performs tasks, and supplies actual output files. Product records scores, moves baseline → train → maintainer → proposer → validation, and chooses the retained successor. Maintainer/proposer are computational authors when run as instructed; APIs do not authenticate authorship. A caller can submit files directly. Human contributions are task choice, feedback, optional skill, score input or scorer approval; the loop does not require human approval of each pattern or candidate. Operating mode is a bounded train/validation comparison, with later rounds reusing validation cases rather than an independent held-out test. The answer oracle is caller scores or the configured external command, which receives the full task including reference fields plus the retained output path/text; an oracle's quality is external (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/score_rules.py`).

> return improvement(candidate, incumbent, direction) > threshold
> --- `src/wikiskill/score_rules.py`

> if not isinstance(sources,list) or not sources or any(x not in allowed for x in sources):raise ValueError('Cite permitted training request or human-feedback IDs')
> --- `src/wikiskill/product.py`

The second check admits knowledge by identifier membership, not a semantic proof. Patterns are name/content/source JSON; proposed skills need only nonempty UTF-8 text at this admission point. Guidance asks for reusable procedures, explicit human requirements, successful/failed cases and no one-off answers. It persists as Wiki and skill text, not parameter updates. Failures stop progression and require explicit retry; scorer failures preserve output and can reuse execution rather than turn infrastructure errors into wrong-answer scores.

Theory account: the shipped Proposer asks for applicability, exclusions, concrete actions and supporting counterexamples. A returned procedural rule can express a localized theory, but no submitted candidate was inspected in this report. Theory-builder conditions 1–4: (1) implementation conclusion status: afforded — whole-text skills can state a theory, content uninspected; (2) operation conclusion status: uninspected — delivery and a read instruction do not establish content-dependent decisions; (3) implementation conclusion status: afforded — counterexample guidance and training evidence support criticism, not proof of claim/result/blame formulation; (4) implementation conclusion status: wired — retained Wiki, skill and gate history reach later rounds, while iteration of formulated criticism remains uninspected. Addressability is whole-file skill replacement and named patterns; finer assumptions are not enforced. Persistence reaches rounds and explicitly inherited workspaces. Under learning, improved future capacity and attribution are uninspected. Under reflection, feedback about task execution can shape later skill instructions; represented execution is selected outcomes/traces, not verified self-criticism. Reflective and autonomous theory-builder conclusions remain uninspected: neither all four content conditions nor role-by-role realized computation is established by these APIs (SRC-1, `src/wikiskill/resources/product/roles/proposer.md`, `src/wikiskill/product.py`).

> Identify a useful procedural change with supporting evidence, including counterexamples and prior rejected ideas.
> --- `src/wikiskill/resources/product/roles/proposer.md`

#### RT-RTE-native-handoff
Label: Native host role handoff

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dispatch returns prompt/payload/output/result paths; bind returns host-reported agent identity; collect returns product status.
- Later read-back: Role output is admitted through the product route; saved failed-scoring output can be reused by a retry without a new child.
- Delegated visibility: Executor gets task and skill, not the learning Wiki or baseline answers in its payload. Learning roles get a staged learning-context file; native aggregate history omits candidate text and validation outputs.
- Selection predicate: Runtime must match configured comparison, context_mode must equal fresh, and a normal new binding must use a previously unused host ID. Role follows request kind.
- Invalidation or expiry: Fail requires pending request; retry supersedes failed request. Completed collect never reapplies a changed scratch result; runtime or binding conflicts are rejected.
- Activation or effect: Creates request-specific files and delegation events, then collect dispatches output to record/learn/propose. Actual fresh-context creation and adherence are external host actions.
- Evidence limits: IDs and freshness are declared, not independently attested. Normal host tools can reach files beyond payload; output-directory confinement belongs to collect, not all direct APIs.

Owner is split: WikiSkill stages work, host creates/waits on subagent, coordinator binds and collects, product makes admission decisions. Context isolation is a requested per-task frame: coordinator conversation is kept out, task/skill or learning context is pushed, and only result pointer/status should escape. Durable files remain reachable to a sufficiently privileged host; the frame is not memory protection. Retry reuse is a deliberate exception to one-new-agent-per-request. Capability/permission boundaries still come from the host, as the executor role itself states (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/resources/product/roles/executor.md`).

> 'context_mode': context_mode, 'evidence': 'host-reported; not independent attestation'}
> --- `src/wikiskill/native_agents.py`

> A fresh task context is required. Host policies, tools, project instructions and permissions still apply; this role does not establish filesystem isolation.
> --- `src/wikiskill/resources/product/roles/executor.md`

#### RT-RTE-feedback-gate
Label: Feedback-first paired admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: begin/work/finish expose phase, candidate, retained skill, patterns, feedback and history.
- Later read-back: Feedback and Wiki feed Maintainer/Proposer requests; rejected requirement-driven gates return to maintenance with revision guidance until the round bound.
- Delegated visibility: Reuses native learning handoffs; paired results are supplied by host rather than generated by this API.
- Selection predicate: Ordinary feedback requires better>worse and no regressions; explicit requirements require complete fulfilled source checks, zero worse cases and no regressions. no_action cannot satisfy outstanding explicit requirements.
- Invalidation or expiry: Initialization intent is fixed; accepted/no-action-without-pending-requirements or exhausted rounds end the study. Rejection keeps current skill, while patterns remain.
- Activation or effect: finish appends feedback_gate; accepted skill becomes current_skill. Actual later consumption is uninspected.
- Evidence limits: Pair verdicts, evidence strings, human-origin declarations and requirement fulfillment are caller reports, not independently checked experiments.

Trigger is user feedback or explicit human requirement; proposed changes come from Maintainer and Proposer under the same procedural guidance as the numeric route. Software owns final selection, caller supplies pairs and may decline to proceed; there is no separate per-candidate human-approval requirement. Optional evidence_file is copied for provenance. Answer oracle is the external paired comparison and requirement check, not a model judgment necessarily. Mode is a bounded feedback comparison rather than the numeric task curriculum. On requirements_pending the next guidance says revise regressions without dropping requirements, and gate history persists (SRC-1, `src/wikiskill/feedback_loop.py`, `src/wikiskill/product.py`).

> accepted=not no_action and fulfilled and not any(x['regressions'] for x in pairs) and (worse==0 if explicit else better>worse)
> --- `src/wikiskill/feedback_loop.py`

Theory properties share the product route's representational affordances but not its numeric oracle: conditions 1 and 3 are afforded by localized text and feedback-guided revision; condition 2 is uninspected at model behavior; condition 4 is wired for carrying history to a later round, with formulated criticism uninspected. Persistence is bounded rounds plus inherited workspaces. Whole-skill/named-pattern addressability does not verify claim-level criticism. Learning benefit, reflective theory building and realized autonomous theory building are uninspected, independently of the wired admission mechanism.

#### RT-RTE-research-evolve
Label: Legacy research evolution

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: evolve returns reconstructed experiment state and writes progress, attempts, outcomes, proposals and gate events.
- Later read-back: Accepted skill enters next train rollout; Wiki and accepted/rejected impact records enter subsequent optimizer contexts; resume reuses valid task rows and committed proposals.
- Delegated visibility: Default role factory loads train outcomes, guards train-only data, samples maintainer cases and stages traces. Legacy optimizer is an external Codex subprocess, not a native product handoff.
- Selection predicate: Disjoint train/val IDs; binary valid rollout rows; candidate mean validation accuracy must strictly beat best. Stop at validation ceiling or iteration limit.
- Invalidation or expiry: Manifest and prompt hashes, batch bindings and incumbent hash reject changed conditions. Infrastructure failures preserve attempts, drain pending work and require resume. Rejection preserves incumbent; Wiki learning is not automatically reverted.
- Activation or effect: Accepted skill is written and journaled; next rollout receives skill_text. Default Maintainer updates Wiki before candidate selection.
- Evidence limits: Custom callbacks may supply different data/roles/scorers; callback-source binding is a caller contract. External Codex workspace-write is not the isolated study's OS envelope. No run outcome was inspected.

Owner is engine.evolve; adapters own task-specific execution/scoring, optimizer factories author Wiki/skill changes, engine owns successor admission. Baseline uses an empty skill on validation; train uses incumbent; default optimizer model can differ from inference model. With no proposal cache, Maintainer runs once behind a completion marker and Wiki-before backup, then Proposer returns validated structured output; proposal.json is reused on resume. The engine records diffs, purpose, motivating patterns and gate impact. Those are evidence/history, not a proof of explanatory criticism or generalization (SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/officeqa/rollout.py`).

> Adapters supply data, scored rollouts and validated role results; this engine
> still owns iteration, validation selection, rollback and experiment records.
> --- `src/wikiskill/engine.py`

> env = dict(os.environ)
> env.pop("CODEX_HOME", None)
> --- `src/wikiskill/officeqa/rollout.py`

Mode is bounded benchmark evolution. Answer oracles come from domain scorers; exact scoring on all domains is uninspected here. Supplied callback results are trusted at the engine boundary after UID/binary-score/infrastructure checks. Human involvement is configuration and adapter provision, not obligatory content approval. A synthetic demo branch bypasses models and deterministically supplies candidate text; it cannot establish model improvement. Theory-builder conditions: 1 afforded by whole skill text, 2 wired for prompt supply but content-dependent behavior uninspected, 3 afforded by trace/impact exposure but formulated criticism uninspected, 4 wired for retained Wiki/skill/impact iteration. Addressability includes pattern edits and full skill replacement; horizon is experiment rounds. Learning benefit, realized reflection and autonomous theory building remain uninspected. Guidance and retained products concern procedures, traces, purpose, patterns and impact records, not weight optimization.

#### RT-RTE-isolated-study
Label: Isolated single-round Spreadsheet study

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Prepared protocol is consumed by run; run writes a gate, final skill JSON/Markdown, freeze manifest and complete/needs_attention state.
- Later read-back: Maintainer's Wiki updates reach Proposer within this study; accepted skills persist in FINAL-SKILLS.json and FINAL-SKILL.md. No second round or test invocation is scheduled by run.
- Delegated visibility: Fresh task payload has input workbook/task/skill, not reference workbook or Wiki. Learning payloads have staged TRAIN references and traces; Maintainer gets sampled cases, Proposer all train rows.
- Selection predicate: One baseline validation arm, one baseline training arm, one proposal, optional candidate validation; accept only candidate_correct>baseline_correct. Tool modes and split checks restrict route entry.
- Invalidation or expiry: Native request identity and sealed artifacts are checked on reuse; unsealed native attempts refuse automatic retry. Protocol/input checks and final freeze prevent silently changed comparisons. Rejection retains empty active skills while preserving Wiki/proposal evidence.
- Activation or effect: Candidate skill is inserted into validation system text; accepted candidate becomes final retained output. There is no inspected subsequent deployment by this driver.
- Evidence limits: Requested/catalog model identity is not weight pinning. Source policy/probe/audit code does not prove a deployed sandbox or actual improvement; reference scorer and contract details beyond inspected callers remain limits.

The study controller owns dispatch and scoring; isolated runtime owns the Codex invocation and tools. Spreadsheet mode exposes bash; learning roles expose staged file reads and structured submission, not general shell. Runtime uses separate workspace/control paths, disables project docs, memories, agents and web search, configures filesystem/network restrictions, verifies a boundary before calling, preserves native events/session/final output, and audits completed archives. The outer policy is used for tool execution; it should not be confused with removing the inference service's necessary communication. Native timeouts terminate the process group and preserve partial output (SRC-1, `src/wikiskill/spreadsheet/study.py`, `src/wikiskill/isolated/runtime.py`, `src/wikiskill/isolated/tools_server.py`).

> raise IntegrityError('Unsealed native attempt preserved; no automatic model retry')
> --- `src/wikiskill/isolated/runtime.py`

> accepted = candidate_correct is not None and candidate_correct > baseline_correct
> --- `src/wikiskill/spreadsheet/study.py`

This is bounded single-round research, not an open self-modifying host. Human supplies study inputs/configuration; model proposes structured Wiki/skill edits, software validates and gates them. Scoring oracle is the separately held reference workbook and target region. Proposer trace-read IDs are checked against actual successful read_file events; this checks reads, not comprehension. Model guidance prohibits task IDs/reference answers in skills, asks for justified procedures or no_action, and is not itself proof of compliance. Theory-builder conditions 1 afforded by structured skill text; 2 wired for skill injection with actual content-dependent decisions uninspected; 3 afforded by train references/traces but actual claim/blame/revision uninspected; 4 wired for Maintainer-to-Proposer retained Wiki, not an additional criticized skill generation. Pattern-edit/skill contracts offer localized revision; detailed contract correctness is uninspected. Persistence ends at a frozen one-round artifact for this driver. Learning benefit, reflective theory building and realized autonomy remain uninspected separately.

#### RT-RTE-skill-install
Label: Retained skill installation and restoration

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Export returns skill path/hash/score; install returns changed flag and backup/restore details; restore returns restored state.
- Later read-back: Host skill discovery may read installed SKILL.md in future sessions; no host reload or actual behavioral use is established here.
- Delegated visibility: inapplicable — local file installation, not agent delegation.
- Selection predicate: Export selects current_skill. Install requires complete phase and retained skill; replacing different existing SKILL.md requires replace=True. Other supporting files are untouched.
- Invalidation or expiry: Restore verifies destination, backup hashes and current installed hash, refusing to overwrite later edits. Backup remains local; export destination must be empty and outside workspace.
- Activation or effect: Copies retained text to destination or atomically replaces SKILL.md with a backup receipt. Filesystem effect is wired; host discovery and interpretation are external.
- Evidence limits: Installing a skill is not evidence it was loaded, obeyed or beneficial. Installation API checks an explicit flag, not human identity; a shell-enabled agent can call CLI/API.

Trigger/principal is an explicit caller export/install/restore request. Proposal is the already retained current skill; software enforces replacement conditions, caller can veto by withholding replace, rollback restores checked previous bytes or removes a newly installed file. Guidance is the selected skill body; provenance stores journal/config hashes and previous/installed content hashes, not a new model-generated theory. No answer oracle or candidate comparison is performed on this route. Mode is deployment/rollback after learning (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/product_install.py`).

> if state['phase'] != 'complete':
>     raise ValueError('Finish the current loop before installing its retained skill')
> --- `src/wikiskill/product_install.py`

### Claims

#### RT-CLM-mcp-separation
Label: MCP separation of privileged local operations

The module claims its connected agent cannot approve its own scorer or overwrite local skills because those functions are CLI-only. The MCP surface separation is meaningful only for a client restricted to those tools. It is not a system-wide permission boundary: product CLI/API expose approval/install, and normal host tools may invoke them (SRC-1, `src/wikiskill/mcp_server.py`, `src/wikiskill/product.py`, `src/wikiskill/product_install.py`).

> authorization, skill installation and restoration stay CLI-only so a connected
> agent cannot approve its own scorer command or overwrite local skills.
> --- `src/wikiskill/mcp_server.py`

The external scorer's own scope declaration narrows any stronger reading:

> 'scope':'Runs with normal host permissions; direct files are fingerprinted, not every imported dependency.'}
> --- `src/wikiskill/scorer_trust.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-consumption
Label: Retained skill to task executor

Consumer is a later task executor; channel is a skill file pointer in native/product payload or skill text passed into a research rollout/system prompt. Force is natural-language instruction interpreted under host policy, not a new permission grant. Horizon is subsequent rounds, inherited workspaces, and potential sessions after installation. Candidate validation also supplies proposed instructions before retention. Delivery is implemented; actual content-dependent behavior and benefit are uninspected (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/native_agents.py`, `src/wikiskill/engine.py`, `src/wikiskill/spreadsheet/study.py`).

> payload.update(task=request['task'], skill=_absolute_record(root, request['skill']))
> --- `src/wikiskill/native_agents.py`

#### RT-BAP-role-guidance
Label: Packaged role guidance to host child

Consumer is a host-created executor, Maintainer or Proposer. Channel is staged role.md plus payload/context paths. Force is host-interpreted instructions to limit inputs, avoid one-off answers, produce structured files and return only completion pointers. Horizon is one role invocation; packaged host assets can make these roles discoverable in later sessions without changing model defaults or global permissions. Controller checks output structure/provenance separately; it does not enforce every natural-language prohibition (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/resources/product/roles/executor.md`, `src/wikiskill/resources/product/roles/proposer.md`).

> 'note': 'Files installed only; no permissions, model defaults or global configuration changed.'}
> --- `src/wikiskill/native_agents.py`

## Annotations

none
