---
type: kb/types/agentic-system-analysis-result.md
description: "Complete retained code-grounded replay analysis of Academic Research Skills at commit 94436237913091d4739870159d241660527e8338, bounded as a complete artifact with a partial external loop"
run-id: AAS-2026-09-03-academic-research-skills-02
system: "Academic Research Skills"
run-date: "2026-09-03"
result-disposition: complete
target-class: "extension or tool mechanism"
boundary-kind: "complete artifact, partial loop"
reviewed-boundary: "git commit 94436237913091d4739870159d241660527e8338"
analysis-cutoff: "2026-09-03"
evidence-tier: code-grounded
---

# Academic Research Skills agentic-system analysis

## Run identity

**Canonical carrier:** `kb/reports/retained/`.

**Physical form:** one file. This file is the canonical entry artifact for run
`AAS-2026-09-03-academic-research-skills-02`.

**Exact-result consumers:** the operability-hardening acceptance audit and
future clean-checkout replay comparison.

**Retention and cleanup:** keep this exact file while the acceptance record or
a durable citation consumes it. Retire it only with that record and every
durable citation.

**Run state:**
`kb/reports/state/agentic-system-analysis/AAS-2026-09-03-academic-research-skills-02/run-state.md`
reached `handoff-ready` before the retained acceptance snapshot. The result does
not depend on that ignored operational file after handoff.

**Permitted projection:**
`kb/agentic-systems/academic-research-skills.md` is a compact library artifact
derived from this run. It is not a substitute for this exact result.

The frozen source register is
`SRCREG-v1-94436237913091d4739870159d241660527e8338`; accepted lens proposals
advanced the reconciled canonical register to
`CANON-v2-94436237913091d4739870159d241660527e8338`. The accepted packets were
`AAS-2026-09-03-academic-research-skills-02-MEM-P1` and
`AAS-2026-09-03-academic-research-skills-02-EPI-P1`. No correction packet was
needed.

## Boundary and evidence

**Intended use:** explain what the reviewed artifact wires, where the loop crosses external participants, what its state and context routes return, and what its research-integrity mechanisms warrant. This result does not assess transfer to Commonplace.

**Classification and boundary:** Academic Research Skills 3.21.1 is an extension or tool mechanism: an independently distributed Claude Code plugin and prompt workflow. Its complete artifact is inside the boundary, but its material loop is partial because Claude Code supplies scheduling, model execution, context assembly, tool dispatch, and permission handling.

Included are the four skills; sixteen command entry files; the role-prompt corpus and three plugin-exposed agents; plugin manifests and hooks; deterministic scripts and schemas; the ordinary ten-stage workflow; direct-mode and alternate-install routes; the Material Passport, ledgers, and caches; citation and package checks; and the optional cross-model transport. The plugin manifest claims thirty-nine prompt roles. A bounded replay count found thirty-eight skill-local agent prompt files plus three plugin-exposed files that duplicate role identities; this packaging detail changes no runtime conclusion. Repository-side CI and tests were inspected only when they established implementation shape, never as observed operation.

Excluded participants and the conclusions their exclusion prevents are:

| Excluded participant | Conclusion prevented |
|---|---|
| Claude Code runtime, model, scheduler, context builder, and tool dispatcher | Whether prompts or hook output reached a model, whether roles ran as declared, and whether the host enforced returned decisions |
| Human researcher and a real project workspace | Whether checkpoints, consent, overrides, source choices, or manuscript decisions actually occurred |
| Crossref, OpenAlex, Semantic Scholar, arXiv, and optional model providers | Whether a live lookup or second-model check returned correct evidence |
| Experiments, raw data, institutions, and external reproducibility systems | Whether reported procedures occurred, data are authentic, analyses reproduce, or manuscript claims are true |

The frozen revision is [commit 94436237913091d4739870159d241660527e8338](https://github.com/Imbad0202/academic-research-skills/commit/94436237913091d4739870159d241660527e8338), committed 2026-09-01T17:57:38Z. It was captured as a 12,341,902-byte commit archive with SHA-256 e298af69dc06ffb6642e5a64141954f3b4169e793626db907bedb0decd22d08c. The result is code-grounded relative to the artifact: material prompts, manifests, hooks, scripts, schemas, alternate paths, and forcing cases were inspected. It is not operation-grounded or causally grounded.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Commit-pinned repository tree | Imbad0202/academic-research-skills; temporary extracted archive | 94436237913091d4739870159d241660527e8338; archive SHA-256 e298af69dc06ffb6642e5a64141954f3b4169e793626db907bedb0decd22d08c | implementation | Plugin metadata, hooks, Python/shell implementations, contracts, Pi adapter, and targeted tests as code evidence | [plugin metadata](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/.claude-plugin/plugin.json), [hook wiring](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/hooks/hooks.json), [write guard](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/ars_write_scope_guard.py), [citation gate](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/verification_gate/__init__.py), [verification cache](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/verification_cache.py), [Codex transport](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/cross_model_codex_transport.py) | External host and services were not present; prevents end-to-end execution and service-result conclusions |
| SRC-2 | Same commit-pinned repository tree, separately scoped | Imbad0202/academic-research-skills documentation and natural-language programs | 94436237913091d4739870159d241660527e8338 | doctrine/design | README, POSITIONING, architecture/control/data-flow docs, skill bodies, role prompts, state machine, Passport protocol, and integrity protocol | [pipeline skill](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/SKILL.md), [orchestrator prompt](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/agents/pipeline_orchestrator_agent.md), [state machine](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/references/pipeline_state_machine.md), [Passport protocol](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/references/passport_as_reset_boundary.md), [architecture](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/docs/ARCHITECTURE.md), [control matrix](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/docs/CONTROL_AVAILABILITY.md), [data flows](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/docs/DATA_FLOWS.md), [positioning](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/POSITIONING.md) | Doctrine cannot prove host adherence, a run, an outcome, or causality; same-revision recovery conflict prevents one determinate persistent-FAIL transition |

No dynamic probe source was selected. There is no observed-run or causal-experiment source in this result.

## Shared records

### Components

| ID | Source-native component | Representational form and substrate | Conclusion status and evidence |
|---|---|---|---|
| CMP-1 | Plugin package, marketplace entry, slash commands, and skill entry surface | JSON plus natural-language Markdown in the Git tree | Package conclusion status: wired. SRC-1 .claude-plugin/plugin.json:1-11, .claude-plugin/marketplace.json:8-20, commands/ars-full.md:1-8 |
| CMP-2 | academic-pipeline lightweight orchestrator | Natural-language system-definition file | Shipped-entry conclusion status: wired; host-operation conclusion status: uninspected. SRC-2 academic-pipeline/SKILL.md:17-32,66-71 |
| CMP-3 | deep-research skill | Natural-language prompts, references, templates, and contracts | Shipped-skill conclusion status: wired; operation conclusion status: uninspected. SRC-2 deep-research/SKILL.md:15-25,103-269 |
| CMP-4 | academic-paper skill | Natural-language prompts plus structured patch and validation contracts | Shipped-skill conclusion status: wired; operation conclusion status: uninspected. SRC-2 academic-paper/SKILL.md:15-25,189-287,361-371 |
| CMP-5 | academic-paper-reviewer skill | Natural-language panel prompts plus structured review contracts | Shipped-skill conclusion status: wired; operation conclusion status: uninspected. SRC-2 academic-paper-reviewer/SKILL.md:15-17,78-238 |
| CMP-6 | Role-prompt corpus and three plugin-exposed agents; manifest claim: thirty-nine roles | Natural-language Markdown in top-level and skill-local agent directories; replay count: thirty-eight skill-local files plus three plugin-exposed duplicate identities | Dispatch conclusion status: claimed; operation conclusion status: uninspected. SRC-1 agents/research_architect_agent.md:1-18 and peers; SRC-2 academic-pipeline/SKILL.md:209-220 and docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md:88-103 |
| CMP-7 | SessionStart and PreToolUse hook layer | JSON hook configuration and shell launcher | Plugin-channel conclusion status: wired; operation conclusion status: uninspected. SRC-1 hooks/hooks.json:1-24, hooks/run_guard.sh:14-32 |
| CMP-8 | Deterministic scripts, reducers, validators, and schemas | Python, shell, JSON Schema, JSON, and YAML in the Git tree | Material-subroute conclusion status: wired; deployed-operation conclusion status: uninspected. SRC-1 scripts/ars_write_scope_guard.py:288-438 and scripts/verification_gate/__init__.py:192-291 |
| CMP-9 | Claude Code host, model, scheduler, context builder, and dispatcher | External software and distributed-parametric model | Boundary conclusion status: uninspected. SRC-2 docs/CONTROL_AVAILABILITY.md:15-46 |
| CMP-10 | Bibliographic index services | External network services and their records | Boundary conclusion status: uninspected. SRC-2 docs/DATA_FLOWS.md:39-67 |
| CMP-11 | Optional cross-model provider and local transport | External model/service plus in-tree Python transport | Transport conclusion status: wired; provider-operation conclusion status: uninspected. SRC-1 scripts/cross_model_codex_transport.py:249-267,787-935 |
| CMP-12 | Human researcher and principal | External human actor | Boundary conclusion status: uninspected. SRC-2 POSITIONING.md:9-17,74-89 |

### Operative objects

| ID | Source-native object | Form | Storage substrate | Evidence |
|---|---|---|---|---|
| OBJ-1 | User request, configuration, and supplied source material | Mixed natural-language and structured input | Host conversation and user workspace | SRC-2 academic-paper/SKILL.md:420-422 |
| OBJ-2 | Research-stage family: bibliography/corpus, RQ brief, methodology blueprint, and synthesis | Mixed; facets are separated in the epistemic lens | Workspace artifacts and Material Passport references | SRC-2 deep-research/SKILL.md:150-220 |
| OBJ-3 | Versioned manuscript, draft, revision, and final-paper family | Natural-language plus embedded structured markers | Workspace files and Passport version references | SRC-2 academic-paper/SKILL.md:361-371 |
| OBJ-4 | Review cards, reports, editorial decision, and revision roadmap | Mixed natural-language and structured records; judgment and derived-decision facets stay separate | Workspace artifacts and Passport | SRC-2 academic-paper-reviewer/SKILL.md:94-216 |
| OBJ-5 | Pipeline state, Material Passport, and append-only reset/resume/compliance/audit ledgers | Mixed YAML/JSON and referenced paths | User-named project files | SRC-2 academic-pipeline/agents/state_tracker_agent.md:8-32,144-173 |
| OBJ-6 | Citation records, resolver outcomes, verification summaries, and cache rows | Structured JSON/records; acquisition, reduction, and cache facets stay separate | Project artifacts and local SQLite cache | SRC-1 scripts/verification_gate/__init__.py:192-291; SRC-2 docs/DATA_FLOWS.md:84-92 |
| OBJ-7 | Claim registry, provenance/traceability records, integrity findings, and verdicts | Mixed structured records and natural-language judgments; registry and verdict facets stay separate | Project artifacts and Passport | SRC-2 academic-pipeline/agents/integrity_verification_agent.md:456-623 |
| OBJ-8 | Cross-model request, judgment, event stream, and validated receipt | Structured JSON plus model-produced truth-apt judgment; request/receipt and judgment facets stay separate | Ephemeral transport and project result artifacts | SRC-1 scripts/cross_model_codex_transport.py:935-953,1251-1310 |
| OBJ-9 | Shipped skill, role, command, and contract corpus | Natural-language and symbolic system-definition artifacts | Git/plugin installation | SRC-1 .claude-plugin/marketplace.json:8-20 |
| OBJ-10 | Final submission package and process record | Mixed MD, LaTeX, PDF, structured markers, and model-authored assessment; package and process-record facets stay separate | User workspace | SRC-2 docs/ARCHITECTURE.md:109-112 |
| OBJ-11 | Checkpoint branch choices, pending decisions, and override receipts used by orchestration | Structured values and attributed natural language | Passport and run-local sidecars | SRC-2 academic-pipeline/references/passport_as_reset_boundary.md:59-78 |
| OBJ-12 | Post-terminal adjudication-activity records and store | Canonical JSON and deterministic rendering | Explicit caller-selected file; no default path | SRC-1 scripts/adjudication_activity.py:1293-1439; SRC-2 academic-pipeline/agents/state_tracker_agent.md:84-109 |
| OBJ-13 | SessionStart update-check state | Structured version/status record with replacement lineage | Local ARS cache file | SRC-1 scripts/ars_update_check.sh:92-215, scripts/announce-ars-loaded.sh:49-142 |
| OBJ-14 | Passport peer human-read ledger | Structured user-attestation events with append/rescind history | Passport-adjacent YAML file | SRC-1 scripts/ars_mark_read.py:92-103,243-323,384-418; scripts/human_read_attestation_resolver.py:311-413 |
| OBJ-15 | Inquiry branch ledger and Passport pointer | Structured append-only event chain, profile bytes, and digest binding | User-project JSON plus Passport reference | SRC-1 scripts/inquiry_branch_ledger.py:1129-1190,1217-1275,2041-2201; SRC-2 academic-pipeline/SKILL.md:338-362 |
| OBJ-16 | Claim-standing probe artifact family | Structured consent, query plan, candidates, stance, transmission, and freshness records | Session-only records or explicitly authorized local export | SRC-1 scripts/build_claim_standing_candidate_ledger.py:928-1145, scripts/check_claim_standing_freshness.py:102-197 |

OBJ-12 is split from the original OBJ-11 family because it has a different consumer and force: it is forbidden from model, checkpoint, gate, verdict, and pipeline-transition inputs. OBJ-13 through OBJ-16 are separately registered because their write agency, retention, invalidation, selection, and consumption differ from the broader state and evidence families.

### Routes

| ID | Endpoints and progression | Owner; context/state/action effect | Implementation conclusion status | Operation conclusion status | Evidence |
|---|---|---|---|---|---|
| RTE-1 | Plugin install or command → SessionStart/command material → external host/model | CMP-1/CMP-7; emits command/agent availability and an optional update reminder | wired | uninspected | SRC-1 hooks/hooks.json:1-24, scripts/announce-ars-loaded.sh:30-142 |
| RTE-2 | User entry → research → writing → integrity → review → revision → final integrity → finalization/process record | CMP-2; selects stages, state transitions, and artifacts | wired | uninspected | SRC-2 academic-pipeline/SKILL.md:101-138 |
| RTE-3 | Orchestrator/subskill → role prompt plus stage artifacts → external model/worker → returned artifact | CMP-2 through CMP-6; declares bounded-call context and role | claimed | uninspected | SRC-2 academic-pipeline/agents/pipeline_orchestrator_agent.md:8-16 |
| RTE-4 | Candidate/report/user choice → semantic check, deterministic subcheck, checkpoint, correction, or recovery → next state | CMP-2/CMP-4/CMP-5/CMP-8/CMP-12; changes progression and sometimes content | claimed | uninspected | SRC-2 academic-pipeline/SKILL.md:125-193; persistent-FAIL conflict recorded below |
| RTE-5 | Matched tool call → PreToolUse launcher/guard → Claude Code dispatcher | CMP-7/CMP-8; deny or pass through one tool call | wired | uninspected | SRC-1 scripts/ars_write_scope_guard.py:288-438, hooks/run_guard.sh:14-28 |
| RTE-6 | Citation → live/cached resolver outcomes → deterministic summary → integrity/terminal policy | CMP-8/CMP-10; acquires, caches, classifies, and supplies gate input | wired | uninspected | SRC-1 scripts/verification_gate/__init__.py:192-291 |
| RTE-7 | Configured route plus user consent → external-model request → validated receipt/judgment → original owner | CMP-2/CMP-8/CMP-11/CMP-12; optional transmission and checking | wired | uninspected | SRC-1 scripts/cross_model_codex_transport.py:249-267,935-953; SRC-2 shared/cross_model_verification.md:9-24 |
| RTE-8 | Completed stage → Passport boundary/ledger → explicit resume hash/path → later orchestrator/stage | CMP-2/CMP-8/CMP-12; intended cross-session state and context recovery | claimed | uninspected | SRC-2 academic-pipeline/references/passport_as_reset_boundary.md:17-125 |
| RTE-9 | Checked draft → formatter/package checks/terminal policy → submission package or remediation | CMP-2/CMP-4/CMP-8; formats, checks, strips audit markers, emits or blocks | claimed | uninspected | SRC-2 docs/ARCHITECTURE.md:109-112 |
| RTE-10 | User → direct single-skill generation or check mode → local output | CMP-1/CMP-3/CMP-4/CMP-5; bypasses the full-pipeline acceptance path | wired | uninspected | SRC-2 academic-pipeline/SKILL.md:83-97 |
| RTE-11 | Skills copy, repo clone, Cowork, Claude Science, or Pi → alternate host behavior | CMP-1/CMP-9; changes routing, hooks, orchestration, or isolation availability | afforded | uninspected | SRC-2 docs/CONTROL_AVAILABILITY.md:15-46; SRC-1 pi/README.md:1-25 |
| RTE-12 | User mark/rescind → OBJ-14 current coverage recomputation → provenance finalizer → marker promotion/demotion or invalid-ledger stop | CMP-2/CMP-8; exact retained input changes a deterministic gate input | wired | uninspected | SRC-1 scripts/human_read_attestation_resolver.py:311-413; SRC-2 pipeline_orchestrator_agent.md:1008-1046 |
| RTE-13 | Inquiry event → OBJ-15 append/Passport binding → later replay/summary → checkpoint display or branch action | CMP-2/CMP-8; exact-pointer read-back is advisory and cannot satisfy a mandatory gate | wired | uninspected | SRC-1 scripts/inquiry_branch_ledger.py:1129-1190,1217-1275,2041-2201; SRC-2 pipeline_orchestrator_agent.md:225-268 |
| RTE-14 | Prior update fetch → OBJ-13 replacement → later SessionStart selection → optional update line in additionalContext | CMP-7/CMP-8; use-derived update state reaches the in-tree hook-output boundary | wired | uninspected | SRC-1 scripts/ars_update_check.sh:92-215, scripts/announce-ars-loaded.sh:49-142 |
| RTE-15 | Consent-bound claim/query/retrieval inputs → OBJ-16 retained artifacts → later replay/freshness comparison → bounded advisory or stale refusal | CMP-8; exact-artifact read-back is deterministic, while service/provider/human routes are external | wired | uninspected | SRC-1 scripts/build_claim_standing_candidate_ledger.py:928-1145, scripts/check_claim_standing_freshness.py:102-197 |

RTE-4, RTE-6, RTE-7, RTE-8, and RTE-9 are runtime route families. Their epistemically different functions are split under suffixed annotations in the epistemic lens; those suffixes do not mint parallel route IDs. RTE-12 through RTE-15 are registered routes, not suffixes, because their retained object, selection rule, and consumption effect are independently testable.

### Claims

| ID | Claimed operation | Claim source | Artifact-support conclusion status | Operation conclusion status | Bounded disposition |
|---|---|---|---|---|---|
| CLM-1 | Contract-audited end-to-end research, writing, review, revision, finalization, and auditable artifacts | SRC-2 academic-pipeline/SKILL.md:17-33 | wired | uninspected | Workflow and bounded deterministic subroutes ship; completion, truth, and bundle effect are unsupported |
| CLM-2 | Explicit confirmation after stages and non-skippable mandatory checkpoints | SRC-2 academic-pipeline/SKILL.md:27-31,142-193 | claimed | uninspected | Checkpoint occurrence, PASS progression, and initial FAIL correction are declared; persistent-FAIL retry and recovery are not determinable |
| CLM-3 | Coverage-bounded integrity/citation checks expose denominators and unknowns | SRC-2 academic-pipeline/SKILL.md:27-32; integrity_verification_agent.md:456-623 | wired | uninspected | Supported only for named formal/registered/sampled surfaces; not complete semantic or empirical truth |
| CLM-4 | Deterministic phase write-scope confinement for Bucket A agents | SRC-1 scripts/ars_phase_scope_manifest.json:1-31; SRC-2 docs/CONTROL_AVAILABILITY.md:35-46 | wired | uninspected | Holds for matched plugin-hook calls when the launcher and guard execute; not an all-channel or fail-closed invariant |
| CLM-5 | Resumable, auditable Material Passport state | SRC-2 academic-pipeline/references/passport_as_reset_boundary.md:17-125 | afforded | uninspected | Schemas and protocol exist, but no executable reset/resume transaction or context loader was found |
| CLM-6 | Optional external-model verification requires explicit per-session consent | SRC-2 shared/cross_model_verification.md:9-24 | wired | uninspected | Transport validation exists; consent remains a prompt/orchestrator condition rather than transport-local proof |
| CLM-7 | Human copilot boundary; no guarantee of actual procedures, raw-data authenticity, reproducibility, or result truth | SRC-2 POSITIONING.md:9-50 | claimed | uninspected | The artifact does not implement experiment execution or raw-data authentication; actual human control remains unobserved |

### Evidenced absences

| ID | Conclusion status | Searched boundary and evidence | Conclusion supported or prevented |
|---|---|---|---|
| ABS-1 | absent | Complete commit tree for Claude Code scheduler/model/context/tool-dispatch implementation; SRC-2 docs/CONTROL_AVAILABILITY.md:15-46 | Prevents end-to-end host and model conclusions |
| ABS-2 | absent | Frozen packet for a candidate-linked current-revision run or interventional comparison | Prevents observed and causally supported conclusions |
| ABS-3 | absent | Plugin code and control docs for coercive enforcement of prompt-only checkpoints; SRC-2 docs/CONTROL_AVAILABILITY.md:93-100 | Prevents treating checkpoint compliance as a runtime invariant |
| ABS-4 | absent | Claim-registry extraction/check path for deterministic semantic completeness; SRC-2 docs/ARCHITECTURE.md:109 | Prevents extending all registered claims to all substantive claims |
| ABS-5 | absent | Documented non-plugin channels for PreToolUse hook wiring; SRC-2 docs/CONTROL_AVAILABILITY.md:19-46 | Prevents cross-channel write-confinement claims |
| ABS-6 | absent | scripts, hooks, commands, and Pi adapter for executable Passport reset/resume writer, transaction, and context loader; SRC-2 passport_as_reset_boundary.md:120-125 | Prevents upgrading RTE-8 from protocol/affordance to wired or observed resume |
| ABS-7 | absent | SessionStart hook path for a Passport read; SRC-1 hooks/hooks.json:3-12 and scripts/announce-ars-loaded.sh:30-142 | Prevents treating SessionStart as workflow-state restoration |
| ABS-8 | absent | Closed citation transport request schema for a consent field or receipt; SRC-1 scripts/cross_model_codex_transport.py:249-267 | Prevents calling consent transport-enforced; it does not establish that consent is absent in practice |
| ABS-9 | absent | Adjudication state-machine/tracker/helper surfaces for any store or renderer delivery to Passport, handoff, Process Record, model, observer, gate, checkpoint, or transition | Prevents classifying OBJ-12 retention and human rendering as agent-memory activation |
| ABS-10 | absent | RTE-2 through RTE-10 for an evidence-consuming transition that accepts substantive manuscript or synthesis propositions as scientific truth | Prevents treating integrity PASS, editorial Accept, packaging, or user continuation as scientific-knowledge acceptance |
| ABS-11 | absent | Reviewer/cross-model prompt, provenance, and transport routes for evidence of statistically or causally independent error processes | Prevents treating agreement across seats or model families as independent corroboration |

### Behavioral-authority paths

| ID | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|
| BAP-1 | External host/model | Loaded skill, command, or SessionStart additionalContext | Binding instruction if consumed by the host | One invocation or session |
| BAP-2 | Worker/model call | Role prompt plus stage handoff | Binding instruction if dispatched | One call |
| BAP-3 | Orchestrator | User checkpoint, consent, branch, or override response | Permissive or branch-selecting operational authority | Next transition or current run |
| BAP-4 | Orchestrator/formatter | Integrity, review, or audit result | Revision-triggering or conditionally enforcing | Current candidate and gate |
| BAP-5 | Claude Code dispatcher | PreToolUse decision JSON | Enforcing deny for the matched call when the hook is honored | One tool call |
| BAP-6 | Later orchestrator | Passport/resume entry and referenced artifacts | Intended binding state/context input | Resumed stage/run |
| BAP-7 | Research/writing role | Source, provenance, or stage handoff | Advisory epistemic input | Current generation/check |
| BAP-8 | Integrity/review owner | Validated cross-model result | Advisory check input or reinvocation trigger | Current item/checkpoint |
| BAP-9 | Formatter | Terminal-policy marker | Enforcing under enabled strict policy; advisory under the default policy | Current package |
| BAP-10 | Resolver wrapper/verifier | Local SQLite cache lookup | Permissive substitution for a live resolver call | Row until TTL, invalidation, or incompatible version |
| BAP-11 | Pipeline orchestrator | Submission-verifier report and terminal token | Conditionally enforcing if the external orchestrator consumes it | Current package/policy/fingerprint |
| BAP-12 | Human operator | Deterministic adjudication-activity rendering | Advisory only; never a pipeline input | One rendered report |

Epistemic authority, operational authority, and these behavioral paths are not interchangeable.

## Runtime account

### Ordinary invocation

A user invokes /ars-full or an equivalent full-workflow trigger. CMP-1 selects CMP-2, which declares the stage sequence and versioned material identities. CMP-2 is the next-step owner; its natural-language policy chooses modes, dispatches CMP-3 through CMP-6, asks the user at checkpoints, and updates OBJ-5. The host is expected to assemble the selected skill/role prompt with OBJ-1 through OBJ-7, execute the model and tools, and return each artifact. That scheduling, context assembly, identity binding, cancellation, and actual effect dispatch belong to CMP-9 and remain uninspected.

State is current-conversation state plus user-workspace artifacts and, where used, OBJ-5. Deterministic clients add schemas, reducers, path decisions, hashes, and terminal tokens. External index responses and optional provider outputs cross RTE-6/RTE-7. Terminal output is OBJ-10. Recovery is declared through pause/redo, correction/recheck, version history, and optional Passport resume.

### Material alternate paths

RTE-10 directly invokes a research, writing, review, citation-check, rebuttal-audit, or conversion mode. These modes do not inherit a full-pipeline integrity or acceptance result; some explicitly prohibit Passport or ready-to-submit claims. RTE-11 changes the control envelope: skills-copy and repo-clone installs omit plugin-manifest hooks, Cowork lacks the designed Task-style coordination, Claude.ai Project use is read-only, Claude Science substitutes its own runtime, and Pi may run roles sequentially and has no Claude hooks. SRC-2 docs/CONTROL_AVAILABILITY.md:15-100 and SRC-1 pi/README.md:7-25.

### Forcing cases

1. **Persistent integrity failure.** All current surfaces agree that an initial FAIL triggers correction and re-verification. They disagree on the exhausted branch: the skill/state machine permit a recorded user decision after more than three rounds, including partially-unverified continuation, while the orchestrator prompt says Stage 2.5 cannot be overridden and Stage 4.5 aborts after its second failed check. Exact recovery is not determinable. SRC-2 academic-pipeline/SKILL.md:127-136; pipeline_state_machine.md:162-176,332-339; pipeline_orchestrator_agent.md:490-502.
2. **Out-of-scope or degraded write attempt.** A healthy plugin hook denies Bucket A Bash wholesale and structured writes outside the phase glob. Main/B/C/D roles are outside that fence; same-phase cross-skill collisions and one dual-phase union remain declared limits. Missing Python, timeout, malformed output, or launcher/guard failure passes through rather than locking out writes. SRC-1 scripts/ars_phase_scope_manifest.json:1-31 and hooks/run_guard.sh:14-28.
3. **Cross-session resume.** The prompt protocol requires an exact boundary hash, rejects mismatch/double use, warns on stale or unverified state, and specifies a stable sidecar lock. No executable in-tree reset/resume transaction or context loader was found, so actual recovery and concurrency behavior are uninspected. SRC-2 passport_as_reset_boundary.md:17-125.
4. **Optional external-model route.** Configuration without explicit session consent should skip transmission; transport failure degrades to the primary model; a successful but ungrounded citation check stays NOT_SEARCHED. Local request/result validation is wired, but consent occurrence and provider behavior are uninspected. SRC-2 shared/cross_model_verification.md:9-24; SRC-1 cross_model_codex_transport.py:249-267,935-953.

### Load-bearing guarantees

| Property | Owner and enforcement point | Guarantee strength | Covered and alternate paths | Required external contract | Artifact conclusion status | Operation conclusion status |
|---|---|---|---|---|---|---|
| Stage checkpoints and transitions | CMP-2 prompts at RTE-2/RTE-4 | participant protocol | Ordinary full pipeline; not a full-pipeline guarantee for RTE-10/RTE-11 | Host/model follows prompt and user supplies a response | claimed | uninspected |
| Integrity disposition | CMP-2/CMP-8 at RTE-4/RTE-6/RTE-9 | policy plus protocol | Named gates and enabled policies; direct modes/default-advisory paths differ | Host consumes results; services and model judgments are valid within scope | wired | uninspected |
| Phase write confinement | CMP-7/CMP-8 at PreToolUse RTE-5 | best effort overall; enforcing policy on a healthy matched call | Plugin hook, Bucket A, matched tools; not degraded/non-plugin/unfenced paths | Claude Code invokes hook and honors deny JSON | wired | uninspected |
| Passport resume | CMP-2 and schemas at RTE-8 | participant protocol | Opt-in FULL boundaries and explicit resume; no ordinary SessionStart restore | Host/model performs file, lock, hash, and context steps as instructed | claimed | uninspected |
| Cross-model consent | CMP-2/CMP-12 before RTE-7 dispatch | participant protocol | Configured optional calls only | Host asks, user answers, dispatcher withholds transmission on decline | claimed | uninspected |

### Dynamic-check preflight

No dynamic check planned. Static inspection establishes in-artifact wiring and conflict boundaries; executing this untrusted plugin would not establish excluded-host adherence or research quality without a separately designed, candidate-linked run.

## Lens scoping

### Memory/context scope

**Trigger evidence:** OBJ-5, OBJ-6, OBJ-11 through OBJ-16; RTE-1, RTE-6, RTE-8, RTE-12 through RTE-15; BAP-6, BAP-10, BAP-12. **Inspected boundary:** frozen plugin tree and its declared external host contract. **Depth:** full. The Passport, verification cache, update-check state, human-read and inquiry ledgers, claim-standing artifacts, and decision/activity records create distinct persistence and later-consumption paths, so a brief retained-state check would not separate executable read-back from static shipped context.

### Epistemic scope

**Trigger evidence:** OBJ-1 through OBJ-8 and OBJ-10; RTE-2 through RTE-10; CLM-1, CLM-3, CLM-6, CLM-7; BAP-3, BAP-4, BAP-7 through BAP-11. **Inspected boundary:** the same frozen tree, with host/model/services explicitly external. **Depth:** full. The system both generates truth-apt research/manuscript/review content and makes consequential, qualified warrant claims.

## Lens outputs

### Memory/context lens

The lens inventoried the Material Passport and reset_boundary protocol, citation-verification cache, update-check cache, prompt corpus, checkpoint/pending-decision state, and post-terminal adjudication-activity store.

| Record | Write side and read-back | Selection and delivery | Status separation | Limit |
|---|---|---|---|---|
| OBJ-5/RTE-8 | Mixed agent/human state maintenance; prior stage state is intended to return across invocations | Exact resume hash, current version, verification status, and referenced stage artifacts; receiver pull then orchestrator push | Context presence: claimed. Shipped wiring: claimed. Operation: uninspected. Activation: claimed. Causal effect: uninspected. | ABS-6 prevents an executable-resume claim; full transcript memory is not restored |
| OBJ-6/RTE-6/BAP-10 | Successful resolver outcomes are automatically cached; later calls read them | Exact citation/resolver/query-form/version key; one row per applicable resolver, 90-day semantic TTL | Context presence: claimed. Shipped wiring: wired. Operation: uninspected. Activation: wired. Causal effect: uninspected. | A cache hit can replace a network call, but no hit rate or scholarly effect was observed |
| OBJ-13/RTE-14 | A successful update fetch atomically replaces state; a later SessionStart can reuse it | `startup|clear`, matching installed version, valid grammar, and age under 24 hours select at most one `additionalContext` reminder | Hook-output presence: wired. Host/model context presence: uninspected. Operation: uninspected. Activation: uninspected. Causal effect: uninspected. | ABS-7: SessionStart does not read the Passport; external hook activation was not inspected |
| OBJ-14/RTE-12 | User mark/rescind events persist; the finalizer recomputes current coverage from the exact ledger | Exact ledger path, peer identity, event order, and current document hashes can promote, demote, or stop a marker | Deterministic input presence: wired. Host/model context presence: uninspected. Operation: uninspected. Activation: uninspected. Causal effect: uninspected. | Human attestation is operational input, not proof of reading or claim truth; finalizer activation was not observed |
| OBJ-15/RTE-13 | Inquiry events append to a digest-bound chain; later code replays the exact Passport pointer | Exact pointer, profile bytes, event chain, and checkpoint scope select an advisory summary or branch action | Deterministic read-back: wired. Model context presence: uninspected. Operation: uninspected. Activation: uninspected. Causal effect: uninspected. | Replay cannot alter an integrity verdict or satisfy a mandatory checkpoint; no host run was observed |
| OBJ-16/RTE-15 | Consent-, query-, candidate-, stance-, and freshness-bound artifacts can be replayed | Exact digests and authorized export scope select validation, freshness comparison, stale refusal, or bounded advisory | Deterministic read-back: wired. Provider/model context presence: uninspected. Operation: uninspected. Activation: uninspected. Causal effect: uninspected. | Search-bounded output is not consensus or verified truth; human/provider activation was not observed |
| OBJ-11 | Pending decision/override state may return through the Passport | Boundary hash and option value before resumed routing | Context presence: claimed. Shipped wiring: claimed. Operation: uninspected. Activation: claimed. Causal effect: uninspected. | Exact persistent-FAIL decision route is conflicted |
| OBJ-12/BAP-12 | Deterministic post-terminal store can be read by its renderer | Explicit path; last N eligible runs, default 10 and bounded 2–50 | Context presence for model/pipeline: absent. Renderer wiring: wired. Operation: uninspected. Activation on pipeline: inapplicable. Causal effect: inapplicable. | Explicitly excluded from model, gate, verdict, and transition inputs |
| OBJ-9 | Maintainer-authored static instructions are retained but not use-derived | Host command/skill/role routing | Context presence: claimed. Shipped wiring: afforded. Operation: uninspected. Activation as memory: inapplicable. Causal effect as memory: inapplicable. | Static installation material is not memory read-back |

The source-native mechanisms are exact-key, explicit-path, pointer, and digest-bound retrieval, not relevance search. Commonplace's read-back distinction fits the executable cache, ledger, update-state, and claim-standing routes and the intended Passport route because accumulated material returns to a later action; it does not fit the as-shipped prompt corpus. No source establishes external host/model context presence, behavioral activation by a model or human, token savings, protocol adherence, or causal research-quality effects.

**Legacy agent-memory review routing:** selected subject Academic Research Skills 3.21.1; detection not detected; evidence CMP-1 through CMP-6, RTE-2, and CLM-1; rationale: the primary offered work is academic research, writing, review, revision, and finalization, while persistence supports that workflow; publication authority not authorized; invocation disposition: not invoked because target not detected.

### Epistemic lens

The lens inventoried acquired sources and citation metadata; generated research, manuscript, review, integrity, and process claims; deterministic reducers and validators; operational dispositions; retention; and behavioral-authority paths.

| Route annotation | Function and content/update relation | Architectural status | Observed candidate state | Epistemic and operational authority | Evidence and limit |
|---|---|---|---|---|---|
| RTE-2/acquisition | Content transformation: truth-apt transformation: acquisition/import | doctrine only | no instance observed | Preserves only attributed source warrant to retrieval/lineage fidelity; supplies later work | SRC-2 deep-research/SKILL.md:150-200; live acquisition unobserved |
| RTE-2/generation | Content transformation: truth-apt transformation: ampliative conjecture | doctrine only | no instance observed | Produces candidate RQ, method, synthesis, and manuscript claims; no truth license | SRC-2 deep-research/agents/synthesis_agent.md:38-79 |
| RTE-3/dispatch | Operational admission/selection/consumption; no content change | doctrine only | no instance observed | Declares role/input scope; does not validate content | SRC-2 academic-paper/SKILL.md:195-233; external scheduler excluded |
| RTE-4/semantic-check | Check/evidence production: ampliative conjecture | doctrine only | no instance observed | Findings license only named registered/sampled surfaces; initial FAIL is revision-triggering | SRC-2 integrity_verification_agent.md:456-633; evaluator correctness and registry completeness unobserved |
| RTE-4/panel-recompute | Check/evidence production: entailed derivation | implemented | no instance observed | Validates derivation consistency from submitted structured judgments; can reject inconsistent synthesis | SRC-1 scripts/check_panel_synthesis.py:948-1016,1184-1198; does not validate judgments |
| RTE-4/disposition-correction-recovery | Disposition/acceptance plus indeterminate correction and no-content-change recovery | doctrine only | no instance observed | PASS admits only covered checks for the named next use; continuation, if permitted, adds no warrant | SRC-2 skill/state-machine/orchestrator conflict; exact persistent-FAIL effect not determinable |
| RTE-5/guard | Operational admission/selection/consumption; no content change | implemented | no candidate truth-apt output | No epistemic authority; per-call operational deny when healthy | SRC-1 ars_write_scope_guard.py:288-438; launcher fails open |
| RTE-6/resolver-reducer-cache | Acquisition/import, entailed derivation, retention, and freshness | implemented | no instance observed | Resolver outcomes warrant current index responses; reducer warrants only its three-class rule; cache age is applicability, not endorsement | SRC-1 verification_gate/__init__.py:192-291, citation_verification_summary.py:46-85, verification_cache.py:102-276 |
| RTE-7/consent-judgment-receipt | Policy admission, ampliative external judgment, and entailed receipt validation | doctrine only for consent/judgment; implemented for receipt validation | no instance observed | Consent permits transmission only; judgment is advisory; receipt licenses shape/event binding, not correctness | SRC-2 shared/cross_model_verification.md:9-24; SRC-1 cross_model_codex_transport.py:935-953 |
| RTE-8/retention-resume | Retention plus lineage/recovery; no truth upgrade | doctrine only | no instance observed | Intended byte/lineage and later-context authority, not event truth | SRC-2 passport_as_reset_boundary.md:17-125; ABS-6 |
| RTE-9/format-package-disposition | Indeterminate formatting, entailed package checks, and policy disposition | doctrine only for formatting/consumption; implemented for package checks | no instance observed | Checks license enumerated package conditions; default citation existence is advisory, strict policy can emit a block token | SRC-2 docs/ARCHITECTURE.md:109-112; final host consumption unobserved |
| RTE-10/direct modes | Ampliative generation or mode-local checking | doctrine only | no instance observed | Local mode scope only; no full-pipeline acceptance or ready-to-submit license | SRC-2 academic-paper/SKILL.md:290-357 |
| RTE-12/human-read-ledger | Operational admission and selection; no truth-apt content upgrade | implemented for append/rescind/recompute; external for the human event and finalizer consumption | no instance observed | Current coverage may promote, demote, or stop a marker; user attestation supplies operational authority, not epistemic evidence of reading or truth | SRC-1 scripts/human_read_attestation_resolver.py:311-413; host/human activation unobserved |
| RTE-13/inquiry-ledger-replay | Non-truth-apt state and branch replay | implemented for ledger validation/replay; doctrine only for checkpoint consumption | no instance observed | Exact-pointer replay can inform an advisory branch action but cannot accept a claim, alter an integrity verdict, or satisfy a mandatory checkpoint | SRC-1 scripts/inquiry_branch_ledger.py:1129-1190; SRC-2 pipeline_orchestrator_agent.md:225-268 |
| RTE-14/update-state-reuse | Acquisition/import of version status, replacement retention, and operational delivery | implemented to hook-output boundary | no instance observed | A fresh status can license an update reminder only; it supplies no scholarly warrant | SRC-1 scripts/ars_update_check.sh:92-215, scripts/announce-ars-loaded.sh:49-142 |
| RTE-15/claim-standing-replay | Acquisition, deterministic retention/freshness comparison, and optional ampliative stance | implemented for bounded records/checks; external for services, provider, human, and later host use | no instance observed | Exact-artifact currentness licenses only a bounded advisory or stale refusal; it is not scientific consensus, verified truth, or knowledge acceptance | SRC-1 scripts/check_claim_standing_freshness.py:102-197 |

Per-object lifecycle disposition is:

| Object | Transformation and lifecycle | Architectural status | Observed candidate state | Missing evidence or warrant limit |
|---|---|---|---|---|
| OBJ-1 | Acquisition/import for attributed sources; configuration is non-truth-apt policy input | doctrine only | no instance observed | Authenticity and truth unknown |
| OBJ-2 | Bibliography facet: acquisition/import and non-ampliative reshaping. RQ/method/synthesis facets: ampliative conjecture through observation, generation, checking, intended acceptance, and later use | doctrine only, with implemented citation subchecks | no instance observed for every phase | No candidate lineage or disposition; deduplication/formatting does not improve source warrant |
| OBJ-3 | Ampliative manuscript conjecture; model correction is indeterminate until rechecked | doctrine only, with implemented byte/patch subchecks | no instance observed for every phase | No draft, check, acceptance, or integration trace; operational continuation is not acceptance |
| OBJ-4 | Review judgments are ampliative conjectures; contract-derived decision is entailed only from submitted judgments | doctrine only for judgments; implemented for recomputation | no instance observed for every phase | Role separation is not independent error and recomputation is not reviewer correctness |
| OBJ-5 | Non-ampliative state/lineage reshaping | doctrine only for resume | no instance observed | Hashes can bind bytes, not event authenticity or truth |
| OBJ-6 | Resolver responses are acquired; three-class summary is entailed from them; cache retains without acceptance | implemented | no instance observed | Index coverage and claim support remain outside the summary |
| OBJ-7 | Claim registry transformation is indeterminate; integrity judgments are ampliative and coverage-bounded | doctrine only, with implemented bounded structural checks | no instance observed for every phase | Semantic extraction completeness absent |
| OBJ-8 | External judgment is ampliative; request/receipt derivation is entailed within its schema | doctrine only for judgment; implemented for validation | no instance observed for every phase | Different provider/model does not establish independent errors |
| OBJ-9 | No run-produced candidate truth-apt output; direct behavioral adaptation only | implemented/declared surfaces | no candidate lifecycle record | Presence does not establish host obedience |
| OBJ-10 | Submission formatting is indeterminate; process-record evaluations are ampliative | doctrine only, with implemented package subchecks | no instance observed for every phase | Semantic preservation and causal collaboration claims unobserved |
| OBJ-11/OBJ-12 | Choices are non-truth-apt policy; receipts record attributed events non-ampliatively within authentication limits | doctrine only for pipeline receipt; implemented for post-terminal store | no instance observed | Event byte binding does not authenticate actor or add scientific warrant |
| OBJ-13 | Acquired version status is retained by replacement and later selected by freshness/version predicates | implemented to hook-output boundary | no instance observed | Currentness licenses an update reminder, not truth or model activation |
| OBJ-14/OBJ-15 | Attributed human-read and inquiry events are retained and replayed non-ampliatively; deterministic reducers derive current operational state | implemented for ledger operations; external/doctrine only for participant and host consumption | no instance observed | Hashes and attestations bind declared events but do not authenticate reading, establish truth, or accept knowledge |
| OBJ-16 | Search inputs/results are acquired; closed artifacts and freshness are entailed; an optional stance is ampliative | implemented for artifact construction/replay; external for services/provider/human | no instance observed | Search-bounded currentness does not warrant consensus, novelty, or substantive truth |

Claim comparison preserves these bounds: CLM-1 has shipped prompt and deterministic subroutes but no completed run; CLM-2 has a same-revision persistent-FAIL conflict; CLM-3 is supported only for declared formal and sampled populations; CLM-4 is conditional on the healthy plugin path; CLM-5 remains protocol plus affordance; CLM-6 has a wired transport but prompt-level consent; CLM-7 is a supported scope boundary, not proof that a human controlled an actual run.

## Reconciliation

Both fresh P1 workers echoed the exact run, lens, packet, revision, source-register, canonical-register, and runtime-baseline digest. Their packet and return digests matched, all cited evidence stayed inside the frozen commit, neither requested a targeted read, and neither made a publication decision. No correction packet was needed.

The memory proposals registered four separately testable retained objects and routes: MEM-1 through MEM-4 became OBJ-13 through OBJ-16; MEM-5 through MEM-8 became RTE-12 through RTE-15; and MEM-9 became ABS-9. The epistemic absence proposals EPI-ABS-1 and EPI-ABS-2 became ABS-10 and ABS-11. Those additions were already within SRCREG-v1 and advanced the post-reconciliation register to CANON-v2 without invalidating either P1 packet. Functional annotations on existing routes remain suffixes rather than parallel route identities.

Independent convergence occurred on four findings: deterministic subroutes license only their closed inputs and rules; the Passport is a detailed prompt/schema protocol without an executable in-tree general resume loader; exact retained inputs have several executable read-back routes but no candidate-linked activation evidence; and multi-seat or cross-model agreement does not establish independent errors.

The anchored conflict is preserved rather than resolved by precedence. SRC-2 academic-pipeline/SKILL.md:127-136, pipeline_state_machine.md:162-176,332-339, and docs/ARCHITECTURE.md:261 permit a three-round/user-decision recovery; pipeline_orchestrator_agent.md:498-500 forbids a Stage 2.5 override and aborts Stage 4.5 after the second failure. The common conclusion is only that PASS permits ordinary progression and an initial FAIL triggers correction/recheck. Exact exhausted recovery is not determinable.

Cross-lens ownership checks passed: the runtime account owns endpoints and progression; the memory lens owns persistence, selection, read-back, context-presence, and activation distinctions; the epistemic lens owns transformations, checks, warrant, acceptance, integration, and epistemic/operational authority. No curation label was used as warrant, and no behavioral path was treated as epistemic authority. Legacy review projection is inapplicable because detection was not detected and no legacy review was invoked.

The compact projection had material drift only in its persistence account: it named the Passport and citation cache but omitted the additional executable human-read, inquiry-ledger, update-state, and claim-standing read-back routes. The compact artifact was updated economically and linked back to this retained result; the rest of its system account did not require replacement.

## Bounded synthesis

**Evidence basis:** inspected natural-language programs, manifests, hooks, scripts, and schemas at one commit; no deployed run or causal comparison.

ARS is a prompt-defined academic workflow with a substantial deterministic support layer. The ordinary progression is user entry, research artifacts, manuscript generation, integrity checking, simulated editorial review, revision, rechecking, formatting, and a process record. Claude Code and its model perform the material scheduling and semantic work outside this artifact; the plugin contributes discoverable prompts, state and handoff contracts, optional transports, and several checkers that can constrain artifacts or emit operational decisions.

The most discriminating mechanism is the split between prompt protocols and executable subchecks. Panel arithmetic, citation-outcome reduction, cache selection, write-path decisions, receipt validation, and package predicates have inspectable symbolic semantics. Research synthesis, manuscript writing, semantic claim extraction, review judgment, user checkpoints, Passport resume, and terminal consumption remain model/host protocols. Calling the whole system “contract-audited” is supportable only if “contract” is read at this mixed grain.

Persistence has the same mixed grain. Besides citation-cache reuse, the tree wires deterministic replay for a human-read ledger, an inquiry branch ledger, update-check state, and claim-standing artifacts. These routes use exact paths, keys, pointers, or digests and can change a reducer result, advisory, stale refusal, or hook output. They do not establish that the external host delivered the result, that a model or human used it, or that scholarship improved. Human-read attestation in particular is an attributed operational input, not evidence that reading occurred or that any claim is true.

For supervised manuscript/process QA in the healthy Claude Code plugin channel, the artifact supplies useful stage boundaries, visible denominators, lineage records, and narrow fail/block signals. Responsibilities for actual scholarship are deliberately externalized to the researcher, source services, raw-data/experiment systems, and the host. That is a declared boundary, not a missing runtime feature. The main tradeoff is that assurance varies by install channel, entry mode, optional policy, and whether a control is code or prompt.

Two implications need qualification. First, VERIFIED_ONLY is a stage-output label for named checks, not a claim that every substantive statement, experiment, or data point is verified; final registered-claim coverage still cannot establish registry completeness. Second, citation existence is advisory by default and metadata existence is not claim support. Strict policy can emit blocking markers, but actual blocking still depends on the external orchestrator.

The same-revision integrity-recovery conflict is a gap relative to a uniform mandatory-gate claim. It does not erase the initial FAIL/correction route, but it prevents one exact account of retry count, override availability, and terminal behavior. Direct modes and non-plugin channels further prevent full-pipeline guarantees from transferring automatically.

Evidence that would change this assessment includes: a candidate-linked host trace showing prompt/context/tool/result/state transitions; an executable, tested Passport transaction and loader or an observed locked resume trace; removal of the persistent-FAIL contradiction; a complete-population semantic claim audit with an independently justified evaluator; live service evidence tied to exact candidates; and an interventional comparison that varies one component before attributing outcome effects.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| External host/model/runtime uninspected | CMP-9, RTE-1 through RTE-4, RTE-8 through RTE-11, ABS-1 | Commit tree and host-contract docs | Actual scheduling, prompt/context delivery, model adherence, and enforcement | Candidate-linked Claude Code execution trace and relevant host implementation/contract |
| No observed run or causal comparison | ABS-2, all operation and causal fields | Frozen sources | Observed candidate states, activation, outcome quality, and component effects | Retained exact run evidence; controlled intervention/comparison for causality |
| External services and empirical world excluded | CMP-10/CMP-11, RTE-6/RTE-7, CLM-3/CLM-6/CLM-7 | In-tree clients and docs | Live lookup correctness, independent judgment, procedures, data authenticity, reproducibility, and truth | Candidate-linked service results and external empirical/reproducibility evidence |
| Persistent-FAIL doctrine conflicts | RTE-4, CLM-2, CLM-3, OBJ-3/OBJ-7/OBJ-11 | Four same-revision source surfaces | Exact retry cap, override availability, and terminal recovery | One authoritative transition contract with other shipped surfaces brought into conformance |
| Semantic claim extraction is model-mediated and completeness is absent | ABS-4, OBJ-7, RTE-4, CLM-3 | Integrity prompts and bounded checkers | “All registered claims” becoming “all substantive claims” | Independently warranted complete-population evaluation |
| Control availability varies by channel, mode, flag, and launcher health | RTE-5, RTE-9 through RTE-11, CLM-4 | Plugin and alternate-channel implementation/docs | Universal confinement, orchestration, or terminal-block claims | Deployment-specific evidence for a named channel/configuration |
| Other optional audit extensions were not exhaustively traced | CMP-8 and non-material optional modes outside RTE-12 through RTE-15 | Only extensions needed for the declared question | Claims about every optional audit/mode | A separately scoped feature analysis |

## Verification and blockers

### Semantic verification

Passed. One run ID, boundary, revision, source register, target class, and evidence tier are used throughout. Canonical IDs resolve, P1 proposal mappings are recorded, and the reconciled CANON-v2 advance is distinguished from a correction. Conclusion-status fields use only absent, inapplicable, uninspected, claimed, afforded, wired, observed, or causally supported; `implemented` appears only as epistemic architectural status. Ordinary, alternate, and four forcing routes are covered. Guarantee owner, enforcement point, strength, paths, and external contract are explicit. Both fresh full lenses ran and their exact headers and baselines matched; no correction packet was required. Retention is not read-back; context presence is not activation; operation is not causality; curation/use is not warrant/acceptance; and operational continuation is not PASS. No source-native mechanism was replaced by Commonplace vocabulary.

### Deterministic validation

The decisive acceptance command is `commonplace-validate --json kb/reports/retained/agentic-system-analysis-operability-replay-20260903/AAS-2026-09-03-academic-research-skills-02.md` from the Commonplace repository root. Acceptance requires JSON schema version 1, `status: success`, `files_analysed: 1`, and exactly one `analysed_artifacts` entry for that relative path with normalized type `agentic-system-analysis-result`, zero warnings, and zero failures. The unchanged JSON receipt is retained with the replay evidence.

### Blockers

none
