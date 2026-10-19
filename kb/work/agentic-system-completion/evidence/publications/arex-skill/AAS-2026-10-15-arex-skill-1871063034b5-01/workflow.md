---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AREX-Skill workflow account: source-anchored direct Creator construction, verification, generic import and Researcher handoff."
run-id: AAS-2026-10-15-arex-skill-1871063034b5-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill workflow report

## Workflow account

### Selected workflow and evidence

This account follows a source-anchored, task-agnostic **direct** construction run: a Creator turns source material into an operating skill graph, verifies it, imports it through the generic importer and leaves a handoff for a later Researcher. It is selected because the canonical distillation entry and its direct-construction reference explicitly connect request interpretation, approval, verification, recovery and delivery. This is a shipped procedural workflow with an executable admission step, not a reconstructed successful run. The containing route is [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission); its later instruction-delivery route is [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery).

All evidence is SRC-1 at the revision in [the boundary](boundary.md). Inspection here covers `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`, adds the full references `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md` and `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/construction-strategy-and-adequacy.md` as doctrine/design, and checks validation and transaction sections of `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs` as implementation. No target execution or example trace was inspected. Completion, compliance and later usefulness remain unobserved.

### 1. Request becomes an approved construction contract

The caller supplies a source anchor, not necessarily a downstream task. Creator instructions require an anchor record naming the source kind, version/access/trust boundary, intended future use and unknowns. The Creator scopes capabilities, applicability, non-goals, graph entries and verification targets, then grounds them in retained evidence with provenance, exclusions and conflicts. The source-anchored path must not invent a downstream task merely to obtain a task-level outcome trial (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`).

The direct branch is conditional, not the universal default. The Creator inventories visible construction contracts; an adequate existing workflow is preferred. Direct construction applies when no existing workflow or bounded composition is adequate and the current run can produce and verify a graph. A recurring construction gap can instead route to designing a future Creator workflow, which is not delivery of the present operating graph (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/construction-strategy-and-adequacy.md`).

> Use `direct` when no existing workflow or bounded composition is adequate, a
> concrete anchor is available, and the current run can produce and verify the
> operating graph. This can serve either distillation form.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/construction-strategy-and-adequacy.md`

After grounding, the Creator presents the exact construction specification for user approval. It supplies scoped capabilities, evidence and revisions, proposed graph boundaries/links, checks with expected observations and strict/soft gates, permissions, budget, recovery, deployment/importer and owned unknowns. Blocking unknowns must be resolved. Material changes to anchor, evidence boundary, scope, budget, permissions or verification gate reopen approval. These are instructions to the agent and user, not an executable approval-token check. The user may request revision; the Creator is responsible for not proceeding under a stale specification (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`).

### 2. Creator constructs, checks and repairs the candidate

The approved specification delegates production of the operating graph to the Creator, while the user retains the requested approval decisions. Direct construction does not mandate a child agent. The runtime's separate child-session capability is not evidence that this selected workflow necessarily uses it. Here the consequential handoffs are contract approval, candidate-to-checks, approved candidate-to-importer and Creator-to-later-Researcher.

Each candidate node must contain applicability, procedures, expected observations, checks, recovery actions and evidence provenance, with an explicit operating role. Drafts, evidence plans, verification output, construction records and handoff files stay outside live skill roots. Verification includes structure, source support, links, executable or representative-use behavior and failure recovery. Because this selected branch has no downstream task, representative uses are source-supported rather than an invented task evaluator (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`).

> 6. Repair only affected skills, links, evidence mappings, or fixtures, then
>    rerun the affected checks and graph integration. A strict blocker leaves the
>    candidate unverified.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`

Thus a failed strict check does not procedurally become an accepted graph: the Creator repairs the affected material and reruns checks, or reports an unverified candidate with explicit blockers. The expected observations and gates come from the approved specification. There is no universal answer oracle; source-support review and representative checks are not equivalent to an external reference answer. This branch establishes requested verification and repair, not that checks ran or that a graph is scientifically correct. The importer below does not independently enforce these semantic checks.

### 3. Separate import approval precedes executable admission

Only after verification does the Creator assess reuse and destination. Task-bound or uncertain output defaults to project scope; managed scope requires a self-contained, provenance-backed graph with cross-project representative-use evidence. All roots and sub-skills stay in one scope. Before import approval, the Creator shows exact destinations, entry point, verification, gaps, collisions, shadowing and overwrite status. Overwrite approval is separate. The selected generic importer is invoked once with all top-level roots (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`). These user decisions are procedural requirements; the executable sees arguments, not authenticated evidence of human approval, as bounded by [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission).

The helper rejects drafts inside the live root, overlapping draft roots, nonportable files, malformed or duplicate names, missing operating roles, reserved repository-routing content, broken/out-of-graph relative links and protected namespace collisions. Existing targets reject without overwrite. It copies drafts into staging, validates them again, rechecks collisions, backs up replaced roots, renames staged roots into place and validates live targets before marking the transaction committed (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`). These checks admit graph structure and bytes, not the truth of the instructions or the quality of their evidence.

For the selected failure path, a caught error before commit makes the importer remove installed partial targets and restore backed-up targets in reverse order. Rollback errors are reported rather than converted into success. Recovery ownership therefore changes from Creator-led content repair before import to importer-led filesystem restoration during admission, with unresolved failures returned to the caller. The shared lock wrapper is invoked by the ordinary entry, but its implementation was not audited here. Sequential renames and fallible restoration do not establish power-loss recovery or all-reader atomicity. This is the same bounded transaction mechanism already recorded in [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission), not a second admission route.

### 4. Delivery ends with installed paths and an external handoff

On success the helper prints imported IDs and exact destinations and asks for a new Researcher session. The Creator separately writes `researcher-handoff.md` outside live roots. It carries anchor and distillation form, capabilities, evidence provenance, accepted or unverified graph, construction-record path, strategy, selected scope and imported paths, entry point, verification evidence, unresolved limits and overwrite status (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`).

> 10. Write `researcher-handoff.md` after the deployment decision. Do not load the
>     graph or execute the downstream task in the Creator session.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/references/direct-construction-and-handoff.md`

The intended delivered product is therefore an admitted operating graph plus construction evidence and a handoff, not a solved downstream research task. An unverified candidate can still be reported, but must not be described as verified delivery. The importer does not enforce production of the construction record or handoff file. The protocol calls for them; no supplied execution establishes their existence for a particular run.

A later eligible Researcher discovers installed descriptions/locations, then receives selected bodies by reads or explicit skill expansion. It does not automatically receive the Creator's full conversation or construction evidence merely because import succeeded. The handoff points to evidence; whether a later session is actually given that handoff is unobserved. [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) and [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance) establish the wired instruction channel, not activation or compliance. Direct file/shell writes also remain alternate paths outside this importer's checks. No exercised self-improvement or demonstrated learning follows from this workflow's installation step.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission)

Workflow-specific ordering: source anchor and capability scope → grounding → exact direct-specification approval → candidate construction → verification/affected repair → destination and import approval → generic import → external Researcher handoff. Material specification changes reopen approval; overwrite is separately approved. A strict verification blocker leaves an unverified candidate. The Creator owns content repair; the importer owns caught precommit filesystem rollback; the caller receives unresolved errors. Delivery of this Creator workflow stops before downstream task execution. The account above supplies the added direct-reference evidence; these fields refine the supplied route rather than declare another identity.

#### On [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery)

Workflow-specific successor boundary: installed paths and the handoff identify the entry point for a new Researcher session. The Creator is instructed not to test delivery by loading the resulting operating graph in its own session. Later discovery and selected reads can supply operating guidance without carrying the full construction conversation. The selected workflow's successful transition into actual Researcher use remains unobserved.
