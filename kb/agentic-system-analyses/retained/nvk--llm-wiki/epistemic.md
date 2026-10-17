---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llm-wiki truth-apt routes: source selection, synthesis, trust review, feedback promotion and bounded executable checks."
run-id: AAS-2026-10-17-llm-wiki-a93f86f698d7-01
reviewed-boundary: "95a042c68998559305bc69ac8c482c4e1a415ad3"
---

# llm-wiki epistemic report

## Source-and-claim boundary

Question: what licenses reliance on the content that llm-wiki acquires, synthesizes, retains and later uses? The functional boundary and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). All source anchors below use SRC-1 at the frozen revision. There is no observed-run or causal-experiment evidence. Model instructions establish doctrine, not reliable model execution. The external host's model is see [RT-CMP-host-model](runtime.md#rt-cmp-host-model): parameter updates, deployment identity and inference internals remain uninspected.

The analysis distinguishes source credibility assessment from factual confirmation; article persistence from acceptance; and reported trust verdicts from a universal interposition on use. The consequential knowledge claims are see [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge), [EPI-CLM-audit-trust](#epi-clm-audit-trust) and [EPI-CLM-feedback-noise](#epi-clm-feedback-noise). Concurrency is see [RT-CLM-concurrent-writes](runtime.md#rt-clm-concurrent-writes).

| Entry point or operation | Source path, SRC-1 | Coverage and records | Remaining limit / conclusion prevented |
|---|---|---|---|
| Full skill, compile, ingest, query-lite, portable and runtime-specific entries | `claude-plugin/skills/wiki-manager/SKILL.md`; `claude-plugin/commands/compile.md`; `profiles/query-lite/SKILL.md`; `AGENTS.md`; `plugins/llm-wiki/skills/wiki/SKILL.md`; `plugins/llm-wiki-opencode/skills/wiki-manager/SKILL.md` | Supplied runtime findings: [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki). Direct additional compilation-protocol read. | Not an independent exhaustive comparison of every host prompt; equivalence across hosts is not established. |
| Research, thesis, credibility and repeat rounds | `claude-plugin/commands/research.md`; `claude-plugin/commands/thesis.md` | Direct research sections on round selection, thesis, credibility and Plan Mode handoffs; thesis dispatch searched. [EPI-RTE-source-review](#epi-rte-source-review), [EPI-RTE-source-selection](#epi-rte-source-selection), [EPI-RTE-thesis-verdict](#epi-rte-thesis-verdict). | No real search results, source assessments or accepted thesis instance supplied. |
| Audit and librarian | `claude-plugin/skills/wiki-manager/references/audit.md`; `claude-plugin/skills/wiki-manager/references/librarian.md` | Audit read completely; librarian principles and scoring read directly. [EPI-RTE-trust-review](#epi-rte-trust-review). | Later librarian proposal/application details not independently exhausted; no claim that all repair or guide-revision routes lack acceptance. |
| Refresh and lessons learned | `claude-plugin/commands/refresh.md`; `claude-plugin/commands/ll.md` | Direct refresh comparison/action protocol and lesson extraction/article/rule stages. [EPI-RTE-source-refresh](#epi-rte-source-refresh), [EPI-RTE-lesson-extraction](#epi-rte-lesson-extraction). | No factual equivalence proof or trace that a proposed general rule works. |
| CLI dispatch, structural checking, privacy withdrawal | `scripts/llm-wiki` | Direct dispatch search/main, provenance checker and retract apply/rescan read. [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki), [EPI-RTE-privacy-retract](#epi-rte-privacy-retract). Dispatch includes lint, archive, schema, retract, specialist, adapter, checkpoint. | All schema/archive internals not re-read; no system-complete negative about authority-changing operations. |
| Hooks, feedback capture and promotion | `plugins/llm-wiki/hooks/hooks.json`; `scripts/llm-wiki-session`; `claude-plugin/skills/wiki-manager/references/feedback.md` | Hook/session route supplied by runtime; feedback classifier, lesson formatter and promote read directly. [EPI-RTE-feedback-classification](#epi-rte-feedback-classification), [EPI-RTE-feedback-promotion](#epi-rte-feedback-promotion). | Real prompt context and genuine digests missing; correctness of captured user intent cannot be inferred. |
| Adapter execution, specialist enablement, checkpoint export | `scripts/llm-wiki`; `claude-plugin/skills/wiki-manager/references/adapters.md`; `claude-plugin/skills/wiki-manager/references/specialists.md`; `claude-plugin/skills/wiki-manager/references/checkpoints.md` | Supplied findings: [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute), [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable), [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export). | Private methods/providers absent. Hash/receipt/scanner acceptance cannot establish factual truth or successful method improvement. |
| Pi launchers, DS4 callbacks and registered fixture tool | `scripts/pi-wiki-query`; `scripts/pi-ds4-wiki-query`; `profiles/ds4/pi-query-tools.ts`; `scripts/benchmark-token-efficiency` | Runtime launcher/tool findings; direct fixture-tool and grader read. [RT-RTE-query-evaluation](runtime.md#rt-rte-query-evaluation), [EPI-RTE-fixture-evaluation](#epi-rte-fixture-evaluation). | No model execution, measured savings or causal improvement. Other benchmark modes not exhaustively re-read. |
| Behavioral assertions and fixture artifacts | `tests/promptfooconfig.yaml`; `tests/evals/assertions/check-frontmatter.js`; `tests/evals/assertions/check-index-integrity.js`; `tests/evals/assertions/check-raw-source.js` | Direct initial behavioral config and complete three assertions. [EPI-RTE-fixture-evaluation](#epi-rte-fixture-evaluation). | Synthetic examples are not provenance-linked outcomes of production workflows. No evaluation pass rate. |
| Collection, dataset, collect, inventory, Ideas/portfolio, output and package-generation families | `claude-plugin/skills/wiki-manager/SKILL.md`; `scripts/` | Skill dispatcher searched; runtime/boundary coverage only for these families' details. | Relevant prompt bodies and generation branches remain unassessed here. Prevents a complete enumeration of truth-apt transformations, evaluators or acceptance criteria across the entire product. |

Missing live primary sources prevents judging import warrant; absent article/claim histories prevents semantic-preservation or entailed-derivation findings for actual compilations; absent evidence-consuming decisions prevents identifying an actually accepted ampliative claim. These are conclusion limits, not evidence that the routes never operate. No supplied fact requires supersession. The source-refresh exception below qualifies the runtime's bounded raw-immutability account rather than contradicting its explicit non-universal scope.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | Imported claims, quotations, measurements and source metadata | Source evidence for synthesis | see record | Source truth and completeness unknown; refresh may overwrite raw text. |
| [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | Synthesized factual explanations; thesis core claims and verdicts | Retained knowledge used for answers | see record | No instance with traced synthesis/acceptance supplied; conversation/mixed provenance permitted. |
| [EPI-OBJ-trust-reports](#epi-obj-trust-reports) | Propositions about article support, contradiction, source chains and staleness | Review and maintenance evidence | see record | Scores and timestamps do not license universal truth or replay safety. |
| [EPI-OBJ-feedback-candidates](#epi-obj-feedback-candidates) | Attribution of correction/preference/approval to user; may carry policy rather than factual content | Candidate operational lessons | see record | Regex class and confidence are not calibrated warrant. |
| [RT-OBJ-query-profile](runtime.md#rt-obj-query-profile) | None as a factual store; instructions governing evidence use | Query control | see record | Intended compliance only. |
| [RT-OBJ-adapters-registry](runtime.md#rt-obj-adapters-registry) | None as topic knowledge; symbolic execution policy | Operation registration/admission | see record | Receipt validation delegates remote truth to the adapter. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Not determinable at parameter-content level | External inference | see record | No accessible parameter provenance or training/update evidence. |

## Authority-route ledger

Each row's other fields are owned by its cited record: `see` is deliberate, not a claim that retention or use proves acceptance. Architectural status here describes the particular function, independently of operation status.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) | content transformation | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | truth-apt transformation: indeterminate | raw claims → synthesized article | host model; credibility/corroboration criteria, not entailment proof | compile request; after source survey | candidate article | requested Write/Edit | unknown preservation; not demonstrated acceptance | article production permitted | host → files → later query; model-mediated, cross-session | SRC-1 `claude-plugin/skills/wiki-manager/references/compilation.md` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | verified date is not a checked truth result | see [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) |
| [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) | retention | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | candidate article → retained files | host workflow | after writing | articles/indexes/log retained | requested persistence | no additional warrant | later access permitted | later query/compiler via files; advisory evidence; across sessions | see [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | retention before acceptance | no observed candidate history |
| [EPI-RTE-source-review](#epi-rte-source-review) | check/evidence production | doctrine only | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | no content change | source credibility | see record | before ingestion in single-path or delegated path pipeline | scores/reasons | model assessment requested | source-quality estimate only | feeds separate selection | see record | see record | none | none | no scored source instance |
| [EPI-RTE-source-selection](#epi-rte-source-selection) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | truth-apt transformation: acquisition/import | scored source → raw | see record | after review within each pipeline; plan-path raw writes precede foreground compilation | selected/rejected source | ranking and ingest policy | source warrant unknown | select top N; omit rejected sources | see record | see record | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | credibility is not proposition acceptance | no executed import |
| [EPI-RTE-thesis-verdict](#epi-rte-thesis-verdict) | check/evidence production | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | scoped thesis against for/against evidence | see record | after evidence compilation | supported/partial/insufficient/contradicted/mixed | requested evidence judgment | conditional, scoped model judgment | changes reported reliance and follow-up focus | see record | see record | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | no observed acceptance decision | see record |
| [EPI-RTE-thesis-verdict](#epi-rte-thesis-verdict) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | evidence → verdict/completed status | see record | final round | retained verdict and caveats | requested model disposition | acceptance-like protocol, not evidenced accepted instance | status/reliance direction set | see record | see record | none | no implemented universal admission gate | see record |
| [EPI-RTE-trust-review](#epi-rte-trust-review) | check/evidence production | doctrine only | [EPI-OBJ-trust-reports](#epi-obj-trust-reports) | no content change | current article/output claims, dependencies and freshness | see record | explicit audit/librarian | verdict/report | advisory diagnosis | bounded evidence judgment; clean not universal truth | reports guide user; escalation changes search | see record | see record | [EPI-CLM-audit-trust](#epi-clm-audit-trust) | no forced withdrawal of contradicted articles | no observed review |
| [EPI-RTE-source-refresh](#epi-rte-source-refresh) | check/evidence production | doctrine only | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | no content change | 5–10 stored key facts versus live URL | see record | refresh request | change/impact assessment | advisory comparison | sampled source drift only | presents choices | see record | see record | none | upstream change is not itself truth | see record |
| [EPI-RTE-source-refresh](#epi-rte-source-refresh) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | assessment → user choice | see record | after report | skip/update/flag/retract | user-directed policy | skip purports human confirmation, not measured truth | can reduce confidence or route update/retract | see record | see record | none | verified date updated after all actions | see record |
| [EPI-RTE-source-refresh](#epi-rte-source-refresh) | content transformation | doctrine only | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | truth-apt transformation: acquisition/import | live source → replacement raw | see record | user selects update | overwritten raw and recompiled article | requested overwrite | new source warrant unknown; old lineage may be lost | changes later compiler inputs | see record | see record | none | exception to simple immutable-raw reading | see record |
| [EPI-RTE-feedback-classification](#epi-rte-feedback-classification) | content transformation | implemented | [EPI-OBJ-feedback-candidates](#epi-obj-feedback-candidates) | truth-apt transformation: indeterminate | user text → attributed feedback lesson | see record | capture hook/manual request | candidate or none | deterministic regex/template | text-pattern evidence, not intent verification | candidate availability, no automatic rule installation | see record | see record | [EPI-CLM-feedback-noise](#epi-clm-feedback-noise) | context omitted; false positives possible | see concrete deduction in record |
| [EPI-RTE-feedback-promotion](#epi-rte-feedback-promotion) | retention | implemented | [EPI-OBJ-feedback-candidates](#epi-obj-feedback-candidates) | truth-apt transformation: non-ampliative reshaping | existing candidate → topic raw note | see record | explicit promote call | note/status/index/log | filesystem write | preserves candidate attribution, not its truth | raw note admitted for later compile/rule proposal | see record | see record | [EPI-CLM-feedback-noise](#epi-clm-feedback-noise) | explicit is not content-reviewed acceptance | see record |
| [EPI-RTE-lesson-extraction](#epi-rte-lesson-extraction) | content transformation | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | truth-apt transformation: indeterminate | session events → cause/fix/general rule | see record | /wiki:ll | lesson raw note/article appendix | model interpretation | causal/generalization warrant unestablished | articles may receive rule without per-lesson user gate | see record | see record | none | generalization requested, not proven | see record |
| [EPI-RTE-lesson-extraction](#epi-rte-lesson-extraction) | behavior/policy adaptation | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | non-truth-apt policy/content update: proposed behavior rule | lesson → proposed agent instructions | see record | --rules | proposed rule; approval requested | advisory until user approval | no truth acceptance implied | does not auto-edit AGENTS/CLAUDE | see record | see record | none | no exercised self-improvement trace | see record |
| [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | retained files → answer evidence | see [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) | user query | cited answer or gap | model selection policy | retrieved evidence not endorsed source truth | answer construction permitted | see [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) | see [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) | none | query-lite not full-skill write policy | answer semantics indeterminate |
| [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki) | check/evidence production | implemented | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | schema/provenance/path/freshness | Python fixed rules | explicit lint | issues, counts, exit status | report/threshold; optional fixes separate | structure and reference resolution only | caller can continue depending threshold | see [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki) | SRC-1 `scripts/llm-wiki` | none | sources exempt for conversation/mixed | not factual verification |
| [EPI-RTE-privacy-retract](#epi-rte-privacy-retract) | content transformation | implemented | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | truth-apt transformation: indeterminate | matching bytes/names → marker/deletion | see record | explicit --apply | rewritten files, optional binary deletion | enforcing selected local transformation | privacy withdrawal, not epistemic refutation | removes selected material from later file reads | see record | see record | none | partial claim replacement can break meaning | not global fact retraction |
| [EPI-RTE-privacy-retract](#epi-rte-privacy-retract) | check/evidence production | implemented | [EPI-OBJ-raw-articles](#epi-obj-raw-articles) | no content change | post-apply local pattern residue | see record | after mutation | verification report/incomplete exit | reports failure; no undo | scan-bounded match absence only | signals incomplete cleanup | see record | see record | none | no rollback/global erasure proof | see record |
| [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) | operational admission/selection/consumption | implemented | [EPI-OBJ-feedback-candidates](#epi-obj-feedback-candidates) | no content change | session state → context | see [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) | configured hook events | summary/pointers | advisory context injection | explicitly not canonical topic knowledge | later model may resume/read digest | see [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) | see [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) | none | delivery not activation | no factual validation by hook |
| [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute) | check/evidence production | implemented | [RT-OBJ-adapters-registry](runtime.md#rt-obj-adapters-registry) | no content change | request, manifest, plan, response/receipts | see [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute) | before/after subprocess | valid/error | pre-dispatch rejection; post-effect checking | hash/protocol matching; adapter owns remote attestation | registered operation allowed/blocked | see [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute) | see [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute) | none | receipt not independent remote verification | no remote sandbox or truth oracle |
| [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export) | check/evidence production | implemented | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | fixed bundle hashes/scanner/word floor | see [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export) | seal/verify | pass/overridden/fail | bounded protocol admission | integrity/privacy-pattern coverage only | staging allowed; final copy separately authorized | see [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export) | see [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export) | none | word floor not semantic completeness | no factual acceptance |
| [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable) | operational admission/selection/consumption | implemented | specialist topic allowlist: see [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable) | non-truth-apt policy/content update: topic method allowlist | specialist structural validity → enablement | see [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable) | explicit enable/disable | allowlist update | structural gate | not method quality acceptance | later selected method may shape review, not tools | see [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable) | see [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable) | none | instruction admission is not quality acceptance | see record for actual specialist state |
| [EPI-RTE-fixture-evaluation](#epi-rte-fixture-evaluation) | check/evidence production | implemented | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | synthetic answer/files and tool behavior | see record | benchmark/eval invocation | scores/pass/fail | report to maintainer | case-specific text/structure/tool checks | no automatic production replacement established | see record | see record | none | case oracle not general semantic truth | no results supplied |

No lifecycle-integration row is inferred merely from article linking or feedback promotion: those can organize and retain candidates before any evidenced acceptance. No route is classified as checked entailed derivation. The sampled code transformations establish narrower syntactic deductions, not factual entailment of a generated article.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | see record | see record | Source-based synthesis, confidence rubric and source links | No inspected semantic compiler; structural helper see [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki) | none supplied | No source-to-article checked interpretation or outcome comparison | Design supports model-operated candidate synthesis and retention | Actual source warrant, entailment and accepted ampliative production unknown. |
| [EPI-CLM-audit-trust](#epi-clm-audit-trust) | see record | see record | see [EPI-RTE-trust-review](#epi-rte-trust-review) | No target-owned executable semantic truth adjudicator established by inspected audit protocol | none supplied | No calibrated verdict reliability; source independence not guaranteed | Explicit adversarial, unresolved-capable review doctrine | A report can diagnose trust; no enforcement excludes contradicted content from query. |
| [EPI-CLM-feedback-noise](#epi-clm-feedback-noise) | see record | see record | Candidate layer, explicit promotion and contextual-approval warning | [EPI-RTE-feedback-classification](#epi-rte-feedback-classification), [EPI-RTE-feedback-promotion](#epi-rte-feedback-promotion) | none supplied | Pattern recognition is not intent understanding; no false-positive comparison | Some acknowledgements excluded and candidates separated from topic notes | Noise prevention or future benefit not demonstrated. |
| [RT-CLM-concurrent-writes](runtime.md#rt-clm-concurrent-writes) | see record | see record | see record | see [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) | none supplied | Same-file last-write-wins and conversation/overwritten-raw exceptions limit rebuildability | Bounded coordination policy only | Index repair cannot certify preservation of earlier evidence or edits. |

## Bounded conclusion

llm-wiki's primary truth-apt route is **acquisition plus model synthesis**, with linked raw sources, confidence fields and retained articles. Source warrant remains unknown in this evidence boundary. Compiling can reshape or infer beyond sources, but instructions and missing article histories do not establish which relation holds for any actual output. Conversation-origin articles are explicitly permitted; `sources:` is not a universal raw-provenance invariant. See [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles).

The strongest semantic checking doctrine is **evidence-directed research and trust review**, not lint. Credibility scoring has operative selection criteria: the foreground model in single-path mode, or each delegated path-agent in plan mode, scores source attributes, rejects below zero, conditionally admits low-ranked sources and selects top N for ingestion. In plan mode, each path admits and writes its selected raw sources before returning; the foreground model then compiles across those already-ingested sources. Foreground cross-path compilation is not a pre-ingest source-admission gate. That licenses an intended source-selection use, not truth of every proposition. Thesis mode explicitly scopes a claim, gathers opposing evidence and retains a verdict, caveats and what would change it. This is an acceptance-like evidence-consuming design for the investigated claim; no supplied trace establishes an actually accepted ampliative claim. Audit's corroboration/counter-evidence protocol is a counterexample to saying that the product has no semantic checking route. Its result is advisory reporting, not a hard gate on later queries. See [EPI-RTE-source-review](#epi-rte-source-review), [EPI-RTE-source-selection](#epi-rte-source-selection), [EPI-RTE-thesis-verdict](#epi-rte-thesis-verdict), [EPI-RTE-trust-review](#epi-rte-trust-review).

Refresh grants a distinct **user-choice authority**: sampled live-source comparisons lead to skip/update/flag/retract. Flag lowers confidence; update replaces raw content and recompiles; skip updates `verified` as purported human confirmation. Compilation also sets `verified` to today. Therefore a recent date alone cannot distinguish an evidence-consuming human acceptance from a model-created freshness label. Privacy retraction is a separate implemented withdrawal of selected local content, followed by a pattern rescan; it does not judge whether the removed proposition is false. See [EPI-RTE-source-refresh](#epi-rte-source-refresh), [EPI-RTE-privacy-retract](#epi-rte-privacy-retract).

Feedback/session paths retain **operational candidates**, with a warning against treating digests as canonical knowledge. Automatic candidate formation and explicit promotion are implemented; promotion does not itself verify the attributed user intent or broaden contextual approval into a global fact. Lessons learned separately requests causal/general rules and appends them to articles; agent-instruction edits are proposed for user approval, not automatically made. Later query/model consumption is an advisory behavioral-authority path across sessions, not proof of benefit. See [EPI-RTE-feedback-classification](#epi-rte-feedback-classification), [EPI-RTE-feedback-promotion](#epi-rte-feedback-promotion), [EPI-RTE-lesson-extraction](#epi-rte-lesson-extraction), [RT-BAP-session-context](runtime.md#rt-bap-session-context).

Executable checks grant narrower licenses: provenance resolution and schema hygiene; exact adapter-plan/receipt conformance; checkpoint integrity and scanner-pattern admission; fixture term/length, structure and tool-use checks. Their targets differ and none is a universal factual oracle. A passing result can authorize its bounded operation without licensing topic claims. No supplied result establishes benchmark success, efficiency savings, component effects or automatic deployment of an improved profile. See [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki), [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute), [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export), [EPI-RTE-fixture-evaluation](#epi-rte-fixture-evaluation).

Theory-related findings stay separate. Thesis text offers localized claims and falsification criteria; model-mediated consumption, criticism and next-round reuse are prescribed, but no exercised criticism-to-revision trace is supplied. Persistent specialist methods offer inspectable instruction changes but their quality and operation remain unobserved. Research has a named representation of gaps/progress that is instructed to shape subsequent search; this supports a reflection-oriented protocol, not demonstrated reflection or improved capacity. Learning, autonomous theory building and exercised self-improvement are not established by retention, revised rules or a score. The missing outcome/reuse evidence does not erase the independent source-selection, advisory checking and implemented promotion capabilities. Unassessed collection/output and other prompt bodies prevent a system-complete negative or a single epistemic verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-raw-articles
Label: Raw source files

Source-native identity: `raw/` typed Markdown source files, including promoted notes. Representational form and storage substrate: Natural-language source claims with symbolic frontmatter; filesystem Markdown. Evidence: SRC-1 `claude-plugin/skills/wiki-manager/references/compilation.md` and `claude-plugin/commands/refresh.md`. Distinct from the compile route, which operates on these inputs. No supplied object record is the raw-source store.

#### EPI-OBJ-wiki-articles
Label: Wiki articles and thesis files

Source-native identity: `wiki/` compiled articles and `wiki/theses/<slug>.md`. Representational form and storage substrate: Natural-language claims and explanations plus symbolic provenance/confidence/verdict fields; filesystem Markdown. Evidence: SRC-1 `claude-plugin/skills/wiki-manager/references/compilation.md` and `claude-plugin/commands/research.md`. Distinct from [RT-OBJ-query-profile](runtime.md#rt-obj-query-profile), which is shipped operational guidance, and from [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), which is the producing workflow.

#### EPI-OBJ-trust-reports
Label: Audit and librarian reports

Source-native identity: `.audit/scan-results.json`, `.audit/REPORT.md`, `.librarian/scan-results.json` and report/checkpoint files. Representational form and storage substrate: Natural-language judgments with symbolic score/status fields; JSON and Markdown files. Evidence: SRC-1 `claude-plugin/skills/wiki-manager/references/audit.md` and `claude-plugin/skills/wiki-manager/references/librarian.md`. No counterpart object in supplied runtime. These are diagnostic claims, not topic articles.

#### EPI-OBJ-feedback-candidates
Label: Feedback candidates

Source-native identity: `HUB/.sessions/feedback/candidates.jsonl`, status/index and promoted notes. Representational form and storage substrate: Natural-language preview/lesson plus symbolic type/confidence/scope/hash; JSONL, JSON, Markdown. Evidence: SRC-1 `scripts/llm-wiki-session`. Candidate store is distinct from operational context delivery in [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge); the general route did not establish this classifier or feedback-promotion content path.

Evidence for source-to-article provenance and its confidence/date boundary (SRC-1):

> 2. Write the body — explain using information from source(s). Synthesize, contextualize, explain. Do NOT copy-paste.
> --- `claude-plugin/skills/wiki-manager/references/compilation.md`

> When creating or updating a wiki article, set `volatility` and `verified` in frontmatter. Default `volatility` to `warm`. Set `verified` to today's date. The full rubric — what each tier means, when to use it, how the decay differs — lives in `references/wiki-structure.md` § Volatility Classification. The short version: news/trends sources → `hot`, foundational/historical sources → `cold`, everything else → `warm` (the safe default). The author can override during review.
> --- `claude-plugin/skills/wiki-manager/references/compilation.md`

### Routes

#### EPI-RTE-source-review
Label: Research source credibility review

Part of: [RT-RTE-research-paths](runtime.md#rt-rte-research-paths)

SRC-1 `claude-plugin/commands/research.md`, Phase 2b and Plan Mode. In single-path mode, the foreground host model assesses search-worker-returned source candidates before ingestion. In plan mode, each delegated path-agent owns the full search → credibility → ingest pipeline and assesses its own sub-agents' returned candidates before writing that path's raw sources. Both use peer review, recency, author authority, bias and corroboration scoring. The foreground model's cross-path compilation occurs after path returns, not before their source admission. Target/domain: estimated source credibility for this research request, not proof of each source claim. The score is consumed by the separate selection part below. No expected-answer oracle exists. Open research mode; source counts/depth change the intended work, not a known-correct reference outcome. This is the review part of the supplied research container, not a duplicate end-to-end research route.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Source scores and reasons passed to selection.
- Later read-back: Scores/confidence are requested to persist with research reports/raw/article metadata.
- Delegated visibility: Single-path search-worker findings return to the foreground model; plan-mode sub-agent findings return to their path-agent for credibility review. Each path-agent receives focus/search angles, the standard agent template, full-pipeline instructions and a path identifier; no actual packet supplied.
- Selection predicate: All sources returned by the relevant search agents, before ingestion within the single path or each delegated plan path.
- Invalidation or expiry: New evidence, other source versions or another review can change assessment; no automatic validity horizon.
- Activation or effect: Requested scoring by the foreground model in single-path mode or by each path-agent in plan mode changes that pipeline's ranking inputs; use unobserved.
- Evidence limits: Source reputation and agent corroboration may be correlated and do not independently verify facts.

> After all agents return and before ingestion, run a credibility assessment. This prevents the "fox guarding the henhouse" problem where agents self-rate their own source quality.
> --- `claude-plugin/commands/research.md`

> - **Reject** (<0 points): Obvious spam, predatory journal, fabricated data → skip entirely
> --- `claude-plugin/commands/research.md`

#### EPI-RTE-source-selection
Label: Research source admission

Part of: [RT-RTE-research-paths](runtime.md#rt-rte-research-paths)

SRC-1 `claude-plugin/commands/research.md`, Phase 2b–4 and Plan Mode. In single-path mode, the foreground model proposes and decides deduplication/ranking/ingestion using the review score, agent quality and requested source count. In plan mode, each delegated path-agent makes those decisions within its assigned path and writes selected raw sources before returning. The foreground model then reads all newly ingested sources for one cross-path compilation pass; this is not a separate pre-ingest source approval. Below-zero sources are skipped; low-tier ones require no better angle coverage. These are evidence-consuming source-selection criteria for research ingestion, not recorded acceptance of a novel proposition. User initiates and may reject a plan; this is not per-source approval. Recovery is rerun/revise sources and recompile; no inspected atomic rollback. Guidance and selected raw sources/confidence persist. No answer oracle. This selection part is distinct from its checking part and from the supplied research container.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Chosen sources and skipped-source reasons.
- Later read-back: Raw files/indexes feed compilation and subsequent queries.
- Delegated visibility: Single-path worker returns are selected by the foreground model; plan-mode sub-agent returns are selected by their path-agent. Plan paths persist selected raw files with path-prefixed names and defer index updates; the foreground compiler reads those files after all path agents return. Not all search findings need enter raw files; actual deliveries are unobserved.
- Selection predicate: Credibility tiers, same-URL/content deduplication, credibility × quality ranking and top N in the relevant single-path or delegated path pipeline.
- Invalidation or expiry: New sources or changed review permit reselection; no universal source expiry.
- Activation or effect: Requested ingestion writes selected source content in the foreground single-path pipeline or within each delegated plan path before foreground compilation; imported warrant unknown.
- Evidence limits: No execution or actual assessed source; credibility selection is not proposition-level acceptance.

> 4. Select top N for ingestion (--sources count)
> 5. Report skipped sources with reasons in Phase 5
> --- `claude-plugin/commands/research.md`

Plan-mode ownership and delivery differ from the single-path foreground pipeline (SRC-1):

> - Instructions to run the full search → credibility → ingest pipeline
> --- `claude-plugin/commands/research.md`

> Each path-agent internally launches its own 5/8/10 sub-agents (standard/deep/retardmax) for the search phase, exactly as single-path research does today.
> --- `claude-plugin/commands/research.md`

> After all path agents return, run a single compilation pass that:
>
> 1. Reads ALL newly ingested sources from all paths
> --- `claude-plugin/commands/research.md`

#### EPI-RTE-thesis-verdict
Label: Thesis evidence and verdict

Part of: [RT-RTE-research-paths](runtime.md#rt-rte-research-paths)

SRC-1 `claude-plugin/commands/research.md`, thesis mode. Separate check function: the model weighs scoped supporting/opposing/nuancing findings, credibility and evidence strength. Separate disposition function: it writes completed status and a verdict, confidence, caveats and what would change it. Intended use/scope: the decomposed claim with named variables, prediction and falsification criteria, confirmed by the user before investigation. No expected-answer oracle. Model proposes/decomposes, user can veto scope, then model selects findings and renders verdict. Retention starts while investigating, before final judgment; evidence linking during this period is not post-acceptance integration. Follow-up searches and final verdict are prescribed, not observed. This is a thesis-mode part of the supplied research route.

Theory-builder conditions 1–4: condition 1 afforded by a whole localized core claim and scope; condition 2 claimed by thesis-directed selection; condition 3 claimed by explicit opposing evidence/falsification and changed verdict direction, but actual blame placement on an instantiated claim/test/data is uninspected; condition 4 claimed by weakest-side next-round search and retained round state. Addressability: claim, variables, falsification, evidence and verdict sections individually editable. Persistence: rounds and retained thesis file across sessions. Learning: uninspected improved capacity, no outcome comparison. Reflection: round-gap/progress representation is instructed to change search, not observed causal dependence. Autonomous theory building: uninspected internal execution; user scope confirmation does not itself establish or defeat it. No exercised self-improvement attribution: there is no trace connecting evidence to a live changed method and later dependent operation.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Scoped thesis evidence and verdict; future-change criteria.
- Later read-back: Thesis file and durable events/checkpoint support later inspection; ephemeral thesis-session file deleted on normal completion.
- Delegated visibility: Support/opposition/mechanistic branches return evidence findings; host scheduling external.
- Selection predicate: Claim relevance, evidence strength and direction; next round targets weakest side.
- Invalidation or expiry: Contradictory/new evidence and stated future findings may change verdict; no universal expiry.
- Activation or effect: Advisory retained verdict and next-round selection policy, no hard universal query gate.
- Evidence limits: No investigated thesis instance, accepted ampliative result, actual criticism or subsequent reuse supplied.

> - **Round 2**: Drill into the WEAKEST side. If Round 1 found mostly supporting evidence, Round 2 focuses harder on finding counter-evidence (and vice versa). This prevents confirmation bias — the most important methodological difference from standard research.
> --- `claude-plugin/commands/research.md`

#### EPI-RTE-trust-review
Label: Audit and librarian trust review

SRC-1 `claude-plugin/skills/wiki-manager/references/audit.md` and `claude-plugin/skills/wiki-manager/references/librarian.md`. No counterpart to this semantic diagnostic route in supplied runtime. Host model checks named article/output claims, source dependencies, staleness and source strength; audit can re-fetch primary material and split support/attack searches. Librarian uses specified date-decay/integrity formulas and model-scored depth/coherence/utility; the formulas are doctrine here, not inspected executable semantic checks. Mode: open trust request with local-only quick option; no expected-answer oracle. The model produces verdicts, user can request narrower scope or confirm later repair. Audit reports do not themselves rewrite knowledge. `clean` addresses dependency/drift checks; it is not evidence that every factual proposition was tested. Session-event presence is called replayable by doctrine, but that supplies neither deterministic replay nor completeness verification.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Findings, supported/weakened/contradicted/unresolved truth verdicts; output dependency verdicts and provenance classification.
- Later read-back: Audit/librarian JSON, reports/log/checkpoint; audit can reuse a fresh librarian result.
- Delegated visibility: Optional support/attack/primary-source branches return findings; actual packet content unobserved.
- Selection predicate: Scope options; local weakness, staleness, contradiction, thin important claims or user trust question trigger escalation.
- Invalidation or expiry: Fresh scan on --fresh; new evidence or drift changes review; no inspected semantic freshness proof.
- Activation or effect: Advisory reports to user and later workflows; diagnostic findings can cause research escalation, not forced content exclusion.
- Evidence limits: No observed verdict; support search can still rely on flawed/shared sources. Detailed later repair bodies unassessed.

> 3. **Read-only on knowledge artifacts.** Audit writes reports under `.audit/`
>    and may reuse `.librarian/`, but it does not rewrite wiki or output content
>    during a scan.
> --- `claude-plugin/skills/wiki-manager/references/audit.md`

> 4. Run targeted research with both supportive and adversarial queries:
>    - one query that tries to confirm the current claim
>    - one query that tries to break or disprove it
> --- `claude-plugin/skills/wiki-manager/references/audit.md`

> 1. **Score then act.** The librarian produces scores and reports. It never modifies wiki content during a scan. Write operations (fix, auto-fix) are separate commands requiring explicit confirmation.
> --- `claude-plugin/skills/wiki-manager/references/librarian.md`

#### EPI-RTE-source-refresh
Label: Source refresh and user disposition

SRC-1 `claude-plugin/commands/refresh.md`. No supplied runtime route individuates this semantic change-assessment/user-choice path. Checking targets 5–10 extracted key facts and changed sections at cited live URLs; the host model classifies unchanged/updated/contradicted/unreachable and impact. Disposition is separate: user selects skip/update/flag/retract. Model proposes; user decides and can skip. Scope/intended use: current source/article currency, not universal source truth. No answer oracle. Update re-ingests by overwriting raw content while preserving frontmatter, then recompiles. Flag lowers confidence and inserts a warning; retract routes elsewhere. Recovery is user-directed future refresh/recompile, not an inspected transaction or preserved previous source version. This is a concrete exception to a stronger immutable-source interpretation. `verified` is updated even after flag/retract, so the date cannot uniquely certify endorsement.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Comparison report and per-source user options.
- Later read-back: Changed raw/article/confidence/verified fields and log feed subsequent compilation/query/review.
- Delegated visibility: inapplicable — inspected protocol is foreground fetch/comparison and user choice.
- Selection predicate: Explicit article or user-selected due list; cited source URL, sampled key facts.
- Invalidation or expiry: New upstream changes, missing URLs, future due review; verified date refreshed after actions.
- Activation or effect: Model asks user; selected update/flag/retract requests writes or another workflow.
- Evidence limits: Changed upstream claims may be wrong; sampled unchanged facts cannot establish semantic identity of whole source.

> - **update**: Re-ingest the changed source (overwrite the raw file with new content, preserve frontmatter), then recompile the article following the standard compilation protocol.
> --- `claude-plugin/commands/refresh.md`

> After all actions, update the article's `verified` date to today.
> --- `claude-plugin/commands/refresh.md`

#### EPI-RTE-feedback-classification
Label: Feedback candidate classification

SRC-1 `scripts/llm-wiki-session`, `classify_feedback_text`, `feedback_scope_hint`, `feedback_lesson`; doctrine SRC-1 `claude-plugin/skills/wiki-manager/references/feedback.md`. Distinct from [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge): this is a feedback candidate transformation rather than digest context delivery or digest promotion. Code normalizes whitespace, rejects a fixed set of pure acknowledgements, then tests correction before preference before approval before decision. It assigns confidence/scope and a templated attributed lesson. Domain: text-pattern classification of candidate feedback, not validated user intent or outcome success. Hook/manual caller supplies text; code decides classification; explicit promotion is separate. No factual answer oracle.

Concrete implementation deduction, not execution: input `wrong` normalizes to `wrong`, matches the correction rule, produces type `correction`, confidence `high`, scope `session`, and lesson `User correction/redirection to remember: wrong`. No preceding result, challenged claim, root cause or corrected proposition is needed. Input `thanks` returns none unless forced. These cases establish both actual filtering and its boundary. Candidate attribution may add meaning beyond the text; preservation/entailment depends on omitted context, so the semantic relation is indeterminate rather than proved ampliative. The update can also carry non-truth-apt preferences.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate dictionary or none, with confidence/scope/preview/hash/lesson/recommendation.
- Later read-back: Captured candidates persist in JSONL and derived feedback indexes; may enter promotion and digest workflows.
- Delegated visibility: inapplicable — deterministic local classifier, no model worker in this function.
- Selection predicate: Ordered regex rules over normalized user text; force permits manual fallback.
- Invalidation or expiry: Candidate hash identifies normalized text, not preceding context; no automatic semantic invalidation.
- Activation or effect: Candidate classification is implemented; later behavior depends on separate promotion/consumption.
- Evidence limits: False-positive patterns and omitted context are possible; no calibration or benefit evidence.

>     if feedback_type == "approval":
>         return f"User validated the immediately preceding result or action: {preview}"
> --- `scripts/llm-wiki-session`

>     if not force and re.fullmatch(r"(ok|okay|cool|thanks|thank you|ty|k|👍|👌)[.!]*", lower):
>         return None
> --- `scripts/llm-wiki-session`

>     if feedback_type == "correction":
>         return f"User correction/redirection to remember: {preview}"
> --- `scripts/llm-wiki-session`

#### EPI-RTE-feedback-promotion
Label: Feedback promotion to raw note

SRC-1 `scripts/llm-wiki-session`, `run_feedback_promote`. Distinct from [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) digest-body promotion: input is an identified feedback candidate, output a feedback-type note. CLI caller chooses candidate/topic; code checks existence/topic notes and non-overwrite unless force, then renders lesson, preview, metadata and usage guidance. Explicit invocation supplies operational admission, not authenticated human factual acceptance. No evidence comparison occurs in this function. Intended use is a candidate for future rule/compile work; approval is explicitly local to prior context. Code can reject missing candidate/topic or existing destination; force permits replacement. Status/index/log persist; no generic rollback. Natural-language candidate content is retained with symbolic metadata and explicit guidance, not semantically verified.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Promoted note path.
- Later read-back: Topic raw/notes, promotion status, feedback index and topic log remain for later compile/rule-proposal consumers.
- Delegated visibility: inapplicable — local filesystem operation, no delegated inference.
- Selection predicate: Explicit candidate ID and topic; valid notes directory and overwrite policy.
- Invalidation or expiry: Force can replace an existing note; no semantic expiry or automatic source-context revalidation.
- Activation or effect: Writes candidate into topic raw notes; no automatic AGENTS/skill installation.
- Evidence limits: No user review trace or criterion consuming corroborating evidence; retention cannot be relabeled lifecycle integration.

>         - Treat approval/decision candidates as validation of the immediate prior context unless corroborated by session digests.
>         - Do not infer broader factual claims from this feedback alone.
> --- `scripts/llm-wiki-session`

#### EPI-RTE-lesson-extraction
Label: Session lessons and rule proposals

SRC-1 `claude-plugin/commands/ll.md`. No supplied route covers this cause/fix/general-rule extraction path; it overlaps the session bridge only in possible session input. Host model selects error→fix patterns, user corrections, discoveries/configuration/gotchas and writes context/symptom/root cause/fix/rule. Model decides lesson text and article appends; user can preview via dry-run and individually approve instruction proposals under --rules. Open session-review mode; no known-correct causal oracle. Raw notes and appends persist. Rule suggestions name exact target/text but prohibit automatic agent-instruction editing. Recovery is subsequent edit/recompile; no atomic rollback shown.

A request to generalize from one episode does not establish non-entailment for an unspecified claim or warrant for its cause. Theory-builder conditions 1–4: 1 afforded by localized Rule/context fields; 2 claimed by future article/agent consumption; 3 claimed for error/assumption/root-cause criticism but actual blame/evidence uninspected; 4 uninspected beyond proposed reuse, with no actual revised rule next-round trace. Addressability: individual lesson fields and proposed instruction text. Persistence: raw note/article across sessions, proposed instructions only if approved. Learning: improved future capacity uninspected. Reflection: own-session representations and possible future rules are a design path, not observed two-way dependence. Autonomous theory building and exercised self-improvement independently unestablished; evidence-to-update and later causally dependent operation are not supplied.

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Lesson note/article additions and optional exact instruction proposals.
- Later read-back: Raw lesson notes, article appends and indexes/log remain; approved rule installation is not observed.
- Delegated visibility: inapplicable — selected protocol uses foreground conversation scan.
- Selection predicate: Error/fix and correction signals; related article keyword search; user topic selection.
- Invalidation or expiry: Future contradiction can motivate edits; no automatic validity/rollback mechanism.
- Activation or effect: Model-requested note writes and article appends; rule changes advisory pending user approval.
- Evidence limits: General rules/causal explanations are candidates without traced comparisons; high confidence in a template proves no warranted outcome.

> Do NOT auto-edit CLAUDE.md/AGENTS.md. Present the proposals and let the user approve each one.
> --- `claude-plugin/commands/ll.md`

#### EPI-RTE-privacy-retract
Label: Local privacy withdrawal and verification

SRC-1 `scripts/llm-wiki`, `run_retract`, `apply_retract`, `atomic_replace_patterns`. No supplied runtime declaration covers this implementation; it is not the same operation as lint or archived-topic exclusion. User/caller supplies hidden/file value and roots/options; code scans, defaults to report, applies only with --apply, then rescans. Separate functions are mutation versus check: text matches become `[RETRACTED]`, optional binaries are deleted and names changed; matching log entries may instead be removed. Concrete code deduction: selected bytes `alpha secret beta` with pattern `secret` become `alpha [RETRACTED] beta` by `bytes.replace`; no proposition truth test occurs. Check domain is residual local pattern/name matches in selected roots, not semantic paraphrases or remote/history erasure. Caller controls apply/deletion/log options; code decides matches and can report errors. No expected factual answer oracle. Recovery uses atomic replacement per file, not a whole-operation rollback; no backup established by this code. Changed knowledge/lineage is a privacy action, not epistemic rejection of its content.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dry-run or applied report; incomplete status returns exit 2.
- Later read-back: Rewritten/deleted/renamed files and remaining log are consumed by later file-based workflows.
- Delegated visibility: inapplicable — deterministic local mutation/check route.
- Selection predicate: Selected roots, exact/variant patterns, --apply, binary/log options.
- Invalidation or expiry: Later writes may reintroduce matches; rescan covers current selected roots only.
- Activation or effect: Local removal enforced after apply; verification reports residue without undoing prior effects.
- Evidence limits: Not factual refutation, semantic-safe redaction, global erasure or guaranteed complete withdrawal from every host context.

>         verification = scan_retract_roots(roots, byte_patterns, name_patterns)
> --- `scripts/llm-wiki`

>             data = data.replace(pattern, replacement)
> --- `scripts/llm-wiki`

#### EPI-RTE-fixture-evaluation
Label: Synthetic fixture delivery and grading

Part of: [RT-RTE-query-evaluation](runtime.md#rt-rte-query-evaluation)

This record individuates the fixture-delivery and check/evidence-production parts of the supplied benchmark container, not its invocation, persistence or maintainer-deployment decisions. The JS assertions below are inspected comparison evaluators, not claimed parts of that benchmark implementation; no separate assertion-route declaration or complete behavioral-evaluation account is made here.

SRC-1 `scripts/benchmark-token-efficiency`, `grade_output`/`handle_fixture_tool`; `tests/evals/assertions/check-frontmatter.js`, `tests/evals/assertions/check-index-integrity.js`, `tests/evals/assertions/check-raw-source.js`; initial `tests/promptfooconfig.yaml`. The benchmark part and the separately inspected assertion surfaces share reporting purpose, not production truth adjudication. Candidate model output is proposed by the external host; cases supply required/forbidden terms and length oracle. Grader uses casefolded substring tests. Concrete deduction: for required `alpha`, no forbidden terms and max length 4000, output `not alpha` passes this grader, despite negating the term. Other driver requirements may still fail; this establishes only the local term check limit. Fixture tool resolves/guards a relative file path, reads UTF-8 and truncates above 100000 characters before delivery; activity byte count reports file size, not guaranteed full content delivered.

Additional JS targets are field presence/enums, subdirectory indexes, and first raw article containing field-name substrings. Raw-source assertion does not verify that fields are in parsed frontmatter. Frontmatter assertion can return pass if raw/wiki directories are absent because checkFiles returns no errors. Index assertion ignores hidden subdirectories. Behavioral config uses external model-rubric and skill-used assertions with cost thresholds; a rubric is a requested model judgment of a case, not an observed pass. Bounded synthetic experiment mode; maintainer selects variants and decides any deployment. Rejection is a failing grade/report, not automatic production rollback or profile replacement. No causal attribution without independent treatment comparison.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Delivered fixture prefix/path error or structured grades, misses and metrics.
- Later read-back: Benchmark reports available to maintainers; no automatic installation of winning instructions established.
- Delegated visibility: Model receives selected/truncated file text, not a guarantee of entire fixture.
- Selection predicate: Cases and requested paths, containment/file checks; term/length and driver-specific read/tool checks.
- Invalidation or expiry: Fixture/instruction digests qualify comparisons; changed fixtures invalidate unqualified cross-report attribution.
- Activation or effect: Enforcing tool containment and grading; advisory reports for product changes.
- Evidence limits: No observed run, token-saving result, general factual oracle, calibrated robustness or successful improvement.

>     if len(content) > 100_000:
>         content = content[:100_000] + "\n[truncated by benchmark harness]"
> --- `scripts/benchmark-token-efficiency`

>     missing = [term for term in case.get("required", []) if term.casefold() not in folded]
>     forbidden = [term for term in case.get("forbidden", []) if term.casefold() in folded]
> --- `scripts/benchmark-token-efficiency`

>   const missing = requiredFields.filter(f => !content.includes(f));
> --- `tests/evals/assertions/check-raw-source.js`

>   if (!fs.existsSync(dir)) return errors;
> --- `tests/evals/assertions/check-frontmatter.js`

>     const subdirs = entries.filter(e => e.isDirectory() && !e.name.startsWith('.'));
> --- `tests/evals/assertions/check-index-integrity.js`

### Claims

#### EPI-CLM-compiled-knowledge
Label: LLM-compiled knowledge

The public skill presents source-to-article compilation as a knowledge base, with the host as compiler and query engine. SRC-1 `claude-plugin/skills/wiki-manager/SKILL.md`; doctrine/design. No counterpart claim is supplied by runtime; distinct from its concurrency claim.

> You manage an LLM-compiled knowledge base. Source documents are ingested into `raw/`, then incrementally compiled into a wiki of interconnected markdown articles. Claude Code is both the compiler and the query engine — no Obsidian, no external tools.
> --- `claude-plugin/skills/wiki-manager/SKILL.md`

#### EPI-CLM-audit-trust
Label: Audit trust inspection

Audit purports to answer whether current knowledge and outputs can be trusted, with adversarial evidence escalation and unresolved states. SRC-1 `claude-plugin/skills/wiki-manager/references/audit.md`; doctrine/design. No counterpart claim is supplied by runtime; distinct from its concurrency claim.

> Umbrella truth-seeking audit for llm-wiki. If `/wiki:librarian` keeps the
> `wiki/` layer in check, `/wiki:audit` answers a broader question: can the user
> trust the current knowledge and outputs right now?
> --- `claude-plugin/skills/wiki-manager/references/audit.md`

#### EPI-CLM-feedback-noise
Label: Feedback candidate noise control

Candidate capture/review/promotion is claimed to keep noise out while preserving useful corrections and contextual validation. SRC-1 `claude-plugin/skills/wiki-manager/references/feedback.md`; doctrine/design. No counterpart claim is supplied by runtime; distinct from its concurrency claim.

> This keeps the wiki from learning noise while still preserving corrections,
> preferences, and validation that should influence future sessions.
> --- `claude-plugin/skills/wiki-manager/references/feedback.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; consumers, channels, force and horizons are specified in route records and the ledger.
