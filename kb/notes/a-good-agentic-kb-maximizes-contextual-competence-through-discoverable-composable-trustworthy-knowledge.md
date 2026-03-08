---
description: Theory of why commonplace's arrangements work — three properties (discoverable, composable, trustworthy) serve contextual competence under bounded context; accumulation is the basic learning operation (reach distinguishes facts from theories); stabilisation, distillation, and discovery transform accumulated knowledge; Deutsch's reach criterion distinguishes knowledge that transfers from knowledge that merely fits
type: note
areas: [kb-design, learning-theory]
status: seedling
---

# A good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge

## What is a good agentic knowledge base?

A knowledge base for an agent is not a search engine. An agent doesn't just retrieve facts — it classifies, plans, communicates, and reasons on behalf of a user. The accumulated knowledge must make all of these actions more competent. [Claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) names this directly: a Claw's learning loop must improve *action capacity*, not just answer-finding.

The criterion is **contextual competence**: the agent's ability to act appropriately given what it knows about the domain, the user, and the project. A good agentic KB maximizes contextual competence under the constraint of [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the finite window through which the agent receives everything it can attend to.

This rules out "just put everything in the context." The constraint is real and structural: context degrades before it runs out (attention rot), complexity costs more than volume, and [there is no scoping mechanism](./llm-context-is-composed-without-scoping.md) to isolate what matters from what doesn't. A KB that produces competence must produce it *efficiently*.

## Three properties of knowledge that serves competence

For knowledge to improve an agent's actions under bounded context, it needs three properties. Each addresses a different failure mode:

**Discoverable** — the agent can find what it needs without loading everything. Failure mode: knowledge exists but the agent doesn't encounter it. Commonplace mechanisms: search over [files as the universal interface](./files-not-database.md) (grep for pattern matching, frontmatter queries for structured fields, qmd for semantic full-text search — the base layer that makes everything else work), [claim titles](./title-as-claim-enables-traversal-as-reasoning.md) that carry the argument without requiring descent into the body, retrieval-oriented descriptions that differentiate notes from each other, [area indexes](./areas-exist-because-useful-operations-require-reading-notes-together.md) that give the landscape at a glance, [progressive disclosure](./context-loading-strategy.md) that matches specificity to loading frequency.

**Composable** — pieces of knowledge combine into larger arguments and can be used as premises in new reasoning. Failure mode: the agent retrieves a note but can't use it with other notes — the knowledge is an island. Commonplace mechanisms: [typed links with articulated relationships](./link-strength-is-encoded-in-position-and-prose.md) that encode how notes relate ("since X" is a premise, "but Y" is a tension, "extends Z" is a generalization), [resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) between indexes (broad) and note bodies (narrow), the composability check in [WRITING.md](../WRITING.md) ("can this note be linked without dragging irrelevant context?").

**Trustworthy** — the agent can rely on what the knowledge says without independently verifying it each time. Failure mode: the agent loads a note but can't trust its claims — the knowledge is noise. Commonplace mechanisms: the [stabilisation gradient](./stabilisation.md) from raw text to structured claims to deterministic code, the [type system](./document-classification.md) that marks what kind of artifact something is, status fields that signal maturity (seedling → current), [validation scripts](./deterministic-validation-should-be-a-script.md) that enforce structural contracts.

These three properties have a dependency structure. Composability depends on the other two: you can't compose what you can't find (discoverability), and you can't build on an unreliable premise (trustworthiness). Trustworthiness depends on discoverability: a note that can't be found can't be challenged, corrected, or kept current. Discoverability is the foundation — without it, the other two are inert.

## Accumulation and three operations that improve these properties

The KB doesn't stay good automatically. It improves through learning, starting with the most basic operation.

**Accumulation** — adding knowledge to the store — is [the most basic learning operation](./learning-is-not-only-about-generality.md). But what you accumulate varies in [reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md). Storing a fact ("the key is on the table") is low-reach accumulation — useful for the immediate context but it doesn't transfer. Storing a theory ("systems that optimize for efficiency under normal load sacrifice resilience to overload") is high-reach accumulation — it applies in contexts it wasn't designed for. Both are genuine learning. Reach is the property that distinguishes them.

Three operations transform accumulated knowledge, each targeting different properties and operating on different dimensions of [capacity](./learning-is-not-only-about-generality.md):

**Stabilisation** constrains the interpretation space — from storing an output, to writing conventions, to extracting deterministic code. It [trades generality for the reliability+speed+cost compound](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). Stabilisation primarily improves **trustworthiness**: a validated script is more trustworthy than a prose instruction, a structured claim more trustworthy than a raw observation. It secondarily improves discoverability — a note with good frontmatter is more findable than raw text.

**Distillation** extracts focused artifacts from larger bodies of reasoning — methodology notes become skills, workshop explorations become design principles, research becomes prescriptive notes. It also [trades generality for compound gains](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md), but through selection and compression rather than constraint. Distillation primarily improves **discoverability**: a distilled skill fits in one context load where fifteen methodology notes wouldn't. It secondarily improves composability — a focused note composes better than a sprawling exploration. Deletion and pruning are distillation's negative face — selecting what to keep implies selecting what to discard, and removing outdated or contradictory knowledge improves capacity by subtraction.

**Discovery** posits a new general concept and [simultaneously recognizes existing particulars as instances of it](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md). Unlike stabilisation and distillation, discovery *creates* generality rather than sacrificing it. It primarily improves **composability**: a note that names a shared mechanism ("systems degrade under structural overload") becomes a hub that connects previously isolated notes, making them available as premises in each other's arguments. It secondarily improves discoverability — once the mechanism has a name, recognizing further instances becomes cheap. The naming amortizes the discovery cost. Discovery also produces the highest-reach items for accumulation — theories are what accumulation stores when it's at its most valuable.

| Operation | Capacity trade-off | Primary property improved | Commonplace example |
|---|---|---|---|
| Accumulation | Adds knowledge (reach varies) | All three (depends on what's accumulated) | Storing a new observation, recording a discovered principle |
| Stabilisation | Generality → compound | Trustworthiness | text → note → structured claim → validation script |
| Distillation | Generality → compound | Discoverability | 15 methodology notes → 1 `/connect` skill |
| Discovery | Creates generality | Composability | Seeing that PL scoping and agent context loading share the same mechanism |

A KB that only accumulates grows but never improves what it has — a pile, not a system. One that only stabilises gets rigid — trustworthy but unable to grow. One that only distils gets focused but shallow — discoverable but with nothing deep to discover. One that only discovers gets conceptually rich but unreliable and hard to navigate — composable in theory but not in practice. All four must operate continuously.

## Reach: why some knowledge serves competence better than others

The three properties tell you what knowledge must *be* — discoverable, composable, trustworthy. They don't tell you which knowledge is *worth* making discoverable, composable, and trustworthy. A KB could satisfy all three properties while being full of shallow facts that don't help the agent reason in new situations.

David Deutsch [distinguishes](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) **adaptive** knowledge (patterns that work but don't explain why) from **explanatory** knowledge (accounts that capture causal structure). The distinguishing property is **reach**: explanatory knowledge applies in contexts it was never designed for, because the explanation captures structure that isn't context-dependent. A gene "knows" how to build an eye but can't help you design a telescope. Newton's optics does both.

Reach matters for an agentic KB because an agent encounters novel situations constantly — new tasks, new codebases, new user requests. Knowledge with reach transfers to these situations. Knowledge without reach doesn't. A note that says "files beat a database because agents already have Read/Write/Grep tools" is adaptive — it works now, but if the toolset changes, the conclusion changes unpredictably. A note that says "files beat a database because [the universal interface principle](./files-not-database.md) minimizes coupling between the storage layer and the consumer" has reach — it explains *why*, predicts *when* the conclusion would change, and applies to storage decisions beyond this specific system.

Reach connects to accumulation and the three transformation operations asymmetrically:

- **Accumulation** is where reach varies most. Reach is the key property of what you accumulate — facts sit at the low end (adaptive, context-bound), theories at the high end (explanatory, transferable). The same operation (adding knowledge to the store) produces vastly different value depending on the reach of what's added.
- **Stabilisation** preserves reach but doesn't create it. A crystallised script is no more explanatory than the prompt it replaced — just more reliable. Stabilisation improves the compound (reliability, speed, cost) without affecting generality, and reach lives in the generality dimension.
- **Distillation** can preserve or destroy reach. Distilling methodology into a skill preserves reach *if* the skill captures the principle, not just the procedure. A skill that says "do steps 1-5" has lost the reach of the reasoning that produced those steps. A skill that says "do steps 1-5 *because* X" keeps it.
- **Discovery** is where reach is *created*. The discovery operation — positing a general concept, recognizing particulars as instances — is precisely the act of finding structure that reaches beyond the original cases. The [three depths of discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) (shared feature → shared structure → generative model) correspond to increasing reach. Discovery produces theories — the highest-reach items accumulation can store.

The KB's [first-principles filter](./design-methodology-borrow-widely-filter-by-first-principles.md) is, in Deutsch's terms, a filter that selects for reach. When we require notes to derive patterns from constraints rather than recording "X works," we're selecting for explanatory knowledge that will transfer to new contexts. The [programming fast-pass](./design-methodology-borrow-widely-filter-by-first-principles.md) is a bet on reach — PL concepts apply to KB design because they capture structure that isn't programming-specific. Convergence evidence ([Thalo](./related-systems/thalo.md) independently building a compiler for knowledge management) suggests the reach is real.

### Tension: reach vs action value

There is a tension between reach as the primary quality criterion and contextual competence as the goal. [Claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) argues that an action-oriented system needs preferences, procedures, and judgment precedents — knowledge types that are inherently low-reach (context-specific) yet high-value for action. A procedure like "always run validation before committing" has minimal reach but substantial competence value.

The tension is real but not a contradiction, for two reasons. First, under bounded context, a compact theory replaces many facts — one note explaining *why* a pattern holds is more context-efficient than twenty notes recording instances where it worked. Reach is practical, not just intellectually satisfying, because it compresses knowledge. Second, reach matters most when knowledge leaves the KB — when insights transfer to new projects, new agents, or new domains. A KB that only stores context-specific procedures is useful for its host system but produces nothing portable. One that also stores explanatory knowledge generates value beyond its immediate context.

The resolution is not to choose one over the other but to recognize that the four operations serve different needs: accumulation stores both facts and theories, stabilisation makes procedures reliable, and discovery creates the theories that give a KB reach beyond its origin.

## Why this favors authored knowledge

The reviews of [sift-kg](./related-systems/sift-kg.md) and [Siftly](./related-systems/siftly.md) sharpen this theory by contrast. Both systems build knowledge structures from documents — sift-kg extracts entity-relation graphs via LLM, Siftly enriches and classifies bookmarks. Both are effective at what they do. But the kind of knowledge they produce — entity-relation triples, category assignments, semantic tags — is adaptive, not explanatory.

An extracted triple ("Person X works for Organization Y, confidence 0.85") captures a fact, not an explanation. It has no reach: it says nothing about *why* the relationship exists, doesn't predict when it would change, and doesn't compose with other triples to produce novel reasoning. The graph's value is in aggregation and navigation, not in the explanatory power of individual edges.

An authored note ("Context efficiency is the central design concern because context is the only channel and it degrades before it runs out") captures causal structure. It predicts consequences of change and composes with other notes to support novel arguments. Its value is in reach — it applies to design decisions not yet imagined.

This isn't a claim that extraction can never produce knowledge with reach — an LLM that extracted causal explanations from papers might. It's that the act of authoring, specifically the judgment that selects what matters and explains why, is what produces reach. Current extraction systems optimize for coverage and accuracy of facts, not for explanatory depth. Commonplace optimizes for explanatory depth — and that is the theory of why its arrangements work.

## The theory, compressed

A good agentic knowledge base maximizes **contextual competence** — the agent's ability to act appropriately given accumulated knowledge about the domain, user, and project — under **bounded context**. It does this through knowledge that is **discoverable** (findable without loading everything), **composable** (usable as premises in novel reasoning), and **trustworthy** (reliable enough to act on without re-verification). **Accumulation** — adding knowledge to the store — is the most basic learning operation, and **reach** is its key property: facts (low reach) are adaptive, theories (high reach) are explanatory and transfer to new contexts. Three operations transform accumulated knowledge: **stabilisation** (constraining — improves trustworthiness), **distillation** (extracting and pruning — improves discoverability), and **discovery** (generalizing — improves composability, produces the highest-reach items to accumulate). The KB's first-principles filter selects for reach — not because procedures and facts lack value, but because theories compress knowledge under bounded context and transfer when knowledge leaves the KB. Authoring — the act of judgment that explains why — is the primary source of knowledge with reach.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the bounded-context constraint that makes efficiency necessary
- [claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) — grounds: contextual competence as the criterion, not retrieval accuracy
- [stabilisation](./stabilisation.md) — mechanism: one of three learning operations; improves trustworthiness, preserves reach
- [distillation](./distillation.md) — mechanism: one of three learning operations; improves discoverability, preserves or destroys reach
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — mechanism: one of three learning operations; improves composability, creates reach
- [first-principles reasoning selects for explanatory reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — grounds: Deutsch's reach criterion as the quality measure for knowledge
- [stabilisation and distillation both trade generality for compound](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — grounds: the capacity trade-off that two of three operations make
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: Simon's definition and the generality-vs-compound decomposition
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: resolution-switching is a concrete test for discoverability + composability working together
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — exemplifies: claim titles serve both discoverability (scan without loading) and composability (use as premise)
- [files beat a database](./files-not-database.md) — exemplifies: architectural choice explained by reach (universal interface principle) not just adaptive fit (current tools)
- [design methodology — borrow widely, filter by first principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — exemplifies: first-principles filtering is selecting for reach
- [sift-kg](./related-systems/sift-kg.md) — contrasts: extraction-based KG produces adaptive knowledge (facts) where reach comes from aggregation, not individual edges
- [Siftly](./related-systems/siftly.md) — contrasts: enrichment-based system produces classified artifacts, not composable reasoning with reach

Topics:

- [kb-design](./kb-design.md)
- [learning-theory](./learning-theory.md)
