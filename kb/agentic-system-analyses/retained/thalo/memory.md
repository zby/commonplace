---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Thalo memory mechanisms: file-backed entries, schema and prompt authority, incremental synthesis and checkpoint limits."
run-id: AAS-2026-10-14-thalo-86fcc3efe983-01
source-identity: "https://github.com/rejot-dev/thalo"
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
---

# Thalo memory report

## Boundary and evidence

The memory boundary follows the whole knowledge-system boundary in [boundary](boundary.md#boundary-and-evidence). It includes ordinary entry and schema files, synthesis definitions, generated Markdown, actualization metadata, query and change-tracker selection, local maintenance, editor reload, browser snapshots, the action and its shipped Pi command. External model parameters are included as an opaque operative dependency, not as an inspected store. General development agents, external provider internals and production host behavior remain excluded as the boundary specifies. Those exclusions prevent conclusions about deployed model retention, enclosing-agent session management and actual human acceptance.

Evidence is SRC-1, implementation and doctrine/design at the registered commit. Direct reads rechecked synthesis extraction, actualize, both trackers, marker parsing, query service and command, CLI query and dispatch, the Pi command, action orchestration, VFS loading/persistence, workspace rebuild, schema resolution, scripting API sections, skill, sample schemas/entries, sample guide, and browser state owners. Supplied runtime findings supply the editor lifecycle, init, formatting and merge-driver paths below; they are not represented as new direct reads. No target execution or observed-run evidence supports this report. HEAD matched the reviewed commit and `git status --short` was empty at inspection.

### Coverage

| Entry point or operation | Source paths, SRC-1 | Coverage and limits |
| --- | --- | --- |
| CLI dispatch; ordinary authoring, init, formatting and merge | `apps/thalo-cli/src/mod.ts`; `apps/thalo-cli/src/commands/init.ts`; `apps/thalo-cli/src/commands/format.ts`; `apps/thalo-cli/src/commands/merge-driver.ts`; `skills/thalo/SKILL.md` | Dispatch and skill directly read; maintenance implementation supplied by [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring). Caller determines content; filesystem writer admits it. Full merge/formatter semantics not audited; correctness of conflict resolution is not established. |
| File discovery, parsing and reload | `packages/thalo/src/vfs/loader.ts`; `packages/thalo/src/model/workspace.ts` | Direct reads: [MEM-CMP-workspace](#mem-cmp-workspace). Scratch loading admits parsed state but is not a semantic truth gate. Parser internals not exhaustively inspected; exact malformed-input recovery remains unresolved. |
| Schema maintenance and checking | `packages/thalo/src/schema/registry.ts`; `packages/thalo/src/checker/rules/actualize-missing-updated.ts` | Direct reads: [MEM-OBJ-schema-entries](#mem-obj-schema-entries), [MEM-RTE-schema-resolution](#mem-rte-schema-resolution); supplied [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) covers diagnostics. No complete rule-correctness audit or observed correction loop. |
| Requested query/read-out and library views | `apps/thalo-cli/src/commands/query.ts`; `packages/thalo/src/commands/query.ts`; `packages/thalo/src/services/query.ts`; `packages/thalo/src/api.ts` | Direct reads: [MEM-RTE-query-readout](#mem-rte-query-readout). Distinguish raw payload from metadata display. API has no identified deployed downstream model consumer. |
| Synthesis definition and changed-entry selection | `packages/thalo/src/services/synthesis.ts`; `packages/thalo/src/commands/actualize.ts`; `packages/thalo/src/services/change-tracker/git-tracker.ts`; `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`; `packages/thalo/src/services/change-tracker/change-tracker.ts` | Direct reads and annotations on [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection) and [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint). Current-instance filtering does not deliver deletion/retraction notices. |
| Model transformation and durable read-back | `packages/scripts/src/synthesize-with-pi.mjs` | Direct complete read; [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose), annotations on [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis). Host admits nonempty text; semantic compliance and model-internal compaction remain uninspected. |
| Publication, review, failure and withdrawal | `packages/thalo-action/src/action.ts` | Direct complete read and [RT-RTE-action-publication](runtime.md#rt-rte-action-publication). Commands precede branch publication; human PR rejection is later, external to local admission. Earlier local writes survive a subsequent failure. |
| Revision-aware library file write | `packages/thalo/src/vfs/persistence.ts`; `packages/thalo/src/vfs.ts` | Direct persistence read and bounded caller search. Optional hash mismatch rejects a write. No production caller using this guard was identified in the searched `packages`/`apps` roots; this is a capability, not an established later-consumer route or universal write guard. |
| LSP/VSCode edit, formatting and reload | `packages/thalo-lsp/src/server.ts`; `packages/thalo-vscode/src/mod.ts` | Supplied [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring), [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback); bounded registration search found formatter/restart and configuration registrations. These are editor consumers, not registered model retrieval tools. Full handler internals not read; all editor transformations are not enumerated. |
| Browser preparation and reset | `apps/docs/app/components/playground/playground-context.tsx`; `apps/docs/app/components/playground/thalo-runner.ts`; `apps/docs/app/components/demo/demo-context.tsx` | State owners directly read; runner supplied by [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection). [MEM-OBJ-playground-state](#mem-obj-playground-state) is session state; no browser-to-provider route is established. Demo step navigation is presentation state, not synthesis execution evidence. |
| Example KB, rationale and instructions | `thalo-test/entities.thalo`; `thalo-test/entries.thalo`; `thalo-test/typescript-guide.md`; `thalo-test/AGENTS.md` | Direct reads support authored rationale and user guidance, not authenticated model-run artifacts. Other example files and most documentation remain available but uninspected; no complete fixture provenance or doc-consistency conclusion. |
| Provider state | `packages/scripts/src/synthesize-with-pi.mjs` | [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini). Weights, provider retention and actual processing inaccessible within this boundary. No parameter-update or endpoint-immutability conclusion beyond supplied limits. |

## Core ideas

Thalo retains readable content in files while symbolic metadata controls access. A source entry can carry reasons and caveats; its entity, tags, links and metadata determine whether code emits it. These two roles must not be collapsed into either a prose-only store or a symbolic-only memory. See [MEM-OBJ-instance-entries](#mem-obj-instance-entries) and [MEM-RTE-query-readout](#mem-rte-query-readout).

The incremental synthesis selector and the model context are different scopes. The selector returns current matching instances changed since a marker. The shipped command then adds the entire existing target file. Prior generated prose can therefore shape a later generation even when its original source entry is not emitted again. No explicit token cap, ranking, eviction or token-budget compaction is configured in the inspected command. See [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis), and [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose).

A checkpoint records a selector position, not evidence that the model faithfully incorporated the selected material. Deletion and loss of query membership are important countercases to complete dependency invalidation: neither produces a current matching instance to send. Existing prose may retain a withdrawn claim. Missing or switched markers can replay all current matches, but that is not a retraction channel. See the annotations on [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint) and [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection).

Structural checking is feedback rather than universal admission control. Human/external-agent edits, merge output and the Pi writer can enter files without that check. A confidence or source-status field can be queried, but does not certify truth; the sample guide query includes every `#typescript` opinion, including the sample `#bad` low-confidence entry. SRC-1, `thalo-test/typescript-guide.md`, `thalo-test/entries.thalo`, `thalo-test/entities.thalo`; [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback).

## Shared records

### Components

#### MEM-CMP-workspace
Label: Parsed workspace and derived indexes

Source-native identity: `Workspace`, documents/models, schema registry, link index and dependency maps. Representational form: symbolic ASTs/indexes containing natural-language source payload; storage substrate: process-memory Maps and Document source copies. Lineage: parsed/rebuilt from caller-supplied files, not a separately authoritative knowledge database. Direct SRC-1 reads: `packages/thalo/src/vfs/loader.ts`, `packages/thalo/src/model/workspace.ts`. Closest supplied records are [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring) and [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection); those are consumer routes, not this derived component.

The loader builds a scratch workspace and installs its maps only after reads finish. It clones any existing models first; a reload into a reused workspace does not itself prove removal of files no longer discovered. Workspace mutation/deletion APIs and supplied editor lifecycle are separate. Thus fresh-load selection and arbitrary repeated library loading need not have identical withdrawal semantics.

> for (const model of workspace.allModels()) {
>   scratchWorkspace.updateDocument(model.file, model.source);
> }
> --- `packages/thalo/src/vfs/loader.ts`

> target.models = new Map(scratch.models);
> target.documents = new Map(scratch.documents);
> --- `packages/thalo/src/vfs/loader.ts`

Consumers are queries, navigation, checker and synthesis extraction. Symbolic membership affects these operations deterministically; it does not establish semantic trust or model compliance. Workspace `clear` discards derived state, not underlying files. Persistence comes from reloading files, not retaining this process object across jobs.

### Operative objects

#### MEM-OBJ-instance-entries
Label: Knowledge instance entries

Source-native identity: `InstanceEntry`, including `create`/`update` entries, sections and metadata. Storage substrate: `.thalo` text or embedded Thalo fences in Markdown, subsequently copied into workspace models. Form at human/model consumption: natural-language sections and rationales. Form at query/checker consumption: symbolic headers, tags, links and metadata values. Initial authorship can be human, software or external agent; the samples are authored fixtures, not operational traces. SRC-1, `thalo-test/entities.thalo`, `thalo-test/entries.thalo`, `packages/thalo/src/services/query.ts`, `packages/thalo/src/services/synthesis.ts`.

Closest supplied record is [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring), a write route rather than this retained content. This object is distinct from [RT-OBJ-command-input](runtime.md#rt-obj-command-input), its transient serialization. Selected raw text includes reasons when they exist. The sample schema requires Reasoning for opinions, while reference Summary and Key Takeaways are optional:

> Claim ; "Core opinion in 1-2 sentences"
> Reasoning ; "Bullet points supporting the claim"
> Caveats? ; "Edge cases, limitations, exceptions"
> --- `thalo-test/entities.thalo`

The later Pi request includes selected raw source, not just a title pointer. Retaining a URL or `related` link does not fetch its destination in that command. Source truth and trace origin remain local to authored content; a `journal` or `reflection` label is not proof of captured runtime experience. The query service loops over all physical instance entries and does not resolve an `update` or `supersedes` relationship into a canonical active stance. A query may therefore deliver historical and successor text together. SRC-1, `packages/thalo/src/services/query.ts`; [MEM-RTE-query-readout](#mem-rte-query-readout).

#### MEM-OBJ-schema-entries
Label: Retained entity schema entries

Source-native identity: `SchemaEntry` / model schema entries with `define-entity` and `alter-entity`, fields, sections and removal lists. Form: symbolic type/requirement directives at registry/checker consumers; descriptions are natural-language documentation. Substrate: file text; derived EntitySchema Maps in process memory. Lineage: caller-edited definitions, then timestamp-ordered registry resolution. SRC-1, `packages/thalo/src/schema/registry.ts`, `packages/thalo/src/model/workspace.ts`, `thalo-test/entities.thalo`.

Distinct from [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring), which supplies a write mechanism, and [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback), which consumes resolved constraints. Later checks can change when retained schemas change, but uncalled checks cannot veto another writer. The [MEM-RTE-schema-resolution](#mem-rte-schema-resolution) passage establishes alteration and removal. Explanations in schema descriptions are readable; the inspected registry applies field/section directives, not their historical reasons.

#### MEM-OBJ-synthesis-sources
Label: Synthesis source queries

Source-native identity: `sources` metadata in `SynthesisEntry`; extracted `Query[]` in `SynthesisInfo`. Form: symbolic query values or arrays; storage substrate: retained file text, then parsed in-memory predicates. Lineage: caller-authored definitions. Consumer: tracker selection on each actualization. Queries have ANDed conditions; multiple sources combine by OR. SRC-1, `packages/thalo/src/services/synthesis.ts`, `packages/thalo/src/services/query.ts`.

Distinct from [RT-OBJ-command-input](runtime.md#rt-obj-command-input), which carries formatted query strings, and [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), which applies them. Editing a query changes membership on future loads, but unchanged instances newly admitted by that query are not necessarily emitted under an existing Git checkpoint. The Git tracker first restricts to changed files. Full rebuild after query or prompt change is therefore not guaranteed by the pending-entry predicate.

> const content = sourcesMeta.value.content;
> if (content.type === "query_value") {
>   return [astQueryToModelQuery(content.query)];
> }
> --- `packages/thalo/src/services/synthesis.ts`

#### MEM-OBJ-synthesis-prompt
Label: Retained synthesis prompt content

Source-native identity: content under prompt-containing headers of `SynthesisEntry`, extracted by `getSynthesisPrompt`. Form: natural-language instruction. Substrate: retained text file; later action JSON and model user prompt. Lineage: caller-authored or caller-edited definition, not automatically learned method text. Consumer: shipped model request, with interpretive rather than enforced authority. SRC-1, `packages/thalo/src/services/synthesis.ts`, `thalo-test/typescript-guide.md`. Closest supplied record [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance) describes its authority path; this declares the retained object, not a duplicate authority path. It is distinct from the static [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt).

The extractor accepts any Markdown header whose lowercase text includes `prompt`, not only the exact header `# Prompt`; another header ends collection. Material prompt scope follows this code, not merely the documentation label.

> if (headerText.includes("prompt")) {
>   inPrompt = true;
> } else {
>   inPrompt = false;
> }
> --- `packages/thalo/src/services/synthesis.ts`

#### MEM-OBJ-synthesis-prose
Label: Retained synthesized Markdown

Source-native identity: Pi script's `markdown` installed after the first Thalo block in the synthesis file. Form: natural-language Markdown interpreted by later model/human readers. Substrate: filesystem text, optionally committed/published by the action. Lineage: proposed model output derived from retained prompt, changed source entries and the entire previous file. Distinct from [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint), which is symbolic access state, and [RT-OBJ-command-input](runtime.md#rt-obj-command-input), which is transient input. Its producer/consumer route is [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis), not a second route declaration.

SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`. The minimum decisive read-back passage is:

> "Current File Content:",
> original.trim() || "(file is empty)",
> --- `packages/scripts/src/synthesize-with-pi.mjs`

This makes prior generated content a later generation input. It does not make it a higher-priority system instruction or certify factual adoption. The host neither demands retained reasoning nor records a source-to-output proof. Reasons can survive as generated prose, but their retention is model-dependent; selected raw entry reasons are supplied separately. Existing prose is not automatically returned by instance-query selection merely because it is in the same Markdown file.

The host replaces the old suffix rather than retaining a verbatim tail. This is product rewrite with recurrent read-back, not implemented conversation compaction. The first-fence countercase and exact write expression are already retained in [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis).

#### MEM-OBJ-playground-state
Label: Playground editable file snapshot

Source-native identity: React `PlaygroundState`, virtual files and `InMemorySnapshot`. Form: natural-language/symbolic text by content, plus symbolic panel/path/tab state. Substrate: browser process state. Lineage: defaults and optional initialState, then `setContent`; reset replaces it with defaults. SRC-1, `apps/docs/app/components/playground/playground-context.tsx`. Distinct from [MEM-CMP-workspace](#mem-cmp-workspace), the parsed consumer, and the browser alternative in [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection).

> const resetToDefaults = useCallback(() => {
>   setState(DEFAULT_STATE);
> }, []);
> --- `apps/docs/app/components/playground/playground-context.tsx`

This is current session working state, not established cross-session memory. Its virtual filesystem gives the runner current edited content; supplied runner evidence establishes deterministic preparation, not model synthesis/writeback. Reload after page exit and external durable saving remain uninspected, so no cross-page persistence is inferred.

### Routes

#### MEM-RTE-query-readout
Label: Requested knowledge query read-out

Endpoints/progression: saved entries → loaded workspace → caller query/checkpoint → symbolic match and optional limit → CLI display or wrapped API results. Owner: query code selects; caller requests and decides subsequent use. SRC-1, `apps/thalo-cli/src/commands/query.ts`, `packages/thalo/src/commands/query.ts`, `packages/thalo/src/services/query.ts`, `packages/thalo/src/api.ts`. Distinct from [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection): no synthesis definition, prompt or newly persisted checkpoint is required. It shares query predicates, not route identity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI default lists timestamp/entity/title/link/tags and file-line locations; JSON returns metadata/location, not section content; raw mode returns source text. API query returns wrapped entries with raw AST access.
- Later read-back: Previously saved or edited entry content reaches later caller requests through workspace loading. API exposure alone does not establish a model consumer; CLI stdout is the identified delivery endpoint.
- Delegated visibility: CLI caller gets its selected output format. No automatic agent/tool handoff is wired in these files; scripting documentation affords external programmatic reading.
- Selection predicate: Entity equality plus ANDed field/tag/link tests, OR across queries, optional since marker and result-count limit. Timestamp-ordered ordinary results are sliced from the beginning; no relevance score, embedding search or token budget appears in this path.
- Invalidation or expiry: Current workspace state replaces loaded text; since filtering can hide older material. Queries return physical instances rather than resolving superseded stances. Git since mode inherits current-entry and missing-commit limits of its tracker.
- Activation or effect: Selects and emits retained text or its metadata; caller semantic adoption is unobserved. This is pull/request delivery, not independent unsolicited supply.
- Evidence limits: Source establishes delivery surfaces, not effective use or complete downstream consumer enumeration. A display title/location is not the full retained payload.

> includeRawText: format === "raw",
> --- `apps/thalo-cli/src/commands/query.ts`

> const limitedResults = limit && limit > 0 ? results.slice(0, limit) : results;
> --- `packages/thalo/src/commands/query.ts`

#### MEM-RTE-schema-resolution
Label: Retained schema resolution

Endpoints/progression: parsed define/alter entries → registry → EntitySchema field/section Maps → later checker callers. Owner: deterministic registry code. Context: retained schema directives; effect: changed checking requirements, not knowledge truth. SRC-1, `packages/thalo/src/schema/registry.ts`, `packages/thalo/src/model/workspace.ts`. Distinct from [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback): this is its schema-input transformation, not diagnostic production or content approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Resolved schema or undefined if no definition is present.
- Later read-back: Edited/accumulated schema entries are reloaded and resolved for later checks; derived registry caches are reconstructed from models.
- Delegated visibility: Checker consumers receive typed constraints. Description strings remain in resolved schemas; no inspected model invocation consumes the entire registry automatically.
- Selection predicate: Requested entity name, base definition and alterations sorted by formatted timestamp; alteration fields/sections overwrite named values and removal lists delete them.
- Invalidation or expiry: Workspace rebuild clears registry and adds model schema entries again. Removing a constraint changes future resolution; it does not rewrite existing knowledge prose.
- Activation or effect: Deterministically changes available checking constraints; user compliance and universally gated writes are not established.
- Evidence limits: Bounded registry resolution read, not exhaustive duplicate-definition/cache correctness or test execution. External authorship and initial schema choices remain caller-dependent.

> const sortedAlters = [...alters].sort((a, b) => a.timestamp.localeCompare(b.timestamp));
> --- `packages/thalo/src/schema/registry.ts`

> for (const fieldName of alter.removeFields) {
>   schema.fields.delete(fieldName);
> }
> --- `packages/thalo/src/schema/registry.ts`

Admission is separate: a caller proposes retained schema text, filesystem/editor code admits it locally, and registry code applies it. [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring) retains the proposal/veto/recovery account. The resolver is not a human review mechanism or an expected semantic-answer oracle.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint)

Memory lineage: action selector captures current Git HEAD (or timestamp fallback captures current minute); the shipped script serializes that marker into an appended actualization entry only after receiving nonempty model text. The actualization's own timestamp records host wall-clock time, not the selected source cutoff. Storage is plain file metadata; form is symbolic control state, not synthesis rationale or raw execution trace. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo/src/services/change-tracker/git-tracker.ts`, `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`.

Read-back: latest actualization is chosen across all workspace files by target ID and greatest formatted timestamp; its `checkpoint` is parsed. A missing/unknown provider marker becomes null. Latest-entry ordering is string-based, whereas timestamp tracking compares parsed epoch values; timestamp normalization/equivalence across latest-entry candidates is not established by this bounded inspection. A malformed or misplaced newest record can alter later selection even without changing prose. SRC-1, `packages/thalo/src/services/synthesis.ts`, `packages/thalo/src/services/change-tracker/change-tracker.ts`.

> if (!latest || ts > latest.timestamp) {
> --- `packages/thalo/src/services/synthesis.ts`

The missing-checkpoint rule checks field presence, not faithful synthesis completion. Its misleading legacy code name still says `actualize-missing-updated`, but implementation requires `checkpoint`. SRC-1, `packages/thalo/src/checker/rules/actualize-missing-updated.ts`. [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection) identifies the actual behavioral force; operation remains unobserved.

#### On [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection)

Memory selection inputs: target IDs, retained source queries, latest target checkpoint and current workspace instances. Selected payload is current raw entry text plus metadata, not a before/after diff, deleted-entry tombstone or recursively dereferenced source document. Persistence resides in caller files and markers; actualize output is transient. Request direction is caller → selector → CLI/action, not autonomous background retrieval. No numeric entry/token budget is set by `runActualize`. SRC-1, `packages/thalo/src/commands/actualize.ts`, `packages/thalo/src/services/synthesis.ts`.

Git alternatives: entry identity/equality against a historical parsed file; rename-aware old path; or blame/ancestry when ignore-revs is available. Missing commits and timestamp-to-Git switches replay all current matches. Old parse failure treats current instances as changed. Timestamp alternative uses strict epoch cutoff, orders by time, and deduplicates by file/timestamp/entity/link, which can collapse distinct same-minute instances sharing these fields. Ordinary query instead deduplicates by physical position. These are alternative selector representations, not opaque provider memory. SRC-1, `packages/thalo/src/services/change-tracker/git-tracker.ts`, `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`, `packages/thalo/src/services/query.ts`.

> const key = `${model.file}:${timestampStr}:${entityType}:${linkId}`;
> --- `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`

Consumers only receive current query matches. Deleting a source entry, removing a matching tag, or editing the prompt/query without producing a qualifying changed instance can leave `isUpToDate` true. This limits automatic withdrawal and guidance invalidation. The optional `getChangedSchemaEntries` capability does not feed `runActualize`; the API's `filteredSince` path uses it separately. SRC-1, `packages/thalo/src/commands/actualize.ts`, `packages/thalo/src/api.ts`.

#### On [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

Working-context control: pending execution triggers code to build selected-entry text and read all existing target-file content. A new Agent is constructed per command process; no prior conversational turns are loaded by this script, no delegated frame return is implemented, and no host token trimming or summarization policy appears here. What escapes the model invocation is accumulated text deltas, admitted as Markdown. Provider/Pi-internal session processing is external and uninspected. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`; [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini).

The command-input fields for file provenance, timestamps, queries and previous checkpoint are not separately rendered into the model's entry block. Raw source can still contain timestamp/metadata and reasons. Neither a metadata display summary nor the symbolic checkpoint is a complete provenance ledger. Full current file inclusion also exposes retained prompts/metadata and unrelated content alongside prior prose, so selection is broader than the changed entries alone.

Raw-to-derived-to-later-consumer chain: caller-authored knowledge and prior file → model-generated Markdown → same file read during a later invocation. This is not established automatic learning from execution traces: console logs are operational reporting, while selected inputs are KB entries whose original experiential provenance is caller-dependent. Synthesis can curate content, but semantic change and improved future capacity are unobserved. Host admission enforces nonempty output and required fence/link/checkpoint structure, not truth, preserved rationale or claimed narrow-edit compliance.

#### On [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring)

Admission distinctions: init/formatter/merge are software transformations admitted by their filesystem writes; generic editor/agent callers have unresolved per-content human control. A human genuinely supplying/editing/reverting text is a separate possible admission decision, not implied by triggering an automated command. Structural diagnostics are not a universal veto. Existing files, schemas and prompts can be physically replaced, formatted or merged without model synthesis. Supplied source passages establish these writes and init skipping/force behavior.

Additional library write capability, SRC-1, `packages/thalo/src/vfs/persistence.ts`: optional expected content hash rejects mismatched content before writing. It does not adjudicate meaning and does not establish a transactional compare-and-swap or an action/Pi guard; the Pi script uses `writeFile` directly. The bounded caller search found exports and documentation but no production caller wiring this helper into those writers.

> if (actualRevision.token !== expectedRevision.token) {
>   throw new FileRevisionConflictError(resolvedPath, expectedRevision, actualRevision);
> }
> --- `packages/thalo/src/vfs/persistence.ts`

## Write side

**Acquisition and authoring.** Source-native entry sections can retain claims, reasons, caveats, summaries and links; the shipped skill asks collaborators to edit and check files. It does not authenticate a reference's source or capture agent traces automatically. Direct/external saves, initialization and software maintenance use the distinct controls in [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring). The initial authorship/admission of arbitrary KB text remains unresolved; known subsequent parser, registry and synthesis transformations remain established despite that uncertainty.

**Automatic transformation.** File load produces [MEM-CMP-workspace](#mem-cmp-workspace); schema resolution produces constraints through [MEM-RTE-schema-resolution](#mem-rte-schema-resolution); synthesis produces [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose) and appends [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint). Only the last two persist through the shipped model command. No separate rationale/evaluation record is demanded by that writer. Source reasons are delivered when present but generated reason retention is not guaranteed.

**Evaluation and rejection.** [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) emits transient structural diagnostics. Its caller can revise text; the action does not consume diagnostics as a commit gate. Pi failures/empty output stop its write; configured command failures stop later publication, not prior local writes. PR reviewers can reject base-branch adoption after branch publication. The action's PR body retains selected-entry titles, paths and timestamps as review metadata, not the complete model reasoning or a semantic evaluation. SRC-1, `packages/thalo-action/src/action.ts`; [RT-RTE-action-publication](runtime.md#rt-rte-action-publication).

**Cleanup and withdrawal.** Formatting changes presentation; merge can write conflict-bearing text; schema removal changes checking constraints. Caller edits/deletes or Git restoration can withdraw durable material, with recovery owned by the caller/Git. Selector filtering is not semantic retraction: an absent source can remain represented in old generated prose. Full file rewrite may incidentally remove claims or unrelated content, but that is not evidence-responsive withdrawal enforcement. Marker growth preserves actualization history inside the first block while later selection uses only the newest relevant entry. Reused library workspace loading can also retain undiscovered models unless another operation removes them. These limits are attached to the actual consumers above, not treated as system-wide absence of maintenance.

## Read-back

- **Requested source access:** [MEM-RTE-query-readout](#mem-rte-query-readout) supplies raw text only when the caller selects that channel. Metadata-only JSON/default output is a locator/display summary. API `query`, iteration and navigation afford external access; no additional deployed model reader is inferred.
- **Requested synthesis preparation:** [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection) consumes retained definitions and checkpoint control state, then emits selected raw instances. CLI stops at context output. The action triggers this request under its configured workflow and delivers stdin to the selected subprocess; that automation is not an independent relevance model or unsolicited memory injection.
- **Prior generated content:** [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) reloads the entire current file. This is the concrete later-model consumer of [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose), with interpretive influence rather than guaranteed obedience. No external reader of the finished guide is needed to establish this recurrent input path.
- **Symbolic retained control:** [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection) controls future context membership; [MEM-RTE-schema-resolution](#mem-rte-schema-resolution) changes later checker requirements. [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance) is the separate natural-language instruction path.
- **Alternative API selection:** `filteredSince` in SRC-1, `packages/thalo/src/api.ts` returns a filtered view: timestamp mode filters all entry classes by time; Git mode filters changed instances and optionally schemas, while synthesis and actualization entries remain visible. This affords a caller-specific read view rather than a hidden persistence route. It has no identified downstream generation caller in this analysis and must not inherit the action's wiring.
- **Editor/browser state:** supplied LSP evidence establishes buffer priority and disk reload on close. Browser snapshots pass current edited state to deterministic checks/query/actualize; reset discards it. Neither proves that an external agent saw or obeyed feedback, or that browser content survives sessions.

## Integration issues

1. **No correction to supplied runtime facts is required.** Its withdrawal, timestamp, first-fence rewrite, init-doc divergence and browser checkpoint limits remain supported. The memory-specific additions refine selection/provenance rather than contradict them.
2. **No same-referent duplicate is proposed.** New objects name retained entry/schema/query/prompt/prose/browser parts, whereas the closest supplied objects are static system guidance, transient command JSON and checkpoints. New component/route declarations state their comparisons. [MEM-OBJ-synthesis-prompt](#mem-obj-synthesis-prompt) and [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance) intentionally distinguish object from authority path; [MEM-RTE-schema-resolution](#mem-rte-schema-resolution) and [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) distinguish resolution from diagnosis.
3. **Withdrawal and guidance invalidation remain incomplete at the selector.** Evidence: current-instance iteration and changed-file restriction in SRC-1, `packages/thalo/src/services/change-tracker/git-tracker.ts`, pending condition in `packages/thalo/src/commands/actualize.ts`. Consequence: deletion, no-longer-matching entries and prompt/query-only edits do not establish a reliable resynthesis trigger. Relevant records: [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), [MEM-OBJ-synthesis-sources](#mem-obj-synthesis-sources), [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose).
4. **Reused loader removal is not guaranteed.** SRC-1, `packages/thalo/src/vfs/loader.ts` clones previous models and only adds/updates discovered files. [MEM-CMP-workspace](#mem-cmp-workspace) distinguishes this from a fresh action load and supplied editor deletion handling. Consequence: no universal reload-implies-withdrawal claim; full stale-state behavior of arbitrary consumers remains uninspected.
5. **API and persistence affordances need caller identity before stronger routing claims.** SRC-1, `packages/thalo/src/api.ts`, `packages/thalo/src/vfs/persistence.ts`. Changed-schema views and hash-guarded writes are real capabilities, but this analysis identifies no additional production model reader or use of the write guard by the shipped Pi path. Relevant [MEM-RTE-query-readout](#mem-rte-query-readout), [MEM-OBJ-schema-entries](#mem-obj-schema-entries), [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring). Consequence: do not classify them as deployed automatic delivery or universal conflict prevention.
6. **Rationale, trust and experiential origin remain content-dependent.** Source rationale is present in sample entries and sent as raw text; generated rationale, faithful source use and trace-fed improvement are unobserved. Relevant [MEM-OBJ-instance-entries](#mem-obj-instance-entries), [MEM-OBJ-synthesis-prose](#mem-obj-synthesis-prose), [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis). The intentionally nonsensical sample is a countercase to trusting entity/confidence labels as truth gates, not an observed bad model result.
7. **Context internals and operation remain external/unsupplied.** Relevant [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini), [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis). Fresh host construction and explicit input assembly are inspectable; provider eviction, actual retention, activation and benefit are not. No hidden compaction, training or self-improvement conclusion follows.

## Limitations and checks

Source/method identity: read the complete supplied invocation, member types, collection, worker rules and record contract; source HEAD equals the boundary pin, with clean checkout at inspection. Only authorized outputs and worker identity were written. No target execution, dependency installation, service call or experiment was performed. The provided runtime is provisional evidence and was challenged at selector invalidation, prior-file context, checkpoint authority and write-admission boundaries.

Limits: parser and all editor handler semantics, full merge/format correctness, all documentation/fixture provenance and arbitrary API caller behavior were not exhaustively inspected. No observed run establishes successful synthesis, model obedience, human acceptance, improved capacity or reliable semantic withdrawal. These gaps prevent stronger operation/benefit claims while preserving the inspected wiring.

Deterministic validation: the invocation-specific `commonplace-run validate-output` reported: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The content pass checks form and quotation occurrence, not analytical correctness or coordinator acceptance; identity was separately rechecked as stated above.
