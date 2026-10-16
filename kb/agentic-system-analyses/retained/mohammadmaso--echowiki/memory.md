---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "EchoWiki memory: persistent wiki synthesis, brief-selected rewriting, operator instructions and source/queue provenance limits."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
source-identity: "https://github.com/mohammadmaso/echowiki"
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
---

# EchoWiki memory report

## Boundary and evidence

EchoWiki retains Markdown knowledge for later compilation and human browsing. This report covers the shipped plugin, CLI/API, compiler, instructions, page/index/log writers, storage adapters and standalone file utilities at the boundary's frozen commit. All evidence below is SRC-1 implementation unless explicitly identified as doctrine/design. No compilation, target test, provider call or fixture was executed. HEAD matched the pin and checkout status was clean. The source register remains [boundary](boundary.md#source-register).

The compiler's meaningful cross-invocation context is prior concept/entity content, not a saved conversation. Raw notes/transcripts and audio, queue identifiers, editable instructions, summaries, catalog and operation log have different consumers. Provider parameters and host storage behavior remain opaque. Private vault contents, actual initial page authorship, deployed settings and operational outcomes are unavailable; these gaps prevent claims of successful preservation, factual accuracy, activated learning or measured benefit.

The following table distinguishes direct reads from supplied findings. All paths are commit-relative SRC-1 anchors. Direct inspection rechecked material compiler routes rather than treating the provisional runtime as an inspection limit.

| Surface / operation | Source paths and inspection | Records / limit |
|---|---|---|
| Manual, watcher, approval and note-copy admission | Direct: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/approval-modal.ts` | [RT-RTE-document-compile](runtime.md#rt-rte-document-compile), [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval), [MEM-OBJ-raw](#mem-obj-raw); approval is a path decision, not output review. |
| Audio/transcript acquisition | Direct plugin driver; supplied STT/device findings in runtime | [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest), [MEM-OBJ-raw](#mem-obj-raw); no audio/transcript supplied. |
| CLI and public library admission | Direct: `src/cli/compile.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts` | [RT-RTE-document-compile](runtime.md#rt-rte-document-compile); API caller provenance is unresolved, CLI bypasses watcher approval. |
| Instructions and settings reload | Direct: `src/wiki/schema.ts`, `templates/wiki/AGENTS.md`, plugin driver; supplied settings UI findings | [RT-OBJ-agents](runtime.md#rt-obj-agents), [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings); unknown actual installed instructions/settings. |
| Brief planning and selected body reload | Direct: `src/wiki/briefs.ts`, `src/wiki/compiler.ts`, `src/wiki/prompts.ts` | [MEM-RTE-retained-selection](#mem-rte-retained-selection); descriptions, bodies and source counts are distinct inputs. |
| Summary/concept/entity generation and admission | Direct: compiler, `src/wiki/llm.ts`, `src/wiki/page-writer.ts`, `src/wiki/wikilink.ts` | [MEM-OBJ-summaries](#mem-obj-summaries), [MEM-OBJ-concepts](#mem-obj-concepts), [MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-RTE-page-maintenance](#mem-rte-page-maintenance). |
| Catalog, links and operation trace | Direct: `src/wiki/index-writer.ts`, page writer, `README.md` | [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-log](#mem-obj-log); catalog is a browsing affordance, log is not model feedback. |
| Persistence implementation | Direct: `src/storage/node-storage.ts`, `obsidian-plugin/src/vault-storage.ts`, `src/wiki/frontmatter.ts` | Per-file writes, not whole-ingest transaction; external host durability uninspected. |
| Standalone reads/writes and page/image alternatives | Direct: `src/wiki/tools.ts`; caller search across `src/` and `obsidian-plugin/src/`; direct `src/llm/client.ts` | [MEM-OBJ-sources](#mem-obj-sources); utility capability does not establish a query agent or automatic admission. |
| Evaluation, cleanup and withdrawal | Direct reader/writer/driver inspection; scoped search for `delete`, `remove`, `log.md`, `test`, `lint`, helper calls and model tool registration; supplied boundary evaluation findings | [MEM-ABS-feedback-consumer](#mem-abs-feedback-consumer); queue removal is not knowledge withdrawal. No quality report/result or source invalidation path established. |
| Remote model state / releases | Supplied model and release records; direct chat client confirms messages-only call | [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model), [RT-CMP-stt-model](runtime.md#rt-cmp-stt-model), [RT-RTE-release-build](runtime.md#rt-rte-release-build); provider retention/training and installed release operation uninspected. |

## Core ideas

1. **A page description is the first-stage memory interface.** Every eligible concept/entity brief is enumerated for planning. Only model-selected update bodies are then loaded. There is no similarity index or enforced aggregate token budget. A fallback preview limits one body excerpt to 150 characters, not the total context. Entity source counts are selection context, not confidence scores ([MEM-RTE-retained-selection](#mem-rte-retained-selection)).
2. **Knowledge is rewritten, not accumulated as conversation history.** Each task gets explicit inputs in its own message array. Results escape to writers; sibling results do not enter generation context. Summary rewriting sees a target whitelist, not final generated page bodies. This resembles isolated task frames only in input/return isolation: no agent stack or reloadable conversation exists. Page files remain reachable through later compilation, whereas current-run planning/results are not saved checkpoints (SRC-1: `src/wiki/compiler.ts`; [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).
3. **Retention and source trust are not the same.** Writers record source pointers and descriptions, but no quality evaluator admits claims. The compiled `full_text` pointer does not prove a corresponding source copy was written. Preserving prior intent is a model instruction, not a diff/conflict invariant. Human approval applies upstream to a queued raw path, not to the generated assertions ([MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-sources](#mem-obj-sources), [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw notes, transcripts and audio

Identity: configured raw-folder text files and recorded audio. Text is natural-language source material, copied from a user note or returned by STT; audio is an opaque binary media payload here, not parametric memory or a readable text summary. Substrate: Obsidian vault files. Raw text is read in full by later manual/watcher compilation; audio goes to STT and remains a separate acquisition artifact, with no compiler audio read. External file authors and transcription accuracy are unresolved. The driver writes audio before requesting transcription and writes a transcript only after a successful request. User initiation does not establish per-transcript review. This is an object absent from the supplied declarations, overlapping the state handled by [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) and [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval), not those routes themselves. SRC-1: `obsidian-plugin/src/main.ts`; minimum acquisition passage is in the voice route.

#### MEM-OBJ-summaries
Label: Document summary pages

Identity: `summaries/<docName>.md`; natural-language model-derived Markdown bodies in WikiStorage. The initial summary derives from full current source and instructions; the final rewrite derives from that draft plus valid-target context. Links and headings then receive code edits. Human browsing is documented; prior summary bodies are not loaded into subsequent planning/generation in the inspected compiler. Summary filenames do contribute to later target whitelists. Whole-body replacement loses the prior draft; neither model reasoning nor change justification is separately retained. Distinct from [RT-OBJ-agents](runtime.md#rt-obj-agents); an output object handled by [RT-RTE-document-compile](runtime.md#rt-rte-document-compile), which declares no corresponding object. SRC-1: `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`.

> const parts = frontmatter.split(summary);
>   const body = (parts ? parts.body : summary).replace(/^\n+/, '');
> --- `src/wiki/page-writer.ts`

#### MEM-OBJ-concepts
Label: Concept page bodies

Identity: `concepts/<sanitized-name>.md` bodies. Form: natural-language Markdown, interpreted by models and humans; wikilink tokens additionally receive fixed code treatment. Substrate: WikiStorage. Authorship may be generated or externally edited; initial content provenance is unknown. Create generation uses current source/summary/instructions/targets; update adds prior body, not prior frontmatter. Later planning reads description/preview, and selected update generation reads the body. Replacement retains synthesis, not an obligatory reasoning trace. This object supplies the concept side of [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages); that record is an authority path, not a duplicate object. SRC-1: `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/page-writer.ts`.

#### MEM-OBJ-entities
Label: Entity page bodies

Identity: `entities/<sanitized-name>.md` bodies; natural-language Markdown in WikiStorage with the same model/human consumers as concepts. Named-entity type and source count provide additional planning context, separately classified below. Generated update body derives from old body and current source; entity create generation omits old body even when the writer discovers an existing filename and uses update metadata handling. Thus metadata preservation does not demonstrate semantic preservation. Distinct material object from [MEM-OBJ-concepts](#mem-obj-concepts); no supplied entity object exists, closest supplied authority path is [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages). SRC-1: `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`.

> const isUpdate = await storage.exists(entityPath(safe));
>     await writeEntity(storage, item.name, content, sourceFile, isUpdate, item.brief, item.type);
> --- `src/wiki/compiler.ts`

#### MEM-OBJ-page-metadata
Label: Page descriptions and lineage fields

Identity: code-managed frontmatter on summary/concept/entity files. Substrate: the same Markdown files, but operative parts differ from page prose. Description/legacy brief values are natural-language model output or externally authored text. `type`, `doc_type`, `full_text`, and `sources` are symbolic fields for parsing, identity and link lineage; entity type/source length become model-visible text. Concept/entity sources name summary files, not raw inputs. Summary `full_text` names a wiki source copy. These pointers do not retain derivation reasons or establish that referenced content exists. Writers preserve/update metadata conditionally and drop legacy `brief`; planning prefers description, then brief, then body preview. No supplied metadata object exists; this separates inputs hidden within [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages). SRC-1: `src/wiki/page-writer.ts`, `src/wiki/briefs.ts`, `src/wiki/frontmatter.ts`.

> fmLines.push(frontmatter.kvLine('full_text', `sources/${docName}.${ext}`));
> --- `src/wiki/page-writer.ts`

> const etype = String(fm.type ?? 'other').toLowerCase();
>     const sources = Array.isArray(fm.sources) ? fm.sources : [];
>     const suffix = brief ? ` — ${brief}` : '';
>     lines.push(`- ${file.slice(0, -3)} (${etype}, ${sources.length} sources)${suffix}`);
> --- `src/wiki/briefs.ts`

#### MEM-OBJ-index
Label: Knowledge base index

Identity: wiki-root `index.md`. Form: mixed natural-language descriptions and symbolic wikilinks/section structure; substrate WikiStorage. Code seeds it when missing, inserts document links, updates concept descriptions when supplied and replaces entity entries. Humans are the documented later consumer through Obsidian; code reloads the existing index to maintain it. Compiler target enumeration includes `index` but does not deliver its catalog body to the model. Document entries are not replaced when the same document link already exists, so displayed document descriptions can remain stale after recompilation. Distinct from [RT-OBJ-agents](runtime.md#rt-obj-agents); output of [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) with no supplied catalog object. SRC-1: `src/wiki/index-writer.ts`, `src/wiki/wikilink.ts`, `README.md`.

> if (!sectionContainsLink(lines, '## Documents', docLink)) {
> --- `src/wiki/index-writer.ts`

#### MEM-OBJ-log
Label: Operations log

Identity: wiki-root `log.md`; timestamped symbolic operation headers plus natural-language descriptions in WikiStorage. It is a coarse execution-status trace, not retained dialogue, source content, criticism or measured outcomes. The compiler appends an ingest description after its internal workflow returns, including fallback/skipped-page cases. No inspected compiler consumer reads it to guide future synthesis or retry. Human inspection is possible; actual use is unobserved. No supplied log object exists; closest record is [RT-RTE-document-compile](runtime.md#rt-rte-document-compile). SRC-1: `src/wiki/compiler.ts`, `src/wiki/index-writer.ts`.

> await appendLog(storage, 'ingest', `Compiled ${docName} from raw/`);
> --- `src/wiki/compiler.ts`

#### MEM-OBJ-sources
Label: Wiki source-copy and utility payload surface

Identity: schema-declared `sources/<docName>.md` or per-page JSON; helper-readable images, explorations and output files are additional utility payloads. Natural-language document/page content, symbolic page/image paths and opaque binary media are different encodings on the filesystem. Initial producer/admission is unresolved for externally supplied payloads. The shipped short compiler does not populate source copies, despite summary pointers and template descriptions. `getWikiPageContent` can select requested page numbers from JSON and render text/image-path summaries; `readWikiImage` can return base64 media. These are exposed storage capabilities, not established consumer routes. `writeWikiFile` can write any lexically root-confined wiki path; `writeKbFile` limits writes to wiki explorations or output. Neither utility imposes semantic approval; unspecified callers prevent a human-admission or query-agent conclusion. No counterpart object exists in supplied records; the closest supplied route [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) is not wired to these helpers. SRC-1: `src/wiki/tools.ts`, `src/wiki/schema.ts`, `templates/wiki/AGENTS.md`, `src/wiki/page-writer.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts`.

> const data = JSON.parse(fs.readFileSync(fullPath, 'utf-8')) as WikiPageEntry[];
>   const requested = new Set(parsePages(pages));
>   const matches = data.filter((entry) => entry.page !== undefined && requested.has(entry.page));
> --- `src/wiki/tools.ts`

### Routes

#### MEM-RTE-retained-selection
Label: Retained page selection and delivery

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This subroute begins on each compile: code enumerates concept/entity pages, builds briefs, submits planning context, then loads only selected update bodies for generation. The parent is a route because this is its read-back progression, not its output container. The planner chooses create/update/related names; code filters structural eligibility and checks existence for related names. Human input approval is upstream, not this selector's decision. No answer oracle or bounded experiment is used. Contextual source trust is model-mediated; no provenance quality ranking is computed. SRC-1: `src/wiki/briefs.ts`, `src/wiki/compiler.ts`, `src/wiki/prompts.ts`, `src/wiki/llm.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Brief strings, model plan, selected prior-body context and generated task results inside the current compiler invocation.
- Later read-back: Prior concept/entity descriptions or previews reach planning; selected update bodies reach rewriting across document invocations. Existing page names also enter the target whitelist.
- Delegated visibility: Provider receives all listed briefs plus full current source and draft summary; each update task receives its selected body without frontmatter, not other old bodies or sibling generated results.
- Selection predicate: Sorted immediate `.md` files in concepts/entities; description then brief then 150-character preview. Model plan selects updates; code sanitizes names and reads those paths, using a missing-page placeholder when necessary.
- Invalidation or expiry: Current file replacement/edit changes the next reload; no scheduled expiry. Current task context is not persisted as a reloadable conversation.
- Activation or effect: Context supply and task selection are wired; actual response dependence, preservation and improved synthesis remain unobserved.
- Evidence limits: No vault or model trace; no aggregate token budget, truncation result or empirical selection accuracy established.

> return body.trim().replace(/\n/g, ' ').slice(0, 150);
> --- `src/wiki/briefs.ts`

> const brief = resolveDescription(fm) || bodyPreview(text);
>     if (brief) {
>       lines.push(`- ${file.slice(0, -3)}: ${brief}`);
>     }
> --- `src/wiki/briefs.ts`

> const name = concept.name;
>     const title = concept.title ?? name;
>     const relativePath = conceptPath(sanitizeSlug(name));
>     let existingContent = '(page not found — create from scratch)';
>     const rawText = await storage.readText(relativePath);
>     if (rawText) {
>       const parts = frontmatter.split(rawText);
>       existingContent = parts ? parts.body.trim() : rawText;
>     }
> --- `src/wiki/compiler.ts`

The longer passage disambiguates identical concept/entity read snippets. Per-task arrays isolate work by code policy; full source and instructions remain in every task, selected old bodies are reloadable only through the page-selection path. The plan's reasoning is not requested or stored: the plan prompt requests no explanation (SRC-1: `src/wiki/prompts.ts`).

#### MEM-RTE-page-maintenance
Label: Page admission and link maintenance

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This is the parent's write-side subroute. Models propose content/descriptions and plan membership. Compiler code admits nonempty generation results, transforms links, and owns writes, metadata maintenance and reciprocal-link insertion. The user cannot veto each generated body here. Guidance is current source, stored instructions, selected prior prose and output prompts; operating mode is open ingestion, with no answer oracle. Physical writes are delegated to storage, not semantic admission. SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`, `src/wiki/wikilink.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Persistent summary/concept/entity content, links, catalog updates and eventual parent completion; thrown write failures can leave partial state.
- Later read-back: Admitted concept/entity descriptions and bodies feed the selection subroute; index/summary/links afford human browsing. Metadata also supplies entity counts and catalog maintenance.
- Delegated visibility: Model output passes through JSON extraction, frontmatter stripping and link filtering before storage. No independent critic or per-page approval receives a generated diff.
- Selection predicate: Structurally acceptable plan entries and nonempty page content; generation errors are skipped. Related pages must exist; known targets include planned names before generation succeeds.
- Invalidation or expiry: Full-body replacement invalidates prior prose without a retained checkpoint. Rejecting a pending path does not undo old wiki writes. No automatic source-withdrawal cascade is present in this subroute.
- Activation or effect: Code wires transformed outputs to retained files and later context. Actual knowledge preservation, graph integrity and downstream benefit remain unobserved.
- Evidence limits: No target execution; whitelist membership is not eventual target existence, and per-file storage is not whole-ingest atomicity.

> const { content } = stripGhostWikilinks(item.content, knownTargets);
>     pendingWrites[i] = { ...item, content };
> --- `src/wiki/compiler.ts`

> text += `\n\nSee also: ${link}`;
>   await frontmatter.atomicWriteText(storage, relativePath, text);
> --- `src/wiki/page-writer.ts`

Recovery is fallback summary on unparseable/empty plan, skip failed page tasks, fallback to draft if summary rewrite fails, and retry from current files after thrown failures. Malformed page JSON can be admitted as raw text, rather than rejected. Updating a concept preserves source metadata only through the update branch; entity writing uses actual existence. Neither branch retains a reasoned change record. Node temporary-file rename protects one write under filesystem assumptions; Vault modifies/creates through the host. These differ from semantic approval and do not supply rollback (SRC-1: `src/wiki/llm.ts`, `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`, `src/storage/node-storage.ts`, `obsidian-plugin/src/vault-storage.ts`; supporting malformed-output/writer passages are in [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)).

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-feedback-consumer
Label: Operation-log feedback consumer

- implementation conclusion status: absent

Bounded finding: the inspected shipped compiler/plugin/CLI loop does not read `log.md` as model context, derive guidance from logged outcomes, or use quality-report results to admit subsequent writes. Searched SRC-1 roots `src/` and `obsidian-plugin/src/` at the reviewed commit for `log.md`, `test`, `lint`, source helper names and model tool registration; direct compiler, client and index-writer reads identify only append behavior and connection probes. This supports a bounded absence of trace-fed guidance in this loop, not an absence of inaccessible provider learning or all possible external consumers. It does not deny that new source text is transformed into retained knowledge. No supplied absence record exists; the closest route [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) and boundary's evaluator limit agree with this scope. SRC-1: `src/wiki/compiler.ts`, `src/wiki/index-writer.ts`, `src/llm/client.ts`; the retained append passage is in [MEM-OBJ-log](#mem-obj-log).

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-agents](runtime.md#rt-obj-agents)

Storage text is natural-language operator-editable guidance, not compiler learned parameters. Its initial contents can be a manually installed template, another user-written file, or static fallback; actual provenance is unknown. Each compilation reloads stored instructions if non-null; even an empty stored file overrides fallback. Editing/adoption is an operator action; compiler loading supplies no semantic admission check. Runtime retains the relevant source quote. Trust force is a system-message request to the model, not enforced conflict detection. Reasons for operator changes are not retained by the compiler (SRC-1: `src/wiki/schema.ts`, `src/wiki/compiler.ts`, `templates/wiki/AGENTS.md`).

#### On [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue)

This is access/admission metadata, not derived knowledge. Saved path/timestamp entries reload on plugin load and populate the approval UI. Preview opens the current file; compilation rereads current text. Queue removal on rejection/success affects future admission display, not source persistence or knowledge invalidation. Failure leaves a path for retry rather than a generated-output checkpoint. No time-based expiry, content hash or frozen-body approval is supplied (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/approval-modal.ts`; runtime retains queue-write evidence).

#### On [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages)

The planning channel contains textual descriptions/legacy briefs/previews, plus entity types and source counts; the update channel contains body prose with frontmatter stripped. Those are different authority-bearing parts. The body does not receive system-role force. Prior descriptions can shape which page is selected without the planner seeing its full evidence. Body rewriting requests continuity, but create-on-existing-name is a counterexample to universal prior-body delivery. Summary bodies, log entries and index descriptions are not supplied as old knowledge bodies to these model calls (SRC-1: `src/wiki/briefs.ts`, `src/wiki/compiler.ts`, `src/wiki/prompts.ts`; [MEM-RTE-retained-selection](#mem-rte-retained-selection)).

## Write side

Raw acquisition is user note copying, external raw-file creation or user-initiated voice capture followed by service-proposed transcription. The driver does not approve transcript meaning. Watcher approval is a human path-admission option; direct manual/CLI/API routes do not use it. Caller-supplied API content has unresolved human control. These admission mechanisms are separate from file authorship and storage I/O ([MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval), [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest)).

Compilation transforms full source to draft summary, model plan and synthesized page content. Code removes generated frontmatter, manages lineage fields, replaces unknown wikilinks with readable text and adds navigation links. This is implemented content/link maintenance, not evidence of factual validation. No claim warrants treating raw input as an execution trace by origin: the system treats notes/transcripts as source text. The operation log is a retained trace, but its lack of an update consumer prevents a trace-fed learned-guidance conclusion ([MEM-RTE-page-maintenance](#mem-rte-page-maintenance), [MEM-ABS-feedback-consumer](#mem-abs-feedback-consumer)).

Rejection has several scopes: a human rejects a queued path; plan parsing/filtering drops or falls back; failed page tasks are skipped; the link stripper removes unrecognized link syntax. None guarantees removal of an unsupported assertion. Full replacement retains the new synthesis and symbolic source references, not the previous body or mandatory explanation of revision. A later model gets selected current content, not the reasons for adopting it. There are no alternative conversation checkpoints in the inspected compiler; retries regenerate from current inputs/files. The standalone utility writers are additional physical write capabilities with unspecified callers, not hidden per-content admission mechanisms ([MEM-OBJ-sources](#mem-obj-sources)).

## Read-back

The retained-page chain is request-driven by a new document compilation, with code enumeration followed by model-directed body selection. It is not independent unsolicited memory injection. The automatic watcher pushes a compile trigger into that chain; it does not independently select retained knowledge. Budget is only a per-page fallback preview and prompt-requested short descriptions, not an enforced total context limit. Full current input and selected bodies remain unbounded in these calls ([MEM-RTE-retained-selection](#mem-rte-retained-selection); SRC-1: `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/prompts.ts`).

The instruction chain loads operator-editable prose into system-role content; the queue chain loads identifiers into human approval UI; the catalog/summary/link chain affords human browsing. The documented human consumer is sufficient for an affordance, not evidence of actual reading:

> | Browse results | Open `wiki/index.md`, graph view on `wiki/`, follow `[[wikilinks]]` |
> --- `README.md`

Utility file/page/image reads establish storage capability only. A requested page-number selector has no observed or wired query caller here. Neither source-count metadata nor the log is an oracle of truth; source pointers remain available to humans but are not dereferenced for evidence checks by the compiler (SRC-1: `src/wiki/tools.ts`, `src/wiki/compiler.ts`; [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-sources](#mem-obj-sources)).

## Integration issues

- **Source-copy distinction:** schema/template descriptions and summary `full_text` metadata name wiki source copies, but the inspected short-document caller/compiler path does not write them. Do not integrate the declared layout as an implemented raw-to-source archival route. This is a qualification of boundary/runtime scope, not a contradiction of their source-grounded compilation account. Initial utility payload producer remains unresolved; therefore full evidence recovery through those pointers cannot be concluded ([MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-page-metadata](#mem-obj-page-metadata); SRC-1: `src/wiki/schema.ts`, `src/wiki/page-writer.ts`, `src/wiki/compiler.ts`, `src/compiler-api.ts`, `obsidian-plugin/src/main.ts`).
- **Entity/concept create asymmetry:** runtime's create-on-existing-name forcing case correctly identifies possible semantic replacement. Entity writes nevertheless use actual existence for metadata-update handling, whereas concept writes retain plan `isUpdate`. Integrate the semantic-loss warning without implying that both metadata paths discard old sources identically ([MEM-OBJ-entities](#mem-obj-entities), [MEM-RTE-page-maintenance](#mem-rte-page-maintenance), [RT-RTE-document-compile](runtime.md#rt-rte-document-compile); SRC-1: `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`).
- **Record overlap:** the two new routes are explicit subroutes of [RT-RTE-document-compile](runtime.md#rt-rte-document-compile), not replacement duplicates. New page/metadata objects distinguish the parts consumed by [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages); existing instructions/queue receive annotations rather than new IDs. No candidate duplicate referents remain after these comparisons.
- **Operational unknowns:** initial externally authored wiki/source content, actual human edits/approval, utility callers, provider state and host durability are unresolved. These prevent provenance, deployed admission, outcome and benefit conclusions, not the wired compiler read-back finding. Evidence and consequences are local to [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-sources](#mem-obj-sources), [MEM-RTE-retained-selection](#mem-rte-retained-selection), and runtime model/storage findings.

## Limitations and checks

The report establishes source-native retention and context wiring, not actual successful memory use. It distinguishes natural-language synthesis, symbolic access/lineage metadata and opaque media/provider state. Raw-to-derived content can shape later work; retained operational traces have no inspected guidance consumer. No broader learning, reflection or self-improvement benefit is inferred.

Source identity and full revision were rechecked against the supplied boundary and Git HEAD; checkout was clean. Method identity is the supplied invocation, member type and records/worker contracts, all read completely. No source IDs were added, no prior analyses or other run state were inspected, and no target execution occurred.

Validation: the invocation-specific deterministic output check passed; this establishes form and quotation occurrence, not semantic acceptance or demonstrated outcomes.
