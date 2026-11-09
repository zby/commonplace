---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MDCP epistemic routes: source-shard reliance, structural checks, evidence links, research doctrine and maintainer evaluation."
run-id: AAS-2026-11-08-mdcp-1e4e8314c1e4-01
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
---

# MDCP epistemic report

## Source-and-claim boundary

This overlay assesses the whole shipped documentation loop under the [boundary and Source register](boundary.md#source-register), SRC-1. The question is what licenses reliance on source shards and derivatives, rather than whether compilation succeeds. External host inference, peer implementations, installed dependencies and successor Merlon are not frozen. No run or experiment is registered: actual compliance, accepted novel claims, later activation and comparative benefit are unestablished.

Direct inspection here covers CLI dispatch including standalone fix/lint/prose/links, the public core surface, callback execution, code-evidence and insert hooks, the path probe, review interfaces, semantic review instructions, research archetype and remote-session installer. Other coverage below is supplied runtime evidence, not claimed direct inspection. These additions use SRC-1 at the same frozen commit. No target execution was performed.

| Entry point or operation | Source path in SRC-1 | Coverage and records |
| --- | --- | --- |
| Host feature work, discovery and later shard reads | `skills/mdcp/SKILL.md`; `skills/mdcp/references/workflows/feature-level.md` | Supplied [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host); host processing uninspected |
| Compile, refs-gen/check/list; removed export | `packages/mdcp-cli/src/cli.ts` | Direct dispatch; supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check); export exits rather than supplies context |
| Check, lint, prose, links | `packages/mdcp-cli/src/cli.ts` | Direct dispatch/check consumer; supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check); external peer judgments remain opaque |
| Fix | `packages/mdcp-cli/src/cli.ts` | Direct [EPI-RTE-peer-fix](#epi-rte-peer-fix); omitted standalone mutation in runtime narrative is added, not a contradiction |
| Shard | `packages/mdcp-core/src/shard/orchestrator.ts` | Supplied [RT-RTE-shard-import](runtime.md#rt-rte-shard-import); parser semantics not frozen |
| Public APIs and registered hooks | `packages/mdcp-core/src/index.ts`; `packages/mdcp-core/src/compile/hooks.ts` | Direct API/callback inspection; supplied [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension); new hook parts below |
| Code evidence, inserts | `packages/mdcp-core/src/compile/hooks/code-evidence.ts`; `packages/mdcp-core/src/compile/hooks/inline-inserts.ts` | Direct [EPI-RTE-code-evidence](#epi-rte-code-evidence), [EPI-RTE-inline-inserts](#epi-rte-inline-inserts) |
| Path checks | `packages/mdcp-core/src/validate/path-probe.ts` | Direct recognizer/evaluator; CLI consumer; [EPI-RTE-path-probe](#epi-rte-path-probe) |
| Review and semantic cleanup | `packages/mdcp-core/src/validate/review.ts`; `skills/mdcp/references/workflows/doc-review.md`; `skills/mdcp/references/review/lenses.md` | Direct interfaces/normalization and complete workflow/lenses; supplied [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) |
| Research evidence and specification | `skills/mdcp-arch-research/SKILL.md` | Direct [EPI-CLM-research-warrant](#epi-clm-research-warrant), [EPI-CLM-structure-truth](#epi-clm-structure-truth) |
| Site publication, backup and registry persistence | `packages/mdcp-site/scripts/sync-content.mjs`; `packages/mdcp-core/src/compile/write-output.ts`; `packages/mdcp-core/src/refs/registry.ts` | Supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check); no publication outcome |
| Context-size benchmark and conditional public claim | `scripts/bench-context-size.mjs`; `docs/features/protocol/benefit-claims-and-evidence.md`; `docs/features/protocol/context-size-dogfood.csv` | Direct [EPI-RTE-context-size](#epi-rte-context-size), [EPI-CLM-context-size](#epi-clm-context-size); static report, not observed agent savings |
| Evaluation/optimization | `.agents/skills/skill-creator/scripts/run_loop.py`; `docs/developer/live-skill-evals.md` | Supplied [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation), [RT-CMP-claude](runtime.md#rt-cmp-claude); not independently re-inspected |
| CI/release and session-start hook | `.github/workflows/ci.yml`; `.github/workflows/release.yml`; `.claude/hooks/session-start.sh` | Supplied [RT-RTE-release-admission](runtime.md#rt-rte-release-admission); hook directly read: remote-session installation, not truth evaluation |

Additional direct correction inspection covers SRC-1, `docs/features/protocol/benefit-claims-and-evidence.md`, `docs/features/protocol/context-size-dogfood.csv` and `scripts/bench-context-size.mjs`: reported static size evidence and its measurement implementation, not a newly observed run.

Other included archetype/bootstrap workflows, individual research artifacts, presets, test assertions and evaluator-helper internals were not exhaustively assessed. Their availability is not an access gap. This prevents a system-complete negative about semantic evaluation or knowledge production. No result from an uninspected research artifact is inferred. The bounded research doctrine is a positive warrant prescription; it must not be collapsed into “MDCP only formats text.”

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp) | Vendor skill/workflow instructions; normative instructions are not themselves observations | see record | SRC-1, `skills/mdcp/SKILL.md` | Vendor policy only; mutable project assertions belong to the separate source-shard record |
| [MEM-OBJ-shards](memory.md#mem-obj-shards) | Mutable project intent/contracts and factual assertions | see record | SRC-1, `skills/mdcp/SKILL.md` | Distinct from vendor policy; individual accepted claims unavailable |
| [EPI-OBJ-document-body](#epi-obj-document-body) | Selected shard prose and transformed compile body | see record | SRC-1, `packages/mdcp-core/src/compile/hooks.ts` | Derivative content, not configuration |
| [EPI-OBJ-skill-description](#epi-obj-skill-description) | Candidate trigger-scope policy, not project assertions | see record | SRC-1, `.agents/skills/skill-creator/scripts/run_loop.py` | Candidate descriptions are not the installed vendor policy |
| [EPI-OBJ-context-size](#epi-obj-context-size) | Reported static sizes and ratios | see record | SRC-1, `docs/features/protocol/context-size-dogfood.csv` | Not a transcript or causal experiment |
| [RT-OBJ-config](runtime.md#rt-obj-config) | None intrinsically; gate/selection policy | see record | SRC-1, `packages/mdcp-core/src/config/schema.ts` | Symbolic policy validity is not policy adequacy |
| [EPI-OBJ-evidence-links](#epi-obj-evidence-links) | A file/line association, not proof that surrounding prose follows | see record | SRC-1, `packages/mdcp-core/src/compile/hooks/code-evidence.ts` | First occurrence is not declaration resolution |
| [EPI-OBJ-insert-body](#epi-obj-insert-body) | Imported table/diagram/media prose where truth-apt; particular proposition not determinable without selected payload | see record | SRC-1, `packages/mdcp-core/src/compile/hooks/inline-inserts.ts` | Body copying preserves text, not warrantedness |
| [EPI-OBJ-path-claims](#epi-obj-path-claims) | Recognized repository path exists within searched roots | see record | SRC-1, `packages/mdcp-core/src/validate/path-probe.ts` | Author exemptions, syntax and selected files bound domain |

Compiled Markdown, registry and site derivatives are outputs of [RT-RTE-compile-check](runtime.md#rt-rte-compile-check), not independent corroborating sources. Evaluation labels, candidate descriptions and score history remain distinct from production documentation assertions; see [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation). Distributed-parametric host and evaluator dependencies retain their independent fixity/opacity limits in [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-CMP-claude](runtime.md#rt-cmp-claude); no weight learning is inferred.

## Authority-route ledger

Each row splits a consequential function. “See” delegates fields owned by the declaring record rather than re-declaring them. Architectural status is local to this overlay. No row establishes observed operation.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) | content transformation | doctrine only | [MEM-OBJ-shards](memory.md#mem-obj-shards) | truth-apt transformation: indeterminate | Task intent → proposed/as-built shards | Host interpretation; source/task dependent | see [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) | Requested edits | Interpreted protocol | No recorded evidence-consuming acceptance | Edit docs before implementation | Host; skill/shard reads; advisory; work item and later reload | SRC-1, `skills/mdcp/references/workflows/feature-level.md` | [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline) | none | Actual claims needed to distinguish reshaping, derivation and conjecture; no observed adherence |
| [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) | retention | doctrine only | [MEM-OBJ-shards](memory.md#mem-obj-shards) | no content change | Edited shards → future task | Repository writes through host | see [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) | Durable Markdown requested | Protocol | Retention is not acceptance | Future discovery/read | Host; search/index → shard; advisory; future sessions | SRC-1, `skills/mdcp/SKILL.md` | none | none | No observed run |
| [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | content transformation | implemented | [EPI-OBJ-document-body](#epi-obj-document-body) | truth-apt transformation: non-ampliative reshaping | Selected shards → guides/registry | Deterministic assembly, subject to separately assessed hooks | see [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | Compiled derivatives | Writes | No new warrant for source propositions | Publish/inspect derived text | CLI/site; files; permissive; later invocations | SRC-1, `packages/mdcp-cli/src/cli.ts` | none | none | Classifies assembly, not arbitrary callback semantics |
| [EPI-RTE-code-evidence](#epi-rte-code-evidence) | content transformation | implemented | [EPI-OBJ-evidence-links](#epi-obj-evidence-links) | truth-apt transformation: entailed derivation | Recognized link/symbol → file/line association | First lexical occurrence in resolved file | see [EPI-RTE-code-evidence](#epi-rte-code-evidence) | Line fragment or unchanged link | Rewrites | Occurrence only, conditional on resolution; not semantic support | Output carries a citable location | Assembly → output reader; link; advisory; compiled artifact | SRC-1, `packages/mdcp-core/src/compile/hooks/code-evidence.ts` | [EPI-CLM-structure-truth](#epi-clm-structure-truth) | none | Checked concrete deduction in record; pre-existing line fragments are not validated here |
| [EPI-RTE-inline-inserts](#epi-rte-inline-inserts) | content transformation | implemented | [EPI-OBJ-insert-body](#epi-obj-insert-body) | truth-apt transformation: acquisition/import | Referenced insert body → compiled body | Resolvable nonempty insert; per-guide state | see [EPI-RTE-inline-inserts](#epi-rte-inline-inserts) | First inline and subsequent backlink | Writes | Source warrant unknown; text import supplies no acceptance | Reader sees body or backlink | Assembly → output readers; Markdown; permissive; artifact | SRC-1, `packages/mdcp-core/src/compile/hooks/inline-inserts.ts` | none | none | No observed run |
| [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension) | content transformation | implemented | [EPI-OBJ-document-body](#epi-obj-document-body) | truth-apt transformation: indeterminate | Registered callback body → replacement | Caller-supplied executable function | see [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension) | Arbitrary returned string | Executable callback | No general semantic-preservation license | Can replace text without semantic gate | Core caller → assembly; callback; enforcing locally; process/output | SRC-1, `packages/mdcp-core/src/compile/hooks.ts` | none | none | Inspect particular installed callback to classify its content relation |
| [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | check/evidence production | implemented | [MEM-OBJ-shards](memory.md#mem-obj-shards); [EPI-OBJ-document-body](#epi-obj-document-body) | no content change | Selected structural/link/style/coverage criteria | Built-ins and configured peers, not universal prose oracle | see [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | Issues/status | Diagnostic | Only enabled domain; no source-truth endorsement | Produces gate inputs | CLI/CI; issues/exit codes; advisory then gate; invocation | SRC-1, `packages/mdcp-cli/src/cli.ts` | [EPI-CLM-structure-truth](#epi-clm-structure-truth) | none | No observed run |
| [EPI-RTE-path-probe](#epi-rte-path-probe) | check/evidence production | implemented | [EPI-OBJ-path-claims](#epi-obj-path-claims) | no content change | Recognized path claims → unresolved issues | Filesystem existsSync over roots; exemptions apply | see [EPI-RTE-path-probe](#epi-rte-path-probe) | Unresolved path list | Diagnostic | Existence under syntactic interpretation, not behavior or contents | Supplies failures only when enabled | Probe → CLI; issue array; advisory; invocation | SRC-1, `packages/mdcp-core/src/validate/path-probe.ts` | [EPI-CLM-structure-truth](#epi-clm-structure-truth) | none | No observed run |
| [EPI-RTE-path-probe](#epi-rte-path-probe) | disposition/acceptance | implemented | [EPI-OBJ-path-claims](#epi-obj-path-claims) | no content change | Path issues → check failure | CLI error severity and nonempty issues | see [EPI-RTE-path-probe](#epi-rte-path-probe) | Failure entry then exit 1 | Conditional gate | Mechanical rejection only; no general claim acceptance | Blocks successful check, not earlier writes | CLI → CI/caller; exit; enforcing for selected gate; invocation | SRC-1, `packages/mdcp-cli/src/cli.ts` | none | none | No observed run |
| [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | disposition/acceptance | implemented | [MEM-OBJ-shards](memory.md#mem-obj-shards); [EPI-OBJ-document-body](#epi-obj-document-body) | no content change | Diagnostics → check success/failure | Configured severity, strictness, peer availability | see [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) | Pass or process failure | Conditional gate | Pass licenses selected mechanical criteria only | CI can fail; outputs may already be written | CLI → caller/CI; exit; enforcing job status; invocation | SRC-1, `packages/mdcp-cli/src/cli.ts` | [EPI-CLM-structure-truth](#epi-clm-structure-truth) | none | No observed run |
| [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | check/evidence production | implemented | [MEM-OBJ-shards](memory.md#mem-obj-shards) | no content change | Shard-set size/duplication/title proxies | Configured symbolic thresholds and normalization | see [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | Warning findings | Advisory; strict exit optional | Evidence for measured proxy, not necessity of semantic edit | Signals review attention | CLI → host; findings; advisory; next review pass | SRC-1, `packages/mdcp-core/src/validate/review.ts` | none | none | No observed run |
| [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | disposition/acceptance | doctrine only | [MEM-OBJ-shards](memory.md#mem-obj-shards) | no content change | Findings/shard truth → action or leave | Host semantic lenses, spot-check code, audience/job criteria | see [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | One-line rationale and revisions requested | Interpreted protocol | Requested evidence-sensitive review; no recorded claim-level acceptance | Delete superseded text, reword, leave, regroup | Host → repository; edits/review; advisory protocol; later tasks | SRC-1, `skills/mdcp/references/workflows/doc-review.md` | none | none | No actual review decision, tested proposition or accepted novel claim supplied |
| [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | behavior/policy adaptation | doctrine only | [RT-OBJ-config](runtime.md#rt-obj-config) | non-truth-apt policy/content update: thresholds, glossary or Vale guidance | Recurring findings → revised guidance | Agent judgment under review workflow | see [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) | Tuned rule requested | Interpreted protocol | Not a measured capacity improvement | Changes later review/lint behavior if installed | Host → config/rule consumers; files; permissive; later runs | SRC-1, `skills/mdcp/references/workflows/doc-review.md` | none | none | No observed run |
| [EPI-RTE-peer-fix](#epi-rte-peer-fix) | content transformation | implemented | [MEM-OBJ-shards](memory.md#mem-obj-shards) | truth-apt transformation: indeterminate | Docs-root files → peer auto-fixes | External Prettier and markdownlint | see [EPI-RTE-peer-fix](#epi-rte-peer-fix) | Requested in-place changes | Delegated write authority | Semantic preservation not established by wrapper | Bypasses doc-review action selection | CLI → peers → files; argv; permissive; current and later reads | SRC-1, `packages/mdcp-cli/src/cli.ts` | none | none | Peer versions/config and actual edits unavailable |
| [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) | check/evidence production | implemented | [EPI-OBJ-skill-description](#epi-obj-skill-description) | no content change | Trigger expectation vs detected skill invocation | Labeled should_trigger oracle, repeated subprocess calls | see [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) | Train/test passed counts | Diagnostic | Trigger agreement only; not successful task performance | Feeds optimizer ranking | Evaluator → optimizer; score; ranking; iterations | SRC-1, `.agents/skills/skill-creator/scripts/run_loop.py` | none | none | No observed run |
| [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) | operational admission/selection/consumption | implemented | [EPI-OBJ-skill-description](#epi-obj-skill-description) | no content change | Description candidates → next/best description | Train failure stop, test or train selection | see [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) | New current and returned best description | Ranking | Fixture-relative selection; reused holdout not untouched final estimate | Next evaluation uses candidate; production installation separate | Optimizer → next eval/maintainer; text/JSON; ranking; bounded rounds | SRC-1, `.agents/skills/skill-creator/scripts/run_loop.py` | none | none | No observed run |
| [EPI-RTE-context-size](#epi-rte-context-size) | check/evidence production | implemented | [EPI-OBJ-context-size](#epi-obj-context-size) | truth-apt transformation: entailed derivation | Static text size under counting method | String length/tokenizer and ratio arithmetic | Caller after compile | Metrics and optional CSV | Advisory evidence | Corpus-size ratio only, conditional on inputs/counter | Informs conditional benefit wording, no automatic admission | Maintainer/public-copy author; CSV link; advisory; later copy edits | SRC-1, `scripts/bench-context-size.mjs` | [EPI-CLM-context-size](#epi-clm-context-size) | none | Reported data not an observed agent run or causal test |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline) | see record | SRC-1, `skills/mdcp/SKILL.md`, doctrine/design | see record | [RT-BAP-skill-host](runtime.md#rt-bap-skill-host); not a physical cap | None registered | Reported dogfood static size comparison; no behavioral or causal benefit comparison; see [EPI-CLM-context-size](#epi-clm-context-size) | Narrow shard consumption requested | Host can read broader files |
| [EPI-CLM-structure-truth](#epi-clm-structure-truth) | see record | SRC-1, `skills/mdcp-arch-research/SKILL.md`, doctrine/design | see record | [RT-RTE-compile-check](runtime.md#rt-rte-compile-check), [EPI-RTE-path-probe](#epi-rte-path-probe), [EPI-RTE-code-evidence](#epi-rte-code-evidence) | None registered | Path existence is a limited truth-apt check, not blanket truth validation | Stated limitation fits gate; do not interpret it as zero checkable propositions | Peers and host semantic review differ from structural gate |
| [EPI-CLM-research-warrant](#epi-clm-research-warrant) | see record | SRC-1, `skills/mdcp-arch-research/SKILL.md`, doctrine/design | see record | No inspected automatic evidence-to-spec acceptance evaluator; host-mediated [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) are adjacent routes | None registered | Links and method disclosure enable inspection, not validation or causal attribution | A declared evidence/position/clause lineage and supersession policy | No criterion proving that any particular normative clause follows from its evidence |
| [EPI-CLM-context-size](#epi-clm-context-size) | see record | SRC-1, `docs/features/protocol/benefit-claims-and-evidence.md`, doctrine/design; linked CSV reported static measurement | see record | [EPI-RTE-context-size](#epi-rte-context-size) | No observed agent run; reported static CSV available | Corpus-specific sizes, approximate tokenizer, no causal task comparison | One feature shard is reported much smaller than whole dogfood monolith; conditional context reduction is supported as a size comparison | Actual selection, total context, recall, task quality and exercised savings unestablished |

## Bounded conclusion

Vendor policy [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp) governs work; mutable project shards [MEM-OBJ-shards](memory.md#mem-obj-shards) are its edited/retained content, not that vendor policy. Configuration selects compilation/check policy; [EPI-OBJ-document-body](#epi-obj-document-body) is the transformed body. Peer-fix targets docs-root files; its identity overlaps [MEM-RTE-peer-fix](memory.md#mem-rte-peer-fix), not the skill-policy object.

The reported dogfood CSV supplies a static size comparison: median feature shard 864 estimated tokens versus monolith 61941, about 1.4%; character ratio about 1.5%. The conditional benefit claim is therefore not evidence-free. The benchmark and interpretation support a scoped size comparison, not actual one-shard adherence, complete prompt savings, recall or causal benefit; see [EPI-CLM-context-size](#epi-clm-context-size) and [EPI-RTE-context-size](#epi-rte-context-size).

MDCP's source shards acquire operational reliance through agent instructions and later search/read, while compiled guides, registries and site pages are derivatives, not fresh corroboration. Retention/use and selected mechanical admission are not recorded semantic acceptance; see [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host) and [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

The deterministic code-evidence route derives occurrence locations within a narrow lexical domain, not explanations or proof of prose. Insert expansion imports retained bodies with source warrant unknown; arbitrary hooks and peer fixes prevent an unqualified semantic-preservation claim. The relevant limits and concrete source deduction are in [EPI-RTE-code-evidence](#epi-rte-code-evidence), [EPI-RTE-inline-inserts](#epi-rte-inline-inserts), [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension) and [EPI-RTE-peer-fix](#epi-rte-peer-fix).

The structural gate can reject selected link/path/style/coverage failures, but may write derivatives before rejection and offers no general semantic rollback. The path probe genuinely evaluates a narrow truth-apt assertion—existence relative to roots—while author exemptions and default-off policy constrain coverage. It does not check what a file does. A pass does not establish source truth, endorsement or acceptance of a novel ampliative claim; [EPI-RTE-path-probe](#epi-rte-path-probe) and [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

Semantic review is not absent: the shipped workflow requests code spot-checking, per-finding rationales, a leave option and deletion of superseded text. Research doctrine requests reproducible methods, scoped confidence and evidence-to-position-to-clause links, preserving superseded observations separately. These are explicit evidence-sensitive prescriptions, not an observed evidence-consuming acceptance decision or lifecycle integration after such acceptance; [RT-RTE-doc-review](runtime.md#rt-rte-doc-review), [EPI-CLM-research-warrant](#epi-clm-research-warrant). Particular research outcomes remain unassessed. No entailed or non-entailed classification of an unseen authored proposition is justified.

Maintainer trigger optimization has a real expected-label oracle and ranking consumer, independent of prose truth. It supports bounded candidate selection, not successful tasks, general learning or production self-improvement. Recurring-findings guidance can request changes to future checks, but improved capacity, completed content-directed criticism, criticism-led iteration and exercised production self-improvement remain independently unestablished; see [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review). Opaque model processing is not evidence for or against hidden theories. No single epistemic score or system-wide negative follows.

## Shared records

### Operative objects

#### EPI-OBJ-document-body
Label: Compile document body

Part of: [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

Source-native body strings: selected Markdown input, intermediate callback body, and compiled output. Natural-language assertions plus symbolic Markdown links; substrate is process strings and output files. SRC-1, `packages/mdcp-core/src/compile/hooks.ts`; callback replacement passage in [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension). This is the transformed material within the route (a route parent), not [RT-OBJ-config](runtime.md#rt-obj-config), which selects policy. [MEM-OBJ-shards](memory.md#mem-obj-shards) is the source file object; this record distinguishes its compile-body consumption/derivation path and transient replacement state. It does not enlarge [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp).

#### EPI-OBJ-skill-description
Label: Candidate skill description

Part of: [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation)

Source-native current_description and best_description candidates: natural-language trigger-scope policy in process strings, temporary skill files and optional JSON/log outputs. SRC-1, `.agents/skills/skill-creator/scripts/run_loop.py`; evidence and selection passages are supplied by the parent route. Distinct from [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp), the installed vendor skill/workflow policy: a candidate can eventually replace its description, but that does not make it the installed policy or a part of that policy object. It is a material candidate within the evaluation route (a route parent). No project-shard assertion is judged by the trigger oracle.

#### EPI-OBJ-context-size
Label: Context size measurements

Source-native CSV metrics in filesystem text: symbolic metric/value/unit/date fields read as measurements, with prose interpretation in the benefit-claims shard. SRC-1, `docs/features/protocol/context-size-dogfood.csv`. Distinct from [MEM-OBJ-shards](memory.md#mem-obj-shards): a measurement dataset rather than authored project contracts; related public-copy interpretation is [EPI-CLM-context-size](#epi-clm-context-size). The CSV reports o200k_base, 2026-10-05, 53 feature shards, median 4319 characters/864 estimated tokens versus monolith 282975 characters/61941 estimated tokens, ratios 1.5%/1.4%. No inference about which files an actual agent read follows.

> median_shard_token_pct_of_monolith,1.4,percent,median feature shard / monolith token ratio,2026-10-05
> --- `docs/features/protocol/context-size-dogfood.csv`


#### EPI-OBJ-evidence-links
Label: Code evidence links

Markdown link labels/targets and line fragments in source/compiled files; symbolic link syntax consumed by fixed hook rules, with natural-language labels read by humans/agents. Storage is Markdown strings/files. SRC-1, `packages/mdcp-core/src/compile/hooks/code-evidence.ts`.
Part of: [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

This object is material transformed state inside the runtime's compile route (a route parent, not an object container). It is not [RT-OBJ-config](runtime.md#rt-obj-config): its contents are document links rather than gate configuration. Its processing is the narrower [EPI-RTE-code-evidence](#epi-rte-code-evidence).

#### EPI-OBJ-insert-body
Label: Inline insert body

Source-native insert Markdown is natural-language or mixed table/diagram content in files, copied into compiled Markdown strings/files; symbolic path and per-guide counters select placement. SRC-1, `packages/mdcp-core/src/compile/hooks/inline-inserts.ts`.
Part of: [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

A material input/output part of that route, not a duplicate of the configuration or skill policy object. A concrete insert's truth-apt propositions require reading that selected file; the hook alone establishes import.

#### EPI-OBJ-path-claims
Label: Repository path claims

Backtick spans in shard prose interpreted by a symbolic recognizer as existence claims. Storage: Markdown source files; resulting issues are process-local structured objects. SRC-1, `packages/mdcp-core/src/validate/path-probe.ts`.
Part of: [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)


This is the path-check target within the route, not [RT-OBJ-config](runtime.md#rt-obj-config) (which controls whether it runs). The representational boundary matters: prose around the recognized span is not evaluated.

### Routes

#### EPI-RTE-context-size
Label: Static context size measurement

Endpoints: compiled guides/source Markdown → string/token counts and summaries → console/optional CSV → public benefit-copy interpretation. Script owns measurement; maintainers own claim wording. SRC-1, `scripts/bench-context-size.mjs`, implementation; [EPI-CLM-context-size](#epi-clm-context-size) is the doctrine consumer. No supplied individual measurement route counterpart; [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) instead measures trigger/task behavior.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Console metric table and optional CSV write.
- Later read-back: Persisted CSV is linked by benefit-claims policy for interpreting public wording; no observed reader activation.
- Delegated visibility: inapplicable — local deterministic script with tokenizer import, not an agent frame.
- Selection predicate: Fixed guide list and six shard directories; recursive Markdown excluding index.md; feature-only ratios against monolith.
- Invalidation or expiry: Regenerate after compile by instruction; optional overwrite, --no-write suppresses it; no automatic freshness gate.
- Activation or effect: Counts and ratios can inform conditional public copy; no measured agent context or causal benefit.
- Evidence limits: Reported CSV is available, but execution provenance and dependency behavior are not independently verified; no tokenizer or benchmark executed.

Check target/domain: static text sizes under chosen counting method, not correctness of documentation or agent performance. No expected-answer oracle for recall. This does not admit project assertions or automatically revise skill policy.

> const pct = (part, whole) => (whole > 0 ? Math.round((part / whole) * 1000) / 10 : 0);
> --- `scripts/bench-context-size.mjs`

> const measure = (path) => {
>     const text = readFileSync(path, 'utf-8');
>     return { chars: text.length, tokens: tokenizer.count(text) };
>   };
> --- `scripts/bench-context-size.mjs`


#### EPI-RTE-code-evidence
Label: Code evidence location derivation

Part of: [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension)

Endpoints: recognized Markdown link → resolved repository file and label/symbol lookup → rewritten output link. Fixed hook code owns progression and body changes; caller/compile hook selection controls activation. SRC-1, `packages/mdcp-core/src/compile/hooks/code-evidence.ts`. Distinct narrower hook implementation, not a second declaration of the runtime's general callback route.

Concrete deduction from inspected code, not execution: let a resolvable citable file `src/a.ts` contain exactly `// foo\nfunction foo() {}\n`. For a prose link `[foo](src/a.ts)`, with no outputFile and no explicit fragment, symbolFromLabel returns foo; lineForSymbol scans from index zero and the first word-boundary pattern matches the comment. It returns L1; evidenceLink produces `[foo](src/a.ts#L1)`. Thus the derived proposition is “foo occurs on line 1,” conditional on those input premises. It is not “the declaration is on line 1” or “the surrounding claim is supported.” This countercase defeats treating the hook as a semantic evidence checker. Explicit pre-existing L fragments take a separate preserving branch; their correctness is not checked by this hook.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Replacement Markdown string or unchanged link; first lexical occurrence can supply a line fragment.
- Later read-back: Compiled links can persist in output and reach later readers; see runtime compile route for persistence.
- Delegated visibility: inapplicable — no worker/model call; local file reads only.
- Selection predicate: Recognized repository file extensions, non-code-span prose links, resolvable paths; citable code extensions for symbol lookup.
- Invalidation or expiry: Recompilation may recompute symbol locations; explicit line fragments remain authored values.
- Activation or effect: When selected, hook changes location syntax before output; observed reader activation unavailable.
- Evidence limits: Lexical occurrence not declaration identity, premise truth, semantic entailment of prose, or observed execution.

> for (let i = 0; i < lines.length; i++) {
>     if (patterns.some((re) => re.test(lines[i]))) {
>       return formatLineFragment(String(i + 1));
>     }
>   }
> --- `packages/mdcp-core/src/compile/hooks/code-evidence.ts`

#### EPI-RTE-inline-inserts
Label: Insert body expansion

Part of: [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension)

Endpoints: source-shard insert link → resolve/read file → body insertion or backlink. Hook owns deterministic text updates and per-guide first-anchor/counter state. SRC-1, `packages/mdcp-core/src/compile/hooks/inline-inserts.ts`. Distinct concrete hook part of the runtime callback route. First resolution reads trimmed UTF-8; nonempty body is inserted under a numbered heading; later same-path occurrences use the first anchor. This is acquisition/import from the insert file into the compiled document, with source warrant unknown, plus presentation reshaping. There is no evidence-consuming truth decision in this branch.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Replacement Markdown body with content on first occurrence, backlink on repeated resolved path; unchanged original when unresolved/empty.
- Later read-back: Compiled body can reach later readers/site consumers through runtime compile route.
- Delegated visibility: inapplicable — local hook, no isolated context.
- Selection predicate: Links into recognized insert-library directories ending in Markdown; successful resolution and nonempty read.
- Invalidation or expiry: Per-guide state lifetime; rebuilding reads source again, not semantic withdrawal.
- Activation or effect: Copy and backlink placement are implemented; actual reader behavior unobserved.
- Evidence limits: Text copying does not establish source warrant or correctness; particular insert payloads unassessed.

> const existing = state.firstAnchorByPath.get(insert.resolvedPath);
>   if (existing) {
>     return formatBackLink(ref.label, existing, locale);
>   }
> 
>   return formatFirstInline(insert.resolvedPath, insert.content, ref.label, state, locale);
> --- `packages/mdcp-core/src/compile/hooks/inline-inserts.ts`

#### EPI-RTE-path-probe
Label: Path existence checking

Part of: [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

Endpoints: selected source files → recognized backtick paths → filesystem existence tests → issue list → CLI failure accumulation when severity is error. Probe owns evidence production; CLI owns disposition, separated in the ledger. SRC-1, `packages/mdcp-core/src/validate/path-probe.ts`, `packages/mdcp-cli/src/cli.ts`. This part elaborates the runtime's already mentioned path checks; no counterpart individual route was declared.

Target/domain: syntactically eligible repository-relative path existence in selected files under searched roots. Direct source deduction: a prose span `src/a.ts` outside fences/opt-outs with a recognized extension, no generated/vocabulary exemption, and no existing matching path in any root yields an issue; a match in any root suppresses it. This supports that narrow filesystem proposition, not repository behavior or the intended reference. Whole-file or line illustrative markers bypass claims. Default CLI severity off prevents evaluation. Error issues feed failures and the final exit; warn issues print without that failure.

Caller/config author controls activation/exemptions; software proposes issues and CLI decides mechanical failure. No per-claim human approval or universal answer oracle. Mode: deterministic caller-invoked check. Recovery is edit/delete/exempt and rerun; earlier writes are not rolled back. This is not admission of a new knowledge claim.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Array of unresolved path issues; CLI prints them and may fail.
- Later read-back: inapplicable — issue array is current-run state, no probe history write inspected.
- Delegated visibility: inapplicable — filesystem predicate, no model delegation.
- Selection predicate: Recognized relative spans, extensions, selected docs; excludes fenced examples, illustrative markers and declared generated/vocabulary paths.
- Invalidation or expiry: Recomputed on invocation; no cached semantic endorsement.
- Activation or effect: CLI severity other than off runs probe; error plus issues accumulates failure; final failure exits 1.
- Evidence limits: Existence is neither intended-root identity nor behavior correctness; selected grammar/exemptions bound coverage.

> if (isDeclared(claim, options)) continue;
>       if (roots.some((root) => existsSync(resolve(root, claim)))) continue;
>       issues.push({ file, line: i + 1, path: match[1].trim() });
> --- `packages/mdcp-core/src/validate/path-probe.ts`

#### EPI-RTE-peer-fix
Label: Peer automatic fixes

Endpoints: explicit fix command → external Prettier/markdownlint → caller documentation-root files. Possible duplicate: [MEM-RTE-peer-fix](memory.md#mem-rte-peer-fix) identifies the same CLI mutator, with matching docs-root cwd and peer arguments; both IDs remain declared. This is a related alternate path, not a contained part of the runtime compile/check route. It shares peer resolution infrastructure with [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) but invokes mutators directly. SRC-1, `packages/mdcp-cli/src/cli.ts`. CLI selects tools/arguments; peer implementations/configuration own actual content changes. Proposer/decider: caller invokes, software applies fixes; no per-content MDCP human veto. Mode: automatic repair, no expected semantic answer oracle. Trigger and proposed change: explicit fix request and formatting/lint edits. Recovery requires caller Git/backups; wrapper does not perform semantic rejection or rollback. Guidance is external peer configuration. This source trace adds the omitted standalone operation without superseding the runtime's valid broader container.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Peer subprocess effects; wrapper does not inspect returned exitCode to veto subsequent peer call.
- Later read-back: Mutated files are eligible for later reads/compilation; actual changes unobserved.
- Delegated visibility: Peer argv and documentation-root cwd, process permissions; no separate agent.
- Selection predicate: Explicit CLI fix command; peer config determines file/rule scope.
- Invalidation or expiry: inapplicable — no result cache; changed files persist until another edit/recovery.
- Activation or effect: Passes --write . and --fix; no semantic acceptance consumer in wrapper.
- Evidence limits: External tool semantics/configuration not frozen; content relation indeterminate.

> const prettier = findPeerBinary('prettier', getDocsRoot(opts));
>   runPeer(prettier, { cwd: getDocsRoot(opts), args: ['--write', '.'] });
>   const mdlint = findPeerBinary('markdownlint-cli2', getDocsRoot(opts));
>   runPeer(mdlint, { cwd: getDocsRoot(opts), args: ['--fix'] });
> --- `packages/mdcp-cli/src/cli.ts`

### Claims

#### EPI-CLM-context-size
Label: Conditional shard context size

Claim: following one-shard rather than whole-monolith reading can reduce per-turn context. SRC-1, `docs/features/protocol/benefit-claims-and-evidence.md`, doctrine/design with attributed static measurement; the linked CSV is reported static size evidence, not an independently authenticated execution trace. Distinct from [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline), the normative reading policy: this is its conditional quantitative benefit claim. Measurement implementation is [EPI-RTE-context-size](#epi-rte-context-size). No new source or observed-run layer is asserted.

> On this repository, the median `docs/features/` shard is about **1.5%** of the monolith `docs/_build/guides.md`, by characters and by estimated tokens (about 850 tokens against about 60,000). Here the monolith contains the features guide and the glossary terms it links. When agents follow the [usage model](./usage-model.md) and read one shard instead of the whole monolith, per-turn context can be smaller. MDCP does not enforce that discipline. The Agent Skill and your workflow do.
> --- `docs/features/protocol/benefit-claims-and-evidence.md`

The script counts UTF-8-decoded JavaScript string length and selected tokenizer estimates, recursively selects Markdown except index.md, summarizes distributions and computes rounded ratios. This measures corpus sizes, not total prompt overhead, search cost, task-relevant shard counts, recall or exercised savings. Tokenizer/dependency implementation is external; counts are explicitly approximate and model-dependent. The reported CSV date need not identify a run on the frozen commit. Source reading here did not regenerate it.


#### EPI-CLM-structure-truth
Label: Structure versus truth

Claimed operation: the structural gate is not the truth evaluator for research. SRC-1, `skills/mdcp-arch-research/SKILL.md`, doctrine/design. Distinct from [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline), which concerns context discipline. It constrains warranted interpretation of [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

> `mdcp check` validates structure, not truth. Two rules keep records honest where the gate cannot reach:
> --- `skills/mdcp-arch-research/SKILL.md`

#### EPI-CLM-research-warrant
Label: Evidence to specification lineage

Claimed operation: record observed evidence/limits, link durable positions to it and normative clauses to positions; unsupported clauses must be disclosed as guesses. Research observations are preserved and superseded rather than edited as current product truth. SRC-1, `skills/mdcp-arch-research/SKILL.md`, doctrine/design. No supplied runtime claim counterpart; adjacent [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review) describe general production/maintenance rather than this evidence lineage.

> 1. The record states what was observed and what it cannot support.
> 2. The durable position cites the record by link.
> 3. The normative clause cites the position.
> --- `skills/mdcp-arch-research/SKILL.md`

> A clause with no record behind it is a guess presented as a standard. Say so in the specification rather than quietly picking a number: a threshold derived from one small corpus is the failure this separation exists to make visible.
> --- `skills/mdcp-arch-research/SKILL.md`

The operative semantic-review countercase also has direct doctrine support. It prevents interpreting the mechanical gate's limits as absence of all prescribed truth checking (SRC-1, `skills/mdcp/references/review/lenses.md`):

> - Is each claim true of the default branch today? Spot-check commands, file
>   paths, flag names, and config keys against the repository.
> --- `skills/mdcp/references/review/lenses.md`

No actual record-to-clause acceptance instance was inspected. The doctrine does not itself individuate an accepted produced claim, demonstrate that evidence entails a specification, or establish lifecycle integration after acceptance.
