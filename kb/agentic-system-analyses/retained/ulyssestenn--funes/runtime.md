---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Funes runtime baseline: external Librarian invocation, retained-library workflow, extraction helpers and mechanical CI at the frozen revision."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
---

# Funes runtime report

## Runtime account

Funes supplies a repository and instructions for a caller-supplied agent, not a model scheduler. Its consequential claimed work is preserving sources, compiling a linked wiki, answering from that wiki and maintaining it. The semantic path is specified in natural language; the executable paths are extraction wrappers and mechanical evaluators. All evidence here is SRC-1 at the frozen revision in [boundary](boundary.md#source-register). No target was executed and no observed run or causal experiment was supplied. Operation, model adherence and benefit remain unobserved. SRC-1, `README.md`, `protocol.md`, `tools/README.md`.

> Use Claude Code, Codex, or any LLM agent that can read and edit files in a repo.
> --- `README.md`

### Ordinary invocation and ownership

A human points a file-capable agent at the repository, supplies a source and asks for ingest. The root entry directs it to the selected library's `AGENTS.md`, which supplies scope and points to `protocol.md`. The external host decides whether these instructions actually reach a model invocation. The Librarian then owns the next step: save raw material, compile a source note, merge or create concept articles, connect topic maps and backlinks, update navigation and mark the registry row compiled, and log the changes. This is [RT-RTE-ingest-compile](#rt-rte-ingest-compile). Library identity is a folder and its local instructions; source identity is a registry row and raw path. There are no shipped run IDs, transaction IDs or task scheduler for this loop. SRC-1, `AGENTS.md`, `starter-library/AGENTS.md`, `protocol.md`, `starter-library/raw/INDEX.md`.

> Each library is governed by its own `AGENTS.md`. **Read that file before acting**
> within the folder.
> --- `AGENTS.md`

On a later question, the same role searches the wiki through its index, source notes and concepts, produces cited answers and saves substantial outputs. Durable output is offered for filing back rather than automatically committed by a software feedback loop: [RT-RTE-wiki-answer](#rt-rte-wiki-answer). Markdown files, indices and the changelog carry state across sessions. The protocol requests session closure; it does not implement atomic multi-file commits, concurrent-writer coordination or retry scheduling. Git affords recovery through history, but ingest itself has no explicit commit step. New-library creation explicitly requests commit and push: [RT-RTE-library-setup](#rt-rte-library-setup). SRC-1, `protocol.md`, `library.md`, `README.md`.

The external model is [RT-CMP-librarian-model](#rt-cmp-librarian-model). The decision policy is interpreted text, not a state machine: [RT-OBJ-protocol](#rt-obj-protocol), [RT-BAP-librarian-instructions](#rt-bap-librarian-instructions). The library is the work product and later context source: [RT-OBJ-library-tree](#rt-obj-library-tree). No fixed context budget, compaction algorithm, eviction rule or separate agent frame is specified in these entry instructions. The explicit context controls are instruction loading, wiki-first search, on-demand file reading and deliberate cross-library traversal. What remains in the model window, and whether a host trims it, is outside the supplied runtime boundary. SRC-1, `AGENTS.md`, `protocol.md`, `README.md`.

### Alternate paths and forcing cases

Four forcing cases bound the guarantees rather than assuming every path passes through one gate.

1. **Direct edits versus instruction rules.** A file-capable host can edit files directly. The raw immutability and citation requirements are protocol obligations, not filesystem protections. Cross-library links require human approval in the protocol, but no executable approval interception is shipped. The libraries share one tree and relative paths, not separate sandboxes. Capability is broad file access supplied by the host; the current grant set and deployed isolation envelope are not supplied. CI's `contents: read` permission applies to its audit job, not the Librarian. SRC-1, `README.md`, `protocol.md`, `.github/workflows/funes-lint.yml`; [RT-CLM-library-guarantees](#rt-clm-library-guarantees).
2. **A structurally valid but shallow or false compile.** The source describes an earlier compile that passed link checks despite templated notes. Current compile lint adds duplicate and echo gates, but cannot establish factual grounding. Link resolution ignores remote URLs and pure fragments; orphan detection is basename occurrence in another Markdown file; frontmatter detection only checks an opening `---`. Compile lint compares selected summary/lead sections and linked takeaway lines, not all article meaning. Thus a green audit is a bounded mechanical result, not a source-fidelity oracle. SRC-1, `tools/check_links.py`, `tools/compile_lint.py`; [RT-RTE-health-audit](#rt-rte-health-audit). The historical episode is attributed reported operation, not a supplied trace.
3. **PDF extraction with a failed page or alternate flags.** The wrapper attempts native text and falls back to OCR below the configured character threshold. It writes successful pages and failure markers, returning 1 on page failures. Contrary to a strong reading of the tool README's description of `--fail-fast`, that flag stops page iteration but still reaches the output write: it does not make output all-or-nothing. `--no-header` omits provenance, `--force` permits replacement of existing output, and output protection is a lexical Path equality check against the input, not a general canonical-path isolation boundary. The helper is not a raw-layer enforcement service. SRC-1, `tools/pdf_text.py`, `tools/README.md`; [RT-RTE-pdf-sidecar](#rt-rte-pdf-sidecar).
4. **Caption retrieval instead of local PDF or text ingest.** The optional helper fetches one selected public video, can list tracks without fetching content, and can select manual-only or generated-only captions. Its output is not automatically registered or compiled. Dependency absence, service blocking or caption errors terminate that command; there is no shipped retry or identity-rotation mechanism. The human/agent must choose a permitted next route. SRC-1, `tools/youtube_transcript.py`, `tools/README.md`; [RT-RTE-caption-fetch](#rt-rte-caption-fetch).

These cases cover instruction-mediated file work, direct helper invocation and the separate CI caller. The tracked tree and all executable helper files were inspected for alternate drivers: no direct model-call, provider-native tool loop, remote worker, extension loader or graph-control driver is shipped ([RT-ABS-model-driver](#rt-abs-model-driver)). Such capabilities may exist in a chosen host; this report does not infer their grants or isolation. No wall-clock performance, extraction accuracy or retrieval-quality measurement is available. PDF per-command timeouts are local reliability controls, not an end-to-end latency bound. SRC-1, `README.md`, `tools/pdf_text.py`, `tools/youtube_transcript.py`, `.github/workflows/funes-lint.yml`.

### Guarantee boundaries and admission

The Librarian owns semantic quality and raw preservation under a **protocol** guarantee; enforcement is model/human interpretation of instructions. CI owns only reported mechanical failures under code rules. Its push/pull-request caller wires both audits without strict compile-depth mode; branch protection and merge blocking are not established. The external contract is a host that loads instructions, supplies appropriate file capabilities and honors human decisions, plus Git/GitHub if versioning and CI are wanted. Raw preservation and grounding therefore have instruction conclusion status **claimed**, implementation enforcement conclusion status **absent** for a universal write barrier, and operation conclusion status **uninspected**. Mechanical gate exit behavior has implementation conclusion status **wired** and operation conclusion status **uninspected**. SRC-1, `protocol.md`, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`.

Routine knowledge edits are proposed and admitted by the Librarian; the human supplies sources/questions but is not required to approve each compile. Cross-library links have a distinct human approval rule. Health checks distinguish safe fixes from proposed fixes. Filing output back is offered to the human. New-library setup confirms structural choices before agent creation. These admission roles, rejected alternatives and recovery limits are recorded on the routes below. No shipped mechanism revises model weights, extends tools dynamically or autonomously deploys product machinery; generic ability of an external coding agent is not attributed to Funes. SRC-1, `protocol.md`, `library.md`, `AGENTS.md`.

## Shared records

### Components

#### RT-CMP-librarian-model
Label: Externally supplied Librarian model

Identity: the LLM used by the user's file-reading/editing agent. Representational form: distributed-parametric model internals, with natural-language instructions as inputs. Storage substrate: external model/provider, unspecified by Funes. Parameters changing during operation: uninspected; no Funes training/update path is shipped. Exact version pinned: no. Mutable endpoint resolving to another model: uninspected because no endpoint configuration is supplied. Provider internals, host tool policy and inference state are outside the acquired source. This does not imply absence of learning through retained files. Evidence: SRC-1, `README.md`, `AGENTS.md`.

> The Librarian preserves the raw record, compiles it into an interlinked wiki, and uses that wiki to produce cited answers, reports, reading plans, comparisons, routines, syntheses, and other reusable outputs.
> --- `README.md`

### Operative objects

#### RT-OBJ-protocol
Label: Librarian Protocol and entry instructions

Identity: shared `protocol.md`, reached through root and per-library `AGENTS.md`; the local file supplies scope and deviations. Representational form: natural-language operating instructions and illustrative Markdown templates, interpreted by the external agent. Storage substrate: Git-tracked Markdown. These static instructions are not themselves read-back accumulated through use. Changes to local instructions during setup are covered separately below. Evidence: SRC-1, `AGENTS.md`, `starter-library/AGENTS.md`, `protocol.md`.

> **Operating manual:** follow the shared **[Librarian Protocol](../protocol.md)**
> (ingest → compile → Q&A → health-check, conventions, templates). Link style:
> markdown relative links. No deviations from the standard structure.
> --- `starter-library/AGENTS.md`

#### RT-OBJ-library-tree
Label: Managed library tree

Identity: one top-level library, represented by `starter-library/` in the frozen tree. Natural-language material comprises raw source text, compiled prose, outputs and maintenance reports; symbolic organization comprises paths, Markdown link targets, registry status and index structure consumed by tools or navigation. Binary source files are retained originals, with derived text sidecars on the extraction path. Storage substrate: ordinary repository files; Git provides optional version history. This container does not assert one shared revision mechanism for every part: raw content is instructed immutable, registry/index entries mutable, wiki merged, outputs optionally filed back and changelog append-only. Evidence: SRC-1, `protocol.md`, `starter-library/raw/INDEX.md`, `starter-library/wiki/INDEX.md`, `starter-library/meta/CHANGELOG.md`.

> _The wiki is empty so far. As sources are ingested and compiled, topics,
> concepts, and source notes will be listed below._
> --- `starter-library/wiki/INDEX.md`

### Routes

#### RT-RTE-ingest-compile
Label: Source ingest and wiki compilation

Endpoints and progression: human/chat or dropped file → Librarian → verbatim raw persistence → source note → concept merge/create → topic/backlinks → index, registry and changelog. The Librarian decides decomposition and merging under the protocol. File effects persist without an executable transaction coordinator. Source identity is carried by raw filename, registry and links. Evidence: SRC-1, `protocol.md`, `starter-library/raw/INDEX.md`.

> 1. Source note in `wiki/sources/` — summary, key takeaways, link to the raw file.
> 2. Extract ideas → create/update **concept** articles; merge rather than duplicate.
> 3. Add **bidirectional** backlinks: source ↔ concepts, concept ↔ related concepts.
> 4. Slot concepts under a **topic** map (create one for a genuinely new theme).
> 5. Update `wiki/INDEX.md`; mark the source `compiled` in `raw/INDEX.md`.
> 6. Log to `meta/CHANGELOG.md`.
> --- `protocol.md`

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested persisted raw and compiled files, registry/index updates and session summary; no structured API result is defined.
- Later read-back: compiled wiki and navigation are intended inputs to later Q&A and maintenance invocations; source links retain a route back to originals.
- Delegated visibility: uninspected — no delegate context contract is supplied by these instructions.
- Selection predicate: user-supplied/new sources, then Librarian judgment of ideas, existing concepts and topic fit; no exact retrieval algorithm is shipped.
- Invalidation or expiry: no timed expiry; merge/update concepts and repair links on rename, while raw content is instructed immutable.
- Activation or effect: instructions request source abstraction and multi-file writes; delivered context changing agent behavior is not observed.
- Evidence limits: source text establishes requested behavior, not semantic extraction, successful persistence or grounded results in an actual run.

Admission: open requests, not a bounded curriculum. The human supplies source content; the Librarian proposes and admits ordinary wiki edits without per-content approval. Guidance requires source-specific substance, merging and citations. Cross-library connections require human approval before both forward link and reciprocal backlink. The human can reject that proposal; the instruction supplies no machine veto on a direct write. No expected-answer oracle is provided; source material is evidence, not a predetermined answer key. Recovery is editorial redo, index/link repair and available Git history, not automatic rollback. What persists is raw material, derived articles, navigation and change records. This route does not establish revision of the Librarian's method or model. SRC-1, `protocol.md`.

> - **Propose, then write.** When compiling reveals a strong, substantive tie to
>   another library, propose it to the human and add it after approval. Do not
>   silently add loose "see also" associations.
> --- `protocol.md`

#### RT-RTE-wiki-answer
Label: Wiki answer and output filing

Endpoints and progression: human question → Librarian wiki search → cited answer → substantial output file → offer to file durable parts back into wiki. The agent owns search, synthesis and proposed durability judgment; human response to the offer governs the requested follow-up. Evidence: SRC-1, `protocol.md`.

> **Q&A:** search the wiki first (INDEX → sources → concepts); answer with
> relative-link citations; say so plainly if it isn't covered. Write substantial
> outputs to `outputs/` and offer to file durable parts back in.
> --- `protocol.md`

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: cited answer and, for substantial work, a requested file under outputs; uncertainty is to be stated if wiki coverage is missing.
- Later read-back: saved output may supply durable content for subsequent wiki filing; the wiki itself is retained context from earlier compilation.
- Delegated visibility: uninspected — no delegation boundary or return payload is defined.
- Selection predicate: question-driven wiki-first search, INDEX then sources then concepts, with cross-library navigation informed by advertised connections.
- Invalidation or expiry: inapplicable — no output expiry or answer-cache invalidation mechanism is specified; wiki changes require editorial upkeep.
- Activation or effect: requested consumption of article content in answer generation; no trace demonstrates reliance on any particular retained passage.
- Evidence limits: no populated wiki or answer trace is supplied; citations and delivery do not prove truth or behavioral activation.

Admission: open-ended human requests. Agent authors the output and proposes filing; the offer is not an implemented approval gate or automatic knowledge-write trigger. Later wiki edits follow compile conventions. There is no expected-answer oracle. Rejection can occur through the human declining the offer; no automatic quality-based rollback exists. Guidance is wiki-first answering, relative citations and explicit noncoverage; outputs and admitted durable findings persist. SRC-1, `protocol.md`.

#### RT-RTE-health-audit
Label: Editorial health check and mechanical CI

Endpoints: human request/periodic Librarian review → editorial audit and dated health report → safe fixes or proposals; independently, GitHub push/pull request → syntax check → link/orphan/frontmatter audit → compile lint → job result. The two Python CLIs select a library root or discover child directories with `wiki/`. These are symbolic consumers of file text, paths and numeric thresholds, not model-based fact checking. Evidence: SRC-1, `protocol.md`, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`.

> Both linters run in CI; duplicate,
> contradiction, grounding, and gap review beyond them remains editorial.
> --- `protocol.md`

> return 1 if gate_problems else 0
> --- `tools/compile_lint.py`

- implementation conclusion status: wired
- editorial conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: stdout findings and nonzero exit for mechanical problems; requested editorial path writes a dated report and fixes safe items or proposes others.
- Later read-back: requested reports under meta/health and updated articles/indexes are available to later review; CI logs alone are not a shipped automatic behavior-shaping write route.
- Delegated visibility: GitHub job receives the checked-out repository; separate-agent editorial review visibility is uninspected because no such host mechanism is specified.
- Selection predicate: Markdown files under root; link audit exclusions; source/concept sections for duplicate, echo and depth checks; editorial audit scope follows the protocol.
- Invalidation or expiry: rerun on new push/pull request or local request; no stored pass certificate, report expiry or incremental invalidation mechanism is shipped.
- Activation or effect: implemented exit codes report failures to the caller; non-strict advisories do not fail CI. Semantic edits remain requested agent actions, not linter writes.
- Evidence limits: no successful job trace, branch-protection configuration or editorial outcome is supplied; code establishes only the configured checks.

Decision roles: the Librarian diagnoses semantic issues and decides safe fixes; the human receives proposals for the rest. Python rules decide mechanical findings; GitHub consumes their status. The routines have no expected-answer oracle: current files, link existence, n-gram overlap and word counts are measured references, not gold semantic outcomes. Mode is ordinary repository maintenance. Triggered improvement objective is library coherence and extraction depth; proposals are guided by protocol conventions and reports. Rejection is through failed checks or human response, not a demonstrated merge barrier. Scripts do not alter files; agent fixes can be rejected/revised and Git history can support recovery. SRC-1, `protocol.md`, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`.

The compile policy deliberately separates gates from proxies: 8-gram duplication, default pair overlap 0.85, template fraction 0.3 with at least five owners, and linked-concept echo comparisons gate; default 120-word stub floor and raw/wiki ratio above 12 are advisory unless `--strict`. Raw ratio counts `.txt`/`.md`, excluding assets and registry; it does not measure all binary or HTML source material. Missing sections can escape duplicate comparisons. The docstring's claim that clearing template detection requires reading sources is design rationale, not an enforced necessity. The rules cannot prove grounding. SRC-1, `tools/compile_lint.py`.

#### RT-RTE-pdf-sidecar
Label: PDF searchable sidecar extraction

Endpoints: caller-selected local PDF → page-count lookup → selected-page native extraction/OCR → labeled text sections → output file and status. Python owns deterministic page progression; Poppler and Tesseract execute the extraction. Context is command arguments and per-page text, not a model window. State accumulates sections in memory and uses a temporary render directory, then writes one output. Evidence: SRC-1, `tools/pdf_text.py`.

> if args.output.exists() and not args.force:
>         parser.error(f"output already exists (use --force): {args.output}")
> --- `tools/pdf_text.py`

> failures.append((page, str(exc)))
>                 sections.append(f"===== PAGE {page} (extraction failed) =====\n[{exc}]")
>                 print(f"page {page}/{total_pages}: ERROR: {exc}", file=sys.stderr)
>                 if args.fail_fast:
>                     break
> --- `tools/pdf_text.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: default sibling .txt or chosen output, page diagnostics on stderr, exit 1 if a page failed; argument/dependency setup errors can terminate before output.
- Later read-back: protocol directs extracted text to remain beside the binary so later agents need not re-extract it; helper alone does not register or compile it.
- Delegated visibility: subprocesses receive explicit file/page/render/OCR arguments and return text or error; no external agent delegation is defined.
- Selection predicate: chosen PDF and sorted validated page ranges; native text accepted at default 40 alphanumeric characters, otherwise OCR, or OCR all selected pages by flag.
- Invalidation or expiry: no automatic refresh; existing output refused unless force, and retained original supports re-extraction/manual verification.
- Activation or effect: filesystem write of machine-generated text with page method/failure labels; provenance header is default but optional.
- Evidence limits: dependencies are external; character count does not certify accuracy and timeout covers each command, not total runtime or file-write atomicity.

Admission: caller chooses file, output, pages and options; code accepts extraction based on command success and text checks, not human per-page approval. Output may be admitted despite failed pages, including with fail-fast. No answer oracle is supplied; verifying critical readings against PDF images is requested editorial work. Operating mode is targeted extraction. Rejection/recovery: argument validation, per-command errors/timeouts, no-overwrite default, retained source and manual rerun; no automatic rollback after a partial write. Subprocess argument arrays do not create an OS sandbox. The source-path equality check does not establish protection against aliases or arbitrary output locations. SRC-1, `tools/pdf_text.py`, `tools/README.md`.

#### RT-RTE-caption-fetch
Label: Targeted YouTube caption retrieval

Endpoints: public video URL/ID → ID validation → optional library import → track listing/selection → fetch → format → stdout or selected path. Python controls progression; external API library and YouTube own remote availability and returned captions. Evidence: SRC-1, `tools/youtube_transcript.py`, `tools/requirements-youtube.txt`.

> if args.manual_only:
>             track = transcript_list.find_manually_created_transcript(args.languages)
>         elif args.generated_only:
>             track = transcript_list.find_generated_transcript(args.languages)
>         else:
>             track = transcript_list.find_transcript(args.languages)
> --- `tools/youtube_transcript.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: track-list JSON or transcript as text/JSON/SRT/VTT; optional output file and stderr metadata; missing dependency exits 3 and caught retrieval/output exceptions return 4.
- Later read-back: possible if caller saves and ingests output; no automatic registry/wiki update or read-back consumer is wired by this helper.
- Delegated visibility: external library receives video ID and language/track requests; provider implementation and service internals are uninspected.
- Selection predicate: one validated known video, requested language preference, manual/generated flags; default preference behavior is delegated to find_transcript.
- Invalidation or expiry: no cache freshness rule; explicit refetch or overwrite is caller-controlled.
- Activation or effect: outputs captions or track metadata, not a grounded synthesis; chosen output is written without a no-overwrite guard.
- Evidence limits: actual upstream selection and network success are unobserved; plain text collapses whitespace and omits timing unless requested, whereas JSON retains snippet metadata.

Admission: open targeted research, not bulk scraping or a curriculum. Caller selects the source/options; software selects a track and serializes its content without per-caption human approval. No expected-answer oracle or factual verification is implemented. Documentation asks users to verify substantive claims against stronger sources. Error reporting permits a caller-chosen next route but no automatic retry/rotation; previous output overwritten by a successful write has no wrapper rollback. Dependency version is a range, not an immutable pin. SRC-1, `tools/youtube_transcript.py`, `tools/requirements-youtube.txt`, `tools/README.md`.

#### RT-RTE-library-setup
Label: New library provisioning

Endpoints: human creation request → confirm conventions → agent scaffold → write local AGENTS → seed registry/navigation/meta files → commit and push. The agent owns execution under `library.md`; human domain/link-style decisions shape proposed organization. Natural-language instructions produce persistent paths and prompts, not a code-based factory. Evidence: SRC-1, `library.md`.

> Ask the human (use `AskUserQuestion`) to settle the choices that shape the whole
> structure. Skip any the human has already specified. Offer sensible defaults:
> --- `library.md`

> Commit the scaffolding with a clear message and push to the working branch.
> --- `library.md`

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested new library tree and branch commit/push; no software return schema is defined.
- Later read-back: new local AGENTS, registry, wiki navigation and retained files are intended inputs to future Librarian sessions.
- Delegated visibility: uninspected — AskUserQuestion availability and host behavior are external, not implemented by Funes.
- Selection predicate: human requested folder/domain, confirmed or already specified conventions, shared standard layout and declared deviations.
- Invalidation or expiry: no expiry; subsequent local instruction edits and structural migrations have no dedicated admission workflow here.
- Activation or effect: requested creation of a new scoped instruction entry point and library; future host instruction loading is not demonstrated.
- Evidence limits: setup recipe and empty reference scaffold establish intended provisioning, not a successful run, tool availability or repository write grants.

Admission: human can choose or reject conventions; the agent authors files, with no final per-file approval required by this recipe. Guidance is the standard raw/wiki/outputs spine, terse local instructions and shared protocol. The reference template is a construction guide, not an answer oracle. Mode is open human-requested provisioning. Commit history affords recovery if executed, but no automated rollback is prescribed. This changes retained knowledge infrastructure and local instructions, not model parameters or the external host's production machinery. SRC-1, `library.md`.

### Claims

#### RT-CLM-library-guarantees
Label: Immutable raw and cited library claims

Claimed operation: preserve raw content, require source links for wiki/output claims and maintain library coherence. Owner: Librarian. Enforcement point: interpreted protocol instructions; helpers provide narrower local validation and audits. Guarantee strength: protocol. Covered intended paths: ingest, compile, Q&A and health review under the protocol. Alternate paths: direct host edits, extraction output overrides, caption writes and unreviewed commits do not pass a universal semantic/raw-write gate. Required external contract: host instruction delivery, agent adherence, appropriate file permissions and human approval where requested. Evidence: SRC-1, `protocol.md`, `README.md`, `tools/pdf_text.py`, `tools/youtube_transcript.py`.

> Every claim in the wiki and outputs must link back to the source note or raw
> document it rests on. A source-note link is sufficient when that note links to
> the immutable raw source.
> --- `protocol.md`

> - **Never edit `raw/` content** — it is the immutable record.
> --- `protocol.md`

- instruction conclusion status: claimed
- universal-enforcement conclusion status: absent
- operation conclusion status: uninspected

The absent enforcement conclusion is bounded to the tracked shipped instructions, helpers and CI, not the external host or OS. Mechanical checks can reject selected defects but neither inspect every write nor establish citations' entailment. The exact admission roles are on [RT-RTE-ingest-compile](#rt-rte-ingest-compile) and [RT-RTE-health-audit](#rt-rte-health-audit).

### Evidenced absences

#### RT-ABS-model-driver
Label: No shipped model-call driver

- implementation conclusion status: absent

Searched boundary: SRC-1 at 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11, complete tracked path listing, root entry/setup/protocol/README, all four Python helpers, optional dependency declaration and CI workflow. Queries: `git ls-tree -r --name-only HEAD`; `rg -n 'model|provider|agent|approval|subprocess|write_text|force|strict' AGENTS.md protocol.md library.md tools .github starter-library`, followed by complete reads of executable helpers and entry text. All executable files are linters or extraction wrappers, and the CI caller invokes only syntax checks and linters. No model API caller or enclosing agent loop is shipped in this bounded tree. Evidence: SRC-1, `AGENTS.md`, `tools/check_links.py`, `tools/compile_lint.py`, `tools/pdf_text.py`, `tools/youtube_transcript.py`, `.github/workflows/funes-lint.yml`.

> **No application stack required.** Funes needs no server, vector database, embedding pipeline, or proprietary runtime. It is a repository structure, an operating protocol, and optional maintenance and extraction tools.
> --- `README.md`

Supported conclusion: scheduling, grants, context isolation and provider policy cannot be attributed to a Funes-owned model driver. Prevented conclusion: this is not evidence that a user's deployed host lacks those features. This report adds no source or boundary coverage beyond the files already included by boundary.

### Behavioral-authority paths

#### RT-BAP-librarian-instructions
Label: Librarian instruction authority

Consumer: external file-capable LLM agent. Channel: root and library AGENTS routing to shared protocol and local deviations. Force: requested operating authority, contingent on host loading and model adherence, not mechanically mandatory execution. Horizon: future actions within a session and later sessions that reload the same instructions. Local instructions created through [RT-RTE-library-setup](#rt-rte-library-setup) can therefore become later behavior-shaping text, but no trace establishes activation. Static shipped instruction loading is not experience read-back. Evidence: SRC-1, `AGENTS.md`, `starter-library/AGENTS.md`, `protocol.md`, `README.md`.

> If your agent does not automatically load `AGENTS.md`, tell it once: “Read `AGENTS.md` and follow `protocol.md` as the Librarian.”
> --- `README.md`

## Annotations

none
