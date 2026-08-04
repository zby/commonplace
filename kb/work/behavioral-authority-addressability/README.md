# Behavioral-authority addressability audit

## Goal

Test the working claim that Commonplace makes its repository-defined behavioral authority completely addressable to its human–agent process. The aim is not to confirm the claim. Find the strongest coverage the repository supports, and actively look for an authority-bearing artifact or relation that the process cannot identify, inspect, criticize, or selectively revise.

This workshop continues the [self-revision design-space workshop](../self-revision-design-space/README.md) after the article replaced “recursive targetability” with complete addressability of behavioral authority. It supplies the evidence audit requested by [Reflective self-improvement](../../articles/reflective-self-improvement.md) and its companion, [What makes human-inclusive self-revision non-trivial?](../../articles/what-makes-human-inclusive-self-revision-non-trivial.md).

## Important starting uncertainty

The current [behavioral-authority definition](../../notes/definitions/behavioral-authority.md) decomposes an artifact's behavior-shaping use into **consumer, channel, and force**. Treat that decomposition as preliminary, not exhaustive.

If a real authority path cannot be described adequately with those elements, record the mismatch in this workshop. Do not force the case into the existing vocabulary and do not silently extend the durable definition. For each candidate addition or decomposition change, preserve:

- the concrete case that exposes the gap;
- what consumer, channel, and force fail to distinguish;
- the additional element or relation the case appears to require;
- whether it belongs inside behavioral authority or in a neighbouring concept such as representation, scope, operativity, warrant, dependency, or lifecycle;
- what difference the addition would make to the addressability claim or its test.

One discriminating case is more valuable than an ungrounded catalogue of possible dimensions.

## Where the audit landed

The representative audit is complete in this workshop:

- [Hard-path audit](./audit.md) — six case files covering global goals, the explanatory-reach criterion and its evaluator path, tag-README validation, the revision lifecycle, model bindings, and maintainer admission authority.
- [Synthesis](./synthesis.md) — strongest supported claim, counterexample, decomposition result, stable/provisional distinctions, and article-ready wording.

The result is broad but incomplete addressability. Commonplace makes the canonical artifacts and most intended consumer relations in the examined paths inspectable and selectively revisable, with demonstrated operative reuse for natural-language and symbolic machinery. The strongest unresolved path is the generic maintainer admission relation: the repository names designated maintainers and some path-specific approval requirements, but does not represent who is designated, the scope of that grant, or a generic admission condition bound to the installed content version.

The audit also found one evidence-driven candidate addition to the behavioral-authority decomposition: **applicability scope** — which target cohort or operation receives the force, under which trigger. Authorization provenance, requested-to-realized binding, and revision-closure dependencies remain neighbouring governance, operativity, and lineage records rather than further fields of behavioral authority.

Promotion was outside this workshop's authorization, so the articles and durable definition remain unchanged.

## Audit brief

Fill this workshop with a compact, evidence-grounded audit of Commonplace's hardest repository-defined authority paths.

Start by reading:

- [Behavioral authority](../../notes/definitions/behavioral-authority.md)
- [Reflection buys addressability](../../notes/reflection-buys-addressability.md)
- [A repeatable operative path keeps a redesign class open to revision](../../notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md)
- [The declared Commonplace frame](../../reference/commonplace-declared-frame.md)
- [Reflective self-improvement](../../articles/reflective-self-improvement.md)
- [What makes human-inclusive self-revision non-trivial?](../../articles/what-makes-human-inclusive-self-revision-non-trivial.md)
- the current artifacts in the [self-revision design-space workshop](../self-revision-design-space/README.md)

Choose the working format after inspecting the cases. A table is useful only if the cases share stable fields; use prose case files where a table would hide a moving boundary. Keep the audit economical—roughly five to seven discriminating paths rather than a repository-wide enumeration. Candidate hard cases include objectives and quality criteria, evaluators and review criteria, maintainer admission or merge authority, revision methods, validators and executable code, and model bindings. Replace these candidates if inspection reveals more informative cases.

For each examined path, establish as much of the following as the evidence supports:

- the operative artifact or represented relation;
- the current behavioral-authority decomposition, including consumer, channel, and force;
- where that path is represented and which parts remain tacit or reconstructed;
- which addressability operations are demonstrated, merely supported, or unestablished;
- the applicable route for criticizing and revising it;
- how an accepted successor enters a live behavioral path;
- whether that revision route remains usable after the successor is installed;
- the repository evidence and the strongest missing edge.

Search directly for a counterexample. File writability is not sufficient, and an undocumented maintainer intervention is not a retained revision affordance. Pay particular attention to tacit human judgment, authority allocation, evaluator validity, relationships represented only implicitly in code or convention, and anything whose physical location is known while its semantic role is not.

Keep these claims separate throughout:

- complete addressability is coverage over repository-defined behavioral-authority paths;
- continuity asks whether a named operative revision path remains usable after a transition;
- warrant asks why adopting the successor was better than continuing with the incumbent;
- operativity requires the successor to affect later behavior;
- reuse, leverage, and compounding require later evidence.

Do not reintroduce “recursive targetability.” Repetition belongs to the self-revision process, not to addressability. Do not reuse “revision closure” for this property; the parent workshop already uses that phrase for the dependency surface affected by a change.

Before stopping, leave a synthesis in this directory that states:

1. the strongest addressability claim the evidence currently supports;
2. the strongest counterexample or unresolved authority path;
3. any evidence-driven additions or revisions proposed for the behavioral-authority decomposition;
4. which distinctions are stable and which remain provisional;
5. the exact wording the articles could responsibly use.

Work only in this workshop unless the maintainer asks for promotion. Preserve unrelated working-tree changes, use `apply_patch` for file edits, validate any typed artifacts you create, and do not commit.

## Evaluation boundary

- Use [Commonplace's declared frame](../../reference/commonplace-declared-frame.md): repository and operative artifacts, consuming software and agents, and designated maintainers in their established roles are inside; provider weights, inference infrastructure, and hosting are outside.
- “Complete” is relative to the repository-defined organization inside that frame. It does not imply that tacit human expertise is readable.
- Distinguish declared possibility, structurally supported revision, demonstrated operative change, and routinely exercised revision.
- Do not infer absence in other research systems from papers that report only their experimental paths; this workshop audits Commonplace.

## What closes this workshop

The workshop closes when representative hard paths have been examined, the strongest counterexample has been pursued, changes required by any decomposition gap have been identified, and the resulting claim can be promoted to the article or durable theory. Exhaustive proof that no unrepresented authority exists is not required. On closure, extract durable conclusions and delete this directory.
