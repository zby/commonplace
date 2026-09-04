---
description: "Definitions for The Automated Software House Conjecture paper"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
---
# Appendix A: Definitions

These entries bind the terms that the paper otherwise obtains from mutable KB artifacts or leaves implicit in its subtitle.

### Open-ended software development with fixed LLMs

In this paper, this phrase means continued software development under an advance-declared request process that can produce relevant demands not enumerated before the run. The eligible LLM versions, their weights, and every other learned component stay fixed. The house may instead learn by computationally changing and retaining its natural-language and symbolic state, including its software and production machinery. Open-ended does not mean unbounded: the product scope, operating horizon, input process, and resource budget are declared before the witness run.

Paper-native; defined from the body's usage. Source commit: `50121b7178058782f7b264127bbd23d94f7eeff5`.

### Software house

A software house is the complete persistent system responsible for developing and evolving software for external users in response to their requirements, feedback, and operating consequences. It includes the software being evolved, the production knowledge and machinery used to change it, and every person or computational component filling an internal production role. Users remain outside when they supply product-level requirements, domain facts, feedback, or judgments about visible behaviour. An automated software house requires no human in an internal production role over its declared product scope and operating horizon.

Adapted from kb/notes/definitions/software-house.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Distributed-parametric state

Distributed-parametric state is behaviour-shaping numerical state whose relevant content is spread across parameters or dense representations rather than localized in an addressable unit. In this paper it includes LLM weights and any other learned component, such as an embedding model. These components are pinned for the witness run. Dense-vector indexes derived mechanically from the paper's mutable notes and code are views of that state only when the declared pinned machinery regenerates them; they are not independently trained state.

Adapted from kb/notes/definitions/representational-form.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Notes and code

Notes and code is the paper's collective name for the house's localized, mutable state. Notes carry behaviour-shaping content through natural-language interpretation. Code, schemas, tests, validators, tools, route tables, and other symbolic artifacts receive assigned consequences from defined consumers. The phrase names representational form rather than storage format: a Markdown file may contain natural-language and symbolic operative parts. A retained item affects learning only if a later production path consumes it and its retention changes later behaviour.

Adapted from kb/notes/definitions/representational-form.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Definition

The linked definition supplies the internal production-role boundary. An internal production role is work on which the house depends to produce or evolve its software, including interpreting production knowledge, making implementation decisions, diagnosing internal failures, comparing candidates, editing project theory, selecting successors, or repairing production machinery. The boundary follows the role performed, not the person's identity. The same person is external while supplying a requirement or acceptance judgment about visible behaviour and internal while performing a production decision the house needs.

Adapted from kb/notes/definitions/software-house.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Transition closure of the seed

The transition closure of the seed is the least set of complete house states that contains the initial seed and is closed under every successor transition its current update machinery can produce from permitted external inputs. A state includes mutable notes, software, production machinery, retention rules, evaluators, and context assembly; pinned learned components are fixed parameters. The successor relation may be deterministic, nondeterministic, or probabilistic, and may itself change when the house rewrites its machinery. Such a rewrite still has to be produced by a predecessor state, so every autonomous successor remains in the seed's lineage by descent.

Adapted from kb/articles/reachability-as-closure-under-the-seed-gate.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live article may have changed.

### Gödel machine

A Gödel machine is a formal self-modifying construction whose entire software, including its proof searcher, may be rewritten. A single gate controls every rewrite: under axioms describing the machine, environment, initial code, and utility function, the machine must prove that executing the proposed rewrite now has higher expected utility than continuing the current search. The proof checker then invokes and retains the rewrite. Its guarantee is conditional on that formalization and excludes beneficial changes the machine cannot prove. The construction has no users and changes only itself, so it is not a software house in this paper's sense.

Adapted from kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.
