---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Exocomp's truth-apt content, structural signoff, report withdrawal and model-facing authority routes at the frozen revision."
run-id: AAS-2026-10-14-exocomp-692bb27c35f9-01
reviewed-boundary: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
---

# Exocomp epistemic report

## Source-and-claim boundary

The question is what licenses reliance on Exocomp's project claims and what those claims can change. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). All new evidence below is SRC-1 at the frozen commit, implementation unless labelled doctrine/design. No target execution, provider call or experiment was performed. Historical stored sessions are not used to establish current-revision operation.

The runtime is a useful baseline, not an inspection ceiling. Direct inspection adds report closure, requirement regeneration, website imports and human answers. The supplied [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff) now distinguishes reconstructed implemented status from durable signoff: the writer omits implemented entries; later reads reconstruct them from source, with empty behavior. [EPI-RTE-requirement-refresh](#epi-rte-requirement-refresh) retains the corresponding lineage analysis.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Main CLI variants and debug restore | SRC-1 `source/cmds/exocomp/main.go`, `source/cmds/exocomp-agent/main.go`, `source/cmds/exocomp-web/main.go`, `source/cmds/agimus/main.go` | Direct dispatch search checked against supplied [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | No executed invocation |
| Tool registration and completion hook | SRC-1 `source/tools/Toolset.go`, `source/ui/jsonl/Client.go` | Direct reads; registered agents, bugs, changelog, files, humans, programs, requirements, skills, websites; QuitHook exits from supplied success, not an independent evaluator; [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) | No claim of reliable task completion from process termination |
| Model requests, adapter, ordinary tools, backup, restore | SRC-1 `source/engine/Session.go`, `source/engine/Recovery.go`, `source/adapters/DeepSeek.go` | Supplied runtime findings: [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat), [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-program-execution](runtime.md#rt-rte-program-execution) | Provider internals, weights, actual compliance and test outcomes uninspected |
| Requirements definition, check, cleanup and reconstruction | SRC-1 `source/tools/Requirements.go`, `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/tools/writeRequirements.go`, `source/utils/ast/HasSymbol.go`, `source/utils/ast/hasFunc.go`, `source/utils/ast/GetPackageSymbols.go` | Direct reads of DefineFunc, Signoff, List and helpers; [EPI-RTE-symbol-check](#epi-rte-symbol-check), [EPI-RTE-signoff-disposition](#epi-rte-signoff-disposition), [EPI-RTE-requirement-refresh](#epi-rte-requirement-refresh) | Other Define variants and AST extraction helpers not fully inspected; no complete declaration-fidelity claim |
| Bug reporting, closure and selection | SRC-1 `source/tools/Bugs.go`, `source/tools/readBugs.go`, `source/tools/writeBugs.go` | Direct Add/Fix/List and persistence reads; [EPI-RTE-bug-records](#epi-rte-bug-records), [EPI-RTE-bug-closure](#epi-rte-bug-closure) | Search branches not fully read; List exclusion does not imply universal erasure |
| Changelog and Remove | SRC-1 `source/tools/Changelog.go`, `source/tools/writeChangelog.go` | Direct wrappers/createEntry/writer; [EPI-RTE-changelog-records](#epi-rte-changelog-records) | Detailed UI rendering and Search uninspected |
| Human clarification and confirmation | SRC-1 `source/tools/Humans.go`, `source/engine/Session.go`, `source/ui/web/routes/session/CallTool.go`, `app/engine/Session.go`, `app/controllers/Chat.go`, `source/agents/planner.yaml` | Direct Ask/Choose/Answer/Await/HasMethod, qualified and bare-name Session consumers, ToolCall/Command name parsing, web CallTool, browser AnswerQuestion/Waiting gate and prompt reads; [EPI-RTE-human-answers](#epi-rte-human-answers) | Qualified dispatch admits Answer and released Ask/Choose results as generic tool messages; only bare-name Answer reaches the bounds defect. Browser submission is conditional on its Waiting gate. No authenticated respondent or acceptance instance |
| External imports | SRC-1 `source/tools/Websites.go`, `source/tools/getWebsiteText.go`, `source/tools/getWebsiteMarkdown.go`, `source/tools/Files.go` | Direct Fetch/helper/Files.Read reads; [EPI-RTE-website-fetch](#epi-rte-website-fetch) | HTML parser internals, Websites.Stat, file Search/ReadSymbol not fully inspected; no complete extraction-fidelity verdict |
| Summarization | SRC-1 `source/utils/chat/SummarizeMessages.go`, `source/utils/fmt/FormatSingleLine.go`, `source/utils/fmt/isPrintableASCII.go`, `source/agents/summarizer.yaml` | Direct projection/formatter/prompt reads; supplied Inquire consumer; [EPI-RTE-inquire-projection](#epi-rte-inquire-projection) | Model summary semantic relation remains indeterminate |
| Skills and build/install | SRC-1 `source/tools/Skills.go`, `source/engine/Session.go`, `source/schemas/ToolCall.go`, `source/types/Command.go`, `toolchain/actions/BuildExocomps.go`, `installer/actions/InstallExocomp.go` | Direct qualified/bare-name dispatch and Load/Unload/helper reads; supplied [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading), [RT-ABS-skill-grants](runtime.md#rt-abs-skill-grants), [RT-RTE-build-install](runtime.md#rt-rte-build-install) | No activated skill or compiled/installed executable evidence |
| Tests, browser and retained examples | SRC-1 `docs/TESTING.md`, `source/agents/tester.yaml`, `app/controllers/`, `sessions/` | Direct testing doctrine; browser/state consumption supplied by boundary/runtime; historical artifacts deliberately unused | Tests not run; no efficacy estimate, causal attribution or system-complete negative about acceptance in all possible project workflows |

No separate evaluation hook was identified by the scoped CLI/engine/UI hook search. The identified Quit hook is a termination consumer. This scoped finding is not a whole-repository absence claim. Consequential design claims are [EPI-CLM-correct-results](#epi-clm-correct-results), [EPI-CLM-summary-fidelity](#epi-clm-summary-fidelity) and the supplied [RT-CLM-role-separation](runtime.md#rt-clm-role-separation).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-specification](#epi-obj-specification) | See record | See record | SRC-1 `source/tools/Requirements.go` | Intended behavior is normative; existence and implementation assertions are truth-apt |
| [EPI-OBJ-implemented-status](#epi-obj-implemented-status) | See record | See record | SRC-1 `source/tools/readImplementedRequirements.go` | Not a behavioral satisfaction certificate |
| [EPI-OBJ-bug-description](#epi-obj-bug-description) | See record | See record | SRC-1 `source/tools/Bugs.go` | Report truth not checked by storage |
| [EPI-OBJ-fixed-status](#epi-obj-fixed-status) | See record | See record | SRC-1 `source/tools/Bugs.go` | Closure and report content have distinct consumers |
| [EPI-OBJ-changelog-entry](#epi-obj-changelog-entry) | See record | See record | SRC-1 `source/tools/Changelog.go` | A record named Fix/Remove is not a checked repair/deletion |
| [EPI-OBJ-website-content](#epi-obj-website-content) | See record | See record | SRC-1 `source/tools/Websites.go` | Remote source warrant unknown |
| [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) | Assistant assertions can be truth-apt; exact propositions not determinable without an instance | See record | SRC-1 `source/engine/Session.go` | Tool choice is policy, not necessarily a proposition |
| [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) | Quit reports may assert completed work | See record | SRC-1 `source/tools/getAgentWorkReport.go` | Report presence and truth differ |
| [EPI-RTE-human-answers](#epi-rte-human-answers) | Answers may supply facts, preferences or approval; instance-dependent | See record | SRC-1 `source/tools/Humans.go` | Not all answers are truth-apt |
| [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire) | Projected prose and model summary | See record; projection part below | SRC-1 `source/utils/chat/SummarizeMessages.go` | Summary instance and semantic preservation unknown |
| [RT-OBJ-role-grants](runtime.md#rt-obj-role-grants), [RT-BAP-role-prompt](runtime.md#rt-bap-role-prompt) | Grants and imperatives are policy, not truth-apt updates | See records | SRC-1 `source/agents/NewAgent.go` | Factual claims inside prompts assessed separately |
| [RT-CMP-planner-model](runtime.md#rt-cmp-planner-model), [RT-CMP-coder-model](runtime.md#rt-cmp-coder-model), [RT-CMP-summarizer-model](runtime.md#rt-cmp-summarizer-model) | Individuated parameter-encoded propositions not determinable | See records | SRC-1 `source/types/Config.go` | Weights, training provenance and provider-side updates inaccessible |

## Authority-route ledger

Each row is one function. `See` delegates record-owned fields rather than redeclaring them. No row establishes observed operation. The locally assessed content relation and architectural status are independent of a record's conclusion-status vocabulary.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) | content transformation | implemented | See record | truth-apt transformation: indeterminate | See record | See record | See record | See record | See record | Candidate assertions, not accepted ampliative claims | See record | See record | SRC-1 `source/engine/Session.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | none | No proposition/inputs to establish non-entailment |
| [RT-RTE-contractor-work](runtime.md#rt-rte-contractor-work) | operational admission/selection/consumption | implemented | See record | no content change | See record | See record | See record | See record | See record | Quit report presence licenses workflow continuation, not report truth | See record | See record | SRC-1 `source/tools/Agents.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | completion versus correctness | Report not independently checked |
| [RT-RTE-program-execution](runtime.md#rt-rte-program-execution) | check/evidence production | implemented | Caller-selected code/test | no content change | Proposed program behavior on selected test cases | External executed program and caller-written tests; see record | See record | See record | See record | At most test-specific outcome if obtained; no general correctness license | See record | See record | SRC-1 `source/tools/Programs.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | none | No actual tests or reference answers supplied |
| [EPI-RTE-symbol-check](#epi-rte-symbol-check) | check/evidence production | implemented | [EPI-OBJ-implemented-status](#epi-obj-implemented-status) | truth-apt transformation: entailed derivation | See record | See record | See record | See record | See record | AST predicate result over parseable bytes only | See record | See record | SRC-1 `source/utils/ast/HasSymbol.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | narrow structural license | Parsing is not type checking or behavioral testing |
| [EPI-RTE-signoff-disposition](#epi-rte-signoff-disposition) | disposition/acceptance | implemented | [EPI-OBJ-implemented-status](#epi-obj-implemented-status) | non-truth-apt policy/content update: status assignment | See record | See record | See record | See record | See record | Structural disposition only; criterion is not spec behavior | See record | See record | SRC-1 `source/tools/Requirements.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | implemented label exceeds behavioral check | Not acceptance of an explanatory claim |
| [EPI-RTE-requirement-refresh](#epi-rte-requirement-refresh) | lineage/freshness/recovery | implemented | [EPI-OBJ-specification](#epi-obj-specification), [EPI-OBJ-implemented-status](#epi-obj-implemented-status) | truth-apt transformation: non-ampliative reshaping | See record | See record | See record | See record | See record | Source-derived symbol availability, not preserved intent/warrant | See record | See record | SRC-1 `source/tools/readRequirements.go` | none | source-first reconstruction | Behavior/rationale can disappear from reconstituted requirements |
| [EPI-RTE-bug-records](#epi-rte-bug-records) | content transformation | implemented | [EPI-OBJ-bug-description](#epi-obj-bug-description) | truth-apt transformation: acquisition/import | See record | See record | See record | See record | See record | Imported caller claim; source warrant unknown | See record | See record | SRC-1 `source/tools/Bugs.go` | none | none | Software does not diagnose the bug from evidence |
| [EPI-RTE-bug-records](#epi-rte-bug-records) | retention | implemented | [EPI-OBJ-bug-description](#epi-obj-bug-description) | no content change | See record | See record | See record | See record | See record | Retention is not acceptance | See record | See record | SRC-1 `source/tools/writeBugs.go` | none | none | Direct file overwrite, not a provenance ledger |
| [EPI-RTE-bug-closure](#epi-rte-bug-closure) | disposition/acceptance | implemented | [EPI-OBJ-fixed-status](#epi-obj-fixed-status) | non-truth-apt policy/content update: report closure | See record | See record | See record | See record | See record | No evidential repair license | See record | See record | SRC-1 `source/tools/Bugs.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | closure without repair check | Caller may have evidence; method does not require it |
| [EPI-RTE-bug-closure](#epi-rte-bug-closure) | operational admission/selection/consumption | implemented | [EPI-OBJ-fixed-status](#epi-obj-fixed-status) | no content change | See record | See record | See record | See record | See record | No new truth warrant | See record | See record | SRC-1 `source/tools/Bugs.go` | none | none | List exclusion is enforcing selection, not proof model changes priorities |
| [EPI-RTE-changelog-records](#epi-rte-changelog-records) | content transformation | implemented | [EPI-OBJ-changelog-entry](#epi-obj-changelog-entry) | truth-apt transformation: acquisition/import | See record | See record | See record | See record | See record | Caller claim with unknown source warrant | See record | See record | SRC-1 `source/tools/Changelog.go` | none | Remove is an entry, not deletion | No validation of described event |
| [EPI-RTE-changelog-records](#epi-rte-changelog-records) | retention | implemented | [EPI-OBJ-changelog-entry](#epi-obj-changelog-entry) | no content change | See record | See record | See record | See record | See record | No acceptance from persistence | See record | See record | SRC-1 `source/tools/writeChangelog.go` | none | none | De-duplication is not corroboration |
| [EPI-RTE-website-fetch](#epi-rte-website-fetch) | content transformation | implemented | [EPI-OBJ-website-content](#epi-obj-website-content) | truth-apt transformation: acquisition/import | See record | See record | See record | See record | See record | Source warrant unknown; URL/status retained, meaning may be degraded | See record | See record | SRC-1 `source/tools/Websites.go` | none | none | 16 MiB bound and parser conversion; no factual validation |
| [EPI-RTE-human-answers](#epi-rte-human-answers) | content transformation | implemented | See record | truth-apt transformation: acquisition/import | See record | See record | See record | See record | See record | Conditional on an answer being truth-apt; provenance/warrant unknown | See record | See record | SRC-1 `source/tools/Humans.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | human label is not authentication | Qualified Answer imports into Humans.contents and generic Session messages; browser submission may be blocked by Waiting |
| [EPI-RTE-human-answers](#epi-rte-human-answers) | operational admission/selection/consumption | implemented | See record | no content change | See record | See record | See record | See record | See record | No additional warrant from answer arrival | See record | See record | SRC-1 `source/engine/Session.go` | [EPI-CLM-correct-results](#epi-clm-correct-results) | bare-name bounds defect only | Qualified results have implemented advisory force; concurrent append order and successful browser delivery are not established |
| [EPI-RTE-inquire-projection](#epi-rte-inquire-projection) | content transformation | implemented | See record | truth-apt transformation: non-ampliative reshaping | See record | See record | See record | See record | See record | Reduced source prose only; degraded evidence visibility | See record | See record | SRC-1 `source/utils/chat/SummarizeMessages.go` | [EPI-CLM-summary-fidelity](#epi-clm-summary-fidelity) | omitted evidence | Reshaping does not guarantee semantic equivalence |
| [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire) | content transformation | implemented | See record | truth-apt transformation: indeterminate | See record | See record | See record | See record | See record | Model condensation is a candidate, not checked preservation | See record | See record | SRC-1 `source/tools/Agents.go` | [EPI-CLM-summary-fidelity](#epi-clm-summary-fidelity) | factuality instruction versus unchecked output | No default Inquire grant or observed summary |
| [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading) | operational admission/selection/consumption | implemented | See record | non-truth-apt policy/content update: qualified Load changes loaded state | See record | See record | See record | Generic tool notice; see record | Tool-state admission, not system-body supply | Capability compatibility is not instruction-quality warrant | Loaded object permits subsequent script selection; see record | Model receives generic notice at tool priority; loaded object feeds Execute; see record | SRC-1 `source/tools/Skills.go` | none | qualified dispatch bypasses helper | No default grants or observed activation |
| [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading) | behavior/policy adaptation | implemented | See record | non-truth-apt policy/content update: qualified Unload removes loaded state | See record | See record | Explicit qualified Unload | Generic tool notice; see record | Removes script-selection state, not injected bodies | No retrospective invalidation of earlier claims | Later Execute cannot select removed object; see record | Skills.Execute enforcing loaded-state selection; model receives tool notice; see record | SRC-1 `source/tools/Skills.go` | none | qualified dispatch bypasses helper | Prior system bodies and script/file effects are not rolled back |
| [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading) | operational admission/selection/consumption | implemented | See record | non-truth-apt policy/content update: helper/bare-name system instruction supply | See record | See record | Session.LoadSkill helper or bare-name skills/Load after tool success | Body inserted as system message; see record | Model-interpreted instruction priority | Compatibility is not instruction-quality warrant | Supplies additional guidance without expanding grant arrays | Invoking model, system-message channel, advisory instruction priority, conversation and possible recovery; see record | SRC-1 `source/engine/Session.go` | none | distinct entry point | No shipped qualified parser reaches this branch; direct helper has weaker program checking |
| [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading) | behavior/policy adaptation | implemented | See record | non-truth-apt policy/content update: helper/bare-name instruction withdrawal | See record | See record | Session.UnloadSkill helper or bare-name skills/Unload after tool success | Matching system bodies removed; see record | Enforcing context removal, not rollback | No retrospective invalidation of earlier claims | Removes matching instruction text from subsequent requests | Session message filtering, enforcing removal, subsequent conversation requests; see record | SRC-1 `source/engine/Session.go` | none | distinct entry point | Older differing bodies and prior effects remain; no observed use |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-correct-results](#epi-clm-correct-results) | See record | SRC-1 `source/agents/planner.yaml`; doctrine/design | See record | [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), [EPI-RTE-symbol-check](#epi-rte-symbol-check), [EPI-RTE-bug-closure](#epi-rte-bug-closure), [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) | None used | No comparison; test design/model compliance unknown | Testing and clarification are requested and executable; correctness is not a global admission invariant | Symbol existence, report closure and immediate writes are weaker than verified behavior |
| [EPI-CLM-summary-fidelity](#epi-clm-summary-fidelity) | See record | SRC-1 `source/agents/summarizer.yaml`; doctrine/design | See record | [EPI-RTE-inquire-projection](#epi-rte-inquire-projection), [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire) | None used | No reference-summary comparison | Factual compression is requested; incomplete evidence reaches summarizer | Omission can remove the very facts the prompt asks it to preserve |
| [RT-CLM-role-separation](runtime.md#rt-clm-role-separation) | See record | SRC-1 `source/agents/planner.yaml`; doctrine/design | See record | [RT-RTE-program-execution](runtime.md#rt-rte-program-execution), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) | None used | No isolation experiment | Method filtering and role guidance are distinct controls | See supplied forcing case; no new universal sandbox claim |

## Bounded conclusion

Exocomp can acquire project files, remote pages and caller-authored reports, and return them to model invocations. Qualified Answer calls import answers into Humans and generic Session tool messages; released qualified Ask/Choose calls also return the answer or error into that transcript. This implements model-facing supply, not observed successful delivery or epistemic acceptance. Files.Read preserves the read bytes under a header (SRC-1 `source/tools/Files.go`); website extraction can reduce or truncate content. Neither transport authenticates a proposition's truth. Source warrant remains unknown except for the narrow implementation-derived predicates described below. Model generation and condensation are implemented invocations; without concrete outputs and inputs, their semantic relation is indeterminate, not proven ampliative production.

The clearest checked derivation is structural: parseable source containing the requested symbol satisfies HasSymbol. The immediate consumer can mark a requirement implemented. Its criterion, intended use and scope are symbol-presence admission for project status, not matching the requested behavior, compiling, passing tests or producing accepted explanatory knowledge. Read-back is more consequential than a status bit: implemented entries are filtered out of the requirements file, source scanning regenerates implemented declarations with empty behavior, and those source-derived entries take precedence over saved specifications. This can remove intent from the requirements tool's next view. See [EPI-RTE-symbol-check](#epi-rte-symbol-check), [EPI-RTE-signoff-disposition](#epi-rte-signoff-disposition), [EPI-RTE-requirement-refresh](#epi-rte-requirement-refresh).

Bug closure is a different disposition: an existing report and successful I/O suffice. The fixed flag enforces omission from Bugs.List, while planner doctrine says unfixed bugs should be prioritized. Thus an unchecked closure can change the information used for work selection before any further test. The description survives in the store; closure is not a checked refutation and does not erase every read path. Changelog Remove likewise records a removal claim rather than deleting a claim or checking that source was removed. See [EPI-RTE-bug-closure](#epi-rte-bug-closure), [EPI-RTE-changelog-records](#epi-rte-changelog-records).

Testing is an important counterweight to an overly negative reading: the tester is explicitly instructed to run go test, and Programs can execute it. A valid test result could warrant behavior on its tested domain. No supplied test result, expected-answer provenance, sufficient behavioral criterion, enforced test-success write gate or evidence-consuming acceptance instance establishes that broader route here. Human plan confirmation is also requested. Humans.Answer stores an answer and releases its waiter. Shipped model, terminal and web parsers supply qualified names, so Session admits both Answer and the released Ask/Choose result through generic tool-message handling. Ask/Choose completion permits the response loop to continue inference; direct Answer does not independently start another inference. Transcript retention and later backup/restore are afforded, not guaranteed persistence success. Browser AnswerQuestion returns local validation success before asynchronous submission, and its Session.CallTool can refuse while Waiting; neither return proves delivery. Concurrent Answer and Ask/Choose appends have no unconditional ordering, and web GetLastMessage need not select the requesting call's own result. Only an embedding passing bare name humans with method Answer reaches the reverse scan at len(Messages), panicking before append/unlock and leaving the mutex locked. These entry-point distinctions preserve real qualified model-facing authority without treating answer arrival as authentication or evidence-consuming acceptance. See [EPI-RTE-human-answers](#epi-rte-human-answers). These are bounded findings, not a claim that no task can be successfully tested or accepted.

No lifecycle-integration witness after epistemic acceptance was established by the assessed routes. Retention, source regeneration, delivery and operational use before acceptance must not be renamed integration. The remaining uninspected branches prevent a system-complete negative. Role instructions and symbolic grants have real behavior-shaping paths independently of truth-apt production. Skills need separate entry-point treatment: ordinary qualified Load/Unload changes loaded objects and delivers generic tool notices, while Session.LoadSkill/UnloadSkill and bare-name skills calls afford system-body insertion/removal. Qualified Unload does not withdraw an already injected body; helper removal does not roll back prior effects. No default skill grants or observed skill use were established. See [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading). Exact weights, parameter updates inside providers, improved future capacity, exercised reflection, autonomous criticism and evidence-responsive self-improvement are not established by this inspection. External parameter opacity is not evidence that these properties are absent, and persistence or delegated work does not establish them.

## Shared records

### Operative objects

#### EPI-OBJ-specification
Label: Requirement specification

Source-native identity: Requirement.Declaration and Requirement.Behavior, keyed by File/Symbol. Representational form: symbolic Go declaration plus natural-language intended behavior, with distinct checks: DefineFunc parses/extracts the declaration but copies Behavior. Storage substrate: in-memory Requirements.contents and pending entries in `.exocomp/requirements.json`. The behavior is a requested policy, not necessarily a factual assertion; claims of implementation are separate. No object counterpart is declared in the supplied runtime; [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff) acts on this object. SRC-1 `source/tools/Requirements.go`, `source/tools/writeRequirements.go`.

> Type:        "func",
> Declaration: prettified.Body,
> Symbol:      prettified.Name,
> Behavior:    behavior,
> --- `source/tools/Requirements.go`

#### EPI-OBJ-implemented-status
Label: IsImplemented status

Source-native identity: Requirement.IsImplemented, a symbolic boolean consumed by persistence and status rendering. Storage substrate: in-memory Requirement; true entries are omitted from the persisted pending-requirements file and regenerated from source on read. This is distinct from the specification's intended behavior and from the route [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff). SRC-1 `source/tools/writeRequirements.go`, `source/tools/readImplementedRequirements.go`.

> Behavior:      "",
> IsImplemented: true,
> --- `source/tools/readImplementedRequirements.go`

#### EPI-OBJ-bug-description
Label: Bug description

Source-native identity: Bug.Description keyed by file/symbol. Representational form: natural language, potentially claiming that a named symbol behaves incorrectly. Storage substrate: Bugs.contents and `.exocomp/bugs.json`. Distinct from fixed-status selection; no supplied runtime object counterpart. SRC-1 `source/tools/Bugs.go`, `source/tools/writeBugs.go`.

> bug_report.Description = description
> bug_report.IsFixed = false
> --- `source/tools/Bugs.go`

#### EPI-OBJ-fixed-status
Label: IsFixed status

Source-native identity: Bug.IsFixed. Representational form: symbolic boolean with fixed List filtering; the label may be read as a truth-apt repair assertion by a human, but software uses it as closure authority. Storage substrate: same bug map/JSON as the separate description. No supplied runtime counterpart. SRC-1 `source/tools/Bugs.go`.

> if bug_report.IsFixed == false {
> --- `source/tools/Bugs.go:277-324`

#### EPI-OBJ-changelog-entry
Label: Changelog entry

Source-native identity: ChangelogEntry.Description and symbolic Date/Type/File/Symbol metadata. Natural-language event assertion and symbolic exact-duplicate key have distinct consumers: models/humans interpret the description; createEntry compares the full event tuple. Storage substrate: map of entry arrays and `.exocomp/changelog.json`. No supplied runtime object counterpart. SRC-1 `source/tools/Changelog.go`, `source/tools/writeChangelog.go`.

> if entry.Type == method && entry.File == internal_path && entry.Symbol == symbol && entry.Description == description {
> --- `source/tools/Changelog.go`

#### EPI-OBJ-website-content
Label: Website content

Source-native identity: Websites.Fetch returned page body with URL/status header. Representational form: natural-language webpage text or symbolic HTML/Markdown serialization, depending on format; source claims remain imported. Storage substrate: tool return string, and session messages when invoked through Session. No supplied runtime counterpart; [RT-RTE-planner-chat](runtime.md#rt-rte-planner-chat) is a downstream generic consumer rather than this object. SRC-1 `source/tools/Websites.go`.

> bytes, err4 := io.ReadAll(io.LimitReader(response.Body, 16*1024*1024))
> --- `source/tools/Websites.go`

### Routes

#### EPI-RTE-symbol-check
Label: Signoff symbol check

Part of: [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff)

Check component: caller-selected source/specification → HasSymbol → boolean. Requirements owns invocation; Go parser and AST name/type dispatch own the evaluator. Domain: parseable single-file Go AST and requested symbol/kind, not declaration equivalence or runtime behavior. The caller selects the target; program rejects missing/unparseable symbols. No human veto or expected behavioral answer is required. Operating mode: open signoff request, not a comparison experiment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean consumed by Signoff, not an independent public work report.
- Later read-back: inapplicable — this check itself retains no result; downstream disposition and refresh are separate.
- Delegated visibility: Caller-selected project source may be contractor-authored; parent can request signoff.
- Selection predicate: Existing specification and readable source; expected_type dispatch to hasFunc/hasType.
- Invalidation or expiry: Source changes can invalidate the result immediately; no ongoing check is installed.
- Activation or effect: True permits status assignment; false yields Signoff error. License is structural only.
- Evidence limits: No observed execution or warranted premise about behavioral correctness.

SRC-1 `source/utils/ast/HasSymbol.go`, `source/utils/ast/hasFunc.go`. A concrete deduction from inspected code: `package p; func F() {}` with symbol `F`, expected type `func`, reaches the top-level name comparison and returns true, regardless of a behavior requirement such as “F writes a file.” This is an implementation-layer deduction, not target execution. The structural result follows from the bytes and inspected algorithm; the behavioral requirement does not.

> } else if func_decl.Name.Name == symbol {
> return true
> }
> --- `source/utils/ast/hasFunc.go`

#### EPI-RTE-signoff-disposition
Label: Signoff status disposition

Part of: [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff)

Disposition component: true check → IsImplemented assignment → pending-record writer → notice/error. Requirements owns progression. Criterion: presence of the selected AST symbol; intended use: mark project specification implemented; scope: selected file/symbol, not behavioral satisfaction. Caller proposes, code decides, no content-specific human veto. The supplied runtime distinguishes this assignment from durable true-status persistence; refresh below explains the affected later read-back. Existing files are not rolled back.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Implemented notice or write/path/check error; see supplied parent for exact strings.
- Later read-back: True entries are excluded from JSON; subsequent source scan reconstructs status, not an archived acceptance decision.
- Delegated visibility: Planner can observe project symbol status through requirement tools, not necessarily a child test trace.
- Selection predicate: Caller-selected matching specification plus true HasSymbol and successful writer for success notice.
- Invalidation or expiry: Later source edits or requirement definitions; no versioned rollback of specification intent.
- Activation or effect: In-memory true status and omission from pending JSON; status tools can present implemented declarations.
- Evidence limits: No test or evidence-consuming semantic acceptance; criterion is weaker than full implementation.

SRC-1 `source/tools/Requirements.go`, `source/tools/writeRequirements.go`. Assignment evidence is supplied by the parent record; the load-bearing cleanup condition is:

> if specification.IsImplemented == false {
> --- `source/tools/writeRequirements.go`

#### EPI-RTE-requirement-refresh
Label: Requirement refresh

Distinct identity: the writer/read reconstruction chain spans and extends [RT-RTE-requirement-signoff](runtime.md#rt-rte-requirement-signoff); it is not merely Signoff or its check. Requirements construction and reads clear contents, scan source, then import pending JSON only where the scanned entry is absent. Source-derived entries have empty Behavior. Writer persists only unimplemented entries. Software, not a human, determines precedence and cleanup. Go syntax/symbol extraction is the admission domain; there is no behavioral oracle. A caller's intended specification guides definition but does not survive in each implemented record. DefineFunc can replace a current entry; later refresh can again prefer source. No versioned recovery of lost behavior is provided by these helpers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Helper success/error; List renders merged declarations/status, DefineFunc or Signoff returns its own notice.
- Later read-back: Constructors/List/Signoff reread source and pending JSON; implemented entries are reconstructed, not loaded as persisted true decisions.
- Delegated visibility: Shared source plus pending records can be read by planner and contractors within their path view.
- Selection predicate: Scan sandbox Go files, extract public symbols via GetPackageSymbols(false), then admit saved specs only for absent file/symbol keys.
- Invalidation or expiry: Source edits change generated status; pending-file replacement and later writes can remove saved intent. No historical acceptance chain.
- Activation or effect: Source-derived declaration/status can displace saved behavior before later models see requirements; omission from writer can make the loss durable.
- Evidence limits: AST extraction details not exhaustively audited; this warrants precedence/cleanup findings, not complete symbol coverage or correct software.

SRC-1 `source/tools/readRequirements.go`, `source/tools/readImplementedRequirements.go`, `source/tools/writeRequirements.go`, `source/utils/ast/GetPackageSymbols.go`.

> tool.contents = make(map[string]map[string]types.Requirement)
>
> if tool.Playground != "" {
> readImplementedRequirements(tool)
> }
> --- `source/tools/readRequirements.go`

> _, exists := tool.contents[file][symbol]
>
> if exists == false {
> tool.contents[file][symbol] = specification
> }
> --- `source/tools/readRequirements.go`

The supplied parent's corrected Later read-back distinguishes status reconstruction from persistence of the original specification. Its narrow AST-check finding remains separate from this reconstruction route.

#### EPI-RTE-bug-records
Label: Bug report recording

Distinct from supplied generic file admission: Bugs.Add takes a description, keys it by file/symbol, sets IsFixed false, and overwrites an existing description when the key exists. Code admits paths and serialization, not the report's evidence. Caller proposes content and may be a tester model or direct client; no intrinsic human approval, truth oracle or repair criterion. Open reporting mode. Update resets closure, and later Add can revise a report; JSON overwrite is not historical rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Written/updated notice or error.
- Later read-back: readBugs reloads `.exocomp/bugs.json`; List returns unfixed visible reports.
- Delegated visibility: Shared project reports are available to planner/coder tools within path checks.
- Selection predicate: Existing or new path/symbol key; supplied description; path and write success, not diagnosis validation.
- Invalidation or expiry: Later Add replaces description and reopens report; Fix changes closure flag.
- Activation or effect: Imported claim is retained and delivered as work-selection input; no demonstrated prioritization change.
- Evidence limits: No witnessed report or test evidence proving the alleged defect.

SRC-1 `source/tools/Bugs.go`, `source/tools/readBugs.go`, `source/tools/writeBugs.go`. Object record above supplies overwrite/reset evidence.

> resolved, err0 := resolveSandboxPath(tool.Playground, filepath.Join(".exocomp", "bugs.json"))
> --- `source/tools/writeBugs.go`

#### EPI-RTE-bug-closure
Label: Bug closure selection

No supplied counterpart; distinct from requirement signoff because it checks no source symbol or test. Bugs.Fix accepts a caller-selected existing report, assigns IsFixed and writes it. Bugs.List independently consumes that flag and filters fixed reports out. Caller proposes closure; code decides key/path/I/O admissibility; human participation is unresolved for direct calls. No answer oracle, regression criterion or evidence attachment is required. Operating mode: explicit report closure. Add can reopen; closure does not roll back product effects or delete stored description.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Fixed notice/error; later List gives only unfixed reports in the sandbox view.
- Later read-back: Flag persists with the report and is reloaded before List; closed description remains stored.
- Delegated visibility: Coder can close a report that planner later requests through Bugs.List.
- Selection predicate: Existing file/symbol plus path checks for Fix; IsFixed false plus path visibility for List.
- Invalidation or expiry: Add resets IsFixed false; actual source regressions do not automatically reopen reports here.
- Activation or effect: List suppression is enforcing software selection; planner model receives a reduced list over subsequent requests. Planner prompt gives unfixed reports advisory priority for project work.
- Evidence limits: No observed repair, regression test, behavioral activation or proof of complete erasure across all read paths.

SRC-1 `source/tools/Bugs.go`, `source/agents/planner.yaml`.

> bug_report.IsFixed = true
> tool.contents[internal_path][symbol] = bug_report
> --- `source/tools/Bugs.go`

> If there are unfixed bug reports listed in the "bugs" tool,
> those should be prioritized over the implementation of additional features.
> --- `source/agents/planner.yaml`

#### EPI-RTE-changelog-records
Label: Changelog recording

No supplied counterpart. Caller event label/path/symbol/description → createEntry → exact tuple duplicate check → dated append → JSON write. Code owns progression. Candidate is an imported account of a change; deduplication compares metadata and description, not evidence of the event. Caller may be model or direct client; no human veto or expected-answer oracle. Open project logging. Guidance requests logging file changes; what persists is the event description, not proof or rationale. Remove is another creation wrapper, not withdrawal or deletion of a prior record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/already-exists notice or error.
- Later read-back: Changelog tool exposes retained entries via List/Search; detailed selectors are uninspected in this report.
- Delegated visibility: Planner prompt requests changelog.List; shared JSON is not confined to the writer's conversation.
- Selection predicate: Path checks and exact Type/File/Symbol/Description equality for duplicate detection.
- Invalidation or expiry: No expiration or semantic contradiction handling in createEntry; subsequent Remove creates another event.
- Activation or effect: Retains caller event assertion for advisory interpretation in later work reports; no demonstrated behavior change.
- Evidence limits: No check that a reported fix/removal/change occurred; read-helper/UI details not independently established here.

SRC-1 `source/tools/Changelog.go`, `source/tools/writeChangelog.go`.

> func (tool *Changelog) Remove(path string, symbol string, description string) (string, error) {
> return tool.createEntry("Remove", path, symbol, description)
> }
> --- `source/tools/Changelog.go`

#### EPI-RTE-website-fetch
Label: Website import

No supplied counterpart. Caller URL/format → HTTP response → bounded body → requested HTML/text/Markdown → tool string → generic Session context. Websites owns request and conversion; source website supplies content. No evaluator assesses page truth. Format/URL/HTTP handling checks request suitability, not propositions. Caller chooses source; no content-specific human veto or answer oracle. Open retrieval mode. Returned URL/status provide some transport lineage; no independent source endorsement is carried.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: URL/status header plus converted body, or request/format/read error.
- Later read-back: Generic Session tool messages can be backed up and restored; no separate page repository is written by Fetch.
- Delegated visibility: Result goes to invoking agent; parent sees it only through shared reporting/transcript routes, not automatic page delivery.
- Selection predicate: Caller URL, user agent and accepted format; defaults to Markdown; 16 MiB body cap.
- Invalidation or expiry: Later fetch can see another page; existing returned snapshot is not revalidated or withdrawn.
- Activation or effect: Imported content is advisory model context; transport status does not gate factual reliance.
- Evidence limits: HTTP errors can still yield response bodies; parser internals uninspected, no extraction-completeness or page-truth guarantee.

SRC-1 `source/tools/Websites.go`, `source/tools/getWebsiteText.go`, `source/tools/getWebsiteMarkdown.go`.

> fmt.Sprintf("websites.Fetch: URL \"%s\" (%s) contents", url.String(), response.Status),
> strings.TrimSpace(content),
> --- `source/tools/Websites.go`

#### EPI-RTE-human-answers
Label: Human answer delivery

Distinct from the supplied generic [RT-RTE-client-tools](runtime.md#rt-rte-client-tools): this record covers question/answer content and its downstream admission. Ask/Choose records a question and waits; Humans.Answer matches question text, stores a supplied string and releases the waiter; Humans.Await returns the nonempty answer or an error. Model ToolCall.GetName returns a qualified name, terminal Command.Name preserves one, and the web handler forwards GetName. Session.GetTool resolves these names, but the special branch requires name == "humans". Normal qualified humans.Answer therefore reaches generic tool-message handling, as do released humans.Ask/humans.Choose returns. These messages preserve the supplied call ID/name, not the defective branch's attempted retroactive matching.

Only a bare-name embedding call with name humans and method Answer reaches that branch. After tool execution it locks the Session mutex and indexes Messages at len(Messages), unconditionally out of bounds. It panics before append/unlock, leaving the mutex locked; a released Ask/Choose may then be blocked at its generic append. This is a conditional implementation deduction, not an executed failure or a classification of shipped qualified callers.

Symbolic question/options/Multiple organize interaction; natural-language question/answer can supply facts or approval. Storage substrate: Humans.contents, waiting state and qualified Session tool messages. Browser AnswerQuestion launches qualified humans.Answer asynchronously after local nonempty validation. Its Session.CallTool refuses when Waiting, otherwise sends the qualified name to the web handler; AnswerQuestion's true return does not await that result. Human authorship is intended, not authenticated. HasMethod admits Answer without explicit Answer membership when Humans is installed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Qualified Session calls append generic formatted Answer or Ask/Choose answer/error messages and return success/error according to generic content handling. Web returns GetLastMessage on success, not a call-specific message lookup. Browser AnswerQuestion returns local validation success; its asynchronous CallTool separately returns false on Waiting or request failure, or response.OK.
- Later read-back: Humans.contents retains answers in-process. Qualified Session messages can reach later inference and planner backup/restore under the supplied recovery route; direct Answer does not itself trigger backup or inference. Successful persistence and cross-session live-question recovery are not established.
- Delegated visibility: Delivered answers are advisory context for the invoking model; a parent may use them in later contractor task prompts, but automatic propagation to other agents is not implemented here.
- Selection predicate: Exact question match; Await accepts nonempty stored text without truth or option-membership validation. Installed Humans admits Answer specially. Qualified names select generic admission; only bare-name humans selects the defective custom branch.
- Invalidation or expiry: Pending wait times out; matching answers can be replaced. Existing transcript snapshots are not automatically withdrawn. Bare-name Answer panic leaves the Session mutex locked, without deferred unlock in that branch.
- Activation or effect: Matching Answer stores text and releases a waiter; qualified Ask/Choose completion appends a result and permits ReceiveChatResponse to continue inference. Qualified Answer independently appends its generic result but does not itself start inference. Model interpretation has advisory force, not epistemic certification. Concurrent append order is not guaranteed.
- Evidence limits: No observed successful submission, continuation, acceptance or benefit. Browser Waiting may block submission; concurrent web GetLastMessage may return another call's last message. Bare-name failure is source-supported but not reached by inspected shipped qualified parsers. No authenticated respondent, reference answer or evidence-based approval is established.

Open clarification/plan-confirmation mode; caller proposes question and respondent supplies content. Code checks question existence, not epistemic fitness. Planner doctrine requests human confirmation, but file writes remain ungated by a confirmation state. SRC-1 `source/tools/Humans.go`, `source/engine/Session.go`, `source/ui/web/routes/session/CallTool.go`, `app/engine/Session.go`, `app/controllers/Chat.go`, `source/agents/planner.yaml`; compare [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), not a duplicate of it.

> result, err0 := tool.Call(method, arguments)
> --- `source/engine/Session.go`

> if name == "humans" && method == "Answer" {
> --- `source/engine/Session.go`

> session.mutex.Lock()
>
> for m := len(session.Agent.Messages); m >= 0; m-- {
>
> message := session.Agent.Messages[m]
> --- `source/engine/Session.go`

Qualified dispatch and generic admission are supported by these passages:

> return tool + "." + method, nil
> --- `source/schemas/ToolCall.go`

> command.Name = strings.TrimSpace(name)
> command.Method = strings.TrimSpace(command.Name[strings.LastIndex(command.Name, ".")+1:])
> --- `source/types/Command.go`

> Role:       "tool",
> Content:    content,
> ToolCallID: id,
> ToolName:   name,
> Created:    schemas.NewDatetime(),
> --- `source/engine/Session.go:365-377`

> return session.infer_chat_completions()
> --- `source/engine/Session.go:697-706`

> if session.Waiting == true {
> return false
> }
> --- `app/engine/Session.go:38-42`

> state.cancel()
> close(state.done)
> --- `source/tools/Humans.go`

> err6 := session.CallTool(tool_id, tool_name, tool_method, tool_arguments)
> --- `source/ui/web/routes/session/CallTool.go`

> go chat.Session.CallTool("humans.Answer", "Answer", map[string]any{
> "question": question,
> "answer":   answer,
> })
> --- `app/controllers/Chat.go`

> // NOTE: Special case, required for UI/UX integration
> if method == "Answer" {
> return true
> --- `source/tools/Humans.go`

> other.Answer = answer
> --- `source/tools/Humans.go`

#### EPI-RTE-inquire-projection
Label: Inquire transcript projection

Part of: [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire)

Deterministic part before the model: selected child messages → role filtering → printable-ASCII single-line Content → labelled text. Code owns projection, not a critic model. Tool calls/arguments and system instructions are not represented by these Content-only branches. Domain: selected transcript representation, not factual validation. The caller selects an agent; code determines what reaches the summarizer. No human approval or reference-summary oracle is used.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Text passed to the separate summarizer process, not directly accepted as final knowledge.
- Later read-back: inapplicable — this projection alone writes no replacement record; the parent route can retain a returned model summary as a tool message.
- Delegated visibility: Summarizer sees projected user/assistant prose, not the complete child execution evidence; original child transcript remains separately reachable.
- Selection predicate: Supplied Inquire call uses user=true, assistant=true, tool=false; system always ignored.
- Invalidation or expiry: Projection is a snapshot; later child messages do not update it in place.
- Activation or effect: Enforcing omission before summarizer invocation; resulting summary can later become advisory caller context.
- Evidence limits: Semantic equivalence not checked; no observed output or default Inquire grant.

SRC-1 `source/utils/chat/SummarizeMessages.go`, `source/utils/fmt/FormatSingleLine.go`, `source/utils/fmt/isPrintableASCII.go`. Concrete deterministic trace, not execution: user Content `check\nnow`, tool Content `test failed`, assistant Content `done` with flags true,true,false yields `User wrote: checknow`, a blank separator, then `Assistant wrote: done`. The newline byte fails printable-ASCII and the tool branch is disabled. The model cannot recover the omitted failure from this projection alone. This demonstrates evidence loss, not a claim that every summary hallucinates.

> content := strings.TrimSpace(utils_fmt.FormatSingleLine(message.Content))
> result = append(result, fmt.Sprintf("User wrote: %s", content))
> --- `source/utils/chat/SummarizeMessages.go`

> } else if message.Role == "tool" && tool == true {
> --- `source/utils/chat/SummarizeMessages.go`

> return chr >= 0x20 && chr <= 0x7E
> --- `source/utils/fmt/isPrintableASCII.go`

### Claims

#### EPI-CLM-correct-results
Label: Correct final result

Claimed operation: planner ensures correct, idiomatic code and passing tests; tester executes tests and reports bugs. Source is doctrine/design, not execution evidence. This is distinct from the capability/sandbox claim [RT-CLM-role-separation](runtime.md#rt-clm-role-separation), although both occur in role prompts. SRC-1 `source/agents/planner.yaml`, `source/agents/tester.yaml`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> - You ensure the final result is correct, with idiomatic code and passing unit tests
> --- `source/agents/planner.yaml`

> - ALWAYS run "go test" with the "programs" tool
> --- `source/agents/tester.yaml`

#### EPI-CLM-summary-fidelity
Label: Summary factual fidelity

Claimed operation: preserve facts/constraints/decisions and avoid adding missing information while compressing. Source is summarizer role doctrine/design, not an implemented preservation verifier. The closest supplied record [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire) is an invocation route, not this design claim. SRC-1 `source/agents/summarizer.yaml`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> - ALWAYS preserve key facts, constraints, and decisions
> --- `source/agents/summarizer.yaml`

> - You DO NOT invent missing information
> --- `source/agents/summarizer.yaml`
