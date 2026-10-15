---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of llm-context-base: source extraction, completion criteria, precedent use and behavior-shaping retained text at the frozen template revision."
run-id: AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
---

# llm-context-base epistemic report

## Source-and-claim boundary

The question is how this template acquires, checks and licenses retained content for later answers and behavior. Scope and exclusions are **see [boundary](boundary.md#boundary-and-evidence)**; sources are **see [Source register](boundary.md#source-register)**. The assessment concerns shipped prompts, templates, configuration and the metadata converter, not the external assistant's inference or tool implementation. All new inspections below concern SRC-1 at the frozen revision. Prompt routes have architectural status `doctrine only`: executable host delivery and observed adherence are not supplied. The converter alone supplies an inspected executable transformation. No target execution was performed.

Knowledge and warrant claims are [EPI-CLM-decision-learning](#epi-clm-decision-learning), [EPI-CLM-standard-enforcement](#epi-clm-standard-enforcement), [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory), and the supplied [RT-CLM-review-policy](runtime.md#rt-clm-review-policy). Context-efficiency claims and host-permission limits are see [RT-RTE-context-review](runtime.md#rt-rte-context-review) and [RT-CLM-host-permissions](runtime.md#rt-clm-host-permissions).

| Entry point or operation | Source path, SRC-1 | Coverage and provenance | Limit and conclusion prevented |
|---|---|---|---|
| Generic bootstrap and startup | `AGENTS.md`, `_config/config.md`, `_meta/instructions/general.md` | Direct reads; see [RT-RTE-session-start](runtime.md#rt-rte-session-start) | Framework-mode bypass; no observed delivery/adherence |
| Other five bootstraps and tool discovery | `.claude/CLAUDE.md`, `.cursor/rules/bootstrap.mdc`, `.cursorrules`, `.github/copilot-instructions.md`, `.windsurfrules` | Supplied runtime and boundary findings, not new direct reads; see [RT-RTE-session-start](runtime.md#rt-rte-session-start) | External host discovery not inspected; no cross-host reliability conclusion |
| Capture, web clip triage and source preservation | `_meta/instructions/agent-write.md`, `_meta/instructions/general.md`, `assets/clipper-template.json`, `_sources/README.md` | Direct reads; see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | Clipper implementation external; no semantic fidelity or factual endorsement established |
| Query, missing-document response and decision precedent | `_meta/instructions/knowledge-query.md`, `_meta/templates/decision.md` | Direct reads; see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | No user corpus or outcome trace; retrieval quality and improved decisions unobserved |
| Standards, completion and links | `_config/standard.md`, `_meta/instructions/definition-of-done.md`, `_meta/templates/knowledge-article.md` | Direct reads; [EPI-RTE-completion-check](#epi-rte-completion-check), [EPI-RTE-completion-status](#epi-rte-completion-status), [EPI-RTE-completion-links](#epi-rte-completion-links) | Accuracy is a requested criterion without specified evidence procedure |
| Lint evaluation and cleanup/withdrawal | `_meta/instructions/knowledge-lint.md`, `_config/standard.md` | Direct reads; [EPI-RTE-lint-check](#epi-rte-lint-check), [EPI-RTE-lint-action](#epi-rte-lint-action) | Seven prescribed structural/age checks, not factual verification |
| Immediate rule/preference capture | `_meta/instructions/general.md`, `_config/context.md`, `_config/config.md` | Direct reads; [EPI-RTE-pattern-capture](#epi-rte-pattern-capture), see [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) | No required per-rule evidence acceptance or observed later activation |
| Optimization, optional hooks, permissions | `_meta/instructions/optimization-review.md`, `docs/claude-code-setup.md`, `.claude/settings.json` | Direct reads; see [RT-RTE-context-review](runtime.md#rt-rte-context-review), [RT-CLM-host-permissions](runtime.md#rt-clm-host-permissions) | Hook recipes are not installed scripts; logs of paths/line counts do not license source truth |
| Blog review, publication and tracking | `_meta/instructions/blog-posts/instructions.md` | Direct read; [EPI-RTE-blog-review](#epi-rte-blog-review), [EPI-RTE-blog-publish](#epi-rte-blog-publish) | Newly elaborated runtime omission; platform implementation and factual review criteria absent |
| Standalone Python dispatch and rewrite | `migrate-to-yaml-frontmatter.py` | Complete direct read, static trace; [EPI-RTE-metadata-transform](#epi-rte-metadata-transform), see [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate) | No run evidence, parser, backup or semantic comparator |
| Project indexing, local capture and exports | `1-Projects/README.md`, `.obsidian/app.json`, `_output/README.md`, `docs/linked-code-repos.md` | General-module direct read plus supplied boundary/runtime coverage; see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | Renderers, linked repositories and plugins external; no independent evaluator inferred |

The tracked tree was enumerated and has no additional shipped CLI driver, registered-tool implementation or hook script. This is not an absence claim about external intelligence layers. Available supporting documentation excluded by the boundary is not represented as inaccessible evidence. No additional material operation was identified outside the frozen functional boundary. Coverage of indirectly read paths depends on the supplied findings, not a fresh complete-source audit.

Missing evidence is local: original-source truth and extraction fidelity prevent a warrant-preservation verdict; evidence-consuming accuracy decisions prevent identification of accepted newly produced claims; user corpus and authentic outcome records prevent retrieval/decision effectiveness conclusions; host/model identity and parameter behavior prevent claims about parametric learning; actual update and later-consumer traces prevent exercised adaptation or self-improvement attribution; intervention comparisons prevent causal benefit attribution. The template's sample or placeholder artifacts do not supply these traces.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | Processes, references, extracted points and saved synthesis; particular propositions not determinable in an empty user corpus | see record | SRC-1, `_meta/templates/knowledge-article.md` | Draft/active labels do not establish factual warrant |
| [EPI-OBJ-sources](#epi-obj-sources) | Imported original content; truth and original provenance unknown | see record | SRC-1, `_sources/README.md` | Optional preservation, not endorsement |
| [EPI-OBJ-decision-outcome](#epi-obj-decision-outcome) | Reports of what happened and discovered constraints | see record | SRC-1, `_meta/templates/decision.md` | Pending/example fields are not observed evidence |
| [EPI-OBJ-context](#epi-obj-context) | Personal details and reports of preferences; preferences also prescribe behavior | see record | SRC-1, `_config/context.md` | User assertions versus inferred patterns not uniformly distinguished |
| [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules) | Mainly non-truth-apt policy; guidance also asserts context-efficiency mechanisms | see record | SRC-1, `_meta/instructions/optimization-review.md` | Policy obedience and mechanism truth are different questions |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Structural, date and count claims about files | see record | SRC-1, `_meta/instructions/knowledge-lint.md` | Model-followed recipe, no observed checking |
| [EPI-OBJ-blog-post](#epi-obj-blog-post) | Possible factual prose and real examples; proposition content not determinable before a user draft exists | see record | SRC-1, `_meta/instructions/blog-posts/instructions.md` | Presentation review is not source verification |
| [EPI-OBJ-metadata](#epi-obj-metadata) | Summary/date/source fields may describe the file; tags/status also direct selection | see record | SRC-1, `migrate-to-yaml-frontmatter.py` | Symbolic consumer behavior can differ from surface text preservation |
| [RT-CMP-ai-assistant](runtime.md#rt-cmp-ai-assistant) | Distributed-parametric content opaque | see record | SRC-1, `_config/config.md` | Parameters, exact version and endpoint mutability uninspected; no parametric epistemic verdict |

## Authority-route ledger

Fields owned by the declaring records say `see`; the ledger supplies architectural status and content-edge assessment rather than recopying canonical findings. Repeated citations split consequential functions, not identities. None of the doctrine rows is an observed route.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | content transformation | doctrine only | [EPI-OBJ-sources](#epi-obj-sources) → [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | truth-apt transformation: acquisition/import | External clips/user assertions enter captures | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | Prescribed draft/extracted working copy | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | Source warrant unknown; attribution is not verification | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | SRC-1, `_meta/instructions/agent-write.md` | [RT-CLM-review-policy](runtime.md#rt-clm-review-policy) | none | External source truth, semantic extraction fidelity and execution unknown |
| [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | retention | doctrine only | [EPI-OBJ-sources](#epi-obj-sources) and [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | no content change | Original/working-copy persistence | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | Prescribed filing; optional original retention | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | No added warrant from disk or Git | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) | SRC-1, `_sources/README.md` | [RT-CLM-review-policy](runtime.md#rt-clm-review-policy) | none | Preservation defaults off; full source may be discarded |
| [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | content transformation | doctrine only | [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | truth-apt transformation: indeterminate | Selected files → synthesized answer | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | Prescribed cited synthesis, or nothing-found response | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | May reshape or derive; conjecture requires evidence of non-entailment | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | SRC-1, `_meta/instructions/knowledge-query.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | No input/output pair to distinguish reshaping, entailment or ampliation |
| [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-decision-outcome](#epi-obj-decision-outcome) | no content change | Relevant past outcomes → new decision deliberation | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | Prescribed precedents and failure constraints | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | Outcome report licenses bounded precedent consideration, not causal explanation/transfer | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | SRC-1, `_meta/instructions/knowledge-query.md` | [EPI-CLM-decision-learning](#epi-clm-decision-learning) | none | No observed dependence or improved decision; no universal superseded-content ban |
| [EPI-RTE-completion-check](#epi-rte-completion-check) | check/evidence production | doctrine only | [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | no content change | Knowledge accuracy/completeness and type-specific completion criteria | Assistant/user checklist; accuracy evidence procedure unspecified | see [EPI-RTE-completion-check](#epi-rte-completion-check) | Checklist judgment requested | see [EPI-RTE-completion-check](#epi-rte-completion-check) | Criterion named, but evidence-consuming factual acceptance not established | Supports subsequent status proposal | Assistant → checklist judgment → completion; advisory, current task | SRC-1, `_meta/instructions/definition-of-done.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | Accuracy criterion not an implemented verifier |
| [EPI-RTE-completion-status](#epi-rte-completion-status) | disposition/acceptance | doctrine only | [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | non-truth-apt policy/content update: lifecycle label | All checklist items → active/complete | Assistant with user nudges; useful/findable intended use | see [EPI-RTE-completion-status](#epi-rte-completion-status) | Requested status and filing change | see [EPI-RTE-completion-status](#epi-rte-completion-status) | Operational completion only; no observed accepted ampliative claim | File becomes designated in-use/complete | Future assistant → file status → reliance/selection; advisory, later sessions | SRC-1, `_meta/instructions/definition-of-done.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | Active is not a truth guarantee |
| [EPI-RTE-completion-links](#epi-rte-completion-links) | lifecycle integration | doctrine only | [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | non-truth-apt policy/content update: links and organization | Completed item → related links and proper directory | Assistant; relevance and checklist condition | see [EPI-RTE-completion-links](#epi-rte-completion-links) | Requested connected/filed artifact | see [EPI-RTE-completion-links](#epi-rte-completion-links) | Conditional integration after prescribed completion, not observed epistemic acceptance | Makes completed item navigable | Later reader → links/directory → discovery; advisory, later queries | SRC-1, `_meta/instructions/definition-of-done.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | Links are also a completion prerequisite; graph connection can precede acceptance |
| [EPI-RTE-lint-check](#epi-rte-lint-check) | check/evidence production | doctrine only | [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: entailed derivation | Dates, type-field presence, inbound links, sizes, names and link targets | Assistant following specified searches/counts; filesystem structural domain | see [EPI-RTE-lint-check](#epi-rte-lint-check) | Requested seven-check report | see [EPI-RTE-lint-check](#epi-rte-lint-check) | If correctly interpreted, findings follow file measurements; no source-truth license | Reports feed recommendations and optimization trigger | Assistant/user → report → advisory action; current maintenance session | SRC-1, `_meta/instructions/knowledge-lint.md` | [EPI-CLM-standard-enforcement](#epi-clm-standard-enforcement) | none | No execution; inconsistent metadata coverage; not a complete schema check |
| [EPI-RTE-lint-action](#epi-rte-lint-action) | disposition/acceptance | doctrine only | [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article) | non-truth-apt policy/content update: cleanup and retirement | Flagged records → review/update/archive/link repair | Assistant recommends; user/manual resolution on broken links | see [EPI-RTE-lint-action](#epi-rte-lint-action) | Requested triage/discard/archive or in-place format fixes | see [EPI-RTE-lint-action](#epi-rte-lint-action) | Structural fitness/freshness disposition, not falsification of factual claims | Retirement affects relevance and freezes stale-check exemption | Assistant → status/links/report → advisory selection; later queries | SRC-1, `_meta/instructions/knowledge-lint.md` | [EPI-CLM-standard-enforcement](#epi-clm-standard-enforcement) | none | No universal enforced withdrawal or rollback cascade |
| [EPI-RTE-blog-review](#epi-rte-blog-review) | check/evidence production | doctrine only | [EPI-OBJ-blog-post](#epi-obj-blog-post) | no content change | Draft → visual, screenshot, keyword and social-post checklist | Self-review or peer reviewer; presentation readiness domain | see [EPI-RTE-blog-review](#epi-rte-blog-review) | Requested readiness judgment and pushback on absent visuals | see [EPI-RTE-blog-review](#epi-rte-blog-review) | Licenses presentation readiness, not factual truth of examples | Supports publishing continuation | Author/reviewer → checklist → advisory; current draft | SRC-1, `_meta/instructions/blog-posts/instructions.md` | none | none | No factual correctness or evidence acceptance criterion specified |
| [EPI-RTE-blog-publish](#epi-rte-blog-publish) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-blog-post](#epi-obj-blog-post) | non-truth-apt policy/content update: published label and URL | Reviewed draft → primary publication/cross-post tracking | External author/assistant and platform; deployment uninspected | see [EPI-RTE-blog-publish](#epi-rte-blog-publish) | Requested posted content, status published and links | see [EPI-RTE-blog-publish](#epi-rte-blog-publish) | Publication licenses no additional epistemic warrant | Makes content publicly consumable | Author/platform → publish and cross-post channels → requested action; durable audience exposure | SRC-1, `_meta/instructions/blog-posts/instructions.md` | none | none | Review ownership does not require independent factual evaluator |
| [EPI-RTE-pattern-capture](#epi-rte-pattern-capture) | behavior/policy adaptation | doctrine only | [EPI-OBJ-context](#epi-obj-context) | non-truth-apt policy/content update: operating convention/preference | Conversation rule/preference → context or instruction edit | Assistant identifies established patterns; ask if ambiguous; user can override | see [EPI-RTE-pattern-capture](#epi-rte-pattern-capture) | Requested immediate update and later reload | see [EPI-RTE-pattern-capture](#epi-rte-pattern-capture) | User preference may license personalization; inferred patterns lack mandatory acceptance test | Changes requested future behavior without ordinary draft gate | see [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) | SRC-1, `_meta/instructions/general.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | Factual personal-detail edges separately acquired; no observed activation |
| [RT-RTE-context-review](runtime.md#rt-rte-context-review) | behavior/policy adaptation | doctrine only | [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules) | non-truth-apt policy/content update: instruction restructuring | Measured organization → user-approved leaner instructions | see [RT-RTE-context-review](runtime.md#rt-rte-context-review) | see [RT-RTE-context-review](runtime.md#rt-rte-context-review) | Prescribed proposal, possible rejection or approved edits | see [RT-RTE-context-review](runtime.md#rt-rte-context-review) | Size/repeated reads warrant review, not demonstrated speed or reliability | see [RT-RTE-context-review](runtime.md#rt-rte-context-review) | see [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) | SRC-1, `_meta/instructions/optimization-review.md` | [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | none | Successful learning/reflection/self-improvement remain independently unestablished |
| [EPI-RTE-metadata-transform](#epi-rte-metadata-transform) | content transformation | implemented | [EPI-OBJ-metadata](#epi-obj-metadata) | truth-apt transformation: indeterminate | Legacy bullet metadata and surrounding text → frontmatter rewrite | Fixed regex and formatter; matching Markdown domain | see [EPI-RTE-metadata-transform](#epi-rte-metadata-transform) | Statically deduced rewrite; can lose pre-title content/duplicate metadata | see [EPI-RTE-metadata-transform](#epi-rte-metadata-transform) | No validation or preservation guarantee; bounded witness below | Direct overwrite supplies changed text to future file consumers | Operator → converter → file → later reader/parser; enforcing rewrite, durable | SRC-1, `migrate-to-yaml-frontmatter.py` | [EPI-CLM-standard-enforcement](#epi-clm-standard-enforcement) | none | Intended reshaping, but loss and YAML interpretation defeat general semantic preservation |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-review-policy](runtime.md#rt-clm-review-policy) | see record | SRC-1, `_meta/instructions/agent-write.md`; doctrine/design | see record | [EPI-RTE-metadata-transform](#epi-rte-metadata-transform) is an alternate direct rewrite, not a review gate | None supplied | see record | Inbox/draft enables review opportunity | Immediate pattern edits, explicit destinations and migration defeat universal per-content approval |
| [EPI-CLM-standard-enforcement](#epi-clm-standard-enforcement) | see record | SRC-1, `_config/standard.md`; doctrine/design | Required fields plus lint recipe | [EPI-RTE-metadata-transform](#epi-rte-metadata-transform) converts text, does not validate | None supplied | No compliance experiment; lint tests only type-field presence in limited roots | A requested metadata convention and partial check | “Always enforced” and missing-field coverage exceed specified check |
| [EPI-CLM-decision-learning](#epi-clm-decision-learning) | see record | SRC-1, `_meta/instructions/knowledge-query.md`; doctrine/design | Outcome template and proactive precedent query | None in target; see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | None supplied | Outcomes alone do not establish explanation, transfer or improvement | Prescribed future use of operational experience | Improved capacity, causal attribution and actual decision dependence unknown |
| [EPI-CLM-knowledge-memory](#epi-clm-knowledge-memory) | see record | SRC-1, `PHILOSOPHY.md`; doctrine/design | Capture, completion, querying and evolution guidance | Converter only supplies bounded file maintenance | None supplied | No authentic update/consumer trace or causal comparison | Durable text supports a prescribed institutional-memory and adaptation path | Accuracy, complete retention, instant retrieval and successful improvement not demonstrated |

## Bounded conclusion

**Acquisition and retention:** see [RT-RTE-capture-file](runtime.md#rt-rte-capture-file), [EPI-OBJ-sources](#epi-obj-sources) and [EPI-OBJ-knowledge-article](#epi-obj-knowledge-article). External statements enter drafts and extracted working copies. Source attribution records origin, not truth. Originals are selectively preserved only when enabled; the default can discard originals. Warrant preservation is unknown, while loss of auditability is a supported design risk. Later query selection can omit most files and the later sections of large files. Freshness warnings and citations do not restore omitted evidence or endorse claims.

**Production and checks:** see [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [EPI-RTE-completion-check](#epi-rte-completion-check), [EPI-RTE-lint-check](#epi-rte-lint-check) and [EPI-RTE-blog-review](#epi-rte-blog-review). Synthesis/idea reactions are candidate production, but no concrete input/output pair establishes a particular reshaping, entailed claim or non-entailed conjecture. Lint predicates can entail structural claims from correctly measured file premises; those premises and interpretations have not been observed. Blog review checks presentation. None supplies a general factual oracle. The accuracy item in completion is a counterexample to “no accuracy criterion exists,” but not evidence that such a criterion was applied against evidence.

**Disposition and integration:** see [EPI-RTE-completion-status](#epi-rte-completion-status), [EPI-RTE-completion-links](#epi-rte-completion-links), [EPI-RTE-lint-action](#epi-rte-lint-action) and [EPI-RTE-blog-publish](#epi-rte-blog-publish). Useful/findable completion is a named intended use with type-specific criteria. Prescribed checklist satisfaction permits active/complete status and final filing; related links support discovery, sometimes before status change. No supplied evidence individuates an evidence-consuming acceptance of a newly produced ampliative claim. Archive/superseded labels request changed reliance and require a reason, but query explicitly deprioritizes archived records rather than enforcing universal rejection of retired claims. Publication is an operational consequence, not epistemic acceptance. There is no supported downstream retraction guarantee.

**Behavioral use:** see [EPI-RTE-pattern-capture](#epi-rte-pattern-capture), [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) and [RT-RTE-context-review](runtime.md#rt-rte-context-review). Retained preferences, conventions and instructions request future assistant behavior through startup and task-triggered file reads. This is a behavior-shaping path even without producing a truth-apt proposition. Immediate pattern capture differs from user-approved optimization restructuring. Human override/approval is route-specific; initiating a session or capture is not approval of every sentence. No observed update-to-consumer dependence or successful improvement is established.

**Independent properties:** the optimization record supplies separately bounded theory-builder conditions and improvement objective. Whole textual guidance is addressable and persistent by design; consumption is prescribed; content-directed criticism and criticism-fed iteration remain unobserved. The decision-outcome route separately prescribes use of experience, without proving improved capacity or causal mechanism. Host model mutability is see [RT-CMP-ai-assistant](runtime.md#rt-cmp-ai-assistant), not inferred from file adaptation. These observations neither confer nor deny a single system-wide learning, reflection, autonomy or self-improvement status.

**Executable exception:** see [EPI-RTE-metadata-transform](#epi-rte-metadata-transform). Static code supports direct metadata rewrite and a concrete loss witness, not factual validation or a successful runtime migration. The converter's printed success labels cannot establish YAML fidelity, source truth or replay safety. No observed run or causal experiment closes the uncertainties above.

## Shared records

### Operative objects

#### EPI-OBJ-knowledge-article
Label: Knowledge article

Source-native identity: retained knowledge documents shaped by `_meta/templates/knowledge-article.md`, including working versions of captures/syntheses. Natural-language body and summary on Markdown/filesystem, with symbolic metadata selectors separately assessed in [EPI-OBJ-metadata](#epi-obj-metadata). These are outputs/read-back inputs of [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) and [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), not duplicates of [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules). SRC-1, doctrine/design, `_meta/templates/knowledge-article.md`:

> [Content here]
> --- `_meta/templates/knowledge-article.md`

The placeholder gives a content shape, not a completed proposition or its production provenance. Individual truth-apt claims in user documents are not determinable here.

#### EPI-OBJ-sources
Label: Preserved sources

Source-native identity: original documents moved to `_sources/`. Natural-language originals (or externally encoded PDFs) reside in files and are Git-versionable; opaque binary source content is not supplied. Distinct from working articles; no supplied operative-object counterpart after comparison with [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules). Closest route is [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). SRC-1, doctrine/design, `_sources/README.md`:

> Sources here are **immutable** - they're reference copies, not working documents
> --- `_sources/README.md`

This is requested immutability, not a filesystem invariant. Originating-source truth and full reprocessing fidelity remain unknown. The preservation default is evidenced in `_config/config.md`:

> - **Preserve Important Sources:** no
> --- `_config/config.md`

#### EPI-OBJ-decision-outcome
Label: Decision outcome

Source-native identity: the `Outcome` part of decision Markdown, natural-language reports and constraints with status/date fields, stored on filesystem. Distinct from operating instructions and generic knowledge articles; closest supplied route [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) consumes it but is not the object. SRC-1, doctrine/design, `_meta/templates/decision.md`:

> <!-- Fill this in AFTER the decision has played out — weeks or months later. -->
> <!-- This is what makes decisions compound: future decisions learn from past outcomes. -->
> --- `_meta/templates/decision.md`

> [Any constraints or failure modes you didn't anticipate that should inform future decisions?]
> --- `_meta/templates/decision.md`

No specified independent measurement, expected-answer oracle or causal comparison validates the reported outcome or its proposed lesson. Pending fields and examples do not establish any completed evaluation route.

#### EPI-OBJ-context
Label: Personal context

Source-native identity: `_config/context.md`, profile and learned conventions in `_config/config.md`. Natural-language facts/preferences stored in Markdown on filesystem; dates/phases have selector roles. These accumulated personal facts differ from the operating modules in [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); closest supplied route [RT-RTE-session-start](runtime.md#rt-rte-session-start) reloads them. SRC-1, doctrine/design, `_config/context.md`:

> **This file is populated by your AI during training.** As it learns about you, it logs personal details here so future sessions can reference them without asking again. You can also add things manually at any time.
> --- `_config/context.md`

Assertion provenance is not uniformly separated from inferred preference. Facts are truth-apt over the person/time named; instructions such as response preferences have non-truth-apt policy force.

#### EPI-OBJ-lint-report
Label: Lint report

Source-native identity: the report prescribed in knowledge lint and its logged issue counts. Natural-language findings plus symbolic counts/dates, returned in chat and summarized in `WIKI-LOG.md`; no actual report supplied. Unlike [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules), this is a requested evaluation product, not evaluator guidance. SRC-1, doctrine/design, `_meta/instructions/knowledge-lint.md`:

> After running all checks, compile a summary:
> --- `_meta/instructions/knowledge-lint.md`

#### EPI-OBJ-blog-post
Label: Blog post

Source-native identity: template-shaped blog draft, visual plan, full draft and social-post adaptation. Natural-language prose with code/data/screenshots, stored in Markdown and potentially published externally. No user instance or image semantics available. The closest supplied [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) covers general creation but not the public publishing consumer; no supplied object counterpart. SRC-1, doctrine/design, `_meta/instructions/blog-posts/instructions.md`:

> - **Code / data blocks** — real examples, not hypothetical. Readers skim for code.
> --- `_meta/instructions/blog-posts/instructions.md`

#### EPI-OBJ-metadata
Label: File metadata

Source-native identity: legacy bullet fields and YAML frontmatter in content files. Symbolic keys/status/tags/dates drive routing and format interpretation; summary/source strings carry natural-language descriptions. Filesystem storage, versionable when committed. Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); closest supplied [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate) transforms it. SRC-1, implementation, `migrate-to-yaml-frontmatter.py`:

> METADATA_LINE = re.compile(r'^- \*\*(\w+):\*\* (.*)$')
> --- `migrate-to-yaml-frontmatter.py`

### Routes

#### EPI-RTE-completion-check
Label: Completion checklist evaluation

Part of: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)

Closest supplied records: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: completion checklist evaluation, not the whole supplied invocation/container. No same-function supplied route declaration.

Assistant/user consumes drafted content and type-specific checklist → requested completion judgment. Domain: completeness, accuracy and usability for knowledge; rationale/options/owner for decisions; shipped criteria for projects. Assistant proposes, user can decline; no independent oracle or specified accuracy-evidence protocol. Open completion request, not a controlled experiment. SRC-1, doctrine/design, `_meta/instructions/definition-of-done.md`.

- Immediate return: Checklist judgment / readiness nudge
- Later read-back: inapplicable — this check itself retains no product; the disposition route can write status
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Draft content and declared type
- Invalidation or expiry: inapplicable — no durable check result expiry is specified
- Activation or effect: Requested readiness assessment; actual checking unobserved
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> Content is complete and accurate
> --- `_meta/instructions/definition-of-done.md`

#### EPI-RTE-completion-status
Label: Completion status disposition

Part of: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)

Closest supplied records: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: completion status disposition, not the whole supplied invocation/container. No same-function supplied route declaration.

Checklist judgment → active/complete status and final filing. Assistant writes through host tools; user can accept/reject nudges. Trigger is all checklist items done; admission requests useful/findable content for intended future use, not an independently recorded factual acceptance. No answer oracle. Open maintenance mode; user can edit or externally revert committed files, no automatic rollback. SRC-1, doctrine/design, `_meta/instructions/definition-of-done.md`.

- Immediate return: Status/filing response
- Later read-back: Changed status/files may reach later queries; no observed read-back
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: All checklist items judged done
- Invalidation or expiry: Status may later be changed; no universal expiry
- Activation or effect: Requested in-use/complete designation
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> When ALL checklist items are done:
> --- `_meta/instructions/definition-of-done.md`

#### EPI-RTE-completion-links
Label: Completion link integration

Part of: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)

Closest supplied records: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: completion link integration, not the whole supplied invocation/container. No same-function supplied route declaration.

Completed article → related links/proper directory, conditional on prescribed completion. Assistant selects relevant connections; user can decline filing or change links. Related links are themselves checklist items, so operational organization may precede epistemic acceptance. Intended future use is findability; no new factual oracle or autonomous acceptance engine. Open filing; edits/Git are external recovery. SRC-1, doctrine/design, `_meta/instructions/definition-of-done.md`.

- Immediate return: Connected/filed artifact
- Later read-back: Links/directories may guide later readers
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Connections exist and type-specific completion criteria
- Invalidation or expiry: Links can become broken/retired; lint requests repair
- Activation or effect: Requested navigation/integration, not observed acceptance
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> Related links added if connections exist
> --- `_meta/instructions/definition-of-done.md`

#### EPI-RTE-lint-check
Label: Lint predicate evaluation

Closest supplied records: [RT-RTE-context-review](runtime.md#rt-rte-context-review). Distinct consequential function: lint predicate evaluation, not the whole supplied invocation/container. No same-function supplied route declaration.

User lint request/cadence → assistant reads files/searches dates, metadata, links, sizes and names → seven-check report/count log. Assistant follows deterministic predicates through host tools but also interprets scope and output. User may dispute findings. Reference domain is actual file existence/text/date/line counts, not an expected factual answer. Open health check; no measured accuracy run. SRC-1, doctrine/design, `_meta/instructions/knowledge-lint.md`.

- Immediate return: Report with flags/counts
- Later read-back: Logged issue counts may be read from wiki log; no observed later effect
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Seven declared checks and root-specific scans
- Invalidation or expiry: Active age threshold 90 days; archived/superseded exempt; review marker 30 days
- Activation or effect: Requested structural evidence and recommendations
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> **How:** Read each file's first 20 lines. If no `type:` YAML frontmatter field found, flag it.
> --- `_meta/instructions/knowledge-lint.md`

Under the declared predicates, a file with `status: active`, an accurately read update date 100 days before today, and no exemption entails a stale-active flag (>90). This is a doctrine-level conditional deduction, not execution or a freshness-to-truth inference. Metadata check can pass mere `type:` presence while summary/tags/status/date are missing.

#### EPI-RTE-lint-action
Label: Lint cleanup disposition

Closest supplied records: [RT-RTE-context-review](runtime.md#rt-rte-context-review). Distinct consequential function: lint cleanup disposition, not the whole supplied invocation/container. No same-function supplied route declaration.

Lint flags → assistant recommendations or specified in-place path-format fixes; user/manual resolution for broken targets → edited/archived/linked records. Software measurements and assistant judgment propose actions; no independent factual oracle. Archive/superseded reasons follow standard. Review/update/archive can be rejected by user; no automatic restore/withdrawal cascade, committed Git edits potentially reversible. Open maintenance, triggered by flags. SRC-1, doctrine/design, `_meta/instructions/knowledge-lint.md`.

- Immediate return: Cleanup recommendation or requested edit
- Later read-back: Changed metadata/links reach later query selection; archived records generally deprioritized
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Flag category; manual resolution on broken links
- Invalidation or expiry: Terminal statuses exempt stale-active check, not removed from all retrieval
- Activation or effect: Requested cleanup and changed selection relevance
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> → Action: Convert format issues in-place; broken links need manual resolution
> --- `_meta/instructions/knowledge-lint.md`

SRC-1, `_config/standard.md`, supplies retirement reasons:

> - `superseded` — replaced by a newer file or approach. Requires `failure_reason:` explaining what replaced it.
> --- `_config/standard.md`

The downstream selection limit is SRC-1, `_meta/instructions/knowledge-query.md`:

> - Status filter: `archived` files can usually be deprioritized unless explicitly asked about history
> --- `_meta/instructions/knowledge-query.md`

#### EPI-RTE-blog-review
Label: Blog presentation review

Closest supplied records: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: blog presentation review, not the whole supplied invocation/container. No same-function supplied route declaration.

Template draft → self-review or peer review → readiness judgment. Reviewer checks visuals, screenshot accessibility/caption, keyword use and social section. User/reviewer can request revision; zero visuals prompts pushback. Domain is presentation readiness; “real examples” asks for authenticity without an evidence procedure. No factual answer oracle, open publication preparation. SRC-1, doctrine/design, `_meta/instructions/blog-posts/instructions.md`.

- Immediate return: Review/pushback
- Later read-back: inapplicable — no persisted review report or later reviewer invocation is specified
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Visual plan and publishing checklist
- Invalidation or expiry: inapplicable — no retained result expiry specified
- Activation or effect: Requested review before publishing
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> If a post has zero visual elements, push back and ask what could be added.
> --- `_meta/instructions/blog-posts/instructions.md`

#### EPI-RTE-blog-publish
Label: Blog publishing consumption

Closest supplied records: [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: blog publishing consumption, not the whole supplied invocation/container. No same-function supplied route declaration.

Reviewed draft → primary platform post → published status/date → cross-post adaptation → retained URLs. External author/assistant/platform executes; no target-owned posting client. User can stop publication; reviewer identity/mandatory human approval not specified. Published status is operational admission, not factual acceptance. Open publishing task; no rollback/unpublish procedure supplied. SRC-1, doctrine/design, `_meta/instructions/blog-posts/instructions.md`.

- Immediate return: Published/cross-posted artifact and links requested
- Later read-back: Status and URLs may be consumed by later file readers or audiences
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Publishing flow after review
- Invalidation or expiry: Dates updated and URLs tracked; no automatic withdrawal
- Activation or effect: Requested publication and tracking
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> 5. **Track** — Update the post file with the published URL and any cross-post links.
> --- `_meta/instructions/blog-posts/instructions.md`

#### EPI-RTE-pattern-capture
Label: Conversation pattern capture

Closest supplied records: [RT-RTE-session-start](runtime.md#rt-rte-session-start) and [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). Distinct consequential function: conversation pattern capture, not the whole supplied invocation/container. No same-function supplied route declaration.

Conversation-established rule/preference/detail → assistant immediate write to context/config/module → future startup/task read. Assistant identifies pattern; ask if ambiguous, user can reject or override. Direct rule edits differ from approval-gated restructuring. Trigger is explicit rule or inferred usage pattern; policy change or imported personal assertion persists as text. No required source-truth oracle. Open personal use; user edits and available Git history offer nonautomatic recovery. SRC-1, doctrine/design, `_meta/instructions/general.md`.

- Immediate return: Immediate file update requested
- Later read-back: Context/conventions/modules requested inputs to later sessions
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Established conversation pattern; ask when ambiguous
- Invalidation or expiry: User override or replacement; no general expiry
- Activation or effect: Requested durable policy/personality adaptation; no observed later dependence
- Evidence limits: Static source only; no observed host adherence, evidence-consuming acceptance or causal benefit
- design conclusion status: claimed
- operation conclusion status: uninspected

> If it's ambiguous whether something is worth capturing, ask: *"We worked out [X] — should I add that to the instructions?"* Then capture it in the same exchange, not at the end of the session.
> --- `_meta/instructions/general.md`

See [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) for later policy consumer/channel/force/horizon. Preference capture need not formulate a theory; learning benefit is uninspected. For inferred conventions, the textual unit is addressable and persistent by design, consumption is prescribed, and no content-directed criticism episode or criticism-fed iteration is supplied. No autonomous or reflective theory-builder verdict follows. This is separate from the optimization theory account in [RT-RTE-context-review](runtime.md#rt-rte-context-review).

#### EPI-RTE-metadata-transform
Label: Metadata text transformation

Part of: [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate)

Operator invokes utility → fixed regex scans/collects legacy fields → formatter builds frontmatter/title/body → direct overwrite. This is the transformation part of the supplied batch route, not a new invocation. Caller initiates mutation, code decides matches, no per-file user veto, independent oracle or expected-output comparison. Fixed batch mode. No backup/transaction; Git recovery only if available. SRC-1, implementation, `migrate-to-yaml-frontmatter.py`.

- Immediate return: Converted label after write
- Later read-back: Rewritten text becomes later reader/parser input
- Delegated visibility: inapplicable — no delegated worker is specified
- Selection predicate: Leading frontmatter skip; first H1 followed by matching bullet fields
- Invalidation or expiry: Rerun skips leading frontmatter; no semantic invalidation
- Activation or effect: Implemented direct overwrite, not executed
- Evidence limits: Static source only; no target execution or comparator; semantic preservation not guaranteed
- implementation conclusion status: wired
- operation conclusion status: uninspected

>     body_lines = lines[i:]
> --- `migrate-to-yaml-frontmatter.py`

Static concrete witness, not a target fixture or execution: input `Caution: obsolete instructions.\n# Guide\n\n- **Type:** knowledge\n- **Summary:** yes\n\n---\n\nBody.\n`. `title_index` selects `# Guide`; the metadata regex collects type and summary; `body_lines` starts after the separator; the builder emits `---\ntype: knowledge\nsummary: yes\n---\n\n# Guide\n\nBody.\n`. The pre-title caution is lost. An unquoted `summary: yes` is also not forced to remain a string for all YAML consumers. The direct write return merely says converted. This refutes universal lossless reshaping; it does not establish an ampliative conjecture. For well-formed restricted inputs the utility may only reshape, but the general edge is indeterminate without a checked source/consumer domain. Duplicate field names additionally overwrite earlier values in the dict. SRC-1, implementation:

>             fields[m.group(1).lower()] = m.group(2).strip()
> --- `migrate-to-yaml-frontmatter.py`

>     title_line = lines[title_index]
>     new_content = '\n'.join(yaml) + '\n\n' + title_line + '\n'
> --- `migrate-to-yaml-frontmatter.py`

No supersession of the supplied migration container is needed: its warning about leading material and absence of validation is consistent with this narrower transformation record.

### Claims

#### EPI-CLM-decision-learning
Label: Decision experience learning

Claimed operation: outcome-bearing past decisions become operational experience that informs later choices. Closest supplied route [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) describes delivery, but no supplied claim record declares this learning assertion. SRC-1, doctrine/design, `_meta/instructions/knowledge-query.md`:

> The system doesn't just remember what you decided — it learns from how those decisions played out. Over time, your decision records become operational experience, not just documentation.
> --- `_meta/instructions/knowledge-query.md`

Supported scope: requested precedent consumption. Learned capacity and causal benefit uninspected; outcome success does not validate a mechanism or its transfer.

#### EPI-CLM-standard-enforcement
Label: Universal metadata enforcement

Claimed operation: every content file has required Tier 1 fields and lint flags missing fields. Distinct from [RT-CLM-review-policy](runtime.md#rt-clm-review-policy), which concerns review, not schema enforcement; closest supplied migration route warns it is no validator. SRC-1, doctrine/design, `_config/standard.md`:

> **Tier 1 — Universal (always enforced)**
> Required on every content file. Non-negotiable. Lint will flag missing Tier 1 fields.
> --- `_config/standard.md`

Specified lint scope and `type:` presence test in [EPI-RTE-lint-check](#epi-rte-lint-check) are insufficient for that universal guarantee. This elaborates, rather than supersedes, the supplied runtime account's metadata warning.

#### EPI-CLM-knowledge-memory
Label: Institutional knowledge memory

Claimed operation: captures/processes persist and are queryable, while usage improves the system and prior decisions inform future ones. Closest supplied [RT-CLM-review-policy](runtime.md#rt-clm-review-policy) concerns admission only; this distinct claim describes persistent knowledge/use/adaptation. SRC-1, doctrine/design, `PHILOSOPHY.md`:

> - Past decisions inform future decisions (precedent chain)
> - Patterns emerge across journal entries and knowledge articles
> - Stale content gets surfaced automatically (lint)
> - The system improves as you use it (training period)
> --- `PHILOSOPHY.md`

> - Processes are captured once and queryable forever
> --- `PHILOSOPHY.md`

Prompt paths support intended persistence/consumption, not universal retention or factual correctness. The “automatically” lint wording does not supply a scheduler; startup checks old inbox items but full lint is request/cadence guidance. No causal improvement or infinite retention evidence is supplied. Completion's useful/findable criterion and accuracy requirement limit reliance as requested policy, not demonstrated acceptance.

### Behavioral-authority paths

none declared in this member; see [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) and the ledger's route-specific consumers.
