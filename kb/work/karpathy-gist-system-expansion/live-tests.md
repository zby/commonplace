# Sequential live command tests

## Historical record — current status supersedes the handoff

The sections below retain the six-run pilot, its stop decision and initial
integration refusal. They are not current pending-work instructions. The
[2026-11-09 reconciliation](./status-2026-11-09.md) confirms that all 30 original
targets, including these six, now have integrated publications and comparisons
have been refreshed. Later execution does not by itself establish prevention of
the recurring worker mistakes diagnosed here.

## Commission and limits

The operator authorized sequential live testing of the dispatch list on
2026-11-07: run one system, repair local errors and rerun, inspect its results
and traces for hidden failures, then proceed to the next. Stop for a defect
requiring fundamental changes or bugs still recurring after the first five
live attempts. Count every actual analysis execution attempt, including reruns,
and also track distinct systems. Do not silently reset that counter.

This commission adds live execution to the earlier discovery-only commission.
It does not authorize integration of publications, cleanup, source edits or
rewriting a prepared method. Use `pi-sol` and default three role workers, with
one analysis at a time. Keep triage rationale outside worker inputs. Inspect
only this campaign's Pi worker traces; completed advisory audits are leads,
not independent correctness certificates. Preserve all failed evidence.

Use the checked-in method at launch. Local code/method repairs require targeted
regressions, relevant tests and a commit before a fresh worktree can test them.
Resume the original run only when its existing method can perform the intended
recovery. Never mutate a pinned worktree or launch a replacement while ownership
or effects remain unsettled. A fresh run after a committed repair must cite its
settled predecessor and why its old method cannot test the fix.

## Preflight

- First target: `https://github.com/liushengyu/memexos`, first URL in dispatch order.
- No matching retained path, named worktree, completion-workshop assignment or
  active analysis process was found by the scoped ownership checks.
- Method at first intake: `0aa1fb36a` (default HEAD; exact hash retained by controller).
- `commonplace-analysis` and Pi are installed on PATH; selected profile is
  `pi-sol`, model `gpt-6.1-sol`, medium effort.
- Local filesystem: 36 GiB available, approximately 22.7 million free inodes.
  Existing sample worktree occupies 259 MiB. Use default ignored worktree parent,
  retain evidence and recheck space before each target. Stop before a new launch
  if available storage falls below 10 GiB; do not clean other evidence.
- Unrelated dirty theory, source ingests, script/tooling and workshop navigation
  are excluded from all method commits.

## Attempts

### 1 — memexos

Intake authorized; controller destination:
`.commonplace/worktrees/controllers/gist-live-01-memexos`.
Command exited 0. Published only in its isolated worktree; not integrated.

- Run: `AAS-2026-11-07-memexos-5cd34a715eb7-01`.
- Worktree: `.commonplace/worktrees/memexos-4460a2f51a56`.
- Frozen source: `bb9e9b2ac0adbca87d13a9f7600867128b5f71b9`.
- Method: `0aa1fb36a5915c260dd07adb7933df1f0eea2587`.
- Controller JSON/stderr: `.commonplace/worktrees/gist-live-tests/01-memexos.*`.
- Fourteen role attempts, including epistemic correction and renewed report
  verification/reconciliation. All final verifiers accepted. Overview and
  synthesis were read; retained-artifact validation passed without warnings.
- Audit snapshot under the run: `audit/ae66e319ec961f3318a1403c03f0836dfb278f5cfd6b2f76b4ee2ad6baf389ce/`.
  All 14 worker streams scanned as Pi JSON, zero partial/unscanned streams and
  zero input issues; ten scanner failure leads (including nested representations
  of the same missing read, not ten distinct bugs). No provider observations.
- Audit read and original trace failure/recovery sequences sampled in memory,
  runtime, epistemic, profile and report verification. Observed missing paths,
  drafting/syntax mistakes, duplicate profile citations, citation labels and
  quote attribution repairs. The completed artifact and accepted verdicts
  establish final validation, not success of every intermediate operation.
- Bounded audit checked capture/retrieval/publication exceptions against source
  and established no material final defect in those passages. Final synthesis
  explicitly retains incomplete acquisition/evaluation inventories and lack of
  runtime benefit evidence. No automation code bug established; no patch or
  redundant rerun required. Comparisons remain unchanged and stale relative
  to this new worktree publication.

### 2 — Obelyth/cortex

No existing ownership found by source-identity checks of run parameters;
36 GiB remains available. Next source: `https://github.com/Obelyth/cortex`.
Controller: `.commonplace/worktrees/controllers/gist-live-02-cortex`.
Command exited 0; published in worktree only. Run:
`AAS-2026-11-07-cortex-6101286707a0-01`; worktree
`.commonplace/worktrees/cortex-b09108a35d0c`; source revision
`65d449a3275eee51efd6ce0c275572806ee9d553`; same method as attempt 1.
Thirteen role attempts; one profile-verifier blocker was corrected and accepted.
Overview, synthesis, final profile verification and audit were read; retained
validation passed without warnings. Audit `9fc1a2b506c8df45a7d9d94007bbe0f1115944d921209006489f6b773334d947`
scanned all 13 streams with 14 failure leads, no input/coverage gaps and no
provider observations. Leads include missing/guessed paths, undefined codemode
root, failed globs and repaired quote/citation validation. The audit checked
cache policy and access-history/lifecycle claims against source and successful
follow-up reads; no material final defect was established. The repeated profile
work and failed tool calls are execution overhead, not evidence of an automation
bug. No code repair or additional run was needed. Not integrated; comparisons
not rebuilt. Console-adapter and development-plane coverage remain bounded.

### 3 — exia-seed

Next URL: `https://github.com/francisdu53/exia-seed`; source-identity ownership
checks found no existing run. Controller:
`.commonplace/worktrees/controllers/gist-live-03-exia-seed`.
Command exited 0; published only in the isolated worktree. Run:
`AAS-2026-11-07-exia-seed-804e805b7a8d-01`; worktree
`.commonplace/worktrees/exia-seed-c2176cbd6b2b`; source revision
`c7497ac96da20bd1818096e35a59b6c0237f9730`; unchanged method. Eleven
role attempts, no role-level correction rounds. All three verifier stages
accepted. Overview, synthesis and audit read; retained validation passed.
Audit `e7c7ff0db006f75e5e3473e71cf582a6043f86b8afc97fe6d7616e03809c0567`
scanned all 11 streams: four leads are two failed guessed-path reads plus
nested batch representations, no input/coverage gaps or provider observations.
Original successful replacement reads and their collateral reads were checked
at epistemic trace lines 1880–1890 and runtime lines 1133–1139. Audit checked
benchmark judge semantics, forced nightly closure and withdrawal handling
against source; no final defect established. Limits include benchmark inventory
and grouped profile units, disclosed in synthesis. No automation bug or code
repair; not integrated, no comparison rebuild.

### 4 — suwonleee/llmwiki

Next URL: `https://github.com/suwonleee/llmwiki`; no existing source-identity
ownership found. Storage before launch: 35 GiB available.
Controller: `.commonplace/worktrees/controllers/gist-live-04-llmwiki`.
Command exited 0; published in worktree only. Run:
`AAS-2026-11-08-llmwiki-7f7e35008c0f-01`; worktree
`.commonplace/worktrees/llmwiki-43812a7c978d`; source
`e6be788bdfd969c3695f839a5d6b5752bb233cfc`; unchanged method. Fifteen role
attempts. First report verification required epistemic, memory and reconciliation
corrections; final verifiers accepted. Synthesis and audit were read; retained
validation passed without warnings. All 15 streams scanned, seven leads,
zero input/coverage gaps. A normal `git diff --no-index` difference is not a bug;
other leads were a synthetic nonexistent-path probe and repaired ledger syntax,
quote anchors, status enum and citation labels. Original quotation repair and
successful validation at memory trace line 13820, and ledger-generation recovery
at epistemic lines 10391–10394, were checked. Audit checked failed topic-merge
rollback, authority ledger and turn-context caps against source; no material
analysis defect established. The target's reachable failed-merge rollback defect
is a finding about llmwiki, not a bug to fix in this Commonplace commission.
No method/code patch or redundant rerun needed. Not integrated; comparisons
unchanged. Alternate read-back inventories remain explicitly incomplete.

### 5 — llm-wiki-newsroom

Next URL: `https://github.com/alfadur7/llm-wiki-newsroom`; source-identity
ownership check found no existing run. Storage: 35 GiB available.
Controller: `.commonplace/worktrees/controllers/gist-live-05-newsroom`.
Command exited 0; publication in worktree only. Run:
`AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01`; worktree
`.commonplace/worktrees/llm-wiki-newsroom-ded445f4e371`; frozen source
`8e209cab483da544852d7213f0e25291d06d8a88`; same method. Sixteen role
attempts included epistemic and profile corrections; final verifiers accepted.
Synthesis and audit read, retained-artifact validation passed. Audit
`898bb69afba070cbf991174c77193410dce9585641c42cc9f4f5fcfd734d3fca`
scanned all 16 streams; three leads: two beyond-EOF requests and a repaired
export quotation. No coverage/input gaps. Original source reread/quote-edit/
validator pass at runtime events 10004–10493 and already-complete Reporter read
at workflow events 1021–1022 were sampled. No material output defect or command
bug established. Audit's revision comes from frozen checkout and report boundary;
receipt source-revision is null because no explicit source revision was requested.
No mutation of the external source. Not integrated; comparisons unchanged.

## Five-attempt checkpoint

Five distinct systems and five full analysis executions completed. Zero
controller/preparation failures, unsettled launches, unscanned role traces or
established automation defects. Transient worker read/draft/validation failures
and verifier corrections occurred, but final acceptance was not bypassed and
bounded audits found no consequential surviving defect. These are retained as
process overhead, not silently relabelled clean runs. Continue sequentially;
apply the recurrence boundary after the next attempt. Distinguish an
orchestration defect, recurring worker execution mistakes and expected verifier
rejections or search no-matches; do not collapse them into one bug count.

### 6 — crow-hq/llm-wiki-v2

Next URL: `https://github.com/crow-hq/llm-wiki-v2`; no source-identity ownership
match found. Storage: 35 GiB. Controller:
`.commonplace/worktrees/controllers/gist-live-06-llm-wiki-v2`.
Command exited 0; publication in worktree only. Run:
`AAS-2026-11-08-llm-wiki-v2-5abff9a6c5c3-01`; worktree
`.commonplace/worktrees/llm-wiki-v2-0504f862305f`; frozen source
`e0a205afe60bd1913d083a3ed4cdab81e38e4c26`; unchanged method. Eleven role
attempts; final verifiers accepted without role-level correction. Synthesis and
audit read, retained-artifact validation passed. All 11 streams scanned; four
leads represent a boundary quotation failure, nonexistent benchmark filename,
and missing prompt-module read with its enclosing failed batch. Original
replacement quotation/content check, prompt/store reads and benchmark reads
were checked at the audit's cited trace events. Audit
`16449a38c3c99332f9131a617a9ecb48235b7a11882c145213ca1b2606f7e6c1`
verified selected MCP, persistence, evaluator and reported-comparison claims
against source; no material final defect established. No controller failure,
uncertain effect or unresolved worker launch. Not integrated.

## Stop decision and handoff

**Stopped before system 7**, applying the operator's recurrence limit
conservatively to worker execution mistakes, not only controller software bugs.
The sixth run repeats the guessed-path and nonmatching-quotation failures seen
in earlier runs. Relevant recovery was checked, but successful repair does not
establish prevention. Normal verifier objections and deliberate search/diff
statuses are not themselves bugs. No fundamental architecture defect or broken
controller receipt was established, and no speculative code/prompt patch was
made. There was therefore no new method to justify an additional paid rerun.
The workflow itself already performed the required content corrections and
renewed verification before publication where needed.

Representative recurrence evidence, relative to each named run's
`calls/launches/<launch-id>/stdout.log`:

| Mechanism | Earlier occurrence | Occurrence beyond the fifth full run | Recovery evidence |
| --- | --- | --- | --- |
| Guessed source path aborts sequential reads and skips later intended reads | memexos runtime `f5b9b5261e474f308cfaa1fc6533a5ba:2016–2018`, nonexistent `intake/plugins.py`; EXIA runtime `c33bd5281d9a4aacb427cc26752e82e2:1038–1040` | v2 runtime `93197822fbf84e5883e4ce5914a7f88b:1390–1392`, nonexistent `agents/prompts/__init__.py` | v2 corrected prompt module plus both skipped store reads succeed at `1494,1498,1502` |
| Source quotation fails exact-source check, then must be replaced | newsroom runtime `05faad5806284c2aafa8850560121b82:9933`; llmwiki memory `2ca82bf241ea42af80898892992f6701:13240` | v2 boundary `dd680a9b4db7458a95b965f5fc2fb832:5748` | v2 replacement and reread followed by content-check pass at `6273` |

These observations support a repair question, not a proven root cause. A
candidate interface pressure is that convenient sequential read batches abort
on one guessed path; listing exact paths and isolating independent reads might
reduce collateral skipped work. Another is composing a plausible quotation
instead of copying a retained source span. Changing interfaces could introduce
extra calls, noise or incorrect source selection. The smallest next observation
is a bounded comparison using these retained incidents, preserving the same
source and acceptance checks; do not assume another instruction reminder will
prevent recurrence. Further live execution needs the operator's decision about
whether this worker-error recurrence should block an otherwise passing campaign.

### Final checks and coverage

- Six full analyses, six exit-0 publications and six completed advisory audits.
  All remain isolated and unintegrated. No live work remains owned by this pilot.
- Eighty role streams scanned; 42 failure leads, not 42 independent bugs.
  Nested tool/batch representations and expected `git diff` statuses are
  included. Zero partial/unscanned inputs or input issues, and no scanner
  provider/interruption/compaction observations. This is parser coverage,
  not proof that every shell operation was healthy.
- The six auditor Pi streams were separately scanned using
  `python3 scripts/scan_tools/scan_pi_tool_failures.py --format pi-json`:
  zero failure leads, observations or input issues. Audit reports and sampled
  original role events were inspected; not every successful call was audited.
- Fresh pinned-command inspection confirms published state with no unsettled
  role/audit launches or uncertainty. All 13 receipt-member hashes per system
  match retained bytes. Frozen source HEAD agrees with each saved audit revision.
- Complete unchanged controller JSON/stderr files, consolidated bindings and
  auditor scan are in ignored `.commonplace/worktrees/gist-live-tests/`;
  each controller and run
  retains original evidence. `summary.json` maps sources to every path.
- All six retained artifacts validated without warnings. KB documentation
  validation is separate from those run acceptance checks.
- No external source edits, integration, comparison rebuild, synthesis refresh
  or evidence removal. Existing comparisons remain unchanged; any earlier
  landscape synthesis is historical. No automation code patch or pytest rerun
  was necessary in this live phase.

## Integration request and recurrence diagnosis

The operator subsequently authorized integrating the six reports and checking
what can reduce the most common recurring failures. The first pinned integration
command, for MemexOS, refused with `integration requires a clean origin checkout`.
It stopped at the origin guard before publication staging or branch creation.
The origin has unrelated tracked theory/navigation/script edits and untracked
source ingests, discovery artifacts and tooling. Nothing was stashed, committed
or discarded to bypass the guard. Integration remains pending a clean origin or
explicit authority to temporarily set aside and restore the dirty work after
confirming writer coordination. No report has been integrated.

### Counting method

The 42 scanner findings collapse into **34 outer-call groups** by trace and
call ID, removing eight nested child/batch representations. This is operation
correlation, not a claim of 34 independent root causes. Original full results
were inspected for truncated diagnostic tails: one apparent search/no-match
candidate was actually `wc` on nonexistent `configuration.ts`. It belongs with
path discovery failures. The saved classification is local evidence at
`.commonplace/worktrees/gist-live-tests/incident-groups.json`.

| Mechanism | Outer calls | Systems | Evidence and practical implication |
| --- | ---: | ---: | --- |
| Source path discovery: guessed files or unmatched shell globs | 13 | 4 | Includes missing prompt, plugin, benchmark and config names. The preceding runtime search in MemexOS had already listed candidates, but its same script immediately used a prewritten guessed path. Listing alone is not prevention. |
| Quotation occurrence or block syntax | 6 | 5 | Two ambiguous short quotations, three absent/mutated quotations and one block whose literal `> ---` text collides with attribution parsing. |
| Record-citation label differs from its target ID | 6 | 3 | The Cortex profile verifier repeated the same label error on its next attempt despite being supplied and reading the records grammar. |
| Script construction/state | 4 | 3 | Two syntax failures, one undefined stored root and one failed exact replacement expectation. |
| Schema enum/duplicate-value error | 2 | 2 | Wrong status-field content and duplicate profile records. |
| Beyond-EOF continuation | 2 | 1 | Both already had equivalent complete reads; no unread source tail established. |
| Deliberate nonexistent-file probe | 1 | 1 | llmwiki's explicitly synthetic `cli-nonexistent.ts` probe; not accidental source discovery. |
| Expected diff status | 1 | 1 | `git diff --no-index` exit 1 means differences, not malfunction. |

One runtime validation call reports both citation-label and quote-block errors,
so category counts overlap once. There are 34 distinct call groups, not 35.
The two intentional/expected cases are not defects. No accepted-content defect
or measured degradation follows merely from the remaining failures.

### Recommendations, not implemented changes

The goal is to reduce failed authoring operations and their collateral skipped
reads while retaining exact-source grounding, canonical record references and
fresh semantic verification. No method or validator change is authorized by
this diagnosis alone, and no accepted report should be rewritten.

1. **Separate discovery from dependent reads; isolate independent reads.** Use
   an exact file inventory/search result to construct paths in a later tool
   step, instead of a precomputed read list in the same script that performs
   discovery. Use per-read settled results for genuinely independent reads,
   exposing every failure explicitly. This limits skipped collateral work; it
   does not turn a missing source into success. Existing tools suffice for a
   bounded trial; a new filesystem abstraction is not yet justified. The risk
   is extra round trips and losing the convenience of batching.
2. **Render quotations from selected source spans.** A read-only author-side
   helper could return the exact bytes, a checked range and a correctly parsed
   attribution, then round-trip through the existing parser/matcher before
   insertion. The author must still select the occurrence whose context supports
   the claim. Existing `quote_ambiguity_advice` already returns checked candidate
   ranges, so adding the same advice again after failure is not a useful fix.
   Literal source delimiters need a parser-compatible encoding or a documented
   quote grammar decision; they must not silently lose bytes. This would address
   mechanical quoting, not source truth or claim support.
3. **Generate canonical record links during drafting.** The full ID is already
   recoverable from a uniquely resolved member/anchor. An author-side formatter
   could emit the required `[ID](member#anchor)` form and show its diff before
   content validation. Fail on ambiguous/missing targets. This avoids asking
   the model to reproduce a redundant constrained label. Do not normalize frozen
   publications or silently relax the current record contract.
4. **Do not add bespoke machinery for the long tail yet.** EOF, enum, duplicate
   and short script mistakes recovered under existing checks. Prefer smaller
   scripts and explicit state; the sample does not justify another coordinator
   or a stronger-model migration.

The first practical test should use retained failure examples and unchanged
validators, measuring failed outer calls, collateral skipped reads, total calls
and any source-selection/claim-support regressions. Deterministic fixtures can
check span and link formatting, but cannot establish that workers will use them
or that live failure rates improve. Any bounded live comparison and production
implementation remains a separate decision. These six systems do not establish
a general failure rate, a causal effect of the interface, or the effectiveness
of any proposed repair.
