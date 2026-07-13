---
description: "A synthesis of how LLM-executable methodology becomes system machinery, when that machinery becomes reflexive, and where the analogy to Gödel machines stops"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model]
---

# Actionable theories and reflexive system construction

Some theories do more than explain a class of systems. They also specify distinctions to make, decisions to take, artifacts to produce, and tests to apply. When a capable interpreter can act on such a theory, the theory doubles as a construction mechanism. An LLM is one practical interpreter path: natural-language methodology can produce operational behavior without first being compiled into a separate implementation language—but the prose still requires human authoring and curation, and other interpreters (rule engines, human operators following runbooks) can also apply actionable theory.

The relationship takes three progressively stronger forms—not necessarily strict prerequisites, but increasing demands on self-targeting and verification:

1. **Executable theory.** An interpreter applies a theory to construct or operate some system.
2. **Reflexive executable theory.** The system carrying the theory is among the systems the theory can construct or modify.
3. **Verified reflexive extension.** Candidate modifications are retained only when an applicable oracle accepts them as improvements.

Schmidhuber's [Gödel machine](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html) is the proof-bound limiting case of the third form—as oracles are strengthened toward formal proof, not as a claim of convergence to equivalence: a formally specified self-improving system whose proof searcher may rewrite any part of the machine, including itself, only after proving increased utility. Agent-operated knowledge systems occupy a less formal but often more practically reachable part of the same design space—actionable methodology applied by an interpreter to a mutable self-representation, with improvement bounded by what the system can verify rather than by formal proof.

## From explanation to construction

A theory becomes system machinery when four conditions coincide:

- It is **actionable**: its concepts discriminate cases and imply operations rather than merely naming phenomena;
- An **interpreter** can turn those implications into actions;
- The system has a **mutable representation** the interpreter is authorized to change; and
- Accepted changes have a path to **behavioral effect** in later operation (a retained artifact, an enforced rule, or another change in system behavior traceable to the modification—not merely a one-off interpretation).

Together, these conditions yield a generative rule:

> A theory of system construction becomes part of a system's implementation when an interpreter can apply it to a mutable representation of that system.

"Implementation" here means the mutable surround—context, instructions, tools, and stored knowledge—not the fixed model weights or inference procedure. In an LLM system, prose can fill both explanatory and operational roles because [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md)—a shared representation in which prose can act as both data and instruction: methodology, system description, and instructions can share one representation. The same text may be read as evidence in one call and treated as prescription in another, but that duality is not guaranteed: it depends on prompt framing, and stochastic interpretation can diverge across sessions. The theory has not become deterministic code; at most it changes the conditions for subsequent interpretation rather than rewriting the executing machinery itself.

## Prose and symbolic co-evolution

Agent-operated systems rarely live in prose alone. The [readable pair](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md)—prose and symbolic artifacts updated under shared context and heterogeneous oracles—is the tractable unit for deploy-time improvement. Methodology in notes, instructions, and skills proposes changes; validators, tests, schemas, and package code enforce and execute them. Reflexive construction therefore applies to **both** halves: a theory that recommends new gates but never updates the validator that enforces them, or code that enforces rules no note still endorses, is not self-extending—it is a split implementation.

Commonplace is the local instance: `kb/` carries prose registers; `src/commonplace/` and the review store carry symbolic machinery. Closure under recommendations must span that boundary—when to [codify](./definitions/codification.md) prose into schemas and commands, and when rationale for a symbolic change must be retained in prose.

## Reflexivity requires closure

Executability alone does not make a theory self-extending. A methodology may competently direct the construction of ordinary artifacts while saying nothing about how its own rules, validators, or representations should change.

Reflexivity begins where [a methodology is closed under its own recommendations](./methodology-agent-extensible-only-with-closure-under-recommendations.md). The theory must cover the meta-decisions raised by applying it to itself: which representational form the new artifact should take, how it should be verified, and how it acquires authority over subsequent behavior. At that point, the theory can propose changes to the machinery through which the theory itself operates—subject to whatever oracles and authority paths the system actually supplies.

Closure is not all-or-nothing. A methodology may be closed for adding a validator but open for changing its quality goals; closed for revising instructions but open for deciding who may approve them. Its self-extension frontier is the first consequential meta-decision for which it supplies neither a rule nor an oracle.

## The Gödel-machine correspondence

The structural correspondence is:

| Gödel machine | Agent-operated knowledge system |
|---|---|
| Axiomatic self-description | Methodology, system descriptions, schemas, and instructions |
| Utility function | Purpose, quality goals, and acceptance criteria |
| Proof searcher | Agents and improvement workflows |
| Candidate rewrite | Proposed note, rule, validator, skill, or code change |
| Proof of increased utility | Tests, validators, semantic review, experiments, and human judgment |
| Executed self-rewrite | Retained artifacts that govern later agent behavior |

The correspondence is architectural, not an equivalence. A Gödel machine has a formal proof system and an explicit utility function. A knowledge system generally has plural, partly stated objectives and heterogeneous oracles of unequal strength. It may modify the context, instructions, tools, and stored knowledge surrounding a fixed model rather than rewrite the model itself. Its changes are governed repository transitions, not necessarily autonomous modifications of a running controller. Nothing in the analogy grants global optimality.

The two systems fail in opposite directions. A Gödel machine cannot use an improvement whose value it cannot prove, even when the improvement is real; this is an explicit limitation of the proposal ([Schmidhuber, 2003](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html)). An LLM-mediated system can act on semantic, empirical, or human judgment where proof is unavailable, but may accept changes that only appear beneficial. It exchanges proof-bound reach for fallible reach.

## The verification boundary

The Gödel-machine comparison makes the oracle impossible to treat as an afterthought. Self-description and an interpreter can generate candidate modifications indefinitely; neither establishes that the modifications are improvements. The effective reach of reflexive construction is therefore bounded by what the system can evaluate—the same structural limit named in [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) and graded by [oracle strength](./oracle-strength-spectrum.md) (how decisively a verification method can accept or reject changes).

Retained [design rationale](../reference/design-rationale-management.md)—decision records that capture constraints, alternatives, and acceptance reasons—may inform this loop prospectively, delimiting candidate changes and selecting verification methods when authors carry them forward explicitly; the reference surfaces support retention but do not guarantee end-to-end continuity or reliable agent mining of rationale on each pass.

A further risk arises when the same theory generates a change and supplies the only judgment of that change: the loop may become self-confirming—the reflexive analogue of the oracle gap [automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) names. Deterministic tests, observations from an external environment, independent review contexts, and human authority do not provide formal proof, but they can prevent proposal and acceptance from collapsing into one act. In a proof-relaxed system, separation and diversity of verification may compensate partly for the missing theorem prover when oracles are decorrelated and above chance, following the same logic as [error correction with decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md)—but no degree of compensation is guaranteed here.

The practical analogue of a Gödel machine is therefore not simply a system that edits itself. It is a system in which self-description, actionable methodology, a change mechanism, an authority path, and verification form a closed—but revisable—loop.

## Open questions

- **TODO:** Record a worked Commonplace example when one occurs in maintenance work: a prose change and a symbolic change that co-evolved (note/skill plus validator, schema, or CLI command), one verification step, and one later behavior change traceable to both—grounding the readable-pair loop in observed practice rather than architectural analogy alone.

---

Sources:

- Schmidhuber, J. (2003). [Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html).

Relevant Notes:

- [Design rationale management](../reference/design-rationale-management.md) — see-also: locates the descriptive field whose retained decision structures may inform reflexive construction when authors carry rationale forward explicitly
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: the retained-artifact loop is deploy-time learning framed as reflexive executable theory
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — extends: names the practical near-term substrate for verified reflexive extension under heterogeneous oracles
- [Ingest: Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) — evidence: modern inspectable-scaffold self-improvement in Schmidhuber's lineage at benchmark-oracle strength