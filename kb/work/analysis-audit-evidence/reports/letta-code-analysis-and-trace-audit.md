# Letta Code analysis and trace audit

## Judgment and identity

The sampled implementation claims are supported, publication bytes agree with
run evidence, and semantic review removed an unsupported comparison value.
Trust this as a bounded, code-grounded analysis, not an exhaustive inventory or
evidence of successful learning. This partial audit found no new substantive
correction requiring a replacement analysis. It does not certify every record.

The traces contain recovered quotation failures and shell wrappers that report
success after inner failures. Final publication therefore does not imply an
error-free process. The profile repair is evidence that review worked, not a
reason to remove that review.

```yaml
run-id: AAS-2026-10-11-letta-code-88afa3263646-01
method-commit: 0265fff4dd8a9d00fa2aba78495b2c95b2abbad6
source-revision: 271f119dcf37d58649a18e6c733386b3c710a456
audit-date: 2026-10-11
worker-profile: pi-sol
worker-runtime: {harness: pi, model: openai/gpt-6.1-sol, reasoning-effort: medium}
reporter-profile: {harness: pi, model: openai/gpt-6-astra, reasoning-effort: medium}
```

Reporter identity is exposed by `PI_PROVIDER`, `PI_MODEL` and
`PI_REASONING_LEVEL`, not inferred from the audited profile. This auditor is a
separate worker, but not a blind reviewer: it read the retained verification
and previous workshop reports. No delegation was performed by this auditor.

## Evidence, approach and limits

Local locators below identify evidence, not alternative run identities:

- `W`: `/home/zby/llm/commonplace/.commonplace/worktrees/letta-code-88afa3263646`.
- `R`: `W/kb/agentic-system-analyses/state/AAS-2026-10-11-letta-code-88afa3263646-01`.
- `A`: `W/kb/agentic-system-analyses/retained/letta-code`.
- `S`: `W/related-systems/letta-ai--letta-code`.
- `T`: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T07-51-46-718Z_01a129f2-491e-711e-8a12-57ed0373030a.jsonl`.

`T L<n>/R<n>/m<n>` means a one-based JSONL line, zero-based
`message.details.results` index and zero-based embedded message index.
Trace findings below concern tool actions and results, not private reasoning.
The handout directories are no longer present; embedded worker messages and
content-addressed versions remain available.

I chose three complementary checks:

1. Independently hash the publication, manifest members and version store;
   compare identities and historical judgments without running the analysis
   engine.
2. Read the boundary, synthesis, full memory profile and report/profile
   verification, then sample consequential implementation claims against the
   frozen source. Samples target production-versus-stub execution, committed
   versus current-file context, and hook failure semantics. These distinctions
   can change how a consumer interprets the analysis.
3. Scan tool results across all twelve analytical worker transcripts for
   failures, examine recovery sequences and the profile repair, and calculate
   timing from retained timestamps. Compare prior audit measurements with
   explicit scope and method qualifications.

The trace inventory contains 811 embedded messages and 470 tool results:
371 reads, 58 shell calls, 30 writes and 11 edits. This is an inventory and
failure-oriented scan, not a line-by-line semantic review of all 371 reads.
All twelve analytical result envelopes report exit zero and normal completion.
The diagnostic launch and subsequent audit activity are excluded.

Coverage is deliberately partial. Runtime and epistemic records were not
independently reviewed in full; neither were every quotation, model resolver,
reflection branch, remote driver, compaction fallback or security boundary.
No target execution, provider calls, causal experiment, network acquisition or
integration into the main retained collection was checked. Prior runs' timing
and findings come from their workshop reports, not a fresh audit of their
traces. Missing coverage is unknown, not a pass.

The user explicitly authorized direct read-only inspection of the frozen
source for this audit. This report is workshop evidence about that run, not a
new ingest or authoritative external-system characterization. The writing and
validation skills were read; no source records or ancillary briefs were added
outside the sole authorized report path.

## Observations

### LC1 — Publication and historical identity agree

The preparation record `W.preparation.json` pins the method commit above and
records exclusion of dirty-origin changes. Worktree HEAD independently matches
that commit. `R/effects/acquire.json`, `A/boundary.md` and source HEAD agree on
the source revision; source `git status --porcelain` is empty.

Independent SHA-256 calculations found:

- All twelve files named by `R/effects/publish.json.new`, including
  `ARTIFACT.yaml`, match the bytes at its retained destination.
- All eleven Markdown member hashes in `A/ARTIFACT.yaml` match their files.
- All 81 files under `R/state/versions/` hash to their filenames.

For reproducible spot checks, the published manifest hash is
`48d258aa46cac187616c7b1c8f8a9eee3c29bde40d6fc16b035fc099e22873a9`;
the repaired profile hash is
`ae9ce40d20107c950178ed0753cbf01374a5ad68c0d00cd20cdbf4b7452ce382`.
The working `R/artifact/ARTIFACT.yaml` is type-only. Its difference from the
published manifest is not evidence of corruption: the assembly product and
publication journal pin the expanded manifest separately.

The state contains 32 completed attempts: twelve model and twenty code jobs.
Its 23 judgments comprise 22 acceptances and one refusal. Thus present
completion and historical refusal coexist. These checks establish local byte
correspondence, not independent provenance authentication or correctness of
all claims.

### LC2 — Consequential source samples support the retained qualifications

| Sample and retained anchor | Independent source inspection at `S` | Audit result |
|---|---|---|
| Local execution is not merely a deterministic stub: `A/boundary.md`, Boundary and evidence | `src/backend/local/local-executor-factory.ts:42–74` | The factory first permits an explicit executor and two deterministic modes, then constructs `ProviderTurnExecutor` with `PiStreamAdapter`. This supports the normal-path distinction, not a claim that every invocation uses a provider. |
| Committed projection differs from current checkout reads: `A/memory.md#mem-rte-core-projection`, `#mem-rte-deferred-read`; synthesis, What later invocations receive | `src/backend/local/system-prompt-compilation.ts:81–199`; `src/backend/local/local-backend.ts:896–976`; `src/tools/impl/memory.ts:306–405` | Compilation enumerates Git HEAD and reads `HEAD:<path>`. Revision changes can produce a separate mid-conversation update while retaining the original prompt. Memory rendering uses `readFileSync` on the resolved checkout path. The analysis correctly avoids a universal committed-only visibility claim. |
| Root archival is not automatic withdrawal: synthesis, From completed activity to standing guidance | `src/agent/memory-format.ts:13–21`; `src/backend/local/system-prompt-compilation.ts:150–199` | V2 core selection includes root `.md` files; the renderer excludes `MEMORY.md` from the ordinary root loop but not `ARCHIVE.md`. The warning is a valid predicate-based deduction, not an observed archival incident. |
| Hook ERROR differs from BLOCK: `A/epistemic.md#epi-rte-hook-disposition`; synthesis, From invocation to action | `src/hooks/executor.ts:392–468`; `src/tools/manager.ts:2192–2220` | BLOCK sets `blocked`; ERROR sets `errored` and continues. The inspected manager consumer returns before execution for `blocked`, not merely `errored`. This supports the narrow non-fail-closed distinction, not universal behavior across all hook consumers. |

The synthesis repeatedly distinguishes implementation from execution and
benefit. The sampled code does not warrant upgrading those claims. The existing
verification also retains incomplete recall, maintenance and remote coverage;
this audit did not close those gaps.

### LC3 — Semantic review removed an unsupported extracted value

The first profile emitted `curation_operations: promote` with a claimed basis:
it inferred an upward change of tier or salience from generic tiering guidance.
The first profile verifier refused that positive value. Its objection was
specific: an overall partial assessment does not make an unsupported positive
safe for comparison consumers.

Evidence chain:

- Attempt `000019-memory-profile` produced profile version
  `cc6252d99656b2ad74f0a83bf340141e84e3c7529392db7cf467a944b40c316a`.
- Verifier version
  `6fb28aefdeb82bf7744669e44d9f421b7f2950d2fb4d334230133821e69545fc`
  has the objection under Blockers.
- `R/state/judgments/000022-apply-profile-verification-1.json` records
  `outcome: refused`, `installs: false`, with no overrides.
- Attempt `000023-memory-profile` removes the seven-line positive finding,
  adds the missing directionality qualification to its unit note, and revises
  the rationale. A direct old/new version diff shows those three changes,
  rather than a broad unexplained rewrite.
- `000025-profile-verification` accepts the substantive repair;
  `000026-apply-profile-verification-1.json` installs the revised profile with
  `outcome: accepted` and no overrides. Trace anchors are `T L45`, `L49`, `L53`.

This is a successful local safeguard. The unsupported value does not survive
in the published profile. The audit checked the repair and judgment chain;
it did not independently reclassify every reflection instruction.

Two nonblocking profile limitations remain explicitly visible: the omitted
separate prose-consumption path for changed hook criteria, and overly cautious
local runtime authorship classification. Both appear in
`A/profile-verification.md#limits` and the synthesis limitation table. Readers
must not treat the profile as complete part-level coverage. These are retained
review findings, not newly discovered audit defects or additional independent
runs.

### LC4 — Quotation checks repeatedly failed, then succeeded

Four original analysts needed local quotation repair:

| Worker trace | Failure and recovery |
|---|---|
| Boundary, `T L19/R0/m55–69` | Two validator failures over attribution syntax; an intervening edit also failed because its old text matched twice (`m57`). The worker inspected the parser, added revision-qualified attributions and passed at `m69`. |
| Runtime, `T L23/R0/m80–92` | Missing revision syntax, then a duplicated provider-adapter quotation. Revised attribution/range and later edits passed at `m92`. |
| Memory, `T L27/R0/m80–84` | A headless skill-delivery quotation occurred twice. A range correction passed at `m84`. |
| Epistemic, `T L27/R1/m60–70` | Missing revision syntax, then ambiguous compaction/hook/manager quotations. Range edits passed at `m70`. |

These are seven failed validator invocations across four workers, not seven
independent runs. The repair sequence demonstrates value in deterministic
checks. It does not prove every selected occurrence supports its surrounding
claim; the hook sample in LC2 supplies a separate semantic check for one of
the repaired areas. No new full-set validation was run against audited state.

### LC5 — Some failures were text-visible but masked at the shell boundary

Runtime validator calls ended with `printf` after capturing the return code.
At `T L23/R0/m80` and `m84`, output says `EXIT=1` but the tool result has
`isError: false`. The same mechanism occurs for Memory's failed validator
(`T L27/R0/m80`) and both failed Epistemic validators (`T L27/R1/m60`, `m66`).
The workers read the textual diagnostics and repaired them, so these five
masked validator failures did not bypass publication checks in this run.

Missing guessed source paths also reached nominally successful wrappers:
`src/hooks/runner.ts` in Runtime `T L23/R0/m53`, and
`src/tools/index.ts` / `src/hooks/runner.ts` in Epistemic
`T L27/R1/m22`, `m31`. The latter prints `search-exit=2` before later commands.
Subsequent reads of the real hook executor and manager underpin the repaired
account; the missing guessed file was not treated as proof of absent hooks.
These are at least eight masked inner failures, not an exhaustive count of all
nonzero search statuses.

Counterexamples matter. Boundary's failed validator correctly propagates its
status (`T L19/R0/m55`, `m61`, `isError: true`), and Memory's nonexistent
`system-prompt.ts` read reports ENOENT directly (`T L27/R0/m28`). A failed
operation is therefore not uniformly hidden by this harness. The demonstrated
mechanism is command construction, not proof of a broken tool error channel.

### LC6 — Publication prerequisite was loaded before publication here

The coordinator read `publish-analysis.md` at `T L36–37`, before the final
publication-producing advance at `L62–63`. This is a counterexample to the late
read reported in the Letta and Graphiti 85a21a06d35c audits. It does not establish
that all coordinator prerequisites or worker instruction reads were ordered
correctly; those were not exhaustively audited.

## Timing and comparison

Worker durations below use the minimum and maximum numeric timestamps within
each embedded worker transcript. They include tool and model waiting within
that span, but not the entire launch/return overhead. They are not provider
compute time. All timestamps are from the retained trace, not filesystem mtimes.

| Attempt | Trace result | Embedded span, seconds |
|---|---|---:|
| Boundary 000003 | L19/R0 | 239.827 |
| Runtime 000005 | L23/R0 | 489.926 |
| Memory 000007 | L27/R0 | 493.669 |
| Epistemic 000008 | L27/R1 | 430.080 |
| Reconciliation 000014 | L31/R0 | 176.996 |
| Report verification 000017 | L35/R0 | 267.205 |
| Profile 000019 | L41/R0 | 251.492 |
| Profile verification 000021 | L45/R0 | 202.953 |
| Profile repair 000023 | L49/R0 | 131.715 |
| Profile re-verification 000025 | L53/R0 | 174.225 |
| Synthesis 000027 | L57/R0 | 252.825 |
| Synthesis verification 000029 | L61/R0 | 163.990 |
| **Summed worker duration** | | **3,274.903 (54.58 min)** |

Preparation call through publication-producing result spans **3,105.776 s
(51.76 min)**, `T L12–63`, 07:52:13.717Z–08:43:59.493Z. Start call through the
same result is 3,097.034 s. Memory and Epistemic launched together at `L26`;
other analytical launch groups were sequential. Summed worker time exceeds
wall time despite preparation and coordinator overhead because that pair
overlaps. Summing top-level subagent tool durations gives a different measure,
2,916.892 s: occupied call envelopes with the parallel pair counted once.
None is interchangeable with total elapsed time or billed compute.

The repair plus fresh re-verification adds **305.940 summed worker-seconds**.
Their launch-to-return window is **330.386 wall seconds** (`L48–53`), including
a coordinator advance between them. The first verifier's useful detection
cost is separate; it should not all be labelled waste. The long Runtime,
Memory and Epistemic spans include source exploration and quotation repairs;
this audit did not isolate how much time each activity caused.

Harness-reported totals for the twelve analytical workers are 317 model turns
and 4.5389664 reported cost units. These exclude coordinator, diagnostic and
audit activity and are not an invoice.

| Comparison run | Available timing and scope | Confounds and interpretation |
|---|---|---|
| `AAS-2026-10-10-graphiti-85a21a06d35c-01` | Prior audit reports about 38½ min preparation-to-publication, ten workers, 264 turns and cost 3.9385776. | Full analysis, same pi-sol/medium profile. Letta Code has two extra profile repair/review attempts and broader shipped harness surfaces. Those extra attempts explain part, not all, of its longer elapsed time; source complexity, output scope, service latency and cache behavior are not controlled. |
| `AAS-2026-10-10-napkin-b831630d0978-01` | Prior audit reports 2,420.02 summed worker-seconds, thirteen workers, 305 turns and cost 4.1360508. | Full analysis with overlap. Its summed time is comparable only as worker-span cost, not as a 40-minute wall time. More workers did not imply greater summed duration than Letta Code. Scope and inspection depth differ. |
| `AAS-2026-10-11-letta-d460b458ddad-01` | Prior audit reports 177.145 s authorized preparation retry to local completion; one worker, about 129.9 s embedded span. | Blocked landing-page source, not the implementation repository. No downstream analysis or verification. Its 2,210.645 s authorization wait is operator latency and excluded from that active interval. This is an early-stop comparison, not an implementation-analysis speedup. |

Comparison sources: [Graphiti 85a21a06d35c audit](./graphiti-85a21a06d35c-analysis-and-trace-audit.md),
[Napkin audit](./napkin-analysis-and-trace-audit.md), and
[Letta audit](./letta-analysis-and-trace-audit.md).
All three pin method `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad`, unlike this
run's `0265fff4dd8a9d00fa2aba78495b2c95b2abbad6`. An independent commit diff
shows only four workshop/navigation files changed between those commits; no
analysis method or implementation changed. This makes mechanism comparison
reasonable, while preserving the distinct method-commit identities. It does
not make different sources and execution conditions a controlled experiment.
The other Graphiti audit reports no established timing/cost total, so none is
invented here.

## Cross-run interpretation and recommendations

Observations and proposed dispositions are separate:

| Mechanism | Evidence and counterevidence | Disposition |
|---|---|---|
| Shell status lost after logging | LC5; Graphiti GT2 and Napkin T2 report the same wrapper mechanism. Letta L2 and this run's Boundary preserve status. | Recurring behavior under the same analytical code/profile, not an estimated failure rate. Existing-rule compliance and variable command construction remain plausible causes. |
| Semantic review corrects a structurally admissible positive | LC3; Graphiti GT1 and Napkin T1 report different substantive repairs. | Successful safeguards across distinct runs. Specific content errors differ; do not merge them into one proven method defect. |
| Quotation repair | LC4; Letta L2 and Graphiti/Napkin recovered-failure sections. | Recurrent local cost with successful checks. Attribution-format usability, source repetition and model compliance remain competing explanations. |
| Late publication read | This run LC6 complies; Letta L3 and Graphiti T1 report late reads. | Retain the counterexample. No evidence here supports an additional gate. |

The [Graphiti audit](./graphiti-analysis-and-trace-audit.md) supplies GT1/GT2;
multiple reports about one Graphiti run are not counted as multiple runs.

Recommendations for the operator, not adopted changes:

- Retain the current bounded result and its explicit limitations. Do not use
  the profile as an exhaustive part-level comparison or the synthesis as
  demonstrated benefit. No replacement run is recommended from this sample;
  a contradictory source-backed claim would change that recommendation.
- Preserve historical refusal/repair evidence when assessing trust. Its benefit
  is distinguishing successful recovery from error-free execution; its cost is
  audit and retention effort. If it does not change trust decisions, a shorter
  recovery summary may suffice, but deleting the evidence is not authorized.
- Apply the existing shell-status preservation rule rather than adding another
  method instruction on this evidence. Correct propagation is cheap and makes
  failure visible; textual recovery in this run limits the demonstrated impact.
  Any tooling change or controlled comparison needs separate authorization.

No method proposal is inferred solely from this run. Broad graph discovery
through `cp-skill-connect` is a possible later step, not part of this restricted
write commission. The coordinator owns workshop navigation updates.

## Verification and preservation

This audit used read-only Python/stdlib calculations and Git inspection, not
`commonplace-run`, `commonplace-analysis` or a state-locking inspection command.
Only this report was written. The pre-existing README modification and three
untracked peer audit reports were left untouched. No method, retained member,
run state, source, index or commit was changed.

`commonplace-validate kb/work/analysis-audit-evidence/reports/letta-code-analysis-and-trace-audit.md`
returned:

```text
VALIDATION SUCCESS
Target: kb/work/analysis-audit-evidence/reports/letta-code-analysis-and-trace-audit.md
Scope: kb/work/analysis-audit-evidence/reports/letta-code-analysis-and-trace-audit.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```
