---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Interview Doc Agent's user-fed dossier memory, two lookup indexes and instruction-directed read-back, including permission-dependent cloud persistence."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
source-identity: "https://github.com/Shilren/interview-doc-agent"
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
---

# Interview Doc Agent memory report

## Boundary and evidence

The memory boundary includes user-supplied raw materials, model-organized project dossiers, personal profile, lookup index, templates, job descriptions and generated documents. It includes their initialization, update, selection, local persistence and described cloud alternatives. All conclusions concern SRC-1's doctrine/design layer at the frozen revision. These are inspected instructions and starter artifacts, not executable memory machinery or observed personal memory.

Direct reads covered `SKILL.md`, `README.md`, all four `docs/` tutorials, `materials/README.md`, `jd/README.md`, `wiki/index.md`, both shipped experience-library files, both templates and `.gitignore`. The supplied [boundary](boundary.md#source-register) establishes the complete tracked tree and source identity; the supplied runtime establishes provisional routes. Direct reads confirm those routes and supply the object distinctions below. No target code, CLI dispatch, hooks, registered tool implementation, evaluator or library/service implementation occurs in this tracked prompt-and-document artifact. Named host and lark tools are external affordances, not frozen implementations. `LICENSE` and the empty `output/.gitkeep` add no memory behavior; their presence comes from the boundary and checked tree inventory.

External host context, provider state, embedding/retrieval machinery, permissions, synchronization and model internals remain outside the inspected source. This prevents statements about actual context occupancy, cloud retrieval fidelity, durable write success or cross-session activation. No real inputs, outputs, traces or experiments were supplied. Static examples are not evidence of the raw-to-derived transformation having run.

| Entry point / operation | Source paths (SRC-1) | Coverage / records | Limits and prevented conclusions |
|---|---|---|---|
| Load skill, initialize missing layout | `SKILL.md`, `README.md`, `docs/02-安装-obsidian.md` | Direct reads; [RT-OBJ-skill](runtime.md#rt-obj-skill), [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace); annotations below | Host resolves root and performs writes; partial initialization recovery is unspecified. |
| Admit original experience | `materials/README.md`, `docs/01-理念-karpathy-wiki.md`, `SKILL.md` | Direct reads; [MEM-OBJ-materials](#mem-obj-materials) | Human supplies content; origin/authenticity and subsequent edits are not verified. |
| Consolidate / revise project memory | `SKILL.md`, `经历库/01-示例经历.md`, `docs/04-使用指南.md` | Direct reads; [MEM-OBJ-experience-dossiers](#mem-obj-experience-dossiers), [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) | Model admission under prose standards; no observed completeness or automatic invalidation. |
| Maintain two access surfaces | `经历库/00-个人档案.模板.md`, `wiki/index.md`, `SKILL.md` | Direct reads; [MEM-OBJ-personal-profile](#mem-obj-personal-profile), [MEM-OBJ-wiki-index](#mem-obj-wiki-index) | No atomic update, stale-pointer check or reconciliation procedure is supplied. |
| Ordinary selective dossier read and missing-detail fallback | `SKILL.md`, `wiki/index.md`, `docs/01-理念-karpathy-wiki.md` | Direct reads; [RT-RTE-generate-document](runtime.md#rt-rte-generate-document), [MEM-BAP-dossier-context](#mem-bap-dossier-context) | No fixed context budget, forced exclusion, compaction or observed selector accuracy. |
| Style/template input, replacement, optional default | `templates/简历/简历模板.示例.md`, `templates/逐字稿/产品面试话术模版.示例.md`, `README.md`, `SKILL.md` | Direct reads; [MEM-OBJ-templates](#mem-obj-templates), [MEM-BAP-template-guidance](#mem-bap-template-guidance) | Default is mentioned but its single-file-deployment content is unspecified; filename mismatch remains. |
| JD-based selection/reordering | `jd/README.md`, `SKILL.md`, `docs/04-使用指南.md` | Direct reads; [MEM-OBJ-jd](#mem-obj-jd), generation annotation | JD is a target constraint, not factual validation or an answer oracle. |
| Persist and use generated product | `SKILL.md`, `docs/04-使用指南.md`, `wiki/index.md` | Direct reads; [MEM-OBJ-output](#mem-obj-output), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) | Human consumption is documented; no prescribed output-to-memory feedback loop. |
| Cloud automatic / human-copy admission and later knowledge lookup | `docs/03-接入-飞书.md` | Direct read; [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback), annotation | Page/Base storage is described; host selector, actual grants and synchronization are uninspected. |
| Evaluation, deletion, cleanup, rollback and trace-fed updates | `SKILL.md`, all tutorials, full tracked inventory | Direct behavioral-file reads; [MEM-ABS-memory-maintenance](#mem-abs-memory-maintenance) | No shipped protocol; manual deletion and external host behavior remain possible. |

## Core ideas

The retained unit is a whole project dossier, not a vector chunk. User records are organized once into interview-ready narrative and quick-access figures; future document requests read selected dossiers. A lightweight table supplies project/path/keyword hints. The profile is a separate mixture of factual content, persona keywords and project index. Neither index substitutes for the complete dossier at the declared generation consumer (SRC-1, `SKILL.md`, `wiki/index.md`; [MEM-OBJ-wiki-index](#mem-obj-wiki-index)).

> - **经历库**是核心：每篇档案已整理成「一句话 + 三段式 + 关键数据速取 + 人设亮点」，面试就绪
> --- `SKILL.md`

This is user-fed semantic organization, not an observed learning-from-agent-execution route. Raw inputs may include chat records and work retrospectives, but their presence does not establish that the agent's own execution traces update its instructions. The maintained artifact describes the user's experience, while the extraction policy stays in the skill (SRC-1, `materials/README.md`, `SKILL.md`; [MEM-OBJ-materials](#mem-obj-materials)).

Selection is foreground-model interpretation of a current request, optional JD, index and persona/project content. It reduces requested file reads, not storage accessibility or already-loaded conversation state. There is no fixed numerical budget or enforced one-to-two-file cap. The rationale explicitly permits reading the entire small library. Therefore “context mode” and “100% retrieval reliability” do not establish universal delivery or recall (SRC-1, `docs/01-理念-karpathy-wiki.md`; [MEM-CLM-retrieval-reliability](#mem-clm-retrieval-reliability)).

Trust is instructed rather than checked. Raw materials and dossiers carry asserted user facts; examples carry placeholders and fictional demonstration data. Templates guide expression; JD guides relevance. None supplies independent factual authentication. Missing numbers should remain placeholders, but shared storage does not enforce agreement between independently rewritten products; the raw-material fallback also makes “single trusted source” a primary-source policy rather than exclusive access (SRC-1, `SKILL.md`, `经历库/01-示例经历.md`; [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-materials
Label: materials

Identity: the user-populated `materials/` raw-input collection. Form: natural-language project records, PRD excerpts, work reports, chats, brainstorms and numeric statements; no shipped parser assigns them fixed execution semantics. Substrate: local files, ordinarily pasted Markdown; the cloud mapping proposes knowledge pages or Base records. Lineage: human-supplied external experience records, not supplied agent runs. Human chooses admission and can edit sources; the model reads them for consolidation or missing-detail lookup. Raw originals remain reachable rather than being replaced by dossiers. The rationale calls the raw layer unchanged, while the skill explicitly permits user modifications; this bounds “immutable” to the model's stated organization policy, not enforced storage immutability. Closest supplied record: [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience); distinct input object, not a duplicate route. Evidence: SRC-1, `materials/README.md`, `docs/01-理念-karpathy-wiki.md`, `SKILL.md`.

> - 聊天记录、脑暴笔记、随手记的数据
> - 复制粘贴成 `.md` 文件即可，不用整理
> --- `materials/README.md`

#### MEM-OBJ-experience-dossiers
Label: 经历库 project dossiers

Identity: per-project experience-library dossiers, illustrated by `经历库/01-示例经历.md`; excludes the separate personal profile. Form: natural-language narrative and interpreted metrics, including one-sentence summary, background judgment, problem, why/how, results, quick-access data and follow-up detail. Substrate: Markdown files; described cloud alternative is pages/Base records. Lineage: model-derived from raw experience under fixed skill standards. Local admission is the model's requested direct write, not a required per-content human approval. Manual cloud copying introduces human admission in that branch. Users may replace/edit content. Consumer: a later generation model treats selected dossier content as factual and narrative source, not general execution authorization. Reasons for the user's project choices are retained as why/how; the later script consumer is instructed to express them, whereas the resume consumer is instructed to omit reasoning. No evidence establishes preservation of the model's own derivation rationale or per-claim source pointers. Closest supplied record: [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience); distinct retained result object. Evidence: SRC-1, `SKILL.md`, `经历库/01-示例经历.md`.

> - 逻辑（why）：xx 的根因是 xx
> - 具体动作（how）：①… ②… ③…（含触发时机/面向谁/展示什么）
> - 结果：xx 指标达到 xx
> --- `经历库/01-示例经历.md`

The supplied [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) retains the fictional-example warning. Its five-star data-completeness display is demonstration text, not an evaluation result or admission check.

#### MEM-OBJ-personal-profile
Label: 00-个人档案

Identity: intended `经历库/00-个人档案.md`, shipped as `经历库/00-个人档案.模板.md`. Form: natural-language identity/career/skills facts and persona keywords, plus human/model-interpreted project references. Substrate: Markdown or adapted knowledge page. Lineage: initialization creates an empty template; users replace placeholders with real information; consolidation updates its project index. The initial allocation of each biographical field between user and model is unspecified. Subsequent index updating is explicitly model-directed. Consumer: resume/self-introduction generation uses biography; JD matching uses persona keywords; index aids project lookup. It is both content and access metadata, not only a pointer list. Closest supplied records: [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace) and [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience); distinct persistent object, no duplicate declaration. Evidence: SRC-1, `经历库/00-个人档案.模板.md`, `SKILL.md`.

> ## 人设关键词（自我介绍 / JD 匹配可用）
> - **复合背景**：xx + xx → xx 视角
> - **经验跨度**：xx + xx + xx
> - **能力标签**：数据驱动 / 0-1 拓荒 / 跨垂类迁移 / 策略分层 / 系统诊断（按实际填）
> --- `经历库/00-个人档案.模板.md`

#### MEM-OBJ-wiki-index
Label: wiki index

Identity: `wiki/index.md`, the lightweight lookup table. Form: Markdown paths and natural-language project/template labels, keywords and quick figures, consumed by the model rather than a shipped fixed-rule resolver. Substrate: persistent Markdown; cloud path adaptation is user-specified. Lineage: initialization makes an empty table; new experience is registered by prescribed model index updates. This is derived access metadata with possible content summaries, not an opaque embedding or complete dossier. Consumer: generation model selects relevant whole dossiers/templates using current request. The source lists `output/` as a destination but does not prescribe using its products as future selection inputs. Closest supplied records: [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace), [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document); distinct object spanning those routes, not contained by one. Evidence: SRC-1, `wiki/index.md`, `SKILL.md`.

> | 经历 | 路径 | 关键词 / 速取数据 |
> |---|---|---|
> --- `wiki/index.md`

#### MEM-OBJ-templates
Label: templates

Identity: resume and interview-script templates under `templates/`, including both shipped `.示例.md` files. Form: natural-language style rules, prose frames and illustrative facts; Markdown layout is not a shipped executable schema. Substrate: local Markdown and optionally user-supplied LaTeX; cloud pages in the proposed adaptation. Lineage: static author examples, or human-selected/replaced preferred documents. Persistent user replacements can guide later requests, but unchanged shipped templates are static guidance, not accumulated read-back. Consumer: generation model learns writing structure and style from the text; sample figures are not validated user facts. Closest supplied record: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document); distinct guidance objects, not a duplicate route or [RT-OBJ-skill](runtime.md#rt-obj-skill). Evidence: SRC-1, both template paths in the coverage table, `README.md`, `docs/04-使用指南.md`.

> - 高度浓缩：只留结论和数字，不展开推理（推理过程留给面试逐字稿）
> --- `templates/简历/简历模板.示例.md`

#### MEM-OBJ-jd
Label: jd

Identity: human-supplied target-job documents under `jd/`, one file per position. Form: natural-language requirements. Substrate: local files; actual cloud JD placement is not detailed. Lineage/admission: user pastes a selected JD and names it in a request. Consumer: generation model extracts capability requirements and selects/reorders/cuts experience. Retention enables later reuse of the same target, but does not validate dossier truth or modify generic extraction instructions. Closest supplied record: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document); distinct selector input object. Evidence: SRC-1, `jd/README.md`, `SKILL.md`.

> 1. 读 JD，提取岗位要求的能力点
> 2. 从你的经历库里挑出最相关的经历，突出对应数据
> 3. 弱化无关项，生成定制版简历或逐字稿
> --- `jd/README.md`

#### MEM-OBJ-output
Label: output

Identity: generated resumes and interview scripts saved under `output/`, or new cloud documents/conversation text. Form: natural-language user-facing products; optional LaTeX is a layout artifact whose compilation is not shipped. Substrate: local files or cloud documents; conversation-only output requires manual persistence in the denied-write branch. Lineage: derived from selected dossier/profile facts, templates, optional JD and raw-detail fallback. Local model admission writes products without mandatory per-product human approval; user then consumes and may refine them. In manual cloud copying, the human can edit/reject before persistence. Consumer: human applicant, not a prescribed later-agent guidance consumer. Persistent products alone therefore do not establish feedback memory or method revision. Closest supplied records: [RT-RTE-generate-document](runtime.md#rt-rte-generate-document), [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback); distinct output object. Evidence: SRC-1, `SKILL.md`, `docs/04-使用指南.md`, `docs/03-接入-飞书.md`.

> ④ 取用     产出在 output/，按需微调
> --- `docs/04-使用指南.md`

### Routes

none declared in this member

### Claims

#### MEM-CLM-retrieval-reliability
Label: Retrieval reliability

Claimed operation: all information is in the model's view, giving 100% retrieval reliability in the described small-library context mode. Source: SRC-1, `docs/01-理念-karpathy-wiki.md`. 
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

The same document permits whole-library reads but describes index-selected partial reads as normal. Index omission, wrong selection or stale paths can prevent a dossier reaching the consumer; window fit alone does not establish actual delivery or accurate use. Distinct from [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity): concerns selection/delivery rather than numerical preservation; closest route is [RT-RTE-generate-document](runtime.md#rt-rte-generate-document).

> - **检索可靠性 100%**：所有信息都在 AI「视线」内，不会出现 RAG「没匹配到相关片段」或「分块切断语义」的问题
> --- `docs/01-理念-karpathy-wiki.md`

> 即便把整个经历库全读进去也放得下，索引只是让它更省而已。
> --- `docs/01-理念-karpathy-wiki.md`

### Evidenced absences

#### MEM-ABS-memory-maintenance
Label: Memory maintenance protocols

Conclusion status: absent

Searched boundary: SRC-1 at the reviewed commit; complete tracked-path inventory and direct reads of `SKILL.md`, `README.md`, all four tutorials, both admission READMEs, indexes, profile, example and templates. Inspection query: whether any shipped instruction or executable route specifies automatic evaluation, deletion/withdrawal propagation, expiry, cleanup, transaction/rollback, agent-execution-trace compaction, checkpoint replacement or performance-fed revision of skill/templates. None does. This is an absence of a shipped protocol within this artifact, not an absence of host facilities, user deletion or inaccessible model processing. Existing supplied [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) supports user-triggered updates; that positive does not imply deletion propagation. [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback) affords manual copying but no synchronization protocol. No counterpart absence record is supplied. Evidence: SRC-1, `SKILL.md`, `docs/03-接入-飞书.md`, `docs/04-使用指南.md`; full source inventory is in [boundary](boundary.md#boundary-and-evidence). Consequently no supported path connects evaluation or cleanup results to a later memory consumer.

### Behavioral-authority paths

#### MEM-BAP-dossier-context
Label: Dossier context

Consumer: later host-model document generation. Channel: requested reads of selected persistent project dossiers and profile, with optional raw detail. Force: asserted factual/narrative knowledge plus persona-based relevance guidance, not tool permission or hard constraint. Horizon: future document requests across sessions if storage persists and the host reloads it; actual activation is unobserved. The update model has authority to transform raw facts under the skill; the downstream model has knowledge supplied by that transformation. Distinct from [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions), which supplies general procedural instructions; closest consumer route is [RT-RTE-generate-document](runtime.md#rt-rte-generate-document). Evidence: SRC-1, `SKILL.md`; the main-source and selective-read passages retained above and in the supplied route establish the channel, not adherence.

#### MEM-BAP-template-guidance
Label: Template guidance

Consumer: host-model resume/script generation. Channel: reading the selected persistent writing template. Force: requested style, structural and sentence guidance. Horizon: current request and subsequent requests that reread a retained user replacement; unchanged shipped examples remain static instruction. This is separate from [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions): it is template content selected for the product, not the skill's global procedure. [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) supplies the consumer route. Evidence: SRC-1, `SKILL.md`, `templates/简历/简历模板.示例.md`, `templates/逐字稿/产品面试话术模版.示例.md`; the resume-template quotation above establishes requested compression guidance. Compliance and improvement are unobserved.

## Annotations

#### On [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace)

Memory result: empty persistent profile/index and directories, not populated autobiographical memory. The host model is instructed to create starter content; first invocation is a human workflow trigger, not per-field approval. Initial biographical values remain for later human input. Later organization/generation is the named consumer. Profile rename and host-root resolution matter because a persisted file at another name/root need not reach those reads. Evidence: SRC-1, `SKILL.md`, `经历库/00-个人档案.模板.md`; the supplied initialization quotation and [MEM-OBJ-personal-profile](#mem-obj-personal-profile) retain the pertinent evidence.

#### On [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience)

Raw-to-derived chain: human-populated project records → model-organized dossier → model-updated profile/index → selected dossier/profile content in a future generation request. This is requested natural-language curation: narrative structure, why/how, quick metrics and persona emphasis change how facts are presented and found. Local admission belongs to the model; host tools perform physical I/O. The source supplies no required per-content human veto, independent consolidation oracle or candidate-comparison evaluation. Numeric preservation is a prose standard, not a tested rejection gate. Writes persist content and access metadata, not a changed extraction method. User edits plus a new request trigger maintenance; automatic invalidation and rollback are unspecified. Evidence: SRC-1, `SKILL.md`, `materials/README.md`, `docs/04-使用指南.md`; supplied route quotation and [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity) support the chain and policy limits.

#### On [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)

Read-back is foreground-request-driven, not unsolicited memory injection. Selector inputs are requested product, project/direction/length, optional JD requirements, index labels/keywords/quick figures and persona/project content. Selected retained parts are whole relevant dossiers, profile where needed, a writing template and optional original detail. Host file reads deliver text to the current model context; actual tool payload formatting is uninspected. No token budget, scoring function, enforced top-k, context eviction or isolated frame is specified. “Relevant 1–2 dossiers” is a rationale/example, not a universal cap. The selector leaves unread files reachable, and says nothing about removing old loaded turns. This differs from a stack-frame isolation mechanism: no frame is created or popped, and outside files become context by subsequent reads, not by live in-window references. Evidence: SRC-1, `SKILL.md`, `wiki/index.md`, `docs/01-理念-karpathy-wiki.md`.

Selected facts guide product content; templates guide style; JD guides relevance. Short resumes deliberately omit reasons that interview scripts expose. Results persist as products but no later agent reuse is prescribed. Whole-library alternative and raw-detail lookup qualify an exclusive index/dossier interpretation. 
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

See [MEM-CLM-retrieval-reliability](#mem-clm-retrieval-reliability) and [MEM-BAP-dossier-context](#mem-bap-dossier-context).

#### On [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback)

Storage alternatives: knowledge documents or Base records for raw/dossier/template content, new cloud documents for products. Local text-path instructions are manually adapted to page lookup. Automatic admission depends on host permissions; human manual copying is an alternative, not a required gate on writable deployments. Bound knowledge is intended for future requests, but the intervening host selector, selected page portions, budget, transformations and actual delivery channel are uninspected. No claim of whole-dossier or embedding-free cloud delivery follows from the local Markdown account. Proposed lark-base/lark-doc access establishes an integration idea without a shipped caller. Cross-platform copying is described but automatic synchronization and version conflict handling are not. Evidence: SRC-1, `docs/03-接入-飞书.md`; the supplied route retains the minimum writeback passage.

## Write side

Human acquisition admits raw experience, JD and preferred templates. These have different roles: asserted personal facts, target requirements and writing guidance. Model consolidation admits derived dossiers and both indexes in direct-write mode. Model generation admits products. In the denied-write cloud branch, humans decide which returned text to persist. Starting an organization request does not establish review/approval of each proposed fact (SRC-1, `SKILL.md`, `materials/README.md`, `jd/README.md`, `docs/03-接入-飞书.md`; object records and annotations above).

Reasons about project decisions are explicitly retained in dossier why/how fields and used in later interview narratives. This does not establish retained extraction provenance, error explanations, critic reports or model reasoning traces. Some raw materials may themselves be traces of human work or chats; there is no shipped automatic agent-trace-to-behavioral-memory update, current-context compaction or alternate checkpoint form. Static skill/template guidance is not revised against observed agent outcomes ([MEM-ABS-memory-maintenance](#mem-abs-memory-maintenance)).

Maintenance is request-triggered rereading of changed source material and corresponding dossier/index updates. No automatic evaluator marks memory valid; the example's completeness stars do not certify it. The numerical policy requests placeholders and reminders rather than invention, but supplies no independent rejection checker. No prescribed deletion cascade withdraws a removed raw claim from dossiers, indexes or old output. Human corrections and storage edits remain possible; successful consistency repair, rollback and conflict resolution cannot be inferred (SRC-1, `SKILL.md`, `经历库/01-示例经历.md`; [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), [MEM-ABS-memory-maintenance](#mem-abs-memory-maintenance)).

## Read-back

Persistent updated dossiers/indexes reach later generation through the model-directed file-selection route. Profile content also supplies facts/persona, not only lookup metadata. Optional JD steers relevance; optional raw-material reads restore detail not represented in derived memory. Template reads deliver style guidance, including user-replaced persistent templates. These are documented consumer roles, not hypothetical storage APIs, but no execution trace establishes delivery, activation or benefit ([RT-RTE-generate-document](runtime.md#rt-rte-generate-document) and its annotation).

Cloud read-back has a distinct uncertainty: binding a knowledge source does not expose the host's selector or prove that complete stored pages reach the model. Manual copy can admit content to the intended store without proving future delivery. Products have a human consumption route; they are not prescribed future model instructions. Nothing in the output index entry creates that route (SRC-1, `docs/03-接入-飞书.md`, `wiki/index.md`, `docs/04-使用指南.md`; [MEM-OBJ-output](#mem-obj-output)).

## Integration issues

1. No supplied fact requires correction. The runtime's primary-not-exclusive dossier interpretation is confirmed by raw fallback and the whole-library alternative. Its path/root and template-name issues remain relevant to whether retained files are found. Evidence: SRC-1, `SKILL.md`, `wiki/index.md`, `经历库/00-个人档案.模板.md`, `docs/02-安装-obsidian.md`; [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace), [RT-RTE-generate-document](runtime.md#rt-rte-generate-document). Actual host-root resolution and missing-template behavior remain unresolved, preventing guaranteed read-back.
2. No duplicate referent is declared: supplied routes receive memory annotations; new objects identify their inputs/results/guidance rather than redescribing route identities. New authority paths distinguish factual dossier context and selected template guidance from [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions). The retrieval-reliability claim is distinct from [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), though both qualify the author's quality language.
3. Initial profile values, per-claim source lineage, deletion propagation and multi-file consistency are not specified. Subsequent model index updating is specified and must not be suppressed by those unknowns. Consequence: intended persistence and transformation can be described, but factual auditability and reliable withdrawal cannot. Evidence: SRC-1, `SKILL.md`, `经历库/00-个人档案.模板.md`; [MEM-OBJ-personal-profile](#mem-obj-personal-profile), [MEM-OBJ-experience-dossiers](#mem-obj-experience-dossiers), [MEM-ABS-memory-maintenance](#mem-abs-memory-maintenance).
4. Cloud admission and later selector/delivery require external host facts. Do not transfer the local full-file/non-vector description to the knowledge-source consumer. Cross-platform copying is not an inspected synchronization mechanism. Evidence: SRC-1, `docs/03-接入-飞书.md`; [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback). This prevents a single uniform read-back guarantee across hosts.
5. The source's 100% retrieval and always-aligned-number claims exceed inspected evidence. Selected dossier reads and user/model edits are source-supported countercases to a universal delivery or fidelity invariant, not observed failures. Evidence: SRC-1, `docs/01-理念-karpathy-wiki.md`, `SKILL.md`; [MEM-CLM-retrieval-reliability](#mem-clm-retrieval-reliability), [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity). Reconciliation should preserve those claims as attributed doctrine alongside their limits.

## Limitations and checks

Git HEAD was rechecked as `6ebfe9aba989d7949dadea0fc4af6fb64892c6aa`; the source working tree was clean and tracked-path inventory matched the supplied boundary. No external source, prior analysis or target execution was used. Governing member types, worker rules and record contract were read completely; supplied runtime findings were tested against direct source reads rather than treated as an inspection limit.

No observed execution or causal evidence supports accurate extraction, actual token savings, instruction adherence, factual fidelity, privacy, durable cross-session writes or improved capacity. Host context management and cloud retrieval remain uninspected. Source-text coverage does not remove those operational limits.

Validation: invocation-specific `commonplace-run validate-output` passed after separating the absence status from its supporting prose. This establishes form, identities, relation checks and quotation occurrence, not semantic acceptance or observed behavior.
