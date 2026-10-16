---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Tracecraft epistemic routes: caller assertions, transcript transformations, coordination authority and bounded storage evaluators."
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
reviewed-boundary: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
---

# Tracecraft epistemic report

## Source-and-claim boundary

The question is whether Tracecraft checks retained content for truth, or instead preserves caller content and gives coordination state operational force. Scope, exclusions and source identity are see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register), SRC-1. External model hosts, backend internals and actual deployment grants remain excluded. Their missing evidence prevents conclusions about model reasoning, downstream compliance and universal service guarantees. No external model parameters are exposed by these SDK paths; external-host learning is not determinable from them.

This is a sparse overlay on the supplied runtime records. Direct inspection below checks dispatch and selected transformations/evaluators against that provisional account. No target execution occurred. Raw benchmark results and generated reports remain available but uninspected: numerical performance, observed invariants and causal benefit are not established here. Actual memory/message/artifact/transcript instances were not supplied, so individual propositions, their original sources and their truth are not determinable. Architecture can nevertheless be traced.

| Entry point or operation | SRC-1 source path | Coverage and evidence basis | Limit and conclusion prevented |
|---|---|---|---|
| CLI registration | `sdk/tracecraft/cli/__init__.py` | Direct complete read; registered operations match supplied runtime | No additional model tool registry or content evaluator exposed in this dispatch |
| Init, backend and direct writes | `sdk/tracecraft/store.py`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`, `sdk/tracecraft/cli/init_cmd.py` | Supplied [RT-RTE-init-config](runtime.md#rt-rte-init-config), [RT-CMP-get-store](runtime.md#rt-cmp-get-store) | Service authentication and deployed conditional-write behavior unobserved; direct writes bypass CLI checks |
| Memory set/get/history/list | `sdk/tracecraft/cli/memory.py` | Direct complete read; [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | No value-level semantic criterion in this path; attribution strings are not authenticated authorship |
| Send/inbox/delete and cursor | `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/protocol.py` | Supplied [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) | No independent inspection of all cursor branches here; no system-complete delivery guarantee |
| Claim/complete/status/wait and git evidence | `sdk/tracecraft/cli/steps.py` | Direct complete read; [RT-RTE-step-control](runtime.md#rt-rte-step-control), [EPI-RTE-git-files](#epi-rte-git-files) | Completion is not a correctness judgment; git failure becomes an ambiguous empty list |
| Agents and aggregate status | `sdk/tracecraft/cli/agents.py`, `sdk/tracecraft/cli/status.py` | Supplied runtime account and [RT-BAP-step-polling](runtime.md#rt-bap-step-polling) | Staleness is heartbeat age, not measured liveness; aggregate state is not transactional |
| Artifact upload/download/list | `sdk/tracecraft/cli/artifacts.py` | Supplied [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share) | Opaque bytes; truth-aptness and later interpretation not determinable |
| Mirror, follow, follow-all and discovery | `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/harness/__init__.py`, `sdk/tracecraft/harness/hermes.py` | Direct flush read and Hermes row serialization; other discovery/control branches supplied by [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) | Host content production and project isolation for non-Claude adapters not established |
| Redact | `sdk/tracecraft/redact.py` | Direct complete read; [EPI-RTE-regex-scrub](#epi-rte-regex-scrub) | Pattern membership is not secret identity or transcript truth |
| Session show/stop/compact | `sdk/tracecraft/cli/session.py` | Direct complete operation reads; [RT-RTE-session-compact](runtime.md#rt-rte-session-compact) | Stop resets cursor, not retention or process cancellation; interrupted compact can duplicate later display |
| Shipped verification instruction | `examples/hermes-agent/SKILL.md` | Direct complete read; [EPI-RTE-read-verification](#epi-rte-read-verification), [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt) | Requested read-back is not observed agent checking or semantic review |
| Benchmark evaluators | `benchmarks/contention_bench.py`, `benchmarks/messaging_bench.py` | Direct selected trial/read-back functions; [EPI-RTE-bucket-evaluation](#epi-rte-bucket-evaluation) | Preflight/sweep/report and frozen results not independently assessed; no numerical or causal finding |
| Test/release checks | `sdk/tests/test_v025_features.py`, `.github/workflows/ci.yml`, `.github/workflows/release.yml` | Direct memory test sample; workflow findings supplied by [RT-RTE-package-release](runtime.md#rt-rte-package-release) | Not exhaustive test adequacy; no observed passing CI or publication |

Consequential warrant claims are see [RT-CLM-mirror-idempotence](runtime.md#rt-clm-mirror-idempotence), [RT-CLM-secret-redaction](runtime.md#rt-clm-secret-redaction), [EPI-CLM-git-truth](#epi-clm-git-truth) and [EPI-CLM-history-loss](#epi-clm-history-loss). These concern preservation, confidentiality and local evidence, not a declared general theory-production engine. The selected reads do not support an unqualified system-complete negative about all possible caller content or uninspected evaluation reports.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-step-state](runtime.md#rt-obj-step-state) | Caller declaration of work state; symbolic status also controls tooling | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | Complete names no substantive criterion, intended-use evidence or independent judge |
| [EPI-OBJ-handoff](#epi-obj-handoff) | Optional note assertions, optional git-derived file list; next-action is a directive, not necessarily truth-apt | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | Mixed object split by consumers below; no supplied instance |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | Caller string may assert facts; key/writer/time are symbolic envelope | see record | SRC-1 `sdk/tracecraft/cli/memory.py` | No semantic restrictions; metadata-only get preserves attribution, default get omits it |
| [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) | Caller message may assert facts or request actions | see record | SRC-1 `sdk/tracecraft/cli/messages.py` | Acquired communication, not evidence of produced accepted knowledge |
| [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share) | Not determinable for arbitrary file bytes | see record | SRC-1 `sdk/tracecraft/cli/artifacts.py` | No artifact contents or parser supplied |
| [EPI-OBJ-session-parts](#epi-obj-session-parts) | Records of host utterances/tools may contain assertions, outputs or directives | see record | SRC-1 `sdk/tracecraft/cli/session.py` | A transcript records an assertion without endorsing it; redaction removes original details |
| [EPI-RTE-bucket-evaluation](#epi-rte-bucket-evaluation) | Computed owner-consistency and delivered-body-count propositions in test domains | see record | SRC-1 `benchmarks/contention_bench.py`, `benchmarks/messaging_bench.py` | Evaluator source, not observed outcome; no truth oracle for message bodies |

## Authority-route ledger

All rows are architectural findings. Observed activation is uninspected unless stated otherwise. Fields owned by supplied records are referenced rather than restated as new declarations. The same cited route appears in distinct functional rows deliberately: checking, disposition, retention and consumption have different licenses.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | Caller value to envelope | Structural key validation, not value truth | see record | Stored text and attribution | Software vetoes invalid key only | Source warrant unknown; value not endorsed | Allows valid-key write | see record | SRC-1 `sdk/tracecraft/cli/memory.py` | none | none | Human/model authorship unresolved |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | retention | implemented | see record | no content change | History then live value | Timestamp/unique key, ordinary overwrite | see record | Snapshot plus current value | Persistence and explicit reads | Availability and claimed attribution only | Later get/history deliver text | see record | SRC-1 `sdk/tracecraft/cli/memory.py` | [EPI-CLM-history-loss](#epi-clm-history-loss) | Immutable is not enforced | Direct writes/deletes and partial failure remain possible |
| [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange), [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share) | operational admission/selection/consumption | implemented | see records | no content change | Retained mail/files to requesting reader | see records | see records | Printed or downloaded content | Delivery, not content execution | No semantic warrant added | Reader can receive selected retained data | see records | SRC-1 `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/cli/artifacts.py` | none | none | Truth-aptness of artifacts indeterminate; mail source warrant unknown |
| [RT-RTE-step-control](runtime.md#rt-rte-step-control) | check/evidence production | implemented | [RT-OBJ-step-state](runtime.md#rt-obj-step-state) | no content change | Claim conflict and completion ownership | Conditional service write or agent-string comparison | see record | Conflict/mismatch or admissible completion | Structural/cooperative veto | License over claim admission only | Rejects competing claim or mismatched completion unless override | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | none | none | HF arbitration differs; not work evaluation |
| [RT-RTE-step-control](runtime.md#rt-rte-step-control) | disposition/acceptance | implemented | [RT-OBJ-step-state](runtime.md#rt-obj-step-state), [EPI-OBJ-handoff](#epi-obj-handoff) | truth-apt transformation: acquisition/import | Caller outcome declaration | Caller flags; no semantic evaluator | see record | Complete, blocked, needs_review | Persists declaration | Operational admission, not evidence-consuming epistemic acceptance | Makes symbolic state available to polling | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | none | none | No separate reviewer required to clear review state |
| [RT-BAP-step-polling](runtime.md#rt-bap-step-polling) | operational admission/selection/consumption | implemented | [RT-OBJ-step-state](runtime.md#rt-obj-step-state) | no content change | Dependency readiness | Fixed status comparison | see record | Return, wait or error | Enforcing within waiter | Status equality only, not actual completed-work truth | Complete permits return; blocked fails | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | none | none | No control over external work; complete precedes handoff write |
| [EPI-RTE-git-files](#epi-rte-git-files) | check/evidence production | implemented | [EPI-OBJ-handoff](#epi-obj-handoff) | truth-apt transformation: acquisition/import | Local tracked diff paths versus HEAD | Git exit status and name output | see record | List or empty fallback | Optional field writer | Conditional local diff evidence, not all activity | Handoff receives changed_files | see record | SRC-1 `sdk/tracecraft/cli/steps.py` | [EPI-CLM-git-truth](#epi-clm-git-truth) | Empty conflates failure and no tracked change | Untracked files, committed changes and content correctness outside license |
| [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) | content transformation | implemented | [EPI-OBJ-session-parts](#epi-obj-session-parts) | truth-apt transformation: acquisition/import | Host records into delta stream | see record | see record | File bytes or serialized Hermes rows | Imports records | Original assertion warrant unknown; attribution retained only to extent host data supplies it | Makes host records available for retention | see record | SRC-1 `sdk/tracecraft/harness/hermes.py`, `sdk/tracecraft/cli/session.py` | none | none | Imported host claims are not Tracecraft-produced conclusions |
| [EPI-RTE-regex-scrub](#epi-rte-regex-scrub) | content transformation | implemented | [EPI-OBJ-session-parts](#epi-obj-session-parts) | truth-apt transformation: indeterminate | Byte-pattern replacement | Regex membership, not proposition truth | see record | Redacted bytes plus counts | Replaces matching substrings before mirror upload | Original matched details unavailable; untouched assertion warrant still unknown | Consumer sees modified stream | see record | SRC-1 `sdk/tracecraft/redact.py` | [RT-CLM-secret-redaction](runtime.md#rt-clm-secret-redaction) | No privacy/truth equivalence | Cannot establish semantic preservation for arbitrary transcripts |
| [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) | retention | implemented | [EPI-OBJ-session-parts](#epi-obj-session-parts) | no content change | Transformed delta to bucket parts/meta/cursor | see record | see record | Durable transformed trace | Storage and later show | No semantic endorsement | Explicit show can retrieve parts | see record | SRC-1 `sdk/tracecraft/cli/session.py` | [RT-CLM-mirror-idempotence](runtime.md#rt-clm-mirror-idempotence) | Replay possible after cursor failure | Stop does not withdraw retained assertions |
| [RT-RTE-session-compact](runtime.md#rt-rte-session-compact) | content transformation | implemented | [EPI-OBJ-session-parts](#epi-obj-session-parts) | truth-apt transformation: non-ampliative reshaping | Ordered part bytes to concatenation | Fixed byte-copy code | see record | Same byte sequence on completed normal path | Storage-layout replacement | No new semantic warrant | Show reads merged content after originals removed | see record | SRC-1 `sdk/tracecraft/cli/session.py` | none | none | Partial completion changes replay multiplicity; lineage metadata loses per-part detail |
| [EPI-RTE-read-verification](#epi-rte-read-verification) | check/evidence production | doctrine only | Caller retained state | no content change | Write/read correspondence | Host agent interpreting matching reads | see record | Potential write verification | Advisory instruction only | At most write/read agreement; not truth of value | Requests subsequent read or recipient confirmation | see record | SRC-1 `examples/hermes-agent/SKILL.md` | none | none | No checked result or uptake supplied |
| [EPI-RTE-bucket-evaluation](#epi-rte-bucket-evaluation) | check/evidence production | implemented | Trial results | truth-apt transformation: entailed derivation | API outcomes versus durable owner; intended sends versus distinct bodies | Fixed arithmetic/equality under trial inputs | see record | Invariant boolean, duplicate/loss counts | Trial reporting only | Conditional conclusions in configured benchmark domain | Invalidates trial on unexpected errors; records result | see record | SRC-1 `benchmarks/contention_bench.py`, `benchmarks/messaging_bench.py` | none | none | No route from these results to acceptance of message meaning or automatic SDK policy revision |

No lifecycle integration after semantic acceptance is evidenced by these inspected writes/readers: they are retention and operational use before any such acceptance. This is a bounded account of these mechanisms, not a negative about what an external agent might implement. CI/package disposition is separately see [RT-RTE-package-release](runtime.md#rt-rte-package-release): packaging checks have publication force, but neither sampled storage assertions nor release smoke checks judge the truth of retained claims.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-mirror-idempotence](runtime.md#rt-clm-mirror-idempotence) | see record | SRC-1 `sdk/tracecraft/cli/session.py`; doctrine/design | see record | [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) | Uninspected | No intervention evidence | Cursor suppresses normal repeated ingestion | Part success before cursor write permits repeated bytes |
| [RT-CLM-secret-redaction](runtime.md#rt-clm-secret-redaction) | see record | SRC-1 `sdk/tracecraft/redact.py`; doctrine/design and implementation | Explicit denylist limits | [EPI-RTE-regex-scrub](#epi-rte-regex-scrub) | Uninspected | No disclosure experiment | Recognizable shapes replaced and counted | Counts do not establish all secrets removed or original truth preserved |
| [EPI-CLM-git-truth](#epi-clm-git-truth) | see record | SRC-1 `sdk/tracecraft/cli/steps.py`; doctrine/design | Optional non-hand-typed list | [EPI-RTE-git-files](#epi-rte-git-files) | Uninspected | No support for quoted frequency claim | Imported tracked diff paths when subprocess succeeds | Not exhaustive work evidence; failure/no-change both empty |
| [EPI-CLM-history-loss](#epi-clm-history-loss) | see record | SRC-1 `sdk/tracecraft/cli/memory.py`; doctrine/design | Append snapshot before overwrite | [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | Uninspected | No crash/durability experiment | Normal CLI set creates historical copy | No enforced immutability or unconditional no-loss guarantee |

## Bounded conclusion

Tracecraft retains and retrieves caller assertions, messages, handoff text, arbitrary artifacts and host records without licensing their substantive truth. The memory writer records attribution and time, but default get prints only the value; historical availability and freshness are not endorsement. Messages and artifacts supply selected data to later invocations; external-agent interpretation and compliance remain unobserved. Evidence is see [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) and [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share).

Step status has concrete enforcing force at the dependency waiter, not merely advisory text. Complete permits return, blocked raises and review-needed waits. The completion writer admits the caller's outcome without an evidence-consuming criterion for work correctness. Clearing review does not require a separate reviewer. The handoff's directive has no implemented scheduler consumer here, and its optional changed-files field imports a narrower local Git measurement. These paths give operational authority without semantic acceptance: see [RT-RTE-step-control](runtime.md#rt-rte-step-control), [RT-BAP-step-polling](runtime.md#rt-bap-step-polling) and [EPI-RTE-git-files](#epi-rte-git-files).

Mirroring acquires host-produced content whose source warrant is unknown. Redaction deliberately degrades access to original matched details; it does not verify the remaining assertions. Compaction preserves ordered bytes on the completed normal path, not meaning by a new inference, and interrupted cleanup can duplicate displayed material. Show selects tail lines, not a resumed model conversation. Stop removes local cursor and stamps metadata, not epistemic withdrawal. See [EPI-RTE-regex-scrub](#epi-rte-regex-scrub), [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) and [RT-RTE-session-compact](runtime.md#rt-rte-session-compact).

There are narrow truth-apt checks: benchmark equality/arithmetic derives propositions from supplied trial outcomes and durable reads; the memory test compares returned v2 to a reference outcome. Their premises would require execution evidence for actual result claims. They do not check message meaning, explanation quality, transfer or model reasoning. The Hermes read-verification instruction requests a possible check but supplies no operative checked result. No demonstrated learning benefit, reflective criticism loop or exercised self-improvement follows from retaining raw traces or reporting storage results. These independent properties remain unestablished within these routes, not disproved for excluded hosts. See [EPI-RTE-bucket-evaluation](#epi-rte-bucket-evaluation), [EPI-RTE-read-verification](#epi-rte-read-verification) and [RT-RTE-package-release](runtime.md#rt-rte-package-release).

## Shared records

### Operative objects

#### EPI-OBJ-handoff
Label: Structured handoff

Part of: [RT-RTE-step-control](runtime.md#rt-rte-step-control)

Material output of that route, not a replacement for its claim/status control account. Source-native identity: `steps/<sid>/handoff.json`; bucket JSON contains natural-language note/next-action, symbolic state/recipient/schema and optional symbolic changed_files. No counterpart object for the handoff is declared in supplied runtime; [RT-OBJ-step-state](runtime.md#rt-obj-step-state) is the separate claim/status pair. The status poller reads that pair rather than the handoff. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`:

> store.put_json(f"steps/{sid}/handoff.json", handoff)
> --- `sdk/tracecraft/cli/steps.py`

#### EPI-OBJ-session-parts
Label: Transcript parts

Part of: [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

Material retained output of the route, not another declaration of mirroring. Source-native identity: numbered `part-*.jsonl` objects; substrate is configured bucket. Form is serialized host records containing natural language and symbolic tool/row metadata; opaque content remains possible. [RT-RTE-session-compact](runtime.md#rt-rte-session-compact) later rearranges these same objects. No counterpart operative-object declaration in supplied runtime. SRC-1 implementation, `sdk/tracecraft/cli/session.py`:

> part_key = f"{_session_prefix(harness_name, sess.session_id)}part-{seq:05d}-{uniq}.jsonl"
> --- `sdk/tracecraft/cli/session.py`

Hermes is a source-supported alternative to literal byte copying: rows are serialized, with content decoding while tool_calls/reasoning_details remain strings. It does not produce a summary or test the assertions in those rows. SRC-1 implementation, `sdk/tracecraft/harness/hermes.py`:

> lines.append(json.dumps(d, default=str, ensure_ascii=False))
> --- `sdk/tracecraft/harness/hermes.py`

### Routes

#### EPI-RTE-git-files
Label: Optional git evidence

Part of: [RT-RTE-step-control](runtime.md#rt-rte-step-control)

Distinct material evidence-producing subroute. Caller opts into --changed-files-from-git; `_git_changed_files` calls Git, parses names and inserts changed_files into handoff. Caller proposes completion; code chooses the reference measurement; no human approval of each path or answer oracle for work correctness is established. Open coordination request. Failure yields [] rather than a veto. Guidance and persisted result are see [EPI-CLM-git-truth](#epi-clm-git-truth). No automatic policy adaptation or rollback follows; a later completion can overwrite handoff.

- Immediate return: List of stripped nonempty diff output lines, or [] on nonzero exit/exception.
- Later read-back: Persisted changed_files can be read through direct store access to handoff.
- Delegated visibility: Bucket readers can see the optional field.
- Selection predicate: Explicit flag; fixed git diff --name-only HEAD in caller's working directory.
- Invalidation or expiry: Handoff overwrite; field is not refreshed by later commits or file changes.
- Activation or effect: Inserts machine-derived paths into handoff; downstream interpretation unobserved.
- Evidence limits: No execution supplied; excludes untracked paths and cannot certify completed work; empty is ambiguous.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 implementation, `sdk/tracecraft/cli/steps.py`:

> ["git", "diff", "--name-only", "HEAD"],
> --- `sdk/tracecraft/cli/steps.py`

> if out.returncode != 0:
>     return []
> --- `sdk/tracecraft/cli/steps.py`

#### EPI-RTE-regex-scrub
Label: Regex scrub and counts

Part of: [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror)

A transformation subroute, not semantic acceptance. Source-native `redact` consumes bytes, applies denylist patterns sequentially and returns replacement bytes/counts to mirror. Code decides substring removal; no human/model judgment or secret/truth oracle. Caller selects activation through mirror options. Open ingestion. Counts and altered bytes persist; source bytes are not overwritten by this routine, and restoration would require original host material. [RT-CLM-secret-redaction](runtime.md#rt-clm-secret-redaction) owns the claim.

- Immediate return: Replacement bytes and nonzero pattern counts.
- Later read-back: Mirror parts carry altered bytes; metadata stores cumulative counts.
- Delegated visibility: Bucket readers receive scrubbed parts and counts, not removed originals through this path.
- Selection predicate: Byte regex membership, unless --no-redact bypasses the call.
- Invalidation or expiry: No rule-driven re-scrub of already retained parts; later source/package revision changes future calls.
- Activation or effect: Replaces matched substrings before mirror upload; no behavior-shaping model consumer inspected.
- Evidence limits: No run supplied; arbitrary secrets and split-chunk matches not covered; counts do not license original truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 implementation, `sdk/tracecraft/redact.py`:

> ("aws_access_key", re.compile(rb"AKIA[0-9A-Z]{16}")),
> --- `sdk/tracecraft/redact.py`

> out, n = pat.subn(f"[REDACTED:{name}]".encode(), out)
> if n:
>     counts[name] = n
> --- `sdk/tracecraft/redact.py`

Concrete source deduction, not execution: input bytes `key=AKIA1234567890ABCDEF` match the 16-character uppercase/digit suffix. The AWS rule changes them to `key=[REDACTED:aws_access_key]` and records aws_access_key count 1. Later patterns do not match this replacement. This establishes loss of the literal credential-like value, not that the input was a real credential. In an arbitrary sentence or structured record such replacement can change a proposition or its parseability, so semantic preservation/entailment is indeterminate; no ampliative conjecture is inferred just from that uncertainty.

#### EPI-RTE-read-verification
Label: Requested read verification

Distinct doctrine-only checking request, compared with [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt), which owns the broader instruction delivery path, and [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)/[RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange), which own executable reads/writes. The Hermes host agent is instructed to compare write/read results. No automatic comparator, recorded criterion outcome or acceptance disposition is implemented by this Markdown. Human/model compliance is unresolved; an expected prior write could be a reference for correspondence, not an answer oracle for substantive truth. Open coordination use, not a bounded experiment.

- Immediate return: inapplicable — static skill instruction returns no checked result.
- Later read-back: Requested memory get, recipient inbox or step-status reads retained state.
- Delegated visibility: Send verification explicitly asks a recipient to read inbox.
- Selection predicate: Corresponding read command after the named action.
- Invalidation or expiry: inapplicable — no persisted check result or acceptance state is specified.
- Activation or effect: Advisory request only; actual comparison and changed reliance unobserved.
- Evidence limits: No host loading/compliance trace; read success alone does not certify message meaning.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

SRC-1 doctrine/design, `examples/hermes-agent/SKILL.md`:

> After any action, verify with the corresponding read command:
> - After `memory set` → `memory get`
> - After `send` → ask the recipient to check `inbox`
> - After `claim` → `step-status`
> --- `examples/hermes-agent/SKILL.md`

#### EPI-RTE-bucket-evaluation
Label: Bucket benchmark evaluation

No counterpart benchmark route is declared in supplied runtime; [RT-RTE-step-control](runtime.md#rt-rte-step-control) and [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) are product routes whose primitives the evaluators exercise, not these test drivers. Two fixed evaluators remain separate in license: contention compares API winners to durable owner; messaging compares intended sends to distinct retained bodies. Script caller chooses conditions; software performs writes, counts and judges equality. Human initiation/interpretation unresolved. Reference outcomes are one consistent winner and sent distinct bodies, not truth oracles for payload text. Bounded experimental mode. Exceptions invalidate contention trials; results report rather than admit product content. Contention deletes its trial key after evaluation; deletion failure is swallowed, and the inspected function does not confirm deletion despite its comment. No feedback consumer modifies the SDK policy in these functions.

- Immediate return: Contention Trial fields including invariant_held/valid; messaging sent, delivered_keys, distinct_messages, lost and errors.
- Later read-back: Fresh backend client retrieves claim owner or messages within the trial; publication/retention of resulting reports uninspected here.
- Delegated visibility: Test objects use configured bucket access; distribution of results uninspected.
- Selection predicate: Unique trial claim key or configured recipient mailbox; selected concurrency/key scheme and optional stagger.
- Invalidation or expiry: Trial cleanup attempts claim deletion; no epistemic rollback or product content acceptance state.
- Activation or effect: Deterministic result computation; no actual trial or downstream policy revision observed.
- Evidence limits: Source only; service correctness, supplied benchmark result authenticity and causal comparisons not assessed. Key counts are not end-user inbox delivery or message truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 implementation, `benchmarks/contention_bench.py`:

> t.invariant_held = (
>     t.valid and win_count == 1 and t.stored_owner == t.declared_winner
> )
> --- `benchmarks/contention_bench.py`

SRC-1 implementation, `benchmarks/messaging_bench.py`:

> "distinct_messages": len(bodies),
> "lost": sent - len(bodies),
> --- `benchmarks/messaging_bench.py`

The stagger control affords testing a simultaneous-contention hypothesis, but without inspected intervention results it supports no causal finding. The treatment changes launch timing, not independently isolated backend components. Sampled SDK test supplies a different fixed reference outcome, not a semantic oracle. SRC-1 implementation, `sdk/tests/test_v025_features.py`:

> r = env.invoke(cli, ["memory", "get", "k"])
> assert r.output.strip() == "v2"
> --- `sdk/tests/test_v025_features.py`

### Claims

#### EPI-CLM-git-truth
Label: Git source of truth

Part of: [RT-RTE-step-control](runtime.md#rt-rte-step-control)

A design/warrant claim attached to that route's optional evidence producer, not the runtime's mechanism declaration. SRC-1 doctrine/design, `sdk/tracecraft/cli/steps.py`, claims local Git is authoritative for changed paths and self-reported lists are unreliable. No evidence for the frequency estimate is supplied by this implementation.

> Git is the source of truth for what changed — we never let an agent type
> the file list by hand (self-reported change lists are wrong ~half the time
> and go stale on the next commit).
> --- `sdk/tracecraft/cli/steps.py`

#### EPI-CLM-history-loss
Label: Immutable no-loss history

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Design claim about its retention subfunction, not another declaration of the writer. SRC-1 doctrine/design, `sdk/tracecraft/cli/memory.py`, claims every set appends an immutable snapshot and no version is ever lost. Implementation gives snapshot-before-live ordering, not object immutability, transactional success or universal backend durability. Direct wrapper mutation is the counterroute supplied in runtime's forcing cases.

> Every set also appends an immutable snapshot under memory/_history/, so
> the current value is last-write-wins but no version is ever lost. See
> `memory history`.
> --- `sdk/tracecraft/cli/memory.py`

Normal ordering evidence is see [RT-RTE-memory-write](runtime.md#rt-rte-memory-write). No semantic repair of that supplied route is needed: it already limits immutable-history claims to a nontransactional, directly mutable implementation.
