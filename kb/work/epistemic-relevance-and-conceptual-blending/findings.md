# Findings and competing explanations

Date: 2026-10-31. Status: exploratory synthesis, not a new Commonplace theory note. Following the operator's subsequent direction, the current next step is the [observational watch](./README.md), not execution of the experimental proposals below.

## Conclusion

The distinction is useful, but its strongest empirical interpretation remains unproved. The investigation identifies a precise target: **a consideration that warrants attention to B is used to warrant an unsupported explanatory or constitutive relationship between B and A**. Existing studies establish several plausible ingredients, not the full utility-driven conceptual-blending mechanism. See the primary-source cards in the [evidence register](./evidence-register.md).

Three claims survive this pass. First, investigation priority and evidential warrant are different decisions. Second, relationship assignment can fail even when both ideas are retained and individually sensible. Third, acknowledging a correction is weaker than changing the relationships and consequences that govern subsequent work. Only the first is a general normative distinction; the frequency, causes, and tractable remedies of the other failures require measurement.

## 1. What the motivating episode establishes

The operator reports that an agent included generalization within an account of operationalization, initially accommodated criticism without removing that organization, and subsequently explained the distinction. The revised [operationalization workshop](../operationalization-executability-automation/README.md) keeps task-scope generalization separate from operationalizing knowledge for an admitted task.

This is evidence of a reported output-level mistake and feedback-sensitive correction. It is not evidence of prevalence, an RL cause, a particular internal representation, or durable transfer of the correction. An explanation produced after feedback may use information supplied by the feedback; it is not an inspection of what the earlier model call represented. An apparent correction also needs held-out tests to distinguish learning in context from agreement with the operator.

## 2. Concepts and the invalid inference

Epistemic relevance is relative to a question and an evidential situation. A line can be relevant by supporting an answer, challenging an assumption, supplying a counterexample, or identifying a boundary. It need not be part of the concept being explained.

Instrumental attractiveness is relative to a goal, available resources, and expected consequences. Practical payoff, novelty, interestingness, and pleasing the user are separable contributors, not interchangeable operational measures. The primary test should manipulate practical payoff rather than use enthusiasm as its proxy.

Suppose A and B both help achieve C. That supports grouping them as ways to achieve C. It does not entail that B is a component of A, that A and B mean the same thing, or that one mechanism explains both. The grouping can be valid at the project level while becoming invalid when silently relabeled as a definition of A.

Barsalou's goal-derived categories provide a useful conceptual comparison [E11]. Fauconnier and Turner's conceptual blending is not itself a pathology [E12]. Neither source demonstrates this LLM failure. For the present investigation, ordinary descriptions such as **unsupported conceptual integration** or **incorrect relationship assignment** are preferable to a new syndrome name.

The epistemic/instrumental distinction is not absolute. A successful method can be evidence about a claim when an explicit argument connects success to that claim and rules out relevant alternatives. Shared outcomes can suggest a common mechanism worth investigating. Such a suggestion is not yet its confirmation.

## 3. Why blend rather than preserve both?

The simplest candidate explanation is a wrong assignment of argumentative role. A useful idea is admitted into consideration; the current answer plan offers it a place as a dimension, component, or instance of the main concept; the answer then treats that placement as warranted. The model can retain the content of both ideas while losing the distinction between their contributions.

A possible sequence is:

1. A broader goal increases B's salience or priority.
2. The response adopts a frame such as a unified account of A.
3. B is retained by being assigned a relation to A that the evidence does not support.
4. Later elaboration and local revision preserve that relation.

This is a testable process hypothesis, not an observed hidden computation. It contains at least three independently variable transitions: selecting material, assigning relationships, and preserving an existing organization. They may have different causes.

There is a crucial alternative: the model may have silently answered a broader question, such as how to improve the project, while presenting the result as an answer to what A means. That is a task-interpretation error, not necessarily a failure to know the distinction. Compare [underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md), but do not relabel violations of explicit constraints as legitimate ambiguity.

## 4. Competing explanations and discriminators

**Pragmatic reinterpretation.** The agent treats project context as permission to expand the question. Predicts a large reduction when the local question and the permission to retain a separate tangent are made unambiguous. Persistence despite a completely specified local task weakens this account, although failure to follow that specification remains possible.

**Associative or template-driven integration.** Lexical similarity, familiar schemas, or shared consequences suggest an unsupported relationship even without a project payoff. Predicts effects from semantic relatedness and familiar wording in low-utility and no-goal conditions. Semantic leakage [E1] motivates this account but does not establish its relationship-level extension.

**Response-selection incentives.** Training or inference-time ranking favors apparent coverage, helpfulness, or narrative unity. Predicts that fixed incorrect-but-unified answers beat matched correct alternatives under a particular preference model. Surface-format bias is not evidence for a preference for conceptual unity; these must be manipulated separately [E4, E5].

**Trajectory dependence and local repair.** Once an unsupported frame is present, revisions preserve its organizing relation. Predicts worse correction with the old explanation retained than with the same facts and criticism supplied in a fresh context. This account can explain persistence without explaining initial selection [E3, E7].

**Presentation-only error.** The text places B under a misleading heading, but subsequent classifications and inferences respect the boundary. Predicts disagreement between prose-relation ratings and downstream behavior. This is still a communication defect, but a weaker threat than an operative false relation.

These explanations can combine. Evidence for one does not establish all of them. A mechanism is explanatory only if it predicts which intervention changes which transition.

## 5. What the literature does and does not establish

No reviewed study directly combines all three necessary elements: independent manipulation of project utility, fixed conceptual relevance, and measurement of false conceptual incorporation. This is a targeted-search result, not a claim that no such research exists.

The empirical foundation is narrower: semantic influence from irrelevant material [E1–E2], preferences that sometimes select appealing but epistemically worse responses [E4–E5], and failures to apply changed conditions or recover from earlier assumptions [E3, E7]. Training-origin comparisons caution against attributing every such effect to post-training [E6].

Negative and boundary findings matter. Increased reasoning effort can help on rigidity tasks [E3]; trained models can preserve separate answer roles [E8]; RL can improve correction [E9]; and a human separation intervention did not demonstrate the expected learning advantage [E10]. These findings do not establish an ideal intervention here, but exclude simple claims that more thinking, separation, or RL must have one universal effect.

The stronger claim that LLMs prefer one synthesis over multiple threads remains a research question. Neither next-token prediction nor fluent outputs logically require false unification. A model can produce one coherent document containing several correctly distinguished investigations.

## 6. Observable failures

Use the operator's five failures as overlapping labels, not mutually exclusive diagnoses. Failure to notice and failure to retain require evidence at multiple stages: a final omission alone does not distinguish them. Incorrect relationship assignment can occur without concept identity, for example reversing evidential dependence. Active blending incorporates B's conditions into A's definition or explanation. Premature synthesis asserts a common account without adequate warrant, including cases where the common account later happens to prove true.

A response can have separate headings and still say that B is required for A. Conversely, a short unified paragraph can preserve every relevant distinction. Score asserted relations and downstream consequences, not layout.

Omission is not automatically a failure. It depends on the commission and available resources. Recognition, durable capture, current execution, and final-answer inclusion are four different decisions. A useful tangent can be retained cheaply without being investigated immediately.

## 7. Boundaries and corrective principle

A valid synthesis must identify what relationship is asserted and why that relationship is warranted. A common cause, a derivation, a justified abstraction, or a stipulated formal inclusion can license unification. A shared benefit alone licenses only the corresponding functional grouping unless further evidence is supplied.

Test an inclusion claim with counterexamples: can A hold without B, or B without A? Counterexamples refute the relevant inclusion or identity, not every possible connection. For a common-mechanism claim, ask what observation it explains better than separate accounts and where it predicts the accounts should fail together. For an abstraction, ask which distinctions its downstream users must still recover.

The candidate corrective principle should therefore be conditional:

> Preserve productive threads when their expected value warrants retention; keep the purpose and evidential status of their relationships explicit; unify only as far as the warrant supports.

This does not mean always producing two long sections. Under tight budgets, a compact distinction and a deferred question may be enough. Under stronger evidence, unification may be the right result. The intervention must be tested against missed legitimate synthesis, capture cost, and reduced task performance, not only fewer false integrations.

## 8. Longer-horizon prediction

An unsupported relationship could be more consequential than an isolated incorrect sentence if later investigators inherit it as the organizing structure of the problem. They might select different questions, omit disconfirming comparisons, or judge corrections against the wrong frame. This is a conditional prediction, not a measured Commonplace failure rate.

Retention can preserve the false relation; repeated summaries can make it appear settled. But later criticism, independent evidence, or a fresh task frame could also remove it. The handoff experiment must measure these alternatives. Accurate copying is not epistemic validation, and storing explicit thread roles does not guarantee that a later model uses them.

The [bounded-context orchestration model](../../theory/bounded-context-orchestration-model.md) offers a place to retain state outside a call, not a proof that a new scheduler or schema is needed. The present workshop needs only existing Markdown artifacts.

## 9. Concrete Commonplace dispositions

**Use existing conceptual owners.** The [search-control/adoption boundary](../../theory/lightweight-search-control-does-not-license-adoption.md) already expresses the central warrant distinction. The [activation note](../../theory/knowledge-storage-does-not-imply-contextual-activation.md) and the [structural-coherence workshop](../agent-curiosity-and-structural-coherence/README.md) own neighboring problems. No new definition or general LLM-bias theory is justified by this pass.

**Review a specific cross-source inference.** The current [semantic-leakage ingest](../../sources/semantic-leakage-lms-gonen.ingest.md), under “Connections Found” and “Extractable Value,” treats semantic leakage, GSM-DC, content effects, and ConvexBench as measurements of one underlying mechanism. Its limitations are more cautious. The primary semantic-leakage study establishes associative influence, not a shared causal identification across those benchmarks [E1]. The proposed correction is to replace established-equivalence wording with a common-mechanism hypothesis and a statement of missing comparative evidence. This recommendation concerns evidential warrant; it does not establish that the mechanisms differ.

That passage is a candidate second fixture for premature synthesis. We have not observed its generation process or manipulated its instrumental attractiveness, so it cannot validate the complete target mechanism. A good repair preserves the productive cross-source hypothesis while withdrawing unsupported certainty; deletion of the connection is unnecessary.

**Current disposition: observe and correct before commissioning experiments.** The operator chose a [local checklist](./watch-checklist.md) and [case log](./observations.md) for the next few occurrences. Use those records to narrow, split, or reject the working hypothesis. The utility-versus-relation experiment and correction-versus-restart experiment remain possible later tests; neither is authorized, executed, or formally preregistered here. The source-interpretation review above is also a candidate, not a library change made by this workshop.

**Do not change operationalization.** The motivating distinction is an input to this investigation. None of these findings belongs in the definition of operationalization.
