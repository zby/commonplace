---
description: "Classifies the shipped Commonplace system against the five reflective-system obligations and, on the same trace, as a human-inclusive self-improving system"
type: kb/types/note.md
traits: [has-implementation]
tags: [foundations, computational-model, self-improving-systems]
---

# Commonplace as a reflective system

Commonplace is a reflective system: it contains a causally connected representation of selected aspects of itself, available to processes inside its declared boundary, and operations mediated through that representation change its subsequent behavior. It is also a human-inclusive, reflective [self-improving system](../notes/definitions/self-improving-system.md) — the stronger and more interesting claim, since reflection alone is cheap.

This is a case classification, not a new theory. It discharges the five obligations [reflective system](../notes/definitions/reflective-system.md) requires, then reads the same trace against [self-improving system](../notes/definitions/self-improving-system.md), which asks for two further things: operative change to the system's own organization, and responsiveness to evidence bearing on an improvement objective it could have failed. Both classifications rest on one observed repository trace, not on architectural possibility. Reflection here is aspect-bound and partial; the negative conclusions at the end are part of the claim, not hedges around it.

## The frame

The system is socio-technical. Four of the five obligations are structural and are discharged by the table below; the fifth, causal connection, needs the observed trace in the next section and carries the weight of the classification.

| Obligation | Discharged by |
|---|---|
| **Declared boundary** | Inside: the repository and its retained artifacts; the software that validates, selects, renders, or consumes them (`src/commonplace/`, the `commonplace-*` commands, the review store); agents operating under the repository's instructions and skills; the established human authoring, review, and merge roles. Outside: the model provider and its weights, the fixed inference machinery, hosting and CI, and unaffiliated readers — none of which Commonplace can inspect or modify. |
| **Represented aspects** | Artifact types and contracts (`kb/types/`), collection routing (`COLLECTION.md`), repository organization and navigation, maintenance/review/validation procedures, behavioral-authority paths, and design rationale (`kb/reference/adr/`). Unrepresented or only partial: the model's runtime behavior, any note's effectiveness at its job, the search process by which problems get noticed, and most ordinary knowledge content. |
| **Self-representation** | The artifacts that state how the system's own artifacts must be shaped — type specs, collection contracts, instructions and skills, ADRs, schemas, review criteria. `kb/types/tag-readme.md` qualifies, because the system consumes it as the rule for that type; a note about a general phenomenon does not. |
| **Internal reflective processes** | Human maintainers who author and approve contract changes; editing and review agents under the repository's instructions; the validators and review commands that *load the self-representation as their rule*; the build-time renderer and routing surfaces that make represented constraints operative. Human judgment identifies how part of the process is implemented, per the definition's allowance for established roles — not a limit on the classification. |
| **Causal connection** | The `tag-readme` trace below, observed end to end and in both directions. |

## Causal connection: an observed trace

Causal connection is the decisive obligation, and it must be shown as an observed instance rather than argued from architecture. The `tag-readme` type (ADR 026) supplies one, end to end.

**The adaptation signal.** An observed strain, not a logged failure: the `index` type was doing two jobs — complete enumeration and introduction to a tag — and the `learning-theory` head had reached 18.8 KB / 55 entries, a size at which completeness could no longer be declared. The strain was interpreted through a claim the KB already held, that [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md): a marked-but-incomplete head tells an exhaustive consumer to stop looking while members are missing.

**Revision of the self-representation.** `91130f82` added [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), splitting the type and specifying `complete` as an *enforced* membership mark. The ADR is explicit that the unenforced prose version of the claim must never be written — a stale trusted cache is the failure it exists to prevent.

**Coordinated change across representational forms.** `94769805` carried the same decision into four forms in one commit: the prose spec (`kb/types/tag-readme.md`), the JSON schema (`kb/types/tag-readme.schema.yaml`), the validator (`src/commonplace/lib/validation.py`), and the build-time renderer. The mapping between the prose and the code is not incidental — the validator dispatches on the spec's own path, so the specification file *is* the enforcement key:

```python
@type_rule("kb/types/tag-readme.md")
def validate_tag_readme(results, parsed, *, run) -> None:
```

The ADR's numbers appear as constants (`TAG_README_SOFT_BYTES = 8 * 1024`, `TAG_README_HARD_BYTES = 16 * 1024`, `TAG_README_MAX_FANOUT = 7`), and the failure message routes the reader back to the maintenance instruction.

**Evaluation.** Tests landed in the same commit, pinning the contract: `test_complete_mark_fails_on_missing_member`, `test_covered_by_fails_on_uncovered_note`, `test_weight_gates_warn_and_fail`. ADR 026 mentions a rename-list review gate for the migration, but no review-system artifact recording that run was located — so the evaluation evidenced here is the test suite plus the maintainer's review and merge, not a logged review-gate run.

**Retention.** `9976a081` migrated fifteen tag indexes to the new type. The marks are live: `kb/notes/tags-README.md`, `discovery-README.md`, `distillation-README.md`, and `artifact-analysis-README.md` carry `complete: true` today.

**Later behavior change traceable to the modification.** Three consumers changed, and this is where [behavioral authority](../notes/definitions/behavioral-authority.md) names the paths precisely rather than saying the artifact "influenced" the system:

| Consumer | Channel | Force |
|---|---|---|
| `commonplace-validate-notes` | validation | enforcement — rejects what it used to accept |
| `cp-skill-connect` agent | instruction | routing — skips a search it used to run |
| Maintainer / navigation recipe | advice | correction of the documented procedure |

The validator change is the sharpest. `dab163c6` made validating *one ordinary note* also pull in every marked tag-README carrying that note's tags. The test `test_note_target_also_validates_marked_tag_readmes` pins it: validating `tagged-note.md` now exits 1 because of a violation in a *different* file, and only the *marked* README is pulled in. In the same commit, the live KB had to be edited to satisfy the new check — `artifact-analysis-README.md` gained entries it would not otherwise have gained. The represented constraint reached back and forced a change in the represented system.

The agent-routing change is `kb/instructions/cp-skill-connect/SKILL.md:58`: "If a tag-README declares `complete: true`, it links every note carrying that tag — **skip the by-tag rg for that tag**." An agent now performs fewer tool calls because of what the self-representation asserts.

The third runs in the opposite direction, from code back to prose. In `ba1a7d9f`, adopting `covered_by` on the `learning-theory` head, the new symbolic check **caught a member the prose `rg` recipe had missed** — a note using block-style YAML tags, invisible to the documented pattern. The prose recipe in `kb/reference/navigation.md` was then corrected to record the blind spot. Execution of the symbolic artifact produced evidence that revised the prose, and the loop closed back into theory when the workshop was dissolved into a retained note (`46f106c5`).

Both directions of causal connection are therefore observed: a change in the system's organization forced revision of its self-representation, and a change made through the self-representation altered what the system subsequently required, rejected, and searched.

## The same trace as a self-improving system

Reflection is the machinery; it is not yet the interesting claim. The trace above also discharges [self-improving system](../notes/definitions/self-improving-system.md), and it is worth rereading in those terms, since the definition asks for two things the reflective obligations do not: a change to the system's own organization, and evidence-responsiveness toward an objective. Commonplace's improvement pathway takes the [proposal-selection](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) form — candidates are drafted, reviewed with a real possibility of rejection, and selectively merged — so the subtype's decomposition is the right reading grid.

| Requirement | Discharged by |
|---|---|
| **Change to the system itself** | The change ran on `kb/types/tag-readme.md` — a self-representing artifact, not ordinary content. |
| **Search** | Human. A maintainer noticed the `index` type was doing two jobs and that the `learning-theory` head had outgrown its completeness claim. |
| **Improvement objective** | The criterion under which the change could have failed: a marked head must not lie to an exhaustive consumer, per [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md). ADR 026 makes it enforceable — `complete` is a mark the validator can falsify. |
| **Evaluation** | Mixed. Tests and the validator are mechanical; the judgment that the type split was the right shape was the maintainer's. |
| **Operative retention** | The three consumers in the table above: enforcement, routing, advice. |

The improvement objective is the requirement the reflective classification never had to state, and stating it is what makes the loop improvement-*directed* rather than merely change-directed. Note what it does not establish: the validator's acceptance says the marks are consistent, not that the type split made the KB better. That remains an improvement *claim*.

**Autonomy profile.** Search: human. Evaluation: split — mechanical where the constraint is structural, human where it is judgment-heavy. Retention: mechanical once merged, with the merge itself human. So Commonplace is a **human-inclusive, reflective self-improving system**, not an autonomous one: the loop closes, and it closes through the self-representation. Humans remain where no adequate automatable oracle reaches, [since warranted autonomy is bounded by oracle reach](../notes/warranted-autonomy-is-bounded-by-oracle-reach.md).

## Coverage across representational forms: partially demonstrated

Basic reflection does not require the stronger claim that Commonplace's reflective reach *covers* every behavior-bearing representation and the mappings between them. Since [reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md), the assessment goes form by form, and the trace above shows real but incomplete coverage:

- **Prose-mediated reasoning revising formal artifacts** — demonstrated by the trace above: ADR 026's prose decision became a schema and a validator.
- **Symbolic execution producing evidence that revises prose** — demonstrated once in the trace above: the `covered_by` check found what the documented `rg` recipe missed, and the recipe was corrected.
- **Mappings represented and modifiable** — partial. The type-spec-to-validator mapping is unusually tight (the spec path is the dispatch key), so the two are hard to drift silently; most other prose-to-code relationships in the repository have no such binding.
- **Lineage and staleness across the forms** — largely unrepresented. Commonplace does not guarantee an end-to-end trace from a claim to the code that implements it; see [design rationale management](./design-rationale-management.md). Freshness tracking exists for review pairs, not for theory-to-implementation lineage.
- **The distributed-parametric form — selection-grade only.** The model weights sit outside the boundary: nothing inside can inspect or edit them. The one represented lever is selection among sealed alternatives — skill frontmatter pins a model (`model: opus` in `kb/instructions/cp-skill-write/SKILL.md`, `model: sonnet` on lighter skills), and review baselines partition by model. What is modifiable is the *binding*, not the component: editing that prose changes which parametric substrate runs, and nothing finer — selection depth over the parametric form, the crudest lever that is still useful.

In summary: reflective coverage reaches modification depth on the prose and symbolic forms — demonstrated on the type-system spine, architecturally possible elsewhere, not systematically achieved — and selection depth on the parametric form.

## What this classification does not claim

- Commonplace does not represent every aspect of itself; reflection is aspect-bound.
- Not all self-modification is automated. Search — noticing the problem, choosing the target — remains substantially human, and the system's methodology does not govern it.
- Nothing here establishes that the accepted changes were improvements; the autonomy profile above says what was checked and by what, and the improvement claim stops there.
- Commonplace cannot modify the model weights, the inference machinery, or the other dependencies outside its boundary, and rationale lineage across the forms is not mechanically guaranteed.
- Reflection does not entail [closure under recommendations](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). Commonplace is reflective whether or not its methodology governs the meta-decisions its own extension raises; those are separate properties, assessed separately.
- The bare classification is not the informative part: under a human-inclusive boundary nearly every maintained system is reflective, since [human-inclusive boundaries make reflection cheap](../notes/human-inclusive-boundaries-make-reflection-cheap.md). What the trace establishes is not that Commonplace qualifies but where it sits — which is what the autonomy profile above records.

---

Relevant Notes:

- [Reflective system](../notes/definitions/reflective-system.md) — rationale: supplies the five obligations this classification discharges
- [Self-improving system](../notes/definitions/self-improving-system.md) — rationale: supplies the loop, objective, and autonomy profile the same trace is read against a second time
- [Behavioral authority](../notes/definitions/behavioral-authority.md) — defined-in: names the consumer, channel, and force in the observed trace
- [Reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md) — rationale: the graded coverage criterion this system meets unevenly across its forms
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rationale: the change-loop decomposition the trace is read against
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — rationale: the separate, stronger self-extension property
- [ADR 026: tag-readme type with completeness and coverage marks](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidence: the decision at the center of the observed trace
- [Design rationale management in Commonplace](./design-rationale-management.md) — part-of: why theory-to-implementation lineage is not enforced end to end
- [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the retained claim through which the adaptation signal was interpreted
