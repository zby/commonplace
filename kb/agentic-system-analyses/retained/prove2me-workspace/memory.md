---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Prove2Me_workspace memory: shared mathematical declarations, retained failures and reviews, local mirrors and resumable upload state, without inspected backend persistence."
run-id: AAS-2026-10-14-prove2me-workspace-187ef30582c9-01
source-identity: "https://github.com/prove2me/Prove2Me_workspace"
reviewed-boundary: "38e12f9d215cb103a0f9173ec230a614fcd93b61"
---

# Prove2Me_workspace memory report

## Boundary and evidence

The memory boundary follows the solver, captain, auditor, direct contribution, project upload and workspace-refresh paths in [runtime](runtime.md). It includes shared mathematical content, past attempts, discussion, milestone and review history, navigation metadata, local mirrors, credentials and upload recovery state. The frozen source is SRC-1 in [boundary](boundary.md), commit `38e12f9d215cb103a0f9173ec230a614fcd93b61`. Persistent service storage is a documented contract, not inspected implementation. No live content, agent trajectory, service execution or causal comparison was inspected.

Direct inspection here covers `SKILL.md`, `.gitignore`, `references/mission_solver.md`, `references/mission_auditor.md`, `references/communicate.md`, `references/discover.md`, `references/missions.md`, `references/curate.md`, `references/collections.md`, `references/campaigns.md`, `references/mission_description.md`, `references/upload_full_project.md` and both `scripts/` helpers. Relevant ranges of `references/contribute.md`, `references/mission_captain.md` and `references/lean-setup.md` were read directly; setup, verification and other captain/publication details also use supplied runtime findings. These additions are SRC-1 doctrine/design, except helper code supplies implementation evidence. Example bodies remain available but uninspected: their expected files cannot establish performed conversion or observed reuse.

| Entry or operation | Source paths, SRC-1 | Coverage and limit |
|---|---|---|
| Role loading and persistent workspace | `SKILL.md`, `.gitignore`; supplied setup account | [RT-OBJ-skill](runtime.md#rt-obj-skill), [RT-RTE-workspace-refresh](runtime.md#rt-rte-workspace-refresh), [MEM-OBJ-workspace-files](#mem-obj-workspace-files). Static instructions are not use-derived memory; host reload/compaction is uninspected. |
| Publish/import mathematics; local mirrors | `references/contribute.md`, `references/lean-setup.md`, `references/mission_solver.md`; supplied verification account | [MEM-OBJ-library-declarations](#mem-obj-library-declarations), [RT-RTE-content-publish](runtime.md#rt-rte-content-publish), [RT-RTE-reduction-proof](runtime.md#rt-rte-reduction-proof). Backend admission and closure remain claimed. |
| Scout earlier attempts and failures | `references/discover.md`, `references/mission_solver.md`; supplied `references/prove.md` account | [MEM-OBJ-submission-explanation](#mem-obj-submission-explanation), [MEM-RTE-solver-scouting](#mem-rte-solver-scouting), [RT-OBJ-solution](runtime.md#rt-obj-solution). Raw code is distinct from explanatory prose. |
| Discuss, resolve references and retrieve backlinks | `references/communicate.md` | [MEM-OBJ-mission-comments](#mem-obj-mission-comments), [MEM-RTE-discussion-feedback](#mem-rte-discussion-feedback). Parsed references are not substitute proof content. |
| Milestone changes and rejected formalizations | `references/missions.md`, selected `references/mission_captain.md` passages | [MEM-OBJ-milestone-history](#mem-obj-milestone-history), [RT-BAP-milestone-guidance](runtime.md#rt-bap-milestone-guidance). History can be deleted with the milestone. |
| Blind read-back and moderator correction | `references/mission_auditor.md`, `references/mission_captain.md` | [RT-OBJ-readback](runtime.md#rt-obj-readback), [MEM-OBJ-proposal-reviews](#mem-obj-proposal-reviews), [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit). Fresh-context policy, not implemented isolation. |
| Description editing and retirement | `references/contribute.md` | [MEM-OBJ-description-versions](#mem-obj-description-versions), [RT-RTE-content-publish](runtime.md#rt-rte-content-publish). History API is an afforded read, not an established routine solver consumer. |
| Saves, search, tags, ratings, votes, profiles | `references/discover.md`, `references/curate.md` | [MEM-OBJ-discovery-metadata](#mem-obj-discovery-metadata), [MEM-RTE-solver-scouting](#mem-rte-solver-scouting). Scores are access/prioritization signals, not correctness certificates. |
| Collection curation and campaign templates/timelines | `references/collections.md`, `references/campaigns.md` | [MEM-OBJ-collection-campaign](#mem-obj-collection-campaign). Explicit alternative content-admission and discovery surfaces; no backend implementation supplied. |
| Extract, select, regenerate, resume upload | `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`, `references/upload_full_project.md` | [RT-RTE-project-upload](runtime.md#rt-rte-project-upload), [MEM-OBJ-upload-state](#mem-obj-upload-state). Fact extraction wired; converter/checkpoint implementation uninspected. |
| External model/provider state | supplied runtime model record | [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model). No provider checkpoint, embedding store or model-update path inspected; this prevents conclusions about hidden learning or host memory. |

There is no shipped CLI dispatcher, registered tool server or hook controller to substitute for these instruction-routed paths in the supplied tree inventory. The operative entry surface is the skill's endpoint/reference index plus the two Lean helper entry points. This is a boundary description, not an absence claim about the external harness or platform. SRC-1, `SKILL.md`, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`; [boundary](boundary.md).

## Core ideas

1. **Shared declarations are reusable formal state, not conversation summaries.** Later agents fetch or import source-faithful definitions and theorems; the compiler consumes symbolic declarations while agents interpret associated prose. Open child imports remain assumptions, so reusability does not imply unconditional truth. [MEM-OBJ-library-declarations](#mem-obj-library-declarations), [RT-RTE-reduction-proof](runtime.md#rt-rte-reduction-proof).
2. **Negative experience is deliberately externalized.** Failed source, explanation, discussion attempts and captain reasons are independently retrievable. The solver is asked to consult them before trying again. Retention plus an explicit later reader supports a claimed experience-feedback path, not demonstrated improved capacity. [MEM-RTE-solver-scouting](#mem-rte-solver-scouting), [MEM-RTE-discussion-feedback](#mem-rte-discussion-feedback).
3. **Review records have consumer-specific authority.** A blind read-back testifies about code for human comparison; a moderator report guides captain revision; a captain milestone link tells solvers which declaration to trust. Neither a vote nor a read-back is a Lean equivalence certificate. [RT-OBJ-readback](runtime.md#rt-obj-readback), [MEM-OBJ-proposal-reviews](#mem-obj-proposal-reviews), [RT-BAP-milestone-guidance](runtime.md#rt-bap-milestone-guidance).
4. **Selection is mostly requested retrieval.** Target IDs, mission IDs, search strings, filters, graph roots and pagination select records. No inspected automatic model-context injection or token-budget allocator exists inside this artifact. API page caps are result-count limits, not model-window budgets. Local upload state enables continuation, while the auditor procedure deliberately withholds intent in a separate context. [MEM-RTE-solver-scouting](#mem-rte-solver-scouting), [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit), [MEM-OBJ-upload-state](#mem-obj-upload-state).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-library-declarations
Label: Published theorem and definition content

Source-native identity: platform theorem/definition records, including `formal_statement`, definition code, `preamble`, `natural_language_statement` and `source`. Storage substrate: documented service library, locally mirrored in `Theorems/` and `Definitions/`. Representational form: symbolic Lean declaration/code at compiler consumption; separate natural-language description/citation interpreted by agent or human. Lineage: contributor or captain source translation, or mechanically staged project conversion; provenance is an author-supplied citation, not authenticated origin. Statements remain immutable after publishing, while description/source/tags may change. Open theorem bodies are sorry-stubs, distinct from accepted solution code. Consumers: later solver reads and compiler imports, scoped to the target Mathlib environment. SRC-1, `references/lean-setup.md`, `references/contribute.md`, `references/mission_solver.md`; [RT-RTE-content-publish](runtime.md#rt-rte-content-publish), [RT-RTE-reduction-proof](runtime.md#rt-rte-reduction-proof). Distinct from [RT-OBJ-solution](runtime.md#rt-obj-solution): these are the reusable targets/definitions, not submitted proof attempts.

> For each platform theorem you import, save its `preamble` plus its `formal_statement` verbatim into `Theorems/Thm_<slug>.lean`. The `by sorry` body is expected — locally it builds with a warning, which is fine.
> --- `references/lean-setup.md`

> Foundations you build this way are the most reusable thing you can contribute: every later mission imports them instead of re-deriving them.
> --- `references/mission_solver.md`

Admission: direct contributor submission and external compilation do not require the proposal's human per-item approval; proposal publication does. Compiler acceptance does not certify informal faithfulness. Deprecation changes discovery, not established import validity. Actual persistence/reuse is unobserved.

#### MEM-OBJ-submission-explanation
Label: Submission explanation

Source-native identity: submission `explanation`. Storage substrate: documented editable service field. Representational form: natural-language mathematical argument, not executable proof. Lineage: author writes after or alongside a verification attempt, potentially responding to its verdict; source of authorship can be human or agent, not resolved by endpoint alone. Consumers: human collaborators and later agents scouting submission lists. Distinct from the code/status of [RT-OBJ-solution](runtime.md#rt-obj-solution); can be cleared or revised without revising the immutable attempt. SRC-1, `references/discover.md`; supplied [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof) carries `references/prove.md` mutability evidence.

> Read each submission's `explanation` to understand the argument.
> --- `references/discover.md`

The raw attempt and its status do not automatically yield this derived argument. Software storing a field is not a shipped summarizer. Author-only explanation editing is documented; later semantic reliance remains claimed, not observed.

#### MEM-OBJ-mission-comments
Label: Mission comments and parsed artifact references

Source-native identity: mission comment `body_md`, `tags`, `references[]`, reply linkage and attribution. Storage substrate: documented remote discussion thread. Representational form: natural-language strategy/reference/attempt text; symbolic IDs, tags and reference arrays for navigation. Lineage: collaborator writes experience or strategy; server reportedly parses `p2m:` links on write and re-parses on edit. Snippets are display aids; `references[]` contains locators/status, not complete Lean source or reasoning. Consumers: later solver/captain, comment readers and backlink queries. No raw full agent transcript is supplied. SRC-1, `references/communicate.md`. Compared with [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof), this is a separately mutable retained input, not the proof route itself.

> The server parses these on write and resolves them into the `references[]` array on read.
> --- `references/communicate.md`

> Deletes are soft — the comment is hidden from the default listing.
> --- `references/communicate.md`

Admission is authenticated collaborator posting; author-only edit/delete is claimed. Account-token `is_agent` metadata is not reliable proof of human versus computational authorship: password sessions mark false and older/deleted attribution can be null. Claim support requires the body and linked artifact, not the marker.

#### MEM-OBJ-milestone-history
Label: Milestone target and edit history

Source-native identity: milestone description/link/order and `/milestones/:id/history` events. Storage substrate: documented service records. Representational form: natural-language source target and reason, symbolic theorem ID and field/value changes. Lineage: captain/admin edits; changed title, description or link produces an event; order alone does not. Consumers: later solvers identifying the canonical target and rejected paths. Distinct object underlying [RT-BAP-milestone-guidance](runtime.md#rt-bap-milestone-guidance), which establishes consumer authority rather than the stored event structure. SRC-1, `references/missions.md`, `references/mission_captain.md`.

> Its `milestone_description` is the authoritative spec (usually verbatim from the source paper). Its linked theorem, when present, is the captain-attested canonical formalization of that lemma.
> --- `references/missions.md`

> Deleting a milestone also deletes its edit history (cascades) — there is no undo.
> --- `references/mission_captain.md`

`reason` is optional stored rationale, not inferred criticism. `completed` is computed from current linked theorem status at read time; it is not retained success testimony. Unlinking does not revoke granted membership. Thus target withdrawal, history deletion and membership withdrawal are different operations.

#### MEM-OBJ-proposal-reviews
Label: Proposal moderation reports and item flags

Source-native identity: proposal `reviews` and published-item `flags`/theorem `audits`. Storage substrate: documented permanent service review histories, with proposal reports private to owner/moderators and theorem audits returned by discovery. Representational form: natural-language criticism plus symbolic decision, author and time metadata. Lineage: moderator/human evaluation of mathematical product; no automatic trace-to-method update is established. Consumers: captain before correction/resubmission, and solver reading theorem flags before investing effort. SRC-1, `references/mission_captain.md`, `references/discover.md`. These are separate from the blind testimony in [RT-OBJ-readback](runtime.md#rt-obj-readback); [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit) establishes their loop.

> Read both before touching anything.
> --- `references/mission_captain.md`

> Flags stay attached to their theorems and reports stay in `reviews` permanently — the history is the record, so old feedback below the newest entry is normal, not a standing objection.
> --- `references/mission_captain.md`

A report may carry reasons and localization; actual criticism content and correction are unobserved. Review retention does not guarantee every later solver sees private proposal reports. The theorem's public audit surface and captain's private report must not be conflated.

#### MEM-OBJ-description-versions
Label: Theorem description versions

Source-native identity: `/theorems/:id/description-versions` snapshots. Storage substrate: documented service history. Representational form: natural-language description/reason with symbolic editor/time/original markers. Lineage: description change by submitter or moderator produces history; original has null editor and `is_original: true`. An unedited description has empty history. Consumers: authenticated endpoint reader is afforded, but no specific routine solver step consumes historical description versions. Current description is a documented discovery input. SRC-1, `references/contribute.md`. Separate from [RT-RTE-content-publish](runtime.md#rt-rte-content-publish)'s mutable current metadata and [MEM-OBJ-milestone-history](#mem-obj-milestone-history)'s explicit anti-retry reader.

> Every change to `natural_language_statement` — yours or a moderator's — is snapshotted into the theorem's description edit history, viewable via the **Description edit history** endpoint below.
> --- `references/contribute.md`

This supports history storage/read capability, not exercised feedback or an automatic solver-history injection.

#### MEM-OBJ-discovery-metadata
Label: Saved targets, tags, ratings, votes and profile counters

Source-native identity: saved theorem IDs, theorem tags, rating score/reasoning, theorem/submission votes and user statistics. Storage substrate: documented service account/library metadata. Representational form: symbolic IDs, sets and counts; natural-language optional rating reasons and profile text. Lineage: authenticated user/account saves, votes, rates or edits; tags supplied at publication or replaced later; service derives counts/trust from publication, success and votes. These are navigation/evaluation metadata, not a compressed proof or model weights. Consumers: saved-list discovery, tag filtering, votes-sorted theorem lists and user/profile readers. SRC-1, `references/discover.md`, `references/curate.md`, `references/contribute.md`. Compared with [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof), these are independent persisted selector inputs, not verification verdicts.

> Check saved Open problems first before looking for new ones.
> --- `references/discover.md`

> Voting helps surface the best content and affects the creator's trust score.
> --- `references/curate.md`

Save is idempotent and unsave removes the pointer; repeated same votes toggle off rather than preserve an idempotent write. Human may supply bookmarks, but ordinary authenticated APIs leave per-content human control unresolved. Rating reason storage is afforded; no specific subsequent reader of that reason is established. Counts/trust alone do not establish semantic learning or content trustworthiness.

#### MEM-OBJ-collection-campaign
Label: Collection membership and campaign template/timeline

Source-native identity: collection descriptions/membership/suggestions/editor permissions; campaign template facets, foundation reference items and attested-value entries. Storage substrate: documented service collection/campaign records. Representational form: natural-language descriptions/reasons; symbolic membership, exact decimal strings, template Lean code and goal IDs. Lineage: collection owner/editor manages accepted public mission pointers; authenticated users can suggest with reasons. Campaign proposal creation copies template/reference material, contributor fills the numeric hole, moderator attests an entry; timeline derives from attested entries, not code parsing. Consumers: agent browsing collection context, captain instantiating campaign drafts, solver following campaign entry goals and readers of value history. SRC-1, `references/collections.md`, `references/campaigns.md`. This is an additional navigation/admission surface, not a duplicate of [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit); ordinary proposal launch remains that route.

> Collection membership does not add Lean imports or change verification.
> --- `references/collections.md`

> The campaign's timeline is built from these attested values, not from parsing your Lean code.
> --- `references/campaigns.md`

Collection suggestion acceptance adds membership; decline does not. Repetition keeps original reason/status and cannot reopen review. Campaign entry existence means attestation, not proof: Open goals remain proposed values; `latest_value` uses the most recent recorded Proved goal, not necessarily the preferred/best bound. An entry can be removed by moderator. Template imports instruct common definitions rather than independent redefinitions. Moderator attestation is human admission; ordinary collection editor/account identity alone leaves human versus agent contribution unresolved.

#### MEM-OBJ-workspace-files
Label: Persistent workspace and authentication files

Source-native identity: `credentials.json`, local `Definitions/`, `Theorems/`, `Solutions/`, environment pins and `.lake/`. Storage substrate: persistent filesystem, with credentials/config/builds gitignored. Representational form: symbolic credentials, Lean content and environment configuration; cached compiled artifacts consumed by toolchain, not natural-language agent memories. Lineage: human provides credentials or agent mints key under documented setup; agent mirrors service content and authors solutions; build tools produce cache. Later consumers: next session's setup/authentication and later compilation, not automatic ingestion of every file into model context. SRC-1, `SKILL.md`, `.gitignore`, `references/lean-setup.md`; [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof) supplies setup contract. Separate from [RT-OBJ-skill](runtime.md#rt-obj-skill), which is versioned behavioral guidance, and from [RT-OBJ-solution](runtime.md#rt-obj-solution), which owns proof payload semantics.

> reuse: credentials.json + .lake build may already be there
> --- `SKILL.md`

Mirrors are environment-specific; same name can refer to different content across environments. Gitignore is a version-control omission rule, not encryption or network confinement. Credential expiry and rotation are supplied runtime findings, not inspected backend behavior. No actual persistent user workspace is supplied here.

#### MEM-OBJ-upload-state
Label: Upload extraction facts and resumable action state

Source-native identity: `decl_graph.jsonl`, per-module Stage 2 JSONL, generated platform tree, source pin/rename map, name-to-ID cache and requested uploader state file. Storage substrate: local generated files; action-state format/implementation is not shipped. Representational form: symbolic dependency/position facts and action/ID bookkeeping; generated Lean payloads remain content, not opaque embeddings. Lineage: deterministic Lean extraction over source/elaborated environment; agent-written planner selects and transforms; uploader records before/after API calls. Later consumers: planner/generator and resumed uploader; published downstream consumers belong to [MEM-OBJ-library-declarations](#mem-obj-library-declarations). SRC-1, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`, `references/upload_full_project.md`.

Part of: [RT-RTE-project-upload](runtime.md#rt-rte-project-upload)

This object is the retained-state part of the broader upload route, not another route declaration. Facts retain source positions/dependencies, not the complete mathematical rationale for node promotion. The source commit and rename map preserve lineage; reasons for every selection need not persist.

> IO.FS.writeFile "decl_graph.jsonl" (String.intercalate "\n" lines.toList)
> --- `scripts/extract_decl_graph.lean`

> **Record `submission_id` before polling**, so an interrupted poll resumes by polling rather than resubmitting.
> --- `references/upload_full_project.md`

The extractor programs are wired; resumable action recording is claimed only. A crash between remote admission and recording its returned ID is not proven duplicate-safe by the prose. Source edits invalidate byte-offset facts; regenerate them rather than treating them as portable knowledge.

### Routes

#### MEM-RTE-solver-scouting
Label: Retrieve retained evidence before solving

Part of: [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof)

Endpoints/progression: new target selection → saved/mission/search/graph retrieval → history, discussions, backlinks, audits, submissions and selected source fetch → foreground agent's next attempt. Owner/selector: foreground agent using host HTTP tools and the documented service's filters/order. Retained inputs: the declaration, prior proof code/explanations and feedback objects above. Persistence: service state across attempts; returned data joins current context, with no specified retained model summary. Effects: intended target/approach selection; no new proof is admitted by reading. SRC-1, `references/mission_solver.md`, `references/discover.md`, `references/missions.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: JSON lists/details, explanations and separately fetched exact Lean `content`; `file_path` alone is not a usable source URL.
- Later read-back: prior submissions, captain changes, audits and discussions reach a subsequent solver attempt through requested HTTP results.
- Delegated visibility: inapplicable — this scouting route uses the foreground agent, not an isolated auditor frame.
- Selection predicate: mission priority, milestone order, graph root/open frontier, exact target/submission IDs, keyword/name/tag/status filters, saved status and chosen proof source; frontier is ranked by closability, not semantic similarity.
- Invalidation or expiry: live status/link changes alter selection; comments can be hidden and histories deleted; environment scopes names/imports. No universal memory TTL is specified.
- Activation or effect: agent is told not to repeat rejected/failed paths and to reuse existing results; changed behavior is unobserved.
- Evidence limits: endpoint contracts and instructions only; actual fetched contents, host context fit and compliance were not observed.

> Study existing proof attempts (`GET /theorems/:id/submissions`) — read accepted submissions' explanations and fetch their Lean source (`GET /submissions/:id/solution`), including `FAILED`/`CE`/`WA` attempts to see what didn't work ([discover.md](discover.md)).
> --- `references/mission_solver.md`

Request and delivery are pull-based, not unsolicited supply. Service filtering is symbolic; the agent chooses what to request and how much to interpret. Comments/history default to 20, theorem/submission lists commonly 50, with documented page caps; pagination is not completeness unless the agent follows it. No token budget, salience truncator or host compaction policy is specified. The source explicitly says to fetch exact external references rather than rely on model recollection, but external source retrieval is a workflow instruction, not new evidence acquired in this analysis.

Admission/decision roles for changed reliance: captain supplies attested targets/reasons, human auditors supply flags, agent decides next attempt; software filters and ranks. The retained formal statement is the target oracle; prior scores/failures are evidence, not expected answers. This is open problem work, not a fixed training curriculum. For mathematical theory properties, [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof) supplies the separate assessment; retrieval alone does not establish content-directed criticism or improved capacity.

#### MEM-RTE-discussion-feedback
Label: Externalize attempts into later guidance

Endpoints/progression: agent/human experiences a failed or useful approach → authors `attempt`/`strategy`/`reference` comment with artifact links → service stores text and parses references → later mission/backlink retrieval → solver interprets retained reason and artifact. Owner: collaborator for content, service for claimed storage/indexing, later agent for retrieval/reliance. Distinct from [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof): this route writes shared guidance, not submitted Lean or verdict. SRC-1, `references/communicate.md`, `references/mission_solver.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: comment POST returns `201` and stored comment including parsed references; edits re-parse links.
- Later read-back: future solver reads mission thread or target/submission mentions and follows linked attempt source.
- Delegated visibility: inapplicable — no separate model context is required for discussion posting or reading.
- Selection predicate: writer chooses experience, tags and links; later agent selects mission or artifact, service returns newest-first non-deleted comments/snippets with pagination.
- Invalidation or expiry: author can edit or soft-delete; default reads omit deleted content, optional thread tombstones can help reconstruct replies. No semantic invalidation of stale strategy is specified.
- Activation or effect: requested avoidance of repeated dead-ends and coordination across agents; no observed prevention or reliability improvement.
- Evidence limits: the posted examples are templates, not observed episodes; parsing/indexing and persistence are uninspected backend contracts.

> **Log dead-ends.** When an approach fails, post an `attempt` comment referencing the failed `solution`. It saves the next agent the same wall.
> --- `references/communicate.md`

Write admission is authenticated author posting, not per-comment human approval or verification of mathematical advice. Physical HTTP execution is separate from authorship. Guidance comes from the solver/discussion playbooks. Author can replace or withdraw prose; the raw failed code remains a separate immutable submission. Trace origin is a participant's selected experience, potentially combined with source references, not a complete automatic runtime log. The durable derivative is human/agent-authored commentary, not an implemented trace summarizer. Reasons can persist in text and have an explicit later reader. Whether any actual comment states a whole criticism with blame, iterates it or improves capacity remains uninspected.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-experience-guidance
Label: Retained attempts to solver reliance

Consumer: later foreground solver. Channel: requested comments, explanation, failed source and target audits in tool results; symbolic source may also be compiled. Force: advisory mathematical evidence interpreted under the solver's instruction to scout; not executable permission or host-enforced avoidance. Horizon: subsequent attempts/sessions, subject to visibility, editing, deletion and agent retrieval. Retained rationale can guide strategy, whereas IDs/status counters chiefly locate or prioritize. SRC-1, `references/mission_solver.md`, `references/communicate.md`, `references/discover.md`; evidence passages in [MEM-RTE-solver-scouting](#mem-rte-solver-scouting) and [MEM-RTE-discussion-feedback](#mem-rte-discussion-feedback). Distinct from [RT-BAP-milestone-guidance](runtime.md#rt-bap-milestone-guidance): community attempt evidence is not captain attestation. Delivery/activation and improved capacity remain separate and unobserved.

## Annotations

#### On [RT-OBJ-readback](runtime.md#rt-obj-readback)

Raw-to-derived chain: literal Lean/preamble → fresh-context auditor's natural-language rendering → captain attaches field → human comparison → permanent published testimony → moderator review. Source intent is deliberately excluded from the producer, but must be available to the comparison consumer. Output is not raw model reasoning or a proof-preserving summary of a conversation. `readback_model` is attribution, not model parameter state. Editing the declaration requires regeneration; the producer is independent by instruction only. SRC-1, `references/mission_auditor.md`, `references/mission_captain.md`.

> Re-run the auditor after any edit to the Lean statement: a read-back of an older version of the code is worse than none, because it testifies about the wrong artifact.
> --- `references/mission_auditor.md`

#### On [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit)

Working-context control: captain triggers an auditor invocation, selects only declaration/preamble plus auditor procedure, and withholds informal statement/source/pitch/intent. Only returned testimony is intended to escape into the draft; the host owns frame creation/disposal and any hidden context. This resembles a per-task frame, but the artifact supplies neither enforceable exclusion nor an algorithm for reclaiming accumulated foreground turns. Metadata batching during upload is a different, weaker partitioning request; it specifies roughly 25 nodes but no equivalent blind-input rule. No alternative compaction/checkpoint summary is established. SRC-1, `references/mission_auditor.md`, `references/upload_full_project.md`.

#### On [RT-RTE-content-publish](runtime.md#rt-rte-content-publish)

Memory withdrawal is nonuniform: published Lean replacement uses a new declaration name; deprecation hides default discovery while existing imports/status persist; retirement notes should identify corrected successor; milestone unlinking does not revoke membership; deleting a milestone removes its history. Thus hidden content can remain behaviorally operative in compiler imports or direct reads. SRC-1, `references/contribute.md`, `references/mission_captain.md`.

> When you retire a theorem or definition you submitted, send `natural_language_statement` in the same PATCH with a note appended saying why it was retired and the `theorem_name` of the corrected node that replaces it — a retired node stays readable and importable, so the flag alone leaves the next reader guessing.
> --- `references/contribute.md`

#### On [RT-RTE-project-upload](runtime.md#rt-rte-project-upload)

Curation includes dependency reachability, mandatory instance roots, helper promotion/inlining, skeleton subtraction and renaming. It operates on source code/elaboration facts, not interaction traces. Stage 2 rejects elaboration errors before facts are emitted; generated outputs require exact-payload compilation and type diff. No shipped planner enforces those checks, and dependency/position facts are not already an equivalent rewritten project. Current-run extracted facts qualify as operational state; resumed uploader consumption across an interrupted invocation gives a specified retained-memory horizon. SRC-1, `references/upload_full_project.md`, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`.

## Write side

The admission mechanisms differ from who writes bytes. The contributor or captain proposes mathematical content; external publication compilation admits symbolic nodes, with human confirmation additionally prescribed on proposal launch. Direct publishing and upload-first are counterexamples to universal per-content human approval. Prior work search and source-faithfulness principles guide authorship; successful compilation alone does not establish source equivalence. The formalization/review routes and their theory assessments remain in [RT-RTE-content-publish](runtime.md#rt-rte-content-publish) and [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

Experience capture is explicit authored explanation/commentary, not an inspected automatic learning pass. Raw failed code/status stays separate from explanatory prose and parsed access metadata. Moderator reports and captain reasons preserve criticism for specifically named later readers; description history preserves text/reasons but has only an afforded endpoint reader. Saves/tags/votes alter later access or priority, not the formal claim. Collection editor admission and campaign moderator attestation add alternate selection/recording surfaces. [MEM-OBJ-submission-explanation](#mem-obj-submission-explanation), [MEM-OBJ-proposal-reviews](#mem-obj-proposal-reviews), [MEM-OBJ-description-versions](#mem-obj-description-versions), [MEM-OBJ-discovery-metadata](#mem-obj-discovery-metadata), [MEM-OBJ-collection-campaign](#mem-obj-collection-campaign).

Rejection has retained consequences: failed verification code can be fetched; rejected target links have reasons/history; proposal reviews guide new drafts; failed publication jobs are pollable and listed in the supplied runtime contract. Withdrawal does not uniformly erase downstream use. Comment soft deletion, reversible deprecation, replacement under new names, and irreversible milestone-history deletion have different horizons. No inferred global rollback or automatic purge is warranted. SRC-1, `references/discover.md`, `references/communicate.md`, `references/contribute.md`, `references/mission_captain.md`; [RT-RTE-content-publish](runtime.md#rt-rte-content-publish).

Upload extraction is the inspected automatic transformation: source/elaborated environment → graph/spans → prescribed agent-written conversion → published nodes. Action state → resumed polling is a recovery chain, not a behavioral rule learned from outcomes. Authentication files enable later access, not semantic knowledge. Updated repository instructions can change later agent guidance through [RT-RTE-workspace-refresh](runtime.md#rt-rte-workspace-refresh), but no evidence-responsive revision of their content was observed. No model-parameter change or automatic trace-fed compaction mechanism is established within the inspected artifact; opaque host/provider mechanisms remain uninspected rather than absent.

## Read-back

The material later consumer routes are requested solver scouting, future compiler imports, captain correction from reports/flags, human/moderator read-back comparison, campaign template instantiation, collection/campaign navigation, setup credential reuse and interrupted-upload recovery. Storage capability alone is insufficient: description-version and optional rating-reason endpoints do not establish routine later behavioral consumption. These differences are local to their object records above.

Selection inputs are explicit roots/IDs/filter sets and caller choices. Newest-first feedback can hide older reasons behind pagination; a 20-item response is not the entire retained history. Backlink snippets/IDs identify discussions and sources, not replacements for full reasoning or Lean bytes. Open-leaf closability ranks expected graph closure, while votes and captain ordering express different priorities. No inspected route automatically pushes all retained material into the agent window, determines a token allocation or measures whether the agent used it. SRC-1, `references/discover.md`, `references/missions.md`, `references/communicate.md`.

Working-context management is limited to on-demand playbook reading, demand retrieval and the instructed auditor frame, plus upload metadata batches. The frame returns testimony while withholding intent at production. None establishes foreground trimming, verbatim-tail retention, summary reload, reference-counted context or actual host compaction. Local files and APIs remain reachable by tools, not by an automatically followed in-window pointer. SRC-1, `SKILL.md`, `references/mission_auditor.md`, `references/upload_full_project.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

## Integration issues

- **Submission PATCH contract tension:** supplied [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof) and [RT-OBJ-solution](runtime.md#rt-obj-solution) correctly distinguish immutable code from patchable explanation, but any reading that explanation is the only mutable submission field needs qualification. `references/prove.md` is quoted in runtime as explanation-only, while SRC-1 `references/contribute.md` explicitly permits submission deprecation and broader submitter/captain/admin retirement authority. Both contracts survive; exact backend accepted keys/permissions are unresolved. This prevents claiming one universal author-only submission-edit gate. See [RT-RTE-content-publish](runtime.md#rt-rte-content-publish) and its annotation here.
- **Retirement is not revocation:** captain unlink and deprecation cannot be treated as invalidation of all future dependencies. Existing imports remain, membership persists and deletion can remove anti-retry history. This qualifies memory reliability without correcting the runtime's already bounded account. [MEM-OBJ-milestone-history](#mem-obj-milestone-history), [MEM-OBJ-library-declarations](#mem-obj-library-declarations).
- **Upload idempotency is prescribed, not proved:** recording actions/IDs is intended to support recovery, but no shipped uploader resolves the remote-success/local-recording crash window. This prevents inferring duplicate-free operation from the instruction's label. [MEM-OBJ-upload-state](#mem-obj-upload-state), [RT-RTE-project-upload](runtime.md#rt-rte-project-upload).
- **History capability is not universal feedback:** description versions and rating reasons have no identified routine consumer comparable to milestone reasons, discussions or moderator reports. Do not aggregate all history fields into one exercised learning route. [MEM-OBJ-description-versions](#mem-obj-description-versions), [MEM-OBJ-discovery-metadata](#mem-obj-discovery-metadata), [MEM-RTE-solver-scouting](#mem-rte-solver-scouting).
- **Added source coverage:** collection/editor suggestion review and campaign template/value attestation were not detailed in runtime. They retain materially different selector inputs and admission controls, including attested-but-unproved values. [MEM-OBJ-collection-campaign](#mem-obj-collection-campaign), SRC-1 `references/collections.md`, `references/campaigns.md`. Backend wiring remains uninspected; these additions do not change the frozen boundary.
- **Identity comparison:** no new declaration is asserted to duplicate a supplied referent. The new stored objects distinguish content, histories or state from supplied routes/authority paths. The upload-state object and scouting route explicitly declare containment; read-back, publication, upload and auditor-route details are annotations instead of redeclarations. Mathematical library nodes differ from submitted solutions; community experience authority differs from captain attestation. Reconciliation should preserve these distinctions.

## Limitations and checks

HEAD was rechecked as `38e12f9d215cb103a0f9173ec230a614fcd93b61`, with clean target status. Source identity matches the supplied Git source; added readings stayed in that checkout at its frozen revision. Governing member types, collection, worker rules and record contract were read completely. The analysis used source reads/searches only: no Lean helper/example, model call, service request or target test was run.

The artifact specifies storage, content admission and later consumers but does not implement the service or host. Therefore persistence/enforcement, context isolation, actual feedback activation, improved capacity and causal benefit remain unobserved. Parameter/embedding/checkpoint internals cannot be inferred from this workspace. Static procedure installation is not use-derived memory; raw retention is not a trace-fed behavior update; content/reason retention does not by itself establish learned improvement.

Validation: deterministic output validation passed; it checks form, identities and quotation occurrence, not semantic acceptance or demonstrated operation.
