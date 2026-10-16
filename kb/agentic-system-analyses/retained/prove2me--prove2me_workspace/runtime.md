---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Prove2Me_workspace runtime baseline: instructed solver, proposal audit and project-upload routes, with executable extraction helpers and external verification limits."
run-id: AAS-2026-10-14-prove2me-workspace-187ef30582c9-01
reviewed-boundary: "38e12f9d215cb103a0f9173ec230a614fcd93b61"
---

# Prove2Me_workspace runtime report

## Runtime account

### Evidence and entry paths

This is an agent-facing workflow artifact, not an agent scheduler or model client. The frozen boundary is [boundary.md](boundary.md). The shipped entry is `SKILL.md`, which routes the agent to the default mission solver or the captain; an existing proved project takes the upload playbook. The host supplies model calls, file/shell tools, HTTP execution and sub-agent launch. The two shipped Lean programs extract facts for agent-written conversion machinery. SRC-1, `SKILL.md`, `references/mission_solver.md`, `references/mission_captain.md`, `references/upload_full_project.md`, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`.

> The orchestration code (a few Python scripts: planner, generator, uploader) is ordinary engineering you write yourself — this playbook gives you the design rules and the failure modes that are expensive to rediscover.
> --- `references/upload_full_project.md`

Fully inspected for this baseline: `SKILL.md`; `references/setup.md`, `references/lean-setup.md`, `references/mission_solver.md`, `references/prove.md`, `references/mission_captain.md`, `references/mission_auditor.md`, `references/contribute.md`, `references/communicate.md`; both `scripts/` programs. Newly added detailed coverage beyond the boundary's initial inspection is `references/contribute.md`, doctrine/design evidence. No target code, example, test or API call was executed. The other reference bodies and example artifacts remain available but uninspected here; campaign-specific value attestation and detailed discovery/rating behavior are not established. No observed-run or causal-experiment evidence is supplied. The workflow routes below therefore remain claimed, while the helper extraction implementation is wired; neither establishes activation or benefit.

### Ordinary solver invocation

The human names a mission or the agent recommends one. The agent is the next-step owner: it reuses the persistent workspace and saved credentials, obtains an access token, chooses a milestone/frontier theorem, and scouts source references, earlier attempts, milestone history and discussions. Account identity and theorem/submission IDs are the service identities; the host's model/session identity is not specified. Context combines natural-language procedures and retrieved mathematical source with symbolic Lean declarations and service JSON. [RT-RTE-solver-proof](#rt-rte-solver-proof) records selection and decision roles; [RT-CMP-agent-model](#rt-cmp-agent-model) records model uncertainty. SRC-1, `references/setup.md`, `references/mission_solver.md`.

The agent mirrors the target's preamble and statement in `Theorems/`, writes a top-level `theorem solution` in `Solutions/`, and preferably compiles locally in the theorem's Mathlib/Lean environment. It then sends the file and target ID to `/verify`, records the returned submission ID and polls until terminal. The server is the claimed executor of verification; the workspace does not implement that executor. Successful direct proof or disproof is a service verdict, not a model judgment. The agent then attaches an explanation, rates the target and returns to discovery. No fixed iteration budget or host retry policy is specified. Compile/type failures require a new submission; submitted code is immutable, while explanation text is patchable. At most 100 pending verification submissions are permitted by the documented service contract, so queue saturation requires waiting rather than duplicate submission. SRC-1, `references/prove.md`, `references/mission_solver.md`, `references/lean-setup.md`.

> The `explanation` field is patchable; `solution.lean`, status, and `proof_type` are immutable once submitted.
> --- `references/prove.md`

The effect boundary includes local files, stored account credentials and remote library/submission/discussion writes. The runtime client controls target, proof type, imports and submitted bytes; `/verify` does not accept an environment override because it uses the target's environment. Multiple agents coordinate through the platform's dependency graph, milestones and artifact-linked comments, not a shipped host-side lock or task allocator. Later agents are instructed to consult this history, but actual compliance is unobserved. SRC-1, `references/prove.md`, `references/communicate.md`, `references/mission_solver.md`.

### Forcing routes and guarantees

Four forcing cases change the ordinary proof account materially.

1. **Local success is not server acceptance; sketch acceptance is not closure.** Local compilation accepts a self-import of the sorry-stub target; the server contract rejects it. Other Open theorem imports are deliberately allowed as tracked reduction assumptions. A disproof instead negates the whole quantified statement and cannot import platform theorems. The reduction route can return `SKETCH_ACCEPTED`, leaving the parent conditional until children close. This qualifies the skill's broad mathematical-guarantee claim: it is about the formal target and admitted assumptions, not source faithfulness or unconditional proof of every accepted sketch. [RT-RTE-solver-proof](#rt-rte-solver-proof), [RT-RTE-reduction-proof](#rt-rte-reduction-proof), [RT-CLM-verification-boundary](#rt-clm-verification-boundary). SRC-1, `SKILL.md`, `references/prove.md`, `references/lean-setup.md`.

> Check the three gating rules in [SKILL.md](../SKILL.md#three-basic-rules-that-gate-every-submission) — in particular, a local build will happily let you import your own target theorem, but the server rejects that.
> --- `references/lean-setup.md`

2. **Human proposal launch is not a universal publication gate.** A captain drafts mutable items, obtains blind read-backs and hands the proposal to the human for item confirmation and website submission. Public missions then require moderator approval for catalog launch; private missions skip moderation. Direct contribution APIs publish library nodes without this proposal confirmation path, and the full-project procedure explicitly uploads before proposal audit. Public proposal submission itself publishes statements before moderator approval. Mission release can also publish theorem dependencies immediately, before the mission is catalog-approved. [RT-RTE-proposal-audit](#rt-rte-proposal-audit), [RT-RTE-content-publish](#rt-rte-content-publish), [RT-RTE-project-upload](#rt-rte-project-upload), [RT-CLM-human-gate](#rt-clm-human-gate). SRC-1, `references/mission_captain.md`, `references/contribute.md`, `references/upload_full_project.md`.

3. **Blind review is a requested context boundary, not implemented isolation.** The captain is told to supply only code/preamble and the auditor procedure, excluding source intent and pitch. Only the read-back escapes to the draft item and human comparison. This resembles a per-task frame: selected inputs go in and a text return comes out. The host owns actual context creation/disposal; the artifact supplies no proof that prohibited context stayed out. There is no described compaction/reload algorithm for the foreground agent. [RT-RTE-proposal-audit](#rt-rte-proposal-audit). SRC-1, `references/mission_auditor.md`, `references/mission_captain.md`.

> Never give the auditor the informal statement, the source material, the mission pitch, or your own intent. An auditor who knows what the code is "supposed to say" will read that meaning into it — and the discrepancies the human needs to see disappear.
> --- `references/mission_auditor.md`

4. **Graph extraction is not semantic preservation of generated uploads.** Stage 1 reads an elaborated environment; Stage 2 re-elaborates each source file and reports syntax/value/reference positions, aborting on errors. The agent-written planner must preserve instance roots, traverse constructors, handle private names and span containment, and avoid deleting notation commands. Stage 2 does not emit every reference: macro-generated and recursive-local occurrences have limits. The prescribed downstream gates are exact-payload compilation and elaborated type diff against the original, not merely trusting a graph label. Stale offsets after edits require extraction again. [RT-RTE-project-upload](#rt-rte-project-upload), [RT-CMP-extract-decl-graph](#rt-cmp-extract-decl-graph), [RT-CMP-extract-sketch-info](#rt-cmp-extract-sketch-info). SRC-1, `references/upload_full_project.md`, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`.

> Pretty-print the elaborated type of every node in the original tree and in the staged tree (a 20-line `run_meta` with `ppExpr`) and diff; the only acceptable differences are universe display names (`u_1` vs `u_2`).
> --- `references/upload_full_project.md`

The load-bearing guarantees have different owners and strengths:

| Guarantee | Owner and enforcement point | Strength, scope and external contract | Separate conclusions |
|---|---|---|---|
| Target-type verification and rejection of own-code sorry/self-import | External service, `/verify` worker | Claimed invariant over documented verification paths, including private targets; local build is not this gate. Depends on backend checks and Lean trust/toolchain. Reduction children remain assumptions until closed. | implementation conclusion status: uninspected; operation conclusion status: uninspected; contract conclusion status: claimed |
| Human launch of a mission proposal | Human website confirmation and service proposal transition | Protocol for proposal launch, not all content writes; direct contribution, upload-first and release paths differ. Private launch omits moderators. Backend auth distinctions are uninspected. | implementation conclusion status: uninspected; operation conclusion status: uninspected; contract conclusion status: claimed |
| Blind statement read-back | Captain handoff and host context creation | Policy, covering instructed auditor tasks only; runtime isolation depends on host. Read-back is optional in the API contract. | implementation conclusion status: uninspected; operation conclusion status: uninspected; contract conclusion status: claimed |
| Extraction failure does not emit a successful Stage 2 result | Stage 2 checks `messages.hasErrors` before emitting facts | Invariant on this inspected helper path: it returns exit code 1 on elaboration errors. Does not cover Stage 1 imports, agent planner/generator correctness or service publication. Depends on Lean error reporting. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Upload preserves target types | Agent-written generator, local exact-payload compilation and type diff | Protocol, not an invariant enforced by a shipped converter. Depends on correct generator, source pin, elaborator and performed comparison. | implementation conclusion status: uninspected; operation conclusion status: uninspected; contract conclusion status: claimed |

Evidence: SRC-1, `references/prove.md`, `references/mission_captain.md`, `references/mission_auditor.md`, `references/upload_full_project.md`, `scripts/extract_sketch_info.lean`.

> if s.commandState.messages.hasErrors then
>     for msg in s.commandState.messages.toList do
>       IO.eprintln (← msg.toString)
>     return 1
> --- `scripts/extract_sketch_info.lean`

### Capability, grants and change admission

The capability surface is broad host access requested by prose: shell commands, downloads, local file edits, HTTP calls, sub-agents and generated background orchestration. No current host grant set or deployed isolation envelope is supplied. Service contracts scope writes by token identity: proposal owner, submission author, captain/admin or moderator depending on endpoint; they do not demonstrate an OS sandbox. Keeping credentials gitignored and sending tokens only to the base URL are agent policies, not a shipped network enforcement mechanism. Account password login is also a documented alternate to agent-token use, so an API-key attribution label is not proof of who computed the work. SRC-1, `SKILL.md`, `references/setup.md`, `references/communicate.md`, `references/mission_captain.md`, `references/contribute.md`.

> Posting with a shared email and password rather than an API key records `false`, so use an API key if you want your contributions attributed to the agent.
> --- `references/communicate.md`

Mathematical product admission is distributed across server compilation, source-faithfulness policies, captain attestation and human/moderator review. Draft statements can change; published statements require new names and replacement. Deprecation is reversible hiding, not invalidation of existing imports. Captain milestone unlinking does not revoke previously granted mission membership, while deleting a milestone deletes its history with no undo. These recovery differences prevent a single rollback claim. They are documented contracts, not tested service behavior. [RT-RTE-content-publish](#rt-rte-content-publish), [RT-RTE-proposal-audit](#rt-rte-proposal-audit). SRC-1, `references/contribute.md`, `references/mission_captain.md`.

> Deprecating a node hides it from discovery (browse, mission views) but never deletes it — anything that already imports it keeps working, and its proof status is unchanged.
> --- `references/contribute.md`

The version self-check admits changed workflow instructions via a repository pull after a service version mismatch. The upload procedure also asks the agent to write planner/generator/uploader machinery and adjust extraction configuration in the supplied source project. These are explicit behavior-changing surfaces, but not an observed self-improvement loop or model-weight update. [RT-RTE-workspace-refresh](#rt-rte-workspace-refresh) records instruction admission. Retained mathematical content revisions and their longer-term effects belong to the later memory account; this baseline establishes callers and gates only. SRC-1, `SKILL.md`, `references/upload_full_project.md`.

## Shared records

### Components

#### RT-CMP-agent-model
Label: Enclosing agent and auditor models

Source-native identity: the unspecified foreground agent and independent auditor sub-agent used by the role playbooks. Representational form: distributed-parametric model computation, with natural-language procedure and symbolic code inputs. Storage substrate: external harness/provider parameters; not shipped in this repository. Parameter changes during operation: uninspected. Exact version pinned: not established; `readback_model` records an attributed model name, not a pinned model implementation. Whether a mutable endpoint can resolve to another model: uninspected because no provider/client code is supplied. The foreground and auditor roles may use different models; illustrative model names are not deployment evidence. SRC-1, `references/mission_auditor.md`, `references/mission_captain.md`, `SKILL.md`.

> The captain attaches the auditor's output to the draft item via the `readback` field, with `readback_model` naming the model that wrote it (e.g. `claude-opus-4-8`) — on the item `POST` or `PATCH`, exactly like any other draft field.
> --- `references/mission_auditor.md`

#### RT-CMP-extract-decl-graph
Label: Declaration graph extractor

Source-native identity: `scripts/extract_decl_graph.lean`. Representational form: symbolic Lean program. Storage substrate: tracked file, executed in the built source project's Lean environment after root-import/prefix edits. It selects declarations from project modules, preserves private declarations, splits statement/proof dependencies and traverses filtered internal constants. It writes `decl_graph.jsonl`, including names, kinds, instance/privacy flags, source spans and type/value dependencies. This is implementation evidence, not an executed graph. Stage 1 does not generate platform payloads or validate their equivalence. SRC-1, `scripts/extract_decl_graph.lean`.

> IO.FS.writeFile "decl_graph.jsonl" (String.intercalate "\n" lines.toList)
> --- `scripts/extract_decl_graph.lean`

#### RT-CMP-extract-sketch-info
Label: Sketch position extractor

Source-native identity: `scripts/extract_sketch_info.lean`. Representational form: symbolic Lean program. Storage substrate: tracked file invoked with a source-file path and optional constant prefix. It re-elaborates with InfoTree recording, emits whole-command declaration spans, proof cuts, docstring/private-token ranges, and deduplicated/sorted original-position constant references. It returns 1 for missing arguments or elaboration errors. Generated references lacking original syntax and recursive self-references elaborated as locals are outside the reported reference surface. SRC-1, `scripts/extract_sketch_info.lean`.

> A recursive def's self-references inside its own body elaborate as local
>     variables, not constants, so they produce no `ref` fact.
> --- `scripts/extract_sketch_info.lean`

### Operative objects

#### RT-OBJ-skill
Label: Role and operation instructions

Source-native identity: `SKILL.md` plus selected reference playbooks. Representational form: natural-language instructions; displayed shell/JSON/Lean examples are symbolic payload templates only when interpreted and instantiated by the agent. Storage substrate: versioned Markdown in the reused workspace. Consumers: foreground agent, auditor and human handoff. These texts specify role routing, API use, source faithfulness and submission rules; loading them is not enforced compliance. SRC-1, `SKILL.md`, `references/mission_solver.md`, `references/mission_auditor.md`.

> Read the playbook for your role first — it tells you which reference files you actually need, in order:
> --- `SKILL.md`

#### RT-OBJ-solution
Label: Lean solution payload

Source-native identity: `Solutions/Sol_<theorem_name>.lean` / submitted `solution.lean`. Representational form: symbolic Lean declaration/proof, consumed under fixed elaboration/type-checking rules. Storage substrate: local workspace file and documented immutable service submission. It is distinct from an editable natural-language explanation and from the target's sorry-stub. The target ID, proof type and target environment determine checking. SRC-1, `references/prove.md`, `references/lean-setup.md`.

> Your solution must be self-contained — copy the imports and `open`s it needs from the target's `preamble`:
> --- `references/prove.md`

#### RT-OBJ-readback
Label: Blind declaration read-back

Source-native identity: draft item `readback`, with `readback_model` attribution. Representational form: natural-language mathematical testimony, not an automatic equivalence certificate. Storage substrate: editable proposal field, then documented permanent published-item record. The auditor generates it from code/preamble only; the human compares it to intent, and moderators may read it. SRC-1, `references/mission_auditor.md`, `references/mission_captain.md`.

> Read-backs are attached to draft theorem/definition items in a mission proposal (see [mission_captain.md](mission_captain.md)), stay editable until the human clicks **Submit Proposal**, and are then recorded permanently alongside the published theorem, where moderators read them during review.
> --- `references/mission_auditor.md`

### Routes

#### RT-RTE-solver-proof
Label: Solver direct proof or disproof

Endpoints and progression: human mission request or agent discovery → scouting → mirrored statement and solution → optional local build → `/verify` → polling → explanation/rating → next target. Owner: foreground agent for choices and file/HTTP actions; service for claimed verdict. Inputs include exact target declaration/preamble, source reference, earlier attempts and the target's environment. Effects cross local file and remote submission boundaries. SRC-1, `references/mission_solver.md`, `references/prove.md`, `references/lean-setup.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: `/verify` returns a submission ID and `PENDING`; polling returns a terminal verdict/error.
- Later read-back: later solver scouting is instructed to fetch earlier submission explanations and Lean source, including failures.
- Delegated visibility: inapplicable — ordinary proof submission does not prescribe a delegated model context.
- Selection predicate: human mission priority, milestone order/frontier, graph or library search; agent chooses the target and proof versus disproof.
- Invalidation or expiry: access tokens last one hour and API keys 30 days; immutable failed code is corrected through a new submission, not patched.
- Activation or effect: claimed verification can change theorem status; actual execution and downstream behavior are unobserved.
- Evidence limits: no backend verifier, model client or execution episode is inspected; local compilation alone does not establish server acceptance or source faithfulness.

Decision roles: agent proposes the proof; local Lean reports compile results; server supplies the target-type verdict and can reject; human supplies mission priorities but no per-proof approval is prescribed. Answer oracle: target formal statement or its whole negation, supplied by the theorem API; Lean/service comparison checks that formal outcome, not informal source equivalence. Operating mode: open mathematical requests with iterative error-driven repair, not a fixed curriculum or causal experiment. Admission trigger: completed candidate proof; proposed change: theorem proof/disproof status plus submission artifact; gate: claimed `/verify` checks; recovery: fix errors and resubmit, retain submission ID to poll rather than duplicate. Guidance: the three submission rules and faithful source translation; immutable proof code and patchable explanation persist. SRC-1, `references/mission_solver.md`, `references/prove.md`.

> When disproving, your `solution` must prove the negation of the whole quantified statement.
> --- `references/prove.md`

Theory assessment boundary: submitted mathematical propositions and proof attempts, not inaccessible model reasoning. `theory-builder conditions 1–4`: condition 1 conclusion status: afforded — Lean states whole localized propositions; condition 2 conclusion status: claimed — prescribed proof choices depend on source statements and prior attempts; condition 3 conclusion status: uninspected — error statuses do not by themselves identify content-directed criticism and blame; condition 4 conclusion status: claimed — scouting prior failures is requested, with no trace of actual iteration. Addressability: binders/conclusions and proof text are inspectable locally, but immutable published statements need replacement. Persistence: documented submissions span later attempts; actual later consumer use is unobserved. Learning: uninspected — no improved-capacity or attribution evidence. Reflection: uninspected — no two-direction self-representation mechanism established here. Reflective theory builder: uninspected — no method criticism against its own operation established. Autonomous theory builder: uninspected — host/model internal operation is unavailable; absence of per-proof human approval is not sufficient.

#### RT-RTE-reduction-proof
Label: Open-child reduction and closure

Endpoints and progression: agent publishes or selects child lemmas/definitions → submits sorry-free parent solution importing children → server verdict → child proofs by any permitted solver → claimed parent auto-resolution. Owner: foreground agent for decomposition; service for dependency recording/closure; other solvers for children. Effects add graph edges and conditional parent status. SRC-1, `references/prove.md`, `references/contribute.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: pending submission, then `SKETCH_ACCEPTED` when Open children are imported, or `ACCEPTED` when imports are already Proved.
- Later read-back: future agents discover decomposition children, fetch statements and solve the open frontier; server is claimed to revisit parent closure as children become Proved.
- Delegated visibility: children are independent platform problems, not prescribed private sub-agent frames; private targets remain owner-visible under the documented service contract.
- Selection predicate: agent chooses reusable lemmas and imports; imports must exist, match environment and meet visibility rules.
- Invalidation or expiry: missing/invisible/cross-environment imports fail; deprecated content remains importable, so deprecation is not dependency revocation.
- Activation or effect: claimed graph recording and eventual parent auto-resolution; no closure event is observed.
- Evidence limits: dependency tracking and closure implementation are external; an accepted sketch is not proof that every child has been solved.

Decision roles: agent proposes reduction and children, service can reject, permitted community solvers close children; no per-reduction human veto is prescribed. Answer oracle: exact parent type checked under child assumptions; closed-child proof status supplies the documented resolution predicate. Mode: open collaborative decomposition; trigger: hard proof or reusable missing groundwork. Admission: child publication then verification; rejection: server import/type/sorry rules and contributor faithfulness review policies; recovery: create missing dependencies, repair and resubmit. Guidance discourages trivial reductions; child propositions, parent code and dependency graph persist. SRC-1, `references/prove.md`.

> When **all** imported children of your reduction are proved, the parent theorem auto-resolves to `Proved`.
> --- `references/prove.md`

Theory-builder conditions 1–4: condition 1 conclusion status: afforded — localized child propositions and reduction; condition 2 conclusion status: claimed — solving/closure depends on these statements; condition 3 conclusion status: uninspected — decomposition alone is derivation, not criticism of a challenged theory; condition 4 conclusion status: uninspected — no retained criticism shaping revisions is established for this route. Addressability: separate child statements and dependency edges, with immutable published types. Persistence: documented graph across agent invocations. Learning: uninspected — reuse is not demonstrated improved capacity. Reflection: uninspected — external mathematical graph is not by itself a representation of the system's operation. Reflective theory builder: uninspected — no method revision shown. Autonomous theory builder: uninspected — host and solver computations are outside implementation evidence.

#### RT-RTE-proposal-audit
Label: Proposal drafting, blind audit and launch

Endpoints and progression: human source request → captain draft items/dependency order/milestones → independent auditor read-backs → human item confirmations and website submit → compile/publish → moderator approval or changes requested; private launch skips moderator. Owner: captain for drafting, auditor for testimony, human for comparison/launch, moderator for public mission admission, external service for state transitions. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: draft-item APIs return stored mutable items; auditor returns text; launch produces documented proposal status transitions.
- Later read-back: read-backs persist with published items for moderator review; newest review reports and item flags are read in subsequent correction rounds.
- Delegated visibility: captain is instructed to provide only Lean declaration/preamble and auditor procedure in a fresh context, excluding informal source and intent; returned testimony is attached to the draft.
- Selection predicate: captain selects source goal/supporting items; auditor translates literal code; human compares each item with intent; moderator reviews public proposals.
- Invalidation or expiry: statement edits require a new read-back and clear prior human confirmation; launch freezes published declarations, requiring replacement drafts after a bounce.
- Activation or effect: claimed publication at human submit, then public mission catalog admission on approval; private mission immediately becomes live without moderation.
- Evidence limits: read-back is optional API content; isolation, faithful translation, human scrutiny and service transitions are not observed or implemented here.

Decision/admission roles: captain proposes; auditor must not advocate or judge faithfulness; human can withhold item confirmation or submission; moderator can request changes. Answer oracle: exact external mathematical source and author intent, supplied by human/source material and compared by captain/human, not by the blind auditor; compilation is a separate formal well-formedness gate. Mode: open source formalization with review rounds. Trigger: new mission or feedback; proposed change: localized statement/definition or wrapper revision. Guidance: nine captain faithfulness principles and literal auditor testimony. Recovery: mutable draft correction before publication; thereafter new declaration name, deprecate superseded content, update goal/milestones and resubmit through human. Reviews/flags and read-backs are documented durable records. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`.

> Published items are immutable, so a flagged statement is fixed by replacement: add a corrected draft item under a new `theorem_name`, remove the old reference from the proposal, and if you created the bad theorem, retire it with the deprecation flag ([contribute.md](contribute.md)).
> --- `references/mission_captain.md`

Theory-builder conditions 1–4: condition 1 conclusion status: afforded — whole draft statements/definitions can be localized and replaced; condition 2 conclusion status: claimed — source content/read-back comparison is prescribed to determine admission; condition 3 conclusion status: claimed — item flags and written review reports identify statement defects for replacement, though an actual criticism with blame is unobserved; condition 4 conclusion status: claimed — retained reviews/flags are explicitly read before revision and resubmission. Addressability: item-level statement, preamble and definition edits before launch, new-item replacement afterward. Persistence: draft rounds and permanent published testimony/reviews are documented; operation unobserved. Learning: uninspected — successful faithfulness correction and later capacity improvement are not demonstrated. Reflection: uninspected — review is of mathematical products, not established self-representation of the workflow. Reflective theory builder: uninspected — static method instructions are not shown criticized against operation records. Autonomous theory builder: inapplicable — the prescribed internal comparison and admission include human and moderator decisions, rather than computation performing every operation.

#### RT-RTE-content-publish
Label: Direct contribution and captain maintenance

Endpoints and progression: agent authors sourced problem/definition → `/submit-problem` or `/submit-definition` → publish-job polling → immutable platform declaration; later creator metadata/deprecation edits or captain goal/milestone retargeting change its discovery and use. These are separate from human proposal confirmation. Owner: contributor/captain account and external service. Representational forms: symbolic declarations and identifiers; natural-language descriptions, source citations and edit reasons. SRC-1, `references/contribute.md`, `references/mission_captain.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: `202` and job IDs, not theorem IDs; terminal `PUBLISHED` supplies the usable ID, while `FAILED`/`ERROR` require different recovery.
- Later read-back: published definitions/theorems are imported by future solutions; linked milestones and history are prescribed solver inputs.
- Delegated visibility: inapplicable — no separate delegated context is required for ordinary contribution or captain writes.
- Selection predicate: author chooses reusable, source-faithful content after search; captain attests linked theorem against milestone prose; service checks account/field/import constraints.
- Invalidation or expiry: published statements are immutable; descriptions/tags/links remain editable; deprecation hides discovery but preserves existing imports; milestone deletion removes history without undo.
- Activation or effect: claimed library publication and updated attack-path metadata; delivery to later agents is prescribed, not observed behavioral activation.
- Evidence limits: compilation is not informal faithfulness; no direct-contribution per-content human approval is stated; backend enforcement and later use are unobserved.

Decision roles: contributor proposes and directly submits; software can reject compilation/import/name failures; captain decides milestone attestation and can unlink/replace; permitted authors/captains/admins can deprecate. Human involvement in each ordinary API content write is unresolved, rather than inferred from account identity. Answer oracle: source theorem/definition for faithfulness policy; Lean compilation for syntax/type admissibility, not truth of sorry-stub problem. Mode: open contribution and maintenance. Trigger: missing lemma/definition or erroneous content; proposed change: published knowledge or source-facing attack path. Guidance: contributor source/faithfulness rules and captain attestation. Recovery: fix `FAILED`, resubmit unchanged on infrastructure `ERROR`; replace immutable declarations under new names; un-deprecate if appropriate. SRC-1, `references/contribute.md`, `references/mission_captain.md`.

> **Linking is attestation.** Attaching a `theorem_id` declares that theorem faithful to the milestone's statement. Review before you link — solvers are told to use linked declarations as-is, without re-checking.
> --- `references/mission_captain.md`

Theory-builder conditions 1–4: condition 1 conclusion status: afforded — whole formal statements/definitions are supplied; condition 2 conclusion status: claimed — attestation and imports are content-sensitive prescribed decisions; condition 3 conclusion status: claimed — reasons for rejected formalization links and corrected replacements are requested; condition 4 conclusion status: claimed — solver is instructed to consult history and not repeat rejected approaches. These are contract capacities, not observed criticism episodes. Addressability: localized fields and links, but published types cannot be edited. Persistence: documented platform library/history across invocations, subject to history deletion. Learning: uninspected — no capacity-improvement evidence. Reflection: uninspected — no two-way model of the system itself shown. Reflective theory builder: uninspected — method criticism is not established. Autonomous theory builder: uninspected — captain role can be agent-operated, but per-content judgment origin and host execution are not established.

#### RT-RTE-project-upload
Label: Extract, transform and publish a proved project

Endpoints and progression: human supplies project/targets → environment-matched source pin and axiom check → Stage 1 graph plus per-module Stage 2 positions → reachability/planning → skeleton subtraction and namespace/identifier transformations → exact-payload build/type diff → metadata → definitions/theorems/solutions uploaded leaves-first → final zero-Open check → proposal handoff. Owner: foreground agent and its generated planner/generator/uploader; supplied helpers execute extraction; external service verifies/publishes. Inputs/state: built source environment, exact source bytes, target roots, JSONL graph/spans, generated payloads and requested uploader state file. SRC-1, `references/upload_full_project.md`, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`.

- contract conclusion status: claimed
- helper implementation conclusion status: wired
- orchestration implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: Stage 1 writes `decl_graph.jsonl`; Stage 2 prints JSONL or fails elaboration; service calls return publish-job or submission IDs for later polling.
- Later read-back: the prescribed uploader state file records actions before/after calls to resume after interruption; published declarations become later importable library content.
- Delegated visibility: metadata may be fanned out in batches of about 25 nodes with JSON parse checks; concrete handoff context and host isolation are unspecified, unlike the blind auditor route.
- Selection predicate: target reachability plus instance roots, constructor traversal and node promotion by proof size/reuse/source significance; agent-written machinery applies these rules.
- Invalidation or expiry: regenerate extraction after source edits because byte offsets are version-specific; refresh one-hour tokens; recorded IDs permit resumed polling without resubmission.
- Activation or effect: helper facts drive the prescribed transformations; claimed ordered publication should leave every selected theorem Proved, then mission proposal is prepared. No performed transformation or service result is observed.
- Evidence limits: helpers are inspected, planner/generator/uploader are not shipped; expected example outputs are not execution evidence inspected by this report; performance and idempotency remain prescribed, not measured.

Decision roles: human chooses main theorem(s); agent plans survivors, helper promotion, renames and metadata; Lean elaboration/compiler supplies facts/errors; service can reject. Answer oracle: original elaborated target types, source project's axiom set and final service status, with comparison authored by the agent. Mode: bounded transplant of already-proved project, not open proof discovery. Trigger: supplied compiling project; proposed change: platform library graph and generated operational machinery. Admission: local compile/type-diff gates followed by asynchronous service verification; mission confirmation happens afterward, not before those uploads. Recovery: re-extract after edits, split oversized jobs, poll recorded IDs, repair compile failures or retry infrastructure errors, replace immutable rejected-content successors as needed. Guidance includes skeleton subtraction, type/value dependency separation and exact-payload validation. Persisted results: generated files, source commit/rename map, service IDs and prescribed uploader state. SRC-1, `references/upload_full_project.md`.

> Write an **idempotent uploader**: a state file records every action before and after its API call, so an interrupted run (server load, token expiry, killed processes — all of these will happen) resumes with no duplicates.
> --- `references/upload_full_project.md`

Working-context control: batching metadata is a requested partition of work, but input isolation and return filtering are unspecified. Background supervision is explicitly delegated to the host, not a shipped process manager. This route transfers formalized mathematics under unchanged conversion rules; no content-directed revision of those rules is established. Learning, reflection, autonomous method-building and exercised self-improvement are uninspected rather than inferred from writing scripts. The original type oracle checks external product preservation, not improvement of the agent's own organization.

#### RT-RTE-workspace-refresh
Label: Service-version-driven instruction refresh

Endpoints and progression: login/token refresh response version → compare with skill metadata → on mismatch pull workspace repository before continuing. Owner: foreground agent following `SKILL.md`; remote service supplies version, Git supplies candidate instruction files. Proposed change: cached procedure/API-contract text. SRC-1, `SKILL.md`, `references/setup.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: authentication response includes version; a prescribed Git pull changes local checkout files if successful.
- Later read-back: updated skill/reference text is intended to guide continued and later invocations in the reused workspace.
- Delegated visibility: inapplicable — no delegated context is prescribed for the version check.
- Selection predicate: response version differs from `metadata.version`; supplied command pulls tags from `origin main`, rather than selecting a specific immutable version pin.
- Invalidation or expiry: check every login/refresh; rollback and failed-pull recovery are unspecified in this procedure.
- Activation or effect: intended replacement of stale instructions before further work; actual loading, compliance and later behavioral change are unobserved.
- Evidence limits: no executed updater or authority check is shipped, and no evidence shows the repository update corresponds exactly to the reported service version.

Admission roles: external maintainers provide the candidate repository revision; agent compares versions and performs pull; Git merge/failure can prevent installation; no per-update human content approval is required by this text. Answer oracle: service version string, not an expected behavioral outcome. Mode: maintenance during authentication. Trigger/objective: prevent stale endpoint/response-shape use; guidance is the skill's compatibility warning. What persists: repository instruction changes, not model parameters. Rejection and rollback policy beyond Git behavior are uninspected. This supports a claimed instruction-update surface only: neither evidence-shaped determination of a specific content update nor subsequent causally dependent operation is established, so exercised self-improvement is not attributed. SRC-1, `SKILL.md`.

> Make this check every time you log in or refresh the token.
> --- `SKILL.md`

### Claims

#### RT-CLM-verification-boundary
Label: Formal verification guarantee and its boundary

Claimed operation: the skill calls a verdict a mathematical guarantee because the service checks the exact formal target. Owner/enforcement: external verification worker. Guarantee strength: invariant as claimed, not independently inspected. Covered paths: proof/disproof verification in target environment, with tracked reduction assumptions for proofs. Alternate local compilation does not cover the server's rejection rules; semantic source equivalence needs a separate review. SRC-1, `SKILL.md`, `references/prove.md`, `references/mission_captain.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> Every proof you submit is **type-checked against the target's exact formal statement** by a Lean toolchain on the server, so a verdict from Prove2me is a real mathematical guarantee, not a heuristic.
> --- `SKILL.md`

> Faithfulness is the single criterion: each Lean statement must say exactly what the source says, no less and no more. A missing hypothesis makes the theorem false; a missing conclusion makes it a different theorem; a degenerate reading makes it empty. "It compiles and is true in Lean" is not the bar.
> --- `references/mission_captain.md`

The forcing distinctions in [RT-RTE-reduction-proof](#rt-rte-reduction-proof) prevent interpreting `SKETCH_ACCEPTED` as unconditional closure; [RT-RTE-proposal-audit](#rt-rte-proposal-audit) separates formal truth from faithful encoding.

#### RT-CLM-human-gate
Label: Human mission launch, not universal content approval

Claimed operation: only the human can self-audit and submit a mission proposal. Guarantee strength: protocol, owned by human website actions and claimed backend transition permissions. Covered paths: public/private proposal launch; public approval additionally uses moderators. Alternate paths: direct publishing, upload-first, creator release API and post-launch captain edits do not all use that per-item confirmation gate. Credential access is not evidence that the artifact prevents emulating human website actions; the enclosing harness and backend auth implementation are unavailable. SRC-1, `references/mission_captain.md`, `references/contribute.md`, `references/upload_full_project.md`, `references/setup.md`.

- contract conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> You and your human can both edit the proposal, but **only your human can self-audit and submit it** — that is how a proposal leaves your hands and becomes a real mission (see **Handing off to your human** below).
> --- `references/mission_captain.md`

> If the proposal's `visibility` is `"private"`, the same launch performs no moderator step: identical per-item confirmation and compile-and-publish, but the **private** mission goes live immediately, visible only to you (`status` → `Private`).
> --- `references/mission_captain.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-role-guidance
Label: Role instructions to model-directed actions

Consumer: foreground agent and independent auditor. Channel: loaded skill/playbook natural-language text, with supplied code/templates. Force: requested behavioral policy, not host-enforced restriction. Horizon: current task and future sessions reusing the workspace; compatibility refresh can replace the text. Decisions include role selection, scouting, file generation, HTTP actions and auditor context exclusion. Presence is established; activation is unobserved. SRC-1, `SKILL.md`, `references/mission_solver.md`, `references/mission_auditor.md`. Operative object: [RT-OBJ-skill](#rt-obj-skill); update route: [RT-RTE-workspace-refresh](#rt-rte-workspace-refresh).

> Otherwise you don't have to wait for them between iterations.
> --- `SKILL.md`

#### RT-BAP-milestone-guidance
Label: Captain attestation to solver target choice

Consumer: future mission solver. Channel: milestone list, linked formal declarations, edit history and captain reason. Force: instructed source of authoritative targets and rejected paths; no automatic model-compliance mechanism supplied. Horizon: later solver attempts on the mission, bounded by editable links and deletable history. Captain's write and solver's read are different admission/consumption points; delivery alone is not changed behavior. SRC-1, `references/mission_captain.md`, `references/mission_solver.md`. Write route: [RT-RTE-content-publish](#rt-rte-content-publish); consumer route: [RT-RTE-solver-proof](#rt-rte-solver-proof).

> Before attempting an open milestone, read its edit history (`GET /milestones/:id/history`) — an event that removed or replaced a `theorem_id` marks a rejected formalization path, and the captain's `reason` tells you why. Do NOT retry an approach the captain already rejected ([missions.md](missions.md)).
> --- `references/mission_solver.md`

## Annotations

none
