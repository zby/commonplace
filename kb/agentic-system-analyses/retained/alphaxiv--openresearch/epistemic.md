---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenResearch epistemic routes: imported literature, measured-run evidence, instructed interpretation, experiment promotion and ungated retention."
run-id: AAS-2026-10-20-openresearch-62725ad1cd0a-01
reviewed-boundary: "2c45ff3183b494aac4001bd44eefbe57a3c249ae"
---

# OpenResearch epistemic report

## Source-and-claim boundary

This report asks how OpenResearch turns literature and experiment output into claims and consequential research decisions. Scope, exclusions and frozen evidence identity are see [boundary](boundary.md#boundary-and-evidence); evidence registration is see [Source register](boundary.md#source-register). All additional inspection uses SRC-1 at that revision. Implementation supports possible routes, not executed research or model compliance. No target was executed.

The public research-assistance assignment is see [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance). More specific warrant and iteration prescriptions are see [EPI-CLM-results-evidence](#epi-clm-results-evidence) and [EPI-CLM-experiment-loop](#epi-clm-experiment-loop). These are instructions, not claims that every output has already been validated.

| Entry point or operation | Source path | Coverage and conclusion limit |
| --- | --- | --- |
| CLI commands, hidden hooks and permission tool | SRC-1 `src/main.rs`; `src/commands/invocation_gate.rs`; `src/commands/mcp_gate.rs` | Direct enum/dispatch searches and hook reads; permission policy see [RT-RTE-permission-review](runtime.md#rt-rte-permission-review). Invocation hook adds model identity to Bash, not scientific validation. MCP exposes approval, not a truth oracle. Full alternate harness hook parity unassessed. |
| Chat/model interpretation, recovery and user shell | SRC-1 `src/local/chat/mod.rs`; `src/local/harness/claude.rs` | Supplied findings see [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-user-shell](runtime.md#rt-rte-user-shell). No fresh direct reconstruction of all adapters; native reasoning and provider internals unavailable. Prevents claims of reliable interpretation or complete context preservation. |
| Literature discovery and paper reading | SRC-1 `src/commands/discover.rs`; `src/commands/paper.rs`; `src/client.rs`; `agent-skills/orx-lit-review/SKILL.md` | Direct command files, client markdown fetch, LitHit/OpenAlex representation and reconstruction, and complete skill; see [EPI-RTE-literature-import](#epi-rte-literature-import), [EPI-RTE-abstract-reshape](#epi-rte-abstract-reshape). Server ranking, embedding internals, full PubMed/bioRxiv parsing and corpus reliability unassessed. |
| Experiment launch, status, wake-up and cancellation | SRC-1 `src/commands/exp.rs`; `src/plane/local_plane.rs` | Direct dispatch and launch reads; compute details supplied by [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run), wake-up by [RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup). Remote executor parity unassessed; prevents a universal provenance/reproducibility conclusion. |
| Logs, interpretation, selection of next experiments | SRC-1 `src/commands/logs.rs`; `agent-skills/orx-results/SKILL.md`; `agent-skills/orx-experiment-tree/SKILL.md` | Direct complete logs implementation/results and tree skills; see [EPI-RTE-log-preview](#epi-rte-log-preview), [EPI-RTE-results-check](#epi-rte-results-check), [EPI-RTE-winner-promotion](#epi-rte-winner-promotion). No trace of an actual evidence-consuming acceptance. |
| Description overwrite, reparent, archive/unarchive | SRC-1 `src/commands/exp.rs`; `src/plane/local_plane.rs`; `src/local/experiments.rs` | Direct write/read, archive traversal and move/check code; see [EPI-RTE-description-store](#epi-rte-description-store), [EPI-RTE-tree-organize](#epi-rte-tree-organize). These are retention/organization controls, not independent scientific rejection. |
| Artifacts, figures, manuscript | SRC-1 `src/local/files.rs`; `agent-skills/orx-reports/SKILL.md`; `agent-skills/orx-figures/SKILL.md`; `agent-skills/orx-figures/assets/orx_chart.py`; `agent-skills/orx-paper/SKILL.md` | Direct artifact root/list/read/delete, complete reports skill/chart helper, bounded figure and paper instruction reads; see [EPI-RTE-artifact-retain](#epi-rte-artifact-retain), [EPI-RTE-chart-render](#epi-rte-chart-render). LaTeX compiler, static figures and browser chart execution not traced; successful rendering would not prove claims. |
| Persistent skills and binary updates | SRC-1 `src/local/user_skills.rs`; `src/updates.rs` | Supplied findings see [RT-RTE-skill-upload](runtime.md#rt-rte-skill-upload), [RT-RTE-release-update](runtime.md#rt-rte-release-update). Structural/channel admission, not measured improvement. |
| Shipped nanochat evidence | SRC-1 `demo/nanochat/evidence/README.md` | Direct evidence inventory read only. It attributes small outputs to a completed run and explicitly omits weights, data and environment. Metrics, scripts and checkpoint provenance were not traced here. No independent observed-route or causal claim follows. |
| Other included operations | SRC-1 `src/main.rs`; `docs/`; `tests/`; `scripts/`; `ui/` | CLI surface mapped; detailed remote services, project editing, publication/Overleaf, feedback/rankings, UI claim-link rendering, figure templates and evaluation/demo generation remain unassessed here. They prevent a system-complete negative about checking or adaptation. Boundary inclusion is not inspection. |

Missing traces prevent conclusions about exercised checking, acceptance, theory revision or later effects. Missing controlled comparisons prevent attribution of research quality or improvement to any component. Provider internals prevent conclusions about weight updates and hidden reasoning; supplied model limits are see [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model) and [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model). These gaps do not cancel the inspectable architecture.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-literature-content](#epi-obj-literature-content) | Abstracts, paper claims, snippets, metadata and externally generated reports | External research evidence/candidates | SRC-1 `src/client.rs`; `src/commands/paper.rs` | Imported report is not original text; source truth and extraction fidelity unknown. |
| [EPI-OBJ-run-log](#epi-obj-run-log) | Printed configuration, metrics and trajectory; error/status text separately describes execution | Measurement evidence requested before reporting | SRC-1 `src/commands/logs.rs`; `agent-skills/orx-results/SKILL.md` | Arbitrary run output; evaluator correctness, data integrity and completeness not certified. |
| [EPI-OBJ-experiment-description](#epi-obj-experiment-description) | Hypotheses, observations, summaries, or no truth-apt content depending on caller text | Durable notes | SRC-1 `src/plane/local_plane.rs`; `agent-skills/orx-experiment-tree/SKILL.md` | Whole-text replacement; no content/provenance criterion. |
| [EPI-OBJ-research-outputs](#epi-obj-research-outputs) | Report assertions and charted measurements, possibly novel interpretations | Durable deliverables | SRC-1 `src/local/files.rs`; `agent-skills/orx-reports/SKILL.md` | File presence is not acceptance. Manuscripts in worktrees are a separate destination, not all artifacts. |
| [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot) | Committed experiment code; hypotheses may reside in code but are not inferred from metadata | Code/run binding | see cited record | Does not freeze data or ambient dependencies. |
| [RT-OBJ-playbook](runtime.md#rt-obj-playbook) | Policy text, project facts and identifiers; policy is not itself an empirical result | Research/evidence guidance | see cited record | Separate natural-language authority from symbolic enforcement. |
| [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model), [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model) | Individuated stored propositions not determinable from accessible weights/endpoints | Generation and interpretation | see cited records | Provider parameters and actual semantic decisions uninspected; no claim of absent parametric knowledge. |

## Authority-route ledger

The following are function-level overlays. Fields owned by cited records are **see** those records; local fields below assess warrant and force. Multiple functions sharing a route stay separate. Architectural status does not imply activation.

Route ID: [EPI-RTE-literature-import](#epi-rte-literature-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-literature-content](#epi-obj-literature-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: external responses to literature commands.
Evaluator/condition and domain: source-enabled checks, HTTP/result parsing and requested search parameters; service/interface domain, not truth of paper claims.
Activation and timing: explicit discovery/paper command; output immediately.
Possible or observed result: ranked hits or paper/report/abstract text; missing-source errors.
Implemented force: imported content becomes available to the caller.
Epistemic authority and scope: attributed external content only; source warrant unknown. DOI/id/source labels help lineage, not endorsement. Default alphaXiv report is not an original-text quotation source.
Operational authority: behavior permitted, blocked, or changed: enabled connectors can supply candidates; disabled connectors reject requests.
Behavioral-authority path: consumer, channel, force, horizon: agent/operator, CLI stdout, evidence/advisory input, current task and any later retained quotation.
Evidence source ID and local anchor: SRC-1 `src/commands/discover.rs`; `src/commands/paper.rs`; `src/client.rs`.
Claim IDs or none: [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance).
Mismatch marker or none: none.
Gap/limit: retrieval ranking is not scientific acceptance; corpus and remote report generation uninspected.

Route ID: [EPI-RTE-abstract-reshape](#epi-rte-abstract-reshape)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-literature-content](#epi-obj-literature-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: OpenAlex token-position index to printable abstract.
Evaluator/condition and domain: deterministic sort/join, assuming faithful unique token positions.
Activation and timing: OpenAlex abstract access during hit conversion or paper printing.
Possible or observed result: reordered words joined by spaces; absent index gives empty string.
Implemented force: determines the text delivered downstream.
Epistemic authority and scope: preserves indexed word order under the stated input assumption; no new scientific proposition warranted.
Operational authority: behavior permitted, blocked, or changed: reconstructed abstract enters CLI output.
Behavioral-authority path: consumer, channel, force, horizon: LitHit/paper printer then agent, text, advisory, current read.
Evidence source ID and local anchor: SRC-1 `src/client.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: malformed/tied positions do not establish faithful reconstruction; source truth remains unknown.

Route ID: [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot), [EPI-OBJ-run-log](#epi-obj-run-log)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: project-selected code/run command; whether output measures the scientific hypothesis depends on that code and setup.
Evaluator/condition and domain: OS/backend execution and process status; project-specific evaluator inside supplied code uninspected.
Activation and timing: see cited route.
Possible or observed result: run status, logs and any command-generated metrics.
Implemented force: scheduling/status and data production, not scientific acceptance.
Epistemic authority and scope: source revision and process outcome do not establish a scientific answer. Entailed metric calculations versus novel claims require individual program and premise inspection.
Operational authority: behavior permitted, blocked, or changed: see cited route; later wake-up can trigger interpretation.
Behavioral-authority path: consumer, channel, force, horizon: store/UI/agent, status/logs, informational then scheduling, run and subsequent turn.
Evidence source ID and local anchor: see cited route, SRC-1 `src/compute.rs`; `src/local/localrun.rs`.
Claim IDs or none: [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance).
Mismatch marker or none: none.
Gap/limit: no executed or causally isolated hypothesis test supplied.

Route ID: [EPI-RTE-log-preview](#epi-rte-log-preview)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-log](#epi-obj-run-log)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: captured log suffix to compact preview plus full-file pointer.
Evaluator/condition and domain: byte-length check and fixed clipping; text display domain.
Activation and timing: `orx logs` after resolving a run.
Possible or observed result: path, byte size and last 500 decoded characters from up to 2048 bytes.
Implemented force: limits initial agent-visible evidence; targeted reads remain possible.
Epistemic authority and scope: preview cannot establish absent configuration/metric/trajectory in the full log.
Operational authority: behavior permitted, blocked, or changed: caller can locate/search full evidence; no automatic claim check.
Behavioral-authority path: consumer, channel, force, horizon: agent/operator, stdout plus file path, advisory, current evidence acquisition.
Evidence source ID and local anchor: SRC-1 `src/commands/logs.rs`.
Claim IDs or none: [EPI-CLM-results-evidence](#epi-clm-results-evidence).
Mismatch marker or none: none.
Gap/limit: UTF-8 lossy decode can alter boundary characters; extraction is not measurement verification.

Route ID: [EPI-RTE-results-check](#epi-rte-results-check)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-run-log](#epi-obj-run-log), [EPI-OBJ-research-outputs](#epi-obj-research-outputs)
Content/update relation: no content change
Transition or check target: a proposed run-derived assertion, for reporting or comparison of named variants.
Evaluator/condition and domain: instructed agent checks variant/effective configuration, final metric/summary, trajectory for long runs and supporting file lines; literature claims separately require reading original evidence.
Activation and timing: requested before accepting/reporting; no exercised check established.
Possible or observed result: sufficient support, missing evidence, or qualified inference.
Implemented force: instruction delivery exists via playbook/skills; semantic check itself is requested, not a Rust evaluator.
Epistemic authority and scope: criteria can support bounded run reporting if actually applied; do not certify evaluator design, causality, generality or source truth.
Operational authority: behavior permitted, blocked, or changed: agent is told to retrieve missing output and not invent data; no software block on unsupported reports identified in these paths.
Behavioral-authority path: consumer, channel, force, horizon: foreground model, native skill text and playbook, advisory, present interpretation/report.
Evidence source ID and local anchor: SRC-1 `agent-skills/orx-results/SKILL.md`; `agent-skills/orx-lit-review/SKILL.md`; delivery see [RT-BAP-playbook-injection](runtime.md#rt-bap-playbook-injection).
Claim IDs or none: [EPI-CLM-results-evidence](#epi-clm-results-evidence).
Mismatch marker or none: requested checks versus unobserved compliance.
Gap/limit: no recorded evidence-consuming acceptance decision.

Route ID: [EPI-RTE-results-check](#epi-rte-results-check)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-research-outputs](#epi-obj-research-outputs)
Content/update relation: no content change
Transition or check target: eligibility to accept/report a run-derived claim.
Evaluator/condition and domain: same agent, only after the preceding evidence criteria; reporting use scoped to the inspected run/configuration.
Activation and timing: before reporting.
Possible or observed result: withhold pending evidence or report with evidence/limits; observed decision unavailable.
Implemented force: advisory only.
Epistemic authority and scope: conditional license to state the measurement, not guaranteed truth or accepted ampliative knowledge.
Operational authority: behavior permitted, blocked, or changed: instructed reporting restraint; no enforced pre-publication acceptance gate in the inspected artifact write path.
Behavioral-authority path: consumer, channel, force, horizon: reporting model, instructions, advisory, report/chat output.
Evidence source ID and local anchor: SRC-1 `agent-skills/orx-results/SKILL.md`.
Claim IDs or none: [EPI-CLM-results-evidence](#epi-clm-results-evidence).
Mismatch marker or none: none.
Gap/limit: instruction to accept conditionally is not a recorded acceptance event.

Route ID: [EPI-RTE-winner-promotion](#epi-rte-winner-promotion)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-run-log](#epi-obj-run-log), [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot)
Content/update relation: no content change
Transition or check target: chosen experiment as next round's parent; hypothesis answered versus implementation failure.
Evaluator/condition and domain: instructed agent compares project outcomes against goal; clear win promotes; unanswered run repairs, mediocre result refills, goal/exhaustion stops.
Activation and timing: per completion after reading logs and applying results guidance.
Possible or observed result: repair, refill, promote or stop; these choices are not observed.
Implemented force: prescribed selection policy; branch/launch primitives are implemented separately.
Epistemic authority and scope: measured consequence fit can guide local optimization; no mechanism explanation or transfer warranted by winner selection alone.
Operational authority: behavior permitted, blocked, or changed: parent selection carries winning code into a subsequent round; caps request escalation/stop after failures.
Behavioral-authority path: consumer, channel, force, horizon: foreground agent then create-experiment/launch, skill text and branch identifiers, advisory then executable branch selection, rounds of a project.
Evidence source ID and local anchor: SRC-1 `agent-skills/orx-experiment-tree/SKILL.md`; execution primitives see [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run).
Claim IDs or none: [EPI-CLM-experiment-loop](#epi-clm-experiment-loop).
Mismatch marker or none: none.
Gap/limit: no enforced scientific winner selector; frozen-node rule remains instruction, not a demonstrated universal branch lock.

Route ID: [EPI-RTE-description-store](#epi-rte-description-store)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-experiment-description](#epi-obj-experiment-description)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: caller text into experiment description.
Evaluator/condition and domain: input-source resolution and experiment lookup, not content truth.
Activation and timing: explicit desc set/stdin.
Possible or observed result: whole description saved or read back.
Implemented force: durable text replacement.
Epistemic authority and scope: unknown warrant; retention is not acceptance.
Operational authority: behavior permitted, blocked, or changed: later callers can read hypotheses/observations and act on them without another quality gate here.
Behavioral-authority path: consumer, channel, force, horizon: CLI user/model, SQLite description then stdout, advisory, subsequent project invocations.
Evidence source ID and local anchor: SRC-1 `src/plane/local_plane.rs`.
Claim IDs or none: [EPI-CLM-experiment-loop](#epi-clm-experiment-loop).
Mismatch marker or none: none.
Gap/limit: arbitrary descriptions need not be truth-apt; when purely policy, relation is non-truth-apt text update instead. No automatic source provenance field or restoration in this write function.

Route ID: [EPI-RTE-tree-organize](#epi-rte-tree-organize)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot)
Content/update relation: no content change
Transition or check target: experiment parent/archive state, not prior scientific conclusions.
Evaluator/condition and domain: transaction, project membership, baseline/root and cycle checks; structural consistency domain.
Activation and timing: explicit move/archive/unarchive.
Possible or observed result: changed parent or hidden/restored nodes while branches/runs remain.
Implemented force: changes navigation and comparison context.
Epistemic authority and scope: no scientific revocation/reacceptance; current parent need not be historical code ancestry.
Operational authority: behavior permitted, blocked, or changed: users/agents can reorganize visible research; invalid structural moves rejected.
Behavioral-authority path: consumer, channel, force, horizon: tree/diff readers, store parent/archive fields, enforcing structure/ranking visibility, later project use.
Evidence source ID and local anchor: SRC-1 `src/local/experiments.rs`; `src/commands/exp.rs`.
Claim IDs or none: [EPI-CLM-experiment-loop](#epi-clm-experiment-loop).
Mismatch marker or none: lineage caveat: move changes comparison parent but not branch code.
Gap/limit: archive is reversible presentation control, not withdrawal of every copied claim; downstream UI details uninspected.

Route ID: [EPI-RTE-artifact-retain](#epi-rte-artifact-retain)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-outputs](#epi-obj-research-outputs)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: producer's finished file into project filesystem deliverables.
Evaluator/condition and domain: writer's OS authority and file path containment for API access, not scientific accuracy.
Activation and timing: file write; listing does not await approval.
Possible or observed result: immediately listed deliverable, later read or deletion.
Implemented force: storage/serving; no separate content admission in inspected listing path.
Epistemic authority and scope: source warrant unknown; files may be unaccepted candidates.
Operational authority: behavior permitted, blocked, or changed: operator/agent can inspect/link existing deliverables; deleting a file does not retract transcript copies or evidence claims elsewhere.
Behavioral-authority path: consumer, channel, force, horizon: dashboard/operator and later readers, filesystem/link, availability/advisory, across sessions until changed/deleted.
Evidence source ID and local anchor: SRC-1 `src/local/files.rs`; `agent-skills/orx-reports/SKILL.md`.
Claim IDs or none: [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance).
Mismatch marker or none: none.
Gap/limit: arbitrary binary/non-truth-apt files are also admitted; import classification concerns truth-apt report/data portions only. No lifecycle integration after established acceptance evidenced.

Route ID: [EPI-RTE-chart-render](#epi-rte-chart-render)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-outputs](#epi-obj-research-outputs)
Content/update relation: no content change
Transition or check target: supplied metric/series representation, finite coordinates, log positivity, intervals and diagram references.
Evaluator/condition and domain: deterministic Python checks, chart-schema/numerical domain.
Activation and timing: validate_views before JSON serialization/output write.
Possible or observed result: passes or raises ValueError/other input error.
Implemented force: failed checks prevent this helper's new write.
Epistemic authority and scope: well-formed plottable values, not run provenance, honest seed counts, correct metric interpretation or valid uncertainty estimates.
Operational authority: behavior permitted, blocked, or changed: rejects unsuitable inputs to this renderer only.
Behavioral-authority path: consumer, channel, force, horizon: render_chart, exceptions/return, enforcing, this render invocation.
Evidence source ID and local anchor: SRC-1 `agent-skills/orx-figures/assets/orx_chart.py`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: static plots and arbitrary hand-written HTML bypass helper; valid fabricated data would pass structural checks.

Route ID: [EPI-RTE-chart-render](#epi-rte-chart-render)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-outputs](#epi-obj-research-outputs)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: validated values to offline HTML data payload.
Evaluator/condition and domain: prior validation then JSON serialization and template replacement.
Activation and timing: after checks within render_chart.
Possible or observed result: self-contained output file with encoded data.
Implemented force: validation result permits write; no scientific acceptance.
Epistemic authority and scope: serialization preserves supplied numbers within its supported domain; plotted meaning depends on labels and viewer implementation.
Operational authority: behavior permitted, blocked, or changed: write chart for downstream reader.
Behavioral-authority path: consumer, channel, force, horizon: reader/browser, HTML file, advisory presentation, later deliverable reads.
Evidence source ID and local anchor: SRC-1 `agent-skills/orx-figures/assets/orx_chart.py`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: browser plotting not traced; rendering success is not an empirical result.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance) | see record | see record | Broad research assignment | [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run), [EPI-RTE-literature-import](#epi-rte-literature-import), [EPI-RTE-artifact-retain](#epi-rte-artifact-retain) | None assessed | No comparison establishes research effectiveness or component effect | Implements tools/context enabling research requests | Model compliance and product quality unknown |
| [EPI-CLM-results-evidence](#epi-clm-results-evidence) | see record | SRC-1 `agent-skills/orx-results/SKILL.md`; doctrine/design | Explicit evidence prerequisites and claim-link guidance | [EPI-RTE-log-preview](#epi-rte-log-preview), [RT-BAP-playbook-injection](runtime.md#rt-bap-playbook-injection); semantic assessment see [EPI-RTE-results-check](#epi-rte-results-check) | No check/acceptance trace | No comparison; criteria are bounded to supporting output, not causal explanation | Clear requested separation of run success from result interpretation | Requested semantic validation, not an enforced publication gate |
| [EPI-CLM-experiment-loop](#epi-clm-experiment-loop) | see record | SRC-1 `agent-skills/orx-experiment-tree/SKILL.md`; doctrine/design | Hypothesize, measure, choose, retain winners, stop/repair | Branch/run primitives see [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run); retention [EPI-RTE-description-store](#epi-rte-description-store), organization [EPI-RTE-tree-organize](#epi-rte-tree-organize); selection see [EPI-RTE-winner-promotion](#epi-rte-winner-promotion) | No exercised round traced | Outcome selection cannot attribute component effects unless comparison isolates them | Instructed research loop with durable code/notes | No established autonomous scientific completion, theory criticism or improvement |

## Bounded conclusion

OpenResearch acquires attributed literature rather than producing those imported claims. Search results, citations and freshness govern candidate availability/ranking, not acceptance. The default alphaXiv paper report is externally supplied; the literature skill explicitly distinguishes that report from original evidence suitable for quotation. Source warrant remains unknown. OpenAlex reconstruction is a bounded non-ampliative transformation, not discovery of a new scientific fact ([EPI-RTE-literature-import](#epi-rte-literature-import), [EPI-RTE-abstract-reshape](#epi-rte-abstract-reshape)).

The local experiment path binds a source archive to execution but not all empirical premises. Arbitrary run programs may derive measurements or generate conjectures; their content/update relation cannot be assigned from exit status. No warranted-premise derivation or accepted ampliative claim instance is established here. The instructed agent can interpret logs and suggest hypotheses, but no particular non-entailing inference, check or evidence-consuming acceptance event was inspected. The explicit result criteria license only supported reporting about the inspected configuration/run if applied; they do not establish mechanism truth or transfer ([RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run), [EPI-RTE-results-check](#epi-rte-results-check)).

Operational success and warrant have separate consumers. Completion wake-ups schedule later model work using status, not full measurements. Log previews omit most evidence but preserve a pointer to full logs. The chart helper enforces numerical/schema conditions and blocks its own write on errors; it does not authenticate values. Thus an implemented evaluator exists, but its license is chart validity, not scientific truth ([RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup), [EPI-RTE-log-preview](#epi-rte-log-preview), [EPI-RTE-chart-render](#epi-rte-chart-render)).

Descriptions and project artifacts retain candidates without requiring scientific approval. Reparenting and archive controls organize/hide nodes; they do not constitute rejection or withdrawal of conclusions everywhere those conclusions were copied. No post-acceptance lifecycle integration event is established; retention and branch use remain separate from acceptance. The instructed winner-promotion path can carry selected code into later rounds without a new truth-apt theory, and is distinct from retaining a proposition as knowledge ([EPI-RTE-description-store](#epi-rte-description-store), [EPI-RTE-artifact-retain](#epi-rte-artifact-retain), [EPI-RTE-tree-organize](#epi-rte-tree-organize), [EPI-RTE-winner-promotion](#epi-rte-winner-promotion)).

The theory-builder properties remain independent. Hypothesis descriptions and inspectable code afford localized content; the tree skill requests content-dependent experiment decisions and iteration. Neither actual theory consumption nor criticism allocating blame among theory/test/data/auxiliaries is demonstrated. Winner scores alone would not establish such criticism. Persistence of descriptions/code does not establish improved capacity for future action. A research goal about an external project does not establish reflection on OpenResearch's own operation, autonomous performance of every internal research role, or evidence-responsive self-improvement of OpenResearch. Skill and binary update paths can alter later instructions/machinery, but their actual force and evidence limits are see [RT-RTE-skill-upload](runtime.md#rt-rte-skill-upload) and [RT-RTE-release-update](runtime.md#rt-rte-release-update). No inference of weight learning or its absence follows from opaque inference endpoints. Unassessed operations in the coverage table preclude a whole-system absence verdict.

## Shared records

### Operative objects

#### EPI-OBJ-literature-content
Label: Literature content

Source-native identity: LitHit and paper-command markdown/abstract output. Natural-language abstracts/reports plus symbolic source/id/date/vote/citation metadata, held in response structs and stdout; any durable retention is caller-owned. SRC-1 `src/client.rs`; `src/commands/paper.rs`. No counterpart among supplied runtime objects: this is acquired scholarly content, not the playbook or source archive.

> pub struct LitHit {
>     /// `"alphaxiv" | "openalex" | "biorxiv" | "pubmed"` — set by the search fn.
>     pub source: String,
> --- `src/client.rs`

> let kind = if args.full { "abs" } else { "overview" };
> --- `src/commands/paper.rs`

#### EPI-OBJ-run-log
Label: Run log

Source-native identity: local run log at log_path(run id), plain filesystem text with arbitrary program output, numerals and status messages. Truth-apt measurement portions require interpreting experiment code and configuration. Distinct from [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot), which stores selected source, and from the run route itself, which produces the output. SRC-1 `src/commands/logs.rs`.

> let path = log_path(&args.run_id);
> --- `src/commands/logs.rs`

#### EPI-OBJ-experiment-description
Label: Experiment description

Source-native identity: experiment.description, optional free-form markdown persisted through Store's experiment update. Natural-language notes may state hypotheses, observations or instructions. No counterpart among supplied runtime objects; not identical to executable source or static playbook. SRC-1 `src/plane/local_plane.rs`.

> exp.description = Some(description);
>                 self.store.update_local_experiment(&exp)?;
> --- `src/plane/local_plane.rs`

#### EPI-OBJ-research-outputs
Label: Research outputs

Source-native identity: files under project artifacts root, including reports, datasets, PDFs and figures. Filesystem substrate; natural-language assertions and symbolic measurement/chart payloads are separately consumed as prose or parsed chart data. Not the worktree source archive; no supplied runtime object counterpart. Arbitrary files may also be non-truth-apt. This is a container, not an assertion that all these parts share a validator. SRC-1 `src/local/files.rs`; `agent-skills/orx-reports/SKILL.md`.

> Written files become project artifacts
> immediately.
> --- `agent-skills/orx-reports/SKILL.md`

### Routes

#### EPI-RTE-literature-import
Label: Literature retrieval

Endpoints/progression: caller → discovery/paper command → enabled external connector → parsed hit/text → stdout. Caller owns query/selection; Rust owns dispatch/error handling. Distinct from [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn): this is a CLI evidence acquisition operation a turn may use, not the enclosing turn. SRC-1 `src/commands/discover.rs`; `src/commands/paper.rs`; `src/client.rs`.

- Immediate return: JSON hits or markdown/metadata/abstract; transport/missing/disabled-source errors otherwise.
- Later read-back: inapplicable — command itself does not store retrieved literature; caller may retain it elsewhere.
- Delegated visibility: foreground caller receives the returned output; no independent retrieval subagent implemented in this command.
- Selection predicate: source, query, limit, date/priority options; paper source autodetection or override and full flag.
- Invalidation or expiry: no persistent endorsement/cache lifecycle established by inspected command functions; next call fetches anew.
- Activation or effect: implementation returns candidate evidence and routes disabled-source requests to errors; downstream use unobserved.
- Evidence limits: provider search/report generation and service truth uninspected; no observed query.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Discovery services provide candidate order, not an expected-answer oracle. Code can veto disabled sources; caller/model chooses which returned papers to inspect. Open-request literature task, not a built-in correctness curriculum. The literature skill requests deduplication/ranking and dropping invented IDs, but those are model instructions, not checks in the CLI command.

> println!("{}", serde_json::to_string_pretty(&results)?);
> --- `src/commands/discover.rs`

> if status.as_u16() == 404 {
>         return Ok(None);
>     }
> --- `src/client.rs:915-917`

> Ok(Some(res.text().await?))
> --- `src/client.rs`

> match (full, primary_found) {
>         (false, false) => Some("abs"),
>         _ => None,
>     }
> --- `src/commands/paper.rs`

> Read a paper before using it as claim-level support. Discovery lists may link
> candidate titles, but must not imply that methods or findings were verified
> from snippets alone.
> --- `agent-skills/orx-lit-review/SKILL.md`

> Quote only original text you actually read, including full-text snippets with
> sufficient context—not generated reports or summaries.
> --- `agent-skills/orx-lit-review/SKILL.md`

#### EPI-RTE-abstract-reshape
Label: Abstract reconstruction

Endpoints/progression: OpenAlex abstract_inverted_index → reconstruct_abstract → abstract_text → LitHit or paper printer. Rust owns deterministic text order. Distinct from acquisition: this is a local transformation within the imported object, not external retrieval. SRC-1 `src/client.rs`.

- Immediate return: joined token string, or empty string for absent index.
- Later read-back: inapplicable — transformation does not persist state.
- Delegated visibility: caller receives reconstructed abstract through command output.
- Selection predicate: every token-position pair supplied in the index, sorted by numeric position.
- Invalidation or expiry: inapplicable — recalculated from each supplied response.
- Activation or effect: changes indexed representation into reading order before output.
- Evidence limits: implementation deduction only; no source text comparison or malformed-input guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction, without execution: index {"works":[2], "Deep":[0], "learning":[1]} yields sorted pairs (0,Deep),(1,learning),(2,works), then `Deep learning works`. This is non-ampliative reshaping under unique correct positions. It does not prove the sentence true. None produces empty text; equal positions can leave ordering dependent on hash iteration, so reconstruction fidelity is conditional, not universal.

> for (token, positions) in index {
>         for &p in positions {
>             positioned.push((p, token.as_str()));
>         }
>     }
>     positioned.sort_by_key(|(p, _)| *p);
>     positioned
>         .into_iter()
>         .map(|(_, t)| t)
>         .collect::<Vec<_>>()
>         .join(" ")
> --- `src/client.rs`

#### EPI-RTE-log-preview
Label: Compact log preview

Endpoints/progression: resolved run → local log file → captured-length suffix read → lossy UTF-8/character clipping → stdout pointer and preview. Rust owns selection; caller must inspect full evidence separately. Distinct from [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run): delivery transformation of its output, not execution. SRC-1 `src/commands/logs.rs`.

- Immediate return: file path, size and 500-character suffix, or missing-log notice.
- Later read-back: full log remains reachable by supplied filesystem path; this command does not write a summary memory.
- Delegated visibility: only suffix initially reaches caller; remaining evidence requires targeted reads.
- Selection predicate: last up to 2048 captured bytes then last up to 500 decoded characters.
- Invalidation or expiry: short read against captured size errors; later calls may see appended output.
- Activation or effect: bounded context delivery, not proof that excluded evidence is irrelevant or absent.
- Evidence limits: no log retrieval executed; provenance inherited from run/log writer rather than authenticated here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete transformation deduction: an ASCII log of 600 `a` characters has all 600 bytes in the suffix read but only its final 500 characters printed as preview. Configuration in its first 100 characters would be absent from the preview yet reachable through the path. The code's own warning matches this limitation.

> const PREVIEW_CHARS: usize = 500;
> const PREVIEW_SUFFIX_BYTES: usize = 2048;
> --- `src/commands/logs.rs`

> "Use targeted search on this path (for example `rg PATTERN` or an editor) to inspect portions of the log. This preview is not proof of absence."
> --- `src/commands/logs.rs`

#### EPI-RTE-results-check
Label: Validate before reporting

Endpoints/progression: candidate result assertion → instructed agent inspects supporting output → accept/report or retrieve/qualify. Agent is proposed evaluator; instructions name evidence, not a reference answer. This is distinct from runtime execution/status and permission admission. SRC-1 `agent-skills/orx-results/SKILL.md`; `SYSTEM_PROMPT.md`.

- Immediate return: inapplicable — instruction, not a separate executable check API.
- Later read-back: inapplicable — this instruction establishes no dedicated retained check result; reports/notes are independent write paths.
- Delegated visibility: foreground model is instructed to load results/logs skills; actual skill invocation/compliance unobserved.
- Selection predicate: before accepting/reporting any run-derived claim; long runs additionally need trajectory evidence.
- Invalidation or expiry: missing evidence should withhold reporting; no automated global claim revocation mechanism established here.
- Activation or effect: requested checking and reporting restraint; delivery wired through runtime guidance, semantic action unobserved.
- Evidence limits: doctrine/design for semantic check and disposition; implementation of model reasoning inaccessible.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

Proposer/decider: agent or user proposes assertion; instructed agent checks and decides report contents. Human can judge products, but no mandatory per-claim approval is specified. No expected-answer oracle; recorded run output is evidence, not infallible ground truth. Mode: open research request. Revised guidance is not admitted here; changed report text would be an external work product. The before-report criterion does not establish a recorded acceptance merely because a file was saved.

> Never infer a result from run status or memory. Before accepting or reporting a
> run-derived claim, confirm that:
>
> - the log identifies the variant and effective configuration;
> - the final metric and compact summary are present;
> - the relevant trajectory is recoverable for a long run; and
> - the cited file lines actually contain the supporting output.
> --- `agent-skills/orx-results/SKILL.md`

> Ground substantive claims about this project's code, files, artifacts, or
> measured results with a clickable reference immediately after the claim. Clearly
> label an inference instead of presenting it as an observation.
> --- `SYSTEM_PROMPT.md`

#### EPI-RTE-winner-promotion
Label: Per-completion experiment decision

Endpoints/progression: finished run → read logs/results → repair/refill/promote/stop → next parent/child experiments. Foreground agent owns scientific decisions; branch/run software executes commands separately. Distinct from [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run) and [RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup): policy selecting subsequent experiments, not execution or wake delivery. SRC-1 `agent-skills/orx-experiment-tree/SKILL.md`.

- Immediate return: inapplicable — prescribed agent loop, no separate automatic winner-selection API.
- Later read-back: selected parent's committed code is inherited by subsequent children; notes can retain rationale separately.
- Delegated visibility: agent reads run states/logs and branches; no automatic hidden scientific judge is specified.
- Selection predicate: clear win → promote; no answer → repair; mediocre/inconclusive → refill; goal met/exhausted → stop.
- Invalidation or expiry: answered nodes instructed frozen; failed setup may be repaired; repair caps/escalation and scientific stop requested.
- Activation or effect: requested adaptive experiment choice and carried-forward code; not an observed decision.
- Evidence limits: doctrine only for judgment/criticism/iteration; software primitives do not establish compliance or improved capacity.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

Admission: agent proposes hypotheses and selects winners, human supplies objective and is asked on repeated repair failures. No per-winner human veto gate or expected-answer oracle is specified; goal/measurements are project-specific. Scope is external research-product change; recovery is repair/new child and stopping, not automatic restoration of rejected scientific text. The fixed-command/environment rule protects comparison in doctrine; actual confound control is not established without inspected experiments.

Theory account: descriptions can formulate hypotheses and code states testable variants. The rule applies evidence to variant selection and requests iterative retention of winners. It does not by itself demonstrate content-directed criticism of a theory, or which theory/test/data assumption is blamed. Theory-builder conditions 1–4: (1) afforded — localized hypotheses may be stated as whole descriptions/code; (2) claimed — decisions should depend on those hypotheses/results; (3) uninspected — no actual formulated criticism and changed reliance trace supplied; (4) claimed — next round should descend onto prior winner. Addressability is at least whole-description replacement and ordinary source editing, not a structured assumption ontology. Persistence can span rounds/projects through code/notes; actual repeated theory consumption unobserved. Learning: improved future capacity unestablished without improvement evidence. Reflection: no inspected self-representation/feedback loop about OpenResearch itself. Autonomous theory builder: role-by-role exercised computation unestablished; user escalation is explicitly allowed. No self-improvement attribution: optimizing external research code need not alter OpenResearch's behavior-determining organization.

> - **Promote** — result is a clear win: this node becomes the **parent for the next
>      round**. The next batch of children branch off *it*, not the baseline, so the win
>      carries forward and the next ideas stack on top of it.
> --- `agent-skills/orx-experiment-tree/SKILL.md`

> Unintended behaviour is not an answer. An OOM, a timeout, a divergence from a
> bug, a missing dep — those are implementation and hardware details, and the
> node is still provisional (unless the node's hypothesis *is* about memory or
> runtime, in which case that outcome is exactly its result).
> --- `agent-skills/orx-experiment-tree/SKILL.md`

#### EPI-RTE-description-store
Label: Description read and overwrite

Endpoints/progression: desc set/stdin → DescInput → cloned experiment description replacement → Store update; get prints nonempty description. Rust owns write; caller owns meaning and whether to preserve prior text. Distinct from runtime skill upload: project-specific notes rather than reusable native instructions. SRC-1 `src/plane/local_plane.rs`; `agent-skills/orx-experiment-tree/SKILL.md`.

- Immediate return: saved acknowledgment or current description text/empty hint.
- Later read-back: subsequent desc get returns stored text; later model interpretation possible, not automatic in this function.
- Delegated visibility: caller receives text; no autonomous broadcast to other agents established here.
- Selection predicate: explicit experiment ID and set/stdin/get choice.
- Invalidation or expiry: next set overwrites whole description; no automatic content invalidation shown.
- Activation or effect: persists caller-supplied notes without checking the claimed result; subsequent effects unobserved.
- Evidence limits: no exercised note update or later use; consumer compliance and quality not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes and decides entire text; Rust saves it, not a semantic evaluator or human-approval gate. No answer oracle or correctness curriculum. A replacement can remove earlier claims; no automatic rollback in this function. This can retain theories/criticisms, but does not prove those contents exist or satisfy theory conditions.

> DescInput::Get => match exp.description.as_deref().filter(|d| !d.trim().is_empty()) {
>                 Some(d) => println!("{d}"),
> --- `src/plane/local_plane.rs`

> Each experiment node carries a free-form **description** (markdown) — the same
> field set by `create-experiment --description`. Use it for notes: observations,
> hypotheses, or a running summary. It is a whole-document field: writing
> overwrites whatever was there.
> --- `agent-skills/orx-experiment-tree/SKILL.md`

#### EPI-RTE-tree-organize
Label: Move and archive experiments

Endpoints/progression: caller command → scoped IDs or checked parent → store update → future tree/comparison readers. Code owns structural checks; caller decides research organization. Distinct from source creation/execution: changing parent metadata leaves code unchanged, and archiving does not erase run evidence. SRC-1 `src/local/experiments.rs`; `src/commands/exp.rs`.

- Immediate return: changed scope/count or prior/new parent; structural errors can reject move.
- Later read-back: parent/archive metadata persists for subsequent tree readers; branch/run identity stays attached to node.
- Delegated visibility: UI and command readers can see changed organization; full UI filtering uninspected.
- Selection predicate: explicit node/parent or ancestor/descendant/only scope; project, baseline and cycle constraints for move.
- Invalidation or expiry: unarchive reverses hiding; later valid move can replace parent; no automatic scientific withdrawal.
- Activation or effect: changes structure/visibility, not branch source; subsequent interpretations unobserved.
- Evidence limits: implemented metadata mutation; scientific suitability of new parent is caller judgment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes/decides reorganization; software vetoes structural invalidity, not scientific mismatch. No answer oracle. Guidance says move only where code fits new parent; the software does not rebase code to make that true. Recovery uses unarchive/another valid move; not acceptance of the preserved results.

> check_move(&experiments, &project, &selected, parent)?;
>     store.set_experiment_parent(&selected.id, parent)?;
>     tx.commit()?;
> --- `src/local/experiments.rs`

> println!("  Git branch {} is unchanged.", before.branch_name);
> --- `src/commands/exp.rs`

> `move` changes only the tree; runs and results stay attached to the node.
>   Its branch is not rebased and still holds the old parent's code, so diffs
>   then compare against the new parent's branch (or the project base branch
>   for `--baseline`). Move only nodes whose code fits the new parent.
> --- `agent-skills/orx-experiment-tree/SKILL.md`

#### EPI-RTE-artifact-retain
Label: Artifact write and access

Endpoints/progression: agent/user writes project file → filesystem tree listing and contained read → operator/later consumer; delete removes chosen file/folder. OS/file writer owns content; Rust owns serving. Distinct from source snapshot and skill upload: deliverable filesystem, not executable archive or native skill directory. SRC-1 `src/local/files.rs`; `agent-skills/orx-reports/SKILL.md`.

- Immediate return: writer's I/O result; artifact listing returns paths/metadata and truncation marker.
- Later read-back: files remain available through project artifact path until overwritten/deleted; not automatically injected into model context by this function.
- Delegated visibility: dashboard/external reader and agents able to read linked files; actual consumption unobserved.
- Selection predicate: project directory and requested relative path; listing cap/ignored OS metadata and path containment limit delivery.
- Invalidation or expiry: direct overwrite/delete; no claim-level evidence-expiry policy found in inspected listing/access functions.
- Activation or effect: stored candidates become visible immediately, without demonstrated acceptance.
- Evidence limits: no actual artifact write/read exercised; content may be arbitrary and is not scientifically validated by serving.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: user/agent file writer decides contents. Existing-directory inspection and stable published paths are instructions, not content approval. No answer oracle. This admits an external research product; deletion/replacement is recovery at file level, without global retraction of copied claims. Lifecycle integration cannot be inferred from directory organization before acceptance is established.

> let (entries, truncated) = collect_tree(&canonical, &canonical, "", &mut seen);
> --- `src/local/files.rs`

> pub fn file_path(project: &LocalProject, rel_path: &str) -> Result<PathBuf> {
>     resolve_contained(&files_dir(project), rel_path)
> }
> --- `src/local/files.rs`

> if md.is_dir() {
>         std::fs::remove_dir_all(&path)
>     } else {
>         std::fs::remove_file(&path)
>     }
> --- `src/local/files.rs`

#### EPI-RTE-chart-render
Label: Validated chart rendering

Endpoints/progression: supplied metrics/series → validate_views → JSON serialization → template insertion → file. Python owns numerical/schema checks; caller supplies labels/values. Distinct from artifact retention: a particular producer/checker, not the storage access mechanism. SRC-1 `agent-skills/orx-figures/assets/orx_chart.py`.

- Immediate return: writes HTML or raises before write for invalid supported inputs.
- Later read-back: output file can be opened later; helper does not reload it or retain a check history.
- Delegated visibility: reader receives encoded chart data; browser rendering internals not traced here.
- Selection predicate: supplied metric keys and per-metric/default series; missing/null values omitted from measured subset for checks.
- Invalidation or expiry: caller rerenders/overwrites output; failure before write does not remove an older output already on disk.
- Activation or effect: check result directly gates new output; no check of run provenance or scientific interpretation.
- Evidence limits: source deduction, no helper/browser execution; alternate chart generators not covered.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes values; deterministic validation can veto malformed render input. No expected-answer oracle; numeric/schema domain only. For metric key `loss`, linear axes, a series containing {step:1,loss:2} satisfies finite coordinate checks and reaches serialization. Replacing loss with NaN raises; replacing it with a fabricated finite value still passes. Intervals must bracket values but are not statistically estimated here. This separates operative rejection from epistemic acceptance. Prior files surviving a failure are not newly validated outputs.

> if not all(isinstance(value, (int, float)) and math.isfinite(value) for value in (x, y)):
>                     raise ValueError("Graph coordinates must be finite numbers")
> --- `agent-skills/orx-figures/assets/orx_chart.py`

> validate_views(metrics, series)
>     data = dict(title=title, subtitle=subtitle, metrics=metrics, series=series, xLabel=x_label)
>     payload = json.dumps(data, allow_nan=False).replace("<", "\\u003c")
>     template = Path(__file__).with_name("orx-chart.html").read_text(encoding="utf-8")
>     Path(output).write_text(template.replace("__ORX_CHART_DATA__", payload), encoding="utf-8")
> --- `agent-skills/orx-figures/assets/orx_chart.py`

### Claims

#### EPI-CLM-results-evidence
Label: Evidence before reporting

Claimed operation: instruction requires supporting configuration, final metrics/summary, long-run trajectory and verified file lines before accepting/reporting run-derived claims. Doctrine/design, SRC-1 `agent-skills/orx-results/SKILL.md`. Passage and criteria are see [EPI-RTE-results-check](#epi-rte-results-check). Distinct from broader [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance): this is its specific warrant procedure, not a duplicate assignment.

#### EPI-CLM-experiment-loop
Label: Auto-research loop

Claimed operation: instructed hypotheses/measurements and per-completion repair/refill/promote/stop; winners become next-round parents. Doctrine/design, SRC-1 `agent-skills/orx-experiment-tree/SKILL.md`. Load-bearing promotion passage is see [EPI-RTE-winner-promotion](#epi-rte-winner-promotion). Distinct from [RT-CLM-research-assistance](runtime.md#rt-clm-research-assistance): a specific adaptive operating method, not a guarantee of successful science.

### Behavioral-authority paths

#### EPI-BAP-results-guidance
Label: Results guidance authority

Consumer: foreground native model. Channel: results/tree/literature skill text, selected per playbook; playbook delivery see [RT-BAP-playbook-injection](runtime.md#rt-bap-playbook-injection). Force: advisory semantic guidance, not programmatic veto of claims. Horizon: current result interpretation and proposed subsequent round, with code/notes possibly persisting further. SRC-1 `SYSTEM_PROMPT.md`; `agent-skills/orx-results/SKILL.md`; `agent-skills/orx-experiment-tree/SKILL.md`. Distinct from system-prompt injection itself: focused loaded skill content, whose loading/compliance remains unobserved. Evidence passages are see [EPI-RTE-results-check](#epi-rte-results-check) and [EPI-RTE-winner-promotion](#epi-rte-winner-promotion).
