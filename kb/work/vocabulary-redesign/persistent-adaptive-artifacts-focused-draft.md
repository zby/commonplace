# Persistent Adaptive Artifacts in LLM Agents: A Future-Use Taxonomy for Memory and Adaptation

## Abstract

LLM agents adapt across the whole deployed system, not only by changing base-model weights or writing to explicit memory stores. This paper calls the retained products of such adaptation **persistent adaptive artifacts**: durable objects, states, parameter sets, configurations, policies, packages, or derived views that preserve prior experience, supervision, evaluation, maintenance, or incident review. They include memory entries, workflows, prompt surfaces, tools, validators, routing rules, learned policies, adapted checkpoints, and runtime configuration.

Common labels such as memory, tool, skill, prompt, policy, validator, route, or checkpoint do not by themselves specify how retained adaptation enters later behavior. This paper instead asks: **what future system use is this artifact eligible for?** A retained artifact may be retrieved as advice, loaded as instruction, invoked as a skill, executed as a tool, enforced as a validator, used by a router, assembled into a derived view, or embedded in a learned policy. The operational unit is therefore not the artifact alone, but the retained artifact together with a specified future system use.

The paper proposes an **Artifact × Future System Use** taxonomy. The artifact side records form, substrate, and source relation; the use side records control path, authority, scope, and eligibility. This framing supports traceability across heterogeneous adaptation channels: what exists, where it lives, how it becomes consequential, what authority it has, and how that influence can be changed or withdrawn.

For system designers, the vocabulary exposes the properties that matter before choosing an implementation path. The same retained lesson may be realized as a prompt patch, workflow, script, validator, routing rule, learned policy, adapter, or weight change; the taxonomy makes visible the resulting differences in inspection, testing, cost, authority, and rollback.

Keywords: LLM agents; persistent adaptation; adaptive artifacts; agent memory; skills; context engineering; system adaptation

## 1. Introduction

A coding agent repeatedly fails at dependency resolution. It installs incompatible versions, ignores lockfile constraints, and misses conflicts that appear only after test execution. After several runs, the system may retain a reflection about the failure pattern, a project-specific dependency workflow, a conflict-checking script, a lockfile validator, a derived prompt summary, and a learned policy that decides when dependency memories should be retrieved or suppressed.

This example reflects an observed systems pressure. Long-horizon agents accumulate action and observation histories that exceed convenient context budgets; context-compression work shows that compressed histories can reduce peak token use while largely preserving task performance [Acon]. Agent-memory survey work describes memory as a write-manage-read loop rather than simple retrieval, including summarization, consolidation, contradiction handling, deletion, and policy control [MemoryAutonomousAgents].

Calling the retained products "memory" is too coarse. Memory-centered work already treats memory as more than passive retrieval [MemoryAutonomousAgents], but deployed systems also retain adaptation as prose reflections, symbolic scripts and validators, derived prompt views, and opaque learned policies. These artifacts differ in inspection, testing, execution, attribution, rollback, and future system use. A reflection may be retrieved as advice, a workflow loaded as instruction, a script invoked as a tool, a validator enforced by a runtime service, a prompt summary loaded as an instruction surface, and a learned policy used to control retrieval, writing, deletion, or summarization. For system-defining artifacts, the familiar memory "read" step generalizes into loading, invoking, executing, enforcing, assembling into derived views, auditing, or controlling another artifact.

The paper contributes an **Artifact × Future System Use** taxonomy. Prior memory, model-adaptation, context-engineering, and externalization work classifies important parts of this landscape [AIHippocampus; MemoryAutonomousAgents; AdaptationSurvey; ContextEngineeringSurvey; Externalization]. This taxonomy makes a different unit primary: not a memory, prompt, tool, policy, validator, route, or checkpoint considered in isolation, but the retained artifact paired with the authorized future system use through which it may affect later behavior.

The taxonomy also treats lifecycle state as use-specific eligibility. The same artifact can be active as retrieved advice, candidate as enforced policy, deprecated in production, and archival for audit. The practical output is a Future-Use Readiness Test: before a persistent adaptive artifact enters or remains available for future system use, the system should be able to say what exists, where it lives, how it acts, and whether that specific use is currently eligible.

The security motivation is concrete. Memory-poisoning work shows that long-term experience records can be implanted, later retrieved as trusted procedural examples, and imitated across sessions, producing persistent behavioral drift rather than a transient prompt failure [MemoryGraft]. A record that is inert as evidence becomes dangerous when retrieved, trusted, loaded, or imitated in a later task.

## 2. Scope: Persistent Adaptive Artifacts

A **persistent adaptive artifact** is any retained system object, state, package, parameter set, configuration, policy, or derived view whose content, parameters, configuration, or derived state have been produced, selected, revised, parameterized, or maintained in response to prior experience, supervision, evaluation, maintenance, incident review, user correction, or benchmarking.

The definition is broad because the paper is not trying to define memory. It is trying to define the accounting boundary for retained changes that can influence future agent behavior. Explicit memory infrastructure is one channel for retained adaptation. Externalization work argues that agent capability increasingly moves into memory, skills, protocols, and harness engineering rather than only into model weights [Externalization]. Conventional software maintenance is another channel: when a programmer fixes a harness bug, adds a regression test, revises a validator, changes a workflow, or updates configuration after observing system failure, the resulting artifact carries information from past behavior into future behavior. From a software-engineering perspective, this may be ordinary maintenance. From a deployed-agent perspective, it is also part of the system's adaptation surface when it changes how future runs unfold.

This broad boundary avoids representation bias. A retained lesson should not count as adaptation only when it is stored in a memory database and disappear from view when the same lesson is encoded as a prompt patch, routing rule, config change, validator, regression test, tool-selection rule, or human-authored policy. Otherwise, adaptation can be hidden in infrastructure side channels. The point is not that all such artifacts are cognitively or technically similar; it is that they can all carry information from prior behavior into future behavior.

The breadth is also pragmatic. A system designer cannot reason only about objects labeled memory. The same desired adaptation may be realized as a prompt, workflow, script, validator, routing rule, learned policy, adapter, or weight change; that choice affects inspectability, testability, authority, runtime cost, and rollback burden. The taxonomy supplies vocabulary for naming these parts and comparing their roles without forcing them into a single implementation category.

The practical boundary is whether a retained adaptive change, or a retained binding between an artifact and a use, can later affect agent behavior, system behavior, evaluation, routing, validation, maintenance, or artifact production. Static infrastructure remains background infrastructure rather than the focal adaptive artifact until it is produced, selected, revised, parameterized, promoted, demoted, or bound to a use because of experience, evaluation, maintenance, incident review, correction, benchmarking, or observed failure.

Adaptation may live either in the artifact itself or in the system state that binds it to a future system use. A workflow rewritten after repeated failures is adaptive at the artifact level. A static script whose code is unchanged may still participate in adaptation when incident review changes how the surrounding system selects, activates, prioritizes, or enforces it. In that case, the adaptive state is not in the script alone, but in the artifact-use binding. This distinction keeps object properties separate from deployment properties while still including software-lifecycle changes as whole-system adaptation.

Future system use is the corresponding deployment question: how can the deployed system use that retained adaptation later? Here, "system" includes the acting LLM agent as well as surrounding runtimes, retrievers, routers, validators, prompt assemblers, learning loops, evaluation pipelines, reviewers, maintainers, and human-mediated maintenance processes. Uses may occur at runtime, build or assembly time, review time, or inside learning and evaluation loops. They may be direct, as when a memory is retrieved or a validator is enforced, or indirect, as when a log, benchmark result, incident report, or scratchpad is used to create, revise, evaluate, promote, demote, or retire another artifact that later shapes behavior. Inclusion in the taxonomy does not imply equal governance burden: a candidate note, manually invoked helper, and enforced runtime validator require different levels of metadata, evaluation, and review. The framework uses a broad accounting boundary and a proportional readiness burden.

## 3. Framework: Artifact × Future System Use

Persistent adaptive artifacts should be described through two linked layers:

**Artifact × Future System Use**

The **artifact** describes the retained adaptive object, state, package, parameter set, configuration, policy, or derived view. The **future system use** describes the authorized way the deployed system, runtime, agent, maintainer, or learning loop may later use that artifact. It includes the control path, authority, scope, and eligibility of that use.

The taxonomy asks two questions separately: what retained adaptive object exists, and how may a later system use it? The same workflow may appear as a repository file, prompt fragment, skill package, or derived runtime view. The same stored workflow may be retrieved as advice, loaded as instruction, invoked as a skill, or enforced by a runtime; those are different future system uses. Two artifact-use pairings should be treated as distinct when they differ in consumer, activation trigger, consumption mode, authority, scope, or eligibility.

| Layer | Dimension | Question | Typical values |
| --- | --- | --- | --- |
| Artifact property | Artifact form | What kind of object exists, and how inspectable is its operative content? | Prose, symbolic, opaque, or mixed package |
| Artifact property | Persistence substrate and source relation | Where does persistent state live, and what is canonical or derived? | File, repository, database, vector store, prompt registry, runtime config, service object, model or policy weights |
| Future system use property | Control path | Who consumes it, when does it activate, and how is it consumed? | Retrieval, preloading, invocation, execution, enforcement, routing, assembly into a derived view, review |
| Future system use property | Authority and scope | What authority does this use have, and where does it apply? | Low-priority advice, instruction, executable procedure, service policy, enforced constraint, learned controller; user, project, organization, or deployment scope |
| Future system use property | Eligibility/lifecycle | Is this use currently eligible? | Candidate, active, superseded, deprecated, retired, archival |

### Artifact

#### Artifact form

**Prose artifacts** are interpreted through natural language. Examples include reflections, user facts, project notes, prompts, instructions, workflow descriptions, policies, playbooks, and skill descriptions. Their strength is flexibility and inspectability; their weakness is ambiguity.

**Symbolic artifacts** have machine-interpretable structure whose semantics are enforced by an interpreter, runtime, validator, or other formal consumer. Examples include code tools, schemas, tests, validators, routing tables, typed records, manifests, and runtime configuration. Their strengths are enforceability, repeatability, speed, and lower runtime cost; their weaknesses are engineering cost, narrower coverage, brittleness, and systematic failure when the specification is wrong.

**Opaque artifacts** cannot be inspected as discrete operational units in the same way as a prompt, file, validator, or code module. Examples include weights, adapters, checkpoints, and learned memory-control policies. They may improve behavior while reducing attribution, so their analysis depends on evidence, deployment constraints, behavioral tests, monitoring, and rollback.

Opacity is practical and scale-relative, not a binary property of the bytes. Distributed representations cross the inspection threshold quickly because meaning is spread across many parameters jointly. Localized artifacts such as prose, code, schemas, and tables usually remain inspectable at larger scales because they support per-unit reading, search, diffing, modular revision, and targeted tests. They too can become practically opaque once they exceed the scale of available tooling and review. The form axis therefore asks how much inspectability a class's structure buys before direct review gives way to retrieval, filtering, testing, monitoring, or other indirect evidence.

Prose and symbolic artifacts are both readable in this sense, but they differ in their semantic regime. Prose artifacts are read informally by humans or language models. Symbolic artifacts are read by formal consumers such as interpreters, validators, schema checkers, routers, or runtimes. The move from prose to symbolic form usually changes the medium, consumer, and verification regime: a markdown workflow becomes code, a loose prompt becomes a template, or an instruction becomes a schema-enforced contract. Boundary cases are common. Typed prose, schema-validated markdown, and prompts with strict templates may be read formally for shape and informally for substance.

These forms are therefore not mutually exclusive. A skill may combine instructions, examples, code, tests, metadata, tool bindings, and activation cues. A derived prompt view may combine summaries, source pointers, priority labels, and structured constraints. Form should be described directly rather than inferred from package labels.

#### Persistence substrate and source relation

Persistence substrate describes where state lives. Common substrates include files, repositories, relational or document databases, key-value stores, vector stores, prompt registries, service objects, runtime configuration, audit logs, and model or policy weights. Substrate shapes operational properties, but it does not determine them. A vector store can feed high-priority context; a file-backed script can be executed by a runtime; a prompt registry can store low-authority draft material.

Source relation describes how an artifact stands to other retained artifacts. Some artifacts are canonical sources: the authoritative version of a fact, workflow, rule, policy, validator, or configuration. Others are derived views assembled from one or more sources for a particular consumer or context: a prompt summary, skill bundle, manifest, index, route table, or client-specific loading file. A derived view may be produced by a deterministic build step, an LLM summarizer, a human editor, or a mixed process, so two views from the same source need not be identical. Derivation can also cross the form boundary: a prose workflow may be compiled into a symbolic validator or route table, while symbolic test results may be summarized into prose guidance. The important question is whether the system can tell what source material a view depends on, when it should be refreshed, what form change occurred, and what authority it carries relative to its source.

Derived views are useful because they put material where it can act, but they create drift and divergence risk. A dependency workflow may be revised in a repository while a stale skill manifest continues to route tasks to the old procedure. A prompt summary generated from a policy may omit an exception, preserve old priority, or vary across regenerations. These are not only storage errors; they are source-relation failures that matter when the derived view has a future system use.

### Future system use

Future system use describes how a retained artifact may later be made consequential by an agent, runtime, maintainer, or learning loop. Its main dimensions are control path, authority, scope, and eligibility for that use.

#### Control path and authority

A control path says what happens after an artifact is retained. It follows the artifact from storage into a later run: who can find it, what activates it, and how it is consumed. It is the route inside a future system use by which an artifact informs behavior or defines part of the system.

| Part of control path | Question | Examples |
| --- | --- | --- |
| Consumer | Who or what uses the artifact? | Acting agent, retriever, context scheduler, planner, runtime service, validator, router, view assembler, reviewer, maintainer, learning loop |
| Activation | What causes it to become relevant? | Retrieval, preloading, trigger matching, scheduler selection, explicit invocation, service lookup, runtime enforcement, route selection, derived-view assembly |
| Consumption mode | How is it used? | Read, loaded, invoked, executed, enforced, inspected, reviewed, routed through, assembled into another view |

Authority and scope specify the strength and reach of that use. An artifact can activate automatically while having low authority, or activate manually while having high authority. Authority concerns precedence, actionability, and enforcement; scope concerns whether the use applies to one user, project, organization, deployment, or class of tasks. Automaticity, invisibility, irreversibility, and opacity can amplify risk, but they are deployment modifiers rather than authority itself.

Declared authority and effective authority can diverge. A nominally advisory memory may dominate behavior if it is always included, placed late in the prompt, repeated often, or phrased imperatively. A formally authoritative rule may have little effect if it is not surfaced to the component that acts. Future system use analysis should therefore record both the authority assigned by design and behavioral evidence that the system actually treats the artifact that way.

**Knowledge use and system-defining use.** Control path and authority also explain the difference between knowledge use and system-defining use. The distinction is not between two intrinsic artifact types. An artifact functions as **knowledge** when it is consumed as evidence, context, or advice that a future agent or human may weigh. It functions as **system definition** when its use gives it authority over instructions, routing, execution, validation, evaluation, memory operations, or policy.

| Same artifact | Knowledge use | System-definition use |
| --- | --- | --- |
| Reflection | Retrieved as prior experience the agent may consider | Loaded as a standing instruction to follow prior reflections |
| User preference | Shown as context with uncertainty and provenance | Enforced automatically by a personalization layer |
| Workflow | Read as advice during planning | Preloaded as required procedure or invoked as a skill |
| Schema | Read as documentation | Used by an interpreter to validate inputs or outputs |
| Prompt summary | Used as a compact source note | Loaded as high-priority policy or instruction surface |
| Memory policy | Described in documentation | Learned or configured controller selects write, retrieve, update, delete, or summarize operations |

The artifact's text or package may remain unchanged while its behavioral meaning changes. What changes is the future system use: route, authority, scope, eligibility, or some combination of these.

#### Eligibility and conflict

Eligibility is part of a future system use. It answers whether an artifact may be used in a specified way now, and under what conditions. A note may be active for retrieval as low-priority context but not active for automatic policy loading. A workflow may be active for manual use by a reviewer but still candidate for runtime enforcement. A validator may be active for staging but deprecated in production.

| State | Meaning | Use status |
| --- | --- | --- |
| Candidate | Persisted for review, testing, or possible activation | Not eligible for ordinary activation except as explicitly marked evidence |
| Active | Approved for its stated use | Eligible to affect behavior within defined authority and activation rules |
| Superseded | Replaced by a newer artifact | Retained for provenance; yields precedence to replacement |
| Deprecated | No longer recommended or trusted for ordinary use | Blocked, down-ranked, warning-labeled, or available only through explicit access |
| Retired | Removed from behavior-shaping use | Not eligible for activation; retained only if needed for audit, rollback, or investigation |
| Archival | Preserved as historical evidence | Immutable or controlled-access record; not behavior-shaping by default |

Persistent adaptive systems also need conflict policy. A user preference may conflict with a project policy. A derived prompt view may lag behind its canonical source. A learned retrieval policy may suppress a memory needed by a validator. Conflict handling should record which artifact wins, whether precedence depends on source, recency, authority, scope, or consumer, and whether a lower-authority artifact may surface evidence that a higher-authority artifact is stale, mis-scoped, or superseded. Derived views should be invalidated or refreshed when their source artifacts are superseded, deprecated, or retired.

## 4. Applying the Framework

Return to the dependency-resolution example. After repeated coding-agent failures, suppose the system retains six artifacts: a reflection about the failure pattern, a project-specific workflow, a conflict-checking script, a lockfile validator, a derived prompt summary, and a learned memory policy.

A generic memory analysis would flatten their differences. Their operational roles depend on future system use: control path, authority, eligibility, and evaluation target.

| Artifact | Control path | Behavioral role | Failure mode | Needed check |
| --- | --- | --- | --- | --- |
| Reflection | Retrieved as context | Knowledge | Stale or overgeneral advice | Provenance, freshness, retrieval precision, demotion after misleading use |
| Workflow | Loaded as instruction or invoked as skill | System definition | Over-activation or conflict with project constraints | Trigger evaluation, conflict handling, source alignment, task-success test |
| Conflict-check script | Explicitly invoked or selected by tool router | Executable procedure | Side effects, dependency errors, false confidence | Unit tests, sandboxing, permissions, rollback |
| Lockfile validator | Enforced by runtime | Constraint | False blocks or false passes | False-block / false-pass evaluation, override policy, staged rollout |
| Derived prompt view | Preloaded before dependency tasks | Instruction surface | Drift from canonical workflow or omitted constraints | Source-of-truth tracking, refresh tests, derived-view audit |
| Learned retrieval policy | Selects memory operations | Learned controller | Hard-to-attribute retrieval failures or poisoning | Behavioral probes, ablations, monitoring, rollback, staged activation |

This use-specific view matches a broader shift in memory evaluation. Recent benchmarks move beyond static fact recall toward memory organization, multi-session interaction, test-time learning, long-range understanding, and selective forgetting [StructMemEval; MemoryAgentBench]. For persistent adaptive artifacts, the same principle generalizes: evaluation should ask what downstream behavior a specific future use is supposed to improve or constrain.

The same symbolic object can play very different roles. A conflict-checking script may be documentation, an agent-invoked helper, an automatic pre-write check, or an enforced blocker. The code may be identical across these uses; the control path changes its behavioral meaning and the evidence required before deployment.

```python
def validate_lockfile(lock):
    for package in lock.get("packages", []):
        version = package.get("version", "")
        if not version or any(mark in version for mark in "*^~><"):
            return [f"{package.get('name', '<unknown>')}: version is not pinned"]
    return []
```

The example also shows how the framework improves failure diagnosis. Suppose the dependency workflow is updated after a package-manager change, but the derived prompt view used by the coding agent is not refreshed. The agent keeps following the old instruction surface and produces lockfile errors. Calling this "stale memory" is too coarse. Under this framework, the failure is source-to-derived-view drift in a high-authority instruction use. The repair is not merely to delete a bad memory; it is to restore source alignment, refresh or invalidate the derived view, and decide whether the stale view should be superseded, deprecated, or retired for that use.

## 5. Relation to Existing Work

Prior work covers much of the surrounding design space. Memory surveys classify temporal scope, read-write operations, representational substrate, consolidation, forgetting, and memory-management policy [AIHippocampus; MemoryAutonomousAgents]. Model-adaptation surveys classify update mechanisms, training signals, and parameter-efficient methods [AdaptationSurvey]. Context-engineering work treats the active context supplied to an LLM as a managed system surface spanning retrieval, generation, processing, memory systems, tool-integrated reasoning, and multi-agent systems [ContextEngineeringSurvey]. Work on externalization and experience compression also shows that agent capability can move into memory, skills, rules, tools, and harness engineering, raising systems concerns around evaluation, governance, and the coordination of external infrastructure [Externalization; ExperienceCompression].

Existing categories remain useful, but they do not make artifact-use pairings the primary governance unit. This paper asks a deployment question left underspecified by those labels: once a persistent adaptive artifact exists, through what future system use can it affect behavior? A representation-centered memory taxonomy can classify both a retrieved reflection and a derived prompt summary as textual memory-like artifacts [GenerativeAgents; Reflexion; AIHippocampus]. The future-use taxonomy distinguishes them because one may be low-priority retrieved evidence while the other may be a high-priority instruction surface derived from a canonical source. A tool or skill taxonomy can classify both a helper script and a validator as symbolic procedures [Voyager; SkillWeaver]. The future-use taxonomy distinguishes an optional helper from an enforced runtime blocker because their authority, scope, eligibility, rollback, and evaluation targets differ.

| Existing area | Usually classifies | This paper adds |
| --- | --- | --- |
| Memory taxonomies | Representation, read/write operations, consolidation, forgetting | Authority, activation, and use-specific eligibility |
| Model adaptation | Update method, training signal, parameter efficiency | Deployed checkpoint as an opaque artifact with scope, rollback, and use-specific lifecycle |
| Tool and skill learning | Production and reuse of procedures | Executable authority, permissions, tests, and invocation paths |
| Context engineering | Construction of active context | Persistent source-control relationships behind prompt surfaces, indexes, and derived views |
| Security and privacy | Poisoning, leakage, access control | Where stored material becomes behaviorally consequential |

Verbal-reflection systems preserve prose artifacts that are usually retrieved as advice [GenerativeAgents; Reflexion]. Skill-library systems preserve mixed or symbolic artifacts that may be invoked as executable procedures [Voyager; AgentWorkflowMemory; SkillWeaver]. Prompt-optimization systems preserve instruction surfaces whose authority depends on loading context [PromptOptimizers]. Learned memory policies preserve opaque controllers that affect retrieval, writing, deletion, or summarization [MemoryAutonomousAgents; AgeMem]. Security work shows why the distinction matters: stored material becomes dangerous when it is retrieved, trusted, loaded, invoked, or otherwise made consequential [AgentPoison]. Across these systems, the common deployment question is the same: through what future system use does retained adaptation enter later behavior?

## 6. Evaluation and Readiness

Persistent adaptive artifacts should be evaluated against their intended future system uses. A model checkpoint, note, workflow, skill, validator, derived view, and learned memory policy should not share the same success test simply because they are all persistent adaptations. A retrieved note is judged by usefulness and non-interference; an enforced validator is judged by false blocks, false passes, override behavior, and rollout safety. This does not replace task-level benchmarking or longitudinal monitoring; it specifies which artifact-use pairing those evaluations should be attached to.

| Future system use | Primary evaluation target |
| --- | --- |
| Retrieved advice | Retrieval precision, usefulness, non-interference, freshness |
| Loaded instruction | Task improvement, conflict rate, precedence behavior, override safety |
| Invoked skill | Success rate, invocation precision, side effects, permission scope |
| Executed tool | Correctness, sandbox safety, reproducibility, rollback |
| Enforced validator | False positive and false negative tradeoff, override policy, staged rollout behavior |
| Derived view | Source alignment, freshness, divergence, compression loss, priority preservation |
| Learned memory policy | Behavioral probes, ablations, rollout monitoring, attribution, rollback |
| Model checkpoint or adapter | Behavioral evaluation, regression tests, scope control, versioning, rollback |

### The Future-Use Readiness Test

A persistent adaptive artifact should not enter or remain available for future system use unless the system can answer two artifact questions and two use questions.

1. **What exists?** Identify the artifact's form, package, operative content when inspectable, and inspectability limits.
2. **Where does it live?** Identify the persistence substrate, access path, source evidence, canonical version, versioning model, provenance, owner, permissions, rollback path, and replacement mechanism.
3. **How does it act?** Identify the consumer, activation trigger, consumption mode, authority, scope, expected effect, override rules, and evaluation target.
4. **Is this use eligible?** Identify whether this future system use is candidate, active, superseded, deprecated, retired, or archival, and define the conditions for activation, demotion, supersession, retirement, or archival retention.

For the lockfile validator, a compact artifact-use record is enough to instantiate the framework.

| Field | Example |
| --- | --- |
| Artifact ID | `lockfile-validator-v3` |
| Artifact form | Symbolic validator |
| Substrate | Repository file and runtime service |
| Source relation | Canonical validator for Project X dependency updates |
| Consumer | Runtime write gate |
| Activation | Before lockfile writes |
| Consumption mode | Enforced validation |
| Authority | Blocking constraint |
| Scope | Project X dependency updates |
| Eligibility | Active in staging; candidate in production |
| Evaluation | False blocks, false passes, downstream task success, override rate |
| Rollback | Disable enforcement, restore previous validator, and invalidate derived prompt or skill references |

The record is intentionally small. Its purpose is to attach evaluation and rollback to the artifact-use pairing rather than to the validator file alone. For low-authority or single-user uses, this may be a minimum viable record. For high-assurance uses, the same schema can be extended with provenance, approvals, monitoring probes, rollback tests, conflict rules, and audit history.

This test is not a complete governance program or risk taxonomy. It is a practical minimum for traceability. Persistent adaptation is not just retained information; it is retained adaptive state, procedure, policy, validation, routing, execution, or learned control that can shape future runs.

## 7. Limitations

Because the category is operational rather than ontological, the framework trades narrowness for coverage across heterogeneous agent systems. The relevant boundary question is not whether every deployment would assign the same label, but whether retained adaptive state has an identifiable future system use.

The framework also does not provide a complete safety or governance taxonomy. Promotion, source-to-derived-view drift, poisoning, privacy exposure, stale activation, conflicting authority, and opaque learned behavior are visible through the artifact-use lens, but this paper does not enumerate every operational risk. Its purpose is to locate future system use pathways so that system-specific evaluation and governance can be attached to the right artifact-use pairing.

Lifecycle metadata may be expensive for lightweight artifacts and indirect for opaque ones. The framework should therefore be applied proportionally. Stronger, broader, less visible, more irreversible, or more enforceable future system uses justify stronger metadata and evaluation. For opaque artifacts, metadata and evidence are companion records, not substitutes for content inspection. They make the artifact traceable, bounded, testable, monitored, and reversible through its future system uses rather than directly readable.

## 8. Conclusion

Agent adaptation becomes a deployment problem when retained adaptive artifacts survive one run and affect future behavior. The relevant artifact may be a fine-tuned parameter set, note, fact, prompt, workflow, tool package, validator, route, derived view, runtime configuration, or learned memory policy.

Future system use is what turns persistent adaptive state into behavior. A reflection can be advice or policy; a workflow can be documentation or executable procedure; a schema can be reference material or an enforced contract; a prompt summary can be a compact note or a high-authority instruction surface. The central deployment question is whether retained adaptive state has acquired a behavior-shaping use: what exists, where it lives, how it acts, what authority it has, and how that influence can be changed or withdrawn.

The paper's main claim is therefore deliberately narrow: persistent adaptation in LLM agents should be analyzed at the level of artifact-use pairings. Broad labels such as memory, tool, skill, policy, prompt, route, configuration, or checkpoint are useful implementation labels, but they do not by themselves identify how retained adaptation governs future behavior. The future-use taxonomy supplies that missing deployment vocabulary by describing not only what adaptive artifacts exist, but how they may become consequential in later system behavior.

## References
