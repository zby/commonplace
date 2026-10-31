# Revised experimental proposals

**Deferred background:** the operator selected an [observational watch](./README.md) as the next step. These designs are retained for later use if the case records justify a controlled study; they are not an execution plan or authorization.

Status: designs only, 2026-10-31. No trials, infrastructure, or formal preregistration were performed. If a controlled study is later authorized, Experiments 1 and 2 are the initial candidates; other studies depend on their results.

## What changed after reading the literature

The [initial framing](./initial-experimental-framing.md) separated relevance and utility. The literature adds four requirements. Semantic similarity must not be used as a substitute for false relations (E1). Compute must be varied within a checkpoint, since model-family comparisons and longer thinking can point in different directions (E3). Layout must be separated from conceptual organization (E5, E8). A fresh-context comparison and a false-criticism control are necessary to distinguish correction from persistence or acquiescence (E4, E7, E13). E10 makes the benefit of separation an empirical question.

A fifth refinement comes from the conceptual analysis: epistemic relevance is not the same as constitutive inclusion. B may be useful as a contrast or counterexample without belonging inside A's definition.

## Experiment 1 — Does utility alter conceptual relationships?

### Micro-world and intervention

Construct families of short fictional domains with stipulated predicates. For example, an artifact receives certification A exactly when property p holds; capability B is determined independently by q. Include all four p/q combinations among available examples so independence can be checked. The primary question asks what A requires and how to classify new cases.

Both A and B contribute to a broader project. Change only B's stipulated project payoff between matched high and low conditions. Keep the certification rule, cases, vocabulary, wording length, information position, and task request fixed. Keep both payoffs positive and investigation cost below both, so low utility does not automatically mean worthless. Randomize which named property carries which payoff to remove label effects.

In the primary setting, the secondary opportunity is available without explicitly instructing the model to separate it. A parallel unambiguous-scope setting states that project priorities cannot redefine certification. This distinguishes pragmatic expansion from violations of a fixed local task. Include a no-project-goal control.

### Controls

Include cases where B genuinely is a defining condition, where it is evidence relevant to A without being a component, where both instantiate a justified higher-level mechanism, and where their relation is genuinely unknown. Do not equate all high-relevance cases with valid inclusion. Use shared-benefit versus equally valuable distinct-benefit versions to test whether a common endpoint is especially influential.

Independently vary lexical relatedness and familiar terminology in later variants. Use neutral numerical payoffs, not praise, as the main utility manipulation. Measure whether an agent understood the payoff in separate probes that do not cue the original answer. Synthetic cases secure labels; independently adjudicated natural cases test transfer and avoid mistaking an easy logic benchmark for ordinary conceptual research.

### Outcomes

The primary estimand is the high-minus-low utility difference in **false constitutive or explanatory relation rate**, conditional on worlds where that relation is false. Report effect sizes and uncertainty, not only significance. Also measure primary accuracy, secondary opportunity recognition, retention, and false rejection of justified unification.

Score first responses before administering probes. Use blinded human relation labels and mechanically checkable classifications or counterfactual predictions. Examples: if p holds but q does not, does the agent withhold A? Does it design a test of A that unnecessarily requires q? Separate prose-only misplacement from a relation that changes behavior. Do not rely on a global LLM-judge quality score or headings.

Final omission cannot distinguish failure to notice from failure to retain. Stage-separated outputs can support that distinction, but eliciting intermediate outputs is itself an intervention; report its effect rather than assuming it reveals an untouched process.

### Interpretation

A utility effect at fixed semantic relations supports goal-conditioned distortion. An effect limited to ambiguous tasks favors pragmatic reinterpretation. An effect of lexical relatedness without utility supports associative influence. No utility effect with tight confidence bounds weakens the distinctive hypothesis for the tested domains; it does not prove its absence in long open-ended work. Correct retention of B with stable relations is a successful outcome, not an error for being off-topic.

## Experiment 2 — Does correction replace the organizing relation?

Use both naturally occurring false integrations and standardized seeded flawed explanations. Randomize the correction intervention after the erroneous answer. Report these strata separately: conditioning on self-generated errors can select unusually difficult examples, while externally seeded errors may not behave like the model's own commitments.

Compare: no feedback; generic request to reconsider; a true counterexample; a false criticism of a correct boundary; and a fresh context containing the same task facts and true criticism but not the earlier explanation. Control context length with irrelevant neutral text rather than leaving length as an explanation. An own-versus-external prior-answer comparison must hold content fixed and acknowledge role-attribution differences.

Score four distinct outcomes: acknowledgment; removal or qualification of the false relation; correct held-out consequences; and maintenance of the repair in a subsequent related task. A sentence conceding that A and B differ is insufficient when the operative classification still requires both.

A larger restart benefit after explicit evidence supports trajectory dependence. Revisions that remove a heading but leave false predictions unchanged support superficial repair. Acceptance of false criticism indicates that apparent correction may be deference. Successful correction followed by transfer weakens claims of intractable framing persistence.

## Experiment 3 — Is the proposed remedy better than its alternatives?

Compare neutral explanation, requested unified account, and permitted multiple threads. Cross these with tight and generous output budgets, keeping available facts and total computation fixed where possible. Include a compact relation statement as an alternative to separate long sections.

Evaluate false integration together with missed warranted synthesis, missed secondary opportunities, task success, and capture/execution cost. Allow capture without immediate execution. Separation only wins if its overall tradeoff improves; fewer blends accompanied by systematic fragmentation is not success.

Vary inference effort within the same checkpoint and hold visible answer budget fixed. Separately compare more continuation with a fresh independent attempt at comparable total cost. Do not interpret longer outputs as more hidden computation or a reasoning-model/non-reasoning-model contrast as a clean compute manipulation.

## Experiment 4 — Which training or selection stage matters?

Begin with matched pretrained, supervised, and preference-optimized checkpoints from the same lineage, using appropriate native prompting formats and competence/compliance controls. These comparisons locate a change but can still bundle multiple modifications.

A more discriminating preference test uses a frozen answer set crossing correctness of relationships with rhetorical unity, formatting, and length. Include correct higher-level syntheses, correct separate accounts, false syntheses, and false fragmented answers. Otherwise a preference for good prose or lists could be mistaken for a reward for unification.

A causal claim about a particular training objective requires training runs from a common starting checkpoint with controlled data and randomized objective variants. Such work is outside the present authorization. Neither an instruction-tuned/base contrast nor a reward-model ranking alone demonstrates that RL caused the deployed policy's behavior.

## Experiment 5 — Does an unsupported relation propagate?

Provide downstream investigators with matched retained artifacts: correct separate threads; an unsupported relation connecting the same facts; an omitted secondary opportunity; a justified synthesis; and an explicitly tentative common-mechanism conjecture. Hold the underlying evidence, task budget, and handoff length approximately fixed.

Measure subsequent hypothesis choice, discriminating-test selection, interpretation of counterevidence, and final relational accuracy. Include independent evidence that can reject the false relation. Track whether the later agent treats source organization as evidential authority, not merely whether it quotes the prior text.

The key comparison is downstream decisions under the false relation versus the same facts without it. Propagation is not shown by repeating a phrase. Correction, harmless non-use, and beneficial abstraction are legitimate negative results.

## Sampling, scoring, and preregistration boundary

The independent unit is a micro-world or independently authored natural case, not each sampled completion. Cluster repeated samples by world and model; vary templates and labels, blind scorers, record disagreements, and report per-family results. Determine sample sizes from a pilot variance estimate and a minimum meaningful effect, not a convenient arbitrary benchmark size.

Freeze world truths and admissible relations before running models. Use incorrect-unification and incorrect-separation controls to detect one-sided scoring. Keep all results, including nulls and correct unifications. Preserve exact prompts, model/checkpoint identifiers, dates, budgets, outputs, annotations, and exclusions through existing Commonplace procedures. The current document is not itself a claim that this future study has been preregistered on the main branch.
