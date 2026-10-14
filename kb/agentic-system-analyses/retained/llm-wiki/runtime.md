---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM Wiki runtime baseline: external-agent maintenance, CLI/MCP retrieval, scaffolding and forcing routes at the frozen commit."
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
---

# llm-wiki runtime report

## Runtime account

### What performs the work

LLM Wiki ships a Python toolkit and a maintainer protocol, not an enclosing model execution loop. The human supplies sources, questions and emphasis; the external agent interprets the protocol and performs semantic writes. The toolkit supplies search, expansion, structural diagnostics and scaffold writes. This separation is the decisive runtime boundary: an MCP call can return a page or create a template, but does not itself synthesize an answer or ingest a document. SRC-1: `docs/ARCHITECTURE.md`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.

> | CLI + MCP for read/lint/scaffold | Agent writes all `wiki/` pages |
> --- `docs/ARCHITECTURE.md`

The model-dependent component is [RT-CMP-agent](#rt-cmp-agent). The protocol reaches that component through [RT-BAP-maintainer-instructions](#rt-bap-maintainer-instructions). This is instruction delivery intent, not evidence that a particular host loaded or obeyed it. The natural-language instruction body and the symbolic Python tool implementation have different consumers and enforcement strengths.

### Ordinary invocation, from project creation to a filed answer

A caller runs `wiki init <dir>` to copy bundled project files, render dates and absolute root placeholders, seed the log and optionally invoke `git init`. The package entry point is `llm_wiki.cli:main`; the wheel explicitly includes the scaffold. The created project contains instructions, templates, raw-source storage and wiki seed pages. The user opens the instructions in an external agent. [RT-RTE-project-init](#rt-rte-project-init) covers initialization; SRC-1: `pyproject.toml`, `src/llm_wiki/bootstrap.py`, `src/llm_wiki/cli.py`.

The ordinary maintenance trigger is the human adding a raw document and asking for ingest. The human is the source-curation principal; the agent owns subsequent bookkeeping decisions. Its prescribed context is the complete raw document, templates and affected wiki pages. It discusses takeaways unless batch mode applies, creates a source summary, updates entities/concepts, conditionally revises synthesis and contradictions, updates the index and appends the log. There is no toolkit ingest command executing those semantic steps. The durable terminal output is edited Markdown, not a toolkit-generated answer. [RT-RTE-source-ingest](#rt-rte-source-ingest) describes the admission policy and its limits. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/ingest.py`.

A later human question initiates [RT-RTE-wiki-query](#rt-rte-wiki-query). The prescribed agent reads the index, chooses a search query, reads relevant pages or sections, synthesizes with citations and offers to file a valuable answer. CLI root selection is explicit `--root` or environment/upward discovery; MCP uses environment/upward discovery. Search returns paths, scores and snippets, not a synthesized response. The agent then chooses page and optional heading arguments for expansion. Full expansion returns the page and headings; section expansion returns the first matching heading block, its descendants and outbound links. The answer may stay in chat or become an answer page with a log entry. Neither search nor expansion commits a file. SRC-1: `src/llm_wiki/paths.py`, `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.

Coordination is a human/agent protocol over shared files. The inspected writers use direct `write_text`; they do not stage a multi-page transaction. The external host schedules model steps, supplies filesystem tools and returns the final response. Its context isolation, compaction, approvals, concurrent-agent behavior and recovery are outside this implementation. The target offers optional Git initialization and recommends history, but does not commit each maintenance operation or implement rollback. No run traces or experiments were supplied. All model compliance, actual answer quality, exercised read-back and benefit remain unobserved.

### Selected alternate and forcing routes

Four source-inspected forcing cases delimit the ordinary account:

1. **Native MCP versus shell CLI or direct host reads.** Both exposed tool surfaces share search, expansion, lint and page-creation helpers. MCP runs over stdio with project-root discovery, while CLI can choose an explicit root. The host may also read and edit files without either interface. Therefore an expansion-helper restriction is not a host-wide filesystem sandbox. SRC-1: `src/llm_wiki/mcp_server.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/scaffold/.mcp.json`.
2. **Optional qmd subprocess.** [RT-RTE-qmd-search](#rt-rte-qmd-search) calls an external executable and adapts its JSON rather than computing BM25 in-process. Collection configuration, retrieval freshness and internal algorithm are external contracts. A qmd result adapter is not proof of a model or embedding pipeline implemented by this repository. SRC-1: `src/llm_wiki/search.py`.
3. **Direct scaffold overwrite.** [RT-RTE-page-create](#rt-rte-page-create) permits `force=True` through both CLI and MCP. Creation is not gated by lint, human content approval or completion of index/log updates. It can replace an existing page with rendered template text. This is a countercase to treating the semantic-maintenance checklist as enforced on every write. SRC-1: `src/llm_wiki/new_page.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.
4. **Watch and status without ingest.** [RT-RTE-pending-watch](#rt-rte-pending-watch) reports a newly pending filename to a callback or stdout, remembers names only in the current process and polls again. The CLI callback prints. A library caller could supply another callback, but no model-dependent callback is shipped here. The coverage classifier calls a raw file “ingested” when a source-page `raw_file` value maps to it; that is not an oracle for summary fidelity or completion of all maintenance steps. SRC-1: `src/llm_wiki/watch.py`, `src/llm_wiki/ingest.py`, `src/llm_wiki/cli.py`.

The shell checklist prints status and checklist text; the demo driver consumes retained example pages through stats/search/status/lint/log/expand. These callers do not add a hidden semantic producer. SRC-1: `scripts/ingest-checklist.sh`, `scripts/demo-walkthrough-fast.sh`. These are static source findings, not executed trials.

### Guarantees and control envelopes

**Raw immutability and append-only history:** the owner is the external maintainer following the shipped protocol; the enforcement point is instruction interpretation. Guarantee strength: protocol. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. The toolkit maintenance readers do not rewrite raw documents, but the protocol does not restrict external filesystem tools, and direct editing can bypass it. Required external contract: host tool permissions and agent compliance. The append-only instruction does not make `wiki/log.md` physically append-only. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

> | Raw sources | `raw/` | **Read-only.** Never modify. |
> --- `src/llm_wiki/scaffold/AGENTS.md`

> - **`wiki/log.md`** — Append-only timeline. Never edit past entries.
> --- `src/llm_wiki/scaffold/AGENTS.md`

**Explicit-page expansion containment:** the toolkit owns a symbolic check in `resolve_page` that resolves a candidate and rejects it unless it is a file inside the resolved wiki root. Guarantee strength: invariant within that helper. Implementation conclusion status: wired. Operation conclusion status: uninspected. CLI/MCP expansion and explicit-page backlinks use it. Recursive corpus readers and qmd adaptation take different paths; direct host reads do not use it. This conclusion is only about candidates accepted by this helper, not a deployed isolation envelope or race-free filesystem guarantee. SRC-1: `src/llm_wiki/links.py`.

> resolved = candidate.resolve()
> resolved.relative_to(root_resolved)
> --- `src/llm_wiki/links.py`

**Overwrite rejection:** page creation owns an existing-destination check, overridden by `force`; initialization owns a nonempty-target check, likewise overridden. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. Coverage is these writers under ordinary filesystem assumptions, not symlink-safe confinement, atomic replacement, manual edits or other host writes. SRC-1: `src/llm_wiki/new_page.py`, `src/llm_wiki/bootstrap.py`.

**Structural lint failure:** the CLI owns a post-inspection exit threshold, described in [RT-RTE-wiki-lint](#rt-rte-wiki-lint). Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. It reports and optionally fails; it is not a content-admission gate. MCP returns filtered diagnostic data and does not replicate a process exit policy. Required external contract: the caller must run lint and act on its report or exit status. SRC-1: `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.

Capability surface, grant set and isolation must therefore remain separate. The target exposes inspection tools and a template writer, with project selection controlled by caller configuration; the maintainer protocol also expects broader host filesystem writing and optionally web search. Which capabilities a real agent possesses and which require approval are uninspected. No deployed sandbox, provider grant set, remote-worker delegation or execution reliability is established by the shipped MCP configuration.

### Change admission and inspected coverage

Knowledge admission and optional answer filing are delegated to the maintainer; instruction change is explicitly co-evolved with the human. The local prompt-sync script copies the canonical instructions to scaffold and examples, but does not judge the proposal. [RT-RTE-instruction-sync](#rt-rte-instruction-sync) traces that propagation. No source finding here attributes package updates, model replacement or production-machinery evolution to the agent. Semantic revision details are left to the memory analyst rather than inferred from template writes.

This member inspected the scaffold maintainer and Claude handoff, `.mcp.json`, CLI/MCP, root resolution, bootstrap, page creation, search, section expansion, links, ingest status, watcher, lint, package configuration, architecture, prompt-sync script, checklist and fast demo driver. All are SRC-1 at the frozen commit. Evidence layers are implementation for Python/shell paths and doctrine/design for instructions/configuration/documentation. The newly traced details remain within the boundary register. Source tests, other example pages and other host configuration variants were not used to infer operation. No target execution, tests, models or external tools were run.

## Shared records

### Components

#### RT-CMP-agent
Label: External wiki maintainer agent

Source-native identity: the “wiki maintainer” instructed by the generated project's `AGENTS.md`; its enclosing host and provider are external. Representational form: distributed-parametric model inference, supplied with natural-language instructions and document text. Storage substrate: external model/provider weights and host context, neither exposed by this repository. Exact model version pinned: uninspected; the shipped protocol does not select a model. Parameters change during operation: uninspected; provider internals are outside the boundary. Mutable endpoint can resolve to another model: uninspected; endpoint configuration belongs to the host. These independent uncertainties prevent a fixity or training conclusion, not the finding that the protocol assigns interpretation to an agent. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `docs/ARCHITECTURE.md`.

> You are the **wiki maintainer** for this knowledge base. Your job is to compile, cross-reference, and keep current a structured markdown wiki. The human curates sources and asks questions. You do the bookkeeping.
> --- `src/llm_wiki/scaffold/AGENTS.md`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-project-init
Label: Project scaffold initialization

Endpoints/progression: CLI caller → `bootstrap_wiki` → bundled scaffold enumeration/rendering → project files → optional `git init` → result object/CLI listing. Owner: caller selects destination, name, force and Git option; Python determines copy/render rules. Context/state/action effects: symbolic placeholder replacement on scaffold text, directory creation and direct file writes; optional subprocess uses the target as cwd. Natural-language instructions and seed Markdown persist on filesystem; MCP JSON remains symbolic host configuration. SRC-1: `src/llm_wiki/bootstrap.py`, `src/llm_wiki/cli.py`, `pyproject.toml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Result gives target, created file list and Git-initialization flag; CLI prints next steps.
- Later read-back: Initial scaffold is static shipped material, not accumulated memory; later modified project files can reach maintenance/query consumers.
- Delegated visibility: External agent is asked to open AGENTS.md; generated MCP configuration supplies tools but host loading is unobserved.
- Selection predicate: Caller target and bundled regular-file enumeration, excluding Python cache artifacts; force permits overwrite.
- Invalidation or expiry: No expiry; subsequent edits or forced initialization may replace files.
- Activation or effect: Writes project scaffold; whether an agent subsequently follows it is unobserved.
- Evidence limits: File-copy implementation inspected, not executed; Git success and host startup are unobserved.

Admission: open caller request, no answer oracle. Caller proposes target/configuration and can cancel before invocation; software rejects a nonempty target unless forced. Guidance is bundled scaffold, date/project/root substitution and prescribed project layout. It persists rendered files. No all-files transaction or rollback is implemented; `git init` failure is caught and reflected in a false flag, not reverted scaffold creation.

> if target.exists() and any(target.iterdir()) and not force:
> --- `src/llm_wiki/bootstrap.py`

#### RT-RTE-source-ingest
Label: Human-triggered source ingest

Endpoints/progression: human-curated raw source/request → external maintainer reads/discusses → source and affected wiki pages → index/log. Owner of next steps: maintainer agent under human guidance; execution and filesystem effects belong to the external host. Policy/form: natural-language ingest procedure and templates, interpreted rather than executed by this toolkit. Context comprises full source and affected wiki content; later state is edited Markdown. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Prescribed discussion and completed maintenance; no toolkit ingest return object exists on this route.
- Later read-back: Updated wiki pages and catalog are intended to feed later query and maintenance invocations.
- Delegated visibility: Human sees discussion and browsable files; host decides what the agent actually reads and writes.
- Selection predicate: Human chooses raw source; maintainer identifies touched entities/concepts and whether synthesis or contradiction updates are warranted.
- Invalidation or expiry: Incremental revisions are prescribed; no software expiry or mandatory stale-source refresh is wired by this instruction.
- Activation or effect: Agent is requested to integrate source content across the wiki; actual writes and subsequent behavior are unobserved.
- Evidence limits: Shipped doctrine, not an execution trace; complete reading, integration quality and checklist compliance are not established.

Admission/mode: open human ingest request; batch mode can bypass discussion. Agent proposes interpretations and determines individual wiki edits; human guides emphasis and decides what matters. Discussion is not an explicit per-page approval gate. No expected-answer oracle is specified. Human can guide or later edit content, but a host-enforced veto is uninspected. Rejection and recovery are conversational/manual; optional Git history could assist recovery but no automatic commit/revert occurs on this protocol route.

> 2. **Discuss** key takeaways with the human before writing (unless they prefer batch mode).
> --- `src/llm_wiki/scaffold/AGENTS.md`

Guidance and theory account: instructions request synthesis revision when evidence shifts the picture and a contradiction ledger when claims conflict. They retain pages, synthesis, contradictions and operation entries, not model parameters. This affords localized prose claims and criticism, but a ledger label alone does not establish formulated theory revision or changed reliance.

> 5. **Revise** `wiki/synthesis.md` if the source shifts the overall picture.
> 6. **Flag** contradictions in `wiki/contradictions.md` when new data conflicts with existing claims.
> --- `src/llm_wiki/scaffold/AGENTS.md`

Theory-builder conditions 1–4: condition 1 conclusion status: afforded — named synthesis/claim pages can hold whole localized accounts; no particular theory is reconstructed here. Condition 2 conclusion status: claimed — procedure asks the agent to condition updates on what sources imply; actual theory-dependent decisions are unobserved. Condition 3 conclusion status: uninspected — conflict flagging is requested, but this source route does not show blame assignment and resulting revision. Condition 4 conclusion status: uninspected — files permit later rounds; criticism shaping another round is not demonstrated. Addressability: pages/headings provide inspectable text, not proven assumption-level organization. Persistence: intended project/session horizon with later maintenance/query readers, actual recurrent use unobserved. Learning: improved future capacity and attribution are unestablished. Reflection: schema co-evolution represents methods, but both causal directions are unobserved. Reflective and autonomous theory builder: unestablished independently; human contributions and opaque model processing prevent a claim of computation performing every internal operation. No exercised self-improvement is inferred from wiki revision.

#### RT-RTE-wiki-query
Label: Wiki query and optional answer filing

Endpoints/progression: human question → agent index read/query selection → CLI/MCP BM25 search → agent page/section selection → expansion → interpreted answer → optional durable answer/log. Owner: agent selects relevance and synthesis; code ranks corpus and extracts content. Symbolic BM25 tokenization uses lowercase `[a-z0-9]+`, boosted title/headings and corpus statistics; input/output Markdown is natural-language content to the model. Search rebuilds counts from current files; no model call occurs inside it. SRC-1: `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/scaffold/AGENTS.md`.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Tools deliver ranked path/score/snippet records or requested page/section content; agent is instructed to return an answer with citations.
- Later read-back: Existing maintained pages are requested for the current question; a filed answer can join the corpus for later search/expansion.
- Delegated visibility: Tool results reach their external caller; delivery into the actual model context depends on the host.
- Selection predicate: BM25 positive scores sorted descending and sliced to limit; agent/caller chooses query, page and section. Section extraction takes the first normalized heading match and stops at the next same-or-higher-level heading.
- Invalidation or expiry: BM25 reads current files each call; edits/deletions change future results. Filed answers have no implemented expiry.
- Activation or effect: Tools expose selected text; agent is requested to synthesize and optionally persist it. Compliance and effects on answer behavior are unobserved.
- Evidence limits: Ranking/extraction code is inspected; completeness, factual accuracy, successful corpus scoring and model benefit are not established.

Working-context control: expansion on demand can keep unrequested sections out of a tool response. Caller chooses heading; code keeps that block, descendants and links. Full page remains reachable through another call. This is selective external reload, not trimming accumulated turns or isolating a sub-agent frame; host compaction is uninspected. CLI display shortens snippets over 120 characters; MCP/JSON carry the helper snippet instead. These transforms do not deliver all source content.

> section_lines = lines[start_idx:end_idx]
> content = "\n".join(section_lines).strip()
> outbound = sorted(extract_wikilinks(content))
> --- `src/llm_wiki/expand.py`

Answer admission/mode: open question, no expected-answer oracle; citations are requested, not an answer verifier. Agent proposes synthesis/filing; the human is offered filing but the instructions do not specify an enforced acceptance handshake. External host writes any accepted answer; rollback is manual/history-dependent, not wired in search/expand. Optional qmd selection is a distinct executor in [RT-RTE-qmd-search](#rt-rte-qmd-search).

#### RT-RTE-qmd-search
Label: External qmd search adaptation

Endpoints/progression: caller selects backend qmd → executable presence check → subprocess `qmd search` on collection `wiki` → JSON parsing/path filtering/snippet truncation → CLI/MCP result. Owner: adapter controls command arguments and result transformation; external qmd controls search. Context/state: project cwd and external collection configuration; target adapter does not update that collection. SRC-1: `src/llm_wiki/search.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Adapted results capped at limit, or handled missing-executable/nonzero-exit/non-JSON errors.
- Later read-back: External collection is intended to retrieve project wiki content; its indexing and freshness relative to changed pages are uninspected.
- Delegated visibility: Query and collection arguments reach a local subprocess; resulting snippets reach the external caller.
- Selection predicate: Backend request selects qmd; adapter skips non-dictionary items and paths failing `relative_to(wiki_root)`, accepts path/file/uri fields and takes score/relevance/fallback rank.
- Invalidation or expiry: uninspected — external collection maintenance is not implemented in this adapter.
- Activation or effect: Spawns qmd and transforms returned records; downstream model consumption remains unobserved.
- Evidence limits: External algorithm, numerical components, deployment, malformed-payload behavior beyond explicit guards and freshness are not established.

> if backend == "bm25":
>     return search_wiki(wiki_root, query, limit=limit, include_index=include_index)
> return search_wiki_qmd(wiki_root, query, limit=limit)
> --- `src/llm_wiki/search.py`

The adapter uses argument-list subprocess execution rather than interpolating a shell command. It does not apply `resolve_page` to each result: relative paths are resolved, but absolute paths receive a lexical containment conversion. This is not evidence of the explicit-page helper's canonical-file invariant covering qmd results. No timeout or retry is supplied in the inspected subprocess call.

#### RT-RTE-page-create
Label: Template-based page creation

Endpoints/progression: CLI `new` or MCP `wiki_new` → `create_page` → validate page type/normalize slug → read project template → replace date/title/slug → write destination → return path. Owner: caller chooses content parameters/force; software maps type to directory and formats template. Context/state: filesystem templates, date and caller strings. SRC-1: `src/llm_wiki/new_page.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created relative path/result flag; CLI/MCP hint requests index and cross-link follow-up.
- Later read-back: Written template page joins future wiki enumeration/search/expansion; useful semantic content requires subsequent authoring.
- Delegated visibility: Caller receives path/hint; no separate agent or reviewer is invoked.
- Selection predicate: Supported page type, normalized slug and project-local template determine destination/content; existing file rejects unless forced.
- Invalidation or expiry: Force can replace destination; no expiry or versioned rollback is implemented.
- Activation or effect: Direct filesystem write of rendered template, not semantic integration or automatic index/log repair.
- Evidence limits: Host authorization, human identity and template correctness are not inferred from calling identity.

Admission/mode: open tool request. Caller proposes strings; software decides syntactic admissibility; no answer oracle, semantic review or per-content human approval is implemented. Recovery is later edit or external version history, not atomic transaction. Guidance is the selected template; its rendered text persists. The check is deliberately overridable:

> if dest.exists() and not force:
>     raise FileExistsError(f"Page already exists: {dest.relative_to(root)}")
> --- `src/llm_wiki/new_page.py`

> dest.write_text(content, encoding="utf-8")
> --- `src/llm_wiki/new_page.py`

#### RT-RTE-wiki-lint
Label: Structural diagnosis and delegated correction

Endpoints/progression: periodic/requested human lint → agent CLI/MCP invocation → `lint_wiki` file enumeration/checks → filtered report → requested agent fixes/log. Owner: code diagnoses specified structure; agent evaluates warnings, contradiction resolution and further sources. Symbolic check rules consume YAML, links and lexical markers; semantic correction uses interpreted prose outside the toolkit. SRC-1: `src/llm_wiki/lint.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/scaffold/AGENTS.md`.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Diagnostic issues, with CLI exit 1 at the selected fail-on threshold; MCP returns filtered JSON issues.
- Later read-back: Toolkit report is not automatically persisted; prescribed fixes and log can feed later inspections and queries.
- Delegated visibility: Caller sees selected severity/category diagnostics; CLI failure is evaluated on the unfiltered report.
- Selection predicate: All enumerated wiki Markdown; frontmatter/structure/link/raw/index checks and bounded contradiction-language heuristics, then caller display filters.
- Invalidation or expiry: Recomputed from files per invocation; no durable issue state or expiry.
- Activation or effect: Toolkit reads/reports; instruction asks agent to fix errors, propose warning fixes and log the operation.
- Evidence limits: Structural predicates are not semantic truth or a complete contradiction oracle; no correction run is supplied.

Diagnosis/admission/mode: open request or unspecified periodic scheduling. Software decides issue predicates against local references (link targets, allowed types, required fields); these are structural reference outcomes, not expected answers for wiki claims. Agent proposes semantic corrections; human receives warnings/proposals. Error fixes are instructed immediately, not blocked on an explicit human approval gate. No automatic writer or rollback is connected to lint. Contradiction checks search marker words and ledger references; they do not establish claim-level criticism.

> if fail_on != "none":
> --- `src/llm_wiki/cli.py`

> failing = [i for i in report.issues if severity_rank[i.severity] <= cutoff]
> if failing:
>     sys.exit(1)
> --- `src/llm_wiki/cli.py`

#### RT-RTE-pending-watch
Label: Pending source notification

Endpoints/progression: CLI watch/library invocation → source coverage classifier → new pending filename difference → stdout/callback → repeat or return once. Owner: deterministic poller; caller callback owns any subsequent action. Context/state: raw filenames, source-page frontmatter mapping and process-local `seen_pending`. SRC-1: `src/llm_wiki/watch.py`, `src/llm_wiki/ingest.py`, `src/llm_wiki/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Notifications while polling; `once` returns after one check, ordinary loop continues until interrupted.
- Later read-back: Reads current raw/source state each poll; process-local seen names are not durable retained memory.
- Delegated visibility: Callback receives message and raw filename; shipped CLI callback only prints the message.
- Selection predicate: Classifier status pending and filename not already seen in this process; raw README and .gitkeep excluded.
- Invalidation or expiry: Seen names persist until process ends; same-name content edits do not cause a second notification within that instance.
- Activation or effect: Notification only in shipped caller; library callback could perform external effects whose implementation is not inspected here.
- Evidence limits: Name/frontmatter coverage is not ingest completeness; no autonomous maintenance or freshness guarantee follows.

> pending = [s.raw_file for s in statuses if s.status == "pending"]
> new_pending = [f for f in pending if f not in seen_pending]
> --- `src/llm_wiki/watch.py`

#### RT-RTE-instruction-sync
Label: Maintainer instruction change and synchronization

Endpoints/progression: human/agent convention revision to canonical AGENTS.md → maintainer runs sync script → whole-text copies to scaffold and four examples → later initialization or agent reading. Owner: human/agent co-evolve convention; script blindly propagates canonical text to existing target parents. Natural-language rules persist as filesystem Markdown; symbolic target list controls copies. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `scripts/sync_agents.py`.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Script prints each synchronized path and returns zero; missing canonical file yields nonzero status.
- Later read-back: Changed maintainer text can reach future generated projects or example agents; existing arbitrary user projects are not sync targets.
- Delegated visibility: External maintainer consumes instructions only if its host loads them; script starts no model session.
- Selection predicate: Fixed scaffold/example target list and existing parent directories.
- Invalidation or expiry: Later canonical edit requires another sync; copied text has no expiry or automatic migration of deployed projects.
- Activation or effect: Copies instruction files; subsequent rule compliance and effect on behavior are unobserved.
- Evidence limits: Co-evolution request is not a demonstrated evidence-responsive improvement or automatic admission review.

Admission/mode: open convention change when it is not working, with human co-evolution. Proposer can be agent/human; final agreement mechanism and veto are not implemented. Script accepts canonical bytes, has no oracle and no semantic rejection gate. Rollback is external edit/history; guidance is the current schema and operating experience as requested by the prompt. Only revised instructions persist through this route; no model weights or new host capability grants are installed.

> Co-evolve this file: when a convention isn't working, change it here.
> --- `src/llm_wiki/scaffold/AGENTS.md`

> content = CANONICAL.read_text(encoding="utf-8")
> --- `scripts/sync_agents.py`

### Claims

#### RT-CLM-agent-bookkeeping
Label: Agent-owned knowledge bookkeeping

Claimed operation: human source curation and questions are separated from agent reading, extraction, wiki writing, cross-reference maintenance and contradiction/gap suggestions. This is the shipped operational allocation, not observed reliability. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, supported by the passage in [RT-CMP-agent](#rt-cmp-agent).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-maintainer-instructions
Label: Maintainer instruction authority

Consumer: external wiki maintainer agent. Channel: project AGENTS.md, with scaffold CLAUDE.md directing Claude Code to read it. Force: natural-language role/schema/operation guidance, not toolkit-enforced filesystem permission. Horizon: project maintenance and later query sessions if the host reloads it. Generated MCP configuration instead governs tool startup symbolically; it does not prove prompt loading. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/scaffold/CLAUDE.md`, `src/llm_wiki/scaffold/.mcp.json`. Actual activation and model compliance are uninspected.

> You are the **wiki maintainer** for this project. Read **`AGENTS.md`** for the full schema and operations (ingest, query, lint).
> --- `src/llm_wiki/scaffold/CLAUDE.md`

## Annotations

none
