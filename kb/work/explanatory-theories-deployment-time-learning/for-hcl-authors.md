# Invitation: test an explicit theory intermediate in HCL

> **Status:** Exploratory note from the Commonplace project. We have not contacted the HCL authors, and no response or endorsement is implied. The proposed treatment is ours; HCL does not claim or test it.

Harness Continual Learning (HCL) makes three useful mechanisms explicit around a frozen model. An optimizer proposes isolated harness changes, an evaluator can reject them, and atomic commitment makes an accepted state operative in later tasks. HCL's controlled benchmark streams are not deployment-time learning, but these mechanisms offer a concrete substrate for studying how evidence becomes a governed behavioral change. Our [HCL reading](./hcl-reading.md) separates that contribution from the proposed extension. The [source analysis](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) records the supporting evidence.

## One extension: require a working theory before proposal

HCL's optimizer turns an outcome and execution context into component choices and candidate edits. The paper neither exposes nor tests a separately represented theory between that evidence and those decisions. Abstract Memory stores summarized, scoped guidance, but the evidence does not establish it as a premise-bearing theory or show that it mediates candidate search.

We propose that HCL add one intermediate artifact. Before generating candidates, the optimizer records a working theory `tau_n` that explains the observed behavior through a mechanism, invariant, or other explanatory relation. The theory states its premises, scope, expected consequences, and a possible falsifier. The optimizer must then use those consequences to choose an intervention point and generate or prioritize candidates.

The artifact matters only if it changes the decision path. Researchers must record it before candidate generation and before revealing evaluator-only outcomes. This order rules out a purely post hoc rationale. HCL's Abstract Memory should not be relabeled `T_n`; a retained, revisable theory would be a later and stronger treatment with its own acceptance decision.

## One discriminating experiment

First, test candidate search while leaving HCL's evaluator intact. Hold the model, task evidence, editable surface, candidate count, total resource budget, and hidden full evaluator fixed. Compare three arms:

1. direct proposal from the available evidence, with no required theory artifact;
2. a deliberation-matched control that produces a structured plan but need not state an explanatory mechanism or falsifiable consequences; and
3. the `tau_n` treatment above.

Freeze the intermediate artifact and candidate ordering before applying the same independent evaluator to every candidate. Use the best admissible candidate found within budget as the primary endpoint. Report total cost, current benefit, and historical regressions. A gain over direct proposal alone could reflect extra deliberation; a gain over the matched control would more specifically support the explicit-theory requirement.

To distinguish mediation from narration, withhold or alter a load-bearing premise in a preregistered subset. Intervention-point choices or candidate ordering should change in the predicted direction. If the recorded theory changes without the predicted change in search, the evidence does not establish the artifact as an operative intermediate. The broader [experiment design](./experiment-design.md) gives the protocol and later stages. Selective evaluation should remain outside this first contrast.

## Questions for the HCL authors

- Does the current optimizer produce a diagnosis or rationale not exposed in the paper, and does any later optimizer call retrieve it?
- Where in the optimizer would a prerecorded theory be least likely to leak evaluator-only information or merely restate the chosen edit?
- Which HCL tasks present several plausible intervention points and enough hidden evaluation coverage to discriminate search quality?
- Would the three-arm comparison preserve the resource and proposal constraints that matter in HCL? Which cost should be matched most tightly?
- What result would persuade you that an explicit theory adds no useful constraint beyond ordinary optimizer deliberation?
- If the within-episode treatment worked, what failure mode would you test before allowing a retained theory to influence later tasks?

We welcome corrections to our reading of HCL and criticism of this experimental contrast, especially if an existing optimizer mechanism already supplies the proposed intermediate or makes it impossible to isolate.
