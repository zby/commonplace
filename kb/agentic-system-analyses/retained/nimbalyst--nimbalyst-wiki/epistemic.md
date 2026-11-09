---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Nimbalyst Wiki epistemic routes: attributed session capture, source-backed context, structural checks and later reliance, bounded by external implementations."
run-id: AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01
reviewed-boundary: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
---

# Nimbalyst Wiki epistemic report

## Source-and-claim boundary

This report asks how session material becomes content a later agent may rely on, what checks constrain that reliance, and whether retention establishes accepted new knowledge. The [boundary and Source register](boundary.md#source-register) govern SRC-1 throughout: the released plugin artifact at the frozen commit, not the external CLI, host, browser implementation or team service. There is no registered observed run or causal experiment. Prompt instructions establish requested procedures, not reliable compliance. Integration manifests establish dispatch declarations, not implementations of the dispatched commands.

The principal knowledge claim is session-to-wiki distillation, [EPI-CLM-session-wiki](#epi-clm-session-wiki). The guide also claims a behavioral purpose for retained reasons, [EPI-CLM-reason-reliance](#epi-clm-reason-reliance). Transcript isolation is separately claimed in [RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation). None of these is a claim of infallible truth adjudication.

### Coverage

Direct reads below use SRC-1 at the registered revision. Supplied findings are identified separately; their quotations are not presented as new direct inspection.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
| --- | --- | --- | --- |
| Host MCP and hooks | `.mcp.json`, `.codex-mcp.json`, `hooks/hooks.json` | Direct complete reads; see [RT-RTE-host-entry](runtime.md#rt-rte-host-entry) | Dispatch reaches external code; injected content and predicate correctness unverified. |
| Capture and recall | `skills/capture/SKILL.md`, `skills/recall/SKILL.md` | Direct complete reads; see [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall) | No actual session/page pair establishes fidelity or activation. |
| Page writes, citation checks, repair | `skills/update/SKILL.md` | Direct complete read; [EPI-RTE-citation-check](#epi-rte-citation-check), [EPI-RTE-doctor-check](#epi-rte-doctor-check), [EPI-RTE-doctor-repair](#epi-rte-doctor-repair) | External search, parser, conflict and diagnostic code unavailable. |
| Construction and retained writing policy | `skills/setup/SKILL.md`, `skills/setup/references/wiki-guide.md`, `skills/setup/references/strategic-wiki.md` | Direct complete reads; see [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing) | Intended-use read-back is prescribed, not a completed acceptance record. |
| Legacy knowledge conversion | `skills/update/references/migrating-v1.md` | Direct complete read; [EPI-RTE-legacy-reshape](#epi-rte-legacy-reshape) | No before/after corpus establishes preservation. |
| Formula and assertion alternatives | `skills/update/references/editor-pages.md` | Direct lines 131–166; [EPI-RTE-sheet-derive](#epi-rte-sheet-derive), [EPI-RTE-sheet-check](#epi-rte-sheet-check) | Syntax/examples, not executable evaluator. Other editor formats uninspected here; no complete rendering or transformation verdict. |
| Human choice and source excerpts | `skills/update/references/components.md` | Direct lines 135–178; [EPI-RTE-block-choice](#epi-rte-block-choice) | External app records choices; no run, voting aggregation or enforcement implementation. Other component bodies not inspected; no exhaustive component-level negative. |
| Destination, archives and team migration | `skills/connect/SKILL.md`, `skills/team/SKILL.md` | Direct complete reads; see [RT-RTE-team-transition](runtime.md#rt-rte-team-transition), [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall) | Team migration verification flag and source exclusion are external contracts, not proof of fidelity or freshness. |
| Storage, identity and cooperating writers | `FORMAT.md` | Direct complete read; see [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | Hash/version consistency is not a semantic truth test; direct file editors remain possible. |
| Product claims and alternate clients | `README.md`, `skills/start/SKILL.md` | README lines 1–140 directly read; start completely read; supplied runtime covers other-agent/update sections and manifests | Other clients may lack skills; no universal capture or citation guarantee. |
| Installation, access and machinery succession | root/team plugin manifests, team MCP manifests, README updater sections | Supplied [RT-RTE-host-entry](runtime.md#rt-rte-host-entry), [RT-RTE-plugin-update](runtime.md#rt-rte-plugin-update), [RT-RTE-team-transition](runtime.md#rt-rte-team-transition); not separately re-read | No evidence of release-quality acceptance, access enforcement or self-improvement. |

No executable evaluator was found in the supplied tracked-tree boundary or direct skill reads. The uninspected editor/component alternatives and external implementations prevent a system-complete negative about all evaluation. Provider numerical state is separately uninspected: see [RT-CMP-host-model](runtime.md#rt-cmp-host-model). No model fixity, parameter update, or provider-internal learning conclusion follows.

## Epistemic-object inventory

Object fields belong to the cited declarations; this overlay does not replace the page container.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-decision-prose](#epi-obj-decision-prose) | See record | See record | SRC-1, `skills/update/SKILL.md` | A chosen policy is not itself a factual discovery; who chose it and why are truth-apt. |
| [EPI-OBJ-context-prose](#epi-obj-context-prose) | See record | See record | SRC-1, `skills/update/SKILL.md` | Source-backed does not mean source-verified. |
| [EPI-OBJ-writing-guide](#epi-obj-writing-guide) | See record | See record | SRC-1, `skills/setup/references/wiki-guide.md` | Prescription and empirical rationale differ. |
| [EPI-OBJ-citation-inputs](#epi-obj-citation-inputs) | See record | See record | SRC-1, `skills/update/SKILL.md` | Transcript attribution is not verification of the attributed assertion. |
| [EPI-OBJ-sheet-expressions](#epi-obj-sheet-expressions) | See record | See record | SRC-1, `skills/update/references/editor-pages.md` | Formula inputs, encoding fidelity and evaluation are not established. |
| [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | See record | See record | SRC-1, `FORMAT.md` | Symbolic ID/path/type parts govern location and display, not prose truth. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Not determinable for internal representations | See record | SRC-1, `README.md` | No accessible distributed-parametric content or training trace. |

Open marks are questions, not propositions accepted as true. A `decided` mark records a choice, not a general truth certificate; `current`, a safe ID and successful write likewise carry no semantic validation. See the distinct objects and the capture/recall records.

## Authority-route ledger

Every row separates a function even where one skill performs several. Fields owned by supplied records say **see**; the present report supplies architectural classification and epistemic interpretation. All doctrine-only routes remain unobserved. BAP abbreviates the behavioral-authority path (consumer, channel, force, horizon).

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-host-entry](runtime.md#rt-rte-host-entry) | operational admission/selection/consumption | implemented | See record | no content change | See record | See record | See record | See record | Dispatch declaration only | No truth license from hook invocation | See record | See record | SRC-1, `hooks/hooks.json` | none | none | CLI outputs uninspected; implemented applies only to manifest wiring. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | content transformation | doctrine only | [EPI-OBJ-decision-prose](#epi-obj-decision-prose), [EPI-OBJ-context-prose](#epi-obj-context-prose) | truth-apt transformation: indeterminate | See record | See record | See record | See record | Requested, not enforcing | Attribution/source support is requested; generated sentence fidelity unknown | See record | See record | SRC-1, `skills/capture/SKILL.md` | [EPI-CLM-session-wiki](#epi-clm-session-wiki) | No universal capture | Could import, reshape, or infer; no concrete output decides entailment/non-entailment. |
| [EPI-RTE-citation-check](#epi-rte-citation-check) | check/evidence production | doctrine only | [EPI-OBJ-citation-inputs](#epi-obj-citation-inputs) | no content change | See record | See record | See record | See record | No inspected enforcement | Supports attribution only, conditional on genuine input and model comparison | See record | See record | SRC-1, `skills/update/SKILL.md` | [RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation) | Quote optional | A missing tool quote does not reject all content. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | disposition/acceptance | doctrine only | [EPI-OBJ-decision-prose](#epi-obj-decision-prose) | no content change | Worth recording and appropriate page, not global factual truth | See record | See record | Write, omit routine material, or ask | Requested model selection; direct edits | Admission to wiki is not evidence-consuming acceptance of a novel claim | See record | See record | SRC-1, `skills/capture/SKILL.md` | [EPI-CLM-session-wiki](#epi-clm-session-wiki) | No review step | People supplying decisions does not mean they approve each synthesized sentence. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | retention | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | See record | See record | See record | See record | See record | Persistence adds no warrant | See record | See record | SRC-1, `skills/update/SKILL.md` | none | none | Successful persistence not observed. |
| [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-decision-prose](#epi-obj-decision-prose), [EPI-OBJ-context-prose](#epi-obj-context-prose) | truth-apt transformation: indeterminate | See record | See record | See record | See record | Advisory/contextual request | Report what wiki says; disclose stale content and separate inference | See record | See record | SRC-1, `skills/recall/SKILL.md` | [EPI-CLM-reason-reliance](#epi-clm-reason-reliance) | Reliance not proof | Model-generated answer may reshape or infer; no output supplied. |
| [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing) | behavior/policy adaptation | doctrine only | [EPI-OBJ-writing-guide](#epi-obj-writing-guide) | non-truth-apt policy/content update: team writing preferences | See record | See [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) for admission | See record | See record | Explicit prompt priority, not enforcement | No factual truth license from guide priority | See record | See record | SRC-1, `skills/update/SKILL.md` | none | Guide exception to page-as-data | Retained policy can shape writing without producing knowledge. |
| [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) | check/evidence production | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | Read-back content, placement, links and rendering against intended use | Agent, available browser and user brief; artifact usability domain | After writes, before claiming complete | Confirm or report incomplete/gaps | Prescribed completion gate | Checks availability/usability, not truth of all source claims | See record | Foreground agent, read-back/report, advisory completion policy, setup invocation | SRC-1, `skills/setup/SKILL.md` | none | none | No completed check/acceptance result supplied. |
| [EPI-RTE-doctor-check](#epi-rte-doctor-check) | check/evidence production | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | no content change | See record | See record | See record | See record | Diagnostic, changes nothing | Structural/freshness indicators only | See record | See record | SRC-1, `skills/update/SKILL.md` | none | Stale is not false | No evaluator implementation or precision evidence. |
| [EPI-RTE-doctor-repair](#epi-rte-doctor-repair) | disposition/acceptance | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | truth-apt transformation: indeterminate | See record | See record | See record | See record | Requested edits/withdrawal of current status | Marking outdated withholds current-use confidence; merging alone establishes no truth | See record | See record | SRC-1, `skills/update/SKILL.md` | none | none | Structural repair and semantic revision differ; outputs unknown. |
| [EPI-RTE-legacy-reshape](#epi-rte-legacy-reshape) | content transformation | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | truth-apt transformation: indeterminate | See record | See record | See record | See record | Requested migration | Intended preservation of sources, basis, scope and limitations; actual warrant unknown | See record | See record | SRC-1, `skills/update/references/migrating-v1.md` | none | Qualifiers dropped, meaning kept in prose by policy | Intended non-ampliative reshaping not established for any output. |
| [EPI-RTE-sheet-derive](#epi-rte-sheet-derive) | content transformation | doctrine only | [EPI-OBJ-sheet-expressions](#epi-obj-sheet-expressions) | truth-apt transformation: entailed derivation | See record | See record | See record | See record | Display contract only | Conditional arithmetic consequence of stated inputs, not source truth | See record | See record | SRC-1, `skills/update/references/editor-pages.md` | none | none | No inspected deterministic implementation; no claim of executed calculation. |
| [EPI-RTE-sheet-check](#epi-rte-sheet-check) | check/evidence production | doctrine only | [EPI-OBJ-sheet-expressions](#epi-obj-sheet-expressions) | no content change | See record | See record | See record | See record | Check syntax; consequential consumer uninspected | Positivity predicate only, not economic/model adequacy | See record | See record | SRC-1, `skills/update/references/editor-pages.md` | none | No admission consumer shown | Cannot treat assertion as page/claim acceptance. |
| [EPI-RTE-block-choice](#epi-rte-block-choice) | disposition/acceptance | doctrine only | [EPI-OBJ-decision-prose](#epi-obj-decision-prose) | non-truth-apt policy/content update: human choice and vote | See record | See record | See record | See record | Human choice followed by requested mark | Records preference/choice, no general truth warrant | See record | See record | SRC-1, `skills/update/references/components.md` | none | none | Recording votes is not evidence-consuming acceptance of an ampliative claim. |
| [RT-RTE-team-transition](runtime.md#rt-rte-team-transition) | lineage/freshness/recovery | doctrine only | [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) | truth-apt transformation: indeterminate | See record | See record | See record | See record | See record | Migration verification concerns copying, not endorsement | See record | See record | SRC-1, `skills/team/SKILL.md` | none | Archive must not masquerade as current | Page text bypasses conversation; no inspected server transformation or independent comparison. |

No lifecycle-integration route **after epistemic acceptance of a produced ampliative claim** is established by these reads. Linking, organizing, retaining and using prose are prescribed, but do not supply the missing acceptance event. This is not a claim that the product must use a separate acceptance phase, or that no human can evaluate its contents.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-session-wiki](#epi-clm-session-wiki) | See record | SRC-1, `README.md`; reported operation/design | See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | [RT-RTE-host-entry](runtime.md#rt-rte-host-entry) for dispatch only | None supplied | No intervention; capture can say nothing to record; Codex lacks hook reminders | A detailed prescribed session-to-wiki route exists | Actual faithful distillation and universal decision coverage unknown. |
| [EPI-CLM-reason-reliance](#epi-clm-reason-reliance) | See record | SRC-1, `skills/setup/references/wiki-guide.md`; doctrine/design | See [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall), [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing) | None for model compliance | None supplied | No later code-choice comparison or ablation of reasons | Retained reasons are intended to constrain later action | Prevention of unwanted reversals is not demonstrated. |
| [RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation) | See record | SRC-1, `skills/update/SKILL.md`; doctrine/design | See record and [EPI-RTE-citation-check](#epi-rte-citation-check) | [RT-RTE-host-entry](runtime.md#rt-rte-host-entry) dispatch only | None supplied | Transcript reader unavailable; manual attribution and team comments are alternate routes | Current-session citation restriction is specified | Actual isolation and quotation fidelity unverified; not a universal citation requirement. |

## Bounded conclusion

Nimbalyst Wiki prescribes acquiring people's decisions and source-linked context, synthesizing them into affected pages, and retrieving a few relevant full pages before future answers or code work. The source warrants an attribution-oriented design, not verified preservation of source warrant: citations should remain verbatim, changing facts carry dates, guesses must stay distinct, and missing data should remain explicit. No actual input/output pair establishes fidelity. Model-produced prose therefore has an indeterminate content relation here, not automatically an ampliative conjecture and not automatically an entailed summary. See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [EPI-RTE-citation-check](#epi-rte-citation-check), and [EPI-RTE-legacy-reshape](#epi-rte-legacy-reshape).

The checks have different licenses. Source-support comparison concerns the attribution of a sentence; setup read-back concerns content presence and intended usability; `wikiDoctor` concerns links, coverage and freshness; version hashes concern concurrent writes. None establishes all page assertions as true. Diagnostic results have a prescribed consumer that repairs links, merges duplicates or marks pages outdated. That is an operational withdrawal/repair path, not a universal rejection oracle. Formula/assertion syntax offers a separate formal-domain alternative: arithmetic can conditionally derive a result, while an assertion checks a particular predicate. Its implementation and any acceptance consequence are uninspected. See [EPI-RTE-doctor-check](#epi-rte-doctor-check), [EPI-RTE-doctor-repair](#epi-rte-doctor-repair), [EPI-RTE-sheet-derive](#epi-rte-sheet-derive), and [EPI-RTE-sheet-check](#epi-rte-sheet-check).

Ordinary wiki edits land without per-edit review. Human decisions are imported subject matter; the agent's admission of prose is not the same decision. Setup permits purpose/depth choice and requires approval for replacing a customized guide; the guide then has explicit later writing authority through read-before-write instructions. Recall gives retained decisions contextual force in later coding work, while requiring attribution, freshness caveats and separation of inference. A decision block separately records human choices and votes. These are identified behavioral-authority paths, not observed behavior changes. See [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing), [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall), and [EPI-RTE-block-choice](#epi-rte-block-choice).

No supplied run records an evidence-consuming acceptance of a new ampliative proposition against a named criterion, intended use and scope. The architecture does prescribe source support and artifact-completion criteria, so it is not accurately described as having no checks. Nor does persistence alone establish learning, exercised reflection, autonomous theory building or self-improvement. No content-directed criticism and next-round outcome is supplied; model internals are uninspected. Retained writing guidance has a prospective consumer, but that positive path is independent of unestablished improvement or causal benefit. These bounds apply to the partial loop and inspected alternatives, not to every possible external host/server behavior.

## Shared records

### Operative objects

#### EPI-OBJ-decision-prose
Label: Decision sentences and reasons
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Natural-language sentences about what a person chose, alternatives, reasons and dates persist in Markdown page bodies. Mark attributes are symbolic selectors/display metadata; people/models interpret the claim and rationale. Distinct from the container's ID/type machinery and from factual context below. The empirical proposition is that a person made the recorded choice, not that the choice is universally correct. SRC-1, `skills/update/SKILL.md`.

> When a decision changes, rewrite the sentence and say what it replaced and when.
> --- `skills/update/SKILL.md`

#### EPI-OBJ-context-prose
Label: Source-linked factual context
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Natural-language facts about limits, pricing, maturity and capabilities, with ordinary source links and checked dates, persist in Markdown bodies. The later reader is a person or host model. This is distinct from decision attribution: an authentic quotation can still assert a false external fact. SRC-1, `skills/update/SKILL.md`.

> Facts the team weighs (limits, pricing, maturity, what a competitor ships) carry a source and the date you checked it.
> --- `skills/update/SKILL.md`

#### EPI-OBJ-writing-guide
Label: How we write this wiki
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

The installed guide is natural-language policy in a retained page; the shipped base is Markdown. Its rules are prescriptions, while statements about their effects can be truth-apt. Distinct page part with an overriding writing consumer, already described by [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing); this object does not duplicate that path. SRC-1, `skills/setup/references/wiki-guide.md`.

> Mark what is decided, what was observed and what is a guess. Never present a guess as a decision.
> --- `skills/setup/references/wiki-guide.md`

#### EPI-OBJ-citation-inputs
Label: Citable session and comment inputs

Tool-returned ready citation Markdown contains quoted natural-language statements and identity/time/link metadata. Tool payload storage is external/uninspected; a copied citation persists in a page. Distinct from [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages): the referent here is the upstream evidence payload, not the retained destination. SRC-1, `skills/update/SKILL.md`.

> Each entry carries ready `citation` markdown (a console link whose title holds who, email, when and the quote). Paste it unchanged; never write or edit one by hand, and attach a person's words only when they support the sentence.
> --- `skills/update/SKILL.md`

#### EPI-OBJ-sheet-expressions
Label: Spreadsheet and calc expressions
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

CSV formulas and calc-sheet expressions/assertions are symbolic text in `.csv` and `.calc.md` editor-page files, consumed under fixed arithmetic/check rules by external editors. Comments/prose are separately human/model interpreted. Named inputs can denote prices and quantities; results can assert numerical consequences over those inputs. Distinct from prose and page identity parts because evaluation consumers differ. SRC-1, `skills/update/references/editor-pages.md`.

> A cell starting with `=` is a formula with A1 references.
> --- `skills/update/references/editor-pages.md`

### Routes

#### EPI-RTE-citation-check
Label: Sentence support comparison
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

The foreground agent compares a candidate sentence with returned session/comment words before attaching ready citation Markdown. This is the checking part, distinct from capture's production and write admission. Domain: whether these particular words support this attribution/sentence, not external factual truth. The human supplies original words; the model judges support and can withhold the citation. No expected-answer oracle or mandatory human sentence approval is specified. Open-request mode. SRC-1, `skills/update/SKILL.md`; evidence passage in [EPI-OBJ-citation-inputs](#epi-obj-citation-inputs).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Supported citation attachment, no attachment, or prose attribution when neither tool lists the input.
- Later read-back: The attached quote/link is intended to reach later page readers; route itself only compares support.
- Delegated visibility: Foreground agent receives listed inputs; session-tool isolation is an external claim.
- Selection predicate: Person-origin statement; session prompt/answer or team comment query.
- Invalidation or expiry: Rewritten sentence needs renewed support comparison by policy; no automatic citation withdrawal is specified.
- Activation or effect: Agent should attach words only when supportive, but absence of a quote does not block recording a signed-in person's decision.
- Evidence limits: No support-classification implementation or observed sentence/quote pair; no guaranteed truth inference.

> If neither lists it, name the person and where it was said in prose: `(Dana Lee, in a Claude Code session, 2026-10-01)`.
> --- `skills/update/SKILL.md`

#### EPI-RTE-doctor-check
Label: Wiki structural diagnosis

After a large local rework, external `wikiDoctor` returns structural/freshness findings to the agent. No exact counterpart after comparison with [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup): this is the explicit diagnostic operation in update, not session candidate generation or setup read-back. Target: wiki links, orphaning, stale coverage, duplicate titles and current pages with dead paths. Program evaluates these classes, while its implementation is uninspected. No reference-answer oracle is supplied. Open maintenance mode; no content proposal is admitted by the diagnostic itself. SRC-1, `skills/update/SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Issues, orphans, stale pages, duplicateTitles and deadPaths; changes nothing.
- Later read-back: inapplicable — diagnostic itself does not retain content.
- Delegated visibility: Agent receives report; external server inspects wiki/code coverage by contract.
- Selection predicate: Large rework, and before claiming the wiki is tidy.
- Invalidation or expiry: Findings describe scanned state; subsequent edits can supersede them; no TTL specified.
- Activation or effect: Supplies targets to the repair route, not semantic endorsement.
- Evidence limits: Diagnostic algorithm, false positives and actual output uninspected.

> After a large rework, and before saying the wiki is tidy, call `wikiDoctor`. It changes nothing;
> --- `skills/update/SKILL.md`

#### EPI-RTE-doctor-repair
Label: Diagnostic disposition and repair

Endpoints: `wikiDoctor` findings to foreground-agent page/link/status edits through external wiki tools. This consumes [EPI-RTE-doctor-check](#epi-rte-doctor-check), not another check. Distinct from ordinary [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): diagnostic-triggered maintenance need not originate in a session decision. The model chooses correction, merge or outdated marking; it should ask before deleting/rewriting others' prose. No oracle for the truth of repaired prose is supplied. Guidance is update/guide, persists as edits/status. Recovery is prescribed reread on conflict, local trash or team history as applicable, not observed rollback. SRC-1, `skills/update/SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Small repair writes and links to changed pages.
- Later read-back: Revised pages/statuses reach recall; outdated content must be disclosed rather than treated as current.
- Delegated visibility: Foreground model sees diagnostics and pages; server receives mutations.
- Selection predicate: Diagnostic category and affected page; repair or mark outdated when meaningful update cannot be made.
- Invalidation or expiry: Subsequent code/page changes can obsolete repair; no general expiry.
- Activation or effect: Fix links/paths, connect orphans, merge duplicates, update content or withdraw current status.
- Evidence limits: Prescribed disposition only; no observed repaired page, verified semantic merge or implementation enforcement.

> scan `issues` such as broken links, `orphans` to link from the page they belong under or from Home, `stale` pages to update or mark `outdated`, `duplicateTitles` to merge into one page, and `deadPaths` (a `current` page whose `paths` match no file) to correct or mark `outdated`.
> --- `skills/update/SKILL.md`

#### EPI-RTE-legacy-reshape
Label: Legacy item to prose conversion

The foreground agent converts earlier claim/finding/investigation items into sourced prose, preserving keys and selected metadata. Distinct from [RT-RTE-team-transition](runtime.md#rt-rte-team-transition), which copies local wiki pages between stores; distinct from [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), which explicitly leaves legacy migration as a separate job. Intended non-ampliative reshaping includes writing basis as words, preserving scope/limitations, and dropping qualifiers while retaining relevant meaning. Actual semantic relation is indeterminate without outputs. Human starts the migration and sees the proposed mapping; only human approval permits retiring old material, item/batch scoped. Agent proposes destinations and can leave items explicitly unmigrated; no reference-answer oracle. Guidance persists in pages and old-key lineage links. SRC-1, `skills/update/references/migrating-v1.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Area-by-area page writes and report of retained/unmigrated old items.
- Later read-back: New prose and old keys are available to later readers; old items remain until approved retirement.
- Delegated visibility: Agent reads old items and writes new pages; no separate inference worker specified.
- Selection predicate: User-started earlier-model migration, mapped by item kind and subject.
- Invalidation or expiry: Superseded claims keep current value, with previous value/date when relevant; retirement requires approval.
- Activation or effect: Changes representation and location while requesting source/attribution preservation; no new factual acceptance supplied.
- Evidence limits: No concrete converted corpus or execution; dropping qualifier structure could lose meaning despite preservation instructions.

> **Keep every source.** Each citation, URL, session id, document link and date on an old item goes into the sentence it supports.
> --- `skills/update/references/migrating-v1.md`

> The answer written as a decision or a conclusion on the page the question affects, with the claims it rested on as linked sources. Keep `scope` and `limitations` as one sentence each.
> --- `skills/update/references/migrating-v1.md`

#### EPI-RTE-sheet-derive
Label: Formula consequence display

Endpoints are formula inputs in CSV/calc editor files to numerical results displayed by an external editor. Distinct from [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) and capture: an editor formula consumer, not model synthesis. Fixed-rule symbolic semantics are documented but implementation uninspected. In the documented calc example, conditional on `seats = 25`, `price = 12 USD`, and `discount = 0.1`, the stated expressions specify monthly 270 USD and yearly 3240 USD. This is arithmetic interpretation of a documentation example, not a trace through inspected executable code or evidence of source-price truth. SRC-1, `skills/update/references/editor-pages.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Intended formatted computed values.
- Later read-back: Expressions persist in editor-page files and may be reopened; exact result caching uninspected.
- Delegated visibility: Editor receives file; host model may see text or displayed values, not established for a run.
- Selection predicate: Opening/evaluating CSV formula cells or named calc expressions; exact reevaluation trigger uninspected.
- Invalidation or expiry: Input edits should change results under formula semantics; propagation implementation uninspected.
- Activation or effect: Intended numerical display, with no evidenced downstream policy/claim admission consumer.
- Evidence limits: Doctrine/example only; cannot establish executable arithmetic correctness, units handling or observed benefit.

> monthly = seats * price * (1 - discount) -> currency(USD, 2)
> yearly = monthly * 12 -> currency(USD, 0)
> assert yearly > 0 USD
> --- `skills/update/references/editor-pages.md`

#### EPI-RTE-sheet-check
Label: Calc assertion check

The calc assertion assesses a particular expression, separate from [EPI-RTE-sheet-derive](#epi-rte-sheet-derive)'s result production. Its target in the example is positivity of yearly revenue in USD, not the economic adequacy of the pricing model. External symbolic evaluator and failure display/admission effects are uninspected. No counterpart in supplied runtime; shared evidence with the derivation route, distinct function. SRC-1, `skills/update/references/editor-pages.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Intended check result for the asserted expression; exact failure result unspecified here.
- Later read-back: Assertion text persists with sheet; check-result persistence uninspected.
- Delegated visibility: External calc editor receives formula/assertion text.
- Selection predicate: An `assert` line in a calc sheet; exact evaluation timing uninspected.
- Invalidation or expiry: Inputs may change; recomputation and stale-result handling uninspected.
- Activation or effect: No inspected acceptance, rejection, rollback or continuation consumer; cannot assign enforcing force.
- Evidence limits: Check syntax alone establishes neither operational admission nor truth beyond the predicate and premises.

> `assert <expression>` to check one, and `// comment`. Any other line is prose.
> --- `skills/update/references/editor-pages.md`

#### EPI-RTE-block-choice
Label: Human decision block outcome

A page contains a question addressed to named people; the external app records their choices/votes and the agent should copy the resolved outcome into a decision mark. No exact counterpart after comparison with [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): the input here is an in-page interactive choice, not a terminal session. Open collaborative-choice mode. People answer, may decline an offered choice, and can supply write-ins where enabled; agent proposes question/options. No aggregation or tie rule, truth criterion, oracle or per-outcome veto implementation is established. Guidance says use only for unresolved choices and not to manufacture votes; persistence is block outcome plus mark. Recovery/history remains external. SRC-1, `skills/update/references/components.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Recorded answer, respondent, time and votes; exact interactive response uninspected.
- Later read-back: Outcome and decision mark persist for page/mark readers.
- Delegated visibility: Named people see choice in page; app records results; agent reads outcome for marking.
- Selection predicate: Team must choose and people asked can be named; not for a choice already made.
- Invalidation or expiry: Subsequent changed decisions follow rewrite/replacement policy; block reopening semantics uninspected.
- Activation or effect: Records a human choice and requests a decided mark, not automatic code execution or factual endorsement.
- Evidence limits: UI implementation, actual votes, aggregation and later reliance uninspected.

> The app records the answer, who answered, when, and each vote in the block; never write `resolved`, `resolvedAt`, `resolvedBy` or `votes` yourself.
> --- `skills/update/references/components.md`

> Once a block is resolved, also write the outcome as a `decided` mark in the page it affects.
> --- `skills/update/references/components.md`

### Claims

#### EPI-CLM-session-wiki
Label: Sessions become project wiki

The README claims a coding-agent session can become a Markdown wiki with decisions in affected pages. This is distinct from [RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation): knowledge retention/synthesis rather than source-reader privacy. SRC-1, `README.md`, reported operation/design; no observed run.

> Your agent distills what you worked on into a wiki of plain markdown files: a Home page, the decisions you made and why, open questions with owners, and the things you track.
> --- `README.md`

#### EPI-CLM-reason-reliance
Label: Reasons prevent reversal

The shipped guide says retaining a decision's reason stops a later agent undoing it. This is a consequential behavioral-purpose claim, distinct from transcript isolation and the broader session-to-wiki claim. It is not interpreted as a theorem of guaranteed obedience. SRC-1, `skills/setup/references/wiki-guide.md`, doctrine/design.

> The reason is what stops a later agent from undoing the decision.
> --- `skills/setup/references/wiki-guide.md`
