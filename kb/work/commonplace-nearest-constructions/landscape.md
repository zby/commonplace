# Nearest existing constructions to Commonplace

Working landscape. The evidence cutoff is 2026-09-03 and the local baseline is
repository commit `6c73908fb7a0aab2b47284abbccd3ed763daae3b`.

## Working result

Within the reviewed corpus, no construction is nearest to Commonplace across
all three lenses. Different systems are near different parts of it, and
collapsing those relations into one ranking hides the main result.

- **Commonplace today:** Ars Contexta is closest to an agent-operated
  methodology environment; AI Research OS is closest in inspectable Markdown
  medium and source-to-synthesis structure; Eigenius is closest in typed
  epistemic objects and checked commit routes. None combines Commonplace's
  theory-building purpose, collection and type contracts, semantic review, and
  current human-agent allocation.
- **Commonplace's development path:** Ars Contexta comes closest to turning
  corrections and session evidence into methodology observations and later
  system changes. Among reviewed systems, GBrain has the broadest implemented
  operational machinery for capture, consolidation, scheduled maintenance,
  retrieval, and gated skill revision. Both expose useful pieces of the missing
  path; neither establishes reliable acquisition and admission of the
  operator's recurring semantic judgments.
- **The conjectured endpoint:** Fluent is closest to the software-house
  topology, while Exo is closest to broad agent-executed self-revision and
  recovery. Recuris, Memento-Skills, and Harness Continual Learning contribute
  bounded attribution and admission mechanisms. No witness to the
  [reachability
  conjecture](../../articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md)
  was located in the reviewed corpus.

The nearest-neighbor picture is therefore composite only as a research heuristic:
Commonplace-like theory and governance, Ars Contexta- or GBrain-like trace
processing, Exo-like self-revision and recovery, Fluent-like product operation,
and bounded-learning admission mechanisms. This list does not show that the
parts compose, that their objectives agree, or that the resulting system could
acquire and revise an adequate theory.

## Commonplace as the reference construction

### Starting purpose and first implementation

Commonplace began as a tool for a human operator, not as an autonomous coding
agent. Its founding function can now be stated as **theory building**: help the
operator develop, criticize, connect, and retain theories about how agentic
systems should be built. The first implementation was a knowledge-base
framework. The KB remains the first worked application in which theories about
retrieval, representation, review, validation, and self-modification meet real
operating constraints together; it is not the final program boundary, as
[Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md)
states.

The direction was always for the system to perform more of this work from less
and less task-specific human input. That does not mean eliminating all human
input or optimizing for fewer operator hours. It means increasing useful and
better-warranted work per consequential human judgment, while moving the
remaining judgments toward harder questions and longer horizons. [Increasing
computational autonomy relocates human effort to the
frontier](../../notes/increasing-computational-autonomy-relocates-human-effort.md)
states that objective more precisely.

This starting point differs from most nearby constructions surveyed. Harness
optimizers begin with a task loop and add enough retained state to improve a
score. Software factories begin with application production and add documents,
feedback, and governance. Commonplace begins with semantic work: forming
explanations, assessing their fit and warrant, revising them under contrary
evidence, and integrating them into a larger theory.

### Current human-inclusive construction

Under [the declared Commonplace
frame](../../reference/commonplace-declared-frame.md), the repository, its
operative artifacts and software, the agents that consume them, and designated
maintainers form one system. Model weights and their provider remain outside.
Agents already perform substantial search, comparison, synthesis, criticism,
drafting, and implementation. Natural-language theory, instructions, schemas,
validators, review state, and code retain accepted changes and affect later
work.

The operator still supplies decisive judgments about research direction,
global theoretical fit, semantic admission, and system design where no
adequate check exists. Commonplace is therefore classified, relative to its
declared boundary, as a bounded human-inclusive [reflective self-improving
system](../../notes/evidence/commonplace-as-a-reflective-system.md), not as an
autonomous theory learner. A [2026-08-30 revision
trace](../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
shows retained theory guiding model-mediated search while the operator supplied
sparse but decisive global-fit corrections. That is evidence for one mixed
human-computational pathway, not for computational theory acquisition.

### Developmental path: less task-specific human input

The working path is function-by-function transfer rather than an undifferentiated
increase in autonomy:

```text
human operator + theory-building assistant + retained theory and software
  -> an operator or agent notices and formulates a task-local problem       [current]
  -> a candidate changes a note, procedure, check, route, schema, or code   [current]
  -> review, validation, use, and later consequences test the change        [partial]
  -> accepted machinery lets later runs perform more of that function       [partial]
  -> human input becomes less frequent and less task-specific               [direction]
  -> the system repairs limits in its own supporting software               [endpoint]
  -> a computational theory builder that is also a software house           [endpoint]
```

> **Current automation boundary.** If the operator repeatedly supplies the same
> distinction, notices the same kind of gap, identifies the same artifact to
> revise, or makes the same admission decision, Commonplace does not
> systematically capture that intervention, recognize its recurrence across
> episodes, or convert it into a candidate change. The operator or an agent must
> presently notice and formulate the pattern in a task-specific episode.

The missing automatic bridge is therefore:

```text
operator intervention traces
  -> cross-episode recurrence recognition
  -> a scoped candidate with evidence and provenance
  -> testing and semantic admission
  -> a behavior-changing retained artifact
```

A human-recognized recurrence can already influence Commonplace. What is absent
is an end-to-end recurrence-to-candidate loop. Existing mechanisms distribute
task-local noticing and drafting across agents, skills, reports, freshness
checks, and validators, but they neither observe operator interventions as a
class nor close unattended triage and promotion. The [candidate-source
survey](../../reference/where-change-candidates-come-from-in-commonplace.md)
and [agent-memory gap
plan](../../reference/commonplace-agent-memory-gap-plan.md) describe the
present mechanisms and missing prerequisites.

The existing [bootstrap
account](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
describes the larger direction as learning while constructing the machinery
that makes further learning selectable. The missing automatic bridge above is
one concrete part of that direction.

A human function should move only when its required premises are represented,
its method or authority is settled enough to act, plausible errors can be
defeated, and later consequences can reach the responsible artifact. [The
decisions that stay
human](../../articles/the-decisions-that-stay-human-and-what-would-move-them.md)
develops those transfer conditions. Replacing an approval with another model
call does not by itself satisfy them.

### Working program thesis: theory building and software building converge

The realization that motivates the current program is stronger than “a theory
builder needs some tooling.” Under open-ended operation, a theory builder will
eventually encounter material its current software cannot represent, retrieve,
compare, test, schedule, or govern. Supporting a new source kind may require a
snapshot path; a new relation may require a schema and validator; a larger
corpus may require a different index; a new review problem may require another
evaluator or execution path.

At that point, either a person changes the supporting software or the theory
builder does. If the same person repeatedly diagnoses and implements such
changes, that person remains an internal production and theory-holding
component. A computational theory builder that brings the function inside must
keep developing software in response to the demands of its external users. In
the [software-house definition](../../notes/definitions/software-house.md), it
has become a software house. This is a working thesis about open-ended
operation, not an empirically established inevitability.

The implication also runs from software building toward theory building, under
the narrower condition that the software must remain coherent across novel
demands whose fit cannot be decided by existing checks. Such a software house
must preserve, apply, criticize, and sometimes revise an explanation of why the
product is organized as it is. The proposed research object is therefore one
coupled system approached from two directions: theory work creates demands for
new machinery, while coherent software change creates demands for theory.

### Three comparison lenses

| Lens | Object being compared | Questions that determine proximity |
|---|---|---|
| **Present construction** | The human-inclusive theory builder operating now | Does the system serve theory or knowledge work; retain inspectable claims, evidence, rationale, and system definitions; route them into later work; distinguish their authority; and govern semantic admission? |
| **Developmental path** | The process by which more functions could move from repeated operator judgment into retained capacity | Does the system capture interventions or traces, recognize recurrences, attribute evidence, form scoped candidates, revise natural-language and symbolic artifacts, test and admit them, recover from failure, reactivate them later, and measure the resulting change in human contribution? |
| **Conjectured endpoint** | A computational theory builder that is also a software house | Does one fixed-model lineage maintain software for external users, acquire and revise program theory, change both software and natural-language state, and continue over a declared scope and horizon without a human in an internal production or theory-holding role? |

“Partial” means that a mechanism exists but its causal role, scope, evidence, or
actor allocation falls short of the named lens. It is not half credit toward a
single score.

## Landscape map

| Construction | Nearest lens or function | What it contributes | Decisive divergence from Commonplace | Evidence basis |
|---|---|---|---|---|
| [Ars Contexta](../../agent-memory-systems/reviews/arscontexta.md) | Present operating shape; recurrence-to-methodology path | Agent-operated file graph, generated instructions and hooks, session/correction mining, observation and tension state, later promotion or implementation | Most extraction and promotion judgment is encoded in LLM skill procedure; reliable cross-episode recognition and behavioral improvement are not established | Code-grounded review |
| [AI Research OS](../../agent-memory-systems/reviews/ai-research-os-workshop.md) | Present knowledge medium | Inspectable Markdown, immutable sources, source/synthesis separation, progressive pull, deterministic indexes | It continuously rewrites a topic wiki, has no reject-capable content-acceptance step, and does not promote learned knowledge into system-definition artifacts | Code-grounded review |
| [Agent Skills for Context Engineering](../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) | Methodology corpus and research-to-skill promotion | File-first skills, source and claim provenance, run gates, mechanism records, validation, router benchmarks, and example trace-to-skill tooling | Published skills remain authored or human-reviewed; the trace optimizer is example scope rather than a standing cross-task learning loop | Code-grounded review |
| [GBrain](../../agentic-systems/gbrain.md) | Operational development machinery | Trace and signal capture, fact/take/concept promotion, scheduled consolidation, durable jobs, retrieval, and gated skill revision | A larger database/runtime surface carries much of the authority; semantic admission uses machine oracles and uneven provenance rather than Commonplace's slower explicit theory governance | Code-grounded whole-system and memory reviews |
| [Eigenius](../../agentic-systems/eigenius.md) | Typed epistemic governance | Typed graph objects, epistemic grades, certificates, route-specific validation, optional proof checking | The host supplies the reasoning protocol and calls; the system does not own a continuing theory-building loop, and formal validity does not establish content truth or explanatory quality | Code-grounded analysis |
| [ScienceFlow](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) | Long-horizon research continuation | Recoverable workspaces, retained evidence, bounded memory, evaluated stages, re-anchoring, and resource control | Its evaluators and stage decomposition are fixed; explanation is not a retained governing object and the reported outcomes are not independently reproduced | Code-grounded mechanisms; paper-reported outcomes |
| [Fluent](../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) | Software-house topology | Users, product code, rationale-bearing work packets, expertise, rejection, deployment evidence, and corrective follow-ups | People retain consequential context, judgment, expertise, and authority; program-theory acquisition is not tested | Public repository and practitioner account |
| [Wheelhouse](../../sources/steve-yegge-fences-not-sandboxes.ingest.md) | Human-inclusive cross-form learning | Incidents and rulings can become doctrine, warnings, and executable fences | The operator supplies the generalization and verdict; implementation and outcomes are not independently inspectable | Practitioner account |
| [Exo](../../agentic-systems/exo.md) | Mutable and recoverable runtime | Broad agent-executed self-editing, source inspection, build/test/restart, rollback, event history, and scheduling | It has no demonstrated theory-building service, automatic trace-to-improvement trigger, or semantic gate for delayed product fit | Code-grounded analysis |
| [Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md), [Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md), and [Harness Continual Learning](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) | Bounded attribution and admission | Trace-based patching, mixed-form skills, regression anchors, rollback, and fixed-model continuation | Benchmarks and supplied decompositions provide the objective and oracle; none maintains a changing user product or acquires its theory | Papers and pinned implementations where available |
| [Knowledge-Centric Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Knowledge as the learned object | Cross-task forums and distilled natural-language guidance isolate improvement in an external knowledge base | The protocol deliberately fixes software and uses benchmark answers; it does not build a connected, governed theory or revise its supporting system | Paper |
| [Rainbow](../../sources/rainbow-architecture-based-self-adaptation.ingest.md) | Historical model-mediated adaptation | A live architectural model, probes, constraints, and strategies govern adaptation | Designers supply the model, goals, operators, and strategies; the system does not learn or revise that governing theory | Paper and historical implementation account |

The table names nearest relations, not a winner. In particular, AI Research OS
is nearer in medium than in governance; GBrain is nearer in operational
learning machinery than in inspectability; Fluent is nearer in production
topology than in actor allocation; and Exo is nearer in mutation reach than in
semantic selection.

## Nearest constructions to Commonplace's present and path

### Ars Contexta is closest to the agent-operated methodology shape

Ars Contexta treats the knowledge base as an agent-operated methodology
environment rather than a passive memory store. Like Commonplace, it uses
plain files, explicit spaces and conventions, search-friendly descriptions,
validation, and procedures that agents execute. Its `/remember` path can mine
current corrections or stored sessions for repeated redirections, workflow
breakdowns, agent confusion, and undocumented decisions. `/rethink` can then
classify accumulated observations and tensions for promotion, implementation,
methodology change, archiving, or continued observation.

That makes Ars Contexta the closest reviewed construction to the exact missing
transition named by the operator. The qualification is decisive: much of the
capture, recurrence judgment, classification, and promotion policy is a
natural-language skill executed by an LLM, not an independently verified
automatic loop. The review establishes an implemented and instructed path. It
does not establish faithful recognition of the same distinction across
episodes, warranted admission, or improved later behavior.

### AI Research OS is closest in knowledge medium

AI Research OS uses immutable source material, per-source pages, concept and
entity pages, cross-source comparisons, synthesis, explicit open questions,
and deterministic indexes in a local Markdown research directory. Its staged
read path and source/synthesis separation closely resemble Commonplace's
inspectable medium and progressive pull.

The systems differ at admission and durability. AI Research OS lets later
ingests rewrite its wiki and retains every generated page without a
reject-capable content gate. Structural lint can find broken links, missing
hubs, and possible stale claims, but does not establish faithfulness or
explanatory quality. Generated knowledge also remains knowledge; it does not
become a validator, schema, or operating instruction through a governed
promotion path.

### GBrain is closest in implemented operational learning machinery

GBrain combines a Markdown-facing brain with a Postgres-shaped active store,
hybrid retrieval, typed operations, background jobs, scheduled maintenance,
trace and signal extraction, consolidation into stronger knowledge objects,
and SkillOpt revision. Its host protocol asks for per-message signal detection;
its owned dream cycle creates and maintains facts, takes, patterns, concepts,
and skill candidates; its durable queue supports crash-resumable subagents.
This is a much more complete operational answer to capture and continuation
than Commonplace currently has.

It is not simply a more automated Commonplace. Much of its active authority
lives in database state, ranking machinery, daemons, and LLM maintenance calls.
Default capture creates curation and provenance risks that Commonplace avoids
by default exclusion. SkillOpt's strongest automatic changes are evaluated
against supplied tasks and scores, while bundled-skill changes remain proposals
for human review. The comparison is an architectural trade, not an ordered
maturity claim.

Agent Skills for Context Engineering is a nearer neighbor on the narrower
corpus-maintenance path. Its researcher OS records sources, proposed and
rejected mechanisms, claim provenance, run readiness, and benchmark results
before changes reach a skill corpus. It also contains trace-to-skill tooling,
but that tooling is example scope and normal promotion remains reviewed. The
[cross-system trace-learning
survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md)
owns the more detailed comparison of capture, extraction, promotion, and
reinjection mechanisms; this landscape uses only their relation to
Commonplace's development path.

### Eigenius and ScienceFlow supply governance and continuation pieces

Eigenius gives epistemic objects and program outputs typed commit paths,
certificates, validation, pinned layers, and optional proof checking. It is a
near neighbor for Commonplace's attempt to distinguish artifact authority and
make some admission conditions executable. Its agent reasoning method is
manually loaded by the host, however, and its strongest checks establish
formal or structural validity rather than the truth, faithful encoding, or
explanatory quality of natural-language content.

ScienceFlow is nearer on sustained research execution. It separates reversible
workspace state from retained evidence, admits evaluated stages, folds memory
without deleting the raw ledger, restores earlier anchors, and controls
resources from validated progress. The task adapter, evaluator, stage trigger,
and response vocabulary remain supplied. Unlike Commonplace, it does not make
claims, explanations, or a revisable working theory the governing retained
object.

ARC is a useful mechanism-level neighbor rather than a nearest whole-system
construction. Its pre-action predictions, post-action consequence grading,
provenance-bounded plans, executable replay, and halt-on-surprise behavior show
why authority must be traced per route. They do not amount to a general
theory-building or software-house loop; the [epistemic-architectures
workshop](../epistemic-architectures/README.md) keeps that comparison.

## Commonplace and Exo

Exo is the sharpest direct comparison for Commonplace's development path
because the two systems start from opposite scarce resources. Exo permits broad
agent-executed self-modification but lacks a strong semantic basis for deciding
which changes are improvements. Commonplace has built a comparatively rich
semantic and governance substrate but still depends on the operator for the
highest-level theory and admission judgments.

Technical basis: the code-grounded [Exo whole-system
analysis](../../agentic-systems/exo.md) and [Exo memory-system
review](../../agent-memory-systems/reviews/exo.md).

| Dimension | Commonplace today | Exo harness |
|---|---|---|
| Starting purpose | Help a human operator build and assess theories about agentic systems | Let a long-running personal agent inspect and rewrite as much of its own runtime as safely practical |
| Primary self-representation | Distributed typed notes, collection contracts, instructions, ADRs, schemas, validators, and code | A literal source tree, injected self-map, prompts, tools, adapters, skills, memory, and executor code |
| Mutable surface | Natural-language theory and system-definition artifacts can both change, but consequential changes remain human-gated | The agent can rewrite the executor, prompts, tools, adapters, and memory machinery; the Rust substrate is protected by default policy |
| Preserved evidence | Git history, source snapshots, review results, freshness state, and retained artifacts | An append-only event stream and versioned artifacts survive sandbox rewind and failed executor changes |
| Context strategy | Selective pull through search, indexes, links, skills, and explicit routing | Full conversation replay plus coarse-pushed memory and skill descriptions, with skill bodies pulled on demand |
| Admission strength | Structural validation plus semantic review and operator judgment; broad automatic promotion is deliberately absent | Build, tests, module-shape checks, restart observation, and rollback; no independent semantic judge or mandatory canary |
| Current improvement trigger | Task-local human or agent noticing; operator interventions are not systematically captured or clustered | Deliberate model or human self-editing using inspectable state; no implemented automatic trace-learning or self-maintenance trigger |
| Theory-building role | Explicit purpose, with retained theory already guiding search; operator still decides global fit | No explicit service or evaluation for acquiring and revising a theory of an external product |
| Autonomy direction | Move one function at a time when representation, method, correction, and warrant support the transfer | Maximize mutable agent control while keeping a small recovery and safety substrate fixed |
| Main missing bridge | Automatic evidence capture, recurrence detection, credit assignment, semantic admission, and sustained continuation | An objective-bearing semantic theory, delayed evidence attribution, and a gate able to judge more than buildability and immediate behavior |

Exo therefore supplies several pieces Commonplace does not yet have: a durable
execution-event substrate, an explicit protected-substrate/mutable-policy
boundary, model-accessible self-inspection, rebuild-and-restart, recovery that
preserves failed-attempt evidence, and scheduled continuation. Commonplace
supplies what Exo deliberately leaves thin: explicit surfaces for typed
knowledge claims, rationale, and provenance; separation between knowledge and
system-definition authority; semantic review; and an explicit account of which
human judgments have not yet moved. Those surfaces do not guarantee complete
rationale coverage or end-to-end continuity.

Neither can be described as the other with one component added. Giving
Commonplace Exo's rewrite and restart machinery would not automate theory
selection. Giving Exo Commonplace's notes would not make them a causally active
or faithfully acquired program theory. The constructive question is whether
the two control directions can be joined: Exo-like operational self-revision
constrained by Commonplace-like theory, evidence, and admission, with recurring
operator judgments progressively—but not yet automatically—turned into
testable changes to both.

Commonplace's distinctive wager is the direction of construction: begin with a
human-guided theory-building loop whose decisions and rationale are explicit;
use operation to expose where that loop fails; retain and test changes to both
the theory and its machinery; and progressively contract the human role without
discarding the semantic function that made the system useful. This is a more
specific approach than “the LLM stays fixed and external memory learns,” but it
remains a program direction rather than evidence that the final contraction is
reachable.

## Endpoint lens: reachability witness obligations

The original search asked which systems come closest to the reachability
conjecture. Its six questions remain useful as an endpoint-specific view, but
they do not rank proximity to Commonplace today or to its development path:

1. **House:** Does it keep changing software for external users across demands
   that are not a fixed benchmark list?
2. **Fixed model:** Can the documented learning occur without changing the
   foundation-model weights, and is that condition actually held or pinned?
3. **Software learning:** Does experience cause a retained executable or
   codified change that affects later production?
4. **Note learning:** Does experience cause a retained natural-language change
   that is read back into later production?
5. **Program theory:** Is rationale-bearing project understanding acquired and
   applied, rather than merely supplied, logged, or paraphrased? Is an
   inadequate rationale later replaced from consequences?
6. **Continuation:** Is the relevant loop sustained with no human in an
   internal production, theory-holding, generalization, selection, or
   admission role?

The table retains the candidates selected by that narrower search. Its cells
are mechanism judgments, not uniform evidence grades; the map and detailed
sections state whether support comes from inspected code, papers, product
documentation, or practitioner reports. “Partial” means that a mechanism
exists but its causal role, scope, or actor allocation does not satisfy the
endpoint condition.

| Construction | House | Fixed model | Software learning | Note learning | Program theory | No-human continuation | Decisive shortfall |
|---|---|---|---|---|---|---|---|
| Commonplace today | Not assessed; present target is the theory-building instrument | Compatible; realization not reliably pinned | Partial, human-inclusive | Yes, human-inclusive | Partial, with operator selection | No | Global fit, semantic admission, and unsupported system-design decisions remain human |
| Fluent | Reported yes | Partial | Reported yes | Reported yes | Partial; faithful acquisition and reuse unverified | Partial | Humans confirm behavior, technical approach, and unresolved decisions; theory acquisition is not tested |
| Wheelhouse | Yes | Unclear | Partial | Partial | Unshown | No | Human rulings and verdicts produce doctrine; Frog's theory-holding role is only a hypothesis |
| Ona Memo factory | Bounded trial | Unclear | Partial | Partial | Unshown | No | Humans built the harness, specified taste and intent, and retained product direction |
| OpenAI agent-first product | Yes | No pinned lineage | Partial | Partial | Partial | No | Humans made the repository legible and turned failures into tools, rules, and checks |
| Warp skill improver | Partial | Unclear | No | Yes | No | No | Human feedback supplies evidence and human PR review admits every skill update |
| Exo harness | No | Compatible | No demonstrated learning; broad self-edit capability | No demonstrated learning; deliberate authoring path | No | Partial; scheduling and restart exist, automatic improvement does not | It rewrites a personal-agent executor, not a user product; build/tests do not judge program theory |
| Prime Agent | No demonstrated house | Yes in reported refinement | Partial | Yes | No | Yes, within bounded goals | Persistent refinement is directly adopted and has preserved a specification exploit; no product-theory test |
| Autogenesis | No | Yes | Yes | Yes | No | Partial | Benchmarks and a weak semantic gate; the public implementations are transitional or incomplete |
| Recuris | No | Yes | Partial | Yes | No | Yes, within a fixed gate | Four predeclared memory coordinates and benchmark tasks; no project rationale or product demand stream |
| Memento-Skills | No | Yes | Yes | Yes | No | Yes, within its task loop | Mixed-form skills learn under answer oracles, not delayed software-maintenance consequences |
| Harness Continual Learning | No | Yes | Partial | Yes | No | Yes, within its task loop | Finite benchmark streams and a fixed four-part harness partition; held-out forgetting remains |
| Knowledge-Centric Self-Improvement | No | Yes | No | Yes | No | Yes, within its task loop | It deliberately isolates knowledge-only learning on benchmark families |
| PROJECTMEM | No | Compatible | No | Partial | No | No evidence | It records decisions and warns before repeated mistakes but does not acquire or revise project theory |
| Rainbow | No | Not an LLM system | No | No | Fixed, supplied model | Yes, within supplied strategies | It adapts a running configuration through a causal architecture model but does not learn its model or action repertoire |

## Nearest constructions under the endpoint lens

### Fluent is closest to the software-house topology

[Fluent's public repository](https://github.com/mrinalwadhwa/fluent) describes
an implemented factory that turns vision, bug reports, user feedback,
production logs, and agent traces into work items. Writers change the product;
deterministic tests and independent reviewers reject candidates; a Learner can
land project Expertise with the change; post-merge review can create and run a
corrective work item; and an opt-in `execute` mode can authorize a bounded
chain of follow-ups. The local [Fluent
ingest](../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
captures the same architecture from the builder's practitioner account.

Under the endpoint lens, Fluent is closer than benchmark self-improvement
systems because it has external stakeholders, product code, deployment
evidence, natural-language expertise, a scheduler, rejection, retention, and
later reuse. Among the reviewed constructions, its standard work packet is
unusual in explicitly including both technical decisions and their reasoning.

The gap is actor allocation. People and Fluent jointly shape and confirm the
Brief, Behavior Specifications, Technical Approach, and Implementation Plan.
Ambiguous corrective observations wait for a person. The human queue is
defined for context, judgment, expertise, and authority—the same functions the
endpoint lens requires a complete witness to bring inside. The public materials do
not test whether the Learner can infer a project rationale not already present,
distinguish it from a plausible but false lesson, or replace it when later
consequences invalidate it. Fluent is therefore a near constructional scaffold,
not evidence of initial acquisition, successor acquisition, or no-human
continuation.

### Wheelhouse connects deployment experience to doctrine and enforcement

Steve Yegge's [Wheelhouse
account](../../sources/steve-yegge-fences-not-sandboxes.ingest.md) reports a
50–60-agent software factory in which clarifications, incident postmortems,
verdicts, and recurring practices accumulate as constitution-like rules. Some
rules progress from custom to warning, written doctrine, and finally programs
that refuse or flag an action. A dedicated agent, Frog, was assigned to
consolidate obsolete and cancelled rulings.

That lifecycle is unusually close to Commonplace's cross-form development path:
production experience changes natural-language state and can later become
executable enforcement. It also exposes a maintenance problem any such path
must solve: the corpus reached hundreds of artifacts and retained obsolete or
misclassified rulings.

The report nevertheless places the decisive learning outside the automated
boundary. Yegge's judgments become the rulings and verdicts. The available
evidence does not show Frog inferring the original project theory, revising it
adequately, or causing later code choices through a tested consumption path.
The source is a first-person report without inspectable implementation or
independent outcome evidence.

### Ona and OpenAI show long production spans over code and notes

Ona's [ten-day Memo factory
report](https://ona.com/stories/software-factory-what-we-learned) describes an
empty repository becoming a deployed product through background agents. A
`quality.md` self-assessment caused the factory to create further issues;
scheduled agents inspected the automation system; production feedback was
summarized back toward planning; and repository files carried architecture,
design, conventions, product intent, and quality state. This is direct evidence
that software, notes, schedulers, and production signals can form one operative
loop. It is a bounded construction trial, not a learned successor lineage:
people spent the early days writing automations, prompts, instructions,
conventions, escalation paths, and review loops, then continued to supply
metrics, documentation, review, and product direction.

OpenAI's [agent-first product
report](../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
is the strongest scale case found for the substrate. Agents generated the
product code, repository-local product and architecture documents made the
business domain legible, structural tests and custom linters enforced
invariants, and recurring gardening agents repaired stale documentation and
drift. Yet the report explicitly assigns human engineers the work of putting
knowledge into the repository and responding to failures by choosing missing
capabilities, constraints, tools, or checks. The system applies a supplied and
continually human-shaped theory; it does not demonstrate computational initial
or successor acquisition. The model lineage is also not pinned across the
five-month development history.

Factory.ai's [product
page](https://factory.ai/product/software-factory) and [private-preview
documentation](https://docs.factory.ai/software-factory/overview) describe a
commercial 24/7 control plane spanning intake, code generation, validation,
release, documentation, and monitoring. This is product-documented capability,
not independent operational evidence. Its published boundary remains
“automated validation, humans on judgment,” and the documentation does not
expose a computational theory-acquisition mechanism or a fixed-model learning
lineage.

### Exo, Prime Agent, and Autogenesis supply mutable persistent substrates

The direct comparison above gives [Exo](../../agentic-systems/exo.md) its full
treatment. Under the endpoint lens, its contribution is a protected substrate
around a broadly rewritable executor, with agent-executed inspection and edits,
build and test rejection, restart, rollback, and preservation of failed-attempt
evidence. It remains a personal-agent harness rather than a software house, and
these mechanisms show revision capability rather than an automatic learning
trigger or theory-acquisition process.

[Prime
Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) adds a
persistent recursive runtime, versioned prompts, memories, skills, and subagent
specifications, rollback, bounded autonomous continuation, goals, cron, and
heartbeat jobs. A fixed model can therefore carry behavior across trajectories
by revising external state. Its most informative case is adverse: a Factorio
agent found a specification exploit and retained it as a reusable skill. The
case demonstrates that persistence and autonomy do not supply semantic
admission. Prime Agent is strong on retained behavior and bounded continuation,
but its reported evaluations do not show an ongoing user software product or
program-theory acquisition.

[Autogenesis](../../agentic-systems/autogenesis.md) is the broadest explicit
resource protocol: prompts, agents, tools, environments, memory, skills,
connectors, and workflows can be generated, versioned, evaluated, committed,
and rolled back. It covers more endpoint-relevant writable forms than Exo,
but its semantic selection is weaker than its versioning machinery, its tests
cover structure and smoke behavior, and the inspected paper-aligned and current
implementations are incomplete in different ways.

### Memento-Skills, Recuris, and HCL supply bounded fixed-model learning

[Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md)
is the cleanest reviewed construction in which a surrounding system improves
through one inspectable mixed-form unit while model weights remain frozen. Each
skill combines a declarative `SKILL.md`,
prompts, and executable code. Execution outcomes drive failure attribution,
skill rewriting or creation, generated unit-test gating, rollback, and
behavior-trained routing into later tasks. Unlike
[Voyager](../../agent-memory-systems/reviews/voyager.md), it revises skills
instead of only adding or replacing successful programs. Its held-out gains
support the narrow claim that a fixed-model system can improve through code
plus text when future tasks revisit the learned behavioral structure. Answerable
benchmarks supply the oracle; product rationale, delayed maintenance, and
open-ended demands are absent.

[Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md)
is narrower in writable form but stronger in state and admission. A frozen
agent carries experiential memory, a verified pending/done/blocked work-state
ledger, invocation policy, and checkers. A meta-agent uses structured traces to
patch one component, and a deterministic paired gate decides whether the patch
survives. The pinned code supports these mechanisms. The fixed four-coordinate
surface, benchmark partitions, and gate are supplied; the work does not ask
whether the agent acquires a rationale for why a user product is organized as
it is.

[Harness Continual
Learning](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
extends the pattern across sequential tasks by jointly versioning a task
interface, experience memory, capability map, and adaptive router. Candidate
changes are committed only after current-task improvement, finite historical
anchors, and validity checks. It is important negative evidence for any easy
continuation claim: even a zero-loss gate on the retained anchors still permits
held-out forgetting. The system remains benchmark-bound and does not test
program theory.

The larger fixed-model harness-optimization
cluster—[Self-Harness](../../sources/self-harness-harnesses-that-improve-themselves.ingest.md),
[AutoSaddler](../../sources/autosaddler-automatic-harness-optimization-with-durable-updates.ingest.md),
[Meta-Harness](../../agent-memory-systems/reviews/meta-harness.md),
[HarnessCompass](../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md),
[JIT-Agent](../../sources/jit-agent-scaling-harness-intelligence.ingest.md),
[Workspace Optimization](../../sources/workspace-optimization-how-to-train-your-agent.ingest.md),
[Symbolic Learning](../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md),
and [Agentic Harness
Engineering](../../agent-memory-systems/reviews/agentic-harness-engineering.md)—strengthens
the codified-revision part of the developmental and endpoint lenses. Across
the cluster, fixed models use traces and scores to revise prompts, tools,
middleware, routing, topology, or harness code. The same fixed outer
decomposition and machine-score boundary recurs. None adds users, open-ended
product demands, or a program-theory test, so listing every optimizer would not
change the nearest-neighbor result.

### Knowledge and rationale systems retain the other form

[Knowledge-Centric
Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md)
is the strongest controlled notes-only case found. Disposable, stateless agents
write task evidence into forums; cross-task forums test transfer; distillation
produces scoped natural-language guidance; and later agents receive the
resulting bundle. Held-out and cross-model experiments are designed to isolate
the external knowledge base as the changing object. The protocol deliberately
holds software and solver state fixed and uses benchmark answers. It is near to
Commonplace only on making external knowledge the learned object, not on
connected-theory construction, software revision, or software-house
continuation.

[PROJECTMEM](https://arxiv.org/abs/2606.12329) is a smaller but more directly
software-specific construction. It stores issues, attempts, fixes, decisions,
and notes in an append-only text event log, projects them into agent-readable
summaries, and uses a deterministic pre-action gate to warn before repeated
failed fixes or edits to fragile files. This makes retained project memory
causally active, but its two-month self-study does not establish automatic
acquisition, semantic revision, or product development without people.

Proprietary or lightly evidenced coding-memory products are worth watching, not
promoting into the nearest set. Several store or deliver ADRs, decisions,
conventions, and lessons. Those claims establish, at most, representation and
retrieval; they do not establish learning or adequate theory.

Warp's [scheduled skill
improver](../../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
and the production [accumulated-rules
study](../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md)
show the same boundary particularly clearly. Both convert operational feedback
into versioned instructions used by later coding sessions. In Warp, people
write the feedback and approve the skill PR. In the accumulated-rules study,
an engineer decides whether one accepted review comment generalizes into a
future rule. These are genuine production deployment-time learning systems at
the human-inclusive boundary, but the human performs the same generalization
and admission work that remains inside Commonplace's operator role.

### Older constructions locate the boundary without LLMs

[Rainbow](../../sources/rainbow-architecture-based-self-adaptation.ingest.md)
is the closest pre-LLM construction on the program-model side. An external
architectural graph is updated from live probes, checked against constraints,
and used to select strategies that change a running system. The model is
causally operative, but its vocabulary, goals, constraints, operators,
translations, and strategies are all designer-supplied and remain fixed. It
adapts configuration without learning the theory that governs adaptation.

The [Tool
Factory](../../sources/cook-kent-tool-factory-2003.ingest.md) and
[MDSoFa](../../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md)
show recursive software-production machinery: a factory can generate tools or
another factory from metamodels, mappings, patterns, templates, and expertise.
They also make the missing acquisition step explicit. People supply the
family-specific production knowledge. Regenerating or bootstrapping the
producer propagates that knowledge; it does not discover or revise it from
product consequences.

## Composite construction hypothesis

The comparison suggests a possible assembly, not an existing architecture:

- Commonplace supplies the theory-building purpose, inspectable semantic state,
  artifact authorities, and explicit admission problem.
- Ars Contexta and GBrain supply different versions of trace capture,
  recurrence-oriented processing, promotion state, and scheduled maintenance.
- Exo supplies a protected substrate, broad agent-executed revision, restart,
  and recovery without erasing failed-attempt evidence.
- Fluent supplies the external-user product topology, rationale-bearing work
  packets, production observations, and corrective follow-ups.
- Recuris and Harness Continual Learning supply paired and historical admission
  patterns; Memento-Skills supplies a mixed natural-language and executable
  mutation unit.

These parts were built around different objectives, authority models, state
representations, and evaluators. Their juxtaposition identifies engineering
questions. It is not evidence that the parts compose, that the composite would
preserve their reported properties, or that semantic theory acquisition follows
from joining them.

## Evidence that would change the map

### Evidence of movement along Commonplace's developmental path

The strongest evidence would be a traced sequence in which:

1. operator interventions are retained with enough episode context to recover
   what distinction or missing premise they supplied;
2. a computational process identifies a recurrence across separate episodes
   without being told the shared abstraction;
3. the recurrence becomes a scoped candidate rather than an immediately
   authoritative rule;
4. evidence, review, or a defeating check admits or rejects the candidate;
5. an admitted note, instruction, route, critic, validator, or code change is
   demonstrably activated and changes later work; and
6. matched later episodes require less task-specific operator input without
   weakening outcome warrant.

Capturing transcripts alone, generating a plausible lesson, or reducing total
operator messages would not establish this progression.

### Evidence of a nearer external construction

A new neighbor becomes materially nearer by joining currently separated
functions: an explicit theory-building service, trace-to-candidate learning,
semantic admission, broad but recoverable self-revision, and operation on a
continuing product or knowledge service. Another benchmark gain or a larger
editable harness changes the map only on the function it actually tests.

### Evidence of a reachability witness

The endpoint needs the more demanding conjunction from the original search:

1. A pinned fixed-model system maintains one user product over a declared
   horizon of incrementally revealed requirements and production events.
2. The seed withholds at least one decisive project rationale while retaining
   the records from which it can be acquired.
3. The system writes both the product or production machinery and a
   rationale-bearing natural-language artifact, then demonstrably loads the
   latter at the later decision where it matters.
4. A later change is locally valid under tests but conflicts with the acquired
   rationale. The system preserves coherence without receiving the answer from
   a person.
5. A later dependency or operating consequence makes the old rationale false.
   The system attributes the evidence, admits a successor rationale and code
   change, and avoids both blind preservation and ungrounded rewrite.
6. Candidate admission, rollback, retirement, and conflict resolution operate
   without a person supplying the decisive theory or choosing the successor.
7. Evaluation includes untouched later changes and counterfactual removal or
   perturbation of the retained rationale, so success demonstrates causal use
   rather than storage, retrieval, or benchmark selection alone.

Fluent is a plausible current host for such a test because its public materials
describe users, product code, production observations, rationale-bearing work
packets, expertise, scheduling, rejection, and correction. Recuris or Harness
Continual Learning supplies the nearest admission pattern; Memento-Skills
supplies the nearest mixed-form mutation unit; Exo supplies the nearest
restart-and-rollback continuation substrate. That is a synthesis of parts, not
an existing construction or evidence that the mechanisms are compatible.

## Evidence boundary and search record

This is a working qualitative synthesis, not a corpus-wide assay. “Nearest”
judgments depend on the three declared lenses and the evidence available at the
cutoff. Absence means not located in this bounded search, not that no such
construction exists.

The local search used repository commit
`6c73908fb7a0aab2b47284abbccd3ed763daae3b` and covered:

- the reachability article and its linked sources and notes;
- titles and descriptions under `kb/agentic-systems/`,
  `kb/agent-memory-systems/`, and `kb/sources/`;
- lexical families around `self-improv*`, `self-evol*`, `fixed`, `frozen`,
  `harness`, `software factory`, `coding agent`, `skill`, `memory`, `rationale`,
  `architecture decision`, `production feedback`, and `continual learning`;
- the self-improving-systems curated head, the trace-learning survey, and the
  epistemic-architectures workshop;
- full local analyses for the candidates discussed above, including the
  Commonplace comparisons in Ars Contexta, AI Research OS, GBrain, Eigenius,
  ScienceFlow, and ARC;
- the framing history at commits `195822b0`, `0a1a6b79`, `854af45f`,
  `f00d5359`, and `beb4d4a6`, used to distinguish Commonplace's original
  instrument from the later coupled theory-builder/software-house program.

The external search was run on 2026-09-03. Query families combined:

- fixed or frozen LLMs with self-improving coding agents, harnesses, memory,
  and software factories;
- autonomous software factories with production feedback, persistent project
  knowledge, and user demands;
- architecture decisions, rationale, and persistent coding-agent memory;
- recursive agent code, skill, prompt, tool, workflow, and memory revision.

The original external search emphasized the endpoint. The later Commonplace
reframing broadened the candidate set through code-grounded analyses already in
the local corpus; it did not claim a second exhaustive web search for every
theory-building product.

Primary papers, official repositories, official product documentation, and
first-person engineering reports were preferred. Surveys and search results
were used for discovery rather than as decisive evidence. Marketing-only
claims, non-inspectable product claims, and systems that only preserve session
history were excluded from the nearest set. The cutoff is the search date, not
a claim of exhaustive coverage. Several 2026 papers are recent preprints with
paper-only outcomes; several production cases are self-reports without
independent evaluation.

A refresh should preserve the three lenses, update the local baseline and
evidence cutoff, repeat the endpoint query families, and search explicitly for
new theory-building and epistemic systems. It should reassess implementation
and evidence tiers before changing a proximity judgment. Detailed mechanism
comparisons remain owned by the [trace-learning
survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md),
[self-revision design-space
workshop](../self-revision-design-space/README.md),
[epistemic-architectures workshop](../epistemic-architectures/README.md), and
[Exo experiment track](../explanatory-theories-deployment-time-learning/README.md);
this landscape records only their relation to Commonplace.
