# Tolaria exact-publication audit

## Decision

**Integrate with recorded limits.** No consequential defect was established in the inspected discrepancies. The publication explicitly limits its account to selected implementation paths, not observed operation, exhaustive retention, universal permission enforcement or learning benefit. In particular, the historically prominent active-note context path is now explicitly uninspected end to end; this is a coverage reduction, not a supported claim that the feature disappeared.

This is an independent bounded audit under [the next-61 commission](../../audit-next-61-commission.md) and [Audit a rerun](../../audit-a-rerun.md), not authorization to integrate. Parent scheduling, full review and integration remain separate.

## Identity and method

- Exact run: `AAS-2026-10-14-tolaria-42ddaf2ee8cd-01`.
- Auditor: fresh project worker; commissioned profile `openai/gpt-6.1-sol`, medium. No delegation.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd` (abbreviated `W` below).
- Recorded command prefix: `W/.venv/bin`.
- Method revision and independently read worktree HEAD: `a568c6dc489ad546374536b642c3889ce23149a8`.
- Sole frozen source: `https://github.com/refactoringhq/tolaria`, Git checkout `W/related-systems/refactoringhq--tolaria` (abbreviated `S`), revision `48f2a70844c1e8005a7aa5f1499c66f7678360de`. Independent HEAD matches; `GIT_OPTIONAL_LOCKS=0 git status --short` returned no changes in S.
- Publication: `W/kb/agentic-system-analyses/retained/tolaria` (abbreviated `P`). No origin incumbent was supplied.
- Read the complete commission, audit procedure, earlier substantive commission, root instructions, work collection contract and workshop framing. The owned report is plain workshop text.

Method: verify exact bytes; compare historical coverage leads; inspect the consequential write-authority and active-context differences against the frozen source; sample actual runtime analyst and independent verifier calls/results. Full public overview, boundary, synthesis and report verification were read, with selected memory-profile fields. This was not a second full analysis or a fresh semantic review of every record.

## Exact publication bytes

Independently SHA-256 checked all 13 files against the exact-run inventory row: `ARTIFACT.yaml` and all 12 Markdown members match. The actual directory contains exactly those names. The completed `effects/publish.json` identifies this run/source/destination, expects an absent incumbent, records no archive and carries the same map. All 33 stored attempt JSON records have `state: completed`; this is engine-state evidence only.

Manifest hash: `a93e9d5f36b1347b4dc8443aba66bdd4055acb6c231844cf5cc26ed920c31ac5`. This is the assembled published manifest, not the working type declaration (`093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322` in the intake). The latter hash is an intake distinction, not a separate rehash performed here.

## Historical comparison and consequential checks

Historical lead: [Tolaria review](../../../../agent-memory-systems/reviews/tolaria.md), dated 2026-06-05, reviewed commit `82b2ff2ac455334a255c7c2a2a1d2173083c6d59`. It is a different revision and review format. I did not acquire or reconstruct that checkout, assert source equivalence, or use its findings as current truth.

### 1. Read-oriented MCP versus implemented writes

The historical review describes a read/UI-oriented stdio tool list and CLI-mediated mutation. Current source search finds registered `create_note`, `update_note` and append tools in `S/mcp-server/index.js` (registration/schema near lines 197–230 and handlers near 366). `S/mcp-server/vault.js:99–128` actually implements replacement and append; replacement checks optional `expectedMtime` and then writes. Lines 539–546 show omission bypasses the comparison. The guard and write are separate operations, not atomic stale-write exclusion.

Current synthesis, “From assignment to a changed note,” correctly reports these routes, optional guard, caller-owned retry, full replacement and lack of batch rollback. It does not preserve the stale read-only characterization. `S/src-tauri/src/codex_cli.rs:336–409` separately configures the Node MCP process and maps Safe to Codex's native `read-only` sandbox. This supports distinguishing the native sandbox from the service's exposed capabilities; it does not demonstrate a live sandbox escape or actual tool execution. The synthesis already makes that distinction and withholds an application-wide read-only guarantee.

### 2. Direct-provider write qualification

`S/src-tauri/src/ai_model_tools.rs:56–169` conditionally advertises `create_note` when an active vault and provider/capability conditions hold. The returned-call loop executes supported calls sequentially and stops on error. This corroborates the publication's refusal to inherit a universal chat-only claim. The synthesis names the provider-conditional scope, local execution and earlier writes surviving later failure, without claiming all-provider tools or shell access. No audit-only qualification is needed to repair this point.

### 3. Active-note context coverage is reduced, not negated

The old review emphasizes UI-selected active-note/open-tab/list context as the distinctive push path. The new account emphasizes transcript replay and explicit references instead. `S/src/components/useAiPanelContextSnapshot.ts:26–54` still constructs context from active entry/content, tabs, list/filter, entries and draft references. That builder alone does not establish complete dispatch or actual downstream consumption.

The new memory-profile explicitly labels “Active-note snapshot and complete panel dispatch” uninspected (near lines 670–678). The synthesis's context-budget limitation says complete active-panel wiring was not retraced, and its opening declares a partial loop. This is a real loss of end-to-end coverage relative to the historical account, but it is publicly disclosed rather than recast as absent functionality. Closing it would require a bounded panel-to-payload route trace, including editor/disk provenance; it is not a prerequisite for this expressly partial publication. Desktop cache/Git, remaining adapters and collaboration lifecycle are likewise public limits, not certified exclusions.

### 4. Retention is not factual acceptance or learning

The historical review already separated transcript persistence from learned lessons. The current synthesis retains that distinction and adds concrete bounds on replay, reference omission and file-operation admission. It also discloses additional collaborative Yjs state and Markdown/revision checkpoints identified by verification. The selected worker evidence below supports that this limit arose from source inspection, not merely a publication claim. I found no inspected assertion of successful operation, factual acceptance, automatic learned lessons or causal benefit that contradicts these qualifications.

## Selected actual worker evidence

Trace: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/tolaria.output`. Locators below are one-based outer JSONL lines, then zero-based indexes in `result.details.results[0].messages`. I used completed `tool_execution_end` payloads once, not repeated streaming snapshots. Calls are paired with tool results by full ID within the same worker.

- Runtime worker: launch at outer line 865; completed nested payload at line 952, model `gpt-6.1-sol`. Messages 21→24, call `call_HyBYbjAiTVWbqzOoOIT93yC8|fc_0a907dd0194b56ed016acfd65f281c87d2bf42d8af9ba980da`, read `ai_model_tools.rs:1–220`; result returns implementation, `isError: false`. Messages 25→26 recover lines 221 onward. Messages 41→45, `call_Mk2d0uscpF582zLFx7oFj8fn|fc_0a907dd0194b56ed016acfd68eff2c87d29d0385e72a0229bd`, read `mcp-server/vault.js:1–140`; successful result includes actual update implementation. These are performed source reads, not tool proposals.
- Independent report verifier: launch at line 2293; completed nested payload at line 2409. Messages 44→45 execute environment/HEAD/tree checks, returning `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium` and the frozen source revision. Messages 87→90, `call_5Motn0b6KN3ubPQgl21TeNR4|fc_069a5d4c2db0d317016acfdb10f96887d299171fb61da71ccd`, successfully read `apps/server/src/collab/snapshots.ts`, including binary state and versioned base storage. Messages 98→99 and 98→100 return `noteSession.ts` opening/reload and saveSnapshot ranges. This is actual omission-search evidence beyond analyst prose.
- That same verifier writes its output (109→110), then directly runs the prescribed `commonplace-run validate-output .../000022-report-verification/prompt.md` (111→112), call `call_skEGA8xlTEfp5fflb1OmagEI|fc_069a5d4c2db0d317016acfdb9df8bc87d2858f832f483cb9bf`. Result: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This demonstrates that selected obligation, not exhaustive compliance.

Operational imperfections: runtime worker compound search calls at message pairs 39→40 and 48→49 returned “Command exited with code 2” and “Command exited with code 1,” respectively. These were searches, not successful full inspections; subsequent paired source reads provide direct evidence for the selected claims. No semantic refusal or consequential scope violation was established in these samples. This does not certify all workers or all writes. The 33 completed attempts do not prove absence of intermediate local revisions.

Audit access error preserved: direct read of `W/kb/agentic-system-analyses/state/AAS-2026-10-14-tolaria-42ddaf2ee8cd-01/state/handouts/000022-report-verification/prompt.md` returned `ENOENT: no such file or directory`. The complete prompt was recovered read-only from the verifier's paired read result at line 2409, messages 2→3. No state reconstruction was attempted.

## Validation

Executed from W with the recorded absolute command prefix:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/tolaria
/home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd/.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/tolaria
```

Both exit 0. Summary: `VALIDATION SUCCESS`; files analysed 1 (one directory artifact), text files 0; 0 failures and 0 warnings. Full output checks all 12 members plus directory roles/relations, reports `Overall: PASS (clean)`, WARN/FAIL/INFO all `(none)`, no excluded subtrees and no collection warnings. No source-unavailable notices were emitted. This is deterministic validation, not independent proof of quotation meaning or operational success.

Also executed from W with the same recorded prefix:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd/.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-tolaria-42ddaf2ee8cd-01.md
```

Exit 0; type `text`; `Overall: PASS (clean)`. PASS: text file has no frontmatter and no structural requirements. WARN/FAIL/INFO all `(none)`. This checks the report as workshop text, not the soundness of its disposition.

## Limits and follow-up

No additional sources, live providers, Tolaria execution, test runs, dependency internals or old-revision checkout were used. This audit does not certify every historical assertion, every profile value, every worker read/revision or all source-acquisition behavior. It leaves source, method, publications and engine state unchanged.

No blocking unblock condition is established. Parent must review this report, recheck unchanged bytes and separately authorize integration. If a complete active-note, storage or enforcement comparison is required instead of this published partial scope, commission the missing end-to-end routes before using the set for that purpose. Changed bytes or evidence contradicting a selected route require renewed review, not automatic acceptance under this disposition.
