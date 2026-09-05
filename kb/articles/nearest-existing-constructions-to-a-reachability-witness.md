---
description: "Eighteen constructions with local review or evidence compared against the automated software house conjecture's four witness conditions, which allow a human-built start; plus the explicit-theory test from the training article"
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

The [automated software house conjecture](./automated-software-houses-with-fixed-llms.md)
proposes that a complete persistent producer can keep developing software for
users across demands not listed in advance, with learned components available
by 2026-09-02 held fixed and no human production decisions. This comparison
maps eighteen constructions against its four witness conditions: holding and
application, coherent revision, automated continuation, and practical
reliability. It identifies available mechanisms and missing evidence; no row
demonstrates the conditions together.

## How to read the table

Each column asks about one witness condition. Cells identify relevant evidence
and its limit within the reviewed source's scope. Retained patches need not
establish coherent product revision, and an autonomous benchmark loop need not
meet the complete [software-house boundary](../notes/definitions/software-house.md).

**Holding and application** requires project-specific commitments to guide
novel changes, including unstated implications. **Coherent revision** requires
revision from later consequences that supports continued modification.
**Automated continuation** requires both capacities across the declared product
scope with pinned learned components and no internal human decisions.
**Practical reliability** requires useful success across the declared horizon
and budget, supported by repeated runs or another justified estimate.

No row establishes reliability under the full witness conditions. The final
column records narrower outcomes or gaps in their assessment. The accounts below
separately identify code inspection, papers, and practitioner reports as
sources. Implementation evidence establishes mechanisms; outcome evidence
assesses performance. Reported outcomes were not independently reproduced here.

## Comparison table

| Construction | Holding and application | Coherent revision | Automated continuation | Practical reliability |
|---|---|---|---|---|
| Fluent | Supplied rationale; causal use untested | People help settle revisions | Internal human decisions; pinning unshown | Product operation; no witness reliability estimate |
| Wheelhouse | Human rulings; computational theory use unshown | People supply the governing rulings | Internal human decisions | Practitioner account only |
| OpenAI agent-first product | Supplied rationale; causal use untested | People generalize failures into machinery | Internal human decisions; pinning unshown | Five months of human-agent product work |
| Warp skill improver | Program theory outside tested scope | People supply feedback and admit skill edits | Internal human decisions | No independently assessed outcomes |
| Darwin Gödel Machine | Program theory outside tested scope | Agent-code evolution on benchmarks | Autonomous benchmark loop; no product demand stream | Coding-benchmark improvements |
| Huxley-Gödel Machine | Program theory outside tested scope | Parent selection tested through descendants | Autonomous benchmark loop; no product demand stream | Coding-benchmark outcomes |
| HyperAgents | Program theory outside tested scope | Executable patch lineage; rationale absent | Bounded generations; model pinning unshown | No reproduced run or outcome in the review |
| Autogenesis | Program theory outside tested scope | Broad mutation paths; weak semantic selection | Implementations transitional or incomplete | Paper outcomes; incomplete inspected implementations |
| Exo harness | Program theory outside tested scope | Self-editing tools; no automatic learning trigger | Scheduling and restart, without an improvement loop | No live instance run in the review |
| Prime Agent | Program theory untested | Retained refinements can include an exploit | Bounded autonomous goals; producer boundary unshown | Cases include a retained exploit |
| Memento-Skills | Program theory outside tested scope | Skills revised under answer oracles | Bounded task loop; router training changes learned state | Answerable-benchmark outcomes |
| Recuris | Program theory outside tested scope | Memory patches pass a supplied gate | Fixed memory coordinates and benchmark loop | Benchmark outcomes only |
| Harness Continual Learning | Program theory outside tested scope | Harness edits checked against sampled anchors | Fixed harness partition and benchmark streams | Held-out forgetting despite retained-anchor checks |
| Dynamic Cheatsheet | Program theory outside tested scope | Curated notes; correctness does not gate retention | Sequential benchmark loop; pinning unshown | No independently reproduced outcomes |
| Voyager | Program theory outside tested scope | Critic-admitted skills; no theory-revision test | Game curriculum; model pinning unshown | Game outcomes only |
| Knowledge-Centric Self-Improvement | Program theory outside tested scope | Knowledge-only revision under benchmark oracles | Bounded autonomous task loop | Benchmark outcomes only |
| Rainbow | Supplied causal model drives configuration | Governing model and strategies remain fixed | Automatic configuration adaptation | Configuration-adaptation outcomes |
| Commonplace | One human-inclusive use of retained theory; no ablation | Operator supplies decisive global-fit judgments | Internal human decisions; models not reliably pinned | One episode; no evaluated witness outcome |

## Evidence behind the rows

The following accounts explain the mechanisms and evidence limits behind the
comparison.

### User-product operation and human admission

[Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
product documentation and its builder's report describe external stakeholders,
product code, deployment evidence, retained expertise, scheduling, rejection,
and reuse. People and the system jointly settle the brief, behaviour
specifications, and technical approach.

OpenAI's five-month report describes agent-generated code, repository documents
that explain the business domain, and recurring documentation repair. People
perform the generalization: when agents struggle, engineers ask "what capability
is missing? What constraint is unenforced?" and build the tool, linter, or test
([agent-first product](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md),
verbatim).

Steve Yegge reports human rulings progressing from custom to warnings, written
doctrine, and programs that refuse actions. Maintaining those rulings also has
costs: the corpus retained "old rulings that were obsolete or had changed"
([Wheelhouse](../sources/steve-yegge-fences-not-sandboxes.ingest.md), verbatim).
[Warp's scheduled skill improver](../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
likewise depends on human feedback and review to admit its skill updates.

### Self-rewriting agents and persistent substrates

The Darwin Gödel Machine paper reports evolution of coding agents around frozen
foundation models. A separate fixed diagnostician uses the selected parent's
logs to suggest improvements. Admission requires viability: "Only agents that
compile successfully and retain the ability to edit a given codebase are added
to the DGM archive" ([Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md),
verbatim). Benchmark score weights parent sampling; diagnostic rationale is not
shown to persist as a project explanation across generations.

The [Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
paper reports that immediate benchmark score poorly predicts descendant
productivity. It targets the parent-selection layer DGM leaves fixed, also
around frozen models. Neither implementation was independently inspected here.

The code-inspected [HyperAgents](../agent-memory-systems/reviews/hyperagents.md)
release replays patch lineages into the next generation's code. Its retained
memory is executable but carries no explanation. The code-inspected
[Autogenesis](../agentic-systems/reviews/autogenesis.md) protocol covers more
writable forms, but semantic selection is weaker than versioning. Its mutation
surface excludes model-weight updates without pinning model lineage; public
implementations are transitional or incomplete, and outcomes remain paper
reports.

The inspected [Exo](../agentic-systems/reviews/exo.md) harness supports
self-inspection, revision, restart, rollback, and preserved failure evidence,
but has no automatic trigger from experience to improvement. Prime Agent's
inspected runtime carries versioned prompts, memories, skills, and subagent
specifications across trajectories without weight updates. One reported case
found a specification exploit and "preserved it as a reusable skill"
([Prime Agent](../sources/prime-agent-a-self-improving-rlm-harness.ingest.md),
verbatim): persistence and rollback do not themselves ensure sound admission.

### Benchmark-scoped retained learning

[Harness Continual Learning](../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
reports retaining edits only when they improve the current task, respect
sampled historical anchors, and pass validity checks. Updates to parsers,
skills, and routing workflows leave learned components fixed. Held-out
forgetting persists even at zero loss on retained anchors, showing the limit
of those checks.

Memento-Skills reports learning mixed-form skills—declarative instructions and
executable code—under benchmark answer oracles. It also trains a router, so
learned components do not all remain fixed. Its optimization ablation leaves
"no failure attribution, no skill rewriting, and no skill discovery"
([Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md),
verbatim).

The inspected Recuris mechanism proposes memory-component patches from traces
and decides each through a deterministic paired held-out gate. Four memory
coordinates, the gate, and benchmark partitions are supplied in advance; fixed
learned components and outcomes are paper-reported. It does not test acquiring
an account of a user product's organization. Its retention limit is explicit:
"The memory only grows, and it can afford to."
([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
verbatim).

The inspected [Dynamic Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md)
loop curates notes from solver traces and injects them into later prompts. The
curator prompt is the only gate; no software changes. The inspected
[Voyager](../agent-memory-systems/reviews/voyager.md) loop admits executable
skills on a critic's success report and overwrites a same-named program rather
than revising it. Its skill and QA indexes contain embeddings derived from
retained descriptions and questions. Such index generation is allowed when the
embedding model and algorithm are pinned; the reviewed code does not establish
that pinning. Neither review isolates a retained item's causal effect.
Voyager's aggregate outcomes are repository-reported; neither system's outcomes
were independently reproduced in the reviews.

Knowledge-Centric Self-Improvement holds software and solver state fixed and
uses benchmark answers as an oracle: "The only object that changes is the
curated knowledge base."
([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim). The preprint thereby isolates external knowledge as the learned
object.

### Fixed-model adaptation and the reference construction

The paper-reported [Rainbow](../sources/rainbow-architecture-based-self-adaptation.ingest.md)
architecture selects adaptation strategies using a causal model of a running
system. Its vocabulary, goals, constraints, operators, and strategies are
supplied and fixed. The model drives adaptation without the system learning
that model or its action repertoire.

Commonplace retains explanatory notes with scope and evidence and revises them
under review. Its [system-definition artifacts](../notes/definitions/system-definition-artifact.md)
describe the machinery; models are not reliably pinned. One [evidence
note](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
records theory-guided computational search with the operator selecting global
fit, without ablation or autonomous successor selection.

## What a witness would have to do

The missing evidence suggests a test with five checks:

1. With learned components pinned, maintain one user product over a declared
   horizon and a predeclared process of incrementally revealed requirements and
   operating consequences. The seed may be human-built.
2. Handle implications not stated verbatim in retained state. Withholding or
   replacing the relevant state or consumption path must change proposal,
   evaluation, diagnosis, or recovery as predicted.
3. When a later consequence defeats part of the earlier understanding, use
   that evidence to revise the product, retained state, or machinery and
   support further coherent modification.
4. Continue through admission, rollback, and conflict resolution without human
   design, diagnosis, theory editing, candidate comparison, or successor
   selection. Users may supply requirements, facts, observed outcomes, and
   judgments about visible behaviour.
5. Evaluate untouched later changes and estimate success within the declared
   budget through repeated runs or another justified method.

Reliable reconstruction from records or mixed carriers can satisfy these checks;
an explicit theory artifact is optional. Acquisition of understanding and
machinery absent from the seed is a further question for the
[training](./the-software-house-as-the-unit-of-training.md) and
[bootstrap](./bootstrapping-the-first-automated-software-house.md) articles.

## The test for explicit project theory from the training article

The training article asks whether an explicit explanation improves learning
compared with other uses of the same production evidence. Its [component
experiment](./the-software-house-as-the-unit-of-training.md#testable-hypotheses)
compares theory, raw records, a descriptive summary, and a plausible wrong
theory across changes that preserve or break assumptions. It can run before a
complete witness exists.

The prediction combines useful transfer while an account applies, specific
misdirection when it is wrong, and recovery after contrary evidence. Errors
under a wrong theory establish influence; an advantage also needs better
transfer or recovery relative to the controls, with observations and total
cost counted. The training article specifies the treatments and their limits.

A supplied theory tests use and revision. To test acquisition, withhold the
decisive rationale from the seed while retaining the records from which it can
be synthesized, and count the cost of forming it. A whole-house training claim
additionally requires these updates and later production to continue without
internal human decisions.

## What the set shows together

The reviewed work supplies candidate components: retained notes and code,
scheduled revision, gates capable of rejection, and rollback with failure
evidence. Product operation is reported with human authority. What remains to
be shown is reliable composition under the witness conditions, and whether
explicit theory improves that process in the matched comparison.
