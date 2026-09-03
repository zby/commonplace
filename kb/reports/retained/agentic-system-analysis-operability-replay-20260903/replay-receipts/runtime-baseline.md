# Runtime baseline — AAS-2026-09-03-academic-research-skills-02

## Packet identity

- Run: `AAS-2026-09-03-academic-research-skills-02`
- System: Academic Research Skills 3.21.1
- Reviewed boundary: commit
  `94436237913091d4739870159d241660527e8338`
- Analysis cutoff: 2026-09-03
- Source register: `SRCREG-v1-94436237913091d4739870159d241660527e8338`
- Canonical register: `CANON-v1-94436237913091d4739870159d241660527e8338`
- Frozen root:
  `/tmp/aas-ars-replay-EWuw3w/academic-research-skills-94436237913091d4739870159d241660527e8338`
- Evidence tier: code-grounded for the complete artifact; no observed run or
  causal experiment

## Boundary

Academic Research Skills is an extension or tool mechanism: a complete
independently distributed Claude Code plugin and prompt workflow whose material
loop crosses the external Claude Code host, model, researcher, project
workspace, scholarly services, and optional model providers. The boundary kind
is `complete artifact, partial loop`.

Included are the four skills, sixteen command entry files, skill-local and
plugin-exposed role prompts, plugin manifests and hooks, deterministic scripts
and schemas, the ordinary ten-stage workflow, direct-mode and alternate-install
routes, the Material Passport, ledgers and caches, citation and package checks,
and optional cross-model transport. The plugin manifest claims 39 prompt roles;
the frozen tree contains 38 skill-local agent prompt files plus three
plugin-exposed prompt files that duplicate role identities. This inventory
distinction does not change a runtime conclusion.

Excluded participants and prevented conclusions:

| Excluded participant | Conclusion prevented |
|---|---|
| Claude Code runtime, model, scheduler, context builder, and dispatcher | Whether prompts or hook output reached a model, roles ran as declared, or the host enforced returned decisions |
| Human researcher and a real project workspace | Whether checkpoints, consent, overrides, source choices, or manuscript decisions occurred |
| Crossref, OpenAlex, Semantic Scholar, arXiv, and optional model providers | Whether a live lookup or second-model check returned correct evidence |
| Experiments, raw data, institutions, and reproducibility systems | Whether reported procedures occurred, data are authentic, analyses reproduce, or manuscript claims are true |

## Source register

| ID | Layer | Identity and inspected scope | Anchors and gaps |
|---|---|---|---|
| SRC-1 | implementation | Commit-pinned extracted tree; plugin metadata, hooks, Python/shell implementations, contracts, Pi adapter, and targeted tests | `.claude-plugin/plugin.json`; `hooks/hooks.json`; `hooks/run_guard.sh`; `scripts/ars_write_scope_guard.py`; `scripts/verification_gate/__init__.py`; `scripts/verification_cache.py`; `scripts/cross_model_codex_transport.py`. External host and services are unavailable, preventing end-to-end and service-result conclusions. |
| SRC-2 | doctrine/design | Same tree; README, POSITIONING, architecture/control/data-flow docs, skill bodies, role prompts, state machine, Passport protocol, and integrity protocol | `academic-pipeline/SKILL.md`; `academic-pipeline/agents/pipeline_orchestrator_agent.md`; `academic-pipeline/references/pipeline_state_machine.md`; `academic-pipeline/references/passport_as_reset_boundary.md`; `docs/ARCHITECTURE.md`; `docs/CONTROL_AVAILABILITY.md`; `docs/DATA_FLOWS.md`; `POSITIONING.md`. Doctrine cannot prove host adherence or operation; same-revision persistent-FAIL sources conflict. |

Archive identity: 12,341,902 bytes; SHA-256
`e298af69dc06ffb6642e5a64141954f3b4169e793626db907bedb0decd22d08c`.
No dynamic probe is planned: executing the untrusted plugin would not establish
excluded-host adherence or research quality without a separately designed,
candidate-linked run.

## Canonical components

| ID | Source-native component | Generic identity, form, substrate, and baseline status |
|---|---|---|
| CMP-1 | Plugin package and entry surface | JSON manifests plus natural-language slash-command and skill entry files in Git; package/command wiring is `wired`. |
| CMP-2 | `academic-pipeline` lightweight orchestrator | Natural-language system-definition file; shipped entry is `wired`, host operation `uninspected`. |
| CMP-3 | `deep-research` skill | Natural-language prompts, references, templates, and contracts; shipped skill `wired`, operation `uninspected`. |
| CMP-4 | `academic-paper` skill | Natural-language prompts plus symbolic patch/validation contracts; shipped skill `wired`, operation `uninspected`. |
| CMP-5 | `academic-paper-reviewer` skill | Natural-language panel prompts plus structured review contracts; shipped skill `wired`, operation `uninspected`. |
| CMP-6 | Role prompt corpus and three plugin-exposed agents | Natural-language Markdown in Git; dispatch `claimed`, operation `uninspected`. |
| CMP-7 | SessionStart and PreToolUse hook layer | JSON configuration and shell launchers; plugin-channel wiring `wired`, operation `uninspected`. |
| CMP-8 | Deterministic scripts, reducers, validators, and schemas | Python, shell, JSON Schema, JSON, and YAML; material subroutes `wired`, operation `uninspected`. |
| CMP-9 | Claude Code host, model, scheduler, context builder, and dispatcher | External software and distributed-parametric model; `uninspected`. |
| CMP-10 | Bibliographic index services | External services and records; `uninspected`. |
| CMP-11 | Optional cross-model provider and local transport | External model/service plus in-tree Python transport; transport `wired`, provider operation `uninspected`. |
| CMP-12 | Human researcher and principal | External actor; `uninspected`. |

## Canonical operative objects

| ID | Source-native object | Generic identity, form, and substrate |
|---|---|---|
| OBJ-1 | User request, configuration, and source material | Mixed natural-language/structured input in host conversation and workspace. |
| OBJ-2 | Bibliography/corpus, RQ brief, methodology blueprint, and synthesis family | Mixed artifacts in workspace and Material Passport references. |
| OBJ-3 | Versioned manuscript, draft, revision, and final-paper family | Natural-language plus structured markers in workspace files and Passport references. |
| OBJ-4 | Review cards/reports, editorial decision, and revision roadmap | Mixed judgments and derived decisions in workspace artifacts and Passport. |
| OBJ-5 | Pipeline state, Material Passport, and append-only ledgers | YAML/JSON and paths in user-named project files. |
| OBJ-6 | Citation records, resolver outcomes, verification summaries, and cache rows | Structured records in project artifacts and local SQLite cache. |
| OBJ-7 | Claim registry, provenance records, integrity findings, and verdicts | Mixed structured records and natural-language judgments in project artifacts and Passport. |
| OBJ-8 | Cross-model request, judgment, event stream, and validated receipt | JSON plus model-produced truth-apt judgment in ephemeral transport/project outputs. |
| OBJ-9 | Shipped skill, role, command, and contract corpus | Natural-language and symbolic system-definition artifacts in Git/plugin installation. |
| OBJ-10 | Final submission package and process record | Mixed Markdown, LaTeX, PDF, markers, and model assessment in workspace. |
| OBJ-11 | Checkpoint branch choices, pending decisions, and override receipts | Structured values and attributed natural language in Passport/run-local sidecars. |
| OBJ-12 | Post-terminal adjudication-activity records and store | Canonical JSON and deterministic rendering in an explicit caller-selected file; excluded from model, checkpoint, gate, verdict, and transition inputs. |

## Canonical routes

| ID | Endpoints and progression | Owner and baseline status |
|---|---|---|
| RTE-1 | Plugin install/command → SessionStart or command material → external host/model | CMP-1/CMP-7; wiring `wired`, operation `uninspected`. |
| RTE-2 | User entry → research → writing → integrity → review → revision → final integrity → finalization/process record | CMP-2; prompt policy selects stages and artifacts; wiring `wired`, operation `uninspected`. |
| RTE-3 | Orchestrator/subskill → role prompt and artifacts → model/worker → returned artifact | CMP-2–CMP-6; context/dispatch `claimed`, operation `uninspected`. |
| RTE-4 | Candidate/report/user choice → semantic or deterministic check, checkpoint, correction, or recovery → next state | CMP-2/CMP-4/CMP-5/CMP-8/CMP-12; progression `claimed`, operation `uninspected`; persistent-FAIL conflict applies. |
| RTE-5 | Matched tool call → PreToolUse launcher/guard → Claude Code dispatcher | CMP-7/CMP-8; matched plugin route `wired`, operation `uninspected`; degraded launcher fails open. |
| RTE-6 | Citation → live/cached resolver outcomes → deterministic summary → integrity/terminal policy | CMP-8/CMP-10; `wired`, operation `uninspected`. |
| RTE-7 | Configured route and user consent → model request → validated receipt/judgment → original owner | CMP-2/CMP-8/CMP-11/CMP-12; transport `wired`, operation `uninspected`. |
| RTE-8 | Completed stage → Passport boundary/ledger → explicit resume hash/path → later orchestrator/stage | CMP-2/CMP-8/CMP-12; protocol/affordance `claimed`, operation `uninspected`. |
| RTE-9 | Checked draft → formatter/package checks/terminal policy → submission package or remediation | CMP-2/CMP-4/CMP-8; progression `claimed`, deterministic subchecks `wired`, operation `uninspected`. |
| RTE-10 | User → direct single-skill generation/check mode → local output | CMP-1/CMP-3/CMP-4/CMP-5; `wired`, operation `uninspected`; bypasses full-pipeline acceptance. |
| RTE-11 | Skills copy, repo clone, Cowork, Claude Science, or Pi → alternate host behavior | CMP-1/CMP-9; available route `afforded`, operation `uninspected`; control envelope varies. |

## Canonical claims

| ID | Claimed operation and baseline disposition |
|---|---|
| CLM-1 | Contract-audited end-to-end research/writing/review/finalization. Shipped prompt and deterministic subroutes are `wired`; operation is `uninspected`. |
| CLM-2 | Explicit confirmation and mandatory checkpoints. Occurrence is `claimed`; exact persistent-FAIL retry/recovery is not determinable. |
| CLM-3 | Coverage-bounded integrity/citation checks expose denominators and unknowns. Named subchecks are `wired`; complete semantic truth is not established. |
| CLM-4 | Deterministic phase write-scope confinement for Bucket A agents. Matched healthy plugin route is `wired`; not an all-channel/fail-closed invariant. |
| CLM-5 | Resumable, auditable Material Passport state. Schemas/protocol are `afforded`; executable resume wiring was not found. |
| CLM-6 | Optional model verification requires per-session consent. Transport is `wired`; consent is a prompt/orchestrator protocol. |
| CLM-7 | Human copilot boundary and no guarantee of procedures, data authenticity, reproducibility, or truth. Boundary is `claimed`; actual human control is `uninspected`. |

## Canonical evidenced absences

| ID | Status, searched boundary, and prevented conclusion |
|---|---|
| ABS-1 | `absent` from the commit tree: Claude Code scheduler/model/context/tool-dispatch implementation; prevents end-to-end host/model conclusions. |
| ABS-2 | `absent` from supplied evidence: candidate-linked run or intervention; prevents `observed` and `causally supported` conclusions. |
| ABS-3 | `absent` from plugin code/control docs: coercive enforcement of prompt-only checkpoints; prevents runtime-invariant claims. |
| ABS-4 | `absent` from claim-registry check paths: deterministic semantic completeness; prevents generalizing registered-claim coverage to all substantive claims. |
| ABS-5 | `absent` from non-plugin channels: PreToolUse hook wiring; prevents cross-channel confinement claims. |
| ABS-6 | `absent` from scripts/hooks/commands/Pi adapter: executable Passport reset/resume transaction and context loader; prevents `wired` or observed resume. |
| ABS-7 | `absent` from SessionStart: Passport read; prevents treating SessionStart as state restoration. |
| ABS-8 | `absent` from the closed cross-model transport schema: consent field/receipt; prevents transport-enforced consent. |

## Canonical behavioral-authority paths

| ID | Consumer; channel; force; horizon |
|---|---|
| BAP-1 | Host/model; skill/command/SessionStart context; binding if consumed; invocation/session. |
| BAP-2 | Worker/model; role prompt and handoff; binding if dispatched; one call. |
| BAP-3 | Orchestrator; user checkpoint/consent/branch/override; permissive or branch-selecting; next transition/run. |
| BAP-4 | Orchestrator/formatter; integrity/review/audit result; revision-triggering or conditional; candidate/gate. |
| BAP-5 | Claude Code dispatcher; PreToolUse decision JSON; enforcing deny if honored; one call. |
| BAP-6 | Later orchestrator; Passport/resume entry and artifacts; intended binding state/context; resumed stage/run. |
| BAP-7 | Research/writing role; sources/provenance/handoff; advisory epistemic input; current generation/check. |
| BAP-8 | Integrity/review owner; validated cross-model result; advisory or reinvocation trigger; item/checkpoint. |
| BAP-9 | Formatter; terminal-policy marker; enforcing under strict policy, advisory by default; package. |
| BAP-10 | Resolver/verifier; SQLite cache hit; permissive substitution; row TTL/version horizon. |
| BAP-11 | Orchestrator; submission-verifier report/token; conditional if consumed; package/policy/fingerprint. |
| BAP-12 | Human operator; adjudication-activity rendering; advisory only and never pipeline input; report. |

## Runtime account

The ordinary route is user invocation of `/ars-full` or the equivalent skill
trigger, followed by CMP-2's natural-language ten-stage policy. The external
host must assemble prompts and artifacts, schedule models/tools, return outputs,
and enforce decisions. Workspace files and OBJ-5 carry state. Deterministic
clients add schemas, reducers, path decisions, hashes, and terminal tokens.
Terminal output is OBJ-10. Recovery is declared through correction/recheck,
pause/redo, version history, and optional Passport resume.

Material alternate routes are RTE-10 direct modes and RTE-11 install/host
channels. They do not inherit the same hook, orchestration, or acceptance
surface. `docs/CONTROL_AVAILABILITY.md:15-104` explicitly distinguishes plugin,
skills copy, repo clone, Cowork, claude.ai Project, Claude Science, and Pi.

Forcing cases:

1. Persistent integrity failure. `academic-pipeline/SKILL.md:127-136`,
   `pipeline_state_machine.md:162-176,332-339`, and
   `docs/ARCHITECTURE.md:261` permit three correction rounds and a recorded
   user decision, including partially unverified continuation. The orchestrator
   prompt at `pipeline_orchestrator_agent.md:498-500` says Stage 2.5 cannot be
   skipped/overridden and Stage 4.5 aborts after the second failed check. No
   precedence rule was found. Only initial FAIL → correction/recheck and PASS →
   progression are determinate.
2. Degraded write guard. A healthy matched plugin hook can deny named Bucket A
   calls, while missing/broken Python, timeout, malformed output, or launcher
   failure produces pass-through. Other role buckets and channels are outside
   that fence.
3. Cross-session resume. The Passport protocol specifies exact hashes,
   append-only entries, double-use checks, and a sidecar lock, but states at
   `passport_as_reset_boundary.md:120-125` that it adds no runtime CLI tooling.
4. Optional external-model route. Configuration plus prompt-level session
   consent is required; transport validation is executable, but live consent,
   provider behavior, and judgment quality are uninspected.

Load-bearing guarantees:

| Property | Owner/enforcement | Strength | Covered paths and external contract |
|---|---|---|---|
| Stage checkpoints/transitions | CMP-2 prompt policy at RTE-2/RTE-4 | participant protocol; `claimed`/operation `uninspected` | Full pipeline only; requires host/model adherence and user response. |
| Integrity disposition | CMP-2/CMP-8 at RTE-4/RTE-6/RTE-9 | policy plus protocol; subchecks `wired`/operation `uninspected` | Named gates/policies; host must consume results and services/judgments must be valid in scope. |
| Phase write confinement | CMP-7/CMP-8 at RTE-5 | best effort overall; enforcing policy for a healthy matched call | Plugin/Bucket A/matched tools; host must invoke hook and honor deny JSON. |
| Passport resume | CMP-2 plus schemas at RTE-8 | participant protocol; `claimed`/operation `uninspected` | Opt-in boundaries and explicit resume; host/model must perform file/lock/hash/context protocol. |
| Cross-model consent | CMP-2/CMP-12 before RTE-7 | participant protocol; `claimed`/operation `uninspected` | Configured optional calls; host must ask and dispatcher must withhold on decline. |

## Lens scoping inputs

Memory/context trigger evidence: OBJ-5, OBJ-6, OBJ-11, OBJ-12; RTE-1, RTE-6,
RTE-8; BAP-6, BAP-10, BAP-12. Full depth is warranted because the Passport,
verification/update caches, and decision/activity ledgers have distinct
persistence and later-consumption routes.

Epistemic trigger evidence: OBJ-1–OBJ-8, OBJ-10; RTE-2–RTE-10; CLM-1, CLM-3,
CLM-6, CLM-7; BAP-3, BAP-4, BAP-7–BAP-11. Full depth is warranted because the
system generates truth-apt research/manuscript/review content and makes
consequential but qualified warrant claims.

Legacy agent-memory review detection: not detected. The selected system's
primary offered work is research, writing, review, revision, and finalization;
persistence supports that workflow rather than constituting its primary
memory/context product. No legacy review is invoked.

## Worker return contract

Each lens returns a sparse overlay on these IDs. Accepted top-level blocks are
canonical-ID annotations, lens-local new-record proposals, corrections or
amendments, evidenced absences, evidence limitations/targeted-read requests,
and the lens summary. A return must preserve source-native mechanisms,
conclusion statuses, separate authority kinds, and prevented conclusions. It
must not reacquire sources, change the boundary, mint canonical IDs, publish,
or delegate.
