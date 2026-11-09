---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Nimbalyst Wiki memory: attributed page prose, file-coverage recall, editable writing guidance and external maintenance contracts."
run-id: AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01
source-identity: https://github.com/nimbalyst/nimbalyst-wiki
reviewed-boundary: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
---

# Nimbalyst Wiki memory report

## Boundary and evidence

The memory boundary is the released plugin's instructions and file/integration contracts, not the implementations of the CLI, local library, transcript reader, browser, desktop or hosted team server. All findings use SRC-1 at the revision above. The [boundary](boundary.md) fixes a complete artifact, partial loop. The supplied runtime orders the account but does not establish actual tool behavior. No run evidence or causal experiment was supplied. Pages are intended to persist across coding sessions; a conversation window is not the store.

Direct reads covered `FORMAT.md`, all seven skill entry points, `skills/setup/references/wiki-guide.md`, `skills/update/references/migrating-v1.md`, root MCP declarations, `hooks/hooks.json`, and `CONTRIBUTING.md`. Additional bounded reads covered `README.md`'s CLI/file sections, `skills/update/references/components.md`'s decision/buttons/views/transclusion sections, and `skills/update/references/editor-pages.md`'s creation/embedding contract. HEAD was rechecked as 97c1ba1594d6e3d466a23d33c1bda084026b01b8 and tracked paths inventoried. These reads supply doctrine/design, except manifest declarations, which supply integration implementation. README behavior remains reported operation. Setup's strategic template, relation examples and detailed visual grammars remain available but uninspected; no claim of syntax correctness or complete visual payload interpretation is made.

| Entry point or memory operation | Source paths; inspection basis | Records or conclusion limit |
| --- | --- | --- |
| Capture from session; no-content rejection; attribution | `skills/capture/SKILL.md`, `skills/update/SKILL.md`; direct | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), annotations below; raw transcript retention/selection implementation outside source |
| Recall, marks, changed-file targeting | `skills/recall/SKILL.md`, `skills/update/SKILL.md`, `FORMAT.md`; direct | [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall), [MEM-OBJ-page-metadata](#mem-obj-page-metadata) |
| SessionStart context and Stop reminder | `.mcp.json`, `.codex-mcp.json`, `hooks/hooks.json`; direct; README host distinctions supplied by runtime | [RT-RTE-host-entry](runtime.md#rt-rte-host-entry); actual hook payload, budget and predicate unavailable |
| Setup, guide, optional repository instructions | `skills/setup/SKILL.md`, `skills/setup/references/wiki-guide.md`; direct | [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [MEM-OBJ-writing-guide](#mem-obj-writing-guide); strategic template body not inspected, preventing a full starter-content inventory |
| Plain/typed page bodies and ordinary file editing | `FORMAT.md`, `skills/update/SKILL.md`; direct | [MEM-OBJ-page-prose](#mem-obj-page-prose), [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages); external I/O unverified |
| CSV tables, schemas and conversion | `FORMAT.md`, `skills/setup/SKILL.md`; direct | [MEM-OBJ-table-types](#mem-obj-table-types), [MEM-RTE-table-conversion](#mem-rte-table-conversion) |
| Editor payloads, sidecars, attachments and embedded display | `FORMAT.md`; direct; `skills/update/references/editor-pages.md` creation/embedding sections direct | [MEM-OBJ-editor-pages](#mem-obj-editor-pages); detailed formats/renderers uninspected, so readable agent summaries are not presumed equivalent to payloads |
| Decision answers, desktop buttons, views and transclusion | `skills/update/references/components.md` decision through transclusion sections; direct | [MEM-RTE-component-consumption](#mem-rte-component-consumption); host implementation unavailable |
| Diagnosis, stale/outdated treatment, link/ID repairs, deletion/restore | `skills/update/SKILL.md`, `FORMAT.md`; direct | [MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance), [MEM-OBJ-recovery-records](#mem-obj-recovery-records) |
| Legacy item migration and retirement | `skills/update/references/migrating-v1.md`; direct | [MEM-RTE-legacy-migration](#mem-rte-legacy-migration) |
| Destination selection, move to team and archive withdrawal | `skills/connect/SKILL.md`, `skills/team/SKILL.md`; direct; team endpoint declaration supplied by runtime | [RT-RTE-team-transition](runtime.md#rt-rte-team-transition), [MEM-OBJ-destination-metadata](#mem-obj-destination-metadata); hosted persistence/access/history unverified |
| CLI, browser, desktop and other-agent alternatives | `README.md` CLI/file sections, `FORMAT.md`; direct; other-agent host details supplied by runtime | [MEM-RTE-cli-file](#mem-rte-cli-file); no shipped dispatch/tool implementations to inspect |
| Plugin/CLI replacement | Supplied runtime, `CONTRIBUTING.md` direct | [RT-RTE-plugin-update](runtime.md#rt-rte-plugin-update); not an inspected experience-driven update mechanism |
| Tour only | `skills/start/SKILL.md`; direct | Says not to write pages; points to capture/setup/recall, not another memory writer |

## Core ideas

1. **Derived prose, not transcript replay.** Capture selects people's decisions, alternatives, reasons and unresolved questions, excludes routine progress, then changes existing subject pages. Available verbatim human input is attached as a citation rather than used as the entire memory. The retained prose is explicitly intended for later recall. This is a prescribed trace-fed update, not observed autonomous learning or evidence of improved capacity ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [MEM-OBJ-page-prose](#mem-obj-page-prose)).
2. **Two targeting channels.** Marks support keyword/kind/person queries; `paths` globs support code-to-page targeting. The agent then reads whole pages because mark snippets omit reasons. About five pages is advice, not a token-budget enforcement point. Team recall lacks the local-only marks/coverage tools ([RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall), [MEM-OBJ-page-metadata](#mem-obj-page-metadata)).
3. **Retained instructions are a special consumer path.** Ordinary page text is declared data, yet the installed guide is deliberately read and followed before writing and overrides base writing advice. Its admission differs from ordinary additions: replacing an existing guide needs approval. This is intended behavioral authority, not demonstrated compliance or injection resistance ([MEM-OBJ-writing-guide](#mem-obj-writing-guide), [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing)).
4. **Durability and currency differ.** Trash, activity and moved local archives preserve material without making it current answer context. Stale pages are not automatically rejected; readers must report staleness. Physical retention alone does not establish a recall route ([MEM-OBJ-recovery-records](#mem-obj-recovery-records), [MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance), [RT-RTE-team-transition](runtime.md#rt-rte-team-transition)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-page-prose
Label: Page prose and attribution
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

The natural-language body of a local Markdown page is the decision/context-bearing part of the supplied mixed file object. This part excludes identity/coverage keys and editor payloads. The analogous team body is collaborative Markdown on an external server; no team storage engine is established. Lineage can be user edits, model synthesis of repository material or current session inputs, or migrated old items. Initial corpus contents are not supplied. Tool-made citations retain human words and identity/time metadata; manual attribution remains permitted when tools find none. Marks do not make the model author of the human decision. The later consumers are recall, writing agents and people; their interpretive knowledge use is not executable truth enforcement. Reasons belong around the mark, not inside a guaranteed complete snippet. SRC-1, `skills/capture/SKILL.md`, `skills/update/SKILL.md`, `skills/recall/SKILL.md`.

> If neither lists it, name the person and where it was said in prose: `(Dana Lee, in a Claude Code session, 2026-10-01)`.
> --- `skills/update/SKILL.md`

> Never invent a decision, a reason or a quote.
> --- `skills/update/SKILL.md`

#### MEM-OBJ-page-metadata
Label: Page fields, identity and coverage
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

This is the symbolic frontmatter/link/mark-attribute part of local pages, distinct from their prose. Flat YAML stores identity, title, ordering, type, status and fields; `paths` is conventional rather than reserved. External tools use repository-relative globs to find pages affected by files. These globs are retrieval/access metadata, not a summary of the covered code. IDs survive rename; links carry relative paths and IDs so scans can repair moved targets. A typed schema does not verify the body. Mark attributes expose kind/person/date for filtering, while their sentences require interpretation. Humans and agents can set these values; library scans are also specified to add missing IDs and repair links, with no per-repair approval. Malformed/unsafe IDs and duplicates have separate repair/read-only contracts. SRC-1, `FORMAT.md`, `skills/update/SKILL.md`, `skills/setup/SKILL.md`; recall consumer: [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall).

> Tools match it against changed files to find the pages a change affects (`nim mcp`'s `pagesForFiles`); nothing else depends on it, and it shows like any other field.
> --- `FORMAT.md`

#### MEM-OBJ-writing-guide
Label: How we write this wiki
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

A material page-role within the supplied page container, not a duplicate of its authority path [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing). The installed guide is natural-language, initially copied from the shipped base version 8, then editable by the team. Its local substrate is a page file; the team substrate is externally hosted collaborative content. Later writers read this guide and Home. The guide says what belongs, how decisions/reasons are recorded and which visuals to choose. Existing-guide merge has explicit human approval; that differs from normal direct page writes. Missing-guide fallback consumes static shipped guidance, which is not itself accumulated memory. SRC-1, `skills/setup/SKILL.md`, `skills/setup/references/wiki-guide.md`, `skills/update/SKILL.md`.

> **Hard-won lessons.** A failure someone would repeat, with the rule it taught. Skip the incident narrative.
> --- `skills/setup/references/wiki-guide.md`

This permits derived lessons without the full incident narrative. It does not promise that every behavior-shaping rule retains its originating criticism. Ordinary decisions are instead asked to retain reasons, and recall explicitly reads surrounding prose. Neither rule demonstrates actual criticism, reliable generalization or improved future capacity.

#### MEM-OBJ-table-types
Label: Table rows and type definitions

No counterpart after comparison with [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages): the material alternate substrate is one CSV per table type, explicitly without page bodies/children, plus schema files outside the wiki page tree. Symbolic field encodings include scalar strings/numbers, IDs, semicolon-separated multivalues and JSON cells. Text cell meaning remains human/model-interpreted. Types live at `.nimbalyst/trackers/<type>.yaml`; only an explicit `storage:` makes the type's items wiki-stored. Other app types can be linked without becoming local wiki memory. External readers consume field definitions for header/table display and typed I/O; `tableView.defaultColumns` determines visible columns, so a stored field is not necessarily shown. Team type schemas are externally stored through tools. Human agreement admits a type; the agent writes the schema; destructive overwrite/narrowing needs additional approval. SRC-1, `FORMAT.md`, `skills/setup/SKILL.md`.

> `storage: table`: one CSV for the whole type. No bodies, no children.
> --- `FORMAT.md`

#### MEM-OBJ-editor-pages
Label: Editor payload and sidecar
Part of: [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Editor file bodies and hidden YAML sidecars form another operative part of the supplied page container. Bodies keep their native file text; sidecars hold identity/order/fields separately. Payloads can mix prose with symbolic layout, formula, graph or schema structures. No embedding-vector or model-weight store is specified by these formats; exact extension-specific representations remain uninspected. Attachments are files under a page's hidden `.assets/`, carried with it but not pages. Initial content is authored by a person/agent or imported; later browser/editor writes persist in those files. On local wiki the agent may create supported editor types; team terminal creation is Markdown-only, though existing editor pages can be embedded. The named consumer is the external editor/rendering host or file-text tools, not an established lossless prose-summary route. SRC-1, `FORMAT.md`, `skills/update/references/editor-pages.md`.

> The file keeps its own extension and its content is exactly what that editor reads and writes; the format never adds anything to it.
> --- `FORMAT.md`

#### MEM-OBJ-recovery-records
Label: Activity, trash and caches

Distinct from current pages [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages): typed-item activity is append-only `.activity.jsonl`, recording actor/time/action/field changes. Trash is a hidden retained recovery container with a JSON manifest and moved files, or saved row cells. Both are primarily symbolic records; they are not distilled lessons. Activity accompanies typed items; deletion history is not evidence that recall reads raw activity. Restore consumes trash to reintroduce content into the live tree. Purge is the declared irreversible deletion boundary. Team history is only a supplied external contract. Search indexes/backlinks/read state are described as caches, not portable authoritative format objects; implementation and any cache invalidation are unavailable. SRC-1, `FORMAT.md`, `skills/update/SKILL.md`.

> Only an explicit purge of an entry already in trash deletes files.
> --- `FORMAT.md`

> Backlinks, search indexes, saved views, kanban positions and read state are caches.
> --- `FORMAT.md`

#### MEM-OBJ-destination-metadata
Label: Wiki destination metadata

Distinct from page content [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages), and consumed by [RT-RTE-team-transition](runtime.md#rt-rte-team-transition). `.nimbalyst/local-wiki.json` chooses a local location and can record `migratedTo`; `.nimbalyst/wiki.json` pins a team project; `.nimbalyst-wiki.yaml` records local format version and optional immutable `wikiId`. These are symbolic file metadata, not knowledge prose. User choice admits location/project; the prescribed move creates routing metadata and archives the local copy. Later sessions use these identifiers to locate the same store and avoid treating the archive as current. `wikiId` keys resumptive migration copies. Physical implementation remains external, and project pins explicitly grant no access. SRC-1, `FORMAT.md`, `skills/connect/SKILL.md`, `skills/team/SKILL.md`.

> Its presence never starts anything on its own (no status prompt, no binding, no project creation).
> --- `skills/connect/SKILL.md`

### Routes

#### MEM-RTE-wiki-maintenance
Label: Diagnose, repair and withdraw wiki content

Distinct maintenance route alongside session-driven [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): large rework/tidiness claim triggers the foreground agent's `wikiDoctor`, then targeted repair of links/orphans/duplicate titles/dead paths/stale pages. The diagnostic call changes nothing. Agent proposes semantic repairs; writing tools perform I/O. External library scans separately repair IDs and moved links according to the format contract. Open maintenance mode, no reference-answer oracle; doctor issues are diagnostics, not semantic truth adjudication. Routine permitted edits need no per-content approval, but another person's rewriting/deletion needs asking. Original human content can veto destructive changes. Guidance is update plus retained guide. Recovery is reread after version conflict, trash restore or external team history; atomic file writes are not a multi-page transaction. SRC-1, `skills/update/SKILL.md`, `FORMAT.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Issues and updated/outdated page links; scan implementation/results unavailable.
- Later read-back: Repaired current pages and outdated status reach later recall; trashed content returns to live reads only after restoration.
- Delegated visibility: Foreground agent sees diagnostics and selected pages; external tools see affected files, with no separate inference worker prescribed.
- Selection predicate: Large rework/tidiness check; affected code globs and doctor issue categories; library scans additionally check IDs and link targets.
- Invalidation or expiry: Outdated status is explicit rather than a TTL; deleted items leave the current tree for trash; purge deletes retained recovery files.
- Activation or effect: Requests changed prose/metadata/navigation or withdrawal; no observed repair or improved answer.
- Evidence limits: External diagnostics, locking, restoration and actual admission compliance cannot be verified from prompt/format text.

> **Checking the wiki.** After a large rework, and before saying the wiki is tidy, call `wikiDoctor`. It changes nothing; fix what it reports with the tools above:
> --- `skills/update/SKILL.md`

#### MEM-RTE-table-conversion
Label: Convert table storage to pages

No counterpart after comparison with [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup): this converts already retained row state rather than initializes the wiki. A user need for notes triggers local `convertTypeStorage` or documented `nim wiki convert-type`; the external converter owns row-to-page serialization, per-page read-back, activity relocation, schema storage switch and CSV trash. Source specifies refusal before writes for incompatible schema/header conditions. User chooses conversion, software applies its checks; no separate human approval of every generated page is specified. No answer oracle; read-back tests persistence rather than truth. SRC-1, `FORMAT.md`, `skills/setup/SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Conversion result/error; exact payload unavailable.
- Later read-back: Same IDs and field values become page files; typed-page tools and people can consume them, while body/children become possible.
- Delegated visibility: External local converter reads rows, type file and activity; no foreground model synthesis is specified.
- Selection predicate: One selected table type; safe plain storage line and permitted column names are preconditions.
- Invalidation or expiry: Old CSV moves to trash after conversion; schema changes to pages, not duplicate active stores.
- Activation or effect: Storage transformation, not semantic learning; caller is told not to move CSV or change storage by hand.
- Evidence limits: The prescribed read-back and pre-write refusal are not inspected executable code or a demonstrated rollback guarantee.

> To convert a table type, call `convertTypeStorage` (`storage: pages`); it keeps item ids and field values, so never move the CSV or edit `storage:` by hand.
> --- `skills/setup/SKILL.md`

#### MEM-RTE-legacy-migration
Label: Legacy graph to prose migration

A distinct transformation of historical retained knowledge, related to but not identical with setup [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup). Agent proposes a plan, adds prose one area at a time, preserves old item keys and sources, and asks before retiring old items. The old graph is not the current file model. Inputs include claims, findings, questions, investigations and decisions; outputs place their meaning on subject pages. Humans can reject deletion/archive/overwrite item-by-item or batch; showing a plan is not proof of explicit approval for every additive sentence. Open migration mode; no reference-answer oracle beyond the supplied original items for fidelity checking. SRC-1, `skills/update/references/migrating-v1.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Migrated pages, provenance keys and deliberate omissions reported to the person.
- Later read-back: Ordinary page recall can read migrated conclusions with linked sources; old graph access/history remains external.
- Delegated visibility: Foreground agent interprets old content; no separate worker prescribed.
- Selection predicate: Legacy model found and separate migration job started; items mapped to affected pages, one area at a time.
- Invalidation or expiry: Old items remain until approved retirement; superseded values may be omitted except when historical change matters.
- Activation or effect: Requests representation change and provenance retention, not demonstrated fidelity or better reasoning.
- Evidence limits: No migrated corpus, loss audit, executable migration or later consumption trace supplied.

> **Keep every source.** Each citation, URL, session id, document link and date on an old item goes into the sentence it supports.
> --- `skills/update/references/migrating-v1.md`

> Superseded claims | Only the current value, plus "until 2026-08, it was X" when the change matters.
> --- `skills/update/references/migrating-v1.md`

The second passage is a table-row fragment: its selective history policy qualifies any claim that migration retains the whole old reasoning record. Finding scope/limitations and investigation outcomes are explicitly asked to survive, but exact old representations need not.

#### MEM-RTE-cli-file
Label: CLI and direct-file alternatives

Distinct from the host plugin entry [RT-RTE-host-entry](runtime.md#rt-rte-host-entry): README affords terminal/script callers and FORMAT affords people/editors/Git reading and writing ordinary files without the plugin. These are documented consumer roles, not inferred deployed callers. CLI read selects title/path/id, search selects query; write replaces from stdin/file. A human may supply content directly or an agent/script may author it, so CLI invocation alone leaves per-content human approval unresolved. File mutation need not invoke capture or guide. Optional expected-version checking is not a universal gate. Recovery outside cooperating tools depends on the editor/Git/user rather than the claimed trash protocol. SRC-1, `README.md`, `FORMAT.md`.

- design conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Documented page text/tree/search output or write result, plus browser URL for serve; exact outputs uninspected.
- Later read-back: Persisted files can be read by later agents, people, CLI and browser; shared files do not require the original writer's conversation.
- Delegated visibility: Caller supplies input files/stdin and receives selected results; no hidden agent delegation established.
- Selection predicate: CLI title/path/id/query; local default with team fallback for documented list/read/move/search, explicit team/local override; arbitrary file choice outside CLI.
- Invalidation or expiry: Body replacement can supersede prior content; CLI expected-version is optional; direct-file retention follows caller/editor policy.
- Activation or effect: Affords alternate admission and read-back, not enforcement of plugin workflow or successful mutation.
- Evidence limits: Actual CLI dispatch, browser transformations, permissions and direct-editor compliance with the lock contract are outside the source.

> `write` replaces a page body from stdin or `--file`. With `--expected-version` (from `read --json`) it refuses to overwrite a page that changed since you read it.
> --- `README.md`

#### MEM-RTE-component-consumption
Label: Retained components to host actions

Distinct from prose recall [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall). Retained Markdown can encode decision questions/answers, placed-view selectors, action prompts and new-item templates. The external host interprets symbolic block/link keys; humans/models interpret the natural-language question/prompt/template. A named person answers a decision block; the app records votes/identity/time and a later writer is instructed to mark the outcome in the affected page. Desktop-only buttons can start a new agent session or create a typed page from a literal/page-body template. This is an afforded consumer route, not in-repository host implementation. Source: SRC-1, `skills/update/references/components.md`.

- design conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Rendered view/question or button action; actual created-session context/output uninspected.
- Later read-back: Later page viewers consume persisted answers or selectors; clicking an action supplies its retained prompt to an agent, and new-item can copy a retained template body.
- Delegated visibility: Desktop action starts another session; other transferred context and return-to-caller behavior are uninspected, so frame isolation cannot be established.
- Selection predicate: Human click for buttons, named responders for decisions; view keys select fields/filter/sort; transclusion selects a page or heading in desktop only.
- Invalidation or expiry: Live views follow underlying pages; handwritten snapshots require same-pass updates; no action/template TTL specified.
- Activation or effect: Prescribes interpretation, answer retention and explicit human-triggered actions; no exercised downstream behavior established.
- Evidence limits: Browser/desktop rendering and answer recording unavailable; desktop action is not evidence that arbitrary recalled page instructions execute.

> An `action` block is a button that starts an agent session with its `prompt` (optional `label`, `model`, `effort`).
> --- `skills/update/references/components.md`

> Once a block is resolved, also write the outcome as a `decided` mark in the page it affects.
> --- `skills/update/references/components.md`

Admission: page-writing policy governs authored prompts/templates; the human click admits the documented action, not an inspected safety review. Decision answers are human input, with app-side metadata rather than agent-fabricated votes. Rejection is nonparticipation/nonclick or later edits under normal page policy; a dedicated transaction rollback is not specified. These are not demonstrated theories or improvements.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Memory lineage: conversation and changed files → model-selected decisions/questions/context → persistent affected pages → later recall/code work. Raw human session input can support verbatim citations; team comments provide a separate input route. Neither storing raw transcripts nor a citation-tool name establishes semantic curation by that server. The foreground agent does the requested synthesis, while tools execute writes. Ordinary additions are admitted directly; starting capture is not per-content approval. Candidate rejection includes “nothing to record”, duplicate avoidance, irrelevant code changes and exclusion of routine progress. Citation absence does not universally reject a write. Reasons are requested in prose; compliance/fidelity and later activation remain unobserved. SRC-1, `skills/capture/SKILL.md`, `skills/update/SKILL.md`; minimum passages supplied by the runtime record and [RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation).

#### On [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall)

The foreground agent requests selected retained content; this is pull, even when it proactively recalls before changing code without a new explicit user retrieval request. Keyword/kind/person filtering, file globs and relevant full-page reading are different selection stages. Marks return handles/snippets, but the prescribed later consumer receives surrounding page prose to recover reasons. About five pages bounds page count heuristically, not bytes/tokens. There is no prescribed trimming of prior conversation or replacement checkpoint. Pages not loaded remain reachable via tools, not references automatically dereferenced in the model window. This resembles external demand loading but not pointer-based heap liveness. Model/host compaction and separate-context behavior are uninspected. SRC-1, `skills/recall/SKILL.md`; runtime record supplies the passage establishing whole-page reading.

#### On [RT-RTE-host-entry](runtime.md#rt-rte-host-entry)

SessionStart is a claimed push path from retained local wiki coverage/changed-file matches into foreground context, independent of an explicit query. Stop instead requests a write; it is not itself an extraction or durable-memory result. Manifests wire external commands, not the selectors or content budget. Trigger is host event; automatic selector implementation, selected fields/full bodies, truncation, persistence of injected output and actual consumer acceptance are uninspected. SRC-1, `hooks/hooks.json`; runtime supplies README's changed-file description and Codex exception.

> At session start, tell the agent what the project's local wiki covers.
> --- `hooks/hooks.json`

#### On [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup)

Read-back checks newly admitted pages before reporting success, not proof of later recall. Setup can install code-derived paths and optional repository instruction lines directing future readers to Home/covering pages/capture. User says yes to those instruction-file changes; teammates without the plugin can then encounter the pointer. The pointer is symbolic location plus natural-language guidance, not copied wiki content. Missing-guide initialization is specified; an existing guide must not be overwritten and approved merges preserve team changes. Source: SRC-1, `skills/setup/SKILL.md`; record already retains merge-approval passages.

#### On [RT-RTE-team-transition](runtime.md#rt-rte-team-transition)

Migration is meant to transfer retained content without flooding the foreground conversation: local server sends batches and rewrites links, returning counts/errors/Home URL, not page bodies. Dry-run skips remain local; thus “verified” must not imply every local item became team-visible. Later `connect`/recall choose team destination using pins/migrated metadata; the kept local copy is not default current memory. An inaccessible team may cause explicit user-authorized local use, and recall must label archive results. These qualify absolute exclusion of archive reads, not ordinary no-double-write policy. Hosted storage, permissions, history and migration idempotency remain contracts. SRC-1, `skills/team/SKILL.md`, `skills/connect/SKILL.md`, `skills/recall/SKILL.md`; runtime retains the batch/no-page-text passage.

#### On [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing)

This path supplies a local retained procedure rather than only task facts. Guide edits can change later content-selection and visual choices across sessions. Update consumer and downstream coding consumer differ: capture changes knowledge prose; guide changes later writing guidance; recall requests use of knowledge but does not prove changed code behavior. No source-provided run closes that chain. SRC-1, `skills/setup/references/wiki-guide.md`, `skills/update/SKILL.md`; runtime quotes the explicit override. The tension with treating page text as data remains an interpretation/enforcement limit, not a blanket memory distrust rule.

## Write side

Acquisition includes repository/docs plus discovery answers at setup, session inputs and changed-file context at capture, team comments through a separate citation tool, imported legacy items, and direct person/editor/CLI writes. Authors, decision makers and physical writers differ: the agent generally proposes/serializes prose; people own attributed decisions; external tools perform persistence. Initial user corpora are not available. Setup defaults and guided choices do not establish that unknown owners/values may be invented ([RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [MEM-RTE-cli-file](#mem-rte-cli-file)).

Curation is predominantly requested model work: filter routine progress, extend rather than duplicate, preserve attribution, replace superseded decisions, retain reasons, mark unknowns and use current snapshots. A session-to-page write is the prescribed trace-fed transformation; later recall supplies its consumer. Hard-won lessons may deliberately omit incident narrative, so reason preservation is not universal. No automatic full-transcript-to-summary checkpoint or model-parameter update is established; host compaction and training remain outside inspection, rather than evidenced absent ([MEM-OBJ-page-prose](#mem-obj-page-prose), [MEM-OBJ-writing-guide](#mem-obj-writing-guide)).

Maintenance changes access metadata as well as content: scan repairs IDs/links, doctor reports issues without writing, agent repairs meaning or marks outdated, table conversion changes substrate, and legacy migration converts structured historical items into prose with source keys. None of these alone establishes epistemic warrant. Human control is per mechanism: normal additions direct; approval for rewriting another person's content, existing guide merges, destructive schema changes, deletion and legacy retirement; conversion uses explicit request plus software preconditions. Tool locks/version checks govern physical consistency, not truth or approval ([MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance), [MEM-RTE-table-conversion](#mem-rte-table-conversion), [MEM-RTE-legacy-migration](#mem-rte-legacy-migration)).

Rejection and withdrawal have later consumers: empty capture returns nothing, invalid ID can make content read-only, stale body version refuses a cooperating tool write, outdated status survives for recall caveats, deletion moves content out of the live tree, restore reintroduces it, and migration routing withdraws archive currency while retaining files. Direct editors can bypass the tool procedure; no universal guarantee is inferred from FORMAT. Team history and local trash are different recovery substrates ([MEM-OBJ-recovery-records](#mem-obj-recovery-records), [RT-RTE-team-transition](runtime.md#rt-rte-team-transition)).

## Read-back

The principal chain is task/question or intended code files → marks/search/coverage selection → full-page read → foreground answer/code work. It delivers interpreted attributed knowledge, not an enforced plan. Captured reasons can reach later readers through surrounding prose. A schema's fields, cache index, raw activity or trash entry do not establish that same consumer path. Trash has a restore consumer; table cells have typed readers; editor payloads have renderers; destination metadata has routing consumers ([RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall), [MEM-OBJ-table-types](#mem-obj-table-types), [MEM-OBJ-editor-pages](#mem-obj-editor-pages)).

Other directions remain separate: SessionStart claims unsolicited coverage context; guide/Home are requested before writing; desktop buttons explicitly deliver retained prompts/templates on human click; CLI and browser afford later human/tool reads without the plugin skills. Views are live symbolic selectors; local replacement lists/maps are snapshots requiring maintenance. The source does not establish whether an embedded editor object's complete payload, display summary or extracted text reaches a later model. Static installed skills/base guide are behavioral input, but only installed and subsequently edited guide content is accumulated retained material ([RT-RTE-host-entry](runtime.md#rt-rte-host-entry), [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing), [MEM-RTE-component-consumption](#mem-rte-component-consumption), [MEM-RTE-cli-file](#mem-rte-cli-file)).

No shipped separate model worker/fork-return protocol was found in the inspected skill entry points. The desktop action affords a new session but supplies no inspection of its isolation or return. Migration's no-body-return policy keeps copied content outside conversation; that is not a summarization mechanism. Context page-count advice, limited search retries and proportionate reads are the specified working-window controls. Old-turn eviction, preferential tool-result trimming, summary checkpoints and reload after compaction remain host questions, not properties established by these files.

## Integration issues

- **Additional alternative admission route:** [MEM-RTE-cli-file](#mem-rte-cli-file) qualifies any global interpretation of stale-write or destination guarantees in [RT-RTE-host-entry](runtime.md#rt-rte-host-entry) and [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). README makes expected-version optional and CLI defaults differ from the fuller connect policy. This extends coverage, not a correction to runtime's already scoped claims.
- **Additional consumer route:** [MEM-RTE-component-consumption](#mem-rte-component-consumption) adds desktop retained-prompt/template and decision-answer paths absent from the supplied route inventory. It is not ordinary recall or a demonstrated host execution path. Buttons are documented in `skills/update/references/components.md`; frozen host code is unavailable.
- **Contained parts, not duplicates:** page prose, metadata, guide and editor records declare material parts of [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages). Guide object and [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing) name different things: stored text versus its consumer/authority path. Table types, recovery records and destination metadata are distinct objects; maintenance, conversion, legacy migration and CLI/component consumption are distinct routes. No possible duplicate declaration remains after comparison.
- **Unresolved external implementation:** search ranking/coverage freshness, hook payload/budget, transcript isolation, actual field/body delivery, editor model-readable extraction, hosted access/history, file locking and migration verification cannot be resolved from SRC-1. Consequence: prescribed/afforded mechanisms cannot be upgraded to executed or reliable memory operation. A verified migration flag is not independent proof of fidelity; skipped items remain local ([RT-RTE-team-transition](runtime.md#rt-rte-team-transition), [MEM-OBJ-editor-pages](#mem-obj-editor-pages), [MEM-OBJ-recovery-records](#mem-obj-recovery-records)).
- **Reason retention is scoped:** decision prose asks for reasons and recall reads surrounding text, but hard-won lessons omit incident narrative and legacy conversion selects current values. Therefore no universal raw-evidence/reason retention claim follows ([MEM-OBJ-writing-guide](#mem-obj-writing-guide), [MEM-RTE-legacy-migration](#mem-rte-legacy-migration)).
- **Supplied-fact corrections:** none. Destination-order tension, guide/data authority tension, Codex hook/citation exceptions and alternate file writers remain as supplied, with bounded annotations rather than silently revised facts.

## Limitations and checks

The source and boundary identity were rechecked against Git HEAD and tracked paths before analysis. Method inputs were read as supplied, with truncated delivery recovered through bounded reads; the assigned contracts govern this report. No target execution, dependency installation, provider/service calls or new source acquisition occurred. Source-native operations and data formats are established as contracts; no execution trace establishes model obedience, durable writes, later activation, benefit, learning or exercised self-improvement. Uninspected strategic/visual reference detail prevents exhaustive starter-content/rendering claims, not the supported alternate consumer inventory above.

Validation: the required `commonplace-validate` member check passed. Its complete result was “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes content form and quotation checks, not semantic acceptance or source support.
