# Continuity current-batch publication audit

## Disposition

**Integrate with recorded limits.** No consequential defect was established in this bounded audit. The public synthesis already carries the qualifications needed for source-defined continuity, incomplete organization integration and partial subsystem inventories. Integration does not certify live operation, benefit or exhaustive worker compliance.

Blockers: **none**. The coordinator owns integration; this audit performs no integration or publication edits.

## Identity and method

- Exact inventory row: Continuity, batch 02, `AAS-2026-10-14-continuity-3e490e1d39f0-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/continuity-3e490e1d39f0`; its sibling `.preparation.json` reports ready, method/input commit `4266dabc470929df0ff753e57fee0c55d7b87fc6`, and the worktree-local `.venv/bin` command environment.
- Publication: that worktree's `kb/agentic-system-analyses/retained/continuity/`.
- Run evidence: that worktree's `kb/agentic-system-analyses/state/AAS-2026-10-14-continuity-3e490e1d39f0-01/` (called `R` below).
- Frozen source: `https://github.com/uziiuzair/continuity`, checkout `related-systems/uziiuzair--continuity`, revision `4ca8f6b4108aa4494e3861ed33c8019dbd662c67`, cutoff 2026-10-14. Independent HEAD/status inspection agrees; status was empty.
- Stored method: `R/run.json` names `analyse-agentic-system/plan.yaml`, SHA-256 `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`, and profile `pi-sol`.
- Auditor runtime: Pi, `openai/gpt-6.1-sol`, medium reasoning, confirmed by `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`; session `01a138f0-3841-763e-a696-25d86abe7756`. No delegation.

Method: compare the exact publication's overview, boundary, synthesis and all three verification reports with the target-specific legacy review; challenge consequential differences against the frozen source; check publication hashes and stored judgments; inspect selected nested worker call/result evidence. No new analysis, acquisition, target execution or state-writing inspection command was used.

## Historical comparison and consequential findings

The `systems.md` row points to [the retained legacy review](../../../agent-memory-systems/reviews/continuity.md). Scoped historical search found this matching account; incidental mentions in other reviews were not treated as additional Continuity reports. The legacy review's date is 2026-06-04, but its source revision is exactly the new publication's revision. The differences below cannot be explained by a newer source checkout. Legacy comparisons and borrowing recommendations are outside the new analysis's purpose, so their omission is not a regression.

1. **The main memory architecture is retained, not lost.** Shared desktop/MCP SQLite facts, typed/versioned rows, symbolic links, narrative maintenance, passive prompt supply and requested recall remain explained. The synthesis makes admission owners and later consumers clearer. Its `Retention and later context` section qualifies the old “bounded context” account: the 50-row selection covers all scopes, groups by type and uses a nominal 4,000-character counter, not query relevance or a total-context cap. Frozen `lib/ai/memory-tools.ts:467–548` confirms selection, source/project omission and extra formatting/overflow text. This is a warranted precision gain.

2. **The legacy observation ladder was too strong.** The old review describes memory row → learning signal → narrative as the strongest ladder and calls learning signals trace-extracted. The new synthesis distinguishes caller-recorded observations from desktop model-selected fact writes, and preserves fact-fed narrative continuity even without a separate automatic desktop observation writer. Scoped searches for `learning_record`, `recordLearning` and `INSERT INTO learnings` in desktop/server/plugin roots locate the explicit producer in `server/tools/narrative-tools.ts` and `server/db/learnings.ts`, not a desktop extractor. Frozen `lib/ai/narrative-synthesis.ts:148–217` consumes active facts, scoped observations and prior narrative content. The public account correctly retains the positive fact-to-briefing path while withholding actual extraction instances, faithful transformation and improvement. See `memory.md`, `MEM-ABS-learning-extractor`, and `profile-verification.md`.

3. **Organization sync is not an established shared-memory loop.** The old review already calls integration partly scaffolded, but also describes imported remote rows and possible frontend influence more positively. The new synthesis states the concrete database-routing defect and keeps prompt delivery unresolved. Frozen `plugins/continuity-org-memory-sync/src/sync-engine.ts` calls `plugin.db.execute`; `plugin-sdk/src/db.ts:11–18` sends only SQL/params; `plugin-host/src/handlers/db.ts:23–26` defaults an omitted database selector to app storage. The same sync engine serializes deletion events without withdrawal state and advances its local-clock cursor after internally caught pull errors. These findings support the new refusal to claim joined/convergent desktop memory. They are already visible publicly, not qualifications added only here.

4. **Broader runtime coverage is useful but expressly partial.** Deep research, separate delivery milestones, plugin capabilities and Threads publication extend the older memory-focused review. The synthesis carries all four report-verification limits: packaged-distribution parity; incomplete workspace inventory; vault fidelity/containment/cleanup; relational and organization integration. Its opening paragraph explicitly distinguishes whole-system functional scope from exhaustive path inspection. I did not independently retrace all these additions; their verification accounts and visible uncertainty were inspected, not converted into a security or operational certification.

## Publication and operational evidence

`R/effects/publish.json` records completed publication to the exact inventory destination. All 13 listed file hashes match the retained files. All 12 Markdown members are byte-identical to `R/artifact/`; the manifests differ because the publication adds member hashes and worker identity, while the working manifest declares only the set type. The retained manifest reports Pi/Sol/medium; stored model attempts independently carry matching worker-reported model and effort.

Stored attempts 000001–000037 are completed. Judgment `000027-apply-profile-verification-1.json` refused the earlier profile's missing tool-feedback source branch and incomplete fact-fed narrative inventory. Attempt 000028 produced the retained replacement hash `970601714c73cbcbdd0dc6ba1ab6a7a25836de46bea3586122fdc428162ec7ce`; judgments 000029 and 000031 accept that replacement. The final public profile verification explains the repair. This is semantic correction evidence, not merely engine completion.

The coordinator log `kb/work/agentic-system-reruns/outputs/continuity.output` contains 12 completed subagent results with nested messages. Thus worker traces are available here, although transient handout directories are not retained under `R/state/`. Selected inspection paired calls and tool results within the report and synthesis verification workers. For example, log line 2510, report verifier call `call_gZO2B7KypIxnAGCsUPjemkJv|fc_0c48d72286209748016aced074253087d29350a5730e4dc4c2`, actually reads the SDK database wrapper and receives a non-error result. Both selected verifiers execute `commonplace-run validate-output`; paired results say member content passes, invocation residue is not checked, and this is not job acceptance or claim support. The synthesis verifier also recovers split member reads. These witnesses establish selected performed obligations, not every worker's complete source-isolation, read recovery or write-scope compliance. No unavailable trace is presumed compliant.

## Validation and remaining coverage limits

Called from the prepared worktree with its `.venv/bin` first on PATH:

```text
commonplace-validate kb/agentic-system-analyses/retained/continuity
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/continuity
Scope: kb/agentic-system-analyses/retained/continuity
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The validator reports the directory artifact as one analysed file; this is not a claim of 12 independent semantic audits. From the same prepared command environment, report validation returned:

```text
commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-continuity.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-continuity.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-continuity.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
``` No pytest or target tests were run. This audit is not an exhaustive source, distribution, security or trace-compliance review. The publication's no-execution/no-causal-comparison boundary remains essential. Any request to certify those stronger properties requires separately authorized evidence work, not removal of these limits.
