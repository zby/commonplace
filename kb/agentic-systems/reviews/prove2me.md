---
{
  "type": "types/note.md",
  "description": "Prove2Me host integration: formal proof and translation review contracts, retained feedback, and shipped Lean extraction helpers.",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-25-prove2me-01",
  "source-identity": "https://github.com/prove2me/prove2me_workspace",
  "reviewed-revision": "326b972580e0640b1f3739ec7b12d2b34d8d3527",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-prove2me-01/result.md",
  "analysis-result-sha256": "20273c57e7ee775353a5afafc1a6e601182f5d84624f97641fe8b7845e54ecd8"
}
---

# Prove2Me

Evidence basis: repository instructions and two Lean source helpers at `326b972580e0640b1f3739ec7b12d2b34d8d3527`, inspected 2026-09-25. Overall doc-grounded; no platform interaction or target execution was performed.

The Prove2Me workspace is a host integration for an external coding agent. Its skill and reference files prescribe theorem discovery, proof attempts, collaboration, human review and project upload. The remote platform, enclosing agent runtime and Lean kernel are outside the inspected artifact. The supplied code implements dependency and source-position extraction; the broader agent and verification workflows remain documented interfaces. [Workspace](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/README.md#L3-L5), [skill](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/SKILL.md#L12-L39).

The ordinary solver reuses its local environment, reads prior statements and attempts, writes a proof, disproof or reduction, compiles locally, submits, polls and explains the result. Formal reuse permits open assumptions: a reduction importing an Open child can receive SKETCH_ACCEPTED, while the parent becomes Proved only after its children are Proved. ACCEPTED and SKETCH_ACCEPTED therefore carry different conditions. A successful local build also does not establish that the server's exact-target and import rules have passed. [Verification and reductions](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/prove.md#L187-L246).

Formal validity and faithful translation have separate consumers. The formal target governs proof checking. A fresh auditor receives only a draft's Lean code and produces a literal natural-language read-back; a human compares that rendering with the intended source before launch. Public proposals also pass moderation, whereas private launch bypasses that stage. Editing a draft clears confirmation and calls for a fresh read-back. These are procedural contracts, not runtime isolation or deployed checks established by the workspace. [Audit and adoption](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/mission_captain.md#L189-L225), [human and moderator roles](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/mission_captain.md#L302-L324).

Retained explanations, failed attempts, captain reasons and review history have explicit later consumers: solvers are told to inspect them before choosing another approach. This affords an attempt-to-lesson-to-later-solver learning route, without measured improvement. Most retrieval is requested by the solver or compiler; the captain-to-auditor handoff is prescribed identifier-based push. Deprecation withdraws a node from discovery while preserving imports and proof status, and deleting a milestone deletes its history. Curation changes availability and attention without necessarily changing formal warrant. [Solver scouting](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/mission_solver.md#L28-L36), [dead-end reports](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/communicate.md#L117-L122), [deprecation](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/contribute.md#L312-L328).

The project-upload mode starts from existing proofs. Two shipped Lean helpers extract elaborated dependencies and source coordinates. The host must write the planner, generator and uploader. The playbook prescribes mechanical source slicing, exact upload-byte compilation, elaborated-type comparison and checkpoints that resume polling recorded job IDs. It does not supply an exactly-once recovery implementation. The checkpoint writer's unspecified transformation also leaves its classification as derived learning, rather than copied operational records, unresolved. [Upload method](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/upload_full_project.md#L5-L10), [validation and continuation](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/upload_full_project.md#L90-L117), [source-position helper](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/scripts/extract_sketch_info.lean#L101-L177).

Campaigns add another distinct warrant: a moderator can attest that a goal instantiates a shared template and record its value while the goal remains Open. That acceptance is not a completed proof. Similarly, source citations, votes and explanations have different force from formal verification. [Campaign attestation](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/campaigns.md#L89-L94), [review condition](https://github.com/prove2me/prove2me_workspace/blob/326b972580e0640b1f3739ec7b12d2b34d8d3527/references/campaigns.md#L154-L159).

## Scope

Internal documentation conflicts remain explicit: broad submission-source access wording versus private-proof restrictions; explanation-only PATCH wording versus submission deprecation; alternate task priorities; and different instructions for dropping spanless extraction rows. They do not establish a deployed privacy leak or a verified exhaustive API contract. The exact result retains both sides and their consequences.

The strongest learning finding is an afforded feedback-and-reuse route. Criticism and replacement are prescribed; improved future capacity, a revised theory of the agent's own organization and measured self-improvement remain unestablished. Backend/host implementation, candidate-linked checking and controlled recall comparisons would materially change this assessment.

---

Relevant Notes:

- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-prove2me-01/result.md) — see-also: canonical records, quotations, documentation conflicts, both lenses and normalized comparison fields.
