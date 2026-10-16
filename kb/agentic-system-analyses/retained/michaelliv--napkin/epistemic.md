---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Napkin's routes from conversation and vault content to retained notes, agent answers, structural checks and benchmark scores."
run-id: AAS-2026-10-12-napkin-2b85bef38252-01
reviewed-boundary: "7582d6a46f5a11995956e60a59c41a5b242109f1"
---

# Napkin epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on Napkin's retained and delivered content, and what its checks actually authorize. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). Napkin is a file-based memory system with a CLI/SDK, packaged agent procedures and shipped benchmark callers, not the enclosing model runtime. All new findings below use SRC-1 at the frozen revision. Direct source reads establish implementation or doctrine/design, not exercised behavior. No target execution was performed.

The core can deliver and mutate truth-apt prose without judging it. Distill requests selection of established session knowledge and marked generalizations; tend requests conservative cleanup. Benchmarks instead import datasets directly, disable those skills, and evaluate external-agent answers. These are different authority paths, not one knowledge-admission loop. See [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault), and [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer).

The inspected claim surfaces include knowledge preservation, safe scheduled upkeep, external background distillation, benchmark performance, and overview keyword validation: [EPI-CLM-distill-knowledge](#epi-clm-distill-knowledge), [EPI-CLM-tend-safety](#epi-clm-tend-safety), [EPI-CLM-background-distill](#epi-clm-background-distill), [EPI-CLM-benchmark-results](#epi-clm-benchmark-results), and [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes). None licenses an unqualified system-wide truth guarantee.

### Coverage

| Entry point or operation | Source path | Inspection and covering records | Limit and conclusion prevented |
|---|---|---|---|
| CLI dispatch, task/property/template registration, stdout-copy hook | `src/main.ts` | Direct command-registration search across file; direct reads of property/task and template/config/hook sections | The hook captures stdout for clipboard use, not knowledge checking. Other wrappers are primarily supplied runtime findings, not independently re-audited here. |
| CLI/SDK overview, search, read and cache reuse | `src/core/search.ts`, `src/core/overview.ts`, `src/sdk.ts` | Supplied [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes) | Ranking/probe and freshness limits retained; no measured relevance or actual host reliance. |
| Create, append, overwrite, move, delete, configuration/scaffold/update | `src/core/crud.ts`, `src/core/init.ts`, `src/core/config.ts`, `src/commands/update.ts` | Supplied [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change) | No source-truth admission can be inferred from existing-file checks, installation success or tests. |
| Distill and tend | `skills/distill/SKILL.md`, `skills/tend/SKILL.md` | Both fully read directly; supplied skill routes plus claims below | Model compliance and actual semantic preservation unavailable. |
| Link diagnostics | `src/core/links.ts`, `src/utils/markdown.ts` | Both fully read directly; [EPI-RTE-link-check](#epi-rte-link-check) | Resolution checks are narrower than referential or propositional correctness. Resolver tie behavior supplied by runtime. |
| Frontmatter property edits | `src/core/properties.ts`, `src/utils/frontmatter.ts` | Both fully read directly; [EPI-RTE-property-edit](#epi-rte-property-edit) | Dependency serialization internals unavailable; setting a status is not an acceptance decision. |
| Template read/insert | `src/core/templates.ts` | Fully read directly; [EPI-RTE-template-insert](#epi-rte-template-insert) | Symbolic replacement is implemented; truth of resolved prose is not checked. |
| Bases query/create | `src/core/bases.ts`, `src/utils/bases.ts` | Core fully read; query/summary tail directly read; [EPI-RTE-base-summary](#epi-rte-base-summary) | Database population, filter translation and formula interpreter remain available but uninspected. No complete derivation or evaluator inventory for arbitrary bases. |
| Daily and task mutation | `src/core/daily.ts`, `src/core/tasks.ts` | Daily state path supplied by boundary; task update/parse tail directly read, CLI registration read | Task checkbox edits test syntax, not task accomplishment. Detailed daily template/date paths not re-audited; semantic content not determinable. |
| Canvas, bookmarks, tags, file metadata, graph, other template bodies | `src/core/canvas.ts`, `src/core/bookmarks.ts`, `src/main.ts`, `src/templates/` | Dispatch search identifies exposed operations; boundary/runtime supply selected state paths | Bodies not fully inspected here. Mixed prose/structural content and possible additional transformations remain unassessed. This prevents a system-complete negative about truth-apt routes. |
| LongMemEval ingestion/answer/check/report | `bench/longmemeval-eval.ts`, `bench/longmemeval-prompt.md` | Supplied [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer); judge, result and reporting ranges directly read | Dataset, result traces and external extension unavailable; scoring implementation is not observed accuracy. |
| LoCoMo and HotpotQA ingestion, answer extraction, scoring and cleanup | `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts` | Direct ingestion/scoring/answer-driver ranges; [EPI-RTE-dataset-import](#epi-rte-dataset-import), [EPI-RTE-answer-extract](#epi-rte-answer-extract), [EPI-RTE-token-score](#epi-rte-token-score) | Remaining sampling/aggregation paths not fully read; no dataset provenance audit or exercised evidence-dependence claim. |
| Background distillation | `docs/distill.md` | Fully read directly; [EPI-CLM-background-distill](#epi-clm-background-distill) | External implementation unavailable, as boundary states; timer, parser and direct writes remain doctrine only within this evidence boundary. |
| Provider state, legacy forwarding, build/release | `legacy/napkin-ai/cli.js`, `.github/workflows/release.yml`, `package.json` | Supplied boundary/runtime findings; [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model) | Exact weights, parameter changes, endpoint resolution, external package behavior and successful release remain uninspected. |

Missing run traces prevent conclusions about activated knowledge use, skill compliance, preserved meaning, learning benefit or exercised improvement. Missing datasets prevent independently checking the gold answers and imported summaries. Missing external host/extension sources prevent verifying unsolicited context injection, tool registration and scheduling. Available auxiliary bodies and base interpreter code not inspected are coverage limits, not access gaps or evidence of absence.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | Session-established claims, inferred generalizations, explanations and project context | see [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | SRC-1, `skills/distill/SKILL.md` | Actual accepted candidates and semantic lineage unavailable. |
| [EPI-OBJ-benchmark-notes](#epi-obj-benchmark-notes) | Imported dialogues, source paragraphs, supplied summaries/observations | see [EPI-OBJ-benchmark-notes](#epi-obj-benchmark-notes) | SRC-1, `bench/locomo-eval.ts` | Imported, not newly warranted by Napkin. |
| [RT-OBJ-vault-info](runtime.md#rt-obj-vault-info) | None: path/configuration identity | see [RT-OBJ-vault-info](runtime.md#rt-obj-vault-info) | SRC-1, `src/utils/vault.ts` | Configuration authority is not propositional warrant. |
| [EPI-OBJ-link-index](#epi-obj-link-index) | Syntactic links and bounded claims of resolvability/incoming-edge absence | see [EPI-OBJ-link-index](#epi-obj-link-index) | SRC-1, `src/core/links.ts` | No truth or referent-equivalence check. |
| [EPI-OBJ-answer-score](#epi-obj-answer-score) | External answer text, gold answer and resulting comparison metrics | see [EPI-OBJ-answer-score](#epi-obj-answer-score) | SRC-1, `bench/longmemeval-eval.ts` | Metric validity and gold truth independent of score calculation. |
| [EPI-OBJ-base-values](#epi-obj-base-values) | Query rows, symbolic formulas and numeric summaries | see [EPI-OBJ-base-values](#epi-obj-base-values) | SRC-1, `src/utils/bases.ts` | Narrow aggregate derivation assessed; broader encoding fidelity not determinable. |
| [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model) | Distributed-parametric state: individual propositions not determinable | see [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model) | SRC-1, `bench/longmemeval-eval.ts` | External weights and updates inaccessible; selector text is not the weights. |

## Authority-route ledger

Each row separates a consequential function even where the implementation container is shared. A `see` cell delegates fields to the cited declaration, rather than re-declaring them. No observed-run status is assigned.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | operational admission/selection/consumption | implemented | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | no content change | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | Ranking, delivery | No source-truth license | Caller receives selected text | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | SRC-1, `src/core/search.ts` | [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes) | Probe fallback | Delivery not compliance. |
| [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | lineage/freshness/recovery | implemented | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | no content change | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | Cache reuse/rebuild | Freshness proxy, not endorsement | Cached ranking may persist | see [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | SRC-1, `src/utils/fingerprint.ts` | none | Mtime is not content identity | Ranking/snippet states can differ. |
| [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | retention | implemented | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | truth-apt transformation: acquisition/import | see [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | see [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | see [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | see [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | Filesystem persistence/removal | External warrant unknown; core preserves supplied bytes in ordinary writes | Later calls can read changed notes | see [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) | SRC-1, `src/core/crud.ts` | none | Storage is not acceptance | Acquisition classification applies to content writes, not path-only moves/deletes. |
| [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | content transformation | doctrine only | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | truth-apt transformation: indeterminate | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | Model-facing request | Candidate generation; marker distinguishes claimed synthesis | Requests note rewrite/create | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1, `skills/distill/SKILL.md` | [EPI-CLM-distill-knowledge](#epi-clm-distill-knowledge) | none | Concrete input/output needed to distinguish reshaping, entailed derivation and non-entailed conjecture. |
| [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | disposition/acceptance | doctrine only | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | no content change | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | see [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) | KEEP/SKIP instruction | Usefulness/session-established gate; not recorded evidence-consuming acceptance of a produced ampliative claim | Retain or skip requested | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1, `skills/distill/SKILL.md` | [EPI-CLM-distill-knowledge](#epi-clm-distill-knowledge) | Knowledge label exceeds independently shown warrant | No candidate-specific decision record. |
| [EPI-RTE-link-check](#epi-rte-link-check) | check/evidence production | implemented | [EPI-OBJ-link-index](#epi-obj-link-index) | truth-apt transformation: entailed derivation | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | SRC-1, `src/core/links.ts` | none | Structural validity is not knowledge truth | Markdown-link coverage narrower than outgoing count. |
| [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | disposition/acceptance | doctrine only | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | no content change | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | Conservative agent policy | Usefulness, duplication and supersession judgments requested, not truth-certified | Merge/retire/skip; user controls schema proposal | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1, `skills/tend/SKILL.md` | [EPI-CLM-tend-safety](#epi-clm-tend-safety) | Safe scheduling not demonstrated | No reliable compliance evidence. |
| [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | content transformation | doctrine only | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | truth-apt transformation: indeterminate | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | see [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) | Model-facing integration request | Preservation intended, not established | Requests edits and link repair | see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) | SRC-1, `skills/tend/SKILL.md` | [EPI-CLM-tend-safety](#epi-clm-tend-safety) | none | Note integration is not lifecycle integration after evidenced acceptance. |
| [EPI-RTE-property-edit](#epi-rte-property-edit) | content transformation | implemented | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | truth-apt transformation: acquisition/import | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | see [EPI-RTE-property-edit](#epi-rte-property-edit) | SRC-1, `src/core/properties.ts` | none | Status label is not acceptance | Removal instead withdraws a field; policy-valued fields are non-truth-apt updates. |
| [EPI-RTE-template-insert](#epi-rte-template-insert) | content transformation | implemented | [EPI-OBJ-vault-prose](#epi-obj-vault-prose) | truth-apt transformation: acquisition/import | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | see [EPI-RTE-template-insert](#epi-rte-template-insert) | SRC-1, `src/core/templates.ts` | none | none | Import into target; interpretation of instantiated prose unverified. |
| [EPI-RTE-base-summary](#epi-rte-base-summary) | content transformation | implemented | [EPI-OBJ-base-values](#epi-obj-base-values) | truth-apt transformation: entailed derivation | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | see [EPI-RTE-base-summary](#epi-rte-base-summary) | SRC-1, `src/utils/bases.ts` | none | Numeric aggregate is not real-world verification | Bounded to numeric summary, not arbitrary formulas. |
| [EPI-RTE-dataset-import](#epi-rte-dataset-import) | retention | implemented | [EPI-OBJ-benchmark-notes](#epi-obj-benchmark-notes) | truth-apt transformation: acquisition/import | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | see [EPI-RTE-dataset-import](#epi-rte-dataset-import) | SRC-1, `bench/locomo-eval.ts` | none | Import is not produced knowledge | Warrant unknown; formatting preserves supplied content but title sanitation can collide. |
| [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) | content transformation | implemented | [EPI-OBJ-answer-score](#epi-obj-answer-score) | truth-apt transformation: indeterminate | see [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) | see [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) | see [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) | see [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) | External model request | Answers are candidates; derivation not shown | Driver continues to scoring | see [RT-BAP-benchmark-evidence](runtime.md#rt-bap-benchmark-evidence) | SRC-1, `bench/longmemeval-eval.ts` | [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | none | Implemented request does not establish model reasoning. |
| [EPI-RTE-answer-extract](#epi-rte-answer-extract) | content transformation | implemented | [EPI-OBJ-answer-score](#epi-obj-answer-score) | truth-apt transformation: indeterminate | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | see [EPI-RTE-answer-extract](#epi-rte-answer-extract) | SRC-1, `bench/hotpotqa-eval.ts` | none | Gold-conditioned truncation | Can remove qualifications; scored string is not necessarily full answer. |
| [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | check/evidence production | implemented | [EPI-OBJ-answer-score](#epi-obj-answer-score) | no content change | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | see [EPI-RTE-longmem-judge](#epi-rte-longmem-judge) | SRC-1, `bench/longmemeval-eval.ts` | [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | Substring fast path | Full-credit counterexample below; result is rubric/heuristic bounded. |
| [EPI-RTE-token-score](#epi-rte-token-score) | check/evidence production | implemented | [EPI-OBJ-answer-score](#epi-obj-answer-score) | no content change | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | see [EPI-RTE-token-score](#epi-rte-token-score) | SRC-1, `bench/locomo-eval.ts` | none | Overlap is not semantic correctness | Word order and negation can invalidate semantic reading. |
| [EPI-RTE-score-report](#epi-rte-score-report) | operational admission/selection/consumption | implemented | [EPI-OBJ-answer-score](#epi-obj-answer-score) | no content change | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | see [EPI-RTE-score-report](#epi-rte-score-report) | SRC-1, `bench/longmemeval-eval.ts` | [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | Report is not knowledge admission | No inspected score-to-note revision consumer. |

The external background route has architectural status `doctrine only`, not the status of a shipped timer: see [EPI-CLM-background-distill](#epi-clm-background-distill). No separate route record is declared because the executable endpoints cannot be inspected within the frozen source. Its documentation does not supply a checked acceptance criterion; the example's `status: accepted` is merely generated text.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-distill-knowledge](#epi-clm-distill-knowledge) | see [EPI-CLM-distill-knowledge](#epi-clm-distill-knowledge) | SRC-1, `skills/distill/SKILL.md`; doctrine/design | see claim | [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [EPI-RTE-link-check](#epi-rte-link-check) execute writes/diagnostics, not the model's content decisions | None supplied | No causal evidence; no concrete session-to-note pair | Retention gate and synthesis marking requested | Produced accepted ampliative knowledge not established. |
| [EPI-CLM-tend-safety](#epi-clm-tend-safety) | see [EPI-CLM-tend-safety](#epi-clm-tend-safety) | SRC-1, `skills/tend/SKILL.md`; doctrine/design | see claim | [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [EPI-RTE-link-check](#epi-rte-link-check) | None supplied | No measured loss/recovery; overwrite lacks archive; permanent deletion remains exposed | Conservative defaults, bounded task and trash policy exist | Reliable safe scheduled operation unverified. |
| [EPI-CLM-background-distill](#epi-clm-background-distill) | see [EPI-CLM-background-distill](#epi-clm-background-distill) | SRC-1, `docs/distill.md`; doctrine/design | see claim | None for timer/model/parser; only generic I/O available | None supplied | External implementation unavailable | Declared host integration, not a core scheduler | Cannot attribute autonomous extraction or accepted status to inspected implementation. |
| [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | see [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | SRC-1, `README.md`; reported operation | see claim | [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), [EPI-RTE-longmem-judge](#epi-rte-longmem-judge), [EPI-RTE-score-report](#epi-rte-score-report) | None supplied | Scores and comparisons reported, not reconstructed traces or interventions; same model selector for answer/judge | Shipped evaluator with bounded scoring semantics | Headline accuracy not independently verified; component benefit not causally identified. |
| [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes) | see [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes) | SRC-1, `src/main.ts`; doctrine/design | see claim | [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) | None supplied | Probe tests retrieval placement, not knowledge truth; fallback exceptions | Best-effort search handles | Universal validation unsupported by implementation. |

## Bounded conclusion

**Retention and delivery have operational authority, not automatic truth authority.** Caller I/O persists supplied notes; ranking delivers selected notes and snippets; subsequent callers may rely on them. Existing-file rejection and cache fingerprints concern replacement and freshness. They neither endorse content nor track warranted provenance. Generic caller authorship remains unresolved. These implemented paths need no model, while the model-dependent admission procedures remain requests to an external host ([RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval)).

**The skills request curation with epistemic distinctions but do not establish accepted ampliative production.** Distill distinguishes established claims from inferred generalizations, names usefulness over a three-month horizon, requests explicit contradiction handling and allows SKIP. Tend reads before merging and can veto by doing nothing. Their intended use is future session knowledge and conservative upkeep. Their force is advisory/policy through external model interpretation during the invocation, then possible durable note influence. No supplied candidate-level evidence-consuming acceptance decision demonstrates that an inferred proposition was tested and accepted for that use. A model merge is semantic integration in the everyday sense, not evidence of lifecycle integration after acceptance. Link verification checks a different target ([RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault), [EPI-RTE-link-check](#epi-rte-link-check)).

**The core also exposes smaller material routes that bypass the skills.** Frontmatter status edits and template insertion can alter what later readers interpret as authority without a truth criterion. Task updates validate that a line is a checkbox and replace its status character; they do not check completion in the world (SRC-1, `src/core/tasks.ts`). Base numeric aggregation derives a result within an explicit computational domain: `Sum` over finite values 2 and 3 gives 5 by numeric conversion/filter/reduce. This licenses the arithmetic result conditional on those inputs, not the source facts or arbitrary base formulas ([EPI-RTE-property-edit](#epi-rte-property-edit), [EPI-RTE-template-insert](#epi-rte-template-insert), [EPI-RTE-base-summary](#epi-rte-base-summary)).

**Benchmark scoring changes reports, not retained knowledge acceptance.** LongMemEval's check consumes an external answer and gold text; substring matches can grant full credit before its model judge, whose temporal rubric tolerates off-by-one answers. Failure falls back to continuous token F1 despite a binary return description. LoCoMo and HotpotQA score a potentially gold-conditioned, truncated answer using lexical overlap. Imported summaries are supplied dataset content, not Napkin-produced abstractions. The benchmark consumer retains/report scores; inspected question paths do not use them to revise notes, change policy or admit answers into a lasting knowledge ledger. Temporary-vault cleanup ends the inspected LongMemEval/HotpotQA horizon; LoCoMo cleanup is visible in the source search at its sample driver, not independently audited for every failure path ([EPI-RTE-dataset-import](#epi-rte-dataset-import), [EPI-RTE-answer-extract](#epi-rte-answer-extract), [EPI-RTE-longmem-judge](#epi-rte-longmem-judge), [EPI-RTE-token-score](#epi-rte-token-score), [EPI-RTE-score-report](#epi-rte-score-report)).

A claimed correct outcome would not establish the reasoning process, faithful retrieval, component effect, transfer or replay safety. Parameters, exact weights and endpoint resolution retain the limits in [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model). No learning benefit, activated reflection, autonomous theory-building or exercised self-improvement follows from storage and scores alone. This does not negate their possible independent existence in uninspected host behavior. Auxiliary operations and the base formula interpreter remain unassessed; therefore the report does not conclude that no other truth-apt derivation, evaluator or adaptation route exists anywhere in the whole shipped system.

## Shared records

### Operative objects

#### EPI-OBJ-vault-prose
Label: Vault knowledge and context prose

Source-native identity: Markdown notes and `NAPKIN.md` named by the skills. Representational form: natural-language claims and explanations interpreted by later humans/models; frontmatter additionally supplies symbolic fields to program consumers. Storage substrate: vault files. Claimed role: lasting session knowledge and project orientation. No counterpart operative object in the supplied runtime after comparison with [RT-OBJ-vault-info](runtime.md#rt-obj-vault-info), which represents paths/configuration, not content. Routes touching this object are [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) and [RT-RTE-distill-session](runtime.md#rt-rte-distill-session). Evidence: SRC-1, `skills/distill/SKILL.md`; established and inferred content are not identical warrant classes.

> **Mark synthesis.** A claim the session actually established needs no marker.
>   A generalization you are drawing gets a trailing `^[inferred]`.
> --- `skills/distill/SKILL.md`

#### EPI-OBJ-benchmark-notes
Label: Imported benchmark notes

Source-native identity: LoCoMo session notes, HotpotQA paragraph notes, and the conversational round notes in the supplied LongMemEval route. Natural-language content is stored as Markdown; titles, dates and links also serve symbolic selection. Unlike [EPI-OBJ-vault-prose](#epi-obj-vault-prose), these instances are constructed by dataset drivers without distill admission. No supplied operative-object counterpart; [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) contains the LongMemEval usage, not this object declaration. Evidence: SRC-1, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`; LoCoMo summary and observation origin is the supplied sample, not an inspected generation process.

> const summary = sample.session_summary?.[`session_${num}_summary`] ?? "";
>     const observations = sample.observation?.[`session_${num}_observation`] ?? [];
> --- `bench/locomo-eval.ts`

#### EPI-OBJ-link-index
Label: Link index diagnostics

Source-native identity: `VaultLinks` maps `outgoing`, `incoming`, `unresolved`. Representational form: symbolic path lists/maps. Storage substrate: current process memory reconstructed from Markdown. Claimed role: structural evidence used by upkeep. No supplied object counterpart; distinct from content or cached search, although [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) consumes these diagnostics. Evidence: SRC-1, `src/core/links.ts`.

> return { outgoing, incoming, unresolved };
> --- `src/core/links.ts`

#### EPI-OBJ-answer-score
Label: Answer and score parts

Source-native identity: `agentAnswer`, gold `answer`, `accuracy`/`ansF1` in benchmark results. Natural-language answer/gold text is interpreted by the judge; numeric metrics are symbolic values consumed by reporting. Storage substrate: subprocess output/current process result objects and optional result logs/JSON. These parts differ from imported source notes in their producer/checker/consumer. No supplied object counterpart; [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) is a container for the LongMemEval operations. Evidence: SRC-1, `bench/longmemeval-eval.ts`, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`.

> accuracy: answerF1,
> --- `bench/longmemeval-eval.ts`

#### EPI-OBJ-base-values
Label: Base rows and summaries

Source-native identity: `BaseQueryResult` rows, columns, groups, summaries. Representational form: symbolic values and expressions; prose in source rows can retain a natural-language consumption path. Storage substrate: temporary query database and process-returned data; input configuration comes from a `.base` file. No counterpart after comparison with [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), which covers overview/search/read rather than base query derivation. Evidence: SRC-1, `src/core/bases.ts`, `src/utils/bases.ts`.

> summaries: computeViewSummaries(view, columns, rows, baseConfig),
> --- `src/utils/bases.ts`

### Routes

#### EPI-RTE-link-check
Label: Structural link check

External caller invokes diagnostics; core reads Markdown, extracts links, resolves wikilink targets and returns unresolved/incoming/outgoing maps. Owner: program for extraction/resolution, external agent for interpreting diagnostics. Check target/domain: extracted wikilink targets against listed Markdown files, not real-world claims or heading correctness. Markdown outgoing links are extracted but the unresolved/incoming loop traverses only `wikilinks`. Orphan means zero incoming resolved wikilinks, not no semantic relevance. Strict file-reference resolution differs from loose index resolution supplied by [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval). This route is a distinct diagnostic, not another retrieval container; no counterpart after comparison with that route and [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault).

Force/license: deterministic structural report only. Consumer/channel/horizon: caller gets returned lists; skill agent is instructed to use them before/after edits during current upkeep and distillation. No core write block is attached to a failed diagnostic. Concrete implementation deduction: `[[Missing#Section]]` is reduced to `Missing`; if no resolver match exists it enters unresolved; an ordinary `[x](Missing.md)` contributes outgoing but not the wikilink unresolved loop. This checks resolvability within parser/resolver semantics, not referential correctness. Evidence: SRC-1, `src/core/links.ts`, `src/utils/markdown.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sorted unresolved pairs, orphan/deadend lists or backlink/outgoing lists.
- Later read-back: inapplicable — no diagnostic result is persisted by these functions.
- Delegated visibility: Caller receives structural evidence; packaged skills request interpretation.
- Selection predicate: Listed Markdown and regex-extracted links; incoming edges require wikilink resolution.
- Invalidation or expiry: Reconstructed on call; no persisted acceptance or expiry.
- Activation or effect: Structural calculation wired; resulting semantic edits and reliable compliance uninspected.
- Evidence limits: Dependency/filesystem behavior and observed diagnostic-to-edit outcomes unavailable; heading/block reference is stripped rather than validated.

> for (const target of links.wikilinks) {
>       const resolved = resolve(target);
>       if (resolved) append(incoming, resolved, file);
>       else append(unresolved, target, file);
>     }
> --- `src/core/links.ts`

> const clean = target.split("#")[0].trim();
> --- `src/utils/markdown.ts`

#### EPI-RTE-property-edit
Label: Caller frontmatter edit

Caller selects target/key/value; core resolves file, coerces true/false/numeric strings, parses and serializes frontmatter, then writes. This is a distinct exposed metadata admission mechanism not declared by [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation)'s CRUD trace. Human/software proposal and decision cannot be separated from a generic caller; no per-content approval or answer oracle. Operating mode: open caller edits. Missing file or parsing failure can reject; overwrite of a property does not evaluate its truth. Rollback requires caller rewriting old values; none automatically archived. A `status=accepted` value can be retained with no evidence-consuming acceptance decision. Warrant of imported value is unknown; non-truth-apt configuration/status policies receive operational labels, not truth validation. Consumer/channel/force/horizon: later field readers and natural-language consumers receive changed file data; local write is enforcing, later reliance external. Evidence: SRC-1, `src/core/properties.ts`, `src/utils/frontmatter.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Path/property/value or removed-key result.
- Later read-back: Changed fields are read by later `readProperty` or whole-note calls.
- Delegated visibility: Current caller gets status; later vault readers see changed metadata/prose.
- Selection predicate: Caller file reference, property name/value; strict resolution and parse success.
- Invalidation or expiry: Caller replacement/removal; no semantic expiry or acceptance revocation protocol.
- Activation or effect: File rewrite wired; altered trust or behavior from metadata unobserved.
- Evidence limits: Serializer/parser dependency internals unavailable; caller identity and value truth uninspected.

> const updated = setProp(content, name, parsedValue);
>   fs.writeFileSync(fullPath, updated);
> --- `src/core/properties.ts`

> const data = { ...result.data, [name]: value };
>   return matter.stringify(result.content, data);
> --- `src/utils/frontmatter.ts`

#### EPI-RTE-template-insert
Label: Resolved template insertion

Caller chooses a stored template and target; program resolves both, substitutes local date/time/target basename and appends template content. Distinct from registry/scaffolding in [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change); overlaps template-assisted creation in [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) but is an independent exposed insert path. Check target: template/target existence, not template truth. Open caller request; caller proposes/decides, missing-file errors veto; no oracle or semantic reviewer; recovery is manual rewrite. Symbolic substitution can instantiate policy or truth-apt text, but is not evidence-consuming knowledge acceptance. For a concrete input `# {{title}}` with target basename `Decision`, inspected replacement produces `# Decision`; insertion concatenates it to existing bytes without a new separator. Date/time use local clock, not a historical event check. Consumer/channel/force/horizon: immediate caller receives content/status; persisted target reaches later readers; write enforcing, truth authority unknown. Evidence: SRC-1, `src/core/templates.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Resolved template content or file/template/inserted status.
- Later read-back: Inserted bytes persist in the target for later reads.
- Delegated visibility: Caller and later file consumers receive instantiated text.
- Selection predicate: Caller template name and target; strict resolution; substitutions match literal variable tokens.
- Invalidation or expiry: Manual later edits; no semantic expiry.
- Activation or effect: Substitution and append wired; downstream behavior or truth uninspected.
- Evidence limits: Actual templates/targets used in a run absent; semantic preservation cannot be generalized from token replacement.

> .replace(/\{\{title\}\}/g, title || "Untitled");
> --- `src/core/templates.ts`

> fs.writeFileSync(targetPath, existing + templateContent);
> --- `src/core/templates.ts`

#### EPI-RTE-base-summary
Label: Numeric base summary

Program returns aggregates over query rows under caller-selected base/view configuration. Distinct from overview/search/read in [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval); no supplied counterpart. Target/domain: numeric aggregates after JavaScript `Number` conversion and NaN filtering, not the truth of source properties. For finite input values 2 and 3 and `Sum`, conversion preserves them and reduction from 0 gives 5. This is entailed arithmetic conditional on the inputs and implementation interpretation. It is not a separate truth evaluator, acceptance criterion or novel ampliative claim. Operational authority: returned summary, not a core update. Consumer/channel/force/horizon: SDK/CLI caller gets symbolic returned values, advisory for current query; later use is external. Custom summaries have only built-in fallback in the inspected function. Broader formula processing is present but not fully inspected. Evidence: SRC-1, `src/core/bases.ts`, `src/utils/bases.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query rows/columns/groups/summaries or query error.
- Later read-back: inapplicable — this query path returns results without persisting them.
- Delegated visibility: Returned aggregate reaches caller; no verified model reliance.
- Selection predicate: Selected base/view plus query row set and configured summary function.
- Invalidation or expiry: inapplicable — temporary database closes after query; no retained result expiry.
- Activation or effect: Numeric computation/return wired; changed downstream decisions unobserved.
- Evidence limits: Population/filter/formula paths uninspected, dependency internals unavailable; no source-premise truth or domain-transfer license.

> const nums = values.map(Number).filter((n) => !Number.isNaN(n));
> --- `src/utils/bases.ts`

> Sum: (nums) => nums.reduce((a, b) => a + b, 0),
> --- `src/utils/bases.ts`

#### EPI-RTE-dataset-import
Label: LoCoMo and HotpotQA import

Shipped drivers deterministically create temporary vaults from dataset records. LoCoMo stores session dialogue plus supplied summary/observations, date and adjacency links. HotpotQA joins supplied sentences, writes original titles in headings and sanitized titles in filenames, and adds links by title substring occurrence. Distinct from skill retention and [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)'s LongMemEval instance; no duplicate source/object claim. Proposal/content: external dataset; admission: driver loops without semantic review or per-note human approval; no answer oracle at import, though gold data later evaluates answers. Mode: bounded benchmark. Rejection skips missing/empty LoCoMo sessions; filesystem failure can abort. There is no content-level acceptance gate. Recovery is temporary-vault cleanup, not rollback to a prior knowledge version. Source warrant remains unknown: provenance labels and dialogues are retained, but no independent checking of those records occurs here. Sanitized-title collision can overwrite a HotpotQA note; sentence joining and link heuristics do not validate paragraph truth. Consumer/channel/force/horizon: question agent is requested to search/read these files; program writes enforce retention during the temporary-vault lifetime. Evidence: SRC-1, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Temporary directory and, for LoCoMo, session-title list.
- Later read-back: Subsequent question subprocess retrieves previously written notes; LoCoMo can reuse sample notes for several questions.
- Delegated visibility: External question agent receives vault path and command-use prompts; extension injection uninspected.
- Selection predicate: Nonempty LoCoMo session arrays; HotpotQA supplied context entries; summaries/observations conditional on presence.
- Invalidation or expiry: HotpotQA removes vault in question finally; LoCoMo sample-driver removal found by source search, not fully audited for failure coverage.
- Activation or effect: Dataset file writes and subprocess requests wired; actual reads/reliance unobserved.
- Evidence limits: No datasets, source-generation history or run traces; formatting and storage do not warrant imported propositions.

> content += `## Dialogue\n${bodyLines.join("\n")}\n`;
> --- `bench/locomo-eval.ts`

> const body = sentences.join(" ");
> --- `bench/hotpotqa-eval.ts`

> return title.replace(/[<>:"/\\|?*]/g, "_");
> --- `bench/hotpotqa-eval.ts`

#### EPI-RTE-answer-extract
Label: Gold-conditioned answer extraction

LoCoMo/HotpotQA driver transforms external assistant text before token scoring. The program chooses `ANSWER:` capture or last line; if the gold answer has at most three words and extracted answer exceeds five times its character length, it takes the first comma/period clause. This is a distinct part of the two question drivers, not part of supplied LongMemEval [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer). Criterion is string shape and gold length, not semantic correctness. Deterministic trace: gold `yes`, input `ANSWER: yes, but only if permitted` yields capture longer than 15 characters, then first clause `yes`. A qualification disappears; thus semantic preservation cannot be guaranteed. Gold text is not copied to the answer, but evaluation preprocessing is gold-conditioned. Owner: driver; consumer/channel/force/horizon: token scorer receives substituted answer string, enforcing preprocessing for one question. No content acceptance or lasting note change. Evidence: SRC-1, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extracted or truncated answer string.
- Later read-back: inapplicable — transformation itself retains nothing; result may enter benchmark logs, not future answering.
- Delegated visibility: Scorer and result object receive transformed answer, not necessarily full assistant text.
- Selection predicate: ANSWER regex, final line fallback, gold word/character-length conditions.
- Invalidation or expiry: inapplicable — current-question transformation, not retained knowledge.
- Activation or effect: Preprocessing wired; changed semantic interpretation possible by code trace, not observed in a run.
- Evidence limits: No actual answer/gold trace; concrete deduction concerns the implementation domain only.

> if (goldAnswer.split(/\s+/).length <= 3 && answer.length > goldAnswer.length * 5) {
>     const short = answer.split(/[,.]/, 1)[0].trim();
>     if (short.length > 0) answer = short;
>   }
> --- `bench/hotpotqa-eval.ts`

#### EPI-RTE-longmem-judge
Label: LongMemEval answer check
Part of: [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

This isolates the checking function inside the supplied benchmark container. Target: current answer relative to dataset gold/primary answer and question-selected rubric, not retained note truth, reasoning fidelity or retrieval causality. Driver proposes the check inputs and decides numeric result. First normalized exact/substrings; otherwise external pi-selected model judges yes/no, with preference/abstention/temporal/general prompts; on subprocess failure, token F1. Human contribution is dataset reference and driver design, not per-question approval. Oracle: dataset answer; provider model is judge, not an independent truth oracle. Mode: bounded benchmark; no improvement trigger or knowledge-change admission.

Counterexample to interpreting full credit as semantic correctness: gold `Paris`, prediction `not Paris` normalize to `paris` and `not paris`; nonempty primary occurs in prediction, so return 1 before model judging. Conversely prediction `New` and gold `New York` can receive 1 via reverse substring. These implementation deductions require no execution. Temporal judge permits off-by-one errors; fallback is continuous overlap despite the binary function comment. None of these tests establishes source truth or explanatory mechanism. Epistemic license is only the selected heuristic/rubric result. Consumer: reporting route below; channel numeric `accuracy`; force labels benchmark result, not operational note admission; horizon current question and run report. Evidence: SRC-1, `bench/longmemeval-eval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: 1/0 from matching or model response; continuous token F1 on judge failure.
- Later read-back: inapplicable — checker does not persist; reporting retains the numeric result separately.
- Delegated visibility: External judge receives question/gold/prediction; caller receives number.
- Selection predicate: Exact/substrings precede gold/question-text-selected rubric; judge output first yes/no word or fallback rule.
- Invalidation or expiry: inapplicable — per-question evaluation without acceptance revocation state.
- Activation or effect: Check request and number computation wired; actual judge operation unavailable.
- Evidence limits: Gold truth, model reliability, actual traces and causal component effect uninspected; same model selector for answer/judge is not independent adjudication.

> if (normPred === normGold || normPred === normPrimary) return 1;
>   if (normPrimary.length > 0 && normPred.includes(normPrimary)) return 1;
>   if (normPred.length > 0 && normPrimary.includes(normPred)) return 1;
> --- `bench/longmemeval-eval.ts`

> return tokenF1Basic(prediction, primaryAnswer);
> --- `bench/longmemeval-eval.ts`

#### EPI-RTE-token-score
Label: LoCoMo and HotpotQA token check

Distinct from [EPI-RTE-longmem-judge](#epi-rte-longmem-judge): these two drivers use token overlap without the model judge/substrings; their core formula matches LongMemEval's fallback. Target/domain: transformed answer token membership relative to dataset reference after article/punctuation/case normalization. Dataset supplies expected answer and evidence IDs/titles; program derives answer F1 and retrieval proxies. Driver decides scores, no human veto per answer, open model request inside bounded benchmark. Retrieval proxies detect note strings in combined answer/tool argument/tool result text, not verified complete reads. The model is not oracle here. Concrete token trace: `Alice likes Bob` versus `Bob likes Alice` produces identical sets and precision/recall 1, although the propositions differ. This licenses overlap only, not semantic correctness or causal evidence dependence. Consumer/channel/force/horizon: per-question result numeric fields used by benchmark reporting, advisory to result readers; no score-directed note revisions in inspected drivers. Evidence: SRC-1, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numeric answer/retrieval metrics in result object; missing evidence can exclude a question.
- Later read-back: uninspected — remaining aggregate/report paths not fully audited; no inspected later answer use of scores.
- Delegated visibility: Driver/report reader receives metrics; string-proxy extraction does not establish actual read completeness.
- Selection predicate: Normalized token sets and evidence mapped to sessions/sanitized titles; extracted assistant answer.
- Invalidation or expiry: inapplicable — no persistent truth-acceptance state; current-question scores.
- Activation or effect: Metric computation wired; accuracy and retrieval-benefit claims unobserved.
- Evidence limits: Gold truth, actual answer traces and score calibration unavailable; word order and repeated-token handling differ from semantic checking.

> const rs = new Set(r), ps = new Set(p);
>   const prec = p.filter((t) => rs.has(t)).length / p.length;
>   const rec = r.filter((t) => ps.has(t)).length / r.length;
> --- `bench/locomo-eval.ts`

> ansF1: tokenF1(agentAnswer, q.answer),
> --- `bench/hotpotqa-eval.ts`

#### EPI-RTE-score-report
Label: LongMemEval score reporting
Part of: [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

Distinct consequential consumer of [EPI-RTE-longmem-judge](#epi-rte-longmem-judge), not another checker. Driver attaches result as `accuracy`, aggregates means/confidence intervals and publishes console/log/optional JSON output. Owner is driver; the report reader decides later interpretation. No admission of checked answer into knowledge is implemented by this reporting path. Numeric score is the operative result because it changes displayed/stored performance values; it does not choose a note rewrite, weight update or policy successor in the inspected path. Possible failure returns null from question and removes temporary vault, rather than accepting content or recording a truth rejection. Consumer/channel/force/horizon: aggregate routine and console/log/JSON, enforcing report field assignment and advisory to operator, current run plus durable report artifact. Evidence: SRC-1, `bench/longmemeval-eval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Question result, console summaries, log summary and optional result JSON.
- Later read-back: Stored report can be read later; no inspected automatic read-back into question answering or note admission.
- Delegated visibility: Console/log/JSON readers receive results, model selector, dataset and configured sampling fields.
- Selection predicate: Completed non-null question results and per-ability grouping; JSON option controls extra result artifact.
- Invalidation or expiry: Timestamped result naming; temporary vault cleanup is separate; no epistemic revocation protocol.
- Activation or effect: Score-to-report assignments wired; published results from an actual run unavailable.
- Evidence limits: Aggregation implementation does not authenticate runs or establish causal benefit; comparison table contains historical constants, not controlled contemporaneous comparisons.

> overall: { sessionRecall: avg(allResults, "sessionRecall"), sessionF1: avg(allResults, "sessionF1"), accuracy: avg(allResults, "accuracy"), accuracyCI },
> --- `bench/longmemeval-eval.ts`

> try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch {}
> --- `bench/longmemeval-eval.ts`

### Claims

#### EPI-CLM-distill-knowledge
Label: Distill session knowledge

Claimed operation: preserve knowledge itself, not conversational minutes; retain investigated fixes, confirmed non-obvious behavior, reasoned decisions and reusable patterns, marking drawn generalizations. Doctrine/design, SRC-1, `skills/distill/SKILL.md`. Distinct from [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes); closest supplied route [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) describes the procedure, not this public knowledge claim. It supplies future-use gating and model interpretation, not a demonstrated candidate acceptance record.

> You are preserving knowledge from this session into a napkin vault. Write the
> knowledge itself, not a record of the conversation.
> --- `skills/distill/SKILL.md`

#### EPI-CLM-tend-safety
Label: Safe scheduled upkeep

Claimed operation/warrant: conservative default makes upkeep safe to schedule. Doctrine/design, SRC-1, `skills/tend/SKILL.md`. Distinct claim, no counterpart after comparison with [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes); related supplied [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault) states the procedure. Policies reduce intended scope but are not filesystem enforcement or demonstrated safe behavior.

> This skill is safe to run on a schedule precisely because its
> default answer is "nothing needs doing."
> --- `skills/tend/SKILL.md`

#### EPI-CLM-background-distill
Label: Automatic background distillation

Claimed operation: external pi timer reads new session messages, calls a model with context/templates, skips `NO_DISTILL` or parses notes and writes them directly. Doctrine/design, SRC-1, `docs/distill.md`. No counterpart claim in supplied runtime; distinct from [RT-RTE-distill-session](runtime.md#rt-rte-distill-session)'s shipped skill procedure. Boundary states external extension unavailable; the document explicitly locates intelligence outside the core. Example `status: accepted` has no named evidence-consuming acceptance check. Scheduler/model/parser behavior and distributed-parametric state cannot be assessed from this text alone.

> Each note is written directly to the vault at the specified path.
> --- `docs/distill.md`

> **Lives in pi** — it's a pi extension, not a napkin feature
> --- `docs/distill.md`

#### EPI-CLM-benchmark-results
Label: Headline benchmark accuracy

Claimed operation/warrant: README reports high LongMemEval benchmark performance for pi plus Napkin and describes zero preprocessing/BM25 Markdown retrieval. Evidence layer: reported operation, SRC-1, `README.md`; no raw trace/result source is available. Distinct from [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes); [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) supports implemented evaluation, not reproduction. The no-summaries statement is adjacent to LongMemEval results, not a universal description of all shipped benchmarks: LoCoMo imports supplied summaries. The no-graphs phrasing does not remove hyperlink/backlink features from retrieval. No unsupported whole-system preprocessing negative is inferred.

> | Oracle | 1-6 | **92.0%** | 92.4% | 92.4% |
> | S | ~40 | **91.0%** | 86% | 64% |
> | M | ~500 | **83.0%** | 72% | n/a |
> --- `README.md`

> Zero preprocessing. No embeddings, no graphs, no summaries. Just BM25 search on markdown files.
> --- `README.md`
