---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "WikiBrain epistemic routes: source acquisition, compilation, structural and semantic checks, and the difference between durable use and warranted acceptance."
run-id: AAS-2026-11-08-wikibrain-f815b0976cda-01
reviewed-boundary: "32cc135877c8d7cd7be997ce57f25bb83128d891"
---

# WikiBrain epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on WikiBrain's imported sources, compiled pages, answers and maintenance results. The frozen scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identities resolve in its [Source register](boundary.md#source-register). All added inspection uses SRC-1 at that same commit. Evidence is implementation or doctrine/design, never observed execution or causal experiment. No target code was executed.

The material loop includes acquisition, model compilation and query, note admission, deterministic lint, requested semantic lint, source-pending classification, answer filing, rule delivery and replacement, and page withdrawal/recovery. Database versions, permissions and successful job return are evaluated for their actual domains, not as semantic truth tests. Remote provider reasoning and external MCP clients remain opaque. No user wiki, completed model transcript or comparison was supplied; therefore no particular generated claim's truth, exercised criticism, evidence-consuming acceptance or improved future capacity can be established. The relevant public claims are [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds), [EPI-CLM-health-check](#epi-clm-health-check), and [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard).

### Coverage

| Entry point or operation | Source path | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| Start command and service scheduling | SRC-1 `package.json`; `src/server.ts` | Direct package-script read; server findings supplied by boundary/runtime | No execution or independent full scheduler audit. |
| Six registered MCP tools | SRC-1 `src/mcp.ts` | Direct full read; [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | External planning and hooks not frozen. README advertises REST use by hooks, not a separate inspected hook executor. |
| Built-in ingest/lint/tool dispatch and result handling | SRC-1 `src/ingest.ts` | Direct full read; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs) | Provider loops and web polling supplied by runtime; no observed operation. |
| Persistent notes, retrieval, links, pending sources, archive/delete/rollback | SRC-1 `src/notes.ts` | Direct full read; [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-wiki](#epi-obj-wiki), [EPI-RTE-pending-selection](#epi-rte-pending-selection) | No production database. |
| Import conversion and saving | SRC-1 `src/import.ts` | Direct reads of finishHtml body and convertText/renderSource/saveSource; bounded search of conversion branches; [EPI-RTE-source-import](#epi-rte-source-import) | PDF/DOCX/parser internals and remote metadata correctness unassessed; no global fidelity verdict. |
| Structural and requested semantic lint | SRC-1 `src/lint.ts` | Direct full read; [EPI-RTE-structural-check](#epi-rte-structural-check), [EPI-RTE-semantic-check](#epi-rte-semantic-check) | Sampling and compliance unobserved. |
| Chat history and filing | SRC-1 `src/chat.ts` | Direct full read; [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | No actual selected answer or human assessment rationale. |
| General English compilation/conflict rules | SRC-1 `templates/general/en/schema/instructions.md` | Direct full read; [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions) | Other templates/languages uninspected; no system-complete negative about their epistemic instructions. |
| Rule replacement/merge and browser overwrite confirmation | SRC-1 `src/templates.ts`; `web/src/components/RuleUpdates.tsx` | Supplied [RT-RTE-rule-update](runtime.md#rt-rte-rule-update) | No direct reinspection; comparison is text/version based, not demonstrated quality. |
| REST dispatch, web edits, archive and rollback | SRC-1 `src/api.ts`; `src/web-api.ts` | Direct bounded operation searches; shared note implementations read; [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | Authorization findings supplied by runtime; not a full endpoint audit. |
| Zotero, bibliography import/export, citation rendering, public sharing, custom templates | SRC-1 `src/zotero.ts`; `src/bib.ts`; `src/templates.ts`; `src/shares.ts` | Included but not independently traced here; boundary describes source and rule entry families | Metadata reconciliation, citation-to-proposition support and public rendering correctness unassessed; prevents a system-complete negative about every check or transformation. |
| Provider internals, private hosted console, third-party services | See boundary | Excluded or unavailable as specified there; [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models) | No model-internal learning, hosted quality or causal benefit attribution. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | Imported source assertions and bibliographic assertions | see record | SRC-1 `src/import.ts` | Imported, not locally established truth; capture may be abstract-only or metadata-only. |
| [EPI-OBJ-wiki](#epi-obj-wiki) | Summaries, concepts, syntheses, answers, diagnoses and conflict statements | see record | SRC-1 `src/notes.ts` | Exact generated propositions and entailment indeterminable without instances. |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Structural propositions over current notes/links; separate requested semantic diagnoses | see record | SRC-1 `src/lint.ts` | Code predicates and model judgments have different domains. |
| [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs) | Tool-result/status assertions, not evidence that all page claims are correct | see record | SRC-1 `src/ingest.ts` | Log truncation and permissive event parsing bound success attribution. |
| [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | Retained answer/message text and filed answer body | see record | SRC-1 `src/chat.ts` | Role eligibility and user filing do not specify a truth criterion. |
| [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions) | Primarily non-truth-apt editing directives; occasional factual advice about search | see record | SRC-1 `src/notes.ts` | Natural-language guidance, not a guaranteed preflight. |
| [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models) | Not individually inspectable from weights here | see record | SRC-1 `src/ai/providers.ts` | No exact weight pin or accessible parameter-update evidence. |

## Authority-route ledger

The ledger is an overlay: fields owned by a cited record say see. Repeated citations split different functions of one implementation without redeclaring its referent. All possible results below are implementation deductions, not observed candidates.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-source-import](#epi-rte-source-import) | content transformation | implemented | [EPI-OBJ-raw](#epi-obj-raw) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | External assertions acquired; warrant unknown, not upgraded by metadata | see record | see record | SRC-1 `src/import.ts` | [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | none | Full-text fidelity not assured |
| [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) | content transformation | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: indeterminate | Sources to proposed wiki text | Model interpretation; no checked entailment domain | see record | see record | see record | Candidate production only; summaries may reshape while syntheses may add claims | see record | see record | SRC-1 `src/ingest.ts` | [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | Requested compilation is not acceptance | Need actual inputs/outputs to distinguish reshaping, derivation and conjecture |
| [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | disposition/acceptance | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Proposed write's path, size, permissions, quota, version | see records; software checks admissibility, not factual support | see records | see records | see records | Operational admission only; no evidence-consuming truth acceptance in these gates | see records | see records | SRC-1 `src/notes.ts` | none | Admission is not warrant | No oracle for page semantics |
| [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | retention | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Admitted page or assistant message | see records | see records | see records | see records | Retained candidate, not thereby an accepted claim | see records | see records | SRC-1 `src/notes.ts`; `src/chat.ts` | [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | none | Retention and links alone do not establish lifecycle integration after acceptance |
| [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | content transformation | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: indeterminate | Retrieved wiki/history to answer | Model; citation and no-fabrication requests are policy | see record | see record | see record | Candidate answer; no checked derivation or accepted ampliative claim established | see record | see record | SRC-1 `src/chat.ts` | [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | none | Model can also write; not read-only validation |
| [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | disposition/acceptance | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Selected assistant answer for filing | see record; caller selects, code checks assistant role | see record | see record | see record | Human selection may reflect judgment; no recorded evidence-consuming criterion for truth supplied | see record | see record | SRC-1 `src/chat.ts` | none | Filing is not demonstrated epistemic acceptance | Failed assistant messages are not excluded by the inspected role-only predicate |
| [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) | content transformation | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: non-ampliative reshaping | Selected answer text to filed Markdown | Deterministic fileAnswer wrapper, not a semantic evaluator | see record | see record | see record | Answer body copied without increased warrant | see record | see record | SRC-1 `src/chat.ts` | none | none | Attribution metadata and question wrapper do not validate the answer |
| [EPI-RTE-structural-check](#epi-rte-structural-check) | check/evidence production | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Local relational/regex facts only, conditional on DB inputs and interpretation | see record | see record | SRC-1 `src/lint.ts` | [EPI-CLM-health-check](#epi-clm-health-check) | none | Not source truth, semantic consistency or exhaustive coverage |
| [EPI-RTE-semantic-check](#epi-rte-semantic-check) | check/evidence production | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Requested criticism/evidence comparison; no demonstrated correct diagnosis | see record | see record | SRC-1 `src/lint.ts` | [EPI-CLM-health-check](#epi-clm-health-check) | none | No particular criticism or blame placement observed |
| [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) | disposition/acceptance | implemented | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Model's repair/suggestion choice and allowed writes | see record | see record | see record | see record | No independent semantic acceptance gate; judgment calls requested as suggestions | see record | see record | SRC-1 `src/ingest.ts` | [EPI-CLM-health-check](#epi-clm-health-check) | Semantic check and repair admission are separate | No mandatory recheck after repair |
| [EPI-RTE-pending-selection](#epi-rte-pending-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-raw](#epi-obj-raw) | no content change | see record | see record | see record | see record | see record | Link existence licenses scheduling only, not adequate compilation | see record | see record | SRC-1 `src/notes.ts` | [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | Nonpending does not mean accepted | No content-quality check on linking wiki page |
| [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions), [RT-RTE-rule-update](runtime.md#rt-rte-rule-update), [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling) | behavior/policy adaptation | implemented | See cited records | non-truth-apt policy/content update: retained schema text changes delivered guidance | see records | see records | see records | see records | see records | Rule distribution/admission does not certify rule truth or effectiveness | see records | see records | SRC-1 `src/templates.ts`; `src/notes.ts`; `src/ingest.ts` | [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard) | Universal automatic-write prohibition contradicted by spelling route | Neither delivery nor writable rules establishes exercised self-improvement |
| [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki](#epi-obj-wiki), [EPI-OBJ-raw](#epi-obj-raw) | no content change | Page versions, normal-read visibility and pending visibility | Optimistic version check; delete/archive/rollback operations in shared notes code | Caller requests operation; see record for general admission | Rollback creates a new version; delete hides wiki/schema; archive removes raw from pending without retracting its assertions | Software enforcement at shared functions | Recovery/access control, not semantic withdrawal of every dependent claim | Later reads/pending selection change; existing derived wiki claims are not automatically repudiated | Shared notes callers; SQL state and tool results; enforcing selection; later reads until reversed/edited | SRC-1 `src/notes.ts` | none | Withdrawal of visibility differs from withdrawal of warrant | No dependency-wide truth re-evaluation demonstrated |

The filing transformation has a concrete implementation deduction: given an eligible assistant message with content `Mars has two moons.`, fileAnswer places that exact body after the question wrapper and appends a newline. It adds query metadata, title and the prior question; it does not evaluate the proposition. The role-only guard also admits an assistant message marked failed. No target execution or real answer is asserted.

> if (!msg || msg.role !== 'assistant') throw new NoteError('BAD_PATH', { 'zh-TW': '只能歸檔 agent 的回答', en: 'Only agent answers can be filed as pages' });
> --- `src/chat.ts`

> const content = `---\nsource_type: query\nasked_at: ${msg.at}\n---\n# ${title}\n\n> 問：${question}\n\n${msg.content}\n`;
> --- `src/chat.ts`

Withdrawal/recovery has a narrower license than retracting knowledge: the inspected SQL changes the selected note's normal-read visibility or path. It does not traverse dependent wiki pages to retract their claims.

> `UPDATE notes SET deleted_at = now(), updated_at = now()
> WHERE workspace_id = $1 AND path = $2 AND deleted_at IS NULL`,
> --- `src/notes.ts`

> const { rowCount } = await pool.query(`UPDATE notes SET path = $3, updated_at = now() WHERE workspace_id = $1 AND path = $2 AND deleted_at IS NULL`, [ws, path, target]);
> --- `src/notes.ts`

No accepted-claim lifecycle integration route is established in the assessed write/filing/check paths: linking, indexing and later use are implemented, but those facts do not establish prior acceptance against evidence for a named intended use. This is a bounded assessment of those paths, not a system-complete negative about uninspected templates or external clients.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compiling-compounds](#epi-clm-compiling-compounds) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), [EPI-RTE-pending-selection](#epi-rte-pending-selection) | None supplied | No comparison of retained compilation with source rereading or future answers | Persistent compilation and reuse are wired | Compounding epistemic benefit not established by persistence; no per-claim warrant gate |
| [EPI-CLM-health-check](#epi-clm-health-check) | see record | SRC-1 `README.md`; doctrine/design | see record | [EPI-RTE-structural-check](#epi-rte-structural-check), [EPI-RTE-semantic-check](#epi-rte-semantic-check), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) | None supplied | No real-model contradiction-detection evaluation | Deterministic structural checking plus requested semantic sampling and repairs | Structural and semantic detection have different licenses; semantic completeness/reliability unknown |
| [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard) | see record | SRC-1 `src/ingest.ts`; doctrine/design and implementation | see record | [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | None supplied | Static counterexample, not an injection experiment | Literal-prefix denial only in built-in execution; MCP intentionally broader | A rule write can reach later instruction consumers without the declared human-only restriction |

## Bounded conclusion

WikiBrain acquires external assertions and bibliography, retains compiled pages and conversation text, and makes them available to later models and readers. Imported provenance fields help identify origin; they do not endorse the assertions. The inspected import fallback can replace a page body with an abstract or retain bibliography only, so the raw layer is immutable stored conversion output, not a guaranteed complete original. Source warrant remains unknown. See [EPI-RTE-source-import](#epi-rte-source-import).

Compilation and answer generation are implemented candidate-producing routes. The exact content relation remains indeterminate: summary labels do not prove semantic preservation, and synthesis labels alone do not prove non-entailment. No checked derivation from warranted source premises or evidence-consuming acceptance of a produced ampliative claim is demonstrated. Writes can enter the later read path before human judgment; explicit answer filing supplies a distinct user selection but no required evidence record or truth criterion. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) and [RT-RTE-chat-session](runtime.md#rt-rte-chat-session).

The deterministic evaluator warrants only structural statements over its queried representation. Its results go to a display/prompt, where model interpretation rather than a hard correctness gate chooses repairs. Semantic lint requests contradiction and staleness comparison, with suggestions for judgment calls, but neither a correct diagnosis nor an accepted repair is observed. Pending-source status is a scheduling predicate based on inbound links, not evidence of adequate synthesis. These are independent conclusions, not one system score. See [EPI-RTE-structural-check](#epi-rte-structural-check), [EPI-RTE-semantic-check](#epi-rte-semantic-check), and [EPI-RTE-pending-selection](#epi-rte-pending-selection).

Rules have later behavioral force as model-readable guidance. Template merges, direct client edits and the noncanonical automatic-write route can change that guidance; the version mechanism protects concurrent edits, not semantic merit. Page history enables local recovery, while deletion/archive do not automatically retract claims in dependent pages. None establishes learning as improved future capacity, content-directed theory criticism and iteration, reflective self-representation, or exercised self-improvement. Those properties remain independently unestablished by the assessed implementation/run evidence; provider opacity is not proof of their absence. The uninspected operation families in coverage also preclude an unqualified system-wide negative.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-raw
Label: Raw source pages

Source-native identity: raw/ notes created from Converted metadata/Markdown. Representational form: natural-language source text plus symbolic frontmatter consumed by parsers; storage substrate: PostgreSQL notes and note_versions. Unlike [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs), these are source candidates, not job telemetry; no counterpart found among supplied operative-object declarations. SRC-1 `src/import.ts`, `src/notes.ts`. No original capture or instantiated converted source supplied. Imported bibliography and content have unknown truth warrant. The raw update/delete restrictions preserve stored content, not accuracy or completeness of extraction; archive changes its pending visibility.

> const body = renderSource(c);
> await assertCanWrite(ws, body);
> const r = await createNote(ws, path, body, actor);
> --- `src/import.ts`

#### EPI-OBJ-wiki
Label: Compiled wiki pages

Source-native identity: wiki/ summaries, entity/concept pages, syntheses, queries and lint pages. Representational form: natural-language claims and editing prose, with symbolic paths/links/tags; storage substrate: PostgreSQL notes with snapshots and derived link/tag tables. No counterpart among supplied objects; distinct from telemetry [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs). They are products/inputs of [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) and [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), not duplicate routes. SRC-1 `src/notes.ts`, `templates/general/en/schema/instructions.md`. Concrete source propositions and generated claims were not supplied; authorship/retention alone do not identify accepted claims.

> **wiki/** holds compiled pages that you maintain: source summaries, entity pages, concept pages, comparisons, syntheses. One topic per page; name pages by concept.
> --- `templates/general/en/schema/instructions.md`

#### EPI-OBJ-lint-report
Label: Structural lint report

Source-native identity: LintReport returned by lintWorkspace. Representational form: symbolic structured arrays/counts/paths and natural-language issue messages; storage substrate: current function return, then prompt text when startLint consumes it. Requested wiki/lint reports are separately persisted wiki pages, not proof that this exact return was retained. Distinct from [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs): this is a structural-check result, not execution telemetry. SRC-1 `src/lint.ts`, `src/ingest.ts`.

> const missing_special: string[] = [];
> if (!indexNote) missing_special.push('wiki/index.md');
> if (!logNote) missing_special.push('wiki/log.md');
> --- `src/lint.ts`

### Routes

#### EPI-RTE-source-import
Label: Converted source admission

Part of: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)

This part isolates acquisition before model compilation. Endpoints: converted external text/metadata → renderSource → unique raw path → quota check/createNote → durable raw candidate. Owner: source/caller supplies assertions, software serializes/adopts them. Selection includes import-format and fallback rules; import is not evidence-consuming truth acceptance. Remote metadata is not an answer oracle. Open import mode, not an improvement experiment. Caller can decline before import; software can reject bad paths/capacity/content. Recovery for raw content is archival, not rewriting through updateNote. SRC-1 `src/import.ts`, `src/notes.ts`.

- Immediate return: note path/title/version and metadata from saveSource.
- Later read-back: raw note text reaches subsequent read_note consumers and pending-source selection.
- Delegated visibility: built-in models receive selected raw content with an untrusted_source label; external MCP read returns content without that label, per [RT-RTE-client-tools](runtime.md#rt-rte-client-tools).
- Selection predicate: import route's converted candidate and unused path under raw; remote extraction fallback depends on thin/challenge and bibliography conditions.
- Invalidation or expiry: raw cannot be updated/deleted by shared note functions; archive removes it from pending but preserves the note.
- Activation or effect: successful create persists acquired assertions; actual downstream use or source fidelity unobserved.
- Evidence limits: direct inspection of conversion-saving and selected HTML fallback branches, not all parsers or remote services.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Source warrant is unknown; lineage can retain origin/bibliography, while representation can degrade from full text to abstract or metadata. A source-supported countercase to “raw is always the complete original” is explicit abstract substitution:

> out.markdown = `# ${out.meta.title}\n\n## 摘要 / Abstract\n\n${abstract}\n`;
> --- `src/import.ts`

> if (m.source_url) lines.push(`source_url: ${yamlStr(m.source_url)}`);
> --- `src/import.ts`

#### EPI-RTE-structural-check
Label: Structural lint evaluation

Part of: [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)

Endpoints: current workspace notes/links → SQL predicates, index membership and log-heading regex → LintReport → lintPrompt/model, or structural display. Owner/evaluator: program. Target/domain: relational orphan/dangling/index status, pending sources and heading syntax, not truth of topic claims. It produces evidence; it neither accepts a semantic theory nor directly approves a repair. Structural reference outcomes are the predicates themselves. SRC-1 `src/lint.ts`, `src/ingest.ts`.

- Immediate return: complete structural report to caller; prompt lists at most 30 paths per category and selected issue text.
- Later read-back: inapplicable — this function does not retain the return; later model-authored report persistence belongs to [RT-RTE-lint-job](runtime.md#rt-rte-lint-job).
- Delegated visibility: model lint invocation receives the formatted structural subset, not every full page or necessarily every listed finding.
- Selection predicate: live workspace notes and links, with special/system-page exclusions varying by category.
- Invalidation or expiry: report reflects separate fresh queries, not a transactionally consistent snapshot; subsequent edits can change its truth.
- Activation or effect: advisory evidence in the prompt/display; model selects repairs under the enclosing route, not a hard gate on future writes.
- Evidence limits: structural derivations assume DB representation and query semantics; not semantic consistency, source correctness, or tested repair quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

A concrete static deduction: if indexNote is null, the inspected branch pushes wiki/index.md into missing_special. The inferred proposition is “the index lookup yielded no note,” not “this wiki has no adequate knowledge.” Likewise `## [2026-99-99] ingest | x` matches the heading shape despite an invalid calendar month; the regex is a syntax evaluator, not a calendar or truth evaluator. No target execution is needed for either deduction.

> const bad = heads.filter(h => !/^## \[\d{4}-\d{2}-\d{2}\] \S+ \| .+/.test(h));
> --- `src/lint.ts`

> Fix what you can directly with update_note (add links, add pages to index.md, repoint broken links); list judgement calls as suggestions.
> --- `src/lint.ts`

#### EPI-RTE-semantic-check
Label: Semantic lint request

Part of: [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)

Endpoints: formatted structural findings plus requested index/sample reads → model comparison of pages/sources → proposed diagnoses, repairs or suggestions → enclosing write/report route. Owner/evaluator: provider model under stored schema and lint prompt. Target/domain: contradictions, stale claims superseded by newer sources, missing concepts, cross-references and data gaps in sampled wiki pages. This part differs from deterministic checking in evaluator/domain and does not duplicate repair admission. SRC-1 `src/lint.ts`, `src/ingest.ts`.

- Immediate return: requested model diagnosis/final summary, with tool results throughout the enclosing run.
- Later read-back: requested diagnoses/suggestions in wiki/lint and log pages can reach later readers if the model writes them; the enclosing route permits persistence without a diagnosis-quality gate.
- Delegated visibility: same lint model sees structural prompt and chosen note results; no separate critic or answer reference supplied.
- Selection predicate: prompt requests index-first sampling; model chooses actual pages and comparison content.
- Invalidation or expiry: no implemented semantic verdict expiry; ordinary page revisions can change reviewed claims and retained reports.
- Activation or effect: diagnoses may guide immediate repair tools or suggestions; no demonstrated diagnosis, correct criticism or changed reliance supplied.
- Evidence limits: request for semantic comparison is implemented, reliable checking/compliance not established; content relation indeterminate without outputs.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model proposes and decides straightforward repairs versus suggestions, software may veto writes, and user initiation is not per-repair approval. No external semantic answer oracle. Open maintenance mode rather than controlled improvement curriculum. Normal snapshots support page recovery; they do not make the whole diagnosis/repair sequence atomic. Theory-builder conditions 1–4 are not jointly established: localized topic theories and their actual consumption are not evidenced by a supplied wiki; the prompt requests criticism but supplies no observed challenged claim, blame placement and changed reliance; retained criticism shaping a next round is unobserved. These are separate evidence limits, not a finding that opaque model internals contain no criticism.

> Now do the semantic checks: read_note wiki/index.md first, then sample related pages and look for (1) contradictions between pages; (2) stale claims superseded by newer sources; (3) concepts mentioned repeatedly without their own page; (4) cross-references worth adding; (5) data gaps that more sources could fill.
> --- `src/lint.ts`

#### EPI-RTE-pending-selection
Label: Link-based pending selection

Part of: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)

Endpoints: current raw notes plus derived links → listPendingSources → getInstructions prelude or default startIngest targets. Owner/selector: SQL/program. Distinct material scheduling part, not acceptance of the source's claims. Target is existence of a live wiki inbound link; reference outcome is that predicate, not compilation adequacy. Explicit existing-path ingest can bypass default selection. SRC-1 `src/notes.ts`, `src/ingest.ts`.

- Immediate return: pending path/title/update list.
- Later read-back: later calls recompute from persisted notes/links; a successful wiki link changes default future selection.
- Delegated visibility: getInstructions includes paths and sanitized titles; startIngest passes selected paths to the model task.
- Selection predicate: live raw non-README, non-archive notes with no live wiki page linking to their note ID.
- Invalidation or expiry: link changes, wiki deletion or source archival alter next selection; no semantic expiry date.
- Activation or effect: selects default compilation work and prompts later agents; any live wiki backlink suffices to remove a raw source from pending.
- Evidence limits: no check of whether the linking page summarizes the source accurately, fully or at all; no completed instance supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

There is no per-source human approval here. Source/caller proposes content, code selects work, model decides compilation details. Open ingestion mode; no truth oracle. Recovery is changing links/restoring visibility or supplying explicit ingest targets, not an acceptance rollback. A countercase to equating nonpending with well-compiled is a live wiki page containing only a resolvable backlink: the inspected predicate tests no summary body or support criterion.

> AND NOT EXISTS (
>   SELECT 1 FROM links l JOIN notes f ON f.id = l.from_note_id
>    WHERE l.to_note_id = n.id AND f.deleted_at IS NULL AND f.path LIKE 'wiki/%')
> --- `src/notes.ts`

### Claims

#### EPI-CLM-compiling-compounds
Label: Compile once and compound

Claimed operation: persistent intermediary wiki avoids rereading raw sources per question and compounds knowledge. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard), which concerns rule-edit authority. Storage/reuse wiring supports persistence, not a causal improvement or acceptance claim.

> rather than re-reading the sources on every question as RAG does — so knowledge is compiled once and compounds.
> --- `README.md`

#### EPI-CLM-health-check
Label: Wiki health checking

Claimed operation: agent answers with citations and health-checks structural problems and contradictions into reports. SRC-1 `README.md`, doctrine/design. No counterpart in supplied claims; closest [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard) instead concerns permitted rule writes. This claim has separate deterministic and model-dependent implementation support.

> answers questions with citations in a chat panel, and health-checks the wiki (orphans, broken links, contradictions) into `wiki/lint/`.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; shared instruction delivery is [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions), and the new route declarations specify their own consumers, channels, force and horizon.
