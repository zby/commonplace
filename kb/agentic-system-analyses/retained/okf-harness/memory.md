---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OKF Harness memory mechanisms: retained source bytes, agent-authored wiki synthesis, reconciliation state, bounded read-back and Git recovery."
run-id: AAS-2026-10-15-okf-harness-6bf5507fbdbf-01
source-identity: https://github.com/pumblus/okf-harness
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
---

# OKF Harness memory report

## Boundary and evidence

This report covers the whole-system memory loop at SRC-1 commit **0dd4f806c454a68088c5a3e64b4cbebbe2c216be**: source registration; agent-owned synthesis and revision; conversation-derived answer write-back; checking, evidence selection and direct retrieval; graph artifacts; and Git checkpoints/restoration. The source identity and evidence layers remain those in [boundary](boundary.md#source-register). No new source or execution layer is introduced.

The principal memory is a local Markdown wiki, not a model-owned vector store or an execution-history summarizer. Local source bytes and URL metadata are different acquisition products. Manifest identities, wiki frontmatter/citation syntax and reconciliation edge IDs have symbolic consumers; wiki claims and judgment notes have natural-language consumers. These parts are separated below rather than assigning one form or one authority to the workspace. SRC-1: `packages/core/src/source/index.ts`, `packages/core/src/read/index.ts`, `packages/core/src/source/reconciliation.ts`.

Direct inspection extended the supplied runtime account at the same frozen revision. The inventory below distinguishes those reads from reliance on supplied records. It covers CLI dispatch, exposed core operations and the supplied host synchronization route; it does not treat an exported storage operation as evidence of an unspecified model consumer. Host model/session internals, provider state, effective instruction loading and host compaction remain external and uninspected. This prevents conclusions about actual window occupancy, activation, semantic compliance or improved answer quality, not the source-visible persistence and selection mechanisms.

| Entry point or operation | Source path and inspection basis | Covering records or inspection limit |
|---|---|---|
| CLI dispatch and public exports | Direct: `packages/cli/src/index.ts`; supplied runtime inventory of `packages/core/src/index.ts` | [RT-CMP-core](runtime.md#rt-cmp-core); source/query/recovery and installation routes below. No target-managed model call inferred from exports. |
| Initialize local substrate | Direct: `packages/core/src/workspace/index.ts` workspace plan/config/scaffold; supplied init caller | [MEM-OBJ-wiki-content](#mem-obj-wiki-content), [MEM-OBJ-manifest](#mem-obj-manifest); [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery). Initial payload authorship outside shipped scaffolds is not universally known. |
| Source add/list; manifest reload | Direct: `packages/core/src/source/index.ts` registration and manifest reader | [MEM-OBJ-source-bytes](#mem-obj-source-bytes), [MEM-OBJ-url-metadata](#mem-obj-url-metadata), [MEM-OBJ-manifest](#mem-obj-manifest); [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). |
| Ingest plan and semantic writing | Direct: `packages/core/src/source/ingest.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md` | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-wiki-content](#mem-obj-wiki-content). Actual source interpretation remains unobserved. |
| Revision diagnosis and acknowledgment | Direct: `packages/core/src/source/reconciliation.ts`, `packages/core/src/lineage/index.ts`, shipped reconcile reference | [MEM-OBJ-reconciliation-edges](#mem-obj-reconciliation-edges), [MEM-OBJ-reconciliation-notes](#mem-obj-reconciliation-notes), [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile). |
| Check/status/lint and source integrity | Direct: `packages/core/src/check/index.ts`, snapshot assembly, registered-source hash checks in `packages/core/src/lint/index.ts`; supplied status consumer | [MEM-RTE-workspace-check](#mem-rte-workspace-check), [MEM-CLM-currency-evidence](#mem-clm-currency-evidence). Semantic correctness is not checked. |
| Evidence brief and continuation | Direct: `packages/core/src/evidence/index.ts` planner, excerpts, provenance, seals and budgets; query CLI; answer reference | [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context). |
| Alternate search/read | Direct: search scoring; read target resolution/result assembly; query CLI | [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval), [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata). Detailed section-option error branches not exhaustively audited; supplied runtime findings bound the general read account. |
| Accepted conversation write-back | Direct: answer reference; evidence no-match permission branch | [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), [MEM-OBJ-wiki-content](#mem-obj-wiki-content), [MEM-CLM-provenance-signal](#mem-clm-provenance-signal). Protocol is not an enforced write API. |
| Graph/backlinks report | Direct: `packages/core/src/graph/index.ts` generation and persistence; query CLI | [MEM-OBJ-backlinks](#mem-obj-backlinks), [MEM-RTE-graph-report](#mem-rte-graph-report). Browser interaction itself unobserved. |
| Checkpoint/history/restore | Direct: `packages/core/src/recovery/index.ts` functions; supplied CLI recovery route | [MEM-OBJ-checkpoint-tree](#mem-obj-checkpoint-tree), [MEM-OBJ-checkpoint-judgment](#mem-obj-checkpoint-judgment), [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery). |
| Static guidance installation, OpenCode synchronization and runtime pin | Supplied implementation findings, not independently re-audited: `packages/agent-pack/src/index.ts`, `packages/native-integration/src/opencode.ts`, `packages/setup/src/index.ts`, `packages/core/src/config/index.ts` | [RT-RTE-guidance-install](runtime.md#rt-rte-guidance-install), [RT-RTE-runtime-launch](runtime.md#rt-rte-runtime-launch), [RT-OBJ-workflow-guidance](runtime.md#rt-obj-workflow-guidance), [RT-OBJ-runtime-pin](runtime.md#rt-obj-runtime-pin). Static instruction delivery is not use-derived memory. No online trace-learning conclusion follows. |
| Legacy wiki log and evaluation fixtures | Direct: reserved-file scan/read handling; CLI maintenance-loop test | [MEM-CLM-log-exclusion](#mem-clm-log-exclusion), [MEM-CLM-currency-evidence](#mem-clm-currency-evidence). Test definitions are not observed runs. |

## Core ideas

1. **Registration preserves inputs; the agent produces knowledge.** File bytes are copied and hashed. URL registration preserves a pointer document, not webpage contents. Metadata-only planning proposes paths and candidates; source reading and meaning-changing synthesis belong to the host agent. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-url-metadata](#mem-obj-url-metadata).
2. **The same wiki accepts sourced synthesis and explicitly accepted conversation-derived answers.** Both later enter ordinary lexical retrieval. The latter deliberately lacks source citations; the provenance-empty payload asks the agent to disclose a conversation origin, but does not independently prove it. [MEM-CLM-provenance-signal](#mem-clm-provenance-signal).
3. **Integrity withholding and revision currency are different controls.** Missing/drifted sources can remove linked concepts from evidence; an unacknowledged revision edge does not itself remove their excerpts. Acknowledgment changes a maintenance fact, not wiki meaning. [MEM-CLM-currency-evidence](#mem-clm-currency-evidence).
4. **Context selection is request-driven and bounded, not host memory management.** Code chooses at most three wiki excerpts; workflow text limits follow-up reading. Character limits apply to excerpt bodies, not the entire JSON result or host window. Direct search/read and shell access remain distinct routes. [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval).
5. **Recovery preserves both a workspace version and a caller judgment, with different consumers.** Restoration changes files read by later commands. History exposes judgments to callers. Neither is a trace-to-policy learning loop or an automatic semantic rollback. [MEM-OBJ-checkpoint-tree](#mem-obj-checkpoint-tree), [MEM-OBJ-checkpoint-judgment](#mem-obj-checkpoint-judgment).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-bytes
Label: Registered file source bytes

Raw file contents are copied byte-for-byte under the configured raw-source directory on local disk. The bytes can be text or opaque binary; registration does not interpret their representational form or derive a readable semantic summary. Source ID/hash/path are separate metadata in [MEM-OBJ-manifest](#mem-obj-manifest). The later ingest/reconcile agent reads these registered inputs through its shell; checks read bytes to verify integrity, whereas ordinary evidence answering reads synthesized wiki content instead. Initial input authorship/trust is user-supplied or otherwise external, not certified by registration. Distinct object from the closest supplied route [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest): this is its retained acquisition input, not the route itself. SRC-1: `packages/core/src/source/index.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/agent-pack/templates/okf-harness/references/reconcile.md`.

> const contents = await readFile(sourcePath);
>   const sha256 = sha256Hex(contents);
> --- `packages/core/src/source/index.ts`

Immutability is exclusive creation plus delivered policy, not a filesystem-wide prohibition; see the supplied route's counterpaths. Same-hash file reuse can return a prior identity instead of another copy. Retention lasts until outside mutation or recovery changes the workspace; no expiry is applied by registration.

#### MEM-OBJ-url-metadata
Label: Registered URL metadata

A URL registration stores a generated `.url.md` file and its hash on local disk. This is mixed natural-language pointer content and symbolic URL/date information, not retained remote webpage bytes. Reuse is by normalized URL, so later registration of that URL does not establish a newly acquired revision. A later ingest agent still needs accessible source content. The registered hash can validate the pointer file, not the truth or current body of the remote page. Distinct from file-source bytes and from the supplied acquisition route [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `packages/core/src/source/index.ts`.

> const metadata = urlMetadataContents(original, context.now);
> --- `packages/core/src/source/index.ts`

> sha256: sha256Hex(metadata),
> --- `packages/core/src/source/index.ts`

#### MEM-OBJ-manifest
Label: Source manifest entries

The configured manifest, default `.okfh/manifest.jsonl`, stores symbolic JSONL source IDs, kind, original name/URL, path, SHA-256 and timestamp, with optional descriptive fields. A title/notes string is descriptive text; inspected registration/planning/check consumers use identities and metadata, not a retained reasoning episode. Registration appends entries after writing raw data; invalid rows or duplicate IDs/paths reject ordinary operations. List, ingest plan, snapshots, hash checks, reference resolution and revision detection consume it on later invocations. Its authority is procedural identity/provenance, not semantic certification. Distinct retained access/lineage object associated with [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not a second declaration of that route. SRC-1: `packages/core/src/source/index.ts`, `packages/core/src/source/ingest.ts`, `packages/core/src/lineage/index.ts`.

> await appendFile(manifestPath, `${JSON.stringify(entry)}\n`, "utf8");
> --- `packages/core/src/source/index.ts`

#### MEM-OBJ-wiki-content
Label: Wiki claim prose

Natural-language concept/reference content persists in local Markdown, separate from mechanically parsed fields in [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata). The scaffold creates directories for decisions, entities, projects, questions, references and topics. Host agents author or revise prose under ingest/reconcile guidance, or write one accepted conversation-derived concept. Existing workspace prose can also have external/human provenance; a scan does not capture its author identity. This object spans outputs of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) and [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer); none supplies a separate wiki-content object counterpart.

Later evidence/read invocations deliver selected prose to the answering agent as knowledge, not as privileged workflow instructions. Index prose/link titles also influence search navigation. Claims may retain uncertainties, contradictions or reasons in their text, but inspected machinery neither requires a complete rationale nor guarantees its selection into a later excerpt. Conversation raw turns are not captured as a source; accepted semantic output is derived memory. SRC-1: `packages/core/src/workspace/index.ts`, `packages/core/src/search/index.ts`, `packages/core/src/evidence/index.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

> Never write to `raw/`. Write-back never captures the conversation as a source.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

#### MEM-OBJ-wiki-metadata
Label: Wiki retrieval and citation fields

Frontmatter, concept paths, tags, source IDs and parsed citation/link targets are symbolic parts of local Markdown consumed by the scanner, search scorer, reader, graph and lineage checks. Titles/descriptions also contain natural-language text; lexical code uses their strings as scoring input rather than treating them as established claims. Index link mentions influence search ranking; the index itself is reserved, readable navigation rather than a normal candidate concept. Concept identity is path-derived. This is distinct from claim prose because structural checks, provenance extraction and seal propagation act on these fields independently of meaning. The closest supplied records are the consumers [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) and [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval), not object counterparts. SRC-1: `packages/core/src/okf/concepts.ts`, `packages/core/src/lineage/index.ts`, `packages/core/src/read/index.ts`, `packages/core/src/search/index.ts`.

> const sourceId = frontmatterSourceId(file.frontmatter.data);
> --- `packages/core/src/lineage/index.ts`

Reference promotion for currency uses source IDs on valid reference documents under `references/`; evidence's source-risk linkage also inspects document source IDs. Provenance is extracted from the document and linked references, not authenticated as a claim-by-claim entailment. A citation-rich document can still contain an unsupported sentence.

#### MEM-OBJ-reconciliation-edges
Label: Reconciliation ledger edge identities

Local `reconciliation.jsonl` beside the manifest retains symbolic `prior_source_id` and `revision_source_id` fields. The exact pair suppresses a recomputed suspected revision edge. Suspicions group file sources by original filename, then compare the latest registered sibling's hash to each earlier sibling; URL registrations do not enter this detector. The ledger is not a source-version diff and does not replace raw copies. Snapshot/currency consumers use endpoint equality, not the note's semantics. Distinct stored part of the mechanism described in [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile); the supplied record is a route, not a ledger object. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/core/src/lineage/index.ts`.

> return suspectedRevisions(entries).filter(
>     (edge) => !isReconciledEdge(acknowledgements, edge.priorSourceId, edge.revisionSourceId),
>   );
> --- `packages/core/src/source/reconciliation.ts`

#### MEM-OBJ-reconciliation-notes
Label: Reconciliation judgment notes

The same local JSONL rows retain caller-authored natural-language `note` strings. The write API requires a nonempty trimmed note; parsing validates a nonempty string, not the truth of its explanation. The command returns the acknowledgment immediately. Later ledger reads retain the note in parsed entries, but the inspected dangling-edge consumer uses IDs alone. No later answer/planning route is established as reading the note's reasons. Thus retained rationale exists as inspectable text without an established semantic read-back consumer; it must not be equated with the wiki update itself. Distinct operative part from the edge IDs and from the supplied route [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile). SRC-1: `packages/core/src/source/reconciliation.ts`.

> const acknowledgement: ReconciliationAcknowledgement = {
>     prior_source_id: edge.priorSourceId,
>     revision_source_id: edge.revisionSourceId,
>     note,
>   };
> --- `packages/core/src/source/reconciliation.ts`

#### MEM-OBJ-checkpoint-tree
Label: Git checkpoint workspace tree

Git objects retain a versioned snapshot of Git-visible workspace files. Tree/path/blob identities are symbolic recovery material; contained files preserve their own natural-language, symbolic or opaque encodings. A checkpoint stages `--all`, so scope includes more than wiki claims: configuration, source records and workspace instructions can be restored together. Ignored files are not thereby guaranteed retention. Restore's selected tree becomes ordinary input to later status, ingest and answering invocations. This retained state is distinct from the recovery route [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery) and from its judgment body below. SRC-1: `packages/core/src/recovery/index.ts`.

> await runRecoveryCommand(workspaceRoot, ["add", "--all"], "write");
> --- `packages/core/src/recovery/index.ts`

The initialization baseline and later allow-empty checkpoints are alternative retained forms: an unchanged checkpoint may add a judgment without a meaning-changing wiki update. Neither form is a compressed conversation or an automatically distilled behavioral rule.

#### MEM-OBJ-checkpoint-judgment
Label: Checkpoint judgment body

A trimmed caller judgment is retained as a natural-language Git commit body. Caller identity may be human or agent; the core only requires nonempty text. History parses bodies and returns `{id, judgment}` records to later callers; no inspected answer selector automatically includes them. Their authority is to inform the caller's interpretation/restore choice, whereas restoration itself selects by completion ID. Listing omits restore commits and stops at the initialization baseline. Closest supplied record [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery) declares the operation, not this rationale-bearing part. SRC-1: `packages/core/src/recovery/index.ts`.

> judgment: fields[index + 2]?.trim() ?? "",
> --- `packages/core/src/recovery/index.ts`

#### MEM-OBJ-backlinks
Label: Backlinks and graph report

Derived symbolic nodes, edges, backlinks, missing-target information and generation time are persisted to `.okfh/backlinks.json`; an HTML rendering is written to `.okfh/reports/graph.html`. Labels display wiki titles, not opaque learned representations. The HTML supports a human/browser consumer. Evidence seal computation uses fresh graph data built from the current snapshot, not the persisted JSON report as a stale authoritative cache. No counterpart is declared in runtime; closest related consumer is [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). SRC-1: `packages/core/src/graph/index.ts`, `packages/core/src/evidence/index.ts`.

> await writeFile(backlinks.absolutePath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
>     await writeFile(html.absolutePath, renderGraphHtml(data), "utf8");
> --- `packages/core/src/graph/index.ts`

### Routes

#### MEM-RTE-workspace-check
Label: Workspace check and diagnostic consumption

A caller requests check/status or the evidence planner invokes the common pipeline. Core reloads config/wiki/manifest/ledger, derives lineage, hashes registered bytes, classifies lint and computes currency. Host guidance requests reporting and, only under a separate mutating workflow, repairing findings. Distinct from [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile): this route produces diagnostics without adopting prose edits or ledger acknowledgments. It supplies evaluation input to that route and to [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). SRC-1: `packages/core/src/lineage/index.ts`, `packages/core/src/check/index.ts`, `packages/core/src/lint/index.ts`, `packages/agent-pack/templates/okf-harness/references/check.md`.

- Immediate return: check yields ready/needs_attention/blocked, conformance findings, priority-grouped lint and currency; status/evidence consume the same pipeline output internally.
- Later read-back: current retained wiki, manifest, ledger and source bytes are reloaded on later invocations; diagnostic output itself is not automatically persisted as knowledge.
- Delegated visibility: CLI JSON exposes diagnostics to the host; evidence receives pipeline facts and emits selected risk warnings/seals rather than all possible semantic defects.
- Selection predicate: structural conformance codes determine blocked; lint groups remaining findings; currency considers promoted source edges and error diagnostics; byte hashes identify source drift.
- Invalidation or expiry: recomputed on each invocation; a prior ready result is not a permanent certification.
- Activation or effect: read-only evaluation; evidence can reject or withhold using derived facts. A host may elect repairs under another workflow; actual repair/adherence is unobserved.
- Evidence limits: structural validity, byte identity and acknowledged edge state do not establish claim truth, successful synthesis or a reference-answer oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Core decides mechanical classifications; the host/user selects whether to start a repair. The check workflow forbids writes on a check-only request. It admits no semantic change by itself and offers no semantic rollback. Its operating mode is open workspace maintenance, not a scored improvement curriculum.

> None. If the user asks to fix findings, treat it as a combined request: finish the check report, load the relevant mutating workflow, make only the requested wiki edits, and run check again.
> --- `packages/agent-pack/templates/okf-harness/references/check.md`

#### MEM-RTE-graph-report
Label: Graph report generation and inspection

Caller `graph` request → snapshot → deterministic node/edge extraction → JSON/HTML files and CLI paths → optionally opened browser. The code owns extraction; caller owns the inspection decision. This route has no counterpart in supplied records; its graph-data function is also used without report persistence by [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). SRC-1: `packages/core/src/graph/index.ts`, `packages/cli/src/commands/query.ts`.

- Immediate return: report paths, node/edge counts, issues and missing targets.
- Later read-back: persisted report can be opened later; documented CLI next action names the browser consumer. No inspected evidence-planner reload of backlinks JSON is established.
- Delegated visibility: CLI exposes paths/stats; HTML exposes derived graph labels and links to a browser reader, not a target-owned model context.
- Selection predicate: current nonreserved wiki files form nodes; parsed links/reference targets form typed edges and backlinks. No question-specific semantic selection or model budget applies.
- Invalidation or expiry: regeneration overwrites derived report files; edits after generation can make an existing report stale, while evidence rebuilds graph data from its own snapshot.
- Activation or effect: writes derived navigation artifacts and may request browser opening; model behavior change is unobserved.
- Evidence limits: graph linkage establishes a parsed relation, not semantic dependence or full contamination closure; browser operation is unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is caller-requested generation under fixed code, with safe output-path resolution and write failures reported. No model proposes a new claim, no human approves per-edge content, and no answer oracle is supplied. Recovery is regeneration for derived reports; no separate semantic-adoption or experiment loop is implemented in these functions.

> description: "Generate OKF backlinks data and a self-contained graph report.",
> --- `packages/cli/src/commands/query.ts`

### Claims

#### MEM-CLM-currency-evidence
Label: Currency acknowledgment is not evidence withholding

`currency.sealed` means promoted suspected revision edges are acknowledged and error diagnostics permit computation. It can be true with no promoted sources. It is not the evidence seal list, and false currency does not itself ban old prose from answers. Evidence risk codes include source loss/drift and manifest/config problems, not the suspected-revision warning. A ledger append can clear an edge without changing an excerpt. The supplied [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) establishes the acknowledgment limitation; [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary) establishes bounded contamination propagation. This record adds the distinction between two similarly named mechanisms. SRC-1: `packages/core/src/check/index.ts`, `packages/core/src/evidence/index.ts`, `packages/cli/test/maintenance-loop.test.ts`.

> return { sealed: dangling.length === 0, promotedSources, dangling, diagnostics };
> --- `packages/core/src/check/index.ts`

The maintenance-loop test explicitly expects pending revision evidence to remain available, then clears currency without a wiki-edit step. These are executable assertions, not an observed test outcome:

> expect(conceptIds(pending)).toEqual(conceptIds(restored));
>       expect(pending.result.data.seals).toEqual([]);
> --- `packages/cli/test/maintenance-loop.test.ts`

#### MEM-CLM-provenance-signal
Label: Empty provenance is a disclosure convention

The answer workflow instructs conversation-origin disclosure when citations and source pointers are empty. This is a convention at the agent consumer, not stored authorship proof. Accepted write-back deliberately produces that state, but an otherwise authored citation-empty page can produce it too. No author-capture field distinguishes those histories in the inspected read/provenance construction. Natural-language derived-from links are walkable provenance for an agent, not validated formal lineage. Closest supplied [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) already establishes acceptance; this claim qualifies inference from the resulting signal. SRC-1: `packages/agent-pack/templates/okf-harness/references/answer.md`, `packages/core/src/read/index.ts`, `packages/core/src/evidence/index.ts`.

> The empty provenance payload is the whole signal. No tier flag, no computed marker, and no authorship capture enters the evidence brief or any page's frontmatter.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

> The lineage is prose, written for the next reader's walkable trail.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

#### MEM-CLM-log-exclusion
Label: Legacy log files are not readable knowledge

Ingest/reconcile instructions still permit affected log-file edits, but the frozen scanner reserves `log.md`, search/evidence and graph omit reserved files, and read target resolution explicitly rejects a legacy log. The scaffold no longer creates it. Thus log retention or an allowed log write does not establish trace-fed knowledge read-back through these commands. This corrects any implication from the supplied boundary's example/log inventory that such a file is an answer surface; it does not deny possible external shell reading. Closest supplied [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval) needs this exception to a broad wiki-file description. SRC-1: `packages/core/src/okf/concepts.ts`, `packages/core/src/read/index.ts`, `packages/core/src/search/index.ts`, `packages/core/src/graph/index.ts`, `packages/core/src/workspace/index.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`.

> // log.md is no longer scaffolded; it stays reserved so a leftover log file in an older
> // workspace is ignored instead of being scanned as a concept document.
> --- `packages/core/src/okf/concepts.ts`

> path.posix.basename(candidate.bundlePath) !== "log.md" &&
> --- `packages/core/src/read/index.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Memory lineage is external input → raw copy/pointer and manifest → agent-authored reference/concept prose → later lexical retrieval and answering. Raw acquisition and derived wiki synthesis are separate writes with separate consumers. Code admits registration under path/type/manifest checks, exclusive creation and same-input reuse; it does not admit individual semantic claims. The host agent proposes/adopts wiki edits under text guidance, with a user stop before exceeding the configured file ceiling. Starting ingest is not per-content human approval. Failed registration/planning should prevent wiki editing by policy; a failed post-edit check does not physically reject an already saved claim. SRC-1: `packages/core/src/source/index.ts`, `packages/core/src/source/ingest.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`.

The ingest plan's read-back selector uses registered source metadata and concept metadata, caps five candidates and excludes references. It returns recommendations rather than source-body excerpts or synthesized claims. Candidate relevance must be judged after source reading. Source trust is not conferred by a hash: bytes establish recorded identity, not claim correctness. Retained wiki reasons may be present in prose but no complete explanation record is enforced.

> "Preserve uncertainty and contradictions; do not invent claims or citations.",
> --- `packages/core/src/source/ingest.ts`

#### On [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile)

The retained results split into edited wiki meaning, symbolic acknowledgment pairs and free-text judgments. The agent reads both registered revisions and every affected concept under the workflow; then the code checks IDs/edge/nonempty note and appends the ledger. A missing/invalid note can reject the acknowledgment after wiki files have changed. It does not undo the prose or establish that it matches the revision. Later snapshots filter edges by IDs, whereas later answers read wiki prose. The note's reasons are retained but are not selected into evidence provenance by the inspected route. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/core/src/lineage/index.ts`, `packages/agent-pack/templates/okf-harness/references/reconcile.md`.

Withdrawal is agent-owned prose replacement: the workflow requires positive textual evidence for suspected removal, not absence from a new revision alone. Raw prior copies remain; no semantic removal follows automatically from registration or acknowledgment. Recovery requires the separate Git route. This preserves the source-supported revision capacity without calling the ledger a semantic evaluator.

> Treat removal as suspected only when the new revision contains a positive textual signal; omission alone does not establish removal.
> --- `packages/agent-pack/templates/okf-harness/references/reconcile.md`

#### On [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer)

Read-back is a pull chain: user question → host-issued evidence command → code-selected wiki parts → JSON tool-result context → agent answer. Selection uses lexical question matching against title/path/tags/description/index/body, with a 200,000-character cutoff for body scoring of large documents. Search defaults to ten returned cards; evidence selects at most three and emits the remaining available cards as thin candidates. Those candidates are not all possible matches when search itself is capped. The excerpt selector ranks non-citation/non-reference sections by question overlap and chooses bounded text; it falls back to a range when needed. Provenance is assembled from document citations and one level of referenced-document source pointers, not from reading raw source bodies into the answer context. SRC-1: `packages/core/src/search/index.ts`, `packages/core/src/evidence/index.ts`.

The excerpt budget defaults to 400,000 characters, with compact 256,000 and large 1,000,000 presets and a positive explicit override. Remaining characters are shared among remaining selected items; actual returned characters reduce the remainder. Metadata, candidates, provenance and host conversation are outside that body budget. Code returns continuation cues for truncated ranges; the at-most-one automatic follow-up limit is agent policy, not a read-call counter. The core result is ephemeral; no evidence brief write-back is implemented in the planner. SRC-1: `packages/core/src/evidence/index.ts`, `packages/cli/src/commands/query.ts`.

> const itemLimit = Math.ceil(remainingChars / remainingItems);
> --- `packages/core/src/evidence/index.ts`

An explicit yes on the no-match permission branch admits a derived conversation answer as one ordinary concept plus an index link. Silence/no persists nothing under this protocol. This is foreground-agent curation of conversational input into knowledge, not automatic capture of an interaction trace, and not user certification of correctness. Its later delivery uses exactly the ordinary wiki route, without a special learning/authority tier. Reasons survive only if authored into the page; source raw turns are not retained by write-back. SRC-1: `packages/agent-pack/templates/okf-harness/references/answer.md`.

#### On [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval)

Search is question/metadata/body lexical selection returning access cards, not full evidence bodies. Read is caller-directed document/section/range selection; a target ID alone does not make it relevance-ranked. The read result exposes metadata, outlines, citations, warnings and selected text. Evidence withholding is not applied as a universal access rule here. Legacy `log.md` is an explicit exception to direct wiki reading, while the index remains readable navigation. Source bytes are not a normal wiki read target. SRC-1: `packages/core/src/search/index.ts`, `packages/core/src/read/index.ts`, `packages/cli/src/commands/query.ts`; see [MEM-CLM-log-exclusion](#mem-clm-log-exclusion).

#### On [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery)

Checkpoint tree contents and judgment bodies have different read-back channels. Git restore changes the local files that later commands consume; history returns judgments that a caller can interpret. The code retains reasons without proving they explain a successful change. Checkpoints can be empty, baseline initialization retains preexisting state, and restore creates another commit rather than discarding successor history. A caller chooses checkpoint/admission and restore ID; core rejects empty judgments or unsafe restore state but does not judge semantic fitness. Human-versus-model admission remains unresolved for a generic caller. SRC-1: `packages/core/src/recovery/index.ts`.

This is broad, explicit recovery, not a trace-derived summary, critic-generated procedure or automatic improvement loop. It can restore prior instructions/configuration as well as knowledge; this establishes a recovery authority path without establishing exercised self-improvement.

## Write side

Acquisition, semantic authorship and admission are not interchangeable. Registration physically writes raw bytes or a URL pointer and appends the manifest; core rejects malformed state and unsupported input, reuses existing entries and deletes a newly written raw file if manifest append fails. No claim-level approval occurs. The ingest plan returns metadata suggestions; the host then reads material and writes meaning under the source-preservation and bounded-edit instructions. Local prose writes precede post-edit checking. These findings are in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and its annotation, with retained parts [MEM-OBJ-source-bytes](#mem-obj-source-bytes), [MEM-OBJ-url-metadata](#mem-obj-url-metadata), [MEM-OBJ-manifest](#mem-obj-manifest) and [MEM-OBJ-wiki-content](#mem-obj-wiki-content).

Maintenance has two outputs, not one: agent revision of affected claims and code acknowledgment of an exact edge. The guidance permits destructive replacement when justified and asks the agent to report which claim will no longer be served. It does not delete old raw sources. The mechanical append can reject an acknowledgment while leaving saved wiki changes in place; it can also accept a note without observing any changed claim. [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile), [MEM-OBJ-reconciliation-edges](#mem-obj-reconciliation-edges), [MEM-OBJ-reconciliation-notes](#mem-obj-reconciliation-notes).

Conversation write-back is a separate admission rule. User explicit acceptance is required before the agent writes one concept and its index link; it is permission to keep the answer, not verification. The write-back is derived knowledge, not a raw trace or a special source class. Ingest can later create a sourced revision that disagrees with this unsourced knowledge; the ingest workflow explicitly requests disclosure of that divergence. The inspected policy supports representing a contradiction, but cannot prove any agent did so. [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), [MEM-CLM-provenance-signal](#mem-clm-provenance-signal). SRC-1: `packages/agent-pack/templates/okf-harness/references/ingest.md`.

> An ingest that resolved a contradiction against a page does not stop again; the user has already adjudicated.
> --- `packages/agent-pack/templates/okf-harness/references/ingest.md`

Check and graph generation are deterministic transformations with different results. Check returns diagnostics without editing knowledge; graph saves derived navigation data rather than new semantic claims. Neither is a semantic correction engine. No later evidence consumer is established for persisted graph JSON; evidence uses freshly derived graph data. [MEM-RTE-workspace-check](#mem-rte-workspace-check), [MEM-RTE-graph-report](#mem-rte-graph-report).

Static workflow provisioning and runtime-pin adoption have already been separated from experience memory in [RT-RTE-guidance-install](runtime.md#rt-rte-guidance-install) and [RT-RTE-runtime-launch](runtime.md#rt-rte-runtime-launch). Automatic managed-file replacement/legacy-skill cleanup changes delivered instructions under ownership checks, not under an experience-derived proposal evaluator. It cannot be used as evidence that raw operating traces become improved instructions. Git baseline, changed/unchanged checkpoint and restored-tree forms remain distinct from trace-fed distillation; their retained reasons and consumers are described in the recovery annotation.

No automatic trace-to-summary-to-later-model update is established in the inspected CLI registration, query, snapshot, graph, check and recovery functions or supplied host synchronization account. This is a bounded inspection result, not a repository-wide or host-wide absence claim. The positive conversation-to-wiki route remains established as a requested, human-admitted transformation; opaque host compaction and model internal updates remain uninspected.

## Read-back

The ordinary semantic consumer is the host agent answering a later question. The evidence planner's selection and transport are wired; compliant semantic dependence is unobserved. Wiki text gives evidence authority through agent interpretation, while symbolic citation/source data govern selection, provenance and risk warnings. Core neither makes prose true nor confers higher instruction priority on retrieved wiki content. [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context).

Requesting evidence is not an unsolicited memory push. The planner automatically selects once requested, but the host/user initiated the route. Similarly, source metadata drives an ingest-plan recommendation only after an ingest-plan request. Direct read delivers caller-targeted content without ranking it for relevance; history exposes caller-requested judgments. Static skill discovery may be host-triggered, but newly installed unchanged templates are provisioning, not accumulated read-back. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval), [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery), [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance).

Withholding is limited to its actual consumer. Conformance failures can reject evidence planning; invalid config/manifest can return successful withheld evidence; missing/drifted raw data seal source-linked pages and incoming citation dependents. The code does not recursively traverse every semantic derivation. Direct search/read can still deliver material, and the agent is separately asked to widen withholding where prose carries contamination. Pending revision currency does not itself trigger the same gate. [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary), [MEM-CLM-currency-evidence](#mem-clm-currency-evidence).

Working-context control has two visible layers. Code keeps most retained material outside the current evidence result by lexical selection and excerpt budgeting; it leaves the files reachable through explicit later reads. The foreground agent is asked to load workflow references just in time and stop after at most one continuation-cue read, leaving other reference bodies out until their workflow begins. These mechanisms limit additions; neither removes already accumulated host turns or injected text. No separate worker frame or frame-pop return is implemented by the inspected paths. In the stack-frame lens, the CLI call has a selected return but does not establish an isolated model frame that is later discarded. Files remain external by value until read, and an ID/path does not imply a live pointer in the host window. Actual trimming, summaries, preserved tails and reload of host-evicted state are uninspected external responsibilities, not properties inferred from excerpt bounds. SRC-1: `packages/core/src/evidence/index.ts`, `packages/agent-pack/templates/okf-harness/SKILL.md`; supplied just-in-time passage in [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance) and runtime account.

## Integration issues

1. **Currency versus evidence eligibility needs an explicit distinction.** [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) correctly limits acknowledgment, but an account that equates clearing revision currency with unsealing answer content would be wrong. [MEM-CLM-currency-evidence](#mem-clm-currency-evidence) supplies implementation and test-definition support: pending revisions can remain retrievable. Consequence: do not classify every maintenance warning as evidence rejection, or the ledger as semantic validation.
2. **Legacy logs qualify the supplied coverage inventory.** Boundary mentions example wiki/log state and runtime broadly describes direct wiki retrieval. [MEM-CLM-log-exclusion](#mem-clm-log-exclusion) adds the explicit reserved/unreadable exception and the inconsistency with permitted log edits. Consequence: log presence/writes do not establish a trace-fed answer-memory route. No supplied record explicitly asserted the contrary, so this is a scope qualification, not a demonstrated false positive.
3. **Conversation origin is not authenticated.** [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) correctly describes accepted citation-empty write-back; [MEM-CLM-provenance-signal](#mem-clm-provenance-signal) limits the reverse inference. Consequence: the disclosure convention cannot establish the actual origin of every empty-provenance page.
4. **Retained reasons have unequal later consumers.** [MEM-OBJ-reconciliation-notes](#mem-obj-reconciliation-notes) retains reasons without an established semantic read-back route; [MEM-OBJ-checkpoint-judgment](#mem-obj-checkpoint-judgment) exposes them through history. Wiki rationale is optionally authored and only selected if it falls within delivered excerpts. Consequence: neither persistence alone nor a nonempty note proves iterative criticism or learning. Whether a host later reads ledger notes for their meaning is unresolved by inspected callers.
5. **Caller and historical author control remain local unknowns.** Generic checkpoint/reconcile callers do not identify a human approver, and existing wiki page authorship is not captured by retrieval. Native host entry does not guarantee delivery of detailed workspace write-back/provenance rules, per [RT-RTE-guidance-install](runtime.md#rt-rte-guidance-install). Consequence: do not convert authoring or a workflow-start request into per-content human admission, or assume cross-integration policy parity.
6. **Duplicate check.** No new route redeclares supplied ingest, evidence, direct-read, reconciliation, recovery, installation or launcher identities: those receive annotations or citations. The new graph/check routes are distinct operations absent from the supplied record declarations. New objects identify retained operative parts, not alternative names for those routes. No possible duplicate requiring supersession was found after comparison.

## Limitations and checks

The registered checkout HEAD was rechecked as `0dd4f806c454a68088c5a3e64b4cbebbe2c216be`; `git status --short` was clean. New source reads stay in SRC-1 and use implementation or doctrine/design evidence only. CLI maintenance-loop assertions were read, not run; they support intended behavior, not observed execution. No target command, test, provider, installer or example was executed. The supplied worker rules, member types and record contract govern this output; repository authoring skills and prior analyses were not used.

Inspection was mechanism-selective rather than a complete security or distribution audit. Exact read-option edge behavior, all lint rules, all integrations and filesystem races were not exhaustively traced. This prevents universal access-control, host-parity or reliability conclusions. Host weights, session state, permission grants, compaction and actual loaded payloads remain uninspected. Source-grounded wiring establishes available memory operations; it does not establish activation, successful learning, iterative theory criticism or exercised self-improvement. The known retained conversational knowledge route must not disappear behind those limits.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed for this member and empty correction-answers file. This establishes checked structure, identity, citations and quotation occurrence, not semantic correctness or job acceptance.
