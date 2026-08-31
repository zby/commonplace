# Program-article review residuum — 2026-08-30

This report records the deeper issues left deliberately unresolved by the focused review of [A research program for learning software factories](../../articles/a-research-program-for-learning-software-factories.md). The accompanying article patch takes only changes that are clearly precision fixes: it softens the historical claim about Naur, explains how the article's implementation-role table relates to the proposal-selection and residue decompositions, narrows the evidential reading of the Commonplace episode, and removes rhetoric that overstates closure of the reflective loop.

The questions below are not defects that should be patched by wording alone. Each can change the research program's ontology, experiment design, or success criteria, so they should be resolved through dedicated investigation or explicit operator choice.

## 1. What is the minimum operational threshold for a retained theory?

The program contrasts revisable theory with rules, skills, episodic records, and weights, but it does not yet give a classification test sharp enough to decide borderline cases prospectively. A causal rule with a stated scope may already look theory-like; an ADR can contain purpose and dependency structure; a skill with applicability conditions may support more than one downstream decision.

A useful eventual threshold may require some combination of:

- a project-specific mechanism, dependency, purpose, or invariant rather than only a local prescription;
- explicit applicability conditions or scope;
- consequences for more than one possible decision, prediction, or branch;
- a shared revision target such that later evidence can alter one retained object and thereby change several downstream choices.

But adopting such a threshold would be substantive. It could reclassify neighbouring systems currently described as retaining rules rather than theory. Before changing the article, the workshop should test the proposed threshold against Prime Agent, Recuris, workspace optimization, ADR-style rationale, small causal models, and deliberately minimal synthetic examples.

A related distinction may be useful:

1. **theory-shaped state** — retained content has mechanism, dependency, purpose, or scope structure;
2. **theory mediation** — changing that state changes search, diagnosis, evaluation, or recovery;
3. **theory learning** — evidence revises the same state;
4. **theory advantage** — the pathway outperforms an appropriate control.

The current evidence ladder partly covers 2–3, but not the category boundary in 1 or comparative claim in 4.

## 2. Should the program expose a nested hypothesis ladder?

The central research question currently bundles several increasingly strong claims. They can fail independently:

- **H1 — mediation:** with model, symbolic state, tools, task, and budget fixed, changing retained theory changes search, diagnosis, recovery, or the realized modification;
- **H2 — read-back:** independent or delayed outcomes produce selective revision of the same retained theory state;
- **H3 — recurrence:** the revision changes a later structurally related operation;
- **H4 — comparative advantage:** the pathway improves recovery, sample efficiency, collateral-change control, human effort, or total cost relative to raw history, direct search, stronger-model, or other relevant baselines;
- **H5 — outgrowth:** the process increasingly produces and revises its own theories, decompositions, checks, and selection machinery while bespoke human effort falls and transfer extends beyond anticipated domains.

This hierarchy could make disagreement more productive: a researcher might accept H1–H3 and reject H4, or demonstrate H1 while failing to find H2. But introducing named hypotheses would change the article's exposition and perhaps the workshop's shared model. It should therefore be designed deliberately rather than inserted as a review fix.

## 3. The fact-matched control is still a bundled intervention

The proposed experiment compares a reference theory, a fact-matched record with theory-level organization removed, theory withheld, and wrong theory. The article correctly says the record is matched on facts rather than information: removing purposes and dependency relations removes information too.

That means a positive result against the fact-matched record can conflate several mechanisms:

- relational or causal structure;
- compression;
- salience;
- context length and retrieval cost;
- editorial synthesis;
- explicit applicability conditions;
- theory-level organization as such.

A cleaner primary experiment may need a synthetic or semi-synthetic task family generated from a known latent rationale graph. Candidate arms include:

1. correct structured theory;
2. the same atomic propositions with relations removed or shuffled;
3. raw episodes/history;
4. theory withheld;
5. one controlled wrong premise while the rest of the theory is correct;
6. append-only theory that cannot reject or rescope old commitments;
7. an evaluator-ablation arm that retains addressability but weakens reach-assessment.

The single-premise corruption is especially attractive because it permits a preregistered negative-transfer prediction. Still, this design changes the experiment materially and should be worked out as its own protocol rather than patched into the article in passing.

## 4. The several decompositions need a canonical mapping

The article uses four current implementation roles. Elsewhere the workshop has:

- proposal-selection: search, reject-capable evaluation, operative retention;
- residue analysis: representation, settlement/semantic application, verification, continuity, with authority possibly separate;
- shared-model operations: retained project state, model-mediated semantic operation, independently executed symbolic operation, independent exposure/read-back;
- representational forms: natural-language, symbolic, distributed-parametric.

The obvious article fix is only to state that these answer different questions. The deeper issue is whether the workshop should maintain an explicit mapping table and declare one decomposition canonical for each analytical purpose. Without that, future notes can accidentally derive architecture from implementation history or compare unlike partitions.

A likely resolution is:

- **proposal-selection** owns update-loop anatomy;
- **residue classes** own reasons warranted transfer stops;
- **functional architecture** owns current implementation responsibilities and failure surfaces;
- **representational form** owns encoding and consumption.

But this should be checked against the shared model, target problems, closure work, and current note titles before being made doctrine.

## 5. "Theory fit" may still combine several selection questions

The truth-versus-fit distinction is valuable, but global fit currently covers several judgments that may have different evidence:

- theoretical integration — what a claim explains, contradicts, supersedes, or depends on;
- explanatory reach — whether its claimed mechanism and scope are genuine;
- instrumental learning value — whether retaining it improves later search or revision at acceptable cost;
- operational utility — whether using it improves the current system;
- admission priority — whether it is worth retrieval and maintenance cost;
- authorization — whether the system may install or act on it.

Collapsing these back into one global-fit evaluator would recreate the missing oracle under a broad name. A future cleanup may need at least four coordinates: epistemic warrant, theoretical integration, learning value, and authorization. Reach-assessment would remain one epistemic subproblem, not a synonym for fit.

This is deeper than an editorial split because current notes and operator judgments may already use "fit" in several of these senses.

## 6. Scaling and abandonment conditions need operational denominators

The current abandonment conditions are directionally good but not yet measurement protocols. Examples of possible operationalizations:

- replace "more computation does not improve useful search" with an outcome frontier over inference/search compute under fixed total-cost accounting;
- measure human minutes or interventions per accepted useful revision, normalized by maintained capability scope, rather than corpus size alone;
- treat a new domain-specific ontology as failure only when a person must design the ontology and evaluator before computational learning can begin — a general learner may legitimately construct domain-specific representations itself;
- define comparable total cost to include model use, retrieval, context, theory construction, validation, maintenance, recovery, and human work.

These choices will strongly shape any Bitter-Lesson claim and should be agreed before the longitudinal study is interpreted.

## 7. The Commonplace longitudinal study needs production-time instrumentation

Git can establish artifact changes and later ancestry, but it cannot reconstruct discarded model context, branch alternatives, or the operator correction that changed a decision. The next evidence episode should therefore retain enough information at production time to identify the claimed causal path.

A minimal event schema might assign stable identifiers to:

- task episode;
- theory-state version;
- theory components actually supplied to the deciding call;
- candidate and accepted changes;
- evidence event;
- operator intervention;
- resulting theory revision;
- later operation claimed to depend on it.

This would make "causally co-indexed" an executable recording requirement. The open question is how much trace detail is needed without making the research machinery itself dominate the process.

## 8. The program statement and Bitter Lesson article still overlap

The program article currently carries a substantial portion of the companion article's full argument: production method versus representation, bootstrap versus scaffold, computation already inside the loop, operator judgments becoming machinery, domain-extensibility, and abandonment conditions.

Some overlap is necessary because the scaling challenge constrains the program. But the current division may still impose synchronization cost and dilute the program article's center. A later editorial pass could keep only:

1. the narrow production-method/form distinction;
2. the reason theory-guided bootstrapping is the first strategy;
3. the requirement that present machinery remain challengeable and computational production expand;
4. abandonment conditions.

The companion would carry the detailed Bitter Lesson argument and Sutton comparison. This is intentionally deferred because article boundaries are an exposition decision, not a correctness fix.

## 9. What should stay fixed in a reflective improvement loop?

The article now avoids saying that a reflective loop literally has "no outside". The deeper problem remains: if objectives, authorization, evaluator machinery, representations, and the update procedure can all in principle be revised, what supplies stability and warrant while those mechanisms are under change?

The existing machinery-by-warrant note replaces exemption by position with assessed persistence, but this may still require a minimal trusted kernel, reversible update protocol, governance rule, or external adoption "no". The workshop should distinguish:

- components outside the declared revision surface by current scope;
- functions that are externally supplied by category, such as objectives or commitments;
- components inside the surface but not yet computationally revisable;
- components currently revisable with sufficient warrant.

This question may matter more to eventual autonomous self-improvement than to the first theory-mediation experiment, so it should not block the immediate study.

## Priority

The highest-leverage deeper work appears to be:

1. define and adversarially test the minimum theory-state threshold;
2. design the stronger synthetic intervention protocol, including controlled relation and premise ablations;
3. decide whether to expose the nested H1–H5 hypothesis structure;
4. define prospective longitudinal instrumentation before the next Commonplace episode;
5. only then refine global-fit taxonomy, scaling metrics, and article boundaries.

The article is already strong enough to expose these as research questions. Prematurely resolving them in prose would make the program look cleaner while reducing what the experiments are allowed to teach us.
