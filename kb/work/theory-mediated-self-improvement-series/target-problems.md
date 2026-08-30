# Target problems

The program is organized around one central scientific question and four
supporting problems. Each problem is stated independently of its source
tradition so that mechanism matches do not smuggle in conclusions. The
[match register](./match-register.md) records which sources bear on which
problem and what each match licenses.

| ID | Problem | Optimization target | Feedback | Information structure | Characteristic failure |
|---|---|---|---|---|---|
| P1 | **Coherent modification.** Can a computational composite use a fallible, project-specific theory to keep model-mediated search, independently executed symbolic operations, backtracking, recovery, and revision coherent across novel programming demands and delayed feedback? | Changes that preserve or deliberately revise the program's purpose and organization across a sequence of demands | Branch choices, immediate checks, later requirements, code execution, maintenance failures, operational outcomes, and recovery quality | The model-mediated operation is instantiated by weights plus a prompt assembled from mixed project state; code supplies runtime-assigned operations; the theory is partial and no local rule uniquely determines the right change | Weight–prompt search and symbolic execution drift apart; a locally successful patch damages the wider organization; or the process cannot diagnose and recover when delayed evidence exposes the damage |
| P2 | **Warranted transfer.** On a declared path, how does a decision leave the human cut with warrant, and how does the composition of the remaining work change? | Fewer required human decisions at fixed or better warrant and utility, including staged transfer of search allocation, reversible execution, and adoption authority | Before-and-after classification of transferred and residual decisions; later outcome evidence | Transfer may preferentially select decisions with represented premises, settled criteria, independently executable transitions, and checkable outcomes | Apparent transfer through a captured evaluator, viability-only gate, boundary export, displaced review, irreversible trial, or degraded residual judgment |
| P3 | **Operative theory.** How does retained theory causally change a weight–prompt proposal, branch allocation, diagnosis, evaluation, recovery step, or symbolic revision; receive outcome read-back; and affect later operation? | Increasingly strong evidence from mediation through recurrence, including changed later search or execution | Theory interventions with weights and symbolic state held fixed, mediation traces, independent consequences, theory and code revisions, and later use | Natural-language theory, symbolic project state, prompt assembly, model interpretation, runtime execution, evaluation, and continuity are distinct functions that may be coupled through one path | Inert documentation, code-only success misattributed to theory, post-hoc rationale, self-sealing evaluation, wholesale replacement without traceable revision, or disconnected witnesses inside one boundary |
| P4 | **Evaluation and comparison.** How are search-controller quality, symbolic-complement value, usefulness, computational autonomy, warrant, and power compared without collapsing them into one scalar? | Measurements that detect better branch allocation, reliable execution, a real change in the human cut, accepted outcomes, correction quality, and total human effort | Matched search budgets, downstream branch consequences, model-mediated versus symbolic comparisons, declared task selection, capability floors, evaluator tests, outcome records, and residual-decision records | Search judgments and acceptance judgments have different authority; code may execute exactly while implementing a bad requirement; functions differ in stakes and grain; closure is structural while warrant is evidential | Candidate volume mistaken for search quality, code exactness mistaken for objective validity, percentages of autonomy, activity counts, self-scored prose, or an evaluator treated as the definition of closure |
| P5 | **Search-control and operation-boundary bootstrapping.** Can an already-computational theory-guided human-agent loop improve weight–prompt search through retained project state, use code for independently executed symbolic operations, learn which responsibilities belong on each side, and convert recurring judgments into reusable computational search, selection, and credit-assignment machinery? | Better downstream results from additional computation, reliable and economical symbolic complements, a revisable operation boundary, falling marginal human judgment per accepted improvement, transfer beyond anticipated domains, and competitive total cost | Truth and validity checks, theory interventions, branch-routing comparisons, symbolic-complement experiments, operator corrections, delayed system consequences, codification and relaxing events, evaluator conversions, cross-domain transfer, and direct-learning baselines | Weights provide general competence; prompts specialize it from natural-language, symbolic, and evidential project state; code plus runtime executes selected operations independently of model reinterpretation; global fit, credit, and operation placement remain distributed and partly human-selected | More computation only generates candidates; retained theory makes no causal difference; code is treated as fixed infrastructure or codifies bad proxies; model-mediated bookkeeping remains unreliable; human fit and boundary judgments do not fall; every domain needs a bespoke ontology and operation allocation; or a direct method performs better |

## Relations among the problems

P1 is the scientific center. It asks whether a computational bearer can do what
human programmers do with partial theory: use it to control search and recovery
while coordinating exact executable changes when no complete specification or
cheap oracle settles the modification.

The leading operation-level model is that prompts do not define semantic
operations alone. A call's behavior is instantiated by the model's weights plus
its prompt, while code complements that pair with operations whose consequences
are assigned and executed by a symbolic runtime. See
[code complements the weight–prompt pair with independently executed symbolic
operations](../../notes/code-complements-the-weight-prompt-pair-with-independently-executed-symbolic-operations.md).

P2 meets P1 at the same hard modification decisions but asks a different
question. P1 concerns the capability to sustain coherent modification. P2
concerns whether enough premises, authority, correction, continuity, and
reversibility lie inside the declared boundary for a decision to move with
warrant. Lightweight branch allocation, reversible symbolic execution, and
final adoption can move at different times. A system can be computationally
closed and still fail P2 because its evaluator or requirement is weak.

P3 supplies the attribution test for P1. A stored theory does not count merely
because it accompanies a successful code change. The programme distinguishes
mediation, empirical contact, theory-state revision, and recurrent later use.
The clean theory intervention holds weights, code, runtime, tools, and task
fixed while changing the natural-language theory supplied through the prompt.
Longitudinal episodes may then let theory, code, and their allocation coevolve.

P4 is evaluation infrastructure for P1–P3. It separately asks whether a search
controller routes limited resources toward stronger downstream consequences,
whether moving an operation into code improves reliability and cost after
specification and maintenance are counted, and whether an accepted change is
adequately warranted. It keeps structural closure, capability, warrant,
usefulness, and power separate.

P5 is the first construction strategy under the Bitter Lesson's scaling
pressure, not a defense of hand-crafted artifacts and not a uniqueness claim.
The narrow rebuttal says only that learned results need not all live in weights.
P5 begins from the fact that the current Commonplace loop already composes both
operation classes: weights plus prompts perform retrieval, interpretation,
search, synthesis, criticism, and semantic judgment; code plus runtime performs
repository transitions, tests, validation, scheduling, state retention, and
other independently executed operations. The operator currently supplies much
of the sparse high-level selection, credit, and operation-placement signal.

P5 asks whether the live system can improve all three connected surfaces:

1. model-mediated search over project theory and code;
2. symbolic operations that execute selected behavior and improve the later
   selection environment; and
3. the boundary deciding which behavior should be model-mediated, codified,
   relaxed, or retained as a provisional search control.

It succeeds only if additional computation improves downstream search quality,
not merely candidate volume; symbolic operations earn their placement through
measured reliability, cost, and scope; the marginal human share falls; the
boundary and selection machinery remain challengeable; and the process
transfers beyond domains and decompositions anticipated by its designers.
End-to-end, evolutionary, parametric, and other computational approaches remain
comparison strategies.

## What is deliberately not a target problem here

- Whether a current system qualifies as “self-improving” by category membership;
  the definitions already classify that, and category membership is not the
  research result.
- Whether computation has begun. The current human-agent loop already composes
  computational model-mediated and symbolic operations; the problem is improving
  search, execution, selection, credit assignment, and their allocation.
- Whether a prompt alone defines an LLM operation. The programme treats the
  operation as instantiated by the weight–prompt pair under fixed call settings.
- Whether code or the model is globally superior. They provide complementary
  operation classes whose appropriate scope must be learned and tested.
- Whether theory-guided bootstrapping is the only possible route. It is the first
  strategy being tested because global theory fit and operation placement lack
  complete fixed evaluators.
- Whether natural-language, symbolic, and parametric carriers must remain
  permanently separate. The current realization keeps their roles inspectable;
  the durable claim concerns complementary functions and failure surfaces.
- Whether structural computational closure guarantees correctness or value. It
  says where required decisions and transitions occur; capability and warrant
  need separate evidence.
- Execution of this workshop. The operator's intent, authority boundary,
  priorities, and hand-back conditions are governed by [the workshop
  README](./README.md), not promoted into a scientific target problem.
