# What HCL contributes to theory-mediated learning

> **Status:** Workshop reading. This note identifies the HCL mechanisms that could support a theory-mediated treatment and the point where that treatment would enter. The paired [source analysis](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) owns the detailed evidence and qualifications.

## HCL supplies a governed improvement loop

Harness Continual Learning (HCL) keeps foundation-model parameters fixed while allowing four parts of persistent harness state to change: the Task Interface, Experience Memory, Capability Map, and Adaptive Router. After a benchmark task, the optimizer uses the outcome and execution context to construct an isolated candidate. It searches the components in a predefined order. HCL commits the resulting multicomponent candidate atomically but does not optimize its components jointly.

The evaluator admits a candidate only when it improves current validation performance, stays within a historical-loss budget, and passes validity checks. Commitment then makes the accepted harness state available to later tasks. HCL therefore implements the search, reject-capable evaluation, and operative retention required by a [proposal-selection improvement loop](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

These mechanisms provide concrete techniques for governing behavior-changing harness updates: isolate candidates from deployed state, compare them with the incumbent, test current benefit and historical retention, and commit related state atomically. They support treating [the deployed system rather than the model alone as the learning unit](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).

The evaluator's warrant remains bounded by its evidence. Historical loss `D_n` counts sampled earlier-task anchors that the incumbent solves and the candidate newly fails. A zero loss budget protects every such anchor, not every prior behavior. HCL still reports nonzero held-out forgetting in controlled regimes with a zero budget. This result separates stricter acceptance from broader oracle coverage: HCL demonstrates protection over sampled checks, not a general no-regression guarantee. [Warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) develops that distinction.

## The proposed theory layer enters before the edit

HCL's optimizer already asks a frozen LLM to analyze an outcome, identify components to revise, and generate alternatives. However, HCL exposes no separately represented theory between that evidence and the candidate edit. Its Abstract Memory stores summarized, scoped guidance, but the study neither establishes those entries as premise-bearing explanatory theories nor tests whether they mediate a decision. Abstract Memory should therefore not be relabeled `T_n`.

The proposed treatment inserts a recorded working theory `tau_n` after the task evidence and before the decision it will guide. The theory states a mechanism or invariant, its premises and scope, and consequences that could prove it wrong. It may guide diagnosis, select an intervention point, direct candidate search or choice, or derive evaluation obligations. Recording the theory before candidate selection and before the experiment reveals hidden outcomes distinguishes mediation from a post hoc rationale.

The first HCL-compatible experiment should test an on-the-spot `tau_n` while retaining HCL's full evaluation. This contrast asks whether theory improves search or candidate choice without confounding the result with selective evaluation. A later experiment can allow theory-derived obligations to guide evidence acquisition. The [experiment design](./experiment-design.md) specifies these stages, and the [selective-evaluation model](./selective-evaluation-model.md) defines the evidence-selection claim.

The retained-theory design is a stronger treatment. It requires an addressable `T_n`, evidence that later episodes retrieve and use it, and a separate gate for each revision to `T_n`. HCL's atomic commitment of harness state does not provide that theory lifecycle. Candidate acceptance and theory acceptance remain different decisions: a useful edit can follow from a false explanation, while a failed edit can reveal a useful counterexample. The [theory-mediated improvement model](./theory-mediated-improvement-loop.md) locates both decisions.

## What HCL does not establish

HCL studies controlled benchmark streams. It does not show that the same mechanisms learn reliably from delayed, noisy, or incomplete evidence produced by real-world work. Applying them at deployment time would require an explicit evidence boundary, live isolation and rollback, and an evaluator whose claims match its observable domain.

HCL's four-part state is also an engineering partition, not a validated theory of system operation. Its ablations vary bundles of permitted persistent updates. They do not identify the four parts as necessary components, causal variables, or boundaries that contain behavioral effects. [An experiment identifies only the contrast it actually runs](../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) supplies this attribution limit.

HCL thus provides the governed substrate, not evidence for the added theory layer. The open question is whether making an explanatory intermediate explicit improves a specific decision enough to justify its construction and checking cost.
