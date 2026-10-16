---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Decapod epistemic routes: provenance-labelled knowledge, evaluator imports, proof-scoped publication and opaque internalization at the frozen commit."
run-id: AAS-2026-10-14-decapod-c44705119841-01
reviewed-boundary: "067b8f55071e13dd103779998168b4c9ffd31a79"
---

# Decapod epistemic report

## Source-and-claim boundary

The question is what Decapod licenses for reliance when it stores knowledge, supplies context, records judgments and verifies delivery. Scope and exclusions remain those of the [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. There is no observed target execution or causal experiment. External host inference, Jev internals and dependency implementations are excluded; their absence prevents claims about model reasoning, parameter updates, host compliance and end-to-end correctness, not static conclusions about inspected Decapod code.

The runtime is a provisional baseline. Direct inspection added knowledge admission, promotion, search, withdrawal, feedback proposal generation, evaluation artifacts and gate consumers, internalization creation/inspection/attach/detach, LCM summarization and commit-message policy. The schema catalog was checked against CLI/RPC dispatch. Available but uninspected alternatives remain explicit below; this is not a system-complete negative about knowledge production.

| Entry point or operation | Source path at SRC-1 | Coverage and conclusion prevented |
| --- | --- | --- |
| CLI/RPC and registered subsystem catalog | `src/decapod/lib.rs`, `src/decapod/cli.rs` | Direct reads/searches of knowledge/store, feedback, context/internalize, QA eval and catalog; other dispatch supplied by runtime, not all mutators traced. |
| Knowledge add/promote/search; library merge/decay/feedback | `src/decapod/plugins/knowledge.rs` | Direct implementation; records below cover content admission, retention, ranking and withdrawal. CLI add/RPC upsert use persistent active entries without merge key; schema advertises richer library operations, not proof every advertised option is CLI-exposed. Correction search for `decay_knowledge` in `src/`, `assets/tools/` and `.github/` found only its public declaration, not a shipped caller; decay is afforded, not wired. |
| QA eval judge/aggregate/gate | `src/decapod/plugins/eval.rs`, `src/decapod/core/workspace.rs` | Direct implementation, including publisher consumer. Task execution and external judge generation are not inspected; imported verdicts are not independently authenticated outcomes. |
| Context internalize | `src/decapod/plugins/internalize.rs` | Direct create/profile/inspect/attach/detach implementation. Non-noop configured binaries and model loading are uninspected; adapter semantic content and actual parameter application are not determinable. |
| Feedback add/propose | `src/decapod/plugins/feedback.rs` | Direct implementation; deterministic non-binding proposal, not automatic rule adoption. |
| LCM summarize/summary | `src/decapod/plugins/lcm.rs` | Direct summarizer plus source search of summary retrieval. Full ingest/rebuild/integrity routes uninspected; no whole-ledger integrity conclusion. |
| Prompt eval | `src/decapod/core/agent_eval.rs` | Direct evaluator read; dispatch/return supplied by runtime. |
| Constitution/spec/context resolution | `src/decapod/core/docs.rs`, `src/decapod/lib.rs`, `src/decapod/core/project_specs.rs` | Supplied runtime/boundary findings; semantic fidelity of every embedded projection not independently inspected. |
| Assurance/Jev, readiness/publication, updater | `src/decapod/core/assurance.rs`, `src/decapod/core/decision_provider.rs`, `src/decapod/core/validation_runtime.rs`, `src/decapod/core/workspace_publication.rs`, `src/decapod/lib.rs` | Supplied runtime records; added direct eval gate caller only. Full remote proof/CI/release drivers uninspected, preventing universal proof-adequacy or release-warrant conclusions. |
| Commit-message hook | `src/decapod/hooks/commit-msg.sh` | Direct complete read: conventional-subject regex, exit status. Formatting policy, not epistemic acceptance. Installation/host bypass uninspected. |
| Aptitude/memory, federation/decision, decide, context pack/restore | `src/decapod/plugins/aptitude.rs`, `src/decapod/plugins/federation.rs`, `src/decapod/plugins/decide.rs`, `src/decapod/plugins/context.rs` | Catalog, signatures and bounded RPC decision write examined, not full route traces. Confidence values, consolidation, status transitions, decision trees and caller-authored archive summaries require further inspection; cannot infer no additional warrant or adaptation routes. |
| Other QA, state-commit proof, policy/reflex/workflow/cron, primitives/map and build/release drivers | `src/decapod/lib.rs`, `assets/tools/`, `.github/` | Included, available, not exhaustively inspected. Prevents system-complete negative, exhaustive evaluator account, or universal enforcement conclusion. |

Consequential public/design claims are declared below rather than presumed true. The external research paper linked by README is not an acquired source. No assertion about its contents follows.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | Caller-supplied title/content may state propositions; no instance supplied | see [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | SRC-1, `src/decapod/plugins/knowledge.rs` | Provenance syntax and active status are not source truth; source warrant unknown. |
| [EPI-OBJ-promotion-event](#epi-obj-promotion-event) | Assertion of approval and evidence references | see [EPI-OBJ-promotion-event](#epi-obj-promotion-event) | SRC-1, `src/decapod/plugins/knowledge.rs` | Strings do not authenticate approval, resolve evidence or bind procedural content semantically. |
| [EPI-OBJ-eval-artifacts](#epi-obj-eval-artifacts) | Container of verdict and aggregate parts below | see [EPI-OBJ-eval-artifacts](#epi-obj-eval-artifacts) | SRC-1, `src/decapod/plugins/eval.rs` | Parts have distinct content and consumers; container alone confers no warrant. |
| [EPI-OBJ-eval-verdict](#epi-obj-eval-verdict) | Imported success assertion and explanation | see [EPI-OBJ-eval-verdict](#epi-obj-eval-verdict) | SRC-1, `src/decapod/plugins/eval.rs` | External judge warrant unknown; contract checking does not judge task truth. |
| [EPI-OBJ-eval-aggregate](#epi-obj-eval-aggregate) | Derived rates, sample counts and interval | see [EPI-OBJ-eval-aggregate](#epi-obj-eval-aggregate) | SRC-1, `src/decapod/plugins/eval.rs` | Numerical derivation conditional on imported verdicts, sampling design and settings. |
| [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | Symbolic assertions of source/adapter hashes, replayability and capability | see [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | SRC-1, `src/decapod/plugins/internalize.rs` | Metadata checks do not establish adapter semantics or model loading. |
| [EPI-OBJ-adapter-payload](#epi-obj-adapter-payload) | not determinable for external profile; none for noop | see [EPI-OBJ-adapter-payload](#epi-obj-adapter-payload) | SRC-1, `src/decapod/plugins/internalize.rs` | Noop emits empty bytes; external payload form and model application are opaque. |
| [EPI-OBJ-feedback-entry](#epi-obj-feedback-entry) | Caller feedback may assert experience | see [EPI-OBJ-feedback-entry](#epi-obj-feedback-entry) | SRC-1, `src/decapod/plugins/feedback.rs` | Source truth and human authorship unresolved. |
| [EPI-OBJ-preference-proposal](#epi-obj-preference-proposal) | Quoted feedback; rule placeholder is non-truth-apt policy text | see [EPI-OBJ-preference-proposal](#epi-obj-preference-proposal) | SRC-1, `src/decapod/plugins/feedback.rs` | No actual inferred rule or installed policy in the placeholder diff. |
| [EPI-OBJ-lcm-summary](#epi-obj-lcm-summary) | Extracted original text can carry propositions; truncated suffix may change meaning | see [EPI-OBJ-lcm-summary](#epi-obj-lcm-summary) | SRC-1, `src/decapod/plugins/lcm.rs` | Pointers preserve discoverability, not completeness or truth of summary text. |
| [RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor) | Immutable identity and controller closure facts | see [RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor) | SRC-1, `src/decapod/core/readiness_profile.rs` | Identity/closure checks do not prove semantic project correctness. |
| [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | Imported doctrine/specs; selected fragments | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | SRC-1, `src/decapod/lib.rs` | Container route cited as inventory referent; no duplicate object declaration. Warrant is that of original authored text, unknown independently. |
| [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | Alignment probability and model attribution | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | SRC-1, `src/decapod/core/decision_provider.rs` | Probability is a candidate estimate, not calibrated warrant or approval. |

## Authority-route ledger

Each row is a consequential function, not an assertion of exercised operation. All implemented rows are static implementation assessments; record-owned progression, timing, results, consumers and limits say `see` rather than redeclaring them. Checking and disposition, and retention and acceptance, are separate rows. No lifecycle-integration row is inferred from retention alone.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | check/evidence production | implemented | [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | no content change | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | Syntax/state/event structural license only | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | No evidence resolution or semantic binding | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) |
| [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | disposition/acceptance | implemented | [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | no content change | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | Operational write admission, not evidence-consuming epistemic acceptance | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | Procedural prefix gate is narrower than semantic procedural content | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) |
| [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | retention | implemented | [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | truth-apt transformation: acquisition/import | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | Source warrant unknown; imported text and labels retained | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | Merge replaces content, not semantic synthesis | see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit) |
| [EPI-RTE-promotion-record](#epi-rte-promotion-record) | retention | implemented | [EPI-OBJ-promotion-event](#epi-obj-promotion-event) | truth-apt transformation: acquisition/import | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | Approval/evidence assertions retained with unknown source warrant | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | Promotion record does not itself promote or edit a knowledge row | see [EPI-RTE-promotion-record](#epi-rte-promotion-record) |
| [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | operational admission/selection/consumption | implemented | [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | no content change | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | Active/temporal/recency selection does not endorse truth | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | none | see [EPI-RTE-knowledge-select](#epi-rte-knowledge-select) |
| [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | disposition/acceptance | implemented | [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) | no content change | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | Expiry removes reliance availability without truth assessment | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) | SRC-1, `src/decapod/plugins/knowledge.rs` | none | none | see [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw) |
| [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | check/evidence production | implemented | [EPI-OBJ-eval-verdict](#epi-obj-eval-verdict) | no content change | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | Checks JSON/plan contract, not task success | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | SRC-1, `src/decapod/plugins/eval.rs` | [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | Judge model label is metadata, not a model invocation | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) |
| [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | retention | implemented | [EPI-OBJ-eval-verdict](#epi-obj-eval-verdict) | truth-apt transformation: acquisition/import | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | External success/explanation warrant unknown | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) | SRC-1, `src/decapod/plugins/eval.rs` | [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | none | see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import) |
| [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | content transformation | implemented | [EPI-OBJ-eval-aggregate](#epi-obj-eval-aggregate) | truth-apt transformation: entailed derivation | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | Rates and bootstrap endpoints follow imported binary scores and configured algorithm, not population truth | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) | SRC-1, `src/decapod/plugins/eval.rs` | [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | Sampling/causal attribution unestablished | see [EPI-RTE-eval-statistics](#epi-rte-eval-statistics) |
| [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | check/evidence production | implemented | [EPI-OBJ-eval-aggregate](#epi-obj-eval-aggregate) | no content change | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | Named aggregate thresholds only | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | SRC-1, `src/decapod/plugins/eval.rs` | [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | Upper CI endpoint test is not proof of non-regression | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) |
| [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | operational admission/selection/consumption | implemented | [EPI-OBJ-eval-aggregate](#epi-obj-eval-aggregate) | no content change | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | Permits or blocks covered publication; no task/mechanism/transfer warrant | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | SRC-1, `src/decapod/plugins/eval.rs` | [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | Optional required marker; no candidate binding at this helper | see [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) |
| [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | content transformation | implemented | [EPI-OBJ-adapter-payload](#epi-obj-adapter-payload) | truth-apt transformation: indeterminate | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | No semantic license; noop is non-truth-apt empty payload, external profiles opaque | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | SRC-1, `src/decapod/plugins/internalize.rs` | [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | Semantic preservation versus generation cannot be classified for external executable | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) |
| [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | retention | implemented | [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | non-truth-apt policy/content update: artifact and manifest cache | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | Retains hashes/claims, not acceptance of source propositions | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | SRC-1, `src/decapod/plugins/internalize.rs` | [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | none | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) |
| [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | check/evidence production | implemented | [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | no content change | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | Hash/source/TTL/metadata consistency only | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | SRC-1, `src/decapod/plugins/internalize.rs` | [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | Replayability metadata check does not execute replay | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) |
| [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | operational admission/selection/consumption | implemented | [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | no content change | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | Mount metadata permission, not observed model loading | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | SRC-1, `src/decapod/plugins/internalize.rs` | [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | Unavailable source can attach with best-effort status | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) |
| [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | lineage/freshness/recovery | implemented | [EPI-OBJ-internalization-manifest](#epi-obj-internalization-manifest) | no content change | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | Detach removes mount file; no demonstrated parameter rollback | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | SRC-1, `src/decapod/plugins/internalize.rs` | [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | none | see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) |
| [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | content transformation | implemented | [EPI-OBJ-preference-proposal](#epi-obj-preference-proposal) | truth-apt transformation: non-ampliative reshaping | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | Feedback quotes packaged; rule placeholder is non-truth-apt policy, not derived knowledge | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) | SRC-1, `src/decapod/plugins/feedback.rs` | none | none | see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal) |
| [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | content transformation | implemented | [EPI-OBJ-lcm-summary](#epi-obj-lcm-summary) | truth-apt transformation: indeterminate | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | Below budget: ordered/labeled extraction; above budget: prefix can omit qualifications | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | SRC-1, `src/decapod/plugins/lcm.rs` | none | Determinism alone does not establish semantic preservation | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) |
| [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | retention | implemented | [EPI-OBJ-lcm-summary](#epi-obj-lcm-summary) | no content change | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | Summary/pointers retained without epistemic acceptance | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) | SRC-1, `src/decapod/plugins/lcm.rs` | none | none | see [EPI-RTE-lcm-summary](#epi-rte-lcm-summary) |
| [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | check/evidence production | implemented | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | no content change | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | Matched-marker facts only; not general safety | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | SRC-1, `src/decapod/core/agent_eval.rs` | none | none | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) |
| [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | operational admission/selection/consumption | implemented | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | no content change | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | CLI error and host stop instruction, not control of later tools | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) | SRC-1, `src/decapod/core/agent_eval.rs` | none | none | see [RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval) |
| [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | content transformation | implemented | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | truth-apt transformation: non-ampliative reshaping | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | Selection/deduplication does not add warrant to source doctrine/specs | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | SRC-1, `src/decapod/core/docs.rs` | none | none | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) |
| [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | operational admission/selection/consumption | implemented | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | no content change | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | Advisory text delivery and awareness state, not semantic obedience | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) | SRC-1, `src/decapod/core/docs.rs` | none | none | see [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve) |
| [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | check/evidence production | implemented | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | truth-apt transformation: indeterminate | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | Opaque probabilistic estimate, not acceptance or proof | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | SRC-1, `src/decapod/core/decision_provider.rs` | none | none | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) |
| [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | retention | implemented | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | no content change | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | History of observations, not integrated accepted claims | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) | SRC-1, `src/decapod/core/assurance.rs` | none | none | see [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) |
| [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | check/evidence production | implemented | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | no content change | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | Configured proof outcomes bounded by tests/controller domain | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) | SRC-1, `src/decapod/core/validation_runtime.rs` | [EPI-CLM-checked-work](#epi-clm-checked-work) | none | see [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) |
| [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | operational admission/selection/consumption | implemented | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | no content change | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | Exact-candidate readiness and remote identity scope only | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | SRC-1, `src/decapod/core/workspace.rs` | [EPI-CLM-checked-work](#epi-clm-checked-work) | none | see [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) |
| [RT-RTE-release-update](runtime.md#rt-rte-release-update) | operational admission/selection/consumption | implemented | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | non-truth-apt policy/content update: installed executable replacement | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | Registry version/install status, not evidence-directed improvement | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) | SRC-1, `src/decapod/lib.rs` | none | none | see [RT-RTE-release-update](runtime.md#rt-rte-release-update) |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-checked-work](#epi-clm-checked-work) | see [EPI-CLM-checked-work](#epi-clm-checked-work) | see [EPI-CLM-checked-work](#epi-clm-checked-work) | see [EPI-CLM-checked-work](#epi-clm-checked-work) | [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate); [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish) | none supplied | No universal semantic correctness, test adequacy or host interception | Configured proof and current-candidate/remote verification on governed surfaces | No universal semantic correctness, test adequacy or host interception |
| [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | see [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | see [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | see [EPI-CLM-eval-promotion](#epi-clm-eval-promotion) | [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import); [EPI-RTE-eval-statistics](#epi-rte-eval-statistics); [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate) | none supplied | Imported verdict provenance, sampling and component causality unestablished; wide CI can pass | Conditional binary-score aggregation and optional publication threshold gate | Imported verdict provenance, sampling and component causality unestablished; wide CI can pass |
| [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | see [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | see [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | see [EPI-CLM-adapter-replay](#epi-clm-adapter-replay) | [EPI-RTE-internalization-flow](#epi-rte-internalization-flow) | none supplied | No actual replay comparison; cache key omits binary hash; missing source can remain best-effort | Declared deterministic profile and nonempty binary hash qualify metadata | No actual replay comparison; cache key omits binary hash; missing source can remain best-effort |
| [RT-CLM-session-auth](runtime.md#rt-clm-session-auth) | see [RT-CLM-session-auth](runtime.md#rt-clm-session-auth) | see [RT-CLM-session-auth](runtime.md#rt-clm-session-auth) | see [RT-CLM-session-auth](runtime.md#rt-clm-session-auth) | [RT-RTE-session-custody](runtime.md#rt-rte-session-custody) | none supplied | Auto-reacquisition and exemptions qualify barrier | Custody machinery, not universal approval | see [RT-RTE-session-custody](runtime.md#rt-rte-session-custody) |

## Bounded conclusion

Decapod implements several different authority paths, not one truth oracle. Knowledge content and promotion assertions are imported with unknown source warrant. The procedural-prefix firewall checks a recorded event's shape but does not resolve evidence, authenticate its approver or establish semantic identity between event and newly admitted content. Active status is a retrieval eligibility label; supersession can withdraw availability without establishing falsity. The implemented library expiry algorithm can also withdraw availability if invoked, but no shipped decay caller was established; search does not itself expire rows. Retention is not lifecycle integration after evidence-consuming acceptance (see [EPI-RTE-knowledge-admit](#epi-rte-knowledge-admit), [EPI-RTE-promotion-record](#epi-rte-promotion-record), [EPI-RTE-knowledge-select](#epi-rte-knowledge-select), [EPI-RTE-knowledge-withdraw](#epi-rte-knowledge-withdraw)).

Evaluation imports success judgments, derives statistics within a fixed numerical domain and can enforce aggregate thresholds on publication. Its criterion is minimum sample counts, positive bootstrap iterations, zero recorded timeouts and no upper CI endpoint below the configured negative regression tolerance. That grants operational authority over the covered publisher, not acceptance of a general causal improvement claim. The inspected counterexample is an interval crossing zero: with sufficient counts and no timeout it can pass even with a negative lower endpoint. Neither the judge label nor the interval authenticates task outcomes or identifies a component effect (see [EPI-RTE-eval-judge-import](#epi-rte-eval-judge-import), [EPI-RTE-eval-statistics](#epi-rte-eval-statistics), [EPI-RTE-eval-promotion-gate](#epi-rte-eval-promotion-gate)).

Internalization separately checks byte lineage and metadata before recording mounts. Noop discards all source content into an empty adapter. External profiles can produce opaque bytes; accessible code cannot determine their semantic content or parameter change. Attachment writes metadata and allows best-effort source unavailability; it does not establish that a model loaded the artifact, that scopes are enforced inside a model, that replay succeeds or that detach reverses parameter changes (see [EPI-RTE-internalization-flow](#epi-rte-internalization-flow)). Jev's mutable remote alias and inaccessible parameters retain the runtime's independent uncertainty; finite probability/type checks do not calibrate alignment truth (see [RT-CMP-jev](runtime.md#rt-cmp-jev), [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe)).

Feedback proposals and LCM summaries have different force: the former quotes feedback and emits a literal non-binding rule placeholder; the latter stores ordered source extracts/pointers and can truncate meaning. Neither constitutes an evidence-consuming acceptance decision or observed behavior adaptation (see [EPI-RTE-feedback-proposal](#epi-rte-feedback-proposal), [EPI-RTE-lcm-summary](#epi-rte-lcm-summary)). Context delivery is guidance to the host; readiness gates enforce covered publication and bind proof to current artifacts. Checks license only their configured domain, not source truth, test adequacy or correctness outside the governed path (see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery), [RT-BAP-readiness-gates](runtime.md#rt-bap-readiness-gates)).

No accepted ampliative claim is established by these inspected routes. This is a bounded result, not an absence across all Decapod operations: federation status/decision handling, aptitude consolidation, other QA/proof operations and remote drivers remain unassessed. Formulated theory criticism, iterative theory building, improved future capacity and exercised self-improvement are independently unestablished here; neither raw history nor a gate substitutes for their evidence. Readiness can reject failed proof and the host can revise work, but no supplied run traces content-directed criticism through a retained revision and later causal use. The installer changes machinery on version selection, independently of evidence-responsive self-improvement. No system-wide epistemic score follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-knowledge-entry
Label: KnowledgeEntry

Source-native identity: KnowledgeEntry. Natural-language title/content with symbolic identity, provenance, status, expiry and supersession fields; SQLite knowledge table under store root. Provenance syntax and active status are not source truth; source warrant unknown. Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-promotion-event
Label: KnowledgePromotionEvent

Source-native identity: KnowledgePromotionEvent. Natural-language reason and symbolic approval/evidence-reference fields; serialized JSON in the knowledge event stream of decapod.db. Strings do not authenticate approval, resolve evidence or bind procedural content semantically. Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-eval-artifacts
Label: Evaluation artifact family

Source-native identity: Evaluation artifact family. Container of symbolic plan/run/verdict/aggregate identities with judgment prose, on filesystem under eval/. Its operative verdict and aggregate parts are declared separately below. Parts have distinct content and consumers; container alone confers no warrant. Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-eval-verdict
Label: EvalVerdict

Source-native identity: EvalVerdict. Natural-language explanation/failure reason with symbolic success, model attribution, plan/run IDs and hashes in verdict JSON. Aggregate consumes success under fixed binary rules; explanation is host-readable, not a computational justification for the aggregate. External judge warrant unknown; contract checking does not judge task truth. Operative subpart of the evaluation artifact family. Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-eval-aggregate
Label: EvalAggregate

Source-native identity: EvalAggregate. Symbolic counts/rates/percentile endpoints/settings/hash in aggregate JSON under eval/aggregates, consumed by numerical gate predicates. Numerical derivation conditional on imported verdicts, sampling design and settings. Operative subpart of the evaluation artifact family. Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-internalization-manifest
Label: InternalizationManifest

Source-native identity: InternalizationManifest. Symbolic manifest/lease JSON on filesystem under managed/artifacts/internalizations and managed/sessions. Source identity, TTL, replay class and adapter hash have fixed inspection/attachment consumers. Model ID is caller text, not verified weights identity. Metadata checks do not establish adapter semantics or model loading. Evidence: SRC-1, `src/decapod/plugins/internalize.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-adapter-payload
Label: adapter.bin

Source-native identity: adapter.bin. Opaque adapter.bin on filesystem under managed/artifacts/internalizations. Representation is not determinable for external executable output; noop bytes are empty, not distributed parameters. Creation can write payload, but actual parameter loading/change, exact weights pin and endpoint resolution are uninspected. Binary hash records file identity, not semantic or model warrant. Noop emits empty bytes; external payload form and model application are opaque. Evidence: SRC-1, `src/decapod/plugins/internalize.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-feedback-entry
Label: FeedbackEntry

Source-native identity: FeedbackEntry. Natural-language text with symbolic source/id/time/link fields in SQLite, reloaded by proposal generator. Source truth and human authorship unresolved. Evidence: SRC-1, `src/decapod/plugins/feedback.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-preference-proposal
Label: Preference proposal

Source-native identity: Preference proposal. Returned natural-language feedback quotations and literal policy placeholder; not persisted as SYSTEM.md or consumed by an installed rule evaluator. No actual inferred rule or installed policy in the placeholder diff. Evidence: SRC-1, `src/decapod/plugins/feedback.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

#### EPI-OBJ-lcm-summary
Label: LCM summary

Source-native identity: LCM summary. Natural-language summary text plus symbolic original hashes, scope and timestamp in SQLite; original ledger is a separate pointer target, not verified by this bounded summarizer read. Pointers preserve discoverability, not completeness or truth of summary text. Evidence: SRC-1, `src/decapod/plugins/lcm.rs` (implementation). No counterpart among supplied runtime objects after comparison: these are knowledge, evaluation, adapter and feedback/LCM parts, not custody or accepted-executor state.

### Routes

#### EPI-RTE-knowledge-admit
Label: Knowledge admission and retention

Caller proposes title/content/provenance to add_knowledge; CLI add and RPC store.upsert call the library. Code vetoes invalid provenance/status/TTL/expiry and, for IDs starting procedural/, missing or malformed promotion events. Database inserts imported text or handles merge-key conflict by replacement, supersession or rejection. Owner is code for admission; proposer identity does not prove human per-content approval. Open write requests, no answer oracle. Guidance is the field contract and supplied promotion event. Retained material is [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry). Supersession keeps old row; merge overwrites its title/content/provenance, so recovery differs. This route is distinct from supplied context retrieval/readiness routes, which neither define nor semantically accept these entries.

- Immediate return: Entry ID, action and superseded IDs, or validation/storage error.
- Later read-back: Knowledge search reloads active rows; promotion lookup reloads event metadata on procedural add.
- Delegated visibility: Calling host receives result; no reasoning delegate is spawned.
- Selection predicate: Provenance regex; controlled status/TTL; procedural/ ID prefix; active root merge-key match.
- Invalidation or expiry: Supersede changes prior status; merge replaces content/provenance and updates timestamp; expiry is separate withdrawal.
- Activation or effect: Write admission and retention occur through fixed SQL; no observed truth checking or human approval.
- Evidence limits: Procedural gate checks event class/evidence_refs/approved_by only; no content equality or source-entry binding check in add. Prefix-based gate cannot establish governance of every semantically procedural statement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation).

> if event.evidence_refs.is_empty() {
> --- `src/decapod/plugins/knowledge.rs`

> if event.approved_by.trim().is_empty() {
> --- `src/decapod/plugins/knowledge.rs`

> KnowledgeConflictPolicy::Reject => {
>                         return Err(error::DecapodError::ValidationError(
>                             "knowledge merge_key conflict: active entry already exists and on_conflict=reject"
>                                 .to_string(),
>                         ));
>                     }
> --- `src/decapod/plugins/knowledge.rs`

#### EPI-RTE-promotion-record
Label: Promotion event recording

Caller supplies source_entry_id, evidence refs, approved_by and reason; current agent supplies actor at CLI. Code requires nonempty fields, trims/sorts/deduplicates references, fixes target_class to procedural and appends [EPI-OBJ-promotion-event](#epi-obj-promotion-event). No evidence-content evaluator or expected-answer oracle is invoked. Open caller declarations; computational admission, human approval asserted as text rather than authenticated. Guidance is promotion field contract; event survives for later procedural add. No knowledge row is created or transformed here. No supplied runtime counterpart; distinct from model assurance and product publication.

- Immediate return: Promotion event or validation/storage error.
- Later read-back: add_knowledge looks up event by event ID in knowledge stream.
- Delegated visibility: CLI host sees JSON; evidence providers/approver are not called here.
- Selection predicate: Nonempty source ID, evidence list, approver, actor and reason; trim/dedup validation.
- Invalidation or expiry: uninspected — event revocation/expiry consumers beyond this function were not traced.
- Activation or effect: Append-only declaration becomes structural prerequisite for procedural-prefixed writes.
- Evidence limits: Function does not verify source entry exists, resolve refs, compare content or authenticate approval; raw event assertion is not evidence-consuming acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation).

> target_class: "procedural".to_string(),
>         evidence_refs,
>         approved_by: input.approved_by.trim().to_string(),
>         actor: input.actor.trim().to_string(),
>         reason: input.reason.trim().to_string(),
> --- `src/decapod/plugins/knowledge.rs`

#### EPI-RTE-knowledge-select
Label: Knowledge query selection

search_knowledge reads [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry), selects active substring matches, optionally filters creation time and sorts recency score. Code owns selection; host interprets returned content. This is distinct from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve): that route supplies doctrine/spec fragments and merely suggests querying retained knowledge. No source-truth oracle or candidate acceptance occurs.

- Immediate return: KnowledgeEntry list with retained provenance/status and optional score.
- Later read-back: Later query invocations reload accumulated knowledge rows.
- Delegated visibility: Calling CLI/RPC/library consumer receives text/metadata; downstream host reliance unobserved.
- Selection predicate: Title/content/provenance LIKE query, active status; optional as_of/window; recency 1/(1+age_days). CLI search uses relevance with no time filters.
- Invalidation or expiry: Superseded/deprecated/stale entries excluded; search does not itself compare expires_ts to now.
- Activation or effect: Ranking/filtering shapes delivered content, not confidence or truth.
- Evidence limits: as_of limits creation times over current active state, not reconstruction of historical supersession; no full historical truth view or automatic expiry-on-read established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation).

> WHERE (title LIKE ?1 OR content LIKE ?1 OR provenance LIKE ?1)
>                AND status = 'active'
> --- `src/decapod/plugins/knowledge.rs`

> entry.recency_score = Some(1.0 / (1.0 + age_days));
> --- `src/decapod/plugins/knowledge.rs`

#### EPI-RTE-knowledge-withdraw
Label: Knowledge expiry withdrawal

The public decay_knowledge library function affords a caller-controlled maintenance request; no shipped invocation was established. If invoked, code selects expiring active ephemeral/decay rows, marks stale unless dry_run and logs an event. Computational disposition on freshness, not evidential falsity. Open maintenance request with no answer oracle; policy string is logged, while inspected algorithm uses expiry. [EPI-OBJ-knowledge-entry](#epi-obj-knowledge-entry) remains stored for recovery/manual replacement; rollback uninspected. Distinct from runtime custody expiry and source freshness checks. Correction search at the frozen revision for `decay_knowledge` in `src/`, `assets/tools/` and `.github/` found only the declaration; direct CLI knowledge dispatch exposes add/search/promote, not decay (SRC-1, `src/decapod/lib.rs`). This agrees with the afforded decay branch of [MEM-RTE-promotion-lifecycle](memory.md#mem-rte-promotion-lifecycle); no new referent is declared.

- Immediate return: As-of/policy/dry_run, stale IDs and event ID.
- Later read-back: If decay is invoked and marks rows stale, later search excludes them; knowledge events retain the maintenance record.
- Delegated visibility: Calling host receives results, no delegated evaluator.
- Selection predicate: Active ephemeral/decay entry, non-null expiry <= supplied/default epoch.
- Invalidation or expiry: Stale status removes query eligibility; dry-run leaves status intact.
- Activation or effect: If invoked, SQL changes availability and logs result; dry-run also logs event. Shipped activation is unestablished.
- Evidence limits: No proposition comparison; no production caller found in the bounded source search, so automatic maintenance and shipped decay wiring are unestablished. Reactivation uninspected. Persistent CLI/RPC default entries are not expired by this selection. Architectural status remains implemented for the inspected algorithm, not its invocation.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/knowledge.rs` (implementation).

> if !dry_run && !stale.is_empty() {
>             for id in &stale {
>                 conn.execute(
>                     "UPDATE knowledge SET status = 'stale', updated_at = ?2 WHERE id = ?1",
>                     params![id, as_of],
>                 )?;
>             }
>         }
> --- `src/decapod/plugins/knowledge.rs`

#### EPI-RTE-eval-judge-import
Label: Evaluation judge import

QA eval Judge loads plan/run, checks plan association and parses externally supplied JSON, requires explanation, writes verdict and updates run reference. Caller proposes verdict; code vetoes malformed payload/plan mismatch but does not judge task truth. Open run-result ingestion under an evaluation plan; judge_model_id/prompt_hash are copied metadata, not an invoked answer oracle. Guidance is JudgeInput contract. [EPI-OBJ-eval-artifacts](#epi-obj-eval-artifacts) persists; correction/replacement uses file writes, no semantic rollback proven. Distinct from [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe) (live optional provider) and configured readiness proof.

- Immediate return: Verdict ID/path or contract error; delay timeout is simulated branch, not supervision of remote judge.
- Later read-back: Aggregate loads verdicts and converts success booleans to numerical scores.
- Delegated visibility: Caller supplies file/string and receives artifact receipt; no model call in inspected Judge branch.
- Selection predicate: Plan/run ID agreement, JSON decoding, nonempty explanation; one input source.
- Invalidation or expiry: Updated run/verdict files can replace prior artifacts; stale-outcome invalidation not established.
- Activation or effect: Imported decision is retained and later contributes to gate statistics.
- Evidence limits: No independently known expected task outcome; attribution to model is declared metadata. No actual execution evidence was supplied by this run.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation).

> success: input.success,
>                 explanation: input.explanation,
>                 failure_reason: input.failure_reason,
> --- `src/decapod/plugins/eval.rs`

#### EPI-RTE-eval-statistics
Label: Evaluation statistics derivation

Aggregate loads plan, runs and verdicts; success booleans become 1/0, computes means, difference and seeded bootstrap percentile endpoints, then writes aggregate JSON. Code owns calculation; caller chooses variants/iterations and can acknowledge plan drift when comparing a prior aggregate. Bounded numerical comparison, not causal experiment. No task oracle beyond imported verdict values. Distinct material statistics part of [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate) ecosystem, but not the configured readiness proof referent; new operation omitted from runtime account. For a concrete deduction, five baseline scores all 0 and five candidate scores all 1 yield baseline mean 0, candidate mean 1 and every resampled delta 1 for positive iterations, hence both endpoints 1. This is entailed within algorithm inputs; it does not establish those task outcomes are true.

- Immediate return: Aggregate ID/path, delta, interval and counts; rejects empty variant samples and unacknowledged prior-plan mismatch.
- Later read-back: Gate and publication verification reload aggregate.
- Delegated visibility: Host receives numerical artifact; no remote evaluator is invoked.
- Selection predicate: Runs for plan/variant with available verdict; binary success, configured seed and iterations.
- Invalidation or expiry: Aggregate computation generates new file/hash; no universal current-code binding at this operation.
- Activation or effect: Derived values become gate inputs, not a learned policy or general mechanism explanation.
- Evidence limits: Sampling independence, representative tasks, judge validity, settings drift and causal treatment/control not established by artifact structure.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation).

> out.push(if verdict.success { 1.0 } else { 0.0 });
> --- `src/decapod/plugins/eval.rs`

> samples.push((c_sum / n_c as f64) - (b_sum / n_b as f64));
> --- `src/decapod/plugins/eval.rs`

#### EPI-RTE-eval-promotion-gate
Label: Evaluation publication gate

Caller selects aggregate/min_runs/max_regression and optional mark_required; code computes pass/reasons and can persist EvalGateRequirement. Publisher reloads marked aggregate and recomputes decision. Proposer chooses evidence and threshold; software vetoes covered publication, human per-content approval unresolved. Bounded evaluation/promotion mode with imported success judgments rather than independent answer oracle. Guidance is count/iteration/timeout/regression criteria. No marker means helper returns success; failed gate can still be marked required. Recovery is new evidence/settings/requirement and retry; no automatic rollback of published product. Distinct gate within [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish), not replacement for exact-candidate readiness.

Part of: [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish)

- Immediate return: Pass/reasons and nonzero on failed CLI gate; publication helper returns error on failing required aggregate.
- Later read-back: Publication reads required marker and aggregate on subsequent calls.
- Delegated visibility: Publisher receives Result/error; host receives remediation/status.
- Selection predicate: Both counts >= min_runs; iterations > 0; recorded judge timeouts zero; reject only if ci_high < -max_regression.
- Invalidation or expiry: No requirement => no gate; re-evaluates stored fields rather than trusting decision_at_mark.
- Activation or effect: Enforcing control-flow veto of covered publisher before push; not automatic installation or model policy update.
- Evidence limits: Upper-bound criterion does not demand lower CI >= 0. Helper does not bind aggregate to current code or reauthenticate underlying runs; separate current-candidate readiness still applies.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/eval.rs` (implementation).

> if aggregate.ci_high < -max_regression {
> --- `src/decapod/plugins/eval.rs`

> eval::verify_eval_gate_for_publish(&repo_root.join(".decapod").join("data"))?;
> --- `src/decapod/core/workspace.rs`

#### EPI-RTE-internalization-flow
Label: Internalization artifact lifecycle

Caller selects local source/model/profile/scopes/TTL; code hashes source/profile executable, caches by request binding, executes noop or external binary, hashes adapter and stores manifest. Inspect checks source/adapter hash, TTL and replay metadata. Attach rejects expiry, mismatch, corrupt adapter, inconsistent replay metadata or forbidden tool, then writes session mount/log; detach removes mount. Code proposes metadata and vetoes invalid attachment, caller configures executable/model; human content approval unresolved. Open artifact requests, no answer oracle or semantic evaluator. Guidance is profile/capability contract and metadata policy. Existing manifest cache returns without fresh inspect; request ID omits binary_hash although manifest records it. Recovery is rejection/recreate or detach metadata, not proven model rollback. No runtime counterpart after comparison: the supplied workspace-container record describes filesystem preparation, not evidence of internalization adapter loading.

Concrete implementation deduction: on successful cache-miss execution, builtin:noop writes empty adapter.bin regardless of the local source's propositions. Hence noop cannot preserve or infer their content. External executable transformation remains indeterminate: extraction, parameter training and generation require inspecting that executable and its consumers.

- Immediate return: Create manifest/hashes/cache result; inspect status/integrity; attach lease; detach success or typed failure.
- Later read-back: Inspect/attach read saved manifest/adapter; later mount consumer/model loader uninspected.
- Delegated visibility: External executable gets source_path/base_model/output_dir/params; host receives manifest or lease. No weights or inference-loader handoff is shown by attach.
- Selection predicate: Local source on create; profile name/config; artifact ID; hashes/TTL/replay-class/tool-permission on attach.
- Invalidation or expiry: TTL invalidates attachment; source mismatch blocks, unavailable source is best-effort; detach deletes mount but retains artifact.
- Activation or effect: Artifact/manifest and mount/log files written; no observed model loading or parameter adaptation.
- Evidence limits: Checks license byte consistency, not source truth, semantic preservation, replay execution, capability enforcement by host or exact model pin. External binary/parameters uninspected; distributed-parametric form/change cannot be inferred from adapter name.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/internalize.rs` (implementation).

> crate::core::fs_permissions::write_private(&adapter_file, b"")
>                 .map_err(InternalizeError::Io)?;
>             return Ok((adapter_file, self.default_params.clone()));
> --- `src/decapod/plugins/internalize.rs`

> ReplayClass::Replayable => {
>             manifest.determinism_class == DeterminismClass::Deterministic
>                 && !manifest.binary_hash.trim().is_empty()
>         }
> --- `src/decapod/plugins/internalize.rs`

> return Ok((false, "best-effort-source-unavailable".to_string()));
> --- `src/decapod/plugins/internalize.rs`

#### EPI-RTE-feedback-proposal
Label: Feedback preference proposal

add_feedback imports caller text; propose_prefs retrieves latest ten rows, quotes their id/source/text and appends literal placeholder diff. Code owns selection/rendering; caller/human must decide any real rule change. Non-binding open proposal, no answer oracle or semantic inference. Guidance is fixed template; feedback persists, proposal returned rather than installed. Distinct from runtime context resolve and release update; no automatic product/instruction admission, rollback or file edit at this path.

- Immediate return: Feedback ID or proposal string; no-feedback message if empty.
- Later read-back: Proposal invocation reads feedback accumulated in earlier calls.
- Delegated visibility: Calling host sees evidence quotes and non-binding placeholder.
- Selection predicate: ORDER BY created_at DESC LIMIT 10; links are loaded but not rendered in evidence list.
- Invalidation or expiry: uninspected — feedback deletion/versioning outside these functions not traced.
- Activation or effect: add_feedback writes accumulated text to SQLite; propose_prefs returns a template, not an installed rule. Behavioral adoption is unobserved.
- Evidence limits: Template says derived but computes no new semantic rule; neither learned preferences nor accepted knowledge established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/feedback.rs` (implementation).

> // This generates a proposal text based on feedback.
>     // It MUST NOT edit files directly.
> --- `src/decapod/plugins/feedback.rs`

> - [Placeholder rule]
> + [New rule derived from feedback]
> --- `src/decapod/plugins/feedback.rs`

#### EPI-RTE-lcm-summary
Label: LCM summary transformation

summarize reads ledger events, sorts timestamps, optionally filters most recent session, formats kind/time/content, joins lines, slices first 65536 bytes if oversized, hashes original hashes plus text and stores summary. Code owns reshape/retention; no semantic evaluator, human approval or expected-answer oracle. Open summarization under scope selection. Guidance is fixed formatting/budget rule; summary and original hashes persist for later summary display. Distinct from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve), whose fragments are doctrine/specs. Concrete deduction: two below-budget events (kind=tool, ts=1, content="A is true") and (kind=tool, ts=2, content="B is false") become "[tool:1] A is true\n[tool:2] B is false". This is non-ampliative formatting for those complete inputs, not new knowledge. If a qualification lies past byte 65536, delivered prefix omits it; arbitrary UTF-8 slicing may fail at a non-character boundary. Thus oversized summaries cannot be classified as universally meaning-preserving.

- Immediate return: Summary hash/scope/count/token estimate/time, or no-originals message.
- Later read-back: CLI summary uses show_summary to return stored summary with original hashes; full downstream model use uninspected.
- Delegated visibility: Host receives summary/pointers on request; no summarizing model call.
- Selection predicate: Chronological order, scope=session newest session ID if present, otherwise all events; 64KB byte prefix.
- Invalidation or expiry: Resummarization writes by derived hash; originals intended separate; integrity/rebuild guarantees uninspected here.
- Activation or effect: Deterministic compressed extract and pointers retained, no observed epistemic acceptance or host activation.
- Evidence limits: Whole semantic preservation not guaranteed by determinism/hash; full ingest provenance and ledger integrity routes uninspected. Recovering original content through pointers requires separate reader, not implied completeness of summary.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/decapod/plugins/lcm.rs` (implementation).

> .map(|e| format!("[{}:{}] {}", e.kind, e.ts, e.content))
>         .collect::<Vec<_>>()
>         .join("\n");
> --- `src/decapod/plugins/lcm.rs`

> let summary_text = if concatenated.len() > budget {
>         concatenated[..budget].to_string()
>     } else {
>         concatenated
>     };
> --- `src/decapod/plugins/lcm.rs`

### Claims

#### EPI-CLM-checked-work
Label: Checked work claim

Claimed operation: Built-in validation ties results to current change and required checks; missing proof keeps work unverified. Source: SRC-1, `README.md` (doctrine/design expressed in public prose or executable schema/metadata). No counterpart among supplied runtime claims after comparison: session-auth is custody, not these proof/evaluation/replay assertions.

> 6. **Know what has been checked.** Built-in validation ties results to the current change and the project's required checks. Missing required proof keeps the work unverified; Jev can add advisory input.
> --- `README.md`

#### EPI-CLM-eval-promotion
Label: Evaluation promotion gate claim

Claimed operation: Schema calls subsystem variance-aware evaluation artifacts and promotion gates. Source: SRC-1, `src/decapod/plugins/eval.rs` (doctrine/design expressed in public prose or executable schema/metadata). No counterpart among supplied runtime claims after comparison: session-auth is custody, not these proof/evaluation/replay assertions.

> "description": "Variance-aware evaluation artifacts and promotion gates",
> --- `src/decapod/plugins/eval.rs`

#### EPI-CLM-adapter-replay
Label: Adapter replayability claim

Claimed operation: Replay recipe labels deterministic profile with pinned binary hash as replayable. Source: SRC-1, `src/decapod/plugins/internalize.rs` (doctrine/design expressed in public prose or executable schema/metadata). No counterpart among supplied runtime claims after comparison: session-auth is custody, not these proof/evaluation/replay assertions.

> "deterministic profile with pinned binary hash".to_string(),
> --- `src/decapod/plugins/internalize.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
