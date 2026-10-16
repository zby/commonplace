---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MentisDB epistemic routes: candidate extraction, structural admission, operational withdrawal, selective context and the limits of knowledge-loss and improvement claims."
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
reviewed-boundary: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
---

# MentisDB epistemic report

## Source-and-claim boundary

The question is what MentisDB acquires or produces that can be true or false, what checks license reliance, and how retained results reach later consumers. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identities and layers are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. The Rust memory service, shipped Python consumer, skill registry, extraction and evaluators are included. External task agents, provider internals and dependency/model assets are not captured.

The supplied runtime is provisional. This member directly inspected additional dispatch, retrospective, import, withdrawal, summary selection, context-bundle and evaluator paths at the same frozen commit. Available but uninspected paths below prevent a system-complete negative about acceptance or knowledge production. No supplied fact requires supersession: the new records separate material parts or add routes without changing the runtime's referents.

Consequential claims include [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol), [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review), [EPI-CLM-context-continuity](#epi-clm-context-continuity), and [EPI-CLM-fleet-improvement](#epi-clm-fleet-improvement).

| Entry point or operation | SRC-1 source path | Inspection basis and covering records, or limit |
|---|---|---|
| Binary CLI/daemon/HTTP/local stdio dispatch | `src/bin/mentisdb.rs`, `src/cli/mod.rs` | Supplied runtime dispatch, alternate enforcement and update findings: [RT-RTE-access-control](runtime.md#rt-rte-access-control), [RT-RTE-release-update](runtime.md#rt-rte-release-update). Direct scoped CLI dispatch search identifies Add, Search, Backup, Restore and setup/admin operations; their entire implementations were not reread. |
| MCP registered execution, REST operations and resource delivery | `src/server.rs` | Direct execution-match read covers append, retrospective, all search families, summaries, import/export, lookup/traversal, identity/key and entity administration, skill lifecycle, branch/merge, webhook registration and extraction; supplied transport coverage: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [RT-BAP-core-skill](runtime.md#rt-bap-core-skill). Metadata bodies and every REST alias were not exhaustively audited. |
| Ordinary append, Python message write and prompt read-back | `src/lib.rs`, `src/server.rs`, `pymentisdb/langchain.py` | Direct append and recent-context reads plus supplied Python consumer findings: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [EPI-OBJ-thought-content](#epi-obj-thought-content). |
| Retrospective append | `src/server.rs` | Direct `append_retrospective`: caller content defaults to LessonLearned/Retrospective and reaches shared append; part of [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), not a separate semantic evaluator. |
| Extraction and schema gate | `src/llm.rs`, `src/server.rs` | Direct prompt, parser, transformer and extraction return reads: [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction), [EPI-RTE-extraction-schema](#epi-rte-extraction-schema). |
| Deduplication, invalidating relations, current and as-of visibility | `src/lib.rs`, `src/search/lexical.rs` | Direct append, invalidation index and time-aware predicate reads; tokenizer bounded read: [EPI-RTE-relation-withdrawal](#epi-rte-relation-withdrawal). |
| Summary candidates and claimed coverage | `src/lib.rs`, `src/search/summary_index.rs`, `src/server.rs` | Direct source-window selector and caller/service trace: [EPI-RTE-summary-selection](#epi-rte-summary-selection). |
| Context bundles | `src/lib.rs`, `src/search/bundle.rs`, `src/server.rs` | Direct lexical seed/graph grouping and response trace: [EPI-RTE-bundle-selection](#epi-rte-bundle-selection). Graph expansion internals are not exhaustively assessed. |
| Ranked and federated search | `src/lib.rs`, `src/server.rs` | Supplied ordinary ranking/ancestor findings and direct federated request construction read: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip). Federated fusion/reranking implementation remains partially uninspected; complete score comparability and lineage preservation cannot be concluded. |
| Markdown import/export and direct thought lookup | `src/lib.rs`, `src/server.rs` | Direct import loop and service read/write traces: [EPI-RTE-markdown-import](#epi-rte-markdown-import). Full Markdown parser/export fidelity remains uninspected. Direct get_thought does not apply the recent-context invalidation filter. |
| Skill upload/read/signature and lifecycle | `src/skills.rs`, `src/server.rs`, `src/dashboard.rs` | Supplied admission/version reconstruction plus direct read/revoke/deprecate bodies: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal). All UI mutation paths remain uninspected. |
| Branch, merge, archive restore and release update | `src/server.rs`, `src/backup.rs`, `src/bin/mentisdb.rs` | Supplied [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) and [RT-RTE-release-update](runtime.md#rt-rte-release-update). Full restore reconciliation and branch lineage are not re-assessed. |
| Callbacks and webhooks | `src/lib.rs`, `src/server.rs`, `src/webhooks.rs` | Direct append callback/spawn sites plus supplied callback finding. Host callback can act after admission; destination consumers, retries and complete payload transformations uninspected. This prevents conclusions about their epistemic checks or later behavioral effects. |
| LongMemEval, ConvoMem and LoCoMo | `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py` | Direct matching/reference and aggregate-consumer reads: [EPI-RTE-recall-evaluation](#epi-rte-recall-evaluation). LoCoMo aggregate consumer is supplied by boundary coverage; full ingest, external datasets and measured outcomes uninspected. |
| Rust tests, performance benches, TUI and maintenance instructions | `tests/`, `benches/`, `src/tui.rs`, `skills/`, `docs/` | Included but not inspected in this job beyond supplied boundary/runtime scope. Cannot certify all evaluators, task-result acceptance or maintenance procedures. No target execution performed. |

Missing evidence is local to conclusions. No retained live chain, uploaded skill, provider output or host trace was supplied: candidate instances, actual semantic transformation, caller review, host reliance and instruction compliance are unobserved. No model artifact or provider internals were captured: extraction accuracy and exact distributed-parametric state are uninspected. No benchmark run or intervention was supplied: even an implemented metric cannot establish measured benefit or causal component effects. These are not evidence that the corresponding behavior is absent.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-thought-content](#epi-obj-thought-content) | Caller assertions, hypotheses, corrections or lessons when their content states a proposition; questions/plans need not be truth-apt | see record | SRC-1, `src/lib.rs` | Type names do not individuate propositions or establish truth; no actual retained instance supplied. |
| [RT-OBJ-thought](runtime.md#rt-obj-thought) | Structural indices, identifiers, attribution fields, relations and hashes; no semantic truth check | see record | SRC-1, `src/lib.rs` | Attribution and graph labels do not certify authorship, correctness or evidence support. |
| [EPI-OBJ-extracted-thoughts](#epi-obj-extracted-thoughts) | Model-returned memory statements and self-reported extraction confidence | see record | SRC-1, `src/llm.rs` | Natural-language content plus symbolic envelope; exact content and entailment not determinable without a supplied input/output pair. |
| [EPI-OBJ-skill-document](#epi-obj-skill-document) | Instructions with possible truth-apt premises; instruction imperatives themselves are policy | see record | SRC-1, `src/skills.rs` | Concrete live skill theories, criticisms and quality uninspected. |
| [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry) | Symbolic version/status/hash information | see record | SRC-1, `src/skills.rs` | Latest and signed are not best or true. |
| [RT-OBJ-core-skill](runtime.md#rt-obj-core-skill) | Static memory-work instructions, including startup, correction and checkpoint policy | see record | SRC-1, `MENTISDB_SKILL.md` | Delivery is not compliance or accumulated learning. |
| [EPI-OBJ-summary-candidate](#epi-obj-summary-candidate) | Deterministic source-index/ID grouping; no generated summary proposition | see record | SRC-1, `src/search/summary_index.rs` | Coverage records caller-declared Summarizes edges, not verified semantic completeness. |
| [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-fast-embed-provider](runtime.md#rt-cmp-fast-embed-provider) | Truth-apt content inside weights is not determinable from accessible source; extraction statements are separately listed above | see records | SRC-1, `src/llm.rs`, `src/search/fastembed_provider.rs` | Component fixity/mutability fields: see records. No training or weight-level epistemic assessment follows from their adapters. |

## Authority-route ledger

Fields owned by cited records are referenced rather than redeclared. Architectural status and the distinction between structural checks, disposition, retention and downstream use are this overlay's assessments. All implemented rows are implementation evidence, with operation uninspected.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) | content transformation | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: acquisition/import | Caller text entering chain | see route | see route | Caller text admitted, metadata normalized | Content available for later use | Source warrant unknown; content preserved by ordinary core append, not validated | Caller content becomes retrievable | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1, `src/lib.rs` | [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol) | Mandatory prior search is not enforced | Python direct writes and retrospective defaults are not acceptance events. |
| [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) | check/evidence production | implemented | [RT-OBJ-thought](runtime.md#rt-obj-thought) | no content change | References and stored sequence/hash representation | see route and runtime chain-consistency account | Append/open/explicit integrity check | Valid/invalid representation | Structural invariant under storage contract | Sequence/hash consistency only | Invalid references fail; invalid reopened chain rejected subject to legacy migration | Core append/open; enforcing; admission/reopen horizon | SRC-1, `src/lib.rs` | none | none | No statement-factuality license; downstream failure can follow canonical write. |
| [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) | disposition/acceptance | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | no content change | Candidate admission to ledger | see route | see route | Append or error | Storage admission, not epistemic acceptance | No evidence-consuming criterion for proposition truth in inspected append | Retained content may be used without semantic review | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1, `src/lib.rs`, `src/server.rs` | [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) | Review doctrine is not a universal gate | Does not exclude checks in uninspected routes or external callers. |
| [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) | retention | implemented | [RT-OBJ-thought](runtime.md#rt-obj-thought), [EPI-OBJ-thought-content](#epi-obj-thought-content) | no content change | Canonical append/reload | see route | see route | Retained record and rebuilt indexes | Later availability | Retention licenses no new factual claim | Subsequent requests can select state | see route | SRC-1, `src/lib.rs` | [EPI-CLM-context-continuity](#epi-clm-context-continuity) | Durability is conditional, completeness not guaranteed | Not lifecycle integration after epistemic acceptance. |
| [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) | operational admission/selection/consumption | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: non-ampliative reshaping | Ranked/recent context and Python prompt material | see route | see route | Scored hits/catch-up prompt/bounded string | Ranking and advisory prompt delivery | Relevance/recency and availability, not endorsement | Selected text reaches host input | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1, `src/server.rs`, `pymentisdb/langchain.py` | [EPI-CLM-context-continuity](#epi-clm-context-continuity) | Recent limit, invalidation and Python role reconstruction defeat universal faithful-history reading | Core text reshaping preserves selected statements; Python speaker attribution fidelity is degraded; host effects unobserved. |
| [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction) | content transformation | implemented | [EPI-OBJ-extracted-thoughts](#epi-obj-extracted-thoughts) | truth-apt transformation: indeterminate | Text to proposed memory statements | see route | see route | Transient candidates or error | Candidate production only | Conservative prompt is requested; no factuality license | Caller may separately discard/edit/append | Caller; API response; advisory; current request | SRC-1, `src/llm.rs`, `src/server.rs` | [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) | none | Without outputs, reshaping, entailed derivation and ampliative conjecture remain unresolved alternatives; non-entailment is not established. |
| [EPI-RTE-extraction-schema](#epi-rte-extraction-schema) | check/evidence production | implemented | [EPI-OBJ-extracted-thoughts](#epi-obj-extracted-thoughts) | no content change | JSON structure, parseable type, nonempty trimmed content | see route | see route | Schema success/error | Parser veto on return | Structural admissibility only; confidence uncalibrated | Malformed batch blocked | see route | SRC-1, `src/llm.rs` | [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) | Validation name does not mean truth validation | No source-grounding or entailment evaluator. |
| [EPI-RTE-extraction-schema](#epi-rte-extraction-schema) | disposition/acceptance | implemented | [EPI-OBJ-extracted-thoughts](#epi-obj-extracted-thoughts) | truth-apt transformation: non-ampliative reshaping | Parsed candidates to returned ThoughtInput | see route | see route | Trimmed content, clamped/default metadata, empty provenance fields | Candidate-return admission | Not accepted knowledge | Returns inputs without appending them | see route | SRC-1, `src/llm.rs`, `src/server.rs` | [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) | Caller review remains outside service gate | No lifecycle integration. |
| [EPI-RTE-relation-withdrawal](#epi-rte-relation-withdrawal) | check/evidence production | implemented | [RT-OBJ-thought](runtime.md#rt-obj-thought) | no content change | Similarity between new and recent prior text | see route | Optional dedup before append | Best Jaccard match/threshold decision | Supplies automatic Supersedes edge | Token-set overlap only, not semantic equivalence or contradiction | Can cause default withdrawal | see route | SRC-1, `src/lib.rs`, `src/search/lexical.rs` | none | Similarity does not warrant supersession | Caller relations bypass this similarity computation. |
| [EPI-RTE-relation-withdrawal](#epi-rte-relation-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | no content change | Prior thought's default availability | see route | On relation-bearing append and reopen | Target indexed as invalidated | Enforcing default selection change | Declared withdrawal, not proof of falsity or replacement truth | Default query/recent context excludes target | see route | SRC-1, `src/lib.rs`, `src/server.rs` | none | Withdrawal has force without semantic acceptance | Include-invalidated and direct lookup still expose old text; as-of uses time windows separately. |
| [EPI-RTE-summary-selection](#epi-rte-summary-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-summary-candidate](#epi-obj-summary-candidate) | no content change | Source windows and already-covered source IDs | see route | see route | Candidate source lists | Selection only | Membership under config, not adequacy of a summary | Caller gets windows to summarize later | see route | SRC-1, `src/search/summary_index.rs`, `src/lib.rs`, `src/server.rs` | [EPI-CLM-context-continuity](#epi-clm-context-continuity) | Summary candidates do not generate or check summaries | Unfiltered core variant uses all thoughts; filtered variant uses query semantics. |
| [EPI-RTE-bundle-selection](#epi-rte-bundle-selection) | content transformation | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: non-ampliative reshaping | Lexical seeds and graph-linked support | see route | see route | Grouped selected records with paths | Ranking/grouping | Graph connectivity, not evidential warrant | Groups reach requesting consumer | see route | SRC-1, `src/search/bundle.rs`, `src/lib.rs`, `src/server.rs` | none | Support label does not verify a proposition | Complete graph expansion lineage uninspected. |
| [EPI-RTE-markdown-import](#epi-rte-markdown-import) | content transformation | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: acquisition/import | Parsed MEMORY.md lines to new chain records | see route | see route | New appended records, skipped unparsed lines or error | Durable import | Source warrant unknown; lineage degraded in inspected field copy | Imported text participates in later retrieval | see route | SRC-1, `src/lib.rs`, `src/server.rs` | none | Not an identity-preserving full-ledger replay | Full parser/export semantic fidelity uninspected. |
| [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) | lineage/freshness/recovery | implemented | [RT-OBJ-thought](runtime.md#rt-obj-thought) | no content change | Branch/merge/archive state | see route | see route | Changed/recovered retained state | Administrative admission | Checksums/remapping do not establish source truth; merge lineage degraded | Later reads reflect copied/remapped state | see route | SRC-1, `src/server.rs`, `src/backup.rs` | none | Merge does not preserve all original graph metadata | Entire restore reconciliation uninspected. |
| [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | check/evidence production | implemented | [EPI-OBJ-skill-document](#epi-obj-skill-document) | no content change | Skill structure and conditional content signature | see route | see route | Import validation/signature success or error | Conditional service veto | Structure and key-possession provenance on covered path; not safety/quality | Upload admitted or refused | see route | SRC-1, `src/server.rs`, `src/skills.rs`, `src/dashboard.rs` | [EPI-CLM-fleet-improvement](#epi-clm-fleet-improvement) | Signature gate is not universal | Dashboard/direct registry alternatives and no-active-key cases. |
| [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | retention | implemented | [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry), [EPI-OBJ-skill-document](#epi-obj-skill-document) | no content change | Uploaded instruction version | see route | see route | Full/delta version persisted | Version availability | Latest is not evidence-selected better | Later reconstruction/read | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1, `src/skills.rs` | [EPI-CLM-fleet-improvement](#epi-clm-fleet-improvement) | Versioning is not improvement acceptance | Host loading/obedience and quality unobserved. |
| [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-skill-document](#epi-obj-skill-document) | non-truth-apt policy/content update: lifecycle status | Skill deprecation/revocation | see route | see route | Status/reason retained | Enforcing status write; advisory downstream restriction | Caller declares concern; no automatic correctness judgment | Consumers receive status, not enforced execution ban | see route | SRC-1, `src/skills.rs` | none | Revoked content remains readable | Host must interpret the signal; delete is a separate removal operation. |
| [EPI-RTE-recall-evaluation](#epi-rte-recall-evaluation) | check/evidence production | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: entailed derivation | LongMemEval retrieved top-k versus dataset evidence | see route | Explicit benchmark invocation | Boolean hit and aggregate recall | Diagnostic metric only | Substring metric under given references/k; not generated-answer truth | Printed/returned diagnostics; no live memory acceptance consumer traced | see route | SRC-1, `lme-benches/longmemeval_bench.py` | none | Empty or partial text can satisfy matcher | No run, dataset validation or causal contrast supplied. |
| [EPI-RTE-recall-evaluation](#epi-rte-recall-evaluation) | check/evidence production | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: entailed derivation | ConvoMem ordinary evidence retrieval and abstain category | see route | Explicit benchmark invocation | Hit, or negated hit for abstain | Diagnostic metric only | Absence of substring evidence, not observed model abstention | Category counters/printed report | see route | SRC-1, `lme-benches/convomem_bench.py` | none | Abstain metric does not call a task-answer model | References and provider/source truth unverified. |
| [EPI-RTE-recall-evaluation](#epi-rte-recall-evaluation) | check/evidence production | implemented | [EPI-OBJ-thought-content](#epi-obj-thought-content) | truth-apt transformation: entailed derivation | LoCoMo returned text versus target/neighbor evidence | see route | Explicit benchmark invocation | Substring hit under expanded evidence | Diagnostic metric only | Retrieval against broadened reference set | Recall/miss diagnostics; no deployment gate evidenced | see route | SRC-1, `locomo-benches/locomo_bench.py` | none | Neighbor evidence is not exact target recovery | Full aggregate consumer not independently reread; no measured outcomes. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol) | see record | SRC-1, `MENTISDB_SKILL.md`; doctrine/design | see record | [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [RT-BAP-core-skill](runtime.md#rt-bap-core-skill) | none supplied | Host behavior not captured | Startup/search/checkpoint instructions are available | Not enforced by append; automatic Python writes are a counterroute. |
| [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) | see record | SRC-1, `src/llm.rs`; doctrine/design | see record | [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction), [EPI-RTE-extraction-schema](#epi-rte-extraction-schema) | none supplied | No caller review trace | Candidate return is separate from durable append | Schema gate cannot stand in for factual review. |
| [EPI-CLM-context-continuity](#epi-clm-context-continuity) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [EPI-RTE-summary-selection](#epi-rte-summary-selection) | none supplied | No checkpoint fidelity/task continuation test or contrast; external host compaction excluded | Durable records and selective later context afford continuity | Zero loss/all decisions is not licensed by limited/filtered recent context or unverified caller summaries. |
| [EPI-CLM-fleet-improvement](#epi-clm-fleet-improvement) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal), [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | none supplied | No evidence-directed update or before/after performance comparison; signer identity does not supply quality evidence | Updated instruction versions can be stored, reconstructed and returned | Better skills, exercised fleet learning and self-improvement unestablished. |

## Bounded conclusion

MentisDB implements acquisition and durable operational use of caller text. Ordinary core append preserves supplied content while constructing metadata, relations and hashes. Source warrant is unknown: the append gate does not compare statements with world evidence. Structural checks license sequence/reference integrity, and conditional skill signatures license a bounded provenance claim, not factual accuracy or safe instructions. [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

Extraction implements model candidate generation followed by schema-return admission. Its requested conservatism does not establish entailment. Without an input/output instance, it is not determinable whether a returned statement imports, merely reshapes, derives or conjectures beyond its input. The inspected parser checks type and nonempty content and reshapes metadata; it consumes no evidence for claim truth, intended use or scope. The service returns candidates without persisting them. Caller review is declared, not demonstrated or universally enforced. [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction), [EPI-RTE-extraction-schema](#epi-rte-extraction-schema), [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review).

Withdrawal is consequential even without acceptance. Caller Corrects/Invalidates/Supersedes edges and optional token-set deduplication suppress earlier text in default retrieval; they do not establish the old proposition's falsity or the new proposition's truth. Direct lookup/include-invalidated alternatives limit the withdrawal horizon. Skill revocation persists a lifecycle signal but still allows read-back; the downstream consumer must honor it. These are ledger/policy functions, not lifecycle integration after evidence-consuming epistemic acceptance. [EPI-RTE-relation-withdrawal](#epi-rte-relation-withdrawal), [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal).

Recent/ranked read-back, graph bundles and source-window candidates select and regroup existing material. Bundle support means graph support, not verified evidential support. Summary candidates produce source IDs, not accepted summaries. The unfiltered summary path even begins with all thoughts rather than ordinary query filtering. Markdown import and merge retain text while losing some original lineage/relations; their new hashes cannot restore that warrant. The Python adapter's speaker reconstruction degrades transcript fidelity. No universal zero-loss result follows. [EPI-RTE-bundle-selection](#epi-rte-bundle-selection), [EPI-RTE-summary-selection](#epi-rte-summary-selection), [EPI-RTE-markdown-import](#epi-rte-markdown-import), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip).

The inspected benchmark matchers derive bounded Boolean/aggregate claims from reference strings and returned text. They do not validate reference truth, generated answers, explanations, source fidelity or transferable task improvement. ConvoMem's abstain category checks lack of evidence-string match, not an answer model declining to answer. No benchmark result or independent causal intervention was supplied. [EPI-RTE-recall-evaluation](#epi-rte-recall-evaluation).

Retained memories and instructions have an implemented host-input path: API responses and Python prompt-string delivery are advisory to a human/model, selected by symbolic code, and can extend across sessions. Activation, obedience and benefit remain unobserved. No evidence-consuming acceptance of an ampliative claim or post-acceptance lifecycle integration was found in the inspected append, extraction, summary, import, bundle and skill routes; uninspected relevant operations prevent a system-wide absence claim. There is direct policy-state change through skill lifecycle and operator-selected versions, but no traced evaluation-driven behavior adaptation in these paths. The supplied model components remain separately bounded; no weight training inference is justified. [RT-BAP-retained-context](runtime.md#rt-bap-retained-context), [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-fast-embed-provider](runtime.md#rt-cmp-fast-embed-provider).

The fleet-improvement claim has no independently evaluated objective/update pair in the supplied evidence. Version storage and potential read-back establish neither that evaluation caused a better update nor that later operation causally depended on it. Learning, reflection, autonomy, content-directed theory criticism and exercised self-improvement are not inferred from one another or from persistence. Concrete skill content and update episodes would be needed to assess theory-builder conditions independently; this report does not turn opaque models or unavailable episodes into a system-wide negative. [EPI-CLM-fleet-improvement](#epi-clm-fleet-improvement).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-thought-content
Label: Thought content

Part of: [RT-OBJ-thought](runtime.md#rt-obj-thought)

Source-native identity: `Thought.content` and incoming `ThoughtInput.content`. Representational form: natural-language text interpreted by later humans/models, separate from the symbolic thought envelope. Storage substrate: the parent's canonical storage and selected prompt/API copies. Candidate truth-apt content depends on actual text; the thought type alone is insufficient. SRC-1, `src/lib.rs`. This material part is distinct from the envelope's fixed hash/filter consumer. The supplied [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) covers its admission and read-back; it does not establish factuality.

> thought_type: input.thought_type,
> role: input.role,
> content: input.content,
> confidence: input.confidence.map(|value| value.clamp(0.0, 1.0)),
> --- `src/lib.rs`

Retrospective admission is the same content path, not an internal analysis of observed outcomes. SRC-1, `src/server.rs`:

> let mut input = ThoughtInput::new(thought_type, request.content)
>     .with_agent_name(agent_name)
>     .with_role(ThoughtRole::Retrospective)
>     .with_importance(request.importance.unwrap_or(0.7))
> --- `src/server.rs`

#### EPI-OBJ-extracted-thoughts
Label: Extracted ThoughtInput candidates

Source-native identity: returned `ExtractionResult.thoughts`, created from `RawExtractedThought`. Representational form: natural-language statements plus symbolic type/confidence/importance/tag envelope. Storage substrate: transient result vector, not durable chain state in this route. Distinct identity from [EPI-OBJ-thought-content](#epi-obj-thought-content): these candidates exist before and independently of append; possible later content duplication requires caller admission. Closest supplied counterpart [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction) is their producer, not the candidate object. SRC-1, `src/llm.rs`, `src/server.rs`.

> Ok(ExtractMemoriesResponse {
>     thoughts: result.thoughts,
>     model: result.model,
>     usage: result.usage,
> })
> --- `src/server.rs`

The content has no automatically preserved source-episode or statement evidence link in the transformation:

> refs: Vec::new(),
> relations: Vec::new(),
> entity_type: None,
> source_episode: None,
> --- `src/llm.rs`

#### EPI-OBJ-skill-document
Label: Skill instruction document

Part of: [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry)

Source-native identity: reconstructed `SkillReadOutput.content`. Representational form: natural-language instruction/premise bodies inside Markdown or JSON export, distinct from the registry's symbolic version/lifecycle machinery. Storage substrate: parent's stored full/delta versions; read result is a transient rendered copy. Concrete uploaded content is uninspected. Evidence and closest admission counterpart: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), SRC-1, `src/skills.rs`.

> let snapshot = read_skill_from_entry(skill_id, entry, version_id, format)?;
> Ok(SkillReadOutput {
>     content: snapshot.content,
>     warnings: snapshot.warnings,
>     status: entry.status,
> })
> --- `src/skills.rs`

#### EPI-OBJ-summary-candidate
Label: SummaryCandidate source window

Source-native identity: `SummaryCandidate`, source_indices/source_ids/group/start_index/end_index. Representational form: symbolic source membership, not generated natural-language summary. Storage substrate: returned in-memory candidate list. No supplied object counterpart after comparison with [RT-OBJ-thought](runtime.md#rt-obj-thought); it points to several thought records without containing their content and is not a part of one thought. SRC-1, `src/search/summary_index.rs`.

> /// Deterministic source set that a caller may summarize and append later.
> #[derive(Debug, Clone, PartialEq, Eq)]
> pub struct SummaryCandidate {
> --- `src/search/summary_index.rs`

### Routes

#### EPI-RTE-extraction-schema
Label: Extraction schema gate

Part of: [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction)

Endpoints/progression: raw model response → JSON deserialization → `validate_and_transform_thoughts` → returned candidate vector/error. Owner: Rust parser/transformer; external model proposes statements and caller chooses whether to persist. Context/state/action effects: checks schema and transforms a transient envelope; no durable content or behavioral policy update. Target/domain: JSON thought array, parseable thought type and nonempty content, not statement accuracy. SRC-1, `src/llm.rs`, `src/server.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: transformed candidate inputs or parse/schema error; a bad type/empty content aborts the batch result.
- Later read-back: inapplicable — candidate return is not persisted; separate append is required.
- Delegated visibility: uninspected — caller gets result and remote provider sees input; provider retention/delegates are not captured.
- Selection predicate: first provider response choice, parseable JSON thoughts, recognized thought_type and nonempty trimmed content.
- Invalidation or expiry: inapplicable — this transient route has no retained lifecycle.
- Activation or effect: malformed candidates can be blocked from return; successful candidates are reshaped, not endorsed.
- Evidence limits: no input/output trace, source-truth evaluator, calibration or caller-review observation.

Open opt-in requests supply input/templates; the model proposes, code vetoes structure, and the caller can discard or edit output. Human per-candidate contribution is unresolved. Answer oracle: inapplicable — no expected factual answer is consulted. No server-controlled improvement curriculum is implemented by this gate. Trigger/proposed change: caller requests extracted memory statements. Admission is candidate-return admission only; there is no persisted update to roll back. Proposal guidance requests conservative explicit/strongly-implied facts; custom templates can replace it. Guidance persists in source, not as an attached acceptance rationale on the returned inputs.

> 2. Be conservative: only extract what is explicitly stated or strongly implied
> --- `src/llm.rs`

> let content = raw.content.trim();
> if content.is_empty() {
>     return Err(LlmExtractionError::SchemaMismatch(format!(
>         "Empty content at index {}",
>         i
>     )));
> }
> --- `src/llm.rs`

> let importance = raw.importance.unwrap_or(0.5).clamp(0.0, 1.0);
> let confidence = raw.confidence.unwrap_or(0.5).clamp(0.0, 1.0);
> --- `src/llm.rs`

Behavioral-authority path: extraction caller consumes the API result; the parser is enforcing on candidate return, while the statements are advisory. Horizon: this request unless the caller separately admits them to retained memory.

Concrete deterministic deduction, not target execution: a valid raw type with content `"  Paris is in France.  "` and omitted confidence passes the inspected nonempty/type gates and yields trimmed content `"Paris is in France."` with confidence 0.5. Neither that default nor clipping a supplied 2.0 to 1.0 consumes geographical evidence. The string transformation is non-ampliative; model generation before it remains indeterminate.

#### EPI-RTE-relation-withdrawal
Label: Relation driven withdrawal

Part of: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)

Endpoints/progression: caller relation or configured token-set dedup → append relation → invalidated-ID index → default query/recent-context exclusion. Owner: caller proposes explicit relations; code chooses optional most-similar prior target and enforces exclusion. Context/state/action effects: adds symbolic relation/withdrawal state without deleting or proving claims. SRC-1, `src/lib.rs`, `src/search/lexical.rs`, `src/server.rs`. This is a material subroute of the supplied roundtrip, separating its check and disposition functions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: append result with relations, or error; successful storage admission can precede downstream failure.
- Later read-back: invalidation set rebuilds from retained relations on open; default query/recent-context selection omits targets.
- Delegated visibility: accessible-chain clients receive the filtered result; callers can separately retrieve old records.
- Selection predicate: explicit Supersedes/Corrects/Invalidates target IDs, or optional best normalized-token Jaccard match within recent scan window at configured threshold.
- Invalidation or expiry: old record remains canonical; include-invalidated bypasses default selection and direct get_thought does not apply that filter; as-of predicate honors relation/time windows separately.
- Activation or effect: sets operational withdrawal and changes default later selection; no observed host behavior.
- Evidence limits: no entailment, contradiction, equivalent-meaning or replacement-quality check; complete cross-chain relation semantics uninspected.

Admission is open relation-bearing writes, with optional automatic similarity proposal. Code decides membership/exclusion; callers can withhold input, and structural/I/O checks can veto admission. Human truth judgment is not required. Answer oracle: inapplicable — token sets are not expected answers. Trigger/proposed change: append a replacement/correction/invalidation or near-duplicate; ordinary ledger admission persists relations. Rollback/recovery is limited to alternate/history reads and later caller changes, not demonstrated automatic reversal. Guidance: relation kinds and similarity threshold define operational rules, not a criticism rationale; any natural-language criticism depends on caller text.

> let intersection = new_tokens.intersection(&prior_tokens).count() as f32;
> let union = new_tokens.union(&prior_tokens).count() as f32;
> if union == 0.0 {
>     continue;
> }
> let similarity = intersection / union;
> --- `src/lib.rs`

> // Update the invalidated-thoughts index if this thought contains
> // Supersedes, Corrects, or Invalidates relations.
> for relation in &self.thoughts.last().unwrap().relations {
>     if is_invalidating_relation_kind(relation.kind) {
>         self.invalidated_thought_ids.insert(relation.target_id);
>     }
> }
> --- `src/lib.rs`

> let include_invalidated = request.include_invalidated.unwrap_or(false);
> let thoughts: Vec<&crate::Thought> = if let Some(ref agent_id) = request.agent_id {
> --- `src/server.rs`

Behavioral-authority path: core query/recent-context code consumes the retained invalidation-ID set through a symbolic predicate with enforcing selection force across later requests/reopens. The host then receives selected natural-language text through the advisory context channel. As-of/include-invalidated/direct-lookup alternatives bound that force.

A concrete deduction illustrates the evaluator's domain: two identical nonempty input strings necessarily yield the same normalized token set; where that set is nonempty, their Jaccard similarity is 1.0. This establishes token identity, not truthful content. The implementation also accepts explicit withdrawal edges without first performing that similarity check. No semantic correctness claim follows.

#### EPI-RTE-summary-selection
Label: Summary source selection

Endpoints/progression: core/service summary-candidates request → optional query filter → source metadata/coverage extraction → grouped windows → paginated source lists. Owner: caller chooses filters/config; fixed Rust selector decides windows. Context/state/action effects: read-only selection; no summary generated, appended or accepted. No supplied route counterpart after comparison: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) covers ordinary memory read/write, while this selector returns source sets for a later caller operation. SRC-1, `src/lib.rs`, `src/search/summary_index.rs`, `src/server.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deterministic candidate windows or empty list, paginated by service.
- Later read-back: inapplicable — selector does not persist its result; caller-created summary needs separate append.
- Delegated visibility: requesting caller receives source locators; shared-chain callers can independently repeat selection.
- Selection predicate: append-index sort, optional session/agent/entity grouping, window size/overlap; omit windows whose every source is covered by stored same-chain Summarizes target IDs.
- Invalidation or expiry: no candidate lifecycle; unfiltered summary_candidates uses all thoughts, while matching variant first calls query; coverage scans all stored relations without a semantic-adequacy test.
- Activation or effect: returns work candidates and skips declared covered windows; no implementation of model summarization in this selector.
- Evidence limits: Summarizes assertion is not verified coverage of decisions; no actual summary or acceptance episode supplied.

Caller proposes source scope, code selects, caller can ignore or request another scope. Human summarizer contribution is unresolved. Answer oracle: inapplicable — coverage is symbolic target membership, not a reference summary. Operating mode: open read requests; future summary-writing trigger is caller-owned. No knowledge update is admitted here.

> /// This type only controls source selection. It does not create, append, or
> /// persist summary thoughts.
> --- `src/search/summary_index.rs`

> if !covered.covers_all(window) {
>     candidates.push(candidate_from_window(window, group.clone()));
> }
> --- `src/search/summary_index.rs`

> .filter(|relation| {
>     relation.kind == ThoughtRelationKind::Summarizes && relation.chain_key.is_none()
> })
> .map(|relation| relation.target_id.to_string())
> --- `src/lib.rs`

Behavioral-authority path: requesting caller consumes source-ID lists over the API; selection is enforcing on the returned list, advisory as a summarization work proposal. Horizon: current request; claimed Summarizes coverage persists in source records and can affect later candidate requests.

Concrete source deduction: two source records at indices 0 and 1 in one group, window_size 2 and no coverage produce the source window [0,1]. Mark both IDs covered and that window is omitted, regardless of whether the text of the alleged summary mentions either decision. This is selection under declarations, not a semantic summary-quality evaluator.

#### EPI-RTE-bundle-selection
Label: Context bundle selection

Endpoints/progression: query → candidate filtering/lexical scoring → seed locators → optional graph expansion → grouping/dedup → response thoughts/path metadata. Owner: caller supplies request; core/service code determines result. Context/state/action effects: reorganizes selected retained statements beneath seeds without changing their text. Distinct from [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)'s flat hit/recent-context return; no supplied bundle counterpart found. SRC-1, `src/lib.rs`, `src/search/bundle.rs`, `src/server.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bundles with seed thoughts, linked support thoughts, relation/path/depth metadata; empty without text or seeds.
- Later read-back: retained thoughts are the sources of a later requested bundle; bundle assembly itself does not persist a new memory.
- Delegated visibility: requesters with chain access receive returned bundle; actual host interpretation uninspected.
- Selection predicate: query/filter/invalidated/as-of options, lexical seeds, optional graph hits; dedup seed locators and group support under matching path.seed.
- Invalidation or expiry: source visibility is filtered at retrieval; transient bundles have no independent lifecycle.
- Activation or effect: grouping/selection affects model-visible response; no claim evidence is accepted and no observed behavior change.
- Evidence limits: full graph expansion and all cross-chain lookup cases uninspected; path existence is not truth support.

Selection is fixed computation on caller requests, not human per-record approval. Caller can ignore response; no factual answer oracle is used. Mode is open retrieval. No retained knowledge/instruction update is admitted.

> let Some(&bundle_index) = seed_positions.get(&hit.path.seed) else {
>     continue;
> };
> --- `src/search/bundle.rs`

> ContextBundleHitResponse {
>     locator,
>     thought: thought_json_for_locator(&chain, &support_hit.locator),
>     depth: support_hit.depth,
>     seed_path_count: support_hit.seed_path_count,
> --- `src/server.rs`

Behavioral-authority path: requesting human/model consumes bundled thoughts and paths over the API; source selection/grouping has ranking force, and returned statements have advisory force. Horizon: this response, or later requests while its source records remain accessible; no retained bundle update is made.

Concrete grouping deduction: a graph hit whose path.seed is absent from the seed-position map is skipped; a matching hit is assigned to that seed's bundle. This establishes membership/connectivity under inputs, not an evidence-consuming inference about any returned proposition.

#### EPI-RTE-markdown-import
Label: Markdown memory import

Endpoints/progression: explicit import request → line parser → new ThoughtInput selected fields → shared append for each parsed line → returned indices/count. Owner: caller supplies text/default attribution; parser and core admit. Context/state/action effects: durable text import with new envelope identities and incomplete original metadata. Distinct from [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance)'s archive/merge transformation and from ordinary [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip); overlap is the downstream append, not input grammar/lineage. SRC-1, `src/lib.rs`, `src/server.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: new indices/count or append error; unparsed lines are skipped.
- Later read-back: new thoughts participate in later chain query/context and reopen.
- Delegated visibility: accessible-chain consumers can retrieve imported state.
- Selection predicate: parse_memory_markdown_line succeeds; parsed agent ID or caller default; copy type/content/role/importance/tags/optional confidence.
- Invalidation or expiry: shared append/invalidation rules apply; inspected copy does not restore original relation/ref graph or source_episode.
- Activation or effect: appends retained text; new identifiers/hashes do not preserve original evidence linkage.
- Evidence limits: parser/export bodies not fully inspected; exact semantic round-trip fidelity and all accepted formats unassessed.

Behavioral-authority path: shared append admits new records with enforcing storage/selection effects; later host consumers receive imported text through ordinary API/context responses, with advisory force across later requests/sessions. Source graph omissions persist in that reconstructed ledger.

Open explicit import admits knowledge-shaped text, not accepted knowledge. Caller proposes and can cancel; code skips malformed lines and I/O can veto subsequent appends. Human review is unresolved. Answer oracle: inapplicable — no factual reference. Trigger is import request; guidance is Markdown grammar and caller content, not a truth criterion. Rollback: no transaction-wide rollback in this loop; earlier appends can remain if a later append errors. Recovery uses ordinary chain/history/administrative routes.

> let mut input = ThoughtInput::new(parsed.thought_type, parsed.content)
>     .with_role(parsed.role)
>     .with_importance(parsed.importance)
>     .with_tags(parsed.tags);
> if let Some(conf) = parsed.confidence {
>     input = input.with_confidence(conf);
> }
> let thought = self.append_thought(agent_id, input)?;
> indices.push(thought.index);
> --- `src/lib.rs`

#### EPI-RTE-skill-withdrawal
Label: Skill lifecycle withdrawal

Part of: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Endpoints/progression: explicit deprecate/revoke request → status/reason/index/persist update → read returns body, warnings and lifecycle status. Owner: caller decides concern; registry records/enforces metadata. Context/state/action effects: policy state changes; body need not change and read is not blocked. SRC-1, `src/skills.rs`. This material lifecycle part separates disposition from the parent's upload/check/retention functions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated skill summary or missing-entry/persistence error.
- Later read-back: read still reconstructs body and returns entry.status; deprecated/revoked versions remain for audit.
- Delegated visibility: accessible registry consumers receive lifecycle signal with content; actual adherence uninspected.
- Selection predicate: explicit skill ID and caller reason; no automatic content correctness evaluator.
- Invalidation or expiry: revocation preserves history and status across upload per supplied runtime; delete is the separate permanent-removal operation.
- Activation or effect: status/index/persistence changes are wired; downstream nonexecution is an instruction to consumers, not an enforced read ban.
- Evidence limits: callers' evidence for concern and downstream execution checks are uninspected; no observed rollback of host behavior.

Behavioral-authority path: registry read/search consumers receive persisted lifecycle state through symbolic status fields and exported content; the status update is enforcing on registry metadata, but nonexecution is advisory to the host. Horizon: subsequent reads while the entry is retained, not automatic rollback of instructions already delivered.

Open lifecycle requests change policy. Caller proposes/decides concern, code can reject missing ID or failed I/O; whether caller is human is unresolved. Answer oracle: inapplicable — no expected task output. Trigger/proposed change is caller-selected retirement; an optional reason persists alongside status, not a verified criticism. Recovery includes reading prior versions and publishing another skill; automatic behavioral rollback is unestablished. The doctrine asks agents not to apply revoked instructions, but the read implementation is a countercase to universal enforced withholding.

> entry.status = SkillStatus::Revoked;
> entry.status_reason = normalize_optional(reason);
> entry.updated_at = Utc::now();
> --- `src/skills.rs`

> /// correctness concern** that makes the skill unsuitable for use.  Agents
> /// and callers must treat revoked skills as untrusted and must not execute
> /// or apply them.
> --- `src/skills.rs`

Read's consequential output is retained in [EPI-OBJ-skill-document](#epi-obj-skill-document)'s quotation; it has no status-based rejection branch.

#### EPI-RTE-recall-evaluation
Label: Retrieval recall evaluation

Endpoints/progression: explicit benchmark driver invocation → ingest/reference extraction → ranked retrieval → substring predicate → counters/recall/miss diagnostics. Owners: driver author defines predicate/reference treatment; runner chooses parameters/dataset; deterministic Python code scores. Context/state/action effects: dataset conversation text is ingested in benchmark chains; metrics diagnose retrieval, not deployed memory acceptance. No supplied evaluator route counterpart after comparison with [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip); it invokes retrieval but has separate reference and metric consumers. SRC-1, `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hit Booleans, aggregate counters/recall and diagnostic reports, or driver errors.
- Later read-back: driver-ingested records can remain in benchmark chains; metric output is not connected to later agent prompt selection in inspected code.
- Delegated visibility: runner receives metrics/diagnostics; benchmark state is available to clients with its chain access; actual audiences uninspected.
- Selection predicate: LongMemEval uses answer_session_ids/has_answer evidence or answer fallback and top-k bidirectional substring containment; ConvoMem uses message_evidences and negates match for abstain; LoCoMo broadens target evidence with session neighbors before the same containment test.
- Invalidation or expiry: no epistemic candidate lifecycle is scored; ConvoMem switches chain key between items; live cleanup/isolation outcomes unobserved.
- Activation or effect: hit changes counters and miss diagnostic membership; no live acceptance, policy update or task-answer consumer traced.
- Evidence limits: no execution/results/intervention; datasets not substantively verified; incomplete driver coverage prevents certifying every evaluator or production feedback path.

Behavioral-authority path: driver aggregation consumes hit Booleans over function results with enforcing counter/miss-selection force during the benchmark invocation; human runners receive printed/returned diagnostic reports with advisory force. No longer-horizon deployment or memory-admission consumer is evidenced.

Target and domain are separate by driver. LongMemEval checks occurrence of any gold evidence/answer text in returned top-k (or returned text in evidence); it does not score an answer generator. ConvoMem ordinary categories use the same string relation; abstain checks its negation, not model refusal. LoCoMo uses expanded target/neighbor evidence, so matching a neighbor can count. References are dataset-provided expected evidence, not model judgment. Runner selects inputs/k, code decides metrics, and a human can interpret or discard diagnostics; no automatic production successor selection is implemented in the inspected consumers. Operating mode: bounded offline evaluation of given dataset requests, not ordinary append. No knowledge/instruction update is admitted by its score.

> def _hit(evidence_texts: list[str], results: list[dict], k: int) -> bool:
>     """True if any gold evidence text is subsumed by any of the first k results."""
>     contents = [r["thought"].get("content", "").strip().lower() for r in results[:k]]
> --- `lme-benches/longmemeval_bench.py`

> if ev_l in c or c in ev_l:
>     return True
> --- `lme-benches/longmemeval_bench.py`

> if hit_k:
>     s["correct"] += 1
> --- `lme-benches/longmemeval_bench.py`

> def _abstain_hit(evidence_texts: list[str], thoughts: list[dict]) -> bool:
>     """For abstention: correct when the evidence is NOT surfaced (model should say 'I don't know')."""
>     return not _hit(evidence_texts, thoughts)
> --- `lme-benches/convomem_bench.py`

> if hit:
>     correct += 1
> --- `lme-benches/convomem_bench.py`

> if abs(tn - tnum) <= _NEIGHBOR_RADIUS and txt not in seen:
>     texts.append(txt)
>     seen.add(txt)
> --- `locomo-benches/locomo_bench.py`

Concrete code deductions, not execution: evidence `"Paris is in France"` and returned content `"Paris"` produce a hit through `c in ev_l`, despite omitting the proposition. A returned empty content also satisfies that direction for nonempty evidence; an empty fallback evidence matches any returned string in the other direction. Conversely, in ConvoMem abstain, a list with no matching evidence counts as correct without consulting an answer model. These are exact predicate-domain consequences, not observations of benchmark inflation or deployed failures. Aggregate recall is entailed only from these hit results and chosen denominator; it does not establish geographical truth, answer completeness or causal retrieval quality.

### Claims

#### EPI-CLM-context-continuity
Label: Claimed zero loss continuity

Claimed operation/warrant: summary checkpoint, compaction and recent-context reload lose no decision; returning agents know exact project state without new investigation. Source: SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol): that record declares required procedure; this record concerns the stronger losslessness/state-knowledge outcome.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> **Zero Knowledge Loss Across Context Boundaries** — when an agent's context window fills, it writes a `Summary` checkpoint to MentisDB, compacts, reloads `mentisdb_recent_context`, and continues without losing a single decision. Chat history is ephemeral. MentisDB is permanent.
> --- `README.md`

> **Session Resurrection** — any agent can call `mentisdb_recent_context` and immediately know exactly where the project stands, what decisions were made, what traps were already hit, and what comes next — without re-reading code, re-running exploratory searches, or asking the human to re-explain context that was earned through hours of work.
> --- `README.md`

Countercase: default recent context takes twelve selected non-invalidated thoughts, not the entire ledger; summary selector does not test summary completeness. See [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [EPI-RTE-summary-selection](#epi-rte-summary-selection). Durable storage can support continuity without licensing this universal warrant.

#### EPI-CLM-fleet-improvement
Label: Claimed fleet skill improvement

Claimed operation/warrant: agents learn, upload updated skills, and the skills are better by project end; signing makes authorship provenance verifiable. Source: SRC-1, `README.md`, doctrine/design. No supplied claim counterpart after comparison with [RT-CLM-extraction-review](runtime.md#rt-clm-extraction-review) and [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol); this is a quality/change attribution, not extraction review or startup procedure.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> **Self-Improving Agent Fleets** — agents upload updated skill files after learning something new. A skill checked in at the start of a project is better by the end of it. Combine with Ed25519 signing to create a verifiable, tamper-evident record of which agent authored which version of institutional knowledge.
> --- `README.md`

The supported architectural part is instruction-version retention/return and conditional covered-path signature verification, not accepted better performance or universally verified authorship. See [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Objective independent of the update, evaluation-caused determination, later live host consumption, and causally dependent improved subsequent behavior were not supplied. This prevents exercised self-improvement attribution over a project horizon, without denying the operational availability of versioned instructions.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; the closest existing paths are [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) and [RT-BAP-core-skill](runtime.md#rt-bap-core-skill). New route-local selectors and diagnostic consumers above have their consumer/channel/force/horizon stated separately; no distinct observed behavioral activation is asserted.
