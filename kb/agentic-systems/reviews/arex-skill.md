---
type: types/note.md
description: "AREX-Skill's repository-skill construction and deployment subsystem: model-directed verification, transactional admission, selective reads and evidence limits"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-arex-skill-01
source-identity: https://github.com/VectorSpaceLab/AREX-Skill
reviewed-revision: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/result.md
analysis-result-sha256: 973dc7c3679aaadff574cb9b4cc9d40602a8a9c120190430fa48bf8fdd356d47
---

# AREX-Skill

**Evidence basis:** repository code and workflow instructions at `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`, inspected on 2026-09-25. No target experiment ran; benchmark numbers remain source-reported claims.

AREX-Skill retains repository knowledge as operating skill graphs: instructions, linked references and executable helpers that a later agent can select and use. This review covers the repository-skill construction, verification, refresh, managed deployment, export and role-filtered loading subsystem. The repository also ships the DisCo agent runtime; general conversation memory, arbitrary extensions, paper-specific construction and new meta-skill design are outside this boundary.

## Construction and verification

DisCo Creator follows bundled workflows to inspect source and prepared environments, plan sub-skills, delegate writing, integrate files and verify the resulting graph. Review records stay separate from runtime skills. The workflow asks for explicit assertions, fresh-agent usability checks when available, selected native tests, targeted revision and rechecking. Human scope and import decisions can be delegated under specified conditions; an unresolved required-backend limitation disables automatic import by instruction. See exact-result RTE-1 and RTE-9; [construction workflow](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md) and [verification workflow](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md) — evidenced-by.

These semantic checks are model-directed procedures. The optional native-case helper implements command execution, timeouts and retained result summaries, but exit zero establishes only the selected command outcome. Generated assertions, upstream reference tests and a model's qualitative review have different warrant. Construction subagents have separate in-memory sessions and inherited roles, while their tools and written files remain within the host's authority. A supplied prepared environment is checked before lane startup; missing model resolution can fall back to the session default. Provider identifiers do not establish immutable weights.

## Deployment and later use

The dedicated importer validates a staged graph's names, role/visibility fields, license consistency, links, routing metadata and matched content digest. It swaps the graph, router and index under its managed protocol, with restoration on handled failures. The official-library manager additionally compares retained state with current and desired files to detect local modifications. These are implemented integrity controls. Import success does not prove the workflow performed semantic review or passed native/backend tests: the importer does not require those reports as admission receipts. See RTE-2; [importer](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs) — evidenced-by.

Researcher sees eligible operating/shared skills; Creator sees meta/shared skills. Repository roots can remain registered for explicit invocation while hidden from the initial model-visible list. The visible router guides requested reads through area, family and selected skill pages. That supports progressive disclosure, but the prescribed narrow-read sequence depends on model behavior and has no inspected hard context budget. Role filtering and project trust govern resource loading; they are not filesystem or tool-execution sandboxes. See RTE-3 and RTE-8; [skill visibility and prompt formatting](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/core/skills.ts) — evidenced-by.

Classification reasons remain in an external handoff. Runtime routing metadata and generated assignment projections omit them. A Creator refresh can consult prior review evidence; an ordinary Researcher is not thereby given the derivation reason for every rule. Portable export supplies selected graphs and target-specific visibility metadata to named external agents, whose actual loading and behavior were not inspected.

## Memory and epistemic limits

Two trace-fed retention paths are afforded: verification feedback can revise portable skills for later tasks, and setup-command results can produce a private environment handoff for later stages of the current construction task. Requested skill/report reads are pull. Lane startup separately pushes a coarse bundle of retained environment fields to a machine checker; it does not send the whole report to the child model. The exact result preserves these distinct horizons and the complete fourteen-axis comparison profile.

The strongest supported contribution is a revision and reuse pathway with explicit criticism and narrower executable controls. Whether criticism improved future capacity remains **uninspected**. A published graph's existence does not establish its original verification lifecycle, and the reported benchmark treatment concerns the equipped-skill bundle rather than any isolated router or refinement mechanism.

Reflection is **wired** in a limited operational sense: the official manager records installed-library state, updates that representation when deployment changes, and uses it in later update/conflict decisions. This establishes neither an explanatory self-theory nor improved capacity. Demonstrated self-improvement remains separately **uninspected**. See OBJ-4 and RTE-2; [managed-library state and updates](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/core/repo-skills-library-manager.ts) — evidenced-by.

## Scope

The sampled library content establishes artifact shape, not population-wide correctness. Provider/dependency internals, live execution, crash recovery and downstream scientific outcomes are uninspected. Candidate-linked construction records, skill-dependent tests and controlled comparisons would strengthen the empirical conclusions. Full source quotations, route audits, specialist reconciliation and limits are in the [retained exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/result.md) — see-also.

- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the separate requirement for criticism to improve future capacity.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the connected self-representation used for the bounded manager finding.
