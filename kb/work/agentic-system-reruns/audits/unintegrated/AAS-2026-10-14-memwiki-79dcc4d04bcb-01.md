# Independent audit: MemWiki

**Disposition: integrate with recorded limits.** No integration blocker established
within this bounded audit. Integration remains a separate coordinator decision.

## Identity and inspection boundary

- Run: `AAS-2026-10-14-memwiki-79dcc4d04bcb-01`.
- Auditor: `audit-memwiki`, Pi, `openai/gpt-6.1-sol`, assigned medium effort;
  session `01a13b10-6fed-730d-8d2c-25fae212b616`.
- W: `/home/zby/llm/commonplace/.commonplace/worktrees/memwiki-79dcc4d04bcb`.
- P: `W/kb/agentic-system-analyses/retained/memwiki`.
- Method: `f7732e9c6bc5622031571d2d429bc017253eb64f`; ready preparation
  independently matches method and token `79dcc4d04bcb`.
- Frozen source: `https://github.com/hereisSwapnil/memwiki`,
  `W/related-systems/hereisSwapnil--memwiki`, revision
  `8034a3da991ac2639b87875172a9572903ecf1d5`; HEAD matches and status is clean.
- Historical lead: `kb/agent-memory-systems/reviews/memwiki.md`, checked
  2026-06-18 at the **same revision**. No moved-account boundary is involved.
  No origin-main incumbent exists at the publication path; no replacement question.
- Method: compare historical mechanism coverage with public overview/synthesis;
  check consequential differences against frozen CLI/protocol/package/index/log;
  inspect publication bytes, attempt states and paired worker validation evidence.

## Findings

1. **No consequential mechanism regression found.** Synthesis preserves the thin
   installer versus host-agent maintenance distinction, hook entry, hot-first and
   conditional page reading, work/raw ingestion, session-end persistence, and
   chat-only lint/fold. The executable accepts only `init` and `update`.
   Evidence: `P/synthesis.md`, source `src/index.ts`, `AGENTS.md`, `README.md`.
2. **Historical push classification is not current implementation evidence.**
   Source hooks request file reads; they do not independently deliver selected
   wiki payloads. The new pull-only classification is bounded to those shipped
   routes and excludes host internals. Likewise, original trace serialization
   is unresolved rather than inferred from dated summaries. These changes narrow
   unsupported historical claims without losing the declared continuity loop.
   Evidence: `P/memory-profile.md`, `P/synthesis.md`, source `AGENTS.md`.
3. **Update safety is qualified publicly.** Four protocol/hook files are replaced
   without merging customizations; existing wiki files are skipped, while missing
   ones are created. Init also skips existing hooks. This corrects the historical
   shorthand that update leaves the wiki untouched. Distribution equivalence is
   explicitly unverified: the package points to untracked `dist/index.js`.
   Evidence: `P/synthesis.md`, source `src/index.ts`, `package.json`.
4. **Two accepted local defects remain visible, not silently certified.** The
   frozen index has six outgoing links; workflow's seven-page enumeration remains
   inconsistent. The profile omits separate assessment of patterns/bugs/decisions
   work-discovery routes. Synthesis records both and withholds exact link-count
   consistency and complete per-route comparison. Neither changes the central
   mechanism or supported positive existence finding. No audit-only repair needed.
   Evidence: `P/reconciliation.md`, `P/synthesis.md#limitations`, source index.
5. **Benefit and factual acceptance are not overstated.** Public synthesis records
   host dependence, absent execution/causal comparisons, lint's proposal-versus-fix
   ambiguity, untested folding, self-dependency despite dependency-free prose,
   and reported landscape/competitor links missing from the index. Frozen protocol,
   README, package metadata and log support those qualifications.

## Publication and operational evidence

- `effects/publish.json` is completed; actual file set and all 13 SHA-256 values
  match its `new` map and the assigned inventory. No extra publication files.
- Assembled manifest: `f15e6631931d5086e380d64632b00acfba545bcde6db47a63627b3bfc08c18cb`.
  Working declaration: `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`;
  these are distinct artifacts. Attempt `000033-publish` pins the assembled hash.
- All 33 stored attempts are completed. This establishes acceptance, not obedience.
- Trace: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/memwiki.output`.
  Parsed terminal subagent results, not duplicate update snapshots. Within each
  of 11 analytical workers, paired its executed `validate-output` call with its
  own tool result; every worker ultimately obtained the member-content pass.
- Trace line 2624, worker `000024-memory-profile`, first reports
  `trace_learning.units[2]: local no requires resolved bounded absence`, then
  `[Errno 2] No such file or directory: '/home/zby/llm/commonplace/.commonplace/worktrees/memwiki-79dcc4d04bcb-01'`.
  Same-worker subsequent validation passes; accepted profile uses inapplicable,
  not local no, for pure repository ingestion. These resolved errors are not holds.

## Validation and limits

Called from W with `.venv/bin/commonplace-validate`, without output/state writes:
- Publication target `kb/agentic-system-analyses/retained/memwiki`:
  `VALIDATION SUCCESS`; files analysed 1, text files 0, 0 failures, 0 warnings.
- Owned origin report, absolute path: `VALIDATION SUCCESS`; files analysed 1,
  text files 1, 0 failures, 0 warnings.

This is not exhaustive worker-compliance certification or a target execution test.
No source acquisition, target code execution, delegation, accepted-output changes,
engine mutation or integration was performed. Public limitations already carry
all consequential qualifications found here. **Blockers: none.**
