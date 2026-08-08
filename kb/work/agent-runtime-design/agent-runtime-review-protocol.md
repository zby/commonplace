# Provisional Agent-Runtime Review Protocol

## Status and purpose

This is a workshop protocol for testing how to review agent runtimes, including systems that describe themselves as harnesses. It is not yet a type contract or a skill. Its purpose is to make pilot reviews comparable enough to reveal which questions recur, which are conditional, and which distinctions change an architectural assessment.

The protocol inherits the `kb/agentic-systems/` quality goal: fidelity plus economy. It should produce a compact account of what a system actually wires, where its responsibilities end, and which work stories its guarantees support. It should not produce an exhaustive feature catalogue or a universal score.

## Review target

The review target is the **operational execution system and its externalized boundaries**, not the repository name or user interface alone. Begin by locating these roles:

- **model or bounded inference call** — where semantic judgment occurs;
- **agent runtime** — what owns execution state and turns judgments into situated work;
- **runtime client** — CLI, TUI, API, service, or host callback that starts, observes, steers, interrupts, or authorizes work;
- **host application** — what supplies responsibilities the runtime does not own;
- **memory subsystem** — retained knowledge and context engineering, reviewed separately where substantial;
- **builder or improvement plane** — what can change prompts, tools, policies, executors, or the protected runtime.

One process may contain several roles, and one product may distribute one role across services. The review describes responsibility before process placement.

The word **harness** should be preserved when it is the system's own term. Use **agent runtime** for the architectural object under comparison.

A pattern, generated program, workflow, tool, or extension subsystem is not automatically a runtime. When one mechanism deserves detailed analysis, record its enclosing operational system and attribute scheduling, authority, client, durability, and recovery guarantees to the layer that implements and wires them. Mechanisms may be compared across systems in a workshop analysis, but completed runtime reviews should not present them as peer runtimes.

Treat target classification as an early review result, not an administrative precondition. A repository may contain a returning model-call library, an agentic loop, optional UI adapters, and durable integrations without making them one operational surface. If the selected target does not own situated execution or its lifecycle, stop the runtime comparison at that boundary: analyse it as a mechanism or review the enclosing host that turns it into operational work. Do not manufacture runtime deficiencies from responsibilities the target never claims.

For an embedded library, record both the inner and outer horizons. The library may own one invocation's transition and tool semantics while the host owns the sequence of invocations, persistence, user relationship, deployment, and recovery. “Who owns the loop?” is incomplete unless the review says which loop.

## Evidence contract

Every review opens with a one-line evidence basis and records:

- repository or document identity;
- pinned revision or dated version;
- capture date;
- source areas inspected;
- tests or live scenarios run;
- important evidence not obtained.

Keep four evidence states distinct in the prose:

1. **Implemented and wired** — source shows the mechanism on the shipped execution path.
2. **Available to an integrator** — an API or hook exists, but the shipped product does not exercise it.
3. **Documented or proposed** — a claim or intended design was found without matching implementation evidence.
4. **Not established** — the inspected evidence does not answer the question.

Absence from one search is not proof of absence. Conversely, an interface, example extension, or test fixture is not evidence that every deployment gets the property. When docs and source disagree, say so and prefer the source for implemented behavior.

Code-grounded reviews should use commit-pinned source links for load-bearing claims. Live operation establishes deployed behavior that static inspection cannot, but it does not replace source evidence about guarantees or alternative paths.

For this workshop's primary methodology tests, a completed runtime review must be code-grounded. Documentation-only, closed-source, and first-hand interface evidence may still motivate questions or support a mechanism analysis, but cannot establish that the review method finds ownership boundaries, alternate execution paths, or enforcement gaps in an implementation. This is an evidence rule for the review methodology, not a claim that closed-source systems are not runtimes.

## Code-grounded review procedure

Use the smallest source inspection that can establish the operational boundary and challenge its consequential guarantees. Code-grounded does not mean reading every file.

1. **Prepare a stable source basis.** Read repository instructions, identify the canonical remote, pin the inspected commit, record the capture date and checkout state, and note whether dependencies or adjacent repositories are unavailable. Do not silently review a moving branch.
2. **Inventory operational surfaces.** Locate public entry points, run objects, model adapters, tool dispatch, clients, persistence adapters, extension loading, and tests. Sketch candidate inner and outer loops before choosing the target. Repository and product names are search handles, not architectural boundaries.
3. **Classify the target.** Decide whether the selected surface is an enclosing runtime, embedded inner runtime, client, returning computation, workflow, extension mechanism, builder, or host integration. Name the enclosing owner for responsibilities outside it. If no operational runtime is present, redirect the work to a mechanism analysis or the enclosing host rather than continuing with a deficient-runtime template.
4. **Record claimed work and entry paths.** Use documentation to identify the work stories and guarantees the system invites users to rely on. For each claim, identify the shipped entry path that would have to uphold it. Separate default paths, optional adapters, examples, tests, and integrator hooks.
5. **Trace one ordinary invocation.** Follow a request through identity creation, state transitions, semantic-call projection, model response, effect dispatch, events, client controls, terminal result, and retained state. For embedded libraries, trace both the inner invocation and the host contract around it.
6. **Enumerate alternate paths before assessing guarantees.** Search for direct model calls, provider-native tools, raw host callbacks, trusted extension code, generated code, subprocesses, remote workers, manual graph control, and durable variants. A guarantee applies only to the paths its enforcement point actually covers.
7. **Run forcing traces selected by the claims.** Trace two to four cases such as denial or unresolved authority, interruption or retry, child escalation, process loss, generated execution, or durable activation. Prefer a focused test or probe when static source cannot establish concurrency, persistence, isolation, event delivery, or effect-commit behavior. Record tests that could not run.
8. **Build the responsibility and guarantee ledger.** For every load-bearing conclusion, name the owner, enforcement point, evidence state, guarantee strength, alternative paths, and required host contract. Treat checked-in tests as implementation evidence for the exercised composition, not as proof that all deployments inherit it.
9. **Write from the ledger, then perform semantic QA.** Use the fixed spine below and keep only distinctions that change use or trust. Reopen every load-bearing citation, challenge negative claims and words such as “prevents,” “durable,” “isolated,” and “all,” then run deterministic validation. A separate reviewer may gather or check source traces, but the final writer owns target classification, cross-path attribution, and the architectural judgment.

This procedure should eventually become the production skill if independent reviews reproduce its boundary and guarantee judgments. Checkout preparation, parallel source tracing, citation capture, semantic QA, and validation belong in that skill; the completed-review type should contain only the stable result fields.

## Begin from claimed work

Before applying architectural lenses, state what work the system claims to support. Typical work stories include:

- interactive tool use with a person present;
- headless or embedded agent execution;
- long-running or resumable tasks;
- delegated research, review, or mutation;
- deterministic automation authored by an agent;
- distributed execution across workers;
- model-authored symbolic decomposition;
- durable self-generated change to the runtime or agent's own behavior-determining organization.

These stories select the relevant tests. Durable approval is material for a service that claims resumable workflows. Its absence need not condemn a small interactive loop. A system that claims subagent isolation must be examined across context, authority, lifecycle, and result semantics even if it does not claim distribution.

## Trace forcing scenarios end to end

Do not infer the architecture only from type names. Trace two to four concrete scenarios from request to terminal outcome. Select scenarios that pressure the system's claims:

- an ordinary tool or domain effect;
- an effect that policy denies or leaves unresolved;
- a delegated child or remote worker with narrower authority;
- interruption, failure, retry, or process loss;
- model-authored code or runtime mutation, when claimed;
- promotion of a run-local result into durable behavior, when claimed.

For each scenario, identify:

1. the principal and input;
2. the state transition or scheduler path;
3. the context and capability surface supplied;
4. the effect-enforcement point;
5. events and client-visible controls;
6. the result, denial, inline wait, terminal deferral and re-entry, failure, or recovery path;
7. what persists and what is lost.

This end-to-end trace distinguishes an implemented control path from a collection of potentially composable hooks.

## Stable review lenses

The lenses below are a question inventory, not mandatory equal-sized sections.

| Lens | Questions that recur | Applicability |
|---|---|---|
| Boundary and purpose | What does the runtime own, externalize, or assume? Which work stories does it claim? | Always |
| Execution and scheduling | Who owns the loop, decomposition, concurrency, stop conditions, queues, and dependencies? | Always |
| Context and state | How are instructions, tools, retained state, child projections, compaction, and limits assembled? | Always; depth follows claims |
| Effects and authority | What can the model attempt, what may the principal perform, and what can the environment physically permit? | Always |
| Client and control | What can a person or application observe, steer, interrupt, authorize, resume, or audit? | Always |
| Delegation and coordination | How are children or workers created, scoped, joined, cancelled, and reconciled? | When delegation, teams, or workers are claimed |
| Approval routing | Who can request authority, who resolves it, what is deferred, how continuation or re-entry works, and how operator attention is bounded? | When unresolved authority can occur |
| Reliability and recovery | What do completion, retry, cancellation, idempotency, replay, and resume mean? | Proportional to duration and effect risk |
| Dynamic extension | Who authors code or configuration, what does it change, and with what authority, namespace, lifetime, admission path, and resource limits? | When extensions or generated programs affect execution |
| Builder and improvement plane | What may change future behavior, what evidence admits the change, and what remains protected? | When the system builds or modifies agents or itself |
| Observation and evaluation | Which events, traces, costs, failures, and outcome evidence support diagnosis or audit? | Always; evaluation depth follows claims |
| Adoption and deployment | Which providers, operating systems, sandboxes, services, and fleet controls carry architectural assumptions? | When they change guarantees or usability |

If a lens is central to the claimed work but evidence is missing, record `not established`. If the lens does not apply to the system's boundary, say why rather than treating it as a failed feature.

## Protected mechanism and extensible policy

Use scheduler, context engine, and execution substrate as a starting map. Within each, separate protected mechanism from replaceable strategy:

| Component | Candidate protected mechanism | Candidate extensible policy |
|---|---|---|
| Scheduler | Run and call identity, state transitions, suspension, cancellation, fork/join mechanics, continuation recovery | Decomposition, topology, ordering, aggregation, retries, stopping heuristics |
| Context engine | Bounded call envelope, scope boundaries, provenance channels, size enforcement | Retrieval, compaction, prompt construction, source selection, child projection |
| Execution substrate | Effect interception, authority enforcement, isolation ceiling, durable-state primitives, resource accounting | Tool implementations, domain integrations, transforms, task-local programs |

These columns are hypotheses to test against the system. Do not praise a mechanism merely for being in the protected column. Ask whether it must be protected for the system's claimed guarantees, whether extensions can bypass it, and whether the implementation actually routes all relevant paths through it.

## Authority record

Every review should distinguish:

- **Capability surface** — actions exposed to a model, generated program, extension, or worker.
- **Grant set** — effects the current principal may execute under policy.
- **Isolation envelope** — the maximum effects the deployed environment permits regardless of policy.

These are architectural terms, not names to match lexically. If a source calls plugins, hooks, or composable behavior wrappers “capabilities,” establish whether they carry authority before mapping them to the grant set. Conversely, a structured approval record is not automatically authorization: establish who can forge it, which principal and effect it covers, and where the resulting decision is enforced.

For consequential effects, record the principal, effect class, target scope, lifetime, limits, decision source, and enforcement point where the evidence supports them. A tool-name allowlist is evidence about the capability surface and perhaps dispatch. It is not automatically evidence of path confinement, network isolation, secret separation, or attenuated delegation.

When approval is present, also establish:

- requesting principal;
- policy resolver;
- user-facing client or headless policy source;
- direct, parent-brokered, or absent request routing;
- resolution shape: inline waiting, terminal pending output plus later re-entry, or another protocol;
- which dependent effect or continuation is blocked, whether unrelated work may proceed, and what state persists while unresolved;
- run, conversation, request, and decision identities across any re-entry;
- denial and escalation result;
- effect of concurrent requests on operator attention;
- whether the shipped client exercises the path.

Do not assume that more approval prompts mean stronger governance. Describe whether the design resolves authority before delegation, prompts during effects, aggregates requests, fails closed, or routes escalation to a parent. Judge the choice against the claimed work story.

## Delegation and dynamic extension records

For each child, team member, or worker, establish:

- context inheritance and isolation;
- capability surface, grants, and environment;
- parent-child identity and authority relation;
- task, result, error, and progress protocol;
- join, cancellation, timeout, and failure propagation;
- shared artifact ownership and conflict handling;
- escalation when assigned authority is insufficient.

For extensions and model-authored code, classify the horizon:

| Horizon | Typical authorship | Typical lifetime | Admission question |
|---|---|---|---|
| Call-local computation | Model or host | One call or step | Does it remain inside the current envelope? |
| Run-local control program | Model or host | One task or run | Can it compose runtime primitives without ambient authority? |
| Durable project capability | Model, builder, or human | Cross-session | What review, test, version, rollback, and retirement admit it? |
| Runtime or policy extension | Maintainer, builder, or model | Deployment lifetime | Is it trusted installation outside ordinary run authority? |

Record ordinary agent-authored declarative workflows separately from online model-authored guest code. Both are symbolic decomposition, but their authoring time, authority, and persistence differ.

Do not use `session-local` without defining the session. Record whether state lasts for one model call, one top-level run, one runtime instance across several runs, one operating-system process, or later processes through explicit discovery and activation. A retained artifact and an operative registry entry may have different lifetimes.

Do not infer self-modification from either generatedness or durability alone. Record three independent facts:

1. **Authorship:** Did a process inside the declared system boundary generate the concrete change?
2. **Persistence:** Are only the bytes retained, or does a later run discover and exercise the accepted change?
3. **Target:** Does it alter the bounded runtime's own [behavior-determining organization](../../notes/definitions/behavior-determining-organization.md), or only an external work product or project capability?

For this workshop, call a pathway **runtime self-modification** only when the change is self-generated, durable across the relevant later-operation horizon, and directed at the runtime's own organization. Human approval of admission does not erase model authorship. Automatic installation does not establish improvement, adequate verification, or reflective coverage. [The RLM, Tendril, and llm-do comparison](../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) supplies boundary cases in which generatedness and durability vary independently.

For a durable extension, also record the later activation path. Persistence of source bytes without discovery, loading, or execution is archival retention, not an operative runtime change.

## Writing shape: fixed spine, flexible body

The review should use this fixed spine:

1. **Evidence basis.** One compact paragraph.
2. **Architectural characterization.** What the system is, the work it targets, and the main responsibility boundary.
3. **Runtime map.** A short paragraph or table locating runtime, client, host, memory, and builder roles.
4. **Discriminating mechanism sections.** Usually three to six sections selected from the stable lenses.
5. **Architectural assessment.** Scenario-relative strengths, tradeoffs, externalized responsibilities, and unsupported implications.
6. **What to watch.** Specific changes that would alter the assessment.
7. **Relevant Notes.** Theory and related-system links that explain the analysis.

Do not require one heading per lens. A small runtime may need one combined section for state, control, and recovery. A distributed control plane may need separate scheduler, worker, policy, and audit sections. The mandatory information is the spine and the consequential mechanisms, not uniform headings.

A provisional template is:

```markdown
---
description: "{Discriminating retrieval description}"
type: kb/types/note.md
traits: [has-external-sources]
tags: [{only useful theory-routing tags}]
---

# {System name}

**Evidence basis:** {source identity, revision, capture date, inspected scope, operation/tests, limits}.

{Architectural characterization: what it is, claimed work, and decisive boundary.}

## Runtime map

{Locate runtime, client, host, memory, and builder roles.}

## {Discriminating mechanism}

{Trace implemented behavior, enforcement, failure path, and evidence.}

## {Further discriminating mechanisms}

{Use only what this system needs.}

## Architectural assessment

{Supported work stories, tradeoffs, externalized responsibilities, unsupported implications, and unknowns.}

## What to watch

- {Specific possible change and why it would alter the assessment.}

---

Relevant Notes:

- {Markdown link to note, resolved relative to the eventual review under `kb/agentic-systems/`} — {formal relation and reason}
```

## Assessment discipline

End with a scenario-relative judgment, not a total ranking. Separate:

- **implemented strength** — a wired mechanism supports a claimed work story;
- **deliberate externalization** — another named layer owns the responsibility;
- **tradeoff** — a simplification improves one work story while narrowing another;
- **gap** — a claimed work story requires a mechanism that is missing or bypassable;
- **unknown** — the evidence cannot establish the property;
- **misleading implication** — product language invites a stronger conclusion than the wiring supports.

“Minimal” is not itself praise, and “feature-rich” is not itself criticism. Minimality concerns which semantic commitments the runtime fixes. Complexity is justified only by the guarantees and work stories it buys.

## Promotion test

Before this protocol becomes a type or skill, pilot it against materially unlike systems and ask:

- Do the same distinctions recur?
- Do they change an architectural judgment?
- Can the writer establish them from source without speculative classification?
- Which fields are always useful, conditional, or redundant?
- Does the fixed spine improve comparison without making reviews longer than their evidence warrants?
- Can deterministic validation check any part of the contract without pretending to validate semantic truth?

Only stable, discriminating fields should enter a type. The eventual skill should own checkout preparation, evidence capture, drafting, semantic QA, and validation; the type should describe the completed review rather than encode the whole production procedure.
