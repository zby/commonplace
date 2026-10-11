# Napkin repeat analysis and trace audit

## Outcome

Both runs preserve the central supported account: local file retention, explicit retrieval, host-interpreted curation and no demonstrated learning benefit. Both publications match their accepted bytes. The new run is not a clean resolution of the old audit findings. It explicitly handles successful-result-only benchmark averages and avoids the old exposure-evaluator correction cycle. It improves the retained-results account but leaves an evidence-strength inconsistency in the profile. The distill path mismatch remains unreported. Documented automatic context delivery is still not characterized at its documented strength; the new profile instead explicitly narrows its scope.

The revised omission procedure is visible in the new verification, including selected questions, bounded source searches, dispositions and a stopping rationale. Its local limits preserve supported claims rather than asserting exhaustive coverage. This is evidence of procedure uptake, not proof of better detection or lower cost. The new run used fewer workers and tool calls but took longer, including longer summed worker spans.

Audit date: 2026-10-11. This is a static, post-run audit under [Audit an analysis](../audit-an-analysis.md). The [old audit](napkin-analysis-and-trace-audit.md) and [coverage-policy comparison](../../analysis-lenses/coverage-policy-comparison.md) supplied hypotheses, not accepted findings. No target execution, engine invocation, source/method/run-state change, integration, commit or delegation was performed. Only this report was authored; the workshop README was intentionally left unchanged under the commission.

## Identities and evidence locators

```yaml
reporter-profile:
  harness: pi
  model: openai/gpt-6-astra
  reasoning-effort: medium
  basis: PI_CODING_AGENT, PI_PROVIDER, PI_MODEL, PI_REASONING_LEVEL
new:
  run-id: AAS-2026-10-11-napkin-1b60c5d21780-01
  method-commit: 0275b8abb307039d0bc975b5699e5b86fe6ca1d5
  source-revision: 7582d6a46f5a11995956e60a59c41a5b242109f1
  audited-profile:
    profile: pi-sol
    harness: pi
    launch-model: gpt-6.1-sol
    model: openai/gpt-6.1-sol
    reasoning-effort: medium
old:
  run-id: AAS-2026-10-10-napkin-b831630d0978-01
  method-commit: 6ff7c828e94dd66abdf5af00c89db6420bc6a1ad
  source-revision: 7582d6a46f5a11995956e60a59c41a5b242109f1
  audited-profile:
    profile: pi-sol
    harness: pi
    launch-model: gpt-6.1-sol
    model: openai/gpt-6.1-sol
    reasoning-effort: medium
source-identity: https://github.com/Michaelliv/napkin
```

Abbreviations used for exact local anchors:

- `N/`: `/home/zby/llm/commonplace/.commonplace/worktrees/napkin-1b60c5d21780/`.
- `O/`: `/home/zby/llm/commonplace/.commonplace/worktrees/napkin-b831630d0978/`.
- `A/` within either worktree: `kb/agentic-system-analyses/retained/napkin/`.
- `R/` within either worktree: `kb/agentic-system-analyses/state/<that worktree's exact run-id>/`.
- `S/` within either worktree: `related-systems/Michaelliv--napkin/`.
- `TN`: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T11-36-19-469Z_01a12abf-dd0d-7274-939c-cb2daf375a55.jsonl`.
- `TO`: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-10T22-10-09-558Z_01a127dd-cc16-745a-b8d3-80ae1386ab9d.jsonl`.

Trace `L` is the 1-based JSONL line; `r` is the 0-based `message.details.results` index; `m` is the 0-based embedded `messages` index. Omitted `r` means zero. Original analytical messages survive in these arrays even where handouts have been cleaned up. Later audit workers in TO are not original analysis workers and are excluded from counts.

The opening metadata, both `A/overview.md:15` fields, publication receipts and preparations agree on method identity. Both source checkout HEADs equal the revision above, and both source `git status --porcelain` checks were empty. The old opening and publication receipt have `source-revision: null`: that was the optional requested revision, not a missing evidence pin. Its acquired source and `O/A/boundary.md:14,57` establish the resolved revision. The new opening explicitly requested the same revision.

Both manifests' `worker` mappings, model attempts' `worker_model`/`worker_effort`, and the original workers' environment outputs support the audited profile. For example, TN L19 m12–13 and TO L18 m12–13 report `openai`, `gpt-6.1-sol`, `medium`. These are distinct from this reporter's runtime.

### Method correspondence

The plan SHA-256 is identical in both `R/run.json` files: `9062207fdc5fecf8ffd5e697924c52228125fd7c0a73d3e7c0ebcfa03cfac6a2`. The commit diff under `kb/agentic-system-analyses/` changes only the shared worker rules, report-verifier instruction and verification type. No plan, schema or engine change appears in that boundary. Other repository differences include workshop/audit/navigation material and a general review instruction; the whole checkout is not a three-file-only diff.

Independently compared the new report-verifier attempt's pinned bytes to both the committed blobs and its worktree files. All match:

| `N/R/state/attempts/000017-report-verification.json` pin | SHA-256 |
|---|---|
| `instruction` | `41163de951b29115cfad318fa1f3baf7b36a94ee730dbb93b2d91397145490b2` |
| `worker-rules` | `c57fb05c4c065384ee49d47f1d2d626a757da382d9ca108cc5d108e3b3880e35` |
| `member-type` | `6ea2cb1ca1f41e26bbe835f6d20ac30f74627d962454b0e304de98308761432e` |

TN L35 m4, m6 and m43 load those governing documents. Thus the new policy was actually delivered, not merely present in the checkout.

### Publication-byte correspondence

For **each run**, independently hashed all eleven retained Markdown members and compared them with the manifest, publication-receipt hashes, matching `R/state/versions/<hash>` bytes and working `R/artifact/<member>` bytes. All eleven match in all comparisons. The retained manifest also matches its version blob and receipt hash. This covers twelve published files per run, not merely an engine success message.

Exact receipt locators:

- New: `N/R/state/attempts/000028-publish.json`, output receipt version `d77c0cbe0b87f898c4f7a15904559b3ba636ba5a6888dd455537f8f3f707d71c`; manifest hash `93f48f81cd77153ab6582749bc7c460832d9766c80374cb83ecce83ac3739cf6`.
- Old: `O/R/state/attempts/000037-publish.json`, output receipt version `12095aea60d2d7eea2d7eb6e67b8ce1442fc2fef73832c087e09b73a64dc84b0`; manifest hash `ea72efe30f92f18bab94d62bab8f3b9ed70f0803cd6d03a5ee7cc7c948d500f1`.

The working artifact's minimal `ARTIFACT.yaml` is not the assembled publication manifest; comparing those two directly would create a false discrepancy. Byte correspondence establishes publication integrity, not semantic correctness.

## Independent claim comparison

### C1 — Old N1: distill instruction/API mismatch remains a material qualification

`S/skills/distill/SKILL.md:79–86` tells the agent to rewrite by name and create using `--path "<folder>"`. But `S/src/core/crud.ts:46–55` treats a supplied path as the whole filename, adds `.md` if necessary and ignores the title. CLI forwarding does not combine folder and title (`S/src/main.ts:230–241`, `S/src/commands/crud.ts:57`). A title `Connection Pooling` with path `guides` therefore targets `guides.md`, not `guides/Connection Pooling.md`. Name-only overwrite also does not perform read-style nested basename resolution.

Old `O/A/runtime.md:35,107` describes the instructed route without this mismatch. New `N/A/runtime.md:28,154–170`, `N/A/memory.md:252–260` and `N/A/synthesis.md:20` still describe the intended search/merge/create progression without it. The new account is explicitly policy-level, so omission is **not** proof that it falsely claims successful execution. Nevertheless, its mechanism account should say literal skill adherence may not produce the intended placement or rewrite. Neither run observed an actual failed distillation.

Disposition: retain the old source-level finding, with this distinction between incomplete operating conditions and a false observed-success claim. Local medium-priority qualification; no demonstrated central-characterization failure.

### C2 — Old N2: substantially improved read-back account, residual profile overstatement

The source confirms two different outputs: current-run `allResults` and saved JSONL/JSON. LongMemEval pushes a returned object and separately writes it at `S/bench/longmemeval-eval.ts:628–632`; aggregates consume the array at `661–694`. LoCoMo does the same at `439–445,454–495`. Those spans do not reload the saved files.

Old `O/A/memory.md:180`, `epistemic.md:307` and `memory-profile.md:613–624` attach aggregation/read-back or wired informational authority to the retained-results account. The old audit's objection is supported.

New `N/A/memory-profile.md:345–353` explicitly makes later human review **afforded**, and excludes current-run aggregation from accumulated read-back. `N/A/memory.md:175–185,315` also limits future external consumption. This is a real improvement, not just omission of a disputed field.

However, `N/A/memory-profile.md:161–169` groups **report text** with note/canvas/bookmark readers under one `knowledge`, `basis: wired` finding, citing the retained-results object. Its own later-review classification is only afforded. `N/A/memory.md:282` and `synthesis.md:44` still use wording that can make retained reports inherit the aggregation consumer. The profile type at `N/kb/agentic-system-analyses/types/agentic-system-memory-profile.md:56–59,107` requires the actual retained part and consumer; one wired witness cannot upgrade another alternative.

Disposition: local medium-priority correction remains. Separate the result-file consumer and evidence strength from immediate reporting. Keep the supported wired knowledge findings for actual reload/read paths. The new profile verifier's acceptance at `N/A/profile-verification.md:16,18,21` does not resolve this inconsistency. No external consumer absence is asserted.

### C3 — Old N3: scope narrowing replaces uncertainty, not the documented delivery account

`S/docs/distill.md:11–24,44,75,79–82` supplies more than an always-loaded label: a timer checks for new entries, assembles a prompt from retained `NAPKIN.md` and templates, and calls a separate model. This establishes a **documented** automatic supply mechanism, not implemented or observed operation. The old profile's statement that documented consumers do not specify automatic selection (`O/A/memory-profile.md:915–975`) misses those details.

New `N/A/runtime.md:290–298` retains a timed external design claim. But the retained context/template objects still omit its specific consumption chain. New `N/A/memory-profile.md:9,315–365,423` explicitly excludes independent external injection, changes direction to `known` pull and signal to `inapplicable`; `profile-verification.md:18` endorses that scope. These local pull findings are not, by themselves, false claims that no external push exists. Nor are they evidence that N3 was repaired. The old and new axes have different coverage and cannot be treated as improved certainty over the same inventory.

There is a boundary-consistency question: `N/A/boundary.md:44` expressly includes the document as declared design, while missing **implementation** is used to exclude that later-consumer alternative from the memory profile. The profile type requires scope agreement with records and forbids dropping opaque included alternatives merely to obtain `known` (`:73–95`). The warranted distinction is documented mechanism versus uninspected wiring, not missing documentation.

Disposition: retain a local coverage/scope recommendation. Characterize the documented timer/new-entry/context/template chain in analyst records and either classify it at documented strength or explain an authorized functional exclusion consistently. Do not silently upgrade it to wired delivery, and do not count the narrower pull-only scope as a detection success.

### C4 — Old N4: default-search condition is still useful

`S/src/utils/files.ts:28–54` skips encountered trash directories but starts directly at a caller-selected folder. `S/src/core/search.ts:53,160–165,234` passes the selected path into enumeration/fingerprinting. Consequently, folder-scoped search at `.trash` can discover deleted Markdown; exact-path read is not the sole remaining access route.

Both accounts qualify with “ordinary” or “normal” enumeration. New examples are `N/A/memory.md:61,300`, `runtime.md:142` and `synthesis.md:36`; old examples are `O/A/memory.md:75,310`. These can reasonably mean default vault-wide discovery, so I do not promote them to a claim of universal search exclusion. The missing explicit `--path .trash` condition is a low-priority precision improvement in both runs, not evidence of secure-deletion promises. Both reject secure or historical rollback guarantees.

### C5 — Old N5: narrower new wording reduces the problem

`S/src/utils/vault.ts:91–94` creates empty `NAPKIN.md` only when absent. Old `O/A/runtime.md:18` says discovery creates an empty file without that condition. New `N/A/runtime.md:16` says a nominal read/search **can** create an empty file when no vault is found. That modal statement is supported; it does not say an existing note is erased. New `runtime.md:30` also says existing scaffold files are preserved, although that is a different path.

Disposition: do not count N5 as an unchanged falsehood in the new run. Adding “if absent” would remove residual ambiguity cheaply. Constructor side effects remain a supported finding in both accounts.

### C6 — Old N6: explicitly resolved in the new epistemic account

Old `O/A/epistemic.md:82,302–307` describes null/error results but not their exclusion from denominators. New `N/A/epistemic.md:75,253–254` explicitly says null questions do not enter successful-result averages and retains the `if (result)` passage at `268–274`. The source array/mean branches cited in C2 independently support this.

This is a substantive added qualification. It does not establish that any published score was biased: raw attempts, failure rates and correlation with difficulty remain unknown. The public synthesis need not enumerate every scoring qualification to remain a bounded summary.

### C7 — Old repaired evaluator issue: repair preserved, now present before verification

`S/bench/overview-exposure.ts:22` passes two strings to `loadSearchCorpus`; `S/src/core/search.ts:160–165` expects/destructures `VaultInfo`. Both final runs correctly separate present metric formulas from an established viable invocation. The target was not executed; neither an observed crash nor repaired target code follows.

Independently checked the old inner history: TO L30 m40 preserves the memory/epistemic conflict; L34 m63 blocks publication; L38 m41 repairs the epistemic account; L46 m67 accepts the correction. New runtime already records the mismatch at `N/A/runtime.md:68–80`; its original draft in TN L23 precedes report verification. New epistemic `:75–76,279–294`, reconciliation's “Exposure evaluator” paragraph and synthesis `:46` retain it. No new semantic refusal/retry was needed for this issue. This is convergence on a correct final qualification, not causal evidence that the revised verifier discovered it earlier.

### Other comparison changes

The new reports separate distill from tend and distinguish release-test prerequisites from direct npm update. They explicitly distinguish template substitution from CRUD/daily copying, and carry a base-calculation limit. These are more explicit record organization and qualifications, not necessarily newly discovered mechanisms: the old runtime/memory already covered many of the same alternate consumers and cache/confinement conditions.

The verifier adds the older promotion/summarization doctrine as a **limit**, not an executable route (`N/A/report-verification.md:42–59`). `S/docs/agent-memory-progressive-disclosure.md:99–118` does assert a distill command and proposes access-driven promotion; current dispatch searches do not corroborate that command. The new synthesis carries this inventory limit rather than declaring promotion absent. This is a supported example of limiting completeness without erasing the main account. It does not establish complete doctrine coverage or settle every template/formula behavior.

## Does the revised verification procedure appear?

**Question selection: yes.** `N/A/report-verification.md:40` names five consequential question families: alternate admission/recovery paths; independent context/scheduling; cached/probed exposure; scores feeding revision; auxiliary/formula consumers. It states a search basis in tree, dispatch and producer/consumer paths. TN L35 m47–50 inventories the tree/files; m81–88 searches and reads additional doctrine; m97–110 inspects evaluator, base, overview, graph and prompt ranges; m111–112 checks dispatch and reporting. These are actual source operations, not only retrospective boilerplate.

**Stopping: a bounded rationale is present; a measured effort trade-off is not.** `N/A/report-verification.md:50,58–59` stops after named dispositions and explains why unread formula branches, dependency internals and external behavior do not defeat local persistence/retrieval and policy claims. The retained text does not quantify expected search cost or show a particular claim narrowed because retaining its breadth was too costly. It demonstrates selective stopping compatible with the revision, not a demonstrated optimization. The trace supplies no controlled counterfactual about how long the old procedure would have searched.

**Brief reporting: yes for omission accounting.** The question paragraph, doctrine example and stop paragraph replace a read-by-read coverage ledger. The whole report remains substantial: approximately 1,322 whitespace-delimited words versus 1,337 in the old final verification (Markdown syntax included). New report-verifier direct source reads rise to 49, versus 11 in the old first pass and 13 in its second. A short retained account did not mean fewer source reads.

**Correctness preservation: mixed, not waived.** The formula/doctrine limits leave supported bounded claims true, and the exposure mismatch remains correctly qualified. There is no evidence that workers dropped a supported finding merely to pass validation or save effort. But the selected questions did not surface C1 or fully separate C2's consumers, and C3's documented delivery remains outside the comparison. A no-blocker verdict is not proof of complete correctness. Question selection and ordinary model variability remain plausible explanations; this pair cannot identify a method effect.

## Failure-oriented trace audit

Inspected all ten new and thirteen old original analytical worker traces for tool calls/results, nonzero/hidden statuses, truncation and continuations, writes/edits, validation and recovery. All 23 enclosing results report exit code 0, normal `stop` and empty stderr. Those envelopes conceal internal history; they do not mean every operation succeeded.

### T1 — Recurrent quotation failures, all recovered

New boundary fails twice: TN L19 m67, m71. Its first attempted attribution reordering at m68 does not repair the missing revision syntax. It searches/reads Commonplace's parser at m72–75, adds revision-bearing attributions at m76, and passes at m79. New epistemic fails at TN L27 r1 m73, adds attribution revisions at m74, and passes at m77. These are three failed validation invocations, not three failed workers.

Old boundary fails at TO L18 m93 and passes at m101 after repair. Old epistemic fails at L26 r1 m64 for attribution and m68 for an ambiguous quote, then passes at m72. Thus three validation failures recur across the two runs, with different local repair details. Inspection of the repairs found attribution/context fixes, not claim removal to satisfy the checker.

Each run has 17 worker validation invocations: 14 passes, three failures. New memory (TN L27 r0 m74–77) and profile verification (L45 m51–54) repeat a successful check with explicit status handling. New runtime adds supporting quotations after an initial pass (L23 m71); new epistemic expands object/ledger distinctions after a pass (L27 r1 m78), then revalidates. In particular it separates deterministic matching, model judging and token metrics rather than retaining one homogeneous derivation claim. A current pass does not imply no earlier repair or no subsequent edit.

### T2 — Old masked command failure; new status-risk patterns but no demonstrated masked failure

TO L22 m16–17 requests nonexistent `src/utils/file.ts` in `wc`. The output prints the error and `exit=1`, but a successful final `printf` leaves the Bash tool result successful. The correct `src/utils/files.ts` is read at m23; the source-access need is recovered, though the inventory command is not successfully rerun. This independently confirms the old audit's masked-failure mechanism.

New runtime TN L23 m15 and report verification L35 m47, m49, m81, m111, m119 still use semicolon/final-printf patterns that do not forward all underlying failure statuses. In particular the final verifier validation would mask a nonzero validator exit at the tool level, but m120 actually contains a content pass and `exit=0`. No new masked failed command, failed pipeline, missing source path or unhandled command-not-found event was found in the ten traces. Status-risk noncompliance is distinct from an observed failed operation. The shared rule already requires status preservation; this is not evidence of a missing instruction.

### T3 — Truncation and completeness

The old memory search at TO L26 r0 m50 is genuinely tail-truncated: 109 lines were omitted by the 50 KB delivery limit. Its narrower SDK query at m51–52 recovers the affected navigation. No new Bash output with an actual delivery-truncation marker was found.

For required supplied-input reads, the new workers generally follow the printed chunks through completion. New synthesis TN L49 m28 leaves an advertised one-line continuation at memory offset 332; the accepted file has 331 physical lines and the omitted logical remainder is empty EOF content. Old profile verification TO L54 m27 and m31 similarly leave blank EOF continuations. These are not demonstrated substantive reading gaps. Ordinary bounded target-source reads with “more lines” are not failures to read an entire file unless the worker needed or claimed complete coverage. This audit did not certify every source-coverage assertion.

The old verifier's requested ranges exceeding source EOF are still visible in TO L46 m49/m54 and its authored log m67. They describe requests, not exact delivered coverage. The new verifier no longer emits that per-read ledger; absence of the old logging defect does not prove perfect source coverage.

### T4 — Authority and source isolation

No explicit analytical-worker writes outside assigned outputs/identity/scratch, target execution, network call, nested delegation, Git publication or prior-analysis read was found. Old profile generation runs only its authored scratch generator (TO L50 m43–54); it is not Napkin execution. Old epistemic copies its supplied previous report to its assigned output (TO L38 m39–40), then edits it. New profile/synthesis verification and reconciliation do not read target sources, matching their record-based roles.

Some workers use worktree-relative spellings of absolute method-input paths despite the shared preference for supplied absolute paths. Invocation output/input artifact paths themselves were supplied relatively (for example TN L19 m3), so relative writes there are not evidence of reconstructed unauthorized destinations. No wrong-file consequence was found. The coordinator reads publication instructions at TN L36–37 before the final publication advance. Analytical trace scans found no prior-audit exposure; they cannot establish an absence of model pretraining knowledge or unrecorded activity.

## Timing and costs

These measurements cover original analysis only, not the previous audits or this audit. Wall time uses coordinator `start` result through the advance result reporting publication; worker spans use last minus first timestamp in each embedded worker message array. Those spans include tool/model waiting, are not CPU time, and omit some launch/final-return envelope overhead. Memory and epistemic overlap. Neither wall time nor summed spans is a standalone measure of analytical effort.

| Measure | Old | New |
|---|---:|---:|
| Start result → publication | 22:10:58.225–22:49:35.927 UTC, Oct 10 | 11:37:00.634–12:26:22.805 UTC, Oct 11 |
| Wall duration | 2,317.702 s (38m 37.7s) | 2,962.171 s (49m 22.2s) |
| Summed embedded worker spans | 2,420.020 s (40m 20.0s) | 3,198.127 s (53m 18.1s) |
| Analytical workers / embedded messages | 13 / 836 | 10 / 713 |
| Tool calls | 505 | 437 |
| Reads / Bash / writes / edits | 419 / 47 / 33 / 6 | 364 / 40 / 27 / 6 |
| Direct source read calls | 172 | 177 |
| Harness model turns | 305 | 256 |
| Input / cache-read / output tokens | 991,770 / 12,145,408 / 93,797 | 898,558 / 11,779,072 / 91,959 |
| Harness-reported worker cost | $4.1360508 | $3.8946132 |

Wall anchors: TO L14/L66; TN L15/L55. Preparation and diagnostic launch are excluded. Commission-to-publication spans are 2,341.313 s old and 2,998.241 s new. Publication is not integration into the main checkout.

All analytical trace locations and spans:

| Role/attempt | Old trace; seconds | New trace; seconds |
|---|---|---|
| `000003-boundary` | TO L18; 201.385 | TN L19; 265.343 |
| `000005-runtime` | TO L22; 219.664 | TN L23; 404.779 |
| `000007-memory` | TO L26 r0; 318.850 | TN L27 r0; 450.195 |
| `000008-epistemic` | TO L26 r1; 364.039 | TN L27 r1; 613.871 |
| `000014-reconciliation` | TO L30; 119.515 | TN L31; 196.409 |
| `000017-report-verification` | TO L34; 156.436 | TN L35; 341.650 |
| Epistemic repair `000019` | TO L38; 102.828 | none |
| Reconciliation repeat `000023` | TO L42; 111.539 | none |
| Report-verification repeat `000026` | TO L46; 159.400 | none |
| Memory profile | TO L50 (`000028`); 245.535 | TN L41 (`000019`); 352.059 |
| Profile verification | TO L54 (`000030`); 131.282 | TN L45 (`000021`); 179.975 |
| Synthesis | TO L60 (`000032`); 163.922 | TN L49 (`000023`); 229.885 |
| Synthesis verification | TO L64 (`000034`); 125.625 | TN L53 (`000025`); 163.961 |

### Recovery costs and interpretation

- Old semantic repair plus required reconciliation/reverification accounts for **373.767 summed worker-seconds and $0.762344** across TO L38/L42/L46. This is successful safeguarding cost, not three independent errors. It excludes the initial verification that found the blocker and coordinator gaps.
- Within-worker quotation-recovery windows, measured from first failed validation result to first successful result, are **22.269 s boundary + 56.122 s epistemic = 78.391 s old**, versus **43.781 + 56.743 = 100.524 s new**. The intermediate failure windows overlap and must not be added again. These windows include reasoning/edit/tool wait, not just validator runtime; per-repair token costs were not isolated.
- The new epistemic post-pass ledger/object refinement is additional self-review, not an engine-requested repair. The trace supports its occurrence, but I do not assign the whole worker span to repair. Masked-inventory and truncation recovery costs were not separately isolated.
- New wall time is about **27.8% longer**, summed spans **32.2% longer**, while reported cost is about **5.8% lower** and tool calls **13.5% lower**. Removing the old repair cycle did not make this new run faster. Even the new report verifier's 341.650 s exceeds both old report-verifier spans combined, 315.836 s, although their scopes differ.

Concurrent-run confounds are directly visible. Pi sessions `2026-10-11T11-25-10-443Z_01a12ab5-a7aa-745a-b8d3-80b050b39d2c.jsonl` and `2026-10-11T11-36-42-623Z_01a12ac0-377f-75ee-95ac-d2493cc60647.jsonl` in the same session directory commission Graphiti and Letta Code at L5, overlapping this run's period. No provider queue, host-load or rate-limit telemetry was measured. Old concurrency was not exhaustively reconstructed. The same profile and source pin do not control scheduling, model variability, chosen coverage, output organization or service latency. The new source-read count is slightly higher, and its report verifier does substantially more source reading. This is not causal proof of method benefit or harm.

## Local corrections versus method conclusions

### Local recommendations, requiring separate authorization

1. **Split retained-result consumer evidence** in the new profile and clarify the remaining aggregation wording (C2). Expected benefit: prevent saved files inheriting current-run authority. Small bounded record/profile correction; no new target execution needed. A concrete inspected saved-file reload consumer would change this recommendation.
2. **Qualify the distill path contract** (C1). Explain folder-versus-filename and nested rewrite behavior, without inventing an observed failure. Cost: a small cross-path qualification carried into the relevant account; a different forwarding path that actually combines folder and name would rebut it.
3. **Resolve documented-delivery scope consistently** (C3). Preserve timer/new-entry/context/template details at documented strength and distinguish them from missing implementation. Cost: analyst-record and dependent-profile work, not just adding a caveat to a complete axis. An authorized exclusion of that documented responsibility would change the needed comparison scope, not prove delivery absent.
4. **Prefer default-vault-wide withdrawal and absent-file wording** (C4–C5). Low-cost precision improvements. Do not exaggerate these into data-erasure or universal-search claims that the reports do not make.

These are correction recommendations for frozen results, not edits performed by this audit. A correction must use the separately authorized retained-analysis process; do not mutate these publications in place.

### Method conclusions

Retain this as mixed repeat-run evidence. The new prose procedure is delivered and used; supported limits and a short omission account are visible. Recurrent quotation repair and fragile shell status handling remain observations about execution of existing rules. The old semantic repair loop worked, and the new run reached the same evaluator qualification earlier without that loop. The surviving qualifications show that asking consequential questions does not guarantee selecting every material condition.

No additional method change is justified causally by this pair. Before any broader change, compare these mechanisms across further commissioned cases and adjudicate C2/C3's local effects. An added exhaustive checklist would have a real reading/reporting cost; these traces do not show that it would outperform selective questions. Conversely, the observed selective stopping does not justify weakening ordinary correctness checks.

## Coverage and remaining unknowns

All original analytical worker traces were failure-scanned, including all commands/results and mutation destinations; all publication members were byte-checked. Correctness inspection concentrated on actual old/new claims for N1–N6, the repaired evaluator, the new omission account, dependent profile/synthesis wording and the supporting frozen source branches. It was not an independent reanalysis of every Napkin feature, every formula branch, dependency, quote or benchmark. Read-call counts measure calls, not unique source coverage or comprehension. No deployed distillation, retrieval quality, published-score bias, external result consumer, or causal method effect was established.

The report's deterministic validation result is recorded in the audit completion response. A validation pass establishes this report's form and links, not the truth of its judgments.
