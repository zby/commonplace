---
description: "Twenty reviewed constructions compared against the automated software house conjecture's four witness conditions, which allow a human-built start; plus the explicit-theory test from the training article"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
  - kb/sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md
  - kb/sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md
  - kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md
  - kb/sources/how-warp-builds-self-improving-agents-on-claude.ingest.md
  - kb/sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
  - kb/sources/memento-skills-let-agents-design-agents.ingest.md
  - kb/sources/prime-agent-a-self-improving-rlm-harness.ingest.md
  - kb/sources/rainbow-architecture-based-self-adaptation.ingest.md
  - kb/sources/recursive-experiential-working-memory-evolution.ingest.md
  - kb/sources/steve-yegge-fences-not-sandboxes.ingest.md
---
# Nearest existing constructions to a reachability witness

> **Draft supplement.** This is the map behind the existing-constructions
> section of [The Automated Software House
> Conjecture](./automated-software-houses-with-fixed-llms.md).
> Everything in it may still change, including which systems belong in the
> comparison and how each row is graded. Comments, corrections, and additional
> candidates are welcome on [the repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

The [automated software house conjecture](./automated-software-houses-with-fixed-llms.md) holds that an automated [software
house](../notes/definitions/software-house.md), one that keeps developing
software for its users across demands nobody listed in advance, can be built
with LLMs and other learned components available by 2026-09-02 and held fixed
during the run, while the natural-language and symbolic state around them, its
notes and code, may change. It states four conditions that one working house
must meet: holding and application, coherent revision, automated continuation,
and practical reliability. The conditions do not fix whether notes, code, or
reconstruction from records carries the theory, and they allow a human-built
start: the house need not have acquired its starting understanding or built
its starting machinery. This article does not argue for the conjecture. It
compares the constructions and system reports reviewed for this program against
those conditions, so
that a researcher with a system of
their own can find the nearest row and read what would still be missing. Only
the rows resting on inspected code are placements of an implementation; the rest
are comparisons of designs as their sources describe them.

The table below runs two separate vocabularies, and neither upgrades the other.
The six criterion columns say what the reviewed record presents. **Meets stated
scope** means the record presents the criterion as holding inside the boundary
that record declares, and nothing more. **Partial** means the mechanism exists
but its causal role, scope, or actor allocation does not meet the question.
**Human-dependent** means a person occupies the role the question asks about.
**Not demonstrated** means the record does not show the property, **not in
scope** means the source did not set out to perform the function, **not
applicable** means the question does not apply to that kind of system, and
**not assessed** means no judgment was formed.

The **Evidence basis** column carries the doubt. It says whether the record was
inspected code at a pinned commit, a paper, a practitioner report, or product
material, and whether any outcome was independently reproduced. Only
code-inspected rows support a claim about an implementation. Rows resting on
papers, practitioner reports, or product materials are design-space
comparisons, and this article attributes them as such rather than treating them
as inspected implementations or evaluated outcomes. A row that reads *meets
stated scope* across several columns is therefore not close to a witness: the
scopes differ, and the evidence differs. The table is not a ranking.

## The six endpoint questions

The comparison runs on six questions, which are narrower and more directly
checkable than the conditions:

1. **Software-house boundary.** Does the construction include the complete
   persistent system responsible for changing software for external users across
   demands that are not a fixed benchmark list?
2. **Fixed parametric state.** Can the documented learning happen without
   changing foundation-model weights or other distributed-parametric internal
   state, and are those components actually held or pinned?
3. **Software learning.** Does experience cause a retained executable or
   codified change that affects later production?
4. **Note learning.** Does experience cause a retained natural-language change
   that is read back into later production?
5. **Program theory.** Is project-specific understanding applied across novel
   changes, rather than only logged or paraphrased, and is inadequate
   understanding later revised from consequences, whether it is retained as
   explicit theory or reconstructed from records? Understanding supplied by
   people at the start is allowed; what the question asks is whether it
   governs later decisions and whether the house, not a person, revises it.
6. **Continuation.** Is the loop sustained with no person in an internal
   production, theory-holding, generalization, selection, or admission role?

The first question is a boundary test, not an automation test. A coding harness
may repeatedly change software across benchmark or repository tasks while
remaining only one component used by a larger producer. It has software-house
boundary only when the reviewed construction includes the complete persistent
system responsible for evolving a user product across requirements, feedback,
and operating consequences. Direct conversation with end users is unnecessary;
those inputs may arrive through tickets, product management, telemetry, or other
interfaces. Human independence is assessed separately under **Continuation**. A
construction meeting both questions would be an automated software house over
its stated scope and horizon.

## How the questions relate to the four conditions

The conditions describe what one working house must show. The questions
decompose properties, and one property can serve more than one condition.

**Holding and application** asks whether the system realizes a program-theory
function across novel changes. **Program theory** asks that directly. The
witness conditions below require an implication not stated verbatim, causal
use of the relevant retained state or consumption path, and a change in what
the system does next under withholding or replacement.

**Coherent revision** asks whether, when later evidence exposes an inadequacy,
the house revises the product, its retained state, or its machinery to a
successor that supports coherent later modification. It needs **Program
theory** in its revision half plus an operative retained change in at least
one form, **Software learning** or **Note learning**. Neither form is
required on its own, and a step need not change both. **Automated
continuation** is bounded by **Software-house boundary**, **Fixed parametric
state**, and **Continuation**, and it requires holding and revision to keep
working across that boundary. **Practical reliability** has no column: no
reviewed record reports repeated runs or a justified estimate of usable
success under a declared regime, so the **Evidence basis** column is the
nearest reading.

One warning governs every use of the table. **Software-house boundary** and
**Fixed parametric state** are cross-cutting controls on a whole witness, not
stages. **Software learning** and **Note learning** report which retained
forms changed, and neither alone establishes **Program theory**. A partial
cell is therefore not partial satisfaction of a condition. Storing,
retrieving, or paraphrasing a rationale does not show that it governed a later
decision; a software or note update does not by itself show that the house
reached an adequate successor; a reject-capable gate does not show that the
admitted successor was adequate; and scheduling or restart does not show
continued software-house operation. *Human-inclusive* in a cell means that
people fill internal roles in that construction.

## Comparison table

| Construction | Software-house boundary | Fixed parametric state | Software learning | Note learning | Program theory | Continuation | Evidence basis | Decisive shortfall |
|---|---|---|---|---|---|---|---|---|
| Fluent | Meets stated scope | Not demonstrated; model lineage and auxiliary parametric state not pinned | Meets stated scope; human-inclusive | Meets stated scope; human-inclusive | Partial; rationale is supplied, while its causal use across novel changes and its revision by the system are not demonstrated | Human-dependent | Product documentation and practitioner report; implementation and outcomes not independently inspected | Humans confirm behaviour, technical approach, and unresolved decisions; causal use and revision of the theory are not tested |
| Wheelhouse | Not demonstrated | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Practitioner report; implementation and outcomes not independently inspected | Human rulings and verdicts produce the doctrine; the consolidating agent's theory-holding role is only a hypothesis |
| Ona Memo factory | Partial; bounded trial | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Product report; implementation and outcomes not independently inspected | Humans built the harness, specified taste and intent, and retained product direction |
| OpenAI agent-first product | Meets stated scope | Not demonstrated; model lineage and auxiliary parametric state not pinned | Partial; human-inclusive | Partial; human-inclusive | Partial; supplied rationale, causal use and revision not tested | Human-dependent | Practitioner report; no pinned model lineage or independent comparative evaluation | Humans made the repository legible and turned failures into tools, rules, and checks |
| Warp skill improver | Not in scope | Not demonstrated | Not in scope | Partial; human-inclusive | Not in scope | Human-dependent | Practitioner report; linked demonstration not independently inspected | Human feedback supplies the evidence and human review admits every skill update |
| Darwin Gödel Machine | Not in scope | Meets stated scope for the evolving agents; a separate fixed diagnostician sits outside them | Meets stated scope | Not in scope | Not in scope | Meets stated scope; bounded benchmark loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Admission is compile-and-edit viability, the benchmark score only weights parent sampling, and no rationale is retained |
| Huxley-Gödel Machine | Not in scope | Meets stated scope | Meets stated scope | Not in scope | Not in scope | Meets stated scope; bounded benchmark loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Its contribution is a lineage-level parent-selection signal; benchmark-style scoring is an explicit assumption and no rationale is retained |
| HyperAgents | Not in scope | Partial; no parametric-update path in the reviewed commit, but model lineage is not pinned | Meets stated scope | Not demonstrated | Not in scope | Meets stated scope; bounded generation loop | Code-inspected mechanism at a pinned commit; no run or outcome reproduced | Replayed patches change later behaviour but carry no reason, and no test isolates a replayed patch's causal effect |
| Autogenesis | Not in scope | Partial; the inspected mutation surface excludes parametric updates, but model lineage is not pinned | Partial | Partial | Not in scope | Partial | Code-inspected mutation paths; outcomes paper-reported and not reproduced | Benchmarks and a weak semantic gate; the public implementations are transitional or incomplete |
| Exo harness | Not in scope | Not demonstrated; no learning process reviewed | Not demonstrated; the broad self-edit path is distinct from learning | Not demonstrated; the deliberate authoring path is distinct from learning | Not in scope | Partial; scheduling and restart paths, no automatic improvement | Code-inspected mechanism; no live instance run | It rewrites a personal-agent executor, not a user product, and build and test results do not judge program theory |
| Prime Agent | Not demonstrated | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; bounded goals | Code-inspected mechanism; paper-reported cases and outcomes | The paper reports direct adoption of persistent refinement and a retained specification exploit; it does not test product theory |
| Memento-Skills | Not in scope | Partial; the foundation LLM is fixed, but the router is trained | Meets stated scope | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Mixed-form skills learn under answer oracles, not under delayed software-maintenance consequences |
| Recuris | Not in scope | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; fixed gate and benchmark loop | Code-inspected mechanism; fixed-parametric-state condition and outcomes paper-reported | Four predeclared memory coordinates and benchmark tasks; no project rationale and no product demand stream |
| Harness Continual Learning | Not in scope | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Finite benchmark streams and a fixed four-part harness partition; held-out forgetting remains |
| Dynamic Cheatsheet | Not in scope | Meets stated scope | Not in scope | Meets stated scope | Not in scope | Meets stated scope; bounded sequential benchmark run | Code-inspected mechanism at a pinned commit; outcomes not independently reproduced | A curator prompt is the only gate, correctness never gates a retained entry, and entries carry no provenance |
| Voyager | Not in scope | Meets stated scope | Meets stated scope | Partial; descriptions and the question cache guide retrieval and task choice | Not in scope | Meets stated scope; bounded game curriculum | Code-inspected mechanism at a pinned commit; aggregate outcomes repository-reported and not reproduced | A critic's success report admits a skill, and a same-named program overwrites the old one instead of being revised |
| Knowledge-Centric Self-Improvement | Not in scope | Meets stated scope | Not in scope | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | It deliberately isolates knowledge-only learning on benchmark families |
| PROJECTMEM | Not in scope | Not demonstrated | Not in scope | Partial | Partial; decisions are logged, not applied as theory | Not demonstrated | Paper-reported mechanism; no local ingest or inspected implementation | It records decisions and warns before repeated mistakes, but does not test application or revision of project theory |
| Rainbow | Not in scope | Not applicable | Not in scope; fixed strategies adapt configuration | Not in scope | Not in scope; the governing model is designer-supplied and fixed | Meets stated scope; supplied strategies | Paper-reported mechanism, implementation, and outcomes; not independently reproduced | It adapts a running configuration through a causal architectural model, but does not learn that model or its action repertoire |
| Commonplace | Not assessed | Not demonstrated; models not reliably pinned | Partial; human-inclusive | Partial; human-inclusive | Design target: explicit, revisable theory loaded at later decisions; no causal-use evidence | Human-dependent | Code-inspected design, this repository; no evaluated outcome | No witness run; the operator selects global fit and admits successors |

The **Program theory** column has three values and one gap, and that
distribution is the table's main result. Fourteen rows read *not in scope*
because their objective does not ask them to acquire project understanding that
relates a maintained user product to the activity it supports and guides later
modification. A benchmark agent could still need a theory of its own
organization; these records do not test that function. PROJECTMEM logs
decisions, which is more than not setting out to hold a theory and less than
applying one. Fluent and the OpenAI account, the two rows with a product and
users, carry theory that people wrote: expertise files and repository documents
that make the domain legible. Wheelhouse's people supply rulings rather than
explanations, which is why it reads *not demonstrated* beside them. So the
column runs absent, logged, and supplied, and the value the conjecture needs,
supplied or not but shown to govern later decisions and to be revised by the
system from consequences, is empty. Users and project theory arrive together
in this set, and so far only with people inside. Whether a house can acquire
its theory rather than receive it is a further question, asked by the
training and bootstrap articles, and no row tests it either.

## Reading the rows

**Human-inclusive software factories.**
[Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
is one of two rows classified as meeting the software-house boundary within its
stated scope. Its product documentation and its builder's practitioner report
describe external stakeholders, product code, deployment evidence,
natural-language expertise, a scheduler, rejection, retention, and later reuse;
people and the system jointly shape and confirm the brief, the behaviour
specifications, and the technical approach. The product-reported [Ona
Memo factory](https://ona.com/stories/software-factory-what-we-learned) trial
took an empty repository to a deployed product in ten days with software, notes,
schedulers, and production signals in one loop, and people spent the early days
writing the automations, conventions, and review paths that made it run. Steve
Yegge's practitioner-reported account describes rulings progressing from custom
to warning to written doctrine to programs that refuse an action, with his own
judgments producing the rulings, and it also reports the maintenance cost of
that path in a corpus that retained "old rulings that were obsolete or had
changed" ([Wheelhouse](../sources/steve-yegge-fences-not-sandboxes.ingest.md),
verbatim).

**Production scale reports and rule accumulation.** [Warp's scheduled skill
improver](../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
is practitioner-reported on the note side only: people write the feedback and a
human review admits every skill update. OpenAI's five-month
practitioner-reported account describes agents generating the product code,
repository-local documents making the business domain legible, and recurring
agents repairing stale documentation, and it assigns the generalization work
to people. When agents struggled,
engineers asked "what capability is missing? What constraint is unenforced?"
and then built the tool, wrote the linter, or added the structural test
([agent-first
product](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md),
verbatim).

**Self-rewriting agent lineages around frozen models.** The Darwin Gödel
Machine paper reports an evolutionary loop over coding agents around frozen
foundation models, in which a child is admitted on viability rather than on
score, because "Only agents that compile successfully and retain the ability to
edit a given codebase are added to the DGM archive" ([Darwin Gödel
Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md),
verbatim).

**Neighbours in that family.** The [Huxley-Gödel
Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
paper reports that immediate benchmark score predicts descendant productivity
poorly, a result aimed at the parent-selection layer the Darwin Gödel Machine
leaves fixed; its implementation was not inspected here. The code-inspected
[HyperAgents](../agent-memory-systems/reviews/hyperagents.md) release replays
patch lineages into the code its next generation edits, so its retained memory
is executable but not explanatory. The code-inspected
[Autogenesis](../agentic-systems/autogenesis.md) protocol covers more writable
forms than either, and its semantic selection is weaker than its versioning
machinery.

**Mutable persistent substrates.** The code-inspected
[Exo](../agentic-systems/exo.md) harness supports broad self-inspection,
symbolic revision, restart, rollback, and preserved failure evidence, and the
inspected design contains no automatic trigger from experience to improvement.
Prime Agent has a code-inspected runtime carrying versioned prompts, memories,
skills, and subagent specifications across trajectories without a weight
update. One reported case used here is adverse: an agent found a specification
exploit and "preserved it as a reusable skill", which shows that persistence,
versioning, and rollback do not by themselves supply semantic admission ([Prime
Agent](../sources/prime-agent-a-self-improving-rlm-harness.ingest.md), verbatim).

**Fixed-parametric-state learning under benchmark oracles.** The
paper-reported [Harness Continual
Learning](../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
work commits an edit only when it improves the current task, respects sampled
historical anchors, and passes validity checks, and it reports held-out
forgetting even at zero loss on the retained anchors, which is negative
evidence for any easy continuation claim. The Memento-Skills paper reports
learning through one mixed-form unit of declarative instructions plus
executable code under an answerable-benchmark oracle, but also trains a router,
so it is not a witness to the stronger fixed-parametric-state condition. Its
ablation isolates the mixed-form optimization mechanism by removing the
optimisation step, leaving "no failure attribution, no skill rewriting, and no
skill discovery" ([Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md),
verbatim).

**A reject-capable gate on a fixed surface.** Recuris forms component-scoped
patch proposals from traces and decides each with a deterministic paired
held-out gate. Its four memory coordinates, gate, and benchmark partitions are
all supplied in advance, and the work does not ask whether the agent acquires a
rationale for why a user product is organized as it is. Its reported retirement
limit is explicit: "The memory only grows, and it can afford to."
([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
verbatim).

**Single-form retention under a thin gate.** The code-inspected [Dynamic
Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md) keeps a
natural-language cheatsheet curated from solver traces and injected into the
next prompt, with the curator prompt as the only gate and no software change at
all. The code-inspected [Voyager](../agent-memory-systems/reviews/voyager.md)
keeps the other form, admitting an executable skill when a critic reports
success and overwriting a same-named program rather than revising it. Neither
review found a test isolating a retained item's causal effect on later
behaviour.

**Knowledge-only and project-memory studies.** The paper-reported
[PROJECTMEM](https://arxiv.org/abs/2606.12329) study logs issues, attempts,
fixes, and decisions and warns before repeated failed fixes, which gives
project memory a path into later action without testing application or
revision. The Knowledge-Centric Self-Improvement preprint reports a protocol
that isolates external knowledge as the learned object, holding software and
solver state fixed and letting benchmark answers supply the oracle, so that
"The only object that changes is the curated knowledge base."
([Knowledge-Centric
Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim).

**Pre-LLM.** The paper-reported
[Rainbow](../sources/rainbow-architecture-based-self-adaptation.ingest.md)
architecture keeps a causally operative model of a running system and selects
adaptation strategies from it, and its vocabulary, goals, constraints,
operators, and strategies are all designer-supplied and fixed. It locates the
boundary precisely: a model can drive adaptation without the system learning
the theory that governs adaptation.

**Reference construction.** Commonplace, the knowledge base in which this
comparison is written, is included as a construction built to address holding
and revision directly: it retains explanatory theory as notes with declared
scope and evidence, loads them into later work, and revises them under review.
It is scored by the same rubric and evidence classes as every other row, and it
is a design target, not evidence. Its evidence notes record one revision in
which retained theory guided computational search with the operator selecting
global fit, and no case in which a later improvement has been traced to an
earlier retained theory. It is not a witness: no run exists, the models are not
pinned, and the operator fills the admission role.

## What a witness would have to do

No row above is a witness. A test of the conjecture needs the following five
checks, which operationalize the main article's four conditions:

1. A system with every learned component pinned maintains one user product
   over a declared horizon and a demand process, specified in advance, of
   incrementally revealed requirements and production events. Its starting
   product, project theory, tools, tests, and machinery may have been written
   by people.
2. The system later handles an implication not stated verbatim in its
   retained state, and withholding or replacing the relevant retained state or
   consumption path changes proposal, evaluation, diagnosis, or recovery in a
   predicted way.
3. A later dependency or operating consequence makes part of the earlier
   understanding inadequate. The system attributes the evidence and revises
   the product, its retained state, or its machinery to an adequate successor
   rather than preserving the old account blindly or rewriting it without
   grounds.
4. Candidate admission, rollback, conflict resolution, and continuation operate
   without a person supplying the decisive understanding or choosing the
   successor. Users may supply product requirements, facts, observed outcomes,
   and acceptance judgments about visible behaviour; internal diagnosis,
   candidate comparison, theory editing, or successor selection remains an
   internal role whatever the participant is called.
5. Evaluation covers untouched later changes and repeated runs or another
   justified estimate of usable success within the declared budget of compute,
   time, and cost, so one lucky path does not establish practical reachability.

This protocol does not require the understanding to persist as a theory
stored as its own artifact; reliable reconstruction from retained records or a
mixed carrier can satisfy it if the house passes the same causal tests over
many changes. It also does not require the house to have acquired that
understanding, or to have built its machinery, by computation. Those are the
stronger questions of the [training
article](./the-software-house-as-the-unit-of-training.md) and the [bootstrap
article](./bootstrapping-the-first-automated-software-house.md).

## The explicit-theory test from the training article

The training article's explicit-theory advantage hypothesis says that a house
which forms, loads, applies, and revises a separately retained project theory
does better under structured change than one that reconstructs its
understanding from records or searches the implementation directly. Testing it
adds these conditions to the witness:

1. The seed withholds a decisive project rationale while retaining the records
   from which it can be synthesized.
2. The system writes a rationale-bearing natural-language artifact and
   demonstrably loads it at later decisions where its unstated implications
   matter.
3. A later change is locally valid under tests but conflicts with the
   synthesized rationale. The system preserves coherence without receiving the
   answer from a person.
4. A later dependency or operating consequence makes the old rationale false.
   The system attributes the evidence, admits a successor rationale and the
   corresponding software or machinery change, and avoids both blind
   preservation and ungrounded rewrite.
5. Candidate admission, rollback, retirement, and conflict resolution operate
   without a person supplying the decisive theory or choosing the successor.
6. Evaluation includes untouched later changes, counterfactual removal or
   replacement of the retained rationale, and raw-record or direct-artifact
   baselines under the same model, source evidence, demand sequence, and
   inference budget, with the outcome measures declared before the run.
   Adaptation of model weights on the same production evidence is a further
   baseline, comparing the fixed-model regime with a different one.

These conditions identify the mechanism claim. Storing or citing a rationale
is insufficient; success must show causal use, revision, and an advantage over
the routes that reconstruct understanding when needed.

## What the set shows together

Read as a whole, the comparison is evidence about parts. Separate component
mechanisms are inspected in code or reported by their sources: trace-derived
candidates, scheduled consolidation, retention in both forms, notes and code,
reject-capable gates, broad self-revision, rollback that preserves
failed-attempt evidence, and continuing product operation with human authority.
What no reviewed source supplies is the full conjunction: project
understanding with causal use on unstated implications, coherent revision from
delayed product consequences, user-facing operation with every learned
component pinned, and continuation without a human in an internal role. None
also supplies the explicit-theory test against matched raw-record or
direct-search baselines. The set therefore supports claims about available
components and missing tests. It does not show that the components compose, and
it does not show that the conjectured endpoint is reachable.
