# Workshop: review-bundle-packing

## Question

How should review execution pack gates into prompts so review runs stay efficient without crossing the effective context-length and focus boundary?

## Why this workshop exists

The current review system has a gate-native storage model, but prompt execution still has several packing shapes:

- `commonplace-run-review-bundle` accepts any list of gate ids or bundle names and creates one review run for the resolved gate set.
- `commonplace-review-sweep --all-gates` iterates bundle directories, but each bundle is selected through freshness state; prior mixed runs can make later bundle-local sweeps look current for the same model partition.
- `commonplace-create-review-run --with-prompt` also creates one run for the resolved gate set, so live-agent review can accidentally mix multiple bundles into one prompt.
- `commonplace-run-gate-sweep` packs the other axis: one gate across many notes.

The accidental case is "all bundles for one note in one prompt." It is attractive because it amortizes note-reading cost, but it may exceed the effective context length even when it fits the formal context window. The reviewer has to hold many heterogeneous lenses at once, which can reduce finding quality, increase missed gates, and make parse/output failure more likely.

## Scope

This workshop is about **prompt packing policy and measurement** for review execution.

In scope:

- Whether a single review run may contain gates from more than one bundle/lens.
- How `run_review_bundle`, `create_review_run --with-prompt`, and `review_sweep --all-gates` should behave when asked for multiple bundles.
- Measurements of prompt size, output size, latency, parser failure, and review quality across packing shapes.
- Tests and command contracts that prevent accidental cross-bundle prompts.

Out of scope:

- Changing gate definitions or gate content.
- Changing acceptance semantics, gate sha freshness, or review database schema unless measurement shows the current schema cannot express the needed run identity.
- Re-reviewing notes just to repair the accidental mixed run history. Historical mixed runs can stay as history; the policy question is about future execution.

## Current grounding

- [review system](../../instructions/REVIEW-SYSTEM.md) - current workflow contract.
- [run review bundle on note](../../instructions/run-review-bundle-on-note.md) - live-agent single-note review flow.
- [review-architecture.md](../../reference/review-architecture.md) - current execution architecture.
- [review-prompt-consolidation](../review-prompt-consolidation/README.md) - prior decision to share one prompt/parser protocol across live-agent and subprocess paths.
- [review-run-lifecycle](../review-run-lifecycle/README.md) - lifecycle constraints for review run creation, completion, failure, telemetry, and acceptance.
- [gate-refactor](../gate-refactor/README.md) - background for gate-native review state.

## Working hypotheses

1. Bundle-local packing is probably the default safe policy: one note plus one bundle/lens per prompt.
2. Cross-bundle packing should not be the implicit behavior of any normal command. If it remains possible, it should require an explicit opt-in flag with measurements justifying the use.
3. Formal context-window fit is not enough. The relevant limit is effective context: whether the reviewer can reliably apply every requested gate without losing focus.
4. Sweep orchestration should preserve bundle boundaries even when the user asks for `--all-gates`.

## What would close this workshop

- A measurement table comparing at least these packing shapes:
  - one note x one bundle
  - one note x all bundles
  - one gate x many notes
  - prepared arbitrary batch of note-gate pairs, if still relevant
- A decision about command behavior for mixed bundle arguments.
- A patch plan with tests for the chosen invariant.
- Durable output in the right collection:
  - command/reference update if behavior changes,
  - instruction update if operator workflow changes,
  - ADR if the packing invariant becomes architectural.

## Files

- [measurement-plan.md](./measurement-plan.md) - proposed measurements and fixtures.
