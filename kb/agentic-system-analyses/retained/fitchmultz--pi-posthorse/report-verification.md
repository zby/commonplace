---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Pi Posthorse's extension, retained-state and foreground continuation routes at the frozen commit."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
---

# Pi Posthorse report verification

## Verification

The pinned reports support a bounded implementation account. No material correction is required. I read every supplied report, type, correction-answer input and structural check. The answer inputs are empty; the structural check reports `none`. I independently traced consequential behavior in SRC-1 rather than accepting the analysts' inspection statements. The checkout HEAD equals the registered revision; status is clean and `git diff --exit-code` passed. No target code, test, example or provider was executed. Source assertions remain evaluator design, not observed results.

### Runtime and authority

Complete reads of SRC-1, `index.ts`, `package.json`, `src/context-tools.ts`, `src/rollover.ts`, `src/budget.ts`, `src/paging.ts` and `src/reminders.ts` support the component, object and route findings:

- [RT-CMP-active-model](runtime.md#rt-cmp-active-model) correctly leaves external weights, exact deployment version and endpoint mutability unresolved. The factory uses the current host configuration rather than pinning a model. [RT-CMP-page-reservations](runtime.md#rt-cmp-page-reservations) is shared ephemeral admission state, not acquired knowledge.
- [RT-OBJ-reset-requests](runtime.md#rt-obj-reset-requests), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset) and [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) preserve the distinction between a successful callback, eligible draft and host commitment. Matching callback IDs, sibling errors, existing assistant failures, abort state and recalculated capacity are checked at the described points. A failed explicit request can still leave a separately eligible automatic fallback; prior sibling effects are not rolled back.
- [RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance), [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance) and [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance) distinguish regenerated prose, retained reminder metadata and code filtering. Forced-prompt guidance takes the alternate custom-message channel. Delivery is not compliance.
- [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery) correctly separates the reached native hook from the narrower threshold fallback. Manual and unsupported cases preserve native alternatives; construction failure cancels within the supported hook. The eager fallback cannot incorporate arbitrary later edits, and sentinel append is not transactional with the entire compaction.
- [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) describe physical publication and bounded delivery, not semantic approval, sandboxing or provider-exact sizing. The no-summary qualification in [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) agrees with SRC-1, `README.md` and `docs/reference.md`: it does not cover every native/manual route.

The `wired` implementation and `uninspected` operation statuses are supported. Protocol guarantees remain conditional on the named host contracts; estimated page sizing remains best effort. I also read SRC-1, `test/official.test.mjs`, lines 1534–1578: the later-handler abort assertion supports the retained countercase as test intent only, not a witnessed host outcome.

### Retained material and epistemic checks

Complete independent reads of SRC-1, `src/notes.ts`, `src/files.ts`, `src/recovery.ts`, `src/recovery-results.ts`, `src/history.ts`, `src/history-entries.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-pages.ts`, `src/message-text.ts` and `src/contracts.ts` support the following distinctions:

- [MEM-OBJ-notes](memory.md#mem-obj-notes) and [MEM-RTE-notes-migration](memory.md#mem-rte-notes-migration) correctly separate content authorship from location maintenance. Migration can run on reads as well as writes; existing destination content is not semantically merged. Replacement, append, external editing, empty clearing and symlink following prevent a single-writer or semantic-admission interpretation.
- [MEM-OBJ-session-journal](memory.md#mem-obj-session-journal), [MEM-RTE-notes-recall](memory.md#mem-rte-notes-recall) and [MEM-RTE-history-recall](memory.md#mem-rte-history-recall) distinguish original/replacement versions, requested recall and normalized payloads. Binary/size exclusions, live positions, project membership, inherited descendant scope, priority groups and text/image budgets bound retrieval. Raw journal retention is not exact normalized replay.
- [MEM-OBJ-explicit-handoff](memory.md#mem-obj-explicit-handoff) and [MEM-OBJ-recovery-record](memory.md#mem-obj-recovery-record) are different retained payloads. Recovery applies projected omissions/replacements, selects owner anchors and bounded receipts, and can carry older nonautomatic checkpoints. It does not certify current progress or recursively retain all earlier tool evidence.
- [EPI-OBJ-owner-inputs](epistemic.md#epi-obj-owner-inputs), [EPI-OBJ-result-evidence](epistemic.md#epi-obj-result-evidence), [EPI-RTE-recovery-provenance](epistemic.md#epi-rte-recovery-provenance) and [EPI-RTE-recovery-reshape](epistemic.md#epi-rte-recovery-reshape) accurately distinguish recorded provenance from truth. Registered unnamespaced projected calls and successful linked results govern owner-answer classification. Orphan/legacy async receipts can survive as evidence without becoming owner approval. The non-ampliative classification concerns excerpting source content; its explicit truncation caveat withholds semantic equivalence of incomplete fragments.
- [EPI-OBJ-context-report](epistemic.md#epi-obj-context-report) and [EPI-RTE-context-report](epistemic.md#epi-rte-context-report) support arithmetic derivation under supplied native estimates, not physical provider measurement. Unknown usage withholds a count.

Independent complete reads of SRC-1, `ui.ts`, `src/ui/display.ts` and `src/ui/cards.ts` support [MEM-OBJ-posthorse-display](memory.md#mem-obj-posthorse-display): expansion renders returned content and metadata; it does not fetch an omitted page. [MEM-BAP-recalled-content](memory.md#mem-bap-recalled-content) correctly separates changing task content reaching the model from fixed guidance and symbolic host admission. Neither channel establishes successful reliance.

The epistemic ledger keeps checking, disposition, retention and consumption separate. Inspected write/reset/recovery dispatches do not consume evidence to accept task propositions for a named intended use. The report's negative is scoped to those dispatches, not opaque model processing or every evaluator. No accepted ampliative claim, exercised learning or self-improvement is inferred from retention alone.

### Workflow, relations and conflicts

I read SRC-1, `test/official.test.mjs`, lines 1–349 and 490–521, including the faux-provider fixture, reset/read/reopen scenario and failed-sibling retry. [EPI-RTE-reset-evaluator](epistemic.md#epi-rte-reset-evaluator) and the [workflow account](workflow.md#workflow-account) describe the same connected scenario. The test scripts restoration and a terminal answer; it neither tests live task truth nor establishes autonomous checkpoint selection. The separate retry really is a new request, not retained authorization or automatic repair.

I checked every declaration, supporting source anchor, evidence status and annotation against its referent. Every `Part of:` relation preserves actual containment: notes/history recall are parts of the combined retrieval route; explicit/automatic handoff objects are payload parts of their routes; epistemic input, receipt, classification and reshaping records are parts of automatic recovery. Migration spans read/write location resolution and is correctly not contained in write-only admission. Containers remain valid; no duplicate requires supersession.

The [reconciliation](reconciliation.md#reconciliation) preserves these identities and disposes every memory integration issue. Its distinction between member-specific inspection coverage and mechanism disagreement is sound. There are no amendments, unresolved conflict paragraphs or correction answers to adjudicate. I found no unmarked disagreement requiring one. Runtime `wired` and epistemic `implemented` are compatible statuses at different layers.

### Consequential omission searches and stopping decision

The frozen tracked tree, published file list, factory imports, production registrations and shipped SDK callers supplied the search basis. I investigated whether another shipped dispatcher or state consumer changed the extension boundary; whether native/manual compaction, fallback ordering, external editors or projected receipt alternatives invalidated the ordinary route; and whether production checks or evaluator feedback changed unchecked retention into task-claim acceptance. Tree/registration searches plus independent producer-to-consumer traces found no material unaccounted shipped product path. The SDK tests are included callers, not excluded merely because they use an API. Searches across SRC-1, `src`, `index.ts` and `ui.ts` for evaluation, acceptance, verification and registration supplemented code reads; search misses alone were not treated as absence.

The known alternate paths are already preserved in the reports. Additional engineering-checker or release artifacts do not warrant expanding the selected functional boundary. Further omission search stopped because the identified consequential questions have supported dispositions and no material challenge remains undisposed. Detailed prefilter equivalence and a complete evaluator audit remain outside the conclusions accepted here. Missing execution and external-host evidence continue to prevent observed success, deployment-independent guarantees and causal benefit, rather than making the inspectable extension mechanisms unknown.

## Blockers

none

## Limits

- [MEM-RTE-history-recall](memory.md#mem-rte-history-recall) and [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval): independent reads establish the optional file/line prefilters, normalized matching and failure fallback in SRC-1, `src/session-files.ts`, `src/history-search.ts` and `src/history-entries.ts`, but do not certify full-scan equivalence across arbitrary journal encodings and query text. Requested scoped retrieval and paging remain supported; consumers should withhold exhaustive-recall and exact-replay comparisons. The records already withhold those stronger conclusions.
- [EPI-RTE-reset-evaluator](epistemic.md#epi-rte-reset-evaluator) and [workflow](workflow.md#workflow-account): the inspected connected fixture establishes evaluator design for reset, retrieval and journal reopening, with a separate rejection/retry case. Other shipped assertion bodies were inventoried but not exhaustively audited. SRC-1, `test/official.test.mjs` and `test/host.test.mjs` support the selected account, not complete evaluator coverage or checker correctness. Withhold comparisons of total test coverage and general recovery reliability; no passing execution or live task-state verification was supplied.
