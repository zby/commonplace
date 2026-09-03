---
description: "Comparison of reviewed self-improving systems against the reachability conjecture's four witness obligations, which do not fix which form carries the theory, with a separate stronger protocol for explicit retained theory"
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

> **Draft supplement.** This is the map behind the nearest-constructions
> section of [The reachability
> conjecture](./reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md).
> Everything in it may still change, including which systems belong in the
> comparison and how each row is graded. Comments, corrections, and additional
> candidates are welcome on [the repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

The reachability conjecture holds that an automated [software
house](../notes/definitions/software-house.md), one that keeps developing
software for its users across demands nobody listed in advance, can be built
with the LLMs available in 2026 while its distributed-parametric internal state
stays fixed and the natural-language and symbolic state around it, its notes and
code, learns. It states four obligations that one constructive witness must
eventually discharge. The obligations are carrier-neutral: they do not fix
whether notes, code, or reconstruction from records carries the theory. This
article does not argue for the conjecture. It compares the systems reviewed for
this program against those obligations, so that a researcher with a system of
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
checkable than the obligations:

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
5. **Program theory.** Is project-specific understanding acquired and applied,
   rather than supplied, logged, or paraphrased, and is inadequate
   understanding later replaced from consequences, whether it is retained as
   explicit theory or reconstructed from records?
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

## How the questions relate to the four obligations

The obligations describe a progression. The questions decompose properties,
and one property can serve more than one obligation.

**Holding and application** asks whether the system realizes a program-theory
function across novel changes. **Program theory** asks that directly. The broad
witness conditions below require an implication not stated verbatim, causal use
of the relevant retained state or consumption path, and a change in what the
system does next under withholding or replacement.

**Initial acquisition** needs **Program theory** plus an operative retained
change in at least one of the two forms, notes or code: the system must acquire
the project-specific understanding rather than receive it from a person, and
that acquisition must alter later production. **Successor acquisition** asks the
same of understanding that later evidence makes inadequate. A complete witness
must eventually demonstrate both **Software learning** and **Note learning**
across its sequence, but one learning step need not change both forms.
**Automated continuation** is bounded by **Software-house boundary**, **Fixed
parametric state**, and **Continuation**, and it requires the holding and
acquisition capacities to keep working across that boundary.

One warning governs every use of the table. **Software-house boundary** and
**Fixed parametric state** are cross-cutting controls on a whole witness, not
acquisition stages. **Software learning** and **Note learning** report which
retained forms changed, and neither alone establishes **Program theory**. A
partial cell is therefore not partial completion of an obligation. Storing,
retrieving, or paraphrasing a rationale does not show that it governed a later
decision; a software or note update does not by itself show that adequate
project understanding was acquired; a reject-capable gate does not show that the
admitted successor was adequate; and scheduling or restart does not show
continued software-house operation. *Human-inclusive* in a cell means that
people fill internal roles in that construction.

## Comparison table

| Construction | Software-house boundary | Fixed parametric state | Software learning | Note learning | Program theory | Continuation | Evidence basis | Decisive shortfall |
|---|---|---|---|---|---|---|---|---|
| Fluent | Meets stated scope | Not demonstrated; model lineage and auxiliary parametric state not pinned | Meets stated scope; human-inclusive | Meets stated scope; human-inclusive | Partial; rationale is supplied, while acquisition and faithful reuse are not demonstrated | Human-dependent | Product documentation and practitioner report; implementation and outcomes not independently inspected | Humans confirm behaviour, technical approach, and unresolved decisions; theory acquisition is not tested |
| Wheelhouse | Not demonstrated | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Practitioner report; implementation and outcomes not independently inspected | Human rulings and verdicts produce the doctrine; the consolidating agent's theory-holding role is only a hypothesis |
| Ona Memo factory | Partial; bounded trial | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Product report; implementation and outcomes not independently inspected | Humans built the harness, specified taste and intent, and retained product direction |
| OpenAI agent-first product | Meets stated scope | Not demonstrated; model lineage and auxiliary parametric state not pinned | Partial; human-inclusive | Partial; human-inclusive | Partial; supplied rationale, acquisition not tested | Human-dependent | Practitioner report; no pinned model lineage or independent comparative evaluation | Humans made the repository legible and turned failures into tools, rules, and checks |
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
| PROJECTMEM | Not in scope | Not demonstrated | Not in scope | Partial | Partial; decisions are logged, not applied as theory | Not demonstrated | Paper-reported mechanism; no local ingest or inspected implementation | It records decisions and warns before repeated mistakes, but does not test acquisition or revision of project theory |
| Rainbow | Not in scope | Not applicable | Not in scope; fixed strategies adapt configuration | Not in scope | Not in scope; the governing model is designer-supplied and fixed | Meets stated scope; supplied strategies | Paper-reported mechanism, implementation, and outcomes; not independently reproduced | It adapts a running configuration through a causal architectural model, but does not learn that model or its action repertoire |

The **Program theory** column has three values and one gap, and that
distribution is the table's main result. Fifteen rows read *not in scope*
because their objective does not ask them to acquire project understanding that
relates a maintained user product to the activity it supports and guides later
modification. A benchmark agent could still need a theory of its own
organization; these records do not test that function. PROJECTMEM logs
decisions, which is more than not setting out to hold a theory and less than
applying one. Fluent and the OpenAI account, the two rows with a product and
users, carry theory that people wrote: expertise files and repository documents
that make the domain legible. Wheelhouse's people supply rulings rather than
explanations, which is why it reads *not demonstrated* beside them. So the
column runs absent, logged, supplied, and the fourth value, acquired, is empty.
Users and project theory arrive together in this set, and so far only with
people inside.

## Reading the rows

**Human-inclusive software factories.**
[Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
is the strongest reviewed match to the software-house boundary, because the
architecture described in its product documentation and its builder's
practitioner report includes external stakeholders, product code, deployment
evidence, natural-language expertise, a scheduler, rejection, retention, and
later reuse; people and the system jointly shape and confirm the brief, the
behaviour specifications, and the technical approach. The product-reported [Ona
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
practitioner-reported account is the largest substrate case in the set, with
agents generating the product code, repository-local documents making the
business domain legible, and recurring agents repairing stale documentation,
and it assigns the generalization work to people. When agents struggled,
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
update, and its most informative reported case is adverse: an agent found a
specification exploit and "preserved it as a reusable skill", which shows that
persistence, versioning, and rollback do not by themselves supply semantic
admission ([Prime
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
held-out gate, which is the strongest admission mechanism in the set, while its
four memory coordinates, its gate, and its benchmark partitions are all
supplied in advance and the work does not ask whether the agent acquires a
rationale for why a user product is organized as it is. Its reported retirement
behaviour is the weakest part of the design, because "The memory only grows,
and it can afford to." ([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
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
project memory a path into later action without testing acquisition or
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

## What a broad reachability witness would have to do

No row above is a witness. A test of the broad conjecture needs the following
conjunction:

1. A system with every distributed-parametric internal component pinned
   maintains one user product over a declared horizon and a demand process,
   specified in advance, of incrementally revealed requirements and production
   events.
2. The seed withholds at least one decisive piece of project-specific
   understanding while retaining the permitted records and interactions from
   which the capacity a program theory provides can be acquired.
3. The system later handles an implication not stated verbatim in those records,
   and withholding or replacing the relevant retained state or consumption path
   changes proposal, evaluation, diagnosis, or recovery in a predicted way.
4. A later dependency or operating consequence makes part of the earlier
   understanding inadequate. The system attributes the evidence and reaches an
   adequate successor state rather than preserving the old account blindly or
   rewriting it without grounds.
5. Across the sequence, experience causes operative learning in both
   natural-language and symbolic state, though the two forms need not change in
   the same learning step.
6. Candidate admission, rollback, conflict resolution, and continuation operate
   without a person supplying the decisive understanding or choosing the
   successor. Users may supply product requirements, facts, observed outcomes,
   and acceptance judgments about visible behaviour; internal diagnosis,
   candidate comparison, theory editing, or successor selection remains an
   internal role whatever the participant is called.
7. Evaluation covers untouched later changes and repeated runs or another
   justified estimate of usable success within the declared budget of compute,
   time, and cost, so one lucky path does not establish practical reachability.

This protocol does not require the acquired understanding to persist as a theory
stored as its own artifact. Reliable reconstruction from retained records or a
mixed carrier can satisfy it if the house passes the same causal tests over many
changes.

## The stronger explicit-theory mechanism test

To establish that a separately retained theory that can be found and revised on
its own contributes more than the broad witness requires, add these conditions:

1. The seed withholds a decisive project rationale while retaining the records
   from which it can be synthesized.
2. The system writes a rationale-bearing natural-language artifact and
   demonstrably loads it at later decisions where its unstated implications
   matter.
3. A later change is locally valid under tests but conflicts with the acquired
   rationale. The system preserves coherence without receiving the answer from
   a person.
4. A later dependency or operating consequence makes the old rationale false.
   The system attributes the evidence, admits a successor rationale and the
   corresponding software or machinery change, and avoids both blind
   preservation and ungrounded rewrite.
5. Candidate admission, rollback, retirement, and conflict resolution operate
   without a person supplying the decisive theory or choosing the successor.
6. Evaluation includes untouched later changes, counterfactual removal or
   replacement of the retained rationale, and raw-record or direct-artifact
   baselines under the same model, source evidence, demand sequence, and
   inference budget.

These conditions identify the stronger mechanism claim. Storing or citing a
rationale is insufficient; success must show causal use, revision, and an
advantage over the routes that reconstruct understanding when needed.

## What the set shows together

Read as a whole, the comparison is evidence about parts. Separate component
mechanisms are inspected in code or reported by their sources: trace-derived
candidates, scheduled consolidation, retention in both forms, notes and code,
reject-capable gates, broad self-revision, rollback that preserves
failed-attempt evidence, and continuing product operation with human authority.
What no reviewed source supplies is the full conjunction: acquired project
understanding, causal use on unstated implications, successor acquisition from
delayed product consequences, learning in both forms, notes and code,
user-facing operation, and continuation without a human in an internal role.
None also supplies the stronger explicit-theory test against matched raw-record
or direct-search baselines. The set therefore supports claims about available
components and missing tests. It does not show that the components compose, and
it does not show that the conjectured endpoint is reachable.