---
description: "Classifies Commonplace as a partially autonomous, reflective self-improving system, using one observed trace to locate which parts of the improvement loop run in code and which stay human"
type: kb/types/note.md
traits: [has-implementation]
tags: [foundations, computational-model, self-improving-systems]
---

# Commonplace as a partially autonomous, reflective self-improving system

Commonplace is reflective — it holds a representation of selected parts of itself, that representation is available to processes inside its boundary, and acting through it changes what the system does next. On its own that says little: under a boundary that counts human maintainers as internal processes, [almost any maintained system is reflective](../notes/human-inclusive-boundaries-make-reflection-cheap.md). Reflection is the floor here, not the claim.

The claim is that Commonplace is a **partially autonomous self-improving system**. Its improvement loop closes — a change is proposed, evaluated against an objective it could have failed, and retained — and part of that loop runs with no human in it. The [proposal-selection](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) shape names the parts: **search** and the judgment-heavy half of **evaluation** stay human, while the objective-check half of evaluation and the **retention** of the change run in code. The interesting question is not whether Commonplace is reflective but where on that human/autonomous split it sits — and the answer is read off one observed change, not off what the architecture could do in principle.

The evidence is a single trace from the repository's history, the `tag-readme` type (ADR 026), walked in full in [the observed trace](./tag-readme-trace-observed-causal-connection.md) and read as an improvement loop in [the self-improving reading](./tag-readme-trace-as-self-improving-loop.md). This note carries the argument those two walkthroughs support. The limits at the end are part of the claim, not apologies for it.

## The frame

Commonplace is socio-technical, so its boundary runs through people as well as code. Inside are the repository and its artifacts, the software that validates, selects, renders, and consumes them (`src/commonplace/`, the `commonplace-*` commands, the review store), the agents working under the repository's instructions, and the human authors, reviewers, and maintainers who approve and merge. Outside are the things Commonplace cannot touch: the model provider and its weights, the inference machinery, the hosting and CI, and the readers of the published site.

Three more obligations round out the frame, and each is quickly met. Commonplace represents its **artifact types and their contracts** (`kb/types/`), its **routing and organization** (`COLLECTION.md` files, navigation), its **maintenance and review procedures**, and its **design rationale** (`kb/reference/adr/`) — but not the model's runtime behavior, how well any note does its job, or how a problem comes to be noticed. Its **self-representing** artifacts are the ones that say how the system's own artifacts must be shaped: type specs, collection contracts, instructions, ADRs, schemas, review criteria. (`kb/types/tag-readme.md` counts, because the system enforces it as a rule; an ordinary note about some general phenomenon does not.) And the **processes that read and act through** that self-representation are a mix of people and code — maintainers approving contract changes, agents editing under instruction, and the validators, review commands, and renderer that load the self-representation as their rule.

The fifth obligation, causal connection, is the one that carries the weight, and it is what the observed trace supplies.

## Causal connection, in brief

Causal connection separates a reflective system from a merely well-documented one, and it has to be shown, not argued. The tag-readme change shows it in both directions. A strain in the system — an `index` head grown too large to honestly call complete — drove a revision of the self-representation: [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) split the type and made `complete` an *enforced* mark, carried into the prose spec, the schema, the validator, and the renderer in one stroke. That revised self-representation then reached back and changed what the system does — the validator now rejects notes it used to accept, an agent skips a search it used to run, and a symbolic check even caught a member the prose search recipe had missed and got the prose corrected. [The full walkthrough](./tag-readme-trace-observed-causal-connection.md) traces every step commit by commit; the short version is that a change in the system forced a revision of its self-representation, and a change made through the self-representation changed what the system afterward required, rejected, and searched.

## Where the autonomy is

Read that same trace as an improvement loop and the autonomy becomes locatable step by step. [The self-improving reading](./tag-readme-trace-as-self-improving-loop.md) does the full mapping; the thesis rests on three of its rows.

**Search is human.** A maintainer noticed the `index` type was doing two jobs and that the `learning-theory` head had outgrown its completeness claim. Nothing in the methodology noticed it for them.

**Evaluation is split, and the split is the whole point.** The improvement objective — a head marked complete must not mislead a thorough reader, per [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — was not left as prose for a person to check. ADR 026 *codified* it: `complete` became a mark the validator can falsify. From that point the objective is checked in code, on every run, with no human in the loop — validating an ordinary note now fails if a marked README sharing its tags is missing a member. What stays human is the other half of evaluation, the judgment that splitting the type was the right shape, which no validator can pass on.

**Retention is autonomous once the human merge lands.** The accepted change does not need a person to keep enforcing it: the constraint rejects future violations by itself, and an agent now skips a search by itself. The human merge installed the change; its continued operation is the system's.

So the autonomy covers the back of the loop — the codified objective-check and the retention that enforces it — while the front, search and the shape-judgment, stays human. That is what "partially autonomous" means here, precisely: not that Commonplace improves itself unattended, but that once a human has framed an objective sharply enough to codify, the system evaluates and enforces against it on its own. The reach of that autonomy is the reach of the available oracle — humans keep exactly the gates where no adequate automatic check exists, [since warranted autonomy is bounded by oracle reach](../notes/warranted-autonomy-is-bounded-by-oracle-reach.md) — so sharpening an objective enough to codify it is the move that shifts a gate from the human side to the code side.

One honesty check belongs here: the validator passing means the marks are consistent, not that the type split made the KB better. Autonomy over the objective-check is not autonomy over whether the objective was worth adopting. That judgment was the maintainer's, and it stays a claim, not a result.

## How far the coverage reaches

Being reflective at all is a weaker thing than *covering* every behavior-bearing representation and the mappings between them. Coverage is graded, [form by form](../notes/reflective-coverage-is-graded-across-representational-forms.md), and the trace shows it reaching unevenly:

- **Prose reasoning revising formal artifacts** — shown: ADR 026's written decision became a schema and a validator.
- **Symbolic execution revising prose** — shown once: the `covered_by` check found what the `rg` recipe had missed, and the recipe was fixed.
- **Mappings that are themselves represented and editable** — only partly. The spec-to-validator mapping is unusually tight, since the spec path is the dispatch key, so those two can't drift apart quietly; most other prose-to-code links in the repository have no such binding.
- **Lineage and staleness across forms** — mostly absent. Commonplace does not guarantee a traceable path from a claim to the code that implements it (see [design rationale management](./design-rationale-management.md)); freshness tracking covers review pairs, not theory-to-implementation lineage.
- **The model weights** — selection only. The weights sit outside the boundary and nothing inside can read or edit them; the single lever is choosing among sealed alternatives, as when skill frontmatter pins `model: opus` or `model: sonnet` and review baselines partition by model. What is editable is the *binding*, not the model.

In short, reflective reach hits modification depth on the prose and symbolic forms — proven on the type-system spine, possible but not systematic elsewhere — and only selection depth on the weights.

## What the classification does not claim

Commonplace is not *fully* autonomous, and saying where it stops is part of the point. Search — noticing the problem, choosing the target — is human, and the methodology does not govern it; so is the judgment that any given change is the right shape. Nothing here shows the accepted change was an improvement, only that it holds against the objective it was checked against. Rationale lineage is not mechanically guaranteed, and the weights and the other outside dependencies stay beyond reach. Reflection also does not imply [closure under recommendations](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): whether Commonplace's methodology governs the meta-decisions its own extension raises is a separate property, judged separately. What the trace earns is not a label but a location — where on the autonomy split Commonplace actually sits.

---

Relevant Notes:

- [The tag-readme change as an observed causal-connection trace](./tag-readme-trace-observed-causal-connection.md) — contains: the full observed trace behind the causal-connection claim
- [The tag-readme trace read as a self-improving loop](./tag-readme-trace-as-self-improving-loop.md) — contains: the full search/evaluation/retention mapping behind the autonomy claim
- [Reflective system](../notes/definitions/reflective-system.md) — rationale: supplies the five obligations this classification discharges
- [Self-improving system](../notes/definitions/self-improving-system.md) — rationale: supplies the loop and autonomy profile the trace is read against
- [Behavioral authority](../notes/definitions/behavioral-authority.md) — defined-in: names the consumer, channel, and force in the observed trace
- [Reflective coverage is graded across representational forms](../notes/reflective-coverage-is-graded-across-representational-forms.md) — rationale: the graded coverage criterion this system meets unevenly across its forms
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rationale: the change-loop decomposition the trace is read against
- [warranted autonomy is bounded by oracle reach](../notes/warranted-autonomy-is-bounded-by-oracle-reach.md) — rationale: why the autonomy stops exactly at the human gates
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — rationale: the separate, stronger self-extension property
- [human-inclusive boundaries make reflection cheap](../notes/human-inclusive-boundaries-make-reflection-cheap.md) — rationale: why the bare reflective label is uninformative here
- [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the retained claim through which the adaptation signal was interpreted, and the improvement objective
