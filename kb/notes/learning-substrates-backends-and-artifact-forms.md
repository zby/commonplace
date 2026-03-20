---
description: Tips, notes, rules, prompts, schemas, and playbooks belong to one symbolic artifact substrate even when stored in repos, databases, or memory services; backend and artifact form are separate axes
type: note
traits: [has-comparison]
tags: [learning-theory]
status: current
---

# Learning substrates, backends, and artifact forms

"Weights," "tips," and "repo artifacts" look like parallel terms, but they name things at three different levels. Weights names a **substrate class** — what kind of thing changes when the system learns. Tips names one **artifact form** within a substrate. Repo names a **storage backend**. Conflating the three makes the comparison space blurry: you end up arguing "tips vs weights" when the real contrast is between substrate classes, and treating "repo artifacts" as an umbrella when it is one backend choice.

The primary split is substrate class:

- **Subsymbolic substrate** — the learned result lives in model parameters or other latent state. AgeMem and [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) are clean examples.
- **Symbolic artifact substrate** — the learned result lives in discrete, inspectable symbolic objects. What those objects look like and where they are stored are separate decisions.

## Backend: where symbolic artifacts live

Symbolic artifacts can live in different backends without changing substrate class — repo files, database rows, service-managed memory objects, graph stores, or vector stores with attached symbolic records and provenance. This is why "repo artifacts" is too narrow as the umbrella term. Repo-hosted markdown is one important backend, especially for commonplace, but it is not the whole symbolic artifact substrate. [Cognee](./related-systems/cognee.md) keeps symbolic units in a database-backed poly-store; the backend changed, the learned result is still symbolic and inspectable.

## Artifact form: what symbolic artifacts look like

Within the symbolic artifact substrate, systems can produce many different artifact forms — tips, notes, reflections, rules, prompts, schemas, tests, playbooks, ranked memories. These differ in granularity, retrieval mode, and how directly they constrain later behavior, but they belong to one family: durable symbolic objects that can be inspected, revised, and composed.

## Why the distinction matters

The three-level split prevents category mistakes that keep recurring in comparisons across this KB.

[Files beat a database for agent-operated knowledge bases](./files-not-database.md) argues that a database schema forces premature commitment to access patterns — a claim about **which backend** to pick within the symbolic artifact substrate, not about whether to use symbolic artifacts at all. Separating the levels makes that scope visible: files can beat a database for a young KB without implying that all symbolic artifact learning must live in files.

The comparison between [trajectory-informed memory generation](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) and [AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md) sharpens the same way. The real contrast is not "tips vs weights" but **symbolic artifact substrate vs subsymbolic substrate**. "Tips" are just one artifact form on the symbolic side.

[Deploy-time learning](./deploy-time-learning-the-missing-middle.md) in Commonplace mostly operates through repo-hosted symbolic artifacts, but the repo is a backend choice. A different system could do deploy-time learning through a memory service or database and still remain in the same substrate class.

The taxonomy that falls out:

| Learned result | Substrate class | Backend | Artifact form |
|---|---|---|---|
| AgeMem memory policy | Subsymbolic | Model parameters | Learned policy |
| Trajectory-informed memory | Symbolic artifact | Memory store / DB / files | Tips |
| Commonplace constraining | Symbolic artifact | Repo | Prompts, rules, schemas, tools, tests |

At this level, substrate trade-offs become easier to state. Subsymbolic learning usually buys tighter optimization and gives up inspectability. Symbolic artifact learning usually buys inspectability, diffability, and composability, while depending more heavily on retrieval design, lifecycle management, and governance.

---

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: argues that non-weight adaptation is still learning if it durably changes capacity
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — applies: commonplace's main symbolic-artifact loop, currently implemented mostly through repo-hosted artifacts
- [trace-derived learning techniques in related systems](./trace-derived-learning-techniques-in-related-systems.md) — grounds: already distinguishes promotion targets, but this note separates substrate class from backend and artifact form
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — sharpens: backend choice is downstream of substrate choice
- [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: the core benefit of the symbolic artifact side is inspectability
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a clean subsymbolic case that makes the symbolic/subsymbolic split visible
- [Cognee](./related-systems/cognee.md) — counterexample: database-backed symbolic artifacts show that files are not the only artifact backend
