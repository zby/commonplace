# Audit of Commonplace's hardest behavioral-authority paths

## Result in one paragraph

The six paths examined support **broad, path-relative addressability**, not complete addressability. Commonplace makes the canonical artifacts carrying goals, collection criteria, review criteria, revision procedures, validator rules, and requested model bindings readable and selectively editable. The repository also records operative revisions of both natural-language and symbolic machinery. Coverage weakens at two relations that file writability does not settle: a requested model binding is not reliably bound to the model that actually executes, and the generic authority by which a designated maintainer admits a change is named but not represented as a designation, scoped grant, or content-bound decision. The latter is the strongest counterexample to the working claim's inclusion of revision authority.

## Boundary and evidence scale

This audit uses [Commonplace's declared frame](../../reference/commonplace-declared-frame.md): the repository, its operative artifacts, consuming commands, validators, review store and agents, and designated maintainers in their established roles are inside. Provider weights, inference infrastructure, and hosting are outside. Model *selection* remains in scope because repository artifacts request bindings and review freshness partitions by them; editing or interpreting provider weights does not.

The audit distinguishes:

- **Declared** — prose states that the operation or route is intended, without showing that current wiring provides it.
- **Structurally supported** — current artifacts and wiring provide the operation, but no later causal trace establishes its exercise. Case-file shorthand: **supported**.
- **Demonstrated** — a retained trace or executable test shows the operation occurred.
- **Routinely exercised** — repeated retained use establishes ordinary operation rather than one episode. This audit does not infer routine exercise from installed wiring or test coverage. The current Commonplace store establishes it for the explanatory-reach assay path, but not for the other five paths.
- **Unestablished** — the relation is absent, only reconstructed, or contradicted by retained evidence.

Addressability operations are identify, inspect, state the commitment, criticize it, and selectively revise or retire it. Operative installation, warrant, and continuity are recorded separately; none is smuggled into addressability.

## Compact comparison

| Path | Consumer, channel, force | Addressability standing | Installation and continuity | Strongest missing edge |
|---|---|---|---|---|
| Global KB goals | Agent; always-loaded context; instruction and inclusion selection | Artifact explicit; inspection and revision supported | Next-session loading supported; later dependence unestablished | No retained generic admission or warrant rule for changing the objective |
| Explanatory-reach criterion | Author/reviewer; collection contract and assay; instruction and audit trigger | Distributed target identified and historically revised | Gate routinely exercised; full four-part later review dependence unestablished | Derived criterion copies and prompt scaffolding are outside one freshness/dependency closure |
| Tag-README validator | Validator and connect agent; validation/instruction; enforcement and routing | Spec, schema, code, tests, and consumer paths explicit | Operative revision and later extension/use demonstrated | Invocation remains explicit; human admission of the code change is reconstructed |
| Revision lifecycle | Agent/maintainer; routing, review, instruction, validation; proposal/decision/installation force | Method and artifacts explicit; revision of the method demonstrated | ADR 056 → ADR 057 → ADR 063 demonstrates reuse and another challenge | The method maps surfaces but supplies no repository-wide admission condition |
| Model binding | Harness/worker/finalizer; skill metadata and dispatch; selection/configuration influence | Requested binding and partition identity explicit | Effective binding is runtime-contingent; a false-provenance incident is demonstrated | No trusted requested-to-realized binding or execution attestation |
| Maintainer admission | Maintainer consumes candidate/diff; conversation/review/Git; selection/admission | Candidate and role name inspectable; grant relation unestablished | File installation occurs, but authorization is not bound to the installed version | Who is designated, grant scope, and the generic condition that makes a change incumbent |

The shared columns earn a table; the moving boundary sits in the case files below.

## Case 1 — Global goals are explicit, but their revision path is lightly governed

### Operative path

The operative artifact is the `## KB Goals and Scope` section of [`AGENTS.md`](../../../AGENTS.md): purpose, in/out scope, and quality bar. [Control-plane goals](../../reference/control-plane-goals.md) states the intended causal relation: every agent invocation receives the file in always-loaded context, including forked skill contexts. The consumer is the agent, the channel is session bootstrap/context assembly, and the force is instruction plus selection—especially whether a candidate belongs in the KB at all. [KB goals in always-loaded context guide inclusion decisions](../../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) supplies the rationale and says goals should change when the domain changes.

Applicability matters here. The same consumer, channel, and force would describe a goal that applied only to source ingestion, only to note admission, or to every repository action. The current artifact says the goals govern the KB generally; that target scope is necessary to enumerate the path.

### Addressability and revision

The objective is easy to identify, read, quote, criticize, and edit. The revision route is the general workshop/theory/design route plus a direct `AGENTS.md` edit; the goal note supplies a trigger (domain change) but no specialized procedure or acceptance test. A successor would enter the live path when a later session loads the file. Because the successor remains in the same location and format, another revision is structurally supported.

No retained episode examined here demonstrates a changed Commonplace goal governing a later inclusion decision. More importantly, the repository does not record a generic condition under which one proposed objective displaces another. That is a warrant/admission gap, not a reason to deny that the objective artifact itself is addressable.

### Standing

- Identify, inspect, criticize, revise: **supported**.
- Operative entry of the incumbent: **supported by the declared load path**, not traced to one later decision in this audit.
- Successor dependence and continuity: **supported**, not demonstrated.
- Strongest missing edge: the acceptance and warrant relation for a changed top-level objective.

## Case 2 — Explanatory-reach is addressable across theory, contract, and review, but the dependency closure is manual

### Operative paths

Explanatory-reach is distributed across several authority-bearing uses:

- The anchor theory, [First-principles reasoning selects for explanatory-reach over adaptive fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), states the four-part negative test.
- [`kb/notes/COLLECTION.md`](../../notes/COLLECTION.md) makes the property the theoretical collection's quality goal. [`cp-skill-write`](../../instructions/cp-skill-write/SKILL.md) requires the authoring agent to read that contract before writing, so the consumer is the authoring agent, the channel is skill-directed prompt assembly, and the force is instruction and candidate-shaping.
- The [explanatory-reach gate](../../instructions/review-gates/semantic/explanatory-reach.md) is consumed by a review worker through the assay prompt with audit-trigger force. The [review-gate type](../../types/review-gate.md) explicitly denies it rejection authority: WARN/FAIL creates disposition work; it does not itself block commit or merge.
- The [recurring explanatory-reach review](../../tasks/recurring/review-explanatory-reach.md) applies all four tests through a human–agent review procedure.

The gate's `requires_trait: title-as-claim` is the discriminating scope case. Consumer, channel, and force stay the same whether the gate applies to every note or only that cohort, while the behavioral reach changes. A complete authority-path inventory therefore needs the applicability target/trigger in addition to consumer, channel, and force.

### Addressability and revision

The repository demonstrates substantive revision. The anchor changed from a harder adaptive/explanatory binary to a polarity, added rival-practice pressure, and added observed fit; the collection contract and recurring task carry the four-part test. [ADR 055](../../reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md) then renamed the technical property across registered surfaces, and [reach-assessment](../../notes/definitions/reach-assessment.md) reused the four-part test in a later theoretical application.

That same history exposes the missing edge. The current semantic gate tests mechanism, premise variation, falsifiability, and ad-hoc accommodation, but does not test whether observed fit disciplines the explanation. The anchor's `Derived into` footer identifies the collection contract and recurring task, but no machine-readable dependency makes an anchor edit stale those derivatives. Review freshness hashes the note and criterion text; [review architecture](../../reference/review-architecture.md) states that prompt scaffolding and prompt-assembly code also sit outside that hash. A judgment-changing scaffolding edit requires a deliberate corpus rerun rather than automatic invalidation.

The operative assay path is not merely possible. A read-only query of the current Commonplace store found 269 completed pairs for `semantic/explanatory-reach`, from 2026-04-06 through 2026-08-04, across multiple model partitions. That establishes routine invocation of the gate. It does not establish that reviewers applied the anchor's full revised four-part test, because the criterion text supplied to them still omits observed fit; nor does it validate every recorded model identity.

The target is therefore semantically locatable and historically revisable, but installing one conceptual successor across every authority-bearing derivative is a revision-closure task reconstructed by search and author discipline.

### Standing

- Identify, inspect, criticize, revise: **demonstrated** across theory, contract, task, and gate.
- Operative installation: **demonstrated** for the contract and gate surfaces; gate execution is **routinely exercised** in the review store.
- Later dependence: **demonstrated** by the reach-assessment definition; **unestablished** for a review applying all four revised tests.
- Continuity: **demonstrated** by later renaming and reuse, but not mechanically closed across derivatives.
- Strongest missing edge: dependency and freshness coverage over the full evaluator contract.

## Case 3 — The tag-README validator is the strongest end-to-end operative trace

### Operative path

The `complete` and `covered_by` marks are declared in the [tag-README type spec](../../types/tag-readme.md), structurally admitted by its [schema](../../types/tag-readme.schema.yaml), and enforced by the path-dispatched rule in [`validation.py`](../../../src/commonplace/lib/validation.py). The validator is the consumer, validation is the channel, and the force is enforcement: a false mark produces a failure. A second path sends the same mark to the connect agent with routing force, allowing it to skip a by-tag search when `complete: true` is valid.

The applicability scope is again load-bearing: the rule applies to artifacts whose canonical type identity is `kb/types/tag-readme.md`, and validation of an ordinary tagged note also pulls in affected marked heads. Without that type/cohort and trigger relation, consumer–channel–force would not say when the rule acts.

### Addressability and revision

The [observed causal-connection trace](../../reference/tag-readme-trace-observed-causal-connection.md) records the route from strain through ADR 026 into spec, schema, validator, renderer, and tests. The implementation is localized enough to inspect and criticize by semantic rule, dispatch key, constants, and executable cases; [`test_validation_tag_readme.py`](../../../tests/commonplace/lib/test_validation_tag_readme.py) pins missing-member, uncovered-note, and fan-out behavior.

Operative use is demonstrated twice. The installed `covered_by` rule found a block-style-YAML member the natural-language search recipe had missed, forcing a procedure correction. A later validator change made validating an ordinary tagged note also validate the affected marked tag-README, extending the installed machinery rather than freezing it after first adoption. The successor rule, its tests, and its consuming path all remain addressable.

The path is still user-invoked: `commonplace-validate` acts when a writer, skill, or operator runs it. That is a trigger property, not inertness. The weaker edge is admission: the trace can reconstruct maintainer review and merge, but the repository does not bind that approval to the exact installed code version.

### Standing

- Identify, inspect, criticize, revise: **demonstrated**.
- Operative installation and later dependence: **demonstrated**.
- Continuity after successor installation: **demonstrated** by later extension of validation reach.
- Warrant: mixed—the objective is explicit and code checks consistency, while the choice of this design remains human judgment.
- Strongest missing edge: content-bound admission provenance, shared with Case 6.

## Case 4 — The revision lifecycle is reusable and revisable, but does not decide adoption in general

### Operative path

Commonplace retains a general development route across workshops, [proposals](../../reference/proposals/README.md), [ADRs](../../reference/types/adr.md), contracts, instructions, configuration, validators, and code. The lifecycle separates exploration, an undecided design object, an implemented decision record, and operative installation. Agents and maintainers consume the contracts and procedures through routing, authoring, review, and validation channels with instruction, selection, and enforcement force.

The path is not one mandatory pipeline. [Design rationale management](../../reference/design-rationale-management.md) explicitly describes a distributed practice, not an enforced traceability protocol; some deterministic fixes can go directly to code, and no transition contract covers every stage.

### Addressability, reuse, and continuity

[ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) revised the proposal lifecycle itself. It required later ADRs to retain considered alternatives, changed proposal retirement, updated authoring contracts, and installed deterministic archive-boundary validation. [ADR 057](../../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) then used the new alternatives requirement while creating the article lifecycle. That successor was challenged again: [ADR 063](../../reference/adr/063-all-article-drafts-circulate-behind-a-banner.md) removed its excluded-draft placement and updated the live [article collection contract](../../articles/COLLECTION.md) and [publication procedure](../../instructions/publish-an-article.md).

This sequence demonstrates more than editable files. A changed revision method shaped a later architectural decision, and that installed successor remained available for criticism and another operative revision. The method's artifacts, rationale, alternatives, and current installation surfaces are inspectable.

The boundary appears at admission. The proposal contract says a converged choice that ships becomes an ADR; the ADR type says ADRs record implemented decisions; publication requires explicit user approval naming the target state. These are useful local conditions, but no repository-wide artifact says who may adopt a generic change, how a person becomes a designated maintainer, or which review/approval event binds the exact installed version. Git is expected for review and reconstruction, while [storage architecture](../../reference/storage-architecture.md) explicitly gives commits, branches, and merges no framework-wide semantic meaning.

### Standing

- Identify, inspect, criticize, revise: **demonstrated**.
- Operative installation and later dependence: **demonstrated** in the 056 → 057 → 063 sequence.
- Continuity: **demonstrated** for the article-lifecycle redesign class.
- General admission: **unestablished**; path-specific approval clauses do not compose into a repository-wide rule.
- Strongest missing edge: the generic admission relation isolated in Case 6.

## Case 5 — Model bindings are requested and recorded, not end-to-end bound

### Operative path

Model choice appears in two repository-defined paths. Promoted skills declare bindings such as `model: opus` in their canonical `SKILL.md` files. Review execution separately declares `claude-sonnet-5` as the cheapest adequate default in [Run review batches](../../instructions/run-review-batches.md), maps concrete model names into freshness partitions in [`review_model.py`](../../../src/commonplace/review/review_model.py), and records optional runner/model/effort provenance at finalization.

The intended consumer is the harness or worker dispatcher, the channel is skill loading or delegated review launch, and the force is selection/configuration influence. Applicability includes the skill or review pair, selected model partition, runner, and execution episode; omitting that scope would conflate distinct bindings.

### Addressability and the realized path

The requested binding, alias registry, selection policy, and stored claim are easy to inspect and revise. They do not determine which provider model actually executes. [The retained model-selection regression](../../reference/harness-sub-agent-model-selection-regression.md) records 268 review results created under a `luna` partition even though retained child traces showed Sol execution; the parent finalized them with claimed Luna provenance. That incident remains discriminating even if a later harness restores per-worker selection: repository requests and parent-supplied labels are not trusted execution evidence.

The current procedure improves honesty by requiring the worker to report its exact model when exposed and by refusing a reported partition mismatch. But the parent cannot observe the model directly, provenance is optional, and finalization validates the supplied string rather than the execution event. A repository edit can therefore revise the *requested* successor while operative entry remains conditional on a runner surface and evidence outside that artifact.

Provider weights and inference infrastructure remain outside the declared frame. The gap here is narrower: the inside-the-path request is not bound to a trustworthy observation that the requested model became the consumer.

### Standing

- Identify, inspect, criticize, revise requested binding: **demonstrated**.
- Select or modify provider weights: **out of scope**.
- Operative installation of a requested successor: **supported only when the harness honors the request**; not established by repository state.
- Failure of request/provenance to match execution: **demonstrated**.
- Continuity: runtime-dependent and therefore **unestablished** from repository evidence alone.
- Strongest missing edge: a trusted requested-to-realized binding and attestation.

## Case 6 — Generic maintainer admission is named but not represented

### The candidate counterexample

The declared frame includes “designated maintainers acting in their established improvement roles.” Many retained traces then say a maintainer judged, adopted, approved, committed, or merged a change. Path-specific instructions can demand explicit user approval—for example, [Publish an article](../../instructions/publish-an-article.md) requires approval naming the target lifecycle state. The [retained operative-path test](../../notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md) also correctly requires an identifiable admission condition.

For a generic Commonplace system change, however, no canonical repository artifact records:

- who is a designated maintainer or how designation occurs;
- the scope and duration of that person's grant;
- which candidate classes require which approval;
- the decision event that makes the candidate incumbent; or
- a binding from that decision to the exact content/version later consumed.

`AGENTS.md` gives agents Git conduct rules, but those rules are permissions for repository work, not a maintainer registry or adoption protocol. Git history can reconstruct that a merge occurred, while the storage contract deliberately denies merge a uniform semantic role. Review gates also deny themselves admission force: findings route to downstream disposition, and commit or merge retains whatever the operator chooses.

An adversarial second search found no tracked `CODEOWNERS`, `OWNERS`, `MAINTAINERS`, branch-policy, or ruleset artifact that supplies the missing designation or grant. An external hosting rule could govern a particular remote, but it would not be a represented repository artifact and cannot repair the repository-defined completeness claim without being brought into the declared path.

### Why consumer, channel, and force do not close it

After the fact, the path can be described: a maintainer consumes a candidate, diff, and review through conversation/review/Git channels with selection or admission force; later agents and tools consume the installed artifact with its own force. That description does not identify which actor was authorized to exercise admission, for what scope, or whether the installed bytes are the version approved.

The counterexample is observable without inventing an attacker. Two identical final worktrees—one produced after the required user decision, one produced by a direct unauthorized edit—receive identical treatment from the validator, review selector, skill loader, and later agent. The repository contains no authorization state those consumers can inspect to distinguish them. [A consumption channel delivers force without the history that earned it](../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) names exactly this boundary: provenance, review, and consumption enforcement must bind authorization to content, version, role, and use if legitimacy is meant to survive into the live path.

This does not make ordinary maintenance impossible. The included human can decide and the files become operative. It means the working claim cannot say the repository makes the *revision-authority relation itself* completely addressable. An agent asked to criticize or revise that grant must first invent a representation for it or rely on live user/harness roles outside the repository record.

### Standing

- Identify and inspect installed artifacts: **demonstrated elsewhere**.
- Identify the generic maintainer role name: **supported**.
- Identify designation, grant scope, and content-bound admission condition: **unestablished**.
- Selectively revise the generic grant relation: **unestablished**, because no canonical target represents it.
- Install and re-use changes through human action: **demonstrated**, but not as a retained admission protocol.
- Verdict: **strongest counterexample to complete addressability of the revision authority included in the working claim**.

## Hostile search: why the other gaps are not the counterexample

- **Uncalibrated semantic gates** are a warrant gap. Their criteria, consumer paths, and limited audit-trigger force are represented and revisable; weak validity does not make them unaddressable.
- **Review prompt scaffolding outside the freshness hash** is a dependency and invalidation gap. The code and compensating rerun rule are explicit, so the relation is inspectable even though it is not mechanically tracked.
- **User-invoked validation** is not inert merely because it is not always-on. The trigger and force are named, and later invocations demonstrably enforce the rule.
- **Provider weights and inference infrastructure** are declared outside the frame. Their opacity cannot refute a claim scoped to repository-defined organization.
- **Requested model bindings** are a serious operative-installation gap, but the requested artifact remains addressable. The generic maintainer grant is stronger because the repository-defined role is inside the frame while the designation and admission relation lack a canonical target.
- **Tacit judgment about whether a successor is better** is excluded from complete addressability as unarticulated human expertise. The counterexample is not the contents of judgment; it is the repository-declared allocation and admission relation that says whose judgment can install what.

## Evidence-driven decomposition result

Consumer, channel, and force remain a useful description of one live use. They are not a sufficient key for this audit.

| Concrete case | What consumer–channel–force fails to distinguish | Needed addition or relation | Conceptual home | Effect on the claim |
|---|---|---|---|---|
| Explanatory-reach gate applies only to `title-as-claim`; tag validation acts only for a type/cohort and trigger | Same consumer, channel, and force can reach different targets under different conditions | **Applicability scope**: target cohort/aspect plus activation trigger | Candidate fourth field of behavioral authority, or an immediately adjacent required qualifier | Complete coverage must range over scoped uses, not artifact names |
| Authorized and unauthorized edits produce the same live bytes | Which actor/decision was entitled to confer force on this content version and use | Source-state designation, grant scope, admission condition, content/version binding | Revision governance and authorization, not behavioral authority itself | Complete addressability of revision machinery fails until this relation is represented |
| Requested Luna/Opus binding differs from the executing model | Declared selection influence versus realized consumer | Requested-to-realized binding plus trustworthy execution evidence | Operativity and runtime realization | A revised request cannot count as installed merely because the file changed |
| Anchor theory changes while a derived gate remains semantically older | Which derivative and interface obligations must change or be revalidated together | Dependency/revision-closure record | Lineage, freshness, and revision closure | Selective revision is supported, but complete installation across authority derivatives remains manual |

The conservative theory change is therefore:

1. Retain consumer, channel, and force as the stable local-link decomposition.
2. Treat **applicability scope** as a provisional fourth behavioral-authority field because it changes who or what receives force without changing the other three fields.
3. Do not overload behavioral authority with legitimacy, execution truth, or change propagation. Require adjacent records for authorization/admission, realization/operativity, and dependency/revision closure when the stronger general-revision claim is tested.

This split matters. A path can exercise real behavioral force without legitimate admission, can carry a legitimate request that is not realized, and can revise one addressable artifact while leaving a dependent authority surface stale.
