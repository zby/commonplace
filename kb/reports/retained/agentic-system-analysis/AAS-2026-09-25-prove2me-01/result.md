---
{
  "type": "agentic-system-analysis-result",
  "description": "Complete Prove2Me host-integration analysis distinguishing documented proof, translation and reuse contracts from shipped Lean extraction helpers.",
  "run-id": "AAS-2026-09-25-prove2me-01",
  "system": "Prove2Me",
  "run-date": "2026-09-25",
  "result-disposition": "complete",
  "target-class": "host integration",
  "boundary-kind": "complete artifact, partial loop",
  "reviewed-boundary": "326b972580e0640b1f3739ec7b12d2b34d8d3527",
  "analysis-cutoff": "2026-09-25",
  "evidence-tier": "doc-grounded",
  "memory-comparison": {
    "scope": "Accumulated local project files and access/environment state; documented platform mathematical objects, attempts, feedback, discovery metadata and drafts; extracted facts and prescribed upload checkpoints. Static skill text supplies routes but is not itself learned memory. Remote storage internals, host internals and Lean internals are excluded.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "files",
          "repo",
          "service-object"
        ],
        "records": [
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-20",
          "OBJ-21",
          "OBJ-22",
          "OBJ-23",
          "OBJ-8",
          "OBJ-9",
          "OBJ-24",
          "OBJ-25"
        ],
        "note": "Files and the per-workspace Mathlib checkout accompany API objects. Graph-shaped content does not establish a graph database; no backend database substrate is claimed."
      },
      "representational_form": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "records": [
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-20",
          "OBJ-21",
          "OBJ-22",
          "OBJ-23",
          "OBJ-8",
          "OBJ-9",
          "OBJ-24",
          "OBJ-25"
        ],
        "note": "Lean code, structured identities, dependency facts and checkpoints are symbolic; descriptions, reasons, discussions and read-backs are prose. Compiled Lean artifacts are symbolic, not model weights. Credential bytes are access tokens, not semantic summaries."
      },
      "lineage": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "authored",
          "imported",
          "other-compiled",
          "trace-extracted"
        ],
        "records": [
          "RTE-1",
          "RTE-3",
          "RTE-5",
          "RTE-7",
          "RTE-9",
          "RTE-10"
        ],
        "note": "Humans and agents author; platform/source files and dependencies are imported; Lean metadata is compiled from source; experience summaries and resume state derive from work and API traces."
      },
      "behavioral_authority": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "enforcement",
          "instruction",
          "knowledge",
          "ranking",
          "routing",
          "validation"
        ],
        "records": [
          "OBJ-11",
          "OBJ-12",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-6",
          "RTE-8",
          "OBJ-9",
          "OBJ-24",
          "OBJ-25"
        ],
        "note": "Credentials and visibility constrain access; selected milestone statements instruct formalization; feedback advises; votes/frontier metrics rank; dependency and checkpoint state route work; formal targets validate proofs. No weight-update or learned-policy consumer is established."
      },
      "write_agency": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "automatic",
          "manual"
        ],
        "records": [
          "RTE-1",
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "RTE-9",
          "RTE-10"
        ],
        "note": "Documented agent/API writes and implemented extractors coexist with human audit, moderation and author edits. Only the extractor transformations are wired here."
      },
      "curation_operations": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "decay",
          "evolve",
          "invalidate",
          "promote",
          "synthesize"
        ],
        "records": [
          "RTE-5",
          "RTE-6",
          "OBJ-9",
          "RTE-9"
        ],
        "note": "Edits evolve, deprecation withdraws discovery reliance, votes/bookmarks/milestone selection raise salience, failed-attempt explanations synthesize lessons, and deleting milestone/history forgets retained material. Invalidation is limited: imports still work. Acquisition-time deduplication and upload slicing do not establish memory dedup or consolidation."
      },
      "read_back_direction": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "pull",
          "push"
        ],
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-3",
          "RTE-5",
          "RTE-7",
          "RTE-8",
          "RTE-11"
        ],
        "note": "Solvers, compilers and uploaders request retained files/objects. The captain procedure supplies each draft's code to a fresh auditor without an auditor request; this is a prescribed push, not implemented context assembly."
      },
      "read_back_signal": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "identifier"
        ],
        "records": [
          "RTE-11"
        ],
        "note": "For each selected draft item, captain selects that item's Lean statement and preamble for its auditor. No vector or lexical push selector is established. Search keywords elsewhere characterize pull queries."
      },
      "trace_learning": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "yes"
        ],
        "records": [
          "RTE-9",
          "RTE-10"
        ],
        "note": "Prescribed agents derive durable lessons/explanations from attempts for later solvers. Checkpoint continuation is afforded, but whether its unimplemented writer transforms traces beyond copying action/response records is not determinable. The positive value rests on the lesson route."
      },
      "trace_source": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "tool-traces",
          "trajectories"
        ],
        "records": [
          "RTE-9",
          "RTE-10"
        ],
        "note": "Proof/verification attempts and their outcomes feed explanations and dead-end reports; upload API calls and responses feed checkpoints. Raw history retention by itself is not counted."
      },
      "learning_scope": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-9",
          "RTE-10"
        ],
        "note": "Lessons support per-project and cross-task learning. A per-task checkpoint consumer is explicit, but its derivation beyond raw-record copying is unspecified, preventing a complete union of qualifying horizons."
      },
      "learning_timing": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "online"
        ],
        "records": [
          "RTE-9",
          "RTE-10"
        ],
        "note": "Feedback is written within the solver loop after an attempt/verdict, and checkpoint writes surround API calls. No separate offline trainer or batch distillation phase is established."
      },
      "distilled_form": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-9",
          "RTE-10"
        ],
        "note": "Argument/dead-end prose supports natural-language. Symbolic checkpoint state is retained and consumed, but no implementation determines whether it is derived memory or copied raw records; the complete distilled-form union is unresolved."
      },
      "faithfulness_tested": {
        "assessment": "known",
        "basis": "afforded",
        "values": [
          "no"
        ],
        "records": [
          "ABS-1"
        ],
        "note": "No retained experiment tests dependence on recalled content. Formal checking, read-back auditing and source-type comparison concern mathematical correctness or translation, not a recall-dependence experiment."
      }
    }
  }
}
---

# Prove2Me agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-prove2me-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/prove2me.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-prove2me-01/memory-report.md`

**Memory analysis report SHA-256:** `2eec262d2461808e05c00d9a177c67de614efc31c9dc7e1f5fc4e25ffb221d99`

Frozen specialist input SHA-256: `6d260cc81690071ab0169e346fbc25b7aef1ab0d8a086c1ed4514ead5010bf70`.

## Boundary and evidence

Prove2Me is assessed as a host integration: the complete source workspace supplies skill/reference instructions for an enclosing model-driven coding agent plus two Lean extraction helpers. Boundary kind: complete artifact, partial loop. Overall evidence tier doc-grounded, with narrower helper operations code-grounded. Revision `326b972580e0640b1f3739ec7b12d2b34d8d3527`, cutoff 2026-09-25. Intended use: independent architecture, memory/context and epistemic characterization, not a deployed-service assessment.

Includes solver/captain/auditor/project-upload procedures; documented API objects, async statuses, dependency and review contracts; local environment and credentials retention; formal-object and feedback reuse; curation; extraction code. Excludes enclosing host implementation, remote API/backend implementation, Lean kernel/toolchain internals, provider parameters and external mathematics. These exclusions prevent claims about deployed enforcement, source truth, model activation, complete agent execution or empirical improvement. No source instructions were executed, no accounts/credentials accessed, no API/network actions or Lean build performed. Worked-example description is reported operation only, not an admitted candidate-linked platform run or causal experiment.

## Source register

SRC-1 — Git `https://github.com/prove2me/prove2me_workspace` at `326b972580e0640b1f3739ec7b12d2b34d8d3527`; access root `/home/zby/llm/commonplace/related-systems/prove2me--prove2me_workspace`. Doctrine/design: README.md, SKILL.md and references/setup, lean-setup, prove, discover, contribute, communicate, curate, missions, campaigns, mission_solver, mission_captain, mission_auditor and upload_full_project Markdown files, with precise anchors on records. Implementation: `scripts/extract_decl_graph.lean:25-102` and `scripts/extract_sketch_info.lean:77-177`. Reported operation only: `examples/upload_full_project/README.md:3,60-66`. All reads commit-addressed; no prior review/ingest used. Truncated initial reads were repeated in bounded ranges. No access gap inside admitted repository; external implementations and actual candidate execution are not evidence.

## Shared records

### Components

CMP-1 — External enclosing coding-agent host, instructed to load the skill and perform local/API work. Model-dependent inference is required by the prescribed authorship/auditing roles, but model identity, exact version, weights and parameter updates are uninspected. No host runtime or context assembler is supplied. Interface conclusion status: afforded. SRC-1 `SKILL.md:1-39,43-69`.

CMP-2 — Described remote Prove2Me service API for formal objects, publish/verify jobs, dependency states, missions and feedback. Physical storage and implementation are uninspected; service-object interfaces are afforded. SRC-1 `references/prove.md:115-166,187-307`; `references/contribute.md:82-131`.

CMP-3 — External local Lean/Mathlib project and build tools. The playbooks prescribe exact target environment pins and reusable builds. Compiler/kernel semantics and package execution are not inspected here. Interface conclusion status: afforded; exact toolchain identity varies by selected platform environment. SRC-1 `references/lean-setup.md:17-54,98-113`; `references/prove.md:45-82`.

CMP-4 — Two shipped Lean source helpers. extract_decl_graph reads elaborated constant dependencies/kinds/source spans and writes JSONL; extract_sketch_info elaborates source and extracts declaration/reference positions from syntax/InfoTree, writes JSONL to stdout and returns nonzero on elaboration errors. Symbolic program, no parametric update. Implementation conclusion status: wired. SRC-1 `scripts/extract_decl_graph.lean:25-102`; `scripts/extract_sketch_info.lean:77-177`.

CMP-5 — Human mission approver, fresh auditor role and moderator as prescribed participants. Fresh auditor model identity/fixity/provider internals uninspected; source isolation is a procedural constraint, not supplied runtime enforcement. Humans compare intended meaning and choose adoption; public moderator and private launch differ. Conclusion status: afforded. SRC-1 `references/mission_auditor.md:3-14,51-55`; `references/mission_captain.md:191-195,302-324`.

### Operative objects

OBJ-1 — Static `SKILL.md` and role/API references. Instructional context for the host, not content accumulated from execution. Skill-version refresh is maintenance of shipped doctrine, not trace learning. SRC-1 `SKILL.md:43-69,103-128`.

OBJ-2 — Retained local workspace, `credentials.json`, environment pins, `.lake/` checkout/builds and global toolchain/cache reuse. These are files/repository state; tokens supply access, pins govern compilation and environment selection. Keys expire after 30 days, access tokens after one hour; old refresh-token flows require saving the rotated token. No semantic summary is encoded in credential bytes. SRC-1 `references/setup.md:7-24,126-157`; `references/lean-setup.md:17-54,98-113`.

OBJ-3 — Published Lean statements and definition bodies with `preamble`, names, environment and source citations; local mirrors retain exact formal text. Symbolic content is distinct from natural-language title/description and source/access metadata. Imports consume formal definitions or theorem stubs. Published formal content is immutable by contract; corrections require new nodes. SRC-1 `references/contribute.md:31-45,129-165`; `references/prove.md:45-82,292-307`; `references/mission_captain.md:223-225,318-324`.

OBJ-4 — Uploaded solution code and target/proof-type identity, plus local candidate files. Exact source remains separately fetchable after success or failure. A submission explanation is not the code, and code alone does not expose the author's full rationale. SRC-1 `references/prove.md:115-163`; `references/discover.md:184-255`.

OBJ-5 — Raw submission and publication outcomes/diagnostics, request echoes, and derived theorem/dependency state. JSON fields include IDs/status/error and the import graph; no physical backend storage is revealed. Failed publication retains submitted content for correction. Open-leaf selection traverses remaining open branches and ranks by how many ancestors would close. SRC-1 `references/contribute.md:82-127`; `references/prove.md:187-246,256-279`; `references/missions.md:97-119`.

OBJ-6 — Derived explanations/dead-end lessons, comments/references/backlinks, human audits/read-backs, ratings, captain edit reasons and moderation reports. Service objects mix natural-language content with symbolic provenance/access metadata. Comments label agent attribution from authentication context, not verified authorship; a null marker is unknown. Milestone history stores reasons separately from the current milestone. SRC-1 `references/communicate.md:3-62,84-122`; `references/missions.md:164-191`; `references/discover.md:77-97,169-190`; `references/mission_captain.md:295-324,431-469`.

OBJ-7 — Two kinds of symbolic extraction facts: declaration names/dependency sets/source spans in `decl_graph.jsonl`, and declaration/reference byte positions in per-file sketch JSONL. Their prescribed consumer is a host-written planner/generator, which creates platform files for later compilation/upload. Stage 1 writes a file; Stage 2 prints JSONL and the documented invocation redirects it. These are source/elaboration transformations, not agent-experience distillation. SRC-1 `scripts/extract_decl_graph.lean:25-102`; `scripts/extract_sketch_info.lean:77-177`; `references/upload_full_project.md:19-61,83-95`.

OBJ-8 — Prescribed uploader state file recording actions and job/submission IDs, plus a name-to-theorem-ID cache. Symbolic trace-derived control state tells a restarted uploader to poll rather than resubmit. Schema, storage atomicity, retention and unresolved-call reconciliation are not implemented here. SRC-1 `references/upload_full_project.md:101-117`.

OBJ-9 —  discovery/access metadata including saved theorem IDs, tag sets and votes, extending the parent's ratings inventory without changing OBJ-6. Human/agent selection and API updates persist as service objects; status/tag/lexical/exact-name queries retrieve them, and votes rank results. Saving twice is idempotent, not semantic deduplication. SRC-1 `references/discover.md:9-75,99-117`; `references/curate.md:3-80`.

OBJ-10 —  mission proposal drafts, ordered milestone specs, and campaign template/entry context. Draft code/prose is editable before publication; reference items point at existing immutable nodes. Campaign templates and shared foundation definitions constrain comparability; moderator-attested values can remain unproved. Metadata and recorded history are distinct from proof status. SRC-1 `references/mission_captain.md:191-225,295-324`; `references/missions.md:121-162`; `references/campaigns.md:3-11,64-95,122-159`.


Heterogeneous seed containers retain their original referents but are superseded by parts for the epistemic inventory: OBJ-2 by OBJ-11 and OBJ-12; OBJ-3 by OBJ-13 and OBJ-14; OBJ-4 by OBJ-15 and OBJ-16; OBJ-5 by OBJ-17 and OBJ-18; OBJ-6 by OBJ-19, OBJ-20 and OBJ-21; OBJ-7 by OBJ-22 and OBJ-23; OBJ-10 by OBJ-24 and OBJ-25. No existing ID is reused for one part.

OBJ-11 — Workspace/credential access state. Local files and retained keys/tokens; host checks reuse/expiry; operational access, not a semantic summary. Source SRC-1 `references/setup.md:7-24,126-157`. Conclusion status: afforded.

OBJ-12 — Environment/build state. Symbolic Lean/Mathlib pin and local repository/build artifacts, consumed by compiler and environment selection. Source SRC-1 `references/lean-setup.md:17-54,98-113`. Conclusion status: afforded.

OBJ-13 — Formal mathematical declarations. Lean statements, binders, definitions/preambles and imports, authored/imported then published immutably by contract; solver/compiler consume. Source SRC-1 `references/contribute.md:31-45,129-165`. Conclusion status: afforded.

OBJ-14 — Source/natural-language statement metadata. Authored descriptions and source references, mutable with history; translation intent and provenance, not formal proof payload. Source SRC-1 `references/contribute.md:238-270`. Conclusion status: afforded.

OBJ-15 — Candidate proof/disproof/reduction code. Symbolic Lean terms/tactics, host-produced or transplanted, local and submitted bytes consumed by compile/verify. Source SRC-1 `references/prove.md:45-82,115-166`. Conclusion status: afforded.

OBJ-16 — Submission identity. Target ID/proof type/source retrieval identity, symbolic routing and immutable contract metadata. Source SRC-1 `references/prove.md:154-166`. Conclusion status: afforded.

OBJ-17 — Raw outcomes/diagnostics. Documented status/error/request echoes, evidence about attempted operations; retained remotely and polled byhost. Source SRC-1 `references/contribute.md:82-127`. Conclusion status: afforded.

OBJ-18 — Derived dependency/proof status. Documented Open/Proved and reduction-child graph, used by compiler/solver/frontier and ancestor-resolution logic. Source SRC-1 `references/prove.md:187-246,256-279`. Conclusion status: afforded.

OBJ-19 — Explanations and failure lessons. Natural-language argument/failure claims derived from attempts, retained as explanation/attempt comment for later solvers. Source SRC-1 `references/prove.md:115-136`. Conclusion status: afforded.

OBJ-20 — Audit read-backs and criticism reports. Fresh-model literal rendering and human/moderator critique of statements, retained for human adoption/revision. Source SRC-1 `references/mission_captain.md:191-195,295-324`. Conclusion status: afforded.

OBJ-21 — History and discussion access metadata. Comments/backlinks, ratings and captain edit reasons; reason may live only in history and be optional. Source SRC-1 `references/mission_captain.md:443-469`. Conclusion status: afforded.

OBJ-22 — Extracted declaration/position facts. Symbolic elaboration-derived dependencies and source coordinates, shipped helpers produce, host-written generator consumes. Source SRC-1 `scripts/extract_decl_graph.lean:25-102`. Conclusion status: wired.

OBJ-23 — Generated upload tree. Symbolic transformed Lean source, host-written planner/generator prescribed, later local/compiler/API consumers. Source SRC-1 `references/upload_full_project.md:48-95`. Conclusion status: afforded.

OBJ-24 — Draft/milestone goal content. Editable formal/natural-language goal, source intent and ordered milestone specifications; host/human/moderator consume. Source SRC-1 `references/mission_captain.md:191-225`. Conclusion status: afforded.

OBJ-25 — Campaign template and attested value. Formal template/shared definitions plus moderator-attested numerical value; attested entry can remain Open, distinct from proof. Source SRC-1 `references/campaigns.md:3-11,89-94,154-159`. Conclusion status: afforded.

### Routes

RTE-1 — Setup and reuse. A later host checks existing workspace/credentials before acquiring new ones, uses retained pins to compile and refreshes expired access. Static skill-version comparison can request a source update but does not learn from traces. Conclusion status: afforded. SRC-1 `references/setup.md:7-24,126-157`; `references/lean-setup.md:98-113`; `SKILL.md:103-107`.

RTE-2 — Solver discovery and scouting. Agent selects a mission/theorem, calls saved/milestone/frontier/search endpoints, then fetches relevant histories, audits, discussions, decompositions and source. Pull to the named solver, with human target choice and captain ordering. Conclusion status: afforded. SRC-1 `references/mission_solver.md:16-36`; `references/discover.md:99-117,184-255`; `references/missions.md:97-162`.

RTE-3 — Agent authors formal statements/proofs using source and selected existing platform nodes, mirrors imported declarations locally and asks local Lean to build. Formal target/type is validation authority; source/prose informs translation; a local successful build can still import its own target stub and therefore is weaker than the advertised server gate. Conclusion status: afforded. SRC-1 `references/prove.md:45-82`; `references/lean-setup.md:73-92`.

RTE-4 — Submit/poll and formal dependency reuse. API queues candidate code, compiler/verifier consumes the target formal statement and requested imports, and service records status/decomposition. Completion of children is claimed to update ancestors. Named compiler consumers and import interface establish afforded reuse, but backend resolution/cycle controls are not inspected. Environment and visibility restrict imports. Conclusion status: afforded. SRC-1 `references/prove.md:187-246,292-307`; `references/contribute.md:82-131`.

RTE-5 — Explanations, discussion and curation. Agent/human writes reusable prose and access metadata; later solvers explicitly request it before attempting a theorem. Author/captain/moderator edits, deprecation and comment deletion alter later availability; public histories and precise source pointers allow checking reasons. Conclusion status: afforded. SRC-1 `references/mission_solver.md:28-36,52-74`; `references/communicate.md:84-122`; `references/contribute.md:238-328`.

RTE-6 — Draft, audit, human adoption and moderation. Agent drafts retained proposal objects and attaches a fresh auditor's read-back/model. Human compares intent to read-back and confirms items; submission publishes compile-accepted drafts, then public missions require moderation. Private launch has no moderator stage. Later captain reads reports/flags to replace rejected published statements. Conclusion status: afforded. SRC-1 `references/mission_captain.md:191-225,295-324`; `references/mission_auditor.md:3-14,51-55`.

RTE-7 — Existing-project extraction and transformation. User's target and imported source determine the project closure; helpers produce facts from elaboration; planner/generator is required to retain instances, distinguish type/proof dependencies, prune irrelevant declarations and rewrite exact source spans. Extraction conclusion status: wired. Planning/generation and validation workflow conclusion status: afforded. Facts must be re-extracted after edits; source commit/line links provide provenance. SRC-1 `references/upload_full_project.md:14-61,83-99`; `scripts/extract_decl_graph.lean:25-102`; `scripts/extract_sketch_info.lean:101-177`.

RTE-8 — Ordered upload/continuation. Host-written uploader consumes generated files and graph order, persists action/response identities, polls terminal jobs, maps names to IDs and resumes from checkpoint state. Final tag query verifies all nodes reportedly Proved. Conclusion status: afforded. SRC-1 `references/upload_full_project.md:101-123`.

RTE-9 — Route refinement under RTE-5: attempt-to-lesson loop. Agent produces an argument explanation after proof/verification, or a dead-end comment when an approach fails; it persists prose associated with the attempt; later solvers fetch explanations/comments/mentions before choosing or retrying work. This is automatic trace-fed derivation at the instructed-agent layer, even though the host/backend are absent. Manual human commentary remains another write branch. The reason is retained where prose actually explains the argument/failure, and later read instructions expressly consume it. Conclusion status: afforded. SRC-1 `references/prove.md:115-136`; `references/communicate.md:3,64-79,117-122`; `references/mission_solver.md:28-36,52-62`.

RTE-10 — Route refinement under RTE-8: action/API trace to durable upload checkpoint to resumed uploader. Symbolic state shapes later control flow, but the unspecified writer might only copy raw records; whether it produces a qualifying derived artifact is not determinable. One upload task supplies the continuation horizon; persistence across interrupted processes is explicit. Rationale retention: state stores action/IDs, not an explanation of why the proof/decomposition was selected; only the static playbook explains poll-versus-resubmit. Conclusion status: afforded. SRC-1 `references/upload_full_project.md:103-116`.

RTE-11 — Route refinement under RTE-6: captain supplies each selected draft's Lean code/preamble to a fresh auditor. Trigger is assembled/edited draft; selector uses item identity; selected parts exclude source/intent; delivery is agent handoff; later consumer is the independent auditor. There is no implementation or token budget. The resulting read-back is persisted and then consumed by human/moderator. Conclusion status: afforded. SRC-1 `references/mission_captain.md:191-195`; `references/mission_auditor.md:3-14,51-55`.


The following minimum excerpts support the accepted generic records: RTE-2/RTE-5/RTE-9 for retrieval and retained lessons; RTE-4 for conditional reductions; RTE-6/RTE-11 for translation audit and human use; RTE-7/RTE-8/RTE-10 for shipped helper versus prescribed orchestration/checkpoints; RTE-5 for bounded deprecation/deletion. Quotes occur once here and are referenced by lens overlays.

> 2. Read each submission's `explanation` to understand the argument.
> 3. Fetch the Lean source of a chosen submission via `GET /api/v1/submissions/:id/solution` (next section).
> --- `references/discover.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> A key feature: you may import both **Proved and Open** theorems. If you import an Open theorem, the parent's status depends on its children — the parent is Proved when all its children are proved.
> --- `references/prove.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Before attempting an open milestone, read its edit history (`GET /milestones/:id/history`) — an event that removed or replaced a `theorem_id` marks a rejected formalization path, and the captain's `reason` tells you why.
> --- `references/mission_solver.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> - **Log dead-ends.** When an approach fails, post an `attempt` comment referencing the failed `solution`. It saves the next agent the same wall.
> --- `references/communicate.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Faithfulness is the single criterion: each Lean statement must say exactly what the source says, no less and no more. A missing hypothesis makes the theorem false; a missing conclusion makes it a different theorem; a degenerate reading makes it empty. "It compiles and is true in Lean" is not the bar.
> --- `references/mission_captain.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> For each draft item, launch an **independent sub-agent** with a fresh context
> --- `references/mission_captain.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> The orchestration code (a few Python scripts: planner, generator, uploader) is ordinary engineering you write yourself — this playbook gives you the design rules and the failure modes that are expensive to rediscover.
> --- `references/upload_full_project.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Write an **idempotent uploader**: a state file records every action before and after its API call, so an interrupted run (server load, token expiry, killed processes — all of these will happen) resumes with no duplicates.
> --- `references/upload_full_project.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

>   IO.FS.writeFile "decl_graph.jsonl" (String.intercalate "\n" lines.toList)
> --- `scripts/extract_decl_graph.lean` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

>   if s.commandState.messages.hasErrors then
>     for msg in s.commandState.messages.toList do
>       IO.eprintln (← msg.toString)
>     return 1
> --- `scripts/extract_sketch_info.lean` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Placeholder definitions, unprovable junk theorems, or a bad sketch can be retired with a reversible **deprecation** flag. Deprecating a node hides it from discovery (browse, mission views) but never deletes it — anything that already imports it keeps working, and its proof status is unchanged.
> --- `references/contribute.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Returns `204` (no body). Deleting a milestone also deletes its edit history (cascades) — there is no undo.
> --- `references/mission_captain.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

RTE-12 — Documentation conflicts and alternate control prescriptions. No code correction is inferred; conclusion status: uninspected for the actual backend/host resolution. (a) references/prove.md says only explanation is PATCHable by original creator, but contribute.md permits submission deprecation by submitter/captain/admin. (b) discover.md allows any authenticated user to fetch any submission source, while mission_captain.md promises private statements/proofs never observable by another account. (c) discovery says saved problems first, while solver instructions start from human mission choice/milestones/frontier. These are alternate/inconsistent instructions, not an implemented scheduler. (d) upload playbook drops spanless rows after reachability, example README says filter first. Main playbook/helper explanation governs intended general traversal; example cannot establish behavior for dependencies passing through spanless entries. SRC-1 `references/prove.md:154-166`; `references/contribute.md:314-326`; `references/discover.md:3-16,255`; `references/mission_captain.md:330-332`; `references/mission_solver.md:18-24`; `references/upload_full_project.md:29`; `examples/upload_full_project/README.md:33`.

> Pass `{"explanation": null}` to clear it. Setting an explanation echoes the `guidelines` digest back in the response. Max length 50,000 characters. Only the submission's original creator may PATCH. In this JSON body, escape every LaTeX backslash (`\\frac`, `\\ge`) — a raw backslash makes the request fail to parse; the `-F` form field on `/verify` takes them raw.
> 
> Errors:
> - `400` — body contains any key other than `explanation`, wrong type, or oversized.
> --- `references/prove.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> - **Theorem / definition** — `PATCH /api/v1/theorems/:theorem_id` with `{ "deprecated": true }` (`false` un-retires).
> - **Submission (proof / sketch)** — `PATCH /api/v1/submissions/:id` with `{ "deprecated": true }`.
> --- `references/contribute.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> `content` is the exact `solution.lean` the submitter uploaded. Any authenticated user can fetch any submission's source — there is no ownership or status restriction, so you can also read `FAILED`/`CE`/`WA` attempts to see what didn't work.
> --- `references/discover.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> One caveat: private theorems and definitions still occupy the per-environment name space. Someone creating a declaration with a name you already used privately gets the ordinary name-taken error. Name occupancy is the only thing observable from outside — never your ownership, the statement, the proofs, or anything else.
> --- `references/mission_captain.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> - **Drop every row with `startLine: 0` after computing reachability.** These are compiler-generated companions (equation lemmas `*.eq_*`, match auxiliaries `*.match_*`, class internals) with no source span. Reachability may legitimately reach them (a def's `valueDeps` often lists its own `match_1`); that needs no action — each is regenerated automatically when its parent declaration compiles, and none is ever uploaded or subtracted.
> --- `references/upload_full_project.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> Filter out compiler-generated entries first — anything with `startLine: 0` (equation lemmas `*.eq_*`, match auxiliaries `*.match_*`) has no source span and is never uploaded. Then collapse span-sharing members: the `class SumBudget` generates `.mk`, `.budget`, `.rec`/`.casesOn`/`.noConfusion` entries whose spans sit inside the class's own span — the Phase 2 containment rule ("anything whose span is contained in a Def-bundle span is provided by that bundle") folds them all into the class. What remains is the plan:
> --- `examples/upload_full_project/README.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

RTE-13 — Campaign value attestation. Trigger: campaign-flagged proposal review; moderator compares the goal with a template over shared foundation definitions and records its numeric value. Rejection ability: remove campaign flag while mission can launch normally. Admission target is template/value correspondence, not theorem proof; an Open goal may have an attested entry. Timeline date records attestation, not achievement. Proposed updates remain human-adopted/documented; no implemented backend or observed attestation. Conclusion status: afforded. SRC-1 `references/campaigns.md:3-11,89-94,139-159`.

> Approval of a campaign-flagged proposal is also the **value attestation**: the moderator checks that the goal theorem instantiates the template over the foundation definitions, and records the numeric value. Expect one of two outcomes:
> 
> - **It instantiates the template.** The mission launches and its campaign entry is created, with `recorded_at` set to the approval time. The entry does not wait for the goal to be proved: an open bound is a valid entry.
> - **It does not.** The moderator removes the campaign flag and the mission simply launches as an ordinary mission. Nothing else is lost; the mission is exactly as good as any non-campaign mission.
> --- `references/campaigns.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

Revision admission is route-specific. RTE-3 proposes new code guided by source statements, imported lemmas and proof procedures; local compile is a prescribed check, and the remote RTE-4 claims stronger exact-target/no-own-sorry/no-self-import checks. New published formal content is immutable; rejected or criticized statements require replacement/new names, while descriptions/explanations remain editable. RTE-5/RTE-9 write argument/failure prose and optional reasons; no semantic verifier for that prose is supplied. RTE-6 lets humans confirm changed drafts and moderators request replacement; editing a draft clears prior confirmation by contract. RTE-7 proposes mechanical source transforms under dependency/position rules and exact-byte compile/type-diff gates. RTE-8/RTE-10 prescribe checkpointed upload/retry, not shipped transactional recovery. RTE-13 accepts campaign membership/attestation only. These guidelines are readable/addressable instructions and retained knowledge, not an optimizer or model-weight update. SRC-1 `references/mission_captain.md:189-195,223-225,302-324`; `references/upload_full_project.md:90-117`.

> Because you changed what your human would audit, **editing a draft item clears any prior confirmation** — it must be re-confirmed before launch. `DELETE` returns `204` and drops the item from `item_order`.
> --- `references/mission_captain.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

> 1. Stage every `preamble + formal_statement` concatenation and every transformed solution as local libraries and `lake build` them — what compiles is byte-for-byte what you upload.
> 2. Pretty-print the elaborated type of every node in the original tree and in the staged tree (a 20-line `run_meta` with `ppExpr`) and diff; the only acceptable differences are universe display names (`u_1` vs `u_2`).
> --- `references/upload_full_project.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`

Theory-related guidance is contentful: a proof argument says why its conclusion follows; a failed-attempt comment can name why an approach failed; a captain reason can challenge a formalization's fidelity. Formulation and later operative-use routes are afforded through RTE-9 and RTE-2; content-directed criticism and resulting statement/reliance revision are afforded by RTE-6's flags/reports/replacement loop. Addressability is afforded by individually named formal declarations, assumptions, comments and items; helper facts make coordinates wired but do not prove mathematical rationale. Retention of reasons is afforded, contingent on writing/fetching history; missing historical rationale does not exclude criticism. Improved future capacity attributable to these processes remains uninspected without candidate-linked outcomes. Externally hosted model internals are uninspected, so neither presence nor absence of additional internal reasoning is inferred.

### Claims

CLM-1 — Skill claims that exact formal statements plus server Lean verdicts supply a real mathematical guarantee. Conclusion status: claimed. Its warranted intended domain is the checked formal statement and accepted dependency assumptions; translation fidelity and actual backend implementation are separate. SRC-1 `SKILL.md:12,97-99`.

> Prove2me hosts a growing library of open theorems and gives you the tools to discover, create, decompose, and resolve them. Every proof you submit is **type-checked against the target's exact formal statement** by a Lean toolchain on the server, so a verdict from Prove2me is a real mathematical guarantee, not a heuristic.
> --- `SKILL.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`


CLM-2 — README describes an agent skill/working workspace for a collaborative, automatically proof-verified Lean platform. Conclusion status: claimed. The complete artifact is an integration contract and helpers, not the complete hosting/runtime/verifier implementation. SRC-1 `README.md:1-16`.

> This repository contains both the **agent skill**
> --- `README.md` @ `326b972580e0640b1f3739ec7b12d2b34d8d3527`


CLM-3 — Full-project playbook prescribes idempotent resume with no duplicate uploads and compiled, type-preserving mechanical transplantation. Conclusion status: claimed. Source helpers support narrower extraction operations; orchestration is explicitly host-written. SRC-1 `references/upload_full_project.md:5-10,90-116`.

### Evidenced absences

ABS-1 — Bounded absence; conclusion status: absent. inspected instructions, helpers and worked-example description provide no retained recall-dependence experiment or observed benefit of learning from prior attempts. Prevents observed/causal learning and a positive `faithfulness_tested` classification. The source reports compilation of example outputs, which tests a different proposition. SRC-1 `examples/upload_full_project/README.md:3,60-66`; `references/upload_full_project.md:90-95`; `references/mission_auditor.md:3-5`.


ABS-2 — No planner/generator/uploader implementation supplied as the advertised orchestration. Conclusion status: absent within this workspace's shipped scripts and explicit design statement, not a claim about other Prove2Me repositories. Frozen root/scripts file inventory plus `references/upload_full_project.md:10` identifies the two ready-made helpers and tells the host to write orchestration. Prevents wired exact-once/recovery assertions. Source SRC-1; no target execution attempted.

### Behavioral-authority paths

BAP-1 — Solver/host requests retained formal objects, proof source, explanations, histories and discussions through API/files; target statements instruct, prose advises, votes/frontier rank, identifiers route. Horizon later proof task/mission or project. Auditor is a distinct prescribed push on RTE-11. SRC-1 `references/mission_solver.md:16-36`; `references/discover.md:184-255`; `references/mission_captain.md:195`.

BAP-2 — Compiler/verifier consumes symbolic source, imports, formal target and environment; prescribed enforcing checks allow/deny admission and change dependency status. Horizon each job plus later import/ancestor use. Deployment force is uninspected, not established from contract text. SRC-1 `references/prove.md:187-246,292-307`.

BAP-3 — Human compares retained read-back with intended source, confirms changed items and launches; moderator accepts public mission/attestation or sends criticism; private launch bypasses moderation. Channel UI/API proposal/review artifacts; force adoption/veto by prescribed role; horizon mission publication/revision. SRC-1 `references/mission_captain.md:302-324`; `references/campaigns.md:154-159`.

## Runtime account

An enclosing coding agent is the runtime. The supplied skill routes it to setup and reference procedures. The ordinary solver flow reuses local workspace/auth/build state, chooses a theorem/mission, requests prior work and exact source, writes a direct proof/disproof/reduction, locally compiles, submits and polls, then explains results and reads feedback before trying again. The host chooses next actions under text policy; API jobs have their own identities/status. Human authentication and mission approval are prescribed boundaries. The artifact does not enforce host shell/network grants, context isolation or external permissions. Credentials, source files, generated objects and service responses are capabilities available through the external host, not a deployed sandbox established by this repository.

The server contract distinguishes compile success, exact target match, prohibited own sorry/import, accepted conditional reduction and completed parent proof. Open imported child theorems are allowed assumptions; SKETCH_ACCEPTED is not a proof without those assumptions. A parent is said to become Proved once all its children are Proved. Imports are environment- and visibility-scoped; disproof cannot import platform theorems. Local compilation is a weaker diagnostic because own-target stub/import can compile locally despite server rejection. Formal-target identity is the independently named reference for proof checking; there is no expected informal answer oracle. Lean's formal evaluator and human intent comparison have different domains, both external here. Source SRC-1 RTE-3, RTE-4, RTE-6.

Material alternatives: direct solving versus transplanting an existing project; proof versus whole-proposition disproof versus conditional reduction; public human+moderator launch versus private human-only launch; mission/saved-list/frontier selection; campaign attestation; local script extraction versus host-written planner/generator/uploader. The upload mode begins with an already compiled source project and is not a proof-discovery claim. Its source dependency/type/position facts guide byte-range edits, then prescribed build/type comparison checks the exact upload text. Script extraction's narrower wired boundary is distinct from the rest of this mode.

State and recovery: workspace/pins/auth persist by procedure, published formal statements are immutable by contract, candidates/drafts and descriptive prose can change, failed jobs echo inputs, and checkpoint state records action/job IDs. On ordinary retry, code/error/feedback leads to another proposal; after immutable publication, correction uses new nodes with deprecation/links. Deprecation hides discovery but preserves imports and proof status. No guaranteed rollback across multiple async writes or lost-response reconciliation is implemented. Deleting a milestone loses its reason history; unlinking does not revoke membership. RTE-12's access/PATCH contradictions prevent unqualified claims about visibility or exhaustive admission schemas.

Static forcing cases: (1) a correct proof of a weakened or vacuous formal statement can pass formal checking while failing source intent; the separate blind read-back/human comparison addresses that different proposition, by doctrine. (2) SKETCH_ACCEPTED with an Open child is still conditional; only the documented dependency-resolution condition closes it. (3) HTTP202/queued job is not publication; later FAILED or ERROR requires different handling, and response loss before saved ID leaves idempotence unproven. (4) editing source invalidates extracted byte offsets and editing draft invalidates confirmation/read-back; re-extraction/re-audit is prescribed, not supplied end-to-end automation. These are contract/code implications, not observed platform failures.

Decision roles and admission differ: host/model authors and diagnoses; compiler checks formal code; backend records/rejects jobs by advertised rules; humans veto source-faithfulness and launch; moderators assess public proposals/campaign templates. A model-generated explanation is advisory, not an independent answer oracle. Formal exact-target reference comes from the stored theorem; its relationship to intended mathematics remains human/source work. Operations serve open user/mission proof requests, long-running campaigns and bounded existing-project uploads, not a shipped training curriculum. Improvement triggers are failed attempts, verification diagnostics and human/moderator criticism; no measured successor-capacity comparison is admitted.

Guarantee strengths: skill/auditor/source-faithfulness instructions are policy; API immutability/status/visibility promises are protocol claims; helper source traversal/output/error behavior is wired local control conditional on toolchain semantics; exactly-once upload and formal mathematical guarantee are not verified deployment guarantees here. No dynamic check planned. Considered Lean helper/example execution and API acceptance probes; source inspection suffices for the admitted narrow helper claims, while those executions would require excluded environment/service actions and would not establish the whole documented contract. No target command was run.

Read-back audit:

| Route | Immediate return and later consumer | Selection, retention, expiry and evidence limit |
|---|---|---|
| See RTE-1 | Credentials/environment to host/compiler | Existing-file checks;one-hour access / 30-day key contract, refresh rotation; external implementation |
| See RTE-2 | Requested objects/history/source to solver | IDs/name/keyword/tags/status/frontier; pull; alternate priorities RTE-12; no total token budget |
| See RTE-3 | Candidate/source/build diagnostic to host | Exact imports/target; local files; no assured server acceptance |
| See RTE-4 | Async status/dependency state to polling host/later compiler | Job ID/module identity/environment; Open children remain conditional; stale/cycle handling uninspected |
| See RTE-5 | Edited prose/access metadata to later solver | Requested retrieval; deprecation hides discovery but keeps imports; history reasons optional |
| See RTE-6 | Proposal/read-back/review to human/moderator | Item confirmation; edits clear confirmation; published formal content replacement; isolation policy only |
| See RTE-7 | Extracted JSONL to host-written generator/compiler | Project prefix/elaboration/source positions; rerun after edit; macro/self-reference limits |
| See RTE-8 | Job IDs/status to uploader/human | Ordered upload and final tag query; final Proved status claimed; no shipped transaction |
| See RTE-9 | Derived lesson to later solver | Attempts/outcomes→prose retained→explicit scouting; afforded learning, benefit unobserved |
| See RTE-10 | Checkpoint to restarted uploader | Saved action/IDs select poll/resubmit; raw copy versus derived state uncertain |
| See RTE-11 | Draft code to fresh auditor then readback to human | Automatic item identity push; intent excluded; rerun audit after changes |
| See RTE-12 | No independent return; qualifies other routes | Conflicting documentation, no implemented resolution inferred |
| See RTE-13 | Attested value to campaign consumers | Template/foundation comparison; Open entry allowed; no proof upgrade |

## Lens scoping

### Memory/context scope

Full lens triggered by accumulated workspace, mathematical objects, prior attempts/feedback, drafts/history and checkpoint prescriptions. Includes RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 plus accepted refinements RTE-9, RTE-10, RTE-11. Fresh specialist owns analysis/profile; static OBJ-1 is routing doctrine, not learned content. Remote storage/host/model internals excluded; interface affordances are not deployed operation.

### Epistemic scope

Full standalone lens triggered by CLM-1 mathematical warrant, source-faithfulness doctrine, generated formal/code/prose candidates, dependency acceptance and helper transformations. Includes RTE-13 campaign attestation because it grants a different warrant from proving. All material in-boundary routes assessed; external Lean/backend correctness and source mathematics remain uninspected. Separate six-block overlay follows.

## Lens outputs

### Memory/context lens

The accepted specialist finds two distinct kinds of reuse: compilers request symbolic imports/formal targets, while agents request prior argument, failures, criticism and captain reasons. Named retrieval routes establish afforded later use, not storage alone. Local files/Mathlib repository coexist with service-object interfaces; physical backend databases remain unknown. Prose and symbolic content are not model parameters. Host/API writes and human moderation/edits coexist; only the helper extraction transformations are wired here.

The lesson route RTE-9 automatically derives explanations/dead-end prose from attempts for future solvers under the instructed-agent contract, supporting trace_learning=yes at afforded basis. It does not show measured benefit. RTE-10's symbolic checkpoint-to-resume consumer is explicit, but its writer might simply copy raw action/response records. That uncertainty leaves learning_scope and distilled_form not-determinable as complete unions; source/timing still map to tool-traces/trajectories and online. Raw error echoes, counters, history and imported mathematical objects are not silently counted as learned summaries.

Most selection is pull by solver/compiler/uploader. RTE-11 is prescribed identifier-based push: captain selects each retained draft's Lean code/preamble for a fresh auditor without an auditor request, excluding source intent. This is a procedural affordance, not implemented context assembly. Search keywords elsewhere remain pull, not lexical push. Pagination and prose length caps do not bound the full host context.

Curation maps narrowly: edited descriptions evolve; deprecated nodes withdraw discovery reliance without revoking imports/proof; votes/bookmarks/target selection promote salience; failure explanations synthesize; milestone/history deletion forgets. No semantic dedup/consolidation follows from exact-key idempotence or source slicing. Reason retention varies: explanations/attempt comments and fetched history can guide later work; current milestone alone does not retain its optional historical reason. ABS-1's faithfulness-tested=no concerns recall dependence, distinct from mathematical translation audits.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 for Prove2Me revision and separated documentary/helper/reported-operation layers. Question: which supplied routes acquire, formulate, test, accept and reuse mathematical or procedural content, and what does each check license? Assessed families: formalization/proof, local extraction/transplant, async admission/dependency state, human translation audit, feedback/curation, campaign attestation and continuation. External source truth, Lean/kernel/server enforcement and host execution are excluded, preventing whole-service formal reliability or empirical-learning conclusions. CLM-1, CLM-2, CLM-3 are the consequential claims. No candidate-linked platform artifact or run is admitted.

#### 2. Epistemic-object inventory

Generic identity/form/lineage/producer/consumer remain on canonical parts. OBJ-13 carries formal mathematical propositions/definitions and assumptions; OBJ-14 carries informal intended propositions/source attribution; OBJ-15 carries proposed derivations/disproofs/reductions; OBJ-17 supplies reported execution status/diagnostics; OBJ-18 carries conditional dependency/proof-status claims; OBJ-19 gives argument/dead-end claims; OBJ-20 gives read-back and criticism of specific content; OBJ-22 gives source-structure facts; OBJ-23 gives transformed formal code; OBJ-24 supplies goal drafts; OBJ-25 separates value/template correspondence from proof of that value. OBJ-11, OBJ-12, OBJ-16, OBJ-8 and OBJ-9 are access/routing/configuration state. OBJ-21 carries history/access metadata for already inventoried reasons. OBJ-1 is static guidance. Source anchors and part boundaries remain on these records.

#### 3. Authority-route ledger

One function per row. Unless explicitly implemented below, architectural status is doctrine only; this corresponds to afforded interface use in the main analysis, not a wired backend. Observed candidate state throughout is no instance observed. Each row inherits SRC-1 and the named route's anchors. Activation is the stated prescribed phase, not observed execution.

| Route / function | Target; content/update relation | Evaluator/condition, timing and possible result | Force, epistemic license and boundary |
|---|---|---|---|
| See RTE-2 — content transformation | OBJ-13, OBJ-14, OBJ-19, OBJ-20; acquisition/import | Solver requests prior source/argument/history before attempt | BAP-1 advisory/instructive; imported attribution is not new proof |
| See RTE-3 — content transformation | OBJ-13, OBJ-15, OBJ-24; indeterminate formulation | Host derives formalization/proof from source and prior lemmas | BAP-1 proposed formal content; source preservation/ampliation depends on actual candidate |
| See RTE-3 — check/evidence production | OBJ-15; no content change | Local compiler on candidate/imports before submit | BAP-2 local diagnostic only; own-target stub can weaken meaning |
| See RTE-4 — check/evidence production | OBJ-15 versus OBJ-13; no content change | Advertised server exact target/type/sorry/import checks | BAP-2 formal-domain check; conditional imports tracked, encoding truth outside |
| See RTE-4 — disposition/acceptance | OBJ-17, OBJ-18; no content change | ACCEPTED or SKETCH_ACCEPTED versus CE/WA/SORRY/FAILED/ERROR | Permits stored proof/reduction status within dependency assumptions; queued job not acceptance |
| See RTE-4 — retention | OBJ-13, OBJ-15, OBJ-17; no content change | Advertised immutable formal objects and job history | Later source fetch/reuse; retention separate from proof/warrant |
| See RTE-4 — lifecycle integration | OBJ-18; no content change | After verified proof/conditional reduction, attach dependencies; all children Proved closes parent | Formal-dependency use through BAP-2, conditional scope; backend resolution uninspected |
| See RTE-11 — content transformation | OBJ-20; indeterminate read-back | Fresh model sees only selected formal code, emits literal rendering | BAP-3 testimony, no guarantee of faithful interpretation |
| See RTE-6 — check/evidence production | OBJ-13, OBJ-14, OBJ-20; no content change | Human compares intent/read-back; moderator flags specific statements | Source-faithfulness judgment, separate from Lean validity; BAP-3 |
| See RTE-6 — disposition/acceptance | OBJ-24; no content change | Human confirmation/launch, public moderator approval/private bypass | Allows mission adoption under documentary policy; not proof of theorem |
| See RTE-6 — lifecycle integration | OBJ-13, OBJ-20, OBJ-24; no content change | Accepted statements enter mission; criticism causes replacement/new links | BAP-3 scoped adoption; actual candidate sequence unobserved |
| See RTE-9 — content transformation | OBJ-19; indeterminate explanation or ampliative failed-approach conjecture | Host formulates argument/why failed from attempt/outcome | BAP-1 later guidance; no dedicated semantic checker supplied |
| See RTE-5 — retention | OBJ-19, OBJ-20, OBJ-21; no content change | Explanation/comment/history write | Available later, not epistemic acceptance |
| See RTE-5 — operational admission/selection/consumption | OBJ-9, OBJ-19, OBJ-21; no content change | Search/votes/deprecation/history reads | Ranking/discovery reliance changes; imports/proof status survive deprecation |
| See RTE-7 — content transformation | OBJ-22; entailed derivation within Lean elaboration/source-coordinate domain | Shipped helper traverses environment/InfoTree; architectural status implemented | Symbolicfacts for generator, conditional on compiler/source; not mathematical truth/test benefit |
| See RTE-7 — content transformation | OBJ-23; intended non-ampliative reshaping | Host-written skeleton subtraction/renaming | Code-preservation objective only; unexecuted transformations not certified |
| See RTE-7 — check/evidence production | OBJ-23 versus original declarations; no content change | Exact upload byte build + elaboratedtypecomparison | Formal preservation check prescribed; excludes universe-displaydifferences, no source-intentwarrant |
| See RTE-8 — disposition/acceptance | OBJ-17, OBJ-18, OBJ-23; no content change | Poll PUBLISHED/verification statuses and final Proved query | Operational completion under remote contract; no observed jobs |
| See RTE-10 — lineage/freshness/recovery | OBJ-8; non-truth-apt continuation update | Action/ID state drives later poll/resume | Operational routing; no exactly-once implementation or learned rationale |
| See RTE-13 — check/evidence production | OBJ-25; no content change | Moderator compares template/shared definitions/value | Warrants stated template instance/value attribution, not its proof |
| See RTE-13 — disposition/acceptance | OBJ-25; no content change | Moderator attests value or removes campaign flag | Campaign timeline admission even Open; BAP-3 |

RTE-12 is lineage/authority uncertainty: conflicting docs prevent an exhaustive schema/privacy/control guarantee. It grants no new epistemic license. The local script error check is implemented; human/backend checks elsewhere remain doctrine only.

#### 4. Per-object lifecycle disposition

OBJ-13, OBJ-14, OBJ-15 and OBJ-24 through RTE-3, RTE-4 and RTE-6: transformation indeterminate until a concrete source/formalization/proof is available. Translation may preserve or change meaning; a proof may derive a target from stated assumptions; a proposed goal may be a new conjecture. Retained source IDs, formal statements and the prescribed separate formal/fidelity checks preserve inspectable lineage without deciding that content relation. All observed candidate states no instance observed. Needed evidence: exact source intent, formal statement/dependencies, proof bytes and linked verifier/human decisions.

OBJ-19 through RTE-9: argument explanation is indeterminate (faithful derivation rendering versus additional assertions); a claimed general reason that an approach fails can be ampliative. For that ampliative branch: observation/anomaly RTE-4 diagnostics/failed attempt, doctrine only, no instance observed; conjecture RTE-9 lesson, doctrine only, no instance observed; derived consequence not determinable, no instance observed; test/evidence against the stated failure theory not determinable, no instance observed; acceptance criterion for that lesson not determinable, no instance observed; post-acceptance lifecycle integration not determinable, no instance observed. RTE-2 provides prescribed later use, not evidence-consuming epistemic acceptance or improved capacity. Missing: candidate proposition, content-directed criticism, resulting reliance change and assessment.

OBJ-20 read-back/critique through RTE-11 and RTE-6: transformation indeterminate. A blind paraphrase can preserve or distort formal meaning; human comparison is the prescribed check/adoption route. No candidate instance observed, so neither correct criticism nor accepted translation is established. OBJ-18 and OBJ-17: formal/procedural outcomes are documentary outputs; conditional inference from verified children to parent is prescribed formal derivation, with backend/kernel uninspected. Discovery lifecycle not applicable to simple status/diagnostic propagation; no observed verdict.

OBJ-22: non-ampliative/entailed symbolic extraction within elaboration/source-position semantics, RTE-7 implemented; discovery lifecycle not applicable. Exact coverage limits (macro-fabricated references/recursive self-references) and source-edit staleness prevent a universal completeness guarantee. OBJ-23: intended non-ampliative mechanical rewriting; actual preservation indeterminate without before/after type checks. OBJ-25: template-value attestation is non-ampliative identification, discovery lifecycle not applicable to attestation itself; the mathematical bound may be an ampliative conjecture before proof. For that branch, proposal RTE-13 and RTE-3 doctrine only/no instance observed; proof-consequence/test/admission RTE-4 doctrine only/no instance observed; template attestation is not proof acceptance; lifecycle integration after formal acceptance remains doctrine only/no instance observed. No candidate-specific achievement or causal improvement inferred from timeline entry.

No lifecycle record for OBJ-1, OBJ-8, OBJ-9, OBJ-11, OBJ-12 or OBJ-16: no candidate truth-apt output for these operational objects; updates RTE-1, RTE-5, RTE-8, RTE-10. OBJ-21 is history/access transport of separately inventoried content, not a new candidate. Superseded containers inherit part dispositions.

#### 5. System-claim versus route comparison

CLM-1: doctrine supports exact formal checking and dependent closure through RTE-4; implementation of server/kernel uninspected, no observed/causal support. Supported conclusion is an explicit formal-verification contract with pending-assumption and translation boundaries. A real guarantee for deployed service or intended mathematical source is not established.

CLM-2: RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10 and RTE-11 are documented host integration/reuse routes, with RTE-7's helper implementation. Source workspace/skill characterization supported; whole platform execution absent from admitted evidence. Worked-example compilation is reported operation, not platform acceptance or causal learning.

CLM-3: source helpers implement extraction and doctrine supplies exact-byte/type-check and checkpoint principles. No planner/generator/uploader implementation, executed transformation comparison or lost-response recovery trace is admitted. Supported contribution is a specified method and helpers; idempotence and complete preservation remain unverified obligations.

#### 6. Bounded conclusion

The artifact separates mathematical proof, source-faithful formulation, procedural success and reusable explanation. Its strongest executable contribution is extraction of dependency/source facts for a host-written upload workflow. The broader contracts afford formal rejection, conditional reduction tracking, human criticism/replacement and future-agent lesson use. They do not establish that the host obeys the procedures, the backend enforces every promise, or a retained explanation improves future proof work. Campaign value attestation and deprecation have specifically bounded force; neither upgrades proof status. Formal validity is always scoped to the encoded proposition and assumptions, never automatically to source intent.

## Reconciliation

Accepted local proposals map exactly: MEM-OBJ-1→OBJ-9, MEM-OBJ-2→OBJ-10, MEM-RTE-1→RTE-9, MEM-RTE-2→RTE-10, MEM-RTE-3→RTE-11, MEM-ABS-1→ABS-1. Original seed referents remain; heterogeneous parts receive new IDs and explicit superseded dispositions. Profile references expand to those parts without changing values/bases/uncertainties. Additional RTE-12 and RTE-13 and CLM-3 record parent runtime/epistemic distinctions.

All 11 specialist issues accepted: source/metadata/staging proposals retained; positive lesson route and uncertain checkpoint route distinct; mathematical guarantee bounded by assumptions and translation; helper code separated from orchestration and coverage limits; optional reason/history/deletion behavior retained; PATCH/privacy conflicts preserved rather than resolved by inference; competing selection priorities treated as instructions; uploader idempotence not established; example/general spanless ordering conflict retained; affordances not promoted to wired/observed. No substantive correction or new specialist required. The report supplies substantive memory analysis, not independent clearance. Parent owns runtime/epistemic reconciliation; no prior review supplied evidence.

## Bounded synthesis

Prove2Me's supplied workspace is a procedural integration for an external theorem-proving agent. Formal objects and dependency status let proofs be reused, while descriptions, failed attempts, histories and critiques inform future agents. Its local code extracts source facts; most task ownership, model calls, async jobs, proof enforcement and social review reside outside this repository boundary.

For understanding the intended collaboration, the division of warrants is concrete: an Open-child reduction is conditional, a formal proof concerns its exact statement, a human source audit checks meaning, and a campaign attestation checks a template/value. For judging actual server correctness/privacy or recovery, implementation and reached runs would be needed. The internal documentation conflicts remain bounded uncertainties, not evidence of a deployed leak or failure.

The strongest learning contribution is an afforded attempt-to-explanation/dead-end-to-later-solver route. Operative formulated arguments and criticism/replacement are afforded; retained reasons are partially addressable by statement/item/history; improved capacity attributable to criticism is uninspected. A limited reflective route is afforded: agents retain their own failed approaches or formalization history and read it to choose later attempts. Whether that becomes a revised self-theory of the complete theory-building organization is uninspected. Self-improvement in future capability remains uninspected independently of reflection and normalized trace_learning=yes. Source instructions and symbols alone do not demonstrate outcomes.

## Limitations

| Limitation | Affected records | Boundary / prevented conclusion | Resolving evidence |
|---|---|---|---|
| Host/model behavior external | CMP-1, CMP-5, RTE-9, RTE-11 | No enforced context isolation, activation or provider fixity | Host implementation and linked execution |
| Backend/kernel external | CMP-2, CMP-3, RTE-4 | No deployed proof/privacy/visibility/dependency guarantee | Server/checker source and reached tests |
| Documentation conflicts | RTE-12 | No exhaustive PATCH/privacy/scheduler/helper ordering contract | Authoritative reconciled docs/implementation |
| Orchestration absent | ABS-2, RTE-7, RTE-8, RTE-10 | No exact-once upload or proven transform/recovery | Supplied implementation and failure comparisons |
| No candidate-linked run | ABS-1, RTE-3, RTE-4, RTE-6, RTE-9 | No accepted mathematical result or empirical learning benefit | Linked source/code/check/criticism/outcome records |
| Checkpoint derivation unspecified | RTE-10 | Complete learning horizon/form unions not determinable | Exact writer/consumer showing transformation or raw-copy behavior |
| Source truth/encoding external | CLM-1, OBJ-13, OBJ-14 | Formal proof cannot establish intended informal mathematics | Source evidence plus faithful encoding assessment |

## Verification and blockers

### Semantic verification

Checked frozen report/input/source identity, completion and hashes; full specialist report read and all11 issues integrated. Profile scope includes local access/environment and all specified remote interfaces, with afforded basis for unions and wired helper distinctions. Trace-fed lessons and uncertain raw checkpoint route audited together; read-back push identifies captain selector/item payload/auditor; requested API returns remain pull. Object splits preserve identities; no opaque provider weights included as a known form. Warrant/operational force, architecture status and observed candidate state remain separate. All quotations matched full pinned blobs and citation bounds checked before publication. No target execution or prior-review exposure.

### Deterministic validation

`commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-prove2me-01/result.md` passed; final prose and quote refinements are revalidated before publication. Structural checks are not independent semantic clearance.

### Blockers

None.
