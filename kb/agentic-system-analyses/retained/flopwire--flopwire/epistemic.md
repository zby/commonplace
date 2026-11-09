---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Flopwire epistemic routes: transcript evidence, commit observations, scoped checks and later reliance"
run-id: AAS-2026-10-20-flopwire-184bd013bba1-01
reviewed-boundary: "057a4b87603cc878e81d9eb49298ddc4eb9eeb23"
---

# Flopwire epistemic report

## Source-and-claim boundary

This assesses how retained conversations and messages become evidence for later agents, and what checks license that reliance. Scope, external dependencies and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All new source reads below are SRC-1 at the frozen commit. They supply implementation or attributed doctrine/design, not observed runs. The supplied runtime orders the investigation but does not bound it.

The material distinction is between evidence that a transcript reports something and evidence that its subject is true. History retrieval imports claims; lexical ranking does not accept them. Commit observation extraction adds a narrower programmatic check with addressed command/result provenance. No source supplied here authenticates arbitrary transcript statements against the outside world. This is a limit on those routes, not a system-complete negative about all shipped operations.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| CLI dispatch and MCP registry | `cmd/flopwire/main.go`, `cmd/flopwire/mcp.go` | Direct dispatch/registry reads; supplied runtime covers retrieval, agent, serve, messaging, hook, upgrade and trial | Registration is not observed invocation |
| Agent extraction and shared upload | `internal/agent/index.go`, `internal/devicesync/syncer.go` | Supplied [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index), [RT-RTE-shared-upload](runtime.md#rt-rte-shared-upload) | All parser and remote admission implementations not independently audited here; no universal source-fidelity conclusion |
| Search, grep, sessions, read, raw | `cmd/flopwire/mcp.go`, `internal/retrieval/format/render.go`, `internal/retrieval/format/text.go` | Registry, rendering call sites and complete text transformations directly read; [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval), [EPI-RTE-text-render](#epi-rte-text-render) | Ranking quality and complete chronology unobserved |
| Digest and outline | `internal/digest/digest.go`, `internal/retrieval/format/summary.go` | Direct digest declarations/Fold and full summary renderer; [EPI-OBJ-digest](#epi-obj-digest), [EPI-RTE-digest-fold](#epi-rte-digest-fold) | Other fold helpers not fully inspected; no semantic-summary accuracy guarantee |
| Commit change/trace and MCP change | `cmd/flopwire/change.go`, `internal/digest/evidence.go`, `internal/digest/evidence_stream.go`, `internal/digest/commits.go`, `internal/ingest/commit_evidence.go`, `internal/retrieval/change.go`, `internal/retrieval/local/change.go` | Direct complete extraction state machine and projection, selected command parser and lookup ranges; [EPI-RTE-commit-check](#epi-rte-commit-check), [EPI-RTE-commit-store](#epi-rte-commit-store), [EPI-RTE-change-lookup](#epi-rte-change-lookup) | Shell grammar/helper coverage partial; no exhaustive spoof resistance or sole-authorship claim |
| Hook and alternate delivery; retained threads | `plugins/codex/flopwire/hooks/hooks.json`, `plugins/codex/flopwire/skills/messaging/SKILL.md` | Direct hook manifest and full skill; supplied [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery), [RT-RTE-adapter-delivery](runtime.md#rt-rte-adapter-delivery) | Bus backend/thread visibility not independently inspected; delivery is not agreement or authorization |
| Redact CLI and local withdrawal | `cmd/flopwire/redact.go`, `internal/localindex/redact.go`, `internal/redact/redact.go` | Direct complete CLI, local maskRow/maskDigest and scanner opening; [EPI-RTE-index-redact](#epi-rte-index-redact) | Remote archive rewrite, tombstone replay and all secret rules not fully audited; no total erasure or secret-removal guarantee |
| Policy, sender admission, binary installation | `internal/api/api.go`, `internal/api/bus.go`, `internal/upgrade/upgrade.go` | Supplied [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission), [RT-RTE-binary-upgrade](runtime.md#rt-rte-binary-upgrade) | Operational checks have narrower domains than truth or improvement |
| Qualification and parser oracle | `scripts/qualify-agent-workflow.py`, `testdata/oracle/README.md`, `internal/transcript/oracle/oracle.go` | Direct qualification check body, oracle contract and Assert; [RT-RTE-workflow-trial](runtime.md#rt-rte-workflow-trial), [EPI-RTE-parser-parity](#epi-rte-parser-parity) | Other probe/bench/acceptance/nightly and source-native reports remain unassessed here; no complete evaluator inventory or global negative |
| Backup/verify/restore, import, setup, admin/deletion and web administration | `cmd/flopwire/main.go` | Direct dispatch coverage; boundary and runtime identify shipped responsibilities | Handler internals not independently traced here. Prevents system-complete absence claims about acceptance, recovery and withdrawal |

The consequential claim found is [RT-CLM-recovery-evidence](runtime.md#rt-clm-recovery-evidence). Additional tool guidance is declared as [EPI-CLM-commit-evidence](#epi-clm-commit-evidence). No live harness trace, independently verified task outcome or causal comparison was supplied. These gaps prevent claims of exercised reliance, reliable truth recovery or improved capacity. Distributed-parametric processing is external: see [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model). Its exact parameters, mutation and endpoint resolution remain uninspected; no conclusion about parametric learning follows.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-localindex](runtime.md#rt-obj-localindex) | Imported utterances about decisions, commands and outcomes; symbolic location/state metadata | see record | SRC-1: `internal/localindex/store.go`; see record passages | A container; truth varies per utterance, and initial speaker warrant is unknown |
| [EPI-OBJ-digest](#epi-obj-digest) | Selected prompt/reply fragments and derived activity fields | see record | SRC-1: `internal/digest/digest.go` | Navigation does not certify intent, success or approval |
| [EPI-OBJ-commit-evidence](#epi-obj-commit-evidence) | A captured command/result supports a commit observation with a possibly abbreviated hash | see record | SRC-1: `internal/digest/evidence.go` | Transcript authenticity and actual repository state not independently checked |
| [RT-OBJ-standing-instruction](runtime.md#rt-obj-standing-instruction) | Primarily directives; message bodies can carry arbitrary factual claims | see record | SRC-1: `internal/busrender/busrender.go`; see record | Directives are not truth acceptance; sender identity does not establish body truth |
| [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model) | Internal truth-apt units not determinable from accessible parameters | see record | SRC-1: `scripts/qualify-agent-workflow.py`; see record | External opaque model; trial outputs are separate from parameters |

## Authority-route ledger

Route ID: [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Native transcript to indexed messages
Evaluator/condition and domain: Parser and policy; structural eligibility, not factual truth
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Rows or parse error
Implemented force: Enforcing parser/policy admission
Epistemic authority and scope: Speaker/source warrant unknown; provenance retained in addresses, not external verification
Operational authority: Makes parsed utterances queryable
Behavioral-authority path: Later CLI/MCP → selected retained text → advisory evidence → later request
Evidence source ID and local anchor: SRC-1: `internal/agent/index.go`; see cited route
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

Route ID: [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index); [RT-RTE-shared-upload](runtime.md#rt-rte-shared-upload)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)
Content/update relation: no content change
Transition or check target: Extracted rows and uploaded archive/index inputs
Evaluator/condition and domain: See routes; policy and transport constraints
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Retained local rows; shared visibility after parsing
Implemented force: Storage and eligibility enforcement
Epistemic authority and scope: Retention licenses no additional truth claim
Operational authority: Permits subsequent retrieval subject to scope
Behavioral-authority path: Retriever → durable index/archive → permissive access → later calls
Evidence source ID and local anchor: SRC-1: `internal/localindex/store.go`, `internal/devicesync/syncer.go`; see records
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

Route ID: [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Query to selected excerpts
Evaluator/condition and domain: Lexical ranking/filtering; relevance domain
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Ranked excerpts, empty/partial page or error
Implemented force: Ranking, not truth acceptance
Epistemic authority and scope: Evidence of retained text in selected scope; no global absence from empty results
Operational authority: Supplies model-visible evidence
Behavioral-authority path: External agent → tool result → advisory/ranking → current and later retained context
Evidence source ID and local anchor: SRC-1: `cmd/flopwire/mcp.go`; see record
Claim IDs: [RT-CLM-recovery-evidence](runtime.md#rt-clm-recovery-evidence)
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

Route ID: [EPI-RTE-text-render](#epi-rte-text-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Text to safe display/window
Evaluator/condition and domain: Code-point replacement and byte/line budget; display domain
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Cleaned or clipped excerpt
Implemented force: Enforcing displayed selection
Epistemic authority and scope: Preserves ordinary ASCII propositions but can remove decisive context; raw/JSON paths differ
Operational authority: Bounds what reader sees
Behavioral-authority path: Renderer → tool/hook text → advisory content → invocation
Evidence source ID and local anchor: SRC-1: `internal/retrieval/format/text.go`, `internal/retrieval/format/render.go`
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

Route ID: [EPI-RTE-digest-fold](#epi-rte-digest-fold)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-digest](#epi-obj-digest)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Prompt and reply fragments to bounded navigation fields
Evaluator/condition and domain: Ordinal and clipping rules, not semantic intent assessment
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: First selected prompt and last reply snippets
Implemented force: Selection/ranking guidance
Epistemic authority and scope: Only selected source fragments; derived counters require their separate count rules
Operational authority: Allows session navigation before full reads
Behavioral-authority path: Session/outline renderer → digest text → advisory → later query
Evidence source ID and local anchor: SRC-1: `internal/digest/digest.go`, `internal/retrieval/format/summary.go`
Claim IDs: none
Mismatch marker: none
Gap/limit: This row covers textual fields; inspected code also derives counters/commit fields, whose full semantics are not established by this classification

Route ID: [EPI-RTE-commit-check](#epi-rte-commit-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-commit-evidence](#epi-obj-commit-evidence)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Captured command/result to observed hash and execution outcome
Evaluator/condition and domain: Deterministic shell/call pairing and output grammar over one source generation/session
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Addressed observation or no event; whole-call failure can coexist with printed commit
Implemented force: Rejects unsupported pairings and limits inferred continuity
Epistemic authority and scope: Conditional derivation from captured bytes under parser rules; no independent Git authentication
Operational authority: Emits eligible observations for projection
Behavioral-authority path: Extractor → event list → enforcing evidence eligibility → next storage step
Evidence source ID and local anchor: SRC-1: `internal/digest/evidence_stream.go`, `internal/digest/evidence.go`
Claim IDs: [EPI-CLM-commit-evidence](#epi-clm-commit-evidence)
Mismatch marker: none
Gap/limit: Entailment is within the encoded transcript interpretation. External commit existence depends on truthful harness/output premises; mixed wrappers may be omitted

Route ID: [EPI-RTE-commit-store](#epi-rte-commit-store)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-commit-evidence](#epi-obj-commit-evidence)
Content/update relation: no content change
Transition or check target: Eligible observations to durable projection
Evaluator/condition and domain: Available referenced rows, active/non-superseded source, budget and transaction revision
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Inserted/kept IDs, deleted obsolete fingerprints, dirty/limited state or rollback
Implemented force: Enforcing projection consistency
Epistemic authority and scope: Retains conditional observations; does not accept historical authorship
Operational authority: Makes admitted events available to lookup
Behavioral-authority path: Projection → SQL events → permissive access → subsequent lookup
Evidence source ID and local anchor: SRC-1: `internal/ingest/commit_evidence.go`
Claim IDs: none
Mismatch marker: none
Gap/limit: A storage acceptance criterion is not evidence-consuming acceptance of a broader historical claim

Route ID: [EPI-RTE-change-lookup](#epi-rte-change-lookup)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-commit-evidence](#epi-obj-commit-evidence)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Requested full hashes to exact/prefix evidence matches
Evaluator/condition and domain: Repository visibility, prefix predicate and cursor revision; index domain
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Evidence addresses, coverage flags, restart request
Implemented force: Enforces page/scope; ranks no truth verdict
Epistemic authority and scope: Exact equality or prefix relation over stored observation; prefix does not establish uniqueness
Operational authority: Permits follow-up reads and requires restart for changed cursor state
Behavioral-authority path: Change tool → JSON addresses/flags → advisory evidence, enforcing pagination → next call
Evidence source ID and local anchor: SRC-1: `internal/retrieval/change.go`, `internal/retrieval/local/change.go`, `cmd/flopwire/change.go`
Claim IDs: [EPI-CLM-commit-evidence](#epi-clm-commit-evidence)
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

Route ID: [EPI-RTE-index-redact](#epi-rte-index-redact)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex); [EPI-OBJ-digest](#epi-obj-digest); [EPI-OBJ-commit-evidence](#epi-obj-commit-evidence)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Selected local message content and dependent metadata to masked state
Evaluator/condition and domain: Explicit requested target; masking/storage code, not a truth evaluator
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Masked row, scrubbed digest/title, FTS rebuild and refreshed change events
Implemented force: Enforcing local withdrawal
Epistemic authority and scope: Removes availability, not a finding that the content is false
Operational authority: Changes subsequent search/read/change evidence
Behavioral-authority path: Local write transaction → index/derived views → enforcing selection → later queries
Evidence source ID and local anchor: SRC-1: `internal/localindex/redact.go`, `cmd/flopwire/redact.go`
Claim IDs: none
Mismatch marker: none
Gap/limit: Native harness file and already delivered contexts remain outside this local withdrawal; remote rewrite not fully audited

Route ID: [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery); [RT-RTE-adapter-delivery](runtime.md#rt-rte-adapter-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-standing-instruction](runtime.md#rt-obj-standing-instruction)
Content/update relation: no content change
Transition or check target: Delivered envelopes to recipient context
Evaluator/condition and domain: Lease/event/budget rules; host delivery domain
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Rendered context or retry/undelivered state
Implemented force: Software delivery; model handling advisory
Epistemic authority and scope: No truth license from receipt or sender alone
Operational authority: Requests replies/actions within existing authorization
Behavioral-authority path: See [RT-BAP-message-guidance](runtime.md#rt-bap-message-guidance); model/hook or host context → advisory policy → recipient turns
Evidence source ID and local anchor: SRC-1: `internal/busrender/busrender.go`; see runtime routes
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed compliance; historical thread reads are not new direct requests

Route ID: [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission); [RT-RTE-binary-upgrade](runtime.md#rt-rte-binary-upgrade)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-standing-instruction](runtime.md#rt-obj-standing-instruction)
Content/update relation: non-truth-apt policy/content update: configuration or executable replacement
Transition or check target: Policy, sender or binary candidate
Evaluator/condition and domain: See records; credential/config validation or checksum/runnable version criteria
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Reject or persist/replace
Implemented force: Enforcing operational admission
Epistemic authority and scope: No acceptance of truth or proof of improvement
Operational authority: Changes future eligible collection/delivery or executable behavior
Behavioral-authority path: See records; daemon/server or executable loader → symbolic config/binary → enforcing → subsequent use
Evidence source ID and local anchor: SRC-1: `internal/api/api.go`, `internal/upgrade/upgrade.go`; see records
Claim IDs: none
Mismatch marker: none
Gap/limit: Separate mechanisms grouped only for their non-epistemic consequence; individual criteria and rollback limits remain in cited records

Route ID: [RT-RTE-workflow-trial](runtime.md#rt-rte-workflow-trial)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Synthetic discovery, source reading, refusal and correlated token reply
Evaluator/condition and domain: Script-owned expected token, exact session/thread IDs and transcript command checks
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Failure or completed trial report
Implemented force: Check failure raises; no automatic product promotion
Epistemic authority and scope: Conditional test result for explicit CLI resume workflow
Operational authority: Stops failed trial/report; no production admission authority
Behavioral-authority path: Script → report/exception → enforcing trial continuation, advisory maintenance → trial/review
Evidence source ID and local anchor: SRC-1: `scripts/qualify-agent-workflow.py`; see record
Claim IDs: none
Mismatch marker: none
Gap/limit: No execution evidence; script does not qualify hooks, MCP, automatic wake, arbitrary research correctness or component benefit

Route ID: [EPI-RTE-parser-parity](#epi-rte-parser-parity)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Parser conversation/message projection versus FAD synthetic expected output
Evaluator/condition and domain: Programmatic comparison after declared divergence drops; fixture parity domain
Activation and timing: On explicit request or newly eligible input; operation unobserved
Possible or observed result: Differences cause test errors
Implemented force: Enforcing test outcome
Epistemic authority and scope: Agreement on projected fixture values only; reference itself has documented limitations
Operational authority: Can fail parser tests; no runtime truth gate
Behavioral-authority path: Oracle Assert → testing error → enforcing test failure → test invocation
Evidence source ID and local anchor: SRC-1: `internal/transcript/oracle/oracle.go`, `testdata/oracle/README.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied execution or causal evidence

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-recovery-evidence](runtime.md#rt-clm-recovery-evidence) | see record | SRC-1: `plugins/codex/flopwire/skills/messaging/SKILL.md`; doctrine/design | see record and [RT-BAP-recovery-guidance](runtime.md#rt-bap-recovery-guidance) | [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval), [EPI-RTE-text-render](#epi-rte-text-render) | none supplied | No comparative outcome evidence | Implemented evidence access plus requested source/contradiction checks | Interpretation and reliable claim support depend on external reader |
| [EPI-CLM-commit-evidence](#epi-clm-commit-evidence) | see record | SRC-1: `cmd/flopwire/change.go`; doctrine/design | see record | [EPI-RTE-commit-check](#epi-rte-commit-check), [EPI-RTE-commit-store](#epi-rte-commit-store), [EPI-RTE-change-lookup](#epi-rte-change-lookup) | none supplied | No independent Git/causal verification; encoded pairing rules bound inference | Captured command/result provenance with explicit prefix and coverage limits | Sole authorship, complete enumeration and truthful underlying transcript unestablished |

## Bounded conclusion

Flopwire retains and imports conversation claims for later use; it does not thereby endorse their subject matter. Source warrant is unknown for arbitrary imported utterances. Addresses and follow-up reads preserve a path back to captured evidence, while clipping, outlines, digests and redaction reduce what a consumer sees. The shipped skill asks readers to recover decisive text and distinguish proposals from approval. Its authority is advisory at the external model, over invocations loading the guidance. See [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval), [RT-BAP-recovery-guidance](runtime.md#rt-bap-recovery-guidance), [EPI-RTE-text-render](#epi-rte-text-render) and [EPI-RTE-digest-fold](#epi-rte-digest-fold).

Commit extraction is a supported narrower derivation and check route. It links captured command/result records, rejects selected ambiguous command patterns and preserves whole-call outcome separately from observed commit output. Thus a failing shell call is not sufficient evidence that no commit occurred. Its warrant is conditional on truthful captured inputs and the inspected interpretation, not independently warranted Git facts. Projection retention and change lookup give those observations later evidential force; prefix matching still cannot license unique identity or sole authorship. See [EPI-RTE-commit-check](#epi-rte-commit-check), [EPI-RTE-commit-store](#epi-rte-commit-store) and [EPI-RTE-change-lookup](#epi-rte-change-lookup).

There is no evidence-consuming acceptance decision for an ampliative historical explanation in the inspected retrieval, digest and commit routes. This route-local result does not assert such acceptance is absent from unassessed evaluators or source-native maintenance practice. No lifecycle integration after such acceptance is established. Indexing, storage, visibility admission and operational consumption are separate functions. Local redaction withdraws content and updates derived readers; it does not retract already supplied model context or classify an assertion as false. See [EPI-RTE-index-redact](#epi-rte-index-redact).

The workflow trial and parser oracle check named synthetic targets, with operative failure consumers. Their licenses do not transfer to general research truth, reliable messaging across all hosts or improved capacity. No trial was executed in this analysis. Policy/sender gates and checksum/version tests change operational authority against specific criteria; they establish neither epistemic endorsement nor successful improvement. Delivered requests can change a recipient's tasks without a truth-apt update, but receipt is not agreement. See [RT-RTE-workflow-trial](runtime.md#rt-rte-workflow-trial), [EPI-RTE-parser-parity](#epi-rte-parser-parity), [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission), [RT-RTE-binary-upgrade](runtime.md#rt-rte-binary-upgrade) and [RT-BAP-message-guidance](runtime.md#rt-bap-message-guidance).

These findings establish retained experience access, bounded deterministic derivation and operational admission capacities. They do not establish learning as improved future capacity, content-directed theory criticism and iteration, reflection's two causal directions or exercised self-improvement. Those remain separate questions requiring route-specific evidence; opaque provider internals and absent run comparisons do not justify a bundled negative. The unassessed operations in the coverage table prevent a system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-digest
Label: Digest

Part of: [RT-OBJ-localindex](runtime.md#rt-obj-localindex)

Source-native identity: `digest.Digest`, JSON stored with conversation state. Natural-language Intent/Last snippets and symbolic counts, paths, hashes and fold bookkeeping are distinct operative parts. Text is interpreted by readers; counters and references have fixed renderer/selector rules. This is a material part of the supplied runtime's local-index container, not a replacement container. SRC-1: `internal/digest/digest.go`, `internal/retrieval/format/summary.go`.

> // Two kinds of fields make it up:
> //
> //   - Fold reads the messages a batch writes, in order: the intent (first
> //     user prompt), the last assistant message, files edited, PRs, commits
> //     and issues. Re-folding a message is harmless: these are sets, or keep
> //     the lowest (intent) or highest (last) ordinal seen.
> --- `internal/digest/digest.go`

#### EPI-OBJ-commit-evidence
Label: CommitEvidence

Source-native identity: `digest.CommitEvidence`, symbolic fields and evidence references represented as Go values and persisted JSON/SQL projection entries. Distinct from the digest's bounded commit list and the runtime's undifferentiated local-index container: this object spans local and server projections and retains command/result lineage. Closest supplied record is [RT-OBJ-localindex](runtime.md#rt-obj-localindex); it supplies the local storage container, not the cross-backend observation referent. SRC-1: `internal/digest/evidence.go`, `internal/ingest/commit_evidence.go`.

> // CommitEvidence is an observed commit, with the records supporting that observation.
> // Hash may be abbreviated. DirectoryKnown describes captured directory placement,
> // never repository identity. Outcome describes the whole execution, not commit creation.
> --- `internal/digest/evidence.go`

### Routes

#### EPI-RTE-text-render
Label: Text rendering

Part of: [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval)

Source-native `Clean`, `Cut` and renderer calls are symbolic Go transformations of text. This is the display subroute of the supplied history-retrieval route. The renderer calls Clean on message text; the bus also cleans and escapes message bodies. A concrete implementation deduction: Clean on the character sequence `A`, carriage return, newline, `B`, ESC yields `A`, newline, `B`, `␛`. Cut on `approved\nreversed` with from=1 and maxChars=8 returns `approved` with Clipped=true: omission can change a historical interpretation. These are source deductions, not executed target examples. SRC-1: `internal/retrieval/format/text.go`, `internal/retrieval/format/render.go`, `internal/busrender/busrender.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned display string or bounded excerpt
- Later read-back: inapplicable — this display function itself writes no retained result
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Selected output format and line/byte budgets
- Invalidation or expiry: inapplicable — transient output; raw/JSON branches preserve different representations
- Activation or effect: Code changes displayed characters and visible context
- Evidence limits: Does not certify semantic equivalence for all Unicode/control-dependent inputs or full context


> // characters (isBidiControl) become U+FFFD, a CR before a newline is dropped, and invalid
> // UTF-8 is replaced. JSON output never goes through Clean; it is exact.
> --- `internal/retrieval/format/text.go`

> text := Clean(m.Text)
> --- `internal/retrieval/format/render.go`

> e.Text = b.String()
> if e.From > 1 || e.To < e.Lines {
>     e.Clipped = true
> }
> --- `internal/retrieval/format/text.go`

#### EPI-RTE-digest-fold
Label: Digest folding

Part of: [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index)

Indexer-time code folds message snippets and symbolic activity into Digest; rendering supplies navigation summaries. Closest supplied route is [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index). This is its digest-specific subroute, with different output/checks from full extracted messages. User snippets use lowest eligible ordinal; assistant Last uses highest. The label Intent is not an evaluated explanation of intent. SRC-1: `internal/digest/digest.go`, `internal/retrieval/format/summary.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated Digest fields
- Later read-back: Stored conversation digest reaches later sessions/outline renderers
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Non-superseded, non-evidence-only rows; eligible user/assistant text and ordinal rules
- Invalidation or expiry: Reparse can replace same-ordinal text; local masking can scrub derived fields
- Activation or effect: Supplies shorter navigation text and activity fields
- Evidence limits: Textual selection shown directly; count/store helpers and all semantic implications are not exhaustively inspected


> case transcript.KindAssistant:
>     if t := oneLine(m.Text); t != "" {
>         if d.State == nil || d.State.LastOrd == nil || m.Ordinal >= *d.State.LastOrd {
>             d.state().LastOrd = ptr(m.Ordinal)
>             d.Last = clip(t, LastLen)
>         }
>     }
> --- `internal/digest/digest.go`

#### EPI-RTE-commit-check
Label: Commit evidence extraction

Owner: deterministic CommitEvidenceState/ExtractCommitEvidence, over source-generation/session-ordered retained messages. It pairs addressed shell calls/results, tracks running handles, invalidates open HEAD continuity on uncertain/moving commands, and emits observation events. Distinct from [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval): this produces provenance-bearing observations before retrieval, not lexical hits. Different from ordinary [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index) parsing: it checks cross-message Git evidence. SRC-1: `internal/digest/evidence.go`, `internal/digest/evidence_stream.go`, `internal/digest/commits.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New CommitEvidence events or empty list
- Later read-back: Events can enter local/server projections, then change lookup
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Typed call identity, shell grammar, safe output sources, printed hash or permitted successful HEAD reveal
- Invalidation or expiry: Superseded rows, HEAD movement and unsupported placement break inferred continuity
- Activation or effect: Emits conditional observation with command/result references and separate whole-call outcome
- Evidence limits: No external Git execution, source authentication or independent truth oracle; full shell grammar not audited

Proposer: retained captured commands/results. Decider/veto: code pairing and eligibility predicates; no per-observation human approval. Mode: open transcript evidence projection. Answer oracle: no externally provided expected commit; captured output is evidence input. This admits derived observations, not a revised explanatory theory.
> // Other programs can print convincing Git output. Reject such compound calls.
> --- `internal/digest/evidence.go`

> if p.g.printed && p.printedSafe {
>     for _, hash := range printedEvidenceHashes(out) {
>         e := base
>         e.Hash = hash
>         events = append(events, e)
>         printed = true
>     }
> }
> --- `internal/digest/evidence_stream.go`

> // Commands enrichment is best effort, including heuristic Codex event joins.
> // Parse the addressed call itself to establish command ownership.
> --- `internal/digest/evidence_stream.go`

#### EPI-RTE-commit-store
Label: Commit projection retention

Server RefreshCommitEvidence reads retained live tool rows grouped by source/generation, invokes extraction and atomically replaces the derived projection while retaining unchanged fingerprints. Closest supplied [RT-RTE-shared-upload](runtime.md#rt-rte-shared-upload) describes shared ingestion, but this is a distinct derived-evidence persistence operation. SRC-1: `internal/ingest/commit_evidence.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Transaction success, error or limited/dirty state
- Later read-back: Later shared Change queries join evidence and source/conversation visibility
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Live non-superseded rows on active path, no tombstoned source; byte/row budgets and available references
- Invalidation or expiry: Deletes fingerprints not regenerated; revision mismatch requires rollback; limits leave dirty state
- Activation or effect: Updates later available observations and preserves provenance references
- Evidence limits: Inspected server transaction only; not proof of observed crash safety or all local projection semantics

Admission trigger: parsed/dirty conversation. Proposed change: rebuilt observation set. Software decides and can reject missing referenced messages or changed snapshot; no human approval or truth oracle. Recovery: entire transaction rollback on inconsistent projection. This criterion admits storage consistency for lookup, not historical explanatory acceptance.
> // RefreshCommitEvidence atomically replaces one conversation's projection from
> // retained live rows. The caller holds its conversation row lock. Appended rows
> // can complete an older call; replay is source scoped, never cross-source.
> // Unchanged observations keep their IDs so appends do not disturb open pages.
> --- `internal/ingest/commit_evidence.go`

#### EPI-RTE-change-lookup
Label: Change lookup

Part of: [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval)

CLI/MCP change lookup selects projected observations by full requested IDs and repository scope, maps exact/prefix matches, and returns addresses plus coverage/restart state. Material part of the supplied retrieval container route; no supersession needed because that container remains valid. SRC-1: `cmd/flopwire/change.go`, `internal/retrieval/change.go`, `internal/retrieval/local/change.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON evidence addresses, match kind, coverage flags or error
- Later read-back: Reads retained observations; request itself does not persist a revised historical claim
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Repository/visibility scope, requested hash prefix equality, cursor/cutoff and budget
- Invalidation or expiry: Index/revision changes invalidate pagination; dirty/quarantined/limited states qualify coverage
- Activation or effect: Guides source reads and can refuse stale pagination
- Evidence limits: No complete-history, unique-prefix or sole-author claim; backend source inspected in bounded ranges

Selector proposer: user/model supplies IDs and repository; decider: code matches all qualifying stored prefixes. No human selection gate or expected-answer oracle. Open lookup mode. Reader still decides historical attribution after reading evidence.
> // Change returns indexed observations, including all submitted IDs that share
> // an abbreviated observation. Prefix observations never establish uniqueness.
> --- `internal/retrieval/change.go`

> if prior.Revision != cursor.Revision {
>     out.RestartRequired = true
>     return nil
> }
> --- `internal/retrieval/change.go`

#### EPI-RTE-index-redact
Label: Local index redaction

Explicit redact request routes through daemon or direct local store; local maskRow masks selected row text, digest/title and FTS entries and refreshes change events. Distinct from collection deny/rewrite described in [RT-RTE-transcript-index](runtime.md#rt-rte-transcript-index): this withdraws selected content and dependent evidence. The CLI also requests remote redaction separately; its complete server archive mechanics remain unassessed. SRC-1: `cmd/flopwire/redact.go`, `internal/localindex/redact.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Count or error; server and local results separate
- Later read-back: Subsequent local search/read/change sees masked/recomputed views
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Explicit address/line range and copy options; local target resolution
- Invalidation or expiry: Masked text replaces original in index; native file unchanged; delivered contexts not retracted
- Activation or effect: Withdraws available text and dependent projection evidence
- Evidence limits: No total secret detection or cross-device erasure guarantee; tombstone replay/remote archive implementation not fully inspected

Proposer: request principal chooses target; code resolves/masks it, with remote credential/ownership distinctions exposed by CLI. Generic caller identity does not prove human action. Explicit maintenance mode; no correctness oracle. Failure can stop the operation; server success can precede a local error. Withdrawal expresses availability control, not epistemic falsification.
> if err := w.maskDigest(t.conv, hidden); err != nil {
>     return Tombstone{}, err
> }
> --- `internal/localindex/redact.go`

> w.ftsInsert(t.id, p)
> if err := w.refreshChangeEvents(t.conv); err != nil {
>     return Tombstone{}, err
> }
> --- `internal/localindex/redact.go`

> // device's local index. The harness's own transcript file is not touched.
> --- `cmd/flopwire/redact.go`

#### EPI-RTE-parser-parity
Label: Parser parity oracle

Fixture oracle compares parser conversation/message projections to committed synthetic FAD outputs, after named divergence exclusions. Assert consumes differences as test errors. No supplied runtime record describes this comparator; closest [RT-RTE-workflow-trial](runtime.md#rt-rte-workflow-trial) is a distinct real-model synthetic messaging trial. SRC-1: `testdata/oracle/README.md`, `internal/transcript/oracle/oracle.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Test errors for differences
- Later read-back: inapplicable — this test comparator does not itself install retained runtime content
- Delegated visibility: inapplicable — this subroute does not delegate a model task; host delivery remains in supplied runtime routes
- Selection predicate: Explicit parser test invocation, fixture and projection/divergence rules
- Invalidation or expiry: Fixture/reference edits change comparison; excluded divergences limit target
- Activation or effect: Test failure/reporting, not runtime admission of utterance truth
- Evidence limits: No tests executed; reference parser has documented limits; no production outcome or causal comparison

Proposer: fixture/test author. Decider: projected differential comparator; maintainer chooses expected output and divergences. Answer oracle: committed FAD 0.3.1 expected values, subject to declared limitations. Bounded test mode, not open historical interpretation; failure rejects the test outcome, not automatically the installed binary.
> // Assert reports Diff's problems on t, prefixed with the expected file name.
> func Assert(t testing.TB, f File, exp Conversation, conv *transcript.Conversation, msgs []*transcript.Message, rules Rules) {
>     t.Helper()
>     for _, p := range Diff(exp, conv, msgs, rules) {
>         t.Errorf("%s: %s", f.Name, p)
>     }
> }
> --- `internal/transcript/oracle/oracle.go`

> Every fixture here is synthetic. Never copy real transcript content into this
> tree.
> --- `testdata/oracle/README.md`

### Claims

#### EPI-CLM-commit-evidence
Label: Captured commit evidence

The MCP change tool promises sessions with captured evidence and source addresses, while explicitly withholding prefix uniqueness. This narrows rather than contradicts [RT-CLM-recovery-evidence](runtime.md#rt-clm-recovery-evidence): it addresses change provenance, not arbitrary research recovery. SRC-1: `cmd/flopwire/change.go`; doctrine/design tool description implemented by the lookup/extractor routes.

> Read the evidence before attributing a change; a prefix observation remains a prefix match.
> --- `cmd/flopwire/change.go`

> hint := "Read relevant command/result addresses, compare the evidence with the requested claim, and state remaining gaps."
> --- `cmd/flopwire/change.go`
