---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Ars Contexta memory: source-derived notes, task-file handoffs, operational directives and distinct plugin/generated session reload paths."
run-id: AAS-2026-10-12-arscontexta-f9e5f2f34166-01
source-identity: "https://github.com/agenticnotetaking/arscontexta"
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
---

# Ars Contexta memory report

## Boundary and evidence

The memory boundary includes the generated vault's content, navigation, operational evidence, instructions and recovery state, plus the shipped procedures that admit and later consume them. The frozen source is SRC-1 at `2acfd5cc4473c4d06c46be63df748e77e00e2746`, as registered in boundary.md. Git HEAD was rechecked against that pin. Direct reads below add source inspection, not new sources or observed runs. Shell hooks are implementation; model-directed skills, templates and generators are doctrine/design. Supplied runtime records are provisional findings and provide quoted support where cited.

Excluded implementations are Claude Code, search/model services and actual user vaults. Their absence prevents conclusions about host enforcement, exact numerical state, real retrieval results, successful installation and behavioral benefit. Static bundled methodology is guidance, not itself accumulated read-back. Generated or subsequently edited project instructions are retained outputs with later consumers. No target execution was performed.

| Entry point / operation | SRC-1 paths and inspection | Coverage and remaining limit |
|---|---|---|
| Setup, initial configuration and compaction recovery | Direct: `skills/setup/SKILL.md` derivation-first section; supplied runtime generation findings | [RT-RTE-setup-generation](runtime.md#rt-rte-setup-generation), [MEM-OBJ-derivation](#mem-obj-derivation). Initial user content and actual generated artifacts are unsupplied; template choice is not observed lineage. |
| Seed, reduce, serial/parallel ralph, pipeline archive | Direct: `skill-sources/reduce/SKILL.md` provenance/observations, `skill-sources/ralph/SKILL.md` create prompt, `skill-sources/pipeline/SKILL.md` archive; supplied runtime scheduling/admission | [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), [RT-RTE-parallel-claims](runtime.md#rt-rte-parallel-claims), [MEM-OBJ-task-files](#mem-obj-task-files), [MEM-OBJ-notes](#mem-obj-notes). `/enrich` and `/archive-batch` callers are known; standalone implementation is unresolved. |
| Reflect / reweave retrieval and revision | Direct: `skill-sources/reflect/SKILL.md` freshness/discovery/evaluation, `skill-sources/reweave/SKILL.md` evaluation/admission/challenge/split | [MEM-RTE-note-maintenance](#mem-rte-note-maintenance), [MEM-OBJ-topic-maps](#mem-obj-topic-maps). Search-provider internals excluded; count equality does not certify fresh content. |
| Learn, alternative external-source admission | Direct: `skill-sources/learn/SKILL.md` configuration through goals update; reduce provenance | [MEM-RTE-research-intake](#mem-rte-research-intake), [MEM-OBJ-inbox](#mem-obj-inbox). External reports are mixed synthesis/search inputs, not authenticated source truth. |
| Plugin session orientation and persistence | Direct: `hooks/hooks.json`, entire `hooks/scripts/session-orient.sh`; supplied runtime guard/commit/validator findings | [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation), [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks), [MEM-OBJ-session-state](#mem-obj-session-state). Config-dependent wiring is not execution. |
| Generated session hooks and manual handoff | Direct: entire `platforms/claude-code/hooks/session-orient.sh.template`, `platforms/claude-code/hooks/session-capture.sh.template`, `generators/features/session-rhythm.md`, `reference/templates/session-log.md` | [MEM-RTE-generated-orientation](#mem-rte-generated-orientation), [MEM-OBJ-session-log](#mem-obj-session-log). Templates are not deployment; automatic transcript/friction claims exceed these hook bodies. |
| Remember explicit/contextual/mining; rethink triage | Direct: `skill-sources/remember/SKILL.md` mode, creation, mining and edge-case sections; `skill-sources/rethink/SKILL.md` drift/triage; supplied runtime proposal findings | [MEM-RTE-friction-retention](#mem-rte-friction-retention), [MEM-OBJ-methodology](#mem-obj-methodology), [MEM-OBJ-observations](#mem-obj-observations), [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution). Mining requires Markdown session content not supplied by inspected JSON hooks. |
| Ask and proactive knowledge-guide | Direct: `skills/ask/SKILL.md` search/context/local-methodology sections, `agents/knowledge-guide.md` | [MEM-RTE-local-guidance](#mem-rte-local-guidance). Ask rereads accumulated local state; knowledge-guide's explicit reads name static bundled references and do not independently establish local-memory reload. |
| Next, tasks and recommendation-history read-back | Direct: `skill-sources/next/SKILL.md` reconciliation/signals/cascade/logging, `skill-sources/tasks/SKILL.md` done/drop | [MEM-RTE-work-selection](#mem-rte-work-selection), [MEM-OBJ-task-stack](#mem-obj-task-stack), [MEM-OBJ-next-log](#mem-obj-next-log); queue annotation below. No actual maintenance reconciliation observed. |
| Health, verify, validate, graph, stats, kernel evaluator | Direct: `skills/health/SKILL.md` report storage, `skill-sources/stats/SKILL.md` history; scoped headings/path searches in `skill-sources/graph/SKILL.md`, `skill-sources/validate/SKILL.md`; supplied runtime verify/kernel findings | [MEM-OBJ-health](#mem-obj-health), [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate). Graph/validate details and complete kernel checks not audited here: exhaustive graph correctness and automatic repair are not concluded. Stats' history writer remains unresolved. |
| Refactor, architect, reseed, upgrade; configuration/instruction consumers | Direct: `skill-sources/refactor/SKILL.md` approval/execution; supplied runtime architect/reseed/upgrade findings | [MEM-RTE-config-refactor](#mem-rte-config-refactor), [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution), [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade). Different approval routes and archival strength remain distinct. |
| Presets, domain templates, shared skill blocks, help/tutorial/add-domain and other builder commands | Boundary inventory and runtime setup; direct research/session templates, searches in shared blocks | Static initialization/generation surfaces, not evidence of later accumulated content by themselves. Full bodies of these alternate generators/commands and opaque tutorial progress initialization are uninspected here; no exhaustive vocabulary migration, whole-system recovery or equivalence of copied/inherited skills is asserted. See [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths). |

## Core ideas

1. **Files substitute for conversational continuity.** Ralph's next invocation reads task-file findings; setup rereads a persisted derivation after compaction. Notes preserve arguments and links for later work. Queue status is access/scheduling metadata, not a substitute for the reasoning body or quality result. [MEM-OBJ-task-files](#mem-obj-task-files), [MEM-OBJ-derivation](#mem-obj-derivation), [RT-OBJ-queue](runtime.md#rt-obj-queue).
2. **Navigation is curated and searched.** Topic-map membership, inline relationships, descriptions and semantic neighbors select content for model interpretation. A search result count bounds candidates, not the full context token budget. External embeddings/reranking are not inspectable memory payloads here. [MEM-RTE-note-maintenance](#mem-rte-note-maintenance).
3. **Operational corrections can become specifications.** Remember converts user corrections or mined session evidence into scoped directives with reasons; ask and rethink request full-body reads. The plugin SessionStart excerpt is narrower and can omit the directive entirely. [MEM-RTE-friction-retention](#mem-rte-friction-retention), [MEM-RTE-local-guidance](#mem-rte-local-guidance), [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation).
4. **Different readers grant different authority.** Notes inform knowledge work; methodology directs behavior and serves as a drift reference; queue fields select phases; recent recommendations discourage repeated suggestions. None of these deliveries establishes reliable obedience or improved capacity. [MEM-BAP-retained-content](#mem-bap-retained-content), [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Domain notes

Source-native identity: domain-vocabulary notes directory, default `notes/`. Natural-language claims, reasoning, sources and relationship explanations are Markdown on the vault filesystem, optionally Git. YAML fields and wiki-link targets provide access metadata but their semantic judgment remains model-mediated. Lineage includes user/manual notes, approved reduce extraction and ralph create/enrichment, followed by reflect/reweave transformations. Initial personal content is unsupplied; do not treat all notes as extracted external facts. Later reflect/reweave workers read full arguments; links and topic membership select other notes. Knowledge authority at that consumer differs from live instruction authority. Distinct result of [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), not part of its queue or generated instruction object. SRC-1: `reference/templates/research-note.md`, `skill-sources/ralph/SKILL.md`.

> - Body: 150-400 words showing reasoning with connective words
> - Footer: Source (wiki link), Relevant Notes (with context), Topics
> --- `skill-sources/ralph/SKILL.md`

#### MEM-OBJ-topic-maps
Label: Topic maps and inline navigation

Source-native identity: domain topic-map Markdown files and notes' inline relationships/Topics footers. Natural-language map descriptions, tensions, gaps and relationship reasons coexist with file-link identifiers on the filesystem. Maps are curated by human/agent choices; reflect writes membership and connections, and later reflect follows Core Ideas links. They are content and selection aids, not a numerical index or a universal ranking oracle. No closest runtime object counterpart: they are distinct outputs of [RT-RTE-source-processing](runtime.md#rt-rte-source-processing). SRC-1: `skill-sources/reflect/SKILL.md`.

> - Read the relevant {vocabulary.topic_map}(s)
> - Follow curated links in Core Ideas — these are human/agent-curated connections
> - Note what is already connected to similar concepts
> - Check Tensions and Gaps for context
> - What do agent notes reveal about navigation?
> --- `skill-sources/reflect/SKILL.md`

#### MEM-OBJ-task-files
Label: Persistent per-claim task findings

Source-native identity: `ops/queue/{source}-NNN.md` claim tasks and enrichment tasks, later batch archive copies. Natural-language reduce findings, intended additions and phase findings reside in Markdown; symbolic task IDs, source-line pointers and classifications are metadata. Files preserve reasoning/context separately from [RT-OBJ-queue](runtime.md#rt-obj-queue); they are not a part of the queue mapping. Later workers are instructed to read the task file, including extraction rationale; phase results augment it. The handoff return is a report to the lead, not the only retained payload. SRC-1: `skill-sources/reduce/SKILL.md`, `skill-sources/reflect/SKILL.md`, `skill-sources/pipeline/SKILL.md`.

> **If a task file exists** (pipeline execution): read the task file to see what the extraction phase discovered. The reduce notes, semantic neighbor field, and classification provide critical context about why this {vocabulary.note} was extracted and what it relates to.
> --- `skill-sources/reflect/SKILL.md`

Batch archival moves task files and writes source/count/title/learning summaries, then removes completed entries or marks them archived. It retains detailed files rather than necessarily replacing them with a summary. No inspected consumer of the batch summary itself establishes independent summary read-back. SRC-1: `skill-sources/pipeline/SKILL.md`.

#### MEM-OBJ-derivation
Label: Derivation rationale and configuration

Source-native identity: `ops/derivation.md`, associated `ops/derivation-manifest.md` and `ops/config.yaml`. Natural-language rationale and quoted conversational signals are distinct from vocabulary/feature/dimension fields; those fields are interpreted by generation skills and, for hook configuration, shell logic. Substrate: project files, optionally Git. Setup derives and persists these from conversation and bundled design guidance; later generation rereads rationale rather than relying on compacted conversation. Ask reads it for user-specific answers; approved refactor/reseed can change it. It is a distinct input/output of [RT-RTE-setup-generation](runtime.md#rt-rte-setup-generation), not the generated instructional container [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md). SRC-1: `skills/setup/SKILL.md`, `skills/ask/SKILL.md`, `skill-sources/refactor/SKILL.md`.

> 2. **Stateless generation.** Every subsequent step re-reads `ops/derivation.md` as its source of truth. No generation step relies on conversation memory for configuration decisions.
> --- `skills/setup/SKILL.md`

This is a specified checkpoint of interpreted design reasons, not a complete raw transcript or an implementation of the host's compactor.

#### MEM-OBJ-methodology
Label: Accumulated operational directives

Source-native identity: `ops/methodology/*.md` and its `ops/methodology.md` MOC. Markdown natural-language What to Do/Avoid, Why This Matters and Scope sections; metadata includes category, source, creation time and active/superseded status. Vault files/Git store them. Remember converts explicit user guidance, confirmed contextual corrections or mixed session evidence into directives; rethink can create/extend them after triage. Reasons persist in the body and ask/rethink request full-body consumption; plugin orientation prints only headers and generated orientation prints titles. Distinct from the setup-generated instruction container [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md), while supplementing [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions). SRC-1: `skill-sources/remember/SKILL.md`, `skills/ask/SKILL.md`, `skill-sources/rethink/SKILL.md`.

> **Rule Zero:** This methodology note becomes part of the system's canonical specification. ops/methodology/ is not a log of what happened — it is the authoritative declaration of how the system should behave. Write this note as a directive: what the agent SHOULD do, not what went wrong. Future sessions, /rethink drift checks, and meta-skills will consult this note as ground truth for system behavior.
> --- `skill-sources/remember/SKILL.md`

A superseded marker is stored withdrawal metadata. Full-body readers do not specify a universal active-only admission filter; marker presence alone cannot prove the old directive stops influencing them.

#### MEM-OBJ-observations
Label: Operational observations and tensions

Source-native identity: `ops/observations/` and `ops/tensions/`. Natural-language incident descriptions, contradictory claims and drift findings, plus symbolic status and resolution pointers in Markdown frontmatter; substrate is vault filesystem/Git. Reduce logs these during work; remember mining derives observations from session material; rethink creates drift observations from configuration/spec comparisons. Later rethink reads pending/open items, separating unresolved evidence from promoted knowledge or behavioral specifications. These are inputs to [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution), not its revised instruction result. SRC-1: `skill-sources/reduce/SKILL.md`, `skill-sources/rethink/SKILL.md`.

> Read each pending item fully. These are small atomic notes — load all of them. Understanding the full content is required for accurate triage. If zero pending items, report clean state and exit early.
> --- `skill-sources/rethink/SKILL.md`

Triage stores promoted/implemented/archive or dissolved dispositions and target/reason pointers. Pending/open selection can exclude resolved items; plugin hook counts instead count all matching filenames. Archiving is not necessarily physical deletion.

#### MEM-OBJ-inbox
Label: Incoming and archived source material

Source-native identity: domain inbox files, default `inbox/`, and seed's batch source archive. Natural-language source documents include external texts, user captures and learn's synthesized research reports, with provenance/URLs as access metadata. Filesystem/Git stores them. Initial source trust is not established merely by insertion; learn's provider synthesis differs from a raw source. Later reduce interprets them, while created notes link back for provenance. Distinct input retained by [RT-RTE-source-processing](runtime.md#rt-rte-source-processing). SRC-1: `skill-sources/learn/SKILL.md`, `skill-sources/reduce/SKILL.md`.

> - Each created {vocabulary.note}'s Source footer links to the source file
> - The source file's YAML contains the research prompt
> - The chain: research query -> inbox file -> /{vocabulary.reduce} -> {vocabulary.notes}
> --- `skill-sources/reduce/SKILL.md`

Learn's concrete template uses `exa_prompt`/`exa_tool`; reduce lists `research_prompt`/`research_server`. The conceptual provenance path is specified, but exact-field interoperable preservation is unresolved.

#### MEM-OBJ-session-state
Label: Session lifecycle JSON

Source-native identity: `ops/sessions/current.json` and timestamped `.json` archives. Symbolic ID/time/status records on disk/Git, produced by plugin SessionStart or generated Stop template. These are lifecycle metadata, not opaque transcript payloads with human-readable summaries. Plugin orientation prints current.json after its possible replacement; generated orientation prints it without tracking writes. Existing runtime routes already cover these effects: [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation). This object isolates the retained payload rather than redeclaring that route. SRC-1: `hooks/scripts/session-orient.sh`, `platforms/claude-code/hooks/session-capture.sh.template`.

>   "id": "${CLAUDE_CONVERSATION_ID}",
>   "ended": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
>   "status": "completed"
> --- `platforms/claude-code/hooks/session-capture.sh.template`

No subject matter, corrections or unfinished-work body occurs in that payload.

#### MEM-OBJ-session-log
Label: Session summaries and working handoffs

Source-native identity: session-log Markdown template, handoffs in `ops/reminders.md` or relevant task files, and goals in `self/goals.md` or `ops/`. Natural-language accomplishments, unfinished work and next priority are files written under session-rhythm instructions. These are derived working summaries, not the lifecycle JSON [MEM-OBJ-session-state](#mem-obj-session-state). Initial goals/identity may be user-elicited or preset-derived; no actual initialization artifact was supplied. Later session-rhythm orientation requests identity/goals/reminders and clear handoffs; hooks directly supply goals and identity under their distinct existence gates. Overlap with [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation) is consumption, not duplicate object identity. SRC-1: `generators/features/session-rhythm.md`, `reference/templates/session-log.md`, `hooks/scripts/session-orient.sh`.

> 4. **Leave a handoff** — If work continues in the next session, leave a clear note about where you stopped and what's next. This can be in ops/reminders.md or a comment in the relevant task file.
> --- `generators/features/session-rhythm.md`

No inspected automatic writer makes every session a substantive Markdown summary. These manual/model checkpoint alternatives remain supported despite the transcript-hook gap.

#### MEM-OBJ-task-stack
Label: User task stack

Source-native identity: `ops/tasks.md` Current, Completed and Discoveries sections; natural-language task descriptions with symbolic checkboxes/order/date metadata, filesystem/Git storage. Tasks is instructed to edit this file in response to user add/done/drop/reorder requests; next reads Current as user priorities overriding automatic signals. It is distinct from [RT-OBJ-queue](runtime.md#rt-obj-queue), whose tasks drive processing phases. SRC-1: `skill-sources/tasks/SKILL.md`, `skill-sources/next/SKILL.md`.

> Remove the item entirely. Do NOT move to Completed.
> --- `skill-sources/tasks/SKILL.md`

Done instead moves content to dated Completed. Drop withdraws it from the live recommendation input without retaining a completion claim.

#### MEM-OBJ-next-log
Label: Recommendation history

Source-native identity: `ops/next-log.md`; natural-language state summaries, recommendation and rationale with priority metadata on filesystem/Git. Next appends it and later rereads the last three entries; repetition in the last two changes recommendation selection unless a stronger signal warrants repetition. Distinct from queue and task stack in [RT-OBJ-queue](runtime.md#rt-obj-queue). SRC-1: `skill-sources/next/SKILL.md`.

> - If the same recommendation appeared in the last 2 entries, select the next-best action instead
> - This prevents the system from getting stuck recommending the same thing repeatedly when the user has chosen not to act on it
> --- `skill-sources/next/SKILL.md`

The instruction supports trace-responsive next-round selection, not demonstrated preference inference or benefit.

#### MEM-OBJ-health
Label: Retained health reports

Source-native identity: `ops/health/YYYY-MM-DD-report.md`, with same-day counter suffixes. Natural-language diagnostic findings/fixes and symbolic counts/severities on filesystem/Git. Health's model/tool diagnostic procedure writes reports; next reads the latest report and architect consults health history. This is retained evaluation evidence distinct from the live queue or admission gate. Closest supplied record: input to [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution). SRC-1: `skills/health/SKILL.md`, `skill-sources/next/SKILL.md`.

> Write every health report to `ops/health/YYYY-MM-DD-report.md`. If multiple reports are run on the same day, append a counter: `YYYY-MM-DD-report-2.md`.
> --- `skills/health/SKILL.md`

Stats conditionally reads `ops/stats-history.yaml` or similar and explicitly does not create it. Its assertion that health owns that writer is not independently traced here; health Markdown history does not establish a YAML snapshot writer. SRC-1: `skill-sources/stats/SKILL.md`.

### Routes

#### MEM-RTE-note-maintenance
Label: Retained-note discovery and revision

Endpoints/progression/owner: explicit reflect/reweave target, topic or sparse/stale selection → full target/task read → curated map plus semantic/keyword candidates → model relationship/claim evaluation → notes, map and task-file changes. Model skill execution owns semantic choices; tools perform filesystem effects. This expands maintenance within [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), but also covers independent interactive invocations, so it is not a part of exactly that route. SRC-1: `skill-sources/reflect/SKILL.md`, `skill-sources/reweave/SKILL.md`.

- Immediate return: discovery trace, added relationships, map updates, claim changes, cascade and synthesis recommendations; handoff additionally reports phase findings.
- Later read-back: changed notes/maps are selected and read in later reflect/reweave invocations; task findings inform later pipeline workers.
- Delegated visibility: phase workers are instructed to read designated task/target files; exact host context inheritance is uninspected.
- Selection predicate: target claim concepts, Topics maps/Core Ideas, semantic query with limit 15, keywords, descriptions and one neighborhood's existing links; reweave also uses newer knowledge/backlinks.
- Invalidation or expiry: note revisions, renames/splits and map edits change live content/navigation; no automatic note TTL specified in inspected sections.
- Activation or effect: instructions request link/argument edits; later comprehension or changed model behavior is unobserved.
- Evidence limits: design procedure, no vault execution; qmd indexing/ranking outside source; file-count comparison misses same-count edits.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: reflect's model rejects unarticulated/no-utility connections and flags synthesis for future work rather than creating it. Reweave applies directly in handoff mode but waits for approval interactively; merge/delete recommendations require human judgment even in the enrichment path. Authors and physical writers are model/tools, distinct from this admission policy. Guidance: claim relevance, articulated relation, coherence and network utility. Oracle: no independently correct claim/link set; model critique plus link existence checks. Operating modes: open interactive maintenance and pipeline handoff. Recovery: preserve valid text, update links/description on rename; instructed atomic changes are not an inspected transaction implementation. SRC-1: `skill-sources/reflect/SKILL.md`, `skill-sources/reweave/SKILL.md`.

> **For pipeline execution (--handoff mode):** Apply changes directly. The pipeline needs to proceed without waiting for approval.
>
> **For interactive execution (no --handoff):** Present the reweave proposal first, then apply after approval.
> --- `skill-sources/reweave/SKILL.md`

Theory account, limited to reweave's formulated domain claims: guidance asks whether the old claim holds under newer evidence, supports nuanced revision/challenge and keeps original claim, new evidence and revised position in the task file. Later reflect explicitly reads task rationale; a universal later reread of every challenge record is not established.

> **Always log challenges:** When a claim is challenged or revised, this is a significant event. Note it in the task file Reweave section with the original claim, the new evidence, and the revised position.
> --- `skill-sources/reweave/SKILL.md`

Theory-builder conditions 1–4:
- condition 1 conclusion status: claimed
  Title/body locates the whole claim.
- condition 2 conclusion status: claimed
  Evaluation and proposed edits are requested to depend on its argument, not only a score.
- condition 3 conclusion status: claimed
  Challenge patterns locate old claim, contradictory evidence and successor position; actual blame placement remains unobserved.
- condition 4 conclusion status: claimed
  Revised note/task findings persist and later workers read them; realized iteration is unobserved.
Addressability: file/claim and argument-section granularity, not provider reasoning internals. Persistence: specified across worker invocations and sessions. Learning: uninspected — changed capacity/benefit not measured. Reflection: inapplicable — this assessment concerns domain knowledge, not the system's method self-representation. Reflective theory builder: inapplicable — method criticism belongs to the architecture route. Autonomous theory builder: not established; interactive revisions have internal human admission, and no computational performance of every internal operation is supplied. These limits do not negate the specified content-criticism path.

#### MEM-RTE-friction-retention
Label: Corrections and session evidence to directives

Endpoints/progression/owner: explicit user friction, inferred recent correction or requested session mining → model parses behavior/scope/category → compares existing directives/observations → creates/extends directive or pending observation → updates MOC and mined marker → later ask/rethink/full-body or orientation excerpt consumers. Closest supplied route [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution) performs later proposal/admission, not this low-ceremony capture. SRC-1: `skill-sources/remember/SKILL.md`.

- Immediate return: filed/extended note names, observation counts, mined sessions and category-threshold rethink suggestion.
- Later read-back: operational directive bodies/reasons reach ask and rethink; recent excerpts/titles reach session orientation; observations reach approved triage.
- Delegated visibility: uninspected — no executed mining delegation or host inheritance is supplied.
- Selection predicate: explicit description; most recent correction with contextual confirmation; session mining selects `ops/sessions/*.md` lacking `mined: true`, reads full content, and looks for corrections, repeated redirections, failures, confusion and implicit choices.
- Invalidation or expiry: superseded directives gain `superseded_by`; mined marker suppresses repeat mining; duplicate guidance is extended instead of duplicated. No global active-only read filter or expiration proved.
- Activation or effect: specified raw/mixed experience-to-directive transformation and subsequent consumption, not observed behavior improvement.
- Evidence limits: design prompts, no transcripts/results; inspected capture hooks create JSON lifecycle records rather than required Markdown evidence.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission and trust differ by mode. Explicit mode uses user-supplied content without a second confirmation gate; contextual mode requires yes/no/modify confirmation and treats implicit signals as lower confidence. Mining requests model classification/deduplication and creation without stating that contextual confirmation gate; do not generalize the latter to every write. Starting mining is not per-finding human approval. Original evidence mixes user corrections, agent actions/tool failures and inferred preferences; `source: session-mining` identifies a transformation, not uniform human authorship. Guidance is concrete DO/DON'T plus scope/reason, not merely raw event retention. No answer oracle is supplied. Mode is open operational capture, not a controlled experiment. Recovery retains contradictory evidence and supersession pointers; no automatic rollback is established. SRC-1: `skill-sources/remember/SKILL.md`.

> **For methodology findings:** Follow the same creation process as explicit mode (Step 3 in Explicit Mode section), with `source: session-mining` and add `session_source: [session filename]`.
> --- `skill-sources/remember/SKILL.md`

> 2. Update the existing methodology note's status to `superseded` and add `superseded_by: [new note]`
> 3. Create the new methodology note with the updated guidance
> --- `skill-sources/remember/SKILL.md`

The trace-fed update path is specified as raw conversation/session → derived observation or directive with Why This Matters/Scope → later guidance or drift reference. Reasons survive full-body reads but not title/header-only push. This is not evidence that user-correction rates fall. Method theory criticism/admission properties are already assessed in [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution); this route captures local guidance and preserves evidence for that separate consumer.

#### MEM-RTE-local-guidance
Label: Ask reads local operational knowledge

Endpoints/progression/owner: user methodology question → ask model routes bundled research/reference retrieval → reads user derivation/constraints and local methodology → synthesizes cited answer. Static bundled research search and accumulated local state have different lineage. Distinct from generation and from [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions): consumer here is the answering model, not automatic host context loading. SRC-1: `skills/ask/SKILL.md`.

- Immediate return: answer with research/local-methodology citations and flagged tensions.
- Later read-back: previous derivation and ongoing methodology notes are reread for a later user question; their reasons influence requested answer synthesis.
- Delegated visibility: uninspected — no delegated ask run supplied.
- Selection predicate: question classification and claim-map guide bundled search; top 3–7 full results and one-hop links; 2–4 reference documents; local method loop loads all matching files, then relevance determines answer use.
- Invalidation or expiry: file edits/supersession change live source; no explicit active-only local-methodology filter in the read loop.
- Activation or effect: prompt prioritizes local methodology for how-my-system-works questions and research for general justification; performed reliance is unobserved.
- Evidence limits: source design, no answer trace or search implementation; local notes are normative/self-reported knowledge, not verified configuration truth.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> - Methodology notes about system behavior are more authoritative for "how does MY system work" questions than the general research graph
> --- `skills/ask/SKILL.md`

This is a consumer-relative preference. The same procedure can flag contradiction with research, rather than declaring local guidance universally correct. A 3–7 document budget is not a token cap, and the all-local-notes loop has no inspected token ceiling.

#### MEM-RTE-research-intake
Label: External research becomes retained source

Endpoints/progression/owner: user research topic/depth and config → model invokes configured external search/research cascade → writes synthesized findings, URLs and provenance to domain inbox → optional processing handoff and goals append. Distinct alternative acquisition preceding [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), not its seed route. SRC-1: `skill-sources/learn/SKILL.md`, `skill-sources/reduce/SKILL.md`.

- Immediate return: research/tool/source-count report, filed path and processing suggestion or automatic-queue announcement.
- Later read-back: later reduce reads the inbox report; note Source footer retains backlink; meaningful new directions added to existing self/goals reach session orientation.
- Delegated visibility: uninspected — provider result and full query are requested to persist, but actual API payloads/runs absent.
- Selection predicate: explicit depth overrides config/default; configured tool cascade with depth-specific source counts; meaningful directions matched to existing goals format.
- Invalidation or expiry: duplicate/enrichment judgment in reduce may skip or update existing knowledge; later file edits replace live research; no inspected inbox TTL.
- Activation or effect: requested report/goals writes and subsequent extraction; automatic-mode wording alone does not prove a dispatched queue task.
- Evidence limits: external providers excluded; synthesized propositions and URL lists do not establish authenticated factual support.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: user sets topic/depth; model chooses/tools synthesize and files findings without a per-finding approval step in learn. Subsequent reduce retains its separate user-approval instruction. Guidance is configured research depth, practical findings and extractable propositions. No expected-answer oracle; open research mode. All-tier tool failure reports failure and invites retry/manual input; no fabricated fallback content is specified. Provenance keeps query/tool/result identity but field names differ from reduce's generic list.

> [Synthesized findings organized by theme, not by source. Each finding
> should be a clear proposition the reduce phase can extract as an atomic insight.]
> --- `skill-sources/learn/SKILL.md`

#### MEM-RTE-generated-orientation
Label: Generated hook retained-state push

Endpoints/progression/owner: a generated deployment's SessionStart → template shell reads existing goals, methodology titles, current JSON and self identity/methodology → stdout context and maintenance/queue counts. Owner is generated shell under host event delivery. Distinct from registered plugin [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation): template does not perform plugin session-tracking writes, extracts titles rather than first-three-line excerpts, and reads self/methodology independently of identity existence. SRC-1: `platforms/claude-code/hooks/session-orient.sh.template`.

- Immediate return: formatted orientation text, conditions, tutorial-resume notice and queue counts.
- Later read-back: previously edited goals/self files, previous current.json and recent methodology titles reach a later session.
- Delegated visibility: uninspected — host worker inheritance is outside the source.
- Selection predicate: file existence; prefer self/goals over ops/goals; five newest methodology files by mtime, first `# ` heading per file; full self files; current JSON; depth-three tree and count thresholds.
- Invalidation or expiry: edits/current-state replacement and mtime reorder change delivered material; no active/superseded filter in title selector.
- Activation or effect: executable template specifies unsolicited context supply; deployment, actual host delivery and behavior change unobserved.
- Evidence limits: template only, generation varies enabled features; selected title omits body/reasons; no hard context token budget for full goals/self files.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

>     TITLE=$(grep '^# ' "$f" 2>/dev/null | head -1 | sed 's/^# //')
> --- `platforms/claude-code/hooks/session-orient.sh.template`

This contrasts with the plugin's header excerpt, not evidence of a full directive read. Session-rhythm instructions additionally afford requested/manual reminder/handoff reads and advise ~20% orientation/~60% work/~20% persistence; those ratios are guidance, not enforced allocation. SRC-1: `generators/features/session-rhythm.md`.

#### MEM-RTE-work-selection
Label: Task priorities and recommendation read-back

Endpoints/progression/owner: user tasks operation changes task stack; later next invocation reconciles maintenance conditions/queue → reads stack/goals/reports/signals/recent log → recommends one concrete action → appends state/action/rationale. Model lead owns prioritization and instructed reconciliation; suggested action is not itself guaranteed execution. Distinct from ralph phase selection in [RT-RTE-source-processing](runtime.md#rt-rte-source-processing); overlaps [RT-OBJ-queue](runtime.md#rt-obj-queue) as an alternate producer/reader. SRC-1: `skill-sources/tasks/SKILL.md`, `skill-sources/next/SKILL.md`.

- Immediate return: tasks edit/status report or next action with rationale and consequence of deferral.
- Later read-back: user-set stack affects next invocation; last three next-log entries affect repeat avoidance; health history and goals influence priorities; condition tasks persist for later selection.
- Delegated visibility: uninspected — no executed delegated recommender supplied.
- Selection predicate: Current stack first, then session-priority maintenance/signals, multi-session signals and slow signals; repeated last-two recommendation replaced unless signal strengthens.
- Invalidation or expiry: done moves stack item to Completed, drop removes it; condition satisfaction auto-closes maintenance task; updated target and next-log additions change next round.
- Activation or effect: prompt requests trace-responsive recommendation and automatic condition-task writes, not proof user follows it or improvement results.
- Evidence limits: design and shell examples, not execution; session counts differ across JSON hook and Markdown mining paths.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: user directly orders stack changes; next's model/condition procedure can add/update/close maintenance entries without a separate human confirmation gate. The human may ignore recommendations. Guidance: consequence speed, goals, explicit user priorities and anti-repetition rules. Oracle: condition counts/link checks rather than a reference optimal next action; open advisory mode. Range-invalid task requests error; queue migration is instructed for old schema, not validated transaction recovery. Retained rationale in next-log supports later deduplication and rethink evidence. SRC-1: `skill-sources/next/SKILL.md`.

> - This prevents the system from getting stuck recommending the same thing repeatedly when the user has chosen not to act on it
> --- `skill-sources/next/SKILL.md`

#### MEM-RTE-config-refactor
Label: Approved configuration-driven regeneration

Endpoints/progression/owner: dimension/config changes → model computes artifact/content impact and plan → human yes/no/adjust → model regenerates affected skills, context sections, templates/hooks and derivation/configuration, then migrates content and validates. This is a distinct config-to-artifact route alongside [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution) and [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade), not a new identity for either. SRC-1: `skill-sources/refactor/SKILL.md`.

- Immediate return: plan/dry-run, approval dialog, then changed-artifact and validation report.
- Later read-back: new live skills/context govern later invocations; rationale/date/recommendation references in derivation inform later ask/refactor; moved notes/maps alter later navigation.
- Delegated visibility: uninspected — no executed refactor/worker consumption supplied.
- Selection predicate: changed dimensions map to affected skills/context/schema/hooks; human adjusts/approves; vocabulary and new processing depth constrain generation.
- Invalidation or expiry: approved text replaces live sections/skills; migrations alter schema/files/links; old unchanged sections preserved by instruction.
- Activation or effect: requested revision of behavior-determining files and content organization; no deployment or changed downstream behavior observed.
- Evidence limits: prompt procedure; heading Archive Current State leads to a changelog example, not independently established full artifact backup.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: model diagnoses/drafts; user can refuse or adjust before writes; dry-run stops without approval. Guidance: dimensional impact, latest generation references and vocabulary, not an independent semantic oracle. Operating mode: open approved regeneration. Recovery: record planned state/change references, use Git moves and validate; complete automatic rollback or atomic migration not established. Persisted reasons include new dimension rationale and architect reference, later read by derivation consumers. SRC-1: `skill-sources/refactor/SKILL.md`.

> 1. Update `ops/derivation.md` with:
>    - New dimension positions
>    - Rationale for each change
>    - Date of change
>    - Reference to /architect recommendation (if applicable)
> --- `skill-sources/refactor/SKILL.md`

### Claims

#### MEM-CLM-transcript-gap
Label: Transcript capture versus lifecycle records

Claimed operation: session rhythm says Stop hooks automatically retain transcripts and detect friction/create mining tasks. The inspected plugin registration has SessionStart and Write callbacks only; generated Stop template emits ID/end/status JSON and commits directories. Remember mining instead selects Markdown sessions lacking mined markers. These inspected parts do not implement the advertised automatic transcript-to-mining chain. This adds the format/consumer mismatch to, rather than duplicates, [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation)'s lifecycle account. SRC-1: `generators/features/session-rhythm.md`, `hooks/hooks.json`, `platforms/claude-code/hooks/session-capture.sh.template`, `skill-sources/remember/SKILL.md`.

> 5. **Session capture** — Stop hooks automatically save the session transcript to ops/sessions/. The system runs lightweight friction detection on the transcript and creates mining tasks for any detected friction or insights. This ensures no work is lost, even when you forget to explicitly capture something during the session.
> --- `generators/features/session-rhythm.md`

> UNMINED=$(grep -rL '^mined: true' ops/sessions/*.md 2>/dev/null)
> --- `skill-sources/remember/SKILL.md`

Bounded conclusion: automatic substantive session mining is not established by these inspected hooks. This is not a repository-wide absence of every possible transcript producer; model-written session logs/handoffs remain an alternative and actual host transcripts are excluded.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-content
Label: Retained knowledge and operational evidence authority

Consumer/channel/force/horizon: later reflect/reweave models read selected notes/maps/task files as knowledge and revision context; next reads goals/task stack/log/reports as priorities and anti-repetition evidence; ask reads full local methodology as system-specific guidance; rethink reads directives as drift reference and pending observations as criticism evidence. Force is natural-language model interpretation, with symbolic statuses/targets used by prompted selection and limited shell consumers, not unconditional enforcement. Horizon is later phase invocations and sessions while files remain live and selected. Source trust depends on admission/lineage, not YAML presence. Distinct from [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions)'s host-loaded instruction channel, though local methodology can also enter that channel through orientation. SRC-1: `skill-sources/reflect/SKILL.md`, `skill-sources/next/SKILL.md`, `skills/ask/SKILL.md`, `skill-sources/rethink/SKILL.md`; minimum supporting passages are in their route/object records above.

## Annotations

#### On [RT-OBJ-queue](runtime.md#rt-obj-queue)

The queue is persisted scheduling/access state, distinct from natural-language task bodies and verification reports. Later serial/parallel ralph reads filtered pending entries/current phase; next adds condition-triggered maintenance tasks, updates targets and closes satisfied conditions. These producers have different admission: source processing carries reduce's approval conflict, while next's condition reconciliation specifies no per-task dialog. Selection is model-driven reading plus tool examples, not a compiled authoritative state machine. Done status can cease later eligibility without proving verification passed. SRC-1: `skill-sources/next/SKILL.md`; [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate) supplies the conflicting verification passages.

#### On [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md)

Generated context/skill bodies carry operational guidance derived from bundled methodology, conversational configuration and later approved revisions. Their natural-language rationale differs from symbolic host-facing metadata. Later context loading and skill invocation grant instructional force only through host/model interpretation. Copied versus inherited delivery remains unresolved; no automatic update reach is inferred. SRC-1: `skills/setup/SKILL.md`, `skill-sources/refactor/SKILL.md`; [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths), [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade).

#### On [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation)

Memory-specific selector: plugin SessionStart pushes full existing goals; identity and self/methodology bodies are read only under identity-file existence; five newest methodology files contribute first three lines, not titles or directive bodies. The remember template starts with delimiter, description and type, so this can expose metadata without the DO/DON'T or Why This Matters. Modification time is an access signal, not semantic relevance. There is no hard token ceiling for full goals/self files. Current-session JSON may replace previous state before display; lifecycle archives do not reconstruct substantive unfinished work. Implementation is wired as runtime states, operation uninspected. SRC-1: `hooks/scripts/session-orient.sh`, `skill-sources/remember/SKILL.md`.

> for f in $(ls -t ops/methodology/*.md 2>/dev/null | head -5); do
>   head -3 "$f"
> done
> --- `hooks/scripts/session-orient.sh`

#### On [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution)

Rethink full-body methodology reads retain both directive and reason; configuration/context comparisons produce explicit drift observations. Pending/open evidence admission is filtered before triage. Confirmed triage can promote into domain notes, implement concrete guidance, create/extend methodology, archive or keep pending; it records target and reason/status links for later reliance. Approved proposals add resolved_by pointers; rejected proposals are retained as deferred and cannot be resurfaced without new evidence under the supplied runtime account. Thus archived/dissolved/pending status has a later selector, unlike a claim that every stored superseded directive is automatically suppressed. SRC-1: `skill-sources/rethink/SKILL.md`; runtime supplies proposal/rejection passages.

## Write side

Acquisition has at least three authorities: user/manual captures, learn's model/provider-synthesized reports, and source processing with reduce's separate approval instruction. Seed's relocation/duplicate handling and reduce's approval conflict with dontAsk remain as [RT-RTE-source-processing](runtime.md#rt-rte-source-processing). Learn is not raw-source authentication; query/tool/source URLs preserve lineage, but reduce's field vocabulary mismatch prevents asserting exact metadata interoperability. [MEM-RTE-research-intake](#mem-rte-research-intake).

Transformations are substantive, not only archival: reduce creates/enriches claims, reflect admits articulated links and map membership, reweave challenges arguments and splits notes. Reweave retains original/new evidence/revised position, with task-file consumers; synthesis opportunities are flagged rather than silently promoted, and merge/delete remains human judgment. Archive replacement and rename must update navigation by instruction, but automatic rollback/withdrawal is not guaranteed. [MEM-RTE-note-maintenance](#mem-rte-note-maintenance).

Trace retention and trace-fed guidance are separate. JSON session IDs/times cannot ground substantive corrections. Explicit/contextual conversation and externally written Markdown session logs can ground remember's model conversion to directive/observation; full reasons and scope persist and are later read by ask/rethink. Mining writes a processed marker; duplicate evidence extends an existing directive; conflicting guidance retains contradiction plus successor/supersession markers. Their raw-to-derived-to-consumer chain is specified, not observed. [MEM-RTE-friction-retention](#mem-rte-friction-retention), [MEM-CLM-transcript-gap](#mem-clm-transcript-gap).

Automatic post-Write validation does not admit or reject content before persistence. Broad async Git staging can include alternate-path writes; warnings, commits and quality gates are different effects. Verify failure should keep a task at verify, but done metadata alone cannot certify that result. Health report retention gives later evidence, not retroactive rejection. [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks), [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate), [MEM-OBJ-health](#mem-obj-health).

Recovery has several retained checkpoint forms: derivation reasons for setup compaction; task phase findings for ralph resumption; goals/reminders/session summaries for manual cross-session continuity; lifecycle JSON for identity/status only; archived skill versions for manual rollback. Refactor's changelog-first step is not equivalent to upgrade's full copied-skill archive. Next/tasks can withdraw work from live selectors without deleting every historical artifact. Architecture revisions have human approval and retain rationale/resolution pointers, but this gate is not universal over remember, hooks or condition-task writes. [MEM-OBJ-derivation](#mem-obj-derivation), [MEM-OBJ-task-files](#mem-obj-task-files), [MEM-OBJ-session-log](#mem-obj-session-log), [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade), [MEM-RTE-config-refactor](#mem-rte-config-refactor).

## Read-back

Requested reads are distinct from automatic push. Ralph workers are told to read the designated task file and note; selection points to retained phase findings, not evidence of host-inherited hidden memory. Reflect/reweave search concepts, topic-map links and neighboring arguments; qmd limits candidate count and grep provides an alternative. The optional numerical index/embedding lineage, exact model revision, mutability and cache persistence remain external and uninspected; readable hits are not the numerical payload. File-count freshness repair requests update/embed when counts differ but cannot detect all equal-count edits. [MEM-RTE-note-maintenance](#mem-rte-note-maintenance), [RT-CMP-session-model](runtime.md#rt-cmp-session-model).

Ask reads question-relevant bundled guidance plus all local methodology and appropriate derivation. Rethink reads directive assertions/reasons and selected pending evidence before proposals. These consumer routes can use complete bodies despite session excerpts. Next gives previously stored user priorities and recent recommendations selection influence; report history also reaches architect and next. [MEM-RTE-local-guidance](#mem-rte-local-guidance), [MEM-RTE-work-selection](#mem-rte-work-selection), [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution).

The plugin and generated orientation push different selected parts. Plugin prints three-line metadata excerpts and gates self/methodology with identity existence; generated template extracts five recent titles and reads self/methodology independently. Neither recent-note path delivers the complete scoped directive/reason. Both can print full goals/self content with no hard token ceiling. Session-rhythm's proportional budget and reminders/handoffs are model-directed alternatives, not host enforcement. [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation), [MEM-RTE-generated-orientation](#mem-rte-generated-orientation).

Static research/template loading alone is not read-back. Likewise archive existence does not establish a later consumer of batch summaries or old skill bodies: upgrade affords manual rollback, and pipeline retains source/task history, but actual rereads are unobserved. Delivery and authority affordances do not establish activation or benefit.

## Integration issues

- **No correction to supplied runtime facts is required.** Its distinction between plugin/generated capture, current-state overwrite, non-blocking warnings and completion conflict survives source checks. Generated orientation is an additional distinct route, not a contradiction of the plugin route. [MEM-RTE-generated-orientation](#mem-rte-generated-orientation), [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation).
- **Transcript/mining integration remains unresolved.** Doctrine promises automatic transcript/friction capture, inspected hooks write JSON metadata, and remember/next concrete mining checks use Markdown with mined markers. Missing fact: which included producer supplies substantive Markdown transcripts and creates mining tasks. Consequence: no claim of a closed automatic trace-fed loop. Manual summaries/directives remain viable independent paths. [MEM-CLM-transcript-gap](#mem-clm-transcript-gap), [MEM-RTE-friction-retention](#mem-rte-friction-retention), [MEM-OBJ-session-log](#mem-obj-session-log).
- **Withdrawal is consumer-specific.** Remember marks old directives superseded, but ask's all-files loop, rethink's full methodology read and orientation recency selectors do not specify a common active-only filter. Missing fact: whether status is reliably interpreted before reliance. Pending/open observation selection is clearer, while plugin filename counts can continue signaling archived items. [MEM-OBJ-methodology](#mem-obj-methodology), [MEM-OBJ-observations](#mem-obj-observations), [MEM-RTE-local-guidance](#mem-rte-local-guidance).
- **Exact provenance fields differ.** Learn emits exa_prompt/exa_tool, reduce lists research_prompt/research_server. Backlinks and conceptual provenance are specified, but literal preservation/translation remains uninspected. This prevents asserting a complete machine-compatible provenance chain, not source retention itself. [MEM-OBJ-inbox](#mem-obj-inbox), [MEM-RTE-research-intake](#mem-rte-research-intake).
- **Search freshness and opaque numerical memory remain bounded.** Reflect uses count inequality to request update/embed; equal-count content changes can escape it. Provider/index encoding, model identity/mutability and persisted caches are outside inspected implementation. Consequence: candidate retrieval quality and fully fresh embeddings cannot be concluded. [MEM-RTE-note-maintenance](#mem-rte-note-maintenance).
- **Stats snapshot writer and alternate command bodies remain unresolved.** Stats names a history capability and assigns creation to health, but inspected health report storage establishes Markdown reports, not the YAML history writer. `/enrich` and `/archive-batch` references do not establish standalone implementation; pipeline's direct archive alternative remains known. [MEM-OBJ-health](#mem-obj-health), [MEM-OBJ-task-files](#mem-obj-task-files), [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).
- **Generation/update reach and recovery strength differ.** Copied/inherited skill conflict remains; refactor's changelog does not prove the full archive offered by upgrade. Automatic-mode learn wording alone does not demonstrate queue dispatch. [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths), [MEM-RTE-config-refactor](#mem-rte-config-refactor), [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade), [MEM-RTE-research-intake](#mem-rte-research-intake).
- **Possible record overlaps:** no new record intentionally redeclares a supplied referent. The session-state object isolates payload used by the supplied session route; generated orientation is separate implementation; note maintenance spans pipeline and interactive invocation; config-refactor is distinct from architect/reseed/upgrade. Methodology supplements but is not identical to generated CLAUDE.md/SKILL.md. Existing queue/instruction/session/architecture referents receive annotations. Reconciliation should preserve these distinctions rather than merge solely by common directory or label. Closest records are cited within every declaration.

## Limitations and checks

The source pin and invocation identities were rechecked; evidence remains SRC-1 only, with no host/service execution or user-vault traces. Direct source reads and supplied runtime findings are separated in coverage. Available but uninspected alternate builder bodies, shared generation details, complete diagnostic scripts and opaque initialization/history writers prevent exhaustive operation, recovery and interoperability claims. Missing observed operation prevents exercised learning, reliable compliance or successful improvement conclusions; it does not erase the specified memory and criticism capacities.

Deterministic validation: passed with the invocation's `commonplace-run validate-output` command after repairing conclusion-status field formatting. A content pass checks form, relations and quotation occurrence, not analytical acceptance or behavioral benefit.
