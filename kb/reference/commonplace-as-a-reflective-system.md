---
description: "Classifies the shipped Commonplace system against the five reflective-system obligations and, on the same trace, as a human-inclusive self-improving system"
type: kb/types/note.md
traits: [has-implementation]
tags: [foundations, computational-model, self-improving-systems]
---

# Commonplace as a reflective system

Commonplace is a reflective system: it holds a representation of selected parts of itself, that representation is available to processes inside the system's boundary, and acting through it changes what the system does next. The stronger and more interesting claim is that Commonplace is also a human-inclusive, reflective [self-improving system](../notes/definitions/self-improving-system.md) — stronger because reflection on its own is cheap.

This is a classification of an existing system, not a new theory. [Reflective system](../notes/definitions/reflective-system.md) names five things anyone must state before using the term; the note works through them, then reads the same evidence against [self-improving system](../notes/definitions/self-improving-system.md), which asks for two more — that the system change its own organization, and that it answer to evidence about an objective it could have failed. All of it rests on one trace from the repository's history, not on what the architecture could do in principle. The reflection here is partial and bound to particular aspects, and the limits at the end are part of the claim, not apologies for it.

## The frame

Commonplace is socio-technical, so its boundary runs through people as well as code. Inside are the repository and its artifacts, the software that validates, selects, renders, and consumes them (`src/commonplace/`, the `commonplace-*` commands, the review store), the agents working under the repository's instructions, and the human authors, reviewers, and maintainers who approve and merge. Outside are the things Commonplace cannot touch: the model provider and its weights, the inference machinery, the hosting and CI, and the readers of the published site.

Three more obligations round out the frame, and each is quickly met. Commonplace represents its **artifact types and their contracts** (`kb/types/`), its **routing and organization** (`COLLECTION.md` files, navigation), its **maintenance and review procedures**, and its **design rationale** (`kb/reference/adr/`) — but not the model's runtime behavior, how well any note does its job, or how a problem comes to be noticed. Its **self-representing** artifacts are the ones that say how the system's own artifacts must be shaped: type specs, collection contracts, instructions, ADRs, schemas, review criteria. (`kb/types/tag-readme.md` counts, because the system enforces it as a rule; an ordinary note about some general phenomenon does not.) And the **processes that read and act through** that self-representation are a mix of people and code — maintainers approving contract changes, agents editing under instruction, and the validators, review commands, and renderer that load the self-representation as their rule. Human judgment sitting in that loop is not a gap in the classification; the definition allows for established roles inside a socio-technical boundary.

The fifth obligation, causal connection, is the one that carries the weight, and it needs the trace below.

## Causal connection: an observed trace

Causal connection has to be shown, not argued from architecture, and the `tag-readme` type (ADR 026) shows it end to end.

It began as a strain rather than a logged failure. The `index` type was doing two jobs at once — enumerating a tag's members completely and introducing the tag — and the `learning-theory` index had grown to 18.8 KB and 55 entries, past the point where anyone could still call it complete. The KB already held a claim that made sense of the strain: [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md), because a head marked complete tells a thorough reader to stop looking while members are still missing.

The response was to revise the self-representation. Commit `91130f82` added [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), which split the type in two and made `complete` an *enforced* mark — the ADR insists the unenforced prose version must never be written, since a trusted-but-stale cache is exactly the failure it guards against. Commit `94769805` then carried that single decision into four forms at once: the prose spec (`kb/types/tag-readme.md`), the JSON schema, the validator (`src/commonplace/lib/validation.py`), and the build-time renderer. The tie between prose and code is not loose — the validator dispatches on the spec's own path, so the spec file *is* the key that turns enforcement on:

```python
@type_rule("kb/types/tag-readme.md")
def validate_tag_readme(results, parsed, *, run) -> None:
```

The ADR's numbers reappear as constants (`TAG_README_SOFT_BYTES`, `TAG_README_HARD_BYTES`, `TAG_README_MAX_FANOUT`), and a failing check points the reader back to the maintenance instruction. Tests landed in the same commit to pin the contract (`test_complete_mark_fails_on_missing_member`, `test_covered_by_fails_on_uncovered_note`, `test_weight_gates_warn_and_fail`); ADR 026 mentions a rename-list review gate for the migration, but nothing recording that run survives, so the evidence here is the tests plus the maintainer's review and merge. Commit `9976a081` migrated fifteen indexes to the new type, and the marks are live today — `tags-README.md`, `discovery-README.md`, `distillation-README.md`, and `artifact-analysis-README.md` all carry `complete: true`.

What makes this a causal connection rather than a coordinated edit is what changed afterward. Three consumers behave differently now, and [behavioral authority](../notes/definitions/behavioral-authority.md) lets us name each path precisely instead of saying the artifact vaguely "influenced" the system:

| Consumer | Channel | Force |
|---|---|---|
| `commonplace-validate-notes` | validation | enforcement — rejects what it used to accept |
| `cp-skill-connect` agent | instruction | routing — skips a search it used to run |
| Maintainer / navigation recipe | advice | correction of the documented procedure |

The validator change is the sharpest. Commit `dab163c6` made validating *one ordinary note* also pull in every marked tag-README that shares its tags; the test `test_note_target_also_validates_marked_tag_readmes` pins it, so validating `tagged-note.md` now exits 1 over a violation in a *different*, marked file. To satisfy the new check, the live KB had to change in that same commit — `artifact-analysis-README.md` gained entries it otherwise would not have. The represented constraint reached back and altered the represented system. The routing change is gentler but real: `kb/instructions/cp-skill-connect/SKILL.md:58` now tells the agent that when a tag-README is marked `complete`, it can skip the by-tag `rg` for that tag, so the agent makes fewer tool calls because of what the self-representation asserts.

The third change runs the other way, from code back to prose. Adopting `covered_by` on the `learning-theory` head (commit `ba1a7d9f`), the new symbolic check caught a member the prose `rg` recipe had missed — a note written with block-style YAML tags that the documented pattern couldn't see. The recipe in `kb/reference/navigation.md` was corrected to record the blind spot, and the loop closed back into theory when the workshop holding the work was dissolved into a retained note (`46f106c5`). Both directions are therefore on record: a change in the system forced a revision of its self-representation, and a change made through the self-representation changed what the system afterward required, rejected, and searched.

## The same trace, read as self-improvement

Reflection is the machinery, not yet the interesting part. Read the same trace against [self-improving system](../notes/definitions/self-improving-system.md) and it discharges that definition too, which asks for two things the reflective obligations do not: a change to the system's own organization, and a response to evidence about an objective. Commonplace improves in the [proposal-selection](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) shape — draft a candidate, review it with a real chance of rejection, merge selectively — so that loop is the right grid to lay over the trace:

| Requirement | In the trace |
|---|---|
| **Change to the system itself** | The edit landed on `kb/types/tag-readme.md`, a self-representing artifact rather than ordinary content. |
| **Search** | Human — a maintainer noticed the `index` type was doing two jobs and that the `learning-theory` head had outgrown its completeness claim. |
| **Improvement objective** | The bar the change could have missed: a marked head must not mislead a thorough reader, per [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md). ADR 026 makes it testable — `complete` is a mark the validator can falsify. |
| **Evaluation** | Mixed — tests and the validator are mechanical, but the judgment that the split was the right shape was the maintainer's. |
| **Operative retention** | The three consumers above: enforcement, routing, advice. |

Naming the objective is the step the reflective reading never had to take, and it is what makes the loop improvement-*directed* rather than merely change-directed. It is also where the honesty comes in: the validator passing means the marks are consistent, not that the split actually made the KB better. That stays a claim, not a result.

The autonomy, then, is partial. Search is human; evaluation is split between mechanical checks and human judgment; retention is mechanical once the human merge happens. So Commonplace is a **human-inclusive** self-improving system, not an autonomous one — the loop closes, and it closes through the self-representation, but people stay in it wherever no good automatic oracle reaches, [since warranted autonomy is bounded by oracle reach](../notes/warranted-autonomy-is-bounded-by-oracle-reach.md).

## How far the coverage reaches

Being reflective at all is a weaker thing than *covering* every behavior-bearing representation and the mappings between them. Coverage is graded, [form by form](../notes/reflective-coverage-is-graded-across-representational-forms.md), and the trace shows it reaching unevenly:

- **Prose reasoning revising formal artifacts** — shown: ADR 026's written decision became a schema and a validator.
- **Symbolic execution revising prose** — shown once: the `covered_by` check found what the `rg` recipe had missed, and the recipe was fixed.
- **Mappings that are themselves represented and editable** — only partly. The spec-to-validator mapping is unusually tight, since the spec path is the dispatch key, so those two can't drift apart quietly; most other prose-to-code links in the repository have no such binding.
- **Lineage and staleness across forms** — mostly absent. Commonplace does not guarantee a traceable path from a claim to the code that implements it (see [design rationale management](./design-rationale-management.md)); freshness tracking covers review pairs, not theory-to-implementation lineage.
- **The model weights** — selection only. The weights sit outside the boundary and nothing inside can read or edit them; the single lever is choosing among sealed alternatives, as when skill frontmatter pins `model: opus` or `model: sonnet` and review baselines partition by model. What is editable is the *binding*, not the model — changing that line changes which substrate runs, and nothing finer.

In short, reflective reach hits modification depth on the prose and symbolic forms — proven on the type-system spine, possible but not systematic elsewhere — and only selection depth on the weights.

## What the classification does not claim

The reach stops well short of the whole system, and saying where is part of the point. Search — noticing the problem, choosing the target — is still substantially human, and the methodology does not govern it. Nothing here shows the accepted change was an improvement; the reading above says only what was checked and by what. Rationale lineage is not mechanically guaranteed, and the weights and the other outside dependencies stay beyond reach. Reflection also does not imply [closure under recommendations](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): whether Commonplace's methodology governs the meta-decisions its own extension raises is a separate property, judged separately.

The bare label is the least of it. Under a human-inclusive boundary almost any maintained system comes out reflective, [since that boundary makes reflection cheap](../notes/human-inclusive-boundaries-make-reflection-cheap.md). What the trace earns is not the label but the location — where on the autonomy profile Commonplace actually sits.

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
