---
source: https://www.blackhc.net/essays/future_of_software/
description: Essay arguing AI makes software more malleable, not ephemeral, because validation, state, interface stability, and auditability remain the load-bearing bottlenecks.
captured: 2026-03-19
capture: web-fetch
type: blog-post
---

# The Flawed Ephemeral Software Hypothesis

Author: Andreas Kirsch
Source: https://www.blackhc.net/essays/future_of_software/
Date: March 18, 2026

## Overview

Kirsch argues against the strong claim that AI coding tools will make software disposable. He accepts that "vibe coding" already makes one-off scripts, prototypes, and lightweight apps cheaper to produce, but argues that this does not generalize to important, repeatedly used, stateful systems. The hard part of software engineering, in his framing, is not code generation but discovering correct behavior under real-world ambiguity, integrations, and operational constraints.

## Core Thesis

The essay's central claim is:

- AI makes code cheaper to produce, but does not make software itself ephemeral.
- As generation gets cheaper, the bottlenecks shift to validation, integration, ergonomics, and operational trust.
- Durable artifacts proliferate rather than disappear: code, version history, tests, schemas, specs, audit trails, logs, and postmortems all become more important.
- The future of software is therefore better described as *malleable* rather than *ephemeral*.

Kirsch treats code as the final place where operational ambiguity is resolved into deployed behavior. Natural language can express intent, but cannot replace formal executable semantics for software with meaningful stakes.

## Avoiding the Motte and Bailey

Kirsch distinguishes two claims that are often blurred together:

- **Vibe coding:** natural-language intent can produce working code quickly enough that some artifacts are genuinely disposable.
- **Ephemeral software:** important software is generated on demand, used briefly, and not meaningfully maintained; the durable layer moves upward into prompts, specs, logs, and policies while code becomes a cache.

He argues that current evidence mostly supports the first claim, not the second. High adoption of AI coding tools, fast growth of coding startups, and AI-generated codebases inside normal engineering workflows show increased malleability, not disappearance of persisted code artifacts.

He decomposes ephemerality along two axes:

- regeneration frequency
- artifact durability

The strong form of the hypothesis sits at the extreme of both: continuous regeneration with minimal persisted code artifacts. Kirsch argues that this corner becomes unstable as systems accumulate users, state, and integration complexity.

## Why the Idea Is Seductive

Kirsch takes the case for ephemerality seriously. He cites:

- Andrej Karpathy's framing of code as free, malleable, and disposable in some contexts
- Tomasz Tunguz's prediction that ephemeral apps could outnumber SaaS applications
- Anish Acharya's economic argument that software no longer needs to be permanent or practical
- market signals such as major valuations for AI coding companies
- survey and code-quality data suggesting developers already treat code as more disposable

He grants a real economic case for ephemeral software in lightweight settings. If regeneration gets reliable enough, it can beat maintaining low-quality legacy systems. But he argues that the residual costs do not vanish; they move into maintaining trust in regenerated systems.

## Historic Precedents and the Compiler Analogy

Kirsch compares the hypothesis to failed software rewrites. He invokes Brooks's move from "plan to throw one away" to "grow, not build," and Joel Spolsky's critique of Netscape's rewrite, to argue that mature systems contain large amounts of embedded operational knowledge not fully captured in documentation.

He also addresses the compiler analogy directly. Prior abstraction shifts moved from one formal language to another with clear semantics. The strong ephemeral-software thesis asks for natural language, with its residual ambiguity, to become the persisted specification layer for important systems. Kirsch argues that this is historically different and structurally unstable.

## Structural Barriers

Kirsch says cheap generation does not remove the main sources of software difficulty. He names four barriers that remain even with stronger AI systems.

### 1. Edge Cases

Edge cases emerge from real usage, bad data, and strange environmental interactions. This knowledge accumulates only after deployment. Regeneration reintroduces novelty, so teams must rediscover or preserve those lessons somehow. If robust regeneration uses logs, incident histories, tests, canaries, and production memory, the system has already become more durable than "ephemeral."

### 2. State, Data, and Integration Surfaces

Real systems carry backward-compatibility constraints, migrations, hidden API quirks, and implicit module dependencies. Regenerated code must still work against old state and external systems. Kirsch argues this is where rewrites historically fail and where "almost right" behavior can be especially dangerous because it can silently corrupt data.

### 3. Interface Stability

Repeated use creates expectations. Users rely on consistency in UI layouts, shortcuts, workflows, and behavioral details. Unresolved ambiguity in natural-language specifications produces variance across regenerations, which shows up to users as instability. High-stakes domains such as healthcare and operations make this especially costly.

### 4. Ambiguity, Determinism, and Auditability

Kirsch separates non-determinism from ambiguity. Non-determinism in model outputs may be technically manageable. The deeper problem is that natural language leaves many behavioral questions open. Systems with serious stakes also require traceable artifacts for compliance, incident response, and liability. As requirements become more critical, the specification layer must become more formal, pushing it back toward code-like artifacts.

## From Ephemeral to Malleable Software

Kirsch's alternative is a "malleable software" model. In this model:

1. A stable deployed baseline exists, including code, infrastructure, schemas, and interfaces.
2. AI agents accumulate production memory from incidents, logs, support tickets, and deployment outcomes.
3. Requested changes update multiple persisted artifacts together: specs, code, tests, migration plans, and runbooks.
4. Verification runs against tests and replayed traces.
5. Deployment feeds new observations back into the memory layer.

The optimization target becomes reliable change at lower cost, not code disposability. AI accelerates edits and maintenance, but within a bounded, persisted artifact stack.

## Example: Multi-Currency Payments

Kirsch contrasts three workflows for adding multi-currency support:

- a traditional team that updates code, tests, and rollout plans over weeks
- an ephemeral-software team that regenerates the module from updated prompts and historical traces, but still risks novel failures from new code interacting with old state
- a malleable-software team that uses AI to draft implementation and surrounding artifacts, then verifies and rolls out incrementally behind feature flags

The lesson is that AI helps most when paired with persisted artifacts and staged deployment, not when code is treated as disposable.

## Could the Boundary Shift?

Kirsch allows that AI may expand the zone of software that can safely remain lightweight and therefore somewhat ephemeral. Better decomposition could isolate parts of systems that are more safely regenerable. But he argues there are limits because state, integration complexity, shared data, and user expectations are often properties of the problem domain, not just accidents of poor architecture.

## What Would Falsify the View

Kirsch says he would update toward the ephemeral-software hypothesis if the following became common within a few years:

- most new consumer and internal business applications are generated ephemerally with acceptable reliability
- production-critical systems run mainly on repeatedly regenerated, disposable code without worse incident rates
- regulated domains accept prompt or spec lineage without code-level persistence as sufficient audit evidence
- engineering organizations show falling persisted artifact volume per service rather than continued artifact growth

## Conclusion

The essay concludes that vibe coding is real and expanding, but strong claims about disposable software overreach. Software engineering remains dominated by discovering correct behavior in contact with the world, preserving continuity across state and integrations, and maintaining auditable, stable systems. AI changes the economics of editing and maintaining artifact stacks, but does not eliminate the need for those stacks. The future, in Kirsch's framing, is more software that is easy to reshape, not software that can be forgotten.
