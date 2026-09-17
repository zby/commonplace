---
type: kb/types/agentic-system-analysis-result.md
description: "Complete code-grounded analysis of WikiSkill (Stahl-G), separating host-driven skill evolution, research execution, and bounded score admission."
run-id: AAS-2026-09-17-wikiskill-stahl-g-01
system: "WikiSkill (Stahl-G)"
run-date: "2026-09-17"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "9df975b2145a0e924f344f2a3d116e11d3f025ac"
analysis-cutoff: "2026-09-17"
evidence-tier: code-grounded
memory-comparison: {"scope": "Product Wiki patterns, human feedback, carried/candidate skills, training outcome/trace artifacts and gate history; research Wiki/index/logs, impacts, skills, raw and compacted trajectories; retained installation backups and their withdrawal route. Static prompts are mechanism evidence, not accumulated memory. Host runtime internals and external datasets/services are excluded. Includes isolated Spreadsheet study Wiki snapshots, candidate/final skill and purpose mappings, compacted traces and TRAIN reference feedback; its single round has no deployed next-round consumer.", "axes": {"storage_substrate": {"assessment": "known", "basis": "wired", "values": ["files"], "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "OBJ-5", "OBJ-6", "OBJ-7", "OBJ-9", "OBJ-10", "RTE-7", "OBJ-11"], "note": "Durable Markdown, JSON/JSONL, copied artifacts and restore backups; reconstructed in-process dictionaries are not another persistent store."}, "representational_form": {"assessment": "not-determinable", "basis": null, "values": [], "records": ["OBJ-4", "OBJ-7", "OBJ-9"], "note": "Known operative prose and symbolic records coexist, but product output and optional trace files are arbitrary bytes read by learning roles; container metadata cannot establish every payload form."}, "lineage": {"assessment": "known", "basis": "wired", "values": ["authored", "imported", "other-compiled", "trace-extracted"], "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-5", "OBJ-7", "RTE-4", "RTE-9", "RTE-7"], "note": "Human notes/initial skill, inherited knowledge, generated indexes/gate projections, and trace-derived patterns/skills."}, "behavioral_authority": {"assessment": "known", "basis": "wired", "values": ["instruction", "knowledge", "routing", "validation", "enforcement"], "records": ["OBJ-1", "OBJ-3", "OBJ-4", "OBJ-5", "OBJ-7", "OBJ-9", "OBJ-10", "RTE-7"], "note": "Skills instruct; Wiki and impacts advise; indexes route reads; retained scores drive admission; artifact/receipt hashes enforce unchanged inputs. No parametric learning authority established."}, "write_agency": {"assessment": "known", "basis": "afforded", "values": ["automatic", "manual"], "records": ["RTE-2", "RTE-3", "RTE-4", "RTE-5", "RTE-7"], "note": "Human feedback/import coexists with model-authored extraction and controller-maintained artifacts; host coordinator must execute the handoff."}, "curation_operations": {"assessment": "known", "basis": "afforded", "values": ["consolidate", "evolve", "invalidate", "promote", "synthesize"], "records": ["RTE-2", "RTE-3", "RTE-5", "RTE-11", "RTE-7"], "note": "Role instructions afford consolidation and generalization; replacements evolve entries, admission promotes skill, restore withdraws installed reliance while retaining receipt/history. No semantic deduplication or time decay mechanism identified."}, "read_back_direction": {"assessment": "known", "basis": "afforded", "values": ["pull", "push"], "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-9", "RTE-10", "RTE-7"], "note": "Research prompts automatically supply remembered content; maintainers/proposers are explicitly afforded requested reads of staged full traces/pattern pages; native roles read named payload files. Isolated proposer pulls through read_file; successful distinct trace reads are enforced before a change."}, "read_back_signal": {"assessment": "known", "basis": "wired", "values": ["coarse", "identifier"], "records": ["RTE-1", "RTE-2", "RTE-9", "RTE-10", "RTE-7"], "note": "Full Wiki/current skill and impact history are coarse push; current round/phase/request identity selects product training rows. Research score-stratified sampling is coarse, not semantic retrieval."}, "trace_learning": {"assessment": "known", "basis": "wired", "values": ["yes"], "records": ["RTE-2", "RTE-3", "RTE-5", "RTE-9", "RTE-7"], "note": "Research directly wires training traces to retained patterns and skill candidates, then later rounds consume them; native product extraction is an explicit host-agent afforded workflow."}, "trace_source": {"assessment": "known", "basis": "wired", "values": ["event-streams", "session-logs", "tool-traces", "trajectories"], "records": ["OBJ-4", "OBJ-7", "RTE-9", "RTE-7"], "note": "Research consumes rollout outcome trajectories, stdout session tails and JSONL events containing shell/MCP/function calls. Product optionally supplies visible work logs and outcome records."}, "learning_scope": {"assessment": "known", "basis": "wired", "values": ["cross-task"], "records": ["RTE-2", "RTE-3", "RTE-4", "RTE-5", "RTE-7"], "note": "Patterns and retained skills derive from multiple training cases and guide later task cases and rounds; inheritance carries them to a new workspace. A project path alone is not a project-scoped learning route. Isolated study aggregates distinct TRAIN tasks and supplies candidate skill to separate VAL tasks, despite stopping after one round."}, "learning_timing": {"assessment": "known", "basis": "wired", "values": ["staged"], "records": ["RTE-2", "RTE-3", "RTE-5", "RTE-9", "RTE-7"], "note": "Explicit training, maintenance, proposal and validation stages; compacted excerpts are prepared after task execution for optimization, not ongoing executor adaptation. Isolated trace compilation and reference comparison occur between completed TRAIN execution and optimizer calls, followed by candidate validation."}, "distilled_form": {"assessment": "known", "basis": "wired", "values": ["natural-language", "symbolic"], "records": ["OBJ-1", "OBJ-3", "OBJ-5", "OBJ-6", "OBJ-9", "RTE-7"], "note": "Patterns and procedural skills are prose; retained compacted trace prompts include machine-selected command/call records and structured outcomes that guide the optimizer. No parameter update route."}, "faithfulness_tested": {"assessment": "not-determinable", "basis": null, "values": [], "records": ["CLM-4", "RTE-7"], "note": "Wired admission tests compare outcomes; this inspection does not verify retained execution evidence that tests dependence on recalled content. Research result artifacts were enumerated but not audited for that narrower criterion. Isolated read-ID checks establish access, not semantic dependence on recalled content."}}}
---

# WikiSkill (Stahl-G) agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/wikiskill-stahl-g.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/memory-report.md`

**Memory analysis report SHA-256:** 2a3cccdd139e91b6458bb30bd9280335926b7a3ade09e65e9594fae62c15f62e

The source-native name is WikiSkill (Stahl-G). This is Stahl-G's independent implementation of ideas from the WikiSkill paper, not the paper authors' code. No earlier system analysis, ingest or comparison supplied findings.

## Boundary and evidence

Evidence basis: static inspection of implementation and shipped doctrine at commit `9df975b2145a0e924f344f2a3d116e11d3f025ac`, cutoff 2026-09-17. This whole-system analysis characterizes the improvement plane: product request controller, native-role handoffs, Wiki and skill updates, direct research engine and domain adapter interfaces, optional isolated spreadsheet study, scorer authorization, and local skill installation/recovery. It is intended to establish what changes and who admits each change.

The product returns requests to an enclosing host rather than owning the host's model/tool loop. Host runtime implementations and provider internals are excluded: neither actual fresh context, weight identity, deployed permissions nor behavioral activation can be established from this repository. External datasets, live search/environment services, and imported package internals are excluded: their truth and availability are not certified. Domain adapters are inspected at dispatch/scoring boundaries, not every benchmark matcher or tool implementation. Reported historical performance and retained research specimens are not independently audited; no observed or causal effectiveness conclusion follows. Static baseline coverage includes all materially different orchestration/admission families, with these functional limits.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/Stahl-G/wikiskill` | `9df975b2145a0e924f344f2a3d116e11d3f025ac` | implementation | Product controller, native handoff, scoring/trust/install, engine, Wiki maintenance/proposal, adapter interfaces and isolated study | `src/wikiskill/product.py:1-430`; `src/wikiskill/native_agents.py:1-198`; `src/wikiskill/score_rules.py`; `src/wikiskill/scorer_trust.py:15-74`; `src/wikiskill/product_install.py:30-103`; `src/wikiskill/engine.py:63-284`; `src/wikiskill/officeqa/wiki_agents.py`; `src/wikiskill/wiki.py`; `src/wikiskill/wiki_maintainer.py`; `src/wikiskill/officeqa/rollout.py`; `src/wikiskill/officeqa/scoring.py`; `src/wikiskill/spreadsheet/rollout.py`; `src/wikiskill/livemath/rollout.py`; `src/wikiskill/sealqa/rollout.py`; `src/wikiskill/alfworld/rollout.py`; `src/wikiskill/isolated/runtime.py:70-140,337-415`; `src/wikiskill/spreadsheet/study.py`; `src/wikiskill/paper_alignment/evidence.py`; `src/wikiskill/paper_alignment/contracts.py`; `src/wikiskill/officeqa/loop.py`; `src/wikiskill/livemath/loop.py`; `src/wikiskill/sealqa/loop.py`; `src/wikiskill/spreadsheet/loop.py`; `pyproject.toml:1-32` | Operational access root `/home/zby/llm/commonplace/related-systems/Stahl-G--wikiskill`; only commit-addressed blobs inspected. No provider or deployment observation. |
| SRC-2 | Git | `https://github.com/Stahl-G/wikiskill` | `9df975b2145a0e924f344f2a3d116e11d3f025ac` | doctrine/design | README and packaged role instructions | `README.md:1-160`; `src/wikiskill/resources/product/roles/executor.md`; `src/wikiskill/resources/product/roles/maintainer.md`; `src/wikiskill/resources/product/roles/proposer.md` | Statements of intent and reported outcomes are not execution evidence. |

## Shared records

### Components

CMP-1 — Product controller. Conclusion status: wired. Python event-driven workflow emits work and admits submitted results; JSON records and SHA-256 identities reconstruct state. Installed CLI is `wikiskill`, package `wikiskill-research` 0.1.1, Python 3.11+. SRC-1 `src/wikiskill/product.py:1-154`, `pyproject.toml:5-25`.

> This controller emits work requests; the caller's agent executes them in its
> normal environment. Immutable event records own scores and retained versions.
> No model is invoked and no sandbox or account configuration is changed here.
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CMP-2 — Host-selected executor, Maintainer and Proposer model roles. Conclusion status: afforded for model operation; wired for request preparation. Distributed-parametric consumer supplied by caller, with natural-language role instructions. Product configuration records `caller_selected`; actual parameters and endpoint resolution are uninspected. No exact weight version is pinned by product configuration. Its changed artifacts are Wiki/skills, not an implemented weight-training call in this controller. Native delegation records the host's returned ID; it cannot attest host execution. SRC-1 `src/wikiskill/product.py:183-190,275-292`, `src/wikiskill/native_agents.py:125-143`.

> 'execution':'host_agent','environment':'host_default','model':'caller_selected','agent_runtime':agent_runtime}
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CMP-3 — Direct research engine and adapter/model clients. Conclusion status: wired. Domain rollouts and Wiki optimizer calls use configured model/effort identifiers through Codex CLI. Requested/reported model checks concern identities exposed by that runtime, not an immutable provider weights digest. Parameter change and provider internals: uninspected. The isolated backend selects a model catalog/slug and separate context; this is configuration pinning, not inspection of provider parameters. SRC-1 `src/wikiskill/engine.py:148-284`, `src/wikiskill/officeqa/rollout.py:77-115,189-214`, `src/wikiskill/isolated/runtime.py:86-140`.

> if json_events:
>     cmd.append("--json")
> if output_last_message is not None:
>     cmd += ["--output-last-message", str(output_last_message)]
> cmd.append("-")
> env = dict(os.environ)
> env.pop("CODEX_HOME", None)
> --- `src/wikiskill/officeqa/rollout.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CMP-4 — Scorers and isolated tool execution boundary. Conclusion status: wired. Product accepts a finite supplied score or executes a locally authorized subprocess; direct research uses adapter scorers; isolated execution requires macOS sandbox-exec, Codex, spreadsheet dependencies and a matching catalog. These symbolic components issue operational verdicts but do not establish general correctness. SRC-1 `src/wikiskill/product.py:321-365`, `src/wikiskill/scorer_trust.py:15-74`, `src/wikiskill/isolated/runtime.py:120-140`.

### Operative objects

OBJ-1 — Product Wiki patterns: source-named natural-language content plus symbolic source identifiers, retained in event JSON and projected Markdown files. SRC-1 `src/wikiskill/product.py:235-255,367-385`.

OBJ-2 — Product human feedback: original text, source metadata and copied Markdown records, later present in learning contexts and inherited runs. SRC-1 `src/wikiskill/product.py:170-180,405-411`.

OBJ-3 — Product current and candidate SKILL.md files: copied immutable artifacts with SHA-256 metadata, instructional prose delivered by request/host. Candidate is distinct from retained successor. SRC-1 `src/wikiskill/product.py:149-153,275-280,388-403`.

OBJ-4 — Product task outcomes/traces and gate history: scores/feedback/identities in event JSON, optional raw trace and actual output files, copied hashes. Output may be binary; metadata does not decide payload representational form. SRC-1 `src/wikiskill/product.py:321-365`.

OBJ-5 — Research Wiki pattern pages and index: Markdown rules/explanations and access structure, read by Maintainer/Proposer, with structured edit contracts. SRC-1 `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/officeqa/wiki_agents.py`.

OBJ-6 — Research current and candidate skills: retained Markdown in direct evolution and structured skill objects/rendered prose in isolated study, selected by score gate. SRC-1 `src/wikiskill/engine.py:225-278`, `src/wikiskill/spreadsheet/study.py:615-655`.

OBJ-7 — Research skill-impact records and trajectories: symbolic score/purpose/pattern references plus textual execution material. Distinguish raw trajectories from automatic compressed context and generated guidance. SRC-1 `src/wikiskill/engine.py:261-282`, `src/wikiskill/officeqa/wiki_agents.py:147-218,565-580`.

OBJ-9 — Retained optimizer prompt snapshots. Files contain selected/compacted outcomes and tool calls plus Wiki context and feed later optimizer calls. These are derived consumer inputs rather than raw logging. SRC-1 `src/wikiskill/officeqa/wiki_agents.py:318-345,651-661`. Conclusion status: wired.

OBJ-10 — Installation backups and receipts. Previous skill bytes plus installed/previous hashes allow user-requested withdrawal with retained history. SRC-1 `src/wikiskill/product_install.py:42-68,73-102`. Conclusion status: wired.

OBJ-8 — Product request/event and scorer authorization records. Symbolic JSON/files bind comparison configuration, submitted artifacts, identities and local scorer authorization. Their role is recovery and admission, not independent semantic endorsement. SRC-1 `src/wikiskill/product.py:96-147`, `src/wikiskill/scorer_trust.py:15-74`.

OBJ-11 — Isolated TRAIN reference feedback. Symbolic prediction/reference/match and formula records derive from output/reference workbook comparison, with sealed count checks. Large payloads retain all cells in paged files and present an index/preview; preview is not the whole payload. Learning roles can request full pages. SRC-1 `src/wikiskill/spreadsheet/study.py:467-552`. Conclusion status: wired.

### Routes

RTE-1 — Product start → next task → external execution → record/scorer → next phase. Implementation conclusion status: wired. Principal supplies train/validation inputs, optional initial skill, rounds, direction and scorer. Controller decides phase symbolically; host owns model/tool choices and task execution. Request identity and selected skill enter context; executor outputs are copied before scoring. External scorer sees full task (including references when supplied), while task request omits top-level reference/expected/gold/score fields. Immediate return is pending work or status, terminal return complete state. Events persist, repeated completed submissions require compatible bytes/scores; failed scoring retains output and requires explicit retry. It serves bounded user-chosen practice batches, not autonomous open-ended task acquisition. Read-back: controller reconstructs state; later task receives retained skill through RTE-3; delegation payload visibility through RTE-6. Selection uses current phase and pending task IDs; no expiry, changed task inputs block continuation. Activation/benefit uninspected. SRC-1 `src/wikiskill/product.py:155-235,257-295,296-365`.

> req['task']={k:v for k,v in task.items() if k not in ('reference','expected','gold','score','file_sha256')}
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> if any(row.get('scorer_authorization') != info['fingerprint'] for row in s['results'].values()):
>     raise ValueError('Scorer changed after recorded scores. Start a new workspace for a consistent comparison; old outputs and scores remain preserved.')
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-2 — Product Maintainer learn and human feedback writes. Implementation conclusion status: wired; external interpretation afforded. Training completion produces a context containing training results, prior Wiki, feedback, current skill and gate history. Host Maintainer proposes patterns; controller admits nonblank named content with nonempty allowed source IDs. This validates provenance references, not semantic support. Same-name content updates existing patterns; original feedback persists. Return moves to Proposer; learning context later reads retained content. No automatic semantic withdrawal is established; event history preserves earlier content. Retained guidance is theory when rules prescribe procedures: rule-level structure, with rationale optional in content and no enforced defect-localization schema. Theory application is afforded in host prompts; outcome-to-specific-rule diagnosis and actual changed-rule activation remain uninspected. SRC-1 `src/wikiskill/product.py:248-255,367-411`. Specialist evidence supplements this route below.

> if not isinstance(sources,list) or not sources or any(x not in allowed for x in sources):raise ValueError('Cite permitted training request or human-feedback IDs')
> patterns[name]={'content':content,'sources':sources}
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-3 — Product Proposer → candidate validation → retained skill gate. Implementation conclusion status: wired. Model/host proposes nonblank skill or no_action from learning context; code decides adoption with strict improvement over retained best score, configurable maximize/minimize and minimum. Human controls task/scorer setup and supplies non-scorer ratings; controller can reject ties or regressions and leaves incumbent current. Candidate bytes and note persist independently of adoption. Successor skill appears in later task requests; Wiki is not rolled back by skill rejection. Behavioral effect is uninspected. Theory guidance is current skill/Wiki rules, not model weights; the code routes outcomes back into context, but a skill edit alone does not establish a localized theory correction. Link statuses: guidance delivery wired, outcome delivery wired, theory revision in response afforded, revised successor delivery wired conditional on gate, actual theory-guided behavior uninspected. These procedures describe executor organization inside the declared improvement plane boundary in part, but complete reflective theory refinement is uninspected. SRC-1 `src/wikiskill/product.py:212-233,248-255,275-292,388-403`, `src/wikiskill/score_rules.py`.

> return improvement(candidate, incumbent, direction) > threshold
> --- `src/wikiskill/score_rules.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> if value['accepted']: s.update(best_score=value['candidate_score'],current_skill=value['skill'])
> --- `src/wikiskill/product.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-4 — Product inheritance and export/install. Conclusion status: wired. User selects prior workspace or completed retained skill. `start --from` imports prior patterns/feedback and defaults to prior current skill; new tasks establish a new comparison. Export copies current skill with provenance; install requires completed loop, explicit replacement for differing existing skill, backup and restore identity checks. Inherited patterns retain source references but original raw task records/traces and prior gate history are not copied; lineage may require the original workspace. Human chooses admission to a consuming project; the host's later skill loading is afforded, not demonstrated. Persistent bytes survive across task batches; no implicit expiry. Retained guidance is copied theory, application rather than new refinement; export itself creates no new theory. Recovery restores backed-up bytes only if installed state matches. SRC-1 `src/wikiskill/product.py:165-180,420-429`, `src/wikiskill/product_install.py:30-103`.

> if current != receipt['installed_sha256']:
>     raise ValueError('Installed skill changed since this backup; preserve those edits before restoring')
> --- `src/wikiskill/product_install.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-5 — Direct research evolution. Conclusion status: wired. Operator fixes manifest, train/validation split, model/effort, optimizer and iteration budget. Engine executes baseline validation, training under incumbent, Maintainer then Proposer, and candidate validation. Model calls propose edits; contracts reject malformed/oversized/evaluation-vocabulary proposals; score gate chooses successor. Retained Wiki and impacts enter later iterations even after skill rejection. Cached valid outcomes resume under a cases/config/skill binding; infrastructure errors retain attempts, drain outstanding workers, then stop. Prompt, manifest and incumbent changes block resume. Immediate return is state/progress; terminal output is evolution_complete or validation ceiling, not a deployment. Guidance is editable Wiki rules plus skill procedures, partly explanatory; purpose/pattern references survive gate feedback. This affords revising a theory, but outcome attribution to a specific premise is a model judgment and not codified by numeric gain. Guidance delivery wired, outcome delivery wired, proposed revision afforded, successor delivery wired; actual refinement and benefit uninspected. SRC-1 `src/wikiskill/engine.py:63-284`, `src/wikiskill/officeqa/wiki_agents.py:432-508,565-580`. Memory amendment: full proposal rationale/diff is not all automatically delivered in impact summaries; legacy LiveMath resume substitutes a resume purpose and empty pattern references (`src/wikiskill/livemath/loop.py:244-258`). Retained behavior therefore does not guarantee retained diagnostic rationale across every resume branch.

> if sha256((root/'wiki/prompts'/name).read_bytes()).hexdigest() != expected:
>     raise ValueError('Agent prompt changed during evolution')
> --- `src/wikiskill/engine.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> # Model-facing impact contains accepted and rejected proposals alike.
> --- `src/wikiskill/engine.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> if entry.purpose_summary:
>     lines.append(f"  purpose: {entry.purpose_summary}")
> if entry.motivated_by_patterns:
>     lines.append(f"  patterns: {', '.join(entry.motivated_by_patterns)}")
> --- `src/wikiskill/officeqa/wiki_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-6 — Native host dispatch/bind/collect. Conclusion status: wired for handoff protocol; host execution afforded. Host-selected runtime uses fresh-role request assets; executor receives task/skill only, learning roles get current skill, Wiki, feedback, training records and gate summaries. Controller enforces binding before submissions and rejects reused agent IDs. It records fresh-context assertions, not independently attested host context. Host owns actual spawn, tool grants, wait and cancellation; no filesystem sandbox follows from this route. Collection confines output path to request output directory and then invokes normal record/learn/propose. Failed score retries can reuse saved output/delegation; completed work is not resubmitted. Immediate return is handoff or collected status; later visibility is phase-specific. Static role instructions are not accumulated memory. SRC-1 `src/wikiskill/native_agents.py:48-198`, `src/wikiskill/product.py:316-319`. Memory amendment: native learning context strips proposal notes and candidate identity from gate history, unlike general product context; previous rejected-proposal explanations are therefore not automatically delivered by this branch.

> context['gate_history'] = [{k: row[k] for k in ('round','verdict','incumbent_score','candidate_score','improvement')}
>                            for row in state['history']]
> --- `src/wikiskill/native_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> 'context_mode': context_mode, 'evidence': 'host-reported; not independent attestation'}
> --- `src/wikiskill/native_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-7 — Isolated spreadsheet study. Conclusion status: wired. Operator prepares bounded study; controller freezes protocol, runs fresh baseline/training, separate learning roles, candidate validation, and single strict score gate. Isolated context disables memory/project instruction loads and web/network in configuration; macOS-specific tools boundary and audits differ from ordinary product/direct execution. Maintainer gets sampled traces; Proposer's declared read IDs must equal audited file reads before proposal contract admission. Training reference-cell feedback is explicitly supplied; validation/test references are excluded from learning role payload by construction. Maintainer Wiki survives rejection; active skill becomes candidate only on better validation count, otherwise empty initial skill. The one-round study proposes against an empty skill mapping; patching an existing skill is therefore not reached in this route. Separate PURPOSE.md content is retained in skill objects, but validation renders only skill_md; no later study round consumes that retained purpose. No automatic retry after an unsealed native attempt; recover unchanged sealed calls or create separate study. Outcome: final skill, gate, impact and freeze manifest. Guidance is theory in Wiki/skill content; code verifies reads, not the model's use of reasons. Guidance delivery wired, outcome feedback wired, revision afforded, candidate validation delivery wired, post-study deployment uninspected. SRC-1 `src/wikiskill/isolated/runtime.py:86-140,337-415`, `src/wikiskill/spreadsheet/study.py:467-501,570-660`.

> if reads != sorted(set(submitted.get("read_trace_ids", []))):
>     raise IntegrityError("Proposer trace IDs do not match successful actual file reads")
> --- `src/wikiskill/spreadsheet/study.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> accepted = candidate_correct is not None and candidate_correct > baseline_correct
> active = candidate if accepted else {}
> --- `src/wikiskill/spreadsheet/study.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> if archive.exists():
>     raise IntegrityError('Unsealed native attempt preserved; no automatic model retry')
> --- `src/wikiskill/isolated/runtime.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> if len(set(read_trace_ids))<4:raise ContractError('Read at least four distinct execution traces before proposing a change')
> --- `src/wikiskill/paper_alignment/contracts.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> change, candidate = contracts.proposal(submitted["proposal"], {}, reads)
> --- `src/wikiskill/spreadsheet/study.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> def skill_text(skills):
>     return '\n\n'.join(skills[name]['skill_md'].strip() for name in sorted(skills))
> --- `src/wikiskill/paper_alignment/contracts.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> _save(root / "skill-impact.json", {"iteration": 1, "proposal": change, "gate": gate,
>                                     "candidate_skills": candidate, "wiki_retained": True})
> --- `src/wikiskill/spreadsheet/study.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> _save_text(payload / trace_path, evidence.visible_trace(row, case, limit=15000))
> --- `src/wikiskill/spreadsheet/study.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-8 — Scorer capability admission. Conclusion status: wired. Operator authorizes fingerprint of command, executable/direct files, cwd, workspace and timeout. Controller checks receipt before execution; changed fingerprint after prior scores prevents comparison continuation. Scorer subprocess uses normal host permissions, not product-enforced isolation; imported dependencies are outside fingerprint coverage. Immediate return is trusted metadata or error, later reads authorize scoring, no memory interpretation. Rejection is missing/mismatched receipt; recovery is inspection/reauthorization or new comparison. Guidance: none; symbolic configuration and operator approval authorize capability, not theory revision. SRC-1 `src/wikiskill/scorer_trust.py:15-74`, `src/wikiskill/product.py:331-355`.

> 'scope':'Runs with normal host permissions; direct files are fingerprinted, not every imported dependency.'}
> --- `src/wikiskill/scorer_trust.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-9 — Research trace compaction and optimizer context delivery. Conclusion status: wired for persisted context preparation/direct delivery; requested full-file reads afforded. Training completion selects bounded success/failure samples, last 40 stdout lines and last 12 parsed tool events. Maintainer receives full non-prompt Wiki; proposer receives index, summarized impacts and incumbent, with staged full files for requested reads. A 900,000-character ceiling rejects excess rather than selecting Wiki pages. Immediate return is assembled prompt/model result, prompt.md persists; later optimizer consumes it. Selection is coarse score/category plus deterministic sampling, not semantic retrieval. No expiry; new iteration creates new context. Guided transformation is symbolic extraction/reshaping rather than a separately revised theory; it can support later theoretical interpretation. Activation and fidelity uninspected. SRC-1 `src/wikiskill/officeqa/wiki_agents.py:129-143,169-218,300-345,407-424,611-661`, `src/wikiskill/wiki.py:132-143`.

> kept = commands[-max_commands:]
> --- `src/wikiskill/officeqa/wiki_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> (iter_dir / "prompt.md").write_text(prompt, encoding="utf-8")
> --- `src/wikiskill/officeqa/wiki_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> for path in sorted(wiki_dir.rglob("*.md")):
>     if "prompts" in path.parts:
>         continue  # harness-owned prompt files are not loop memory
>     snapshot[path.relative_to(wiki_dir).as_posix()] = path.read_text(
>         encoding="utf-8"
>     )
> --- `src/wikiskill/wiki.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

> "### Staged files you may read on demand",
> --- `src/wikiskill/officeqa/wiki_agents.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

RTE-10 — Research read-back into task execution. Conclusion status: wired. Batch selection supplies retained skill to next train or candidate validation rollout; domain prompt builders append nonempty skill without semantic relevance filtering. Immediate consumer is executor prompt, no separate memory write; persistent skill remains until replacement, no timed expiry. Delegated model sees selected skill, not necessarily motivating Wiki or proposal rationale. Guidance theory application is afforded by instructions, actual interpretation uninspected. SRC-1 `src/wikiskill/engine.py:148-174,225-228`, `src/wikiskill/officeqa/rollout.py:53-63`; BAP-1 holds minimum quote.

RTE-11 — External installation withdrawal. Conclusion status: wired. Refines RTE-4's install/restore branch without changing its identity. User selects backup; receipt admits restoration only when target matches installed or previous hash; restores previous skill or removes newly installed skill, while preserving history. Immediate return is restore status; later external host consumption afforded, not evidenced. Theory content is copied, not revised; no outcome diagnosis is claimed. SRC-1 `src/wikiskill/product_install.py:73-102`; OBJ-10, RTE-4 carry evidence.

### Claims

CLM-1 — Independent implementation and experience→Wiki→skills purpose. Conclusion status: claimed. SRC-2 `README.md:3-24`. Implementation supports a separated write/adoption loop, not verification of the paper's experiments.

> Built from the ideas in **[WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://huggingface.co/papers/2608.27454)**, this independent implementation lets your existing agent enter an improvement loop using its own model and normal tools.
> --- `README.md` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CLM-2 — Better score admits skill while Wiki retains learning on rejection. Conclusion status: claimed; implementation support wired through RTE-2, RTE-3, RTE-5, RTE-7. Warrant is configured task score, not generalization or explanation validity. SRC-2 `README.md:20-24`.

> A **Wiki Maintainer** consolidates experience. A **Skill Proposer** turns relevant patterns into a candidate skill. The agent tries it on validation tasks; the system keeps it only if its score improves. If the candidate is rejected, the Wiki retains what was learned.
> --- `README.md` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CLM-3 — Native fresh contexts are not filesystem sandboxes. Conclusion status: claimed, protocol bound in RTE-6. SRC-2 `README.md:106-113`. Actual host adherence remains uninspected.

> Fresh child contexts still inherit host policies and may receive project instructions or memory. They are not filesystem sandboxes.
> --- `README.md` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

CLM-4 — Recall faithfulness remains uninspected. Retained research experiment files were enumerated but not audited for dependence on recalled content. A score gate or higher score alone cannot establish that dependence. SRC-1 `src/wikiskill/engine.py:250-264`, `src/wikiskill/resources/research/` (tree boundary only). This is an uncertainty, not an absence.

### Evidenced absences

No separate absence claim is made from a search miss. Provider internals, behavioral activation, historical performance replication and universal knowledge validity remain uninspected, not absent.

### Behavioral-authority paths

BAP-1 — Executor consumes retained/candidate skill through product task payload or research prompt; force instruction, horizon selected task or iteration; delivery wired, interpretation/activation uninspected. SRC-1 `src/wikiskill/product.py:275-285`, `src/wikiskill/officeqa/rollout.py:53-63`.

> if skill_text.strip():
>     prompt += f"\n{SKILL_SECTION_HEADER}\n\n{skill_text}\n"
> --- `src/wikiskill/officeqa/rollout.py` @ `9df975b2145a0e924f344f2a3d116e11d3f025ac`

BAP-2 — Maintainer/Proposer consume Wiki, feedback, outcome and prior gate context as knowledge and learning guidance for the next proposal; force advisory, horizon current role call and retained revisions. SRC-1 `src/wikiskill/product.py:248-255`, `src/wikiskill/officeqa/wiki_agents.py:565-580`. Delivery wired; semantic reliance uninspected.

BAP-3 — Controller consumes numeric score and gate condition; force enforcing successor selection, horizon subsequent tasks within comparison. Epistemic license is measured configured score only. SRC-1 `src/wikiskill/product.py:212-233`, `src/wikiskill/engine.py:251-278`. Wired.

BAP-4 — Product controller consumes local scorer receipt and native binding; force admission, horizon matching scorer configuration or request. Receipt permits execution, not truth of scorer output; native binding permits submission, not attestation of isolation. SRC-1 `src/wikiskill/scorer_trust.py:70-74`, `src/wikiskill/product.py:316-319`. Wired.

## Runtime account

Ordinary invocation begins with operator-supplied train/validation examples and optional skill. `start` binds tasks/configuration. `next` reconstructs immutable journal state and requests baseline validation work. Host executes request, returns actual output, and either an authorized external scorer or supplied human/rubric score judges it. Successful completion advances to incumbent training, Wiki maintenance, skill proposal, candidate validation and strict admission. Training/validation are reused across bounded rounds. The host may batch pending requests; the controller serializes writes with a workspace lock. Completion returns retained skill/history; installation is a separate user-selected mutation with backup.

Principal/identity: operator chooses experiment and host; each request gets ID and optional native agent binding. Policy is symbolic stage progression plus natural-language role instructions. State lives in artifact files and event JSON, not only model context. External host has execution authority; product only constructs and verifies submission contracts. External scorer is another effect boundary with local approval. Model calls belong to host in product mode; research directly spawns Codex subprocesses and controls worker concurrency. Logging/hash identity can expose changed bytes and support resume, but it is not a tamperproof log against a writer able to replace all records.

Material alternatives: manual host submission versus native dispatch; explicit supplied score versus external subprocess scorer; direct research engine with five domain adapters plus OfficeQA retrieval variant; optional isolated spreadsheet study; synthetic offline demo. No guarantee from isolated study is assigned to ordinary product/default host execution. Direct research requests workspace-write but inherits the installed runtime's capabilities; isolated route has its own macOS-specific config/tool surface. Learned skill cannot by itself grant tools withheld by its host.

Four forcing cases were traced statically:

1. Candidate ties or underperforms: strict comparator rejects; incumbent remains; Wiki and candidate/impact history persist (RTE-2, RTE-3, RTE-5, RTE-7). No-action skips candidate execution and remains a non-admission.
2. Scorer fails or returns invalid/nonfinite result: product records failure with output, stops progress, requires explicit retry; it does not convert this to a wrong answer. Scorer/task/config changes after recorded comparison are blocked (RTE-1, RTE-8).
3. Native submission without binding or reused child identity: normal native workflow rejects; host-reported binding remains the trust boundary. Scoring retry can reuse a previous execution without fabricating another fresh run (RTE-6).
4. Research attempt interrupts: direct engine resumes cached valid tasks with binding and preserves failed attempts; isolated study refuses automatic reuse of unsealed attempt and accepts only unchanged sealed native calls (RTE-5, RTE-7).

Guarantees: product lock and phase gate are code invariants only on controller entry paths with filesystem contracts intact. Host fresh context is protocol strength, owned by the host and coordinator, not an isolation invariant. Scorer receipt is capability admission policy over fingerprinted direct files, with normal host execution. Isolated boundary is a deployment-dependent mechanism requiring its checked macOS/backend contracts; this static pass makes no deployed isolation guarantee.

Decision roles: Maintainer/Proposer model roles generate diagnoses/edits. Product/controller contracts can reject malformed provenance or proposals, and numeric gate decides successor. Human chooses tasks, metric, direction, threshold, scorer trust and installation; human rating can replace external scoring. Research fixes train/validation and optimizer choices; demonstration mode generates synthetic proposals. Improvement trigger is training completion; operating modes are bounded experiments/practice batches, including cross-batch inheritance. There is no inferred self-selected curriculum.

Answer-oracle access is mode-specific. Product task may contain supplied reference/expected/gold for scorer, withheld from executor request; train results include full task in learning context, so product learning is not a universal gold-free route. No-scorer mode has only supplied ratings unless caller actually supplies an expected answer. Direct OfficeQA uses reference-answer matcher; SealQA and LiveMath call answer scoring; Spreadsheet compares produced workbook to reference workbook; ALFWorld uses environment win state. These judge task outcomes, not Wiki explanations. Isolated spreadsheet deliberately exposes training cell references and verifies feedback counts against sealed scorer counts, while keeping validation/test materials out of learning payload. Dataset authors/operator provide references, and their truth is outside scope. SRC-1 `src/wikiskill/product.py:248-255,280-285,340-350`, `src/wikiskill/officeqa/scoring.py:22-37`, `src/wikiskill/sealqa/rollout.py:117`, `src/wikiskill/livemath/rollout.py:97-99`, `src/wikiskill/spreadsheet/rollout.py:120-127`, `src/wikiskill/alfworld/rollout.py:179`, `src/wikiskill/spreadsheet/study.py:467-501`.

No dynamic check planned. Considered a synthetic demo, full host workflow, adapter benchmark run and isolated study. Static branches answer the control/admission question; a synthetic demo would not establish model use, and live calls require paid models, host credentials/services and platform dependencies outside this authorization. No target execution was attempted; no observed or causal conclusion is supported by this pass.

## Lens scoping

### Memory/context scope

Full depth. Trigger CLM-1, CLM-2; objects OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7; routes RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7. Retained content and its write/read routes are the intended mechanism. Fresh specialist has fixed revision/input identity and must account for product/direct/isolated branches, opaque payloads and trace compaction. Excludes static shipped prompts as accumulated memory and external host memory.

### Epistemic scope

Full depth. Trigger CLM-1, CLM-2; SRC-1, SRC-2; Wiki generalizations, skill changes, task scoring and adoption through the same objects/routes plus OBJ-8, RTE-8. Question: which outcome evidence licenses what retained content or successor? Include lineage/check/admission and direct policy adaptation. Exclude external dataset truth, model internals and unaudited historical experiments; these prevent empirical/general validity conclusions.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried product Wiki/feedback/skills/outcomes, direct research Wiki/impacts/skills, compacted optimizer contexts, installation backups, and isolated study feedback/Wiki/skill objects. Its complete report is integrated into the canonical objects and routes, not required to interpret them. All fourteen comparison fields retain its classifications and uncertainty.

RTE-2 and RTE-3 separate Wiki admission from scored skill adoption. RTE-5, RTE-9 and RTE-10 wire direct model-based extraction and later instruction delivery. RTE-7 adds a single-round isolated branch with TRAIN reference feedback, successful trace-read checks and no later round. RTE-4 transfers retained knowledge/skills across batches without transferring all original experience; RTE-11 withdraws an installed skill while retaining backup history.

File storage includes prose and symbolic records, but the aggregate representation axis is not-determinable because OBJ-4 admits opaque outputs/traces. Lineage includes authored/imported material, trace extraction, and compiled indexes/context. Native host semantic writing and requested reads are afforded; direct research extraction and conditional read-back are wired. Neither delivery nor an admission gate establishes semantic activation or recall faithfulness.

Push signals are explicit: product round/phase/request identity selects completed training rows for learning roles, while Wiki/feedback/history and selected skill supply are coarse. Research success/failure sampling and full-Wiki supply are coarse; proposer choice to read named staged files is pull, not inferred-judgment push. In RTE-7 sampled Maintainer traces are inline push; Proposer uses requested read_file access, with successful distinct reads checked before a change. These signals do not imply semantic relevance ranking.

Every trace-fed durable write was checked: generated Wiki and skills through RTE-2, RTE-3, RTE-5, RTE-7, plus persisted compaction through RTE-9 and isolated visible-trace files. The main learning horizon is cross-task and staged: completed TRAIN cases inform optimizer calls and later distinct execution/VAL cases. The isolated branch remains cross-task despite ending after one round. Compaction creates retained behavior-shaping input even without inventing a new claim; its symbolic and natural-language forms both enter distilled_form.

Reasons are branch-specific. RTE-6 strips prior proposal notes/candidate identity from native gate history; general product contexts retain them. RTE-5 delivers summarized purpose/pattern references but not every rationale/diff, and legacy resume can weaken provenance. RTE-7 retains separate purpose text with structured headings, while validation consumes only skill_md and no later round consumes that separate purpose. Skill retention is therefore not equivalent to retaining and reusing its explanatory rationale.

Limitations remain explicit: no host compliance observation, no audited retained recall-dependence experiments, no proof that cited source IDs warrant a pattern, no general reference-hiding guarantee, and no activation or efficacy upgrade from file-read evidence. No material integration issue remains unresolved.

### Epistemic lens

#### 1. Source-and-claim boundary

WikiSkill (Stahl-G), pinned boundary above; SRC-1 implementation and SRC-2 doctrine only. Assessed product/research/isolated content production, scoring, retention, adoption and recovery. Host internal reasoning and research-performance attribution unassessed. CLM-1 and CLM-2 are knowledge/learning claims; source-only evidence supports mechanisms, not accepted truth of every pattern.

#### 2. Epistemic-object inventory

| object | truth-apt part and lineage | warrant limitation |
|---|---|---|
| OBJ-1, OBJ-5 | Model-proposed reusable rules/explanations from training outcomes and prior Wiki | Ampliative interpretations; source IDs or structural edits do not entail their conclusions. |
| OBJ-2 | Imported human observations/instructions | Source identified where supplied; truth remains caller-dependent. |
| OBJ-3, OBJ-6 | Procedural instructions, possibly embedded explanatory assertions | Primarily policy adaptation; any causal/general claims remain model conjectures. |
| OBJ-4, OBJ-7 | Recorded score/output/trace and purpose/history | Scores derive from configured judgment; raw traces are acquired, compact excerpts reshaped; rationale is a model assertion. |
| OBJ-9 | Persisted compact optimizer contexts: trace extraction/reshaping, not new claims by extraction alone | Truncation and selection constrain available evidence; semantic dependence uninspected. |
| OBJ-10 | Copied previous skills and restore metadata | Byte identity supports restoration, not continued applicability. |
| OBJ-11 | TRAIN reference-cell feedback and paged detail | Conditional workbook comparison, not verified truth of reference cells. |
| OBJ-8 | Binding/identity/authorization metadata | Supports byte/configuration relationships and operational permission; no domain truth claim. |

#### 3. Authority-route ledger

All following architectural status: implemented. All observed candidate state: no instance observed within inspected implementation/doctrine evidence; static example strings are not candidate-linked operational evidence. Generic endpoints/forms remain on canonical records. Each row separates a function.

| route | function | content/update relation | target/check and activation | epistemic scope; operational/behavioral force |
|---|---|---|---|---|
| RTE-1 | check/evidence production | entailed derivation within configured scorer domain, or indeterminate supplied rating | Actual task output judged after completion; external scorer or human score | Score for named task/metric only; BAP-3 enables phase/gate. No endorsement of process explanation. |
| RTE-2 | content transformation | ampliative conjecture for reusable Wiki explanations; acquisition/import for human feedback | Maintainer interprets training/current guidance; human supplies note | Candidate generalization, no truth license from fluent explanation; BAP-2 advisory. |
| RTE-2 | disposition/acceptance | no content change | Permitted source IDs and nonblank structure at submission | Acceptance of submission provenance/shape only, not epistemic acceptance of every pattern. BAP-4 permits retention. |
| RTE-2 | retention | no content change | Event update and Markdown projection after successful submission | Future availability even if skill rejected; BAP-2, not post-truth-acceptance integration. |
| RTE-3 | content transformation | non-truth-apt policy/content update; embedded explanations ampliative | Proposer makes skill from current skill/Wiki/records | Candidate behavior, not a deduction from reference answers. BAP-1 candidate instructions. |
| RTE-3 | disposition/acceptance | no content change | Strict validation score gain | Operational acceptance for that comparison; BAP-3 selects successor. Bundle score does not validate each rule or explanation. |
| RTE-3 | operational admission/selection/consumption | no content change | Later request selects retained/candidate skill by phase | BAP-1 instructional use; actual activation uninspected. |
| RTE-4 | operational admission/selection/consumption | no content change | Completed retained skill installed by user-selected operation | Post operational adoption deployment, not proof-based integration of Wiki truth; rollback guarded by hashes. |
| RTE-5 | content transformation | ampliative conjecture and policy update; non-ampliative trace reshaping | Research Maintainer/Proposer use selected outcomes/current Wiki | Structural/citation/size restrictions constrain form, not truth. BAP-2. |
| RTE-5 | disposition/acceptance | no content change | Candidate mean accuracy exceeds retained best | Operational skill admission; no causal attribution to individual pattern. BAP-3. |
| RTE-5 | retention | no content change | Wiki, candidate, accepted/rejected impacts retained | Reasons/pattern references can inform later proposals; not independent theory verification. BAP-2. |
| RTE-6 | lineage/freshness/recovery | no content change | Fresh agent-ID binding and confined collection | Host-reported role separation; BAP-4 controls submissions, no attestation of host behavior. |
| RTE-7 | check/evidence production | entailed derivation within cell comparison domain | Training reference comparisons/read-ID audit | Count consistency and successful file-read evidence; no proof that read content shaped proposal. |
| RTE-7 | content transformation | ampliative conjecture and policy update | Isolated learning roles with training evidence | BAP-2 role guidance; explanatory warrant remains model judgment. |
| RTE-7 | disposition/acceptance | no content change | Strict candidate validation count gain | BAP-3 chooses active skills for bounded study; later deployment uninspected. |
| RTE-9 | content transformation | non-ampliative reshaping | Selected outcome/tool snippets and prompt snapshots | Persisted optimizer context, no claim acceptance; BAP-2. |
| RTE-10 | operational admission/selection/consumption | no content change | Retained skill inserted into later execution prompt | BAP-1 instructional delivery, not demonstrated dependence. |
| RTE-11 | operational admission/selection/consumption | no content change | Matching backup/installed hashes on requested restore | Withdrawal/restoration of installed skill, no truth adjudication. |
| RTE-8 | operational admission/selection/consumption | no content change | Locally trusted scorer fingerprint | Authorizes scorer capability only; BAP-4, not reliability certification. |

Evidence is the SRC-1 path/quote on each referenced canonical route; CLM-1 and CLM-2 govern transformation/adoption rows, CLM-3 governs RTE-6. Shared mismatch: operational score admission is narrower than general knowledge warrant. No whole-system oracle is assigned.

#### 4. Per-object lifecycle disposition

OBJ-1 and OBJ-5 reusable explanations: ampliative conjecture. Observation/anomaly inputs through RTE-2 and RTE-5 are implemented; conjecture is implemented as model request/structured submission. Consequence derivation and testing of individual explanatory claims: not determinable from those routes; operational candidate-skill evaluation is implemented separately through RTE-3, RTE-5, RTE-7. Epistemic acceptance of a particular explanation is not determinable; score acceptance concerns bundle utility, not the explanatory claim. Lifecycle integration of accepted truth is not determinable. Observed candidate state for every phase: no instance observed. Missing evidence: candidate-linked explanation, distinguishing prediction, test and reasoned disposition; no inference from retention to acceptance.

OBJ-2: acquisition/import, discovery lifecycle not applicable; retained source labels preserve attribution, not truth. OBJ-4 and OBJ-7: raw evidence acquisition and trace reshaping; scores are conditional derivations from outputs/references, purpose explanations are indeterminate without inspecting their propositions. No preservation claim is made for opaque product trace/output payloads. Missing evidence: execution-linked inputs and raw outputs.

No lifecycle record for OBJ-3: primarily instructional policy output; relevant direct-adaptation routes RTE-3, RTE-4. No lifecycle record for OBJ-6: primarily instructional policy output; relevant direct-adaptation routes RTE-5, RTE-7. Embedded claims, if any, require the same conjecture/warrant analysis as OBJ-1; these files are not treated as uniformly truth-apt. OBJ-11: acquired reference values and conditional derived comparisons through RTE-7; discovery lifecycle not applicable; sealed counts establish consistency, not reference truth. OBJ-9: non-ampliative reshaping through RTE-9; discovery lifecycle not applicable, retained excerpts preserve selected visible content but omit other trajectory details. OBJ-10: copied content through RTE-11; discovery lifecycle not applicable, byte checks license restoration only.

No lifecycle record for OBJ-8: no candidate domain truth output; relevant permission/recovery routes RTE-1, RTE-6, RTE-8.

#### 5. System-claim versus route comparison

CLM-1 has doctrine support SRC-2 and implemented experience/Wiki/skill routes RTE-2, RTE-3, RTE-5, RTE-7. No observed-run or causal support admitted here. Supported conclusion: machinery for retained experience-shaped instruction changes; unknown: semantic correctness and measured benefit.

CLM-2 has doctrine plus explicit strict gate and independent Wiki retention. It supports selected-metric operational adoption, not universal improvement or validation of every Wiki claim. CLM-3 matches a host-owned protocol with declarative fresh context. No source-only claim of actual host isolation follows.

#### 6. Bounded conclusion

WikiSkill retains model-generated rules and tests candidate instruction bundles against task outcomes. It can reject a skill while preserving its motivating knowledge artifacts. That is a coherent operational learning route, but numeric adoption grants authority to the skill bundle for the configured comparison, not to each explanation as true. Source IDs make lineage inspectable; actual evidence-to-rule inference remains model-dependent. Imported references, cell scorers, text matchers and environment outcomes license only their respective task judgments.

## Reconciliation

Specialist proposals were mapped by exact tokens: MEM-OBJ-1 → OBJ-9; MEM-OBJ-2 → OBJ-10; MEM-OBJ-3 → OBJ-11; MEM-RTE-1 → RTE-9; MEM-RTE-2 → RTE-10; MEM-RTE-3 → RTE-11; MEM-RTE-4 → existing RTE-7; MEM-CLM-1 → CLM-4. RTE-7 keeps its original isolated-study referent; new memory detail annotates that route rather than splitting/reusing its ID. Other seeded IDs retain identity.

Accepted amendments are attached to RTE-4 (inherited references without raw experience), RTE-5 (limited purpose/diff delivery and resume loss) and RTE-6 (native gate-note stripping). They replace any unqualified rationale-preservation inference, not generic object identity. OBJ-4's opaque form and CLM-4's unaudited faithfulness remain uncertainty. The initial specialist pass did not cover the isolated study controller sufficiently; the specialist completed that branch against unchanged frozen input and revalidated its final report before integration.

Memory specialist owns mechanisms/profile; coordinator owns runtime and epistemic authority. Both found separate Wiki retention and skill gate admission, but no independent empirical confirmation is claimed. Scope covers direct, native and isolated alternatives; exact quotes and findings are carried into canonical records. No substantive source conflict remains, and all proposal IDs are confined to this reconciliation mapping.

## Bounded synthesis

WikiSkill (Stahl-G) is an improvement plane around an existing agent. Its product controller delegates execution and interpretation, while retaining comparison configuration, evidence and a strict admission rule. The strongest discriminating separation is between continuing Wiki revision and conditional skill adoption: rejected procedures need not erase retained patterns or feedback. User-selected scorers and immutable records make the comparison inspectable without making it universally valid.

For repeatable tasks with a meaningful supplied metric, the architecture wires a bounded loop from outcomes to reusable rules to scored instructions. For claims about general knowledge quality, isolated host behavior or causal benefit of an individual pattern, this boundary is insufficient. Native host protocol and isolated research backend have different authority and deployment assumptions. Training reference feedback also differs by path; no universal no-gold guarantee applies.

A revisable theory is afforded when Wiki/skills contain rules with separately editable parts; model prompts deliver these to decision-makers. Reflective theory refinement remains uninspected because delivery, edits and score feedback do not establish theory-specific defect localization and actual subsequent behavioral use. Instruction self-improvement is wired as a proposed-change/score-selection mechanism; realized improvement is uninspected. Changing model weights is not required for these retained-instruction learning routes.

Assessment would change with candidate-linked traces showing what guidance shaped a proposal, comparisons distinguishing a rule's predicted consequence, independently verified host isolation, and out-of-comparison evaluation under a frozen scorer/dataset/model boundary. These would answer different gaps; a higher validation score alone cannot resolve all of them.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No target executions or historical result audit | SRC-1, SRC-2, CLM-1, CLM-2 | Source/doctrine only | Observed activation, improvement and causal component effect | Frozen executions, inputs, outputs and controlled comparisons |
| Host and provider internals excluded | CMP-2, CMP-3, RTE-6 | Handoff/CLI configuration | Exact weights, actual fresh context and deployed grants | Host/version configuration and runtime traces |
| Dataset/scorer authority bounded | CMP-4, RTE-1, RTE-5, RTE-7 | Scoring interfaces, selected implementation | General correctness, explanation validity, transfer | Independent reference verification and scoped tests |
| Opaque product output/trace payloads | OBJ-4 | Generic file interface | Complete representation classification for all payloads | Concrete typed payload contract or inspected retained payloads |
| Isolated deployment not run | RTE-7 | Static macOS backend | Effective isolation on any deployment | Backend preflight/audit and adversarial probes under deployed configuration |
| Semantic admission is model-dependent | OBJ-1, OBJ-5, RTE-2, RTE-5 | Shape/provenance checks and score gates | Accepted truth of each explanatory rule | Claim-level predictions, evidence-consuming decisions and later reliance traces |

## Verification and blockers

### Semantic verification

Source pin/origin verified; source reads commit-addressed and selected ranges bounded. Quoted support is minimum text anchored to complete pinned blobs. Canonical source, object, route and authority identities are fixed; statuses distinguish wiring from host affordance and observations. Runtime baseline covers ordinary product route, native/manual/scorer variants, direct and isolated research, and four static forcing cases. Epistemic procedure separates checking, operational adoption, retention and truth warrant. Integrated profile checked against RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-9, RTE-10, RTE-11 and OBJ-9, OBJ-10, OBJ-11. Compaction and isolated trace/reference preparation are included in staged cross-task learning; no per-task horizon inferred from session IDs. Push selectors identify consumers/inputs/selected retained parts; requested file reads remain pull. Opaque output forms and unaudited faithfulness prevent known aggregate answers. Specialist input/run/source/method/report hashes and completion matched; final report validated. Each refinement link remains separately bounded; retained reasons are not inferred to guide diagnosis when delivery/use is missing.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md`; full validation passed cleanly before publication.

### Blockers

None.
