---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llm-wiki epistemic routes: source transformation, structural checks, local L1 verification and the limits of later reliance."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
---

# llm-wiki epistemic report

## Source-and-claim boundary

Can llm-wiki acquire or produce truth-apt content, check it and license later reliance? The assessed boundary is the shipped knowledge-maintenance system, not Claude Code's model or automatic memory loader. See [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All source anchors below use SRC-1 at that frozen commit. Natural-language maintenance procedures establish doctrine/design, not executable maintenance or observed compliance. The initializer supplies a narrower implementation layer.

The material counterexample to a blanket “no verification” conclusion is `prune --l1`: it requests per-claim evidence and correction before user admission. Conversely, structural lint, source attribution, recent timestamps and file retention do not by themselves establish factual acceptance. Public/design claims are [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision), [EPI-CLM-l1-honesty](#epi-clm-l1-honesty), [EPI-CLM-confidence-lifecycle](#epi-clm-confidence-lifecycle) and [EPI-CLM-automatic-repromotion](#epi-clm-automatic-repromotion).

| Entry point or operation | Source path | Coverage and records | Limit/conclusion prevented |
|---|---|---|---|
| Plugin/copied command dispatch | `SKILL.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `setup.sh`, `wiki.md` | Direct complete skill/manifest reads; supplied [RT-BAP-skill-dispatch](runtime.md#rt-bap-skill-dispatch) and [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) for remaining packaging | Host permission/loading implementation excluded; no universal mediation claim |
| Setup and direct initializer | `scripts/init-wiki.sh`, `templates/obsidian/Schema.md` | Direct complete reads; [EPI-RTE-template-render](#epi-rte-template-render) | Other templates and installer behavior supplied through runtime/boundary, not independently reread |
| Ingest and bulk import | `SKILL.md` | Direct complete read; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | No actual inputs/outputs; entailment and provenance preservation unknown |
| Query, fallback, logging, write-back | `SKILL.md` | Direct; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | No answer/retrieval trace; actual synthesized propositions not determinable |
| L2 prune and re-promotion | `SKILL.md`, `README.md` | Direct skill plus README Query/Prune/Lint excerpt; [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) | Age/use is not evidence of falsity; README automation conflicts with skill offer |
| L1 classify, evidence, re-verify, correct, demote, delete, skip | `SKILL.md`, `openspec/specs/prune.md` | Direct skill and specification scenarios 9–10; [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) | Spec scenarios are design examples, not executions |
| Lint, --fix, status, Dashboard | `SKILL.md`, `openspec/specs/schema.md` | Direct skill and schema Knowledge/Feedback excerpt; [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) | No executable independent validator or supplied check result |
| Other supporting docs, diagrams, examples, specifications | Paths inventoried in boundary | Not independently assessed beyond scoped search of README, architecture and specifications | No exhaustive consistency/historical claim; search hits alone are not corroborating operation |
| Provider parameters and host L1 consumption | External host | See [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) | Weight changes, exact version and endpoint substitution uninspected; no parametric-learning conclusion |

No additional target-owned CLI dispatcher, hook or registered executable maintenance tool appears in the supplied tracked-tree account and inspected skill/manifest/initializer. The separate direct-script entry is included, rather than assumed subject to the model's quality gate. This is not a negative about arbitrary host extensions. Missing user vaults/L1 files prevent individuating actual claims or evaluating checks on them; missing traces prevent observed acceptance, activation or benefit; missing comparisons prevent causal retrieval or self-improvement claims. Unread supporting documents prevent a system-complete negative about every design formulation, but do not erase the positively evidenced routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Source-derived facts, relationships, decisions and current/history states | Retained L2 material for answers | SRC-1, `SKILL.md` ingest/query | Actual propositions and initial warrant not supplied |
| [EPI-OBJ-hub-index](#epi-obj-hub-index) | Page descriptions can assert page subject matter; tags/links primarily select | Routing keys and archive membership | SRC-1, `SKILL.md` Hub-Index-Routing | Compression fidelity/relevance not checked independently |
| [EPI-OBJ-l1-rules](#epi-obj-l1-rules) | Current-behavior claims; also non-truth-apt directives/preferences | Session-steering L1 rules and index descriptions | SRC-1, `SKILL.md` prune --l1 | Rule contents absent; claim-class false does not mean every sentence lacks truth value |
| [EPI-OBJ-access-log](#epi-obj-access-log) | Assertion that a page was read on a date, plus selection reason | Evidence for cold/hot selection | SRC-1, `SKILL.md` Access-Log | Self-reported by maintainer, not independent instrumentation |
| [RT-OBJ-schema](runtime.md#rt-obj-schema) | Normative conventions; factual confidence labels | See cited record | SRC-1, `templates/obsidian/Schema.md` | Schema is not a truth evaluator |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Procedures plus design claims | See cited record | SRC-1, `SKILL.md` | Not a learned method or observed execution |

L1 verdicts, query answers and Dashboard metrics are current outputs of the cited route containers, not independently evidenced persisted claim instances. Whether a particular answer adds an ampliative proposition is not determinable without its inputs and output.

## Authority-route ledger

Each row separates function even when the same supplied route container covers several phases. Field ownership for the container's progression, owner and read-back remains in the cited record. Architectural status below concerns the specific function, not the host's ability to execute tools. “Policy” force means requested model/human behavior, not a hard interceptor.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-template-render](#epi-rte-template-render) | content transformation | implemented | [RT-OBJ-schema](runtime.md#rt-obj-schema) | non-truth-apt policy/content update: template parameter substitution | Shipped conventions to configured Schema | Python literal replacements, filesystem existence | Setup, before later commands | Created or skipped files | Executable write/skip | No factual warrant added | Installs conventions available to maintenance | Maintainer, Schema read, advisory policy, later commands | SRC-1, `scripts/init-wiki.sh` | none | none | Implementation deduction, not execution |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: acquisition/import | External URL/file/text to extracted facts or converted notes | Foreground model using source/schema | User ingest/import | Candidate retained facts | Model-interpreted writes | Source warrant unknown; import is not independent production | Creates/updates pages, history and links | Future query agent, page reads, advisory content, later invocations | SRC-1, `SKILL.md` ingest/import | none | none | Extraction may alter meaning; no actual edge proves preservation or novelty |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | check/evidence production | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Properties, links, routing, credential exclusion, touches | Same model, structural/security-policy domain | After ingest writes; import calls lint | Issues/warnings | Policy report | Checks organization, not source truth | Reports deficiencies; no specified automatic rollback | Maintainer/user, gate report, advisory, current invocation | SRC-1, `SKILL.md` Phase 4 | none | none | Gate name does not establish pre-write fact admission |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | retention | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Current state and superseded wording to Markdown/history/Git | Model decides supersession under schema | Ingest updates | Current headline plus dated old wording | Policy writes/commit | Retention preserves wording, not warrant | Supplies later content; old claims remain inspectable | Query/maintainer, files/history, advisory, across sessions | SRC-1, `SKILL.md` State + History | none | none | Not lifecycle integration after demonstrated acceptance |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-hub-index](#epi-obj-hub-index) | no content change | Hubs/descriptions or grep to 3–5 pages | Model relevance judgment; namespace/description domain | Query before synthesis | Selected retained text, optionally L1 | Ranking policy | Relevance selection grants no factual endorsement | Chooses evidence/context used in answer | Query agent, Read/search results, ranking, current answer | SRC-1, `SKILL.md` query Phases 0–1 | [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision) | none | Fallback can recover archived pages; no guaranteed context eviction |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | content transformation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Selected pages to attributed answer/summary | Model, no reference-answer oracle | After reads | Candidate answer, stale/confidence warnings | Advisory answer | Attribution identifies pages, not established truth | User may rely or request write-back | User, natural-language answer, advisory, current/future actions | SRC-1, `SKILL.md` query Phases 2–4 | none | none | Could reshape, derive or conjecture; inputs/output needed to classify |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Useful summary/gap proposal to write-back | User confirms; model proposes | Optional after synthesis | Approval/refusal | Human admission protocol | Confirmation authorizes storage; no named factual acceptance criterion | Permits proposed page write | Maintainer, user response, permissive, proposed write | SRC-1, `SKILL.md` Optional Write-Back | none | none | No evidence-consuming factual acceptance established |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | retention | doctrine only | [EPI-OBJ-access-log](#epi-obj-access-log) | truth-apt transformation: acquisition/import | Actual full-page reads to dated log statements | Maintainer self-report | Each full read before synthesis | Append with matched reason | Append policy | Claimed use history, not accuracy or relevance proof | Feeds later prune/status | Prune/status agent, Markdown log, advisory evidence, later invocations | SRC-1, `SKILL.md` Phase 1b | none | none | Logging not covered by optional content-write confirmation |
| [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) | behavior/policy adaptation | doctrine only | [EPI-OBJ-hub-index](#epi-obj-hub-index) | non-truth-apt policy/content update: live-index demotion | Logged access/creation proxy to archive membership | Model threshold/exemptions; user veto | Requested/scheduled externally; confirmation before write | Archived marker and verbatim moved line | Human-gated ranking policy | Coldness does not withdraw factual warrant | Reduces preferred selection; grep/links still available | Query agent, live/archive hub sections, ranking, future queries | SRC-1, `SKILL.md` prune | [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision), [EPI-CLM-automatic-repromotion](#epi-clm-automatic-repromotion) | README automatic vs skill offer | No deletion/denial; no measured precision benefit |
| [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) | check/evidence production | doctrine only | [EPI-OBJ-l1-rules](#epi-obj-l1-rules) | no content change | Due individual claims about paths/commands/flags/versions/etc. | Model interprets local files/source or read-only help/version; remote claims inconclusive | Batch, never-verified then oldest | Supports/contradicts/inconclusive; partial flag and evidence basis | Advisory verdict | Only checked claims within local evidence domain; source is not executed behavior | Recommends user actions, does not perform them | User, per-claim verdict/evidence, advisory, current decision | SRC-1, `SKILL.md` Gather Evidence | [EPI-CLM-l1-honesty](#epi-clm-l1-honesty) | none | No omniscient oracle; credentials checked for existence only |
| [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) | disposition/acceptance | doctrine only | [EPI-OBJ-l1-rules](#epi-obj-l1-rules) | no content change | Verdict/rule to re-verify, correct, demote, delete or skip | User per rule; inconclusive needs user knowledge; contradiction needs corrected text for re-verification | After evidence | Confirmed action or untouched due rule | Human admission protocol | Bounded acceptance procedure for intended continued L1 reliance, not infallibility | Authorizes only selected writes/removal | Maintainer, user response, permissive, per-item action | SRC-1, `SKILL.md` Act | [EPI-CLM-l1-honesty](#epi-clm-l1-honesty) | none | No supplied acceptance episode; user knowledge uninspected |
| [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) | lifecycle integration | doctrine only | [EPI-OBJ-l1-rules](#epi-obj-l1-rules) | truth-apt transformation: indeterminate | Approved correction to body, description, index and verified date | Maintainer applies approved text in all claim locations | After user admission | Corrected rule connected to refreshed verification metadata | Policy synchronized edits | Only approved claim's local scope; date alone not proof | Changes later rule text delivered by host | Future host agent, L1 body/index descriptions, directive policy, later sessions | SRC-1, `SKILL.md` Re-verify | [EPI-CLM-l1-honesty](#epi-clm-l1-honesty) | none | Conditional post-acceptance integration; semantic relation of unsupplied corrections unknown |
| [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-l1-rules](#epi-obj-l1-rules) | non-truth-apt policy/content update: withdraw session rule | Confirmed demote/delete to L1 removal and reference repair | User chooses; model ensures carry-over precedes deletion | After evidence and confirmation | Rule removed; demotion history retained, credentials never demoted | Withdrawal protocol | No L1 reliance intended after removal; L2 history not renewed endorsement | Reduces future L1 loading; demotion changes channel to on-demand history | Host future loader / L2 query, index/files, selection, later sessions | SRC-1, `SKILL.md` Demote/Delete | [EPI-CLM-l1-honesty](#epi-clm-l1-honesty) | none | No Git undo; skipped/stale rules may still load; see [RT-ABS-action-gate](runtime.md#rt-abs-action-gate) |
| [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) | check/evidence production | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-hub-index](#epi-obj-hub-index) | no content change | Page properties/link graph, age, index drift, credentials, L1 due metadata | Foreground model applying listed schema checks | Lint or lightweight status | Counts/severity/fix suggestions/Dashboard metrics | Advisory diagnostics | Structural consistency and age flags only | Informs maintenance; status itself modifies nothing | User/maintainer, report/Dashboard, advisory, current/later maintenance | SRC-1, `SKILL.md` lint/status | [EPI-CLM-confidence-lifecycle](#epi-clm-confidence-lifecycle) | none | No independent regex executable or semantic fact validation |
| [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) | behavior/policy adaptation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-hub-index](#epi-obj-hub-index) | non-truth-apt policy/content update: confidence downgrade and routing repair | Detected age/drift to confidence/index/stubs/cross-links | Model under caller --fix authorization, no per-fix approval | After lint scan | high to stale, backfilled/moved entries, stubs | Model repair policy | Lower confidence cautions; stub/links add no fact warrant | Changes future warnings and context selection; never writes L1 | Query/maintainer, page metadata/index, advisory/ranking, later invocations | SRC-1, `SKILL.md` Auto-Fix | [EPI-CLM-confidence-lifecycle](#epi-clm-confidence-lifecycle) | none | Semantic fidelity of generated descriptions unknown; no automatic multi-file rollback |

These ledger splits do not supersede runtime's valid route containers. Acquisition/import is the established entry-edge classification; transformations within extraction/conversion remain semantically untested. No example of warranted-premise entailed derivation or demonstrated non-entailing conjecture is available. The L1 evidence route supplies a real design counterexample to a universal absence of acceptance; the ingest quality gate does not supply a corresponding fact-acceptance route.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision) | Routing/demotion keep L2 precise | SRC-1, `SKILL.md`; doctrine/design | Query/prune selection and fallback | No executable retrieval evaluator; see [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) for prescribed routes | None | No contrast; age/use need not track correctness/relevance | Preferred-context control is specified | Precision benefit unknown; fallback qualifies “no more grep” |
| [EPI-CLM-l1-honesty](#epi-clm-l1-honesty) | L1 verification keeps rules honest | SRC-1, `SKILL.md`; doctrine/design | Evidence, verdicts, correction, human choice | None for checks; [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) is prompt doctrine | None | Local/read-only boundary; unchecked/remote claims inconclusive; no action gate | Bounded evidence-responsive checking and acceptance protocol | Reliable truth/currentness or later compliance unestablished |
| [EPI-CLM-confidence-lifecycle](#epi-clm-confidence-lifecycle) | high means verified/reliable/current | SRC-1, `openspec/specs/schema.md`; doctrine/design | Enum and downgrade semantics | No factual validator; prescribed [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) | None | Date threshold tests age, not reliability | Intended warning vocabulary and stale repair | No evidence-consuming route for initially assigning high in assessed ingest/query procedures |
| [EPI-CLM-automatic-repromotion](#epi-clm-automatic-repromotion) | Archived query hits automatically re-promote | SRC-1, `README.md`; doctrine/design | Main skill says offer re-promotion | None; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) specifies offer | None | No run chooses between conflicting texts | Re-hit recovery is prescribed as an offer | README overstates automatic disposition |

## Bounded conclusion

- **Acquisition and retention:** [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) requests extraction/import, current-state replacement and retained history. Source warrant is unknown. It does not establish that a retained fact was independently checked. The structural gate assesses properties, links, routing and credential policy, not the truth of the source's assertions.
- **Answers and continued reliance:** [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) selects retained text and requests attributed synthesis with inherited confidence/age warnings. Selection and optional user-approved write-back authorize use/storage, not evidence-consuming acceptance of a novel proposition. Actual answer content is unavailable, so non-ampliative reshaping, entailment and ampliative conjecture cannot be separated at that edge.
- **Local checking, acceptance and integration:** [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) prescribes a distinct chain: named local claim → evidence basis and bounded verdict → user decision → corrected rule/verification metadata and synchronized descriptions/index. Supports recommends continued L1 use; contradiction permits re-verification only with correction; inconclusive requires user knowledge; skip leaves the rule due. This is a design-level acceptance criterion for local behavior claims intended to steer future sessions, not observed acceptance or a guarantee of truth. Demotion/delete withdraw L1 delivery only after user confirmation and reference/carry-over handling. Demoted history remains retrievable but is not endorsed as current. The external host supplies actual later loading, and [RT-ABS-action-gate](runtime.md#rt-abs-action-gate) prevents claiming action-time protection.
- **Direct adaptation without new factual warrant:** [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) lets usage evidence change future preferred retrieval through human-approved archive moves. [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) lets age/drift checks alter confidence and routing under --fix. Neither access frequency nor dates prove factual accuracy. Reports/logs alone are not improvement; no trace closes later behavioral activation or causal benefit.
- **Independently bounded properties:** Provider parameter changes/version resolution remain uninspected in [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code). The L1 theory-property assessment remains the separately qualified one in [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification): localized rule criticism/revision is prescribed, but actual theory contents, iteration and learning benefit are unobserved. Human internal admission decisions prevent an autonomous verification-route claim. There is no supplied evidence of criticism of llm-wiki's own method against operation; no exercised self-improvement or global reflection conclusion follows from file revision alone. These limits coexist with the positive local checking protocol.

## Shared records

### Operative objects

#### EPI-OBJ-wiki-pages
Label: Wiki content pages

Natural-language source-derived facts, current-state blocks and dated History stored in Logseq/Obsidian Markdown; properties support model interpretation. Closest supplied record is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), the producer route, not this retained object. Distinct also from [RT-OBJ-schema](runtime.md#rt-obj-schema), the conventions governing pages. Pages later reach query and maintenance consumers; no actual vault supplied. SRC-1, `SKILL.md` ingest and State + History.

> - Delete nothing: every superseded statement stays readable in the history
> --- `SKILL.md`

#### EPI-OBJ-hub-index
Label: Hub Index and Archive

Natural-language descriptions with link/tag identifiers in retained hub Markdown. The model ranks descriptions; symbolic-looking links do not establish an executable relevance rule. Distinct retained object overlapping consumers/producers [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not a replacement for those routes. SRC-1, `SKILL.md` Hub-Index-Routing.

> A routing line is `[[link]] -- description #tags`, one per child page.
> --- `SKILL.md`

#### EPI-OBJ-l1-rules
Label: L1 rules and loaded descriptions

Natural-language behavior claims/directives in external user Markdown files, plus frontmatter claim class/verification date and index pointers/descriptions. Actual contents absent. Closest supplied [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) is the checking/change route, not the object; host consumer is separately [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code). SRC-1, `SKILL.md` L1 verification.

> - Scan every L1 memory file EXCEPT the index file (e.g. MEMORY.md — an index, not a rule). Its lines are
>     auto-loaded too: keep them in step whenever a rule is corrected, demoted, or deleted
> --- `SKILL.md`

#### EPI-OBJ-access-log
Label: Access-Log entries

Dated page identifiers plus natural-language matched reasons in append-only wiki Markdown. Fixed date/link positions are prescribed for prune/status parsing; reasons are model-interpreted routing transparency. Distinct from the producing [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and consuming [RT-RTE-index-prune](runtime.md#rt-rte-index-prune). Source is maintainer-reported reads, not external fact verification. SRC-1, `SKILL.md` Access-Log.

> - prune/status parse the date + `[[page]]` from fixed positions (split on ` -- `); the `matched:` suffix is
>   irrelevant to LRU aggregation and does not affect parsing
> --- `SKILL.md`

### Routes

#### EPI-RTE-template-render
Label: Schema template rendering
Part of: [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/skipped path messages; generated Schema file if absent.
- Later read-back: Setup installs static shipped conventions, so use-derived read-back is inapplicable; later maintenance reads the generated Schema as guidance.
- Delegated visibility: inapplicable — Python receives flags/templates, not a delegated model task.
- Selection predicate: Tool flag chooses template directory; namespace flags supply replacement text; existing target is skipped.
- Invalidation or expiry: No automatic expiry or overwrite; existing Schema survives rerun.
- Activation or effect: Python writes configured conventions; their later influence depends on host reads/model interpretation and is unobserved.
- Evidence limits: Source inspection and deterministic deduction only; no initializer execution or vault inspection.

This is the template-rendering part of the setup container, not another setup entry. Bash supplies tool/root/namespaces/date; embedded Python reads the selected Schema, replaces namespace/date tokens and calls write_file. For concrete symbolic input `tool=obsidian`, namespaces `Tech Reference`, date `2026-10-17`, the inspected code maps `{{NAMESPACES}}` to `Wiki/Tech, Wiki/Reference` and `{{DATE}}` to `2026-10-17`, targeting `Wiki/Schema.md`. If that file exists it is skipped; otherwise rendered text is written. This deduction establishes non-truth-apt convention instantiation, not a newly warranted proposition. User flags guide the admitted configuration; unsupported tool/invalid namespace fails before writes. No factual oracle or improvement trigger applies. Recovery is rerun/skip, not transaction rollback. SRC-1, `scripts/init-wiki.sh`, `templates/obsidian/Schema.md`.

> schema = read_template("Schema.md")
> schema = schema.replace("{{NAMESPACES}}", ", ".join(f"Wiki/{ns}" for ns in namespaces))
> write_file(page("Schema"), schema.replace("{{DATE}}", today))
> --- `scripts/init-wiki.sh`

>     if os.path.exists(path):
>         print(f"Skipped (already exists): {label}")
>         return
> --- `scripts/init-wiki.sh`

### Claims

#### EPI-CLM-l1-honesty
Label: L1 honesty objective

SRC-1, `SKILL.md` claims L1 verification keeps rules honest. Distinct from [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision), which concerns L2 selection; supported design mechanism is [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification), not observed correctness.

> **One mechanism keeps L1 honest:**
> --- `SKILL.md`

> - Verdict per CLAIM (a rule usually makes several): `supports` / `contradicts` / `inconclusive`, with what
>     was checked and what was found
> --- `SKILL.md`

> - Overall verdict: contradicts if any claim contradicts; supports if all checked claims support; else
>     inconclusive. Mark it partial when claims stayed unchecked, and name them
> --- `SKILL.md`

The source-supported countercase to overbroad endorsement is an unchecked or remote claim: partial support is not whole-rule truth. The design scenario below also individuates intended contradiction handling, not an observed episode:

> THEN the system SHALL report verdict contradicts, with both paths as evidence
> AND recommend demote or delete
> AND offer re-verify only together with a corrected rule text naming the new path
> AND write nothing until the user chooses
> --- `openspec/specs/prune.md`

#### EPI-CLM-confidence-lifecycle
Label: Confidence lifecycle semantics

SRC-1, `openspec/specs/schema.md` assigns high confidence a verified/reliable/current meaning. No supplied claim counterpart after comparison with [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision); [RT-OBJ-schema](runtime.md#rt-obj-schema) is the governing artifact, not this warrant claim. Ingest requires confidence but its quality gate does not establish factual verification; lint's age downgrade is narrower than these semantics.

> - REQ-533: The `confidence` property follows this lifecycle:
>   - `high` → verified, reliable, up-to-date
>   - `medium` → probably correct, verify on next ingest
>   - `low` → uncertain, incomplete, or limited sources
>   - `stale` → was high/medium but `updated` is 90+ days old
> --- `openspec/specs/schema.md`

> - Downgrade stale confidence from high to stale
> --- `SKILL.md`

#### EPI-CLM-automatic-repromotion
Label: Automatic archived-page re-promotion

SRC-1, `README.md` Prune calls re-promotion automatic. Distinct claim from [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision); closest [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) already correctly describes an offer. This flags a source-document mismatch, not a defect or supersession of runtime.

> the page is still found by the L3 grep fallback (and re-promoted automatically if queried again).
> --- `README.md`

> - If the L3 fallback hits an archived page (`archived::` set) — a re-hit on an evicted page: offer to
>     re-promote it — move its routing line back into the hub `### Index`, drop the archived:: property
> --- `SKILL.md`
