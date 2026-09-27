# Assigned-tag issues

Initial inventory: 67 reviewer mismatch proposals and one uncertain judgment. Current status: 68 resolved (36 assignments retained, 32 corrected); none open. Follow the [workshop framing](./README.md) for disposition and closure. Issue IDs remain stable after edits. Fifteen findings depend on a parent–child decision, including two additional llm-reliability cases found during disposition; they are included in these 68.

## TP-001 — context-engineering

- Status: resolved — retagged.
- Note: [A citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22771](../../reports/state/review-jobs/review-job-8790/pair-4-a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).

Reviewer reason: “Fidelity is fixed at ingest” concerns provenance and source grounding. It does not substantively address routing, loading, scoping, or assembling knowledge for a bounded call.

Disposition (2026-09-26): The finite context window motivates lossy capture, but the developed mechanism governs citation fidelity and recapture, not knowledge loading. Replace context-engineering with claims-and-grounding and its kb-maintenance parent. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-002 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [A claim's warrant does not determine its fit in a working theory](../../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 22773](../../reports/state/review-jobs/review-job-8790/pair-6-a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md).

Reviewer reason: The note discusses claim fit in working theories generally. It does not substantively ask whether or how a system makes evidence-responsive changes to its own organization.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: the note distinguishes warrant from the role a retained claim earns in a revisable working theory. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-003 — learning-theory

- Status: resolved — assignment retained.
- Note: [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-06](./parent-child-relations.md#pc-06).
- Local evidence: [review pair 22779](../../reports/state/review-jobs/review-job-8790/pair-12-a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md).

Reviewer reason: “A procedure is a goal compiled away” and the workaround budget explain execution failure, not how a system learns, verifies, or improves through retained change.

Disposition (2026-09-26): Retain learning-theory through llm-reliability: the body explains hidden deviation, correction costs, and semantic checks for goal-holding interpreters. Learning through retained change is not an additional requirement. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-004 — computational-model

- Status: resolved — retagged.
- Note: [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22785](../../reports/state/review-jobs/review-job-8790/pair-18-a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

Reviewer reason: “The decomposition specifies what the loop must accomplish, not a sequence, a component diagram, or a division of labour.” It is a general learning architecture, not LLM call execution or orchestration.

Disposition (2026-09-26): remove computational-model. The three functions define candidate search, reject-capable evaluation, and operative retention across human and computational systems. They do not explain bounded-call execution. Keep improvement-loop and its parent areas. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-005 — context-engineering

- Status: resolved — retagged.
- Note: [A retained instruction preserves what testing selected](../../notes/a-retained-instruction-preserves-what-testing-selected.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22788](../../reports/state/review-jobs/review-job-8791/pair-1-a-retained-instruction-preserves-what-testing-selected.md).

Reviewer reason: “Retaining the winner commits that evaluated choice for reuse” concerns selection and operative retention. It does not address routing, loading, scoping, context budget, or a storage choice made for later loading; the context-engineering inclusion condition is unmet.

Disposition (2026-09-26): Testing selects a candidate procedure and retention makes the evaluated choice reusable outside weights. Replace context-engineering with improvement-loop and continual-learning, plus self-improving-systems and learning-theory. No loading mechanism is developed. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-006 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Abstract an experience into a lesson only when you can state where the lesson stops](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22792](../../reports/state/review-jobs/review-job-8791/pair-5-abstract-an-experience-only-when-you-can-state-the-boundary.md).

Reviewer reason: The episode-to-lesson test and SkillRL examples do not discuss deployed software meeting users, surprising needs after release, or what use reveals beyond design and testing; the tag’s phenomenon is absent.

Disposition (2026-09-26): retain deploy-time-learning. The opening makes the episode-to-lesson decision its subject; the success/failure comparison and boundary test govern how an agent responds to experience without installing an overgeneral rule. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-007 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Ad hoc prompts extend the system without schema changes](../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22797](../../reports/state/review-jobs/review-job-8791/pair-10-ad-hoc-prompts-extend-the-system-without-schema-changes.md).

Reviewer reason: “When a requirement doesn’t fit existing code or configuration” describes extension, but does not establish the tag’s post-release encounter with users, surprising needs, or what deployment reveals; the deployment example is only one possible prompt use.

Disposition (2026-09-26): retain deploy-time-learning. The body explains how prompts absorb requirements that no longer fit the existing deterministic base, then how recurring responses mature into reusable skills. The KB collections case is a worked response to a need encountered in use. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-008 — architecture

- Status: resolved — assignment retained under revised scope.
- Note: [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md).
- Head: [architecture](../../tags/architecture-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22819](../../reports/state/review-jobs/review-job-8792/pair-12-agent-runtime-analysis-should-separate-scheduling-context-state.md).

Reviewer reason: The note analyzes generic agent runtimes and practitioner mappings; it does not substantively address Commonplace repository structure, installation, AGENTS.md control plane, or file-storage decision required by this head.

Disposition (2026-09-26): Retain architecture under the revised general head, superseding the removal under its old Commonplace-only scope. The note separates runtime responsibilities and explains why those boundaries locate failures. Keep the accepted context-engineering addition and computational-model. It does not qualify for commonplace-architecture. See the [architecture split](./architecture-placement-decision.md) for the operator decision, membership check, input versions, and verification.

## TP-009 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [An agentic substrate becomes a software factory through family-specific production machinery](../../notes/agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-03](./parent-child-relations.md#pc-03).
- Local evidence: [review pair 22820](../../reports/state/review-jobs/review-job-8792/pair-13-agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md).

Reviewer reason: “the mapping does not imply learning”; revision by agents is only an optional additional capability. The note does not address operative, evidence-responsive change to the system’s own organization.

Disposition (2026-09-26): Retain self-improving-systems through software-factory: the note defines the family-specific machinery that makes an agentic substrate a factory and explicitly separates factory construction from learning. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-010 — architecture

- Status: resolved — assignment retained under revised scope.
- Note: [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md).
- Head: [architecture](../../tags/architecture-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22825](../../reports/state/review-jobs/review-job-8792/pair-18-always-loaded-context-mechanisms-in-agent-harnesses.md).

Reviewer reason: The note surveys cross-platform harness context mechanisms; the Commonplace installation example is incidental. It does not substantively address Commonplace’s repository structure, installed library, AGENTS.md control plane, or file-storage decision.

Disposition (2026-09-26): Retain architecture and add commonplace-architecture. The survey compares architectural context surfaces, and its configuration-injection section develops a Commonplace installation example. Keep the accepted context-engineering and agent-memory additions, with learning-theory as the latter's parent. See the [architecture split](./architecture-placement-decision.md) for the operator decision, membership check, input versions, and verification.

## TP-011 — continual-learning

- Status: resolved — tag removed.
- Note: [An optimal long-run learning strategy invests in its own machinery](../../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).
- Head: [continual-learning](../../tags/continual-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22833](../../reports/state/review-jobs/review-job-8793/pair-6-an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

Reviewer reason: The note leaves the machinery and its retention form unspecified; it does not substantively address continued learning through retained changes outside model weights, the head’s inclusion condition.

Disposition (2026-09-26): Remove continual-learning. The return on persistent improvements to learning machinery is developed without specifying retained non-weight artifacts. Keep learning-theory and self-improving-systems, and move the curated route to the latter head. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-012 — artifact-analysis

- Status: resolved — tag removed.
- Note: [An artifact must preserve the scope of each named system choice](../../notes/artifacts-must-preserve-named-choice-scope.md).
- Head: [artifact-analysis](../../tags/artifact-analysis-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22836](../../reports/state/review-jobs/review-job-8793/pair-9-artifacts-must-preserve-named-choice-scope.md).

Reviewer reason: The note does not define, extend, test, or draw a design consequence from the substrate/form/lineage/authority scheme; its subject is proposition scope and document placement.

Disposition (2026-09-26): Remove artifact-analysis and keep document-system. The argument establishes reference/range and role obligations for propositions, then uses them to decide document placement. Guaranteed context matters to claim interpretation, but the note does not derive a design consequence from storage substrate, representational form, source/derivation status, or consumer/channel/force. Its link to an artifact-classification note is supporting context rather than an application of a classification field. See [single-field scope decision](./artifact-analysis-scope-decision.md) for the operator decision and verification.

## TP-013 — computational-model

- Status: resolved — retagged.
- Note: [Backtracking keeps lightweight search control provisional](../../notes/backtracking-keeps-lightweight-search-control-provisional.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22842](../../reports/state/review-jobs/review-job-8793/pair-15-backtracking-keeps-lightweight-search-control-provisional.md).

Reviewer reason: The note does not explain LLM call execution, scheduling, scoping, or orchestration; its “return path” is a general search-recovery condition.

Disposition (2026-09-26): remove computational-model. The return path preserves a provisional search choice across artifacts, plans, or theories; it supplies no LLM execution or scheduling mechanism. Keep improvement-loop and its parent areas. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-014 — constraining

- Status: resolved — tag removed.
- Note: [The bitter lesson selects against unearned reach, not against structure](../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md).
- Head: [constraining](../../tags/constraining-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22843](../../reports/state/review-jobs/review-job-8793/pair-16-bitter-lesson-selects-against-unearned-reach-not-against-structure.md).

Reviewer reason: The note discusses structure, formalization, and exactness as examples, but never explains or decides when to narrow the interpretations an artifact admits.

Disposition (2026-09-26): Remove constraining. The argument concerns whether tests earn a generalization's claimed reach, not narrowing or widening an artifact's valid interpretations. Formalization and exactness are cases in that warrant argument. Keep learning-theory, self-improving-systems, and continual-learning for the developed defense of learning in retained readable forms. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-015 — context-engineering

- Status: resolved — retagged.
- Note: [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22848](../../reports/state/review-jobs/review-job-8794/pair-1-brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md).

Reviewer reason: “Prompt rewrite selection” is a benchmark candidate, and “useful in context engineering” names an application; the note does not substantively address routing, loading, scoping, or scheduling knowledge into bounded calls.

Disposition (2026-09-26): Prompt rewrites are one proposed benchmark. The experiment concerns judge discrimination, variance, bias, and correction of selection errors, so keep evaluation and llm-reliability, remove context-engineering, and add the learning-theory parent. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-016 — context-engineering

- Status: resolved — retagged.
- Note: [Cheap generation breaks text volume as an effort signal](../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22855](../../reports/state/review-jobs/review-job-8794/pair-8-cheap-generation-breaks-text-volume-as-an-effort-signal.md).

Reviewer reason: “A large artifact can then require more reviewer effort” concerns human inspection cost, with no developed question about getting knowledge into a bounded LLM call.

Disposition (2026-09-26): Text volume is assessed as a triage signal for reviewer effort. This develops neither bounded-context operations nor an LLM deviation or correction mechanism. Replace context-engineering and llm-reliability with evaluation. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-017 — llm-reliability

- Status: resolved — retagged.
- Note: [Cheap generation breaks text volume as an effort signal](../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md).
- Head: [llm-reliability](../../tags/llm-reliability-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22855](../../reports/state/review-jobs/review-job-8794/pair-8-cheap-generation-breaks-text-volume-as-an-effort-signal.md).

Reviewer reason: Cheap generation changes the evidential value of text volume; the note explicitly says this “does not show that the text is false, incorrect, or machine-generated” and does not diagnose or correct an LLM output deviation.

Disposition (2026-09-26): The note expressly separates its triage signal from evidence that an output is false or incorrect. Remove llm-reliability along with context-engineering; evaluation covers what the signal establishes. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-018 — learning-theory

- Status: resolved — assignment retained.
- Note: [Code complements the weight–prompt pair with independently executed symbolic operations](../../notes/code-complements-weight-prompt-with-symbolic-operations.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-02](./parent-child-relations.md#pc-02).
- Local evidence: [review pair 22861](../../reports/state/review-jobs/review-job-8794/pair-14-code-complements-weight-prompt-with-symbolic-operations.md).

Reviewer reason: The note says a model “may generate, select, explain, or revise the code,” but does not develop how a system learns or improves through those changes; its subject is how installed operations execute.

Disposition (2026-09-26): Retain learning-theory through constraining: installing runtime-assigned operations removes model reinterpretation at execution, and the body explains the precision/reliability boundary of that commitment. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-019 — software-factory

- Status: resolved — retagged.
- Note: [Preferential codification concentrates less predictable work at the agent boundary](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md).
- Head: [software-factory](../../tags/software-factory-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22864](../../reports/state/review-jobs/review-job-8794/pair-17-codifying-predictable-choices-leaves-agents-with-less-predictable-work.md).

Reviewer reason: The note's examples concern generic decision cases, agent planning, and later codification. It does not substantively address reusable production machinery for a declared product family, its development, or a software house.

Disposition (2026-09-26): Replace software-factory with constraining. The shift from model interpretation to symbolic enforcement is substantive; a declared product family is absent. Keep computational-model and self-improving-systems: verified later codification changes the system's operative division of work. Add learning-theory through the supported child assignments. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-020 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22872](../../reports/state/review-jobs/review-job-8795/pair-5-constraining-during-deployment-is-continuous-learning.md).

Reviewer reason: “Constraining is one concrete way continuous learning happens outside weights” describes a retained-change mechanism; the note does not substantively analyze what deployed use reveals that design and testing could not, the head's inclusion condition.

Disposition (2026-09-26): retain deploy-time-learning. The note explicitly explains adaptation to new data, tasks, and shifts during deployment through prompts, schemas, tests, and code. It belongs under both deploy-time-learning and continual-learning. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-021 — agent-memory

- Status: resolved — retagged.
- Note: [A context-operation interface bounds the projections its policy can realize](../../notes/context-operation-interface-bounds-context-policy.md).
- Head: [agent-memory](../../tags/agent-memory-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22875](../../reports/state/review-jobs/review-job-8795/pair-8-context-operation-interface-bounds-context-policy.md).

Reviewer reason: “Retained state and active context are different runtime layers” establishes an input distinction, but the note does not substantively ask what persists between sessions or under what retention authority; the agent-memory head requires that question.

Disposition (2026-09-26): Remove agent-memory. Persistence horizons are comparison coordinates, while the question is which active-context projections an interface admits. Keep context-engineering and computational-model; add architecture for operation and controller boundaries and evaluation for the explicit limits on fixed-interface comparisons. No claim about what should persist across sessions or retention authority is developed. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-022 — context-engineering

- Status: resolved — retagged.
- Note: [Cross-task transition policy remains scheduling behind a tool interface](../../notes/cross-task-transition-policy-remains-scheduling-behind-tools.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22880](../../reports/state/review-jobs/review-job-8795/pair-13-cross-task-transition-policy-remains-scheduling-behind-tools.md).

Reviewer reason: Its transitions choose independently steerable goals and control handoff; no substantive claim concerns knowledge reaching a bounded call, context assembly, or scheduling across context windows as the head requires.

Disposition (2026-09-26): The substantive mechanism locates transition authority and interceptable control boundaries. Keep computational-model and add architecture; scheduling independently steerable goals does not by itself establish a bounded-context question. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-023 — learning-theory

- Status: resolved — assignment retained.
- Note: [Behavioral authority](../../notes/definitions/behavioral-authority.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-01](./parent-child-relations.md#pc-01).
- Local evidence: [review pair 22886](../../reports/state/review-jobs/review-job-8795/pair-19-behavioral-authority.md).

Reviewer reason: “Learning input” appears in the list of possible forces, but the note does not explain how systems learn, verify, or improve; the head requires theory about those processes rather than a possible use of an artifact.

Disposition (2026-09-26): Retain learning-theory through artifact-analysis: consumer, channel, and force define an axis of the retained-artifact scheme and explain its path-relative consequences. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-024 — computational-model

- Status: resolved — retagged.
- Note: [Reach-assessment](../../notes/definitions/reach-assessment.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22898](../../reports/state/review-jobs/review-job-8796/pair-11-reach-assessment.md).

Reviewer reason: “Scope” compares semantic, proof, and predictive assessment routes across forms. It does not explain how LLM calls or orchestration execute, the computational-model inclusion condition.

Disposition (2026-09-26): remove computational-model. The definition compares what semantic, formal, and predictive assessment can establish. The prompt-length example tests a generalization, not call execution. Add evaluation and retain theory-builder with its parents. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-025 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [Software factory](../../notes/definitions/software-factory.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-03](./parent-child-relations.md#pc-03).
- Local evidence: [review pair 22903](../../reports/state/review-jobs/review-job-8796/pair-16-software-factory.md).

Reviewer reason: “Core boundary” says the factory label does not imply learning or self-improvement. The note defines family-specific production machinery but does not substantively analyze whether or how it makes evidence-responsive changes to itself.

Disposition (2026-09-26): Retain self-improving-systems through software-factory: the definition supplies the child area's subject and boundaries. Its explicit exclusion of implied self-improvement does not exclude it from that subject area. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-026 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [Tentative theory](../../notes/definitions/tentative-theory.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 22907](../../reports/state/review-jobs/review-job-8796/pair-20-tentative-theory.md).

Reviewer reason: “Independent of the holder” says tentative status holds whatever a system does with the theory. The note does not address whether or how a system makes operative, evidence-responsive changes to its own organization.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: tentative status is defined and distinguished from revision permissions and from the stated theories a builder operates on. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-027 — warranted-autonomy

- Status: resolved — retagged.
- Note: [Disconnected witnesses do not establish a full causal path through theory](../../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md).
- Head: [warranted-autonomy](../../tags/warranted-autonomy-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22917](../../reports/state/review-jobs/review-job-8797/pair-10-disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md).

Reviewer reason: The note's boundary says “The path can cross model, symbolic, environmental, and human components” and discusses evidence of causal learning, but it does not ask which decisions an agent is warranted to take over or measure decision autonomy.

Disposition (2026-09-26): Replace warranted-autonomy with theory-builder. The causal path joins stated theory, criticism, and later operation, while explicitly allowing human and computational components without asserting autonomy. Keep evaluation and self-improving-systems; add learning-theory through theory-builder and its parent. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-028 — discovery

- Status: resolved — assignment retained.
- Note: [Epiplexity by example: what entropy and complexity miss](../../notes/epiplexity-by-example-what-entropy-and-complexity-miss.md).
- Head: [discovery](../../tags/discovery-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22925](../../reports/state/review-jobs/review-job-8797/pair-18-epiplexity-by-example-what-entropy-and-complexity-miss.md).

Reviewer reason: The four measures and worked examples concern extractable pattern and observer capacity. They do not develop formation, testing, acceptance, explanatory reach, or warrant of a conjecture, as the discovery head requires.

Disposition (2026-09-26): Retain discovery under its unchanged inclusion rule for enabling conditions. The bounded-learner examples explain how tools, prior knowledge, and ordering permit or prevent pattern extraction; the AB example distinguishes acquired regularity from irreducible noise. This is substantive work on conditions for recognizing structure, not a claim that extraction establishes explanatory-reach or warrants acceptance. Clarify the curated entry to state this narrower reason. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-029 — claims-and-grounding

- Status: resolved — retagged.
- Note: [A five-link cap missed four grounding findings in twelve reviews](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md).
- Head: [claims-and-grounding](../../tags/claims-and-grounding-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22929](../../reports/state/review-jobs/review-job-8798/pair-2-a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md).

Reviewer reason: “A five-link cap missed four grounding findings” analyzes an LLM gate's reading budget and verdicts, rather than what makes a claim grounded; the head expressly assigns running a grounding check as a gate to review-system.

Disposition (2026-09-26): Replace claims-and-grounding with review-system. The criterion's substantive grounding question is held fixed while its linked-reading budget changes. The outcome table names detected grounding defects but does not develop a separate account of what constitutes support. Keep evaluation and kb-maintenance, and move the curated entry to review-system. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-030 — computational-model

- Status: resolved — retagged.
- Note: [Commonplace as a reflective self-improving system](../../notes/evidence/commonplace-as-a-reflective-system.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22930](../../reports/state/review-jobs/review-job-8798/pair-3-commonplace-as-a-reflective-system.md).

Reviewer reason: “The full mapping locates problem selection, semantic evaluation, and adoption with the maintainer” reports actor allocation. It does not explain instruction interpretation, call state, tool loops, or orchestration mechanisms required by this head.

Disposition (2026-09-26): remove computational-model. The Commonplace trace establishes reflective coverage and actor allocation through a retained change. It does not develop LLM execution semantics. Add improvement-loop for the documented search, evaluation, and retention mapping. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-031 — artifact-analysis

- Status: resolved — assignment retained.
- Note: [Seven documentation cases left routing and synthesis](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md).
- Head: [artifact-analysis](../../tags/artifact-analysis-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22938](../../reports/state/review-jobs/review-job-8798/pair-11-seven-documentation-cases-left-routing-and-synthesis.md).

Reviewer reason: The “Casebook” compares recoverable prose with source and help, but does not define, test, apply, or draw a consequence from the substrate/form/lineage/behavioral-authority classification scheme required by this head.

Disposition (2026-09-26): Retain artifact-analysis through lineage. The casebook compares prose content with the source or contract that owns the exact facts, identifies discrepancies and maintenance obligations, and uses that dependency analysis to retire, reduce, or retain content. It draws a maintenance consequence from source relationships without needing the other three fields. See [single-field scope decision](./artifact-analysis-scope-decision.md) for the operator decision and verification.

## TP-032 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Exact implementation does not validate a requirement against its objective](../../notes/exact-implementation-does-not-validate-a-requirement.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22947](../../reports/state/review-jobs/review-job-8798/pair-20-exact-implementation-does-not-validate-a-requirement.md).

Reviewer reason: The vision example and “when a hardened link has stopped fitting” concern proxy validity generally. The note does not analyze a released system meeting users, a surprise from use, or the post-release change phenomenon required by this head.

Disposition (2026-09-26): retain deploy-time-learning. The body distinguishes local conformance from whether a requirement serves its objective, then prescribes retracting failed requirement–objective claims, rescoping surviving use, and relaxing hardened links when operation exposes poor fit. This is a generalized response mechanism, not merely a deployment example. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-033 — computational-model

- Status: resolved — retagged.
- Note: [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22960](../../reports/state/review-jobs/review-job-8799/pair-13-formal-systems-assess-explanatory-reach-through-causal-and-proof.md).

Reviewer reason: The note’s “causal route,” “proof route,” and “formalization boundary” concern theory assessment and warrant. It does not explain an LLM-based program’s instruction interpretation, state, tool loop, scheduling, or execution limit, which the computational-model head requires.

Disposition (2026-09-26): remove computational-model. Causal and proof obligations assess a claim inside a formalized domain and expose the translation boundary. That is theory assessment, not an LLM computational limit. Add evaluation and discovery. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-034 — failure-modes

- Status: resolved — retagged.
- Note: [Generation confidence does not by itself certify soundness](../../notes/generation-confidence-does-not-by-itself-certify-soundness.md).
- Head: [failure-modes](../../tags/failure-modes-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22965](../../reports/state/review-jobs/review-job-8799/pair-18-generation-confidence-does-not-by-itself-certify-soundness.md).

Reviewer reason: The failure described is an LLM’s fluent but unsound output and overtrust in generation probability. The note does not analyze a failure caused by how the KB stores, delivers, states, or repairs knowledge, as this tag requires.

Disposition (2026-09-26): Remove failure-modes and add evaluation. The failure is overtrust in generation probability, not KB storage, delivery, or claim repair. Keep llm-reliability and learning-theory; calibration, discrimination, and verifier validation are substantive evaluation questions. See the [remaining-placement disposition](./remaining-placement-decision.md) for versions and verification.

## TP-035 — computational-model

- Status: resolved — retagged.
- Note: [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22966](../../reports/state/review-jobs/review-job-8799/pair-19-goedel-machines-are-a-proof-governed-case-of-self-modification.md).

Reviewer reason: “The change loop” describes a formal self-rewriting machine, and the prompt-editing loop is only a comparison case. The note does not explain how an LLM-based program interprets instructions or runs bounded calls, tools, state, or scheduling, as this head requires.

Disposition (2026-09-26): remove computational-model. The proof-gated self-rewrite construction is not an LLM execution model. The prompt-editing comparison concerns admission warrant, without developing instruction interpretation or bounded-call orchestration. Add improvement-loop for the explicit change-function mapping. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-036 — learning-theory

- Status: resolved — assignment retained.
- Note: [Legal drafting solves the same problem as context engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-02](./parent-child-relations.md#pc-02).
- Local evidence: [review pair 22989](../../reports/state/review-jobs/review-job-8801/pair-2-legal-drafting-solves-the-same-problem-as-context-engineering.md).

Reviewer reason: The “Techniques that transfer” and “Law is rich in constraining” sections compare drafting methods for narrowing interpretation. They do not address learning, verification, memory architecture, or system improvement as the learning-theory head requires; using constraining does not alone establish this broader subject.

Disposition (2026-09-26): Retain learning-theory through constraining: the body compares mechanisms that narrow interpretations, including definitions, precedent, and statutory text, and distinguishes constraining from codification. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-037 — computational-model

- Status: resolved — retagged.
- Note: [Lightweight search control allocates further search without licensing adoption](../../notes/lightweight-search-control-does-not-license-adoption.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22990](../../reports/state/review-jobs/review-job-8801/pair-3-lightweight-search-control-does-not-license-adoption.md).

Reviewer reason: “Lightweight names the judgment's authority, not its cost, formality, or confidence.” The note defines an improvement judgment's consequence, without explaining LLM execution mechanisms, state, scheduling, or bounded calls required by this head.

Disposition (2026-09-26): remove computational-model. The claim distinguishes authority to allocate search from authority to adopt. It explicitly leaves the allocation mechanism unspecified. Keep improvement-loop and its parent areas. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-038 — methodology

- Status: resolved — assignment retained.
- Note: [Literature reuse can reverse a paper’s hierarchy of contributions](../../notes/literature-reuse-can-reverse-a-papers-hierarchy-of-contributions.md).
- Head: [method-guided-action](../../tags/method-guided-action-README.md), renamed from methodology.
- Initial reviewer judgment: uncertain.
- Local evidence: [review pair 22997](../../reports/state/review-jobs/review-job-8801/pair-10-literature-reuse-can-reverse-a-papers-hierarchy-of-contributions.md).

Reviewer reason: “Ingestion should also ask what distinctions the authors had to construct” is guidance for selecting reusable conceptual machinery. The head requires a methodology an agent holds and applies; an operator must decide whether adopting an ontology for classification counts as adopting a method, or whether this is solely literature analysis.

Disposition (2026-09-26): retain the assignment under the renamed method-guided-action tag. The note supplies a method for selecting and checking reusable conceptual distinctions during literature ingestion; it need not establish that every ontology is itself a methodology. See the [methodology disposition](./methodology-scope-decision.md) for the boundary, input versions, and verification.

## TP-039 — constraining

- Status: resolved — retagged.
- Note: [LLM↔code boundaries are natural checkpoints](../../notes/llm-code-boundaries-are-natural-checkpoints.md).
- Head: [constraining](../../tags/constraining-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22998](../../reports/state/review-jobs/review-job-8801/pair-11-llm-code-boundaries-are-natural-checkpoints.md).

Reviewer reason: The only application is a refactoring bullet about logic moving “between a prompt and code through constraining.” The note does not explain, test, or decide when to narrow valid interpretations; the term is background to checkpointing.

Disposition (2026-09-26): Replace constraining with llm-reliability. The main mechanism is exposing and checking arguments at a boundary; deterministic execution does not correct a wrongly interpreted argument. The brief refactoring application does not analyze interpretation-space narrowing. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-040 — learning-theory

- Status: resolved — assignment retained.
- Note: [LLM↔code boundaries are natural checkpoints](../../notes/llm-code-boundaries-are-natural-checkpoints.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 22998](../../reports/state/review-jobs/review-job-8801/pair-11-llm-code-boundaries-are-natural-checkpoints.md).

Reviewer reason: The “Debugging” and “Testing” operations concern locating a defect in one execution. The note does not substantively explain learning, retained capacity change, or a verification mechanism for learning as this head describes.

Disposition (2026-09-26): Retain learning-theory through the corrected llm-reliability assignment (TP-039 / ADD-110). Checks against intent, replay, and the count=3 example substantively diagnose output deviations. The reviewer imposed an extra learning-through-retention condition. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-041 — computational-model

- Status: resolved — retagged.
- Note: [Memory-backed personalization can look like model improvement](../../notes/memory-backed-personalization-can-look-like-model-improvement.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23017](../../reports/state/review-jobs/review-job-8802/pair-10-memory-backed-personalization-can-look-like-model-improvement.md).

Reviewer reason: The note identifies retention, activation, and model use as diagnostic stages but does not explain or compare how bounded calls, instruction interpretation, state, or orchestration execute. The computational-model head requires an execution mechanism or computational limit, rather than a model being one component in a comparison.

Disposition (2026-09-26): remove computational-model. The note separates retained intent, activation, and use, then designs crossed model/memory comparisons. It diagnoses missing information and intervention effects without developing interpreter semantics or call execution. Add context-engineering and evaluation; retain agent-memory and llm-reliability. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-042 — context-engineering

- Status: resolved — retagged.
- Note: [Mixed epistemic status must be preserved below the document level](../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23023](../../reports/state/review-jobs/review-job-8802/pair-16-mixed-epistemic-status-must-be-preserved-below-the-document-level.md).

Reviewer reason: The proposed tests vary output and process structure, but the note does not discuss getting knowledge into a bounded LLM context. The tag head requires routing, retrieval, loading, prompt assembly, scoping, or related context operations.

Disposition (2026-09-26): The note preserves separate warrant for observations, deductions, and compatible explanations inside a document. Replace context-engineering with document-system and claims-and-grounding, plus kb-maintenance; keep evaluation. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-043 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [Naur's human-only conclusion needs more than the absence of explicit criteria](../../notes/naur-equates-machine-execution-with-formulated-criteria.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-05](./parent-child-relations.md#pc-05).
- Local evidence: [review pair 23028](../../reports/state/review-jobs/review-job-8803/pair-1-naur-equates-machine-execution-with-formulated-criteria.md).

Reviewer reason: The functional tests concern a modifier changing a program across demands. The note does not say the program is the modifier’s own behavior-determining organization or analyze that self-change, which this head requires.

Disposition (2026-09-26): Retain self-improving-systems through warranted-autonomy: the body challenges the inference to human-only judgment and sets tests before assigning that function to computation. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-044 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Naur's compiler case tests one historically bounded documentation-and-consumption system](../../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23029](../../reports/state/review-jobs/review-job-8803/pair-2-naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).

Reviewer reason: A successor group’s failed compiler extension is a theory-transfer case. The note does not substantively address deployment meeting users, surprising needs, or changes that use reveals, as this head specifies.

Disposition (2026-09-26): retain deploy-time-learning. The compiler case concerns a successor group attempting extensions and failing to preserve structure; the argument compares retained rationale and consumption pathways that could support coherent modification across later demands. It evaluates a response capability without requiring the note to describe the original user surprise. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-045 — constraining

- Status: resolved — retagged.
- Note: [Opacity is a scale threshold, not a class property](../../notes/opacity-is-a-scale-threshold.md).
- Head: [constraining](../../tags/constraining-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23032](../../reports/state/review-jobs/review-job-8803/pair-5-opacity-is-a-scale-threshold.md).

Reviewer reason: “Readable” and “opaque” are analyzed as inspection properties. The note does not explain or apply narrowing or deliberate widening of valid interpretations, the constraining head’s condition.

Disposition (2026-09-26): Replace constraining with artifact-analysis. The body qualifies how representational form predicts inspectability at scale; it does not analyze narrowing valid interpretations. The complete artifact-analysis head now links this note. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-046 — learning-theory

- Status: resolved — assignment retained.
- Note: [Opacity is a scale threshold, not a class property](../../notes/opacity-is-a-scale-threshold.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23032](../../reports/state/review-jobs/review-job-8803/pair-5-opacity-is-a-scale-threshold.md).

Reviewer reason: The body compares inspectability of representational forms, but does not substantively analyze accumulation, verification, adaptation, or another learning mechanism required by this head.

Disposition (2026-09-26): Retain learning-theory through the corrected artifact-analysis assignment (TP-045 / ADD-133). Its scale-dependent qualification of representational form meets that child's inclusion rule. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-047 — artifact-analysis

- Status: resolved — assignment retained.
- Note: [Orchestration strategies and run-state have opposite persistence economics](../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md).
- Head: [artifact-analysis](../../tags/artifact-analysis-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23042](../../reports/state/review-jobs/review-job-8803/pair-15-orchestration-strategies-and-run-state-have-opposite-persistence.md).

Reviewer reason: The note compares lifecycle value of two scheduler components. It does not define, extend, test, or draw consequences from the artifact-analysis scheme of substrate, form, lineage, and behavioral authority. Merely retaining code is insufficient for this tag.

Disposition (2026-09-26): Retain artifact-analysis through behavioral authority and its lifecycle consequences. The opening separates task data from the selection logic that controls calls despite their shared symbolic substrate. Those different consumption roles justify checkpointing task state separately from promoting tested control strategies, whose reuse brings provenance, permission, and staleness obligations. See [single-field scope decision](./artifact-analysis-scope-decision.md) for the operator decision and verification.

## TP-048 — computational-model

- Status: resolved — retagged.
- Note: [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23046](../../reports/state/review-jobs/review-job-8803/pair-19-pointer-design-tradeoffs-in-progressive-disclosure.md).

Reviewer reason: Fixed abstracts, query-time snippets, and crafted links determine which knowledge reaches a call. The note does not explain call scheduling, instruction execution, orchestration, or another execution mechanism required by this head.

Disposition (2026-09-26): remove computational-model. The comparison explains which pointer helps select content for loading, with availability and accuracy tradeoffs. It does not explain the execution of the retrieval pipeline or surrounding calls. Replace computational-model with context-engineering and keep links. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-049 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [A theory's prototype standing is its revision cost: external binding plus lost investment](../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 23054](../../reports/state/review-jobs/review-job-8804/pair-7-prototype-standing-is-revision-cost-binding-plus-lost-investment.md).

Reviewer reason: The note discusses theory standing across procedures, audits, contracts, proofs, and models. Its Gödel-machine illustration is an example, but it does not substantively analyze whether or how a system makes evidence-responsive changes to its own behavior-determining organization, the head's inclusion condition.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: the argument explains the costs of revising inspectable theories and how binding and reconstruction constrain later criticism and replacement. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-050 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Retained system-definition artifacts enable persistent deployment-time adaptation](../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23067](../../reports/state/review-jobs/review-job-8804/pair-20-retained-artifacts-enable-persistent-deployment-time-adaptation.md).

Reviewer reason: The head requires substantive treatment of what use after release reveals that design and testing could not. The note's “Lifecycle phase is not update speed” and “Why localized artifacts are practical now” sections classify and justify adaptation machinery; production feedback is an input to the example rather than an analysis of the post-release surprise phenomenon.

Disposition (2026-09-26): retain deploy-time-learning. The note explains how deployment experience drives proposed artifact changes, evaluation selects them, and retention changes later behavior. Human proposal or approval is allowed. The mechanism is now explicitly within the tag. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-051 — artifact-analysis

- Status: resolved — assignment retained.
- Note: [RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence](../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md).
- Head: [artifact-analysis](../../tags/artifact-analysis-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23076](../../reports/state/review-jobs/review-job-8805/pair-9-rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md).

Reviewer reason: The comparison uses substrate and persistence as its own axes, but it does not define, test, or draw design consequences from the artifact-analysis scheme of substrate, form, lineage, and behavioral authority. A persistence comparison alone misses that inclusion condition.

Disposition (2026-09-26): Retain artifact-analysis. The live comparison connects representational form and executable authority to design: generated capabilities change what later sessions can execute rather than only what they can retrieve, and switching prompt/code implementations changes verification and maintenance options. The persistence discussion adds provenance, approval, retirement, and dependency-drift consequences. It does more than list a storage location, and it need not enumerate all four fields. See [single-field scope decision](./artifact-analysis-scope-decision.md) for the operator decision and verification.

## TP-052 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23079](../../reports/state/review-jobs/review-job-8805/pair-12-scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).

Reviewer reason: The proposed frontier gap comes from assigning harder tasks as model capability rises. It does not analyze user needs or surprises revealed after release that force changes, which is this head’s inclusion condition.

Disposition (2026-09-26): retain deploy-time-learning. The argument examines when deployment-specific scaffolding should disappear and when new task demands call for new external structure. Its substantive subject is whether that adaptation response remains useful as models and assigned difficulty change. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-053 — learning-theory

- Status: resolved — assignment retained.
- Note: [Silent disambiguation is the semantic analogue of tool fallback](../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md).
- Head: [learning-theory](../../tags/learning-theory-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-06](./parent-child-relations.md#pc-06).
- Local evidence: [review pair 23088](../../reports/state/review-jobs/review-job-8806/pair-1-silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md).

Reviewer reason: “task completion alone cannot distinguish ‘the spec was sufficient’ from ‘the agent improvised well enough’” concerns diagnosis of an ambiguous instruction, not how a system learns, verifies knowledge, or improves through retained change.

Disposition (2026-09-26): Retain learning-theory through llm-reliability: the note distinguishes hidden specification repair from interpreter failure and identifies why success cannot diagnose the intended path. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-054 — architecture

- Status: resolved — assignment retained under revised scope.
- Note: [Skill discovery re-fires in every sub-agent context, not just the top-level invocation](../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md).
- Head: [architecture](../../tags/architecture-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23089](../../reports/state/review-jobs/review-job-8806/pair-2-skill-discovery-re-fires-in-every-sub-agent-context.md).

Reviewer reason: The case is “Observed on Claude Code's harness”; the argument concerns skill advertisement and worker behavior, not how Commonplace is structured or installed.

Disposition (2026-09-26): Retain architecture under the revised general head, superseding the removal under its old scope. Harness-owned discovery crosses a worker context boundary and constrains the available mitigations. Keep context-engineering and computational-model. A historical Commonplace skill is the observed case, but the note does not explain Commonplace's own layout, installation, or subsystem arrangement, so do not add commonplace-architecture. See the [architecture split](./architecture-placement-decision.md) for the operator decision, membership check, input versions, and verification.

## TP-055 — context-engineering

- Status: resolved — retagged.
- Note: [Stateful tools recover control by becoming hidden schedulers](../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23098](../../reports/state/review-jobs/review-job-8806/pair-11-stateful-tools-recover-control-by-becoming-hidden-schedulers.md).

Reviewer reason: The brief mention of “sub-goals that exceed one context window” names a limit, but the note's argument is where the scheduler lives; it does not substantively address knowledge routing, loading, scoping, or context budgets.

Disposition (2026-09-26): The argument relocates scheduler state and control behind a tool boundary. Context overflow is only a named limit delegated to another note. Keep computational-model, replace context-engineering with architecture, and move its curated entry to the architecture head. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-056 — context-engineering

- Status: resolved — tag removed.
- Note: [Bottom-up structure inference needs capture at the decision surface, not the state](../../notes/structure-inference-needs-capture-at-the-decision-surface.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23099](../../reports/state/review-jobs/review-job-8806/pair-12-structure-inference-needs-capture-at-the-decision-surface.md).

Reviewer reason: The decision-surface argument concerns evidence capture for later structure inference; it does not analyze how knowledge is routed into or loaded for a bounded LLM call.

Disposition (2026-09-26): The capture point determines which rationale-bearing structure can later be inferred. This explains memory ingress, not activation or loading into bounded calls. Remove context-engineering; retain agent-memory and learning-theory. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-057 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [System use provides evidence of theory fit and causal usefulness, not independent warrant](../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23106](../../reports/state/review-jobs/review-job-8806/pair-19-system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).

Reviewer reason: “Putting a claim to work in a live system” is broader than a deployed system meeting users and surprising its original design; that post-release phenomenon is not substantively analyzed.

Disposition (2026-09-26): retain deploy-time-learning. The body explains what live-system consequences warrant and when failures justify rescoping or removing a claim. Those limits govern how a system learns from use; a separate account of a surprising user encounter is no longer required. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-058 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [System use provides evidence of theory fit and causal usefulness, not independent warrant](../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 23106](../../reports/state/review-jobs/review-job-8806/pair-19-system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).

Reviewer reason: The scope says the system “does not require ... the system itself [to] perform the independent warrant assessment”; it discusses evidence for theory fit without specifying an operative self-change to the system's organization.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: the note separates criticism from use, theory fit, and independent warrant, including when evidence motivates rescoping or removal. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-059 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [System use is an initial selection environment when theory fit lacks a fixed oracle](../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23107](../../reports/state/review-jobs/review-job-8806/pair-20-system-use-selects-theory-fit-without-a-fixed-oracle.md).

Reviewer reason: “ongoing construction and operation” is the setting, but the note does not substantively describe deployed contact with users exposing needs that force post-release change.

Disposition (2026-09-26): retain deploy-time-learning. The argument makes consequential use an initial selection environment for theory candidates and explains correction, delayed consequences, and the danger of self-confirming feedback. That is a substantive learning response to operating experience. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-060 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [System use is an initial selection environment when theory fit lacks a fixed oracle](../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 23107](../../reports/state/review-jobs/review-job-8806/pair-20-system-use-selects-theory-fit-without-a-fixed-oracle.md).

Reviewer reason: The note includes human-inclusive selection and future possible machinery; its central claim does not require or explain a system making operative changes to its own organization.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: the argument describes consequential use selecting among stated theory candidates when no fixed global oracle suffices. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-061 — computational-model

- Status: resolved — retagged.
- Note: [Task families and product families classify different things](../../notes/task-families-and-product-families-classify-different-things.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23109](../../reports/state/review-jobs/review-job-8807/pair-2-task-families-and-product-families-classify-different-things.md).

Reviewer reason: “Tasks requiring map-reduce over intermediate results” is an example of a task family. The note does not explain how LLM calls, state, scheduling, or surrounding control execute, which this tag requires.

Disposition (2026-09-26): remove computational-model. Task and product families classify different reuse and assessment scopes. Map-reduce is a single example of a task grouping, not an execution analysis. Add evaluation for the declared sampling and acceptance frame. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-062 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [Task families and product families classify different things](../../notes/task-families-and-product-families-classify-different-things.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-03](./parent-child-relations.md#pc-03).
- Local evidence: [review pair 23109](../../reports/state/review-jobs/review-job-8807/pair-2-task-families-and-product-families-classify-different-things.md).

Reviewer reason: “The distinction classifies scope. It does not by itself establish learning, improvement, or generality.” Its account of product-family reuse and assessment frames does not address whether or how a system makes evidence-responsive operative changes to itself.

Disposition (2026-09-26): Retain self-improving-systems through software-factory: the note establishes the product-family boundary of reusable factory machinery and distinguishes it from benchmark task groupings. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.

## TP-063 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [The deployed system, not the model alone, is the unit of learning](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23116](../../reports/state/review-jobs/review-job-8807/pair-9-the-deployed-system-not-the-model-is-the-unit-of-learning.md).

Reviewer reason: The note mentions “a deployment-specific ambiguity,” but it does not analyze surprising user needs revealed after release or the resulting pressure to change, which is this tag's specific subject. It analyzes the mechanisms and boundary of learning.

Disposition (2026-09-26): retain deploy-time-learning. The note identifies the deployed system as the evaluation boundary and describes prompt revisions, validators, and other evidence-responsive updates. It explains why responding only through model weights leaves relevant causes fixed. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-064 — computational-model

- Status: resolved — retagged.
- Note: [Universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23139](../../reports/state/review-jobs/review-job-8808/pair-12-universal-software-factory-needs-a-declared-universality-axis.md).

Reviewer reason: The four universality axes classify software factories and acquisition claims; the note does not explain LLM call execution, state, scheduling, or an LLM computational limit.

Disposition (2026-09-26): remove computational-model. The four universality axes constrain what factory capability claims and their evidence mean. Generic compiler expressivity is a contrast, not an LLM execution analysis. Add evaluation for the required evidence and resource frame. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-065 — deploy-time-learning

- Status: resolved — assignment retained under revised scope.
- Note: [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md).
- Head: [deploy-time-learning](../../tags/deploy-time-learning-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23140](../../reports/state/review-jobs/review-job-8808/pair-13-use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md).

Reviewer reason: The note discusses transfer of design decompositions across contexts; it does not examine deployed software meeting users and revealing needs that force post-release change.

Disposition (2026-09-26): retain deploy-time-learning. The body explains why running a design only supports local sufficiency and what rationale must be retained to test transfer under new demands. It governs what can safely be learned and reused from operating experience rather than merely discussing decomposition. The operator explicitly included responses in this tag. See [scope decision](./deploy-time-scope-decision.md) for the revised rule, input versions, and verification.

## TP-066 — context-engineering

- Status: resolved — retagged.
- Note: [Warranted reader update is the objective of substantive writing](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md).
- Head: [context-engineering](../../tags/context-engineering-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23147](../../reports/state/review-jobs/review-job-8808/pair-20-warranted-reader-update-is-the-objective-of-substantive-writing.md).

Reviewer reason: “Search brings sources and existing notes into co-presence” is one workflow ingredient; the note’s question is how writing selects a warranted reader update, not how knowledge reaches a bounded call.

Disposition (2026-09-26): The workflow searches for a warranted contribution and judges its value relative to the reader. Co-presence is one ingredient, not a developed loading mechanism. Replace context-engineering with document-system; retain learning-theory and discovery. See the [context-engineering disposition](./context-engineering-placement-decision.md) for checked versions and verification.

## TP-067 — computational-model

- Status: resolved — retagged.
- Note: [World models assess explanatory-reach through action-conditioned prediction](../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md).
- Head: [computational-model](../../tags/computational-model-README.md).
- Initial reviewer judgment: mismatch.
- Local evidence: [review pair 23154](../../reports/state/review-jobs/review-job-8809/pair-7-world-models-assess-explanatory-reach-through-action-conditioned.md).

Reviewer reason: “The retained artifact is ... a learned representation plus predictor” describes a predictive model and reach testing. The head requires an explanation of how LLM-based programs execute—their instruction interpretation, scoping, state, tool-call loops, or orchestration—which this note does not supply.

Disposition (2026-09-26): remove computational-model. The note compares predictive, symbolic, and natural-language assessment and selective correction. World-model planning is not bounded LLM-call execution. Add discovery and learning-theory while retaining the theory-builder boundary assignment. See the [computational-model disposition](./computational-model-placement-decision.md) for additions, parent checks, input versions, and verification.

## TP-068 — self-improving-systems

- Status: resolved — assignment retained.
- Note: [World models assess explanatory-reach through action-conditioned prediction](../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md).
- Head: [self-improving-systems](../../tags/self-improving-systems-README.md).
- Initial reviewer judgment: mismatch.
- Dependency: [PC-04](./parent-child-relations.md#pc-04).
- Local evidence: [review pair 23154](../../reports/state/review-jobs/review-job-8809/pair-7-world-models-assess-explanatory-reach-through-action-conditioned.md).

Reviewer reason: “The choice between retaining such a theory and training a predictor” compares representational forms and correction locality. It does not examine whether or how a system makes operative, evidence-responsive changes to its own behavior-determining organization, the head's inclusion condition.

Disposition (2026-09-26): Retain self-improving-systems through theory-builder: the final section compares failure and selective revision in addressable theories with fitting an unlocalized predictor. It is a substantive boundary analysis, not a claim that every predictor is a theory builder. See [parent membership decision](./parent-membership-decision.md) for input versions and verification.
