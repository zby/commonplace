---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM Wiki v2 epistemic routes: source fidelity, semantic guards, retrieval authority and maintenance evaluation."
run-id: AAS-2026-11-08-llm-wiki-v2-5abff9a6c5c3-01
reviewed-boundary: "e0a205afe60bd1913d083a3ed4cdab81e38e4c26"
---

# LLM Wiki v2 epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on the notes and answers of LLM Wiki v2, rather than equating their storage with acceptance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identity: see its [Source register](boundary.md#source-register). All added inspection is SRC-1 at the same frozen commit. External model internals, MCP host behavior and private corpora remain outside that boundary.

The system requests source-faithful, complete and discoverable notes ([RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation)) and source-only answers ([EPI-CLM-source-answers](#epi-clm-source-answers)). Inspected implementation supports acquisition, model-mediated rewriting, heuristic checks, operational filing and later use. Semantic preservation of generated text is indeterminate without comparing a particular input/output; non-entailment is not inferred just because models are used. No execution or causal experiment is supplied. Parameter learning and provider truth evaluation cannot be assessed beyond [RT-CMP-llm](runtime.md#rt-cmp-llm) and [RT-CMP-classifier](runtime.md#rt-cmp-classifier).

Coverage distinguishes direct reads/searches here from supplied runtime evidence. These are selected material routes, not an exhaustive correctness audit.

| Entry point / operation | Source path (SRC-1) | Evidence and coverage |
|---|---|---|
| CLI dispatch, audit/health/check | `src/llmw2/cli.py` | Direct dispatch search and audit/health/check branch read; [EPI-RTE-route-audit](#epi-rte-route-audit), [EPI-RTE-audit-apply](#epi-rte-audit-apply), [EPI-RTE-health-check](#epi-rte-health-check), [EPI-RTE-bundle-check](#epi-rte-bundle-check) |
| Ingest/upload/ask, sync, batch, plan/split | `src/llmw2/wiki.py`, `src/llmw2/server.py`, `src/llmw2/sources/sync.py` | Supplied [RT-RTE-source-filing](runtime.md#rt-rte-source-filing), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-batch-sync](runtime.md#rt-rte-batch-sync); HTTP operation search directly checks exposed surface |
| MCP recall/remember/rebuild/reply/read_note and areas | `src/llmw2/memory.py` | Direct registered-tool search, supplied [RT-RTE-client-relay](runtime.md#rt-rte-client-relay), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [RT-BAP-client-instructions](runtime.md#rt-bap-client-instructions); direct reads do not require relevance selection |
| Structural step checks and merge guards | `src/llmw2/agents/steps.py`, `src/llmw2/agents/steps_classic.py` | Direct check and merge implementation reads; [EPI-RTE-step-check](#epi-rte-step-check), [EPI-RTE-merge-guard](#epi-rte-merge-guard), [EPI-RTE-guard-choice](#epi-rte-guard-choice) |
| Replace/archive and kept sentences | `src/llmw2/agents/revisions.py` | Direct complete read; [EPI-RTE-revision-check](#epi-rte-revision-check), [EPI-RTE-revision-admit](#epi-rte-revision-admit) |
| History, conflicts, raw rows, citations | `src/llmw2/agents/researcher.py`, `src/llmw2/agents/conflicts.py` | Direct ask/expansion read and complete conflicts read; [EPI-RTE-conflict-check](#epi-rte-conflict-check), [EPI-RTE-conflict-hint](#epi-rte-conflict-hint); remaining selection supplied by [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) |
| Deletion, purge, raw rebuild, manual organization | `src/llmw2/wiki.py` | Direct purge/raw-items read; [EPI-RTE-origin-purge](#epi-rte-origin-purge); other paths supplied by [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) |
| Prompt/model/step changes | `src/llmw2/agents/prompts.py`, `src/llmw2/server.py` | Supplied [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration); no automated semantic approval implied |
| Bundle lint / taxonomy metrics | `src/llmw2/bundle/check.py`, `src/llmw2/audit.py` | Direct complete reads; diagnostic results are not source-truth verdicts |
| Offline factual scoring | `benchmarks/note_facts.py` | Direct normalization, matching and metrics read; [EPI-RTE-fact-score](#epi-rte-fact-score) |
| Other offline evaluations | `benchmarks/README.md`, `benchmarks/retrieval.py` | Direct full README; retrieval implementation supplied by runtime. Stability, filing-error, verdict and incremental scoring implementations not traced here: prevents complete evaluator or causal-design assessment. Non-shipped contradiction/revision harness unavailable per README |
| Model prompts | `src/llmw2/agents/prompts/librarian/summarize.md`, `src/llmw2/agents/prompts/researcher/system.md` | Direct reads; librarian goals and combine warning supplied by runtime |

No generic hook discovery or hook execution is claimed: the searched CLI/MCP/HTTP surfaces expose fixed operations, and arbitrary library Steps remain caller-supplied opaque alternatives. Available but uninspected evaluator branches and custom implementations prevent a system-complete negative about all possible acceptance mechanisms. Missing paired source/note/answer traces prevents observed preservation, exercised criticism and successful improvement conclusions. Missing intervention/comparison traces prevents attributing any reported gain to a particular classifier, guard or organizational change.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source](#epi-obj-source) | Imported document assertions | see [EPI-OBJ-source](#epi-obj-source) | SRC-1 `src/llmw2/agents/prompts/librarian/summarize.md` | External truth warrant unknown |
| [EPI-OBJ-note](#epi-obj-note) | Generated or concatenated note assertions | see [EPI-OBJ-note](#epi-obj-note) | SRC-1 `src/llmw2/agents/steps_classic.py` | Fact retention is not guaranteed by token retention |
| [EPI-OBJ-answer](#epi-obj-answer) | Assertions responding to a question | see [EPI-OBJ-answer](#epi-obj-answer) | SRC-1 `src/llmw2/agents/researcher.py` | Citation membership is not support |
| [EPI-OBJ-check-results](#epi-obj-check-results) | Value overlap, identity/still-holds/conflict judgments, lint and route diagnostics | see [EPI-OBJ-check-results](#epi-obj-check-results) | SRC-1 `src/llmw2/agents/revisions.py`, `src/llmw2/audit.py` | Distinct result consumers below; no unified oracle |
| [RT-OBJ-prompts](runtime.md#rt-obj-prompts) | Method instructions; not evidence of document facts | see [RT-OBJ-prompts](runtime.md#rt-obj-prompts) | SRC-1 `src/llmw2/agents/prompts.py` | Static guidance versus accumulated results |
| [RT-CMP-llm](runtime.md#rt-cmp-llm), [RT-CMP-classifier](runtime.md#rt-cmp-classifier) | Distributed parameters: particular propositions not determinable | see these component records | SRC-1 `src/llmw2/models/llm.py`, `src/llmw2/models/classifier.py` | Parameters and internal checking uninspected; no inferred learning |

## Authority-route ledger

Fields owned by declaring records are referenced rather than duplicated. “Implemented” describes inspected wiring, not observed compliance. Each row separates the function of a shared pipeline.

Route ID: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source](#epi-obj-source)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-source-filing](runtime.md#rt-rte-source-filing) and [EPI-OBJ-source](#epi-obj-source).
Claim IDs: [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-OBJ-note](#epi-obj-note); generated summary/merge preservation requires paired semantic evidence; deterministic append subcase preserves supplied bodies, not source truth.
Claim IDs: [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-step-check](#epi-rte-step-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-step-check](#epi-rte-step-check).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-merge-guard](#epi-rte-merge-guard)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-merge-guard](#epi-rte-merge-guard).
Claim IDs: [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-guard-choice](#epi-rte-guard-choice)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-guard-choice](#epi-rte-guard-choice).
Claim IDs: [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-source-filing](runtime.md#rt-rte-source-filing); operational admission of checked drafts, not an evidence-consuming factual acceptance decision.
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-revision-check](#epi-rte-revision-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-revision-check](#epi-rte-revision-check).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-revision-admit](#epi-rte-revision-admit)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-revision-admit](#epi-rte-revision-admit).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-revision-admit](#epi-rte-revision-admit)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-revision-admit](#epi-rte-revision-admit); copied fragments and generated summary coexist; lexical replacement labels need contextual interpretation.
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) and [EPI-OBJ-answer](#epi-obj-answer).
Claim IDs: [EPI-CLM-source-answers](#epi-clm-source-answers)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-conflict-check](#epi-rte-conflict-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-conflict-check](#epi-rte-conflict-check).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-conflict-hint](#epi-rte-conflict-hint)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: non-truth-apt policy/content update: add conflict-reporting instruction
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-conflict-hint](#epi-rte-conflict-hint).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) and [EPI-OBJ-answer](#epi-obj-answer); no particular entailed answer or non-entailed conjecture established.
Claim IDs: [EPI-CLM-source-answers](#epi-clm-source-answers)
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-route-audit](#epi-rte-route-audit)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-route-audit](#epi-rte-route-audit).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-audit-apply](#epi-rte-audit-apply)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: non-truth-apt policy/content update: change filing location
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-audit-apply](#epi-rte-audit-apply).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-health-check](#epi-rte-health-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-health-check](#epi-rte-health-check); arithmetic over recognized log entries only, not warranted premises about real filing events.
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-bundle-check](#epi-rte-bundle-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-bundle-check](#epi-rte-bundle-check).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-origin-purge](#epi-rte-origin-purge)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-origin-purge](#epi-rte-origin-purge).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: non-truth-apt policy/content update: caller-directed taxonomy or deletion
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-batch-sync](runtime.md#rt-rte-batch-sync)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note](#epi-obj-note)
Content/update relation: non-truth-apt policy/content update: plan/split taxonomy and sync progress
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-batch-sync](runtime.md#rt-rte-batch-sync).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-prompts](runtime.md#rt-obj-prompts)
Content/update relation: non-truth-apt policy/content update: operator prompts/settings or caller Steps
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration).
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

Route ID: [EPI-RTE-fact-score](#epi-rte-fact-score)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-check-results](#epi-obj-check-results)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence; gap/limit: see [EPI-RTE-fact-score](#epi-rte-fact-score); string-match result from code, not entailment of source propositions.
Claim IDs: none
Mismatch marker: none unless qualified in the cited finding.

No separate lifecycle-integration route after factual acceptance is established in the inspected filing/answer paths. Source references, indexing, links and archiving serve retention, lineage and operational consumption; they do not retroactively supply that acceptance. This is a bounded result for the traced defaults, not a negative about caller-injected Steps or every offline evaluator.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation) | see record | SRC-1 `src/llmw2/agents/prompts/librarian/system.md`; doctrine/design | see record | [RT-RTE-source-filing](runtime.md#rt-rte-source-filing), [EPI-RTE-merge-guard](#epi-rte-merge-guard), [EPI-RTE-guard-choice](#epi-rte-guard-choice), [EPI-RTE-revision-check](#epi-rte-revision-check) | No linked run supplied | None; checks compare selected values/fragments, not every proposition | Source-faithful production is requested; retries and conservative fallbacks are implemented | Warning-only combine loss and imperfect value guards prevent enforced full preservation |
| [EPI-CLM-source-answers](#epi-clm-source-answers) | see record | SRC-1 `src/llmw2/agents/prompts/researcher/system.md`; doctrine/design | see record | [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [EPI-RTE-conflict-check](#epi-rte-conflict-check), [EPI-RTE-conflict-hint](#epi-rte-conflict-hint) | None supplied | No source-entailment evaluator of final answer in inspected path | Selected notes and hints reach a writer | Path metadata does not validate answer truth |
| [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | see record | SRC-1 `benchmarks/README.md`; reported operation | Comparison procedure and metric definitions retained | [EPI-RTE-fact-score](#epi-rte-fact-score); other evaluators only partially inspected | Reported aggregate tables, not independently inspected paired executions | Versions differ as bundles; single-run/two-model comparisons cannot isolate individual components | Repository reports placement/cost/retrieval tradeoffs | Does not establish factual correctness, scale transfer or a particular mechanism's causal effect |

## Bounded conclusion

The system acquires caller documents and client memories, retains raw provenance and model-authored notes, and uses selected notes in later writing and answering ([RT-RTE-source-filing](runtime.md#rt-rte-source-filing), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)). Source truth warrant is unknown; preserved text and references permit later inspection but do not authenticate a source. Generated summarization and answering are semantically indeterminate at this evidence level. An append branch demonstrably preserves its supplied bodies as strings; it does not establish that the candidate already preserves the original.

There are consequential checks, not simply unchecked storage. Type/tree checks veto malformed steps; merge heuristics trigger another model call and choose by value retention; replacement uses document identity and, in CROW, sentence-level source agreement; conflict classification alters answer guidance. These are different targets with different domains ([EPI-RTE-step-check](#epi-rte-step-check), [EPI-RTE-merge-guard](#epi-rte-merge-guard), [EPI-RTE-guard-choice](#epi-rte-guard-choice), [EPI-RTE-revision-check](#epi-rte-revision-check), [EPI-RTE-revision-admit](#epi-rte-revision-admit), [EPI-RTE-conflict-check](#epi-rte-conflict-check), [EPI-RTE-conflict-hint](#epi-rte-conflict-hint)). Replacement's sentence criterion licenses selected old sentences relative to a new source passage, not a general acceptance of the note as true. Classic lacks that classifier gate. Retention and use are permitted before a full factual acceptance.

Maintenance can withdraw information or change discoverability. Caller-directed purge removes citing notes and refiles other raw sources rather than asking a writer to subtract unsupported sentences; audit apply moves notes based on classifier suggestions. Lint and health return bounded diagnostic facts, not semantic endorsement ([EPI-RTE-origin-purge](#epi-rte-origin-purge), [EPI-RTE-route-audit](#epi-rte-route-audit), [EPI-RTE-audit-apply](#epi-rte-audit-apply), [EPI-RTE-bundle-check](#epi-rte-bundle-check), [EPI-RTE-health-check](#epi-rte-health-check)). Health flags do not automatically update policy. Offline factual scores have lexical rather than propositional force ([EPI-RTE-fact-score](#epi-rte-fact-score)).

No particular accepted ampliative claim, warranted formal derivation about the documents, or integration after such acceptance is established. This is not a finding that models never conjecture. No observed learning benefit, exercised self-improvement or provider parameter adaptation follows from wiring or reported aggregate outcomes. The guards can revise a work product and hints can adapt a current answer instruction without demonstrating a criticism-driven change to the system's own methods. A universal theory-builder/autonomy verdict is unwarranted: localized method text exists, operational consumption is wired, but content-directed criticism and retained iteration on the method are unestablished in these inspected routes ([RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration), [RT-BAP-model-instructions](runtime.md#rt-bap-model-instructions)). Inaccessible internal model processing is not evidence of absent reasoning.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source
Label: Source assertions

Source-native identity: Source.text and raw source body; natural-language assertions on caller-supplied topics, persisted as Markdown raw copies by the filing container [RT-RTE-source-filing](runtime.md#rt-rte-source-filing). This is the input object, not another route or the static [RT-OBJ-prompts](runtime.md#rt-obj-prompts). Source truth warrant is unknown: extraction/import is acquisition, not produced knowledge. Model summarization receives source text through the prompt. SRC-1 `src/llmw2/agents/prompts/librarian/summarize.md`:

> <source>
> {{source_text}}
> </source>
> --- `src/llmw2/agents/prompts/librarian/summarize.md`

#### EPI-OBJ-note
Label: Candidate and stored note bodies

Source-native identity: Candidate/NoteDraft bodies and persisted Note.main_body; natural-language assertions, on disk Markdown after filing, in-memory before it. Distinct from [EPI-OBJ-source](#epi-obj-source) because rewriting, merging and later readers differ; closest supplied container [RT-RTE-source-filing](runtime.md#rt-rte-source-filing) owns the persistence route, not this object. Generated bodies may omit, restate or introduce assertions: semantic relation indeterminate without paired evidence. The over-budget append subcase is non-ampliative reshaping of the supplied existing/incoming bodies, but candidate-to-source fidelity remains unknown.

Concrete source-level deduction, not execution: with existing body "Rate is 10.", incoming candidate body "Rate is 12." and title "Update", the append code retains both and inserts a heading. No truth adjudication follows. SRC-1 `src/llmw2/agents/steps_classic.py`:

> section = f"# {title.strip()}\n\n{body.strip()}"
> return NoteDraft(title=note.title, summary=note.summary, tags=list(dict.fromkeys(tags)), body=f"{existing.rstrip()}\n\n{section}")
> --- `src/llmw2/agents/steps_classic.py`

#### EPI-OBJ-answer
Label: Answer text and citation metadata

Source-native identity: Answer.text is natural-language, transient return data; citation paths/titles are symbolic metadata derived from it, not independently checked evidence. Closest supplied [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) is the producer/consumer route, not a duplicate object. Distinct from stored notes because this route does not save the answer. SRC-1 `src/llmw2/agents/researcher.py`:

> text = check_answer(self.steps.answer(ctx, asked, self._with_rows(question, notes))) if notes else NO_ANSWER
> --- `src/llmw2/agents/researcher.py`

Citation metadata scope and its limits: see [RT-RTE-question-answer](runtime.md#rt-rte-question-answer). No checked entailment or accepted new proposition is established.

#### EPI-OBJ-check-results
Label: Per-check results

Source-native identity: value sets, probability scalars, Problem/RouteProposal/FolderHealth records and fact-match booleans. Symbolic Python return values; route proposals/diagnostics are serialized by callers, while decision traces may enter ordinary provenance/logs. Distinct from natural-language [EPI-OBJ-note](#epi-obj-note) and external distributed parameters [RT-CMP-classifier](runtime.md#rt-cmp-classifier); no counterpart object declared in supplied runtime. This container does not give all results the same warrant: the routes below split their producers, checks and consequences. SRC-1 `src/llmw2/audit.py`:

> share = (new + fallbacks) / filed if filed else 0.0
> rows.append(FolderHealth(folder, mon, filed, new, fallbacks, share, filed >= min_filed and share > max_share))
> --- `src/llmw2/audit.py`

### Routes

#### EPI-RTE-step-check
Label: Structural step checks

Endpoints: returned step objects → check_* → next pipeline operation or StepError. Owner: Python step contract. Target/domain: Python return types, nonempty title, serializable fields, known tree identities and creation depth; not proposition truth. String-only check_answer also belongs to the question route [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), so this structural family overlaps both supplied containers rather than redefining either. Models/custom Steps propose; code decides and vetoes. Open requests, no answer oracle, rollback is stopping before the checked step's downstream write, not undo of earlier writes. Epistemic license: shape and membership only. Behavioral-authority path: pipeline, direct return/exception, enforcing, current operation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Typed value or StepError.
- Later read-back: inapplicable — checks do not accumulate results for later invocations.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: Every checked step return; supplied tree/pool constrains identities.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Code permits continuation or throws; factual adequacy is not tested.
- Evidence limits: Source inspection only. Even a syntactically valid string can assert unsupported facts.

Evidence: SRC-1 `src/llmw2/agents/steps.py` (implementation).
> def check_answer(out: object) -> str:
>     if not isinstance(out, str):
>         raise StepError("answer", f"must return a str, not {type(out).__name__}")
>     return out
> --- `src/llmw2/agents/steps.py`

#### EPI-RTE-merge-guard
Label: Merge value-loss evidence

Part of: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Endpoints: existing/source/candidate and draft → incoming_values comparisons → lost/kept counts. Owner: classic merge code, also used for CROW writing. Target/domain: lexical values in bodies and exact unchanged-body comparison. No expected-answer oracle: source/existing text is the reference, not external truth. This check is distinct from [EPI-RTE-guard-choice](#epi-rte-guard-choice), which consumes its results. No human per-draft evaluation. Epistemic license: selected value presence only. Behavioral-authority path: merge guard branch predicates, direct counts, enforcing retry selection, current merge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New/kept/lost value comparisons.
- Later read-back: inapplicable — transient counts are not independently retained memory.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: Short-source path checks incoming values; long-source path checks unchanged body plus missing new values; old-value loss evaluated after the draft.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Results determine retry conditions, not a final semantic pass.
- Evidence limits: Counts do not preserve who/when/negation; final drafts may still lose facts.

Evidence: SRC-1 `src/llmw2/agents/steps_classic.py` (implementation).
> new = incoming_values(body[:budget]) - incoming_values(existing)
>         kept = len(new & incoming_values(draft.body))
> --- `src/llmw2/agents/steps_classic.py`

#### EPI-RTE-guard-choice
Label: Merge retry and draft selection

Part of: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Endpoints: guard evidence → another ask_json when conditions hold → returned NoteDraft. Owner: merge code; model authors proposals, code selects. Domain: retry if unchanged or fewer than half new values retained; retry old losses above LOST_MAX and take retry only if it loses fewer old values. This is bounded operational acceptance for a merge draft, intended use is filing, not acceptance of every assertion as true. No per-content human veto; exceptions can stop. Guidance: merge/merge_source prompts with named lost values. Persisted result is the filed body, not an updated runtime method. Behavioral-authority path: Librarian, NoteDraft return, permissive, current filing then later note consumers. Closest container remains [RT-RTE-source-filing](runtime.md#rt-rte-source-filing); this is its disposition part, not duplicate of the evidence computation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Chosen draft, even without full fact preservation.
- Later read-back: Chosen draft is saved by filing and may be read on future questions/merges.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: Guard predicates from the preceding check; later comparison chooses fewer lost old values.
- Invalidation or expiry: No general TTL; next operation reads current state; explicit deletion/rebuild or source revision can replace retained effects.
- Activation or effect: Requests one bounded retry per applicable branch; warning-only length checks do not veto content.
- Evidence limits: Not an evidence-consuming global factual acceptance. A value-preserving draft can assign values incorrectly; retry is not proof of improvement.

Evidence: SRC-1 `src/llmw2/agents/steps_classic.py` (implementation).
> again = ctx.ask_json(prompt, NoteDraft, **values)
>         if len(old - incoming_values(again.body)) < len(lost):
>             draft = again
> --- `src/llmw2/agents/steps_classic.py`

#### EPI-RTE-revision-check
Label: Revision identity and kept-sentence checks

Part of: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Endpoints: source and current note/raw copies → same_document and kept_sentences tests → replacement eligibility and surviving sentences. Owner: code plus optional classifier. Domain: body-hash untouchedness, normalized title/file name, raw references, eight-word containment (new-in-old >=0.6; old-in-new >=0.9), then CROW same-subject confidence >=0.7 from openings/first 40 changes. Candidate old sentences must contain values still in source but missing from new body, avoid removed strings and missing date matches. CROW additionally asks STILL against one lexically chosen source paragraph, threshold >=0.3; ModelError rejects that sentence. Classic has no classifier checks. Proposer: summary model and old note; decider: code/classifier. No human or external truth oracle. Epistemic license: similarity/selected sentence agreement with supplied source, not correctness of source. Behavioral-authority path: revision assembly, return values, enforcing eligibility/filtering, one revision.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Eligibility resource/text or None; list of eligible old sentences.
- Later read-back: inapplicable — judgments are transient; retained effects belong to the disposition route.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: revisions=replace, candidate present, supported same-document and sentence filters.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Code can select replacement versus ordinary merge and omit old sentences.
- Evidence limits: Countercase to treating revisions as unchecked: CROW has real sentence filtering. Countercase to universal semantic checking: classic does not; partial passages and low thresholds bound warrant.

Evidence: SRC-1 `src/llmw2/agents/revisions.py` (implementation).
> try:
>                 return classifier.nouls(state, {"q": STILL}, op="revise/still_holds")["q"] >= STILL_MIN
>             except ModelError:
>                 return False
> --- `src/llmw2/agents/revisions.py`

#### EPI-RTE-revision-admit
Label: Revision assembly and replacement admission

Part of: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)
Endpoints: successful revision checks → candidate body plus change annotations and surviving sentences → replacement draft. Owner: revision/Librarian code; model supplies summary. Criterion/intended use/scope: only qualifying same-document updates may replace an untouched code-written note; selected old sentences are retained relative to the supplied new passage. This is operational replacement admission with bounded source-agreement criteria, not blanket acceptance of the summary's claims. Code can veto replacement and fall back to merge; CROW can veto individual old sentences. Archive/write and later previous_version linkage belong to the supplied filing container. Guidance is candidate summary, STILL/IDENTITY questions and previous-version labels. Recovery is a retained predecessor when archive succeeds, not universal transactional rollback. Behavioral-authority path: Librarian/Store, draft and archive pointers, permissive, future note/history consumers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New NoteDraft or None for ordinary merge.
- Later read-back: Filed replacement and archived predecessor may be read by later merge/ask; history classifier can reload predecessor.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: same_document succeeds; candidates bounded by kept-sentence checks and 8000-character kept cap; at most 60 change lines.
- Invalidation or expiry: No general TTL; next operation reads current state; explicit deletion/rebuild or source revision can replace retained effects.
- Activation or effect: New summary plus explicit historical changes can displace prior active content without a full truth check.
- Evidence limits: Change detection is lexical: attributing a before/after value to the same real-world quantity needs context. Successful assembly and actual use are unobserved.

Evidence: SRC-1 `src/llmw2/agents/revisions.py` (implementation).
> body = cand.body.rstrip()
>     if changes := changes_section(old, source.text):
>         body += "\n\n" + changes
> --- `src/llmw2/agents/revisions.py`

#### EPI-RTE-conflict-check
Label: Cross-note disagreement evidence

Part of: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Endpoints: question and notes → conflict_state → classifier probability → boolean. Owner: Researcher. Target/domain: disagreement about question among at most eight notes, each represented by its first best-overlap paragraph truncated to 900 characters. It runs before _with_rows spreadsheet expansion, so it does not check newly inserted raw rows. Condition: answer_conflicts, classifier present and >=2 notes; threshold strictly >0.4. ModelError yields no hint. Not an answer oracle or truth adjudication; computation proposes/decides with code threshold, no human evaluation. Behavioral-authority path: Researcher hint branch, boolean, enforcing branch only, this question.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean and decision trace.
- Later read-back: inapplicable — current-question result, not persistent conflict adjudication.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: Enabled CROW/classifier and two selected/history notes.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Can trigger instruction addition; does not reject notes or final answer.
- Evidence limits: Conflict outside the selected passages can be missed; no conclusion about reliable conflict detection.

Evidence: SRC-1 `src/llmw2/agents/researcher.py` (implementation).
> ctx.decide("conflict", "classifier", "hint" if p > conflicts.CONFLICT_MIN else "none", p)
>         return p > conflicts.CONFLICT_MIN
> --- `src/llmw2/agents/researcher.py`

#### EPI-RTE-conflict-hint
Label: Conflict result changes answer guidance

Part of: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)
Endpoints: true conflict result → appended CONFLICT_HINT → writer answer. Owner: Researcher code inserts instruction; model interprets. No knowledge acceptance decision. Epistemic license: none beyond a warning that notes may disagree. Operational authority: request every conflicting value, provenance and recency rather than silently choosing. Behavioral-authority path: answer writer, question text, advisory, current answer. This is a distinct downstream part from conflict evidence; no retained policy revision or new internal machinery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Augmented asked question reaches answer call.
- Later read-back: inapplicable — hint is reconstructed per question, not stored policy.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: Preceding conflict boolean true.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Instructions can change response policy; compliance is unobserved.
- Evidence limits: Model can ignore or misunderstand hint; no subsequent answer-support check.

Evidence: SRC-1 `src/llmw2/agents/conflicts.py` (implementation).
> "(The notes may disagree on this. If two notes give different values for what the question asks, report every value, "
>     "say which note gives which and which source is more recent, and do not pick one silently.)"
> --- `src/llmw2/agents/conflicts.py`

#### EPI-RTE-route-audit
Label: Audit route proposals

Endpoints: CROW audit request → note Candidate → flat classifier route → RouteProposal. Owner: Wiki.audit_routes; classifier proposes destination; code filters branch and confidence. Target/domain: filing suitability among existing folders using note-derived candidate state, not source truth. No generative writer/per-level fallback and no external oracle. Open maintenance mode, caller initiates; no per-proposal human required. Unlike supplied [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), this newly traced route evaluates current organization computationally. Epistemic license: classifier preference, not established optimal placement. Behavioral-authority path: CLI/HTTP caller and optional apply route, proposal list, advisory before apply, current audit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cross-branch proposals with confidence and applied flag false.
- Later read-back: inapplicable — proposal result itself is not durable queued area-proposal memory.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: CROW only; another branch; neither ancestor nor descendant; probability >= min_confidence (default 0.7).
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Exposes suggested moves; no write without apply.
- Evidence limits: Unobserved utility, calibration and accuracy. Existing note context may already contain errors.

Evidence: SRC-1 `src/llmw2/wiki.py` (implementation).
> if current.startswith(routed[0].label.rstrip("/") + "/"):  # up in its own branch: never undo a plan or a split
>                 continue
>             proposals.append(RouteProposal(note.rel, note.id, note.title, current, routed[0].label, routed[1]))
> --- `src/llmw2/wiki.py`

#### EPI-RTE-audit-apply
Label: Apply audit recommendations

Endpoints: audit proposals plus apply flag → locked move_note → updated applied flags. Owner: Wiki. Distinct from [EPI-RTE-route-audit](#epi-rte-route-audit) because it grants consequence rather than producing a judgment; closest supplied [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) describes caller-driven moves, but not this classifier-driven choice. Proposer: classifier; admission: caller requests apply globally then code moves each candidate; human provenance of flag unresolved. Rejection: route filters and InputError; no fresh truth evaluation. Recovery: failed moves skipped; no all-moves transaction or automatic rollback. Criterion/intended use/scope: confidence/cross-branch constraints for organizational placement. Behavioral-authority path: Store, move_note under lock, enforcing filesystem change, later routing/selection. Retained location can shape what models encounter without asserting the note is true.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated list of applied/not-applied proposals.
- Later read-back: Moved notes/indexes are visible on future tree loads and retrieval.
- Delegated visibility: Only selected text/state reaches model calls; no target-spawned autonomous agent is evidenced.
- Selection predicate: apply=True after proposal construction; current move preconditions.
- Invalidation or expiry: No general TTL; next operation reads current state; explicit deletion/rebuild or source revision can replace retained effects.
- Activation or effect: Moves locations; InputError leaves that proposal unapplied and continues others.
- Evidence limits: Improved retrieval or correctness not established. HTTP apply is a requested flag, not authenticated per-content approval.

Evidence: SRC-1 `src/llmw2/wiki.py` (implementation).
> with self.store.lock():
>                         self.store.move_note(proposal.path, proposal.proposed)
>                     proposal.applied = True
>                 except InputError:  # the note went meanwhile, or is already there: the others go on
>                     continue
> --- `src/llmw2/wiki.py`

#### EPI-RTE-health-check
Label: Taxonomy health diagnostics

Endpoints: log.md text → recognized entries/month counters → FolderHealth → CLI/HTTP output. Owner: deterministic audit code. Target/domain: rate of recognized newly created subfolders plus fallback routes per filed entry, not semantic accuracy or true event completeness. Logged plans/splits excluded from new-subfolder count; unknown verbs and malformed/nonmatching entries ignored. Compared with supplied [RT-RTE-batch-sync](runtime.md#rt-rte-batch-sync), this is a separate read/diagnose route, not split admission. Entailed derivation is licensed only for arithmetic over recognized strings. Behavioral-authority path: operator/API, returned rows and printed flags, advisory, current diagnosis; no automatic policy update.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts, shares and flags.
- Later read-back: inapplicable — diagnostic rows are not automatically retained or fed into a later model.
- Delegated visibility: inapplicable — deterministic code; no delegated model executor
- Selection predicate: By month/folder, filed >= min_filed and share > max_share (defaults 5 and 0.3).
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: CLI marks flagged rows; HTTP returns JSON; no downstream software repair implied.
- Evidence limits: Edited/incomplete logs break correspondence with actual filing. This is a measure of logged activity, not learned policy.

Evidence: SRC-1 `src/llmw2/audit.py` (implementation).
> share = (new + fallbacks) / filed if filed else 0.0
>         rows.append(FolderHealth(folder, mon, filed, new, fallbacks, share, filed >= min_filed and share > max_share))
> --- `src/llmw2/audit.py`

#### EPI-RTE-bundle-check
Label: Bundle lint diagnostics

Endpoints: recursive Markdown/index/log scan → Problem list → Wiki.check → CLI exit or HTTP strings. Owner: deterministic checker. Target/domain: OKF document validation, duplicate IDs, relative links, folder indexes and log heading/order. Raw documents exempt link/id checking; dot paths skipped. No counterpart among supplied runtime route declarations: this is an exposed evaluator missing from their route inventory, not a correction to an established negative. Epistemic license: checked structure only; not factual consistency. Behavioral-authority path: CLI, problem list/exit 1, enforcing command status; HTTP, strings, advisory; current check. No automatic rejection of previously stored notes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Problem list; CLI returns nonzero if nonempty.
- Later read-back: inapplicable — result is returned, not persistent acceptance state.
- Delegated visibility: inapplicable — deterministic code; no delegated model executor
- Selection predicate: All eligible files under requested bundle root.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Diagnostic problems affect command status and operator judgment, not an implemented content rollback.
- Evidence limits: An empty list does not establish semantic correctness, source support, or absence of skipped-file defects.

Evidence: SRC-1 `src/llmw2/bundle/check.py` (implementation).
> """Deterministic lint of a wiki: OKF conformance, index drift, broken links, log format. No model calls."""
> --- `src/llmw2/bundle/check.py`

#### EPI-RTE-origin-purge
Label: Withdraw an origin and dependent notes

Part of: [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance)
Endpoints: origin key → raw copies → all citing notes → purge_notes/scrub_log → reingest other cited documents. Owner: caller requests, Wiki/Store code determines dependencies and deletes. Domain: explicit lineage withdrawal, not semantic falsification. No answer oracle; no per-sentence truth judgment. Mixed-origin notes are removed wholesale, then other sources refiled rather than asking a model to subtract one source's claims. Code can reject missing origins or skip effects in dry_run. Recovery is limited: refile failures retain other raw sources and report errors, no universal undo. Behavioral-authority path: Store/filesystem and later Researcher, deletion/refiling, enforcing removal from future loads, across calls; cannot retract prior answers already returned. This is a finer withdrawal part of the supplied maintenance container.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Purged report or None; dry_run reports prospective effects.
- Later read-back: Later readers no longer see deleted active notes; remaining documents may produce new notes.
- Delegated visibility: inapplicable — deterministic code; no delegated model executor
- Selection predicate: Origin raws (including sheets when applicable), citation intersection and caller dry_run/confirmation surface.
- Invalidation or expiry: No general TTL; next operation reads current state; explicit deletion/rebuild or source revision can replace retained effects.
- Activation or effect: Removes note/raw/archive dependencies, scrubs related logs and refiles surviving inputs.
- Evidence limits: Source references must be complete; manual uncited copying and external consumers not proven retractable. No observed post-purge correctness.

Evidence: SRC-1 `src/llmw2/wiki.py` (implementation).
> notes = [n for n in root.all_notes() if set(raws).intersection(raw_sources(n.frontmatter))]
>             others = self._cited_by(notes, set(raws))  # read before anything is deleted
> --- `src/llmw2/wiki.py`

#### EPI-RTE-fact-score
Label: Offline lexical fact scoring

Endpoints: labels with planted facts and final note bodies → normalized regex match → records/aggregate recall. Owner: benchmark code, operator supplies kept runs/labels. Target/domain: string presence, superseded value presence and number-set differences; not truth/entailment. Distinct from supplied retrieval evaluator [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) discussion: this checks final note bodies rather than selected-note identity. References are corpus label strings; generated labels are not independent real-world oracles. Code decides lexical hits, human must interpret score limits; open offline comparison, not online admission. Behavioral-authority path: benchmark report/operator, metric record, advisory, experiment/report horizon. No inspected consumer gates ordinary ingest or automatically promotes runtime changes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-fact found/old_found booleans and recall aggregates.
- Later read-back: inapplicable — offline results are not wired as later wiki/model input in the inspected route.
- Delegated visibility: inapplicable — deterministic code; no delegated model executor
- Selection predicate: Facts listed in labels; final body chosen from run mapping; None body is a miss.
- Invalidation or expiry: inapplicable — transient evaluation result; rerun uses current inputs
- Activation or effect: Computes scores; no production-content admission effect.
- Evidence limits: Concrete source deduction: fact '€3.85' normalizes to '3.85'; both 'Price is €3.85.' and 'Price is not €3.85.' match the same wanted regex. Thus found cannot license the price assertion. '2.9k' paraphrase may miss; a valid computed value can count as invented. No target execution performed.

Evidence: SRC-1 `benchmarks/note_facts.py` (implementation).
> wanted = "".join(normalize(fact).split())
>     if not wanted:
>         return False
>     pattern = r"(?<![a-z0-9])" + r"\s*".join(re.escape(c) for c in wanted) + r"(?![a-z0-9])"
>     return re.search(pattern, normalize(text)) is not None
> --- `benchmarks/note_facts.py`

### Claims

#### EPI-CLM-source-answers
Label: Answer from notes alone

Claimed operation: Researcher finds relevant notes and answers only from them, without changing wiki state. Source: SRC-1 `src/llmw2/agents/prompts/researcher/system.md`, doctrine/design. Closest supplied [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation) concerns filing, not this answer-side constraint. The read-only route is implemented; note-supported truth remains unestablished.

> You are the Researcher of an LLM wiki: a tree of folders holding Markdown notes. Every folder has a one-line description; every note has a title and a one-line summary. You find the notes that answer a question and answer from them alone. You never change the wiki.
> --- `src/llmw2/agents/prompts/researcher/system.md`

#### EPI-CLM-benchmark-results
Label: Reported CROW comparison

Claimed operation/benefit: author reports better agreement with real folders and lower cost versus prior CROW/classic on the PostHog experiment. Source: SRC-1 `benchmarks/README.md`, reported operation. Distinct from [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation): organizational outcome claim, not every-fact preservation. Its stated setting is 120 pages, two writing models and one run per arm/model; not independent component variation. The report itself qualifies retrieval differences and one-run limits.

> **Against classic.** Classic also builds a deeper tree, but with DeepSeek half of its 40 folders hold one note; 0.6.0
> agrees more with the real folders (AMI +0.11 to +0.12) at 0.45 to 0.65 times its cost.
> --- `benchmarks/README.md`

The offline contradiction/revision scoring cannot be reconstructed as shipped evaluation from this source alone:

> Links between duplicates and answers to contradictions on the `dup` corpus, revisions and the real corpora were scored
> by a harness that is not in the repository (the `dup` corpus is filed and asked by it, not by `stability.py`). A series
> run with `--keep` saves what they read (the final wikis, the usage logs and the raw JSON), so it can be scored later.
> --- `benchmarks/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
