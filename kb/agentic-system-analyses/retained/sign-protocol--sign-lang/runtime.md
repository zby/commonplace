---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SIGN runtime baseline: deterministic CLI preparation, file-level bundle selection, change signals and the external agent-consumption boundary."
run-id: AAS-2026-11-09-sign-lang-379ffbdd642c-01
reviewed-boundary: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
---

# sign-lang runtime report

## Runtime account

### What runs, and what does not follow from it

SIGN ships a knowledge notation and a Node.js command-line tool, not a model-turn scheduler. The installed `sign` entry point dispatches `validate`, `compile`, `coverage`, `drift`, `diff` and `import`. The package requires Node >=18 and names six Node test files; the inspected CI runs `npm test` on Node 18, 20 and 22. Neither that configuration nor this analysis establishes passing tests. All findings below are implementation or doctrine/design evidence from SRC-1 at the boundary pin. No target execution, supplied execution trace or causal experiment supports activation or benefit. Additional inspection under the same source covered the complete parser, rules, CLI, compiler, validation, coverage, drift and diff modules, package/CI wiring, README, skill reference and local architecture/standards/configuration (SRC-1, `validator/package.json`, `.github/workflows/ci.yml`, `validator/bin/sign.js`, `.agent/sign/canon.source.json`).

The consequential claimed work is giving agents structured domain rules and provenance without supplying the entire corpus at every invocation. This is an integration contract, not an implemented provider interface. The README declares:

> SIGN is the contract layer between a governed knowledge graph and the agents that consume it. It expresses structure, relationships, inference rules, constraints, clusters, and provenance in a form agents can reason over — not just retrieve from.
> --- `README.md`

The README's `systemPrompt` and `get_canon_doc` examples leave the host to inject the index, resolve a document ID, call a model and execute any resulting action. [RT-CLM-agent-contract](#rt-clm-agent-contract) and [RT-BAP-canon-guidance](#rt-bap-canon-guidance) preserve that intended authority without claiming a live consumption path. No distributed-parametric component is invoked by the inspected preparation toolchain. External model identity, weight changes, endpoint mutability, granted tools and isolation envelope are uninspected because the enclosing consumer is outside the frozen artifact boundary; these cannot be inferred from SIGN syntax.

### Ordinary invocation: source to compiled files

For `sign compile --source <path> --output <path>`, the principal is the invoking process/user, not an autonomous agent. CLI arguments supply source and destination; `.agent/sign/canon.source.json` names this repository's source/dist locations, but the inspected CLI does not load that configuration. The next-step owner throughout compilation is JavaScript control flow. Source discovery recursively collects `.sign` files for a directory; a directly supplied file is accepted without an extension test. Parsing recognizes document IDs, status, audience, version, summary, links, anchor patterns, declared predicates, edges, inference-field presence and clusters. These are transient structured objects, not a graph inference executor (SRC-1, `validator/bin/sign.js`, `validator/src/parse.js`).

[RT-RTE-compile-canon](#rt-rte-compile-canon) traces admission and effects. Parse errors plus rule errors abort before writes. Strict link resolution checks against all parsed document IDs, then the compiler selects `doc.id && doc.status === 'active'`. It builds index entries with identity, links, optional summarized anchor and summary; it hashes the assembled bundle and writes index, bundle, JSON manifest and checksum. The filesystem is the executor and persistence boundary. No lease, lock, concurrent-writer coordination, transaction or rollback surrounds these four sequential writes in `compile`; a later write exception can leave earlier artifacts updated. Top-level CLI exception handling reports the error and exits 2; repair/retry belongs to the caller (SRC-1, `validator/src/compile.js`, `validator/bin/sign.js`).

The preparation window is selected by code rather than by an LLM: index rule bodies are omitted, anchor excludes are omitted, and at most four distinct include patterns are displayed with a remainder count. Full documents remain in source/bundle for a host to retrieve. This is static context preparation, not turn trimming, sub-agent context isolation or observed model-side retrieval. Identity, status and version are parsed text, not authenticated principals. Hashes provide bundle-content identity if a consumer checks them; they do not authenticate an author or enforce agent compliance (SRC-1, `validator/src/compile.js`, `README.md`).

### Forcing cases and guarantee boundaries

Four source-traced cases challenge broad guarantees; they are not runtime experiments.

1. **Mixed-status source file.** The parser supports multiple `@doc` headers in one file. The active predicate applies to index/manifest entries; bundle assembly copies the whole raw file whenever it contributes an active ID. Thus a supported file containing active and draft/deprecated documents can pass both into the bundle. The guarantee is file-contribution selection, not per-document exclusion. Strict links also resolve before filtering, against all IDs, while links from active to inactive/deprecated documents produce only warnings. Links to known non-active IDs need not be retrievable from an active-only external resolver. See [RT-RTE-compile-canon](#rt-rte-compile-canon) (SRC-1, `validator/src/parse.js`, `validator/src/rules.js`, `validator/src/compile.js`).
2. **Validation is not compilation admission.** `validate` uses non-strict links. More sharply, malformed headers can accumulate parse errors without creating documents; the zero-document branch returns `ok: true` before using those errors to compute `ok`. A file containing only a malformed `@doc` line is reachable through supported direct-file input and can therefore produce an error diagnostic and a successful validation result together. This does not bypass compilation, which checks its accumulated errors before writes. See [RT-RTE-validate-source](#rt-rte-validate-source) (SRC-1, `validator/src/parse.js`, `validator/src/validate.js`, `validator/src/compile.js`).
3. **Maintenance signals are not mandatory admission gates.** `coverage`, `drift` and `diff` use `loadDocs`, which discards each file's `parseErrors`, without calling `validate` or `runAllRules`. Coverage considers anchored parsed documents regardless of active status. Drift resolves currently present files, then intersects them with Git changes between the given ref and HEAD; deleted governed files absent from the current walk and uncommitted source changes do not receive universal drift coverage. See [RT-RTE-source-signals](#rt-rte-source-signals) (SRC-1, `validator/bin/sign.js`, `validator/src/coverage.js`, `validator/src/drift.js`).
4. **CLI diff does not enumerate historical deletions.** Its historical side is reconstructed by iterating current documents and current file paths, assigning current IDs. A removed document/file need not enter either list; a historical read failure becomes empty text, not necessarily a fatal error. The pure `diffCorpus` API likewise iterates only `afterDocs`, although it handles an explicitly missing before ID as additive. Classification is a textual signature comparison of seven sigils, not a proof of unchanged meaning, semantic version compliance or complete deletion detection. See [RT-RTE-corpus-diff](#rt-rte-corpus-diff) (SRC-1, `validator/bin/sign.js`, `validator/src/diff.js`).

The load-bearing enforced guarantee is narrower than “governed knowledge”: the compiler owns a pre-write rejection rule for recognized parse/rule errors on its own path. **Guarantee strength: invariant**, scoped to that control-flow check; **implementation conclusion status: wired**; **operation conclusion status: uninspected**. It requires readable stable inputs, writable outputs and Node filesystem behavior, not a model provider contract. Direct parser/rule APIs, the other commands, raw authored files, external retrieval and `import` do not pass through that gate. The index-budget check is an invariant over its chars/4 estimate, not a tokenizer-independent 400-token bound: headers and actual tokenizer behavior are outside the estimate. Anchor inclusion is a locator; `@constraints` prose and inference conclusions are not executed by this gate (SRC-1, `validator/src/rules.js`, `validator/src/compile.js`, `validator/src/parse.js`).

### Change and capability boundaries

Source edits are supplied by an unspecified author/caller. Compilation admits their structured projection and raw contributing files after fixed software checks; it has no human approval record, semantic reviewer, automatic source repair or version-bump enforcement. The local standards name CI, review and ADRs as intended enforcement, but the inspected CI only wires `npm test`; that is not evidence of each content change being human approved (SRC-1, `.agent/sign/src/SL-STANDARDS.sign`, `.github/workflows/ci.yml`). Drift and diff emit signals to a caller/platform; they do not land revisions. `sign import` discovers and spawns a separate package, inheriting stdio, and returns its status. Its implementation and grant decisions are outside this source, so neither imported content quality nor an approval/isolation guarantee is established ([RT-RTE-import-delegation](#rt-rte-import-delegation)).

The capability surface includes arbitrary caller-selected local read/write paths and Git subprocesses, plus execution of a discovered importer using the current Node executable. The current grant set is the host process's OS permissions and available paths; no SIGN-specific sandbox or approval mediator appears in these inspected paths. This is not a claim about an external deployment's isolation. Changes to executable modules, specs or external importer installations are operator/developer actions, not an inspected self-modifying runtime route. Retained-knowledge details and epistemic properties are left to their specialist members; persisted compilation by itself establishes neither learning nor exercised self-improvement.

## Shared records

### Components

#### RT-CMP-validator
Label: sign-validator deterministic toolchain

Source-native identity: package `sign-validator` version `1.0.0`, with bin `sign` and CommonJS modules. Representational form: symbolic JavaScript control flow and structured parsed objects. Storage substrate: repository source/package files, transient Node memory and caller-selected filesystem outputs. It runs fixed parsing/rule/compilation logic; no model parameters participate in the inspected modules. SRC-1, `validator/package.json`, `validator/bin/sign.js`, `validator/src/parse.js`, `validator/src/rules.js`, `validator/src/compile.js` supply implementation evidence.

> "bin": {
>     "sign": "./bin/sign.js"
>   },
> --- `validator/package.json`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-compile-canon
Label: Compile source into canon artifacts

Endpoints/progression: caller source path → recursive/direct-file parser → all-document rules with strict links → active identity selection → index/raw bundle → hash/manifest → output files. Owner and decision role: code admits or rejects; caller chooses paths and authored source. Human versus machine source authorship and per-content human approval are unresolved. Operating mode is open caller-selected compilation, not a trial curriculum. Answer oracle: inapplicable — fixed structural checks have no expected agent answer/reference outcome. No model judgment is called. Guidance is fixed JavaScript rules and parsed fields, not generated criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `{ok, errors, warnings, summary}` to API caller; CLI prints diagnostics and exits 0/1 for result, or 2 on uncaught exception.
- Later read-back: four persisted artifacts are available to later filesystem consumers; the repository does not implement their later model loading.
- Delegated visibility: inapplicable — compilation does not delegate model work; artifacts are exposed to whoever can read the output path.
- Selection predicate: index and manifest select identified active documents; bundle selects whole files contributing any active document ID.
- Invalidation or expiry: same filenames are overwritten on a subsequent successful compile; timestamps/hash identify builds, not automatic expiry or deletion of stale earlier files after a failed compile.
- Activation or effect: source-derived index/bundle/manifest/checksum writes are wired; agent behavior changes are unobserved.
- Evidence limits: implementation only; no execution or host retrieval supplied. File-level passthrough limits active-only claims; nontransactional writes limit recovery guarantees.

Admission trigger is the command/API invocation; proposed change is replacing the compiled corpus with caller-supplied source. The software can veto on recognized errors; warnings do not veto, and humans have no wired per-content decision point here. No implemented rollback is present in this function; the caller must preserve/rebuild previous artifacts. This admits knowledge artifacts, not executable extensions. Minimum SRC-1 evidence (`validator/src/compile.js`):

> const validationResult = runAllRules(allDocs, { strictLinks: true });
> --- `validator/src/compile.js`

> if (errors.length > 0) {
>     return {
>       ok: false,
>       errors,
>       warnings,
>       summary: `compile aborted — ${errors.length} error(s) must be resolved`,
>     };
>   }
> --- `validator/src/compile.js`

> const activeDocs = allDocs.filter(({ doc }) => doc.id && doc.status === 'active');
> --- `validator/src/compile.js`

> const hasActiveDocs = file.documents.some(d => d.id && activeIds.has(d.id));
>     if (!hasActiveDocs) continue;
>
>     // Re-read and annotate the raw file content
>     const raw = fs.readFileSync(file.filePath, 'utf8');
>     bundleParts.push(`# --- ${path.basename(file.filePath)} ---`);
>     bundleParts.push(raw.trimEnd());
> --- `validator/src/compile.js`

Multi-document reachability is supported by `startDoc` pushing documents and the loop handling every `@doc` in SRC-1, `validator/src/parse.js`. Compilation also rereads raw files after parsing: without an external stable-input contract it is not a snapshot transaction. Index compression deliberately omits full anchor exclusions:

> // include list is capped. (RFC §1.4)
> const INDEX_ANCHOR_MAX = 4;
> --- `validator/src/compile.js`

The rule-based budget estimates only emitted per-document fields; no guaranteed tokenizer is used:

> const estimatedTokens = Math.ceil(indexChars / 4);
> --- `validator/src/rules.js`

#### RT-RTE-validate-source
Label: Validate parsed source

Endpoints: caller path → parser → parse diagnostics → ordinarily non-strict rules → diagnostics/result. Owner: code; caller determines source. It checks structural admission candidates without changing them. Operating mode: open validation request; answer oracle: inapplicable — no expected agent output supplied. Computational rejection applies only to computed `ok`; no human veto/approval is represented. SRC-1, `validator/src/validate.js`, `validator/src/rules.js`, `validator/src/parse.js`, `validator/bin/sign.js`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: validation object; CLI prints warnings/errors and uses `result.ok` for 0/1 exit.
- Later read-back: inapplicable — validation does not persist source revisions or a retained result store.
- Delegated visibility: inapplicable — no delegated worker or provider.
- Selection predicate: all discovered parsed documents; directory traversal selects `.sign` filenames while a direct file has no extension filter.
- Invalidation or expiry: inapplicable — per-call result only.
- Activation or effect: diagnostics and process status, not semantic enforcement on an agent.
- Evidence limits: no execution evidence; zero-document early success and warning-only links prevent treating a pass as compilation readiness.

The zero-document branch does not reset parse errors, but explicitly sets success:

> if (allDocs.length === 0) {
>     warnings.push(`no documents found in ${sourcePath}`);
>     return { ok: true, errors, warnings, summary: 'pass — 0 documents' };
>   }
> --- `validator/src/validate.js`

Malformed headers can reach that branch:

> if (!header) {
>           parseErrors.push(`line ${i + 1}: malformed @doc header`);
>           continue;
>         }
> --- `validator/src/parse.js`

For ordinary documents, missing links differ between validation and compilation:

> if (strictLinks) errors.push(msg);
>       else warnings.push(msg);
> --- `validator/src/rules.js`

This is not a guarantee that cluster/rule references resolve either: those branches add warnings even in strict mode (SRC-1, `validator/src/rules.js`). Inference-field checks test prefix presence, not entailment or human provenance. General `@constraints` bodies have no execution case in `processBlock` (SRC-1, `validator/src/parse.js`).

#### RT-RTE-source-signals
Label: Coverage and source drift signals

Endpoints: `coverage` or `drift` caller → `loadDocs` parsed document/file pairs → repository walk/glob resolution → coverage report or Git-change intersection. Code owns resolution and signal generation; a later review owner is external. Coverage uses include union minus excludes on current files, reports overlaps/ungoverned prefixes and returns 0. Drift compares `since..HEAD`, emits signals and exits 1 when any exist, 0 otherwise, 2 on a Git error (SRC-1, `validator/bin/sign.js`, `validator/src/coverage.js`, `validator/src/drift.js`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: coverage fraction/prefixes/overlaps, or drift document IDs and changed artifacts with checked count; CLI prints these signals.
- Later read-back: inapplicable — these functions do not persist revised knowledge or a review queue.
- Delegated visibility: Git subprocess receives root/ref; external platform review is not invoked here.
- Selection predicate: parsed documents with nonempty anchor includes, regardless of lifecycle status; current filesystem walk skips `.git`, `node_modules`, `.hg`, `.svn`; drift additionally requires changed governed files and unchanged governing file.
- Invalidation or expiry: inapplicable — recomputed per call against caller root/ref and current walk.
- Activation or effect: report/exit status can inform caller workflow; no automatic source update.
- Evidence limits: current-file intersection does not cover every deletion; Git comparison excludes uncommitted changes; unreadable walk directories are silently skipped. Coverage is a path-binding metric, not proof of correct governance.

The CLI's parser projection omits parse errors:

> function loadDocs(sourcePath) {
>   return parseSource(sourcePath).flatMap(file =>
>     file.documents.map(doc => ({ doc, filePath: file.filePath }))
>   );
> }
> --- `validator/bin/sign.js`

Drift's decisive consumer receives only currently governed files:

> const governed = resolveAnchor(doc.anchor, allFiles);
>     const changedArtifacts = [...governed].filter(f => changed.has(f)).sort();
>     if (changedArtifacts.length === 0) continue;
> --- `validator/src/drift.js`

No admission or repair occurs here; the source explicitly separates review ownership:

> // (no platform dependency); the platform layer turns these signals into review workflow.
> --- `validator/src/drift.js`

#### RT-RTE-corpus-diff
Label: Classify corpus change

Endpoints: CLI current parsed documents → historical raw files by current paths via Git → `diffCorpus` textual classification → printed non-additive changes and drift signals. Direct API callers can supply explicit before/after arrays; they do not thereby gain deletion detection, because the classification loop iterates after documents only. Owner/decision policy: deterministic comparison, not model semantic judgment. Operating mode: open caller-selected revision comparison. Answer oracle: inapplicable — before text is a comparison baseline, not a reference answer. No human content admission decision, veto or rollback is wired by the classifier. Guidance is the fixed seven-sigil meaning signature and anchor-set comparison; persisted source edits remain the caller's responsibility (SRC-1, `validator/bin/sign.js`, `validator/src/diff.js`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: API change classes and dropped-pattern signals; CLI prints non-additive changes and exits 1 only when meaning-breaking is found, otherwise 0; historical-load outer failures exit 2.
- Later read-back: inapplicable — no revised source or persistent classifier store is written.
- Delegated visibility: Git receives ref/current relative file paths; no model or reviewer receives content through this implementation.
- Selection predicate: current documents with IDs; meaning signatures compare `def`, `include`, `exclude`, `rules`, `rel`, `constraints`, `infer`; anchor include removal or exclude addition is coverage-narrowing unless meaning-breaking takes precedence.
- Invalidation or expiry: inapplicable — fresh comparison result, no retained decision.
- Activation or effect: signal/exit status only; does not bump versions, block a merge itself or revalidate downstream packages.
- Evidence limits: deletion/rename and read-failure handling limit historical completeness; comments/whitespace normalization and chosen sigils limit semantic interpretation. No executed change examples supplied.

Historical reconstruction's fallback is reachable independently of the outer error branch:

> } catch {
>       raw = ''; // file did not exist at <ref> — treated as a new doc (additive)
>     }
>     out.push({ id: doc.id, raw });
> --- `validator/bin/sign.js`

The classifier only classifies entries that survive into its after input:

> for (const { id, raw } of afterDocs) {
>     if (!beforeById.has(id)) {
>       changes.push({ docId: id, changeClass: 'additive' });   // brand-new doc
>       continue;
>     }
> --- `validator/src/diff.js`

The governance doctrine is broader than this detector:

> Every agent package declaring the affected document must be re-validated before
> production promotion when a breaking change lands.
> --- `spec/skill-reference.md`

That passage establishes a requested downstream obligation, not an implemented production promotion gate in `sign diff`.

#### RT-RTE-import-delegation
Label: Delegate import to sign-ingest

Endpoints: `sign import` arguments → candidate executable discovery → child Node process with `import` and forwarded args → inherited output/status. Owner: caller chooses request; code selects the first existing candidate in three fixed locations (sibling checkout locations before local `node_modules`); external importer owns subsequent transformations. Its content admission, human veto, rejection/rollback and persistent output internals are uninspected because its package is outside SRC-1. Operating mode: open import request; answer oracle: uninspected — external importer not frozen. The proposed capability is running a separately installed ingestion implementation, not generating code or revising the validator itself (SRC-1, `validator/bin/sign.js`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: missing importer exits 127 with install hint; otherwise child status, or 1 when status is null.
- Later read-back: uninspected — any imported artifact persistence/read-back belongs to the external package.
- Delegated visibility: child receives forwarded CLI arguments and inherited stdio; no separate application-level permission restriction is set in this spawn call.
- Selection predicate: first existing executable path among the fixed candidate paths; existence is not package-version or integrity verification.
- Invalidation or expiry: uninspected — external package installation/version policy not supplied; discovery repeats on invocation.
- Activation or effect: child-process execution is wired; ingestion results or benefits unobserved.
- Evidence limits: no external package source or run, so no claim about imported provenance enforcement or sandboxing.

> const res = require('node:child_process').spawnSync(
>     process.execPath, [bin, 'import', ...forwardArgs],
>     { stdio: 'inherit', windowsHide: true }
>   );
>   process.exit(res.status == null ? 1 : res.status);
> --- `validator/bin/sign.js`

### Claims

#### RT-CLM-agent-contract
Label: Agent-oriented structured knowledge contract

Claimed operation: SIGN's index orients each agent invocation and full documents are retrieved on demand; constraints/inference/provenance then guide the consuming agent. Source: SRC-1, `README.md`, `spec/skill-reference.md` (doctrine/design). The source passages in the runtime account and below support intent. They do not establish an actual loader, retrieval success, compliant decisions or causal token savings.

- design conclusion status: claimed
- operation conclusion status: uninspected

> | **Layer 1 — Index** | Injected into every agent system prompt. ~400 tokens for a full corpus. Document identity, status, graph edges, one summary line per document. Orientation without rule text. |
> | **Layer 2 — Full document** | Retrieved on demand via `get_canon_doc(id)`. Agents only pay for documents they actually need. |
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-canon-guidance
Label: Intended canon-to-agent guidance

Consumer: an external agent and its host. Channel: README example inserts compiled index text into `systemPrompt`, then registers a `get_canon_doc` tool whose handler calls an externally provided `canonBundle.getDoc(id)`. Force: intended instruction/domain knowledge through model interpretation, not a validator-mediated constraint on tool actions. Horizon: intended repeated prompt injection and on-demand full-document consumption; actual subsequent invocations unobserved. Index symbolic identifiers/links are fixed-rule compiler outputs; summaries and domain rule text receive their agent-facing meaning through natural-language interpretation. Persisted files are the delivery substrate, not proof of activation. SRC-1, `README.md`, `validator/src/compile.js`; related intent: [RT-CLM-agent-contract](#rt-clm-agent-contract).

- design conclusion status: claimed
- operation conclusion status: uninspected

> You operate under the following knowledge canon:
> ${index}
> Call get_canon_doc(id) when you need full rule text for a document.
> --- `README.md`

The compiler neither selects the external model nor guarantees this channel is used. A deployment may impose stricter retrieval or action controls, but those are not supplied evidence.

## Annotations

none
