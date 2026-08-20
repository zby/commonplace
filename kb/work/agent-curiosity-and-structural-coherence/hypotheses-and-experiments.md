# Hypotheses and experiments

## Status

Everything in this file is provisional. The purpose of the decomposition is to make rival accounts predict different traces and intervention effects, not to replace “taste” with a longer untested vocabulary or to infer a shared cause from similar code and prose symptoms.

## A candidate process model

A structure-relevant observation can pass through at least nine transitions:

```text
global artifact model
  -> local unit and role assignment
  -> role mismatch registration
  -> significance / interruption
  -> structural or epistemic subgoal
  -> explanatory and global search
  -> redesign candidates
  -> evaluation and selection
  -> edit and plan update
```

A final artifact can bypass or leave that path at several different boundaries:

```text
locally conditioned proposal -> emitted without a global role comparison
locally adequate result      -> controller stops before structural review
candidate set                -> explicit local oracle selects the accommodation
```

These paths are not automatically irrational. Most units that compile, pass tests, follow from the previous sentence, or elaborate the current topic are serviceable. But proposal conditioning, controller stopping, and explicit candidate selection are different mechanisms and require different interventions. Reserve **oracle** for a criterion actually applied to an artifact; infer weak selection only when candidate generation and evaluation can be observed separately. The proposed failure occurs somewhere before a wider model can show that the unit has the wrong owner, duplicates an already-filled role, changes the artifact's center of gravity, or should be moved or removed.

Failures at different positions can yield the same final artifact. “The agent added another branch” or “the agent added a transition sentence” does not reveal whether it lacked a global expectation, never assigned the unit an argumentative role, noticed but dismissed the mismatch, generated only local candidates, or generated a structural alternative that lost to the smaller edit.

## Curiosity can react to or construct a possible anomaly

The chain above begins with a structure-relevant observation. It captures **reactive curiosity**: an encountered unit is compared with an expectation, a mismatch becomes significant, and investigation follows. It omits a second route in which the agent actively generates a possible counterexample before anything has presented itself as odd.

```text
reactive route:
observed unit -> expected role -> mismatch -> significance -> probe -> update

prospective route:
structural rule or claimed invariant
  -> consequence if false here
  -> artifact-grounded boundary cue
  -> conjectured failure case
  -> discriminating probe
  -> rule / artifact / plan / uncertainty update
```

The working label **prospective boundary probing** describes this operation without proposing a durable kind of curiosity yet. Within this workshop, a useful probe concerns an ownership, section-role, argument-structure, or decomposition rule and says why its failure would change the artifact's organization, what in this case makes failure plausible, and what observation would discriminate failure from compliance. Merely producing many “what if?” questions is not the target; curiosity without significance and evidence can become unbounded search or rhetorical decoration. General scientific hypothesis generation and factual or stakeholder-completeness review require a separate evidence base unless they directly expose this structural transition.

The author's apparent starting perspective is one possible source of hypotheses, but it must be operationalized without mind-reading. Observable cues include cases sampled from only one side of a declared partition, assumptions treated asymmetrically, a case absent despite being required by a stated scope or independently warranted coverage model, or a rule extrapolated beyond the conditions that motivated it. Such a cue raises a question; it is not evidence of intent and is not proof that the rule fails.

The two routes converge on an epistemic subgoal and a probe, but they expose different early failures. An agent may competently investigate a stated oddity yet never originate “does this rule hold here?” It may originate the question but fail to prioritize it, propose a check that cannot distinguish the alternatives, or obtain an answer without updating the artifact or plan.

### Paper doubt and living doubt are distinguishable outcomes

Use **paper doubt** as a working label for a concern that can be stated but does not alter what could reject the incumbent. A generic critique, a list of possible weaknesses, or a familiar benchmark objection remains paper doubt when it supplies no material consequence, discriminating probe, or uptake. Use **living doubt** for the stronger observed sequence: the concern earns scarce investigation effort, produces or selects a check whose outcomes distinguish compliance from failure, and changes the rule's scope, artifact, plan, or calibrated uncertainty.

This is not a new stage in the process model. It groups outcomes across the existing significance, subgoal, probe, and uptake stages. It also avoids treating fluent concern production as reasoning evaluation: [reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) predicts that a model may reconstruct the expected objection while failing to assess the incumbent process. Likewise, [known-target discovery benchmarks show reachability, not discovery closure](../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): supplying or recognizing the expected concern is a capability ceiling, not evidence of prospective origination.

A direct experimental contrast can hold the artifact and budget fixed:

- **Concern-production condition:** ask for important uncertainties or structural concerns.
- **Consequence condition:** additionally require the organizational consequence if each concern is true.
- **Probe condition:** additionally require a check with outcomes that discriminate failure from compliance.
- **Uptake condition:** supply the same blinded probe result and test whether it changes the artifact, plan, rule scope, or uncertainty.

Score paper-doubt yield separately from living-doubt completion. Include rule-holds and tempting-false-lead controls so indiscriminate investigation cannot win by producing more concerns. The useful dependent variable is not rhetorical force but the fraction of warranted concerns that traverse the full sequence at acceptable investigation cost.

## Curiosity, taste, representation, and selection

A working distinction:

- **Taste** supplies expectations and rankings: what coherent responsibility or argumentative placement looks like, which small awkwardness predicts later cost, and which of several locally acceptable artifacts is preferable.
- **A global artifact model** makes the relevant expectation available now: ownership and dependency structure for code; thesis, section purpose, and argument roles for prose.
- **Curiosity** is a question-generation and control policy: which encountered mismatch deserves interruption; where a consequential rule may be worth stress-testing before a mismatch is visible; how long the question remains active; and when its answer must change the plan.
- **A structural operator repertoire** produces relocation, consolidation, deletion, extraction, or reframing candidates instead of only additions near the observed site.
- **The operative oracle** decides which candidate survives.

On this account curiosity would be causally upstream of a redesign being pursued, while taste and representation would be epistemically upstream of both surprise and candidate ranking. Taste can supply the rule, the consequential boundary, and the ranking; prospective curiosity spends search on the possibility that the rule fails in this case. Taste without that search may support excellent answers to supplied critiques without originating them. Curiosity without taste or significance may spray low-value questions. None is simply “more fundamental.” Without an expectation there may be no anomaly; without a global representation the expectation may not be applied; without interruption the anomaly does not alter the agenda; without structural search inquiry still yields local accommodation; without a discriminating oracle the stronger candidate loses.

This decomposition shows which parts the current Curiosity Pass does not implement or test. It explicitly allocates attention after the artifact exists; it does not create a continuous anomaly trigger, a prospective rule-boundary search, a global role model, persistent question state, investigation budget, structural-candidate generator, or plan-revision rule. Whether adding those parts improves outcomes is an empirical question for the timing and intervention experiments.

## Five local-admissibility conjectures

The brainstorm's candidate mechanism splits into five falsifiable accounts:

1. **Locally conditioned proposal conjecture:** the model proposes the next patch or sentence from immediate context without constructing or retrieving a global role model. There is no represented mismatch to suppress.
2. **Premature-stopping conjecture:** the proposal is locally adequate, so the controller never initiates a whole-artifact review. This is a control-loop boundary, not candidate selection.
3. **Locally masked anomaly conjecture:** a structural concern is explicit in the trace but disappears from the agenda after tests turn green or a local prose accommodation reads smoothly.
4. **Structural-candidate generation conjecture:** the mismatch is diagnosed and remains live, but self-generated remedies are additions; move, merge, delete, fold, and reframe do not enter the set.
5. **Selection conjecture:** both local and structural candidates exist, but an explicit judge favors test success, readability, preservation, or smaller edit radius over the global role criterion.

Their traces differ. The first predicts no usable role model; the second predicts no global review despite a completed local result; the third requires evidence that a concern appeared and then disappeared; the fourth requires a persistent diagnosis and a candidate set without structural operations; the fifth requires a frozen set containing both kinds and a local candidate winning. Silence alone cannot distinguish them.

A possible software trajectory is:

1. A failing test or requested behavior creates immediate pressure.
2. A shim, branch, wrapper, duplicated path, or flag has low edit radius and a clear route to green tests.
3. Moving or deleting machinery requires a broader responsibility model, negative knowledge about what can disappear, and a riskier diff.
4. Tests supply a stopping signal; only some harnesses then run a separate comparison among designs.
5. Either no ownership anomaly is formed, structural review never begins, an already stated concern loses priority, no structural alternative is generated, or a structural alternative loses selection.
6. The next task inherits the old structure and the accommodation, making another addition attractive.

A possible prose trajectory is:

1. A sentence or paragraph is plausible, relevant to the topic, and easy to continue from.
2. Deciding whether it belongs requires a representation of the document's claim, each section's job, and which argumentative roles are already filled.
3. The agent instead adds a bridge, caveat, distinction, or new heading that explains the local adjacency.
4. The passage now reads more smoothly. That may condition the next proposal or stop further review without any explicit candidate-ranking event.
5. The next revision inherits both the unit and its accommodation, so further qualifications or repetition become easier than deletion or relocation.

The prose path is not “green tests in another form.” Continuation fluency is graded and implicit, and a bridge can genuinely repair some passages. The experiment must distinguish a bridge that supplies a missing inferential relation from one that merely disguises a role mismatch.

Only the final branch directly instantiates [weak oracle discrimination](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md): local and structural candidates both exist, then a weak global criterion underselects the structural one. The earlier branches concern proposal, representation, or control. Context limitations, preservation priors, edit risk, backward-compatibility requirements, or a genuinely defensible alternative structure could generate the same artifact.

## Three strengths of cross-domain claim

The user's transfer intuition should be tested at three distinct strengths:

1. **Behavioral homology:** code and prose show the same observable transition failure under matched role-violation tasks.
2. **Intervention transfer:** one representation-agnostic procedure — model global roles, keep mismatches open, generate move/merge/delete alternatives — improves both domains, or an intervention demonstrated in one domain improves the other without domain-specific restatement.
3. **Shared learned origin:** the same training pressure or internal faculty causes both behaviors.

The first is accessible with black-box experiments. The second needs careful prompt-transfer or practice designs and neutral controls. Neither establishes the third; a training-origin claim would need training interventions, model comparisons with known objective differences, or strong mechanistic evidence. The workshop should not turn behavioral analogy into a claim about what faculty was trained.

## Where the analogy must remain domain-specific

- **Local signals and checks:** code has tests, types, and runtime behavior; prose has truth, grammar, referential integrity, and immediate transition quality.
- **Global evaluation:** code can use explicit responsibility rules and later edit radius; prose needs section contracts, argument dependencies, reader tasks, and calibrated editorial judgment.
- **Role uniqueness:** code ownership is sometimes exclusive, while one sentence can legitimately perform several discourse jobs. Human preferred placement is not ground truth.
- **Move semantics:** relocating code can preserve behavior; relocating a sentence can change scope, implicature, anaphora, and premise salience.
- **Risk:** code moves risk regressions and broad diffs. Prose moves are often cheaper, but cross-references and anaphora can make them risky; that difference is itself an experimental manipulation.
- **Legitimate redundancy:** [local materialization](../../notes/local-materialization-should-outperform-distant-declarations.md) is conjectured to improve uptake over declaration-only presentation for distant or non-obvious uses. The common target is role conflict, not locality, repetition, or addition in themselves.

## Structural subgoal origination is not one capability

The cases suggest a rough spectrum:

1. **Entailed operational subgoals** — inspect a file, rewrite a sentence, edit a function, run a test.
2. **Diagnostic subgoals after visible failure** — localize a failing assertion, contradiction, or malformed sentence.
3. **Preventive epistemic subgoals** — investigate a duplicated responsibility or paragraph that reads well but has no clear role.
4. **Structural reframing subgoals** — ask whether the current decomposition, sectioning, thesis, or stated problem is wrong.
5. **Open-ended problem selection** — decide which latent strain deserves work under a fuzzy objective.

Issue-and-test benchmarks supply the result of level 5 and therefore bypass autonomous problem selection; they often narrow or bypass level 4 as well. The issue selects the problem and the tests define a success boundary. Sentence-level editing similarly supplies the target span and defect class. Success shows reachability of a known target, not autonomous origination of the structural concern.

Level 3 can be reactive or prospective. In the prospective form, the agent starts from a rule and the cost of its possible failure, identifies why this case may be near the rule's boundary, and creates a counterexample-seeking subgoal before a visible defect exists.

## Rival hypotheses and discriminating predictions

| Hypothesis | Prediction | Intervention that should help |
|---|---|---|
| Missing structural knowledge or “taste” | The model still fails to diagnose or rank the structural option when the global model and alternatives are explicitly shown | Better model, domain examples, expert design or argument schema |
| Missing global representation | Local judgments are competent, but explicit ownership or section-role maps sharply improve diagnosis | Repository map, thesis-and-section map, argument graph, change history |
| Local proposal conditioning | The initial output hugs adjacent code or sentences, but a separate whole-artifact review finds the role conflict | Separate proposal from review; require role assignment before continuation |
| Premature controller stopping | A locally successful edit ends the task before any global review is called | Mandatory post-local structural check; independent review budget |
| Activation / mismatch-registration failure | Naming the oddity improves diagnosis without supplying the solution | Anomaly cue, counterexample, role-comparison question |
| Significance / curiosity failure | The oddity is mentioned but does not interrupt or create a subgoal | Mandatory question generation, inquiry budget, unresolved-anomaly register |
| Prospective question-origination failure | The agent can evaluate “does this structural rule hold here?” when supplied but does not generate the question from an available rule, material stakes, and a non-conclusive boundary cue | Consequence-first counterexample search; explicit rule-boundary scan |
| Question-discrimination failure | The agent produces numerous generic doubts without artifact evidence, material consequences, or checks that distinguish the alternatives | Require rule, consequence, observable cue, and discriminating observation; rank probes under a fixed inquiry budget |
| Structural candidate-generation failure | Diagnosis is good, but self-generated remedies remain local; a supplied move/delete/merge candidate is preferred | Multi-plan search, explicit structural operators, architecture or argument sketch |
| Selection / oracle failure | A frozen set contains local and structural candidates, but a readability- or test-focused judge selects the local one | Re-rank the identical set under future-change or document-role criteria |
| Context / comprehension failure | All conditions improve when relevant ownership, thesis, and dependency material fits in context | Selective context routing, artifact synopsis, larger-context control |
| Scope, preservation, or edit-risk pressure | The agent identifies the redesign but labels it out of scope or avoids the destructive/larger edit | Permission to widen scope, frozen backup, reversible candidate, explicit deletion permission |
| Different domain mechanisms | Under matched stages, global-role representation closes the prose gap but not the code gap, while identical-set re-ranking closes the code gap but not the prose gap | Model a domain × stage interaction; reject one shared stage bottleneck |

## Experiment discipline

Use fixed model partitions and snapshots, repeated trials, blinded outcome scoring, neutral-cue controls, balanced candidate ordering, and uncertainty intervals. Human baselines need the same visible context and a declared time budget. A vivid single trace is a case lead, not an intervention result.

## Experiments

### 1. Admit role-grounded prose fixtures

Start from the exact [prose fixture candidates](./prose-fixture-candidates.md). For each target, freeze the thesis, section-purpose map, argument dependencies, local window, reference edit, and defensible alternatives before an experimental agent sees the case. Use independent panels:

- a local panel sees the unit and neighbors without headings and must judge it coherent and topically connected;
- a global panel sees the whole note and role map and must agree that the unit duplicates, competes with, or belongs outside its present role; and
- neither panel is told the historical edit.

Each admitted hard case needs an obviously unrelated intrusion control, a locally and globally correct control, and a **genuine bridge-repair** case where adding a transition supplies a missing inference and is the correct operation. Reject low-agreement fixtures. A historical human edit furnishes a candidate, not ground truth.

### 2. Run a stage-separated prose ladder

Keep note, model, context, budget, edit permission, and reversible backup constant. Do not change representation, candidate supply, and oracle inside one opaque call. Run and score separate stages:

1. **Open online work:** give a nearby editing task that can finish without touching the target. Cross strict edit scope with an otherwise identical condition that explicitly permits logging noteworthy structural concerns in a separate report without widening the edit. Silence under strict scope alone is proper scope obedience, not evidence of failed curiosity.
2. **Open retrospective review:** ask for defects without supplying a role model or target.
3. **Representation and diagnosis:** compare a model-generated section-role map, a neutral outline, and a supplied role map. Audit supplied maps for leaking the desired operation or location.
4. **Candidate generation:** after freezing one diagnosis, ask for candidate edits with or without an explicit add/move/merge/fold/delete/reframe repertoire. Freeze all outputs before evaluation.
5. **Candidate selection:** give the **identical randomized candidate set** to separate judges using local readability, global role, and blinded whole-document criteria. This is the only stage that directly tests oracle discrimination.
6. **Execution ceiling:** supply the selected operation and destination, then test whether the agent can preserve claims, anaphora, scope, and local coherence.

Run a human baseline under the same visible context and time budget. Score target detection, role assignment, subgoal creation, candidate mix, ranking, chosen operation and destination, claim preservation, thesis salience, and whole-document role fit. If a supplied role map improves diagnosis but not generation, or frozen-candidate ranking succeeds where self-generation fails, the stages are empirically separated.

### 3. Compare a small software ladder

Use a few [CodeTaste](https://arxiv.org/abs/2603.04177) or locally frozen cases with a local workaround and defensible responsibility-changing alternative. Mirror the prose stages: open nearby task, open review, ownership-map diagnosis, frozen candidate generation, identical-set ranking under current tests versus responsibility/future-change criteria, and exact implementation ceiling.

Equalize scope permission and reversible-edit protection across local and structural options. A larger diff must not be silently disallowed. Current tests remain a local outcome; held-out changes and blinded responsibility judgments supply the global comparison. Compare the **shape of the stage gaps**, not raw accuracy across incomparable tasks.

### 4. Run the prose-specific redundancy counterexperiment

Test the boundary case rather than baking “subtraction is better” into the theory. Place a consequential fact far from its canonical declaration and compare:

- canonical declaration only;
- local restatement only; and
- canonical declaration plus checked point-of-use reinforcement.

Measure immediate reader or agent uptake, context cost, and consistency after a later revision to the canonical fact. If reinforcement improves uptake, or the checked dual representation wins the joint outcome, the simple normalization analogy is falsified. The structural theory may still survive if it distinguishes useful propagation from a unit that conflicts with its section role.

### 5. Run a prospective structural boundary-probing ladder

Build matched case triplets around an ownership, section-role, argument-structure, or decomposition rule that is plainly available in context but whose applicability is not explicitly questioned:

- an ordinary case where the rule holds;
- a boundary case where the rule fails and the artifact contains a relevant but non-conclusive cue; and
- a case with a tempting but irrelevant cue, where the rule still holds.

Freeze the triplet labels before model runs. Ground “holds” and “fails” in an observed downstream requirement or reader outcome, a mechanically checkable ownership or dependency consequence, or independent expert agreement elicited against stated alternatives and consequences. Match the true-boundary and false-lead cues for salience and plausibility so conspicuousness alone cannot solve the task.

Do not plant an explicit anomaly. Keep task, context, budget, and rule availability fixed, and separate the prospective route into stages. Freeze self-generated outputs at each stage or replace them with the same canonical upstream artifact before testing the next:

1. **Open origination:** compare the ordinary task with a generic permission to record consequential questions. Neither condition names a rule, boundary, or operation.
2. **Rule retrieval:** ask for the artifact's load-bearing structural rules without asking whether any rule fails.
3. **Consequence valuation:** supply the same candidate rules and ask what organizational consequence would follow if each failed; rank them under a one-probe investigation budget.
4. **Boundary-cue recognition:** freeze one rule and consequence, then ask which observable features of the case bear on the rule's applicability without supplying the suspected failure.
5. **Applicability-question origination:** supply the same rule, consequence, and balanced observation set, then require the agent to choose whether any rule-boundary question earns the single investigation slot. An exact suspected-boundary question is the downstream capability ceiling.
6. **Probe design:** freeze the question and ask for a check whose possible outcomes distinguish failure from compliance.
7. **Probe selection and execution:** give the identical randomized probe set with explicit costs, require one choice, and execute it or supply the same blinded outcome.
8. **Uptake:** test whether that result changes the rule's stated scope, the artifact's organization, the plan, or calibrated uncertainty.

Require a selected inquiry to name the exact rule, the consequence if false, the observable reason this case may lie outside its scope, the discriminating check, and the update licensed by each result. Score the gaps between stages as well as useful-probe origination, cue specificity, discriminating power, uptake, investigation cost, and false positives on the rule-holds and false-lead controls. An agent that doubts every rule should not outperform one that finds fewer but better probes. Include both code and prose only after each domain has independently credible cases.

## Deferred follow-ons

Do not make these closure requirements until the basic prose effect and stage ladder are established:

- **Masking and timing:** vary intervention timing and anomaly-ledger persistence only in traces where a concern is explicit before local closure. Otherwise “extinguished” is not observable.
- **Preservation bias:** compare generic critique, explicit deletion permission, and structural operator menus after a diagnosis has been frozen.
- **Behavioral prompt transfer:** apply a procedure abstracted from software examples to prose and vice versa. This can support portable intervention structure, not a shared training origin.
- **Longitudinal erosion:** introduce later requirements or revisions only after one-shot local/global alternatives have been validated.
- **Historical question playback:** linking-foundations and Decapod remain possible curiosity-method cases, not evidence for the base misplacement effect.

## Measurements worth retaining

- Was a global model constructed or supplied before editing?
- Was each target unit assigned an ownership or argumentative role?
- Was an anomaly explicitly registered before editing?
- Did the agent originate a rule-applicability question before an anomaly was supplied?
- Did it state a material consequence if the rule failed here?
- Was the suspected boundary grounded in the artifact rather than an unsupported story about the author?
- Would the proposed probe discriminate rule failure from compliance?
- Did the probe result update the rule's scope, artifact, plan, or uncertainty?
- Did the controller call a whole-artifact review after the local task succeeded?
- Did an explicit anomaly become a named subgoal and remain on the agenda after local closure?
- Which alternatives were generated: add, wrap, branch, bridge, qualify, move, merge, fold, replace, reframe, or delete?
- Did the agent inspect dependencies, section purposes, and history outside the immediate site?
- Did it rank a structural alternative correctly when the candidate set was frozen and identical across judges?
- Did the edit preserve all load-bearing behaviors or claims?
- Can independent reviewers infer the intended ownership model or document argument from the result?
- Does the intervention change the same measured transition in both domains?

Static smells, line counts, sentence perplexity, and generic coherence scores may screen cases. Delayed change locality, explicit role judgments, claim preservation, and blinded whole-artifact comparison are closer to the target property.

## Remedies remain downstream

Potential mechanisms include artifact-role maps, anomaly ledgers, consequence-first rule-boundary scans, question-generation passes, interruption thresholds, explicit structural operators, future-change simulation, and whole-artifact oracles. None should be promoted as a general remedy until an experiment shows which transition it changes. Otherwise “add a curiosity pass” risks becoming another additive accommodation in the agent architecture.
