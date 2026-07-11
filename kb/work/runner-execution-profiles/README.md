# Runner execution profiles workshop

## Goal

Build uniform, runner-portable procedures for choosing the model and thinking effort used by each agent role, initially across Codex and Claude. The procedures should make multi-agent workflows faster and cheaper without silently weakening the judgments that matter.

The motivating case is the full improvement pass, whose stages range from mechanical report handling and copyediting to adversarial critique, semantic judgment, synthesis, and closing controls. The same problem already appears elsewhere: skills declare whole-skill `model:` overrides, instructions launch workers without a model policy, and the review subsystem records model partitions plus concrete runner provenance. This workshop treats those as one execution-policy problem while preserving their different semantics.

## Evaluation boundary

In scope:

- every canonical Commonplace skill and instruction that selects a model, invokes a sub-agent/worker, launches a runner, declares an effort, or relies on inherited execution settings;
- Codex and Claude as the first two runner families;
- parent, worker, critic, author, synthesizer, judge, auditor, copyeditor, discovery, and mechanical roles;
- model family/tier, concrete model, thinking or reasoning effort, context isolation, concurrency, fallback, escalation, and provenance;
- the distinction between execution choice and epistemic identity, especially review `model_partition`;
- procedures for resolving a portable profile into runner-specific calls and for reporting what actually ran;
- latency, cost, output quality, failure rate, and escalation rate.

Out of scope until the catalogue and schema force them:

- changing the review freshness model or merging model partitions;
- choosing one permanent cheap or strong model for every workflow;
- silently launching nested `codex` or `claude` CLI processes when the harness provides no authorized worker mechanism;
- treating a model tier as portable merely because two vendors use similar marketing labels;
- editing production skills or instructions as part of workshop setup.

## Semantic constraints

The design must keep these facts separate:

1. **Portable intent** — the capability/cost posture a procedure asks for, such as mechanical, economical, balanced, or strongest available.
2. **Runner resolution** — the concrete runner, model, and effort chosen for this invocation.
3. **Observed provenance** — what the worker reports actually ran.
4. **Epistemic identity** — whether the result belongs to a review freshness partition or another evidence class.

A cheaper execution mapping may be valid for an unanchored report and invalid for an accepted verdict. A fallback may preserve task completion while changing provenance. Neither case may be hidden by a generic `model: cheap` label.

## Required work products

- [inventory.md](./inventory.md) — exhaustive catalogue of current execution-policy declarations and gaps.
- [schema-sketch.md](./schema-sketch.md) — provisional cross-runner schema and unresolved design choices.
- [mvp.md](./mvp.md) — candidate two-level `main`/`fast` system, instruction metadata, dispatch resolution, and a conservative full-pass pilot.
- A verified Codex/Claude capability matrix: which surfaces can select sub-agent model, effort, isolation, concurrency, and clean context; which only inherit; and what provenance each surface exposes.
- A resolution procedure that turns portable role policy plus operator configuration into a concrete worker request, with explicit fallback and escalation behavior.
- A migration map from every catalogued skill/instruction to the uniform schema.
- Worked trials on representative low-, medium-, and high-judgment roles. The full pass must be covered, but it is not sufficient by itself.
- Measurements comparing baseline and routed execution: wall time, model calls, tokens or cost where available, parse/validation failure, material disagreement, escalation, and final artifact quality.

## Bookkeeping

- Catalogue canonical sources, not their generated `.claude/skills/` or `.agents/skills/` projections.
- Give every execution locus a stable `locus_id` based on its repo path and role.
- Record both declared policy and effective behavior; do not infer support from field names alone.
- Mark runner capabilities `verified`, `observed`, `documented`, or `unknown`, with date and source.
- Keep proposed portable tiers runner-neutral. Concrete model names and effort values belong in mappings.
- Treat current frontmatter and review-store names as evidence, not as a schema commitment.

## What closes this workshop

This workshop closes when:

1. the inventory covers every canonical skill/instruction execution locus and a repeatable sweep finds no uncatalogued model, effort, runner, or delegation directive;
2. the schema can represent every catalogued case without runner-specific fields leaking into portable procedure intent;
3. Codex and Claude resolution rules, unsupported-field behavior, fallback, escalation, and provenance are explicit and tested;
4. the full pass and at least two other structurally different workflows run from configuration rather than hard-coded model prose;
5. measurements identify which roles can move to cheaper/faster execution and which require stronger defaults or escalation;
6. durable outputs are promoted: an ADR for the schema and resolution boundary, reference documentation for configuration, and revised skills/instructions or a shared procedure; and
7. the workshop directory and its navigation entry are removed after promotion.

## Grounding

- [Run a full improvement pass](../../instructions/run-full-improvement-pass-on-note.md) — motivating multi-role workflow.
- [Run review batches](../../instructions/run-review-batches.md) — current inherited-model rule and review provenance boundary.
- [Review system](../../reference/README-REVIEW-SYSTEM.md) — model partition as freshness identity rather than execution preference.
- [Skills vs instructions findings](../skills-vs-instructions/findings.md) — existing evidence that skill frontmatter can carry execution policy while plain instructions cannot.
- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — existing runner-specific per-call model surface.
- [Model partition registry proposal](../../reference/proposals/model-partition-registry.md) — adjacent design that must not be conflated with portable role routing.
