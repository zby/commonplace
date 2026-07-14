---
description: "Classifies the shipped Commonplace system against the five reflective-system obligations, with one observed repository trace from type spec through validator to changed behavior"
type: kb/types/note.md
traits: [has-implementation]
tags: [foundations, computational-model, reflective-systems]
---

# Commonplace as a reflective system

Commonplace is a reflective system: it contains a causally connected representation of selected aspects of itself, available to processes inside its declared boundary, and operations mediated through that representation change its subsequent behavior.

This is a case classification, not a new theory. It discharges the five obligations that [reflective system](../notes/definitions/reflective-system.md) requires anyone to state before applying the term, and it rests on one observed repository trace rather than on architectural possibility. Reflection here is aspect-bound and partial; the negative conclusions at the end are part of the claim, not hedges around it.

## 1. The declared boundary

The system is socio-technical. Inside the boundary:

- the Commonplace repository and its retained artifacts;
- the software that validates, selects, renders, or otherwise consumes those artifacts (`src/commonplace/`, the `commonplace-*` commands, the review store);
- agents operating under the repository's instructions and skills;
- the established human authoring, review, and authorization roles — the maintainer who approves and merges.

Outside the boundary: the model provider and its weights, the fixed inference machinery, the hosting and CI infrastructure, and unaffiliated readers of the published site. Commonplace cannot reach these through its self-representation, and nothing below claims that it can.

## 2. Represented aspects

Commonplace does not represent all of itself. The aspects it does represent are:

- artifact types and their contracts (`kb/types/`);
- collection routing and authoring contracts (`COLLECTION.md` files);
- repository organization and navigation;
- maintenance, review, and validation procedures;
- behavioral-authority paths — which artifact governs which consumer;
- design decisions and their rationale (`kb/reference/adr/`).

Unrepresented or only partially represented: the runtime behavior of the model interpreting the instructions, the effectiveness of any given note at its job, the search process by which problems are noticed, and most of the repository's ordinary knowledge content, which is *about* KB methodology but is not a representation of *this* system's organization.

## 3. The self-representation

The self-representing artifacts are those that represent Commonplace as a system, not merely the files it happens to store. They include the type specifications, collection contracts, instructions and skills, ADRs, and the schemas and review criteria that state how the system's own artifacts must be shaped.

Not every repository file qualifies. A note about deploy-time learning is a knowledge artifact about a general phenomenon; `kb/types/tag-readme.md` is a self-representation, because it states what a Commonplace artifact of that type must be and the system consumes it as such.

## 4. Internal reflective processes

Processes inside the boundary that inspect or act through the self-representation:

- human maintainers, who author and approve changes to the contracts;
- editing and review agents operating under the repository's own instructions;
- the validators and review commands, which *load the self-representation as their rule*;
- the build-time renderer and routing surfaces that make represented constraints operative.

The presence of human judgment is not a limitation on the classification. It identifies how part of the reflective process is implemented, per the definition's allowance for established roles inside a socio-technical boundary.

## 5. Causal connection: an observed trace

The decisive obligation is causal connection, and it needs an observed instance rather than an argument from architecture. The `tag-readme` type (ADR 026) supplies one, end to end.

**The adaptation signal.** An observed strain, not a logged failure: the `index` type was doing two jobs — complete enumeration and introduction to a tag — and the `learning-theory` head had reached 18.8 KB / 55 entries, a size at which completeness could no longer be declared. The strain was interpreted through a claim the KB already held, that [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md): a marked-but-incomplete head tells an exhaustive consumer to stop looking while members are missing.

**Revision of the self-representation.** `91130f82` added [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), splitting the type and specifying `complete` as an *enforced* membership mark. The ADR is explicit that the unenforced prose version of the claim must never be written — a stale trusted cache is the failure it exists to prevent.

**Coordinated change across representational forms.** `94769805` carried the same decision into four forms in one commit: the prose spec (`kb/types/tag-readme.md`), the JSON schema (`kb/types/tag-readme.schema.yaml`), the validator (`src/commonplace/lib/validation.py`), and the build-time renderer. The mapping between the prose and the code is not incidental — the validator dispatches on the spec's own path, so the specification file *is* the enforcement key:

```python
@type_rule("kb/types/tag-readme.md")
def validate_tag_readme(results, parsed, *, run) -> None:
```

The ADR's numbers appear as constants (`TAG_README_SOFT_BYTES = 8 * 1024`, `TAG_README_HARD_BYTES = 16 * 1024`, `TAG_README_MAX_FANOUT = 7`), and the failure message routes the reader back to the maintenance instruction.

**Evaluation.** Tests landed in the same commit, pinning the contract: `test_complete_mark_fails_on_missing_member`, `test_covered_by_fails_on_uncovered_note`, `test_weight_gates_warn_and_fail`. Evaluation here was tests plus human review and merge. ADR 026 mentions a rename-list review gate for the migration, but no review-system artifact recording that run was located, so the evaluation evidenced here is the test suite and the maintainer's merge.

**Retention.** `9976a081` migrated fifteen tag indexes to the new type. The marks are live: `kb/notes/tags-README.md`, `discovery-README.md`, `distillation-README.md`, and `artifact-analysis-README.md` carry `complete: true` today.

**Later behavior change traceable to the modification.** Three consumers changed, and this is where [behavioral authority](../notes/definitions/behavioral-authority.md) names the paths precisely rather than saying the artifact "influenced" the system:

| Consumer | Channel | Force |
|---|---|---|
| `commonplace-validate-notes` | validation | enforcement — rejects what it used to accept |
| `cp-skill-connect` agent | instruction | routing — skips a search it used to run |
| Maintainer / navigation recipe | advice | correction of the documented procedure |

The validator change is the sharpest. `dab163c6` made validating *one ordinary note* also pull in every marked tag-README carrying that note's tags. The test `test_note_target_also_validates_marked_tag_readmes` pins it: validating `tagged-note.md` now exits 1 because of a violation in a *different* file, and only the *marked* README is pulled in. In the same commit, the live KB had to be edited to satisfy the new check — `artifact-analysis-README.md` gained entries it would not otherwise have gained. The represented constraint reached back and forced a change in the represented system.

The agent-routing change is `kb/instructions/cp-skill-connect/SKILL.md:58`: "If a tag-README declares `complete: true`, it links every note carrying that tag — **skip the by-tag rg for that tag**." An agent now performs fewer tool calls because of what the self-representation asserts.

The third is the most telling about direction of causation. In `ba1a7d9f`, adopting `covered_by` on the `learning-theory` head, the new symbolic check **caught a member the prose `rg` recipe had missed** — a note using block-style YAML tags, invisible to the documented pattern. The prose recipe in `kb/reference/navigation.md` was then corrected to record the blind spot. Execution of the symbolic artifact produced evidence that revised the prose, and the loop closed back into theory when the workshop was dissolved into a retained note (`46f106c5`).

Both directions of causal connection are therefore observed: a change in the system's organization forced revision of its self-representation, and a change made through the self-representation altered what the system subsequently required, rejected, and searched.

## Coverage across representational forms: partially demonstrated

Basic reflection does not require the stronger claim that Commonplace's reflective reach *covers* every behavior-bearing representation and the mappings between them. Since [reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md), the assessment goes form by form, and the trace above shows real but incomplete coverage:

- **Prose-mediated reasoning revising formal artifacts** — demonstrated. ADR 026's prose decision became a schema and a validator.
- **Symbolic execution producing evidence that revises prose** — demonstrated, once. The `covered_by` check found what the documented `rg` recipe missed, and the recipe was corrected.
- **Mappings represented and modifiable** — partial. The type-spec-to-validator mapping is unusually tight (the spec path is the dispatch key), so it is hard for the two to drift silently. Most other prose-to-code relationships in the repository have no such binding.
- **Lineage and staleness across the forms** — largely unrepresented. Commonplace's rationale surfaces are distributed, and it does not guarantee an end-to-end trace from a claim to the code that implements it; see [design rationale management](./design-rationale-management.md). Freshness tracking exists for review pairs, not for theory-to-implementation lineage.
- **The distributed-parametric form — selection-grade only.** The model weights sit outside the boundary: nothing inside can inspect or edit them. The one represented lever is selection among sealed alternatives — skill frontmatter pins a model (`model: opus` in `kb/instructions/cp-skill-write/SKILL.md`, `model: sonnet` on lighter skills), and review baselines partition by model. Editing that prose changes which parametric substrate runs, and nothing finer. In the [graded-coverage terms](../notes/reflective-coverage-is-graded-across-representational-forms.md) this is real intercession over the parametric form at the crudest useful depth.

The honest summary: reflective coverage reaches modification depth on the prose and symbolic forms — demonstrated on the type-system spine, architecturally possible elsewhere, not systematically achieved — and selection depth on the parametric form.

## What this classification does not claim

- Commonplace does not represent every aspect of itself; reflection is aspect-bound.
- Not all self-modification is automated. Search — noticing the problem, choosing the target — remains substantially human, and the system's methodology does not govern it.
- Not all accepted changes are improvements. Retention under the tests and review that applied does not establish global utility.
- The search and evaluation processes are not complete. The system [requires search, evaluation, and retention](../notes/governed-adaptation-requires-search-evaluation-and-retention.md) to close a change loop, and its evaluation is strong for structural constraints and weak for judgment-heavy ones.
- Rationale lineage is not mechanically guaranteed.
- Commonplace cannot modify the model weights, the inference machinery, or the other dependencies outside its boundary.
- Reflection does not entail [closure under recommendations](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). Commonplace is reflective whether or not its methodology governs the meta-decisions its own extension raises; those are separate properties, assessed separately.
- The bare classification is not the informative part: under a human-inclusive boundary nearly every maintained system is reflective, since [human-inclusive boundaries make reflection cheap](../notes/human-inclusive-boundaries-make-reflection-cheap.md). What the trace establishes is this system's autonomy profile — the harness, validators, and agents consume the self-representation without a human in the read path, while search and judgment-heavy evaluation remain human.

---

Relevant Notes:

- [Reflective system](../notes/definitions/reflective-system.md) — rationale: supplies the five obligations this classification discharges
- [Behavioral authority](../notes/definitions/behavioral-authority.md) — defined-in: names the consumer, channel, and force in the observed trace
- [Reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md) — rationale: the graded coverage criterion this system meets unevenly across its forms
- [Governed adaptation requires search, evaluation, and operative retention](../notes/governed-adaptation-requires-search-evaluation-and-retention.md) — rationale: the change-loop decomposition the trace is read against
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — rationale: the separate, stronger self-extension property
- [ADR 026: tag-readme type with completeness and coverage marks](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidence: the decision at the center of the observed trace
- [Design rationale management in Commonplace](./design-rationale-management.md) — part-of: why theory-to-implementation lineage is not enforced end to end
- [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the retained claim through which the adaptation signal was interpreted
</content>
