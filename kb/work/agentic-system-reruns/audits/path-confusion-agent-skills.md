# Path-confusion retrospective: Agent Skills epistemic draft

## Disposition

**Hold — locally reasonable analysis, not a substantive or validation pass.**
The retained implementation supports the main distinction between prescribed
source review and structural admission checks. Several direct findings are
well bounded. One doctrine claim strengthens a preference into a prohibition.
Other consequential implementation claims depend on supplied runtime findings
whose underlying source bodies are not retained here. The altered-path check
failed before member content validation. This audit neither releases the
owner's reservation nor judges a later publication.

Purpose: answer whether path confusion concealed an unreasonable draft, using
only the historical evidence authorized for this retrospective. Follow-up,
recovery and integration remain with the coordinator and reserved owner.

## Identity and evidence boundary

- Target: Agent Skills for Context Engineering.
- Run: `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01`.
- Attempt: `000008-epistemic`, candidate `outputs/report.md`.
- Frozen source declared by the historical boundary: SRC-1,
  `https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering`,
  commit `9ff0c99108b36d3b886defd825d8ac1f47dba374`.
  W24 retains a matching historical `git rev-parse HEAD` result; this audit
  did not independently inspect that checkout.
- Historical worker: `openai/gpt-6.1-sol`, medium (W24 and W46).
- Retrospective auditor: `openai/gpt-6.1-sol`, medium, as stated by this
  session's `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`.
- Method boundary: historical delivered instructions/types only (W3, W5,
  W7 and W20); no independent method commit inspection or certification.
- Workshop guidance: [validation-path maintenance](../validation-path-maintenance.md)
  and [audit a rerun](../audit-a-rerun.md). This commission narrows the latter
  to a historical candidate, not published output or legacy comparison.

Exact trace T:

```text
/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T13-59-16-666Z_01a13069-19ba-745a-b8d3-80c377c91314.jsonl
```

Every locator below is in T, JSONL line 31, message `5f3ae59f`.
Indexes are zero-based. C is `message.details.results[3]`.
W is `C.messages[25].details.results[1]`; Wn means `W.messages[n]`.
The complete delivered invocation is W3 `content[0].text`.
Candidate text is W42 `content[1].arguments.content`, with successful edits
W44/W45 and W50/W51 applied in memory for this assessment. The removed
unattributed sentence in W44 is not assessed as surviving content.
No current candidate bytes were read.

Source locators alone, file inventories, coverage assertions and analyst
paraphrases are not retained source text. Direct source read results below
are evidence; quotations inside supplied members are evidence only for their
quoted scope. No worktree, changing owner file, live source, download, target
execution or other run was accessed. No later trace or publication is covered.

## Substantive assessment against retained text

| Draft finding | Retained evidence | Assessment and limit |
| --- | --- | --- |
| Content curation prescribes evidence-consuming source admission, not proof of every proposition | W28 complete `researcher/rubrics/content-curation.md`; W29 complete `researcher/runbooks/autonomous-research-loop.md` | Reasonable. Four gates, weighted thresholds, dimension overrides, gate evidence, mechanism summary and limitations are explicit. Credibility and source suitability do not prove each mechanism true. D3=1 forcing review is correctly retained. |
| Retrieval can record manual retrieval without copied files; evaluation records rather than performs judgment | W36 `researcher/scripts/research_loop.py:276-347` | Reasonable for these bodies: `args.file or []` can be empty; the fallback says `manual retrieval recorded`; `mark_evaluated` copies asserted fields into queue/state. Helper behavior and full dispatch are not retained directly, so this does not independently certify the complete CLI. |
| Novelty is token-set overlap, not semantic novelty; selected accepted/candidate entries and corpus feed it | W26 complete `researcher/scripts/novelty_check.py`; W36 driver body | Supported. Selection, stopwords, Jaccard, rounding, thresholds and nonpass exit 2 are visible. The draft's alpha/beta/gamma deduction yields 1/3, rounded 0.3333, above 0.315, hence `likely_duplicate`. This is a code deduction, not an observed target run. Invalid JSON registry lines also enter the comparison as synthetic invalid entries; the summary should not imply that accepted/candidate entries are its only inputs. |
| Readiness checks status/shape, not rubric gates; ordinary promotion is conditional and overridable | W33 complete `researcher/scripts/validate_run.py`; W39 `researcher/scripts/research_loop.py:491-574` | Supported. Active evaluation checking requires asserted `retrieved` status and rejects explicit `REJECT`; it does not score gates. Only the first sorted nondraft evaluation is selected. Promotion checks readiness unless `allow_unready`, requires a nonempty reviewer string, and appends accepted/candidate records. No authentication or source-truth check appears in these bodies. |
| Closed runs select a closure-only branch | W33 and W39 | Supported with an important precision: state validation still runs first, and `validate_closure` returns without error when the closure file is absent. The candidate correctly describes the branch, but it must not imply that a closed state necessarily proves a closure record exists. |
| Revision comparison recommends by structural score and line-count tie-break, with semantic judgment external | W27 complete `researcher/scripts/compare_skill_revisions.py`; W40 complete `researcher/rubrics/pairwise-skill-revision.md` | Supported. The script prints/returns metrics and advice; it does not write or activate a winner. Rubric evidence fidelity is a separate obligation, not enforcement supplied by heading counts. Imported frontmatter-parser internals are not retained. |
| Review reminders select high-volatility claims by date string and write an advisory snapshot, not withdrawal | W34 `researcher/scripts/loop_daily.py:90-199`; W49 lines 1-32 | Supported for the inspected selector, renderer and daily body. Malformed JSON is skipped; dates are compared lexically; the snapshot consumer writes reminders and a count. This does not establish repository-wide absence of retraction or how the unretained CLI invokes daily processing. |
| Direct-score requests model evaluation and returns arithmetic; schema declaration is not parsing-time validation | W35 complete `examples/llm-as-judge-skills/src/tools/evaluation/direct-score.ts`; W38 complete `examples/llm-as-judge-skills/src/config/index.ts`; W50 candidate edit | Supported as a partial observation. `JSON.parse(result.text)` is followed by arithmetic, not output-schema parsing. Scores/summary are model-authored; input and output schema declarations alone do not authenticate evidence or score validity. Zero total weight, unexpected criterion names and arbitrary scores are not ruled out by the inspected arithmetic. The candidate does not claim those safeguards. |
| Deterministic scenario checking compares fixture/golden fields rather than executing the described scenario | W41 `researcher/scripts/run_benchmarks.py:1-142`; W50 edit | Supported for `evaluate_scenarios`. The harness also launches repo/activation validators, explicitly acknowledged by the candidate; their internals are not retained. This finding must not become a claim that the whole benchmark harness performs only field comparison. |

### Overstatement and contradictions

1. **Conflict rule is overstated in EPI-CLM-evidence-review.** The candidate
   says the runbook calls for “no published change while conflicting sources
   remain unresolved.” W29 says:

   > Record both claims and prefer no published change until resolved

   A preference is not an unconditional prohibition. The same draft later
   uses “conflicts should defer publication,” which is closer to the source.
   Narrow the claim to the prescribed preference; do not infer interception.

2. **A reading-completeness claim is too literal.** Coverage calls the
   benchmark body a complete direct read. W41 reports one remaining line
   after line 142, and there is no recovery read in W. All consequential
   displayed functions, including the main guard, are retained, so this is
   not evidence of a hidden substantive contradiction. It is not an exact
   whole-file read claim either. W34/W49 are deliberately partial daily reads,
   and the draft appropriately limits their coverage.

3. **Validation attribution is contradicted, not the main analytical thesis.**
   W54's problem write claims execution “exactly as supplied.” W3 versus
   W52 disproves that statement. Returning `problem` and admitting no pass
   are honest about the failed outcome, but the claimed producer defect and
   request for a corrected invocation are unsupported.

No contradiction to the central review-versus-structural-check distinction
was found in the retained direct source bodies. That is a local result,
not a verdict on every ledger row or the whole system.

### Grounding gaps in inherited route claims

W13/W15/W17 contain the supplied runtime member, not the underlying source
read history of its author. Their quotations support narrow premises:
router equality/top-three scoring; a declared unwired effectiveness executor;
freeze declared/actual surface comparison; export allowed-field copying;
callback dispatch; best-prompt successor assignment; a `system` request
field; and governance's default-deny return/design declaration. These are
useful evidence, but they do not retain the full bodies needed to independently
assess all the epistemic draft's derived classifications.

In particular, this audit cannot independently establish from retained text:

- Description-only router prompt construction and complete resume-key/hash
  behavior. A source path and supplied explanation are not the prompt/scan code.
- All candidate-freeze identity/digest checks, materialization cleanup and
  export source binding, staging scans and receipt-failure cleanup. The few
  supplied quotations establish narrower operations, not whole route contracts.
- Governance deny precedence, complete decision inputs, or absence of
  interception across research writes/CI. Default-deny alone does not prove
  deny precedence or mandatory mediation.
- The optimizer's complete score/stopping/rewrite/next-round path, analyzer
  tool-result truncation, optimizer's partial analyzer-thinking input, or
  absence of an independent task-success gate. Supplied callback/system-field
  and best-prompt quotations are consistent with the analysis, but do not
  prove these full routes. Reflection, self-change and theory-builder
  conclusions are therefore inherited assessments, not independently checked
  findings in this retrospective.

The candidate visibly distinguishes direct reads from supplied findings and
leaves observed operation, improvement and broad system negatives unestablished.
Those qualifications make it substantially more reasonable than an unqualified
system-wide indictment. They do not turn the missing bodies into evidence.

## Validation actually performed

W3 supplies the executable and candidate path under worktree
`agent-skills-for-context-engineering-2423c2f20f83`, and the artifact argument:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/agent-skills-for-context-engineering-2423c2f20f83/kb/agentic-system-analyses/state/AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01/artifact
```

W52 preserves the executable, candidate and `--role epistemic`, but changes
`--artifact` to:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/agent-skills-for-context-engineering-2423c2f20f83-01/artifact
```

The paired call/result is W52/W53, exact tool-call ID:

```text
call_HJkZasq3srhJVwSck7Vu0ii5|fc_0f71b3e42b964d52016acceeeb18ac87d2b1a36d03369e21b9
```

W53 reports missing `ARTIFACT.yaml` at the altered location and
`Command exited with code 2`. There is no supplied-path call or passing result
in W's 57 retained messages. W54 `content[1].arguments.content` writes the
problem; W55 confirms the write; W56 returns `problem`.

This establishes an attempted invocation and manifest-loading failure, not
member content checking. It leaves the draft's schema/frontmatter, tables,
controlled ledger values, record links/relations and quotation occurrence
unchecked against the intended artifact. It also leaves any content findings
and required repairs unknown. Even a successful content check would not prove
claim support, invocation-residue compliance or job acceptance. No historical
revalidation was performed here.

## Procedural compliance, separately

The worker read the complete invocation, job instruction and member type;
recovered the runtime tail (W14/W15 and W16/W17); inspected direct source
bodies; wrote a candidate and successful edits; wrote empty answers and runtime
identity (W46-W48); and returned a problem rather than a pass. The trace shows
no target execution or delegation by this worker.

The validation obligation was not fulfilled: the literal supplied command was
altered, and no successful repair is retained. W20 also requires supplied
absolute input/output/patch paths; the worker used relative paths in many read,
write and edit calls (for example W2, W42, W44 and W50). Successful delivery and
writes do not erase that procedural deviation. W23 uses a semicolon-separated
command sequence and an `rg | head` pipeline without the required pipefail;
its successful output is not certification of every inner status. These are
additional local compliance findings, not claims that source content was
wrong or that prohibited prior material was exposed.

The missing final benchmark line is a minor read-completeness limit, not proof
of consequential source loss. This is not an exhaustive compliance audit.

## What would decide the hold

For substantive certification beyond these local findings, owner-coordinated
access must first supply an immutable copy at the declared commit, not permission
to inspect changing worktree files. The exact missing evidence is:

- `examples/interleaved-thinking/reasoning_trace_optimizer/loop.py`,
  `capture.py`, `analyzer.py`, `optimizer.py`: complete control/evaluator/consumer
  bodies for the optimizer qualifications and property conclusions.
- `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `common.ts` and
  `runEffectiveness.ts`: prompt construction, selection/scoring, resume and
  scaffold bodies for the router license and remaining scope.
- `researcher/scripts/artifact_store.py`, `export_policy.py`,
  `validate_export.py`: freeze/materialization and export check/cleanup bodies.
- `researcher/scripts/governance_policy.py`, `governance/constitution.yaml`,
  `governance/README.md`, `.github/workflows/validate.yml`, and the complete
  `researcher/scripts/research_loop.py`: decision rules, callers, CLI dispatch
  and mediation boundary. The retained retrieval/promotion slices do not
  substitute for that full comparison.
- Any proposed claim of *observed* operation or improvement would separately
  require attributable target-native run evidence or a causal comparison;
  this candidate does not make such a claim.

Owner coordination would also need to freeze the intended candidate and
artifact/member context, preserve their identity against W42 plus W44/W50,
resolve the overstated conflict rule, and arrange the literal W3 content check
with a paired complete result. That work belongs to the owner/coordinator;
this report authorizes none of it. A later successful check cannot retroactively
make W52 literal or W54 accurate.

Until then: **reasonable on the directly retained mechanisms; inherited claims
only partially grounded; no deterministic content pass; procedure not fully
compliant; hold rather than integration clearance.**
