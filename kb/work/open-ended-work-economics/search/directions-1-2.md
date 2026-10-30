# Search results: directions 1 and 2

Raw material for the reconciliation map. Coverage and summary only; no
judgment about whether the economic framing adds anything. Scope searched:
`kb/theory/` (with `definitions/`, `proposals/`, `evidence/`),
`kb/reference/` (with `adr/`), `kb/sources/` ingests, and peer workshops under
`kb/work/`. Paths are relative to `kb/`. Workshop entries are in-flight
material, not library claims, and are marked **(workshop)**.

---

## Direction 1: the nature of commitments

### 1A. What a commitment is: the derivation/commitment boundary

**`theory/commitment-not-derivation-creates-new-ground-truth.md`**
— "Derivation — claims recoverable from the source, nothing added — leaves the source as ground truth; what adds unentailed resolutions becomes ground truth at commit, repaired by supersession."
Defines a commitment as the act that fixes, in a retained artifact, an addition the source does not determine: "a generalization beyond the evidence, a decision among live options, one reading selected from a space of admissible ones." The discriminator is what is added, not what is lost. A committed artifact becomes ground truth and its raw material demotes to provenance. Repair is therefore supersession, not recompute. The committer can be a person (accepting an ADR, attesting `user-verified`, selecting an LLM output) or a model; "the claim classifies productions, not producers." Open question bearing on retraction: "What retires a commitment when no successor commitment is coming?"

**`theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md`**
— "Theory building and capacity building both retain resolutions their evidence does not entail; an explanatory commitment stays answerable to the object it describes while a constructive commitment changes the object, so retraction differs in kind."
The source of the explanatory/constructive split. An **explanatory commitment** "selects an account of how or why something works" and changes the theory used to interpret later situations. A **constructive commitment** "selects how future work will be done: an architecture, representation, tool, workflow, invariant, convention" and changes production machinery. The parallel breaks at retraction: retracting an explanatory commitment revises theory and dependent conclusions, while retracting a constructive one is "supersession followed by reconstruction, not a change of mind." Scope: the split classifies resolutions, not artifacts (an ADR bundles both). Derived organization is "a third kind of retained state, not a milder commitment"; the three kinds "do not form a spectrum." Gives the causal path experience → explanatory commitment → theory-guided constructive commitment → changed machinery → new experience → theory revision. The note says nothing about resource-allocation or investigation decisions as a commitment kind.

**`theory/definitions/discovery-lifecycle.md`**
— "Definition — the discovery lifecycle is an ideal-type six-phase evaluation of an ampliative conjecture."
Six phases: observation, conjecture, consequence derivation, test, acceptance, integration. Acceptance is "gated commitment on the successful branch": "the consuming workflow's recorded decision that this evidence meets its named criterion". Testing, acceptance and integration are distinct acts. Transitions include revision (back to conjecture), suspension (preserves candidate status while awaiting evidence) and rejection. Later counterevidence opens a new instance; prior acceptance "remains part of the record rather than shielding the claim." This is the closest library ladder to considering → adopting → maintaining → retracting, for beliefs only.

**`theory/definitions/tentative-theory.md`**
— "Definition — a tentative theory is a theory proposed as a solution to a problem, which stays open to criticism and revision however well it has survived."
Popper's `TT`. Tentative is "a status, not a stage": corroboration strengthens grounds for reliance without ending the status. The term "licenses no particular use": "does not say how much support permits retention, experimental use, routine reliance, or codification. Those are policy questions a builder answers for each use." Excludes the everyday sense ("not tentative because its author is unsure of it or because approval is pending"). So "provisional" in the workshop's sense is not this term.

**`theory/definitions/theory-builder.md`**
— "Definition — a theory builder applies conjecture and refutation to stated theories: it acts on them, criticizes what they say, and lets the result shape the next round."
Four conditions: localized content, consumption (theories guide action through what they say), criticism, iteration. Under iteration, after survival "the text may stay the same while the theory's testing record changes", and the record "changes how far the theory is relied on". It cites Popper on "a law of diminishing returns from repeated tests", so the next problem is finding a test of a new kind. This is the only place the definition touches the economics of further testing. Contrasts criticism with gradient descent.

**`reference/epistemic-stance.md`**
— "The philosophical tradition Commonplace's assertions assume — Popperian: fallibilism, methodological rules as conventions, anti-essentialism, intersubjective testability — and what it does not inherit."
Point 2 matters most here: "ADRs, contracts, type specs and definitions are adopted by decision and judged by their fruits. They are contested by proposing a better convention, not refuted by counterexample." So the stance already separates claims, which are conjectures and can be refuted, from adopted conventions, which are decisions. Point 5: the propensity interpretation of probability and verisimilitude measures are "not inherited." The stub says nothing about allocation, value or investigation.

**`theory/superseded-choices-are-retained-superseded-beliefs-are-not.md`**
— "Retention after supersession follows remaining truth role rather than maintenance operation: preserve a witness to the choice event, while a refuted belief loses subject-matter standing."
Separates beliefs, which answer to evidence independent of what the system once thought, from choices, which answer to the act of choosing. After supersession, "The system committed to X at t" stays true while "Do X now" loses authority. An ampliative conjecture is a committed addition "but what it asserts remains a belief," so commitment by production relation does not settle the retention regime. Choices form an append-only chain; beliefs are reworked holistically. This is the library's sharpest statement that claims about truth and decisions about action have different lifecycles after retraction.

**`theory/artifact-classification-separates-content-kind-lineage-and-authority.md`**
— "Use this note to classify retained KB artifacts without conflating content kind, production lineage, or path-relative behavioral authority with the collection's local writing contract."
Content kind, production relation and behavioral authority are three questions that cannot stand in for each other, and their answers attach to different units (region, consumption path). It is relevant because a claim's truth-standing and its authority to govern action are classified separately.

### 1B. Considering versus adopting: "worth investigating" is not "warranted"

**`theory/lightweight-search-control-does-not-license-adoption.md`**
— "A search judgment is lightweight when its authority stops at allocating further investigation, probing, continuation, suspension, or abandonment rather than licensing an operative change."
"'Worth investigating' and 'warranted to adopt' are different conclusions. The first may rely on evidence too weak for the second because the selected branch remains subject to stronger evaluation before adoption." "Lightweight" names the authority, not the cost, formality or confidence. A costly analysis can be lightweight, and a cheap rule can be an acceptance control. This is the library's direct statement of the brief's "a judgment that something is worth investigating is not a claim that it is true." It does not say how to allocate.

**`theory/candidacy-evidence-licenses-escalation-not-acceptance.md`**
— "Separates candidacy evidence, which routes a hypothesis to costly assessment, from verdict evidence, which decides it."
Status: conjecture with two worked cases. Candidacy evidence "can afford to be cheap, defeasible, and merely author-external, because the only thing it puts at risk is assessment cost." Explicit external anchor: "Peirce's economy of research. Peirce's question for abduction was economic — which hypotheses deserve the cost of testing, given explanatory promise and the price of the test — and its output is a pursuit-worthiness judgment, not a truth judgment." The failure mode is an "immunizing slot" when routing evidence carries verdict authority. Peirce is cited without an ingest.

**`theory/derivation-and-inheritance-give-starting-warrant-earns-scope.md`**
— "For reusable decompositions, derivation and inheritance supply conditional or transferred starting warrant, while evidence or proof earns only the scope it covers."
For underdetermined choices: "Convenience, symmetry, simplicity, or a mechanism-preserving analogy may justify a provisional preference. Such reasons can make one decomposition more worth testing than another, but they supply neither the conditional warrant of derivation nor the transferred evidence of inheritance." Such a boundary "should remain cheap to replace." It keeps pursuit-worthiness separate from warrant.

**`theory/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`**
— "Treat support for a theory as warrant for only the most specific claim, conjunction, model, and scope the evidence identifies."
Section "Criticizable structure gives candidacy, not warrant": exposing parts makes a theory "a candidate for explanatory-reach", but "Exposure is not support." It supplies the warrant non-distribution mechanism that candidacy-evidence relies on.

**`theory/a-claim-without-external-assessment-carries-three-obligations.md`**
— "Without external assessment a claim needs its own contradiction-and-support rule, a comparison level for objective change, and a performance measure it does not grade itself, plus attribution when it asserts a cause."
"Candidate retention is separate from reliance. A claim may guide an experiment without being ready for routine use or codification." Support must say "what kind of reliance that support licenses." "Entertaining an untested idea does not change its category." It separates uses (experiment, routine reliance, codification) that need different support.

**`theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md`**
— "Independent warrant and fit in a working theory answer different questions."
"'This claim helped the system' cannot silently become evidence that the claim is true, and 'this claim is true' cannot silently become evidence that it deserves a retained role in this theory." This is a neighbouring separation: usefulness or retention-worthiness versus truth.

**`theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md`** (see also 2B)
— "Explains why a disposable local guess can rationally select the next probe when error is cheap and contained, while retained explanations need reach checks."
For direction 1: "Using a guess as a probe premise is not yet retained commitment. ... selecting a probe does not make the explanation ground truth." A discarded explanation never crosses the commitment boundary. If a workflow promotes it into reusable machinery, "that promotion is the commitment." So acting on a hypothesis is separated from committing to it.

**`work/decision-lifecycle-evidence/README.md`** (workshop)
— Commission: preserve a decision's development from proposal through deliberation, implementation and later evaluation.
One of three distinctions it keeps visible: "Adoption is an authorized commitment, not a consequence of a claim clearing an evidential threshold. Implementation and observed benefit remain separate." Open question: how rival claims, options, objections, constraints and adoption relate "without treating a commitment as a corroborated belief". It also separates decision-time expectations from later explanations and observations. This is the nearest treatment of adopting versus acting (implementing) versus evaluating as separate states.

**`work/decision-lifecycle-evidence/adrs4ai-comparison.md`** (workshop)
— Comparison of ADR practice with a richer decision record.
"Architecture includes both conjectures and commitments. 'This layout will reduce context cost' is a claim that evidence can undermine. 'We adopt this layout' is an authorized choice. 'The implementation follows it' is a separate factual claim. New criticism may weaken the rationale without revoking the choice; adoption must not make the supporting conjecture appear established." It splits responsibilities into design reasoning, adoption record and current architecture view. This is the most explicit three-way split of expected-effect claim, adoption decision and implementation fact.

### 1C. Adopting, acting on, entrenching, deferring

**`theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`**
— "Distinguishes reversible adoption from costly structural entrenchment and confines option reasoning to the timing of a commitment supported by an enduring constraint, scoped transfer warrant, or actual coordination value."
Adoption means using a structure for current work. Entrenchment means "creating dependencies or migration costs that make replacement expensive"; "Adoption and entrenchment are therefore different decisions." Entrenchment needs one of three warrants: an enduring constraint, discriminating transfer evidence or proof, or coordination value. Pindyck-style option value "changes timing, not warrant": "Real-options reasoning can change when to commit or whether to preserve and investigate an alternative. It does not add a fourth warrant." It defines a bounded probe (cost, output, stop condition, follow-on decision) and lists delay costs. "The rule is qualitative. The available evidence supplies no portable threshold." This is the library's main place where an economic argument (options) governs the timing of a commitment and is barred from supplying its warrant.

**`theory/prototype-standing-is-revision-cost-binding-plus-lost-investment.md`**
— "A theory's prototype standing is its expected revision cost — external binding plus the investment a revision discards."
Prototype standing is "a standing in the theory's engineering lifecycle — how cheaply it can still be changed — not a phase of the discovery lifecycle," and acceptance is "a separate axis": "An accepted theory can therefore keep prototype standing, and a conjecture can become entrenched or heavily invested before it earns acceptance." Binding before acceptance "spends standing that evidence has not yet licensed"; it is permissible for coordination value or a forced constraint as "knowingly spent standing." "There is no formula and no weighting; 'expected' means anticipated at assessment time, not probability-weighted." This keeps revision cost (an economic quantity) separate from epistemic status.

**`theory/definitions/coordination-value.md`**
— "Definition — coordination value is the worth a shared structure has because adopters commit to the same one; created by the commitment rather than discovered as a property of the choice."
A warrant on the "value-source axis" alongside reach and inherited constraint. It is "absent until the commitment and scoped to its adopters", and "a better-in-principle rival does not increase it". This is a case where the act of commitment creates the value that justifies it, with no truth-claim behind it.

**`theory/productive-deferral-requires-option-evidence-and-convergence.md`**
— "A qualitative test that separates controlled postponement of a consequential choice from hidden commitment, mere delay, and unmanaged indecision."
Three necessary conditions: a preserved option (materially live through the decision point), discriminating evidence ("at least one possible result ... must be capable of changing selection, timing, modification, or abandonment"), and a convergence rule that couples a return condition to a response. Four postures: commit now, passive waiting, bounded probe, maintain alternatives. "The three-part test rejects false deferrals before this domain-specific comparison; it does not supply a portable quantitative threshold." Sources: Pindyck, Kennedy/Sobek set-based design, PMI and Githens rolling-wave planning, Haasnoot adaptive pathways. Operationalized into `instructions/write-instruction.md`.

**`theory/backtracking-keeps-lightweight-search-control-provisional.md`**
— "Backtracking preserves the provisional status of a heuristic branch choice by restoring an earlier usable state and redirecting search after contrary evidence."
"Without an operative return path, a trial can become a de facto commitment. Later work may depend on it, the prior state may become costly to recover, and a judgment that was meant only to allocate search may acquire the consequences of acceptance." This is the mechanism by which acting on a search choice slides into an unwarranted commitment. Scope: reversible branches can still cause irreversible external effects.

**`theory/files-defer-centralized-schema-commitment-until-invariants-stabilize.md`**
— "Canonical files can defer a centralized schema while meanings remain unsettled; a database becomes canonical only when an explicit authority decision and operative write path commit resolutions the files no longer determine."
A worked commitment-timing case for a constructive commitment. It transfers progressive constraining's timing pattern: central codification while meanings remain live "can freeze one unsettled interpretation".

**`theory/progressive-constraining-commits-only-after-patterns-stabilize.md`**
— "Constraining via LLM code generation freezes a single projection of the spec in one shot, but progressive constraining observes behavior across many runs and commits only the interpretations that consistently emerge."
One-shot versus progressive constraining: commit a resolution once observed stability makes it safe. Paired with commitment-not-derivation ("Commit once, derive thereafter"), this is the library's account of converting judgment into routine. It does not price when the conversion is worth paying for.

**`theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md`**
— "Ordering heuristic for decomposition: commit first to decisions with the fewest viable options, then place flexible choices around them to preserve global optionality."
A sequencing heuristic for commitments under interdependence (Alexander's kitchen). It bears on the order of commitments, not their warrant.

**`theory/cheap-adoption-and-weak-retirement-accumulate-cost.md`**
— "Explains why locally cheap structural additions become routing, maintenance, and migration debt when retirement needs distributed evidence and lacks an equally operative path."
The commitment lifecycle is one-sided: adoption is a local change, while retirement needs consumers, dependencies and migration accounted for. "Strong retirement need not make removal automatic or as cheap as adoption; it makes recurring evidence capable of reaching a decision and completing its consequences." Lifecycle capacity should be assessed separately from write capacity. This is direct material on maintaining versus retracting costs.

### 1D. Maintaining, revising and retracting

**`theory/reflection-makes-retained-lessons-second-order.md`**
— "Reflection lets a retained lesson target a prior commitment explicitly — rejecting, revising, or rescoping it — while non-reflective correction acts indirectly through the substrate."
Retained lessons are "learned inductive commitments." There are three second-order operations on a represented commitment: rejection, rescoping and revision. Rescoping requires represented scope. "A second-order lesson is itself a commitment and can be wrong." Open question: whether lessons about rejection and rescoping policies are third-order. This is relevant to recursion and to whether policy-level choices are commitments.

**`theory/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md`**
— "When an index is a list of claims rather than topics, reviewing the KB becomes scanning hypotheses — each title exposes its commitment and invites the question 'do I still believe this?'"
Maintenance as re-asking belief in each exposed commitment. It is a cheap-review mechanism for the maintaining stage.

**`reference/adr/085-withdrawn-proposals-are-deleted.md`** and **`reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md`**
— 085: "a design proposal whose problem or adoption trigger has lapsed, with no decision foreclosing it, is withdrawn by deletion"; 056: adopted and retired proposals move to an archive after extraction.
These are the shipped disposal rules for considered-but-not-adopted options (deleted) versus adopted or retired ones (archived). Commitment-not-derivation uses 056 as evidence that committed records are archived rather than deleted.

**`reference/design-rationale-management.md`**
— "How Commonplace distributes design-rationale records across proposals, ADRs, contracts, and enforcement, without enforcing end-to-end continuity."
This describes where each stage of a design commitment is recorded (proposal, ADR, contract, enforcement). It states continuity is not enforced. (Read at description level only.)

**`work/writing-as-thinking-process-transfer/README.md`** (workshop), candidate 2
— "Counterexample-scope routing": classify a defeated point "*local* (defeats a premise → revise, keep the commitment) vs *global* (propagates to the commitment → retire)."
This is a candidate rule for choosing between revising and retracting a commitment after a counterexample. Status is in the workshop table.

**`work/philosophy-borrowing/quine-web-of-belief.md`** (workshop)
— "Central beliefs are harder to revise because many other commitments depend on them."
This is a candidate borrowing for revision cost as a function of dependants. It parallels prototype standing's external-binding component.

### 1E. Are allocation decisions, goals and policies themselves commitments?

No library note says directly whether a decision to allocate resources is a commitment, a kind of commitment, or an operation on commitments. The nearest material:

**`theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md`**
— "A machinery improvement is paid for once and reused by every later learning episode, so over a long horizon its return can exceed immediate learning; where it does, an optimal strategy diverts effort to the machinery."
"A learning strategy allocates effort between learning now and improving the machinery that learns." It frames allocation as a strategy-level choice whose optimum "follows the returns as the system, its horizon, and its problems change." It is conditional on improvements being findable, persistent and of higher "expected marginal net return" than competing uses. It does not call the allocation a commitment.

**`theory/computationally-directed-self-improvement-is-a-reallocation.md`**
— "The progress question for self-improving systems is not category membership but which decision-bearing functions humans still supply."
"Allocation" here means the assignment of decision-bearing functions (search, evaluation, retention) to human or computational suppliers, not the allocation of effort among investments. This is a vocabulary hazard: the library already uses "allocation" in a second sense.

**`theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md`**
— "Reflection makes selected production machinery challengeable, but placement alone neither warrants nor requires revision; fixed general machinery may persist when its role and scope are earned."
"Exemption by position becomes persistence by warrant": "Applying an assessed standard to consequential free choices, machinery included, is this note's conjecture." It treats machinery choices as commitments that need warrant. "Objectives, commitments, authority grants, and fixed general learning machinery may remain supplied."

**`theory/intent-controls-choices-by-distinguishing-live-alternatives.md`**
— "A stated intent controls a local choice only when it changes which live alternatives are admissible, preferred, worth further search, or sufficient to stop."
It lists "worth further search" and "sufficient to stop" alongside admissibility and preference as the outputs a governing intent controls. This places search-allocation judgments inside the same control relation as action choices.

**`theory/self-improvement-is-relative-to-a-declared-objective.md`**
— "The improvement objective is a declared parameter alongside boundary and horizon, carrying two separable conditions — indexed by the analyst, antecedent in the pathway."
Objectives are declared, not discovered, and are needed for any improvement claim. It bears on the "goals are not beliefs" weak point: the goal side is a declared parameter.

**`theory/revising-an-improvement-objective-is-licensed-from-outside-it.md`**
— "Objective change is improvement only against a level outside both objectives; proxy revision, re-indexing, and surfaced under-specification subtract most apparent cases."
"Every objective approves of itself." Most apparent goal changes are proxy revision, re-indexing or surfacing of under-specification. It bears on brief direction 3 ("discoveries change higher-level goals") and on whether goal commitments can be revised on evidence.

**`theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md`**
— "Between an improvement objective and its oracles sits a target level — a property pursued because it is held to serve the objective — whose linking claim no check in the loop evaluates."
A proximate target bundles a pursued property (a practical commitment) with a linking claim ("this property produces that outcome"), which is truth-apt and unchecked. It is a worked case of a practical commitment resting on an untested explanatory conjecture.

**`theory/technical-constraints-make-kb-objective-choice-engineering.md`**
— "Three technical constraints and the codification lever make KB objective-function choice testable engineering, not philosophy; goals set the loss, local contracts specialize it, and oracle strength differs by objective."
"Goals set the loss." Bounded context, the reader and the verification boundary prune the candidate objectives. This is the library's main place where a value/goal choice is constrained by resource bounds.

**`work/conjecture-store/candidates.md`** (workshop), first candidate
— "every project holds two kinds of commitments, choices it made and theory it built, and its working knowledge is theory stated with some variables bound to those choices and the rest to general knowledge."
The operator's 2026-10-24 conjecture. It names Carnap's external/internal questions and Lakatos's hard core as analogues to check. It is a different two-way split from explanatory/constructive: choices versus theory.

**`work/conjecture-store/research-notes.md`** (workshop), §5
— Self-improvement of connection samplers: "samplers as bandit arms scored by later uptake only, policy in a skill file so it is an addressable commitment."
This is the only place found that explicitly calls an allocation policy a commitment, and it is in passing.

**`work/cognitive-architecture-transfer-scan/synthesis.md`** (workshop), Pattern 2
— "selection values are not one number."
It lists epistemic support, activation, attention priority, "expected utility: how useful might an action be?", "commitment: which plan is currently being pursued?" and behavioral authority as separate quantities ranking systems collapse. This treats commitment (plan pursuit) and expected utility as distinct from epistemic support. Candidate only; the significance test is unmet.

### Not found (direction 1)

- No note that classifies resource-allocation decisions as a commitment kind, as an operation governing commitments, or as a separate layer. Allocation appears as lightweight search control (authority limited to routing further search), as strategy-level effort allocation, and as actor allocation of functions. None of these is related to the explanatory/constructive taxonomy.
- No library treatment of "economic conjectures", meaning conjectures about the value of an investment, as truth-apt claims with their own lifecycle. Candidacy evidence and lightweight search control come closest, but they classify evidence and authority, not the value conjecture itself.
- No note distinguishing epistemic from practical commitment under those names. The nearest pairs are explanatory/constructive, belief/choice (superseded-choices), claim/convention (epistemic stance point 2), and claim/adoption/implementation (decision-lifecycle-evidence workshop).
- No single ladder covers considering → adopting → acting upon → maintaining → retracting. The pieces are scattered: the discovery lifecycle (beliefs, through acceptance and integration), adoption/entrenchment (structures), prototype standing (revision cost), supersession and second-order retraction. "Acting upon" as a stage separate from adopting appears only in the workshop distinction between adoption and implementation, and in the probe-premise case in the ad-hoc note.
- No treatment of whether goals or preferences are commitments in the explanatory/constructive sense. Objectives appear only as declared parameters.

### Sources (direction 1)

- Ingested: Popper (`sources/popper-logic-of-scientific-discovery.ingest.md`, `popper-conjectures-and-refutations.ingest.md`, `popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md`, `popper-epistemology-without-a-knowing-subject-1968.ingest.md`); Pindyck on irreversible investment and options (`sources/pindyck-irreversibility-uncertainty-investment.ingest.md`); Kennedy/Sobek set-based design (`sources/kennedy-sobek-kennedy-set-based-rework.ingest.md`); rolling-wave and adaptive-pathways sources (`sources/pmi-lexicon-project-management-terms-v4.ingest.md`, `githens-manage-innovation-programs-rolling-wave.ingest.md`, `haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md`).
- Not ingested: Peirce (economy of research is cited in `candidacy-evidence-licenses-escalation-not-acceptance.md` without an ingest); Carnap, Lakatos and Quine (only workshop drafts in `work/philosophy-borrowing/` and the conjecture-store candidate); Popper's *Open Society* and *Poverty of Historicism* (the stance flags them as not ingested).

---

## Direction 2: bounded rationality and the economics of investigation

### 2A. Search must be allocated before decisive evaluation

**`theory/open-ended-improvement-allocates-search-before-evaluation.md`**
— "Open-ended improvement must choose which questions, candidates, experiments, or proof paths to develop before decisive evidence about them is available; even a Gödel machine's proof gate retains this prior search problem."
"This is not merely an economic constraint": evaluation may be impossible before a candidate is formulated, not just expensive, so "More resources do not remove the need to choose a direction." "Acceptance quality bounds what survives after search; search allocation bounds what gets the opportunity to survive." Evidence for allocation can be weaker than evidence for adoption "without becoming irrelevant." The note explicitly says it "does not establish which search-allocation method works." Open: how to evaluate an allocation policy without exhaustive counterfactual search.

**`theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md`**
— "A search controller should be evaluated by the branches and probes it routes into stronger evaluation, not by treating every provisional judgment as an acceptance claim."
The evaluation unit is "the distribution of consequences produced by its routing decisions", compared against alternative controllers "under matched tasks, resources, and downstream evaluation." This does not require knowing the best branch. It gives an evaluation criterion for allocation judgments without numerical value estimates.

**`theory/failure-explanation-changes-later-branch-decisions.md`**
— "An explanation of a failed branch becomes operative search control only when its retention changes a later choice about scope, priority, probing, continuation, or abandonment."
This is a test for whether learning from consequences reached the allocation layer: "An explanation that leaves every later branch decision unchanged has not yet improved search control."

**`theory/program-theory-sustains-search-under-delayed-feedback.md`**
— "Holding a program's theory is tested by whether a partial, tentative account of what the program is for keeps modification search, backtracking, and recovery coherent until delayed evidence arrives."
Theory supplies program-specific search control: it narrows candidates, interprets results, separates evidence against a candidate from evidence against the theory, and directs recovery. On update bandwidth: "One surprising consequence read against a theory can single out a specific commitment as at fault and revise a whole region of that space at once. Where trials are few, slow, and expensive, that asymmetry is the regime argument for theory." This is a cost-regime argument for when theory-guided search beats mutation.

**`theory/system-use-selects-theory-fit-without-a-fixed-oracle.md`**
— "When no complete fixed oracle decides whether a claim belongs in a working theory, distributed consequences of live system use can provide an initial selection environment."
Fit is shown through a portfolio of consequences. One of them is whether a claim "reduces search, repair, or intervention relative to rival formulations." It acknowledges vulnerability to self-confirmation. This bears on acting despite uncertainty: claims are used before they are decisively evaluated.

**`theory/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`**
— "Theory-guided bootstrapping is a provisional first strategy under incomplete global evaluation, not a defense of continuing hand production."
"No present fixed evaluator fully decides whether a candidate claim improves the large-scale causal picture," so the first strategy is to use claims in a live system and "grow the selection machinery through use." It frames Commonplace's own strategy as an action taken under unresolved uncertainty.

**`theory/evidence/commonplace-revision-used-theory-guided-computational-search.md`**
— "A 2026-08-30 Commonplace revision shows retained project theory guiding computational search while the operator supplied decisive global-fit selection."
A bounded case of the split: model-mediated search guided by theory, with the human supplying decisive selection. It does not establish ablated causal effect.

### 2B. When to investigate further versus act; cheap error; stopping

**`theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md`**
— "Explains why a disposable local guess can rationally select the next probe when error is cheap and contained, while retained explanations need reach checks."
Three conditions make acting on a guess rational: fast cheap feedback, no reuse, and low coherence demands. Reach machinery "is priced for errors that can propagate." It compares a fast-feedback regime (guess, act, observe; failure mode over-ceremony) with a retention regime (derive, test, integrate; failure mode contamination). "The relevant choice is the cheaper error-control policy for the episode, not an automatic switch triggered by crossing one unnamed threshold." Reach checks sit at the reuse boundary (log versus note, workshop versus library, progressive constraining). With LLMs, "The scarce, expensive thing is no longer producing a plausible account ... it is deciding which accounts are allowed to persist." The conditions are continuous and no universal thresholds are given. Open: how to estimate the intermediate region.

**`theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`** (see 1C)
For direction 2 it supplies the bounded-probe definition ("state its cost, output, stop condition, and follow-on decision"), the requirement that a probe's possible outputs could change the decision, and a list of delay costs to compare. These are investigate-or-commit criteria without numbers.

**`theory/productive-deferral-requires-option-evidence-and-convergence.md`** (see 1C)
For direction 2, the discriminating-evidence condition is a qualitative value-of-information test: "If every possible result leaves the same action preferred, the delay or activity may produce information, but it does not make this decision better informed." The note also has explicit stop/return rules (convergence) and says deferral "can be the wrong choice" when delay costs dominate.

**`theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md`**
— "When a summary cannot license a reliability-compliant stop, the authoritative fallback remains in the path; only fallback work the summary removes can offset its own cost."
It sets out an explicit cost ledger: "read-cost value = fallback work removed − summary consumption cost," with a fixed cost currency. Sufficiency is relative to the four-tuple "(summary, source path, question, required reliability)". An orientation question can stop at an approximation, while an accuracy question cannot. This is a stopping rule for reading: further investigation is required until the answer licenses the action at the required reliability.

**`theory/agents-navigate-by-deciding-what-to-read-next.md`**
— "Models agent navigation as repeated follow/skip judgment under bounded context: cue diagnosticity must repay its own context cost."
Each pointer poses a follow/skip decision "under uncertainty because a cue predicts relevance rather than revealing it"; the reader compares "the expected benefit of following with the context and interaction cost of finding out." It grounds this in Pirolli's information-scent account. It is the KB's micro-level investigate-or-not model.

**`reference/adr/120-report-verification-selects-omission-questions-by-consequence.md`**
— "Report verification selects omission questions by the conclusions they could change, searches beyond cited paths while a consequential conclusion could still change, and stops when every question has a disposition."
This is a shipped search-and-stopping rule: "A search continues while further inspection is reasonably likely to change a consequential conclusion and the breadth of the claim it protects justifies the effort." A question can close with "an uncertainty compatible with the affected conclusion." It gives a qualitative value-of-information stopping rule in operational form.

**`reference/full-improvement-pass-closure.md`**
— "How the shipped full-improvement workflow reassays final note bytes, routes residual findings, and stops without claiming convergence."
The shipped workflow stops after one closing assay cycle with residual findings recorded. This is a fixed stopping rule chosen in place of convergence. (Read via the reflective-improvement-divergence problem map, not in full.)

**`theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`**
— "Loading writing methodology into an already-committed context window is expensive; a one-line log entry preserves the improvement signal at near-zero cost and lets a separate pass do the fix."
A local opportunity-cost argument: fixing a noticed improvement mid-task "costs more attention than the original task," so the improvement is deferred cheaply instead.

**`theory/intent-controls-choices-by-distinguishing-live-alternatives.md`** (see 1E)
"Sufficient to stop" is one of the outputs an intent controls, so stopping is an intent-governed choice.

**`work/reflective-improvement-divergence/problem-map.md`** and **`README.md`** (workshop)
The Gödel-machine section says the proof obligation "treats continued improvement search as an alternative action with opportunity cost, not as free background computation," and suggests "the halt/continue allocation is intrinsic to self-modification architecture." The README frames non-convergence relative to "the system's declared objective, assessment horizon, and opportunity cost." Open question 2 asks which non-convergence cases "impose enough opportunity cost to count as failure."

**`work/agent-curiosity-and-structural-coherence/curiosity-question-sources.md`** (workshop)
It lists "Inquiry allocation" as a question source: "Which possible question deserves scarce investigation effort because its answer could change a decision or discriminate important alternatives?" Its cross-cutting controls include "What is the opportunity cost of investigating it now?" and "If the inquiry stops, was it rejected, deferred for cost, or simply not reached?"

### 2C. Budgets, costs and resource formalisms

**`theory/cost-sensitive-formalisms-for-tentative-theory-search.md`**
— "Exploratory map of backtracking, learning, and complexity models that expose budgets relevant to search guided by tentative theories."
It lists budgets: search work, horizon, discrepancy, frontier memory, checkpoints, theory revision, evaluation, recovery, realized loss and human contribution. "These budgets need not collapse into one scalar ... a comparison could scalarize only the components for which an explicit exchange rate is warranted." It catalogues limited-nondeterminism classes, limited discrepancy search, iterative deepening, memory-bounded A*, real-time heuristic search ("prices provisional commitment, later retreat"), conflict-directed backtracking, mind-change bounds, pebble games, restart schedules, and budgeted MDPs and games. "Probability is optional at the architectural level ... Without probability, the same schedule can be evaluated by worst-case or adversarial cost." Scope: research leads that "require source grounding." It does not include metareasoning, value of computation or resource-rational analysis.

**`theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md`**
— "A procedure compiles its goal away, so a blocked step fails loud and hard; an interpreter holds the goal and re-routes, so failures are absorbed as a per-encounter tax on bounded capacity."
Unfixed defects in the interpreted layer act as "debt taxed per encounter" on context, attention and reasoning. "Maintenance is budget reclamation, not crash prevention." It adds a failure-economics criterion for codifying. "The budget claim is qualitative."

**`theory/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md`**
— "Proposal: distinguish context limits, reconstruction budgets, and the conjectured value of retained theories; trace strategy, effective context, and derived state remain unadopted terms."
An unadopted theory proposal. It separates resource conditions that require retained state from the conjecture that retained theories supply that state efficiently. Its adoption trigger is repeated need for the distinction.

**`theory/increasing-computational-autonomy-relocates-human-effort.md`**
— "In an open-ended system, increasing computational autonomy need not cut total human hours — attention moves to the frontier."
Mechanism: an elastic workload, because "An open-ended system has an unbounded backlog of possible improvements, so attention freed from routine work moves to work that previously went unattempted." Cites Bainbridge. It recommends ratio measures (improvements per human judgment). This bears on the README's weak point "the frontier does not shrink by itself."

**`theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md`**
— "When a system preferentially transfers decisions whose premises, criteria, and checks are available, the remaining human decisions become harder to warrant per decision."
This is a selection effect on what remains after routine conversion, so the residue is enriched for "unrepresented premises, unsettled criteria, weak checks, and delayed consequences." It bears on the same weak point.

**`theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`**
— "Error correction for LLM output is viable whenever the oracle has discriminative power (TPR > FPR) and checks are decorrelated — amplification cost scales with 1/(TPR-FPR)²."
It is the KB's one quantitative cost-of-verification relation. It bears on pricing how much checking a decision buys.

**`theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`**
— "For model-facing derived values, costly model-side recomputation shifts cache economics toward checked materialization, but persistence pays only when its total expected cost beats the alternatives and the copy substitutes for work."
An explicit cost comparison (store versus recompute), mainly retention economics (direction 5). Listed because it uses "total expected cost" comparison language.

**`work/cognitive-architecture-transfer-scan/parallel-terraced-scan.md`** and **`asmo.md`** (workshop)
These are candidate transfers. They define an "Exploration budget" reserved for alternatives without support yet, together with "PTS-2 — allocate by expected information gain, not only current relevance" and "PTS-3 — preserve an exploration quota." "ASMO-4 — evaluate attention by opportunity cost": evaluation should include "important candidates that lost and the work displaced by the winners." All are untested candidates.

### 2D. Value of information and observer-relativity

**`theory/information-value-is-observer-relative.md`**
— "Information value is observer-relative: prior knowledge, tools, compute, and goals determine extractable structure."
This is the only library note that names value of information (Marschak, Radner: "information has value only if it changes a decision") and bounded rationality (Simon: decision-makers "satisfice rather than optimize. The value of information depends on processing capacity"). It also cites relevance theory and Bayesian decision theory. It carries an explicit TODO: "This literature survey is from the agent's training data, not systematic." It applies the idea to retention and presentation for a bounded-context reader, not to choosing investigations.

**`theory/competing-causal-theories-can-guide-distinguishing-experiments.md`**
— "Why observationally equivalent mechanisms can tell a theory builder what to test next."
Retaining rival tentative theories specifies which intervention discriminates them. The design consequence is that "retained theories should help determine what evidence to seek next. When competing explanations matter to a decision, their disagreements should guide a feasible discriminating test." It cites Schmidhuber's compression-progress-seeking controller and separates "Choosing a promising test, measuring the resulting learning progress, and judging what its results warrant."

**`theory/warranted-reader-update-is-the-objective-of-substantive-writing.md`**
— "Defines epistemic interestingness as a relevant, warranted change relative to an intended reader's prior."
Workflow stages "earn their cost by improving the expected warranted update of the retained result." This is a value criterion for investment in writing stages, stated qualitatively.

**`work/conjecture-store/research-notes.md`** (workshop), §1 and §4
§1 principle 2: "A theory's value has three separable components: unification, discrimination, amortization." Principle 4: "Compression and any other cheap score route conjectures to criticism; they never accept them." §4 lists candidate evaluators for prioritizing conjectures, including discriminating-test yield ("Feasible, decision-relevant tests on which conjecture and incumbent disagree, priced") and bounded-reader task-cost delta. It flags a conjecture that premise reduction and discriminating-test yield are anti-correlated early, "any single scalar ranking systematically discards discriminators."

### 2E. Qualitative versus numerical judgment; the KB's position on expected utility

**`theory/prototype-standing-is-revision-cost-binding-plus-lost-investment.md`** (see 1C)
"There is no formula and no weighting; 'expected' means anticipated at assessment time, not probability-weighted." This is an explicit disavowal of an expected-value reading for a cost judgment.

**`theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`** and **`theory/productive-deferral-requires-option-evidence-and-convergence.md`** (see 1C)
Both take an economic source (Pindyck) and keep only its qualitative structure. "Those source-side relations neither test knowledge-base design nor supply a monetary or numeric Commonplace threshold." "The rule is qualitative." "It does not supply a portable quantitative threshold."

**`theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md`** (see 1E)
It is the exception that uses optimization and expected-return language without hedging: "an optimal allocation includes reflective investment for as long as its expected marginal net return exceeds that of competing uses of effort." It is stated conditionally, with no estimation procedure.

**`theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md`**
— "A Gödel machine admits self-rewrites through proof under its current formalization; this restricts admission without establishing how many useful changes are reachable or how reliably they are found."
It presents the formal limiting case where switching requires a proof of "greater expected utility than continuing the current search". The library uses it to show that even an expected-utility gate leaves search allocation unsolved, and that it is relative to axioms and a utility function.

**`reference/epistemic-stance.md`** (see 1A)
"Not inherited: The propensity interpretation of probability, verisimilitude measures." No positive stance on decision theory or subjective probability.

**`work/ideal-interpreter/resource-bounded-ideal-interpreter.md`** (workshop)
It considers "No ideal; class-declared bounded assessment instead," "following the move in Russell and Subramanian" (bounded optimality). A budget "alone does not specify the class." It declares objective, resource model and horizon, including the stopping rule. It is the only workshop applying bounded optimality.

**`work/cognitive-architecture-transfer-scan/synthesis.md`** (workshop) (see 1E)
"Selection values are not one number": expected utility is one of several values that should stay typed. It argues against collapsing them into a single score.

**`theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md`**
— Table row: "Attention economics (Simon) | Decision-maker | Attention (soft) | Satisficing, filtering".
Simon appears as a source tradition for context-engineering strategies under soft bounds. It is a mention, not a treatment of satisficing.

**`theory/learning-is-not-only-about-generality.md`**
— "Per Simon, any capacity change is learning."
Uses Simon's definition of learning, not bounded rationality. Listed so the parent does not mistake it for a bounded-rationality treatment.

### Not found (direction 2)

- **Metareasoning / value of computation** (Russell–Wefald, Horvitz): no note, no ingest. The nearest are the Gödel-machine notes (switch-versus-continue as an expected-utility proof) and the cost-sensitive-formalisms catalogue, which lacks these frameworks.
- **Resource-rational analysis** (Lieder–Griffiths): nothing.
- **Satisficing** and **ecological rationality / fast-and-frugal heuristics** (Simon, Gigerenzer): only one-line mentions (`information-value-is-observer-relative.md`, `soft-bound-traditions-...md`). No note on aspiration levels or heuristics as rational under bounds.
- **Opportunity cost** as a concept: no library note. It appears only as a comparison currency in `opposed-recompute-factors-do-not-decide-documentation-segmentation.md`, plus workshop mentions (reflective-improvement-divergence, curiosity question sources, ASMO-4).
- **Value of information** as a decision rule: no library note applies VOI to choosing investigations. It appears as named prior work in `information-value-is-observer-relative.md`, and in qualitative form as the discriminating-evidence condition of productive deferral and the ADR 120 stopping rule. A general "investigate while the result could change the decision" principle is stated locally in several places but has no note of its own.
- **Explore/exploit**: no library note. Exploration quotas and bandit framing appear only in workshops (parallel-terraced scan, conjecture-store §5).
- **A general account of when to stop investigating and act**: only local rules (ad-hoc regime, summary sufficiency, ADR 120, convergence rules, full-pass closure). There is no unifying note.
- **The KB's explicit position on expected-utility reasoning**: no dedicated statement. The de facto position, found across notes, is qualitative criteria, "no portable threshold", budgets not collapsed into one scalar, and "expected" glossed as "anticipated, not probability-weighted". The machinery-investment note is the exception and uses expected-return language.
- **Bounded optimality** in the library: the ingest recommends updating `the-deployed-system-not-the-model-is-the-unit-of-learning.md` to use it, but no theory note cites the ingest. Only the ideal-interpreter workshop does.

### Sources (direction 2)

Ingested:
- Russell & Subramanian, *Provably Bounded-Optimal Agents*: `sources/provably-bounded-optimal-agents.ingest.md`. This is bounded optimality, not Russell–Wefald metareasoning. No theory note cites it.
- Pindyck on irreversibility and option value: `sources/pindyck-irreversibility-uncertainty-investment.ingest.md`.
- Pirolli on information scent (information foraging, with a random-utility rule): `sources/pirolli-proximal-information-scent-distal-content.ingest.md`. Its description says it "grounds the KB's pointer-quality and stopping claims".
- PrimeScientist (budget-sensitive allocation between planning and execution): `sources/primescientist-research-effort-allocation.ingest.md`. It is useful evidence for controller evaluation. Only `work/decision-lifecycle-evidence/trace-derived-system-scan.md` cites it.
- Model Discovery Agent (Bayesian value of information for experiment selection; "value-of-information acquisition is not always better than LLM or random acquisition"): `sources/model-discovery-agent-bayesian-experiment-design.ingest.md`.
- AERA bounded recursive self-improvement ("allocates computation among concurrent jobs by predicted value"): `sources/bounded-recursive-self-improvement.ingest.md`.
- Epiplexity (information for computationally bounded observers): `sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md`.
- Schmidhuber, compression progress (curiosity as seeking expected learning progress): `sources/driven-by-compression-progress.ingest.md`.
- Set-based design and adaptive planning: `sources/kennedy-sobek-kennedy-set-based-rework.ingest.md`, `haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md`, `githens-manage-innovation-programs-rolling-wave.ingest.md`, `pmi-lexicon-project-management-terms-v4.ingest.md`.
- Teevan orienteering (local steps versus direct jumps in search): `sources/teevan-perfect-search-engine-orienteering.ingest.md`.

Not ingested:
- Herbert Simon (bounded rationality, satisficing). Cited only from training data in `information-value-is-observer-relative.md`. The `simon-*` hit in sources is Simon Willison.
- Russell & Wefald (metareasoning, value of computation).
- Horvitz (bounded rationality, decision-theoretic control of computation).
- Lieder & Griffiths (resource-rational analysis).
- Gigerenzer (ecological rationality, fast-and-frugal heuristics).
- Marschak/Radner and Howard value of information. Cited only from training data.
- Peirce, economy of research. Cited only in `candidacy-evidence-licenses-escalation-not-acceptance.md`.
- NASA SE Handbook §6.8 (trade studies, value of information). The attempted ingest was blocked, per `work/design-space-studies/README.md`.
