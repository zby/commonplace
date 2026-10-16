---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Sentry Skills retained guidance, revision evidence and document handoffs, with host-owned context limits."
run-id: AAS-2026-10-14-skills-2719567f917c-01
source-identity: https://github.com/getsentry/skills
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
---

# Sentry Skills memory report

## Boundary and evidence

The subject is the complete Sentry Skills package at the pin in [boundary](boundary.md), not its enclosing hosts. Memory scope includes guidance written for future agents, evidence retained for later skill revisions, maintainer evaluation results and explicit document-to-later-task handoffs. It also includes current-window selection and isolated reader testing without treating all tool output as durable memory. Static shipped instructions are context inputs; only changed or accumulated material reaching a later invocation qualifies as read-back.

Direct source inspection added agents-md, skill-writer's evidence, synthesis, adaptation, architecture, authoring, SPEC and SOURCES material, both SRED workflows, doc-coauthoring, dynamic-context/fork guidance and reply-to-thread implementation. The table distinguishes these reads from supplied runtime findings. All are SRC-1, implementation or doctrine/design as specified below. No target was executed. External stores, host context assembly, model weights, AXIS result payloads and linked example documents are not captured; their contents and operation remain uninspected.

| Entry or operation | Source paths and evidence | Coverage or prevented conclusion |
|---|---|---|
| Skill invocation, installation and updated guidance loading | SRC-1, `README.md`, `.claude-plugin/plugin.json`; supplied runtime | [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption), [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md); host selection/activation not observed |
| Skill synthesis, replacement and example-fed revision | SRC-1, `skills/skill-writer/SKILL.md`, `skills/skill-writer/references/synthesis-path.md`, `skills/skill-writer/references/source-adaptation.md`, `skills/skill-writer/references/authoring-path.md`, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/references/iteration-path.md`; direct doctrine reads | [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), new evidence objects below; no exercised update trace |
| Maintenance provenance and scope contract | SRC-1, `skills/skill-writer/SOURCES.md`, `skills/skill-writer/SPEC.md`, `skills/skill-writer/references/reference-architecture.md`; direct doctrine reads | [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-spec](#mem-obj-spec); upstream trust labels are attributed, not authenticated |
| Evaluation, rejection and baseline reuse | SRC-1, `skills/skill-writer/EVAL.md`; direct doctrine; configuration/scenario implementation supplied by runtime | [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval); reports/baselines not supplied |
| Project instruction editing | SRC-1, `skills/agents-md/SKILL.md`; direct doctrine | [MEM-OBJ-agents-md](#mem-obj-agents-md), [MEM-RTE-project-guidance](#mem-rte-project-guidance); loading implementation external |
| Work Summary storage and later SRED selection | SRC-1, `skills/sred-work-summary/SKILL.md`, `skills/sred-project-organizer/SKILL.md`; direct doctrine | [MEM-OBJ-work-summary](#mem-obj-work-summary), [MEM-RTE-sred-handoff](#mem-rte-sred-handoff); classification reference/template contents not inspected, preventing independent assessment of their adequacy |
| Document editing and isolated reader checks | SRC-1, `skills/doc-coauthoring/SKILL.md`; direct doctrine | [MEM-OBJ-document-draft](#mem-obj-document-draft), [MEM-RTE-reader-testing](#mem-rte-reader-testing); host isolation not implemented here |
| PR feedback/log selection and monitor | SRC-1, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/fetch_pr_feedback.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py`; supplied implementation findings | [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration), [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor); bounded summaries/current-run outputs, not proved cross-session guidance |
| PR reply mutation | SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py`; direct implementation | [MEM-RTE-thread-reply](#mem-rte-thread-reply); stored reply is remote collaboration content, not established guidance read-back |
| Issue cleanup/status filtering | SRC-1, `skills/triage-frontend-issues/SKILL.md`; supplied runtime | [RT-RTE-issue-triage](runtime.md#rt-rte-issue-triage); service persistence/approval compliance unobserved |
| Other registered skill/helper entry points and hooks | SRC-1, `skills/`, `agents/`, `.claude/settings.json`, `warden.toml`; bounded direct search of all skill/agent entries and seven Python scripts for persistence, dispatch, hooks and context fields; supplied registration findings | Scanner and review-request helper output bodies not fully traced; no exhaustive negative about their state effects. Other domain leaf references and senpai body uninspected; complete repository-wide memory enumeration is not claimed |
| Optional fork and preprocessing design | SRC-1, `skills/skill-writer/references/claude-subagent-fork.md`, `skills/skill-writer/references/claude-dynamic-context.md`; direct doctrine | Authoring options, not evidence of activated fork/preprocessing in skill-writer; host eviction/reload behavior unknown |

## Core ideas

The package's strongest retained behavioral surface is editable instruction text, not an implemented memory service. [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision) can change the text later hosts consume. Its evidence path separates semi-raw examples from interpreted findings and promoted rules. A revision agent reads evidence; a later task agent normally reads the resulting guidance. These are different consumers and authority paths.

Source trust and reasons chiefly live outside runtime guidance. Synthesis records trust tier, confidence, contribution and usage constraints in SOURCES; adaptation records omissions and fidelity tradeoffs. The authoring pass moves provenance and maintenance rationale out of runtime. This limits token cost but means ordinary task consumers are not promised the reasons for every promoted rule. SRC-1, `skills/skill-writer/references/synthesis-path.md`, `skills/skill-writer/references/source-adaptation.md`, `skills/skill-writer/references/authoring-path.md`.

> Move provenance, rationale, or maintenance-only notes out of runtime files.
> --- `skills/skill-writer/references/authoring-path.md`

The SRED pair supplies a counterexample to treating all retained content as instruction learning: a generated project index is explicitly consumed by a later workflow as evidence. Reader testing supplies a different context mechanism: withhold author conversation, pass document plus question, return findings. Neither entails changing model parameters or a host compaction mechanism.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-working-set
Label: Working and holdout example sets

Git/filesystem Markdown under `references/evidence/working-set.md` and `references/evidence/holdout-set.md` is prescribed storage, not an inspected populated set. Natural-language redacted examples carry symbolic-looking labels interpreted by authors: origin human-verified/mixed/synthetic, provenance pointer, expected and observed behavior, delta, anonymization and status. They are semi-raw evidence, not the derived instruction. Future revision/replay agents consume them; source labels do not authenticate trace origin. Holdout movement requires explicit user choice. Distinct supporting objects for [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), not another declaration of that route or of SKILL.md. SRC-1, `skills/skill-writer/references/iteration-evidence.md`.

> `references/evidence/holdout-set.md` stores examples reserved for validation after edits. Do not tune directly against holdout examples unless the user explicitly moves them into the working set.
> --- `skills/skill-writer/references/iteration-evidence.md`

#### MEM-OBJ-findings-log
Label: Interpreted iteration findings

Natural-language Markdown prescribed at `references/evidence/findings-log.md` retains patterns, suspected causes, responsive instruction changes and unresolved risks. It is a derived account rather than the example payload. A later revision agent can read it through synthesis intake; no inspected populated findings file establishes an actual claim/blame/revision chain. Distinct from [MEM-OBJ-working-set](#mem-obj-working-set) and the route [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). SRC-1, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/references/synthesis-path.md`.

> Each negative finding should map to a concrete skill delta or an explicit deferred reason.
> --- `skills/skill-writer/references/iteration-evidence.md`

#### MEM-OBJ-sources
Label: SOURCES provenance and decisions

Source-native `skills/skill-writer/SOURCES.md` is an inspected Git-backed natural-language inventory, decisions, gaps, coverage table and dated changelog. It attributes upstream contributions and rejected alternatives, but its cited upstream sources are not independent frozen evidence. It exemplifies the prescribed destination for later source inventories, one-off example summaries and revision deltas. Consumers are future synthesis/maintenance agents, not automatically every skill invocation. It is distinct supporting material for [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), not the runtime instruction body [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md). SRC-1, `skills/skill-writer/SOURCES.md`, `skills/skill-writer/references/synthesis-path.md`.

> Store provenance in `SOURCES.md`, not long runtime prose.
> --- `skills/skill-writer/references/synthesis-path.md`

#### MEM-OBJ-spec
Label: SPEC maintenance contract

Source-native `skills/skill-writer/SPEC.md` is an inspected Git-backed natural-language contract for scope, evidence policy, outputs, validation and limitations. The router requires updating SPEC for new/materially changed contracts; maintenance agents interpret it. It is not a machine-enforced schema and not promised as ordinary task-agent input. It is distinct from [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md) and supports [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). SRC-1, `skills/skill-writer/SPEC.md`, `skills/skill-writer/references/reference-architecture.md`.

> `SPEC.md` is the maintenance contract.
> --- `skills/skill-writer/references/reference-architecture.md`

#### MEM-OBJ-agents-md
Label: Generated project instruction files

Natural-language Markdown on a consuming repository's filesystem/Git is generated from inspected commands, docs and code conventions. Root AGENTS.md supplies defaults; nested files are intended to narrow scope; CLAUDE.md is an optional symlink alias, not another payload. Later host agents interpret these instructions; no generated instance or actual host precedence is observed. Distinct output of [MEM-RTE-project-guidance](#mem-rte-project-guidance), not the package's SKILL.md object [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md). SRC-1, `skills/agents-md/SKILL.md`.

> - Do not maintain divergent `AGENTS.md` and `CLAUDE.md` copies.
> --- `skills/agents-md/SKILL.md`

#### MEM-OBJ-work-summary
Label: SRED Work Summary and project documents

Work Summary is a prescribed private Notion document: natural-language project headings with link/date/count access metadata, not copies of every underlying payload. It derives grouping from PR title/description, full Notion documents and ticket title/description. A later organizer reads it and linked source material. Organizer output is a separate derived project-document family with descriptions, uncertainties, experiments/results and source links; no subsequent agent route for that output is established. These are external work products, not package guidance. No counterpart in the supplied [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision); the consumer chain is [MEM-RTE-sred-handoff](#mem-rte-sred-handoff). SRC-1, `skills/sred-work-summary/SKILL.md`, `skills/sred-project-organizer/SKILL.md`.

> Prompt the user for a link a Notion document, which is a Work Summary for the previous year produced by the `sred-work-summary` skill.
> --- `skills/sred-project-organizer/SKILL.md`

#### MEM-OBJ-document-draft
Label: Coauthored document draft

Natural-language draft persists as a host artifact or working-directory Markdown file; source material includes human context, fetched shared documents and iterative human/model selections. The later reader receives the document, not necessarily its author conversation. User preferences retained mentally in the active conversation are current-run state, not a specified cross-session preference store. Distinct from [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md); no supplied route accounts for this output. SRC-1, `skills/doc-coauthoring/SKILL.md`.

> Create a markdown file in the working directory. Name it appropriately (e.g., `decision-doc.md`, `technical-spec.md`).
> --- `skills/doc-coauthoring/SKILL.md`

### Routes

#### MEM-RTE-project-guidance
Label: Project guidance authoring and later loading

User task → foreground inspection of repository facts → concise root/nested guidance → verify exact paths/commands → later host instruction loading. Model authors and selects non-obvious rules; user initiates the task but no per-rule approval is required. Host tool controls and repository review are external. Open authoring mode; inspected command existence is a reference check, not an oracle for overall instruction quality. Guidance requests reference-backed minimal content and omitting rationale unless it prevents mistakes. No automatic rollback/admission transaction specified. Distinct from package skill revision [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision): writes consuming-project guidance rather than reusable skill files. SRC-1, `skills/agents-md/SKILL.md`.

- Immediate return: generated or revised instruction file; exact final response format unspecified.
- Later read-back: afforded host consumption of changed AGENTS.md or its alias in future project work; host loading is external.
- Delegated visibility: inapplicable — no worker delegation required in this workflow.
- Selection predicate: repository scope and non-obvious commands/conventions; nested files only for different subtree rules.
- Invalidation or expiry: edit guidance as repository conventions change; alias avoids divergent copies; no automatic expiry.
- Activation or effect: requested future agent policy changes, not observed compliance.
- Evidence limits: prompt doctrine only; no generated artifact, host precedence implementation or run supplied.
- instruction conclusion status: claimed
- read-back conclusion status: afforded
- operation conclusion status: uninspected

> - closest instruction file wins; keep narrower files shorter than root files
> --- `skills/agents-md/SKILL.md`

#### MEM-RTE-sred-handoff
Label: SRED evidence collection and document handoff

User supplies identity/repos/incident choice → foreground searches dated service records → creates private Work Summary and groups links → user later supplies summary link to organizer → model classifies projects → human adjusts classification → model creates project descriptions/uncertainties/results with repeated human review. User controls query scope and classification; model performs grouping and drafting; services own physical persistence. No frozen service implementation supplies admission enforcement. Mode is open evidence-based reporting; SRED reference criteria guide classification rather than providing known answers. Existing Work Summary name requires stop/rename, not overwrite. Project review enables correction; automatic rollback/deletion is unspecified. No counterpart among supplied runtime routes. SRC-1, `skills/sred-work-summary/SKILL.md`, `skills/sred-project-organizer/SKILL.md`.

- Immediate return: Work Summary link, then organizer's parent/child document links.
- Later read-back: organizer explicitly requests the prior generated summary and inspects its related sources; no later model consumer of final submission docs specified.
- Delegated visibility: inapplicable — no model delegation specified; MCP/gh are retrieval and persistence channels.
- Selection predicate: named user/repos and February-to-January window, incident exclusion and other-user relevance; then projects satisfying SRED criteria with human correction.
- Invalidation or expiry: duplicate summary name stops workflow; user reviews and requests changes; no retention TTL or automatic withdrawal.
- Activation or effect: summary grouping informs subsequent project selection/drafting; not package self-modification or demonstrated improved capacity.
- Evidence limits: prescribed full link lists do not prove exhaustive service retrieval; source reference/template adequacy and actual payloads uninspected.
- instruction conclusion status: claimed
- read-back conclusion status: afforded
- operation conclusion status: uninspected

> If a document with this name already exists, notify the user to rename the existing document and stop executing.
> --- `skills/sred-work-summary/SKILL.md`

> Ask the user whether the list of SREDable projects is correct. Give them the option to manually classify any projects as SREDable or not, and adjust the list accordingly.
> --- `skills/sred-project-organizer/SKILL.md`

#### MEM-RTE-reader-testing
Label: Isolated reader testing and draft repair

Author/user collaboration produces draft → foreground predicts reader questions → fresh subagent receives document/question without author conversation → findings summarized → problematic sections revised. Without workers, user opens fresh conversation and relays results. Foreground proposes revisions; user curates content and may decline the structured workflow, alter stages or finalize. Correctness is checked by author/user interpretation of answers, not a supplied exact-answer oracle. Open collaborative drafting with repeated reader checks. File/artifact edits persist; no automatic rollback or cross-session preference adoption specified. Distinct from code-refinement [RT-RTE-code-refinement](runtime.md#rt-rte-code-refinement): document clarity and reader-context testing, not code preservation. SRC-1, `skills/doc-coauthoring/SKILL.md`.

- Immediate return: reader right/wrong summary, issue list, revised draft and document link/file confirmation.
- Later read-back: fresh reader invocation consumes the saved draft; later external readers are intended, but delivery/deployment not observed.
- Delegated visibility: document content and question only, withholding author conversation; manual fresh-chat alternative passes document/link and questions.
- Selection predicate: 5–10 predicted reader questions plus ambiguity/assumption/contradiction checks; no token budget specified.
- Invalidation or expiry: problematic sections return to refinement; exit when answers are consistently correct with no new gaps; no host frame removal semantics specified.
- Activation or effect: findings are prescribed to change draft content, not stable package rules; repairs and benefits unobserved.
- Evidence limits: isolated-context policy and return summary are prompts; actual host isolation and reader correctness are unobserved.
- instruction conclusion status: claimed
- read-back conclusion status: afforded
- operation conclusion status: uninspected

> For each question, invoke a sub-agent with just the document content and the question.
> --- `skills/doc-coauthoring/SKILL.md`

#### MEM-RTE-thread-reply
Label: PR thread reply persistence

CLI thread/body pairs → symbolic Python newline normalization/JSON escaping → batched GraphQL addPullRequestReviewThreadReply mutations → per-alias failure parsing → JSON status/exit code. Caller supplies content; helper does not judge its truth or require human approval. GitHub admission/access and later display are external. Open caller-requested mutation, not candidate comparison or a learning loop. No deletion/rollback implemented in this helper. Material part of the PR workflow: a mutation route, not a replacement for [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration). SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py`.

Part of: [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration)

- Immediate return: per-operation and per-thread JSON success/failure summary; nonzero exit for failures.
- Later read-back: uninspected — external service can retain comments, but no later caller of those written replies is established by this helper.
- Delegated visibility: thread IDs and caller-authored bodies reach gh/GitHub; no model worker.
- Selection predicate: caller-provided thread IDs; no semantic relevance selection.
- Invalidation or expiry: inapplicable — helper specifies neither expiry nor withdrawal of remote replies.
- Activation or effect: implemented request to append remote thread comments, not guaranteed successful mutation or future guidance.
- Evidence limits: no service trace; per-alias response checks support reported mutation status, not content correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Batches all replies into a single GraphQL mutation for efficiency.
> --- `skills/iterate-pr/scripts/reply_to_thread.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md)

Memory-specific lineage: promoted rules can derive from source synthesis, evidence replay and precision passes. Runtime text is separated from provenance and semi-raw examples. Future task consumers receive model-interpreted behavioral rules; maintenance consumers receive supporting evidence. A static copy is context, while updated guidance loaded later supports read-back. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/references/source-adaptation.md`.

> - Put universal behavioral rules in `SKILL.md`.
> - Put domain-specific examples in a focused reference.
> - Put source provenance and decisions in `SOURCES.md`.
> - Keep raw or semi-raw examples in `references/evidence/`.
> --- `skills/skill-writer/references/iteration-evidence.md`

#### On [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision)

Write/read-back chain: human-verified, mixed or synthetic inputs → redacted working/holdout examples → interpreted findings and deltas → promoted runtime instructions/examples plus SOURCES/SPEC updates → later maintenance agents or installed skill consumers. This is a prescribed trace-fed transformation, not an automatic trace ingester or an observed learning result. Model authors decide promotion using the stated behavior-change criterion; user controls explicit holdout-to-working reassignment. Starting the task is not per-change human admission. Initial truth of evidence and claimed origin remains unverified. Synthesis explicitly includes prior SPEC, SOURCES and evidence, establishing a future maintenance read path for reasons; ordinary task invocation is not instructed to reload all reasons. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/references/iteration-path.md`, `skills/skill-writer/references/synthesis-path.md`.

> Promote evidence into the skill artifacts only when it changes future behavior:
> --- `skills/skill-writer/references/iteration-evidence.md`

Context selection: current-step foreground decisions choose leaf files using need tables. Material remains reachable on filesystem; there is no inspected automatic removal of already loaded text or measured context cap. Fork design calls for a task, summary contract, isolation reason and portability note; it does not specify host frame-pop mechanics. Shell preprocessing guidance favors cheap, high-signal output and forbids large/noisy injection; it is an authoring option, not implemented compaction or a shipped persistent store. SRC-1, `skills/skill-writer/SKILL.md`, `skills/skill-writer/references/claude-subagent-fork.md`, `skills/skill-writer/references/claude-dynamic-context.md`.

> Never inject large or noisy output.
> --- `skills/skill-writer/references/claude-dynamic-context.md`

#### On [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval)

Reports are declared to include transcripts, artifacts, scores and raw output; the result template adds baseline/candidate, decision, fixes and evidence pointers. External AXIS owns storage; payload encoding/path and populated results are uninspected. Raw transcripts and selected artifacts are evidence, scores/summary are derived assessments, and a baseline is comparison state rather than runtime instruction. Maintainer reviews reports before resetting baseline and decides adopt/revise/reject; no automatic installed-text replacement follows a score. Failure/slow transcripts can inform instruction revisions. SRC-1, `skills/skill-writer/EVAL.md`; supplied record supports configuration and adoption policy.

> Review transcripts when a run fails or is slow; wasted steps usually point to bloated or ambiguous skill instructions.
> --- `skills/skill-writer/EVAL.md`

#### On [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration)

The supplied record's bounded log snippets, thread/comment limits, short summaries and full first-comment bodies are current-invocation selection, not a complete retained trace store. Git commits and remote replies are durable work/collaboration artifacts. The new reply route does not establish that the feedback fetcher later delivers those specific replies; its first-comment projection cautions against equating thread persistence with model receipt. No evidence-fed permanent guidance write follows a successful repair in the inspected route. SRC-1, `skills/iterate-pr/scripts/fetch_pr_feedback.py`, `skills/iterate-pr/scripts/reply_to_thread.py`; supplied record retains the fetcher evidence limits.

## Write side

The main instruction-changing write is [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), with the example/interpretation/provenance distinction above. Privacy redaction, evidence promotion, pre/post precision and structural validation govern different aspects: redaction controls retained content, promotion decides what belongs in future guidance, precision narrows/replaces/deletes redundant rules, validator checks format/reference existence. Authorship and filesystem I/O are not independent admission proof. Reasons persist in findings/SOURCES and are explicitly collected by later synthesis; runtime rules need not contain them. A one-off fix may keep example summaries in SOURCES rather than create durable evidence folders. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/references/authoring-path.md`.

Evaluation's adopt/revise/reject and baseline-refresh policy are in [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval); actual rejected outputs or retained scores are not supplied. No deployed rollback or installed-copy withdrawal follows from structural rejection. [MEM-RTE-project-guidance](#mem-rte-project-guidance) writes project policy without a specified per-rule human gate. [MEM-RTE-sred-handoff](#mem-rte-sred-handoff) has human classification/review and duplicate-name stop. [MEM-RTE-reader-testing](#mem-rte-reader-testing) has human content curation and model-directed gap repair. Their outputs must not be conflated with self-revision of this package.

Triage cleanup writes issue status and a reason under displayed-batch approval; a wrong archive has no automatic reversal in [RT-RTE-issue-triage](runtime.md#rt-rte-issue-triage). This can remove records from a later unresolved-queue query without deleting the underlying issue or changing skill knowledge. [MEM-RTE-thread-reply](#mem-rte-thread-reply) appends caller content and reports partial failures; it performs no semantic evidence curation.

## Read-back

There are three supported retained-content consumer patterns: changed guidance loaded by a later external host, examples/reasons read by later maintenance, and a generated document read by a distinct reader/organizer invocation. Installation/read-back operation is unobserved. None proves behavioral activation or benefit. Static skill installation by itself is excluded from read-back until use changes retained content.

The foreground agent pulls relevant skill-writer references using task and step as selector inputs; no numerical token budget or automatic context eviction is specified. The practical budget policy is minimal required leaf loads, not an implemented token allocator. Reader testing withholds conversation and returns issue summaries; the stack-frame analogy fits intended input/return separation but cannot establish actual frame destruction. The manual fresh-chat path is a material alternative: a human transfers draft and questions and relays results. SRED pulls a user-identified summary rather than an unsolicited automatic push. Its complete-link requirement does not establish service retrieval completeness, and links are access metadata rather than the full original documents. Relevant source payloads are separately fetched during grouping and project analysis. SRC-1, `skills/skill-writer/SKILL.md`, `skills/doc-coauthoring/SKILL.md`, `skills/sred-work-summary/SKILL.md`, `skills/sred-project-organizer/SKILL.md`; records above retain supporting passages.

## Integration issues

- No supplied fact requires correction. The supplied runtime's broad maintenance route remains valid; this member adds explicit evidence parts, consumer distinctions and untraced document workflows.
- [MEM-RTE-thread-reply](#mem-rte-thread-reply) is a declared material part of [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration), not a duplicate. Remote persistence does not imply feedback projection includes the replies.
- No new declaration is proposed as a replacement for a supplied referent. Evidence/SOURCES/SPEC support the supplied revision route but are not its SKILL.md container. Project guidance and document routes have different outputs and consumers from the supplied code/package revision routes.
- Actual example origins, populated findings, executed promotion/adoption and installed update consumption are unknown. This prevents attributing exercised trace learning or closing the runtime's self-improvement chain; it does not negate the prescribed mechanism. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/EVAL.md`; [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision).
- AXIS report/baseline storage and payloads, host context push/pop/compaction, service completeness and actual remote content remain outside inspected evidence. Available but unread domain leaf references/scanner helper bodies/other scenarios prevent exhaustive memory-route and evaluator coverage. These limits stay local to the affected table rows and routes rather than becoming an unsupported system-wide absence.

## Limitations and checks

Source HEAD was rechecked as d18b7aa8ba878354e5c348310230e652f7690f9c; source status was clean. This account uses the supplied memory type, worker rules and records contract without changing their method or engine state. Direct searches checked shipped CLI dispatch and mutation/persistence terms against runtime routes; findings are source-text capacities and doctrine, not executed target behavior. Counterexamples checked include one-off evidence in SOURCES, optional rather than activated forks, manual reader testing, duplicate summary stop, and remote replies without proven later projection. No target execution, services, installations, prior analyses or agent launches were used.

Validation: the invocation's validate-output command passed: “Member content check passes; invocation residue not checked.” This is not job acceptance or claim support. Form and quote occurrence do not prove causal support.
