---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Memex's runtime, memory, epistemic, workflow and reconciliation at the frozen commit."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
---

# Memex report verification

## Verification

The supplied reports support a bounded source-level account. The previous withdrawal blocker is repaired. I read the complete boundary, five reports, correction answers, previous verification and governing contracts. The structural report-check is `none`, so there is no structural failure to route. I judged the records afresh and independently traced the consequential source behavior; neither the earlier verdict nor the analysts' validation statements substitutes for that inspection. Git HEAD matches the reviewed revision and status is clean. The tracked tree and shipped entry points support the [boundary](boundary.md#boundary-and-evidence): producers, maintenance, later consumers and administration are included. No target code, tests, examples or services were executed.

### Runtime and workflow dispositions

All runtime declarations and source anchors were checked. [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model) correctly distinguishes selected aliases from pinned weights and inaccessible parameter updates. [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs) and [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts) distinguish durable scheduler/results from static task policy. Direct inspection of SRC-1, `src/daemon/runner.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon.ts`, `src/cli/client.ts`, `src/lib/constants.ts` and the ingest/query/lint commands supports all five runtime routes and their separately uninspected operation statuses.

[RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) admits bytes before queued work and permits direct model file effects. [RT-RTE-query-job](runtime.md#rt-rte-query-job) requests index/search/page reads, accepts caller-supplied history without recovering prior results, and retains Write/Edit access. [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) schedules from exit-success counts, not verified integrations; its confident-fix/report-only split is prompt policy. [RT-RTE-config-change](runtime.md#rt-rte-config-change) reloads model/tool configuration and passes MCP by path, without establishing external enforcement or custom-instruction discovery. [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery) restores pending eligibility without restoring clean file state or a model conversation. Its timeout escalation qualification is supported by the inspected `child.killed` predicate.

The forcing cases and guarantee scopes remain supported. SRC-1, `src/daemon/namespace.ts` and `src/daemon/scaffold.ts` show that the child starts at `/workspace` while seeded content is under `wiki/`; the runner supplies no later directory change. Namespace setup does not hide inherited host mounts or the original raw-file alias. [RT-CLM-workspace-isolation](runtime.md#rt-clm-workspace-isolation) appropriately rejects unconditional workspace-only visibility rather than treating it as an invariant. SRC-1, `systemd/memex.service` lacks the stronger documented hardening. Ownership gates were traced through `src/daemon/server.ts`, `src/daemon/peercred.ts`, `src/daemon/peercred.c` and `src/daemon/routes.ts`; the global-token route is a separate ungated admission surface, not a general wiki-ownership bypass.

The [workflow account](workflow.md#workflow-account) faithfully selects upload → queued delegated integration → terminal result, with conditional later lint. Its annotations preserve the runtime identities. Ordering, handoff contents, upload failure without compensation, failed-job continuation, restart replay and result delivery agree with the source. Lint is neither a prerequisite for delivery nor an independent semantic acceptance gate.

### Memory and epistemic dispositions

Every memory declaration, annotation and epistemic counterpart was checked against its anchor and operative consumer. SRC-1, `src/daemon/scaffold.ts`, `src/daemon/routes.ts`, `src/daemon/db.ts` and all four `src/lib/prompts/` modules support the raw archive, derived pages, schema, index and activity-log distinctions. [MEM-OBJ-audit-log](memory.md#mem-obj-audit-log) is a separate fixed event store; the logs/status commands and client confirm reader delivery and the ignored audit-limit parameter. [MEM-RTE-file-browse](memory.md#mem-rte-file-browse) is a shipped client/server consumer route, not a hypothetical inference from a storage method. Its UTF-8 and security qualifications are necessary.

[RT-BAP-wiki-instructions](runtime.md#rt-bap-wiki-instructions) is explicitly appended static policy; [MEM-BAP-schema-guidance](memory.md#mem-bap-schema-guidance) requests later reads of use-changeable conventions. The path mismatch and lack of generated content prevent upgrading either requested schema use or revision to observed activation or benefit. Credential precedence and opaque host state agree with SRC-1, `src/daemon/auth.ts` and `src/daemon/runner.ts`. [MEM-RTE-prompt-evaluation](memory.md#mem-rte-prompt-evaluation) correctly remains a claimed maintainer procedure, supported by `docs/prompts.md`, not an implemented release gate or experiment result.

I checked each epistemic ledger function and its evidence strength. Source import does not endorse source truth. Requested contradiction checking is distinct from resolve-or-flag disposition; neither supplies demonstrated truth acceptance. Retention and links do not establish post-acceptance lifecycle integration. Schema adaptation preserves a requested policy-change opportunity without collapsing learning, reflection, theory-builder conditions or exercised self-improvement into one verdict. The separately qualified theory accounts remain supported at their instruction scope.

[EPI-RTE-result-display](epistemic.md#epi-rte-result-display) follows runner extraction → queue completion → database serialization → query printing. Its concrete plain-answer example is a code deduction of non-ampliative reshaping, not an observed answer or truth check. Its `Part of:` relation is valid because the runtime recovery container explicitly includes terminal result recording. The narrower subroute does not replace the container.

All claim records were compared with SRC-1, `README.md` and `docs/prompts.md`, and their implementation witnesses. Compounding knowledge and wiki-grounded answers are declared intent, not measured quality. Answer filing is only suggested by the query prompt, not an implemented save transaction. [MEM-CLM-reason-audit](memory.md#mem-clm-reason-audit) and its epistemic counterpart correctly distinguish possible reason-bearing job output from coarse SQLite audit entries. No evidenced-absence records are declared; the scoped negative findings do not imply absence of opaque Claude/MCP behavior.

### Withdrawal correction and reconciliation

The memory correction answer is supported by a fresh full caller-to-handler trace through SRC-1, `src/cli/commands/destroy.ts`, `src/cli/client.ts`, `src/daemon/server.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts` and `src/daemon/db.ts`. The client sends keepData in a DELETE body; the server parses only POST/PUT bodies; the handler defaults false and calls scaffold destruction before registry deletion/cascades. The CLI's preservation message reflects the requested option, not a preservation acknowledgment. The minimum passages are retained in [MEM-RTE-wiki-withdrawal](memory.md#mem-rte-wiki-withdrawal).

That record now distinguishes the isolated scaffold preservation capability from the destructive shipped API route. I checked every dependent passage: memory coverage, browse invalidation, route progression, immediate return, read-back, selection, expiry/effects, Write side and Integration issues. None retains the prior affirmative keep-data outcome. Concurrent children and filesystem-error qualifications remain appropriately local. The previous blocker is dismissed because the materially misleading preservation finding has changed, not because an execution caveat was added.

All seven supersessions in [reconciliation](reconciliation.md#reconciliation) are supported identity connections: five retained-object pairs, one browse-route pair and one audit-claim pair. They neither change values nor upgrade statuses. Queue/audit/activity-log identities, static/retained policy paths, prompt evaluation/configuration and withdrawal/replay remain distinct. Every memory integration issue has a compatible disposition. No peer conclusion depends on the withdrawn preservation finding; epistemic's coverage label mentioning keepData does not assert operable preservation. No unresolved cross-report conflict or required undeclared material part was identified.

### Omission searches and stopping decision

Selected omission questions came from the frozen tracked tree, package exports, CLI registration and producer/consumer dependencies: could a shipped caller supply hidden history, accept semantic output, consume old reasons, configure another model-dependent path or preserve withdrawn data? I inspected SRC-1, `package.json`, `src/index.ts`, the complete client/server/route registry, runner dispatch, queue/database, configuration and login commands, status/log/lint commands, all shipped prompts and `docs/architecture.md`, `docs/operations.md`, `docs/prompts.md`. These establish direct file browsing, caller-supplied history, credential import and proposed evaluation without an additional Memex semantic acceptance or automatic prior-result consumer. The withdrawal question now has a supported destructive-route disposition.

Further optional omission expansion stopped because the selected questions are resolved at the account's retained breadth and no identified material challenge lacks a disposition. Additional dependency/security auditing would not support broader claims about model compliance, successful grounding, complete context scans or causal improvement. External Claude instruction discovery, MCP services and provider context/weights remain explicitly uninspected, not evidenced absence. Those uncertainties are already faithfully scoped in the reports; they require neither a new blocker nor an additional verification limit.

## Blockers

none

## Limits

none
