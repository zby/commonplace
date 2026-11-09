---
type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
description: "Reconciliation of the runtime, memory, epistemic and workflow records of the instruction-only recall skill (recall/) of Parcha-ai/parcha-skills at c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) reconciliation

## Reconciliation

This member connects the four analyst members as handed to this job, after
their correction round. It was reconciled afresh against the current records.
No source file was read: every connection rests on the records and their
cited passages. The memory, epistemic and workflow analysts each read the
runtime member but not one another's, so their overlaps are compared here.

The current records resolve every cross-report conflict the previous
reconciliation retained:

- The runtime index route now states the declared ingest scope and splits its
  status into trigger and ingest.
- The runtime continue playbook now reads the branch command the way the
  epistemic record does.
- The epistemic search-result object is now limited to `search` rows.

Those connections are restated below from the current records, not carried
forward.

### Duplicate supersessions

Amendment: [WF-RTE-match-evidence-check](workflow.md#wf-rte-match-evidence-check) is superseded by [EPI-RTE-why-assessment](epistemic.md#epi-rte-why-assessment)

Identity evidence:

- Both declarations carry `Part of` [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read).
- Their progressions are the same steps in the same order. The model reads
  `WHY` on the top few results, treats generic-word matches as weak, and
  prefers identifier, phrase or exact-entity matches over rank 1.
- Both name the host model as owner. Both quote the same `SKILL.md` passage
  on generic words as weak evidence.
- Both have implementation status `wired` and operation status `uninspected`.
- Both state the same conditional fields: the engine proposes, the model
  decides, there is no answer oracle, and the operating mode is open requests.

The remaining differences are compatible detail, not different referents.
The workflow record says the selected path and timestamp pass to `show
--around`. It also says the user can veto only after delivery or by
redirecting. The epistemic record allows "a judgment that all hits are weak"
as a return and says the user can veto in conversation. Neither record
contradicts the other.

Affected findings:

- The workflow account's step 5 and its annotation on
  [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read) name this
  step as the workflow's acceptance step. They keep that meaning under the
  surviving ID.
- [WF-RTE-empty-result-recovery](workflow.md#wf-rte-empty-result-recovery)
  says a successful retry rejoins the superseded record.
- [EPI-RTE-repeat-confirmation](epistemic.md#epi-rte-repeat-confirmation)
  already selects its session through the surviving record.

Amendment: [WF-RTE-empty-result-recovery](workflow.md#wf-rte-empty-result-recovery) is superseded by [EPI-RTE-empty-result-report](epistemic.md#epi-rte-empty-result-report)

Identity evidence:

- Both declarations carry `Part of` [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read).
- Both cover the same branch: empty `search` output, one retry with a
  distinctive identifier or a wider window, then a report of what was
  searched and that no supported match was found.
- Both quote the retry passage from `SKILL.md` and name the host model as
  owner.
- Both have implementation status `wired` and operation status `uninspected`.
- Both state, in their evidence limits, that the cookbook's "confident
  no-answer" wording conflicts at face value with the skill's no-proof rule.

The workflow record also says a retry can return candidates that rejoin the
match check. The epistemic record's endpoints end at the report. The retry
step implies the same possibility, so the referent does not differ. The
workflow account's failure table and its annotation on
[RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read) keep their
meaning under the surviving ID.

Amendment: [MEM-CLM-empty-no-answer](memory.md#mem-clm-empty-no-answer) is superseded by [EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer)

Identity evidence:

- Both are claim records of the same claimed operation: empty scripted
  `search` stdout is a "confident no-answer", and a non-zero exit is engine
  failure.
- Both cite `recall/skills/recall/references/query-cookbook.md` at the
  `doctrine/design` layer and quote the same sentence.
- Both records, or the rows built on them, note that `SKILL.md` contradicts
  the passage at face value. Both say it holds only as "the engine ran and
  nothing cleared the gate".

The memory record's further consequence stays a memory-analyst finding under
the surviving ID: a scripted consumer reading the cookbook literally would
treat index exclusions as absence of work. That consequence also appears in
memory integration issue 5. The epistemic claim-versus-route row keeps its
mismatch entry.

Amendment: [MEM-OBJ-search-hit](memory.md#mem-obj-search-hit) is superseded by [EPI-OBJ-search-results](epistemic.md#epi-obj-search-results)

Identity evidence:

- Both declare the `search` output that the host model reads before choosing
  a session. They quote the same source-native description: "ranked sessions
  with date, cwd, slot, branch, a matched snippet, and `WHY` it matched".
- Both give the same substrate: engine stdout in the current tool result,
  not persisted.
- Both give the same consumer: the host model, judging relevance from `WHY`.
  Both note the `--paths` case, in which no `WHY` is printed.
- Both mark production as `doctrine/design`, because the engine is absent,
  and consumption as the agent-side procedure.
- The epistemic declaration states possible-duplicate evidence against the
  memory record and finds a difference of granularity only: one row versus
  the rows of one call, with no differing check, producer or consumer. The
  memory analyst compared only supplied runtime records, so it had no
  epistemic record to compare against.
- The epistemic record now covers `search` rows only. It excludes `related`
  output, which belongs to
  [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions). Its
  `Part of` [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)
  therefore names exactly one container.

The surviving record is the one with declared containment. Affected findings:

- Memory's core ideas, coverage table and working-context list, and its
  annotation on
  [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read), cite the
  memory record as the selection input. They keep that meaning under the
  surviving ID.
- The memory record's lineage field ("a readable display summary of an opaque
  ranking") and its consumer-authority remark stay memory findings. The remark
  says a hit is a selection input, not citable evidence in the remote route.
  It agrees with
  [EPI-RTE-receipt-support-check](epistemic.md#epi-rte-receipt-support-check)
  that snippets are pointers. It does not extend either record to remote
  `recall_search` output, which neither member declares as an object.

### Identities ruled out

Each pair below was compared, and its records have different referents.

- [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load) and
  [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill). Memory
  integration issue 2 raises this pair. The route has endpoints, a
  progression, an owner (the host skill loader) and status fields, with
  implementation status `afforded`. The path has a consumer, channel, force
  and horizon. They show one delivery as a route and as an authority path.
  Those are different record kinds, so both stand.
  [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission) declares
  the write and names the host's skill loader only in its later read-back
  field, so it is not the same route either.
- [MEM-OBJ-brain-synced-content](memory.md#mem-obj-brain-synced-content) and
  [RT-OBJ-brain-record](runtime.md#rt-obj-brain-record);
  [MEM-RTE-brain-ingest](memory.md#mem-rte-brain-ingest) and
  [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture). The runtime
  records cover model-selected `recall_capture` records only. The memory
  records cover sync, import, collector and connector content, which differs
  in lineage, authorship and consent basis. Memory integration issue 3 states
  this. The memory object's `Part of`
  [RT-CMP-central-brain](runtime.md#rt-cmp-central-brain) is containment
  under a component, and its declaration explains the relation.
- [MEM-ABS-skill-provenance](memory.md#mem-abs-skill-provenance) and
  [EPI-ABS-generated-skill-test](epistemic.md#epi-abs-generated-skill-test).
  Their evidence overlaps: the epistemic absence lists a missing
  source-session link among the missing items. Their supported conclusions
  differ. The memory absence concerns retaining the source session and the
  selection reasons. The epistemic absence concerns any evaluation of the
  generated skill. They are distinct absences that share one searched
  passage. The epistemic bounded conclusion cites only the epistemic absence
  for "no test, approval or source link". The memory absence also supports
  the source-link part.
- [WF-ABS-independent-answer-check](workflow.md#wf-abs-independent-answer-check)
  and [EPI-ABS-acceptance-record](epistemic.md#epi-abs-acceptance-record).
  The workflow absence is narrower: no code, second agent or user checks the
  find/verify answer before delivery. The epistemic absence covers more
  objects (answers, captures and generated skills), but asks whether a
  decision is recorded against a criterion, use and scope. Both stand.
- [EPI-RTE-engine-evidence-gate](epistemic.md#epi-rte-engine-evidence-gate)
  and [RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate). The epistemic
  record is the claimed route, with implementation status `claimed`. The
  runtime record is the claim. The epistemic declaration states this
  distinction.
  [EPI-CLM-why-explains-match](epistemic.md#epi-clm-why-explains-match)
  claims an explanation, and the gate claim claims filtering, so these two
  claims are distinct as well.
- [EPI-CLM-subagent-lineage](epistemic.md#epi-clm-subagent-lineage) and
  [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts). The
  object records the path layout and the claim records the lineage
  assertion. Memory discusses subagent transcripts in its core ideas and its
  annotation on the transcripts but declares no record for them.
- [EPI-OBJ-recall-answer](epistemic.md#epi-obj-recall-answer) and
  [RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt). The answer
  carries the receipt. It spans the local and remote read routes and
  declares no container.
- [EPI-BAP-answer-to-user](epistemic.md#epi-bap-answer-to-user) and
  [RT-BAP-retrieved-sessions](runtime.md#rt-bap-retrieved-sessions). The
  first runs from model to user. The second runs from retrieved material to
  the model. The epistemic declaration names the runtime path as upstream.

These part relations are declared and consistent with their containers, so
no supersession follows:

- [EPI-RTE-engine-evidence-gate](epistemic.md#epi-rte-engine-evidence-gate),
  [EPI-RTE-answer-receipt](epistemic.md#epi-rte-answer-receipt) and
  [EPI-RTE-empty-result-report](epistemic.md#epi-rte-empty-result-report)
  within [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)
- [EPI-RTE-cold-scan-disclosure](epistemic.md#epi-rte-cold-scan-disclosure)
  within [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)
- [EPI-RTE-receipt-support-check](epistemic.md#epi-rte-receipt-support-check)
  within [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read)
- [EPI-RTE-resume-branch-check](epistemic.md#epi-rte-resume-branch-check),
  [EPI-RTE-repeat-confirmation](epistemic.md#epi-rte-repeat-confirmation)
  and [EPI-OBJ-resume-summary](epistemic.md#epi-obj-resume-summary) within
  [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks)
- [EPI-RTE-recipe-separation](epistemic.md#epi-rte-recipe-separation)
  within [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)
- [EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget) within
  [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)
- [MEM-OBJ-export-cursor](memory.md#mem-obj-export-cursor) within
  [RT-OBJ-session-export](runtime.md#rt-obj-session-export)

Each container remains valid alongside its parts.

### Anchored conflicts

No conflict between the current reports was found. Each pair of findings
compared below either agrees or describes compatible aspects of one
mechanism. The faithful unknowns that the members leave open are listed under
integration-issue dispositions as limitations, not conflicts.

### Independent convergence

These findings were reached in more than one member from the same frozen
passages, without one member relying on another's record for them.

- **Index scope and status.**
  [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance) now gives
  trigger implementation status `wired` and ingest implementation status
  `claimed`. Its effects field and selection predicate both state the
  declared scope: Claude Code and Codex transcripts, no pi sessions or
  thinking blocks, and redaction of secret-shaped lines. Other members agree:
  - Memory's annotation on
    [RT-OBJ-session-index](runtime.md#rt-obj-session-index) and its
    integration issue 1 give the same scope.
  - The epistemic ledger gives the same scope. Its `doctrine only` status for
    the route's retention and content-transformation rows uses its own
    vocabulary for the same split: the trigger is skill text, and the ingest
    is engine behavior.
- **Continue's branch check.**
  [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks) and
  [EPI-RTE-resume-branch-check](epistemic.md#epi-rte-resume-branch-check)
  now agree that `git -C <cwd> branch --show-current` reports the branch
  currently checked out in `<cwd>`. Both say it does not establish that the
  prior session's branch exists. Both mark this as a reading of the command
  text, not an observed run.
- **CLI as central client.**
  [RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection),
  [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read) and
  [RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt) agree on three
  points with the epistemic interface-selection row and memory integration
  issue 10:
  - Under a central signal without MCP tools, the `RECALL_SCRIPT` CLI acts as
    a remote client.
  - What CLI `search` returns there is not stated, and `shadow` has no stated
    meaning.
  - Single-store answer provenance is the instruction's intent for the MCP
    path only.
- **Empty results.** Runtime guarantee G5,
  [EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer)
  with its superseded duplicate, and the workflow failure table each find
  the same face-value inconsistency between `SKILL.md` and
  `recall/skills/recall/references/query-cookbook.md`. Each reconciles it only
  as "the engine found nothing above its gate". The members differ in
  emphasis, not in finding:
  - Memory and epistemic retain the conflict between the shipped files.
  - The workflow account says the `SKILL.md` wording governs the user-facing
    report, because the cookbook line describes `--paths` scripting output.

  The workflow account does not deny the conflict, and the others do not deny
  the scripting scope. The inconsistency is the source's own, and every
  member retains it.
- **No answer verification in local mode.** These records agree that nothing
  checks the local find/verify answer against the shown window before
  delivery, beyond the answering model's own reading:
  - [WF-ABS-independent-answer-check](workflow.md#wf-abs-independent-answer-check)
  - the epistemic row for
    [EPI-RTE-answer-receipt](epistemic.md#epi-rte-answer-receipt), with its
    mismatch marker against remote mode
  - [EPI-ABS-acceptance-record](epistemic.md#epi-abs-acceptance-record)

  The workflow and epistemic members also agree that remote mode adds a
  model-enforced citation rule
  ([EPI-RTE-receipt-support-check](epistemic.md#epi-rte-receipt-support-check)).
- **Cold scan bypasses the index filter.** Three members agree that raw
  `rg` reads are not subject to the declared redaction and thinking-block
  exclusions:
  - runtime guarantee G2 and
    [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)
  - memory integration issue 8 and its annotation on
    [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)
  - the epistemic mismatch marker on the
    [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance)
    content-transformation row

  All three leave thinking-text presence as a host fact.
- **Write admission without approval of content.** Runtime, memory and
  epistemic agree on the two model-authored writes,
  [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture) and
  [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission). A user
  request starts each one, and the model authors the content. No step
  requires the user to approve the selected or generated text. Each member
  states this in its own place:
  - runtime, in the admission fields;
  - memory, in its annotations;
  - epistemic, in
    [EPI-ABS-acceptance-record](epistemic.md#epi-abs-acceptance-record) and
    [EPI-ABS-generated-skill-test](epistemic.md#epi-abs-generated-skill-test).
- **Single-agent operation.** The runtime account's coordination statement
  and [WF-ABS-agent-delegation](workflow.md#wf-abs-agent-delegation) agree
  that the skill delegates to no agent. Memory treats host subagent
  transcripts as indexed sessions. That concerns retained material, not
  delegation by the skill, so it does not conflict.
- **Read-back direction, scoped by route.** Memory and runtime agree only
  within two separate scopes, and no member supports a system-wide pull-only
  value:
  - *Routes that read session material.* Memory's
    [MEM-ABS-push-hook](memory.md#mem-abs-push-hook) concludes that every
    route reading retained session material is pull, issued by the
    foreground model or, for export, by a consuming skill's code. The runtime
    routes that read that material name the host model as owner of the
    request:
    - [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)
    - [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)
    - [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions)
    - [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read)
    - [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks)

    [RT-RTE-session-export](runtime.md#rt-rte-session-export) is driven by
    the consuming skill's code or agent.
  - *Generated-skill read-back.* Memory's
    [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load)
    gives the host skill loader as owner and the direction as host-dependent
    and uninspected. Memory integration issue 9 states that a system-wide
    pull-only value is unsupported. The runtime records agree that the host
    loader, not a model request, governs this delivery.
    [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission) names
    "the host's skill loader" as the later read-back consumer.
    [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill) names the
    host skill loader and the later model as consumers. Neither runtime
    record says the model issues the request.

  The synthesis may state pull for session-material routes only. For
  generated skills it must leave direction host-dependent.
- **Retrieved content lacks trust marking.** Memory's core ideas find no
  trust distinction by origin. Two epistemic absences converge with this:
  [EPI-ABS-self-report-distinction](epistemic.md#epi-abs-self-report-distinction)
  finds no assistant-versus-tool distinction, and
  [EPI-ABS-data-instruction-rule](epistemic.md#epi-abs-data-instruction-rule)
  finds no limit on retrieved text's instructional force. These are
  compatible findings about different dimensions, not one record.

### Complementary findings without conflict

- **Export completeness.** Runtime guarantee G6 lists the page checks `recap`
  enforces. The epistemic row on
  [RT-RTE-session-export](runtime.md#rt-rte-session-export) adds a gap in
  that consumer: a run whose pages never carry `source_snapshot_stable`
  yields `source_complete` true. The runtime member does not claim that
  `recap` checks that field, so the epistemic finding extends it rather than
  contradicting it. Both attribute the consumer logic to `recap`, outside
  the functional boundary. Runtime's split statuses (producer `claimed`,
  consumer `wired`) and the epistemic `doctrine only` status for the
  producer check describe the same split in two vocabularies.
- **Index lifetime and forget reach.** Memory integration issues 6 and 7 are
  faithful unknowns, not disagreements. Issue 6 asks whether index entries
  survive deletion of their source transcripts. Issue 7 asks whether
  `recall_forget` reaches synced copies or local material. The epistemic row
  on [EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget) reaches a
  compatible limit: derived uses and local transcript copies are untouched,
  as declared.
- **Generated skills as behavior change.** Memory's annotation on
  [RT-OBJ-generated-skill](runtime.md#rt-obj-generated-skill) and its route
  [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load)
  describe trace-fed, user-triggered instructions with no retained reasons.
  The epistemic bounded conclusion calls this direct behavior adaptation
  without an evaluated truth-apt route. It leaves self-improvement link 1
  unestablished, and links 3 and 4 dependent on the host loader. The memory
  member makes no self-improvement attribution that this finding would
  contradict. Memory's `afforded` status for the read-back leg agrees with the
  epistemic dependence on the external loader.

### Integration-issue dispositions

The memory member lists ten integration issues. The runtime, epistemic and
workflow members have no integration-issue section. Their in-record identity
comparisons were checked above.

1. Absorbed correction to
   [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance): the
   runtime record now states the declared scope. Disposed as convergence. No
   conflict remains.
2. Possible overlap of
   [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load)
   with [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill): identity
   ruled out, because the route and the path are different kinds. Both stand.
3. Distinct identity of the Brain sync and ingest records: confirmed and
   ruled out above.
4. Part relation of [MEM-OBJ-export-cursor](memory.md#mem-obj-export-cursor):
   consistent with its container. No supersession.
5. Conflicting shipped wording on empty results: the duplicate claim record
   is superseded by
   [EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer).
   Every member retains the source's inconsistency. No conflict between
   reports.
6. Index lifetime after host retention deletion: an unknown that every member
   leaves open. It is a limitation of the synthesis, not a conflict.
7. Reach of `recall_forget`: an unknown, compatible with the epistemic
   withdrawal row. It is a limitation, not a conflict.
8. Thinking-block gotcha scoped to indexed search: converges with runtime G2
   and the epistemic mismatch marker. No conflict.
9. Scoped read-back direction: consistent with the runtime records on
   generated-skill delivery. Disposed under the scoped read-back convergence
   above. No member supports a system-wide pull-only value.
10. CLI as central client: consistent with the corrected runtime records and
    the epistemic interface-selection row. Disposed as convergence. Which
    store answers CLI `search` under a central or `shadow` signal remains an
    unknown, and it is a limitation of the synthesis.

### Limits of this reconciliation

This member compared declarations, annotations, ledger rows and integration
issues across the four analyst members. It did not re-read the frozen source,
so it judged no record's support. The verifier owns that judgment. The
supersessions leave the superseded records declared and their members'
findings valid under the surviving IDs. No unresolved conflict between
reports remains. The unknowns named in dispositions 6, 7 and 10, and every
engine and Brain claim, remain limitations of the synthesis.
