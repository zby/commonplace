# Semantic work and the ideal interpreter

> **Status:** Working summary and definition test, 2026-09-14. The operator
> asked to make the ideal interpreter central, reconsider open-endedness as
> an independent condition, and check whether semantic work can be defined
> coherently without making it an ability to do everything. The operator
> subsequently named unsolved mathematical hypotheses, especially P versus
> NP, as required tests of the definition. A further discussion asked how far
> an LLM can extend computations absorbed during training; the operator asked
> to record the resulting resource-bounded ideal-interpreter definition here.
> This file owns the semantic-work definition, rationale, and stress tests.
> The current interpreter definition is in
> [resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md).
> Neither is an accepted library definition.

## Direction from the discussion

The ideal interpreter is the main abstraction of the proposed theory builder.
We first ask what a builder could do with the stipulated semantic operations,
then assess how actual interpreters approximate those operations. An LLM is
one candidate realization. Fixed model weights are a constraint on some
realizations, not a requirement of the abstraction.

The intended semantic capacity includes developing and revising concepts and
procedures as work requires. Faithfully reading theories in an already fixed
vocabulary would be too narrow. Under the broader assumption, the operator
proposed dropping open-endedness as an independent condition: the concepts
and procedures need not all be supplied in advance. Reflection still names
what the builder investigates, including its own machinery; autonomy still
names who performs its internal work.

The abstraction should separate errors in interpreting a theory from errors
in the theory itself. Even faithfully interpreted theories can be false.
Actual systems introduce additional interpretation errors and implementation
failures. Resource costs remain explicit even in the ideal model; evaluating
an implementation must establish its actual costs and capabilities.

The [warrant-bounded proposal](./proposal-warrant-bounded-open-endedness.md)
introduced the ideal interpreter in section 6. This document brings it to the
front of the investigation. The [current definitions](./theory-builder.md)
now use the interpreter and fallible theory, with reflection and autonomy as
the two conditions and extension as a measured quantity. The seed-objective
closure claim remains a separate
unsettled argument, not a premise needed to define semantic work.

## Candidate definition

**Semantic work** is establishing, examining, or revising how expressions and
concepts represent a subject and bear on a question. It makes explicit the
referents, distinctions, commitments, scope, and relevant consequences of a
representation, or proposes changes to them when the current representation
is inadequate.

Here a **representation** may be a theory, model, instruction, specification,
or account of a case. The work concerns the relation between that
representation, its context, and what it is used to understand or do. It is
not limited to natural language, and it does not require a unique correct
representation of the subject.

Interpreting a claim does not include a guarantee of deciding it. A
mathematical conjecture may remain unresolved after successful interpretation.
Conceptual work can contribute to its eventual solution without the semantic
capacity guaranteeing a solution.

This develops the KB's narrower use of semantic work for judgments about
meaning and relevance in
[semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md).
It adds conceptual revision explicitly. It does not define semantic work as
whatever an LLM does, whatever a fixed program cannot do, or whatever makes a
task succeed. Each of those would make the boundary depend on the chosen
implementation or the outcome we want to explain.

## What the work produces

The following are candidate operations, not a claim to an exhaustive taxonomy.
Their outputs must be inspectable enough to be challenged.

| Operation | Output that makes the work reviewable |
|---|---|
| Interpret an existing expression | A reading with its referents, commitments, contextual assumptions, and consequential ambiguities identified. |
| Relate a case to a concept | Grounds for including, excluding, or leaving the case undecided under the concept's stated scope. |
| Connect commitments to consequences | A relevant conditional consequence or test obligation, identifying the premises it depends on. This does not promise every consequence. |
| Criticize a representation | A conflict, missing distinction, scope failure, or rival interpretation, with the case that makes it matter. |
| Develop or revise concepts | A candidate distinction, mechanism, vocabulary, or decomposition, with what changes in interpretation or expected consequences. |
| Translate between representations | A mapping of commitments, including what is preserved, omitted, added, or still unsettled. |

Interpretation and invention have different success conditions. A reading
can misrepresent commitments already fixed by the context. A newly proposed
concept is not a recovered hidden meaning; it is a candidate way to organize
the subject. It needs reasons and discriminating consequences, and may later
fail. A revision that changes a commitment must be reported as a change,
rather than presented as what the old text always meant.

This distinction matters to the idealization. Perfect fidelity to existing
commitments does not imply perfect invention of new ones. The broader worker
may contain both capacities without treating their outputs as equally
settled.

## A bounded role, even across unanticipated subjects

Semantic work can occur within almost any intellectual task. That does not
make it the whole task. The proposed boundary follows the contribution made:
clarifying or changing the representation-to-subject relation. The same
agent or program may perform semantic and other work in one episode.

| Task | Semantic contribution | Work not supplied merely by that contribution |
|---|---|---|
| Explain a scheduler failure | Distinguish total capacity from capacity available under competing load; propose a missing dependency. | Collect traces, measure load, run experiments, implement and deploy a repair. |
| Develop a mathematical argument | Formulate the conjecture, identify the relevant objects and assumptions, or propose a useful reformulation. | A terminating procedure that settles every conjecture, or cost-free proof search. |
| Build a new tool | Work out what the tool must represent and preserve, and how its interface relates to the intended use. | Correct construction, execution, access to resources, and verification of all behavior. |
| Revise an evaluator | Explain a mismatch between its score and its purpose; propose a better distinction or test. | Evidence that the replacement discriminates adequately in its intended use. |

Executing a fixed calculation can discharge an obligation identified by
semantic work without itself revising an interpretation. Conversely, coding
can include semantic work when it settles what a requirement commits the
implementation to. File type and processor identity do not decide the role.

Thus the proposed restriction is on the operation and its claimed result,
not a permanent list of subject areas. We can allow new subjects and concepts
while bounding each episode by a question, available context, accessible
evidence, and a resource allowance.

## What an ideal interpreter can coherently mean

A workable first idealization is **faithful interpretation on a declared
class of tasks**, together with **the capacity to propose conceptual
revisions**. Where context fixes an interpretation, an ideal result preserves
it. Where context leaves consequential alternatives, the result must not
silently invent a uniquely intended meaning. New commitments remain marked
as proposals.

An idealization needs a success relation as well as a list of operations.
For each assessed task, state what counts as preserving the existing
commitments, what can be changed, and what would discriminate a useful
revision from an arbitrary one. A finite assessment need not freeze the
worker's future vocabulary. It does bound what that assessment establishes.

For a first comparison, idealize away misreading on those tasks. Keep the
cost of search, evidence collection, execution, and even semantic calls
explicit. Do not postulate that all semantic questions have a determinate
answer or that the worker always discovers one. An unresolved result may be
appropriate, but a worker that returns unresolved on every task has not
demonstrated the stipulated capacity. Positive cases with independently
specified acceptance conditions are needed alongside the failure cases.

This is a candidate architecture contract, not yet a complete mathematical
model. Its exact task and success relations remain to be specified. An
alternative ideal with access to a noncomputable oracle could be studied,
but computational realization and approximation would then require a
separate argument. Calling the component ideal establishes neither.

The name *interpreter* may prove too narrow for the constructive operations.
For now, *semantic work* names the activity and *ideal interpreter* retains
the discussion's name for the proposed component; the naming question should
not hide the difference between faithful reading and conjectural invention.

## Working definition: resource-bounded ideal interpreter

The operator's sharpened definition is maintained in
[resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md).
It performs the same kinds of semantic work as the ideal interpreter, using
its current knowledge and procedures within a computational budget. Removing
the budget does not grant a guarantee of successful discovery. This section
keeps the motivation; the definition file owns the fidelity and budget clauses.

### Motivation: how far beyond previously performed work?

The operator suggested that LLMs might cache computations performed during
human work, then clarified that the question is how far beyond that work they
can proceed, rather than whether they can produce anything new. A useful
working hypothesis is that training stores reusable results and procedures,
while inference performs additional work using them. This is a hypothesis
about LLMs, not an established limitation or a premise of the definition.

The relevant question is how much further computation a task requires given
the starting repertoire. A result can be new while requiring only a short
combination of familiar procedures. Conversely, developing a useful new
procedure may require extensive search and assessment. This draft does not
yet define a measure of that distance or a cost model for semantic operations.

For P versus NP, the absence of a known human solution does not establish
that an LLM cannot discover one. It also gives no reason to assume that the
remaining work is within its resources. The interpreter may understand the
question and use known methods while failing to resolve it. Ideality grants
no shortcut over the missing work.

The resulting research question is: under a stated resource budget, how far
can a builder extend its starting repertoire, and can retaining useful
extensions make subsequent advances easier? Interpretation is idealized;
discovery remains resource-dependent and fallible. The builder definitions
now use this framing; their remaining conflicts are listed in the
[workshop review plan](./README.md#next-review-reconcile-the-definitions).

## Paradoxes and overreach to avoid

**Understanding must not become omniscience.** A worker can understand what
an empirical claim asserts without knowing whether it holds. Two situations
can supply the same accessible evidence while differing in an unobserved
outcome. No fidelity requirement picks the actual outcome from those inputs.
Report the competing possibilities and the evidence needed to distinguish
them. Interpretation neither invents observations nor gives a terminal
objective its own justification.

**Meaning must not become a universal decision procedure.** Understanding a
program's specification does not guarantee deciding its termination or every
consequence of its execution. Requiring a total computable solver for every
such question would encounter the undecidability limits established by
[Turing, On computable numbers, §§8 and 11](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).
The proposed escape is limited obligations and no guarantee of exhaustive
resolution, rather than an oracle that always recognizes which problems are
undecidable.

**Reflection must not require unrestricted self-truth.** A worker can inspect
and criticize an account of itself without correctly assigning true or false
to every sentence about its own judgments. Requiring classical truth values
for unrestricted sentences such as “this sentence is not true” introduces a
different, inconsistent demand. Tarski's treatment separates the language
being discussed from the language used to define its truth conditions.
That is one discipline to investigate, not a claim that all self-reference
is forbidden.
([Tarski, The semantic conception of truth, §§7–10](https://www.jfsowa.com/logic/tarski.htm))
Our component need not contain a universal truth predicate.

**Correct interpretation must not mean mind-reading.** “Keep the important
notes” does not, without context, fix which importance criterion was intended.
The worker may expose alternatives or propose a criterion; silently choosing
one cannot count as faithful recovery. The assessment must distinguish
authorial intent, declared convention, and newly proposed meaning.

**Concept invention must not certify itself.** Renaming every failed case
“outside scope” can manufacture apparent success. A conceptual repair must
identify what commitment changed, what earlier use depended on it, and a
remaining case that could challenge the revised account. Even those records
do not by themselves establish that the repair is good.

**Semantic work must not be defined by successful problem-solving.** If
“understand the problem” means “produce its correct solution,” the ideal
interpreter assumes the result the builder was meant to achieve. A proposal
that correctly identifies a missing measurement can complete useful semantic
work while leaving the original problem unsolved. The task table above is a
test of this separation.

**The ideal must not erase acquisition or its cost.** If the component
instantly synthesizes, installs, and warrants every needed procedure,
machinery acquisition follows by stipulation. To study acquisition, retain
those steps and their costs outside the semantic primitive's guarantees.
Likewise, a finite implementation is not an unbounded machine simply because
it has external storage.

## Stress test: open mathematical problems

P versus NP and the Riemann hypothesis are particularly useful tests because
they already have precise mathematical statements. Their difficulty cannot
be assigned entirely to ambiguous wording or missing formalization. Clay
lists both as unsolved at the check on 2026-09-14.
([P versus NP](https://www.claymath.org/millennium/p-vs-np/);
[Riemann hypothesis](https://www.claymath.org/millennium/riemann-hypothesis/))

P versus NP asks whether every decision problem with polynomially bounded,
polynomial-time-checkable certificates also has a deterministic polynomial-time
decision algorithm. The Riemann hypothesis concerns whether every nontrivial
zero of the zeta function has real part one-half. These are claims to
investigate, not instructions whose meaning selects their truth value.
([Cook, official P versus NP description, §1](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf);
[Clay's Riemann hypothesis account](https://www.claymath.org/millennium/riemann-hypothesis/))

| Request | What the semantic contract can require | What it must not guarantee merely by ideality |
|---|---|---|
| Explain P versus NP | Preserve the quantifiers, decision-problem setting, certificate condition, and asymptotic resource bound. | Decide whether P equals NP. |
| Propose a new approach to P versus NP | Make the proposed concepts and intermediate obligations explicit; distinguish established steps from conjectures. | Produce an approach that succeeds or is better than every known approach. |
| Examine an attempted proof | Identify the claim each step purports to establish and its dependencies; use separately available proof-checking machinery for a supplied formal derivation. | Find every possible gap in arbitrary informal arguments, or find a proof whenever one exists. |
| Interpret the Riemann hypothesis after many verified cases | Preserve its universal scope and distinguish the tested cases from the full assertion. | Turn a finite collection of successful checks into a proof of the universal claim. |
| Explain why every prime greater than two is odd | Give the short argument from the definitions, within a declared positive test of interpretive and inferential competence. | Use unresolved status as an excuse on every mathematical task. |

These cases require four distinctions: understanding a statement, inventing
a potentially useful representation, finding a proof, and checking a supplied
formal proof. A single worker can do all four on some tasks. Success at the
first does not guarantee success at the others. The model should permit
discoveries without building their success into the semantic primitive.

An open mathematical problem is also not the same as a proven undecidable
decision problem, or a statement shown independent of specified axioms.
The absence of a known solution to P versus NP licenses neither of those
classifications. For such a task, unresolved is a report of the present
result, not a theorem that no resolution is possible.

The operator's subsequent clarification concerns independence from axioms.
If a sentence is independent of a consistent classical theory, neither the
sentence nor its negation is provable in that theory. Adding either one,
separately, gives a consistent extension. A builder may investigate those
extensions and grounds for adopting a new axiom. Adoption changes the
assumptions; it is not a proof from the original assumptions and does not by
itself establish truth about the intended subject.
([Petrakis, Logic, §4.11](https://www.mathematik.uni-muenchen.de/~petrakis/LogicLectureNotes.pdf))
Algorithmic undecidability instead excludes a terminating correct procedure
for every instance of a decision problem. Investigating stronger axioms can
settle further individual cases without supplying such a universal procedure.
The interpreter contract should permit axiom proposals while preserving this
distinction and their status as proposals.

There is a separate cost trap. Suppose the ideal worker can decide every
Boolean satisfiability instance correctly in one uncharged semantic call.
Our model would then assume an efficient SAT oracle. That would not establish
P = NP for ordinary computation: the cost and computational realization of
the new primitive remain unaccounted for. This is an inference from Cook's
distinction between ordinary algorithms and oracle computation, not a result
claimed for a semantic worker in that source.
([Cook, §§1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf))

The definition passes these tests only if it allows faithful understanding
without guaranteed resolution, preserves the status of conjectural steps,
and charges for substantive search and checking. Defining ideality as
“correctly answers every meaningful question” fails this test: it postulates
a general answer oracle rather than isolating semantic work.

## Does this make open-endedness redundant?

The discussion's simplification works at the level of **conceptual capacity**:
the semantic worker can propose distinctions and procedures not individually
specified in advance. We need not repeat that as a separate adjective in the
research target. A processor restricted to interpreting a fixed inventory of
concepts would fail this intended contract, however faithfully it interpreted
that inventory.

This does not prove unrestricted operational capability. A builder may form a
new concept but lack an instrument, authority, implementation, or feasible
search process needed to act on it. Actual acquisition of useful machinery
remains something to demonstrate. This is a limit on what follows from the
semantic assumption, not a proposal to restore open-endedness as another
independent condition.

The resulting definition order would be semantic work, the ideal component,
fallible theory, theory builder, reflection and autonomy, then implementation
and evaluation. A theory remains fallible under ideal interpretation because
its empirical commitments can be wrong. A self-theory can guide machinery
revision without its own acceptance making that revision warranted.

The [Gödel-machine comparison](./goedel-machine-comparison.md) then needs to
state both the semantic operations admitted as primitives in our model and
the different grounds allowed for accepting machinery changes. An ideal
primitive is an assumption for that comparison, not evidence of a
computational advantage or proof that a Gödel machine could never contain an
implementation of some of those operations.

## Checks that would move this from a sketch to a definition

| Case to work through | Required discrimination |
|---|---|
| One text with two contextually legitimate readings | Preserving alternatives versus silently imposing a reading. |
| A new concept introduced after an operating failure | A change with testable consequences versus a new label for the same account. |
| A precisely understood but unresolved program property | Understanding the question versus having a decision procedure for it. |
| P versus NP and the Riemann hypothesis | Precise understanding and conceptual exploration versus a guaranteed mathematical resolution. |
| A sentence independent of specified axioms | Investigating consistent axiom extensions versus proving the sentence from the original axioms. |
| Two worlds consistent with the available observations | Correctly conditional reasoning versus invented factual certainty. |
| A self-description that praises its own evaluator | A represented claim versus independent support for that claim. |
| A sound conceptual proposal that cannot be deployed | Semantic progress versus successful operational extension. |

Use the scheduler example first: take a theory that assumes fixed available
capacity, supply evidence compatible with both external contention and an
internal leak, and ask for the commitments to reopen and a discriminating
measurement. The expected result should not name the true cause before the
measurement. Then supply its outcome and examine the revision. A matched
fixed-vocabulary case can test faithful interpretation separately from
conceptual invention. These are proposed specification probes, not completed
experiments or additions to the other workshop's experiment designs.

Before promotion, compare this account with existing work on interpretation,
conceptual change, belief-base revision, and truth maintenance. The
[belief-base representation](https://www.cambridge.org/core/books/abs/belief-revision/dyadic-representation-of-belief/D435EAAA3E9EDB68FF64835DEE049C38)
already separates explicit premises from a consequence operator; that part
does not need reinventing. The current question is whether the constructive
semantic operations and their success conditions add a coherent, useful
abstraction. No historical novelty claim is established here.

**Assessment:** a coherent role definition appears possible if semantic work
is bounded by its contribution and ideality concerns faithful interpretation,
while concept invention remains conjectural. A complete ideal machine has
not yet been specified. The unresolved choice is how much positive success
to require of conceptual invention without assuming general problem-solving
or making “can propose something” vacuous.
