# Dynamic Cheatsheet worker instruction comparison — 2026-10-10

## Result and retention purpose

The latest run showed partial improvement, not a demonstrated overall quality gain. It produced stronger counterexamples and more precise classifications, but lost a correction that the previous run had preserved. Broader documented verification did not consistently catch more errors.

This is a dated record of the read-only comparison requested after the latest run. Commonplace analysis-method evaluation consumes this report when assessing the worker-instruction changes in commit `935b19194e9687d0ac7cb5b92ae5c9f28916eee9`. It is not a new external-system analysis, an amendment to either accepted analysis, or evidence that the instructions caused the differences. Preserve this observation; record later comparisons separately.

## Inputs and audit method

### Previous run

```yaml
run-id: AAS-2026-10-10-dynamic-cheatsheet-41e85fccfcaf-01
method-commit: 1a20deff31df32a332835974cf1a61d3b58fc8a6
source-revision: 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9
```

### Latest run

```yaml
run-id: AAS-2026-10-10-dynamic-cheatsheet-004374829a63-01
method-commit: 935b19194e9687d0ac7cb5b92ae5c9f28916eee9
source-revision: 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9
```

Both runs used worker profile `pi-sol`, recorded worker model `openai/gpt-6.1-sol`, and medium effort. Both frozen source checkouts were clean at the same revision. Source identity: `https://github.com/suzgunmirac/dynamic-cheatsheet`.

The audit compared the method diff and retained reports, then spot-checked consequential differences against the frozen source. Two fresh Commonplace workers split the comparison: runtime, memory and report verification; epistemic analysis, synthesis, overview and synthesis verification. They were instructed to work read-only, inspect changed claims against source, distinguish accuracy from detail, and return improvements, regressions and remaining defects with line references. The coordinator reviewed their findings and the two syntheses. No target code or provider calls were executed, and no analysis workflow was rerun.

Audit coordinator model: `gpt-6-astra`. Audit workers inherited the coordinator's model and effort under the Pi launch contract; this audit did not separately record resolved worker identities or effort. The user instruction was: “check if the last run improved over the previous one (we have added some instructions to the workers)”.

For the locators below, **old** and **new** mean the corresponding run's `kb/agentic-system-analyses/retained/dynamic-cheatsheet/` directory. **Source** means paths within the pinned external repository. These locators identify audit inputs, not live links or prerequisites for reading this report. The worktrees were `.commonplace/worktrees/dynamic-cheatsheet-41e85fccfcaf/` and `.commonplace/worktrees/dynamic-cheatsheet-004374829a63/`; their paths are local context, not run identities. The essential evidence is retained below.

## Instruction changes assessed

The substantive method commit added four requirements:

1. Runtime, memory and epistemic analysts should seek a source-supported case that would falsify a consequential claim, then correct or qualify it.
2. Report verification should independently trace behavior, checking conditions, scope, ordering and evidence strength rather than relying on analyst checks.
3. Reports should distinguish uninspected evidence from unavailable evidence, implemented requests from model compliance, and supplied historical traces from independently authenticated execution or causal benefit.
4. Synthesis should preserve material conditions and evidence limits.

The intervening commit `2c728337f` also added target-confirmation instructions. That intake change is not the worker-analysis intervention assessed here.

## Improvements

### Falsifying examples made evaluator limits concrete

The new epistemic report identifies source-supported cases that defeat broad correctness claims:

- Multiple-choice substring matching can accept `not water` when the target option text is `water`.
- Game of 24 can accept `2**3+8+8` for inputs `2 3 8 8`, although exponentiation is outside the stated operations.
- Equation balancing can accept `1+2+3=999` against target `1+2+3=6` because it ignores the submitted right-hand side.

These are deductions from the predicates, not observed benchmark failures. The new synthesis retains the limitations. The old report described the predicates but supplied less decisive counterexamples.

Audit locators: new `epistemic.md:265–267`, `synthesis.md:38`; old `epistemic.md:362–377`; source `dynamic_cheatsheet/utils/evaluation.py:47–81,151–170,258–262`.

### The implemented correctness request received a better classification

The old epistemic report called curator assessment “doctrine only” and classified it as “claimed”, despite acknowledging that the instructions reach the model. The new report calls it an implemented assessment request while withholding actual checking, compliance and an evidence-consuming acceptance decision.

The inspected path substitutes the question, answer and prior sheet into the curator template, calls the model, then extracts and installs the replacement. That establishes delivery of the request, not successful checking. The new status better fits this mechanism; much of the distinction already appeared in the old prose.

Audit locators: old `epistemic.md:88–105,419–433`; new `epistemic.md:166–186`; source `prompts/curator_prompt_for_dc_cumulative.txt:18–24` and `dynamic_cheatsheet/language_model.py:423–435`.

### A consequential template condition reached the synthesis

The new synthesis notes that omitting the CLI curator-template option supplies literal `(empty)`. It passes the API's non-null test without supplying the intended curation instructions. The correctness policy therefore depends on an appropriate template, not merely selecting cumulative mode. The old synthesis did not preserve this qualification.

Audit locators: new `synthesis.md:20`; old `synthesis.md:18–20`; source `run_benchmark.py:95–100` and `dynamic_cheatsheet/language_model.py:386–390,423–430`.

### Verification became easier to audit, but not demonstrably more effective

The new report verifier provides a table of source ranges and the ambiguities checked. The old verifier reports one additional source read to resolve recovery. This is improved documentation of the claimed verification process. The table is not independent authentication of tool use, and the recovery regression below shows that more reported reading did not ensure better checking.

Audit locators: new `report-verification.md:14,22–33`; old `report-verification.md:40`.

## Regression: a previously caught recovery defect was accepted

The frozen recovery implementation is:

```python
last_cheatsheet = outputs[-1].get("final_cheatsheet")
if last_cheatsheet is not None:
    cheatsheet = last_cheatsheet
```

Only the final saved record is tested. If its sheet is `None`, initialization survives. There is no backward search for an earlier non-null sheet. Source locator: `run_benchmark.py:185–187`.

The old runtime used ambiguous “last non-None sheet” wording. The old memory analyst and report verifier caught it. The old synthesis explicitly retained the correction:

> If that field is None, initialization remains unchanged; no backward search recovers an older sheet.

The new runtime and memory reports say “last non-null sheet”. The new synthesis says:

> Resume restores the last sheet and prior final outputs and skips examples by saved-record count.

The new report verifier found no material correction necessary, and synthesis verification accepted the checkpoint account without the old limitation. Correct final-record wording remains elsewhere in the new reports, making the account internally inconsistent rather than uniformly wrong. The old public synthesis was nevertheless more accurate.

This is the strongest adverse observation for the intervention: a consequential condition was lost, and independent verification did not recover it.

Audit locators: old `runtime.md:182`, `memory.md:88,200`, `report-verification.md:40,48`, `synthesis.md:28,48`; new `runtime.md:191,198`, `memory.md:79,172`, `synthesis.md:24`, `report-verification.md:56–68`, `synthesis-verification.md:20,40–46`.

## Reduced inspection and an unresolved evidence-use gap

### Actual saved content became uninspected

The old run inspected a saved mathematical sheet and retained concrete claims from it. The new run left result payloads uninspected and withheld assessment of actual formulated content. This is honest reporting of reduced inspection, not stronger evidence or broader coverage.

The audit found that the first record of `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` contains stored target `315`, generated and final answer `15`, and a successor sheet retaining the rectangle-count claim `15`. This supports the bounded observation that a supplied record retains guidance inconsistent with its stored target. It does not authenticate execution or establish that the target is correct.

Neither run fully develops that counterexample. The old run notices the content but not the target mismatch; the new run drops the content inspection.

Audit locators: old `epistemic.md:326–333`, `synthesis.md:36–38`; new `epistemic.md:34,186`, `synthesis.md:44`; source result file, line 1.

### Supplied traces still lack a bounded observation

The notebook calls the model again on the same input with an updated sheet. Its saved output includes “From the cheatsheet” and “Implement the algorithm from the cheatsheet”, followed by implementation text, execution-output text and another sheet update. A sheet count changes from 2 to 3.

The warranted observation is narrow: a supplied historical trace depicts explicit reference to, and implementation of, retained guidance followed by another update. It does not independently authenticate execution, establish hidden reasoning dependence, validate the count, or show improved efficiency or transfer. Repeating the same problem with its solution already available is not a controlled benefit comparison.

The new instructions permit this middle evidence category, but the new report leaves notebook output content unassessed. Both runs underuse this evidence.

Audit locators: new `epistemic.md:32`, `synthesis.md:14,44–46`; source `ExampleUsage.ipynb:390–530`.

## Assessment and limits

| Intended effect | Observed result |
|---|---|
| Seek source-supported counterexamples | Improved evaluator examples |
| Distinguish implemented requests from compliance | Improved classification |
| Preserve consequential conditions | Mixed; template improvement and recovery regression |
| Independently catch inaccurate claims | No demonstrated improvement; a previously caught ambiguity passed |
| Use supplied traces with bounded evidence strength | Still a gap |

The audit recommendation was to retain the instruction changes as plausible improvements, but not cite this run as evidence of overall analytical improvement. Further evaluation should test whether workers preserve the final-record recovery condition and extract bounded observations from supplied traces, rather than count statements about verification.

This is one before/after pair, without replication, blinding or a prespecified scoring rubric. Matching source revision and worker configuration reduces obvious confounds but does not isolate the instruction effect from model variation. The audit spot-checked consequential claims; it did not exhaustively compare every record or the structured memory profiles. It did not independently authenticate either run's source execution or audit worker tool traces. No broad conclusion about reliability, performance or benefit follows from workflow completion or the documented inspection inventory.

This report retains the comparison evidence, not the full run directories. Its creation does not authorize integration, source or retained-analysis edits, or worktree removal.
