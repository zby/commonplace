---
description: "Supplement: eighteen existing constructions graded against the software-house supplement's four witness conditions, what the survey shows for conjectural learning with fixed models, and the separate test of acquiring an explicit theory"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/definitions/addressable-theory.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
---
# Nearest existing constructions to a witness house

> **Draft supplement.** This is the survey of existing systems behind two
> claims in the series that starts with [Conjectural Learning with Fixed
> Models](./conjectural-learning-with-fixed-models.md): that the proposed arrangement is untested
> but its parts have precedents, and that no system in the reviewed evidence
> meets the four conditions of the [software-house
> supplement](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md).
> Everything in it may still change, including which systems belong in the
> comparison and how each row is graded. Comments, corrections, and additional
> candidates are welcome on [the repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

**TL;DR.** The series proposes studying conjectural learning through addressable
written theories while model weights stay fixed. The view this survey denies is
that existing self-improving agent systems already demonstrate that. Across
eighteen systems, the parts have precedents: retained notes and code,
scheduled revision, gates that can reject a change, and rollback with
failure evidence. In the evidence reviewed, no system meets the four
conditions for an automated software house together, and none tests the
arrangement's central mechanism, a retained explanation guiding a later
decision on a case it did not state. Some precedents were inspected in
code. Others are known only from papers or practitioner reports, and no
reported outcome was reproduced here. The finding is about the reviewed
evidence, not about what exists elsewhere.

This supplement grades the systems against the strictest statement the series has,
the four conditions of the [automated software house
conjecture](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md#claim).
It uses those conditions because they are fully specified, while the
protocol for the series' first arrangement, a knowledge base for consuming
projects, is not yet fixed.

The conjecture asks whether a [complete persistent
producer](../notes/definitions/software-house.md) can develop software for
users across requests not listed in advance, with no human internal
production decisions during its run. A **witness house** would be a concrete
example meeting the four conditions below. Its eligible
distributed-parametric models, those whose knowledge is held in trained
weights, must have been available by the conjecture's
chosen cutoff, 2026-09-02. Their parameters remain fixed, including adapters
and the parameters of embedding models, parametric routers, and parametric
critics.

This is a selective comparison of eighteen constructions with retained local
reviews or source analyses. They were chosen for mechanisms relevant to the
conjecture's question: retained project knowledge, revision of production
machinery, automated operation, or causal models guiding adaptation. Rainbow
is a contrast case in runtime configuration, and Commonplace is included as
the authors' own system. The sample is neither exhaustive nor a ranking of
proximity.

The reviewed evidence demonstrates no complete witness house. That negative
finding applies only to this reviewed evidence and does not establish that
no such house exists elsewhere. [What the survey shows for the
paradigm](#what-the-survey-shows-for-the-paradigm) says what the same
evidence shows for the paradigm in general.

## How to read the table

**Program theory** is understanding of the software's purpose, organization,
and how to handle new requests. An **explicit project theory** is one possible
written form: an account of design commitments, causal assumptions, and
invariants. The table assesses the understanding, not whether a system stores
that particular artifact. Reliable reconstruction from records is also eligible.

Each column asks about one of the conjecture's conditions:

- **Holding and application:** program theory guides novel changes, including
  implications not stated verbatim in retained material.
- **Coherent revision:** evidence against earlier understanding leads to changes
  in the product, retained state, or machinery that support continued modification.
- **Automated continuation:** those capacities persist through later requests
  and consequences, with pinned distributed-parametric models and no internal
  human production decisions.
- **Practical reliability:** evaluation supports useful success in sustaining
  adequacy within the declared horizon and budget.

The first two conditions need positive evidence: a run that never challenges
an assumption does not demonstrate coherent revision. An adequate house can
perform the first three functions. The fourth asks how reliably it sustains
that capacity. The evidence supplement
[defines that measure](./testing-the-conjectural-learning-program.md#what-a-runs-path-can-and-cannot-show)
as continuation reliability. Workload and observation limits describe the
evaluation, rather than a product family the house must stay within.

Users may supply requirements, facts, observations, and judgments about
visible behaviour. Supplying implementation diagnosis, internal design, or
selection of retained revisions instead performs a production role.

Cells use two grades against these full conditions. **Not shown** means the
evidence is insufficient, including tests outside software-house operation.
**Not met** means an observed feature conflicts with the condition. The text
after each grade records narrower evidence or a specific gap. An agent-code
patch can be relevant without establishing coherent product revision, just
as a benchmark loop can be autonomous without sustaining a software house.

Row names link to the evidence accounts in the same order. Those accounts
separate inspected code from paper and practitioner reports. Code inspection
establishes mechanisms, while outcome evidence assesses performance. Reported
outcomes were not independently reproduced here.

## Comparison table

| Construction | Holding and application | Coherent revision | Automated continuation | Practical reliability |
|---|---|---|---|---|
| [Fluent](#fluent) | Not shown: supplied rationale | Not shown: people help settle revisions | Not met: internal human decisions | Not shown: practitioner-reported product operation |
| [Wheelhouse](#wheelhouse) | Not shown: human rulings | Not shown: people supply governing rulings | Not met: internal human decisions | Not shown: practitioner-reported factory operation |
| [OpenAI agent-first product](#openai-agent-first-product) | Not shown: supplied rationale | Not shown: people generalize failures | Not met: internal human decisions | Not shown: five months of reported human-agent work |
| [Warp skill improver](#warp-skill-improver) | Not shown: skill improvement | Not shown: people admit skill edits | Not met: internal human decisions | Not shown: no independent outcome assessment |
| [Darwin Gödel Machine](#dgm) | Not shown: coding benchmarks | Not shown: agent-code evolution | Not shown: benchmark loop | Not shown: reported coding-benchmark gains |
| [Huxley-Gödel Machine](#hgm) | Not shown: coding benchmarks | Not shown: parent selection through descendants | Not shown: benchmark loop | Not shown: reported coding-benchmark outcomes |
| [HyperAgents](#hyperagents) | Not shown: agent evolution | Not shown: executable patch lineage | Not shown: bounded generations; pinning gap | Not shown: no reproduced run in the review |
| [Autogenesis](#autogenesis) | Not shown: agent evolution | Not shown: broad mutation, weak selection | Not shown: incomplete implementations | Not shown: paper outcomes only |
| [Exo harness](#exo-harness) | Not shown: harness tooling | Not shown: self-editing tools only | Not shown: no automatic improvement trigger | Not shown: no live run in the review |
| [Prime Agent](#prime-agent) | Not shown: no theory-use test | Not shown: refinements can retain an exploit | Not shown: bounded autonomous goals | Not shown: reported cases include an exploit |
| [Memento-Skills](#memento-skills) | Not shown: answerable benchmarks | Not shown: oracle-selected skills | Not met: router training changes learned state | Not shown: reported benchmark outcomes |
| [Recuris](#recuris) | Not shown: memory benchmarks | Not shown: memory patches under supplied gate | Not shown: fixed-coordinate benchmark loop | Not shown: reported benchmark outcomes |
| [Harness Continual Learning](#harness-continual-learning) | Not shown: harness benchmarks | Not shown: edits checked on sampled anchors | Not shown: fixed-partition benchmark streams | Not shown: held-out forgetting is reported |
| [Dynamic Cheatsheet](#dynamic-cheatsheet) | Not shown: problem solving | Not shown: curator-admitted notes | Not shown: benchmark loop | Not shown: no reproduced outcomes in the review |
| [Voyager](#voyager) | Not shown: game skills | Not shown: critic-admitted skills | Not shown: game curriculum; pinning gap | Not shown: repository-reported game outcomes |
| [Knowledge-Centric Self-Improvement](#knowledge-centric-self-improvement) | Not shown: answerable benchmarks | Not shown: oracle-selected knowledge | Not shown: bounded task loop | Not shown: reported benchmark outcomes |
| [Rainbow](#rainbow) | Not shown: supplied model guides configuration | Not shown: fixed model and strategies | Not shown: runtime adaptation | Not shown: reported configuration outcomes |
| [Commonplace](#commonplace) | Not shown: one human-inclusive theory-use episode | Not shown: operator selects global fit | Not met: internal human decisions | Not shown: one episode; no reliability estimate |

## Evidence behind the rows

### Fluent

[Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
product documentation and its builder's report describe external stakeholders,
product code, deployment evidence, retained expertise, scheduling, rejection,
and reuse. People and the system jointly settle the brief, behaviour
specifications, and technical approach. Product operation is
practitioner-reported, and there is no independent estimate of reliability
under the four conditions.

### Wheelhouse

Steve Yegge reports a software factory in which human rulings progress from
custom to warnings, written doctrine, and programs that refuse actions.
Maintaining those rulings has costs: the corpus retained "old rulings that were
obsolete or had changed"
([Wheelhouse](../sources/steve-yegge-fences-not-sandboxes.ingest.md), verbatim).
Like Fluent, this is practitioner evidence of operation, without a reliability
estimate for an automated house.

### OpenAI agent-first product

OpenAI's five-month report describes agent-generated code, repository documents
that explain the business domain, and recurring documentation repair. People
perform the generalization: when agents struggle, engineers ask "what capability
is missing? What constraint is unenforced?" and build the tool, linter, or test
([agent-first product](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md),
verbatim).

### Warp skill improver

[Warp's scheduled skill improver](../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
depends on human feedback and review to admit its skill updates. The retained
source describes the production workflow but does not establish independent
outcomes for autonomous software-house operation.

### DGM

The Darwin Gödel Machine paper reports evolution of coding agents around frozen
foundation models. A separate fixed diagnostician uses the selected parent's
logs to suggest improvements. Admission requires viability: "Only agents that
compile successfully and retain the ability to edit a given codebase are added
to the DGM archive" ([Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md),
verbatim). Benchmark score weights parent sampling, but diagnostic rationale
is not shown to persist as a project explanation across generations. The
implementation was not independently inspected here.

### HGM

The [Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
paper reports that immediate benchmark score poorly predicts descendant
productivity. It targets the parent-selection layer DGM leaves fixed, also
around frozen models. The implementation was not independently inspected here.

### HyperAgents

The code-inspected [HyperAgents](../agent-memory-systems/reviews/hyperagents.md)
release replays patch lineages into the next generation's code. Its retained
memory is executable but carries no explanation. That is a limit of this
retained form and does not itself establish absence of program theory.

### Autogenesis

The code-inspected [Autogenesis](../agentic-systems/reviews/autogenesis.md)
protocol covers broad writable forms, but semantic selection is weaker than
versioning. Its mutation surface excludes model-weight updates, but it does not pin
model lineage. Public implementations are transitional or incomplete, and
outcomes remain paper reports.

### Exo harness

The inspected [Exo](../agentic-systems/reviews/exo.md) harness supports
self-inspection, revision, restart, rollback, and preserved failure evidence,
but has no automatic trigger from experience to improvement.

### Prime Agent

Prime Agent's inspected runtime retains versioned prompts, memories, skills,
and subagent specifications across trajectories without weight updates. One
reported case found a specification exploit and "preserved it as a reusable skill"
([Prime Agent](../sources/prime-agent-a-self-improving-rlm-harness.ingest.md),
verbatim). The case shows that persistence and rollback do not themselves
ensure sound admission.

### Memento-Skills

Memento-Skills reports learning skills that mix declarative instructions and
executable code, under benchmark answer oracles. It also trains a router, so
distributed-parametric models do not all remain fixed. Its optimization
ablation leaves "no failure attribution, no skill rewriting, and no skill
discovery"
([Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md),
verbatim).

### Recuris

The inspected Recuris mechanism proposes memory-component patches from traces
and decides each through a deterministic paired held-out gate. Four memory
coordinates, the gate, and benchmark partitions are supplied in advance.
Fixed distributed-parametric models and outcomes are paper-reported. Recuris
does not test acquiring an account of a user product's organization. Its
retention limit is explicit:
"The memory only grows, and it can afford to."
([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
verbatim)

### Harness Continual Learning

[Harness Continual Learning](../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
reports retaining edits only when they improve the current task, respect
sampled historical anchors, and pass validity checks. Updates to parsers,
skills, and routing workflows leave distributed-parametric models fixed. Held-out
forgetting persists even at zero loss on retained anchors, showing the limit
of those checks.

### Dynamic Cheatsheet

The inspected [Dynamic Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md)
loop curates notes from solver traces and injects them into later prompts. The
curator prompt is the only gate, and no software changes. The review neither
isolates a retained item's causal effect nor independently reproduces outcomes.

### Voyager

The inspected [Voyager](../agent-memory-systems/reviews/voyager.md) loop admits
executable skills on a critic's success report and overwrites a same-named
program rather than revising it. Its skill and QA indexes contain embeddings
derived from retained descriptions and questions. Such index generation is
allowed when the embedding model and algorithm are pinned, but the reviewed
code does not establish that pinning. The review does not isolate a retained
item's causal effect. Aggregate outcomes are repository-reported, without
independent reproduction in the review.

### Knowledge-Centric Self-Improvement

Knowledge-Centric Self-Improvement holds software and solver state fixed and
uses benchmark answers as an oracle. So the preprint isolates external
knowledge as the learned object: "The only object that changes is the
curated knowledge base."
([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim)

### Rainbow

The paper-reported [Rainbow](../sources/rainbow-architecture-based-self-adaptation.ingest.md)
architecture selects adaptation strategies using a causal model of a running
system. Its vocabulary, goals, constraints, operators, and strategies are
supplied and fixed. It reconfigures a running system rather than producing
and maintaining software under new requests. Its causal model is therefore
relevant as a mechanism comparison, without demonstrating program theory for
software production or learning that model and its action repertoire.

### Commonplace

Commonplace retains explanatory notes with scope and evidence and revises them
under review. Its [system-definition artifacts](../notes/definitions/system-definition-artifact.md)
describe the machinery. Models are not reliably pinned. One [evidence
note](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
records theory-guided computational search with the operator selecting global
fit, without ablation or autonomous successor selection.

## What the survey shows for the paradigm

The reviewed work supplies candidate components for learning by theory
refinement: retained notes and code, scheduled revision, gates capable of
rejection, and rollback with failure evidence. So the parts have precedents,
some inspected in code and others known only from papers or practitioner
reports. Where a product operates, it is reported with human authority
over internal decisions.

What the survey does not find is the paradigm's central mechanism under
test. In most of the research rows, what is retained is admitted by a score,
an oracle, a held-out gate, or a critic. The others replay or version
changes without such a gate, or have no automatic trigger from experience.
In none of them does the reviewed evidence test whether a retained
explanation guided a later decision on a case it did not state. In the
product rows, people supply the rationale and settle the revisions. The
evidence reviewed here includes no matched comparison of a retained
explanation against retained records of the same observations. That is a
finding about this reviewed evidence, not about what those systems could do.

The next test is therefore the same for both arrangements in the series:
combine these mechanisms under a declared boundary, and measure in a matched
comparison whether an explicit theory improves the resulting process.

## What a witness run would have to show

Use the conjecture's [four conditions and the protocol declared before
testing](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md#what-a-witness-house-must-show)
together. The reviewed mechanisms suggest a maintained user product with
incrementally revealed requests, delayed consequences that challenge earlier
assumptions, and later changes, in parts the earlier repair did not modify,
that test recovery. Admission, rollback, and conflict resolution must
continue without internal human decisions.

Test causal use of program theory at matched decisions. An intervention on one
written record is inconclusive if the house reconstructs equivalent
understanding from other records, so the test must control or measure that
route. An explicit theory artifact is optional. Acquiring understanding and
machinery absent from the seed is the further question developed by the
[lead article](./conjectural-learning-with-fixed-models.md) and the
[bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md).

## The separate test for an explicit theory

The table concerns program theory, whatever form holds it. A narrower question
is whether an explicit written theory improves learning compared with other
uses of the same evidence. The evidence supplement's [component
experiment](./testing-the-conjectural-learning-program.md#component-experiments-that-can-run-first)
compares an explicit theory, raw records, a descriptive summary, and a
plausible wrong theory across changes that preserve or break the theory's
assumptions. It can run before a complete witness house exists, and it
specifies the treatments and their limits.

A supplied theory tests use and revision. To test acquisition, withhold the
decisive rationale from the seed while retaining the records from which it can
be synthesized, and count the cost of forming it. A claim about a whole
system learning additionally requires these updates and later production to
continue without internal human decisions.
