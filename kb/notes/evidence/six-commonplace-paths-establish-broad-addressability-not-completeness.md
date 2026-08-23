---
description: "A six-path Commonplace audit establishes broad path-relative addressability without establishing completeness, while exposing separate admission and model-realization gaps in the broader revision affordance"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-comparison, has-implementation]
tags: [artifact-analysis, self-improving-systems]
---

# Six Commonplace paths establish broad addressability, not completeness

A 2026-08-04 audit of six difficult Commonplace authority paths established broad, path-relative addressability. The canonical artifacts carrying goals, collection criteria, review criteria, revision procedures, validator rules, and requested model bindings can be identified, inspected, criticized, and selectively revised. The repository also records operative reuse of natural-language and symbolic revision machinery. Because the six paths are representative rather than exhaustive, the audit does not establish complete coverage. Separately, it found that the repository does not represent the generic grant through which a designated maintainer is authorized to admit a change, and that a requested model binding is not reliably bound to the model that executes. The first gap limits the governed revision affordance; the second limits operative realization.

The audit uses [Commonplace's declared frame](../../reference/commonplace-declared-frame.md): the repository, its operative artifacts, consuming software and agents, and designated maintainers in their established roles are inside; provider weights, inference infrastructure, and hosting are outside. Model-binding requests and policies remain in scope because repository artifacts represent them and the review system partitions freshness by requested model; the provider model and its weights do not.

Evidence strength is calibrated per path. **Declared** means prose states the route. **Supported** means current artifacts and wiring provide it without a retained later-use trace. **Demonstrated** means a trace or executable check records its exercise. **Routinely exercised** requires repeated retained use. **Unestablished** means an edge is absent, reconstructed, or contradicted by retained evidence. Addressability—identify, inspect, state, criticize, and selectively revise or retire—is assessed separately from operative installation, warrant, and continuity.

## The six paths

| Path | Authority path and applicability | Addressability | Installation and continuity | Strongest missing edge |
|---|---|---|---|---|
| Global KB goals | Agent; always-loaded context; instruction and inclusion selection across repository work | Artifact explicit; inspection and revision supported | Next-session loading supported; later dependence unestablished | No retained generic admission or warrant rule for changing the objective |
| Explanatory-reach criterion | Author or reviewer; collection contract and assay; instruction and audit trigger for scoped note cohorts | Distributed target identified and historically revised | Gate routinely exercised; later review dependence on the full revised criterion unestablished | Derived criteria and prompt scaffolding sit outside one freshness/dependency closure |
| Tag-README validator | Validator and connect agent; validation and routing for the tag-README type, affected heads, and explicit invocations | Spec, schema, code, tests, and consumer paths explicit | Operative revision, later use, and a later extension demonstrated | Human admission of the installed code version is reconstructed |
| Revision lifecycle | Agent and maintainer; routing, review, instruction, and validation over proposals, ADRs, contracts, and installation surfaces | Method and artifacts explicit; revision of the method demonstrated | ADR 056 → ADR 057 → ADR 063 demonstrates reuse and another challenge | No repository-wide admission condition |
| Model binding | Harness, worker, and finalizer; skill or review configuration for a selected execution episode | Requested binding and partition identity explicit | Realized binding is runtime-contingent; false provenance is demonstrated | No trusted requested-to-realized binding or execution attestation |
| Maintainer admission | Maintainer consumes a candidate or diff through conversation, review, and Git with influence over selection or admission | Candidate and role name inspectable; designation and grant relation unestablished | Files become operative, but authorization is not bound to the installed version | Who is designated, grant scope, generic admission condition, and approval-to-content binding |

The table's unit is a scoped authority path, not a file. The same artifact can have several consumers and forces, and the same consumer–channel–force triple can apply to different cohorts or triggers.

## Global goals are explicit but lightly governed

The operative objective is the `## KB Goals and Scope` section of [`AGENTS.md`](../../../AGENTS.md). [Control-plane goals](../../reference/control-plane-goals.md) states that every agent invocation receives it in always-loaded context, while [the goals note](../kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) explains its role in inclusion decisions. The artifact and its repository-wide applicability are inspectable and editable. A successor would enter the live path when later sessions load it, so another revision is structurally supported.

The audit found no retained episode showing a changed top-level goal governing a later inclusion decision, nor a generic condition under which one proposed objective displaces another. That is an admission and warrant gap, not a failure to address the objective artifact.

## Explanatory-reach is distributed and routinely invoked

Explanatory-reach acts through an anchor theory, the [notes collection contract](../COLLECTION.md), the [semantic gate](../../instructions/review-gates/semantic/explanatory-reach.md), and the [recurring review](../../tasks/recurring/review-explanatory-reach.md). The gate's `requires_trait: title-as-claim` is a discriminating applicability case: consumer, review channel, and audit-trigger force remain the same whether the gate applies to every note or only that cohort.

The criterion has been revised in substance, propagated into several consumers, renamed through [ADR 055](../../reference/adr/055-explanatory-reach-replaces-bare-reach-as-the-technical-term.md), and reused by [reach assessment](../definitions/reach-assessment.md). Yet the live gate still omits the anchor's observed-fit test, and no dependency record makes all derived criteria or prompt scaffolding stale when the anchor changes. A read-only query of the Commonplace store on 2026-08-04 found 269 completed `semantic/explanatory-reach` pairs from 2026-04-06 through 2026-08-04:

```sql
SELECT COUNT(*), MIN(completed_at), MAX(completed_at)
FROM review_pairs
WHERE completed_at IS NOT NULL
  AND criterion_path = 'kb/instructions/review-gates/semantic/explanatory-reach.md';
```

This establishes routine gate invocation, not use of the full revised criterion or correctness of every recorded model identity.

## Tag-README validation supplies the strongest end-to-end trace

The `complete` and `covered_by` marks are declared in the [tag-README type](../../types/tag-readme.md), admitted by its schema, enforced in [`validation.py`](../../../src/commonplace/lib/validation.py), and pinned by executable tests. Applicability includes the canonical tag-README type, affected marked heads, and the explicit validation trigger; consumer–channel–force alone would not say when the rule acts.

The [observed trace](./tag-readme-trace-observed-causal-connection.md) records the path from operational strain through ADR 026 into specification, schema, validation, rendering, and tests. The installed `covered_by` rule later found a member missed by the natural-language search recipe, causing that procedure to change. Validation was then extended so checking an ordinary tagged note also checks affected marked heads. This demonstrates identification, revision, operative installation, later dependence, and continuity for one redesign class. The remaining weak edge is generic admission provenance: the repository can reconstruct review and merge, but does not bind authorization to the installed code version.

## The revision lifecycle is reusable and revisable

Commonplace retains a development route across workshops, proposals, ADRs, contracts, instructions, validators, and code. [ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) revised that lifecycle, required later ADRs to retain considered alternatives, and installed archive-boundary validation. [ADR 057](../../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) then used the new alternatives requirement while creating the article lifecycle. [ADR 063](../../reference/adr/063-all-article-drafts-circulate-behind-a-banner.md) challenged that successor and changed the live article contract and publication procedure again.

This sequence shows a revised method shaping a later architectural decision and remaining open to another operative revision. It does not supply a universal pipeline or decide who may adopt an arbitrary system change. Path-specific approval requirements do not compose into a repository-wide admission rule, and [storage architecture](../../reference/storage-architecture.md) deliberately gives commits and merges no uniform semantic meaning.

## Requested model bindings are not realized bindings

Promoted skills request models in metadata, while review execution declares defaults, maps model names into freshness partitions, and records optional provenance. These requests, aliases, partitions, and policies are addressable. Their applicability includes the skill or review pair, runner, partition, and execution episode.

They do not prove which model executed. The [model-selection regression](../../reference/harness-sub-agent-model-selection-regression.md) records 268 review results finalized under a Luna partition even though retained child traces showed Sol execution. Current procedures can reject a worker-reported mismatch, but the parent cannot always observe the model directly and finalization validates supplied provenance rather than the execution event. The requested artifact is addressable; its operative realization remains runtime-dependent.

## Generic maintainer admission is the strongest gap in the broader affordance

The declared frame includes designated maintainers, and several paths require maintainer or user approval. No canonical repository artifact records who is designated, the scope or duration of the grant, which changes require which approval, the generic event that makes a candidate incumbent, or a binding from that event to the installed content version. No tracked `CODEOWNERS`, `OWNERS`, `MAINTAINERS`, branch-policy, or ruleset artifact supplied the missing relation at the audit date.

Two identical final worktrees—one produced after the required decision and another by an unauthorized edit—receive identical treatment from validators, loaders, and later agents. The live artifact therefore acquires behavioral force without carrying the authorization history that earned it, as [a consumption channel delivers force without the history that earned it](../a-consumption-channel-delivers-force-without-the-history-that.md). This does not make installed artifacts inert or unreadable, nor does it by itself identify an unaddressable consumer–channel–force path. It means the repository cannot identify and selectively revise the generic admission grant as a represented object, so the stronger governed revision affordance remains incomplete even if every existing behavioral-authority path proved addressable.

This gap is stronger than the others for the broader affordance. An uncalibrated gate has weak warrant but remains addressable. Prompt scaffolding outside a freshness hash is a dependency gap over inspectable code. User-invoked validation has an explicit trigger. Provider weights are outside the declared frame. Requested model bindings have an operative-realization gap, but their requested configuration is represented.

## What the audit adds to the decomposition

Consumer, channel, and force describe a live local use but do not always identify which use is being assessed. The explanatory-reach and tag-validator cases require **applicability**: the target cohort, aspect, or operation that receives the force and the activation condition under which it acts. Whether applicability becomes a fourth behavioral-authority component or a required qualifier remains open in the [behavioral-authority decomposition proposal](../../reference/proposals/revise-behavioral-authority-decomposition.md), whose prior-art survey precedes any migration of the established record.

Three other needs remain adjacent rather than being folded into behavioral authority:

- **Authorization and admission** ask whether an actor or decision was entitled to confer force on this content and use.
- **Realization and operativity** ask whether a request reached the actual consumer and affected later behavior.
- **Dependency and revision closure** ask which derivatives and interfaces must change or be revalidated with the revised artifact.

A path can exercise force without legitimate admission, carry a legitimate request that is not realized, or revise one addressable artifact while leaving dependent authority surfaces stale. Keeping these questions separate prevents a broad addressability finding from being mistaken for warrant, installation, continuity, or compounding.

## Scope

- The six paths were chosen to expose hard cases, not sampled to estimate repository-wide prevalence. Their coverage does not prove that the unexamined remainder is empty.
- Counts and absence claims are snapshot-bound to 2026-08-04. Later review runs, ownership records, or runtime attestations can change the relevant cells.
- Complete addressability remains a useful coverage target. The evidence establishes broad addressability and several operative, repeatable paths; complete coverage remains open.

---

Relevant Notes:

- [Behavioral authority](../definitions/behavioral-authority.md) — defined-in: supplies the consumer, channel, and force record whose applicability boundary the audit exposes
- [Axes of artifact analysis](../axes-of-artifact-analysis.md) — grounds: locates authority alongside substrate, representational form, and lineage
- [A consumption channel delivers force without the history that earned it](../a-consumption-channel-delivers-force-without-the-history-that.md) — grounds: explains why live force does not preserve admission legitimacy
- [A repeatable operative path keeps a redesign class open to revision](../a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — extends: supplies the continuity test exercised by the validator and lifecycle cases
- [Six reported self-improvement paths expose bounded redesign surfaces within supplied methods](./six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) — contrasts: applies the same path-relative discipline to six external systems whose research teams remain outside the reported loops
- [Commonplace as a reflective self-improving system](./commonplace-as-a-reflective-system.md) — see-also: classifies the narrower tag-README episode under the declared human-inclusive frame
- [Revise the behavioral-authority decomposition](../../reference/proposals/revise-behavioral-authority-decomposition.md) — see-also: owns the unresolved choice between applicability as a field or a required qualifier
