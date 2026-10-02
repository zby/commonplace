---
type: types/agentic-system-analysis-overview.md
description: PageIndex indexes a PDF into a stored page-range tree of model-written summaries that a model reads by tool at query time; no check tests summaries or answers, and use changes nothing.
run-id: AAS-2026-09-29-pageindex-02
system: PageIndex
run-date: '2026-09-29'
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d2693d80791a86345ef78b3234834f5fe53a70a0
analysis-cutoff: '2026-09-29'
evidence-tier: code-grounded
inputs-commit: 2344c4fb09a8dd13ef163473e0c9c8ef31097ced
---

# PageIndex agentic-system analysis

## Boundary and evidence

**Intended use.** Characterize PageIndex as a document-retrieval and context-engineering system for LLM agents: how it builds a hierarchical tree index over a long document, how a model-driven agent navigates that tree to select what enters the answering context, what it stores, and which parts depend on model calls. The analysis serves comparison with other agent memory, knowledge, and context-engineering systems. It does not rank products or advise adoption.

**Target classification.** `target-class: memory/knowledge/context-engineering system`. PageIndex is a Python SDK (`pageindex` package, version 0.2.10 in `pyproject.toml`) that indexes documents into a tree of titled, summarized nodes and retrieves by LLM reasoning over the tree instead of vector similarity. Its operation depends on model calls it issues: node summaries and tree expansion at index time, and a tool-using chat agent at query time.

**Boundary kind.** `whole-system`, for the open-source SDK as shipped at the frozen commit. The SDK is the complete inspectable system in local mode: indexing, storage, retrieval tools, and the chat agent all run in-process. Cloud mode is a client of a separate hosted service and is excluded below.

**Functional inclusions** (all at the frozen commit):

- Indexing pipelines: the layout-statistics tree builder `pageindex/flash/` (no LLM for the raw tree), the LLM-driven classic PDF pipeline `pageindex/page_index_classic.py`, the Markdown pipeline `pageindex/page_index_md.py`, and the search-cost tree optimizer `pageindex/tree_optimize.py` (deterministic merge plus LLM-assisted expand), with shared helpers in `pageindex/utils.py` and defaults in `pageindex/config.yaml`.
- Local storage: the on-disk document store `pageindex/local_store.py` and the local SDK surface `pageindex/local_api.py`.
- Retrieval and answering: the client facade `pageindex/client.py`, the agent tool contract `pageindex/agent_tools.py`, the own-model chat agent `pageindex/local_chat.py`, and `pageindex/chat_stream.py`.
- Host-framework adapters that expose the tools to external agent runtimes: `pageindex/integrations/openai_agents.py`, `pageindex/integrations/claude_agent_sdk.py`, `pageindex/integrations/anthropic_sdk.py`.
- The client-side code of cloud mode (`pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`), inspected only as the client half of a contract; see exclusions.
- The CLI `run_pageindex.py`, the test suite under `tests/`, and generated example outputs under `examples/documents/results/`.

**Functional exclusions and the conclusion each prevents:**

- *PageIndex Cloud service* (hosted indexing, OCR, image understanding, block-level citations, folders, metadata, the cloud MCP server, and the "PageIndex File System" corpus-level index). Only its client code is in the repository. Exclusion prevents any conclusion about cloud-side indexing, storage, retrieval behavior, or the live instructions and tool set the cloud MCP server serves; cloud-mode behavior is limited to what the client sends and how it handles responses.
- *PageIndex App* (the hosted document-analysis agent). Not in the repository; prevents conclusions about its agent loop or memory.
- *Host agent runtimes* (OpenAI Agents SDK, Claude Agent SDK, Anthropic SDK tool runner). PageIndex supplies tools and instructions to them; their loops, context management, and persistence belong to the host. Exclusion prevents attributing host-side memory, planning, or retry behavior to PageIndex.
- *Model providers* reached through `litellm` and `openai`. Model behavior is external; the analysis can state what prompts and calls PageIndex issues, not how models respond.
- *External benchmark repositories* (PageIndex-OSS-Benchmark, Mafin2.5-FinanceBench, MMLongBench-Doc-V2) and blog posts linked from `README.md`. Not frozen; their results enter only as README claims (reported operation), which prevents treating the accuracy and cost figures as observed or causal evidence.
- *Repository automation* (`.github/`, `.claude/commands/dedupe.md`): issue-deduplication and CI tooling for maintaining the repository, not part of the system's retrieval operation. Exclusion prevents nothing about the target's runtime.

**External dependencies.** An LLM provider key (for summaries, expand decisions, the classic pipeline, and chat); `litellm`, `openai`, `openai-agents`, and `mcp` libraries; PDF parsing via `pypdfium2` and `PyPDF2`; optional `claude-agent-sdk` and `anthropic` extras; a PageIndex API key and network access for cloud mode only.

**Frozen revision.** `https://github.com/VectifyAI/PageIndex` at commit `d2693d80791a86345ef78b3234834f5fe53a70a0` (origin/main after fetch on 2026-09-29; commit date 2026-09-29T23:50:13+08:00). The local checkout `related-systems/VectifyAI--PageIndex/` is the operational access root only; it was a no-checkout clone at an older commit (`619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`) with no local changes, was fetched, and was detached at the frozen commit with a clean `git status --porcelain`.

**Analysis cutoff.** 2026-09-29, the frozen commit's date. Later upstream changes are out of scope.

**Evidence tier.** `code-grounded`: the indexing, storage, tool, and chat mechanisms are inspectable Python at the frozen commit. Claims about model-dependent quality (retrieval accuracy, index quality) rest on README reports and example outputs, not on runs performed by this analysis.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git repository | `https://github.com/VectifyAI/PageIndex` (access root `related-systems/VectifyAI--PageIndex/`) | `d2693d80791a86345ef78b3234834f5fe53a70a0` | implementation | `pageindex/` (including `pageindex/flash/`, `pageindex/integrations/`, `pageindex/config.yaml`), `run_pageindex.py`, `pyproject.toml`, `requirements.txt`, `tests/` | commit-relative paths at the frozen commit, e.g. `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/agent_tools.py`, `pageindex/tree_optimize.py`, `pageindex/local_store.py`; quotes via `commonplace-quote` | Cloud-mode server side is absent (only `pageindex/cloud_api.py` and `pageindex/mcp_bridge.py` clients); prevents implementation-level conclusions about cloud indexing, cloud tools, and server-served instructions. No tests were executed at boundary time. |
| SRC-2 | git repository | `https://github.com/VectifyAI/PageIndex` | `d2693d80791a86345ef78b3234834f5fe53a70a0` | doctrine/design | `README.md`, `pageindex/flash/README.md`, `docs/naming-rules.md`, module docstrings and comments in SRC-1 files, `cookbook/` notebook prose | commit-relative paths, e.g. `README.md`, `pageindex/flash/README.md`, `docs/naming-rules.md` | Linked external docs (docs.pageindex.ai, blog posts) are not frozen; prevents using them as declared contract beyond what the repository states. |
| SRC-3 | git repository | `https://github.com/VectifyAI/PageIndex` | `d2693d80791a86345ef78b3234834f5fe53a70a0` | reported operation | Benchmark, cost, timing, and FinanceBench accuracy claims and charts in `README.md` and `assets/` | `README.md`, `assets/results-light.png`, `assets/index-cost-light.png`, `assets/query-cost-light.png`, `assets/financebench-light.png` | The benchmark runners and data live in external repositories not frozen here; prevents treating accuracy, cost, or native-PDF comparisons as observed or causal evidence. |
| SRC-4 | git repository | `https://github.com/VectifyAI/PageIndex` | `d2693d80791a86345ef78b3234834f5fe53a70a0` | observed run | Generated tree outputs `examples/documents/results/*_structure.json` for the example PDFs in `examples/documents/`; stored outputs in `cookbook/*.ipynb` if present | commit-relative paths, e.g. `examples/documents/results/2023-annual-report_structure.json` | Outputs carry no recorded run configuration, model, or code revision that produced them; prevents attributing them to the frozen commit's pipeline or to a specific mode or model. |

## Reconciliation

This is reconciliation round 1. The correction-round memory report was checked against the runtime member, the epistemic member and the previous reconciliation. No record is superseded and four records are amended, carried over from round 0 because the members are not rewritten. The one conflict returned in round 0, about the memory scope, was resolved by the specialist and is accepted below. Nothing is returned this round.

### Supersession and identity checks

No record is superseded. The declared parts retain their own fields and statuses; their runtime containers stay declared.

- EPI-OBJ-1 has `Part of: RT-OBJ-1`; EPI-OBJ-3 has `Part of: RT-OBJ-3`; EPI-RTE-1 has `Part of: RT-RTE-1`. These relations resolve the former possible-duplicate descriptions without supersession.
- EPI-RTE-2 groups generation inside RT-RTE-1 and RT-RTE-3; it stays distinct with comparison to both. MEM-RTE-1 supplies targeting metadata to RT-RTE-2 and its RT-RTE-5 variants; it stays distinct across those routes. Neither receives a single-parent relation.
- EPI-OBJ-9 and RT-OBJ-2 remain different extractions. The absence records retain different searched boundaries, and EPI-BAP-1 retains a different consumer from RT-BAP-1, RT-BAP-2 and RT-BAP-3.

### Amendments

Amendment: RT-ABS-1 is corrected in its searched-boundary writer list. Superseded value: the only store writers are `save_document` and `delete_document`, and the CLI and `pageindex/tree_optimize.py` entry points write only user-named result files. Replacement value: those two store writers stand, and the CLI standard-mode run additionally writes a raw trace file under `./logs/` through `JsonLogger` in `pageindex/utils.py` when `run_pageindex.py` calls the standard pipeline without a logger (declared as MEM-OBJ-1). Evidence anchor: MEM-OBJ-1, with `pageindex/utils.py` and `run_pageindex.py`. The log has no reader in the searched code, so the conclusion status stays `absent` and its supported and prevented conclusions are unchanged. Affected findings: MEM-ABS-1 and the memory profile axis `trace_learning`, which cite RT-ABS-1 and MEM-OBJ-1 together.

Amendment: RT-RTE-2 is corrected in the runtime account's wording of its terminal output. Superseded value: page-level citations are checked only by `get_citations` and `resolve_citations`. Replacement value: those functions parse citation tags and resolve each cited document name to a document id (an unknown name keeps no id); they do not check that the cited page exists or supports the statement. Evidence anchor: EPI-RTE-3 and EPI-OBJ-7, read against `pageindex/client.py`, where the constructed entry holds the tag's document name, a looked-up id and the tag's page. Affected findings: RT-CLM-5, EPI-ABS-2, EPI-OBJ-6.

Amendment: RT-CLM-5 is corrected in its evidence status note. Superseded value: this pass did not trace citation resolution. Replacement value: citation resolution was traced by the epistemic pass and is a name-to-id lookup with no support check (EPI-RTE-3, EPI-OBJ-7). The conclusion status stays `afforded`: page-level citation tags and process event streams exist, but no run was observed and no route verifies that a cited page supports a statement (EPI-ABS-2). Evidence anchor: EPI-RTE-3. Affected findings: RT-CLM-1, EPI-OBJ-6.

Amendment: RT-RTE-8 is corrected in the scope of the guarantee that a stored expanded node names only headings printed on its page. Superseded value: a proposed child is kept only if it is a heading printed on the claimed page. Replacement value: a proposed child is kept only if its normalized title string occurs in the index-time page text of the claimed page, which is pdfium layout text (EPI-OBJ-9). The check does not establish that the string is a heading, its level, or that it starts a section, so a title inside running prose passes. The agent later reads different, PyPDF2 text (RT-OBJ-2), and agreement between the two is unchecked. Evidence anchor: EPI-OBJ-4 and EPI-OBJ-9, read against the substring check quoted in RT-RTE-8. The guarantee strength stays `invariant` for the string-presence check on model-proposed children; only the wording of what it guarantees narrows. Affected findings: EPI-OBJ-4, RT-OBJ-1.

The metadata refinement of RT-OBJ-3 needs no amendment. The memory report annotates RT-OBJ-3 to say that the `metadata` field is caller-supplied and shown to the chat model; that adds a lens-specific field and does not change the runtime record's declared facts.

### Anchored conflicts

No conflict between records changes a conclusion status. Two apparent differences are complementary.

- RT-RTE-9 says a failed title-check call is skipped, so accuracy is computed over answered checks only. EPI-OBJ-5 says a reply without an answer field counts as no. These are two different failure modes of the same check. Both hold. The reading that combines them is that transport failures drop out of the accuracy and malformed replies count against an entry.
- The runtime member describes the tool budget as 95,000 characters per page-content response. The memory report derives it as 95 percent of a 100,000-character tool limit. The two figures are the same value.

### Independent convergence

None is reported. The memory specialist took the runtime member as provisional findings, and the epistemic member cites RT-ABS-1 for its finding that no evaluation adapts behavior (L10 in its ledger). The agreement of RT-ABS-1, MEM-ABS-1 and the epistemic no-adaptation finding therefore rests on one search family and is not independent. The absences EPI-ABS-1, EPI-ABS-2 and MEM-ABS-2 support different conclusions and do not converge.

### Cross-lens ownership and route checks

- Write route: RT-RTE-1 (flash) and RT-RTE-3 (standard) own writes into the store. The memory annotation on RT-RTE-1 states write agency as automatic and that no history of indexing runs is stored; this matches the runtime persistence description. Merge and expand act on a tree before it is stored (RT-RTE-8, RT-RTE-9), which the memory report correctly excludes from curation of retained memory (MEM-ABS-1).
- Read routes: RT-RTE-2 owns the model-called tools, MEM-RTE-1 owns the one automatic supply, RT-RTE-4 and RT-RTE-5 own host adapters and protocol lanes. Runtime Guarantee A (document scope, `invariant` for chat lanes on a local client with `doc_id`) and MEM-RTE-1 share the caller-supplied `doc_id` as input. The memory report keeps them apart: scoping restricts lookups and MEM-RTE-1 selects content to deliver. This matches the runtime account.
- Untraced citation resolution: the memory report left open whether citation resolution adds a read-back route (its integration issue 6). EPI-RTE-3 traces it. `get_citations` is invoked by a caller, reads only document names and ids from the store's document listing (or one document's metadata), and returns entries to the caller. It does not read stored pages or tree text, and nothing enters the chat model's context through it. It adds no read-back route to the memory profile.
- Bookmark import: embedded bookmark titles are imported into the stored tree (EPI-OBJ-2 into RT-OBJ-1). The memory profile's `imported` lineage value cites only RT-OBJ-2 (page text). The value set is unchanged, since bookmark titles are also imported and lineage stays `authored`, `imported` and `other-compiled`.
- Transient objects: EPI-OBJ-2, EPI-OBJ-4, EPI-OBJ-5, EPI-OBJ-8 and EPI-OBJ-9 exist in memory during indexing and are not retained as such, so they are correctly outside the memory profile's retained storage.
- Behavioral authority: the profile value `knowledge` describes stored content consumed as advisory data by the chat model (RT-BAP-2, MEM-RTE-1). The enforcing verdicts of EPI-BAP-1 act on tree shape at build time and do not make the stored tree a routing or validation authority over a consumer, so they do not add a value.

### Profile against records

The memory report's `memory-comparison` stays in the memory member with its scope, evidence bases, records, coverage assessments and rationale as written. Checked against the whole set:

- `storage_substrate` (`files`, known) matches RT-OBJ-1, RT-OBJ-2, RT-OBJ-3 and MEM-OBJ-1. No record in the set declares a database, vector store or service object inside scope (RT-ABS-4 for vectors).
- `representational_form` (`natural-language`, `symbolic`, known) matches RT-OBJ-1, RT-OBJ-2 and RT-OBJ-3 and the epistemic form fields. No retained parametric object appears (RT-ABS-1).
- `lineage` (`imported`, `other-compiled`, `authored`, known) matches RT-OBJ-2, RT-OBJ-1, RT-OBJ-3 and RT-RTE-1, and EPI-OBJ-2 is another imported content. No route feeds a stored object from a trace, so `trace-extracted` is not a value (MEM-OBJ-1, MEM-ABS-1).
- `behavioral_authority` (`knowledge`, known) matches RT-BAP-2 and MEM-RTE-1. The static instruction text of RT-BAP-1 and RT-OBJ-4 is outside the memory scope, as the memory report states.
- `write_agency` (`automatic`, `manual`, known) matches RT-RTE-1 and the caller-supplied metadata field of RT-OBJ-3. The `manual` value rests on that single field. It stays, with that limit.
- `curation_operations` (`absent`) matches MEM-ABS-1 and RT-ABS-1, whose search was regex-based (see Limitations).
- `read_back_direction` (`pull`, `push`, known) matches RT-RTE-2, RT-RTE-4 and MEM-RTE-1. `read_back_signal` (`identifier`, known) rests on the `doc_id` lookup of MEM-RTE-1, where the selector input is the caller's choice. Nothing in EPI-RTE-3 adds a route.
- `trace_learning` (`"no"`, known), with the four dependent axes inapplicable, matches RT-ABS-1, MEM-ABS-1 and MEM-OBJ-1, as amended above. The basis field is `wired` because the evidence vocabulary has no negative; the memory note states that the negative rests on bounded searches. The reconciliation keeps that encoding and does not read `wired` as a positive route.
- `faithfulness_tested` (`absent`) matches MEM-ABS-2 and agrees with EPI-ABS-1 and EPI-ABS-2 (no fidelity or answer checks in the searched files). The assessment is `absent` rather than a known `"no"` because only the frozen repository was searched.

The scope conflict returned in round 0 is resolved. The specialist chose the reading in which use includes submission: each `submit_document` call adds a retained document and `delete_document` removes one, while querying, tool calls and citation resolution write nothing back and no stored document is edited (RT-RTE-1, RT-ABS-1, MEM-ABS-1). The profile scope, the report prose and the record annotations now state accumulation by submission, not by learning from queries. No evidence basis or status was raised, and the axis values are the ones checked above. The set accepts the reading as a stated choice. It follows the memory type's wording (retained objects accumulated or changed through use) only if submission counts as use, and the store is the only retained state the agent reads. The alternative reading would leave the boundary empty and turn the retained-object axes into `absent` or `inapplicable`; that alternative is kept as a Limitation, not adopted. This means the profile describes a document index accumulated by submission, not an experience memory that changes through querying.

One statement in the memory report is stale after this set's checks: its integration issue 6 says citation resolution reads the store's pages. EPI-RTE-3 and EPI-OBJ-7 show it reads only document names and ids, so it adds no read-back route, as recorded above. The memory report's core ideas, boundary and write side are consistent with the runtime and epistemic members.

## Bounded synthesis

**Evidence basis and boundary.** The analysis covers the open-source PageIndex Python SDK at commit `d2693d80791a86345ef78b3234834f5fe53a70a0` in local mode, whole-system, code-grounded. Every operation conclusion is `uninspected`: no indexing run, test run or model call was made, so everything below about what the code does is implementation reading (SRC-1) and design prose (SRC-2). Accuracy, cost and timing figures are README reports only (SRC-3; RT-CLM-2, RT-CLM-3). The cloud service, the hosted App, host agent runtimes and model providers are outside the boundary.

**Characterization and claimed work.** PageIndex claims to replace vector similarity with an agent that reasons over a document tree (RT-CLM-1) and to run entirely on the caller's machine with the caller's model key (RT-CLM-4). The code supports the local-storage claim at the implementation level and contains no embedding or vector component (RT-ABS-4). Its retrieval claim is a claim about model behavior, which no record here observed.

**Indexing.** A caller submits a PDF. The default flash route (RT-RTE-1) builds a section tree from layout statistics and, by default, embedded bookmarks, then a model writes node summaries and one document description. Bookmarks are validated for range and order and merged by tier (EPI-RTE-1); the flash structure comes from program code, and the model supplies summaries and expand proposals (RT-CMP-1). A refinement pass (RT-RTE-8) lets the model propose child headings for large nodes, keeps a proposal only if its title string occurs in the index-time page text, and then a cost rule expands the node or keeps it collapsed. The standard route (RT-RTE-3) has the model propose the structure and then check its own entries against page text, with accept, repair and fall-back thresholds (RT-RTE-9). Repair can return a tree that still holds entries judged wrong, with no flag in the stored tree (EPI-OBJ-5). The model-written summaries and description are never compared with their pages (EPI-ABS-1, EPI-RTE-2). Scanned or layout-less long PDFs are refused rather than stored in degraded form (RT-RTE-1).

**Storage.** Indexing writes three JSON files per document and a manifest cache: the tree (RT-OBJ-1), the page text from a second extractor (RT-OBJ-2) and metadata with the model-written description and any caller-supplied metadata (RT-OBJ-3). The tree is written before use and never changed by use. The store grows by submission and shrinks by deletion, and a changed document is deleted and resubmitted (RT-ABS-1, MEM-ABS-1). The only other writer is a CLI trace log that nothing reads (MEM-OBJ-1). Index-time text and query-time text come from different parsers and are reconciled only by page-range bounds (EPI-OBJ-9, RT-OBJ-2).

**Query-time retrieval.** A chat call runs a single model agent over four read-only tools that list documents, return an outline without node text, and return page text up to a character budget (RT-RTE-2). Local discovery has no ranking: the model matches document names and descriptions itself. When the caller supplies a document id, code adds that document's metadata as the first user message (MEM-RTE-1) and restricts tool lookups to it. That restriction holds only on the chat lanes of a local client; the host adapters have no document scope and can expose irreversible deletion when the host opts in (RT-RTE-4, RT-RTE-5). The instruction and tool text is prompt-level guidance (RT-BAP-1, RT-OBJ-4). Stored summaries, page text and the description reach the model unframed, so the model reads them as data with no injection defense at query time (RT-ABS-3, RT-BAP-2). The memory profile classifies this store as files, natural-language and symbolic, imported, compiled and authored, read back by pull plus one identifier-selected push, with no curation and no trace learning; the profile treats the store as memory because each submission adds a retained document, and that scope choice is stated in the profile (see Limitations).

**Answers and citations.** With citations requested, the model is instructed to emit page tags. The code resolves each cited document name to an id and does not check that the page exists or supports the claim (EPI-RTE-3, EPI-ABS-2). Answers reach the caller with no check or acceptance step (EPI-OBJ-6). The README's claim of traceable and explainable retrieval (RT-CLM-5) holds for the addressability of a tag, not for verification of the cited statement.

**Theory-builder conditions, learning, reflection, autonomy.** The only stated theory the system applies is the search-cost model in RT-RTE-8. Condition 1 (localized content) is `wired`: the rule and its constants are separately named in one file. Condition 2 (the theory guides what the system does) is `wired`: expansion depends on the formulas. Condition 3 (criticism aimed at the theory's content) is `absent`, and condition 4 (iteration on the result of criticism) is `absent` (RT-ABS-2). The standard-route verify and repair step (RT-RTE-9) is not a theory route. Whether criticism of a consumed theory improved capacity for future action is therefore `absent`, as is learning, and the system is not reflective (RT-ABS-1, RT-ABS-2). Autonomy in RT-RTE-8 is stated role by role: a model proposes, computation decides, the user configures inputs; that description is `wired` and is not a claim of autonomy for the whole system. Self-improvement at the declared boundary is `absent`. Repository commit history, where maintainers may revise these rules, was not examined.

**Scenario-relative assessment.** For a caller who indexes a text-layer PDF and needs a stable, inspectable, per-document tree that a model can navigate, the code delivers one built once, stored as plain files, read through a small read-only tool set, without embedding or ranking machinery. For a scenario in which retrieved content must be correct, PageIndex supplies no verification: summaries, model-verified structure and answers carry no independent check, and the warrant for an answer stays with the caller. For a scenario that expects the system to improve with use, nothing here adapts.

**What would change this assessment.** A run of the indexing routes on PDFs with known outlines, compared with stored summaries and trees, would give observed evidence on structure accuracy and summary fidelity (EPI-ABS-1). A run of the chat lanes with logged tool calls would show whether the model follows the reading workflow and whether the outline changes which pages it reads (RT-RTE-2, MEM-RTE-1). A run comparing answers with and without retrieved pages would test dependence on retrieved content (MEM-ABS-2). The external benchmark repositories, if frozen and tied to this commit, would let the README figures be judged (RT-CLM-2, RT-CLM-3). The hosted service's code or served instructions would be needed for any cloud conclusion (RT-RTE-6, RT-BAP-4).

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No indexing, test or model run was made, so every operation conclusion is uninspected | SRC-1, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5, RT-RTE-7, RT-RTE-8, RT-RTE-9, EPI-RTE-1, EPI-RTE-2, EPI-RTE-3, MEM-RTE-1 | `pageindex/` and `run_pageindex.py` read statically at the frozen commit | Any statement that a route behaves as coded, that models follow the instructions, or that the summaries or outline change answers | Run the test suite, indexing runs and logged chat runs at the frozen commit |
| README accuracy, cost and timing figures come from external benchmark repositories that are not frozen | SRC-3, RT-CLM-2, RT-CLM-3 | `README.md` and chart assets at the frozen commit | Any observed or causal claim about accuracy, cost or comparison with vector retrieval or native PDF input | Freeze the benchmark runners and data at a commit tied to this SDK and run a one-component contrast |
| Example outputs carry no run configuration, model or code revision | SRC-4, RT-OBJ-1 | `examples/documents/results/` at the frozen commit | Attributing the sample trees to the frozen pipeline, a mode or a model | Regenerate sample outputs with a recorded configuration |
| PageIndex Cloud, the hosted App and the cloud MCP server are excluded; only client code was read | RT-RTE-6, RT-BAP-4, RT-CLM-1, RT-CLM-5 | `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py` as the client half | Any conclusion about cloud indexing, storage, ranking, served instructions or the managed chat | Inspect the hosted service or observed cloud runs |
| Host adapters and protocol lanes were read only as far as the tool wrappers; host loops, approvals and persistence belong to host runtimes | RT-RTE-4, RT-RTE-5 | `pageindex/integrations/` and the lane entry points | Host-side memory, approval or retry behavior, and provider prompt-cache behavior | Trace a host runtime that uses the adapters |
| The memory profile treats submission as use, so the document store is inside the memory boundary; under a reading that counts only query-time writes the boundary would be empty | MEM-RTE-1, RT-OBJ-1, RT-OBJ-2, RT-OBJ-3, RT-RTE-1, MEM-ABS-1 | Store and its write and read routes | Any conclusion that PageIndex learns or accumulates memory through querying; and the positive profile values if the stricter reading were used | A type-level ruling on whether submission counts as use, or a comparison set that fixes the boundary rule |
| The `manual` write-agency value rests on one caller-supplied metadata field, and the `identifier` read-back signal on a caller-supplied document id | RT-OBJ-3, MEM-RTE-1 | `pageindex/local_api.py`, `pageindex/agent_tools.py` | Whether these values would survive a stricter reading of retained memory | A stricter definition of retained memory, or a second write route beyond submission |
| The trace-learning negative is encoded with the basis `wired`, because the evidence vocabulary has no negative | RT-ABS-1, MEM-ABS-1, MEM-OBJ-1 | Bounded code searches of `pageindex/` and the CLI | Reading `wired` as a positive route; the negative rests on searches only | A vocabulary value for bounded negatives, or a run showing no trace-fed writes |
| Absences rest on regex searches of listed terms, so an unlisted synonym could be missed | RT-ABS-1, RT-ABS-2, RT-ABS-3, RT-ABS-4, MEM-ABS-1, MEM-ABS-2, EPI-ABS-1, EPI-ABS-2 | The file sets and term lists in each record | Certainty that no write-back, curation, sanitization, vector component or check exists | A different search method or a code review of the same files |
| Repository commit history and human edits to rules were not examined | RT-ABS-2, RT-RTE-8, RT-RTE-9 | Frozen commit only | Whether maintainers revise the cost rule or prompts from evidence over time, which bears on theory-builder conditions 3 and 4 at repository level | Read the commit history and issue record of the rule files |
| Index-time page text (pdfium) and query-time page text (PyPDF2) come from different parsers, and their agreement is unchecked | EPI-OBJ-9, RT-OBJ-2, EPI-OBJ-4 | `pageindex/local_api.py`, `pageindex/flash/` as consumed | Whether a heading confirmed at index time appears in the text the agent reads, and extraction fidelity | Compare the two extractions on sample PDFs |
| Summary and description fidelity, layout heading precision and bookmark correctness were not tested | EPI-OBJ-1, EPI-OBJ-3, EPI-OBJ-8, EPI-OBJ-2 | Consumers of these outputs only | Whether the model-written and detected structure is accurate | Compare stored summaries and trees with their pages and printed outlines |
| The Markdown pipeline was traced only as far as structure, and its output has no shipped reader | RT-RTE-7 | `pageindex/page_index_md.py` and `run_pageindex.py` | Any conclusion about its content routes | Trace the pipeline and any consumer |
| The four amendments correct records that stay unchanged in their members | RT-RTE-2, RT-CLM-5, RT-RTE-8, RT-ABS-1 | This Reconciliation | A reader of a member alone sees the uncorrected wording | Read the amendments with the members |

## Verification and blockers

### Semantic verification

Checked the overview draft, the runtime member, the memory member (byte-identical to the round's memory report, confirmed by file comparison), the epistemic member and the set check against the frozen commit `d2693d80791a86345ef78b3234834f5fe53a70a0`. Source reads were of a `git archive` extraction of that commit in the job scratch directory, not the worktree. The set check lists no structural failure (its content is `none`), so no set-check failure is carried into Blockers.

**Memory comparison against records, per axis.** Each known value was checked against the records the profile cites, and the scope statement against the profile, the records and the prose of all three members.

- Scope agreement: the profile scope, the memory prose, the annotations on RT-OBJ-1, RT-OBJ-2, RT-OBJ-3, RT-RTE-1 and RT-RTE-2, and the Reconciliation all state accumulation by submission, not by learning from queries. The runtime member words the same fact as the persisted product of an indexing run, not accumulation through use (RT-RTE-1, EPI-RTE-2). These differ in the reading of "use", not in fact, and the Reconciliation names the choice and keeps the stricter reading as a Limitation. Accepted.
- `storage_substrate` (`files`): RT-OBJ-1, RT-OBJ-2, RT-OBJ-3 and MEM-OBJ-1 are JSON on disk in `pageindex/local_store.py`; no database, vector or in-memory retained object exists (RT-ABS-4 confirmed by a search of `pageindex/`, `pyproject.toml` and `requirements.txt`: the only hits are PDF-parser terms).
- `representational_form`, `lineage`: consistent with `pageindex/local_api.py` (PyPDF2 page text stored as-is, tree and description model-written, `metadata` stored as given) and with EPI-OBJ-2 for imported bookmark titles.
- `behavioral_authority` (`knowledge`): RT-BAP-2 and MEM-RTE-1 deliver stored content as data; static instruction text (RT-OBJ-4, RT-BAP-1) is outside the scope as stated.
- `write_agency` (`automatic`, `manual`): `submit_document` is the only writer of documents; the `manual` value rests on the caller-supplied `metadata` field alone, and the Reconciliation and Limitations say so.
- `curation_operations` (`absent`): MEM-ABS-1 and RT-ABS-1 hold; merge and expand run on an unstored tree (RT-RTE-8), the `_1` to `_99` suffix is a collision check, and `delete_document` keeps no history.
- `read_back_direction` and `read_back_signal`: the push route is MEM-RTE-1. Trigger is a chat call with `doc_id`, the selector is code, the selector input is the caller's `doc_id`, and the selected part is the whole metadata row of each named document, resolved by `client.get_document` in `doc_targeting_block` in `pageindex/agent_tools.py`. That is an identity match that selects delivered parts, so `identifier` meets the memory type's rule. Its consumer is the chat model in RT-RTE-2 and RT-RTE-5. Pull routes are the four read tools (`_READ_TOOLS`), and `browse_documents` is a newest-first listing with no ranking, so it is not a push signal.
- `trace_learning` (`"no"`, basis `wired`) with the four dependent axes `inapplicable`: matches RT-ABS-1, MEM-ABS-1 and MEM-OBJ-1. There is no compaction, checkpoint or continuation summary, and PageIndex keeps no conversation store (RT-RTE-2, RT-RTE-5). The encoding follows the memory type, which requires a basis entry; the note discloses that the negative rests on searches.
- `faithfulness_tested` (`absent`): MEM-ABS-2 is a bounded absence over the repository. The `tests/` suite stubs the model.

**Every scoped trace-fed write.** None exists. MEM-OBJ-1 is confirmed: `JsonLogger` in `pageindex/utils.py` creates `./logs` and rewrites the file on each log call, and `run_pageindex.py` calls `page_index_main` without a logger in the standard branch. Nothing in `pageindex/` reads it. The SDK path passes a standard-library logger, as MEM-OBJ-1 says.

**Reconciliation dispositions.** The five integration issues of the memory report and the four amendments were each checked.

- Amendment for RT-ABS-1: the CLI trace log is a real additional writer and the conclusion status `absent` stands. See the note on the manifest below.
- Amendment for RT-RTE-2 and amendment for RT-CLM-5: confirmed against `pageindex/client.py`. `get_citations` parses tags, resolves the cited document name to a document id from the caller's `doc_id` or the library listing, and keeps `doc_id: None` for an unknown name. It does not check the page against the store. It reads only names and ids, so no read-back route is added, and the memory report's integration issue 6 is correctly recorded as stale.
- Amendment for RT-RTE-8: confirmed. `propose_children` in `pageindex/tree_optimize.py` keeps a child only when its normalized title is a substring of the normalized page text passed to the optimizer. That text is the flash `page_texts` (pdfium layout parsing), not the stored PyPDF2 pages, so the narrowed guarantee wording is right. `invariant` remains fitting for that string check.
- Supersession and identity checks: EPI-OBJ-1, EPI-OBJ-3, EPI-RTE-1 and EPI-RTE-2 are declared as content-level views of parts of RT-OBJ-1, RT-OBJ-3 and RT-RTE-1, and MEM-RTE-1 as the push step RT-RTE-2 lists without a route. None duplicates a referent, so no supersession is needed.
- Anchored conflicts: RT-RTE-9 skips a failed title check while EPI-OBJ-5 counts a reply without an `answer` field as `no`. Both hold in `check_title_appearance` and `verify_toc` in `pageindex/page_index_classic.py`. The 95,000-character budget equals 95 percent of the 100,000-character limit.
- Independent convergence `none` is correct: the epistemic finding of no adaptation cites RT-ABS-1.

**Source checks of load-bearing facts** (commit-pinned reads):

- RT-RTE-9: accuracy of 1.0 with no incorrect entries accepts; above 0.6 with mistakes goes to `fix_incorrect_toc_with_retries` (three attempts) and the result is returned whether or not mistakes remain; otherwise the mode falls back and the last mode raises. `verify_toc` returns accuracy 0 early when the last located page lies in the first half of the document. All in `pageindex/page_index_classic.py`.
- RT-RTE-8: `TRIGGER_PAGES` is 5, `max_rounds` is 3, empty model answers are retried and then trusted as none, candidates from the model and from a detection cache are priced and the cheapest kept, and the SDK path passes no cache, in `pageindex/tree_optimize.py` and `pageindex/flash/api.py`. `min_gain_ratio` defaults to 0.0, so the runtime wording that code also requires a minimum gain ratio is accurate but the default makes it inactive.
- RT-RTE-1: `flash_rejection_reason` refuses scanned or text-less PDFs and layout-less PDFs over ten nodes; `save_document` writes `tree.json`, `pages.json` and then `doc.json`, and `list_metas` skips a directory without `doc.json`.
- Retry ladder: ten attempts, one second delay, no retry on 400, 401, 403 or 404 in `pageindex/utils.py`. Default models `gpt-5.6-luna` and `gpt-5.6-sol` confirmed.
- Guarantee A and B: `call_tool` in `pageindex/agent_tools.py` drops underscore-prefixed model arguments and builds `_allowed_ids` from `doc_ids`; `remove_document` appears only when `include_management` is true, and the chat lanes in `pageindex/local_chat.py` do not pass it. Tracing is disabled in the run config.
- RT-ABS-3: `_secure_doc_text`, `_SYSTEM_HARDENING` and `user_document` occur only in `pageindex/page_index_classic.py`, and no query-time framing or redaction exists in `pageindex/agent_tools.py` or `pageindex/local_chat.py`.
- EPI-RTE-1: the docstring of `pageindex/flash/embedded_toc.py` calls the feature opt-in while `pageindex/flash/main.py` and `pageindex/local_api.py` default `use_embedded_toc` to true, as the epistemic member states. The FULL tier merges without page text; the SKELETON tier verifies deeper entries against page text.
- Claims: the README lines for RT-CLM-1, RT-CLM-2, RT-CLM-3, RT-CLM-4 and RT-CLM-5 and the traceable, conversation-history and 98.7 percent statements are present in `README.md`; the benchmark runners are external, so `claimed` is right for RT-CLM-2, RT-CLM-3 and RT-CLM-5 and no operation status above `uninspected` appears anywhere in the set.
- Source register: SRC-1, SRC-2, SRC-3 and SRC-4 paths exist at the commit (`README.md`, `pageindex/flash/README.md`, `docs/naming-rules.md`, `assets/results-light.png`, the example results directory). The limitation on SRC-4 provenance holds.

**Boundaries, exclusions, limitations and evidence statuses.** Exclusions each carry a prevented conclusion. Every route status pairs `wired` implementation with `uninspected` operation; no observation, causality or curation-as-warrant upgrade was found. Theory-builder conditions, learning, reflection and autonomy each carry their own status in RT-RTE-8 and the synthesis; condition 3 and condition 4 rest on RT-ABS-2, and the synthesis states that commit history was not examined. The Limitations table covers the stale-member wording, the scope choice, the encoding of the trace-learning negative and the regex-search caveat.

**Non-blocking imprecisions.** None changes a status, a profile value or a conclusion, and each is a scope or wording point that a later reader should know.

- Query-time manifest rewrite: `list_metas` in `pageindex/local_store.py`, reached by `list_documents` in `pageindex/local_api.py` and so by `browse_documents`, rewrites `manifest.json` when the cache differs from the `doc.json` files. The statements that querying writes nothing back (memory profile scope, RT-ABS-1 as amended, MEM-ABS-1) and that `save_document` and `delete_document` are the only store writers are therefore true of documents, trees, pages and descriptions but not of the manifest cache. RT-OBJ-3 already records the manifest as a cache with no independent content, so no axis value depends on it (curation, trace learning and write agency are unaffected). Affects RT-ABS-1, MEM-ABS-1, RT-OBJ-3.
- Guarantee C in the runtime member attributes the re-raised exceptions to `call_tool`. The re-raise belongs to the cloud bridge invoker in `pageindex/agent_tools.py`; on a local client `call_tool` catches every exception. The guarantee strength `best effort` is conservative for local mode and the cloud limit is stated.
- The runtime member gives the test suite as about 11,000 lines; `tests/*.py` counts about 12,400. Not load-bearing.
- RT-CLM-3 states that the linked blog names Mafin 2.5; the blog is outside the boundary, so this comes from the link address in `README.md`. The hedge that it may not be this SDK is present.
- The scenario-relative assessment says the code delivers a tree that a model can navigate; this is implementation-level wording, and the same paragraph and the evidence-basis paragraph state that operation is uninspected.

### Deterministic validation

`commonplace-validate kb/reports/state/agentic-system-analysis/AAS-2026-09-29-pageindex-02/output --full` runs after the manifest is written, over every member, the manifest and the set's cross-member checks; code publishes only when it passes, and publication runs it again.

### Blockers

none
