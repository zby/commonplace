# Nearest existing constructions to Commonplace

Working landscape. The evidence cutoff is 2026-09-03 and the local baseline is
repository commit `6c73908fb7a0aab2b47284abbccd3ed763daae3b`.

## Working result

This report is a reusable comparison map for authors writing about Commonplace,
an agent-operated framework that helps a human build and govern theories about
agentic systems. It compares existing systems against three distinct objects:
Commonplace as it operates today; a proposed path by which repeated operator
interventions could be captured, generalized, and, when warranted, converted
into retained theory or machinery used by later runs; and a conjectured
endpoint in which a computational theory builder also maintains
software for external users—a software house. Use the article-support index
below to choose the system that bears on an article claim, then carry its
evidence basis and required caveat into the article.

It does not identify an evidence-backed single nearest system or demonstrate
that selected mechanisms compose into a working whole. The three lenses answer
different questions, and no single distance measure or weighting rule has been
defined to collapse their matches into one ranking.

- **Observed today — Commonplace's present construction:** Ars Contexta is the
  strongest reviewed match for an agent-operated environment for developing a
  methodology; AI Research OS is the strongest match in inspectable Markdown
  and a structure that separates sources from synthesis; Eigenius is the
  strongest match in typed claims and evidence with checked paths for accepting
  changes. The reviewed evidence does not show one of these systems combining
  Commonplace's theory-building purpose, rules for artifact types and
  collections, semantic
  review, and current division of judgment between people and agents.
- **Proposed development path:** Ars Contexta is the strongest reviewed match
  for turning corrections and session evidence into methodology observations
  and later system changes. GBrain is the strongest match found in inspected
  code across capture, consolidation, scheduled maintenance, retrieval, and
  skill revision gated by tests and scores. Both expose useful pieces of the
  missing path; the reviewed evidence for neither shows reliable acquisition of
  a recurring semantic judgment from operator interventions or a warranted
  decision to retain the resulting change.
- **Conjectured endpoint — the working thesis that theory building and software
  building converge:** Fluent is the strongest reviewed match for the
  operation of software for external users, while Exo is the strongest match
  found in inspected code for broad agent-executed self-revision and recovery.
  Recuris, Memento-Skills, and Harness Continual Learning contribute bounded
  mechanisms for attributing failures and accepting or rejecting changes. No
  witness to the
  [reachability
  conjecture](../../articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md)
  was located in the reviewed corpus.

The report therefore assembles a research heuristic from different systems:
Commonplace-like theory and governance, Ars Contexta- or GBrain-like processing
of records from past work, Exo-like self-revision and recovery, Fluent-like
product operation, and candidate-rejection gates like those described by
Recuris, Memento-Skills, and Harness Continual Learning. This list does not show
that the parts compose, that their objectives agree, or that the resulting
system could acquire and revise an adequate theory. An author can use these
systems as bounded examples of separate mechanisms and as sources of candidate
tests, not as a witness to Commonplace's full development path or conjectured
endpoint.

## Article-support comparison index

Use this table to select a comparison for an article, then carry its evidence
basis and decisive caveat into the article with it. Each row states the
strongest comparison supported by a local review or tracked ingest. The rows
answer different questions against the three Commonplace lenses and the six
endpoint questions below; they are not a scalar ranking of systems.

Evidence terms are literal. **Code-inspected** means that a local review found
the mechanism in a pinned implementation; it does not establish that the
mechanism ran successfully or produced a reported outcome unless the row says
so. **Paper-reported**, **practitioner-reported**, **product-reported**, and
**product-documented** identify claims made by those sources, not independently
reproduced results.
**Synthesis inference** identifies this report's comparison across those
records. “Not demonstrated” means that the reviewed evidence does not show the
property; “not inspected” means that implementation evidence was unavailable;
and “not in scope” means that the source did not set out to test the property.
Only code-inspected rows support implementation-level placements. Rows based
only on papers, practitioner reports, or product materials remain source-graded
design-space comparisons: an article must attribute them and must not present
them as inspected implementations or independently evaluated outcomes.

| Claim or question an article needs to address | Reviewed comparison | What it retains and what admits a change | Criterion result that may be reused | Required caveat; do not infer |
|---|---|---|---|---|
| Can corrections and session evidence become methodology changes? | [Ars Contexta](../../agent-memory-systems/reviews/arscontexta.md) — code-inspected mechanism | A local Markdown vault retains sessions, observations, tensions, methodology notes, context, skills, and hooks. `/remember` and `/rethink`, executed through LLM skill instructions, classify evidence and may promote it into notes or system changes. | Synthesis inference: strongest match to the observed present construction for an agent-operated methodology environment and a partial match to the proposed development path for capture, candidate formation, promotion, and read-back. | Static code inspection establishes the artifact paths and instructed loop, not that the path ran reliably, captured transcripts deterministically, recognized recurrences faithfully, admitted changes independently, or improved later behavior. |
| Can a system automate more of capture, consolidation, maintenance, and skill revision? | [GBrain](../../agentic-systems/gbrain.md) — code-inspected mechanism | Database and Markdown state retain signals, facts, takes, patterns, concepts, jobs, traces, and skills. Host instructions request per-message signal detection; if adopted, that path and scheduled LLM cycles can generate changes. SkillOpt is configured to admit a locally authored skill edit only when its median score over three runs per task beats the incumbent by a threshold, while bundled-skill edits remain human-reviewed proposals. | Code inspection shows machinery for automatic capture, scheduled consolidation, crash-resumable work, and gated revision of a behavior-shaping artifact—more of the proposed development path's listed machinery than Commonplace currently implements. | The inspected machinery does not establish that the host always follows the capture instruction, that the loops ran successfully, or that its judge models or task scores recover an operator's recurring semantic distinction, acquire an adequate theory, or warrant admission beyond their supplied oracle domain. |
| Can a software factory retain both product changes and project-specific guidance? | [Fluent](../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) — practitioner-reported mechanism | The practitioner reports that accepted product changes, project Expertise, observations, and corrective follow-ups persist; the account assigns rejection to a deterministic Tester and independent Reviewers, while people shape and authorize consequential specifications. | The account supports a human-inclusive **House**, **Software learning**, and **Note learning** topology and reports a path by which retained guidance can affect later shaping and execution. | This is practitioner-reported architecture, not a code-inspected mechanism or independently evaluated outcome. It does not test faithful program-theory acquisition, successor theory after contrary evidence, or **Continuation** without an internal human role. |
| Can operational rulings move from natural language into executable enforcement? | [Wheelhouse](../../sources/steve-yegge-fences-not-sandboxes.ingest.md) — practitioner-reported mechanism | The account reports retained clarifications, human verdicts, incidents, doctrine, warnings, and programs; human rulings authorize the generalization, while a dedicated officer is reported to consolidate obsolete rules. | The account supports a human-inclusive proposed development path from production evidence to natural-language system definition and then codified enforcement. | The source is a first-person report with no inspected implementation or independent outcome evidence. It does not establish computational generalization, program-theory holding by the curator, or human-free admission. |
| Can an agent revise and recover its own broad operating surface? | [Exo](../../agentic-systems/exo.md) — code-inspected mechanism | An ordered event stream and versioned artifacts preserve attempts while the agent may edit the executor, prompts, tools, adapters, and memory machinery. The inspected implementation provides build and test rejection plus restart observation, git, snapshots, and rewind for mechanical recovery. | Code inspection supports broad self-inspection, symbolic revision, activation, rollback, preserved failure evidence, and scheduling and restart paths. | Static inspection establishes revision and recovery paths, not their reliability in a live instance, endpoint continuation, or an automatic experience-to-improvement trigger. The review did not locate an external-user product, a program-theory acquisition test, or a gate that rejects a semantically bad change that still builds and runs. |
| Does persistent fixed-model refinement solve semantic admission? | [Prime Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) — code-inspected mechanism; paper-reported cases | Versioned prompt, memory, skill, subagent, kernel, goal, and schedule state persists across trajectories; agents or a refinement call request edits that are recorded and can be rolled back. | Code inspection supports persistent external-state revision and bounded continuation; the reported fixed-model cases show why these mechanisms are relevant to **Fixed model** learning. | The reported Factorio case retained a specification exploit as a reusable skill. Persistence, versioning, and rollback therefore do not establish semantic admission, a software house, or program-theory acquisition; benchmark outcomes remain paper-only here. |
| Can a fixed model admit trace-derived changes through a reject-capable gate? | [Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md) — code-inspected mechanism; paper-reported outcomes | Experiential memory, verified work state, invocation policy, and checkers form the retained update surface. The paper specifies a fixed Meta-Agent; inspected code implements component-scoped patch proposals and a deterministic paired held-out promotion gate. | Code inspection supports trace-to-candidate formation and reject-capable admission within a supplied four-coordinate memory design; the paper supplies the fixed-model condition and outcome claims. | The gate, benchmark partitions, runtime, and theory of the four coordinates remain fixed. Reported gains are not independently reproduced, and the study does not test software-house operation or acquisition and revision of program rationale. |
| Can one learned unit change both natural-language and executable behavior? | [Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md) — paper-reported mechanism and outcomes | The paper describes a skill folder containing `SKILL.md`, prompts, and executable code. It reports that outcome judgment and failure attribution select a skill to rewrite or create and that a generated unit test scored by a judge gates the mutation, with rollback on failure. | The paper reports fixed-foundation-LLM learning through a mixed-form artifact, including **Software learning**, **Note learning**, later routing, and bounded autonomous admission. | The implementation was not independently inspected in this ingest. The router itself is trained, and answerable benchmarks supply the objective and oracle. Generated tests have a narrow validation radius; the study does not test a continuing user product, program theory, or open-ended successor acquisition. |
| Does a zero-loss historical gate establish no forgetting? | [Harness Continual Learning](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) — paper-reported mechanism and outcomes | The paper describes a jointly versioned task interface, experience memory, capability map, and adaptive router. It reports an optimizer that proposes isolated edits and an evaluator that commits only candidates that improve current validation, respect sampled historical anchors, and pass validity checks. | The paper reports a proposal-evaluation-commitment loop for sequential fixed-model external-state learning and makes regression control an explicit admission criterion. | No implementation was inspected and no outcome was independently reproduced. The paper reports held-out forgetting even at zero loss on retained anchors; finite benchmark oracles do not establish global retention, program theory, or software-house continuation. |

Together these comparisons provide code-inspected or source-reported examples of
separate component mechanisms: trace-derived methodology candidates, scheduled
consolidation, cross-form retention, reject-capable gates, broad self-revision,
rollback that preserves failed-attempt evidence, and continuing product
operation with human authority. No reviewed source tests the full conjunction.
In particular, no reviewed source tests both initial acquisition of a withheld
program rationale and later replacement of that rationale from delayed product
consequences, with causal read-back into software decisions and no human
supplying the generalization or admission verdict. The table therefore
supports claims about available components and missing tests, not a claim that
the components compose or that the conjectured endpoint is reachable.

### Reachability-obligation crosswalk

The [reachability
article](../../articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md)
states four constructive-witness obligations. This crosswalk shows how they
relate to this report's six endpoint questions and the seven numbered test
conditions under [Evidence of a reachability
witness](#evidence-of-a-reachability-witness). The obligations describe a
progression; the endpoint questions decompose properties that may contribute to
more than one obligation.

| Article obligation | Primary endpoint questions | Witness-test conditions | What the correspondence does not establish |
|---|---|---|---|
| **Holding and application** | **Program theory** asks directly whether the system retains and applies the given theory. | The later-load half of condition 3, then conditions 4 and 7: begin with adequate rationale already present; load it at the relevant decision; preserve coherence when a locally valid change conflicts with it; test causal use on untouched changes and by perturbing the rationale. | Storing, retrieving, or paraphrasing a rationale does not establish that it governed the later decision. |
| **Initial acquisition** | **Program theory**, **Software learning**, and **Note learning** together ask whether the system acquired an explanation and changed both legible forms. | Condition 2, the writing and first-read-back portions of condition 3, and condition 7: withhold a decisive rationale; require cross-form writing and read-back; test that the acquired rationale caused later behavior. | A software or note update does not by itself establish acquisition of an adequate theory. |
| **Successor acquisition** | **Program theory**, **Software learning**, and **Note learning** together ask whether contrary evidence produced an adequate replacement and corresponding changes. | Conditions 5, 6, and 7: make the old rationale false; require attributed and admitted successor changes without a person choosing them; test their causal use. | A reject-capable gate or a changed rationale does not by itself establish that the admitted successor is adequate. |
| **Automated continuation** | **House**, **Fixed model**, and **Continuation** set the operating boundary; holding, acquisition, and both learning questions must keep working across it. | Condition 1 plus repeated coverage of conditions 3–7: pin the model and product horizon, then repeat cross-form use, conflict handling, successor acquisition, human-free admission and recovery, and causal-use tests across later changes. | Scheduling, restart, or a bounded human-free benchmark loop does not by itself establish continued software-house operation. |

**House** and **Fixed model** are cross-cutting controls on the whole witness,
not additional acquisition stages. **Software learning** and **Note learning**
show which retained forms changed, but neither alone establishes **Program
theory**. A partial endpoint-table cell therefore must not be read as partial
completion of an article obligation.

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

The operator characterizes the intended direction as having been for the system
to perform more of this work from less and less task-specific human input. This
report treats that characterization as the program's stated direction, not as
an independently reconstructed historical finding. It does not mean eliminating
all human input or optimizing for fewer operator hours. It means increasing useful and
better-warranted work per consequential human judgment, while moving the
remaining judgments toward harder questions and longer horizons. [Increasing
computational autonomy relocates human effort to the
frontier](../../notes/increasing-computational-autonomy-relocates-human-effort.md)
states that objective more precisely.

This operator-stated starting point differs from most constructions in the
reviewed set. The reviewed harness optimizers begin with a task loop and add
retained state to improve a supplied score. The reviewed software factories
begin with application production and add documents, feedback, and governance.
Commonplace's stated starting point is semantic work: forming
explanations, assessing their fit and warrant, revising them under contrary
evidence, and integrating them into a larger theory.

### Observed today: current human-inclusive construction

Under [the declared Commonplace
frame](../../reference/commonplace-declared-frame.md), the repository, its
operative artifacts and software, the agents that consume them, and designated
maintainers form one system. Model weights and their provider remain outside.
Agents already perform search, comparison, synthesis, criticism, drafting, and
implementation. The repository retains accepted changes in natural-language
theory, instructions, schemas, validators, review state, and code. The traced
tag-README pathway establishes later behavioral effect for one bounded subset
of those surfaces, not for every retained artifact.

The operator still supplies decisive judgments about research direction,
global theoretical fit, semantic admission, and system design where no
adequate check exists. Commonplace is therefore classified, relative to its
declared boundary, as a bounded human-inclusive [reflective self-improving
system](../../notes/evidence/commonplace-as-a-reflective-system.md), not as an
autonomous theory learner. A [2026-08-30 revision
trace](../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
records retained theory being retrieved during model-mediated search while the
operator supplied sparse but decisive global-fit corrections. The trace supports
an inference that the retained artifacts constrained the revision, but has no
matched control. It is evidence for one mixed
human-computational pathway, not for computational theory acquisition.

### Proposed development path: less task-specific human input

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

### Working program thesis toward the conjectured endpoint: theory building and software building converge

The working thesis that motivates the current program is stronger than “a theory
builder needs some tooling.” It predicts that, under open-ended operation, a
theory builder will eventually encounter material its current software cannot represent, retrieve,
compare, test, schedule, or govern. Supporting a new source kind may require a
snapshot path; a new relation may require a schema and validator; a larger
corpus may require a different index; a new review problem may require another
evaluator or execution path.

Under the thesis, either a person changes the supporting software or the theory
builder does. If the same person repeatedly diagnoses and implements such
changes, that person remains an internal production and theory-holding
component. A computational theory builder that brings the function inside must
keep developing software in response to the demands of its external users. In
the [software-house definition](../../notes/definitions/software-house.md), it
has become a software house. This is a working thesis about open-ended
operation, not an empirically established inevitability.

The implication also runs from software building toward theory building, under
the narrower condition that the software must remain coherent across novel
demands whose fit cannot be decided by existing checks. The thesis therefore
requires such a software house to preserve, apply, criticize, and sometimes
revise an explanation of why the
product is organized as it is. The proposed research object is therefore one
coupled system approached from two directions: theory work creates demands for
new machinery, while coherent software change creates demands for theory.

### Three comparison lenses

| Lens | Object being compared | Questions that determine proximity |
|---|---|---|
| **Observed today — present construction** | The human-inclusive theory builder operating now | Does the system serve theory or knowledge work; retain inspectable claims, evidence, rationale, and system definitions; route them into later work; distinguish their authority; and govern semantic admission? |
| **Proposed development path** | The process by which more functions could move from repeated operator judgment into retained capacity | Does the system capture interventions or traces, recognize recurrences, attribute evidence, form scoped candidates, revise natural-language and symbolic artifacts, test and admit them, recover from failure, reactivate them later, and measure the resulting change in human contribution? |
| **Conjectured endpoint** | A computational theory builder that is also a software house | Does one fixed-model lineage maintain software for external users, acquire and revise program theory, change both software and natural-language state, and continue over a declared scope and horizon without a human in an internal production or theory-holding role? |

“Partial” means that a mechanism exists but its causal role, scope, evidence, or
actor allocation falls short of the named lens. It is not half credit toward a
single score.

## Landscape map

| Construction | Matched lens or function | What it contributes | Decisive divergence from Commonplace | Evidence basis |
|---|---|---|---|---|
| [Ars Contexta](../../agent-memory-systems/reviews/arscontexta.md) | Present operating shape; recurrence-to-methodology path | Agent-operated file graph, generated instructions and hooks, session/correction mining, observation and tension state, later promotion or implementation | Most extraction and promotion judgment is encoded in LLM skill procedure; reliable cross-episode recognition and behavioral improvement are not established | Code-inspected mechanism; no live outcome evidence |
| [AI Research OS](../../agent-memory-systems/reviews/ai-research-os-workshop.md) | Present knowledge medium | Inspectable Markdown, immutable sources, source/synthesis separation, progressive pull, deterministic indexes | The review did not locate a reject-capable content-acceptance step or a governed promotion path from learned knowledge into system-definition artifacts | Code-inspected mechanism; no live outcome evidence |
| [Agent Skills for Context Engineering](../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) | Methodology corpus and research-to-skill promotion | File-first skills, source and claim provenance, run gates, mechanism records, validation, router benchmarks, and example trace-to-skill tooling | Published skills remain authored or human-reviewed; the trace optimizer is example scope rather than a standing cross-task learning loop | Code-inspected mechanism; reported benchmarks retain their source grade |
| [GBrain](../../agentic-systems/gbrain.md) | Operational development machinery | Trace and signal capture, fact/take/concept promotion, scheduled consolidation, durable jobs, retrieval, and gated skill revision | A larger database/runtime surface carries much of the authority; semantic admission uses machine oracles and uneven provenance rather than Commonplace's slower explicit theory governance | Code-inspected whole-system and memory mechanisms; no live outcome evidence |
| [Eigenius](../../agentic-systems/eigenius.md) | Typed epistemic governance | Typed graph objects, epistemic grades, certificates, route-specific validation, optional proof checking | The host supplies the reasoning protocol and calls; the system does not own a continuing theory-building loop, and formal validity does not establish content truth or explanatory quality | Code-inspected mechanism; no live outcome evidence |
| [ScienceFlow](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) | Long-horizon research continuation | Recoverable workspaces, retained evidence, bounded memory, evaluated stages, re-anchoring, and resource control | Its evaluators and stage decomposition are fixed; explanation is not a retained governing object and the reported outcomes are not independently reproduced | Code-inspected mechanisms; paper-reported outcomes |
| [Fluent](../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) | Software-house topology | Practitioner-reported users, product code, rationale-bearing work packets, expertise, rejection, deployment evidence, and corrective follow-ups | People retain consequential context, judgment, expertise, and authority; program-theory acquisition is not tested | Product-documented architecture and practitioner-reported operation; implementation not code-inspected |
| [Wheelhouse](../../sources/steve-yegge-fences-not-sandboxes.ingest.md) | Human-inclusive cross-form learning | Practitioner-reported incidents and rulings can become doctrine, warnings, and executable fences | The operator supplies the generalization and verdict; implementation and outcomes are not independently inspectable | Practitioner-reported mechanism and outcomes; implementation not code-inspected |
| [Exo](../../agentic-systems/exo.md) | Mutable and recoverable runtime | Broad agent-executed self-editing, source inspection, build/test/restart, rollback, event history, and scheduling | The code-grounded review did not locate a theory-building service, automatic trace-to-improvement trigger, or semantic gate for delayed product fit | Code-inspected mechanism; no live instance run |
| [Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md), [Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md), and [Harness Continual Learning](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) | Bounded attribution and admission | Trace-based patching, mixed-form skills, regression anchors, rollback, and fixed-model continuation | Benchmarks and supplied decompositions provide the objective and oracle; the reviewed records do not test maintenance of a changing user product or acquisition of its theory | Paper-reported mechanisms and outcomes; Recuris mechanisms also code-inspected |
| [Knowledge-Centric Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Knowledge as the learned object | Paper-reported cross-task forums and distilled natural-language guidance isolate improvement in an external knowledge base | The protocol deliberately fixes software and uses benchmark answers; it does not build a connected, governed theory or revise its supporting system | Paper-reported mechanism and outcomes; implementation not code-inspected |
| [Rainbow](../../sources/rainbow-architecture-based-self-adaptation.ingest.md) | Historical model-mediated adaptation | A paper-described live architectural model, probes, constraints, and strategies govern adaptation | Designers supply the model, goals, operators, and strategies; the system does not learn or revise that governing theory | Paper-reported mechanism, implementation, and outcomes; not independently reproduced |

The table names qualitative matches, not a winner. In particular, AI Research
OS matches the medium more strongly than the governance; GBrain matches
operational learning machinery more strongly than inspectability; Fluent
matches production topology more strongly than actor allocation; and Exo
matches mutation reach more strongly than semantic selection.

## Nearest constructions under the observed-today and proposed-path lenses

### Ars Contexta is the strongest reviewed match to the agent-operated methodology shape

Ars Contexta treats the knowledge base as an agent-operated methodology
environment rather than a passive memory store. Like Commonplace, it uses
plain files, explicit spaces and conventions, search-friendly descriptions,
validation, and procedures that agents execute. Its `/remember` path can mine
current corrections or stored sessions for repeated redirections, workflow
breakdowns, agent confusion, and undocumented decisions. `/rethink` can then
classify accumulated observations and tensions for promotion, implementation,
methodology change, archiving, or continued observation.

That makes Ars Contexta the strongest reviewed match to the exact missing
transition named by the operator. The qualification is decisive: much of the
capture, recurrence judgment, classification, and promotion policy is a
natural-language skill executed by an LLM, not an independently verified
automatic loop. Static inspection establishes implemented artifacts and an
instructed path, not that the path ran reliably. It
does not establish faithful recognition of the same distinction across
episodes, warranted admission, or improved later behavior.

### AI Research OS is the strongest reviewed match in knowledge medium

AI Research OS uses immutable source material, per-source pages, concept and
entity pages, cross-source comparisons, synthesis, explicit open questions,
and deterministic indexes in a local Markdown research directory. Its staged
read path and source/synthesis separation closely resemble Commonplace's
inspectable medium and progressive pull.

The systems differ at admission and durability. The code-grounded review found
that later ingests can rewrite the AI Research OS wiki and that generated pages
are retained without a reject-capable content gate. Structural lint can find broken links, missing
hubs, and possible stale claims, but does not establish faithfulness or
explanatory quality. Generated knowledge also remains knowledge; it does not
become a validator, schema, or operating instruction through a governed
promotion path.

### GBrain is the strongest code-inspected match in operational learning machinery

GBrain combines a Markdown-facing brain with a Postgres-shaped active store,
hybrid retrieval, typed operations, background jobs, scheduled maintenance,
trace and signal extraction, consolidation into stronger knowledge objects,
and SkillOpt revision. Its host protocol asks for per-message signal detection;
its owned dream cycle creates and maintains facts, takes, patterns, concepts,
and skill candidates; its durable queue supports crash-resumable subagents.
The inspected implementation covers more of the listed capture and continuation
functions than Commonplace currently implements.

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

## Commonplace and Exo across the observed-today and proposed-path lenses

Exo provides a direct comparison for Commonplace's development path because the
two systems start from opposite scarce resources. Exo permits broad
agent-executed self-modification, but the code-grounded review did not locate an
independent semantic gate for deciding which mechanically valid changes are
improvements. Commonplace has explicit semantic and governance artifacts but
still depends on the operator for the highest-level theory and admission
judgments.

Technical basis: the code-grounded [Exo whole-system
analysis](../../agentic-systems/exo.md) and [Exo memory-system
review](../../agent-memory-systems/reviews/exo.md).

| Dimension | Commonplace today | Exo harness |
|---|---|---|
| Starting purpose | Help a human operator build and assess theories about agentic systems | Let a long-running personal agent inspect and rewrite as much of its own runtime as safely practical |
| Primary self-representation | Distributed typed notes, collection contracts, instructions, ADRs, schemas, validators, and code | A literal source tree, injected self-map, prompts, tools, adapters, skills, memory, and executor code |
| Mutable surface | Natural-language theory and system-definition artifacts can both change, but consequential changes remain human-gated | The agent can rewrite the executor, prompts, tools, adapters, and memory machinery; the Rust substrate is protected by default policy |
| Preserved evidence | Git history, source snapshots, review results, freshness state, and retained artifacts, with coverage differing by path | An append-only event stream and versioned artifacts survive sandbox rewind and failed executor changes |
| Context strategy | Selective pull through search, indexes, links, skills, and explicit routing | Full conversation replay plus coarse-pushed memory and skill descriptions, with skill bodies pulled on demand |
| Admission strength | Structural validation plus semantic review and operator judgment; broad automatic promotion is deliberately absent | Build, tests, module-shape checks, restart observation, and rollback; no independent semantic judge or mandatory canary |
| Current improvement trigger | Task-local human or agent noticing; operator interventions are not systematically captured or clustered | Deliberate model or human self-editing using inspectable state; no implemented automatic trace-learning or self-maintenance trigger |
| Theory-building role | Operator-stated purpose; one trace records retained theory being retrieved during search, while the operator decides global fit | The review did not locate a service or evaluation for acquiring and revising a theory of an external product |
| Autonomy direction | Move one function at a time when representation, method, correction, and warrant support the transfer | Maximize mutable agent control while keeping a small recovery and safety substrate fixed |
| Main missing bridge | Automatic evidence capture, recurrence detection, credit assignment, semantic admission, and sustained continuation | An objective-bearing semantic theory, delayed evidence attribution, and a gate able to judge more than buildability and immediate behavior |

The inspected Exo design therefore supplies several pieces Commonplace does not
yet have: a durable
execution-event substrate, an explicit protected-substrate/mutable-policy
boundary, model-accessible self-inspection, rebuild-and-restart, recovery that
preserves failed-attempt evidence, and scheduled continuation. Compared with the
inspected Exo surface, Commonplace has explicit surfaces for typed knowledge
claims, selected design rationale, and provenance; separation between knowledge
and system-definition authority; semantic review; and an explicit account of
which human judgments have not yet moved. The traced Commonplace evidence does
not establish complete rationale coverage or end-to-end continuity across those
surfaces.

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

## Conjectured endpoint lens: reachability witness obligations

The original search asked which systems come closest to the reachability
conjecture. The [reachability-obligation
crosswalk](#reachability-obligation-crosswalk) maps these diagnostic questions
to the article's four obligations and the seven test conditions below. The six
questions remain useful as an endpoint-specific view, but they do not rank
proximity to Commonplace today or to its development path:

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

The table retains the candidates selected by that narrower search and separates
criterion judgments from evidence grades. Criterion cells use a fixed
vocabulary: **Meets stated scope**, **Partial**, **Human-dependent**, **Not
demonstrated**, **Not in scope**, **Not applicable**, or **Not assessed**. “Meets
stated scope” means only that the reviewed record presents the criterion as
occurring inside its declared boundary; the **Evidence basis** column states
whether that record was inspected or only reported. A row still does not satisfy
the full endpoint unless all six questions hold together under adequate
evidence.

| Construction | House | Fixed model | Software learning | Note learning | Program theory | Continuation | Evidence basis | Decisive shortfall |
|---|---|---|---|---|---|---|---|---|
| Commonplace today | Not assessed | Not demonstrated; model realization not reliably pinned | Partial; bounded human-inclusive paths | Partial; bounded human-inclusive paths | Partial; operator supplies and selects global fit | Human-dependent | Local artifacts and two traced pathways; no matched end-to-end evaluation | Global fit, semantic admission, and unsupported system-design decisions remain human |
| Fluent | Meets stated scope | Not demonstrated; model lineage not pinned | Meets stated scope; human-inclusive | Meets stated scope; human-inclusive | Partial; rationale is supplied, while acquisition and faithful reuse are not demonstrated | Human-dependent | Product documentation and practitioner report; implementation and outcomes not independently inspected | Humans confirm behavior, technical approach, and unresolved decisions; theory acquisition is not tested |
| Wheelhouse | Not demonstrated | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Practitioner report; implementation and outcomes not independently inspected | Human rulings and verdicts produce doctrine; Frog's theory-holding role is only a hypothesis |
| Ona Memo factory | Partial; bounded trial | Not demonstrated | Partial; human-inclusive | Partial; human-inclusive | Not demonstrated | Human-dependent | Product report; implementation and outcomes not independently inspected | Humans built the harness, specified taste and intent, and retained product direction |
| OpenAI agent-first product | Meets stated scope | Not demonstrated; model lineage not pinned | Partial; human-inclusive | Partial; human-inclusive | Partial; supplied rationale, acquisition not tested | Human-dependent | Practitioner report; no pinned model lineage or independent comparative evaluation | Humans made the repository legible and turned failures into tools, rules, and checks |
| Warp skill improver | Not in scope | Not demonstrated | Not in scope | Partial; human-inclusive | Not in scope | Human-dependent | Practitioner report; linked demonstration not independently inspected | Human feedback supplies evidence and human PR review admits every skill update |
| Exo harness | Not in scope | Not demonstrated; no learning process reviewed | Not demonstrated; broad self-edit path is distinct from learning | Not demonstrated; deliberate authoring path is distinct from learning | Not in scope | Partial; scheduling and restart paths, no automatic improvement | Code-inspected mechanism; no live instance run | It rewrites a personal-agent executor, not a user product; build/tests do not judge program theory |
| Prime Agent | Not demonstrated | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; bounded goals | Code-inspected mechanism; paper-reported cases and outcomes | The paper reports direct adoption of persistent refinement and a retained specification exploit; it does not test product theory |
| Autogenesis | Not in scope | Partial; inspected update surface excludes weight change | Partial | Partial | Not in scope | Partial | Code-inspected mutation paths; outcomes paper-reported and not reproduced | Benchmarks and a weak semantic gate; the public implementations are transitional or incomplete |
| Recuris | Not in scope | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; fixed gate and benchmark loop | Code-inspected mechanism; fixed-model condition and outcomes paper-reported | Four predeclared memory coordinates and benchmark tasks; no project rationale or product demand stream |
| Memento-Skills | Not in scope | Meets stated scope for the foundation LLM; router is trained | Meets stated scope | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Mixed-form skills learn under answer oracles, not delayed software-maintenance consequences |
| Harness Continual Learning | Not in scope | Meets stated scope | Partial | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | Finite benchmark streams and a fixed four-part harness partition; held-out forgetting remains |
| Knowledge-Centric Self-Improvement | Not in scope | Meets stated scope | Not in scope | Meets stated scope | Not in scope | Meets stated scope; bounded task loop | Paper-reported mechanism and outcomes; implementation not independently inspected | It deliberately isolates knowledge-only learning on benchmark families |
| PROJECTMEM | Not in scope | Not demonstrated | Not in scope | Partial | Partial; decisions are logged, not applied as theory | Not demonstrated | Paper-reported mechanism; no local ingest or inspected implementation | It records decisions and warns before repeated mistakes but does not test acquisition or revision of project theory |
| Rainbow | Not in scope | Not applicable | Not in scope; fixed strategies adapt configuration | Not in scope | Not in scope; governing model is designer-supplied and fixed | Meets stated scope; supplied strategies | Paper-reported mechanism, implementation, and outcomes; not independently reproduced | It adapts a running configuration through a causal architectural model but does not learn that model or its action repertoire |

## Nearest constructions under the conjectured-endpoint lens

### Fluent is the strongest reviewed match to the software-house topology

[Fluent's public repository](https://github.com/mrinalwadhwa/fluent) documents
a factory intended to turn vision, bug reports, user feedback,
production logs, and agent traces into work items. Writers change the product;
deterministic tests and independent reviewers reject candidates; a Learner can
land project Expertise with the change; post-merge review can create and run a
corrective work item; and an opt-in `execute` mode can authorize a bounded
chain of follow-ups. The local [Fluent
ingest](../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
captures the same architecture from the builder's practitioner account.

Under the endpoint lens, Fluent is a stronger topology match than the reviewed
benchmark self-improvement systems because its documented design includes
external stakeholders, product code, deployment evidence, natural-language
expertise, a scheduler, rejection, retention, and later reuse. Among the
reviewed constructions, its standard work packet is
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
design, conventions, product intent, and quality state. The product report is
evidence that the described trial linked software, notes, schedulers, and
production signals in one operative loop; the implementation was not inspected
for this landscape. It is a bounded construction trial, not a learned successor lineage:
people spent the early days writing automations, prompts, instructions,
conventions, escalation paths, and review loops, then continued to supply
metrics, documentation, review, and product direction.

OpenAI's [agent-first product
report](../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
provides a five-month practitioner-reported scale case for the substrate. The
report says agents generated the
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
Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) has an
inspected persistent runtime with versioned prompts, memories, skills, and
subagent specifications, rollback, goals, cron, and heartbeat jobs. This gives
external state a path to carry behavior across trajectories without a weight
update. Its most informative reported case is adverse: a Factorio agent found a
specification exploit and retained it as a reusable skill. The case shows that
the reported refinement process did not by itself supply adequate semantic
admission. Prime Agent is a strong mechanism-level example of retained behavior
and bounded continuation, but its reported evaluations do not show an ongoing
user software product or program-theory acquisition.

[Autogenesis](../../agentic-systems/autogenesis.md) exposes an explicit resource
protocol in which prompts, agents, tools, environments, memory, skills,
connectors, and workflows can be generated, versioned, evaluated, committed,
and rolled back. It covers more endpoint-relevant writable forms than Exo,
but its semantic selection is weaker than its versioning machinery, its tests
cover structure and smoke behavior, and the inspected paper-aligned and current
implementations are incomplete in different ways.

### Memento-Skills, Recuris, and HCL supply bounded fixed-model learning

[Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md)
provides a paper-reported case in which a surrounding system improves through
one mixed-form unit while foundation-model weights remain frozen. The paper
describes each skill as a declarative `SKILL.md`, prompts, and executable code.
It reports that execution outcomes drive failure attribution, skill rewriting
or creation, generated unit-test gating, rollback, and behavior-trained routing
into later tasks. Unlike the inspected
[Voyager](../../agent-memory-systems/reviews/voyager.md) design, the paper's
procedure revises skills instead of only adding or replacing successful
programs. Its reported held-out comparison supports the bounded hypothesis that
a fixed-model system can improve through code plus text when future tasks
revisit the learned behavioral structure; the implementation and outcomes were
not independently inspected or reproduced here. Answerable benchmarks supply
the oracle, while product rationale, delayed maintenance, and open-ended demands
are not in the study's scope.

[Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md)
is narrower in writable form but stronger in state and admission. A frozen
agent carries experiential memory, a verified pending/done/blocked work-state
ledger, invocation policy, and checkers. A meta-agent uses structured traces to
patch one component, and a deterministic paired gate decides whether the patch
survives. The pinned code supports these mechanisms. The fixed four-coordinate
surface, benchmark partitions, and gate are supplied; the work does not ask
whether the agent acquires a rationale for why a user product is organized as
it is.

The [Harness Continual Learning
paper](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
extends the reported pattern across sequential tasks by jointly versioning a
task interface, experience memory, capability map, and adaptive router. It
describes candidate commitment after current-task improvement, finite
historical-anchor checks, and validity checks. Its reported result is important
negative evidence for any easy continuation claim: even a zero-loss gate on the
retained anchors coincides with held-out forgetting. No implementation or
outcome was independently inspected or reproduced here, and the study remains
benchmark-bound rather than testing program theory.

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
the codified-revision part of the **Proposed development path** and
**Conjectured endpoint** lenses. Across
the cluster, fixed models use traces and scores to revise prompts, tools,
middleware, routing, topology, or harness code. The same fixed outer
decomposition and machine-score boundary recurs. The reviewed records do not
add users, open-ended product demands, or a program-theory test, so listing
every optimizer would not change this function-level comparison.

### Knowledge and rationale systems retain the other form

The [Knowledge-Centric
Self-Improvement preprint](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md)
reports a controlled notes-only protocol. Stateless agents write task evidence
into forums; cross-task forums test transfer; distillation produces scoped
natural-language guidance; and later agents receive the resulting bundle. Its
held-out and cross-model experiments are designed to isolate the external
knowledge base as the changing object, while software and solver state remain
fixed and benchmark answers provide the oracle. The reported comparisons make
it a useful match to Commonplace only on external knowledge as the learned
object, not on connected-theory construction, software revision, or
software-house continuation. The ingest does not independently reproduce the
implementation or outcomes.

[PROJECTMEM](https://arxiv.org/abs/2606.12329) is a smaller, software-specific
paper-reported construction. The paper describes an append-only text event log
of issues, attempts, fixes, decisions, and notes, agent-readable projections,
and a deterministic pre-action gate that warns before repeated failed fixes or
edits to fragile files. The described gate gives retained project memory a path
to affect later action, but the reported two-month self-study does not establish
automatic acquisition, semantic revision, or product development without
people.

Proprietary or lightly evidenced coding-memory products are worth watching, not
promoting into the comparison set. Several product sources report storage or
delivery of ADRs, decisions, conventions, and lessons. Those reports establish,
at most, claimed representation and retrieval; they do not establish learning
or adequate theory.

Warp's [scheduled skill
improver](../../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
and the production [accumulated-rules
study](../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md)
illustrate the same boundary particularly clearly. Both sources describe
operational feedback becoming versioned instructions intended for later coding
sessions. In Warp's practitioner report, people write the feedback and approve
the skill PR. In the accumulated-rules study, an engineer decides whether one
accepted review comment generalizes into a future rule. These are reported
human-inclusive production learning loops, but the human performs the same
generalization and admission work that remains inside Commonplace's operator
role. Neither source independently isolates the retained rule's causal effect.

### Older constructions locate the boundary without LLMs

[Rainbow](../../sources/rainbow-architecture-based-self-adaptation.ingest.md)
is the strongest reviewed pre-LLM match on the program-model side. An external
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

- Commonplace contributes the theory-building purpose, inspectable semantic state,
  artifact authorities, and explicit admission problem.
- The inspected Ars Contexta and GBrain designs provide different versions of trace capture,
  recurrence-oriented processing, promotion state, and scheduled maintenance.
- The inspected Exo design provides a protected substrate, broad agent-executed revision, restart,
  and recovery without erasing failed-attempt evidence.
- Fluent's practitioner account provides the external-user product topology, rationale-bearing work
  packets, production observations, and corrective follow-ups.
- Recuris code and the Harness Continual Learning paper provide paired and
  historical admission patterns; the Memento-Skills paper provides a mixed
  natural-language and executable mutation unit.

These parts were built around different objectives, authority models, state
representations, and evaluators. Their juxtaposition identifies engineering
questions. It is not evidence that the parts compose, that the composite would
preserve their reported properties, or that semantic theory acquisition follows
from joining them.

## Evidence that would change the map

### Evidence of movement along Commonplace's proposed development path

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
packets, expertise, scheduling, rejection, and correction. Recuris code and the
Harness Continual Learning paper provide relevant admission patterns; the
Memento-Skills paper provides a mixed-form mutation unit; and the inspected Exo
design provides a restart-and-rollback continuation substrate. That is a
synthesis of parts, not an existing construction or evidence that the
mechanisms are compatible.

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
