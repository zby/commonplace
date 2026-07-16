---
description: "The ADR-026 tag-readme change traced commit by commit as one observed instance of causal connection between Commonplace and its self-representation, in both directions"
type: kb/types/note.md
traits: [has-implementation]
---

# The tag-readme change as an observed causal-connection trace

Causal connection is the obligation that separates a reflective system from a merely well-documented one, and it has to be shown as an observed instance rather than argued from architecture. The `tag-readme` type (ADR 026) supplies one, end to end. This note is the full walkthrough behind the [classification](./commonplace-as-a-reflective-system.md); the [self-improving reading](./tag-readme-trace-as-self-improving-loop.md) interprets the same trace as an improvement loop.

## The strain

It began as a strain rather than a logged failure. The `index` type was doing two jobs at once — enumerating a tag's members completely and introducing the tag — and the `learning-theory` index had grown to 18.8 KB and 55 entries, past the point where anyone could still call it complete. The KB already held a claim that made sense of the strain: [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md), because a head marked complete tells a thorough reader to stop looking while members are still missing.

## Revising the self-representation

The response was to revise the self-representation, and formulating that response into a specific candidate was not the maintainer's work alone. An agent working in the repository, in Claude Code, retrieved [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) as the claim that made sense of the strain and drafted the two-type split around it — one instance of a wider set of candidate-forming mechanisms [surveyed separately](./where-change-candidates-come-from-in-commonplace.md). Commit `91130f82` then added [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), which split the type in two and made `complete` an *enforced* mark — the ADR insists the unenforced prose version must never be written, since a trusted-but-stale cache is exactly the failure it guards against. Commit `94769805` then carried that single decision into four forms at once: the prose spec (`kb/types/tag-readme.md`), the JSON schema, the validator (`src/commonplace/lib/validation.py`), and the build-time renderer. The tie between prose and code is not loose — the validator dispatches on the spec's own path, so the spec file *is* the key that turns enforcement on:

```python
@type_rule("kb/types/tag-readme.md")
def validate_tag_readme(results, parsed, *, run) -> None:
```

The ADR's numbers reappear as constants (`TAG_README_SOFT_BYTES`, `TAG_README_HARD_BYTES`, `TAG_README_MAX_FANOUT`), and a failing check points the reader back to the maintenance instruction. Tests landed in the same commit to pin the contract (`test_complete_mark_fails_on_missing_member`, `test_covered_by_fails_on_uncovered_note`, `test_weight_gates_warn_and_fail`); ADR 026 mentions a rename-list review gate for the migration, but nothing recording that run survives, so the evidence is the tests plus the maintainer's review and merge. Commit `9976a081` migrated fifteen indexes to the new type, and the marks are live today — `tags-README.md`, `discovery-README.md`, `distillation-README.md`, and `artifact-analysis-README.md` all carry `complete: true`.

## What changed afterward

What makes this a causal connection rather than a coordinated edit is what changed afterward. Three consumers behave differently now, and [behavioral authority](../notes/definitions/behavioral-authority.md) lets us name each path precisely instead of saying the artifact vaguely "influenced" the system:

| Consumer | Channel | Force |
|---|---|---|
| `commonplace-validate-notes` | validation | enforcement — rejects what it used to accept |
| `cp-skill-connect` agent | instruction | routing — skips a search it used to run |
| Maintainer / navigation recipe | advice | correction of the documented procedure |

The validator change is the sharpest. Commit `dab163c6` made validating *one ordinary note* also pull in every marked tag-README that shares its tags; the test `test_note_target_also_validates_marked_tag_readmes` pins it, so validating `tagged-note.md` now exits 1 over a violation in a *different*, marked file. To satisfy the new check, the live KB had to change in that same commit — `artifact-analysis-README.md` gained entries it otherwise would not have. The represented constraint reached back and altered the represented system. The routing change is gentler but real: `kb/instructions/cp-skill-connect/SKILL.md:58` now tells the agent that when a tag-README is marked `complete`, it can skip the by-tag `rg` for that tag, so the agent makes fewer tool calls because of what the self-representation asserts.

The third change runs the other way, from code back to prose. Adopting `covered_by` on the `learning-theory` head (commit `ba1a7d9f`), the new symbolic check caught a member the prose `rg` recipe had missed — a note written with block-style YAML tags that the documented pattern couldn't see. The recipe in `kb/reference/navigation.md` was corrected to record the blind spot, and the loop closed back into theory when the workshop holding the work was dissolved into a retained note (`46f106c5`).

Both directions are therefore on record: a change in the system forced a revision of its self-representation, and a change made through the self-representation changed what the system afterward required, rejected, and searched.

---

Relevant Notes:

- [Commonplace as a partially autonomous, reflective self-improving system](./commonplace-as-a-reflective-system.md) — part-of: the classification this trace is the evidence for
- [The tag-readme trace read as a self-improving loop](./tag-readme-trace-as-self-improving-loop.md) — see-also: the same trace read as an improvement loop
- [Where change candidates come from in Commonplace](./where-change-candidates-come-from-in-commonplace.md) — part-of: surveys the wider set of candidate-forming mechanisms the agent's drafting work here is one instance of
- [Reflective system](../notes/definitions/reflective-system.md) — rationale: the causal-connection obligation this trace instantiates
- [Behavioral authority](../notes/definitions/behavioral-authority.md) — defined-in: names each consumer, channel, and force in the trace
- [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the retained claim the strain was read through
- [ADR 026: tag-readme type with completeness and coverage marks](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — part-of: the decision this trace documents
