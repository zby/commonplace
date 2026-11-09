---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenKB epistemic routes: document synthesis, grounding policy, maintenance checks and skill evaluation at the frozen source."
run-id: AAS-2026-11-09-openkb-bd9c4c38a842-01
reviewed-boundary: "ff54396e575ee6feb0113b631a34caa082b441cc"
---

# OpenKB epistemic report

## Source-and-claim boundary

The question is what licenses reliance on OpenKB's compiled wiki, answers and portable skills, and what checks actually change their subsequent use. Scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is SRC-1 in its [Source register](boundary.md#source-register). Source inspection supplies implementation and doctrine/design only. No target execution, tests, provider calls or external research were performed. The frozen checkout HEAD was checked against the reviewed revision.

The supplied runtime is a provisional route map, not an inspection limit. Direct reads added semantic lint, deterministic link cleanup, source-withdrawal internals, skill graders and their CLI consumer. These are finer parts or checks within the runtime's valid containers; no supplied record needs supersession. In particular, [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) is not evidence that removing a document removes every proposition learned from it.

| Entry point or operation | Source path (SRC-1) | Coverage and supporting records |
| --- | --- | --- |
| CLI add, upload, watch and cloud import; commit/log hooks | `openkb/cli.py`, `openkb/api.py`, `openkb/watch_service.py`, `openkb/add_coordinator.py` | Supplied [RT-RTE-document-add](runtime.md#rt-rte-document-add); direct CLI hook inspection confirms log hook, not semantic approval. API dispatch searched; watcher/indexer internals rely on supplied findings. |
| Short compilation; long-summary compilation | `openkb/agent/compiler.py` | Direct templates, page parser/filter, short/long entry and removal reads; [RT-RTE-document-add](runtime.md#rt-rte-document-add), [EPI-OBJ-summary](#epi-obj-summary), [EPI-OBJ-concept](#epi-obj-concept), [EPI-OBJ-entity](#epi-obj-entity). PageIndex internals remain excluded. |
| Query and saved answers | `openkb/agent/query.py`, `openkb/agent/tools.py`, `openkb/cli.py` | Direct query instructions/build opening; tools and save consumers supplied by [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). Source acquisition differs from answer generation. |
| Chat resume, installed skills and writes | `openkb/agent/chat.py`, `openkb/agent/chat_session.py`, `openkb/agent/skills.py` | Supplied [RT-RTE-session-chat](runtime.md#rt-rte-session-chat), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions); no supplied conversation demonstrates grounding or instruction compliance. |
| Remove and recompile | `openkb/cli.py`, `openkb/agent/compiler.py` | Supplied [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain); direct source-removal helpers, [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal). |
| CLI/chat/REST lint and fix | `openkb/agent/linter.py`, `openkb/lint.py`, `openkb/cli.py`, `openkb/api.py` | Direct lint agent, CLI and REST report consumer, fix implementation; [EPI-RTE-semantic-lint](#epi-rte-semantic-lint), [EPI-RTE-link-cleanup](#epi-rte-link-cleanup). Structural check inventory partly supplied; no comprehensive semantic negative inferred. |
| Skill new/validate/rollback and marketplace | `openkb/skill/generator.py`, `openkb/skill/validator.py`, `openkb/skill/creator.py`, `openkb/cli.py` | Direct validator; creator/generator/admission supplied by [RT-RTE-skill-create](runtime.md#rt-rte-skill-create). Generation does not imply installation. |
| Skill eval and saved eval-set replay | `openkb/skill/evaluator.py`, `openkb/cli.py` | Direct evaluator and entire CLI eval consumer; [EPI-RTE-eval-set](#epi-rte-eval-set), [EPI-RTE-trigger-grade](#epi-rte-trigger-grade), [EPI-RTE-body-grade](#epi-rte-body-grade). |
| Deck production and optional critic | `openkb/deck/creator.py`, `openkb/agent/skill_runner.py` | Supplied [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce). Full critic styling instructions and validator internals not directly inspected here; prevents a system-complete negative about all possible content checks. |
| Visualization, browser display and external-agent reading | `openkb/visualize.py`, `frontend/src/pages/ChatSession.tsx`, `skills/openkb/SKILL.md` | Boundary/supplied runtime only; trust policy [RT-CLM-wiki-trust](runtime.md#rt-clm-wiki-trust). No independent graph-truth evaluator assessment; enclosing host operation excluded. |
| Samples, model/service/dependency internals | `examples/`, `pyproject.toml` | Samples not inspected for outcomes; no actual KB corpus or authenticated execution trace supplied. Provider and dependency implementations outside boundary. Prevents efficacy, complete output lineage and causal attribution. |

Consequential claims are [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki), [RT-CLM-wiki-trust](runtime.md#rt-clm-wiki-trust), [EPI-CLM-current-synthesis](#epi-clm-current-synthesis), [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) and [EPI-CLM-body-alignment](#epi-clm-body-alignment). Missing source truth assessments prevent warrant transfer from “ingested” to “true.” Missing candidate/run evidence prevents deciding which generated sentences merely restate premises, follow from them, or add conjectures. Missing independent outcome comparisons prevents attributing retrieval accuracy, learning or improved artifact quality to these routes. Uninspected included helpers are not evidenced absences.

## Epistemic-object inventory

The rows separate operative parts, not merely filenames. Candidate truth-apt content is assessed here; source-native form/substrate and producers/consumers are owned by the cited records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-source-content](#epi-obj-source-content) | Imported assertions, tables and images over the document's own domain | see record | SRC-1, `openkb/agent/query.py` | Extraction fidelity and original truth unknown; an accessible source is not endorsed. |
| [EPI-OBJ-summary](#epi-obj-summary) | Claims about a particular document's findings | see record | SRC-1, `openkb/agent/compiler.py` | Full-text short path differs from PageIndex summary/overview path; no output-grounding check established. |
| [EPI-OBJ-concept](#epi-obj-concept) | Cross-document topic explanations and synthesis | see record | SRC-1, `openkb/agent/compiler.py` | New text is not necessarily new knowledge; entailment and non-entailment both unresolved without instances. |
| [EPI-OBJ-entity](#epi-obj-entity) | Facts about named things accumulated across documents | see record | SRC-1, `openkb/agent/compiler.py` | Type-enum admission does not assess these facts. |
| [RT-OBJ-agents-md](runtime.md#rt-obj-agents-md) | Mixed schema rules; no distinct empirical claim established here | see record | SRC-1, `openkb/schema.py` | Instruction authority differs from source-evidence authority. |
| [EPI-OBJ-answer](#epi-obj-answer) | Answer propositions and saved explorations | see record | SRC-1, `openkb/agent/query.py` | Wiki-only/citation policy is not evidence of faithful or complete grounding. |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Claims that particular pages contradict, omit or duplicate content | see record | SRC-1, `openkb/agent/linter.py` | Model judgments may be wrong; failure text can also be retained as a report. |
| [EPI-OBJ-skill-content](#epi-obj-skill-content) | Portable instructions plus reference assertions and activation description | see record | SRC-1, `openkb/skill/evaluator.py` | Description-only trigger grading differs from body/reference-preview grading. |
| [EPI-OBJ-eval-prompts](#epi-obj-eval-prompts) | Question/expected-label pairs; “this skill should trigger” is scoped to the question | see record | SRC-1, `openkb/skill/evaluator.py` | Generated or imported labels are not independently established answer references. |
| [RT-CMP-litellm-model](runtime.md#rt-cmp-litellm-model), [RT-CMP-pageindex-client](runtime.md#rt-cmp-pageindex-client) | Truth-apt internal content not determinable from exposed numerical state | see records | SRC-1, `openkb/agent/compiler.py`, `openkb/indexer.py` | Inference interfaces establish no weight-update, provider-memory or inner-evaluator account. |
| [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | Deck assertions may be truth-apt; formatting/HTML rules are a separate symbolic target | see record | SRC-1, `openkb/deck/creator.py` | No artifact supplied to individuate truth claims; critic edits are not necessarily epistemic revisions. |

## Authority-route ledger

Architectural status describes inspected wiring or the bounded absence of an acceptance route, not observed use. “See” delegates source-native operational fields to their owning record. Relations classify content edges, not entire pipelines. Model-generated summaries, answers and skills remain **indeterminate** between non-ampliative reshaping, entailed derivation and ampliative conjecture: requesting synthesis alone proves neither entailment nor non-entailment.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | content transformation | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | truth-apt transformation: acquisition/import | External document to converted text/PageIndex material | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Imported content | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Source warrant unknown; no endorsement | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/converter.py` | [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki) | none | Conversion and indexer supplied findings; fidelity unmeasured. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | content transformation | implemented | [EPI-OBJ-summary](#epi-obj-summary) | truth-apt transformation: indeterminate | Source/summary and existing page to summary | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Candidate authored text | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | No additional truth license from fluent generation | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | completeness unknown | No generated instance establishes semantic preservation or conjectural novelty. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | content transformation | implemented | [EPI-OBJ-concept](#epi-obj-concept) | truth-apt transformation: indeterminate | Source/summary and existing page to concept | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Candidate authored text | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | No additional truth license from fluent generation | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | completeness unknown | No generated instance establishes semantic preservation or conjectural novelty. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | content transformation | implemented | [EPI-OBJ-entity](#epi-obj-entity) | truth-apt transformation: indeterminate | Source/summary and existing page to entity | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Candidate authored text | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | No additional truth license from fluent generation | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | completeness unknown | No generated instance establishes semantic preservation or conjectural novelty. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | check/evidence production | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | Plan shape, body nonemptiness, entity type and link target set | Python parsers/predicates; structural domain only | Before selected writes | Keep/drop/coerce/error; see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Constrains writes | Only checked structural properties, not factual accuracy | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | none | none | Plain non-JSON prose can be accepted; page failures can be omitted. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | disposition/acceptance | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | Admit generated pages to persistent wiki | Software; structural conditions and exception handling | During compilation | Persist/skip/fail; see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Programmatic admission | Operational admission, not evidence-consuming semantic acceptance | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | admission is not warrant | No per-page human approval or expected-fact oracle in this path. |
| [RT-RTE-document-add](runtime.md#rt-rte-document-add) | retention | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | Admitted body to filesystem | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Persistent pages | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | Persistence supplies availability, not truth | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | see [RT-RTE-document-add](runtime.md#rt-rte-document-add) | SRC-1, `openkb/agent/compiler.py` | [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki) | none | Backlinks/indexing organize pre-acceptance candidates; not lifecycle integration after acceptance. |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | operational admission/selection/consumption | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | Select evidence for answering | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Selected text/pages/images | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Access to evidence; correctness not licensed | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | SRC-1, `openkb/agent/query.py` | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | grounding policy | No independent relevance or source-truth check; whole JSON read alternate remains possible. |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | content transformation | implemented | [EPI-OBJ-answer](#epi-obj-answer) | truth-apt transformation: indeterminate | Selected wiki to answer | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Candidate final answer | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | Requested citations do not establish support | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | SRC-1, `openkb/agent/query.py` | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | outcome unknown | No semantic acceptance gate in inspected answering loop. |
| [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | retention | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | Answer/history/output for later turns | see [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | see [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | Saved history/explorations | see [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | Prior utterance remains prior utterance, not validated fact | see [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | see [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) | SRC-1, `openkb/agent/chat_session.py` | none | none | Image removal/reload changes context availability, not epistemic endorsement. |
| [EPI-RTE-semantic-lint](#epi-rte-semantic-lint) | check/evidence production | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: indeterminate | Wiki consistency/coverage/staleness | Model with list/read and schema, not external truth oracle | Explicit lint; see record | Issue report or failure text | Advisory diagnostic | Candidate criticism scoped to read pages | No automatic semantic revision/rejection | see record | SRC-1, `openkb/agent/linter.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | flags not repairs | Operational route exists; actual discovery quality unobserved. |
| [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) | retention | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | no content change | Combined lint report to reports directory | see [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) | see [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) | Report persisted | Diagnostic availability | Not acceptance of report propositions | see [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) | see [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) | SRC-1, `openkb/cli.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | none | Semantic failure can itself be written as report text. |
| [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | content transformation | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Link syntax against existing target names | Deterministic set/normalization; not proposition truth | Compiler/save/fix consumers; see record | Canonical link or plain text | Enforcing link rewrite | Resolvability only; displayed assertion may survive | see record | see record | SRC-1, `openkb/lint.py` | none | none | Name normalization may merge intended referents; reshaping classification limited to syntactic edge. |
| [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | lineage/freshness/recovery | implemented | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Remove source metadata/reference; optionally whole page | Exact source-list membership and link text; Python | Explicit remove | Delete page or retain body without that citation | Enforcing metadata/page change | No claim-level retraction or reassessment established | see record | see record | SRC-1, `openkb/agent/compiler.py` | [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | withdrawal scope | Retained multisource prose can outlive removed evidence. |
| [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | content transformation | implemented | [EPI-OBJ-skill-content](#epi-obj-skill-content) | truth-apt transformation: indeterminate | Wiki/intent to portable text | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | Candidate instructions/references | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | No semantic truth license from distillation | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | SRC-1, `openkb/skill/creator.py` | [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki) | none | Non-truth-apt method directions coexist; no instance to classify each proposition. |
| [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | check/evidence production | implemented | [EPI-OBJ-skill-content](#epi-obj-skill-content) | no content change | Skill metadata, sizes, links and optional imports | Deterministic validator, structural domain | After creator and explicit validate | Errors/warnings | Diagnostic; see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | Checked syntax/portability only | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | see [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) | SRC-1, `openkb/skill/validator.py` | none | not universal gate | Generator retains files and regenerates marketplace despite findings. |
| [EPI-RTE-eval-set](#epi-rte-eval-set) | content transformation | implemented | [EPI-OBJ-eval-prompts](#epi-obj-eval-prompts) | truth-apt transformation: indeterminate | Skill text to question/expected-label set; or import saved labels | Model generator; saved-set loader alternative | Requested eval; see record | Labeled prompts | Grader reference selection | Reference labels express intended trigger scope, not factual answers | see record | see record | SRC-1, `openkb/skill/evaluator.py` | [EPI-CLM-body-alignment](#epi-clm-body-alignment) | reference provenance | Generated labels may share model biases with graders. |
| [EPI-RTE-trigger-grade](#epi-rte-trigger-grade) | check/evidence production | implemented | [EPI-OBJ-skill-content](#epi-obj-skill-content) | truth-apt transformation: indeterminate | Description-only activation on labeled questions | Model verdict vs supplied/generated expected label | Requested eval | Trigger/no-trigger; ambiguous defaults no-trigger | Diagnostic comparison | Agreement with labels, not executed task correctness | see record | see record | SRC-1, `openkb/skill/evaluator.py` | [EPI-CLM-body-alignment](#epi-clm-body-alignment) | proxy evaluator | Malformed verdict can count as a correct negative. |
| [EPI-RTE-body-grade](#epi-rte-body-grade) | check/evidence production | implemented | [EPI-OBJ-skill-content](#epi-obj-skill-content) | truth-apt transformation: indeterminate | Body and reference prefixes sufficient for selected questions | Model coverage verdict, no actual task run | Should-trigger questions only | Supported/unsupported/ambiguous/error | Diagnostic report | Judged textual support, not factual truth or demonstrated capability | see record | see record | SRC-1, `openkb/skill/evaluator.py` | [EPI-CLM-body-alignment](#epi-clm-body-alignment) | preview and proxy | Excludes ambiguous/error cases from denominator; no automated replacement consumer. |
| [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | check/evidence production | implemented | [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | no content change | Expected artifact existence and optional grammar | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | Existence/validation result | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | File/grammar license, not knowledge acceptance | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | SRC-1, `openkb/agent/skill_runner.py` | none | none | Conditional validator; final post-critic validity not established. |
| [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | content transformation | implemented | [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | truth-apt transformation: indeterminate | Optional critic revises artifact | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | Possibly patched HTML | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | No truth license from critic role alone | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | see [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) | SRC-1, `openkb/deck/creator.py` | none | none | Whether any edit changes a truth-apt claim cannot be determined without artifact/trace. |

The inspected compiler's structural check is explicit (SRC-1, `openkb/agent/compiler.py`); the supplied [RT-RTE-document-add](runtime.md#rt-rte-document-add) supplies its consequential skip/failure consumers:

> def _require_nonempty_content(content, name: str) -> None:
>     """Raise if a concept body is missing or whitespace-only."""
>     if not isinstance(content, str) or not content.strip():
>         raise ValueError(f"LLM returned empty content for concept {name!r}")
> --- `openkb/agent/compiler.py`

The searched compiler/query/lint/evaluation paths establish operational admission and retention, but no evidence-consuming semantic acceptance decision specifying criterion, intended use and proposition scope. Consequently their index/backlink organization is not established as **lifecycle integration after acceptance**. This is a bounded finding, not a system-complete negative about every included helper, external host or opaque model process. The positive semantic lint and coverage graders are counterexamples to “OpenKB never checks content”; neither is wired here as a universal truth gate.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-document-add](runtime.md#rt-rte-document-add), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | None supplied | No comparison; dependency internals excluded | Persistent structured compilation is wired | Knowledge quality and retrieval accuracy not established |
| [EPI-CLM-current-synthesis](#epi-clm-current-synthesis) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-document-add](runtime.md#rt-rte-document-add), [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain), [EPI-RTE-semantic-lint](#epi-rte-semantic-lint), [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | None supplied | No corpus-completeness/outcome experiment | Selected old/new pages are synthesized; explicit lint can flag candidate contradictions | “Everything consumed” is stronger than shown coverage; summary bottlenecks, collected failures and partial withdrawal prevent that guarantee |
| [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | see record | SRC-1, `README.md`; doctrine/design | Query prompt requests wiki-only cited answers | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | None supplied | No groundedness scoring or external truth comparison | Model is given evidence access and grounding instructions | Reliable citation support, completeness and correctness unknown |
| [EPI-CLM-body-alignment](#epi-clm-body-alignment) | see record | SRC-1, `openkb/skill/evaluator.py`; doctrine/design | see record | [EPI-RTE-eval-set](#epi-rte-eval-set), [EPI-RTE-trigger-grade](#epi-rte-trigger-grade), [EPI-RTE-body-grade](#epi-rte-body-grade) | None supplied | Shared model, generated labels, truncated references, no task execution | Two distinct diagnostic model judgments and deterministic score aggregation | “Actually answer” is not demonstrated; textual-support judgment is narrower |
| [RT-CLM-wiki-trust](runtime.md#rt-clm-wiki-trust) | see record | SRC-1, `skills/openkb/SKILL.md`; doctrine/design | see record | [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions) concerns a separate host/runner path; no deterministic trust filter established | None supplied | External-host compliance outside boundary | Untrusted-data policy is declared | Neither immunity nor host enforcement follows |

## Bounded conclusion

OpenKB acquires document content with **unknown source warrant**, then retains model-authored summaries, concepts and entity assertions for later answering and generation. Short compilation receives full converted text; long compilation receives a PageIndex summary and generated overview. The source-preservation request in summary rewrite is real, but it is model guidance rather than a checked semantic invariant. No specific new proposition is established as entailed derivation or ampliative conjecture by the available implementation alone. No warranted premises and checked inference chain establish produced knowledge here.

Its operational authority is stronger than its demonstrated epistemic license. Parser, enum, nonempty-body and filesystem controls can permit, skip or reject writes; no per-page human acceptance is required. Retained bodies become future query/compiler/generator evidence without an intervening demonstrated truth decision. The consumer, channel, force and horizon are those of [RT-RTE-document-add](runtime.md#rt-rte-document-add), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) and [RT-RTE-skill-create](runtime.md#rt-rte-skill-create). These are operative routes, not merely storage affordances; actual compliance and benefit remain unobserved.

The material evaluation criteria differ. Semantic lint requests contradictions, gaps, staleness, redundancy and coverage over read wiki pages, returns an advisory report, and has no implemented semantic repair consumer in the inspected drivers. Structural cleanup instead enforces link resolvability and can erase a citation while leaving the assertion. Source removal deletes single-source pages when configured, but multisource bodies need not lose the removed source's factual contribution. Thus citation withdrawal is not equivalent to proposition withdrawal.

Skill evaluation compares description-only activation to expected labels and asks a different model call whether body/reference excerpts support should-trigger questions. These checks supply advisory diagnostics to the CLI, not an admission veto or an answer-truth oracle. Their intended use is trigger and textual-coverage assessment, not measured skill execution. Skill validation likewise checks structure and portability; it does not gate all generated output. Optional deck criticism has a direct work-product write path, but no outcome evidence establishes factual improvement or final validity.

Schema and installed skill text can change future model guidance through [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions) and [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions). This is instruction-mediated behavioral authority, distinct from knowledge acceptance. Nothing inspected establishes model-parameter training. Persistence and possible future reuse do not establish improved capacity (learning), self-representation with both causal directions (reflection), or method criticism retained into a next method-revision round (theory building). Independent inference/tool autonomy within bounded requests does not supply those missing properties. No exercised self-improvement or causal quality benefit is established; this does not negate the implemented retention, synthesis, diagnostic and artifact-editing routes.

## Shared records

### Operative objects

#### EPI-OBJ-source-content
Label: Imported document content

Identity: converted source Markdown, long-document page JSON and associated images used by compiler/query. Natural-language assertions and numerical/tabular/image content, on filesystem; JSON page selectors are symbolic wrappers, not evidence that the assertions are true. Distinct from [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages): input/evidence rather than generated summary/concept/entity bodies. Closest supplied route: [RT-RTE-document-add](runtime.md#rt-rte-document-add); acquisition/extraction details are supplied there. SRC-1, `openkb/agent/query.py` (doctrine/design and implemented tool construction).

> Summaries may omit details — if you need more, follow the summary's
>    `full_text` frontmatter field to the source (see step 4).
> --- `openkb/agent/query.py`

#### EPI-OBJ-summary
Label: Summary page bodies
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Natural-language Markdown assertions retained in wiki summary files. Short-document producer reads converted text; long-document producer includes indexer output plus overview context. Intended role: describe a document's key findings and route deeper reads. Form/substrate inherited from the container, but generation context differs from concepts/entities. SRC-1, `openkb/agent/compiler.py` (implementation and template doctrine).

> content = source_path.read_text(encoding="utf-8")
> --- `openkb/agent/compiler.py`

> _LONG_DOC_SUMMARY_USER = """\
> This is a PageIndex summary for long document "{doc_name}" (doc_id: {doc_id}):
>
> {content}
>
> Based on this structured summary, write a concise overview that captures \
> the key themes and findings. This will be used to generate concept pages.
> --- `openkb/agent/compiler.py`

The summary-rewrite template requests preservation, rather than checking it (SRC-1, `openkb/agent/compiler.py`, doctrine/design):

> - Preserve every factual claim, finding, and detail from your draft. Do \
> NOT add or remove technical content, examples, or claims.
> --- `openkb/agent/compiler.py`

#### EPI-OBJ-concept
Label: Concept page bodies
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Natural-language Markdown topic explanations on filesystem, generated or rewritten using current source/summary context and selected existing page. Intended cross-document synthesis differs from one-document summary and named-entity fact accumulation. SRC-1, `openkb/agent/compiler.py` (template doctrine; entry implementation supplied in [RT-RTE-document-add](runtime.md#rt-rte-document-add)).

> New information from document "{doc_name}" (summarized above) should be \
> integrated into this page. Rewrite the full page incorporating the new \
> information naturally — do not just append. Preserve the existing structure \
> and intent of the page.
> --- `openkb/agent/compiler.py`

#### EPI-OBJ-entity
Label: Entity page bodies
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Natural-language Markdown facts about a named entity on filesystem; symbolic configured entity types shape admission separately from factual content. SRC-1, `openkb/agent/compiler.py` (template doctrine and inspected type filtering). Distinct part from concept abstraction.

> Integrate the new facts about this entity from document "{doc_name}"
> (summarized above). Rewrite the full page — do not just append. Preserve the
> existing structure and intent. Follow the whitelist rules from the message
> above for all [[wikilinks]].
> --- `openkb/agent/compiler.py`

#### EPI-OBJ-answer
Label: Query answer and exploration text

Identity: final model answer, optionally saved exploration, and answer turns retained in chat history. Natural-language propositions, initially SDK/string state then optionally Markdown/session storage. Different referent from [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages), which identifies compiled bodies, not answers. Closest supplied [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) establish consumer and persistence paths. SRC-1, `openkb/agent/query.py`; the instruction supplies intent, not compliance.

> 7. Synthesize a clear, concise, well-cited answer grounded in wiki content.
> --- `openkb/agent/query.py`

#### EPI-OBJ-lint-report
Label: Semantic lint report

Identity: issue claims produced by wiki-linter and combined with structural output under wiki/reports. Natural-language Markdown on filesystem; not the compiled bodies in [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages). Closest supplied [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) includes this output route but declares no report object. SRC-1, `openkb/agent/linter.py`, `openkb/cli.py` (implementation).

> return result.final_output or "Knowledge lint completed. No output produced."
> --- `openkb/agent/linter.py`

> report_content = (
>     f"# Lint Report — {timestamp}\n\n"
>     f"## Structural\n\n{structural_report}\n\n"
>     f"## Semantic\n\n{knowledge_report}\n"
> )
> report_path.write_text(report_content, encoding="utf-8")
> append_log(kb_dir / "wiki", "lint", f"report → {report_path.name}")
> --- `openkb/cli.py`

#### EPI-OBJ-skill-content
Label: Skill body, description and references

Identity: SKILL.md activation description and natural-language instructions/body plus Markdown references under generated skill directory. Filesystem storage; YAML metadata is symbolic, description and body are interpreted text. Split consumption: trigger grader receives description only; coverage grader gets body and each reference prefix; installed runner is a further consumer, not the evaluator. Closest supplied [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) declares creation route, not this operative object; distinct from compiled wiki input. SRC-1, `openkb/skill/evaluator.py`.

> return f"SKILL.md body:\n{body}\n\nReferences (excerpts):\n{refs}"
> --- `openkb/skill/evaluator.py`

#### EPI-OBJ-eval-prompts
Label: EvalPrompt expected labels

Identity: EvalPrompt question and expected activation label, generated in memory or loaded/saved as JSON under .openkb/eval-sets. Natural-language question plus symbolic trigger/no-trigger label consumed by comparison rules. Distinct from skill content and from supplied [RT-RTE-skill-create](runtime.md#rt-rte-skill-create), whose producer does not establish these evaluation references. SRC-1, `openkb/skill/evaluator.py`.

> @dataclass
> class EvalPrompt:
>     question: str
>     expected: Literal["trigger", "no-trigger"]
> --- `openkb/skill/evaluator.py`

### Routes

#### EPI-RTE-semantic-lint
Label: Semantic knowledge lint
Part of: [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain)

Endpoints: wiki files/schema to wiki-linter through list/read tools, then final report to CLI/chat/REST lint driver. Model chooses pages and judges candidate issues; host retains report, including exception text on failure. Distinct material check within maintenance container; not semantic disposition or repair. SRC-1, `openkb/agent/linter.py`, `openkb/cli.py` (implementation and doctrine/design). Check target: consistency, coverage, possible staleness and redundancy of the pages read. The model proposes findings; code records them, no human approval of each finding or automated factual veto. Mode: explicit open audit, no expected-answer oracle. Report recommendations do not automatically rewrite wiki claims in the inspected consumers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown issue report or failure/no-output message.
- Later read-back: Combined lint report persists for later inspection; no automatic semantic-fix consumer found in inspected CLI/REST lint drivers.
- Delegated visibility: Lint model sees schema, user audit request and selected list/read tool outputs; no writer registered.
- Selection predicate: Explicit lint invocation; model-selected files; CLI skips report generation when no document hashes.
- Invalidation or expiry: inapplicable — reports are retained diagnostics, not admission tokens with expiry.
- Activation or effect: Report publication is wired; operational use of recommendations unobserved.
- Evidence limits: No trace demonstrates detected contradictions, accuracy, corrective uptake or benefit.

> tools=[list_files, read_file],
> --- `openkb/agent/linter.py`

> 1. **Contradictions** — Do any pages make conflicting claims about the same fact?
> --- `openkb/agent/linter.py`

> try:
>     knowledge_report = await run_knowledge_lint(kb_dir, model)
> except Exception as exc:
>     knowledge_report = f"Knowledge lint failed: {exc}"
> --- `openkb/cli.py`

#### EPI-RTE-link-cleanup
Label: Wikilink cleanup
Endpoints: candidate/retained Markdown and valid-target set to strip_ghost_wikilinks; compiler, query-save and lint-fix consumers can persist rewritten text. Python owns target normalization, exact/fuzzy lookup and text substitution; no model judge. Closest supplied [RT-RTE-document-add](runtime.md#rt-rte-document-add), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) overlap different callers; this reusable text transformation spans them and is not part of exactly one. SRC-1, `openkb/lint.py` implementation; caller evidence supplied by those records plus direct fix read. Target/domain: target-name resolvability, not the truth of a link's surrounding sentence. Code deduction, not target execution: with known_targets={concepts/attention}, input “See [[concepts/Missing|a mechanism]].” misses direct and normalized lookup; it becomes “See a mechanism.” and records concepts/Missing as a ghost. With concepts/Attention against that target set, normalized lookup rewrites to concepts/attention. The claim text can remain while its evidential/navigation link is lost. No entailment or semantic endorsement is created.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned text and ghost-target list; fix wrapper returns changed-file and ghost counts.
- Later read-back: Persisted rewritten pages/explorations are available to later query and compilation.
- Delegated visibility: inapplicable — transformation is deterministic Python, not a delegated model call.
- Selection predicate: Regex wikilinks; supplied known-target set, exact match then normalized match; fix wrapper excludes reports/sources/schema/log by default.
- Invalidation or expiry: Target set is rebuilt from current files for fix; no independent truth-invalidity marker is written.
- Activation or effect: Unresolvable brackets removed or canonical link substituted; fix writes changed files.
- Evidence limits: Deduction from inspected code, not observed execution; normalization is name equivalence, not a referent-identity proof.

> ghosts.append(target)
> if alias:
>     return alias
> stem = target.rsplit("/", 1)[-1]
> return stem.replace("-", " ").replace("_", " ")
> --- `openkb/lint.py`

> if cleaned != text:
>     atomic_write_text(md, cleaned)
>     files_changed += 1
>     ghosts_stripped += len(ghosts)
> --- `openkb/lint.py`

#### EPI-RTE-source-withdrawal
Label: Source reference withdrawal
Part of: [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain)

Endpoints: removed document identifier to source-frontmatter/link cleanup in concept/entity files, then delete-or-rewrite and subsequent queries. Python owns exact source membership and filename traversal, not semantic contribution analysis. SRC-1, `openkb/agent/compiler.py` implementation; caller/retry registry behavior supplied by [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain). User initiates/approves remove; code applies changes, with keep_empty controlling the empty-source deletion veto. Intended use is source withdrawal, not criterion-based truth acceptance. Recovery/partial PageIndex failure stays as in the supplied container.

Counterexample to complete factual withdrawal, deduced from inspected implementation: a valid inline sources list with summaries/a.md and summaries/b.md plus body “A says P.” loses only summaries/a.md when a is removed. sources_empty is false, the modified page is written, and this plain prose is unchanged. Thus even correct source metadata cleanup need not retract a's asserted contribution. No target fixture or execution is needed for this deduction.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Modified/deleted slug lists to remove driver.
- Later read-back: Multisource body can remain queryable without the removed citation; deleted pages no longer read by filename.
- Delegated visibility: inapplicable — no semantic model is called by this helper.
- Selection predicate: Concept/entity files referencing the source marker; parsed inline source membership, related-document link and standalone See also patterns.
- Invalidation or expiry: Delete page if last source removed and keep_empty false; otherwise update metadata/references.
- Activation or effect: Filesystem deletion/rewrite changes later available evidence; no proposition-level revalidation is wired here.
- Evidence limits: Malformed/no frontmatter can bypass source-list updates; not a proof of complete cleanup for arbitrary hand-edited pages.

> items.remove(source_file)
> fm_lines[i] = _yaml_list_line("sources", items)
> return "\n".join(fm_lines) + closing + body, len(items) == 0
> --- `openkb/agent/compiler.py`

> if sources_empty and not keep_empty:
>     path.unlink()
>     deleted.append(path.stem)
> elif new_text != text:
>     atomic_write_text(path, new_text)
>     modified.append(path.stem)
> --- `openkb/agent/compiler.py`

#### EPI-RTE-eval-set
Label: Generate or reload evaluation set
Endpoints: skill description/body/reference prefixes to generator model, parsed JSON to expected labels; alternatively saved JSON to load_eval_set. CLI can retain newly generated prompts. Owner: model proposes questions and labels through should_trigger/should_not groups; code parses and records them. SRC-1, `openkb/skill/evaluator.py`, `openkb/cli.py` implementation. Closest supplied [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) mentions separate diagnostics but does not individuate the reference-generation route; different operation from authoring the skill. Mode: bounded generated/replayed evaluation set, not open artifact generation. Oracle: expected activation labels come from generator or saved-set supplier, not verified task answers. User selects set/count/model; no per-label human approval required. No installed instruction change is admitted by this route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of EvalPrompt questions and expected labels.
- Later read-back: Optional CLI save writes .openkb/eval-sets/<name>.json; --eval-set reloads labels for later diagnostic runs.
- Delegated visibility: Generator gets description, entire extracted body and reference previews; no wiki/tool-executed task result.
- Selection predicate: Fresh generation unless caller supplies eval_set; CLI --save only saves newly generated sets.
- Invalidation or expiry: Explicit file replacement/replay; no automatic invalidation when skill changes established.
- Activation or effect: Expected labels select coverage prompts and reference trigger comparisons; no automatic successor installation.
- Evidence limits: No label accuracy or actual generation trace supplied; defaults use same configured model family for generator and graders.

> try:
>     data = json.loads(raw)
> except json.JSONDecodeError as exc:
>     raise RuntimeError(
>         f"Eval set generator returned non-JSON output: {exc.msg}. "
>         f"Try a more capable model — small models often ignore "
>         f"'output only JSON' instructions. First 200 chars: {raw[:200]!r}"
>     ) from exc
> prompts: list[EvalPrompt] = []
> for q in data.get("should_trigger", []):
>     prompts.append(EvalPrompt(question=q, expected="trigger"))
> for q in data.get("should_not", []):
>     prompts.append(EvalPrompt(question=q, expected="no-trigger"))
> return prompts
> --- `openkb/skill/evaluator.py`

> if save_flag and eval_set is None:
>     path = save_eval_set(kb_dir, name, result.prompts)
> --- `openkb/cli.py`

#### EPI-RTE-trigger-grade
Label: Description trigger grading
Endpoints: description/question to trigger-grader model, parsed verdict to deterministic expected-label comparison, aggregate metrics/misses to CLI. Model proposes verdict; code prioritizes NO-TRIGGER then TRIGGER substring and otherwise returns no-trigger. No runtime skill is executed. Distinct from [RT-RTE-skill-create](runtime.md#rt-rte-skill-create)'s creation/validation and from body support judgment; no identical supplied route after comparison. SRC-1, `openkb/skill/evaluator.py`, `openkb/cli.py` implementation. Check target/domain: whether description suggests loading for each labeled question. Expected-label oracle supplied by [EPI-RTE-eval-set](#epi-rte-eval-set); not factual answer truth. Mode: bounded evaluation, human chooses invocation/set, software reports, neither vetoes installation. Erroring tasks excluded from scoring. Concrete deduction: grader output “uncertain” becomes no-trigger and counts as passing for a no-trigger reference; this parser fallback is not evidence that the model correctly judged activation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Trigger/no-trigger verdict; run_eval accumulates misses or errors and CLI prints scores.
- Later read-back: inapplicable — CLI retains optional prompt sets, not automatic diagnostic-driven skill revisions.
- Delegated visibility: Each independent grader receives description only and one question, not body, references or execution trace.
- Selection predicate: All eval-set prompts; expected labels used for mismatch comparison.
- Invalidation or expiry: inapplicable — result is a diagnostic on the current read description, not persistent execution permission.
- Activation or effect: Verdicts change diagnostic counts/miss list; no automatic skill admission or successor selection consumer.
- Evidence limits: Label agreement and substring parsing do not measure achieved task outcomes or factual correctness.

> # Default: assume no-trigger on ambiguous output
> return "no-trigger"
> --- `openkb/skill/evaluator.py`

> if graded != prompt.expected:
>     result.misses.append(EvalMiss(prompt=prompt, graded=graded))
> --- `openkb/skill/evaluator.py`

#### EPI-RTE-body-grade
Label: Body support grading
Endpoints: current SKILL.md body plus reference prefixes and should-trigger question to coverage-grader model; parsed verdict/reason to aggregates, then CLI diagnostic. Check target/domain: judged availability of substantive textual material for that question, not correctness of an executed answer. SRC-1, `openkb/skill/evaluator.py`, `openkb/cli.py` implementation and prompt doctrine. Closest supplied [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) includes diagnostic mention but no separately individuated body checker; distinct from trigger checker and creation admission. Model judges, code parses UNSUPPORTED before SUPPORTED; ambiguous and exceptions are separated and excluded from coverage denominator. User chooses invocation; no per-verdict approval or automated skill rewrite/veto. Mode: bounded diagnostic; no independent answer-reference oracle. Each reference contributes at most 4000 Python text characters despite the constant/docstring saying bytes. Excerpts omit later content, so unsupported can reflect a preview limit. A supported verdict remains a model assertion, not proof of truth or successful task execution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: supported/unsupported/ambiguous plus reason; coverage metrics and gaps printed.
- Later read-back: inapplicable — no automated revised skill or verdict persistence consumer in the inspected CLI evaluator.
- Delegated visibility: Full extracted body, reference prefixes and single question, not trigger grader hidden reasoning or a skill execution.
- Selection predicate: Only EvalPrompt entries expected to trigger; reference Markdown recursively sorted and sliced per-file.
- Invalidation or expiry: inapplicable — current-file diagnostic, not an acceptance token reused by runtime.
- Activation or effect: Coverage verdict changes displayed rate/gap list; diagnostic only.
- Evidence limits: No run or outcome comparison; no facts outside supplied text assessed; denominator omits ambiguous/error judgments.

> if len(text) > REFERENCES_PREVIEW_BYTES:
>     text = text[:REFERENCES_PREVIEW_BYTES] + "\n…[truncated]\n"
> --- `openkb/skill/evaluator.py`

> "description claims to handle. Decide whether the body has "
> "substantive material to answer the question.\n\n"
> --- `openkb/skill/evaluator.py`

> coverage_prompts = [p for p in eval_set if p.expected == "trigger"]
> --- `openkb/skill/evaluator.py`

> scored = self.trigger_questions - len(self.coverage_ambiguous) - len(self.coverage_errors)
> return self.coverage_passed / scored if scored else 0.0
> --- `openkb/skill/evaluator.py`

### Claims

#### EPI-CLM-current-synthesis
Label: Current comprehensive synthesis

Claimed operation: accumulated wiki stays current, flags contradictions and reflects everything consumed. SRC-1, `README.md` doctrine/design. Distinct stronger coverage/warrant claim than [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki)'s basic compilation product claim. No source statement is treated as proof of quality.

> Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates. OpenKB compiles knowledge once into a persistent wiki, then keeps it current. Cross-references already exist, contradictions are flagged, and synthesis reflects everything consumed.
> --- `README.md`

#### EPI-CLM-grounded-answer
Label: Grounded cited answers

Claimed operation: produce grounded cited answers, rather than merely emit text after retrieval. SRC-1, `README.md` doctrine/design. Distinct output-warrant claim from [RT-CLM-compiled-wiki](runtime.md#rt-clm-compiled-wiki); no counterpart claim in supplied runtime after comparison.

> | <code>openkb&nbsp;query&nbsp;"question"</code>                                        | A grounded answer with citations (`--save` to persist to `wiki/explorations/`)                                 | [query & save](examples/commands/) |
> --- `README.md`

#### EPI-CLM-body-alignment
Label: Skill body alignment

Claimed operation: body-alignment evaluation tests whether skill can actually answer what it promises. SRC-1, `openkb/skill/evaluator.py` doctrine/design. Closest [RT-RTE-skill-create](runtime.md#rt-rte-skill-create) describes diagnostic admission limits but does not declare this claim; distinct from wiki product/trust claims.

> **Body alignment** — given the *full* SKILL.md (body + references), can
> the skill actually answer the should-trigger questions it claims to
> handle? This catches the failure mode where a well-written description
> promises capability that the body doesn't deliver — a hollow skill that
> would trigger but fail in practice.
> --- `openkb/skill/evaluator.py`
