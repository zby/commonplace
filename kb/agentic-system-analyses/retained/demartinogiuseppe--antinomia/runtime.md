---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Antinomia runtime baseline: interactive note admission, Hunter selection, model transport and maintenance at the frozen plugin revision."
run-id: AAS-2026-11-08-antinomia-19694628edc2-01
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
---

# Antinomia runtime report

## Runtime account

Antinomia performs interactive knowledge work inside Obsidian, not an autonomous tool-using agent loop. Code owns progression between model calls and review interfaces; the user initiates operations and admits proposed note changes. A configured model classifies, extracts, titles, formulates IF/THEN proposals or identifies contradictory pairs. Markdown bodies carry natural-language content; frontmatter types, status and links drive fixed code rules. The host executes vault writes and networking. This account is static implementation evidence from SRC-1, with prompt text as doctrine/design. No target execution, activation evidence or measured benefit was supplied.

### Entry and ordinary invocation

On load, the plugin loads settings, registers the settings tab and a vault deletion callback, and installs commands/views. Commands include guided or empty tension/substrate creation, free input/clipboard input, PDF/YouTube ingest, classification, Hunter/focused Hunter, elevation, resolution, archiving and migration. Command callbacks and result-view actions are internal shipped drivers, not external orchestrators (SRC-1, `main.ts`, `views/HunterResultsView.ts`).

One ordinary invocation is free-form input:

1. The user selects the free-input command, enters text and presses Analyze. `FreeInputModal` passes the trimmed text and a button-owned abort signal to `analyzeFreeInput`.
2. The plugin chooses the active default profile. Missing credentials stop before a request. `FREE_INPUT_SYSTEM` requests a tension/substrate classification and extracted fields; the friction suffix requests optional explanation/confidence/limitations. The user text is one user message; the transport has no accumulated conversational history in this route.
3. The backend returns text. The flow parses it, retries once with a stricter JSON instruction if necessary, and returns analysis plus usage metadata. Network errors do not receive that prose-repair retry.
4. The UI opens a typed creation modal, prefilled with the parsed fields. The user can edit, cancel or skip to an empty template. Create serializes the edited fields with the appropriate template and calls `createNote`.
5. `createNote` ensures the destination folder, chooses a timestamp-prefixed filename with collision suffixes, calls the vault API, opens the file by default and returns a `TFile` or null. Creation and opening share one try/catch, so null does not establish that no file was written if opening failed after creation. No transaction across UI and storage is demonstrated.
6. A later Hunter invocation can select the new tension if open, or the new substrate, from cached frontmatter and read its body. This later selection is conditional on the note cap and modification-time ordering, not guaranteed reuse.

This chain is [RT-RTE-free-input](#rt-rte-free-input), using [RT-RTE-model-request](#rt-rte-model-request) and [RT-CMP-model](#rt-cmp-model). Evidence: SRC-1, `main.ts`, `flows/freeInput.ts`, `modals/FreeInputModal.ts`, `modals/NewTensionModal.ts`, `modals/NewSubstrateModal.ts`, `core/templates.ts`.

> this.onAnalyzed(result.analysis, t, result.meta);
> --- `modals/FreeInputModal.ts`

> const file = await this.app.vault.create(path, content);
> --- `main.ts`

### Material alternate routes

Hunter is a bounded batch comparison, not iterative autonomous search. It selects typed notes, truncates bodies, calls the backend, normalizes/filters output and renders surviving pairs. Focus mode changes both request instructions and the output predicate. A human dismissal persists a pair exclusion for later output filtering; the model still receives the notes. Result-view actions route back to ordinary elevation/resolution/archiving drivers. See [RT-RTE-hunter-scan](#rt-rte-hunter-scan) and [RT-RTE-pair-dismissal](#rt-rte-pair-dismissal) (SRC-1, `flows/hunter.ts`, `views/HunterResultsView.ts`).

Elevation admits a new principle or transforms the original note. AI is optional and only fills editable fields. Mapping a principle's presuppositions is another model proposal followed by per-row create/link/skip decisions. Older tension presupposition mapping instead edits A/B fields in the same note. These are distinct objects and admission paths; mapping a principle does not automatically undermine it or revise its rule. See [RT-RTE-rule-admission](#rt-rte-rule-admission) and [RT-RTE-assumption-admission](#rt-rte-assumption-admission) (SRC-1, `flows/elevation.ts`, `flows/presuppositionMap.ts`, `flows/presupposti.ts`).

PDF and YouTube concept ingestion share an extraction helper, preview selector and bulk substrate creation. PDF text extraction uses the host's bundled PDF facility and a 30,000-character cap with confirmation when truncated; the YouTube concept path separately bounds AI input while preserving the full transcript in its hub. Quick YouTube ingestion instead opens a single prefilled substrate modal. Bulk operations create a hub and individual concept files sequentially and can leave partial results; they are not all-or-nothing admissions. See [RT-RTE-source-ingest](#rt-rte-source-ingest) (SRC-1, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts`).

Other inspected mutation paths retain human admission: classification validates a proposed type then uses `ClassifyConfirmModal`; file-title proposal opens an editable title modal before writing frontmatter. In-modal title assistance only fills a field, so its later acceptance follows that containing modal. Resolve writes status directly on the user's action; defeated archiving collects motive/replacement before changing type and optionally appending a replacement link. Empty-note commands bypass AI and creation modals entirely. These paths challenge any global claim that every vault write requires model-result approval or a friction checkbox (SRC-1, `main.ts`, `flows/titleProposal.ts`). Schema migration is a separate deterministic maintenance admission, [RT-RTE-schema-migration](#rt-rte-schema-migration).

### Three forcing cases and control boundaries

**1. Stop is not universal provider cancellation.** The transport uses Node HTTP only for a local URL with a supplied signal, and destroys that request on abort. Missing Node HTTP falls back to `requestUrl`; remote calls and calls without signals use `requestUrl` directly. The latter takes no abort signal. Hunter additionally races a local abort promise against the call, permitting prompt UI return without establishing that the remote provider stopped generation. Free input, title assistance and concept extraction check an aborted signal after completion before delivering a result. Principle presupposition mapping does not have that same post-success check before opening review; its catch handles rejected aborts. Therefore a Stop affordance is not a universal no-late-review guarantee either. These are inspected reachable branches, not demonstrated live failures (SRC-1, `ai/callAI.ts`, `flows/hunter.ts`, `flows/freeInput.ts`, `flows/titleProposal.ts`, `flows/pdfIngest.ts`, `flows/presuppositionMap.ts`).

**2. High friction is a local UI gate, not a write invariant.** The settings description promises acknowledgment before accepting an AI result. `gateAcceptButton` implements this for its consumers, including concept preview and principle-presupposition review. But free-input creation and elevation only render a card: their Create/Elevate callbacks do not install that gate. Both have shipped AI-prefill paths, so this is more than a hypothetical direct API caller. Manual/empty creation and direct persistence helpers also do not enforce it. The owner is each modal, the enforcement point is button disabling, and the strength is a local UI policy. Obsidian DOM behavior is an external contract; there is no persistence-layer acknowledgment check here. See [RT-CLM-friction-scope](#rt-clm-friction-scope) (SRC-1, `main.ts`, `modals/FrictionCard.ts`, `modals/ConceptsPreviewModal.ts`, `modals/PresuppositionMapModal.ts`, `modals/NewTensionModal.ts`, `modals/ElevateToPrincipleModal.ts`).

**3. Hunter's anti-hallucination filter is structural, not a truth guarantee.** The filter checks two different nonempty selected basenames, a nonempty description and focus participation. It then removes dismissed pairs. It neither verifies semantic contradiction nor checks that descriptions avoid proposing solutions. A real selected pair with an incorrect but nonempty description can satisfy the predicate; this is a source-level forcing input, not a supplied observed output. “Identify, not resolve” is prompt guidance, not enforced semantic exclusion. The owner is the Hunter flow; the predicate is an invariant of successfully filtered result construction, while accuracy and prompt compliance remain best effort. Basename membership does not establish globally unique path identity (SRC-1, `flows/hunter.ts`, `ai/prompts.ts`).

> Resolution is the user's work. You IDENTIFY, they RESOLVE.
> --- `ai/prompts.ts`

### Capability, grants and isolation

The inspected model request is a returning text computation: it sends model/system/messages and budgets, not a provider-tool declaration, and the flow consumers parse text rather than dispatching model tool calls. Effectful actions belong to plugin callbacks using the Obsidian app/vault interfaces. This bounds these inspected routes; it is not a security audit of the host or a proof about arbitrary installed extensions. Local Electron HTTP access is transport code, not delegated shell execution. Clipboard access has Electron and browser fallbacks. There is no worker delegation in the inspected request chains; the model receives only explicitly assembled input (SRC-1, `ai/callAI.ts`, `flows/freeInput.ts`, `flows/hunter.ts`).

The available plugin capability surface includes note reads/writes and configured network access. The current grant set depends on the user's profiles, API credentials and host permissions; the defaults include an empty key, so installation alone does not grant a working model connection. The deployed isolation envelope is not established by plugin source: Obsidian and providers are outside the frozen boundary. A cloud-profile warning examines the active profile and is dismissible; Hunter can use a separate profile override. Neither this warning nor local-host classification is a request-time confidentiality reference monitor (SRC-1, `main.ts`, `core/settings.ts`, `ai/callAI.ts`).

Reliability controls are local: parser recovery, single retries, stop signals, loading buttons, synchronous elevation-modal duplicate protection, collision suffixes, notices and an outer `guardedRun` error catcher on selected wrappers. These do not imply global serialization or atomic multi-file updates. Usage/duration/profile metadata and raw-response debug paths aid diagnosis but supply no execution evidence in this analysis (SRC-1, `main.ts`, `helpers/withLoadingButton.ts`, `flows/freeInput.ts`, `flows/hunter.ts`, `flows/elevation.ts`). Product or model-capability updates are not performed by these note-admission loops; profile edits change future backend routing, not model parameters. Build/release behavior and provider internals were not deeply traced here, so no exhaustive absence claim about improvement machinery is made.

Added coverage beyond the boundary's initial reads comprises the free-input driver/modals, transport branches, friction helper and acceptance consumers, elevation driver/modal, concept-ingest drivers/preview, title proposal, tension presupposition mapping, migration orchestration/modal, templates, request parsing excerpts and command/action methods cited above. All are SRC-1 implementation, except prompt/limitation text as doctrine/design. Memory revisions and full retained-object inventories remain the memory analyst's responsibility.

## Shared records

### Components

#### RT-CMP-model
Label: Configured model service

Source-native identity: `Profile.model`, `Profile.baseUrl` and `Profile.apiKey`, selected by `profileFor`. Representational form: distributed-parametric model behind an external service; request/response interfaces are symbolic JSON carrying natural-language messages. Storage substrate: provider/local-server weights, outside SRC-1. No parameter-update operation is present in the inspected call route; parameter mutability inside the service is uninspected. Exact weight version is not pinned by the plugin. An editable endpoint/model identifier can resolve to a different model; even an unchanged identifier does not prove immutable weights. Default model string is `claude-sonnet-4-6`, with an initially empty key. Evidence: SRC-1, `core/settings.ts`, `main.ts`, `ai/callAI.ts`.

> model: opts.model,
> max_tokens: effectiveMaxTokens,
> system: opts.system,
> messages: opts.messages,
> --- `ai/callAI.ts`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-model-request
Label: Configured model request

Code owns profile-to-HTTP-to-parsed-text progression; the service owns inference. `detectApiFormat` chooses Anthropic by URL substring, otherwise OpenAI-compatible. Explicit token cap overrides task-family recommendations; default fallback is 1024. Short/medium tasks request reduced thinking; deep tasks leave it enabled unless overridden. OpenAI-family reasoning uses `reasoning_effort: low`; runtime-specific disable fields are sent only for URLs classified local. These are requests to the backend, not proof that hidden reasoning is disabled. Local requests first ping the server; HTTP failures become errors, and responses feed the shared parser. No route-level automatic network retry is shown (SRC-1, `ai/callAI.ts`).

- Immediate return: Text and optional usage, or rejected error.
- Later read-back: inapplicable — this transport does not itself retain outputs for later consumption.
- Delegated visibility: Configured backend receives system instructions and caller messages; no child worker receives a separate task.
- Selection predicate: Active profile, except Hunter's valid configured override; URL format/locality and model-family detection control body/transport branches.
- Invalidation or expiry: Per-call request state ends on return/error; warning-deduplication set lasts the module session.
- Activation or effect: Network POST; parameter and instruction compliance remain provider-dependent.
- Evidence limits: Source wiring only; external service implementation, actual deployed model, provider retention and cancellation behavior unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (isLocal && opts.signal) {
> --- `ai/callAI.ts`

> // Fall through to requestUrl below (no cancellation possible)
> --- `ai/callAI.ts`

#### RT-RTE-free-input
Label: Free-input note admission

Endpoints are user text and a user-approved typed Markdown note. Model proposes type/fields, code parses and routes, human edits/decides/vetoes, host executes storage. Open requests, not a curriculum; no answer oracle is used. Guidance is `FREE_INPUT_SYSTEM` plus optional friction fields; what persists is the submitted template content, not a guaranteed faithful copy of the original. Failed parsing after one retry offers explicit confirmation to save the raw model response as a substrate, not silent admission. Cancel prevents the ordinary submit callback from writing; Skip writes a blank template. No automatic rollback is supplied (SRC-1, `flows/freeInput.ts`, `modals/FreeInputModal.ts`, `modals/NewTensionModal.ts`, `modals/NewSubstrateModal.ts`, `main.ts`).

- Immediate return: Parsed analysis/meta followed by modal; persistence returns a file or null through `createNote`.
- Later read-back: Created open tensions/substrates become eligible for later Hunter scans, subject to caps and ordering.
- Delegated visibility: Backend sees supplied raw input; modal sees parsed fields and metadata, not an independently verified analysis.
- Selection predicate: Parser's type selects tension versus substrate; user chooses Create, Cancel or Skip.
- Invalidation or expiry: Modal-local state discarded on close; persisted note has no automatic expiry in this route.
- Activation or effect: User submission writes vault Markdown; later model use is conditional, not observed.
- Evidence limits: Editing and admission are wired, not evidence of human scrutiny, original-text preservation or model accuracy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (fields === null && !skipped) return;
> --- `flows/freeInput.ts:120-136`

#### RT-RTE-hunter-scan
Label: Hunter bounded comparison

User command or focus action triggers code-owned selection → model judgment → normalization → structural/dismissal filtering → result view. Identity uses note basenames, not persistent opaque IDs. Candidates are open tensions and substrates sorted newest-modified first. Defaults are 20 notes and 800 body characters per note; focus is inserted first and fills remaining slots from candidates. Frontmatter is stripped, body prefixes delivered. Context control is deterministic code selection/truncation, not model compaction: omitted text stays in the vault but is not automatically fetched during this call. The model is instructed to examine all pairs; no code enumeration forces semantic examination of each pair. One parse-repair retry is allowed. No answer oracle is consulted. Mode is an open user-requested scan, with no automatic improvement trigger (SRC-1, `flows/hunter.ts`, `core/settings.ts`, `ai/prompts.ts`).

- Immediate return: Filtered pairs and run metadata to `HunterResultsView`, or error/abort notice.
- Later read-back: Later scans reload notes and dismissal frontmatter; stored settings retain last-run timestamp/count rather than the full comparison result in this flow.
- Delegated visibility: Backend receives selected body prefixes and basename/type labels; no separate worker context exists.
- Selection predicate: Type/status, mtime, note cap, optional focus; output requires real selected non-self basenames, nonempty description, focus involvement when requested, and no matching dismissal key.
- Invalidation or expiry: View result changes on a new run or dismissal; note edits do not constitute a new validated comparison.
- Activation or effect: Renders suggestions and updates last-run settings; human actions separately admit note changes.
- Evidence limits: No measured precision, recall, pairwise completeness or successful semantic compliance; truncation and basename ambiguity bound the result.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const truncBody = body.length > bodyLimit ? body.slice(0, bodyLimit) + "..." : body;
> --- `flows/hunter.ts`

> if (!a || !b || a === b) { return false; }
> if (!desc || desc === "undefined") { return false; }
> --- `flows/hunter.ts`

#### RT-RTE-pair-dismissal
Label: Persistent pair dismissal

User marks a displayed pair false positive; code writes peer basenames to both notes' `hunter_false_positives` arrays. A subsequent Hunter call constructs symmetric sorted pair keys from selected notes and filters matching results. The human supplies the negative judgment; computation records/applies it, with no answer oracle. Undismiss removes the entries, permitting future display. Writes are sequential, not a two-file transaction; a missing peer is skipped. This is output suppression, not model training or prompt removal (SRC-1, `flows/hunter.ts`, `views/HunterResultsView.ts`).

- Immediate return: Notice and current-view removal after dismissal.
- Later read-back: Later scans read selected notes' dismissal frontmatter and remove matching returned pairs.
- Delegated visibility: Backend still sees the selected notes; dismissal affects the plugin's returned-result filter.
- Selection predicate: Exact sorted basename pair key; duplicate basenames or renames limit identity reliability.
- Invalidation or expiry: Explicit undismiss removes suppression; no time expiry in this path.
- Activation or effect: A matching future pair is deterministically hidden if the retained entry reaches the filter.
- Evidence limits: Wired feedback path; no supplied observation of recurring use, model change or accuracy improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (dismissedSet.has(key)) {
>   dismissedFiltered++;
>   return false;
> }
> --- `flows/hunter.ts`

#### RT-RTE-rule-admission
Label: Principle rule admission

A user elevates a tension through an editable IF/THEN/GREY form, optionally requesting a model proposal. The model proposes; the human decides/vetoes or skips to placeholders; code applies split (default) or transform. Split creates a principle before converting the tension into defeated with a replacement link. Transform changes frontmatter and then rewrites body while preserving the old body under Origin. There is no automatic rollback of partial updates. No answer oracle tests the proposed rule. Mode is an open request, not a bounded experiment. Guidance requests verifiable contexts, operational outcomes and both sides as cases; retained output is formulated rule text and origin references, not a demonstrated successful resolution (SRC-1, `flows/elevation.ts`, `modals/ElevateToPrincipleModal.ts`, `core/templates.ts`, `ai/prompts.ts`).

- Immediate return: User-visible new principle or transformed note, with notice/error.
- Later read-back: Principle body can reach a later presupposition-mapping model call; it is not an eligible Hunter candidate merely by being a principle.
- Delegated visibility: Proposal call sees tension body; the review modal sees proposed fields and optional friction card.
- Selection predicate: Modal opening checks tension type; setting chooses split versus transform; final fields come from the user form.
- Invalidation or expiry: No automatic expiry or empirical invalidation; user edits/archive actions remain available.
- Activation or effect: Type/body/link writes change later graph and note consumers; operational application of the rule is not demonstrated.
- Evidence limits: Preserving origin is lineage, not a test of the rule; sequential writes do not prove transactional recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - IF must describe a verifiable context, not repeat the thesis
> - THEN must be operational (what to do/conclude), not abstract
> --- `ai/prompts.ts`

Theory account: the rule is localized natural-language conditional content, with separately editable conditions, outcomes and grey zone. It is derived from the tension under static shipped guidance. The UI can retain it and later ask for assumptions, but no inspected automatic loop tests the rule, places blame for failure, revises it and uses that criticism in another round.

- theory-builder conditions 1–4: Condition 1 — implementation conclusion status: afforded. The template/form permits a whole stated conditional rule; placeholder-only submissions do not establish an actual theory. Condition 2 — implementation conclusion status: wired. The later mapping request consumes what the rule says as model input; semantic dependence in a live run remains unobserved. Condition 3 — operation conclusion status: uninspected. No supplied criticism with claim/result/blame/revision establishes this condition; model internals are opaque. Condition 4 — operation conclusion status: uninspected. Retained rules and assumptions enable further work but do not demonstrate criticism-led iteration.
- Addressability: IF/THEN cases and grey zone are inspectable/editable prose units; dependency links provide explicit assumption handles, not verified assumptions.
- Persistence: Vault notes can survive sessions and reach later mapping calls; actual cross-session use unobserved.
- learning: Improved future capacity is unestablished; proposal and persistence alone supply no improvement or attribution evidence.
- Reflection: Subject matter is the user's knowledge/rules; an operational self-representation of plugin machinery is not established by this path.
- Reflective theory builder: Unestablished; no inspected criticism of method texts against the plugin's own operational record.
- Autonomous theory builder: Unestablished; final content admission is human, and criticism-led iteration is not demonstrated.

#### RT-RTE-assumption-admission
Label: Presupposition review admission

For a principle, code reads body/title plus existing U-note basenames/titles, asks for implicit assumptions, parses proposals, then opens per-row editable review. Human selects new/link/skip and can cancel; model-suggested existing matches become defaults only when in the existing list. Confirmation creates U notes and unions forward/reverse links. Link decisions do not need newly generated text. No oracle verifies load-bearing truth; confidence is model output. Later collapse impact uses either direction of the dependency links and offers a separate human action to mark an assumption undermined, not automatic rule rejection. Failure can leave partial notes/links; no multi-file rollback is supplied. Older tension mapping is a distinct inline A/B update flow, not the U-note admission mechanism (SRC-1, `flows/presuppositionMap.ts`, `modals/PresuppositionMapModal.ts`, `flows/presupposti.ts`).

- Immediate return: Review modal, then created notes/link updates and graph refresh after confirmation.
- Later read-back: Existing U-note titles enter future proposal context; dependency links reach impact lookup. This does not prove generated assumptions control later practical decisions.
- Delegated visibility: Backend sees principle body and titles/basenames of existing U notes, not their full bodies from `gatherExistingPresuppositions`.
- Selection predicate: Principle type guard; parsed nonempty proposals; exact existing-match default; human per-row decisions.
- Invalidation or expiry: User can mark undermined; deletion callback removes U links from principles; no automatic expiry.
- Activation or effect: Retained assumption text and symbolic dependency graph change; actual reliance or criticism remains unobserved.
- Evidence limits: Naming dependencies is not evidence that they are true or sufficient; sequential writes and metadata cache timing bound consistency.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fm.presupposes = toWikilinks(mergeUnique(prev, uBasenames), titleMap);
> --- `flows/presuppositionMap.ts`

#### RT-RTE-source-ingest
Label: Source concept admission

User selects PDF or supplies YouTube URL/transcript. Host extraction/fetch precedes model concept extraction; code sanitizes nonempty title/content, then a shared preview lets the human select/veto the batch (default all selected). Confirmation creates hub and linked substrates. The model proposes knowledge content under `EXTRACT_CONCEPTS_SYSTEM`; no reference answer verifies fidelity or distinctness. Mode is open source ingestion, not evaluation. Source/hub references persist; bulk creation continues across individual concept failures and reports actual created count, without undoing earlier files. The quick YouTube path uses a single guided substrate instead of concept extraction (SRC-1, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts`, `modals/ConceptsPreviewModal.ts`).

- Immediate return: Concept preview followed by per-source hub/substrate creation, or error/cancel.
- Later read-back: Created substrates can enter later Hunter selection; hub/transcript retention is distinct from what the extraction model received.
- Delegated visibility: Backend sees bounded extracted text; preview sees sanitized concepts and usage. No per-source subagent or chunk-reduction loop is involved in these drivers.
- Selection predicate: Source input caps, nonempty fields, human-selected concept indices; high-friction checkbox when payload is supplied.
- Invalidation or expiry: No automatic expiry; files remain user-editable.
- Activation or effect: Vault creation and links; semantic faithfulness and future use unobserved.
- Evidence limits: PDF OCR is not provided by the inspected extraction path; truncation prevents full-source coverage claims. Fetch services and PDF engine implementation are external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const PDF_TEXT_HARD_CAP_CHARS = 30_000;
> --- `flows/pdfIngest.ts`

> const aiInput =
>     text.length > YT_AI_INPUT_CAP_CHARS ? text.slice(0, YT_AI_INPUT_CAP_CHARS) : text;
> --- `flows/youtubeFetch.ts`

#### RT-RTE-schema-migration
Label: Schema migration admission

User confirms migration in `MigrationModal`; deterministic tables rename legacy keys/enums/body markers. `migrateVault` scans legacy notes, awaits a full backup of that selection, then applies each note's body/frontmatter transformations and counts failures. It is not model-driven knowledge revision and uses no answer oracle. Human initiation approves the migration batch; code chooses exact transformations. Latest-backup restore overwrites/recreates original paths, rather than validating semantic equivalence or undoing unrelated later changes. The backup-before-loop guarantee covers `migrateVault`, not direct calls to exported `migrateNote` (SRC-1, `flows/migration.ts`, `modals/MigrationModal.ts`, `main.ts`).

- Immediate return: Migration report/counts or backup error; restore returns restored count/report.
- Later read-back: Renamed types/status fields affect later plugin selectors; backup copies are available to explicit restore.
- Delegated visibility: inapplicable — deterministic host operations, no model or worker request.
- Selection predicate: Legacy-key presence and exclusion of backup paths; restore selects latest lexically sorted timestamp backup.
- Invalidation or expiry: Restore overwrites current originals; no automatic expiry/garbage collection established here.
- Activation or effect: Vault body/frontmatter changes; adapter backup writes; no product-code mutation.
- Evidence limits: No observed restore, host durability or atomic migration. Per-note failures can follow successful earlier changes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const backupPath =
>     legacyFiles.length > 0 ? await createPreMigrationBackup(app, legacyFiles) : "";
> --- `flows/migration.ts`

### Claims

#### RT-CLM-friction-scope
Label: High-friction acknowledgment scope

Claimed operation: settings text describes acknowledgment before accepting an AI result at high friction. Source: SRC-1, `main.ts`.

> High = card always open + you must acknowledge limitations before accepting an AI result.
> --- `main.ts`

Implementation narrows that statement. Owner: each consuming modal; enforcement point: `gateAcceptButton` disables a UI button until checked. Guarantee strength: policy. Covered paths inspected: concept-preview batch confirmation and principle-presupposition confirmation with a payload. Alternate reachable paths: free-input AI-prefilled tension/substrate creation and optional-AI elevation render cards without calling the gate; persistence helpers impose no corresponding condition. Required external contract: ordinary DOM disabled-button behavior, not hostile-code isolation. This qualifies the scope without claiming user exploitation or an observed failure (SRC-1, `modals/FrictionCard.ts`, `modals/ConceptsPreviewModal.ts`, `modals/PresuppositionMapModal.ts`, `modals/NewTensionModal.ts`, `modals/NewSubstrateModal.ts`, `modals/ElevateToPrincipleModal.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (level !== "high") return () => true;
> --- `modals/FrictionCard.ts`

> this.onSubmit({ ifA, thenA, ifB, thenB, greyZone }, false);
> --- `modals/ElevateToPrincipleModal.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-policy
Label: Shipped prompt guidance

Consumer: configured model service. Channel: `callAI` system field (Anthropic) or system message (OpenAI-compatible). Force: natural-language guidance plus expected JSON shape, not semantic enforcement. Horizon: current request; static shipped prompt definitions are reused across requests. Hunter guidance forbids resolution while elevation guidance explicitly requests operational rules, so the restriction is task-specific, not system-wide. Evidence: SRC-1, `ai/prompts.ts`, `ai/callAI.ts`; [RT-RTE-model-request](#rt-rte-model-request).

#### RT-BAP-dismissal-filter
Label: Retained dismissal authority

Consumer: Hunter result filter. Channel: cached note frontmatter → sorted basename-pair set. Force: symbolic exclusion of matching returned pairs, independent of the model's confidence. Horizon: later scans while entries remain and identities still match; undismiss reverses it. This is an actual code-consumer path, not an instruction for the model to comply with. Evidence: SRC-1, `flows/hunter.ts`; [RT-RTE-pair-dismissal](#rt-rte-pair-dismissal).

## Annotations

none
