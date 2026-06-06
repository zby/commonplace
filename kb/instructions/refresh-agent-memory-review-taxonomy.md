---
description: "Use when refreshing existing agent-memory-system reviews for the current artifact taxonomy without doing a full source re-review"
type: kb/types/instruction.md
---

# Refresh agent-memory review taxonomy

Use this procedure to update existing `kb/agent-memory-systems/reviews/` notes so they use the current artifact vocabulary. This is a taxonomy-consistency pass, not a full repository re-review.

## Prerequisites

- The target is one or more existing review notes under `kb/agent-memory-systems/reviews/`.
- The goal is to clarify current review prose, not to reassess the external repository from source.
- The working tree has been checked with `git status --short`.

## Scope

Do:

- clarify storage substrate, representational form, lineage, and behavioral authority where the existing review already contains enough evidence
- replace stale shorthand such as role, substrate class, knowledge memory, or system-definition memory when it means an artifact-analysis field
- keep edits local to review wording and the trace-derived survey when placement wording changes

Do not:

- update `last-checked` unless you actually re-read the source repository
- archive and rewrite the review
- add new implementation claims that require source inspection
- force every review to include a rigid four-field section

## Steps

1. **Select targets.** Prefer trace-derived and behavior-changing systems first. If no target list is supplied, start with reviews whose existing text mentions traces, lessons, rules, playbooks, skills, prompts, validators, learned policies, or benchmark-gated promotion.

2. **Read the current review.** Use only the active review file. Ignore archived `.replaced.*.md` files unless the user explicitly asks for historical comparison.

3. **Check review staleness.** Read `last-checked` from frontmatter. If it is missing or more than 30 days before today's date, record a staleness warning in the final report before editing. Continue only for vocabulary and taxonomy-clarity edits grounded in the existing review prose. Do not resolve ambiguity by adding new mechanism claims; recommend a source re-review instead.

4. **Classify each retained surface that matters.** For each memory, skill, rule, prompt, trace store, index, policy, dataset, or learned state that the review treats as architecturally important, ask:
   - **Storage substrate:** where does it persist?
   - **Representational form:** is the operative part prose, symbolic, distributed-parametric, or mixed?
   - **Lineage:** what source material, derivation path, invalidation rule, or regeneration rule controls it?
   - **Behavioral authority:** is it consumed as evidence, reference, context, explanation, or advice, or with instruction, enforcement, routing, validation, configuration, evaluation, ranking, or learning force?

5. **Patch only ambiguous prose.** Add wording when the old review leaves a taxonomy-relevant mechanism unclear. Prefer short replacements in existing paragraphs over new sections. Leave fields implicit when they are obvious and not central to the review's comparison.

6. **Handle trace-derived reviews carefully.** If the review has a trace-derived placement, ensure it distinguishes raw trace artifacts from distilled artifacts. Raw traces often have knowledge-artifact or evidence use; distilled rules, tools, prompts, validators, fine-tunes, or rankers often have system-definition-artifact use.

7. **Update the trace-derived survey only when needed.** Edit `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md` only if the refresh changes survey placement, axis wording, or a cross-system claim.

8. **Validate.** Run the smallest validation scope that covers the edited reviews and instruction or survey files. For a few files, validate each file directly:
   ```bash
   commonplace-validate path/to/edited-file.md
   ```
   For a broad review sweep, validate:
   ```bash
   commonplace-validate kb/agent-memory-systems
   ```

## Verify

- No active review still uses old taxonomy shorthand where the current fields are meant.
- Reviews whose `last-checked` date is older than 30 days are reported with a staleness warning.
- `last-checked` dates are unchanged unless source was re-read.
- Trace-derived reviews distinguish raw trace storage from distilled behavior-changing artifacts when both exist.
- Validation reports no failures in the edited scope.
