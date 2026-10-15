---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Interview Doc Agent's factual-content, reliance and checking routes in its prompt-operated experience library."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
---

# Interview Doc Agent epistemic report

## Source-and-claim boundary

The question is how personal records become reusable factual sources for resumes and interview narratives, and what licenses reliance on the resulting facts, explanations and job-fit judgments. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities and layers: see the [Source register](boundary.md#source-register). All findings below use SRC-1's doctrine/design layer. The target is a shipped instruction-and-document artifact; its external hosts supply model computation and tools. A route described in instructions is therefore `doctrine only`, not an inspected implementation of model behavior.

Direct source inspection covered every tracked file at the frozen commit, independently checking the runtime's route list for additional material operations. There is no shipped CLI dispatcher, hook registry, tool implementation or executable evaluator to trace. The entry points are host-loaded skill text and user requests. Host internals, provider state, actual personal records, generated outputs, execution traces and experiments are not supplied. These limits prevent conclusions about actual factual fidelity, successful retrieval, accepted claims, activation, privacy and causal benefit; they do not erase the declared maintenance and reuse routes.

| Entry point or operation | Source path, SRC-1 | Coverage and record citations | Inspection basis / limit |
|---|---|---|---|
| Load skill; initialize | `SKILL.md`, `README.md`, `docs/02-安装-obsidian.md` | [RT-OBJ-skill](runtime.md#rt-obj-skill), [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace) | Direct full reads plus supplied runtime; empty schemas introduce no personal factual warrant. Host loading is uninspected. |
| Admit raw records; consolidate; update indexes | `materials/README.md`, `SKILL.md`, `docs/04-使用指南.md` | [EPI-OBJ-materials](#epi-obj-materials), [EPI-OBJ-experience-library](#epi-obj-experience-library), [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) | Direct full reads plus runtime; no real before/after pair. |
| Select dossiers and reread raw detail | `wiki/index.md`, `经历库/00-个人档案.模板.md`, `docs/01-理念-karpathy-wiki.md`, `SKILL.md` | [EPI-OBJ-wiki-index](#epi-obj-wiki-index), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) | Direct full reads plus runtime; selective reading and optional whole-library reading are both described. |
| Resume/script generation; optional LaTeX update | `templates/简历/简历模板.示例.md`, `templates/逐字稿/产品面试话术模版.示例.md`, `SKILL.md`, `output/.gitkeep` | [EPI-OBJ-style-templates](#epi-obj-style-templates), [EPI-OBJ-output-documents](#epi-obj-output-documents), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) | Direct full reads plus runtime; empty output placeholder, not a generated result. No compiler supplied. |
| JD matching | `jd/README.md`, `SKILL.md` | [EPI-OBJ-job-description](#epi-obj-job-description), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) | Direct full reads plus runtime; no scored or externally judged matching instance. |
| Missing-number policy; fictional example | `SKILL.md`, `经历库/01-示例经历.md`, `wiki/index.md` | [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), [EPI-ABS-content-check](#epi-abs-content-check) | Direct full reads; example warning is a countercase to treating dossier placement as authenticity. |
| Cloud write; manual copy; cross-platform copying | `docs/03-接入-飞书.md` | [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback) | Direct full read plus runtime; permissions and retrieval transformations are host-dependent. |
| Public warrant claims | `README.md`, `docs/01-理念-karpathy-wiki.md`, `docs/04-使用指南.md`, `docs/02-安装-obsidian.md` | [EPI-CLM-source-consistency](#epi-clm-source-consistency), [EPI-CLM-retrieval-reliability](#epi-clm-retrieval-reliability), [RT-CLM-local-privacy](runtime.md#rt-clm-local-privacy) | Direct full reads; declarations, not experiments. |
| Distribution and ignore settings | `LICENSE`, `.gitignore` | [RT-CLM-local-privacy](runtime.md#rt-clm-local-privacy) | Direct full reads; license is not factual evaluation, commented privacy patterns are not active controls. |

The knowledge/warrant claims are numeric fidelity, common-source consistency and context-mode retrieval reliability, cited above. Privacy is a consequential deployment claim but not a truth-checking route. External linked Karpathy/RAG/context-window claims are retained only as the project's attributed rationale, not independently established facts. No included material operation remains deliberately unassessed; opaque external execution prevents a broader negative about host capabilities.

## Epistemic-object inventory

Object identity, form and substrate are owned by the cited records, not inferred from the directory names.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-materials](#epi-obj-materials) | Personal events, dates, responsibilities, measurements and explanations | see record | SRC-1, `materials/README.md` | Input assertions; authenticity and completeness unknown. |
| [EPI-OBJ-experience-library](#epi-obj-experience-library) | Profile facts, project results, why/how accounts, persona strengths | see record | SRC-1, `经历库/01-示例经历.md`, `经历库/00-个人档案.模板.md` | Sample is fictional; real transformations and claim-level lineage unavailable. |
| [EPI-OBJ-wiki-index](#epi-obj-wiki-index) | Dossier locations, topic labels and quick-access summaries | see record | SRC-1, `wiki/index.md` | Locator authority differs from factual endorsement; link validity is not checked by shipped code. |
| [EPI-OBJ-job-description](#epi-obj-job-description) | Asserted role requirements | see record | SRC-1, `jd/README.md` | Acquisition of employer/user text, not verification of requirements or candidate fitness. |
| [EPI-OBJ-style-templates](#epi-obj-style-templates) | Illustrative factual/causal statements inside a largely prescriptive scaffold | see record | SRC-1, `templates/逐字稿/产品面试话术模版.示例.md` | Examples are style guidance, not evidence of this user's accomplishments. |
| [EPI-OBJ-output-documents](#epi-obj-output-documents) | User accomplishments, project explanations and job-fit assertions | see record | SRC-1, `SKILL.md` | Intended products only; no populated output or acceptance trace. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Predominantly procedural policy; its fidelity prescriptions are not factual evidence | see record | SRC-1, `SKILL.md` | Requested constraints do not show compliance. |
| [RT-CMP-host-ai](runtime.md#rt-cmp-host-ai) | Not determinable from accessible parametric state | see record | SRC-1, `SKILL.md` | Exact model, weights and mutable endpoint behavior remain uninspected; no parametric epistemic verdict follows. |

## Authority-route ledger

Each entry assesses a consequential function separately. Repeated citations identify functions within the same supplied container route, not newly declared duplicate routes. Immediate returns, later read-back, selectors and route owners: see the cited route records. No observed-run or causal layer is available.

Route ID: [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-materials](#epi-obj-materials) → [EPI-OBJ-experience-library](#epi-obj-experience-library)
Content/update relation: truth-apt transformation: acquisition/import. User-supplied assertions enter the retained dossier workflow; source warrant is unknown. For the subsequent extraction/rewrite edge, truth-apt transformation: indeterminate: reorganization is requested, but semantic preservation and newly supplied explanations cannot be established without an input/output pair.
Transition or check target: raw personal assertions to structured dossier statements.
Evaluator/condition and domain: host model applying extraction instructions; not an independent truth evaluator. Domain is personal-experience narration.
Activation and timing: see route.
Possible or observed result: see route; requested why/how and numerical preservation are not observed transformations.
Implemented force: no implementation inspected; prescribed procedural guidance.
Epistemic authority and scope: dossier is designated the primary source for later job documents, without an evidence-consuming acceptance decision.
Operational authority: proposed dossier content may be written directly and indexed.
Behavioral-authority path: see [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions); dossier text additionally becomes factual context for later generation.
Evidence source ID and local anchor: SRC-1, `SKILL.md`, `materials/README.md`; see route's passages.
Claim IDs: [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), [EPI-CLM-source-consistency](#epi-clm-source-consistency).
Mismatch marker: designated source is not established accepted knowledge.
Gap/limit: factual extraction may preserve assertions, omit qualifiers or add explanations; no trace decides among these alternatives. Failure to prove entailment does not establish ampliative conjecture.

Route ID: [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-experience-library](#epi-obj-experience-library), [EPI-OBJ-wiki-index](#epi-obj-wiki-index)
Content/update relation: no content change at the persistence edge; transformation is assessed above.
Transition or check target: proposed dossiers and indexes to persistent files/pages.
Evaluator/condition and domain: model-controlled admission in local mode; host permissions govern physical writes, not factual truth.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: no persistence implementation inspected; durable writes requested.
Epistemic authority and scope: retained candidate assertions are designated reusable sources; no acceptance criterion or independent endorsement is recorded.
Operational authority: future generation is directed to reuse the stored content.
Behavioral-authority path: later host model reads selected dossiers via profile/wiki locators; factual-context force; horizon is future document requests if writes and reloads succeed.
Evidence source ID and local anchor: SRC-1, `SKILL.md`; see route.
Claim IDs: [EPI-CLM-source-consistency](#epi-clm-source-consistency).
Mismatch marker: retention before acceptance, not lifecycle integration.
Gap/limit: no transactions, evidential provenance links, conflicting-source resolution or successful later activation supplied.

Route ID: [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience)
Route function: lineage/freshness/recovery
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-materials](#epi-obj-materials), [EPI-OBJ-experience-library](#epi-obj-experience-library), [EPI-OBJ-wiki-index](#epi-obj-wiki-index)
Content/update relation: truth-apt transformation: indeterminate. An edited source triggers another extraction, not a verified claim-preserving update.
Transition or check target: user-noticed source changes to revised dossiers and two indexes.
Evaluator/condition and domain: user initiates refresh; model interprets new materials. No stale-fact or withdrawal evaluator specified.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: no implementation inspected; request-driven update policy.
Epistemic authority and scope: refreshed text is not thereby endorsed or more accurate.
Operational authority: a successful overwrite would change the factual context of later generation; no prescribed regeneration of already issued outputs.
Behavioral-authority path: later dossier/index reads by host model; contextual force; future requests only.
Evidence source ID and local anchor: SRC-1, `SKILL.md`, `docs/04-使用指南.md`.
Claim IDs: [EPI-CLM-source-consistency](#epi-clm-source-consistency).
Mismatch marker: common-source updates do not withdraw older output assertions.
Gap/limit: no explicit rejection, deletion, supersession or rollback procedure found in the inspected instructions.

Route ID: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-index](#epi-obj-wiki-index), [EPI-OBJ-experience-library](#epi-obj-experience-library), [EPI-OBJ-job-description](#epi-obj-job-description), [EPI-OBJ-style-templates](#epi-obj-style-templates)
Content/update relation: no content change at the selection edge. Optional JD reading acquires externally asserted requirements with unknown source warrant.
Transition or check target: relevance to requested project/document and optional JD capability requirements, not truth of accomplishments.
Evaluator/condition and domain: host model's natural-language matching; no answer oracle or measured recall reference. Domain is relevance within a personal library.
Activation and timing: see route.
Possible or observed result: see route; selected complete dossiers, templates and optional raw details are intended context.
Implemented force: no implementation inspected; selection/ranking guidance.
Epistemic authority and scope: establishes a proposed relevance choice, not completeness or authenticity.
Operational authority: model selects what it will read, emphasize or omit before output generation.
Behavioral-authority path: index/profile/JD text → host model selection → selected dossier/template context; ranking and contextual force; current document request.
Evidence source ID and local anchor: SRC-1, `wiki/index.md`, `SKILL.md`, `docs/01-理念-karpathy-wiki.md`; see route and [EPI-CLM-retrieval-reliability](#epi-clm-retrieval-reliability).
Claim IDs: [EPI-CLM-retrieval-reliability](#epi-clm-retrieval-reliability).
Mismatch marker: fitting in a possible context window is not actual delivery of all relevant facts.
Gap/limit: index omission, mismatching and host delivery remain possible; raw fallback and reading the entire small library qualify any exclusive-index claim.

Route ID: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-experience-library](#epi-obj-experience-library) → [EPI-OBJ-output-documents](#epi-obj-output-documents)
Content/update relation: truth-apt transformation: indeterminate. Reordering/cutting/reformatting would be non-ampliative reshaping if meaning is preserved. Claimed causal explanations, persona summaries and fit assertions could be newly inferred; no instance establishes entailment or non-entailment.
Transition or check target: factual context and style scaffolds to concise bullets or narrative explanations.
Evaluator/condition and domain: host model following writing methods and numerical policy; domain is job-document composition, not an external measurement of past events.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: no implementation inspected; requested writing and withholding policy. The missing-number instruction requests `___` and a user reminder rather than inventing a measurement.
Epistemic authority and scope: outputs carry source-derived asserted facts at best; placeholders explicitly withhold a number. No checked derivation or accepted ampliative result is established.
Operational authority: output drafting/writing proceeds without a mandatory per-document factual approval gate.
Behavioral-authority path: see [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions); template and dossier text guide host output; requested procedural/contextual force; current request, then human use.
Evidence source ID and local anchor: SRC-1, `SKILL.md`, `templates/逐字稿/产品面试话术模版.示例.md`; see [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity).
Claim IDs: [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), [EPI-CLM-source-consistency](#epi-clm-source-consistency).
Mismatch marker: a narrative explaining why a project worked is not a checked causal mechanism.
Gap/limit: policy requires recognizing genuine/missing data but specifies no separate comparison result, verifier or authenticating evidence.

Route ID: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-output-documents](#epi-obj-output-documents)
Content/update relation: no content change at output storage.
Transition or check target: draft to saved output, optionally updated LaTeX text.
Evaluator/condition and domain: host tool permissions, not truth evaluation; human may subsequently refine.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: no implementation inspected; requested output placement.
Epistemic authority and scope: saving does not certify facts or job suitability.
Operational authority: human can open, edit and use the document in job applications/interviews.
Behavioral-authority path: saved output/conversation text → human; advisory artifact; subsequent use chosen by human. No route promotes output into future skill instructions.
Evidence source ID and local anchor: SRC-1, `docs/04-使用指南.md`, `SKILL.md`.
Claim IDs: [EPI-CLM-source-consistency](#epi-clm-source-consistency).
Mismatch marker: retention is not acceptance or lifecycle integration.
Gap/limit: no acceptance record or output-use observation.

Route ID: [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-experience-library](#epi-obj-experience-library), [EPI-OBJ-output-documents](#epi-obj-output-documents)
Content/update relation: no content change specified at writeback; copy/transmission fidelity is unknown.
Transition or check target: permission to persist a cloud page, or user's manual copying of returned text.
Evaluator/condition and domain: host permission/version condition; human can decline or edit manual copying. These evaluate write ability/choice, not factual truth against a named criterion.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: no cloud implementation inspected; conditional write/manual fallback.
Epistemic authority and scope: neither permitted writes nor manual copies establish acceptance.
Operational authority: denied write changes delivery to conversation text; human controls fallback persistence.
Behavioral-authority path: assistant text → cloud tools if allowed, otherwise human → cloud page; permissive gate/manual admission; immediate write and later knowledge-page reuse if persisted.
Evidence source ID and local anchor: SRC-1, `docs/03-接入-飞书.md`; see route.
Claim IDs: none.
Mismatch marker: human-in-the-loop copying is not a specified evidence-consuming review.
Gap/limit: host retrieval and copy transformations are uninspected; no cloud lineage guarantee.

There is no separate evidence-producing truth check, recorded acceptance decision or post-acceptance lifecycle integration route within the inspected artifact: see [EPI-ABS-content-check](#epi-abs-content-check). The ledger therefore does not invent those functions or evaluators. Numeric withholding remains a real declared constraint despite this absence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support / limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity) | see record | SRC-1, `SKILL.md`; doctrine/design | Preserve numbers; placeholders/reminders | None inspected; [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) are doctrine | None supplied | No intervention/comparison | Explicit anti-fabrication policy, not an oracle | Fictional starter content, extraction and rewriting require faithful interpretation. |
| [EPI-CLM-source-consistency](#epi-clm-source-consistency) | see record | SRC-1, `README.md`, `docs/04-使用指南.md`; doctrine/design | Common primary dossier source | None inspected; same two declared routes | None supplied | No cross-output comparison | Reuse can align source selection | Does not establish perpetual agreement, source truth or preserved qualifiers. |
| [EPI-CLM-retrieval-reliability](#epi-clm-retrieval-reliability) | see record | SRC-1, `docs/01-理念-karpathy-wiki.md`; doctrine/design | Complete Markdown files, small library, optional index | None inspected; [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) is doctrine | None supplied | No recall, accuracy or RAG contrast | Non-vector full-file selection is declared | Selective reads contradict the premise that every fact is necessarily in view; 100% reliability is unwarranted. |
| [RT-CLM-local-privacy](runtime.md#rt-clm-local-privacy) | see record | SRC-1, `docs/02-安装-obsidian.md`; doctrine/design | Local file placement | None inspected; external host transport excluded | None supplied | No traffic or provider evidence | Local storage layout only | Local I/O does not determine model transmission; cloud branch is explicitly different. |

## Bounded conclusion

The system acquires personal assertions and JD requirements with unknown source warrant. It requests structured dossiers and two indexes, then later uses selected retained dossier text as factual context. It also requests compression, rewriting, why/how explanations and job-fit emphasis. No populated input/output pair determines whether those transformations merely reshape, entail new propositions or introduce non-entailed conjectures. No checked derivation from warranted premises is established. The fictional dossier is evidence of an available example, not an observed knowledge-production episode.

There are genuine declared constraints: preserve all quantities, use real dossier data, and withhold missing measurements using placeholders and reminders. These constrain requested generation but do not authenticate source numbers or produce independently consumed check results. In the fully read shipped artifact, no evidence-consuming acceptance decision names criterion, intended use and scope. Direct retention and later use therefore precede any established acceptance; index maintenance is not post-acceptance integration. Human source provision, later edits and manual cloud copying can change content but are not prescribed factual-review decisions.

Operational authority is clearer than epistemic warrant. The model is directed to select, write and reuse candidates; the cloud permission branch can block writes, while its manual fallback gives the user control over persistence. Dossiers and templates shape generation through natural-language context. Changed material can trigger a user-requested refresh, but no explicit withdrawal of issued outputs or checked conflict-resolution procedure is supplied. This limits the common-source and perpetual-alignment claims.

The small-library/full-file rationale supports a declared alternative to vector chunk retrieval, not guaranteed relevance recall, global information delivery or precise inference. Neither provider parameters nor successful route activation are inspectable here. Reusable records and narrative reasoning do not by themselves establish learning, content-directed theory criticism, autonomous theory building or self-improvement; no performance-fed method revision is described. These are independent unestablished properties, not a single adverse system verdict. No target execution was performed.

## Shared records

### Operative objects

#### EPI-OBJ-materials
Label: Raw materials

Identity: user-supplied project records in materials/, including retrospectives, PRD fragments, weekly reports, chats and informal numerical notes. Representational form: natural-language asserted experience content, with textual quantities. Storage substrate: local files or adapted cloud pages. Claimed role: raw input and detail fallback. Compared with [RT-OBJ-skill](runtime.md#rt-obj-skill), this is distinct factual input, not procedural guidance; [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) consumes it but does not declare its object. No supplied object counterpart. Evidence: SRC-1, `materials/README.md`.

> - 项目复盘文档、PRD 片段、工作周报
> - 聊天记录、脑暴笔记、随手记的数据
> --- `materials/README.md`

These assertions can be true or false over a named person's project, but the artifact supplies no authentication or source-quality criterion.

#### EPI-OBJ-experience-library
Label: Experience library

Identity: retained project dossiers plus personal-profile factual/persona fields; the profile's locator entries belong to the index object below. Representational form: natural-language facts, causal accounts and strengths. Storage substrate: Markdown files under 经历库/, or cloud pages/Base records. Claimed role: primary factual source for output. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill); [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) produces this intended content, and [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) consumes it. No supplied object counterpart. Evidence: SRC-1, `SKILL.md`, `经历库/01-示例经历.md`, `经历库/00-个人档案.模板.md`.

> - 手段的 why + how（逻辑 + 具体动作：触发时机/面向谁/展示什么）
> - 判断力与人设亮点
> --- `SKILL.md`

> - 逻辑（why）：xx 的根因是 xx
> --- `经历库/01-示例经历.md`

> 这是一篇**示例经历档案**，展示经历库该长什么样。数据为虚构演示。
> --- `经历库/01-示例经历.md`

The causal slot calls for a proposition, not merely storage formatting. The fictional-data warning defeats any inference that dossier membership alone certifies truth. Real lineage and actual inferential novelty remain unknown.

#### EPI-OBJ-wiki-index
Label: Wiki index

Identity: wiki/index.md's file-location/topic table and personal-profile dossier locator entries. Representational form: natural-language labels and path strings interpreted by the host model; no shipped fixed-rule path consumer. Storage substrate: Markdown or adapted cloud lookup content. Claimed role: select dossiers/templates before full reads. Distinct from factual/persona dossier fields and [RT-OBJ-skill](runtime.md#rt-obj-skill); [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) names the read but does not declare this object. No supplied object counterpart. Evidence: SRC-1, `wiki/index.md`, `经历库/00-个人档案.模板.md`.

> 轻量定位表（Karpathy LLM Wiki 的 Index 层）。AI 生成时先看这张表，按需求挑出要读的经历库档案和模板，不必全读 → 省 token。
> --- `wiki/index.md`

Index summaries can affect which factual sources enter the current context; their inclusion is not evidence of endorsement. The shipped table explicitly marks the example for replacement.

#### EPI-OBJ-job-description
Label: Job description

Identity: per-role user-provided job description in jd/. Representational form: natural-language role requirements. Storage substrate: local text files, with cloud adaptation host-dependent. Claimed role: capability matching and emphasis guidance. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill) and factual dossiers; closest route is [RT-RTE-generate-document](runtime.md#rt-rte-generate-document). No supplied object counterpart. Evidence: SRC-1, `jd/README.md`.

> 1. 读 JD，提取岗位要求的能力点
> 2. 从你的经历库里挑出最相关的经历，突出对应数据
> 3. 弱化无关项，生成定制版简历或逐字稿
> --- `jd/README.md`

Requirements guide relevance, not independent evaluation of factual accuracy or demonstrated role fitness.

#### EPI-OBJ-style-templates
Label: Style templates

Identity: resume and interview-script example templates. Representational form: natural-language writing scaffolds, example assertions and placeholders; formatting has no inspected executable consumer. Storage substrate: templates/ Markdown, optional user-supplied LaTeX. Claimed role: writing structure and style, not user-fact evidence. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill); closest route [RT-RTE-generate-document](runtime.md#rt-rte-generate-document). No supplied object counterpart. Evidence: SRC-1, `templates/简历/简历模板.示例.md`, `templates/逐字稿/产品面试话术模版.示例.md`.

> 这是一份示例简历模板，展示结构和写法。把内容换成你自己的即可。
> --- `templates/简历/简历模板.示例.md`

> **（此环节需要结合项目定制，案例仅参考框架）**
> --- `templates/逐字稿/产品面试话术模版.示例.md`

The warnings qualify any inference that illustrative market explanations or achievements are usable facts about the user. No example-filter implementation is supplied.

#### EPI-OBJ-output-documents
Label: Output documents

Identity: requested resume, interview scripts and tailored variants, not an observed populated artifact. Representational form: natural-language accomplishment/fit assertions, with optional LaTeX formatting. Storage substrate: output/ files, cloud documents or conversation text. Claimed role: human-used job products. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill) and the retained dossier source; closest route [RT-RTE-generate-document](runtime.md#rt-rte-generate-document). No supplied object counterpart. Evidence: SRC-1, `SKILL.md`, `docs/04-使用指南.md`.

> ④ 取用     产出在 output/，按需微调
> --- `docs/04-使用指南.md`

No output artifact establishes production, checking, acceptance or actual use. The empty tracked placeholder carries none of those conclusions.

### Claims

#### EPI-CLM-source-consistency
Label: Source consistency

Claimed operation: all generated variants share a single trusted experience source, hence their data always align. Source: SRC-1, `README.md`, `docs/04-使用指南.md`. This overlaps [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity) but is distinct: an across-output guarantee derived from shared source selection, not the instruction to preserve genuine quantities and mark missing ones.

> 生成时先读 `wiki/index.md` 索引定位，**只读相关的 1-2 篇经历**，不必每次重喂全部资料 → 省 token；所有产出同源 → 数据永远对齐。
> --- `README.md`

> - **经历库是单一可信源**：简历、逐字稿、定制版都从它生成，数据永远对齐
> --- `docs/04-使用指南.md`

Common-source doctrine supports intended reuse, not truth or an agreement invariant; semantic rewriting, raw detail fallback, updates and user edits are relevant countercases.

#### EPI-CLM-retrieval-reliability
Label: Retrieval reliability

Claimed operation: context-mode access gives 100% retrieval reliability and more precise global inference. Source: SRC-1, `docs/01-理念-karpathy-wiki.md`. No counterpart after comparison with [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity) and [RT-CLM-local-privacy](runtime.md#rt-clm-local-privacy); closest route is [RT-RTE-generate-document](runtime.md#rt-rte-generate-document), which already distinguishes selection from isolation.

> - **检索可靠性 100%**：所有信息都在 AI「视线」内，不会出现 RAG「没匹配到相关片段」或「分块切断语义」的问题
> --- `docs/01-理念-karpathy-wiki.md`

> - **推理更精准**：AI 能对全局信息直接推理（多跳推理、跨经历总结），而不只是基于检索到的几个孤立片段
> --- `docs/01-理念-karpathy-wiki.md`

> 即便把整个经历库全读进去也放得下，索引只是让它更省而已。
> --- `docs/01-理念-karpathy-wiki.md`

Full-library feasibility is different from actual full-library delivery; the prescribed selective-read path supplies a countercase to the all-information-in-view premise. No model-window test, retrieval reference set or comparative experiment licenses the percentage or accuracy claim.

### Evidenced absences

#### EPI-ABS-content-check
Label: Content checking

- doctrine conclusion status: absent

Searched boundary: every tracked file of SRC-1 at 6ebfe9aba989d7949dadea0fc4af6fb64892c6aa, especially SKILL.md, all docs, materials/JD instructions, both templates, wiki index and both dossier/profile examples. Query: full-file inspection for a separate numerical/provenance comparison, check result, acceptance criterion, rejecting consumer, withdrawal procedure or post-acceptance integration. The tracked tree contains no executable evaluator, tests, CLI dispatcher, hooks or registered tools. External hosts are excluded; this is not a negative about their facilities.

Compared with [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity) and [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience), this is a bounded absence finding, not a duplicate policy or maintenance route. Missing-data withholding and optional human edits remain positive declared controls. Source evidence: SRC-1, `SKILL.md`, `docs/04-使用指南.md`, `docs/03-接入-飞书.md`; full-tree inspection supplies the negative, while these passages establish the policy and direct-write workflow that must not be mistaken for evaluation.

> - 绝不编造数据；真实数据缺失时用 `___` 占位并提醒用户补充
> --- `SKILL.md`

> 用户新增/修改 materials/ 原始素材后：读新文件 → 提炼整合进 `经历库/` 对应档案 → 更新 `00-个人档案.md` 索引和 `wiki/index.md` 检索表。
> --- `SKILL.md`

Conclusion supported: no separate evidence-producing truth check or evidence-consuming acceptance decision is declared or implemented within this shipped artifact; consequently no established acceptance-to-integration path. Prevented conclusion: do not claim the model cannot privately compare facts, the human never reviews them, or the host supplies no additional evaluator. No run evidence decides those possibilities.
