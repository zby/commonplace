# Closure–capability map

This map tests the operator's correction: computational closure matters only
around a system capable enough to do consequential work. Closure by itself is
cheap. A constant function, a no-op self-loop, or an optimizer over one
irrelevant parameter can have no required human decision and still contribute
nothing to the research goal.

There is no context-free threshold for powerful enough. Adequacy is relative
to a declared challenge distribution and objective. For this workshop the
candidate threshold is the ability to help build and revise explanatory
theories, operate consequential LLM-wiki functions, and revise both retained
theory and some symbolic machinery in response to external evidence.

The practical lower bound is broader. Any tool that increases accepted
software outcomes for fixed total human programming effort, or preserves the
outcomes with less effort, moves toward the goal. This does not imply that the
tool's method can reach the strong benchmark. A method may exhaust a narrow
automation envelope after eliminating one genuine part of the residual human
work.

## Coordinates

Do not place systems on one ladder. Record a profile:

| Coordinate | Question |
|---|---|
| Human leverage | At a fixed acceptance threshold, what outcomes are attainable per unit of total human programming effort? |
| Residual human work | Which programming decisions and actions, including review and recovery, still require a person? |
| Automation envelope | Which residual responsibilities can this mechanism carry, and which remain beyond its method? |
| Computational closure | For which named path and horizon can operation continue without indispensable human judgment? |
| Operational capability | Which externally evaluated tasks can the incumbent system perform, at what quality and breadth? |
| Effective revision reach | Which behavior-determining commitments can the path both determine and install, not merely write syntactically? |
| Evaluator adequacy | What bad candidates can the acceptance mechanism reject, and against what independent objective or evidence? |
| Path continuity | Can an accepted successor perform another licensed revision, including revision of current scheduling or evaluation machinery? |
| Improvement yield | Does the loop produce useful later capability, reliability, or efficiency rather than activity alone? |
| Supplied capability | Which powerful model, ontology, action basis, evaluator, or task decomposition remains fixed outside the path's revision reach? |

The [self-revision boundary map](../self-revision-design-space/boundary-map.md)
already separates broad syntactic writability from effective revision reach and
warns that a closed evidence-responsive path does not establish a favorable
outcome. This map adds incumbent operational capability and supplied capability
because a loop may borrow most of its power from fixed machinery.

## Bounded progress and method ceilings

A narrow automation envelope is not itself a degenerate case. A formatter can
faithfully remove formatting work, and a compiler can remove work that would
otherwise be required to translate and execute a program. Both reduce the
residual programmer role. Neither mechanism can thereby take over
requirements interpretation, program-specific theory building, architectural
choice, or open-ended diagnosis.

The correct conclusion is that the method has a ceiling. It made progress up
to that ceiling, but it does not supply a convergence argument. The broader
program must record which responsibility each mechanism transfers and compose
or add mechanisms for the remainder. Calling bounded progress worthless would
erase real tool gains; calling it sufficient would erase the unsolved work.

Improvement can continue inside the bounded envelope. Better correctness,
reliability, coverage, latency, or resource efficiency counts on the
operational-capability or improvement-yield coordinates even when no new
responsibility moves from the programmer. Envelope expansion and performance
within the envelope are separate contributions to the larger system.

Ceilings are not independent of one another. Warranted transfer selects the
decisions that can be represented, settled, and independently checked, so the
residue left after several mechanisms have reached their ceilings is the
hardest-to-warrant part of the path
([warranted transfer leaves people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)).
Record each item of the human cut set with the reason it resisted transfer,
because the reason names the mechanism that must grow before it can move:

| Why the decision stayed human | What has to grow |
|---|---|
| A required premise is not represented where the system can read it | Representation |
| The criterion is unsettled; the method names a decider instead of a rule | Settlement |
| No oracle independent of the candidate can check the result | Verification |
| The decision arises after the declared automatic horizon ends | Horizon and path continuity |
| Transfer is possible but priced out | Nothing structural; a movable claim |

The same selection explains why the degenerate patterns below cluster at the
evaluator: a captured evaluator, a viability-only gate, and boundary export all
supply apparent warrant at exactly the decisions where real warrant is missing.

## Degenerate closure patterns

| Pattern | How closure is obtained | Why it is insufficient |
|---|---|---|
| Vacuous objective | Success is constant, empty, or satisfied by doing nothing | Every no-op is accepted; closure has no achievement burden |
| Trivial revision surface | The loop tunes one parameter or rewrites an inert artifact | The path is closed only over changes that cannot affect the target capability |
| Syntactic-only reach | The system may write any file but cannot reliably realize, install, or later use the change | A large write surface masquerades as effective revision reach |
| Fixed-decomposition closure | Search and evaluation are automatic inside a designer-supplied ontology, action basis, or component partition | The loop cannot represent failures caused by the decomposition itself |
| Captured evaluator | The candidate supplies or reconstructs the standard that judges it | Coherent self-confirmation replaces correction |
| Viability-only gate | Build success, non-crash behavior, or one synthetic case stands in for useful improvement | Broken candidates are filtered, but worse reasoning can pass |
| Horizon trick | One automatic update is called closed although the next episode requires a person | Closure disappears when the horizon extends |
| Destructive closure | A successor removes the revision mechanism or its evidence path | The current change completes, but the improvement path does not remain open |
| Boundary export | Human selection, a teacher, a powerful fixed model, or evaluator design supplies the hard decision outside the declared path | The apparent closure is bought by moving intelligence rather than representing it |
| Outcome-free closure | The loop repeatedly proposes and installs changes without externally measured benefit | Automation and activity increase while usefulness stays flat or falls |

These patterns are not all disqualifying in every application. A thermostat is
legitimately narrow. The error is using narrow closure as evidence for a broad
self-improvement target.

## Initial system map

This is a provisional comparison surface, not a final empirical verdict.
Named systems route the evidence to inspect; they do not imply that every cell
has already been measured.

| System or ideal type | Closure profile | Incumbent capability | Effective revision reach | Evaluator and continuity | Current reading |
|---|---|---|---|---|---|
| Constant or no-op loop | Complete for an empty or constant path | None beyond the fixed output | None | Trivial acceptance; indefinite repetition | Vacuous closed floor |
| Formatter, compiler, or similar exact tool | Closed over a fixed mechanical subtask, not a software-construction path | Reliably performs one supplied transformation | Normally none over its own method | Deterministic checks or language rules can warrant the bounded result | Real reduction in residual human work with a narrow automation envelope |
| Thermostat or Homeostat | Closed over a narrow regulation path | Maintains a bounded variable or viable setting | Fixed parameters or settings inside a supplied action basis | Fixed viability signal; repeated operation | Real but deliberately narrow closure |
| Fixed-metric parameter or prompt optimizer | Potentially closed for the declared metric and edit slot | Inherits the base model and task representation | Named parameters, prompt, or bounded artifact slots | Fixed benchmark or score; repeatable while decomposition stays fixed | Useful narrow optimizer; supplied capability dominates |
| Artifact repair loop with tests | Some prompt, rule, skill, or code paths may close | Base-model competence plus retained artifacts | Exercised artifact-local changes; broader reach varies | Tests, judges, or regression gates usually stay fixed | Operational closure can coexist with fixed decomposition and thin semantic warrant |
| Self-rebuilding code agent | Some build–test–restart paths are computational | Broad coding competence borrowed from a foundation model | Large syntactic code surface; effective reach bounded by interfaces and tests | Build, tests, or viability may preserve recurrence without proving improvement | Broad write reach, uncertain effective and useful reach |
| Gödel machine | Formally computational inside its axiomatized software boundary | Whatever the formalized machine can compute and prove useful | Broad syntactic software replacement but only proof-reachable changes are admissible | Proof gate; successor may replace the searcher if incumbent proof licenses it | Strong formal closure with a potentially near-empty practical reachable set |
| Commonplace now | Human-inclusive rather than computationally closed | Demonstrated use as an agent-operated KB and candidate theory-building tool | Broad mixed prose, schema, instruction, validator, and code changes through several paths | Mechanical and model review plus human direction and admission | High practical reach is plausible; closure and independent theory possession remain open |
| Target mixed system | Closed only when every required decision on the named path is represented | At the strong benchmark, performs at least as well as a competent remote programmer on the declared challenge distribution | Theory, derived procedures, code, scheduler, and relevant evaluators remain revisable | Independent evidence, rejection, rollback, and recurrent same-path theory revision | Non-degenerate milestone; useful partial systems lie below it |

Evidence starting points:

- [Real systems occupy combinations no rung captures](../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md)
  compares allocation, revision form, and thin versus strong gates.
- [Six reported self-improvement paths](../../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md)
  records which paths actually close and which machinery remains supplied.
- [Theory-mediated self-improvement needs interpretation and retention](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md)
  notes that a loop can close computationally while its acceptance gate weakens.
- [Gödel machines are proof-governed](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
  supplies the formal extreme.
- [Learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
  supplies the decomposition limit.
- [A repeatable operative path](../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md)
  supplies the continuity condition.

## Candidate adequacy gate for this program

A claimed strong milestone is non-degenerate only if all of the following are stated
and evidenced for the same boundary and horizon:

1. **Non-vacuous work:** a held-out or externally anchored challenge
   distribution distinguishes useful outcomes from no-op behavior.
2. **Capability floor:** the incumbent system meets a declared stage-relative
   threshold. At the strong software-construction benchmark it performs at
   least as well as a competent remote programmer given the same brief,
   repository, digital tools, permissions, and feedback.
3. **Consequential reach:** the closed path can revise commitments that
   materially determine that capability, not only inert text or cosmetic
   parameters.
4. **Correction:** the evaluator can reject plausible but harmful candidates
   on grounds not authored solely by the candidate.
5. **Continuity:** later episodes reuse the accepted result and retain a path
   for another licensed revision.
6. **No hidden cut:** supplied models, objectives, evaluators, ontologies, and
   human decisions are named rather than absorbed into the word system.
7. **Outcome evidence:** closure is accompanied by measured utility, warrant,
   or improvement yield. Mere unattended execution does not pass.

This is a working filter, not yet a theorem or a sufficient definition. A
counterexample that passes all seven while remaining obviously trivial should
change the map.

## Evaluation work

- Select representative systems for each region rather than collecting only
  systems marketed as self-improving.
- Reconstruct one named path per system at the same comparison grain.
- Separate inherited base capability from capability produced by the loop.
- Extend the horizon until the next required human intervention or until the
  path demonstrates recurrence.
- Test evaluator adequacy with candidates that pass viability while degrading
  the target function.
- Compare each closed system with a no-update baseline and a human-inclusive
  tool baseline.
- Record total residual human work and the automation envelope of each
  mechanism; do not infer that a real local gain supplies a path beyond its
  ceiling.
- Record counterexamples that force new axes or split an existing region.
