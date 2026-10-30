# Search results: directions 4 and 6

Raw material for the reconciliation map. Search worker output, 2026-10-30.
Coverage and summary only. Whether the economic framing adds anything is
not judged here. Paths are relative to `kb/` unless they start with
`AGENTS.md`. "(description only)" means the body was not read beyond its
opening and the summary rests on the frontmatter and first paragraph.

---

## Direction 4: general operations for open-ended work

### 4.1 The theory-refinement interface (the starting interface)

**work/theory-refinement-interface/README.md**
First sentence of Goal: "Reconcile the interface investigation, which proposes derive, compare, locate, revise, evaluate, and apply as the operations any theory-refinement machinery must implement, with the established theory-refinement literature, without claiming the generic refinement loop, tentative theories, or revision search as new."
- Gives the reason for the work. In a symbolic system the operations have mechanically assigned semantics. In a model-mediated system they are interpreted and therefore fallible. Codification moves particular operations back from interpreted to mechanical. The README calls this "Commonplace's own construction" and a candidate article once grounded.
- Claims flagged as needing source and mechanism checks: (a) every operation is available for any readable representation; (b) the interpreted update space is open; (c) certain classical results transfer at task level.
- Closing conditions: (1) each of the six operations gets a task-level description separate from any implementation guarantee, naming the classical result it restates and when the restatement holds. "A trace identifies candidate repair locations without guaranteeing a unique fault; a particular search algorithm's local-optimum result is not a theorem about all implementations of the roles." (2) The source-check claims are checked against completed ingests: EITHER, FORTE, AGM and belief-base papers, assumption-based TMS, and knowledge-engineering method-construction papers. Each claim is kept, narrowed or dropped. (3) The result is folded into the addressable-theory definition or promoted as its own note. It must not define theory-builder membership.
- State: posed 2026-09-17 as closing condition 3 of the theory-builder workshop. Write scope is the directory only. It explicitly does not depend on the ideal-interpreter workshop.

**work/theory-refinement-interface/theory-refinement-interface.md**
Status line: "Working document, 2026-09-09." The framing came from an operator conversation with Codex.
- **The operations.** "Theory refinement specifies an interface. A theory together with its machinery implements it; the theory file alone does not." The core table lists five operations, each with the question it answers. **Derive**: what does the theory imply for this case? **Compare**: where does that consequence disagree with the evidence? **Locate**: which assumptions, rules or scope conditions are candidate sources of the disagreement? **Revise**: change the selected parts. **Evaluate**: does the revision correct the errors while preserving useful behaviour on the tested cases? **Apply** is added as a sixth operation that the builder needs beyond the interface: "the builder's contract is the refinement interface plus **apply**." Loop closure is the requirement "that apply and compare share a case."
- **Why it matters.** Horn clauses with proof are only one implementation; equations, programs and structured prose with an interpreter are others. "To use the classical theory-refinement results, we do not need Horn clauses. We need to define our theory machinery so that it implements the interface for our representation, and then say which results carry over and under what conditions."
- **Implementations.** One table compares four implementations per operation: EITHER/FORTE, the universal theory manipulator, a general interpreter, and Commonplace today. The universal theory manipulator is "derive-only". The general interpreter "implements all five by interpretation. Every operation is available for any representation the model can read, and none carries the classical guarantee." Codifying back "moves one operation for one part from interpreted to mechanical". For example, a validator makes compare mechanical for its claims, and a schema makes locate mechanical for its fields.
- **Addressability scale.** For each operation, record whether it is mechanical, interpreted or unavailable. FORTE is mechanical on all five operations. A prose note is interpreted on all five. Each codification can then be recorded as a move on this scale.
- **Results that transfer.** At task level: no unique fault, so locate yields candidates; revision is not guaranteed minimal and evaluate can stop at a local maximum; acceptance is fit with the tested cases ("the floor, not the ordering"), with reach as the ordering; the update space is fixed by the operators in classical systems but open for an interpreter, "which removes this limit and removes the guarantee that came with it." Only as hypotheses: revision beats induction when the initial theory is approximately right (FORTE bounds this: with 100 examples and eight errors, induction did better), and relational path finding was needed to escape plateaus. The proposed discriminating test is FORTE tasks stated in prose and repaired through the interpreter.
- **Commonplace mapping.** For each operation the document records what performs it, the record that it ran, the classical result that applies, and whether the operation was checked to be right. In the profile table, the "right" column is mostly "none routine", "partition rerun only" or "by hand". Two findings: "Most cases are criteria, not observations, so the loop as run is a quality loop over the theory's expression more than an empirical loop over its content". The one documented classical failure, a local maximum of the gate set that produced the refuter and citer guards, is "some evidence that the placement is right."
- **Eight open questions.** Is compare separate? What does locate require of an interpreted theory? What does evaluate need, and is reach a separate operation? How is "implements the interface for a family" certified (fault injection)? Does apply belong inside the interface? Where is the interface written? Which classical results do we actually want? Are cases that are criteria legitimate? Every operation in the document is framed for theory refinement. No other domain is discussed.

**theory/definitions/addressable-theory.md**
"Definition — an addressable theory is a theory formulated in language whose assumptions, scope, and parts can be inspected and revised individually; a graded structural property, separate from tentative status."
- This is the theory-side contract that the interface document compares with the repair interface. It supplies parts as candidate repair locations, which can be revised separately. Assigned consequences, a separate axis, decide whether a contradiction can be mechanically checked.
- "A located part is a candidate": a failure rarely identifies one faulty commitment. It cites EITHER and FORTE as "the fully addressable case with computed consequences". It takes "neither its paradigm nor a preference for minimal revision from them."
- The definition does not yet contain the interface section that the workshop might add.

**theory/definitions/theory-builder.md**
"Definition — a theory builder applies conjecture and refutation to stated theories: it acts on them, criticizes what they say, and lets the result shape the next round; addressability and persistence are graded."
- Its Boundary section lists the builder's operations, which differ from the six-operation interface: "noticing a problem in its own theories or work, proposing a theory, deriving what it implies, criticizing it, choosing what to blame, producing a revision, selecting the theory to keep, and changing the machinery that does these things."
- "The boundary follows the operation, not the person". The builder is whoever performs these operations. This operation list also decides who counts as inside the builder in the testing article.

**theory/theory-building-has-distinct-precedents.md**
"Conjecture and criticism, causal self-representation, and persistent artifact editing supply different precedents for a theory builder's operations; similarity on one does not establish the others."
- Splits the question into three: how errors are criticized (Popper), what the representation is about (reflection), and how changes persist (retained text and code around a fixed model).
- EITHER and FORTE are precedents only for "connecting failed consequences to candidate repair locations". They do not establish the same capability for interpreted prose.

**work/ideal-interpreter/README.md**
Goal: work out whether a language model can be modelled "as an interpreter of semantics the way an abstract machine models a computer".
- Bears on direction 4 only by boundary. The theory-refinement-interface workshop "owns the operations a refinement machinery implements; this workshop does not define the interpreter through those operations."
- Rated too experimental for anything to depend on.

**theory/definitions/discovery-lifecycle.md**
"Definition — the discovery lifecycle is an ideal-type six-phase evaluation of an ampliative conjecture."
- A second six-step operation sequence, mapped to KB operations: observation/anomaly (capture without granting rule authority); conjecture (abduction); consequence derivation (deduction); test/accumulation (induction: compare consequences with cases); acceptance (gated commitment with a declared boundary and maintenance regime); integration (reconnect prior evidence, update affected artifacts).
- The idealization is defeated if the phase boundaries stop predicting different evidence, authority or maintenance obligations, "or a rival model that explains those obligations better". The KB does not reconcile it with the derive–compare–locate–revise–evaluate interface.

**theory/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md**
"With models pinned, newly acquired theory-use procedures must persist outside their parameters; existing general machinery may already supply them..."
- A house needs operations "that select relevant commitments, derive consequences, check changes, notice contrary evidence, and revise the account". A theory text does not perform them.
- Directly relevant to reuse: "A fixed interpreter can also apply many new theories through the same retrieval, graph traversal, and checking tools. Their reuse can make a new theory sufficient as the only retained change."
- The relevant limit is the effective update space. "An operation that is possible but too costly is different from one the permitted machinery cannot express. Both can motivate extending the machinery, but they require different evidence." This is the closest library statement of the brief's split between expressing a procedure and economy.
- Codification becomes necessary "only when it is needed to meet the declared outcome and resource limits and no permitted alternative does so. There is no general threshold at which every growing theory must become code."

**articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md**
"Lead article: bets that a fully automated theory builder that learns... can be built from fixed-weight LLMs."
- Lists the functions the loop needs, which "current LLMs appear capable of": formulating and reformulating problems, generating tentative solutions, deriving consequences, criticizing alternatives, designing and interpreting tests, revising explicit knowledge, and using retained knowledge in later work.
- This is a capability list, not a composable interface. Its use for direction 4 is as a third candidate operation list.

### 4.2 Other operation sets, interfaces and their limits

**theory/instructions-are-typed-callables.md**
"Skills and tasks are typed callables — they accept document types as input and produce types as output, and should declare their signatures like functions declare parameter types."
- Proposes type signatures for KB procedures, for example `/ingest: source → source-review`, `/connect: note | index → note | index`, `/validate: note → validation-report`.
- "The type is the interface; the implementation can codify from LLM to code as patterns constrain." This is the KB's nearest procedure-composition proposal for knowledge-work operations in general, but it is about type-checking skill inputs. It does not claim that a small set of operations is sufficient.

**theory/context-operation-interface-bounds-context-policy.md**
"Explains why improving context selection within a fixed operation interface cannot establish that the interface admits every useful active-context projection."
- Formalizes `Reach(I, S, x; M, B)` as the views obtainable through legal traces of an interface `I`, whose operations include locate, expand, transform, summarize, filter, delete and expose. "A better policy may choose useful traces more often... Those gains do not add a view outside `Reach`."
- Bears on the expressiveness question. An operation set bounds what any policy over it can do, and gains under a fixed set "do not establish that excluded operations are unnecessary." Its comparison cases are RLM and lambda-RLM's "small typed com[binator]" set, and JAZ versus Letta.

**theory/reflective-coverage-is-graded-across-representational-forms.md**
"Reflective coverage is stated per represented form and operation profile..."
- Defines a four-operation profile over the system's own components: observation, selection, configuration, modification. "The four do not form a ladder": no operation confers another, and counting them "gives an order but not a measure".
- This is a small-operation-set account in the reflection domain, with an explicit argument against scalarizing it.

**theory/areas-exist-because-useful-operations-require-reading-notes-together.md**
"Explains why orientation and comparative reading need bounded, sufficiently related note sets..."
- Names two KB operations, orientation and comparative reading, whose output comes from relationships among notes and which "one-at-a-time retrieval cannot perform".
- The point for direction 4: some operations need a read-together set under bounded context. Composition at the level of operations has a context-cost precondition.

**theory/types-give-agents-structural-hints-before-opening-documents.md**
"Types and descriptions let agents make routing decisions without loading full documents — the type says what operations a document affords."
- Treats types as declarations of the operations a document affords, for example a `spec` can be implemented from and a `structured-claim` carries a citable argument. These hints are meant to inform routing decisions before loading.

**theory/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md**
"Distinguishes four use-time requirements for remembered knowledge—discoverability, loadability, composability, and calibrated trust..."
- "Composable" here is a property of knowledge, not of operations. A loaded representation needs "enough structure to combine with task context and other memories in reasoning or action". The failure mode is "isolated memory".
- Relevant as the KB's standard sense of "composable", which a direction-4 operation interface would sit beside.

**theory/short-composable-notes-maximize-combinatorial-discovery.md**
"The library's purpose is to produce notes that can be co-loaded for combinatorial discovery..."
- Cites Parnas and the Unix philosophy ("do one thing well, compose through pipes") as prior art for composable units. Its motive is bounded context: "co-loading capacity [is] the scarce resource".
- This is composition of content units, not of operations.

**theory/evolving-understanding-needs-holistic-rewrite-not-composition.md**
"Holistic rewrite shifts reconciliation from each consumer to the author, but only when the whole-picture narrative can fit within effective context..."
- A counterweight to composition. "A note graph distributes knowledge across composable fragments". When the consumer needs a coherent whole and fragment reconciliation costs more context than the task has, a pre-reconciled narrative is better.
- It names architecture exploration and incident investigation as examples. This bounds when composable pieces are economical.

**theory/memory-design-adds-operational-axes-to-artifact-analysis.md**
"Memory design needs operational policy axes (capture, derivation, activation, authority assignment, lifecycle, evaluation)..."
- A provisional operational checklist for memory comparison. "an operational axis is a recurring comparison question, not a claim that the questions form a uniquely exhaustive or pairwise-independent basis."
- This is a hedging precedent for any claimed operation set.

**theory/scenario-decomposition-drives-architecture.md**
"Deriving architectural requirements by decomposing concrete user stories into step-by-step context needs — not from abstract read/write operations..."
- Criticizes operation-first design. "The right unit isn't 'read' or 'write' — it's a complete user story with its full chain of agent actions." Its worked stories are write a note, ingest a source, respond to a change, and answer a question.
- This rivals deriving architecture from a small set of abstract operations.

**theory/bounded-context-orchestration-model.md**
"Defines the formal computational model with the LLM inside — a conditional batched select/call form for closed-world LLM orchestration..."
- Six elements: scheduler state `K`, call specification `C`, batch `B`, `select(K)`, `call_all(B)`, `transition(K,B,R)`. This is a minimal operation vocabulary for the computational substrate, not for knowledge-work semantics.
- "The form represents qualifying workflows; it does not rank orchestration architectures."

**theory/compiling-coordination-preserves-primitive-not-aggregate-authority.md**
"Compiling a coordination strategy preserves the primitive action alphabet but expands aggregate authority..."
- With a fixed primitive alphabet, composing primitives in compiled code adds no new primitive effect channel. It does expand aggregate authority: "'Delete one file when asked' and 'delete files in a loop until the tree is empty' are the same primitive and wildly different authorities."
- This is a cost of composability that is invisible at the level of the primitives.

**theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md**
"Why optimization cannot repair consequential distinctions, responses, or mappings outside the effective update space of a fixed task decomposition."
- Three omissions make corrections unreachable: information, action-closure and hypothesis-class omissions. For action closure: "if the learner can implement it exactly and reliably by composing its available actions, then the response remains inside its effective space. If only a costly or approximate construction is available, the decomposition may impose a sampl[e cost]..."
- This is the KB's general statement that a fixed operation set limits learning, and that composability differs from economical composability.

**work/agent-runtime-design/runtime-minimality-is-a-protected-waist-not-a-small-feature-list.md**
Working thesis: "An agent runtime should be minimal in the number of **semantic commitments it fixes**, not in the number of functions it implements."
- Boundary test: a responsibility belongs in the protected runtime "when an extension cannot implement it without gaining the ability to bypass it, corrupt shared execution state, or break guarantees across suspension and recovery. Everything else should remain replaceable strategy."
- Splits mechanism from policy per component: scheduler, context engine, execution substrate. Model-authored guest programs extend the runtime under explicit authority, isolation and provenance.
- This is a workshop thesis, not library. It is the KB's closest "small shared core plus domain extensions" design, but at the runtime layer, not the knowledge-work layer.

**work/change-operations-catalogue/README.md and catalogue.md**
Governing question: "Which operations change Commonplace, and what must each read first?"
- Lists 18 observed change operations plus candidates, for example altering a collection contract, a type spec, a validation check, a review gate, a skill, the link vocabulary or a decision. "An operation enters it only when an observed instance... shows the system being changed that way."
- No completeness mark. "An operation missing from the list is not evidence that it does not exist."
- This is an empirically grown operation list for the system's own change operations, not a claimed composable basis.

**theory/maintenance-operations-catalogue-should-stage-stable-procedures.md**
"Catalogue of periodic KB maintenance operations and readiness status, used as a staging ground before promotion into kb/instructions procedures."
- Promotion pipeline: capture after first use, re-run in varied contexts, mark ready "when inputs, outputs, and decision points are stable", then rewrite as an instruction.
- This is a procedure-maturation path, not an operation set.

**theory/brainstorming-how-to-enrich-web-search.md**
"Design exploration for enriching web search by reusing /connect's dual discovery and articulation testing on results..."
- Claims a KB operation is reusable across corpora: "`/connect` is corpus-agnostic — it runs the same dual discovery, articulation testing, and synthesis detection regardless of what documents it connects."
- It proposes applying the operation to a temporary research corpus, while admitting that phase 3 goes beyond pure reuse. This is an unevaluated brainstorm. It is the one KB example of proposing to reuse an existing operation in a new domain (research or web search).

**reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md**
"Decision that a subdirectory never carries binding rules: rules about a kind of artifact live in its type spec, rules about location in COLLECTION.md, and lifecycle operations in instructions the type spec names."
- Places operations architecturally. Type specs state invariants and name their lifecycle-operation instructions, and instructions state the steps.
- This is how Commonplace currently packages "operations" (per-type lifecycle instructions), not as a shared generic set.

**theory/definitions/actionable-methodology.md**
"Definition — actionable is a relation a methodology stands in... relative to an operator, available operations, a target system, and a s[etting]."
- A methodology is actionable for an operator "when that operator can use its mapping to choose among available interventions in a target system."
- This ties any operation interface to actionability. The same methodology is actionable or not depending on the operations available.

### 4.3 Domains beyond theory building

**theory/legal-drafting-solves-the-same-problem-as-context-engineering.md**
"Legal drafting parallels context engineering because both write ambiguous natural-language specifications for judgment-based interpreters, but law develops constraining more than codification."
- Shared structure: "a spec in a language with irreducible ambiguity, interpreted by a processor that must choose among multiple reasonable readings". Common-law precedent fuses resolution and constraining; civil law lacks that feedback loop.
- "Statute codification is stronger constraining, not KB-codification." "law shows that a domain can develop sophisticated constraining methodology while doing almost no codification".
- This is the only legal-domain note. It treats law as a parallel source of technique and does not express legal drafting through any operation set.

**articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md**
"Supplement: the automated software house conjecture (2026-09-02 fixed models) as a second test of a theory builder..."
- The software-domain case. Program theory as commitments, for example "a person's identity is separate from their membership in an organization" and "tenants never see each other's data". These "keep the search for a design coherent while the consequences of a choice are still unknown."
- Software gives a stronger falsifier: tests, builds and releases are judged outside the house. "The price is the claim": open-ended coherent change cannot be established by a finite run.
- A witness must show four things: holding and application, coherent revision, automated continuation, and practical reliability. It is kept as "a companion, not the main path."

**theory/program-theory-sustains-search-under-delayed-feedback.md**
"Holding a program's theory is tested by whether a partial, tentative account... keeps modification search, backtracking, and recovery coherent until delayed evidence arrives..."
- The software-architecture domain. Naur's coherent-modification test meets the residue argument. "the least-warrantable decision in that residue is which change preserves the program's structure and purpose."

**theory/addressable-theory-can-coordinate-heterogeneous-factory-development.md**
"Tentative natural-language project theory may provide an addressable way to coordinate heterogeneous factory development..." It carries a TODO to switch to software-house vocabulary.
- One failure symptom in software production can come from any of eight artifact kinds: task understanding, decomposition, context selection, representation, tool, evaluator, workflow, or conflicting schemas. "A fixed update operator for one artifact kind may repair the local symptom while leaving the shared explanation inconsistent elsewhere."
- The contingent hypothesis is that one addressable theory coordinates changes across artifact kinds. This argues against artifact-kind-specific operations in favour of theory-mediated cross-artifact revision.

**theory/new-domains-can-turn-theory-builders-into-software-houses.md**
"A persistent automated theory builder for external users becomes a software house when genuinely new domains require it to revise the software that performs t[heory building]."
- Splits the semantic operations models supply ("interpreting claims, comparing explanations, proposing counterexamples, and revising scope") from software operations: corpus, exact state transitions, scheduling, checks, indexes, rollback.
- "New domains can bring new manipulation requirements as well as new content", for example snapshot pins and validators.
- Refuter stated: "A sufficiently general fixed harness might sustain theory building across genuinely new domains without requiring demand-specific machinery changes." Whether this happens is an empirical issue: do new domains "repeatedly expose production requirements that were not economically or practically anticipated in the fixed substrate"? This is the most direct library statement on whether a fixed shared operation set suffices across domains.

**theory/task-families-and-product-families-classify-different-things.md**
"Task families group obligations or evaluations; software product families group products through declared commonality, variability, and reusable production scope."
- A task family can span many product families. For example, "Tasks requiring map-reduce over intermediate results" groups many domains because they "stress the same computational strategy".
- This is a vocabulary for saying which grouping an operation is reused across.

**theory/competing-causal-theories-can-guide-distinguishing-experiments.md**
"Why observationally equivalent mechanisms can tell a theory builder what to test next..."
- The scientific-investigation case. Retaining two observationally equivalent causal theories can guide which intervention to run, because their disagreement specifies the next test. It uses structural-causal-model semantics and a constructed XOR example.
- This is evidence-acquisition planning, not an operation set.

**theory/first-principles-analysis-maps-design-space-before-selection.md**
"Why deriving independent choice dimensions from boundary constraints exposes rival designs that inherited solution categories hide."
- The design-exploration case. "Exploration over decompositions must precede optimization within one". A design space is "generated rather than catalogued" from boundary constraints.

**work/epistemic-architectures/README.md**
Compares the epistemic architectures of six research systems: Commonplace, Eigenius, ScienceFlow, AI Research OS, an anonymous ontology draft, and the ARC skill.
- Relevant as the KB's broadest cross-system evidence on research and exploration domains. ScienceFlow is ML research. The ARC skill is a game-solving harness with "pre-action admission, post-action consequence grading... halt-on-surprise execution", the nearest the KB comes to an exploration domain.
- The system-level response taxonomy "failed unchanged" on ARC, and comparison moved to route-level authority. This is a cautionary case for one general classification across domains.

---

## Direction 6: why this is an economical architecture for Commonplace

### 6.1 Stated strategy and its reasons

**AGENTS.md (Repository Overview and Development)**
"Commonplace is a framework for agent-operated knowledge bases: methodology, types, instructions, skills and Python commands. This repository is itself a KB; its methodology is its content."
- Strategy line: "Develop it through use: retain observed limits, revise the methods and record episodes as research evidence."
- Related rules: "YAGNI: record unneeded features or gaps instead of implementing them", and "No backwards compatibility without a consumer need." These are standing policies against speculative shared abstraction.

**index.md (public landing)**
"Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**."
- Two goals: a practical LLM wiki, and the theory builder as "a new learning paradigm". "The goals reinforce each other, because memory is always about learning". Real use of the wiki "supplies the problems and criticism a theory builder learns from."
- Reflection is "the core of the method", "so an improvement to the method is reused by all later work. People still perform many of its operations; the work is moving them to computation." Also: "No test of the bet has been run yet."

**theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md**
"Commonplace builds a system meeting the theory-builder conditions and tests whether it learns..."
- This is the research-program note. The development path is reflective from the start, and "people perform many of its operations until they move to computation." It rests on the return to investing in the method, which "requires method changes to compound".
- Why start from a working system: "a bootstrap is the running system itself, so starting from a working system supplies that stream from the first day, with people supplying the functions not yet automated". "Sustaining that requires a system people want to use, so that the judgments are part of work they would do anyway." The stated price is warrant.
- Codification policy: "Codify parts when their intended meaning and operation become sufficiently clear and the commitment is useful." Codification can follow learning part by part.
- Three conjectures: criticism of content against trial and error; addressability against coarser builders; persistence against reconstruction. The persistence conjecture is explicitly economic: "Keeping more of the work of conjecture and criticism... may reduce cost at comparable decision quality". "Retention may save reconstruction, but still requires retrieval, interpretation, and maintenance. Compare total cost at comparable quality and quality under matched budgets." Scope: "None of these advantages is established."

**reference/commonplace-as-an-instrument.md**
"What the KB application is for in Commonplace's design program — composition test, two worked provenance instances, and the transfer evidence the repository does not have."
- "The KB is not the boundary of the program. It is the first worked case in which the design's theories... meet real operating constraints *together*".
- Declared objective: "more useful and better-warranted knowledge work per unit of human judgment spent. Not automation."
- Use tests composition, and composition failure counts as evidence against design theories. The tag-readme trace is one pathway, and it "licenses replay in this repository. It does not license the rule."
- Evidence that would change the status: close the two rationale TODOs with outcomes; an outside assessment, where someone outside reuses a decomposition; a faithfulness test by intervention; and more than one composition failure attributed back. "Disciplined transfer has not been demonstrated."

**articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md**
(Also under 4.1.) This is the public statement of the bet.
- Strategic argument, "Formalize it, or leave it to people": the choice between formalizing and leaving work to people omits a middle. Constraining is a gradient, and an LLM can interpret the middle. "Parts that stop changing can be codified afterwards, one at a time". Stated costs: interpreters fail open, constraining can go too far, and the proof guarantee is lost.
- Why reflection: "an improvement to the method is paid for once and reused by every later learning episode." Under the Bitter Lesson, the relevant distinction is "between **human-supplied knowledge** and **automatically generated, tested, and revised knowledge**", with the bootstrap condition attached.

**articles/bootstrapping-an-autonomous-theory-builder.md**
"Bootstrap supplement: Commonplace starts as a reflective theory builder in which people perform many operations, moves them to computation one at a time, and measures succ[ess]..."
- Why bootstrap rather than design whole: "Designing such a builder whole would require knowing in advance how computation should perform each of these operations, and we do not know that."
- Two routes for moving a repeated operator judgment: codify it, or delegate it to the LLM under a retained procedure. "These are different changes". Functions can move back.
- Let the builder build its own software: "General learning may even require this ability, if new theories keep creating new ways to test, organize, and apply knowledge."
- Measure and failure condition: progress is "the number of human decisions each completed, verified improvement requires". "The conjecture fails... if that number grows as the system grows." The strongest evidence is a removal test.

**articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md**
(Also under 4.3.) For direction 6, it explains why the KB comes first: a house's seed "must already be a working house", whereas the KB "can start from an existing builder staffed by people and agents and move its roles to computation one class at a time."

**articles/testing-whether-a-theory-builder-learns.md**
"Testing supplement: show that a theory builder's retained revisions causally improve later capacity..."
- The adopted sufficiency hypothesis bears on cross-domain reuse. The builder must develop theories "across declared practical areas" "without people performing its internal theory-building roles or designing a new learning method for each area". It is "Refuted... by a builder that reaches the target only with a person in an internal role, or only after a new learning method is designed for an area".
- The comparative hypothesis says gains over a frozen seed and a raw-record baseline "account for both adaptation and task costs". The reflection hypothesis has a stated refuter. "No run has been performed."

**theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md**
"A machinery improvement is paid for once and reused by every later learning episode, so over a long horizon its return can exceed immediate learning..."
- This is the KB's existing economic argument for the strategy. "Immediate learning yields one result; a machinery improvement yields a stream of results". An optimal allocation includes reflective investment "for as long as its expected marginal net return exceeds that of competing uses of effort". "The allocation is not fixed."
- Conditional on three things: improvements can be found and assessed; their benefit persists; and their net return exceeds alternatives. "Harder problems, resource limits, and maintenance costs can erode the return."

**work/commonplace-nearest-constructions/landscape.md and README.md**
Treats Commonplace as three objects: the human-inclusive theory builder today, the development path, and "the conjectured computational theory builder that is also a software house."
- Working program thesis, "theory building and software building converge": an open-ended theory builder "will eventually encounter material its current software cannot represent, retrieve, compare, test, schedule, or govern". Bringing that function inside makes it a software house. "This is a working thesis about open-ended operation, not an empirically established inevitability."
- The landscape table places neighbours (Ars Contexta, AI Research OS, GBrain, Eigenius, ScienceFlow, Fluent, Wheelhouse, Exo and others). It records that in each the operator or a fixed design supplies generalization or admission.

**work/dsw-talk/development-implications.md**
"The talk suggests that Commonplace's next development should be an **observable reuse loop**." This is a workshop conclusion.
- The missing layer is an end-to-end path from raw observation through candidate, review, disposition and cold-session reuse to measured effect. "Do not define a universal candidate schema, queue service, or automatic promotion mechanism before several real episodes show which fields and transitions recur."
- The talk's core claim: reliability comes from a hybrid design in which "stable and checkable rules move into deterministic machinery".

### 6.2 Universality and generality claims

**theory/universal-software-factory-needs-a-declared-universality-axis.md**
"Universal software factory is ambiguous unless the universality axis, covered class, supplied inputs, adequacy relation, and resource bounds are declared."
- Four independent axes: target or platform portability; factory-valued output; constructional expressivity; and production-knowledge acquisition reach. "Constructional expressivity also becomes weak when the supplied description may contain the complete target."
- A qualified claim must declare the axis, class, supplied inputs, adequacy relation, learner and human boundary, horizon and resources, and how failures are counted. "Without these declarations, *universal* can collapse into ordinary portability, recursive output, compiler expressivity, or an untestable promise of arbitrary task competence."
- For the program: "as covered demands widen, computation should increasingly acquire and retain the family-specific production knowledge required for later production rather than receive another bespoke human design." "A fixed general substrate remains compatible with that claim."

**theory/agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md**
"Maps the bounded-call agentic substrate to Greenfield's software-factory ontology without calling every generic harness or generated program a factory."
- Schema `F_P = configure(G, K_P)`: general machinery `G` plus family-specific production knowledge `K_P`. "One substrate can host, select, compose, or help construct several factories."
- "Calling the general substrate one universal software factory would hide this distinction." Task-local software is not factory machinery without reusable family scope. This is the library's closest formal form of "shared substrate plus domain-specific extensions".

**theory/broad-software-demands-create-pressure-for-agentic-factory-development.md**
"Broad software demands make exhaustive predefinition of useful family-specific production machinery practically implausible..."
- "This is a claim about engineering adequacy and scaling, not an impossibility theorem". As demands widen, "exhaustively anticipating and maintaining all useful family-specific production knowledge becomes increasingly implausible and expensive."
- Three cases: configuration, construction, and acquisition. "The practical generality claim concerns the third case. A system does not meet it by hiding a target-indexed catalog of handcrafted factories inside its supposedly general substrate."

**theory/factory-construction-does-not-establish-knowledge-acquisition.md**
"Recursive software-factory construction is prior art, but the demonstrated constructors receive the family definitions, metamodels, mappings, and expertise..."
- Greenfield's factory-building factory, Cook and Kent's Tool Factory and MDSoFa all build factories from supplied family knowledge. "A constructor can be highly expressive on the first problem while doing nothing on the second."
- This is prior art for why reusable machinery for building machinery is not by itself general.

**theory/definitions/software-house.md**
"Definition — a software house is the complete persistent system responsible for developing and evolving software for external users."
- Includes every role-filler, human or computational. "Persistence alone establishes neither retention nor learning." An automated house performs every internal production role computationally.

**theory/definitions/software-factory.md**
"Definition — in the Greenfield lineage, a software factory is a configured family-specific software-production environment."
- "The declared product or solution family is part of the factory's identity." A generic IDE, agent or harness is not a factory "merely because it helps produce software."

**theory/definitions/factory-development.md**
"Definition — factory development constructs or revises reusable family-level production machinery rather than one product's lifecycle state."
- Names Greenfield's factory specialization and factory composition as family-level operations. Feedback from solution development "is evidence for factory development, not the revision itself."

**theory/open-ended-theory-learning-and-factory-learning-close-the-same.md**
"In Commonplace's arrangement, theory learning and software-factory learning require one connected reflective path..."
- The two research directions "are the same loop reached from opposite ends: each, pushed to where it stops being satisfiable on its own terms, requires what the other supplies."
- Bears on the architecture conjecture because it argues that one machinery serves both.

**theory/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md**
"Universal frameworks should replace closed content taxonomies with complete local contracts and guarded creation-time defaults..."
- Commonplace's own generality rule for the KB framework: a closed taxonomy from the KBs seen so far is "induction from too small a sample". It enters as a guarded default, universal "only if its top-level categories survive heterogeneous worked cases without exceptions or relabeling."
- "Demote, don't delete": closure did routing, growth-brake and interoperability work. Interoperability "needs a continuing shared authority or an enforced compatibility contract".
- What the framework may fix: sets fixed by consumer architecture or machinery, decided by a demotion test. It records the contested point that task-fitted structure costs reuse even inside one KB.

**reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md**
"Register retires as a closed taxonomy; COLLECTION.md must declare a text contract, and theoretical/descriptive/prescriptive persist as named default profiles in an open, worked-case-gated library."
- An implemented case of a shared primitive (text contract) with domain-specific extensions (profiles, local types, traits). "a clause typically migrates up that ladder as it proves out, cheapest first."

### 6.3 The Bitter Lesson cluster (why computation, why a bootstrap)

**theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md**
"A hand-crafted starting state fits the Bitter Lesson only if scalable learning displaces the task- and family-specific production knowledge it supplies as claimed reach widens."
- "A bootstrap is the running system itself", unlike a scaffold or prototype. The first strategy is "to grow the selection environment through use". The bootstrap is "an attempt to **learn while constructing the machinery that makes more learning selectable**."
- Generality criterion: "A system with ten hand-built ontologies and ten specialized update procedures is still a bundle of predefined solutions."
- "This is not a uniqueness claim". Strategic comparisons are listed: theory-guided construction against direct search under the same budget; whether human construction falls as the demand class widens; whether recurrent judgments become selection machinery; transfer beyond anticipated domains.
- **Failure conditions** (verbatim list): "system use becomes a self-confirming test of the theory already embodied in the system; claims remain artisanal and computational search stays peripheral; each new domain requires a bespoke ontology and evaluator; human global judgment and maintenance grow with the corpus; task-specific decomposition or evaluation choices remain human supplied while the system claims reach beyond them; interventions on retained theory make no causal difference; or a more direct learning method achieves better results at comparable total cost." Current evidence "does not establish a scalable learning method with broad production reach".

**theory/the-bitter-lesson-selects-production-methods-not-representational.md**
"The lesson's axis is production method — hand-crafted versus search-and-learning — not representational form."
- A 2×2 of production method against form. It rules out weights-monism and "Hand-crafting-forever". "The compliant position is to test search and learning over localized forms too." Sutton and Javed's weight-necessity view is "a serious empirical hypothesis".

**theory/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md**
"The production-method versus representational-form distinction answers only a narrow weights-only inference; theory-guided bootstrapping is a provisiona[l strategy]..."
- "The bootstrap should be stated as a first strategy": "a reason to try theory-guided bootstrapping, but not a proof that it is necessary or optimal." "The strategy is to grow the selection machinery through use."
- Six questions per human-supplied artifact, from what computational proposal is possible through what baseline to use. A table of what the other arguments do not establish includes "Use of Commonplace as an instrument" (it does not prove "the decomposition or bootstrap strategy is right") and codification and relaxing (it does not show "the method itself will become computationally produced").

**theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md**
"The lesson selects against claims whose reach was asserted rather than earned by a refuting test, not against structure or origin..."
- Structure survives scaling when its scope is earned. This connects to codification as a bet on earned scope (DomainBed, IRM cases).

**theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md** (description only)
"Stronger models shrink the scaffolding a fixed task needs; durable deployment-specific structure recurs at the frontier only while assigned difficulty keeps pace with capability and some reliability function stays advantageous to externalize."
- Bears on whether routine machinery stays worth maintaining as models improve.

### 6.4 Codification, constraining and relaxing (how work becomes routine and returns)

**theory/definitions/constraining.md**
"Definition — constraining commits choices in a retained artifact that narrow which readings or behaviors its consumer should treat as valid, or rank the valid ones; codification settles..."
- Interpretation space is consumer-relative. Constraining narrows content, activation or response. It has two regions, natural-language and codified. When it improves capacity it "is learning in Simon's sense". "Constraining is not automatically an improvement. A constraint can freeze the wrong proxy theory, overfit a narrow case, or block useful generality."

**theory/definitions/codification.md**
"Definition — codification is the symbolic region of constraining: a rule or operation is committed to an artifact with formal semantics..."
- "When two consumers disagree about what those rules permit, one of them is wrong." Skills extracted from methodology are not codification. Codified parts give a theory computed consequences, but not diagnosis.
- "Every codification is a bet that the committed reading stays right." Relaxing reverses it.

**theory/progressive-constraining-commits-only-after-patterns-stabilize.md**
"Constraining via LLM code generation freezes a single projection of the spec in one shot, but progressive constraining observes behavior across many runs..."
- One-shot versus progressive constraining. Progressive constraining defers commitment. "You pay for this with observation time and the cost of running the underspecified version longer." One-shot is fine when the spec is narrow.
- This is the KB's stated cost trade for when to convert work into routine.

**theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md**
"Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must codify and relax..."
- Arithmetic-regime codification is "pure gain". Vision-feature codification trades generality. "**relaxing** — replacing a codified component with a learned or general-purpose one when scale makes that viable, accepting higher cost and lower reliability in exchange for regaining generality." "The bitter lesson describes a trajectory, not a law of nature."
- Spec mining improves the bet by starting from a working system. Heuristics: "Codify for current leverage, not permanence"; prefer what-specs over how-specs; composition failure is a relaxing signal.

**theory/operational-signals-that-a-component-is-a-relaxing-candidate.md**
"Operational signals for when a component likely encodes a brittle proxy theory rather than an exact specification and should be relaxed..."
- Signals: paraphrase brittleness, an isolation-versus-integration gap, process rather than outcome constraints, failure conditions that are hard to specify, distribution-shift sensitivity, and composition failure as the late-stage signal.
- Management: replaceable slots, integration tests, and alternative candidates "so relaxing is cheap when the time comes." This is the KB's account of what maintaining a routine costs.

**theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md**
"Explains the negative-selection mechanism by which preferential codification changes the composition of work retained at an agent boundary."
- Under a fixed workload and routing, preferential codification concentrates the residue at the unpredictable end. "The whole system can become more predictable while the agent layer contains a larger share of cases requiring interpretation."
- "Self-improvement moves the frontier". A repeated success is only a candidate and needs a representation, an economical implementation and a verifier. Scope: "The mechanism neither predicts convergence on an agent-free system nor establishes how often deployed systems preferentially codify."

**theory/codify-versus-llm-decision-heuristics.md**
"Specification, checking, permitted interpretations, and repeated-use cost inform which operations to codify; none alone makes code or model interpretation universally preferable."
- Repetition section: "Repeated reconstruction creates an opportunity to retain a procedure... But recurrence can also preserve a repeated mistake. It is a cost signal and a source of candidates, not a correctness criterion." "A sound operation can be worth implementing after one informative case. Another may remain cheaper to interpret even after many cases because its premises change frequently. Compare construction, invocation, checking, retrieval, and maintenance costs under the same outcome requirements."
- A codified operation is a relaxation candidate "when its assumptions repeatedly fail or its maintenance cost exceeds an adequate alternative." This is the closest existing statement of conversion economics. It lists the cost terms but gives no combined account.

**theory/constraining-and-extraction-both-trade-generality-for-reliability.md**
"Constraining narrows interpretation and extraction produces focused use-shaped artifacts; both can trade generality for reliability, speed, or cost..."
- The gains depend on task fit. "Production, maintenance, and fallback work can also outweigh the savings, so extraction does not guarantee faster or cheaper execution." Relaxing trades the gains back for generality.

**theory/constraining-during-deployment-is-continuous-learning.md**
"Continuous learning can happen outside of weights; constraining is one symbolic-artifact form..."
- Gains "persist, accumulate, and compose". "The manual version works; automating the judgment-heavy parts is where the real gap is."

**theory/skills-derive-from-methodology.md**
"The methodology→skill relationship is same-medium derivation, with the methodology retained as live fallback — distinct from codification and constraining."
- Semantic routines (skills) are derived in the same medium, "reorganization for use". "The source stays live", unlike codification where the soft form is superseded. This is the KB's distinction between semantic routines and symbolic routines.

**theory/capability-placement-should-follow-autonomy-readiness.md**
"Three tiers — skills (autonomous-ready), instructions (reusable-but-steered), methodology notes (exploratory)..."
- Migration path: capture, then instruction, then skill "only after repeated successful autonomous execution". "This sequence prevents premature automation".

**theory/theory-and-methodology-form-a-two-layer-execution-system.md**
"In open or incompletely covered domains, the theory-derived fast path and live theory fallback co-execute..."
- "Recurrence is the learning signal. When the same fallback reasoning happens repeatedly, its result is promoted into the methodology, which grows at its boundary, driven by use." The theory must stay accessible as live fallback.

**theory/llm-executed-methodologies-are-metacircular-interpreters.md**
"Self-hosting LLM methodologies are closer to metacircular interpreters than compilers..."
- "This is closer to a JIT than to whole-program compilation. Stable hot paths become symbolic artifacts with assigned consequences; unsettled judgment stays in natural language". Self-hosting is gradual, not a milestone.

**theory/methodological-and-computational-closure-track-different-changes.md**
"Methodological closure tracks what a retained method settles; computational closure tracks the absence of human decisions during the assessed operation."
- Two different senses of routine: the method settles the decision, or computation makes it. "Naming a decider or saying 'use judgment' settles routing, not the content of that judgment."

**theory/a-retained-instruction-preserves-what-testing-selected.md**
"Explains why an instruction generated from model weights can still add KB value: testing selects a procedure under a criterion and retention makes that choice reusable."
- "Reuse avoids repeating candidate generation and evaluation." This gives the economic content of a semantic routine.

**theory/spec-mining-as-codification.md** (description only)
"Operationalizes codification by extracting deterministic verifiers from observed stochastic behavior — the mechanism that converts blurry-zone components into calculators."

**theory/methodology-enforcement-is-constraining.md** (description only)
"Explains why enforcement strength is a partial order over activation and response semantics, rather than a fixed instruction-to-skill-to-hook-to-script ladder."

**theory/oracle-strength-spectrum.md** (description only)
"Exploratory framework — oracle strength, how cheaply correctness can be verified, as the gradient underlying the exact-spec/proxy-theory distinction, with an oracle-hardening pipeline."

**theory/the-boundary-of-automation-is-the-boundary-of-verification.md** (description only)
"Synthesis — oracle theory, labor economics, frontier-lab capability predictions, and supply-chain integrity evidence converge on verification cost as the primary structural determinant of automation."

**reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md**
"scripts/ is named the committed home for reusable ad hoc tooling... with a cleanup norm and a promotion signal."
- This is an implemented promotion rule for symbolic routines. A script graduates to a command "when it has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes — repetition with a stable interface". Heavier machinery was rejected on thin evidence.

**reference/proposals/bidirectional-codification-comparative-test.md**
"Proposal: promote bidirectional codification from design guidance to a comparative conjecture..."
- Conjecture: for mixed task families, codifying as behaviour stabilizes and relaxing it back when brittle "achieves a better reliability–generality–cost frontier than a system with a fixed boundary... and than a system that promotes one way only."
- Arms: natural-language-only, symbolic-only, one-way, bidirectional. Confound: oracle quality.

### 6.5 Cost of shared abstractions and reuse

**theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md**
"Distinguishes reversible adoption from costly structural entrenchment..."
- Entrenchment, meaning dependencies or migration costs that make replacement expensive, needs one of three warrants: an enduring constraint, transfer evidence or proof for a stated scope, or coordination value. "Adoption by more tools or notes can raise migration cost; it does not demonstrate transfer." Real options affect timing only.
- This is the KB's main account of when a shared structure is worth its cost.

**theory/definitions/coordination-value.md**
"Coordination value is the worth a structure has because every artifact, tool, or agent adopts the *same* one".
- "a better-in-principle alternative does not increase it, and defection from the shared choice destroys it." It is a warrant on the value-source axis, distinct from reach. This names one benefit of a shared interface that does not come from the quality of its design.

**reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md** (superseding **adr/113**)
ADR 118 "Supersedes: ADR 113: the engine, its plan model, the advance command, hand-outs, judgments, engine-derived coverage, the run-state layout and the core/consumer boundary."
- This is a concrete case of a generic shared engine being retired. ADR 113's "generic engine ran the analysis workflow from a plan of jobs". Its readiness rules, attempt closing, hand-out validation, run lock and reset machinery "existed to enforce" consistency for a coordinator-conversation shape. With headless harnesses, "one Python process can own a run's control flow." Forces that would recur if reverted: "a run whose control flow is spread over a conversation and a disk state machine needs consistency machinery for every open attempt".
- It is evidence about the maintenance cost of a shared abstraction. The ADR does not frame it that way.

**reference/proposals/checked-inline-blocks-for-shared-instruction-text.md**
"Proposal: reuse natural-language authoring mechanics in specialized writer prompts through literal inlining backed by deterministic source-to-copy checks."
- "This is the natural-language equivalent of a missing function boundary, except the medium lacks trustworthy dereference and composition semantics." Two properties conflict: "one authoritative definition for maintainers" versus "literal, sufficient instructions in the bounded context that performs the work."
- Calling the whole generic writer from a specialized workflow would duplicate responsibilities. This is the KB's direct treatment of the reuse-versus-duplication trade for semantic routines.

**reference/proposals/replaceable-workflow-orchestrators.md**
"Proposal: separate Commonplace workflow requirements from execution machinery so an agent-plus-script orchestrator and a harness-native orchestrator can implement the same workflow."
- A shared contract with multiple implementations. "Policy drift is the primary risk." The contract's representation is open: "a shared specification with conformance tests and an executable common representation are both possible. The latter may reduce duplication but also constrain native control flow."

**theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md**
"Widening a claim's vocabulary to survive counterexamples raises universality by spending precision, so content stays flat..."
- This is the abstraction cost at the level of claims. "It spent precision to buy generality". Each round of abstraction needs scaffolding that "exposes a new edge that invites the next."
- It is relevant if a general operation vocabulary is built by abstracting domain-specific terms.

**theory/learning-is-not-only-about-generality.md**
"Per Simon, any capacity change is learning... capacity splits into generality vs reliability/speed/cost."
- Gives the capacity dimensions on which routine conversion and shared machinery trade, for example "A system that can now multiply without hallucinating has learned, even though it handles no new cases."

### 6.6 Evidence that would show the strategy failing, and how to measure it

**reference/proposals/ablation-baselines-for-the-declared-objective.md**
"Proposal: measure the declared objective — useful and warranted work per unit of human judgment — by running matched repository tasks under ablated conditions..."
- "Nothing measures it." Arms: framework as operated; raw history with no curated layer; episodes without distilled theory; review disabled; a stronger bare model. Measures: quality, escaped errors, retrieval failures, negative transfer, human decisions and minutes, and later maintenance cost.
- Design options include outside-operator transfer and frozen-artifact transfer across model families. Confounds: contamination, the operator who absorbed the methodology, and one bit per run. "Design a comparison that could show the framework failing to earn its cost."

**theory/increasing-computational-autonomy-relocates-human-effort.md** (description only)
"In an open-ended system, increasing computational autonomy need not cut total human hours — attention moves to the frontier — so measure improvements per human judgment, not human time."

**theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md** (description only)
"When a system preferentially transfers decisions whose premises, criteria, and checks are available, the remaining human decisions become harder to warrant per decision; this predicts a residue composition, not structural computational openness."

**theory/computationally-directed-self-improvement-is-a-reallocation.md** (description only)
"The progress question for self-improving systems is not category membership but which decision-bearing functions humans still supply; the endpoint test is whether the boundary can be contracted to exclude them." The bootstrapping article cites it as the removal test.

**theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md** (description only)
"Running a decomposition confirms only that it sufficed here; because many force-sets fit the same split, rationale retained at design time is what gives a transfer claim an antecedent to test."
- This bounds what local use of Commonplace can show about architecture-level transfer.

**theory/system-use-selects-theory-fit-without-a-fixed-oracle.md** (description only)
"When no complete fixed oracle decides whether a claim belongs in a working theory, distributed consequences of live system use can provide an initial selection environment."
- This is the stated reason the strategy starts from a system people use. The bootstrap note lists "system use becomes a self-confirming test" as the matching failure condition.

**theory/evidence/commonplace-as-a-reflective-system.md** (description only)
"Commonplace witnesses that a human-inclusive KB can be reflectively self-improving on one pathway despite uneven coverage and human-gated design judgment."

---

## Not found

### Direction 4
- **A small composable operation set for knowledge work in general.** No library note proposes or criticizes one beyond theory refinement. Existing sets are domain-local: refinement interface, discovery lifecycle, theory-builder Boundary operations, reflective operation profile, context-operation interface, select/call form, change-operations catalogue. None is reconciled with the others.
- **Expression versus economy.** The brief's split between whether operations can express a procedure and whether reusing them makes it cheaper has no direct treatment. The closest statements are the fixed-model-house note ("possible but too costly" versus inexpressible), the fixed-decomposition note (costly or approximate composition), and the context-operation note (reach versus policy).
- **Procedures in other domains.** No note expresses scientific investigation, software architecture, legal drafting or exploration procedures as compositions of operations. The legal note treats law as a parallel to context engineering. The software notes are about the software house conjecture. The scientific note covers one experiment-selection mechanism.
- **Exploration as a domain.** Exploration has no dedicated library note. The ARC game-solving case exists only in the epistemic-architectures workshop.
- **Designing the procedures for those activities.** The KB treats procedure design only for Commonplace's own procedures: capability placement, the maintenance catalogue, skills derived from methodology.
- **Universality on the strength of examples.** No note guards against this for operation sets specifically. The universality-axis and universal-framework notes guard against it for factories and taxonomies.

### Direction 6
- **"General computational environment".** The phrase appears in no library artifact. It occurs only in this workshop's README and handoff and in `kb/work/README.md`. No note states the architecture-level conjecture in those terms.
- **Why start with explicit knowledge management.** No note argues this specifically as a route to general computation. The stated reasons are a working system supplies the episode stream and use supplies selection (commonplace-builds-a-theory-builder, bootstrap, system-use), plus the KB as the first worked case (commonplace-as-an-instrument).
- **A small shared interface that reduces duplication while permitting domain-specific extensions.** This is not stated as a thesis about knowledge work. The nearest structures are `configure(G, K_P)` (agentic-substrate note), the protected-waist runtime thesis (workshop only), text contract plus profiles (ADR 042), and guarded defaults (universal-framework note).
- **Cost of maintaining shared abstractions.** No dedicated theory note covers this. It appears piecemeal in entrenchment and coordination value, the ADR 113/118 engine retirement, checked-inline-blocks, replaceable orchestrators, relaxing signals, and the maintenance terms in codify-versus-LLM.
- **One account of when conversion into routine pays.** Frequency, savings, conversion and maintenance cost, and stability probability are not combined anywhere, as the workshop README already noted. The pieces are spread across codify-versus-LLM (repetition section), progressive constraining, ADR 040's promotion signal, and capability placement.
- **Reuse across domains as evidence.** The sufficiency hypothesis and the bootstrap failure condition ("each new domain requires a bespoke ontology and evaluator") name it as a test. No KB evidence of cross-domain reuse exists. The instrument note says "Disciplined transfer has not been demonstrated."
- **Human judgment, reliability and implementation complexity as evidence for the architecture.** The measures are named: human decisions per verified improvement, the ablation proposal's metrics. No measurement has been run.
