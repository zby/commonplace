---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Antinomia memory report: human-admitted Markdown, symbolic feedback and dependency links, bounded model context and retained source lineage."
run-id: AAS-2026-11-08-antinomia-19694628edc2-01
source-identity: https://github.com/demartinogiuseppe/antinomia
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
---

# Antinomia memory report

## Boundary and evidence

The memory boundary is the shipped Obsidian plugin's retained notes, source hubs, dependency and dismissal metadata, settings, backups, debug retention and later consumers. It includes manual creation/import and maintenance, not only AI extraction. The source is SRC-1 at the boundary's frozen commit. Direct source inspection supplements the supplied runtime; neither supplies an observed target run. Provider weights, provider-side conversation/retention, Obsidian implementation, actual user vault contents and human decisions are outside the frozen evidence. These limits prevent durability, semantic accuracy, actual adoption and improvement claims.

Direct reads covered `core/templates.ts`, `core/types.ts`, `core/settings.ts`, `core/frontmatter.ts`, `flows/hunter.ts`, `flows/elevation.ts`, `flows/presuppositionMap.ts`, `flows/presupposti.ts`, and `modals/MapPresuppostiModal.ts`; bounded passages covered dispatch, settings and persistence/maintenance in `main.ts`, PDF/YouTube ingestion, free input, title proposal, example evaluation and retained-state view consumers. These are SRC-1 implementation evidence; template guidance and the example measurement key also provide doctrine/design. Runtime-supplied findings remain explicitly identified below. Available but uninspected bodies are not access gaps.

| Entry or operation | Source path; inspection basis | Coverage and conclusion limit |
|---|---|---|
| Guided/empty creation, free text/clipboard | `main.ts`, `flows/freeInput.ts`, `core/templates.ts`; direct dispatch/templates plus supplied runtime | [RT-RTE-free-input](runtime.md#rt-rte-free-input), [MEM-OBJ-note-content](#mem-obj-note-content); empty creation bypasses AI review. No actual content fidelity established. |
| PDF attachment/import, extraction, hub and concepts | `flows/pdfIngest.ts`; direct extraction/helper/hub/driver passages plus runtime | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-source-hubs](#mem-obj-source-hubs); PDF text has a cap, binary remains separately accessible. PDF engine internals excluded. |
| YouTube quick and concept ingestion | `flows/youtubeFetch.ts`; direct hub/cap/write searches and hub body, supplied runtime for quick/fetch flow | Same ingest route; retained transcript differs from model input. Fetch implementation and real transcript fidelity unobserved. |
| Ordinary/focused Hunter, raw failure retention | `flows/hunter.ts`, `core/settings.ts`; direct full flow/defaults | [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), [MEM-OBJ-hunter-raw](#mem-obj-hunter-raw); no semantic validation or complete examination guarantee. |
| Dismiss/undismiss and retained pair list | `flows/hunter.ts`, `views/DismissedPairsView.ts`; direct | [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal), [MEM-OBJ-hunter-feedback](#mem-obj-hunter-feedback); symbolic suppression, not model learning. |
| Split/transform elevation | `flows/elevation.ts`; direct full flow, supplied modal findings | [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); separate origin-pointer and embedded-origin forms. |
| Principle U-note creation/linking, undermining, deletion | `flows/presuppositionMap.ts`, `main.ts`; direct | [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission), [MEM-OBJ-presupposition](#mem-obj-presupposition), [MEM-OBJ-note-metadata](#mem-obj-note-metadata); deletion hook is filename-prefix limited. |
| Older tension A/B assumptions | `flows/presupposti.ts`, `modals/MapPresuppostiModal.ts`; direct full files | [MEM-RTE-inline-assumptions](#mem-rte-inline-assumptions); distinct from U-note dependencies. |
| Classify, manual type/ignore, title and generic linking | `main.ts`, `flows/titleProposal.ts`; direct methods/proposal driver | [MEM-RTE-note-maintenance](#mem-rte-note-maintenance); human UI admission is separate from software persistence. |
| Resolve/archive, retroactive origins, orphan origin, merge | `main.ts`; direct methods and registered commands | Same maintenance route; merge redirects references but does not copy removed body. |
| Schema migration and restore | `flows/migration.ts`; direct migration/restore passages, supplied runtime for modal admission | [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration), [MEM-OBJ-migration-backup](#mem-obj-migration-backup); no transactional or host-durability conclusion. |
| Graph, assumptions map, audit, dashboard, typed/unclassified lists | `views/AntinomiaGraphView.ts`, `views/PresuppositionsMapView.ts`, `views/AuditVaultView.ts`, `views/DashboardView.ts`, `views/UnclassifiedNotesView.ts`; direct bounded reads/searches; typed-list rendering supplied by boundary | [MEM-RTE-retained-inspection](#mem-rte-retained-inspection); detailed typed-list rendering and all interactive graph handlers not exhaustively inspected. No complete display-correctness claim. |
| Settings load/save, profile/context controls, last-run summary | `main.ts`, `core/settings.ts`, `views/DashboardView.ts`; direct | [MEM-OBJ-plugin-settings](#mem-obj-plugin-settings); external provider retained state unresolved, not inferred absent. |
| Example admission, key and deletion | `main.ts`, `flows/exampleVault.ts`; direct command and measurement/deletion passages | [MEM-CLM-evaluation-key](#mem-clm-evaluation-key); human-readable reference outcomes, not an automatic adaptation loop. |
| Model request, cancellation, acceptance friction | `ai/callAI.ts`, `modals/FrictionCard.ts` and consumers; supplied runtime only | [RT-RTE-model-request](runtime.md#rt-rte-model-request), [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope); no independent source re-audit of transport or gate wiring here. |

No CLI, model tools or worker context is established by these dispatch paths: they are Obsidian commands calling returning model computations, per the supplied runtime. This is not a global host security claim. Static shipped prompts are instructions reused across calls, not material accumulated through use.

## Core ideas

1. **Retained text and retained control data have different consumers.** Tension/substrate bodies reach Hunter as prefixes; type/status gates eligibility; dismissals never need to reach the model to suppress output. U-note titles, rather than U-note bodies, reach later assumption proposals. The same vault therefore supports model interpretation, deterministic filtering and human inspection without granting every part the same authority ([MEM-OBJ-note-content](#mem-obj-note-content), [MEM-OBJ-note-metadata](#mem-obj-note-metadata), [MEM-OBJ-hunter-feedback](#mem-obj-hunter-feedback)).
2. **Admission is interactive, not a truth certificate.** Models propose extracted concepts, rules and assumptions. Humans can edit or reject through the shipped interfaces; software sanitization and structural checks precede writes. Manual/empty notes and batch maintenance use other admission mechanisms. Starting an operation is not scrutiny of every generated sentence ([RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-RTE-note-maintenance](#mem-rte-note-maintenance)).
3. **Context control is selection by value, not conversational compaction.** Hunter selects by type/status, recency, cap and optional focus, then strips frontmatter and truncates bodies. Removed material stays in vault files, not a resumable model frame. Source extraction similarly bounds input without feeding every retained source character to the model. There is no subagent frame/return boundary in these routes; only explicit request messages and a returning result ([RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).
4. **Lineage is retained unevenly.** Elevation transform embeds the old body, split points to a defeated original, PDF hubs point to the binary, and YouTube hubs retain a near-original transcript. These support revisiting origins but do not prove that later model consumers receive or verify the underlying evidence ([MEM-OBJ-source-hubs](#mem-obj-source-hubs), annotations on rule admission).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-note-content
Label: Tension substrate and principle prose

Source-native identity: tension A/B prose, substrate Content/Original slots, principle IF branches and GREY ZONE. Representational form: natural language, including conditionals interpreted by models or humans, not executed by a rule engine. Storage substrate: Markdown bodies in the Obsidian vault. This is distinct from runtime routes admitting/consuming it, closest [RT-RTE-free-input](runtime.md#rt-rte-free-input), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); no supplied object counterpart.

Lineage varies: manual text; model-extracted free input or source concepts followed by review; optional model rule proposal followed by editable elevation. A substrate's source-native description as raw material does not establish literal source quotation: concept extraction is derived prose. Tension templates provide Original slots but do not automatically fill them with the initial input. Principle transform retains the old body; split retains an origin pointer to the original now defeated. Defeated text is historical material, not an automatic prohibition on future human use. Later consumers: Hunter for eligible tension/substrate prefixes; mapping for principle body; editor and UI for humans. Principle rules have interpretive authority at the mapping model, not executable policy authority over plugin operations. Evidence: SRC-1, `core/templates.ts`, `flows/freeInput.ts`, `flows/elevation.ts`, `flows/pdfIngest.ts`, `flows/hunter.ts`.

> - **Content (base):** ${c}
> - **Original:**
> --- `core/templates.ts`

> const oldBody = stripFrontmatter(raw).trim();
> --- `flows/elevation.ts`

#### MEM-OBJ-presupposition
Label: Presupposition text and confidence

Source-native identity: U-note assumption sentence and confidence field. Storage: vault Markdown body plus frontmatter. Form: the assumption and model confidence labels are natural-language assertions; confidence is displayed metadata, not an independently calibrated probability. Distinct object from its admitting route [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission); no supplied object counterpart. Links and status are separated in [MEM-OBJ-note-metadata](#mem-obj-note-metadata).

Lineage: reviewed model proposal or user-edited sentence; a link decision reuses an existing note rather than regenerating its body. Template adds a request to describe conditions/counterexamples/sources, not evidence they were supplied. Mapping gathers every U-note's human title/basename with an empty snippet, not its body or status-qualified truth assessment. Thus future dedup context can include an undermined assumption's title. Human readers can inspect full notes; automatic dependency lookup uses links rather than testing the assertion. Evidence: SRC-1, `core/templates.ts`, `flows/presuppositionMap.ts`.

> snippet: "",
> --- `flows/presuppositionMap.ts`

> > Describe when this assumption holds, counter-examples, and sources.
> --- `core/templates.ts`

#### MEM-OBJ-note-metadata
Label: Typed note state and dependency addresses

Source-native identity: `antinomia_type`, status, title, dates, source/origin fields, `links`, `origin_tension`, `replaced_by`, `presupposes`, `presupposes_of`, ignore flag; excludes Hunter feedback. Storage: YAML frontmatter in Markdown, subsequently exposed through Obsidian metadata cache. Symbolic operative parts are types/status, links and identity strings interpreted by fixed selectors; title/source labels are readable metadata, not the body or verified provenance. Wikilink aliases display titles while basenames remain addresses. Confidence content is separately described in [MEM-OBJ-presupposition](#mem-obj-presupposition).

Closest supplied records are [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan); distinct retained data, not duplicate routes. Lineage includes manual editing, approved classification, templates, deterministic link union, user undermining and maintenance. Cache is an access substrate, not a separately authored knowledge store. Consumers include Hunter eligibility, graph node/edge assembly, impact lookup and title/list rendering. Two-direction union supports dependency discovery but not logical entailment or automatic principle withdrawal. Basename identity can collide across folders; newly created title mapping compensates locally for cache lag, not globally atomic consistency. Evidence: SRC-1, `core/frontmatter.ts`, `core/types.ts`, `main.ts`, `flows/presuppositionMap.ts`, `views/AntinomiaGraphView.ts`.

> const prev = basenamesFromFrontmatter(fm.presupposes_of);
> fm.presupposes_of = toWikilinks(mergeUnique(prev, [principleBasename]), titleMap);
> --- `flows/presuppositionMap.ts`

> return app.metadataCache.getFileCache(file)?.frontmatter;
> --- `core/frontmatter.ts`

#### MEM-OBJ-hunter-feedback
Label: Hunter false positive entries

Source-native identity: `hunter_false_positives` arrays of peer basenames. Representational form: symbolic exact-pair exclusions. Storage: note YAML; a transient set of sorted pair keys is reconstructed on later Hunter calls. Human dismissal authors the judgment; code admits/idempotently stores it on both available notes. No reason, cited counterevidence or revised instruction is stored in the array. This is distinct data underlying [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal) and [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter), not another route or authority record.

Consumer authority: deterministic post-model output exclusion, not removal from model input or a parameter update. Explicit undismiss reverses retained exclusion. Dismissed-pairs UI scans all notes' arrays and may display both mirrored entries; its comment about one alphabetically smaller owner does not describe the two-sided writer. Later suppression requires selected-note metadata to supply the key. Evidence and minimum filter passage are already retained in the cited runtime records; additional SRC-1 path: `views/DismissedPairsView.ts`.

> pairs.push({
>   ownerFile: f,
>   ownerBasename: f.basename,
>   otherBasename: other,
> });
> --- `views/DismissedPairsView.ts`

#### MEM-OBJ-source-hubs
Label: PDF and YouTube source hubs

Source-native identity: H-source meta_notes and their source materials. Separate operative parts: (a) natural-language extracted concept bodies in substrates, covered by [MEM-OBJ-note-content](#mem-obj-note-content); (b) symbolic hub/source addresses and concept wikilinks; (c) readable PDF reference, with the PDF binary separate in the vault; (d) natural-language YouTube transcript embedded under Transcript. Markdown hub storage and PDF binary attachment storage are distinct. No supplied object counterpart; closest route [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

Code creates/updates hubs after human batch selection; physical vault writes do not constitute another per-hub human review. PDF hub contains concept links and original-file link, not a stored full extracted-text transcript. YouTube concept hub includes the full supplied transcript after line-start `---` substitution, even though only the first 30,000 characters enter extraction. Therefore the source comment's “verbatim” description is not byte-for-byte retention. Initial provenance is automatic fetch or user paste; neither authenticates the video's actual speech. Hub overwrite replaces its listing/transcript rather than preserving an append-only source history. Actual consumers are human navigation and graph links; Hunter selects substrates, not meta_note hubs, and does not automatically follow provenance links. Retention permits manual source checking, not an automatic source-grounding guarantee. Evidence: SRC-1, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts`, `flows/hunter.ts`.

> const safeTranscript = transcript.replace(/^---/gm, "———");
> --- `flows/youtubeFetch.ts`

> const aiInput =
>     text.length > YT_AI_INPUT_CAP_CHARS ? text.slice(0, YT_AI_INPUT_CAP_CHARS) : text;
> --- `flows/youtubeFetch.ts`

#### MEM-OBJ-plugin-settings
Label: Plugin settings and run summary

Source-native identity: settings object with profiles, active/Hunter profile IDs, selection caps, onboarding/hint flags, friction/elevation modes and last-Hunter timestamp/count. Form: symbolic configuration and event/access metadata, not a retained contradiction explanation. Storage: plugin `saveData`/`loadData` through external Obsidian storage; exact host file/durability not established. No supplied object counterpart; closest [RT-CMP-model](runtime.md#rt-cmp-model) and [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan).

Lineage/admission: human settings edits supply routing/context choices; software supplies defaults, migrates old settings and automatically updates progress flags and last-run summary. These are different admission mechanisms from human content review. Later startup reloads settings; subsequent Hunter selection consumes caps, model dispatch consumes profiles, dashboard displays timestamp/count and onboarding consumes flags. Summary metrics are raw run metadata, not a trace-derived behavioral rule. No inspected consumer derives revised prompts or selection policy from detection success. Provider weight state/provenance remains outside the source; see configured model record rather than treating config strings as pinned weights. Evidence: SRC-1, `core/settings.ts`, `main.ts`, `flows/hunter.ts`, `views/DashboardView.ts`.

> await this.saveData(this.settings);
> --- `main.ts`

> plugin.settings.lastHunterRunISO = meta.timestamp;
> plugin.settings.lastHunterRunCount = filtered.length;
> --- `flows/hunter.ts`

#### MEM-OBJ-migration-backup
Label: Pre migration note copies

Source-native identity: timestamped pre-migration backup tree. Storage: vault adapter files retaining complete original Markdown strings, including natural-language bodies and symbolic frontmatter. These parts retain their original form, not an opaque learned representation. No supplied object counterpart; closest [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration). Software chooses legacy files after user migration confirmation and copies them before mutation; human did not individually approve each backup string. Explicit restore reloads the latest backup and overwrites or recreates original paths. This is recovery read-back, not model memory retrieval; later note selectors can then see the restored content. No automatic expiry, archival semantics or protection against overwriting unrelated later edits is established by these functions. Evidence: SRC-1, `flows/migration.ts`; supplied runtime retains backup-before-loop passage.

> const content = await adapter.read(backupFile);
> const existing = app.vault.getAbstractFileByPath(original);
> if (existing instanceof TFile) {
>   await app.vault.modify(existing, content);
> --- `flows/migration.ts`

#### MEM-OBJ-hunter-raw
Label: Hunter raw response debug note

Source-native identity: optional `HUNTER-RAW` note from the parse-failure modal action. Storage: vault Markdown with natural-language/raw structured response rendered in a code block, plus profile and response length. The raw content is not an admitted typed substrate and is not a derived general lesson. Distinct object from [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan). Code exposes a save action only after failure; human clicking admits retention, code writes the raw response. Intended later consumer is the human editor/debug reader opened by `createNote`; no automatic Hunter re-ingestion follows from this untyped note. Console/error-modal excerpts are separate transient diagnostics. Free-input raw-response rescue can instead admit a typed substrate, per [RT-RTE-free-input](runtime.md#rt-rte-free-input), so not all raw-output retention has the same eligibility. Evidence: SRC-1, `flows/hunter.ts`, `main.ts`.

> label: "Open raw response",
> --- `flows/hunter.ts`

### Routes

#### MEM-RTE-inline-assumptions
Label: Tension inline assumptions

Distinct from [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission): this changes two fields inside a tension rather than creating U-notes and graph dependencies. User command opens the prefilled modal; code prefers existing frontmatter A/B then falls back to body markers. Optional model proposal receives the stripped tension body under `PRESUPPOSTI_SYSTEM`, fills editable fields, and human Apply admits the fields or Cancel vetoes. Software writes nonempty A/B to frontmatter and replaces/appends body lines. Empty input does not clear an existing field. Owner of proposal is model, of decision human, of sequencing/write code/host. Open request, no answer oracle, no automatic test or rollback. Guidance asks for epistemic/value assumptions; retained result is assertions, not a tested explanation or full model rationale. Evidence: SRC-1, `flows/presupposti.ts`, `modals/MapPresuppostiModal.ts`.

- Immediate return: Editable modal then write notice/error.
- Later read-back: Subsequent modal opening reloads stored A/B; later Hunter may receive body copies within its prefix budget.
- Delegated visibility: Model sees current tension body; no worker or global assumption store is supplied.
- Selection predicate: Tension type; frontmatter preference over body fallback; apply only nonempty edited fields.
- Invalidation or expiry: Replacement overwrites old field text; blank submissions leave it, with no automatic expiry.
- Activation or effect: Writes assertion text and modified date; semantic adoption and criticism unobserved.
- Evidence limits: No model-run or human-scrutiny evidence; redundant body/frontmatter writes are sequential.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (a) fm.presupposizioniA = a;
> if (b) fm.presupposizioniB = b;
> --- `flows/presupposti.ts`

#### MEM-RTE-note-maintenance
Label: Human directed note maintenance

Distinct from the AI admission and schema migration routes: user commands/views select manual type/ignore, title edit, generic links, resolve/archive, origin repair or merge. No counterpart route in supplied runtime covers this full maintenance group; overlap with [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) is origin data, not the elevation operation. Human chooses commands/targets and can veto modals/pickers; optional model title/classification proposes content under static task prompts. Classification requires parsed type plus motivation and valid enum before confirmation. Admitted type does not necessarily receive manual markAsType defaults: classification writes type/date only. Resolve directly writes resolved; archive collects motive/replacement. Generic linking updates both frontmatters and an active-note body marker.

Retroactive origin migration reads an Italian `## Origine (tensione)` heading despite its English comment; it is not a universal extractor of the current `## Origin (tension)` template. Orphan repair creates a placeholder defeated, not a reconstructed verified history. Merge redirects principle references, appends a merge marker to the kept file and trashes the other without copying its body. These controls admit metadata/content changes under user action and deterministic transformations, not an oracle or automatic improvement experiment. Sequential writes have no common rollback; trash/recovery depends on host. Evidence: SRC-1, `main.ts`, `flows/titleProposal.ts`.

- Immediate return: Review interface or write/trash notice, with errors caught on selected paths.
- Later read-back: New types/status affect selectors; titles affect display and mapping context; origin/replacement/links affect navigation and graph.
- Delegated visibility: Optional title/classification model receives note text; manual actions invoke no model.
- Selection predicate: Active note or picker; command type guards, classification enum validation, origin matching and exact/substring link checks differ by operation.
- Invalidation or expiry: Explicit overwrite/removal/status changes, merge trash; no automatic expiration or universal undo.
- Activation or effect: Deterministic retained-state changes, including removal from open-Hunter eligibility on resolution/archiving; correctness of history and decisions not established.
- Evidence limits: Does not audit all host editor writes; origin migration and merge are limited transforms, not semantic consolidation guarantees.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fm.status = "resolved";
> --- `main.ts`

> await this.app.fileManager.trashFile(removeFile);
> --- `main.ts`

#### MEM-RTE-retained-inspection
Label: Retained note inspection

Distinct from model read-back [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) and admission [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission): consumers are human-facing views. Opening views and host events trigger code to reload metadata and assemble summaries. Graph selects typed/visible layers and constructs edges from origin/replacement/links/presupposes and cached body wikilinks. Presuppositions Map displays title/status/confidence and dependent principle count from either link direction; its optional load-bearing filter is degree >1, not an evidence test. Audit caches full typed note text keyed by path/mtime and checks particular marker patterns; dashboard reads type/status and last-run summary. Typed lists and editor navigation provide additional human access as stated by boundary; detailed list rendering is not independently audited here. Evidence: SRC-1, `views/AntinomiaGraphView.ts`, `views/PresuppositionsMapView.ts`, `views/AuditVaultView.ts`, `views/DashboardView.ts`, `core/frontmatter.ts`.

- Immediate return: Graph/cards/counts/issues/links to the human; editor opening makes the full file reachable.
- Later read-back: Persisted note content and metadata feed later view openings/event refresh; display caches are reconstructible, not a learned store.
- Delegated visibility: Human receives selected labels, relationship summaries and linked files; no automatic delivery to another agent context.
- Selection predicate: Type/status/layer and view filters; dependency count; audit's explicit marker predicates; dashboard recency selection.
- Invalidation or expiry: View refresh after subscribed host events, graph refresh calls and path/mtime cache keys; host timing guarantees uninspected.
- Activation or effect: Presentation and opportunity for human action; display does not automatically revise rules or prove user reliance.
- Evidence limits: Degree is structural dependency, not logical proof; audit markers are incomplete and actual UI correctness is unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (this.loadBearingOnly) rows = rows.filter((r) => r.degree > 1);
> --- `views/PresuppositionsMapView.ts`

> const key = files.map((f) => f.path + ":" + f.stat.mtime).join("|");
> --- `views/AuditVaultView.ts`

### Claims

#### MEM-CLM-evaluation-key
Label: Seeded Hunter evaluation key

Claimed operation: example vault provides named sharp/medium/subtle contradictions, noise and expected confidence ordering, with a human-readable measurement key. This supplies a potential human answer oracle for a seeded exercise, not an oracle consulted by production Hunter or an automatic update consumer. User confirms example creation; code authors seeded notes/key; user separately confirms deleting example-marked notes. Later Hunter can consume eligible examples exactly like other typed notes, with ordinary cap/truncation limits. The key's instruction that a missed subtle case is a model limit does not causally isolate the model from selection, prompts or budgets. No retained evaluation result or adaptation is supplied. Distinct from [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan); no counterpart claim in runtime. Evidence: SRC-1 doctrine/design and implementation, `flows/exampleVault.ts`, `main.ts`.

> - **False positives on noise**: zero is ideal.
> --- `flows/exampleVault.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-dependency-display
Label: Dependency display authority

Consumer: dependency lookup, graph and human reviewing collapse impact. Channel: cached `presupposes`/`presupposes_of` → dependent principle set/count → view/modal. Force: symbolic relationship inclusion and displayed structural warning, not automatic logical invalidation of the principle. Horizon: later lookups while addresses/metadata persist. Distinct from [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter), which suppresses model output; closest [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission) supplies the writer. Evidence: SRC-1, `flows/presuppositionMap.ts`, `views/PresuppositionsMapView.ts`.

> wanted.has(f.basename) ||
> basenamesFromFrontmatter(ffm.presupposes).includes(presupFile.basename)
> --- `flows/presuppositionMap.ts`

## Annotations

#### On [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan)

Memory selector is a user-requested batch followed by automatic selection, not unsolicited push. Defaults 20 notes and 800 characters per body are configurable; recency is modification time, not semantic retrieval. Frontmatter type labels and basenames cross to model; most frontmatter, source hubs, excluded files and body suffixes do not. Focus forces the target first and fills remaining slots. Body suffixes remain manually reachable by reopening files or new requests; there is no model-call tool to follow a pointer and fetch omitted text. A fresh call reloads files, not a conversational summary. Newest-modified sorting can be affected by maintenance writes, not just new knowledge. Direct confirmation: SRC-1, `flows/hunter.ts`, `core/settings.ts`; the runtime retains truncation/filter passages.

#### On [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Two checkpoint forms matter. Transform embeds the old tension body in the new principle; split creates the rule and links the defeated original, leaving only a pointer/placeholder in the principle's Origin section. Later principle mapping strips frontmatter and supplies the whole remaining body: transform's embedded origin reaches that call, whereas split's original body is not automatically dereferenced. Thus retaining reasons somewhere in the vault differs from delivering them to the next model. Origin text itself is not necessarily a reasoned justification. Direct evidence: SRC-1, `flows/elevation.ts`, `flows/presuppositionMap.ts`.

> "\n## Origin (tension)\n\n" +
> `> Derived from: [[${originBasename}]]\n\n` +
> oldBody +
> "\n";
> --- `flows/elevation.ts`

#### On [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission)

Read-back is human-requested mapping followed by code-built context: full stripped principle body plus all existing U-note basenames/human titles, with no explicit character cap in this builder. No semantic nearest-neighbor lookup, embedding store or body-based dedup is established here. Existing-note title selection ignores active/undermined status. Code unions addresses and creates missing notes, but that transformation neither derives a new criticism nor stores a separate warrant. The title/snippet distinction is verified directly in SRC-1, `flows/presuppositionMap.ts`; [MEM-OBJ-presupposition](#mem-obj-presupposition) retains the empty-snippet passage.

#### On [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal)

This is durable human feedback from the displayed result into a later deterministic filter. It does not automatically transform accumulated traces into an instruction or derived theory. The stored exclusion loses the user's reason and the rejected description; the later filter reads only identity keys. It can change returned suggestions across sessions without improving the model or testing a general hypothesis. Direct evidence SRC-1, `flows/hunter.ts`; [MEM-OBJ-hunter-feedback](#mem-obj-hunter-feedback) describes retained parts.

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Source-to-derived-to-consumer chain is PDF binary/transcript → bounded extraction input → sanitized model concepts → human batch picks → substrate Markdown → conditional later Hunter prefix. Hubs preserve provenance separately, not an automatically reloaded evidence attachment. Sanitization trims title/content, caps titles at 120 characters and rejects empty fields; it does not check source entailment. PDF text input cap is 30,000 characters with user truncation confirmation; YouTube concept input is independently capped while full transformed transcript stays in hub. Helpers themselves accept caller-supplied strings, so driver caps are not a universal transport cap. Direct evidence SRC-1, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts`; supplied runtime retains cap passages.

## Write side

The records distinguish admission from authorship and I/O. Manual/empty creation admits user text/placeholders on command or modal submission. Free input admits edited extracted fields, not necessarily the raw original. Concept ingestion admits selected concepts in bulk; code additionally writes/rewrites hubs and links. Optional title, classification, elevation and inline-assumption calls propose rather than commit; their interfaces admit the result. Principle assumption review admits new/link decisions, and deterministic union creates graph addresses. High friction is only the local gate scope established in [RT-CLM-friction-scope](runtime.md#rt-clm-friction-scope), not a universal admission invariant.

Curation is implemented through extraction/field conversion, user editing, body replacement, schema translation, link union, lifecycle status and explicit trash. Those operations can change retained meaning but do not establish warrant. [MEM-RTE-note-maintenance](#mem-rte-note-maintenance) names counterexamples to historical-preservation claims: placeholder origins and merge without body copy. [RT-RTE-schema-migration](runtime.md#rt-rte-schema-migration) has a backup/restore route, not a general rollback for all note transformations.

Rejection has different retained consequences. Cancel/skip in admission modals can discard proposals or create blank templates; malformed Hunter responses remain transient unless the user chooses raw retention. Dismissal instead keeps an exclusion used later. Resolve/archive removes ordinary open-tension eligibility while retaining text. Marking U undermined changes its status/display, not principle content; the direct delete hook only cleans when an `.md` filename starts `U-`, so arbitrary renamed U-note deletion is not covered by that hook (SRC-1, `main.ts`, `flows/presuppositionMap.ts`). Examples are explicitly trashable by their marker ([MEM-CLM-evaluation-key](#mem-clm-evaluation-key)).

No qualifying automatic trace-fed knowledge/instruction rewrite is established by these inspected paths. Raw diagnostics and timestamp/count summaries are traces/access metadata; concept extraction transforms source input, not the plugin's own operational experience. Human pair rejection yields a specific symbolic exclusion, not a model-generated lesson. These bounded findings do not establish absence of learning by people or opaque providers, nor improved future capacity. Source origin for each transformation is kept local in its object/route rather than inferred from an AI label.

## Read-back

Concrete later model consumers are Hunter, principle mapping, optional elevation, inline assumption proposal, title proposal and classification of existing notes. Hunter receives bounded body prefixes; principle/inline mapping receive stripped bodies; direct title and classification drivers receive raw existing-note text (including frontmatter), not the Hunter projection. The former routes' input limits therefore cannot be generalized to all outbound requests (SRC-1, `flows/hunter.ts`, `flows/presuppositionMap.ts`, `modals/MapPresuppostiModal.ts`, `flows/elevation.ts`, `flows/titleProposal.ts`, `main.ts`; route citations above).

Selection direction is user request → software selection/assembly → backend input. Dismissals travel a separate user feedback → note metadata → later output filter path, not backend context. Human-facing views can refresh automatically on host events after opening, but that is UI refresh rather than unsolicited injection into an agent invocation. Explicit restore is another read-back direction: backup → original note path → ordinary later consumers. None of these imply exercised semantic reliance merely because content is delivered.

Working-context control here resembles copying selected values from a larger external store, not pushing and popping child-agent stack frames. There is no delegated reasoning frame with a summary escaping. Hunter and ingestion leave full originals externally accessible while omitting/truncating values in a particular request. No automatic conversational compaction, tail retention or summary checkpoint is established in the supplied runtime or directly inspected builders. Provider internal context/retention is uninspected; no absent-provider-memory conclusion follows. Model output budgets are separate from note-body character caps, as [RT-RTE-model-request](runtime.md#rt-rte-model-request) records.

## Integration issues

- **Qualification, not correction, of supplied rule retention:** [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) is accurate about split/transform, but later mapping receives embedded original text only for transform, not the defeated body behind split's link. Annotation and SRC-1 `flows/elevation.ts`/`flows/presuppositionMap.ts` preserve the consequence: lineage retention is not complete reason delivery.
- **New maintenance coverage:** [MEM-RTE-note-maintenance](#mem-rte-note-maintenance) adds registered retroactive-origin/orphan/merge paths omitted from the runtime narrative's detailed account. Italian origin matching and merge-without-copy prevent universal reconstruction/history-preservation claims. They do not invalidate the supplied elevation route.
- **Deletion scope:** [RT-RTE-assumption-admission](runtime.md#rt-rte-assumption-admission)'s delete callback description needs the `U-` basename condition beside it for renames/nonstandard filenames. Evidence SRC-1 `main.ts`; [MEM-OBJ-note-metadata](#mem-obj-note-metadata). No supplied observation establishes all deletions clean dependencies.
- **Source-native “verbatim” qualification:** [MEM-OBJ-source-hubs](#mem-obj-source-hubs) retains YouTube line-start substitution. Full retained length is not byte identity or full model-input coverage; runtime's full-transcript distinction otherwise stands.
- **Display predicates are not epistemic tests:** [MEM-RTE-retained-inspection](#mem-rte-retained-inspection) and [MEM-BAP-dependency-display](#mem-bap-dependency-display) distinguish degree-based load-bearing display from established logical dependence. Graph counting uses visible assembled edges, whereas map counts either dependency direction. A universal equality of these counts is not established (SRC-1, `views/AntinomiaGraphView.ts`, `views/PresuppositionsMapView.ts`, `flows/presuppositionMap.ts`).
- **Audit coverage limit:** direct audit source checks Italian placeholder strings while current template emits English placeholders. Therefore a clean audit cannot certify all rules are compiled. This limits the display route, not note admission ([MEM-RTE-retained-inspection](#mem-rte-retained-inspection); SRC-1, `views/AuditVaultView.ts`, `core/templates.ts`).
- **Potential duplicates:** none identified after comparing supplied declarations. New objects are retained operands/results of supplied routes, not declarations of those routes again. New maintenance/inspection/inline routes state their distinct scope. No supersession is requested.
- **Unresolved implementation dependencies:** Obsidian cache timing, multi-file atomicity, real persisted payloads, provider state, detailed typed-list rendering and actual user reliance remain uninspected/external as scoped above. These prevent complete consistency, deployed operation and improvement conclusions, without negating inspected positive paths.

## Limitations and checks

Frozen checkout HEAD was rechecked as `6fafd01082fbecb2a18803500a1abe70a2bdc9f4`, equal to supplied boundary and runtime. Only SRC-1 text and handed members were used; no target code/tests/examples/services ran. Method identity is the supplied job, worker rules, member types, collection and record contract; no method-version hash was supplied or inferred. Checked countercases include split versus transform origin delivery, source hub versus model-input coverage, undermined-note titles remaining eligible for mapping context, gate bypasses supplied by runtime, and maintenance that loses rather than copies old body text.

Static implementation supports wiring, not exercised behavior, semantic activation, learning benefit or causally attributed self-improvement. Current user vault contents and historical rationales are not frozen. Validator success checks document form/citations and quotation occurrence, not those stronger conclusions.

Validation: passed the required role-memory artifact check (command result inspected).
